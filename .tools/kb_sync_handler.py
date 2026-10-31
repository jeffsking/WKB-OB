#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kb_sync_handler.py — IMA → Obsidian 知识管道 · 阶段 B 落地器（第 2 批）

职责（设计依据 .tools/IMA_DAILY_PIPELINE_DESIGN_v2_2026-10-11.md §5）：
  把「账本 stage=discovered、RAW 有占位、RAW_FULL 无正文」的条目，按通道分级抓正文落盘。

通道分级（§5 表）：
  A  MCP  fetch_media_content  无日配额   笔记/录音/session/网页 (media_type ∈ {11,12,15,20,2})
  B  REST get_media_info → 签名 URL → GET 宽松  无文字层原件（图纸/扫描 PDF/Office/CSV），含录音音频
  C  REST get_doc_content      受日配额   仅兜底，命中 200005 即当日放弃，禁止循环重试

实测（2026-10-11）：本会话 IMA MCP connector 可用 -> 走通道 A。
  MCP 调用在 Agent 会话内执行（脚本无法直连 trpc），故本脚本采用
  「Agent 枚举/抓取 → 落 JSON → 脚本合并落盘」的 relay 契约（同 ima_sync_state.py enumerate）。

子命令：
  plan    扫描账本，产出待回填清单（含通道分配），落 _kb_sync_plan.json
  apply   吃 Agent 抓取结果 JSON，写 RAW_FULL 正文 + 更新账本 stage
  gaps    覆盖缺口报告（对账 ima_note_backfill.py / 账本 / wkb_dedup.py 三方口径）
  status  一行摘要

铁律（不可破）：
  1. 正文一律写 RAW_FULL/<同相对路径>，绝不写 RAW/（只读红线）
  2. extract_status ∈ {ok, empty, original-only} 即终态，不重跑
  3. 录音（type 15）双落盘：<50MB 落转写文本+音频原件；≥50MB 只落文本
  4. 幂等：目标已存在且终态 -> skip
"""

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / ".tools"
RAW = ROOT / "RAW"
RAW_FULL = ROOT / "RAW_FULL"
STATE = TOOLS / "_ima_sync_state.json"
PLAN = TOOLS / "_kb_sync_plan.json"
RESULT = TOOLS / "_kb_sync_result.json"

AUDIO_ORIGINAL_MAX_MB = 50  # §5.1

# media_type -> 通道
CHANNEL_BY_TYPE = {11: "A", 12: "A", 15: "A", 20: "A", 2: "A"}
# 无文字层/原件类前缀 -> 通道 B
ORIGINAL_PREFIXES = {"img", "pdf", "word", "ppt", "excel"}

# 前缀 -> 显示名
PREFIX_LABEL = {
    "note": "笔记", "soundrecording": "录音", "session": "session",
    "html": "html", "weburl": "网页", "markdown": "Markdown",
    "pdf": "PDF", "word": "Word", "ppt": "PPT", "excel": "Excel",
    "img": "图片", "wechatarticle": "微信公众号文章",
}

TERMINAL = ("ok", "empty", "original-only")


def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def today():
    return datetime.now().strftime("%Y-%m-%d")


def rel(p):
    return str(Path(p).relative_to(ROOT)).replace("\\", "/")


def read_text(p):
    try:
        return Path(p).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def fm_field(text, field):
    m = re.search(rf'^{field}\s*:[ \t]*["\']?(.*?)["\']?[ \t]*$', text, re.M)
    return m.group(1).strip() if m else None


def full_body_ok(fp):
    """RAW_FULL 侧是否已达终态（有正文 / 明确标记无正文 / 原件独立落盘）。"""
    if not os.path.isfile(fp):
        return False
    t = read_text(fp)
    st = fm_field(t, "extract_status")
    return st in TERMINAL


def prefix_of(media_id):
    return media_id.split("_")[0] if "_" in media_id else "num"


def media_type_of(media_id, entry):
    """从账本 media_type 或 media_id 前缀推断通道归属。"""
    mt = entry.get("media_type")
    if isinstance(mt, int):
        return mt
    return None


def channel_for(media_id, entry):
    pfx = prefix_of(media_id)
    mt = entry.get("media_type")
    if mt in CHANNEL_BY_TYPE:
        return CHANNEL_BY_TYPE[mt], "type"
    if pfx in ORIGINAL_PREFIXES:
        return ("A" if pfx == "note" else "B"), "prefix"
    # 笔记前缀（note_ 哈希型）虽 media_type 未知，仍走通道 A
    if pfx in ("note", "soundrecording", "session", "html", "weburl", "wechatarticle"):
        return "A", "prefix"
    return "B", "prefix-default"


def raw_to_full(raw_path):
    """RAW/... -> RAW_FULL/..."""
    assert raw_path.startswith("RAW/"), raw_path
    return "RAW_FULL/" + raw_path[len("RAW/"):]


# 文件名非法字符（Windows）。含这些字符的标题不可类推绑定（插件会把 / 换成 _，
# 但换法不唯一，凭猜绑定 = 制造幽灵锚点）。
ILLEGAL_FS_CHARS = set('/\\:*?"<>|')


def expected_raw_path(it):
    """raw_path 缺失时，按 kb_path + 插件命名惯例推导「预期 RAW 锚点」。

    惯例依据（库内 400+ 存量样本，2026-10-24 首次标定）：
      kb_path 形如 `ima_sync/个人知识库/WKB/<链>`（不带 RAW/ 前缀）
      预期 RAW 路径 = `RAW/<kb_path>.md`
        · 标题已含 .md（markdown 类）→ 插件再追加一次 → 实为本条 `.md.md`
        · 其它（docx/pdf/ppt/录音/公众号…）→ 原件名 + `.md` 索引壳

    返回 (path|None, reason)。None 表示不可绑定（缺 kb_path / 标题含非法字符）。
    ⚠ 预期路径 ≠ 插件实落名。插件恢复落盘后必须复核实落名，不符则三处同步修
      （RAW_FULL 镜像 / 账本 raw_path·full_path / WIKI source_path），禁建重复页。
    """
    kb = (it.get("kb_path") or "").replace("\\", "/").strip()
    if not kb:
        return None, "kb_path 为空"
    title = it.get("title") or ""
    bad = [c for c in ILLEGAL_FS_CHARS if c in title]
    if bad:
        return None, f"标题含非法文件名字符 {bad}，不可类推绑定"
    if kb.startswith("RAW/"):
        kb = kb[4:]
    return "RAW/" + kb.rstrip("/") + ".md", "expected"


# ---------------------------------------------------------------- plan

def cmd_plan(args):
    if not STATE.exists():
        print("[!] 账本不存在，请先跑 ima_sync_state.py init")
        return 1
    s = json.loads(STATE.read_text(encoding="utf-8"))
    items = s.get("items", {})

    todo, done, unbound, rebound = [], 0, [], []
    for mid, it in items.items():
        if it.get("stage") != "discovered":
            continue
        rp = it.get("raw_path")
        if not rp:
            # 修复 2026-10-11 起的「plan 空 raw_path 盲区」：插件零落盘时新条目
            # 永远进不了计划。改为按 kb_path 推导预期锚点并回写账本，标注来源。
            rp, why_bad = expected_raw_path(it)
            if not rp:
                unbound.append((mid, it.get("title") or "", why_bad))
                continue
            it["raw_path"] = rp
            it["raw_path_source"] = "expected"
            it["raw_path_bound"] = today()
            rebound.append((mid, rp))
        fp = raw_to_full(rp)
        if full_body_ok(str(ROOT / fp)):
            done += 1
            continue
        ch, why = channel_for(mid, it)
        todo.append({
            "media_id": mid,
            "prefix": prefix_of(mid),
            "type_label": PREFIX_LABEL.get(prefix_of(mid), prefix_of(mid)),
            "media_type": it.get("media_type"),
            "title": it.get("title") or "",
            "raw_path": rp,
            "full_path": fp,
            "kb_path": it.get("kb_path"),
            "channel": ch,
            "channel_basis": why,
        })

    todo.sort(key=lambda x: (x["channel"], x["type_label"], x["full_path"]))
    payload = {
        "generated": now_iso(),
        "count": len(todo),
        "already_terminal": done,
        "note": "待回填条目；channel A=MCP fetch_media_content, B=REST get_media_info 原件下载",
        "items": todo,
    }
    PLAN.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    if rebound or unbound:
        for mid, rp in rebound:
            items[mid]["full_path"] = raw_to_full(rp)
        s.setdefault("stage_log", []).append({
            "at": now_iso(), "stage": "B-plan",
            "raw_path_expected_bound": len(rebound),
            "raw_path_unbound": len(unbound)})
        STATE.write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[plan] 待回填 {len(todo)} 条（账本 discovered；已终态 {done} 条）")
    if rebound:
        print(f"       [锚点] 按 kb_path 推导预期 RAW 路径并回写 {len(rebound)} 条"
              f"（标记 raw_path_source=expected，插件落盘后须复核）")
        for mid, rp in rebound:
            print(f"         + {rp.split('/')[-1]}")
    if unbound:
        print(f"       [!] 无法绑定锚点 {len(unbound)} 条（需人工处理）")
        for mid, t, why in unbound:
            print(f"         - {t[:60]} :: {why}")
    print(f"       已写 {rel(PLAN)}")
    for ch in ("A", "B"):
        sub = [x for x in todo if x["channel"] == ch]
        if not sub:
            continue
        print(f"  通道 {ch}: {len(sub)} 条")
        for k, v in Counter(x["type_label"] for x in sub).most_common():
            print(f"      {k}: {v}")
    return 0


# ---------------------------------------------------------------- apply

def write_body(item, body, extract_status, agent_meta):
    """写 RAW_FULL 正文（幂等）。返回 (action, path)。"""
    fp = ROOT / item["full_path"]
    if os.path.isfile(fp) and full_body_ok(str(fp)):
        return "skip-terminal", item["full_path"]
    fp.parent.mkdir(parents=True, exist_ok=True)
    raw = read_text(ROOT / item["raw_path"])
    # 从 RAW 占位 front matter 继承关键字段
    src = fm_field(raw, "source") or ""
    ts = item.get("media_type")
    lines = [
        "---",
        f'media_id: "{item["media_id"]}"',
        f'extract_status: "{extract_status}"',
        f'extract_channel: "{item["channel"]}"',
        f'synced_at: "{now_iso()}"',
        f'source_path: "{item["raw_path"]}"',
    ]
    if src:
        lines.append(f'source: "{src}"')
    if ts is not None:
        lines.append(f"media_type: {ts}")
    for k, v in (agent_meta or {}).items():
        if v in (None, ""):
            continue
        lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {item['title']}")
    lines.append("")
    lines.append(body.rstrip())
    lines.append("")
    fp.write_text("\n".join(lines), encoding="utf-8")
    return "written", item["full_path"]


def update_ledger(done_mids):
    if not done_mids or not STATE.exists():
        return
    s = json.loads(STATE.read_text(encoding="utf-8"))
    items = s.get("items", {})
    n = 0
    for mid in done_mids:
        if mid in items and items[mid].get("stage") == "discovered":
            items[mid]["stage"] = "synced"
            n += 1
    STAGE_LOG = s.setdefault("stage_log", [])
    STAGE_LOG.append({"at": now_iso(), "stage": "B", "synced": n})
    STATE.write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[apply] 账本 stage discovered->synced: {n} 条")


def cmd_apply(args):
    """
    两种输入形态（二选一）：

    ① --input <result.json>：
    {
      "results": [
        {"media_id": "...", "extract_status": "ok|empty|original-only",
         "body": "正文 markdown（ok 时必填）",
         "meta": {"extract_method": "...", "audio_bytes": 1234567, ...}}
      ]
    }

    ② --bodies-dir <dir>：目录下每个文件名为 <media_id>.md（内容即正文），
       <media_id>.json 可选（存 meta）。适合正文超长、逐条落盘的场景。
       extract_status 默认 ok；可在 <media_id>.json 里覆盖。
    """
    if not args.input and not args.bodies_dir:
        print("[!] 需 --input <result.json> 或 --bodies-dir <dir>")
        print(json.dumps({
            "results": [{
                "media_id": "note_...",
                "extract_status": "ok",
                "body": "# 正文\n...",
                "meta": {"extract_method": "MCP fetch_media_content"},
            }]
        }, ensure_ascii=False, indent=2))
        return 1
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    by_mid = {x["media_id"]: x for x in plan["items"]}

    results = []
    if args.bodies_dir:
        d = Path(args.bodies_dir)
        for f in sorted(d.glob("*.md")):
            mid = f.stem
            body = f.read_text(encoding="utf-8", errors="replace")
            meta = {}
            jf = d / f"{mid}.json"
            st = "ok"
            if jf.exists():
                j = json.loads(jf.read_text(encoding="utf-8"))
                meta = j.get("meta") or {}
                st = j.get("extract_status") or "ok"
            results.append({"media_id": mid, "extract_status": st,
                            "body": body, "meta": meta})
    else:
        results = json.loads(Path(args.input).read_text(encoding="utf-8")).get("results", [])

    written = skipped = failed = 0
    done_mids = []
    log = []
    for r in results:
        mid = r.get("media_id")
        it = by_mid.get(mid)
        if not it:
            # 不在待办清单：要么本批已落盘（暂存残留），要么真异常。判终态区分。
            log.append({"media_id": mid, "action": "already-done-or-unplanned"})
            skipped += 1
            continue
        st = r.get("extract_status")
        if st not in TERMINAL:
            log.append({"media_id": mid, "action": "bad-status", "status": st})
            failed += 1
            continue
        body = r.get("body") or ""
        if st == "ok" and not body.strip():
            log.append({"media_id": mid, "action": "empty-body-for-ok"})
            failed += 1
            continue
        act, path = write_body(it, body, st, r.get("meta"))
        log.append({"media_id": mid, "action": act, "path": path, "status": st})
        if act == "written":
            written += 1
            done_mids.append(mid)
        else:
            skipped += 1
            done_mids.append(mid)

    update_ledger(done_mids)
    RESULT.write_text(json.dumps({
        "at": now_iso(), "written": written, "skipped": skipped,
        "failed": failed, "log": log,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[apply] 写入 {written} · 跳过 {skipped} · 失败 {failed}")
    print(f"        已写 {rel(RESULT)}")
    return 0


# ---------------------------------------------------------------- gaps

def cmd_gaps(args):
    """三方口径对账：账本 / ima_note_backfill / wkb_dedup。"""
    print("=" * 64)
    print("阶段 B 缺口对账（三方口径）")
    print("=" * 64)
    # 1) 账本
    if STATE.exists():
        s = json.loads(STATE.read_text(encoding="utf-8"))
        items = s.get("items", {})
        c = Counter(it.get("stage") for it in items.values())
        print(f"[账本] 总 {len(items)}  " +
              "  ".join(f"{k}={v}" for k, v in sorted(c.items())))
        disc = [(m, i) for m, i in items.items() if i.get("stage") == "discovered"]
        pre = Counter(prefix_of(m) for m, _ in disc)
        print(f"       discovered 前缀分布: {dict(pre)}")
    # 2) RAW_FULL 覆盖
    n_raw = n_full = 0
    for f in RAW.rglob("*.md"):
        t = read_text(f)
        if fm_field(t, "media_id"):
            n_raw += 1
            fp = ROOT / raw_to_full(rel(f))
            if os.path.isfile(fp) and full_body_ok(str(fp)):
                n_full += 1
    print(f"[RAW_FULL] RAW 带 media_id {n_raw} · 已终态正文 {n_full} · 缺口 {n_raw - n_full}")
    # 3) wkb_dedup
    dedup = TOOLS / "wkb_dedup.py"
    if dedup.exists():
        import subprocess
        r = subprocess.run([sys.executable, str(dedup), "scan"],
                           capture_output=True, text=True, encoding="utf-8")
        for ln in (r.stdout or "").splitlines():
            if "真实未编译" in ln or "已编译" in ln and "条" in ln:
                print(f"[wkb_dedup] {ln.strip()}")
    return 0


def cmd_status(args):
    if not STATE.exists():
        print("[!] 账本不存在")
        return 1
    s = json.loads(STATE.read_text(encoding="utf-8"))
    items = s.get("items", {})
    c = Counter(it.get("stage") for it in items.values())
    print(f"账本 {len(items)} 条: " + "  ".join(f"{k}={v}" for k, v in sorted(c.items())))
    if PLAN.exists():
        p = json.loads(PLAN.read_text(encoding="utf-8"))
        print(f"待回填计划: {p.get('count')} 条（{p.get('generated')}）")
    return 0


def main():
    ap = argparse.ArgumentParser(description="阶段 B 落地器")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("plan")
    p_apply = sub.add_parser("apply")
    p_apply.add_argument("--input")
    p_apply.add_argument("--bodies-dir", dest="bodies_dir")
    sub.add_parser("gaps")
    sub.add_parser("status")
    a = ap.parse_args()
    if a.cmd == "plan":
        return cmd_plan(a)
    if a.cmd == "apply":
        return cmd_apply(a)
    if a.cmd == "gaps":
        return cmd_gaps(a)
    if a.cmd == "status":
        return cmd_status(a)
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())

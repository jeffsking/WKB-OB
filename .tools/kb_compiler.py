#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kb_compiler.py — IMA → Obsidian 知识管道 · 阶段 C 编译器（第 3 批）

职责（设计依据 .tools/IMA_DAILY_PIPELINE_DESIGN_v2_2026-10-11.md §6 + AGENTS.md §2.3/§3）：
  把「账本 stage=synced（RAW_FULL 已有正文、WIKI 无源摘要页）」的条目，
  编译为 WIKI/sources/ 源摘要页。

为什么是 relay 而非全自动：
  源摘要页的核心（定位/摘要/关键论断）是**语义提炼**，必须由 LLM 读正文后产出；
  脚本无法凭空生成高质量摘要。故本脚本只做：
    plan    从账本挑出「synced 且 wkb_dedup 未登记」的条目 → 待编译清单
    apply   吃 Agent 写好的源摘要页（front matter + 正文）→ 校验 + 落 WIKI/sources/
    stub    为「正文极短/无文字层」的条目生成 minimal 源摘要页（机工可完成的部分）
    verify  编译后与 wkb_dedup.py scan 对账，确认未编译数下降

铁律（AGENTS.md，不可破）：
  1. source_path 一律指 RAW/（禁 RAW_FULL 锚）
  2. 幂等：WIKI 已存在同名源摘要页 -> skip
  3. 编译后必须与 wkb_dedup.py 对账（唯一「已编译」判定入口）
  4. 一个页面只讲一个主题；英文为主 + 中文对照（§2.0）
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / ".tools"
RAW = ROOT / "RAW"
RAW_FULL = ROOT / "RAW_FULL"
WIKI_SOURCES = ROOT / "WIKI" / "sources"
STATE = TOOLS / "_ima_sync_state.json"
DEDUP = TOOLS / "wkb_dedup.py"
PLAN = TOOLS / "_kb_compile_plan.json"
PAGES_IN = TOOLS / "_kb_compile_pages"   # Agent 写好的源摘要页暂存目录
RESULT = TOOLS / "_kb_compile_result.json"

PREFIX_TO_SOURCE_TYPE = {
    "note": "会议纪要",
    "wechatarticle": "公众号",
    "weburl": "行业新闻",
    "pdf": "研报",
    "word": "研报",
    "ppt": "研报",
    "excel": "报价单",
    "img": "行业新闻",
    "soundrecording": "会议纪要",
    "session": "会议纪要",
}

STUB_MIN_BODY = 200  # 正文短于此值 → 只能建 minimal 页


def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def today():
    return datetime.now().strftime("%Y-%m-%d")


def rel(p):
    return str(Path(p).relative_to(ROOT)).replace("\\", "/")


def raw_to_full(raw_path):
    assert raw_path.startswith("RAW/"), raw_path
    return "RAW_FULL/" + raw_path[len("RAW/"):]


def prefix_of(media_id):
    return media_id.split("_")[0] if "_" in media_id else "num"


# --------------------------------------------------- wkb_dedup 索引

def dedup_index():
    """调用 wkb_dedup.build_index 取得已登记 RAW 路径集（权威判重）。"""
    sys.path.insert(0, str(TOOLS))
    import importlib
    mod = importlib.import_module("wkb_dedup")
    importlib.reload(mod)
    idx, merged = mod.build_index(verbose=False)
    return set(idx.keys()), merged


def safe_name(kb_path, title):
    """源摘要页文件名：用标题（去掉扩展名）+ 去非法字符。"""
    stem = title or Path(kb_path).stem
    stem = re.sub(r"\.(md|docx?|pptx?|xlsx?|pdf)$", "", stem, flags=re.I)
    stem = re.sub(r'[\\/:*?"<>|]', "-", stem).strip()
    return (stem or "untitled")[:120]


# --------------------------------------------------- plan

def cmd_plan(args):
    if not STATE.exists():
        print("[!] 账本不存在")
        return 1
    s = json.loads(STATE.read_text(encoding="utf-8"))
    items = s.get("items", {})
    idx, _ = dedup_index()
    # 归一：wkb_dedup 用 os.path.normpath，Windows 下是反斜杠；统一成正斜杠比对
    idx_norm = {p.replace("\\", "/") for p in idx}

    todo = []
    for mid, it in items.items():
        if it.get("stage") not in ("synced",):
            continue
        rp = it.get("raw_path")
        if not rp or rp.replace("\\", "/") in idx_norm:
            continue
        fp = ROOT / raw_to_full(rp)
        if not fp.is_file():
            continue
        body = fp.read_text(encoding="utf-8", errors="replace")
        # 去掉 front matter 后取正文长度
        core = body.split("---", 2)[-1] if body.startswith("---") else body
        todo.append({
            "media_id": mid,
            "prefix": prefix_of(mid),
            "source_type": PREFIX_TO_SOURCE_TYPE.get(prefix_of(mid), "行业新闻"),
            "title": it.get("title") or Path(rp).stem,
            "raw_path": rp.replace("\\", "/"),
            "full_path": raw_to_full(rp).replace("\\", "/"),
            "page_name": safe_name(rp, it.get("title")),
            "body_chars": len(core.strip()),
            "stub_only": len(core.strip()) < STUB_MIN_BODY,
        })

    todo.sort(key=lambda x: (x["stub_only"], x["source_type"], x["raw_path"]))
    payload = {
        "generated": now_iso(),
        "count": len(todo),
        "stub_only": sum(1 for x in todo if x["stub_only"]),
        "note": "待编译源摘要页；stub_only=True 的正文过短，只能建 minimal 页",
        "items": todo,
    }
    PLAN.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"[plan] 待编译 {len(todo)} 条（其中 minimal {payload['stub_only']} 条）")
    print(f"       已写 {rel(PLAN)}")
    for k, v in Counter(x["source_type"] for x in todo).most_common():
        print(f"   {k}: {v}")
    return 0


# --------------------------------------------------- apply

PAGE_HEAD = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.S)


def parse_page(text):
    m = PAGE_HEAD.match(text)
    if not m:
        return None, None
    return m.group(1), m.group(2)


def fm_val(fm, key):
    m = re.search(rf'^{key}\s*:[ \t]*["\']?(.*?)["\']?[ \t]*$', fm, re.M)
    return m.group(1).strip() if m else None


def build_front_matter(item, extra=None):
    t = item["title"]
    lines = [
        "---",
        "type: source",
        f'title: "{t}"',
        f"source_type: {item['source_type']}",
        f"source_path: {item['raw_path']}",
        'original_link: ""',
        f"date_published: {today()}",
        f"date_processed: {today()}",
        "credibility: 中",
        "knowledge_update_status: pending",
        "key_claims: []",
        "pages_linked: []",
    ]
    lines.append("---")
    return "\n".join(lines)


def update_ledger_compiled(done_mids):
    """把已编译条目的账本 stage 提升为 compiled 并记 source_page_hint。"""
    if not done_mids or not STATE.exists():
        return
    s = json.loads(STATE.read_text(encoding="utf-8"))
    items = s.get("items", {})
    n = 0
    for mid, page in done_mids:
        if mid in items and items[mid].get("stage") == "synced":
            items[mid]["stage"] = "compiled"
            items[mid]["source_page_hint"] = page
            n += 1
    s.setdefault("stage_log", []).append(
        {"at": now_iso(), "stage": "C", "compiled": n})
    STATE.write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[apply] 账本 stage synced->compiled: {n} 条")


def cmd_apply(args):
    """把 Agent 写在 _kb_compile_pages/<media_id>.md 的完整页面落到 WIKI/sources/。"""
    src_dir = Path(args.input) if args.input else PAGES_IN
    if not src_dir.exists():
        print(f"[!] 暂存目录不存在：{rel(src_dir)}")
        return 1
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    by_mid = {x["media_id"]: x for x in plan["items"]}

    written = skipped = failed = 0
    log = []
    done_mids = []
    for f in sorted(src_dir.glob("*.md")):
        mid = f.stem
        it = by_mid.get(mid)
        if not it:
            # 不在待办清单：多为本批已落盘的暂存残留（plan 已剔除），计为 skip
            log.append({"media_id": mid, "action": "already-done-or-unplanned"})
            skipped += 1
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_page(text)
        if fm is None:
            log.append({"media_id": mid, "action": "no-front-matter"})
            failed += 1
            continue
        sp = fm_val(fm, "source_path")
        if not sp or sp.replace("\\", "/") != it["raw_path"]:
            log.append({"media_id": mid, "action": "bad-source-path",
                        "got": sp, "want": it["raw_path"]})
            failed += 1
            continue
        dest = WIKI_SOURCES / f"{it['page_name']}.md"
        if dest.exists():
            log.append({"media_id": mid, "action": "skip-exists",
                        "path": rel(dest)})
            skipped += 1
            done_mids.append((mid, rel(dest)))
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        log.append({"media_id": mid, "action": "written", "path": rel(dest)})
        written += 1
        done_mids.append((mid, rel(dest)))

    update_ledger_compiled(done_mids)
    RESULT.write_text(json.dumps({
        "at": now_iso(), "written": written, "skipped": skipped,
        "failed": failed, "log": log,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[apply] 写入 {written} · 跳过 {skipped} · 失败 {failed}")
    print(f"        已写 {rel(RESULT)}")
    return 0


# --------------------------------------------------- stub

def cmd_stub(args):
    """为正文过短条目生成 minimal 源摘要页（机工可完成部分）。"""
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    n = 0
    for it in plan["items"]:
        if not it["stub_only"]:
            continue
        dest = WIKI_SOURCES / f"{it['page_name']}.md"
        if dest.exists():
            continue
        if not args.write:
            print(f"  [stub] {it['title'][:50]}  ({it['body_chars']} chars)")
            n += 1
            continue
        fm = build_front_matter(it)
        body = (
            f"# {it['title']}\n\n"
            f"## Positioning 定位\n\n"
            f"Auto-generated minimal source page（正文过短/无文字层，{it['body_chars']} chars）。\n\n"
            f"## Original 原文\n\n"
            f"- 本地路径：`{it['raw_path']}`\n"
            f"- 镜像正文：`{it['full_path']}`\n"
        )
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(fm + "\n\n" + body, encoding="utf-8")
        n += 1
    verb = "已写" if args.write else "待写"
    print(f"[stub] {verb} {n} 条 minimal 源摘要页")
    return 0


# --------------------------------------------------- verify

def cmd_verify(args):
    print("=" * 64)
    print("阶段 C 编译对账")
    print("=" * 64)
    idx, _ = dedup_index()
    print(f"[wkb_dedup] 已登记 RAW 路径：{len(idx)}")
    if DEDUP.exists():
        r = subprocess.run([sys.executable, str(DEDUP), "scan"],
                           capture_output=True, text=True, encoding="utf-8")
        for ln in (r.stdout or "").splitlines():
            if "真实未编译" in ln or "已编译" in ln or "RAW 条目数" in ln:
                print(f"[wkb_dedup] {ln.strip()}")
    if STATE.exists():
        s = json.loads(STATE.read_text(encoding="utf-8"))
        c = Counter(it.get("stage") for it in s.get("items", {}).values())
        print("[账本] " + "  ".join(f"{k}={v}" for k, v in sorted(c.items())))
    return 0


def cmd_status(args):
    if PLAN.exists():
        p = json.loads(PLAN.read_text(encoding="utf-8"))
        print(f"待编译计划：{p.get('count')} 条（minimal {p.get('stub_only')}）· {p.get('generated')}")
    else:
        print("尚无编译计划，先跑 plan")
    if PAGES_IN.exists():
        print(f"暂存待落页面：{len(list(PAGES_IN.glob('*.md')))} 个")
    return 0


def main():
    ap = argparse.ArgumentParser(description="阶段 C 编译器")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("plan")
    p_apply = sub.add_parser("apply")
    p_apply.add_argument("--input", help="可选：从其他暂存目录读页面")
    p_stub = sub.add_parser("stub")
    p_stub.add_argument("--write", action="store_true")
    sub.add_parser("verify")
    sub.add_parser("status")
    a = ap.parse_args()
    if a.cmd == "plan":
        return cmd_plan(a)
    if a.cmd == "apply":
        return cmd_apply(a)
    if a.cmd == "stub":
        return cmd_stub(a)
    if a.cmd == "verify":
        return cmd_verify(a)
    if a.cmd == "status":
        return cmd_status(a)
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())

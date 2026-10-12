#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IMA 条目正文回填 —— 清单生成 / 切片 / 验收（方案 A + C 的地基）

背景（2026-10-10 根因定位）：
  Obsidian 插件 ima-copilot-sync v6.6.0 只有一条取正文通道
  openapi/note/v1/get_doc_content，受当日配额限制（超量返回 200005），
  且把配额错误误判为永久失败 → 写占位符；占位符含 media_id，
  主循环 `if (a.has(i.media_id)) continue` 使其**永不重试**。

  合法可用通道：
    · 会话内 MCP  fetch_media_content   ← 不受 REST 日配额限制（实测有效）
    · REST get_doc_content              ← 受配额，仅作兜底

  落盘约定：正文写 RAW_FULL/ 同相对路径（RAW/ 为只读红线），
  幂等键 = RAW 占位符 front matter 里的 media_id。

用法：
  python ima_note_backfill.py --scan             生成缺口清单
  python ima_note_backfill.py --slices 15        切分为子代理任务片
  python ima_note_backfill.py --verify           覆盖率报告
  python ima_note_backfill.py --status           一行摘要
"""

import argparse
import datetime
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "RAW")
RAW_FULL = os.path.join(ROOT, "RAW_FULL")
TOOLS = os.path.join(ROOT, ".tools")

GAP_JSON = os.path.join(TOOLS, "_ima_note_gap.json")
SLICE_DIR = os.path.join(TOOLS, "_ima_note_slices")

UNSUPPORTED_MARK = "暂不支持自动同步内容"
PLACEHOLDER_STUB_MAX = 600  # 小于此值视为占位壳

MD_RE = re.compile(r'media_id["\']?\s*[:=]\s*["\']?([A-Za-z0-9_+/=-]+)')
TYPE_RE = re.compile(r"此条目为(.{1,12}?)，暂不支持")
TITLE_RE = re.compile(r"\*\*标题\*\*:\s*(.+)")

TYPE_LABEL = {
    "11": "笔记",
    "12": "类型 12 (session)",
    "15": "类型 15 (录音)",
    "20": "类型 20 (html)",
    "2": "网页",
}
PREFIX_LABEL = {
    "note": "笔记", "soundrecording": "类型 15 (录音)", "session": "类型 12 (session)",
    "html": "类型 20 (html)", "weburl": "网页", "markdown": "Markdown",
    "pdf": "PDF", "word": "Word 文档", "ppt": "PPT", "excel": "Excel",
    "img": "图片", "wechatarticle": "微信公众号文章",
}


def rel(p):
    return os.path.relpath(p, ROOT).replace("\\", "/")


def full_path_for(raw_path):
    """RAW/... → RAW_FULL/..."""
    r = rel(raw_path)
    assert r.startswith("RAW/"), r
    return os.path.join(ROOT, "RAW_FULL" + r[len("RAW"):])


def read_text(p):
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def full_body_ok(p):
    """RAW_FULL 侧是否已处理过（有正文，或已明确标记 IMA 侧无正文）

    注意：不能只看体积。`extract_status: empty` 的合法落盘（如无文字层的
    .jmp 数据文件、空录音）体积很小，但已处理完毕，不得反复重跑。
    """
    if not os.path.isfile(p):
        return False
    t = read_text(p)
    if UNSUPPORTED_MARK in t:
        return False
    if re.search(r'extract_status:\s*"(ok|empty|original-only)"', t):
        return True
    return os.path.getsize(p) >= PLACEHOLDER_STUB_MAX


def collect():
    items = []
    for dirpath, _dirnames, filenames in os.walk(RAW):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            t = read_text(p)
            m = MD_RE.search(t)
            media_id = m.group(1) if m else ""
            if not media_id:
                continue
            prefix = media_id.split("_")[0] if "_" in media_id else "num"
            if UNSUPPORTED_MARK in t:
                kind = "unsupported"
                tm = TYPE_RE.search(t)
                label = tm.group(1).strip() if tm else PREFIX_LABEL.get(prefix, prefix)
            elif len(t) < PLACEHOLDER_STUB_MAX:
                kind = "attach_stub"
                label = PREFIX_LABEL.get(prefix, prefix)
            else:
                kind = "has_body"
                label = PREFIX_LABEL.get(prefix, prefix)
            tm2 = TITLE_RE.search(t)
            title = tm2.group(1).strip() if tm2 else os.path.splitext(fn)[0]
            fp = full_path_for(p)
            items.append({
                "media_id": media_id,
                "prefix": prefix,
                "kind": kind,
                "type_label": label,
                "title": title,
                "raw_path": rel(p),
                "full_path": rel(fp),
                "full_has_body": full_body_ok(fp),
                "raw_bytes": len(t),
            })
    return items


def gaps(items, kinds=("unsupported",)):
    out = [it for it in items if it["kind"] in kinds and not it["full_has_body"]]
    out.sort(key=lambda x: (x["type_label"], x["raw_path"]))
    return out


def cmd_scan(items, kinds):
    g = gaps(items, kinds)
    os.makedirs(TOOLS, exist_ok=True)
    payload = {
        "generated": datetime.date.today().isoformat(),
        "kinds": list(kinds),
        "note": "RAW 侧为占位、RAW_FULL 侧尚未处理的条目；回填目标 = full_path",
        "count": len(g),
        "items": g,
    }
    with open(GAP_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
    print(f"缺口清单已写入 {rel(GAP_JSON)}：{len(g)} 条  (kinds={','.join(kinds)})")
    for k, v in Counter(x["type_label"] for x in g).most_common():
        print(f"  {k}: {v}")


def cmd_slices(items, n, kinds):
    g = gaps(items, kinds)
    os.makedirs(SLICE_DIR, exist_ok=True)
    for old in os.listdir(SLICE_DIR):
        if old.endswith(".json"):
            os.remove(os.path.join(SLICE_DIR, old))
    chunks = [g[i:i + n] for i in range(0, len(g), n)]
    for i, ch in enumerate(chunks, 1):
        p = os.path.join(SLICE_DIR, f"batch_{i:02d}.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump({"batch": i, "count": len(ch), "items": ch},
                      f, ensure_ascii=False, indent=1)
        print(f"{rel(p)}  ({len(ch)} 条)")
    print(f"共 {len(chunks)} 片，每片 {n} 条")


def cmd_verify(items):
    covered = [x for x in items if x["full_has_body"]]
    total_kinds = Counter(x["kind"] for x in items)
    print(f"RAW 侧带 media_id 条目：{len(items)}")
    for k, v in total_kinds.most_common():
        print(f"  {k}: {v}")
    print()
    fam = defaultdict(lambda: [0, 0])
    for x in items:
        if x["kind"] not in ("unsupported", "attach_stub"):
            continue
        fam[x["type_label"]][0] += 1
        if x["full_has_body"]:
            fam[x["type_label"]][1] += 1
    print(f"{'类型':<22}{'占位总数':>10}{'已回填':>8}{'缺口':>8}")
    for k, (tot, ok) in sorted(fam.items(), key=lambda x: -x[1][0]):
        print(f"{k:<22}{tot:>10}{ok:>8}{tot - ok:>8}")
    print()
    print(f"RAW_FULL 侧有正文条目合计：{len(covered)}")


def cmd_status(items, kinds):
    g = gaps(items, kinds)
    notes = [x for x in g if x["prefix"] == "note"]
    print(f"待回填 {len(g)} 条（其中笔记 {len(notes)} 条）")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--slices", type=int, metavar="N")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--kinds", default="unsupported",
                    help="unsupported / attach_stub / 逗号分隔 (默认 unsupported)")
    a = ap.parse_args()
    kinds = tuple(k.strip() for k in a.kinds.split(",") if k.strip())
    items = collect()
    if a.scan:
        cmd_scan(items, kinds)
    elif a.slices:
        cmd_slices(items, a.slices, kinds)
    elif a.verify:
        cmd_verify(items)
    else:
        cmd_status(items, kinds)


if __name__ == "__main__":
    sys.exit(main())

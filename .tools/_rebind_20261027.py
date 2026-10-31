#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-27 回绑 raw_path：仅对 raw_path 为空的 discovered 条目绑「预期 RAW 路径」。

依据：
  1. 插件落盘惯例 = `<原题>.md`（库内存量样本充分，pptx/xlsx/pdf/docx 皆如此）
  2. markdown 条目原题已含 `.md` → 插件再追加 = `.md.md`
  3. IMA REST 标题返回 HTML 转义（`&amp;amp;` 双转义）→ 落盘真实文件名须还原为 `&`

只填空值，不覆盖；幂等。
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
STATE = ".tools/_ima_sync_state.json"

with open(STATE, encoding="utf-8") as f:
    s = json.load(f)
items = s["items"]

bound = 0
for mid, it in items.items():
    if it.get("raw_path") or it.get("first_seen") != "2026-10-27":
        continue
    kb = it.get("kb_path") or ""
    if not kb:
        continue
    # 还原 HTML 转义（可能多轮）
    name = kb
    for _ in range(3):
        dec = html.unescape(name)
        if dec == name:
            break
        name = dec
    exp = "RAW/" + name + ".md"
    it["raw_path"] = exp
    it["raw_path_source"] = "expected_20261027"
    it["raw_path_caveat"] = "插件连续两日未落盘，按 `<原题>.md` 惯例绑预期路径；次日必须复核实落名，不符须三处同步修"
    bound += 1
    print(f"  + [{it.get('media_type')}] {it.get('title')}")
    print(f"      -> {exp}")

with open(STATE, "w", encoding="utf-8") as f:
    json.dump(s, f, ensure_ascii=False, indent=2)
print(f"\nbound {bound} items")

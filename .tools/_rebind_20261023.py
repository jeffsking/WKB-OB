#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-23 回绑 raw_path：仅对 raw_path 为空的 discovered 条目按 kb_path 绑「预期 RAW 路径」。

规则（与既有约定一致）：
  expected = 'RAW/' + kb_path + '.md'   # 插件对 title 统一追加 .md，故 title 自带 .md 时为双后缀
  IMA知识库索引.md 为滚动周度快照，绑定到既有同路径（更新既有页，不新建页）
只填空值，不覆盖；幂等。
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
STATE = ".tools/_ima_sync_state.json"

with open(STATE, encoding="utf-8") as f:
    s = json.load(f)
items = s["items"]

ROLLING = "IMA知识库索引.md"
bound = 0
for mid, it in items.items():
    if it.get("raw_path"):
        continue
    kb = (it.get("kb_path") or "").strip()
    if kb.startswith("ima_sync/"):
        kb = kb[len("ima_sync/"):]
    if not kb:
        continue
    title = it.get("title") or ""
    exp = "RAW/ima_sync/" + kb + ".md"
    if title == ROLLING:
        exp = "RAW/ima_sync/个人知识库/WKB/IMA知识库索引.md.md"
    it["raw_path"] = exp
    it["raw_path_source"] = "expected_20261023"
    bound += 1
    print(f"  + [{it.get('media_type')}] {title[:40]} -> {exp}")

with open(STATE, "w", encoding="utf-8") as f:
    json.dump(s, f, ensure_ascii=False, indent=2)
print(f"bound {bound} items")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-26 回绑 raw_path：仅对 raw_path 为空的 discovered 条目绑「预期 RAW 路径」。

标题含 `/` 时插件把 `/` 转 `_`（库内 411 个存量样本佐证的命名惯例），
故 kb_path 里的 `/` 不可直接当目录分隔符用，须显式给出预期文件名。

只填空值，不覆盖；幂等。
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
STATE = ".tools/_ima_sync_state.json"

# 显式预期路径映射（media_id -> 预期 RAW 路径）
EXPECTED = {
    # 标题「恒碳ptt/pet成本拆解」含 `/` -> 插件落名会把 `/` 换成 `_`
    "note_3867e2b60070d7dc3f413086d0b0036e_7519362139311345":
        "RAW/ima_sync/个人知识库/WKB/恒碳ptt_pet成本拆解.md",
}

with open(STATE, encoding="utf-8") as f:
    s = json.load(f)
items = s["items"]

bound = 0
for mid, it in items.items():
    if it.get("raw_path"):
        continue
    exp = EXPECTED.get(mid)
    if not exp:
        continue
    it["raw_path"] = exp
    it["raw_path_source"] = "expected_20261026"
    it["raw_path_caveat"] = "插件尚未落盘，按 /-> _ 命名惯例绑预期路径；次日必须复核实落名"
    bound += 1
    print(f"  + [{it.get('media_type')}] {it.get('title')} -> {exp}")

with open(STATE, "w", encoding="utf-8") as f:
    json.dump(s, f, ensure_ascii=False, indent=2)
print(f"bound {bound} items")

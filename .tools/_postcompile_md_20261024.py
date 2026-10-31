#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-24：CN/EN 同一纪要合并为一页后的收尾。

- 页面改名去掉 `_CN` 后缀（一页同时覆盖 CN + EN，front matter 已用 source_paths 双登记）
- 账本两条（CN / EN）均置 compiled，source_page_hint 指向合并页
- 幂等：页面已改名、账本已指向则无改动
"""
import json
import os
import shutil
from datetime import datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
STATE = ".tools/_ima_sync_state.json"
SRC = "WIKI/sources/会议纪要_金佰利×聚合芯能_功能性材料技术对接_20261023_CN.md"
DST = "WIKI/sources/会议纪要_金佰利×聚合芯能_功能性材料技术对接_20261023.md"
CST = timezone(timedelta(hours=8))
NOW = datetime.now(CST).isoformat(timespec="seconds")

MIDS = [
    "markdown_3867e2b60070d7dc3f413086d0b0036e_f5d67c32985d6dc7161e17124454d931001a693ee6c0644e",
    "markdown_3867e2b60070d7dc3f413086d0b0036e_256cbf2d99691b18c27f42b9085ee22b001a693ee6c0644e",
]

if os.path.exists(SRC) and not os.path.exists(DST):
    os.rename(SRC, DST)
    print("[RENAME]", SRC, "->", DST)
elif os.path.exists(DST):
    print("[NOOP] 目标已存在:", DST)
else:
    print("[WARN] 源页面不存在:", SRC)

s = json.load(open(STATE, encoding="utf-8"))
changed = 0
hint = DST.replace("/", "\\")
for mid in MIDS:
    it = s["items"].get(mid)
    if not it:
        print("[SKIP] 无条目", mid[-12:])
        continue
    if it.get("stage") == "compiled" and it.get("source_page_hint") == hint:
        print("[NOOP]", mid[-12:], "已 compiled")
        continue
    if changed == 0:
        shutil.copy(STATE, STATE + ".bak.20261024-postcompile")
    it["stage"] = "compiled"
    it["stage_source"] = "merged-cn-en-20261024"
    it["stage_updated"] = NOW
    it["source_page_hint"] = hint
    changed += 1
    print("[COMPILED]", mid[-12:], "->", hint)

if changed:
    json.dump(s, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("改动", changed, "条")

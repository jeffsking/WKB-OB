#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-31 公众号条目落地（plan 拒绑：标题含 ASCII |，非法文件名）。

策略：
  · 正文写 RAW_FULL（合法文件名，ASCII | → 全角 ｜，与库内 4 条 NC 系列同惯例）
  · 账本 raw_path / full_path 绑「预期路径」，标 raw_path_source=expected_sanitized
  · 页内必须注记锚点状态；次日复核插件实落名，不符则三处同步修（禁建重复页）
"""
import json
import os
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

MID = "wechatarticle_3867e2b60070d7dc3f413086d0b0036e_47b652bdde6ef08fa72bc6e041e28a3c"
TITLE = "NC | 盐调控氢键网络：纤维素液晶弹性体实现可视化力致变色"
SAFE = TITLE.replace(" | ", "｜").replace("|", "｜")
REL = f"ima_sync/个人知识库/WKB/{SAFE}.md"
RAW_EXP = "RAW/" + REL
FULL = "RAW_FULL/" + REL
BODY = f".tools/_kb_sync_bodies/{MID}.md"

os.makedirs(os.path.dirname(FULL), exist_ok=True)
text = open(BODY, encoding="utf-8").read()

fm = f'''---
media_id: "{MID}"
extract_status: "ok"
extract_channel: "A5-wechat"
synced_at: "{datetime.now().astimezone().isoformat(timespec='seconds')}"
source_path: "{RAW_EXP}"
media_type: 6
anchor_status: "expected_sanitized（标题含 ASCII |，插件落盘时按历史惯例转全角 ｜，次日须复核实落名）"
---

# {SAFE}

'''
with open(FULL, "w", encoding="utf-8") as f:
    f.write(fm + text)
print(f"[write] {FULL} chars={len(text)}")

# 账本回写
p = ".tools/_ima_sync_state.json"
d = json.load(open(p, encoding="utf-8"))
e = d["items"][MID]
e["raw_path"] = RAW_EXP
e["full_path"] = FULL
e["raw_path_source"] = "expected_sanitized"
e["raw_path_bound"] = datetime.now().astimezone().isoformat(timespec="seconds")
e["stage"] = "synced"
e["stage_source"] = "manual-wechat（plan 拒绑非法字符，正文已到手）"
e["stage_updated"] = datetime.now().astimezone().isoformat(timespec="seconds")
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("[ledger] synced:", RAW_EXP)

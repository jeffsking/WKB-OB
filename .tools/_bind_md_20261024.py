#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-24：两条 markdown 条目「回绑锚点 + 落 RAW_FULL 镜像」。

背景：插件今日未落 RAW（find RAW -newermt 0 条），plan 因 raw_path 空而漏此 3 条（已知盲区）。
markdown 命名惯例已由 411 个存量 `.md.md` 文件证实（原题含 .md 时插件再追加 .md），
故按期望路径回绑；标题不含 "/" → 无路径歧义。**仅回绑 markdown 两条**，
note「恒碳ptt/pet成本拆解」无正文（200005）且标题含 "/"，今日不回绑。

备份账本 → 写 RAW_FULL 镜像（front matter: media_id/extract_status/extract_channel/synced_at/source_path）
→ stage 置 synced。幂等：镜像已存在且非空则跳过写入。
"""
import json
import os
import shutil
from datetime import datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
STATE = ".tools/_ima_sync_state.json"
BODIES = ".tools/_kb_sync_bodies"
CST = timezone(timedelta(hours=8))
NOW = datetime.now(CST).isoformat(timespec="seconds")

TARGETS = [
    "markdown_3867e2b60070d7dc3f413086d0b0036e_f5d67c32985d6dc7161e17124454d931001a693ee6c0644e",
    "markdown_3867e2b60070d7dc3f413086d0b0036e_256cbf2d99691b18c27f42b9085ee22b001a693ee6c0644e",
]

s = json.load(open(STATE, encoding="utf-8"))
changed = 0
for mid in TARGETS:
    it = s["items"].get(mid)
    if not it:
        print("[SKIP] 账本无此条目", mid[-12:])
        continue
    title = it["title"]
    rel = "ima_sync/个人知识库/WKB/" + title + ".md"
    rp, fp = "RAW/" + rel, "RAW_FULL/" + rel
    body_p = os.path.join(BODIES, mid + ".md")
    if not os.path.exists(body_p):
        print("[SKIP] 无暂存正文", mid[-12:])
        continue
    body = open(body_p, encoding="utf-8").read().strip()
    if changed == 0:
        shutil.copy(STATE, STATE + ".bak.20261024-prerebind")
    # 镜像
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    if os.path.exists(fp) and os.path.getsize(fp) > 500:
        print("[NOOP] 镜像已存在", fp)
    else:
        lines = [
            "---",
            f'media_id: "{mid}"',
            'extract_status: "ok"',
            'extract_channel: "B"',
            f'synced_at: "{NOW}"',
            f'source_path: "{rp}"',
            f"media_type: {it.get('media_type')}",
            "---",
            "",
            body,
            "",
        ]
        open(fp, "w", encoding="utf-8").write("\n".join(lines))
        print("[MIRROR]", fp, os.path.getsize(fp), "B")
    it["raw_path"] = rp
    it["full_path"] = fp
    it["stage"] = "synced"
    it["stage_source"] = "manual-markdown-20261024"
    it["stage_updated"] = NOW
    it["rebind_source"] = "expected-path-markdown-pattern-20261024"
    changed += 1
    print("[BIND]", mid[-12:], "->", rp)

if changed:
    json.dump(s, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("回绑/落地", changed, "条")

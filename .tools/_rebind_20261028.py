#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-28 锚点回绑：为插件未落盘的新条目绑「预期 RAW 路径」（plan 空 raw_path 盲区绕行）。

规则（依据 411 个存量样本 + 根层实况 RAW/ima_sync/个人知识库/WKB/）：
  markdown(type 7)  title 已含 .md → 插件再追加 .md → <title>.md（即 xxx.md.md）
  excel(5)/pdf(1)/word(6)  → <title>.md（原扩展名保留 + .md）
  note(11) → 跳过（REST 标题 ~40 字符截断 + 含 "..."，绑预期=制造幽灵锚点）

幂等：只绑 raw_path 为空且 6 类文件型条目；已有值一律不动。
安全：绑前若发现同名真实文件已存在，则直接用真实文件路径（防幽灵锚点）。
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
STATE = ".tools/_ima_sync_state.json"
BASE_DIR = "RAW/ima_sync/个人知识库/WKB"
TODAY = "2026-10-28"


def expected_raw_path(title, media_type):
    t = (title or "").strip()
    if not t:
        return None
    if media_type == 11:          # note 标题不可信 → 不绑
        return None
    if "/" in t or "\\" in t:     # 插件把 / 转 _ → 不可类推
        return None
    if "..." in t:                # 截断标题
        return None
    name = t + ".md" if not t.lower().endswith(".md") else t + ".md"
    return f"{BASE_DIR}/{name}"


def main():
    st = json.load(open(STATE, encoding="utf-8"))
    items = st["items"]
    bound, skipped, existed = [], [], []
    for mid, it in items.items():
        if it.get("first_seen") != TODAY:
            continue
        if (it.get("raw_path") or "").strip():
            continue
        rp = expected_raw_path(it.get("title"), it.get("media_type"))
        if not rp:
            skipped.append((mid, it.get("media_type"), (it.get("title") or "")[:50]))
            continue
        if os.path.isfile(rp):
            existed.append(rp)
        it["raw_path"] = rp
        it["full_path"] = "RAW_FULL/" + rp[len("RAW/"):]
        it["raw_path_hint"] = "expected-naive-20261028"   # 明示为预期路径，次日须复核
        bound.append((mid, it.get("media_type"), rp))

    json.dump(st, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"[rebind] 绑定 {len(bound)} 条 · 跳过 {len(skipped)} 条 · 真实文件已存在 {len(existed)}")
    for mid, mt, rp in bound:
        print(f"  + t={mt} {rp}")
    if skipped:
        print("--- 跳过（note / 含 / / 截断标题）---")
        for mid, mt, t in skipped:
            print(f"  - t={mt} {t}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

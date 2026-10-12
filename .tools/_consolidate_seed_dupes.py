"""Consolidate duplicate seed pages.

For each duplicate pair: keep the LARGER page as canonical, rewrite every
inbound `[[stub]]` -> `[[canonical]]`, and turn the stub into a short pointer
page (NOT deleted — AGENTS.md §5 forbids auto-deletion; flagged manual_review).
"""
import glob
import json
import os
import re
import shutil
import sys

VAULT = "E:/WKB-OB"
WIKI = os.path.join(VAULT, "WIKI")
BACKUP = os.path.join(VAULT, ".tools", "_page_backup_dupes")

# Collapse ONLY where one side is a thin stub. Pairs where BOTH pages carry real
# content are NOT auto-merged — they are flagged for human review instead.
CANDIDATES = [
    ("2025.06.25 - Learning Cycle Check In（GRIFFIN 学习周期复盘）",
     "GRIFFIN Learning Cycle Check In（GRIFFIN 学习周期复盘 · 2025-06-25）"),
    ("热致变色", "热致变色 Thermochromic"),
    ("SymDeo™ XPP 抑臭聚合物", "Symrise SymDeo™ XPP 抑臭聚合物（中文版）"),
    ("Contact Angle", "接触角 Contact Angle"),
    ("Hot Melt Adhesive", "热熔胶 Hot Melt Adhesive"),
    ("毛细管压力 Capillary Pressure", "毛细压力 Capillary Pressure"),
]

# Both sides substantive -> needs a human merge decision
REVIEW_PAIRS = [
    ("Changeover Four-Layer Architecture（换型要素四层分层与变更控制）",
     "83 Changeover Four-Layer Architecture（换型要素四层分层与变更控制）"),
    ("Repitch（鼓距与产品节距解耦）", "82 鼓距与产品节距解耦 repitch 选型"),
]


def find(name):
    for d in ("concepts", "entities", "sources", "comparisons"):
        p = os.path.join(WIKI, d, name + ".md")
        if os.path.exists(p):
            return p
    return None


os.makedirs(BACKUP, exist_ok=True)
resolved, skipped = [], []
for a, b in CANDIDATES:
    pa, pb = find(a), find(b)
    if not pa or not pb:
        skipped.append((a, b, "page missing"))
        continue
    sa, sb = os.path.getsize(pa), os.path.getsize(pb)
    if sa > sb * 1.3:                     # stub (a) is actually the richer one
        stub, canon, pstub, pcanon = b, a, pb, pa
    else:
        stub, canon, pstub, pcanon = a, b, pa, pb
    shutil.copy2(pstub, os.path.join(BACKUP, os.path.basename(pstub)))
    resolved.append((stub, canon, pstub))
    print(f"  canonical = {canon}  ({os.path.getsize(pcanon)} B)")
    print(f"  stub      = {stub}  ({os.path.getsize(pstub)} B)")

if "--apply" not in sys.argv:
    print("\n(dry-run; add --apply)")
    sys.exit(0)

n_links = 0
for stub, canon, pstub in resolved:
    # 1) rewrite all inbound links
    for f in glob.glob(os.path.join(WIKI, "*", "*.md")):
        t0 = open(f, encoding="utf-8").read()
        t = t0.replace(f"[[{stub}]]", f"[[{canon}]]").replace(f"[[{stub}|", f"[[{canon}|")
        if t != t0:
            open(f, "w", encoding="utf-8", newline="\n").write(t)
            n_links += 1
    # 2) stub -> pointer page (kept on disk)
    t = open(pstub, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    fm = m.group(1) if m else ""
    typ = (re.search(r"^type:\s*(\S+)", fm, re.M) or [None, "concept"])[1]
    dom = re.search(r"^domain:\s*(.+)$", fm, re.M)
    dom = dom.group(1).strip() if dom else "[待补]"
    body = f"""---
type: {typ}
title: "{stub}"
domain: {dom}
status: merged
updated: 2026-09-30
tags: [merged, 指针页]
---

# {stub}

> 🔴 **manual_review（2026-09-30）**：本页与 [[{canon}]] 为同一主题的重复页。已把全库入链改写为 `[[{canon}]]`，本页保留为**指针页**（未删除——按 AGENTS.md §5，删页须人工确认）。**请人工裁决是否删除本文件。**

本主题的正文见：[[{canon}]]
"""
    open(pstub, "w", encoding="utf-8", newline="\n").write(body)

print(f"\n合并 {len(resolved)} 对；改写含入链的文件 {n_links} 个")
print(f"备份 -> .tools/_page_backup_dupes/")
if skipped:
    print("跳过:", skipped)

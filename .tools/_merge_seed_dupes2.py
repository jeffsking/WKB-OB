"""Merge the 2 remaining naming-variant duplicate pairs found among the empty seeds."""
import glob
import os
import re
import shutil

VAULT = "E:/WKB-OB"
WIKI = os.path.join(VAULT, "WIKI")
BACKUP = os.path.join(VAULT, ".tools", "_page_backup_dupes")

PAIRS = [
    ("有限差分法", "有限差分法 Finite Difference"),
    ("Silane Coupling Agent", "硅烷偶联剂 Silane Coupling Agent"),
]


def find(name):
    for d in ("concepts", "entities", "sources", "comparisons"):
        p = os.path.join(WIKI, d, name + ".md")
        if os.path.exists(p):
            return p
    return None


os.makedirs(BACKUP, exist_ok=True)
n_links = 0
for stub, canon in PAIRS:
    ps, pc = find(stub), find(canon)
    if not ps or not pc:
        print("skip", stub, canon)
        continue
    shutil.copy2(ps, os.path.join(BACKUP, os.path.basename(ps)))
    for f in glob.glob(os.path.join(WIKI, "*", "*.md")):
        t0 = open(f, encoding="utf-8").read()
        t = t0.replace(f"[[{stub}]]", f"[[{canon}]]").replace(f"[[{stub}|", f"[[{canon}|")
        if t != t0:
            open(f, "w", encoding="utf-8", newline="\n").write(t)
            n_links += 1
    t = open(ps, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    fm = m.group(1) if m else ""
    typ = (re.search(r"^type:\s*(\S+)", fm, re.M) or [None, "concept"])[1]
    dom = re.search(r"^domain:\s*(.+)$", fm, re.M)
    dom = dom.group(1).strip() if dom else "[待补]"
    open(ps, "w", encoding="utf-8", newline="\n").write(f"""---
type: {typ}
title: "{stub}"
domain: {dom}
status: merged
updated: 2026-09-30
tags: [merged, 指针页]
---

# {stub}

> 🔴 **manual_review（2026-09-30）**：本页与 [[{canon}]] 为同一概念的命名变体。已把全库入链改写为 `[[{canon}]]`，本页保留为**指针页**（未删除——按 AGENTS.md §5，删页须人工确认）。**请人工裁决是否删除本文件。**

本主题的正文见：[[{canon}]]
""")
    print("merged:", stub, "->", canon)

print("改写含入链文件:", n_links)

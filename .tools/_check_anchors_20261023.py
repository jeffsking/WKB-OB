#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""核验 WIKI/sources 的 source_path 锚点是否存在；对缺失者按文件名在 RAW 内找候选。只读。"""
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

allf = []
for dp, dn, fn in os.walk("RAW"):
    for f in fn:
        allf.append((os.path.join(dp, f)).replace(os.sep, "/"))
print("RAW 文件数", len(allf))

pages = []
for p in glob.glob("WIKI/sources/*.md"):
    txt = open(p, encoding="utf-8", errors="ignore").read()
    m = re.search(r"^source_path:[ \t]*(.+)$", txt[:3000], re.M)
    if m:
        pages.append((p, m.group(1).strip().strip('"').strip("'")))

missing = [(p, sp) for p, sp in pages if not os.path.exists(sp)]
print(f"含 source_path 页 {len(pages)} · 目标不存在 {len(missing)}\n")

for p, sp in missing:
    base = os.path.basename(sp)
    key = base[:-3] if base.endswith(".md") else base
    key = key.replace(".md", "")
    cands = [f for f in allf if key[:14] in f]
    print("--", base[:60])
    print("   page:", os.path.basename(p)[:70])
    if not cands:
        print("   [NO CANDIDATE by basename]")
    for c in cands[:5]:
        print("   cand:", c)

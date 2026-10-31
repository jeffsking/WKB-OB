#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-23 新建页链接校验：检查指定页内 [[...]] 是否都有目标页。只读。"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

names = set()
for dp, dn, fn in os.walk("WIKI"):
    for f in fn:
        if f.endswith(".md"):
            names.add(f[:-3])

files = sys.argv[1:]
bad = {}
for p in files:
    txt = open(p, encoding="utf-8").read()
    for m in re.finditer(r"\[\[([^\]|#]+)", txt):
        t = m.group(1).strip()
        if t not in names:
            bad.setdefault(p, set()).add(t)
for p, ts in bad.items():
    print("==", p)
    for t in sorted(ts):
        print("   MISSING:", t)
if not bad:
    print("all links OK")

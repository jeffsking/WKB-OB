#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-23 给概念页 `## Related Sources` 补入新源（按标题排序插入，幂等）。"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

EDITS = {
    "WIKI/concepts/Zeolite Odour Control（沸石除臭载体）.md": [
        "会议纪要_金佰利×中科一然_除味材料技术对接",
    ],
    "WIKI/concepts/Odor Control Technology Landscape（异味控制技术图谱）.md": [
        "会议纪要_金佰利×中科一然_除味材料技术对接",
    ],
    "WIKI/concepts/相变材料 Phase Change Material.md": [
        "会议纪要_金佰利×中科一然_除味材料技术对接",
        "NTMT丨PCM相变调温纤维：是黑科技还是噱头？从芯材选择到纺丝应用，这篇全讲明白了",
    ],
}

for path, titles in EDITS.items():
    if not os.path.exists(path):
        print("! missing page:", path)
        continue
    txt = open(path, encoding="utf-8").read()
    m = re.search(r"^## Related Sources[^\n]*\n(.*?)(?=^## |\Z)", txt, re.S | re.M)
    if not m:
        print("! no Related Sources section:", path)
        continue
    block = m.group(1)
    lines = [ln for ln in block.strip("\n").splitlines()]
    entries = [ln for ln in lines if ln.startswith("- [[")]
    added = []
    for t in titles:
        if f"[[{t}]]" in txt:
            continue
        entries.append(f"- [[{t}]]")
        added.append(t)
    if not added:
        print("= no change:", os.path.basename(path))
        continue

    def key(ln):
        mm = re.match(r"- \[\[(.+?)\]\]", ln)
        return mm.group(1) if mm else ln

    entries.sort(key=key)
    new_block = "\n" + "\n".join(entries) + "\n\n"
    txt2 = txt[:m.start(1)] + new_block + txt[m.end(1):]
    open(path, "w", encoding="utf-8").write(txt2)
    print(f"+ {os.path.basename(path)} ← {added}")

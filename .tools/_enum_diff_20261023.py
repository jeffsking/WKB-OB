#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-23 枚举对撞 + 幽灵锚点目标路径探测。只读。"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def mids(d):
    return {e.get("media_id"): e for e in d.get("items", []) if e.get("media_id")}


a = load(".tools/_ima_enum_20261022.json")
b = load(".tools/_ima_enum_20261023.json")
ma, mb = mids(a), mids(b)
new = set(mb) - set(ma)
gone = set(ma) - set(mb)
print(f"10-22 文件条目 {len(ma)} · 10-23 文件条目 {len(mb)}")
print(f"新增 {len(new)} · 消失 {len(gone)}")
for m in sorted(new):
    e = mb[m]
    print(f"  + [{e.get('media_type')}] {e.get('title','')[:55]} | kb_path: {e.get('kb_path','')[:70]}")
for m in sorted(gone):
    e = ma[m]
    print(f"  - [{e.get('media_type')}] {e.get('title','')[:55]} | {e.get('kb_path','')[:60]}")

# 幽灵锚点目标路径探测：这 8 个 media_id 在今日枚举里的 kb_path
targets = [
    "soundrecording_3867e2b60070d7dc3f413086d0b0036e_01a162b5e6017d5d938b55d238339fc0001a693ee6c0644e",
    "soundrecording_3867e2b60070d7dc3f413086d0b0036e_01a162b36c8c7e51a178d839cfd68bad001a693ee6c0644e",
    "soundrecording_3867e2b60070d7dc3f413086d0b0036e_01a162b62dff7dbcaed0855d0b90a280001a693ee6c0644e",
    "soundrecording_3867e2b60070d7dc3f413086d0b0036e_01a162b49b01773995ca0f3c60a7e320001a693ee6c0644e",
    "soundrecording_3867e2b60070d7dc3f413086d0b0036e_01a162b3c01a7f08b4e7cda51ad15652001a693ee6c0644e",
    "markdown_3867e2b60070d7dc3f413086d0b0036e_910cc7726e3b79b9729c5536a6d86c5c001a693ee6c0644e",
    "markdown_3867e2b60070d7dc3f413086d0b0036e_903428b49d13679de587398ab07212eb001a693ee6c0644e",
    "markdown_3867e2b60070d7dc3f413086d0b0036e_5d9bbd4465f535eb0f873c570d397830001a693ee6c0644e",
]
print("\n[幽灵锚点目标路径]")
for t in targets:
    e = mb.get(t)
    if not e:
        print("  ! 今日枚举未命中:", t[:40])
        continue
    kb = e.get("kb_path", "")
    guess = os.path.join("RAW/ima_sync/个人知识库/WKB", kb + ".md").replace(os.sep, "/")
    print(f"  {e.get('title','')[:34]:<36} kb_path={kb[:58]}")
    print(f"      预期RAW={guess}  exists={os.path.exists(guess)}")

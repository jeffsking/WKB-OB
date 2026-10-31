#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-31 编译后处理：页名语义化 + 账本 hint 回写 + 合并页次源标记。

铁律：改名只替换 [[wikilink]] 形态，永不动 source_path/source_paths；
      写前校验 /\\:*?"<>|；缺文件跳过（幂等可续跑）。
"""
import json
import os
import re
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

S = "WIKI/sources"
RENAMES = [
    ("纸尿裤可视化功能层_PEG基slot_die复配乳液技术方案_20261030",
     "PEG-Based Slot-Die Emulsion for Visual Cue Layer（可视化功能层复配乳液方案集 · 2026-10-30）"),
    ("NC - 盐调控氢键网络：纤维素液晶弹性体实现可视化力致变色",
     "Cellulose-Based LCE with Salt-Tuned Hydrogen Bonding（盐调控氢键网络 · 纤维素液晶弹性体 · NC 2026）"),
]
ILLEGAL = set('/\\:*?"<>|')

MAIN = "markdown_3867e2b60070d7dc3f413086d0b0036e_49240900fa45de87fba84f5c102fc290001a693ee6c0644e"
SEC = "markdown_3867e2b60070d7dc3f413086d0b0036e_3bb235881e629b6e72a4b2a94d21ab15001a693ee6c0644e"
WX = "wechatarticle_3867e2b60070d7dc3f413086d0b0036e_47b652bdde6ef08fa72bc6e041e28a3c"

done = {}
for old, new in RENAMES:
    if ILLEGAL & set(new):
        print(f"[skip-非法字符] {new[:40]}")
        continue
    src = os.path.join(S, old + ".md")
    dst = os.path.join(S, new + ".md")
    if not os.path.exists(src):
        print(f"[skip-缺文件] {old[:40]}")
        if os.path.exists(dst):
            done[old] = new
        continue
    if os.path.exists(dst):
        print(f"[skip-目标已存在] {new[:40]}")
        done[old] = new
        continue
    os.rename(src, dst)
    done[old] = new
    print(f"[rename] {old[:34]} → {new[:44]}")

# 全库 wikilink 换名（只动 [[...]] 形态）
if done:
    pat = re.compile(r"\[\[([^\]|#]+)((?:[#|][^\]]*)?)\]\]")
    touched = 0
    for dirpath, _d, files in os.walk("WIKI"):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            t = open(p, encoding="utf-8", errors="replace").read()
            if not any(o in t for o in done):
                continue
            def rep(m):
                tgt = m.group(1).strip()
                if tgt in done:
                    return f"[[{done[tgt]}{m.group(2)}]]"
                return m.group(0)
            nt = pat.sub(rep, t)
            if nt != t:
                open(p, "w", encoding="utf-8").write(nt)
                touched += 1
    print(f"[links] 改写文件 {touched} 个（只动 [[wikilink]]）")

# 账本 hint
p = ".tools/_ima_sync_state.json"
d = json.load(open(p, encoding="utf-8"))
now = datetime.now().astimezone().isoformat(timespec="seconds")
main_page = RENAMES[0][1]
wx_page = RENAMES[1][1]
for mid, page in ((MAIN, main_page), (WX, wx_page)):
    e = d["items"][mid]
    e["stage"] = "compiled"
    e["source_page_hint"] = f"WIKI/sources/{page}.md"
    e["stage_updated"] = now
    print("[hint]", mid[:24], "→", page[:40])

# 次源（Knight IV）不走 apply：并入合并页
e = d["items"][SEC]
e["stage"] = "compiled"
e["source_page_hint"] = f"WIKI/sources/{main_page}.md"
e["stage_source"] = "merged-into-v1.1（同文档 v1.0/v1.1 两版本，按 §1.1.4 以最全版本为主件，未建平行页）"
e["stage_updated"] = now
print("[merged]", SEC[:24], "→ 合并页")

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("[ledger] 已回写 3 条")

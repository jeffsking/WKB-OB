#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-31 组装暂存正文：3 条（2 markdown + 1 wechatarticle）。"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
OUT = ".tools/_fetch_out_20261031"
BODIES = ".tools/_kb_sync_bodies"
os.makedirs(BODIES, exist_ok=True)

PLAN = json.load(open(".tools/_kb_sync_plan.json", encoding="utf-8"))

MAP = {
    "49240900fa45de87fba84f5c102fc290": ("peg_general.md", "markdown-original"),
    "3bb235881e629b6e72a4b2a94d21ab15": ("peg_knight_iv.md", "markdown-original"),
    "47b652bdde6ef08fa72bc6e041e28a3c": ("nc_lce_mechanochromic.txt", "wechat-html"),
}


def clean_wechat(t):
    # 去掉尾部公众号 UI 噪声
    for tail in ["预览时标签不可点", "阅读原文", "不喜欢"]:
        i = t.find(tail)
        if i > 0:
            t = t[:i]
    return t.strip() + "\n"


for it in PLAN["items"]:
    mid = it["media_id"]
    tag = None
    for frag, (fn, channel) in MAP.items():
        if frag in mid:
            tag = (fn, channel)
            break
    if not tag:
        print("[skip] 无映射", mid[:30])
        continue
    fn, channel = tag
    p = os.path.join(OUT, fn)
    if not os.path.exists(p):
        print("[miss]", fn)
        continue
    text = open(p, encoding="utf-8").read()
    if channel == "wechat-html":
        text = clean_wechat(text)
    dest = os.path.join(BODIES, mid + ".md")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(text)
    meta = {"media_id": mid, "channel": channel, "chars": len(text),
            "extract_status": "ok" if len(text) > 300 else "empty",
            "source_file": fn}
    with open(os.path.join(BODIES, mid + ".json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    print(f"[ok] {mid[:26]} ← {fn} chars={len(text)} channel={channel}")

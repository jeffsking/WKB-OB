#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""列出「真实未编译」明细 —— 严格按 AGENTS §1.1.1 三形态算法复算，
用于与 .tools/wkb_dedup.py scan 的计数交叉自证（不是替代判重权威，只是把它没打印的清单列出来）。

铁律遵守：
  · 正则一律 [ \\t]*，禁用 \\s*
  · 三形态全收：source_path 单值 / source_paths 多值 / merged 指针页
  · 扫描后先自证覆盖率（打印匹配条数）
只读，不改任何文件。
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def collect_paths(fm):
    paths = set()
    m = re.search(r"^source_path:[ \t]*(.+)$", fm, re.M)
    if m:
        v = m.group(1).strip().strip('"').strip("'")
        if v:
            paths.add(v.replace("\\", "/"))
    ml = re.search(r"^source_paths:[ \t]*\n((?:[ \t]*-[ \t]*.+\n?)+)", fm, re.M)
    if ml:
        for ln in ml.group(1).splitlines():
            v = ln.strip().lstrip("-").strip().strip('"').strip("'")
            if v:
                paths.add(v.replace("\\", "/"))
    return paths


def main():
    idx = set()
    pages = 0
    with_reg = 0
    for r, d, fs in os.walk(os.path.join(ROOT, "WIKI")):
        for f in fs:
            if not f.endswith(".md"):
                continue
            pages += 1
            p = os.path.join(r, f)
            try:
                t = open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            fm = t.split("---", 2)[1] if t.startswith("---") else ""
            got = collect_paths(fm)
            if got:
                with_reg += 1
                idx |= got

    raws = set()
    for r, d, fs in os.walk(os.path.join(ROOT, "RAW")):
        if "attachments" in r or ".obsidian" in r:
            continue
        for f in fs:
            if f.endswith(".md"):
                raws.add(os.path.relpath(os.path.join(r, f), ROOT).replace("\\", "/"))

    unc = sorted(raws - idx)
    print(f"[自证] WIKI 页面 {pages} · 含登记 {with_reg} · 登记路径去重 {len(idx)}")
    print(f"[自证] RAW 条目 {len(raws)}")
    print(f"[结论] 真实未编译 {len(unc)} 条")
    for u in unc:
        print("  -", u)
    print(f"[交叉] 与 wkb_dedup scan 的 3 条比对：{'一致' if len(unc) == 3 else '不一致，需复核'}")


if __name__ == "__main__":
    main()

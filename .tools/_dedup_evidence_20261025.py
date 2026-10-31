#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""判重取证：4 条待编译笔记 vs 既有 WIKI 源页，用字符 8-gram Jaccard 估算重合度。

只用共享片段率，不改任何文件。输出供人工裁定。
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BODIES = os.path.join(ROOT, ".tools", "_done", "2026-10-25")
WIKI = os.path.join(ROOT, "WIKI", "sources")
N = 8


def norm(t):
    """去 front matter、去 markdown 结构符、去空白，保留字母数字与汉字。"""
    t = re.sub(r"^---.*?---\s*", "", t, count=1, flags=re.S)
    t = re.sub(r"[#*|>`\-\[\]()]", "", t)
    t = re.sub(r"\s+", "", t)
    return t.lower()


def grams(s, n=N):
    return {s[i:i + n] for i in range(max(0, len(s) - n + 1))}


def main():
    bodies = {}
    for f in sorted(os.listdir(BODIES)):
        if not f.endswith(".md"):
            continue
        p = os.path.join(BODIES, f)
        bodies[f[:-3]] = grams(norm(open(p, encoding="utf-8", errors="replace").read()))

    pages = {}
    for f in sorted(os.listdir(WIKI)):
        if not f.endswith(".md"):
            continue
        p = os.path.join(WIKI, f)
        try:
            pages[f[:-3]] = grams(norm(open(p, encoding="utf-8", errors="replace").read()))
        except OSError:
            pass

    out = {}
    for mid, bg in bodies.items():
        scores = []
        for name, pg in pages.items():
            if not pg:
                continue
            inter = len(bg & pg)
            if inter == 0:
                continue
            jac = inter / len(bg | pg)
            # 该页覆盖了多少比例的本条内容（recall 视角，更贴近"本条已被该页消化"）
            cov = inter / len(bg) if bg else 0
            scores.append((round(jac, 4), round(cov, 4), name))
        scores.sort(key=lambda x: -x[1])
        out[mid] = {"body_grams": len(bg), "top": scores[:5]}

    print(json.dumps(out, ensure_ascii=False, indent=1))
    with open(os.path.join(ROOT, ".tools", "_dedup_evidence_20261025.json"), "w",
              encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()

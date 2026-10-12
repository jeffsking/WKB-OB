"""Dump the relevant context for a seed page: for each citing source, the
sentences that actually mention the concept. Deterministic extraction only —
no synthesis, no fabrication. Used to fill seed pages from real content.

Usage:
  python .tools/_seed_context.py "吸收芯体" [--max-per-src 4] [--chars 6000]
"""
import glob
import os
import re
import sys
import json

VAULT = "E:/WKB-OB"
WIKI = os.path.join(VAULT, "WIKI")


def find_page(name):
    for d in ("concepts", "entities", "sources", "comparisons"):
        p = os.path.join(WIKI, d, name + ".md")
        if os.path.exists(p):
            return p
    return None


def body_of(p):
    t = open(p, encoding="utf-8", errors="ignore").read()
    if t.startswith("---"):
        i = t.find("\n---", 3)
        if i > 0:
            t = t[i + 4:]
    return t


def sentences(t):
    t = re.sub(r"`[^`]*`", "", t)
    t = re.sub(r"^[#>\-*|].*$", "", t, flags=re.M)      # drop headings/quotes/tables/list
    parts = re.split(r"(?<=[。！？\.])\s+|\n{2,}", t)
    return [p.strip() for p in parts if len(p.strip()) > 25]


def variants(name):
    """Concept name -> search tokens (split ZH / EN parts)."""
    vs = {name}
    zh = re.findall(r"[\u4e00-\u9fff]{2,}", name)
    en = re.findall(r"[A-Za-z][A-Za-z0-9\-']{3,}", name)
    vs |= set(zh) | set(en)
    return {v for v in vs if len(v) >= 3}


def main():
    name = sys.argv[1]
    max_per = 4
    if "--max-per-src" in sys.argv:
        max_per = int(sys.argv[sys.argv.index("--max-per-src") + 1])

    p = find_page(name)
    if not p:
        print("page not found:", name)
        return
    t = open(p, encoding="utf-8", errors="ignore").read()
    sec = re.search(r"## Cited by[\s\S]*?(?=\n## |\Z)", t)
    cited = re.findall(r"\[\[([^\]|#]+)\]\]", sec.group(0)) if sec else []

    print(f"# {name}  ——  引用来源 {len(cited)} 个")
    toks = variants(name)
    print(f"# 检索词: {sorted(toks)}\n")
    hits = 0
    for c in cited:
        cp = find_page(c)
        if not cp:
            print(f"--- [[{c}]]  (页面不存在)\n")
            continue
        b = body_of(cp)
        keep = []
        for s in sentences(b):
            if any(tk.lower() in s.lower() for tk in toks):
                keep.append(s)
        if not keep:
            print(f"--- [[{c}]]  (无命中)")
            continue
        hits += 1
        print(f"--- [[{c}]]  ({len(keep)} 命中)")
        for s in keep[:max_per]:
            print("   •", s[:400])
        print()
    print(f"# 有命中的来源: {hits}/{len(cited)}")


main()

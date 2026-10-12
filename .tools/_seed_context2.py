"""Find REAL prose about a concept anywhere in the vault (not just citing pages).

Usage:
  python .tools/_seed_context.py "吸收芯体" [--terms "absorbent core,芯体,core"]
                              [--max-per-src 3] [--top 15]
"""
import glob
import os
import re
import sys

VAULT = "E:/WKB-OB"
WIKI = os.path.join(VAULT, "WIKI")


def body_of(p):
    t = open(p, encoding="utf-8", errors="ignore").read()
    if t.startswith("---"):
        i = t.find("\n---", 3)
        if i > 0:
            t = t[i + 4:]
    return t


def prose(t):
    t = re.sub(r"`[^`]*`", "", t)
    out = []
    for chunk in re.split(r"\n{2,}", t):
        c = chunk.strip()
        if not c:
            continue
        if c.startswith(("#", ">", "|", "---")):
            continue
        # keep list items but strip the marker
        c = re.sub(r"^[-*+]\s+", "", c)
        c = re.sub(r"\[\[([^\]|#]+)(\|[^\]]+)?\]\]", r"\1", c)
        out.append(c)
    return out


def main():
    name = sys.argv[1]
    terms = set()
    for z in re.findall(r"[\u4e00-\u9fff]{2,}", name):
        terms.add(z)
    for e in re.findall(r"[A-Za-z][A-Za-z0-9\-']{3,}", name):
        terms.add(e)
    if "--terms" in sys.argv:
        for x in sys.argv[sys.argv.index("--terms") + 1].split(","):
            if x.strip():
                terms.add(x.strip())

    max_per = int(sys.argv[sys.argv.index("--max-per-src") + 1]) if "--max-per-src" in sys.argv else 3
    top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 15

    low = [t.lower() for t in terms]
    results = []
    for f in glob.glob(os.path.join(WIKI, "*", "*.md")):
        base = os.path.basename(f)[:-3]
        if base == name:
            continue
        hits = []
        for c in prose(body_of(f)):
            cl = c.lower()
            if any(t in cl for t in low) and len(c) >= 30:
                hits.append(c)
        if hits:
            results.append((base, hits))

    results.sort(key=lambda r: -len(r[1]))
    print(f"# 概念「{name}」  检索词 {sorted(terms)}")
    print(f"# 正文命中页 {len(results)} 个，共 {sum(len(h) for _, h in results)} 句\n")
    for base, hits in results[:top]:
        print(f"--- [[{base}]]  ({len(hits)} 句)")
        for c in hits[:max_per]:
            print("   •", c[:420])
        print()


main()

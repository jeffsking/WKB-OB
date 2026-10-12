"""Detect remaining empty seeds that are near-duplicates of existing real pages.

A duplicate seed should be REDIRECTED (link rewritten to the real page + seed
removed) rather than filled with a second version of the same content.

Conservative matching: normalised-form equality, or token-set containment where
the existing page is the broader/equivalent page.
"""
import glob
import json
import os
import re

VAULT = "E:/WKB-OB"
WIKI = os.path.join(VAULT, "WIKI")

data = json.load(open(os.path.join(VAULT, ".tools", "_seed_classify.json"), encoding="utf-8"))
empty = {r["name"]: r for r in data["empty"]}
have = {r["name"] for r in data["have_body"]}


def norm(s):
    s = re.sub(r"[（(][^）)]*[）)]", "", s)
    s = re.sub(r"[\s_\-–—×x·、，,。.:：;；\"'“”‘’/]", "", s)
    return s.strip().lower()


def toks(s):
    out = set()
    for z in re.findall(r"[\u4e00-\u9fff]{2,}", s):
        out.add(z)
        if len(z) >= 4:
            out |= {z[i:i + 3] for i in range(len(z) - 2)}
    for e in re.findall(r"[A-Za-z][A-Za-z0-9\-']{3,}", s):
        out.add(e.lower())
    return out


# every non-empty page in the vault
real = {}
for d in ("sources", "concepts", "entities", "comparisons"):
    for f in glob.glob(os.path.join(WIKI, d, "*.md")):
        b = os.path.basename(f)[:-3]
        if b in empty:
            continue
        real[b] = d

real_norm = {}
for b in real:
    real_norm.setdefault(norm(b), []).append(b)
real_toks = {b: toks(b) for b in real}

pairs = []
for name in empty:
    n = norm(name)
    hit = real_norm.get(n)
    if hit and len(set(hit)) == 1:
        pairs.append((name, hit[0], "norm-equal", 1.0))
        continue
    tk = toks(name)
    if not tk:
        continue
    best, score = None, 0.0
    for b, bt in real_toks.items():
        if not bt:
            continue
        inter = len(tk & bt)
        if not inter:
            continue
        s = inter / max(len(tk | bt), 1)          # Jaccard — symmetric, safe
        if s > score:
            best, score = b, s
    if best and score >= 0.62:
        pairs.append((name, best, "jaccard", round(score, 2)))
        continue
    # containment: one token set fully inside the other (>=2 tokens on the small side)
    sub = None
    for b, bt in real_toks.items():
        if not bt or not tk:
            continue
        if tk <= bt and len(tk) >= 2:
            if sub is None or len(bt) < len(real_toks[sub]):
                sub = b
        elif bt <= tk:
            pass
    if sub:
        pairs.append((name, sub, "contained", 0.8))

print(f"疑似重复 seed: {len(pairs)}")
for a, b, how, sc in sorted(pairs, key=lambda x: -x[3]):
    print(f"  [{how} {sc}] [[{a}]]  ->  [[{b}]]")

json.dump(pairs, open(os.path.join(VAULT, ".tools", "_seed_duplicates.json"), "w",
                      encoding="utf-8"), ensure_ascii=False, indent=2)

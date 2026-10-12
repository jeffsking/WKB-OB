"""Find duplicate PAIRS *within* the remaining empty-seed set (both sides are seeds)."""
import json
import os
import re

VAULT = "E:/WKB-OB"
rows = json.load(open(os.path.join(VAULT, ".tools", "_seed_classify2.json"), encoding="utf-8"))
names = [r["name"] for r in rows if r["chars"] < 500]


def toks(s):
    out = set()
    for z in re.findall(r"[\u4e00-\u9fff]{2,}", s):
        out.add(z)
        if len(z) >= 4:
            out |= {z[i:i + 3] for i in range(len(z) - 2)}
    for e in re.findall(r"[A-Za-z][A-Za-z0-9\-']{3,}", s):
        out.add(e.lower())
    return out


tk = {n: toks(n) for n in names}
pairs = []
for i, a in enumerate(names):
    for b in names[i + 1:]:
        ta, tb = tk[a], tk[b]
        if not ta or not tb:
            continue
        inter = len(ta & tb)
        if not inter:
            continue
        j = inter / len(ta | tb)
        sub = ta <= tb or tb <= ta
        if j >= 0.6 or (sub and min(len(ta), len(tb)) >= 2 and len(ta & tb) >= 2):
            pairs.append((a, b, round(j, 2), sub))

print(f"待补集合内部疑似重复: {len(pairs)}")
for a, b, j, sub in sorted(pairs, key=lambda x: -x[2]):
    print(f"  j={j} subset={sub}\n     A: {a}\n     B: {b}")
json.dump(pairs, open(os.path.join(VAULT, ".tools", "_seed_intra_dupes.json"), "w",
                      encoding="utf-8"), ensure_ascii=False, indent=2)

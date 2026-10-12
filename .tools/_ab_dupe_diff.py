"""Diff the 4 timestamped Absorbent Technology variants against their base chapters."""
import glob
import os
import difflib

files = sorted(glob.glob("RAW_FULL/**/Absorbent Technology_ch*.md", recursive=True))

buckets = {}
for f in files:
    b = os.path.basename(f)
    for n in ("ch09", "ch10", "ch11", "ch12"):
        if b.startswith(f"Absorbent Technology_{n}_"):
            key = "ts" if "20260823" in b else "base"
            buckets.setdefault(n, {})[key] = f
            break


def rd(p):
    return open(p, encoding="utf-8", errors="ignore").read().splitlines()


for n in sorted(buckets):
    pair = buckets[n]
    if "base" not in pair or "ts" not in pair:
        print(f"=== {n}: only {[k for k in pair]} -> no pair to diff")
        continue
    a, b = rd(pair["base"]), rd(pair["ts"])
    diffs = [
        l
        for l in difflib.unified_diff(a, b, lineterm="", n=0)
        if l[:1] in "+-" and l[:3] not in ("+++", "---")
    ]
    print(f"=== {n}: base {len(a)}L vs ts {len(b)}L -> {len(diffs)} changed lines ===")
    for l in diffs[:8]:
        print("   ", l[:160])
    print()

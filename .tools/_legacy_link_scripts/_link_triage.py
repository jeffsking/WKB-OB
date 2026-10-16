"""Categorise the 297 truly-missing link targets.

For each missing target decide:
  REDIRECT -> an existing page name (variants, aliases, EN/ZH pairs)
  SEED     -> genuinely absent, needs a placeholder page (no fabricated data)
  REVIEW   -> ambiguous, needs human call
"""
import glob
import os
import re
import json
from collections import Counter, defaultdict

VAULT = "E:/WKB-OB"
WIKI = os.path.join(VAULT, "WIKI")


def norm(s):
    s = re.sub(r"[（(][^）)]*[）)]", "", s)
    s = re.sub(r"[\s_\-–—×x·、，,。.:：;；\"'“”‘’/]", "", s)
    return s.strip().lower()


# ---- existing pages: name -> (dir, aliases) ----
pages = {}      # exact basename
aliases = {}    # normalised -> list of real basenames
for d in ("sources", "concepts", "entities", "comparisons"):
    for f in glob.glob(os.path.join(WIKI, d, "*.md")):
        b = os.path.basename(f)[:-3]
        pages[b] = d
        aliases.setdefault(norm(b), []).append((b, d))
        t = open(f, encoding="utf-8", errors="ignore").read(3000)
        m = re.search(r"^aliases:\s*\[(.*?)\]", t, re.M)
        if m:
            for a in re.findall(r'"([^"]+)"', m.group(1)):
                aliases.setdefault(norm(a), []).append((b, d))

# ---- missing targets: target -> citing pages ----
missing = defaultdict(list)
for d in ("sources", "concepts", "entities", "comparisons"):
    for f in glob.glob(os.path.join(WIKI, d, "*.md")):
        src = os.path.basename(f)[:-3]
        t = open(f, encoding="utf-8", errors="ignore").read()
        for l in set(re.findall(r"\[\[([^\]|#]+)", t)):
            l = l.strip()
            if l and l not in pages:
                missing[l].append(src)

print(f"现有页面 {len(pages)}  |  缺失目标 {len(missing)} 种  |  引用总数 {sum(len(v) for v in missing.values())}")

redirect, seed, review = {}, {}, {}
for target, cited in sorted(missing.items(), key=lambda kv: -len(kv[1])):
    n = norm(target)
    hit = aliases.get(n)
    if hit and len({h[0] for h in hit}) == 1:
        redirect[target] = hit[0][0]
        continue
    # containment match: existing page name contains target or vice versa
    cands = [b for nb, lst in aliases.items() if nb and (nb in n or n in nb) and abs(len(nb) - len(n)) <= 12
             for b, _ in lst]
    cands = sorted(set(cands))
    if len(cands) == 1 and len(n) >= 6:
        redirect[target] = cands[0]
        continue
    if cands and len(n) >= 6:
        review[target] = cands[:4]
        continue
    seed[target] = cited

print(f"\n可改指 REDIRECT : {len(redirect)} 种")
print(f"待裁决 REVIEW   : {len(review)} 种")
print(f"需补 seed 页    : {len(seed)} 种  (引用 {sum(len(v) for v in seed.values())} 处)")

json.dump({"redirect": redirect, "review": review,
           "seed": {k: v for k, v in seed.items()}},
          open(os.path.join(VAULT, ".tools", "_link_triage.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

print("\n--- REDIRECT 明细 ---")
for k, v in sorted(redirect.items(), key=lambda kv: -len(missing[kv[0]])):
    print(f"  {len(missing[k]):>3}x  [[{k}]]  ->  [[{v}]]")

print("\n--- REVIEW 明细（含候选） ---")
for k, c in sorted(review.items(), key=lambda kv: -len(missing[kv[0]]))[:25]:
    print(f"  {len(missing[k]):>3}x  [[{k}]]  候选: {c}")

print("\n--- SEED 页（按引用频次 top 60） ---")
for k, v in sorted(seed.items(), key=lambda kv: -len(kv[1]))[:60]:
    print(f"  {len(v):>3}x  {k}")

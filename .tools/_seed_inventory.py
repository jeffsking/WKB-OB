"""Inventory seed pages + citation counts, and build a fill-in priority list."""
import glob
import os
import re
import json
import collections

VAULT = "E:/WKB-OB"
WIKI = os.path.join(VAULT, "WIKI")

seeds = []
for d in ("concepts", "entities"):
    for f in glob.glob(os.path.join(WIKI, d, "*.md")):
        t = open(f, encoding="utf-8", errors="ignore").read()
        if re.search(r"^status:\s*seed", t, re.M) or re.search(r"tags:\s*\[seed", t, re.M):
            m = re.search(r"^## Cited by[^\n]*?（(\d+) 处", t, re.M)
            n = int(m.group(1)) if m else 0
            cited = re.findall(r"^- \[\[([^\]]+)\]\]", t, re.M)
            cited = [c for c in cited if not c.startswith(("吸收",))]
            # links under "Cited by" section only
            sec = re.search(r"## Cited by[\s\S]*?(?=\n## |\Z)", t)
            cl = re.findall(r"\[\[([^\]|#]+)\]\]", sec.group(0)) if sec else []
            typ = "entity" if d == "entities" else "concept"
            seeds.append({"dir": d, "name": os.path.basename(f)[:-3], "type": typ,
                          "citations": n, "cited_by": sorted(set(cl))})

print(f"seed 页总数: {len(seeds)}")
print("  概念:", sum(1 for s in seeds if s["type"] == "concept"))
print("  实体:", sum(1 for s in seeds if s["type"] == "entity"))
c = collections.Counter(s["citations"] for s in seeds)
print("  引用分布:", dict(sorted(c.items(), reverse=True)))

seeds.sort(key=lambda s: -s["citations"])
json.dump(seeds, open(os.path.join(VAULT, ".tools", "_seed_inventory.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

print(f"\n=== 引用 >=2 的 seed（{sum(1 for s in seeds if s['citations']>=2)} 个）===")
for s in seeds:
    if s["citations"] >= 2:
        print(f"  {s['citations']:>2}x  {s['type']:<7} {s['name']}")

print(f"\n=== 引用 =1 的 seed: {sum(1 for s in seeds if s['citations']==1)} 个 ===")
print(f"=== 引用 =0（无 Cited by 计数）: {sum(1 for s in seeds if s['citations']==0)} 个 ===")

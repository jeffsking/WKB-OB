"""Build the remaining-seed fill plan: 176 pages ordered by digest richness,
grouped into batches for agent dispatch.
"""
import glob
import json
import os
import re
import collections

VAULT = "E:/WKB-OB"
rows = json.load(open(os.path.join(VAULT, ".tools", "_seed_classify2.json"), encoding="utf-8"))
seeds = {r["name"]: r for r in rows if r["chars"] < 500}

out = []
for f in glob.glob(os.path.join(VAULT, ".tools", "_seed_ctx", "*.txt")):
    name = os.path.basename(f)[:-4]
    if name not in seeds:
        continue
    t = open(f, encoding="utf-8", errors="ignore").read()
    m = re.search(r"全库正文命中 (\d+) 页，(\d+) 句", t)
    out.append({"name": name, "sent": int(m.group(2)) if m else 0,
                "dir": seeds[name]["dir"], "chars": seeds[name]["chars"]})

out.sort(key=lambda r: -r["sent"])

c = collections.Counter()
for r in out:
    b = "A >=200" if r["sent"] >= 200 else ("B 50-199" if r["sent"] >= 50 else
                                            ("C 10-49" if r["sent"] >= 10 else "D <10"))
    c[b] += 1
print("待补 seed:", len(out), " digest 丰富度:", dict(sorted(c.items())))

CHUNK = 8
batches = [out[i:i + CHUNK] for i in range(0, len(out), CHUNK)]
print(f"分 {len(batches)} 批，每批 {CHUNK} 页\n")
for i, b in enumerate(batches, 1):
    print(f"--- 批 {i:02d} ({len(b)} 页)")
    for r in b:
        print(f"      {r['sent']:>4}句 {r['dir']:<9} {r['name']}")

json.dump(batches, open(os.path.join(VAULT, ".tools", "_seed_fill_plan.json"), "w",
                        encoding="utf-8"), ensure_ascii=False, indent=2)
print("\n写入 .tools/_seed_fill_plan.json")

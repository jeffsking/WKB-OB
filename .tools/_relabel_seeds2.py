"""Re-label seeds that already carry real content: status: seed -> growing."""
import json
import os
import re

VAULT = "E:/WKB-OB"
rows = json.load(open(os.path.join(VAULT, ".tools", "_seed_classify2.json"), encoding="utf-8"))

n = 0
for r in rows:
    if r["chars"] < 500:
        continue
    p = r["path"]
    t = open(p, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if not m:
        continue
    fm = m.group(1)
    fm2 = re.sub(r"^status:\s*seed\s*$", "status: growing", fm, flags=re.M)
    fm2 = re.sub(r"^updated:\s*\S+\s*$", "updated: 2026-09-30", fm2, flags=re.M)
    if fm2 == fm:
        continue
    open(p, "w", encoding="utf-8", newline="\n").write("---\n" + fm2 + "\n---\n" + t[m.end():])
    n += 1
    print("  relabelled:", r["name"])

print(f"重标 {n} 页 status: seed -> growing")

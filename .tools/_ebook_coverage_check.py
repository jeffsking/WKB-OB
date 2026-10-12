"""Authoritative ebook compile coverage: judge by source_path registered in
WIKI/sources/*.md front matter (never by mtime, never by filename guessing).

Usage: python .tools/_ebook_coverage_check.py
"""
import json
import glob
import os
import re

SRC = "WIKI/sources"

# 1) collect every source_path / source_paths value registered in source pages
covered = set()
for f in glob.glob(os.path.join(SRC, "*.md")):
    try:
        t = open(f, encoding="utf-8", errors="ignore").read(6000)
    except OSError:
        continue
    for mm in re.finditer(r"^\s*source_paths:\s*\[(.*?)\]", t, re.M):
        for v in re.findall(r'"([^"]+)"', mm.group(1)):
            covered.add(v.strip())
    for mm in re.finditer(r"^\s*source_path:\s*[\"']?([^\"'\n#]+)", t, re.M):
        covered.add(mm.group(1).strip().strip('"').strip("'"))

m = json.load(open(".tools/ebook_compile_manifest.json", encoding="utf-8"))

print("registered source_paths in WIKI/sources :", len(covered))
print()

totals = {}
rows = []
for b in m["books"]:
    ch = b.get("chapter_source_paths") or []
    n = b.get("n_chapters") or 0
    if not ch:
        continue
    done = [p for p in ch if p in covered]
    todo = [p for p in ch if p not in covered]
    pri = b.get("priority", "?")
    totals[pri] = totals.get(pri, 0) + len(todo)
    rows.append((pri, b["name"], len(done), len(ch), todo))

rows.sort(key=lambda r: (0 if r[0] == "P0" else 1 if r[0] == "P1" else 2, -r[3]))
for pri, name, d, tot, todo in rows:
    mark = "DONE " if d == tot else "PART "
    print(f"[{pri}] {mark} {name}: {d}/{tot}  pending={tot - d}")
    for t in todo[:4]:
        print("       -", os.path.basename(t))
    if len(todo) > 4:
        print(f"       ... 其余 {len(todo) - 4} 章")
    print()

print("=== PENDING BY PRIORITY ===")
for k in sorted(totals):
    print(f"  {k}: {totals[k]}")
print("  ALL:", sum(totals.values()))

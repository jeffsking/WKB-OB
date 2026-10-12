# -*- coding: utf-8 -*-
"""Check per-book compile coverage for the ebook manifest against WIKI/sources."""
import json, os, re, sys

VAULT = r"E:\WKB-OB"
SRC = os.path.join(VAULT, "WIKI", "sources")
MANIFEST = os.path.join(VAULT, ".tools", "ebook_compile_manifest.json")

# Collect all source_path values already registered in WIKI/sources
registered = set()
fm_re = re.compile(r"^(?:source_path:[ \t]*(.*?)[ \t]*$|source_paths:[ \t]*$)", re.M)
for fn in os.listdir(SRC):
    if not fn.endswith(".md"):
        continue
    with open(os.path.join(SRC, fn), encoding="utf-8", errors="replace") as fh:
        head = fh.read(4000)
    # single-line source_path (path may contain spaces, e.g. "Ebook Extract")
    m = re.search(r"^source_path:[ \t]*(.*?)[ \t]*$", head, re.M)
    if m:
        registered.add(m.group(1).strip().strip('"'))
    # multi-value source_paths list
    m2 = re.search(r"^source_paths:[ \t]*\n((?:[ \t]*-[ \t]*.+\n)+)", head, re.M)
    if m2:
        for line in m2.group(1).splitlines():
            v = line.strip().lstrip("- ").strip().strip('"')
            if v:
                registered.add(v)

def norm(p):
    """Normalize: unify RAW/ vs RAW_FULL/ prefix, drop the fixed IMA sync prefix."""
    p = p.replace("\\", "/").strip().strip('"')
    p = re.sub(r"^(?:RAW_FULL|RAW)/ima_sync/[^/]*/WKB/", "", p, flags=re.I)
    return p.lower()

reg_norm = {norm(x) for x in registered}

m = json.load(open(MANIFEST, encoding="utf-8"))
books = m["books"] if isinstance(m, dict) and "books" in m else m

rows = []
for b in books:
    name = b.get("name", "?")
    pr = b.get("priority", "?")
    ca = b.get("compile_as", "?")
    chs = [c for c in b.get("chapter_source_paths", []) if c]
    done = [c for c in chs if norm(c) in reg_norm]
    rows.append((pr, ca, len(chs), len(done), name))

def k(r):
    return (r[0], r[1], -r[2], r[4])

print(f"{'Prio':5} {'mode':10} {'ch':>3} {'done':>4}  book")
print("-" * 90)
tot_ch = tot_done = 0
for pr, ca, n, d, name in sorted(rows, key=k):
    if n == 0:
        continue
    tot_ch += n; tot_done += d
    flag = "✅" if d == n else ("⬜" if d == 0 else "🟡")
    print(f"{pr:5} {ca:10} {n:3d} {d:4d} {flag}  {name}")

print("-" * 90)
print(f"章节书合计: {tot_done}/{tot_ch} 章节页已落盘")

print("\n=== index_only 书（P0/P1 轻量索引）===")
for b in sorted(books, key=lambda x: (x.get("priority", "?"), x.get("name", "?"))):
    if b.get("compile_as") == "index_only":
        print(f"  {b.get('priority'):3}  {b.get('name')}")

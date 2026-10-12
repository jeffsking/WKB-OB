# -*- coding: utf-8 -*-
"""For each uncompiled P0 chapter book, show its chapter paths + detect overlap with already-compiled index pages."""
import json, os, re

VAULT = r"E:\WKB-OB"
SRC = os.path.join(VAULT, "WIKI", "sources")
MANIFEST = os.path.join(VAULT, ".tools", "ebook_compile_manifest.json")

def norm(p):
    p = p.replace("\\", "/").strip().strip('"')
    p = re.sub(r"^(?:RAW_FULL|RAW)/ima_sync/[^/]*/WKB/", "", p, flags=re.I)
    return p.lower()

# gather all registered source_paths (full, incl. spaces)
reg = {}
for fn in os.listdir(SRC):
    if not fn.endswith(".md"):
        continue
    head = open(os.path.join(SRC, fn), encoding="utf-8", errors="replace").read(4000)
    m = re.search(r"^source_path:[ \t]*(.*?)[ \t]*$", head, re.M)
    if m:
        reg[norm(m.group(1))] = fn

m = json.load(open(MANIFEST, encoding="utf-8"))
books = m["books"] if isinstance(m, dict) and "books" in m else m

target = [
    "SAP Research Advances", "Superabsorbent_Polymers_SAP_Composites",
    "Stimuli_Responsive_PCM_Optical", "Stimuli_Responsive_Photonic_Coatings",
    "Stimuli_Responsive_Polymers_DeepBook", "Mechanochromic_Fluorescent_Polymers_AIE",
    "Photochromism_Dihydroindolizines", "Ancient_Dyes_Pigments_Chemistry",
    "handbook-of-adhesive-technology",
]
for b in books:
    if b.get("name") in target:
        print("=" * 96)
        print("BOOK:", b["name"], "| prio", b.get("priority"), "| root_file_rel:", b.get("root_file_rel"))
        for c in b.get("chapter_source_paths", []):
            key = norm(c)
            hit = reg.get(key)
            print("   ch:", os.path.basename(c))
            print("       ", "→ COVERED by " + hit if hit else "     → NOT compiled")
        if b.get("root_file_rel"):
            rkey = norm(b["root_file_rel"])
            print("   root:", os.path.basename(b["root_file_rel"]),
                  "→ COVERED by " + reg[rkey] if reg.get(rkey) else "→ NOT compiled")

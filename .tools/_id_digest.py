"""Dump a compact digest of each of the 13 new Industrial Drying pages so
key_claims can be written accurately (no fabrication)."""
import glob
import os
import re

pages = sorted(
    p
    for p in glob.glob("WIKI/sources/Industrial Drying Ch*.md")
    if os.path.basename(p) not in ("",)
)
for f in pages:
    t = open(f, encoding="utf-8", errors="ignore").read()
    h2 = re.findall(r"^##\s+(.+)$", t, re.M)
    h3 = re.findall(r"^###\s+(.+)$", t, re.M)
    q = re.findall(r'^>\s+"(.+?)"\s*\((?:p{1,2}\.)?[^\n]*\)\s*$', t, re.M)
    num = re.findall(r"\b(\d[\d,]*\s?(?:%|kJ|kg|m/s|kPa|bar|mJ|mm|g|cm|s|°C|W))\b", t)
    print("=" * 70)
    print(os.path.basename(f))
    print("  H2:", " | ".join(x.strip()[:44] for x in h2[:8]))
    print("  H3:", " | ".join(x.strip()[:34] for x in h3[:12]))
    print("  QUOTES:")
    for x in q[:6]:
        print("    -", x[:150])
    print("  NUMS:", " ".join(sorted(set(num))[:18]))
    print()

import json, os, sys

base = "E:/WKB-OB"

items = []

def add(dst, content_escaped):
    items.append((dst, content_escaped))

# Item 8: Hypothesis Map (smallest)
add(
    "RAW_FULL/ima_sync/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Hypothesis Map.xlsx.md",
    r'''[Depend - Historical]\n|Key||||||||||||||||||||||||\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n|Lower Rewet||||||||||||||||||||||||\n|Lower to No Change|||||||||||||||||||||||||Pre-ATACAMA surges (Ct8, CT9, dual layers)|\n|No Change|||||||||||||||||||||||||39840 - untreated liner higher leakage|\n|Higher to No Change|||||||||||||||||||||||||What changed in AD to make improvements to rewet &amp; intake?|\n|Higher Rewet|||||||||||||||||||||||||BONNIE - have they learned anything on rewet? (Liz Bradley)|\n|Not Tested|||||||||||||||||||||||||Was Shalag 3 promoting one-way flow?|\n\n\n[Depend - Proposed]\n|Proposed based on reasearch into principle drivers of rewet|\n|---|\n|Key|\n|Lower Rewet|\n|Lower to No Change|\n|No Change|\n|Higher to No Change|\n|Higher Rewet|\n|Not Tested|\n\n\n[Baby-Child Care]\n|Key|\n|---|\n|Lower Rewet|\n|Lower to No Change|\n|No Change|\n|Higher to No Change|\n|Higher Rewet|\n|Not Tested|\n\n'''
)

for dst, content_escaped in items:
    full = os.path.join(base, dst)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    content = json.loads('"' + content_escaped + '"')
    with open(full, "w", encoding="utf-8", newline="") as f:
        f.write(content)
    print(f"OK: {os.path.basename(dst)[:30]} ({len(content)} chars)")

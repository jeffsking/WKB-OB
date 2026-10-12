"""Classify remaining seed pages: truly empty vs legacy-seed-with-content.

'status: seed' alone is misleading — the 2026-09-29 batch marked pages seed but
several already carry real body content.
"""
import glob
import os
import re
import json

VAULT = "E:/WKB-OB"
WIKI = os.path.join(VAULT, "WIKI")

rows = []
for d in ("concepts", "entities"):
    for f in glob.glob(os.path.join(WIKI, d, "*.md")):
        t = open(f, encoding="utf-8", errors="ignore").read()
        if not (re.search(r"^status:\s*seed", t, re.M) or re.search(r"tags:\s*\[seed", t, re.M)):
            continue
        m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
        body = t[m.end():] if m else t
        # strip the boilerplate seed notice + metadata table + link lists
        plain = re.sub(r"^[#>|\-*].*$", "", body, flags=re.M)
        plain = re.sub(r"\[\[([^\]|#]+)\]\]", "", plain)
        n = len(plain.strip())
        legacy = not re.search(r"tags:\s*\[seed, 待补\]", t)
        rows.append({"dir": d, "name": os.path.basename(f)[:-3],
                     "body_chars": n, "legacy": legacy, "path": f})

empty = [r for r in rows if r["body_chars"] < 400]
have = [r for r in rows if r["body_chars"] >= 400]
print(f"status:seed 页面 {len(rows)}")
print(f"  已有实质正文 (>=400 字) : {len(have)}   <- 只需改 status，无需补内容")
print(f"  基本空白 (<400 字)      : {len(empty)}   <- 真正待补")
print()
print("--- 已有正文的 legacy seed（前 30）---")
for r in sorted(have, key=lambda r: -r["body_chars"])[:30]:
    tag = "legacy" if r["legacy"] else "new"
    print(f"  {r['body_chars']:>6}字 [{tag}] {r['dir'][:-1]:<8} {r['name']}")
print()
print("--- 真正空白（前 30）---")
for r in sorted(empty, key=lambda r: r["body_chars"])[:30]:
    tag = "legacy" if r["legacy"] else "new"
    print(f"  {r['body_chars']:>6}字 [{tag}] {r['dir'][:-1]:<8} {r['name']}")

json.dump({"have_body": have, "empty": empty},
          open(os.path.join(VAULT, ".tools", "_seed_classify.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

"""Accurate seed triage: how much REAL content does each seed page carry?

Differs from _seed_classify.py by KEEPING table rows and list items (earlier
version stripped them, which mis-labelled table-heavy legacy pages as empty).
Excludes only: the seed banner, the Metadata table, and pure link-list lines.
"""
import glob
import json
import os
import re

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
        keep = []
        for line in body.splitlines():
            s = line.strip()
            if not s:
                continue
            if s.startswith("> ⏳") or s.startswith("> 📌") or s.startswith("> 🔴"):
                continue                                   # seed banner
            if re.fullmatch(r"[-*]\s*\[\[[^\]]+\]\]\s*.*", s):   # pure link list
                continue
            if s.startswith("## Metadata") or s.startswith("| Item 项目") or s.startswith("|---"):
                continue
            keep.append(re.sub(r"\[\[([^\]|#]+)(\|[^\]]+)?\]\]", r"\1", s))
        txt = "\n".join(keep)
        # drop the standard seed sections that carry no content
        txt = re.sub(r"## (Metadata 元数据|Cited by[^\n]*|Pending 待补维度|Open Questions 待补|Related Sources 关联来源)[\s\S]*?(?=\n## |\Z)", "", txt)
        n = len(re.sub(r"\s+", "", txt))
        rows.append({"dir": d, "name": os.path.basename(f)[:-3], "chars": n, "path": f})

rich = [r for r in rows if r["chars"] >= 500]
mid = [r for r in rows if 150 <= r["chars"] < 500]
thin = [r for r in rows if r["chars"] < 150]

print(f"status:seed 页面 {len(rows)}")
print(f"  已有实质内容 (>=500 字) : {len(rich)}  -> 只需改 status")
print(f"  部分内容   (150-499 字) : {len(mid)}  -> 补关键缺口")
print(f"  基本空白   (<150 字)    : {len(thin)}  -> 需从来源补内容")
print()
print("--- 部分内容 (150-499 字) ---")
for r in sorted(mid, key=lambda r: -r["chars"]):
    print(f"  {r['chars']:>5}  {r['dir'][:-1]:<8} {r['name']}")
print()
print("--- 基本空白，前 40 ---")
for r in sorted(thin, key=lambda r: -r["chars"])[:40]:
    print(f"  {r['chars']:>5}  {r['dir'][:-1]:<8} {r['name']}")

json.dump(rows, open(os.path.join(VAULT, ".tools", "_seed_classify2.json"), "w",
                     encoding="utf-8"), ensure_ascii=False, indent=2)

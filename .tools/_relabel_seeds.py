"""Re-label legacy seed pages that already carry real body content:
status: seed -> growing, updated -> 2026-09-30.

Only touches pages whose body (after stripping seed boilerplate / headings /
link lists) is >= 400 chars. Metadata-only change; no content altered.
"""
import json
import os
import re

VAULT = "E:/WKB-OB"
data = json.load(open(os.path.join(VAULT, ".tools", "_seed_classify.json"), encoding="utf-8"))

fixed = 0
for r in data["have_body"]:
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
    out = "---\n" + fm2 + "\n---\n" + t[m.end():]
    open(p, "w", encoding="utf-8", newline="\n").write(out)
    fixed += 1

print(f"重标 status: seed -> growing 共 {fixed} 页")
print(f"剩余仍为 seed: {len(data['empty'])} 页（真正空白，待补内容）")

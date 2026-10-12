"""Build compile batches for the 40 pending Handbook of Industrial Drying chapters.

Outputs .tools/compile_batches/idb_XX.json with items:
  {src, title_hint, chapter}
plus a summary. 5 chapters per batch (subagent sweet spot).
"""
import glob
import json
import os
import re

VAULT = "E:/WKB-OB"


def body_of(p):
    t = open(p, encoding="utf-8", errors="ignore").read()
    if t.startswith("---"):
        i = t.find("\n---", 3)
        if i > 0:
            t = t[i + 4:]
    return t


# 1) already-compiled source_paths
compiled = set()
for f in glob.glob(os.path.join(VAULT, "WIKI", "sources", "*.md")):
    t = open(f, encoding="utf-8", errors="ignore").read(6000)
    for mm in re.finditer(r"^\s*source_paths:\s*\[(.*?)\]", t, re.M):
        for v in re.findall(r'"([^"]+)"', mm.group(1)):
            compiled.add(v.strip())
    for mm in re.finditer(r'^\s*source_path:\s*["\']?([^"\'\n#]+)', t, re.M):
        compiled.add(mm.group(1).strip().strip('"').strip("'"))

m = json.load(open(os.path.join(VAULT, ".tools", "ebook_compile_manifest.json"), encoding="utf-8"))
book = next(b for b in m["books"] if b["name"] == "Handbook_of_Industrial_Drying")
pending = [p for p in book["chapter_source_paths"] if p not in compiled]
print(f"工业干燥待编译章节: {len(pending)}")

# 2) title hint from each source file's H1 / first heading
items = []
for p in pending:
    full = os.path.join(VAULT, p.replace("/", os.sep))
    hint, ch = "", ""
    mm = re.search(r"ch(\d{2})", os.path.basename(p))
    ch = mm.group(1) if mm else ""
    if os.path.exists(full):
        b = body_of(full)
        h = re.search(r"^#\s+Chapter\s*\d+\s*[—–-]\s*(.+)$", b, re.M)
        if not h:
            h = re.search(r"^##\s+Chapter\s*\d+[.:—–-]?\s*(.+)$", b, re.M)
        if h:
            hint = h.group(1).strip()[:80]
    if not hint:
        hint = "（标题未在源文件中找到，请打开源文件自行确定）"
    items.append({"src": p, "chapter": ch, "title_hint": hint,
                  "bytes": os.path.getsize(full) if os.path.exists(full) else 0})

items.sort(key=lambda x: int(x["chapter"]) if x["chapter"] else 999)

CHUNK = 5
batches = [items[i:i + CHUNK] for i in range(0, len(items), CHUNK)]
outdir = os.path.join(VAULT, ".tools", "compile_batches")
idx = []
for i, b in enumerate(batches, 1):
    name = f"idb_{i:02d}"
    fn = os.path.join(outdir, name + ".json")
    json.dump({"batch": name, "book": "Handbook_of_Industrial_Drying", "items": b},
              open(fn, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    idx.append({"batch": name, "n": len(b), "file": ".tools/compile_batches/" + name + ".json"})
    print(f"--- {name} ({len(b)} 章)")
    for it in b:
        print(f"      Ch{it['chapter']}  {it['title_hint'][:56]}")

json.dump(idx, open(os.path.join(VAULT, ".tools", "_id_batch_index.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print(f"\n共 {len(batches)} 批 -> .tools/_id_batch_index.json")

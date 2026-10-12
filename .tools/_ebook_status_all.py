"""WKB-OB ebook batch-compile status: P0 / P1 / P2.

Unit definitions (state them explicitly in the report — do not mix them up):
  书 (book)   = one ebook title in the manifest
  章 (chapter)= one compilable chapter/report file under a book
  索引页      = one book-index page for a book compiled as index_only
  批次 (batch)= one agent dispatch unit (.tools/compile_batches/*.json)

Authoritative completion judge = `source_path` registered in WIKI/sources
front matter. Never mtime, never filename guessing.
"""
import glob
import os
import re
import json

VAULT = "E:/WKB-OB"
SRC = os.path.join(VAULT, "WIKI", "sources")


def load_covered():
    cov = {}
    for f in glob.glob(os.path.join(SRC, "*.md")):
        t = open(f, encoding="utf-8", errors="ignore").read(6000)
        page = os.path.basename(f).rsplit(".md", 1)[0]
        for mm in re.finditer(r"^\s*source_paths:\s*\[(.*?)\]", t, re.M):
            for v in re.findall(r'"([^"]+)"', mm.group(1)):
                cov[v.strip()] = page
        for mm in re.finditer(r'^\s*source_path:\s*["\']?([^"\'\n#]+)', t, re.M):
            cov[mm.group(1).strip().strip('"').strip("'")] = page
    return cov


def rollup(books, covered, label):
    ch_done = ch_tot = 0
    root_done = root_tot = 0
    full = part = 0
    rows = []
    root_pending = []
    for b in books:
        chs = b.get("chapter_source_paths") or []
        r = b.get("root_file_rel")
        d = sum(1 for c in chs if c in covered)
        ch_done += d
        ch_tot += len(chs)
        if r:
            root_tot += 1
            if r in covered:
                root_done += 1
            else:
                root_pending.append(b["name"])
        if chs:
            if d == len(chs):
                full += 1
            else:
                part += 1
        rows.append((b["name"], d, len(chs), r in covered if r else None))
    return dict(label=label, ch_done=ch_done, ch_tot=ch_tot, root_done=root_done,
                root_tot=root_tot, full=full, part=part, rows=rows,
                root_pending=root_pending)


covered = load_covered()
p0p2 = json.load(open(os.path.join(VAULT, ".tools", "ebook_compile_manifest.json"), encoding="utf-8"))
p1 = json.load(open(os.path.join(VAULT, ".tools", "ebook_p1_manifest.json"), encoding="utf-8"))

print("WIKI/sources 页面总数:", len(glob.glob(os.path.join(SRC, "*.md"))))
print("已登记 source_path:", len(covered))
print()

print("=" * 76)
print("① P0  （scope: 核心卫材材料与工艺）")
print("=" * 76)
r0 = rollup([b for b in p0p2["books"] if b["priority"] == "P0"], covered, "P0")
print(f"  书: {len(r0['rows'])}  全书完成: {r0['full']}  未完成: {r0['part']}")
print(f"  章: {r0['ch_done']}/{r0['ch_tot']}")
print("\n  未完成书明细:")
for n, d, t, rc in r0["rows"]:
    if t and d < t:
        print(f"    PART  {n[:52]:<52} {d:>3}/{t}")

print()
print("=" * 76)
print("② P1  （scope: 高分子/纤维/智能材料；大部头仅建索引页）")
print("=" * 76)
r1 = rollup(p1["books"], covered, "P1")
n_with_ch = sum(1 for n, d, t, rc in r1["rows"] if t)
print(f"  书: {len(r1['rows'])}   逐章编译书: {n_with_ch}   索引页书: {r1['root_tot']}")
print(f"  章: {r1['ch_done']}/{r1['ch_tot']}   全书章节完成: {r1['full']}   部分: {r1['part']}")
print(f"  索引页: {r1['root_done']}/{r1['root_tot']}")
print("\n  未完成章明细:")
for n, d, t, rc in r1["rows"]:
    if t and d < t:
        print(f"    PART  {n[:52]:<52} {d:>3}/{t}")
print("\n  未建索引页:")
for n in r1["root_pending"]:
    print("    TODO -", n)

print()
print("=" * 76)
print("③ P2  （scope: cosmetic / ancient，compile_as=index_only）")
print("=" * 76)
r2 = rollup([b for b in p0p2["books"] if b["priority"] == "P2"], covered, "P2")
print(f"  书: {len(r2['rows'])}   索引页: {r2['root_done']}/{r2['root_tot']}")
for n, d, t, rc in r2["rows"]:
    print(f"    {'DONE' if rc else 'TODO'}  {n[:52]:<52} 章 {d}/{t} (index_only)")

print()
print("=" * 76)
print("合计")
print("=" * 76)
print(f"  章页落盘: P0 {r0['ch_done']}/{r0['ch_tot']}  +  P1 {r1['ch_done']}/{r1['ch_tot']}"
      f"  =  {r0['ch_done'] + r1['ch_done']}/{r0['ch_tot'] + r1['ch_tot']}")
print(f"  索引页: P1 {r1['root_done']}/{r1['root_tot']}  +  P2 {r2['root_done']}/{r2['root_tot']}")
print(f"  待办：P0 缺 {r0['ch_tot'] - r0['ch_done']} 章 | "
      f"P1 缺 {r1['ch_tot'] - r1['ch_done']} 章（大部头，按规则跳过）+ {len(r1['root_pending'])} 索引页")

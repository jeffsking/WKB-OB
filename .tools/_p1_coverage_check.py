"""P1 ebook coverage: judge by source_path registered in WIKI/sources front matter.
Also reconciles the user's "38 项 / 52 项" book-count framing.
"""
import glob
import os
import re
import json

SRC = "WIKI/sources"

covered = {}
for f in glob.glob(os.path.join(SRC, "*.md")):
    t = open(f, encoding="utf-8", errors="ignore").read(6000)
    page = os.path.basename(f).rsplit(".md", 1)[0]
    for mm in re.finditer(r"^\s*source_paths:\s*\[(.*?)\]", t, re.M):
        for v in re.findall(r'"([^"]+)"', mm.group(1)):
            covered[v.strip()] = page
    for mm in re.finditer(r'^\s*source_path:\s*["\']?([^"\'\n#]+)', t, re.M):
        covered[mm.group(1).strip().strip('"').strip("'")] = page

p1 = json.load(open(".tools/ebook_p1_manifest.json", encoding="utf-8"))
p0p2 = json.load(open(".tools/ebook_compile_manifest.json", encoding="utf-8"))

print("WIKI/sources 页面总数:", len(glob.glob(os.path.join(SRC, "*.md"))))
print("已登记 source_path 数:", len(covered))
print()

# ---------- P1 chapter books ----------
print("=" * 74)
print("P1 逐章编译书（12 本 / 80 章）")
print("=" * 74)
d_tot = t_tot = 0
for b in p1["books"]:
    chs = b["chapter_source_paths"]
    if not chs:
        continue
    d = [c for c in chs if c in covered]
    d_tot += len(d)
    t_tot += len(chs)
    print(f"  {'DONE' if len(d)==len(chs) else 'PART'}  {b['name'][:46]:<46} {len(d):>3}/{len(chs)}")
print(f"  --> P1 章节合计: {d_tot}/{t_tot}")

# ---------- P1 index books ----------
print()
print("=" * 74)
print("P1 只建索引页（31 本）")
print("=" * 74)
idx_done = idx_tot = 0
idx_pending = []
for b in p1["books"]:
    if b["chapter_source_paths"]:
        continue
    root = b["root_file_rel"]
    if not root:
        print(f"  SKIP  {b['name'][:46]:<46} (无 root 文件，源侧无内容)")
        continue
    idx_tot += 1
    hit = root in covered
    idx_done += 1 if hit else 0
    if not hit:
        idx_pending.append(b["name"])
    print(f"  {'DONE' if hit else 'TODO'}  {b['name'][:46]:<46}")
print(f"  --> P1 索引页: {idx_done}/{idx_tot}")

print()
print("=" * 74)
print(f"P1 合计落盘页面: {d_tot}（章）+ {idx_done}（索引） = {d_tot + idx_done}")
print(f"P1 合计待办: {t_tot - d_tot}（章）+ {idx_tot - idx_done}（索引）")
print("=" * 74)
if idx_pending:
    print("\n待建索引页清单:")
    for n in idx_pending:
        print("  -", n)

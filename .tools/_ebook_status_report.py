"""Definitive P0/P1/P2 status report for the WKB-OB ebook batch compile plan.

Judge completion by `source_path` registered in WIKI/sources front matter
(never mtime, never filename guessing).
"""
import glob
import os
import re
import json
import collections

# ---------- 1. what has actually been compiled ----------
compiled = {}          # source_path -> page file
for f in glob.glob("WIKI/sources/*.md"):
    t = open(f, encoding="utf-8", errors="ignore").read(6000)
    page = os.path.basename(f).rsplit(".md", 1)[0]
    for mm in re.finditer(r"^\s*source_paths:\s*\[(.*?)\]", t, re.M):
        for v in re.findall(r'"([^"]+)"', mm.group(1)):
            compiled[v.strip()] = page
    for mm in re.finditer(r'^\s*source_path:\s*["\']?([^"\'\n#]+)', t, re.M):
        compiled[mm.group(1).strip().strip('"').strip("'")] = page

m = json.load(open(".tools/ebook_compile_manifest.json", encoding="utf-8"))

# ---------- 2. section map for Handbook of Industrial Drying ----------
SEC = [
    ("A 原理与计算基础", range(1, 6)),
    ("B 设备/干燥器类型", range(6, 21)),
    ("C 物料品类分论", range(21, 44)),
    ("D 系统与辅助工程", range(44, 50)),
    ("E 单元操作与经济", range(50, 54)),
]
KEY_CH = {33, 34, 35, 36, 40, 41}   # 卫材关键轴线 per book index page


def section_of(n):
    for label, r in SEC:
        if n in r:
            return label
    return "?"


# ---------- 3. per-book rollup ----------
rows = []
for b in m["books"]:
    ch = b.get("chapter_source_paths") or []
    done = [p for p in ch if p in compiled]
    todo = [p for p in ch if p not in compiled]
    rows.append((b.get("priority"), b["name"], len(done), len(ch), todo, b))

rows.sort(key=lambda r: (0 if r[0] == "P0" else 2, -r[3], r[1]))

print("=" * 78)
print("WKB-OB Ebook 分批编译 — P0 / P1 / P2 状态总览")
print("manifest generated:", m.get("generated"), "| scope:", m.get("scope"))
print("=" * 78)

buckets = collections.OrderedDict([("P0", []), ("P1", []), ("P2", [])])
for r in rows:
    if r[2] == r[3] and r[3] == 0:
        continue
    buckets.setdefault(r[0], []).append(r)

for pri in ("P0", "P1", "P2"):
    rs = buckets.get(pri, [])
    if not rs:
        print(f"\n### {pri}：无（清单中不存在该优先级条目）")
        continue
    d = sum(r[2] for r in rs)
    t = sum(r[3] for r in rs)
    full = [r for r in rs if r[2] == r[3]]
    part = [r for r in rs if r[2] < r[3]]
    print(f"\n### {pri}：{len(rs)} 本 | 章节 {d}/{t} | 全书完成 {len(full)} 本 | 未完成 {len(part)} 本")
    print("-" * 74)
    for _, name, dn, tot, todo, b in rs:
        tag = "DONE " if dn == tot else "PART "
        print(f"  {tag} {name:<52} {dn:>3}/{tot:<3}")
    for _, name, dn, tot, todo, b in part:
        print(f"\n  >> 未完成明细 {name}:")
        for p in todo:
            bn = os.path.basename(p)
            mm = re.search(r"ch(\d{2})", bn)
            if mm:
                n = int(mm.group(1))
                star = "★" if n in KEY_CH else " "
                print(f"      {star} Ch{n:02d}  [{section_of(n)}]  {bn}")
            else:
                print(f"        {bn}")

# ---------- 4. Industrial Drying section triage ----------
print("\n" + "=" * 78)
print("Handbook of Industrial Drying — 40 章待编译，按板块归类")
print("=" * 78)
for _, name, dn, tot, todo, b in rows:
    if name != "Handbook_of_Industrial_Drying":
        continue
    bysec = collections.defaultdict(list)
    for p in todo:
        mm = re.search(r"ch(\d{2})", os.path.basename(p))
        n = int(mm.group(1)) if mm else 0
        bysec[section_of(n)].append(n)
    for label, _ in SEC:
        ns = sorted(bysec.get(label, []))
        if not ns:
            continue
        star = " ← 含卫材关键章" if any(n in KEY_CH for n in ns) else ""
        print(f"\n  {label}: {len(ns)} 章{star}")
        print("     " + ", ".join(f"Ch{n:02d}" for n in ns))

print("\n" + "=" * 78)
print("合计待编译：", sum(len(r[4]) for r in rows), "章 /",
      f"manifest 总章数 {sum(r[3] for r in rows)}")

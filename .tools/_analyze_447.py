import glob, re, os, collections, statistics

VAULT = "E:/WKB-OB"
rawfull_dir = os.path.join(VAULT, "RAW_FULL")
wiki_sources = os.path.join(VAULT, "WIKI", "sources")

# Build anchors from WIKI/sources
anchors = set()
for f in glob.glob(os.path.join(wiki_sources, "**", "*.md"), recursive=True):
    try:
        t = open(f, encoding="utf-8").read()
    except Exception:
        continue
    m = re.search(r"---\s*\n(.*?)\n---", t, re.S)
    fm = m.group(1) if m else ""
    mm = re.search(r"(?im)^\s*source_path\s*:\s*(.+?)\s*$", fm)
    if not mm:
        continue
    p = mm.group(1).strip().strip("`")
    if p.startswith("RAW_FULL/"):
        p = p[len("RAW_FULL/"):]
    elif p.startswith("RAW/"):
        p = p[len("RAW/"):]
    anchors.add(p)

rawfull = set()
for f in glob.glob(os.path.join(rawfull_dir, "**", "*.md"), recursive=True):
    rel = os.path.relpath(f, rawfull_dir).replace("\\", "/")
    rawfull.add(rel)

uncovered = rawfull - anchors
print("RAW_FULL 总数:", len(rawfull))
print("已编译覆盖:", len(rawfull & anchors))
print("未编译(目标集):", len(uncovered))

SKIP = {"ima_sync", "个人知识库", "WKB"}
def topfolders(rel, n=2):
    parts = rel.split("/")
    idx = 0
    for i, p in enumerate(parts):
        if p in SKIP:
            idx = i + 1
        else:
            break
    return "/".join(parts[idx:idx+n])

fb = collections.Counter()
sizes = []
for u in uncovered:
    fb[topfolders(u, 2)] += 1
    fp = os.path.join(rawfull_dir, u)
    try:
        sizes.append(os.path.getsize(fp))
    except Exception:
        pass

print("\n=== 未编译项 顶级文件夹分布(前2层) ===")
for k, v in fb.most_common(30):
    print(f"  {v:4d}  {k}")

print("\n=== 文件大小(byte) ===")
if sizes:
    sizes.sort()
    print("min/median/max:", sizes[0], statistics.median(sizes), sizes[-1])
    print(">100KB:", sum(1 for s in sizes if s > 100000),
          " | >500KB:", sum(1 for s in sizes if s > 500000))

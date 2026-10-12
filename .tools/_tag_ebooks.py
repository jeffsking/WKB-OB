import glob, os, re, collections

VAULT = "E:/WKB-OB"
ebook_dir = os.path.join(VAULT, "RAW_FULL", "ima_sync", "个人知识库", "WKB", "Resources", "Ebook")
extract_root = os.path.join(ebook_dir, "Ebook Extract")

def norm(s):
    s = s.lower()
    s = re.sub(r"\.pdf\.md$|\.md$|\.epub.*$|preview-|deepread|deepbook|拆解|_compress", "", s)
    s = re.sub(r"[\W_]+", " ", s).strip()
    return s

# root whole-book files
roots = {}
for f in glob.glob(os.path.join(ebook_dir, "*.md")):
    roots[os.path.basename(f)] = f

# extract subbooks (each subfolder = a book)
extracts = {}
if os.path.isdir(extract_root):
    for d in sorted(os.listdir(extract_root)):
        dp = os.path.join(extract_root, d)
        if os.path.isdir(dp):
            n = len(glob.glob(os.path.join(dp, "**", "*.md"), recursive=True))
            extracts[d] = (dp, n)

# build distinct books: key = normalized name
books = {}  # key -> dict(name, has_root, root_file, has_chapters, n_chapters, extract_dir)
def add(key, info):
    if key not in books:
        books[key] = {"aliases": [], "has_root": False, "root_file": None,
                      "has_chapters": False, "n_chapters": 0, "extract_dir": None}
    books[key].update(info)

for rf in roots:
    key = norm(rf)
    add(key, {"aliases": [rf], "has_root": True, "root_file": rf})
for d, (dp, n) in extracts.items():
    key = norm(d)
    if key in books:
        books[key]["has_chapters"] = True
        books[key]["n_chapters"] = n
        books[key]["extract_dir"] = d
        books[key]["aliases"].append("[ch]"+d)
    else:
        books[key] = {"aliases": ["[ch]"+d], "has_root": False, "root_file": None,
                      "has_chapters": True, "n_chapters": n, "extract_dir": d}

# relevance tagging
P0_kw = ["sap", "superabsorb", "高吸水", "nonwoven", "非织造", "adhes", "胶黏", "粘合",
         "chromic", "色", "变色", "mechanochrom", "photochrom", "smart textile", "智能纺织",
         "wearable", "可穿戴", "liquid crystal", "液晶", "stimuli", "刺激响应", "diffusion", "扩散",
         "dry", "干燥", "absorbent", "吸收", "hygiene", "卫生"]
P2_kw = ["cosmetic", "化妆", "skin", "皮肤", "ancient", "古代", "archae", "pigment"]

def tag(name):
    low = name.lower()
    if any(k in low for k in P2_kw):
        # but chromic/pigment are P0 colorants; guard
        if "chromic" in low or "色" in low or "pigment" in low:
            return "P0"
        return "P2"
    if any(k in low for k in P0_kw):
        return "P0"
    return "P1"

tiers = collections.defaultdict(list)
for key, b in books.items():
    display = b["aliases"][0]
    t = tag(display)
    tiers[t].append((display, b["has_root"], b["has_chapters"], b["n_chapters"]))

for t in ["P0", "P1", "P2"]:
    print(f"\n===== {t}  (书数: {len(tiers[t])}) =====")
    for display, hr, hc, nc in sorted(tiers[t]):
        flags = ("R" if hr else "-") + ("C" if hc else "-")
        print(f"  [{flags}] {nc:3d}ch  {display}")

print("\n=== 总计 ===")
print("P0:", len(tiers["P0"]), " P1:", len(tiers["P1"]), " P2:", len(tiers["P2"]),
      " 合计书:", len(books))
# chapter page estimate for P0/P1 (compile per-chapter) + index pages
ch_p0 = sum(b[3] for b in tiers["P0"] if b[2]) + sum(1 for b in tiers["P0"] if b[1] and not b[2])
ch_p1 = sum(b[3] for b in tiers["P1"] if b[2]) + sum(1 for b in tiers["P1"] if b[1] and not b[2])
print("P0 预计章节/独存整书页:", ch_p0, " + 索引页", len(tiers["P0"]))
print("P1 预计章节/独存整书页:", ch_p1, " + 索引页", len(tiers["P1"]))

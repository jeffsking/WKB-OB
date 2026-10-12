import glob, os, re, json, collections

VAULT = "E:/WKB-OB"
ebook_dir = os.path.join(VAULT, "RAW_FULL", "ima_sync", "个人知识库", "WKB", "Resources", "Ebook")
extract_root = os.path.join(ebook_dir, "Ebook Extract")

def norm(s):
    s = s.lower()
    s = re.sub(r"\.pdf\.md$|\.md$|\.epub.*$", "", s)
    s = re.sub(r"preview-|deepread|deepbook|拆解|_compress|compress", "", s)
    s = re.sub(r"[\W_]+", " ", s).strip()
    return s

def rel(p):
    return os.path.relpath(p, VAULT).replace("\\", "/")

# ---- content-file selection: keep real chapter deep-reads, drop AI meta-artifacts ----
META_TOKENS = ["摘要","summary","全书","核心观点","汇总","合成报告","全局","global",
               "readme","引用索引","index","csv","拆书文摘","概览","overview","digest",
               "概念","concepts","文摘","_all_","outline","大纲"]
def is_meta(fn):
    low = fn.lower()
    return any(tok in low for tok in META_TOKENS)

def select_content(files):
    """Return the files that should become chapter source pages (exclude meta/redundant)."""
    non_meta = [f for f in files if not is_meta(os.path.basename(f))]
    numbered = [f for f in non_meta if re.search(r'(analysis_?ch\d+|ch\d+_|_ch\d+|\bach\d+\b|深度拆解|part\d+)', os.path.basename(f).lower())]
    def has_full():
        return any(re.search(r'full_?report', os.path.basename(f).lower()) for f in non_meta)
    if numbered:
        if any(re.search(r'analysis_?ch\d+', os.path.basename(f).lower()) for f in numbered):
            return numbered  # real chapters win; drop whole-book report
        if has_full():
            return [f for f in non_meta if re.search(r'full_?report', os.path.basename(f).lower())]
        return numbered
    if has_full():
        return [f for f in non_meta if re.search(r'full_?report', os.path.basename(f).lower())]
    return non_meta  # report-only / part-only fallback

# root whole-book files
roots = {}
for f in glob.glob(os.path.join(ebook_dir, "*.md")):
    roots[os.path.basename(f)] = rel(f)

# extract subbooks
extracts = {}
if os.path.isdir(extract_root):
    for d in sorted(os.listdir(extract_root)):
        dp = os.path.join(extract_root, d)
        if os.path.isdir(dp):
            ch = sorted(glob.glob(os.path.join(dp, "**", "*.md"), recursive=True))
            extracts[d] = {"dir_rel": rel(dp), "chapters": [rel(c) for c in ch]}

# match root <-> extract by normalized name
def match_key(nk, cand_keys):
    # exact
    if nk in cand_keys:
        return nk
    # containment with length guard
    best = None
    for ck in cand_keys:
        if not ck:
            continue
        if (nk in ck or ck in nk) and len(nk) >= 8 and len(ck) >= 8:
            if best is None or len(ck) < len(best[1]):
                best = (ck, ck)
    return best[0] if best else None

root_norm = {norm(r): r for r in roots}
ext_norm = {norm(d): d for d in extracts}

# Build distinct books (merge root <-> extract by normalized name)
books = {}
def ensure(k):
    if k not in books:
        books[k] = {"root_file": None, "extract_key": None, "chapters": [], "extract_dir_rel": None}
    return books[k]

ext_norm = {norm(d): d for d in extracts}
root_norm = {norm(r): r for r in roots}

# First seed extract books (canonical = extract norm when matched)
for d, info in extracts.items():
    nk = norm(d)
    b = ensure(nk)
    b["extract_key"] = d
    b["extract_dir_rel"] = info["dir_rel"]
    b["chapters"] = info["chapters"]

# Then attach roots, merging into matching extract book when possible
for r, rrel in roots.items():
    rn = norm(r)
    m = match_key(rn, list(ext_norm.keys()))
    if m:
        canonical = m  # merge into extract book (chapters preserved)
    else:
        canonical = rn
    b = ensure(canonical)
    b["root_file"] = rrel  # set/overwrite root_file with the whole-book file path

# priority tagging
P0_kw = ["sap", "superabsorb", "高吸水", "nonwoven", "非织造", "adhes", "胶黏", "粘合",
         "chromic", "色", "变色", "mechanochrom", "photochrom", "smart textile", "智能纺织",
         "wearable", "可穿戴", "liquid crystal", "液晶", "stimuli", "刺激响应", "diffusion", "扩散",
         "dry", "干燥", "absorbent", "吸收", "hygiene", "卫生", "dye", "pigment", "染料", "颜料"]
P2_kw = ["cosmetic", "化妆", "skin", "皮肤", "ancient", "古代", "archae"]

def tag(name):
    low = name.lower()
    if any(k in low for k in P2_kw):
        if "chromic" in low or "色" in low or "pigment" in low or "dye" in low or "染料" in low or "颜料" in low:
            return "P0"
        return "P2"
    if any(k in low for k in P0_kw):
        return "P0"
    return "P1"

# P2 forced set = cosmetic/ancient only (4): 3 root + 1 extract(Cosmetic Science and Technology)
def is_p2(name):
    if not name:
        return False
    low = name.lower()
    return ("cosmetic" in low or "化妆" in low or "skin" in low or "古代" in low or "ancient" in low) \
           and not any(k in low for k in ["chromic","色","pigment","dye","染料","颜料"])

manifest = {"generated": "2026-09-29", "scope": "P0 + P2(index_only)", "books": []}
counts = collections.Counter()
for k, b in books.items():
    # display name
    disp = b["root_file"] or b["extract_key"]
    name_only = os.path.basename(disp).replace(".pdf.md","").replace(".md","")
    if is_p2(name_only) or is_p2(b.get("extract_key","")):
        pri = "P2"
    else:
        pri = tag(name_only)
    if pri not in ("P0", "P2"):
        continue  # P1 deferred
    content_files = select_content(b["chapters"]) if b["chapters"] else []
    has_chapters = len(content_files) > 0
    if pri == "P2":
        compile_as = "index_only"
    else:
        compile_as = "chapter" if has_chapters else "index_only"
    entry = {
        "name": name_only,
        "priority": pri,
        "compile_as": compile_as,
        "has_root": b["root_file"] is not None,
        "has_chapters": has_chapters,
        "n_chapters": len(content_files),
        "root_file_rel": b["root_file"],
        "extract_dir_rel": b["extract_dir_rel"],
        "chapter_source_paths": content_files,
    }
    manifest["books"].append(entry)
    counts[pri + "/" + compile_as] += 1

manifest["books"].sort(key=lambda e: (e["priority"], e["name"].lower()))
out = os.path.join(VAULT, ".tools", "ebook_compile_manifest.json")
json.dump(manifest, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print("写入:", out)
print("P0 书数:", sum(1 for e in manifest["books"] if e["priority"]=="P0"))
print("P2 书数:", sum(1 for e in manifest["books"] if e["priority"]=="P2"))
print("总计书:", len(manifest["books"]))
print("章节页(compile_as=chapter 的 n_chapters 之和):",
      sum(e["n_chapters"] for e in manifest["books"] if e["compile_as"]=="chapter"))
print("索引/独存页(compile_as=index_only 的书数):",
      sum(1 for e in manifest["books"] if e["compile_as"]=="index_only"))
print("\n分类计数:")
for k, v in sorted(counts.items()):
    print(f"  {k}: {v}")
print("\nP0 书目:")
for e in manifest["books"]:
    if e["priority"]=="P0":
        print(f"  [{e['compile_as'][:4]}] {e['n_chapters']:3d}ch  {e['name']}")
print("\nP2 书目:")
for e in manifest["books"]:
    if e["priority"]=="P2":
        print(f"  [{e['compile_as'][:4]}] {e['n_chapters']:3d}ch  {e['name']}")

"""Enumerate the P1 ebook backlog that _gen_ebook_manifest.py deferred
(`if pri not in ("P0","P2"): continue  # P1 deferred`).

Reuses exactly the same book-building / priority-tagging / chapter-selection
logic so the P1 list is consistent with the P0+P2 manifest.
"""
import glob
import os
import re
import json
import collections

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


META_TOKENS = ["摘要", "summary", "全书", "核心观点", "汇总", "合成报告", "全局", "global",
               "readme", "引用索引", "index", "csv", "拆书文摘", "概览", "overview", "digest",
               "概念", "concepts", "文摘", "_all_", "outline", "大纲"]


def is_meta(fn):
    low = fn.lower()
    return any(tok in low for tok in META_TOKENS)


def select_content(files):
    non_meta = [f for f in files if not is_meta(os.path.basename(f))]
    numbered = [f for f in non_meta if re.search(r"(analysis_?ch\d+|ch\d+_|_ch\d+|\bach\d+\b|深度拆解|part\d+)",
                                                 os.path.basename(f).lower())]
    def has_full():
        return any(re.search(r"full_?report", os.path.basename(f).lower()) for f in non_meta)
    if numbered:
        if any(re.search(r"analysis_?ch\d+", os.path.basename(f).lower()) for f in numbered):
            return numbered
        if has_full():
            return [f for f in non_meta if re.search(r"full_?report", os.path.basename(f).lower())]
        return numbered
    if has_full():
        return [f for f in non_meta if re.search(r"full_?report", os.path.basename(f).lower())]
    return non_meta


roots = {}
for f in glob.glob(os.path.join(ebook_dir, "*.md")):
    roots[os.path.basename(f)] = rel(f)

extracts = {}
if os.path.isdir(extract_root):
    for d in sorted(os.listdir(extract_root)):
        dp = os.path.join(extract_root, d)
        if os.path.isdir(dp):
            ch = sorted(glob.glob(os.path.join(dp, "**", "*.md"), recursive=True))
            extracts[d] = {"dir_rel": rel(dp), "chapters": [rel(c) for c in ch]}


def match_key(nk, cand_keys):
    if nk in cand_keys:
        return nk
    best = None
    for ck in cand_keys:
        if not ck:
            continue
        if (nk in ck or ck in nk) and len(nk) >= 8 and len(ck) >= 8:
            if best is None or len(ck) < len(best[1]):
                best = (ck, ck)
    return best[0] if best else None


books = {}
def ensure(k):
    if k not in books:
        books[k] = {"root_file": None, "extract_key": None, "chapters": [], "extract_dir_rel": None}
    return books[k]


ext_norm = {norm(d): d for d in extracts}
root_norm = {norm(r): r for r in roots}

for d, info in extracts.items():
    nk = norm(d)
    b = ensure(nk)
    b["extract_key"] = d
    b["extract_dir_rel"] = info["dir_rel"]
    b["chapters"] = info["chapters"]

for r, rrel in roots.items():
    rn = norm(r)
    m = match_key(rn, list(ext_norm.keys()))
    canonical = m if m else rn
    b = ensure(canonical)
    b["root_file"] = rrel


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


def is_p2(name):
    if not name:
        return False
    low = name.lower()
    return ("cosmetic" in low or "化妆" in low or "skin" in low or "古代" in low or "ancient" in low) \
        and not any(k in low for k in ["chromic", "色", "pigment", "dye", "染料", "颜料"])


# ---------- which source_paths are already compiled ----------
compiled = {}
for f in glob.glob(os.path.join(VAULT, "WIKI", "sources", "*.md")):
    t = open(f, encoding="utf-8", errors="ignore").read(6000)
    page = os.path.basename(f).rsplit(".md", 1)[0]
    for mm in re.finditer(r"^\s*source_paths:\s*\[(.*?)\]", t, re.M):
        for v in re.findall(r'"([^"]+)"', mm.group(1)):
            compiled[v.strip()] = page
    for mm in re.finditer(r'^\s*source_path:\s*["\']?([^"\'\n#]+)', t, re.M):
        compiled[mm.group(1).strip().strip('"').strip("'")] = page


p1 = []
counts = collections.Counter()
for k, b in books.items():
    disp = b["root_file"] or b["extract_key"]
    if not disp:
        continue
    name_only = os.path.basename(disp).replace(".pdf.md", "").replace(".md", "")
    if is_p2(name_only) or is_p2(b.get("extract_key", "")):
        pri = "P2"
    else:
        pri = tag(name_only)
    counts[pri] += 1
    if pri != "P1":
        continue
    content = select_content(b["chapters"]) if b["chapters"] else []
    root = b["root_file"]
    root_done = bool(root and (root in compiled))
    ch_done = [c for c in content if c in compiled]
    p1.append({
        "name": name_only,
        "priority": "P1",
        "root_file_rel": root,
        "extract_dir_rel": b["extract_dir_rel"],
        "n_chapters": len(content),
        "chapter_source_paths": content,
        "root_compiled": root_done,
        "chapters_compiled": len(ch_done),
    })

p1.sort(key=lambda e: (-e["n_chapters"], e["name"].lower()))

print("全部书数（含 P0/P1/P2）:", len(books))
print("优先级分布:", dict(counts))
print()
print("=" * 78)
print(f"P1 书数: {len(p1)}   总章节: {sum(e['n_chapters'] for e in p1)}")
print("=" * 78)
for e in p1:
    root_tag = "[root已编译]" if e["root_compiled"] else "[root未编译]"
    root_tag = "[无root]" if not e["root_file_rel"] else root_tag
    print(f"  {e['name'][:58]:<58} {e['chapters_compiled']:>3}/{e['n_chapters']:<3} {root_tag}")

out = os.path.join(VAULT, ".tools", "ebook_p1_manifest.json")
json.dump({"generated": "2026-09-29", "scope": "P1", "books": p1},
          open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("\n写入:", out)

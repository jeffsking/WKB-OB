import glob, os, re, collections

VAULT = "E:/WKB-OB"
ebook_dir = os.path.join(VAULT, "RAW_FULL", "ima_sync", "个人知识库", "WKB", "Resources", "Ebook")

root_files = []          # whole-book files at Ebook root
extract_subbooks = []    # subfolders under Ebook Extract (each = a book's chapters)
for f in glob.glob(os.path.join(ebook_dir, "*.md")):
    root_files.append(os.path.basename(f))
extract_root = os.path.join(ebook_dir, "Ebook Extract")
if os.path.isdir(extract_root):
    for d in sorted(os.listdir(extract_root)):
        dp = os.path.join(extract_root, d)
        if os.path.isdir(dp):
            n = len(glob.glob(os.path.join(dp, "**", "*.md"), recursive=True))
            extract_subbooks.append((d, n))

print("=== 整书文件(root) 数:", len(root_files), "===")
for r in sorted(root_files)[:70]:
    print("  ", r)

print("\n=== Ebook Extract 子书(每本书的章节集) 数:", len(extract_subbooks), "===")
total_ch = 0
for d, n in extract_subbooks:
    total_ch += n
    print(f"  {n:3d} chapters  <-  {d}")
print("  章节文件合计:", total_ch)

# Try to map root whole-book name -> extract subbook folder
def norm(s):
    s = s.lower()
    s = re.sub(r"\.pdf\.md$|\.md$|\.epub.*$", "", s)
    s = re.sub(r"[\W_]+", " ", s).strip()
    return s

root_norm = {norm(r): r for r in root_files}
matched = 0
unmatched_root = []
unmatched_extract = []
for d, n in extract_subbooks:
    dn = norm(d)
    # fuzzy: does any root_norm key share a significant token overlap?
    found = None
    for k, rv in root_norm.items():
        if dn and k and (dn in k or k in dn or (len(dn) > 8 and dn[:12] == k[:12])):
            found = rv
            break
    if found:
        matched += 1
    else:
        unmatched_extract.append(d)
for r in root_files:
    rn = norm(r)
    hit = any((rn in norm(d) or norm(d) in rn or (len(rn) > 8 and rn[:12] == norm(d)[:12])) for d, _ in extract_subbooks)
    if not hit:
        unmatched_root.append(r)

print("\n=== 映射(粗匹配) ===")
print("整书↔章节集 匹配数:", matched, "/", len(extract_subbooks))
print("仅整书无章节集(root-only):", len(unmatched_root))
for r in unmatched_root:
    print("   ROOT-ONLY:", r)
print("仅章节集无整书(extract-only):", len(unmatched_extract))
for d in unmatched_extract:
    print("   EXTRACT-ONLY:", d)

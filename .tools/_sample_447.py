import glob, os, re, collections

VAULT = "E:/WKB-OB"
ebook_dir = os.path.join(VAULT, "RAW_FULL", "ima_sync", "个人知识库", "WKB", "Resources", "Ebook")

files = glob.glob(os.path.join(ebook_dir, "**", "*.md"), recursive=True)
print("Ebook 文件夹 md 数:", len(files))

# subfolder structure
sub = collections.Counter()
for f in files:
    rel = os.path.relpath(f, ebook_dir).replace("\\", "/")
    depth1 = rel.split("/")[0] if "/" in rel else "(root)"
    sub[depth1] += 1
print("\n=== Ebook 子文件夹分布 ===")
for k, v in sub.most_common(20):
    print(f"  {v:4d}  {k}")

# size buckets
sizes = sorted((os.path.getsize(f), f) for f in files)
print("\n=== 大小分桶 ===")
print("最小5个(byte):", [s[0] for s in sizes[:5]])
print("最大5个(byte):", [s[0] for s in sizes[-5:]])

# sample: smallest, median, largest -> show first 600 chars + heading count
def sample_info(f):
    try:
        t = open(f, encoding="utf-8").read()
    except Exception:
        return "(read fail)"
    heads = len(re.findall(r"(?m)^#{1,3}\s", t))
    lines = t.count("\n")
    name = os.path.basename(f)
    return name, len(t), heads, lines

for label, item in [("最小", sizes[0]), ("中位", sizes[len(sizes)//2]), ("最大", sizes[-1])]:
    name, sz, h, ln = sample_info(item[1])
    print(f"\n--- {label} (size={sz}B, heads={h}, lines={ln}) : {name} ---")
    t = open(item[1], encoding="utf-8").read()
    print(t[:700].replace("\n", " ⏎ "))

# how many are 'thin' (< 2KB) - possible shells
thin = [f for f in files if os.path.getsize(f) < 2048]
print("\n=== <2KB 疑似空壳/薄文件数:", len(thin), "===")
for f in thin[:8]:
    print("  ", os.path.basename(f), os.path.getsize(f))

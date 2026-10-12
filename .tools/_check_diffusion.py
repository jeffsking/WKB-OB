import os, re

SRC = "E:/WKB-OB/WIKI/sources"
diff_chs = []
for fn in os.listdir(SRC):
    if not fn.endswith(".md"):
        continue
    fp = os.path.join(SRC, fn)
    try:
        with open(fp, encoding="utf-8", errors="replace") as f:
            content = f.read(3000)
        if "Mathematics of Diffusion" in content:
            m = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", content, re.M)
            t = m.group(1) if m else "?"
            diff_chs.append(t)
    except:
        pass
print("Mathematics of Diffusion pages:")
for c in sorted(diff_chs):
    print(f"  {c}")
print(f"Total: {len(diff_chs)}")

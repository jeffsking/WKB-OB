"""Build P1 compile batches.

Rules (user decision 2026-09-29):
  - P1 全量 43 本，按章编译
  - root 正文 > 800,000 字符的大部头 -> index_only（只建索引页）

Outputs .tools/compile_batches/p1_*.json and a summary.
"""
import json
import os
import re
import glob

VAULT = "E:/WKB-OB"
BIG_ROOT = 800_000


def body_len(relp):
    if not relp:
        return -1
    p = os.path.join(VAULT, relp.replace("/", os.sep))
    if not os.path.exists(p):
        return -1
    t = open(p, encoding="utf-8", errors="ignore").read()
    if t.startswith("---"):
        i = t.find("\n---", 3)
        if i > 0:
            t = t[i + 4:]
    t = re.sub(r"^\s*#.*$", "", t, flags=re.M)
    return len(t.strip())


m = json.load(open(".tools/ebook_p1_manifest.json", encoding="utf-8"))

chapter_books = []      # 逐章编译
index_books = []        # 只建索引页
for b in m["books"]:
    rl = body_len(b["root_file_rel"])
    chs = b["chapter_source_paths"]
    if rl > BIG_ROOT:
        index_books.append((b["name"], rl, "root>800k 大部头"))
    elif chs:
        chapter_books.append((b["name"], sum(body_len(c) for c in chs), chs, rl))
    else:
        index_books.append((b["name"], rl, "无分章文件"))

chapter_books.sort(key=lambda x: (-x[1], x[0].lower()))

print("=" * 80)
print(f"P1 分组：逐章编译 {len(chapter_books)} 本 / "
      f"{sum(len(c[2]) for c in chapter_books)} 章  |  索引页 {len(index_books)} 本")
print("=" * 80)
print("\n--- A 组：逐章编译 ---")
for n, tot, chs, rl in chapter_books:
    print(f"  {n[:52]:<52} {len(chs):>3} 章  正文 {tot:>8,}  (root {max(rl,0):,})")
print("\n--- B 组：只建索引页 ---")
for n, rl, why in sorted(index_books, key=lambda x: -max(x[1], 0)):
    print(f"  {n[:52]:<52} root {max(rl,0):>9,}  ({why})")

# ---------- emit batch files ----------
outdir = os.path.join(VAULT, ".tools", "compile_batches")
os.makedirs(outdir, exist_ok=True)

CHUNK = 7   # 每代理 5-7 项最稳（记忆铁律）
batches = []
for name, tot, chs, rl in chapter_books:
    for i in range(0, len(chs), CHUNK):
        part = chs[i:i + CHUNK]
        batches.append({
            "batch": f"p1_{name[:28]}_{i // CHUNK + 1:02d}",
            "book": name,
            "root_file_rel": None,
            "items": [{"src": c, "bytes": body_len(c)} for c in part],
        })

for n, rl, why in index_books:
    root = None
    for b in m["books"]:
        if b["name"] == n:
            root = b["root_file_rel"]
            break
    batches.append({
        "batch": "p1_index_" + re.sub(r"[^\w]+", "_", n)[:40],
        "book": n,
        "root_file_rel": root,
        "mode": "index_only",
        "items": [{"src": root, "bytes": max(rl, 0)}] if root else [],
    })

idx = []
for b in batches:
    fn = os.path.join(outdir, b["batch"] + ".json")
    json.dump(b, open(fn, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    idx.append({"batch": b["batch"], "book": b["book"],
                "n_items": len(b["items"]), "file": ".tools/compile_batches/" + b["batch"] + ".json"})
json.dump(idx, open(os.path.join(VAULT, ".tools", "_p1_batch_index.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

print(f"\n生成批次 {len(batches)} 个 -> .tools/compile_batches/")
print("批次索引 -> .tools/_p1_batch_index.json")

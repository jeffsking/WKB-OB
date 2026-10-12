"""Generate a context digest file per seed page, so a filler (human or agent)
can write real content WITHOUT re-searching.

Output: .tools/_seed_ctx/<safe name>.txt
Each digest: citing pages + the actual prose sentences that mention the concept.

Usage:
  python .tools/_gen_seed_digests.py --min-citations 2
"""
import glob
import os
import re
import sys
import json

VAULT = "E:/WKB-OB"
WIKI = os.path.join(VAULT, "WIKI")
OUT = os.path.join(VAULT, ".tools", "_seed_ctx")


def body_of(p):
    t = open(p, encoding="utf-8", errors="ignore").read()
    if t.startswith("---"):
        i = t.find("\n---", 3)
        if i > 0:
            t = t[i + 4:]
    return t


def prose(t):
    t = re.sub(r"`[^`]*`", "", t)
    out = []
    for chunk in re.split(r"\n{2,}", t):
        c = chunk.strip()
        if not c or c.startswith(("#", ">", "|", "---")):
            continue
        c = re.sub(r"^[-*+]\s+", "", c)
        c = re.sub(r"\[\[([^\]|#]+)(\|[^\]]+)?\]\]", r"\1", c)
        out.append(c)
    return out


def terms_for(name):
    ts = set(re.findall(r"[\u4e00-\u9fff]{2,}", name))
    ts |= set(re.findall(r"[A-Za-z][A-Za-z0-9\-']{3,}", name))
    return [t for t in ts if len(t) >= 3]


def safe(n):
    return n.translate(str.maketrans({"/": "／", "\\": "＼", ":": "：",
                                      "*": "＊", "?": "？", '"': "”",
                                      "<": "＜", ">": "＞", "|": "｜"}))


min_cit = 2
if "--min-citations" in sys.argv:
    min_cit = int(sys.argv[sys.argv.index("--min-citations") + 1])

seeds = json.load(open(os.path.join(VAULT, ".tools", "_seed_inventory.json"), encoding="utf-8"))
targets = [s for s in seeds if s["citations"] >= min_cit]
print(f"目标 seed: {len(targets)} 个 (引用 >= {min_cit})")

# preload all prose once
corpus = []
for f in glob.glob(os.path.join(WIKI, "*", "*.md")):
    corpus.append((os.path.basename(f)[:-3], prose(body_of(f))))

os.makedirs(OUT, exist_ok=True)
made = 0
for s in targets:
    name = s["name"]
    ts = [t.lower() for t in terms_for(name)]
    found = []
    for base, prs in corpus:
        if base == name:
            continue
        hits = [c for c in prs if any(t in c.lower() for t in ts) and len(c) >= 30]
        if hits:
            found.append((base, hits))
    found.sort(key=lambda r: -len(r[1]))
    fn = os.path.join(OUT, safe(name) + ".txt")
    with open(fn, "w", encoding="utf-8", newline="\n") as w:
        w.write(f"# SEED: {name}\n")
        w.write(f"# type: {s['type']} | 原引用数: {s['citations']}\n")
        w.write("# 原 Cited by 列表:\n")
        for c in s.get("cited_by", [])[:15]:
            w.write(f"#   - {c}\n")
        w.write(f"#\n# 全库正文命中 {len(found)} 页，"
                f"{sum(len(h) for _, h in found)} 句。以下为原文摘录（禁止改写为不实内容）:\n\n")
        for base, hits in found[:10]:
            w.write(f"--- [[{base}]]  ({len(hits)} 句)\n")
            for c in hits[:4]:
                w.write(f"   • {c[:500]}\n")
            w.write("\n")
    made += 1

print(f"生成 digest {made} 个 -> .tools/_seed_ctx/")

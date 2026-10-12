"""Update the Handbook of Industrial Drying book-index page:
  - regenerate the compiled-chapter list (all 53, grouped by section)
  - extend pages_linked
"""
import glob
import os
import re

VAULT = "E:/WKB-OB"
P = os.path.join(VAULT, "WIKI", "sources", "Handbook of Industrial Drying.md")

SEC = [("A 原理与计算基础", range(1, 6)),
       ("B 设备/干燥器类型", range(6, 21)),
       ("C 物料品类分论", range(21, 44)),
       ("D 系统与辅助工程", range(44, 50)),
       ("E 单元操作与经济", range(50, 54))]
KEY = {33, 34, 35, 36, 40, 41, 28, 17}

# collect actual chapter pages
ch = {}
for f in glob.glob(os.path.join(VAULT, "WIKI", "sources", "Industrial Drying Ch*.md")):
    b = os.path.basename(f)[:-3]
    m = re.match(r"Industrial Drying Ch(\d+) ", b)
    if m:
        ch[int(m.group(1))] = b
print("章节页实数:", len(ch))

t = open(P, encoding="utf-8").read()

# --- build section list ---
lines = ["\n## Compiled Chapters 已编译章节（全 53 章 · 2026-09-30 收官）\n"]
for label, rng in SEC:
    ns = [n for n in sorted(ch) if n in rng]
    if not ns:
        continue
    star = " ← 卫材关键轴" if any(n in KEY for n in ns) else ""
    lines.append(f"\n**{label}**{star}\n")
    for n in ns:
        mark = " ★" if n in KEY else ""
        lines.append(f"- Ch{n}{mark} — [[{ch[n]}]]\n")
new_section = "".join(lines) + "\n"

# replace old compiled-chapters section if present, else append
pat = re.compile(r"\n## Compiled Chapters[^\n]*[\s\S]*?(?=\n## |\Z)")
if pat.search(t):
    t = pat.sub(new_section, t, count=1)
else:
    t = t.rstrip("\n") + "\n" + new_section

# --- extend pages_linked ---
all_links = ["[[Handbook of Industrial Drying]]"] + [f"[[{ch[n]}]]" for n in sorted(ch)]
old = re.search(r"^pages_linked:\s*\[.*\]\s*$", t, re.M)
if old:
    t = t[:old.start()] + "pages_linked: " + "[" + ", ".join('"%s"' % x for x in all_links) + "]\n" + t[old.end():]
    print("pages_linked 项数:", len(all_links))

open(P, "w", encoding="utf-8", newline="\n").write(t)
print("书目索引页已更新")

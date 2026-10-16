# -*- coding: utf-8 -*-
"""孤立节点审计：断链=0 之后，图谱里还剩多少单点、都是谁。
区分：① 正文出链  ② front matter pages_linked（Obsidian 是否计为链接存疑）  ③ 入链
"""
import glob, os, re
from collections import defaultdict, Counter

VAULT = r'E:/WKB-OB'
DIRS = ['concepts', 'entities', 'sources', 'comparisons', 'MOC']

FM = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)

def read(p):
    return open(p, encoding='utf-8', errors='ignore').read()

pages = {}          # name -> (dir, body, fm)
for d in DIRS:
    for f in glob.glob(os.path.join(VAULT, 'WIKI', d, '*.md')):
        name = os.path.basename(f)[:-3]
        t = read(f)
        m = FM.match(t)
        fm = m.group(1) if m else ''
        body = t[m.end():] if m else t
        pages[name] = (d, body, fm)

valid = set(pages)

def links(text):
    return set(re.findall(r'\[\[[ \t]*([^\]\|#]+?)[ \t]*(?:\||#|\]\])', text))

# 正文出链
body_out = {n: links(pages[n][1]) for n in pages}
# front matter pages_linked 里的链接
fm_out = {n: set(re.findall(r'\[\[([^\]\|#]+?)\]\]', pages[n][2])) for n in pages}
# 入链（仅按正文）
in_deg = defaultdict(int)
for n, outs in body_out.items():
    for t in outs:
        if t in valid:
            in_deg[t] += 1

print('总页数:', len(pages))
print('  按目录:', dict(Counter(v[0] for v in pages.values())))
print()

iso_both, iso_in, iso_out = [], [], []
for n in pages:
    bo, bi = len([x for x in body_out[n] if x in valid]), in_deg[n]
    if bo == 0 and bi == 0:
        iso_both.append(n)
    elif bi == 0:
        iso_in.append(n)
    elif bo == 0:
        iso_out.append(n)

print('=== 完全孤立（正文出链0 且 入链0）: %d ===' % len(iso_both))
by_d = Counter(pages[n][0] for n in iso_both)
print('   目录分布:', dict(by_d))
print()
print('=== 孤儿（入链0，但有出链）: %d ===' % len(iso_in))
print('   目录分布:', dict(Counter(pages[n][0] for n in iso_in)))
print()
print('=== 死胡同（有入链，但正文出链0）: %d ===' % len(iso_out))
print('   目录分布:', dict(Counter(pages[n][0] for n in iso_out)))
print()

# 关键：这些"孤立"页里，有多少其实在 front matter pages_linked 里有链接？
fm_rescue = [n for n in iso_both if fm_out[n]]
print('=== 完全孤立页中，front matter `pages_linked` 里有链接的: %d / %d ==='
      % (len(fm_rescue), len(iso_both)))
print('   （若 Obsidian 不把 FM 里的 [[..]] 计入图谱 → 这些页就会显示为单点）')
print()

print('=== 完全孤立页样本（前 25）===')
for n in sorted(iso_both)[:25]:
    print('   [%-9s] %s   FM_pages_linked=%d' % (pages[n][0], n, len(fm_out[n])))
print()
print('=== 孤儿页样本（前 15）===')
for n in sorted(iso_in)[:15]:
    print('   [%-9s] %s' % (pages[n][0], n))

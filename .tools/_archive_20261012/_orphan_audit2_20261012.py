# -*- coding: utf-8 -*-
"""孤立节点审计 v2：区分「链接源是否含 index.md/MOC」两种口径。"""
import glob, os, re
from collections import defaultdict, Counter

VAULT = 'E:/WKB-OB'
DIRS = ['concepts', 'entities', 'sources', 'comparisons', 'MOC']
FM = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)

def body(p):
    t = open(p, encoding='utf-8', errors='ignore').read()
    m = FM.match(t)
    return t[m.end():] if m else t

def links(txt):
    return set(re.findall(r'\[\[[ \t]*([^\]\|#]+?)[ \t]*(?:\||#|\]\])', txt))

def norm(x):
    return x[:-3] if x.endswith('.md') else x

pages = {}
for d in DIRS:
    for f in glob.glob(os.path.join(VAULT, 'WIKI', d, '*.md')):
        pages[os.path.basename(f)[:-3]] = f
valid = set(pages)

def indeg(sources):
    ind = defaultdict(int)
    for p in sources:
        for t in links(body(p)):
            tt = norm(t)
            if tt in valid:
                ind[tt] += 1
    return ind

wiki_sources = list(pages.values())
idx_sources = wiki_sources + [os.path.join(VAULT, 'index.md')]
if os.path.exists(os.path.join(VAULT, 'wikilinks.md')):
    idx_sources.append(os.path.join(VAULT, 'wikilinks.md'))

# 正文出链
out = defaultdict(int)
for n, f in pages.items():
    for t in links(body(f)):
        tt = norm(t)
        if tt in valid and tt != n:
            out[n] += 1

for label, srcs in [('A. 仅 WIKI 内部互为链接源（不含 index.md）', wiki_sources),
                    ('B. 含 index.md / wikilinks.md 作链接源', idx_sources)]:
    ind = indeg(srcs)
    iso = [n for n in pages if ind[n] == 0 and out[n] == 0]
    orph = [n for n in pages if ind[n] == 0 and out[n] > 0]
    print('--- %s' % label)
    print('    完全孤立(入0/出0): %d   %s' % (len(iso), dict(Counter(pages[n].split(os.sep)[2] for n in iso))))
    print('    孤儿(入0/有出):    %d   %s' % (len(orph), dict(Counter(pages[n].split(os.sep)[2] for n in orph))))
    print()

# 出链缺口统计
no_out = [n for n in pages if out[n] == 0]
print('正文无出链的页共 %d：' % len(no_out), dict(Counter(pages[n].split(os.sep)[2] for n in no_out)))
print()
# 其中 front matter pages_linked 非空的
def fm_body(f):
    t = open(f, encoding='utf-8', errors='ignore').read()
    m = FM.match(t)
    return (m.group(1) if m else ''), (t[m.end():] if m else t)
rescued = 0
for n in no_out:
    fm, _ = fm_body(pages[n])
    pl = re.search(r'^\s*pages_linked:[ \t]*(.+)$', fm, re.M)
    if pl and pl.group(1).strip() not in ('[]', ''):
        rescued += 1
print('其中 front matter `pages_linked` 非空（可据此补正文链接）: %d' % rescued)

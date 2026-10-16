# -*- coding: utf-8 -*-
"""图谱节点分布 + 两种过滤口径下的孤立节点。"""
import os, re
from collections import defaultdict, Counter

VAULT = 'E:/WKB-OB'
FM = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)
LINK = re.compile(r'\[\[[ \t]*([^\]\|#]+?)[ \t]*(?:\||#|\]\])')

allmd = []
for root, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for fn in files:
        if fn.endswith('.md'):
            allmd.append(os.path.join(root, fn))

def top(p):
    r = os.path.relpath(p, VAULT)
    return r.split(os.sep)[0] if os.sep in r else '(根)'

print('=== 全库 .md 按顶层目录 ===')
for k, v in Counter(top(p) for p in allmd).most_common():
    print('  %-14s %d' % (k, v))

def read_body(p):
    t = open(p, encoding='utf-8', errors='ignore').read()
    m = FM.match(t)
    return t[m.end():] if m else t

for label, keep in [
    ('A. 过滤 `-path:RAW -path:.tools`（目录精确，RAW_FULL 保留）',
     lambda p: not (top(p) in ('RAW', '.tools'))),
    ('B. 过滤「路径含 RAW」+ `-path:.tools`（RAW_FULL 一并排除）',
     lambda p: not ('RAW' in os.path.relpath(p, VAULT).upper() or top(p) == '.tools')),
]:
    notes = [p for p in allmd if keep(p)]
    base2path = {os.path.basename(p)[:-3]: p for p in notes}
    # Obsidian 名字 = basename 去掉最后一个 .md
    edges = defaultdict(set)
    for p in notes:
        sb = os.path.basename(p)[:-3]
        for t in LINK.findall(read_body(p)):
            tb = t[:-3] if t.endswith('.md') else t
            if tb in base2path and tb != sb:
                edges[sb].add(tb)
    deg = Counter()
    for s, ts in edges.items():
        deg[s] += len(ts)
        for t in ts:
            deg[t] += 1
    iso = [b for b in base2path if deg[b] == 0]
    print()
    print('--- %s' % label)
    print('    节点 %d | 度=0 孤立节点 %d' % (len(base2path), len(iso)))
    print('    孤立分布:', dict(Counter(top(base2path[b]) for b in iso)))

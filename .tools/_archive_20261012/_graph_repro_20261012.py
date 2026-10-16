# -*- coding: utf-8 -*-
"""按用户 Obsidian 图谱配置复算：节点度 + 未解析链接（phantom）。"""
import glob, os, re
from collections import defaultdict, Counter

VAULT = 'E:/WKB-OB'
SKIP_PARTS = ('RAW' + os.sep, '.tools' + os.sep, '.obsidian' + os.sep)
FM = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)

notes = []
for root, dirs, files in os.walk(VAULT):
    rel = os.path.relpath(root, VAULT)
    if rel != '.' and any((rel + os.sep).startswith(p) for p in SKIP_PARTS):
        dirs[:] = []
        continue
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for fn in files:
        if fn.endswith('.md'):
            notes.append(os.path.join(root, fn))

# Obsidian 解析：[[Target]] 或 [[Target|alias]] 或 [[Target#head]]；basename 匹配
base2path = {}
for p in notes:
    base2path[os.path.basename(p)[:-3]] = p

def read(p):
    return open(p, encoding='utf-8', errors='ignore').read()

def body(t):
    m = FM.match(t)
    return t[m.end():] if m else t

LINK = re.compile(r'\[\[[ \t]*([^\]\|#]+?)[ \t]*(?:\||#|\]\])')

edges = defaultdict(set)      # source_base -> set(target_base resolved)
unresolved = Counter()        # target text -> 出现次数
unresolved_from = defaultdict(set)

for p in notes:
    sb = os.path.basename(p)[:-3]
    for t in LINK.findall(body(read(p))):
        tb = t[:-3] if t.endswith('.md') else t
        if tb in base2path:
            if tb != sb:
                edges[sb].add(tb)
        else:
            unresolved[t] += 1
            unresolved_from[t].add(sb)

# 度（无向）
deg = defaultdict(int)
for s, ts in edges.items():
    deg[s] += len(ts)
    for t in ts:
        deg[t] += 1

print('节点(笔记)总数:', len(notes))
iso = [b for b in base2path if deg[b] == 0]
print('图谱中度=0 的孤立笔记:', len(iso))
print('  分布:', dict(Counter(os.path.relpath(base2path[b], VAULT).split(os.sep)[0] for b in iso)))
print()
print('未解析链接(Obsidian 会画成灰色虚点/phantom)目标数:', len(unresolved))
tot = sum(unresolved.values())
print('  引用总次数:', tot)
print('  前 25 个未解析目标:')
for k, v in unresolved.most_common(25):
    print('    %2dx  %s' % (v, k))

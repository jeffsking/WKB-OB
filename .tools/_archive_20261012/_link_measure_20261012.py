# -*- coding: utf-8 -*-
"""测量：无出链 source 页 × concept/entity 标题(含别名) 的正文命中率。只读，不写盘。"""
import glob, os, re
from collections import Counter

VAULT = 'E:/WKB-OB'
FM = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)

def read(p):
    return open(p, encoding='utf-8', errors='ignore').read()

def split(p):
    t = read(p)
    m = FM.match(t)
    return (m.group(1) if m else ''), (t[m.end():] if m else t)

def getlist(fm, key):
    m = re.search(r'^%s:[ \t]*(.+)$' % key, fm, re.M)
    if not m:
        return []
    return [x.strip().strip('"').strip("'") for x in m.group(1).strip('[]').split(',') if x.strip()]

is_cjk = lambda s: any('\u4e00' <= c <= '\u9fff' for c in s)
def ok_len(s):
    s = s.strip()
    if len(s) < 2: return False
    if len(s) == 2 and not all(is_cjk(c) for c in s): return False
    if len(s) < 3 and not is_cjk(s): return False
    return True

# 目标：非 merged 的 concept/entity
targets = {}   # canonical -> set(candidates)
for d in ('concepts', 'entities'):
    for f in glob.glob(os.path.join(VAULT, 'WIKI', d, '*.md')):
        name = os.path.basename(f)[:-3]
        fm, _ = split(f)
        if re.search(r'^status:[ \t]*merged', fm, re.M):
            continue
        cands = {name}
        bare = re.sub(r'[（(][^）)]*[）)]', '', name).strip()
        if bare: cands.add(bare)
        for a in getlist(fm, 'aliases'):
            cands.add(a)
        cands = {c for c in cands if ok_len(c)}
        if cands:
            targets[name] = cands

print('目标页(非 merged concept/entity):', len(targets))
allc = [(c, n) for n, cs in targets.items() for c in cs]
print('候选串总数:', len(allc))
print()

# 待补 source 页
srcs = []
for f in glob.glob(os.path.join(VAULT, 'WIKI', 'sources', '*.md')):
    fm, body = split(f)
    if '[[' not in body:
        srcs.append((os.path.basename(f)[:-3], body))

dist = Counter(); total = 0; samples = []
for name, body in srcs:
    low = body.lower()
    hits = set()
    for c, canon in allc:
        if c.lower() in low:
            hits.add(canon)
    total += len(hits)
    dist[min(len(hits), 9)] += 1
    if len(samples) < 8:
        samples.append((name, sorted(hits)[:6]))

print('待补 source 页:', len(srcs))
print('命中分布(命中数→页数):', dict(sorted(dist.items())))
print('总命中链接数:', total)
print('平均每页: %.1f' % (total / max(1, len(srcs))))
print()
print('=== 样本 ===')
for n, h in samples:
    print('  %-46s -> %s' % (n[:46], h))

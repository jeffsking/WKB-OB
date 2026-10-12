# -*- coding: utf-8 -*-
"""只读审计 v3：电子书未编译 177 条的真实身份拆解"""
import os, re, glob, json
from collections import Counter, defaultdict

ROOT = 'E:/WKB-OB'
def norm(p): return p.replace('\\', '/')
def read(p):
    try: return open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()
    except OSError: return ''

raw = []
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW')):
    for f in fn:
        if f.endswith('.md'):
            raw.append(norm(os.path.relpath(os.path.join(dp, f), ROOT)))

sp = defaultdict(list)
for p in glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_path:\s*(.+)$', t, re.M)
    if m:
        v = norm(m.group(1).strip().strip('"'))
        if v.lower().startswith('raw/'):
            v = 'RAW/' + v.split('/', 1)[1]
        sp[v].append(os.path.basename(p))

def is_attach(r): return '/attachments/' in r or r.startswith('RAW/attachments/')
def is_book(r):
    s = r.lower()
    return ('/ebook' in s) or ('deepbook' in s) or ('book extract' in s)

un_book = [r for r in raw if is_book(r) and not sp.get(r) and not is_attach(r)]

print('=' * 78)
print(f'【电子书未编译件总数】{len(un_book)}')

# ---- 按是否位于已建索引页的书籍目录下 ----
# 建立 book-index 页 -> 其 source_path 推导的书籍目录
bidx_dirs = set()
bidx_pages = 0
for p in glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    if re.search(r'^source_type:\s*"?book-index', t, re.M):
        bidx_pages += 1
        m = re.search(r'^source_path:\s*(.+)$', t, re.M)
        if m:
            v = norm(m.group(1).strip().strip('"'))
            if v.lower().startswith('raw/'):
                v = 'RAW/' + v.split('/', 1)[1]
            # 书籍目录 = 该路径的父目录
            bidx_dirs.add('/'.join(v.split('/')[:-1]))

print(f'  已建 book-index 页:{bidx_pages}个，对应书籍目录 {len(bidx_dirs)} 个')

in_known = [r for r in un_book if '/'.join(r.split('/')[:-1]) in bidx_dirs]
orphan   = [r for r in un_book if '/'.join(r.split('/')[:-1]) not in bidx_dirs]
print(f'  ├─ 属已建索引页的书籍（增量章/补编）: {len(in_known)}')
print(f'  └─ 无索引页的孤儿书籍                    : {len(orphan)}')

# ---- 按文件名后缀类型 ----
print()
print('=' * 78)
print('【电子书未编译件 · 文件角色分类】')
def role(p):
    b = os.path.basename(p)[:-3]
    if b.endswith('_synthesis'): return 'synthesis(整书综合)'
    if b.endswith('_concepts'): return 'concepts(概念清单)'
    if b.endswith('README'):return 'README(索引件)'
    if b.endswith('_index') or b.endswith('_master_index'): return 'index(索引件)'
    if b.endswith('_report') or '_report_' in b:           return 'chapter(章节提取件)'
    return 'other(整书原件等)'
rc = Counter(role(r) for r in un_book)
for k, v in rc.most_common():
    print(f'  {k:<24}{v:>6}')

# ---- 孤儿书籍按书名聚合 ----
print()
print('=' * 78)
print('【孤儿书籍聚合（前 20 本，按未编译章数）】')
bks = defaultdict(list)
for r in orphan:
    m = re.search(r'/Ebook Extract/([^/]+)/', r) or re.search(r'/Ebook/([^/]+?)(?:\.md)?$', r)
    name = m.group(1) if m else '(根级散件)'
    bks[name].append(r)
for name, lst in sorted(bks.items(), key=lambda x: -len(x[1]))[:20]:
    print(f'  {len(lst):>4} 章  {name}')

# ---- 已建索引页书籍的增量（说明是正常增量） ----
print()
print('=' * 78)
print('【属已索引书籍的未编译件（前 15）——正常增量】')
bks2 = defaultdict(int)
for r in in_known:
    bks2['/'.join(r.split('/')[:-1])] += 1
for d, n in sorted(bks2.items(), key=lambda x: -x[1])[:15]:
    print(f'  {n:>4} 章  {d.split("/Ebook Extract/")[-1]}')

# ---- 整书原件（>500KB）是否被误当单页 ----
print()
print('=' * 78)
print('【电子书未编译件 · 大文件检查（整书原件应轻量页，非巨页）】')
big = []
for r in un_book:
    fr = os.path.join(ROOT, 'RAW_FULL', r[len('RAW'):]) if False else os.path.join(ROOT, r.replace('RAW/', 'RAW_FULL/', 1))
    try: sz = os.path.getsize(fr)
    except OSError: sz = 0
    if sz > 500_000: big.append((sz, r))
print(f'  >500KB 的未编译电子书件: {len(big)} 个')
for sz, r in sorted(big, reverse=True)[:10]:
    print(f'    {sz/1024/1024:>6.2f} MB  {r.split("/")[-1][:70]}')
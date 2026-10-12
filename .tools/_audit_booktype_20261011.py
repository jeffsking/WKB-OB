# -*- coding: utf-8 -*-
"""只读审计：未编译条目的 media_type 分布，重点核对「电子书是否占未入库大部分」"""
import os, re, glob
from collections import Counter, defaultdict

ROOT = 'E:/WKB-OB'

def norm(p): return p.replace('\\', '/')
def read(p):
    try: return open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()
    except OSError: return ''

# ---------- 1. 全量 RAW md ----------
raw = []
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW')):
    for f in fn:
        if f.endswith('.md'):
            raw.append(norm(os.path.relpath(os.path.join(dp, f), ROOT)))
rawset = set(raw)

# ---------- 2. source 页锚点 ----------
sp = defaultdict(list)
for p in glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_path:\s*(.+)$', t, m := None) if False else re.search(r'^source_path:\s*(.+)$', t, re.M)
    if m:
        v = norm(m.group(1).strip().strip('"'))
        if v.lower().startswith('raw/'):
            v = 'RAW/' + v.split('/', 1)[1]
        sp[v].append(os.path.basename(p))

# ---------- 3. media_type / media_id 抽取 ----------
MT = re.compile(r'^media_type:\s*["\']?([A-Za-z0-9_]+)["\']?\s*$', re.M)
MID = re.compile(r'media_id["\']?\s*[:=]\s*["\']?([A-Za-z0-9_+/=-]+)')

info = {}
for r in raw:
    t = read(r)
    m = MT.search(t)
    mt = m.group(1) if m else '(none)'
    mm = MID.search(t)
    info[r] = (mt, mm.group(1) if mm else None)

# RAW_FULL 侧 extract_status
FULLSTATUS = {}
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW_FULL')):
    for f in fn:
        if not f.endswith('.md'): continue
        p = norm(os.path.relpath(os.path.join(dp, f), ROOT))
        t = open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()
        m = re.search(r'extract_status:\s*"?(ok|empty|original-only)"?', t)
        FULLSTATUS[p] = m.group(1) if m else '(none)'

def full_of(r):
    return 'RAW_FULL' + r[len('RAW'):]

def is_attach(r):
    return '/attachments/' in r or r.startswith('RAW/attachments/')

# ---------- 4. 分类 ----------
compiled, uncompiled_att, uncompiled_other = [], [], []
for r in raw:
    (compiled if sp.get(r) else (uncompiled_att if is_attach(r) else uncompiled_other)).append(r)

print('=' * 74)
print('【总览】')
print('  RAW md 总数      :', len(raw))
print('  已建 source 页   :', len(compiled))
print('  未编译·attachments:', len(uncompiled_att))
print('  未编译·其他       :', len(uncompiled_other))

# ---------- 5. media_type × 编译状态 交叉表 ----------
print()
print('=' * 74)
print('【交叉表】media_type × 编译状态（排除 attachments 后）')
rows = defaultdict(lambda: [0, 0])   # mt -> [compiled, uncompiled]
for r in compiled:
    if is_attach(r): continue
    rows[info[r][0]][0] += 1
for r in uncompiled_other:
    rows[info[r][0]][1] += 1

print(f"{'media_type':<18}{'已编译':>8}{'未编译':>8}{'合计':>8}{'未编译率':>10}")
print('-' * 74)
for mt, (c, u) in sorted(rows.items(), key=lambda x: -(x[1][0] + x[1][1])):
    tot = c + u
    print(f"{mt:<18}{c:>8}{u:>8}{tot:>8}{u/tot*100:>9.1f}%")
print('-' * 74)
tc = sum(v[0] for v in rows.values()); tu = sum(v[1] for v in rows.values())
print(f"{'TOTAL':<18}{tc:>8}{tu:>8}{tc+tu:>8}{tu/(tc+tu)*100:>9.1f}%")

# ---------- 6. 电子书口径 ----------
BOOK = {'book', 'book-index'}
bk_c = sum(v[0] for k, v in rows.items() if k in BOOK)
bk_u = sum(v[1] for k, v in rows.items() if k in BOOK)
print()
print('=' * 74)
print('【电子书口径核对】')
print(f"  book已编译   : {bk_c}")
print(f"  book 未编译  : {bk_u}← 占未编译 {bk_u/tu*100:.1f}%")
print(f"  非书 未编译  : {tu - bk_u}")

# ---------- 7. 未编译条目的回填状态（电子书是否有正文） ----------
print()
print('=' * 74)
print('【未编译条目中，RAW_FULL 侧有正文的分布】')
st = Counter()
for r in uncompiled_other:
    st[FULLSTATUS.get(full_of(r), 'NO_MIRROR')] += 1
for k, v in st.most_common():
    print(f'  {k:<18}{v:>6}')

print()
print('  按 media_type × 回填状态（未编译子集）:')
grid = defaultdict(Counter)
for r in uncompiled_other:
    grid[info[r][0]][FULLSTATUS.get(full_of(r), 'NO_MIRROR')] += 1
hdr = ['ok', 'empty', 'original-only', '(none)', 'NO_MIRROR']
print(f"{'media_type':<18}" + ''.join(f'{h:>14}' for h in hdr))
for mt, c in sorted(grid.items(), key=lambda x: -sum(x[1].values())):
    print(f"{mt:<18}" + ''.join(f'{c.get(h,0):>14}' for h in hdr))

# ---------- 8. 电子书未编译样本 ----------
print()
print('=' * 74)
print('【book / book-index 未编译样本（前 15，按路径）】')
n = 0
for r in sorted(uncompiled_other):
    if info[r][0] in BOOK:
        print(f'  [{info[r][0]:<10}] {r}   RAW_FULL={FULLSTATUS.get(full_of(r), "NO_MIRROR")}')
        n += 1
        if n >= 15: break

# ---------- 9. WIKI 侧书籍聚合页规模 ----------
print()
print('=' * 74)
print('【WIKI侧书籍相关页统计】')
for pat, label in [('WIKI/concepts/book-*.md', 'concepts/book-*'),
                   ('WIKI/entities/book-*.md', 'entities/book-*'),
                   ('WIKI/sources/book-*.md', 'sources/book-*')]:
    print(f'  {label:<24}{len(glob.glob(os.path.join(ROOT, pat))):>6}')

# ---------- 10. 日志中电子书相关决策 ----------
print()
print('=' * 74)
print('【log.md 中电子书/book 决策记录】')
lg = read('log.md').splitlines()
hits = [(i + 1, l.strip()) for i, l in enumerate(lg)
        if re.search(r'电子书|book-index|\bbook\b', l, re.I)]
for i, l in hits[-25:]:
    print(f'  L{i}: {l[:160]}')
print(f'  （共 {len(hits)} 条命中，显示末 25 条）')
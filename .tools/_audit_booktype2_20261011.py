# -*- coding: utf-8 -*-
"""只读审计 v2：改用路径口径判定电子书（RAW 侧无 media_type 字段）"""
import os, re, glob
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
rawset = set(raw)

sp = defaultdict(list)
for p in glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_path:\s*(.+)$', t, re.M)
    if m:
        v = norm(m.group(1).strip().strip('"'))
        if v.lower().startswith('raw/'):
            v = 'RAW/' + v.split('/', 1)[1]
        sp[v].append(os.path.basename(p))

FULLSTATUS = {}
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW_FULL')):
    for f in fn:
        if not f.endswith('.md'): continue
        p = norm(os.path.relpath(os.path.join(dp, f), ROOT))
        t = open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()
        m = re.search(r'extract_status:\s*"?(ok|empty|original-only)"?', t)
        FULLSTATUS[p] = m.group(1) if m else '(none)'

def full_of(r): return 'RAW_FULL' + r[len('RAW'):]
def is_attach(r): return '/attachments/' in r or r.startswith('RAW/attachments/')

# ---- 电子书判定：路径含 Ebook / DeepBook / Book Extract ----
def is_book(r):
    s = r.lower()
    return ('/ebook' in s) or ('deepbook' in s) or ('book extract' in s)

# ---- 章节级 vs 书级 ----
def book_level(r):
    """DeepBook / Book Extract 下的 md = 章节提取件；Ebook 直属 = 书级"""
    s = r.replace('\\', '/')
    if '/Ebook Extract/' in s: return 'chapter(章节提取件)'
    if '/Ebook/' in s:        return 'book(书级)'
    return None

compiled   = [r for r in raw if sp.get(r)]
un_att     = [r for r in raw if not sp.get(r) and is_attach(r)]
un_other   = [r for r in raw if not sp.get(r) and not is_attach(r)]

print('=' * 78)
print('【总览】')
print('  RAW md 总数        :', len(raw))
print('  已建 source 页     :', len(compiled))
print('  未编译·attachments :', len(un_att), '(设计不编译)')
print('  未编译·其他        :', len(un_other))

# ---- 交叉表：电子书 vs 非书 ----
print()
print('=' * 78)
print('【交叉表】电子书 × 编译状态')
print(f"{'类别':<26}{'已编译':>9}{'未编译':>9}{'合计':>9}{'未编译率':>11}")
print('-' * 78)
book_all  = [r for r in raw     if is_book(r)]
nonbook   = [r for r in raw     if not is_book(r)]
bc = sum(1 for r in book_all if sp.get(r)); bu = len(book_all) - bc
nc = sum(1 for r in nonbook  if sp.get(r)); nu = len(nonbook) - nc
print(f"{'电子书 (Ebook/DeepBook)':<24}{bc:>9}{bu:>9}{len(book_all):>9}{bu/len(book_all)*100:>10.1f}%")
print(f"{'非电子书':<26}{nc:>9}{nu:>9}{len(nonbook):>9}{nu/len(nonbook)*100:>10.1f}%")
print('-' * 78)
tc, tu = bc + nc, bu + nu
print(f"{'TOTAL':<26}{tc:>9}{tu:>9}{tc+tu:>9}{tu/(tc+tu)*100:>10.1f}%")

# ---- 关键问题：未编译 518 条里电子书占多少 ----print()
print('=' * 78)
print('【核心问题的直接回答】')
print(f'  未编译·其他（真实欠账候选）: {len(un_other)} 条')
book_un = [r for r in un_other if is_book(r)]
print(f'    其中电子书            : {len(book_un)} 条  ← 占 {len(book_un)/len(un_other)*100:.1f}%')
print(f'    其中非书类            : {len(un_other)-len(book_un)} 条  ← 占 {(len(un_other)-len(book_un))/len(un_other)*100:.1f}%')
print()
print(f'  全部未编译（含 attachments {len(un_att)}）: {len(un_att)+len(un_other)} 条')
allbook_un = [r for r in raw if is_book(r) and not sp.get(r)]
print(f'    其中电子书            : {len(allbook_un)} 条  ← 占 {len(allbook_un)/(len(un_att)+len(un_other))*100:.1f}%')

# ---- 电子书细分：章节级 vs 书级 ----
print()
print('=' * 78)
print('【电子书细分】书级 vs 章节提取件')
lv = defaultdict(lambda: [0, 0])
for r in book_all:
    L = book_level(r) or '(其他路径)'
    lv[L][0 if sp.get(r) else 1] += 1
print(f"{'层级':<26}{'已编译':>9}{'未编译':>9}{'合计':>9}")
for L, (c, u) in sorted(lv.items()):
    print(f'{L:<26}{c:>9}{u:>9}{c+u:>9}')

# ---- 电子书未编译件：有无正文 ----
print()
print('=' * 78)
print('【电子书未编译件的 RAW_FULL 回填状态】')
st = Counter(FULLSTATUS.get(full_of(r), 'NO_MIRROR') for r in book_un)
for k, v in st.most_common():
    print(f'  {k:<18}{v:>6}')
ok_books = [r for r in book_un if FULLSTATUS.get(full_of(r)) == 'ok']
print(f'  →其中有完整正文的{len(ok_books)} 条，是真欠账')

# ---- 非书未编译件：有无正文 ----
print()
print('=' * 78)
print('【非书未编译件的 RAW_FULL 回填状态】')
non_un = [r for r in un_other if not is_book(r)]
st2 = Counter(FULLSTATUS.get(full_of(r), 'NO_MIRROR') for r in non_un)
for k, v in st2.most_common():
    print(f'  {k:<18}{v:>6}')

# ---- 修正后的真实欠账（剔除电子书） ----
print()
print('=' * 78)
print('【修正后的欠账口径】')
real_all= len(un_other)
real_nb = len(non_un)
print(f'  口径 A：全部未编译（不含 attachments）      : {real_all}')
print(f'  口径 B：剔除电子书（电子书按决策暂不编译）: {real_nb}')
print(f'  → 两个口径差 {real_all-real_nb} 条，即电子书欠账')

# ---- 书籍聚合页规模 ----
print()
print('=' * 78)
print('【WIKI 侧书籍聚合页】')
for d in ['concepts', 'entities', 'sources']:
    fs = glob.glob(os.path.join(ROOT, 'WIKI', d, '*.md'))
    bk = [f for f in fs if is_book(norm(os.path.relpath(f, ROOT)))]
    print(f'  WIKI/{d:<10} 总 {len(fs):>5}页，其中书籍相关 {len(bk):>4} 页')

# ---- 电子书未编译样本 ----
print()
print('=' * 78)
print('【电子书未编译样本（前 12）】')
for r in sorted(book_un)[:12]:
    print(f'  [{FULLSTATUS.get(full_of(r), "NO_MIRROR"):>13}] {r}')

# ---- 非书未编译 TOP 目录 ----
print()
print('=' * 78)
print('【非书未编译件所在目录 TOP 15】')
dd = Counter('/'.join(r.split('/')[:-1]) for r in non_un)
for d, n in dd.most_common(15):
    print(f'  {n:>4}  {d}')
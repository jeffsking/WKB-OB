import os, re, glob
from collections import Counter

ROOT = 'E:/WKB-OB'
def norm(p): return p.replace('\\', '/')
def readrel(p):
    try: return open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()
    except OSError: return ''

raw = set()
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW', 'ima_sync')):
    for f in fn:
        if f.endswith('.md'):
            raw.add(norm(os.path.relpath(os.path.join(dp, f), ROOT)))

sp = {}
for p in glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_path:\s*(.+)$', t, re.M)
    if m:
        v = norm(m.group(1).strip().strip('"'))
        if v.startswith('raw/'):
            v = 'RAW/' + v.split('/', 1)[1]
        sp.setdefault(v, []).append(os.path.basename(p))

nonatt = {x for x in raw if '/attachments/' not in x}
missing = sorted(nonatt - set(sp))
UNSUP = '暂不支持自动同步内容'
LINK = re.compile(r'!?\[\[([^\]]+)\]\]')
MD_RE = re.compile(r'media_id["\']?\s*[:=]\s*["\']?([A-Za-z0-9_+/=-]+)')
EXTRACT_OK = re.compile(r'extract_status:\s*"?ok"?')

fulltext = {}
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW_FULL')):
    for f in fn:
        if f.endswith('.md'):
            p = norm(os.path.relpath(os.path.join(dp, f), ROOT))
            t = open(os.path.join(dp, f), encoding='utf-8', errors='replace').read()
            mid = MD_RE.search(t)
            if mid:
                fulltext.setdefault(mid.group(1), (p, t))

shells = [m for m in missing if UNSUP not in readrel(m) and len(readrel(m)) < 600]

cat = Counter()
detail = {k: [] for k in ['A', 'B', 'C', 'D']}
for m in shells:
    t = readrel(m)
    mid = MD_RE.search(t)
    mid = mid.group(1) if mid else None
    ft = fulltext.get(mid) if mid else None
    if ft:
        fpath, fbody = ft
        if EXTRACT_OK.search(fbody) and len(fbody) >= 600:
            cat['A_RAW_FULL已回填正文·可编译'] += 1; detail['A'].append((m, fpath, len(fbody)))
        else:
            cat['B_RAW_FULL有文件但内容不足'] += 1; detail['B'].append((m, fpath, len(fbody)))
    else:
        cat['D_RAW_FULL无镜像·真未回填'] += 1; detail['D'].append((m, None, 0))

print('=' * 76)
print('342 条「空壳」的真实分类（王总质疑后复核）')
print('=' * 76)
for k, v in sorted(cat.items()):
    print('  %-34s %d' % (k, v))
print()
print('  >> A + B = 已回填过内容 =', cat['A_RAW_FULL已回填正文·可编译'] + cat['B_RAW_FULL有文件但内容不足'])
print('  >> D = 确实没回填 =', cat['D_RAW_FULL无镜像·真未回填'])

print()
print('=' * 76)
print('D 类（真未回填）按 media_type 分布')
print('=' * 76)
c = Counter()
for m, _, _ in detail['D']:
    t = readrel(m)
    mid = MD_RE.search(t)
    c[mid.group(1).split('_')[0] if mid else '?'] += 1
for k, v in c.most_common():
    print('  %-18s %d' % (k, v))

print()
print('=' * 76)
print('D 类全部明细（真·未回填，需要处理）')
print('=' * 76)
for m, _, _ in sorted(detail['D']):
    print('  ', m)

print()
print('=' * 76)
print('B 类明细（RAW_FULL 有文件但内容不足 600 字节）')
print('=' * 76)
for m, fp, n in sorted(detail['B'])[:40]:
    print('   %-6d %s' % (n, m))
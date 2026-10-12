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

sp = set()
for p in glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_path:\s*(.+)$', t, re.M)
    if m:
        v = norm(m.group(1).strip().strip('"'))
        if v.startswith('raw/'):
            v = 'RAW/' + v.split('/', 1)[1]
        sp.add(v)

nonatt = {x for x in raw if '/attachments/' not in x}
missing = sorted(nonatt - sp)

UNSUP = '暂不支持自动同步内容'
LINK = re.compile(r'\[\[([^\]]+)\]\]')
MD_RE = re.compile(r'media_id["\']?\s*[:=]\s*["\']?([A-Za-z0-9_+/=-]+)')

shells = []
for m in missing:
    t = readrel(m)
    if UNSUP in t:
        continue
    if len(t) >= 600:
        continue
    shells.append(m)

print('空壳候选数（未编译 + 无unsup 标记 + <600 字节）:', len(shells))
print()
print('=' * 72)
print('空壳内部结构统计')
print('=' * 72)
stat = Counter()
withlink = []
for m in shells:
    t = readrel(m)
    links = LINK.findall(t)
    has_mid = bool(MD_RE.search(t))
    has_unsup = UNSUP in t
    nlink = len(links)
    if nlink:
        withlink.append((m, links))
    stat['含 wikilink' if nlink else '无 wikilink'] += 1
    stat['含 media_id' if has_mid else '无 media_id'] += 1
    stat['含 unsup 提示' if has_unsup else '无 unsup 提示'] += 1
for k, v in sorted(stat.items()):
    print('  %-18s %d' % (k, v))

print()
print('含 wikilink 的空壳数:', len(withlink))
print()
print('=' * 72)
print('空壳样本（完整原文，逐字显示）')
print('=' * 72)
for m in shells[:6]:
    t = readrel(m)
    print()
    print('--- FILE:', m, ' (%d 字节) ---' % len(t))
    print(t[:900])
    print('--- END ---')
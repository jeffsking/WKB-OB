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
rawset = raw

sp = {}
for p in glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_path:\s*(.+)$', t, re.M)
    if m:
        v = norm(m.group(1).strip().strip('"'))
        if v.startswith('raw/'):
            v = 'RAW/' + v.split('/', 1)[1]
        sp.setdefault(v, []).append(os.path.basename(p))

nonatt = {x for x in rawset if '/attachments/' not in x}
missing = sorted(nonatt - set(sp))
UNSUP = '暂不支持自动同步内容'
LINK = re.compile(r'\[\[([^\]]+)\]\]')

shells = [m for m in missing if UNSUP not in readrel(m) and len(readrel(m)) < 600]

# RAW_FULL 侧同 media_id 是否有正文
full_by_mid = {}
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW_FULL')):
    for f in fn:
        if f.endswith('.md'):
            p = os.path.join(dp, f)
            t = open(p, encoding='utf-8', errors='replace').read()
            m = re.search(r'media_id["\']?\s*[:=]\s*["\']?([A-Za-z0-9_+/=-]+)', t)
            if m:
                full_by_mid.setdefault(m.group(1), []).append(norm(os.path.relpath(p, ROOT)))

MD_RE = re.compile(r'media_id["\']?\s*[:=]\s*["\']?([A-Za-z0-9_+/=-]+)')

print('=' * 74)
print('空壳 342 条的链接性质判定')
print('=' * 74)
selflink = 0
otherlink = 0
resolved_to_source = 0
resolved_to_rawfile = 0
unresolved = 0
samples_unresolved = []
samples_other = []

for m in shells:
    t = readrel(m)
    links = LINK.findall(t)
    mid = MD_RE.search(t)
    mid = mid.group(1) if mid else None
    stem = os.path.splitext(os.path.basename(m))[0]
    for L in links:
        if L.strip() == stem:
            selflink += 1
        else:
            otherlink += 1
            if len(samples_other) < 10:
                samples_other.append((m, L))
    # 是否有正文镜像
    if mid and mid in full_by_mid:
        resolved_to_rawfile += 1
    else:
        # 链接是否能解析到某个 RAW 文件（去掉 .md 后缀）
        cand = [x for x in rawset if os.path.splitext(os.path.basename(x))[0] == stem and x != m]
        if cand:
            resolved_to_rawfile += 1
        else:
            unresolved += 1
            if len(samples_unresolved) < 10:
                samples_unresolved.append(m)

print('链接总数中，指向自身标题（自引用）:', selflink)
print('链接总数中，指向其他页面:', otherlink)
print()
print('空壳中 RAW_FULL 侧已有正文镜像的:', resolved_to_rawfile)
print('空壳中无正文镜像、链接也无法解析的:', unresolved)

print()
print('=' * 74)
print('关键验证：RAW_FULL 侧这些media_id 有没有正文？')
print('=' * 74)
cnt = Counter()
for m in shells:
    t = readrel(m)
    mid = MD_RE.search(t)
    prefix = mid.group(1).split('_')[0] if mid else '?'
    has = bool(mid and mid.group(1) in full_by_mid)
    cnt[(prefix, 'RAW_FULL有正文' if has else 'RAW_FULL无')] += 1
for (p, s), v in sorted(cnt.items(), key=lambda x: -x[1]):
    print('  %-18s %-18s %d' % (p, s, v))

print()
print('=' * 74)
print('非自引用链接样本（若为空则证明全是自引用）')
print('=' * 74)
if samples_other:
    for m, L in samples_other:
        print('  %s' % m)
        print('      -> [[%s]]' % L)
else:
    print('  （无）全部 339 条链接均为自引用')

print()
print('=' * 74)
print('无法解析链接的空壳样本')
print('=' * 74)
for x in samples_unresolved:
    print('  ', x)
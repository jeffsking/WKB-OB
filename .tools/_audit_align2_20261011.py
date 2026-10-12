import os, re, glob
from collections import Counter

ROOT = 'E:/WKB-OB'
RAW = os.path.join(ROOT, 'RAW', 'ima_sync')
FULLROOT = os.path.join(ROOT, 'RAW_FULL')

def norm(p): return p.replace('\\', '/')

raw = []
for dp, dn, fn in os.walk(RAW):
    for f in fn:
        if f.endswith('.md'):
            raw.append(norm(os.path.relpath(os.path.join(dp, f), ROOT)))
rawset = set(raw)

sp = set()
for p in glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_path:\s*(.+)$', t, re.M)
    if m:
        v = m.group(1).strip().strip('"')
        if v.startswith('raw/'):
            v = 'RAW/' + v.split('/', 1)[1]
        sp.add(norm(v))

missing = sorted(rawset - sp)

def read(p):
    try:
        return open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()
    except OSError:
        return ''

UNSUP = '暂不支持自动同步内容'
MD_RE = re.compile(r'media_id["\']?\s*[:=]\s*["\']?([A-Za-z0-9_+/=-]+)')

buckets = Counter()
detail = {k: [] for k in ['att_subdir', 'root_stub', 'root_body_nofm', 'root_real']}
for m in missing:
    parts = m.split('/')
    if '/attachments/' in m:
        buckets['1_attachments 子目录（设计如此不编译）'] += 1
        continue
    # WKB 根层级 或 一级目录下
    depth = len([x for x in parts[3:-1] if x])
    t = read(m)
    has_mid = bool(MD_RE.search(t))
    has_unsup = UNSUP in t
    extract = re.search(r'extract_status:\s*"?(ok|empty|original-only)"?', t)
    has_body = len(t) >= 600 and not has_unsup
    if has_unsup:
        buckets['2_根层占位符-暂不支持'] += 1
        detail['root_stub'].append(m)
    elif not has_mid:
        buckets['3_根层无 media_id 的派生件'] += 1
        detail['root_body_nofm'].append(m)
    elif has_body or extract:
        buckets['4_根层有正文但未编译'] += 1
        detail['root_real'].append(m)
    else:
        buckets['5_根层空壳（无正文）'] += 1
        detail['root_stub'].append(m)

print('=== 902 缺失 source 页的文件分层 ===')
for k, v in sorted(buckets.items()):
    print('  %-42s %d' % (k, v))
print()
for k in ['root_real', 'root_stub', 'root_body_nofm']:
    lst = detail[k]
    print('--- %s (%d) 前 25 ---' % (k, len(lst)))
    for x in lst[:25]:
        print('   ', x)
    print()
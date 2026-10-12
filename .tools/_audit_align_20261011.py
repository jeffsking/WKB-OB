import os, re, glob, json
from collections import Counter

ROOT = 'E:/WKB-OB'
RAW = os.path.join(ROOT, 'RAW', 'ima_sync')
FULL = os.path.join(ROOT, 'RAW_FULL', 'ima_sync')

def norm(p):
    return p.replace('\\', '/')

# 1) RAW 侧 md 全量
raw = []
for dp, dn, fn in os.walk(RAW):
    for f in fn:
        if f.endswith('.md'):
            raw.append(norm(os.path.relpath(os.path.join(dp, f), ROOT)))
print('RAW/ima_sync md total:', len(raw))

full = set()
for dp, dn, fn in os.walk(FULL):
    for f in fn:
        if f.endswith('.md'):
            full.add(norm(os.path.relpath(os.path.join(dp, f), ROOT)))
print('RAW_FULL/ima_sync md total:', len(full))

# 2) source 页 source_path 集合
sp = set()
no_sp = []
for p in glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_path:\s*(.+)$', t, re.M)
    if m:
        v = m.group(1).strip().strip('"')
        if v.startswith('raw/'):
            v = 'RAW/' + v.split('/', 1)[1]
        sp.add(norm(v))
    else:
        no_sp.append(os.path.basename(p))
print('source pages with source_path:', len(sp), '| without:', len(no_sp))
if no_sp:
    print('  no-source_path sample:', no_sp[:10])

rawset = set(raw)
hit = sp & rawset
dangling = sp - rawset
missing = rawset - sp

print()
print('=== A. source anchors hitting real RAW files:', len(hit))
print('=== B. source anchors dangling (point to non-existent RAW):', len(dangling))
for x in sorted(dangling)[:15]:
    print('     DANGLING:', x)
print('=== C. RAW files with NO source page:', len(missing))

# C 分组
grp = Counter()
for m in missing:
    parts = m.split('/')
    if '/attachments/' in m:
        grp['<attachments 子目录>'] += 1
    else:
        grp['/'.join(parts[2:4])] += 1
print()
print('--- C 分组 (top 30) ---')
for k, v in grp.most_common(30):
    print('   %-60s %d' % (k, v))

# D. missing 中有多少在 RAW_FULL 有正文（即已回填但未编译）
full_rel = set(x.replace('RAW_FULL/', 'RAW/', 1) for x in full)
missing_with_body = sorted(set(missing) & full_rel)
print()
print('=== D. missing 中 RAW_FULL 已有正文的（真·可编译欠账）:', len(missing_with_body))
grp2 = Counter()
for m in missing_with_body:
    parts = m.split('/')
    grp2['/'.join(parts[2:4])] += 1
for k, v in grp2.most_common(20):
    print('   %-50s %d' % (k, v))
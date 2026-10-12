import os, re, glob, json
from collections import Counter

ROOT = 'E:/WKB-OB'
def norm(p): return p.replace('\\', '/')

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
att = {x for x in raw if '/attachments/' in x}
hit = sp & raw
missing = nonatt - sp

print('RAW md 总数                    :', len(raw))
print('  attachments/ 子目录（不编译）:', len(att))
print('  非attachments 知识条目       :', len(nonatt))
print('source 锚点命中 RAW            :', len(hit))
print('  其中落在非attachments         :', len(hit & nonatt))
print('  其中落在 attachments          :', len(hit & att), '(说明：有 source 页把附件当独立资料编译)')
print()
print('非attachments 未编译            :', len(missing))
print('  >> 覆盖率（排除 attachments）  : %.1f%%' % (100.0 * len(hit & nonatt) / len(nonatt)))

bl = set(norm(x) for x in json.load(open(os.path.join(ROOT, '.tools', '_compile_backlog.json'), encoding='utf-8')))
print()
print('--- backlog.json (840) 与本次集合对照 ---')
print('  backlog 条数                :', len(bl))
print('  backlog ∩ 本次未编译        :', len(bl & missing))
print('  backlog 有但已被编译(陈旧)  :', len(bl - missing))
print('  本次未编译但 backlog 未收录  :', len(missing - bl))
print()
print('  backlog 中陈旧条目按目录分布:')
c = Counter()
for x in sorted(bl - missing)[:200]:
    c['/'.join(x.split('/')[2:4])] += 1
for k, v in c.most_common(12):
    print('     %-45s %d' % (k, v))
print()
print('  陈旧样例（backlog 有、实际已有 source 页）:')
for x in sorted(bl - missing)[:8]:
    print('     ', x)
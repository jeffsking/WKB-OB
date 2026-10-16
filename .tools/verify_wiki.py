import re, os, glob

os.chdir(r'E:\WKB-OB')

files = {os.path.splitext(os.path.basename(p))[0] for p in glob.glob('WIKI/**/*.md', recursive=True)}
files |= {'index', 'log'}

# ---- 1. 断链检查（剔除行内代码）----
bad = {}
for p in glob.glob('WIKI/**/*.md', recursive=True) + ['index.md', 'log.md']:
    t = open(p, encoding='utf-8').read()
    t = re.sub(r'`[^`]*`', '', t)
    for m in set(re.findall(r'\[\[([^\]|#]+)', t)):
        n = m.strip()
        if n not in files:
            bad.setdefault(n, []).append(os.path.basename(p))
print('=== 断链检查 ===')
for k, v in sorted(bad.items()):
    print('  BROKEN:', k, '<-', ', '.join(sorted(set(v))))
print('  断链数:', len(bad))

# ---- 2. front matter 必填字段检查 ----
REQ = {
    'source':     ['type', 'title', 'source_type', 'source_path', 'date_published',
                   'date_processed', 'credibility', 'knowledge_update_status', 'key_claims', 'pages_linked'],
    'concept':    ['type', 'title', 'domain', 'status', 'updated', 'tags'],
    'entity':     ['type', 'title', 'category', 'relationship', 'updated', 'tags'],
    'comparison': ['type', 'title', 'subjects', 'dimension', 'updated', 'tags'],
}
# MOC 是导航层，不参与 status 治理（AGENTS §1）→ 豁免必填字段校验
MOC_TYPES = {'moc'}
FM = re.compile(r'^---\n(.*?)\n---\n', re.S)
ok, fail = 0, []
for p in sorted(glob.glob('WIKI/**/*.md', recursive=True)):
    t = open(p, encoding='utf-8').read()
    m = FM.match(t)
    name = os.path.relpath(p, 'WIKI').replace('\\', '/')
    if not m:
        fail.append((name, '无 front matter'))
        continue
    body = m.group(1)
    tm = re.search(r'^type:\s*(\S+)', body, re.M)
    if not tm:
        fail.append((name, '缺 type'))
        continue
    typ = tm.group(1)
    if typ in MOC_TYPES:
        ok += 1                      # MOC 豁免（不参与 status 治理，AGENTS §1）
        continue
    if typ not in REQ:
        fail.append((name, 'type 非法: ' + typ))
        continue
    miss = [k for k in REQ[typ] if not re.search(r'^' + k + r':', body, re.M)]
    if miss:
        fail.append((name, '缺字段 ' + ','.join(miss)))
    else:
        ok += 1
        print('  OK  %-11s %s' % (typ, name))
print()
print('=== front matter 校验 ===')
print('  通过 %d / %d' % (ok, ok + len(fail)))
for p, r in fail:
    print('  FAIL', r, '->', p)

# ---- 3. 索引与实际文件对齐检查 ----
print()
print('=== index.md 与文件系统对齐 ===')
idx = open('index.md', encoding='utf-8').read()
actual = {os.path.splitext(os.path.basename(p))[0] for p in glob.glob('WIKI/**/*.md', recursive=True)}
listed = set(re.findall(r'\[\[([^\]|#]+)\]\]', idx)) & actual
print('  实际页面:', len(actual), ' 索引已收录:', len(listed))
missing_in_index = sorted(actual - listed)
if missing_in_index:
    print('  索引缺失:', missing_in_index)
else:
    print('  索引覆盖完整：所有页面均已收录')

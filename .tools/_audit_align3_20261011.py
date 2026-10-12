import os, re, glob
from collections import Counter

ROOT = 'E:/WKB-OB'
RAW = os.path.join(ROOT, 'RAW', 'ima_sync')
def norm(p): return p.replace('\\', '/')
def readrel(p):
    try: return open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()
    except OSError: return ''

raw = []
for dp, dn, fn in os.walk(RAW):
    for f in fn:
        if f.endswith('.md'):
            raw.append(norm(os.path.relpath(os.path.join(dp, f), ROOT)))
rawset = set(raw)

srcpages = glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md'))
sp = {}
for p in srcpages:
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_path:\s*(.+)$', t, re.M)
    if m:
        v = norm(m.group(1).strip().strip('"'))
        if v.startswith('raw/'): v = 'RAW/' + v.split('/', 1)[1]
        sp.setdefault(v, []).append(os.path.basename(p))

UNSUP = '暂不支持自动同步内容'
MD_RE = re.compile(r'media_id["\']?\s*[:=]\s*["\']?([A-Za-z0-9_+/=-]+)')
EXTRACT = re.compile(r'extract_status:\s*"?(ok|empty|original-only)"?')

# source_path 指向 RAW_FULL 的（book-index 元数据特例）
full_anchor = [k for k in sp if k.startswith('RAW_FULL/')]
raw_anchor = [k for k in sp if k.startswith('RAW/')]
print('=' * 70)
print('【指标 1】source 页锚点分布')
print('  source 页总数            :', len(srcpages))
print('  锚点指 RAW/              :', len(raw_anchor))
print('  锚点指 RAW_FULL/（book-index 元数据特例，日志 09-30 已登记 8 个）:', len(full_anchor))
print('  RAW_FULL 锚点明细:')
for k in sorted(full_anchor):
    print('      ', k, '->', sp[k])

hit = [k for k in raw_anchor if k in rawset]
dang = [k for k in raw_anchor if k not in rawset]
print('  RAW锚点命中实际文件      :', len(hit))
print('  RAW锚点悬空              :', len(dang))

print()
print('=' * 70)
print('【指标 2】编译覆盖率（分母口径决定结论）')
att = [x for x in rawset if '/attachments/' in x]
non_att = [x for x in rawset if '/attachments/' not in x]
print('  RAW md 总数                    :', len(rawset))
print('  其中 attachments/ 子目录       :', len(att), '(设计如此：不逐个编译)')
print('  非 attachments 的知识条目      :', len(non_att))
print('  已建 source 页（RAW 锚点命中） :', len(hit))
cov_all = 100.0 * len(hit) / len(rawset)
cov_non = 100.0 * len(hit) / len(non_att)
print('  >> 覆盖率（全量口径）          : %.1f%%' % cov_all)
print('  >> 覆盖率（排除 attachments）  : %.1f%%' % cov_non)

print()
print('=' * 70)
print('【指标 3】非attachments 未编译条目再分层')
missing = sorted(set(non_att) - set(hit))
b = Counter(); real = []
for m in missing:
    t = readrel(m)
    if UNSUP in t: b['A_占位符-插件取正文失败'] += 1
    elif EXTRACT.search(t): b['B_RAW_FULL已回填正文'] += 1; real.append(m)
    elif len(t) >= 600: b['C_有正文但无extract标记'] += 1; real.append(m)
    else: b['D_空壳（<600字节）'] += 1
for k, v in sorted(b.items()): print('  %-28s %d' % (k, v))
print('  >> 真正「有内容可编译」的欠账 = B + C =', len(real))

print()
print('=' * 70)
print('【指标 4】占位符归因检验：是否等于「未存入 IMA」')
unsup = [x for x in rawset if UNSUP in readrel(x)]
fullset = set()
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW_FULL')):
    for f in fn:
        if f.endswith('.md'):
            fullset.add(norm(os.path.relpath(os.path.join(dp, f), ROOT)).replace('RAW_FULL/', 'RAW/', 1))
withbody = [x for x in unsup if x in fullset]
print('  RAW 侧占位符「暂不支持」总数   :', len(unsup))
print('  其中 RAW_FULL 已有正文（→ 可编译，插件失败所致）:', len(withbody))
print('  >> 占位符中真正「IMA 无内容」的 :', len(unsup) - len(withbody))
bytype = Counter()
for x in unsup:
    t = readrel(x)
    m = re.search(r'此条目为(.{1,12}?)，暂不支持', t)
    bytype[m.group(1) if m else '?'] += 1
for k, v in bytype.most_common(): print('      %-22s %d' % (k, v))

print()
print('=' * 70)
print('【指标 5】source 页按 source_type 分布')
tc = Counter()
for p in srcpages:
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_type:\s*(.+)$', t, re.M)
    tc[(m.group(1).strip().strip('"') if m else '?')] += 1
for k, v in tc.most_common(): print('  %-16s %d' % (k, v))
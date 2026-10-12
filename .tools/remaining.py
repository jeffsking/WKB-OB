# -*- coding: utf-8 -*-
"""剩余待编译统计（权威判据：source 页 front matter 的 source_path / source_paths 覆盖批次 src）。
用法: python .tools/remaining.py
"""
import json, re, glob, os

vals = set()
pat_single = re.compile(r'source_paths?:\s*(.*)$')
pat_list = re.compile(r'^\s*-\s*(.+)$')
for f in glob.glob('WIKI/sources/*.md'):
    t = open(f, encoding='utf-8', errors='ignore').read()
    fm = t.split('---')[1] if t.startswith('---') else ''
    cur = False
    for ln in fm.split('\n'):
        m = pat_single.match(ln)
        if m:
            v = m.group(1).strip()
            if v in ('|', '>-', '>', ''):
                cur = True; continue
            vals.add(v.strip('"\'').strip()); cur = False
        elif cur:
            m2 = pat_list.match(ln)
            if m2:
                vals.add(m2.group(1).strip().strip('"\'').strip())

idx = json.load(open('.tools/_compile_batch_index.json', encoding='utf-8'))
tot = 0
per = {}
for r in idx:
    if r['stage'] == 'S6':
        continue
    items = json.load(open('.tools/compile_batches/' + r['file'], encoding='utf-8'))['items']
    rem = [it for it in items if it['src'] not in vals]
    if rem:
        per.setdefault(r['stage'], []).append((r['file'], len(items), rem, r['bytes'] / 1024))
        tot += len(rem)

for st in sorted(per):
    print('=== %s：剩 %d 份 ===' % (st, sum(len(x[2]) for x in per[st])))
    for fn, n, rem, kb in sorted(per[st]):
        print('   %-50s 剩 %2d / %2d  (%4.0f KB)' % (fn, len(rem), n, kb))
        for it in rem:
            print('        ↳ %s' % it['src'].rsplit('/', 1)[-1])
print('\n>>> 全部剩余待编译：%d 份' % tot)

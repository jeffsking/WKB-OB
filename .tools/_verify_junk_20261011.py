# -*- coding: utf-8 -*-
"""核验：垃圾件过滤是否真的生效 + 17 条垃圾件都在哪"""
import json, os, re
ROOT = 'E:/WKB-OB'
rows = json.load(open(os.path.join(ROOT, '.tools/compile_plan/nonbook_backlog.json'), encoding='utf-8'))

J = [r for r in rows if r.get('junk')]
print(f'JSON 中标记junk=True: {len(J)} 条')
print()
print('=== 垃圾件所在二级区分布 ===')
from collections import Counter
for k, v in Counter(r['z2'] for r in J).most_common():
    print(f'  {v:>3}  {k}')
print()
print('=== 垃圾件明细 ===')
for r in sorted(J, key=lambda x: x['path']):
    print(f"  [{r['z2']:<16}] {r['title'][:66]}")
print()
print('=== B07 (WKB根级) 实际条数校验 ===')
b07 = [r for r in rows if r['z2'] == 'WKB根级']
print(f'  JSON 中 WKB根级: {len(b07)} 条，其中 junk: {sum(1 for r in b07 if r.get("junk"))}')
print()
print('=== B07 有效件（应进批次）===')
for r in sorted([x for x in b07 if not x.get('junk')], key=lambda y: y['path']):
    print(f"  {r['title'][:70]}")
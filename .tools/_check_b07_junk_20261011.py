# -*- coding: utf-8 -*-
"""只读：检查 B07 根级批次里的垃圾件比例"""
import os, re, collections

ROOT = 'E:/WKB-OB'
p = '.tools/compile_plan/P1-B07_WKB根级.md'
t = open(os.path.join(ROOT, p), encoding='utf-8').read()
BT = chr(96)
rows = [l for l in t.splitlines() if l.startswith('| ') and BT in l]
print(f'B07 共 {len(rows)} 条')

JUNK = re.compile(r'^(我先|让我|首先|接下来|下面是|这是一个|以下是|好的|现在)'
                  r'|^(会议纪要[一二三四五六七八九十]?)$'
                  r'|^Screenshot_\d{4}-\d{2}-\d{2}'
                  r'|^\d{6,}$'
                  r'|_by_\d{8}$')
TITLECOL = re.compile(r'^\|\s*(\d+)\s*\|\s*(.+?)\s*\|')

junk, good = [], []
for l in rows:
    m = TITLECOL.match(l)
    if not m: continue
    n, title = m.group(1), m.group(2)
    (junk if JUNK.search(title) or len(title) < 8 else good).append((n, title))

print()
print(f'=== 可疑垃圾件 {len(junk)} 条 ===')
for n, title in junk:
    print(f'  {n:>3}  {title[:75]}')

print()
print(f'=== 有效内容 {len(good)} 条 · 按主题归类 ===')
KW = [('COCO V6 试验', r'COCO|Coco|CI-06'),
      ('REL 超薄芯体', r'REL'),
      ('BNC / 纳米纤维素', r'BNC|纳米纤维素'),
      ('热舒适 / 变色油墨', r'变色|Thermochromic|光子晶体|Active|Thermal'),
      ('会议纪要', r'会议纪要'),
      ('供应商推进', r'供应商拜访|供应商考察|供应链'),
      ('聚合物基础', r'聚合物|PEG|纺丝'),
      ('索引 / 元数据', r'索引|标签体系')]
cnt = collections.Counter()
for n, title in good:
    hit = '其他'
    for k, p_ in KW:
        if re.search(p_, title): hit = k; break
    cnt[hit] += 1
for k, v in cnt.most_common():
    print(f'  {v:>3}  {k}')
print()
for n, title in good:
    print(f'  {n:>3}  {title[:72]}')
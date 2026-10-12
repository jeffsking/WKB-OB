# -*- coding: utf-8 -*-
"""盘点可编译清单并输出批次规划"""
import json, os, re
from collections import Counter, defaultdict

inv = json.load(open('.tools/_inventory.json', encoding='utf-8'))


def norm(p):
    return p.replace('\\', '/')


PREFIX = 'RAW/ima_sync/'


def rel(p):
    """去掉 `ima_sync/<知识库>/WKB/` 前缀，返回库内相对路径（布局无关，勿用固定段位索引）。"""
    n = norm(p)
    if n.startswith(PREFIX):
        seg = n[len(PREFIX):].split('/')
        if len(seg) >= 3 and seg[1] == 'WKB':
            return '/'.join(seg[2:])
    return n


def grp(p):
    r = rel(p).split('/')               # 例: Areas/IP/xxx.md
    if len(r) <= 1:
        return 'ROOT / 根层级'
    sub = r[1] if len(r) > 2 else ''
    return r[0] + (' / ' + sub if sub and not sub.endswith('.md') else '')


print('=== 可编译 %d 份 · 按目录细分组 ===' % len(inv['valid']))
c = defaultdict(list)
for p in inv['valid']:
    c[grp(p)].append(p)
for k in sorted(c, key=lambda x: -len(c[x])):
    print('  %4d  %s' % (len(c[k]), k))

print()
print('=== 占位符 %d 份 · 按附件扩展名 ===' % len(inv['stub']))
ext = Counter()
for p in inv['stub']:
    m = re.search(r'\.(pdf|docx|doc|pptx|ppt|xlsx|xls|csv)\.md$', p, re.I)
    ext[m.group(1).lower() if m else 'other'] += 1
for k, v in ext.most_common():
    print('  %4d  .%s' % (v, k))

print()
print('=== 根层级可编译清单 ===')
for p in sorted(c['ROOT / 根层级']):
    print('   -', os.path.basename(p))

print()
print('=== Projects 可编译清单 ===')
for p in sorted(c.get('Projects', [])):
    print('   -', norm(p))

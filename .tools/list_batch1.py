# -*- coding: utf-8 -*-
"""列出第一批（研发核心层）的确切文件清单"""
import json, os

inv = json.load(open('.tools/_inventory.json', encoding='utf-8'))


def norm(p):
    return p.replace('\\', '/')


PREFIX = 'RAW/ima_sync/'


def rel(n):
    """去掉 `ima_sync/<知识库>/WKB/` 前缀，返回库内相对路径。
    布局无关：2026-09-28 IMA 在 ima_sync 下插入过 `个人知识库/` 一段，不能用固定段位索引。"""
    if n.startswith(PREFIX):
        seg = n[len(PREFIX):].split('/')
        if len(seg) >= 3 and seg[1] == 'WKB':
            return '/'.join(seg[2:])
    return n


b1 = []
for p in inv['valid']:
    n = norm(p)
    r = rel(n)
    if '/' not in r:                    # 根层级
        b1.append(p)
    elif '/Projects/' in n:
        b1.append(p)

b1.sort(key=lambda x: (norm(x).count('/'), norm(x)))
print('第一批共 %d 份：' % len(b1))
for p in b1:
    print('  %7d B  %s' % (os.path.getsize(p), norm(p)))

json.dump(b1, open('.tools/_batch1.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('\n已写 .tools/_batch1.json')

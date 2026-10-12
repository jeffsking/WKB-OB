# -*- coding: utf-8 -*-
"""解析并修复 WIKI 断链 + 诊断 title/文件名不一致。

断链来源（实测）：并发代理写 `[[链接]]` 时用了页面「标题」的长写法或括号后缀，
而实际文件名是短形式（Obsidian 按 basename 解析）→ 链接失配。

策略（幂等）：
  1. 精确匹配 basename → 保留
  2. 归一化匹配（去括号内容 / 去空格 / 大小写 / 去标点）→ 唯一命中则改写链接为真实 basename
  3. 仍无命中 → 列为「真实缺失」，不擅自删链接（可能是代理计划页未创建）

用法：
  python .tools/fix_broken_links.py            # dry-run
  python .tools/fix_broken_links.py --apply    # 执行
"""
import glob
import os
import re
import sys
from collections import Counter, defaultdict

VAULT = r'E:\WKB-OB'


def norm(s):
    s = s.replace('\\', '/').split('/')[-1]
    s = re.sub(r'[（(][^）)]*[）)]', '', s)          # 去括号及内容
    s = re.sub(r'[\s_\-–—×x·、，,。.:：;；"\'“”‘’]', '', s)
    return s.strip().lower()


def main():
    apply = '--apply' in sys.argv
    os.chdir(VAULT)

    files = glob.glob('WIKI/**/*.md', recursive=True)
    base = {os.path.basename(f)[:-3]: f for f in files}
    norm_map = defaultdict(list)
    for n in base:
        norm_map[norm(n)].append(n)

    # 诊断 title vs 文件名
    mism = []
    for f in files:
        t = open(f, encoding='utf-8', errors='ignore').read()
        m = re.search(r'^title:\s*"?(.+?)"?\s*$', t, re.M)
        if m:
            title = m.group(1).strip().strip('"')
            if norm(title) != norm(os.path.basename(f)[:-3]):
                mism.append((os.path.basename(f)[:-3], title))
    print('=== title 与文件名不一致的页面: %d ===' % len(mism))
    for fn, ti in mism[:12]:
        print('   文件 %s\n     title %s' % (fn, ti))
    if len(mism) > 12:
        print('   ...（其余 %d 条）' % (len(mism) - 12))

    # 收集链接
    link_re = re.compile(r'\[\[([^\]\|#]+)(\|[^\]]*)?\]\]')
    fixes, missing = Counter(), Counter()
    per_file = defaultdict(list)
    for f in files:
        t = open(f, encoding='utf-8', errors='ignore').read()
        for m in link_re.finditer(t):
            tgt = m.group(1).strip()
            if tgt in base:
                continue
            cand = norm_map.get(norm(tgt), [])
            if len(cand) == 1:
                fixes[(tgt, cand[0])] += 1
                per_file[f].append((tgt, cand[0]))
            else:
                missing[tgt] += 1

    print('\n=== 可自动修复（归一化唯一命中）: %d 种，共 %d 处 ==='
          % (len(fixes), sum(fixes.values())))
    for (a, b), c in fixes.most_common(15):
        print('   %-56s -> %s  (%d 处)' % (a[:56], b[:40], c))

    print('\n=== 真实缺失（无任何命中）: %d 种 ===' % len(missing))
    for k, v in missing.most_common(15):
        print('   %-56s 被引 %d 次' % (k[:56], v))

    if apply:
        n_file = n_link = 0
        for f, pairs in per_file.items():
            t = open(f, encoding='utf-8', errors='ignore').read()
            orig = t
            for a, b in pairs:
                t = re.sub(r'\[\[' + re.escape(a) + r'(\|[^\]]*)?\]\]',
                           lambda m, _b=b: '[[' + _b + (m.group(1) or '') + ']]', t)
            if t != orig:
                open(f, 'w', encoding='utf-8').write(t)
                n_file += 1
                n_link += len(pairs)
        print('\n已修复: %d 个文件 / %d 处链接' % (n_file, n_link))
        print('重跑 python .tools/verify_wiki.py 复核')
    else:
        print('\n（dry-run，加 --apply 执行）')


if __name__ == '__main__':
    main()

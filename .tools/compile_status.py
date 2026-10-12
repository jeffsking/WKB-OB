# -*- coding: utf-8 -*-
"""编译波次完成度状态：以「源摘要页的 source_path 是否覆盖批次 src」为权威判据。

（不依赖子代理回执——实测会出现「页面已产出但代理中途死掉没写回执」的情况。）

用法：python .tools/compile_status.py [stage]   # stage 可选，如 S1
"""
import glob
import json
import os
import re
import sys
from collections import defaultdict

VAULT = r'E:\WKB-OB'


def sp_of(path):
    """取源摘要页 front matter 的 source_path。"""
    t = open(path, encoding='utf-8', errors='ignore').read(1500)
    m = re.search(r'^source_path:\s*"?([^"\r\n]+)', t, re.M)
    return m.group(1).strip().rstrip('"') if m else None


def main():
    os.chdir(VAULT)
    only = sys.argv[1] if len(sys.argv) > 1 else None

    # 已编译的 source_path 全集（正反斜杠统一）
    compiled = set()
    for f in glob.glob('WIKI/sources/*.md'):
        v = sp_of(f)
        if v:
            compiled.add(v.replace('\\', '/').strip())

    rows = []
    for bf in sorted(glob.glob('.tools/compile_batches/*.json')):
        d = json.load(open(bf, encoding='utf-8'))
        st = d.get('stage', '?')
        if only and st != only:
            continue
        items = d.get('items', [])
        cov = [it for it in items if it['src'].replace('\\', '/').strip() in compiled]
        has_receipt = os.path.exists(
            os.path.join('.tools/compile_batches/_done',
                         os.path.basename(bf)))
        rows.append({'file': os.path.basename(bf), 'stage': st, 'block': d.get('block', ''),
                     'n': len(items), 'cov': len(cov), 'receipt': has_receipt})

    print('%-46s %-3s %5s %6s %s' % ('批次', '阶段', '份数', '已编译', '状态'))
    print('-' * 78)
    agg = defaultdict(lambda: [0, 0, 0])
    for r in rows:
        st = '✅ 完成' if r['cov'] == r['n'] and r['n'] else (
            '🟡 部分 %d/%d' % (r['cov'], r['n']) if r['cov'] else '⬜ 未开始')
        if r['cov'] == r['n'] and r['n'] and not r['receipt']:
            st += '（无回执）'
        print('%-46s %-3s %5d %6d %s' % (r['file'][:46], r['stage'], r['n'], r['cov'], st))
        a = agg[r['stage']]
        a[0] += 1
        a[1] += r['n']
        a[2] += r['cov']

    print('-' * 78)
    print('%-6s %6s %8s %8s %8s' % ('阶段', '批数', '份数', '已编译', '完成率'))
    tot = [0, 0, 0]
    for st in sorted(agg):
        b, n, c = agg[st]
        print('%-6s %6d %8d %8d %7.1f%%' % (st, b, n, c, 100.0 * c / n if n else 0))
        tot[0] += b
        tot[1] += n
        tot[2] += c
    print('%-6s %6d %8d %8d %7.1f%%' % ('合计', tot[0], tot[1], tot[2],
                                         100.0 * tot[2] / tot[1] if tot[1] else 0))
    print('\nWIKI 现有页面：', end='')
    for sub in ['sources', 'concepts', 'entities', 'comparisons']:
        print('%s %d ' % (sub, len(glob.glob('WIKI/%s/*.md' % sub))), end='')
    print()


if __name__ == '__main__':
    main()

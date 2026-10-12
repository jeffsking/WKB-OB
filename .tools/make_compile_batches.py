# -*- coding: utf-8 -*-
"""按「编译恢复方案」生成 S1–S7 各阶段的批次清单（用户已定：Ebook 暂跳过）。

输入：.tools/_compile_plan_data.json（compile_plan_data.py 产出）
输出：.tools/compile_batches/<stage>_<block>_<nn>.json
     每批结构 {"stage","block","items":[{"src","dst","read","name","title_hint"}...]}
     read = 实际读取路径（优先 RAW_FULL，缺失回退 RAW）

用法：python .tools/make_compile_batches.py [--skip-ebook]
"""
import json
import os
import re
import sys
from collections import defaultdict

VAULT = r'E:\WKB-OB'
FILE_EXT = re.compile(r'\.(md|pdf|docx|pptx|xlsx|csv|txt|jmp|doc|xls|ppt)$', re.I)

STAGES = [
    ('S1', ['Projects/']),
    ('S2', ['Areas/Test Method', 'Areas/IP']),
    ('S3', ['Areas/Supply Base', 'Areas/Regulation&PSC', 'Areas/Market Insight', 'Areas/Personal']),
    ('S4', ['Resources/Open Innovation', 'Resources/Training', 'Resources/Pulp World', 'Resources/FEI']),
    ('S5', ['Areas/Meeting Minutes']),
    ('S6', ['Resources/Ebook']),
    ('S7', ['(根', 'Archives', 'attachment']),
]


def block_of(dst):
    p = dst.replace('\\', '/').split('/')
    i = p.index('WKB') if 'WKB' in p else 0
    tail = p[i + 1:]
    if not tail or FILE_EXT.search(tail[0]):
        return '(根层级)'
    if len(tail) == 1:
        return tail[0] + '/(直属文件)'
    if FILE_EXT.search(tail[1]):
        return tail[0] + '/(直属文件)'
    return tail[0] + '/' + tail[1]


def stage_of(blk):
    for s, keys in STAGES:
        for k in keys:
            if blk.startswith(k):
                return s
    return 'S7'


def safe(s):
    return re.sub(r'[\\/:*?"<>|]', '_', s)[:60]


def main():
    os.chdir(VAULT)
    skip_ebook = '--skip-ebook' in sys.argv or True   # 用户已定：Ebook 暂跳过（与方案一致）
    data = json.load(open('.tools/_compile_plan_data.json', encoding='utf-8'))
    out_dir = os.path.join('.tools', 'compile_batches')
    os.makedirs(out_dir, exist_ok=True)

    # 清理旧批次文件（只清本脚本自己写的）
    for f in os.listdir(out_dir):
        if f.endswith('.json'):
            os.remove(os.path.join(out_dir, f))

    index = []
    counter = defaultdict(int)
    for blk, batches in data['plan'].items():
        st = stage_of(blk)
        if skip_ebook and st == 'S6':
            continue
        for bi, items in enumerate(batches, 1):
            counter[(st, blk)] += 1
            recs = []
            for dst in items:
                src = dst.replace('RAW_FULL/', 'RAW/', 1)
                read = dst if os.path.exists(dst.replace('/', os.sep)) else src
                name = os.path.basename(dst)
                title_hint = re.sub(r'\.(md|pdf|docx|pptx|xlsx|csv|txt|jmp|doc|xls|ppt)$', '', name, flags=re.I)
                recs.append({'src': src, 'dst': dst, 'read': read,
                             'name': name, 'title_hint': title_hint})
            fn = '%s_%s_%02d.json' % (st, safe(blk), counter[(st, blk)])
            path = os.path.join(out_dir, fn)
            json.dump({'stage': st, 'block': blk, 'items': recs},
                      open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            index.append({'file': fn, 'stage': st, 'block': blk,
                          'n': len(recs), 'bytes': sum(
                              os.path.getsize(r['read'].replace('/', os.sep))
                              for r in recs if os.path.isfile(r['read'].replace('/', os.sep)))})

    json.dump(index, open('.tools/_compile_batch_index.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    print('已生成 %d 个批次文件（Ebook %s）' % (len(index), '已跳过' if skip_ebook else '含'))
    bystage = defaultdict(lambda: [0, 0, 0])
    for r in index:
        bystage[r['stage']][0] += 1
        bystage[r['stage']][1] += r['n']
        bystage[r['stage']][2] += r['bytes']
    print('%-4s %6s %7s %10s' % ('阶段', '批数', '份数', 'MB'))
    for st in sorted(bystage):
        b, n, sz = bystage[st]
        print('%-4s %6d %7d %10.1f' % (st, b, n, sz / 1e6))
    print('\n批次索引: .tools/_compile_batch_index.json')


if __name__ == '__main__':
    main()

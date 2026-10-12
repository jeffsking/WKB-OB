# -*- coding: utf-8 -*-
"""为「恢复编译」方案做数据准备：积压分块、体量分析、批次切分与产出估算。

输出 .tools/_compile_plan_data.json 供方案书引用。
"""
import json
import os
import re
from collections import Counter, defaultdict

VAULT = r'E:\WKB-OB'


def strip_fm(t):
    if t.startswith('---'):
        parts = t.split('\n---', 1)
        if len(parts) == 2:
            t = parts[1].lstrip('-\n')
    return t


def net_len(p):
    t = open(p, encoding='utf-8', errors='ignore').read()
    t = strip_fm(t)
    t = re.sub(r'^\s*#.*$', '', t, flags=re.M)
    t = re.sub(r'\[\[[^\]]*\]\]', '', t)
    t = re.sub(r'\[图片[^\]]*\]', '', t)
    return len(re.sub(r'\s', '', t))


FILE_EXT = re.compile(r'\.(md|pdf|docx|pptx|xlsx|csv|txt|jmp|doc|xls|ppt)$', re.I)


def block_of(dst):
    """把 dst 映射到业务区块（把直属文件归入 '/(直属文件)'，避免按文件名碎成单例块）。"""
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


# 推进阶段（按业务优先级；用户核心业务 = REL 芯体/纸尿裤 + 采购/木浆）
STAGES = [
    ('S1 直接项目层', ['Projects/']),
    ('S2 方法与专利', ['Areas/Test Method', 'Areas/IP']),
    ('S3 供应·法规·市场', ['Areas/Supply Base', 'Areas/Regulation&PSC',
                          'Areas/Market Insight', 'Areas/Personal']),
    ('S4 创新素材·培训', ['Resources/Open Innovation', 'Resources/Training',
                          'Resources/Pulp World', 'Resources/FEI']),
    ('S5 会议纪要', ['Areas/Meeting Minutes']),
    ('S6 大部头书籍', ['Resources/Ebook']),
    ('S7 根层级·归档·其他', ['(根', 'Archives', 'attachment']),
]


def stage_of(blk):
    for name, keys in STAGES:
        for k in keys:
            if blk.startswith(k):
                return name
    return 'S7 根层级·归档·其他'


def main():
    os.chdir(VAULT)
    backlog = json.load(open('.tools/_compile_backlog.json', encoding='utf-8'))

    sizes = []
    for d in backlog:
        p = d.replace('/', os.sep)
        sizes.append((d, net_len(p), os.path.getsize(p)))

    sizes.sort(key=lambda x: -x[1])
    n = len(sizes)
    lens = [s[1] for s in sizes]
    print('待编译积压: %d 份' % n)
    print('净正文字数：max %d / p90 %d / 中位 %d / min %d'
          % (lens[0], lens[int(n * 0.1)], lens[n // 2], lens[-1]))

    buckets = Counter()
    for _, L, _ in sizes:
        if L < 1000:
            buckets['<1k'] += 1
        elif L < 5000:
            buckets['1k–5k'] += 1
        elif L < 20000:
            buckets['5k–20k'] += 1
        elif L < 100000:
            buckets['20k–100k'] += 1
        elif L < 500000:
            buckets['100k–500k'] += 1
        else:
            buckets['>500k'] += 1
    print('\n体量分档:', dict(buckets))

    blocks = Counter(block_of(d) for d, _, _ in sizes)
    print('\n按区块:')
    for k, v in blocks.most_common():
        sub = [L for d, L, _ in sizes if block_of(d) == k]
        print('  %-34s %4d 份  总字数 %9d  中位 %6d' % (k, v, sum(sub), sorted(sub)[len(sub) // 2]))

    # 批次切分：普通 10 份/批；>100k 字的每批 3 份；>500k 单独 1 份
    plan = {}
    for blk, _cnt in blocks.most_common():
        items = [(d, L) for d, L, _ in sizes if block_of(d) == blk]
        items.sort(key=lambda x: -x[1])
        big = [x for x in items if x[1] >= 500000]
        mid = [x for x in items if 100000 <= x[1] < 500000]
        nor = [x for x in items if x[1] < 100000]
        batches = []
        for x in big:
            batches.append([x[0]])
        for i in range(0, len(mid), 3):
            batches.append([y[0] for y in mid[i:i + 3]])
        for i in range(0, len(nor), 10):
            batches.append([y[0] for y in nor[i:i + 10]])
        plan[blk] = batches

    total_batches = sum(len(v) for v in plan.values())
    print('\n=== 批次切分（普通 10 份/批；100k–500k 3 份/批；≥500k 1 份/批）===')
    for blk in sorted(plan, key=lambda k: -len(plan[k])):
        bs = plan[blk]
        cnts = [len(b) for b in bs]
        print('  %-34s %3d 批  (每批 %d–%d 份, 计 %d 份)'
              % (blk, len(bs), min(cnts), max(cnts), sum(cnts)))
    print('  %-34s %3d 批 合计 %d 份' % ('总计', total_batches, sum(sum(len(b) for b in v) for v in plan.values())))

    json.dump({'plan': plan,
               'blocks': dict(blocks),
               'buckets': dict(buckets),
               'size_max': lens[0], 'size_median': lens[n // 2],
               'total': n, 'total_batches': total_batches},
              open('.tools/_compile_plan_data.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    # ---------- 按推进阶段汇总 ----------
    print('\n=== 按推进阶段汇总 ===')
    stage_sum = defaultdict(lambda: {'files': 0, 'chars': 0, 'batches': 0})
    for blk in plan:
        st = stage_of(blk)
        stage_sum[st]['files'] += sum(len(b) for b in plan[blk])
        stage_sum[st]['batches'] += len(plan[blk])
    for d, L, _ in sizes:
        stage_sum[stage_of(block_of(d))]['chars'] += L
    order = [s[0] for s in STAGES]
    print('  %-22s %6s %8s %14s %7s' % ('阶段', '份数', '批数', '总字数', 'MB'))
    for st in order + [k for k in stage_sum if k not in order]:
        v = stage_sum.get(st)
        if not v or not v['files']:
            continue
        print('  %-22s %6d %8d %14d %7.1f'
              % (st, v['files'], v['batches'], v['chars'], v['chars'] / 1e6))

    print('\n已写 .tools/_compile_plan_data.json')


if __name__ == '__main__':
    main()

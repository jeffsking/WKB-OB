# -*- coding: utf-8 -*-
"""生成压测批次：从高位队列按类型配额选 30 份，打散成 3 批 ×10，写 .tools/pilot/batch_N.json"""
import json, os
from collections import defaultdict, Counter

queue = json.load(open('.tools/_extract_queue.json', encoding='utf-8'))

# 每类型配额（共 30），保证覆盖全部清洗场景
QUOTA = {'pdf': 8, 'markdown': 6, 'ppt': 6, 'word': 4, 'excel': 3, 'soundrecording': 2, 'html': 1}

picked = defaultdict(list)
for q in queue:                        # 已按价值降序
    t = q['type']
    if len(picked[t]) < QUOTA.get(t, 0):
        picked[t].append(q)

pool = []
for t, items in picked.items():
    pool.extend(items)

# 打散：按类型轮转排序，再切成 3 批
by_type = defaultdict(list)
for q in pool:
    by_type[q['type']].append(q)
order = sorted(by_type, key=lambda t: -QUOTA.get(t, 0))
inter = []
while any(by_type.values()):
    for t in order:
        if by_type[t]:
            inter.append(by_type[t].pop(0))

os.makedirs('.tools/pilot', exist_ok=True)
N = 3
batches = []
for i in range(N):
    chunk = inter[i::N]                # 跨步切分 → 每批类型混合
    b = {'batch_id': i + 1, 'items': [
        {'media_id': q['media_id'], 'dst': q['dst'], 'name': q['name'], 'type': q['type']}
        for q in chunk]}
    json.dump(b, open('.tools/pilot/batch_%d.json' % (i + 1), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    batches.append(b)

print('=== 压测批次已生成 ===')
print('入选总数:', len(inter))
print('类型分布:', dict(Counter(q['type'] for q in inter)))
print()
for b in batches:
    print('--- batch %d（%d 份）---' % (b['batch_id'], len(b['items'])))
    for it in b['items']:
        print('   %-14s %s' % (it['type'], it['dst'].replace('RAW_FULL/', '')))
    print()

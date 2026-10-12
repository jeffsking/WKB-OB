# -*- coding: utf-8 -*-
"""
波次生成器：从提取台账里挑 pending 项，按价值分降序切成波次批次。
用法：python .tools/make_wave.py <wave名> <批数> <每批份数> [最低分 | 分值列表]
例：  python .tools/make_wave.py W1 3 10 100
      python .tools/make_wave.py W6 3 8 74,55,40   # 只取指定分值档（可跳过中间档）
输出：.tools/pilot/<wave>_batch_<n>.json
"""
import json, os, sys
from collections import defaultdict

wave = sys.argv[1] if len(sys.argv) > 1 else 'W1'
nb = int(sys.argv[2]) if len(sys.argv) > 2 else 3
bs = int(sys.argv[3]) if len(sys.argv) > 3 else 10
min_score = 0
score_list = None
if len(sys.argv) > 4:
    if ',' in sys.argv[4]:
        score_list = sorted((int(x) for x in sys.argv[4].split(',')), reverse=True)
    else:
        min_score = int(sys.argv[4])

led = json.load(open('.tools/_extract_ledger.json', encoding='utf-8'))
if score_list is not None:
    pend = [l for l in led if l['status'] == 'pending' and l['score'] in score_list]
else:
    pend = [l for l in led if l['status'] == 'pending' and l['score'] >= min_score]
pend.sort(key=lambda x: (-x['score'], x['src']))

# 排除已出现在任何既有批次中的条目（台账未及时更新时防重复切批）
import glob as _glob
batched = set()
for _f in _glob.glob('.tools/pilot/*_batch_*.json'):
    try:
        for _it in json.load(open(_f, encoding='utf-8'))['items']:
            batched.add(_it['media_id'])
    except Exception:
        pass
_unbatched = [l for l in pend if l['media_id'] not in batched]
if len(_unbatched) != len(pend):
    print('已剔除已入批条目: %d' % (len(pend) - len(_unbatched)))
pend = _unbatched

need = nb * bs
sel = pend[:need]
_tag = ('分值档 %s' % score_list) if score_list is not None else ('≥%d' % min_score)
print('待处理(%s): %d ｜ 本次选取: %d' % (_tag, len(pend), len(sel)))

# 按类型轮转打散，保证每批类型混合
by_type = defaultdict(list)
for q in sel:
    by_type[q['type']].append(q)
order = sorted(by_type, key=lambda t: -len(by_type[t]))
inter = []
while any(by_type.values()):
    for t in order:
        if by_type[t]:
            inter.append(by_type[t].pop(0))

os.makedirs('.tools/pilot', exist_ok=True)
for i in range(nb):
    chunk = inter[i::nb]
    if not chunk:
        continue
    b = {'batch_id': '%s-%d' % (wave, i + 1), 'items': [
        {'media_id': q['media_id'], 'dst': q['dst'], 'name': q['name'], 'type': q['type']}
        for q in chunk]}
    fn = '.tools/pilot/%s_batch_%d.json' % (wave, i + 1)
    json.dump(b, open(fn, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('  %s  (%d 份)' % (fn, len(chunk)))
    for it in chunk:
        print('     %-13s %s' % (it['type'], it['dst'].replace('RAW_FULL/', '')))

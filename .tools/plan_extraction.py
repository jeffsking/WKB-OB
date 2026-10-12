# -*- coding: utf-8 -*-
"""
占位符正文提取 · 调度规划
1) 读 .tools/_media_ids.json（1151 条）
2) 排除不可提取类型（img / wechatarticle）与已知加密件
3) 按业务价值打分排序
4) 输出：
   - .tools/_extract_queue.json   全量有序待提取队列（含 RAW_FULL 目标路径）
   - .tools/_extract_skipped.json 排除项
   - .tools/pilot/batch_*.json    压测批次（默认 3 批 × 10 份）
"""
import json, os, re, io

ROOT = os.getcwd()
recs = json.load(open('.tools/_media_ids.json', encoding='utf-8'))

def norm(p):
    return p.replace('\\', '/')

# ---------- 排除规则 ----------
SKIP_PREFIX = {'img', 'wechatarticle'}          # 实测返回近乎空 / 仅图片链接
SKIP_NAME_PAT = re.compile(r'加密|encrypt|MIP|RMS|PTT_PVA_Composition', re.I)

# ---------- 价值打分 ----------
def score(p):
    s = norm(p)
    if '/Projects/' in s:                     return 100
    if 'Meeting Minutes' in s:                return 92
    if '/Supply Base/' in s:                  return 88
    if '/Regulation' in s:                    return 78
    if '/Market Insight' in s:                return 74
    if '/Inbox/' in s:                        return 70
    if '/Areas/' in s:                        return 66
    if '/Archives/' in s:                     return 40
    if '/Resources/' in s:                    return 30
    return 55                                  # 根层级

queue, skipped = [], []
for r in recs:
    mid = r['media_id']
    p = r['path']
    pref = mid.split('_')[0]
    base = os.path.basename(norm(p))
    if pref in SKIP_PREFIX:
        skipped.append({'path': norm(p), 'media_id': mid, 'reason': 'type-%s' % pref})
        continue
    if SKIP_NAME_PAT.search(base):
        skipped.append({'path': norm(p), 'media_id': mid, 'reason': 'encrypted'})
        continue
    # RAW/... -> RAW_FULL/...
    rel = norm(p)
    assert rel.startswith('RAW/'), rel
    dst = 'RAW_FULL/' + rel[len('RAW/'):]
    queue.append({
        'media_id': mid,
        'type': pref,
        'src': rel,
        'dst': dst,
        'name': base,
        'score': score(p),
    })

queue.sort(key=lambda x: (-x['score'], x['src']))

# ---------- 目录建好（懒建的备份） ----------
dirs = sorted({os.path.dirname(q['dst']) for q in queue})
for d in dirs:
    os.makedirs(d, exist_ok=True)

json.dump(queue, open('.tools/_extract_queue.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(skipped, open('.tools/_extract_skipped.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print('=== 队列构建完成 ===')
print('待提取 :', len(queue))
print('已排除 :', len(skipped))
from collections import Counter
print('排除明细:', dict(Counter(s['reason'] for s in skipped)))
print()
print('=== 队列按价值档分布 ===')
for k, v in Counter(q['score'] for q in queue).most_common():
    print(f'  {v:5d}  score={k}')
print()
print('=== 队列按类型分布（前 12）===')
for k, v in Counter(q['type'] for q in queue).most_common(12):
    print(f'  {v:5d}  {k}')
print()
print('=== 前 15 条（最高优先）===')
for q in queue[:15]:
    print('  [%3d] %-12s %s' % (q['score'], q['type'], q['src']))
print()
print('=== RAW_FULL 目录骨架已建：%d 个目录 ===' % len(dirs))

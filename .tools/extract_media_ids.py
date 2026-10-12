# -*- coding: utf-8 -*-
"""从占位符文件中抽取 media_id，按类型分组，输出清单供提取试验使用。"""
import json, os, re
from collections import Counter, defaultdict

inv = json.load(open('.tools/_inventory.json', encoding='utf-8'))
stub = inv['stub']

recs = []
noid = []
for p in stub:
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^media_id:\s*"?([^"\r\n]+)"?', t, re.M)
    if m:
        recs.append({'path': p, 'media_id': m.group(1).strip()})
    else:
        noid.append(p)

print('占位符总数 :', len(stub))
print('含 media_id:', len(recs))
print('无 media_id:', len(noid))
print()

# media_id 前缀（第一个下划线前）
pref = Counter(r['media_id'].split('_')[0] for r in recs)
print('=== media_id 前缀分布 ===')
for k, v in pref.most_common():
    print(f'  {v:5d}  {k}')

print()
# 后缀（是否是 KB ID 统一结尾）
suf = Counter(r['media_id'][-16:] for r in recs)
print('=== media_id 末16位分布 ===')
for k, v in suf.most_common(10):
    print(f'  {v:5d}  {k}')

print()
# 段数分布
seg = Counter(len(r['media_id'].split('_')) for r in recs)
print('=== media_id 下划线段数分布 ===')
for k, v in sorted(seg.items()):
    print(f'  {v:5d}  段数={k}')

print()
print('=== 样例 5 条 ===')
for r in recs[:5]:
    print(' ', r['media_id'])
    print('    <-', os.path.basename(r['path']))

# 落盘
json.dump(recs, open('.tools/_media_ids.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
if noid:
    json.dump(noid, open('.tools/_no_media_id.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
print()
print('已写 .tools/_media_ids.json （%d 条）' % len(recs))
if noid:
    print('已写 .tools/_no_media_id.json （%d 条）' % len(noid))

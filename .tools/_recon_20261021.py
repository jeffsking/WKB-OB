# -*- coding: utf-8 -*-
"""2026-10-21 一次性核对：RAW 实体 vs 账本 raw_path；并定位 dedup 未编译项。"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

s = json.load(open('.tools/_ima_sync_state.json', encoding='utf-8'))['items']
led = {(i.get('raw_path') or '').replace('\\', '/') for i in s.values() if i.get('raw_path')}
raw = set()
for r, d, fs in os.walk('RAW'):
    if 'attachments' in r or '.obsidian' in r:
        continue
    for f in fs:
        if f.endswith('.md'):
            raw.add(os.path.relpath(os.path.join(r, f), '.').replace('\\', '/'))

print('RAW %d / 账本 raw_path %d' % (len(raw), len(led)))
print('--- 账本漏登（RAW 有、账本无）%d ---' % len(raw - led))
for p in sorted(raw - led):
    print('  ', p)
print('--- 账本多登（账本有、RAW 无）%d ---' % len(led - raw))
for p in sorted(led - raw):
    mirror = os.path.exists(p.replace('RAW/', 'RAW_FULL/', 1))
    print('  ', p, 'MIRROR' if mirror else 'NO-MIRROR')

print('\n--- discovered 条目 ---')
for mid, it in s.items():
    if it.get('stage') == 'discovered':
        print('  ', mid, '|', it.get('title'), '| raw_path=', it.get('raw_path'), '| kb_path=', it.get('kb_path'))

print('\n--- 新条目 聚合芯能 账本态 ---')
for mid, it in s.items():
    if '7518291224433921' in mid:
        print(json.dumps(it, ensure_ascii=False, indent=1))

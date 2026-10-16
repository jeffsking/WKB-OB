#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建 2026-10-13 的 enumerate 输入：只喂「枚举有 / 账本无」的 5 条新增 + 根层文件夹。
铁律（MEMORY §2.6）：只喂新增条目，绝不回灌全量路径。"""
import json
import re
from pathlib import Path

ROOT = Path('.')
ENUM = ROOT / '.tools/_ima_enum_20261013.json'
STATE = ROOT / '.tools/_ima_sync_state.json'

d = json.loads(ENUM.read_text(encoding='utf-8'))
s = json.loads(STATE.read_text(encoding='utf-8'))
led = set(s['items'].keys())

# 建 RAW 路径索引（media_id -> RAW 相对路径），只扫 WKB 下
raw_map = {}
for f in (ROOT / 'RAW' / 'ima_sync').rglob('*.md'):
    try:
        t = f.read_text(encoding='utf-8', errors='ignore')[:400]
    except Exception:
        continue
    m = re.search(r'^media_id:\s*"?([^"\n\r]+?)"?\s*$', t, re.M)
    if m:
        raw_map[m.group(1)] = str(f).replace('\\', '/')

new_items = []
for it in d['items']:
    mid = it.get('media_id')
    if not mid or str(mid).startswith('folder_') or it.get('media_type') == 99:
        continue
    if mid in led:
        continue
    rp = raw_map.get(mid)
    if not rp:
        print('[!] 新增条目无 RAW 文件:', mid, it.get('title'))
        kb = (it.get('title') or '') + '.md'
    else:
        kb = rp[len('RAW/'):]  # 例如 ima_sync/个人知识库/WKB/xxx.md
    new_items.append({
        'media_id': mid,
        'media_type': it.get('media_type'),
        'title': it.get('title'),
        'create_time': it.get('create_time'),
        'kb_path': kb,
        'parent_folder_id': it.get('parent_folder_id'),
    })

out = {'root': d['root'], 'items': new_items}
p = ROOT / '.tools/_ima_enum_input_20261013.json'
p.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print('新增条目', len(new_items), '→', p)
for x in new_items:
    print('  +', x['media_id'][:50], '|', x['kb_path'])

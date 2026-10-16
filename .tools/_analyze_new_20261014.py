#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, collections, os
S = json.load(open('.tools/_ima_sync_state.json', encoding='utf-8'))
items = S['items']
print("总", len(items))
print("stage:", dict(collections.Counter(v.get('stage') for v in items.values())))
print("media_type:", dict(collections.Counter(str(v.get('media_type')) for v in items.values())))
new = [(k, v) for k, v in items.items() if v.get('first_seen') == '2026-10-14']
print("今日新增:", len(new))
print("new by (media_type,stage):", {str(k): c for k, c in collections.Counter(
    (v.get('media_type'), v.get('stage')) for k, v in new).items()})
have_raw = 0; noraw = 0
for k, v in new:
    rp = v.get('raw_path')
    if rp and os.path.exists(rp.replace('/', os.sep)):
        have_raw += 1
    else:
        noraw += 1
print("new 有本地RAW:", have_raw, " 无:", noraw)
for k, v in sorted(new, key=lambda x: str(x[1].get('media_type')))[:40]:
    print(" ", v.get('media_type'), '|', v.get('stage'), '|', (v.get('kb_path') or '')[:95])

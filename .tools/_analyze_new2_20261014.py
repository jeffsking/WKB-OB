#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
S = json.load(open('.tools/_ima_sync_state.json', encoding='utf-8'))
items = S['items']
new = [(k, v) for k, v in items.items() if v.get('first_seen') == '2026-10-14']
print("=== 非文件夹新增 ===")
for k, v in new:
    if v.get('media_type') != 99:
        print(json.dumps({k: v}, ensure_ascii=False, indent=1))
print("=== 文件夹新增样例(前3) ===")
n = 0
for k, v in new:
    if v.get('media_type') == 99:
        print(json.dumps({k: v}, ensure_ascii=False, indent=1))
        n += 1
        if n >= 3:
            break

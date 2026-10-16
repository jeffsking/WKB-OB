#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14：清理账本 items 中被误当条目的 folder 记录（media_type==99）。

REST 全量枚举把 folder 条目也塞进了 items，导致 discovered 由 4 虚增到 140。
folder 应只存在于账本的 folders 字典。备份后剔除。
"""
import json
import shutil
import os
from pathlib import Path

STATE = Path('.tools/_ima_sync_state.json')
BAK = Path('.tools/_ima_sync_state.bak.20261014-preclean')
shutil.copy2(STATE, BAK)

s = json.loads(STATE.read_text(encoding='utf-8'))
items = s['items']
before = len(items)

removed = []
for mid in list(items.keys()):
    it = items[mid]
    if it.get('media_type') == 99 and not it.get('raw_path') and not it.get('full_path'):
        removed.append(mid)
        del items[mid]

STATE.write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding='utf-8')

import collections
print(f"备份 -> {BAK}")
print(f"items {before} -> {len(items)}（剔除 folder {len(removed)} 条）")
print("stage:", dict(collections.Counter(v.get('stage') for v in items.values())))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15：本地 RAW ↔ 账本 items 对账，找「RAW 有但账本无」的新条目。"""
import json
import re
from pathlib import Path

ROOT = Path('.')
STATE = Path('.tools/_ima_sync_state.json')


def fm_media_id(txt):
    m = re.search(r'^media_id:[ \t]*["\']?([^"\'\n\r]+)', txt, re.M)
    return m.group(1).strip() if m else None


s = json.loads(STATE.read_text(encoding='utf-8'))
led = set(s['items'].keys())

raw = {}
for f in (ROOT / 'RAW').rglob('*.md'):
    t = f.read_text(encoding='utf-8', errors='ignore')[:1500]
    mid = fm_media_id(t)
    if mid:
        raw[mid] = str(f).replace('\\', '/')

print('RAW media_id 数:', len(raw))
print('账本 items 数  :', len(led))

not_in_led = [(k, v) for k, v in raw.items() if k not in led]
print('RAW 有但账本无 :', len(not_in_led))
for k, v in not_in_led:
    print('   ', k, '->', v.split('/WKB/')[-1])

led_not_raw = [k for k in led if k not in raw]
print('账本有但 RAW 无:', len(led_not_raw))

# -*- coding: utf-8 -*-
"""2026-10-21 账本回绑：为新条目「聚合芯能拜访纪要」补 raw_path / full_path。

背景：kb_sync_handler.py plan 存在 `if not rp: continue` 盲区 —— raw_path 为空的新条目
不进 plan。本条目 RAW 侧已由插件落盘（占位壳 170 B），路径与 kb_path 严格对应，
故按真实路径回绑（**非预期路径，无幽灵锚点风险**）。
幂等：重复运行应报「无改动」。
"""
import json, os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
STATE = '.tools/_ima_sync_state.json'
TARGET = 'ima_sync/个人知识库/WKB/聚合芯能拜访纪要'

s = json.load(open(STATE, encoding='utf-8'))
changed = 0
for mid, it in s['items'].items():
    if it.get('kb_path') != TARGET:
        continue
    rp = 'RAW/' + TARGET + '.md'
    fp = 'RAW_FULL/' + TARGET + '.md'
    if not os.path.exists(rp):
        print('[SKIP] RAW 实文件不存在，拒绝回绑（防幽灵锚点）:', rp)
        break
    if it.get('raw_path') != rp or it.get('full_path') != fp:
        if changed == 0:
            shutil.copy(STATE, STATE + '.bak.20261021-prerebind')
        it['raw_path'] = rp
        it['full_path'] = fp
        it['rebind_source'] = 'real-raw-path-20261021'
        changed += 1
        print('[BIND]', mid, '->', rp)
    else:
        print('[NOOP] 已绑定，无改动:', mid)
    break

if changed:
    json.dump(s, open(STATE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('改动', changed, '条')

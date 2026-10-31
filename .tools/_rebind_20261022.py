# -*- coding: utf-8 -*-
"""2026-10-22 账本回绑：今日 9 条新条目全部 raw_path 为空（插件尚未落盘）。
按 kb_path 推「预期 RAW 路径」绑定 8 条（3 markdown + 5 录音）；截断标题的 note 不绑。
⚠ 预期路径非实文件 → 明日 A 阶段必须复核插件实落名，防幽灵锚点。
幂等：重复运行报「无改动」。
"""
import json, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
STATE = '.tools/_ima_sync_state.json'
MIDS = json.load(open('.tools/_new_mids_20261022.json', encoding='utf-8'))

s = json.load(open(STATE, encoding='utf-8'))
items = s['items']
changed = 0
for mid in MIDS:
    it = items.get(mid)
    if not it:
        continue
    kb = it.get('kb_path') or ''
    title = it.get('title') or ''
    pfx = mid.split('_')[0]
    if pfx == 'note':
        print('[SKIP] note 标题被截断，无法确定落盘名，留空待插件落盘:', title)
        continue
    if not kb:
        print('[SKIP] 无 kb_path:', mid)
        continue
    # RAW 侧落盘名 = kb_path + '.md'（markdown 类标题已带 .md → 双后缀，与历史一致）
    rp = 'RAW/' + kb + '.md'
    fp = 'RAW_FULL/' + kb + '.md'
    if os.path.exists(rp):
        print('[BIND-REAL] RAW 实文件已存在:', rp)
    if it.get('raw_path') == rp:
        print('[NOOP]', title[:30])
        continue
    if changed == 0:
        shutil.copy(STATE, STATE + '.bak.20261022-prerebind')
    it['raw_path'] = rp
    it['full_path'] = fp
    it['rebind_source'] = 'expected-path-20261022-need-verify'
    changed += 1
    print('[BIND]', title[:44], '->', rp)

if changed:
    with open(STATE, 'w', encoding='utf-8') as f:
        json.dump(s, f, ensure_ascii=False, indent=1)
print('改动', changed, '条')

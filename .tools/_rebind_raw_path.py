import json, re
from pathlib import Path

ROOT = Path('.')
STATE = Path('.tools/_ima_sync_state.json')
s = json.loads(STATE.read_text(encoding='utf-8'))
items = s['items']


def fm_media_id(txt):
    m = re.search(r'^media_id:\s*"?([^"\n]+?)"?\s*$', txt, re.M)
    return m.group(1) if m else None


raw_map = {}
for f in (ROOT / 'RAW').rglob('*.md'):
    try:
        txt = f.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue
    mid = fm_media_id(txt)
    if mid:
        raw_map[mid] = str(f).replace('\\', '/')

bound = 0
for mid, it in items.items():
    if not it.get('raw_path') and mid in raw_map:
        it['raw_path'] = raw_map[mid]
        bound += 1

STATE.write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding='utf-8')
print('bound raw_path for', bound, 'items')
for mid, it in items.items():
    if 'NIFO' in (it.get('title') or ''):
        print(' ', it['title'], '->', it['raw_path'])

# -*- coding: utf-8 -*-
"""front matter 补全：按类型补齐必填字段（title:=文件名；缺失字段填待补默认值）。
用法: python .tools/patch_frontmatter.py --apply
"""
import re, glob, os, sys

REQ = {
    'concept': ['type', 'title', 'domain', 'status', 'updated', 'tags'],
    'entity': ['type', 'title', 'category', 'relationship', 'updated', 'tags'],
    'comparison': ['type', 'title', 'subjects', 'dimension', 'updated', 'tags'],
    'source': ['type', 'title', 'source_type', 'source_path', 'date_published',
               'date_processed', 'credibility', 'knowledge_update_status'],
}
DEFAULTS = {
    'domain': '[卫材研发]', 'status': 'seed', 'category': '待核', 'relationship': '待核',
    'subjects': '[待补]', 'dimension': '[待补]', 'tags': '[待补]',
    'source_type': '待核', 'date_published': '[待验证]', 'date_processed': '2026-09-29',
    'credibility': '待核', 'knowledge_update_status': 'done', 'original_link': '""',
    'key_claims': '[待补]', 'pages_linked': '[待补]', 'source_path': '[待补]',
}

def patch(t, fname):
    if not t.startswith('---'):
        return None
    parts = t.split('\n---', 1)
    raw, body = parts[0][3:], parts[1]
    lines = raw.split('\n')
    fm = {}
    for ln in lines:
        m = re.match(r'^([A-Za-z_]+):\s*(.*)$', ln)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    typ = fm.get('type', '')
    if typ not in REQ:
        return None
    changed = False
    if 'title' not in fm or not fm['title']:
        fm['title'] = '"%s"' % fname; changed = True
    for k in REQ[typ]:
        if k not in fm:
            fm[k] = DEFAULTS.get(k, '[待补]'); changed = True
    if not changed:
        return None
    # 保持字段顺序：type, title, 其余按原顺序，新增的放最后
    ordered = ['---']
    seen = set()
    for k in ['type', 'title']:
        if k in fm:
            ordered.append('%s: %s' % (k, fm[k])); seen.add(k)
    for ln in lines:
        m = re.match(r'^([A-Za-z_]+):', ln)
        if m and m.group(1) in fm and m.group(1) not in seen:
            ordered.append('%s: %s' % (m.group(1), fm[m.group(1)])); seen.add(m.group(1))
    for k in fm:
        if k not in seen:
            ordered.append('%s: %s' % (k, fm[k]))
    return '\n'.join(ordered) + '\n---' + body

n = 0
for f in glob.glob('WIKI/**/*.md', recursive=True):
    t = open(f, encoding='utf-8', errors='ignore').read()
    r = patch(t, os.path.basename(f)[:-3])
    if r is not None:
        open(f, 'w', encoding='utf-8').write(r); n += 1
print('补全 %d 页 front matter' % n)

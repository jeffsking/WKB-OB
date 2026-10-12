# -*- coding: utf-8 -*-
"""诊断 remaining.py 判缺失的真实情况：
1) 收集所有 front matter 的 source_path / source_paths（含列表项）
2) 对指定批次缺失项逐一看是否有页命中（含格式变体：引号/反斜杠/尾随空格）
"""
import json, re, glob, sys

# 1) 全量收集 source_path 值（两种键 + 列表项）
vals = {}   # normalized value -> page
pat_single = re.compile(r'source_paths?:\s*(.*)$')
pat_list = re.compile(r'^\s*-\s*(.+)$')
for f in glob.glob('WIKI/sources/*.md'):
    t = open(f, encoding='utf-8', errors='ignore').read()
    fm = t.split('---')[1] if t.startswith('---') else ''
    lines = fm.split('\n')
    cur = None
    for ln in lines:
        m = pat_single.match(ln)
        if m:
            v = m.group(1).strip()
            if v in ('|', '>-', '>', ''):      # 列表块开始
                cur = v; continue
            v2 = v.strip('"\'').strip()
            vals.setdefault(v2, []).append(f.rsplit('/', 1)[-1])
            cur = None
        elif cur is not None:
            m2 = pat_list.match(ln)
            if m2:
                v2 = m2.group(1).strip().strip('"\'').strip()
                vals.setdefault(v2, []).append(f.rsplit('/', 1)[-1])

print('收集到的 source_path(s) 值总数:', len(vals))

# 2) 检查指定批次的缺失项
batches = sys.argv[1:] or ['S2_Areas_IP_01.json']
for b in batches:
    items = json.load(open('.tools/compile_batches/' + b, encoding='utf-8'))['items']
    for it in items:
        src = it['src']
        hit = vals.get(src)
        # 变体：反斜杠、尾随空格、加引号
        alts = [src.replace('/', '\\'), src + ' ', '"' + src + '"']
        alt_hits = [vals.get(a) for a in alts if vals.get(a)]
        status = 'HIT: %s' % hit if hit else ('ALT-HIT: %s' % alt_hits if alt_hits else 'MISS')
        print('  [%s] %s' % (b.replace('.json','').split('_')[-1], status), '<-', src.rsplit('/',1)[-1][:70])

# -*- coding: utf-8 -*-
"""补全回链：对「已有 `## Related Sources` 小节」的概念/实体页，追加其缺失的关联来源。
纯追加（不删原文），幂等，apply 前备份。
用法：python .tools/_link_layer_backfill2_20261012.py [--apply]
"""
import glob, os, re, sys, shutil
from collections import defaultdict

VAULT = 'E:/WKB-OB'
WIKI = os.path.join(VAULT, 'WIKI')
APPLY = '--apply' in sys.argv
BACKUP = os.path.join(VAULT, '.tools', '_link_layer_backup2_20261012')
FM = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)
LINK = re.compile(r'\[\[[ \t]*([^\]\|#]+?)[ \t]*(?:\||#|\]\])')
MAX_TOTAL = 25   # 小节总数上限（确定性封顶 → 幂等）

def read(p): return open(p, encoding='utf-8', errors='ignore').read()
def split(p):
    t = read(p); m = FM.match(t)
    return (m.group(1) if m else ''), (t[m.end():] if m else t)

# 目标集（concept/entity 非 merged）
targets = set()
for d in ('concepts', 'entities'):
    for f in glob.glob(os.path.join(WIKI, d, '*.md')):
        fm, _ = split(f)
        if re.search(r'^status:[ \t]*merged', fm, re.M): continue
        targets.add(os.path.basename(f)[:-3])

# 反向：target -> {sources linking to it}
final_map = defaultdict(set)
for f in glob.glob(os.path.join(WIKI, 'sources', '*.md')):
    n = os.path.basename(f)[:-3]
    _, body = split(f)
    for t in LINK.findall(body):
        tt = t[:-3] if t.endswith('.md') else t
        if tt in targets: final_map[tt].add(n)

plan = {}
for n in targets:
    srcs = final_map.get(n, set())
    if not srcs: continue
    for d in ('concepts', 'entities'):
        p = os.path.join(WIKI, d, n + '.md')
        if not os.path.exists(p): continue
        t = read(p)
        m = re.search(r'^##[ \t]*Related Sources[^\n]*\n', t, re.M)
        if not m:            # 无该小节 → 由首个脚本负责，跳过
            break
        start = m.end()
        nm = re.search(r'^##[ \t]', t[start:], re.M)
        end = start + (nm.start() if nm else len(t[start:]))
        sec = t[start:end]
        existing = set(LINK.findall(sec))   # 原样比对，**不剥 .md**（有页面名本身以 .md 结尾）
        room = max(0, MAX_TOTAL - len(existing))
        missing = sorted(srcs - existing - {n})[:room]
        if missing:
            plan[n] = (p, start, end, missing)
        break

print('需补回链的页:', len(plan), '共新增', sum(len(v[3]) for v in plan.values()), '条')
for n, (p, s, e, miss) in list(plan.items())[:6]:
    print('  %-40s +%d' % (n[:40], len(miss)))

if APPLY:
    os.makedirs(BACKUP, exist_ok=True)
    n_mod = 0
    for n, (p, start, end, miss) in plan.items():
        t = read(p)
        sec = t[start:end]
        add = ''.join('- [[%s]]\n' % x for x in miss) + '\n'   # 末留空行，与后续小节分隔
        if not sec.endswith('\n'): add = '\n' + add
        newt = t[:end] + add + t[end:]
        shutil.copy2(p, os.path.join(BACKUP, os.path.basename(p)))
        open(p, 'w', encoding='utf-8', newline='\n').write(newt)
        n_mod += 1
    print('[APPLY] 改动 %d 页；备份 %s' % (n_mod, BACKUP))
else:
    print('[DRY-RUN] 未写盘')

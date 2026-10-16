# -*- coding: utf-8 -*-
"""知识层语义建链：① 源摘要页补 `## 关联页面`（出链）② 概念/实体页补 `## Related Sources`（回链）。

纪律：只链接「正文中逐字出现」的 concept/entity 标题或别名，绝不臆造；幂等；apply 前备份。
用法：python .tools/_link_layer_build_20261012.py [--apply]
"""
import glob, os, re, sys, json, shutil
from collections import defaultdict

VAULT = 'E:/WKB-OB'
WIKI = os.path.join(VAULT, 'WIKI')
TODAY = '2026-10-12'
APPLY = '--apply' in sys.argv
BACKUP = os.path.join(VAULT, '.tools', '_link_layer_backup_20261012')

FM = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)
LINK = re.compile(r'\[\[[ \t]*([^\]\|#]+?)[ \t]*(?:\||#|\]\])')
BAD = set('[]|#')
MAX_SRC_LINKS = 12
MAX_REL_SOURCES = 15
PRIORITY = {'stable': 0, 'growing': 1, 'seed': 2}

def read(p): return open(p, encoding='utf-8', errors='ignore').read()
def split(p):
    t = read(p); m = FM.match(t)
    return (m.group(1) if m else ''), (t[m.end():] if m else t)
def getlist(fm, key):
    m = re.search(r'^%s:[ \t]*(.+)$' % key, fm, re.M)
    if not m: return []
    return [x.strip().strip('"').strip("'") for x in m.group(1).strip('[]').split(',') if x.strip()]
def is_cjk(s): return any('\u4e00' <= c <= '\u9fff' for c in s)
STOP = {'ltd', 'inc', 'co', 'corp', 'gmbh', 'llc', 'plc', 'sa', 'ag', 'bv', 'nv', 'srl',
        'pte', 'pvt', 'limited', 'company', 'group', 'no', 'etc', 'vs', 'the', 'and'}
PAREN_JUNK = {'待补', '待核', '待定', '待验证', '待确认', '暂缺', '未知', '无', 'n/a', 'na',
              'tbd', 'tba', 'todo', 'other', 'others', '等'}
# 通用合规/标准/泛义缩写（单独作链接目标会全库误命中）
STOP_ACRO = {'reach', 'rohs', 'iso', 'astm', 'en', 'gb', 'fda', 'epa', 'eu', 'us', 'usa', 'uk',
             'cn', 'jp', 'kr', 'oem', 'odm', 'kpi', 'ai', 'it', 'id', 'pdf', 'sop', 'bom',
             'rfq', 'sku', 'po', 'am', 'fm', 'pm', 'no', 'na', 'ok', 'hr', 'qa', 'qc', '环保'}
def ok_cand(s):
    s = s.strip()
    if len(s) < 2 or len(s) == 1: return False
    if len(s) == 2 and not all(is_cjk(c) for c in s): return False
    if len(s) < 3 and not is_cjk(s): return False
    if s.endswith('.'): return False
    if s.lower() in STOP: return False
    if not re.search(r'[0-9A-Za-z\u4e00-\u9fff]', s): return False
    return True

def hit(cand, low):
    """CJK 候选用子串；含拉丁字母的候选必须词边界匹配（防 'cti' 命中 'practice'）。"""
    cl = cand.lower()
    if is_cjk(cand):
        return cl in low
    return re.search(r'(?<![0-9a-z])%s(?![0-9a-z])' % re.escape(cl), low) is not None

# ---------- 1. 目标页（非 merged 的 concept/entity） ----------
targets = {}
for d in ('concepts', 'entities'):
    for f in glob.glob(os.path.join(WIKI, d, '*.md')):
        name = os.path.basename(f)[:-3]
        if BAD & set(name): continue
        fm, _ = split(f)
        if re.search(r'^status:[ \t]*merged', fm, re.M): continue
        st = re.search(r'^status:[ \t]*(\S+)', fm, re.M)
        st = st.group(1) if st else 'growing'
        cands = {name}
        bare = re.sub(r'[（(][^）)]*[）)]', '', name).strip()
        if bare: cands.add(bare)
        for a in getlist(fm, 'aliases'): cands.add(a)
        # 唯一扩展：标题中的全大写缩写（SAP/PET/ADL 等，词边界匹配）；剔除通用合规/标准类缩写
        for ac in re.findall(r'\b[A-Z]{2,6}\b', name):
            if ac.lower() not in STOP_ACRO: cands.add(ac)
        cands = {c for c in cands if ok_cand(c) and c.lower() not in PAREN_JUNK}
        if cands: targets[name] = {'cands': cands, 'status': st}

tmp = defaultdict(list)
for n, info in targets.items():
    for c in info['cands']: tmp[c].append(n)
cand_map = {}; ambiguous = []
for c, ns in tmp.items():
    if len(ns) == 1:
        cand_map[c] = ns[0]
    else:
        pick = sorted(ns, key=lambda n: (PRIORITY.get(targets[n]['status'], 1), len(n)))[0]
        cand_map[c] = pick
        ambiguous.append((c, ns, pick))

# ---------- 2. 源页：正文零出链者补 `## 关联页面` ----------
src_plan = {}      # srcname -> list[target]
final_map = defaultdict(set)   # target -> set(srcname)  反向（含既有）
n_src_total = n_src_nolink = 0
for f in glob.glob(os.path.join(WIKI, 'sources', '*.md')):
    n = os.path.basename(f)[:-3]; n_src_total += 1
    fm, body = split(f)
    existing = set()
    for t in LINK.findall(body):
        tt = t[:-3] if t.endswith('.md') else t
        existing.add(tt)
    for t in existing:
        if t in targets: final_map[t].add(n)
    if existing: continue
    n_src_nolink += 1
    low = body.lower()
    hits = {canon for c, canon in cand_map.items() if hit(c, low)}
    if hits:
        src_plan[n] = sorted(hits)[:MAX_SRC_LINKS]
        for h in src_plan[n]: final_map[h].add(n)

# ---------- 3. 概念/实体页：缺 `## Related Sources` 者补回链 ----------
rel_plan = {}
for n in targets:
    srcs = sorted(final_map.get(n, ()))
    if not srcs: continue
    f = None
    for d in ('concepts', 'entities'):
        p = os.path.join(WIKI, d, n + '.md')
        if os.path.exists(p): f = p; break
    if not f: continue
    _, body = split(f)
    if re.search(r'^#+[ \t]*Related Sources', body, re.M): continue
    rel_plan[n] = srcs[:MAX_REL_SOURCES]

print('目标页(非 merged concept/entity): %d | 别名歧义候选: %d' % (len(targets), len(ambiguous)))
print('源页总数: %d | 正文零出链: %d' % (n_src_total, n_src_nolink))
print('待补 `## 关联页面`: %d 页，共 %d 条链接' % (len(src_plan), sum(len(v) for v in src_plan.values())))
print('待补 `## Related Sources`: %d 页' % len(rel_plan))
print()
if ambiguous:
    print('=== 歧义候选（多页共用同一候选串，已按 status+名字长度选一）===')
    for c, ns, pick in ambiguous[:20]:
        print('  %-40s -> %s' % (c[:40], pick))
    print()

print('=== 抽样（源页 → 命中链接）===')
for n in list(src_plan)[:12]:
    print('  %-42s -> %s' % (n[:42], src_plan[n]))
print()
print('=== 抽样（概念/实体页 → 回链来源数）===')
for n in list(rel_plan)[:8]:
    print('  %-42s <- %d' % (n[:42], len(rel_plan[n])))
print()

# ---------- 4. 写盘 ----------
modified = []
if APPLY:
    os.makedirs(BACKUP, exist_ok=True)
    def backup(path, rel):
        dst = os.path.join(BACKUP, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(path, dst)

for n, hits in src_plan.items():
    f = os.path.join(WIKI, 'sources', n + '.md')
    t = read(f)
    block = '## 关联页面\n\n- ' + '　'.join('[[%s]]' % h for h in hits) + '\n'
    newt = t.rstrip('\n') + '\n\n' + block      # 纯追加，不改动原文任何字符
    if APPLY:
        backup(f, os.path.join('sources', n + '.md'))
        open(f, 'w', encoding='utf-8', newline='\n').write(newt)
    modified.append(os.path.join('sources', n + '.md'))

for n, srcs in rel_plan.items():
    for d in ('concepts', 'entities'):
        f = os.path.join(WIKI, d, n + '.md')
        if not os.path.exists(f): continue
        t = read(f)
        block = '## Related Sources 关联来源\n\n' + '\n'.join('- [[%s]]' % s for s in srcs) + '\n'
        newt = t.rstrip('\n') + '\n\n' + block  # 纯追加
        if APPLY:
            backup(f, os.path.join(d, n + '.md'))
            open(f, 'w', encoding='utf-8', newline='\n').write(newt)
        modified.append(os.path.join(d, n + '.md'))
        break

print('[%s] 改动文件 %d 个' % ('APPLY' if APPLY else 'DRY-RUN', len(modified)))
if APPLY:
    print('备份目录:', BACKUP)
    json.dump({'src_plan': src_plan, 'rel_plan': {k: v for k, v in rel_plan.items()},
               'ambiguous': ambiguous},
              open(os.path.join(VAULT, '.tools', '_link_layer_plan_20261012.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('计划已存: .tools/_link_layer_plan_20261012.json')

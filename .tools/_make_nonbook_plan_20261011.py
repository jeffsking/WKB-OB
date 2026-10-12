# -*- coding: utf-8 -*-
"""只读 v2：非书类 341 条的可执行批次清单（修正切分维度）"""
import os, re, glob, json
import re as _re
from collections import Counter, defaultdict

ROOT = 'E:/WKB-OB'
OUT = os.path.join(ROOT, '.tools', 'compile_plan')
def norm(p): return p.replace('\\', '/')
def read(p):
    try: return open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()
    except OSError: return ''

raw = []
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW')):
    for f in fn:
        if f.endswith('.md'):
            raw.append(norm(os.path.relpath(os.path.join(dp, f), ROOT)))

sp = {}
for p in glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_path:\s*(.+)$', t, re.M)
    if m:
        v = norm(m.group(1).strip().strip('"'))
        if v.lower().startswith('raw/'):
            v = 'RAW/' + v.split('/', 1)[1]
        sp.setdefault(v, []).append(os.path.basename(p))

FULL = {}
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW_FULL')):
    for f in fn:
        if not f.endswith('.md'): continue
        p = norm(os.path.relpath(os.path.join(dp, f), ROOT))
        t = open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()
        m = re.search(r'extract_status:\s*"?(ok|empty|original-only)"?', t)
        FULL[p] = (m.group(1) if m else '(none)', os.path.getsize(os.path.join(ROOT, p)))

def full_of(r): return 'RAW_FULL' + r[len('RAW'):]
def is_attach(r): return '/attachments/' in r
def is_book(r):
    s = r.lower()
    return any(k in s for k in ('/ebook', 'deepbook', 'book extract'))

def stat(r): return FULL.get(full_of(r), ('NO_MIRROR', 0))

cand = [r for r in raw if r not in sp and not is_attach(r) and not is_book(r)]

def zone(r):
    """返回 (一级区, 二级区,三级标签) —— 三级标签仅用于批内分组，不再作为切分维度"""
    m = re.search(r'/WKB/(Areas|Resources)(?:/([^/]+))?(?:/([^/]+))?', r)
    if not m:
        return ('Z_其他', 'IMA笔记区' if '/notes/' in r else 'WKB根级', '')
    return (m.group(1), m.group(2) or '(根)', m.group(3) or '')

def ctype(r):
    b = os.path.basename(r)[:-3].lower()
    ext = b.rsplit('.', 1)[-1] if '.' in b else ''
    s = r.lower()
    if 'minutes' in s or '会议纪要' in b or 'meeting' in s: return '会议纪要'
    if ext == 'pdf': return 'PDF'
    if ext in ('pptx', 'ppt'): return 'PPT'
    if ext in ('xlsx', 'xls', 'csv'): return 'Excel/CSV'
    if ext in ('docx', 'doc'): return 'Word'
    if b.endswith('.jpg') or b.endswith('.png'): return '图片'
    if 'readme' in b or b.endswith('_index'): return '索引件'
    if b.endswith('_report'): return '分析报告'
    if any(k in b for k in ('summary', 'synthesis', 'overview', 'digest')): return '汇总件'
    return '其他'

def score(r):
    a, b, c = zone(r); st, sz = stat(r)
    s = {'ok': 100, 'empty': 55, 'original-only': 55}.get(st, 10)
    s += {'Areas': 40, 'Resources': 20}.get(a, 8)
    if b in ('IP', 'Supply Base', 'Meeting Minutes'): s += 12
    elif b == 'Training': s += 6
    elif b == 'Market Insight': s += 5
    if sz > 400_000: s -= 25
    elif sz < 8000: s -= 8
    return s

rows = []
for r in cand:
    a, b, c = zone(r); st, sz = stat(r)
    rows.append(dict(path=r, z1=a, z2=b, tag=c, ctype=ctype(r), status=st,
                     size=sz, score=score(r), title=os.path.basename(r)[:-3].replace('.md', '')))

rows.sort(key=lambda x: -x['score'])

# ---------- 垃圾件识别（AI 对话残篇 / 无意义占位） ----------
# 教训：规则必须极保守。`_20261007` 这类日期后缀是合法命名（大量报告/索引都带），
# 不可作为垃圾特征；标题短也不代表无意义（「OI 会议纪要」「README」都是有效页）。
# 只命中「明确是模型对话输出」的特征。
JUNK = _re.compile(r'^(我先|让我|首先我|接下来我|这是(一|个)?很|以下是|这个问题问得好)'
                   r'|^关键区别是[：:]'
                   r'|^__(?!一句话)'
                   r'|^Screenshot_\d{4}-\d{2}-\d{2}'
                   r'^\d{10,}$'
                   r'|^会议纪要[一二三四五六七八九十]?$'
                   r'|^(note|笔记)\s*\d*$')

def is_junk(r):
    t = r['title'].strip()
    if JUNK.search(t): return True
    # 纯 AI 续写残句：以冒号+长句且含模型口吻
    if len(t) > 30 and _re.match(r'^(我先|让我)', t): return True
    return False

for r in rows:
    r['junk'] = is_junk(r)
njunk = sum(1 for r in rows if r['junk'])
print(f'  ⚠ 识别为垃圾件（AI 中间产物/空标题/截图占位）: {njunk} 条 → 不进编译批次，单列清单')

# ---------- 优先级 ----------
def tier(s):
    if s >= 140: return 'P0'
    if s >= 100: return 'P1'
    if s >= 55:  return 'P2'
    return 'P3'
for r in rows: r['tier'] = tier(r['score'])

print('=' * 80)
print(f'【非书类未编译件】{len(rows)} 条')
for k, v in Counter(r['status'] for r in rows).most_common():
    print(f'  {k:<16}{v:>6}')
print()
T = defaultdict(list)
for r in rows:
    if not r['junk']: T[r['tier']].append(r)
J = [r for r in rows if r['junk']]
print('【优先级分层】')
LBL = {'P0': 'P0 正文就绪+Areas 业务核心', 'P1': 'P1 正文就绪',
       'P2': 'P2 内容不足需补源(7条)', 'P3': 'P3 无镜像需先回填'}
for k in ['P0', 'P1', 'P2', 'P3']:
    v = T[k]; okc = sum(1 for x in v if x['status'] == 'ok')
    print(f'  {LBL[k]:<32}{len(v):>5} 条（正文就绪 {okc}）')

# ---------- 批次：只按 二级区 切分 ----------
print()
print('=' * 80)
print('【可执行批次（切分维度 = 二级区，避免碎片化）】')
batches = defaultdict(list)
for r in rows:
    if r['tier'] in ('P0', 'P1'):
        batches[(r['tier'], r['z1'], r['z2'])].append(r)

order = sorted(batches.items(), key=lambda x: (x[0][0], -len(x[1])))
print(f"{'批次':<7}{'层':<5}{'一级':<11}{'二级区':<26}{'条数':>5}{'全就绪':>8}")
print('-' * 80)
plan = []
for i, ((t, z1, z2), v) in enumerate(order, 1):
    allok = all(x['status'] == 'ok' for x in v)
    bid = f'{t}-B{i:02d}'
    print(f'{bid:<7}{t:<5}{z1:<11}{z2[:24]:<26}{len(v):>5}{"是" if allok else "否":>8}')
    plan.append((bid, t, z1, z2, sorted(v, key=lambda x: x['path'])))

print()
print(f'  批次总数 {len(plan)}　覆盖 {sum(len(v) for *_, v in plan)} 条'
      f'（= P0 {len(T["P0"])} + P1 {len(T["P1"])} = {len(T["P0"])+len(T["P1"])}）')

# ---------- 导出 ----------
os.makedirs(OUT, exist_ok=True)
json.dump(rows, open(os.path.join(OUT, 'nonbook_backlog.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
for old in glob.glob(os.path.join(OUT, '*.md')): os.remove(old)

for bid, t, z1, z2, v in plan:
    fn = os.path.join(OUT, f'{bid}_{z2[:26].replace(" ", "_").replace("/", "-")}.md')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(f'# {bid} · {z1}/{z2}　（{len(v)} 条）\n\n')
        f.write(f'**优先级**：{t}　**正文就绪**：{sum(1 for x in v if x["status"]=="ok")}/{len(v)}\n\n')
        f.write('## 编译纪律（每条必做）\n\n')
        f.write('- 源摘要页 `WIKI/sources/`，`source_path` 用 `RAW/` 侧相对路径（**不是 RAW_FULL**）\n')
        f.write('- front matter 六字段必填（AGENTS.md §2.0），`credibility` 按源类型取低/中\n')
        f.write('- 商务敏感 / 结论冲突 / 需人工确认 → `knowledge_update_status: manual_review`\n')
        f.write('- 与源摘要页用 `[[wikilink]]` 互链\n')
        f.write(f'- 编译完跑 `python .tools/rebuild_index.py`\n\n')
        f.write('## 清单\n\n')
        f.write('| # | 文件 | 类型 | 大小 | 正文路径 |\n|---|---|---|---|---|\n')
        for j, x in enumerate(v, 1):
            f.write(f'| {j} | {x["title"][:75]} | {x["ctype"]} | {x["size"]//1024}KB | `{full_of(x["path"])}` |\n')
    print('  ->', os.path.basename(fn))

# P2/P3 单独出清单
for t, lbl in [('P2', '内容不足需补源'), ('P3', '无镜像需先回填')]:
    v = T[t]
    if not v: continue
    fn = os.path.join(OUT, f'_{t}_{lbl}_待处理.md')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(f'# {t} · {lbl}（{len(v)} 条）\n\n')
        f.write(f'**状态分布**：')
        for k, c in Counter(x['status'] for x in v).most_common():
            f.write(f'{k} {c}  ')
        f.write('\n\n')
        d = Counter(x['z2'] for x in v)
        f.write('**按二级区**：\n\n')
        for k, c in d.most_common():
            f.write(f'- {k}: {c} 条\n')
        f.write('\n## 清单\n\n| # | 文件 | 状态 | 二级区 |\n|---|---|---|---|\n')
        for j, x in enumerate(sorted(v, key=lambda y: y['path']), 1):
            f.write(f'| {j} | {x["title"][:75]} | {x["status"]} | {x["z2"]} |\n')
    print('  ->', os.path.basename(fn))

# 垃圾件单独出清单
if J:
    fn = os.path.join(OUT, '_X_垃圾件_建议不编译.md')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(f'# 垃圾件 · 建议不编译（{len(J)} 条）\n\n')
        f.write('**识别依据**：标题为 AI 对话中间产物（「我先读取…」「这个问题问得好…」）、'
                '占位式标题（「会议纪要一」）、纯截图名（`Screenshot_*`）、纯数字名（IMA 时间戳图片）、'
                '下划线截断残篇（`__一句话：…`）、无意义后缀（`…_20261007`）。\n\n')
        f.write('**处置建议**：不建 source 页；若已有价值内容应并入对应主题页而非独立成页。'
                '需王总裁定是否全部剔除。\n\n')
        f.write('| # | 文件 | 判定原因 | 目录 |\n|---|---|---|---|\n')
        for j, x in enumerate(sorted(J, key=lambda y: y['path']), 1):
            t = x['title']
            if len(t) < 8: why = '标题过短/无意义'
            elif t.startswith(('我先', '让我', '首先', '接下来', '这是', '以下')): why = 'AI 中间产物'
            elif t.startswith('Screenshot_'): why = '纯截图文件名'
            elif t.startswith('__') or t.startswith('这个问题问得好'): why = '对话残篇/截断'
            elif t.startswith('会议纪要'): why = '占位式标题'
            else: why = '疑似残篇'
            f.write(f'| {j} | {t[:70]} | {why} | `{x["path"].rsplit("/",1)[0][-46:]}` |\n')
    print('  ->', os.path.basename(fn))

# ---------- 计划文档 ----------
fn = os.path.join(OUT, 'PLAN.md')
with open(fn, 'w', encoding='utf-8') as f:
    f.write('# 非书类欠账编译计划（341 条）\n\n生成时间：2026-10-11　源脚本：`.tools/_make_nonbook_plan_20261011.py`（只读）\n\n')
    f.write('## 总量\n\n')
    f.write(f'原始 {len(rows)} 条 − 垃圾件 {len(J)} 条 = **{len(rows)-len(J)} 条待编译**\n\n')
    f.write('| 层级 | 条数 | 正文就绪 | 处置 |\n|---|---:|---:|---|\n')
    f.write(f'| P0 | {len(T["P0"])} | {sum(1 for x in T["P0"] if x["status"]=="ok")} | 立即编译 |\n')
    f.write(f'| P1 | {len(T["P1"])} | {sum(1 for x in T["P1"] if x["status"]=="ok")} | 立即编译 |\n')
    f.write(f'| P2 | {len(T["P2"])} | 0 | 补源或走通道 B 取原件 |\n')
    f.write(f'| P3 | {len(T["P3"])} | 0 | 先回填正文（无镜像） |\n')
    f.write(f'| **合计** | **{len(T["P0"])+len(T["P1"])+len(T["P2"])+len(T["P3"])}** | '
            f'**{sum(1 for x in rows if x["status"]=="ok" and not x["junk"])}** | |\n')
    f.write(f'| 垃圾件 | {len(J)} | — | 不编译，待裁定 |\n\n')
    f.write('## 批次表\n\n')
    f.write('| 批次 | 层 | 一级区 | 二级区 | 条数 | 正文就绪 |\n|---|---|---|---|---:|---|\n')
    for bid, t, z1, z2, v in plan:
        okc = sum(1 for x in v if x['status'] == 'ok')
        f.write(f'| [{bid}]({os.path.basename(fn.replace("PLAN.md", [p for p in os.listdir(OUT) if p.startswith(bid)][0]))}) | {t} | {z1} | {z2} | {len(v)} | {okc}/{len(v)} |\n')
    f.write('\n## 执行顺序建议\n\n')
    f.write('1. **P0 优先**：Areas/IP（专利）、Areas/Meeting Minutes（供应商与内部评审纪要）、Areas/Supply Base（供应商资料）——直接支撑研发决策与供应商管理\n')
    f.write('2. **P1 次之**：Resources/Training（芯体与裤型培训）、Resources/Open Innovation（材料/性能/仿真）\n')
    f.write('3. **P2/P3 挂起**：P2 走通道 B 取原件；P3 先跑正文回填（MCP `fetch_media_content` 优先，不受 200005 配额限制）\n')
    f.write('4. 每批编译完跑 `rebuild_index.py` + 追加 `log.md`，并回写各批次文件的「已编译」列\n')
print('\n计划文档 -> PLAN.md')
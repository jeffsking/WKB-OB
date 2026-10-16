# -*- coding: utf-8 -*-
"""WKB-OB 断链治理常驻工具（wkb_link_guard）

收敛 2026-09 ~ 10 期间三代碎片化断链修复脚本为单一入口。

子命令
------
  check    只读诊断：断链 + front matter 必填字段 + index.md 对齐（均含 MOC）
  plan     断链三级分级（REDIRECT / REVIEW / SEED），产出报表，零改动
  apply    执行改动；--mode=redirect（默认）| seed | all
  report   汇总最近一次 plan / apply 结果

纪律（承 AGENTS §1.1 与 2026-09-30 / 10-11 血泪教训）
-----------------------------------------------
  * 正则一律 [ \t]*，禁 \\s*（防贪婪吞换行）
  * 每子命令首行自证覆盖率，再看结论
  * apply 前自动全量备份受影响页
  * apply 默认只做「改指」；建 seed 页须显式 --mode=seed / all（**seed 默认只出清单**）
  * 改指只允许「同名变体」（curated 白名单命中且目标页已存在）；语义近似一律走 SEED
  * BLOCK 名单强制走 SEED，禁止自动改指（防「上位→下位」窄化）

用法
----
  python .tools/wkb_link_guard.py check
  python .tools/wkb_link_guard.py plan
  python .tools/wkb_link_guard.py apply --mode=redirect
  python .tools/wkb_link_guard.py report
"""
import glob
import json
import os
import re
import shutil
import sys
from collections import defaultdict
from datetime import datetime

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(VAULT, 'WIKI')
TOOLS = os.path.join(VAULT, '.tools')
CURATED_PATH = os.path.join(TOOLS, 'link_guard_curated.json')
REPORTS = os.path.join(TOOLS, 'link_guard_reports')

NOW = datetime.now()
TODAY = NOW.strftime('%Y-%m-%d')
TS = NOW.strftime('%Y%m%d_%H%M%S')

KIND_DIRS = ('sources', 'concepts', 'entities', 'comparisons', 'MOC')

FM_RE = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)
CODE_RE = re.compile(r'`[^`]*`')                 # 行内代码（其中链接不算）
LINK_RE = re.compile(r'\[\[([^\]|#\[]+)')        # 剥 |别名 与 #锚；与 verify_wiki 同口径
MALFORMED_RE = re.compile(r'\[\[\[([^\]|#]+)')

# front matter 必填字段（moc 豁免——AGENTS §1：MOC 不参与 status 治理）
REQ = {
    'source': ['type', 'title', 'source_type', 'source_path', 'date_published',
               'date_processed', 'credibility', 'knowledge_update_status', 'key_claims', 'pages_linked'],
    'concept': ['type', 'title', 'domain', 'status', 'updated', 'tags'],
    'entity': ['type', 'title', 'category', 'relationship', 'updated', 'tags'],
    'comparison': ['type', 'title', 'subjects', 'dimension', 'updated', 'tags'],
}
MOC_TYPES = {'moc'}

UNSAFE = str.maketrans({'/': '／', '\\': '＼', ':': '：', '*': '＊', '?': '？',
                        '"': '”', '<': '＜', '>': '＞', '|': '｜'})
ENTITY_HINT = ['公司', '集团', 'inc', 'ltd', 'llc', 'gmbh', 'corp', 'co.', 'industries',
               'chemical', 'chem', 'solutions', 'technologies', 'materials', 'group',
               'basf', 'henkel', 'arkema', 'evonik', 'dow', 'lg chem', 'snf',
               'glatfelter', 'bostik', 'sumitomo', 'toray', 'supplier', 'vendor']


# ---------------------------------------------------------------- 基础

def read(rel):
    return open(os.path.join(VAULT, rel.replace('/', os.sep)), encoding='utf-8', errors='ignore').read()


def write_abs(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def norm(s):
    """同名变体归一化：去括号内容 + 去空白/标点 + 小写。"""
    s = re.sub(r'[（(][^）)]*[）)]', '', s)
    s = re.sub(r'[ _\-–—×x·、，,。.:：;；"\'“”‘’/]', '', s)
    return s.strip().lower()


def collect_pages():
    """返回 {basename: relpath}（WIKI 全库，含 MOC）。"""
    pages = {}
    for f in glob.glob(os.path.join(WIKI, '**', '*.md'), recursive=True):
        b = os.path.basename(f)[:-3]
        pages[b] = os.path.relpath(f, VAULT).replace('\\', '/')
    return pages


def extract_links(text):
    return {m.group(1).strip() for m in LINK_RE.finditer(CODE_RE.sub('', text)) if m.group(1).strip()}


def load_curated():
    if not os.path.exists(CURATED_PATH):
        raise SystemExit('!! 缺白名单文件 %s（先跑 _build_link_curated_20261012.py）' % CURATED_PATH)
    return json.loads(open(CURATED_PATH, encoding='utf-8').read())


# ---------------------------------------------------------------- check

def cmd_check():
    pages = collect_pages()
    valid = set(pages) | {'index', 'log'}

    # 扫描源 = WIKI 内页 + index.md + log.md
    sources = list(pages.items()) + [('index', 'index.md'), ('log', 'log.md')]
    n_link = 0
    broken = defaultdict(set)
    malformed = defaultdict(set)
    for b, rel in sources:
        text = read(rel)
        links = extract_links(text)
        n_link += len(links)
        for tgt in links:
            if tgt not in valid:
                broken[tgt].add(b)
        for m in MALFORMED_RE.finditer(text):
            malformed[m.group(1).strip()].add(b)

    # 覆盖率自证（AGENTS §1.1.2-2）
    print('=' * 70)
    print('[check] 覆盖率自证')
    print('  扫描页数      : %d（WIKI %d + index/log 2）' % (len(sources), len(pages)))
    print('  提取链接目标  : %d 处（逐页去重后合计）' % n_link)
    print('  合法目标页    : %d 种' % len(valid))
    print('  断链目标      : %d 种（%d 处引用）'
          % (len(broken), sum(len(v) for v in broken.values())))
    print('=' * 70)

    # front matter 校验
    ok, fails = 0, []
    for b, rel in sorted(pages.items()):
        text = read(rel)
        m = FM_RE.match(text)
        if not m:
            fails.append((rel, '无 front matter'))
            continue
        fm = m.group(1)
        tm = re.search(r'^type:[ \t]*(\S+)', fm, re.M)
        if not tm:
            fails.append((rel, '缺 type'))
            continue
        typ = tm.group(1)
        if typ in MOC_TYPES:
            ok += 1                      # MOC 豁免（不参与 status 治理）
            continue
        if typ not in REQ:
            fails.append((rel, 'type 非法: ' + typ))
            continue
        miss = [k for k in REQ[typ] if not re.search(r'^' + k + r':', fm, re.M)]
        if miss:
            fails.append((rel, '缺字段 ' + ','.join(miss)))
        else:
            ok += 1

    # index 对齐
    idx = read('index.md')
    listed = set(re.findall(r'\[\[([^\]|#]+)\]\]', idx)) & set(pages)
    missing_in_index = sorted(set(pages) - listed)

    print('\n[check] front matter 校验: 通过 %d / %d' % (ok, ok + len(fails)))
    kind = defaultdict(int)
    for rel, r in fails:
        kind[r.split(' ')[0] + (' ' + r.split(' ')[1] if len(r.split(' ')) > 1 else '')] += 1
    for k, v in sorted(kind.items(), key=lambda x: -x[1]):
        print('    %-24s %d' % (k, v))
    for rel, r in fails[:15]:
        print('    FAIL %-40s %s' % (r, rel))
    if len(fails) > 15:
        print('    ...（余 %d 条）' % (len(fails) - 15))

    print('\n[check] index.md 对齐: 实际 %d / 收录 %d / 漏收 %d'
          % (len(pages), len(listed), len(missing_in_index)))
    if missing_in_index:
        for x in missing_in_index[:15]:
            print('    漏收:', x)
        if len(missing_in_index) > 15:
            print('    ...（余 %d 条）' % (len(missing_in_index) - 15))

    if malformed:
        print('\n[check] 畸形链接 [[[X]]]: %d 种' % len(malformed))

    # 断链明细（按引用数排序，前 30）
    print('\n[check] 断链目标 Top30（按引用数）')
    for tgt, srcs in sorted(broken.items(), key=lambda kv: -len(kv[1]))[:30]:
        print('    %3dx  %s' % (len(srcs), tgt))
    return broken


# ---------------------------------------------------------------- plan

def classify_seed(name):
    return 'entity' if any(h in name.lower() for h in ENTITY_HINT) else 'concept'


def safe_name(n):
    n = n.translate(UNSAFE).strip().rstrip('. ')
    return n[:120] if len(n) > 120 else n


def cmd_plan():
    pages = collect_pages()
    valid = set(pages) | {'index', 'log'}
    curated = load_curated()
    redirects = curated.get('redirects', {})
    sanitize = curated.get('filename_sanitize', {})
    groups = curated.get('groups', {})
    block = set(curated.get('block', []))

    group_map = {}
    for canon, variants in groups.items():
        for v in variants:
            group_map[v] = canon

    sources = list(pages.items()) + [('index', 'index.md'), ('log', 'log.md')]
    broken = defaultdict(set)
    n_link = 0
    for b, rel in sources:
        links = extract_links(read(rel))
        n_link += len(links)
        for tgt in links:
            if tgt not in valid:
                broken[tgt].add(b)

    print('[plan] 覆盖率自证: 页 %d | 链接 %d 种 | 断链 %d 种'
          % (len(sources), n_link, len(broken)))

    redirect, review, seed = {}, {}, {}
    for tgt, srcs in broken.items():
        ss = sorted(srcs)
        if tgt in block:
            seed[tgt] = ss
            continue
        if tgt in group_map and group_map[tgt] in valid:
            redirect[tgt] = group_map[tgt]
            continue
        if tgt in redirects and redirects[tgt] in valid:
            redirect[tgt] = redirects[tgt]
            continue
        if tgt in sanitize and sanitize[tgt] in valid:
            redirect[tgt] = sanitize[tgt]
            continue
        n = norm(tgt)
        hits = {b for b in valid if b != tgt and norm(b) == n}
        # 括号变体检查：防「去括号归一化」造假唯一
        # （例：X（中文产品册）与 X 产品手册 都归一为 X → 不能自动改指）
        variants = {b for b in valid if b != tgt and norm(b).startswith(n) and norm(b) != n}
        if len(hits) == 1 and not variants and len(n) >= 6:
            redirect[tgt] = next(iter(hits))
            continue
        cands = sorted({b for b in valid
                        if b and abs(len(norm(b)) - len(n)) <= 12
                        and (n in norm(b) or norm(b) in n)})
        if cands and len(n) >= 6:
            review[tgt] = {'candidates': cands[:4], 'cited_by': ss}
            continue
        seed[tgt] = ss

    print('[plan] REDIRECT %d 种 | REVIEW %d 种 | SEED %d 种'
          % (len(redirect), len(review), len(seed)))
    print('        （SEED 仅出清单，不自动建页——纪律：人工裁决后跑 apply --mode=seed）')

    os.makedirs(REPORTS, exist_ok=True)
    payload = {'date': TODAY, 'generated_at': NOW.isoformat(timespec='seconds'),
               'stats': {'redirect': len(redirect), 'review': len(review), 'seed': len(seed)},
               'redirect': redirect, 'review': review, 'seed': seed}
    json.dump(payload, open(os.path.join(REPORTS, '%s_plan.json' % TODAY), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)

    md = ['# 断链分级计划 · %s' % TODAY, '',
          '- REDIRECT %d · REVIEW %d · SEED %d' % (len(redirect), len(review), len(seed)),
          '- 纪律：REDIRECT 只走同名变体白名单；SEED 只出清单，人工裁决后执行', '']
    md += ['## REDIRECT（同名变体，可直接改指）', '']
    for k, v in sorted(redirect.items(), key=lambda kv: -len(broken[kv[0]])):
        md.append('- `%s` → `%s`（%d 处）' % (k, v, len(broken[k])))
    md += ['', '## REVIEW（多候选，须人工裁决）', '']
    for k, v in sorted(review.items(), key=lambda kv: -len(broken[kv[0]])):
        md.append('- `%s`（%d 处）候选：%s' % (k, len(broken[k]), '、'.join(v['candidates'])))
    md += ['', '## SEED（真缺失，待裁决建页）', '']
    for k, v in sorted(seed.items(), key=lambda kv: -len(kv[1])):
        md.append('- `%s`（%d 处）拟建 %s' % (k, len(v), classify_seed(safe_name(k))))
    write_abs(os.path.join(REPORTS, '%s_plan.md' % TODAY), '\n'.join(md) + '\n')
    print('[plan] 报表 -> .tools/link_guard_reports/%s_plan.{json,md}' % TODAY)
    return redirect, review, seed


# ---------------------------------------------------------------- apply

def cmd_apply(mode):
    if mode not in ('redirect', 'seed', 'all'):
        raise SystemExit('!! --mode 只能是 redirect | seed | all')
    plan_path = os.path.join(REPORTS, '%s_plan.json' % TODAY)
    if not os.path.exists(plan_path):
        print('[apply] 无当日 plan，先跑 plan …')
        cmd_plan()
    payload = json.loads(open(plan_path, encoding='utf-8').read())
    redirect = payload['redirect']
    seed = payload['seed']
    pages = collect_pages()
    plain = list(load_curated().get('plain_text', {}).keys())

    stats = {'malformed': 0, 'redirect': 0, 'plain_text': 0, 'seed_pages': [], 'backup': None}

    # 定位需要改动的文件（重扫全库，避免路径歧义）
    all_rels = list(pages.values()) + ['index.md', 'log.md']
    hit_rels = set()
    for rel in all_rels:
        text = read(rel)
        stripped = CODE_RE.sub('', text)
        for old in redirect:
            if ('[[%s]]' % old) in stripped or ('[[%s|' % old) in stripped:
                hit_rels.add(rel)
        for old in plain:
            if ('[[%s]]' % old) in stripped:
                hit_rels.add(rel)
        for m in MALFORMED_RE.finditer(text):
            hit_rels.add(rel)

    if mode in ('redirect', 'all') and hit_rels:
        # 备份
        dst = os.path.join(TOOLS, '_link_guard_backup_%s' % TS)
        for rel in sorted(hit_rels):
            p = os.path.join(dst, rel.replace('/', os.sep))
            os.makedirs(os.path.dirname(p), exist_ok=True)
            shutil.copy2(os.path.join(VAULT, rel.replace('/', os.sep)), p)
        stats['backup'] = os.path.relpath(dst, VAULT).replace('\\', '/')
        print('[apply] 备份 %d 文件 -> %s' % (len(hit_rels), stats['backup']))

        for rel in sorted(hit_rels):
            p = os.path.join(VAULT, rel.replace('/', os.sep))
            t0 = open(p, encoding='utf-8', errors='ignore').read()
            t = t0
            # 畸形 [[[X]]] -> [[X]]
            for m in set(MALFORMED_RE.findall(t)):
                if '[[[%s]]]' % m in t:
                    t = t.replace('[[[%s]]]' % m, '[[%s]]' % m)
                    stats['malformed'] += 1
            # 改指
            for old, new in redirect.items():
                if '[[%s]]' % old in t or '[[%s|' % old in t:
                    t = t.replace('[[%s]]' % old, '[[%s]]' % new)
                    t = t.replace('[[%s|' % old, '[[%s|' % new)
                    stats['redirect'] += 1
            # 占位符 → 纯文本（去掉链接标记）
            for old in plain:
                if '[[%s]]' % old in t:
                    t = t.replace('[[%s]]' % old, old)
                    stats['plain_text'] += 1
            if t != t0:
                open(p, 'w', encoding='utf-8', newline='\n').write(t)

    # seed 建页（仅显式 mode=seed/all）
    if mode in ('seed', 'all'):
        for tgt, cited in seed.items():
            typ = classify_seed(tgt)
            fn = safe_name(tgt)
            if not fn:
                continue
            d = 'entities' if typ == 'entity' else 'concepts'
            path = os.path.join(WIKI, d, fn + '.md')
            if os.path.exists(path):
                continue
            uniq = sorted(set(cited))
            shown = uniq[:12]
            if typ == 'entity':
                fm = ('---\ntype: entity\ntitle: "%s"\ncategory: 待补\n'
                      'relationship: 待核\nupdated: %s\ntags: [seed, 待补]\n---\n' % (fn, TODAY))
            else:
                fm = ('---\ntype: concept\ntitle: "%s"\ndomain: [卫材研发, 待归类]\nstatus: seed\n'
                      'updated: %s\ntags: [seed, 待补]\n---\n' % (fn, TODAY))
            body = [fm, '\n# %s\n' % fn,
                    '\n> ⏳ **Seed page（%s）**：断链治理按引用反查补建的占位页 —— %d 处引用指向本标题但页面不存在。'
                    '**仅登记引用来源与待补维度，未填任何数据**；补内容须回来源页核对原文，禁止编造。\n'
                    % (TODAY, len(uniq)),
                    '\n## Cited by 主要引用来源（%d 处%s）\n\n' % (len(uniq), '' if len(uniq) <= 12 else '，取前 12')]
            body += ['- [[%s]]\n' % c for c in shown]
            body.append('\n## Pending 待补维度\n\n')
            if typ == 'entity':
                body.append('- 公司全称 / 国别 / 主营产品\n- 与金佰利的既有关系（供应商 / 竞品 / 合作方）\n')
            else:
                body.append('- 定义 / 口径 / 关键参数\n- 与卫材（REL 芯体 / SAP / 无纺布 / 胶黏）的关联点\n')
            write_abs(path, ''.join(body))
            stats['seed_pages'].append('%s/%s.md' % (d, fn))

    stats['mode'] = mode
    stats['date'] = TODAY
    os.makedirs(REPORTS, exist_ok=True)
    json.dump(stats, open(os.path.join(REPORTS, '%s_apply.json' % TODAY), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)
    print('[apply] mode=%s | 畸形修复 %d | 改指 %d 处 | 占位符转文本 %d | seed 新建 %d'
          % (mode, stats['malformed'], stats['redirect'], stats['plain_text'], len(stats['seed_pages'])))
    if mode == 'redirect':
        print('        （默认不改指建页；如需建 seed 请显式 --mode=seed 或 --mode=all）')
    print('[apply] 结果 -> .tools/link_guard_reports/%s_apply.json' % TODAY)
    return stats


# ---------------------------------------------------------------- report

def cmd_report():
    plan_path = os.path.join(REPORTS, '%s_plan.json' % TODAY)
    apply_path = os.path.join(REPORTS, '%s_apply.json' % TODAY)
    if not os.path.exists(plan_path):
        print('[report] 无当日 plan，先跑 plan …')
        cmd_plan()
    plan = json.loads(open(plan_path, encoding='utf-8').read())
    lines = ['# 断链治理日报 · %s' % TODAY, '',
             '- plan: REDIRECT %d / REVIEW %d / SEED %d'
             % (plan['stats']['redirect'], plan['stats']['review'], plan['stats']['seed'])]
    if os.path.exists(apply_path):
        ap = json.loads(open(apply_path, encoding='utf-8').read())
        lines.append('- apply: mode=%s 畸形 %d / 改指 %d / seed %d'
                     % (ap.get('mode'), ap['malformed'], ap['redirect'], len(ap['seed_pages'])))
        if ap.get('backup'):
            lines.append('- 备份: `%s`' % ap['backup'])
    else:
        lines.append('- apply: 未执行')
    write_abs(os.path.join(REPORTS, '%s_report.md' % TODAY), '\n'.join(lines) + '\n')
    print('\n'.join(lines))
    print('\n[report] -> .tools/link_guard_reports/%s_report.md' % TODAY)


# ---------------------------------------------------------------- main

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('check', 'plan', 'apply', 'report'):
        print(__doc__)
        raise SystemExit(1)
    cmd = sys.argv[1]
    if cmd == 'check':
        cmd_check()
    elif cmd == 'plan':
        cmd_plan()
    elif cmd == 'apply':
        mode = 'redirect'
        for a in sys.argv[2:]:
            if a.startswith('--mode='):
                mode = a.split('=', 1)[1]
        cmd_apply(mode)
    else:
        cmd_report()


if __name__ == '__main__':
    main()

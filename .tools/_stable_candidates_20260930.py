# -*- coding: utf-8 -*-
"""growing → stable 晋升候选审计（2026-09-30 Reconciliation 第一步 #4，只读）。

依 AGENTS §2.1 stable 判据（2026-09-30 版）做**只读**扫描，产出候选清单。
不修改任何页面 status —— 晋升须人工确认（AGENTS 明确 AI 不得自动晋升）。

判据实现（近似）：
  A 来源支撑  : 相关来源页 ≥2 个独立来源；或仅 1 个来源但该 source 页
                credibility ∈ {高, A, internal-expert}
  B 无未决矛盾: 正文无「⚠️ 矛盾记录」标记
  C 无未决缺口: 正文无 `[待验证]` / `待补` / `定义待补` 标记
  D 三要素齐备: 含 Definition / Key Parameters（或对比维度表）/ Related Sources

输出：.tools/_stable_candidates_20260930.json + 控制台摘要
用法：python .tools/_stable_candidates_20260930.py
"""
import glob
import json
import os
import re

VAULT = r'E:\WKB-OB'
HIGH_CRED = {'高', 'A', 'internal-expert'}


def front_matter(t):
    fm = {}
    if not t.startswith('---'):
        return fm
    parts = t.split('---')
    if len(parts) < 3:
        return fm
    for line in parts[1].split('\n'):
        m = re.match(r'^([A-Za-z_]+):\s*(.*)$', line.strip())
        if m and m.group(2):
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm


def source_credibility(page_title):
    """查 source 页 credibility。title 形如 '[[X]]' 或 'X'。"""
    name = page_title.strip().strip('[]')
    fp = os.path.join(VAULT, 'WIKI', 'sources', name if name.endswith('.md') else name + '.md')
    if not os.path.exists(fp):
        for cand in glob.glob(os.path.join(VAULT, 'WIKI', 'sources', '*.md')):
            if os.path.basename(cand).startswith(name[:40]):
                fp = cand
                break
    try:
        t = open(fp, encoding='utf-8', errors='ignore').read(3000)
        m = re.search(r'^credibility:\s*(.+)$', t, re.M)
        return m.group(1).strip().strip('"') if m else ''
    except Exception:
        return ''


def audit(f, t, fm):
    body = t.split('---', 2)[-1] if t.startswith('---') else t
    # 来源页识别：正文全部 wikilink 反查 WIKI/sources/ 落盘文件（兼容新旧版式）
    links = {x.strip() for x in re.findall(r'\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]', body)}
    src_links = set()
    for l in links:
        l2 = l[:-3] if l.endswith('.md') else l
        if os.path.exists(os.path.join(VAULT, 'WIKI', 'sources', l2 + '.md')):
            src_links.add(l2)
    reasons, ok = [], True

    # A 来源支撑
    n_src = len(src_links)
    single_high = False
    if n_src == 1:
        cred = source_credibility(next(iter(src_links)))
        single_high = cred in HIGH_CRED
        if not single_high:
            ok = False
            reasons.append('仅 1 个来源且可信度不足（%s）' % (cred or '未标注'))
    elif n_src == 0:
        ok = False
        reasons.append('无可识别来源链接')
    # B 矛盾
    if '⚠️' in body and '矛盾' in body:
        ok = False
        reasons.append('存在未决矛盾记录')
    # C 缺口标记
    gaps = re.findall(r'\[待验证\]|待补|定义待补|待人工', body)
    if gaps:
        ok = False
        reasons.append('存在 %d 处待补/待验证标记' % len(gaps))
    # D 三要素（兼容英文/中文版式）
    has_def = bool(re.search(r'Definition|定义', body, re.I))
    has_param = bool(re.search(r'Key Parameters|关键参数|对比维度|Parameter', body, re.I))
    has_src_sec = bool(re.search(r'Related Sources|关联来源|来源', body, re.I))
    if not (has_def and has_param and has_src_sec):
        ok = False
        reasons.append('三要素缺项（def=%s param=%s src=%s）' % (has_def, has_param, has_src_sec))
    return {'page': os.path.basename(f), 'n_sources': n_src, 'candidate': ok,
            'reasons': reasons}


def main():
    os.chdir(VAULT)
    results = []
    for f in glob.glob('WIKI/concepts/*.md') + glob.glob('WIKI/entities/*.md') \
            + glob.glob('WIKI/comparisons/*.md'):
        t = open(f, encoding='utf-8', errors='ignore').read()
        fm = front_matter(t)
        if fm.get('status') != 'growing':
            continue
        r = audit(f, t, fm)
        r['type'] = fm.get('type', '?')
        results.append(r)

    cand = [r for r in results if r['candidate']]
    by_type = {}
    for r in cand:
        by_type[r['type']] = by_type.get(r['type'], 0) + 1
    print('growing 页总数        : %d' % len(results))
    print('stable 候选（满足判据）: %d  %s' % (len(cand), by_type))
    print('不满足（top 缺因）:')
    from collections import Counter
    cnt = Counter(r['reasons'][0].split('（')[0] for r in results if not r['candidate'])
    for k, v in cnt.most_common(6):
        print('   %4d  %s' % (v, k))
    json.dump({'generated': '2026-09-30', 'criteria': 'AGENTS §2.1（2026-09-30 版）',
               'n_growing': len(results), 'n_candidates': len(cand), 'candidates': cand},
              open('.tools/_stable_candidates_20260930.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('候选清单 → .tools/_stable_candidates_20260930.json（只读产物，晋升须人工确认）')


if __name__ == '__main__':
    main()

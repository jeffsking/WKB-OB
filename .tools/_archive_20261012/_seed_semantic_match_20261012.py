# -*- coding: utf-8 -*-
"""concept 语义档案 + SEED 语义匹配（2026-10-12）。

**方法论纠正**：判断「是否需建新 concept」必须基于**库内 concept 的定义内容**，
不能只看页名相似度。本脚本：
  1) 遍历 WIKI/concepts/*.md，提取 title + domain + status + 定义首句 → 语义档案
  2) 对给定 SEED 目标，用「核心词命中 title/定义」+「title 相似度」双路匹配，输出候选

只读。产物：
  .tools/_concept_index_20261012.json   语义档案
  .tools/_seed_match_20261012.txt       匹配结果（供人工裁定）
"""
import difflib
import glob
import json
import os
import re
import sys

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONC = os.path.join(VAULT, 'WIKI', 'concepts')
ENTS = os.path.join(VAULT, 'WIKI', 'entities')
FM_RE = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)


def strip_links(s):
    s = re.sub(r'\[\[([^\]|]+)(\|[^\]]+)?\]\]', r'\1', s)
    return re.sub(r'[*`]', '', s)


def extract_defn(body, n=140):
    for line in body.split('\n'):
        s = line.strip()
        if not s or s[0] in '#>|-*=':
            continue
        s = strip_links(s)
        if len(s) < 8:
            continue
        return s[:n]
    return ''


def fv(fm, key):
    m = re.search(r'^%s:[ \t]*(.*)$' % key, fm, re.M)
    return m.group(1).strip().strip('"') if m else ''


def norm(s):
    s = re.sub(r'[（(][^）)]*[）)]', '', s)
    s = re.sub(r'[ _\-–—×x·、，,。.:：;；"\'“”‘’/]', '', s)
    return s.strip().lower()


def core_terms(s):
    cn = re.findall(r'[\u4e00-\u9fa5]{2,}', s)
    en = re.findall(r'[A-Za-z][A-Za-z0-9\-]{1,}', s)
    return [x for x in cn + en if len(x) >= 2]


def build_index():
    idx = {}
    for f in glob.glob(os.path.join(CONC, '*.md')) + glob.glob(os.path.join(ENTS, '*.md')):
        name = os.path.basename(f)[:-3]
        t = open(f, encoding='utf-8', errors='ignore').read()
        m = FM_RE.match(t)
        fm = m.group(1) if m else ''
        body = t[m.end():] if m else t
        idx[name] = {'dir': 'concepts' if f.startswith(CONC) else 'entities',
                     'title': fv(fm, 'title') or name,
                     'domain': fv(fm, 'domain') or fv(fm, 'category'),
                     'status': fv(fm, 'status') or fv(fm, 'relationship'),
                     'defn': extract_defn(body)}
    return idx


def match(seed, idx):
    n = norm(seed)
    terms = core_terms(seed)
    out = []
    for name, c in idx.items():
        hay = (c['title'] or '') + ' ' + (c['defn'] or '')
        hit = sum(1 for x in terms if x and x.lower() in hay.lower())
        tn = norm(c['title'] or name)
        r = difflib.SequenceMatcher(None, n, tn).ratio()
        score = hit * 1.0 + r * 2.0
        if hit or r > 0.5:
            out.append((score, hit, r, name, c['defn'][:80]))
    out.sort(key=lambda x: -x[0])
    return out[:6]


def main():
    idx = build_index()
    json.dump(idx, open(os.path.join(VAULT, '.tools', '_concept_index_20261012.json'), 'w',
                        encoding='utf-8'), ensure_ascii=False, indent=1)
    print('语义档案: %d 页（concepts %d / entities %d）'
          % (len(idx),
             sum(1 for v in idx.values() if v['dir'] == 'concepts'),
             sum(1 for v in idx.values() if v['dir'] == 'entities')))

    d = json.load(open(os.path.join(VAULT, '.tools', 'link_guard_reports', '2026-10-12_plan.json'),
                       encoding='utf-8'))
    seed = d['seed']
    todo = sorted(seed, key=lambda k: -len(seed[k]))
    print('待裁定 SEED: %d 条\n' % len(todo))

    lines = []
    for i, s in enumerate(todo, 1):
        cands = match(s, idx)
        lines.append('=' * 78)
        lines.append('%d. ■ %s  (%d处)  引用自: %s'
                     % (i, s, len(seed[s]), '、'.join(sorted(seed[s])[:2])))
        for sc, h, r, name, dd in cands:
            lines.append('     [命中%d 相似%.2f] %s' % (h, r, name))
            if dd:
                lines.append('            %s' % dd)
        if not cands:
            lines.append('     (无候选)')
    open(os.path.join(VAULT, '.tools', '_seed_match_20261012.txt'), 'w',
         encoding='utf-8').write('\n'.join(lines) + '\n')
    print('匹配结果 -> .tools/_seed_match_20261012.txt')


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""为 seed 页抽取「来源素材」（2026-10-12）。

对每个 status: seed 的 concept/entity 页：
  ① 找出全库中引用它的页面
  ② 在这些引用页里，抽取**含该概念关键词**的段落（±1 段上下文）
  ③ 汇总输出，作为补内容的唯一依据（禁止编造）

只读。产物：.tools/_seed_fill_material_20261012.txt
"""
import glob
import os
import re

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(VAULT, 'WIKI')
FM_RE = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)


def read(p):
    return open(p, encoding='utf-8', errors='ignore').read()


def para_hits(text, terms, limit=4):
    """返回含 terms 任一者的段落（含前一段作上下文）。"""
    paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    out, n = [], 0
    for i, p in enumerate(paras):
        if p.startswith('>') or p.startswith('---'):
            continue
        if any(t and t in p for t in terms):
            ctx = paras[i - 1] if i > 0 and not paras[i - 1].startswith('>') else ''
            body = (ctx + ' ' if ctx else '') + p
            out.append(re.sub(r'\s+', ' ', body)[:400])
            n += 1
            if n >= limit:
                break
    return out


def main():
    # 引用者主要是 sources/（源摘要页）；必须全库扫描
    files = []
    for d in ('concepts', 'entities', 'sources', 'comparisons'):
        files += glob.glob(os.path.join(WIKI, d, '*.md'))
    cache = {os.path.basename(f)[:-3]: read(f) for f in files}

    seeds = []
    for n, t in cache.items():
        m = FM_RE.match(t)
        if m and re.search(r'^status:[ \t]*seed', m.group(1), re.M):
            seeds.append(n)

    lines = []
    for s in sorted(seeds):
        # 关键词：整名 + 中文/英文核心词
        terms = [s]
        terms += re.findall(r'[\u4e00-\u9fa5]{2,}', s)
        terms += [x for x in re.findall(r'[A-Za-z][A-Za-z0-9\-]{2,}', s) if x.lower() not in ('the',)]
        citers = [n for n, t in cache.items()
                  if n != s and ('[[%s]]' % s in t or '[[%s|' % s in t)]
        lines.append('=' * 90)
        lines.append('■ %s   （被 %d 页引用：%s）' % (s, len(citers), '、'.join(citers[:4])))
        got = 0
        for c in citers[:4]:
            for h in para_hits(cache[c], terms, limit=2):
                lines.append('   [%s] %s' % (c, h))
                got += 1
        if not got:
            lines.append('   （引用页无该概念的直接描述——需溯源到 source 页）')
    open(os.path.join(VAULT, '.tools', '_seed_fill_material_20261012.txt'), 'w',
         encoding='utf-8').write('\n'.join(lines) + '\n')
    print('seed 页:', len(seeds))
    print('素材 -> .tools/_seed_fill_material_20261012.txt')


if __name__ == '__main__':
    main()

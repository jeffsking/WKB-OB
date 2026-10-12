# -*- coding: utf-8 -*-
"""修正 P0-B01 生成页的 date_published 口径"""
import os, re, glob

ROOT = 'E:/WKB-OB'
SRC = os.path.join(ROOT, 'WIKI', 'sources')

# 已知真实会议日期（从原文正文提取）；其余原文未记日期
KNOWN = {
 'OI（Open Innovation）团队会议纪要.md': ('2026-09-18', '原文正文「会议时间：2026年9月18日（周五）」'),
 'TJ 供应商工厂访问与会谈纪要（英文）.md': ('2026-09', '原文记「Meeting Date: September 2026」，未精确到日'),
}

n_fix = 0
n_no = 0
for p in glob.glob(os.path.join(SRC, '*.md')):
    b = os.path.basename(p)
    if not re.search(r'2026-10-11', open(p, encoding='utf-8').read()[:600]):
        continue
    # 只处理本批 26 页（date_processed 为今天且 source_type 会议纪要）
    t = open(p, encoding='utf-8').read()
    if 'date_processed: 2026-10-11' not in t: continue
    if 'source_type: 会议纪要' not in t: continue
    if 'date_published: 2026-10-11' not in t: continue

    if b in KNOWN:
        d, how = KNOWN[b]
    else:
        d, how = '', '原文未记载会议日期；RAW_FULL 的 extracted 字段是正文回填日期（2026-09-30），非会议日期'
        n_no += 1

    if d:
        t2 = t.replace('date_published: 2026-10-11', f'date_published: "{d}"', 1)
        # 加口径注记
        t2 = t2.replace(f'credibility: ', f'# date_published 口径：{how}\ncredibility: ', 1)
        n_fix += 1
    else:
        # 留空并在 front matter 注明
        t2 = t.replace('date_published: 2026-10-11',
                       f'date_published: ""  # 原文未记载会议日期', 1)
        n_fix += 1
    open(p, 'w', encoding='utf-8').write(t2)

print(f'修正 {n_fix} 页（有明确日期 {n_fix-n_no} 页，留空并注明 {n_no} 页）')
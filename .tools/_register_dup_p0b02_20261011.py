# -*- coding: utf-8 -*-
"""为已编译页补登同专利/同源副本的 source_paths（追加式，不改动既有结论）。
同时在已编译页正文末尾追加"同源副本说明"段。仅追加，不覆盖。"""
import os, io, sys, re
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

JOBS = [
 # (page, 要补登的 RAW 相对路径列表, 说明文本)
 ('WIKI/sources/CN 101679760 B（包覆吸水性聚合物颗粒的方法·BASF）.md',
  ['RAW/ima_sync/个人知识库/WKB/Areas/IP/09_包覆吸水性聚合物颗粒的方法 (EDANA ERT 完整引用).pdf.md',
   'RAW/ima_sync/个人知识库/WKB/Areas/IP/10_Method for coating SAP particles (with EDANA ERT citations).pdf.md',
   'RAW/ima_sync/个人知识库/WKB/Areas/IP/v3非传统资源_②OEM测试协议_9_Nippon_Shokubai_CN_101679760_B___EDANA_测试方法引用清单.pdf.md'],
  'CN 101679760 B（BASF，包覆吸水性聚合物颗粒的方法）在 IMA 内共 3 份不同命名的副本，均已并入本页：\n\n'
  '| 副本 | 命名差异 | 正文 |\n|---|---|---|\n'
  '| `CN101679760B.pdf` | 主副本（`source_path` 主值） | 19,246 字符基准 |\n'
  '| `09_包覆吸水性聚合物颗粒的方法 (EDANA ERT 完整引用).pdf` | EDANA ERT 完整引用标注版 | 19,246 字符 |\n'
  '| `10_Method for coating SAP particles (with EDANA ERT citations).pdf` | 英文引用标注版 | 19,276 字符 |\n'
  '| `v3非传统资源_②OEM测试协议_9_Nippon_Shokubai_CN_101679760_B___EDANA_测试方法引用清单.pdf` | 日本触宝 OEM 测试协议版 | 19,287 字符 |\n\n'
  '四份正文的专利公开号（CN101679760 出现 15 次）与引用专利（EP0640330A1、CN1589304）完全一致，'
  '**属同一专利的重复标注副本，非不同技术方案**。差异仅在引文标注粒度，故合并为单页，不重复建页。'),

 ('WIKI/sources/CN 101641398 B（包覆吸水性聚合物颗粒的方法·BASF）.md',
  [],
  'CN 101641398 B 与 [[CN 101679760 B（包覆吸水性聚合物颗粒的方法·BASF）]] 是**同族但不同专利**'
  '（同为巴斯夫欧洲公司、同一优先权日 2007-03-19、同日申请 2008-03-17、同属 PCT/EP2008 批次），'
  '**不可合并**：CN101679760 B 对应 PCT/EP2008/053169 → WO2008/113788；'
  'CN101641398 B 对应 PCT/EP2008/053172 → WO2008/113790。IMA 内另有独立副本 '
  '`10_包覆吸水性聚合物颗粒的方法（含 SFC 详细计算）.pdf`，已登记于本页 `source_paths`。'),

 ('WIKI/sources/WO2010071584A1 & US9162007 SAP-Cellulosic Nanofibril Composite (SCA).md',
  ['RAW/ima_sync/个人知识库/WKB/Areas/IP/CN102245218B.pdf.md',
   'RAW/ima_sync/个人知识库/WKB/Areas/IP/JP5604444B2.pdf.md',
   'RAW/ima_sync/个人知识库/WKB/Areas/IP/US9162007 (1).pdf.md',
   'RAW/ima_sync/个人知识库/WKB/Areas/IP/US9162007.pdf.md'],
  '**同族与同源副本登记（2026-10-11 P0-B02 补充）**\n\n'
  '| RAW 条目 | 关系 | 归并理由 |\n|---|---|---|\n'
  '| `WO2010071584A1.pdf` | 主副本（`source_path` 主值） | WO/PCT 公开 |\n'
  '| `CN102245218B.pdf` | CN 国家阶段授权 | 同一发明（W02010/071584 → CN102245218 B），SCA 卫生用品公司 |\n'
  '| `JP5604444B2.pdf` | JP 国家阶段 | 同一发明族日本授权 |\n'
  '| `US9162007.pdf` | US 371 国家阶段授权 | PCT/SE2009/051446 → US 9,162,007 B2（2015-10-20） |\n'
  '| `US9162007 (1).pdf` | 同上，另一 IMA 副本 | 正文 90,218 字符，与上件相似度 0.9996，仅 `media_id` 不同（`63a8b2303e` / `d7cf3bafdc`），**内容实质相同** |\n\n'
  '**US9162007 两份的 diff 结论**：两份正文长度完全相同（90,218 字符），`difflib.SequenceMatcher` 全文档相似度 **0.9996**，'
  '首个差异出现在第 1 行且仅为 front matter 的 `media_id` 值不同（同一 PDF 被IMA 存为两个 media_id）。'
  '→ **判为重复件，不单独建页。**\n\n'
  '参见 [[BNC 基 SAP 表面交联]]（CN102245218 B 的中文技术要点页）。'),

 ('WIKI/sources/US5266394A Disposable Articles Containing SIS Block Copolymers (Dow).md',
  [],
  '**同专利不同 IMA 副本（2026-10-11 P0-B02 补充）**\n\n'
  'IMA 内 US 5,266,394 A 共2 份不同命名的副本：\n\n'
  '| 副本 | 正文长度 | sha1(正文) |\n|---|---|---|\n'
  '| `16_模块三：..._US5266394A_..._(block_co.pdf` | 5,860 字符 | `a0a1823aa8` |\n'
  '| `16_模块三：..._US5266394A_..._(嵌段共聚物).pdf` | 5,860 字符 | 同上 |\n\n'
  '两件正文长度与指纹一致，**属同一识读结果的重复命名**，已另行整理为 '
  '[[US 5266394 A SIS 嵌段共聚物热熔胶（Dow 与 Exxon·多线贴合用）]]（该页另含完整的实施例配比与测试方法表）。'
  '两页 source_path 不同，按库纪律分别登记、互链，**内容不合并**。'),

 ('WIKI/sources/盛色科技官网关于我们（BLOCLO 温变与光变材料）.md',
  [],
  '**同源非 PDF 副本（2026-10-11 P0-B03 补充）**\n\n'
  'IMA 内 BLOCLO 盛色科技资料共 2 份：\n\n'
  '| 条目 | 形态 | 已编译页 |\n|---|---|---|\n'
  '| `关于我们_盛色科技.html` | 官网「关于我们」 | 本页 |\n'
  '| `BLOCLO盛色科技公司及产品介绍.pdf` | 公司产品册 PDF | [[BLOCLO 盛色科技（广州盛色）光变与温变动态色彩材料产品册]] |\n\n'
  '两件为**同一公司的不同物料**（官网简介 vs 产品册），非重复件，按库纪律分别编译、互链，不合并。'),
]

for page, extras, note in JOBS:
    if not os.path.exists(page):
        print('MISSING PAGE:', page); continue
    t = io.open(page, encoding='utf-8').read()
    changed = []
    # 1) 补 source_paths
    for e in extras:
        if e in t:
            continue
        m = re.search(r'^source_paths:[ \t]*\n((?:[ \t]*-[ \t]*.+\n?)+)', t, re.M)
        if m:
            block = m.group(1)
            t = t[:m.start(1)] + block + f'  - {e}\n' + t[m.end(1):]
        else:
            m2 = re.search(r'^source_path:[ \t]*(.+)\n', t, re.M)
            t = t[:m2.end()] + 'source_paths:\n  - ' + m2.group(1) + f'\n  - {e}\n' + t[m2.end():]
        changed.append('source_paths+' + e.split('/')[-1][:40])
    # 2) 追加说明段
    if '同源副本登记（2026-10-11' not in t and '同族与同源副本登记' not in t and note:
        t = t.rstrip('\n') + '\n\n## 同源副本与同族登记\n\n' + note + '\n'
        changed.append('note')
    if changed:
        io.open(page, 'w', encoding='utf-8', newline='\n').write(t)
        print('UPDATED:', os.path.basename(page), '->', changed)
    else:
        print('NO CHANGE:', os.path.basename(page))
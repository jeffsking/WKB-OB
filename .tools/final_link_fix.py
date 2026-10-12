# -*- coding: utf-8 -*-
"""断链终修：① 别名/近名改指 ② 占位符清理 ③ 高频缺失目标补 seed 页（不编造数据）。
用法: python .tools/final_link_fix.py --apply
"""
import re, glob, os, sys, collections

WIKI = 'WIKI'
LINK = re.compile(r'\[\[([^\]\|#]+)(?:[|#][^\]]*)?\]\]')
pages = glob.glob(WIKI + '/**/*.md', recursive=True)
basenames = {os.path.basename(f)[:-3] for f in pages}

REWRITE = {
    '化妆品限用/准用组分体系（中国 2015 技术规范）': '化妆品限用-准用组分体系（中国 2015 技术规范）',
    '温变湿变微胶囊（Thermochromic/Hydrochromic Microcapsules）': '温变湿变微胶囊（Thermochromic_Hydrochromic Microcapsules）',
    '抗菌整理定量测试（AATCC TM100 / AATCC 100）': '抗菌整理定量测试（AATCC TM100 _ AATCC 100）',
    'GB/T 36420-2018（生活用纸化学品安全评价体系）': 'GB-T 36420-2018（生活用纸化学品安全评价体系）',
    'EDANA AHPs Dossier (2022 V2.0) — CODEX™ 痕量物质与 Stewardship Program': 'EDANA AHPs Dossier (2022 V2.0) — CODEX 痕量物质与 Stewardship Program',
    'SCCS Final Opinion on Phenoxyethanol in Cosmetic Products (SCCS/1575/16, 2016)': 'SCCS Final Opinion on Phenoxyethanol in Cosmetic Products (SCCS-1575-16, 2016)',
    '功能性纤维产品简介（PTT/超仿棉/咖啡炭/纳米凉感）': '功能性纤维产品简介（PTT_超仿棉_咖啡炭_纳米凉感）',
    '功能性差别化纤维（PTT/超仿棉/纳米凉感）': '功能性差别化纤维（PTT_超仿棉_纳米凉感）',
    'LG Chem SAPPYER SAP（Chinaplas Acrylates/SAP）': 'LG Chem SAPPYER SAP（Chinaplas Acrylates_SAP）',
    'SAPPYER® SLI/SLIM/SLIE + Bio-balanced SAP（LG Chem）': 'SAPPYER® SLI_SLIM_SLIE + Bio-balanced SAP（LG Chem）',
    'LG Chem SAP Product Page（Chinaplas Acrylates/SAP）': 'LG Chem SAP Product Page（Chinaplas Acrylates_SAP）',
    '蒙脱土纳米复合高吸水树脂（CMC/AA/OMMT）': '蒙脱土纳米复合高吸水树脂（CMC-AA-OMMT）',
    'Composite Nonwoven Structures（复合非织造结构对比）': 'Composite Nonwoven Structures（SMS_SMMS_SSMMS_SSS 复合结构对比）',
    '高吸水树脂（SAP）': 'SAP（高吸水树脂）',
    'Nuoer（诺尔）': '诺尔（Nuoer）',
    'Sanyo Chemical / SDP Global（三洋化成工业）': 'Sanyo Chemical · SDP Global（三洋化成工业）',
    'STM-00060）': 'Acquisition Test STM-00060（导流性能测试）',
    'Acquisition (Liquid Guidance) Test（导流性能测试': 'Acquisition Test STM-00060（导流性能测试）',
    '2025.10.03 - STEC 2025 - Rewet Design Principles Script': '2025.10.03 - STEC 2025 - Rewet Design Principles Script.docx',
    'STM-00305 SAM分布.docx.md': 'STM-00305 SAM分布.docx',
    '一次性使用卫生用品卫生要求（GB 15979-2024）': 'GB 15979-2024 Hygienic Requirements for Disposable Sanitary Products（一次性使用卫生用品卫生要求）',
    'EP1146916B1 Hot Melt Adhesive (Disposable)（聚烯烃热熔胶）': 'EP1146916B1 Oil Resistant Polybutylene-Based Hot Melt Adhesive (Bostik)',
    'EP1347788B1 Hot Melt Adhesives (Disposable)（聚烯烃热熔胶）': 'EP1347788B1 Antimicrobial Hot Melt Adhesive (Bostik)',
    'Consumer Relevancy of FIUP Method Feb 2025（FIUP 方法消费者相关性）': 'Consumer Relevancy of FIUP Method Feb 2025.docx',
    '可迁移性荧光增白剂（Migratable Fluorescent Whitening Agents）': 'Migratable Fluorescent Whitening Agents（可迁移性荧光增白剂）',
    'Triple Cutting（三层切割）· 未验证概念': 'Triple Cutting Topsheet（三层切割面层）',
    '豪悦护理（HaoYue Nursing）': 'HaoYue Nursing（豪悦护理）',
    'BASF SE': '巴斯夫欧洲公司（BASF SE）',
    '超吸水性纤维（SAF）': 'Super Absorbent Fibre（超吸水纤维 SAF）',
    '热风无纺布供应商考察纪要（修订版）': 'Air-Through Nonwoven Supplier Audit（热风无纺布供应商考察纪要·修订版 2026-08-21）',
    '83 换型要素四层分层与变更控制': '83 Changeover Four-Layer Architecture（换型要素四层分层与变更控制）',
    'log': None,        # 占位/行文，改纯文本
    'wikilink': None,   # 占位/行文，改纯文本
}

COMPARISON_PAT = re.compile(r'对比|Compared| vs |VS')
ENTITY_PAT = re.compile(r'公司|有限|大学|集团|GHC|锦琪昶|BASF|Daehyun|Shin-Etsu|KSC')
FRONT = {
    'concepts': 'type: concept\ndomain: [待补]\nstatus: seed\n',
    'entities': 'type: entity\ncategory: 待核\nrelationship: 待核\n',
    'comparisons': 'type: comparison\nsubjects: [待补]\ndimension: [待补]\n',
}

# 1) 统计缺失目标引用者（改指前）
refs = collections.defaultdict(list)
for f in pages:
    t = open(f, encoding='utf-8', errors='ignore').read()
    for m in LINK.finditer(t):
        tgt = m.group(1).strip()
        if tgt and tgt not in basenames:
            refs[tgt].append(f)

# 2) 改指 + 占位符清理
if '--apply' in sys.argv:
    n_files = 0
    for f in pages:
        t = open(f, encoding='utf-8', errors='ignore').read()
        o = t
        for old, new in REWRITE.items():
            if new is None:
                o = o.replace('[[%s]]' % old, old)
            else:
                o = o.replace('[[%s]]' % old, '[[%s]]' % new)
                o = re.sub(r'\[\[%s\|' % re.escape(old), '[[%s|' % new, o)
        if o != t:
            open(f, 'w', encoding='utf-8').write(o); n_files += 1
    print('改指完成: 修改 %d 个文件' % n_files)

# 3) 剩余缺失 → seed 页
refs2 = collections.defaultdict(list)
for f in pages:
    t = open(f, encoding='utf-8', errors='ignore').read()
    for m in LINK.finditer(t):
        tgt = m.group(1).strip()
        if tgt and tgt not in basenames and tgt not in REWRITE:
            refs2[tgt].append(f)

print('剩余缺失目标: %d 个' % len(refs2))
if '--apply' in sys.argv:
    # 先把含 / 的链接目标改写为安全名（与库内惯例一致：/ → _）
    slash_targets = {t: t.replace('/', '_') for t in list(refs2) + list(REWRITE) if '/' in t}
    n_files = 0
    for f in pages:
        t = open(f, encoding='utf-8', errors='ignore').read()
        o = t
        for old, new in slash_targets.items():
            o = o.replace('[[%s]]' % old, '[[%s]]' % new)
            o = re.sub(r'\[\[%s\|' % re.escape(old), '[[%s|' % new, o)
        if o != t:
            open(f, 'w', encoding='utf-8').write(o); n_files += 1
    if n_files: print('斜杠目标清洗: 修改 %d 个文件' % n_files)
    # 重建缺失表（清洗后）
    refs2 = collections.defaultdict(list)
    for f in pages:
        t = open(f, encoding='utf-8', errors='ignore').read()
        for m in LINK.finditer(t):
            tgt = m.group(1).strip()
            if tgt and tgt not in basenames and tgt not in REWRITE:
                refs2[tgt].append(f)
    print('清洗后剩余缺失目标: %d 个' % len(refs2))
    made = 0
    for tgt, citing in sorted(refs2.items(), key=lambda x: -len(x[1])):
        sub = 'comparisons' if COMPARISON_PAT.search(tgt) else ('entities' if ENTITY_PAT.search(tgt) else 'concepts')
        path = '%s/%s/%s.md' % (WIKI, sub, tgt)
        if os.path.exists(path):
            print('  [跳过·已存在] %s' % path); continue
        citers = []
        for c in citing[:5]:
            b = os.path.basename(c)[:-3]
            citers.append('- [[%s]]' % b)
        body = """---
{front}updated: 2026-09-29
tags: [seed, 待补]
---

# {t}

> ⏳ **Seed page（2026-09-29）**：本页为编译收尾时按引用反查补建的占位页——{n} 处引用指向本标题，但此前代理未创建页面。**仅登记引用来源与待补维度，未填任何数据**；补充内容时须回到下列来源页核对原文，禁止编造。

## Cited by 主要引用来源（{n} 处，取前 5）

{cites}

## Pending 待补维度

- 定义 / 口径 / 关键参数（回到引用来源核对原文后补齐）
- 与既有相关页面的关系（避免同主题重复页）
""".format(front=FRONT[sub], t=tgt, n=len(citing), cites='\n'.join(citers))
        open(path, 'w', encoding='utf-8').write(body)
        made += 1
    print('seed 页已建: %d 个' % made)

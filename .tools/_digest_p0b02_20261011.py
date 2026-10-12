# -*- coding: utf-8 -*-
"""只读：提取 P0-B02/B03/B04 共20 份源文件要点"""
import os, re

ROOT = 'E:/WKB-OB'
DIRS = {
 'IP': 'RAW_FULL/ima_sync/个人知识库/WKB/Areas/IP',
 'SB': 'RAW_FULL/ima_sync/个人知识库/WKB/Areas/Supply Base',
 'TM': 'RAW_FULL/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ',
}

TARGETS = [
 ('IP', '01_模块一：SMMS_US20070203469A1_Disposable_garment_comprising_meltblown_.pdf.md'),
 ('IP', '01_模块一：SMMS_纺粘-熔喷-熔喷-纺粘无纺布_US20070203469A1_Disposable_garment_comprising_meltblown_.pdf.md'),
 ('IP', '09_包覆吸水性聚合物颗粒的方法 (EDANA ERT 完整引用).pdf.md'),
 ('IP', '10_Method for coating SAP particles (with EDANA ERT citations).pdf.md'),
 ('IP', '10_包覆吸水性聚合物颗粒的方法（含 SFC 详细计算）.pdf.md'),
 ('IP', '16_模块三：聚烯烃类热熔胶_US5266394A_Hot_melt_adhesive_compositions_(嵌段共聚物).pdf.md'),
 ('IP', '18_模块四：氨纶橡筋_弹性纤维_CN111134966A_一种具有防漏尿功能的裤型纸尿裤（ω型腿围橡筋）.pdf.md'),
 ('IP', 'CN102245218B.pdf.md'),
 ('IP', 'CN104004521B (1).pdf.md'),
 ('IP', 'JP5604444B2.pdf.md'),
 ('IP', 'US5389093.pdf.md'),
 ('IP', 'US9162007 (1).pdf.md'),
 ('IP', 'US9162007.pdf.md'),
 ('IP', 'v3非传统资源_②OEM测试协议_9_Nippon_Shokubai_CN_101679760_B___EDANA_测试方法引用清单.pdf.md'),
 ('IP', '五-1_一种便于识别吸湿状态的吸收性物品及其方法.pdf.md'),
 ('SB', 'BLOCLO盛色科技公司及产品介绍.pdf.md'),
 ('SB', 'Insilico_brochure_eng.pdf.md'),
 ('SB', 'Matsui 松井☆クロミ総合POP英語20260703.pdf.md'),
 ('SB', 'microcapsule_brochure_2019_chn.pdf.md'),
 ('TM', 'JMP软件操作流程.docx.md'),
]

import hashlib
H = {}
for i, (d, fn) in enumerate(TARGETS, 1):
    p = os.path.join(ROOT, DIRS[d], fn)
    print('=' * 76)
    if not os.path.isfile(p):
        print(f'[{i:02d}] ✗ 缺失 {fn}'); continue
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1); fm[k.strip()] = v.strip().strip('"')
    body = t[m.end():] if m else t
    h = hashlib.sha1(body.encode()).hexdigest()[:10]
    H.setdefault(h, []).append(fn)
    heads = re.findall(r'^#{1,4}\s*(.+)$', body, re.M)
    print(f'[{i:02d}] {fn[:66]}')
    print(f'   {d}  {len(body)}字  sha1={h}')
    if heads: print(f'   标题: ' + ' | '.join(x.strip()[:34] for x in heads[:10]))
    # 首段
    para = re.split(r'\n\s*\n', body.strip())
    first = next((x.strip() for x in para if len(x.strip()) > 40), '')
    if first:
        print('   首段: ' + re.sub(r'\s+', ' ', first)[:260])
    # 含参数行
    nums = [re.sub(r'\s+', ' ', l.strip())[:120]
            for l in body.splitlines()
            if re.search(r'\d', l) and len(l.strip()) > 20 and not l.strip().startswith('#')]
    if nums:
        print(f'   含参行({len(nums)}):')
        for x in nums[:7]: print(f'     · {x}')
    print()

print('=' * 76)
print('【重复件检测 sha1】')
for h, fs in H.items():
    if len(fs) > 1:
        print(f'  ⚠ {h}  {len(fs)} 份完全相同:')
        for x in fs: print(f'      {x[:76]}')
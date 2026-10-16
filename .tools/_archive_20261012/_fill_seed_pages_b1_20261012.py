# -*- coding: utf-8 -*-
"""为 seed 页补内容（第 1 批，2026-10-12）。

**唯一依据**：`.tools/_seed_fill_material_20261012.txt` 抽取的引用来源段落。
**纪律**：绝不编造；来源未描述者保持 seed 并在正文说明。

作用：把 `status: seed` → `growing`，用实质内容替换 Seed 占位段，保留 Cited by 与关联。

用法：python .tools/_fill_seed_pages_b1_20261012.py [--apply]
"""
import glob
import os
import re
import shutil
import sys

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONC = os.path.join(VAULT, 'WIKI', 'concepts')
BACKUP = os.path.join(VAULT, '.tools', '_seed_fill_backup_20261012')
TODAY = '2026-10-12'
FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)

# 页名 -> (定义, [要点...], [关联...])
FILL = {
    '2820结构胶': (
        '汉高的结构胶牌号，用作「气味 1.0」方案的中和剂载体基底，在 KC 实验室胶机上放大测试。',
        ['汉高提供添加气味中和剂的胶样，**以 2820 结构胶为基底**，由 KC 在实验室胶机上放大测试其气味中和效果（源：汉高亚太研发中心技术交流会会议纪要）',
         '气味评价方法尚待建立——计划结合 VOC 探针与人工嗅评（同上）'],
        ['[[汉高]]', '[[Odour Management Routes（气味管理技术路线）]]']),
    '320D': (
        '拟用于替代 240D/470D 规格的等效弹性旦数方案（预计 320D 左右），服务于尿裤弹性收紧力改进。',
        ['会议待办：设计 **240D/470D 等效弹性所需旦数（预计 320D 左右）**方案（源：尿裤（卫生巾）弹性收紧力不足问题及 Niso 材料工艺改进方案探讨）',
         '与 320D 用量增加后的成本平衡需重新核算（价差参照 5000 元/吨）（同上）'],
        ['[[Niso]]', '[[弹性收紧力]]', '[[无粘弹性丝]]']),
    '3D凹凸网面': (
        '丝网工艺可实现的三维凹凸网面结构（**底部平、表面凹**），用于面层/导流层的开孔与储液设计。',
        ['关键结论：**3D 凹凸网面（底部平、表面凹）可做**，但凹凸与大孔的最优组合方案待日方建议（源：日本 Nichidai 丝网工艺技术交流）',
         '工艺实施建议**分片制作安装**（片间有间断、需切割）——连续整张会有圆度及棱角问题，日方工艺本身即逐片制作（同上）',
         '待确认结论：「孔大 → SAP 吸附量多」；需提供 A/B/C 分区孔径及开孔密度设计（同上）'],
        ['[[丝网工艺]]', '[[Pinhole开孔]]', '[[Nichidai（日丝）]]']),
    'Insilico': (
        '**Insilico**（Insilicotech Co., Ltd.，韩国）——化学 + IT 融合的新材料公司，以分子模拟/计算机手段做配方与材料开发；本库中作为功能性微胶囊（感温/感光/水致变色/香精）供应商出现。',
        ['2002 年成立（Insilicotech Co. Ltd.）；公司标识为 **C**（Carbon 碳）的艺术化写法，象征分子对接（docking）（源：Insilico 功能性微胶囊产品手册（英文版））',
         '业务板块贯通基础研究→应用研究→产品：Formulation / AI / Bioinformatics / Atomistic / Quantum 优化 / Scale-up / Product Discovery（同上）',
         '产品体系为**微胶囊包覆**路线（与松井色素的粉末/油墨级 Chromicolor 体系相对比，稳定性/耐久性/成本需按项目实测比选）（源：Insilico 功能性微胶囊（中文产品册·2019））'],
        ['[[Insilico 功能性微胶囊]]', '[[Microencapsulation]]', '[[Daehyun（大炆·微胶囊）]]']),
    'JMP 统计分析软件': (
        '实验室用于分析 Mannequin（人体模型）测试数据的统计分析软件（当前版本 JMP 16）。',
        ['依据内部作业指导书 **WI-JMP《JMP 软件操做流程》**（第 0 版，修订日期 2024-02-26）；实验目的为分析 Mannequin 测试数据（源：JMP 16 软件操作流程（Mannequin 测试数据分析 WI-JMP 第0版））',
         '操作流程：打开 JMP 16 → 将 Mannequin 导出的 Excel 数据拖放至 JMP 主窗口左侧 → 双击打开（同上）'],
        ['[[Mannequin 测试]]']),
    'Kigami': (
        'TJ 供应商的关键工艺之一（与 RTC 组合使用），属**拉伸开孔**类工艺。',
        ['TJ 供应商核心技术为 **Kigami + RTC** 组合；核心判断是拉伸策略——**一步拉伸不可行，须两步（或多步）拉伸并配在线张力监测**（源：TJ 供应商工厂访问与会谈纪要（英文））',
         'pattern pitch 研发曾同时考虑 12 mm 与 8 mm，最终选定 **10 mm**；孔尺寸记录为 **2 mm**（同上）'],
        ['[[RTC工艺]]', '[[Pinhole 开孔]]', '[[张力控制]]']),
    'Niso': (
        '弹性材料相关供应商/材料代号，出现在尿裤弹性收紧力改进的会议讨论中。',
        ['会议议题为「尿裤（卫生巾）弹性收紧力不足问题及 Niso 材料工艺改进方案探讨」，Niso 为该方案涉及的材料方（源：同名会议纪要）',
         '⚠️ 库内来源未展开 Niso 的公司全称、材料规格或供货关系，标 `[待验证]`'],
        ['[[320D]]', '[[弹性收紧力]]', '[[华峰橡筋]]']),
    'PTMEG': (
        '聚四亚甲基醚二醇（Polytetramethylene Ether Glycol），氨纶（聚氨酯弹性纤维）的关键软段原料。',
        ['**生物基路线成本口径**：bio-PTMEG 原料成本为常规的 **3.3 倍**；掺 30% 后总成本 **1.5–2 倍**（玉米芯路线）（源：与华峰集团研发及合作会议纪要）',
         '生物基 PTMEG 存在**回弹损失、耐温差**问题；正与汉高开发低温胶，若无法平替则需规格加粗 10–20%（同上）'],
        ['[[氨纶]]', '[[TPU]]', '[[无溶剂TPU]]', '[[华峰集团（Huafon Group）]]']),
    'Pinhole 开孔': (
        '**旋转刀具 + 拉伸**实现的针孔开孔工艺，用于面层（liner）分区开孔。',
        ['KC 与韩国供应商 Daehyoon 交流该工艺：询问可实现的最小孔尺寸（当前示例 6×9 mm），并提出 liner 分区需求——部分区域 die cut 大孔、部分区域小孔（一半一半或 40% 大孔 + 60% 小孔）（源：Daehyoon 供应商技术来访（主会））',
         '工艺**不是一次完成**——后端做第二次拉伸，可在第二次拉伸时微调总张力（同上）',
         '商业背景：Daehyoon 与 Yuhan Kimberly（YK）关系紧密，YK 占其业务近 50%；与 KC Global 业务很少、KC China 目前无实际业务（同上）',
         '注：与 `[[Kirigami Apertured Nonwoven（切割拉伸开孔工艺）]]` 的**切割拉伸**路线不同，本项为**针孔（pinhole）**路线'],
        ['[[Daehyun（大炆·微胶囊）]]', '[[Tooling Cost]]', '[[TBCW结构]]']),
    'RTC工艺': (
        'TJ 供应商的关键工艺之一（与 Kigami 组合使用）。',
        ['TJ 核心技术为 **Kigami + RTC** 组合，配合两步（多步）拉伸 + 在线张力监测（源：TJ 供应商工厂访问与会谈纪要（英文））',
         '⚠️ 库内来源未展开 RTC 全称与工艺原理，标 `[待验证]`'],
        ['[[Kigami]]', '[[TBCW结构]]']),
    'SIS 嵌段共聚物': (
        '**SIS（聚苯乙烯-聚异戊二烯-聚苯乙烯）嵌段共聚物**，用作可弃式尿布多线贴合（multi-line construction）用热熔胶的基体。',
        ['专利依据：US 5,266,394 A（Dow Chemical + Exxon Chemical Patents；授权日 1993-11-30；发明人 Diehl / Myers / Tancrede；29 项权利要求）（源：US 5266394 A SIS 嵌段共聚物热熔胶）',
         '软相 = 中间聚异戊二烯（SIS）或聚丁二烯（SBS）嵌段，硬相 = 两端聚苯乙烯嵌段（物理交联点）；两相结构是全部性能的来源（源：Styrenic Block Copolymer Hot Melt）',
         'Adhesive Handbook Part 3 将其归入「SBR + 嵌段共聚物」胶类（该类含 SBS/SIS）（同上）'],
        ['[[Styrenic Block Copolymer Hot Melt（SIS-SBS 苯乙烯嵌段共聚物热熔胶）]]', '[[SBS 弹性体]]', '[[热熔胶 Hot Melt Adhesive]]']),
    'SMMS 纺粘-熔喷-熔喷-纺粘无纺布': (
        '**SMMS**（纺粘-熔喷-熔喷-纺粘）四层复合非织造布，作为液不可透 + 可透气的背片材料。',
        ['P&G 专利 US 2007-0203469 A1 用**熔喷细纤维网替代传统 PE 薄膜**做液不可透背片，解决 PE 膜「穿着不适、几乎无透湿与透气性」痛点（源：US 2007-0203469 A1 熔喷非织造背片）',
         '**硬性指标**：背片透气率 ≥20 cm³/cm²/sec、透湿率 ≥9000 g/m²/24hr —— 这是 SMMS 取代 PE 薄膜在「液不可透 + 可透气」间的量化门槛（同上）',
         '与 `[[SMS复合结构]]`（三层 S-M-S）相比多一层熔喷，阻隔与强度更高'],
        ['[[SMS复合结构]]', '[[纺粘熔喷 Spunbond-Meltblown]]', '[[背片 Backsheet]]']),
    'SUPER ABSORBENT RESIN': (
        'SAP（高吸水树脂）的英文泛称，出现于 P&G 熔喷背片专利的吸收芯方案描述中。',
        ['专利原文口径：吸收芯可为**绒毛浆木浆纤维、coform、化学改性或交联纤维素纤维、tissue、吸收泡沫、SAP 等**，可为非对称改良 T 形（前腰区矩形）（源：US 2007-0203469 A1 熔喷非织造背片）',
         '中文对应库内页 `[[SAP（高吸水树脂）]]`（Superabsorbent Polymer）'],
        ['[[SAP（高吸水树脂）]]', '[[Super Absorbent Fibre（超吸水纤维 SAF）]]']),
    'T-channel': (
        '张力控制/开孔用的模块型式之一，与张力控制模块并列。',
        ['Daehyoon 供应商提到 **KC 也开发过张力控制模块或 T-channel 模块**，因此可提供完整解决方案（源：Daehyoon 供应商技术来访（主会））',
         '⚠️ 库内来源未展开 T-channel 的结构定义，标 `[待验证]`'],
        ['[[Pinhole 开孔]]', '[[张力控制模块]]', '[[旋转刀具]]']),
    'TPU': (
        '热塑性聚氨酯（Thermoplastic Polyurethane），可用作无溶剂路线材料与基膜。',
        ['**无溶剂 TPU** 是行业主流，但物性波动（熟化漂移）（源：与华峰集团研发及合作会议纪要）',
         '产线调整方案：简易方案（下移喷丝/热风点促挥发）约 1 个月出结果；复杂重卷绕退 DMF 方案**增本 20–30%**（同上）',
         '会议给出 TPU 基膜完整参数（同上）'],
        ['[[无溶剂TPU]]', '[[水性聚氨酯 Waterborne PU]]', '[[PTMEG]]']),
    'Tooling Cost': (
        '开孔/模切等工艺的**刀具（tooling）成本**及其分担安排。',
        ['Daehyoon 表态 **tooling cost 部分承担、非 100%**，理由是 co-development（源：Daehyoon 供应商技术来访（总结与行动项））',
         '前提条件：**不向其他客户销售**（排他）与 tooling 分担挂钩（同上）'],
        ['[[旋转刀具]]', '[[Rotary Die Tooling Material Route（旋转模切刀具材质路线：高速钢 vs 硬质合金）]]']),
    '中纺技术': (
        '三叶草（异形截面）纤维的国内供应方，与蓝鲸同源。',
        ['中纺技术与蓝鲸**同源但便宜约 4000 元/吨**；决议为推动三叶草喷丝板开发并**深度绑定中纺**（源：OI（Open Innovation）团队会议纪要）'],
        ['[[异形纤维]]', '[[三叶形截面纤维（Trilobal Fibre）]]', '[[蓝鲸]]']),
    '亲水胶3059': (
        '汉高的亲水胶牌号（3059），用于芯体中 SAP 固定与导流通道。',
        ['行动项：尽快寄送样品，在 **KC 芯体机上实测其对 SAP 固定、导流通道的实际效果**，关注能否与 Hybrid 结构结合创新（源：汉高亚太研发中心技术交流会会议纪要）'],
        ['[[汉高]]', '[[Hydrophilic SAP Wrapping Adhesive（亲水SAP包裹胶）]]', '[[2820结构胶]]']),
    '低温PP': (
        '低熔点聚丙烯（熔点约 **140℃**），作为 TBCW 底层降本替代材料。',
        ['TBCW 底层（Bottom Layer / Spun Bond）由 20 gsm 降至 12 gsm 即足够，并**建议改用低温 PP（熔点约 140℃）替代昂贵的皮芯 PE/PP 材料**（源：KC 团队内部技术讨论会（TBCW 在线超声波复合工艺））'],
        ['[[TBCW结构]]', '[[低熔点聚丙烯]]']),
    '低聚半乳糖GOS': (
        '益生菌项目的主成分（益生元），宝洁微生物平台常用。',
        ['**低聚半乳糖（GOS）**为主成分（宝洁微生物平台常用，**粒径需 <20 微米**、价格低廉），另含乳酸钠等；premium 版含额外成分（加量约 0.5%）（源：会议纪要：FEI & OI 益生菌项目）',
         '施加量约 **3 克/片**，转移到皮肤的起效量约 **6 毫克**（同上）'],
        ['[[益生菌]]', '[[凡士林]]']),
    '凡士林': (
        '益生菌项目的配方组分（含量 55–65%），兼作低粘度施胶载体。',
        ['AI 方案复现 Nate-3/Nate-4 配方：**凡士林 55–65%** + 氧化锌等，与实际相符（源：会议纪要：FEI & OI 益生菌项目）',
         '**凡士林量仅 0.5% 的版本粘度较低**，利于现有胶枪系统的刮涂工艺（刮枪粘度不能太高）（同上）'],
        ['[[低聚半乳糖GOS]]', '[[益生菌]]']),
    '动态色彩': (
        'BLOCLO（广州盛色科技）的定位概念——材料本身随**光或温度**发生可逆颜色变化的「动态色彩」材料。',
        ['BLOCLO = **B**looming **C**olor（盛开的色彩），定位功能性「动态色彩」材料制造商（源：BLOCLO 盛色科技产品册）',
         '产品形态：光变类（光变染料/粉/色膏/纤维，4 种）、温变类（温变粉/色膏/色母粒，3 种）；设「动态色彩协同开发中心」四大开发方向（同上）'],
        ['[[光变材料]]', '[[变色材料 Chromic Materials]]', '[[盛色科技（BLOCLO）]]']),
    '分叉导流': (
        '导流层/芯体的**分叉（树状）导流**结构设计，用于改善液体铺展与对位容差。',
        ['建议**中间树干部分做细槽**（如上方叉 8、下方叉 4），兼顾对位容差（**MD 方向 2 mm 偏差可接受**）与上下绑定强度（源：纸尿裤产品设计与材料开发评审会）'],
        ['[[MD Liquid Distribution]]', '[[分叉导流]]', '[[哑铃型版型]]']),
    '单纺位试验线': (
        '闽瑞（纤维供应商）的小试装备：**可换喷丝板、与生产线共用原料**，用于异形纤维的初步验证。',
        ['经济性判据：小批量添加（**5%~10%**）优先用单组分最经济；若添加量大，由闽瑞用**单纺位试验线**配合初步验证（源：复合纤维生产工艺及性能探讨（KC 与闽瑞纤维技术交流））',
         '双组分全熔/半熔的意义在于**异形纤维添加量上限可提高**（单组分一般只能加 5%~10%）（同上）'],
        ['[[异形纤维]]', '[[皮芯复合纤维]]', '[[福建闽瑞新合纤]]']),
    '去味粉': (
        '用于芯体除味的粉体功能材料；因 EHS 粉尘管控改由诺尔预混。',
        ['去味粉因**实验室无大规模混料能力且涉 EHS 粉尘管控**，改为**委托诺尔预混**（源：CO V6 新体机芯体验证实验方案评审）',
         '（另一路线）中科依兰纳米除臭粉可通过**油剂施加于热风无纺布**，需验证喷嘴堵塞与线上跌落问题（源：OI（Open Innovation）团队会议纪要）'],
        ['[[诺尔（Nuoer）]]', '[[Zeolite Odour Control（沸石除臭载体）]]', '[[Odour Management Routes（气味管理技术路线）]]']),
    '双组分纤维PE／PET': (
        '**PE/PET 双组分（bicomponent）纤维**，作 Liner 打样的粘结组分（2D/4D Bico）。',
        ['Liner 打样 Code 1（50 gsm）：上层 25 gsm（10% 三叶草 + **90% 2D Bico PE/PET**）、下层 25 gsm（50% 三叶草 + **50% 4D Bico PE/PET**），幅宽 102 mm（源：Liner Trial Request）',
         'Code 2-A（30 gsm，优先）：上层 15 gsm（10% 三叶草 + 90% 2D Bico）、下层 15 gsm（50% 三叶草 + 50% 4D Bico），幅宽 82 mm（同上）',
         '配比策略：**上层少量异形、下层大量异形**（同上）'],
        ['[[双组分纤维 Bicomponent]]', '[[三叶形截面纤维（Trilobal Fibre）]]', '[[皮芯复合纤维]]']),
    '可弃式服装（P&G 专利族）': (
        'P&G 可弃式吸收制品专利族的构造要件集合，按专利附图 FIG.1 给出完整分解。',
        ['FIG.1 构造要件：容纳组件 22 / 液可透顶片 24 / 液不可透背片 26 / 吸收芯 28 / 侧片 30 / 弹性腰区 34 / 腿箍 32 / 紧固系统 36（源：US 2007-0203469 A1 熔喷非织造背片）',
         '该族另一件 US 5,266,394 A 针对可弃式尿布的 **multi-line construction（多线贴合）**工况设计热熔胶（源：US 5266394 A SIS 嵌段共聚物热熔胶）',
         '注：库内另有 `[[US 7,195,621 B2（P&G 熔喷背片授权本）]]` 关联本族'],
        ['[[US 7,195,621 B2（P&G 熔喷背片授权本）]]', '[[多线贴合（multi-line construction）]]', '[[背片 Backsheet]]']),
    '哑铃型版型': (
        '芯体/产品的**哑铃型（两端宽中间窄）**版型设计，配合撒粉工艺。',
        ['需复核**最窄区域负压/镂空面积优化方案**，验证抓粉上限（源：纸尿裤产品设计与材料开发评审会）'],
        ['[[分叉导流]]', '[[撒粉均匀性]]', '[[Pattern 成型芯体]]']),
}


def main():
    apply = '--apply' in sys.argv
    todo = []
    for n, (d, pts, rel) in FILL.items():
        p = os.path.join(CONC, n + '.md')
        if not os.path.exists(p):
            print('[跳过] 不存在:', n); continue
        if not re.search(r'^status:[ \t]*seed', open(p, encoding='utf-8', errors='ignore').read(), re.M):
            print('[跳过] 非 seed:', n); continue
        todo.append((n, p, d, pts, rel))
    print('本批拟补: %d 页' % len(todo))
    if not apply:
        for n, *_ in todo:
            print('  ', n)
        print('\n(dry-run; 加 --apply 执行)')
        return
    os.makedirs(BACKUP, exist_ok=True)
    for _, p, *_ in todo:
        dst = os.path.join(BACKUP, os.path.basename(p))
        if not os.path.exists(dst):
            shutil.copy2(p, dst)
    n_ok = 0
    for name, p, d, pts, rel in todo:
        t = open(p, encoding='utf-8', errors='ignore').read()
        m = FM_RE.match(t)
        fm, body = m.group(1), t[m.end():]
        # 保留 Cited by 段
        cb = re.search(r'(## Cited by.*?)(?=\n## |\Z)', body, re.S)
        cb_txt = cb.group(1).strip() if cb else ''
        fm2 = re.sub(r'^status:[ \t]*seed', 'status: growing', fm, count=1, flags=re.M)
        fm2 = re.sub(r'^updated:[ \t]*.*$', 'updated: %s' % TODAY, fm2, count=1, flags=re.M)
        new = ['---\n' + fm2 + '\n---\n', '\n# %s\n' % name,
               '\n## Definition 定义\n\n%s\n' % d,
               '\n## Key Points 要点\n\n' + '\n'.join('- %s' % x for x in pts) + '\n',
               '\n## Related 关联\n\n' + '\n'.join('- %s' % x for x in rel) + '\n']
        if cb_txt:
            new.append('\n' + cb_txt + '\n')
        new.append('\n> 内容依据：见上方 Cited by 所列来源页；未在来源中出现的表述均未写入。\n')
        with open(p, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write('\n'.join(new))
        n_ok += 1
    print('已补: %d 页 (seed → growing)' % n_ok)


if __name__ == '__main__':
    main()

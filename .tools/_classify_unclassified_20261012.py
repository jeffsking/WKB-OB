# -*- coding: utf-8 -*-
"""逐条细分 114 页「待归类」concept（2026-10-12）。

方法：人工逐条读定义 → 归入 MOC 11 域（必要时补少量域）。
依据：`.tools/_unclassified_20261012.txt`（含各页定义摘要）。

幂等：域值确定，第二次运行 0 改动。
安全：--apply 前备份。

用法：
  python .tools/_classify_unclassified_20261012.py            # dry-run
  python .tools/_classify_unclassified_20261012.py --apply
"""
import glob
import json
import os
import re
import shutil
import sys
from collections import Counter

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONC = os.path.join(VAULT, 'WIKI', 'concepts')
BACKUP = os.path.join(VAULT, '.tools', '_unclassified_fix_backup_20261012')
FM_RE = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)
TODAY = '2026-10-12'

# title → MOC 域（逐条人工裁定，依据定义内容）
ASSIGN = {
    '2025.08.28 - GRIFFIN Regroup（GRIFFIN 重整与再聚焦）': '实体与供应链',
    '82 鼓距与产品节距解耦 repitch 选型': '芯体与吸收',
    '87 卫材产线约束常量表（待并入补充行）': '芯体与吸收',
    'APAC 卫生纸产品矩阵（2017  workshop 预研）': '实体与供应链',
    'AUL 加压吸水率': 'SAP与流体',
    'Ardex': '实体与供应链',
    'Botanical Extract Efficacy Verification（植物提取物功效验证）': '功能添加剂与整理',
    'CLC 手性向列晶': '变色与智能材料',
    'CRC 离心保持能力': 'SAP与流体',
    'CTMP 化学热磨浆': 'REL增强层与纤维',
    'Clariant': '实体与供应链',
    'DIC': '实体与供应链',
    'Deep-Tech Commercialisation Due Diligence（深科技商业化尽调四支柱）': '实体与供应链',
    'Front Belt Force Window（前腰带弹性力窗口）': '芯体与吸收',
    'GST': '变色与智能材料',
    'Grafted Cellulose and Starch': 'SAP与流体',
    'Hercules Aqualon': '实体与供应链',
    'Hygiene Absorption Model': '基础理论与模型',
    'IPA（间苯二甲酸）': 'REL增强层与纤维',
    'IPC BCC OI Portfolio（开放创新项目组合）': '实体与供应链',
    'Klemm 法': '测试与标准',
    'Lagrangian Particle Tracking': '基础理论与模型',
    'LbL 自组装 Layer-by-Layer': '表面处理与胶黏剂',
    'Material Safety Control（材料安全双轨管控）': '法规与合规',
    'PAA 聚丙烯酸': 'SAP与流体',
    'PET（聚酯）': 'REL增强层与纤维',
    'PVAc 乳液': '表面处理与胶黏剂',
    'Pain-Point Backward Derivation（痛点倒推法）': '实体与供应链',
    'Polyolefin Absorbent Materials': 'SAP与流体',
    'Product Dimension Measurement（成品尺寸测量）': '测试与标准',
    'Product Safety Crisis Management（产品安全危机管理）': '法规与合规',
    'Rotary Die Tooling Material Route（旋转模切刀具材质路线：高速钢 vs 硬质合金）': '无纺布工艺',
    'SBS 弹性体': '表面处理与胶黏剂',
    'STM-00146': '测试与标准',
    'Sensor-Equipped Absorbent Article（含传感器吸收性物品）': '变色与智能材料',
    'Shaped PET Add-On Window': '芯体与吸收',
    'Signal Comprehension Gate': '变色与智能材料',
    'Specific Air Volume': '测试与标准',
    'TCF Bleaching（全无氯漂白）': 'REL增强层与纤维',
    'TPE Tetraphenylethylene': '变色与智能材料',
    'Technology Roadmap 2026-2029（技术路线图）': '实体与供应链',
    'VO2': '变色与智能材料',
    'Videoimagescope': '测试与标准',
    'WRV 水保留值': '测试与标准',
    'k-ε 湍流模型': '基础理论与模型',
    'pH 响应材料': '变色与智能材料',
    '一氯乙酸 Monochloroacetic Acid': '功能添加剂与整理',
    '三相接触线 TPL': '基础理论与模型',
    '交联 CMC': 'SAP与流体',
    '健康监测 Health Monitoring': '变色与智能材料',
    '全息存储 Holographic Storage': '变色与智能材料',
    '动边界 Moving Boundary': '基础理论与模型',
    '化妆品科学 Cosmetic Science': '功能添加剂与整理',
    '原纤化': 'REL增强层与纤维',
    '取代度 DS': 'SAP与流体',
    '可冲散拭布 Flushable Wipe': '无纺布工艺',
    '可穿戴传感器 Wearable Sensor': '变色与智能材料',
    '含水率 Moisture Regain': '测试与标准',
    '复合材料 Composite': '基础理论与模型',
    '复合膜 Composite Membrane': '无纺布工艺',
    '天丝 Tencel': 'REL增强层与纤维',
    '导电纱线 Conductive Yarn': '变色与智能材料',
    '尾水培养基（非粮生物合成）': '基础理论与模型',
    '戊二醛 Glutaraldehyde': '功能添加剂与整理',
    '承压吸收 AUL': 'SAP与流体',
    '接枝共聚 Graft Copolymer': 'SAP与流体',
    '摩擦电自供电 TENG': '变色与智能材料',
    '时间滞后法 Time Lag Method': '测试与标准',
    '智能包装 Smart Packaging': '变色与智能材料',
    '智能织物 Smart Textile': '变色与智能材料',
    '机械脱水 Mechanical Dewatering': '基础理论与模型',
    '柔性电子 Flexible Electronics': '变色与智能材料',
    '植物基材料 Plant-Based Material': '功能添加剂与整理',
    '植物提取物 Plant Extract': '功能添加剂与整理',
    '每克厚度 T／W': '测试与标准',
    '浊点 Cloud Point': '功能添加剂与整理',
    '深沟槽涤纶 Deep-groove Polyester': 'REL增强层与纤维',
    '温度响应材料': '变色与智能材料',
    '湿冷感 Wet-Cool': '芯体与吸收',
    '湿巾 Wet Wipes': '无纺布工艺',
    '湿强剂 Wet-Strength Resin': '功能添加剂与整理',
    '湿态压缩模量': '测试与标准',
    '湿态强度 Wet Strength': 'REL增强层与纤维',
    '湿热耦合 Heat-Moisture Coupling': '基础理论与模型',
    '湿迁移 Wet Migration': '基础理论与模型',
    '热传递 Heat Transfer': '基础理论与模型',
    '热电现象 Thermoelectric': '基础理论与模型',
    '环氧氯丙烷 Epichlorohydrin': '功能添加剂与整理',
    '生物基单体 Bio-based Monomer': '功能添加剂与整理',
    '甲醛 Formaldehyde': '法规与合规',
    '甲醛排放 E1': '法规与合规',
    '电子纺织品 E-textile': '变色与智能材料',
    '皮肤科学 Dermatology': '功能添加剂与整理',
    '硅烷偶联剂 Silane Coupling Agent': '表面处理与胶黏剂',
    '离子强度 Ionic Strength': '基础理论与模型',
    '粘合剂 Binder': '表面处理与胶黏剂',
    '结构性常数 K': '基础理论与模型',
    '聚合物刷 Polymer Brush': '基础理论与模型',
    '自-sizing Self-sizing': '无纺布工艺',
    '自由体积 Free Volume': '基础理论与模型',
    '茂金属聚丙烯': 'REL增强层与纤维',
    '蒙脱土 Montmorillonite': '功能添加剂与整理',
    '薄膜压力分布传感（Pressure-Sensing Film）': '测试与标准',
    '藻酸盐 Alginate': 'SAP与流体',
    '虚拟原型 Virtual Prototyping': '基础理论与模型',
    '螺噁嗪 Spiroxazine': '变色与智能材料',
    '解键剂 Debonding Agent': '功能添加剂与整理',
    '超分子 Host-Guest Chemistry': '基础理论与模型',
    '辐射冷却材料 Radiation Cooling': '基础理论与模型',
    '过滤材料 Filter Material': '无纺布工艺',
    '银纳米线 AgNW': '变色与智能材料',
    '防水透气 Waterproof Breathable': '无纺布工艺',
    '香豆素 Coumarin': '变色与智能材料',
    '驻极体 Electret': '基础理论与模型',
}


def main():
    apply = '--apply' in sys.argv
    files = glob.glob(os.path.join(CONC, '*.md'))
    todo, dist, miss = [], Counter(), []
    for f in files:
        n = os.path.basename(f)[:-3]
        t = open(f, encoding='utf-8', errors='ignore').read()
        m = FM_RE.match(t)
        if not m or '待归类' not in m.group(1):
            continue
        dom = ASSIGN.get(n)
        if not dom:
            miss.append(n)
            continue
        todo.append((f, n, dom))
        dist[dom] += 1

    print('待归类页: %d | 已裁定: %d | 未覆盖: %d' % (len(todo) + len(miss), len(todo), len(miss)))
    if miss:
        print('未覆盖（保持待归类）:')
        for x in miss:
            print('   ', x)
    print()
    print('=== 裁定分布 ===')
    for k, v in dist.most_common():
        print('  %-22s %d' % (k, v))

    if not apply:
        print('\n(dry-run; 加 --apply 执行)')
        return

    os.makedirs(BACKUP, exist_ok=True)
    for f, _, _ in todo:
        dst = os.path.join(BACKUP, os.path.basename(f))
        if not os.path.exists(dst):
            shutil.copy2(f, dst)
    print('\n备份: %d 文件 -> %s' % (len(todo), os.path.relpath(BACKUP, VAULT)))

    n = 0
    for f, name, dom in todo:
        t = open(f, encoding='utf-8', errors='ignore').read()
        m = FM_RE.match(t)
        fm, body = m.group(1), t[m.end():]
        fm2 = re.sub(r'^domain:[ \t]*.*$', 'domain: [卫材研发, %s]' % dom, fm, count=1, flags=re.M)
        with open(f, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write('---\n' + fm2 + '\n---\n' + body)
        n += 1
    print('已细分: %d 页' % n)
    json.dump(ASSIGN, open(os.path.join(VAULT, '.tools', '_unclassified_assign_20261012.json'),
                           'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()

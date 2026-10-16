---
type: concept
title: "机械变色 Mechanochromic"
domain: [卫材研发, 变色与智能材料]
status: growing
updated: 2026-09-30
tags: [mechanochromic, 机械变色, 力致变色, chromic-materials, mechanophore, photonic-crystal, geometric-optical-mask, wearable-indicator]
---

# 机械变色 Mechanochromic

> 📌 **Page completed 2026-09-30** from 10 citing sources in the vault. All figures traced to their source pages. Anything not evidenced in the vault is marked `[待补]`.

## Definition 定义

Mechanochromic（机械变色 / 力致变色）is colour change triggered by a **mechanical** input. The vault sets a hard scope rule: it covers **只由拉伸、压力、形变或剪切触发的变色**，**全程排除湿致变色（hydrochromic）、吸湿响应与液体感知**（源：[[Mechanochromic Supplier Report 2026-08（力致变色供应商调研·英文版）]]）。The governing classification principle is **按触发量分类，而不是按化学分类** — 判类的关键问题是「到底什么物理量抵达材料」；中文语境里「变色材料」同时涵盖温/湿/光/力四族，**询证时必须问「触发量是什么」，而不是问「有没有变色材料」**（源：[[Chromism Taxonomy（变色现象分类）]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Threshold gap 阈值鸿沟 | 工业计量材料 ≥ 40,000 psi → 吸收性卫品低张力窗口 20–150 kPa | [[力致变色材料研究报告（2026-08-02·纸尿裤应用研判）]] |
| False-negative strain window 假阴性应变区间 | 25–27%（Barty-King et al., 2025） | [[力致变色材料研究报告（2026-08-02·纸尿裤应用研判）]] |
| Market trajectory 市场轨迹 | US$1.2 B（2024）→ US$4.1 B（2033）；全球 CAGR 14.6%，APAC CAGR 17.2% | [[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]] |
| Roadmap milestones 路线图里程碑 | M1 台架协议 第 4 月；M2 产线集成 第 9 月；M3 合规/FTO 第 16 月；M4 商业化上市 第 24 月 | [[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]] |
| OI-17 concept target 力致变色概念指标 | ~0.09¢/pant；ΔE*ab > 18；全可逆 | [[CTI (Chromatic Technologies)]] |
| Opal particle size 蛋白石粒子尺寸 | core-shell PS/PEA 粒子 ~200–300 nm，剪切组装成弹性蛋白石 | [[Structural Colour Mechanochromism（结构色力致变色）]] |
| Photonic-fibre shift / durability 光子纤维位移与耐久 | 红→蓝跨越 127 nm；耐受 100+ 拉伸循环；roll-to-roll > 100 m 蛋白石膜 | [[Structural Colour Mechanochromism（结构色力致变色）]] |
| Wet-set strain for opal ordering 蛋白石有序化的应变 | ~300% 应变振幅（加热辊间振荡剪切） | [[Structural Colour Mechanochromism（结构色力致变色）]] |
| Pressure-sensing range 压力传感量程 | 0.1–3 psi（≈ 0.7–20 kPa，芯体内/体表载荷口径） | [[智能尿裤功能层]] |
| Panel strain→force 面板应变→力 | 85 mm 面板在 38 / 67 / 101% 应变下为 1.4 / 2.5 / 3.9 N | [[智能尿裤功能层]] |
| Skin-contact pressure 皮肤接触压力 | 宽 85 mm 面板在 101% 应变下仅 ~4.3 mmHg；约 10 mm 窄腰弹性体在 2.5 N 下 ~29 mmHg | [[智能尿裤功能层]] |
| Comfort over-estimate 舒适度高估 | 阈值标定若落在加载支，舒适度被高估约 30% | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Incoming-material control 来料控制 | 预拉伸比与松弛波纹间距须写进面板采购规格（Cpk ≥ 1.33 + 逐批证书） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |

## Method / Mechanism 方法 / 机理

- **Four technology routes / build-not-buy 四条路线与自建结论.** The Mechanochromic block maps **M1–M4 four routes**, screens four material candidates, and lands on **「build, not buy」**（自定义阈值 + 自定义印刷工艺）——推翻「买一款商用压力材料」的初始假设（源：[[Mechanochromic Materials Technical Review（EN v3, 2026-08）]]）。Day-1 主假设被显式证伪：**无成熟 SKU，必须 build 而非 buy**（源：[[力致变色材料研究报告（2026-08-02·纸尿裤应用研判）]]）。
- **Three routes named 三条命名路线.** 力致变色分支含 **Mechanophore Mechanochromism（机械力致变色分子）、Structural Colour Mechanochromism（结构色力致变色）、Geometric Optical Mask（几何光学掩膜）**（源：[[Chromism Taxonomy（变色现象分类）]]）。分子路线被三条理由否决（阈值、热/极性稳定性、循环寿命），**几何掩膜是唯一 TRL 8 方案**（源：[[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]]）。
- **Second and third axes 可逆性与阈值.** 第二条轴是**可逆性**（reversible vs irreversible / one-shot）——连续监测需可逆路线，单次报警可用半可逆或不可逆路线，**淘汰设计的是这条轴，不是化学类别**；第三条轴是**阈值**（源：[[Chromism Taxonomy（变色现象分类）]]）。
- **Implementation selection 落地选型.** 弹性侧片「拉伸式合身指示器」定下 **7 条硬约束**、筛查 **7 大变色族**，最终落到**单道狭缝涂布 + 几何光学掩膜**（源：[[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]]）。立项提案用**五候选筛查表**选中几何掩膜（源：[[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]]）。

## Hygiene Relevance 卫材关联

- **Power-free safety indication 无源安全指示.** 整合 **force-responsive, power-free** 传感器可把普通纸尿裤变为「智能」安全装置，**无源 = 无电池、无芯片、无电子件**——这是进入一次性用品的先决条件；Zone 1（腰围 tabs）在拉力超出生理安全阈值时触发高可见信号以**防勒伤**（源：[[Active Diagnostic Zones（主动诊断分区）]]）。
- **Fitness, not medical claim 合身指引而非医疗声明.** 面板伸长可用，但**面板不是压迫源**，指示器只能定位为**合身/防漏指引**，**绝不可作医疗或压力安全声明**（源：[[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]]、[[智能尿裤功能层]]）。换算链的结论：宽 85 mm 面板在 101% 应变下仅约 4.3 mmHg，远低于 20–30 mmHg 持续毛细血管闭塞阈值；**真正的红印来源是约 10 mm 的窄腰弹性体**（源：[[智能尿裤功能层]]）。
- **Supplier landscape at the hygiene gate 卫材门槛上的供应格局.** 四大领导者锁定高价值应用（Merck — polymer platform；GIVIDI — security pressure materials；Avient — elastomers/composites；Sun Chemical — printable mechanochromic inks），加两家可印刷油墨差异化者（CTI、LCR Hallcrest）；唯一无巨头把守的入场段是 **printable pressure-activated inks**（源：[[Mechanochromic Materials Technical Review（EN v3, 2026-08）]]）。**CTI 在「合规与商业成熟度」两项均居首**，被列为 ★ Primary，并在立项提案中指定为**索取报价与样品**的接收方（gate：samples within 2–4 weeks）；**库内无任何已发生的采购、打样或交付记录**（源：[[CTI (Chromatic Technologies)]]）。
- **No new chemical classes 不新增化学品类别.** 几何掩膜方案的全部组分**已存在于纸尿裤结构胶或印刷底膜中**（源：[[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]]）。
- **Adjacent structural-colour route 相邻结构色路线（间接）.** 光子晶体/聚合物蛋白石与弹性体光子纤维依赖 ~300% 应变的专用振荡剪切线，**不是狭缝涂布线**；该路线与卫材的关联为**间接**（源：[[Structural Colour Mechanochromism（结构色力致变色）]]）。

## Open Questions 待补

- 各候选的**精确力阈值范围**、**可逆循环次数**、**皮肤/口服安全检测报告**均缺（原文标 [A]/[E]）（源：[[力致变色材料研究报告（2026-08-02·纸尿裤应用研判）]]）。
- **CTI 压力墨下移至卫材低张力的可行性与报价**未验证；库内**无报价或价格区间**（源：[[力致变色材料研究报告（2026-08-02·纸尿裤应用研判）]]、[[CTI (Chromatic Technologies)]]）。
- **R1 阈值漂移与 R2 信号弛豫均为 HIGH 风险**；**信号弛豫的假阴性比没有指示器更糟**（源：[[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]]）。
- **两种力度量口径不可直接互换**：芯体内/体表载荷（kPa）与带体对皮肤的接触压力（mmHg）；跨页比较前须人工确认口径（源：[[智能尿裤功能层]]）。
- **精确门槛数值**：力致变色材料研究报告的完整 DOI 为 10.1177/00405175251352163，市场规模来源 Marketintelo——但各量化边界仍待原文补足（源：[[力致变色材料研究报告（2026-08-02·纸尿裤应用研判）]]）。

## Related Sources 关联来源

- [[Mechanochromic Materials Technical Review（EN v3, 2026-08）]]
- [[力致变色材料研究报告（2026-08-02·纸尿裤应用研判）]]
- [[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]]
- [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]]
- [[Chromism Taxonomy（变色现象分类）]]
- [[Mechanochromic Supplier Report 2026-08（力致变色供应商调研·英文版）]]
- [[Structural Colour Mechanochromism（结构色力致变色）]]
- [[Active Diagnostic Zones（主动诊断分区）]]
- [[CTI (Chromatic Technologies)]]
- [[智能尿裤功能层]]
- [[Mechanochromic Routes Comparison（力致变色技术路线对比）]]
- [[Geometric Optical Mask（几何光学掩膜）]]

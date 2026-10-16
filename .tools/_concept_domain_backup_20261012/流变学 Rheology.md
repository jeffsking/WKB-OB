---
type: concept
title: "流变学 Rheology"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [rheology, viscoelasticity, hot-melt-adhesive, peel-strength, MFR, melt-rheology, PSA]
---

# 流变学 Rheology

> 📌 **Page completed 2026-09-30** from 1 citing source (7 vault pages carry verbatim excerpts). All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**流变学 = 研究材料变形与流动的科学**；"The branch of science related to the study of deformation and flow of materials was given the name **rheology** by Bingham"；前缀 rheo 源自希腊语 *rheos*，意为"流"（源：[[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]]）。

- 库内引用来源把它作为**力学与流变学核心章**：从两个元件——**胡克弹簧**与**牛顿黏壶**——出发，建立**黏弹性**的数学框架（源：[[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]]）。
- 该来源未给出"流变学"的完整形式化定义，只有上述**命名学定义 + 元件模型框架** `[待补]`。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 剥离强度主方程 | $G = G_0\cdot\psi(v,T)$（ψ 远大于 E，黏弹性耗散为主导贡献） | （源：[[Adhesive Handbook Part 2 Fundamental Aspects]]） |
| 本征断裂能与交联分子量 | $G_0 = E\cdot g(M_c)$；$G_0 \propto E^2 \propto W_A^2$ | （源：[[Adhesive Handbook Part 2 Fundamental Aspects]]） |
| 配方粘度（便指示设计） | 3,200 mPa·s @120 °C（2,100 @130 °C、1,400 @140 °C） | （源：[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]） |
| Cross index n | 0.88（规格 ≥0.85；近牛顿设定） | （源：[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]） |
| 松弛时间 λ | ≤ 2×10⁻⁴ s | （源：[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]） |
| 流动活化能 | 56 kJ/mol | （源：[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]） |
| 缝口压力—缝口厚度标度 | $P \propto 1/t^3$；200 µm shim → 13.6 bar（5 mm land, 400 m/min）；100 µm → 99.7 bar 并堵泵 | （源：[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]） |
| 便指示体系 Ca 数 | 272（因此须接触式（wiped）缝口 + 冷辊） | （源：[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]） |
| PP 薄膜级 MFR（slit film, non-CR homopolymer） | 2–4 g/10 min | （源：[[Handbook of Polypropylene and Polypropylene Composites]]） |

## Method / Mechanism 方法 / 机理

- **黏弹性元件模型**：**Maxwell 串联 → 应力松弛**；**Kelvin-Voigt 并联 → 蠕变**（源：[[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]]）。
- **黏弹性耗散主导胶接强度**：$G = G_0\cdot\psi(v,T)$ 中 ψ 远高于 E，能量耗散是强度 G 的主要贡献（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）。
- **剥离强度是速率与温度的函数**：通过 $\psi(v,T)$ 表达——这是卫材胶接设计"最可操作的一个方程"（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）。
- **熔体流变设定异形截面**：异形截面（trilobal、rectangular、hexalobal、hollow）由喷丝孔形状与**熔体流变**共同决定（源：[[Manufactured Fibre Technology Ch14 Speciality Polyamide and Polyester Yarns]]）。
- **受控流变（CR）处理是 PP 的调级手段**：tacticity、分子量及其分布、共聚单体与 CR 处理共同撑开 PP 的性能范围（源：[[Handbook of Polypropylene and Polypropylene Composites]]）。

## Hygiene Relevance 卫材关联

- **芯体点胶工艺的核心方程**：婴儿抓挠与穿着运动属高速剥离，$\psi(v,T)$ 峰值位置决定"低速不漏、高速不脱层"；热熔胶（POP/EVA/SEBS）中蜡/树脂/弹性体比例调节，本质就是设计 $\psi(v,T)$（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）。
- **以体温流变而非结合强度表征性能**：P&G 热熔胶专利把性能表达为**体温下的流变**而非结合强度数值（源：[[US11878492B2 Tackified Hotmelt Adhesive Composition (P&G)]]）。
- **熔体流变约束工艺窗口**：便指示油墨的 Melt rheology 与缝口几何共同决定可加工性（源：[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]）。
- **PSA 测试条件须严格控制**："conditions under which any pressure-sensitive adhesive is both prepared for testing, then tested, must be rigidly controlled"（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）。

## Open Questions 待补

- 库内只给出命名学定义与元件模型框架，缺"流变学"的完整形式化定义 `[待补]`。
- 库内未给出黏弹性模型参数（ψ、G₀）在具体卫材胶层算例中的标定值 `[待补]`。

## Related Sources 关联来源

- [[Adhesive Handbook Part 2 Fundamental Aspects]]（主要引用来源）
- [[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]]、[[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]]
- [[Handbook of Adhesive Technology Full Report]]、[[Book Review Handbook of Adhesion by Packham]]
- [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]、[[US11878492B2 Tackified Hotmelt Adhesive Composition (P&G)]]
- [[Handbook of Polypropylene and Polypropylene Composites]]、[[Manufactured Fibre Technology Ch14 Speciality Polyamide and Polyester Yarns]]
- [[热熔胶 Hot Melt Adhesive]]、[[Polyolefin Hot Melt Adhesive（聚烯烃热熔胶）]]、[[Styrenic Block Copolymer Hot Melt（SIS-SBS 苯乙烯嵌段共聚物热熔胶）]]、[[APAO（非晶态聚α-烯烃）]]
- [[压敏胶 PSA]]、[[卫材胶黏系统 Hygiene Adhesive Systems]]、[[胶接理论 Adhesion Theories]]、[[胶接热力学 Adhesion Thermodynamics]]、[[断裂力学 Fracture Mechanics]]、[[润湿 Wetting]]、[[层压 Lamination]]

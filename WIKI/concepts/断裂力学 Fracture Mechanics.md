---
type: concept
title: "断裂力学 Fracture Mechanics"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [断裂力学, 胶接强度, 剥离强度, 断裂韧性, 非织造力学]
---

# 断裂力学 Fracture Mechanics

> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**定义待补（引用来源未给出明确定义）** —— 两份引用来源都只把它列为胶接科学的**覆盖主题**，未给出本库口径的定义：断裂力学是胶接参考书 coverage 的一部分（与胶接热力学、表面力、润湿、胶接理论、定量测量并列）（源：[[Book Review Handbook of Adhesion by Packham]]）。

Traceable operational content 可溯源的操作内容: in the adhesion literature it appears as the **fracture-energy formalism behind joint strength** — peel strength decomposed into an intrinsic fracture energy and a viscoelastic dissipation term, `G = G₀·ψ(v,T)`（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）.

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Peel-strength master equation 剥离强度主方程 | G = G₀·ψ(v,T) | [[Adhesive Handbook Part 2 Fundamental Aspects]] |
| Intrinsic fracture energy vs crosslink MW | G₀ = E·g(Mc) | [[Adhesive Handbook Part 2 Fundamental Aspects]] |
| Scaling 标度关系 | G₀ ∝ E² ∝ W_A² | [[Adhesive Handbook Part 2 Fundamental Aspects]] |
| PF + PVA 模式 I 断裂韧性跃升 | **+340 %**，200 → ~700 J/m² | [[Adhesive Handbook Part 2 Fundamental Aspects]] |
| EPI 胶最高韧性 | 900–1000 J/m² | [[Adhesive Handbook Part 2 Fundamental Aspects]] |
| 厚胶层 + 硫橡胶 裂纹引发能 | 900–1200 J/m² | [[Adhesive Handbook Part 2 Fundamental Aspects]] |
| 纤维倾角效应 | 0°→45° 断裂韧性**翻倍**；10–30° 间通常有韧性最小值 | [[Adhesive Handbook Part 2 Fundamental Aspects]] |
| Griffith fracture stress (plane stress) | σ_f = √(2Eγ_s/πa) | [[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]] |
| Crack-tip stress concentration | σ_t = σ₀(1 + 2a/ρ) | [[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]] |
| Stress intensity factor | K = √(πa)·σ | [[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]] |
| Strain-energy release rate | G_Ic = K_Ic²/E | [[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]] |

## Method / Mechanism 方法 / 机理

- **粘弹性耗散而非界面热力学主导强度。** `G = G₀·ψ(v,T)`, and "the value of ψ is usually far higher than that of E and the energy dissipated can then be considered as the major contribution to the adhesion strength G"（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）. ⇒ peel rate 与温度是主变量。
- **柔性胶层通过扩大断裂过程区降峰应力。** "Flexible or semirigid adhesives produce joints having higher short-term strength and fracture toughness compared to rigid adhesives."；柔性胶层扩展 fracture process zone 以降低峰值应力（源：[[Adhesive Handbook Part 2 Fundamental Aspects]] / [[Handbook of Adhesive Technology Full Report]]）.
- **机械互锁可用乘积模型表达。** G = (常数)·(互锁分量)·(界面相互作用分量)；橡胶-织物胶接中 "penetration of the protruding fiber ends into the rubber was the most important parameter"（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）.
- **线弹性断裂力学（LEFM）形式体系。** Griffith 断裂应力、裂尖应力集中 σ_t = σ₀(1+2a/ρ)、应力强度因子 K = √(πa)·σ 与应变能释放率 G_Ic = K_Ic²/E 给出**穿刺与撕破的定量语言**（源：[[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]]）.
- **与胶接理论的关系。** 断裂力学是六大胶接理论体系之外的**强度量化层**：六理论 "each of these theories is valid to some extent … they do not negate each other"（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）.

## Hygiene Relevance 卫材关联

- **芯体点胶的速率-温度窗口。** G = G₀·ψ(v,T) 的峰值位置决定「**低速不漏、高速不脱层**」；热熔胶中蜡/树脂/弹性体比例调节本质就是设计 ψ(v,T)（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）.
- **SAP 层热熔胶到浆纤维的锚固。** 机械互锁是橡胶-织物胶接的主导机理，直接对应 SAP 层热熔胶点到浆纤维的锚固深度（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）.
- **木浆纤维方向性。** 纤维倾角 0°→45° 使断裂韧性翻倍、10–30° 存在韧性最小值 ⇒ 高取向纤维束端头胶接强度最低（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）.
- **湿态失效。** 水浸泡后有机涂层粘附力最高损失 **85 %** ⇒ 耐水解是芯体层合/回渗控制的核心（源：[[Adhesive Handbook Part 2 Fundamental Aspects]]）.
- **非织造布撕裂/穿刺评价。** 非织造布拉伸断裂、撕破、穿刺强度评估落在 stress–strain 体系内，K_Ic / G_Ic 提供断裂力学的定量语言（源：[[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]]）.

## Open Questions 待补

- 本库口径的**形式化定义与适用范围**缺失 `[待补]`。
- LEFM 适用边界：K_Ic / G_Ic 建立在**小范围屈服与线弹性假设**上；非织造布的大变形、纤维拔出与桥联机制不满足该假设，**只能作定性参考**（源：[[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]]）。
- 本库未见卫材专用 K_Ic / G_Ic 实测值 `[待补]`。

## Related Sources 关联来源

- Citing sources 引用来源：[[Adhesive Handbook Part 2 Fundamental Aspects]]、[[Book Review Handbook of Adhesion by Packham]]
- Additional vault pages used 另有正文来源：[[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]]、[[Handbook of Adhesive Technology Full Report]]
- Adjacent concepts 相邻概念：[[胶接理论 Adhesion Theories]]、[[胶接热力学 Adhesion Thermodynamics]]、[[润湿 Wetting]]、[[Surface Tension and Surface Energy]]、[[硅烷偶联剂 Silane Coupling Agent]]、[[压敏胶 PSA]]、[[流变学 Rheology]]
- Application pages 应用页：[[卫材胶黏系统 Hygiene Adhesive Systems]]、[[热熔胶 Hot Melt Adhesive]]、[[SAP（高吸水树脂）]]、[[绒毛浆（Fluff Pulp）]]、[[吸收芯体]]、[[Characterisation, testing and modelling of nonwoven fabrics]]

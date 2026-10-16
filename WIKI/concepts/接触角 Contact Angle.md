---
type: concept
title: "接触角 Contact Angle"
domain: [卫材研发, 表面处理与胶黏剂]
status: growing
updated: 2026-09-30
tags: [接触角, 润湿, 毛细压力, 亲水整理耐久性, 表面能]
---

# 接触角 Contact Angle

> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**定义待补（引用来源未给出明确定义）** —— 本库相关来源页都只把接触角 θ 当作一个**操作量**使用，未给出形式化定义。

Traceable operational role 可溯源的操作定位: contact angle enters the Laplace capillary-pressure term as `P_s = 2γcosθ/r_c`, i.e. it is the surface-chemistry variable that sets the sign and magnitude of capillary pull (源：[[Computational Modeling in Absorbent Technology]]).

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Capillary pressure term | P_s = 2γcosθ/r_c（Laplace） | [[Computational Modeling in Absorbent Technology]] |
| Penetration threshold (zero external pressure) | θ ≥ 90° ⇒ zero penetration | [[Computational Modeling in Absorbent Technology]] |
| Advancing contact angle of water on pure cellulose fibre | 0° | [[The Role of Surfactants]] |
| Groove capillary suction (design-calculation basis) | ≈40–50 kPa at θ→20°, γ ≈ 66 mN/m | [[亲水整理耐久性]] |
| Failure threshold after 2nd/3rd insult | θ 回升 **> 60° ⇒ 沟槽吸力归零** | [[亲水整理耐久性]] |
| Effective contact angle (REL 配方口径) | 140° | [[亲水整理耐久性]] |
| Young's equation (contact angle ↔ surface energy) | cosθ = (γ_S − γ_SL) / γ_L | [[Handbook of Adhesive Technology Full Report]] |

## Method / Mechanism 方法 / 机理

- **θ 通过 cosθ 进入毛细驱动力。** Net driving pressure in a non-wicking medium is ΔP = P_b + P_w + P_s, with P_s = 2γcosθ/r_c; penetration time is then a monotonic function of pore radius, pore depth, contact angle, surface tension, viscosity and external pressure（源：[[Computational Modeling in Absorbent Technology]]）.
- **θ ≥ 90° 是毛细驱动的死区。** "When the contact angle is 90 degrees or greater and external pressure is zero, then there is no penetration of liquid. However, increasing external pressure causes penetration even at contact angles greater than 90 degrees." ⇒ 压力与亲水化是**可互换的两个工程杠杆**（源：[[Computational Modeling in Absorbent Technology]]）.
- **θ 由表面能/吸附控制。** Contact angle is linked to surface energies through Young's equation cosθ = (γ_S − γ_SL)/γ_L; the same source ties Dupré work of adhesion W = γ_S + γ_L − γ_SL to a contact-angle measurement（源：[[Handbook of Adhesive Technology Full Report]]）. Surfactant adsorption on the fibre surface is the practical lever that moves θ（源：[[The Role of Surfactants]]）.
- **θ 会随冲击次数漂移。** The groove-suction figure ≈40–50 kPa is valid only while θ stays near 20°; once θ climbs above 60° after repeated insults the advantage is lost — finish durability is therefore a *contact-angle* specification, not a "hydrophilic" label（源：[[亲水整理耐久性]]）.

## Hygiene Relevance 卫材关联

- **Topsheet / ADL 亲水整理。** Contact angle is the only surface parameter in this set shown to track dryness directly: a less-wetting liner (higher θ) drains liquid more readily than a more-wetting one at equal pore size（源：[[亲水整理耐久性]]）.
- **Shaped / grooved fibres.** The groove capillary benefit is conditional on a low contact angle; the sourcing specification should carry "post-multiple-insult contact angle", not "hydrophilic"（源：[[亲水整理耐久性]]）.
- **Fluff pulp 与绒毛浆。** Pure cellulose is already fully wet at 0° advancing contact angle, so wetting agents buy nothing from cellulose itself — rewetting agents work only against residual hydrophobic extractives（源：[[The Role of Surfactants]]）.
- **吸收建模输入参数。** In penetration-absorbency modelling, contact angle is one of five monotonic input levers; a hydrophilic surface buys back penetration at zero external pressure（源：[[Computational Modeling in Absorbent Technology]]）.

## Open Questions 待补

- 形式化定义缺失：本库来源页未给出接触角本身的定义 `[待补]`。
- 定量曲线缺失：耐久整理在沟槽纤维上的**添加量—接触角—吸力**三者定量曲线未见；整理水平 ±1 档对回渗的实测影响未见（源：[[亲水整理耐久性]]）。
- 接触角与 **回渗/干燥度** 的定量关系未在库内建立；`亲水整理耐久性` 记录的溯源自测为定性对照，未给接触角数值 `[待补]`。

## Related Sources 关联来源

- Citing sources 引用来源：[[Computational Modeling in Absorbent Technology]]、[[The Role of Surfactants]]
- Additional vault pages used 另有正文来源：[[亲水整理耐久性]]、[[Handbook of Adhesive Technology Full Report]]
- Adjacent concepts 相邻概念：[[毛细压力 Capillary Pressure]]、[[Laplace Pressure]]、[[Washburn Equation]]、[[Surface Tension and Surface Energy]]、[[表面活性剂 Surfactant]]、[[润湿剂 Wetting Agent]]、[[再润湿剂 Rewetting Agent]]、[[CMC 临界胶束浓度]]
- Application pages 应用页：[[Groove Capillary Suction]]、[[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]]、[[ADL（导流层）]]、[[绒毛浆（Fluff Pulp）]]、[[SAP（高吸水树脂）]]

---
type: concept
title: "Washburn Equation"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [Washburn, 毛细上升, 芯吸, 多孔介质流动, 吸收动力学, Lucas-Washburn, Rudd 关系]
---

# Washburn Equation

> 📌 **Page completed 2026-09-30** from 4 citing sources（digest 命中 10 页含摘录）。All figures traced to their source pages. Anything not evidenced is marked `[待补]`。

## Definition 定义

定义待补（引用来源未给出 Washburn 方程的完整显式解析式）。

What the digest *does* evidence is its **result form and its theoretical family**：in a porous medium the advancing wicking-front distance obeys **x_v ∝ t^(1/2)**，named the **Washburn / Rudd relation**（源：[[Porous Structure and Liquid Flow Models]]，p. 24, p. 37）；the equation is grouped into Chapter 1 "Porous Structure and Liquid Flow Models" of *Absorbent Technology*, alongside the **Péclet number, Darcy's law, Washburn equation and capillary rise**（源：[[Absorbent Technology]]）。The full explicit form（in terms of γ, θ, μ, r）is `[待补]`。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Wicking-front scaling 芯吸前沿距离 | x_v ∝ t^(1/2)（Washburn / Rudd relation） | [[Porous Structure and Liquid Flow Models]] |
| Wicking-relation pages 页码 | p. 24, p. 37 | [[Porous Structure and Liquid Flow Models]] |
| Capillary pressure 毛细压力 | p_c = 2γcosθ/r | [[Porous Structure and Liquid Flow Models]] |
| Capillary dominance 主导地位 | absorption is driven primarily by capillary pressure；gravity / imposed pressure play only a secondary role（p. 19） | [[Porous Structure and Liquid Flow Models]] |
| Darcy's law 达西定律 | q = −K·∇P，where K = k/μ | [[Porous Structure and Liquid Flow Models]] |
| Unsteady equivalence 非稳态等价性 | under unsteady conditions，flow in porous media is mathematically identical to a diffusion process | [[Porous Structure and Liquid Flow Models]] |
| Diffusivity factor 扩散因子 | F(s) = (k/μΦ)(dp_c/ds)，linking permeability and capillary gradient | [[Porous Structure and Liquid Flow Models]] |
| Hagen–Poiseuille flow vs radius 流量-半径 | flow ∝ r²（Y ×2 → flow ×16） | [[Porous Structure and Liquid Flow Models]] |
| Capillary pressure vs radius 毛细压力-半径 | p_c ∝ 1/r | [[Porous Structure and Liquid Flow Models]] |
| Kozeny–Carman permeability 渗透率 | k ∝ Φ³/(1−Φ)² | [[Porous Structure and Liquid Flow Models]] |
| Capillary pull on a single fibre 单根纤维毛细拉力 | F = γ_LV·cos θ_eq·C（rod / tube model） | [[Surface Tension and Surface Energy]] |
| Young's equation（corrected） | γ_SV = γ_SL + γ_LV cos θ_eq | [[Surface Tension and Surface Energy]] |

## Method / Mechanism 方法 / 机理

- **Theoretical position 理论定位**：the Washburn equation is one of the physical bases of absorption kinetics, alongside the Péclet-number criterion, Darcy's law, capillary pressure and the Kelvin equation, and interfaces directly with simulation（源：[[Absorbent Technology]]）。
- **Relation to Darcy / diffusion 与达西·扩散的关系**：flow in porous media follows Darcy's law（q = −K·∇P）；under unsteady conditions it is mathematically identical to a diffusion process, so the advancing wicking front grows as t^(1/2)（源：[[Porous Structure and Liquid Flow Models]]）。
- **Rate-vs-capacity antagonism 率-容对抗**：bigger pores raise rate（Hagen–Poiseuille: flow ∝ r²）but lower capillary pressure（p_c ∝ 1/r），so capacity falls；the optimum sits mid-range, not at either extreme（源：[[Porous Structure and Liquid Flow Models]]）。
- **Limits of one-dimensional Washburn 一维局限**：excerpt reads "—One-dimensional Washburn is a lowe[原文残缺]"；the same page notes that **pore radius, depth, contact angle, viscosity and external pressure each map monotonically onto penetration time**，so the parameter space can be scanned on a laptop instead of on a pilot line（源：[[Computational Modeling in Absorbent Technology]]）。
- **Pressure and hydrophilisation are substitutes 润湿与压力可互换**：once **θ ≥ 90°**，capillary pull is zero and only imposed pressure breaks the deadlock；conversely a hydrophilic surface buys back penetration at zero pressure（源：[[Computational Modeling in Absorbent Technology]]）。
- **Surface chemistry supplies the micro level 表面化学补微观层**：Chapter 2 replaces the flat-plate sessile drop with a rod/tube model giving the capillary pull on an individual fibre F = γ_LV·cos θ_eq·C, and stresses that Young's equation is a **thermodynamic identity, not a force balance**（源：[[Surface Tension and Surface Energy]]）。

## Hygiene Relevance 卫材关联

- The equation governs **wicking rate and capacity in diaper / incontinence cores**, the physical foundation of absorbent technology（源：[[Porous Structure and Liquid Flow Models]]）。
- Simulation interface 对接口：Washburn / Lucas-Washburn, together with Darcy's law and capillary pressure, forms the physical basis of absorption kinetics and interfaces directly with simulation（源：[[Absorbent Technology]]）。
- Related concepts（navigational）：[[达西定律 Darcy's Law]]、[[毛细压力 Capillary Pressure]]、[[Laplace Pressure]]、[[Hagen-Poiseuille Equation]]、[[接触角 Contact Angle]]、[[孔隙率 Porosity]]、[[渗透率 Permeability]]、[[ADL（导流层）]]、[[吸收芯体]]。
- Related test conventions（navigational；no direct Washburn figures in the digest）：[[Klemm 法]]、[[GATS 重力吸收测试]]、[[Groove Capillary Suction]]、[[时间滞后法 Time Lag Method]]、[[Hygiene Absorption Model]]。

## Open Questions 待补

- **The full explicit Washburn expression and its corrected form in fibrous / nonwoven porous media** —— `[待补]`。
- Boundary conditions where one-dimensional Washburn fails（the excerpt is truncated）——`[原文残缺]`，not guess-repaired。
- The distinction and applicability domains of the Rudd and Washburn relations `[待补]`。
- Parameterisation of the equation in this vault's core C/Q model（values of Φ, r, θ, μ）`[待补]`。

## Related Sources 关联来源

- [[Computational Modeling in Absorbent Technology]]
- [[Fluid Absorption in High Bulk Nonwovens]]
- [[Porous Structure and Liquid Flow Models]]
- [[The Role of Surfactants]]
- [[Absorbent Technology]]
- [[Porous Structure and Liquid Flow Models]]
- [[Surface Tension and Surface Energy]]
- [[达西定律 Darcy's Law]]
- [[毛细压力 Capillary Pressure]]
- [[Laplace Pressure]]
- [[Hagen-Poiseuille Equation]]
- [[接触角 Contact Angle]]
- [[孔隙率 Porosity]]
- [[渗透率 Permeability]]
- [[ADL（导流层）]]
- [[吸收芯体]]
- [[Klemm 法]]
- [[GATS 重力吸收测试]]
- [[Groove Capillary Suction]]
- [[时间滞后法 Time Lag Method]]
- [[Hygiene Absorption Model]]
- [[Absorbent Technology_master_index.csv]]
- [[Absorbent Technology_synthesis]]


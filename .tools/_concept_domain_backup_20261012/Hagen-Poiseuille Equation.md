---
type: concept
title: "Hagen-Poiseuille Equation"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [fluid-mechanics, capillary-flow, absorbency-modelling, porous-media, simulation]
---

# Hagen-Poiseuille Equation

> 📌 **Page completed 2026-09-30** from 5 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）—— 库内来源未给出 Hagen–Poiseuille 的独立定义句，仅以**工作方程**形式记录：在无三维孔网的多孔介质（被建模为均匀圆管束）中，**毛细流动 q = (r_c² / 8μ)(ΔP / L)**，标注为 **Hagen–Poiseuille**（源：[[Computational Modeling in Absorbent Technology]]）。

（中文：无独立定义句；库内只给出圆管黏性流动的工作式 q = (r_c²/8μ)(ΔP/L)。）

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Hagen–Poiseuille capillary flow | **q = (r_c² / 8μ)(ΔP / L)** | [[Computational Modeling in Absorbent Technology]] |
| Net driving pressure it is paired with | **ΔP = P_b + P_w + P_s**（Eq. 1） | [[Computational Modeling in Absorbent Technology]] |
| Capillary pressure (Laplace term) | **P_s = 2γ cos θ / r_c** | [[Computational Modeling in Absorbent Technology]] |
| External-pressure sweep in the worked case | **P_b = 0, 2700, 6200 Pa**（Figs. 2–3） | [[Computational Modeling in Absorbent Technology]] |
| Surface-tension sweep | **γ = 0.01 vs 0.05 N/m**；at 0.05 *"the penetration time is already small enough"*（Fig. 4） | [[Computational Modeling in Absorbent Technology]] |
| Pore depth tested | **up to 100 µm**（Fig. 5） | [[Computational Modeling in Absorbent Technology]] |
| Viscosity sweep | **to 0.05 Pa·s**（Fig. 6） | [[Computational Modeling in Absorbent Technology]] |
| Darcy-law companion | **q = −K·∇P**（porous-media flow） | [[达西定律 Darcy's Law]] |

## Method / Mechanism 方法 / 机理

1. **Where it sits in the absorbency model.** The penetration-absorbency case models a medium with no 3-D pore network (*"the porous medium does not have a three-dimensional network of pores and therefore wicking phenomenon is not as dominant"*) as a **bundle of uniform circular capillaries**; Hagen–Poiseuille gives the flow, Laplace the driving pressure（源：[[Computational Modeling in Absorbent Technology]]）.
2. **Integration gives the design map.** Integrating through thickness **d** yields **penetration time as an explicit function of pore radius, pore depth, contact angle, surface tension, viscosity and external pressure** — i.e. the parameter space can be scanned on a laptop instead of on a pilot line（源：[[Computational Modeling in Absorbent Technology]]）.
3. **Pressure can substitute for hydrophilisation.** *"When the contact angle is 90 degrees or greater and external pressure is zero, then there is no penetration of liquid. However, increasing external pressure causes penetration even at contact angles greater than 90 degrees"*（源：[[Computational Modeling in Absorbent Technology]]、[[接触角 Contact Angle]]）.
4. **One-dimensional treatment is a lower bound, not reality.** *"A porous medium can be considered as a network of pores of myriad shapes and sizes in three-dimension"* — real webs need diffusion-analogy or multi-scale methods whose accuracy *"depends on empirical inputs"*（源：[[Computational Modeling in Absorbent Technology]]、[[Washburn Equation]]）.
5. **Discretisation and closure.** The chapter lists *"finite difference, finite element, finite volume and spectral methods"* and phenomenological turbulence models（k-ε）for the continuous phase（源：[[Computational Modeling in Absorbent Technology]]、[[有限差分法 Finite Difference]]、[[有限元法]]、[[有限体积法]]、[[k-ε 湍流模型]]）.

## Hygiene Relevance 卫材关联

- **Core / SAP penetration formalism.** The same capillary-bundle formalism applies to **SAP particles**（pore radius, applied buttock pressure）and to **hot-melt glue penetration/curing** — one framework, three product domains（源：[[Computational Modeling in Absorbent Technology]]、[[SAP（高吸水树脂）]]）.
- **Material-selection precondition.** Contact angle / wetting index / work of adhesion decide whether a fibre or structure can imbibe liquid at all — the precondition for any Darcy/capillary flow（源：[[达西定律 Darcy's Law]]、[[Computational Modeling in Absorbent Technology]]）.
- **Core modelling interface.** Hagen–Poiseuille sits with Darcy's law, Laplace pressure and Washburn in Chapter 1 *Porous Structure and Liquid Flow Models*, and interfaces directly with the C/Q model and 2D/3D finite-element simulation（源：[[达西定律 Darcy's Law]]、[[Computational Modeling in Absorbent Technology]]）.
- **Neighbouring vault pages**：[[Washburn Equation]]、[[Laplace Pressure]]、[[毛细压力 Capillary Pressure]]、[[接触角 Contact Angle]]、[[CFD 计算流体力学]]、[[虚拟原型 Virtual Prototyping]]（源：[[Computational Modeling in Absorbent Technology]]）.

## Open Questions 待补

- **No standalone prose definition of Hagen–Poiseuille** anywhere in the vault's cited excerpts — only the working equation `[待补]`.
- **Parameterisation of the equation in the vault's own core C/Q model**（values of Φ, r, θ, μ）is listed as open for the sibling Washburn pages（源：[[Computational Modeling in Absorbent Technology]]、[[Porous Structure and Liquid Flow Models]]）.
- **No hygiene-product-specific r_c / L / μ value** is recorded in the vault's excerpt `[待补]`.

## Related Sources 关联来源

- [[Computational Modeling in Absorbent Technology]]（本页主体来源）
- [[Washburn Equation]] · [[达西定律 Darcy's Law]] · [[Laplace Pressure]] · [[毛细压力 Capillary Pressure]] · [[接触角 Contact Angle]]
- [[CFD 计算流体力学]] · [[有限差分法 Finite Difference]] · [[有限元法]] · [[有限体积法]] · [[k-ε 湍流模型]]
- [[Absorbent Technology]] · [[Porous Structure and Liquid Flow Models]] · [[Fluid Absorption in High Bulk Nonwovens]] · [[Characterisation, testing and modelling of nonwoven fabrics]]
- [[SAP（高吸水树脂）]] · [[Stokes Number]] · [[Lagrangian Particle Tracking]] · [[虚拟原型 Virtual Prototyping]]

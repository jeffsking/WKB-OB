---
type: concept
title: "复合膜 Composite Membrane"
domain: [卫材研发, 待归类]
status: growing
updated: 2026-09-30
tags: [composite-membrane, multilayer-film, diffusion, series-resistance, backsheet, laminate]
---

# 复合膜 Composite Membrane

> 📌 **Page completed 2026-09-30** from 5 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义
No standalone formal definition is given in the cited sources → 定义待补（引用来源未给出明确定义）. The vault uses "composite membrane 复合膜" operationally in two senses: (1) a **layered heterogeneous diffusion medium**, i.e. a stack of layers of different transport coefficients（源：[[Diffusion in Heterogeneous Media (Crank Ch.12)]]、[[Diffusion in a Plane Sheet (Crank Ch.4)]]）; and (2) a **multilayer film**, among the direct objects of the film handbook together with backsheets, release films and packaging films（源：[[Handbook of Plastic Films]]）.

## Key Parameters and Data 关键参数与数据
| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Series resistance (slab) 串联阻力（片层） | Σ(lᵢ/Dᵢ) = total resistance | [[Diffusion in a Plane Sheet (Crank Ch.4)]] §4.2.3 |
| Series resistance (general) 通用串联阻力 | 1/R_L = Σ 1/R_Li | [[Diffusion in Heterogeneous Media (Crank Ch.12)]] §12.2(i) |
| Slab form 片层形式 | Σ(lᵢ/Pᵢ) = l/P_total | 同上 §12.2 |
| Cylindrical shell 圆柱壳 | Σ(ln(Rᵢ/Rᵢ₋₁)/Pᵢ) = ln(R_n/R₀)/P_total | 同上 §12.2 |
| Spherical shell 球壳 | Σ((1/Rᵢ₋₁ − 1/Rᵢ)/Pᵢ) = (1/R₀ − 1/R_n)/P_total | 同上 §12.2 |
| D(C) case 变扩散系数情形 | integral diffusion coefficient D̄ᵢ | 同上 §12.2 |
| Adhesive multilayer film 多层复合膜 | up to 7 layers，其中 ≤3 层为胶层 | [[Adhesive Handbook Part 1 History and Information Resources]] |

## Method / Mechanism 方法 / 机理
- **Series-resistance model 串联阻力模型.** The total transport resistance of a multilayer medium is the sum of the layer resistances; each layer contributes independently（源：[[Diffusion in Heterogeneous Media (Crank Ch.12)]]、[[Diffusion in a Plane Sheet (Crank Ch.4)]]）.
- **Three-dimensional generalisation.** Because core layers have different geometries, the model is generalised to slab / cylindrical shell / spherical shell forms（源：[[Diffusion in Heterogeneous Media (Crank Ch.12)]]）.
- **Penetration constant.** Steady-state flux uses P = DS (from the plane-sheet account)（源：[[Diffusion in a Plane Sheet (Crank Ch.4)]]）.
- **Multilayer film build.** A composite film can stack up to 7 layers with up to 3 adhesive layers; compatibilizers are used to solve interlayer delamination / incompatibility（源：[[Adhesive Handbook Part 1 History and Information Resources]]）.

## Hygiene Relevance 卫材关联
- Composite-membrane theory maps directly onto the **diaper core multilayer**: topsheet + (spunbond) ADL + fluff pulp + SAP layer + PP backsheet — total resistance = Σ(lᵢ/Dᵢ)（源：[[Diffusion in Heterogeneous Media (Crank Ch.12)]]、[[Diffusion in a Plane Sheet (Crank Ch.4)]]）.
- The **backsheet** is itself a composite membrane on either route: microporous breathable film + spunbond laminate, or a film-free high-barrier meltblown composite（源：[[底膜 Backsheet]]）.
- The 7-layer / 3-adhesive multilayer film maps to the topsheet–ADL–SAP-lock–backsheet structure, with compatibilizers as an alternative to solving delamination by adhesive selection（源：[[Adhesive Handbook Part 1 History and Information Resources]]）.
- Related concept in the vault: [[时间滞后法 Time Lag Method]] applies the same Σ(lᵢ/Dᵢ) stacking（源：[[时间滞后法 Time Lag Method]]）.

## Open Questions 待补
- No standalone formal definition of "composite membrane" in the cited sources → 定义待补（引用来源未给出明确定义）.
- No measured permeability / resistance value for any named KC composite membrane or backsheet film `[待补]`.

## Related Sources 关联来源
- [[Diffusion in Heterogeneous Media (Crank Ch.12)]]
- [[Diffusion in a Plane Sheet (Crank Ch.4)]]
- [[时间滞后法 Time Lag Method]]
- [[底膜 Backsheet]]
- [[Adhesive Handbook Part 1 History and Information Resources]]
- [[Handbook of Plastic Films]]
- [[吸收芯体]]
- [[Fick 定律]]

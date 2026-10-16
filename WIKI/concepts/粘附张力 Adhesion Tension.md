---
type: concept
title: "粘附张力 Adhesion Tension"
domain: [卫材研发, 表面处理与胶黏剂]
status: growing
updated: 2026-09-30
tags: [surface-energy, adhesion, wetting, surfactant, interfacial-tension, absorbency]
---

# 粘附张力 Adhesion Tension

> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义
The vault gives an **explicit dynamic** form only: in the surfactant chapter, **dynamic adhesion tension** (γSG − γSL)* = γ₂ₗ·(k*/k_water)（源：[[The Role of Surfactants]] p.194）, where γSG/γSL are the solid–gas / solid–liquid interfacial energies and k*/k_water is a diffusivity ratio. A static/equilibrium definition of adhesion tension is **not** stated in the cited sources → 定义待补（引用来源未给出明确定义）.

## Key Parameters and Data 关键参数与数据
| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Dynamic adhesion tension 动态粘附张力 | (γSG − γSL)* = γ₂ₗ·(k*/k_water) | [[The Role of Surfactants]] p.194 |
| Wicking-equivalent tension 等效芯吸张力 σ* | σ* = γ₂ₗ·(k_water/k) | 同上 p.194 |
| Wetting-time law 润湿时间律 | log t_w = A' − B'·log C₂ | 同上 p.205 |
| Tube capillary drive 管内毛细驱动 | F ∝ (γSL − γSV) × TPL length（independent of cross-section） | [[Surface Tension and Surface Energy]] p.95 |
| Rod capillary pull 单纤维毛细拉力 | F = γLV·cos θeq·C | 同上 |

## Method / Mechanism 方法 / 机理
- **Origin term inside Young's equation.** The sibling source states Young's equation γSV = γSL + γLV cos θeq is an **energy identity, "not a force balance"**（源：[[Surface Tension and Surface Energy]]）；the (γSV − γSL) interfacial-energy pair that defines adhesion tension sits inside it.
- **Used as a diagnostic, not a design number.** In the surfactant chapter, dynamic adhesion tension is paired with wicking-equivalent surface tension to read how surfactant adsorption shifts interfacial energies **before equilibrium is reached**（源：[[The Role of Surfactants]] p.194）.
- **Recovered inside the work of adhesion.** WA = γLV + γSV − γSL = γLV(1 + cos θeq), so the adhesion-tension term is one of its two components（源：[[Surface Tension and Surface Energy]]；参见 [[Work of Adhesion]]）.
- **Tube sign convention.** For a tube the driving force is given as (γSL − γSV)，independent of tube cross-section and proportional only to the three-phase-line length（源：[[Surface Tension and Surface Energy]] p.95）.

## Hygiene Relevance 卫材关联
- Adhesion tension is the interfacial-energy bookkeeping behind **urine wetting / penetration into a fibrous core**; the source only uses its dynamic form because urine is multi-component（源：[[The Role of Surfactants]]、[[Surface Tension and Surface Energy]]）.
- Because "urine is not water", equilibrium is not reached and selective adsorption / Marangoni effects complicate capillary behaviour — so the **dynamic** adhesion tension, not the equilibrium value, is what the vault records（源：[[Surface Tension and Surface Energy]]）.
- Feedstock design target stated in the sibling source: diaper-core fibre/water θ < 30°, SAP wet-state θ < 10°（源：[[Surface Tension and Surface Energy]]）.

## Open Questions 待补
- No static/equilibrium definition of adhesion tension is given in the cited sources → 定义待补（引用来源未给出明确定义）.
- No numeric adhesion-tension value for any named KC pulp / SAP / topsheet material is recorded `[待补]`.

## Related Sources 关联来源
- [[The Role of Surfactants]]
- [[Surface Tension and Surface Energy]]
- [[Work of Adhesion]]
- [[Young's Equation]]
- [[表面活性剂 Surfactant]]
- [[润湿 Wetting]]
- [[Nonwoven Lamination]]

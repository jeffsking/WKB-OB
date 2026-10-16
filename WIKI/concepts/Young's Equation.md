---
type: concept
title: "Young's Equation"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [wetting, contact-angle, surface-thermodynamics, capillary, absorbency]
---

# Young's Equation

> 📌 **Page completed 2026-09-30** from 4 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**Young's equation**, as recorded in the vault：**γSV = γSL + γLV cos θeq**（Eq. 18, p. 83）（源：[[Surface Tension and Surface Energy]]）.

The source explicitly overturns the common misreading：**"Young's equation is not a force balance"** — it is a **thermodynamic equation** relating **energies (scalar quantities)**, valid for **acute, obtuse, 90°, and θeq = 0**（源：[[Surface Tension and Surface Energy]]）.

（中文：Young 方程 γSV = γSL + γLV cos θeq（Eq. 18, p. 83）。库内来源强调它是**能量恒等式**，不是力平衡；对锐角、钝角、90° 与 θeq = 0 均成立。）

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Young's equation | **γSV = γSL + γLV · cos θeq**（Eq. 18, p. 83） | [[Surface Tension and Surface Energy]] |
| Work of adhesion (Dupré) | **WA = γLV + γSV − γSL = γLV(1 + cos θeq)** | [[Surface Tension and Surface Energy]] |
| Work of cohesion | **WC = 2γLV** | [[Surface Tension and Surface Energy]] |
| Zero-angle condition | **WA = WC = 2γLV**（complete spreading） | [[Surface Tension and Surface Energy]] |
| Fundamental inequality | **(γSV + γLV) > γSL**（SL interface always forms） | [[Surface Tension and Surface Energy]] |
| Contact-angle span | **0°（full spread）→ 180°（perfectly non-wetting）** | [[Surface Tension and Surface Energy]] |
| Water surface tension（参考常量） | **72.8 dynes/cm at 20 °C**（Harkins & Brown, 1919） | [[Surface Tension and Surface Energy]] |
| Rod capillary pull（几何修正后的驱动力） | **F = γLV · cos θeq · C**（C = fibre circumference, p. 95） | [[Surface Tension and Surface Energy]] |
| Tube capillary drive | **F ∝ (γSL − γSV) × TPL length**；independent of tube cross-section | [[Surface Tension and Surface Energy]] |
| Diaper core fibre / water θ | **< 30° target**（Young + Wenzel） | [[Surface Tension and Surface Energy]] |
| SAP particle θ | **< 10°（wet state）**, θeq = 0 ideal | [[Surface Tension and Surface Energy]] |
| Capillary driving pressure（应用口径） | ΔP = P_b + P_w + P_s，**P_s = 2γcosθ / r_c** | [[接触角 Contact Angle]] |

## Method / Mechanism 方法 / 机理

1. **It is an energy identity, not a force diagram.** The source states：*"Contrary to statements or implications in some of the literature Young's equation is not a force balance. It is a thermodynamic equation showing a valid and easily proved relationship among energies, i.e. scalar quantities."*（源：[[Surface Tension and Surface Energy]]）.
2. **Scope caveat carried by the source**：*"Equation 18 shows an energy equilibrium but tells nothing about the forces or molecular mechanisms that cause the system to approach this equilibrium"* — thermodynamics gives the destination, not the path（源：[[Surface Tension and Surface Energy]]）.
3. **Geometry correction is the business-critical point.** *"The sessile drop on a flat plate is not at all typical of the capillary systems of absorbency. The solid surfaces of absorbency are better modeled either by the exterior of a rod or the interior of a tube"* — hence **stop measuring absorbency on flat plates** and evaluate **fibre-level capillary pull**（源：[[Surface Tension and Surface Energy]]）.
4. **Zero-angle regime dominates real hygiene systems.** θeq = 0 systems are *"the systems most commonly encountered in practice"*; at θeq = 0 → WA = WC = 2γLV, i.e. the liquid fully wets and never beads（源：[[Surface Tension and Surface Energy]]）.
5. **θ ≥ 90° is a dead zone for capillary drive.** *"When the contact angle is 90 degrees or greater and external pressure is zero, then there is no penetration of liquid"* — external pressure becomes the only way in（源：[[接触角 Contact Angle]]）.
6. **Multi-component fluids break the equilibrium assumption.** Urine（salts, proteins, surfactants）makes equilibrium unachievable in practice — selective adsorption and **Marangoni effects** *"can seriously complicate the capillary behavior"*（源：[[Surface Tension and Surface Energy]]、[[Marangoni Effect]]）.

## Hygiene Relevance 卫材关联

- **Core fibre wettability target**：diaper core fibre/water θ **< 30°**（Young + Wenzel）（源：[[Surface Tension and Surface Energy]]）.
- **Adhesive selection is a surface-energy match**：WA = γLV(1 + cos θeq) means glue strength rises monotonically as contact angle falls — adhesive and substrate surface energies must be paired, not chosen independently（源：[[Surface Tension and Surface Energy]]、[[Chemical bonding]]）.
- **Anti-rewet backsheet design law**：a structured surface via Cassie–Baxter lets a modestly hydrophilic polymer behave hydrophobically — the design principle behind anti-rewet backsheet structures（源：[[底膜 Backsheet]]、[[Cassie-Baxter Equation]]）.
- **SAP design implication**：θeq → 0 is the ideal; the vault target is SAP-particle θ **< 10°** in the wet state（源：[[Surface Tension and Surface Energy]]、[[SAP（高吸水树脂）]]）.
- **Wet-wipe surface**：θeq → 0, second-level wetting; WA = γLV(1 + cos θeq)（源：[[Surface Tension and Surface Energy]]）.
- **Neighbouring vault pages**：[[Wenzel Equation]]、[[Cassie-Baxter Equation]]、[[Work of Adhesion]]、[[亲水化 Hydrophilisation]]、[[三相接触线 TPL]]、[[Laplace Pressure]]、[[毛细压力 Capillary Pressure]]（源：[[Surface Tension and Surface Energy]]、[[接触角 Contact Angle]]）.

## Open Questions 待补

- **No roughness factor r is quantified for any real hygiene substrate** in the vault `[待补]`.
- **Parameterisation of Φ, r, θ, μ** for the vault's own core C/Q model is listed as open（源：[[Surface Tension and Surface Energy]]）.
- **Wenzel vs Cassie–Baxter regime boundary**（Wenzel→Cassie transition criterion）is **not** recorded `[待补]`（源：[[Surface Tension and Surface Energy]]）.
- Whether the **< 30° core-fibre target** is a specification or an inference from Young + Wenzel is not stated in the vault's excerpt（源：[[Surface Tension and Surface Energy]]）.

## Related Sources 关联来源

- [[Surface Tension and Surface Energy]]（本页主体来源）
- [[Wenzel Equation]] · [[Cassie-Baxter Equation]] · [[Work of Adhesion]] · [[接触角 Contact Angle]]
- [[Marangoni Effect]] · [[三相接触线 TPL]] · [[Laplace Pressure]] · [[亲水化 Hydrophilisation]] · [[毛细压力 Capillary Pressure]]
- [[底膜 Backsheet]] · [[SAP（高吸水树脂）]] · [[Chemical bonding]]
- [[Absorbent Technology]] · [[Porous Structure and Liquid Flow Models]]
- [[Absorbent Technology_master_index.csv]]
- [[Absorbent Technology_synthesis]]
- [[Introduction to Physical Polymer Science_ch12_report]]


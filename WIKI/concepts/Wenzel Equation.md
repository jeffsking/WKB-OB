---
type: concept
title: "Wenzel Equation"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [wetting, surface-roughness, contact-angle, hydrophilisation, surface-thermodynamics]
---

# Wenzel Equation

> 📌 **Page completed 2026-09-30** from 8 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**Wenzel's roughness relation**, as recorded in the vault：**cos θW = r · cos θY，r > 1**（源：[[Surface Tension and Surface Energy]]）.

The source states its meaning in one line: **roughness and structured surfaces change wetting only by *amplifying the underlying tendency*** — **roughness pushes hydrophilic surfaces more hydrophilic and hydrophobic surfaces more hydrophobic**（源：[[Surface Tension and Surface Energy]]）.

（中文：Wenzel 粗糙度关系 cos θW = r·cos θY（r > 1）；其库内唯一表述是"粗糙与结构化表面只**放大原有倾向**"——亲水更亲水，疏水更疏水。）

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Wenzel (rough) relation | **cos θW = r·cos θY, r > 1** | [[Surface Tension and Surface Energy]] |
| Young's equation it modifies（被修正的方程） | **γSV = γSL + γLV cos θeq**（an **energy** identity, **not** a force balance） | [[Surface Tension and Surface Energy]] |
| Companion composite model | **cos θCB = f1·cos θY + f2·cos 180° = f1(cos θY + 1) − 1** | [[Surface Tension and Surface Energy]] · [[Cassie-Baxter Equation]] |
| Water surface tension（参考常量） | **72.8 dynes/cm at 20 °C**（Harkins & Brown, 1919） | [[Surface Tension and Surface Energy]] |
| Contact-angle span | **0°（full spread）→ 180°（perfectly non-wetting）** | [[Surface Tension and Surface Energy]] |
| Diaper core fibre / water θ | **< 30° target**（Young + Wenzel） | [[Surface Tension and Surface Energy]] |
| SAP particle θ | **< 10°（wet state）**, θeq = 0 ideal | [[Surface Tension and Surface Energy]] |
| Sanitary-pad backsheet, apparent θ | **> 100°**（Cassie–Baxter structure） | [[Surface Tension and Surface Energy]] |
| Rod capillary pull（几何修正后的驱动力） | **F = γLV · cos θeq · C**（C = fibre circumference, p. 95） | [[Surface Tension and Surface Energy]] |
| Tube capillary drive | **F ∝ (γSL − γSV) × TPL length**; independent of tube cross-section | [[Surface Tension and Surface Energy]] |
| Capillary driving pressure（应用口径） | ΔP = P_b + P_w + P_s，**P_s = 2γcosθ / r_c** | [[接触角 Contact Angle]] |

## Method / Mechanism 方法 / 机理

1. **Wenzel is a *multiplier*, not an additive term.** The vault's stated engineering consequence：**"Hydrophilisation is compounding, not additive"** — grafting −OH / −COOH lowers θeq, and **Wenzel then multiplies the gain through roughness**; engineering **both** surface chemistry **and** micro-roughness is **strictly better than either alone**（源：[[Surface Tension and Surface Energy]]）.
2. **Use it against Cassie–Baxter as the opposite branch.** Wenzel（rough homogeneous contact）amplifies the base tendency; Cassie–Baxter（composite / gas-trapping）**inverts** it — *"a structured backsheet beats a chemically hydrophobic one"*, because Cassie–Baxter lets a **modestly hydrophilic polymer behave hydrophobically through geometry — cheaper and more durable than chemistry**, and it is **the design principle behind anti-rewet backsheet structures**（源：[[Surface Tension and Surface Energy]]、[[底膜 Backsheet]]）.
3. **Geometry correction is the business-critical point**：*"The sessile drop on a flat plate is not at all typical of the capillary systems of absorbency"* — absorbency surfaces are better modelled as the **exterior of a rod** or the **interior of a tube**; hence **stop measuring absorbency on flat plates** and evaluate **fibre-level capillary pull**（源：[[Surface Tension and Surface Energy]]）.
4. **Scope caveat carried by the source**：*"Equation 18 shows an energy equilibrium but tells nothing about the forces or molecular mechanisms that cause the system to approach this equilibrium"* — thermodynamics gives the destination, not the path（源：[[Surface Tension and Surface Energy]]）.
5. **Zero-angle regime dominates real hygiene systems**：θeq = 0 systems are *"the systems most commonly encountered in practice"*; at θeq = 0, **WA = WC = 2γLV** so the liquid fully wets and never beads（源：[[Surface Tension and Surface Energy]]）.
6. **Multi-component fluids break the equilibrium assumption**：urine（salts, proteins, surfactants）makes equilibrium unachievable in practice — selective adsorption and **Marangoni effects** *"can seriously complicate the capillary behavior"*（源：[[Surface Tension and Surface Energy]]、[[Marangoni Effect]]）.
7. **θ ≥ 90° is a dead zone for capillary drive**：*"When the contact angle is 90 degrees or greater and external pressure is zero, then there is no penetration of liquid"* — external pressure becomes the only way in（源：[[接触角 Contact Angle]]）.

## Hygiene Relevance 卫材关联

- **Core fibre wettability target**：diaper core fibre/water θ **< 30°**（Young + Wenzel）— i.e. the Wenzel gain is assumed available on a fibrous web, not on a flat film（源：[[Surface Tension and Surface Energy]]）.
- **Anti-rewet backsheet design law**：structured surfaces via Cassie–Baxter, not chemical hydrophobicity — *"cheaper and more durable"*（源：[[底膜 Backsheet]]、[[Cassie-Baxter Equation]]）.
- **Adhesive selection is a surface-energy match**：WA = γLV(1 + cos θeq) means glue strength rises monotonically as contact angle falls; adhesive and substrate surface energies must be paired, not chosen independently（源：[[Surface Tension and Surface Energy]]、[[Work of Adhesion]]、[[Chemical bonding]]）.
- **SAP design implication**：the ideal SAP particle is a **Cassie–Baxter doublet** — a thin hydrophobic shell（wax / siloxane）guarantees dry flowability while the hydrophilic core keeps θeq → 0 for maximum adhesion（源：[[Surface Tension and Surface Energy]]、[[SAP（高吸水树脂）]]）.
- **Wet-wipe surface**：θeq → 0, second-level wetting; WA = γLV(1 + cos θeq)（源：[[Surface Tension and Surface Energy]]）.
- **Neighbouring vault pages**：[[亲水化 Hydrophilisation]]、[[润湿 Wetting]]、[[Laplace Pressure]]、[[三相接触线 TPL]]、[[毛细压力 Capillary Pressure]]（源：[[Surface Tension and Surface Energy]]、[[接触角 Contact Angle]]）.

## Open Questions 待补

- **No roughness factor r is quantified for any real hygiene substrate** in the vault `[待补]`.
- **Parameterisation of Φ, r, θ, μ** for the vault's own core model is listed as open（源：[[Surface Tension and Surface Energy]]）.
- **Wenzel vs Cassie–Baxter regime boundary** (Wenzel→Cassie transition criterion) is **not** recorded `[待补]`（源：[[Surface Tension and Surface Energy]]）.
- Whether the **< 30° core-fibre target** is a specification or an inference from Young + Wenzel is not stated in the vault's excerpt（源：[[Surface Tension and Surface Energy]]）.

## Related Sources 关联来源

- [[Surface Tension and Surface Energy]]（本页原始 Cited-by 来源）
- [[Young's Equation]] · [[Cassie-Baxter Equation]] · [[接触角 Contact Angle]] · [[Work of Adhesion]] · [[Laplace Pressure]]
- [[三相接触线 TPL]] · [[Marangoni Effect]] · [[亲水化 Hydrophilisation]] · [[润湿 Wetting]]
- [[底膜 Backsheet]] · [[SAP（高吸水树脂）]] · [[Chemical bonding]] · [[Hygiene Absorption Model]]
- [[Absorbent Technology]] · [[Absorbent Technology Introduction]] · [[Porous Structure and Liquid Flow Models]] · [[毛细压力 Capillary Pressure]]

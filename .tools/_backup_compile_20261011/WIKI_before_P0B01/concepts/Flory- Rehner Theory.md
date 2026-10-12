---
type: concept
title: "Flory- Rehner Theory"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [SAP, hydrogel, swelling, crosslink-density, flory-rehner, flory-huggins, CRC, simulation]
---

# Flory- Rehner Theory

> 📌 **Page completed 2026-09-30** from 1 citing source, expanded with cross-referenced vault pages. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**Flory–Rehner theory（Flory–Rehner 平衡溶胀理论）** describes the **equilibrium swelling of a cross-linked hydrophilic network**（如 SAP）. An immersed equilibrium gel is subject to only **two opposing forces** — `"the thermodynamic force of mixing and the retractive force of the polymer chains"` — giving **ΔG_total = ΔG_elastic + ΔG_mixing**; an **ionic network adds a ΔG_ionic term**（源：[[Smart Polymers Ch11 Smart Polymer Drug Delivery]]）.

- **Role in the vault**: cross-link density feeds directly into the Flory–Rehner swelling model as a **parameter interface**（源：[[Acrylic-Based Superabsorbent Polymers]]）; see [[交联密度 Crosslink Density]]、[[SAP 溶胀 SAP Swelling]].

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Free-energy balance 自由能平衡 | ΔG_total = ΔG_elastic + ΔG_mixing（ionic networks add ΔG_ionic） | [[Smart Polymers Ch11 Smart Polymer Drug Delivery]] |
| Mc relations Mc 关系式 | Eq. 11.3（neutral network prepared without solvent）; Eq. 11.4（with relaxed volume fraction υ₂,ᵣ） | [[Smart Polymers Ch11 Smart Polymer Drug Delivery]] |
| Network mesh size 网孔尺寸 | ξ = υ₂,ₛ^(−2/3)(2C_n·Mc/M_r)^(1/2)·l | [[Smart Polymers Ch11 Smart Polymer Drug Delivery]] |
| Rubber-elasticity relation 橡胶弹性关系 | τ = (ρRT/Mc)(1 − 2Mc/Mn)(α − α⁻²)(υ₂,ₛ/υ₂,ᵣ)^(1/3) | [[Smart Polymers Ch11 Smart Polymer Drug Delivery]] |
| Network-tightness rule 网络松紧规律 | lower Mc ⇒ tighter network, higher modulus, **slower uptake** | [[Smart Polymers Ch11 Smart Polymer Drug Delivery]] |
| Salt-correction equilibrium capacity 盐修正平衡容量（v8） | Q_eq = 21.2 g/g（Q0 = 38.0 g/g, C_salt = 0.15 mol/L, C_half = 0.18 mol/L, γ = 1.3）⇒ urine ≈ 56% of pure water | [[2D Absorption Model v8 Simulation Report（二维吸收模型 v8 仿真报告）]] |
| Flory–Rehner–Donnan equilibrium capacity（v11） | Q_eq = 26.6 g/g | [[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]] |
| v11 solving inputs v11 求解输入 | χ = 0.48; ν_e = 800 mol/m³; G ≈ 1.98 MPa; f_ion = 0.85; ρ_p = 1400 kg/m³; M_mono = 94 g/mol; C_salt = 0.15 mol/L (0.9% NaCl); T = 298.15 K | [[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]] |
| v11 solving route 求解方式 | Newton–Raphson for φ_p*, then Q_eq = 1/φ_p* − 1 | [[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]] |

## Method / Mechanism 方法 / 机理

- **Two-force balance**: mixing thermodynamics pushes solvent in; chain retraction pulls back; equilibrium is where they balance（源：[[Smart Polymers Ch11 Smart Polymer Drug Delivery]]）.
- **Rubber-elasticity back-out**: tensile testing recovers the equilibrium modulus and, via the τ relation, **backs out Mc**（源：[[Smart Polymers Ch11 Smart Polymer Drug Delivery]]）.
- **Osmotic pressure form（v11）**: Π_mix + Π_el + Π_ion = P_ext, with Π_mix = −(RT/V_w)[ln(1−φ_p) + φ_p + χ·φ_p²]（Flory–Huggins mixing）（源：[[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]）.
- **SAP design as a mesh-size problem**: ξ and Mc are the proper language for the **free-swell vs. gel-strength trade-off**; map ξ against fluid-uptake rate to select SAP grade per layer（acquisition vs. anti-gel-blocking）（源：[[Smart Polymers Ch11 Smart Polymer Drug Delivery]]）.

## Hygiene Relevance 卫材关联

- **SAP capacity must be salt-corrected**: urine swelling is only ~56% of pure-water swelling — **a required correction, not optional**, for capacity calculation（源：[[2D Absorption Model v8 Simulation Report（二维吸收模型 v8 仿真报告）]]）.
- **Model vs. measured口径不同**: the v8 report's **Q_eq = 21.2 g/g is computed by the Flory-Rehner thermodynamic model**, which is **not the same口径 as measured CRC**（源：[[2D Absorption Model v8 Simulation Report（二维吸收模型 v8 仿真报告）]]）; see [[SAP性能指标（CRC AUL GBP Vortex）]].
- Feeds the REL project's SAP formulation playbook via cross-link density as the pivotal parameter（源：[[Acrylic-Based Superabsorbent Polymers]]）.
- Related pages: [[交联密度 Crosslink Density]] · [[SAP 溶胀 SAP Swelling]] · [[Donnan 溶胀]] · [[Gel Blocking（凝胶阻塞）]] · [[Cross-linked Cellulose and Its Derivatives]] · [[水凝胶 Hydrogel]] · [[SAP（高吸水树脂）]].

## Open Questions 待补

- **口径并列不裁决**: Flory-Rehner curve gives 0.15 mol/L → Q_eq = 21.5 g/g while the parameter table computes 21.2 g/g（差 0.3 g/g）— both registered, not adjudicated（源：[[2D Absorption Model v8 Simulation Report（二维吸收模型 v8 仿真报告）]]）`[待补]`.
- No vault-recorded experimental（measured）swelling dataset matched to a Flory–Rehner Mc value for a specific SAP grade `[待补]`.

## Related Sources 关联来源

- [[Acrylic-Based Superabsorbent Polymers]]（cited-by）
- [[Smart Polymers Ch11 Smart Polymer Drug Delivery]]
- [[2D Absorption Model v8 Simulation Report（二维吸收模型 v8 仿真报告）]]
- [[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]
- [[交联密度 Crosslink Density]]
- [[SAP 溶胀 SAP Swelling]]
- [[Cross-linked Cellulose and Its Derivatives]]

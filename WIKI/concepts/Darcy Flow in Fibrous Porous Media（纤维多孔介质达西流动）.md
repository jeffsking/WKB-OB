---
type: concept
title: "Darcy Flow in Fibrous Porous Media（纤维多孔介质达西流动）"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [porous-media, Darcy, capillary-flow, absorbent-core, permeability]
---

# Darcy Flow in Fibrous Porous Media（纤维多孔介质达西流动）
> 📌 **Page completed 2026-09-30** from 6 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义
The governing relation for flow in porous media **as used in the vault**: **q = −K·∇P**, with the conduction coefficient **K = k/μ** (k = permeability, μ = fluid viscosity) — flow rate proportional to the pressure gradient（源：[[Porous Structure and Liquid Flow Models]]）. In absorbent systems the driving force is not an external pressure but **capillary pressure**, with gravity or applied load only secondary（源：[[Porous Structure and Liquid Flow Models]]）.

## Key Parameters and Data 关键参数与数据
| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Darcy's law 达西定律 | **q = −K·∇P**; **K = k/μ** | [[Porous Structure and Liquid Flow Models]] |
| Capillary driving pressure 毛细驱动压 | **p_c = 2γcosθ/r**（γ = surface tension, θ = contact angle, r = pore radius） | [[Porous Structure and Liquid Flow Models]] |
| Unsteady (diffusion) form 非稳态扩散式 | **∂s/∂t = ∇·[F(s)∇s]**, with **F(s) = (k/μΦ)(dp/ds)**（Φ = porosity） | [[Porous Structure and Liquid Flow Models]] |
| Wicking-front scaling 芯吸前沿标度 | **x_v ∝ t^(1/2)** — the Washburn / Rudd relation | [[Washburn Equation]] |
| Material-level k, Φ for fluff / nonwoven / SAP 实测值 | **not given in the vault**（库内未给出） | [[达西定律 Darcy's Law]] |

## Method / Mechanism 方法 / 机理
- **Steady flow** follows Darcy's law (q = −K·∇P); **unsteady flow in a porous medium is mathematically equivalent to a diffusion / heat-conduction process** — "Unsteady flow in a porous medium is similar to a diffusion process ... or a heat conduction process"（源：[[Porous Structure and Liquid Flow Models]]）.
- The unsteady control equation ∂s/∂t = ∇·[F(s)∇s] carries the diffusion factor F(s) = (k/μΦ)(dp/ds)（源：[[Porous Structure and Liquid Flow Models]]）.
- A **surface-chemistry precondition** must be met first: contact angle / wetting index / work of adhesion decide whether the fibre and structure can take up liquid at all（源：[[Absorbent Technology]]）.

## Hygiene Relevance 卫材关联
- **Core-modelling interface 芯体建模接口**: Darcy's law is a core building block of Ch.1 *Porous Structure and Liquid Flow Models*, connecting directly to core uptake-kinetics modelling; Ch.3 (*Fluid Absorption in High Bulk Nonwovens*) supplies the uptake-kinetics / C–Q model and Ch.4 (*Computational Modeling in Absorbent Technology*) the 2D/3D numerical (FE) simulation（源：[[Absorbent Technology]]）.
- Nonwovens are treated as porous media; Darcy's law is listed among their characterisation/modelling concepts（源：[[Absorbent Technology]]）.
- Capacity is set by pore **volume** ([[Specific Air Volume]]), while rate is set by pore **size** (Hagen–Poiseuille, flow ∝ r²)（源：[[Specific Air Volume]]）.

## Open Questions 待补
- **No material-level permeability / porosity values**: the vault gives the formulas but **no measured k, Φ for fluff pulp / nonwoven / SAP layers**（源：[[达西定律 Darcy's Law]]）.
- Applicability ceiling: no Reynolds-number limit or Forchheimer-correction trigger is given（源：[[达西定律 Darcy's Law]]）.
- Fluid-property term: μ appears only inside K = k/μ; **no viscosity values for urine / blood / simulant** are given（源：[[达西定律 Darcy's Law]]）.
- No vault record applies Darcy's law directly to **line process parameters** (add-on, embossing) — it is a theoretical interface, not a process spec（源：[[达西定律 Darcy's Law]]）.

## Related Sources 关联来源
- [[Differentiable CFD and AI Surrogate Solvers（可微分 CFD 与 AI 代理求解器）]]（原引用来源）
- [[达西定律 Darcy's Law]]、[[Porous Structure and Liquid Flow Models]]、[[Porous Structure and Liquid Flow Models]]、[[Washburn Equation]]、[[Absorbent Technology]]
- Adjacent pages 相邻页：[[渗透率 Permeability]]、[[孔隙率 Porosity]]、[[Hagen-Poiseuille Equation]]、[[Specific Air Volume]]、[[接触角 Contact Angle]]

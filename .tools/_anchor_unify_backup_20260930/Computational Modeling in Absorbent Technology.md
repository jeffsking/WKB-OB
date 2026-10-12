---
type: source
title: "Computational Modeling in Absorbent Technology"
source_type: book
source_path: RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Absorbent Technology (Chatterjee & Gupta)/chapters/Absorbent Technology_ch04_report.md.md
original_link: ""
date_published: 2002
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
author: "Sach Kangovi (Simutel Associates, Princeton Junction NJ)"
edition: "2nd"
publisher: "Elsevier (Academic Press) Science B.V."
year: 2002
isbn: ""
original_language: "EN"
parent_book: "[[Absorbent Technology]]"
key_claims:
  - "'Modeling, based on sound governing laws, is accurate, cost effective and efficient' — modeling can replace expensive parametric experiments (e.g. building multiple web-forming machines) and shorten time to market."
  - "Penetration absorbency collapses to a solvable 1-D capillary-bundle problem: net pressure ΔP = P_b + P_w + P_s with P_s = 2γcosθ/r_c, giving penetration time as a function of pore radius, depth, contact angle, surface tension, viscosity and external pressure."
  - "θ ≥ 90° with zero external pressure means zero penetration; 'increasing external pressure causes penetration even at contact angles greater than 90 degrees' — wetting and pressure are interchangeable levers."
  - "1-D Washburn is inadequate for real webs: 'a porous medium can be considered as a network of pores of myriad shapes and sizes in three-dimension' — 3-D behaviour needs diffusion-analogy or multi-scale methods whose accuracy 'depends on empirical inputs'."
  - "Airlaid web-forming is a two-phase turbulent particle-dynamics problem; CFD + Lagrangian tracking is the only way to see fibre trajectories, and 'computations proved to peerless in visualizing particle motion, which could not be visualized by experiments'."
  - "Phase coupling is mandatory, not optional: 'coupling does have a significant influence on the particle trajectories ... it is important to include coupling despite the fact that it increases computation time considerably.'"
pages_linked: ["[[Absorbent Technology]]", "[[达西定律 Darcy's Law]]", "[[Washburn Equation]]", "[[Hagen-Poiseuille Equation]]", "[[Laplace Pressure]]", "[[CFD 计算流体力学]]", "[[有限体积法]]", "[[Stokes Number]]", "[[气铺 Airlaid]]", "[[Characterisation, testing and modelling of nonwoven fabrics]]", "[[SAP（高吸水树脂）]]"]
---

# Computational Modeling in Absorbent Technology

## One-line Position 一句话定位

Chapter 4 (pp. 146–165; author Sach Kangovi, Simutel Associates) is the virtual-prototyping chapter: two worked cases — penetration absorbency and airlaid web-forming — demonstrate that physics-based modeling delivers parameter sensitivity unobtainable in the lab, at a fraction of the cost, and closes the loop with experimental validation (high-speed video, Fiberscope/Videoimagescope, static-pressure probes).（中文：本章以"渗透吸收"与"气流成网"两个实证案例论证基于物理定律的建模在精度、成本与效率上的优势，并以实验验证闭环，是吸收材料"虚拟原型"的方法论基础。）

## Summary 摘要

- **The value claim.** "Computational modeling, when applicable, is a powerful and cost-effective tool to study a problem with considerable accuracy in a short time," and it is "far more convenient way of investigation than experiments" — chiefly because experiments "would require building many such expensive machines".
- **Case A — Penetration absorbency.** A medium with no 3-D pore network ("the porous medium does not have a three-dimensional network of pores and therefore wicking phenomenon is not as dominant") is modelled as a bundle of uniform circular capillaries. Net driving pressure ΔP = P_b + P_w + P_s, with P_s = 2γcosθ/r_c (Laplace) and q = (r_c²/8μ)(ΔP/L) (Hagen–Poiseuille); integrating through thickness d yields penetration time as an explicit function of pore radius, pore depth, contact angle, surface tension, viscosity and external pressure.
- **The contact-angle threshold.** "When the contact angle is 90 degrees or greater and external pressure is zero, then there is no penetration of liquid. However, increasing external pressure causes penetration even at contact angles greater than 90 degrees."
- **Case B — Airlaid web-forming (pneumophoresis).** Governing set: mass ∂ρ/∂t + ∇·(ρU) = 0, Navier–Stokes momentum, energy, ideal gas, plus a Lagrangian particle force balance d/dt(U_p) = F(U − U_p + u') − g + s with drag F = 18μC_DRe/(ρ_p D_p²).
- **Discretisation and closure.** "Finite difference, finite element, finite volume and spectral methods"; eddy viscosity from "phenomenological turbulence models ... one of the popularly used turbulence models is called k-e model". Particle behaviour hinges on the Stokes number — "the ratio of particle kinetic energy and work done against viscous drag" — and wall impact on the coefficient of restitution.
- **Coupling is non-optional.** Coupling continuous and dispersed phases "does have a significant influence on the particle trajectories".
- **Validation.** Penetration: surfactant-modified contact angle, multi-liquid viscosity sweeps, materials of differing pore size. Webber: multi-tube manometer (0.01 in-water resolution), Fiberscope (11 mm, 120°/40° fields), Videoimagescope (12.6 mm, CCD), Kodak Ektapro 1000 at 125–6000 fps — "Experimental results compared extremely well with the trends shown by modeling."
- **Visualization is engineering, not cosmetics.** "Numerical solutions of equation 3 usually generate large quantities of data and therefore a good scientific data visualization capability is essential in order to derive meaningful conclusions from voluminous data."

## Key Numbers & Conclusions 提炼数字与结论

| 项目 Item | 数值 / 结论 Value / Conclusion | 备注 Note |
|---|---|---|
| Net driving pressure | ΔP = P_b + P_w + P_s | Eq. 1 |
| Capillary pressure | P_s = 2γcosθ/r_c | Laplace |
| Capillary flow | q = (r_c²/8μ)(ΔP/L) | Hagen–Poiseuille |
| External pressure sweep | P_b = 0, 2700, 6200 Pa | Figs. 2–3 |
| Surface tension sweep | γ = 0.01 vs 0.05 N/m; at 0.05 "the penetration time is already small enough" | Fig. 4 |
| Pore depth tested | up to 100 µm | Fig. 5 |
| Viscosity sweep | to 0.05 Pa·s | Fig. 6 |
| Webber inlet pressure | 1.25 kPa below atmosphere | — |
| Webber outlet suction | 2.49 kPa below atmosphere | — |
| Air velocity profile | inlet ~30 m/s → throat 90 m/s → outlet ~5 m/s | Fig. 10 |
| Turbulence intensity | inlet 5%, max ~9% | — |
| Manometer resolution | 0.01 inches of water | — |
| Typical pressure profile | inlet 5 in-water below atm → 30 in-water pre-fibrizer → ~20 in-water near outlet | — |
| Fiberscope | 11 mm OD; 120° and 40° fields | — |
| Videoimagescope | 12.6 mm OD; built-in CCD, remotely movable | — |
| Lighting | 300 W continuous, 3000 flashes/min, 1 W stroboscopic | — |
| Frame rate | 125–6000 fps (Ektapro 1000) | — |
| Wicking-equivalent caveat | 3-D webs need diffusion analogy; "Accuracy of this method depends on empirical inputs" | — |

## Key Claims 关键论断

- **Model before you spin.** Pore radius, depth, contact angle, viscosity and external pressure each map monotonically onto penetration time — the parameter space can be scanned on a laptop instead of on a pilot line.
- **Pressure can substitute for hydrophilisation.** Once θ ≥ 90°, capillary pull is zero and only imposed pressure breaks the deadlock; conversely a hydrophilic surface buys back penetration at zero pressure. The two are engineering substitutes.
- **One-dimensional Washburn is a lower bound, not a model of reality.** Real webs are 3-D pore networks; any diffusion-analogy solution inherits empirical inputs, so modelled web absorption should be read as trend, not magnitude.
- **Airlaid quality is fundamentally a trajectory problem.** Fibre distribution uniformity — hard to measure and impossible to see — is the quantity CFD actually resolves; it is the only instrument that can show trajectories.
- **Coupling cost is not optional cost.** Uncoupled CFD under-resolves dense fibre loading; the extra compute is the price of correctness, not overhead.
- **The validation protocol is transferable.** Pressure profiles + high-speed capture + optical fibre probes are the concrete recipe; a modelling capability without this validation harness is unfalsifiable.
- **Strategic read-across.** The same penetration formalism applies to SAP particles (pore radius, applied buttock pressure) and to hot-melt glue penetration/curing — one framework, three product domains.

## Related Pages 关联页面

- 父书：[[Absorbent Technology]]
- 概念：[[达西定律 Darcy's Law]]、[[Washburn Equation]]、[[Hagen-Poiseuille Equation]]、[[Laplace Pressure]]、[[毛细压力 Capillary Pressure]]、[[接触角 Contact Angle]]
- 方法：[[CFD 计算流体力学]]、[[Navier-Stokes Equation]]、[[有限差分法 Finite Difference]]、[[有限元法]]、[[有限体积法]]、[[k-ε 湍流模型]]、[[Stokes Number]]、[[Lagrangian Particle Tracking]]、[[虚拟原型 Virtual Prototyping]]
- 设备/工艺：[[气铺 Airlaid]]、[[Fiberscope]]、[[Videoimagescope]]
- 相邻章节：[[Porous Structure and Liquid Flow Models]]、[[Fluid Absorption in High Bulk Nonwovens]]、[[Characterisation, testing and modelling of nonwoven fabrics]]

## Source 原文

- 本地路径 Local path：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Absorbent Technology (Chatterjee & Gupta)/chapters/Absorbent Technology_ch04_report.md.md`
- 原文链接 Original link：

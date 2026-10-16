---
type: concept
title: "虚拟原型 Virtual Prototyping"
domain: [卫材研发, 待归类]
status: growing
updated: 2026-09-30
tags: [virtual-prototyping, computational-modeling, simulation, absorbent, CFD]
---

# 虚拟原型 Virtual Prototyping

> 📌 **Page completed 2026-09-30** from 4 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

Physics-based **computer modelling used in place of physical prototypes** to design and study absorbent structures. Within the absorbent-technology corpus it is the subject of the dedicated virtual-prototyping chapter, which argues that modelling delivers parameter sensitivity unobtainable in the lab at a fraction of the cost（源：[[Computational Modeling in Absorbent Technology]]）.

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Chapter anchor 章节定位 | Ch.4 (pp. **146–165**; author Sach Kangovi, Simutel Associates) = the virtual-prototyping chapter | [[Computational Modeling in Absorbent Technology]] |
| Demonstrated cases 实证案例 | **Penetration absorbency** and **airlaid web-forming** | [[Computational Modeling in Absorbent Technology]] |
| Value proposition 价值主张 | Parameter sensitivity unobtainable in the lab, at a fraction of the cost | [[Computational Modeling in Absorbent Technology]] |
| Cost/efficiency rationale 成本效率论据 | Modelling is "a powerful and cost-effective tool to study a problem with considerable accuracy in a short time"; physical experiments "would require building many such expensive machines" | [[Hygiene Absorption Model]] |
| Validation loop 验证闭环 | High-speed video, Fiberscope / Videoimagescope, static-pressure probes | [[Computational Modeling in Absorbent Technology]] |
| Precision gate (rewet) 精度门槛 | Must detect differences of **0.03%** of total liquid volume; validated models "likely not accurate enough" | [[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]、[[Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）]] |
| Deployment gate 部署门槛 | ALBA may be useful but must be **validated with GRIFFIN experiments** before scheduling; added to the Virtual R&D bullpen | [[Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）]] |

## Method / Mechanism 方法 / 机理

- **Physics-based modelling → parameter sensitivity.** Two worked cases (penetration absorbency and airlaid web-forming) demonstrate that a physics-based model exposes sensitivities that a lab test matrix cannot reach economically（源：[[Computational Modeling in Absorbent Technology]]）.
- **Experimental closure.** The model is closed with experiment — high-speed video, Fiberscope/Videoimagescope borescope imaging and static-pressure probes — so predictions are tied to a physical benchmark（源：[[Computational Modeling in Absorbent Technology]]）.
- **Precision-before-deployment discipline.** For rewet prediction the bar is a 0.03% (of total liquid volume) resolution, which the vault flags as beyond currently validated models; ALBA is therefore gated behind GRIFFIN experimental validation rather than scheduled directly（源：[[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]、[[Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）]]）.

## Hygiene Relevance 卫材关联

- **Absorbent-core design tool.** Virtual prototyping predicts penetration/absorbency behaviour for core and nonwoven layers, reducing the need to build expensive physical test machines（源：[[Computational Modeling in Absorbent Technology]]、[[Hygiene Absorption Model]]）.
- **Rewet programme gate.** The rewet work-stream treats simulation as a candidate method but binds it to a physical experiment benchmark and a stated resolution target before it enters the Virtual R&D schedule（源：[[Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）]]）.

## Open Questions 待补

- The 0.03% rewet resolution is currently unmet — "likely not accurate enough"; numerical-diffusion / grid-convergence qualification is required (`[待补]`)（源：[[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]）.
- Which specific absorbency metrics the two worked cases validated, and against what tolerance: not given in the vault.
- Timeline/ownership of the ALBA–GRIFFIN validation loop: not stated beyond "Virtual R&D bullpen".

## Related Sources 关联来源

- [[Computational Modeling in Absorbent Technology]]
- [[Hygiene Absorption Model]]
- [[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]
- [[Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）]]
- [[CFD 计算流体力学]]
- [[达西定律 Darcy's Law]]
- [[Absorbent Technology]]
- [[Fiberscope]]
- [[Videoimagescope]]

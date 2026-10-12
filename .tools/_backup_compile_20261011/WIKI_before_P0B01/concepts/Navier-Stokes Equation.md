---
type: concept
title: "Navier-Stokes Equation"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [fluid-mechanics, cfd, airlaid-web-forming, porous-media, simulation]
---

# Navier-Stokes Equation

> 📌 **Page completed 2026-09-30** from 5 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）—— 库内来源未给出 Navier–Stokes 的独立定义句；它出现在**气流成网（airlaid web-forming / pneumophoresis）**案例的**支配方程组**中，作为**连续相的动量方程**，与质量守恒 ∂ρ/∂t + ∇·(ρU) = 0、能量方程、理想气体方程并列（源：[[Computational Modeling in Absorbent Technology]]）。

（中文：无独立定义句；库内仅作为气流成网 CFD 支配方程组的**动量方程**出现，与质量、能量、理想气体方程并列。）

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Governing set (airlaid case) | **mass ∂ρ/∂t + ∇·(ρU) = 0 + Navier–Stokes momentum + energy + ideal gas** | [[Computational Modeling in Absorbent Technology]] |
| Coupled Lagrangian particle balance | **d/dt(U_p) = F(U − U_p + u') − g + s** | [[Computational Modeling in Absorbent Technology]] |
| Particle drag term | **F = 18μ C_D Re / (ρ_p D_p²)** | [[Computational Modeling in Absorbent Technology]] |
| Air velocity profile | inlet **~30 m/s** → throat **90 m/s** → outlet **~5 m/s**（Fig. 10） | [[Computational Modeling in Absorbent Technology]] |
| Turbulence intensity | inlet **5%**, max **~9%** | [[Computational Modeling in Absorbent Technology]] |
| Discretisation methods named | finite difference, finite element, finite volume, spectral | [[Computational Modeling in Absorbent Technology]] |
| Turbulence closure | phenomenological models — *"one of the popularly used turbulence models is called k-e model"* | [[Computational Modeling in Absorbent Technology]]、[[k-ε 湍流模型]] |
| Particle-behaviour criterion | **Stokes number** — *"the ratio of particle kinetic energy and work done against viscous drag"* | [[Computational Modeling in Absorbent Technology]]、[[Stokes Number]] |

## Method / Mechanism 方法 / 机理

1. **Role in the solver.** In the airlaid case, Navier–Stokes supplies the **continuous-phase（air）momentum** while a **Lagrangian particle force balance** tracks the dispersed fibres; the two phases must be solved together（源：[[Computational Modeling in Absorbent Technology]]、[[Lagrangian Particle Tracking]]）.
2. **Coupling is mandatory, not optional.** *"coupling does have a significant influence on the particle trajectories ... it is important to include coupling despite the fact that it increases computation time considerably."* — uncoupled CFD under-resolves dense fibre loading（源：[[Computational Modeling in Absorbent Technology]]）.
3. **Discretisation and closure.** The chapter lists *"finite difference, finite element, finite volume and spectral methods"* and eddy-viscosity turbulence models（the k-ε model）as the closure route（源：[[Computational Modeling in Absorbent Technology]]、[[有限差分法 Finite Difference]]、[[有限元法]]、[[有限体积法]]）.
4. **Airlaid quality is a trajectory problem.** Fibre-distribution uniformity — hard to measure and impossible to see — is what CFD resolves: *"computations proved to peerless in visualizing particle motion, which could not be visualized by experiments"*（源：[[Computational Modeling in Absorbent Technology]]、[[CFD 计算流体力学]]）.
5. **Validation harness.** Pressure profiles + high-speed capture + optical fibre probes: multi-tube manometer（0.01 in-water）, **Fiberscope**（11 mm, 120°/40°）, **Videoimagescope**（12.6 mm CCD）, **Kodak Ektapro 1000 at 125–6000 fps**（源：[[Computational Modeling in Absorbent Technology]]、[[Fiberscope]]、[[Videoimagescope]]）.

## Hygiene Relevance 卫材关联

- **Directly a hygiene process model.** The case is **airlaid web forming** — the process behind airlaid absorbent cores and 无尘纸 structures — so Navier–Stokes here is the momentum model of a real core-manufacturing step（源：[[Computational Modeling in Absorbent Technology]]、[[气铺 Airlaid]]）.
- **Model before you spin.** *"Modeling, based on sound governing laws, is accurate, cost effective and efficient"* — modelling can replace expensive parametric experiments（e.g. building multiple web-forming machines）and shorten time to market（源：[[Computational Modeling in Absorbent Technology]]、[[虚拟原型 Virtual Prototyping]]）.
- **Modelling interface for absorbent materials.** This chapter is the "virtual prototyping" anchor of *Absorbent Technology*; it closes the loop with experimental validation for both penetration absorbency and airlaid forming（源：[[Computational Modeling in Absorbent Technology]]、[[Absorbent Technology]]）.
- **Neighbouring vault pages**：[[Computational Modeling in Absorbent Technology]]、[[CFD 计算流体力学]]、[[Stokes Number]]、[[Lagrangian Particle Tracking]]、[[达西定律 Darcy's Law]]、[[Hagen-Poiseuille Equation]]（源：[[Computational Modeling in Absorbent Technology]]）.

## Open Questions 待补

- **No standalone prose definition of the Navier–Stokes equation** in the vault's cited excerpts — only its role in the governing set `[待补]`.
- **No mesh, solver or turbulence-model validation error** for a real airlaid line is recorded in the vault's excerpt `[待补]`.
- **Fibre-level boundary conditions**（wall impact via coefficient of restitution）are named but not parameterised for hygiene fibres（源：[[Computational Modeling in Absorbent Technology]]）.

## Related Sources 关联来源

- [[Computational Modeling in Absorbent Technology]]（本页主体来源）
- [[CFD 计算流体力学]] · [[k-ε 湍流模型]] · [[有限差分法 Finite Difference]] · [[有限元法]] · [[有限体积法]]
- [[Stokes Number]] · [[Lagrangian Particle Tracking]] · [[虚拟原型 Virtual Prototyping]] · [[气铺 Airlaid]]
- [[Fiberscope]] · [[Videoimagescope]] · [[达西定律 Darcy's Law]] · [[Hagen-Poiseuille Equation]] · [[Washburn Equation]]
- [[Absorbent Technology]] · [[Porous Structure and Liquid Flow Models]] · [[Fluid Absorption in High Bulk Nonwovens]] · [[Characterisation, testing and modelling of nonwoven fabrics]]

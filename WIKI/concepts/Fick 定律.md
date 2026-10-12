---
type: concept
title: "Fick 定律"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [diffusion, fick, transport, SAP, absorbent-core, modelling, Crank]
---

# Fick 定律

> 📌 **Page completed 2026-09-30** from 9 citing sources in the vault. All figures traced to their source pages. Anything not evidenced in the vault is marked `[待补]`.

## Definition 定义

Diffusion is the process by which matter is transported from one part of a system to another as a result of **random molecular motion**（扩散是分子随机运动驱动的物质从系统一部分传输到另一部分的过程）（源：[[Diffusion Equations (Crank Ch.1)]]）. **Fick's first law** states the transfer rate is proportional to the concentration gradient, `F = −D dC/dx`, by analogy with heat conduction (Fourier's law). **Fick's second law**, `∂C/∂t = D ∂²C/∂x²`（一维恒 D）, is described as **the single core PDE** of the whole [[Mathematics of Diffusion]] reference, on which every chapter builds. Fick's law is the sole core assumption underlying SAP swelling kinetics, absorbent-core liquid uptake, wet-migration and wet-wipe uniformity models in this vault.

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Fick's first law 第一定律 | `F = −D dC/dx`（flux ∝ concentration gradient） | [[Diffusion Equations (Crank Ch.1)]] |
| Fick's second law（1D, const D） | `∂C/∂t = D ∂²C/∂x²` — the single core PDE | [[Diffusion Equations (Crank Ch.1)]] |
| D(C) variation in SAP SAP 的 D(C) 跨度 | spans **3–4 orders of magnitude** after swelling（稀溶液中 D≈常数） | [[Diffusion Equations (Crank Ch.1)]] |
| Time-lag method 时间滞后法 | `L = l²/6D` — industry standard (Daynes 1920, Barrer 1951) | [[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]] |
| Series-resistance model 串联阻力模型 | `Σ(lᵢ/Pᵢ)` — per-layer mass-transfer resistance | [[Diffusion in Heterogeneous Media (Crank Ch.12)]] |
| Effective-D reduction by network water immobilisation 网络水固定化使等效 D 下降 | `×(R+1)` | [[Mathematics of Diffusion]] |
| Reference-frame requirement 参考系要求 | SAP must define D in a **mass-fixed reference frame**（溶胀体积剧变，否则 D 不可比） | [[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]] |
| Coverage 覆盖范围 | 15 chapters（Fick 定律 → 解析/数值 → D(C) → 非菲克 → 复合介质 → 动边界 → 反应-扩散 → 湿热耦合） | [[Mathematics of Diffusion]] |

## Method / Mechanism 方法 / 机理

**Derivation chain:** physical motivation → molecular random walk → statistical averaging gives net flux → Fick assumption → differential mass conservation → conservative form → simplification under constant D（源：[[Diffusion Equations (Crank Ch.1)]]）.

**SAP swelling is not plain Fickian.** The **Alfrey-Gurnee-Lloyd three-way classification** splits behaviour by the ratio of diffusion to relaxation rate: **Case I（Fickian）** when diffusion << relaxation; **Case II** when diffusion >> relaxation; **non-Fickian** when they are comparable. SAP maps onto the sequence 干态玻璃态 → Case II → 非菲克 → 橡胶态 Case I, which is the physical root of the **S-shaped sorption curve**（源：[[Non-Fickian Diffusion (Crank Ch.11)]]）. Critically, **a glassy polymer cannot be described by the D(C) form of Fick's law**, so the swelling front requires a **moving-boundary (Stefan) model**（源：[[Moving Boundaries (Crank Ch.13)]]）. The key mathematical trick for SAP particles is the **`u = Cr` transformation**, which maps the sphere geometry onto the 1-D linear PDE so the plane-sheet solution can be reused（源：[[Mathematics of Diffusion]]）.

**Scope limits:** Fick's law applies only to isotropic media — a composite core's MD/CD difference requires a **diffusion tensor `D_ij`**; forced-convection scenarios (e.g. wet-wipe wiping) need an added convection term（源：[[Diffusion Equations (Crank Ch.1)]]）.

## Hygiene Relevance 卫材关联

This is the mathematical foundation layer for the REL core: **[[SAP 溶胀 SAP Swelling]]** kinetics（[[Diffusion in a Sphere (Crank Ch.6)]]）, **[[吸收芯体]]** uptake and layered structure（[[Diffusion in a Plane Sheet (Crank Ch.4)]]、[[Diffusion in Heterogeneous Media (Crank Ch.12)]]）and **[[湿迁移 Wet Migration]]** all rest on Fick's second law. The series-resistance model `Σ(lᵢ/Pᵢ)` is the modelling basis for the multilayer core, and the `L = l²/6D` time-lag method is the standard route to measuring D in SAP and films. Coupled heat–moisture diffusion gives the physical account of **"湿冷感"（cool-damp sensation）**（源：[[Mathematics of Diffusion]]）. For the simulation stack see [[Hygiene Absorption Model]].

## Open Questions 待补

- No numeric D values (m²/s) for KC's own SAP grades or core layers are evidenced in the vault `[待补]`.
- The vault states SAP D(C) spans 3–4 orders of magnitude but gives no fitted D(C) function for a named grade `[待补]`.
- Anisotropic `D_ij` tensors for composite cores are called for but not supplied `[待补]`.

## Related Sources 关联来源

- [[Mathematics of Diffusion]]
- [[Diffusion Equations (Crank Ch.1)]]
- [[Non-Fickian Diffusion (Crank Ch.11)]]
- [[Moving Boundaries (Crank Ch.13)]]
- [[Case II 扩散]]
- [[Diffusion in a Sphere (Crank Ch.6)]]
- [[Diffusion in a Plane Sheet (Crank Ch.4)]]
- [[Diffusion in Heterogeneous Media (Crank Ch.12)]]
- [[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]]
- [[时间滞后法 Time Lag Method]]
- [[Boltzmann 变换]]
- [[湿迁移 Wet Migration]]

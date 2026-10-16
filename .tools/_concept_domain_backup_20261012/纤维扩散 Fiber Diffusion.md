---
type: concept
title: "纤维扩散 Fiber Diffusion"
domain: [卫材研发, REL增强层与纤维]
status: growing
updated: 2026-09-30
tags: [diffusion, fibre, Bessel, Crank, wet-migration]
---

# 纤维扩散 Fiber Diffusion
> 📌 **Page completed 2026-09-30** from 4 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义
`定义待补（引用来源未给出明确定义）` — the vault does not give a standalone definition of fibre diffusion. It is evidenced **through its method chapter** — Crank Ch.5 *Diffusion in a Cylinder* — i.e. the diffusion-analytical treatment of a cylinder (fibre / cylindrical particle), with single-fibre radial liquid uptake modelled by the **Bessel J₀ series**（源：[[Diffusion in a Cylinder (Crank Ch.5)]]）.

## Key Parameters and Data 关键参数与数据
| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Geometry 几何 | Cylinder (fibre / cylindrical particle); Bessel functions are the standard analytical tool | [[Diffusion in a Cylinder (Crank Ch.5)]] |
| Analytical tool 解析工具 | Bessel **J₀ series** — single-fibre radial uptake kinetics（单纤维吸液动力学） | [[Diffusion in a Cylinder (Crank Ch.5)]] |
| Origin of the tool 工具来源 | Bessel functions arise from separation of variables C = u(x)·exp(−Dα²t) in cylindrical/spherical coordinates for the constant-D diffusion equation | [[Bessel 函数]] |
| Scope limit 适用边界 | Fick's law applies only to isotropic media; a composite core's MD/CD difference requires a **diffusion tensor**, and forced convection (e.g. wiping) needs an added convection term | [[Fick 定律]] |

## Method / Mechanism 方法 / 机理
- The fibre-scale problem is the constant-D diffusion equation in **cylindrical coordinates**; separation of variables reduces it to a Bessel eigenvalue problem（源：[[Bessel 函数]]）.
- Within this family, the **J₀ series** is the specific tool used to model single-fibre **radial** liquid uptake（源：[[Diffusion in a Cylinder (Crank Ch.5)]]、[[Bessel 函数]]）.
- The wider diffusion mathematics (Fick's law as the single core assumption) is shared with the vault's SAP-swelling, core-uptake-rate and wet-migration models（源：[[湿迁移 Wet Migration]]）.

## Hygiene Relevance 卫材关联
- Fibre diffusion is the fibre-scale member of the vault's diffusion family（Crank Ch.3–11）that also covers [[湿迁移 Wet Migration]] and SAP swelling; these share Fick's law as root（源：[[湿迁移 Wet Migration]]）.
- `[待补]` No hygiene-facing numeric application (fibre radius, D, boundary conditions) for fibre diffusion is given in the read excerpts.

## Open Questions 待补
- Definition, boundary conditions and the numerical values of J₀ / J₁ / I₀ in specific hygiene models — `定义待补`（源未给出）.
- Whether the vault's fibre-diffusion treatment is applied to fluff-pulp or synthetic nonwoven fibres is not stated（源未给出）.
- The corresponding spherical (SAP microsphere) solution is only cross-referenced, not expanded, in this batch（源未给出）.

## Related Sources 关联来源
- [[Diffusion in a Cylinder (Crank Ch.5)]]（原引用来源）
- [[Bessel 函数]]、[[Fick 定律]]、[[湿迁移 Wet Migration]]
- Adjacent pages 相邻页：[[SAP（高吸水树脂）]]、[[Washburn Equation]]

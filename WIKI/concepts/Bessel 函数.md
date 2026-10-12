---
type: concept
title: "Bessel 函数"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [Bessel, 数学工具, 扩散, 柱坐标, Crank, 建模]
---

# Bessel 函数

> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**定义待补（引用来源未给出明确定义）。** 引用来源未给出 Bessel 函数的数学定义，仅给出其在扩散解析解中承担的角色：

- *"Bessel 函数：I₀, J₀, J₁ 是柱 / 球坐标下的标准工具"*（源：[[Infinite and Semi-Infinite Media (Crank Ch.3)]]）。
- *"Bessel 函数 J₀ 级数是单纤维吸液动力学的解析工具"*（源：[[Diffusion in a Cylinder (Crank Ch.5)]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 标准工具集（柱 / 球坐标） | I₀, J₀, J₁ | [[Infinite and Semi-Infinite Media (Crank Ch.3)]] |
| 圆盘源解中的 Bessel 项 | Q(t) = 2πa²C₀ ∫₀^∞ [J₁(ωa)]² exp(−Dτω²)dω | [[Infinite and Semi-Infinite Media (Crank Ch.3)]] |
| J₀ 级数用途 | 单纤维吸液动力学的解析工具 | [[Diffusion in a Cylinder (Crank Ch.5)]] |
| 分离变量法导出 | C = u(x)·exp(−Dα²t) → Bessel / 三角本征值问题 | [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] |
| 关联几何（柱） | 纤维径向水含量呈 ln(r) 稳态分布 | [[Diffusion in a Cylinder (Crank Ch.5)]] |
| 关联最优壁厚条件 | b = 1/h（指导纺粘纤维直径设计） | [[Diffusion in a Cylinder (Crank Ch.5)]] |

## Method / Mechanism 方法 / 机理

- Bessel 函数由**分离变量法**在**柱 / 球坐标**下解恒 D 扩散方程时自然出现：C = u(x)·exp(−Dα²t) 得到 Bessel / 三角本征值问题（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。
- 在**柱坐标**（纤维 / 圆柱颗粒）中，Bessel 函数是扩散解析解的标准工具；J₀ 级数用于**单纤维吸液动力学**建模（源：[[Diffusion in a Cylinder (Crank Ch.5)]]）。
- 在**圆盘源**（湿巾湿斑）解中，[J₁(ωa)]² 出现在积分核里（源：[[Infinite and Semi-Infinite Media (Crank Ch.3)]]）。

## Hygiene Relevance 卫材关联

- **单纤维吸液动力学**：J₀ 级数用于建模纤维径向吸液（源：[[Diffusion in a Cylinder (Crank Ch.5)]]）。
- **湿巾湿斑扩散**：圆盘源解 Q(t) 含 [J₁(ωa)]² 项，作为湿斑扩散模型（源：[[Infinite and Semi-Infinite Media (Crank Ch.3)]]）。
- 关联概念页：[[纤维扩散 Fiber Diffusion]]、[[湿迁移 Wet Migration]]、[[格林函数 Green's Function]]、[[SAP（高吸水树脂）]]、[[Nonwoven 非织造布]]、[[湿巾 Wet Wipes]]。

## Open Questions 待补

- Bessel 函数的数学定义（引用来源未给出）`[待补]`。
- J₀ / J₁ / I₀ 各分量在具体卫材模型中的取值与边界条件 `[待补]`。
- 球坐标（SAP 微球）下的对应解可参见 [[Diffusion in a Sphere (Crank Ch.6)]]，本批来源未展开 `[待补]`。

## Related Sources 关联来源

- [[Diffusion in a Cylinder (Crank Ch.5)]]
- [[Infinite and Semi-Infinite Media (Crank Ch.3)]]
- [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]
- [[Mathematics of Diffusion]]
- [[纤维扩散 Fiber Diffusion]]
- [[格林函数 Green's Function]]

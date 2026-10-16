---
type: concept
title: "时间滞后法 Time Lag Method"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-30
tags: [时间滞后法, 扩散系数测量, 湿迁移, SAP表征, Crank]
---

# 时间滞后法 Time Lag Method

> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**Time lag L 的定义**（唯一可溯源口径）：渗透曲线**稳态段的 t 轴截距**。测出湿流稳态段的截距 L，除以 `6/l²` 即得扩散系数 D —— `L = l²/6D`（源：[[Diffusion in a Plane Sheet (Crank Ch.4)]]）。

It is listed as one of the standard D-measurement families in Crank Ch.10 — 稳态法 / 非稳态法 / **时间滞后法（Ch.4）** / 动态法 / D(C) 反演（源：[[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Time-lag relation 时间滞后关系 | L = l²/6D | [[Diffusion in a Plane Sheet (Crank Ch.4)]] |
| 反演口径 | 截距 L ÷ (6/l²) ⇒ D | [[Diffusion in a Plane Sheet (Crank Ch.4)]] |
| Daynes 方法提出年 | 1920 | [[Diffusion in a Plane Sheet (Crank Ch.4)]] |
| Barrer 方法应用年 | 1951 | [[Diffusion in a Plane Sheet (Crank Ch.4)]] |
| 稳态通量（前置关系） | F = D(C₁−C₂)/l | [[Diffusion in a Plane Sheet (Crank Ch.4)]] |
| 渗透常数（前置关系） | P = DS | [[Diffusion in a Plane Sheet (Crank Ch.4)]] |
| 复合膜总阻力（串联叠加） | Σ(lᵢ/Dᵢ) | [[Diffusion in a Plane Sheet (Crank Ch.4)]] |
| 参考系选项（D 的定义前提） | 体积固定 / 质量固定 / 溶剂固定 | [[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]] |
| SAP 推荐参考系 | 质量固定 | [[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]] |
| 二元体系互扩散系数 | D_A^V = D_B^V = D（体积固定参考系） | [[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]] |

## Method / Mechanism 方法 / 机理

- **几何前提：一维有限域平面片。** 时间滞后法是 Ch.4「平面片扩散」在渗透测量上的应用；同一章的稳态解给出浓度线性分布与通量 `F = D(C₁−C₂)/l`（源：[[Diffusion in a Plane Sheet (Crank Ch.4)]]）。
- **操作步骤。** 对一片厚度 l 的膜/片做渗透实验，记录下游累积湿流量-时间曲线；取**稳态段的线性段**，其在时间轴上的截距即 L；由 `D = l²/6L` 反演（源：[[Diffusion in a Plane Sheet (Crank Ch.4)]]）。
- **非稳态段的分工。** 小 t 用误差函数类解，大 t 用傅里叶级数解 —— 时间滞后法取的正是**大 t 稳态段**（源：[[Diffusion in a Plane Sheet (Crank Ch.4)]]）。
- **D 必须先指定参考系。** D 的定义依赖于参考系选择（体积 / 质量 / 溶剂固定），不同参考系给出不同 D 值；SAP 因溶胀体积剧变**通常用质量固定参考系**，否则 D 值无法比较（源：[[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]]）。
- **二元体系只需一个 D。** 体积固定参考系下 `D_A^V = D_B^V = D`，即 SAP+水互扩散系数唯一，无需分别定义 D_SAP 与 D_水（源：[[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]]）。

## Hygiene Relevance 卫材关联

- **几何直接对应芯体。** 一维有限域扩散是纸尿裤**芯体层、湿巾、SAP 片层、复合膜**的最直接对应几何（源：[[Diffusion in a Plane Sheet (Crank Ch.4)]]）。
- **行业标准 D 测量法。** `L = l²/6D` 是 SAP/纤维材料 D 测量的**行业标准方法**（Daynes 1920, Barrer 1951）（源：[[Diffusion in a Plane Sheet (Crank Ch.4)]]）。
- **多层芯体的传质阻力叠加。** 复合膜总阻力 = 各层阻力之和 Σ(lᵢ/Dᵢ)，是芯体多层结构（顶表层 / 纺粘导流层 / 绒毛浆 / SAP 层 / PP 底膜）传质阻力建模的基础公式（源：[[Diffusion in a Plane Sheet (Crank Ch.4)]]）。
- **MVTR 与液态阻隔率差异的解释。** 渗透常数 `P = DS`（D 与溶解度 S 之积），MVTR 与液态阻隔率的差异本质是 P 不同（源：[[Diffusion in a Plane Sheet (Crank Ch.4)]]）。
- **SAP 表征的前提条件。** 报 SAP 的 D 时必须声明参考系（推荐质量固定），否则数据不可跨来源比较（源：[[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]]）。

## Open Questions 待补

- 本库未见任何**实测**时间滞后曲线、L 值或由本法反演出的 D 值 `[待补]`。
- 时间滞后法在**非理想几何**（溶胀中的 SAP 颗粒、蓬松纤网）上的适用性/修正未见记录 `[待补]`。

## Related Sources 关联来源

- Citing sources 引用来源：[[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]]、[[Diffusion in a Plane Sheet (Crank Ch.4)]]
- Parent book 父书：[[Mathematics of Diffusion]]
- Adjacent concepts 相邻概念：[[Fick 定律]]、[[格林函数 Green's Function]]、[[Laplace 变换]]
- Application pages 应用页：[[SAP（高吸水树脂）]]、[[吸收芯体]]、[[水凝胶 Hydrogel]]

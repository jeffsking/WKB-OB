---
type: concept
title: "Boltzmann 变换"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [Boltzmann, 扩散, 变系数扩散, Crank, SAP建模, 数学工具]
---

# Boltzmann 变换

> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**Boltzmann 变换**：令 **η = x / 2√t**，把扩散 PDE 化为二阶常微分方程（源：[[Concentration-Dependent Diffusion Methods (Crank Ch.7)]]）：

```
d²C/dη² + 2η · d/dη ( D · dC/dη ) = 0
```

它是 **D(C) 浓度依赖扩散**的方法论核心，也是 SAP 吸液问题（D 强烈依赖浓度）的核心数学工具（源：[[Concentration-Dependent Diffusion Methods (Crank Ch.7)]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 变换 Definition | η = x / 2√t | [[Concentration-Dependent Diffusion Methods (Crank Ch.7)]] |
| 化归结果 Resulting ODE | d²C/dη² + 2η·d/dη(D·dC/dη) = 0 | [[Concentration-Dependent Diffusion Methods (Crank Ch.7)]] |
| 适用条件 Applicability | 初始 / 边界条件须可表为 η 的函数；x 与 t 不单独出现 | [[Concentration-Dependent Diffusion Methods (Crank Ch.7)]] |
| SAP 映射·适用 | 半无限 SAP 颗粒表面 | [[Concentration-Dependent Diffusion Methods (Crank Ch.7)]] |
| SAP 映射·不适用 | 有限厚 SAP 片层（边界含 t）→ 需数值方法 | [[Concentration-Dependent Diffusion Methods (Crank Ch.7)]] |
| SAP 的 D(C) 形态 | 常呈指数上升型（exponentially rising） | [[Mathematics of Diffusion]] |

## Method / Mechanism 方法 / 机理

- **推导逻辑链**：Boltzmann 变换 → PDE 化 ODE → 解析 / 数值求解 → Crank Ch 9 给出具体图表结果（源：[[Concentration-Dependent Diffusion Methods (Crank Ch.7)]]）。
- 变换把二阶 PDE 降为**二阶 ODE**，解析或数值均可求解（源：[[Concentration-Dependent Diffusion Methods (Crank Ch.7)]]）。

## Hygiene Relevance 卫材关联

- **SAP 吸液建模**：D 强烈依赖浓度时，Boltzmann 变换是把 PDE 降为 ODE 的核心工具；对**半无限 SAP 颗粒表面**有效，而**有限厚 SAP 片层需改用数值方法**（源：[[Concentration-Dependent Diffusion Methods (Crank Ch.7)]]）。
- 属 Crank 变系数扩散（Ch 7–9）体系：Boltzmann 变换、数值方法、等效扩散系数并列，其中 SAP 的 D(C) 常呈指数上升型（源：[[Mathematics of Diffusion]]）。
- 关联概念页：[[Fick 定律]]、[[自由体积 Free Volume]]、[[SAP（高吸水树脂）]]、[[Non-Fickian Diffusion (Crank Ch.11)]]、[[Numerical Methods for Diffusion (Crank Ch.8)]]。

## Open Questions 待补

- SAP 的 D(C) 具体函数形式与拟合参数 —— 本批来源未给出数值 `[待补]`。
- 有限厚 SAP 片层所需的具体数值方法细节 `[待补]`（可参见 [[Calculated Results for Variable Diffusion Coefficients (Crank Ch.9)]]）。

## Related Sources 关联来源

- [[Concentration-Dependent Diffusion Methods (Crank Ch.7)]]
- [[Calculated Results for Variable Diffusion Coefficients (Crank Ch.9)]]
- [[Mathematics of Diffusion]]
- [[Fick 定律]]
- [[自由体积 Free Volume]]

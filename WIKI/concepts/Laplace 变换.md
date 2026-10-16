---
type: concept
title: "Laplace 变换"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [diffusion, analytical-method, crank, sap-modelling, core-design]
---

# Laplace 变换

> 📌 **Page completed 2026-09-30** from 5 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）：库内未给出 Laplace 变换的数学单句定义。[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] 把它列为**恒扩散系数（恒 D）条件下解析解三类工具箱中的第三类**，并称之为最强工具 —— 在 p 域求像函数，再经逆变换回到时间域解。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Role 定位 | 恒 D 解析解三类方法之一，且为最强工具 | [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] |
| Solution flow 求解路径 | p 域求像函数 → 逆变换 → 时间域解 | [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] |
| Three toolboxes 三类工具 | ① 反射与叠加法 ② 分离变量法 ③ Laplace 变换法 | [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] |
| Two standard solutions 两类标准解 | 误差函数类（小时间数值评估方便）；三角函数级数（大时间收敛最好） | [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] |
| Plane-source Green's function 平面源格林函数 | C = (M / 2(πDt)^½)·exp(−x²/4Dt) | [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] |
| Impermeable boundary 不透水边界 | dC/dx = 0（对应 PP 底膜） | [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] |
| Moisture-permeable boundary 透湿边界 | dC/dx + hc = 0（对应顶表层） | [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] |

## Method / Mechanism 方法 / 机理

- **Three analytical methods for constant D（恒 D 情形的三类解析工具箱）**：① 反射与叠加法 —— 利用线性方程叠加性构造边界解；② 分离变量法 —— C = u(x)·exp(−Dα²t)，得到 Bessel／三角本征值问题；③ **Laplace 变换法 —— 最强工具**，p 域求像函数 → 逆变换给出时间域解（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。
- **Division of labour between the two standard solutions（两类标准解分工明确）**：小时间（SAP 吸液初期）用误差函数；大时间（稳态接近）用级数（源：[[格林函数 Green's Function]]）。
- **Derivation logic chain（推导逻辑链）**：恒 D PDE → 试探解 → 质量守恒定 A → 反射＋叠加 → 扩展初值 → 分离变量 → Laplace 变换（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。
- **Reflection method maps onto core structure（反射法直接映射芯体结构）**：不透水膜（PP 底膜）对应 dC/dx = 0，透湿膜（顶表层）对应 dC/dx + hc = 0（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。

## Hygiene Relevance 卫材关联

- Laplace 变换法对**复杂问题（多层复合芯体）**尤其关键，是 SAP 溶胀动力学与芯体湿迁移建模的解析基础（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。
- **平面源格林函数是 SAP 建模的原子单元**——单个 SAP 微球可视作瞬时点源，多粒子场可叠加（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。
- 相邻方法/工具：[[Bessel 函数]]（分离变量法的本征值问题）、[[湿迁移 Wet Migration]]、[[Fick 定律]]；下游应用页 [[SAP（高吸水树脂）]]、[[吸收芯体]]。

## Open Questions 待补

- Laplace 变换的数学定义与收敛条件：库内未给出 [待补]
- 多层复合芯体逆变换的数值实现与精度：库内未给出 [待补]

## Related Sources 关联来源

- [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]
- [[格林函数 Green's Function]]
- [[Mathematics of Diffusion]]
- [[SAP（高吸水树脂）]]
- [[吸收芯体]]
- [[concept_index]]
- [[synthesis]]


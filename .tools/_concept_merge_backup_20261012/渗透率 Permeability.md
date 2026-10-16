---
type: concept
title: "渗透率 Permeability"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [permeability, 渗透率, 达西定律, Kozeny-Carman, 凝胶阻塞, 吸收芯体]
---

# 渗透率 Permeability

> 📌 **Page completed 2026-09-30** from 8 vault pages. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

渗透率 **k** 是达西定律中的材料属性：传导系数 **K = k/μ**（k 为渗透率，μ 为流体黏度），流率正比于压力梯度 **q = −K·∇P**（源：[[达西定律 Darcy's Law]]）。

在吸液体系中，驱动力通常不是外压而是毛细压力 **p_c = 2γcosθ/r**（源：[[达西定律 Darcy's Law]]）。渗透率与孔隙率由 **Kozeny–Carman 关系 k ∝ Φ³/(1−Φ)²** 挂钩（源：[[Porous Structure and Liquid Flow Models]]）。

> 口径提醒：本库各页给出达西定律与扩散因子的**公式**，但**未给出绒毛浆/非织造/SAP 层的 k、Φ 实测值** `[待补]`（源：[[达西定律 Darcy's Law]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 达西传导系数 | K = k/μ（渗透率 k ÷ 流体黏度 μ） | [[达西定律 Darcy's Law]] |
| Kozeny–Carman 关系 | k ∝ Φ³/(1−Φ)²（孔隙率小幅提升 → 渗透率大幅提升） | [[Porous Structure and Liquid Flow Models]] |
| 凝胶阻塞：有效渗透率（仿真反推） | 基准 **1e-12 m²** → **~2e-13 m²**（约 1/5） | [[Gel Blocking（凝胶阻塞）]] |
| 凝胶阻塞：吸收区渗透率下降 | 约 **2–5 倍**（Carman-Kozeny 模型） | [[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]] |
| 相对渗透率瓶颈（干/湿界面） | kr ~ Sw³ → 0 | [[Gel Blocking（凝胶阻塞）]] |
| ADL 层渗透率 | **k = 5e-11 m²**，约为 Core 的 **50 倍** | [[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]] |
| Core 有效渗透率 | **~2e-13 m²**（模型反推，无实测对应） | [[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]、[[Gel Blocking（凝胶阻塞）]] |
| 压缩换算输出 | Permeability 随载荷函数输出（与 Thickness / Strain / Available Void Volume / Porosity 并列） | [[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]] |

## Method / Mechanism 方法 / 机理

- **速率与容量互为对手，且都受几何支配**：大孔提高速率（Hagen–Poiseuille：flow ∝ r²，Y×2 → flow×16）但降低毛细压力（p_c ∝ 1/r），故容量下降；最优值位于中段（源：[[Porous Structure and Liquid Flow Models]]）。
- **凝胶阻塞自限性机制**：由**颗粒填充床微观流道理论（Carman-Kozeny）**推导 —— SAP 溶胀 → 降低孔隙率 → 降低渗透率 → 限制后续液体到达更深层（源：[[孔隙率 Porosity]]、[[Gel Blocking（凝胶阻塞）]]）。
- **干界面瓶颈**：干燥芯层界面处 **kr ~ Sw³ → 0**，压力求解器无法驱动重力流穿过干/湿界面 —— 这是均匀芯体模型根本性失效的原因，即"机制上走不动"，靠调渗透率修不好（源：[[Gel Blocking（凝胶阻塞）]]）。
- **非稳态即扩散**：∂s/∂t = ∇·[F(s)∇s]，扩散因子 F(s) = (k/μΦ)(dp/ds)（源：[[达西定律 Darcy's Law]]、[[Porous Structure and Liquid Flow Models]]）。

## Hygiene Relevance 卫材关联

- **芯体三大可测量之一**：第 1 章把"吸得快"翻译成毛细压力、**渗透率/流速**、孔隙体积三个可测量量（源：[[Porous Structure and Liquid Flow Models]]）。
- **"高 SAP 含量反而易侧漏"的机理**：溶胀降孔隙率 → 降渗透率 → 后续液体到不了深层；⚠️ 本库标注此为**模型推论，无实验验证**（源：[[孔隙率 Porosity]]、[[Gel Blocking（凝胶阻塞）]]）。
- **ADL 角色**：ADL 高渗透率（约为 Core 的 50 倍）使液体快速通过并均匀分配到多层 Core，绕过干界面瓶颈；但 Core 层内的凝胶阻塞仍限制进一步深度渗透（源：[[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]）。
- **SAP 改性提升渗透率**：木浆芯体用 SAP 以原位 nano-SiO₂ 提高渗透率/扩散并降低回渗（源：[[CN 107854223 B（一种适用于木浆芯体纸尿裤的吸水树脂及其制备方法）]]）。
- 关联概念：[[孔隙率 Porosity]]、[[Gel Blocking（凝胶阻塞）]]、[[吸收芯体]]、[[ADL（导流层）]]、[[绒毛浆（Fluff Pulp）]]、[[SAP（高吸水树脂）]]（源：[[Porous Structure and Liquid Flow Models]]）。

## Open Questions 待补

- 绒毛浆/非织造/SAP 层的 **k、Φ 实测值**（库内缺）`[待补]`。
- 达西定律的适用上限（Reynolds 数边界 / Forchheimer 修正触发条件）`[待补]`。
- 渗透率与 [[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]、[[SAP性能指标（CRC AUL GBP Vortex）]] 的量化耦合口径 `[待补]`。

## Related Sources 关联来源

- [[Porous Structure and Liquid Flow Models]]
- [[达西定律 Darcy's Law]]
- [[孔隙率 Porosity]]
- [[Gel Blocking（凝胶阻塞）]]
- [[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]
- [[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]
- [[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]
- [[CN 107854223 B（一种适用于木浆芯体纸尿裤的吸水树脂及其制备方法）]]
- [[Washburn Equation]]
- [[毛细压力 Capillary Pressure]]
- [[吸收芯体]]
- [[ADL（导流层）]]

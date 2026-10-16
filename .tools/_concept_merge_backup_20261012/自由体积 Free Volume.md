---
type: concept
title: "自由体积 Free Volume"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [free-volume, glass-transition, diffusion, SAP, swelling, polymer-physics]
---

# 自由体积 Free Volume

> 📌 **Page completed 2026-09-30** from 4 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**自由体积理论（free volume theory）**：*"free volume is assumed to be the difference between the total volume and the occupied volume"*（自由体积假定为总体积与已占体积之差）（p.27，源：[[Manufactured Fibre Technology Ch02 Structural Principles of Polymeric Fibres]]）。该章以膨胀计（dilatometer）测绘**比容—温度曲线**来界定 Tg 与 Tm（源：[[Manufactured Fibre Technology Ch02 Structural Principles of Polymeric Fibres]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 定义 | 自由体积 = 总体积 − 已占体积（总体积与已占体积之差） | [[Manufactured Fibre Technology Ch02 Structural Principles of Polymeric Fibres]] |
| 自由体积与 Tg | 自由体积增加 → Tg 降低（"The increased free volume results in a lower Tg."，p.100） | [[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]] |
| 链段协同运动尺度 | Tg 处约 25 个碳的链段（~25 carbon atoms）开始协同旋转（p.20） | [[Manufactured Fibre Technology Ch02 Structural Principles of Polymeric Fibres]] |
| SAP 等效扩散系数（浓度依赖） | D/D₀ = 1 + 10(1 − e^(−2.303c)) | [[Calculated Results for Variable Diffusion Coefficients (Crank Ch.9)]] |
| SAP 稳态浓度分布 | D₀∫{1+f(C)}dC = Ax + B | [[Calculated Results for Variable Diffusion Coefficients (Crank Ch.9)]] |
| 脱挥发分（devolatilization）温度 | 通常在聚合物 Tg 以上进行（p.977） | [[Industrial Drying Ch41 Drying of Polymers]] |

## Method / Mechanism 方法 / 机理

- **自由体积是 Tg 的结构解释变量**：体积随温度膨胀，超过已占体积的部分即自由体积；自由体积增加使链段运动更容易，因而 Tg 下降 *"The increased free volume results in a lower Tg."*（p.100，源：[[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]）。反向地，**庞大且刚性、贴近主链的侧基造成位阻、降低链段活动性，从而抬高 Tg**（p.100，同源）。
- **扩散通道机理（干燥 / 脱挥发分）**：残留单体、溶剂、水等小分子的脱除需要扩散通道 —— *Tg 以下为玻璃态，自由体积过低，挥发物无法扩散出去；Tg 以上链段拥有足够自由体积可供扩散*；因此脱挥发分通常在 Tg 以上进行（源：[[Industrial Drying Ch41 Drying of Polymers]]）。
- **SAP 吸液非线性的物理图像**：非稳态等效扩散系数曲线 D/D₀ = 1 + 10(1 − e^(−2.303c)) 呈**指数上升型**，其物理解释即"**高分子溶胀 → 自由体积增加 → D(C) 指数上升**"；稳态解的凸/凹向（D↑→凸向浓度轴、D↓→凹向）是 D(C) 形态判据（源：[[Calculated Results for Variable Diffusion Coefficients (Crank Ch.9)]]）。
- 与 [[Boltzmann 变换]]的关系：D 强烈依赖浓度时，Boltzmann 变换是把扩散 PDE 降为 ODE 的核心工具，属 Crank 变系数扩散（Ch 7–9）体系（源：[[Boltzmann 变换]]、[[Mathematics of Diffusion]]）。

## Hygiene Relevance 卫材关联

- **SAP 吸收动力学的定量描述**：SAP 的 D(C) 常呈指数上升型，对应溶胀驱动的自由体积增加 —— 这是 SAP 吸液非线性行为的物理解释，可直接用于吸液建模（源：[[Calculated Results for Variable Diffusion Coefficients (Crank Ch.9)]]、[[Boltzmann 变换]]）。
- **SAP 干燥窗口存在口径张力（如实记录）**：一方面，脱挥发分（去除残单）通常在 **Tg 以上**进行以便扩散（源：[[Industrial Drying Ch41 Drying of Polymers]]）；另一方面，该来源同时给出 SAP 侧的工程口径 —— "**末段干燥温度须低于 Tg，以避免过度交联而杀死可溶胀性**"（源：[[Industrial Drying Ch41 Drying of Polymers]]）。两条口径的适用边界（脱除残单 vs 控制交联）未在库内澄清，见 Open Questions。
- 关联：[[SAP（高吸水树脂）]]、[[交联密度 Crosslink Density]]、[[达西定律 Darcy's Law]]、[[Fick 定律]]。

## Open Questions 待补

- **无定量自由体积值**：库内未见任何聚合物 / 纤维的绝对自由体积数值（如 WLF 常数、分数自由体积 v_f）`[待补]`。
- **干燥温度口径冲突未裁决**：脱挥发分"须在 Tg 以上"与 SAP 末段干燥"须低于 Tg"两条口径的适用边界（残单扩散 vs 抑制过度交联）在库内未澄清 `[待补]`。
- **无卫材纤维的自由体积—性能关联**：未见把 PP / PET 纤维的自由体积与其热粘合、回渗或渗透率联系起来的来源 `[待补]`。
- **⚠️ Digest 命中偏差**：本页 digest（`.tools/_seed_ctx/自由体积 Free Volume.txt`）的正文摘录多为相邻主题（孔隙率、比空气体积、底膜、PCM 等），仅 [[Calculated Results for Variable Diffusion Coefficients (Crank Ch.9)]] 一段与本主题直接相关；本页定义与其他机理事实另据库内实际提及自由体积的页面核对（[[Manufactured Fibre Technology Ch02 Structural Principles of Polymeric Fibres]]、[[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]、[[Industrial Drying Ch41 Drying of Polymers]]）。建议重跑 digest。

## Related Sources 关联来源

- [[Calculated Results for Variable Diffusion Coefficients (Crank Ch.9)]]
- [[Boltzmann 变换]]
- [[Mathematics of Diffusion]]
- [[Manufactured Fibre Technology Ch02 Structural Principles of Polymeric Fibres]]
- [[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]
- [[Industrial Drying Ch41 Drying of Polymers]]
- 相关概念：[[SAP（高吸水树脂）]] · [[交联密度 Crosslink Density]] · [[Fick 定律]] · [[达西定律 Darcy's Law]]

---
type: source
title: "多孔介质流动仿真，从达西定律到完整 CFD 建模"
source_type: 公众号
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/多孔介质流动仿真，从达西定律到完整 CFD 建模.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# 多孔介质流动仿真，从达西定律到完整 CFD 建模

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 公众号`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/多孔介质流动仿真，从达西定律到完整 CFD 建模.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# 多孔介质流动仿真，从达西定律到完整 CFD 建模

做过滤器、催化转化器、地下水流动的仿真，都会遇到多孔介质。多孔介质的核心问题是：流速和压降的关系。

今天用一个完整的案例，演示多孔介质 CFD 建模的全流程。

## 第一步：判断流动状态

计算雷诺数 Re = ρ × U × D / μ

其中 D 是特征孔径（颗粒直径或孔径）。

Re < 1：粘性力主导，达西定律够用

1 < Re < 10：惯性力开始出现

Re > 10：惯性力显著，需要 Forchheimer 修正

Re > 100：可能进入湍流区

## 第二步：获取渗透率和惯性阻力系数

方法 1：实验测定

测不同流速下的压降，拟合 ΔP/L = A×U + B×U²

A = μ/K → K = μ/A；B = C₂×ρ → C₂ = B/ρ

方法 2：经验公式

球形颗粒床（Carman-Kozeny + Ergun）：

K = dp²×ε³ / (150×(1-ε)²)

C₂ = 1.75 / (dp×(1-ε))

其中 dp 是颗粒直径，ε 是孔隙率。

## 第三步：Fluent 设置

在 Cell Zone Conditions 里选中多孔介质区域：

勾选 Porous Zone

Direction 设为各向同性或各向异性

Viscous Resistance = 1/K

Inertial Resistance = C₂

注意方向：各向异性多孔介质，三个方向的阻力系数不同。

## 第四步：网格要求

多孔介质区域不需要特别加密（因为内部流动是宏观平均的）。

但多孔介质入口和出口区域需要加密，因为这里有流动过渡。

## 第五步：验证

压降对比：仿真压降和实验/公式计算对比，误差 < 15% 可接受

速度分布：多孔介质后的速度分布是否均匀

如果压降差了 2 倍以上，检查 Viscous Resistance 和 Inertial Resistance 是否设反了（常见错误！）

## 常见错误

错误 1：Viscous Resistance 和 Inertial Resistance 搞反

Viscous Resistance = 1/K（粘性阻力），Inertial Resistance = C₂（惯性阻力）

很多人把 K 直接填到 Viscous Resistance 里，差了 K² 倍！

错误 2：忘了惯性项

Re > 10 时，惯性项贡献可能超过粘性项。只设粘性阻力，压降算低很多。

错误 3：各向同性设成各向异性

有些多孔介质（比如纤维毡）在不同方向渗透率不同。设成各向同性，流场分布完全不对。

## 经验总结

多孔介质建模流程：

1. 算 Re 判断流动状态

2. 获取 K 和 C₂（实验或经验公式）

3. Fluent 设置 Viscous Resistance = 1/K，Inertial Resistance = C₂

4. 检查方向（各向同性/异性）

5. 验证压降（误差 < 15%）

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/多孔介质流动仿真，从达西定律到完整 CFD 建模.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/多孔介质流动仿真，从达西定律到完整 CFD 建模.md`

## 关联页面

- [[CFD 计算流体力学]]

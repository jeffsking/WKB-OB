---
type: source
title: "COMSOL多孔介质流动三剑客：达西、Brinkman 与理查兹方程全解析"
source_type: 公众号
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/COMSOL多孔介质流动三剑客：达西、Brinkman 与理查兹方程全解析.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
key_claims: []
pages_linked: []
compile_mode: extractive
---

# COMSOL多孔介质流动三剑客：达西、Brinkman 与理查兹方程全解析

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 公众号`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/COMSOL多孔介质流动三剑客：达西、Brinkman 与理查兹方程全解析.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# COMSOL多孔介质流动三剑客：达西、Brinkman 与理查兹方程全解析

在COMSOL，Brinkman 方程、理查兹方程和 达西定律都是用来描述多孔介质中流体流动的数学模型，但它们适用于不同的物理条件和应用场景。下面分别介绍这三种模型的基本原理、适用范围以及在 COMSOL 中的实现方式。

## 1. 达西定律

基本形式：

达西定律是最经典的多孔介质渗流模型，适用于低雷诺数（Re ≪ 1）、层流且忽略惯性项的情况：

u = -(κ/μ)∇p

其中：

u：达西速度（体积通量，m/s）

k：渗透率（m²）

mu：流体动力粘度（Pa·s）

p：压力（Pa）

若考虑重力，则常写作：

u = -(κ/μ)(∇p - ρg)

适用场景：

地下水流动

油藏工程中的缓慢渗流

多孔介质中无显著剪切或惯性效应的情形

在 COMSOL 中：

使用 "达西定律" 接口

可与传热、溶质输运等物理场耦合

## 2. Brinkman 方程

基本形式：

Brinkman 方程是对 Navier-Stokes 方程在多孔介质中的修正，既包含粘性剪切项（类似 Stokes 流），又保留了达西阻力项，适用于过渡区域（如靠近固体边界或多孔结构孔隙较大时）：

-∇p + μ_eff∇²u - (μ/κ)u + ρg = 0

其中：

mu：有效粘度

其余符号同上

连续性方程仍为：

∇·u = 0 (不可压缩)

适用场景：

多孔介质与自由流体交界处（如过滤器、生物组织）

孔隙尺度较大、存在明显速度梯度的区域

需要捕捉边界层效应的情形

在 COMSOL 中：

使用 "Brinkman 方程" 接口

可与 Navier-Stokes 方程在自由流区域耦合（通过多物理场接口）

## 3. 理查兹方程

基本形式：

理查兹方程用于描述非饱和多孔介质中的水分运动，即当孔隙中同时存在水和空气时（如土壤）。其核心是将达西定律与质量守恒结合，并引入水力传导率和压力水头 的非线性关系：

∂θ/∂t = ∇·[K(θ)(∇h - g)]

其中：

θ：体积含水率（无量纲）

h：压力水头（m）

K(θ)：水力传导率，随含水率变化（非线性）

通常通过 van Genuchten 或 Brooks-Corey 模型关联θ(h) 和 K

(θ)也可写成以压力 (p = rho*g*h) 为变量的形式。

适用场景：

土壤水分迁移（农业、环境工程）

非饱和带地下水模拟

降雨入渗、蒸发过程

在 COMSOL 中：

使用 "理查兹方程" 接口

内置 van Genuchten 等本构关系

支持瞬态模拟，处理强非线性问题（需适当设置求解器）

## 三者对比总结：

| 模型 | 适用饱和度 | 是否考虑粘性剪切 | 是否非线性 | 典型应用 |
| --- | --- | --- | --- | --- |
| 达西定律 | 饱和 | 否 | 否(线性) | 地下水、油藏 |
| Brinkman 方程 | 饱和 | 是 | 否(线性,除非κ变化) | 过滤器、多孔-自由流耦合 |
| 理查兹方程 | 非饱和 | 否(基于达西扩展) | 是(K(θ),θ(h)非线性) | 土壤水文学 |

## 在 COMSOL 中的选择建议：

如果你的问题是完全饱和、低速渗流 ,建议用达西定律；

如果涉及多孔介质与自由流交界，或需要捕捉速度梯度，建议用用 Brinkman 方程；

如果模拟土壤吸水、降雨入渗、干湿循环等非饱和过程，建议用 理查兹方程。

此外，COMSOL 支持这些接口与其他物理场（如传热、化学反应、结构力学）进行多物理场耦合，非常适合复杂多孔介质系统的建模。

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/COMSOL多孔介质流动三剑客：达西、Brinkman 与理查兹方程全解析.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/COMSOL多孔介质流动三剑客：达西、Brinkman 与理查兹方程全解析.md`
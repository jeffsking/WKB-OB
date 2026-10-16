---
type: concept
title: "达西定律 Darcy's Law"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [darcy-law, 达西定律, porous-media, permeability, capillary-pressure, wicking, washburn, absorbent-core]
---

# 达西定律 Darcy's Law

> 📌 **Page completed 2026-09-30** from 9 citing sources in the vault. All figures traced to their source pages. Anything not evidenced in the vault is marked `[待补]`.

## Definition 定义

Darcy's law（达西定律）is the governing relation for flow in porous media as used in the vault: **q = −K·∇P，K = k/μ**（流率正比于压力梯度，K 为传导系数 = 渗透率 k / 流体黏度 μ）（源：[[Porous Structure and Liquid Flow Models]]）。In absorbent systems the absorption driving force is not an external pressure but **capillary pressure**: **p_c = 2γcosθ/r**，外加重力或压力只起次要作用（源：[[Porous Structure and Liquid Flow Models]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Darcy's law form 达西定律形式 | q = −K·∇P；K = k/μ（源文 p. 19–24） | [[Porous Structure and Liquid Flow Models]] |
| Capillary pressure 毛细压力 | p_c = 2γcosθ/r | [[Porous Structure and Liquid Flow Models]] |
| Unsteady-flow equivalence 非稳态等价 | 数学上等同于扩散过程；推进的芯吸前沿距离 obey **x_v ∝ t^(1/2)**（Washburn / Rudd relation，p. 24, 37） | [[Porous Structure and Liquid Flow Models]] |
| Diffusivity factor 扩散因子 | F(s) = (k/μΦ)(dp_c/ds) | [[Porous Structure and Liquid Flow Models]] |
| Governing PDE 控制方程（非稳态） | ∂s/∂t = ∇·[F(s)∇s] | [[Porous Structure and Liquid Flow Models]] |
| Driving force 驱动力 | 大体积液体被吸入吸收材料的驱动力为**毛细压力**；重力/外压次要（p. 19） | [[Porous Structure and Liquid Flow Models]] |

## Method / Mechanism 方法 / 机理

- **Capillary-driven absorption 毛细驱动的吸收.** 「The driving force for absorption of the bulk of the liquid into an absorbing material ... is the capillary pressure」，重力或外压为次要项（源：[[Porous Structure and Liquid Flow Models]]）。
- **Unsteady flow = diffusion 非稳态流动即扩散.** 「Unsteady flow in a porous medium is similar to a diffusion process ... or a heat conduction process」；控制方程为 ∂s/∂t = ∇·[F(s)∇s]，其中 F(s) = (k/μΦ)(dp/ds) 即扩散因子（土壤物理中的「湿度扩散率」）（源：[[Porous Structure and Liquid Flow Models]]）。
- **Coupling of permeability and capillary gradient 渗透率与毛细梯度的耦合.** 扩散因子 F(s) = (k/μΦ)(dp_c/ds) 把**渗透率**与**毛细梯度**联系起来（源：[[Porous Structure and Liquid Flow Models]]）。
- **Chapter placement 章节定位.** 在 *Absorbent Technology* 中，达西定律属于**第 1 章「多孔结构与液体流动模型」**，与 Péclet 数判据、Washburn/Lucas-Washburn 方程、毛细压力与 Kelvin 方程同章，是吸液动力学的物理基础（源：[[Absorbent Technology]]）。

## Hygiene Relevance 卫材关联

- **Core modelling interface 芯体建模接口.** 达西定律是第 1 章「多孔结构与液体流动模型」的核心构件，直接对接**芯体吸液动力学建模**；第 3 章 *Fluid Absorption in High Bulk Nonwovens* 与第 4 章 *Computational Modeling in Absorbent Technology* 分别提供吸液动力学/C-Q 模型与 2D/3D 数值模拟（有限元）（源：[[Absorbent Technology]]）。
- **Material selection precondition 材料选择先决条件.** 接触角/润湿指数/附着功等表面化学第一性原理决定纤维与结构能否有效吸液——达西流动发生的**前置条件**（源：[[Absorbent Technology]]）。
- **Porous-media treatment of nonwovens 非织造布的多孔介质处理.** 达西定律在非织造织物表征与建模中被列为关联概念（源：[[Characterisation, testing and modelling of nonwoven fabrics]]）；在吸液性能测试与计算建模中同样被列为概念接口（源：[[Absorbent Product Testing]]、[[Computational Modeling in Absorbent Technology]]）。
- **Fibrous porous media 纤维多孔介质.** 已有专页 [[Darcy Flow in Fibrous Porous Media（纤维多孔介质达西流动）]] 承接纤维介质的达西流动；本页为其上位/平行索引。
- **Related quantitative anchors 相关定量锚点.** 达西定律与 [[毛细压力 Capillary Pressure]]、[[Washburn Equation]]、[[孔隙率 Porosity]]、[[渗透率 Permeability]]、[[Gel Blocking（凝胶阻塞）]] 等在同一建模链上被引用（源：[[Porous Structure and Liquid Flow Models]]）。Acrylic-Based SAP 页给出交联密度→Flory-Rehner 溶胀仿真的参数接口（源：[[Acrylic-Based Superabsorbent Polymers]]）。

## Open Questions 待补

- **无材料级渗透率 / 孔隙率数值**：库内各页给出达西定律与扩散因子的**公式**，但**未给出绒毛浆/非织造/SAP 层的 k、Φ 实测值**——需回 *Absorbent Technology* 原文补齐。
- **达西定律的适用上限**：摘要未给出 Reynolds 数适用边界或 Forchheimer 修正的触发条件（源：[[Porous Structure and Liquid Flow Models]] 未涉及）。
- **与毛细动力学的时间标度**：x_v ∝ t^(1/2) 的比例常数在摘要中**未数值化**（源：[[Porous Structure and Liquid Flow Models]]）。
- **流体性质项**：μ（黏度）在摘要中仅作为 K = k/μ 的组成出现，**具体流体（尿/血/模拟液）黏度值未给出**。
- **落地方案**：库内无把达西定律直接用于**产线工艺参数（如施胶量、压花）**的记录，属理论接口而非工艺口径。

## Related Sources 关联来源

- [[Porous Structure and Liquid Flow Models]]
- [[Absorbent Technology]]
- [[Fluid Absorption in High Bulk Nonwovens]]
- [[Computational Modeling in Absorbent Technology]]
- [[Characterisation, testing and modelling of nonwoven fabrics]]
- [[Nonwovens in Absorbent Materials]]
- [[Absorbent Product Testing]]
- [[Acrylic-Based Superabsorbent Polymers]]
- [[吸收芯体]]
- [[Washburn Equation]]
- [[毛细压力 Capillary Pressure]]
- [[Liquid Flow in Porous Structures]]


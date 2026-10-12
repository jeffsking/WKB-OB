---
type: source
title: "Manufactured Fibre Technology Ch05 Computer Simulation of Melt Spinning"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Manufactured_Fibre_Technology/Manufactured Fibre Technology · analysis_ch05.md.md
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "The molecular orientation of the as-spun fibre represents the 'frozen-in' stress in the spinline; for slowly crystallising polymers such as PET, orientation is uniquely determined by σL, the spinline stress at the glass transition temperature (the freeze line)."
  - "A linear stress-optical law holds for PET: Δn = Cσ = C(F/A), with the stress optical coefficient C between 1×10⁻⁹ and 8×10⁻⁹ Pa⁻¹, so birefringence is directly proportional to spinline stress."
  - "σL is very strongly affected by extrusion temperature, melt intrinsic viscosity (IV), take-up velocity and melt throughput rate; quench air temperature has almost no effect."
  - "A variation of about 3 °C — a 1% change in extrusion temperature — could result in about 10% variation in spinline stress."
  - "Simulation defines the scope of experimentation, thereby eliminating the trial-and-error approach and leading to significant savings in time and effort."
summary_cn: "PET 熔纺计算机仿真：以 Kase-Matsuo 非等温单轴拉伸流模型 + Runge-Kutta 数值求解纺丝线应力，确立『as-spun 取向唯一由冻结线应力 σL 决定』与应力-光学定律 Δn=Cσ，并以敏感性分析给出控温/控 IV 的工艺优先级与三个工业仿真案例。"
tags: ["source/book", "simulation", "melt-spinning", "PET", "spinline-stress", "birefringence", "sensitivity-analysis", "Manufactured Fibre Technology"]
tags_zh: ["源摘要/书", "计算机仿真", "熔体纺丝", "PET", "纺丝线应力", "双折射", "敏感性分析", "人造纤维技术"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Manufactured Fibre Technology]]", "[[Manufactured Fibre Technology Ch04 Melt-Spinning Processes]]", "[[Meltblown Nonwoven（熔喷非织造布）]]", "[[Nonwoven Process Classification（非织造布工艺分类）]]", "[[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]"]
---

# Computer Simulation of Melt Spinning 熔纺的计算机仿真

> Source: Manufactured Fibre Technology, Ch.05, pp.98–123. (Author: V.M. Nadkarni)

## Scope 本章范围

全书少数以**计算建模**贯通"工艺—结构—性能"（processing–structure–property 工艺-结构-性能）的章节：以 Kase & Matsuo 的非等温单轴拉伸流（non-isothermal, uniaxial elongational flow 非等温单轴拉伸流）模型为基础，引入恒定张力与可变纺丝线力模型，用四阶 Runge-Kutta 法求解纺丝线应力（spinline stress 纺丝线应力）与温度场，并以**增产、细旦丝（subdenier）、低起球丝（low pill）**三个工业案例演示工艺优化。子节：5.1 引言、5.2 理论背景、5.3 纺丝线取向、5.4 敏感性分析、5.5 工艺含义、5.6 PET 应力-取向关系、5.7 增产案例、5.8 产品开发案例、5.9 结论。

## Core Physics 核心物理：取向 = 冻结的纺丝线应力

>"the molecular orientation of the as-spun fibre is expected to represent the 'frozen-in' stress in the spinline." (p.104)

>"the molecular orientation … is uniquely determined by σL, the spinline stress at the glass transition temperature (the freeze line)." (p.101)

对 PET 这类缓慢结晶聚合物，取向在玻璃化温度（glass transition 玻璃化转变）处被**冻结**；冻结线（freeze line 冻结线）即纺丝线冷却固化、距喷丝板距离 L 的位置（p.99）。故 as-spun 取向是 σL 的**单值函数** —— 这是全章仿真的物理基石。

### 应力-光学定律 Stress-Optical Law

>"Δn = Cσ = C(F/A) … the birefringence is directly proportional to the spinline stress for PET." (p.105)

| 符号 Symbol | 含义 Meaning | 数值 Value | 页码 p. |
|---|---|---|---|
| Δn | 双折射（birefringence 双折射），取向的光学度量 | — | 105 |
| C | 应力光学系数（stress optical coefficient） | **1×10⁻⁹ ~ 8×10⁻⁹ Pa⁻¹**（PET） | 105 |
| σ = F/A | 纺丝线应力 | — | 102 |
| σL | 冻结线处纺丝线应力 | 决定取向的唯一量 | 101 |

该定律把**可测工艺量（应力）与结构参数（取向）直接挂钩**，使仿真具备预测产品性能的能力；作者称其对 PET 与 PS 普适（p.105）。

## Model 模型与数值方法

- 六条简化假设（p.102）：稳态、一维（径向温度/速度无关）、Trouton 粘度、忽略惯性/重力/表面张力/空气阻力。
- 控制方程（p.102）：质量守恒 **W = ρAV**；力平衡 **σ = F/A = 3η₀(dV/dx)**；截面积与温度沿程微分（式 5.2 / 5.3）。
- 数值求解（p.103–104）：四阶 **Runge-Kutta**；因纺丝线张力 F 未知，用打靶法（shooting method 初值迭代）逼近边界条件（式 5.4b），初值估计式（5.8）提供良好起点。
- 物性关联：PET 零剪切粘度 η₀ = 9.76×10⁻³ · (IV)^5.28⁹³ · exp(6923.7/(T+273))（式 5.5，p.103）—— **指数项存在 OCR 变形，需回查原书 [待验证]**；密度/比热用线性式（5.6）；传热系数用 Kase & Matsuo 关联式（5.7）。

## Sensitivity Ranking 敏感性排序

>"σL is very strongly affected by changes in extrusion temperature, melt IV, take-up velocity and the melt throughput rate." (p.107)

| 排序 Rank | 变量 Variable | 中文 | 对 σL 影响 Effect |
|---|---|---|---|
| 1 | Extrusion temperature 挤出温度 | 挤出温度 | 极强 |
| 2 | Melt IV 熔体特性粘度 | 熔体特性粘度（分子量代理量） | 极强 |
| 3 | Take-up velocity 卷绕速度 | 卷绕速度 | 极强 |
| 4 | Melt throughput rate 熔体流量 | 熔体流量 | 极强 |
| — | Quench air temperature 冷却风温 | 冷却风温 | **几乎无影响** |

>"A variation of about 3°C … represents a 1% change in the extrusion temperature, but could result in about 10% variation in the spinline stress." (p.109)

工程推论（p.109–111）：多锭位工厂的温度均匀性直接决定纤度/伸长 CV，建议采用**静态混合器（static mixer 静态混合器）与在线测温**；并需稳定冻结线位置 L。

## Validation 工业验证

- 应力-取向关系式（5.10）用 **37 个数据点**回归（含印度三家工厂 19 组条件 + 文献 [3] 公开数据），**相关系数 r = 0.96**（p.112）。
- 案例（p.113–122）为基于 Dutta–Nadkarni 仿真包的 **数值 what-if 分析**：① 增产：温度↑ + 风温↓ 抵消增产带来的 σL 与 L 变化（表 5.3/5.4）；② 细旦丝：小孔径喷丝板 + 风温↓；③ 低起球丝：降 IV + 卷绕/流量↑ + 风温↓（表 5.5/5.6）。

>"The scope of experimentation is then clearly defined, thereby eliminating the trial-and-error approach and leading to significant savings in time and effort." (p.123)

## Source Quality 源文质量注记

- ✅ 亮点：取向-应力唯一关系与应力-光学定律逻辑清晰且多源数据支撑；敏感性分析给出可操作的变量优先级；三案例示范仿真替代试错。
- ⚠️ 不足：模型基于**单丝恒定张力假设**，作者自承多丝束（multifilament）冷却不均需另建模（p.101）；关键物性关联（5.5）（5.6）多来自作者私人通讯，外部可重复性差，且 **IV > 0.9 时粘度被低估**（p.103–104）[推断：多丝束冷却差异在 Dutta [18] 处提及但本章未展开]。
- ⚠️ 案例属数值 what-if，**缺少独立实验对照**；图 5.4–5.10 曲线斜率定量依赖具体关联式，**外推至非 PET 体系需谨慎**；工业验证仅覆盖 PET 且卷绕速度 ≤ 3000 m/min（p.112）。

## Hygiene Implication 卫材关联

- **"仿真替代试错"的方法论可直接复制到纺粘/熔喷线**：本章证明"先建模 → 敏感性排序 → 界定实验范围"能把工艺开发从试错转为定向搜索；对 PP 纺粘提速、熔喷细旦化这类高成本试产，同样的路径可显著压缩试验次数。见 [[Nonwoven Process Classification（非织造布工艺分类）]] 与 [[Meltblown Nonwoven（熔喷非织造布）]]。
- **1 % → 10 % 放大律与第 4 章互相印证**：第 4 章给出"1 % 挤出温度波动 → 10 % 纺丝线应力 → 纤度 CV 恶化"（p.89），本章给出量化版本"约 3 °C ≈ 1 % → 约 10 % σL"（p.109）。对超低克重纺粘/熔喷，这意味着**熔体温度均匀性优先级高于冷却风温**（风温对 σL 几乎无影响，p.107）—— 一个反直觉但可直接用于现场排查的结论。
- **冻结线位置 L 是无纺布纤度/克重均匀性的隐性变量**：L 的稳定化（p.109–111）对应纺粘线"固化点"的沿程一致性；多孔丝束冷却不均正是单丝模型的已知盲区（p.101），在多孔纺粘板上必须另行建模。
- **IV（特性粘度）作为分子量代理量**：PP/PE 体系虽不用 IV 口径，但其等价变量熔指 MFR 同样是"分子量 → 熔体粘度 → 纺丝线应力"链条的输入，敏感性等级应与本章 IV 同级。
- **建模方法论上的对照**：本章与库内吸收仿真在方法层级上同属"机理模型 + 数值求解 + 敏感性分析"，可互为参照。见 [[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]。
- **PET 专用性提醒**：本章定量结论（C 值、η₀ 关联式、r = 0.96 的关系式）**均在 PET 体系内建立**，迁移到聚烯烃需重新标定物性关联，不宜直接外推。

## Related Sources 关联来源

- [[Manufactured Fibre Technology]] — book index
- [[Manufactured Fibre Technology Ch04 Melt-Spinning Processes]] — 上一章：熔纺产线与速度区间
- [[Meltblown Nonwoven（熔喷非织造布）]]
- [[Nonwoven Process Classification（非织造布工艺分类）]]
- [[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]

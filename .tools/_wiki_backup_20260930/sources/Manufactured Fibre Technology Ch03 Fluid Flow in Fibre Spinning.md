---
type: source
title: "Manufactured Fibre Technology Ch03 Fluid Flow in Fibre Spinning"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Manufactured_Fibre_Technology/Manufactured Fibre Technology · analysis_ch03.md.md"
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Spinning is two flow fields in series: confined shear flow inside the spinneret capillary and free-surface elongational flow along the spinline — the polymer is squirted under pressure through capillaries and pulled rapidly onto a winder as it is attenuated and solidified."
  - "Neither the Newtonian assumption nor the 'all energy dissipated in viscous resistance' assumption is valid for molten polymers and polymer solutions, which are non-Newtonian and viscoelastic."
  - "Shear flow inside the spinneret is ineffective for orientation in melt spinning (short residence time + dieswell relaxation); 'the principally important technological state is not the shear flow but extension or jet drawing.'"
  - "A Troutonian fluid has elongational viscosity equal to three times the shear viscosity; real polymer fluids may be Troutonian, tension-thinning or tension-stiffening depending on polymer, molecular-weight distribution, temperature and deformation rate."
  - "Spinnability requires elongational viscosity to increase with strain rate to stabilize the filament; otherwise a localized defect is drawn endlessly, leading to catastrophic ductile (cohesive) failure."
summary_cn: "纺丝流体力学基础：把纺丝抽象为喷丝孔内剪切流加纺丝线拉伸流的二元流场，给出 Poiseuille、幂律、Bagley 修正、Trouton 比 3 与可纺性判据，并指出取向主要来自拉伸流而非剪切流。"
tags: ["source/book", "rheology", "shear-flow", "elongational-flow", "spinnability", "melt-spinning", "Manufactured Fibre Technology"]
tags_zh: ["源摘要/书", "流变学", "剪切流", "拉伸流", "可纺性", "熔纺", "人造纤维技术"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Manufactured Fibre Technology]]", "[[Manufactured Fibre Technology Ch02 Structural Principles of Polymeric Fibres]]", "[[Meltblown Nonwoven（熔喷非织造布）]]", "[[Bicomponent Fibre Production & Performance Review — Spinneret, Crimp & Functional Masterbatch（复合纤维生产及性能探讨）]]", "[[Electrospinning（静电纺丝）]]", "[[Nonwoven Process Classification（非织造布工艺分类）]]"]
---

# Basic Principles of Fluid Flow During Fibre Spinning 纺丝过程中的流体流动基本原理

> Source: Manufactured Fibre Technology, Ch.03, pp.31–65. (Authors: V.B. Gupta & Y.C. Bhuvanesh)

## Scope 本章范围

全书的**流变学总论**（rheology fundamentals 流变学基础）：将纺丝抽象为两个串联流场 —— 喷丝孔道内的受限剪切流（shear flow 剪切流）+ 离开孔口后纺丝线上的自由表面拉伸流（elongational flow 拉伸流），并给出黏度本构、分子理论与可纺性判据。子节：3.1 引言、3.2 剪切流、3.3 拉伸流、3.4 流体流动分子理论、3.5 可纺性与流动不稳定。

>"the polymer in the form of a melt or a solution is squirted under pressure through capillaries... It is pulled rapidly onto a winder as it is attenuated and solidified to a thin filament" (p.31)

三种纺丝方法在传热传质上不同（p.32）：熔纺（melt-spinning 熔纺）、干法纺（dry-spinning 干纺）、湿法纺（wet-spinning 湿纺）。

## Shear Flow 剪切流

| 概念 Concept | 中文 | 定义 / 公式 Definition | 页码 p. |
|---|---|---|---|
| Shear flow 剪切流 | 剪切流 | "one set of parallel material planes sliding over another" | 35 |
| Newtonian fluid 牛顿流体 | 牛顿流体 | 剪切应力 ∝ 剪切速率，η 为常数 | 36 |
| Poiseuille's equation 泊肃叶方程 | 泊肃叶方程 | **Q = πPR⁴ / 8ηL**（流量 ∝ 半径四次方） | 38 |
| Pseudoplastic / shear-thinning 假塑性 | 剪切变稀 | 表观黏度随剪切速率增大而下降 | 40 |
| Power-law 幂律 | 幂律 | **τ = k(γ̇)ⁿ**，n < 1 为假塑性 | 41 |
| Viscoelastic fluid 黏弹性流体 | 黏弹性流体 | 部分能量以弹性能储存并松弛 | 42 |
| Dieswell 出口膨胀 | 模口膨胀 | 出喷丝孔后液流膨胀，源于弹性储能释放 | 42 |

>"Neither of these assumptions is valid for molten polymers and polymer solutions which are non-Newtonian and viscoelastic." (p.38)

工程修正（p.43）：**Bagley 末端修正**（有效长度 L + bR）用于真实剪切应力；幂律修正用于真实剪切速率。温度依赖用 Arrhenius 与 WLF 方程（p.46，式 3.20–3.24）。

剪切黏度的五大影响因素（p.44–49）：温度、分子量、剪切历史、分子结构、压力。

## Elongational Flow 拉伸流

- 定义（p.50）：沿流向存在速度梯度、截面积缩小、速度增大的自由表面流动。
- **Trouton 规律（Trouton ratio 特鲁顿比）**：>"the elongational viscosity is equal to three times the shear viscosity" (p.52) —— 在极低形变速率下成立，材料称 Troutonian（特鲁顿流体）。
- 高形变速率下三类行为（p.52–53，Vinogradov 聚苯乙烯、Münstedt 低密度聚乙烯实验曲线 Fig. 3.14–3.15）：**Troutonian（始终 3 倍）**、**tension-thinning（张力变稀）**、**tension-stiffening（张力变稠）**，取决于聚合物、分子量分布、温度与形变速率。
- 分子量分布影响表观拉伸黏度：Ishizuka & Koyama 宽/窄分布对比（p.53–54，Fig. 3.16）。

### 关键工艺结论 剪切流不产生有效取向

>"two facts make this mechanism ineffective in melt-spinning: 1. the residence time... is rather short; and 2. the polymer jet leaving the spinneret channel is subject to relaxation indicated by the dieswell" (p.51)

>"the principally important technological state is not the shear flow but extension or jet drawing." (p.51)

即：喷丝孔道内停留时间短 + 出口 dieswell 松弛 → 剪切取向大部分消失；纤维取向沿纺丝路径由局部拉伸速率逐步建立。

## Molecular Theories 分子理论谱系

Eyring 过渡态（局部活化）→ Rouse/Bueche（松弛谱）→ Yamamoto/Lodge（网络）→ de Gennes 蠕动（reptation 蠕动）/ Doi-Edwards → **Curtiss-Bird**（p.56–60）。

>"the Curtiss-Bird molecular theory is more general; it has been shown that the Doi-Edwards theory is a special case of the Curtiss-Bird theory." (p.60)

评判标准（p.60，Fig. 3.21）：能否预测 **M_w^3.4** 黏度-分子量标度与纵向黏度行为 —— Curtiss-Bird 表现最优。

## Spinnability and Flow Instabilities 可纺性与流动不稳定

>"elongational viscosity should increase with strain rate to stabilize the filament... a localized defect could get drawn endlessly, leading to catastrophic ductile failure." (p.61)

| 现象 Phenomenon | 中文 | 机理 Mechanism | 页码 p. |
|---|---|---|---|
| Cohesive failure 黏聚断裂 | 黏聚断裂 | 拉伸黏度不随应变速率上升 → 局部缺陷无限拉伸 | 61–62 |
| Capillary wave break-up 毛细波断裂 | 毛细波断裂 | 表面张力驱动的丝条断裂 | 61–62 |
| Dieswell / melt fracture 出口膨胀与熔体破裂 | 熔体破裂 | 弹性储能超过临界 → 表面畸变 | 63–64 |
| Draw resonance 拉伸共振 | 拉伸共振 | "Periodic fluctuations in the thread diameter"，拉伸比超临界值发生 | 64 |

作者指出：凝固快的聚合物（PET、尼龙）松弛时间短因而纺丝稳定；**聚烯烃易发生黏聚断裂**（p.61–63，Ziabicki 模型 + Kast 能量表 Table 3.4）。

## Source Quality 源文质量注记

- ✅ 亮点：概念辨析清晰（剪切流 vs 拉伸流）；理论演进脉络完整并指出 Doi-Edwards 是 Curtiss-Bird 的特例；强调非牛顿/黏弹性修正对工程计算的必要性。
- ⚠️ 不足：部分图（Fig. 3.1、3.6、3.10、3.14 等）为低分辨率扫描图，数据点难以精确读取 —— 引用其定量值需回查原书 [待验证]；分子理论节（3.4）偏定性，Rouse 松弛谱与 Curtiss-Bird β 参数未展开推导；可纺性以 Ziabicki 模型为主线，提及 Walczak 批评（p.61–63）但未完全调和，存在单边倾向。
- 证据层级：解析/理论推导 6 处 + 实验曲线 7 处 + 数据表 4 处（Table 3.1–3.4），整体"强框架、中细节"。

## Hygiene Implication 卫材关联

- **熔喷（meltblown 熔喷）就是极端拉伸流的工程化**：高速热风牵伸使聚合物在毫秒级内被拉伸到亚微米直径，其成败直接取决于 melt 的 tension-stiffening 行为与松弛时间 —— 本章的"拉伸黏度须随应变速率上升"是熔喷可纺性判据；**聚烯烃易黏聚断裂**（p.61–63）正是 PP 熔喷细旦化与"飞丝/断丝"缺陷的机理根源。见 [[Meltblown Nonwoven（熔喷非织造布）]]。
- **喷丝板（spinneret 喷丝板）设计的半径⁴效应**：Poiseuille 指出 Q ∝ R⁴，孔径公差被四次方放大 → 多孔板孔间均匀性直接决定纤度 CV 值；而 dieswell 意味着出口胀大必须计入孔长径比（L/D）设计。见 [[Bicomponent Fibre Production & Performance Review — Spinneret, Crimp & Functional Masterbatch（复合纤维生产及性能探讨）]]。
- **双组分纤维的皮芯分层在剪切流中不混合**：孔道内停留时间极短（p.51），PE/PP 两组分在层流剪切下保持界面清晰 —— 这是皮芯型（sheath-core 皮芯）复合纺丝组分不互窜的流体力学前提。
- **纺粘线提速的物理上限 = draw resonance**：拉伸比超临界即出现丝条直径周期性波动（p.64），对应纺粘高速度下的克重条纹与纤度不均，是提速项目的核心约束。见 [[Nonwoven Process Classification（非织造布工艺分类）]]。
- **取向来自拉伸而非剪切 → 牵伸区才是性能调控区**：对 ES 纤维潜在卷曲（latent crimp）与热风布回弹，调控点应在纺丝线牵伸与冷却段而非喷丝板内。
- **静电纺（electrospinning 静电纺丝）同样受可纺性判据约束**：射流稳定段依赖拉伸黏度与松弛时间，可类比本章断裂机制。见 [[Electrospinning（静电纺丝）]]。

## Related Sources 关联来源

- [[Manufactured Fibre Technology]] — book index
- [[Manufactured Fibre Technology Ch02 Structural Principles of Polymeric Fibres]] — 上一章：取向/结晶的结构后果
- [[Meltblown Nonwoven（熔喷非织造布）]]
- [[Bicomponent Fibre Production & Performance Review — Spinneret, Crimp & Functional Masterbatch（复合纤维生产及性能探讨）]]
- [[Electrospinning（静电纺丝）]]
- [[Nonwoven Process Classification（非织造布工艺分类）]]

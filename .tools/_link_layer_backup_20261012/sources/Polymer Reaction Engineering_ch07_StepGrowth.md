---
type: source
title: "Polymer Reaction Engineering_ch07_StepGrowth.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Polymer Reaction Engineering (Asua)/chapters/Polymer Reaction Engineering_ch07_StepGrowth.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# Polymer Reaction Engineering_ch07_StepGrowth.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Polymer Reaction Engineering (Asua)/chapters/Polymer Reaction Engineering_ch07_StepGrowth.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# Polymer Reaction Engineering_ch07_StepGrowth.md.md

# Chapter 7 深度拆解报告 — Step-Growth Polymerization

源书：Polymer Reaction Engineering, Edited by José M. Asua, Wiley-VCH
章节：Chapter 7 "Step-Growth Polymerization" by Kyu Yong Choi and Kim B. McAuley
页码：PDF pages 295–337（书内 274–313 + references）
业务聚焦：卫材创新研发——PET/PET 芯层材料（ES 纤维）、PA 尼龙（热熔胶 / 底膜）、Carothers 方程在交联设计中的应用

## 一、执行摘要（中文）

Carothers 方程是卫材芯层分子量设计的"主控开关"：$DPn = \frac{2}{2 - p f^*_{av}}$（Eq. 7.20），直接联系功能基转化率 $p$、平均官能度 $f^*_{av}$ 与数均聚合度。对 PET 芯层：$p$ 每提高 0.01（如从 0.98 → 0.99），$DP_n$ 从 50 提升到 100；对 AA+BB 型非等摩尔比体系，$DP_n = \frac{r+1}{2r(1-p)+1-r}$（Eq. 7.11），仅 1% 的等摩尔偏差（r=0.99）即导致 $DP_n$ 从 100 降到 66.8（−33%）——这是 PET/PA 工业化生产中最敏感的工艺指标。

凝胶点（gel point）预测是 SAP 交联设计、ES 纤维交联 PET 芯层设计的"红线"：Flory 临界分支系数 $\alpha_c^* = 1/(f^*-1)$（Eq. 7.21 后），$f^*=3$ 时 $\alpha_c^* = 0.5$，$f^*=4$ 时 $\alpha_c^* = 0.333$。书中 Example 4 演示：A4+AA+BB 体系在 ~68% 转化率 即出现凝胶（$DPn$ 仅 4.76），远低于 Carothers 的 $p=2/f^*_{av}=0.857$。这意味着实际凝胶在数均链长仍很小时就开始出现——为 ES 纤维 PET 交联剂用量与 SAP 交联度设定了安全边界。

MPD（最可能分布 / 舒尔茨-弗洛里分布）P(n) = p^{n−1}(1−p) 是线性逐步聚合的理论基线；PDI = 1 + p ≈ 2.0 是卫材 PET/PA 产品规格的关键质量判据，若实测 PDI 显著偏离 2，说明体系已偏离纯线性假设（有支化、环化或副反应）。

PET 工业建模的两阶段范式（melt + SSP）：熔融缩聚 + 固相聚合 SSP，温度介于 $T_g < T < T_m$（260–280°C），通过移动床反应器（Figure 7.5）在真空或 N₂ 气氛下进一步去除 EG。这是卫材 ES 纤维高粘度指数（IV）PET 芯层的生产基线。

PA 热熔胶/底膜的工艺核心是"先加水后脱水"：Nylon 6,6 生产先在 50 wt% 水中溶解 HMD + adipic acid 制成盐，然后真空脱水；Nylon 6 采用 caprolactam 水解开环聚合，末端需热水萃取去除 10–12 wt% 环状低聚物。这对 PA 热熔胶的熔融流动性、底膜的耐热性设计至关重要。

平衡常数 $K_a$ 决定聚合上限：聚酯 $K_a \approx 0.5$（Eq. 7.27）→ 平衡转化率 $p_e = 0.414$，若不去除副产物，$DP_n$ 只有 1.7；聚酰胺 $K_a \approx 100$，明显更利于高聚物形成。这是"真空脱 EG/脱 H₂O 是 PET/PA 工艺不可省略的关键步骤"的热力学根源。

卫材业务启示：ES 纤维 PET 芯层的分子链设计由 Carothers 方程 + MPD 主导；支化/交联由 Flory 凝胶点理论主导；PA 热熔胶/底膜的 $K_a$ 和环状低聚物控制决定其加工窗口；SAP 交联设计则依赖 $\alpha_c^*$ 与功能度组合的定量预测。

## 二、章节概览

|||||
|---|---|---|---|
|7.1|Introduction|逐步聚合定义、AB 型 vs AA+BB 型、常见工业聚合物表 7.1、与链式聚合的对比、多种聚合工艺（熔融/溶液/界面/乳液/固相）|PET（Table 7.1 首列）、Nylon 6,6、PA 6,12、RIM 聚氨酯|
|7.2|Polymerization kinetics and modeling|动力学建模目标、MPD（Eq. 7.4）、非等摩尔比（Eq. 7.11）、非线性逐步聚合、Carothers 方程（Eq. 7.20）、Flory 凝胶点（Eq. 7.21）|全部公式均为卫材核心公式|
|7.3|Industrial step-growth products, processes and modeling|PET 生产与建模（三阶段：酯化-预聚-终缩聚）、PA 6 与 PA 6,6 生产（HMD 逃逸、热降解）、功能团建模 vs 分子物种建模、SSP 动态模型|卫材 PET 芯层、PA 热熔胶工艺的直接映射|
|7.4|Summary|全书总结|—|

## 三、Step 1 宏观定位

### 1.1 学科定位

逐步聚合（Step-Growth Polymerization）与活性聚合（第 4 章）、自由基聚合（第 2 章）构成高分子反应工程的三大支柱。本章聚焦通过官能团之间的逐步反应形成高分子链的一类反应，特点是：
- 任何两个含适当官能团的分子（单体、低聚物、聚合物）都可以相互反应
- 分子量随官能团转化率 p 缓慢累积，最终期转化率微小提升即可带来分子量大幅跃升
- 反应可逆，需移除缩合副产物才能推动向高聚物方向
- 工业聚合物分子量（如 PET $M_n \approx 20\,000$ g/mol）远低于链式聚合，但极性重复单元带来的分子间作用力弥补了此不足

### 1.2 卫材业务锚定

|||||
|---|---|---|---|
|ES 纤维芯层|PET / PET-G|AA+BB 型熔融缩聚 + SSP|Eq. 7.11、Eq. 7.20、SSP 模型|
|ES 纤维皮层（热可熔层）|PP 嵌段共聚物|无（链式）；但可与 PET 交联|Flory 凝胶点理论|
|底膜|PA6 / PA6,6 / PE|AA+BB 型缩聚|Eq. 7.23–7.25、Eq. 7.39、热降解模型|
|热熔胶|PA 尼龙 / PO / EVA|缩聚 + 交联|Carothers + Flory 凝胶点|
|SAP 交联剂设计|丙烯酸 / 丙烯酸酯共聚 + 交联剂|非线性逐步 / 自由基 + 逐步交联|$\alpha_c^* = 1/(f^*-1)$|
|湿强剂 / 粘合剂|缩醛树脂 / 酚醛|非线性逐步聚合|Flory 分支系数模型|

### 1.3 与全书其他章节的衔接

- 第 1 章 Table 1.4 / 1.5 对比逐步 vs 链式
- 第 2 章 Eq. 2.84 MPD 的另一形式；2.3 章矩方法（moment method）
- 第 3 章 反应器的 CSTR/PFR 建模基础（本章 Example 8 的 film-bulk 双相模型）
- 第 4 章 活性聚合对比
- 第 7 章是卫材业务中 PET/PA 类材料唯一的权威反应工程章节
## 四、Step 2 中观章节拆解（6 模块）

### 2.1 核心论点表

|||||
|---|---|---|---|
|1|高转化率（p → 1）是获得高 $DP_n$ 的必要条件：$DP_n = 1/(1-p)$，p=0.99 → $DP_n$=100|7.2.1|PET 芯层 IV 目标值的直接决定因素|
|2|等摩尔比是 AA+BB 型体系的生死线：r=0.99 即 −33% $DP_n$|7.2.2|PET 芯层原料配比的工艺精度要求|
|3|可逆反应 + 副产物移除 = 高分子量的前提|7.1.2、7.3.1|真空脱 EG/脱 H₂O 工艺不可省|
|4|多官能度单体 → 支化 → 凝胶；Carothers 给出 $DP_n \to \infty$ 的边界，Flory 给出首分子出现的概率边界|7.2.3|SAP 交联剂设计、ES 纤维交联 PET 的安全窗口|
|5|PDI ≈ 2.0 是线性逐步聚合的"指纹"；偏离 2 说明支化 / 副反应发生|7.2.1 Eq. 7.8|卫材 PET/PA 产品的内在质量标准|
|6|SSP 是在低分子量预聚物基础上进一步升 M_n 的工业化方法|7.3.1|高 IV PET 芯层（纺丝级）的标准路线|
|7|热降解是 PA 尼龙高温熔融缩聚的"双刃剑"|7.3.2.2|PA 底膜/热熔胶加工温度的上限|

### 2.2 关键概念操作化定义

|||||
|---|---|---|
|Step-Growth Polymerization|逐步聚合|任何两个含合适官能团的分子间均可反应；分子量随转化率缓慢累积|
|Functional Group Conversion, p|官能团转化率|已反应的官能团数 / 初始官能团数；对线性 AB 型，等于单个官能团已反应的概率|
|Stoichiometric Ratio, r|等摩尔比|$r = N_{A0}/N_{B0} < 1$（B 过量时）|
|Most Probable Distribution (MPD)|最可能分布 / 舒尔茨-弗洛里分布|$P(n) = p^{n-1}(1-p)$；对应数均链长的理论分布|
|Number-Average Degree of Polymerization, $DP_n$ / $X_n$|数均聚合度|$\frac{\text{初始分子数}}{\text{最终分子数}}$；AB 型 $= 1/(1-p)$|
|Polydispersity Index, PDI|多分散指数|$DP_w / DP_n = 1 + p \approx 2$（高转化率）|
|Average Functionality, $f^*_{av}$|平均官能度|$f^*_{av} = \sum n_i f^*_i / \sum n_i$（等摩尔体系）|
|Carothers Equation|Carothers 方程|$DPn = \frac{2}{2 - p f^*_{av}}$（Eq. 7.20）|
|Branching Coefficient, $\alpha^*$|分支系数|一个分支单元上的某官能团经双官能团序列到达另一分支单元的概率|
|Gel Point|凝胶点|体系中开始出现无限大网络分子（凝胶）的临界状态；$\alpha_c^* = 1/(f^*-1)$|
|Solid-State Polymerization (SSP)|固相聚合|温度介于 $T_g < T < T_m$，通过 N₂/真空去除副产物，进一步升 $M_n$|
|Functional-Group Modeling|功能团建模|对官能团浓度建立微分方程，简化版（9 个 ODE）|
|Molecular-Species Modeling|分子物种建模|对每个链长的分子分别建立 ODE，无穷组（需截断）|

### 2.3 证据链

[假设] Equal Reactivity of Functional Groups (7.2.1 首段)
    ↓
[公式推导] P(n) = p^{n-1}(1-p)  (Eq. 7.4)   ← MPD
    ↓
[推论] DPn = 1/(1-p) ; DPw = (1+p)/(1-p) ; PDI = 1+p (Eq. 7.8)
    ↓
[推广 AA+BB] DPn = (r+1) / [2r(1-p) + 1-r]  (Eq. 7.11)
    ↓
[验证] r=1 时退化为 1/(1-p)；r=0.99, p=0.99 → DPn=66.8 (vs 100)
    ↓
[推广非线性] DPn = 2 / [2 - p f^*_av]  (Eq. 7.20 Carothers)
    ↓
[Carothers 边界] DPn → ∞ as p → 2/f^*_av
    ↓
[Flory 更精确预测] α* = pA·pB·ρ* / [1 - pA·pB·(1-ρ*)]  (Eq. 7.21)
    ↓
[凝胶判据] α*_c = 1/(f^*-1)
    ↓
[数值验证 Example 4] A4+AA+BB：Carothers p=0.857；Flory 首凝胶 pB=0.677
    ↓
[工业建模] PET 三阶段：酯化 → 预聚 → 终缩聚（Figure 7.4）
[工业建模] PA 6,6：盐水浴 → 高压自聚 → 真空 → SSP（Figure 7.8）
[工业建模] SSP 移动床 PDE 模型（Table 7.6）

### 2.4 段落级微观精读（精选 8 段）

段落 1（§7.1 首段）
> "In step-growth polymerization, polymer linkages occur between macromolecules containing reactive functional groups... the polymer molecular weight increases gradually with functional-group conversion."
- 解读：逐步聚合的"逐步"二字意味着链增长不是爆发式的，而是每步都生成新的活性端基。这决定了工业反应器设计（长停留时间、多级反应）与卫材 PET 芯层"先酯化-再预聚-再终缩聚"的三阶段结构。

段落 2（§7.1.2 第 3-5 段）
> "To prepare polymers of high molecular weight, the reaction must be driven to very high conversions, which

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Polymer Reaction Engineering (Asua)/chapters/Polymer Reaction Engineering_ch07_StepGrowth.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Polymer Reaction Engineering (Asua)/chapters/Polymer Reaction Engineering_ch07_StepGrowth.md.md`
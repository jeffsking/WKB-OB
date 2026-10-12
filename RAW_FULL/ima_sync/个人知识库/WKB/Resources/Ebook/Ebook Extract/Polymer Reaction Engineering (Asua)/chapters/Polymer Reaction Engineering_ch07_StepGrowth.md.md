---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_c45785239fb2aa02507c23ad716e5e80001a693ee6c0644e"
source_file: "Polymer Reaction Engineering_ch07_StepGrowth.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Polymer Reaction Engineering (Asua)/chapters/Polymer Reaction Engineering_ch07_StepGrowth.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

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
> "To prepare polymers of high molecular weight, the reaction must be driven to very high conversions, which can lead to the reaction medium becoming very viscous... mass transfer is often the rate-controlling factor in step-growth polymerizations."
- 解读：这是PET 终缩聚反应器设计的第一原理——高转化率 → 高粘度 → 副产物扩散受限 → 传质控速。卫材工厂终缩聚采用 wiped film / rotating disk 反应器（Figure 7.4）正是为了解决这个问题。

段落 3（§7.2.1 MPD 推导）
> "P(n) = p^{n−1}(1 −p) ... the probability that it will have chain length n ... This same distribution also arises in some chain-growth polymerization systems."
- 解读：MPD 是随机聚合的理论指纹。卫材 PET/PA 的实测 PDI 若偏离 2（如 2.3–2.8），说明工艺中已出现非均匀混合或支化副反应，需要工程干预。

段落 4（§7.2.2 Example 1）
> "if the composition is just 1% different from the ideal stoichiometric ratio, the molecular weight decreases by 33%! A nearly perfect stoichiometric ratio of the functional end-groups must be maintained to obtain high-molecular weight step-growth polymer."
- 解读：这是卫材 PET 芯层配方设计的"铁律"。PTA:EG 摩尔比 1.0:1.4（§7.3.1）或 1.0:1.8（DMT 路线）的设定，正是为了在 EG 挥发后实现精确等摩尔。

段落 5（§7.2.3 Carothers 方程）
> "DPn = 2 / (2 − p f^*_{av}) ... DPn → ∞ as p → 2/f^*_{av}. So, if f^*_{av} ≥ 2, and the conversion of limiting functional groups is sufficiently large, the number-average chain length can become infinite, and gelation of the polymer occurs."
- 解读：Carothers 方程给出数均链长趋近无穷的几何边界。但对卫材 SAP 交联设计来说，Carothers 的边界偏保守——实际凝胶点出现在更早的转化率。

段落 6（§7.2.3.2 Flory 凝胶点）
> "α*_c = 1/(f^*−1). This critical value can be used to solve Equations 7.21 and 7.22 for the conversion of the limiting functional group when large gel molecules first appear."
- 解读：Flory 用概率方法给出首凝胶分子出现的条件。$f^*=3$（如甘油）→ $\alpha_c^*=0.5$；$f^*=4$（如季戊四醇）→ $\alpha_c^*=0.333$。这是SAP 交联剂选择和用量设定的核心公式。

段落 7（§7.3.1 PET 工艺）
> "The finishing (polycondensation stage) reactor requires large surface areas for the removal of ethylene glycol from the viscous polymer melt. Several different types of reactors are used ... including: cage reactors, rotating disk reactors, wiped film reactors and extruder type reactors."
- 解读：这是卫材 ES 纤维高 IV PET 芯层工业生产的真实反应器类型清单，直接对应卫材工厂的工艺选型。

段落 8（§7.3.2.2 热降解）
> "This example shows the kinetic schemes that have been used to account for thermal degradation in high-temperature melt-phase nylon 6,6 polymerization. Reducing the water concentration ... increases the net rate of polycondensation, but also increases the rate of degradation reactions."
- 解读：这是 PA 热熔胶 / 底膜加工温度的双约束：脱水利于缩聚升 M_n，但也加速降解。卫材 PA 底膜加工需要精确的温度-水分平衡窗口。

### 2.5 业务连接点

|||||
|---|---|---|
|Carothers Eq. 7.20|PET 芯层 $M_n$ 目标 → 转化率目标 → 真空度 / 停留时间设定|工艺参数设定的定量基线|
|Eq. 7.11 非等摩尔比|PTA:EG 配比精度 → $DP_n$ 预测 → 产品 IV 合格率|原料配比容忍度（±0.5% 以内）|
|MPD + PDI = 1+p|产品 PDI 作为工艺诊断指标|质量问题溯源（PDI 偏离 2 → 副反应 / 混合不均）|
|Flory 凝胶点 $\alpha_c^*$|SAP 交联剂用量上限；ES 纤维 PET 交联度设计|凝胶出现前的安全边界|
|聚酯 $K_a \approx 0.5$|真空脱 EG 是 PET 工艺不可省略步骤|反应器设计（真空度 ≥ 15 mmHg）|
|PA $K_a \approx 100$|PA 缩聚比 PET 更容易，但热降解更显著|PA 底膜温度窗口设定|
|SSP 模型（Table 7.6）|高 IV PET 芯层的终段升 $M_n$ 工艺优化|SSP 反应器尺寸 / 停留时间|
|功能团建模 vs 分子物种建模|PET/PA 工艺模拟：功能团建模 9 ODE vs 分子物种建模无穷 ODE|建模复杂度与精度取舍|

### 2.6 学术对话与批判

- Flory (1953) 的概率凝胶点理论 vs Carothers (1936) 的平均场凝胶点理论：本章明确给出两者数值差异（Example 4 中 p=0.677 vs 0.857），为读者提供了选择合适模型的判据。
- 功能团建模 vs 分子物种建模：本章坦承"molecular-species modeling is more complex than functional group modeling"（§7.3.1.1），并提供 9 ODE vs 无穷 ODE 的对比，是卫材研发人员实际建模时的重要取舍参考。
- Schaffer 2004 修正 Steppan 1991 的热降解模型：本章展示了一个学术模型迭代的真实案例，从 5 步反应扩展为 11 步，增加环戊酮、NH₃ 生成等副反应——这本身就是PA 工业建模持续改进的样板。
## 五、Step 3 核心概念深挖（6 个概念）

### 5.1 Carothers 方程（Carothers Equation）

英文原文：
> "DPn = 2 / (2 − p f^*_{av})" — Eq. 7.20
> "Note that the development of Equation 7.20 assumes that each step-growth reaction converts two molecules into one larger molecule (i.e., that cyclization reactions can be neglected)."

概念内涵：Carothers 方程是逐步聚合最简洁、最实用的聚合度预测工具，将数均聚合度 $DPn$ 表示为转化率 $p$ 与平均官能度 $f^*_{av}$ 的显函数。

卫材应用场景：
| 场景 | 输入参数 | 输出 |
|---|---|---|
| PET 芯层 $M_n$ 目标设定 | $f^*_{av}=2$，目标 $M_n = 20\,000$ g/mol（~100 重复单元） | $p = 1 - 1/DP_n = 0.99$（99% 转化率） |
| PET 芯层工艺偏差分析 | $r = 0.995$，$p = 0.99$ | $DPn = 1.995 / [2×0.995×0.01 + 0.005] = 74.7$（损失 25%） |
| SAP 交联剂设计 | $f^*_{av}=2.5$，目标凝胶 | $p_{gel} = 2/2.5 = 0.80$（转化率达 80% 时出现凝胶） |
| ES 纤维 PET 交联 | $f^*_{av}=2.2$，$p = 0.95$ | $DP_n = 2/(2-0.95×2.2) = 24.2$；凝胶边界 $p = 2/2.2 = 0.909$ |

关键限制：假设无环化；对含大量环状低聚物的体系（如 melt PET 1.4–1.8 wt% cyclic oligomers）会高估 $DP_n$。

### 5.2 Flory 凝胶点理论（Flory Gel Point Theory）

英文原文：
> "α* = pA·pB·ρ* / [1 − pA·pB·(1 − ρ*)]" — Eq. 7.21
> "α_c = 1 / (f^* − 1)"
> "This same thinking can be extended to systems with crosslinking monomers that have any arbitrary functionality f^*."

概念内涵：Flory 用概率方法预测首凝胶分子出现的转化率。核心是分支系数 $\alpha^*$（一个分支单元上的官能团经双官能团序列到达另一分支单元的概率），当 $\alpha^* > \alpha_c^*$ 时体系中出现无限网络。

卫材关键数值：
| 交联剂功能度 $f^*$ | $\alpha_c^*$ | 卫材应用 |
|---|---|---|
| 3（甘油类、三羟甲基丙烷） | 0.500 | ES 纤维皮芯交联 |
| 4（季戊四醇、苯六醇） | 0.333 | SAP 高度交联核心 |
| 6（六官能度） | 0.200 | 高强度凝胶体系 |

Example 4 数值演示（书中原文数据）：
> "Very large gel molecules will begin to appear at about 68% conversion of the limiting functional groups. At this conversion, the number-average chain length (including the large number of unreacted monomer molecules) will be only DPn = 2/(2−0.677(2.3333)) = 4.76"

- Carothers 预测：$p = 2/f^*_{av} = 2/2.3333 = 0.857$（85.7%）
- Flory 预测：$p_B = 0.677$（67.7%）
- 差异：Flory 更早 18 个百分点——这是卫材 SAP 交联设计必须用 Flory 而非 Carothers 的根本原因。
### 5.3 最可能分布（Most Probable Distribution / Schulz-Flory Distribution）

英文原文：
> "P(n) = p^{n−1}(1 − p)" — Eq. 7.4
> "DPn = 1/(1 − p)" — Eq. 7.8a
> "DPw = (1 + p)/(1 − p)" — Eq. 7.8b
> "The polydispersity index (PDI) (=DPw/DPn) is 1 + p. Since p is very close to 1.0 for linear high-molecular-weight step-growth polymers, the polydispersity is very close to 2.0."

概念内涵：在等反应性假设下，AB 型逐步聚合产物的链长分布由 MPD 精确描述。这是一个几何分布，意味着：
- 单体摩尔分数总是最高的
- 链长分布随 $p$ 增加向右侧展宽（Figure 7.1）
- PDI = 1+p → 2.0（$p \to 1$）是线性逐步聚合的"指纹"

卫材应用：
- PET 芯层产品 PDI 2.0–2.2 → 正常线性聚合
- PDI 2.3–2.8 → 有支化副反应或温度不均
- PDI > 3.0 → 严重副反应，需工艺干预

### 5.4 非等摩尔比效应（Non-Stoichiometric Composition）

英文原文：
> "DPn = (r + 1) / [2r(1 − p) + 1 − r]" — Eq. 7.11
> "if r = 0.99 (1% excess B groups) and p = 0.99, then ... DPn = 66.8. On the other hand, if r = 1 and p = 0.99 then DPn = 100. This example illustrates that, if the composition is just 1% different from the ideal stoichiometric ratio, the molecular weight decreases by 33%!"

概念内涵：AA+BB 型体系中，等摩尔比是实现高分子量的第一前提。$r$ 偏离 1 时，过量官能团无法参与反应，最终成为"链终止剂"。

卫材 PET 工艺映射：
- PTA:EG 摩尔比 1.0 : 1.4（TPA 路线）或 1.0 : 1.8（DMT 路线）（§7.3.1）
- 初始 EG 过量是为了在酯化阶段提供溶剂、吸收水分、并补偿后续蒸发损失
- 1% 的 HMD 蒸发损失（Example 2）同样会导致 $DP_n$ 从 100 降到 67
- 单官能团杂质 2%（Example 3）：$DP_n$ 从 50 降到 25（减半）

### 5.5 PET 后缩聚 / SSP（Solid-State Polymerization）

英文原文：
> "SSP of the semicrystalline polymer particles is carried out at a temperature above the glass transition temperature (Tg) to provide mobility of reactive end groups in the amorphous phase of the polymer particles, and below the polymer's melting point (Tm) to prevent the sticking of polymer particles."

> "the diffusion rate of condensates (water, methanol, ethylene glycol) from the particle interior to the surrounding gas phase has the strongest effect on the rate of SSP and on polymer molecular weight."

概念内涵：SSP 是在熔融缩聚之后进一步提升 $M_n$ 的关键工艺。温度窗口 $T_g < T < T_m$（PET: 80°C < T < 255°C，实际操作 ~200–230°C），水分/EG 通过颗粒内部扩散→蒸发移除。

卫材 SSP 关键参数（§7.3.1 + Table 7.6）：
- 停留时间：6–24 小时（Nylon 6,6）
- 反吹气：N₂（200°C）
- 颗粒结晶度：先退火结晶防止烧结
- 反应器：移动床（Figure 7.5）
- 质量传质控速（与熔体终缩聚一致）

### 5.6 平衡常数与 $K_a$（Equilibrium Constant）

英文原文：
> "For polyesters, a typical value of the equilibrium constant, Ka, is approximately 0.5 at the conditions used in melt-phase reactors... pe = 0.414. As a result ... DPn = 1/(1−0.414) = 1.707."
> "for polyamides, Ka ≈ 100"
> "Ka = kp/kr = Keq·(γAγB)/(γZγW)" — Eq. 7.39

概念内涵：$K_a$ 决定反应平衡位置；$K_a < 1$ 的体系（聚酯）必须强力移除副产物才能形成高聚物；$K_a \gg 1$ 的体系（聚酰胺）更容易，但仍需脱水。

卫材应用：
| 聚合物 | $K_a$ | 平衡转化率 $p_e$ | 卫材启示 |
|---|---|---|---|
| PET | ~0.5 | 41.4% | 真空脱 EG 是生命线 |
| PA 6,6 | ~73.5（Eq. 7.42） | ~89% | 脱水要求低于 PET 但仍需真空 |
| PA 6,12 | ~53.78 | ~85% | 更疏水性，$Ka$ 与 $K_{eq}$ 关系由 γW 决定 |

## 六、Step 4 学术对话与批判

### 6.1 与 Carothers 原始工作的对话

Carothers（1936）提出的原始方程 $DP_n = 1/(1-p)$（对等官能度体系）奠定了高分子化学的基础。本章的 Eq. 7.20 是其推广到任意平均官能度的形式。批判性观点：
- Carothers 方程是平均场近似，假设每步反应减少 1 个分子
- 未考虑环化：对 PET melt 中 1.4–1.8 wt% 的环状低聚物（§7.3.1），Carothers 会高估 $DPn$
- 未考虑凝胶发生的概率性质：Carothers 的凝胶边界（$p = 2/f^*_{av}$）偏晚，实际凝胶由 Flory 理论预测的更早

### 6.2 与 Flory 理论框架的对话

Flory（1953）的概率方法是凝胶点预测的更精细工具。本章 Example 4 展示了 Carothers vs Flory 的量化差异（85.7% vs 67.7%）。对卫材业务的意义：
- SAP 交联设计必须使用 Flory，否则会严重高估安全转化率
- ES 纤维皮芯 PET 交联必须使用 Flory，否则交联剂用量上限会设定错误

### 6.3 功能团建模 vs 分子物种建模的争论

- 功能团建模（Eq. 7.3）：9 个 ODE，计算快速，适用于工程放大
- 分子物种建模（Table 7.4）：无穷组 ODE，精度更高，但计算负担大
- 批判：功能团建模假设"等反应性"，但在高转化率时粘度增加导致官能团可及性变化，该假设失效
- 卫材实践：初步工艺设计用功能团建模；精细产品优化（如 PDI 分布控制）用分子物种建模 + 矩方法
### 6.4 热降解模型的不确定性

- Steppan 1991 原始模型 → Schaffer 2004 扩展模型（5 步 → 11 步）
- 关键不确定性：$K_a$ 在不同聚酰胺间的传递（Eq. 7.39–7.42）
- 批判：表观平衡常数 $K_a$ 包含活度系数，不能直接跨聚酰胺传递；需通过 $\gamma_W$ 修正（Eq. 7.40）
### 6.5 学术空白与未来方向（从本章可推断）

- 本章未涉及生物基逐步聚合（如 PLA 开环聚合）
- 本章未讨论回收/解聚（第 7.1 段末提及"step-growth polymers easier to recycle"但未展开）
- 卫材业务延伸：回收 PET（rPET）芯层材料的 $M_n$ 与 PDI 控制、PA 热熔胶回收后的性能预测——这些是当前研究热点但本章未覆盖
## 七、Step 5 知识体系关联

### 7.1 PET 芯层知识图谱

逐步聚合理论
  ├── Carothers Eq. 7.20 → $DP_n$ 目标设定
  ├── 非等摩尔比 Eq. 7.11 → 原料配比
  ├── MPD + PDI → 产品规格
  └── Flory 凝胶点 → 交联上限
        ↓
PET 工业工艺（§7.3.1）
  ├── 酯化（160–180°C, 3–4h, PTA:EG = 1:1.4）
  ├── 预聚（260–280°C, 15–25 mmHg, 2h, DPn 15–30）
  ├── 终缩聚（rotating disk / wiped film, 高真空）
  └── SSP（移动床, Tg<T<Tm, 6–24h）→ 高 IV PET 芯层
        ↓
ES 纤维应用
  ├── 芯层 PET：高 M_n（~20,000）→ 强度
  └── 皮层 PET-G / PP：低 M_n → 热可熔

### 7.2 PA 热熔胶 / 底膜知识图谱

PA 6,6 逐步聚合理论
  ├── Equal reactivity + 可逆反应（Ka ≈ 73.5）
  ├── 非等摩尔比（HMD 挥发性，Example 2）
  └── 热降解模型（Table 7.5，11 步反应）
        ↓
PA 6,6 工业工艺（§7.3.2.2）
  ├── 盐水浴溶解（50 wt% 水）
  ├── 高压自聚（~150°C, 1–2h）
  ├── 常压蒸发（220°C, 3h, 真空）
  └── SSP 升 Mn
        ↓
PA 热熔胶 / 底膜应用
  ├── 热熔胶：中等 Mn → 熔融流动性
  └── 底膜：高 Mn → 耐热性

### 7.3 SAP 交联凝胶点设计知识图谱

非线性逐步聚合
  ├── 平均官能度 Eq. 7.18
  ├── Carothers 边界 Eq. 7.20：p = 2/f^*_{av}
  ├── Flory 分支系数 Eq. 7.21
  └── Flory 凝胶判据：α*_c = 1/(f^*-1)
        ↓
SAP 交联设计
  ├── 交联剂功能度选择（f^*=4, α*_c=0.333）
  ├── 交联剂用量上限（α* < α*_c）
  └── 转化率安全边界（p < p_gel by Flory）
        ↓
实例（Example 4 类）
  ├── A4+AA+BB：Flory p_gel = 67.7%
  └── 卫材 SAP：实际转化率需 < 60%（安全余量）

### 7.4 跨章节关联表

|||||
|---|---|---|---|
|MPD Eq. 7.4|第 2 章 Eq. 2.84|自由基聚合中的 MPD 形式|
|矩方法（moment method）|第 2 章 §2.3|从无穷 ODE 到有限方程|
|CSTR / PFR 建模|第 3 章|反应器设计基础|
|两相模型（film-bulk）|第 3 章|复杂几何反应器|
|Flory-Huggins 相互作用参数|第 2 章 + 传质章节|液-气平衡|
|活性聚合对比|第 4 章|与逐步聚合的对比|
|回收 / 解聚|全书未展开|未来方向|

## 八、Step 6 RIA 实践转化

### 8.1 RIA 卡片（5 张）

#### RIA 卡片 1：PET 芯层 $DP_n$ 目标 ↔ 工艺参数

|||
|---|---|
|R (Recall)|Carothers 方程 $DP_n = 1/(1-p)$（等官能度体系）；$p=0.99$ → $DP_n=100$ → $M_n \approx 20\,000$ g/mol|
|I (Interpret)|PET 芯层目标 IV 对应 $M_n$ 约 20,000 g/mol（~100 重复单元），需要99% 官能团转化率；工业上通过三阶段（酯化-预聚-终缩聚）+ SSP 实现|
|A (Apply)|① 设定 PTA:EG 摩尔比 1:1.4（允许 EG 挥发至最终等摩尔）；② 终缩聚真空度 ≥ 5 mmHg 以强制脱 EG；③ 若 $DP_n$ 目标 120，则 $p = 1 - 1/120 = 0.9917$（需 SSP 补量）|
|业务场景|卫材 ES 纤维高 IV PET 芯层配方设计、工艺参数设定|
|证据|Eq. 7.8a, §7.3.1（160–180°C 酯化, 260–280°C 终缩聚, 15–25 mmHg 真空）|

#### RIA 卡片 2：PA 热熔胶 $K_a$ 与水分平衡

|||
|---|---|
|R (Recall)|聚酯 $K_a \approx 0.5$ → $p_e=0.414$；聚酰胺 $K_a \approx 73.5$（Nylon 6,6 276°C）→ $p_e \approx 0.89$；$Ka = K_{eq} \cdot (\gamma_A\gamma_B)/(\gamma_Z\gamma_W)$（Eq. 7.39）|
|I (Interpret)|PA 缩聚比 PET 更容易获得高转化率，但水分控制仍是关键；水分过高（$[W]$ 高）抑制正向反应，水分过低（高温）加速热降解|
|A (Apply)|① PA 底膜加工温度窗口：225–280°C（$K_a$ 高但热降解可控）；② 热熔胶 $M_n$ 目标 ~8,000–12,000（$p \approx 0.95$–0.96）；③ 水分需控制在 0.1–0.3 wt% 区间|
|业务场景|卫材 PA 热熔胶熔融加工、PA 底膜耐热性优化|
|证据|§7.3.1.1 Example 6, §7.3.2.2 Example 10|

#### RIA 卡片 3：SAP 交联剂功能度与凝胶点

|||
|---|---|
|R (Recall)|$\alpha_c^* = 1/(f^*-1)$；$f^*=4$（季戊四醇）→ $\alpha_c^*=0.333$；Example 4 中 A4+AA+BB 体系在 $p_B=0.677$ 首凝胶|
|I (Interpret)|SAP 交联设计的安全转化率上限为 60–65%（留 10–15% 安全余量）；Carothers 的 $p=2/f^*_{av}$ 会给出偏高的估计（85.7%），不能用|
|A (Apply)|① SAP 交联剂选 $f^*=4$（季戊四醇类），用量使 $\rho^* < 0.8$；② 目标转化率 $p < 0.60$（Flory 预测 0.677，留 0.07 余量）；③ 实时监测粘度上升速率作为凝胶预警|
|业务场景|卫材 SAP 吸收芯体交联度设计、凝胶风险预警|
|证据|Eq. 7.21, Eq. 7.22, Example 4|

#### RIA 卡片 4：非等摩尔比对 PET 芯层 $DP_n$ 的影响

|||
|---|---|
|R (Recall)|$DP_n = (r+1)/[2r(1-p)+1-r]$；$r=0.99$, $p=0.99$ → $DP_n=66.8$（vs 100，−33%）；单官能团杂质 2% → $DP_n$ 从 50 降到 25|
|I (Interpret)|PET 芯层原料配比的精度要求极严；单官能团杂质（如乙二醇中的水、羟基乙酸）是隐形"链终止剂"|
|A (Apply)|① PTA 纯度 ≥ 99.9%；② EG 纯度 ≥ 99.5%；③ 在线监测末端官能团浓度（羧基端基 < 25 meq/kg）；④ 配方中可有意加入 0.1–0.5% 单官能团链终止剂以控制 $M_n$ 上限（书中原文提及）|
|业务场景|卫材 PET 芯层原料质量控制、异常批次 $DP_n$ 波动诊断|
|证据|Eq. 7.11–7.17, Example 1, Example 3|

#### RIA 卡片 5：ES 纤维皮芯交联的安全边界

|||
|---|---|
|R (Recall)|卫材 ES 纤维皮芯 PET 可通过引入少量多官能度单体（如季戊四醇 1,2,6-己三酸酯）交联；$f^*_{av}$ 略 > 2（如 2.05）|
|I (Interpret)|Carothers 边界：$p = 2/2.05 = 0.9756$；Flory 会更早出现首凝胶。卫材 ES 纤维的目标是轻度支化（提升耐热性）而非凝胶|
|A (Apply)|① 多官能度单体加入量 < 2 mol%；② 转化率控制在 $p < 0.95$（远离凝胶点）；③ 监控 PDI 变化（若 PDI > 2.5 说明支化加剧）；④ 交联度通过 DSC 玻璃化转变温度 $T_g$ 上升量间接表征|
|业务场景|卫材 ES 纤维耐热性能提升、皮芯交联设计|
|证据|§7.2.3.1, Example 4, §7.2.3.2|

### 8.2 卫材业务行动卡

|||||||
|---|---|---|---|---|---|
|A1|建立 PET 芯层原料配比精度控制 SOP（PTA:EG 摩尔比 ±0.3%）|RIA 1, 4|高|工艺工程师|$DP_n$ 波动 < 5%|
|A2|建立 SAP 交联剂用量上限计算表（基于 Flory $\alpha_c^*$）|RIA 3|高|研发工程师|凝胶事故率 = 0|
|A3|引入 PDI 在线监测（GPC）作为 PET/PA 产品质量判据|RIA 1|中|品控工程师|PDI 2.0–2.2 合格率 > 98%|
|A4|建立 PA 热熔胶加工温度-水分双约束窗口|RIA 2|中|工艺工程师|热熔胶性能合格率 > 95%|
|A5|ES 纤维皮芯交联配方安全边界评估（Flory 模型）|RIA 5|中|材料研发|交联度可控，凝胶 0 出现|
|A6|建立 PET/PA 功能团建模工具（9 ODE）用于新配方快速评估|RIA 1, 2|中|工艺模拟工程师|新配方评估时间 < 2 天|

## 九、Step 7 原文摘选索引（CSV 格式）

ID,页码,英文原文摘选,中文释义,关联概念,卫材关联
EX01,p.274,"Step-growth polymerization is important for synthesizing various types of commodity, engineering and specialty polymers such as polyesters, polyamides, polyurethanes, polycarbonates, polyarylates and silicon- and sulfur-containing polymers.",逐步聚合是合成聚酯、聚酰胺、聚氨酯、聚碳酸酯等多种商品/工程/特种聚合物的关键工艺,Polyester / Polyamide,PET 芯层、PA 底膜
EX02,p.274,"polymer linkages occur between macromolecules containing reactive functional groups... the polymer molecular weight increases gradually with functional-group conversion",高分子链之间的逐步连接；分子量随官能团转化率缓慢累积,Gradual molecular weight build-up,卫材 PET 芯层工艺长停留时间
EX03,p.275,"In this type of system, it is important to carefully control the stoichiometry of the reacting mixture so that long polymer molecules can be formed. An excess of AA or BB will limit the molecular weight.",AA+BB 体系必须严格控制等摩尔比；过量会限制分子量,Stoichiometric balance,PTA:EG 配比 ±0.3%
EX04,p.276,"the polycondensation process is reversible, so that high molecular weights cannot be obtained unless nearly all the side product (e.g., water) is removed",缩聚可逆；必须近乎完全移除副产物才能获得高分子量,Reversible polycondensation,真空脱 EG/脱 H2O 工艺
EX05,p.276,"A high-molecular-weight PET will have a number-average molecular weight approaching 20 000 g mol−1 (∼100 repeat units)",高 M_n PET 约 20,000 g/mol（~100 重复单元）,PET Mn target,PET 芯层 Mn 目标
EX06,p.277,"mass transfer is often the rate-controlling factor in step-growth polymerizations",传质通常是逐步聚合的速率控制因素,Mass transfer limitation,终缩聚反应器设计
EX07,p.279,"the assumption of complete removal of side product (W), as in Equation 7.2, is usually an oversimplification because, in practice, it is not easy to remove all of the condensation byproduct",完全移除副产物通常是过度简化；实际很难完全移除,Oversimplification,真空度/停留时间设定
EX08,p.280,"The hypothesis of equal reactivity of functional groups applies in most step-growth polymerization systems",等官能团反应性假设适用于大多数逐步聚合体系,Equal reactivity,建模基本假设
EX09,p.281,"P(n) = p^{n-1}(1 −p) ... This distribution is called the most probable distribution (MPD) or Schulz–Flory distribution.",P(n) = p^{n-1}(1-p) 是最可能分布 / 舒尔茨-弗洛里分布,MPD,Schulz-Flory distribution,PET/PA 产品 PDI 判据
EX10,p.281,"the species with the largest concentration is always the monomer, so that the number CLD is a decreasing function of chain length",数均链长分布是链长的减函数；单体摩尔分数总是最高,Number CLD shape,产品质量诊断
EX11,p.282,"DPn = 1/(1 −p) ... DPw = (1 + p)/(1 −p) ... PDI = 1 + p ≈ 2.0",数均/重均聚合度公式；PDI = 1+p ≈ 2.0,DPn / DPw / PDI,PDI 2.0 是线性逐步聚合指纹
EX12,p.283,"DPn = (r + 1) / [2r(1 − p) + 1 − r] ... if r = 0.99 and p = 0.99 then DPn = 66.8. If r = 1 and p = 0.99 then DPn = 100.",非等摩尔比 DPn 公式；r=0.99 时 DPn 降 33%,Non-stoichiometric,Eq. 7.11,PTA:EG 配比精度
EX13,p.284,"if the composition is just 1% different from the ideal stoichiometric ratio, the molecular weight decreases by 33%! A nearly perfect stoichiometric ratio must be maintained.",组成偏离理想等摩尔比 1% → 分子量降 33%；必须维持近乎完美等摩尔比,Stoichiometric balance criticality,卫材原料配比铁律
EX14,p.285,"monofunctional impurity A is 2% and the conversion is 98%, then DPn = 25; whereas if the impurity is absent ... DPn = 50, which is twice as large",2% 单官能团杂质使 DPn 减半,Monofunctional chain stoppers,原料纯度控制
EX15,p.286,"Hyperbranched polymers ... are used as functional modifiers for crosslinked polymers and as components in adhesives and coatings",超支化聚合物用作交联聚合物功能改性剂和胶粘剂 / 涂料组分,Hyperbranched polymers,卫材粘合剂改性
EX16,p.287,"DPn = 2 / (2 − p f^*_{av}) ... this is the Carothers equation (named after W.H. Carothers)",DPn = 2/(2 - p f^*_{av}) 是 Carothers 方程,Carothers Equation,Eq. 7.20,PET 芯层 / SAP 交联
EX17,p.287,"DPn → ∞ as p → 2/f^*_{av} ... gelation of the polymer occurs",p → 2/f^*_{av} 时 DPn 趋于无穷；凝胶出现,Carothers gelation boundary,卫材 SAP 凝胶边界
EX18,p.289,"α* = pA·pB·ρ* / [1 − pA·pB·(1 − ρ*)] ... α*_c = 1/(f^* − 1)",分支系数公式；临界值 α*_c = 1/(f^*-1),Flory branching coefficient,Eq. 7.21,Flory gel point,SAP 交联剂设计核心公式
EX19,p.290,"Very large gel molecules will begin to appear at about 68% conversion of the limiting functional groups. At this conversion ... DPn = 4.76",首凝胶在 ~68% 转化率出现；此时 DPn 仅 4.76,Flory vs Carothers,Example 4,SAP 交联安全边界
EX20,p.291,"Poly(ethylene terephthalate) ... is produced using ethylene glycol (EG) and either dimethyl terephthalate (DMT) or terephthalic acid (TPA)",PET 用 EG 与 DMT 或 TPA 生产,PET monomers,PTA 路线 / DMT 路线
EX21,p.291,"EG and TPA are fed at a molar rate of approximately 1.4:1 (with DMT, this ratio is 1.8:1)",EG:TPA 摩尔比 1.4:1；EG:DMT 1.8:1,PET feed ratio,卫材 PET 原料配比
EX22,p.291,"small amounts of cyclic oligomers (1.4–1.8 wt%) are produced, which are in equilibrium with the linear polymer chains",产生 1.4–1.8 wt% 环状低聚物，与线型聚合物链平衡,Cyclic oligomers,卫材 PET 产品杂质控制
EX23,p.292,"SSP of the semicrystalline polymer particles is carried out at a temperature above Tg ... and below Tm",SSP 在 Tg<T<Tm 温度范围内进行,SSP temperature window,卫材高 IV PET 芯层工艺
EX24,p.293,"For polyesters, Ka ≈ 0.5 ... pe = 0.414 ... DPn = 1.707. For polyamides, Ka ≈ 100.",聚酯 Ka≈0.5 平衡转化率 41.4%；聚酰胺 Ka≈100,Equilibrium constant Ka,PET vs PA 缩聚难易度
EX25,p.296,"It is critical to remove the reaction byproduct, EG, from the reactor to promote the forward chain-growth reaction. This is why high vacuum is applied to industrial PET reactors.",必须移除 EG 副产物；这是 PET 工业反应器采用高真空的原因,Byproduct removal criticality,真空度 ≥ 5 mmHg
EX26,p.301,"Chain-growth polymerization reactions, where caprolactam adds directly to the ends of linear chains, are also important in nylon 6 production",己内酰胺直接加成到线性链端的链式反应在 Nylon 6 生产中也很重要,Nylon 6 ring-opening,PA 6 工艺
EX27,p.302,"Nylon 6,6 is made from HMD and adipic acid, producing water as a condensation byproduct",Nylon 6,6 由 HMD 和己二酸缩聚，产生水,Nylon 6,6 monomers,PA 底膜工艺
EX28,p.305,"The functional-group model has nine differential equations, whereas the molecular-species model has an infinite number.",功能团模型 9 个微分方程；分子物种模型无穷多,Functional-group vs molecular-species,建模复杂度取舍
EX29,p.308,"Reducing the water concentration ... increases the net rate of polycondensation, but also increases the rate of degradation reactions",降低水分提高缩聚净速率，但也加速降解反应,Water concentration trade-off,PA 加工温度-水分双约束
EX30,p.313,"A nearly perfect stoichiometric balance of functional group is also required. Most step-growth polymerizations are reversible, and produce a condensation byproduct that must be removed.",需要近乎完美等摩尔比；多数逐步聚合可逆，需移除副产物,Summary of key principles,卫材工艺铁律总结

## 十、结论与后续阅读建议

### 10.1 本章对卫材业务的核心价值

- PET 芯层：Carothers 方程 + 非等摩尔比公式 → 原料配比 + 转化率目标；SSP 模型 → 高 IV 产品工艺优化
- PA 底膜 / 热熔胶：$K_a$ + 热降解模型 → 加工温度-水分窗口；盐水浴-自聚-真空-SSP 四步工艺
- SAP 交联：Flory $\alpha_c^* = 1/(f^*-1)$ → 交联剂功能度选择 + 用量上限 + 安全转化率边界
- ES 纤维皮芯：MPD + PDI 判据 → 交联程度监控；Flory 理论 → 轻度支化安全窗口
### 10.2 推荐延伸阅读

- 卫材 ES 纤维：McAuley 相关文献中的 PET 终缩聚动力学模型扩展
- SAP 交联：Flory, P.J. Principles of Polymer Chemistry (1953) 第 9-11 章凝胶理论的完整推导
- PA 热熔胶：Costa and Bachmann, Polymer Processing, Wiley (2001) 第 7 章
- 回收 PET：本书未覆盖，需另找专门文献

报告撰写完成
日期：2026-08-13
源文件：/sandbox/workspace/deepread/chapters_20260813/prereac_asua_ch07.txt
报告文件：/sandbox/workspace/deepread/chapters_20260813/prereac_asua_ch07_report.md


---
type: concept
title: "Residual Fluid & Pore Stranding（残液与孔隙滞留）"
domain: [卫材研发, SAP与流体]
status: growing
updated: 2026-09-30
tags: [残液, 孔径分布, Young-LaPlace, 润湿性, 层间空隙, 毛细]
aliases: ["残液（Residual Fluid）", "孔隙滞留（Pore Stranding）"]
---

# Residual Fluid & Pore Stranding（残液与孔隙滞留）

> 一句话定义：**回渗的近因不是"吸得不够多"，而是"有液体留在了不该留的地方"**——这些液体叫**残液（residual fluid）**。它滞留在面层/导流层的孔隙里、层间空隙里或包裹层里，随后以解吸形式回到贴肤面层。因此降低回渗的正确姿势是**逐个部件清点并把残液清零**，而不是继续加大芯体容量。

## 机理 / 结构拆解

1. **残液的两个出口条件由 Young-LaPlace 方程给出**：**ΔP = −2γcosθ / R**。毛细压由**润湿性（θ）**与**孔径（R）**共同决定。**毛细压越高 → 孔越想把液体留住；解吸能越高 → 纤维越难"晾干"**。因此降低残液只有两条路：**降低润湿性（提高 θ）**或**加大孔径 R**（以及让孔径分布收敛）。
2. **孔径分布（PSD）比平均孔径更重要**：假说是**液体滞留在极小孔里，因为旁边没有足够大的孔把它拉出来**。双峰/宽分布会造成"抽不出来"的死角；对策是**让纤维尺寸趋同以收窄分布**，并**减少孔的总数以减少可拘留液体的位置**。
3. **润湿性这条路有硬冲突**：去掉面层润湿处理确实降回渗（0.26 → 0.20 g），但**漏液率从 3.2% 升到 4.6%**——因为面层不亲水就拦不住涌流。**同一处改动同时影响"干"与"漏"，必须成对验收**；且该冲突在不同品类上结论不同（未处理面层在 BCC 可行，在成人护理上不可行）。
4. **加大孔径这条路相对安全**：粗纤维 → 大孔径的面层（LOKI 类）在预测与实测上**双双优于基准面层**（0.32/0.16 g vs 0.63/0.36 g），且 DOE 确认**收益来自面层而非导流层或芯体**。
5. **导流层的陷阱是"毛细性更好 ≠ 排水更好"**：Depend 导流层毛细性优于竞品，但**因克重更高而整体排水更差**；降克重又直接伤摄入。竞品的解法是**用卷曲纤维补偿摄入**——**卷曲纤维不影响回渗**，等于把"摄入"与"残液"两个功能解耦到不同手段上。
6. **层间空隙（interstitial space）是独立的残液仓库**：两层若只是叠放，界面间隙会存液体；**提高结合强度可压缩该空隙并改善面层排空**。但**压合本身会产生小空腔**（对回渗不利）——因此**该界面的最优解是"强而均匀的结合"，而不是"更强的压合"**。
7. **结合强度 ≠ 回渗**：同一批 DOE 中，**剥离强度最高的胶种（Henkel 5402）在残液/回渗上反而劣于 Rextac RT-8723**；添加量也**"够高即可，更高无益"**。这提示界面变量的**最优区间**而非单调关系。
8. **包裹层同样会贡献残液**：数据提示 **SMS 包裹层可能抬高回渗**（成因未知），拟通过**润湿处理量梯度（0% / 0.25% / 0.50%）**验证——即**包裹层也要纳入残液清点**。
9. **清点工具是毛细测试**：整条拆解以毛细测试（解吸毛细压 + 解吸能 + 残液量）为诊断手段；该能力被明确标注为**当前瓶颈**，正在扩产设备（见 [[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]）。

## 关键参数表

| 参数 Parameter | 典型值 / 范围 Value | 出处 Source |
|---|---|---|
| 控制方程 | **ΔP = −2γcosθ / R**（γ 表面张力、θ 接触角、R 孔径） | [[War on Wetness - Adult Care Rewet Update（成人护理回渗进展 2026-03）]] |
| 判读规则 | **毛细压越高 → 孔越想留住液体**；**解吸能越高 → 纤维越难晾干** | 同上 |
| 面层润湿性改动 | 去润湿处理：**回渗 0.26 → 0.20 g**；**HUT 漏液 3.2% → 4.6%**（对照 3.1%） | 同上 |
| 面层孔径改动 | **LOKI 面层（粗纤维/大孔径）+ CT5 + Credible：预测 0.32 g / 实测 0.16 g**；基准 Fitesa + CT5 + NCSF：0.63 / 0.36 g | 同上 |
| 导流层孔径分布 | 目标：**纤维尺寸趋同以收窄 PSD**；**减少孔的数量**；现有 CT8/CT9 会降低众数孔径（可能影响摄入） | 同上 |
| 导流层克重 | 克重更高 → 毛细性更好但**整体排水更差**；降克重伤摄入；**卷曲纤维补偿摄入且不影响回渗** | 同上 |
| 层间结合 | **AD 结合强度高于 Depend（层间空隙更小）**；**LSE 的压合会产生小空腔（不利），但 LSE 净效应为正** | 同上 |
| 界面变量最优（HSBL DOE） | 胶种 **RT-8723 > Henkel 5402**；**施胶在导流层侧 > 面层侧**；**添加量够高即可，更高无益**；**花型以结合强度高者为佳**；**不压合略好** | 同上 |
| 包裹层 | **SMS 包裹层可能抬高回渗**；拟验证润湿处理量 **0% / 0.25%（对照）/ 0.50%** | 同上 |

> ⚠️ **禁止无来源参数**：上表数值来自同一份内部汇报 PPT（[[War on Wetness - Adult Care Rewet Update（成人护理回渗进展 2026-03）]]），**尚无第二来源交叉验证**；**残液量 ↔ 回渗值的定量换算系数、孔径分布的最优宽度**在本库中缺失，标 `[待验证]`。
> 🔴 **竞争情报提示 Competitive-intel note**：本页含竞品拆机结论与对照数值，**仅作机理登记**，不作对外宣称；引用前须经法务确认。

## 相邻概念

- 机理上游：[[Liquid Modes（TL-1607 液体四态）]]（残液主要位于 Mode 3/4）、[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]（残液 → 解吸型低压回渗）
- 测量手段：[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]（解吸毛细压、解吸能、残液量的直接度量，且为当前瓶颈）
- 结构对照：[[毛细梯度设计]]（用梯度把液体往下抽）、[[Median Absorption Pressure Gradient（中值吸收压梯度）]]（竞品侧的同原理量化版）
- 界面工艺：[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]、[[Liner-Surge Embossing（面层-导流层压花）]]
- 材料：[[Resilient Surge（PET 回弹导流层）]]、[[绒毛浆（Fluff Pulp）]]

## 经验教训

> ✅ 验证（2026-09-29，来源 [[War on Wetness - Adult Care Rewet Update（成人护理回渗进展 2026-03）]]）：本页为新概念页。首条来源把本库此前分散的回渗议题**统一到"残液清点"这一可操作的框架**下——不是"加大吸收"，而是"**逐个部件清零**"，并把每个部件的残液来源归因到 **Young-LaPlace 的两个变量（θ、R）**上。

- **教训**：**降回渗与防漏必须在同一次试验里验收**。去润湿处理把回渗降了 0.06 g，却把漏液率抬了 1.4 个百分点——**只看回渗会做出错误决策**。
- **教训**：**"更好"的单项指标可能整体更差**。导流层毛细性更好 ≠ 排水更好（克重更高）；剥离强度更高 ≠ 回渗更低（Henkel 强度高但 RT-8723 残液更少）。**每个界面变量都有最优区间，不是单调的**。
- **教训**：**把两个耦合功能解耦到不同手段上**。竞品用**卷曲纤维单独承担摄入**（且不影响回渗），从而让导流层可以降克重——这是"不要用一个手段解决两个问题"的范例。
- **教训**：**预测模型可用于排序，不可用于绝对值**。三组预测全部高估（0.63→0.36；0.32→0.16），但组间排序正确。
- **待补 `[待验证]`**：残液量 ↔ 回渗的定量系数；孔径分布的最优宽度与"孔数量"的度量方法；SMS 包裹层抬高回渗的成因。

## 追加：Open Innovation 批（2026-09-29 追加 · ADT 版 2026-03-31）

> 追加来源：[[ADT Rewet Update 2026-03-31（回渗进展 ADT 版）]]。**不改动上文既有结论**；本批新增的是**互换实验的量化取舍、润湿性路线的失败边界、PSD 假说的原文表述、APAC SAM 数据与机台变异证据**。

### 1. 摄入系统互换实验（本批最有价值的一组数据）

| 指标 | Depend 芯 + Depend 面层/导流层 | Depend 芯 + **AD 面层/导流层** | + 卷曲纤维 |
|---|---|---|---|
| 1st Intake（s） | **19.5** | 34.8 | 19.6 |
| 2nd Intake（s） | 37.3 | **100.5** | 49.5 |
| 3rd Intake（s） | 46.6 | **135.1** | 63.9 |
| **Rewet（g）** | **0.51** | **0.15** | 0.17 |

> ✅ **与本页既有教训完全同向**：① 回渗降到一流水平（0.51 → 0.15 g）**以摄入大幅变慢为代价**——再次证明"降回渗与摄入必须同验"；② **卷曲纤维本身无回渗收益**（0.15 → 0.17 g），只补偿摄入——印证本页"把耦合功能解耦到不同手段"的教训。**本页既有结论未被修正，而是被量化**。

### 2. ⚠️ 润湿性路线的失败边界（本页此前未记录）

| Code | Std Lkg |
|---|---|
| Control | **3.1%** |
| GRIFFIN | 3.2% |
| **Always Discreet** | 3.7% |
| **Untreated Liner** | **4.6%** |

> 中文：**竞品（AD）的"低润湿性"解法搬到 Depend 上会抬高渗漏**。这与上文"去润湿处理降回渗 0.06 g 却抬漏液 1.4 个百分点"**是同一类现象的不同尺度证据**——**降润湿性在 Depend 平台上以渗漏为代价**。

### 3. PSD 假说的原文表述（此前为转述）

> **"fluid gets trapped in small pores because large pores can't draw it out"**（液体被困在小孔中，因为大孔无法把它吸出来）。

- 操作方向：**Shalag 可降低孔径分布（PSD）**；**改善幅度与对摄入/加工的权衡仍未知**。
- 中文：这条假说把"孔径"从**单值**问题升级为**分布**问题——**决定残液的是分布的尾部（小孔），而不是平均孔径**。

### 4. APAC SAM 牌号（第二次回渗的差异）

| Sample | 1st rewet（g） | 2nd rewet（g） |
|---|---|---|
| SF-1（Stockhausen 5660, full SAM） | 0.2004 | **0.6208** |
| SF-2（Stockhausen 5660, **−1 g**） | 0.2016 | **1.2436** |
| SF-9（Sumitomo HP550, −1 g） | 0.1482 | **0.2558** |
| SF-10（Sumitomo HP550, −1.7 g） | 0.1742 | 0.5478 |

> ⚠️ **源文未给统计分组，本页不排名**。可记的方向性事实：**减 SAM 会显著抬高第二次回渗**（SF-1 → SF-2：0.62 → 1.24 g）。且源文自陈**"高压回渗由不同机制驱动，能否迁移到 Depend 不明确"**——与 [[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]] 的机制分野一致。

### 5. 机台变异证据（影响所有残液数据的可比性）

| 现象 | 观察 |
|---|---|
| **Ogden** | 回渗方向性偏高（怀疑绒毛浆设备型式不同） |
| **L14 随时间** | 与其他机台不同，**L14 回渗随时间上升**（2023→2026） |
| **Shalag 生产卷序** | **批次开头（START）的导流层做出的产品回渗高，后续卷下降**；成因源文标为未解 |
| L14 vs L18 | 指向 **pad formation**（L14 回渗更低、厚度更低、密度更高、湿态 X 光均匀性更好） |

> 中文：**同一供应商的同一导流层，在"生产批次调机期"与"稳态期"表现不同**——这意味着**残液/回渗数据必须记录生产卷序**，否则跨批次比较无效。

> ✅ 验证（2026-09-29）：本追加段**未修正**本页任何既有结论；上文三条教训（同验、非单调、解耦）均被**进一步支持**。上文标 `[待验证]` 的"残液 ↔ 回渗定量系数"**仍未闭环**——源文明确"下一步需确认残液是否可预测回渗"。

> 🔴 **manual_review（2026-09-29）**：本源为 **PRIVILEGED & CONFIDENTIAL** 内部汇报，含竞品实测数据与宣称；本页**只记技术判据与相对关系**，不落竞品性能全表。

## 追加：Open Innovation 批（2026-09-29 追加 · ActivTech Hybrid 把绒毛浆变成滞留层）

> 追加来源 `[[Depend Rewet Update 2025-04-04（LUGH 与 GRIFFIN 回渗进展）]]`（2025-04-04）。本段**只补"层数—滞留点"的结构归因与体系层序差异，不改动上文任何机理、参数与经验教训结论**。

### 1. ✅ 与上文同向：从"孔径/解吸"扩展到"层序"

| 维度 | 上文（既有） | 本批追加 |
|---|---|---|
| 归因对象 | 面层/导流层的**孔径与解吸** | **芯体体系的层序配置** |
| 核心陈述 | 残液滞留在孔隙中，受压后被挤回 | **ActivTech Hybrid（ATH）体系确认抬高回渗**；差异来自**包覆层**与 **SAM/绒毛浆配置** |
| 关键机理 | 解吸受毛细控制 | **在 ATH 体系中绒毛浆成为摄入系统的一部分**（fluff becomes part of the intake system）；**层数越多 = 液体可被滞留的位置越多** |

### 2. 层序对比（源文图示）

| 体系 System | 层序（自上而下） | 对本页的意义 |
|---|---|---|
| **SAM/Fluff System** | Liner → Surge → **Wrapsheet (Tissue)** → Fluff / SAM → **Intake System** → Retention System | 绒毛浆与 SAM 混合层归入**摄入系统之后**的保持结构 |
| **ActivTech Hybrid System** | Liner → Surge → **Wrapsheet (SMS)** → Fluff → SAM → SAM | 绒毛浆**位于 SAM 之上**，因而**参与摄入**并成为滞留点；且**包覆层由 Tissue 变为 SMS** |

> ⚠️ **口径提示**：源文把 ATH 的绒毛浆层**视为摄入层**来诊断（"considered an intake layer in ActivTech Hybrid system"），这与传统 SAM/Fluff 体系中绒毛浆的定位**不同**；本页**照录该诊断口径，不推断其是否应为通用分类**。

### 3. 对策与诊断前提（源文原话）

- **对策**：在**绒毛浆层少量加入 SAM**，促使该层**解吸（desorb）**，把液体移出摄入系统。
- **诊断前提**：**需要不含 SAM 的产品**才能完成诊断（源文："Need products without SAM for diagnosis"）。
- ⚠️ **未闭环**：本件**只给出对策方向，未给出该对策的验证结果**；上文标 `[待验证]` 的"残液 ↔ 回渗定量系数"**仍未闭环**。

### 4. 与本页"解吸"机理的关系

- 上文把**解吸**定位为回渗的控制环节之一；本批给出的是**同一机理在结构层面的实现方式**——**让绒毛浆层不再"挂住"液体**（加 SAM 使其解吸）。
- ⚠️ **并列记录**：本批另一条杠杆（**降低面层润湿性以减少毛细滞留**）与本条的**作用层与机理不同**（面层 vs 绒毛浆层），**不互推、不合并**。

> ✅ 验证（2026-09-29）：本追加段**未修正**本页任何既有结论；上文三条教训（同验、非单调、解耦）**均未被触及**。

> 🔴 **manual_review（2026-09-29）**：本源为内部汇报，含竞品实测数据、内部 HUT 编号与供应商牌号；本页**只记结构归因与对策方向，不落竞品性能全表**。

## 追加：Open Innovation 批（2026-09-29 追加 · PSD 假说的两次一致表述与 LSE 的符号争议）

> 追加来源 `[[Rewet Learning Plan（回渗学习计划工作表）]]`（推断 2026-02 前后）。本段**只补"孔径分布假说的可操作变量"与"LSE 判断的两种语气"，不改动上文任何机理、参数与经验教训结论**。

### 1. ✅ PSD 假说出现两次，机理表述完全一致

| 路线 | 假说 Hypothesis | 共同机理 |
|---|---|---|
| **Shalag（窄 PSD 导流层）** | **More similar fiber sizes will reduce distribution of pore sizes**（纤维尺寸更相近 → 孔径分布更窄） | **stranding less fluid in unconnected pockets（更少液体滞留在不连通的孔隙中）** |
| **Fitesa（树脂粘合导流层）** | **Resin-bonded surges reduce distribution of pore sizes**（树脂粘合 → 孔径分布更窄） | 同上 |

> ✅ **与上文同向**：上文已把 **PSD 假说**列为残液滞留的核心机制之一；本批给出的是**两条可操作的实现路径**（**收窄纤维尺寸分布** / **树脂粘合**），且**两条路线的机理措辞一字不差** —— 说明**"孔径分布 → 不连通孔隙滞留"在此阶段已被当作统一机理使用**。

- **进展状态**：Shalag 样品 **10/17/25 已到货**做毛细测试，下一步为**验证建议牌号的 PSD**；Fitesa 路线 **Not Started**（尚未索样）。
- ⚠️ **未闭环**：**毛细测试的验证结果本件未给出**；上文标 `[待验证]` 的"残液 ↔ 回渗定量系数"**仍未闭环**。

### 2. ⚠️ LSE 在本源中出现两种语气（并列，不裁决）

| 出处 | 表述 | 语气 |
|---|---|---|
| Sheet1（Interstitial space learning） | **"Does LSE create small pores to trap fluid, and is there a better way to achieve the same benefit?"** | **怀疑**：LSE 可能形成小孔**捕住**液体 |
| Sheet2（Liner surge attachment） | **"Although LSE is a net rewet positive, a different adhesive setup may be even better"** | **肯定**：LSE 对回渗是**净正向** |

> ⚠️ **两种语气并存，源文未调和**。本页**照录并列**——它们指向的**是同一现象的两面**（LSE 形成的间隙既可能捕液、也可能把液体拉离皮肤），**不作单向结论**。相关机理页见 `[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]`。

### 3. LOKI 面层：把"更低回渗"归因到孔径/纤维尺寸

- **假说**：*"LOKI liner results in lower rewet, and mechanism could be replicated by domestic vendors"*（LOKI 面层回渗更低，其机理**可被国产供应商复制**）。
- **验证路径**：**通过毛细测试确认 fiber size / pore size 驱动因素**，再**请美国本土供应商复制关键属性**做试产料。
- ⚠️ **尚未验证**：12/8/25 完成的是**材料属性与显微表征**，**毛细测试的结果本件未给出**。

> 🔴 **manual_review（2026-09-29）**：本源为内部工作计划表，含负责人姓名、分工与供应商试产状态；本页**只记假说、机理与进展状态，不转述竞品技术细节**。

## 追加：Open Innovation 批（2026-09-29 追加 · 滞留的三种方式与"更粗纤维"的一击多因）

来源：[[Rewet Principles（回渗设计原则与测试方法关联）]]（Updated 10/22/25，Draft 1/2/3 三版并存）。

### 1. 液体在非织造材料里"挂住"的三种方式（Draft 1 原词）

| 方式 | 源文 | 中文 |
|---|---|---|
| **Capillarity 毛细** | *"smaller pores will hang onto more fluid"*；受表面张力驱动，**润湿性处理会改变表面张力** | 孔越小滞留越多 |
| **Pore Connectivity 孔连通** | *"pores that don't connect will trap fluid"* | 不连通的孔隙会困住液体 |
| **Adhesion 粘附** | *"more fiber surface area will hold onto more fluid"*；*"Combine with capillarity"* | 纤维表面积越大滞留越多，**与毛细叠加** |

- **源文给出的"少孔"解法**：*"Less pores (i.e.: **lower BW at same density**, **non-fibrous film surge**)"* —— 即**同密度下更低克重**、或**非纤维的 film surge**。
- ⚠️ **毛细具有两面性**：*"Drawing fluid may be a desirable trait to drain fluid from upper layers into lower layers"* —— 把液体从上层往下抽**本身是想要的**，滞留只是其副作用。

> 与本页既有"**残液 = 留在不该留的地方**"口径一致：本件把"不该留的地方"细化为 **孔隙内（毛细 / 不连通）** 与 **纤维表面（粘附）** 两类位置，**不改本页结论**。

### 2. ⚠️ 解吸判据在 Draft 3 中被改为"梯度判据"

- Draft 2：*"Materials have **large pores to reduce capillarity**"* / *"Materials are **minimally wettable** to reduce capillarity"*（**绝对属性**）
- Draft 3：*"Materials have **lower capillarity and wettability compared to where fluid is locked up**"*（**相对属性**）

（中文：**孤立地测一个部件的毛细性不足以判定回渗**——必须与"锁液处"比较。这与本页"逐个部件清点残液"是同一思路的两种表述，**源文未交叉引用，故不合并**。）

### 3. Example: Larger Fibers & Desorption（更粗的纤维一击多因）

> *"Larger diameter surge fibers are a **common low rewet solution** because they **target multiple causes** of rewet."*

```
Increasing Fiber Size (at same basis wt)
  → Decreasing # of fibers
  → Decreasing surface area for adhesion
  → Decreased capillarity
  → More chances of pores connecting
  → Less fluid trapped on fibers
  → Less fluid trapped in pores
  → Fluid can drain out into core
```

（中文：同克重下增大纤维直径 → 纤维根数减少 → 粘附表面积减少 → 毛细性下降 → 孔隙连通概率上升 → 纤维上与孔隙内滞留均减少 → 液体排入芯体。）

> ⚠️ **柔软度取舍（源文明写）**：*"Since smaller fibers are perceived as softer, **softness and rewet are often opposites**."* —— **越细越软 → 柔软与回渗常相反**。

### 4. 与 Flowback 的交叉（Crossover）

- *"**Film surge** is non-fibrous (so has lower surface area) and can be a **one-way valve**"*
- *"**Less wettable fibers** reduce adhesion of fluid and can be a **buffer between core & blotter**"*

> ⚠️ 第二条与 [[Depend Rewet Update 2025-04-04（LUGH 与 GRIFFIN 回渗进展）]] 的"降低润湿性改善回渗但**依赖防漏隔边**"是**同一路线**；本源**未提隔边条件**，故**不作因果合并**。

> ✅ 验证（2026-09-29）：本追加段**未修正**本页既有结论（含 PSD 假说两次一致表述、LSE 两种语气并列、LOKI 面层归因）；补的是**滞留方式的官方三类划分**与**更粗纤维的因果链**。
> 🔴 **manual_review（2026-09-29）**：源文为 **K-C 内部原则草稿**，含内部方法编号与自评句；本页**只记机理与相对关系**，**不外发**。

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · 解吸机制的竞品实证）

> 追加来源 `[[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]]`（K-C 内部竞品分析，2025-11-20，一手实测）。本段**只补"解吸机制的量化竞品证据与一个未解释缺口"，不改动上方任何既有结论**。

### 1. ✅ 回渗的两种机制划分（与本页"滞留"主题直接对应）

- 原文：**回渗由两种机制驱动——解吸（Desorption）与回流（Flowback）**；**在 POISE 的 FIUP 测试中，解吸主导回渗**。
- **解吸由摄入系统（intake system）控制**：摄入系统中的**高毛细压力与界面会截留液体**，被截留的液体**在受压时表达为回渗**。
- 机理要素清单（原文）：解吸毛细张力 / 界面 / 回渗 / **液体可得性（availability of fluid）** / **润湿性（wettability）** / **与芯体的分离（separation from core）** / **双向流动（two-way flow）**。

> ✅ 与本页的关系：本页核心议题是"**液体以什么方式被滞留在哪里**"；本批给出**官方的两机制划分**与**"摄入系统是滞留的主要位点"**这一归因。

### 2. 竞品实测：ALWAYS DISCREET 摄入系统**更难解吸**

| 层位 | 产品 | Bn-abs1 | **Bn-des1** | 解吸能（ergs） |
|---|---|---|---|---|
| **Liner + Surge** | Poise | 3.54 | **11.58** | 1.92E+04 |
| | Always Discreet | 8.58 | **22.60** | 1.78E+04 |
| **Liner** | Poise | 3.22 | **14.90** | 3.69E+03 |
| | Always Discreet | 6.02 | **18.84** | 4.96E+03 |
| **Surge** | Poise | 3.22 | **10.38** | 1.41E+04 |
| | Always Discreet | 5.62 | **24.39** | 1.67E+04 |

- **更难解吸是双重原因**（Young-LaPlace `Δp = −2γ·cosθ/R`）：**孔径 R 更小** + **润湿性更高（θ 更小）**。滴液润湿性（0→60 s）：Liner **POISE 2.4→4.7 vs AD 8.4→9.5**；Surge **POISE 8.4→9.2 vs AD 9.6→9.8**。
- **BET 比表面积**：AD Core **17.48** vs POISE Core **1.37 m²/g**（约 **12.8×**）；AD 拆分为 composite 1 **56.25**、composite 2 **47.57**、SAM 颗粒（带胶）**0.70** → **高比表面积来自复合层，不是 SAP 颗粒**。

### 3. ⚠️ 一个**未解释的缺口**（本批最重要的保留项）

> 按机理 AD 摄入系统毛细压力全面更高 → **应回渗更高**；但**实测中 POISE 并未在回渗上碾压 AD**。原文自设问题："*Why is POISE not crushing ALWAYS DISCREET in rewet tests?*"，**并给出三个未证实的假说**：
> ① **尺寸/覆盖差异**——POISE surge 蓬松度约为 AD 的 2 倍但**易解吸**；**AD surge 与 liner 等长等宽**，而 POISE surge 仅 **50 mm 宽**、长度约为护垫一半；
> ② **AD surge 芯吸好，是否反而降低回渗？**
> ③ **高比表面积材料的作用未知**。

- ⚠️ **未鉴定项**：AD 芯材中的**涂层与球形结节**尚未鉴定；SEM 提问"**是否为 HIPE 泡沫？若是，孔在哪里？**"**未解答**。
- **Micro-CT @10 cm（0.14 psi）**：两个 liner 都**未很好解吸**，但 **AD surge 非常湿**。

> ⚠️ **引用纪律**：上列三条为**假说**，**不得当作结论引用**。本批的价值在于**登记缺口**，而不是填补它。

### 4. 一条可迁移的判据（"蓬松度 ≠ 解吸难易"）

> **POISE surge 蓬松度约为 AD 的 2 倍，却更易解吸** —— 说明**蓬松度（loft）与解吸难易是两个独立维度**：蓬松度由纤维网络几何决定，解吸由**孔径 + 润湿性**决定（Young-LaPlace）。**用蓬松度推测回渗会出错**。

> ✅ 验证（2026-09-29）：本追加段**未修正**上方任何结论；上方"滞留方式官方三类划分""更粗纤维的因果链""降低润湿性改善回渗但依赖防漏隔边"**均未被触及**。本批补的是**两机制划分、竞品量化证据、一个未解释缺口与一条可迁移判据**。
> 🔴 **manual_review（2026-09-29）**：本源为 **K-C 竞品拆解内部分析**，含**竞品结构拆解、SEM/Micro-CT 结论与未鉴定材料推测（HIPE 泡沫假说）**。依 AGENTS.md §5，本页**只记机理与实测参数**，**不落竞品配方推断与未鉴定材料的定性结论**，**不外发**。

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · 残液定位：面层自身持液与"低定量"杠杆）

> 来源：[[Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）]]（K-C 内部项目汇报）。

1. **MicroCT 把残液定位到了面层本身** —— 源文：「MicroCT showed liner is holding fluid – new opportunity to reduce rewet」；**残液不只存在于 surge/芯体，面层自身就是一个持液库**。
2. **一个决定机理归属的量级事实** —— 「**Rewet weight is much smaller than the blotter. Much of the fluid picked up as rewet with no pressure on blotter.**」（回渗重量远小于吸墨纸所吸；**在无压力下**已有大量液体被带起）⇒ **回渗的主贡献者是"本来就留在面层的液体"，不是压力下从芯体挤出的液体**。
3. **当前产品的失败位置** —— 「Our current product leaves fluid in the topmost layer near the blotter.」**液体停在最靠近吸墨纸的最顶层**，即**失效发生在最外一层，而非芯体深处**。
4. **新杠杆：更低定量（basis weight）** —— **3D topical surge 回渗大幅更低**，**主假设 = 更低定量**。**"少材料 = 少持液"是本轮最强单一解释**，与上方"更粗纤维降低持液表面积"是同一族机理的不同旋钮。
5. **新杠杆：层间互连（interconnection）** —— 次要假设是**双层压花 topical surge 具有更连通的孔隙网络，从而排空最顶层**；**抓手从"改材料表面能"扩展到"改层间孔道连通性"**。
6. **Bond pattern 假设被否（对照性证据）** —— 更开放的 bond pattern（CD Rod 10% vs Oval 18%）**未产生回渗差异**；**"更少小口袋 = 更少残液"的几何假设不成立**，提示**残液不由压合点几何主导，而由润湿性与定量主导**。
7. **系统边界决定归因** —— ActivTech Hybrid 的 "**core = 从 wrapsheet 往内的全部材料**"，因此**材料更多 + 界面更多 = 更多持液点**；**比较任何"谁更差"之前必须先定义系统边界**。
8. **诊断困难点** —— 「**Difficult to analyze where fluid sits when SAM is present**」：SAM 存在时**液体位置无法定位**；源文的解法是**做无 SAM 样品专供成像**（12/20 gsm wrapsheet × ±SAM 矩阵）。**这是一个可复用的实验设计：先拆掉最会吸水的组分，才看得见液体停在哪。**

> ✅ 验证（2026-09-29）：本追加段**未修正上方任何结论**；上方"滞留方式官方三类划分""蓬松度 ≠ 解吸难易"等结论均保持原样，本节只补**残液的新定位证据与两个新杠杆**。
> 🔴 **manual_review（2026-09-29）**：来源为 **K-C 内部项目汇报**（GRIFFIN / SIROCCO / ATACAMA / ActivTech Hybrid 内部代号与内部试样结果）；本页**只记机理与方向性结论**，**不外发**；图表数值在原文已退化为图注，**本页未提取任何 g 值**。

## 来源

- [[Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.03.26 - Raegan Informal.pptx.md`（2026-09-29 追加）
- [[War on Wetness - Adult Care Rewet Update（成人护理回渗进展 2026-03）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Updates and Presentations/2026.03.16 - Adult Care Manager Rewet Update.pptx.md`
- [[ADT Rewet Update 2026-03-31（回渗进展 ADT 版）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Updates and Presentations/2026.03.31 - ADT Rewet Update.pptx.md`（2026-09-29 追加）

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · ★ 残液被量化：解吸能量（ergs）与残液质量双指标）

> 来源：[[ATH SAM Relocation（2025-07-29 · 解吸能量·残液·microCT 与 SAM 再分配台架）]]（K-C 内部研究 + 台架）。

1. **残液有了两个可测量的量化指标** —— **① 解吸能量（desorption energy，单位 ergs）**与**② 残液质量（residual fluid mass）**；两者与 **③ microCT** 一起构成源文的三工具方案。**⇒ 本页此前的"残液"多为定性描述，本次给出了可直接比较的标量。**
2. **解吸能量实测（源文原表）**：

| 产品 | 样品质量 (g) | des1 解吸能量 (ergs) |
|---|---|---|
| Code 31 — Whole Absorbent System | **0.42** | **6.67E+04** |
| Code 32 — Whole Absorbent System | **0.42** | **6.52E+04** |
| Code 31 — LSE+CW，12 gsm dSB | **0.21** | **1.83E+04** |
| Code 32 — LSE+CW，20 gsm TABCW | **0.21** | **1.78E+04** |

3. **"系统边界"决定了残液量** —— **"完整吸收系统"（Liner + surge + CW + 绒毛浆）的解吸能量约为"LSE+CW"的 3.6 倍**（本页据源文两值计算）。**⇒ 残液不是某一层的属性，而是"你把这个系统划到哪里"的函数。**
4. **⚠️ 但本组数据有未控制的混淆** —— **完整系统样品 0.42 g vs LSE+CW 0.21 g（差 2 倍）**，源文未说明归一化。**⇒ 引用"3.6 倍"时必须连同质量差异一起说明。**
5. **第三条独立路径：microCT** —— 假设"含绒毛浆的摄入系统相对 LSE 会显示额外湿润"**Supported**；而"面层湿润度在 ATH / LSE / 商品 Depend 之间无明显差异"为 **Likely Supported 待跟进**。**⇒ 残液的差异出现在摄入系统内部，不在面层。**
6. **一条重要的负值结果（对"往持液层加吸收剂"这一思路）** —— 把 **30% / 47% 的 SAM 搬进绒毛浆层**后，**回渗由 0.34 g 变为 0.38 / 0.40 g（更差）**，且 **Open Cradle 第 3 次摄入由 65.93 s 恶化到 150.58 / 142.62 s**。**⇒ 当持液点在系统内部时，"加吸收剂"会同时改变该层的渗透通道，可能把入口堵死。**
7. **"时间尺度"被源文列为未解变量** —— 解吸是一个有时间常数的过程；**⇒ 残液不是一个静态量，而是"在多长的时间尺度上仍可被表达"的量。**

> ✅ 验证（2026-09-29）：本追加段**未修正上方任何结论**；上方"滞留方式官方三类划分""蓬松度 ≠ 解吸难易"等结论均保持原样。
> 🔴 **manual_review（2026-09-29）**：来源为 **K-C 内部研究 + 台架**；**样品质量差异（0.42 vs 0.21 g）未归一化，3.6 倍为计算值且含混淆**；含**竞品 AD 实测（回渗 0.17 g、摄入 34.80 s）**，**属竞品内部数据，不外发**；回渗图注统计阈值源文写 **0.7（疑为 0.05）**。

## 追加：孔径分布（PSD）主导排液的实证判据（2026-09-29 追加 · 来源：Rewet Update 2025-12-02 Depend 拆解）

- **决定性区分：平均孔径相近 ≠ 排液行为相同**。Depend 与 AD 导流层的**平均孔径（average pore size）相近**，但 **Depend 的 PSD 更宽、大孔更多**，回渗更差 → 直接坐实本页「孔径分布比平均孔径更重要」的判断。
- **滞留机理（假设，B）**：**小孔里的液体不会被紧邻的非常大的孔拉出来**（大孔的毛细压低于小孔，无法把小孔抽空），于是液体被 **stranded 滞留**在导流层内。与 **SIROCCO 学习**一致。
- **量化路径**：该假设的判据是**收窄 PSD 后回渗是否下降**（Shalag 已提供样品：先查 PSD，再上产品验回渗）。
- **配套设计原则（本批新增）**：
  - `The number of pores is minimized to provide less places for fluid to be trapped` —— **孔的数量要尽量少**，减少液体可被困住的位置；
  - `Pore networks are well connected, and no fluid is trapped at interfaces` —— **孔网络要连通良好，界面处不滞液**。
- **归因级证据**：摄入互换实验显示，**仅替换面层+导流层**（芯体不变）即可把 Depend 回渗从 ~0.51 g 降到 0.15–0.17 g —— 残液主战场在**摄入系统**，不在芯体容量。
- 方法论出处见 [[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]；来源页 [[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]。

> 校验：本节为 2026-09-29 追加，**未修正上方任何结论**。

## Related Sources 关联来源

- [[ADT Rewet Update 2026-03-31（回渗进展 ADT 版）]]
- [[ATH SAM Relocation（2025-07-29 · 解吸能量·残液·microCT 与 SAM 再分配台架）]]
- [[Depend Rewet Update 2025-04-04（LUGH 与 GRIFFIN 回渗进展）]]
- [[Depend Rewet Update 2025-04-04（成功标准 · LUGH-GRIFFIN-ATH 进展 · Walmart NWSP 070.9 方法对比）]]
- [[Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）]]
- [[GRIFFIN Rewet Technical Problem Statement（GRIFFIN 回渗技术问题描述 · 2025-01-31）]]
- [[HSBL Attachment Strength Results（HSBL 附着强度结果 · 2025-11-18）]]
- [[Intake Systems Tech Pipeline（吸收系统技术管线 2025-11）]]
- [[Liner-Surge Rewet Density Testing（面层-导流层密度测试数据）]]
- [[Rewet Competitive Analysis - Depend vs Always Discreet Intake System（回渗竞品分析 · 2025-09-11）]]
- [[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]]
- [[Rewet Learning Plan（回渗学习计划工作表）]]
- [[Rewet Principles History and Opportunity（2025-03-04 回渗总纲与历史沿革）]]
- [[Rewet Principles（回渗设计原则与测试方法关联）]]
- [[Rewet Quarterly Update 2025-08（设计原则落地与五个项目战绩）]]

---
type: source
title: "Rewet Quarterly Update 2025-08（设计原则落地与五个项目战绩）"
source_type: 内部季度进展汇报（Rewet · ADT · 原则 → 项目 → 竞品三段式）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Updates and Presentations/2025.08.21 - Josie Quarterly Update.pptx.md
original_link: ""
date_published: 2025-08-21
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: manual_review
key_claims:
  - "**回渗被拆成两套机理，各有独立原则集**：**Flowback（回流）**——芯体里未被锁住的液体回流至吸墨介质/皮肤，原则围绕「有足够且可达的容量」「SAM 在压力下持液且及时锁液」「未锁液与皮肤/吸墨介质隔离」；**Desorption（解吸）**——吸收层截留的液体在压力下被挤出，原则围绕「不截留液体」「孔径大 / 润湿性低 / 孔数少」「抗压以保持开孔」「孔网连通、界面无截留」「毛细梯度把液体引向锁液位」"
  - "**贯穿原则（唯一一条跨两套机理的原则）**：**每条原则都要同时评估材料与工序的变异与能力（variability and capability）**，以确保商业化执行的可靠性 ⇒ **原则是设计判据，不是材料属性清单**"
  - "**T5 BUFF BABY 的双目标**：**低压回渗 0.15 g**、**高压回渗 0.30 g**；低压侧靠 **liner-surge 压花**达标（经验来自 Depend），高压侧最大驱动是**优化后的吸收系统**（T4/T5 已压到 ~0.4 g），最新 T5 学习在**多种芯体变更下做到 <0.3 g**，但**机理尚未确认 ⇒ 不能保证稳定复现**"
  - "**五个项目均按同一套原则取得量化的回渗下降**：GRIFFIN **0.26 → 0.20 g**（无处理面层）；LUGH **0.41 → 0.34 g**（把柔软方案从「处理剂」移到「纤维」+ 调整表面活性剂）；LOKI **0.62 → ≤0.32 g**（Credible 面层，手工改制）；AC4 4U **3.8 → 1.6 g**（Textor 材料组分变更，更大纤维）⇒ **同一套原则跨品类有效**"
  - "**竞品互换实验的关键结论**：**把 Always Discreet 的面层 + 导流层换到 Depend 芯体上，就足以把 Depend 回渗降到 AD 水平**；且 **AD 的卷曲纤维（curly fiber）没有额外的回渗收益，但对摄入有益** ⇒ **AD 的干燥优势来自面层/导流层的解吸特性，而非卷曲纤维**"
  - "**竞品专利地图显示 P&G 同样在系统性处理回渗**：US 11,202,723（毛细测量方法）、US 2021/0369509（面层 phobic/philic 双面性 → 润湿梯度）、US 2022/0133554（超细纤维把液体从面层/皮肤/吸墨介质引走）、EP 2679209（100% 绒毛浆层会漏液 → 置于 SAM 层之下）、EP 3243565（日本触媒，受 P&G 约束的 SAM 属性认知）"
  - "**大纤维降回渗是一击多因的通用解**：AC4 4U 上 **1.3 d → 2.0 d** 使高压回渗显著下降（CleanShield 测试，KCA LeakShield 结果提示同样适用于 AC4），**并同时改善摄入时间**"
  - "**回渗不是终点，是沟通工具**：**Rewet 衡量产品干爽、EWL/STEWIE 衡量皮肤干爽**；原文提出二者**可能成为对外沟通与「对竞品的获胜主张（winning proposition）」** ⇒ 回渗指标具有**消费者可感知与可宣称**的双重属性"
  - "⚠️ **GRIFFIN 的开放风险**：无处理面层降回渗，但 **AFC 曾在 ATACAMA 上见到渗漏上升**；BCC 侧 HUT 未见差异；假设是 **GRIFFIN 的护翼（flaps）能让面层正常工作** ⇒ **渗漏影响正在 HUT 中筛查，尚未结案**"
pages_linked: ["[[Rewet Principles（回渗设计原则与测试方法关联）]]", "[[Rewet Test（回渗测试）]]", "[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]", "[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]", "[[Liner-Surge Embossing（面层-导流层压花）]]", "[[P&G Rewet Patent Deep Dive（宝洁回渗专利深挖）]]", "[[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]]", "[[IPC BCC OI Portfolio（开放创新项目组合）]]"]
---

# Rewet Quarterly Update 2025-08（设计原则落地与五个项目战绩）

## 一句话定位

K. Clemmer（ADT）**2025 年 8 月的回渗季度汇报**。结构是「**设计原则 → 项目落地 → 竞品分析**」三段式：先给出 **Flowback / Desorption 两套原则集**，再用 **五个项目（BUFF BABY / GRIFFIN / LUGH / LOKI / AC4 4U）**的实测数字证明原则有效，最后用 **P&G 专利地图 + 竞品互换实验**定位外部基准。本库价值：它是 [[Rewet Principles（回渗设计原则与测试方法关联）]]（2025-10-22，Draft 3）**在时间上的前一版快照**，且**独有五个项目的量化战绩与互换实验结论**。

> 🔴 **manual_review（2026-09-29）**
> 本页含**竞品实测回渗值（Millie Moon / Colt / Credible / Always Discreet）、竞品专利分析与内部项目代号（GRIFFIN / LOKI / LUGH / BUFF BABY / AC4 4U / MOJAVE / ATACAMA）**。属**竞争性技术情报**：
> 1. **不得对外引用**，尤不得用于对外宣称（原文虽提到回渗可能是「winning proposition」，但**该主张尚未经法务/宣称合规确认**）；
> 2. 本页**不含报价、合同条款、未公开合作方或个人联系方式**——上述项在该资料中未出现（汇报人为内部作者，属来源元信息，予以保留）。

## 摘要

**总纲**：*"Tackling rewet on all fronts to deliver best-in-class"*，方法论是*"Systematically eliminating residual fluid from every component"*——**逐层消灭残液**，覆盖 **GRIFFIN 无处理面层 / LOKI 面层驱动因素 / Ourly 纤维复合 / 芯体 / BUFF BABY 分析 / Liner-Surge 压花 / SAM 去溶胀 / 间隙空间（interstitial spaces）/ 界面 DOE** 九条战线。

**两套机理 + 原则集**（见下表）。**贯穿原则**只有一条：**每条原则都要评估材料与工序的变异与能力**。

## 提炼的数字与结论

### 回渗设计原则（2025-08 版措辞）

| 机理 | 原则（原文） |
|---|---|
| **Flowback 回流** | ① 有**足够容量**锁住液体（There is enough capacity available to fully lock up fluid） |
| | ② **容量对液体可达**（Capacity is accessible to the fluid） |
| | ③ **SAM 在压力下仍持液**（SAM holds fluid, even under pressure） |
| | ④ **SAM 及时锁液**（SAM locks up fluid in a timely manner） |
| | ⑤ **芯体中未锁住的液体与皮肤/吸墨介质隔离**——吸收层提供**物理隔离**并促进**单向流动** |
| **Desorption 解吸** | ① 吸收材料**不截留**液体，而是促其排向芯体 |
| | ② 材料**孔径大**以降低毛细性 |
| | ③ 材料**抗压**，确保使用中孔隙保持开放 |
| | ④ 材料**润湿性最低**以降低毛细性 |
| | ⑤ **孔数最小化**，减少液体可被困住的位置 |
| | ⑥ **孔网连通良好**，界面处无液体滞留 |
| | ⑦ **毛细梯度**把液体从皮肤引向可被锁住的位置 |
| **贯穿** | **材料与工序的变异与能力须在设计阶段一并考虑**（Material and process variability and capability are considered in design） |

> 📌 **与 [[Rewet Principles（回渗设计原则与测试方法关联）]] 的措辞差异（重要）**：本页为 **2025-08 措辞**（"**large pores**"、"**minimally wettable**"、"**number of pores minimized**"）；2025-10 的 Draft 3 已改为**相对表述**（"lower capillarity and wettability **compared to where fluid is locked up**"、"resist compression to ensure pores **stay fully open**"）。**这是从「绝对材料属性」到「相对锁液区属性」的演进，两版本并列保留、不合并。**

### T5 BUFF BABY 目标与现状

| 压力档 | 目标 | 现状 / 驱动 |
|---|---|---|
| **低压回渗（LPR）** | **0.15 g** | **Liner-surge 压花**可降至目标；经验来自 Depend |
| **高压回渗（HPR）** | **0.30 g** | 最大驱动是**优化后的吸收系统**（T4/T5 已压到 **~0.4 g**）；**弹性导流层（如 MOJAVE）+ 低克重面层（如 spunbond）**；最新 T5 学习在多种芯体变更下做到 **<0.3 g** |

| 回渗（g） | Millie Moon | Code G | **Colt** |
|---|---|---|---|
| 低压 | 0.34 | 0.32 | **0.14** |
| 高压 | 1.58 | 0.47 | **0.21** |
| 参照 | HUT 40477 | HUT 40477 | CUT 91836 |

> ⚠️ **原文自陈的开放项**：*"Need to confirm the driving mechanisms in order to consistently deliver target"* —— **<0.3 g 是「多种芯体变更」下的观测值，机理未确认 ⇒ 不能保证稳定复现**。

### 五个项目的量化战绩（按同一套原则）

| 项目 | 变更 | 回渗变化 | 备注 |
|---|---|---|---|
| **GRIFFIN** | **无处理面层** | **0.26 → 0.20 g** | 经验来自 Huggies；渗漏影响正在 HUT 筛查 |
| **LUGH** | 把**柔软方案从处理剂移到纤维** + 调整表面活性剂 | **0.41 → 0.34 g**，**柔软度保持** | 14gsm 面层天然高于对照 12gsm（0.41 vs 0.34 对照水平） |
| **LOKI** | **Credible 面层**（手工改制） | **0.62 → ≤0.32 g** | 正在研究驱动因素及可向美国面层迁移的部分 |
| **AC4 4U** | **Textor 材料组分变更**（更大纤维 1.3 d → 2.0 d） | **高压回渗 3.8 → 1.6 g** | Textor 材料擅长 BM 管理、回渗偏弱；**大纤维同时改善摄入时间** |
| **BUFF BABY** | Liner-surge 压花 + 吸收系统优化 | 见上表（目标 0.15 / 0.30 g） | — |

### 竞品互换实验（★ 本篇最有因果力的实验）

| 组合 | 结论 |
|---|---|
| Depend 芯体 + **Depend** 面层/导流层 | 基准（回渗最高） |
| Depend 芯体 + **Always Discreet（AD）面层/导流层** | **回渗降至 AD 水平** |
| 上述 + **AD 卷曲纤维** | **无额外回渗收益** |

> 📌 **因果结论**：**AD 的低回渗来自其面层/导流层的解吸特性，而非卷曲纤维**；**卷曲纤维的价值在摄入（intake），不在回渗**。这与 [[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]] 中「AD 面层更干 = 更低润湿性」的结论**互相印证**。

### P&G 专利地图（回渗相关）

| 公开号 | 内容 | 归属层 |
|---|---|---|
| US 11,202,723 | 理解毛细性的**测量方法** | 吸收系统 |
| US 2021/0369509 | 面层 **phobic/philic 双面性** → **润湿梯度**驱动液体向芯体 | 吸收系统 |
| US 2022/0133554 | **超细纤维**把液体从面层/皮肤/吸墨介质引走 | 吸收系统 |
| EP 2679209 | **100% 绒毛浆层会漏液** → 应置于 **SAM 层之下**以远离皮肤/吸墨介质 | 芯体 |
| EP 3243565 | 日本触媒（受 P&G 约束）对**回渗相关 SAM 属性**的认知 | 芯体 |

> 📌 **原文判断**：*"P&G patent estate reveals they're also thinking systematically about rewet across the whole absorbent system"* ⇒ **竞争对手同样在系统性处理回渗，而非单点优化**。

### 指标定位与后续

- **Rewet 衡量产品干爽；EWL / STEWIE 衡量皮肤干爽** —— 二者**用途不同，不可互换**。
- **下一步（当时）**：8 月 BUFF BABY 深挖 → 9 月竞品分析 → 9 月界面试验 → 10 月 GRIFFIN HUT 结果 → 10 月 SAM 影响与其他芯体驱动（DML 试产）。
- **再下一步**：**回渗测试方法优化**、**EWL/STEWIE** 方法建设。

## 关键论断（key_claims）

- **回渗 = Flowback + Desorption 两套机理，各有原则集；贯穿原则是评估变异与能力。** —— 支撑页：[[Rewet Principles（回渗设计原则与测试方法关联）]]
- **BUFF BABY 双目标：LPR 0.15 g / HPR 0.30 g；HPR 的 <0.3 g 机理未确认。** —— 支撑页：[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]
- **五项目实测：GRIFFIN 0.26→0.20；LUGH 0.41→0.34；LOKI 0.62→≤0.32；AC4 4U 3.8→1.6 g ⇒ 同一套原则跨品类有效。** —— 支撑页：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]
- **互换实验：AD 面层+导流层足以把 Depend 回渗降到 AD 水平；AD 卷曲纤维无额外回渗收益但利于摄入。** —— 支撑页：[[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]]
- **大纤维（1.3 d → 2.0 d）降高压回渗并改善摄入 ⇒ 一击多因的通用解。** —— 支撑页：[[ADL（导流层）]]
- **Rewet = 产品干爽，EWL/STEWIE = 皮肤干爽；可能成为对外沟通主张（待合规确认）。** —— 支撑页：[[Rewet Test（回渗测试）]]
- ⚠️ **GRIFFIN 开放风险：无处理面层降回渗但 AFC 曾见渗漏上升（ATACAMA），HUT 筛查中未结案。** —— 支撑页：[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]

## 关联页面

- 概念：[[Rewet Test（回渗测试）]]、[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]、[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]、[[Liner-Surge Embossing（面层-导流层压花）]]、[[ADL（导流层）]]
- 来源：[[Rewet Principles（回渗设计原则与测试方法关联）]]（**本页的后继版本，2025-10-22**）、[[P&G Rewet Patent Deep Dive（宝洁回渗专利深挖）]]、[[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]]、[[Depend Ultra-Low Rewet M2M Learning Share（2025-04-22 面层与 ActivTech 芯体）]]
- 项目：[[IPC BCC OI Portfolio（开放创新项目组合）]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Updates and Presentations/2025.08.21 - Josie Quarterly Update.pptx.md`
- 原文链接：（无）
- 作者 / 归属（来源元信息）：K. Clemmer – ADT，Kimberly-Clark，2025-08

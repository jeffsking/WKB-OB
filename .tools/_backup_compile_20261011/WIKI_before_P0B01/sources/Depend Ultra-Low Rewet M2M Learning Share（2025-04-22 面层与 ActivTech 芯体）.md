---
type: source
title: "Depend Ultra-Low Rewet M2M Learning Share（2025-04-22 面层与 ActivTech 芯体）"
source_type: 内部学习分享（M2M 例会纪要 · 超低回渗攻关双工作流）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.04.22 - M2M learning share - Depend ultra low rewet.pptx.md
original_link: ""
date_published: 2025-04-22
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "目标量化：**Depend Fresh Protection 闭式 Cradle 回渗 ≤0.15 g**；方法论是「系统性地从每一层里消灭每一滴水（eliminate every drop of water from every layer）」，而非单点优化"
  - "**面层粘合面积（bond area）对回渗无显著影响**：Oval bond 18% 与 CD Rod bond 10% 差异不显著 ⇒ 否证「更开放的粘合花型 = 更少小口袋滞留残液」的机理假设"
  - "**亲水整理剂（Lertisan）用量越低，回渗越低**（0.65% → 0.3% → 0% 单调下降），且**与吸收时间无明显趋势关系** ⇒ 存在「回渗↓ / 吸收与渗漏风险↑」的**权衡（tradeoff）**，而非单赢"
  - "**HUT 数据与台架数据方向相反**：ATACAMA+（39840, Depend）中 ATACAMA Untreated Liner 为**最差档**（Medium 7.9 B / Large 9.5 B，对照组 BAYMAX 4.9 A / 3.4 A）⇒ **台架上的回渗收益不能外推到使用测试**，无处理面层在 HUT 中付出渗漏/潮湿代价"
  - "**Always Discreet 面层更干的原因 = 更低的润湿性（wettability），不是更大的孔径**：假设 1（孔径更大）被**否证**（两者均为 PP SB，纤维直径与孔径当量，14–20 µm 区间重叠）；假设 2（更不润湿）被**证实**（TTM-00382 50 滴法：AD 初始 3、60 s 后 11 → 22%；Depend 50 s 后 46 → 92%）"
  - "**方法学创新：用「改变液体表面张力」替代「改变面层整理水平」**来建立回渗-吸收权衡曲线 ⇒ 可在**不重新打样**的前提下回答「GRIFFIN HUT 是否应含无处理/半处理面层」"
  - "**ActivTech（AT）Hybrid 芯体在头对头测试中确实抬高回渗**；归因候选为包裹层（12gsm dSB vs 17gsm tissue）、面层压花（printed vs unprinted）、 liner-surge 压花（light vs yes）、以及**更低的总吸收容量**"
  - "**AT Hybrid 的下一步诊断设计包含一个关键对照：做「无 SAM」芯体**（12gsm dSB / 20gsm BCW × Standard fluff × No SAM）⇒ 用于判定**绒毛浆本身是否在持液**，以及**少量 SAM 能否把绒毛浆里的液体解吸出来**"
  - "⚠️ **待验证的因果链**：AT Hybrid 容量低于 SAM/Fluff，而「低容量是 GRIFFIN 上市的不可让步项」；SAM/Fluff 体系中容量对比**未显示影响回渗** ⇒ **容量是否为 AT Hybrid 高回渗的成因，目前是未决问题**"
pages_linked: ["[[Rewet Test（回渗测试）]]", "[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]", "[[亲水整理耐久性]]", "[[Liner-Surge Embossing（面层-导流层压花）]]", "[[Cradle Intake Test（Cradle 摄入测试）]]", "[[IPC BCC OI Portfolio（开放创新项目组合）]]"]
---

# Depend Ultra-Low Rewet M2M Learning Share（2025-04-22 面层与 ActivTech 芯体）

## 一句话定位

K. Clemmer（ADT）2025-04-22 的 M2M（meeting-to-meeting）学习分享，是 **Depend 超低回渗（≤0.15 g，闭式 Cradle）攻关的中期进展**。两个并行工作流：**WS1 面层（liner）**、**WS2 ActivTech 芯体**。本库价值：它给出了**两条被明确否证的假设**（粘合面积、孔径）与**两条被证实的结论**（整理剂用量、润湿性），并记录了**台架回渗 ↔ HUT 使用结果方向相反**这一关键陷阱——对 [[Rewet Test（回渗测试）]] 的**指标外推边界**具有直接约束力。

> 🔴 **manual_review（2026-09-29）**
> 本页含**竞品（Always Discreet、Depend 主线）实测对比数据**与**内部项目代号（GRIFFIN / ATACAMA / ATACAMA+ / MOJAVE / BAYMAX / SIROCCO / BUFF BABY / KCM / LUGH）**及其 HUT 评分。属于**竞争性技术情报**，不得对外引用或写入对外材料；如需外部化，须先脱敏并获项目组书面同意。
> 补充：本页**不含报价、合同条款、未公开合作方或个人联系方式**，上述商务敏感项在该原始资料中未出现。

## 摘要

**目标**：系统性地从每一层消灭每一滴水，使 **Depend Fresh Protection 的闭式 Cradle 回渗 ≤0.15 g**。

**WS1 — 面层**：在 2 月 GRIFFIN GML 试产中检验 3 条假设。基底均为 **Fitesa 12gsm SB**：
- 对照：Oval bond（18%）+ 0.65% Lertisan
- CD Rod bond（10%）+ 0.65% Lertisan —— 假设「更开放的粘合花型 = 更少滞留残液的小口袋」
- CD Rod bond（10%）+ 0.3% Lertisan —— 假设「无处理 = 排斥残液（对吸收/渗漏有对等风险）」
- CD Rod bond（10%）+ 0% Lertisan —— 同上，但风险更高
- （计划外）打孔膜面层 Fitesa 22gsm TS3，因**胶渗透（adhesive burnthrough）未能取到样**

**结果**：**粘合面积无显著影响**（假设 1 否证）；**整理剂用量越低回渗越低**（符合预期）；**整理剂水平与吸收时间无明显趋势**。

**WS1 — 竞品解吸机理**：GR&D 评估 Always Discreet（AD）面层的解吸驱动因素。假设 1（AD 孔径更大 → 更易向导流层排液）**被否证**——两者同为 PP SB 非织造布，纤维直径当量，孔径均在 14–20 µm 区间重叠。假设 2（AD 更不润湿 → 更易排液）**被证实**——TTM-00382 50 滴法：AD 初始 3 滴、60 s 后 11 滴（22%）；Depend 主线 50 s 后 46 滴（92%）。

**WS2 — ActivTech 芯体**：重做带 LSE 的 Depend AT 样品（此前样品可能 LSE 过轻，而 LSE 对回渗是**关键**）。头对头结果：**AT Hybrid 芯体确实抬高回渗**。差异清单：包裹层 12gsm dSB vs 17gsm tissue；面层 12gsm SB 印花 vs 未印花；导流层同为 Shalag SS7CT5H80；面层-导流层压花 Light vs Yes（2024 GRIFFIN HUT 产品）。

## 提炼的数字与结论

### WS1 面层 DOE（Fitesa 12gsm SB 基底）

| 变量 | 水平 | 对回渗的影响（TTM:00672 闭式 Cradle） |
|---|---|---|
| **Bond 花型/面积** | Oval 18% vs CD Rod 10% | **无显著差异**（假设否证） |
| **Lertisan 用量** | 0.65% → 0.3% → 0% | **单调下降：用量越低回渗越低**（符合预期） |
| **Lertisan 用量 vs 吸收时间** | 同上 | **无明显趋势**（闭式 TTM:00672 与开式 TTM:00148 均是） |

### 使用测试（HUT）中的反向信号 ⚠️

| 试验 | Code | Medium | Large | 档位 |
|---|---|---|---|---|
| **ATACAMA+**（39840, Depend） | BAYMAX Control | 4.9 | 3.4 | **A / A** |
| | ATACAMA Zoned Pad | 5.9 | 5.7 | B / A |
| | ATACAMA Base | 6.1 | 6.0 | B / A |
| | **ATACAMA Untreated Liner** | **7.9** | **9.5** | **B / B（最差）** |
| | Always Discreet（竞品参照） | 2.6 | 6.7 | A / AB |
| **MOJAVE**（39634, Diapers） | P：12gsm GNW FPS SB，**半处理** + 80gsm Mojave 导流层 | — | — | **4.8 A（最优）** |
| | Q：同上，**无处理** | — | — | 5.0 AB |
| | T：20gsm Fitesa Gold + 80gsm Mojave | — | — | 5.1 AB |
| | W：12gsm GNW dSB + 80gsm Mojave | — | — | 5.2 AB |
| | U：12gsm Fitesa Gold SB + 80gsm Mojave | — | — | 5.8 AB |
| | LM Control / SND Control | — | — | 6.0 AB / 6.1 AB |

> ⚠️ **本页最重要的判读**：**台架上「无处理 → 回渗更低」在使用测试中反转为「无处理 → 最差档」**（ATACAMA+ Medium 7.9 B / Large 9.5 B，差于对照 4.9 A / 3.4 A）。即**回渗收益以渗漏/潮湿体感为代价**。MOJAVE 中**半处理 P 码最优（4.8 A）**、无处理 Q 码（5.0 AB）次之——**半处理似乎是权衡的较优解，但样本仅单次试验，未做显著性检验。**
>
> 📌 **数值-档位关系说明**：两张表的数值均为**越小越好**（4.9→A，7.9→B），与字母等级一致；表头在图片提取中部分缺失，**指标名未确证**（推测为潮湿感/渗漏类综合评分），故**不做定量外推**。

### WS1 下一步（方法学转换）

- 机理认知：**润湿整理改变的是液体表面张力**，而非材料本身。
- 实验设计转换：**不改整理水平，改为直接改变测试液体的表面张力**，在**未处理面层的现有样品**上建立「回渗 vs 吸收」权衡曲线。
- 目的：**不重新打样**即可回答「GRIFFIN HUT 是否应包含无处理或半处理面层」。HUT 打样时间为 5 月中下旬。
- 遗留疑问：所供样品的整理**可能存在中断（interruptions）**，影响上述对比。

### WS2 ActivTech Hybrid 的归因候选与下一步

| 候选归因 | 当前证据 |
|---|---|
| 包裹层材质（12gsm dSB vs 17gsm tissue） | SIROCCO 测试**未发现 dSB 与 tissue 有差异**；TABCW 包裹层曾在 BUFF BABY 与 KCM（尿片）上有效 ⇒ 此处待验 |
| 面层印花 vs 未印花 | 同时变化，**未解耦** |
| Liner-Surge 压花（Light vs Yes） | 同时变化；压花强度已知影响界面排液（见 [[Liner-Surge Embossing（面层-导流层压花）]]） |
| 层数更多 ⇒ 更多持液位点 | 机理假设「more layers = more places fluid can be trapped」，**需无 SAM 样品做诊断** |
| 绒毛浆自身持液 | 待验；若成立，则「少量 SAM 能否把绒毛浆中的液体解吸出来」是关键问题 |
| **总容量更低** | AT Hybrid 容量低于 SAM/Fluff；**低容量是 GRIFFIN 上市的不可让步项**；SAM/Fluff 体系中容量对比**未显示影响回渗** ⇒ **因果未决** |

**下一步打样矩阵（芯体 3/17 周产出，成品 4 月底–5 月初，台架结果 5 月中下旬）**：

| 包裹层 | 绒毛浆 | SAM |
|---|---|---|
| 12gsm dSB | Standard | Standard |
| 20gsm BCW | Standard | Standard |
| 12gsm dSB | Standard | **None** |
| 20gsm BCW | Standard | **None** |
| 12gsm dSB | **+30% SAM** | Standard |

> 判读：矩阵中**两组「No SAM」是诊断组**（隔离绒毛浆持液），**「+30% SAM」是机理验证组**（检验 SAM 是否解吸绒毛浆持液）。**不含 SAM 的芯体在成品层面无法正常使用，仅作机理诊断用途。**

## 关键论断（key_claims）

- **目标 ≤0.15 g 闭式 Cradle 回渗；路径是逐层清零残液，而非单点优化。** —— 支撑页：[[Rewet Test（回渗测试）]]
- **粘合面积（Oval 18% vs CD Rod 10%）对回渗无显著影响 ⇒ 「开放花型减少小口袋」假设被否证。** —— 支撑页：[[Rewet Test（回渗测试）]]
- **整理剂用量 0.65%→0.3%→0% 回渗单调下降，但与吸收时间无趋势 ⇒ 回渗-吸收权衡存在且未被量化。** —— 支撑页：[[亲水整理耐久性]]
- **HUT 中无处理面层为最差档（7.9 B / 9.5 B）⇒ 台架回渗收益不可外推到使用结果。** —— 支撑页：[[Rewet Test（回渗测试）]]
- **AD 面层更干 = 更低润湿性（TTM-00382：AD 22% vs Depend 92%），而非更大孔径（孔径假设被否证）。** —— 支撑页：[[亲水整理耐久性]]
- **改用「调节液体表面张力」替代「调节整理水平」，可在不重新打样下建立权衡曲线。** —— 支撑页：[[Rewet Test（回渗测试）]]
- **AT Hybrid 头对头确实抬高回渗；归因未解耦（包裹层/印花/压花/容量同时变化）。** —— 支撑页：[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]
- **「无 SAM」与「+30% SAM」两组是机理诊断设计 ⇒ 绒毛浆持液与 SAM 解吸是 AT Hybrid 回渗的核心待验机制。** —— 支撑页：[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]
- ⚠️ **容量是否为 AT Hybrid 高回渗的成因，目前未决**（低容量为不可让步项；SAM/Fluff 中容量不影响回渗）。 —— 支撑页：[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]

## 关联页面

- 概念：[[Rewet Test（回渗测试）]]、[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]、[[亲水整理耐久性]]、[[Liner-Surge Embossing（面层-导流层压花）]]、[[Cradle Intake Test（Cradle 摄入测试）]]
- 来源（同主题前后继）：[[Depend Rewet Update 2025-04-04（LUGH 与 GRIFFIN 回渗进展）]]、[[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]]
- 项目：[[IPC BCC OI Portfolio（开放创新项目组合）]]

> 📌 **术语对齐**：原文写作 **ActivTech**，本库既有概念页写作 **ActiveTech**（见 [[ActiveTech Platform（ActiveTech 在线薄芯体平台）]] 与 `Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）`）。二者指同一在线薄芯体平台，本页**统一按既有页面拼写 ActiveTech 互链**，此处登记为同义异写。

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.04.22 - M2M learning share - Depend ultra low rewet.pptx.md`
- 原文链接：（无）
- 前一版链接（原文内引用）：`M2M 2.25.25 - Depend Ultra Low Rewet.pptx`（**该文件未在本批次中，未见于 RAW/**）

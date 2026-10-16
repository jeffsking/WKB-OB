---
type: entity
title: "Nippon Shokubai（日本触媒）"
category: 供应商
relationship: 候选
updated: 2026-09-29
tags: [SAP, 高吸水树脂, 高CRC, 低GBP, P&G主供]
aliases: ["日本触媒", "Nippon Shokubai Co., Ltd.", "NSKK"]
---

# Nippon Shokubai（日本触媒）

## Basic profile 基本盘

| Item 项目 | Content 内容 |
|---|---|
| 主营 Main business | SAP（高吸水树脂）与丙烯酸产业链；CA / W 系列 SAP 牌号 |
| 产地 / 基地 Base | 日本（Japan） |
| 产能 Capacity | 源内未给出具体产能数字 `[待验证]` |
| 角色 Role in this library | **高 CRC / 低 GBP 阵营的代表供货源**；同时在资料备注中被标注为「P&G 主供」，属对标对象而非直接替代对象 |

## Grades on record 在录牌号参数

> 口径 Caliber：CRC（g/g）｜AUL（g/g）｜GBP（10⁻⁷ cm³·s/g）｜Vortex（s）。均为 SAM Database 与 Decision Base 收录口径，未标注年份者为原表未填。

| Grade 牌号 | CRC | AUL | GBP | Vortex | Note 备注 |
|---|---|---|---|---|---|
| CA W109 | 37 | 14 | 17 | 49 | GBP 在触媒系列中偏高 |
| CA W2001 | 40 | 11 | 1 | 39 | 高容量低渗透 |
| CAW2000 | 39 | 12 | 1 | 39 | 同上 |
| W101 | 34 | 14 | 0 | 50 | GBP 记 0 |
| W1030 | 39 | 12 | 1 | 36 | — |
| W2086 | 37 | 10 | 1 | 36 | — |
| **W3020** | 32 | 14 | **32** | 36 | **系列内 GBP 最高（32）** |
| W843F | 40 | 8 | 0 | 40 | — |

**SAM 供应商全景表中的记录 SCM view**

| Supplier | Grade | CRC | AUL | GBP | Vortex | SAM type 类型 | K-C 侧注记 K-C note |
|---|---|---|---|---|---|---|---|
| Nippon Shokubai | CAW | 40 | 12.5 | 1 | 35 | High Capacity（高容量型） | 漏液/回渗风险↑；**难点：其为 P&G 主供（supply is tied to P&G）** |

## Cooperation & supply history 合作与供货历史

- **2026-07-17**（S5 `SAM Database-CW.xlsx` 截止口径，数据截止 2025-01）：CA/W 系列牌号在系统内仅作为**能力底表**存在，未见 KCC 在录使用标记（`KCC 使用` 列对该供应商全为空）。
- **2026-08-01**（decision base 汇编口径）：在 SAM 供应商全景表中被归入 **High Capacity（高容量型）**，K-C 侧注记为「漏液/回渗风险↑」，并列明商务难点——**其为 P&G 主供**，产能/供应优先绑定竞争对手。

## Pricing & commercial notes 价格与商务要点

> ⚠️ 商务敏感信息只记要点与区间，不落完整价格表（AGENTS.md §2.2）。

- **记录日期 2026-08-01**：源资料的价格敏感性分析中提到「SAP3 换日触 CAW → 成本 +10%」，即**以 Nippon Shokubai CAW 替换现 SAP3 会导致约 +10% 成本**，属上升趋势性结论；原始单价表为报价类信息，不在此展开。

## Selection positioning 选型定位

- **容量阵营 Capacity camp**：多数触媒牌号 CRC ≥37 且 GBP ≤1，属典型「高容量 / 低渗透」象限；按 [[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]，这类料在**低载多次（企标）**工况下表现好，在**高载短间隔**工况下最弱。
- **唯一的例外 The exception**：`W3020`（CRC 32 / AUL 14 / **GBP 32** / Vortex 36）是全系列中唯一进入**平衡—高渗透过渡带**的牌号，可作为触媒阵营里的 Pareto 折中点候选。
- **供应可得性风险 Availability risk**：「P&G 主供」这一注记提示其产能存在**竞争绑定**，不宜作为国产替代路线的主攻对象，宜作**对标基准**。

## 追加：Open Innovation 批（2026-09-29 追加）

> 本节为 **Resources / Open Innovation 批（批次 S4_Resources_Open Innovation_05）** 编译时的追加记录，**不改动上方既有结论**。上方「高容量 / 低渗透」「P&G 主供 → 不宜作国产替代主攻对象」两条判断在本批**进一步被坐实**；本节补充的是触媒在 **P&G 回渗专利体系中的角色**与一个新参数。

### 1. 本批新增：触媒与 P&G 共同持有的"受压凝胶间隙持液"专利

- **EP 3243565《Water Absorbent Agent and Method for Producing Same》**（申请人 Nippon Shokubai）提出此前被忽视的参数：**受压凝胶间隙持液量（gap fluid retention property under pressure）**——0.69 wt% 盐水溶胀后，在 **0.3 psi（2.07 kPa）**载荷下滞留在**凝胶颗粒之间（而非颗粒内部）**的液体量，单位 g/g。见 [[P&G Rewet Patent Deep Dive（宝洁回渗专利深挖）]]。
- **专利自述的发现**：控制该参数落在特定范围内即可**降低纸尿裤回渗**；专利给出的门槛是 **> 9 g/g → 受压回渗 < 3 g**。
- **对本页的意义**：本库此前对触媒的判读只停留在 **CRC / AUL / GBP / Vortex** 四参数（高容量低渗透）。该专利提示——**第四个维度（受压下的颗粒间持液）才是回渗的直接预测量**，而 AUL/GBP 都测不到它。详见 [[Median Absorption Pressure Gradient（中值吸收压梯度）]] 的同族解法与 [[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]。

### 2. 本批新增参数（EP 3243565 实施例区间）

| 参数 | 对比例范围 | 发明例范围 | 备注 |
|---|---|---|---|
| 受压间隙持液 Gap fluid retention (g/g) | 7.2 – 8.9 | **10.0 – 11.1** | 门槛 > 9 g/g |
| 对应受压回渗 Re-wet under pressure (g) | 3.43 – 4.73 | **0.51 – 1.89** | 门槛 < 3 g |
| CRC (g/g) | 26.5 – 29.5 | 26.9 – 27.7 | 两组**几乎相同** |
| AAP (g/g) | 23.7 – 25.1 | 24.4 – 25.2 | 两组**几乎相同** |
| SFC (×10⁻⁷ cm³·s/g) | 45 – 89 | 66 – 80 | 重叠 |
| FSR (g/g/s) | 0.19 – 0.32 | 0.33 – 0.41 | 发明例略高 |
| D50 (µm) / σ | 413 – 463 / 0.42 – 0.49 | 404 – 449 / 0.39 – 0.42 | 发明例粒径分布略窄 |

> ⚠️ **关键观察（2026-09-29）**：对比例与发明例的 **CRC 与 AAP 几乎无差别**（26.5–29.5 vs 26.9–27.7；23.7–25.1 vs 24.4–25.2），却给出**相差近 10 倍的回渗**（4.73 g vs 0.51 g）。这直接支持一条判断——**回渗不由 CRC/AAP 决定，而由"受压下液体待在哪里"决定**。本页上方"高 CRC / 低 GBP → 漏液回渗风险↑"的注记与此不冲突，但**需补充粒度：容量型 SAP 的风险来自颗粒间间隙持液，而非容量本身**。

### 3. 验证记录

> ✅ 验证（2026-09-29，来源 [[P&G Rewet Patent Deep Dive（宝洁回渗专利深挖）]]）：本页既有注记「P&G 主供 → 供应绑定竞争对手」在本批得到**第二条独立证据**——触媒不仅是 P&G 的 SAP 供货方，还是**P&G 低回渗专利网中 SAP 层专利（EP 3243565）的申请人**。原页结论**未被修正**，但其含义从"供应可能被绑定"升级为"**技术与供应双重绑定**"。

- **追加要点**：评估触媒（以及任何 SAP 供应商）时，**除 CRC/AUL/GBP/Vortex 外应补测"受压下颗粒间持液"类指标**；仅靠四参数无法区分回渗表现。
- **追加 `[待验证]`**：本库在录触媒牌号（CA/W 系列）的受压间隙持液实测值；该参数与本库 [[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]] 的对应关系。

## Related concepts 相关概念

- [[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]
- [[SAP性能指标（CRC AUL GBP Vortex）]]
- [[IPC BCC OI Portfolio（开放创新项目组合）]]

## Sources 来源

- [[SAP Selection Decision Base（17-SAP选型与实验数据决策库）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/17-SAP选型与实验数据决策库.docx.md`
- [[P&G Rewet Patent Deep Dive（宝洁回渗专利深挖）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Patent Deep Dive PG Rewet_Richmond Cohen_2025.pptx.md`（2026-09-29 追加：EP 3243565 受压凝胶间隙持液）

## 追加：全球第一大 SAP 供应商的产能与工艺位次（2026-09-29 追加 · 来源：生物基SAP-SAF技术研究报告 2026-04 · C 级二手）

- **产能与份额（2023 口径）**：**60+ 万吨/年，全球份额 ~20%**，为全球最大 SAP 供应商；工艺路线**反相悬浮聚合**（产物颗粒均匀、吸水率高）。
- **中国布局**：**张家港基地 5 万吨/年**（反相悬浮），在 2024 中国产能表中列为高端供应；另有 6.1 表称总部日本大阪。
- **工艺参数参照（B 级）**：反相悬浮通用窗口——油水比 3–5:1、中和度 70–80%、聚合 70–80 °C/2–4 h、引发剂 0.1–0.5%、共沸脱水 80–110 °C、筛分粒度 150–850 µm。
- 来源页 [[生物基SAP-SAF技术研究报告（2026-04 · 生物基 SAP 路线·产业化与成本结构）]]。

> 校验：本节为 2026-09-29 追加，**未修正上方任何结论**。

## Related Sources 关联来源

- [[P&G Rewet Patent Deep Dive（宝洁回渗专利深挖）]]
- [[SAM Database-CW（全球 SAM 牌号性能数据库）]]
- [[SAP Grade Selection for Baby Diaper Core（三份PPT对比·最终推荐）]]
- [[SAP Selection Decision Base（17-SAP选型与实验数据决策库）]]
- [[SDP Global 控制自由基聚合 SAP 工业化公告（三洋化成 No.1814 · 2018-05-21）]]
- [[我先读取这两份资料，再做对比分析。]]
- [[海水降解SAP技术研究报告（三维水凝胶-可溶粒子体系·2026-05-21）]]
- [[生物基SAP-SAF技术研究报告（2026-04 · 生物基 SAP 路线·产业化与成本结构）]]
- [[竞品IP专利竞争分析_PCA_BNC-SAP表面交联_20261010]]
- [[纸尿裤材料必读书单_v1]]
- [[纸尿裤材料必读书单_v3_非传统资源]]

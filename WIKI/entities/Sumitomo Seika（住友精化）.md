---
type: entity
title: "Sumitomo Seika（住友精化）"
category: 供应商
relationship: 竞品对标
updated: 2026-09-29
tags: [SAP, 高吸水树脂, 高CRC, 低GBP, 极限容量]
aliases: ["Sumitomo（住友精化）", "住友精化", "Sumitomo Seika Chemicals"]
---

# Sumitomo Seika（住友精化）

## Basic profile 基本盘

| Item 项目 | Content 内容 |
|---|---|
| 主营 Main business | SAP（高吸水树脂）与精细化学品；HP / SA 系列 SAP 牌号 |
| 产地 / 基地 Base | 日本（Japan） |
| 产能 Capacity | 源内未给出具体产能数字 `[待验证]` |
| 角色 Role in this library | **极端性能参照供应商**：产品线位于「最高自由溶胀 / 最大 1 min 纯水吸收 / 最低 GBP」的角落，用于探索容量上限而非主力量产料 |

## Grades on record 在录牌号参数

> 口径 Caliber：CRC（g/g）｜AUL（g/g）｜GBP（10⁻⁷ cm³·s/g）｜Vortex（s）｜30-50 mesh（30–50 目占比 %）。

| Grade 牌号 | CRC | AUL | GBP | Vortex | 30-50 目 | Note 备注 |
|---|---|---|---|---|---|---|
| HP600 | 38 | 15 | 8 | 27 | — | High Capacity 型；漏液/回渗风险↑，需增加 add-on |
| HP650 | 42 | 14 | 6 | 29 | — | 同上 |
| SA60N Type II | 35 | 10 | 4 | 30 | — | — |
| **SA60S（住友60S）** | 35 | 14 | **2 ★** | 36 | 75 | 见下「9 牌号横评」 |

**9 牌号横评中的位置（S1 §二，2026-07-21 口径）**

| Item 项目 | 住友60S 数值 | Rank in cohort 同组位置 |
|---|---|---|
| 吸水倍率（DI 自由溶胀，g/g） | **63.2** | **最高**（第一） |
| 离心保水率 ≈ CRC（g/g） | 35.4 | 中上位 |
| AUL 0.7 psi（g/g） | 14.2 | 中位 |
| 1 min 吸纯水（g/g） | **270** | **最高**（第一） |
| GBP | **2（最低）** | 最低 |
| 残单 Residual monomer（ppm） | **95（最低）** | 最优 |
| 角色定位 Role label | **极限容量储库 Ultimate-capacity reservoir** | — |

## Cooperation & supply history 合作与供货历史

- **2026-07-21**（S1 9 牌号 PDF 转述口径）：住友60S 作为 **阶段一最优配方（930/住友，5/5 顶层/底层）** 的底层储库料进入打样清单 —— 该组合在企标 @34 min 主 KPI 上取得全场最优 **4.325 g**，并在新国标场景回渗上同样最优 **1.120 g**。
- **状态 Status**：源内未见该公司的商务/供货/来访记录，其在库角色目前是**能力与技术标尺**，而非在谈供应商。

## Pricing & commercial notes 价格与商务要点

> ⚠️ 商务敏感信息只记要点与区间，不落完整价格表（AGENTS.md §2.2）。

- **记录日期 2026-09-29**：本页所依据的资料**未给出住友牌号单价**，故无价格条目；不因缺值而补写。

## Selection positioning 选型定位

- **容量天花板 Capacity ceiling**：住友60S 同时拥有最高 DI 自由溶胀（63.2）与最高 1 min 吸纯水（270），是 §「追求更大储库」时的参照锚。
- **GBP 陷阱 GBP trap**：其 GBP 仅 2，属典型的「高容量/低渗透」象限（见 [[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]）。**单独满铺底层 = 瞬时渗透坍塌**，必须与高 GBP 顶层（如 KC 511 GBP 24）或活化 REL 层配对使用。
- **结构性离群 Structural outlier**：930/住友 组合在原始 DOE 中被标为 `STRUCTURAL OUTLIER`——因 SAP 基材不同，须**排除在 511 系列排序之外**作独立参照。

## Related concepts 相关概念

- [[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]
- [[SAP性能指标（CRC AUL GBP Vortex）]]
- [[SAP错峰膨胀]]
- [[IPC BCC OI Portfolio（开放创新项目组合）]]

## Sources 来源

- [[SAP Selection Decision Base（17-SAP选型与实验数据决策库）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/17-SAP选型与实验数据决策库.docx.md`

## 追加：高端 SAP 定位与产能位次（2026-09-29 追加 · 来源：生物基SAP-SAF技术研究报告 2026-04 · C 级二手）

- **产能与份额（2023 口径）**：**30+ 万吨/年，全球份额 ~10%**；技术与市场标签为**「高端产品」**，与日本触媒同属**反相悬浮聚合**路线。
- **对华供应方式**：报告标注为**「上海贸易」**（即通过贸易方式供货，未列本地生产基地）。
- 来源页 [[生物基SAP-SAF技术研究报告（2026-04 · 生物基 SAP 路线·产业化与成本结构）]]。

> 校验：本节为 2026-09-29 追加，**未修正上方任何结论**。

## Related Sources 关联来源

- [[COCO V6 Trial Round-2 Review（录音纪要 2026-09-16）]]
- [[SAM 511 Trial Dataset and Statistical Audit（打样原始数据与实验设计审计）]]
- [[SAM Database-CW（全球 SAM 牌号性能数据库）]]
- [[SAP GBP Improvement & Surface Crosslinking Process Review（GDP提升工艺探讨）]]
- [[SAP Selection Decision Base（17-SAP选型与实验数据决策库）]]
- [[SAP Selection Strategy and Trial Data Synthesis v3（SAP选型策略与实验数据综合分析）]]
- [[SDP Global 控制自由基聚合 SAP 工业化公告（三洋化成 No.1814 · 2018-05-21）]]
- [[生物基SAP-SAF技术研究报告（2026-04 · 生物基 SAP 路线·产业化与成本结构）]]

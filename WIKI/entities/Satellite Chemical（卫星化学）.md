---
type: entity
title: "Satellite Chemical（卫星化学）"
category: 供应商
relationship: 候选
updated: 2026-09-29
tags: [SAP, 高吸水树脂, 丙烯酸, 国产替代, 成本]
aliases: ["Satellite（卫星化学）", "卫星化学"]
---

# Satellite Chemical（卫星化学）

## Basic profile 基本盘

| Item 项目 | Content 内容 |
|---|---|
| 主营 Main business | SAP（高吸水树脂）与丙烯酸产业链；CR-xxx 系列 SAP 牌号 |
| 产地 / 基地 Base | 中国（国内丙烯酸—SAP 一体化路线，具体基地在该源内未列明 `[待验证]`） |
| 产能 Capacity | 源内未给出具体产能数字 `[待验证]` |
| 角色 Role in this library | **国产低成本 SAP 候选源**；亦是 SAM Database 中 KCC/BCC 在用牌号的供应方之一 |

## Grades on record 在录牌号参数

> 口径 Caliber：CRC（g/g）｜AUL（g/g）｜GBP（10⁻⁷ cm³·s/g）｜Vortex（s）。同一牌号跨记录存在双值者并列给出，不做取舍。

| Grade 牌号 | CRC | AUL | GBP | Vortex | Note 备注 |
|---|---|---|---|---|---|
| CR-630 | 43 | 8 | 2 | 45 / 34 | 两条记录 Two records |
| CR-630AD | 42 | 8 | 2 | 45 | — |
| CR-635 | 42 | 8 | 2 | 48 | — |
| CR-640 | 30 / 35 | 20 / 21 | 7 / 11 | 70 / 119 | 两条记录 |
| CR-650 | 32 | 22 | 21 | 94 | — |
| CR-658 | 37 | 15 | 2 | 71 | — |
| CR-730 | 35 / 36 | 8 / 8 | 13 / 8 | 26 / 31 | RMS 100000058013 |
| **CR-710** | 32 | **31（全表最高 AUL）** | 12 | 21 | 2024 记录 |
| CR-740 | 31 | 20 / 19 | 18 / 28 | 35 / 45 | 两条记录；**SAP1 备选** |
| CR-740 improved | 32 | 20 | 24 | 35 | CaiShan 改良版 |

**KCC 口径实测（K-C result / Supplier）**

| Grade | CRC | AUL | GBP | Vortex | Shelf life 货架期 | KCC 使用 Usage |
|---|---|---|---|---|---|---|
| 710 | 32 | 31 | 12 | 21 | 24 月 | — |
| 680 | 36 | 23 | 10 | 20 | 24 月 | — |
| **740** | 31 | 20 | 18 | 35 | 24 月 | **BCC**（K-C 实测值 K-C result） |
| 730 | 35 | 31 | 50 | 24 | 24 月 | — |

## Cooperation & supply history 合作与供货历史

- **2026-07-17**（S5 `SAM Database-CW.xlsx` 截止口径）：`CR-740` 在 KCC-YJ 表中标注为 K-C 实测结果并在 **BCC** 产品上在录；同时 `CR-730` 进入 SAM 实验室级记录（GBP 50，全表最高之一）。
- **2026-08-01**（本资料 `17-SAP选型与实验数据决策库.docx` 汇编口径）：在 SAM 供应商全景表中，`CR-740` 被标为 **Balanced（平衡型）** 且注记「漏液风险↑」（leakage risk elevated）；同一表的优势/机会点记为**成本优势 ↔ 品质、OTIF 不稳、创新不足**。

## Pricing & commercial notes 价格与商务要点

> ⚠️ 商务敏感信息只记要点与区间，不落完整价格表（AGENTS.md §2.2）。每条标注记录日期。

- **记录日期 2026-08-01**：本实体页所依据的资料含 SAP 牌号单价表，属报价类信息，依 AGENTS.md §5 **不在本页展开**；仅保留定性结论——"Satellite 属国产低成本阵营，成本是其相对跨国厂商的核心优势，代价是品质/OTIF 稳定性与创新响应"。具体数值留存于源摘要页 [[SAP Selection Decision Base（17-SAP选型与实验数据决策库）]] 标记的 manual_review 区段对应的原文中。

## Selection positioning 选型定位

- **高容量型候选**：CR-630 / CR-635（CRC 42–43）与 228x/N14 同属 ≥42 梯队，但 GBP 仅 2，属**低 GBP 高风险区** —— 单独满铺底层会导致瞬时渗透坍塌（见 [[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]] 的 R3 风险）。
- **备选架构 Backup architecture**：文档给出「混合层用 Satellite 710（GBP 50 口径记录）直接补通道」的方案，用于 **REL 层活化不稳 / 无 REL** 场景的兜底设计。

## Related concepts 相关概念

- [[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]
- [[SAP性能指标（CRC AUL GBP Vortex）]]
- [[SAP错峰膨胀]]
- [[IPC BCC OI Portfolio（开放创新项目组合）]]

## Sources 来源

- [[SAP Selection Decision Base（17-SAP选型与实验数据决策库）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/17-SAP选型与实验数据决策库.docx.md`

## 追加：SAP 产能位次与「快速崛起」标签（2026-09-29 追加 · 来源：生物基SAP-SAF技术研究报告 2026-04 · C 级二手）

- **产能与份额（2023 全球口径）**：**15 万吨/年，全球份额 ~5%**，标签为**「快速崛起」**。
- **中国基地（2024 口径）**：**浙江嘉兴，15 万吨/年，水溶液聚合，自主研发，中端**。
- **与 OI 组合的关系**：[[IPC BCC OI Portfolio（开放创新项目组合）]] 中卫星石化被列为可降解/生物基方向的**后手供应商**之一；本条给出其**水溶液聚合 + 中端**的定位——即其强项在规模与成本，不在高端牌号。
- 来源页 [[生物基SAP-SAF技术研究报告（2026-04 · 生物基 SAP 路线·产业化与成本结构）]]。

> 校验：本节为 2026-09-29 追加，**未修正上方任何结论**。

## Related Sources 关联来源

- [[COCO V6 Trial Round-2 Review（录音纪要 2026-09-16）]]
- [[Nuoer High-GBP SAP Visit Plan & Roadmap（诺尔高GBP SAP拜访预案）]]
- [[SAM Database-CW（全球 SAM 牌号性能数据库）]]
- [[SAP Grade Selection - Three-PPT Comparison（SAP 选型三份 PPT 对比 · 中文版）]]
- [[SAP Grade Selection for Baby Diaper Core（三份PPT对比·最终推荐）]]
- [[SAP Selection Decision Base（17-SAP选型与实验数据决策库）]]
- [[SAP（高吸水性树脂）技术总结报告]]
- [[生物基SAP-SAF技术研究报告（2026-04 · 生物基 SAP 路线·产业化与成本结构）]]
- [[纸尿裤材料必读书单_v3_非传统资源]]
- [[纸尿裤结构与技术全景_内容大纲_20260428232500]]

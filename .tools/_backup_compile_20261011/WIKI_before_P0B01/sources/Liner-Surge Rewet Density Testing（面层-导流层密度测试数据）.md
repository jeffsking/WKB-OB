---
type: source
title: "Liner-Surge Rewet Density Testing（面层-导流层密度测试数据）"
source_type: 报价单
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/Surge-Liner Interface/Test Results/Liner-Surge Rewet - Density Testing.xlsx.md
original_link: ""
date_published: 2026-09
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Dataset of 22 laminate codes measuring six-point thickness, average thickness, adhesive add-on, and derived density for a fixed 12 gsm liner over an 80 gsm surge（中文：22 个层压代码的厚度/施胶量/密度数据集，材料固定为 12 gsm 面层 + 80 gsm 导流层）"
  - "Adhesive add-on is tested at three levels: 1.7, 2.8 and 3.9 gsm（中文：施胶量设 1.7 / 2.8 / 3.9 gsm 三档）"
  - "Average thickness spans 1.2234-1.4850 mm and derived density spans 0.0638-0.0784 g/cc across codes（中文：平均厚度 1.2234–1.4850 mm，密度 0.0638–0.0784 g/cc）"
  - "The lowest density code (16) is not at the lowest add-on, indicating thickness rather than add-on dominates the density outcome（中文：最低密度码（16）并非最低施胶量码，提示厚度而非施胶量主导密度结果）"
  - "Codes carry B-variants (6B, 11B, 15B, 17B) indicating repeat or variant runs within the same code family（中文：含 6B/11B/15B/17B 重复或变体样）"
pages_linked: ["[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]", "[[Liner-Surge Embossing（面层-导流层压花）]]", "[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]", "[[Rewet Measurement Variability（回渗测试变异性）]]"]
---

# Liner-Surge Rewet Density Testing（面层-导流层密度测试数据）

## 一句话定位 One-line Positioning

本批**面层-导流层（liner-surge）层压件的厚度与密度实测数据表**：在材料固定（12 gsm 面层 + 80 gsm 导流层）的前提下，按三档施胶量测 22 个代码的六点厚度并推算密度。是本库回答「界面施胶量如何改变层压密度（进而可能影响回渗）」的原始数据集。

## 摘要 Summary

数据表结构：每个代码给出 6 个厚度测点（Thickness 1–6，mm）、平均厚度（Average Thickness, mm）、**施胶量（Adhesive Add-On, gsm）**、由平均厚度换算的密度（Density，g/m³ 与 g/cc）。表末固定材料条件：**Liner 12 gsm、Surge 80 gsm**。

代码覆盖 **1–18，并含 4 个 B 变体（6B、11B、15B、17B）**，共 22 行。**施胶量分三档**：**1.7 gsm**（代码 1、15、15B）、**2.8 gsm**（4、5、16、17、17B、18）、**3.9 gsm**（2、3、6、6B、7、8、9、10、11、11B、12、13、14）。

厚度与密度结果：**平均厚度区间 1.2234 mm（代码 14）～ 1.4850 mm（代码 16）**；**密度区间 0.0638 g/cc（代码 16）～ 0.0784 g/cc（代码 14）**。单代码内六点厚度本身也有可观波动（例如代码 6：1.273–1.406 mm；代码 6B：1.25–1.497 mm），说明**厚度测量自身存在点间离散**。

一处值得注意的观察：**最低密度（代码 16，0.0638 g/cc）并不出现在最低施胶量档**，代码 16 的施胶量为 2.8 gsm、却是全表最厚（1.4850 mm）；而最低施胶量档（1.7 gsm）的代码 1 / 15 / 15B 密度为 0.0683 / 0.0686 / 0.0752 g/cc。这提示**厚度差异对密度的贡献大于施胶量差异**（同向提示，非统计结论）。

> ⚠️ **数据边界（2026-09-29）**：本表**不含回渗（rewet）列**，因此**不能直接得出"密度→回渗"的因果**；该关联需与同目录的回渗结果表（如 [[HSBL Attachment Strength Results（HSBL 附着强度结果 · 2025-11-18）]] 一族）联合判读。本页只登记厚度/施胶/密度事实。

## 提炼的数字与结论 Key Numbers and Conclusions

| 项目 Item | 数值 / 结论 Value / Conclusion | 备注 Note |
|---|---|---|
| 材料条件 | Liner **12 gsm** + Surge **80 gsm** | 全表固定 |
| 代码数 | 22（代码 1–18 + 6B/11B/15B/17B） | 含 B 变体 |
| 施胶量档位 | **1.7 / 2.8 / 3.9 gsm** | 三档 |
| 1.7 gsm 代码 | 1、15、15B | 密度 0.0683 / 0.0686 / 0.0752 g/cc |
| 2.8 gsm 代码 | 4、5、16、17、17B、18 | 密度 0.0720 / 0.0757 / **0.0638** / 0.0754 / 0.0766 / 0.0767 g/cc |
| 3.9 gsm 代码 | 2、3、6、6B、7、8、9、10、11、11B、12、13、14 | 密度 0.0654–0.0784 g/cc |
| 平均厚度区间 | **1.2234 – 1.4850 mm** | 最薄代码 14；最厚代码 16 |
| 密度区间 | **0.0638 – 0.0784 g/cc**（63,838 – 78,388 g/m³） | 最低代码 16；最高代码 14 |
| 单点厚度离散示例 | 代码 6：1.273–1.406 mm；代码 6B：1.25–1.497 mm | 六点法内部亦有波动 |
| 关键观察 | **最低密度码不在最低施胶量档** → 厚度对密度的贡献大于施胶量 | 同向提示，`[待验证]` |
| 数据边界 | **本表无回渗列** | 不得据此推断密度→回渗因果 |

## 关键论断（key_claims）

- **界面施胶量在本数据集中不是密度的主导变量，厚度才是** —— 支撑页：[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]
- **层压密度是本批可直接量化、可复现的界面状态指标** —— 支撑页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- **厚度测量本身存在点间离散，均值比较须配合离散度** —— 支撑页：[[Rewet Measurement Variability（回渗测试变异性）]]

## 关联页面

- 概念：[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]、[[Liner-Surge Embossing（面层-导流层压花）]]、[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]、[[Rewet Measurement Variability（回渗测试变异性）]]、[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]
- 实体：（本页未落供应商）
- 对比：（本页为单条件数据集，不构成对比页）

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/Surge-Liner Interface/Test Results/Liner-Surge Rewet - Density Testing.xlsx.md`
- 原文链接：（无；内部测试数据）
- 同族文档：`.../Test Results/HSBL Peel Test Results.xlsx.md`（已编译）、[[HSBL Attachment Strength Results（HSBL 附着强度结果 · 2025-11-18）]]

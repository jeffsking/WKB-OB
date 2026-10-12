---
type: source
title: "HSBL Peel Test Results（面层-导流层剥离强度实测）"
source_type: 试产测试数据表（内部 Excel）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/Surge-Liner Interface/Test Results/HSBL Peel Test Results.xlsx.md
original_link: ""
date_published: 2025-10-31
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "文件性质 = **HSBL 试产（试验编号 53267）的剥离强度实测结果**，方法编号 **STM-00438**，试样宽度 **76 mm**，读数 **Average Load 与 Peak Load（gf）**，传感器 100 N（编号 745548 / 715068），试验人代号 VR；含 Overview（每码 3–10 次重复 + 均值与标准差）与 Raw Data（逐次读数）两个工作表"
  - "**剥离强度跨度超过 30 倍**：从最低 **15.4 gf**（码 15：RT-8723 / 1.7 gsm / Summit / 无压合）到最高 **537.1 gf**（码 7：Henkel 5402 / 3.9 gsm / Minibead / PICASSO 压合），峰值载荷最高 **750.3 gf**——说明**这一界面的结合强度完全由工艺组合决定，基材本身不是瓶颈**"
  - "**压合（PICASSO + Pressure）是最强单一杠杆**：同为 RT-8723 / Summit / 3.9 gsm，**无压合 26.6 gf（码 12）与 56.1 gf（码 13）** vs **压合 124.8 gf（码 14）**；同为 RT-8723 / Signature / 2.8 gsm，**无压合 25.3 gf（码 18）** vs **压合 85.6 gf（码 17）**——**约 2–5 倍提升**"
  - "**喷嘴类型的影响大于添加量**：同在 Henkel 5402 / 3.9 gsm / 压合下，**Minibead 537.1 gf ≫ Signature 293.4 gf ≫ CF Swirl 159.3 gf**；同在 RT-8723 / 3.9 gsm / 压合下，**Minibead 375.9 gf ≫ Summit 124.8 gf**"
  - "**添加量效应在同一喷嘴内单调**：RT-8723 / Summit / 压合下，**1.7 gsm 24.6 gf（15B）→ 2.8 gsm 34.7 gf（16）→ 3.9 gsm 124.8 gf（14）**——支持试产假设②「添加量越高连接性越好」"
  - "**胶种差异显著**：同为 Minibead / 3.9 gsm / 压合，**Henkel 5402（DM5402U）537.1 gf vs Rextac RT-8723 375.9 gf**；Henkel 侧的读数整体高于同配置 RT-8723"
  - "**面层材质改变结果**：码 17（12 gsm SB 面层）**85.6 gf** vs 码 17B（**China Liner**）**24.9 gf**，同工艺下面层换料使剥离强度降到约 1/3.4——**界面结合是"两个表面"的事，不能只评价胶**"
  - "**反向基材码（6B / 11B）离散度爆炸**：6B 标准差 **96.8 gf**、11B **133.8 gf**（正向码 6 为 107.3、11 仅 14.1），且重复次数增至 8–10 次——**把施胶侧/剥离侧互换后失效模式改变，数据不再稳定**"
  - "**失效模式提示（原文注记）**："**高亮的码在导流层上出现了明显撕破（noticeable rips in the surge）**"——即**结合强度超过导流层自身强度后，剥离不再是界面失效而是基材撕裂**；此时"剥离力高"已不代表界面质量更好，而是进入了**过强区**"
  - "**两轮测试**：Raw Data 表注记"高亮的码来自第二轮测试"，即部分码因首轮离散过大而复测"
pages_linked: ["[[Peel Test STM-00438（剥离强度测试）]]", "[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]", "[[HSBL Rewet Trial Plan & Adhesive Calcs（面层-导流层施胶回渗试产计划）]]", "[[汉高]]", "[[Rextac（APAO 热熔胶）]]"]
---

# HSBL Peel Test Results（面层-导流层剥离强度实测）

## 一句话定位 One-line positioning

本库**"面层—导流层界面结合强度"的唯一一套量化实测**：它把 [[HSBL Rewet Trial Plan & Adhesive Calcs（面层-导流层施胶回渗试产计划）]] 里那四条假设中的「连接性」一条**直接测成了数字**，并顺带暴露了两件计划书里没想到的事——**换面层材质能把结合强度砍到 1/3**，以及**结合太强会把导流层撕破**（失效模式转移）。它与回渗的关系是**间接的**：剥离强度只证明"连上了"，能否降低回渗还要看毛细与 MicroCT。

## 摘要 Summary

**Overview 表**给出 23 个码（1–18 含 6B / 11B / 15B / 17B）的逐次读数、均值（Avg Average Load、Avg Peak Load）与标准差；**Raw Data 表**按 STM-00438 的格式逐条记录试样宽度、载荷、试验人、传感器编号与框架号。每码重复 3 次；**6 / 6B / 11 / 11B / 16 等离散大的码重复至 4–10 次**。

结合试产计划的码表，可把每个码还原为「胶种 × 添加量 × 喷嘴 × 是否压合」四要素，从而把剥离强度直接映射到工艺变量上（见下表）。原文的两条注记是解读的关键：**"高亮的码在导流层上出现明显撕破"**与**"高亮的码来自第二轮测试"**。

## 提炼的数字与结论 Key figures & conclusions

### A. 逐码剥离强度（按 Avg Average Load 排序，gf）

| 排名 | 码 Code | 胶种 Adhesive | 添加量 Add-on (gsm) | 喷嘴 Nozzle | 压合 Bonding | Avg Average Load (gf) | Avg Peak Load (gf) | STD | 重复数 n |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **7** | Henkel 5402 | 3.9 | Minibead | PICASSO | **537.1** | 750.3 | 84.4 | 4 |
| 2 | **11** | Rextac RT-8723 | 3.9 | Minibead | PICASSO | **375.9** | 546.4 | 14.1 | 3 |
| 3 | **6** | Henkel 5402 | 3.9 | Minibead | None | **355.9** | 526.3 | 107.3 | 8 |
| 4 | **3** | Henkel 5402 | 3.9 | Signature | PICASSO | **293.4** | 428.6 | 56.4 | 4 |
| 5 | **11B** | Rextac RT-8723 | 3.9 | Minibead（反向基材） | None | 251.2 | 388.9 | **133.8** | 10 |
| 6 | **6B** | Henkel 5402 | 3.9 | Minibead（反向基材） | None | 206.6 | 362.4 | **96.8** | 9 |
| 7 | **8** | Henkel 5402 | 3.9 | CF Swirl | PICASSO | 159.3 | 261.6 | 36.2 | 3 |
| 8 | **9** | Henkel 5402 | 3.9 | CF Swirl | None | 143.4 | 241.5 | 52.5 | 4 |
| 9 | **4** | Henkel 5402 | 2.8 | Signature | PICASSO | 130.1 | 204.8 | 21.3 | 3 |
| 10 | **14** | Rextac RT-8723 | 3.9 | Summit | PICASSO | 124.8 | 190.6 | 16.8 | 3 |
| 11 | **2** | Henkel 5402 | 3.9 | Signature | None | 87.4 | 136.9 | 5.4 | 3 |
| 12 | **17** | Rextac RT-8723 | 2.8 | Signature | PICASSO | **85.6** | 140.4 | 6.4 | 3 |
| 13 | **5** | Henkel 5402 | 2.8 | Summit | None | 85.4 | 131.7 | 2.9 | 3 |
| 14 | **10** | Rextac RT-8723 | 3.9 | CF Swirl | None | 80.4 | 147.4 | 3.5 | 3 |
| 15 | **13** | Rextac RT-8723 | 3.9 | Summit | None | 56.1 | 100.7 | 5.2 | 3 |
| 16 | **1** | Henkel 5402 | 1.7 | Signature | None | 43.2 | 84.7 | 0.6 | 3 |
| 17 | **16** | Rextac RT-8723 | 2.8 | Summit | PICASSO | 34.7 | 74.4 | 27.6 | 5 |
| 18 | **15B** | Rextac RT-8723 | 1.7 | Summit | PICASSO | 24.6 | 55.1 | 4.4 | 3 |
| 19 | **17B** | Rextac RT-8723 | 2.8 | Signature（**China Liner**） | PICASSO | **24.9** | 51.7 | 3.9 | 3 |
| 20 | **18** | Rextac RT-8723 | 2.8 | Signature | None | 25.3 | 47.8 | 2.8 | 3 |
| 21 | **12** | Rextac RT-8723 | 3.9 | Summit | None | 26.6 | 53.1 | 2.6 | 3 |
| 22 | **15** | Rextac RT-8723 | 1.7 | Summit | None | **15.4** | 33.7 | 2.9 | 3 |

> 排序按 Avg Average Load（gf）。码与工艺的对应关系来自 [[HSBL Rewet Trial Plan & Adhesive Calcs（面层-导流层施胶回渗试产计划）]] 的 Mini Code List；**6B / 11B 为把主/副基材互换的反向码**，11B 与 6B 在 Mini Code List 中记为 None（无压合）。

### B. 变量效应（成对对照）

| 对照 Comparison | 条件差异 | 剥离强度变化 | 结论 |
|---|---|---|---|
| 压合开/关（RT-8723 / Summit / 3.9） | 码 12、13（无）vs 码 14（有） | 26.6 / 56.1 → **124.8 gf** | **压合约 2–5 倍提升** |
| 压合开/关（RT-8723 / Signature / 2.8） | 码 18（无）vs 码 17（有） | 25.3 → **85.6 gf**（约 3.4×） | 同上 |
| 喷嘴（Henkel / 3.9 / 压合） | Minibead 537.1 vs Signature 293.4 vs CF Swirl 159.3 | **相差约 3.4 倍** | **喷嘴效应 > 添加量效应** |
| 喷嘴（RT-8723 / 3.9 / 压合） | Minibead 375.9 vs Summit 124.8 | 约 3 倍 | 同上 |
| 添加量（RT-8723 / Summit / 压合） | 1.7 → 2.8 → 3.9 gsm | 24.6 → 34.7 → **124.8 gf** | **单调上升**，支持假设② |
| 添加量（Henkel / Signature / 压合） | 2.8 → 3.9 gsm | 130.1 → **293.4 gf** | 同上 |
| 胶种（Minibead / 3.9 / 压合） | Henkel 5402 vs RT-8723 | **537.1 vs 375.9 gf** | **Henkel 侧更高** |
| 面层材质（RT-8723 / Signature / 2.8 / 压合） | 12 gsm SB（码 17）vs **China Liner**（码 17B） | **85.6 → 24.9 gf**（降到约 1/3.4） | **界面是两个表面的事** |
| 反向基材（Minibead / 3.9） | 码 6 vs 6B；码 11 vs 11B | 355.9 vs 206.6（STD 96.8）；375.9 vs 251.2（**STD 133.8**） | **离散度爆炸**，失效模式改变 |

### C. 两条原文注记与其含义

| 注记 Note | 含义 Implication |
|---|---|
| "Highlighted codes resulted in **noticeable rips in the surge**" | **结合强度超过导流层自身强度后，剥离从"界面分离"变成"基材撕裂"**。进入这一区后，**剥离力高不再代表界面质量更好**，而是进入**过强区**——与试产假设①「胶多也会堵住排液通道」共同构成"结合并非越强越好"的两条独立证据 |
| "Highlighted codes are from **round 2 of testing**" | 部分码因首轮离散过大而复测（6 / 6B / 11 / 11B / 16 的重复数达 4–10 次）——**离散本身是结果的一部分**，标准差不该被平均掉 |

> 🔴 **manual_review（2026-09-29）**：本资料为 **K-C 内部试产实测数据**（试验编号 53267、方法编号 STM-00438、码号体系、传感器与试验人代号、供应商胶种与工艺组合的对应）。属内部研发资产，**本页只登记变量效应与方向性结论，不落逐次原始读数表**；原文留存 `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/Surge-Liner Interface/Test Results/HSBL Peel Test Results.xlsx.md`。**对外引用或向供应商披露前须经 R&E 与采购确认。**
> ⚠️ **抽取噪声与缺失信息 Parse & format note**：① **高亮为 Excel 格式信息，文本抽取无法恢复**——因此"具体哪几个码出现导流层撕破"无法从本文件确知，本页只保留注记本身，并按载荷量级提示**最可能进入过强区的是码 7 / 11 / 6（均值 ≥356 gf）**，此为**推断而非原文**；② 码 1 的 Peak Load 均值（84.7 gf）高于其三次读数的算术均值（78.0 gf），疑为源表公式口径差异，**本页照录不作修正**；③ 码 12 与码 13 在码表中工艺描述相同但读数差异明显（26.6 vs 56.1 gf），疑为重复样或设定微调，**已照录并标注**。
> ⚠️ **日期说明 Date note**：文件无独立日期；依其 belonging to 2025-10 试产（试验编号 53267，日程 10/13–10/17）推定为 **2025-10-31**，属推定值。

## 与本库其它页面的关系 Relations

- 派生概念：[[Peel Test STM-00438（剥离强度测试）]]
- 已追加结果：[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]（本页数据已作为该页的实测证据追加）
- 上游计划：[[HSBL Rewet Trial Plan & Adhesive Calcs（面层-导流层施胶回渗试产计划）]]（码号还原依据）
- 供应商：[[汉高]]（Henkel 5402 / DM5402U）、[[Rextac（APAO 热熔胶）]]（RT-8723）
- 判读边界：[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]——**本页只测"连上没有"，不测"回渗降没降"**；二者不可互相替代

## 原文摘录 Original excerpts

- "Note: Highlighted codes resulted in noticable rips in the surge"（Overview 表右栏注记）
- "Highlighted codes are from round 2 of testing"（Raw Data 表注记）
- STM#：**STM-00438**；Specimen Width：**76 mm**；Average Load / Peak Load 单位 **gf**；Load Cell：**100 N 745548 / 100 N 715068**；Tester Initials：**VR**（Raw Data 表头）

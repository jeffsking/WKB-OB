---
type: concept
title: "Liquid Modes（TL-1607 液体四态）"
domain: [卫材研发, 测试方法]
status: seed
updated: 2026-09-29
tags: [液体四态, TL-1607, 摄入定义, 持留, 锁定, 自由液]
aliases: ["Liquid Modes", "液体模式", "TL-1607"]
---

# Liquid Modes（TL-1607 液体四态）

> 一句话定义：K-C 用来描述**液体在吸收结构里处于什么"状态"**的四档分类——**Mode 4 自由液 → Mode 3 松散持留 → Mode 2 紧密持留 → Mode 1 锁定液**；它的用处是把"摄入""分布""回渗""渗漏"这些模糊词换成**状态转移**，从而让每个性能指标对应到一段明确的物理过程。

## 机理 / 结构拆解

1. **四档对应四种被束缚的强度**：Mode 4 是可以自由流动的液体（仍在表面或未进入结构）；Mode 3 是被结构松散抓住、仍可在压力下移动的液体；Mode 2 是被毛细力紧密持留的液体；Mode 1 是被 SAP 化学锁定、实际上不可被压力挤出的液体。**压力能把 Mode 3 挤出来，但挤不动 Mode 2 / Mode 1**——这正是回渗的物理来源。
2. **"摄入"被严格定义为 Mode 4 → Mode 3**：即液体**进入复合结构**的过程。驱动力有三种——**高动量（冲击）强行灌入、毛细力吸入、重力**。这一定义把摄入与"吸收（absorption）"区分开：摄入是跨界面的转移，吸收是结构内部的持留。
3. **回渗是逆过程**：把 Mode 3（以及部分被压出的 Mode 2）**反向推回 Mode 4 并送回贴肤面层**。因此回渗指标度量的其实是"Mode 3 有多少、以及结构在压力下还能不能把它留住"。
4. **为什么它对方法学至关重要**：若两套测试方法定义的"摄入终点"不同（例如一套以液体消失为终点、另一套以固定时间后称重为终点），它们测的其实是**不同档位的边界**。这是"同一片产品在不同方法下给出不同摄入/回渗值"的根本原因之一。
5. **与其他概念的接口**：[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]] 说的是**限制发生在哪一段**（渗透段 vs 容量段）；液体四态说的是**液体处于哪一档**。二者结合才能定位失效——例如"GBP 受限但回渗仍高"意味着液体大量停留在 Mode 3 而没能推进到 Mode 2/1。

## 关键参数表

| 参数 Parameter | 内容 Content | 出处 Source |
|---|---|---|
| Mode 4 自由液 Free liquid | 可自由流动；位于表面或未进入结构 | [[Intake Systems Tech Pipeline - Archive（摄入系统技术管线·汇编存档）]]（Definition of Intake in Menses；TL-1607） |
| Mode 3 松散持留 Loosely held | 被结构松散抓住，**压力下可移动**——回渗的来源 | 同上 |
| Mode 2 紧密持留 Tightly held | 被毛细力紧密持留，压力不易挤出 | 同上 |
| Mode 1 锁定液 Locked-up | 被吸收材料化学锁定，实际上不可挤出 | 同上 |
| 摄入定义 | **Mode 4 → Mode 3**，即液体进入复合结构 | 同上 |
| 摄入的三种驱动力 | 高动量液体灌入 / 毛细力与重力吸入 / 外力压入 | 同上 |
| 报告出处 | Report No: R168567；Sector: Corporate R&E/Other；Document Source: **SR-00830**；年份 **2018** | 同上 |

> ⚠️ **禁止无来源参数**：本页四档定义与摄入定义来自同一份内部汇编 PPT 引用的 TL-1607 / R168567（SR-00830，2018）；**各档位的定量判据（如以何种压力、何种时间定义 Mode 3 与 Mode 2 的边界）在本库中缺失**，标 `[待验证]`。

## 相邻概念

- 失效定位：[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]（限制发生在哪一段）
- 指标侧：[[Rewet Test（回渗测试）]]（Mode 3 的反向泄漏）、[[Rewet Method Comparison（回渗测试方法横向对比）]]（不同方法对档位边界的定义差异）
- 机理侧：[[毛细梯度设计]]（把液体从 Mode 3 推进到 Mode 2/1 的结构手段）、[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]（测量"多大压力会开始吐液"，即 Mode 3 的边界）
- 摄入侧：[[Bladder Box Intake Test（膀胱箱压载摄入测试）]]（加压下测 Mode 4 → Mode 3 的转移）

## 经验教训

> ✅ 验证（2026-09-29，来源 [[Intake Systems Tech Pipeline - Archive（摄入系统技术管线·汇编存档）]]）：本页为新概念页。首条来源的价值在于**给出了"摄入"的可操作定义**（Mode 4 → Mode 3，驱动力三种），使本库此前分散的摄入/回渗议题有了一个共同的状态坐标。

- **教训**：**指标必须先定义状态边界再谈数值**。若一个"回渗 g"没有说明它挤出的是 Mode 3 还是 Mode 2，跨方法、跨产品的比较就没有意义。
- **待补 `[待验证]`**：各档位的定量判据与测试方法；Mode 3 → Mode 2 的转移速率如何测量；液体四态与 GBP / CRC 受限机制的对应关系。

## 来源

- [[Intake Systems Tech Pipeline - Archive（摄入系统技术管线·汇编存档）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Intake/Intake Systems Tech Pipeline - Archive.pptx.md`

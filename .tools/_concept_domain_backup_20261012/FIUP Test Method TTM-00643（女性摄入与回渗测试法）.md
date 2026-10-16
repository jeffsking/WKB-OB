---
type: concept
title: "FIUP Test Method TTM-00643（女性摄入与回渗测试法）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-30
tags: [FIUP, TTM-00643, 摄入, 回渗, 测试方法, 载荷口径]
---

# FIUP Test Method TTM-00643（女性摄入与回渗测试法）

> 一句话定义 One-line definition：**FIUP**（Female Insult Under Pressure，女性压力加液法，标准号 **TTM-00643**）是 K-C 用于成人女性失禁/护垫类产品的**摄入 + 回渗**组合测试法：在规定位置、规定载荷与流速下分 3 次加液，再以**点压力**压吸墨纸读取回渗量。

## 机理 / 结构拆解 Mechanism and Structure

1. **方法族谱**：FIFE flowback（TTM-0001 / STM-2417，1999 起，真空箱施加 0.5 psi）→ Ad Claim / 膀胱箱法（TOMLIN，2014-10）→ FIUP 前身（4 点加液、0.25 psi 加液、0.7 psi 回流）→ **STM-00497 起草、TTM-00643 v0 发布（2015-03）** → **v4（2020-09，回渗压力 0.7 → 0.5 psi）**。
2. **加液位置**：距产品前端 **5/12 或 7/12** 产品长度。依据女性解剖偏前（人体测量研究 AF32161-00，2008-06）与消费者前后翻转习惯——**位置是解剖学推导，不是便利选择**。
3. **载荷口径**：按产品码分档 **ultrathin 12 / moderate 30 / maximum 78 / ultimate 114 mL**，取**使用后重量的 75 百分位**（IT-34734、2012 ULS #34724）；刻意高于平均以覆盖"更重的日子"。
4. **加液次数与速率**：**3 次加液**（与消费者反馈一致，A-36049 / A-35609）、**8 mL/s**（护垫，来自文献综述）、**37 ℃**（模拟体温）。
5. **时间结构**：加液间隔 **15 分钟**（让产品达平衡、控制测试时长）；**加液后至回渗仅 2 分钟**——因为消费者在达平衡前、换产品时就判断"是不是湿了"（IT-34734）。**这是"回渗"与"平衡吸液"的根本区别**。
6. **回渗介质**：**吸墨纸（blotter paper）**。因其容量足以容纳全部可回流液体，而**胶原蛋白容量仅约 1/10，会系统性低估表面湿气**，且不能在回渗时间尺度内吸收。
7. **压力形态**：**点压力（1 英寸直径、0.7 psi v0 / 0.5 psi v4）**——既有研究认为点压力比全表面均布压力更贴合实际使用条件。**载荷重量的选定依据未记录**。

## 关键参数表 Key Parameters

| 参数 Parameter | 典型值 / 范围 Typical Value | 出处 Source |
|---|---|---|
| 标准号 / 前代 | TTM-00643（v0 2015；**v4 2020-09**）；前代 TTM-0001 / STM-2417 / STM-00497 | [[History of FIUP TTM-00643（FIUP 测试方法沿革史）]] |
| 加液位置 | 距前端 5/12 或 7/12 产品长度 | 同上 |
| 载荷（按码） | 12 / 30 / 78 / 114 mL（ultrathin / moderate / maximum / ultimate） | 同上 |
| 载荷统计口径 | 75 百分位（IT-34734 / #34724） | 同上 |
| 加液次数 / 流速 / 温度 | 3 次 / 8 mL/s / 37 ℃ | 同上 |
| 等待时间 | 间隔 15 min；回渗前 2 min | 同上 |
| 回渗介质 | 吸墨纸（胶原容量仅约 1/10） | 同上 |
| 回渗压力 / 时间 | **0.7 psi（v0）→ 0.5 psi（v4）**；2 min；1 英寸点载荷 | 同上 |
| 量具 R&R | v0 RST 82319；v4 RST 104230（2020-02） | 同上 |
| 早期对照压力 | STM-2414 0.5 psi；STM-2408 1 psi / 3 min；自动回渗仪 1.0 psi | 同上 |

> ⚠️ **禁止无来源参数 No unsourced numbers**：表中数字均来自上列源摘要页。**两处溯源缺口**：① **0.7 → 0.5 psi 的变更理由无文档**；② **1 英寸点载荷的重量如何选定未记录**。引用本方法时必须注明**版本号（v0 还是 v4）与压力值**，否则跨期数据不可比。

## 相邻概念 Adjacent Concepts

- 上位：[[Rewet Test（回渗测试）]]、[[芯体测试方法与验收基准（STM）]]、[[Dryness Measure System（干爽度量三分）]]
- 同族方法：[[FIFE Test（FIFE 摄入-回渗评价）]]、[[Bladder Box Intake Test（膀胱箱压载摄入测试）]]、[[Cradle Intake Test（Cradle 摄入测试）]]
- 载荷口径：[[Use-Test Loading & Leakage Percentile（使用测试载荷与渗漏分位）]]
- 变异性：[[Rewet Measurement Variability（回渗测试变异性）]]、[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]
- 对比：[[Rewet Method Comparison（回渗测试方法横向对比）]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[History of FIUP TTM-00643（FIUP 测试方法沿革史）]]）：本页为方法沿革的一手记录；核心"参数—理由"配对均来自原文，未做外推。`status: seed`（单一来源，待其他 FIUP 文档互证）。

- **教训一（版本号即口径）**：v0（0.7 psi）与 v4（0.5 psi）的回渗读数**不可直接比较**；历史数据与新数据混用前必须确认版本。
- **教训二（介质决定读数）**：换用胶原蛋白会低估表面湿气（容量仅 1/10）——任何"换介质"的方法改动都要重新标定。
- **教训三（2 分钟是刻意的）**：回渗前只等 2 分钟是为了贴合消费者判湿的真实时点，不是测试偷懒；把它改成"等到平衡"会改变方法定义。
- **待补 `[待验证]`**：0.7→0.5 psi 变更的原始依据；1 英寸载荷重量的选定依据；DDLS 模型（TL-10605）对目标加液位置的估算方法。

## Evidence Update 证据追加（2026-09-29 · collagen 介质验证数据）

> ✅ Verification（2026-09-29，source 来源 [[FIUP collagen Testing Victoria Maria.pptx]]）：collagen 介质探索的量化落地——与上方教训二（"换胶原蛋白会低估表面湿气，容量仅 1/10"）的关系是**互补而非矛盾**：collagen 作为蓄液介质容量确小（**0.269 g @ 1"×2" 0.5PSI**，需 10 片叠加防饱和），但其柔软贴合消除了 blotter 的两大失真源——AD 产品 **doming（穹起）** 与纸刚度导致的全接触缺失，后者会**系统性压低** AD 的 blotter 读数。实测（Poise 6DL / AD 6D Old / Always 6DL New）：blotter 2.44" 权重口径 0.270 / 0.898 / 0.448 g（AD Old 显著最差），collagen 10 片口径 0.199 / 0.185 / 0.147 g（AD New 显著最优）——**产品排序随介质翻转**。方法含义：collagen 路线若纳入 TTM-00643，须先固化层数/容量标定；0.7PSI 变体数据已测（Poise 0.201 / AD New 0.181 g）。

## 来源 Sources

- [[History of FIUP TTM-00643（FIUP 测试方法沿革史）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Test Methods/FIUP - TTM-00643/History of FIUP.docx.md`

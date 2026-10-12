---
type: concept
title: "Surface Moisture Test（面层干爽性测试）"
domain: [卫材研发, 测试方法与表征]
status: seed
updated: 2026-09-29
tags: [面层干爽性, surface moisture, TTM-00302, FIFE, 177g, 三次注液, 回渗]
aliases: ["表面干爽性测试", "TTM-00302", "Surface Dryness Test"]
---

# Surface Moisture Test（面层干爽性测试 / TTM-00302）

> One-line definition 一句话定义：**在 FIFE 板上对同一片产品做三次定量注液**，每次记录**吸收时间**，并用 **177 g 压板 + 预称重滤纸**压 **2 min** 读取**回渗量**、同时称下层滤纸得**溢出量**——一次实验输出"摄入—溢出—回渗"三条随时间恶化的曲线，是**面层干爽性（surface dryness）**的综合判据。
> (Three successive insults on a FIFE board; per insult: intake time, run-off and rewet under a 177 g plate for 2 min — one test yields the degradation curve of the topsheet.)

## Definition 定义

面层干爽性回答的是"液体进去之后，表面还剩多少水"。它与 [[Rewet Test（回渗测试）]] 的区别在于**载荷与时间**：本方法用**常压 + 177 g 压板 + 2 min**，而国标回渗是 **1.20 kg 压块 + 1 min**、FIFE 全球版是 **14 ± 1 inH₂O 真空 + 2 min**。**三者的 g 值不是同一个量**，比较前必须先对齐载荷。

它也与"干爽"的消费者感知不同层：[[Dryness Measure System（干爽度量三分）]] 把干爽分成产品内干爽（回渗）、技术皮肤干爽（EWL/STEWIE）与感知干爽；本方法属于**产品内干爽**的轻量实现。

## Mechanism 机理拆解

1. **三次注液是为了看"衰减"**：第 1 次读的是面层/ADL 的最佳状态，第 3 次读的是芯体趋于饱和后的表现；**只看单次回渗会低估真实使用风险**。
2. **30 s 等待是固定"自由吸收窗口"**：吸收完成后等 30 s 再压板，使"未被结构吸走的自由液"有机会迁移，压板读到的才是真正的松散持留液。
3. **177 g 是低压档**：刻意用轻载荷，使读数对应**轻触/躺卧**工况，而非 8 kg 高压那种久坐工况（见 [[Rewet Test（回渗测试）]] 高低压段）。
4. **溢出量与回渗是互补的两条泄漏路径**：溢出量走"侧面流走"，回渗走"返到皮肤侧"（见 [[Run-off & Leakage Test（滑渗与渗漏测试）]]）。
5. **靶区与注液量按 Size 分档**：距吸收体前端边缘 NB 102 → XXL 146 mm，注液量 50 → 100 mL；**档位错配会让不同 Size 的产品不可比**。
6. **去皮筋是必要之恶**：去掉腿部/折页皮筋才能贴平 FIFE 板，但**剪太深会造成侧漏而作废**——制样边界就是有效边界。

## Key Parameters 关键参数表

| 参数 Parameter | 数值 / 口径 Value | 出处 Source |
|---|---|---|
| 方法编号 Method ID | **TTM-00302**（第 1 版） | [[TTM-00302 面层干爽性.doc]] |
| 测试液 Liquid | **0.9% 盐水 + 蓝粉**（0.1 g/100 mL 取 4 mL 加入 1 L），**37 ℃** | 同上 |
| 注液速度 Rate | **15 mL/s** | 同上 |
| 注液量（NB→XXL）Insult | **50 / 60 / 70 / 85 / 100 / 100 mL**（±0.5 mL） | 同上 |
| 靶区（距吸收体前端）Target zone | **102 / 114 / 127 / 140 / 146 / 146 mm**（±5 mm） | 同上 |
| 注液次数 Insults | **3 次** | 同上 |
| 吸收后等待 Wait | **30 s** | 同上 |
| 压板载荷 Plate load | **177 g** | 同上 |
| 压合时间 Hold | **2 min** | 同上 |
| 输出 Outputs | 每次吸收时间（s）、溢出重量（g）、回渗（g）；**Total rewet (g)** 与 s.d. | 同上 |
| 制样 Pretreatment | 去除腿部/折页皮筋（不得剪太深）；产品称重 0.01 g；滤纸预称重 | 同上 |
| 计算式 Formula | 回渗 = 湿滤纸重 − 干滤纸重 | 同上 |

> ⚠️ **禁止无来源参数**：全部数值来自单份 SOP（TTM-00302）；本方法在本库**暂无合格阈值**，标 `[待验证]`。

## 口径差异（不同来源同类方法，勿混为一条）

| 方法 | 载荷 | 压合时间 | 注液次数 | 液体 | 出处 |
|---|---|---|---|---|---|
| **TTM-00302 面层干爽性** | **177 g 压板（常压）** | 2 min | 3 次 | 0.9% 盐水 37 ℃ | [[TTM-00302 面层干爽性.doc]] |
| GB/T 28004-2011 回渗 | **1.20 kg / Ø100 mm 压块** | 1 min | 2 次（0 min + 5 min） | 生理盐水 | [[GB-T28004-2011 回渗渗漏.doc]] |
| FIFE Rev.5（SAT CAP） | **14 ± 1 inH₂O 真空（≈3.4 kPa）** | 2 min | 2–3 次 | 0.9% 盐水 + 染色 | [[STM-00034 FIFE - Fluid Intake Flowback Evaluation Rev.5（FIFE 摄入-回渗评价全球方法）]] |
| TTM-00623 高压反渗 | **2 × 4 kg = 8 kg** | 2 min | — | 37 ℃ 盐溶液 | [[TTM-00623高低压反渗测试.docx]] |

## 相邻概念

- 上位：[[Dryness Measure System（干爽度量三分）]]、[[Rewet Test（回渗测试）]]
- 同平台：[[FIFE Test（FIFE 摄入-回渗评价）]]（共用 FIFE 板与靶区档位）
- 互补：[[Run-off & Leakage Test（滑渗与渗漏测试）]]（溢出量的另一条口径）
- 体系：[[芯体测试方法与验收基准（STM）]]（试产清单中的 "Surface moisture" 项）

## 来源

- [[TTM-00302 面层干爽性.doc]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/TTM-00302 面层干爽性.doc.md`

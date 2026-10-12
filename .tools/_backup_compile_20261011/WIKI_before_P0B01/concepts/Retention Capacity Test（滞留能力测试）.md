---
type: concept
title: "Retention Capacity Test（滞留能力测试）"
domain: [卫材研发, 测试与验收]
status: growing
updated: 2026-09-30
tags: [Retention, 滞留能力, STM-00033, 保液, 芯体]
---

# Retention Capacity Test（滞留能力测试 / STM-00033）

> 一句话定义：在 **14±1 英寸水柱（in WC）外压**下测定纸尿裤/纸尿片**保有的液量（滞留能力）**，反映芯体"受压也不掉液"的能力，是 SAP/绒毛浆复合芯体的基础保液指标。

## Definition 定义 / Principle 原理

样品先自由漂浮吸液（无纺布面朝下、不触底），再在乳胶膜覆盖下承受真空外压，迫使未"锁住"的自由液被抽出；剩余液量即为滞留量。它测的是**结构锁液能力**而非表面回渗，因此与 Rewet（回渗）互补：Rewet 看表层返湿，Retention 看整体保液。

## 方法口径（Caliber 标定）

| 参数 | 典型值 / 范围 | 出处 |
|---|---|---|
| 外压（真空） | 14 ± 1 in WC | [[STM-00033 滞留能力.docx]] |
| 浸泡时间 | 20 min ± 15 s | [[STM-00033 滞留能力.docx]] |
| 滴水时间 | 1 min ± 15 s | [[STM-00033 滞留能力.docx]] |
| 测试时间 | 5 min ± 15 s | [[STM-00033 滞留能力.docx]] |
| 盐溶液高度 | 2 inch（51 mm） | [[STM-00033 滞留能力.docx]] |
| 称重精度 | 0.01 g | [[STM-00033 滞留能力.docx]] |
| 绝对滞留 | 湿重 − 干重（g） | [[STM-00033 滞留能力.docx]] |
| 相对滞留 | 绝对滞留 ÷ 干重（g/g） | [[STM-00033 滞留能力.docx]] |

> ⚠️ **禁止无来源参数**：上表口径来自单份 SOP（STM-00033）；库内暂无该方法的合格基准值（Pass/Excellent 门槛），标 `[待验证]`。

## 相邻概念

- 互补指标：[[Rewet Test（回渗测试）]]、[[SAP性能指标（CRC AUL GBP Vortex）]]
- 芯体对象：[[SAP（高吸水树脂）]]、[[绒毛浆（Fluff Pulp）]]、[[芯体测试方法与验收基准（STM）]]

## 经验教训

- **滞留 ≠ 回渗**：本文档明确施加 14 in WC 外压，衡量"压力下保液"；评价芯体时应与 Rewet 成对引用。
- **待补 `[待验证]`**：合格/优秀滞留基准；不同尺寸产品的干重归一方式。


> ✅ 验证（2026-09-29，来源 [[Preemie Diaper Absorption Test Methods & Parameters（早产儿纸尿裤吸收性能测试方法与参数）]]）：滞留能力在**早产儿规格**下的建模区间为 **104–125 g**，与常规规格不是同一量级；同来源给出 STM-00033 滞留压力 **3.45 kPa（0.5 PSI）** 作为对照。**早产儿数值为建模值且仅单一来源，标 `[待验证]`，不得作为验收限值引用。**

## 来源

- [[STM-00033 滞留能力.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-00033 滞留能力.docx.md`
- [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/STM-00034 FIFE/BCC成品STM-南京南厂 1.pdf.md`
- [[Finished Product Testing Method Summary（成品测试方法汇总表）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/Finished Product Testing Method Summary.xlsx.md`

> ✅ 验证（2026-09-29，来源上述两份）：本页原「待补」的滞留能力正式口径已确认——方法编号 **STM-00033**，全称明写压力为 **3.45 kPa（0.5 PSI）**；南京南厂 WI-56234 的滞留能力法与之一致，写作 **14 ± 1 英寸水柱**（≈ 3.4 kPa），并规定浸泡 20 min ± 15 s、滴水 1 min ± 15 s、测试 5 min ± 15 s。两处表述**互相印证 0.5 psi ≈ 3.4–3.45 kPa 这一换算锚点**。滞留能力分级：**绝对滞留（g）= 湿重 − 干重**；**相对滞留（g/g）= 绝对滞留 / 干重**。
- [[Preemie Diaper Absorption Test Methods & Parameters（早产儿纸尿裤吸收性能测试方法与参数）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/早产儿测试方法.docx.md`

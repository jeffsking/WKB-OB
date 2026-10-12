---
type: concept
title: "Static Mannequin Test（静态假人测试）"
domain: [卫材研发, 测试与验收]
status: seed
updated: 2026-09-29
tags: [Mannequin, 假人测试, WI-63848, 渗漏, 吸收, 尿液模拟液]
---

# Static Mannequin Test（静态假人测试 / WI-63848）

> 一句话定义：把纸尿裤穿在**多工作站静态假人（Static Mannequin）**上，以恒温尿液模拟液按设定流速/体积注液，评价产品在穿着姿态下的**吸收与漏尿性能（absorption & leakage）**的产品级方法。

## Definition 定义 / Principle 原理

假人实验室（BSG1，Rockwell 平台）用蠕动泵把加热到体温的尿液模拟液按程序注入穿戴好的产品，模拟一次或多次排泄；注液过程中产品在 Sitting / Prone / Side 等姿势下承受液体冲击，漏出的液体被漏点探测垫捕获。核心是**用可控的"人工排泄"替代主观穿戴评价**，把渗漏定位到 17 个标准解剖位置。

## 方法口径（Caliber 标定）

| 参数 | 典型值 / 范围 | 出处 |
|---|---|---|
| 模拟液 | 0.1 g 牛黄酸胆酸钠 + 1 L 生理盐水 | [[WI-63848 Static mannequin.docx]] |
| 模拟液温度 | 37 ± 1 °C | [[WI-63848 Static mannequin.docx]] |
| 注液流速 | 15 mL/s | [[WI-63848 Static mannequin.docx]] |
| 工作站延迟 | 10 s（可调） | [[WI-63848 Static mannequin.docx]] |
| 注液体积 | 按产品型号（润洗用 300 mL） | [[WI-63848 Static mannequin.docx]] |
| 液体校准 | ±3%（称重） | [[WI-63848 Static mannequin.docx]] |
| 管路校准 | ±1%（MASTERFLEX L/S，Tube 17） | [[WI-63848 Static mannequin.docx]] |
| 漏点定位 | 17 点 BCC Leak Locations 标准图 | [[WI-63848 Static mannequin.docx]] |
| 姿势 | Sitting / Prone / Side | [[WI-63848 Static mannequin.docx]] |

> ⚠️ **禁止无来源参数**：以上口径均来自单份 SOP（WI-63848）；不同产品型号的注液体积、次数与合格判据来自试产/验收文档，本文未给出，标 `[待验证]`。

## 相邻概念

- 同类方法：[[Mannequin BM Test（BM 假人测试）]]、[[Run-off & Leakage Test（滑渗与渗漏测试）]]
- 配套试剂：[[尿液模拟液（Urine Analog）]]
- 平台：[[Mannequin Lab（Rockwell 假人平台）]]

## 经验教训

- **校准是数据可信的前提**：原文要求润洗后液体不可复用、液体校准 ±3%、管路 ±1%，否则注液体积偏差直接污染渗漏结论。
- **待补 `[待验证]`**：各尺寸/姿势的合格渗漏判据；与 Cradle、L-H 等摄入类方法的关联基准。


> ✅ 验证（2026-09-29，来源 [[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]]）：动态版（WI-63849，第 0 版，2024-02-20）与静态版（WI-63848）**共用同一平台与试剂口径**——牛黄酸胆酸钠 **0.1 g/L 盐水**、**37 ± 1 ℃**、润洗 **300 mL**、液体校准 **±3%**、管路 MASTERFLEX L/S **Tube 17 ±1%**、漏点 **17 区**，差异仅在「运动姿态 + 六项合身性指标」。**故两法的液体与管路校准可互认，但漏点判据与输出指标不可互换。** 编号待核：本页参考项写 **TTM-00313-8**，成品总表写 **TTM-00318-8** `[待验证]`。

## 来源

- [[WI-63848 Static mannequin.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/WI-63848 Static mannequin.docx.md`
- [[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/WI-63849 Motion mannequin.docx.md`

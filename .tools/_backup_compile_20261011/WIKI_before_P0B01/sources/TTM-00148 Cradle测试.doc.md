---
type: source
title: "TTM-00148 Cradle测试.doc"
source_type: 内部测试方法
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/TTM-00148 Cradle测试.doc.md
original_link: ""
date_published: 2021-08-24
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "Cradle 测试把产品拉伸固定在托架上，按 Size 给定流量/容积，测三次 intake time（摄入/吸收时间）——本库产品级吸液速度的主口径（中文：Cradle 试架模拟穿着姿态，测三次摄入时间）"
  - "注液位置按「距产品中心」定义，且 Diaper 与 Pant 男/女三套坐标不同（中文：尿裤与裤型男女注液点不同，不可混用）"
  - "三次注液间隔 15 min；数据无效条件有三条（液体落到非吸收部分 / 流出折页落到模具 / 超过 5 min 才流转）"
  - "泵校验接受窗口为流出液重量 ±3 g（中文：每次测试前与换 Size 时必须校验泵）"
pages_linked: ["[[Cradle Intake Test（Cradle 摄入测试）]]", "[[Rewet Test（回渗测试）]]", "[[Liquid Diffusion Test（液体扩散测试）]]", "[[芯体测试方法与验收基准（STM）]]", "[[KC U Rewet测试.docx]]", "[[TTM-00623高低压反渗测试.docx]]", "[[TTM-00279产品30°滑渗测试.docx]]"]
---

# TTM-00148 Cradle测试.doc

## 一句话定位 One-line Positioning

成品级 **intake time（摄入时间）** 的内部标准方法：把纸尿裤套在 Cradle 试架上模拟穿着状态，按 Size 定量注液并记录三次吸收时间。是 TTM-00623 / TTM-00279 / KC U Rewet 三份成品方法的**共同基准协议**（注液量、流速、注液点均"按 Cradle 设置"）。

## 摘要 Summary

本方法用于模拟纸尿裤穿在身上时吸收一定量液体所需要的时间。测试液为 0.1 g 蓝色食品级粉末定容至 100 mL 蒸馏水后取 4 mL 加入 1 L 0.9% 盐溶液，水浴加热至 37 ℃。泵在每次测试前及不同 Size 检测时校验，以流出液重量落入目标值 ±3 g 为可接受。样品拉伸固定于 Cradle 托架、前端面朝测试者、产品中心对准托架凹槽最底部，出液口距产品水平 10 mm。按 Run 键同时秒表计时，待全部液体渗到表面以下即停表；15 min 后设备自动第二次注液，再过 15 min 第三次。出现三类情况（液体滴到非吸收部分、液体流出折页落到 Cradle 模具、液体超过 5 min 才流转）时数据判为无效并应载明产品失败。

## 测试方法要点 Method Specification

**测试液与仪器 Test fluid & rig**

| 项目 | 口径 | 备注 |
|---|---|---|
| 测试液 | 0.1 g 蓝色食品级粉末 → 100 mL 定容；取 4 mL → 1 L 0.9% 盐水 | 中文：染料仅作可视追踪，不改盐浓度 |
| 液温 | 37 ℃（水浴） | 每次测试前加热 |
| 泵校验判据 | 流出液重量 目标值 ±3 g | 换 Size 必重校 |
| 出液口位置 | 距产品水平 10 mm | 过近会飞溅 |

**按 Size 的注液参数 Injection parameters by size**

| 设置 | NB | S | M | L | XL | XXL |
|---|---|---|---|---|---|---|
| Flow rate（原文单位记作 mL） | 600 | 720 | 900 | 900 | 900 | 900 |
| DISP（s） | 60 | 60 | 60 | 60 | 60 | 60 |
| Insult Rate（mL/s） | 10 | 12 | 15 | 15 | 15 | 15 |
| Volume（mL） | 50 | 60 | 70 | 85 | 100 | 100 |

> ⚠️ 口径提示：原文表中 Flow rate 一列单位写作"mL"，与 DISP（s）并列时逻辑上应为 mL/s 或 mL（在 60 s 内）；此处**照录原文**，实际量纲标 `[待验证]`。

**注液点（距产品中心位置）Injection point, distance from product centre (mm)**

| 产品类型 | NB | S | M | L | XL | XXL |
|---|---|---|---|---|---|---|
| Diaper 尿裤（通用） | 55 | 65 | 75 | 85 | 90 | 92 |
| Pant 裤型 · 男 | 75 | 85 | 95 | 105 | 110 | 112 |
| Pant 裤型 · 女 | 35 | 45 | 55 | 65 | 70 | 72 |

**时序 Timing**

1. 装样 → 调 Volume 灯 → 出液口对准前端标记 → Run + 秒表 → 记录 1st intake time。
2. 15 min 后设备自动重复注液 → 记录 2nd intake time。
3. 再过 15 min → 记录 3rd intake time。

**数据无效条件 Invalid-data conditions**

- a. 液体滴到产品非吸收部分 → 无效，载明产品失败。
- b. 液体流出折页落到 Cradle 模具上 → 无效，载明产品失败。
- c. 液体超过 5 min 后才流转 → 无效，载明产品失败。

## 提炼的数字与结论 Key Numbers & Findings

| 项目 | 数值 / 结论 | 备注 |
|---|---|---|
| 版本 | 第 1 版 | 修订日期 2021-08-24 |
| 注液次数 | 3 次 | 间隔 15 min |
| 出液口距产品 | 水平 10 mm | — |
| 单次注液量 | 50 → 100 mL（NB → XXL） | 见表 |
| 泵校验窗口 | ±3 g | — |
| 测试液温度 | 37 ℃ | — |

## 关键论断 key_claims

- **Cradle 是本库成品吸液速度的主协议** —— 支撑页：[[Cradle Intake Test（Cradle 摄入测试）]]、[[TTM-00623高低压反渗测试.docx]]、[[TTM-00279产品30°滑渗测试.docx]]
- **注液点必须声明产品类型与性别** —— 支撑页：[[Cradle Intake Test（Cradle 摄入测试）]]
- **三次摄入 + 15 min 间隔是本方法的时间口径** —— 支撑页：[[芯体测试方法与验收基准（STM）]]

## 关联页面 Related Pages

- 概念：[[Cradle Intake Test（Cradle 摄入测试）]]、[[Rewet Test（回渗测试）]]、[[Liquid Diffusion Test（液体扩散测试）]]
- 直接沿用本协议的其他来源：[[KC U Rewet测试.docx]]、[[TTM-00623高低压反渗测试.docx]]、[[TTM-00279产品30°滑渗测试.docx]]
- 上位索引：[[芯体测试方法与验收基准（STM）]]

## 原文 Source

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/TTM-00148 Cradle测试.doc.md`
- 原文链接：（无；内部测试方法）

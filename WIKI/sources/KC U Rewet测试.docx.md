---
type: source
title: "KC U Rewet测试.docx"
source_type: 内部测试方法
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/KC U Rewet测试.docx.md
original_link: ""
date_published: 2021-03-01
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "U Rewet 在同一协议内同时产出三个读数：两次吸收时间 + 扩散长度 + 回渗量，回渗以国标回渗压块压 1 min 的量差计（中文：一份方法覆盖 speed / spread / rewet 三件事）"
  - "两次注液的实测等待为 5 min（正文「5 分钟后设备启动重复注入液体」），而操作界面 Pause 灯显示「15'」——原文两处不一致，本页照录并存疑（中文：同型号仪器的等待时长口径存在内部矛盾，跨方法比较时须以正文 5 min 为实测值，并标 [待验证]）"
  - "回渗量 = 湿滤纸重 − 干滤纸重；扩散长度 = 第二次注液后等待 5 min，贴到国标回渗测试板上量的扩散区 MD 长度（中文：扩散长度按 MD 取值，且量尺不得接触产品表面）"
  - "测试液、泵校验表与注液点坐标（NB→XXL 各 6 档）与 TTM-00148 Cradle 完全一致（中文：U Rewet 与 Cradle 共用同一套注液参数表）"
pages_linked: ["[[Rewet Test（回渗测试）]]", "[[Cradle Intake Test（Cradle 摄入测试）]]", "[[Liquid Diffusion Test（液体扩散测试）]]", "[[TTM-00148 Cradle测试.doc]]", "[[Rewet Protocols Compared（回渗测试口径对比）]]"]
---

# KC U Rewet测试.docx

## 一句话定位 One-line Positioning

**U Rewet 测试**（第 2 版）：在 Cradle 试架 + 定量注液的基础上加"国标回渗压块"环节，一次测出**吸收时间 / 扩散长度 / 回渗量**三个读数。是 [[Rewet Protocols Compared（回渗测试口径对比）]] 中"低负载、短等待"的代表口径。

## 摘要 Summary

本测试用于模拟纸尿裤穿在身上时吸收一定量液体所需的时间和回渗。测试液配置、37 ℃ 水浴、泵校验流程与按 Size 的注液参数表（Flow rate 600–900、DISP 60 s、Insult Rate 10–15 mL/s、Volume 50–100 mL）与 TTM-00148 Cradle 一致。样品准备阶段先称量产品干重（Weight (Dry Product)）与国标回渗滤纸干重（Weight (Dry Paper)），标记产品中心并按各 Size 的注液点坐标（尿裤通用 55–92 mm；裤型男 75–112 mm、女 35–72 mm）标记测试位置，把样品拉伸固定在 Cradle 托架上、中心对准托架凹槽最底部，并沿折页和腿部捋平使折页立起且不挡吸收芯。测试时设定 Flow rate 与 Volume、DISP 显示 60、Pause 灯显示 15'，出液口距产品水平 10 mm，按 Run 同时秒表计时，记录第一次吸收时间；5 min 后设备重复注入并记录第二次吸收时间；第二次注液后再等 5 min，取下尿裤贴于国标回渗测试板、用直尺量扩散区 MD 长度作为扩散长度，随后把滤纸放在扩散区域（尽量与扩散中心重合）并压国标回渗压块 1 min，称滤纸湿重。最后回渗 = Weight (Wet Paper) − Weight (Dry Paper)。

## 测试方法要点 Method Specification

**共用注液参数（与 TTM-00148 一致）Shared injection parameters**

| 设置 | NB | S | M | L | XL | XXL |
|---|---|---|---|---|---|---|
| Flow rate | 600 | 720 | 900 | 900 | 900 | 900 |
| DISP（s） | 60 | 60 | 60 | 60 | 60 | 60 |
| Insult Rate（mL/s） | 10 | 12 | 15 | 15 | 15 | 15 |
| Volume（mL） | 50 | 60 | 70 | 85 | 100 | 100 |
| Pause | 15'（设备档位显示） | — | — | — | — | — |

> ⚠️ 口径矛盾（2021-03-01 原文内部）：操作步骤写"调至 Pause 灯亮显示 15'"，但正文实测为"5 分钟后设备启动重复注入液体"且"第二次注液后等待 5 分钟"。**本页不裁决**，5 min 为实测等待值（标 `[待验证]`）。

**注液点（距产品中心，mm）Injection point**

| 产品类型 | NB | S | M | L | XL | XXL |
|---|---|---|---|---|---|---|
| Diaper & Diaper Pant（通用） | 55 | 65 | 75 | 85 | 90 | 92 |
| 男 | 75 | 85 | 95 | 105 | 110 | 112 |
| 女 | 35 | 45 | 55 | 65 | 70 | 72 |

**读数与计算 Measurements & formulas**

| 读数 | 方法 | 单位 |
|---|---|---|
| 第一次吸收时间 | Run 同时秒表计时 → 液体全部渗到表面以下停表 | s |
| 第二次吸收时间 | 第一次后 5 min 重复注液 | s |
| 扩散长度 | 第二次注液后等 5 min，贴国标回渗测试板量扩散区 MD 长度 | mm |
| 回渗量 | 国标回渗压块压 1 min → 回渗 = Weight (Wet Paper) − Weight (Dry Paper) | g |
| 产品干重 | Weight (Dry Product) | g |

## 提炼的数字与结论 Key Numbers & Findings

| 项目 | 数值 / 结论 | 备注 |
|---|---|---|
| 版本 | 第 2 版 | 修订日期 2021-03-01 |
| 注液次数 | 2 次 | 与 Cradle 的 3 次不同 |
| 注液间隔 | 5 min（实测口径；Pause 显示 15' 与之矛盾） | 与 Cradle 的 15 min 不同 |
| 回渗加载 | 国标回渗压块，压 1 min | 低负载短压 |
| 出液口距产品 | 水平 10 mm | 与 Cradle 一致 |
| 测试液 | 0.1 g 蓝粉 → 100 mL；取 4 mL → 1 L 0.9% 盐水，37 ℃ | 与 Cradle 一致 |
| 泵校验窗口 | ±3 g | 与 Cradle 一致 |

## 关键论断 key_claims

- **U Rewet 与 Cradle 共用注液参数但等待时长不同（5 min vs 15 min）** —— 支撑页：[[Rewet Protocols Compared（回渗测试口径对比）]]、[[TTM-00148 Cradle测试.doc]]
- **一份方法三读数（speed / spread / rewet）** —— 支撑页：[[Rewet Test（回渗测试）]]、[[Liquid Diffusion Test（液体扩散测试）]]
- **扩散长度按 MD 取值且量尺不得接触产品表面** —— 支撑页：[[Liquid Diffusion Test（液体扩散测试）]]

## 关联页面 Related Pages

- 概念：[[Rewet Test（回渗测试）]]、[[Cradle Intake Test（Cradle 摄入测试）]]、[[Liquid Diffusion Test（液体扩散测试）]]
- 同族来源：[[TTM-00148 Cradle测试.doc]]
- 对比：[[Rewet Protocols Compared（回渗测试口径对比）]]

## 原文 Source

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/KC U Rewet测试.docx.md`
- 原文链接：（无；内部测试方法）

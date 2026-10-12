---
type: source
title: "mocon底膜透气率测试.docx"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/mocon底膜透气率测试.docx.md
original_link: ""
date_published: 2024-01-18
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Mocon 底膜透气率方法（第 0 版，2024-01-18）：MOCON PERMATRAN-W 101K 测底膜透湿性能（WVTR 类读数）"
  - "口径：6 腔体（A–F）平行；腔体水温 37.8 ℃；37 ℃ 纯水补至距水槽平面 5 mm；气路 25 PSI（分压阀）/15 PSI（设备阀）；Test Mode Convergence"
  - "双层校准：Cal C（Raw Counts 校准至 60±2，每腔 5 min 调整窗口）+ 标准膜校准（偏差不得大于 19%，Excel 自动算校准因子）"
pages_linked: ["[[WVTR 测试口径（失重法 vs 增重法）]]", "[[Film-Free Backsheet（无膜背层）]]"]
---

# mocon底膜透气率测试.docx

## 一句话定位

**底膜透湿率标准仪器法（英文：backsheet WVTR by MOCON PERMATRAN-W 101K）**：测试底膜（backsheet）的透气/透湿性能（中文：透湿量 gm/m²·day），第 0 版（2024-01-18）—— breathable 底膜呼吸性能的仲裁级读数。

## 摘要

校准分两层：**Cal C 校准**（长期停用或数据明显差异时）在软件中将 Test Mode 设为 Continuous、Exam Minutes 5 min、Cal Mode 选 Active Cal C，依次缓慢旋转 A–F 腔体旋钮把 Raw Counts 校准到 60±2，每腔仅 5 min 调整窗口且有显示延迟，建议厂家指导下进行；腔体水温尽量达 37.8 ℃。**标准膜校准**：标准膜按"this side to carrier gas"标识面向下放置（不可触碰表面），测试后把标称值与实测值录入 Excel，**偏差不得大于 19%** 否则重校，Excel 自动算校准因子后输入软件 Expected TR 完成 Calibrate。取样避开破裂/褶皱/污染，用取样模快裁切。气路：气瓶余量 <3 kg 不得测试，分压阀 25 PSI、设备阀 15 PSI，铜管接口不可弯曲；开机顺序气瓶总阀→分压阀→设备阀→设备电源→软件。装样：样品测试面向上平铺于测试仓黑色垫片，水槽箭头朝操作者水平放置（不可旋转扭动、不可触碰槽底薄膜），注射器补加 37 ℃ 纯水至距槽面 5 mm，锁紧固定螺栓。软件设 Material ID、Cal C Mode 必须为 Use Last Cal C，单腔或 6 腔全测（Convergence 模式，报告中 Temperature setpoint 37.8 ℃、Exam Minutes 10）。输出 Transmission Rate gm/m²·day 与 Permeation gm·mil/m²·day。关机顺序与开机相反。

## 提炼的数字与结论

| 项目 | 数值 / 结论 | 备注（口径 Caliber） |
|---|---|---|
| 仪器 | MOCON PERMATRAN-W 101K | 6 腔体（A–F）平行 |
| 读数 | Transmission Rate（gm/m²·day）；Permeation（gm·mil/m²·day） | Convergence 模式，报告示例 Exam Minutes 10 |
| 温度 | 腔体 37.8 ℃（水浴）；纯水 37 ℃ 补液至距槽面 5 mm | 加湿法（water method） |
| 气路 | 分压阀 25 PSI / 设备阀 15 PSI | 气瓶余量 <3 kg 禁测 |
| Cal C | Raw Counts 60±2，每腔 5 min 窗口 | 依赖手法，建议厂家指导 |
| 标准膜 | 偏差 ≤19% | Excel 自动算校准因子 |
| 试样 | 避开破裂/褶皱/污染；测试面向上 | 取样模快裁切 |

> ⚠️ **口径提示（2026-09-29）**：本方法为**仪器化增湿法（水在膜一侧蒸发透过）**，读数口径与杯式失重法/增重法（[[WVTR 测试口径（失重法 vs 增重法）]]）不同，温度条件（37.8 ℃）亦区别于常规 23/38 ℃ 标准组合——跨方法 WVTR 数值**只能排序、不能换算**。
> ⚠️ **单源数值 [待验证]**：取样模快尺寸与测试面积（报告示例 10 cm²）、测试周期未在正文文字中完整给出。

## 关键论断（key_claims）

- **Cal C + 标准膜双层校准是 MOCON 数据可信度的前提，两项校准记录须与测试数据同批保存** —— 支撑页：[[WVTR 测试口径（失重法 vs 增重法）]]
- **6 腔平行 + Convergence 判停，适合底膜来料批次横向比对** —— 支撑页：[[Film-Free Backsheet（无膜背层）]]

## 关联页面

- 概念：[[WVTR 测试口径（失重法 vs 增重法）]]（追加 2026-09-29 注记）、[[Film-Free Backsheet（无膜背层）]]
- 对比：[[SMMMS Film-Free vs Microporous Film Backsheet（无膜背层 vs 微孔膜背层）]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/mocon底膜透气率测试.docx.md`
- 原文链接：（无）

---
type: source
title: "T5 Pants COCO V2 TD34 Trial Results（四个 Bench Code 与试产数据）"
source_type: 内部试产结果总结（PDP T5 Pants L 码 bench 数据 + 施胶参数）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Products/T5 Pants COCO V2 with trial on TD34 Results Summary - 20191112.pptx.md
original_link: ""
date_published: 2019-11-12
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "四个 Bench Code 的差异**只有 LSN 与 PSN 两处**：REL 恒为 DY 40gsm TABCW（12D+6D 混纤）、SAM 恒为 Sandia N210、Liner 恒为 26gsm DY DL794 ⇒ 这是一组**近乎干净的双因子对比**（LSN 材质/克重 × PSN 供应商/克重）"
  - "**回渗最优是 Code 8（0.07 g，木芯 38gsm LSN + Hezhong 35gsm PSN）**，最差是 Code 9（0.65 g，同为木芯 38gsm LSN 但换 Ouli 36gsm PSN）⇒ **木芯 LSN 不是充分条件，PSN 供应商与 LSN 存在组合效应（interaction），不能单因子外推**"
  - "**表面残液 Surface Moisture 与回渗同向但放大差异**：Code 8 0.14 g vs Code 7 1.12 g vs Code 9 1.05 g vs Bench Code A 0.42 g ⇒ 表面残液是比回渗**更敏感**的鉴别指标（极差约 8 倍 vs 回渗约 9 倍，但残液在低端分辨率更高）"
  - "**第三次吸收时间（3rd intake）是区分度最大的动力学指标**：Bench Code A 32.05 s vs Code 7 20.26 s vs Code 8 14.14 s vs Code 9 20.60 s ⇒ 与回渗排序**完全一致**，可作为回渗的早期代理指标（proxy）"
  - "面层侧游离 SAP（SAM on Liner）最低为 Code 7（light off 0.6 / light on 2），最高为 Bench Code A（3.6 / 8）⇒ 木芯 LSN 对**SAP 上窜有抑制作用**，但 Code 9 回升至 1.4/6 ⇒ 同样受 PSN 组合调制"
  - "Free SAM 几乎全部集中在 PSN 侧（0.41–0.57 g）而非 LSN 侧（0.01–0.06 g），**相差约一个数量级** ⇒ 芯体游离 SAP 的取样/判读应以**PSN 侧为主判据**"
  - "Pad integrity 四码均 ≥980 次（上限 1000 次即封顶）⇒ 该指标**已失去分辨力**，不能用于 Code 间优选"
  - "⚠️ 数据可信度限制：全部数值自**图表 OCR/图片文本**提取，未报重复数与标准差；Code 9 回渗 Max=1.84 g（Ave 0.65）⇒ **组内离散极大**，其 Ave 不足以支撑结论，须重测"
pages_linked: ["[[COCO芯体平台]]", "[[Rewet Test（回渗测试）]]", "表面残液 Surface Moisture（指标定义见 [[Rewet Test（回渗测试）]]）", "[[Cradle Intake Test（Cradle 摄入测试）]]", "[[IPC BCC OI Portfolio（开放创新项目组合）]]"]
---

# T5 Pants COCO V2 TD34 Trial Results（四个 Bench Code 与试产数据）

## 一句话定位

**CD Pants COCO V2（China BCC R&D，2019-11）在 TD34 产线上的试产结果总结**：给出 4 个 Bench Code 的**完整层结构 + 尺寸分配（M/L/XL/XXL）+ PDP T5 Pants L 码的 bench 测试数据 + L 码施胶参数**。本库价值：它是 [[COCO芯体平台]] 的**早期（V2 代）基线数据**，且四个 Code **只变 LSN 与 PSN 两层**，是一组难得的**近干净双因子对比**——可直接用于判读「LSN 材质 × PSN 供应商」的**组合效应**，避免单因子外推。

## 摘要

文档为 `T5 Pants COCO V2 with trial on TD34 Results Summary - 20191112.pptx`。结构层从面层侧到膜侧依次为：Liner → LSN（上包裹层）→ LSS（上层 SAP/绒毛浆）→ REL（收集传递层）→ PSS（下层 SAP）→ PSN（下包裹层）→ Poly。芯体采用 **Breeze 1.0 Core**，尺寸 M/L 为 355×110 mm，XL/XXL 为 365×120 mm。

四个 Bench Code 的**唯一变量是 LSN 与 PSN**：

| Code | LSN | PSN | 其余层 |
|---|---|---|---|
| **Bench Code A**（对照） | Nanliu（南六）26gsm SPL，Rayon + PET 混纤 | Ouli（欧丽）36gsm Hydroknit | 同 |
| **Code 7** | N-Bond 木芯材料 **28gsm** | Hezhong（合众）35gsm Hydroknit | 同 |
| **Code 8** | N-Bond 木芯材料 **38gsm** | Hezhong 35gsm Hydroknit | 同 |
| **Code 9** | N-Bond 木芯材料 **38gsm** | **Ouli 36gsm Hydroknit** | 同 |

固定项：Liner = 26gsm DY DL794（M/L 宽 180 mm，XL/XXL 宽 200 mm）；REL = DY 40gsm TABCW（12D + 6D 混纤）；**SAM = Sandia N210**。

**核心结果（PDP T5 Pants L 码）**：Code 8 全面最优——回渗 0.07 g、表面残液 0.14 g、第三次吸收时间 14.14 s；Code 9 最差——回渗 0.65 g（Max 1.84 g）、表面残液 1.05 g。**Code 8 与 Code 9 的 LSN 完全相同（木芯 38gsm），仅 PSN 供应商与克重不同，结果却从最优翻转为最差 ⇒ 存在强组合效应。**

## 提炼的数字与结论

### 尺寸与 SAP 分配（四个 Code 共用）

| 尺寸 | Liner 宽 | PSN 宽 | LSN 宽 | REL 宽 | LSS SAM | PSS SAM | **SAM 总添加量** |
|---|---|---|---|---|---|---|---|
| M | 180 mm | 155 mm | 155 mm | 115 mm | 6 g（153.6 gsm） | 4 g（102.4 gsm） | **10 g** |
| L | 180 mm | 155 mm | 155 mm | 115 mm | 6 g（153.6 gsm） | 6 g（153.6 gsm） | **12 g** |
| XL | 200 mm | 165 mm | 165 mm | 125 mm | 6.5 g（148.4 gsm） | 6.5 g（148.4 gsm） | **13 g** |
| XXL | 200 mm | 165 mm | 165 mm | 125 mm | 7 g（159.8 gsm） | 6.5 g（148.4 gsm） | **13.5 g** |

> 判读：M 码的上下层 SAP **不对称（6/4）**，L 及以上趋于对称（6/6、6.5/6.5）。**M→L 的总量增加全部来自 PSS（4→6 g）**，即**下层补强**，与「大码需要下层兜底」的直觉一致。

### Bench 测试结果（Ave / Max / Min）

| 指标 | Bench Code A | Code 7 | Code 8 | Code 9 |
|---|---|---|---|---|
| 产品重量 / g（回渗组） | 31.41（31.79/31.07） | 31.07（31.33/30.87） | 31.54（31.76/31.37） | 31.39（31.77/31.01） |
| **National Rewet / g** | 0.26（0.37/0.00） | 0.09（0.37/0.01） | **0.07（0.18/0.04）** | **0.65（1.84/0.12）** ⚠️ |
| Run-off / g | 0.00 | 0.00 | 0.00 | 0.01（0.08/0.00） |
| Thickness / mm | 3.57（3.75/3.34） | 3.53（3.87/3.28） | 3.54（3.91/3.07） | 3.39（3.59/3.19） |
| **Surface Moisture / g** | 0.42（0.50/0.32） | 1.12（1.52/0.55） | **0.14（0.16/0.13）** | 1.05（1.76/0.16） |
| Cradle 1st intake / s | 23.63 | 22.23 | 22.84 | 21.21 |
| Cradle 2nd intake / s | 14.07 | 13.37 | 12.13 | 13.98 |
| **Cradle 3rd intake / s** | **32.05（27.13–41.06）** | 20.26（17.55–24.60） | **14.14（12.18–18.47）** | 20.60（19.45–22.20） |
| Pad integrity / 次 | 980（800–1000） | 1000 | 1000 | 1000 |
| **Free SAM — PSN 侧 / g** | 0.46 | 0.57 | 0.44 | 0.41 |
| Free SAM — LSN 侧 / g | 0.01 | 0.05 | 0.06 | 0.06 |
| **SAM on Liner（light off / on）** | **3.6 / 8** | **0.6 / 2** | 2.0 / 2 | 1.4 / 6 |

### L 码施胶参数（基于 TD34 试产参照）

| 施胶位置 | 尺寸 / mm | 上胶量 / g | 花型 | 胶型 |
|---|---|---|---|---|
| LSN Ad | 140 | 0.397 | Signature | Construction |
| SAM1（Liner 侧） | 108 | — | — | — |
| REL Ad（Liner 侧） | 106 | 0.341 | Signature | Construction |
| REL | 110 | — | — | — |
| REL Ad（Poly 侧） | 106 | 0.341 | Signature | Construction |
| SAM2（Poly 侧） | 108 | — | — | — |
| PSN Ad | 106 | 0.397 | Signature | Construction |

> 判读：**四处施胶全部为 Construction 胶 + Signature 花型**，无差异化设计；上胶量呈**对称分布**（上下包裹各 0.397 g，REL 两侧各 0.341 g）。这是典型的**结构胶主导**方案，与后期 [[Glueless Bonding（无胶粘合工艺族）]] 的减胶方向形成对照。

## 关键论断（key_claims）

- **四个 Code 只有 LSN 与 PSN 两个变量** ⇒ 近干净双因子设计；REL / SAM / Liner 全固定。 —— 支撑页：[[COCO芯体平台]]
- **回渗最优 Code 8 = 木芯 38gsm LSN + Hezhong 35gsm PSN（0.07 g）**；**最差 Code 9 = 同为木芯 38gsm LSN + Ouli 36gsm PSN（0.65 g）** ⇒ **木芯 LSN 不是充分条件，存在 LSN × PSN 组合效应**。 —— 支撑页：[[Rewet Test（回渗测试）]]
- **表面残液（Surface Moisture）比回渗更敏感**：Code 8 0.14 g 与 Code 7 1.12 g 相差 8 倍，而回渗仅差 1.3 倍 ⇒ 在**低回渗区间**应改用表面残液做鉴别。 —— 支撑页：表面残液 Surface Moisture（指标定义见 [[Rewet Test（回渗测试）]]）
- **第三次吸收时间与回渗排序完全一致**（A 32.05 > C9 20.60 ≈ C7 20.26 > C8 14.14）⇒ 可作为**回渗的早期代理指标**，用于快速筛选。 —— 支撑页：[[Cradle Intake Test（Cradle 摄入测试）]]
- **木芯 LSN 抑制 SAP 上窜**：SAM on Liner 由 Bench Code A 的 3.6（light off）降至 Code 7 的 0.6；但 Code 9 回升至 1.4 ⇒ 同样受 PSN 组合调制。 —— 支撑页：[[COCO芯体平台]]
- **Free SAM 集中在 PSN 侧（0.41–0.57 g），LSN 侧仅 0.01–0.06 g** ⇒ 相差约 10 倍，取样判读**应以 PSN 侧为主判据**。 —— 支撑页：[[COCO芯体平台]]
- **Pad integrity 四码均 ≥980 次（上限封顶 1000）** ⇒ 指标**饱和、失去分辨力**，不可用于 Code 优选。 —— 支撑页：[[芯体测试方法与验收基准（STM）]]
- ⚠️ **数据可信度限制**：全部数值自图表图片文本提取，未报 n 与标准差；Code 9 回渗 Max = 1.84 g vs Ave 0.65 g ⇒ **组内离散极大，Ave 不可靠，须重测后方可引用**。 —— 支撑页：[[Rewet Test（回渗测试）]]

## 关联页面

- 概念：[[COCO芯体平台]]、[[Rewet Test（回渗测试）]]、表面残液 Surface Moisture（指标定义见 [[Rewet Test（回渗测试）]]）、[[Cradle Intake Test（Cradle 摄入测试）]]
- 对比：[[COCO V6 Liner 方案对比（Code 1 vs Code 2-A vs Code 2-B）]]
- 项目：[[IPC BCC OI Portfolio（开放创新项目组合）]]

> 📌 **跨代对照提示**：本页为 **COCO V2（2019-11）** 数据，与库内 **COCO V6（2026-08/09）** 系列页面相隔约 7 年。两者**不可直接数值比较**（测试协议、原料供应商、产线均已变更），仅可作为**结构演进脉络**引用：V2 已确立「LSN + LSS / REL / PSS + PSN」的**双 SAP 层夹 REL** 架构，且已使用**上下层 SAP 不对称分配**（M 码 6/4）。

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Products/T5 Pants COCO V2 with trial on TD34 Results Summary - 20191112.pptx.md`
- 原文链接：（无）

> ℹ️ 供应商名称（Nanliu / Ouli / Hezhong / N-Bond / DY / Sandia）在本库中**尚无独立实体页**；其信息目前**仅登记于本页的层结构表中**。若后续批次中任一供应商被 ≥2 份资料提及，再按规则建实体页。

---
type: concept
title: "Seal Strength Test（端封·侧封强度测试）"
domain: [卫材研发, 测试方法与表征]
status: seed
updated: 2026-09-29
tags: [端封, 侧封, 粘合强度, gf, STM-00078, 胶量, 拉力仪]
aliases: ["端封强度测试", "STM-00078", "End/Side Seal Bond Strength"]
---

# Seal Strength Test（端封·侧封强度测试 / End & Side Seal Bond Strength）

> One-line definition 一句话定义：用拉力仪把**外层（底膜）与体侧层之间的端封 / 侧封**拉开，读取**峰值载荷（gf）**，以此反推**施胶量与粘合强度**是否达标——它是本库多条 gf 峰值法的**母方法**（STM-00078）。
> (Peak-load peel of the end/side seal between outer cover and body-side layer; the gf peak proxies glue add-on and bond strength — the parent method of the gf-peak family.)

## Definition 定义

密封强度测的不是"材料强度"，而是**界面结合强度**：外层与体侧层通过热熔胶/热压在端部与侧部形成封合，封合太弱会开胶漏液，太强则浪费胶量与手感变硬。因为断裂是瞬时事件，本方法**读峰值（gf）而非平台值**。

在本库中该方法有**双重身份**：
1. **独立判据**：直接判定端封/侧封的胶量与粘合是否合格；
2. **母方法**：[[STM-01086 BCC Pants 产品拉断测试（Pants 产品拉断测试方法）.doc]] 与 [[Topical liner Supporting layer Embossing pressure.pdf]]（WI-57507）**均直接复用 STM-00078 的程序**并只改夹具/速度——因此三条方法构成同一 **gf 峰值法族**，但**夹具距离与对象不同，不可混为一条**。

## Mechanism 机理拆解

1. **制样可复现性决定读数**：产品须挂在灯箱上、以 **1000 g 双配重夹**把腰部松紧带**完全拉平**，再用 **P.O11946994 模块**定位端封边并量取 **3 in × 100 mm** 区域——**松紧带未拉平会使密封边歪斜，读数系统性偏低**。
2. **去绒毛但不破坏密封边**：剪样后须轻轻去除绒毛，任何对密封边的损伤都会直接污染结果。
3. **分离位置须居中**：外层与体侧层的分离边缘应位于上下夹具中心，出现滑动即判无效并重新取样。
4. **夹具气压是隐形变量**：气压 **≤ 0.6 MPa**，超限会压溃试样、不足则打滑。
5. **派生方法改的是"尺子"不是"原理"**：Pants 拉断把夹具距离从 2 in 改成 3 in、速度提到 1000 ± 10 mm/min；面层压纹沿用 2 in 但增加 **23 ± 1 ℃ / 50 ± 2% RH** 恒温恒湿要求。

## Key Parameters 关键参数表

| 参数 Parameter | 端封·侧封 STM-00078 | Pants 拉断 STM-01086 | 面层压纹 WI-57507 | 出处 Source |
|---|---|---|---|---|
| 界面 Interface | 外层 ↔ 体侧层（端封/侧封） | 腰围（快速上提） | 3D 面层 ↔ 支持层（压纹） | [[STM-00078 端封强度.doc]]、[[STM-01086 BCC Pants 产品拉断测试（Pants 产品拉断测试方法）.doc]]、[[Topical liner Supporting layer Embossing pressure.pdf]] |
| 程序 Programme | **STM5599-1** | 由 STM-00078 改参数 | **STM-00078** | 同上 |
| 夹具距离 Gauge | **2 in** | **3 in** | **2 in** | 同上 |
| 拉伸速度 Speed | 未明示（继承 STM5599-1）`[待验证]` | **1000 ± 10 mm/min** | 未明示（继承 STM-00078）`[待验证]` | 同上 |
| 夹具气压 Clamp pressure | **≤ 0.6 MPa** | **≤ 0.6 MPa** | **≤ 0.6 MPa** | 同上 |
| 预拉伸 / 定位 Preload | **1000 g 双配重夹** + P.O11946994 模块 | 自 Insert 边缘下量 **2 in** | Pad 前端 50 mm / 150 mm 标记 | 同上 |
| 试样 Specimen | **3 in × 100 mm** | **3 in 宽 × ≥100 mm** | **100 mm × 15 mm（CD）** | 同上 |
| 环境 Conditioning | 未明示 | 未明示 | **23.0 ± 1.0 ℃ / 50.0 ± 2.0% RH** | [[Topical liner Supporting layer Embossing pressure.pdf]] |
| 读数 Readout | 峰值 **gf** | 峰值 **gf** | 峰值 **gf** | 三份同源 |
| 合格阈值 Threshold | 原文未给 `[待验证]` | 研究页给 2800 gf 内控 / 3500 ± 1000 gf 推荐 | 原文未给 `[待验证]` | [[BCC Pants Waist Break Study（Pants 产品拉断研究与两项新方法创建）]] |

> ⚠️ **禁止无来源参数**：表中数值均来自上列 SOP；四份 SOP 均未给出各自合格阈值，标 `[待验证]`，引用前须与产品内控标准配对。

## 追加：腰封剪切模拟 STM-00090（2026-09-29 追加，不改动上方既有结论）

> 本节为 **Areas / Test Method 批次 06** 编译时的追加记录。上方「gf 峰值法族」结论**未被修改**，本节补入**第四条成员**——它把同一族方法从"剥离/拉伸"扩展到**剪切模式**。

| 参数 Parameter | 数值 / 口径 Value | 出处 Source |
|---|---|---|
| 方法编号 Method ID | **STM-00090**（第 5 版） | [[STM-00090 腰围密封强度.doc]] |
| 力学模式 Mode | **腰封的剪切模拟（shear simulation）** | 同上 |
| 对象 Object | **腰围密封（腰封）热封边** | 同上 |
| 夹具气压 Clamp pressure | **90 psi** | 同上 |
| 计量长度 Gauge | **50 mm（2 in）** | 同上 |
| 定位辅具 Alignment aid | 上下夹面右边缘贴 **1 in 胶带**，样品右缘对齐 | 同上 |
| 装样 Orientation | **外层面向操作者**；**热封边位于夹面中心** | 同上 |
| 剪裁 Cutting | 距腰围上边缘 **1 in** 沿 CD；MD 沿吸收体边缘（距热封边约 **2 in**） | 同上 |
| 读数 Readout | **峰值荷载 + 平均值**，精确 **0.1 gf** | 同上 |
| 拉伸速度 Speed | 原文未给（由软件模板定义）`[待验证]` | 同上 |

> ⚠️ **口径差异（2026-09-29）**：STM-00090 的**夹具气压写成 90 psi**，而同族 STM-00078 / STM-01086 / WI-57507 写 **≤ 0.6 MPa（≈87 psi）**——**单位体系不统一是跨文件引用最易出错之处**；且本方法**同时记录峰值与平均值、精度 0.1 gf**，与同族"只读整数 gf 峰值"不同。
> ⚠️ **为什么腰封要用剪切而非剥离（2026-09-29）**：腰封在穿着中的失效以**层间剪切滑移**为主，故本方法把热封边置于夹面中心做**剪切模拟**——**与端封（剥离）的受力状态不同，两者的 gf 值不构成同一趋势序列**。

## 相邻概念

- 同族方法：[[Product Waist Break Test（产品腰围拉断测试）]]、[[Liner-Surge Embossing（面层-导流层压花）]]、[[Peel Test STM-00438（剥离强度测试）]]
- 上游对象：[[Polyolefin Hot Melt Adhesive（聚烯烃热熔胶）]]、[[Ultra-Low Add-On Adhesive Application（超低添加量施胶）]]
- 体系归属：[[芯体测试方法与验收基准（STM）]]
- 对比：[[峰值 gf 粘合强度方法族对比（端封 vs Pants 拉断 vs 面层压纹）]]

## 经验教训

> ✅ 验证（2026-09-29，来源 [[STM-00078 端封强度.doc]]）：本方法第 6 版（2021-08-24）在厂内被两条新方法复用，**说明"改参数派生"是厂内新建方法的标准路径**——新建方法应先找母方法再改参数，便于跨产品可比。

## 来源

- [[STM-00078 端封强度.doc]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-00078 端封强度.doc.md`
- [[STM-01086 BCC Pants 产品拉断测试（Pants 产品拉断测试方法）.doc]] —— `RAW/…/成品/Pants 产品拉断测试方法/STM-01086 BCC Pants 产品拉断测试.doc.md`
- [[Topical liner Supporting layer Embossing pressure.pdf]] —— `RAW/…/成品/NJ/Topical liner Supporting layer Embossing pressure.pdf.md`

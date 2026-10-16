---
type: concept
title: "Blizzard Core（Blizzard 芯体结构）"
domain: [卫材研发, 芯体与吸收]
status: growing
updated: 2026-09-29
tags: [Blizzard, 无绒毛浆芯体, fluffless, SAM, 芯体胶, 全包裹, 回渗, 高吸水树脂]
---

# Blizzard Core（Blizzard 芯体结构）

> One-line definition 一句话定义：一种**全包裹、以 SAM（高吸水树脂）为主体、用胶黏剂稳定的薄型无绒毛浆吸收芯体构造**——即 ActiveTech 平台所产出的芯体形态；其关键不是「去掉绒毛浆」，而是用 **SAP 分布 + 胶黏 + 包裹构造**替代绒毛浆原本承担的结构角色。（中文：Blizzard = 构造；平台是 [[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]。）

## Mechanism / Structure 机理 / 结构拆解

1. **What fluff actually does in a conventional core 绒毛浆在传统芯体里的真实作用**：fluff pulp provides **capillary wicking and temporary void volume**，supporting rapid initial fluid intake **before the SAM swells and immobilises the fluid**。So the fluff is a *timing* device, not only a bulking agent。（中文：绒毛浆是「SAM 膨胀前那几秒」的通道与空间提供者——是时间装置，不只是填充物。）
2. **The three-layer stack 三层叠构**：top facing / wrap → **SAM + adhesive layer** → bottom facing / wrap。SAM = primary absorbent and fluid-locking component；adhesive = immobilises SAM + supports pad integrity；full wrap = contains the absorbent layer, limits particle migration, maintains thin-core geometry。
3. **The substitution is deliberate, not subtractive 替代是刻意设计而非简单删除**：Blizzard replaces fluff's structural role through **deliberate control of SAP distribution, adhesive bonding, and wrap/facing construction**。原文的关键句是：Blizzard「不是简单地去浆芯体」。
4. **Adhesive add-on is a two-sided control 胶用量是双侧约束**：one cited configuration uses adhesive at approximately **5 % of SAM weight**；too little risks poor integrity，**too much reduces accessible void volume and slows intake**。（中文：过少损整体性，过多损可及空隙体积与摄入速度——与 [[SAP错峰膨胀]] 的空隙体积逻辑同源。）
5. **Where the load goes after de-fluffing 去浆后负荷的转移路径**：SAM、adhesive、facings、wrap construction 都必须**承担更多流体管理负荷**——这也解释了为什么无浆路线的失败模式集中在「摄入速度」与「防漏」，而不是容量。
6. **Measured trade-off 实测量化权衡**（成人护理 ROTC HBC 对照）：thickness **5.5 mm → 4.4 mm**、high-pressure rewet **2.67 g → 0.40 g**，retention capacity 维持约 **700 g**，但 **third intake 变慢**；婴儿护理 ROTC Slim：厚度与回渗如期改善，但 **cradle intake 变慢、漏尿趋势上升** —— 故 ROTC 2.0 保留 **pad channel 混合构型**。
7. **The engineering lesson 工程读法**：无浆的价值在 **薄、柔、结构稳固**；代价在**摄入动力学与防漏裕度**。因此「保留一部分绒毛浆 + 导流槽」不是退步，而是把芯体变成**分区结构**（见 [[分区密度设计]]、[[ADL（导流层）]]）。

## Key Parameter Table 关键参数表

| Parameter 参数 | Typical value / range 典型值 / 范围 | Source 出处 |
|---|---|---|
| Stack 叠层 | top facing/wrap → SAM + adhesive → bottom facing/wrap | [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]] |
| SAM content SAM 占比 | 100 % SAM（fully wrapped fluffless construction） | 同上 |
| Adhesive add-on 胶用量 | ≈ 5 % of SAM weight（one cited configuration） | 同上 |
| Fluff's replaced functions 被替代的绒毛浆功能 | capillary wicking + temporary void volume | 同上 |
| Thickness (adult ROTC HBC) 厚度 | 5.5 mm → 4.4 mm（−20 %） | 同上 |
| High-pressure rewet 高压回渗 | 2.67 g → 0.40 g（−85 %） | 同上 |
| Retention capacity 保液容量 | ≈ 700 g（基本维持） | 同上 |
| Intake penalty 摄入代价 | 第三次摄入变慢（adult HBC）；cradle intake 变慢（baby Slim） | 同上 |
| Leakage trend 漏尿趋势 | baby ROTC Slim 下 trended upward | 同上 |
| Mitigation adopted 采用的缓解 | hybrid architecture with pad channels（ROTC 2.0） | 同上 |
| Cost 成本 | **来源未提供** | `[待验证]` |

> ⚠️ **No unsourced parameters 禁止无来源参数**：上表数值来自源文所引**内部测试**（成人 HBC 一组、婴儿 Slim 一组），**未标样本量、测试方法与置信区间**；本库暂无标准方法交叉核验（对照 [[芯体测试方法与验收基准（STM）]]），标 `[待验证]`。**本页来源完全没有成本与供应商数据**，不得外推。

## Adjacent Concepts 相邻概念

- 平台与产品 平台与产品：[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]、[[ROTC（Real Online ThinTech Core）]]
- 被替代的材料 被替代的材料：[[绒毛浆（Fluff Pulp）]]
- 吸收剂本体 吸收剂本体：[[SAP性能指标（CRC AUL GBP Vortex）]]、[[SAP错峰膨胀]]、[[BNC 基 SAP 表面交联]]
- 相邻结构设计 相邻结构设计：[[分区密度设计]]、[[ADL（导流层）]]、[[亲水-疏水梯度设计]]、[[毛细梯度设计]]、[[芯体测试方法与验收基准（STM）]]
- 库内既有芯体平台 库内既有芯体平台：[[COCO芯体平台]]、[[TBCW结构]]

## Lessons Learned 经验教训

> ✅ Verification（2026-09-29，source [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]]）：本页与库内既有的**「空隙体积不可让步」**判断相互印证——CoPET/ADL 侧的经验是「厚度损失 ≥8% 时干爽收益归零」（见 [[ADL（导流层）]]），而 Blizzard 侧给出的是一组**相反方向**的实测：厚度与回渗同时改善、代价落在**摄入速度**上。二者共同指向同一结论：**无浆/薄型化的胜负点不在容量，而在动力学（摄入/导流）与空隙体积。**（中文：本页结论与库内既有空隙体积论证一致，但不构成矛盾——一个说「不得靠压缩空隙换干爽」，一个说「靠去浆+胶+包裹换薄度，代价记在摄入上」。）

- **Lesson 1（去浆要先补绒毛浆的两个功能）**：毛细导液与临时空隙体积。任何 fluffless 方案都要显式回答这两件事由谁承担——SAM 分布、胶、包裹构造、还是 pad channel。
- **Lesson 2（胶用量是双侧约束，不是越多越好）**：≈5 % of SAM weight 的配置说明胶在「整体性」与「空隙体积/摄入速度」之间权衡；调胶必须同时看回渗与摄入两个指标。
- **Lesson 3（回渗与摄入不是同一根杠杆）**：实测显示高压回渗大幅改善（2.67 → 0.40 g）而第三次摄入变慢——**验收不能只看回渗**，否则会把「吸得住但吸得慢」误判为全面升级。
- **Lesson 4（混合构型是工程解）**：婴儿形态下漏尿趋势上升 → 保留带导流槽的混合构型。这与本库「分区设计优于单参数优化」的一贯判断一致（[[分区密度设计]]）。
- **待补 `[待验证]`**：Blizzard/ROTC 的**成本与供应链**信息（本批来源完全缺失）；粘接剂类型与添加量对**摄入动力学**的定量曲线；不同 SAP 粒径/GBP 组合在无浆结构中的适配性；无浆结构在**持续坐压下的塌缩与回弹**行为。

## Sources 来源

- [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Active Hygiene/blizzard_activetech_explained.md.md`
- 源文引用的内部资料：ROTC Operations Training；YK Absorbent Core_Global ActiveTech Forum_May 2024；ROTC HBC POV_Mar.2026

## Related Sources 关联来源

- [[ActivTech Spring Portfolio 2026（ActivTech 春季组合评审）]]
- [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]]
- [[High-Speed Core Forming Machine & SAP Dosing Design Review（录音纪要 2026-09-03 14-39）]]
- [[Online Core Competition & COCO V6 Strategy Workshop（在线新品竞争与策略）]]
- [[STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）]]
- [[__一句话：ActiveTech 是平台_工艺能力，Bliz]]

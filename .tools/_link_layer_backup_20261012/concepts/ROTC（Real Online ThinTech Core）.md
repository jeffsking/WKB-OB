---
type: concept
title: "ROTC（Real Online ThinTech Core）"
domain: [卫材研发, 芯体与吸收]
status: growing
updated: 2026-09-29
tags: [ROTC, ROTC Slim, ROTC HBC, 混合芯体, pad channel, 回渗, 摄入速度, 薄芯体]
---

# ROTC（Real Online ThinTech Core）

> One-line definition 一句话定义：**Real Online ThinTech Core**——把 [[ActiveTech Platform（ActiveTech 在线薄芯体平台）]] 的在线薄芯体能力落成产品的**产品实现**，分 **ROTC Slim / Fluffless**（近乎全无浆，追极致薄度与柔性）与 **ROTC HBC（Hybrid Core，混合芯体）**（底层 100 % fast-SAM + 上层 SAM/绒毛浆 + pad channel）两种构型。（中文：ROTC 是产品形态，不是工艺；HBC 是「薄度与裕度」之间的折中。）

## Mechanism / Structure 机理 / 结构拆解

1. **Two configurations, one trade-off 两种构型、一个权衡**：**ROTC Slim / Fluffless** = an all- or nearly all-fluffless core designed for **maximum thinness and flexibility**；**ROTC HBC (Hybrid Core)** = a **bottom 100 % fast-SAM ROTC layer** combined with a **SAM/fluff top layer and pad channel**，which **restores capacity and fluid-handling margin while retaining much of the thin-core benefit**。（中文：Slim 追薄度；HBC 用底层快吸 SAM + 上层含浆层 + 导流槽把容量与液体管理裕度加回来。）
2. **Why the hybrid is needed 为什么需要混合构型**：纯无浆路线的两个实测代价——**第三次摄入变慢**（成人）与 **cradle intake 变慢 + 漏尿趋势上升**（婴儿）——直接指向「初期摄入与防漏裕度」不足，而 pad channel 与上层含浆层正是补这一块的结构手段。
3. **The adult-care evidence 成人护理对照数据**：ROTC HBC 使 **thickness 5.5 mm → 4.4 mm**（−20 %）、**high-pressure rewet 2.67 g → 0.40 g**（−85 %），**retention capacity 维持约 700 g**，代价是**第三次摄入变慢**。
4. **The baby-care evidence 婴儿护理对照数据**：ROTC Slim 下**厚度与回渗如期改善**，但**cradle intake 变慢**、**漏尿趋势上升** → 团队**保留带 pad channel 的混合构型**用于 **ROTC 2.0**。
5. **How to read the two datasets together 两组数据合读**：在这两组成人/婴儿实测中，**回渗指标一致改善、摄入指标一致变差**——说明薄芯体的性能指纹是**「干爽 ↔ 速度」的交换**，而不是全面升级。原文的 takeaway 即为此：难点是保住 intake speed、fluid distribution 与 leakage protection 而不牺牲薄度。
6. **Design interfaces 设计接口**：pad channel（导流槽）与上层含浆层的存在，使 HBC 事实上是**分区结构**——与 [[分区密度设计]]、[[ADL（导流层）]]、[[毛细梯度设计]] 属同一套设计语汇。
7. **Library positioning 库内定位**：本页是库内**第一种以「薄芯体产品构型」为主体**的页面；与 [[COCO芯体平台]]（试产平台）、[[TBCW结构]]（结构方案）并列，但回答的是「薄到什么程度、用什么构型兜底」。

## Key Parameter Table 关键参数表

| Parameter 参数 | Typical value / range 典型值 / 范围 | Source 出处 |
|---|---|---|
| Definition 定义 | Real Online ThinTech Core（产品实现，非工艺平台） | [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]] |
| Configuration 1 构型 1 | ROTC Slim / Fluffless：all- or nearly all-fluffless，追最大薄度与柔性 | 同上 |
| Configuration 2 构型 2 | ROTC HBC（Hybrid Core）：底层 100 % fast-SAM + 上层 SAM/fluff + pad channel | 同上 |
| Adult HBC · thickness 成人 HBC 厚度 | 5.5 mm → 4.4 mm | 同上（内部实测口径） |
| Adult HBC · high-pressure rewet 高压回渗 | 2.67 g → 0.40 g | 同上 |
| Adult HBC · retention 保液容量 | ≈ 700 g（基本维持） | 同上 |
| Adult HBC · intake 摄入 | 第三次摄入变慢 | 同上 |
| Baby Slim · outcome 婴儿 Slim 结果 | 厚度与回渗改善；cradle intake 变慢；漏尿趋势上升 | 同上 |
| Decided mitigation 采取的缓解 | ROTC 2.0 保留 hybrid architecture + pad channel | 同上 |
| SAP type in HBC bottom layer 底层 SAM 类型 | **100 % fast-SAM**（快吸型） | 同上 |
| Cost 成本 | **来源未提供** | `[待验证]` |
| Supplier / line 供应方与产线 | **来源未提供** | `[待验证]` |

> ⚠️ **No unsourced parameters 禁止无来源参数**：两组实测值均为**内部测试口径**，未标样本量、测试方法与判定基准；本库暂无 [[芯体测试方法与验收基准（STM）]] 下的同名指标交叉核验（例如「high-pressure rewet」与 STM 定义的对应关系未确认），标 `[待验证]`。**本页来源完全没有成本与供应方数据。**

## Adjacent Concepts 相邻概念

- 平台与构造 平台与构造：[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]、[[Blizzard Core（Blizzard 芯体结构）]]
- 吸收剂与材料 吸收剂与材料：[[SAP性能指标（CRC AUL GBP Vortex）]]、[[SAP错峰膨胀]]、[[绒毛浆（Fluff Pulp）]]
- 结构设计 结构设计：[[分区密度设计]]、[[ADL（导流层）]]、[[毛细梯度设计]]、[[亲水-疏水梯度设计]]
- 验收 验收：[[芯体测试方法与验收基准（STM）]]
- 库内同类平台 库内同类平台：[[COCO芯体平台]]、[[TBCW结构]]

## Lessons Learned 经验教训

> ✅ Verification（2026-09-29，source [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]]）：本页两组实测数据的**方向一致性**（回渗改善、摄入变差）与库内 [[SAP性能指标（CRC AUL GBP Vortex）]] 的「选型逻辑是分工不是排名」互为印证——**不存在单一牌号/单一结构在全部指标上同时领先**，薄芯体的收益必须按指标分账。（中文：无矛盾，属方法论同构。）

- **Lesson 1（薄芯体的收益与代价要分账）**：一组成人数据把「+薄度、+回渗、=容量、−摄入」四件事同时呈现——谈判/立项时应把四项写成一张表，而不是只报回渗与厚度。
- **Lesson 2（发现摄入变差时先加导流槽，再考虑加浆）**：ROTC 2.0 的处置是**保留混合构型 + pad channel**，即在无浆与全浆之间取分区解，而非退回原型。
- **Lesson 3（成人数据不能直接外推到婴儿）**：同一平台在婴儿形态下额外出现**漏尿趋势上升**——这是成人对照中没有的失效模式，说明**使用场景（体位、尿量、活动）会改变薄芯体的风险结构**。
- **Lesson 4（术语口径要先对齐）**：本页「high-pressure rewet」「cradle intake」等指标名称未与库内 STM 方法对齐，跨文档比数前必须先确认口径，否则会把不同方法的数值直接相减。
- **待补 `[待验证]`**：ROTC 与 STM 指标的定义映射；pad channel 的尺寸/排布参数；fast-SAM 的牌号与 CRC/AUL/GBP 指标；成本与线速。

## Sources 来源

- [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Active Hygiene/blizzard_activetech_explained.md.md`
- 源文引用的内部资料（含 ROTC HBC POV_Mar.2026）：见源页

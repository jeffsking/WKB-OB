---
type: source
title: "Blizzard & ActiveTech 技术说明（在线无绒薄芯体平台）"
source_type: 研报
source_path: RAW/ima_sync/个人知识库/WKB/blizzard_activetech_explained.md.md
original_link: ""
date_published: 2026-10-28
date_processed: 2026-10-28
credibility: 中
credibility_note: "英文技术说明稿（4.6k 字符），正文引 3 份 KC 内部 SharePoint 文件（ROTC Operations Training、YK Absorbent Core_Global ActiveTech Forum 2024-05、ROTC HBC POV 2026-03）作为来源，但原件不在库内、不可直读；含成人失禁与 baby-care 两组对比数据，属内部测量口径，未标样本量。"
knowledge_update_status: done
key_claims:
  - "**概念分层关系必须分清：ActiveTech = 制造平台/工艺能力（在线连续成形无绒薄芯）；Blizzard = 由此得到的具体芯体构造（全包裹、100% SAM、胶黏剂稳定的芯）；ROTC = 该平台的产品化实现（Real Online ThinTech Core）** —— 三者不是同义词，工程语境下混用会导致规格书写错对象"
  - "**Blizzard 不是「没有 fluff 的芯体」，而是用「SAP 分布 + 胶黏剂粘接 + 包裹/面层构造」三件事替代 fluff 的结构角色**；典型构型 `Top facing/wrap → SAM + adhesive → Bottom facing/wrap`，引用构型中胶约为 SAM 重量的 **5%**"
  - "**胶黏剂是双刃剑**：过少 → 完整性差、SAP 迁移；过多 → 降低可及 void volume、拖慢 intake。这条直接解释了为何 COCO V6 要把「按位置差异化加胶」当成未决关键项"
  - "**性能权衡的定量证据（成人护理 ROTC HBC 对比）**：厚度 5.5 mm → **4.4 mm**，高压回渗 2.67 g → **0.40 g**，保液量维持约 **700 g**，但**第三次 intake 变慢** —— 薄与回渗改善是拿 intake 速度换的"
  - "**婴儿护理 ROTC Slim 的教训**：薄度与回渗如期改善，但 cradle intake 变慢、尿液渗漏趋势上升 → 团队因此在 ROTC 2.0 保留**带 pad channel 的混合架构**，而非纯无绒"
  - "**ROTC 两构型**：Slim/Fluffless（最大化薄与柔软）vs HBC Hybrid Core（底层 100% fast-SAM + 上层 SAM/fluff + pad channel，找回容量与流体处理余量）；后者是「薄度收益 + 安全边际」的工程折中"
  - "**工艺控制四个关键点**：SAP 计量与分布（容积式给料、可双给料器）｜真空与 web 转移（低绒/无绒结构对真空条件与成形高度敏感）｜D-wrap 折叠与约束（输送与折叠区 SAP 损失/飞散）｜胶选型与上胶量"
pages_linked: ["[[Blizzard Core（Blizzard 芯体结构）]]", "[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]", "[[ROTC（Real Online ThinTech Core）]]", "[[COCO芯体平台]]", "[[Core Wrap（芯体包裹层）]]"]
compile_mode: semantic
---

# Blizzard & ActiveTech 技术说明

## Positioning 一句话定位

The cleanest available statement of **which layer of the stack each term belongs to** — platform (ActiveTech) vs construction (Blizzard) vs product implementation (ROTC) — plus the quantified trade-off that every thin-core program eventually pays.

现有材料里最清楚的一次「术语分层」：平台（ActiveTech）／构造（Blizzard）／产品实现（ROTC）各指什么，以及每一个薄芯体项目最终都要付的那笔**量化权衡账**。

## Three Terms 三个术语的层级关系

| 术语 | 是什么 | 不是什么 |
|---|---|---|
| **ActiveTech** | 制造**平台与工艺能力**：在线连续成形薄型无绒吸收芯 | 不是某一种芯体构造 |
| **Blizzard** | 由该平台得到的**芯体构造**：全包裹、100% SAM、胶黏剂稳定 | 不是「去掉 fluff 的普通芯体」 |
| **ROTC** | Real Online ThinTech Core —— **产品实现**形态 | 不是独立技术路线 |

## Why Leave Conventional Core 为何要离开常规 SAM/fluff 芯

常规芯里 **fluff 提供毛细芯吸与临时 void volume**，支撑 SAM 膨胀前的快速初始 intake。Blizzard 减少或消除 fluff，换来更薄、更柔软、更灵活、完整性更强的吸收垫；**工程代价是**：SAM、胶黏剂、面层与包裹构造必须共同承担原本由 fluff 承担的流体管理负荷。

## Construction 典型构造

```
Top facing / wrap → SAM + adhesive layer → Bottom facing / wrap
```

- **SAM**：主吸收与锁液组分
- **胶黏剂**：固定 SAM、维持垫完整性；引用构型中约为 SAM 重量的 **5%**
- **全包裹**：约束吸收层、限制颗粒迁移、维持薄芯几何

> 关键判断：Blizzard 的价值不是「去 fluff」，而是**能在线上制造出薄、柔软、结构稳健的 SAP/胶芯体**；难的是在不放弃薄度优势的前提下守住 intake 速度、流体分布与防漏。

## Process Controls 四个工艺控制点

| 控制点 | 内容 | 失效后果 |
|---|---|---|
| SAP 计量与分布 | 容积式给料，可双给料器 | 密度不均、局部凝胶阻塞 |
| 真空与 web 转移 | 低绒/无绒结构对真空与成形高度敏感 | 成形塌陷、飞散 |
| D-wrap 折叠与约束 | 输送与折叠区须控 SAP 损失/飞走 | 掉粉、克重偏差 |
| 胶选型与上胶量 | 过少＝完整性差；过多＝可及 void volume 下降、intake 变慢 | 二选一的性能损失 |

## ROTC Configurations 两种构型

| 构型 | 组成 | 适用 |
|---|---|---|
| **ROTC Slim / Fluffless** | 全（或近全）无绒，追求极限薄与柔软 | 薄度优先场景 |
| **ROTC HBC（Hybrid Core）** | 底层 100% fast-SAM ROTC + 上层 SAM/fluff + pad channel | 需保留容量与流体处理余量 |

## Quantified Trade-off 量化权衡

| 对比 | 结果 |
|---|---|
| 成人护理 ROTC HBC | 厚度 **5.5 → 4.4 mm**；高压回渗 **2.67 → 0.40 g**；保液量约 **700 g**（维持）；**第三次 intake 变慢** |
| 婴儿护理 ROTC Slim | 薄度与回渗改善如期；**cradle intake 变慢、渗漏趋势上升** → ROTC 2.0 保留带 channel 的混合架构 |

> 结论性读法：**薄与高压回渗的改善，是用 intake 速度换来的**；纯无绒若材料与结构未优化，会牺牲初始 intake 速度与防漏稳健性。

## Engineering Takeaway 工程结论

Blizzard/ActiveTech 的价值不在于「去掉 fluff」，而在于**在线上制造薄、柔软、结构稳健的 SAP/胶芯体的能力**；难点是在不交出薄度优势的前提下保住 intake 速度、流体分布与防漏。

## Sources 原文所引来源

- ROTC Operations Training（KC SharePoint, pptx）
- YK Absorbent Core_Global ActiveTech Forum_May 2024（KC SharePoint, pptx）
- ROTC HBC POV_Mar.2026（KC SharePoint, pptx）

> 三份原件均不在本库，仅作为本说明的来源线索登记；本页数据取自说明稿转述。

## Linked Pages 关联页面

- 概念：[[Blizzard Core（Blizzard 芯体结构）]]、[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]、[[ROTC（Real Online ThinTech Core）]]、[[COCO芯体平台]]、[[Core Wrap（芯体包裹层）]]

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/blizzard_activetech_explained.md.md`

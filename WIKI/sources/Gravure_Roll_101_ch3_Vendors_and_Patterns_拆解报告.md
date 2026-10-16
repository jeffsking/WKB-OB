---
type: source
title: "Gravure_Roll_101_ch3_Vendors_and_Patterns_拆解报告.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch3_Vendors_and_Patterns_拆解报告.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# Gravure_Roll_101_ch3_Vendors_and_Patterns_拆解报告.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch3_Vendors_and_Patterns_拆解报告.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# Gravure_Roll_101_ch3_Vendors_and_Patterns_拆解报告.md


章节：Ch3 Vendors & Patterns ｜ 覆盖幻灯片：22–28 ｜ 文档：Gravure Roll 101 (KC, Capability Days 2025) ｜ 拆解日期：2026-08-30

# Gravure Roll 101 — Ch3 Vendors & Patterns：学术级章节拆解报告

Source integrity rules applied in this report（本报告遵循的学术诚信规则）
- 每条论断均标注证据来源：SLIDE N（幻灯片文本层）、SLIDE N — SPEAKER NOTES（演讲者备注）、SLIDE N — 图像内容补充（预先从渲染图提取的关键数据）、SLIDE N — 二次读图（本报告直接读取 PPTX 内嵌原图所得）、SLIDE N — 文本层（SmartArt）（本报告从 PPTX 的 ppt/diagrams/data*.xml 中恢复的 SmartArt 文本）。
- 章节内找不到支撑原句的统一标注 [未找到原句]，且不因此编造任何数据。
- 任何由本报告计算得出的数字，统一标注 [本报告推导] 并完整列出算式。
- 非本章内容（Ch1/Ch2/Ch4）引用时显式标注章节归属；一般工程背景显式标注 外部背景，非本章内容。
- 当不同证据源对同一字段给出互相冲突的数值时，本报告并列呈现全部读数并标注 ⚠️，不做单方面取舍。

## ⚠️ 来源校订说明（Read this first — 与既有提取相比的三处重要校正）

本报告在既有章节文件之外，直接读取了 Gravure Roll 101.pptx 内嵌的原始图片与 XML，得到三项既有提取未覆盖或被误读的证据。所有引用均已标注来源类型：

||||
|---|---|---|
|1|SLIDE 22 的「Key Vendors」实为 SmartArt 图形，其文本不在普通形状文本层中，故既有章节文本层为空。真实文本为：Harper - Charlotte, NC / Precision Roll Solutions/IR Engraving - Richmond, VA / Pamarco - Atlanta, GA / Apex - Pittsburgh, PA|SLIDE 22 — 文本层（SmartArt, ppt/diagrams/data2.xml）|证实了 SLIDE 22 — 图像内容补充 的四家名单，且给出了精确拼写（IR Engraving 与 Precision Roll Solutions 为同一实体的两个名称，原文写作 Precision Roll Solutions/IR Engraving）|
|2|SLIDE 28 图纸的 Deep Dot 尺寸、公差与全部点阵尺寸标注：既有 图像内容补充 记为 0.032" × 0.022" ±10%；本报告二次读图（对原图分块 ×2/×3 放大、四个象限独立读取、两次独立复核）一致读得 0.025" × 0.0227" ±5%（635 × 577 μm ±5%，公差区间 0.0237–0.0262" × 0.0216–0.0238"）|SLIDE 28 — 二次读图 vs SLIDE 28 — 图像内容补充|⚠️ 两组读数并列呈现，标注为待澄清。二次读图的数值内部自洽（公差区间与 ±5% 精确吻合、公制换算精确吻合），故本报告倾向于二次读图，但不单方面否定既有提取|
|3|SLIDE 28 图纸的 Shallow Dot 完整规格（既有提取完全缺失）：0.020" × 0.020" ±5%、10,200,000 cubic micrometers (10.2bcm)、上下限与 Test Burn Target、以及 0.033127" / 0.066254" / 0.265015" / 0.148148" 四个点阵尺寸标注、*Always tilt to the right unless requested otherwise.|SLIDE 28 — 二次读图|补充。这是判定「bcm」口径 1000× 矛盾的关键新证据（见 T7）|
|4|SLIDE 27 实为内嵌视频（ppt/media/media1.mp4，5.93 s，1350×1080，含音轨），非图片。逐帧读取后确认：画面为一条在产的 OLU 涂布/印刷工位（上方蓝色背压辊 + 下方深色凹版辊 + 穿过压区的幅材 + 大量干涸乳胶残留），全片无可辨识文字|SLIDE 27 — 二次读图（9 帧逐帧）|既有提取标注 [images: 0]，本报告确认该页介质为视频而非图片，且无文字层|


关于任务书中若干字段的说明（诚信标注）：任务书列举的 HARPERLASER 112x20、128x20、0.070" deep dots spacing、光面 3.050 与 3.0364、0.250" border、独立的 LOCATION 栏、以及「过去几年做过的辊」六条清单、「KC 各厂雕刻商分布表」、"Pictured below is the newest VIVA roll for Beech Island made by Harper" 等字段，经全 deck 全文检索（含文本层、SmartArt XML、全部 38 页图像、内嵌视频逐帧）确认：均不存在于本源材料，相关单元格一律标注 [未找到原句]，并在附录中集中列示。

## 模块 1：核心论点（Core Arguments）

### A1. KC's engraving supply base is four named North-American vendors — and one of the four is already compromised on measurement compatibility



English summary：Ch3 opens the "who can actually make these rolls" question with an explicit list of only four key vendors — Harper (Charlotte, NC), Precision Roll Solutions / IR Engraving (Richmond, VA), Pamarco (Atlanta, GA), Apex (Pittsburgh, PA). The list is not a market overview; it is the entire qualified supply base. Within this closed set, one member (IR Engraving) is later documented as metrologically incompatible with KC (Ch4 SLIDE 34), which mathematically reduces the usable base to three for new-pattern work.

||||
|---|---|---|
|Harper|Charlotte, NC|SLIDE 22 — 文本层（SmartArt）：*"Harper - Charlotte, NC"；SLIDE 22 — 图像内容补充："Harper – Charlotte, NC"*|
|Precision Roll Solutions / IR Engraving|Richmond, VA|SLIDE 22 — 文本层（SmartArt）："Precision Roll Solutions/IR Engraving - Richmond, VA"|
|Pamarco|Atlanta, GA|SLIDE 22 — 文本层（SmartArt）："Pamarco - Atlanta, GA"|
|Apex|Pittsburgh, PA|SLIDE 22 — 文本层（SmartArt）："Apex - Pittsburgh, PA"|


- 支撑依据 1：Ch4 SLIDE 34 — SPEAKER NOTES："Switched to IR Engraving because Jenks had used them for 2 VIVA rolls / Did not measure volume with same tools so none of the data translated" —— 供应商数量（4）与可用供应商数量（3）不是同一个数字。
- 支撑依据 2：Ch4 SLIDE 38 — 文本层（SmartArt, data3.xml）："New vendors are learning with KC as we attempt to get back to healthy gravure roll inventories and look to ignite innovation" —— 说明这 4 家并非成熟稳定供应，而是「正在与 KC 一起学习」。
- 支撑依据 3（[本报告推导]）：Ch3 内部即出现第 5 个雕刻方名称 —— SLIDE 25 的 *"Saueressig – KCP06"*，但它不在 SLIDE 22 的四家名单中。即：「有图案实绩的雕刻方」≥ 5 家，「Key Vendors」= 4 家，两者口径不同，须区分。
### A2. A "pattern" is not artwork on the roll — it is a measurable latex-placement geometry verified by destructive staining



English summary：Ch3 defines a gravure pattern by what it deposits and where, verified chemically: the DRC pattern is documented as a "#1 Printer pattern (VIVA® Towel)" whose physical result is read on a "Stained sample (DuPont Stain #4)" where "Red dots = latex" and "Green = fiber". The pattern is therefore an operational object with three coupled layers: (i) engraved cell geometry on the roll, (ii) transferred latex dots on the sheet, (iii) a stain-based read-out that makes (ii) visible.

- SLIDE 24 — 图像内容补充：*"#1 Printer pattern (VIVA® Towel)，Stained sample (DuPont Stain #4)，Red dots = latex，Green = fiber，尺寸标注 .047"、133°、.1884""*
- SLIDE 24 — 二次读图：尺寸标注精确读得 .0471"（垂直）、.1884"（垂直）、.133°（带角度符号，既有提取记为 133°）
- 支撑依据：Ch4 SLIDE 29 / SLIDE 30 把同一手法用作试车判据（*"Pamarco VIVA Trial #1 DuPont Stain Results"、"Apex VIVA Trial #1 DuPont Stain Results"*，均在 40X Zoom 下与 IR Engraving 的对照辊并排）。即 SLIDE 24 的判据方法在 Ch4 被直接复用为供应商验收方法 —— 图案定义与验收方法在本章是同一套东西。
- 量化推论 [本报告推导]：.1884" ÷ .0471" = 4.000 —— 图案的纵向重复节距恰为单元尺寸的 4 倍，即该 DRC 图案是一个 4×1 的规则阵列（与 SLIDE 28 图纸中 0.148148" = 0.033127" × √20 = 0.033127" × √(4²+2²) 所揭示的「4×2 矢量重复」同构，见 C9）。
### A3. The DRC and OLU process chains are structurally different, which is why one pattern cannot be copied across platforms



English summary：Ch3 documents two distinct process architectures: Marinette DRC (SLIDE 23) is a double-recrepe line with two latex print stations and two recrepe dryers; Jenks & BIL OLU (SLIDE 26) is a print-then-crepe line with a single printer station feeding a single crepe dryer. DRC prints both sides (SLIDE 24 — 二次读图："Engraving to be used on both sides"); OLU prints one side before creping.

|||||
|---|---|---|---|
|成形|Vertical Run → Former → Felt Section → 3-layer H-box 流浆箱 → Yankee Dryer|（图外，未画出）|SLIDE 23 — 图像内容补充|
|印刷站|2 站：Latex Print (Side 1) → After Dryer … （Double ReCrepe = 两次起

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch3_Vendors_and_Patterns_拆解报告.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch3_Vendors_and_Patterns_拆解报告.md.md`
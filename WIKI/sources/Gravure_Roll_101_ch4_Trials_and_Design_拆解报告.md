---
type: source
title: "Gravure_Roll_101_ch4_Trials_and_Design_拆解报告.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch4_Trials_and_Design_拆解报告.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# Gravure_Roll_101_ch4_Trials_and_Design_拆解报告.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch4_Trials_and_Design_拆解报告.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# Gravure_Roll_101_ch4_Trials_and_Design_拆解报告.md



章节：Ch4 Trials & Design ｜ 覆盖幻灯片：29–38 ｜ 文档：Gravure Roll 101 (KC, Capability Days 2025) ｜ 拆解日期：2026-08-30

## 0. Sourcing & Method Notes（来源与方法说明）

Primary sources used for this report

||||
|---|---|---|
|Gravure_Roll_101_ch4_Trials_and_Design.md (text layer + speaker notes)|SLIDE 29–38|Verbatim from PPTX|
|「图像内容补充」block in the same file (pre-extracted by page rendering)|SLIDE 29–38 images|Stated reliable by task owner; used as-is|
|Re-render of uploads/Gravure Roll 101.pptx (LibreOffice → PDF → PNG, 130/260/300 dpi) and model-read of SLIDE 29–38|SLIDE 29–38 images|Added by this report to recover text that exists only inside images (notably SLIDE 38 Summary, SLIDE 36 band table, SLIDE 32 drawing dimensions)|


Why re-rendering was necessary: the SLIDE 38 "Summary" slide carries no text-layer bullets at all — the PPTX text layer contains only the word Summary, with the seven bullets baked into Picture 7. The pre-extracted 「图像内容补充」block states "p38 Summary 七条见正文文本层", which is not correct — the bullets are image-only. This report recovered them by rendering (see Module 3, T5).

Two source discrepancies found and recorded (not silently resolved):

||||||
|---|---|---|---|---|
|D1|SLIDE 34 annotation word|ceramic 'shell'|ceramic "shelf"|Rendered reading used as primary (shelf); shell recorded as the alternate reading. Both refer to the same defect: residual ceramic occluding the engraved cell after laser engraving|
|D2|SLIDE 32 dot-array dimensions|0.02926" / 0.02926" / 0.01463"|0.025926" / 0.051852" / 0.25926" / 0.14493"|Re-read values used; note that 1 / 0.025926² ≈ 1488, which is internally consistent with the drawing's own 1488 DOTS/SQ-IN callout, whereas 1 / 0.02926² ≈ 1168 is not|
|D3|SLIDE 29 control date|—|Control IR Engraving Jenks GR2 – 12/3/25 vs trial Pamarco Trial – 12/3/24|Control dated 1 year after the trial → [本报告标注：疑似笔误，应为 12/3/24]; not used as a factual date|


Verification checks that passed

- SLIDE 36 band widths sum to 13.75 + 11×7 + 13.75 = 104.5" — exactly equal to the 104.5" engraved-area callout on SLIDE 32. This independently validates the 9-band reading.
- SLIDE 32: 3,800,000 µm³/cell × 1488 cells/in² = 5.6544 BCM/in² — a physically plausible OLU gravure volume, cross-checked against Ch3 SLIDE 28's 27.6 BCM VIVA spec (a different, much deeper engraving).
Terms searched across the entire 38-slide deck and NOT found (declared up front; these drive the [未找到原句] marks in Modules 2–3): maintenance (0 hits), refurbish (0), inventory in text layer (0 — appears only inside the SLIDE 38 image), robustness (0), objectives (0), variables (0), defect (0), plugged (0), adhesive (0), cleaning (1 hit, and it is Embossing Cleaning System on Ch1 SLIDE 7 — an embosser-cleaning unit, not roll cleaning).

## 模块1：核心论点（Core Arguments）

### A1 — Every gravure roll trial in this chapter missed the product target; none achieved the 1800 OLU GMT target on first attempt.



"1100 GMT vs 1800 OLU GMT Target" (SLIDE 29, speaker notes)
"1550 GMT vs 1800 OLU GMT Target" (SLIDE 30, speaker notes)

Verifiable support: Two first-round trials (Pamarco VIVA Trial #1, 12/3/24; Apex VIVA Trial #1, 2/12/25) both report a measured GMT below the identical 1800 target. Attainment = 61.1% and 86.1% respectively [本报告推导, T2]. No slide in Ch4 reports a trial that met the GMT target.

### A2 — Gravure roll design is mathematically and practically an iterative loop, not a one-shot specification exercise.



"Gravure roll design is an iterative process" (SLIDE 36)
"Banded gravure rolls can help speed up the iterative process – typically don't produce sellable product – RSR not MSR" (SLIDE 36)

Verifiable support: The iteration is visible at three nested time scales inside Ch4: (i) within one trial — SLIDE 31 shows Apex VIVA Trial #2 "Ran for 24 Hours" with three sequential re-polishes (Re-Polish #1 / #2 / #3); (ii) across trials — VIVA Trial #1 (Pamarco, Apex) → VIVA Trial #2 (Apex); (iii) across vendors and years — SLIDE 34 "VENUS Engraving Journey": Harper → IR Engraving → Pamarco, with Harper needing "9 months to engrave first roll".

### A3 — You can specify only two of the three key engraving parameters (volume, depth, diameter); the third is emergent and must be measured.



"Engraver must have at least 1 degree of freedom. Can only specify 2 from the key engraving parameters of volume, depth, and diameter" (SLIDE 36)
"Same volume from different combinations of diameter vs depth" (SLIDE 36)

Verifiable support: SLIDE 36's band diagram encodes exactly this: 9 bands, only 3 distinct diameters (530 / 560 / 590 µm), only 4 distinct volume targets (5 / 6 / 7 / 8 BCM), and depth as the resulting measured value (31.42 – 43.14 µm). The band roll is a physical design-of-experiments over two locked parameters with one emergent output.

### A4 — Engraving variation translates directly and dramatically into finished-product property variation; therefore vendor capability is product capability.



"Product properties can change dramatically with engraving changes/inconsistencies" (SLIDE 38, bullet 6)
"X and Y direction sheet surface coverage - Key to GMT (Cell diameter)" / "Z direction sheet penetration - Key to VIVA/WypAll Z peel strength (Cell depth)" / "High Z direction penetration can also negatively impact bulk/caliper" (SLIDE 35)

Verifiable support: The causal chain is explicitly stated: cell diameter → GMT, cell depth → Z peel strength, excess depth/penetration → bulk/caliper loss. The 1100 vs 1550 GMT spread between two vendors engraving the same VIVA pattern is the empirical proof of A4.

### A5 — The gravure roll supply base is in a re-qualification phase, and the constraint on KC is inventory health and innovation speed, not just unit cost.



"New vendors are learning with KC as we attempt to get back to healthy gravure roll inventories and look to ignite innovation" (SLIDE 38, bullet 7)
"Engraved with 3 vendors and struggled with engraving consistency and qu

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch4_Trials_and_Design_拆解报告.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch4_Trials_and_Design_拆解报告.md.md`
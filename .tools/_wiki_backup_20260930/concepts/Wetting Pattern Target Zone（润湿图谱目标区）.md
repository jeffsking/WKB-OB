---
type: concept
title: "Wetting Pattern Target Zone（润湿图谱目标区）"
domain: [卫材研发, 吸收系统设计]
status: growing
updated: 2026-09-29
tags: [Target Zone, Wetting Pattern, 成人失禁, X-ray, 设计准则]
---

# Wetting Pattern Target Zone（润湿图谱目标区）

> One-sentence definition: the Single Insult Wetting Pattern (单次排液润湿图谱) defines the **Target Zone (TZ, 目标区)** — the most critical location within the product for absorbent performance — and is a primary input for absorbent system design, material placement, test-method insult location, and cost optimization.（单次排液润湿图谱定义吸收系统的"目标区"，是芯体位置设计、测试加液点与降本评估的关键输入。）

## Mechanism / Structure 机理 / 结构拆解

1. **Two design inputs 设计双输入**：absorbent design criteria depend on (a) single insult loadings（单次排液量） and (b) single insult wetting patterns（润湿图谱位置/尺寸）。Both drift over time with user habits, population changes, and product redesigns（fit、芯体位置、材料、结构变更）。
2. **Measurement chain 测量链**：real-use single-insult study → product returned on mounting board → X-ray imaging → image-analysis program measures WP length / width / area / centroid（几何质心，非质量质心）/ distances from absorbent edges。X-ray replaces ruler-based visual assessment and detects the highest-mass point when anatomical markers are unknown。
3. **Reference datum 基准选择**：for garments（裤型），WP positions must be documented relative to the **product center**（产品中心线），not the absorbent front edge — anatomy is the invariant landmark; edge-based data became invalid whenever rise or absorbent placement changed（历史上加液点目标因此严重偏差）。
4. **Design levers 设计杠杆**：higher % SAM（高吸水树脂占比）→ further spreading, longer WP; narrower crotch width（更窄裆宽）→ longer WP; product size (S/M vs L) shows little impact when absorbent placement is identical relative to the centerline。
5. **Data lifecycle 数据生命周期**：regression models（WP position/size vs insult size）extend data life as loadings change; recommended update cadence = **5 years** per priority product form, plus change triggers on consumer-base or design shifts。

## Key Parameters 关键参数表

| 参数 Parameter | 典型值 / 范围 Value | 出处 Source |
|---|---|---|
| POISE WP length growth since 2000 | +8 to +48 mm | [[R168596_TL-16794_Adult Care Wetting Pattern Fundamentals 2015-2016 New Methodologies and Target Zones.pdf]] |
| Front-area share of WP | 46–63%（"heavily front-loaded" 假设被推翻） | 同上 |
| Image-analysis detection limit | 5–6 g fluid (POISE) | 同上 |
| DEPEND surge phasing change | 60 mm → 30 mm from front absorbent edge | 同上 |
| Moderate (DPU1/DSU1) single insult target | 80 g → 50 g（潜在下调） | 同上 |
| DPU2 female S/M single insult (2015) | 76 g | 同上 |
| DEPEND Moderate overall insult size (n=570) | mean 32.4 g / median 22.5 g / 90% 68.6 g | 同上 |
| Update cadence recommendation | 5 years + change triggers | 同上 |

> ⚠️ All numbers traced to [[R168596_TL-16794_Adult Care Wetting Pattern Fundamentals 2015-2016 New Methodologies and Target Zones.pdf]]（K-C CONFIDENTIAL，2018）。

## Adjacent Concepts 相邻概念

- 上位：[[Dryness Measure System（干爽度量三分）]]、[[ADL（导流层）]]
- 相关方法：[[FIUP Test Method TTM-00643（女性摄入与回渗测试法）]]、[[Acquisition Test STM-00060（导流性能测试）]]、[[Cradle Intake Test（Cradle 摄入测试）]]
- 对比：[[Depend vs Always Discreet Intake System（摄入系统回渗竞品对比）]]

## Experience Notes 经验教训

> ✅ 验证（2026-09-29，来源 [[R168596_TL-16794_Adult Care Wetting Pattern Fundamentals 2015-2016 New Methodologies and Target Zones.pdf]]）：Methodology pitfalls documented — Plexiglas mounting boards interfered with X-ray densitometry (non-uniform basis weight); DEPEND frame-board mounting caused absorbent shifting/voids; off-spec absorbent phasing biased WP results until adjusted. Foam boards identified as lower-cost, X-ray-friendly alternative pending waterproofing.（亚克力板干扰 X 光定量、裤型装板偏移、吸收体相位超规均会污染数据——样本装板与基准校正是 WP 研究的主要踩坑点。）

> ✅ 验证（2026-09-29，来源 [[Relevant Product Measurements.xlsx]]）：上市规格底表与研究结论互相印证——DPU3 surge 位置 15 mm / 长 350 mm（对照研究"surge 前移 60→30 mm"后最新代码进一步前移至 15 mm）；规格表另给出加液点计算基准（女性 95 mm / 男性 200 mm 位于产品中点前方），可用于台架与假人测试加液点设置。⚠️ DPU3 surge 宽度两源不一致（规格表 74 mm vs 研究报告 83 mm），待人工确认。

## Sources 来源

- [[R168596_TL-16794_Adult Care Wetting Pattern Fundamentals 2015-2016 New Methodologies and Target Zones.pdf]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Test Methods/FIUP - TTM-00643/FIUP Research Docs/R168596_TL-16794_Adult Care Wetting Pattern Fundamentals 2015-2016 New Methodologies and Target Zones.pdf.md`

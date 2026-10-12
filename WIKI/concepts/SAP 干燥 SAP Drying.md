---
type: concept
title: "SAP 干燥 SAP Drying"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [sap, drying, tg-window, cross-linking, dry-state-assembly, energy]
---

# SAP 干燥 SAP Drying

> 📌 **Page completed 2026-09-30** from 13 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）。

The vault carries **SAP 干燥** as a **navigational entry point** under *Handbook of Industrial Drying*, in a family with [[纤维干燥 Fiber Drying]]、[[纸浆干燥 Pulp Drying]]、[[干燥角质化 Hornification]]、[[湿迁移 Wet Migration]]、[[机械脱水 Mechanical Dewatering]]（源：[[Handbook of Industrial Drying]]）. **No page defines the SAP drying operation itself** — the substantive content is the drying physics, the Tg window and one line-assembly constraint（见下）。

（中文：本页在库内是《Handbook of Industrial Drying》下的**导航条目**，与纤维干燥/纸浆干燥同族；**无操作定义句**，实质内容为干燥物理、Tg 窗口与一条产线干态装配约束。）

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Drying sub-processes（两个并行子过程） | **external**（heat to evaporate surface moisture）+ **internal**（internal moisture to surface and its evaporation） | [[Industrial Drying Ch1 Principles and Classification]] |
| Constant-rate period | surface evaporation dominates; rate **independent of internal structure** | [[Industrial Drying Ch1 Principles and Classification]] |
| Falling-rate period | internal diffusion / capillarity becomes rate-controlling; **time scales with the square of thickness** | [[Industrial Drying Ch1 Principles and Classification]] |
| Hygiene rule derived from the above | thick / packed hygroscopic beds（fluff in a core）→ falling-rate dominates ⇒ argue for **thin layers / agitation**; thin fast sheets（tissue, nonwoven web）may dry almost entirely in the constant-rate period | [[Industrial Drying Ch1 Principles and Classification]] |
| Bound moisture → dryness floor | bound moisture sets the equilibrium moisture content, hence **the lower limit of achievable dryness for cellulose fluff pulp and SAP** | [[Hygiene Absorption Model]] |
| SAP final-stage drying temperature（工程口径） | **must stay below Tg to avoid over-cross-linking and killing swellability** | [[Industrial Drying Ch41 Drying of Polymers]]（转记于 [[自由体积 Free Volume]]） |
| Devolatilisation（去残单）temperature | usually run **above Tg** so diffusion can proceed | [[Industrial Drying Ch41 Drying of Polymers]]（转记于 [[自由体积 Free Volume]]） |
| Line constraint（产线铁律） | 尿裤为**干态装配**：**SAP 遇水 / 胶水失稳** ⇒ **真空成型必须在 SAP 干燥态完成；先喷胶 → 再落 SAP** | [[87 卫材产线约束常量表（待并入补充行）]] |
| Pulp-drying parallel（角化参照） | over-drying market pulp in the final stage **welds fibres via thermal cross-linking（hornification）**, raising defibration energy and hurting pad integrity | [[Industrial Drying Ch35 Drying of Pulp and Paper]] |
| Energy benchmark, MVR | **134 kJ/kg water** — *"20 times better than the typical adiabatic spray drying"*（p.1086） | [[Industrial Drying Ch46 Energy Aspects]] |
| Energy share, paper sector | **~33%** of sector energy（Table 46.2）；drying removes the least water but is **the most costly step** | [[Industrial Drying Ch46 Energy Aspects]] |

⚠️ **Two red lines about energy numbers（来源自带警示）**：do **not** confuse *"energy efficiency"* with *"drying efficiency"*（Eq 46.6 accounts for exhaust enthalpy）；and mechanical dewatering must come first（源：[[Industrial Drying Ch46 Energy Aspects]]、[[机械脱水 Mechanical Dewatering]]）.

## Method / Mechanism 方法 / 机理

1. **The constant-rate / falling-rate skeleton is the whole design frame.** Drying is governed by two simultaneous subprocesses; once internal transport becomes rate-controlling, **thickness-squared scaling** takes over（源：[[Industrial Drying Ch1 Principles and Classification]]）.
2. **Dryness has a physical floor.** Bound moisture fixes equilibrium moisture content and therefore the achievable dryness of both fluff pulp and SAP; **hot-air convection is the default route for through-drying** of pulp / tissue / nonwoven（源：[[Hygiene Absorption Model]]、[[Industrial Drying Ch1 Principles and Classification]]）.
3. **The SAP drying window is under tension（库内如实记录的矛盾）**：devolatilisation wants **T > Tg** for diffusion, while the SAP engineering rule wants **final-stage T < Tg** to preserve swellability. The vault states the **applicability boundary of the two is not clarified**（源：[[自由体积 Free Volume]]、[[Industrial Drying Ch41 Drying of Polymers]]）.

   > ✅ **裁决（2026-09-30）**：此为**分段工艺窗口关系，非事实矛盾**——两句各自成立的对象与阶段不同。机理上：**前/中段 T > Tg**（聚合物处高弹态，自由体积大、扩散系数高）利于挥发分脱除与快速脱水；**末段降到 T < Tg**（玻璃态"冻结"网络结构）避免高温历史引发网络坍缩/退火与溶胀损失——与第 6 条绒毛浆 hornification 是同一机理方向。所谓"边界"是**按牌号（残余单体/含水率 vs 溶胀保持）经验确定的工艺窗设计参数**，属工程权衡而非待裁事实。原文两句保留，本注记将其降级为"分段关系已澄清，具体窗口值需各 SAP 牌号实测"。
4. **Drying is a structure-forming operation, not simple water removal.** Three routes are named for a hydrogel/aerogel: **(a) capillary-stress**（ambient / hot-air / oven — capillary pressure can pull nanofibres together, raise density, cut swelling or gas permeability）；**(b) sublimation**（freeze-drying — ice templating sets the pore architecture, so freezing rate and direction matter）；**(c) critical-point**（supercritical CO₂）（源：[[Bacterial Cellulose Aerogel Drying（细菌纤维素气凝胶干燥）]]）.
5. **Route selection is not "best route wins"**：freeze-drying **preserves pore structure but does not universally maximise mechanical strength**; **pre-freezing rate is part of the drying process window**; commercial selection must balance **property retention, energy, cost and scalability**（源：[[Effect of Drying Methods on Bacterial Cellulose Aerogel]]）.
6. **The over-drying failure mode is named and quantified in direction.** For pulp it is **hornification** — thermal cross-linking welds fibres, so **high-temperature drying history means collapsed pores and lost swellability**; the source calls this **the single most actionable sentence in the Handbook for fluff-pulp qualification**（源：[[Industrial Drying Ch35 Drying of Pulp and Paper]]）.
7. **Efficiency analogy**：the osmotic route saves energy because it involves **no phase change — no latent heat**, which is stated as the same principle that makes SAP efficient at absorbing liquid water（源：[[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]]）.

## Hygiene Relevance 卫材关联

- **Dry-state assembly is a hard production rule, not a preference**：SAP loses stability with water / glue, so **vacuum forming must be completed with SAP in the dry state**, and the sequence is **glue first, then SAP**（源：[[87 卫材产线约束常量表（待并入补充行）]]）.
- **Drying is the most energy-costly process step** in the paper/nonwoven route even though it removes the least water（源：[[Industrial Drying Ch46 Energy Aspects]]）— directly relevant to core conversion cost.
- **Swelling ceiling is set chemically, and over-drying attacks it**：DS fixes the solubility ceiling and cross-link density fixes the swelling ceiling — both must be tuned jointly（源：[[Cross-linked Cellulose and Its Derivatives]]）；this is the same quantity the "final stage below Tg" rule protects.
- **SAP–saline physics adjacent**：Π = RT·ln a_w and the Donnan osmotic pressure explain why SAP **swells in water but deswells in saline**; network elasticity caps swelling rate / capacity（源：[[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]]）.
- **Sibling vault pages**：[[SAP（高吸水树脂）]]、[[水凝胶脱水干燥工艺族谱]]、[[Hygiene Absorption Model]]。

## Open Questions 待补

- **No SAP-specific drying curve, target moisture, dryer type or residence time** is recorded on any citing page `[待补]`.
- **The Tg-window tension is unresolved**：devolatilisation (T > Tg) vs final-stage swellability protection (T < Tg) — the vault explicitly leaves the boundary open（源：[[自由体积 Free Volume]]）.
- **Body text missing for the three original cited sources**（Handbook of Industrial Drying、Industrial Drying Ch28、Industrial Drying Ch50）in this batch's excerpts（源：[[Hygiene Absorption Model]]）.
- Whether hornification-limited dryness numbers transfer from **market pulp to SAP particles** at all `[待补]`（源：[[Industrial Drying Ch35 Drying of Pulp and Paper]]）.

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]（本页原始 Cited-by 来源）
- [[Industrial Drying Ch1 Principles and Classification]] · [[Industrial Drying Ch35 Drying of Pulp and Paper]] · [[Industrial Drying Ch41 Drying of Polymers]] · [[Industrial Drying Ch46 Energy Aspects]]
- [[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]] · [[Industrial Drying Ch50 Solid-Liquid Separation]]
- [[Hygiene Absorption Model]] · [[自由体积 Free Volume]] · [[干燥角质化 Hornification]] · [[机械脱水 Mechanical Dewatering]]
- [[纤维干燥 Fiber Drying]] · [[纸浆干燥 Pulp Drying]] · [[湿迁移 Wet Migration]]
- [[Bacterial Cellulose Aerogel Drying（细菌纤维素气凝胶干燥）]] · [[Effect of Drying Methods on Bacterial Cellulose Aerogel]] · [[水凝胶脱水干燥工艺族谱]]
- [[SAP（高吸水树脂）]] · [[Cross-linked Cellulose and Its Derivatives]] · [[87 卫材产线约束常量表（待并入补充行）]]

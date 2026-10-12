---
type: source
title: "Industrial Drying Ch27 Drying of Potato, Sweet Potato, and Other Roots"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch27.md.md"
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Two-stage diced-potato drying uses stepped air temperatures: 93–127°C in the first section, 71–105°C in the second section of the first stage, and 55–82°C in the second stage (p.650)"
  - "Storage beyond the convective endpoint requires reduction of moisture to 3–4% (wb), achieved by long-time sorption drying using sorption agents such as calcium oxide (p.650)"
  - "A time-varying square-wave air temperature profile (35°C base, 5°C amplitude, 60-min cycle) reduced overall color change in potato by about 87% (p.655)"
  - "The degree of shrinkage at a low drying temperature (40°C) was greater than at high temperature (70°C) — shrinkage is a residence-time effect (p.656)"
  - "Ginsenoside content may be reduced by over 25% by drying ginseng root using 44°C air instead of 38°C; internal color also darkens with temperature (p.660)"
  - "Osmotic preconcentration (50% sugar + 10% salt, 47°C, 4 h) reduced potato cube moisture from 84 to 60% (wb) before fluidized-bed drying (p.654)"
summary_cn: "薯类根茎干燥章节以质量-速率权衡为主线：分段降温干燥、方波振荡温度可将变色减少约87%、低温干燥反而收缩更大、6°C超温即损失>25%人参皂苷——工程模式（分段/振荡温度程序、预处理锁定质量、渗透预脱水降负荷）可迁移，食品数值常数不可移植。"
tags: ["source/book", "root-drying", "staged-drying", "temperature-profile", "shrinkage", "osmotic-pretreatment", "diffusivity", "monolayer", "color-degradation", "heat-labile-actives"]
tags_zh: ["薯类干燥", "分阶段干燥", "温度程序", "收缩", "渗透预处理", "水分扩散系数", "单分子层水分", "色泽劣变", "热敏活性物", "吸附干燥"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch4 Transport Properties in the Drying of Solids]]", "[[Industrial Drying Ch24 Grain Property Values and Their Measurement]]", "[[Industrial Drying Ch26 Drying of Herbal Medicines and Tea]]", "[[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]]"]
---

# Drying of Potato, Sweet Potato, and Other Roots

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.27, pp.645–662 (Sablani & Mujumdar).

## Chapter Overview 章节概览

Product-specific drying review for starchy/root/bulb food commodities — potato, sweet potato, mushrooms, peanuts, ginseng. Logic: quality-vs-rate trade-off under a two-sided temperature window (too hot destroys structure/colour/actives; too cold prolongs residence, accelerating enzymatic browning and microbial growth). Compiles preprocessing (peeling, blanching, sulfiting, osmotic pretreatment), tabulated physical/thermal properties (moisture diffusivity, activation energy, BET/GAB monolayer — Tables 27.3–27.12), drying methods per product form, and quality outcomes.

> Note: page numbers derived from PDF-page − 21; OCR noise in equations — re-verify D(m,T) constants against print.

## Key Viewpoints 关键观点

### 1. Staged air temperatures inside one dryer 分段变温

> "The temperature of the drying air in the first section of the first stage is in the range 93–127°C, in the second section of first stage 71–105°C, and in the second stage 55–82°C." (p.650)

Plus a final sorption polish: "A further extension of the storage time will require reduction of moisture content to 3–4% (wb), which can be achieved by long-time sorption drying using sorption agents such as calcium oxide." (p.650) — the convective dryer is not the whole moisture story.

### 2. Oscillatory temperature suppresses colour change 方波温度护色

> "square waveform 35°C, amplitude 5°C, peak to valley 10°C, cycle time 60 min, drying time about 300 min... The percentage reduction in overall color change for potato was about 87%." (p.655)

A controlled oscillation — not a fixed setpoint — dramatically slows a degradation pathway by periodically relieving the local thermal dose.

### 3. Shrinkage is a residence-time effect 收缩是驻留时间效应

> "The degree of shrinkage at a low drying temperature (40°C) was greater than at high temperature (70°C)." (p.656)

Dimensional stability is governed by the time-integral of the stress state, not peak temperature alone — counter-intuitive and transferable wherever a dried sheet must hold dimensions.

### 4. Heat-labile actives: steep temperature sensitivity 热敏活性物

> "Typically the roots are dried in conventional dryers using air temperatures of 32 to 38°C." and "The ginsenoside content may be reduced by over 25% by drying the root using 44°C air instead of 38°C. Internal color also darkens with increase in drying air temperature." (p.660)

A 6°C overshoot destroys >25% of the active — the canonical quantitative argument for tight low-temperature control.

### 5. Diffusivity falls with moisture 扩散系数随水分下降

> "D(m,T) = a₀ exp( a₁(1/m − 1/m₀) − a₂(1/T − 1/T₀) )" (p.649, Table 27.4)

Parametric forms capture both moisture and temperature dependence; activation energies cluster 40–52 kJ/mol for potato air-drying. The falling-rate internal-diffusion idiom transfers even though the constants are food-specific.

### 6. Osmotic pretreatment cuts dryer load 渗透预脱水

> "They found that a solution of 50% sugar and 10% salt at 47°C for 4 h was optimum for osmotic preconcentration. The moisture content of potato cubes was reduced from 84 to 60% (wb)." (p.654)

Osmotic pull-out of water before the thermal dryer removes ~30% of total water without thermal input — the pretreatment note whose full physics is Ch.28.

## Research Method 研究方法

Data-compilation + literature review: preprocessing survey; property tabulation (Tables 27.3–27.12); method-per-product catalogue with operating conditions from cited plant/pilot studies; quality assessment (colour, shrinkage/rehydration, nutritional retention — thiamine collapses to 5% in granule processing, p.656–657). No original experiments; quality data are laboratory-scale.

## Strengths and Weaknesses 优劣评估

- Strengths: dense empirical property tables for a biological substrate; makes quality-vs-rate concrete (87% colour saving; >25% ginsenoside loss from 6°C); period-aware energy choice (microwave reserved for the 30→6% finish stage, p.655); treats preprocessing as first-order to final quality.
- Weaknesses: food-specific constants — starch gelatinization (45°C, p.653), enzymatic browning, ginsenosides do not map onto fluff/SAP chemistry; lab-scale quality data with unproven scale-up; osmotic dehydration under-developed here (deferred to Ch.28).

## Hygiene Implication 卫材关联

Relevance: ★★☆☆☆ — substrate is starch-filled, enzyme-active cellular tissue, fundamentally unlike fluff-pulp/SAP polymeric webs; all numeric property constants are non-portable. No hygiene application is invented. What transfers is engineering pattern only:

- Two-sided temperature window for active-loaded webs: treat the 6°C-overshoot → >25%-loss precedent (p.660) as the quantitative argument for setting dryer temperature bands from the active's degradation onset, validated by stability assay.
- Staged cooling inside one dryer (p.650) plus a final low-RH/desiccant conditioning zone to reach the true storage-moisture floor.
- Oscillatory/square-wave temperature programs (p.655) as a control-strategy candidate before assuming a fixed setpoint is optimal for colour- or active-sensitive webs.
- Preprocess to lock quality upstream (p.648) rather than compensating with lower dryer temperature and longer residence.
- Prefer higher-temperature/shorter-residence profiles for dimensionally-critical sheets when the active allows — low-T/long-residence shrinks more (p.656).

## Related Sources 关联来源

- [[Handbook of Industrial Drying]] — Full book index
- [[Industrial Drying Ch4 Transport Properties in the Drying of Solids]] — Effective-diffusivity framework behind the D(m,T) tables
- [[Industrial Drying Ch24 Grain Property Values and Their Measurement]] — EMC/monolayer measurement method
- [[Industrial Drying Ch26 Drying of Herbal Medicines and Tea]] — Sibling two-sided-window logic, ginseng substrate overlap
- [[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]] — Full osmotic-dehydration physics

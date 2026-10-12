---
type: source
title: "Industrial Drying Ch6 Indirect Dryers"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch06.md.md"
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Indirect (contact/conductive) dryers: 'the heating medium … does not come into contact with the product being dried'; heat reaches the wet material mainly by conduction from a heated surface; surface temperatures range from 40°C (freeze drying) to about 300°C (p.135)."
  - "Energy efficiency: 'the typical energy consumption is in the range of 2800–3600 kJ/kg of water evaporated compared to direct dryers, which consume 4000–6000 kJ/kg of water evaporated' (p.136); capex is typically higher due to heat-exchange surfaces."
  - "Design core: Q = UA(T₁ − T₂) (Eq. 6.1) with resistance network 1/U = 1/h_h + 1/h_w + 1/h_f + 1/h_m + 1/h_v (Eq. 6.2); 'there are indeed only two main resistances' — contact resistance and bulk penetration resistance (p.143)."
  - "Typical U values: steam-tube rotary 30–85 W/(m²K) with 70–90% thermal efficiency (p.140); vacuum double-cone ≈35, fouled 5–10 W/(m²K) (p.141); agitated cone ≈60, horizontal paddle ≈50 W/(m²K) (p.142)."
  - "Glass-transition warning: 'Materials that may undergo glass transition over temperature ranges encountered may pose unexpected problems' — plus contact-resistance changes for pasty/lump-forming materials (p.142)."
  - "For hygroscopic materials, bound moisture enters via the sorption-isobar slope: c_p,bed,h = c_p,bed + c_p,L·X_h·(∂X_h/∂T)_p (Eq. 6.32, p.146); sizing integrates 1/drying-rate: A = Ṁ_dry·I for continuous dryers (Eqs 6.35–6.37)."
summary_cn: "间接（接触/传导）干燥机专章——定义与优劣、按物料选型表、五大机族（盘式/蒸汽管转筒/真空双锥/搅拌式等）及基于总传热系数 U 五阻力网络与干燥速率积分的定量设计方法。"
tags: ["source/book", "drying/indirect-dryers", "drying/contact-drying", "drying/heat-transfer", "materials/sap", "energy-efficiency"]
tags_zh: ["来源/书籍", "干燥/间接干燥", "干燥/接触干燥", "干燥/传热", "材料/SAP", "能效"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch3 Basic Process Calculations and Simulations in Drying]]", "[[Industrial Drying Ch4 Transport Properties in the Drying of Solids]]", "[[Industrial Drying Ch5 Spreadsheet-Aided Dryer Design]]", "[[Industrial Drying Ch41 Drying of Polymers]]", "[[Industrial Drying Ch46 Energy Aspects]]"]
---

# Chapter 6 — Indirect Dryers

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.6, pp.135–148. (Authors: Sakamon Devahastin & Arun S. Mujumdar)

## Overview 概述

Chapter 6 opens Part II ("Description of Various Dryer Types") and covers indirect (contact/conductive) dryers — equipment where the heating medium (steam, hot oil, molten salt, electricity) never touches the product; heat reaches the wet solids by conduction through a heated wall (p.135). Relevant when the product must stay in a closed hygienic system, is heat-sensitive or solvent-wet, emissions/fines must be near zero, or highest thermal efficiency is wanted. Contents: definition + advantages/limitations (§6.1), selection tables by feedstock and duty (§6.2, Tables 6.1–6.3), five dryer families (§6.3: tray, steam-tube rotary, rotating-batch-vacuum, agitated, other), and a quantitative design section (§6.4, Eqs 6.1–6.37) built on overall heat-transfer coefficient U and its five resistances.

## Definition 定义

- **Indirect/contact/conductive dryer 间接（接触/传导）干燥机** (p.135): "dryers in which the heating medium (e.g., steam, hot gas, thermal fluids) does not come into contact with the product being dried. Instead, wet material is dried by contact with a heated surface; heat transfer to the wet material is mainly by conduction from this surface." Surface temperature "may range from 40°C (as in freeze drying) to about 300°C."
- **Overall heat-transfer coefficient & resistance network 总传热系数与阻力网络** (p.143): Q = UA(T₁ − T₂) (Eq. 6.1); 1/U = 1/h_h + 1/h_w + 1/h_f + 1/h_m + 1/h_v (Eq. 6.2) — "only two main resistances": the wall↔bed contact resistance and the bulk penetration resistance across the bed.
- **Hygroscopic effective heat capacity 吸湿性有效热容** (p.146, Eq. 6.32): c_p,bed,h = c_p,bed + c_p,L·X_h·(∂X_h/∂T)_p, "where (∂X_h/∂T)_p is the slope of the sorption isobar and X_h is the bound moisture" (Tsotsas & Schlünder, 1987).
- **Drying-rate integral 干燥速率积分** (p.146, Eqs 6.35–6.37): I = ∫ dX/ṁ(X); batch: A·t_dry = M_dry·I; continuous: A = Ṁ_dry·I.
- **Glass transition warning 玻璃化转变警示** (p.142): "Materials that may undergo glass transition over temperature ranges encountered may pose unexpected problems. In addition, significant differences between the heat transfer coefficients as well as thermal contact resistance … may occur for pasty materials and materials that have tendency to form large lumps."

## Key Claims 核心观点

1. **Energy advantage** (p.135–136): "indirect dryers have higher energy efficiency than the direct dryers, because the energy lost through the exhaust gas stream is greatly reduced" — 2800–3600 vs 4000–6000 kJ/kg water evaporated; also "very low emission of fines and particles", easy vapor condensation, easy vacuum operation — "ideal for heat-sensitive materials".
2. **Limitations** (p.136): "limited ability to enhance the drying rates due to their limited availability of the heat transfer areas … Many types of indirect dryers can only be operated in batch mode; hence they have lower production capabilities than direct dryers." Higher capital cost.
3. **Family U values** (p.140–142): steam-tube rotary — L:D 4:1–10:1, steam 4–10 bar, thermal efficiency 70–90%, U = 30–85 W/(m²K); vacuum double-cone U ≈ 35, fouling drops it to 5–10 W/(m²K); agitated cone ≈ 60, horizontal paddle ≈ 50 W/(m²K), "higher values are expected for products that have surface moisture".
4. **Tray dryers for heat-sensitive goods** (p.138–139): trays loaded to ~40 mm depth, ~40 kg wet material/m² (Oakley, 1997); with vacuum, used "extensively for drying heat-sensitive or easily oxidized materials"; "Hygroscopic materials may also be dried completely at temperatures lower than the maximum permissible temperatures."
5. **Rate period dictates choice** (p.147): "During the constant rate period, when heat transfer dominates the drying process, a dryer with a large heating surface is preferred. On the other hand, during the falling rate period when internal resistances control the rate of drying, a dryer that allows a longer residence time … is recommended." Also: high heat-source temperature → minimize residence time (p.137).
6. **Contact resistance spans 100×** (Table 6.6, p.145–146): h_f from 2.8 W/(m²K) (dry solid) to 280 (50% paste) — driven purely by moisture/contact state; conservative design uses the dry, contact-limited value.

## Limitations 局限

- U correlations are particle/bed-centric (Schlünder sphere models); no model for anisotropic fibrous mats (fluff pad, nonwoven web) with partial, evolving wall contact.
- Glass transition is named but not modelled — no Tg-based design rule, safe-ΔT window, or stickiness index.
- Eq. 6.32 requires the sorption-isobar slope (∂X_h/∂T)_p, which is unmeasured for most commercial polymers (per Ch.4).
- Batch-centric; continuous contact dryers for high-rate lines are lightly quantified (Table 6.3 residence times: 0–10 s thin-film to 1–6 h tray).
- OCR noise in source equations (6.3–6.15); verify against print before use [待验证].

## Hygiene Implication 卫材关联

- **SAP 颗粒干燥的首选场景**: SAP 热敏、易起尘，适合密闭、低氧、可溶剂回收的接触干燥 (p.135–136)——选蒸汽管转筒或搅拌桨式，壁温必须低于 SAP 的 Tg 以防颗粒软化粘壁；粘壁后 U 从 ≈35 崩落到 5–10 W/(m²K) (p.141)。
- **玻璃化转变纪律**: 查/测 SAP 与 PP/PE 胶黏剂的 Tg，设定热壁温度留出安全裕量 (p.142)——这是聚合物接触干燥最常见的失败模式；U 关联式假设刚性颗粒，Tg 附近不再适用。
- **能效账**: 2800–3600 vs 4000–6000 kJ/kg (p.136) —— 约 30% 比能耗差是连续吨级 SAP/聚合物碎片产线的 opex 分水岭，可对冲更高的换热面 capex。
- **吸湿耦合不可省略**: SAP/纤维素强结合水 ⇒ 等温线斜率 (∂X_h/∂T)_p 大，Eq. 6.32 的有效热容项显著降低表观干燥速率 —— Ch4 的 GAB 等温线是接触干燥设计的必需输入，而非可选项。
- **按速率段选机型**: SAP 处于降速段（内控）⇒ 选长停留、低壁温的机型（真空双锥、温和桨式），而非大加热面的恒速段机型 (p.147)。
- **对纤维网垫的坦率边界**: 本章 U/h_m 模型不适用于绒毛浆垫/非织造布网的各向异性纤维结构（部分、演变的壁面接触），此类物料仍以热风穿透（Ch2/Ch17 类）为主 —— 本章对卫材的价值集中在 SAP 与聚合物碎料，不应对网垫强行套用。

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch3 Basic Process Calculations and Simulations in Drying]]
- [[Industrial Drying Ch4 Transport Properties in the Drying of Solids]]
- [[Industrial Drying Ch5 Spreadsheet-Aided Dryer Design]]
- [[Industrial Drying Ch41 Drying of Polymers]]
- [[Industrial Drying Ch46 Energy Aspects]]

---
type: source
title: "Industrial Drying Ch24 Grain Property Values and Their Measurement"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch24.md.md"
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "EMC operational definition: a sample of known mass is allowed to reach equilibrium with air at constant RH and temperature; the equilibrium moisture is the EMC, usually created with saturated salt solutions in containers (p.579)"
  - "The sorption EMC is lower than the desorption EMC at the same relative humidity because of the hysteresis phenomenon exhibited by biological materials (p.580)"
  - "The G.A.B. equation has recently been recognized as the most satisfactory theoretical isotherm equation, though its base form does not incorporate temperature effects (p.580–581)"
  - "Thin-layer drying follows M = M_e + (M_i − M_e)·exp(−K·t^N) (Eq 24.5), with K the drying constant and N a fitted coefficient (p.580)"
  - "Moisture contents should be reported on wet basis in percentage and dry basis in decimal fraction, to remove ambiguity (p.578)"
  - "As the moisture content is lowered, the energy required to evaporate water molecules increases — bound water costs more to remove (Eq 24.32, p.589)"
summary_cn: "谷物与油料特性测量章节给出了底物无关的吸湿测量方法学——静态饱和盐法/动态法测 EMC–ERH、五条等温线方程（GAB 最优）、滞后现象、薄层干燥方程 24.5 与 wb/db 规范——正是绒毛浆与 SAP 设定残余水分规格和预测仓储回湿的工具箱。"
tags: ["source/book", "EMC", "ERH", "water-activity", "sorption-isotherm", "GAB", "hysteresis", "thin-layer-drying", "moisture-measurement", "bound-water"]
tags_zh: ["平衡水分", "平衡相对湿度", "水活度", "吸湿等温线", "GAB模型", "滞后现象", "薄层干燥", "水分测量", "结合水", "仓储回湿"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch2 Experimental Techniques in Drying]]", "[[Industrial Drying Ch11 Freeze Drying]]", "[[Industrial Drying Ch33 Drying of Fibrous Materials]]", "[[SAP（高吸水树脂）]]", "[[脱水干燥工艺族谱（一页纸）]]"]
---

# Grain Property Values and Their Measurement

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.24, pp.573–598 (Jayas & Cenkowski).

## Chapter Overview 章节概览

Measurement-and-property handbook for grains and oilseeds: physical (bulk/particle density, porosity, angle of repose, friction), hygroscopic (moisture measurement, EMC, ERH, sorption/desorption, hysteresis, five isotherm equations), thermal (specific heat, conductivity/diffusivity, convective h, latent heat of vaporization, heat of respiration), electrical (dielectric), optical (NIR), and aerodynamic (terminal velocity) properties. The chapter never mentions hygiene products, but its hygroscopic section is substrate-agnostic — it applies to any hydrophilic porous solid, which makes it the strongest method-transfer chapter of the food-crop batch.

> Note: page numbers derived from PDF-page − 21; spot-check against print edition. Table 24.8 isotherm equations are OCR-garbled in the source; Henderson/Chung–Pfost/Halsey forms are [待验证] against print.

## Key Viewpoints 关键观点

### 1. EMC measurement: the static salt method 平衡水分静态盐法

> "In the static method, a sample of known mass is allowed to reach equilibrium with air maintained at a constant relative humidity and temperature. The moisture content of the sample at equilibrium is measured and is defined as the EMC. The constant relative humidity environments are usually created using saturated salt solutions in containers." (p.579)

This is the operational definition of EMC — the residual moisture a material settles at for a given ambient RH/T. Static method takes 1–5 weeks; the dynamic method (0.5–1.0 kg sample, recirculating air, ERH read when RH stabilises) takes 6–12 h (p.579–580).

### 2. Hysteresis: design the spec on the desorption branch 滞后现象

> "The sorption EMC is lower than the desorption EMC at the same relative humidity because of the hysteresis phenomenon that is exhibited by biological materials." (p.580)

A hydrophilic material re-adsorbs water at a higher moisture than it desorbs to at the same RH. A bale dried to a desorption-branch value will creep up on humid warehouse air — the desorption curve is the conservative one for setting the outgoing spec.

### 3. Five isotherm equations; GAB preferred 五条等温线方程

> "The modified Henderson [15,16] and modified Chung–Pfost … equations have been adopted as standard equations by the American Society of Agricultural Engineers... The G.A.B. equation has recently been recognized as the most satisfactory theoretical isotherm equation, but it does not incorporate the effect of temperature on the EMC–ERH relationship." (p.580)

The five models: modified Henderson, modified Chung–Pfost, modified Halsey, modified Oswin, GAB (multilayer BET-type). GAB base form ignores temperature; use the Jayas–Mazza C/T correction for T-dependent specs (p.581). The chapter uses ERH (decimal) — equate a_w = ERH when bridging to water-activity literature.

### 4. Thin-layer equation: exponential approach to EMC 薄层干燥方程

> "M = M_e + (M_i − M_e) exp(−K t^N) (24:5)" (p.580)

Moisture approaches equilibrium exponentially with drying constant K (1/s) and shape coefficient N, both fitted from a single drying curve. The quantitative core for modelling bale/roll conditioning or particle drying kinetics.

### 5. wb/db discipline 湿基/干基规范

> "…it is suggested that the scientific community adopt a convention to report moisture contents on wet basis in percentage and moisture contents on dry basis in decimal fraction." (p.578)

Declare wb% vs db on every residual-moisture spec or QC certificate, or numbers become ambiguous.

### 6. Latent heat rises as moisture falls 结合水更贵

> "To overcome the attractive forces between the adsorbed water molecules and the internal surfaces of grain kernels extra energy is needed... As the moisture content is lowered, there is an increase in the amount of energy required to evaporate the water molecules in seeds." (p.589)

Eq 24.32: h*_fg = h_fg·[1 + a·exp(−b·M)] — the last moisture points dominate energy cost; pairs with staged/lower-temperature finishing.

## Research Method 研究方法

Measurement-methods and property-data compilation under ASAE standards: EMC via static (saturated salts) or dynamic (recirculating air) method (p.579–580); isotherm fitting by nonlinear regression with tabulated constants (Table 24.8–24.9); specific heat via method of mixtures or DSC (p.582–584); thermal conductivity via guarded hot-plate / line-heat-source probe (p.585–587); full List of Symbols (p.598). All tabulated values are grain/oilseed — the method transfers to pulp/SAP, the numbers do not.

## Strengths and Weaknesses 优劣评估

- Strengths: operational EMC/ERH definitions with two measurement protocols; five isotherm equations with constants; thin-layer Eq 24.5; explicit wb/db rule; latent-heat-rise equation with coefficients.
- Weaknesses: all data are grain cultivars — transfer is by method, not value; hysteresis stated qualitatively without a model equation; Table 24.8 OCR-garbled; no a_w terminology (uses ERH).

## Hygiene Implication 卫材关联

Relevance: ★★★★☆ — no hygiene content in the substrate, but the hygroscopic method is directly the toolkit for fluff-pulp and SAP moisture specification; this is genuine transfer, not forced.

- Measure pulp/SAP desorption isotherm by the static salt method (p.579–580): equilibrate over saturated salt solutions at known ERH, weigh at equilibrium, fit GAB → the a_w-vs-moisture curve that sets warehouse RH and the outgoing residual-moisture spec.
- Set spec on the desorption branch and respect hysteresis (p.580): sorption EMC < desorption EMC at equal RH, so re-wetting on humid air creeps toward the higher sorption branch — choose warehouse RH so even the sorption branch stays under the quality limit.
- Model bale/roll/SAP-particle drying with thin-layer Eq 24.5 (p.580): fit K, N from one drying curve, then predict residence time to reach target M_e.
- Enforce the wb% vs db convention (p.578) on every spec and QC certificate.
- Cost the last moisture points via Eq 24.32 latent-heat rise (p.589) — justify staged finishing with a temper hold before low-energy finishing air.

## Related Sources 关联来源

- [[Handbook of Industrial Drying]] — Full book index
- [[Industrial Drying Ch2 Experimental Techniques in Drying]] — Measurement techniques companion
- [[Industrial Drying Ch11 Freeze Drying]] — Bound-water / secondary-drying overlap
- [[Industrial Drying Ch33 Drying of Fibrous Materials]] — FSP and bound/free water in fibres
- [[SAP（高吸水树脂）]] — Residual-moisture spec target material
- [[脱水干燥工艺族谱（一页纸）]] — Drying-process family map

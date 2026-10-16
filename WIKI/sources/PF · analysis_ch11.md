---
type: source
title: "PF · analysis_ch11.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Plastic Films/PF · analysis_ch11.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# PF · analysis_ch11.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Plastic Films/PF · analysis_ch11.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# PF · analysis_ch11.md.md

# Chapter 11 — Physicochemical Criteria for Estimating the Efficiency of Burn Dressings

## 1. Chapter Overview

This chapter (K. Z. Gumargalieva & G. E. Zaikov) develops, for the first time in the book's framing, a quantitative physicochemical basis for judging burn-dressing performance. The authors argue that dressing efficiency cannot be assessed from scattered clinical reports because the underlying physicochemical properties (sorption, penetrability, adhesion) are rarely tabulated. They therefore build a measurement programme — porosity, pore size, surface energy, sorption, air/vapour penetrability, adhesion — and a theoretical model in which the maximal sorption capacity is set by the free volume of the material, calculable from its density. From sorption kinetics, gas/liquid transport equations and an action model (sorption → evaporation → gas transfer), they derive four concrete first-aid dressing criteria: free-volume utilisation ≥0.9, thickness ≥0.5 cm, adhesive strength ≤20 N/m, and open-pore diameter ≤0.5 µm. The chapter is thus a bridge between polymer film/porous-material science and a wound-care application, with extensive tabulated data on cellulose, collagen, polyurethane and polyolefin dressings.

## 2. Key Viewpoints

### Viewpoint 1 — Sorption ceiling equals free volume

- Page: p.285
- Quote: > "Based on theoretical and experimental data, it was found that the maximal sorptional ability of a burn dressing is determined by the free volume of the dressing material calculated from the value of the material density."
- Interpretation: The chapter's central thesis: liquid-holding capacity is a geometric/material property (free volume), not merely a surface effect. This reframes dressing design as a porosity/density optimisation problem — directly transferable to absorbent-core engineering.
### Viewpoint 2 — A dressing must fulfil three coupled functions

- Page: p.290
- Quote: > "(1) Absorb the wound exudate, which contains metabolic products and toxins; (2) Provide optimum water, air and heat exchange between the wound and the atmosphere; (3) Protect the wound from the penetration of microorganisms from the air."
- Interpretation: These three functions (sorb / breathe / barrier) are exactly the functional triad of a diaper or失禁 pad (acquisition–distribution–retention, vapour transmission, leakage/microbe barrier). The chapter operationalises all three with measurable parameters.
### Viewpoint 3 — Polyolefins are near-impermeable to water (great barrier, poor wicking)

- Page: p.299
- Quote: > "Polyethylene (ρ = 0.923) 0.006 298 … Polypropylene 0.007 298 … Polytetrafluoroethylene 0.01 293 … Polyethyleneterephthalate 0.3 303"
- Interpretation: Tabulated water solubility in polymers shows PP/PE ∼0.006–0.007 (10² g/g) versus regenerated cellulose 46 and poly(2-oxyethyl methacrylate) 40. This is the quantitative backbone for choosing a backsheet/barrier film (PE/PET) versus a topsheet/acquisition layer (hydrophilic cellulose/viscose).
### Viewpoint 4 — Wet-state gas penetrability collapses by orders of magnitude

- Page: p.318
- Quote: > "The mass transfer of gases (oxygen and nitrogen) through the dressing is 2-4 orders of magnitude slower with wet samples than with the dry ones in similar conditions."
- Interpretation: Saturation fills pore space and chokes air transport — a direct analogue of the "saturated core = stuffiness" failure mode in hygiene products; barrier/breathability must be specified wet, not dry.
### Viewpoint 5 — Quantitative first-aid efficiency criteria

- Page: p.323–324
- Quote: > "A first-aid burn dressing must use its entire free volume for sorption. This volume must be 0.9 or more of the total volume of the dressing. Dressing thickness must be 0.5 cm or more." … "Average diameter of open (connected) pores must not exceed 5 × 10–7 m (0.5 µm)."
- Interpretation: The authors convert vague "good dressing" requirements into testable numbers — free-volume fraction, thickness, and a 0.5 µm pore-cutoff that physically excludes bacteria. These are directly reusable as absorbent-product design acceptance limits.
### Viewpoint 6 — Adhesion is governed by surface energy and wetting angle

- Page: p.316
- Quote: > "W_a = γ(1 – cos θ)"
- Interpretation: The Dupré–Young work of adhesion shows low-adhesion (atraumatic) removal is achieved by minimising substrate surface tension and controlling the wetting angle — the same lever used to make a non-stick, skin-friendly topsheet.
## 3. Research Method & Data Sources

||||||
|---|---|---|---|---|
|Experimental characterisation|Porosity from density (eq. 11.1) and microscopy (eq. 11.2)|Dressings (collagen, PU, cellulose, metallised)|MIN-10 light microscope|Two independent porosity methods cross-check|
|Sorption|Continuous immersion float device (Fig. 11.3), eq. 11.3 (m = 0.70 h)|C∞ from water/plasma uptake|Horizontal microscope + float cell|Correlation coeff. 0.96 vs. free-volume model|
|Vapour/air penetrability|Desiccator mass-loss (eq. 11.10) & polyethylene-sack airflow (eq. 11.21–11.22)|P_H2O, P_air tables|Desiccator, compressor, manometer|Wet-state measured explicitly|
|Adhesion|Blood/thrombin clot pull-off at 90°|A (mN/m), θ (deg)|Modified clot device (eq. 11.25–11.27)|Thermodynamic W_a model|
|Theory|Diffusion/transport equations (eq. 11.5–11.34)|Derived models|—|Simplifications (Henry's law, cubic-pore model) stated|

Not a pure review: the authors built bespoke devices and present original tables (11.6–11.16).

## 4. Argumentation Process

Premises: (a) dressing efficiency is undefined without physicochemical metrics; (b) exudate is mostly water plus salts/proteins/cells. Evidence chain: measure porosity → define free volume → show C∞ correlates with free volume (r = 0.96, p.302) → derive sorption kinetics (eq. 11.4) → model combined sorption–evaporation–gas-transfer action (§11.6) → observe wet-state penetrability drop (2–4 orders). Conclusion: four numeric criteria. Rhetorical move:

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Plastic Films/PF · analysis_ch11.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Plastic Films/PF · analysis_ch11.md.md`

## 关联页面

- [[PET（聚酯）]]　[[Topsheet（面层）]]　[[Work of Adhesion]]

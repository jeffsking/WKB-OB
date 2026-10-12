---
type: source
title: "Industrial Drying Ch7 Rotary Drying"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch07.md.md"
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Cocurrent flow is used for heat-sensitive materials even for high inlet gas temperature due to the rapid cooling of the gas during initial evaporation of surface moisture (p.149)."
  - "Rotary dryers are classified as direct, indirect–direct, indirect, and special types, based on whether the heating medium is separated from the solids by a metal wall or tube (p.150)."
  - "The total amount of solids contained in the drum is about 10–15% of its volume, which empirically gives the most efficient performance (p.153)."
  - "It is not safe to assume plug flow of the particles in industrial dryers, because only narrowly sized materials were studied; the maximum particle moisture governs acceptability (p.155)."
  - "Heat transfer is expressed via a volumetric coefficient Uₐ: Q = Uₐ·V·(Δt)m (Eq 7.30, p.157), with correlations such as Uₐ ∝ (n−1)·D⁻¹·G^0.46 for 6 flights (Eq 7.33, p.158)."
  - "A degree-of-freedom analysis yields five design variables (T_AC, u, H/V, L/D, n_f/D) with constraints 5% < H/V < 15%, 2 < L/D < 20, 5 < n_f/D < 10 (p.165)."
summary_cn: "转筒干燥章节系统给出气流方向选择（并流保护热敏物料）、抄板设计、10–15%持料率、停留时间与体积传热系数关联式及以单位成本最小化为目标的全套设计模型，是颗粒状SAP等聚合自由流动物料后干燥的能力参照。"
tags: ["source/book", "drying/rotary", "equipment/granular-dryer", "SAP/post-drying", "heat-transfer"]
tags_zh: ["转筒干燥", "热敏物料", "持料率", "停留时间", "体积传热系数"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch1 Principles and Classification]]", "[[Industrial Drying Ch41 Drying of Polymers]]", "[[Industrial Drying Ch46 Energy Aspects]]", "[[Industrial Drying Ch53 Cost Estimation]]"]
---

# Rotary Drying (Ch.7)

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.7, pp.147–168 (Krokida, Marinos-Kouris & Mujumdar).

## Chapter Overview 章节概览

The rotary dryer is a cylindrical, slightly inclined, slowly rotating shell that advances wet granular solids by rotation, slope and head effect while hot gas passes cocurrent or countercurrent to evaporate surface and bound moisture. The chapter's argument runs through five layers: classification by heat-transfer mode, flight design, residence-time models from three particle motions (cascade, kiln action, bouncing), heat/mass-transfer correlations dominated by the volumetric coefficient Uₐ and the Chilton–Colburn analogy, and a full mathematical design model closed by two worked case studies (olive cake, catalyst pellets).

> Note: page numbers are derived from PDF-page − 21 and should be spot-checked against the print edition.

## Key Viewpoints 关键观点

### 1. Cocurrent flow protects heat-sensitive solids 并流保护热敏物料

> "Cocurrent flow is used for heat-sensitive materials even for high inlet gas temperature due to the rapid cooling of the gas during initial evaporation of surface moisture, whereas for other materials countercurrent flow is desirable in order to …" (p.149)

Mechanism: first surface evaporation quenches the hot gas, so the solid never sees the peak gas temperature. A 800–1100 K inlet (p.161) is survivable for heat-sensitive feeds only in cocurrent mode. This is the governing selection rule for SAP granules or cellulose-acetate flake.

### 2. Classification by heating-medium contact 按加热介质接触方式分类

> "Rotary dryers are classified as direct, indirect–direct, indirect, and special types. This classification is based upon the method of heat transfer being direct when heat is added to or removed from the solids by direct exchange between gas and solids, and being indirect when the heating medium is separated from contact with the solids by a metal wall or tube." (p.150)

The direct-heat bare cylinder is "the simplest and most economical" (p.150). Direct heat risks entrainment loss of fines (p.150) — a real concern for dusty superabsorbent powder.

### 3. Polymers and granular chemicals are canonical feeds 聚合物是典型物料

> "Representative materials dried in direct-heat rotary dryers are sand, stone, ilmenite ore, sodium sulfate, sodium chloride, and fluorspar, for which high temperatures are used, cellulose acetate, sodium chloride, styrene, copperas, cast-iron borings, and ammonium sulfate, for which medium temperatures are required, and urea prills, vinyl resins, oxalic acid …" (p.151)

The explicit listing of cellulose acetate, styrene and vinyl resins establishes the rotary dryer as a standard post-treatment unit for polymeric, free-flowing solids.

### 4. Flights and optimal drum loading 抄板与最佳持料率

> "Their purpose is to lift and shower the solid particles through the gas stream promoting intimate contact between wet solids and hot gases." (p.152)

> "The total amount of solids contained in the drum is about 10–15% of its volume. It has been proved empirically that this loading gives the most efficient performance …" (p.153)

Flight geometry: "Radial flights with a 90° lip are used for free-flowing materials and flat radial flights without lip for sticky ones" (p.152); flights are "offset every 0.6–2 m" (p.152). Below optimal fill the dryer is under-utilised; above it material bypasses by kiln action (p.153).

### 5. Residence time: holdup ÷ feed rate, no plug flow 停留时间

> "The average residence time (or, time of passage) tₜ is defined as holdup H divided by the solids feedrate F" (p.154); "it is not safe to assume plug flow of the particles in industrial dryers, because only narrowly sized materials were studied" (p.155).

Because real feeds are wide-size-distributed, "the maximum particle moisture (not the bulk mean) governs acceptability" (p.155). Particle advance mechanisms: cascade D·sin α/tan α (p.156); bouncing contributes ~50% of advance in pilot, ~22% in industrial underloaded drums (p.157).

### 6. Volumetric heat-transfer coefficient and Chilton–Colburn 传热传质

> "Q = Uₐ V (Δt)ₘ (7.30) where Q is the rate of heat transfer … Uₐ is the volumetric heat-transfer coefficient … V is the dryer volume." (p.157)

Miller et al.: Uₐ ∝ (n−1)·D⁻¹·G^0.46 (6 flights) / G^0.60 (12 flights) (Eq 7.33–7.34, p.158); Uₐ ∝ holdup^0.5 and G^0.16 (p.159). Chilton–Colburn: "j_H = j_D = f/2 … j_H = St·Pr^(2/3)" (Eq 7.42–7.43, p.160), valid Pr 0.6–100, Sc 0.6–2500.

### 7. Cost-minimising design model 成本最小化设计模型

> "A degree of freedom analysis suggests that five design variables are available … T_AC, u, H/V, L/D, and n_f/D, where the first and second express the operating conditions and the rest the dryer shape." (p.165)

Constraints: 5% < H/V < 15%, 2 < L/D < 20, 5 < n_f/D < 10 (p.165). Drying kernel: (X−X_SE)/(X₀−X_SE) = exp(−k_M·t) (Eq 7.56, p.164) with k_M = k₀·T₀^k1·Y₀^k2·u₀^k3 (Eq 7.49, p.163). Thermal efficiency ranges: 55–75% (fired) / 30–55% (steam) (p.162, cited in action card).

## Strengths & Weaknesses 优劣评估

- Strengths: the only closed, cost-minimising rotary-dryer design procedure with explicit geometric constraints and two validated case studies; honest scatter reporting (residence-time correlations diverge >100% at 3 m/s, p.157; heat-transfer scale-up "requires caution and experience", p.159).
- Weaknesses: residence-time models built on narrowly sized inorganic tracers (496-µm sand, p.154), unvalidated for polydisperse SAP + fines mixtures; the design model's plug-flow holdup (Eq 7.61) contradicts the authors' own plug-flow warning (p.155); no SAP-specific drying data.

> "the development of a universal model of the rotary dryer, that combines the cascading motion of the particles with the heat and mass transfer, is questionable" (p.168)

## Hygiene Implication 卫材关联

Relevance: ★★★☆☆ — rotary drying is a post-treatment option for granular SAP and polymer flake/pellets, not for webs or fluff mats. It defines the dryer class that post-dries free-flowing granular polymer products (SAP granules, cellulose-acetate flake, PP/polyolefin pellets, vinyl resins):

- Specify cocurrent flow for SAP post-drying: high inlet temperature (up to 800–1100 K, p.161) is quenched at first evaporation (p.149), avoiding thermal degradation / crosslink scission of the polyacrylate network.
- Hold 10–15% drum fill with 90°-lip radial flights for free-flowing feed (p.152–153); verify H/V ∈ [5,15]%, L/D ∈ [4,10] (p.165).
- Close the moisture tail, not the mean: qualify tₜ = H/F against the maximum-particle-moisture criterion (p.155); do not assume plug flow.
- Watch fines entrainment for dusty SAP powder under direct heat (p.150).

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch1 Principles and Classification]]
- [[Industrial Drying Ch41 Drying of Polymers]]
- [[Industrial Drying Ch46 Energy Aspects]]
- [[Industrial Drying Ch53 Cost Estimation]]

---
type: source
title: "Industrial Drying Ch11 Freeze Drying"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch11.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Certain biological materials, pharmaceuticals, and foodstuffs, which may not be heated even to moderate temperatures in ordinary drying, may be freeze-dried; as a rule, freeze drying produces the highest quality food product obtainable by any drying method (p.255)."
  - "However, freeze drying is an expensive form of dehydration for foods because of the slow drying rate and the use of vacuum (p.255)."
  - "The shape of the pores, the pore size distribution, and pore connectivity of the dried layer depend on the ice crystals that formed during the freezing stage; small discontinuous ice crystals limit water-vapor mass transfer (p.258)."
  - "Since water has an inherently higher dielectric loss factor than ice, any localized melting produces a rapid chain reaction, which results in runaway overheating in microwave freeze drying (p.261)."
  - "Fixed costs exceed running costs by 1.5 to 2.5 times; freeze drying can be suitable only for high-value products with specific biological or physicochemical properties (p.270, p.280)."
  - "The secondary drying stage involves removal of water that did not freeze (sorbed or bound water), about 10–35% of the total moisture content (p.259)."
summary_cn: "冷冻干燥章节以三阶段（冻结/一次升华/二次解吸）建立移动边界PDE模型并给出最优控制与成本分析，结论是冷冻干燥因真空+慢速而昂贵（固定成本为运行成本1.5–2.5倍），仅适用于高值热敏生物物料，与大宗卫材生产路径基本无关。"
tags: ["source/book", "drying/freeze", "sublimation", "bound-water", "high-value-actives"]
tags_zh: ["冷冻干燥", "升华", "结合水", "崩塌温度", "高值活性物"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch1 Principles and Classification]]", "[[Industrial Drying Ch8 Fluidized Bed Dryers]]", "[[Industrial Drying Ch10 Industrial Spray Drying Systems]]"]
---

# Freeze Drying (Ch.11)

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.11, pp.255–281 (Liapis & Bruttini).

## Chapter Overview 章节概览

Freeze drying (lyophilization) is vacuum sublimation of a frozen solvent (usually water) from a heat-sensitive material, executed in three stages: freezing, primary drying (sublimation of the frozen solvent), and secondary drying (desorption of bound/sorbed water). The chapter is the most physics- and process-modeling-heavy of the dryer chapters: it builds a full moving-boundary PDE system (Eq 11.2–11.51) for heat and mass transfer through the dried and frozen layers, treats chamber-pressure effects on effective thermal conductivity and pore diffusivity, devotes a long section to optimal-control policies (cyclic vs constant pressure), and closes with costs.

> Note: page numbers derived from PDF-page − 21; spot-check against print edition.

## Key Viewpoints 关键观点

### 1. Freeze drying is for heat-labile, high-value materials 热敏高值物料

> "Certain biological materials, pharmaceuticals, and foodstuffs, which may not be heated even to moderate temperatures in ordinary drying, may be freeze-dried … As a rule, freeze drying produces the highest quality food product obtainable by any drying method." (p.255)

The entire justification is bioactivity/flavor preservation under vacuum at sub-zero product temperatures.

### 2. Intrinsically expensive and slow 昂贵且缓慢

> "However, freeze drying is an expensive form of dehydration for foods because of the slow drying rate and the use of vacuum." (p.255)

"most food products are still dried by conventional means for obvious economic reasons" (p.280).

### 3. Pore structure from freezing dictates drying rate 冻结决定孔结构

> "The shape of the pores, the pore size distribution, and pore connectivity of the porous network of the dried layer … depend on the ice crystals that formed during the freezing stage … If the ice crystals are small and discontinuous, then the mass transfer rate of the water vapor in the dried layer could be limited." (p.258)

Freezing protocol sets the porous matrix and therefore mass-transfer resistance.

### 4. Microwave freeze drying failed industrially 微波冷冻干燥失败

> "In spite of these apparent advantages, the application of microwaves to industrial freeze drying has not been successful … microwave freeze drying is at present only a potential development and is not considered in the following sections of this chapter." (p.260–262)

### 5. Runaway overheating: water out-dissipates ice 介电失控

> "Since water has an inherently higher dielectric loss factor than ice, any localized melting produces a rapid chain reaction, which results in runaway overheating." (p.261)

The dielectric contrast between liquid water and ice is the failure mechanism — a cautionary lesson for any microwave/dielectric drying of wet polymer systems.

### 6. Economics restrict it to high-value products 经济性限制

> "Freeze drying is costly because of the long drying times involved; this factor has hindered the application of the technique to drying of materials in bulk. As a result, fixed costs tend to exceed running costs … fixed costs exceed running costs by 1.5 to 2.5 times." (p.270); "The economics of the process indicate that freeze drying can be suitable for high-value products with specific biological or physicochemical properties." (p.280)

## Key Terms & Process Details 关键术语

- Primary drying: "the frozen solvent is removed by sublimation; this requires that the pressure … be less than or near to the equilibrium vapor pressure of the frozen solvent" (p.257).
- Secondary drying / bound water: removal of non-frozen (sorbed) water, "about 10–35% of the total moisture content" (p.259); this fraction dominates secondary-drying time and final stability.
- Collapse: "if the material has a glass form and if the minimum freezing temperature is exceeded during the primary drying stage, then the phenomenon of collapse can occur" (p.260); T_scorch limits product temperature (p.260).
- Microwave FD trial: theoretically cuts 1-in slab drying from 8.75 h (conductive) to 1.37 h — but cost 10–20× steam, glow discharge at 0.1–5 mmHg, runaway dielectric overheating, and no industrial equipment kill it (p.260–262).
- Optimal control: minimize batch time under T_scorch and melting-temperature constraints; near-optimal constant pressure ≈ cyclic pressure (p.277).

## Strengths & Weaknesses 优劣评估

- Strengths: unmatched model rigor — the primary-drying model predictions "agree well with the experimental freeze drying rate and time data" (p.272–273); honest scope statement (p.280).
- Weaknesses: microwave route dismissed on qualitative grounds; model excludes solid (matrix) diffusion of bound water and assumes a binary water-vapor/inert gas — real multi-solute amorphous systems out of scope (p.272).

## Hygiene Implication 卫材关联

Relevance: ★☆☆☆☆ — plainly low: freeze drying is not a bulk hygiene manufacturing route. SAP, fluff pulp and nonwoven webs have no heat-lability constraint that would justify vacuum sublimation, and the 1.5–2.5× fixed-cost loading (p.270) excludes commodity materials. Remaining genuine connections:

- Do NOT adopt freeze drying for bulk SAP/pulp/web drying — it is reserved for "high-value products with specific biological or physicochemical properties" (p.280, p.270).
- Spray-freeze-dried porous powders (ultra-porous SAP/fragrance carriers) are a premium-only option; spray freeze drying costs 5–10× hot-air spray drying per the chapter's cross-reference to Ch.10 §10.5.4.
- Heed the dielectric runaway warning before any microwave/dielectric piloting of thick wet cores: water's higher dielectric loss than ice caused microwave freeze-drying runaway (p.261) — design dielectric routes with field-uniformity and moisture-control safeguards.
- Bound-water control = shelf life: 10–35% of moisture is sorbed/bound (p.259); set residual-moisture specs against the product's bound-water isotherm even for convective dryers.

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch1 Principles and Classification]]
- [[Industrial Drying Ch8 Fluidized Bed Dryers]]
- [[Industrial Drying Ch10 Industrial Spray Drying Systems]]

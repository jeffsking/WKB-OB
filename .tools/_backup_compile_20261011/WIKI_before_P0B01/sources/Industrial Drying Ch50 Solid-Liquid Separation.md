---
title: "Industrial Drying Ch50: Solid-Liquid Separation"
type: source
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch50.md.md
chapter: 50
book_title: "Handbook of Industrial Drying"
editor: "Arun S. Mujumdar"
author: "Ryuzo Shirato, Tadaaki Iwata"
publisher: "CRC Press"
year: 2014
edition: "4th"
pages: "1181-1199"
lang: "en"
tags: ["source/book", "mechanical-dewatering", "filtration", "expression", "press", "centrifuge", "Ruth-equation", "cake-compressibility", "conditioning", "flocculation", "polyelectrolyte", "pulp", "SAP-slurry", "energy-saving", "press-section", "hydraulic-press"]
tags_zh: ["机械脱水", "过滤", "压榨", "离心", "Ruth方程", "滤饼压缩性", "调理", "絮凝", "聚电解质", "木浆", "SAP浆料", "节能", "压榨段", "液压压"]
domain: "hygiene-materials"
priority: "P0"
relevance_to_rel: "Quantitative anchor for press-section vs dryer-section trade-off. Mechanical dewatering (58 kJ/kg) is 120× cheaper than thermal (7000 kJ/kg). Cake compressibility n: most industrial slurries 0.1–0.8. Expression pressures 0.6–2.5 MPa. Flocculation to enlarge particles = cheapest way to lower residual moisture."
date_published: 2014
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Solid-liquid separation and drying are complementary operations, and the dry-cake cost must be balanced against the dryer's thermal requirement"
  - "Energy gap is the central economic rule: mechanical dewatering ~58 kJ/kg vs convective thermal drying ~7000 kJ/kg"
  - "Ruth filtration equation: for most industrial slurries n lies between 0.1 and 0.8"
  - "Decreased particle size lowers filtration rate and raises cake moisture content, though it can improve washing efficiency"
pages_linked: ["Handbook of Industrial Drying", "Industrial Drying Ch46 Energy Aspects", "Industrial Drying Ch35 Drying of Pulp and Paper", "Industrial Drying Ch34 Drying of Textile Products", "Handbook of Nonwovens", "Hygiene Absorption Model"]
---

# Ch50: Solid-Liquid Separation for Pretreatment of Drying

> **Source:** Shirato, R. & Iwata, T., in Mujumdar (ed.), *Handbook of Industrial Drying*, 4th ed., CRC Press, 2014. Ch.50, pp.1181–1199.

---

## 1. The Central Economic Rule 核心经济规则

> "Solid-liquid separation and drying are **complementary operations** in many industrial fields." (p.1181)

> "It is essential to **balance the additional cost of producing a dry cake against the thermal requirements of dryers**." (p.1183)

**THE single most important sentence for a procurement strategist:** Invest in mechanical dewatering only up to the point where its marginal cost equals the marginal thermal saving in the dryer.

### Energy Comparison 能耗对比

| Method | kJ/kg H₂O | Relative Cost |
|---|---|---|
| **Squeeze/Expression** 挤压/压榨 | **58** | 1× (baseline) |
| **Thermal drying** 热干燥 | **7,000** | **121×** |

---

## 2. Ruth Filtration Equation Ruth过滤方程

$$\alpha = \alpha_0 \cdot p^n \quad \text{(cake compressibility)}$$

| Parameter | Range | Meaning |
|---|---|---|
| **n = 0** | Incompressible cake | Pressure helps linearly |
| **n = 1** | Highly compressible cake | Pressure barely helps |
| **Most slurries** | **0.1–0.8** | Mixed behaviour |

> "For most industrial slurries, n lies between 0.1 and 0.8." (p.1185)

**Procurement rule:** Pressure helps only for incompressible cakes (n≈0). For soft/compressible slurries (n→1) raising pressure barely increases rate.

### Key Filtration Equations 关键过滤方程

| Equation | Type | Application |
|---|---|---|
| **Eq 50.4** | Incompressible cake | Rate independent of pressure |
| **Eq 50.5** | Compressible cake | Rate depends on pressure^((1-n)/(1+2n)) |
| **Eq 50.6** | Constant-pressure filtration | V² ∝ u (time) |

---

## 3. Conditioning & Flocculation 调理与絮凝

> "Decreased particle size results in **lower filtration rates and higher moisture content** of the cake, and sometimes in better washing efficiency." (p.1185)

**Flocculation/conditioning** (polyelectrolytes, pH, temperature) to enlarge particles is the **cheapest way** to lower residual cake moisture before the dryer.

**Hygiene application:** Pulp fines and SAP-slurry handling — flocculation is the first lever.

---

## 4. Equipment Selection by Cake-Formation Rate 按滤饼形成速率选型

| Cake Formation Rate | Equipment Type |
|---|---|
| **Fast** (>1 cm/min, >20% solids) | Continuous vacuum/belt filters |
| **Slow** (<0.1 cm/min, <10% solids) | Pressure filters |
| **Dilute** | Thickening first |

---

## 5. Expression (Pressing) 压榨

> "Expression is the separation of a liquid from a two-phase solid-liquid system by **compression**, due to movement of the retaining wall rather than the pumping of the solid-liquid system into a fixed chamber as in filtration." (p.1197)

### Expression Equipment 压榨设备

| Equipment | Pressure | Application |
|---|---|---|
| **Squeezer** 挤压辊 | Moderate | Nonwoven, fabric |
| **Filter press** 压滤机 | 0.6–2.5 MPa | Pulp, slurry |
| **Membrane press** 膜压滤机 | Two-step: filter + consolidate | Slurry, fine particles |
| **Hydraulic press** 液压压 | High | Final dewatering |

**Key insight:** Expression pressures of 0.6–2.5 MPa and the membrane filter-press (two-step: filter then consolidate) are the mechanical dewatering tools that get cake moisture below what filtration alone achieves — **the last, cheapest water before the dryer**.

---

## 6. National Potential 国家级潜力

> From Ch46 Table 46.6: **Improved dewatering of feedstock** = **4% national potential, High penetration**

**This is the highest-penetration energy saving option** — because it requires no new technology, just better upstream pressing.

---

## 7. Hygiene-Materials Action Cards 卫材应用卡

| Card | Insight | Action | Relevance |
|---|---|---|---|
| **H50-1** | Mechanical dewatering (58 kJ/kg) vs thermal (7000) = 120× saving | Maximize press section capacity before dryer | ⭐⭐⭐⭐⭐ |
| **H50-2** | Flocculation to enlarge particles = cheapest moisture reduction | Use polyelectrolytes for pulp/SAP slurry conditioning | ⭐⭐⭐⭐⭐ |
| **H50-3** | Cake compressibility n: most slurries 0.1–0.8 | Higher-pressure press only helps if n is low | ⭐⭐⭐⭐ |
| **H50-4** | Expression 0.6–2.5 MPa gets cake below filtration limit | Last mechanical water before dryer | ⭐⭐⭐⭐ |
| **H50-5** | 4% national potential, High penetration | Prioritize in plant energy audit | ⭐⭐⭐⭐ |

---

## 8. Related Sources 关联来源

- [[Handbook of Industrial Drying]] — Full book index
- [[Industrial Drying Ch46 Energy Aspects]] — Energy benchmarks
- [[Industrial Drying Ch35 Drying of Pulp and Paper]] — Pulp press section
- [[Industrial Drying Ch34 Drying of Textile Products]] — Nonwoven dewatering
- [[Handbook of Nonwovens]] — Nonwoven forming
- [[Hygiene Absorption Model]] — Absorption simulation

---
title: "Industrial Drying Ch53: Cost Estimation"
type: source
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch53.md.md"
chapter: 53
book_title: "Handbook of Industrial Drying"
editor: "Arun S. Mujumdar"
author: "Janusz Sztabert, Henryk Kudra"
publisher: "CRC Press"
year: 2014
edition: "4th"
pages: "1245-1258"
lang: "en"
tags: ["source/book", "cost-estimation", "FCI", "unit-cost", "Marshall-Swift-index", "capacity-scaling", "installed-cost", "fixed-cost", "variable-cost", "procurement", "benchmarking", "stainless-steel", "titanium", "energy-cost"]
tags_zh: ["成本估算", "固定资产投资", "单位成本", "M&S指数", "容量缩放", "安装成本", "固定成本", "变动成本", "采购", "基准", "不锈钢", "钛", "能源成本"]
domain: "hygiene-materials"
priority: "P0"
relevance_to_rel: "Procurement capstone. Dryer is only one component of a system. Installed cost = 2.25× FOB (carbon steel) or 2.75× (stainless). Material: SS 1.5–1.7×, titanium 2–3× vs carbon steel. Capacity scaling n=0.6: doubling costs 1.52×, not 2×. Worked example: $0.089/kg unit drying cost."
date_published: 2014
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "A dryer is only one component of the whole drying system, which may include preprocessing, conveyors, dust collection, controls and utilities"
  - "Capacity scaling: if n is not given, n = 0.6 can be taken for rough estimation"
  - "Total direct installation cost is roughly 2.25x the equipment FOB cost"
  - "304 stainless construction costs 1.5-1.7x carbon steel, and 2-3x more if built of other alloys"
pages_linked: ["Handbook of Industrial Drying", "Industrial Drying Ch46 Energy Aspects", "Industrial Drying Ch50 Solid-Liquid Separation", "Industrial Drying Ch48 Safety Aspects", "Industrial Drying Ch35 Drying of Pulp and Paper"]
---

# Ch53: Cost Estimation Methods for Drying

> **Source:** Sztabert, J. & Kudra, H., in Mujumdar (ed.), *Handbook of Industrial Drying*, 4th ed., CRC Press, 2014. Ch.53, pp.1245–1258.

---

## 1. The Dryer Is Only One Component 干燥器只是系统的一部分

> "A dryer itself is only one component of the overall drying system. The system may comprise preprocessing equipment (extruders, grinders, mixers, and blenders), feeders, product-discharge devices, and postprocessing equipment such as gas cleaners (cyclones, filters, and scrubbers) and solvent-recovery systems." (p.1247)

**Hygiene implication:** For a hygiene line (coating oven + airlaid former + defibration + abatement), the buyer must cost the **whole battery-limits system** or the estimate is meaningless.

---

## 2. Inflation Correction 通胀修正

$$\frac{\text{Updated cost}}{\text{Original cost}} = \frac{\text{M\&S Index at updated time}}{\text{M\&S Index at time of original cost}} \quad \text{(Eq 53.1)}$$

### M&S Index Table 指数表

| Year | M&S Index |
|---|---|
| 1989 | 895.1 |
| 2004 | 1178.5 |

**Rule:** Any literature/vendor cost in old dollars is useless without index correction.

---

## 3. Capacity Scaling 容量缩放

$$\frac{\text{Predicted cost}}{\text{Original cost}} = \left(\frac{\text{desired capacity}}{\text{original capacity}}\right)^n \quad \text{(Eq 53.2)}$$

> "If not given... n = 0.6 can be taken for rough estimation." (p.1246)

### Key Insight 关键洞察

| Capacity Ratio | Cost Ratio (n=0.6) |
|---|---|
| **2×** | **1.52×** (not 2×) |
| **3×** | **1.93×** |
| **5×** | **2.31×** |

**Buyer's defence:** Against linear "per-tonne scales with size" claims.

### Equipment-Specific n Values 设备特定n值

| Equipment | n |
|---|---|
| Cyclone | 0.61 |
| Cloth collector | 0.78 |
| Roll crusher | 0.97 |
| Venturi scrubber | 0.46 |
| **Default** | **0.6** |

---

## 4. Installed Cost Factors 安装成本系数

| Material | Multiplier |
|---|---|
| **Carbon steel** | **2.25×** FOB |
| **Stainless steel** | **2.75×** FOB |

> "To roughly estimate the total direct cost of the drying installation, it is recommended to multiply the equipment FOB cost by a factor of **2.25** if the equipment is made of carbon steel or by **2.75** if stainless-steel equipment is used." (p.1250)

**Hygiene implication:** Most hygiene lines require stainless → 22% premium on the multiplier alone.

---

## 5. Material of Construction 材料成本

| Material | Cost vs Carbon Steel |
|---|---|
| **304 Stainless steel** | **1.5–1.7×** |
| **Titanium** | **2–3×** |

> "Drying equipment built of 304-stainless steel typically costs from 1.5 to 1.7 times more than that made of carbon steel and 2 to 3 times more if built of titanium." (p.1249)

**Hygiene implication:** Fluff/SAP/coating lines requiring stainless or clad construction → expect 50–70% equipment premium over carbon steel.

---

## 6. Cost Structure 成本结构

### Fixed Costs (% of FCI) 固定成本（占FCI百分比）

| Category | Typical % |
|---|---|
| Depreciation | 5–10% |
| Interest on investment | 2–8% |
| Taxes | 1–5% |
| Maintenance | 3–5% |
| Overhead | 5–10% |

### Variable Costs 变动成本

| Category | Notes |
|---|---|
| **Energy** | Volatile; ±30% typical |
| Raw material | Feedstock |
| Labor | Rules-based |
| Working capital | Inventory |

---

## 7. Worked Example: Fully-Loaded Unit Cost 算例：全负荷单位成本

### Spray Dryer for Laundry Detergent 喷雾干燥器洗衣粉

| Cost Component | Value |
|---|---|
| **Fixed cost** | **$41.09/t** |
| **Variable cost** | **$47.78/t** |
| **Total unit cost** | **$88.87/t = $0.089/kg** |

> "The expected unit cost of drying of the laundry detergent in the year 2006 will most likely be US$41.09/t + US$47.78/t = US$88.87/t = US$0.089/kg." (p.1257)

**Procurement rule:** Demand the same decomposition (fixed + variable, $/t of dry product) from any supplier and compare offers apples-to-apples.

---

## 8. Hygiene-Materials Action Cards 卫材应用卡

| Card | Insight | Action | Relevance |
|---|---|---|---|
| **H53-1** | Installed cost = 2.25× FOB (CS) or 2.75× (SS) | Convert vendor equipment quote to battery-limits cost | ⭐⭐⭐⭐⭐ |
| **H53-2** | Capacity scaling n=0.6: 2× capacity = 1.52× cost | Defence against linear pricing claims | ⭐⭐⭐⭐⭐ |
| **H53-3** | SS 1.5–1.7× vs CS; titanium 2–3× | Spec material based on duty, not default | ⭐⭐⭐⭐⭐ |
| **H53-4** | Worked example: $0.089/kg fully-loaded | Demand same decomposition from suppliers | ⭐⭐⭐⭐⭐ |
| **H53-5** | M&S index correction mandatory | Any old-dollars quote needs inflation update | ⭐⭐⭐⭐ |
| **H53-6** | Dryer is only one component | Cost whole system, not just dryer | ⭐⭐⭐⭐⭐ |

---

## 9. Related Sources 关联来源

- [[Handbook of Industrial Drying]] — Full book index
- [[Industrial Drying Ch46 Energy Aspects]] — Energy → utility cost
- [[Industrial Drying Ch50 Solid-Liquid Separation]] — Lower evaporation → smaller dryer
- [[Industrial Drying Ch48 Safety Aspects]] — Safety equipment cost
- [[Industrial Drying Ch35 Drying of Pulp and Paper]] — Pulp drying costs

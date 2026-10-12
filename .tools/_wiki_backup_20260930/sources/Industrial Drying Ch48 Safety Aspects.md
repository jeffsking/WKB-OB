---
title: "Industrial Drying Ch48: Safety Aspects"
type: source
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch48.md.md"
chapter: 48
book_title: "Handbook of Industrial Drying"
editor: "Arun S. Mujumdar"
author: "Jerzy Markowski, Arun S. Mujumdar"
publisher: "CRC Press"
year: 2014
edition: "4th"
pages: "1131-1157"
lang: "en"
tags: ["source/book", "safety", "fire", "explosion", "dust-explosion", "SAP-powder", "fluff-pulp-dust", "MEC", "MIE", "Kst", "inerting", "venting", "suppression", "ATEX", "static-ignition", "PE-PP", "bag-filter", "housekeeping"]
tags_zh: ["安全", "火灾", "爆炸", "粉尘爆炸", "SAP粉末", "绒毛浆粉尘", "最小爆炸浓度", "最小点火能", "爆炸烈度", "惰化", "泄爆", "抑爆", "ATEX", "静电点火", "PE-PP", "袋式过滤器", "清扫"]
domain: "hygiene-materials"
priority: "P0"
relevance_to_rel: "Direct hazard handbook for fluff-pulp defibration dust and SAP powder. PE MIE 10 mJ, PP MIE 30 mJ — both below 25 mJ spark threshold. Bag filters with synthetic fibres need steel/carbon fibres for conductivity. N₂/CO₂ inerting for solvent-borne coatings. Safety must be built in at design stage."
date_published: 2014
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Drying is a potentially hazardous operation: roughly 8-9% of food-industry dust explosions are related to drying"
  - "Fire/explosion needs three simultaneous conditions: fuel, oxidizer, ignition source"
  - "Most incidents involve spark ignition energies BELOW 25 mJ; the very high resistance of synthetic-fibre bag filters is a major static-discharge hazard"
  - "Safety is far more economical when built in at the design stage than added later"
pages_linked: ["Handbook of Industrial Drying", "Industrial Drying Ch15 Impingement Drying", "Industrial Drying Ch17 Conveyor Dryers", "Industrial Drying Ch40 Drying of Coated Webs", "Industrial Drying Ch53 Cost Estimation"]
---

# Ch48: Safety Aspects of Industrial Dryers

> **Source:** Markowski, J. & Mujumdar, A.S., in Mujumdar (ed.), *Handbook of Industrial Drying*, 4th ed., CRC Press, 2014. Ch.48, pp.1131–1157.

---

## 1. Hazard Baseline 危害基准

> "Drying should be regarded as a potentially hazardous operation... Approximately **8 to 9% of all dust explosions** in the food industry is related to the drying operation... an average of **four major accidents** in spray dryers were reported annually." (p.1131–1132)

**Hygiene implication:** Any hygiene drying step (airlaid oven, coating dryer, SAP spray/flash dryer, fluff defibration) sits in the same risk class as food drying.

---

## 2. Fire Triangle 火三角

> "The simultaneous presence of three basic conditions is required for fire and explosion to occur: 1. **Fuel** (e.g., flammable dusts, solvents) 2. **Oxygen** (air) 3. **Ignition source** with sufficient energy. When any of these three basic conditions is missing, no explosion can occur." (p.1133)

**Safety logic:** Eliminate any one leg — inerting removes O₂, dust-cloud control removes fuel, grounding removes ignition.

---

## 3. Material Classification 物料分类

| Type | Description | Examples | Hygiene Relevance |
|---|---|---|---|
| **Type 1** | Explosive | TNT, picrate | — |
| **Type 2** | Very sensitive | Some metal powders | — |
| **Type 3** | Combustible | **Fluff pulp, SAP, polymer fines** | ⭐⭐⭐⭐⭐ |

> "The drying of solids of type 3 can be safely carried out by proper control of operating conditions and by providing adequate precautionary measures." (p.1134)

**All hygiene materials are Type 3** — not explosives, but combustible dusts requiring control.

---

## 4. Dust Explosion Parameters 粉尘爆炸参数

| Parameter | Description | Key Data |
|---|---|---|
| **MEC** | Minimum Explosive Concentration | Material-specific |
| **MIE** | Minimum Ignition Energy | **PE: 10 mJ; PP: 30 mJ** (Table 48.4) |
| **MIT** | Minimum Ignition Temperature | Material-specific |
| **P_max** | Maximum Explosion Pressure | < 900 kPa at atmospheric |
| **(dP/dt)_max** | Maximum Rate of Pressure Rise | Up to 10 kPa/s |
| **K_st** | Dust Explosion Index | Cube-root law: K_st = (dP/dt)_max · V^(1/3) |

### Critical Ignition Threshold 关键点火阈值

> "The majority of incidents occur with sparks having ignition energy **below 25 mJ**... The extremely high resistance of synthetic fibres used in bag filters may be reduced by adding some **steel or carbon fibres**." (p.1138, p.1147)

**Hygiene implication:** PE MIE 10 mJ and PP MIE 30 mJ are both below the 25 mJ spark threshold. SAP/PP/PE fines and synthetic-fibre filter bags are a static-ignition risk unless grounded with steel/carbon fibres.

---

## 5. Protection Strategies 防护策略

### Prevention 预防

| Strategy | Application |
|---|---|
| **Inerting** (N₂, CO₂, flue gas) | Solvent-borne coatings, fine polymer/SAP powders |
| **Dust-cloud avoidance** | Enclosed systems, proper filtration |
| **Ignition-source exclusion** | Grounding, bonding, ATEX equipment |

### Protection 防护

| Strategy | Application |
|---|---|
| **Venting** | Sized by K_st cube-root law |
| **Suppression** | Chemical suppressants for enclosed spaces |
| **Containment** | Explosion-resistant vessels |
| **Isolation** | Prevention of secondary explosions |

### Thermal Decomposition 热分解

| Parameter | Description |
|---|---|
| **T_A** | Temperature of Self-accelerating Decomposition |
| **T_L** | Limiting Oxygen Concentration |
| **T_B** | Temperature of Burnback |

> "For material with self-heating capabilities collected and stored in the bulk form, the most important data on the self-heating are given by Bowes." (p.1144)

**Design rule:** Operating temperature = T_L − 20°C for dust layers.

---

## 6. Key Design Rules 关键设计规则

> "It is more economical to provide necessary safety measures against a hazard **at the design stage** so that safety can be built into the plant, rather than to 'retrofit' safety equipment, which can be very costly." (p.1156)

> "The **secondary explosion**, usually caused by dust deposition on surrounding surfaces, is always devastating; the importance of good **housekeeping** cannot be overemphasized." (p.1157)

---

## 7. Hygiene-Materials Action Cards 卫材应用卡

| Card | Insight | Action | Relevance |
|---|---|---|---|
| **H48-1** | PE MIE 10 mJ, PP MIE 30 mJ — both below 25 mJ spark threshold | Grounding + bonding for all PE/PP/SAP handling | ⭐⭐⭐⭐⭐ |
| **H48-2** | Synthetic bag filters have very high resistance | Add steel/carbon fibres to bag filters | ⭐⭐⭐⭐⭐ |
| **H48-3** | N₂/CO₂ inerting removes O₂ leg | Use inerting for solvent-borne coating dryers | ⭐⭐⭐⭐⭐ |
| **H48-4** | Safety must be built in at design stage | Include explosion protection in original bid | ⭐⭐⭐⭐⭐ |
| **H48-5** | Secondary dust explosion from deposits is devastating | Daily housekeeping is real defense | ⭐⭐⭐⭐⭐ |
| **H48-6** | K_st cube-root law for vent sizing | Use 1.2-L Hartmann data scaled to real volume | ⭐⭐⭐⭐ |

---

## 8. Related Sources 关联来源

- [[Handbook of Industrial Drying]] — Full book index
- [[Industrial Drying Ch15 Impingement Drying]] — Fire hazard in tissue drying
- [[Industrial Drying Ch17 Conveyor Dryers]] — Combustible dust in conveyor
- [[Industrial Drying Ch40 Drying of Coated Webs]] — LEL, VOC, inerting
- [[Industrial Drying Ch53 Cost Estimation]] — Safety equipment cost

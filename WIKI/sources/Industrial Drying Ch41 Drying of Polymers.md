---
title: "Industrial Drying Ch41: Drying of Polymers"
type: source
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch41.md.md
chapter: 41
book_title: "Handbook of Industrial Drying"
editor: "Arun S. Mujumdar"
author: "Arun S. Mujumdar, Mohammad Hasan"
publisher: "CRC Press"
year: 2014
edition: "4th"
pages: "951-977"
lang: "en"
tags: ["source/book", "polymer-drying", "SAP", "devolatilization", "glass-transition", "residual-monomer", "acrylic-acid", "desiccant-dryer", "hygroscopic-resin", "PP-PE", "PET-nylon", "two-stage-drying", "dew-point", "pellet-drying"]
tags_zh: ["聚合物干燥", "SAP", "脱挥", "玻璃化转变", "残留单体", "丙烯酸", "干燥剂干燥", "吸湿树脂", "PP-PE", "PET-尼龙", "两阶段干燥", "露点", "颗粒干燥"]
domain: "hygiene-materials"
priority: "P0"
relevance_to_rel: "★★★★★ SAP-relevant. Devolatilization performed ABOVE Tg is the mechanism for removing residual acrylic acid/monomer from SAP. Two-stage drying (fast surface + controlled bound). Hygroscopic resins (PET, nylon) hold moisture INSIDE pellet — dew point sets floor. PP/PE nonhygroscopic = surface only."
date_published: 2014
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Most polymers leave the reactor carrying unreacted monomer, solvents, water and/or other volatiles that must be removed"
  - "ABS needs BOTH surface and bound moisture removal, so a two-stage drying system is recommended"
  - "PET, nylon, ABS and PC are hygroscopic resins that collect moisture INSIDE the pellet -- drying by air is insufficient alone"
  - "Devolatilization must be done above the glass transition temperature for effective bound-moisture removal -- directly relevant to SAP / SAP-composite processing"
pages_linked: ["Handbook of Industrial Drying", "Industrial Drying Ch28 Osmotic Dehydration and SAP Physics", "Industrial Drying Ch35 Drying of Pulp and Paper", "Handbook of Nonwovens", "SAP"]
---

# Ch41: Drying of Polymers

> **Source:** Mujumdar, A.S. & Hasan, M., in Mujumdar (ed.), *Handbook of Industrial Drying*, 4th ed., CRC Press, 2014. Ch.41, pp.951–977.

---

## 1. THE SAP Connection 核心SAP关联

### Devolatilization Above Tg 脱挥在Tg之上

> "It is well known that most polymers leaving the polymerization reactor contain various but small amounts of **unreacted monomer, solvents, water, and/or various reaction by-products**... Their separation from bulk polymer is necessary to improve polymer properties, to recover monomer and solvents, to meet health and environmental regulations, to eliminate odors, and/or to increase the extent of polymerization. **This process of devolatilization is usually performed above the glass transition temperature of the polymer**." (p.977)

**SAP transfer:** Residual acrylic acid/monomer is an unavoidable polymerization artifact. Chain polymerization never reaches 100% conversion. Stripping residual monomer requires Tg-controlled heating — below Tg, the glassy polymer has too little free volume for the volatile to diffuse out.

### Why Tg Matters for SAP 为什么Tg对SAP重要

- Below Tg: glassy polymer, free volume too low, volatile cannot diffuse out
- Above Tg: polymer chain has enough free volume for diffusion
- **SAP implication:** Final-stage drying temperature must be below Tg to prevent over-crosslinking that kills swellability

---

## 2. Two-Stage Drying 两阶段干燥

> "Since ABS requires both surface and bound moisture removal, a **two-stage drying system** is recommended." (p.967)

**General rule:** Fast surface-moisture stage + controlled bound-moisture stage.

### Per-Polymer Systems 聚合物系统

| Polymer | Dryer System | Key Parameter |
|---|---|---|
| **PP** | Flash + FBD | Closed-loop N₂/hexane recovery |
| **S-PVC** | Flash + FBD | Constant-rate 35–5% wb |
| **E-PVC** | Spray + FBD | Water-wet slurry |
| **ABS** | Flash + FBD | Two-stage mandatory |
| **PET** | Crystallizer + column | Dew point −40 to −50°C |
| **Nylon** | Column dryer | Dew point −15 to −25°C |

---

## 3. Hygroscopic vs Nonhygroscopic 吸湿vs不吸湿

| Class | Examples | Moisture Location | Drying Method |
|---|---|---|---|
| **Nonhygroscopic** | PE, PS, PP | Surface only | Convection sufficient |
| **Hygroscopic** | PET, nylon, ABS, PC | **Inside pellet** | **Desiccant dryer** (low dew point) |

> "PET, nylon, ABS, and PC come under the classification of **hygroscopic resins**. These types of polymer resin **collect moisture inside the pellet itself**. Removal of this moisture requires dry air as well as heat... **Desiccant dryers are the dominant technology** for these resins." (p.972)

### Dew Point Requirements 露点要求

| Resin | Dew Point |
|---|---|
| **PET** | **−40 to −50°C** |
| Others (nylon, ABS, PC) | −15 to −25°C |

---

## 4. Permissible Moisture 允许含水率

| Resin | Target (db) | Range (db) |
|---|---|---|
| **PP** | 0.05% | 0.03–0.10% |
| **HDPE** | 0.05–0.10% | 0.03–0.05% |
| **Nylon** | 0.04–0.08% | 0.02–0.06% |
| **PC** | max 0.02% | 0.02% |

---

## 5. Hygiene-Materials Action Cards 卫材应用卡

| Card | Insight | Action | Relevance |
|---|---|---|---|
| **H41-1** | Devolatilization above Tg removes residual monomer | SAP final-stage temp must be below Tg to prevent over-crosslinking | ⭐⭐⭐⭐⭐ |
| **H41-2** | Residual monomer spans ppm to tens of percent | Specify residual acrylic acid spec in SAP procurement | ⭐⭐⭐⭐⭐ |
| **H41-3** | Two-stage drying: fast surface + controlled bound | Apply to SAP powder drying lines | ⭐⭐⭐⭐ |
| **H41-4** | Hygroscopic resins need desiccant (very low dew point) | PET/nylon nonwoven supplier must specify desiccant dryer | ⭐⭐⭐⭐ |
| **H41-5** | PP/PE nonhygroscopic = surface moisture only | Simpler drying for backsheet film | ⭐⭐⭐ |

---

## 6. Related Sources 关联来源

- [[Handbook of Industrial Drying]] — Full book index
- [[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]] — SAP osmotic physics
- [[Industrial Drying Ch35 Drying of Pulp and Paper]] — Pulp drying
- [[Handbook of Nonwovens]] — Polymer nonwovens
- [[SAP（高吸水树脂）]] — Super Absorbent Polymer

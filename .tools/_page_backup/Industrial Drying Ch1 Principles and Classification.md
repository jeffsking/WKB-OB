---
title: "Industrial Drying Ch1: Principles, Classification, Selection"
type: source
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch01.md.md"
chapter: 1
book_title: "Handbook of Industrial Drying"
editor: "Arun S. Mujumdar"
publisher: "CRC Press"
year: 2014
edition: "4th"
lang: "en"
tags: ["source/book", "drying-principles", "classification", "bound-water", "hygroscopic", "constant-rate", "falling-rate", "psychrometrics", "selection", "energy-intensive"]
tags_zh: ["干燥原理", "分类选型", "结合水", "吸湿性", "恒速期", "降速期", "湿空气", "干燥选型", "能耗密集"]
domain: "hygiene-materials"
priority: "P0"
relevance_to_rel: "Foundational framework chapter. Bound vs unbound moisture classification directly maps to fluff pulp (hygroscopic) and SAP (colloidal). Constant-rate/falling-rate drying curve is the basis for through-air dryer design. ~35% of papermaking plant energy goes to drying — procurement leverage point."
---

# Ch1: Principles, Classification, and Selection of Dryers

> **Source:** Mujumdar, A.S. (ed.), *Handbook of Industrial Drying*, 4th ed., CRC Press, 2014. Ch.1, pp.1–31.

---

## 1. Core Framework 核心框架

### Two Coupled Processes 两个耦合过程

Drying is governed by two simultaneous subprocesses:
- **Process 1 (External):** Transfer of energy (heat) from environment to evaporate surface moisture
- **Process 2 (Internal):** Transfer of internal moisture to the surface and its evaporation

> "When a wet solid is subjected to thermal drying, two processes occur simultaneously: 1. Transfer of energy (mostly as heat) from the surrounding environment to evaporate the surface moisture and 2. Transfer of internal moisture to the surface of the solid and its subsequent evaporation due to process 1." (p.1)

**Hygiene implication:** In diaper cores, internal moisture transport (capillary/vapor diffusion through fluff pulp and SAP) is usually the rate-limiting step at low final moisture — surface air conditions matter far less than residence time and bed depth.

### Convective Dominance 对流主导

> "Over 85% of industrial dryers are of the convective type with hot air or direct combustion gases as the drying medium. Over 99% of the applications involve removal of water." (p.3)

**Hygiene implication:** Hot-air convection is the default for pulp, tissue and nonwoven through-dryers.

### Bound vs Unbound Moisture 结合水与自由水

> "Moisture held in loose chemical combination, present as a liquid solution within the solid or even trapped in the microstructure of the solid, which exerts a vapor pressure less than that of pure liquid, is called bound moisture. Moisture in excess of bound moisture is called unbound moisture." (p.1)

**Hygiene implication:** Bound moisture sets the equilibrium moisture content and hence the floor of achievable dryness in cellulose fluff and SAP.

### Characteristic Drying Curve 特征干燥曲线

> "In the constant rate period the rate of drying is determined by the rate of evaporation. When all the exposed surface of the solid ceases to be wetted, vapor movement by diffusion and capillarity from within the solid to the surface are the rate-controlling steps." (p.16)

- **Constant-rate period:** Surface evaporation dominates; drying rate independent of internal structure
- **Falling-rate period:** Internal diffusion/capillarity becomes rate-controlling; time scales with square of thickness

**Hygiene implication:** For thin, fast sheets (tissue, nonwoven web) drying may occur almost entirely in the constant-rate period. For thick/packed hygroscopic beds (fluff in a core) the falling-rate period dominates — argue for thin layers / agitation.

### Dryer Selection Is Multi-Criteria 选型是妥协

> "A wrong dryer for a given application is still a poor dryer, regardless of how well it is designed." (p.25)

> "Minor changes in composition or physical properties of a given product can influence its drying characteristics... leading to a different product and in some cases severe blockages in the dryer itself." (p.25)

**Hygiene implication:** For hygiene products where a few-percent composition shift (add SAP, change binder) changes handling — selection must be done with pilot data, not delegated to vendors.

---

## 2. Classification 分类体系

| Criterion 分类标准 | Types 类型 | Hygiene Relevance 卫材相关性 |
|---|---|---|
| **By heating method** 加热方式 | Direct (convective), Indirect, Mixed | Hot-air convection dominates (85%) |
| **By pressure** 压力 | Atmospheric, Vacuum, Superheated steam | Steam drying for tissue; vacuum for heat-sensitive |
| **By conveying** 输送方式 | Batch, Continuous; Static bed, Moving bed, Agitated | Continuous web dryers for tissue/nonwoven |
| **By product type** 物料类型 | Particulate, Fluidized, Sheet/Web, Fibrous | Nonwoven web = sheet + fibrous |

### Hygroscopic Classification 吸湿性分类 (p.12)

| Class | Examples | MC Floor |
|---|---|---|
| **Nonhygroscopic capillary-porous** | Concrete, sand | Can be dried to near-zero |
| **Hygroscopic-porous** | Paper, textile, fluff pulp | Limited by EMC at storage RH |
| **Colloidal nonporous** | SAP, gel polymers | Set by crosslink + osmotic equilibrium |

---

## 3. Psychrometric Toolkit 湿空气工具

### Key Relationships 关键关系

- **Clausius-Clapeyron:** Relates vapor pressure to temperature for evaporation design
- **Humidity ratio (ω):** Mass of water vapor per mass of dry air
- **Wet-bulb temperature (T_wb):** Adiabatic saturation temperature — limits convective drying floor
- **Enthalpy-humidity chart:** Standard design tool for air-water systems

**Key constraint:** The wet-bulb temperature of the drying air sets the minimum achievable product surface temperature during constant-rate drying (evaporative cooling).

---

## 4. Energy Perspective 能耗视角

> "Drying is perhaps the oldest, most common and most diverse of chemical engineering unit operations... It competes with distillation as the most energy-intensive unit operation due to the high latent heat of vaporization and the inherent inefficiency of using hot air as the (most common) drying medium." (p.1)

- Papermaking: up to **35%** of plant energy goes to drying (p.1)
- Drying removes the least water in absolute terms but is the most costly step (cross-ref Ch35)

**Hygiene implication:** Dryer selection is a capital-and-energy decision, not a peripheral one.

---

## 5. Related Sources 关联来源

- [[Handbook of Industrial Drying]] — Full book index
- [[Industrial Drying Ch15 Impingement Drying]] — Surface drying for tissue/nonwoven
- [[Industrial Drying Ch17 Conveyor Dryers]] — Through-air conveyor/TAD
- [[Industrial Drying Ch33 Drying of Fibrous Materials]] — Pulp fiber physics
- [[Industrial Drying Ch35 Drying of Pulp and Paper]] — THE pulp chapter
- [[Industrial Drying Ch46 Energy Aspects]] — Energy benchmarks
- [[Industrial Drying Ch50 Solid-Liquid Separation]] — Mechanical dewatering

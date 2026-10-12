---
type: source
title: "Industrial Drying Ch10 Industrial Spray Drying Systems"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch10.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Spray drying is a process in which a fluid feed is atomized into droplets that are dried to individual particles when moved in a hot gaseous drying medium, usually air (p.213)."
  - "Spray-dried products explicitly include phenol–formaldehyde resin, PVC emulsion-type chemicals, rubber latex, ceramic powders, and detergents (p.214)."
  - "The Sauter mean diameter is the most suitable mean value to characterize the droplet cloud, defined as the ratio of the total droplet volume to the total droplet surface (p.217)."
  - "Hot-air distribution must prevent wall impingement and air temperature should be lower than the melting point of the product to prevent baking on (p.224)."
  - "Superheated-steam spray drying offers no fire and explosion hazards, no oxidative damage, better product quality under certain conditions, and closed-system operation (p.247)."
  - "In encapsulation, the active material dispersed in a hydrocolloid carrier is entrapped as particles within the hydrocolloid or protein film during drying, and is released under specified conditions controlled by temperature, moisture, and pressure (p.253)."
summary_cn: "喷雾干燥系统章节覆盖雾化器与Sauter平均直径、干燥塔构型与气液接触方式、开式/闭式/自惰化及喷雾+流化床两/三段系统、安全与选型设计，其中乳液聚合物喷雾成粉、两段团聚路线和微胶囊包封释放机制直接对应SAP制粉与卫材活性物递送。"
tags: ["source/book", "drying/spray", "SAP/isolation", "microencapsulation", "atomization"]
tags_zh: ["喷雾干燥", "雾化", "Sauter直径", "微胶囊", "两段干燥"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch1 Principles and Classification]]", "[[Industrial Drying Ch8 Fluidized Bed Dryers]]", "[[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]]", "[[Industrial Drying Ch41 Drying of Polymers]]"]
---

# Industrial Spray Drying Systems (Ch.10)

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.10, pp.211–254 (Filkova, Huang & Mujumdar).

## Chapter Overview 章节概览

Spray drying is the unit operation in which a pumpable liquid or slurry feed is atomized into droplets and dried to individual particles in a hot gas stream, producing powders, granules or agglomerates in a single pass. The chapter covers principles (atomization hardware — rotary wheel, pressure, pneumatic and novel nozzles; drop-size distributions and the Sauter mean D₃,₂; chamber shape and air–droplet contact modes; thermal efficiency), complete system layouts (open, closed, semiclosed/self-inertizing, spray-plus-fluidizer combinations; single/two/three-stage), energy, safety, control, selection, design procedures and CFD, plus forward-looking directions (superheated steam, low-dew-point air, spray freeze drying, encapsulation).

> Note: page numbers derived from PDF-page − 21; spot-check against print edition.

## Key Viewpoints 关键观点

### 1. Liquid in, powder out in one pass 一步成粉

> "Spray drying is a process in which a fluid feed is atomized into droplets that are dried to individual particles when moved in a hot gaseous drying medium, usually air." (p.213)

Exactly the isolation step for polymer latices and superabsorbent solutions — no grinding required if the droplet is sized right.

### 2. Polymer/surfactant products explicitly in scope 聚合物乳液在范围内

> "Chemical industry, e.g., phenol–formaldehyde resin, catalysts, PVC emulsion-type, amino acids, etc. … numerous organic and inorganic chemicals, rubber latex, ceramic powders, detergents, and other products." (p.214)

PVC emulsion and rubber latex are named spray-dried products — the latex/SAP-adjacent link for emulsion-polymerized binders (SBR, acrylics) and detergent/surfactant powders.

### 3. Sauter mean diameter governs powder morphology

> "The so-called Sauter mean diameter seems to be the most suitable mean value to characterize the droplet cloud together with the size distribution. This is defined as the ratio of the total droplet volume to the total droplet surface …" (p.217)

D₃,₂ sets drying time (∝ surface/volume) and final particle size. Atomizer correlations: rotating wheel (peripheral velocity ~150 m/s, p.220), pressure nozzle (Eq 10.9–10.11), pneumatic (compressed air 0.15–0.8 MPa, p.222). Droplet/particle sizes: rotating wheels 1–600 µm, chemicals 10–1000 µm (Table 10.3, p.218).

### 4. Two-stage spray + fluid bed is the agglomeration route 两段团聚路线

> "The semi dried powder is deposited on a moving belt (woven polyester filament) situated at the bottom of the primary spray chamber … After a short stabilization period … the powder is conveyed to the third drying stage … agglomerates with 'instant' properties." (p.239)

Structurally identical to SAP post-treatment: spray-dry to primary fines → belt deposit → fluid-bed second stage to agglomerate into free-flowing granules. Combination spray + fluidizer layout: "Improved energy consumption, reduced capital costs" (p.234–235).

### 5. Superheated-steam spray drying eliminates fire/oxidation 过热蒸汽喷雾

> "No fire and explosion hazards … No oxidative damage … Better quality product under certain conditions … Closed system operation to minimize air pollution." (p.247)

LDP variant: "low dew point (LDP) air at near ambient temperature to 80°C, but with very low humidity" (p.249) for pharma/biochemicals at low T.

### 6. Encapsulation delivers actives via oil-in-water emulsion 微胶囊包封

> "The active material to be encapsulated, such as an oil or flavor in an oil base, is dispersed in a hydrocolloid carrier, e.g., gelatin, modified starch, dextrin or maltodextrin, or gum arabic … homogenized to form an oil-in-water emulsion, and then it is fed to the atomizer for spray drying. In the dryer chamber, the aqueous phase dries and the active material is entrapped as particles within the hydrocolloid or protein film." (p.253)

"The active material from the capsule is released under specified conditions. The main controlling factors of its release are temperature, moisture, and pressure." (p.253) — the spray dryer makes not just a powder but a controlled-release device.

### 7. Design honesty: pilot tests still govern 设计依赖中试

> "We are currently unable to express precisely the spray–air contact, the powder trajectories, and airflow patterns … specification and design of spray dryers are still based on the pilot tests and existing industrial experience" (p.244–245); "accuracy of CFD models are still not well defined" (p.245).

Selection questionnaire lists glass transition temperature and hygroscopicity among required dry-product properties (p.245) — directly the polymer-Tg gate for spray-dried SAP/latex.

## Strengths & Weaknesses 优劣评估

- Strengths: breadth of layouts with concrete operating data (p.234–235); honest modeling limits (p.244–245); explicit polymer-latex feed scope (p.214); encapsulation mechanism fully specified (p.253).
- Weaknesses: droplet-size correlations assume Newtonian feeds; non-Newtonian and viscoelastic SAP/slurry feeds are flagged but not resolved (p.221); droplet-drying models assume constant diffusivity, under-predicting skin-formation crusting for polymer solutions; CFD maturity overstated (p.245).

## Hygiene Implication 卫材关联

Relevance: ★★★★★ — the SAP-isolation, binder-latex and active-encapsulation chapter:

- Isolate emulsion-polymerized SAP/latex by spray drying: PVC-emulsion and rubber-latex are standard spray-dried products (p.214); set D₃,₂ (p.217) for target fine size; watch the wall-impingement/melting rule (p.224). One-pass powder, no milling; primary fines then agglomerated in a fluid bed (see [[Industrial Drying Ch8 Fluidized Bed Dryers]]).
- Route SAP fines through the two-stage spray + fluidizer (p.239) for "instant"-type agglomerates with controlled porosity — the diaper-core granule.
- Encapsulate wipe/sanitary actives: fragrance, skin-care or antimicrobial actives in hydrocolloid walls, release triggered by temperature/moisture/pressure (p.253).
- Use superheated-steam or LDP media for oxidation-sensitive carriers (cellulose-pulp fines, starch, heat-sensitive SAP grades) — no yellowing, lower thermal load (p.247, p.249).
- Use closed-cycle inert gas for solvent-based polymer dopes (explosion/solvent-recovery risk) (p.234).

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch1 Principles and Classification]]
- [[Industrial Drying Ch8 Fluidized Bed Dryers]]
- [[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]]
- [[Industrial Drying Ch41 Drying of Polymers]]

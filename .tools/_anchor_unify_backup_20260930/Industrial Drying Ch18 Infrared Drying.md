---
type: source
title: "Industrial Drying Ch18 Infrared Drying"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch18.md.md"
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "The most common current applications of IR drying are in dehydration of coated films and webs and to correct moisture profiles in drying of paper and board (p.421)."
  - "Combined convective and IR dryers have been shown to be very attractive; IR heating can be coupled effectively with vacuum, and applied continuously or intermittently to save energy and often improve product quality (p.422)."
  - "Generally solid bodies absorb all of the radiation in a very narrow layer near the surface; an 'opaque' solid absorbs radiation in a narrow zone near the surface rather than attenuating within its volume (p.422, p.427)."
  - "As drying proceeds the material's reflectivity increases, lowering absorptivity at low water contents; the emitter temperature can be changed to improve absorption during drying (p.424–425)."
  - "To avoid overheating of the surface and allow radiation to penetrate, the heat source should be at about 2500 K; a lower source temperature may scorch the surface due to intense surface heating (p.425)."
  - "A high-velocity hot air impingement oven with IR electric heaters mounted between adjacent nozzles is used specially for drying adhesives and inks on papers, foam and composite web substances — an industrially viable hybrid (p.432, p.434)."
summary_cn: "红外干燥章节以辐射传热理论（Planck/Wien/Stefan–Boltzmann/Bouguer）为基础，确立'发射器波长与物料吸收带匹配+随干燥进程调温'的设计规则与'2500 K热源防焦烧、利穿透'的反直觉选择，并展示工业成熟的IR+冲击式混合烘炉——对卫材是薄涂层/纸面水分匀平的强力工具（IR本质上是表面干燥器，对厚芯体不适用）。"
tags: ["source/book", "drying/infrared", "coating-cure", "web-drying", "hybrid-oven", "emitter-matching"]
tags_zh: ["红外干燥", "涂层固化", "网材干燥", "混合烘炉", "发射器匹配", "水分匀平"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch12 Microwave and Dielectric Drying]]", "[[Industrial Drying Ch15 Impingement Drying]]", "[[Industrial Drying Ch17 Conveyor Dryers]]", "[[Industrial Drying Ch40 Drying of Coated Webs]]"]
---

# Infrared Drying (Ch.18)

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.18, pp.421–436 (Ratti & Mujumdar).

## Chapter Overview 章节概览

Chapter 18 covers infrared (IR) radiative drying — heat supplied by electromagnetic radiation that needs no propagation medium and is absorbed/converted to heat at the product surface. IR is "an increasingly popular, but not yet common" primary heat source whose strengths are direct near-surface energy deposit, fast transient response, leveling of moisture profiles, and easy combination with convection or vacuum. Sections: radiative-transfer theory (Planck, Wien, Stefan–Boltzmann, Kirchhoff, Bouguer — §18.2), material radiation properties and the need to match emitter wavelength to the product's absorption band (§18.2.2), steady-IR modeling (semi-transparent vs opaque models, §18.3.1), advantages/limitations (§18.3.2), industrial dryers and emitters (§18.4.2), costs (§18.4.3).

> Note: page numbers derived from PDF-page − 21; spot-check against print edition.

## Key Viewpoints 关键观点

### 1. Prime applications: coated webs and paper moisture correction 首要应用

> "The most common current applications of IR drying are in dehydration of coated films and webs and to correct moisture profiles in drying of paper and board." (p.421)

The verbatim hygiene anchor: IR cures coatings on webs (lotion, adhesive, print) and flattens moisture profiles.

### 2. Hybrid configuration, intermittent operation 混合与间歇

> "combined convective and IR dryers have been shown to be very attractive. Also, IR heating can be coupled effectively with vacuum operation … IR heating may be applied continuously or intermittently (in space or time) to save energy and often to improve product quality." (p.422)

IR is almost never standalone; the productive configuration is radiant + convective.

### 3. Opaque solids absorb in a thin surface layer 表面吸收

> "Generally solid bodies absorb all of the radiation in a very narrow layer near the surface." (p.422); "an 'opaque' solid absorbs radiation in a narrow zone near the surface rather than attenuating within its volume" (p.427)

Penetration is shallow for opaque webs — IR cures the coating/surface, not the bulk; "essentially surface dryers" (p.429).

### 4. Emitter wavelength matching and re-tuning 发射器匹配与调温

> "For many materials, transmissivity is higher at lower wavelengths … As drying proceeds, the material … increasing its reflectivity, and consequently lowering its absorptivity at low water contents. It is then possible to change adequately the temperature of the emitter in order to improve the absorption of radiation during drying." (p.424–425)

The emitter must be tuned to the coating/web absorption spectrum and re-tuned as the wet coating dries.

### 5. Scorch vs penetration trade-off 焦烧与穿透的权衡

> "To avoid overheating of the surface and to allow the radiation to penetrate into the product it would be better to choose the heat source at 2500 K … On the other hand, if the lower heat source temperature is used, the surface may be damaged (scorched) due to intense surface heating." (p.425)

Counter-intuitive: a hotter source penetrates better (peak shifted to shorter λ); a cooler source dumps all energy at the surface and scorches it.

### 6. IR + impingement hybrid is the industrial web-coating cure 混合烘炉

> "a high velocity hot air impingement oven with IR electric heaters mounted between adjacent nozzles … specially for drying adhesives and inks on papers, foam and composite web substances." (p.432)

The combination "has already proven to be industrially viable" (p.434).

## Key Terms & Process Details 关键术语

- Radiative-transfer toolkit: r + a + t = 1 (18.1); Wien displacement λ_max·T = 2897.6 µm·K (18.3); Stefan–Boltzmann E_b = σT⁴ (18.4); gray-body net exchange (18.8); Bouguer attenuation I_λ(z) = I_λ(0)exp(−∫K_λ dz) (18.9) (p.422–424).
- Thermal radiation span 0.1–100 µm; near/medium/far IR by wavelength (p.422). Note: the source prints "mm" where µm is physically consistent — treat as µm [待验证].
- Opaque model: ρC_p ∂T/∂t = k∂²T/∂z² + ∂q_a/∂z with q_a = Q_r exp(−∫K dz) (18.12/18.16, p.426–427) — the scale-up kernel; but "testing of the equipment must be carried out in the plant" (p.429).
- Emitter selection, five factors (p.431): absorption of heated material, power density, convected/radiant ratio, installation nature, control type. Quartz lamp radiant efficiency 86% (Table 18.3); life 2000–3000 h (p.433).
- Costs (Table 18.4, p.434): IR 500 $/kW vs convection 300, RF 2000.
- IR advantages/limitations: moisture-profile leveling (p.428); fire hazard listed (p.429); penetration into thick porous webs "has not yet been fully developed" (p.430).

## Strengths & Weaknesses 优劣评估

- Strengths: opens with the hygiene-relevant application verbatim (p.421); full radiative theory toolkit; emitter-matching + moisture-dependent re-tuning rule (p.424–425); proven hybrid oven evidence and concrete costs (p.432, p.434).
- Weaknesses: surface-only ("essentially surface dryers", p.429; thick-porous penetration underdeveloped, p.430); no IR absorption spectra for acrylic/PVA/PU coatings actually used on wipes — only food/paper/wool/wood data (Tables 18.1/18.2); wavelength unit slips in print [待验证 against print].

## Hygiene Implication 卫材关联

Relevance: ★★★★☆ — strong for wipe lotion/print coating cure and moisture leveling; weaker for bulk cores.

- Lotion/print coating cure on wipes: deploy IR for dehydrating/curing the coated film on the wipe web (p.421) — the right tool for thin coatings, not the bulk nonwoven.
- Hybrid oven design: mount IR electric heaters between impingement nozzles (p.432) — radiation cures the coating, convective jets strip solvent/water and protect the substrate; industrially proven (p.434).
- Emitter matching: pick source T so the peak λ sits where the coating absorbs but the substrate does not (p.425, Fig.18.3); raise emitter T as reflectivity climbs during drying to avoid late-cycle under-cure or scorch. Coating-polymer band data must be supplied by the engineer [待验证].
- Scorch avoidance: choose the higher source temperature for penetration (p.425) — a cooler source scorches the polymer film.
- Moisture-profile leveling: use IR's leveling advantage (p.428) to even cross-web moisture on coated/printed wipes.
- Fire safety: IR carries a fire-hazard flag (p.429); size exhaust to remove solvent/smoke/moisture (p.430) for combustible nonwoven substrates.
- Cost model: budget IR capital at ~500 $/kW (Table 18.4) and quartz-lamp life 2000–3000 h (p.433) as the maintenance line in the energy-cost/tonne model.
- Honest limit: for a bulky fluff/SAP core, IR cures only the surface (p.429–430) — do not specify IR for bulk-core drying.

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch12 Microwave and Dielectric Drying]]
- [[Industrial Drying Ch15 Impingement Drying]]
- [[Industrial Drying Ch17 Conveyor Dryers]]
- [[Industrial Drying Ch40 Drying of Coated Webs]]

---
type: source
title: "Industrial Drying Ch12 Microwave and Dielectric Drying"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch12.md.md"
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Dielectric heating is done at frequencies between 1 and 100 MHz, whereas microwave heating occurs between 300 MHz and 300 GHz; microwave wavelengths range from 1 mm to 1 m (p.284)."
  - "With internal heat generation, mass transfer is primarily due to the total pressure gradient established by rapid vapor generation within the material — a 'pumping' action forcing liquid to the surface, often as vapor (p.292)."
  - "The critical moisture content for highly hygroscopic materials occurs between 10 and 40% (dry basis); for nonhygroscopic materials it is about 1% (p.289)."
  - "Polymers' relaxation frequency approaches the microwave frequency as temperature rises, improving energy conversion and possibly leading to runaway heating in materials transparent to microwaves at room temperature (p.288)."
  - "Drying is sharply increased with a leverage of 6:1 or 8:1 in terms of increased drying capacity for each unit of electromagnetic energy added; most effective on thick, hard-to-heat materials (p.293)."
  - "Selective heating: the electromagnetic field generally couples into the solvent, not the substrate — moisture is heated and removed while the carrier is heated primarily by conduction (p.292)."
summary_cn: "微波与介电干燥章节以复介电常数/损耗角正切/穿透深度为框架，论证电磁能体积式沉积带来的内部蒸汽'泵送'与选择性加热，主张其作为常规干燥器的增压/终干混合级（6:1–8:1杠杆）最具价值，并警示聚合物近Tg的介电失控风险——对厚型吸水芯体与水性胶乳粘合的卫材结构高度相关。"
tags: ["source/book", "drying/microwave", "drying/dielectric", "selective-heating", "hybrid-drying", "thermal-runaway"]
tags_zh: ["微波干燥", "介电干燥", "选择性加热", "混合干燥", "热失控", "穿透深度"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch11 Freeze Drying]]", "[[Industrial Drying Ch33 Drying of Fibrous Materials]]", "[[Industrial Drying Ch35 Drying of Pulp and Paper]]", "[[Industrial Drying Ch41 Drying of Polymers]]"]
---

# Microwave and Dielectric Drying (Ch.12)

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.12, pp.283–303.

## Chapter Overview 章节概览

Chapter 12 surveys fundamentals, equipment, industrial applications, and economics of dielectric and microwave drying. Unlike convective drying (heat flows surface → interior), these methods deposit energy volumetrically by coupling an oscillating electric field into polar molecules and ions. The author's core thesis: their rapid, selective, self-limiting heating makes them valuable as a booster or finish stage paired with conventional dryers, not as a standalone unit. Sections: governing equations (ionic conduction, dipolar rotation, complex permittivity, loss tangent, penetration depth), then applications from lumber and textiles to latex-coated tires and pharmaceuticals, closing with a candid cost analysis.

> Note: page numbers derived from PDF-page − 21; spot-check against print edition.

## Key Viewpoints 关键观点

### 1. Frequency regimes: dielectric vs microwave 频段划分

> "it is generally accepted that dielectric heating is done at frequencies between 1 and 100 MHz, whereas microwave heating occurs between 300 MHz and 300 GHz. This makes the wavelengths in dielectric heating extend to many meters. Microwave wavelengths range from 1 mm to 1 m." (p.284)

The lower dielectric band penetrates meters-deep (Table 12.5); microwave bands (915/2450 MHz) couple tightly but penetrate only centimeters. Penetration-vs-intensity trade-off.

### 2. Volumetric "pumping" vs diffusion-limited drying 体积式泵送

> "With internal heat generation, in microwave and dielectric systems, mass transfer is primarily due to the total pressure gradient established because of the rapid vapor generation within the material. Most of the moisture is vaporized before leaving the sample … a sort of 'pumping' action, forcing liquid to the surface, often as a vapor." (p.292)

Internal vapor pressure ejects moisture instead of waiting for diffusion — avoids case-hardening, relevant to sealed skins on SAP/fluff composites.

### 3. Critical moisture defines the hygroscopic window 临界含水率

> "The critical moisture content for highly hygroscopic materials occurs between 10 and 40% (dry basis); for nonhygroscopic materials it is in the region of about 1%." (p.289)

SAP and fluff pulp are highly hygroscopic; below ~10–40% db the dielectric loss collapses (bound water is immobile), so EM drying self-limits — sets the practical lower bound of finish-drying leverage.

### 4. Polymer runaway near Tg 聚合物热失控

> "large molecules, such as polymers, have a relaxation frequency at room temperature that is much lower than the microwave frequency but that increases and approaches it as the temperature rises, resulting in better energy conversion into heat. This may lead to runaway heating in materials that at room temperature are very transparent to the microwave field." (p.288)

A polymer-rich composite "transparent" cold can couple strongly as it warms — thermal-runaway hazard requiring closed-loop power control, especially near the glass transition.

### 5. Hybrid booster leverage 6:1–8:1 混合增压杠杆

> "The drying is sharply increased with a leverage of 6:1 or 8:1 in terms of increased drying capacity for each unit of electromagnetic energy added. This is most effective on thick, hard to heat materials." (p.293)

The economics only work where the conventional dryer's falling-rate zone collapses — precisely the thick, insulating absorbent core.

### 6. Selective heating spares the substrate 选择性加热

> "Selective heating may occur. The electromagnetic field generally couples into the solvent, not the substrate. Hence, it is the moisture that is heated and removed, whereas the carrier or substrate is heated primarily by conduction." (p.292)

Energy targets the polar liquid; fibrous/polymeric structures are not directly overheated — critical for heat-sensitive hygiene webs.

## Key Terms & Process Details 关键术语

- Complex dielectric constant: ε = ε′ − jε″; ε′ stores field energy, ε″ dissipates it (p.288).
- Loss tangent tan δ = ε″/ε′; conversion efficiency; power formula Pᵥ = kE²fε″ (Eq 12.4, p.288–289).
- Penetration depth: depth where available power drops to 1/e (≈37%) of surface value; D ≈ λ₀/(2π√ε″) when ε″ small (Eq 12.7–12.8, p.290). Table 12.5: 2450 MHz penetrates only ~0.05 m in Douglas fir vs ~24 m at 5 MHz.
- Moisture rules (p.289): higher moisture → higher ε′; dielectric loss rises with moisture then levels off at 20–30% and may decrease — physical origin of self-limiting drying; mixture rule: composite dielectric constant lies between components'.
- Modes (§12.3.2): preheat / booster / finish; pulsed on/off control available (p.290).

## Strengths & Weaknesses 优劣评估

- Strengths: candid on economics and failure modes; concrete numbers for critical moisture and penetration depth (p.289–291); correctly frames EM heating as booster/finish, not universal replacement.
- Weaknesses: no quantitative drying-rate model; penetration-depth data only for Douglas fir (Table 12.5), not polymers or cellulose; cost comparison admittedly difficult — "suppliers express their costs in many different ways" (p.301).

## Hygiene Implication 卫材关联

Relevance: ★★★★★ — thick, low-density, insulating hygroscopic structures (fluff + SAP cores) and waterborne latex binders are exactly the "hard-to-heat" substrates dielectric methods address.

- Thick-core booster: final 10–40% db moisture in fluff+SAP cores is diffusion-limited in hot-air ovens; add a 915 MHz or 13.56/27.12 MHz dielectric booster/finish stage where the falling-rate zone collapses (p.293 leverage; p.291 deep penetration) → shorter line, less case-hardening, moisture leveling across thick pads.
- Waterborne latex binder drying: field couples to water, substrate heated by conduction (p.292; cf. latex tire coating case, p.298) → drive off binder water without overheating polymer; preserves fiber/bond integrity in airlaid/nonwoven saturation bonding.
- Runaway guard: hot-melt/adhesive layers warming past Tg suddenly couple (p.288) — use closed-loop power control and pulsed on/off (p.290) to avoid internal scorch/bond degradation.
- Scope gap: loss factor, penetration, and runaway are illustrated only for wood/food — never for cellulose fluff, cross-linked polyacrylate SAP, or PE/PP nonwoven; transferring Douglas-fir numbers to a hygiene composite is an [inference] extrapolation. Whether swollen SAP hydrogel permits selective non-destructive finish drying is an open question [待验证].

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch11 Freeze Drying]]
- [[Industrial Drying Ch33 Drying of Fibrous Materials]]
- [[Industrial Drying Ch35 Drying of Pulp and Paper]]
- [[Industrial Drying Ch41 Drying of Polymers]]

---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_c41b7c1576df683c735e9505860672ad001a693ee6c0644e"
source_file: "ID · analysis_ch12.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch12.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch12.md.md

# Chapter 12 — Microwave and Dielectric Drying

## 1. Chapter Overview

Chapter 12 surveys the fundamentals, process advantages, equipment, industrial applications, and economics of electromagnetic (dielectric and microwave) drying. Unlike conductive/convective drying, which moves heat from surface to interior, these methods deposit energy volumetrically by coupling an oscillating electric field directly into polar molecules and ions. The chapter argues that the unique, rapid, selective, and self-limiting nature of this heating makes it especially valuable as a booster or finish stage paired with conventional dryers, rather than as a standalone unit. After establishing the governing equations (ionic conduction, dipolar rotation, complex permittivity, loss tangent, penetration depth), the author catalogs applications from lumber and textiles to latex-coated automotive tires and pharmaceuticals, then closes with a candid cost analysis: high capital cost demands judicious, hybrid deployment. For hygiene-materials R&D the chapter is highly relevant — thick, low-density, insulating structures (fluff + SAP cores) and waterborne latex binders are exactly the "hard-to-heat" substrates dielectric methods address.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

## 2. Key Viewpoints

### Viewpoint 1 — Dielectric vs microwave frequency regimes

- Page: p.284
- Quote: > "it is generally accepted that dielectric heating is done at frequencies between 1 and 100 MHz, whereas microwave heating occurs between 300 MHz and 300 GHz. This makes the wavelengths in dielectric heating extend to many meters. Microwave wavelengths range from 1 mm to 1 m."
- Interpretation: The single most important scoping decision is frequency. The lower dielectric band penetrates meters-deep (Table 12.5), ideal for thick hygiene cores; microwave bands (915/2450 MHz) couple tightly but penetrate only centimeters. Choice of band is a penetration-vs-intensity trade-off.
### Viewpoint 2 — Volumetric "pumping" differs fundamentally from diffusion-limited drying

- Page: p.292
- Quote: > "With internal heat generation, in microwave and dielectric systems, mass transfer is primarily due to the total pressure gradient established because of the rapid vapor generation within the material. Most of the moisture is vaporized before leaving the sample… a sort of 'pumping' action, forcing liquid to the surface, often as a vapor."
- Interpretation: Conventional drying is diffusion-rate-limited and needs high surface temperature; electromagnetic drying generates internal vapor pressure that ejects moisture. This avoids case-hardening — directly relevant to avoiding a sealed skin on SAP/fluff composites.
### Viewpoint 3 — Critical moisture defines the hygroscopic window

- Page: p.289
- Quote: > "The critical moisture content for highly hygroscopic materials occurs between 10 and 40% (dry basis); for nonhygroscopic materials it is in the region of about 1%."
- Interpretation: SAP and fluff pulp are highly hygroscopic; below ~10–40% db the dielectric loss collapses (bound water is immobile), so electromagnetic drying self-limits. This sets the practical lower bound where finish-drying leverage ends.
### Viewpoint 4 — Temperature-dependent runaway in polymers

- Page: p.288
- Quote: > "large molecules, such as polymers, have a relaxation frequency at room temperature that is much lower than the microwave frequency but that increases and approaches it as the temperature rises, resulting in better energy conversion into heat. This may lead to runaway heating in materials that at room temperature are very transparent to the microwave field."
- Interpretation: A polymer-rich hygiene composite that looks "transparent" to microwaves cold can suddenly couple strongly as it warms — a thermal-runaway hazard requiring closed-loop power control, especially near the glass transition.
### Viewpoint 5 — Hybrid booster drying gives 6:1–8:1 leverage

- Page: p.293
- Quote: > "The drying is sharply increased with a leverage of 6:1 or 8:1 in terms of increased drying capacity for each unit of electromagnetic energy added. This is most effective on thick, hard to heat materials."
- Interpretation: The economics only work when MW/dielectric energy is added where the conventional dryer's falling-rate zone collapses — precisely the thick, insulating absorbent core.
### Viewpoint 6 — Selective heating spares the substrate

- Page: p.292
- Quote: > "Selective heating may occur. The electromagnetic field generally couples into the solvent, not the substrate. Hence, it is the moisture that is heated and removed, whereas the carrier or substrate is heated primarily by conduction."
- Interpretation: Because energy targets the polar liquid, fibrous and polymeric structures are not directly overheated — critical for heat-sensitive hygiene webs (nonwoven, SAP, latex bonds) where conventional hot air risks melting or degrading the carrier.
## 3. Research Method & Data Sources

||||||
|---|---|---|---|---|
|Engineering review|Mechanism derivation + equipment/process catalog|Primary literature, vendor/standards data (CISPR 11, ITU ISM bands), industrial case studies|Loss-factor tables (12.4, 12.5), cost tables (12.7), drying-curve schematics (Fig 12.4)|Qualitative-physical; illustrative, not statistically validated|

[纯理论/综述章节，未使用实证方法] — the chapter synthesizes physics and practice; no controlled experiments are reported.

## 4. Argumentation Process

The author builds a layered case: (1) define the energy — EM waves couple to dipoles/ions, not by conduction (Eq 12.1–12.6); (2) characterize the material response — loss factor, critical moisture, penetration depth, self-limiting leveling (§12.2.5); (3) contrast with convention — internal-pressure "pumping" vs surface diffusion (§12.3); (4) operationalize — preheat / booster / finish modes (§12.3.2); (5) show hardware — generators and applicators (§12.4); (6) prove by application — lumber, textile, paper, latex tire, pharma (§12.5); (7) reality-check cost — high capital, justified only hybrid (§12.6–12.7). The rhetorical move is to repeatedly concede limitations (capital cost, runaway, thin penetration) so the hybrid recommendation lands credibly. A second thread runs underneath: the chapter is fundamentally a coupling-efficiency argument — every equation (Eq 12.3 ionic, Eq 12.4 dipolar, Eq 12.7 penetration) is marshaled to show when the field actually deposits energy in this material, which is the exact question a hygiene-core engineer must answer before specifying a band.

## 5. Role in the Book

Ch12 is the capstone "emerging/electromagnetic" drying method among the mechanical/thermal chapters (rotary, fluid bed, drum, spray, freeze). It complements Ch10 (spray) and Ch11 (freeze) by addressing thick, low-thermal-conductivity solids that those atomization/sublimation methods cannot handle, and prefigures the hybrid (two/three-stage) thinking introduced in Ch10.

## 6. Strengths & Weaknesses

✅ Strengths: Unusually candid on economics and failure modes. The critical-moisture and penetration-depth treatment (p.289–291) is given with concrete numbers. ✅ Selective, volumetric heating is correctly framed as a finishing/boosting tool, not a universal replacement.

⚠️ Limitations: No quantitative drying-rate model (unlike Ch10/Ch11 PDE treatments); penetration depth is given only for Douglas fir (Table 12.5), not polymers or cellulose. The author admits the cost comparison difficulty: > "suppliers express their costs in many different ways" (p.301), leaving §12.6 more illustrative than rigorous.

## 7. Key Terms / Concepts

- Complex dielectric constant (p.288): "« ¼ « 0 (cid:2) j« 00 (12:5)" — ε = ε′ − jε″; ε′ = relative permittivity, ε″ = loss factor.
- Loss tangent (p.289): "tand 00 (12:6)" — tan δ = ε″/ε′; ratio of loss to stored field energy.
- Critical moisture (p.289): ~10–40% db for hygroscopic, ~1% for nonhygroscopic materials.
- Penetration depth (p.290): depth at which available power drops to 1/e (≈37%) of surface value; set by wavelength, ε′, ε″.
- Lossy dielectric (p.288): class of materials (water, wood, food, moist solids) that absorb EM energy and convert it to heat.
- Relaxation frequency (p.288): the temperature- and molecular-size-dependent rate at which dipoles align/relax with the field.
## 8. Micro close-reading (ONE key paragraph)

"The higher the moisture content, usually the higher is the dielectric constant. 2. The dielectric loss usually increases with increasing moisture content but levels off at values in the range of 20 to 30% and may decrease at still higher moisture. 3. The dielectric constant of a mixture usually lies between that of its components." (p.289)

Sentence-by-sentence: (1) Moisture ↑ → ε′ ↑ — water's permittivity (~78) dominates the mixture, so wetter = more couplable. (2) Loss rises then plateaus at 20–30% and may fall — once free water saturates, additional water does not linearly increase heating; this is the physical origin of self-limiting drying. (3) Mixture rule — composite cores behave as weighted averages, so a fluff/SAP/PE-film laminate's effective loss is predictable from components. 💡 Standout: the "level-off at 20–30%" inflection is exactly where finish-drying leverage peaks and runaway risk appears — the single most decision-relevant sentence for hygiene-core process design.

## 9. Concept deep-dive

Loss tangent (tan δ = ε″/ε′) and the power formula Pᵥ = kE²fε″. (p.288–289)
- Definition: Pᵥ = kE²fε″ (Eq 12.4); equivalently with tan δ. ε′ stores field energy, ε″ dissipates it; tan δ = ε″/ε′ measures conversion efficiency.
- Operational? Yes — directly measurable; selects frequency/band and predicts heating rate.
- Usage in chapter: governs material classification (conductors/insulators/dielectrics/magnetic, p.288), penetration depth (p.290), and self-limiting leveling (p.289).
- Academic origin: electromagnetic theory of dielectrics; linked here to ionic conduction (Pᵥ = E²qnm, Eq 12.3, p.287) and dipolar rotation (relaxation, p.288).

Penetration depth (Eq 12.7/12.8). (p.290)
- Definition: D is depth where power = 1/e of surface; D ∝ λ₀ / √ε′(√(1+(ε″/ε′)²)−1) … (12:7)"; simplified D ≈ λ₀/(2π√ε″) when ε″ small, Eq 12.8).
- Usage: Table 12.5 shows 2450 MHz penetrates only ~0.05 m in Douglas fir vs ~24 m at 5 MHz — the core reason low-frequency dielectric suits thick cores.

## 10. Academic critique & open questions

- Scope gap: penetration depth, loss factor, and runaway are illustrated only for wood/food, never for cellulose fluff, cross-linked polyacrylate SAP, or PE/PP nonwoven — the very materials of a diaper. Transferring the Douglas-fir numbers to a hygiene composite is an [inference] extrapolation.
- Open Q1: Can a swollen SAP hydrogel be modeled as the "bound water" low-loss region of Fig. 12.3, and does its gel-state dielectric behavior permit selective, non-destructive finish drying?
- Open Q2: With polymers' relaxation frequency rising toward microwave as T→Tg (p.288), what is the safe operating window for drying hot-melt/adhesive-containing cores without runaway?
## 11. Hygiene-material relevance & action cards

Relevance: ★★★★★ — directly addresses thick, insulating, hygroscopic, latex-bonded structures central to diapers/wipes/absorbent cores.

ACTION CARD 1 — Boost thick-core drying
- Situation: Final 10–40% db moisture in fluff+SAP core is diffusion-limited and slow in hot-air ovens.
- Apply: Add a 915 MHz (or 13.56/27.12 MHz dielectric) booster/finish stage where the falling-rate zone collapses (p.293, 6:1–8:1 leverage; p.291 deep penetration).
- Effect: Shorter line, less case-hardening, moisture leveling across thick pads.

ACTION CARD 2 — Dry waterborne latex binders selectively
- Situation: Latex-bonded airlaid cores / nonwoven saturation (cf. auto-tire latex coating, p.298).
- Apply: Use selective heating — field couples to water, substrate heated by conduction (p.292) — to drive off latex water without overheating polymer.
- Effect: Lower thermal profile, preserved fiber/bond integrity.

ACTION CARD 3 — Tame polymer runaway near Tg
- Situation: Hot-melt/adhesive layers in the composite warm past Tg and suddenly couple (p.288).
- Apply: Closed-loop power control + pulsed on/off (p.290) to prevent internal scorch while finishing.
- Effect: Avoids hidden internal burn / bond degradation.

## 12. Book-map quotes

"With internal heat generation… mass transfer is primarily due to the total pressure gradient established because of the rapid vapor generation within the material… a sort of 'pumping' action." — p.292 — the chapter's central contrast with conventional diffusion drying.

"large molecules, such as polymers, have a relaxation frequency at room temperature that is much lower than the microwave frequency but that increases and approaches it as the temperature rises, resulting in better energy conversion into heat. This may lead to runaway heating…" — p.288 — the key hazard for polymer-containing hygiene composites.

"The drying is sharply increased with a leverage of 6:1 or 8:1… most effective on thick, hard to heat materials." — p.293 — the economic justification for hybrid deployment.


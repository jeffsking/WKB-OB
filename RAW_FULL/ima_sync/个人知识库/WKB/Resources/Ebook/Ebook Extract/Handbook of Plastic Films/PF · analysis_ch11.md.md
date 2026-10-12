---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_cbb5e6d6b7cb5dcdc71d2545f19dabdc001a693ee6c0644e"
source_file: "PF · analysis_ch11.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Plastic Films/PF · analysis_ch11.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# PF · analysis_ch11.md.md

# Chapter 11 — Physicochemical Criteria for Estimating the Efficiency of Burn Dressings

## 1. Chapter Overview

This chapter (K. Z. Gumargalieva & G. E. Zaikov) develops, for the first time in the book's framing, a quantitative physicochemical basis for judging burn-dressing performance. The authors argue that dressing efficiency cannot be assessed from scattered clinical reports because the underlying physicochemical properties (sorption, penetrability, adhesion) are rarely tabulated. They therefore build a measurement programme — porosity, pore size, surface energy, sorption, air/vapour penetrability, adhesion — and a theoretical model in which the maximal sorption capacity is set by the free volume of the material, calculable from its density. From sorption kinetics, gas/liquid transport equations and an action model (sorption → evaporation → gas transfer), they derive four concrete first-aid dressing criteria: free-volume utilisation ≥0.9, thickness ≥0.5 cm, adhesive strength ≤20 N/m, and open-pore diameter ≤0.5 µm. The chapter is thus a bridge between polymer film/porous-material science and a wound-care application, with extensive tabulated data on cellulose, collagen, polyurethane and polyolefin dressings.

## 2. Key Viewpoints

### Viewpoint 1 — Sorption ceiling equals free volume

- Page: p.285
- Quote: > "Based on theoretical and experimental data, it was found that the maximal sorptional ability of a burn dressing is determined by the free volume of the dressing material calculated from the value of the material density."
- Interpretation: The chapter's central thesis: liquid-holding capacity is a geometric/material property (free volume), not merely a surface effect. This reframes dressing design as a porosity/density optimisation problem — directly transferable to absorbent-core engineering.
### Viewpoint 2 — A dressing must fulfil three coupled functions

- Page: p.290
- Quote: > "(1) Absorb the wound exudate, which contains metabolic products and toxins; (2) Provide optimum water, air and heat exchange between the wound and the atmosphere; (3) Protect the wound from the penetration of microorganisms from the air."
- Interpretation: These three functions (sorb / breathe / barrier) are exactly the functional triad of a diaper or失禁 pad (acquisition–distribution–retention, vapour transmission, leakage/microbe barrier). The chapter operationalises all three with measurable parameters.
### Viewpoint 3 — Polyolefins are near-impermeable to water (great barrier, poor wicking)

- Page: p.299
- Quote: > "Polyethylene (ρ = 0.923) 0.006 298 … Polypropylene 0.007 298 … Polytetrafluoroethylene 0.01 293 … Polyethyleneterephthalate 0.3 303"
- Interpretation: Tabulated water solubility in polymers shows PP/PE ∼0.006–0.007 (10² g/g) versus regenerated cellulose 46 and poly(2-oxyethyl methacrylate) 40. This is the quantitative backbone for choosing a backsheet/barrier film (PE/PET) versus a topsheet/acquisition layer (hydrophilic cellulose/viscose).
### Viewpoint 4 — Wet-state gas penetrability collapses by orders of magnitude

- Page: p.318
- Quote: > "The mass transfer of gases (oxygen and nitrogen) through the dressing is 2-4 orders of magnitude slower with wet samples than with the dry ones in similar conditions."
- Interpretation: Saturation fills pore space and chokes air transport — a direct analogue of the "saturated core = stuffiness" failure mode in hygiene products; barrier/breathability must be specified wet, not dry.
### Viewpoint 5 — Quantitative first-aid efficiency criteria

- Page: p.323–324
- Quote: > "A first-aid burn dressing must use its entire free volume for sorption. This volume must be 0.9 or more of the total volume of the dressing. Dressing thickness must be 0.5 cm or more." … "Average diameter of open (connected) pores must not exceed 5 × 10–7 m (0.5 µm)."
- Interpretation: The authors convert vague "good dressing" requirements into testable numbers — free-volume fraction, thickness, and a 0.5 µm pore-cutoff that physically excludes bacteria. These are directly reusable as absorbent-product design acceptance limits.
### Viewpoint 6 — Adhesion is governed by surface energy and wetting angle

- Page: p.316
- Quote: > "W_a = γ(1 – cos θ)"
- Interpretation: The Dupré–Young work of adhesion shows low-adhesion (atraumatic) removal is achieved by minimising substrate surface tension and controlling the wetting angle — the same lever used to make a non-stick, skin-friendly topsheet.
## 3. Research Method & Data Sources

||||||
|---|---|---|---|---|
|Experimental characterisation|Porosity from density (eq. 11.1) and microscopy (eq. 11.2)|Dressings (collagen, PU, cellulose, metallised)|MIN-10 light microscope|Two independent porosity methods cross-check|
|Sorption|Continuous immersion float device (Fig. 11.3), eq. 11.3 (m = 0.70 h)|C∞ from water/plasma uptake|Horizontal microscope + float cell|Correlation coeff. 0.96 vs. free-volume model|
|Vapour/air penetrability|Desiccator mass-loss (eq. 11.10) & polyethylene-sack airflow (eq. 11.21–11.22)|P_H2O, P_air tables|Desiccator, compressor, manometer|Wet-state measured explicitly|
|Adhesion|Blood/thrombin clot pull-off at 90°|A (mN/m), θ (deg)|Modified clot device (eq. 11.25–11.27)|Thermodynamic W_a model|
|Theory|Diffusion/transport equations (eq. 11.5–11.34)|Derived models|—|Simplifications (Henry's law, cubic-pore model) stated|

Not a pure review: the authors built bespoke devices and present original tables (11.6–11.16).

## 4. Argumentation Process

Premises: (a) dressing efficiency is undefined without physicochemical metrics; (b) exudate is mostly water plus salts/proteins/cells. Evidence chain: measure porosity → define free volume → show C∞ correlates with free volume (r = 0.96, p.302) → derive sorption kinetics (eq. 11.4) → model combined sorption–evaporation–gas-transfer action (§11.6) → observe wet-state penetrability drop (2–4 orders). Conclusion: four numeric criteria. Rhetorical move: the chapter repeatedly converts a qualitative clinical need ("must not stick", "must protect") into a measured quantity (W_a ≤ 20 N/m; pore ≤ 0.5 µm), then validates the model against experimental C∞. The 0.5 µm pore cutoff is asserted from a stated microbiological fact rather than derived — a minor logical leap left to the reader.

## 5. Role in the Book

As Ch.11 of a Handbook of Plastic Films, this is the most "applied/medical" chapter and the clearest demonstration that film/porous-polymer science generalises beyond packaging. It reconnects to Ch.8 (surface modification, surface energy), Ch.9 (permeation P = D·S, barrier design), Ch.12 (film testing methods), and Ch.13 (material choice & recyclability). For the hygiene expert it is the conceptual twin of topsheet/backsheet/acquisition-layer design, using wound exudate as the analogue of urine/serum.

## 6. Strengths & Weaknesses

✅ Strengths:
- Rigorous, device-level quantification: "The maximal sorption (the amount of liquid, really dissolved and filling micro- and macropores) is determined using the device shown in Figure 11.3" (p.294).
- Strong predictive model: free-volume correlation coefficient 0.96 (p.302).

⚠️ Limitations:
- Scope is burn exudate, not urine/menses: "The composition of oedema liquid changes depending on the burn degree" (p.297) — body-fluid chemistry differs, so absolute C∞ values are not directly portable.
- Some data and devices are from older (largely Russian) sources; modern superabsorbents (SAP) are absent, limiting direct absorbent-core transfer.
- Pore ≤0.5 µm bacterial cutoff is stated without derivation (p.324).

## 7. Key Terms / Concepts

- Free volume: (p.285) "the maximal sorptional ability of a burn dressing is determined by the free volume of the dressing material calculated from the value of the material density."
- Porosity (Π): (p.292) "The porosity of materials (the relation of pore space volume to total volume) is determined by the following two methods."
- Aqua-penetrability: (p.305) "The process of mass transfer of water through the material layers is often called aqua-, water or vapour penetrability."
- Work of adhesion (W_a): (p.316) "W_a = γ(1 – cos θ)".
- Sorption isotherm (S-type): (p.294) "The sorption isotherm for a material with micropores possesses an S-type form (Figure 11.2)."
- Atraumatic / non-adhesive layer: (p.290) "the burn dressing must be removable from the wound without further injury to the patient."
## 8. Micro close-reading

Paragraph (p.285, §11.1 closing):
> "Based on theoretical and experimental data, it was found that the maximal sorptional ability of a burn dressing is determined by the free volume of the dressing material calculated from the value of the material density. Kinetic parameters were determined from the sorption curves. These parameters help in predicting the behaviour of burn dressings. Criteria for estimating the efficiency of first-aid burn dressings are then formulated."

- Sentence 1 — States the core finding: sorption ceiling = free volume from density. Function: thesis. Keyword: free volume (geometric, not chemical).
- Sentence 2 — Method link: kinetics extracted from sorption curves. Technique: curve-fitting to eq. 11.4.
- Sentence 3 — Utility claim: parameters predict in-use behaviour.
- Sentence 4 — Roadmap: the four criteria (§11.7) follow.
- Logic: empirical finding → method → prediction → normative criteria. A compact manifesto for the whole chapter.
💡 Standout: "the maximal sorptional ability … is determined by the free volume … calculated from the value of the material density" — a single sentence that turns absorbency into a measurable, designable material constant.
## 9. Concept deep-dive

### 9.1 Free volume as the determinant of sorption capacity

- Definition (p.285): quoted above; operationalised via density (eq. 11.1) and microscopy (eq. 11.2).
- Operational? Yes — ρ₀ measured on samples pressed at 500 GPa; free volume = 1 − ρ/ρ₀.
- Usage in chapter: Fig. 11.6 plots C∞ vs free volume with r = 0.96 (p.302): "for the majority of hydrophilic burn dressings, the maximum sorption capacity with reference to water may be predicted satisfactorily."
- Academic origin: polymer free-volume theory (cohenential with Williams–Landel–Ferry / Doolittle concepts; here applied to porous sorbents).
### 9.2 Aqua-penetrability and the P = D·σ relation

- Definition (p.307): water mass transfer through layers; governed by "C_H2O = σP" (Henry's law, eq. 11.7) and "P_H2O = D_H2O σ" (eq. 11.9), giving "P_H2O = m_H2O / (ΔP S t)" (eq. 11.10).
- Operational? Yes — measured on the desiccator device; values in Table 11.10 (e.g., perforated metallised cellulose 9.0×10⁹, PET-class low).
- Usage: separates hydrophobic (low solubility, high chain mobility e.g. PDMS) from hydrophilic (high solubility) transport mechanisms (p.305–306).
- Relation: this is the same P = D·S permeation formalism used in Ch.9 packaging barriers.
### 9.3 Work of adhesion & surface energy control

- Definition (p.316): "W_a = γ(1 – cos θ)"; necessary condition for low adhesion is "γ_l >> γ_s" (p.317).
- Operational? Yes — wetting-angle measurement (±1°) per §11.4.3; Table 11.15 lists γ_s and W_a for PE (31/99), PET (43/104), etc.
- Usage: explains atraumatic removal; lowest W_a polymers (PTFE 83, silicone 78) = best non-stick surfaces.
## 10. Academic critique & open questions

- Method scope: The cubic/none-interconnecting pore model (eq. 11.12–11.16) and Henry's-law solubility are simplifications; real nonwovens have tortuous, interconnected pores (acknowledged p.303: "great tortuosity in the direction of mass transfer").
- Body-fluid mismatch: exudate ≠ urine; protein/cell content and electrolyte load differ, so absolute C∞ and adhesive values are indicative, not directly portable to hygiene.
- SAP blind spot: No superabsorbent polymer is considered; modern hygiene cores rely on SAP gel-blocking, absent here.
- Open Q1: Can the free-volume → C∞ correlation (r=0.96) be extended to SAP-containing composites where gel swelling, not free volume, dominates?
- Open Q2: The 0.5 µm bacterial-exclusion pore cutoff — what is the quantitative microbiological basis, and does it hold for viral/aqueous-pathogen transport?
## 11. Hygiene-material relevance & action cards

Relevance to diaper / wipe / absorbent-core R&D: ★★★★☆ (same functional triad — sorb/breathe/barrier — but body fluid and SAP context differ).

ACTION CARD 1 — Design the acquisition/distribution layer by free-volume utilisation
- Situation: Specifying a new acquisition or distribution layer (ADL) / fluff-SAP core.
- Apply: Use the chapter's rule that maximal sorption ≈ free volume (p.285) and require free-volume utilisation ≥0.9 with a thickness threshold (p.323: "Dressing thickness must be 0.5 cm or more").
- Expected effect: Predictive, density-based capacity control instead of trial-and-error; quantified core-weight vs. absorbency trade-off.

ACTION CARD 2 — Choose backsheet polymer from water solubility & gas penetrability tables
- Situation: Selecting breathable vs impermeable backsheet film.
- Apply: Use Table 11.5 (p.299: PP 0.007, PE 0.006 g/g water solubility) and Table 11.11 (p.309: PE O₂ penetrability 0.35×10¹⁵) to position PE/PET as barriers and microporous/breathable films where vapour escape is needed.
- Expected effect: Evidence-based barrier vs breathability tiering; avoid over-breathable backsheet that leaks.

ACTION CARD 3 — Control topsheet skin-friendliness via surface energy
- Situation: Reducing topsheet cling / skin irritation.
- Apply: Apply Dupré–Young W_a = γ(1 − cos θ) (p.316) and the rule γ_l >> γ_s for low adhesion; choose low-γ_s surfaces (PTFE 18.5, silicone 21.0 — Table 11.15) or corona/plasma treat to tune wetting angle.
- Expected effect: Atraumatic, low-residue topsheet; quantifiable adhesion target (≤20 N/m analogue from p.324).

## 12. Book-map quotes

"the maximal sorptional ability of a burn dressing is determined by the free volume of the dressing material calculated from the value of the material density." — p.285 — the chapter's founding thesis, portable to any porous absorbent.
"A first-aid burn dressing must use its entire free volume for sorption. This volume must be 0.9 or more of the total volume of the dressing." — p.323 — turns absorbency into a measurable design acceptance limit.
"W_a = γ(1 – cos θ)" — p.316 — the surface-energy lever that controls stick/non-stick behaviour of any film facing skin.

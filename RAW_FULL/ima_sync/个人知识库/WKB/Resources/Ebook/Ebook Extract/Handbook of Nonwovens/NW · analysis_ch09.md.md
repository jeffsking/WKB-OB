---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_692a659f0a78f1fedf691050b040f61c001a693ee6c0644e"
source_file: "NW · analysis_ch09.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Nonwovens/NW · analysis_ch09.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# NW · analysis_ch09.md.md

# Chapter 9 — Characterisation, testing and modelling of nonwoven fabrics

## 1. Chapter Overview

Chapter 9 (N. Mao & S.J. Russell, with §9.22 by B. Pourdeyhimi) is the measurement-and-modelling capstone of the Handbook. It asserts that nonwoven performance is governed jointly by composition (fibre, binder, filler, finish) and structure, then organises the field into: (1) characterisation of bond structures for each bonding route (needlepunch, hydroentangle, stitch-bond, thermal, chemical); (2) dimensional parameters (weight, thickness, density, uniformity, fibre orientation distribution/FOD, porosity and pore size); (3) a large compendium of test standards (general, medical, air-filtration, and—critically—absorbent hygiene products, lamination strength, wiping efficiency); (4) measurement techniques for basic parameters, FOD (image analysis), pore size (sieving, bubble point, porometry, mercury intrusion, BET); (5) mechanical (tensile), gas/liquid permeability (D'Arcy), water-vapour transmission, and wetting/liquid-absorption testing (wettability/contact angle, wicking vs. demand absorbency, strike time, GATS, drainage); and (6) a substantial modelling section translating structure into properties (thermal conductivity, pore-size, tensile, bending, specific permeability, absorbency, capillary wicking via Lucas–Washburn and the directional Mao–Russell model, thermal resistance, acoustic impedance, filtration). The chapter is the quantitative backbone that lets the bonding/finishing chapters (6–8) be verified and optimised.

## 2. Key Viewpoints

### Viewpoint 1 — Performance = composition × structure

- Page: p.401
- Quote: > "The physical, chemical and mechanical properties of nonwoven fabrics that govern their suitability for use depend on the properties of the composition and the fabric structure. The composition in this context refers to the fibre properties as well as chemical binders, fillers and finishes present on, between, or within the fibres in the fabric."
- Interpretation: The chapter's founding premise—every test and model traces back to composition and structure; essential for designing measurable hygiene specs.
### Viewpoint 2 — Fluid-handling properties are explicitly enumerated

- Page: p.402
- Quote: > "Fluid handling properties: permeability, liquid absorption (liquid absorbency, penetration time, wicking rate, re-wet, bacteria/particle collection, repellency and barrier properties, run-off, strike time), water vapour transport and breathability."
- Interpretation: This sentence is effectively the test-menu for absorbent hygiene products—strike time, wicking, re-wet, barrier are exactly the diaper metrics.
### Viewpoint 3 — Two liquid-transport modes: wicking (in-plane) vs. demand absorbency (through-plane)

- Page: p.442
- Quote: > "There are two main types of liquid transport in nonwovens. One is the liquid absorption which is driven by the capillary pressure in a porous fabric… When the liquid front enters into the fabric from one face to the other face of the fabric, it is referred to as demand absorbency or spontaneous uptake."
- Interpretation: The in-plane/through-plane distinction is the physical basis of ADL (wicking) versus acquisition layer / core uptake (demand absorbency)—central to absorbent-core design.
### Viewpoint 4 — Wettability is a surface-energy balance

- Page: p.442–443
- Quote: > "The wettability of a nonwoven fabric refers to its ability to be wetted by liquid, and is determined by the balance of surface energies in the interface between air, liquid and solid materials (i.e., fibres or filaments in the fabric)."
- Interpretation: Connects directly to Ch7's fibre surface-energy data (PP 23, PET 42 mN/m) and Ch8's rewetters/plasma—wettability is measurable and engineerable.
### Viewpoint 5 — Dedicated test standards exist for absorbent hygiene products

- Page: p.423 (Table 9.1)
- Quote: > "Absorbent hygiene products — Syngina method (tampons); Ethanol-extractable organotin [WSP ERT 360.0-351.0]; Synthetic urine-extractable organotin II [WSP ERT 361.0-352.0]; Lamination strength [WSP New method]; Wiping efficiency [ASTM D6650-01, D6702-01]."
- Interpretation: Confirms the industry has standardised hygiene-specific tests (extractables, wiping efficiency, lamination)—the compliance checklist for R&D/QC.
### Viewpoint 6 — Thermal conductivity of common polymers is tabulated

- Page: p.454–455 (Table 9.7)
- Quote: > "[Tables 9.7] PP = 0.12, PET = 0.14, PE = 0.34 W m⁻¹ K⁻¹" (thermal conductivity values for PP, PET, PE).
- Interpretation: Quantitative input for modelling heat transport in hygiene assemblies (e.g., warmed-surface or thermally insulating layers); PE's higher conductivity matters for film layers.
## 3. Research Method & Data Sources

This chapter is [纯理论/综述章节，未使用实证方法] but uniquely compiles standardised test methods and analytical/numerical models (not a single experiment). Data sources: ISO/ASTM/EDANA/INDA/WSP/ERT/BS standards (Table 9.1), cited primary modelling literature (Backer–Petterson, Hearle, Freeston–Platt, Kozeny–Carman, Davies, Happel, Kuwabara, Mao–Russell, Lucas–Washburn), and measured constants (polymer thermal conductivity, Tables 9.5–9.8). Validity is high—it is the reference layer for the whole book.

||||||
|---|---|---|---|---|
|Standards review|Compilation of test standards|ISO/ASTM/EDANA/INDA|Tables 9.1–9.4|High (normative)|
|Analytical modelling|Structure→property equations|Cited literature|D'Arcy, Lucas–Washburn, Fourier, Poiseuille|Moderate–high (model-dependent)|
|Image analysis|FOD / pore measurement|Pourdeyhimi et al.|Image analyser|High for thin fabrics|

## 4. Argumentation Process

The logic is bottom-up: (1) define what governs performance (composition × structure); (2) characterise bond structures per route; (3) quantify dimensional/structural parameters (weight, thickness, FOD, porosity, pore size); (4) present the standards needed to measure them, including hygiene-specific ones; (5) detail measurement techniques (tensile, permeability, MVTR, wetting/absorption); (6) supply models that predict property from structure. The rhetorical move is encyclopaedic rigour—each property gets a definition, a standard, and (where mature) a predictive equation, building a verification toolkit for Ch6–8.

## 5. Role in the Book

Chapter 9 is the evaluative counterpart to the making chapters (6–8). It is where claims in those chapters become measurable: thermal-bond softness (Ch6) is tested by thickness/tensile/Mao–Russell models; chemical-binder migration (Ch7) by resin-distribution tests (WSP 150.1, §9.5.1); finishing barrier/rewet (Ch8) by permeability, MVTR, contact-angle and wiping-efficiency standards. It also introduces the FOD and pore-size concepts that later sections (and Pourdeyhimi's §9.22 image analysis) build upon. The chapter closes the Handbook's technical core before applications/material-specific chapters.

## 6. Strengths & Weaknesses

✅ Strengths:
- Hygiene-specific standards are explicitly catalogued (organotin extractables, Syngina, lamination strength, wiping efficiency, p.423).
- Clear distinction of wicking vs. demand absorbency (p.442) anchors absorbent-core fluid design.
- Strong modelling arsenal (Lucas–Washburn, Mao–Russell directional wicking, D'Arcy, Kozeny–Carman) with polymer constants (Table 9.7).

⚠️ Limitations / contestable points:
- Many models assume idealised geometries (cylindrical pores, parallel non-intersecting capillaries in mercury porosimetry, p.437; isotropic thin fabrics for FOD, p.431)—real hygiene webs are 3-D, anisotropic, and heterogeneous.
- SAP (superabsorbent polymer) behaviour—the heart of modern absorbent cores—is not modelled; the absorbency equation (9.39) treats the nonwoven, not the gel.
- "Because nonwovens are usually porous, heterogeneous and anisotropic in structure, the reliability of contact angle measurement is debatable, especially when the fabric is hydrophilic" (p.443)—an honest caveat that undercuts simple wettability QC.

## 7. Key Terms / Concepts

- Fibre orientation distribution (FOD/ODF): (p.411) "The frequency distribution (or statistical function) of the fibre orientation angles in a nonwoven fabric is called fibre orientation distribution (FOD) or ODF."
- Porosity: (p.408) "Fabric bulk density together with fabric porosity is important because they influence how easily fluids, heat and sound transport through a fabric."
- Specific (intrinsic) permeability — D'Arcy: (p.441) "v = –(k/η)(dp/dx), where v is the volumetric flow rate… η is the liquid viscosity… k is the specific permeability (m²)."
- Wicking vs. demand absorbency: (p.442) in-plane uptake = wicking; face-to-face uptake = "demand absorbency or spontaneous uptake."
- Wettability/contact angle: (p.442–443) "determined by the balance of surface energies in the interface between air, liquid and solid materials."
- Bubble point (largest pore-throat): (p.435) "a measure of the largest pore-throat in a sample… based on the Laplace equation of capillary pressure."
- Lucas–Washburn wicking: (p.453–454) capillary-rise equation modelling liquid advance in pores.
## 8. Micro close-reading

Paragraph (p.442, two liquid-transport modes):
> "There are two main types of liquid transport in nonwovens. One is the liquid absorption which is driven by the capillary pressure in a porous fabric and the liquid is taken up by a fabric through a negative capillary pressure gradient. The other type of liquid transport is forced flow in which liquid is driven through the fabric by an external pressure gradient. The liquid absorption that takes place when one edge of a fabric is dipped in a liquid so that it is absorbed primarily in the fabric plane is referred to as wicking. When the liquid front enters into the fabric from one face to the other face of the fabric, it is referred to as demand absorbency or spontaneous uptake."

- Sentence 1 ("Two main types of liquid transport"): Announces the dichotomy. Technique: classification opener.
- Sentence 2 ("One is the liquid absorption… negative capillary pressure gradient"): Defines passive mode—capillary-driven. Keyword: "negative capillary pressure gradient."
- Sentence 3 ("The other type… forced flow… external pressure gradient"): Defines active/forced mode. Logic: contrast.
- Sentence 4 ("The liquid absorption that takes place when one edge… absorbed primarily in the fabric plane is referred to as wicking"): Names the in-plane passive mode = wicking. Keyword: "fabric plane."
- Sentence 5 ("When the liquid front enters… from one face to the other face… demand absorbency or spontaneous uptake"): Names the through-plane passive mode = demand absorbency. Keyword: "one face to the other face."
💡 Standout line: "When the liquid front enters into the fabric from one face to the other face of the fabric, it is referred to as demand absorbency or spontaneous uptake"—the precise definition that separates ADL/wicking (in-plane) design from acquisition/core uptake (through-plane) design.

## 9. Concept deep-dive

Core concept 1 — Capillary wicking modelled by Lucas–Washburn and the directional Mao–Russell extension.
- Definition (p.453–454): capillary-rise/penetration governed by Laplace pressure (eq. 9.41), Hagen–Poiseuille flow (9.42), consolidated as Lucas–Washburn equations (9.43–9.48); the Mao–Russell model (9.50–9.54) extends this directionally for anisotropic nonwovens.
- Operational definition? Yes—explicit differential equations with defined variables (capillary pressure, viscosity, pore radius, contact angle, time).
- Usage in chapter: §9.18 capillary wicking, building on §9.11.4 wicking-rate measurement (upward strip test; GATS/MLDA; standards BS EN ISO 9073-6, WSP 10.1, ERT 10.4).
- Relation: links measured wicking rate to the pore geometry and contact angle established in §9.7 and §9.11.1.
- Academic origin: classical Lucas–Washburn (1930s) extended by Mao & Russell for nonwoven anisotropy.

Core concept 2 — Pore-size characterisation (apparent opening vs. pore-throat/bubble point).
- Definition (p.432, 435): apparent opening size (AOS, sieving) vs. constriction/pore-throat size; bubble point = largest pore-throat via Laplace (eq. 9.9: d = 4σ×10⁶/p).
- Operational definition? Yes—multiple standard methods (dry/wet/hydrodynamic sieving, bubble point, liquid-expulsion porometry, mercury porosimetry, image analysis) with ranges.
- Usage: §9.7; critical for filtration and for predicting liquid barrier/penetration (p.409) and absorbency.
- Relation: pore throat governs fluid-flow transport; connects to D'Arcy permeability (§9.16) and to SAP/core acquisition.
- Academic origin: Laplace capillarity; standardised geotextile/filter practice extended to nonwovens.

## 10. Academic critique & open questions

- The modelling section largely ignores the superabsorbent polymer (SAP) gel phase that dominates modern absorbent cores; equations describe the fibrous scaffold, not the swelled gel—an open modelling gap.
- Open question 1: Can the directional Mao–Russell wicking model (9.50–9.54) be extended to include SAP-containing composites where the pore space is progressively occluded by gel swelling?
- Open question 2: Given the stated unreliability of contact-angle measurement on hydrophilic, heterogeneous nonwovens (p.443), what surrogate in-line metric best predicts in-use rewet/wicking for coverstock QC?
- Scope: acoustic/filtration modelling (§9.20–9.21) is brief and less tied to hygiene than the fluid sections.
## 11. Hygiene-material relevance & action cards

Relevance: ★★★★★ — This chapter is the measurement and prediction toolkit for every hygiene metric: strike time, wicking rate, demand absorbency, re-wet, barrier, MVTR, lamination strength, and wiping efficiency; plus models to design ADL and core uptake.

ACTION CARD 1 — Specify and verify coverstock acquisition metrics
- Situation: Defining incoming-spec for a topsheet/ADL (p.402 fluid-handling list; p.423 wiping efficiency ASTM D6650/D6702).
- How to apply: Use §9.11.4 wicking-rate tests (upward strip; GATS/MLDA; BS EN ISO 9073-6, WSP 10.1) for in-plane spread and §9.11 demand-absorbency for through-plane uptake; track strike time and re-wet.
- Expected effect: Objective, standards-based acquisition/rewet spec instead of ad-hoc feel tests.

ACTION CARD 2 — Model ADL vs. core wicking with Lucas–Washburn / Mao–Russell
- Situation: Optimising fluid distribution in the absorbent assembly (p.442, p.453–454).
- How to apply: Treat ADL as in-plane wicking (Lucas–Washburn, eq. 9.43–9.48) and core uptake as through-plane demand absorbency; use the directional Mao–Russell model (9.50–9.54) for anisotropic sheets; input pore radius/contact angle from §9.7 and §9.11.1.
- Expected effect: Predict wicking distance vs. time; reduce wet-back by tuning pore structure and hydrophilicity.

ACTION CARD 3 — Characterise barrier/breathability of backsheet laminate
- Situation: Validating a film–nonwoven backsheet (cf. Ch8 lamination, p.385).
- How to apply: Measure specific permeability by D'Arcy (§9.16, eq. 9.35–9.36), MVTR (§9.10), and pore-throat via bubble point (§9.7.5, Laplace eq. 9.9); use polymer thermal conductivity (Table 9.7: PP 0.12, PE 0.34) if thermal modelling needed.
- Expected effect: Quantified leak-barrier vs. breathability trade-off for compliant backsheet.

## 12. Book-map quotes

"Fluid handling properties: permeability, liquid absorption (liquid absorbency, penetration time, wicking rate, re-wet, bacteria/particle collection, repellency and barrier properties, run-off, strike time), water vapour transport and breathability." — p.402 — the de-facto test menu for any absorbent hygiene product.

"When the liquid front enters into the fabric from one face to the other face of the fabric, it is referred to as demand absorbency or spontaneous uptake." — p.442 — the precise in-plane/through-plane distinction underpinning ADL vs. core design.

"Absorbent hygiene products — Syngina method (tampons); Ethanol-extractable organotin [WSP ERT 360.0-351.0]; Synthetic urine-extractable organotin II [WSP ERT 361.0-352.0]; Lamination strength; Wiping efficiency [ASTM D6650-01, D6702-01]." — p.423 — proof that standardised hygiene-specific test methods already exist.


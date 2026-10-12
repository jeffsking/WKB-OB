---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_47b0c74cf3725457026a2e6a89f7fbf6001a693ee6c0644e"
source_file: "ID · analysis_ch10.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch10.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch10.md.md

# Chapter 10 — Industrial Spray Drying Systems

## 1. Chapter Overview (范围、对象与定位)

Chapter 10 is the handbook's treatment of industrial spray drying — the unit operation in which a pumpable liquid or slurry feed is atomized into droplets and dried to individual particles in a hot gas stream, producing powders, granules, or agglomerates in a single pass. The chapter is authored by Filkova, Huang, and Mujumdar and is the most application- and equipment-breadth-rich chapter in this assignment: it opens with the principles (atomization hardware — rotary wheel, pressure, pneumatic, and novel nozzles; drop-size distributions and the Sauter mean D₃,₂; chamber shape and air–droplet contact modes; ancillary heaters/fans/cyclones; thermal efficiency), then surveys complete system layouts (open, closed, semiclosed/self-inertizing, and spray-plus-fluidizer combinations; single-, two-, and three-stage), then covers energy, safety, control, and selection, and closes with design procedures and CFD, plus a forward-looking §10.5 (superheated steam, horizontal two-stage, low-humidity/LDP, spray freeze drying, encapsulation, energy-efficiency). For the hygiene reader this is the SAP-isolation and binder-fines chapter: the text explicitly lists PVC emulsions and rubber latex among spray-dried products, and the two-stage spray + fluid-bed route and the encapsulation route are both directly usable for superabsorbent and wipe-active delivery. It is the upstream counterpart to Ch.8 (fluid-bed post-treatment) and the convective sibling to Ch.11/Ch.12.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

### Viewpoint 1 — Spray drying converts liquid polymer feeds into powders in one pass.

- Page: p.213
- Quote: > "Spray drying is a process in which a fluid feed is atomized into droplets that are dried to individual particles when moved in a hot gaseous drying medium, usually air."
- Interpretation: The defining feature — liquid in, powder out — is exactly the isolation step for polymer latices and superabsorbent solutions. No grinding required if the droplet is sized right.
### Viewpoint 2 — Polymer/surfactant products are explicitly within scope.

- Page: p.214
- Quote: > "Chemical industry, e.g., phenol–formaldehyde resin, catalysts, PVC emulsion-type, amino acids, etc. … numerous organic and inorganic chemicals, rubber latex, ceramic powders, detergents, and other products."
- Interpretation: PVC emulsion and rubber latex are named spray-dried products. For hygiene this is the latex/SAP-adjacent link: emulsion-polymerized binders (e.g., SBR/styrene-butadiene latex for wet wipes, acrylics) and PVC are isolated by spray drying; detergent/surfactant powders tie to wipe and absorbent-core actives.
### Viewpoint 3 — The Sauter mean diameter governs powder morphology.

- Page: p.217
- Quote: > "The so-called Sauter mean diameter seems to be the most suitable mean value to characterize the droplet cloud together with the size distribution. This is defined as the ratio of the total droplet volume to the total droplet surface … The Sauter mean diameter corresponds to the particle diameter with the same volume-to-surface ratio as the entire spray or powder sample."
- Interpretation: D₃,₂ sets drying time (surface/volume) and final particle size. For polymer solutions, higher molecular weight raises viscosity and shifts D₃,₂ upward — a first-order lever on SAP-fine size and binder-latex powder grade.
### Viewpoint 4 — The two-stage spray + fluid-bed is the agglomeration route.

- Page: p.239
- Quote: > "The semi dried powder is deposited on a moving belt (woven polyester filament) situated at the bottom of the primary spray chamber … After a short stabilization period … the powder is conveyed to the third drying stage … agglomerates with 'instant' properties."
- Interpretation: This is the milk-agglomeration layout, but structurally identical to SAP post-treatment: spray-dry to primary fines (Ch.10) → deposit/wet on a belt → fluid-bed second stage (Ch.8) to agglomerate into free-flowing granules. The chapter's own process logic is the SAP route.
### Viewpoint 5 — Superheated-steam spray drying eliminates fire/oxidation.

- Page: p.247
- Quote: > "No fire and explosion hazards … No oxidative damage … Better quality product under certain conditions … Closed system operation to minimize air pollution."
- Interpretation: For thermally fragile, oxygen-sensitive hygiene polymers (cellulose pulp fines, starch carriers, some SAP grades), steam-medium spray drying removes both explosion risk and yellowing — a decisive advantage over hot-air drying for heat-sensitive actives.
### Viewpoint 6 — Encapsulation delivers actives via an oil-in-water emulsion.

- Page: p.253
- Quote: > "The active material to be encapsulated, such as an oil or flavor in an oil base, is dispersed in a hydrocolloid carrier, e.g., gelatin, modified starch, dextrin or maltodextrin, or gum arabic … homogenized to form an oil-in-water emulsion, and then it is fed to the atomizer for spray drying. In the dryer chamber, the aqueous phase dries and the active material is entrapped as particles within the hydrocolloid or protein film."
- Interpretation: Microencapsulation of oils/actives (fragrances, skin-care actives, antimicrobials for wipes/sanitary) is a one-step spray process using hydrocolloid walls. Directly relevant to wipe "feel" and controlled-release actives.
## 3. Research Method & Data Sources

The chapter is a review + design-synthesis. Method per layer:

||||||
|---|---|---|---|---|
|Principles / atomization|Force/geometric & empirical correlations|Masters, Filkova, Gauvin–Katta (refs 4,5,10,23)|Eq 10.1–10.14, Tables 10.2–10.3|Validated for Newtonian; non-Newtonian flagged (ref 9)|
|Drop-size statistics|Lognormal / Rosin–Rammler fitting|Experimental (Fig 10.2)|Eq 10.2–10.4|Distribution-fit only|
|Chamber design|Geometry + air-contact regimes + wall-impingement rule|Kessler, Masters (Fig 10.13–10.19)|Layout rules|"prevent baking on" heuristic|
|Systems|Layout taxonomy + safety/control/selection|Industrial practice (Table 10.6)|Flow diagrams|Per-product; pilot mandatory|
|Design / CFD|Empirical drying-intensity + droplet diffusion|Huang et al. (Eq 10.20–10.21)|CFD (Fig 10.47)|"accuracy of CFD models still not well defined"|

No new primary experiments; validity bounded by explicit caveats (e.g., CFD accuracy undefined, p.245; non-Newtonian feed needs accurate correlations, p.221).

## 4. Argumentation Process

- Premise A: Any pumpable liquid can be atomized and dried to powder in one pass — universal applicability (§10.1).
- Premise B: Final particle size is set at atomization (D₃,₂, drop-size distribution), so the atomizer choice controls product (§10.2.2).
- Premise C: Chamber geometry and air–droplet contact mode (co-/counter-/mixed-flow) decide wall impingement, residence time, and product quality (§10.2.3).
- Step: Because single-pass spray drying is energy-hungry and leaves internal moisture, the chapter surveys system layouts (open/closed/semiclosed, single/two/three-stage, spray+fluidizer) to trade off safety, energy, and agglomeration (§10.3).
- Resolution: Select via the material questionnaire (aqueous vs solvent, heat-sensitive, explosive, Tg, hygroscopicity — p.244–245), size by empirical drying-intensity + CFD, and confirm in pilot (§10.4–10.5). The logic is characterize-feed → choose-layout → size → pilot, which is exactly the SAP/latex dry-powder decision.
## 5. Role of This Chapter in the Book

Ch.10 is the liquid-feed counterpart to Ch.7 (rotary, granular), Ch.8 (fluid-bed, granular/post-treatment), Ch.11 (freeze, heat-sensitive biochemicals), and Ch.12 (dielectric, thick/absorbent cores). It is the upstream isolation step for SAP and binder latex that Ch.8 then agglomerates; its two-stage spray + fluidizer line (p.239) is the literal bridge to Ch.8. For hygiene, Ch.10 supplies the "make the powder" half of the SAP route and the encapsulation route for wipe actives; Ch.4 (thermodynamics/isotherms) and Ch.3 (diffusivity) feed its modeling.

## 6. Strengths & Weaknesses

✅ Strengths (with quote):
- Breadth of layouts with concrete operating data — "Spray Dryer Layouts … Closed cycle: Inert gas and nonaqueous … Semiclosed (self-inertizing): Air with low O₂ content … Combination Spray and fluidizer … Improved energy consumption, reduced capital costs" (p.234–235).
- Honest about modeling limits — "We are currently unable to express precisely the spray–air contact, the powder trajectories, and airflow patterns … specification and design of spray dryers are still based on the pilot tests and existing industrial experience" (p.244, p.245).

⚠️ Limitations / contestable points (with quote):
- CFD treated as maturity it does not yet have — "accuracy of CFD models are still not well defined" (p.245) sits awkwardly beside strong CFD-visual claims (Fig 10.47).
- Drop-size correlations assumed Newtonian; the chapter flags but does not resolve "a knowledge of the feed properties is needed" (p.221) for polymer solutions — exactly the hygiene case (non-Newtonian SAP/slurry feeds; ref 9, Filkova non-Newtonian liquids).

## 7. Key Terms / Concepts

- Atomization: (p.217) "a fluid feed is atomized into droplets that are dried to individual particles" — the size-setting step.
- Sauter mean diameter D₃,₂: (p.217) "the ratio of the total droplet volume to the total droplet surface"; particle with same volume-to-surface ratio as whole spray.
- Lognormal / Rosin–Rammler: (p.218) "the most common distributions used in the spray drying"; Table 10.3 gives droplet/particle sizes (rotating wheels 1–600 µm, chemicals 10–1000 µm).
- Cocurrent / countercurrent / mixed-flow: (p.226) air–droplet contact modes; cocurrent keeps product cooler (heat-sensitive), countercurrent gives higher thermal efficiency.
- Wall-impingement / melting-point rule: (p.224) hot-air distribution "must prevent [wall impingement] … [air temp] be lower than the melting point of the product to prevent baking on."
- Open / Closed / Semiclosed cycle: (p.234) closed uses inert gas for solvent/explosive feeds; semiclosed self-inertizes with low-O₂ air.
- Spray + fluidizer (two/three-stage): (p.234–239) spray pre-dries, fluid bed finishes internal moisture and agglomerates.
- Glass-transition temperature (product spec): (p.245) listed among dry-product properties to "List … glass transition temperature, hygroscopicity, powder flammability" — directly the polymer-Tg gate for spray-dried SAP/latex.
- Encapsulation: (p.253) oil-in-water emulsion dried so active is "entrapped as particles within the hydrocolloid or protein film."
## 8. Micro Close-Reading (ONE key paragraph)

Selected paragraph — Encapsulation mechanism (p.253):

"The active material to be encapsulated, such as an oil or flavor in an oil base, is dispersed in a hydrocolloid carrier, e.g., gelatin, modified starch, dextrin or maltodextrin, or gum arabic. After the emulsifier is added, the mixture must be homogenized to form an oil-in-water emulsion, and then it is fed to the atomizer for spray drying. In the dryer chamber, the aqueous phase dries and the active material is entrapped as particles within the hydrocolloid or protein film. The active material from the capsule is released under specified conditions. The main controlling factors of its release are temperature, moisture, and pressure."

- Sentence 1 (function: defines the core + lists wall materials): establishes that the active is protected by a hydrocolloid wall — gelatin/modified-starch/dextrin/maltodextrin/gum-arabic, all polysaccharides/proteins.
- Sentence 2 (technique: process sequence): emulsify → homogenize → atomize; the emulsion state is what makes a stable capsule, not the dryer alone.
- Sentence 3 (keyword: "aqueous phase dries"): the drying step only removes water; the oil-active stays inside the coalesced film — a skin-formation event at the droplet surface.
- Sentence 4 (logic relation: consequence): the wall is what enables entrapment; product = matrix particle.
- Sentence 5 (rhetorical move: closes the loop to function): release is trigger-controlled (T, RH, P) — i.e., the wall is a delivery device.
- 💡 Standout line: "The active material … is released under specified conditions. The main controlling factors of its release are temperature, moisture, and pressure" — the spray dryer makes not just a powder but a controlled-release device, the exact mechanism wanted for wipe/sanitary actives.
## 9. Concept Deep-Dive

### Core concept A — Atomization & D₃,₂ (§10.2.2)

- Definition (p.217): "The so-called Sauter mean diameter seems to be the most suitable mean value to characterize the droplet cloud … ratio of total droplet volume to total droplet surface."
- Operational definition? Yes — directly measurable from size distribution; drives drying rate (∝ surface) and final particle size.
- Usage in THIS chapter: wheel (Eq 10.7, peripheral velocity ~150 m/s, p.220), pressure nozzle (Eq 10.9–10.11, pressure-driven), pneumatic (compressed air 0.15–0.8 MPa, p.222); each correlation predicts D₃,₂ from feed/operating variables.
- Relation: D₃,₂ links atomizer choice → particle size → residence-time/thermal load; for polymers, viscosity (∝ MW, PoP Xn) shifts D₃,₂.
- Academic origin: Masters (Spray Drying, 1979); Filkova nozzle atomization (Advances in Drying, 1984).
### Core concept B — System layout & two-stage agglomeration (§10.3)

- Definition (p.234): layouts include Combination Spray and fluidizer — "Improved energy consumption, reduced capital costs."
- Operational: explicitly a process route, not just equipment.
- Usage: two-stage milk agglomeration (p.239) deposits semi-dried powder on a belt into a fluid bed — the SAP post-treatment template.
- Relation: bridges Ch.10 (primary powder) → Ch.8 (fluid-bed granulation/cooling).
### Core concept C — Superheated-steam & LDP spray drying (§10.5.1, §10.5.3)

- Definition (p.247): steam medium gives "No fire and explosion hazards … No oxidative damage." LDP (p.249) uses "low dew point (LDP) air at near ambient temperature to 80°C, but with very low humidity."
- Operational: alternative media for heat-/oxygen-sensitive feeds.
- Usage: steam for explosive/solvent feeds; LDP for pharma/biochemicals at low T (p.249).
- Relation: steam route dovetails with Ch.8 superheated-steam FBD; both serve oxidation-sensitive hygiene carriers.
## 10. Academic Critique & Open Questions

- Theoretical gap: droplet drying models (Eq 10.21, @C/@t = (1/r²)@/@r(r² D @C/@r)) assume constant D (diffusivity). For polymer solutions the effective D drops sharply with concentration/MW during skin formation — the model under-predicts crusting. No concentration-dependent D is offered.
- Methodological gap: non-Newtonian and viscoelastic SAP/slurry feeds are flagged (ref 9) but no sizing guidance is given — the dominant hygiene feed class is under-served.
- Open question 1: For crosslinked polyacrylate feeds (SAP precursor), how does crosslink density (gel point, PoP) interact with atomizer shear to set primary-fine size and agglomerate dispersibility?
- Open question 2: Can superheated-steam or LDP spray drying preserve the swell capacity / Tg of thermally fragile SAP grades better than hot-air cocurrent — and at what energy premium?
## 11. Hygiene-Material Relevance & Action Cards

Relevance rating: ★★★★★ — this is the SAP-isolation, binder-latex, and active-encapsulation chapter.

H11.1 — Isolate emulsion-polymerized SAP/latex by spray drying. Situation: converting a sodium-polyacrylate or SBR/acrylic latex into a free-flowing powder. Apply: per p.214, PVC-emulsion and rubber-latex are standard spray-dried products; choose pressure/rotary atomizer and set D₃,₂ (p.217) for target fine size; watch wall-impingement/melting rule (p.224). Effect: one-pass powder, no milling; primary fines then agglomerated in Ch.8 fluid bed. ★★★★★

H11.2 — Route SAP fines through the two-stage spray + fluidizer. Situation: need agglomerated, dust-free SAP granules. Apply: per p.239, deposit semi-dried spray powder onto a belt into a fluid bed for second-stage drying/agglomeration. Effect: "instant"-type agglomerates with controlled porosity — the diaper-core granule. ★★★★★

H11.3 — Encapsulate wipe/sanitary actives. Situation: deliver fragrance, skin-care, or antimicrobial actives with controlled release. Apply: per p.253, disperse active in oil, emulsify in hydrocolloid (modified starch/gum arabic) oil-in-water, spray dry; release triggered by T/RH/pressure. Effect: stable, trigger-released actives in wipe or topsheet. ★★★★

H11.4 — Use superheated-steam / LDP for oxidation-sensitive carriers. Situation: drying cellulose-pulp fines, starch, or heat-sensitive SAP grade. Apply: per p.247 / p.249, steam medium removes oxidative damage; LDP allows 80°C drying at very low humidity. Effect: no yellowing, lower thermal load on fragile polymers. ★★★★

H11.5 — Close the cycle for solvent-based polymer solutions. Situation: spray-drying a non-aqueous polymer dope (explosion/solvent-recovery risk). Apply: per p.234, use closed cycle with inert gas for evaporation/recovery, or semiclosed self-inertizing for explosive powders. Effect: safe, emissions-controlled isolation of solvent-borne SAP/precursor. ★★★★

## 12. Book-Map Quotes (Top representative quotes)

- p.214 — "numerous organic and inorganic chemicals, rubber latex, ceramic powders, detergents, and other products." — anchors polymer latex/surfactant powders in spray-drying scope.
- p.239 — "agglomerates with 'instant' properties" (two-stage spray + belt + fluid bed) — the SAP post-treatment template bridging Ch.8.
- p.253 — "the active material is entrapped as particles within the hydrocolloid or protein film … released under specified conditions" — spray drying as controlled-release device for hygiene actives.

---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_62062ff28e81020cb2703aac8d2db9ce001a693ee6c0644e"
source_file: "ID · analysis_ch41.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch41.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch41.md.md

# Chapter 41 — Drying of Polymers

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 41 (Mujumdar & Hasan) is the Handbook's dedicated "drying of polymers" chapter and the mechanistic home chapter for resin- and pellet-scale drying of the very plastics used in hygiene materials — polyolefins (PP, PE backing film and nonwovens), PET and nylon (spunbond/nonwoven topsheet and fibers), PVC, ABS and polycarbonates. The authors open by framing polymer drying as the solid-handling tail of polymerization recovery (after unreacted-monomer salvage, coagulation, devolatilization, liquid–solid separation) and warn that selection is proprietary and case-specific. The chapter surveys polymerization routes (bulk/solution/suspension/emulsion/gas-phase), classifies dryers by heat-transfer mode, residence time and physical form, catalogs 10 dryer families, then walks through drying systems for polyolefins, PVC, ABS, synthetic fibers (nylon, PET) and miscellaneous resins. It closes with resin classification (hygroscopic vs nonhygroscopic), desiccant-dryer design, and — critically — a devolatilization paragraph that is the single most SAP-relevant passage: residual monomer is removed above the glass transition temperature.

## 2. Key Viewpoints (with verbatim quotes + print pages)

### Viewpoint 1 — Polymer drying is the solid-handling tail of polymerization recovery

- Page: p.951
- Quote: "Drying is one of the prime polymer recovery operations performed before transfer to the compounding plant or packaging for direct use. It is the part of the process in which the polymer is handled essentially as a solid and liquid and gas streams become relatively minor."
- Interpretation: Sets the frame: drying removes residual volatiles (monomer, solvent, water, by-products), so the feed state is fixed by upstream polymerization. For hygiene buyers this means resin moisture/monomer spec is set by the polymerization route, not the dryer alone.
### Viewpoint 2 — Drying sits downstream of a chain of recovery operations including devolatilization

- Page: p.951
- Quote: "In polymer production, other recovery operations include salvation [salvage] of the unreacted monomer and solvent, coagulation and precipitation, concentration and devolatilization, and liquid–solid separation[1]."
- Interpretation: Residual monomer/solvent is a feed property the dryer must cope with; the chapter later (p.977) names devolatilization as the dedicated unit op for separating volatiles from bulk polymer — directly the mechanism governing SAP residual-acrylic-acid control.
### Viewpoint 3 — Dryer selection is governed by upstream physical state, not by polymer chemistry alone

- Page: p.955
- Quote: "The primary step in specifying a dryer is to define the physical, thermal, and chemical properties of the product and the volatiles present. Often the consistency of the feed reduces the choice of dryer. A few guidelines are helpful… if a solvent must be evaporated and then recovered, it is usually not desirable to choose a convection dryer."
- Interpretation: Feed consistency (solution/slurry/cake/pellet) and volatiles (flammable solvent vs water) pre-select the dryer. This is why PP (hexane-wet) needs closed-loop N₂, while E-PVC (water-wet slurry) uses spray drying.
### Viewpoint 4 — Devolatilization (residual-monomer removal) is performed above Tg

- Page: p.977
- Quote: "It is well known that most polymers leaving the polymerization reactor contain various but small amounts of unreacted monomer, solvents, water, and/or various reaction by-products. The presence of these volatiles in the polymer is undesirable. Their concentrations may range from several parts per million to several tens of percentage. … This process of devolatilization is usually performed above the glass transition temperature of the polymer."
- Interpretation: THE home statement for SAP. Residual (unreacted) monomer is an unavoidable polymerization artifact whose removal is a separate thermal step run above Tg so the polymer chain has enough free volume for diffusion. Chapters-prior SAP-making routes produce residual acrylic acid/monomer precisely because chain polymerization never reaches 100% conversion; stripping it requires Tg-controlled heating. [inference] This paragraph is the bridge from Odian's "unreacted feedstock" to a dryer spec.
### Viewpoint 5 — Two-stage systems dominate because surface and bound moisture need different treatment

- Page: p.967
- Quote: "Since ABS requires both surface and bound moisture removal, a two-stage drying system is recommended."
- Interpretation: A general design rule repeated across PP (flash + FBD), S-PVC (flash + FBD), E-PVC (spray + FBD), PET (crystallizer + column). The first stage removes free/surface moisture fast and adiabatically; the second controls bound moisture at a safe product temperature. Relevant to any hygiene-polymer drying line.
### Viewpoint 6 — Hygroscopic resins hold moisture inside the pellet and demand desiccant (very low dew point) drying

- Page: p.972
- Quote: "PET, nylon, ABS, and PC come under the classification of hygroscopic resins. These types of polymer resin collect moisture inside the pellet itself. Removal of this moisture requires dry air as well as heat. … Desiccant dryers are the dominant technology for these resins."
- Interpretation: Distinguishes surface (nonhygroscopic PP/PE/PS) vs internal (hygroscopic) moisture. For PET/nylon the moisture is diffusion-limited inside the pellet, so dew point — not just temperature — sets the floor. PET needs −40 to −50°C dew point (p.973). Directly transferable to drying any hygroscopic hygiene polymer.
## 3. Research Method & Data Sources

Theory-led equipment review with embedded industrial benchmark tables and process-flow schematics; no independent experiments.

||||||
|---|---|---|---|---|
|Polymerization-route survey|Descriptive comparison of bulk/solution/suspension/emulsion/gas-phase|Driver (1979), Lenz (1967)|Narrative|Conceptual framing|
|Dryer classification|Taxonomy by heat-transfer mode, residence time, physical form|Mujumdar (1981–84), Dittman (1977)|Typology|Industry-recognized|
|Per-polymer systems|Case studies of actual dryer trains (PP, PVC, ABS, nylon, PET)|Glanvill (1974), Herron & Hammel (1980), Eberspacher (1980), Bepex (1983)|Flow diagrams, Tables 41.1–41.2|Representative vendor/plant practice|
|Devolatilization theory|Literature pointer to Albalak (1996)|Albalak (Ed.), Polymer Devolatilization|Referral|Cited, not developed here|

## 4. Argumentation Process

- Framing — drying = recovery tail; selection is proprietary/hard (p.951).
- Upstream determinism — polymerization physical system dictates feed state and dryer class (p.951–955).
- Dryer taxonomy — indirect vs direct; residence-time bands; other considerations (consistency, volatiles, temperature ceiling, particle size) (p.955–961).
- Dryer catalog — 10 families with operating principles, advantages, limits (p.956–961).
- Worked systems — polyolefins → PVC → ABS → synthetic fibers → miscellaneous, each showing two-stage logic and ppm-level specs (p.961–971).
- Resin-level rules — hygroscopic vs nonhygroscopic; desiccant design; vented-barrel; SPP/PET (p.971–976).
- Conclusion — many dryers fit; operate at correct gas conditions; new tech (pulsed bed, superheated steam) emerging; devolatilization requires Tg (p.976–977).
## 5. Role in the Book

Ch41 is the Handbook's polymer-specific drying chapter and pairs with Ch35 (pulp/paper), Ch33 (fibrous materials), Ch40 (coated webs) and Ch42 (enzymes). Where Ch35 treats cellulosic web drying and Ch33 the fibre–water molecular physics, Ch41 treats granular/pellet/powder polymer resins — the feedstocks of hygiene films (PE/PP), nonwovens (PP/PET/nylon) and, by mechanism, superabsorbent polyacrylate. It is the natural counterpart to Ch40 (thin liquid layer on substrate) in that both deal with polymers + volatiles, but Ch41 works on the solid particle scale.

## 6. Strengths & Weaknesses

✅ Strengths: Unusually complete dryer catalog (10 families + proprietary designs), a quantitative Table 41.1 of permissible moisture per resin, explicit two-stage logic, and the only Handbook statement tying devolatilization to Tg (p.977). The PP closed-loop N₂/hexane-recovery and PVC  ppm VC-emission constraints (p.966) are procurement-grade.
⚠️ Limitations/contestable: The chapter is a 2006-vintage review (copyright "(cid:2)2006"); "over 250 U.S. patents… 80 patents annually in the EC" and "new technologies… will eventually replace conventional dryers in the next decade or two" (p.977) are dated speculative claims. No superabsorbent polymer (SAP) is named anywhere — the devolatilization/Tg principle is transferable by inference only. OCR artifacts are present (e.g., "308C" at p.955; "DRT/backmix" and "constant rate/falling rate" labels scrambled in Figure 41.6 at p.963). No diffusion model, no Fickian falling-rate derivation, no explicit Flory–Rehner or crosslink discussion.

## 7. Key Terms / Concepts

- Devolatilization: p.977, "process of devolatilization is usually performed above the glass transition temperature of the polymer"; purpose: "improve polymer properties, to recover monomer and solvents, to meet health and environmental regulations, to eliminate odors, and/or to increase the extent of polymerization."
- Residual monomer/solvent: p.977, "concentrations may range from several parts per million to several tens of percentage."
- Permissible moisture (db): p.962, Table 41.1 — e.g., PP 0.05%/0.03–0.10%, HDPE 0.05–0.10%/0.03–0.05%, PET (not listed directly) but nylon 0.04–0.08%/0.02–0.06%, PC max 0.02/0.02.
- Hygroscopic vs nonhygroscopic resins: p.972, nonhygroscopic (PE, PS, PP) "collect moisture on the surface of the pellet only"; hygroscopic (PET, nylon, ABS, PC) "collect moisture inside the pellet itself."
- Equilibrium moisture content (EMC): p.972, "If the material is exposed to a certain temperature and relative humidity for a period of time, it will reach the equilibrium point, referred to as the equilibrium moisture content (EMC)."
- Permeability (to water vapor): p.972, "product of the diffusion constant of water vapor–polymer system and the solubility coefficient."
- Two-stage drying: recurring p.963/965/967/970 — fast surface-moisture stage + controlled bound-moisture stage.
- Constant-rate vs falling-rate: p.961/963, Figure 41.6 "Break point: constant rate/falling rate"; between 35% (wb) and 5% (wb) S-PVC "exhibit constant-rate drying characteristics."
- Dew point for hygroscopic resins: p.973, "PET absolutely requires dew points in the −40 to −50°C range"; others "−15 to −25°C are adequate."
- Glass transition temperature (Tg) gate for devolatilization: p.977.
## 8. Micro close-reading (ONE key paragraph)

p.977 (Conclusion, devolatilization clause):
> "It is well known that most polymers leaving the polymerization reactor contain various but small amounts of unreacted monomer, solvents, water, and/or various reaction by-products. The presence of these volatiles in the polymer is undesirable. Their concentrations may range from several parts per million to several tens of percentage. Their separation from bulk polymer is necessary to improve polymer properties, to recover monomer and solvents, to meet health and environmental regulations, to eliminate odors, and/or to increase the extent of polymerization. This process of devolatilization is usually performed above the glass transition temperature of the polymer."

Sentence-by-sentence: (1) Premise — every commercial polymer exits the reactor with residual volatiles; this is universal, not exceptional. (2) Normative — their presence is "undesirable," establishing the quality driver. (3) Magnitude — residual level spans ppm to tens of percent, i.e., both trace-odor and bulk-solvent regimes. (4) Objectives — six reasons to strip volatiles: property, recovery, regulation, odor, and increased polymerization extent (the last implies unreacted monomer caps conversion). (5) Mechanism — devolatilization runs above Tg, because below Tg the glassy polymer has too little free volume for the volatile to diffuse out.
💡 Standout line: "This process of devolatilization is usually performed above the glass transition temperature of the polymer" — the entire SAP residual-acrylic-acid / free-monomer control principle in one clause.

## 9. Concept deep-dive

Devolatilization above Tg = the SAP residual-monomer mechanism. The only quantitative-ish devolatilization statement (p.977) is that it "is usually performed above the glass transition temperature of the polymer." In free-radical/ emulsion polymerization of acrylic acid–based SAP, conversion never reaches 100% (Odian, radical chain; gel effect at high conversion), so residual unreacted monomer and free acrylic acid remain in the gel. Stripping them is a diffusion-limited devolatilization step: heat the crosslinked gel above its effective Tg (plasticized by water) so free volume opens, letting residual monomer diffuse to the surface and desorb. The chapter gives no rate law, but the direction — raise temperature above Tg, control residence time, recover/vent the volatile — is exactly the SAP post-reaction drying/stripping logic. [inference] A too-low temperature leaves residual monomer trapped (glassy state); a too-high temperature risks thermal crosslinking that permanently shrinks the network and lowers swell capacity (the inverse of Ch35's hornification clause).

Two-stage architecture as a universal template. Across PP (flash + plug-flow FBD, p.963), S-PVC (flash + FBD, p.965), E-PVC (spray + FBD, p.964), ABS (flash + FBD/rotary, p.967), PET (fluid-bed crystallizer + column, p.973) the same logic recurs: stage 1 = fast removal of free/surface moisture (often adiabatic, near the boiling point, short residence); stage 2 = bound-moisture removal at a controlled, lower product temperature with longer residence. For SAP gel, the analog is a high-rate predry (surface water off) followed by a gentle, Tg-aware finishing dry that strips monomer without over-crosslinking.

Dew-point-limited hygroscopic drying. p.973: "PET absolutely requires dew points in the −40 to −50°C range to be adequately dried. For other hygroscopic resins, dew points in the range of −15 to −25°C are adequate." The moisture floor is set by the gas dew point, not by temperature alone, because internal moisture equilibrates with the drying gas (EMC, p.972). For a moisture-sensitive hygiene polymer this is the levers: desiccant (molecular sieve) beats silica gel at low inlet moisture (p.973, "produces 1000 kcal/kg of moisture absorbed") and reaches lower dew points.

Pellet vs powder vs cake morphology drives dryer choice. Nonhygroscopic PP/PE/PS are pellet-surface wet (p.972); E-PVC is a water-wet slurry spray-dried to powder (p.964); S-PVC and ABS are centrifuge cakes (20–25% wb, p.965; 50% wb, p.967); PET/nylon are 3–4 mm cubic pellets/chips (p.968). Feeding rule (p.956): "Lumpy or pasty polymer must be broken up or mixed with dry product recycle to produce a more uniform and free-flowing feedstock." SAP gel and crumb sit between cake and powder — the chapter's cake-handling rules (venturi deagglomeration, low duct velocity, shear sensitivity for PVC, p.965–966) directly inform SAP crumb feeding.

## 10. Academic critique & open questions

- The chapter is a 2006 review; its "next decade or two" prediction for pulsed-bed/superheated-steam adoption (p.977) is unverified against current practice and should be re-checked.
- No diffusion model: falling-rate period is asserted (constant→falling break, p.963) but never derived from Fick's law; no effective-diffusivity, no activation energy for moisture diffusion in polymers.
- No SAP, no free-acrylic-acid, no crosslink-density/swell discussion — the devolatilization paragraph is the only conceptual bridge, by inference.
- Open question 1: Can the Tg gate for devolatilization (p.977) be quantified for a water-plasticized crosslinked polyacrylate gel — i.e., what residence time at what (water-content-dependent) temperature strips residual monomer to a skin-safety ppm without thermally crosslinking the network?
- Open question 2: Does the chapter's two-stage (fast surface + slow bound) template map onto SAP gel drying such that stage-2 temperature can be bounded by a measurable Tg rather than by trial-and-error discoloration?

## 11. Hygiene-material relevance & action cards

Overall relevance: ★★★★★ (mechanistic home chapter for SAP + PE/PP/PET/nylon resins).

Action Card H41-1 — Specify the residual-monomer strip as a Tg-aware step, not merely "drying." Insight: p.977 devolatilization "is usually performed above the glass transition temperature of the polymer"; residual volatiles "range from several parts per million to several tens of percentage." Action: For SAP or acrylic-based superabsorbents, require the supplier's finishing step to state temperature vs (water-plasticized) Tg and residence time, and demand a residual free-acrylic-acid / residual-monomer CoA (skin-safety ppm). → 卫材相关性★★★★★｜Directly governs residual-monomer/free-acrylic-acid skin safety and the conversion left in the gel.

Action Card H41-2 — Bound the finishing temperature to avoid thermal crosslinking that kills swell capacity. Insight: p.977 devolatilization above Tg; [inference] over-temperature drives additional crosslinking (network shrinkage) exactly as Ch35's hornification welds cellulose. Action: Set a supplier spec ceiling on final-stage temperature and verify swell capacity / absorbency-under-load on incoming lots; trend it lot-to-lot. A falling swell number signals over-crosslinking from an over-hot finishing dry. → 卫材相关性★★★★★｜Thermal crosslinking in the dry step is a silent swell-capacity killer for SAP.

Action Card H41-3 — Use the two-stage template for any hygiene-polymer dry line. Insight: p.967 "Since ABS requires both surface and bound moisture removal, a two-stage drying system is recommended"; repeated for PP, S-PVC, E-PVC, PET. Action: When qualifying a resin or SAP supplier, confirm a fast surface-predry + a gentle bound-moisture finishing stage rather than a single high-temperature pass. → 卫材相关性★★★★★｜Single-stage overheating is the root cause of both residual monomer and crosslink damage.

Action Card H41-4 — For PE/PP backsheet & nonwoven resin, control final moisture to Table 41.1 spec. Insight: p.962 Table 41.1 — PP permissible moisture 0.05% (injection)/0.03–0.10% (extrusion), drying temp 71–93°C; HDPE 0.05–0.10%/0.03–0.05%, 71–104°C; PP is "solvent wet" from hexane (p.962) and closed-loop N₂ is used to reach ~500 ppm solvent (p.963). Action: Require CoA moisture ≤ Table 41.1 limits and confirm nonhygroscopic (surface) moisture is removed pre-extrusion to avoid bubbles/voids in film. → 卫材相关性★★★★★｜Resin moisture spec is the quality gate for film/nonwoven extrusion.

Action Card H41-5 — For PET/nylon nonwoven, demand desiccant (very low dew point) drying. Insight: p.972 PET/nylon are hygroscopic (moisture inside pellet); p.973 "PET absolutely requires dew points in the −40 to −50°C range"; p.971 PET must reach 0.005% db and "can have absolutely no exposure to atmosphere between drying and processing." Action: For spunbond/nonwoven feedstock, require dew-point certificate and sealed transfer; reject lots showing hydrolysis brittleness. → 卫材相关性★★★★★｜Internal moisture hydrolyzes PET during melt spinning; dew point is the real control.

Action Card H41-6 — Watch PVC/VC emission and monomer residuals if using PVC-based hygiene films. Insight: p.966 "U.S. EPA emission limitations of  ppm on VC must be strictly maintained"; p.966 monomer chloride "induces pitting corrosion and stress corrosion cracking." Action: If a supplier runs PVC, verify VC-emission compliance and residuals; this dictates allowed dryer type. → 卫材相关性★★★★☆｜VC monomer residual is both a regulatory and a film-integrity issue.

Action Card H41-7 — Use ppm-level solvent-residual spec for any solvent-polymerized hygiene resin. Insight: p.963 PP dried in N₂ FBD "contains an extremely low level of solvent (e.g., hexane or heptane), typically 500 ppm"; p.957 superheated-vapor fluidization recovers solvent efficiently. Action: Require residual-solvent CoA (≤ a few hundred ppm) for solvent-made PP/PE grades used in skin-contact layers. → 卫材相关性★★★★☆｜Residual solvent is an odor and skin-safety parameter for film layers.

## 12. Book-Map Quotes (Top representative quotes)

"This process of devolatilization is usually performed above the glass transition temperature of the polymer." — p.977 — the SAP residual-monomer home statement.
"PET, nylon, ABS, and PC come under the classification of hygroscopic resins. These types of polymer resin collect moisture inside the pellet itself. Removal of this moisture requires dry air as well as heat." — p.972 — the internal-moisture / desiccant rule.
"Since ABS requires both surface and bound moisture removal, a two-stage drying system is recommended." — p.967 — the universal two-stage template.


---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_e01e528a0ccbd24e14d907291c8ef863001a693ee6c0644e"
source_file: "ID · analysis_ch40.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch40.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch40.md.md

# Chapter 40 — Drying of Coated Webs

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 40 (Hung, Wimberger & Mujumdar) is the Handbook's reference for drying a thin liquid layer on a moving substrate — the exact physics behind lotion/emulsion coating on wipes and adhesive/coating lines on hygiene films and tapes. It opens by classifying coated webs (paper/paperboard, plastic films & tapes, metallic sheets) and coating forms (solventborne, waterbased, 100% solids), then builds the drying-curve framework: adjustment → constant-rate → falling-rate, with the crucial note that water-based latex coatings hold a longer constant-rate than solventborne. The technical core is air-impingement and flotation dryer design (air bars, slots, cushion pressure, web stability), augmented by IR, UV and EB curing. It closes with application examples (paper coating, PVDC barrier, pressure-sensitive adhesives) and an extensive safety section (LEL, inert-gas drying, VOC recovery/incineration). Throughout, the authors tie drying-rate scheduling to final coating morphology — mottle, binder migration, skinning, blistering, curl.

## 2. Key Viewpoints (with verbatim quotes + print pages)

### Viewpoint 1 — A coated web is a thin liquid layer whose final morphology is set by the drying curve

- Page: p.931
- Quote: "Because of the product quality problems associated with the drying process, the proper quantity of heat and mass transfer has to be applied to the coating at the proper time in the drying curve."
- Interpretation: Drying is not just water/solvent removal; the schedule of heat and mass transfer through the three curve stages dictates defects and final film properties. For a lotion-coated wipe this is the governing design principle.
### Viewpoint 2 — Latex (water-based) coatings keep a longer constant-rate than solventborne

- Page: p.931
- Quote: "the drying curve of water-based latex coatings has a longer constant drying rate than solvent-based coatings. Paper has a drying curve with a short warm-up period and a constant drying rate period even longer than latex coatings."
- Interpretation: The constant-rate period is the safe, fast-evaporation window; water/latex systems exploit it longer. Emulsion/lotion coatings on wipes behave like latex — a longer benign constant-rate before the defect-prone falling-rate zone.
### Viewpoint 3 — Over- or rapid drying creates the classic coating defects

- Page: p.931
- Quote: "Over-drying or rapid drying can cause brittleness, blistering, curl, and wrinkles. Brightness, ink receptivity, and varnishability can be reduced. Nonuniform moisture profile… can sometimes also be attributed to drying conditions."
- Interpretation: Defect vocabulary (blistering, curl, wrinkles, brittleness) is exactly what a converting line qualifies against. Fast surface drying is the enemy of uniform film.
### Viewpoint 4 — Binder migration and mottle are governed by the preheat/constant-rate stages

- Page: p.931
- Quote: "most coated papers are intended for printing, and binder migration causing printing mottles should be eliminated or minimized during drying operation. Binder migration can be affected by the rate in the preheating stage. The time in the constant drying rate zone and the temperature in the falling drying rate zone also affect many of the final sheet properties."
- Interpretation: Mottle (nonuniform appearance) traces to binder migrating during drying; controlling preheat rate and constant-rate time suppresses it. Directly relevant to uniform lotion/active distribution on a wipe.
### Viewpoint 5 — Air impingement dries the surface first and accelerates binder migration

- Page: p.933
- Quote: "the high-velocity air impinging directly on the coating surface tends to dry the surface coating and accelerates the binder migration in the coating. 'Rail road tracking' will take place when the dryer temperature exceeds the wet bulb temperature of the constant drying rate period."
- Interpretation: There is a built-in tension: impingement jets speed drying but over-dry the surface (skinning) and drive interior binder outward (railroad tracking defect). The wet-bulb temperature of the constant-rate period is the ceiling to respect.
### Viewpoint 6 — 100% solids UV/EB cure needs no solvent removal and leaves no toxic residuals

- Page: p.942
- Quote: "UV-curable coatings are 100% solids and solvent removal equipment is not required. … In the case of curing or cross-linking, it generally provides a clear-cut reaction with no residual promoters or cross-linking agents that might cause degradation of the product or problems with governmental agency regulations on toxic residues in products for food and drug applications."
- Interpretation: For skin-contact hygiene films and wipes, 100% solids UV/EB is the regulatory-friendly route: no solvent VOC, no extractable cross-linker residuals — directly relevant to food/drug-contact compliance.
## 3. Research Method & Data Sources

Engineering review of commercial dryer hardware with design correlations and safety standards.

||||||
|---|---|---|---|---|
|Drying-curve construction|Plot % solvent vs time and rate vs time (Fig 40.2–40.4)|In-chapter experimental-data summary|Empirical curves|Representative for solvent/latex/paper|
|Air-bar heat transfer|h-coefficient measurement & correlation (Fig 40.11)|Martin (1977), Obot et al., Mujumdar/Douglas|Nu/Sh correlations, CFD-style profiles|Geometry-dependent|
|IR wavelength matching|Absorption spectrum of water film vs IR bands (Fig 40.18)|Hung (1989 TAPPI)|Spectral matching|Sound for water/latex|
|Safety/regulation|LEL, NFPA, EPA, inert-gas O₂ limits (Table 40.1)|NFPA (1990), EPA Clean Air Act|Regulatory tables|Binding legal standards|
|Cure chemistry|UV photoinitiation, EB cross-linking|Rie & Berejka (1986)|Chemical mechanism|Established radiation-curing science|

## 4. Argumentation Process

- Scope — coated-web taxonomy + coating forms (solvent/water/100% solids) (p.929–930).
- Drying-curve framework — three stages; latex vs solvent vs paper differences; defect linkage (p.931–932).
- Hardware ladder — steam cylinders → air cap → impinging jet tunnel → air flotation → air turns → IR → UV → EB (p.932–943).
- Air-flotation deep-dive — air-bar types, cushion pressure, web stability, spent-air removal (p.934–938).
- IR physics — wavelength/penetration/absorptivity matching (p.939–941).
- UV/EB cure — 100% solids, free-radical polymerization, food/drug safety (p.941–942).
- Applications — paper coating, PVDC barrier, PSAs (p.943).
- Safety — LEL, inert gas, VOC recovery/incineration (p.944–948).
## 5. Role in the Book

Ch40 is the "thin-liquid-layer-on-moving-substrate" chapter, complementary to Ch41 (granular polymer resins), Ch35 (pulp/paper web conduction), and Ch33 (fibre–water physics). It is the direct engineering counterpart to any hygiene converting line: lotion/emulsion coating on wipes (Ch40's latex/water-based logic), adhesive and barrier coating on backsheet films (PVDC, PSA sections), and printed packaging. For the hygiene reader it converts "coat a liquid on a film" into a drying-rate-control problem.

## 6. Strengths & Weaknesses

✅ Strengths: Unusually explicit on the defect-mechanism link (binder migration → mottle, surface drying → railroad tracking, over-drying → blistering/curl). The air-flotation design detail (cushion pressure, Pc/Ps ratio, spent-air % of outlet velocity) is procurement-grade. The LEL/inert-gas/VOC section is thorough and quantified (Table 40.1 O₂ limits, 99% thermal-incinerator cleanup).
⚠️ Limitations/contestable: A 2006 review; UV/EB "no toxic residues" claim (p.942) is relative — photoinitiator fragments can still be extractable and are separately regulated. No quantitative diffusion/Fick model for the falling-rate (binder-migration) stage; "railroad tracking" mechanism is asserted, not derived. IR penetration max ~1.5 mm (p.940) is stated without derivation. No mention of superabsorbent or hygiene-specific formulations.

## 7. Key Terms / Concepts

- Coated web types: p.929, "(1) coated paper and paperboard; (2) coated plastic films (e.g., photographic films) and tapes (e.g., adhesive tapes…); and (3) coated metallic sheets."
- Coating forms: p.930, "(1) solventborne; (2) waterbased; and (3) 100% solids."
- Binder / additives / solvent: p.930, coatings contain "a binder… a variety of additives… surface particles… a liquid solvent to dissolve or suspend all particles."
- Three drying-rate periods: p.931, "(1) the adjustment stage or the cooling-down period… A–B; (2) the constant drying rate period… B–C; and (3) the falling drying rate period… C–D."
- Binder migration / mottle: p.931, "binder migration causing printing mottles should be eliminated or minimized during drying operation."
- Over-dry defects: p.931, "Over-drying or rapid drying can cause brittleness, blistering, curl, and wrinkles."
- 75% dryness rule: p.933, "Little migration occurs once the coating is about 75% dryness."
- Railroad tracking: p.933, "will take place when the dryer temperature exceeds the wet bulb temperature of the constant drying rate period."
- Air flotation / cushion pressure: p.934, web "supported on a cushion of heated air issued from the slots"; p.938 "Pc/Ps is important."
- IR penetration: p.940, "maximum depth of penetration is approximately 1.5 mm. Good penetration… heats the substrate rather than skinning and blistering it."
- UV/EB 100% solids: p.942, "UV-curable coatings are 100% solids and solvent removal equipment is not required."
- LEL / inert gas: p.944–945, max solvent vapor 25% LEL (50% with instrumentation); inert gas keeps O₂ "% oxygen."
- VOC: p.946, "The general term for these materials is volatile organic compounds (VOCs)."
## 8. Micro close-reading (ONE key paragraph)

p.931 (Drying-curve stage logic and defect linkage):
> "Once the drying mechanism or drying characteristics of each drying rate stage are identified for each coated web, the proper design and control of the drying system can also affect many of the final sheet properties. Over-drying or rapid drying can cause brittleness, blistering, curl, and wrinkles. Brightness, ink receptivity, and varnishability can be reduced. Nonuniform moisture profile, which is normally caused by raw stock or coating, can sometimes also be attributed to drying conditions."

Sentence-by-sentence: (1) Premise — once you identify each stage's mechanism per web, you can design/control the dryer. (2) Warning — too much or too fast drying produces brittleness, blistering, curl, wrinkles (the defect catalog). (3) Quality — optical/printability properties (brightness, ink receptivity, varnishability) drop. (4) Attribution — nonuniform moisture is usually raw-stock/coating-caused but can be a drying-condition artifact, so drying is a controllable variable for uniformity.
💡 Standout line: "Over-drying or rapid drying can cause brittleness, blistering, curl, and wrinkles" — the concise defect-risk statement every coating-line qualification must respect.

## 9. Concept deep-dive

Binder migration = the mottle/skinning mechanism (the wipe-relevant core). The chapter names binder migration as the cause of printing mottles (p.931) and states it is "affected by the rate in the preheating stage" and by "the temperature in the falling drying rate zone" (p.931). During the falling-rate period, evaporation pulls the continuous-phase binder (and any dissolved active, e.g., lotion/encapsulated ingredient) toward the drying surface; if the surface skins first (impingement over-drying, p.933), the interior keeps migrating and yields nonuniform distribution — visually "mottle," functionally nonuniform active loading on a wipe. The quantitative guardrail: "Little migration occurs once the coating is about 75% dryness" (p.933), so the design target is to reach 75% solids fast (constant-rate) and then finish gently.

Impingement jet vs flotation — surface-drying vs contactless. High-velocity air caps (35–95 kg/m²·h at 50–60 m/s, 150–315°C, p.933) accelerate surface drying and worsen binder migration (p.933); air flotation (up to 60 kg/m²·h, 1100 m/min, p.935) supports the web on a heated-air cushion with no contact, avoiding picking/marks. Double-slot air bars give more stable flotation and tolerate wider clearance (p.934–935). For a delicate lotion-coated wipe web, flotation (no contact, no picking) is the safer choice; impingement is reserved where high rate is needed and migration is not.

IR wavelength must match the coating's absorption (avoid skinning). IR penetration max ~1.5 mm (p.940); with "good penetration into the substrate… heats the substrate rather than skinning and blistering it" (p.940). The water-film absorption peaks at 3 µm and 6 µm (Fig 40.18) match medium/long-wave IR; "the absorption and radiation curves should be matched as closely as possible" (p.941). For water-based lotion coatings, tuned medium/long-wave IR preheats the web without skinning — a direct design rule.

UV/EB cure = solvent-free, low-residual route for skin-contact films. UV-curable coatings are 100% solids with "no residual promoters or cross-linking agents that might cause… problems with… regulations on toxic residues in products for food and drug applications" (p.942). EB curing does "cross-linking" (p.942) as a clean reaction. This is the hygiene-compliant path for adhesive/coating lines on films touching skin or food.

## 10. Academic critique & open questions

- No diffusion model for the falling-rate/binder-migration stage; the "75% dryness" rule is empirical, not derived from a capillary/viscosity model.
- "Railroad tracking" (p.933) is named but not mechanistically derived; its link to wet-bulb temperature is asserted.
- The UV/EB "no toxic residues" statement (p.942) understates modern concerns about photoinitiator migration/extractables in food-contact applications; should be read as "no solvent VOC," not "no extractables."
- Open question 1: Can binder-migration during the falling-rate period be modeled for a water-based lotion/active coating so that the 75%-dryness crossing time (and hence mottle risk) is predictable from rheology and impingement flux?
- Open question 2: For a skin-contact hygiene film, what is the extractable-residual profile of UV photoinitiators vs the IR/flotation-dried solvent route the chapter implicitly prefers to avoid?

## 11. Hygiene-material relevance & action cards

Overall relevance: ★★★★★ (directly maps to wipe lotion coating & film adhesive/barrier lines).

Action Card H40-1 — Schedule drying to cross 75% dryness fast, then finish gently (anti-mottle). Insight: p.933 "Little migration occurs once the coating is about 75% dryness"; p.931 binder migration set in preheat/constant-rate. Action: For lotion/active-coated wipes, specify a high constant-rate predry to reach ~75% solids quickly, then a low-temperature falling-rate finish; forbid over-fast impingement that skins the surface. → 卫材相关性★★★★★｜Directly controls mottle and uniform active loading on the wipe.

Action Card H40-2 — Use flotation (not impingement) for delicate coated-wipe webs. Insight: p.935 air flotation supports web "on a cushion of heated air" with no contact; p.933 impingement "accelerates the binder migration." Action: When qualifying a wipe or film coater, prefer air-flotation drying for the coated side to avoid picking/marks and to limit surface-driven migration. → 卫材相关性★★★★★｜Contactless drying protects coating integrity and uniformity.

Action Card H40-3 — Cap dryer temperature at the constant-rate wet-bulb to avoid railroad tracking. Insight: p.933 "'Rail road tracking' will take place when the dryer temperature exceeds the wet bulb temperature of the constant drying rate period." Action: Require the coater to run impingement below the coating's wet-bulb temperature during constant-rate; add a defect check (railroad tracking / streaks) to incoming-film audit. → 卫材相关性★★★★★｜A named defect mode to screen on coated hygiene films.

Action Card H40-4 — Tune IR to the water-absorption band to preheat without skinning. Insight: p.940 IR penetration max ~1.5 mm; "heats the substrate rather than skinning and blistering it"; p.941 match absorption/radiation curves; water peaks at 3 & 6 µm. Action: For water-based lotion coatings, specify medium/long-wave IR preheat matched to the water band rather than short-wave that skins the surface. → 卫材相关性★★★★★｜Prevents skinning/blistering of the lotion layer.

Action Card H40-5 — Prefer 100% solids UV/EB cure for skin-contact film coatings. Insight: p.942 UV/EB "100% solids and solvent removal equipment is not required… no residual promoters or cross-linking agents… toxic residues in products for food and drug applications." Action: For adhesive/coating lines on films touching skin, evaluate UV/EB cure to eliminate solvent VOC and reduce extractable residuals; verify photoinitiator extractables separately. → 卫材相关性★★★★★｜Regulatory-friendly route for food/drug-contact hygiene films.

Action Card H40-6 — Enforce LEL/inert-gas safety on any solvent-coated hygiene film. Insight: p.944 max solvent vapor 25% LEL (50% with instrumentation); p.945 inert gas keeps O₂ "% oxygen"; p.946 VOCs. Action: If a backsheet/tape line uses solvent coatings, require LEL monitoring + auto-shutdown at 50% LEL and confirm inert-gas O₂ control for solvent recovery. → 卫材相关性★★★★☆｜Fire/explosion compliance for converting lines.

Action Card H40-7 — Specify barrier/adhesive dry rates from the application tables. Insight: p.943 PVDC vapor-barrier "evaporation rates are usually 10 to 15 kg/h/m² with air velocities of 20 to 40 m/s"; p.943 PSAs "Solvent removal rate limitations are at 18 kg/h/m²"; p.943 paper-coat system "80% solid level by air flotation… 4 to 6 steam-heated cylinders with an evaporation rate restriction of 20 kg/h/m²." Action: Benchmark supplier converting-line rates against these figures when qualifying barrier or PSA hygiene films. → 卫材相关性★★★★☆｜Concrete rate benchmarks for film coating qualification.

## 12. Book-Map Quotes (Top representative quotes)

"Because of the product quality problems associated with the drying process, the proper quantity of heat and mass transfer has to be applied to the coating at the proper time in the drying curve." — p.931 — the scheduling thesis of the whole chapter.
"the high-velocity air impinging directly on the coating surface tends to dry the surface coating and accelerates the binder migration in the coating." — p.933 — the impingement/migration tension.
"UV-curable coatings are 100% solids and solvent removal equipment is not required… no residual promoters or cross-linking agents that might cause… problems with… regulations on toxic residues in products for food and drug applications." — p.942 — the hygiene-compliant cure route.


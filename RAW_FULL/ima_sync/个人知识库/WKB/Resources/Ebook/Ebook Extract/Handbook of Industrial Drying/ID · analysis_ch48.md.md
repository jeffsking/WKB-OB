---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_24954884f4748718f2d63ac6113df6ec001a693ee6c0644e"
source_file: "ID · analysis_ch48.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch48.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch48.md.md

# Chapter 48 — Safety Aspects of Industrial Dryers

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 48 (Markowski & Mujumdar) treats dryer safety as a three-factor problem — process, engineering, and management — and argues that drying is "particularly prone to fire and explosion hazards because it is a process in which external heat sources are applied." It first establishes the fire-triangle (fuel, oxygen, ignition source), then gives a material-characterization procedure: explosibility (oxygen balance, flammability), combustibility (CIBA-Geigy rating), dust-explosion characteristics (MEC, MIT, MIE, P_max, (dP/dt)_max, K_st) with an extensive dust table, and thermal-decomposition/self-heating onset (T_A/T_L/T_B via DTA/DSC). The engineering factor covers prevention (inerting, dust-cloud avoidance, ignition-source exclusion) and protection (venting, suppression, containment, isolation). The management factor closes the loop with operation, maintenance, training, ATEX, and SIL-rated reliability. For a hygiene reader the chapter is a direct hazard handbook for fluff-pulp defibration dust and polyacrylate SAP powder.

## 2. Key Viewpoints (with verbatim quotes + print pages)

### Viewpoint 1 — Drying is inherently fire/explosion-prone; dryers are a top dust-explosion location

- Page: p.1131–1132
- Quote: "drying should be regarded as a potentially hazardous operation that has brought a number of reported incidents with serious results for personnel and equipment … Approximately 8 to 9% of all dust explosions in the food industry is related to the drying operation … an average of four major accidents in spray dryers were reported annually."
- Interpretation: Quantifies the hazard baseline. Any hygiene drying step (airlaid oven, coating dryer, SAP spray/flash dryer, fluff defibration) sits in the same risk class as food drying.
### Viewpoint 2 — Three conditions must coincide for fire/explosion

- Page: p.1133
- Quote: "The simultaneous presence of three basic conditions is required for fire and explosion to occur (Figure 48.2) 1. Fuel (e.g., flammable dusts, solvents, or hybrid mixtures) 2. Oxygen (air) 3. Ignition source with sufficient energy. When any of these three basic conditions is missing, no explosion can occur."
- Interpretation: The bow-tie logic every hygiene-line safety case must use: eliminate any one leg (inerting removes O₂; dust-cloud control removes fuel; grounding removes ignition).
### Viewpoint 3 — Most dried powders are type-3 (combustible) and dryable only with control

- Page: p.1134
- Quote: "The majority of powdery, fibrous, and granular products processed in dryers contain fuels … fine combustible dust, when dispersed in air, can form a reactive mixture leading to explosion … The drying of solids of type 3 can be safely carried out by proper control of operating conditions and by providing adequate precautionary measures."
- Interpretation: Fluff pulp (cellulose), SAP (crosslinked polyacrylate), and polymer-film fines are all "type 3" — not explosives, but combustible dusts whose safe drying depends on control, exactly as the chapter prescribes.
### Viewpoint 4 — Dust-explosion violence is quantified by P_max, (dP/dt)_max, and K_st

- Page: p.1138
- Quote: "(dP/dt)_max … The P_max for dryers operating at atmospheric pressure does not exceed 900 kPa and can develop rates up to 10 kPa/s … (dP/dt)_max V^(1/3) = K_st where V is the volume of the vessel and K_st is the dimensional constant characteristic of a particular dust (kPa·m/s)."
- Interpretation: This is the design basis for vent/suppression sizing. The cube-root law lets a hygiene engineer scale a 1.2-L Hartmann result to a real dryer volume.
### Viewpoint 5 — Polymer dusts are low-MIE, easily ignited by static; bag filters need conductive fibers

- Page: p.1138 / p.1147
- Quote: "The majority of incidents occur with sparks having ignition energy below 25 mJ … the extremely high resistance of synthetic fibres used in bag filters may be reduced by adding some steel or carbon fibers."
- Interpretation: Table 48.4 gives PE MIE 10 mJ and PP MIE 30 mJ — both below the 25 mJ spark threshold. On a hygiene line, SAP/PP/PE fines and synthetic-fibre filter bags are a static-ignition risk unless grounded with steel/carbon fibres.
### Viewpoint 6 — Inerting and self-inertizing remove the oxygen leg

- Page: p.1146
- Quote: "The principle of inerting is to create an environment in which combustion cannot take place. Some of the common inerting agents are N₂, CO₂, flue gases, and others … Inerting also decreases the maximum explosion pressure and retards the rate of pressure rise."
- Interpretation: For solvent-borne coatings or fine polymer/SAP powders, N₂/CO₂ inerting (or exhaust-gas recycle "self-inertizing," p.1146) is the cleanest way to break the oxygen leg — directly transferable to enclosed coating/airlaid dryers.
### Viewpoint 7 — Thermal-decomposition onset (T_A/T_L/T_B) sets the safe operating temperature

- Page: p.1140 / p.1144
- Quote: "Characterization of an exothermal behavior of the material involves a determination of the temperature at which exothermicity is first detected and then the rate, magnitude, and nature of the subsequent decomposition … For material with self-heating capabilities collected and stored in the bulk form, the most important … data on the self-heating are given by Bowes."
- Interpretation: For heat-sensitive polymers (SAP decarboxylation, PP/PE oxidative degradation), the DTA/DSC onset (p.1140) defines the temperature ceiling; Table 48.7 then sets operating margin (e.g., T_L − 20°C for dust layers).
### Viewpoint 8 — Build safety in at design; retrofit is costly; secondary dust explosion is devastating

- Page: p.1156 / p.1157
- Quote: "it is more economical to provide necessary safety measures against a hazard at the design stage so that safety can be built into the plant, rather than to 'retrofit' safety equipment, which can be very costly … The secondary explosion, usually caused by dust deposition on surrounding surfaces, is always devastating; the importance of good housekeeping cannot be overemphasized."
- Interpretation: Specifies that explosion protection (venting, isolation, suppression) must be in the original bid, and that deposit cleaning/housekeeping is the real daily defense — both contractually actionable for a hygiene-line buyer.
## 3. Research Method & Data Sources

Review/standards-survey chapter drawing on dust-explosion test standards (ASTM E1226, VDI 3673, NFPA 68/69/325M), IChemE guides, Bartknecht, Gibson/Harper/Rogers, and an extensive compiled explosibility database (Table 48.4).

||||||
|---|---|---|---|---|
|Fire-triangle / hazard classification|Material characterization tree (Fig 48.3, Table 48.1)|CIBA-Geigy; IChemE user guide|Rating Tr0–Tr3; oxygen balance|Industry/regulatory standard|
|Dust explosibility measurement|Hartmann bomb (1.2-L) / 20-L sphere, 10 kJ igniter|Palmer; Field; Bartknecht|MEC, MIT, MIE, P_max, (dP/dt)_max|Empirical; ±sample variability|
|K_st / cube-root law|V^(1/3) scaling of (dP/dt)_max|Simmonds–Cubbage; NFPA 68; VDI 3673|K_st; vent normographs|Validated large-scale|
|Thermal decomposition|DTA/DSC; ICI screening test|Gibson et al.|T_A/T_L/T_B onset|Small-scale; dryer-condition gap noted|
|Protection design|Vent ratio / K-factor / cube-root; suppression; containment|IChemE guides 30–32; Crawl & Louvar|Tables 48.8–48.9; Figs 48.13–48.17|Widely used; dryer-specific sparse|
|Reliability|SIL (IEC 61508); hazard-rate model|Rogers; Markowski & Mujumdar|H = f T_n[1−exp(−D T/n)]|Probabilistic; illustrative|

## 4. Argumentation Process

- Hazard framing — dryers are risky; three-factor model (process/engineering/management) (p.1131–1133).
- Process factor — fire triangle; material classification (types 1–3); characterization procedure (explosibility, combustibility, dust-explosion characteristics, thermal decomposition); flammable vapors; hybrid mixtures; ignition sources; operating-condition selection (p.1133–1144).
- Engineering factor — design; prevention (inerting, no dust clouds, no ignition); protection (venting, suppression, containment, isolation); fire protection; ancillary units; reliability/SIL (p.1145–1153).
- Management factor — operation, maintenance, training, ATEX, human error >90% (p.1153–1157).
- Synthesis — 10-stage safe-design procedure (Fig 48.18) and the "design-in not retrofit" conclusion.
The logic is defensive-layered: eliminate → prevent → protect → isolate → manage, each justified by the preceding hazard data.
## 5. Role in the Book

Ch48 is the plant-safety capstone paired with Ch49 (control), Ch44 (feeding), and the emission-control Ch45. It supplies the hazard vocabulary (MIE, MEC, K_st, MIT, T onset) that Ch49's spray-dryer safety interlocks (p.1169) assume. For the hygiene reader it is the reference for two real line hazards — fluff-pulp defibration dust and SAP powder — and complements procurement specs that must demand venting/isolation/inerting rather than hope.

## 6. Strengths & Weaknesses

✅ Strengths: Genuinely actionable data — Table 48.4 gives MEC/MIT/MIE/P_max/(dP/dt)_max/St for cellulose acetate, nylon, PE, PP, polystyrene, PVA, rayon, rubber; Table 48.5 gives solvent LFL/UFL; Tables 48.7–48.11 give operating margins and per-dryer measures. The MIE mJ and 10 kPa vent-opening rules are directly usable. The K_st cube-root law and vent-ratio table (48.8) let a buyer size protection.
⚠️ Limitations/contestable: 2006 data; some OCR garbling (e.g., "500 mm" particle cutoff at p.1137 should be ~500 µm; "2.8 10³" notation for K_st, p.1138). "T_A = T_A − (30–50°C)" marginal-temperature notation is garbled (p.1144). No SAP (crosslinked sodium polyacrylate) entry in Table 48.4 — the hygiene reader must treat it as an untested member of the "Plastics" class. Hybrid-mixture explosion data explicitly "not yet available" (p.1143). Vent design "very little information is available on vent design for dryers" (p.1148).

## 7. Key Terms / Concepts

- Fire triangle: p.1133, "Fuel … Oxygen (air) … Ignition source with sufficient energy. When any of these three basic conditions is missing, no explosion can occur."
- MEC (minimum explosive concentration): p.1137, "the lowest concentration of suspended dust capable of propagating flame … 0.02 to 0.085 kg of product/m³ of air for polyethylene and coffee, respectively."
- MOC (minimum oxygen concentration): p.1137, "varies between 3 and 15% (v/v) as measured experimentally at 850°C."
- MIT (minimum ignition temperature): p.1138, "370, 500, and 575°C for sugar, cocoa, and coal, respectively."
- MIE (minimum ignition energy): p.1138, "30, 120, and 50 mJ for sugar, cocoa, and coal, respectively … majority of incidents occur with sparks having ignition energy below 25 mJ."
- K_st (dust explosion constant): p.1138, "(dP/dt)_max V^(1/3) = K_st"; St1 0300 kPa·m/s (Table 48.3).
- Dust classes from Table 48.4 (hygiene-relevant): Polyethylene MEC 0.020, MIT 450, MIE 0.010 J, P_max 5.50, (dP/dt)_max 516, St2; Polypropylene MEC 0.020, MIT 420, MIE 0.030 J, P_max 5.30, (dP/dt)_max 356, St1; Cellulose acetate MIT 420, MIE 0.015 J; Nylon MIT 500, MIE 0.020 J; Polyvinylacetate MIE 0.160 J; Rayon MIE 0.240 J.
- Thermal-decomposition onset (T_A/T_L/T_B): p.1140, "temperature at which exothermicity is first detected" in aerated/layer/bulk form; characterized by DTA/DSC.
- Vent ratio: p.1148–1149, Table 48.8: ,000 kPa/s → 1/7 (wood, coal, flour, coffee); 35,000–70,000 → 1/5 (plastics); ,000 → 1/3 (Mg, Al).
- Suppression activation: p.1150, "when the start of a dust explosion is detected (usually within the first 10 ms)"; keeps max pressure rise below 10 kPa; effective if K_st and K_G < 300 Pa·m/s.
- SIL: p.1153, "For category 1 (dryers) the overall protection system SIL3 is assigned, i.e., the probability of failure on demand is from 10⁻⁴ to 10⁻³/y."
## 8. Micro close-reading (ONE key paragraph)

p.1137 (why fine dust is the hazard and what concentration ignites):
> "For a dust to be explodable, the particle size must be small enough to give an adequate reactive surface area, and the dust cloud sufficiently dense and uniform to propagate the combustion reaction. Particles greater than about 500 mm in diameter are unlikely to cause explosions, although during drying a comminution process may take place that produces fine powder much smaller in diameter … The range of explosible concentrations is strongly influenced by many parameters, e.g., the particle size, particle shape, moisture content, the position and nature of the ignition source, and more."

Sentence-by-sentence: (1) Reactivity gate — only fine particles with enough surface area can propagate flame. (2) Particle-size cutoff — coarse particles (>~500 µm, OCR "500 mm") are safe, but drying can generate fines by attrition/comminution. (3) Concentration/uniformity — the cloud must be dense and uniform. (4) Sensitivity list — particle size, shape, moisture content, ignition source all shift the threshold. The sentence on moisture content is the hygiene bridge: wet fluff/SAP is far safer than bone-dry powder, so final-moisture control (Ch49) is also a dust-safety lever.
💡 Standout line: "during drying a comminution process may take place that produces fine powder much smaller in diameter" — the dryer itself can create the explosive fines, so protection cannot assume a benign feed.

## 9. Concept deep-dive

Dust-explosion parameter set and how it sizes protection. The chapter defines the measurable hazard signature of a powder: MEC (fuel concentration floor), MOC (oxygen floor), MIT (thermal ignition ceiling), MIE (spark energy floor), P_max and (dP/dt)_max (pressure violence), and K_st = (dP/dt)_max·V^(1/3) (cube-root law, p.1138). K_st places the dust in St1/St2/St3, which in turn selects the vent ratio (Table 48.8: plastics → 1/5). For a hygiene line, the relevant powders are cellulose (fluff pulp, ≈ wood/flour class), PP/PE (films/nonwoven fines), and SAP (crosslinked polyacrylate, unlisted but a combustible organic polymer powder). Table 48.4 supplies the actual numbers for the polymer analogues (PE St2 K_eff 516; PP St1 356), giving an immediate design basis.

Thermal-decomposition / self-heating onset. The chapter distinguishes flame propagation (dust cloud) from exothermic decomposition in layer/bulk/aerated form (p.1140), characterized by DTA/DSC and the ICI screening test yielding T_A (aerated), T_L (layer), T_B (bulk) onset temperatures (Figure 48.8 distribution for >200 organics). Table 48.7 then sets operating margins: dust layer T_L − 20°C, bulk T_B − 50°C. This is the control limit for drying heat-sensitive polymers (SAP, PP, PE) where overheating triggers decomposition rather than flame.

Protection hierarchy. Prevention removes a leg of the triangle (inerting with N₂/CO₂ to MOC; dust-cloud avoidance by air velocity; ignition exclusion by grounding/friction control). Protection assumes explosion is inevitable: venting (P_stat ≈ 10 kPa, K-factor/cube-root sizing, Table 48.8–48.9), suppression (detect 900 kPa), and isolation (fast knife-gate valve) to stop secondary propagation. SIL3 reliability (Pfd 10⁻⁴–10⁻³/y) is required for dryer protection systems.

## 10. Academic critique & open questions

- The explosibility database (Table 48.4) omits SAP (crosslinked sodium polyacrylate) and most hygiene-relevant polymer powders; the reader must infer from the "Plastics" class, introducing uncertainty.
- OCR degradation: "500 mm" particle cutoff (p.1137) is physically impossible and must be ~500 µm; K_st notation "2.8 10³" (p.1138) scrambles scientific notation; T_A margin "= T_A − (30–50°C)" (p.1144) is garbled.
- Vent design for dryers is explicitly under-documented (p.1148); hybrid-mixture explosion properties "not yet available" (p.1143).
- DTA/DSC small-scale results "differentiate between conditions in the experiment and in the dryer" (p.1141) — onset temperatures need confirmation at process scale.
- Open question 1: Where does crosslinked sodium-polyacrylate SAP powder fall on the St1/St2 scale and what MIE/MEC should a hygiene SAP-handling line be designed to? (No published value in chapter.)
- Open question 2: For an airlaid/defibration line generating cellulose + SAP fines, what is the combined (hybrid with any solvent vapour) K_st and required vent ratio, given hybrid data were unavailable at publication?

## 11. Hygiene-material relevance & action cards

Overall relevance: ★★★★★ (direct, quantified hazard data for fluff-pulp defibration dust and SAP/polymer powder — two real hazards on hygiene lines).

Action Card H48-1 — Require a dust-explosion data sheet (MEC/MIT/MIE/K_st) for every powder handled. Insight: p.1138 K_st = (dP/dt)_max·V^(1/3); Table 48.4 gives PE St2 (516), PP St1 (356), cellulose acetate, nylon, PVA. Action: Demand suppliers certify MEC, MIT, MIE, P_max, (dP/dt)_max and St class for fluff pulp, SAP, and any polymer fines; treat untested SAP as ≥St1. → 卫材相关性★★★★★｜Defines the legal/engineering explosion-protection basis for SAP/fluff powder handling.

Action Card H48-2 — Ground all synthetic-fibre filter bags and bonding; conduct static audit. Insight: p.1138 "majority of incidents occur with sparks having ignition energy below 25 mJ"; p.1147 "synthetic fibres used in bag filters may be reduced [in resistance] by adding some steel or carbon fibers." Action: Specify bag filters with steel/carbon fibres and verified grounding; audit for MIE mJ spark sources (SAP MIE ~10 mJ class). → 卫材相关性★★★★★｜SAP/PP/PE fines + synthetic nonwoven bags are a static-ignition dust-explosion pair.

Action Card H48-3 — Size vents by K_st / cube-root law, not by guess. Insight: p.1148–1149 Table 48.8 plastics → 1/5 vent ratio; K-factor and cube-root scaling from 1.2-L Hartmann to plant volume. Action: In dryer/cyclone/baghouse specs, require vent area sized to the powder's K_st (plastics 1/5), with P_stat ≈ 10 kPa. → 卫材相关性★★★★★｜Converts abstract explosion risk into a dimensioned, code-grade requirement.

Action Card H48-4 — Specify inerting or self-inertizing for solvent/closed powder loops. Insight: p.1146 inerting with N₂/CO₂ "decreases the maximum explosion pressure and retards the rate of pressure rise"; exhaust recycle "self-inertizing" also improves thermal efficiency. Action: For coating-oven or SAP spray dryers using solvent, require N₂/closed-cycle or exhaust-recycle inerting to MOC. → 卫材相关性★★★★★｜Removes the oxygen leg for solvent-borne coatings and fine powders.

Action Card H48-5 — Set operating-temperature margins from thermal-onset data. Insight: p.1140 DTA/DSC onset T_A/T_L/T_B; p.1144 Table 48.7 layer T_L−20°C, bulk T_B−50°C, vapour VC% LFL. Action: Require the dryer spec to state the material's decomposition/MIT onset and operate with the prescribed margin (e.g., 50–80°C below MIT). → 卫材相关性★★★★★｜Prevents thermal decomposition of SAP/PP/PE during drying.

Action Card H48-6 — Mandate explosion isolation + housekeeping against secondary explosions. Insight: p.1157 "The secondary explosion … caused by dust deposition on surrounding surfaces, is always devastating; the importance of good housekeeping cannot be overemphasized." Action: Require fast knife-gate isolation between interconnected vessels (dryer→cyclone→baghouse) and a written deposit-cleaning schedule. → 卫材相关性★★★★★｜Secondary dust explosion is the real killer; isolation+cleaning is daily defense.

Action Card H48-7 — Demand SIL3-rated protection and ATEX categorization. Insight: p.1153 "category 1 (dryers) … SIL3 is assigned, i.e., probability of failure on demand is from 10⁻⁴ to 10⁻³/y"; p.1154 EU ATEX 94/9/EC mandatory risk assessment. Action: Make SIL3 and ATEX risk-assessment documentation a contractual acceptance criterion for any dryer on a hygiene line. → 卫材相关性★★★★☆｜Aligns supplier with regulatory and reliability expectations.

## 12. Book-Map Quotes (Top representative quotes)

"The simultaneous presence of three basic conditions is required for fire and explosion to occur … Fuel … Oxygen (air) … Ignition source with sufficient energy. When any of these three basic conditions is missing, no explosion can occur." — p.1133 — the bow-tie logic for any hygiene dryer safety case.
"(dP/dt)_max V^(1/3) = K_st where V is the volume of the vessel and K_st is the dimensional constant characteristic of a particular dust (kPa·m/s)." — p.1138 — the scaling law that sizes every vent and suppressor.
"The secondary explosion, usually caused by dust deposition on surrounding surfaces, is always devastating; the importance of good housekeeping cannot be overemphasized." — p.1157 — the daily, non-engineering defense that matters most.


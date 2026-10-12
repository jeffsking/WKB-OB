---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_1307deb79070543f007e4215f7d36ddf001a693ee6c0644e"
source_file: "ID · analysis_ch14.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch14.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch14.md.md

# Chapter 14 — Spouted Bed Drying

## 1. Chapter Overview (范围、对象与定位)

Chapter 14 (Pallai, Szentmarjay, Mujumdar) treats the spouted bed dryer (SBD) as a particle-processing technology for materials too coarse to fluidize (grains) and, more importantly for the hygiene reader, for heat-sensitive pastes, slurries, suspensions, and synthetic products dried on a bed of inert particles. The chapter's arc runs: principle/device → residence-time distribution (RTD) → agricultural drying results → pulp/paste drying on inert particles → development (microwave-coupled MSB) → assessment. Its engineering center is the mechanically spouted bed (MSB) with inert packing, where wet feed coats large inert particles, dries in a thin film at low wet-bulb temperature, then wears off as powder. For hygiene R&D this is moderately relevant: it is a genuine low-temperature, attrition-controlled powder-production route for heat-labile polymers — directly parallel to drying SAP gel, fluff-pulp slurry, and nonwoven binder emulsions — and it supplies concrete specific-energy-consumption benchmarks (kJ/kg water) for the energy-cost/tonne question. Polymer examples appear explicitly (PVC, Hostaform, polypropylene, "synthetic products").

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.361–p.382 (PDF p.382–403).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — SBD is engineered for heat-sensitive solids and pastes via short dwell + inert particles.
> "Because of the short dwell time in the spout, SBDs can be used to dry heat-sensitive solids, and, using inert solids as the bed material, SBDs have been used successfully to dry pastes, slurries, and heat-sensitive materials." (p.361)
Interpretation: This is the chapter's core hygiene-relevant claim — short residence + inert-particle thin-film drying = gentle, controllable thermal exposure, exactly what heat-labile SAP/PVA/nonwoven binders require.

V2.2 — Classic SBD is capacity-limited; the draft tube removes the scale-up ceiling.
> "The classic or conventional spouted bed (CSB) is a cylindrical vessel with a conical bottom fitted with an inlet nozzle for the introduction of the spouting air (drying medium). This device suffers from limited capacity due to the maximum spoutable bed height and inability to scale up the apparatus beyond 1-m diameter. The introduction of a hollow, tall vertical tube (draft tube) ... eliminates the former restriction by acting as a pneumatic conveyor." (p.362)
Interpretation: The draft tube is the key scale-up enabler; relevant when translating a lab inert-particle dryer to a tonne-scale powder line.

V2.3 — Inert-particle drying keeps particle T well below gas T; internal diffusion resistance negligible.
> "The wet solid distributed on the large surface of the inert particles forms a thin layer in which a very short drying process occurs. Since the inert particles provide a large contact surface, the heat and mass transfer processes of drying are short even at relatively low wet bulb temperature. Therefore, moisture diffusion resistance in solid can be considered negligible and drying takes place at..." (p.374)
Interpretation: This is the mechanism that makes SBD viable for thermally labile polymers — the product sees low wet-bulb T, not the 120–190 °C inlet gas.

V2.4 — PVC (a polymer) is dried in SBD with explicit energy data.
> "Initial moisture content 60% m/m; Temperature of drying air Inlet 120°C, Outlet 60°C; Final moisture content 0.5% m/m; Specific energy consumption 9000 kJ/kg; Specific rate of evaporation 6.4 kg/m²h." (Table 14.21, p.377)
Interpretation: A real polymer-drying data point; the high specific energy (9000 kJ/kg) reflects that the dried product retains its primary grain size, avoiding grinding — a quality/energy trade-off directly informative for SAP powder production.

V2.5 — SBDs are explicitly suited to synthetic/plastic products with bound moisture.
> "SBDs are especially suited for drying of heat-sensitive materials with surface moisture, as well as those with bound moisture, such as seeds, foodstuffs, pharmaceuticals, and synthetic products, in one or two stages." (p.380)
> "To dry materials with bound moisture (e.g., plastics), tangential air inlet and an inner transport screw are highly recommended since this way the volumetric gas velocity can be adjusted as required by the drying process regardless of the gas velocity requirement for particle motion." (p.381)
Interpretation: Polymers ("plastics", "synthetic products") are named end-users; the tangential-inlet + screw decouples particle motion from drying airflow — a control principle reusable on any convective polymer dryer.

V2.6 — Controllable residence time prevents localized overheating.
> "Intense particle motion: Good particle mixing prevents localized overheating and ensures the product's uniform moisture content. The recirculating motion of particles ensures that during the residence time the drying particles contact the inlet warm air at regular intervals. The residence time of particles may be changed and regulated within very wide limits..." (p.380)
Interpretation: Uniform moisture and tunable thermal dose are precisely the levers for avoiding fibre damage / curl / brightness reversion in heat-sensitive webs.

V6 — Scale-up, not原理, is the remaining barrier. Despite strong pilot evidence, the authors concede "Scaling up of axisymmetric and three-dimensional spouted beds remains a difficult area" (print p.381), and that conventional SBD scale-up relations "cannot be applied to MSB dryers with inert packing due to different hydrodynamical and drying characteristics" (print p.365). For the hygiene reader this means: the principle (gentle inert-particle drying of SAP/polymer feeds) is proven, but a production line would need pilot validation, not a textbook scale-up factor.

## 3. Research Method (研究方法)

The chapter is an experimental results review from the Hungarian Academy (KE MÜKKI) plus literature. Method:
- Device taxonomy: classic CSB → draft-tube SBD → 2-D angular predryer → MSB with inner screw + tangential/swirling-ring air inlet → microwave-coupled MSB.
- Hydrodynamic characterization: RTD via coloured-PVC tracer (Fig. 14.4), plug-flow model with internal recirculation (Eq 14.4), sliding-velocity correlations (Eqs 14.1–14.3).
- Drying experiments: batch & continuous, reporting moisture-vs-time curves, critical moisture, equilibrium isotherms (BET type III for grass seed, Fig. 14.10), specific energy consumption (kJ/kg water), evaporation rate (kg water/m²h).
- Inert-particle mechanism study: cycle-time distribution (CTD) via ⁶⁰Co tracer; partial-process zoning (coating → drying → wearing).
- Assessment: advantages list (p.380) + two development cases (screw-length tube; microwave combination).

## 4. Argumentation (论证逻辑)

- Premise A: Coarse/heat-sensitive/agglomerated materials can't be fluidized or spray-dried cheaply.
- Premise B: A spout + inert bed gives intense gas–solid contact on a renewing thin film at low particle temperature.
- Step: Modify the SBD (draft tube, screw, tangential inlet, MSB) to control RTD, avoid attrition/overheating, and scale up.
- Evidence: Agricultural (wheat/corn/seeds), pulp/paste (potato, yeast, CaCO₃, pigments, PVC), and sludge results with quantitative energy data.
- Resolution: SBDs are an emerging, energy-competitive technology especially for heat-sensitive synthetic products.
The argument is evidence-led and candid that "there are few large-scale industrial applications" (p.382) — appropriate scope discipline.
## 5. Role of This Chapter in the Book (在全书中的角色)

Ch.14 sits in the particulate/specialized dryer cluster. It complements Ch.16 (pneumatic/flash — also for particulates but high-velocity, short-residence) and Ch.17 (conveyor — continuous web). Its unique contribution is the inert-particle thin-film drying of pastes/suspensions — the closest handbook analogue to converting a polymeric slurry (SAP gel, fluff slurry, binder emulsion) into a free-flowing powder without thermal damage. For hygiene R&D it is a reference for gentle powder production and for energy benchmarking.

## 6. Strengths and Weaknesses (贡献与局限)

Strengths
- Explicit heat-sensitive + synthetic-product framing (p.380–381) — directly hygiene-relevant.
- Concrete specific-energy-consumption data across many materials (Tables 14.8–14.24): wheat 3360, corn 2884–3868, potato pulp 3025, yeast 3000–3500, paprika 4091–6158, PVC 9000, CaCO₃ 9715 kJ/kg water.
- Clear inert-particle mechanism (coating→drying→wearing) with CTD evidence.
- Decoupling of particle motion from drying airflow via screw/tangential inlet (p.381).

Weaknesses
- "Few large-scale industrial applications" (p.382) — mostly lab/pilot data; scale-up relations "cannot be applied to MSB dryers with inert packing" (p.365).
- No fluff/SAP/nonwoven specifically; relevance is by analogy.
- OCR noise: concatenated words ("mechanicallyspouted", "quasiconstant") and dropped superscripts in equations/tables.
- Specific energy for PVC (9000 kJ/kg) and CaCO₃ (9715) is high vs simple particulates — the inert-bed route trades energy for product integrity/particle-size retention.

## 7. Key Terms (关键术语)

|||
|---|---|
|Spouted bed (CSB)|"cylindrical vessel with conical bottom fitted with inlet nozzle" (p.362)|
|Draft tube|"hollow, tall vertical tube ... acts as a pneumatic conveyor" (p.362)|
|Mechanically spouted bed (MSB)|central conveyor screw ensures circulation; controls RTD (p.365)|
|RTD (residence time)|measured via tracer; ~ t_t ≈ H/w_a (p.363)|
|Inert-particle drying|wet feed coats inert particles, dries as thin film, wears off as powder (p.374)|
|Coating → drying → wearing|three partial processes of inert-bed drying (p.375)|
|Synthetic products|named as heat-sensitive SBD users (p.380)|
|Specific energy consumption|kJ/kg water; benchmark metric throughout|
|Wet-bulb temperature|particle T stays near this, well below gas T (p.374)|
|Critical moisture X_cr|marks end of constant-rate (Tables 14.4–14.5)|
|BET type III isotherm|grass-seed adsorption isotherm shape (p.368)|

## 8. Micro close-reading (微观精读)

8.1 — The inert-particle gentle-drying sentence (p.374). "Since the inert particles provide a large contact surface, the heat and mass transfer processes of drying are short even at relatively low wet bulb temperature. Therefore, moisture diffusion resistance in solid can be considered negligible and drying takes place at..." This is the chapter's most hygiene-relevant clause. It states the design principle for drying a thermally labile polymeric slurry: keep the particle at wet-bulb temperature (set by the evaporation front, not the 120–190 °C inlet gas), so internal diffusion is no longer the limiting resistance. For an SAP gel or PVA emulsion this is exactly the regime that avoids crosslink scission / Tg-driven casehardening.

8.2 — PVC data row (Table 14.21, p.377). Inlet 120 °C / outlet 60 °C, final 0.5 % m/m, 9000 kJ/kg water. The 60 °C outlet and low final moisture show the polymer leaves cool and dry; the high energy figure is explicitly justified because the product "saved its primary grain size" — grinding/screening avoided. This is the quality-vs-energy trade-off the hygiene reader must price for SAP powder.

8.3 — Temperature ceiling for quality (p.367). For seeds for sowing, "the temperature must not exceed 40–45 °C ... At a drying temperature below 50 °C, the drying rate ... decreases ... In the temperature range between 46 and 50 °C, the aleuron cells form an almost closed, elastic skin in which the diffusion of the moisture is very slow." A pure material-quality-vs-temperature window — the same logic that bounds cure/dry temperature of heat-sensitive nonwoven binders and lotion coatings.

8.4 — Screw decouples motion from airflow (p.381). "the volumetric gas velocity can be adjusted as required by the drying process regardless of the gas velocity requirement for particle motion" — a control architecture (independent particle circulation vs drying-airrate) reusable on any convective polymer dryer.

## 9. Concept deep-dive (概念深掘)

9.1 Inert-particle thin-film drying (p.374–375). Wet feed → annular sliding layer of inert particles → thin coating → intensive drying zone near air inlet (few cm) → wearing in screw zone. CTD shows a particle spends 70 % of cycle in sliding layer, 15–20 % in intensive zone, ~2–10 s in the drying zone (p.375). Net effect: very short high-intensity thermal dose per pass, reset each cycle — ideal for heat-labile polymers.

9.2 Residence-time control (Eqs 14.1–14.3, p.363). Sliding velocity w_a scales with air velocity, bed height, nozzle diameter; t_t ≈ H/w_a. MSB screw widens RTD control "within very wide limits" (p.380) — directly sets thermal dose on sensitive material.

9.3 Specific energy as benchmark (Tables). A consistent dataset of kJ/kg water lets the hygiene reader calibrate target energy/tonne for powder drying: simple particulates ~2900–3900, pastes/polymers ~3000–9700 depending on latent heat recovered and whether grinding is avoided.

9.4 Modified SBD variants (p.382). 2-D beds (modular scale-up advantage), spout-fluid beds (with internal heat-exchange surfaces), microwave-coupled MSB (Case 2, p.381) for heat-sensitive pulps — the latter parallels dielectric/microwave assist used in some polymer drying.

9.5 Polymer-specific notes. Inert particles themselves include polypropylene beads (brewery yeast, p.377: ρ 820 kg/m³, d 3.9×10⁻³ m) and Hostaform (Table 14.3, an acetal/POM copolymer) — confirming genuine polymer presence. PVC (Table 14.21) and "synthetic products" (p.380) are dried products.

9.5 Concrete performance anchors (why the numbers matter). The chapter's tables let the engineer sanity-check the "gentle yet intensive" claim quantitatively: wheat predryer removes moisture at 74 kg water/m²h with 3360 kJ/kg water (Table 14.9); continuous wheat afterdryer reaches 110 kg water/m²h at 7683 kJ/kg water (Table 14.10); shelled-corn pilot gives 396 kg water/m²h at 2884 kJ/kg water (Table 14.13); potato-pulp MSB hits 191 kg water/m²h at 3025 kJ/kg water (Table 14.19); brewery-yeast MSB 120–130 kg water/m²h at 3000–3500 kJ/kg water (Table 14.20). The through-line: specific evaporation of 100–400 kg water/m²h is achievable while keeping the solid below its damage temperature — the operating envelope a hygiene powder line should target when drying SAP or polymer fines.

## 10. Critique (批判性评估)

- Scale-up immaturity. "Scale-up data of conventional SBDs are well known, but the relations cannot be applied to MSB dryers with inert packing" (p.365); "few large-scale industrial applications" (p.382). A hygiene line would need pilot validation.
- No fluff/SAP/nonwoven specifics. All polymer data are PVC/CaCO₃/pigments; SAP/PVA analogues are inferred, not given.
- High energy for quality retention. 9000–9715 kJ/kg for PVC/CaCO₃ reflects the inert-bed premium for particle-size retention — must be weighed against spray-dryer alternative (p.373 notes spray drying "demands very high costs of energy and investment").
- OCR/notation noise. Equations 14.1–14.4 and many tables have concatenated words and dropped superscripts; re-verify against print before use.
## 11. Hygiene-Material Relevance & Action Cards (卫材相关性与行动卡)

H11.1 — Use inert-particle SBD logic for gentle SAP/PVA powder drying (★3). Action: When drying SAP gel or binder emulsion to powder, mimic the thin-film-on-inert-particle principle (p.374) — keep product at wet-bulb T, not inlet-gas T — to avoid crosslink scission / casehardening; benchmark energy against ~3000–9000 kJ/kg water.

H11.2 — Set a quality ceiling temperature like the seed rule (★3). Action: Adopt the seed-for-sowing limit logic (p.367: T must not exceed 40–45 °C for viability; 46–50 °C skins over and stalls diffusion) as a spec for heat-sensitive nonwoven binders and lotion/fragrance coatings — define a max-particle-temperature window, not just inlet-air T.

H11.3 — Decouple circulation from drying airflow (★2). Action: On convective cure ovens for thermobonded webs, copy the screw/tangential-inlet decoupling (p.381) so dwell/throughput is tunable independently of drying-air velocity — protects low-melt binder from over-cure.

H11.4 — Price the grinding-avoidance premium (★2). Action: PVC's 9000 kJ/kg is justified by retained grain size (p.377); for SAP/powder grades where attrition must be minimized, accept higher specific energy in exchange for narrow PSD — quantify via the energy/tonne vs PSD spec.

H11.5 — Benchmark energy/tonne from the tables (★2). Action: Use Tables 14.8–14.24 specific-energy values (2900–9700 kJ/kg water) as sanity bounds when costing a new powder-drying step for fluff/pulp/SAP feedstocks.

H11.6 — Overall relevance: ★★★. Genuine polymer/heat-sensitive-powder content (PVC, PP, Hostaform, "synthetic products"); directly transferable to SAP-slurry and binder-emulsion drying, with one honest gap (no fluff/SAP data).

## 12. Book-Map Quotes (本书脉络引证)

- Ch.4 (p.81): effective diffusivity Fick — internal diffusion "negligible" in inert-particle SBD (p.374) inverts the usual internal-control assumption.
- Ch.16 (p.395): pneumatic/flash drying — the high-velocity, short-residence counterpart to gentle SBD drying.
- Ch.17 (p.409): conveyor dryers — where continuous heat-sensitive web drying is actually deployed in hygiene converting.
- Ch.18 (p.421): infrared drying — another low-thermal-dose route for heat-sensitive coatings (wipes).


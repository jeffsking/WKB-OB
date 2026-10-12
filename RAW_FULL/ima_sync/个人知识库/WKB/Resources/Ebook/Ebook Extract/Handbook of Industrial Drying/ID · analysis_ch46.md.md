---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_c1dcdf1bc08222bcf55e738b65acb862001a693ee6c0644e"
source_file: "ID · analysis_ch46.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch46.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch46.md.md

# Chapter 46 — Energy Aspects in Drying

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 46 (Strumiłło, Jones & Zyłła) treats the drying plant as a major, and largely under-optimised, industrial energy consumer. The authors argue that energy costs are structurally rising and that drying deserves a process-oriented, not industry-specific, treatment. They open with the scale of the problem (12% of manufacturing energy on average; paper ≈33%), then build a quantitative framework: unit energy consumption (kJ/kg water), energy efficiency η=E_ev/E_t, thermal efficiency, and Kudra's instantaneous drying efficiency. The heart of the chapter is a databank of savings — Table 46.5 (13→71% stepwise savings) and Table 46.6 (national potential by option) — followed by heat-recovery hardware (wheels, plates, heat pumps, MVR), non-conventional sources, new techniques (two-stage, superheated-steam, RF/microwave), process control, and worked industrial case studies. The through-line: most drying inefficiency is avoidable, and cheap operational fixes (leaks, insulation, airflow) yield 25–50%, while heat recovery reaches 60–71%.

## 2. Key Viewpoints (with verbatim quotes + print pages)

### Viewpoint 1 — Drying is a top-tier industrial energy consumer

- Page: p.1074
- Quote: "Industrial dryers consume a significant part of the total energy used in manufacturing processes, 12% on the average."
- Interpretation: Sets the macro scale. Paper drying is even more extreme — Table 46.2 (p.1075) shows paper at 33% of sector energy. For a pulp/paper buyer this justifies treating the dryer section as the primary energy-cost battleground, ahead of the wet end.
### Viewpoint 2 — The thermodynamic minimum is far below practice

- Page: p.1079
- Quote: "Theoretically, the amount of heat required for the evaporation of 1 kg of moisture under standard conditions is 2200 to 2700 kJ/kg. The upper limit of this value refers to the removal of bound moisture."
- Interpretation: This 2200–2700 kJ/kg is the evaporative floor (latent heat + bound-water penalty). Actual units run 2700–8000 kJ/kg, so the gap defines the savings headroom. A procurement spec should benchmark any offer against this floor.
### Viewpoint 3 — Energy efficiency has a clean definition

- Page: p.1076
- Quote: "The energy efficiency h, is most frequently quoted in technical specifications. It commonly relates the energy used for moisture evaporation at the solids feed temperature (E_ev) to the total energy supplied to the dryer (E_t): h = E_ev / E_t"
- Interpretation: This is the supplier-facing index. It must not be confused with "drying efficiency" (Equation 46.6, accounting for exhaust enthalpy), which is generally higher. The chapter warns against conflating the two — critical when a vendor quotes a flattering number.
### Viewpoint 4 — Most heat is wasted in the exhaust, not the walls

- Page: p.1079
- Quote: "Statical data obtained from heat balances of convective dryers show that 20 to 60% of the heat supplied to the dryer is used for moisture evaporation, 5 to 25% for material heating, 15 to 40% for heat losses with the exhaust air, 3 to 10% for heat losses from dryer walls to the atmosphere, and 5 to 20% for other losses."
- Interpretation: Exhaust-air loss (15–40%) dwarfs wall loss (3–10%). The practical savings target is therefore exhaust recovery and airflow reduction, not better insulation alone — confirmed by Table 46.5 where insulation+airflow steps reach 50–53% while heat-recovery reaches 64–71%.
### Viewpoint 5 — Cheap operational fixes give 25–53%, heat recovery gives 64–71%

- Page: p.1080
- Quote: "Major capital expenditure … 6. Scheme 5 60% exhaust air recycle 192 0.20 64% … 8. Scheme 5 waste heat exchange with condensation 214 0.17 71%"
- Interpretation: Table 46.5 is the single most actionable table. It climbs from existing 0.53 kg steam/kg product to 0.17 (71% saving) via waste-heat exchange with condensation. It quantifies exactly how a buyer can stage capital: fix leaks (13%) → insulation (26%) → exhaust recycle (64%) → heat exchange with condensation (71%).
### Viewpoint 6 — Heat pumps and MVR are order-of-magnitude better per kWh

- Page: p.1085
- Quote: "The theoretical maximum SMER for conventional thermal drying is 1.55 kg/kWh (i.e., the latent heat of water evaporation at 100°C). A typical value of SMER achieved by a heat pump is 3 kg/kWh, which compares very favorably with conventional convective drying, for which values ranging from 0.5 to 1 kg/kWh are the norm."
- Interpretation: Specific Moisture Extraction Rate (SMER) flips the metric — water removed per kWh. Heat pumps (3) beat convective (0.5–1) ~3–6×. MVR does even better at 134 kJ/kg water, "20 times better than the typical adiabatic spray drying" (p.1086). Relevant for low-temperature, heat-sensitive web drying.
## 3. Research Method & Data Sources

Review/design-survey chapter synthesising monographs [1–5], national surveys (Baker & Reay U.K. [6]; Larreture & Laniau France [7]; Richardson & Jenson U.S. [8]; Hallström Sweden [9]) and equipment manufacturer judgement data (Richardson & Jenson). Empirical heat-balance statistics and case studies from the U.K. Energy Efficiency Office.

||||||
|---|---|---|---|---|
|Scale of energy use|National sector surveys, per-capita evaporation|Baker & Reay [6]; Larreture & Laniau [7]; Richardson & Jenson [8]|Tables 46.2, 46.7, 46.8|Country-specific; "relatively old and approximate data" (p.1081)|
|Efficiency definitions|Analytical indices (η=E_ev/E_t; thermal; instantaneous)|Kudra [20]; Ashworth [21]; Danilov & Leontchik [18]|Eqs 46.1–46.7, Figs 46.1–46.3|Conceptual; depends on moisture-content regime|
|Savings quantification|Stepped heat-balance + capital options|Bahu et al. [24]|Tables 46.3–46.6|Demonstrated ≥10% from analysis alone, 60–70% after modification|
|Heat-recovery hardware|Device efficiency indices|Industry practice|Fig 46.5; p.1082 list|Engineering-standard|
|Heat-pump/MVR|COP, SMER, Carnot limit|Strumiłło & Zyłła [33,34]; Mujumdar texts|Eqs 46.8–46.10|Practical COP 40–50% of Carnot|

## 4. Argumentation Process

- Scale & motivation — energy limited, costs rising; drying = 12% avg, paper 33% (p.1074–1075).
- Intensification — external/internal heat/mass transfer levers; raising textile-dryer T from 140→180°C cuts 25% (p.1076).
- Efficiency framework — η, thermal efficiency, instantaneous drying efficiency; energy use varies 2700–8000 kJ/kg vs 2200–2700 floor (p.1076–1079).
- Savings ladder — Tables 46.3–46.6: cheap operational steps (13–53%) then capital heat-recovery (64–71%) (p.1080–1081).
- Heat recovery — wheels/plates/pipes, heat pumps (COP, SMER), MVR (134 kJ/kg) (p.1082–1086).
- Non-conventional + new techniques — solar/biomass/induction/pulse; two-stage, superheated-steam, RF/microwave (p.1086–1090).
- Control — finish at max acceptable moisture; microcomputer control cuts 6.5–20% (p.1090–1092).
- Environment + case studies — paper-mill heat recovery £66,000/y; tundish dryer 97% cut, £65,000/y (p.1093–1096).
- Conclusions — recommend savings for ecology, not just money; respect energy as a resource.
## 5. Role in the Book

Ch46 is the Handbook's energy/economics capstone. It sits between the unit-operation chapters and the plant-engineering chapters (emission control Ch45, cost estimation Ch53, safety Ch48, control Ch49). Tables 46.5–46.8 are the quantitative backbone that Ch53's cost methods build upon, and the "improved dewatering of feedstock = 4% potential" row (Table 46.6) directly motivates Ch50 (mechanical dewatering). It pairs with Ch47 (heat pumps) and Ch49 (control) as the three high-leverage energy chapters for a buyer.

## 6. Strengths & Weaknesses

✅ Strengths: Unusually quantitative — gives the evaporative floor (2200–2700 kJ/kg), the full unit-consumption range, and the stepwise Table 46.5 with both kg-steam/kg-product and % savings, plus national-potential Table 46.6 and hardware-efficiency indices. The COP/SMER framing (p.1085) is the cleanest way to compare convective vs heat-pump vs MVR. Worked case studies (paper mill, tundish) give real £/GJ figures.
⚠️ Limitations/contestable: Data are "relatively old and approximate" (p.1081) and U.S./French/U.K.-centric; per-capita evaporation cites Czechoslovakia (p.1074). COP/SMER numbers are idealised; practical heat-pump payback "at the verge of profitability" in coal-cheap Poland (p.1085). No hygiene-substrate treatment, no explicit fluff/pulp numbers — the paper-mill row (33% of sector energy, Table 46.2) is the closest transfer. Some Table 46.7 entries are OCR-scrambled (e.g., "Cylinder 127753" p.1081).

## 7. Key Terms / Concepts

- Unit energy consumption q: p.1079, "The measure of energy consumption in a drying process is the unit energy consumption for the evaporation of 1 kg of moisture (q)"; timber 3000–4000, batch 2700–6500, thin/flexible (fabrics, paper) 5000–8000 kJ/kg.
- Energy efficiency η: p.1076, "h = E_ev / E_t" (energy for evaporation ÷ total supplied).
- Thermal efficiency η_T: p.1076, "η_T = (T_1 − T_2)/(T_1 − T_0)" (inlet/outlet/ambient air temperatures).
- Instantaneous drying efficiency η_D: p.1078, "energy used for evaporation at time t ÷ (input − output energy with outlet air) at time t".
- SMER: p.1085, "Specific Moisture Evaporation Rate (SMER) = amount of water evaporated kg / energy used kWh"; theoretical max 1.55 kg/kWh; heat pump typical 3 kg/kWh.
- COP: p.1084, "Coefficient of Performance (COP) = useful heat output / power input"; Carnot COP = T_condenser/(T_condenser − T_evaporator).
- Heat-recovery device efficiency: p.1082, "thermal wheel 75–90%; plate exchanger ≥70%; heat pipe ≥60%; scrubber ≥60%; two-section exchanger ≥50%."
- Drying efficiency (DEF context): p.1082, ratio of experimental to simulated energy efficiency — "The higher the DEF for a particular dryer type, the better is its construction."
## 8. Micro close-reading (ONE key paragraph)

p.1080 (Table 46.5 — Summary of Energy-Saving Schemes, existing dryer → scheme 8):

"Existing dryer — 0.53 [kg Steam/kg Product] —; Minor capital expenditure: 1. Rectify internal steam leak on heater 39 kW 0.46 13%; 2. Scheme 1 + reduce air leaks 54 0.44 18%; 3. Scheme 2 improve insulation of heater 79 0.40 26%; 4. Scheme 3 improve insulation of dryer and reduce airflow rate 150 0.26 50%; 5. Scheme 4 raise X_0 to 4% and reduce airflow rate 159 0.24 53%; Major capital expenditure: 6. Scheme 5 60% exhaust air recycle 192 0.20 64%; 7. Scheme 5 waste heat exchange with no condensation 178 0.22 59%; 8. Scheme 5 waste heat exchange with condensation 214 0.17 71%."

Sentence-by-sentence: (1) Baseline — the as-found dryer needs 0.53 kg steam per kg product. (2–5) Operational, minor-capital steps — each fix removes a discrete loss: steam leaks (13%), air leaks (18%), heater insulation (26%), dryer insulation + airflow (50%), higher final moisture + airflow (53%). (6–8) Capital heat-recovery steps — exhaust recycle (64%), heat exchange dry (59%), heat exchange with condensation (71%). The logic is cumulative and monotonic: every step the supplier skips is money left on the table.
💡 Standout line: "8. Scheme 5 waste heat exchange with condensation 214 0.17 71%" — proof that the right recovery hardware can cut specific steam use by nearly three-quarters.

## 9. Concept deep-dive

The savings ladder as a procurement instrument. Table 46.5 (p.1080) is the chapter's core concept — a single quantified path from 0.53 to 0.17 kg steam/kg product. Combined with Table 46.6 (p.1081), which ranks national potential, the buyer gets two axes: (a) what a given dryer can achieve stepwise, and (b) which class of fix moves the needle most — "Heat recovery from dryer exhaust (other than heat pump): 18.9×10⁹ MJ/y, 15%, High penetration" and "Vapor compression: 26.2×10⁹ MJ/y, 20%, Low penetration" (p.1081). The "Improved dewatering of feedstock: 5.3×10⁹ MJ/y, 4%, High" row is the quantitative bridge to Ch50 — mechanical dewatering is a small national number but high-penetration, low-cost lever.

Energy efficiency vs drying efficiency (the definitional trap). The text is explicit (p.1080): "care should be taken not to confuse drying efficiency with the more widely used concept of energy efficiency (e.g., Equation 46.1 and Equation 46.2), which generally yields a lower value than the drying efficiency." Energy efficiency η=E_ev/E_t (Eq 46.1) ignores exhaust enthalpy; drying efficiency (Eq 46.6) includes it and runs higher. A vendor quoting "drying efficiency" is citing the more flattering number.

SMER / COP as the cross-technology comparison metric. Eq 46.8 COP = useful heat / power input; Eq 46.10 SMER = kg evaporated / kWh. Theoretical max SMER = 1.55 kg/kWh (latent heat at 100°C). Convective real world 0.5–1; heat pump 3. This is the metric that lets a buyer compare a gas-fired convection dryer against a heat pump or MVR on a common denominator (water removed per unit energy), independent of fuel type.

## 10. Academic critique & open questions

- Data vintage: Table 46.6–46.8 are "relatively old and approximate" and only U.S./French/U.K. (p.1081); per-capita figures cite Czechoslovakia (p.1074). A 2026 buyer must re-anchor to current energy prices and local grids.
- The evaporative floor (2200–2700 kJ/kg) assumes the adiabatic equilibrium with no solids heating (p.1079); real bound-water and heat-sensitive-substrate penalties push practice far above it, but the chapter gives no substrate-specific correction for pulp/paper.
- COP/SMER idealisations: practical heat-pump COP is only 40–50% of Carnot (p.1084), and profitability is price-ratio dependent (India 1.5–3 y payback; Poland "at the verge" — p.1085).
- OCR damage: Table 46.7 "Cylinder 127753" (p.1081) is garbled; "127753" should read roughly "1277 (10⁶) … 90–92%".
- Open question 1: For a fluff-pulp or airlaid line, what is the achievable specific energy (kJ/kg water) and how close can it get to the 2200–2700 floor via exhaust recycling + heat exchange?
- Open question 2: Does raising final-residual-moisture tolerance (the "raise X_0 to 4%" lever, p.1080) conflict with SAP/absorbent-core moisture-spec limits — i.e., is the 53% step partly unavailable to hygiene lines?

## 11. Hygiene-material relevance & action cards

Overall relevance: ★★★★★ (highest — direct energy-cost argument for pulp/paper, nonwoven and coating lines).

Action Card H46-1 — Benchmark every supplier quote against the 2200–2700 kJ/kg evaporative floor. Insight: p.1079 — theoretical 2200–2700 kJ/kg; actual 2700–8000 kJ/kg. Action: Require suppliers to state specific energy consumption (kJ/kg water evaporated) and reject/penalise offers that cannot justify a gap above the floor. → 卫材相关性★★★★★｜Turns drying-energy cost into a measurable, comparable procurement metric per tonne of pulp/nonwoven.

Action Card H46-2 — Demand the Table 46.5 savings ladder in the bid. Insight: p.1080 — staged 13%→71% savings; heat exchange with condensation reaches 71%. Action: In the technical bid, ask which of schemes 1–8 the design includes; treat omission of exhaust recycle/heat exchange as a cost/quality red flag. → 卫材相关性★★★★★｜Quantifies how much steam (€/tonne) a better design would save on a fluff/paper dryer.

Action Card H46-3 — Specify exhaust-air heat recovery (wheel/plate ≥70–90%). Insight: p.1082 — thermal wheel 75–90%, plate ≥70%, heat pipe/scrubber ≥60%. Action: For any new coating/airlaid/drying oven, require a heat-recovery device with stated efficiency and ask for the energy-balance measurement points (Fig 46.4). → 卫材相关性★★★★★｜Exhaust is the 15–40% loss bucket; recovery is the biggest single saving on hygiene lines.

Action Card H46-4 — Apply the cheap fixes first (leaks, insulation, airflow). Insight: p.1080 — rectify steam leak 13%, reduce air leaks 18%, insulation 26%, insulation+airflow 50%. Action: Before capital projects, audit steam leaks, dryer insulation and airflow rate on existing lines; these need little/no capital. → 卫材相关性★★★★★｜Low-cost, fast-payback wins on running fluff/paper dryers.

Action Card H46-5 — Evaluate heat pump / MVR where low-temperature drying is needed. Insight: p.1085 — SMER heat pump 3 kg/kWh vs convective 0.5–1; MVR 134 kJ/kg, "20 times better than typical adiabatic spray drying" (p.1086). Action: For heat-sensitive webs (lotion, actives, SAP) or where electricity-vs-gas price favours it, ask suppliers about heat-pump/MVR and payback (India 1.5–3 y; Poland marginal). → 卫材相关性★★★★★｜Protects heat-sensitive substrates while cutting energy per kg water.

Action Card H46-6 — Use SMER/COP to compare fuel-type-agnostic bids. Insight: p.1085 — SMER = kg evaporated/kWh; theoretical max 1.55, heat pump 3, convective 0.5–1. Action: Require all bidders to report SMER (or equivalent water/kg-energy) so gas, steam and electric dryers are compared on one denominator. → 卫材相关性★★★★★｜Enables apple-to-apple energy comparison across fuel types.

Action Card H46-7 — Push dewatering upstream (links to Ch50). Insight: p.1081 — "Improved dewatering of feedstock: 5.3×10⁹ MJ/y, 4%, High" penetration. Action: Where the line includes a press/centrifuge/Thune section, demand the highest feasible mechanical dewatering before the dryer; it is a high-penetration, low-cost lever. → 卫材相关性★★★★★｜Mechanical water removal is far cheaper than evaporation — the dominant cost lever before the dryer.

Action Card H46-8 — Insist on finishing at max acceptable final moisture. Insight: p.1090 — "the drying should be finished at the maximum material moisture content that is acceptable"; over-drying wastes energy and raises explosion risk. Action: Set the residual-moisture spec deliberately (not conservatively) and require control to hold it (see Ch49). → 卫材相关性★★★★☆｜Over-drying fluff/SAP wastes energy and increases dust-explosion hazard.

## 12. Book-Map Quotes (Top representative quotes)

"Industrial dryers consume a significant part of the total energy used in manufacturing processes, 12% on the average." — p.1074 — the macro scale-setting sentence.
"Theoretically, the amount of heat required for the evaporation of 1 kg of moisture under standard conditions is 2200 to 2700 kJ/kg." — p.1079 — the evaporative floor every bid should be benchmarked against.
"8. Scheme 5 waste heat exchange with condensation 214 0.17 71%" — p.1080 — the headline proof that recovery hardware can cut specific steam use by ~71%.

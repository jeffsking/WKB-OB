---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_d87b98284b11c64e5b1a1494349c0353001a693ee6c0644e"
source_file: "ID · analysis_ch50.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch50.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch50.md.md

# Chapter 50 — Solid–Liquid Separation for Pretreatment of Drying Operation

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 50 (Shirato & Iwata) argues that mechanical solid–liquid separation is the most powerful pretreatment of a drying operation: removing water mechanically is vastly cheaper than evaporating it thermally. The authors frame the field via Table 50.1 (conditioning → concentration → separation → posttreatment), then present the selection logic keyed to cake-formation rate (Table 50.2), the Ruth filtration theory (Eqs 50.1–50.7, including cake compressibility α=α₀pⁿ), and a practitioner's catalogue of batch, semi-continuous and continuous filters, centrifugal filters, and expression (pressing) equipment. The economic spine is explicit: "it is essential to balance the additional cost of producing a dry cake against the thermal requirements of dryers" (p.1183). For pulp/paper and wet-laid/hydroentangled nonwoven lines, this is the press-section-vs-dryer-section trade-off made quantitative — every kilogram of water squeezed out upstream never has to be evaporated downstream.

## 2. Key Viewpoints (with verbatim quotes + print pages)

### Viewpoint 1 — Dewatering and drying are complementary; dewatering is the cheap half

- Page: p.1181
- Quote: "solid–liquid separation and drying are complementary operations in many industrial fields. This chapter will focus on the industrial practice and equipment for solid–liquid separation as a pretreatment process of drying operations."
- Interpretation: Sets the preprocessing frame. On a fluff-pulp or airlaid line, the press/centrifuge upstream is not a separate unit — it is the first, cheapest stage of the drying system, and its performance sets the dryer's evaporation load.
### Viewpoint 2 — The central economic rule: balance dewatering cost against dryer thermal load

- Page: p.1183
- Quote: "it is essential to balance the additional cost of producing a dry cake against the thermal requirements of dryers."
- Interpretation: This is the single most important sentence for a procurement strategist. It says: invest in mechanical dewatering (press/centrifuge) only up to the point where its marginal cost equals the marginal thermal saving in the dryer. It is the optimisation frontier between Ch50 and Ch46.
### Viewpoint 3 — Filtration resistance is governed by cake compressibility

- Page: p.1185
- Quote: "a = a₀ pⁿ … n is the cake compressibility, varying from 0 for rigid, incompressible cakes … to 1.0 for very highly compressible cakes. For most industrial slurries, n lies between 0.1 and 0.8."
- Interpretation: Pressure helps only for incompressible cakes (n≈0); for soft/compressible slurries (n→1) raising pressure barely increases rate (Eq 50.5: rate independent of pressure). This tells a buyer when a higher-pressure press pays off — and when it does not.
### Viewpoint 4 — Smaller particles mean wetter cake and slower filtration

- Page: p.1185
- Quote: "Decreased particle size results in lower filtration rates and higher moisture content of the cake, and sometimes in better washing efficiency."
- Interpretation: Flocculation/conditioning (polyelectrolytes, pH, temperature) to enlarge particles (p.1185) is the cheapest way to lower residual cake moisture before the dryer — directly relevant to pulp fines and SAP-slurry handling.
### Viewpoint 5 — Expression (pressing) removes extra water by compression, not pumping

- Page: p.1197
- Quote: "Expression is the separation of a liquid from a two-phase solid–liquid system by compression, due to movement of the retaining wall rather than the pumping of the solid–liquid system into a fixed chamber as in filtration."
- Interpretation: Distinguishes expression (squeeze) from filtration (pump). Expression pressures of 0.6–2.5 MPa (p.1197) and the membrane filter-press (two-step: filter then consolidate, p.1197) are the mechanical dewatering tools that get cake moisture below what filtration alone achieves — the last, cheapest water before the dryer.
### Viewpoint 6 — Selection is dictated by cake-formation rate

- Page: p.1184
- Quote: "The initial choice of the general class of equipment should be tentatively made based on the rate of cake growth. Specific equipment types are related to cake-formation rate as given in Table 50.2."
- Interpretation: Table 50.2 is the decision matrix — fast-filtering (>1 cm/min, >20% solids) → continuous vacuum/belt; slow-filtering ( cm/min) → pressure filters; dilute → thickening first. A buyer uses it to right-size the dewatering stage to the slurry actually produced.
## 3. Research Method & Data Sources

Practice/equipment-survey chapter grounded in filtration theory (Ruth's equation) and industrial catalogues (Mitsubishi Kakoki, Kurita). Theoretical aspects summarised; detailed theory referenced to Shirato et al. [2], Rushton et al. [3], Perry [5].

||||||
|---|---|---|---|---|
|Separation classification|Stage map (conditioning→posttreatment)|Porter et al. [1]|Table 50.1|Industry-standard|
|Filter selection|Cake-formation-rate guide|Porter et al. [1]|Table 50.2|Empirical bands|
|Cake filtration theory|Ruth's equation, compressibility|Shirato et al. [2]|Eqs 50.1–50.7|Widely validated|
|Equipment catalogue|Batch/continuous/centrifuge/expression descriptions|Mitsubishi, Kurita catalogues|Figs 50.2–50.21|Vendor practice|
|Expression theory|Constant-pressure expression|Shirato et al. [6,7]|§50.6|Referenced|

## 4. Argumentation Process

- Complementarity — dewatering + drying are one system (p.1181).
- Field map — Table 50.1 stages; conditioning to enlarge particles (p.1182–1183).
- Selection logic — cake-formation rate → Table 50.2 (p.1184).
- Theory — Ruth's filtration equation, compressibility α=α₀pⁿ, incompressible (Eq 50.4) vs compressible (Eq 50.5), constant-pressure V²∝u (Eq 50.6), particle-size and viscosity effects (p.1184–1185).
- Equipment — batch filters (press, leaf, plate, tray, tube, Nutsche, vacuum leaf); semi-continuous (pan, automatic press); continuous (drum, disk, belt) (p.1187–1196).
- Centrifugal — peeler/siphon/batch vs pusher/continuous (p.1196).
- Expression — compression device, squeezer, pressures 0.6–2.5 MPa (p.1197–1198).
- Conclusion — choose by objective, slurry properties, scale (p.1199).
## 5. Role in the Book

Ch50 is the upstream economic lever that Ch46 (energy) and Ch53 (cost) depend on: lower evaporation load W → smaller, cheaper dryer (Ch53 scaling) and lower thermal energy (Ch46). It is the quantitative anchor for the Table 46.6 "Improved dewatering of feedstock: 4% national potential, High penetration" row. Paired with Ch46 it gives the complete energy story: dewater mechanically, then evaporate the remainder efficiently.

## 6. Strengths & Weaknesses

✅ Strengths: Clear selection matrix (Table 50.2), the explicit cost-balance rule (p.1183), the compressibility insight (Eq 50.3, n 0.1–0.8), and a thorough equipment catalogue with figures. The expression section (§50.6) is the "last cheap water" mechanism most relevant to pulp/nonwoven dewatering.
⚠️ Limitations/contestable: Theory is summarised, not derived; Eq 50.2 (W=cV=material balance) and Eq 50.7 (K coefficient) are OCR-scrambled (p.1184–1185). No quantitative dewatering-vs-evaporation cost comparison is given — the balance rule (p.1183) is stated but not numerically demonstrated. No hygiene-substrate examples (pulp, SAP, nonwoven slurry). Notable by absence: no specific energy of mechanical dewatering (kJ/kg water removed by press vs evaporator) to make the economic case quantitative.

## 7. Key Terms / Concepts

- Cake vs depth filtration: p.1183, cake filtration blocks particles at the medium surface; depth filtration captures them in the medium interstices.
- Ruth's filtration equation: p.1184, dV/(A du) = p / μ (α W/A + R_m).
- Cake compressibility n: p.1185, α = α₀ pⁿ; n=0 rigid incompressible → 1.0 highly compressible; most slurries 0.1–0.8.
- Constant-pressure filtration: p.1184, V²/A² = K u (Eq 50.6); filtration time ∝ (cake thickness)².
- Cake-formation-rate guide: p.1184, Table 50.2 bands fast (>1 cm/min, >20%) → continuous vacuum; slow ( cm/min) → pressure; dilute → thickening.
- Filter press recess depth: p.1187, "depth of the recess is usually about 16 mm, giving a maximum cake thickness of about 32 mm."
- Expression: p.1197, separation by compression via moving retaining wall; time ∝ (cake thickness)²; pressures 0.6–2.5 MPa.
- Membrane/diaphragm press: p.1197, two-step — filtration at low pressure then consolidation at high expression pressure.
## 8. Micro close-reading (ONE key paragraph)

p.1183 (The economic balance — end of §50.2/start of §50.3 context):

"In general, it is essential to balance the additional cost of producing a dry cake against the thermal requirements of dryers. However, capillary pressures for 10-mm particles are so high that it is difficult to blow air or steam through a cake with such particles. If a rotary vacuum filter were chosen, there would be a limitation on moisture reduction for cakes with small particles unless an additional unit for mechanical expression was available."

Sentence-by-sentence: (1) Optimisation rule — weigh the cost of extra mechanical dewatering against the thermal energy it saves in the dryer (the Ch50↔Ch46 frontier). (2) Physical limit — fine particles (10-mm, likely "10-μm"/micrometre-tier) hold water by high capillary pressure, so air/steam blow-through cannot remove it. (3) Equipment implication — a rotary vacuum filter alone cannot reach low moisture on fine cakes; you need a mechanical-expression stage. The logic: mechanical dewatering has a hard limit set by particle size, and beyond that limit only extra mechanical expression (not the dryer) can help.
💡 Standout line: "it is essential to balance the additional cost of producing a dry cake against the thermal requirements of dryers" — the optimisation frontier every dewatering-vs-drying capital decision rests on.

## 9. Concept deep-dive

The dewatering–drying cost frontier (the chapter's core economic concept). The text states the rule (p.1183) but leaves it qualitative; the reader must supply numbers from Ch46/Ch53. Mechanically removing water (press/centrifuge) costs orders of magnitude less per kg than evaporation (Ch46: 2200–2700 kJ/kg floor for evaporation vs a few tens of kJ/kg for mechanical pressing). Therefore the optimum is found where the marginal cost of one more % cake dryness from the press equals the marginal thermal saving in the dryer. This is exactly the Ch46 Table 46.6 "Improved dewatering of feedstock = 4% national potential, High penetration" lever, now given an equipment basis.

Cake compressibility governs whether more pressure pays (Eq 50.3). α = α₀ pⁿ with n from 0 (rigid) to 1.0 (highly compressible). For incompressible cakes, Eq 50.4 gives rate ∝ p (pressure helps linearly); for n→1, Eq 50.5 gives rate independent of pressure. Practical implication for a buyer: if the slurry is compressible (e.g., fine cellulose/SAP flocs), buying a higher-pressure filter yields little — instead invest in conditioning (flocculation, pH, temperature, p.1185) to raise particle size and lower n. This reframes "bigger press" as often the wrong capital spend.

Expression = the last cheap water (§50.6). Filtration stops at the cake's drained moisture; expression (membrane press, squeezer) pushes further by compressing the retaining wall (0.6–2.5 MPa), with expression time ∝ (cake thickness)². The automatic membrane filter-press (Figs 50.10–50.12) does low-pressure filtration then high-pressure consolidation, producing "a cake with low residual moisture content" (p.1190). For fluff/SAP/pulp, this is the stage that shaves the final few % moisture before the (expensive) dryer.

## 10. Academic critique & open questions

- The balance rule (p.1183) is asserted, not demonstrated — no side-by-side kJ/kg or $/kg for mechanical vs thermal water removal. The chapter needs Ch46's numbers to be actionable.
- OCR damage: Eq 50.2 (material balance W=cV) and Eq 50.7 (K coefficient) are not cleanly recoverable (p.1184–1185); only Eqs 50.1, 50.3–50.6 are usable.
- "10-mm particles" (p.1183) is almost certainly a mis-OCR for micrometre-scale (μm) fine particles; capillary-pressure argument only makes sense for fine, not 10-mm, particles.
- No hygiene-substrate examples (pulp, SAP, wet-laid nonwoven slurry); the food/pharma examples (tray filter, squeezer for fish powder/shiitake, p.1198) are the closest analogues.
- Open question 1: For a fluff-pulp or airlaid furnish, what is the achievable residual cake moisture from a membrane press vs a rotary drum filter, and what evaporation load (kg/h) does each leave for the dryer?
- Open question 2: At current gas/electricity prices, where on the dewatering curve (Table 50.2 band) does the marginal press-cost equal the marginal dryer-thermal saving?

## 11. Hygiene-material relevance & action cards

Overall relevance: ★★★★★ (the single biggest lever in drying economics — mechanical dewatering is far cheaper than evaporation).

Action Card H50-1 — Treat the press/centrifuge as stage 1 of the dryer, optimise the boundary. Insight: p.1183 — "balance the additional cost of producing a dry cake against the thermal requirements of dryers." Action: Model the line as dewatering+drying; move the dewatering/drying boundary until marginal press cost = marginal dryer thermal saving (using Ch46 kJ/kg and Ch53 $/t). → 卫材相关性★★★★★｜Every kg mechanically removed never gets evaporated — the dominant cost lever.

Action Card H50-2 — Use Table 50.2 to right-size the dewatering stage. Insight: p.1184 — selection by cake-formation rate: fast (>1 cm/min, >20%) → continuous vacuum/belt; slow ( cm/min) → pressure; dilute → thickening first. Action: Characterise your slurry's cake-formation rate and concentration, then pick the filter class from the matrix; avoid over-specifying a pressure filter for a fast slurry. → 卫材相关性★★★★★｜Matches dewatering equipment to actual fluff/SAP/nonwoven slurry.

Action Card H50-3 — Check cake compressibility before buying higher pressure. Insight: p.1185 — α=α₀pⁿ; n 0.1–0.8; for compressible cakes rate is pressure-independent (Eq 50.5). Action: Determine n for your slurry; if compressible, invest in conditioning (flocculant/pH/temperature) rather than a higher-pressure press. → 卫材相关性★★★★★｜Avoids wasteful high-pressure capital on fine cellulose/SAP flocs.

Action Card H50-4 — Add a mechanical-expression stage for fine cakes. Insight: p.1183 — vacuum filter alone limited on small particles "unless an additional unit for mechanical expression was available"; expression 0.6–2.5 MPa (p.1197). Action: For fine pulp/SAP cakes, specify a membrane/diaphragm filter-press (two-step filtration then consolidation, p.1197) to reach low residual moisture. → 卫材相关性★★★★★｜Last cheap water before the expensive dryer.

Action Card H50-5 — Condition the slurry to enlarge particles. Insight: p.1185 — flocculation/coagulation, polyelectrolytes, pH, temperature, freezing increase particle size → higher filtration rate, lower cake moisture. Action: Trial flocculant/pH adjustment on the wet-laid or pulp slurry to cut downstream dryer load. → 卫材相关性★★★★★｜Cheapest moisture reduction is at the feed, not the dryer.

Action Card H50-6 — Consider centrifugal dewatering for high-throughput solids. Insight: p.1196 — peeler/siphon centrifuges give "large throughput capacities"; siphonic action accelerates filtration (10-m water-column suction at 500g, p.1196). Action: For continuous high-volume dewatering (e.g., pulp), evaluate pusher/peeler centrifuges against filters on $/t and residual moisture. → 卫材相关性★★★★☆｜High-capacity mechanical dewatering option for pulp lines.

Action Card H50-7 — Specify cake washing where product purity matters. Insight: p.1183 — cake washing by displacement or reslurry; plate-and-frame "most cost-effective" for high washing (p.1183). Action: For SAP or surfactant-containing streams, require a wash stage in the filter spec to remove soluble impurities before drying. → 卫材相关性★★★★☆｜Washing at dewatering stage protects final product purity.

Action Card H50-8 — Use the cost-balance to defend dewatering capex in the bid. Insight: p.1183 balance rule + Ch46 energy floor 2200–2700 kJ/kg. Action: In capital requests, quantify the dryer-energy saved (kg water × 2200–2700 kJ) by the proposed dewatering upgrade to justify the press/centrifuge spend. → 卫材相关性★★★★★｜Turns a dewatering purchase into a defensible energy-saving investment.

## 12. Book-Map Quotes (Top representative quotes)

"solid–liquid separation and drying are complementary operations in many industrial fields." — p.1181 — frames dewatering as part of the drying system.
"it is essential to balance the additional cost of producing a dry cake against the thermal requirements of dryers." — p.1183 — the dewatering-vs-drying optimisation frontier.
"Expression is the separation of a liquid from a two-phase solid–liquid system by compression, due to movement of the retaining wall rather than the pumping of the solid–liquid system into a fixed chamber as in filtration." — p.1197 — defines the "last cheap water" mechanism.


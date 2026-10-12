---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_b09dbabd71aa86d7586a6da1272445d2001a693ee6c0644e"
source_file: "ID · analysis_ch47.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch47.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch47.md.md

# Chapter 47 — Heat Pump Drying Systems

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 47 (Chou & Chua) presents the heat-pump dryer (HPD) as an energy-recovering, low-temperature drying route whose two decisive advantages are (a) recovery of latent heat from the moisture-laden exhaust and (b) precise control of drying-gas temperature and humidity (p.1101). The authors build from refrigeration basics (COP, Carnot limit, SMER) through configurations (batch/continuous, single/two-stage), real-time quality control, time-varying operating schemes (intermittent, cyclic — saving 25–61% drying time), and industrial applications (timber, food, fluids, RF/IR/solar-assist, vacuum). Table 47.1 is the headline comparison: HPD SMER 1.0–4.0 kg/kWh and drying efficiency 95% vs hot-air 0.12–1.28 and 35–40%. The economics section shows HPD can cut operating cost up to 70% versus a recuperative dryer, with payback 2–3 y (p.1126). For hygiene lines, HPD is the route that protects heat-sensitive substrates (lotion, actives, SAP) while recovering energy.

## 2. Key Viewpoints (with verbatim quotes + print pages)

### Viewpoint 1 — HPD's edge is exhaust energy recovery + humidity/temperature control

- Page: p.1101
- Quote: "The principal advantages of heat pump dryers emerge from the ability of the heat pumps to recover energy from the exhaust gas as well as their ability to control the drying gas temperature and humidity."
- Interpretation: This is the HPD thesis. Unlike a convective dryer that vents saturated hot air, the HPD condenser reclaims the latent heat and the evaporator dehumidifies — and it does so at a controllable low temperature, ideal for heat-sensitive webs.
### Viewpoint 2 — HPD beats hot-air drying on SMER and efficiency by a wide margin

- Page: p.1107
- Quote: "SMER(kg water/kWh): Hot Air Drying 0.12–1.28; Vacuum Drying 0.72–1.2; Heat Pump 1.0–4.0. Drying efficiency(%): Hot Air 35–40; Vacuum 70; Heat Pump 95."
- Interpretation: Table 47.1 quantifies the HPD advantage — ~3–8× the specific moisture extraction of hot-air drying and 95% drying efficiency. These are the numbers a buyer uses to justify HPD capital against a conventional convection oven.
### Viewpoint 3 — Low temperature protects heat-sensitive products

- Page: p.1104
- Quote: "Heat pump dryers can significantly improve product quality by drying at low temperatures. At low temperatures, the drying potential of the air can be maintained by further reduction of the air humidity."
- Interpretation: HPD drying range is –20 to 100°C (with aux heating) and RH 15–80% (p.1104). This is exactly the regime needed to dry lotion-laden, actives-containing or SAP-bearing hygiene webs without thermal degradation.
### Viewpoint 4 — Practical COP is only 40–50% of Carnot

- Page: p.1104
- Quote: "In practice, the actual efficiency of the heat pump is usually 40 to 50% of the theoretical Carnot efficiency (Geeraert, 1976; Strumiłło and Zyłła, 1985)."
- Interpretation: The Carnot COP (Eq 47.2, T_cond/(T_cond−T_evap)) is the ceiling; real HPD delivers roughly half. A buyer should discount vendor COP claims by ~50% and tie the argument to SMER (kg water/kWh) instead.
### Viewpoint 5 — Time-varying (intermittent/cyclic) operation saves time and energy

- Page: p.1111
- Quote: "employing intermittent temperature drying profile can result in saving drying time by about 25, 48 and 61% for a 1/4, a 1/2, and a 2/3, respectively."
- Interpretation: Fixed-temperature drying is sub-optimal because material properties change as moisture leaves (p.1110). Prescribed intermittent/cyclic profiles both cut drying time and reduce heat-induced quality damage — directly relevant to controlling case-hardening on a coated web.
### Viewpoint 6 — HPD cuts operating cost up to 70% with 2–3 y payback

- Page: p.1126
- Quote: "heat pump dryers can reduce the operating cost as much as 70% in comparison to a recuperative heating dryer. … a heat pump dryer designed for a drying capacity of 200 kg/h has a payback period of 2 to 3 y."
- Interpretation: The economic close. Zylla et al. (1982) and Pendyalala et al. (1986) give the procurement numbers: up to 70% OPEX reduction, 2–3 y payback, and payback shortens as exhaust humidity (recoverable latent load) rises (3.2→2.0 y when RH 0.4→0.7). More recoverable moisture = faster payback.
## 3. Research Method & Data Sources

Review/technology chapter synthesising refrigeration theory, experimental HPD studies (Chou/Chua/Hawlader/Mujumdar group; Alves-Filho & Strømmen; Bannister et al.; Prasertsan; Rossi et al.) and economic analyses (Zylla et al. 1982; Pendyalala et al. 1986; Brundrett 1987).

||||||
|---|---|---|---|---|
|Refrigeration theory|COP, Carnot, SMER, SEC|Strumiłło & Zyłła 1985; Geeraert 1976|Eqs 47.1–47.4|Standard|
|Performance comparison|Cross-dryer table|Perera & Rahman 1990|Table 47.1|Accepted|
|Config optimisation|Single vs two-stage COP|Perry 1981|Fig 47.9|Demonstrated|
|Time-varying schemes|Experimental/intermittent/cyclic|Chou et al. 2000; Devahastin & Mujumdar 1999|Table 47.2, Figs 47.14–47.19|Lab/pilot|
|Applications|Timber/food HPD data|Bannister et al. 1999; Rossi et al. 1992|Tables 47.3–47.5|Field|
|Economics|Cost per litre water, payback|Zylla et al. 1982; Pendyalala 1986; Brundrett 1987|Fig 47.27|Demonstrated|

## 4. Argumentation Process

- Basics — HP components, cycle, COP/Carnot (p.1102–1104).
- Principle — evaporator dehumidifies exhaust, condenser returns heat; SMER/SEC (p.1104–1105).
- Pros/cons — low-temp quality, CFC/maintenance/capital limits (p.1106).
- Efficiency — Table 47.1 HPD vs hot-air/vacuum (p.1107).
- Configuration — batch/continuous, single/two-stage COP gain (p.1107–1108).
- Control — real-time thermovision/PID for colour/AA (p.1108–1110).
- Time-varying — intermittent/cyclic saves 25–61% time (p.1110–1115).
- Applications — timber (Table 47.3), food (Table 47.4), fluids/RF/IR/solar/vacuum (p.1117–1123).
- Airflow, refrigerants, versatility (p.1124–1125).
- Economics — cost/litre water, 70% OPEX cut, 2–3 y payback (p.1125–1126).
- Future — multiple-chamber HPD (p.1128). Conclusion (p.1128).
## 5. Role in the Book

Ch47 is the practical energy-efficiency chapter that operationalises Ch46's heat-recovery principle via a concrete technology, and the low-temperature counterpart to Ch48's safety concerns (low-temp drying also reduces fire/explosion risk). It complements Ch46 (energy) and Ch53 (cost) by giving both the SMER/efficiency evidence and the payback economics a strategist needs to choose HPD over convection. Its quality-control sections (§47.8, §47.9.6) also foreshadow Ch49 (control).

## 6. Strengths & Weaknesses

✅ Strengths: The cleanest cross-technology comparison in the book (Table 47.1: HPD 95% efficiency, SMER 1–4), quantified time-saving (25–61%), field timber/food data (Tables 47.3–47.5), and a real economic case (70% OPEX cut, 2–3 y payback, Fig 47.27 cost-per-litre-water). The refrigerant discussion (Table 47.6–47.7, ammonia/propane natural fluids) is forward-looking.
⚠️ Limitations/contestable: Eq 47.4 (SEC–COP relation) is OCR-scrambled (p.1105). HPD is explicitly unsuited to large-air dryers (flash/spray, p.1102). Capital cost is higher (p.1106) and CFC phase-out creates refrigerant-uncertainty (p.1123). Studies are mostly food/marine/timber — no hygiene-substrate (lotion/SAP/web) data; the transfer is by analogy.

## 7. Key Terms / Concepts

- COP: p.1104, "COP = useful heat output / power input" (Eq 47.1).
- Carnot COP: p.1104, "COP_carnot = T_condenser / (T_condenser − T_evaporator)" (Eq 47.2).
- SMER: p.1104, "SMER = amount of water evaporated / energy input to the dryer (kg/kWh)" (Eq 47.3).
- Actual vs Carnot: p.1104, "actual efficiency … usually 40 to 50% of the theoretical Carnot efficiency."
- HPD operating range: p.1104, "–20°C to 100°C (with auxiliary heating) and relative humidity 15 to 80%."
- Two-stage COP gain: p.1108, Figure 47.9 "significant improvement in the heat pump energy efficiency from a single to two-stage dryer."
- Intermittent time saving: p.1111, 25/48/61% for a=1/4, 1/2, 2/3.
- Cost per litre water: p.1125, "Total cost of removing one liter of water = (total variable cost + total fixed cost) / total water removed."
- Refrigerants: p.1123, CFCs/HCFCs (R12, R22, R502); natural alternatives ammonia R717, propane R290, steam/air.
## 8. Micro close-reading (ONE key paragraph)

p.1107 (Table 47.1 — Comparing Heat Pump Drying with Other Drying Systems):

"Parameter | Hot Air Drying | Vacuum Drying | Heat Pump Drying | SMER(kg water/kWh) 0.12–1.28 | 0.72–1.2 | 1.0–4.0 | Drying efficiency(%) 35–40 | 70 | 95 | Operating temperature range(°C) 40–90 | 30–60 | 10–65 | Capital cost Low | High | Moderate | Running cost High | Very high | Low."

Sentence-by-sentence: (1) SMER — HPD (1.0–4.0) dominates hot-air (0.12–1.28) and matches/exceeds vacuum. (2) Efficiency — HPD 95% vs hot-air 35–40%; the heat-recovery loop closes the energy gap. (3) Temperature — HPD 10–65°C is the low-temperature band that protects heat-sensitive product. (4) Capital — HPD is moderate (not the high capital of vacuum). (5) Running cost — HPD is low, the decisive OPEX advantage. The table is the one-slide case for specifying HPD.
💡 Standout line: "Drying efficiency(%) … Heat Pump 95" — HPD recovers so much latent heat it reaches 95% drying efficiency versus 35–40% for hot air.

## 9. Concept deep-dive

SMER/COP as the HPD performance language. COP (Eq 47.1) and the Carnot ceiling (Eq 47.2) define the refrigeration side; SMER (Eq 47.3, kg water/kWh) defines the drying side. The chapter's key caveat: actual COP is only 40–50% of Carnot (p.1104), so a buyer should evaluate HPD on SMER (water/kg energy), which is directly comparable to Ch46's convective 0.5–1 kg/kWh and heat-pump 3 kg/kWh. Table 47.1 confirms HPD SMER 1.0–4.0 — the highest of any class.

Two-stage and multiple-chamber HPD raise effectiveness. Figure 47.9 shows two-stage COP significantly above single-stage (p.1108); §47.16 extends this to one HP serving multiple chambers sequentially, cutting capital (one HP vs several) and improving economics because the HP runs near-optimal while chambers dry at different rates (p.1128). For a hygiene plant with several low-temperature ovens, this "one HP, many chambers" architecture is the capital-saving deployment.

Time-varying operation as quality + energy lever. Fixed conditions are sub-optimal because material properties shift as moisture leaves (p.1110). Prescribed intermittent/cyclic air-temperature profiles (Fig 47.14) deliver 25–61% time savings (p.1111) and, via real-time control (thermovision camera + PID, Fig 47.12; hypodermic thermocouple + PID, Fig 47.13), hold surface temperature below the threshold that triggers non-enzymatic browning and ascorbic-acid degradation (§47.9.6). This is the quality-control mechanism that matters for actives-bearing hygiene webs.

## 10. Academic critique & open questions

- Eq 47.4 (SEC–COP relation) is OCR-scrambled (p.1105) and not usable as printed; only Eqs 47.1–47.3 are clean.
- HPD explicitly excluded for large-air dryers (flash/spray, p.1102) — so its hygiene relevance is to low-airflow ovens (coating, airlaid, chamber dryers), not high-volume spray.
- Capital cost higher (p.1106); CFC/HCFC phase-out (p.1123) creates refrigerant-selection uncertainty — though ammonia/propane/CO₂ natural fluids are endorsed.
- All performance data are food/marine/timber; no lotion/SAP/nonwoven-web HPD data exists, so hygiene transfer is by analogy.
- Open question 1: For a lotion- or SAP-bearing hygiene web, what is the achievable HPD SMER and does the low-temperature band (10–65°C) avoid actives degradation while still hitting throughput?
- Open question 2: At current electricity-vs-gas ratios, where does HPD's 2–3 y payback (p.1126) fall for a continuously-run hygiene oven versus a convection retrofit with exhaust heat recovery (Ch46)?

## 11. Hygiene-material relevance & action cards

Overall relevance: ★★★★☆ (genuine energy-efficiency + low-temperature route that protects heat-sensitive substrates; slightly below Ch46/Ch50/Ch53 because HPD suits low-airflow ovens, not high-volume spray).

Action Card H47-1 — Specify HPD where low-temperature drying protects actives/lotion/SAP. Insight: p.1104 — HPD dries at –20 to 100°C, RH 15–80%, "significantly improve product quality by drying at low temperatures." Action: For coating/airlaid lines carrying heat-sensitive lotion or actives, require an HPD (or low-temp dehumidifying) option and compare against convection on product quality, not just cost. → 卫材相关性★★★★★｜Low-temp HPD avoids thermal degradation of actives and lotion on hygiene webs.

Action Card H47-2 — Benchmark bids on SMER (kg water/kWh), not COP. Insight: p.1104 — actual COP is only 40–50% of Carnot; HPD SMER 1.0–4.0 (Table 47.1). Action: Require every HPD bid to state SMER and discount any COP claim by ~50%; compare to convective 0.5–1 kg/kWh (Ch46). → 卫材相关性★★★★★｜Common denominator to rank HPD vs convection per kg water.

Action Card H47-3 — Use Table 47.1 to justify HPD capital on efficiency. Insight: p.1107 — HPD drying efficiency 95% vs hot-air 35–40%; running cost Low vs High. Action: In the capital request, cite the 95% vs 35–40% efficiency gap as the OPEX-saving basis for the higher HPD capital. → 卫材相关性★★★★★｜Quantifies the efficiency premium justifying HPD spend.

Action Card H47-4 — Exploit the 70% OPEX-cut / 2–3 y payback economics. Insight: p.1126 — HPD "reduce the operating cost as much as 70%"; 200 kg/h unit payback 2–3 y; payback shortens as exhaust RH rises 0.4→0.7 (3.2→2.0 y). Action: Model HPD payback using your line's exhaust humidity (more recoverable moisture = faster payback); pair with Ch53 FCI method. → 卫材相关性★★★★★｜Turns HPD into a defensible energy-saving capital case.

Action Card H47-5 — Use time-varying drying to cut time and protect quality. Insight: p.1111 — intermittent profiles save 25–61% drying time; §47.9.6 reduces colour change up to 87% and AA loss up to 20%. Action: For quality-critical webs, request an intermittent/cyclic temperature schedule with feedback control rather than fixed-temperature operation. → 卫材相关性★★★★☆｜Cuts energy/time and reduces heat-induced quality damage on coated webs.

Action Card H47-6 — Prefer ammonia/propane/CO₂ refrigerants. Insight: p.1123–1124 — natural fluids (NH₃ R717, propane R290, CO₂, steam/air) have zero ODP/GWP; ammonia favourable 30–80°C. Action: Specify ozone-friendly refrigerant in any HPD purchase to avoid CFC/HCFC phase-out risk. → 卫材相关性★★★★☆｜Future-proofs the refrigerant choice against regulation.

Action Card H47-7 — Consider one-HP-multiple-chamber architecture. Insight: p.1128 — single low-capacity HP serving several chambers cuts capital; HP runs near-optimal while chambers dry at different rates. Action: Where several low-temp ovens exist, evaluate a shared HP with sequential air scheduling instead of per-oven units. → 卫材相关性★★★★☆｜Capital-saving deployment for multi-oven hygiene plants.

Action Card H47-8 — Verify HPD suitability (low airflow) before specifying. Insight: p.1102 — HPD "not suited for HP operation" for dryers needing large drying air (flash/spray). Action: Confirm the target hygiene oven is low-airflow (coating chamber, airlaid, tray) before committing to HPD; otherwise use Ch46 exhaust recovery. → 卫材相关性★★★★☆｜Avoids misapplying HPD to high-airflow dryers.

## 12. Book-Map Quotes (Top representative quotes)

"The principal advantages of heat pump dryers emerge from the ability of the heat pumps to recover energy from the exhaust gas as well as their ability to control the drying gas temperature and humidity." — p.1101 — the HPD thesis.
"SMER(kg water/kWh): Hot Air Drying 0.12–1.28; Vacuum Drying 0.72–1.2; Heat Pump 1.0–4.0. Drying efficiency(%): … Heat Pump 95." — p.1107 — the headline performance comparison.
"heat pump dryers can reduce the operating cost as much as 70% in comparison to a recuperative heating dryer. … payback period of 2 to 3 y." — p.1126 — the economic case.


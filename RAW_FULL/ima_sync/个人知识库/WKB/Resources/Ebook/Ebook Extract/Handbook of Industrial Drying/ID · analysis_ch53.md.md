---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_221392871e0eb3755001d70ed42a6089001a693ee6c0644e"
source_file: "ID · analysis_ch53.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch53.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch53.md.md

# Chapter 53 — Cost-Estimation Methods for Drying

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 53 (Sztabert & Kudra) turns drying engineering into a purchasable, defensible estimate. The authors note that reliable fixed-capital-investment (FCI) and operating-cost estimates are essential for equipment selection and competitive comparison, and that the dryer is only one component of a system that may include preprocessing, feeders, gas cleaners and solvent recovery. They present shortcut empirical methods: inflation correction via the Marshall & Swift (M&S) and Chemical Engineering (CE) indices (Table 53.1), capacity scaling with exponent n (Eq 53.2; n≈0.6 default; Table 53.2), installed-cost factors (2.25× FOб for carbon steel, 2.75× for stainless), and a full fixed/variable cost factor method (§53.3–53.4). The chapter culminates in a complete worked example — a spray dryer for laundry detergent — that produces a bottom-line $0.089/kg unit drying cost (fixed $41.09/t + variable $47.78/t). The through-line for a buyer: every quote can be normalised to FCI, annual fixed cost, and unit cost per tonne, then benchmarked.

## 2. Key Viewpoints (with verbatim quotes + print pages)

### Viewpoint 1 — The dryer is only one part of a costed system

- Page: p.1247
- Quote: "A dryer itself is only one component of the overall drying system. The system may comprise preprocessing equipment (extruders, grinders, mixers, and blenders), feeders, product-discharge devices, and postprocessing equipment such as gas cleaners (cyclones, filters, and scrubbers) and solvent-recovery systems."
- Interpretation: A supplier's "dryer price" is not the system cost. For a hygiene line (coating oven + airlaid former + defibration + abatement), the buyer must cost the whole battery-limits system or the estimate is meaningless.
### Viewpoint 2 — Inflation must be corrected before any number is reused

- Page: p.1246
- Quote: "Updated cost / Original cost = M&S Index at updated time / M&S Index at the time of original cost (53:1)"
- Interpretation: Any literature/vendor cost in old dollars is useless without index correction. M&S rose from 895.1 (1989) to 1178.5 (2004) (Table 53.1), so a 1995 quote must be ×(current/1995) before comparison — directly relevant when auditing a supplier's "we've always built it this way" price.
### Viewpoint 3 — Capacity scales with a sub-unity exponent

- Page: p.1246
- Quote: "Predicted cost / Original cost = [desired capacity / original capacity]^n … If not given … n = 0.6 can be taken for rough estimation."
- Interpretation: Doubling capacity costs roughly 2^0.6 ≈ 1.52×, not 2×. This is the buyer's defence against linear "per-tonne scales with size" claims and the basis for right-sizing a pulp/nonwoven dryer. Table 53.2 gives equipment-specific n (cyclone 0.61, cloth collector 0.78, roll crusher 0.97, venturi scrubber 0.46).
### Viewpoint 4 — Installed cost is ~2.25–2.75× the equipment FOB price

- Page: p.1250
- Quote: "To roughly estimate the total direct cost of the drying installation, it is recommended to multiply the equipment FOB cost by a factor of 2.25 if the equipment is made of carbon steel or by 2.75 if stainless-steel equipment is used."
- Interpretation: This single factor converts a vendor equipment quote into a battery-limits direct cost — the fastest sanity check a procurement strategist has. Stainless (needed for most hygiene lines) carries a 22% premium on the multiplier alone.
### Viewpoint 5 — Material of construction is a 1.5–3× cost multiplier

- Page: p.1249
- Quote: "drying equipment built of 304-stainless steel typically costs from 1.5 to 1.7 times more than that made of carbon steel and 2 to 3 times more if built of titanium."
- Interpretation: For fluff/SAP/coating lines requiring stainless or clad construction, the buyer should expect a 50–70% equipment premium over carbon steel — a negotiable, specifiable cost driver.
### Viewpoint 6 — The worked example yields a fully-loaded unit cost

- Page: p.1257
- Quote: "Then, the expected unit cost of drying of the laundry detergent in the year 2006 will most likely be US$41.09/t + US$47.78/t = US$88.87/t = US$0.089/kg."
- Interpretation: This is the headline deliverable of the chapter — a normalised, all-in unit drying cost. A hygiene buyer can demand the same decomposition (fixed + variable, $/t of dry product) from any supplier and compare offers apples-to-apples regardless of dryer type.
## 3. Research Method & Data Sources

Empirical/shortcut cost-estimation synthesis drawing on process-industries practice [1–9] and drying-specific cost correlations [10,13,21,22]. Method-led with vendor data preferred for definitive estimates.

||||||
|---|---|---|---|---|
|Inflation correction|M&S / CE index ratios|Table 53.1 (1989–2004) [11]|Eq 53.1|US$ market; local adjustment needed [12]|
|Capacity scaling|Power-law (Q)^n|Table 53.2 exponents [10]|Eq 53.2|n varies with design detail; n=0.6 default|
|Equipment cost|A·Q^c·(M&S) correlation|Table 53.3 (A,c per dryer)|Eq 53.5|M&S=1100 baseline; ignores material properties (underestimate)|
|Installed/total cost|Factor method|§53.2 factors|2.25/2.75× FOB|Rough; FCI may reach 3× equipment|
|Fixed cost|% of FCI factors|§53.3 factors|Table 53.5|Developed-country basis; local vary|
|Variable cost|Heat/mass balance + utility prices|Table 53.4, Eq 53.6|Table 53.6|Energy-price volatile; ±30% typical [29,30]|

## 4. Argumentation Process

- Frame — FCI + fixed + variable costs essential; dryer is part of a system (p.1247).
- Inflation & scaling — M&S/CE update (Eq 53.1), capacity power-law (Eq 53.2, n=0.6) (p.1246).
- Equipment cost — spray-dryer Eq 53.4; general Eq 53.3/53.5 with Table 53.3 A,c; material multipliers (p.1247–1249).
- Installed & total cost — FOB→assembly/freight→installed (2.25/2.75×); building/utility factors (p.1250).
- Fixed cost — % of FCI factors (depreciation, interest, taxes, maintenance, overhead) (p.1251–1252).
- Variable cost — raw material, energy (volatile, Eq 53.6), labor rules, working capital (p.1252–1253).
- Worked example — spray dryer for detergent, full Table 53.5/53.6 → $0.089/kg (p.1253–1257).
- Summary — correct for inflation and geography; ±30% reliability.
## 5. Role in the Book

Ch53 is the procurement/economics capstone. It operationalises the energy data of Ch46 (specific energy → utility cost) and the dewatering lever of Ch50 (lower evaporation load → smaller, cheaper dryer) into dollars. It pairs with Ch46 (energy) and Ch47 (heat-pump economics) and underpins any "should we buy/recover/upgrade" decision a strategist faces. It closes the loop the rest of the book opens: unit operation → energy → cost → decision.

## 6. Strengths & Weaknesses

✅ Strengths: Gives immediately usable shortcuts — M&S/CE update (Eq 53.1), n=0.6 default scaling, the 2.25/2.75× FOB→direct-cost rule, Table 53.3 A,c for ~15 dryer types, and a complete worked example with both tables. The fixed-cost factor list (§53.3) is a checklist a buyer can demand from any vendor.
⚠️ Limitations/contestable: US/North-America centric; "published cost data refer to a specific year and apply to … North America" (p.1257). Equation 53.3 is OCR-scrambled (the "30 + 17.77T + 36.74Q" form, p.1248, is not cleanly recoverable). Reliability is only ±30% (p.1257). Energy-price volatility handled only by Eq 53.6 with Ulrich coefficients — fuel prices (Table 53.4) are 2001–2006 vintage. No hygiene-substrate example; the detergent spray-dryer analogue is the closest transfer.

## 7. Key Terms / Concepts

- FCI (Fixed Capital Investment): p.1247, total fixed investment of the drying system; "may be much higher, even by 3 times of the equipment cost" (p.1250).
- FOB vs installed cost: p.1247, "free-on-board (FOB) cost and the installed cost of the equipment"; installed covers purchase + installation + piping/wiring/instrumentation.
- M&S and CE Indices: p.1246, inflation indices for updating equipment/plant cost in US$; Table 53.1 lists 1989–2004.
- Scaling exponent n: p.1246, Eq 53.2 cost ratio = (capacity ratio)^n; n≈0.6 default; Table 53.2 lists equipment-specific values.
- Factor method (installed): p.1250, total direct cost ≈ 2.25× FOB (carbon steel) or 2.75× FOB (stainless).
- Fixed cost factors: p.1251–1252, depreciation 7–9% of installed; interest 3–5% of FCI; taxes/rent 2%; insurance 1%; maintenance 5–10% of FCI; overhead 6% of FCI.
- Variable cost: p.1252, "raw materials, cost of product degradation, costs of energy and utilities, direct labor … interest on working capital, royalties, variable part of maintenance."
## 8. Micro close-reading (ONE key paragraph)

p.1250 (Installed-cost factor method):

"To roughly estimate the total direct cost of the drying installation, it is recommended to multiply the equipment FOB cost by a factor of 2.25 if the equipment is made of carbon steel or by 2.75 if stainless-steel equipment is used. These figures include the cost of piping, instrumentation, electrical connections, insulation, building space, and engineering when applied to spray, flash, rotary, or fluid-bed continuous dryers."

Sentence-by-sentence: (1) Rule — total direct cost ≈ 2.25× (carbon) or 2.75× (stainless) the equipment FOB price. (2) Inclusions — the multiplier already wraps piping, instrumentation, electrical, insulation, building space and engineering. The logic is a single-step "factor estimate" that converts a vendor's equipment quote into a battery-limits direct cost without a full takeoff — the fastest defensible number a strategist can produce.
💡 Standout line: "multiply the equipment FOB cost by a factor of 2.25 … or by 2.75 if stainless-steel" — one number that turns any equipment quote into a system cost.

## 9. Concept deep-dive

The factor method as the buyer's universal translator. The chapter's core concept is that any drying investment can be decomposed into (a) equipment FOB, (b) installed cost via factors (assembly 30–99% of FOB, freight 7%, then ×2.25/2.75), (c) total direct cost (building 20–35%/15%, utility 20–40%), and (d) FCI with contractor fee 10–27%, contingencies 10–30%, owner costs 5–15% (p.1250–1251). Table 53.5 demonstrates the chain end-to-end: FOB 1,757,000 → installed 2,632,000 → direct 3,948,000 → FCI 5,882,520. A buyer receiving only an FOB number can immediately build the full ladder and challenge an under-scoped bid.

Equipment cost via A·Q^c (Eq 53.5) and material multipliers. Table 53.3 gives A and c for each dryer type so P = (M&S Index)·A·Q^c (demonstrated p.1255: 1221.7 × 47 × 570^0.52 = 1,554,000 for a spray dryer). Critically, the text warns dryer cost "depends mainly on its size and the material of construction" and that throughput/evaporation "should not be used as parameters for cost estimation" because the same indices can be obtained at different sizes by manipulating operating conditions (p.1247). 304-SS multiplies cost 1.5–1.7×; titanium 2–3× (p.1249). This is the quantifiable reason hygiene lines (stainless-clad) cost more and why dewatering upstream (Ch50) pays: lower evaporation Q → smaller, cheaper dryer.

Fixed vs variable cost split (the operating lens). §53.3–53.4 separate fixed charges (independent of production level: depreciation, interest, taxes, insurance, maintenance, overhead) from variable costs (scale with output: raw material, degradation, energy, labor, working-capital interest). The worked example shows fixed $41.09/t and variable $47.78/t — energy (fuel 1,004,400 + electricity 86,184) dominating variable cost. For a hygiene buyer, this isolates the energy line (linked to Ch46) as the lever for unit-cost reduction.

## 10. Academic critique & open questions

- Geographic narrowness: "published cost data … apply to a location of the plant in North America" (p.1257); Plavsic's direct-factoring method [12] for non-US is "beyond the scope."
- Equation 53.3 OCR damage (p.1248): the "C = 30 + 17.77T + 36.74Q" form is scrambled; only Eq 53.5 (P = A·Q^c·M&S) is cleanly usable, via the worked example.
- Reliability only ±30% (p.1257); "no warranty can be made concerning the accuracy of the published correlations."
- Energy-price inputs (Table 53.4) are 2001–2006; Eq 53.6 utility model needs current Ulrich coefficients.
- Open question 1: Can the factor method be parameterised for a hygiene line (stainless airlaid former + coating oven + SAP handling) to produce a defensible FCI without vendor quotes?
- Open question 2: How does the fixed/variable split shift when heat-recovery (Ch46) or mechanical dewatering (Ch50) is added — does the higher FCI (recovery capital) get repaid within the variable-energy line at current gas/electricity ratios?

## 11. Hygiene-material relevance & action cards

Overall relevance: ★★★★★ (turns drying engineering into a purchase argument — the procurement strategist's core chapter).

Action Card H53-1 — Demand the full cost ladder, not just an equipment price. Insight: p.1250 — total direct cost ≈ 2.25× (CS) or 2.75× (SS) FOB; FCI can be 3× equipment (p.1250). Action: Require every bid to state FOB, installed, direct and FCI separately; rebuild the ladder yourself from any lone FOB number. → 卫材相关性★★★★★｜Prevents under-scoped bids on coating/airlaid/drying systems.

Action Card H53-2 — Index-correct every historical or competitor quote. Insight: p.1246 — Updated cost = Original × (M&S_now / M&S_then); M&S 895 (1989) → 1178 (2004). Action: Before comparing suppliers or old internal estimates, normalise all to the current M&S/CE index. → 卫材相关性★★★★★｜Apples-to-apples cost comparison across years and vendors.

Action Card H53-3 — Use n≈0.6 to right-size and challenge linear pricing. Insight: p.1246 — cost scales as capacity^n, n≈0.6; Table 53.2 gives device-specific n. Action: When a supplier prices per-tonne linearly with capacity, apply the 0.6 exponent to test realism; use it to choose between one large vs two small dryers. → 卫材相关性★★★★★｜Avoids overpaying for scale; supports right-sizing fluff/nonwoven lines.

Action Card H53-4 — Quantify the stainless premium explicitly. Insight: p.1249 — 304-SS costs 1.5–1.7× carbon steel; titanium 2–3×. Action: In specs, separate "carbon-steel-equivalent" base price from the material upcharge so the corrosion/residue justification is visible. → 卫材相关性★★★★★｜Hygiene lines need stainless/clad; makes the premium a negotiable, justified line item.

Action Card H53-5 — Require the fixed+variable unit-cost decomposition ($/t dry product). Insight: p.1257 — example totals $41.09/t fixed + $47.78/t variable = $0.089/kg. Action: Mandate that each bid report annual fixed cost, annual variable cost, and unit cost per tonne of dry product, so offers are comparable regardless of dryer type. → 卫材相关性★★★★★｜Single normalised metric to rank fluff-pulp / nonwoven dryer options.

Action Card H53-6 — Separate the energy line to link with Ch46 savings. Insight: p.1256 — fuel $1,004,400 + electricity $86,184 dominate variable cost; energy price volatile (Eq 53.6). Action: In the variable-cost table, isolate fuel and electricity so Ch46 heat-recovery / exhaust-recycle savings can be dropped straight into the model. → 卫材相关性★★★★★｜Directly quantifies payback of energy-saving retrofits in $/t.

Action Card H53-7 — Apply the labor rule to compare batch vs continuous. Insight: p.1251 — batch: 2 man-h/m³ + 1/3 man/dryer/shift; continuous automatic: 1/2 man/dryer/shift. Action: Use the rule to estimate labor cost difference between batch and continuous drying of the same hygiene product. → 卫材相关性★★★★☆｜Labor is a real variable-cost differentiator for sizing/automation decisions.

Action Card H53-8 — Use contingencies and owner costs to set a bid tolerance. Insight: p.1251 — contractor fee 10–27%, contingencies 10–30%, owner costs 5–15% of direct cost. Action: Build a +30% pessimistic band on any preliminary FCI (per p.1257 reliability) before committing capital. → 卫材相关性★★★★☆｜Sets realistic capital envelope and guards against surprise overruns.

## 12. Book-Map Quotes (Top representative quotes)

"A dryer itself is only one component of the overall drying system." — p.1247 — the system-costing principle every buyer must honour.
"To roughly estimate the total direct cost of the drying installation, it is recommended to multiply the equipment FOB cost by a factor of 2.25 if the equipment is made of carbon steel or by 2.75 if stainless-steel equipment is used." — p.1250 — the one-line FOB→system rule.
"the expected unit cost of drying of the laundry detergent in the year 2006 will most likely be US$41.09/t + US$47.78/t = US$88.87/t = US$0.089/kg." — p.1257 — the all-in unit-cost deliverable.


---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_41f64025ee90e586bab8b754ff9cad22001a693ee6c0644e"
source_file: "ID · analysis_ch27.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch27.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch27.md.md

# Chapter 27 — Drying of Potato, Sweet Potato, and Other Roots

## 1. Chapter Overview (范围、对象与定位)

Chapter 27 (Sablani & Mujumdar) is a product-specific drying review for starchy/root/bulb food commodities — potato (Solanum tuberosum), sweet potato, mushrooms, peanuts, and ginseng — within the handbook's food/biological applications block (Part IV). Its logic is the quality-vs-rate trade-off under a two-sided temperature window: too hot destroys structure, colour, and heat-labile actives; too cold prolongs residence, accelerating enzymatic browning, microbial growth, and internal degradation. The body compiles (a) preprocessing (peeling, blanching, sulfiting, osmotic pretreatment), (b) tabulated physical/thermal/thermodynamic properties (moisture diffusivity, activation energy, BET/GAB monolayer, conductivity, specific heat, thermal diffusivity — Tables 27.3–27.12), (c) drying methods per product form (diced, strips, flakes, starch, granules, chips; conventional/osmotic/vacuum/freeze/heat-pump/microwave/IR), and (d) quality outcomes (optical, physical, nutritional). For the hygiene reader this is a ★★☆☆☆ chapter: the substrate is a starch-filled cellular food, fundamentally unlike fluff/SAP polymeric webs, so no diaper application is invented below; but the transferable science — quality-vs-rate coupling, bed-depth → internal-ΔT → time interaction, staged/sinusoidal temperature profiles to suppress colour and active-compound loss, and osmotic dehydration used as a load-reducing pretreatment — maps onto absorbent-core and pulp-drying thinking.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.645–p.662 (PDF p.666–683).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — Peeling governs finished-yield and waste. Peeling is not cosmetic; it dominates economics and disposal.
> "Peeling is one of the most important steps in potato processing. The yield of finished product depends on effectiveness, efficiency, and method of peeling... Because the peeling process generates more waste than all of the other potato-processing operations combined, it is important when designing and selecting peeling systems to give proper consideration [3]." (p.646)
Interpretation: Yield and waste are set at preprocessing — a generic lesson for any fibrous feedstock (fluff-pulp) where the front-end cut/defiber step defines usable throughput.

V2.2 — Blanching is an enzymatic-stability pretreatment. Heat pretreatment inactivates enzymes that would otherwise destroy colour and flavour in storage.
> "Blanching destroys or inactivates enzymes; otherwise, potatoes may darken during dehydration and develop off-flavors and off-odors during storage." (p.648)
Interpretation: The chapter frames pretreatment as the primary lever for storage-stable quality — analogous to how stabilizer/additive pre-treatment protects hygiene-web properties before the thermal load.

V2.3 — Sulfiting protects from nonenzymatic browning during dehydration. A chemical additive is applied immediately after blanching.
> "The potatoes are sulfided immediately after blanching using sodium sulfite, sodium bisulfite, sodium metabisulfite, or combinations. Sulfite protects the product from nonenzymatic browning or scorching during dehydration and increases the storage life of the product under adverse temperature conditions." (p.648)
Interpretation: A chemical-protectant step decoupling "can survive the dryer temperature" from "retains colour on shelf" — the same decoupling problem hygiene coatings face.

V2.4 — Two-stage diced-potato dryer uses staged air temperatures; storage demands very low final moisture. Temperature is stepped down within the dryer, and long-term storage requires sorption drying to 3–4% wb.
> "The temperature of the drying air in the first section of the first stage is in the range 93–127°C, in the second section of first stage 71–105°C, and in the second stage 55–82°C." (p.650)
> "A further extension of the storage time will require reduction of moisture content to 3–4% (wb), which can be achieved by long-time sorption drying using sorption agents such as calcium oxide." (p.650)
Interpretation: Staged cooling inside one dryer + a final ultra-low-moisture sorption polish — a temperature-programming pattern relevant to any heat-sensitive fibrous web.

V2.5 — Moisture diffusivity is modelled as a function of both moisture content and temperature. Explicit parametric forms are compiled (Table 27.4).
> "D(m,T) = a₀ exp( a₁(1/m − 1/m₀) − a₂(1/T − 1/T₀) )" (ref. 44; a₀ = 1.29×10⁻⁶, a₁ = 7.25×10⁻², a₂ = 2044; valid 0.03 "D(m,T) = a₀ exp(a₁ m) exp(−a₂(T−T₃))" (ref. 46; a₀ = 168, a₁ = 15.4, a₂ = 30; valid 0.3 "D(m,T,L) = a₀ + a₁ m + a₂ T + a₃ L" (ref. 18; a₀ = −7.015×10⁻¹¹, a₁ = −2.11×10⁻¹⁰, a₂ = 2.57×10⁻¹¹, a₃ = 7.96×10⁻¹¹; L = slab thickness mm) (p.649)
Interpretation: Diffusivity rises with temperature and (in most forms) falls with moisture — the same falling-rate internal-diffusion physics that governs fluff/SAP-core drying, transferable as a modelling idiom even though the numerical constants are food-specific.

V2.6 — Osmotic dehydration is used as a load-reducing pretreatment before conventional drying. This is the bridge concept to Ch.28.
> "Osmotic preconcentration followed by fluidized bed drying of potato pieces to produce dehydrated quick-cooking potato was studied by Ravindra and Chattopadhyay [12]. They found that a solution of 50% sugar and 10% salt at 47°C for 4 h was optimum for osmotic preconcentration. The moisture content of potato cubes was reduced from 84 to 60% (wb)." (p.654)
Interpretation: Osmotic pull-out of water before the thermal dryer cuts the dryer load. The mechanism family (water-out/solute-in across a semipermeable boundary) is the same physics as Ch.28; here it is only a pretreatment note, not a polymer-science treatment.

V2.7 — Time-varying (square-wave) temperature profiles cut colour change by ~87%. Active quality control via the temperature program, not just the setpoint.
> "The use of time-varying air temperature profiles (sinusoidal and square wave) during drying of potato pieces in a two-stage heat pump has shown to reduce color change. Choy and coworkers [13] observed that the overall color change in potato was minimum when subjected to a higher varying dry temperature (square waveform 35°C, amplitude 5°C, peak to valley 10°C, cycle time 60 min, drying time about 300 min). The percentage reduction in overall color change for potato was about 87%." (p.655)
Interpretation: A sinusoidal/square temperature waveform suppresses a degradation pathway far better than a fixed setpoint — a control-strategy lesson transferable to any heat-colour-sensitive web.

V2.8 — Low-temperature drying gives greater shrinkage than high-temperature drying. Counter-intuitive: slower (cooler) drying shrinks more.
> "The degree of shrinkage at a low drying temperature (40°C) was greater than at high temperature (70°C)." (p.656)
Interpretation: Shrinkage tracks residence time and internal moisture-gradient history, not simply peak temperature — relevant wherever dimensional stability of a dried sheet matters.

V2.9 — Active-compound loss is steeply temperature-sensitive (ginseng ginsenosides). A model of the two-sided window for a heat-labile active.
> "The initial moisture content of ginseng is about 70–80% wet basis. The optimal final moisture content for storage is about 12–13% wet basis [37]... Typically the roots are dried in conventional dryers using air temperatures of 32 to 38°C." (p.660)
> "The ginsenoside content may be reduced by over 25% by drying the root using 44°C air instead of 38°C. Internal color also darkens with increase in drying air temperature." (p.660)
Interpretation: A 6°C overshoot destroys >25% of the active — the canonical argument for tight low-temperature control of heat-labile actives, directly transferable to active-ingredient-loaded wipe substrates.

V2.10 — Microwave is evaluated only for the finish-drying stage of heat-sensitive product. Energy mode matched to the drying period.
> "Microwave drying has been evaluated for final stages of drying (between 30 and 6%) of different potato products. For example, raw potato slices of 0.21 mm thick can be dried to 2–3% final moisture content within about 4 min in a microwave field." (p.655)
Interpretation: Volumetric heating is reserved for the bound-moisture tail where surface flux would otherwise overheat — a period-aware energy-choice pattern.

## 3. Research Method (研究方法)

The chapter is a data-compilation + literature-review article (Sablani/Mujumdar's style), not an original study. Method:
- Preprocessing survey (§27.2): peeling (heat/chemical/abrasive), blanching (steam/hot-water 93–100°C), sulfiting — each characterised by its effect on yield, enzyme inactivation, and downstream dehydration/reconstitution.
- Property-tabulation (§27.3, Tables 27.3–27.12): moisture diffusivity + activation energy, BET/GAB monolayer, sorption isotherm/net heat of sorption, thermal conductivity, specific heat, freezing point, thermal diffusivity — compiled from primary food-engineering literature for product-development and process-design use.
- Method-per-product catalogue (§27.4): diced/strips/flakes/starch/granules/chips under conventional, osmotic, vacuum/freeze/heat-pump, microwave/IR dryers, with operating conditions quoted from cited plant/pilot studies.
- Quality assessment (§27.5): optical (colour), physical (structure/density/porosity/shrinkage/rehydration), nutritional (Table 27.12 compositional retention) — mostly laboratory-scale results.

No new hygiene data; value is the empirical property tables, the parametric diffusivity forms, and the staged/oscillatory-temperature quality evidence.

## 4. Argumentation (论证逻辑)

- Premise A: Potato/roots are heat- and mechanically-sensitive; thermal degradation destroys colour, structure, nutrients (p.655).
- Premise B: Enzymes and nonenzymatic browning threaten storage stability unless knocked out pre-drying (blanching, sulfiting, p.648).
- Step: Therefore pre-treat to lock colour/structure, then dry under a temperature program that balances rate against active/colour loss — staged cooling (p.650), or oscillatory profiles (87% colour saving, p.655), or low-T conventional for actives (ginseng 32–38°C, p.660).
- Resolution: Match the dryer and its temperature profile to the product's weakest quality attribute; reserve high-intensity modes (microwave, IR) for the finish/bound-moisture tail. The chapter is candid that most methods beyond convective drying "are still under investigation" and that microwave needs "further industrial development to make it cost-effective" (p.655, p.661).
The argument is empirical and cautionary — appropriate for a food-safety-bound substrate, and a useful contrast to the more design-procedural engineering chapters.
## 5. Role of This Chapter in the Book (在全书中的角色)

Ch.27 is a Part IV product/application chapter sitting beside Ch.26 (herbal/tea) and Ch.28 (osmotic dehydration). It complements the dryer-specific chapters (Ch.14 inert-bed, Ch.15 impingement, Ch.17 conveyor, Ch.18 IR) by showing how those dryers are actually deployed on a real, messy, quality-sensitive food substrate, and it supplies the handbook's most complete tabulated property dataset (Tables 27.3–27.12) for a biological material. For the hygiene engineer its role is as a transferable-methods casebook: the quality-vs-rate window, bed-depth/time coupling, staged and oscillatory temperature programming, and osmotic pretreatment are demonstrated on potato and can be borrowed conceptually. Substrate-difference limit: potato is a starch-filled, enzyme-active, cellular tissue; fluff pulp is refined cellulose fibre and the SAP core is a crosslinked polyelectrolyte gel. The numerical property tables and the food-specific degradation chemistry do not transfer — only the engineering patterns (control of rate vs quality, pretreatment decoupling, staged thermal programs) do. No diaper application is asserted.

## 6. Strengths and Weaknesses (贡献与局限)

Strengths
- Exceptionally dense empirical property tables (moisture diffusivity, activation energy, BET/GAB monolayer, conductivity, specific heat, thermal diffusivity) for a biological substrate — a ready reference block.
- Makes the quality-vs-rate trade-off concrete: 87% colour reduction via square-wave T (p.655); >25% ginsenoside loss from a 6°C overshoot (p.660).
- Demonstrates period-aware energy choice (microwave finish only; IR; staged cooling).
- Treats preprocessing (peeling/blanching/sulfiting/osmotic) as first-order to final quality — a lesson often neglected in dryer-centric chapters.

Weaknesses
- Food-substrate specific: starch gelatinization (45°C, p.653), enzymatic browning, ginsenosides — none map onto fluff/SAP chemistry.
- Property constants (D(m,T), monolayer M₀) are potato/sweet-potato values; reuse on hygiene webs is invalid without re-measurement.
- Quality data "is based on the experiments carried out at the laboratory scale" (p.655) — scale-up gap acknowledged but not closed.
- Osmotic dehydration is only a one-paragraph pretreatment note here (p.654); the genuine physics treatment is deferred to Ch.28.

## 7. Key Terms (关键术语)

|||
|---|---|
|Peeling|first preprocessing step; sets yield and waste (p.646)|
|Blanching|93–100°C steam/hot-water heat treatment inactivating enzymes (p.648)|
|Sulfiting|sodium sulfite/bisulfite post-blanching protectant vs nonenzymatic browning (p.648)|
|Moisture diffusivity D(m,T)|effective diffusion coefficient as function of moisture m and T (Table 27.4)|
|Activation energy Eₐ|40–52 kJ/mol range for potato air-drying (Table 27.3)|
|BET / GAB monolayer M₀|monolayer moisture (≈0.03–0.06 kg/kg db) governing shelf-stable storage (Table 27.5)|
|Osmotic dehydration|water-out/solute-in pretreatment in concentrated sugar/salt solution (p.654)|
|Square-wave temperature profile|oscillatory dryer-air T suppressing colour change ~87% (p.655)|
|Shrinkage|greater at low T (40°C) than high T (70°C) (p.656)|
|Add-back (solid-back mixing)|granule process mixing cooked mash with prior dried granules (Fig. 27.3)|

## 8. Micro close-reading (微观精读)

8.1 — The storage-moisture floor needs a sorption polish (p.650). "A further extension of the storage time will require reduction of moisture content to 3–4% (wb), which can be achieved by long-time sorption drying using sorption agents such as calcium oxide." The two-stage convective dryer only gets to 6–7% wb; the final 3–4% demands a different physics (sorption onto a desiccant). This is the same logic as a final low-RH conditioning zone for a moisture-sensitive hygiene core — the convective dryer is not the whole moisture story.

8.2 — Diffusivity falls with moisture in the parametric forms (p.649). "D(m,T) = a₀ exp( a₁(1/m − 1/m₀) − a₂(1/T − 1/T₀) )" with a₁ = 7.25×10⁻² > 0 means D decreases as m decreases (1/m grows). This is the formal statement of the falling-rate period: as the web dries, internal diffusion throttles. For any fibrous/polymeric web the analogous statement holds qualitatively even if constants differ.

8.3 — Square-wave temperature suppresses colour (p.655). "square waveform 35°C, amplitude 5°C, peak to valley 10°C, cycle time 60 min, drying time about 300 min... The percentage reduction in overall color change for potato was about 87%." A controlled oscillation — not a fixed setpoint — dramatically slows a degradation pathway. The mechanism (periodic relief of the local thermal dose) is a generic quality-control idea independent of substrate.

8.4 — Shrinkage is a residence-time effect (p.656). "The degree of shrinkage at a low drying temperature (40°C) was greater than at high temperature (70°C). The surface structure of potato slab is damaged in 1 h drying, whereas the inner structure is apparently intact." Lower T ⇒ longer residence ⇒ more cumulative collapse. Dimensional stability is governed by the time-integral of the stress state, not peak T alone.

8.5 — Ginseng active loss is a steep temperature function (p.660). "The ginsenoside content may be reduced by over 25% by drying the root using 44°C air instead of 38°C." Six degrees nearly a quarter of the active gone. This is the quantitative backbone of the "two-sided temperature window" argument and the strongest single transferable data point for active-loaded substrates.

## 9. Concept deep-dive (概念深掘)

9.1 Moisture-diffusivity parametric models (Table 27.4, p.649). Three compiled forms: (i) ref.44 exponential in (1/m − 1/m₀) and (1/T − 1/T₀) — captures both moisture and temperature dependence, valid 0.03, 333 K; (ii) ref.46 product-exponential in m and T; (iii) ref.18 linear in m, T, and slab thickness L. Activation energies cluster 40–52 kJ/mol for potato air-drying (Table 27.3), with freeze-drying and IR at the low end. These are the modelling vocabulary for any internal-diffusion-limited drying.

9.2 BET/GAB monolayer (Table 27.5, p.649–650). Monolayer moisture M₀ for potato ranges ≈0.029–0.083 kg/kg db depending on T and variety; GAB parameters (M₀, C/K, A/D) tabulated for potato, starch, dice, slices, vacuum/freeze-dried forms. The monolayer is the quality-stable storage threshold — directly analogous to the equilibrium-moisture / RH-stability concept for a hygiene core.

9.3 Osmotic dehydration as pretreatment (§27.4.2, p.654). 50% sugar + 10% salt at 47°C for 4 h pulls potato cubes from 84→60% wb before fluidized-bed + thin-layer drying to 5% wb. The osmotic step removes ~30% of total water without thermal input, cutting dryer load and (per Ch.28) improving final colour. Here it is a one-paragraph note; Ch.28 develops the mass-transfer science.

9.4 Shrinkage & porosity dynamics (§27.5.2, p.656). Light-microscopy shows surface-first shrinkage migrating inward; cell walls elongate; cracks form in inner structure as it finally dries and internal stress pulls tissue apart. McMinn & Magee (p.656): internal porosity first decreases then rises to ~10%; volume shrinkage is linear with moisture; low-T drying shrinks more; rehydration coefficient rises ~4% as T goes 30→60°C. Density at fixed moisture falls with rising T.

9.5 Nutritional retention (Table 27.12, p.656–657). Processing Russet burbank potato: thiamine collapses to 5% (raw→granule), ascorbic acid to 29–31%, riboflavin to 21–43%; starch and protein largely retained. Demonstrates that water-soluble heat-labile micronutrients are the vulnerable class — the same vulnerability class as active ingredients in functional wipes.

9.6 Microwave/IR placement (§27.4.4, p.655). Microwave effective for finish (30→6%) and for thin slices (0.21 mm → 2–3% in ~4 min); combined air+microwave overcomes thickness-cooking; FIR drying is falling-rate with rate set by radiation intensity (0.125–0.500 W/cm²) and lower activation energy for moisture desorption. Microwave–vacuum gives reduced colour change vs air (Krokida et al., p.677).

## 10. Critique (批判性评估)

- Food-specific constants. Every D(m,T), M₀, conductivity and activation-energy number is for potato/sweet-potato/mushroom/peanut/ginseng. Direct reuse on fluff or SAP cores would be invalid; only the functional forms transfer.
- Laboratory-scale quality data. The chapter admits most quality results are lab-scale (p.655); industrial translation of the 87% colour-saving square-wave result is unproven at tonnage.
- Osmotic dehydration under-developed here. Only a pretreatment paragraph (p.654); readers needing the mass-transfer mechanism must go to Ch.28.
- No falling-rate model beyond diffusivity tables. The parametric D(m,T) is given, but no full drying-curve or shrinkage-consolidation model is solved; engineers still need experimentally determined curves (cf. Ch.15's caveat).
- Starch-gelatinization caveat buried. Moist starch granules swell at 45°C and must be kept °C during drying (p.653) — a substrate-specific constraint with no analogue in polymeric hygiene webs.
- OCR noise. Source concatenates words ("approximately"→"abouter"/"cester") and drops some subscripts in equations; re-verify D(m,T) constants against print.
## 11. Hygiene-Material Relevance & Action Cards (卫材相关性与行动卡)

Rating for this chapter: ★★☆☆☆ — substrate is food starch/cellular tissue; numeric data do not transfer. The engineering patterns below are the genuinely reusable part. No diaper application is invented; statements are limited to transferable method.

H11.1 — Borrow the two-sided temperature window for active-loaded webs (★★★). Action: Where a wipe carries a heat-labile active, treat ginseng's 6°C-overshoot → >25% loss (p.660) as the quantitative precedent: set the dryer's temperature band from the active's degradation onset, not from generic throughput, and validate with a stability assay.

H11.2 — Use staged cooling inside one dryer (★★★). Action: Mirror the diced-potato two-stage profile (93–127°C → 71–105°C → 55–82°C, p.650) when a hygiene web needs a high-flux surface phase followed by a gentle bound-moisture tail; add a final low-RH/desiccant conditioning zone to reach the true storage moisture floor (cf. 3–4% wb sorption polish, p.650).

H11.3 — Try oscillatory temperature to protect colour/actives (★★★). Action: The square-wave T that cut potato colour change ~87% (p.655) is a control-strategy idea: test a sinusoidal/square air-temperature program on colour- or active-sensitive webs before assuming a fixed setpoint is optimal.

H11.4 — Treat preprocessing as a first-order quality lever (★★). Action: As blanching/sulfiting lock potato colour before the thermal load (p.648), pre-stabilize hygiene-web additives (antioxidants, buffers) upstream of the dryer rather than compensating with lower dryer temperature and longer residence.

H11.5 — Recognise shrinkage as a residence-time effect (★★). Action: Low-T/long-residence drying shrank potato more than high-T (p.656); for dimensionally-critical nonwoven/airlaid sheets, prefer a higher-temperature shorter-residence profile if the active allows, to limit collapse.

H11.6 — Use osmotic pull-out as a load concept (link to Ch.28) (★★). Action: The potato result (84→60% wb water removed osmotically before thermal drying, p.654) previews Ch.28's water-out/solute-in physics; consider an osmotic/dewatering pre-step to cut thermal-dryer load where a semipermeable boundary is available — full mechanism in Ch.28.

## 12. Book-Map Quotes (本书脉络引证)

- Ch.4 (p.81): effective diffusivity / Fick — the internal-diffusion framework behind the D(m,T) tables here (p.649) and the falling-rate period invoked throughout.
- Ch.15 (p.383): impingement/conveyor high-flux drying — the dryer family that would execute the "high-temperature short-residence" tail recommended in H11.5.
- Ch.26 (p.633): herbal/tea drying — sibling quality-vs-rate food chapter; same two-sided-window logic, different substrate.
- Ch.28 (p.663): osmotic dehydration of fruits/vegetables — the genuine physics treatment of the pretreatment noted here at p.654; read Ch.28 for the mass-transfer mechanism and the SAP/osmotic-pressure link.

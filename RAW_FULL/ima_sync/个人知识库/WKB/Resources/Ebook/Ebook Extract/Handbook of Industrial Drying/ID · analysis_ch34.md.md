---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_e91b3bd5d4b918a3e26d8b138a0ba841001a693ee6c0644e"
source_file: "ID · analysis_ch34.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch34.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch34.md.md

# Chapter 34 — Drying of Textile Products

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 34 (Carr, Lee & Ok) surveys drying across the textile industry and is directly adjacent to nonwoven-web drying for the hygiene reader: the authors explicitly define "textile" to include nonwoven fabrics (p.779). The chapter classifies drying into predrying (mechanical or thermal, to ~30% moisture regain) and final thermal drying, then catalogs mechanical dewatering (squeeze, vacuum, centrifuge) and thermal dryers (conduction/steam-can, convection circulating-air, through-air, impingement, IR, RF/microwave). Its distinctive assets are quantitative benchmarks: energy per kg water by method (squeeze 58 → vacuum 700 → steam-can 4700 → convection 7000 kJ/kg, Table 34.1), fibre physical/thermal properties (Table 34.2), and an extensive moisture-regain absorption/desorption table (Table 34.3) showing large hygroscopic hysteresis for hydrophilic fibres. The recurring engineering lesson is "remove as much water mechanically as possible" because mechanical dewatering is far cheaper than thermal.

## 2. Key Viewpoints (with verbatim quotes + print pages)

### Viewpoint 1 — "Textile" includes nonwovens; drying is the energy bottleneck

- Page: p.779
- Quote: "textile is defined as any product made from fibers. Thus textiles refer not only to woven fabrics but also to nonwoven fabrics, knitted fabrics, tufted fabrics … Approximately 25% of the energy used in wet processing is consumed in drying."
- Interpretation: The chapter is squarely applicable to hygiene nonwovens. Drying consumes a quarter of wet-processing energy, so it is both a cost and a throughput bottleneck the substrate supplier must manage.
### Viewpoint 2 — Mechanical dewatering is far cheaper than thermal

- Page: p.779
- Quote: "Mechanical dewatering is generally much less expensive than thermal drying. Thus, as much water as possible is usually removed mechanically."
- Interpretation: The energy ladder (Table 34.1) quantifies this: squeezing at 58 kJ/kg vs convection at 7000 kJ/kg is ~120× cheaper per kg water. For wipe/nonwoven lines, maximizing wet-pickup reduction before the dryer is the dominant cost lever.
### Viewpoint 3 — Predry to ~30% regain; final drying fixes dimensions via heat-setting

- Page: p.781
- Quote: "fabrics that are heat set in the drying process will be predried by some means to a moisture regain of approximately 30%. They will be transported through a convection oven using a tenter frame that fixes the width of the fabric, giving it dimensional stability."
- Interpretation: The tenter frame + convection oven combination both dries and sets the web — a crystallisation/heat-setting operation whose temperature window is set by the fibre's Tm/Tg. This is the dimensional-stability control relevant to nonwoven substrates.
### Viewpoint 4 — Hydrophilicity dictates how low mechanical dewatering can go

- Page: p.782
- Quote: "the reduction in moisture regain obtainable with squeezing rollers varies with both the fiber type and the textile construction. For structures composed of hydrophilic fibers such as cotton, the moisture regain can typically be reduced from about 150% to 60–100%. On the other hand, for structures composed of hydrophobic fibers such as polyester, significantly lower moisture regain can be obtained."
- Interpretation: Hydrophobic synthetic webs (PET/PP) shed water to a far lower regain than cellulosic ones — directly relevant when choosing a wipe substrate and predicting residual moisture and SAP partitioning.
### Viewpoint 5 — Through-air drying needs permeability; low-perm webs switch to impingement

- Page: p.786
- Quote: "As the air permeability of the material increases, the airflow rate increases resulting in a higher drying rate. In this case, through-air drying is a good option; however, if air permeability of the material is too low, the electrical energy for driving the fan … would be too high. In this case, impingement drying is often used instead of through-air drying."
- Interpretation: The dryer choice is gated by substrate air permeability — a direct design rule for through-drying spunlace/airlaid hygiene webs versus impinging on latex-backed or low-perm structures.
### Viewpoint 6 — IR is for predrying only (scorch risk); RF gives uniform, low-overdry drying

- Page: p.788
- Quote: "IR ovens are typically used to predry materials that are finally dried in tenter-frame convection ovens. … IR drying is not normally used to accomplish final drying because IR energy is absorbed by dry textiles and there is a danger of scorching or burning the product."
- Interpretation: IR's surface absorption makes it unsafe for final drying of thin webs — a quality caveat for coating/laminating hygiene substrates. RF/microwave, conversely, heat volumetrically and "usually have the advantage of providing a more uniform final drying and reduced chance of overdrying" (p.788–789).
## 3. Research Method & Data Sources

Review/reference compilation; data drawn from DOE reports, fiber-science texts and journal tables.

||||||
|---|---|---|---|
|Energy benchmarking|Tabulated kJ/kg H₂O by method|Georgia Tech DOE Report ORO-5099-T1 (1978); Badin & Lowitt (1988)|Table 34.1|Representative industrial figures|
|Fibre property catalogue|Tabulated density, Cp, k, α|Warner, Fiber Science (1995)|Table 34.2|Standard fibre data|
|Sorption|Absorption/desorption regain vs RH|Fuzek, Ind. Eng. Chem. (1985)|Table 34.3, Fig 34.3|Experimental, 21°C|
|Dewatering yield|Regain after squeeze/vacuum/centrifuge|Ostervold (1982); Morton & Hearle (1993)|Tables 34.5–34.6|Empirical, fibre-dependent|
|Dielectric heating|Dipolar/ionic conduction theory|Orfeuil (1987); Clark et al. (1997)|RF/microwave description|Established physics|

## 4. Argumentation Process

- Define scope — "textile = any product from fibers," including nonwovens (p.779); drying = dewatering; ~25% of wet-process energy.
- Classify — predrying vs final drying; mechanical vs thermal (p.780–781).
- Quantify the energy ladder — Table 34.1 shows mechanical ≪ thermal (p.781).
- Fibre properties & sorption — Tables 34.2–34.3 + hysteresis figure motivate why hydrophilic fibres resist mechanical dewatering (p.782–783).
- Mechanical dewatering — squeeze, vacuum, centrifuge with achievable regains (p.783–785).
- Thermal dryers — conduction (steam cans, ~4700 kJ/kg), convection (circulating/through-air/impingement), IR, RF/microwave, each with strengths/limits (p.785–789).
- Conclusion — many products/many dryers; no design detail attempted (p.789).
## 5. Role in the Book

Ch34 is the "engineered fibrous web" companion to Ch33 (natural fibres/pulp) and Ch35 (paper/pulp webs). It generalizes the conduction/through-air/impingement vocabulary to fabrics and explicitly embraces nonwovens, making it the closest sibling to hygiene nonwoven processing. It feeds the same heat-transfer toolkit used in Ch35 and shares the sorption/hysteresis physics of Ch33.

## 6. Strengths & Weaknesses

✅ Strengths: Excellent quantitative benchmarking (energy ladder, regain tables) that a process or procurement engineer can use directly; explicit inclusion of nonwovens; clear permeability-gate rule for through-air vs impingement; honest scorch caveat for IR and uniformity caveat for microwave.
⚠️ Limitations/contestable: A 2006-vintage review; "no attempt is made to give full design details" (p.789) — purely descriptive, no modeling equations for textile drying kinetics. Moisture-regain tables are at 21°C only; no treatment of SAP, superabsorbents, or hot-air impingement correlations (deferred to other chapters). IR emissivity/wavelength discussion is qualitative.

## 7. Key Terms / Concepts

- Moisture regain (%): p.780, "weight of water in the textile to the dry weight of the textile" — the chapter's master moisture metric (NOT dry-basis fraction).
- Predrying: p.781, lowering regain "to some predetermined level" (e.g., ~30%) before final drying.
- Mechanical dewatering ceiling: p.782, squeezing reduces hydrophilic cotton from ~150% to 60–100% regain; hydrophobic polyester reaches far lower.
- Steam-can (conduction) drying: p.785–786, ~4700 kJ/kg; direct contact risk of surface distortion and dye/adhesive transfer.
- Through-air drying: p.786, "forcing the air to flow through the porous material"; high contact area → high rate; needs air permeability.
- Tenter frame: p.781, fixes transverse dimension "giving it dimensional stability" during heat-set final drying.
- Dielectric heating: p.788, RF/microwave heating by ionic conduction + dipolar rotation of molecules in an alternating field.
- Hygroscopic hysteresis: p.783, "large for hydrophilic fibers, such as cotton, and low for hydrophobic fibers, such as polyester."
## 8. Micro close-reading (ONE key paragraph)

p.781–782 (Mechanical dewatering ceiling, hydrophilic vs hydrophobic):
> "The moisture regain achievable with mechanical methods depends significantly on the type of process used and on the type of textile being dried. For structures composed of hydrophilic fibers such as cotton, the moisture regain can typically be reduced from about 150% to 60–100%. On the other hand, for structures composed of hydrophobic fibers such as polyester, significantly lower moisture regain can be obtained."

Sentence-by-sentence: (1) Scope claim — mechanical-dewatering floor is fibre- and process-dependent. (2) Hydrophilic case — cotton starts at ~150% regain (very wet after dyeing/finishing) and squeezes down only to 60–100%; bound water resists mechanical removal. (3) Hydrophobic contrast — polyester sheds to a much lower regain because it holds little bound water.
💡 Standout line: the hydrophilic/hydrophobic split is the single most decision-relevant fact for a wipe-substrate buyer sizing wet-pickup reduction and SAP partitioning.

## 9. Concept deep-dive

The energy ladder (procurement cost lever). Table 34.1 (p.781): squeeze roll 58, vacuum extractor 700, steam can 4700, convection dryer 7000, radiant predryer 9300 kJ/kg H₂O. The ~120× gap between squeeze and convection is the quantitative backbone of "remove as much water mechanically as possible." For a hygiene converting line this translates to: invest in nip pressure / vacuum extraction ahead of any thermal dryer.

Moisture regain & hysteresis (SAP partitioning proxy). Table 34.3 (p.782) gives absorption/desorption regain vs RH at 21°C for cellulose acetate, cotton, Kevlar, Nomex, nylon 66, PET, silk, viscose rayon, wool. At 65% RH: cotton ~7.9/9.7%, viscose rayon ~14.4/16.1%, PET ~0.43/0.47%, wool ~13.6/17.7%. Hysteresis is "large for hydrophilic fibers … low for hydrophobic fibers" (p.783). This is the quantitative basis for predicting in-package MC drift and fibre-vs-SAP water partitioning under storage RH — the same equilibrium-MC logic Ch33 applies to pulp.

Permeability gate (through-air vs impingement). p.786: higher air permeability → higher through-air rate; if permeability too low, fan energy makes through-air uneconomic and impingement is preferred. Suction/perforated-drum through-air dryers are "often used to dry fabrics, particularly nonwovens" (p.786). This is a direct spec rule for nonwoven hygiene webs: measure air permeability to choose the dryer and to predict rate.

Heat-setting = crystallisation/dimensional fix (PoP link). The tenter-frame convection oven "fixes the width … giving it dimensional stability" (p.781). This is heat-setting: heating the web above the amorphous-phase relaxation temperature so molecular chains rearrange and, on cooling, lock in a set dimension — the polymer-physics anchor for substrate dimensional stability (see POP crossref).

## 10. Academic critique & open questions

- Descriptive only; no drying-rate model, no equations for textile-web kinetics (unlike Ch33/Ch35 which give Fick/conduction formulations). Limits quantitative reuse.
- Regain data at a single temperature (21°C); no temperature-dependent isotherms, so high-temperature dryer behaviour must be inferred.
- RF/microwave uniformity problem noted but "recent research" (waveguide serpentine) is dated (2006); current state should be re-verified.
- Open question 1: Can the hydrophilic/hydrophobic mechanical-dewatering floor (Table 34.5–34.6) be used to predict achievable wet-pickup reduction for a blended spunlace (PET + viscose + binder)?
- Open question 2: How does the heat-set temperature window of a PP/PET nonwoven substrate (set by Tm/Tg) interact with through-air drying temperature to fix or degrade dimensional stability?

## 11. Hygiene-material relevance & action cards

Overall relevance: ★★★★☆ (strong; adjacent to nonwoven web drying).

Action Card H34-1 — Specify substrate drying method & verify the permeability gate. Insight: p.786 through-air "good option" only if air permeability is adequate; low-perm → impingement. Nonwovens "particularly" use suction/perforated-drum through-air. Action: Request the substrate's air-permeability (CFM) and the dryer type; confirm a through-air web wasn't force-dried at excessive fan energy (cost/quality risk). → 卫材相关性★★★★★｜Air permeability decides dryer choice and achievable rate for your nonwoven.

Action Card H34-2 — Drive wet-pickup reduction mechanically before thermal drying. Insight: p.779 "as much water as possible is usually removed mechanically"; Table 34.1 squeeze 58 vs convection 7000 kJ/kg. Action: For wipe converting, specify nip + vacuum extraction ahead of any oven; set a residual-moisture-regain target and audit supplier dewatering. → 卫材相关性★★★★★｜120× energy gap; the dominant cost lever in substrate making.

Action Card H34-3 — Use moisture-regain tables to size SAP vs fibre water split. Insight: p.782 Table 34.3 — at 65% RH viscose rayon ~14–16% vs PET ~0.4–0.5% regain; hysteresis large for hydrophilic. Action: Pick substrate fibre mix from equilibrium regain to control in-package MC drift and SAP partitioning under storage RH. → 卫材相关性★★★★★｜Quantifies fibre water affinity that competes with SAP for fluid.

Action Card H34-4 — QC the heat-set / dimensional-stability history. Insight: p.781 tenter-frame convection oven "fixes the width … dimensional stability"; heat-set is a crystallisation step. Action: For nonwoven substrates requiring flatness/dimensions, specify heat-set temperature against the fibre Tm/Tg window and require dimensional-stability data (MD/CD shrink). → 卫材相关性★★★★☆｜Prevents curl/shrink in the final article.

Action Card H34-5 — Avoid scorch: keep IR to predrying; watch overdry. Insight: p.788 IR "not normally used to accomplish final drying because … danger of scorching or burning"; RF gives "reduced chance of overdrying." Action: If a supplier uses IR, confirm it is predry-only and that coating/laminate webs were not heat-damaged; prefer RF for bulky uniform drying. → 卫材相关性★★★★☆｜Protects substrate strength and appearance.

Action Card H34-6 — Benchmark supplier energy/cost from the energy ladder. Insight: p.781 Table 34.1 quantifies method energy; p.788 electricity 3–5× gas for IR. Action: When comparing substrate quotes, ask which dewatering/drying sequence is used; a mechanically-aggressive supplier should be cheaper and greener. → 卫材相关性★★★★☆｜Energy mix is a negotiable cost/ESG differentiator.

## 12. Book-Map Quotes (Top representative quotes)

"textile is defined as any product made from fibers. Thus textiles refer not only to woven fabrics but also to nonwoven fabrics …" — p.779 — extends the whole chapter to hygiene nonwovens.
"Mechanical dewatering is generally much less expensive than thermal drying. Thus, as much water as possible is usually removed mechanically." — p.779 — the cost thesis.
"if air permeability of the material is too low, the electrical energy for driving the fan … would be too high. In this case, impingement drying is often used instead of through-air drying." — p.786 — the permeability-gate design rule.

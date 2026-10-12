---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_6b16fc034c93d3735082469ab42209ff001a693ee6c0644e"
source_file: "ID · analysis_ch21.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch21.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch21.md.md

# Chapter 21 Analysis — Drying of Foodstuffs

Handbook of Industrial Drying, 4th ed., Mujumdar (CRC Press)
Reader: hygiene-materials R&D engineer (diapers, wipes, absorbent cores, fluff-pulp procurement)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

## 1. 章节概览 / Chapter Overview

Chapter 21 (Sokhansanj & Jayas) is a self-contained primer on food dehydration — objectives, moisture/water-activity theory, psychrometrics, a full drying-modeling derivation (heat/moisture balances, constant/falling-rate periods), physical/thermal properties, a catalog of food dryers, and a section on nutrient losses during dehydration. It is written for the agricultural/food engineer, not the fibre engineer.

For the hygiene reader the chapter is indirect but genuinely useful: its transferable frameworks are (a) the water-activity / equilibrium-moisture formalism that governs microbial stability — directly applicable to the residual-moisture spec of fluff pulp and nonwoven webs; (b) superheated-steam drying of foods (§21.7.14) which echoes Ch19 and is the cleanest book analog for "no oxidation → brightness preserved" in pulp; and (c) non-enzymatic browning / Arrhenius degradation kinetics (§21.8.5) which is the food analog of hydrothermal brightness reversion in cellulose. Per the assignment brief, Ch21 is correctly judged the weakest of the six chapters for hygiene — its value is as a transferable framework, not as a directly applicable case study.

## 2. 核心观点 / Key Viewpoints (verbatim + page + interpretation)

- VP1 (water activity → microbial stability). "Oxidation activity is only possible at water activities higher than 0.4 and the rate of inactivation of other organisms requires a water activity of 0.7 or lower. Some enzymatic activities may continue at low levels of water activities of 0.1–0.3 but their reaction rate decreases at low water activities." (print p.522).
Interpretation: The single most transferable hygiene statement in the chapter — a quantitative water-activity threshold for microbial inactivation. Directly underpins why fluff-pulp and core-wrapping residual-moisture specs exist (control a_w to suppress mold/biotic growth in storage and in the finished article).
- VP2 (moisture binding sites). "Moisture, in the form of water molecules, is bonded to various parts of the product in varying ways as follows: (a) ionic groups, such as carboxyl and amino acids and (b) hydrogen groups, such as hydroxyl and amides." (print p.521).
Interpretation: The taxonomy of bound water maps one-to-one onto cellulose (hydroxyl) and SAP (crosslinked sodium polyacrylate — carboxylate). Useful when reasoning about "free vs. bound" moisture in absorbent cores.
- VP3 (sanitation / disinfestation). "Insects and other microorganisms are destroyed during the application of heat and moisture diffusion… The temperature should be at least 60°C for a short duration of 3 to 5 min. Lower temperatures, to a minimum of 48°C, can be used for disinfestation but the treatment duration should last at least for 24 h or longer." (print p.522).
Interpretation: Gives explicit time–temperature lethality windows; a reference point if bioburden control in pulp/web is ever treated thermally.
- VP4 (GAB/EMC formalism). GAB equation: "M/M_s = C K a_w / [(1 − K a_w)(1 − K a_w + C K a_w)] where C, K, and M_s are constants." (print p.522). EMC is "the moisture content of the product at [vapor-pressure] equilibrium" (print p.521).
Interpretation: The standard model linking equilibrium moisture to water activity — the analytic backbone behind any residual-moisture specification.
- VP5 (superheated steam, no oxidation). "Superheated steam drying has been credited with the following advantages: 1. Improved drying efficiency, as much as 50% less than conventional systems; 3. No product oxidation, because there is no direct contact of hot oxygen with the product; 4. Phytosanitary; steam heat is superior to dry air in destroying all stages of insects, molds, and other microorganisms." (print p.538–539).
Interpretation: This is the strongest hygiene anchor in the chapter — SSD eliminates oxidative damage (the mechanism behind brightness reversion in pulp) and is phytosanitary, echoing Ch19's thesis for paper/tissue.
- VP6 (heat damage by dryer type). "The loss of milk lysine in spray drying ranges from 3 to 10%, whereas in drum drying the loss ranges from 5 to 40%… In drum drying, the milk particles at medium to low moistures are in contact with the hot drum, and therefore the loss of lysine is greater." (print p.540).
Interpretation: A vivid illustration that surface contact at low moisture maximizes heat damage — the same reason through-air/low-surface-temperature routes beat hot-cylinder drying for heat-sensitive webs (cf. Ch17, Ch20 Table 20.1).
- VP7 (non-enzymatic browning). "A model describing the rate of nonenzymatic browning in skim milk for the range of temperature from 35 to 130°C and 3 to 5% db moisture content… k_0 exp(−E/RT)… E = 90816.51 [J/mol]…" (print p.542–543).
Interpretation: The food analog of hydrothermal yellowing/brightness reversion; the Arrhenius machinery transfers to cellulose degradation kinetics.
- VP8 (Arrhenius degradation). "k = k_0 exp(−E/RT) where k_0 is the constant, E is the activation energy of the reaction, R is the gas constant, and T is the absolute temperature." (print p.540).
Interpretation: The universal kinetic framework for any thermally activated loss (nutrient, colour, fibre strength, brightness).
- VP9 (microwave: no surface cracking). "Since high-frequency heating evaporates water inside the material and causes convecting cooling on the surface, the outside surface remains wet until the end of the drying cycle; hence, cracking does not occur." (print p.537).
Interpretation: Volumetric (dielectric) heating avoids the surface-dry/interior-wet gradient that cracks diffusion-limited materials — directly relevant to avoiding web curl/kink and casehardening in thick hygiene structures.
- VP10 (fluidized-bed particle limits). Suitable materials: "1. The average particle size should be between 10 mm and 20 mm… 2. Narrow size distribution… 3. Regular shape… 4. A lump must disintegrate easily upon fluidization." (print p.538).
Interpretation: The particle-size/size-distribution rules that govern fluid-bed drying of granules — the same constraints that decide whether fluff/pulverized cellulose or granular SAP can be fluid-bed processed.
- VP11 (vacuum: hygroscopic, costly). "Vacuum-dried products are quite hygroscopic. Special care is needed during packing… Temperatures range between 35 and 60°C… Vacuum drying is one of the most expensive methods of drying." (print p.536–537).
Interpretation: Low-temperature vacuum drying preserves heat-labile quality but yields hygroscopic product needing sealed packing — a relevant trade-off if low-temp drying of a hygiene web is ever contemplated.
## 3. 研究方法 / Research Method

Pedagogical/derivational chapter: it derives a layer drying model from first principles (heat balance Eq 21.3, moisture balance Eq 21.9, constant-rate Eq 21.10, falling-rate diffusion Eq 21.14–21.17) and then surveys dryers and reports empirical nutrient-retention data (Tables 21.4–21.8). Method = analytical modeling + compiled experimental/ASAE-standard data; not a primary research report.

## 4. 论证逻辑 / Argumentation

Logical flow: (1) why dry food → (2) water/water-activity theory → (3) psychrometrics → (4) drying model (balances + rate periods) → (5) material properties → (6) dryer catalog → (7) quality/nutrient-loss consequences. The implicit argument: drying is a trade-off between removing water (storage/safety) and thermally degrading quality — exactly the hygiene trade-off between residual-moisture spec and fibre/brightness damage.

## 5. 章节定位 / Role in Book

A foundational/reference chapter — it supplies the moisture–water-activity and drying-rate theory that the process-specific chapters (Ch16–Ch20) assume. It is the "theory and food application" counterpart to the industrial dryers; its SSD subsection points back to Ch19 and its spray/drum/fluid-bed descriptions overlap Ch17–Ch20.

## 6. 优点与不足 / Strengths and Weaknesses

Strengths: Exceptionally clean drying-model derivation (balances + constant/falling rate) usable for any particulate/web; the water-activity and GAB framework are gold for residual-moisture specs; SSD advantages (no oxidation, phytosanitary) and the browning/lysine heat-damage cases are directly translatable.
Weaknesses (hygiene): Content is food-specific; examples (grains, milk, meat) do not map onto fluff pulp, SAP, or PP/PET webs without translation. Several equations are garbled in the OCR source (Eq 21.1 BET form and Eq 21.2 Henderson form are partly unreadable — see §9). Nutrient-retention numbers are food chemistries that differ from cellulose degradation.

## 7. 关键术语 / Key Terms

- Water activity (a_w) — ratio of product vapor pressure to saturation vapor pressure; governs microbial/enzymatic stability (print p.522).
- Equilibrium moisture content (EMC) — moisture at vapor-pressure equilibrium; modeled by GAB (print p.521–522).
- Constant-rate vs. falling-rate period — first period surface-wet (external control), second period diffusion-limited (internal control) (print p.527–528).
- Superheated steam drying (SSD) of foods — closed-loop steam with vapor recompression; no oxidation (print p.538).
- Non-enzymatic browning — Maillard-type colour formation; Arrhenius model (print p.542).
- Critical moisture content — transition point from constant to falling rate (print p.528).
## 8. 微观精读 / Micro close-reading

The water-activity sentence (VP1) is the chapter's most quotable hygiene line: the authors state a hard threshold — a_w > 0.4 enables oxidation; a_w ≤ 0.7 inactivates microorganisms; a_w 0.1–0.3 still permits slow enzymatic activity. For a fluff-pulp procurement spec, this is the scientific justification for setting a maximum residual moisture: the spec exists to keep the stored fibre and the finished article below the microbial-growth water-activity window. The GAB equation (VP4) is the tool to convert that a_w target into an engineering moisture-content number for a given RH — i.e., the residual-moisture spec is really a water-activity spec in disguise.

Equally instructive is VP6: lysine loss in drum drying (5–40%) vastly exceeds spray drying (3–10%) because at low moisture the particles sit against the hot drum surface. This is the textbook warning that low-moisture + hot surface contact = maximum thermal damage — the very reason thermo-bonded nonwovens and through-air routes avoid prolonged hot-cylinder residence.

## 9. 概念深析 / Concept Deep-Dive — From food browning to pulp brightness reversion

The chapter's degradation kinetics (§21.8) are framed for nutrients, but the machinery is universal. Eq 21.53 (Arrhenius) and the non-enzymatic-browning model (VP7) describe a first-order thermally activated loss:
- d[N]/dt = −k_0 exp(−E/RT)·N.
The same form governs brightness reversion in dried pulp: hydrothermal exposure at intermediate moisture activates chromophore formation, and the rate rises with temperature via an activation energy. The chemistry differs (Maillard condensation of reducing-sugar + amino group in milk vs. oxidative/hydrothermal yellowing of cellulose lignin residues), but the kinetic governance — activation energy, moisture dependence, low-temperature preference — is identical. Hence Ch21 gives the hygiene engineer a validated kinetic vocabulary to design brightness-stability tests.

On equations: the GAB (VP4) is clean; however the BET-type Eq 21.1 and the Henderson Eq 21.2 are [equation garbled in source] — the OCR collapsed the fraction into "M(P P )¼M Cþ M C P". They are described in words above (sigmoid EMC-vs-ERH; single/multilayer water). The enthalpy relation i = 1005·T_a + X_a·(1820·T_a + 2,501,000) (Eq 21.4) and the rate laws Eq 21.10 / Eq 21.14–21.15 transcribe cleanly.

## 10. 批判性评价 / Critique

The food focus is both the chapter's strength (rich, validated data) and its limitation for this reader. Two cautions: (1) OCR garbling in the EMC equations means the reader must consult the print edition (or ASAE/ASABE standards) before using Eq 21.1/21.2 numerically — never deploy them from this text alone. (2) The nutrient-loss Tables (21.4–21.8) are food chemistries; do not import their percentage losses onto cellulose/SAP — only the kinetic framework transfers. Otherwise the chapter is reliable and well-sourced (ASAE standards, peer-reviewed dehydration literature).

A hygiene-specific gap is that none of the food dryers are qualified by fibre property. The chapter never reports curl/kink, brightness reversion, tensile loss, or web-defect rates for any dryer — its quality metrics are nutrients, colour, and rehydration. The SSD subsection (§21.7.14) is the lone exception where "no oxidation / phytosanitary" speaks directly to brightness preservation, but even there no fibre data are given. The hygiene engineer must therefore use Ch21 for its transferable frameworks (water activity, GAB, Arrhenius, constant/falling-rate modeling) and source fibre-specific outcomes from Ch17–Ch19. Rate it honestly as the weakest chapter of the six for direct hygiene case studies.

## 11. 卫材相关性 / Hygiene Relevance & Action Cards

Rating: ★★★☆☆ (moderate — transferable framework is strong, but content is food-specific and needs translation; honestly the weakest of the six for direct case studies).

- AC1 — Residual-moisture spec as a water-activity spec. Use VP1 (print p.522: a_w ≤ 0.7 inactivates microbes; a_w > 0.4 enables oxidation) and the GAB relation (VP4) to justify and quantify fluff-pulp and core residual-moisture limits. Action: express your spec in a_w terms and convert to %wb via GAB for the local storage RH.
- AC2 — Brightness reversion via Arrhenius. Adopt the §21.8 kinetic framework (VP7/VP8, print p.540–543) to design accelerated brightness-stability tests on dried pulp, treating yellowing as a thermally activated loss with an activation energy. Action: run isothermal humidity-oven aging and fit k = k_0 exp(−E/RT) rather than ad-hoc pass/fail.
- AC3 — SSD as brightness-preserving route. §21.7.14 (print p.538–539) shows SSD gives "no product oxidation" and is phytosanitary — the same argument Ch19 made for pulp/paper. Action: when evaluating energy + brightness, keep SSD on the candidate list and cite the "no oxidation" benefit as the brightness-reversion mitigation.
- AC4 — Avoid hot-surface/low-moisture residence. VP6 (print p.540) proves drum (surface) drying damages far more than spray (rapid, evaporatively cooled) drying. Action: minimize hot-cylinder dwell at low web moisture on bonding/calendering lines; prefer through-air/low-surface-temp routes.
- AC5 — Bound vs. free moisture language. VP2 (print p.521) categorizes moisture into ionic (carboxyl/amino) vs. H-bonded (hydroxyl/amide) sites — directly analogous to cellulose OH and SAP carboxylate. Action: use this language when distinguishing "free surface water" (drives microbial growth) from "bound water" (does not) in absorbent cores.
## 12. 书图引用 / Book-Map Quotes (cross-references)

- Superheated steam: §21.7.14 is the food application of the technology given a dedicated chapter → Ch19.
- Spray / drum / fluid-bed / conveyor / belt / microwave dryers in §21.7 overlap the industrial dryers of Ch17 (conveyor), Ch18 (IR/microwave), Ch20 (novel/impinging/fluid-bed).
- Drying-rate theory (constant/falling, critical moisture) is the generic basis assumed across Ch16–Ch20.
- Water-activity/EMC framing is the storage-stability counterpart to the residual-moisture concern threaded through all fibre chapters.


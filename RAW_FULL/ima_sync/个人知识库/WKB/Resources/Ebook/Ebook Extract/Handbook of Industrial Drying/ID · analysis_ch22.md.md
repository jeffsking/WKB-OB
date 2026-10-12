---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_1e71bf0dc9676bc76281dea5473fc24b001a693ee6c0644e"
source_file: "ID · analysis_ch22.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch22.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch22.md.md

# Chapter 22 — Drying of Fish and Seafood

## 1. Chapter Overview (范围、对象与定位)

Chapter 22 (M. Shafiur Rahman) surveys the drying of fish and seafood as a food-preservation unit operation: it walks from raw-material structure (muscle fibre / extracellular space) through pretreatments (salting, cooking, smoking), dryer selection (sun, convective, vacuum, freeze), packaging under low water activity, and the full catalogue of quality changes (microflora, browning, lipid oxidation, protein denaturation, shrinkage and pore formation, rehydration, solubility, texture, nutrition). Its governing logic is that fish flesh is a high-moisture, high-protein, often high-fat biological matrix whose drying is dominated by case-hardening (pellicle formation), surface-crust barrier, and shrinkage/collapse governed by the glass-transition state. For the hygiene-materials reader this is a low–medium transfer chapter (★★–★★★): the substrate is animal muscle, not fluff pulp or SAP, and the author never mentions hygiene products. The genuinely portable mechanisms are (i) the case-hardening / surface-crust rule — a hard dried-protein skin that retards internal moisture movement — directly analogous to binder-skin / casehardening on a hot-air-dried nonwoven web; (ii) the glass-transition explanation of shrinkage and pore formation (Tg′-based collapse), which is a polymer-physics concept shared with SAP/binder webs; and (iii) the quality-vs-rate trade-off (push temperature to kill microbes vs. keep organoleptic quality). Sections 5 and 11 state plainly where substrate differences limit transfer — do not invent diaper applications for fish.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.545–p.557 (PDF p.566–578; references p.557+).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — Fish flesh is a wet, structured biological matrix that dries by surface evaporation.
> "Fish muscular tissue consists mainly of muscle fibers or cells (86–88%, v/v) and some extracellular space (interstitial space, 9–12% and capillary space, 2–3%)... Removing moisture from fish flesh is a process of surface evaporation and therefore requires heat." (p.545, p.550)
Interpretation: The chapter frames drying as a surface-evaporation problem in a structured porous matrix — the same first-order framing applies to a wet fluff/SAP/nonwoven web, even though the solid phase differs.

V2.2 — Salting is osmotic dehydration with an equilibrium end-point.
> "Salting converts fresh fish into shelf-stable products by reducing the moisture content, and acting as a preservative... The osmotic dehydration process (i.e., salting) can be characterized by equilibrium and dynamic periods... Equilibrium is the end point of osmotic process, i.e., the net rate of mass transport is zero." (p.547)
Interpretation: Osmotic dehydration (mass transport toward zero net flux) is a named mechanism; the hygiene reader will recognise it as the conceptual sibling of SAP moisture desorption/equilibrium with ambient RH (developed rigorously in Ch.24).

V2.3 — Surface crust / case-hardening severely retards drying and must be avoided.
> "Heating the surface too fast can produce a hard crust (mostly dried soluble protein), which retards movement of moisture. This phenomenon (case-hardening) can severely reduce the rate of drying and must be avoided." (p.550)
Interpretation: This is the single most transferable defect rule. On a hot-air-dried hygiene web, a too-fast surface bake forms a bound-skin that traps interior moisture — the identical failure mode to the "casehardening/cracking" warned in Ch.15, here given a food-specific (protein) cause.

V2.4 — Cooking avoids the superficial pellicle that retards drying.
> "The formation of a superficial pellicle (case-hardening), which may considerably retard drying, is avoided by precooking." (p.548)
Interpretation: A pretreatment that breaks the surface-skin barrier is the analogue of a pre-opening / binder-softening step before the falling-rate phase on a hygiene line.

V2.5 — Shrinkage and collapse are explained by the glass-transition state.
> "The glass transition theory is one of the proposed concepts to explain the process of shrinkage and collapse during drying... there is negligible collapse (more pores) in material if processed below glass transition and higher the difference between the process temperature and the glass transition temperature, the higher the collapse." (p.554)
Interpretation: This is the genuine polymer-science bridge in the chapter (see PoP crossref). Tg′ for fish/meat is 11–15 °C (p.554) — freeze-drying stays glassy/porous, hot-air stays rubbery/dense.

V2.6 — Quality-vs-rate trade-off: high T kills microbes but degrades quality.
> "The highest possible drying temperatures should be used to maximize thermal death even though low drying temperatures are best for maintaining organoleptic characteristics [49]. Other alternative is to use high drying temperature initially at high moisture content and then drying at low temperature." (p.552)
Interpretation: The staged high-then-low temperature profile is a direct analogue of the impingement (constant-rate, high flux) → through-air/low-flux (falling-rate) split the hygiene engineer uses to avoid thermal damage.

## 3. Research Method (研究方法)

This is a review/survey chapter [纯理论/综述章节，未使用实证方法]. Method:
- Narrative + literature synthesis across muscle biochemistry, microbiology, and drying engineering (≈95 references, Rahman-dominated).
- Qualitative mechanism description (case-hardening, osmotic phases, glass-transition, pore types).
- Empirical correlations borrowed for porosity: Rahman et al. calamari open/closed porosity ε_op = 0.079 + 0.164y − 0.099y², ε_cp = 0.068 + 0.216y − 0.138y² (p.556), and squid-mantle ε_a = 0.109 + 0.219y − 0.099y² (p.556), where y = X_w/X_w0.
- Generic multiphase density model ρ = (Σ X_i / ρ_Ti)⁻¹ and apparent-shrinkage model V_a/V_0 = (1−ε_ex−ε_a)/(1−ε_ex0−ε_a0) (p.555).
- D-value (decimal-reduction-time) microbial-inactivation discussion (p.552–553), with the key caveat that isothermal D-value models cannot be applied under changing-moisture drying.

No hygiene-specific data; the value is mechanism vocabulary and the glass-transition framework.

## 4. Argumentation (论证逻辑)

- Premise A: Fish is wet, structured, and prone to microbial + oxidative spoilage (p.545, 552).
- Premise B: Drying works by surface evaporation; fast surface heating forms a hard crust that blocks internal moisture (case-hardening, p.550).
- Step 1: Pretreat (salt/cook/smoke) to lower moisture, preserve, and break the pellicle barrier (p.547–548).
- Step 2: Choose dryer by cost/quality; control T, RH, air velocity; stage temperature high→low (p.550–552).
- Step 3: Explain quality changes through biochemistry (browning, lipid oxidation at aw≈0.3) and glass-transition physics of shrinkage (p.553–556).
- Resolution: Low water activity gives shelf life; packaging moisture barrier + desiccant/antioxidant completes preservation (p.552, 557).
The argument is candid that glass-transition theory "does not hold true for all products" (p.554) and that D-value models fail under non-isothermal drying — appropriate scope honesty.
## 5. Role of This Chapter in the Book (在全书中的角色)

Ch.22 is one of the food/agricultural substrate chapters (with Ch.23 grain, Ch.25 fruit/veg, Ch.26 herbal/tea, Ch.27 roots). It is the only chapter that explicitly deploys the glass-transition framework to explain shrinkage/collapse, which dovetails with Ch.4 (property tables) and Ch.24 (sorption/water activity). Its case-hardening and quality-vs-rate material is the biological mirror of Ch.15's web-defect catalogue. Methodologically it is the weakest direct-transfer chapter for hygiene; its role is to supply the case-hardening and Tg-collapse vocabulary that the process-engineering chapters apply to nonwoven webs.

## 6. Strengths and Weaknesses (贡献与局限)

Strengths
- Explicit, verbatim naming of case-hardening as a drying defect and its cause — directly portable (p.550).
- Genuine polymer-physics bridge: glass transition used to explain porosity vs collapse (p.554–555).
- Staged high→low temperature logic for quality-vs-microbial-risk trade-off (p.552).
- Honest caveats on model limits (Tg not universal; D-value models invalid under changing moisture).

Weaknesses
- Substrate is animal muscle; no fluff/SAP/nonwoven data — transfer is by mechanism analogy only.
- Porosity correlations are for calamari/squid (p.556), not hygiene materials — must not be lifted numerically.
- Constant-rate/falling-rate kinetics are discussed qualitatively, not modelled; the thin-layer/deep-bed formalism lives in Ch.23–24.
- OCR concatenates words heavily (e.g., "case hardening" rendered "casehardening"); re-verify against print.

## 7. Key Terms (关键术语)

|||
|---|---|
|Case-hardening|hard crust (dried soluble protein) retarding moisture movement; must be avoided (p.550)|
|Pellicle|superficial protein coating on fish surface that retards drying (p.548, 550)|
|Osmotic dehydration|solvent/solution removes water; ends at mass-transport equilibrium (p.547, 550)|
|Water activity (aw)|low aw preserves by preventing microbial growth (p.550, 552)|
|Monolayer aw≈0.3|greatest resistance to lipid oxidation (p.553)|
|Glass transition (Tg′)|state below which material is glassy/porous, above which rubbery/collapsed (p.554)|
|Isotropic / anisotropic shrinkage|uniform vs directional volume shrinkage (p.555)|
|Rehydration|moistening dry material; partly irreversible (p.556)|
|D-value|decimal reduction time of microorganisms (p.552)|
|Heat-pump drying|lower-T, energy-efficient, better quality alternative (p.551, 552)|

## 8. Micro close-reading (微观精读)

8.1 — The case-hardening rule (p.550). "Heating the surface too fast can produce a hard crust (mostly dried soluble protein), which retards movement of moisture. This phenomenon (case-hardening) can severely reduce the rate of drying and must be avoided." This sentence is the chapter's most portable process rule. Replace "dried soluble protein" with "dried binder / fused pulp skin" and it describes exactly the surface-skin defect that caps drying rate on a hot-air nonwoven line — the same class of failure Ch.15 calls casehardening/cracking. The operative principle: control the surface flux so the interior keeps feeding moisture to a permeable (not vitrified) surface.

8.2 — Glass-transition collapse (p.554–555). "In freeze-drying, since the temperature of drying is below Tg′ ... the material is in the glassy state. Hence shrinkage is negligible. As a result the final product is very porous. In hot air drying, on the other hand, since the temperature of drying is above Tg′ ... the material is in the rubbery state and substantial shrinkage occurs." This is the only place the chapter invokes polymer physics. The bridge to hygiene: a binder/fibre web or SAP particle also has a Tg; drying above Tg′ (rubbery) collapses pores and fuses structure, drying below (glassy) preserves porosity — the same lever used to keep an airlaid core lofty.

8.3 — Monolayer and oxidation (p.553). "At water activities around the monolayer (aw ≈ 0.3), resistance to oxidation is greatest." The monolayer concept (BET-style) is the food analogue of the moisture window below which SAP/pulp degrade slowly — the quantitative version appears in Ch.24.

8.4 — Staged temperature (p.552). "high drying temperature initially at high moisture content and then drying at low temperature." A concrete two-stage recipe for trading microbial kill against quality — the same shape as constant-rate (high flux) → falling-rate (low flux) on hygiene lines.

## 9. Concept deep-dive (概念深掘)

9.1 Case-hardening / pellicle (§22.4.1, p.548, 550). Defined operationally: a surface crust of dried soluble proteins that blocks internal moisture transport. Caused by heating the surface too fast (p.550) and by superficial pellicle in smoking (p.548). Avoided by precooking (p.548) and by moderate initial temperature (p.551: "maximum temperature of 70°C should be used"). Academic origin: general dehydration engineering; the chapter does not give a mathematical model — it is a qualitative barrier concept the engineer must respect empirically.

9.2 Glass-transition model of shrinkage (§22.5.5, p.554–555). Definition (p.554): collapse is governed by the gap between process temperature and Tg′; below Tg′ → glassy, porous, minimal shrinkage; above → rubbery, collapsed, dense. Tg′ for fish/meat = 11–15 °C (p.554). Pore formation grouped into "with inversion point" and "without inversion point" (Fig. 22.1–22.2, p.555–556). Generic shrinkage model: V_a/V_0 = (1−ε_ex−ε_a)/(1−ε_ex0−ε_a0) (p.555). This is the chapter's deepest analytic contribution and the genuine polymer-science link (see PoP crossref).

9.3 Osmotic dehydration equilibrium (§22.2.1.2, p.547). Dynamic period (mass-transfer rates change until equilibrium) → equilibrium (net mass transport = 0). A conceptual template for any desorption that approaches a steady residual moisture set by ambient conditions — the hygiene analogue is Ch.24's equilibrium moisture content.

## 10. Critique (批判性评估)

- No quantitative drying kinetics. The chapter names case-hardening and Tg-collapse but gives no thin-layer or deep-bed model; the engineer must go to Ch.23–24 for prediction.
- Substrate mismatch. All porosity/browning/lipid-oxidation data are muscle-specific; none transfer numerically to fluff/SAP.
- Tg caveat. Author admits glass-transition "does not hold true for all products" (p.554) and lists competing mechanisms (surface tension, capillary force, environment pressure) — so Tg is necessary but not sufficient to predict collapse.
- OCR noise. Heavy word concatenation ("casehardening", "nonsignificant"); re-verify equations/quotes against the print edition.
## 11. Hygiene-Material Relevance & Action Cards (卫材相关性与行动卡)

Relevance rating: ★★ (low–medium). Substrate is fish muscle; the chapter never addresses fluff pulp, SAP, or nonwovens. Genuine mechanism transfer exists for case-hardening, glass-transition collapse, staged-temperature, and monolayer stability — but no diaper application may be invented for fish, salting, smoking, or seafood microbiology.

H11.1 — Treat surface-skin as a rate-limiting barrier (★★★). Action: On hot-air lines for fluff/binder webs, cap initial surface flux so a vitrified/dried-skin layer does not form and trap interior moisture — the case-hardening rule (p.550) applied to nonwoven drying.

H11.2 — Use the Tg′ lens for loft/collapse (★★★). Action: Treat an airlaid/SAP web like the freeze-vs-hot-air contrast (p.554–555): keep the drying zone at/under the relevant glass-transition window to preserve porosity and avoid rubbery collapse; raise T only when the web is already glassy-stable.

H11.3 — Stage temperature high→low (★★★). Action: For microbial-risk or thermal-sensitive hygiene substrates, use high flux at high moisture (constant-rate) then low flux at low moisture (falling-rate) — the staged profile of p.552 — to balance throughput against quality.

H11.4 — Respect the monolayer window for storage (★★). Action: Note the aw≈0.3 monolayer oxidation-minimum (p.553) as a qualitative anchor when setting warehouse RH targets for moisture-sensitive cores (quantitative version in Ch.24).

## 12. Book-Map Quotes (本书脉络引证)

- Ch.15 (p.384): casehardening/cracking on heat-sensitive webs — Ch.22 gives the food-side cause (dried-protein crust, p.550).
- Ch.23 (p.561+): thin-layer / deep-bed modelling — the kinetics Ch.22 lacks.
- Ch.24 (p.573+): equilibrium moisture content / water-activity / sorption — the quantitative home of the osmotic-equilibrium (p.547) and monolayer (p.553) concepts.
- Ch.4 (p.81): property tables / internal diffusion — the physics behind "drying is surface evaporation" (p.550).


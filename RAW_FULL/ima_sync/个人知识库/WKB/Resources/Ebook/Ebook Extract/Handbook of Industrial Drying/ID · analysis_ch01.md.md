---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_71c62b21c08aa760d75f85aba7d514ea001a693ee6c0644e"
source_file: "ID · analysis_ch01.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch01.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch01.md.md

# Chapter 1 — Principles, Classification, and Selection of Dryers

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 1 (A.S. Mujumdar) establishes the conceptual and thermodynamic foundation of industrial drying. It frames drying as a thermal separation operation producing a solid by evaporating a volatile (usually water), distinguishing bound vs unbound moisture and two simultaneous subprocesses — external (Process 1: heat/mass transfer at the surface) and internal (Process 2: moisture transport within the solid). The chapter then builds the psychrometric toolkit (vapor–liquid equilibrium, Clausius–Clapeyron, humidity, wet/dry bulb, enthalpy–humidity charts), the internal-state description (moisture content, sorption isotherms, hysteresis, characteristic drying-rate curve), and a classification of dryers by heating method, pressure, and conveying mode. It closes with selection guidelines, energy/safety/environmental constraints, and design methodology. For the hygiene-materials reader the chapter is the reference framework: cylinder/can dryers for paper and pulp, convective hot-air dominance, glass-transition limits for polymers, and GMP/hygienic-design obligations — though most specifics are deferred to later chapters.

## 2. Key Viewpoints (3–6, each with page + verbatim quote + interpretation)

### Viewpoint 1 — Drying is energy-dominant and structurally diverse

- Page: p.1
- Quote: > "Drying is perhaps the oldest, most common and most diverse of chemical engineering unit operations. Over 400 types of dryers have been reported whereas over 100 distinct types are commonly available. It competes with distillation as the most energy-intensive unit operation due to the high latent heat of vaporization and the inherent inefficiency of using hot air as the (most common) drying medium."
- Interpretation: The author opens by framing drying as both ubiquitous and expensive. For a fluff-pulp / nonwoven buyer this is the central economic fact: drying of papermaking operations consumes up to 35% of plant energy (p.1), so dryer selection is a capital-and-energy decision, not a peripheral one.
### Viewpoint 2 — Two coupled processes govern every dryer; either can be limiting

- Page: p.1
- Quote: > "When a wet solid is subjected to thermal drying, two processes occur simultaneously: 1. Transfer of energy (mostly as heat) from the surrounding environment to evaporate the surface moisture and 2. Transfer of internal moisture to the surface of the solid and its subsequent evaporation due to process 1."
- Interpretation: This is the organizing dichotomy of the whole handbook (Process 1 external, Process 2 internal). In diaper cores the internal moisture transport (capillary/wapor diffusion through fluff pulp and SAP) is usually the rate-limiting step at low final moisture, so surface-air conditions matter far less than residence time and bed depth.
### Viewpoint 3 — Convective hot-air drying dominates industry; indirect is more efficient

- Page: p.3
- Quote: > "Over 85% of industrial dryers are of the convective type with hot air or direct combustion gases as the drying medium. Over 99% of the applications involve removal of water. All modes except the dielectric (microwave and RF) supply heat at the boundaries of the drying object so that the heat must diffuse into the solid primarily by conduction."
- Interpretation: Hot-air convection is the default for pulp, tissue and nonwoven through-dryers. The thermal-efficiency penalty of convective dryers (large enthalpy carried out in exhaust) motivates combined direct–indirect designs (e.g., fluid bed with immersed coils, p.21) — directly relevant to energy cost/tonne.
### Viewpoint 4 — Bound vs unbound, and hygroscopic vs nonhygroscopic, define the drying problem

- Page: p.1
- Quote: > "Moisture held in loose chemical combination, present as a liquid solution within the solid or even trapped in the microstructure of the solid, which exerts a vapor pressure less than that of pure liquid, is called bound moisture. Moisture in excess of bound moisture is called unbound moisture."
- Interpretation: This classification (extended on p.12 with nonhygroscopic capillary-porous, hygroscopic-porous, and colloidal nonporous media) is the hinge for residual-moisture specification in cellulose fluff and SAP — bound moisture sets the equilibrium moisture content and hence the floor of achievable dryness.
### Viewpoint 5 — The characteristic drying-rate curve: constant-rate then falling-rate, often the whole job

- Page: p.16
- Quote: > "In the constant rate period the rate of drying is determined by the rate of evaporation. When all the exposed surface of the solid ceases to be wetted, vapor movement by diffusion and capillarity from within the solid to the surface are the rate-controlling steps."
- Interpretation: For thin, fast sheets (tissue, nonwoven web) drying may occur almost entirely in the constant-rate period; for thick/packed hygroscopic beds (fluff in a core) the falling-rate period dominates and residence time scales with the square of thickness (p.16), arguing for thin layers / agitation.
### Viewpoint 6 — Dryer selection is a multi-criteria compromise, never a single optimum

- Page: p.25
- Quote: > "A wrong dryer for a given application is still a poor dryer, regardless of how well it is designed. Note that minor changes in composition or physical properties of a given product can influence its drying characteristics … leading to a different product and in some cases severe blockages in the dryer itself."
- Interpretation: Selection must be done by the user with pilot data, not delegated to vendors. For hygiene products where a few-percent composition shift (add SAP, change binder) changes handling, this is a direct warning against copying another line's dryer choice.
## 3. Research Method & Data Sources

[纯理论/综述章节，未使用实证方法] — This is a foundational review/theory chapter. It synthesizes psychrometric thermodynamics, equilibrium data, and dryer-classification tables from the cited literature (Keey 1972/1978, Perry, Treybal, Kessler, Toei, Sloan, McCormick, Schlu¨nder, etc.). No new experiments are reported; Tables 1.1–1.7 are compiled from operating practice and Ref. 24. Validity rests on the cited handbooks and on the implicit assumption that air–water psychrometrics approximate other diatomic-gas systems (p.9).

||||||
|---|---|---|---|---|
|Thermodynamic|Vapor–liquid equilibrium, Clausius–Clapeyron|CRC/Perry handbooks|Equations 1.1–1.49|Exact for pure substance; ideal-gas approx|
|Psychrometric|Humidity / wet-bulb / enthalpy charts|Mollier, Perry|Enthalpy–humidity diagram|Approximate above Y=0.05 (p.8)|
|Solid-state|Sorption isotherms, characteristic curve|Lab measurement (Kessler, Nemitz)|Figs 1.6–1.16|Material-specific|
|Selection|Taxonomy + checklist|Vendor practice (Table 1.6)|Heuristic|Non-unique, experience-driven|

## 4. Argumentation Process

The author builds the case in four moves:
1. Problem framing (p.1–2): define drying, assert energy dominance and diversity, list the "fascinating" features (size, porosity, time, speed ranges) that make scale-up hard.
2. External physics (p.3–11): from vapor pressure → Clausius–Clapeyron → humidity definitions → wet/dry bulb → enthalpy–humidity chart → adiabatic saturation. Each step is a deduction from mass/energy balances.
3. Internal physics (p.12–17): classify solids by pore/binding structure; introduce sorption isotherms, hysteresis, enthalpy of binding; derive the constant/falling-rate periods and the characteristic drying curve as a normalizing device.
4. Engineering synthesis (p.18–28): classify dryers (convection/conduction/radiation/dielectric; pressure; conveying), then fold in energy, safety, environmental and GMP constraints, and close with a selection checklist and the "think system, not dryer" conclusion.

Rhetorically the chapter is authoritative and cautionary: it repeatedly stresses that no single design procedure fits all dryers (p.3), that scale-up is "generally very difficult" (p.3), and that the user must stay proactive (p.25).

## 5. Role in the Book

Chapter 1 is the foundation / taxonomy chapter. It supplies the vocabulary (bound/unbound, X*, X_cr, f, characteristic curve), the psychrometric engine used in Ch.2–3, and the selection logic that Ch.5 (spreadsheet design) and Ch.6 (indirect dryers) operationalize. It points forward to specialized chapters on superheated steam (Ch.35), novel dryers (Ch.36), scale-up (Genskow), and mathematical modeling (Turner & Mujumdar) — exactly the pipeline the hygiene reader needs (e.g., can-dryer for pulp → Ch. on paper; conduction dryers → Ch.6).

## 6. Strengths & Weaknesses

✅ Strengths:
- Comprehensive, self-contained psychrometric derivation; the wet-bulb / Lewis-relation treatment (p.10–11) is a clean, quotable result:
> "The identity of hC/K with CPY was first found empirically by Lewis and hence is called the Lewis relation." (p.11)
- Honest about limits: "all processes involved, even in the simplest dryer, are highly nonlinear and hence scale-up of dryers is generally very difficult." (p.3)

⚠️ Limitations / contestable:
- The characteristic drying curve criteria are acknowledged as restrictive: "These criteria are restrictive, and it is quite unlikely that any solid will satisfy them over an exhaustive range of conditions" (p.17) — so design use is interpolation only.
- Psychrometric equations "not recommended above a humidity of 0.05 kg/kg" (p.8) — a narrow envelope for high-moisture pulp lines.
- The chapter is deliberately silent on novel dryers and on mathematical kinetics models, deferring both; the hygiene reader must go elsewhere for SAP/nonwoven specifics.

## 7. Key Terms / Concepts

- Bound moisture: (p.1) "Moisture held in loose chemical combination … which exerts a vapor pressure less than that of pure liquid, is called bound moisture."
- Unbound moisture: (p.1) "Moisture in excess of bound moisture is called unbound moisture."
- Hygroscopic-porous media: (p.12) "Hygroscopic-porous media, such as clay, molecular sieves, wood, and textiles. … (3) Shrinkage often occurs in the initial stages of drying."
- Colloidal (nonporous) media: (p.12) "Colloidal (nonporous) media, such as soap, glue, some polymers (e.g., nylons), and various food products."
- Equilibrium moisture content X*: (p.12) "the moisture content of the solid is called the equilibrium moisture content under the prevailing conditions."
- Critical moisture content X_cr: (p.16) transition where the surface film is so reduced "that further drying causes dry spots to appear upon the surface."
- Characteristic drying curve: (p.17) normalized N/N0 vs (X−X*)/(X0−X*); "often utilized for interpolation and prediction of dryer performance."
- Convective dryer: (p.21) heat supplied by heated air/gas flowing over the surface; "also called direct dryers."
- Conduction (indirect) dryer: (p.21) "Heat for evaporation is supplied through heated surfaces … placed within the dryer to support, convey, or confine the solids."
- Glass transition temperature: (p.26) appears in the heat-sensitivity checklist ("Melting point … Glass transition temperature") as a design limit for temperature-sensitive solids.
## 8. Micro close-reading (ONE key paragraph)

Source paragraph (p.16, second drying stage / falling-rate discussion):

"On further drying (the second falling rate period or the third drying stage), the rate at which moisture may move through the solid as a result of concentration gradients between the deeper parts and the surface is the controlling step. The heat transmission now consists of heat transfer to the surface and heat conduction in the product. Since the average depth of the moisture level increases progressively and the heat conductivity of the dry external zones is very small, the drying rate is increasingly influenced by the heat conduction. However, if the dry product has a relatively high bulk density and a small cavity volume with very small pores, drying is determined not so much by heat conduction but by a rather high resistance to diffusion within the product. … During this stage some of the moisture bound by sorption is removed. As the moisture concentration is lowered by drying, the rate of internal movement of moisture …"

Sentence-by-sentence breakdown:
1. "On further drying … concentration gradients … is the controlling step." — Names the mechanism shift to internal diffusion once surface is dry; this is the falling-rate period's dominant resistance.
2. "The heat transmission now consists of heat transfer to the surface and heat conduction in the product." — Heat path now interior, not just surface evaporation.
3. "Since the average depth of the moisture level increases progressively and the heat conductivity of the dry external zones is very small …" — Explains why rate falls: dry shell is a poor conductor; this is the case-hardening risk.
4. "However, if the dry product has a relatively high bulk density and a small cavity volume … high resistance to diffusion within the product." — Counter-case: dense, fine-pored beds are diffusion-limited, not conduction-limited.
5. "During this stage some of the moisture bound by sorption is removed." — Links back to bound-moisture concept (p.1); the hardest moisture leaves last.
6. "As the moisture concentration is lowered by drying, the rate of internal movement of moisture …" — Sets up the thickness-squared scaling (next lines): long dryness times for low final moisture.

💡 Standout line: "the heat conductivity of the dry external zones is very small" — the dry shell that forms on a fluff/SAP bed is itself the insulator that throttles the whole drying rate; thin layers or agitation are the only remedies.

## 9. Concept deep-dive

### Core concept: The characteristic drying-rate curve (p.17)

- Definition (p.17): normalized variables f = N/N0 and f = (X−X*)/(X0−X*); "all the curves could often be approximated to a single curve, 'characteristic' of a particular substance."
- Operational definition? Yes — it is an empirical interpolation tool, not a mechanistic model. Criteria: (1) X_cr invariant to initial moisture/external conditions; (2) all curves geometrically similar. The author concedes both are "restrictive" and rarely fully satisfied.
- Usage scenes in this chapter: introduced to collapse family-of-curves data (Fig. 1.15 molecular sieves/silica gel), then used to justify that drying behavior depends on exposed surface per unit volume and on form-stability (p.17).
- Relation to other concepts: bridges Process 2 (internal transport) to design residence time; feeds Ch.3 simulations and Ch.5 spreadsheet sizing.
- Academic origin: Keey & Suzuki (1974), Int. J. Heat Mass Transfer 17, 1455–1464 (Ref. [14]).
### Core concept: Sorption isotherm / hysteresis (p.13–14)

- Definition (p.13): graph of moisture bound by sorption per unit weight vs relative humidity; distinguishes monomolecular layer (A), multilayer (B), capillary condensation/swelling (C).
- Operational definition? Yes — measured experimentally (p.14) by equilibrating dry product at stepwise humidities.
- Usage: sets equilibrium moisture content X* and the temperature coefficient @X*/@T = −A·X* (A = 0.005–0.01 K⁻¹ for fibers/wood/potatoes, p.14).
- Hygiene link: PVC powder is "mildly hygroscopic" (Fig. 1.7); nylons are colloidal nonporous (p.12) — both polymer classes appear in hygiene films/fibers.
## 10. Academic critique & open questions

- Theoretical: The chapter rests on quasi-steady, continuum transport with ideal-gas and constant-Cp approximations; it admits these break for high humidity and for swelling/shrinking solids where "mechanisms of moisture transfer may also change with elapsed time of drying" (p.3).
- Methodological: Scale-up is called "the central issue of most significance" yet "information on this subject is rather limited and widely scattered" (p.28); no unified design package exists because of product/dryer diversity.
- Scope: Deliberately excludes mathematical kinetics models and novel dryers.
- Open questions: (1) How to predict X_cr and the falling-rate shape for mixed beds (fluff + SAP + binder) that change form as they dry? (2) Can superheated-steam psychrometrics (mentioned p.26–27) be folded into the same selection logic without vendor-specific data?
## 11. Hygiene-material relevance & action cards

Relevance rating: ★★★★☆ (foundational; direct only where paper/pulp/polymer drying is named).

ACTION CARD 1 — Fluff-pulp / tissue energy cost
- Situation: Specifying or benchmarking a through-/can-dryer for fluff pulp or tissue.
- How to apply: Use p.1 energy fact — "Energy consumption in drying ranges from a low value of under 5% for the chemical process industries to 35% for the papermaking operations" — as the anchor for energy-cost/tonne; target convective exhaust enthalpy recovery (p.23 recycle, heat pumps).
- Expected effect: Identify that pulp/tissue drying, not converting, is the dominant energy sink; prioritize heat recovery over throughput tweaks.

ACTION CARD 2 — Polymer / SAP heat-sensitivity ceiling
- Situation: Drying SAP granules or PP/PE nonwoven webs that must not degrade.
- How to apply: Apply p.26 checklist item "Glass transition temperature" and p.21 steam-environment note ("heat sensitivity can be quite different in a steam environment") to set the maximum allowable temperature; prefer indirect/vacuum or short-residence (spray/flash) routes for heat-sensitive solids (p.22).
- Expected effect: Avoid yellowing / crosslinking of SAP and melting of thermoplastic fibers by bounding dryer temperature to Tg/Tm window.

ACTION CARD 3 — Residual-moisture spec from sorption isotherm
- Situation: Setting a warehouse-stable final moisture for fluff or core.
- How to apply: Use X* (equilibrium moisture content, p.12) and the temperature coefficient @X*/@T = −A·X* (p.14) to compute the moisture floor at storage RH/T; avoid overdrying (p.18 "Overdrying should be avoided").
- Expected effect: Specify a residual-moisture band that is achievable and non-degrading rather than an arbitrarily low number.

## 12. Book-map quotes (Top 3 representative quotes)

"Over 85% of industrial dryers are of the convective type with hot air or direct combustion gases as the drying medium." — p.3 — anchors the default technology the hygiene line will almost certainly use.

"the heat conductivity of the dry external zones is very small" (falling-rate period) — p.16 — the single physical reason thin layers / agitation beat long residence times for packed cores.

"It is typically not a desirable option to depend exclusively on prior experience, reports in the literature or vendors' recommendations. Each drying problem deserves its own independent evaluation and solution." — p.28 — the governing principle for any new hygiene-material dryer purchase.

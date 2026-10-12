---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_022fa4eb002e3219ba95de1d8288518e001a693ee6c0644e"
source_file: "ID · analysis_ch02.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch02.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch02.md.md

# Chapter 2 — Experimental Techniques in Drying

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21 (the source's own embedded print p.X markers use this offset; e.g., PDF page 52 → print p.31); this is an estimate and should be spot-checked against the print edition.

Chapter 2 (K. Molnár) is the measurement chapter of the handbook: it catalogues the laboratory and pilot-scale experimental techniques needed to obtain the material and transport parameters that every dryer design calculation consumes — moisture content, sorption-equilibrium isotherms, drying-rate curves, and the heat/mass transfer and diffusivity coefficients of wet and dry solids. It is deliberately a "techniques" chapter rather than a theory chapter: it tells the engineer how to measure what Chapter 1 defined and what Chapters 3–5 will use. The structure moves from equilibrium properties (moisture content of solids and gases; sorption isotherms via saturated-salt and developed-vapor-pressure methods) to kinetics (lumped and distributed-parameter experiments) to bed-level coefficients (fixed/moving and through-circulation dryers). For the hygiene-materials reader this is the QA and characterisation playbook: how to certify fluff/SAP/nonwoven residual moisture, how to measure an isotherm for a new absorbent, and how to run the small-scale drying test that feeds scale-up.

## 2. Key Viewpoints (each with page + verbatim quote + interpretation)

### Viewpoint 1 — Drying parameters cannot be calculated; they must be measured

- Page: p.31
- Quote: > "The calculation of drying processes requires a knowledge of a number of characteristics of drying techniques, such as the characteristics of the material, the coefficients of conductivity and transfer, and the characteristics of shrinkage. In most cases these characteristics cannot be calculated by analysis … these characteristics can be determined only by adequate experiments."
- Interpretation: This is the chapter's governing thesis and the single most important message for a hygiene R&D lab: there is no shortcut. To size a fluff-pulp or SAP dryer you must run experiments on your actual material — generic literature values for "pulp" or "SAP" will not do, because the coefficients depend on the specific grade, binder, and geometry.
### Viewpoint 2 — The five aims of a drying experiment

- Page: p.32
- Quote: > "The general aim of drying experiments is as follows [1]: 1. Choice of adequate drying equipment 2. Establishing the data required for planning 3. Investigation of the efficiency and capacity of existing drying equipment 4. Investigation of the effect of operational conditions on the shape and quality of the product 5. Study of the mechanism of drying."
- Interpretation: A well-planned experimental programme serves both capital selection (aim 1–3) and product-quality control (aim 4) and fundamental understanding (aim 5). For a new hygiene line, aim 1 (equipment choice) and aim 4 (quality/shape — e.g., nonwoven web integrity, SAP granule integrity) are the priorities.
### Viewpoint 3 — Direct moisture determination: oven method with strict protocol

- Page: p.32
- Quote: > "The direct methods consist essentially of determination of the moisture content of a sample by drying carried out in a drying oven with or without blow through of air, or by drying in a vacuum chamber or in a vacuum desiccator. The material is disintegrated into pieces of 1–2 mm³, and a sample of known mass (4–5 g) is placed into a previously dried and weighed glass container … dried at 102–105°C. The drying process may be considered complete when the difference between the values obtained for the moisture content … by two consecutive measurements does not exceed ±0.05%."
- Interpretation: This is the reference gravimetric method every hygiene QC lab already uses (or should). The discipline — 1–2 mm³ particles, 4–5 g sample, 102–105°C, ±0.05% convergence — is the audit standard for fluff-pulp and SAP residual-moisture certification. Note the author's caution (p.32) that the faster 130–150°C variant can deviate by 0.5–1.0% and is only approximate.
### Viewpoint 4 — Indirect/online methods for industrial speed

- Page: p.33
- Quote: > "Under industrial conditions the moisture present in material must be determined by faster methods, such as by electrical methods of which three main varieties have become widespread: moisture determination based on the change of the ohmic dc resistance, a measurement of the electrostatic capacitance (dielectric constant of the material), and a measurement of the loss in an ac field."
- Interpretation: For a running nonwoven or pulp line you cannot stop to oven-dry; you use dielectric/capacitance sensors. The chapter flags Karl–Fischer titration, toluene distillation, and absolute-ethanol extraction (p.33) for water specifically — relevant when auditing SAP (which is water-swollen) where oven methods can degrade the crosslinked network.
### Viewpoint 5 — Sorption hysteresis must be measured on the correct branch

- Page: p.33
- Quote: > "Although the materials may approximate the equilibrium moisture content either by moisture uptake (adsorption) or by drying (desorption), the value of equilibrium vapor pressure generally depends, for capillary-porous materials, upon the direction of the approximation … This phenomenon is known as sorption hysteresis. For this reason it is necessary to distinguish adsorption equilibrium moisture from desorption equilibrium moisture."
- Interpretation: Critically for hygiene: a fluff core in storage re-adsorbs from the warehouse air (adsorption branch), but the dryer produces it on the desorption branch. The equilibrium moisture content X* you design to is different on the two branches; the chapter mandates measuring both. This directly supports the Ch1 Q2 concern about composite cores.
### Viewpoint 6 — Scale-up validity depends on experimental fidelity, not just the math

- Page: p.39–40
- Quote: > "In order to obtain results that can be applied for scale-up, the following aspects must be taken into account: the sample must not be too small and the conditions of drying must if possible be identical to the conditions anticipated in the industrial unit … 1. The sample must be placed in a similar way in the laboratory unit. 2. The ratios of the drying surface to the nondrying surface must be identical."
- Interpretation: The lumped drying-rate experiment (mass vs. time → X(t) → N vs. X, Eqs. 2.3–2.6) only scales up if the lab sample mimics the industrial geometry and surface-area ratio. For a through-air nonwoven web this means testing a strip with the same open-area and thickness as production, not a crumpled handful.
## 3. Research Method & Data Sources

This is an experimental-methods chapter: it reports no new data of its own but systematises the measurement protocols drawn from the cited literature (Perry; A.V. Lykov, Theory of Drying; Keey 1972; Toei & Hayashi; Imre; Szentgyörgyi; Krischer & Kröll; Molnár's own theses and symposium papers). The "data" in the chapter are illustrative worked examples (e.g., the water-and-powdered-chalk suspension, §2.4.3.1; the sand/gypsum double layer, §2.4.3.3; the rotary contact-fluid dryer, §2.5.1) used to demonstrate how the derived equations recover a coefficient from measurements.

||||||
|---|---|---|---|---|
|Gravimetric equilibrium|Oven / vacuum desiccator; Karl–Fischer|Lab sample|Balance, ±0.05% convergence|Reference accuracy; slow|
|Sorption isotherm|Saturated-salt (constant p_v); developed-p_v (static/dynamic/gravimetric)|Closed chamber + salt soln|Manometer, psychrometer|Branch-dependent (hysteresis)|
|Kinetics (lumped)|Convection drying rig, continuous weighing|Climate duct, balance|Fig. 2.5 apparatus|Needs geometric similarity for scale-up|
|Kinetics (distributed)|Temperature/moisture profiles in slab|Thermocouples in plane slab|Eigenvalue fit (Eqs 2.12–2.25)|1-D, homogeneous slab|
|Bed coefficients|Rotary / through-circulation rig|Plant or pilot bed|Volumetric h_V, K_V (Eqs 2.37–2.53)|Not generally applicable across dryers|

## 4. Argumentation Process

The author proceeds as a measurement engineer, not a theorist:

- Equilibrium first (§2.2–2.3): before any rate can be measured you must know moisture content (of solid and gas) and the sorption isotherm. The isotherm measurement is split into constant vapor-pressure (saturated-salt solutions give a known p_v, Table 2.3) and developed vapor-pressure (the sample itself creates p_v in a closed space, measured by manometer/psychrometer/isotonic method) techniques.
- Kinetics second (§2.4): once equilibrium is known, run a drying experiment. The lumped approach (integral-average moisture only) gives the rate curve N(X); the distributed approach (local T and X profiles) additionally yields heat and mass diffusivities.
- Coefficient extraction third (§2.4.2–2.4.3): from the constant-rate period extract gas-side h and K (Eqs 2.7–2.11); from the falling-rate period extract internal k_h, k_m, l_h, l_m via eigenvalue fits (Eqs 2.19–2.25) or, for dry-layer penetration, the receding-front model (Eqs 2.26–2.36).
- Bed scale-up last (§2.5): for fixed/moving/through-circulation beds where the interfacial area is unknown, replace area-based h, K with volumetric h_V, K_V (Eqs 2.37–2.53), and give an empirical rotary-dryer correlation (Eq 2.45).
The rhetorical stance is pragmatic and caveat-laden: "The coverage is by no means all-inclusive" (p.49); methods are "extremely diverse and in many cases very specific" (p.32).

## 5. Role in the Book

Chapter 2 is the instrumentation bridge between Chapter 1's definitions (bound/unbound moisture, X*, characteristic curve) and Chapters 3–5's calculations and designs. It is where the abstract symbols of Ch.1 become numbers you can measure. Concretely:
- It operationalises X* (Ch.1) via the sorption-isotherm protocols (§2.3) and the adsorption/desorption branch distinction (hysteresis).
- It supplies the drying-rate curve N(X) that Ch.1 introduced as the "characteristic curve" (§2.4.2, Figs 2.6–2.9).
- It defines the transport coefficients (h, K, k_h, k_m, l_h, l_m) that Ch.3 (process calculations) and Ch.5 (spreadsheet design) will plug into balances.
- It introduces volumetric coefficients for beds (§2.5) that Ch.6 (indirect dryers) and any through-circulation/rotary design will use.
It is the chapter a hygiene R&D engineer returns to whenever a new material (new SAP grade, new airlaid furnish) must be characterised before a dryer is specified.

## 6. Strengths & Weaknesses

✅ Strengths:
- Self-contained measurement recipes with tolerances — e.g., the ±0.05% oven convergence (p.32) and the 1–2 mm³ / 4–5 g sample spec are directly implementable QC rules.
- Pedagogically clear ladder: equilibrium → kinetics → coefficients → bed scale-up, each with a worked example.
- Explicit about scale-up prerequisites (geometric and surface-ratio similarity, p.39–40) — a rare and valuable honesty.
- Covers both gas-side (constant-rate) and internal (falling-rate, distributed) coefficient extraction, including the receding-front model for porous solids (p.44) and double-layer materials (p.44–45).

⚠️ Limitations / contestable:
- Entirely 1-D, homogeneous-slab / simple-bed oriented. The distributed-parameter maths assumes a plane slab of uniform properties; it does not address the anisotropic, multi-component webs and cores that dominate hygiene products.
- Double-layer / heterogeneous treatment (p.44–45) is mentioned (laminates, coated seeds) but only for constant-thickness two-layer slabs — not for a SAP/fluff mixture where components have opposing sorption thermodynamics (the Ch.1 Q2 gap persists here).
- The through-circulation section (p.48) flags that heterogeneous mixtures (alfalfa stems vs. leaves) need component-specific treatment and "care must be exercised" — but gives no quantitative method for a multi-component hygiene furnish.
- References are Eastern-European / Hungarian-centric (Lykov, Imre, Molnár, Krischer & Kröll) and dated (much pre-1990); a reader may struggle to find the primary apparatus details in Western literature.
- No uncertainty/error analysis: the eigenvalue fitting (Eqs 2.19–2.25) and the slope-extraction from Figs 2.15–2.16 are presented as exact, with no discussion of propagation of measurement error.

## 7. Key Terms / Concepts

- Direct moisture method: (p.32) oven/vacuum drying of a disintegrated sample to constant mass (±0.05% convergence).
- Indirect moisture method: (p.33) electrical — ohmic dc resistance, dielectric capacitance, ac loss factor; plus Karl–Fischer, toluene distillation, ethanol extraction.
- Sorption hysteresis: (p.33) "the value of equilibrium vapor pressure generally depends … upon the direction of the approximation … known as sorption hysteresis"; adsorption vs. desorption branches must be distinguished.
- Constant vapor-pressure isotherm method: (p.36) saturated salt solutions fix p_v (Table 2.3 gives relative vapor pressures of many salts).
- Developed vapor-pressure method: (p.36–39) the wet sample creates p_v in a closed space; measured by manometer (freeze-out), psychrometer (wet/dry bulb), or isotonic salt method.
- Lumped-parameter model: (p.38) only integral-average moisture and surface/average temperature measured; opposed to distributed-parameter.
- Drying rate N: (p.40) N = −(1/A_s)·dm_SW/dt = (m_S/A_s)·dX/dt (Eq. 2.6).
- Gas-side coefficients: (p.40) h from j_q = h(T_G − T_W) (Eq. 2.7); K from N = K(Y_W − Y_G) (Eq. 2.10).
- Distributed-parameter coefficients: (p.42–43) thermal diffusivity k_h and mass diffusivity k_m from 1-D transient eigenvalue fits (Eqs 2.12–2.25).
- Receding/penetrating front model: (p.44) evaporation front moves inward through macroporous/capillary-porous bodies in the falling-rate period.
- Volumetric transfer coefficients: (p.46) h_V = h·dA_s/dV, K_V = K·dA_s/dV (Eqs 2.37–2.38) for beds of unknown interfacial area.
- Through-circulation coefficients: (p.48) K_V(t), h_V(t) from adiabatic bed energy/mass balances (Eqs 2.46–2.53).
## 8. Micro close-reading (ONE key paragraph)

Source paragraph (p.44, receding/penetrating-front model, §2.4.3.3):

"In the course of drying of macroporous and capillary-porous materials—in the falling rate period of drying—the moisture from the pores of the material is removed, and an evaporation front penetrates from the surface of the material into the interior. At a given time the primarily wet material can be divided into two parts separated by an evaporation front: a part already dried and a part that is still wet. The moisture evaporated at the plane of phase change must pass through the pores of the already dried layer in order to leave the material. At the same time the heat required for drying has to pass through the already dried layer to carry out the evaporation. This model of drying is known as the penetrating or receding front model and is described in the literature [2,4,21,22]."

Sentence-by-sentence breakdown:
1. "…an evaporation front penetrates from the surface of the material into the interior." — Names the mechanism: drying is no longer surface evaporation but an inward-moving phase-change boundary.
2. "At a given time the primarily wet material can be divided into two parts separated by an evaporation front: a part already dried and a part that is still wet." — The solid becomes a two-zone composite (dry shell + wet core) at every instant.
3. "The moisture evaporated at the plane of phase change must pass through the pores of the already dried layer in order to leave the material." — Vapor must diffuse outward through the dry zone; this is the mass-transfer resistance in the falling-rate period.
4. "At the same time the heat required for drying has to pass through the already dried layer to carry out the evaporation." — Heat must conduct inward through the same dry zone; this is the heat-transfer resistance.
5. "This model of drying is known as the penetrating or receding front model …" — Gives the canonical name and points to Lykov, Krischer & Kröll, Szentgyörgyi/Molnár as primary sources.

💡 Standout line: "the heat required for drying has to pass through the already dried layer" — the dry shell that forms on a fluff/SAP bed is simultaneously the barrier to both heat (in) and vapor (out). This is the physical reason the falling-rate period is so slow and why Ch.1's "heat conductivity of the dry external zones is very small" is the controlling resistance. For a through-air nonwoven web, this justifies thin, open structures that keep the dry-zone path short.

## 9. Concept deep-dive

### Core concept A — The lumped drying-rate experiment (§2.4.2, p.39–40)

- Definition: place a sample in a controlled-climate airflow (constant T_G, Y_G, velocity), weigh it continuously, and convert mass to moisture content X(t) = (m_SW − m_S)/m_S (Eq. 2.5) and then to the drying-rate curve N vs. X via N = (m_S/A_s)·dX/dt (Eq. 2.6). From N(X) you read off the constant-rate N_c, the critical moisture X_cr, and the equilibrium X*.
- Operational? Yes — this is the single most-used characterisation experiment in practice. The chapter's scale-up rules (p.39–40) are its real value: the lab sample must replicate the surface-to-nondrying-surface ratio and the drying geometry of the production unit, or the rate curve will not transfer.
- Link to other chapters: N(X) is the empirical input to Ch.3's simulator and Ch.5's spreadsheet sizing; X* and X_cr are the Ch.1 characteristic-curve anchors.
- Hygiene implication: to characterise a new airlaid or fluff grade, run this exact test on a representative coupon (correct basis weight, correct open area) rather than a loose sample.
### Core concept B — Distributed-parameter coefficient extraction & the receding front (§2.4.3, p.42–45)

- Definition: when you also measure internal T and X profiles (thermocouples in a plane slab), the early transient gives thermal diffusivity k_h from the surface-vs-centre temperature eigenvalue (Eqs 2.12–2.21, first eigenvalue d_1 ≈ 1.35 in the worked chalk example), and the falling-rate weight-loss slope gives mass diffusivity k_m (Eqs 2.22–2.25). For porous solids the dry-layer resistance is captured by Krischer & Kröll's effective diffusivity D_a = D_VG·m (Eq. 2.26) and the receding-front model (Eqs 2.26–2.36).
- Operational? Partly — the math assumes a 1-D homogeneous slab and a constant-thickness two-layer system; the eigenvalue fits (Figs 2.15–2.16 slopes) are exact only for those geometries.
- Link to Ch.4: this is the experimental measurement side of Ch.4's transport-properties theory (diffusivity, permeability).
- Hygiene implication: the double-layer example (p.44–45: sand over gypsum; "seeds coated with an earth layer") is the closest analogue in the chapter to a coated nonwoven or a laminate where a surface layer inhibits drying — a case the chapter says is modelled but does not quantify for mixtures.
## 10. Academic critique & open questions

- Theoretical: The whole distributed-parameter framework is built on 1-D transient diffusion in a homogeneous slab (Lykov-type). It cannot represent the anisotropic, multi-layer, multi-component structures of hygiene products (airlaid web + SAP + adhesive + PE film). The receding-front model is extended only to constant-thickness two-layer slabs (p.44–45), not to swelling/contracting or mixed beds.
- Methodological: The coefficient-extraction relies on eigenvalue fitting from slope measurements (Eqs 2.19–2.25, Figs 2.15–2.16) with no stated uncertainty. For materials whose properties change as they dry (fluff shrinks, SAP swells), the assumed constant k_h, k_m is violated, and the recovered "coefficient" is a moving target.
- Scope: The chapter is silent on real-time / in-line measurement of moisture distribution in moving webs (only lab/off-line and pilot rigs are treated). For a 2000 m/min tissue or a continuous nonwoven line, the relevant question — how to monitor moisture on the machine — is deferred.
- Open questions:

- Q1 — How should the lumped/characteristic-curve experiment be modified for a composite (SAP + fluff) where the two components dry on different branches and at different rates? The chapter's "care must be exercised" for heterogeneous mixtures (p.48) is a warning, not a method.
- Q2 — Can the receding-front effective-diffusivity concept be generalised to a swelling front (SAP gel), where the dry/wet boundary moves but the solid itself expands, breaking the constant-thickness assumption (Eqs 2.33–2.36)?
- Q3 — The chapter gives an empirical rotary-dryer correlation (Eq 2.45, h_V = 2950·n^0.173·G^0.9) but states plant-scale data are "not generally applicable" (p.46); is there a universal volumetric-coefficient correlation for through-circulation of hygiene particulates (fluff, SAP granules) that a procurement engineer could use for first-pass sizing?
## 11. Hygiene-Materials Relevance & Action Cards

For the diaper/wipes R&D engineer and pulp-procurement strategist, Chapter 2 is the measurement and QA playbook: it tells you exactly how to certify residual moisture, how to measure an isotherm for a new absorbent, and how to run the small-scale drying test that de-risks scale-up.

### 11.1 Mapping chapter techniques onto hygiene workflows

|||||
|---|---|---|---|
|Certify fluff/SAP/nonwoven residual moisture (incoming QC)|Direct oven method, 1–2 mm³, 4–5 g, 102–105°C, ±0.05%|p.32|Audit-standard gravimetric moisture; the number that gates every lot.|
|In-line moisture on running web/line|Indirect electrical (dc resistance, dielectric capacitance, ac loss)|p.33|Only feasible method at line speed; cross-check against periodic oven grabs.|
|Water-specific SAP moisture|Karl–Fischer titration / toluene distillation|p.33|Oven methods can degrade crosslinked SAP; Karl–Fischer is water-specific.|
|Set warehouse-stable moisture spec|Sorption isotherm + hysteresis (adsorption branch)|p.33–36|Storage re-adsorption follows the adsorption branch, not the desorption branch the dryer produces.|
|Characterise a new SAP grade / airlaid furnish|Lumped drying-rate experiment (N vs. X)|p.39–40|Feeds Ch.3/5 sizing; must use representative coupon geometry.|
|Diagnose slow falling-rate drying of a core|Receding-front / distributed-parameter analysis|p.42–45|Reveals whether the dry shell is the heat- or vapor-barrier.|
|Through-air nonwoven / fluid-bed SAP drying|Volumetric h_V, K_V (through-circulation)|p.46–48|Bed-scale coefficients when interfacial area is unknown.|

### 11.2 Relevance narrative

The chapter's central claim — parameters cannot be calculated, they must be measured on your actual material (p.31) — is the discipline that prevents the most expensive hygiene-line mistake: specifying a dryer from generic literature values. A new fluff grade, a new SAP, or a new airlaid furnish each needs its own isotherm and rate curve.

Two hygiene-specific cautions the chapter makes explicit:
1. Measure the right hysteresis branch (p.33): the dryer produces the desorption branch; warehouse re-adsorption follows the adsorption branch. Designing the residual-moisture floor from the wrong branch over- or under-sets the spec.
2. Heterogeneous mixtures need care (p.48, alfalfa example): a SAP+fluff core dries as two components at different rates; the chapter offers no quantitative mixture method, so pilot work is mandatory (echoes Ch.1 Q2).

### 11.3 Action cards

ACTION CARD 1 — Residual-moisture certification protocol ★★★★★
Adopt the Ch.2 direct method verbatim for incoming fluff/SAP/nonwoven QC: disintegrate to 1–2 mm³, 4–5 g sample, dry at 102–105°C in a pre-weighed container, report moisture only after two consecutive weighings agree within ±0.05% (p.32). Use Karl–Fischer (not oven) for water-swollen SAP to avoid crosslink degradation (p.33).

ACTION CARD 2 — Isotherm + hysteresis on both branches ★★★★★
For every new absorbent grade, measure the sorption isotherm by the saturated-salt (constant p_v) method (Table 2.3, p.36–37). Measure BOTH adsorption and desorption branches (p.33) and record X_ads and X_des separately; set the warehouse spec from the adsorption branch, the dryer endpoint from the desorption branch.

ACTION CARD 3 — Scale-up-faithful rate test ★★★★☆
Before sizing any new line, run the lumped drying-rate experiment (p.39–40) on a coupon whose thickness and surface-area ratio match production (the chapter's explicit scale-up prerequisite). Extract N_c, X_cr, X* and feed them to Ch.3/Ch.5. Do NOT use a crumpled loose sample.

ACTION CARD 4 — In-line moisture cross-check ★★★★☆
Install dielectric/capacitance moisture sensors (p.33) on the nonwoven/pulp line for real-time control, but validate them weekly against grab-samples measured by the oven/Karl–Fischer reference (p.32–33). Treat sensor readings as relative, the lab method as absolute.

ACTION CARD 5 — Through-circulation coefficient audit ★★★☆☆
For fluid-bed SAP drying or through-air web drying, compute volumetric h_V, K_V from the adiabatic bed balances (Eqs 2.46–2.53, p.48) on pilot data; use these — not plant-scale rotary correlations (Eq 2.45, p.47, flagged "not generally applicable") — for first-pass hygiene-particulate sizing.

## 12. Book-Map Quotes (how Ch.2 seeds the rest of the deliverable)

- Seed → Ch.1 (definitions made measurable): Ch.1 defined X* and the characteristic curve; Ch.2 supplies the measurement ("The moisture content is X = (m_SW − m_S)/m_S", Eq. 2.5, p.40; sorption isotherm via salt solutions, p.36). The Ch.1 abstraction becomes a lab procedure here.
- Seed → Ch.3 (process calculations) & Ch.5 (spreadsheet design): the drying-rate curve N(X) (Eq. 2.6, p.40) and the gas-side coefficients h, K (Eqs 2.7–2.10, p.40) are the exact inputs those chapters' mass/energy balances consume.
- Seed → Ch.4 (transport properties): the distributed-parameter diffusivity extraction (k_h Eqs 2.12–2.21; k_m Eqs 2.22–2.25, p.42–43) and the receding-front effective diffusivity (Eqs 2.26–2.36, p.44–45) are the experimental counterpart to Ch.4's transport theory.
- Seed → Ch.6 (indirect dryers) & bed dryers: the volumetric coefficients h_V, K_V (Eqs 2.37–2.38, p.46) and the through-circulation balances (Eqs 2.46–2.53, p.48) are the design coefficients for fixed/moving/through-flow dryers including conduction/contact types.
- Bridge → Handbook of Nonwovens (sibling): "the drying rates are quite dissimilar for the two components, therefore care must be exercised in drying whole [heterogeneous] plants" (alfalfa example, p.48) maps directly onto drying a nonwoven web that carries both a fibre network and an additive (SAP, binder, lotion) with different drying kinetics.
- Bridge → Handbook of Plastic Films (sibling): the double-layer model (p.44–45: "seeds coated with an earth layer", laminates) is the analytic analogue of a coated/laminated film-web, where a surface layer inhibits drying exactly as the chapter describes.


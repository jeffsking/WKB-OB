---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_8ffb1a9b9bc20ebef6962f3914f35c59001a693ee6c0644e"
source_file: "ID · 深度拆书文摘.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · 深度拆书文摘.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · 深度拆书文摘.md.md

# Handbook_of_Industrial_Drying — 全书 digest（供摘要/核心观点汇编使用）

共 53 章。每章含：标题、概述、观点标题、在书中的作用、卫材行动卡。

======================================================================

## Chapter 1 — Principles, Classification, and Selection of Dryers

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 1 (A.S. Mujumdar) establishes the conceptual and thermodynamic foundation of industrial drying. It frames drying as a thermal separation operation producing a solid by evaporating a volatile (usually water), distinguishing bound vs unbound moisture and two simultaneous subprocesses — external (Process 1: heat/mass transfer at the surface) and internal (Process 2: moisture transport within the solid). The chapter then builds the psychrometric toolkit (vapor–liquid equilibrium, Clausius–Clapeyron, humidity, wet/dry bulb, enthalpy–humidity charts), the internal-state description (moisture content, sorption isotherms, hysteresis, characteristic drying-rate curve), and a classification of dryers by heating method, pressure, and conveying mode. It closes with selection guidelines, energy/safety/environmental constraints, and design methodology. For the hygiene-materials reader the chapter is the reference framework: cylinder/can dryers for paper and pulp, convective hot-air dominance, glass-transition limits for polymers, and GMP/hygienic-design obligations — though most specifics are deferred to later chapters.

### 核心观点标题

Drying is energy-dominant and structurally diverse

Two coupled processes govern every dryer; either can be limiting

Convective hot-air drying dominates industry; indirect is more efficient

Bound vs unbound, and hygroscopic vs nonhygroscopic, define the drying problem

The characteristic drying-rate curve: constant-rate then falling-rate, often the whole job

- 

Dryer selection is a multi-criteria compromise, never a single optimum

### 在书中的作用

Chapter 1 is the foundation / taxonomy chapter. It supplies the vocabulary (bound/unbound, X*, X_cr, f, characteristic curve), the psychrometric engine used in Ch.2–3, and the selection logic that Ch.5 (spreadsheet design) and Ch.6 (indirect dryers) operationalize. It points forward to specialized chapters on superheated steam (Ch.35), novel dryers (Ch.36), scale-up (Genskow), and mathematical modeling (Turner & Mujumdar) — exactly the pipeline the hygiene reader needs (e.g., can-dryer for pulp → Ch. on paper; conduction dryers → Ch.6).

### 卫材行动卡

Relevance rating: ★★★★☆ (foundational; direct only where paper/pulp/polymer drying is named).

ACTION CARD 1 — Fluff-pulp / tissue energy cost

Situation: Specifying or benchmarking a through-/can-dryer for fluff pulp or tissue.

How to apply: Use p.1 energy fact — "Energy consumption in drying ranges from a low value of under 5% for the chemical process industries to 35% for the papermaking operations" — as the anchor for energy-cost/tonne; target convective exhaust enthalpy recovery (p.23 recycle, heat pumps).

Expected effect: Identify that pulp/tissue drying, not converting, is the dominant energy sink; prioritize heat recovery over throughput tweaks.

ACTION CARD 2 — Polymer / SAP heat-sensitivity ceiling

Situation: Drying SAP granules or PP/PE nonwoven webs that must not degrade.

How to apply: Apply p.26 checklist item "Glass transition temperature" and p.21 steam-environment note ("heat sensitivity can be quite different in a steam environment") to set the maximum allowable temperature; prefer indirect/vacuum or short-residence (spray/flash) routes for heat-sensitive solids (p.22).

Expected effect: Avoid yellowing / crosslinking of SAP and melting of thermoplastic fibers by bounding dryer temperature to Tg/Tm window.

ACTION CARD 3 — Residual-moisture spec from sorption isotherm

Situation: Setting a warehouse-stable final moisture for fluff or core.

How to apply: Use X* (equilibrium moisture content, p.12) and the temperature coefficient @X*/@T = −A·X* (p.14) to compute the moisture floor at storage RH/T; avoid overdrying (p.18 "Overdrying should be avoided").

- 

Expected effect: Specify a residual-moisture band that is achievable and non-degrading rather than an arbitrarily low number.

======================================================================

## Chapter 2 — Experimental Techniques in Drying

### 概述

Page numbers derived from PDF-page − 21 (the source's own embedded print p.X markers use this offset; e.g., PDF page 52 → print p.31); this is an estimate and should be spot-checked against the print edition.

Chapter 2 (K. Molnár) is the measurement chapter of the handbook: it catalogues the laboratory and pilot-scale experimental techniques needed to obtain the material and transport parameters that every dryer design calculation consumes — moisture content, sorption-equilibrium isotherms, drying-rate curves, and the heat/mass transfer and diffusivity coefficients of wet and dry solids. It is deliberately a "techniques" chapter rather than a theory chapter: it tells the engineer how to measure what Chapter 1 defined and what Chapters 3–5 will use. The structure moves from equilibrium properties (moisture content of solids and gases; sorption isotherms via saturated-salt and developed-vapor-pressure methods) to kinetics (lumped and distributed-parameter experiments) to bed-level coefficients (fixed/moving and through-circulation dryers). For the hygiene-materials reader this is the QA and characterisation playbook: how to certify fluff/SAP/nonwoven residual moisture, how to measure an isotherm for a new absorbent, and how to run the small-scale drying test that feeds scale-up.

### 核心观点标题

Drying parameters cannot be calculated; they must be measured

The five aims of a drying experiment

Direct moisture determination: oven method with strict protocol

Indirect/online methods for industrial speed

Sorption hysteresis must be measured on the correct branch

- 

Scale-up validity depends on experimental fidelity, not just the math

### 在书中的作用

Chapter 2 is the instrumentation bridge between Chapter 1's definitions (bound/unbound moisture, X*, characteristic curve) and Chapters 3–5's calculations and designs. It is where the abstract symbols of Ch.1 become numbers you can measure. Concretely:

It operationalises X* (Ch.1) via the sorption-isotherm protocols (§2.3) and the adsorption/desorption branch distinction (hysteresis).

It supplies the drying-rate curve N(X) that Ch.1 introduced as the "characteristic curve" (§2.4.2, Figs 2.6–2.9).

It defines the transport coefficients (h, K, k_h, k_m, l_h, l_m) that Ch.3 (process calculations) and Ch.5 (spreadsheet design) will plug into balances.

- 

It introduces volumetric coefficients for beds (§2.5) that Ch.6 (indirect dryers) and any through-circulation/rotary design will use.
It is the chapter a hygiene R&D engineer returns to whenever a new material (new SAP grade, new airlaid furnish) must be characterised before a dryer is specified.

### 卫材行动卡

For the diaper/wipes R&D engineer and pulp-procurement strategist, Chapter 2 is the measurement and QA playbook: it tells you exactly how to certify residual moisture, how to measure an isotherm for a new absorbent, and how to run the small-scale drying test that de-risks scale-up.

### 11.1 Mapping chapter techniques onto hygiene workflows

| Hygiene need | Ch.2 technique | Page | Why it matters |
|---|---|---|---|
| Certify fluff/SAP/nonwoven residual moisture (incoming QC) | Direct oven method, 1–2 mm³, 4–5 g, 102–105°C, ±0.05% | p.32 | Audit-standard gravimetric moisture; the number that gates every lot. |
| In-line moisture on running web/line | Indirect electrical (dc resistance, dielectric capacitance, ac loss) | p.33 | Only feasible method at line speed; cross-check against periodic oven grabs. |
| Water-specific SAP moisture | Karl–Fischer titration / toluene distillation | p.33 | Oven methods can degrade crosslinked SAP; Karl–Fischer is water-specific. |
| Set warehouse-stable moisture spec | Sorption isotherm + hysteresis (adsorption branch) | p.33–36 | Storage re-adsorption follows the adsorption branch, not the desorption branch the dryer produces. |
| Characterise a new SAP grade / airlaid furnish | Lumped drying-rate experiment (N vs. X) | p.39–40 | Feeds Ch.3/5 sizing; must use representative coupon geometry. |
| Diagnose slow falling-rate drying of a core | Receding-front / distributed-parameter analysis | p.42–45 | Reveals whether the dry shell is the heat- or vapor-barrier. |
| Through-air nonwoven / fluid-bed SAP drying | Volumetric h_V, K_V (through-circulation) | p.46–48 | Bed-scale coefficients when interfacial area is unknown. |

### 11.2 Relevance narrative

The chapter's central claim — parameters cannot be calculated, they must be measured on your actual material (p.31) — is the discipline that prevents the most expensive hygiene-line mistake: specifying a dryer from generic literature values. A new fluff grade, a new SAP, or a new airlaid furnish each needs its own isotherm and rate curve.

Two hygiene-specific cautions the chapter makes explicit:

Measure the right hysteresis branch (p.33): the dryer produces the desorption branch; warehouse re-adsorption follows the adsorption branch. Designing the residual-moisture floor from the wrong branch over- or under-sets the spec.

- 

Heterogeneous mixtures need care (p.48, alfalfa example): a SAP+fluff core dries as two components at different rates; the chapter offers no quantitative mixture method, so pilot work is mandatory (echoes Ch.1 Q2).

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

======================================================================

## Chapter 3 — Basic Process Calculations and Simulations in Drying

### 概述

Page numbers derived from PDF-page − 21 (the source's own embedded print p.X markers use this offset; e.g., PDF page 72 → print p.51); this is an estimate and should be spot-checked against the print edition.

Chapter 3 (Z. Pakowski & A.S. Mujumdar) is the computational engineering chapter: it teaches the reader to build a mathematical model of a dryer and solve it. It replaces the older graphical/shortcut culture with a computer-oriented methodology (Excel, Mathcad, MATLAB, Mathematica) while insisting the computer "will not relieve one from thinking" (p.52). The chapter is structured as a modeling cookbook: (1) classify the process into one of 16 generic dryer cases by operation type, flow geometry, and flow pattern; (2) assemble the five parts of a deterministic model — balance equations, constitutive (kinetic) equations, equilibrium relations, property equations, geometric relations; (3) solve steady-state input–output or distributed-parameter (DPM) models for cocurrent/countercurrent/cross-flow, including the solid phase with and without shrinkage; (4) apply shortcut methods and software tools. For the hygiene-materials reader this is the chapter that turns Ch.1's definitions and Ch.2's measured coefficients into an actual dryer-size and drying-time calculation — the quantitative core of any new line specification.

### 核心观点标题

Drying calculation has migrated to the computer, but judgment remains

Three reasons you calculate: design, simulation, optimization

Every model is built from the master balance: Inputs − Outputs = Accumulation

Lumped vs. distributed: geometry dictates the math

Kinetics enter through the characteristic drying curve or a thin-layer equation

- 

Psychrometric arithmetic underpins every model

### 在书中的作用

Chapter 3 is the quantitative engine of the handbook. It converts Ch.1's vocabulary (X*, X_cr, characteristic curve, bound/unbound moisture) and Ch.2's measured coefficients (h, K, k_m, isotherms) into solvable models, and it supplies the balance/psychrometric subroutines that Ch.5 (spreadsheet-aided design) automates and that Ch.6 (indirect dryers) specialises to conduction heating. It is the chapter a hygiene engineer uses to answer "what size dryer do I need and how long will it take?" for a fluff line, a SAP fluid bed, or a nonwoven through-air oven.

### 卫材行动卡

Chapter 3 is the sizing-and-simulation chapter: it is where the hygiene engineer computes dryer size, residence time, and energy from Ch.1 definitions and Ch.2 coefficients. Every hygiene drying operation — fluff-pulp oven, SAP fluid bed, nonwoven through-air oven, wipes tunnel dryer — is one of the 16 generic cases and can be built from the balances here.

### 11.1 Mapping chapter constructs onto hygiene workflows

| Hygiene task | Ch.3 construct | Page | Why it matters |
|---|---|---|---|
| Size a new fluff/SAP/nonwoven line | 16-case classification → model template | p.53–54 | Picks LPM vs. DPM and cocurrent/countercurrent before any equation |
| Predict drying time of a batch | LPM balances + kinetic closure (Eqs 3.113–3.120) | p.70 | Batch oven/fluid-bed time from measured coefficients |
| Simulate continuous through-air web | Steady-state DPM cocurrent/cross-flow (§3.6.2) | p.63–65 | Web on cylinder/through-air oven = continuous DPM |
| Fit a rate law to Ch.2 data | Lewis (3.32) / Page (3.36) / CDC (3.29–3.30) | p.56–57 | Empirical kinetics for spreadsheet scale-up |
| Compute humid-gas state | Psychrometric core (Eqs 3.45–3.53) | p.58–59 | Shared routine for every balance; code once in Excel |
| Set equilibrium moisture in model | GAB isotherm (Eq. 3.56) | p.60 | X*(a_w) for fluff/SAP from measured isotherm |
| Model web contraction during drying | Shrinkage DPM (Fig. 3.15, p.69) | p.69 | Nonwoven/film webs shrink; restrained vs. unrestrained matters |
| Quick first-pass size | Shortcut free/bound-moisture split (§3.10.1) | p.76 | Order-of-magnitude size before full model |

### 11.2 Relevance narrative

The chapter's two durable lessons for hygiene R&D: (1) classify before you calculate — the 16-case grid (p.54) prevents the classic error of applying a perfectly-mixed LPM to a deep, non-uniform bed; (2) the material properties are the bottleneck — the conclusion (p.77–78) is explicit that "very little has been done in the area of materials databases" and missing data force experimental determination (i.e., back to Ch.2). For a diaper-core material stream, this means maintaining an internal property library (isotherm, CDC/Page coefficients, shrinkage factor) per grade.

A caution: the psychrometric shortcuts are air–water only. Any solvent-borne lotion or adhesive on a wipe/web requires the general wet-bulb relation (p.59), not Eq. 3.50.

### 11.3 Action cards

ACTION CARD 1 — Classify-then-model gate ★★★★★
For every new hygiene dryer, first place it in the 16-case grid (p.53–54): operation type × flow geometry × flow pattern. Document the choice (e.g., "continuous, cocurrent, plug/mixed → DPM") before writing balances. Reject any vendor size that does not state its assumed case.

ACTION CARD 2 — Internal property library per grade ★★★★★
Maintain a spreadsheet row per material grade with: GAB coefficients (Eq. 3.56), Page parameters k, n (Eq. 3.36), X*, X_cr, shrinkage factor (Fig. 3.15). These are the inputs the §3.6–3.8 models consume; the conclusion (p.77–78) confirms you cannot borrow them from literature. Source them from Ch.2 tests.

ACTION CARD 3 — Build the psychrometric routine once ★★★★☆
Code Eqs 3.45–3.53 (RH, Y, enthalpy, dew point, AST, WBT, Lewis number) as a reusable Excel/Matlab function. Use it in every dryer model. For any solvent (alcohol/acetone) drying, use the general WBT equation (Eq. 3.52), NOT the air–water simplification (Eq. 3.50).

ACTION CARD 4 — Batch-time from LPM + Page fit ★★★★☆
For a batch fluff/SAP oven or fluid bed, fit a Page equation (Eq. 3.36) to the Ch.2 rate test, then solve the LPM balances (Eqs 3.113–3.120 for oven, 3.121–3.127 for fluid bed) to get drying time vs. throughput. Validate against one pilot run before production scale-up.

ACTION CARD 5 — Account for web shrinkage ★★★☆☆
If the nonwoven/film web shrinks during drying, do not use a rigid-geometry DPM. Adopt the shrinkage mesh logic (Fig. 3.15, p.69): choose restrained vs. unrestrained and couple the moving boundary to the mass/heat balances; otherwise predicted residence time and moisture profile will be wrong.

======================================================================

## Analysis of Chapter 4 — Transport Properties in the Drying of Solids

### 概述

Chapter 4 sits at the property layer of the drying knowledge stack. Whereas Ch.1 (classification/selection), Ch.2 (experimental techniques for moisture/isotherms), and Ch.3 (process calculations/simulation) frame the problem, Ch.4 supplies the five transport/thermodynamic properties that every drying model must contain as parameters:

Effective moisture diffusivity, D (internal mass transfer)

Effective thermal conductivity, k (internal heat transfer)

Air-boundary heat-transfer coefficient, *h*ₕ (external heat transfer)

Air-boundary mass-transfer coefficient, *h*ₘ (external mass transfer)

Drying constant, K (a lumped, thin-layer proxy)

- 

Equilibrium material moisture content, *X*ₑ (drives the mass-transfer potential)

The chapter is organized strictly per-property: Definition → Experimental method → Data compilation → Factors affecting → Theoretical estimation. This is the single most data-dense chapter in the assignment — it carries 18 tables and ~24 figures, with large literature compilations (Tables 4.2, 4.6, 4.13, 4.15–4.18). For the hygiene reader the chapter is decisive because four of the six properties are measured almost entirely on polymer systems (Crank & Park Diffusion in Polymers, Frisch & Stern Diffusion of small molecules in polymers) and the data tables explicitly list cellulose acetate, polyvinyl alcohol, polyolefins, Avicel (microcrystalline cellulose), and starch gels — i.e. the exact chemistries of fluff pulp, nonwoven webs, SAP carriers, and tissue.

Print-page span: p.79–p.113 (PDF p.100–134).

---

### 在书中的作用

Ch.4 is the parameter dictionary of the handbook. Ch.1 tells you which dryer; Ch.2 gives you how to measure moisture/isotherms; Ch.3 gives you mass/energy balances and simulators; Ch.4 gives you the coefficients those balances and simulators consume. Ch.5 (spreadsheet design) and Ch.6 (indirect dryers) then use Ch.4's h, hₘ, k, D, Xₑ. For hygiene R&D, Ch.4 is the bridge from "we dried a sample" to "we can simulate/scale a nonwoven through-dryer or an SAP contact dryer."

---

### 卫材行动卡

H11.1 — Characterize fluff-pulp D before scaling a through-dryer. Fluff is "Other materials / cellulose" class; expect D ~10⁻¹²–10⁻⁹ m²/s (cf. cellulose acetate 2E-12, Avicel 5E-9). Action: run §4.7 regression rig on your specific pulp grade at 3–5 m/s, 60–120°C; do not borrow literature D.

H11.2 — Expect SAP to show anomalous (non-Fickian) drying. Polyacrylate chemistry ⇒ D may decrease as the gel hydrates (p.85). Action: model the falling-rate period with a swelling-controlled (Case-II) kernel, not pure Fick 4.1; use desorption isotherm branch.

H11.3 — Nonwoven PP/PE webs ≈ Type III isotherms, low *X*ₑ. Action: anticipate very low equilibrium moisture; on a cylinder/can dryer the web dries in <1 s (tissue analogy, Ch.3) and external *h*ₘ controls (Bi<0.1). Size the dryer from *h*ₘ via Lewis (4.13) + Table 4.9, not from *D*.

**H11.4 — Use Biot threshold to choose your design lever.** *Action:* compute Biₕ,Biₘ for your web; if >1 tune material (basis weight, porosity ε/τ² via Eq 4.3); if <0.1 tune air (velocity, temperature via Table 4.9/Fig 4.8–4.9).

H11.5 — Build the GAB isotherm for your core composite. Action: measure desorption isotherm (gravimetric, p.101–102) for fluff+SAP blend; fit GAB (Table 4.13) to get *X*ₑ(a_w,T); feed *X*ₑ into the dryer mass-balance (Ch.3) and the §4.7 model.

H11.6 — First-cut dryer sizing with thin-layer K. Action: run one constant-T constant-RH thin-layer drying of your web; fit Eq 4.14 → K; convert to D via Eq 4.15 if slab thickness known; iterate in Ch.5 spreadsheet.

H11.7 — Glass-transition discipline for polymer solids. SAP/nonwoven binders have a Tg; keep dryer temp below Tg-driven casehardening window (see POP). Action: set exhaust/dwell so the polymer does not approach its rubbery state mid-drying.

---

======================================================================

## Analysis of Chapter 5 — Spreadsheet-Aided Dryer Design

### 概述

Chapter 5 is the how-to-implement chapter: it converts the physical models of Ch.1–Ch.4 into a working Microsoft Excel + VBA simulator. Its thesis is that spreadsheet software is now an "indispensable tool for engineers" (p.119) and that Excel with Visual Basic for Applications (VBA) "is an effective tool for process design" because "Spreadsheets offer sufficient process model 'hospitality'" (p.119–120) — i.e. they connect models, charts, Solver optimization, and databases into one environment.

The chapter has two parts:

§5.2 Principles and Techniques — a six-step recipe (workbook → model → Solver → charts → dialog boxes → integrated GUI) and the foundational concepts of modeling / simulation / design, plus a degrees-of-freedom analysis (M variables, N equations, F = M−N, D = F−K) that frames every dryer problem.

- 

§5.3–§5.4 A worked conveyor belt dryer — a complete 37-variable / 24-equation model (Table 5.10, Eqs T10.1–T10.24) covering psychrometrics, drying kinetics, mass/energy balances, belt and fan sizing, performance indices, and an annualized-cost (TAC) objective, fully implemented in Excel (Figures 5.5–5.10).

For the hygiene reader this is the directly actionable deliverable: a conveyor/through-belt dryer is exactly the class of equipment used to dry fluff-pulp mats, nonwoven webs, and diaper core composites. The supplied spreadsheet skeleton can be re-pointed at your own material's psychrometric, isotherm, and kinetic parameters (the very properties Ch.4 says you must measure).

Print-page span: p.119–p.134 (PDF p.140–155).

---

### 在书中的作用

Ch.5 is the implementation bridge between theory (Ch.1–4) and the dryer-type catalog (Part II, starting p.134). Ch.1–4 give you definitions, properties, and balances; Ch.5 gives you a working calculator; Ch.6+ describe individual dryer classes you can then model in that calculator. It is the only chapter that is explicitly software-oriented, and it is the most directly reusable artifact in the assignment for a hygiene process engineer.

---

### 卫材行动卡

H11.1 — Build the Ch.5 belt-dryer spreadsheet as your first fluff/SAP dryer sizer. Action: create BeltDryer.xls per §5.2 Steps 1–3; replace the Technical Data block with your measured Oswin/GAB constants (Ch.4 §4.6) and kinetic constants (Ch.4 §4.5 K or t_c).

H11.2 — Use DOF analysis before modeling any nonwoven dryer. Action: list M variables / N equations for your through-circulation or conveyor line; confirm D = F − K ≤ number of knobs you actually control (air T, humidity, velocity, belt geometry). Avoid over-specifying.

H11.3 — Retarget T10.3 to your own isotherm. Action: substitute GAB parameters (Ch.4 Table 4.13/4.14 style) for the Oswin b₁,b₂,b₃; keep the rest of the chain intact. This makes Xₑ physically correct for cellulose (Type II) vs PP/PE (Type III).

H11.4 — Feed Ch.4's drying constant into T10.5. Action: set t_c = 1/K from your thin-layer run (Ch.4 Eq 4.14/4.15); the spreadsheet then predicts residence time and belt length for your web basis weight.

H11.5 — Optimize TAC, not just physics. Action: encode utility costs (C_e, C_s) and equipment costs (C_bel, C_exc, C_fan) for your region; let Solver minimize TAC over {Y,T,V,D}. Compare conveyor vs fluidized vs contact (Ch.6) on equal TAC footing.

H11.6 — Modernize the VBA. Action: replace DialogSheets (Table 5.9) with UserForm; keep the sync logic (edit box ↔ named cell). Otherwise the GUI steps (5–6) will not run in current Excel.

H11.7 — Add uncertainty after first build. Action: once deterministic TAC works, wrap the Technical Data inputs in a one-way/two-way table (Fig 5.7/5.8) to see TAC sensitivity to your measured D, Xₑ, t_c — the properties Ch.4 flags as uncertain.

---

======================================================================

## Analysis of Chapter 6 — Indirect Dryers

### 概述

Chapter 6 covers indirect (contact / conductive) dryers — equipment where the heating medium (steam, hot oil, molten salt, electricity) never touches the product; heat reaches the wet solids by conduction through a heated wall (p.135). This is the dryer class most relevant when (a) the product must stay hygienic/closed-system, (b) the material is heat-sensitive or solvent-wet, (c) emissions/fines must be near zero, or (d) you want the highest thermal efficiency. The chapter gives: definition + advantages/limitations (§6.1), selection tables by feedstock and duty (§6.2, Tables 6.1–6.3), a tour of five dryer families (§6.3: tray, steam-tube rotary, rotating-batch-vacuum, agitated, other), and a quantitative design/modeling section (§6.4, Eqs 6.1–6.37) built on the overall heat-transfer coefficient U and its five resistances.

For the hygiene reader this chapter is decisive: contact dryers are exactly how SAP granules, polymer flakes, and heat-sensitive nonwoven binders are dried in a closed, low-oxygen, low-emission environment — and the chapter contains the single most important polymer-science warning in the assignment (p.142: glass transition of the solid during contact drying).

Print-page span: p.135–p.148 (PDF p.156–169).

---

### 在书中的作用

Ch.6 opens Part II ("Description of Various Dryer Types", p.134) and is the first detailed dryer family chapter. It operationalizes Ch.4's k, h and Biot rules (conduction-controlled, Bi>1) and Ch.3's balances, and it is the dryer class most amenable to the Ch.5 spreadsheet (conduction instead of convection). For hygiene, it precedes the convective/through-circulation families the reader will more often use for webs, but it is the right tool for SAP granule drying, polymer flake/sludge drying, and any heat-sensitive binder.

---

### 卫材行动卡

H11.1 — Use contact drying for SAP granules in inert/N₂ atmosphere. Action: SAP is heat-sensitive + dust-prone + benefits from closed, low-O₂, fume-recoverable drying (p.135–136). Select steam-tube rotary or agitated paddle; keep wall T below SAP's Tg to avoid sticking.

H11.2 — Honor the glass-transition warning (p.142). Action: measure/look up Tg of your SAP and PP/PE binder; set heated-wall temperature a safe margin below Tg; expect U to collapse if exceeded (fouling 5–10 W/(m²K), p.141). This is the single most common contact-dryer failure for polymers.

H11.3 — Size from the rate integral with your own U. Action: run a small heated-plate device (Lecomte et al., p.145) on your SAP/flake to get h_f; compute I = ∫dX/m˙(X); batch area A·t = M_dry·I (6.36) or continuous A = M˙_dry·I (6.37). Do not take U from the food/sludge tables blindly.

H11.4 — Feed GAB isotherm derivative into Eq 6.32. Action: differentiate your Ch.4 §4.6 GAB (or Ch.5 T10.3 Oswin) isotherm w.r.t. T to get (∂X_h/∂T)_p; plug into the hygroscopic effective heat capacity so the contact-drying rate of moisture-binding SAP is correct.

H11.5 — Exploit the 30% energy advantage for capex decisions. Action: compare contact (2800–3600 kJ/kg) vs convective (4000–6000) on opex; if energy and emissions dominate, accept higher heat-exchange capex (p.136) for a closed SAP/ binder dryer.

H11.6 — Match dryer to rate period (p.147). Action: SAP is falling-rate/internally-controlled ⇒ choose a contact dryer allowing long residence, low wall T (rotating vacuum, gentle paddle), not a large-area constant-rate machine.

H11.7 — Use vacuum for heat/solvent-sensitive webs. Action: tray or double-cone vacuum (U≈35, p.141) for nonwoven binder pre-drying or solvent-wet polymer flake; recover solvent via condenser (p.139). Watch fouling if the polymer approaches Tg mid-cycle.

---

======================================================================

## Chapter 7 — Rotary Drying

### 概述

Chapter 7 (Krokida, Marinos-Kouris & Mujumdar) is the mechanical-conveyance and design chapter of the Handbook's dryer catalogue. It treats the rotary dryer as a cylindrical, slightly inclined, slowly rotating shell that advances wet granular solids by rotation, slope and head effect while hot gas passes (cocurrent or countercurrent) to evaporate surface and bound moisture. The chapter's argument runs through five layers: (i) classification by heat-transfer mode (direct, indirect–direct, indirect, special types such as the Roto-Louvre); (ii) flight design as the device that lifts and showers the solids through the gas curtain; (iii) residence-time models built from the three particle motions — cascade, kiln action, bouncing; (iv) heat- and mass-transfer correlations, dominated by the volumetric coefficient Uₐ and the Chilton–Colburn analogy; and (v) a full mathematical design model with burner, dryer, kinetics, residence time and geometrical constraints, closed by two worked case studies (olive cake, catalyst pellets). For the hygiene reader the chapter is a capability reference: it defines the dryer class that post-dries free-flowing granular polymer products — SAP granules, cellulose-acetate flake, PP/polyolefin pellets, vinyl resins — and it supplies the residence-time and thermal-efficiency equations needed to size and cost such a unit. Direct, gentle, through-gas rotary drying is precisely the regime for heat-sensitive, free-flowing absorbent-material feeds.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

---

### 核心观点标题

Cocurrent flow protects heat-sensitive solids.

The classification rests on where the heating medium contacts the solids.

Polymer and granular chemicals are canonical rotary-dryer feeds.

Flights exist to lift and shower the solids; under/over-loading ruins performance.

Optimal drum loading is 10–15% of volume.

Residence time is holdup ÷ feed rate, and plug flow cannot be assumed.

Heat transfer is expressed by a volumetric coefficient Uₐ with strong scatter.

The Chilton–Colburn analogy ties heat and mass transfer in one factor.

- 

A complete design model minimises unit cost over five free variables.

### 在书中的作用

Chapter 7 is the first of the unit-operation-specific chapters (rotary, fluid bed, drum, spray, freeze, microwave) that operationalise the property layer of Ch.4 and the selection layer of Ch.1. It is the mechanical counterpart to Ch.8 (fluidized bed, also a convective granular dryer) and Ch.9 (drum, a conductive/contact alternative). For hygiene R&D it defines the convective post-drying option for granular SAP, cellulose-acetate, and pelletised polymer products.

---

### 卫材行动卡

Relevance to diaper/wipe/absorbent-core R&D: ★★★☆☆ (rotary drying is a post-treatment option for granular SAP and polymer flake, not for webs/fluff mats).

ACTION CARD H11.1 — Specify cocurrent flow for SAP/cellulose-acetate post-drying. Situation: drying heat-sensitive free-flowing SAP granules or cellulose-acetate flake. Apply: set cocurrent gas/solid flow so the high inlet temperature (up to 800–1100 K for fired burners, p.161) is quenched at first evaporation (p.149). Effect: avoids thermal degradation / crosslink scission of the polyacrylate network.

ACTION CARD H11.2 — Hold 10–15% drum fill, size flights to free-flowing feed. Situation: designing or auditing a rotary SAP post-dryer. Apply: 90° lip radial flights (free-flowing, p.152); verify holdup H/V ∈ [5,15]% (constraint p.165); L/D in [4,10]. Effect: maximises cascading contact, prevents bypass by kiln action and loss of hot-gas contact (p.153).

ACTION CARD H11.3 — Close the moisture tail, not the mean. Situation: setting the residence-time spec. Apply: compute tₜ = H/F (Eq 7.61) but qualify against the "maximum moisture of any particle" criterion (p.155); do not assume plug flow. Effect: guarantees no under-dried SAP granule reaches the packaging spec.

ACTION CARD H11.4 — Budget thermal efficiency 55–75% (fired) / 30–55% (steam). Situation: capex/opex estimate for a SAP post-dryer. Apply: use p.162 ranges; steam-heated air halves efficiency. Effect: realistic energy-cost-per-tonne for the absorbent-core line.

---

======================================================================

## Chapter 8 — Fluidized Bed Dryers

### 概述

Chapter 8 (Law & Mujumdar) is the particulate-solids convective chapter and, for the hygiene reader, the single most process-relevant unit in the assignment: it is the drying/agglomeration/granulation technology that post-treats free-flowing superabsorbent polymer granules. The chapter opens with the fluidization principle (minimum fluidization velocity u_mf, dense phase + freeboard, elutriation, Geldart powder classes A/B/C/D), then states advantages/limitations (high heat/mass transfer, low maintenance, but attrition and fines entrainment), then quantifies heat transfer (single-particle h_p 1–700 W/(m²K) yet system rates enormous due to 3,000–45,000 m²/m³ interfacial area), then builds five drying model families (diffusion, empirical, kinetic, single-phase, two-phase), then examines operating parameters, then surveys ~15 dryer variants (batch, well-mixed, plug-flow, multistage, hybrid, pulsating, immersed-tube, vibrated, agitated, inert-solids, spouted, recirculating, jetting, baffled, superheated-steam, fluidized-bed freeze, heat-pump), then closes with a design procedure and a worked sample. Two statements make the chapter decisive for SAP: (i) "spray drying alone is not energy efficient to remove all … internal moisture. Fluidized bed drying can be incorporated as the second-stage drying" (p.175) — exactly the industrial SAP route — and (ii) superheated-steam FBD is reported for "paper and pulp" (p.189), i.e. fluff-pulp drying.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

---

### 核心观点标题

Fluidized beds process polymers, resins and healthcare products.

Wet feed fluidizes poorly; only the top layer lifts initially.

Enormous interfacial area gives near-isothermal, very fast heat transfer.

Spray dryer + fluid bed is the energy-optimal two-stage route for internal moisture.

FBD simultaneously granulates, agglomerates and coats.

Geldart classification governs which variant you need.

Ion-exchange resin is the analogue material named in the chapter.

Multistage spray-fluidized bed = the SAP reactor.

Vibrated FBD extends to fragile, heat-sensitive, attrition-prone solids.

- 

Superheated-steam FBD is used for paper and pulp.

### 在书中的作用

Chapter 8 is the granular-counterpart to Ch.7 (rotary) and the convective sibling of Ch.9 (drum, conductive). It is the technology chapter most aligned with Ch.10 (spray drying) via the two-stage route, and with Ch.12 (dielectric) via the noted "microwave energy field … in a fluidized or spouted bed" future direction (p.197). For hygiene R&D it is the operative chapter for SAP granule post-treatment, agglomeration, and coating.

---

### 卫材行动卡

Relevance to diaper/wipe/absorbent-core R&D: ★★★★★ (fluid-bed post-treatment, agglomeration and coating of SAP granules; superheated-steam pulp drying).

ACTION CARD H11.1 — Adopt the two-stage spray→fluid-bed SAP route. Situation: building or auditing an SAP line. Apply: spray-dry to form granules, then fluid-bed for internal moisture (p.175, p.184); add a third fluid-bed cooling stage to prevent package condensation (p.175). Effect: removes bound moisture far more cheaply than prolonging the spray; yields a free-flowing, low-dust granule.

ACTION CARD H11.2 — Choose variant by Geldart cut. Situation: a SAP product has a cohesive fine fraction (Group C) and a denser granule (Group A/B/D). Apply: use vibrated or agitated FBD for the fine/cohesive cut (p.185, p.187); baffled or spouted FBD for the large/dense cut (p.189). Effect: avoids channeling, reduces fines entrainment and attrition dust.

ACTION CARD H11.3 — Exploit in-bed coating/agglomeration. Situation: adding anti-caking, skin-friendly or fragrance layer to SAP. Apply: spray binder/active onto the fluidized bed in the same unit as post-drying (p.175). Effect: one unit performs dry + agglomerate + coat, cutting capex and handling.

ACTION CARD H11.4 — Pre-dry wet feed or vibrate. Situation: moist SAP feed fluidizes poorly (only top layer lifts, p.173). Apply: flash/cyclone pre-remove surface moisture then fluid-bed (p.184), or use vibrated FBD (p.185). Effect: stable fluidization, no stationary wet heel, uniform drying.

ACTION CARD H11.5 — Use superheated-steam FBD for fluff pulp. Situation: drying fluff/cellulosic pulp. Apply: superheated-steam FBD — reported for paper and pulp, no oxidative damage (p.189). Effect: no fire/explosion hazard, pasteurizable, better pulp brightness retention.

---

======================================================================

## Chapter 9 — Drum Dryers

### 概述

Chapter 9 (Wan Ramli Wan Daud) covers the conductive/contact drum dryer — a steam-heated rotating cylinder (or pair) that spreads a viscous liquid, slurry or paste into a thin adherent sheet and evaporates moisture by the intense heat flux of condensing steam inside the drum. The chapter's logic: (i) classify by drum count/config (atmospheric double/single/twin, enclosed, vacuum double); (ii) state operating variables (steam 2–7 bar, speed 2–30 rpm, nip 0.05–0.5 mm); (iii) describe feeding/spreading (nip, roller, dip, spray/splash) and the rheology of the boiling pool; (iv) analyse the four drying zones on the drum (initial application, initial sheet, slow drying, vacuum) with heat-flux and heat-transfer-coefficient data; (v) cover product handling, control, and the product list. For the hygiene reader the chapter is relevant through three polymer-science hooks: drum dryers explicitly dry polyacrylamides (p.209) — a water-absorbing polymer cousin of SAP; they gelatinize starch slurries into shear-thinning power-law pastes that swell several-fold (p.206–207) — an aqueous-polymer-gel process; and they expose the glass-transition behaviour of sugar sheets (p.210). The drum dryer is the conductive sibling of the rotary (Ch.7) and fluid-bed (Ch.8) chapters and a candidate for drying heat-sensitive polymer hydrogels under vacuum.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

---

### 核心观点标题

Drum dryers process viscous liquids/slurries/pastes by conductive heat.

High heat flux + short time yields a porous, rapidly-rehydrating sheet.

Predictive modelling fails; pilot testing is mandatory.

Starch gelatinization makes a swelling, shear-thinning polymer gel.

Heat flux is enormous at the application zone.

Polyacrylamides are a named drum-dried polymer.

Vacuum drum dryer spares heat-sensitive structure.

- 

Sugar sheets expose a glass-transition sticky failure.

### 在书中的作用

Chapter 9 is the conductive/contact member of the dryer catalogue, complementing Ch.7 (convective rotary), Ch.8 (convective fluidized bed), Ch.10 (convective spray), Ch.11 (sublimation freeze), Ch.12 (dielectric). It is the only chapter treating thin-film boiling of viscous/pasty feeds, which is the regime for polymer gels and starches — linking to Ch.4's conductive (Biot>1) drying and to the polymer-science layer in the POP block.

---

### 卫材行动卡

Relevance to diaper/wipe/absorbent-core R&D: ★★★★☆ (drum drying of aqueous polymer gels — polyacrylamide, starch gelatinization; vacuum for heat-sensitive hydrogels; Tg-stick lesson for polymer films/webs).

ACTION CARD H11.1 — Pilot-test any polymer gel before scaling. Situation: drum-drying a SAP/polyacrylamide/starch gel. Apply: run the mandated pilot-drum performance test (p.205); set steam 2–7 bar, speed 2–30 rpm, nip 0.05–0.5 mm; verify sheet forms. Effect: avoids the "sheet may not form well" failure at high feed concentration (p.204).

ACTION CARD H11.2 — Exploit vapor-bubble porosity for instant-rehydration flakes. Situation: making a porous superabsorbent/hydrocolloid flake. Apply: use the high-flux short-time boiling regime (p.202, ≤85 kW/m²) to generate internal vapor bubbles → porous sheet. Effect: porous product wets/rehydrates fast — valuable for instant hygiene or absorbent composites.

ACTION CARD H11.3 — Use vacuum drum for labile hydrogels. Situation: drying a heat-/oxygen-sensitive polymer gel (enzyme-SAP, bioactive coating). Apply: vacuum double drum (p.208–209) to retain structure/functionality. Effect: less thermal/oxidative damage than atmospheric drum.

ACTION CARD H11.4 — Stay below the glass-transition stick point. Situation: drying a polymer sheet/film (SAP binder, nonwoven coating) on a hot surface. Apply: control drum speed / cool-air at the blade (p.210) so the sheet does not cross into the rubbery/molten Tg regime before takeoff. Effect: prevents sticking, "sticks", and wrinkles — the same defect class that ruins polymer webs in through-dryers.

---

======================================================================

## Chapter 10 — Industrial Spray Drying Systems

### 概述

Chapter 10 is the handbook's treatment of industrial spray drying — the unit operation in which a pumpable liquid or slurry feed is atomized into droplets and dried to individual particles in a hot gas stream, producing powders, granules, or agglomerates in a single pass. The chapter is authored by Filkova, Huang, and Mujumdar and is the most application- and equipment-breadth-rich chapter in this assignment: it opens with the principles (atomization hardware — rotary wheel, pressure, pneumatic, and novel nozzles; drop-size distributions and the Sauter mean D₃,₂; chamber shape and air–droplet contact modes; ancillary heaters/fans/cyclones; thermal efficiency), then surveys complete system layouts (open, closed, semiclosed/self-inertizing, and spray-plus-fluidizer combinations; single-, two-, and three-stage), then covers energy, safety, control, and selection, and closes with design procedures and CFD, plus a forward-looking §10.5 (superheated steam, horizontal two-stage, low-humidity/LDP, spray freeze drying, encapsulation, energy-efficiency). For the hygiene reader this is the SAP-isolation and binder-fines chapter: the text explicitly lists PVC emulsions and rubber latex among spray-dried products, and the two-stage spray + fluid-bed route and the encapsulation route are both directly usable for superabsorbent and wipe-active delivery. It is the upstream counterpart to Ch.8 (fluid-bed post-treatment) and the convective sibling to Ch.11/Ch.12.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

---

### 核心观点标题

Spray drying converts liquid polymer feeds into powders in one pass.

Polymer/surfactant products are explicitly within scope.

The Sauter mean diameter governs powder morphology.

The two-stage spray + fluid-bed is the agglomeration route.

Superheated-steam spray drying eliminates fire/oxidation.

- 

Encapsulation delivers actives via an oil-in-water emulsion.

### 在书中的作用

Ch.10 is the liquid-feed counterpart to Ch.7 (rotary, granular), Ch.8 (fluid-bed, granular/post-treatment), Ch.11 (freeze, heat-sensitive biochemicals), and Ch.12 (dielectric, thick/absorbent cores). It is the upstream isolation step for SAP and binder latex that Ch.8 then agglomerates; its two-stage spray + fluidizer line (p.239) is the literal bridge to Ch.8. For hygiene, Ch.10 supplies the "make the powder" half of the SAP route and the encapsulation route for wipe actives; Ch.4 (thermodynamics/isotherms) and Ch.3 (diffusivity) feed its modeling.

---

### 卫材行动卡

Relevance rating: ★★★★★ — this is the SAP-isolation, binder-latex, and active-encapsulation chapter.

H11.1 — Isolate emulsion-polymerized SAP/latex by spray drying. Situation: converting a sodium-polyacrylate or SBR/acrylic latex into a free-flowing powder. Apply: per p.214, PVC-emulsion and rubber-latex are standard spray-dried products; choose pressure/rotary atomizer and set D₃,₂ (p.217) for target fine size; watch wall-impingement/melting rule (p.224). Effect: one-pass powder, no milling; primary fines then agglomerated in Ch.8 fluid bed. ★★★★★

H11.2 — Route SAP fines through the two-stage spray + fluidizer. Situation: need agglomerated, dust-free SAP granules. Apply: per p.239, deposit semi-dried spray powder onto a belt into a fluid bed for second-stage drying/agglomeration. Effect: "instant"-type agglomerates with controlled porosity — the diaper-core granule. ★★★★★

H11.3 — Encapsulate wipe/sanitary actives. Situation: deliver fragrance, skin-care, or antimicrobial actives with controlled release. Apply: per p.253, disperse active in oil, emulsify in hydrocolloid (modified starch/gum arabic) oil-in-water, spray dry; release triggered by T/RH/pressure. Effect: stable, trigger-released actives in wipe or topsheet. ★★★★

H11.4 — Use superheated-steam / LDP for oxidation-sensitive carriers. Situation: drying cellulose-pulp fines, starch, or heat-sensitive SAP grade. Apply: per p.247 / p.249, steam medium removes oxidative damage; LDP allows 80°C drying at very low humidity. Effect: no yellowing, lower thermal load on fragile polymers. ★★★★

H11.5 — Close the cycle for solvent-based polymer solutions. Situation: spray-drying a non-aqueous polymer dope (explosion/solvent-recovery risk). Apply: per p.234, use closed cycle with inert gas for evaporation/recovery, or semiclosed self-inertizing for explosive powders. Effect: safe, emissions-controlled isolation of solvent-borne SAP/precursor. ★★★★

---

======================================================================

## Chapter 11 — Freeze Drying

### 概述

Chapter 11 is the handbook's treatment of freeze drying (lyophilization) — vacuum sublimation of a frozen solvent (usually water) from a heat-sensitive material, executed in three stages: freezing, primary drying (sublimation of the frozen solvent), and secondary drying (desorption of bound/sorbed water). Authored by Liapis and Bruttini, it is the most physics- and process-modeling-heavy chapter in this assignment: it builds a full moving-boundary PDE system (Eq 11.2–11.51) for heat and mass transfer through the dried and frozen layers, treats chamber-pressure effects on effective thermal conductivity and pore diffusivity, devotes a long §11.7 to optimal-control policies (cyclic vs constant pressure), and closes with a cost and conclusion section. For the hygiene reader this is the lowest-relevance chapter in the batch: freeze drying is explicitly positioned as a premium route for biologicals, pharmaceuticals, and delicate foods, not for bulk hygiene commodities. The chapter states plainly that freeze drying is "an expensive form of dehydration" (p.255) and that "most food products are still dried by conventional means for obvious economic reasons" (p.280). Its only process echoes of hygiene interest are (a) the brief, failed microwave freeze-drying subsection (§11.3), which is abandoned as impractical, and (b) porous-powder formation — both picked up elsewhere (Ch.10 spray freeze drying; Ch.12 dielectric). It is the heat-sensitive, low-throughput sibling to Ch.7–Ch.10 and the conceptual counterpoint to Ch.12's dielectric heating.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

---

### 核心观点标题

Freeze drying is for heat-labile, high-value materials.

Freeze drying is intrinsically expensive and slow.

Pore structure from freezing dictates drying rate and quality.

Microwave freeze drying failed industrially and is deferred.

Runaway overheating: water out-dissipates ice under microwaves.

- 

Economics restrict freeze drying to high-value products.

### 在书中的作用

Ch.11 is the heat-sensitive, low-throughput extreme of the drying spectrum — the counterpart to Ch.10 (spray, high-throughput liquid feed) and Ch.12 (dielectric/microwave, volumetric heating). It is referenced by Ch.10's spray-freeze-drying subsection (§10.5.4) and conceptually brackets Ch.12 (microwave freeze drying is tried and fails here, while pure dielectric drying of thick cores is the live Ch.12 option). In the hygiene value chain it is essentially outside the mass-production path; its modeling toolkit (moving-boundary sublimation, bound-water desorption) is more relevant to pharmaceutical-grade hygiene actives than to pulp/SAP/nonwoven webs.

---

### 卫材行动卡

Relevance rating: ★ (one star) — freeze drying is not a bulk hygiene manufacturing route; relevance is confined to niche, high-value actives and to cautionary dielectric lessons.

H11.1 — Do NOT adopt freeze drying for bulk SAP / pulp / web drying. Situation: evaluating a "gentle" drying route for absorbent cores. Apply: per p.255 and p.270, freeze drying costs 1.5–2.5× fixed over running cost and is reserved for high-value heat-labile products. Effect: avoids a capital-intensive dead-end for commodity hygiene materials. ★

H11.2 — Treat spray-freeze-dried porous powders as a premium-only option. Situation: needing ultra-porous SAP/fragrance carrier powders (cf. Ch.10 §10.5.4). Apply: per p.280, freeze drying suits "high-value products with specific biological or physicochemical properties"; Ch.10 notes SFD costs 5–10× hot-air. Effect: scope to high-value actives only, never to core bulk. ★

H11.3 — Heed the dielectric runaway warning before piloting microwave cores. Situation: planning dielectric/microwave drying of thick wet cores (Ch.12). Apply: per p.261, water's higher dielectric loss than ice caused microwave freeze-drying runaway; the same water/polymer contrast governs thick-core dielectric drying. Effect: design Ch.12 dielectric routes with field uniformity and moisture-control safeguards, not blind volumetric heating. ★★

H11.4 — Bound-water control = shelf-life, not just dryness. Situation: specifying final moisture of a hygroscopic hygiene powder. Apply: per p.259, 10–35% of moisture is bound/sorbed and its removal sets stability (some vaccines need ~2%, others 0.1%). Effect: set residual-moisture specs against the product's bound-water isotherm, even if the dryer is convective. ★

---

======================================================================

## Chapter 12 — Microwave and Dielectric Drying

### 概述

Chapter 12 surveys the fundamentals, process advantages, equipment, industrial applications, and economics of electromagnetic (dielectric and microwave) drying. Unlike conductive/convective drying, which moves heat from surface to interior, these methods deposit energy volumetrically by coupling an oscillating electric field directly into polar molecules and ions. The chapter argues that the unique, rapid, selective, and self-limiting nature of this heating makes it especially valuable as a booster or finish stage paired with conventional dryers, rather than as a standalone unit. After establishing the governing equations (ionic conduction, dipolar rotation, complex permittivity, loss tangent, penetration depth), the author catalogs applications from lumber and textiles to latex-coated automotive tires and pharmaceuticals, then closes with a candid cost analysis: high capital cost demands judicious, hybrid deployment. For hygiene-materials R&D the chapter is highly relevant — thick, low-density, insulating structures (fluff + SAP cores) and waterborne latex binders are exactly the "hard-to-heat" substrates dielectric methods address.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

### 核心观点标题

Dielectric vs microwave frequency regimes

Volumetric "pumping" differs fundamentally from diffusion-limited drying

Critical moisture defines the hygroscopic window

Temperature-dependent runaway in polymers

Hybrid booster drying gives 6:1–8:1 leverage

- 

Selective heating spares the substrate

### 在书中的作用

Ch12 is the capstone "emerging/electromagnetic" drying method among the mechanical/thermal chapters (rotary, fluid bed, drum, spray, freeze). It complements Ch10 (spray) and Ch11 (freeze) by addressing thick, low-thermal-conductivity solids that those atomization/sublimation methods cannot handle, and prefigures the hybrid (two/three-stage) thinking introduced in Ch10.

### 卫材行动卡

Relevance: ★★★★★ — directly addresses thick, insulating, hygroscopic, latex-bonded structures central to diapers/wipes/absorbent cores.

ACTION CARD 1 — Boost thick-core drying

Situation: Final 10–40% db moisture in fluff+SAP core is diffusion-limited and slow in hot-air ovens.

Apply: Add a 915 MHz (or 13.56/27.12 MHz dielectric) booster/finish stage where the falling-rate zone collapses (p.293, 6:1–8:1 leverage; p.291 deep penetration).

Effect: Shorter line, less case-hardening, moisture leveling across thick pads.

ACTION CARD 2 — Dry waterborne latex binders selectively

Situation: Latex-bonded airlaid cores / nonwoven saturation (cf. auto-tire latex coating, p.298).

Apply: Use selective heating — field couples to water, substrate heated by conduction (p.292) — to drive off latex water without overheating polymer.

Effect: Lower thermal profile, preserved fiber/bond integrity.

ACTION CARD 3 — Tame polymer runaway near Tg

Situation: Hot-melt/adhesive layers in the composite warm past Tg and suddenly couple (p.288).

Apply: Closed-loop power control + pulsed on/off (p.290) to prevent internal scorch while finishing.

- 

Effect: Avoids hidden internal burn / bond degradation.

======================================================================

## Chapter 13 — Solar Drying

### 概述

Chapter 13 (László Imre) treats solar drying as an energy-system chapter of the handbook: it engineers dryers around the peculiar physics of intermittent, low-flux, non-dispatchable irradiation. The logic runs limitations → construction principles (three dryer classes) → economics (dynamic payback) → key elements (collectors, heat storage) → simulation methodology (mass-flow network MFN + heat-flow network HFN) → direction/control strategy (§13.7) → prospects (§13.8). Its intellectual center is not a drying mechanism but matching a stochastic, low-density heat source to a batch load via collectors, storage, recirculation, and PID control. For the hygiene-materials reader this chapter is peripherally relevant — solar drying does not appear in tissue, airlaid, or SAP process trains — but generic threads transfer: low-temperature (<60 °C) drying for quality-sensitive materials, the constant/falling-rate framework in thick beds, and recirculation/intermittent-operation strategy for energy effectiveness. These reappear in Ch.15–18 on the hygiene-relevant dryers.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.305–p.360 (PDF p.326–381).

---

### 在书中的作用

Ch.13 is the only chapter treating free thermal input and where storage + intermittency are first-class design variables. Its MFN/HFN simulation vocabulary recurs as the "process model" layer in later dryer chapters, but those assume dispatchable heat. Ch.13 therefore bookends Ch.14–18: it shows the worst-case boundary condition (non-dispatchable, low-grade heat) against which impingement, conveyor, pneumatic, and IR dryers are high-grade, tightly-controlled contrasts.

---

### 卫材行动卡

Overall relevance: ★☆☆☆☆ (very low; not forced per brief). Solar drying does not appear in diaper/wipe/tissue converting. Only methodological cross-links hold:

H11.1 — Storage-decoupling lesson (★). If a hygiene line pilots low-grade thermal recovery (exhaust-air heat wheels, warm-water buffers feeding a thermobond oven), the rock-bed/water-tank operating-mode logic (p.351) is a direct template for dispatchable-vs-stored-energy mode switching.

H11.2 — Payback/D/C discipline (★★). When justifying any capital dryer upgrade (impingement hood, IR cure, through-air oven), borrow the D/C + dynamic-payback method (p.319) rather than simple peak-efficiency claims.

H11.3 — Control-mode selection (★★). The PID selection rule (p.349) is generic and reusable for any dryer temperature/flow loop on a converting line.

H11.4 — Energy-effectiveness over peak efficiency (★★). Eq. 13.15's efficiency–temperature trade-off applies to combustion air heaters on Yankee/thermobond lines: raising supply-air temperature lowers heater efficiency.

No fibre-damage, curl, brightness, residual-moisture, or web-defect mechanisms are addressed; do not cite Ch.13 for those.

---

======================================================================

## Chapter 14 — Spouted Bed Drying

### 概述

Chapter 14 (Pallai, Szentmarjay, Mujumdar) treats the spouted bed dryer (SBD) as a particle-processing technology for materials too coarse to fluidize (grains) and, more importantly for the hygiene reader, for heat-sensitive pastes, slurries, suspensions, and synthetic products dried on a bed of inert particles. The chapter's arc runs: principle/device → residence-time distribution (RTD) → agricultural drying results → pulp/paste drying on inert particles → development (microwave-coupled MSB) → assessment. Its engineering center is the mechanically spouted bed (MSB) with inert packing, where wet feed coats large inert particles, dries in a thin film at low wet-bulb temperature, then wears off as powder. For hygiene R&D this is moderately relevant: it is a genuine low-temperature, attrition-controlled powder-production route for heat-labile polymers — directly parallel to drying SAP gel, fluff-pulp slurry, and nonwoven binder emulsions — and it supplies concrete specific-energy-consumption benchmarks (kJ/kg water) for the energy-cost/tonne question. Polymer examples appear explicitly (PVC, Hostaform, polypropylene, "synthetic products").

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.361–p.382 (PDF p.382–403).

---

### 在书中的作用

Ch.14 sits in the particulate/specialized dryer cluster. It complements Ch.16 (pneumatic/flash — also for particulates but high-velocity, short-residence) and Ch.17 (conveyor — continuous web). Its unique contribution is the inert-particle thin-film drying of pastes/suspensions — the closest handbook analogue to converting a polymeric slurry (SAP gel, fluff slurry, binder emulsion) into a free-flowing powder without thermal damage. For hygiene R&D it is a reference for gentle powder production and for energy benchmarking.

---

### 卫材行动卡

H11.1 — Use inert-particle SBD logic for gentle SAP/PVA powder drying (★3). Action: When drying SAP gel or binder emulsion to powder, mimic the thin-film-on-inert-particle principle (p.374) — keep product at wet-bulb T, not inlet-gas T — to avoid crosslink scission / casehardening; benchmark energy against ~3000–9000 kJ/kg water.

H11.2 — Set a quality ceiling temperature like the seed rule (★3). Action: Adopt the seed-for-sowing limit logic (p.367: T must not exceed 40–45 °C for viability; 46–50 °C skins over and stalls diffusion) as a spec for heat-sensitive nonwoven binders and lotion/fragrance coatings — define a max-particle-temperature window, not just inlet-air T.

H11.3 — Decouple circulation from drying airflow (★2). Action: On convective cure ovens for thermobonded webs, copy the screw/tangential-inlet decoupling (p.381) so dwell/throughput is tunable independently of drying-air velocity — protects low-melt binder from over-cure.

H11.4 — Price the grinding-avoidance premium (★2). Action: PVC's 9000 kJ/kg is justified by retained grain size (p.377); for SAP/powder grades where attrition must be minimized, accept higher specific energy in exchange for narrow PSD — quantify via the energy/tonne vs PSD spec.

H11.5 — Benchmark energy/tonne from the tables (★2). Action: Use Tables 14.8–14.24 specific-energy values (2900–9700 kJ/kg water) as sanity bounds when costing a new powder-drying step for fluff/pulp/SAP feedstocks.

H11.6 — Overall relevance: ★★★. Genuine polymer/heat-sensitive-powder content (PVC, PP, Hostaform, "synthetic products"); directly transferable to SAP-slurry and binder-emulsion drying, with one honest gap (no fluff/SAP data).

---

======================================================================

## Chapter 15 — Impingement Drying

### 概述

Chapter 15 (Arun S. Mujumdar) is the process-engineering core of the Yankee-hood and through-air technologies named in the assignment brief: it covers impinging hot-air jets for rapid convective drying of continuous sheets — explicitly tissue paper, photographic film, coated paper, nonwovens, and textiles (p.383). The chapter's logic: impingement is chosen only when the dominant moisture to remove is unbound/surface moisture and high external heat/mass-transfer rates are wanted; once drying becomes internal-diffusion-controlled, the high flux can degrade heat-sensitive product. The body delivers a design procedure (nozzle configuration → geometry → velocity/temperature/spacing → drying-rate calc → recycle), Martin's empirical Nu/Sh correlations for round and slot arrays, and a catalogue of extraneous effects (crossflow, semiconfinement, mass flux, large ΔT, suction, surface motion, oblique impingement, swirl). For the hygiene reader this is a ★★★★★ chapter: it is the handbook layer governing tissue Yankee hoods, through-air nonwoven bonding ovens, and lotion/coating cure on wipes, and it supplies the energy benchmark (3100 kJ/kg water, 75–90 % thermal efficiency) for the energy-cost/tonne question plus the web-defect mechanisms (case hardening, cracking, coating streaks, fire hazard).

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.383–p.394 (PDF p.404–415).

---

### 在书中的作用

Ch.15 is the high-intensity convective dryer chapter, complementing Ch.14 (gentle inert-bed), Ch.16 (pneumatic/flash — dilute-phase particulates), Ch.17 (conveyor — continuous web/belt), Ch.18 (infrared — radiative). It is the single most hygiene-central dryer chapter because tissue, nonwoven, and wipe-coating drying are explicitly its applications. It supplies the external heat/mass-transfer coefficients (h, hₘ) that Ch.4's property tables and Ch.17's conveyor ovens consume.

---

### 卫材行动卡

H11.1 — Gate impingement on unbound moisture only (★★★★★). Action: For tissue Yankee and nonwoven hoods, use impingement for the surface/constant-rate phase; switch to through-air or lower flux in the falling-rate/bound-moisture phase to avoid casehardening and curl (p.383–384).

H11.2 — Set jet T from evaporative-cooling window, not peak (★★★★★). Action: Exploit the constant-rate latent sink (p.385) to run 100–350 °C jets while holding web surface below degradation/ignition; back off flux once bound moisture dominates and surface T climbs (p.385).

H11.3 — Control coating streaks on wipes (★★★★). Action: For lotion/print-coated wipes, cap jet velocity and tune nozzle-to-substrate spacing to avoid shear-driven "railroading" streaks (p.384); validate coating rheology vs impact shear in lab.

H11.4 — Place exhaust to protect cross-machine uniformity (★★★★). Action: For slot-nozzle (ASN) hoods allow ≤2 jet rows before exhaust (p.389); design exhaust ports to keep crossflow from halving local h and producing moisture stripes across the web.

H11.5 — Cost energy at 3100 kJ/kg, 75–90 % efficiency (★★★★★). Action: Use 3100 kJ/kg water and 75–90 % thermal efficiency (p.388) as the energy-cost/tonne baseline when scoping a new impingement/air-floater line; challenge designs that fall outside this band.

H11.6 — UseMartin correlations to size nozzle pitch (★★★). Action: Apply ARN/ASN Nu correlations (p.388–389) with optimal spacing ~1.40H to predict h and set nozzle pitch for a tissue or nonwoven impingement zone; correct for mass flux (≈10 % paper).

H11.7 — Add suction for falling-rate nonwoven bonding (★★★). Action: Combine impingement with through-drying suction (+10–15 % h/m, p.390) for the falling-rate period of heat-sensitive nonwoven webs — the recommended synergy for permeable sheets.

---

======================================================================

## Chapter 16 — Pneumatic and Flash Drying

### 概述

Chapter 16 (Irene Borde and Avi Levy) treats pneumatic (flash) drying as a gas–solid transport convective dryer in which wet particulates are suspended in a hot gas (usually air, sometimes superheated steam) and conveyed through a duct, with residence time in the drying section of only 0.5–10 s (p.395). The chapter's logical spine: because contact time is so short and flow is parallel (co-current), the material temperature stays always low (p.395), which makes flash drying suitable only for external/surface moisture and for thermolabile solids, but less suitable for internal moisture (p.395–396). The body then delivers (16.2) operation principle and application inventory, (16.3) a design procedure built on heat/mass/momentum balances plus transfer coefficients, (16.4) a long list of dried materials, (16.5) the modelling menu — empirical pressure-drop correlations, Rocha/DryPak models, and the two-fluid/Eulerian-granular/DEM frameworks with the full balance-equation set (16.5)–(16.25), and (16.6) expected developments (heat recovery, heat pumps, combined processes). For the hygiene reader this is a weak chapter: flash drying handles particulates and pastes, not the continuous webs, fluff fibre mats, or airlaid nonwovens that dominate diaper/wipe manufacture. The genuinely relevant threads are narrow but real — drying of SAP powder and polymer pellets, the dust-explosion safety limit on cellulosic/SAP powders, and superheated steam as an explosion-free medium.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.395–p.408 (PDF p.416–429).

---

### 在书中的作用

Ch.16 is the dilute-phase particulate convective dryer in the dryer taxonomy. It complements Ch.14 (spouted bed — dense-phase inert particles), Ch.15 (impingement — continuous sheets), Ch.17 (conveyor/belt — continuous webs), and Ch.18 (infrared — radiative). Its unique position is gas–solid suspension with second-scale residence; it is the only chapter whose primary feed is free-flowing powder/pellets, which is exactly why its hygiene relevance is narrow (SAP powder, polymer masterbatch) rather than web/fibre-centric.

---

### 卫材行动卡

Relevance rating: ★★☆ (narrow). Flash drying is a particulate/paste dryer. It does not dry tissue, nonwoven webs, or fluff mats. The real hygiene hooks are SAP powder, polymer masterbatch, and powder-explosion safety — rated below.

H11.1 — Use flash drying only for surface-moisture powders (★★★★). Action: Route SAP powder, PP/PE masterbatch, and other free-flowing hygrology powders through flash/spin-flash lines sized by free-fall velocity (p.396); do not use it for bound-moisture fluff or web. Expect only surface-moisture removal (p.395–396).

H11.2 — Set inlet gas T from the polymer's thermal window, not just evaporation (★★★★). Action: Cap inlet temperature below the solid's thermal-degradation/Tg (p.397, "thermal sensitivity of the solids"); for PVC-like thermoplastics validate against a decomposition onset. See POP trailer.

H11.3 — Engineer the dust-explosion limit (★★★★★). Action: For cellulosic/SAP dust, stay outside flammability limits (p.397) via inerting or — preferably — superheated steam medium (p.399), which removes fire/explosion risk; if steam, enforce air-tight feed/discharge (p.399).

H11.4 — Consider spin-flash for high-solids slurries/pastes (★★★). Action: A binder or SAP slurry/paste that would otherwise need spray-atomization can be spin-flash dried without an atomizer, up to 10 t/h (p.399) — cheaper thermal energy than spray drying (p.399).

H11.5 — Predict scale-up with the two-fluid kernel (★★★). Action: Use Eqs. (16.5)–(16.25) to forecast that larger/coarser SAP agglomerates need longer residence or higher gas velocity (p.403); validate the model against pilot data first (p.403).

---

======================================================================

## Chapter 17 — Conveyor Dryers

### 概述

Chapter 17 (Dan Poirier) is the handbook's treatment of the conveyor (through-circulation) dryer — a continuous unit in which product is carried on a perforated belt or mesh bed while hot process air is forced through the bed of product (p.409). The chapter's argument: although "conceptually very simple… a conveyor in a box with hot air" (p.409), it is "one of the most versatile dryers available" (p.409) precisely because forcing air through a permeable bed gives high, uniform heat/mass transfer. The logic flows from configuration choice (single-pass, single-pass/multiple-stage, multiple-pass — §17.2) → components (bed, enclosure, fans, heat source, feeder/spreader, accessories — §17.3) → selection & sizing via heat/mass balance and the volumetric heat-transfer coefficient (§17.4) → operation/control (air temperature, retention/bed depth, airflow, humidity — §17.5) → heat recovery (§17.6), sanitation (§17.7), economics (§17.8). For the hygiene reader this is a ★★★★★ chapter: the through-circulation conveyor is exactly the unit operation of through-air (TAD) bonding of airlaid nonwovens and thermobonding of bicomponent-fibre webs, and the chapter explicitly lists "super absorbent polymers" among products dried on single-pass/single-stage conveyors (p.411). It also names the glass transition temperature as the set/quench point for a coating (p.410) — the thermal-bonding window for PP/PET binder fibres.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.409–p.420 (PDF p.430–441).

---

### 在书中的作用

Ch.17 is the continuous permeable-bed convective dryer — the natural home of through-air (TAD) technology. It complements Ch.15 (impingement — air onto a sheet) and Ch.14-family Yankee (conductive), and it is the production-scale cousin of Ch.16's flash (dilute powder). Within the hygiene frame it is the bonding-oven chapter: airlaid through-air bonding and thermobond-oven lines are conveyor dryers forced-air-through-web, even when the handbook does not name nonwovens explicitly.

---

### 卫材行动卡

Relevance rating: ★★★★★ (strongest in this batch for airlaid/thermobond nonwovens and SAP).

H11.1 — Run the through-air oven as a conveyor forced-through-bed dryer (★★★★★). Action: Treat airlaid through-air bonding and thermobond ovens as Ch.17 conveyors: hot air through the permeable web (p.409); exclude impermeable sheets (p.410). Size from bed volume + h_v (p.416).

H11.2 — Spread uniformly or accept shading (★★★★★). Action: Engineer feeder/spreader to even web basis weight; nonuniform loading → preferential airflow → over-dry thin zones + wet clumps (p.415). This is the root cause of cross-web moisture streaks in nonwoven bonding.

H11.3 — Use the Tg quench to lock bonds (★★★★★). Action: After the bond zone, cool the web below the binder-fibre Tg (p.410, "set a coating by getting it below its glass transition temperature") with chilled air to freeze sheath bonds; see POP trailer for PP/PET Tg windows.

H11.4 — Progress bed depth: shallow first, deepen after surface set (★★★★). Action: Run first zone shallow to contain the light/web and avoid clumping; deepen after surface is partially dry (p.420) to maximize throughput without deformation.

H11.5 — Cost energy from the four-term balance (★★★★★). Action: Use Table 17.2 splits (evaporated water ~69 %, exhaust ~21 %, product ~8 %, losses <7 %, p.417–418) and the >10 % heat-recovery lever (p.419) as the energy-cost/tonne baseline for a through-air bonding line.

H11.6 — Avoid casehardening via humidity floor (★★★★). Action: Keep zone humidity off the floor — too-low humidity causes casehardening (p.419); too-high loses capacity/corrodes. Tie exhaust dampers to humidity sensors (p.419).

H11.7 — Size an SAP dryer from conveyor logic (★★★). Action: SAP powder is a named conveyor product (p.411); apply the h_v + heat-balance method (§17.4) to size an SAP post-reaction dryer, measuring h_v on a lab tray first (p.416).

---

======================================================================

## Chapter 18 — Infrared Drying

### 概述

Chapter 18 (Cristina Ratti and Arun S. Mujumdar) covers infrared (IR) radiative drying — supplying heat by electromagnetic radiation that needs no propagation medium and is absorbed/converted to heat at the product surface (§18.2). The argument: IR is "an increasingly popular, but not yet common" primary heat source whose strengths are direct volumetric/near-surface energy deposit, fast transient response, leveling of moisture profiles, and easy combination with convection or vacuum (p.421–422). The chapter delivers the radiative-transfer theory (black/gray body, Planck, Wien, Stefan–Boltzmann, Kirchhoff, Bouguer attenuation — §18.2), the radiation properties of materials and the critical need to match emitter wavelength to the product's absorption band (§18.2.2), a steady-IR modeling framework (semi-transparent "Hasatani" and opaque boundary models, §18.3.1), advantages/limitations (§18.3.2), industrial dryers and emitters (§18.4.2), costs (§18.4.3), and conclusions (§18.5). For the hygiene reader this is a ★★★★☆ chapter: the chapter opens by naming "dehydration of coated films and webs" and "correct moisture profiles in drying of paper and board" as the most common IR applications (p.421), and later shows an IR + impingement oven "specially for drying adhesives and inks on papers, foam and composite web substances" (p.432) — i.e. exactly the lotion/coating cure on wipes and the combination with Ch.15's impingement. The genuine limitation to state honestly: IR is "essentially surface dryers" (p.429) and penetration into thick porous webs is still underdeveloped.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.421–p.436 (PDF p.442–457; chapter body to ~p.434).

---

### 在书中的作用

Ch.18 is the radiative dryer chapter — the counterpart to Ch.15 (convective impingement) and Ch.12 (microwave/dielectric). Its unique position is surface/coating cure with no medium, which is why it is the natural technology for lotion/ink/adhesive cure on wipes and for moisture-profile correction on paper/board. The hybrid IR + impingement oven (p.432) is where Ch.18 and Ch.15 physically merge.

---

### 卫材行动卡

Relevance rating: ★★★★☆ (strong for wipe lotion/coating cure; weaker for bulk cores).

H11.1 — Use IR for the lotion/print coating cure on wipes (★★★★★). Action: Deploy IR for dehydrating/curing the coated film on the wipe web (p.421); it is the right tool for thin coatings, not the bulk nonwoven.

H11.2 — Build the hybrid IR + impingement oven (★★★★★). Action: Mount IR electric heaters between impingement nozzles (p.432) — radiation cures the coating, convective jets strip solvent/water and protect the substrate; proven viable (p.434). Reuse Ch.15 nozzle design.

H11.3 — Match emitter wavelength to the coating band; ramp T as it dries (★★★★★). Action: Pick source T so the peak λ sits where the coating absorbs but the substrate does not (p.425, Fig.18.3); raise emitter T as reflectivity climbs during drying (p.425) to avoid late-cycle under-cure or scorch. See POP trailer for polymer bands.

H11.4 — Avoid scorch with a hotter, better-penetrating source (★★★★). Action: Counter-intuitively choose the higher source T for penetration (p.425); a cooler source dumps flux at the surface and scorches the polymer film.

H11.5 — Level the web moisture profile (★★★★). Action: Use IR's "leveling of the moisture profiles" advantage (p.428) to even cross-web moisture on coated/printed wipes; combine with humidity-controlled exhaust (p.430).

H11.6 — Engineer fire safety and solvent exhaust (★★★★). Action: IR carries a fire-hazard flag (p.429); size oven exhaust to remove solvent/smoke/moisture (p.430) for combustible nonwoven substrates and volatile coating carriers.

H11.7 — Cost at IR 500 $/kW, plan lamp replacement (★★★). Action: Budget IR capital at ~500 $/kW (Table 18.4, p.434), quartz-lamp life 2000–3000 h (p.433) as the maintenance line in the energy-cost/tonne model.

---

======================================================================

## Chapter 19 — Superheated Steam Drying

### 概述

Chapter 19 (Arun S. Mujumdar) treats superheated steam drying (SSD) — replacing hot air/combustion gas with superheated steam as the convective drying medium (p.437). The chapter's logic: because the exhaust is also steam, its latent heat can be recovered by condensation or mechanical/thermocompression, making SSD's net energy 1000–1500 kJ/kg water versus 4000–6000 kJ/kg for hot-air drying (p.438) — a clear energy advantage. SSD also eliminates oxygen, so there is no fire/explosion hazard and no case-hardened skin forms (p.438). The body surveys industrial applications by product — sludges, coal, beet pulp, lumber, peat, paper and tissue (§19.2.6), wood particles, plus quality (§19.2.8, Table 19.2), miscellaneous (§19.3), exhaust-steam utilization (§19.4), and conclusions (§19.5). For the hygiene reader this is a ★★★★★ energy chapter: it is the live energy-reduction route for pulp/paper drying (the fluff-pulp feedstock of diapers), it quantifies fibre-property effects of steam vs air drying (tensile +20–30 %, burst +20 %, internal bond +10–20 %, crystallinity unchanged, brightness slightly worse above 300 °C — Table 19.2, p.446), and it states the hydrothermal / glass-transition limits that govern whether SAP and binder fibres survive (p.439). The honest caveat: "No commercial dryers exist for direct drying of paper webs with superheated steam" (p.444) — the technology is promising but not yet at scale for tissue.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.437–p.450 (PDF p.458–471).

---

### 在书中的作用

Ch.19 is the energy-recovery convective variant — the steam-medium counterpart invoked by Ch.16 (flash, p.399), Ch.17 (conveyor, p.439), and Ch.18 (impingement, p.440) as the explosion-free medium. Its distinct contribution is the latent-heat recovery economics and the fibre-quality evidence, which no other chapter supplies. It is the handbook's answer to the energy-cost/tonne question for pulp/paper.

---

### 卫材行动卡

Relevance rating: ★★★★★ (energy + fibre-property, with honest pre-commercial caveat for tissue).

H11.1 — Scope SSD as the pulp/paper energy lever (★★★★★). Action: For fluff-pulp or tissue lines, model SSD at 1000–1500 kJ/kg vs 4000–6000 air (p.438); require a steam sink (mill integration) for the saving to survive (p.437).

H11.2 — Expect stronger pulp, watch brightness (★★★★★). Action: Steam drying raises tensile +20–30 % and internal bond +10–20 % with crystallinity unchanged (Table 19.2, p.446); cap steam T below ~300 °C to avoid brightness/yellowing loss (p.446) on white fluff.

H11.3 — Use low-pressure SSD for binder/SAP sensitivity (★★★★). Action: Where PP/PET sheath or SAP could approach steam saturation T, run low-pressure SSD (p.439, p.446) so saturation T stays below the polymer Tm/Tg; see POP trailer.

H11.4 — Eliminate fire/explosion on combustible webs (★★★★★). Action: SSD removes O₂ → no fire/explosion and no case-hardened skin (p.438); a compliance path for combustible nonwoven/tissue lines that Ch.15/Ch.18 flag as hazardous.

H11.5 — Combine impingement + through-drying under steam (★★★★). Action: Adopt the Papridryer-style steam impingement + through-drying config (p.444–445) for tissue; it is the Ch.15/Ch.17 merge under an explosion-free medium.

H11.6 — Budget ancillaries, not just the dryer (★★★★). Action: SSD ancillary cost (feed/discharge seals, exhaust recovery) exceeds the dryer alone and needs very large continuous tonnage (p.438); scope capital accordingly before committing.

---

======================================================================

## Chapter 20 Analysis — Special Drying Techniques and Novel Dryers

### 概述

Chapter 20 (Kudra & Mujumdar) is a survey of special drying techniques and novel dryer hardware that do not fit the conventional conveyor / rotary / spray taxonomy. It is explicitly an update/overlay chapter: the authors state the focus "is on special drying techniques and selected novel dryers" and that "this chapter effectively updates several chapters in this handbook" (print p.513). It opens with Mujumdar's enumerated trends driving dryer innovation and then catalogs ~9 special techniques (§20.2.1–20.2.9) and 18 novel dryers (§20.3.1–20.3.18), closing with a brief conclusions section.

For the hygiene reader this is the highest-yield survey chapter in the assignment: it contains a directly on-point nonwoven/textile benchmark (Table 20.1, "unwoven fabric for artificial leather"), a textile dryer family (Remaflam, §20.3.10), paper/pulp-mill sludge dewatering routes (ROTADISC, Carver–Greenfield, Dry-Rex), and dielectric (RF/MW) paper drying (§20.3.18). Many other sub-sections (aerogels, pulse combustion, supercritical drying) are only distantly relevant.

### 在书中的作用

An overlay/update chapter (the authors say it "effectively updates several chapters"). It points the reader to dedicated chapters for superheated steam (Ch19), MW/RF (separate chapters), and pulp/paper drying (a later chapter). Functionally it is the "what else is out there" catalog that a process engineer consults when conventional dryers hit an energy or web-defect wall.

### 卫材行动卡

Rating: ★★★★☆ (strong — multiple directly on-point anchors, but survey depth is thin and many sub-sections are off-target).

AC1 — Nonwoven/web dryer benchmarking. Use Table 20.1 (print p.457) as a reference point: active-fluid-bed (through-bed contact-sorption) drying of an "unwoven fabric" achieved 4,200 vs. 22,300 kJ/kg H₂O and 12 m vs. 56 m path vs. a steam cylinder. Action: when specifying a nonwoven drying/bonding step, benchmark against this ~5× specific-energy and ~5× footprint upside before defaulting to oven/cylinder routes.

AC2 — Pulp-mill sludge & dewatering. ROTADISC (print p.465), Carver–Greenfield (print p.473, explicitly "activated sludge from wood pulp plant"), and Dry-Rex (print p.502, "wood pulp, pulp and paper mill sludge") are three routes for mill waste. Action: in fluff-pulp supplier audits, ask which dewatering/drying route the mill uses — it bears on both mill energy cost (passed through in price) and on biosolids/discharge compliance.

AC3 — Textile/nonwoven line analog. Remaflam (print p.497–498) and the general statement that textiles use "impinging jets, contact, infrared, or through dryers" (print p.497) confirm that hygiene web lines share the textile drying toolbox. Action: borrow textile line-speed/zone-length data (e.g., 42 m/min, 1.6 m zone for 220 g/m²) as a sanity proxy when scoping top-sheet/backsheet drying capacity.

AC4 — Dielectric-assisted paper drying. RF 50-Ω technology on cellulose/mineral board (print p.510–511) is the closest book analog to energy-efficient tissue/paper drying. Action: flag RF/MW-assisted drying as a candidate energy-reduction route worth a pilot vs. conventional hot-air for any future line retrofit.

- 

AC5 — Polymer/binder drying. Vortex dryers list polyvinyl alcohol, polyvinyl acetate (print p.491, Table 20.17); ISDs are "especially suitable for drying… polymers" (print p.484). Action: if drying SAP-precursor or binder dispersions, these intensified dryers are candidates.

======================================================================

## Chapter 21 Analysis — Drying of Foodstuffs

### 概述

Chapter 21 (Sokhansanj & Jayas) is a self-contained primer on food dehydration — objectives, moisture/water-activity theory, psychrometrics, a full drying-modeling derivation (heat/moisture balances, constant/falling-rate periods), physical/thermal properties, a catalog of food dryers, and a section on nutrient losses during dehydration. It is written for the agricultural/food engineer, not the fibre engineer.

For the hygiene reader the chapter is indirect but genuinely useful: its transferable frameworks are (a) the water-activity / equilibrium-moisture formalism that governs microbial stability — directly applicable to the residual-moisture spec of fluff pulp and nonwoven webs; (b) superheated-steam drying of foods (§21.7.14) which echoes Ch19 and is the cleanest book analog for "no oxidation → brightness preserved" in pulp; and (c) non-enzymatic browning / Arrhenius degradation kinetics (§21.8.5) which is the food analog of hydrothermal brightness reversion in cellulose. Per the assignment brief, Ch21 is correctly judged the weakest of the six chapters for hygiene — its value is as a transferable framework, not as a directly applicable case study.

### 在书中的作用

A foundational/reference chapter — it supplies the moisture–water-activity and drying-rate theory that the process-specific chapters (Ch16–Ch20) assume. It is the "theory and food application" counterpart to the industrial dryers; its SSD subsection points back to Ch19 and its spray/drum/fluid-bed descriptions overlap Ch17–Ch20.

### 卫材行动卡

Rating: ★★★☆☆ (moderate — transferable framework is strong, but content is food-specific and needs translation; honestly the weakest of the six for direct case studies).

AC1 — Residual-moisture spec as a water-activity spec. Use VP1 (print p.522: a_w ≤ 0.7 inactivates microbes; a_w > 0.4 enables oxidation) and the GAB relation (VP4) to justify and quantify fluff-pulp and core residual-moisture limits. Action: express your spec in a_w terms and convert to %wb via GAB for the local storage RH.

AC2 — Brightness reversion via Arrhenius. Adopt the §21.8 kinetic framework (VP7/VP8, print p.540–543) to design accelerated brightness-stability tests on dried pulp, treating yellowing as a thermally activated loss with an activation energy. Action: run isothermal humidity-oven aging and fit k = k_0 exp(−E/RT) rather than ad-hoc pass/fail.

AC3 — SSD as brightness-preserving route. §21.7.14 (print p.538–539) shows SSD gives "no product oxidation" and is phytosanitary — the same argument Ch19 made for pulp/paper. Action: when evaluating energy + brightness, keep SSD on the candidate list and cite the "no oxidation" benefit as the brightness-reversion mitigation.

AC4 — Avoid hot-surface/low-moisture residence. VP6 (print p.540) proves drum (surface) drying damages far more than spray (rapid, evaporatively cooled) drying. Action: minimize hot-cylinder dwell at low web moisture on bonding/calendering lines; prefer through-air/low-surface-temp routes.

- 

AC5 — Bound vs. free moisture language. VP2 (print p.521) categorizes moisture into ionic (carboxyl/amino) vs. H-bonded (hydroxyl/amide) sites — directly analogous to cellulose OH and SAP carboxylate. Action: use this language when distinguishing "free surface water" (drives microbial growth) from "bound water" (does not) in absorbent cores.

======================================================================

## Chapter 22 — Drying of Fish and Seafood

### 概述

Chapter 22 (M. Shafiur Rahman) surveys the drying of fish and seafood as a food-preservation unit operation: it walks from raw-material structure (muscle fibre / extracellular space) through pretreatments (salting, cooking, smoking), dryer selection (sun, convective, vacuum, freeze), packaging under low water activity, and the full catalogue of quality changes (microflora, browning, lipid oxidation, protein denaturation, shrinkage and pore formation, rehydration, solubility, texture, nutrition). Its governing logic is that fish flesh is a high-moisture, high-protein, often high-fat biological matrix whose drying is dominated by case-hardening (pellicle formation), surface-crust barrier, and shrinkage/collapse governed by the glass-transition state. For the hygiene-materials reader this is a low–medium transfer chapter (★★–★★★): the substrate is animal muscle, not fluff pulp or SAP, and the author never mentions hygiene products. The genuinely portable mechanisms are (i) the case-hardening / surface-crust rule — a hard dried-protein skin that retards internal moisture movement — directly analogous to binder-skin / casehardening on a hot-air-dried nonwoven web; (ii) the glass-transition explanation of shrinkage and pore formation (Tg′-based collapse), which is a polymer-physics concept shared with SAP/binder webs; and (iii) the quality-vs-rate trade-off (push temperature to kill microbes vs. keep organoleptic quality). Sections 5 and 11 state plainly where substrate differences limit transfer — do not invent diaper applications for fish.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.545–p.557 (PDF p.566–578; references p.557+).

---

### 在书中的作用

Ch.22 is one of the food/agricultural substrate chapters (with Ch.23 grain, Ch.25 fruit/veg, Ch.26 herbal/tea, Ch.27 roots). It is the only chapter that explicitly deploys the glass-transition framework to explain shrinkage/collapse, which dovetails with Ch.4 (property tables) and Ch.24 (sorption/water activity). Its case-hardening and quality-vs-rate material is the biological mirror of Ch.15's web-defect catalogue. Methodologically it is the weakest direct-transfer chapter for hygiene; its role is to supply the case-hardening and Tg-collapse vocabulary that the process-engineering chapters apply to nonwoven webs.

---

### 卫材行动卡

Relevance rating: ★★ (low–medium). Substrate is fish muscle; the chapter never addresses fluff pulp, SAP, or nonwovens. Genuine mechanism transfer exists for case-hardening, glass-transition collapse, staged-temperature, and monolayer stability — but no diaper application may be invented for fish, salting, smoking, or seafood microbiology.

H11.1 — Treat surface-skin as a rate-limiting barrier (★★★). Action: On hot-air lines for fluff/binder webs, cap initial surface flux so a vitrified/dried-skin layer does not form and trap interior moisture — the case-hardening rule (p.550) applied to nonwoven drying.

H11.2 — Use the Tg′ lens for loft/collapse (★★★). Action: Treat an airlaid/SAP web like the freeze-vs-hot-air contrast (p.554–555): keep the drying zone at/under the relevant glass-transition window to preserve porosity and avoid rubbery collapse; raise T only when the web is already glassy-stable.

H11.3 — Stage temperature high→low (★★★). Action: For microbial-risk or thermal-sensitive hygiene substrates, use high flux at high moisture (constant-rate) then low flux at low moisture (falling-rate) — the staged profile of p.552 — to balance throughput against quality.

H11.4 — Respect the monolayer window for storage (★★). Action: Note the aw≈0.3 monolayer oxidation-minimum (p.553) as a qualitative anchor when setting warehouse RH targets for moisture-sensitive cores (quantitative version in Ch.24).

---

======================================================================

## Chapter 23 — Grain Drying

### 概述

Chapter 23 (Raghavan & Sosle) is an equipment-and-operations survey of grain drying: from low-intensity crop conditioning (aeration, natural-air, in-storage supplemental heat) through artificial heated-air dryers (bin: batch/recirculating/continuous; portable: nonrecirculating/recirculating), dryer selection, solar, developing-country practice, nonconventional methods (heat-pump, desiccant, particle–particle conduction), and hay drying. Its central logic is matching dryer type to scale, crop, and facility, governed by the need to reach a safe-storage moisture without heat damage. For the hygiene-materials reader this chapter is a medium-transfer one (★★★): it never mentions fluff pulp, SAP, or nonwovens, but it supplies two genuinely portable frameworks the brief flags — (i) deep-layer vs thin-layer (shallow-layer) drying, where a thin layer (<0.20 m) develops no significant moisture gradient (the exact premise behind the thin-layer drying models that Ch.24 will formalise), and (ii) tempering / multistage drying (dryeration, combination drying), where a high-temperature pass is followed by a hold that lets interior moisture migrate outward before a low-energy finish — directly analogous to bale and roll conditioning of fluff pulp and warehouse moisture equilibration. Sections 5 and 11 state plainly where substrate differences limit transfer.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.561–p.571 (PDF p.582–592; references p.571+).

---

### 在书中的作用

Ch.23 is a food/agricultural substrate chapter and the operations companion to Ch.24 (grain property values and measurement) and Ch.25 (fruit/vegetable). It introduces the deep-bed vs thin-layer and tempering vocabulary that Ch.24量化 (sorption, thin-layer models). For hygiene it is the bridge to bale/roll conditioning and warehouse moisture control — the "how to dry a deep bed of fibrous material and let it equilibrate" chapter, complementing Ch.15's web-drying and Ch.17's conveyor/through-air.

---

### 卫材行动卡

Relevance rating: ★★★ (medium). Substrate is cereal grain; no fluff/SAP/nonwoven content. Genuine method transfer exists for deep-bed vs thin-layer, tempering/multistage, and safe-storage moisture / heat-damage guardrails — directly applicable to fluff-pulp bale and roll conditioning and warehouse RH control. No diaper application may be invented for grain, kernels, or farming.

H11.1 — Apply tempering to bale/roll conditioning (★★★★). Action: After a dryer pass, hold fluff-pulp bales/rolls near target moisture for a temper period so interior moisture migrates outward (dryeration logic, p.563); then finish with low-energy air — cuts the hard-to-remove core moisture uniformly and saves energy, exactly as grain (capacity +60%, fuel −20%+).

H11.2 — Treat bales as deep beds; respect gradients (★★★★). Action: A pulp bale/roll is a deep bed (cf. 3.5 m silo, p.569), not a thin layer (<0.20 m, p.569) — so expect interior-vs-surface moisture gradients and design dryer residence + post-conditioning to equalize, rather than forcing a single pass to spec.

H11.3 — Set residual-moisture spec + max thermal-exposure guardrail (★★★★). Action: Borrow Table 23.1 logic (p.564): define a target residual moisture (cf. 11–13% wb) and a maximum safe temperature by end-use/heat-damage window (cf. 43/54/82 °C) for fluff/SAP/binder; for long warehouse storage set spec 1–2% tighter (footnote b, p.564).

H11.4 — Control warehouse aeration by ambient RH (★★★). Action: When conditioning/equalizing stored material, pick low-RH windows (cf. RH ≤ 70%, air ≥ 1.1 °C above ambient, p.562) to avoid re-wetting — the warehouse-equilibration analogue to Ch.24's ERH logic.

---

======================================================================

## Chapter 24 — Grain Property Values and Their Measurement

### 概述

Chapter 24 (Jayas & Cenkowski) is the measurement-and-property handbook for grains and oilseeds: physical (bulk/particle density, porosity, shape, angles of repose, friction), hygroscopic (moisture measurement, equilibrium moisture content EMC, equilibrium relative humidity ERH, sorption/desorption, hysteresis, five isotherm equations), thermal (specific heat, conductivity/diffusivity, convective h, latent heat of vaporization, heat of respiration), electrical (dielectric, moisture meters), optical (NIR/reflectance), and aerodynamic (drag, terminal velocity) properties, closing with a full List of Symbols. For the hygiene-materials reader this is the single strongest method-transfer chapter of the batch (★★★★★): EMC, ERH (i.e. water activity a_w), sorption/desorption isotherms, hysteresis, and the thin-layer drying equation are precisely the tools used to set residual-moisture specs and predict warehouse moisture pickup for fluff pulp and SAP. The chapter never mentions hygiene products, but its hygroscopic section is substrate-agnostic — it applies to any hydrophilic porous solid. Sections 5 and 11 state plainly where the numbers (grain cultivars, ASAE standards) differ from pulp/SAP, but the methods transfer directly.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.573–p.598 (PDF p.594–619; references p.598+).

---

### 在书中的作用

Ch.24 is the property-and-measurement backbone that makes every other drying chapter quantitative. It is the direct methodological home of the thin-layer premise introduced in Ch.23 (p.569) and the empirical basis for Chs. 25–27 (fruit/veg, herbal, roots). For hygiene it is the bridge from "dry it" to "spec it and predict warehouse pickup": EMC/ERH/isotherm/GAB are the exact toolkit for fluff-pulp and SAP moisture specification. It complements Ch.4 (property tables) and Ch.15 (web drying) with the measurable, modellable hygroscopic foundation.

---

### 卫材行动卡

Relevance rating: ★★★★★ (very high — method transfer). This chapter supplies the exact toolkit (EMC/ERH/sorption isotherm/GAB/thin-layer Eq 24.5/wb-db discipline/latent-heat rise) for setting fluff-pulp and SAP residual-moisture specs and predicting warehouse moisture pickup. Substrate is grain, but the hygroscopic method is substrate-agnostic. No diaper "application" is invented for grain — the transfer is to pulp/SAP measurement and specification.

H11.1 — Measure pulp/SAP desorption isotherm by the static salt method (★★★★★). Action: Dry fluff-pulp and SAP samples over saturated salt solutions (known ERH) at 25 °C to equilibrium (1–5 weeks), weigh, fit the GAB model (p.580) → obtain the a_w-vs-moisture curve that sets warehouse RH and the outgoing residual-moisture spec.

H11.2 — Set spec on the desorption branch, respect hysteresis (★★★★★). Action: Because sorption EMC < desorption EMC at equal RH (p.580), dry to the desorption isotherm value and treat re-wetting on humid air as creeping toward the higher sorption branch — choose warehouse RH so even the sorption branch stays under the microbial/quality limit.

H11.3 — Model bale/roll/SAP drying with thin-layer Eq 24.5 (★★★★★). Action: Fit M = M_e + (M_i − M_e)·exp(−Kt^N) (p.580) from one drying curve to get K, N; then predict residence time / through-air exposure to reach target M_e for fluff bales and SAP particles.

H11.4 — Always declare wb% vs db (★★★★). Action: Enforce the chapter's convention (p.578): report residual moisture as wb% and db decimal on every pulp/SAP spec and QC certificate to remove ambiguity.

H11.5 — Cost the last moisture points via latent-heat rise (★★★★). Action: Use h*_fg = h_fg[1 + a·exp(−bM)] (p.589) logic to justify staged/lower-temperature finishing (cf. Ch.23 tempering): the final moisture fraction is energetically expensive, so remove it with low-energy air after a temper hold.

H11.6 — Equate ERH = a_w for cross-literature work (★★★★). Action: Map the chapter's ERH (decimal) directly to water activity a_w when reading SAP/pulp stability and microbial-growth literature; the monolayer/oxidation window concept (Ch.22, p.553) then plugs into the same isotherm.

---

======================================================================

## Chapter 25 — Drying of Fruits and Vegetables

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 25 (Jayaraman & Das Gupta) surveys the dehydration of fruits and vegetables as a postharvest preservation strategy, moving from commodity context (§25.1–25.2) through pretreatments (§25.3: alkaline dip, sulfiting, blanching) to an encyclopedic inventory of drying hardware (§25.4: solar, hot-air, fluidized-bed, explosion-puffing, foam, microwave, spray, drum, freeze, osmotic, heat-pump, ultrasonic) and closing on the chemistry of quality loss during drying and storage (§25.5). The arc is practical: perishable, >80%-water plant tissue must be stabilized, and every drying choice trades throughput against volatile/heat-labile retention, texture collapse, and microbial/oxidative shelf life. The chapter's analytical spine is the water-activity (a_w) framework and the glass-transition (Tg) concept, which the authors use to rationalize browning, lipid oxidation, pigment loss, shrinkage, and microbiological stability. For a hygiene-materials reader the value is methodological: the same a_w / sorption-isotherm / Tg / monolayer toolkit that governs dried-food stability applies, with substrate substitution, to residual-moisture specification and warehouse moisture-regain of fluff pulp and SAP.

### 核心观点标题

Hot-air drying causes irreversible textural collapse

Pectin is the structural determinant of rehydration capacity

Water activity is the master stability variable

Monolayer / BET optimum defines the safe storage moisture

Glass transition governs collapse, stickiness and caking

- 

Rate-quality trade-off is explicit and quantified

### 在书中的作用

Chapter 25 sits in the food-drying block (Ch22 fish, Ch23 grain, Ch24 grain properties, Ch25 fruit/veg, Ch26 herbs/tea, Ch27 roots). Relative to Ch24 (which supplies the EMC / sorption-isotherm / thin-layer methodology), Ch25 applies that method to a biologically structured substrate and adds the a_w–microbiology and Tg–collapse dimensions that Ch24 treats only as physics. It is the bridge from "how to measure moisture equilibria" (Ch24) to "how moisture equilibria dictate shelf life and texture" — the layer most reusable for hygiene storage-specification. [inference]

### 卫材行动卡

Overall rating: ★★★★☆ (methodological transfer strong; numeric constants non-portable).

Substrate-difference caveat (per assignment): fruits/vegetables are living, enzyme-active, polysaccharide/cell-wall matrices; fluff pulp (cellulose fibre) and SAP (crosslinked polyacrylate gel) are industrial polymers. The physics of a_w, sorption isotherm, monolayer, and Tg transfers; the values and biochemical pathways (NEB, enzymatic browning, carotenoid oxidation) do not. Do not invent "diaper applications" for carrots.

ACTION CARD 1 — Residual-moisture microbial spec (from Viewpoint 3/§25.5.6 & §25.5.8)

Situation: specifying incoming fluff-pulp or SAP moisture for warehouse storage.

How to apply: adopt the a_w ≤ 0.6 microbial-stability principle; measure pulp/SAP EMC–a_w isotherm (method from Ch24) and set received-moisture so equilibrium a_w stays below the microbial-growth cut-off; keep oxygen/light controlled per §25.5.9.

Expected effect: prevents mold/yeast growth in baled pulp and caked SAP without over-drying energy waste. (p.626, p.628)

ACTION CARD 2 — BET-monolayer target instead of "driest possible" (from Viewpoint 4)

Situation: drying or conditioning absorbent-core furnish.

How to apply: determine the substrate's BET monolayer (Ch24 GAB/EMC method) and target that moisture, not minimum; note some polymers may be most stable near-zero like spinach/cabbage (p.629).

Expected effect: avoids brittle/case-hardened web and re-moistening shock; maximizes storage stability. (p.629)

ACTION CARD 3 — Avoid Tg-collapse in dried hygral coatings (from Viewpoint 5)

Situation: spray-/drum-drying or thermally treating hydrocolloid or SAP-containing layers.

How to apply: keep process/storage temperature below the material's Tg (amorphous state) to prevent stickiness, caking, collapse (p.627); plasticizing solutes (sugars in food; analogous humectants/additives in hygiene) lower Tg and must be accounted for.

- 

Expected effect: stable free-flowing powder / intact web structure. (p.627)

======================================================================

## Chapter 26 — Drying of Herbal Medicines and Tea

### 概述

Chapter 26 (Guohua Chen and Arun S. Mujumdar) is a substrate-oriented survey of how thermal drying degrades or preserves the bioactive value of botanical materials — culinary/medicinal herbs, tea leaves (green/oolong/black), ginseng roots, and cut herbal-medicine pieces. Its governing argument is that for these materials the quality of the dried product (retained active ingredients, colour, aroma) — not merely moisture removal — is the design objective, and that quality is set jointly by temperature, drying method, and moisture-transport path. The chapter opens with the economic scale of herbal medicine (US$12 billion in 1994, p.633), then treats small-quantity household drying, the multi-stage tea processes (withering → killing-out/fermentation → staged hot-air drying), a catalogue of tea dryers (multitray, louver, conveyor-belt, fluidized/vibro-fluidized bed), ginseng shed-drying, and finally a quantitative dataset (Tables 26.2–26.5) on convective vs infrared drying of 27 Chinese herbs. The recurring theme — a quality-vs-rate trade-off governed by a material-specific "allowed temperature" — is the transferable payload for a hygiene reader; the substrates themselves (tea, ginseng, glycyrrhiza) are not diaper materials.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.633–p.644 (PDF p.654–665).

---

### 在书中的作用

Ch.26 sits in the handbook's product-specific applications block (Part IV, food/biological substrates) alongside Ch.27 (roots/tubers) and Ch.28 (osmotic dehydration). It repeatedly defers dryer mechanics to the process chapters — "The reader is referred to Chapter 1 of this handbook for information on selection criteria for dryers" (p.634) — and to fluidized-bed / freeze / microwave chapters for equipment detail. Its distinctive contribution is the quality-degradation lens: where Ch.15–18 optimise heat/mass transfer, Ch.26 insists that transfer intensity must be capped by a biochemical constraint. For the hygiene reader it is a methodological analogue chapter, not an equipment chapter: the substrate difference (living plant tissue with assayable actives) limits direct transfer, but the quality-vs-rate discipline and the staged-temperature and bed-depth findings generalise.

---

### 卫材行动卡

Overall relevance: ★★☆☆☆ (2/5) — method-transferable, substrate-irrelevant.

Where the substrate difference limits transfer (stated plainly): tea leaves, ginseng roots and cut herb pieces are living plant tissue whose value is a set of assayable secondary metabolites. Fluff pulp, SAP and nonwoven webs have no volatile actives, no enzymes and no microbial self-degradation pathway; their "quality" variables are fibre bonding/kink, brightness, SAP gel properties, and residual monomer — not menthol retention. Consequently none of Ch.26's temperature tables, tea process schedules, or dryer descriptions can be transferred numerically to hygiene converting. There is also no diaper, wipe or pulp application anywhere in this chapter, and I have invented none. What does transfer is the methodological architecture of a quality-limited drying process.

H11.1 — Adopt the two-sided temperature window as a QA frame for pulp/SAP drying (★★★). Situation: Setting dryer temperature for wet-laid fluff pulp sheet or post-polymerisation SAP drying. How to apply: Do not treat "lower temperature = safer." Ch.26's mechanism (p.634) — that low temperature prolongs the wet residence time and thereby accelerates a competing degradation pathway — maps onto hygiene analogues: prolonged wet residence promotes microbial growth/odour in pulp bales and slime in wet-end systems, and extends the time for residual-monomer and crosslinker side reactions in SAP. Define an upper bound (thermal damage: fibre hornification, SAP surface-crosslink over-cure) and a lower bound (wet-residence-driven degradation). Expected effect: A defensible two-sided process window instead of a one-sided ceiling.

H11.2 — Replace single set-points with staged temperature programming (★★★). Situation: A drying step where product damage caps throughput (fluff-pulp flash/airborne drying, SAP fluid-bed drying, wipe lotion cure). How to apply: Copy the Radix Glycyrrhizae result (p.641, Table 26.3): the staged 30→77→60 °C schedule delivered mean rate 6.9 g/kg·min and material max 49 °C, versus a 70 °C constant run at 8.6 g/kg·min but material max 63 °C and internal ΔT 28 °C. Front-load heat while the evaporative-cooling sink is strong; ramp down before the falling-rate period. Expected effect: Recovers ~80 % of the high-temperature rate benefit at roughly the thermal stress of a 40–50 °C run — quantitatively the same lever as Ch.15's evaporative-cooling window, but expressed as a schedule.

H11.3 — Treat bed depth as a first-order uniformity variable in any packed-bed hygiene drying (★★★). Situation: Drying SAP granules in a static/shallow fluid bed, or drying baled/roll goods where a packed depth exists. How to apply: Ch.26 measured that 25→50 mm bed depth gave 2.7× drying time and internal ΔT widening from 10 to 18 °C at 66 °C air, with an optimum near 30 mm (p.641). Run the same depth-sweep experiment on the actual granule/mat and pick depth from the ΔT curve, not from throughput alone. Expected effect: Prevents the classic core-wet/surface-over-dried defect (the casehardening analogue) and bounds the property spread within a batch.

H11.4 — Benchmark heating mode against the damage mechanism, not against rate (★★). Situation: Choosing between convective, IR, or IR+vibro-fluidised heating for a heat-sensitive hygiene component (lotion/emulsion coating cure, SAP surface crosslinking). How to apply: Ch.26 shows the mode effect is bidirectional and substrate-specific (Table 26.5, p.643) and that IR's surface-overheating penalty is largely removed by adding particle motion (p.642). Screen both modes experimentally on the actual assay of interest (e.g. residual monomer, CRC/AUL, actives in lotion) rather than assuming the faster mode is worse. Expected effect: Avoids a wrong a-priori mode exclusion; identifies the IR+agitation combination as the candidate for surface-sensitive particulates.

---

======================================================================

## Chapter 27 — Drying of Potato, Sweet Potato, and Other Roots

### 概述

Chapter 27 (Sablani & Mujumdar) is a product-specific drying review for starchy/root/bulb food commodities — potato (Solanum tuberosum), sweet potato, mushrooms, peanuts, and ginseng — within the handbook's food/biological applications block (Part IV). Its logic is the quality-vs-rate trade-off under a two-sided temperature window: too hot destroys structure, colour, and heat-labile actives; too cold prolongs residence, accelerating enzymatic browning, microbial growth, and internal degradation. The body compiles (a) preprocessing (peeling, blanching, sulfiting, osmotic pretreatment), (b) tabulated physical/thermal/thermodynamic properties (moisture diffusivity, activation energy, BET/GAB monolayer, conductivity, specific heat, thermal diffusivity — Tables 27.3–27.12), (c) drying methods per product form (diced, strips, flakes, starch, granules, chips; conventional/osmotic/vacuum/freeze/heat-pump/microwave/IR), and (d) quality outcomes (optical, physical, nutritional). For the hygiene reader this is a ★★☆☆☆ chapter: the substrate is a starch-filled cellular food, fundamentally unlike fluff/SAP polymeric webs, so no diaper application is invented below; but the transferable science — quality-vs-rate coupling, bed-depth → internal-ΔT → time interaction, staged/sinusoidal temperature profiles to suppress colour and active-compound loss, and osmotic dehydration used as a load-reducing pretreatment — maps onto absorbent-core and pulp-drying thinking.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.645–p.662 (PDF p.666–683).

---

### 在书中的作用

Ch.27 is a Part IV product/application chapter sitting beside Ch.26 (herbal/tea) and Ch.28 (osmotic dehydration). It complements the dryer-specific chapters (Ch.14 inert-bed, Ch.15 impingement, Ch.17 conveyor, Ch.18 IR) by showing how those dryers are actually deployed on a real, messy, quality-sensitive food substrate, and it supplies the handbook's most complete tabulated property dataset (Tables 27.3–27.12) for a biological material. For the hygiene engineer its role is as a transferable-methods casebook: the quality-vs-rate window, bed-depth/time coupling, staged and oscillatory temperature programming, and osmotic pretreatment are demonstrated on potato and can be borrowed conceptually. Substrate-difference limit: potato is a starch-filled, enzyme-active, cellular tissue; fluff pulp is refined cellulose fibre and the SAP core is a crosslinked polyelectrolyte gel. The numerical property tables and the food-specific degradation chemistry do not transfer — only the engineering patterns (control of rate vs quality, pretreatment decoupling, staged thermal programs) do. No diaper application is asserted.

---

### 卫材行动卡

Rating for this chapter: ★★☆☆☆ — substrate is food starch/cellular tissue; numeric data do not transfer. The engineering patterns below are the genuinely reusable part. No diaper application is invented; statements are limited to transferable method.

H11.1 — Borrow the two-sided temperature window for active-loaded webs (★★★). Action: Where a wipe carries a heat-labile active, treat ginseng's 6°C-overshoot → >25% loss (p.660) as the quantitative precedent: set the dryer's temperature band from the active's degradation onset, not from generic throughput, and validate with a stability assay.

H11.2 — Use staged cooling inside one dryer (★★★). Action: Mirror the diced-potato two-stage profile (93–127°C → 71–105°C → 55–82°C, p.650) when a hygiene web needs a high-flux surface phase followed by a gentle bound-moisture tail; add a final low-RH/desiccant conditioning zone to reach the true storage moisture floor (cf. 3–4% wb sorption polish, p.650).

H11.3 — Try oscillatory temperature to protect colour/actives (★★★). Action: The square-wave T that cut potato colour change ~87% (p.655) is a control-strategy idea: test a sinusoidal/square air-temperature program on colour- or active-sensitive webs before assuming a fixed setpoint is optimal.

H11.4 — Treat preprocessing as a first-order quality lever (★★). Action: As blanching/sulfiting lock potato colour before the thermal load (p.648), pre-stabilize hygiene-web additives (antioxidants, buffers) upstream of the dryer rather than compensating with lower dryer temperature and longer residence.

H11.5 — Recognise shrinkage as a residence-time effect (★★). Action: Low-T/long-residence drying shrank potato more than high-T (p.656); for dimensionally-critical nonwoven/airlaid sheets, prefer a higher-temperature shorter-residence profile if the active allows, to limit collapse.

H11.6 — Use osmotic pull-out as a load concept (link to Ch.28) (★★). Action: The potato result (84→60% wb water removed osmotically before thermal drying, p.654) previews Ch.28's water-out/solute-in physics; consider an osmotic/dewatering pre-step to cut thermal-dryer load where a semipermeable boundary is available — full mechanism in Ch.28.

---

======================================================================

## Chapter 28 — Osmotic Dehydration of Fruits and Vegetables

### 概述

Chapter 28 (Lewicki & Lenart) is the handbook's most physically-fundamental water-removal chapter: it treats osmotic dehydration (OD) — the removal of water from plant tissue immersed in a hypertonic solution — as a countercurrent mass-transfer process across a semipermeable boundary driven by osmotic pressure. Its logic is built on chemical-potential/osmotic-pressure thermodynamics (§28.2.1), plant-cell anatomy as the transport architecture (§28.2.2–28.2.3), and a candid review of why simple Fickian diffusion models only partly capture the process (§28.2.4). The body then covers design (predehydration pretreatment, osmoactive substance, processing parameters, solution management, energy, §28.3) and equipment (immersed/sprayed/solid/reduced-pressure, §28.4) and product characteristics (§28.5). For the hygiene reader this is a ★★★★★ chapter: it is the single most direct bridge to superabsorbent-polymer (SAP) science. The osmotic pressure Π = RT·ln a_w, the semipermeable membrane, and the electrolyte/ion effect on Π are exactly the physics family of SAP swelling/deswelling governed by Flory–Rehner equilibrium and Donnan osmotic pressure in a crosslinked polyelectrolyte network. The "water-out / solute-in" countercurrent flux with osmotic pressure as the driver is the same phenomenon as SAP taking up water against an elastic network resistance.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.663–p.679 (PDF p.684–700; REFERENCES to p.686).

---

### 在书中的作用

Ch.28 sits at the physics core of the handbook's water-removal science, complementing Ch.26 (herbal/tea convective+IR) and Ch.27 (potato, where OD appears only as a brief pretreatment). It is the chapter that actually explains why OD works — osmotic pressure across a semipermeable boundary — and therefore it is the missing-link chapter for the hygiene reader: it supplies the exact physical vocabulary (Π = RT ln a_w, chemical potential, semipermeable membrane, semipermeable boundary, countercurrent flux, ion/electrolyte effect on Π) that describes SAP behaviour. It pairs with the dryer-engineering chapters (Ch.14–18) by showing a non-thermal, phase-change-free dewatering alternative. Substrate note: here the semipermeable boundary is the plasmalemma and the osmotic reservoir is the vacuole; in an SAP the boundary is the crosslinked polyelectrolyte network and the reservoir is the gel phase. The governing equations are identical. No diaper "application" is fabricated; the linkage is mechanistic.

---

### 卫材行动卡

Rating for this chapter: ★★★★★ — it is the direct physical-chemistry bridge to SAP (crosslinked polyelectrolyte superabsorbent) behaviour; the osmotic-pressure/semipermeable-boundary/ion-effect framework is substrate-independent and maps one-to-one onto SAP swelling/deswelling.

H11.1 — Use Π = RT·ln a_w as the SAP swelling driver (★★★★★). Action: When scoping SAP uptake capacity/rate, start from the osmotic-pressure law Ch.28 derives (Eq.28.1–28.3, p.664) and the Flory–Rehner balance (mixing/osmotic pressure vs network elastic pressure). Treat external salt/urine Π as the counter-pressure that caps swell — the same role Ch.28 assigns to surround Π in plasmolysis (p.666).

H11.2 — Engineer the semipermeable boundary like the artificial membranes (★★★★★). Action: Ch.28 shows pectin/starch/alginate coatings reduce solute incorporation while keeping water flux (p.670–671). Mirror this when tuning SAP: surface crosslink density / coating controls uptake-rate vs leakage (gel-blockage, bleeding) — the boundary, not the bulk, is rate-limiting (p.669).

H11.3 — Expect electrolyte (Donnan) collapse, not just dilution (★★★★★). Action: Ch.28's "electrolytes give higher osmotic pressure because each ion affects solvent chemical potential" (p.664) is the Donnan principle. Predict that SAP capacity collapses in saline/urine not by simple dilution but by Donnan osmotic-pressure neutralization of the fixed –COO⁻ charges; validate against AUL (absorption under load) in synthetic urine.

H11.4 — Countercurrent flux ⇒ model water-in and ion-exchange together (★★★★). Action: As Ch.28 warns that water-out and solute-in fluxes interact and can't be split into independent diffusivities (p.667), model SAP uptake and salt/ion ingress as coupled countercurrent fluxes, not separate steps — especially under load where the network resistance dominates (p.669).

H11.5 — Osmotic pre-dewatering saves latent heat (★★★★). Action: Ch.28's energy result (no phase change; ~½–1/5 of convection energy, p.674–675) supports using a liquid-water removal / dewatering pre-step (e.g., mechanical press, membrane, or osmotic contact) ahead of any thermal dryer in fluff/pulp lines, exactly as Ch.27 used OD as a potato pretreatment.

H11.6 — 20–40°C is the selective window; raise T only if solute-ingress is acceptable (★★★). Action: Ch.28's best water-loss:solids-gain ratio sits at 20–40°C, with higher T driving more solute in (p.672). For any temperature-sensitive hygiene dewatering, keep to the lower window unless the co-transferred species is benign.

H11.7 — Cap sample/bed thickness to keep boundary-limited flow (★★★). Action: Lenart & Lewicki's "thickness should not exceed 10 mm" (p.670) and the extracellular-space-limiting effect (p.669) argue for thin, high-surface-area forms (e.g., airlaid/through-air mats, thin SAP layers) so osmotic/boundary transport, not bulk diffusion, sets the rate.

---

======================================================================

## Chapter 29 — Drying of Pharmaceutical Products

### 概述

Chapter 29 (Zdzisław Pakowski and Arun S. Mujumdar) treats drying as the GMP-governed, contamination-intolerant, thermally-cautious stage of drug manufacture — products that must be dried after intermediate synthesis, final synthesis, and dosage-form manufacture, often at low tonnage / high value where energy cost is secondary to product integrity. The chapter's logic is selection-driven: it opens by stating that product deterioration (microbial infection, oxidation, thermal decomposition, metallic or solvent contamination) "must be avoided at any cost" (p.687), then builds a material-classification scheme (Sazhin/Rebinder, by minimum pore diameter → moisture–material bond strength) to match products to dryers, surveys physical/thermal/sorptive properties (particle size, first-order thermal decomposition via Arrhenius, sorption isotherms and hysteresis), catalogues dryer families (batch ovens, fluid bed, band, turbo-tray, pneumatic, cyclone, spouted, vibrated, spray, drum, vacuum, freeze), and closes with granulation, dosage forms, technological data tables, aseptic conditions (HEPA, class 100, sterilization), and solvent-recovery/closed-cycle drying. For the hygiene reader this is a ★★★★ chapter: its GMP residual-moisture control, aseptic/cleanroom discipline, sorption-isotherm reasoning, and closed-cycle/solvent-safety logic transfer directly to medical-grade nonwovens and lotion/active-coated wipes.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.687–p.710 (PDF p.708–731).

---

### 在书中的作用

Ch.29 is the high-value, GMP/aseptic, contamination-sensitive drying chapter — the quality-assurance pole opposite Ch.32 (bulk, energy-cheap peat/biofuels). It complements Ch.4 (sorption isotherms), Ch.17 (conveyor/continuous webs), Ch.18 (infrared cure), and Ch.33 (fibrous bound moisture); its desorption-isotherm and bond-energy ladder feed directly into the moisture-spec reasoning those chapters assume.

---

### 卫材行动卡

H11.1 — Adopt the noncompromise contamination clause for medical-grade lines (★★★★). Action: Mirror p.687's "must be avoided at any cost" for surgical drapes / medicated wipes: define bioburden, oxidation, metal-particle, and residual-solvent acceptance as zero-tolerance critical limits with polished-stainless/inert construction.

H11.2 — Use desorption isotherms + bond-energy ladder for moisture spec (★★★★). Action: Build the final-water-content spec from desorption isotherms (p.691) and the capillary→colloidal bond ladder; set dryer T/residence so bound (fibre/SAP) moisture, not just free surface water, reaches target — prevents rewet/clumping in the pad.

H11.3 — Run an Arrhenius loss check on every active before drying (★★★). Action: For lotion/active-coated wipes, take E/A of the active (or a conservative proxy), set acceptable loss (e.g., 5%), and back out the max web temp/residence (p.691 worked example) — reject dryer settings that exceed it.

H11.4 — Apply aseptic/HEPA/class-100 discipline to cleanroom converting (★★★★). Action: For medical nonwovens, install HEPA (99.97% @ >0.3 µm) + class-100 laminar-flow converting and a 200–250°C sterilization/validation protocol (p.704–707) on contact surfaces; eliminate sliding/rotating parts that shed metallic contamination (p.707).

H11.5 — Use closed-cycle inert gas where solvent/active is flammable or toxic (★★★). Action: Where wipe lotion or coating uses organic solvent or toxic actives, run a closed N₂ loop with condenser recovery (p.708) and compute makeup-gas purge from evaporation rate to avoid explosive mixtures.

H11.6 — Watch sticky/defluidization of fine powders (★★★). Action: Fine SAP fines or additive powders that plasticize in residual moisture can defluidize a fluid bed (p.690); set inlet T below the stick-point or pre-agglomerate before fluidized drying.

---

======================================================================

## Chapter 30 — Drying of Nanosize Products

### 概述

Chapter 30 (Baohe Wang, Li Xin Huang, and Arun S. Mujumdar) is the book's nanomaterials-drying chapter, concerned with two failure modes that are absent or trivial at macroscopic scale: (i) cracking/collapse of the fragile porous gel skeleton and (ii) irreversible agglomeration of nanoparticles during solvent removal. The chapter's logic: nanomaterials are defined by their <100 nm features (p.711); because nanoparticles "tend to agglomerate and properties... are adversely affected if we do not choose appropriate drying methods" (p.712), drying must preserve dispersion. It first builds the solvent-evaporation mechanism (Scherer's three periods: constant-rate → first falling-rate → second falling-rate) and the capillary-pressure theory P = 2σ cosθ / r as the root cause of both cracking and agglomeration, then surveys direct, solvent-replacement, and modified drying families with quantitative product tables (TiO₂, MgO, BaTiO₃), and closes with selection rules and the open challenge of agglomeration + nanoparticle inhalation safety. For the hygiene reader this is a ★★★★ chapter: its capillary-pressure and particle–particle-force framework transfers directly to SAP (sodium polyacrylate) fines handling, nanocellulose/CMC dewatering, agglomerate control and redispersibility.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.711–p.726 (PDF p.732–747).

---

### 在书中的作用

Ch.30 is the small-feature / colloidal-force / powder-agglomeration pole of the book, complementing Ch.31 (ceramics: shrinkage/cracking in rigid porous bodies — same capillary-stress family), Ch.33 (fibrous: bound water, inter-/intra-fibre, shrinkage/hornification), and Ch.4 (sorption, pore structure). Its capillary-pressure equation is the quantitative spine that Ch.31's cracking and Ch.33's shrinkage both implicitly use.

---

### 卫材行动卡

H11.1 — Use P = 2σ cosθ / r_p to size SAP-fines/nanocellulose agglomeration risk (★★★★★). Action: Treat sub-micron SAP fines and nanocellulose by Eq. (30.1): because r_p is tiny, capillary pressure is enormous at the falling-rate transition — keep σ low (avoid pure-water dewatering where possible) and/or raise θ (hydrophobic treatment) to suppress clumping during flash/pad dewatering.

H11.2 — Redispersibility depends on bond type — test before declaring "reversible" (★★★★). Action: Classify any observed agglomerate as H-bond/capillary (shear-redispersible) vs chemical Me–O–Me / crystal-bridge (permanent, p.715). For nanocellulose/SAP fines, validate redispersibility by mild shear rather than assuming it recovers.

H11.3 — Exchange water for low-surface-tension solvent or use freeze to protect nanostructure (★★★★). Action: Where nanocellulose/CMC gels must keep high surface area, apply solvent-replacement (EtOH) or freeze-drying (water expansion separates particles, p.716) instead of direct oven drying, which collapses pores (Table 30.4 proof).

H11.4 — Surface-modify to θ≈90° to minimize capillary pull (★★★★). Action: Mirror Deshpande/TMCS treatment (θ→~90°, Table 30.6, p.721): hydrophobically treat SAP-fine or nanocellulose surfaces so capillary pressure collapses and ambient-pressure drying yields aerogel-like low-bulk product.

H11.5 — Watch the critical point; it is a mechanical peak, not just a rate change (★★★). Action: In pad/film drying of fine-particulate coatings, expect max stress at the constant→falling-rate transition (p.713); back off flux there to avoid microcracking/collapse of the web.

H11.6 — Engineer dust-exposure controls for fine powders (★★★). Action: Treat SAP fines / nanocellulose as inhalable/dermally-ingestible (p.725): enclose dewatering/handling, collect emissions, and set PPE — the chapter's safety flag applies directly to plant converting.

---

======================================================================

## Chapter 31 — Drying of Ceramics

### 概述

Chapter 31 (Yoshinori Itaya, Shigekatsu Mori, and Masanobu Hasatani) treats drying of molded ceramics — a rigid porous body whose shape must be preserved through drying, where the dominant failure modes are shrinkage, cracking, warping, sagging, and internal stress. The chapter's logic: ceramic drying "is usually carried out slowly in order to avoid undesirable cracks and deformations" (p.727); it is bottlenecked by four difficulties (limited initial rate, shrinkage-induced failure, mold-design prediction, nonuniform drying). The body then builds the suction-potential taxonomy (capillary vs osmotic), the shrinkage mechanism (water-film thickness between submicron particles, osmotic suction), the moisture-movement model (liquid/vapor diffusion, Darcy, effective diffusivity, full heat/mass-balance and constant/falling-rate design equations), the dryer families (tunnel, band, batch, IR, microwave, electric-current), and the failure/deformation mechanics (viscoelastic/plastic response, Biot/Lewis numbers, tensile-stress peaks from fast surface dry-up). For the hygiene reader this is a ★★★★ chapter: it is the book's clearest exposition of constant-rate→falling-rate transition, capillary/osmotic shrinkage stress, and case-hardening/cracking in a rigid porous sheet — the exact mechanistic family behind web cracking and case hardening in nonwovens/tissue.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.727–p.740 (PDF p.748–761).

---

### 在书中的作用

Ch.31 is the rigid-porous-body shrinkage/cracking reference — the constant/falling-rate + internal-stress family that Ch.30 (capillary cracking of gels), Ch.33 (fibrous shrinkage/hornification), and Ch.4 (moisture potential) all draw on. It supplies the mechanical (Biot/Lewis, tensile-stress) layer that the food/fibre chapters treat only phenomenologically.

---

### 卫材行动卡

H11.1 — Cap the initial drying rate to protect web shape (★★★★). Action: Honor difficulty (1) (p.728): don't over-drive flux at line start; the constant-rate window is short and over-fast starts cause falling-rate stress — set impingement/through-air ramp so the nonwoven/tissue web doesn't curl or crack.

H11.2 — Treat submicron fibre shrinkage as osmotic, not capillary (★★★★★). Action: For cellulose/nanocellulose mats (fibres  µm), use the osmotic-suction model (p.730): shrinkage is double-layer/electrochemical, so manage it via electrolyte/charge and drying-rate, not just pore-capillary thinking.

H11.3 — Avoid case hardening: no fast surface dry-up over a wet core (★★★★★). Action: Implement the verbatim rule (p.739): prevent rapid surface set while interior stays wet; if surface dries first, back off flux and switch to gentler/falling-rate conditions to avoid crack/warp.

H11.4 — Relieve stress by raising internal moisture mobility, not just h (★★★★). Action: Apply the Bi/Le rule (p.839): add through-air/suction/steam to boost internal 1/Le (moisture migration) rather than only increasing external heat-transfer — the justification for impingement+suction synergy on heat-sensitive webs.

H11.5 — Use IR in the falling-rate period only, with power control (★★★). Action: Mirror ceramic IR practice (p.737): apply IR/convective boost in the falling-rate period for rate without case hardening; control power so surface doesn't over-dry — relevant to wipe coating cure.

H11.6 — Expect anisotropic shrinkage from fibre orientation (★★★). Action: Note Williamson/Cox finding that shrinkage is greater perpendicular than parallel to particle orientation (p.732); for oriented nonwoven webs, anticipate MD/CD dimensional differences and design mold/draw accordingly.

---

======================================================================

## Academic Chapter Analysis — Chapter 32: Drying of Peat and Biofuels

### 概述

Chapter 32 treats drying as a pre-combustion energy-systems problem rather than a materials-science problem. Wimmerstedt frames peat and biofuel drying around three drivers: (1) lowering fuel moisture to raise boiler efficiency and capacity; (2) meeting process thresholds (gasification <10–15% MC, suspension firing <15% MC, briquetting 10–20% MC); (3) mitigating storage degradation. The chapter surveys thermodynamics of fuel drying (flue-gas, superheated-steam, double-effect/Peco), four dryer families (rotary, cascade, pneumatic/flash, fluid-bed steam), environmental VOC/terpene emissions, and operation/availability data, closing with equilibrium (sorption isotherms) and a candid admission that kinetics are "experience-based."

For the hygiene reader this is the weakest of the six assigned chapters: it deals with coarse, non-hygroscopic, non-absorbent bulk solids and with plant-scale energy economics, not with capillary/colloidal water in fibrous or polymeric structures. The genuine, if modest, transfer point is the free-water vs. cell-bound-water (below ~0.3 MC) distinction and the statement that wood is only moderately hygroscopic — directly analogous to fluff-pulp bale-moisture behaviour.

### 在书中的作用

Ch32 sits in the "specific materials" block of the Handbook. It complements the energy-and-bulk-solid drying chapters and provides a counterweight: whereas Ch31/Ch33 emphasize drying-induced damage (cracking, shrinkage, hornification), Ch32 emphasizes drying as a net energy gain with negligible material damage because the feed is inert, coarse, and non-porous at the relevant scale. It is the chapter where "don't over-dry" is driven by energy payback, not by product quality.

### 卫材行动卡

Overall relevance: ★★☆☆☆ (weak — energy/bulk-solids; one genuine bridge).

Action Card H32-1 — Bale-moisture threshold discipline. Insight: drying past a threshold yields marginal returns (p. 744). Action: Specify fluff-pulp bale MC by storage-stability + converting-need, not by a blanket "as dry as possible"; quantify the energy cost of pushing MC below the natural equilibrium before committing. → 卫材相关性★★☆☆☆｜Avoid paying evaporative-drying energy for MC reductions that mechanical pressing + equilibration already achieve.

Action Card H32-2 — Free vs. cell-bound water language for pulp. Insight: wood's cell-bound water appears only below ~0.3 MC; above that it is free water (p. 750). Action: When auditing pulp supplier MC specs, separate "free surface water" (cheap to press out) from "cell-bound" (needs energy); align incoming-MC acceptance with this split. → 卫材相关性★★★☆☆｜Gives procurement a physically correct vocabulary to challenge supplier MC claims.

Action Card H32-3 — Corrosive-condensate vigilance (transfer to steam dryer audits). Insight: acidic condensate demands stainless/clad construction (p. 750). Action: If your line uses any steam/condensate loop for web drying, audit for condensate acidity (volatiles from additives/fragrances). → 卫材相关性★★☆☆☆｜Pre-empts corrosion failures in hygiene converting dryers.

Non-transfer (explicit): boiler integration, terpene VOC abatement, suspension-firing MC limits, Peco/MVR economics — not applicable to absorbent-product manufacturing.

======================================================================

## Academic Chapter Analysis — Chapter 33: Drying of Fibrous Materials

### 概述

Chapter 33 is the single most relevant chapter in the assignment for a hygiene-materials engineer. Keey treats fibres as elongated polymeric particles and systematically develops the physics of fibre–water interaction: sorption isotherms (BET, Henderson), bound vs. free water, anisotropic swelling/shrinkage, single-fibre diffusion (Fick's laws in cylindrical coordinates), the response of a fibre mass to hygrothermal change (Henry–Nordon fronts), convective/through-circulation/impingement drying, pulp-and-paper machine drying, and superheated-steam drying. The chapter closes with the explicit statement that press-drying bonds wet wood webs when the temperature exceeds the glass-transition point of lignin (~150 °C) — a direct polymer-physics anchor.

For the diaper/wipe engineer this chapter maps onto: fluff-pulp bale moisture and redrying damage (hornification), nonwoven/web through-drying, SAP–cellulose interfibre water, and the energy–quality trade-off of thermal drying on cellulosic structures.

### 在书中的作用

Ch33 is the definitive "fibrous/porous polymeric" anchor of the Handbook's materials block, directly complementing Ch31 (ceramics: rigid porous, shrinkage-cracking) and Ch28/29 (food/pharma). It is the only chapter that makes the polymer-physics link explicit (lignin Tg, plasticization). In the hygiene context it is the parent reference for fluff-pulp behaviour; Ch30 (nanosize) and Ch32 (peat) are peripheral by comparison.

### 卫材行动卡

Overall relevance: ★★★★★ (core chapter).

Action Card H33-1 — Specify bale MC against the FSP bound/free split. Insight: bound water (heat of sorption ½–¼ ΔH_vap) cannot be pressed out; free water can (p. 755–756). Action: Set fluff-pulp acceptance MC so that incoming water is predominantly free (above interpolated FSP for that pulp); reject "dry but bound-water-rich" claims by measuring equilibrium MC, not just oven MC. → 卫材相关性★★★★★｜Prevents paying evaporative energy for water that pressing/equilibration already removes; protects converting yield.

Action Card H33-2 — Quantify hygroscopicity from Table 33.1 for fibre selection. Insight: woodpulp 0.034/0.062/0.25 vs viscose 0.0555/0.101/0.46 at RH 0.2/0.5/1.0 (p. 755). Action: Use these equilibrium values to predict in-package MC drift and SAP–pulp partitioning under storage RH. → 卫材相关性★★★★★｜Lets you size SAP vs pulp ratio from sorption equilibrium rather than guesswork.

Action Card H33-3 — Treat every redry as hornification risk. Insight: sorptive (activated) diffusion + strong bonds at low MC (p. 757); "permanent set" irreversible creep (p. 756). Action: Minimise pulp re-wetting/redrying cycles in procurement and broke recovery; audit supplier drying history as a quality attribute. → 卫材相关性★★★★★｜Directly preserves pulp swellability = core absorbent capacity.

Action Card H33-4 — Keep fluffy fluff below lignin Tg; reserve ≥150 °C for bonded structures. Insight: press-drying bonds at lignin Tg+25–50 °C ≈ 150 °C (p. 773). Action: Cap thermal exposure of non-bonded airlaid/woodpulp at <150 °C to preserve swellability; use >150 °C deliberately only for wet-laid/bonded cores or paper. → 卫材相关性★★★★★｜Controls the swellability-vs-bonding trade-off at the process-design level.

Action Card H33-5 — Model webs as non-capillary; use characteristic drying curve. Insight: touching fibrous assemblies lack a true constant-rate period (p. 762); normalized f = A·Fⁿ with n≈0.6 (wool), n≈2/3 (thin wood) (p. 763); internal resistance negligible  mm thickness. Action: Build through-dryer/impingement models on the characteristic-curve form, not capillary-porous assumptions; exploit airflow reversal to even MC (p. 768). → 卫材相关性★★★★☆｜Improves nonwoven/airlaid dryer design and reduces over-drying.

Action Card H33-6 — Steam-drying caution: water enhances degradation above inversion. Insight: inversion 160–230 °C; water present accelerates thermal damage (p. 773). Action: If trialling superheated-steam drying of cellulosic stock, stay below inversion or below lignin-Tg-sensitive thresholds and verify brightness/strength. → 卫材相关性★★★★☆｜Avoids hidden strength/yellowness loss in hygiene-grade cellulose.

Action Card H33-7 — Pulp-machine lesson: 70% water removed by pressing, not heat. Insight: press section removes ~70% of water before drying; sheet emerges ~8% MC (p. 770); ~⅔ of multicylinder heat goes to evaporation, 22% lost from cylinders (p. 771). Action: In any converting line, maximise mechanical dewatering ahead of thermal drying. → 卫材相关性★★★★☆｜Energy-cost discipline directly portable to wet-laid hygiene lines.

======================================================================

## Chapter 34 — Drying of Textile Products

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 34 (Carr, Lee & Ok) surveys drying across the textile industry and is directly adjacent to nonwoven-web drying for the hygiene reader: the authors explicitly define "textile" to include nonwoven fabrics (p.779). The chapter classifies drying into predrying (mechanical or thermal, to ~30% moisture regain) and final thermal drying, then catalogs mechanical dewatering (squeeze, vacuum, centrifuge) and thermal dryers (conduction/steam-can, convection circulating-air, through-air, impingement, IR, RF/microwave). Its distinctive assets are quantitative benchmarks: energy per kg water by method (squeeze 58 → vacuum 700 → steam-can 4700 → convection 7000 kJ/kg, Table 34.1), fibre physical/thermal properties (Table 34.2), and an extensive moisture-regain absorption/desorption table (Table 34.3) showing large hygroscopic hysteresis for hydrophilic fibres. The recurring engineering lesson is "remove as much water mechanically as possible" because mechanical dewatering is far cheaper than thermal.

### 核心观点标题

"Textile" includes nonwovens; drying is the energy bottleneck

Mechanical dewatering is far cheaper than thermal

Predry to ~30% regain; final drying fixes dimensions via heat-setting

Hydrophilicity dictates how low mechanical dewatering can go

Through-air drying needs permeability; low-perm webs switch to impingement

- 

IR is for predrying only (scorch risk); RF gives uniform, low-overdry drying

### 在书中的作用

Ch34 is the "engineered fibrous web" companion to Ch33 (natural fibres/pulp) and Ch35 (paper/pulp webs). It generalizes the conduction/through-air/impingement vocabulary to fabrics and explicitly embraces nonwovens, making it the closest sibling to hygiene nonwoven processing. It feeds the same heat-transfer toolkit used in Ch35 and shares the sorption/hysteresis physics of Ch33.

### 卫材行动卡

Overall relevance: ★★★★☆ (strong; adjacent to nonwoven web drying).

Action Card H34-1 — Specify substrate drying method & verify the permeability gate. Insight: p.786 through-air "good option" only if air permeability is adequate; low-perm → impingement. Nonwovens "particularly" use suction/perforated-drum through-air. Action: Request the substrate's air-permeability (CFM) and the dryer type; confirm a through-air web wasn't force-dried at excessive fan energy (cost/quality risk). → 卫材相关性★★★★★｜Air permeability decides dryer choice and achievable rate for your nonwoven.

Action Card H34-2 — Drive wet-pickup reduction mechanically before thermal drying. Insight: p.779 "as much water as possible is usually removed mechanically"; Table 34.1 squeeze 58 vs convection 7000 kJ/kg. Action: For wipe converting, specify nip + vacuum extraction ahead of any oven; set a residual-moisture-regain target and audit supplier dewatering. → 卫材相关性★★★★★｜120× energy gap; the dominant cost lever in substrate making.

Action Card H34-3 — Use moisture-regain tables to size SAP vs fibre water split. Insight: p.782 Table 34.3 — at 65% RH viscose rayon ~14–16% vs PET ~0.4–0.5% regain; hysteresis large for hydrophilic. Action: Pick substrate fibre mix from equilibrium regain to control in-package MC drift and SAP partitioning under storage RH. → 卫材相关性★★★★★｜Quantifies fibre water affinity that competes with SAP for fluid.

Action Card H34-4 — QC the heat-set / dimensional-stability history. Insight: p.781 tenter-frame convection oven "fixes the width … dimensional stability"; heat-set is a crystallisation step. Action: For nonwoven substrates requiring flatness/dimensions, specify heat-set temperature against the fibre Tm/Tg window and require dimensional-stability data (MD/CD shrink). → 卫材相关性★★★★☆｜Prevents curl/shrink in the final article.

Action Card H34-5 — Avoid scorch: keep IR to predrying; watch overdry. Insight: p.788 IR "not normally used to accomplish final drying because … danger of scorching or burning"; RF gives "reduced chance of overdrying." Action: If a supplier uses IR, confirm it is predry-only and that coating/laminate webs were not heat-damaged; prefer RF for bulky uniform drying. → 卫材相关性★★★★☆｜Protects substrate strength and appearance.

Action Card H34-6 — Benchmark supplier energy/cost from the energy ladder. Insight: p.781 Table 34.1 quantifies method energy; p.788 electricity 3–5× gas for IR. Action: When comparing substrate quotes, ask which dewatering/drying sequence is used; a mechanically-aggressive supplier should be cheaper and greener. → 卫材相关性★★★★☆｜Energy mix is a negotiable cost/ESG differentiator.

======================================================================

## Chapter 35 — Drying of Pulp and Paper

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 35 (Polat & Mujumdar) is the single most commercially relevant chapter in this Handbook for a fluff-pulp / paper-grade procurement strategist. It treats papermaking as fundamentally "a massive dehydration operation" and separates pulp drying from paper drying. The paper-drying half develops the multicylinder (conduction) dryer section, its stacked heat-transfer resistances, steam-and-condensate systems, pocket ventilation, and the full menu of alternatives — Yankee/impingement, through-air, floater, radiant/IR, and the novel thermomechanical consolidators (press, Condebelt, impulse). The pulp-drying half covers conventional cylinder/air-floater, flash, and steam drying, and—critically for hygiene buyers—names the lower-moisture-bound thermal cross-linking that destroys fiber reconstitutability. The through-line is the energy/quality/speed trade-off: drying is "the most costly and energy-intensive step" yet removes the least water in absolute terms.

### 核心观点标题

Drying is the costliest step yet removes the least water

Cylinder drying is conduction-limited by stacked resistances

Pocket ventilation and condensate control are the hidden throughput levers

Drying strategy sets the strength–bulk–swellability trade-off

Thermomechanical drying (press/Condebelt/impulse) builds bonds and cuts energy

- 

Flash drying below the lower moisture bound cross-links the fiber (the hornification clause)

### 在书中的作用

Ch35 is the Handbook's core "cellulosic web" chapter and the direct industrial counterpart to Ch33 (Drying of Fibrous Materials). Where Ch33 develops the molecular/polymer physics of fibre–water (sorption, bound/free split, lignin-Tg bonding), Ch35 supplies the machine-scale realization: cylinder conduction resistances, press/Condebelt/impulse consolidation, and the pulp-flash hornification clause. It complements Ch34 (textiles) on Yankee/through-air and Ch36 (wood) on the upstream fibre source. For the hygiene reader it is the bridge from fibre science to the supplier's actual drying line.

### 卫材行动卡

Overall relevance: ★★★★★ (core procurement chapter).

Action Card H35-1 — Interrogate the flash-dryer lower-moisture-bound control. Insight: p.815 — overheating below the lower moisture bound causes "thermal cross-linking that makes reconstitution of the original fiber difficult"; suppliers hold pulp <70°C. Action: When qualifying a flash-dried fluff supplier, demand the two-stage inlet/exit temperatures and the controlled pulp temperature; require a certificate that final-stage pulp temperature stayed below the cross-linking window. → 卫材相关性★★★★★｜Directly governs defibration energy, knot content and pad integrity of the fluff you buy.

Action Card H35-2 — Make defibration energy a drying-history KPI. Insight: p.815 reconstitution difficulty; p.810 press/impulse bond-building. Action: Require specific refining/defibration energy (kWh/BDt) and CSF (Canadian Standard Freeness) on the CoA; trend it lot-to-lot. A rising trend signals creeping over-dry/over-temp history. → 卫材相关性★★★★★｜Defibration energy is the dollar-and-performance proxy for hidden hornification.

Action Card H35-3 — Specify the strength–bulk–swellability target, not just "fluff pulp." Insight: p.799 restrained drying = high tensile/low stretch/compact; p.804 tension-free = high bulk/stretch/TEA; p.802 through-air = soft high-bulk. Action: For diaper fluff specify bulk (cm³/g), tensile, and wet-collapse; for wipes substrate specify bulk + TEA + softness. Match the drying method (through-air/flash vs cylinder) to the target. → 卫材相关性★★★★★｜Drying method is the dominant determinant of bulk vs strength you are buying.

Action Card H35-4 — Screen knot/shive and rewet as hornification symptoms. Insight: p.815 cross-linking → poor reconstitution; [inference] cross-linked fibres resist defibrating into fines, raising screen rejects and weakening rewet. Action: Add screen-rejects (Pulmac/shive) and rewet (gravimetric) to supplier specs; reject lots exceeding baseline. → 卫材相关性★★★★★｜Converts the invisible drying defect into measurable acceptance criteria.

Action Card H35-5 — Specify shipping MC against the bound/free split and require equilibrium-MC data. Insight: p.814 market pulp "drying up to 10% moisture (90% fiber, 10% water)"; Ch33 FSP bound/free split. Action: Set acceptance MC so incoming water is predominantly free (pressable/equilibrated out), and request equilibrium-MC at storage RH to predict in-bale drift. → 卫材相关性★★★★★｜Prevents paying evaporative energy for water pressing/equilibration already removes.

Action Card H35-6 — Price the drying-method cost advantage (steam dryer). Insight: p.815 first CTMP steam-dryer install "showed a 30% reduction in overall drying costs per ton of market pulp compared with an equivalent-size flash dryer"; claimed "minor or no effect on pulp quality." Action: When a supplier runs steam drying, verify the cost saving is passed through and confirm no quality regression (bulk, brightness, rewet). → 卫材相关性★★★★☆｜A supplier cost lever you can negotiate, if quality holds.

Action Card H35-7 — Demand reel-moisture uniformity as a quality proxy. Insight: p.799 overdrying "from 6 to 4% reel moisture for a typical 800 t/d capacity linerboard machine results in $189,000 additional steam cost and 11,200 t production loss per year"; pocket ventilation lifts efficiency up to 20% (p.798). Action: Ask suppliers for CM moisture-profile uniformity data; poor uniformity implies over-drying of part of the reel = local hornification. → 卫材相关性★★★★☆｜Uniformity is a low-cost signal of disciplined drying control.

======================================================================

## Chapter 36 — Drying of Wood: Principles and Practices

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 36 (Perre´ & Keey) is the Handbook's definitive mechanistic treatment of wood drying and the upstream material source for fluff pulp. It progresses from wood structure (anatomy, knots, reaction/juvenile wood) → chemical composition (cellulose DP ~10,000, 50–70% crystalline; hemicellulose; lignin as the cementing amorphous polymer; extractives 5–30%) → board-scale physics (free vs bound water, fiber saturation point FSP ≈ 30–32%, differential heat of sorption, anisotropic shrinkage, Darcy/capillary/bound-water diffusion) → drying process (low-temperature convective with constant/falling rate; high-temperature internal overpressure; sapwood vs heartwood divergence) → mechanical aspects (shrinkage-driven stress, memory effect, case-hardening, checking) → kiln scale (lumber quality, design, operation, schedules). For the hygiene reader its value is mechanistic (bound-water diffusion below FSP, anisotropic shrinkage, lignin Tg) plus genuine pulpwood supply-chain relevance: juvenile/reaction wood and within-tree variability govern the feedstock that becomes fluff pulp.

### 核心观点标题

Wood is a variable, anisotropic, polymer-composite material

FSP ~30% bounds free/bound water; heat of sorption collapses to zero there

Permeability is the dominant anisotropy (1000× to >10⁶×)

Shrinkage is hydrogen-bond-driven and anisotropic; it creates drying stress

High-temperature drying uses internal overpressure; sapwood and heartwood diverge

- 

Juvenile and reaction wood degrade dried-wood quality (the pulpwood link)

### 在书中的作用

Ch36 is the upstream "material source" anchor: it supplies the wood that Ch33/Ch35 turn into fibres and pulp. It is the most mechanistic chapter in the assignment — the only one deriving Darcy, capillary-pressure and bound-water-diffusion equations and a full viscoelastic/mechanosorptive stress formulation. It complements Ch33 (which treats fibres hygroscopically) and Ch35 (which treats the pulp/paper web industrially) by explaining why the raw material is so variable and how that variability is baked in at the tree level.

### 卫材行动卡

Overall relevance: ★★★☆☆ (mechanistic value high; direct hygiene relevance is upstream/indirect).

Action Card H36-1 — Specify pulpwood feedstock mix, not just pulp specs. Insight: p.859 juvenile wood from plantations carries "higher transport and drying-energy costs" and "increased potential for collapse"; p.822 wood is "extremely difficult to characterize precisely." Action: When qualifying a fluff-pulp supplier, ask the fibre source (plantation vs old-growth, species, rotation age) and request data on juvenile-wood fraction; treat high-juvenile feedstock as a variability/uniformity risk. → 卫材相关性★★★★☆｜Feedstock variability propagates into pulp yield, bulk and refining energy you pay for.

Action Card H36-2 — Use FSP/green-MC to audit incoming chip and pulp MC. Insight: p.828 FSP ≈ 30–32%; Table 36.3 green MC 150–200% (softwood sapwood) must be removed before/at pulping. Action: Benchmark supplier chip/pulp MC against FSP and species green-MC tables; reject lots whose MC implies excessive evaporative energy or incomplete drying. → 卫材相关性★★★★☆｜Directly sizes the dewatering/drying energy embedded in your pulp cost.

Action Card H36-3 — Watch reaction-wood / knot indicators as quality proxies. Insight: p.859 Table 36.10 compression/tension wood = higher density, much greater longitudinal shrinkage, warp/collapse; p.858 large knots "treble the level of board rejection for unacceptable knot checks." Action: Request knot/shive and dirt content; correlate with upstream reaction-wood presence as a predictor of pad defects and refining load. → 卫材相关性★★★☆☆｜Knots/shives are the visible tail of reaction-wood variability.

Action Card H36-4 — Recognize H-bond hornification as the universal micro-mechanism. Insight: p.830 "new hydrogen bonds form between the hydroxyl groups … reduce the distance between the chains" on desorption; Ch33/Ch35 redry damage is the same event. Action: Unify your supplier-audit language: every redry/overdry = H-bond re-locking = lost swellability; apply Ch35's defibration-energy KPI. → 卫材相关性★★★★☆｜Gives a single molecular explanation across wood, pulp and web.

Action Card H36-5 — Expect permeability-driven dewatering limits. Insight: p.832 permeability anisotropy 1000×–10⁶×; p.833 pit aspiration locks low permeability on drying softwoods. Action: Anticipate that high-extractive/heartwood-rich feedstock dewaters and refined-pulps more slowly; factor into supplier capacity and lead-time. → 卫材相关性★★★☆☆｜Explains supplier throughput ceilings.

Action Card H36-6 — Apply the high-RH / high-T / high-velocity drying rules to any cellulosic drying you control. Insight: p.855 Rules 1–3 (high relative humidity to lower MC gradient; high temperature to accelerate internal transfer + viscoelastic creep; high air velocity for stack uniformity). Action: When specifying or auditing a converting/redry line, use these three levers as a checklist for fast-yet-good drying. → 卫材相关性★★★☆☆｜Portable rules for any thermal drying of cellulose.

======================================================================

## Ch37 — Drying in Mineral Processing

### 概述

Chapter 37 is a survey of dryer types used in the mineral and metallurgical industry, written by the handbook's editor (A.S. Mujumdar). Its scope is deliberately economic and selection-oriented: it enumerates conventional dryers (hearth, grate, shaft/tower, rotary) and the less-common types (spray, vacuum, fluid-bed, flash, conveyor, screw, drum, rotating-shelf), then summarizes their thermal-performance envelopes and the rules of thumb for choosing among them. The through-line is bulk-solids economics — drying is treated as a low-value, high-tonnage, energy-hungry unit operation at the handling/beneficiation stage, not as a product-quality step.

Reader-fit for the hygiene-materials / fluff-pulp strategist: the substrate (ore concentrates, coal, kaolin, titanium dioxide) is unrelated to absorbent hygiene products, so direct process transfer is minimal. The durable, substrate-independent lessons are: (1) the dewatering-before-thermal-drying rule re-appears here independently (p.878) — reinforcing Ch38's economic thesis; (2) the dusting / fire / explosion hazards of drying fine solids (p.878) connect to Ch43 (coal) and Ch45 (emissions/explosion); (3) sticky/caking feed handling (p.880) mirrors Ch38's sticky zone; (4) fuel choice and heat-recovery trade-offs (coal vs gas, superheated steam) are generic plant-economics. Relevance rating: ★☆☆☆☆ (one star) — bulk-solids plant economics only, low substrate relevance.

---

### 在书中的作用

Ch37 is the bulk-solids / low-unit-value anchor of the "Drying of Specific Materials" cluster. It bookends Ch43 (coal — a mineral subset with explosion focus) and complements Ch38 (sludge — wet/sticky/bioactive extreme). Its unique book-level contribution is the quantified performance envelope of conventional dryers and the editor's explicit selection philosophy ("several competing systems… different capital and operating costs"), which frames the whole materials section. It is plant-economics, not theory.

---

### 卫材行动卡

Overall relevance: ★☆☆☆☆ — bulk mineral solids; no direct substrate link to absorbent hygiene products. Transfer is limited to plant-economics and powder-handling principles.

H37-1 — Adopt the dewatering-first rule for any hygiene slurry/furnish. "maximize mechanical dewatering… to reduce the thermal load in drying" (p.878) and "nonthermal dewatering using filtration or centrifugation preceding thermal drying" (p.884) apply directly to SAP-slurry or wet-laid furnish: dewater mechanically before the through-air dryer. Relevance: ★☆☆☆☆ — economic principle (shared with Ch38).

H37-2 — Respect a dusting floor, not just a dryness target. "below a typical solid moisture content of 4%, dusting may pose serious handling and environmental problems" (p.878). For SAP/fluff fines handling, set a minimum allowable moisture to suppress dust/explosion, paralleling Ch43. Relevance: ★☆☆☆☆.

H37-3 — Use counter/parallel-flow logic for heat-sensitive hygiene streams. "For thermolabile materials with product moisture in excess of 1%, a parallel-flow dryer is desirable" (p.880) — when drying heat-labile binders/coatings, choose concurrent hot gas so solids stay near wet-bulb. Relevance: ★☆☆☆☆ — selection heuristic.

H37-4 — Expect sticky-feed handling for paste-like hygiene ancillaries. "special internals within the shell to break up the formation of large agglomerates" (p.880) — when drying sticky Coated-fiber/SAP masterbatch feeds, specify agglomeration-breaking internals or back-mix (cf. Ch38 sticky zone). Relevance: ★☆☆☆☆.

H37-5 — Evaluate superheated-steam / closed-loop for heat recovery. "With superheated steam… the exhaust is also steam, which can be condensed to recover heat or… recycled" (p.884) — for energy-sensitive hygiene lines, consider steam drying with condensate heat recovery (links to Ch43/Ch45 closed-cycle). Relevance: ★☆☆☆☆.

---

======================================================================

## Ch38 — Dewatering and Drying of Wastewater Treatment Sludge

### 概述

Chapter 38 reviews the complete water-removal chain for wastewater-treatment sludge: (i) moisture classification (how tightly water is bound), (ii) mechanical dewatering (filtration, pressing, centrifugation — water removed without evaporation), and (iii) thermal drying (direct, indirect, combined, and hybrid dryers). Its organizing thesis is economic and environmental: because sludge arrives at >95% moisture, evaporating that water thermally is ruinously expensive, so the engineering logic is to push as much dewatering as possible into the cheap, non-evaporative mechanical stage before any thermal drying is justified. The chapter is a process-equipment survey aimed at plant designers and utility engineers, not at polymer or material scientists.

Reader-fit for the hygiene-materials / fluff-pulp strategist: the substrate (municipal/industrial sludge) is far from absorbent hygiene products, so direct process transfer is thin. The durable, substrate-independent lessons are two: (1) the dewatering-before-evaporation energy economics rule — which applies equally to dewatering a SAP/fiber slurry or a fluff-pulp furnish before a dryer — and (2) the sticky/plastic-phase handling problem that appears whenever a wet, hydrophilic solids suspension is dried through an intermediate paste zone. Relevance rating: ★☆☆☆☆ (one star) — a real process-economics lesson, but low substrate relevance.

---

### 在书中的作用

Ch38 sits in the "Drying of Specific Materials" / waste-and-biosolids cluster. It complements the mineral/coal/enzyme chapters in this batch by representing the wet, sticky, biologically active end of the solids-drying spectrum — the opposite extreme from free-flowing coal or crystalline enzymes. Its main book-level contribution is the dewatering-first energy hierarchy and the sticky-zone concept, both of which are reused implicitly in chapters on paste- and slurry-drying (e.g. spray and indirect dryers in Ch10/Ch12). It is a plant-engineering chapter; it does not advance drying theory.

---

### 卫材行动卡

Overall relevance: ★☆☆☆☆ — substrate is municipal/industrial sludge, not absorbent hygiene materials. The durable transfer is process-economics logic and sticky-feed handling, not equipment specifics.

H38-1 — Apply the dewater-first hierarchy to any hygiene slurry/furnish. Before committing web or SAP-slurry to a thermal dryer, maximize mechanical dewatering (vacuum, press, through-air pre-dewater, screw press). The energy gap (≈1–70 kJ/kg mechanical vs ≈2260 kJ/kg latent) means every kg of liquid removed mechanically saves an order of magnitude of thermal energy. Relevance: ★☆☆☆☆ — economic principle only.

H38-2 — Expect and design around a sticky/plastic phase. Any hydrophilic fine-solids suspension (SAP masterbatch, Coated-fiber slurry, binder-laden furnish) will pass through a paste zone (~55–70% solids analog). Use back-mix recycle to stay above it, or strong shear (kneading/disc/porcupine agitator) — same remedies the chapter gives for sludge. Relevance: ★☆☆☆☆ — handling principle only.

H38-3 — Treat thermal drying as a sterilization/odour step only when needed. The chapter shows 70°C/2 h (or 90°C/10–15 min) inactivates pathogens (p.899). For hygiene, the parallel is heat treatment of recycled/fiber streams; note the energy cost before assuming thermal routes. Relevance: ★☆☆☆☆.

H38-4 — Prefer indirect/closed-loop when vapour capture matters. Indirect dryers "produce minimal amounts of vapors and are therefore easy to manage" (p.892). On a converting line where VOC/odour capture is regulated (see Ch45), the same logic favours closed-loop/indirect drying to shrink the gas to treat. Relevance: ★☆☆☆☆ — feeds Ch45.

H38-5 — Reuse waste heat; quantify the 60% saving. Flue-gas/vent-gas heat reuse "can save as much as 60% on the cost" (p.899) and mechanical vapour compression "can improve the energy efficiency considerably" (p.899). Build waste-heat recovery into any new hygiene drying line rather than treating dryer exhaust as pure liability. Relevance: ★☆☆☆☆.

---

======================================================================

## Chapter 39 — Drying of Biotechnological Products

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 39 (Adamiec, Kamiński, Markowski & Strumiłło) treats drying as preservation of biologically active material — microorganism cultures, enzymes, antibiotics, vitamins, proteins — rather than as bulk water removal. The authors frame the core problem: in these colloidal-capillary-porous substances, water is both solvent and a structural element of the particle, so drying must preserve activity/storage life, not merely hit a moisture target. They classify products by thermal lability (thermo-/xerolabile vs thermo-/xerostable) and by whether water is life-sustaining or merely a solvent, then derive first-order activity-loss kinetics via the Arrhenius equation (Table 39.3 gives activation energies). Method sections cover spray, jet-spouted-bed, impingement-stream, fluidized/vibrofluidized, fixed-bed, drum, freeze/vacuum, carrier, and encapsulated drying. The chapter closes with the three design levers: shorten high-temperature exposure, enable frequent parameter control, and use carriers/sorbents plus protective additives (glycerin, sugars). For hygiene, this is the home chapter for probiotic/active-ingredient wipes and enzyme-containing formulations.

### 核心观点标题

Water is both solvent and structural element; drying must preserve activity

Products split into thermolabile (life-sustaining water) vs thermostable (water as solvent)

Activity loss follows first-order Arrhenius kinetics

Freeze/vacuum drying excludes thermal inactivation but is slow and energy-heavy

Protective additives and vitrification protect cells during freezing

- 

Spray drying works for thermolabile material if done at the wet-bulb temperature

### 在书中的作用

Ch39 is the "biological activity preservation" chapter, complementary to Ch41 (polymer resins), Ch42 (enzymes specifically), and Ch40 (coated webs). Where Ch42 focuses on enzyme activity-loss, Ch39 generalizes to whole cells, spores, antibiotics and encapsulated actives. For the hygiene reader it is the bridge from bulk/material drying to keeping a living or bioactive ingredient alive through a converting/drying step (probiotic wipes, enzyme-based stain-removal wipes, vitamin/active coatings).

### 卫材行动卡

Overall relevance: ★★★ (moderate — probiotic/active-ingredient wipes, enzyme formulations; not core structural materials).

Action Card H39-1 — Treat active-ingredient drying as activity preservation, not MC targeting. Insight: p.905 water is "a constructional element… of fundamental importance for… activity." Action: For probiotic/enzyme/ vitamin wipes, set the drying spec from an activity-retention target (% viable cells / % enzyme activity remaining), not just final MC. → 卫材相关性★★★★☆｜Converts invisible activity loss into the real acceptance criterion.

Action Card H39-2 — Use first-order/Arrhenius to budget line temperature. Insight: p.910 dA/dt=−k_d A, kd=k{d,0}exp(−E_a/(R_u T)); Table 39.3 E_a per organism/enzyme. Action: When designing or auditing an active-coating/impregnation dryer, compute the allowable product-temperature × residence-time envelope from the active's E_a; require the line stay inside it. → 卫材相关性★★★★☆｜Prevents thermal kill of probiotic/enzyme actives on the line.

Action Card H39-3 — Prefer spray-at-wet-bulb or freeze-dry for labile actives. Insight: p.914 spray drying works for thermolabile material "at a wet bulb temperature"; p.917 freeze/vacuum "excludes thermal inactivation." Action: For live-culture or high-value enzyme wipes, qualify a spray dryer run at wet-bulb (high dispersion, high inlet air) or a freeze-dry step; avoid sustained high-T hovering. → 卫材相关性★★★★☆｜Keeps the most fragile actives alive through drying.

Action Card H39-4 — Add cryo/protective substances to the active formulation. Insight: p.918 glycerin/sugars protect cells, form "vitreous structures," buffer salt concentration. Action: Require protective additives (glycerin, trehalose/sucrose, skim milk, maltodextrin) in any freeze- or spray-dried active system; verify they are skin-contact-compliant. → 卫材相关性★★★★☆｜Formulation-side lever to survive drying and storage.

Action Card H39-5 — Use a food-grade carrier/sorbent for delicate actives. Insight: p.920 carrier "protects cells or biopolymers… takes over part of moisture"; Fig 39.22 ranks sorbents. Action: For powdered active premixes for wipes, specify a food-grade carrier (starch/maize meal/skim milk) that buffers moisture and lowers drying energy. → 卫材相关性★★★｜Two benefits: protection + energy saving in the active premix.

Action Card H39-6 — Consider encapsulation for stabilized, delayed-release actives. Insight: p.922 encapsulation "stored in a stable state… action is prolonged to many hours"; dried as ~10 µm spheres via spray/freeze. Action: For fragrance/active wipes wanting delayed or protected release, evaluate spray-dried microcapsules (starch/chitosan matrix, refs 79/85/88). → 卫材相关性★★★｜Enables stabilized, controlled-release active delivery in wipes.

======================================================================

## Chapter 40 — Drying of Coated Webs

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 40 (Hung, Wimberger & Mujumdar) is the Handbook's reference for drying a thin liquid layer on a moving substrate — the exact physics behind lotion/emulsion coating on wipes and adhesive/coating lines on hygiene films and tapes. It opens by classifying coated webs (paper/paperboard, plastic films & tapes, metallic sheets) and coating forms (solventborne, waterbased, 100% solids), then builds the drying-curve framework: adjustment → constant-rate → falling-rate, with the crucial note that water-based latex coatings hold a longer constant-rate than solventborne. The technical core is air-impingement and flotation dryer design (air bars, slots, cushion pressure, web stability), augmented by IR, UV and EB curing. It closes with application examples (paper coating, PVDC barrier, pressure-sensitive adhesives) and an extensive safety section (LEL, inert-gas drying, VOC recovery/incineration). Throughout, the authors tie drying-rate scheduling to final coating morphology — mottle, binder migration, skinning, blistering, curl.

### 核心观点标题

A coated web is a thin liquid layer whose final morphology is set by the drying curve

Latex (water-based) coatings keep a longer constant-rate than solventborne

Over- or rapid drying creates the classic coating defects

Binder migration and mottle are governed by the preheat/constant-rate stages

Air impingement dries the surface first and accelerates binder migration

- 

100% solids UV/EB cure needs no solvent removal and leaves no toxic residuals

### 在书中的作用

Ch40 is the "thin-liquid-layer-on-moving-substrate" chapter, complementary to Ch41 (granular polymer resins), Ch35 (pulp/paper web conduction), and Ch33 (fibre–water physics). It is the direct engineering counterpart to any hygiene converting line: lotion/emulsion coating on wipes (Ch40's latex/water-based logic), adhesive and barrier coating on backsheet films (PVDC, PSA sections), and printed packaging. For the hygiene reader it converts "coat a liquid on a film" into a drying-rate-control problem.

### 卫材行动卡

Overall relevance: ★★★★★ (directly maps to wipe lotion coating & film adhesive/barrier lines).

Action Card H40-1 — Schedule drying to cross 75% dryness fast, then finish gently (anti-mottle). Insight: p.933 "Little migration occurs once the coating is about 75% dryness"; p.931 binder migration set in preheat/constant-rate. Action: For lotion/active-coated wipes, specify a high constant-rate predry to reach ~75% solids quickly, then a low-temperature falling-rate finish; forbid over-fast impingement that skins the surface. → 卫材相关性★★★★★｜Directly controls mottle and uniform active loading on the wipe.

Action Card H40-2 — Use flotation (not impingement) for delicate coated-wipe webs. Insight: p.935 air flotation supports web "on a cushion of heated air" with no contact; p.933 impingement "accelerates the binder migration." Action: When qualifying a wipe or film coater, prefer air-flotation drying for the coated side to avoid picking/marks and to limit surface-driven migration. → 卫材相关性★★★★★｜Contactless drying protects coating integrity and uniformity.

Action Card H40-3 — Cap dryer temperature at the constant-rate wet-bulb to avoid railroad tracking. Insight: p.933 "'Rail road tracking' will take place when the dryer temperature exceeds the wet bulb temperature of the constant drying rate period." Action: Require the coater to run impingement below the coating's wet-bulb temperature during constant-rate; add a defect check (railroad tracking / streaks) to incoming-film audit. → 卫材相关性★★★★★｜A named defect mode to screen on coated hygiene films.

Action Card H40-4 — Tune IR to the water-absorption band to preheat without skinning. Insight: p.940 IR penetration max ~1.5 mm; "heats the substrate rather than skinning and blistering it"; p.941 match absorption/radiation curves; water peaks at 3 & 6 µm. Action: For water-based lotion coatings, specify medium/long-wave IR preheat matched to the water band rather than short-wave that skins the surface. → 卫材相关性★★★★★｜Prevents skinning/blistering of the lotion layer.

Action Card H40-5 — Prefer 100% solids UV/EB cure for skin-contact film coatings. Insight: p.942 UV/EB "100% solids and solvent removal equipment is not required… no residual promoters or cross-linking agents… toxic residues in products for food and drug applications." Action: For adhesive/coating lines on films touching skin, evaluate UV/EB cure to eliminate solvent VOC and reduce extractable residuals; verify photoinitiator extractables separately. → 卫材相关性★★★★★｜Regulatory-friendly route for food/drug-contact hygiene films.

Action Card H40-6 — Enforce LEL/inert-gas safety on any solvent-coated hygiene film. Insight: p.944 max solvent vapor 25% LEL (50% with instrumentation); p.945 inert gas keeps O₂ "% oxygen"; p.946 VOCs. Action: If a backsheet/tape line uses solvent coatings, require LEL monitoring + auto-shutdown at 50% LEL and confirm inert-gas O₂ control for solvent recovery. → 卫材相关性★★★★☆｜Fire/explosion compliance for converting lines.

Action Card H40-7 — Specify barrier/adhesive dry rates from the application tables. Insight: p.943 PVDC vapor-barrier "evaporation rates are usually 10 to 15 kg/h/m² with air velocities of 20 to 40 m/s"; p.943 PSAs "Solvent removal rate limitations are at 18 kg/h/m²"; p.943 paper-coat system "80% solid level by air flotation… 4 to 6 steam-heated cylinders with an evaporation rate restriction of 20 kg/h/m²." Action: Benchmark supplier converting-line rates against these figures when qualifying barrier or PSA hygiene films. → 卫材相关性★★★★☆｜Concrete rate benchmarks for film coating qualification.

======================================================================

## Chapter 41 — Drying of Polymers

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 41 (Mujumdar & Hasan) is the Handbook's dedicated "drying of polymers" chapter and the mechanistic home chapter for resin- and pellet-scale drying of the very plastics used in hygiene materials — polyolefins (PP, PE backing film and nonwovens), PET and nylon (spunbond/nonwoven topsheet and fibers), PVC, ABS and polycarbonates. The authors open by framing polymer drying as the solid-handling tail of polymerization recovery (after unreacted-monomer salvage, coagulation, devolatilization, liquid–solid separation) and warn that selection is proprietary and case-specific. The chapter surveys polymerization routes (bulk/solution/suspension/emulsion/gas-phase), classifies dryers by heat-transfer mode, residence time and physical form, catalogs 10 dryer families, then walks through drying systems for polyolefins, PVC, ABS, synthetic fibers (nylon, PET) and miscellaneous resins. It closes with resin classification (hygroscopic vs nonhygroscopic), desiccant-dryer design, and — critically — a devolatilization paragraph that is the single most SAP-relevant passage: residual monomer is removed above the glass transition temperature.

### 核心观点标题

Polymer drying is the solid-handling tail of polymerization recovery

Drying sits downstream of a chain of recovery operations including devolatilization

Dryer selection is governed by upstream physical state, not by polymer chemistry alone

Devolatilization (residual-monomer removal) is performed above Tg

Two-stage systems dominate because surface and bound moisture need different treatment

- 

Hygroscopic resins hold moisture inside the pellet and demand desiccant (very low dew point) drying

### 在书中的作用

Ch41 is the Handbook's polymer-specific drying chapter and pairs with Ch35 (pulp/paper), Ch33 (fibrous materials), Ch40 (coated webs) and Ch42 (enzymes). Where Ch35 treats cellulosic web drying and Ch33 the fibre–water molecular physics, Ch41 treats granular/pellet/powder polymer resins — the feedstocks of hygiene films (PE/PP), nonwovens (PP/PET/nylon) and, by mechanism, superabsorbent polyacrylate. It is the natural counterpart to Ch40 (thin liquid layer on substrate) in that both deal with polymers + volatiles, but Ch41 works on the solid particle scale.

### 卫材行动卡

Overall relevance: ★★★★★ (mechanistic home chapter for SAP + PE/PP/PET/nylon resins).

Action Card H41-1 — Specify the residual-monomer strip as a Tg-aware step, not merely "drying." Insight: p.977 devolatilization "is usually performed above the glass transition temperature of the polymer"; residual volatiles "range from several parts per million to several tens of percentage." Action: For SAP or acrylic-based superabsorbents, require the supplier's finishing step to state temperature vs (water-plasticized) Tg and residence time, and demand a residual free-acrylic-acid / residual-monomer CoA (skin-safety ppm). → 卫材相关性★★★★★｜Directly governs residual-monomer/free-acrylic-acid skin safety and the conversion left in the gel.

Action Card H41-2 — Bound the finishing temperature to avoid thermal crosslinking that kills swell capacity. Insight: p.977 devolatilization above Tg; [inference] over-temperature drives additional crosslinking (network shrinkage) exactly as Ch35's hornification welds cellulose. Action: Set a supplier spec ceiling on final-stage temperature and verify swell capacity / absorbency-under-load on incoming lots; trend it lot-to-lot. A falling swell number signals over-crosslinking from an over-hot finishing dry. → 卫材相关性★★★★★｜Thermal crosslinking in the dry step is a silent swell-capacity killer for SAP.

Action Card H41-3 — Use the two-stage template for any hygiene-polymer dry line. Insight: p.967 "Since ABS requires both surface and bound moisture removal, a two-stage drying system is recommended"; repeated for PP, S-PVC, E-PVC, PET. Action: When qualifying a resin or SAP supplier, confirm a fast surface-predry + a gentle bound-moisture finishing stage rather than a single high-temperature pass. → 卫材相关性★★★★★｜Single-stage overheating is the root cause of both residual monomer and crosslink damage.

Action Card H41-4 — For PE/PP backsheet & nonwoven resin, control final moisture to Table 41.1 spec. Insight: p.962 Table 41.1 — PP permissible moisture 0.05% (injection)/0.03–0.10% (extrusion), drying temp 71–93°C; HDPE 0.05–0.10%/0.03–0.05%, 71–104°C; PP is "solvent wet" from hexane (p.962) and closed-loop N₂ is used to reach ~500 ppm solvent (p.963). Action: Require CoA moisture ≤ Table 41.1 limits and confirm nonhygroscopic (surface) moisture is removed pre-extrusion to avoid bubbles/voids in film. → 卫材相关性★★★★★｜Resin moisture spec is the quality gate for film/nonwoven extrusion.

Action Card H41-5 — For PET/nylon nonwoven, demand desiccant (very low dew point) drying. Insight: p.972 PET/nylon are hygroscopic (moisture inside pellet); p.973 "PET absolutely requires dew points in the −40 to −50°C range"; p.971 PET must reach 0.005% db and "can have absolutely no exposure to atmosphere between drying and processing." Action: For spunbond/nonwoven feedstock, require dew-point certificate and sealed transfer; reject lots showing hydrolysis brittleness. → 卫材相关性★★★★★｜Internal moisture hydrolyzes PET during melt spinning; dew point is the real control.

Action Card H41-6 — Watch PVC/VC emission and monomer residuals if using PVC-based hygiene films. Insight: p.966 "U.S. EPA emission limitations of  ppm on VC must be strictly maintained"; p.966 monomer chloride "induces pitting corrosion and stress corrosion cracking." Action: If a supplier runs PVC, verify VC-emission compliance and residuals; this dictates allowed dryer type. → 卫材相关性★★★★☆｜VC monomer residual is both a regulatory and a film-integrity issue.

Action Card H41-7 — Use ppm-level solvent-residual spec for any solvent-polymerized hygiene resin. Insight: p.963 PP dried in N₂ FBD "contains an extremely low level of solvent (e.g., hexane or heptane), typically 500 ppm"; p.957 superheated-vapor fluidization recovers solvent efficiently. Action: Require residual-solvent CoA (≤ a few hundred ppm) for solvent-made PP/PE grades used in skin-contact layers. → 卫材相关性★★★★☆｜Residual solvent is an odor and skin-safety parameter for film layers.

======================================================================

## Chapter 42 — Drying of Enzymes

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 42 (Pilosof & Sánchez) treats enzyme drying as a damage-minimisation problem: enzymes are heat-labile protein catalysts that "are deactivated due to heat-induced structural changes," yet solid (powder/granule) form is required for storage stability and dust-safety. Spray drying is the industrial workhorse; the chapter covers drying-chamber layouts (cocurrent preferred to minimise heat deactivation), the activity-loss kinetics (loss rises with outlet temperature and as moisture falls below 15–20%), and the central stabilisation science — sugars, polyols, and salts that form a glassy amorphous matrix (Tg 60–200 °C) in which the protein is immobilised and hydrogen-bonded as a water substitute. The second half covers powdered-detergent enzyme granulation (fast-mixer, prilling, extrusion, spray-coating of cores) aimed at eliminating active enzyme dust. Relevance to hygiene is modest but real for enzyme/active-containing wipe and cleaning formulations.

### 核心观点标题

Enzymes deactivate on heating; drying must preserve activity

Cocurrent spray drying minimises heat deactivation

Activity loss rises with outlet temperature and below 15–20% moisture

Sugars/salts form a glassy matrix that immobilises and substitutes for water

A glass-forming carrier needs Tg 60–200 °C and chemical inertness

- 

Enzyme granules must be coated to eliminate active dust

### 在书中的作用

Ch42 is the book's only biomolecule-drying chapter and the direct counterpart to Ch45 (emission control — here dust is a biological hazard) and Ch44 (feeding/atomisation of the enzyme slurry). It is the Handbook's bridge from bulk/industrial drying to heat-labile active ingredients — the same regime an enzyme-wipe or active-coated-substrate formulator operates in.

### 卫材行动卡

Overall relevance: ★★★☆☆ (modest — genuine for enzyme/active-containing wipes & cleaning substrates; not for core fluff/SAP).

Action Card H42-1 — Embed heat-labile actives in a glassy sugar/salt matrix. Insight: p.983–984 vitrification; p.984 0.5% lactose lifts protease residual from 83→90%; MgSO₄ gives >100% recovery. Action: For enzyme or probiotic wipes, specify a trehalose/maltose/salt glassy carrier (Tg 60–200 °C) in the active formulation rather than free dried protein. → 卫材相关性★★★☆☆｜Preserves active titre through drying and shelf life of the wipe.

Action Card H42-2 — Cap outlet T and avoid over-drying the active layer. Insight: p.981 loss rises with outlet T; "Significant inactivation occurs when moisture decreases below 15–20%." Action: On any spray- or air-drying step for an active-coated substrate, require a two-stage (spray→low-T fluid bed 40–50 °C) profile and a residual-MC floor. → 卫材相关性★★★☆☆｜Prevents the hydration-shell-removal inactivation shock on the active.

Action Card H42-3 — Use inert (N₂) drying for oxidation-sensitive actives. Insight: p.980 "in the case of enzymes that are particularly sensitive to oxidation, it is preferable to use inert gas, such as nitrogen." Action: For oxidant-sensitive actives (certain enzymes, vitamins), require nitrogen blanketing in the drying/coating step. → 卫材相关性★★☆☆｜Extends active stability where oxidation is the loss mechanism.

Action Card H42-4 — Coat active granules to block dust + bleach/oxidant exposure. Insight: p.986 coating must give "no active enzyme dust … released during handling" and protect against "hydrogen peroxide, and peracetic acid," yet "dissolve readily … even at low temperatures." Action: For enzyme/active granules dosed into wipes, require a low-dust, oxidant-resistant, readily-dissolving coating spec. → 卫材相关性★★★☆☆｜Worker/end-user safety plus protection from wipe oxidants (e.g., peracetic acid).

======================================================================

## Chapter 43 — Drying of Coal

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 43 (Pikoń & Mujumdar) is a large equipment catalogue of coal-drying technology: rotary, rotary-tube, chamber-with-stirrers, pneumatic, fluid-bed, spouted-bed, vibratory, mill-type, shaft, moving-bed, and superheated-steam dryers, followed by low-rank-coal, hot-oil, hot-water, combined grinding-drying, Fleissner, biomass, and mechanical-thermal-expression variants. The authors repeatedly return to two themes with genuine cross-industry value: (1) safety — explosion panels, cocurrent operation to avoid ignition, low-oxygen/inert (superheated-steam) drying to eliminate fire/explosion and spontaneous-combustion risk in reactive low-rank coals; and (2) bulk-solids drying economics — heat consumption quoted per kg of water evaporated (≈2800–3700 kJ/kg H₂O depending on dryer type). For a hygiene reader the substrate is irrelevant, but the safety and energy-economics lessons transfer to any combustible-dust / fine-powder drying or airlaid line.

### 核心观点标题

Coal drying splits moisture into constant-rate surface and falling-rate hygroscopic phases

Rotary dryers run cocurrent to avoid ignition

Pneumatic dryers carry explosion flaps

Low oxygen / inert drying eliminates fire-explosion and spontaneous-combustion risk

Superheated steam drying removes the fire/explosion hazard entirely

- 

Drying is an energy-cost line quoted per kg of water removed

### 在书中的作用

Ch43 is the bulk-solids / high-tonnage drying chapter. It parallels Ch37 (minerals) and Ch38 (sludge) in treating large particulate streams, and complements Ch44 (feeding) and Ch45 (emission control) for any solid-handling dryer. Its safety and energy-economics frames are generic enough to apply to non-coal powders.

### 卫材行动卡

Overall relevance: ★★☆☆☆ (weak substrate relevance; value is the generic safety + energy-economics lessons, not the coal).

Action Card H43-1 — Demand explosion panels + inerting on fine-powder pneumatic/conveying lines. Insight: p.999 "explosion flaps (17)"; p.1009 "not to have high oxygen content … to avoid explosion and fire hazard." Action: For fluff-defibration, SAP-fines, or airlaid pneumatic conveyors, require explosion-relief panels and a documented oxygen-control/inerting policy on the supplier's line. → 卫材相关性★★★｜Cellulosic + SAP fines are combustible; explosion protection is a real compliance/safety need.

Action Card H43-2 — Prefer indirect/low-O₂ drying where self-heating is plausible. Insight: p.1009 "Low-rank coals can be highly reactive … spontaneous combustion. Hence indirect dryers have some advantages." Action: Where a hygiene powder is finely divided and heat-sensitive, ask whether an indirect or inerted dryer was chosen over a direct-fired one, and why. → 卫材相关性★★★｜Self-heating / dust-explosion logic applies to fine hygiene powders.

Action Card H43-3 — Benchmark any dryer upgrade on kJ per kg water removed. Insight: p.993 ≈3700 kJ/kg H₂O (rotary); p.1007 2800–3500 (steam). Action: When a supplier proposes a new dryer or drying route, require the energy quoted as kJ/kg H₂O (not per kg product) so it is comparable to pulp/coating lines. → 卫材相关性★★☆☆｜Generic energy-cost denominator; helps spot an efficient vs wasteful drying route.

Action Card H43-4 — Note cocurrent-direct-fired as an ignition-risk pattern to flag. Insight: p.992 rotary "operate in the cocurrent mode to avoid the possibility of ignition." Action: In audits of direct-fired coaters/dryers, check the firing/direction arrangement and whether ignition-risk mitigation was considered for the combustible web. → 卫材相关性★★☆☆｜Fire-safety design cue for direct-fired hygiene ovens.

======================================================================

## Chapter 44 — Dryer Feeding Systems

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 44 (Jumah & Mujumdar) argues that the feeder and its storage bin are "an integral unit of the dryer system" and that feed consistency, dispersion, and rate control determine dryer performance. The authors first give selection guidelines anchored on the flow behaviour of bulk solids (Carr's property table, material classes, feeder-selection guide), then classify storage bins (funnel / mass / expanded flow) and the two feeder classes (volumetric vs gravimetric). Five feeder types are detailed — screw, vibrating, belt, rotary-table, rotary (airlock) — with design/operating characteristics. The chapter closes with dryer-specific feeding: flash (dispersion + disintegrator + backmixing), fluid-bed, rotary, conveyor, spray (tank–strainer–pump–atomizer), and drum. For a hygiene reader the transference is concrete: the same atomiser/feeder/screw logic governs SAP powder and slurry handling upstream of drying and coating.

### 核心观点标题

Bin and feeder are one integral, flow-determining unit

Most dryers cannot accept feed unless it is free-flowing

Small feed-consistency changes can flip feeder behaviour

Mass-flow bins minimise caking, degradation, segregation

Gravimetric beats volumetric by 2–5× in accuracy

- 

In flash/spray drying, feed dispersion governs product spec

### 在书中的作用

Ch44 is the materials-handling prelude to every dryer chapter. It supplies the upstream logic that Ch45 (emission control) and the unit-operation chapters (spray, flash, fluid-bed, rotary) assume but do not explain: how a consistent, dispersed, metered feed reaches the dryer. For hygiene procurement it is the bridge between "what the dryer vendor ships" and "whether the SAP/slurry/fluff actually arrives feed-ready."

### 卫材行动卡

Overall relevance: ★★★☆☆ (moderate-to-good — feed consistency/dispersion logic transfers to SAP powder & slurry handling upstream of drying).

Action Card H44-1 — Specify mass-flow bin + gravimetric metering for SAP/additive feeds. Insight: p.1021 mass-flow "minimizing caking, degrading, or segregation"; p.1023 gravimetric 2–5× more accurate than volumetric. Action: For SAP or superabsorbent-blend metering into a line, require a mass-flow silo and a gravimetric feeder with tachometer feedback; reject volumetric-only where dose accuracy matters. → 卫材相关性★★★★☆｜Dosing accuracy of SAP/additive into the core directly sets absorbency and avoids lot drift.

Action Card H44-2 — Put a feed rheology window on slurry/lotion specifications. Insight: p.1018 "A liquid needs the right range of viscosity, surface tension … allow it to be pumped and … sprayed"; p.1018 feed-consistency changes "change feeder characteristics significantly." Action: Define and QC the viscosity/solids window of SAP slurry, coating liquor, and fragrance emulsion at the supplier interface; trend lot-to-lot. → 卫材相关性★★★★☆｜Feed rheology, not the dryer, sets whether the line can run; prevents atomiser blockage and off-spec.

Action Card H44-3 — Require filtration ahead of any spray/coating atomiser. Insight: p.1034 "The feed strainer or filter is important because all matter likely to jeopardize the performance of the dryer through partial or total blockage of the atomizer must be removed." Action: Demand a specified micron-rated strainer and demineralised/clean-condensate flush path on any spray or slot-die coating line. → 卫材相关性★★★★☆｜Atomiser blockage is the top failure mode on coating/spray hygiene lines.

Action Card H44-4 — Use a rotary airlock for fine-powder interfaces to pressurized dryers. Insight: p.1030 rotary feeder "Serves as gas pressure seal … Suitable for feeding fine powders"; up to 150 kPa. Action: Where SAP/fluff fines enter a pressurized airlaid former or flash zone, specify a rotary valve airlock rather than an open chute. → 卫材相关性★★★☆☆｜Prevents gas leak (heat loss) and dusting at the dryer feed point.

Action Card H44-5 — Avoid stickiness-driven downtime: test full moisture range of feed. Insight: p.1038 "the full range of moisture content is tested as moisture-induced stickiness can cause severe operational problems." Action: In supplier qualification, require feeder trials across the worst-case MC/viscosity envelope, not just nominal. → 卫材相关性★★★☆☆｜Stickiness at edges of the spec is where feeding lines actually fail.

======================================================================

## Chapter 45 — Dryer Emission Control Systems

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 45 (Jumah & Mujumdar) treats the drying plant as an open-loop source of dust, gases, and odors and argues that emission control is no longer optional: "More stringent demands governing environmental aspects of the plant operations have resulted in better compliance." The authors organize the field into three control targets — particulate matter (PM), gaseous emissions, and odor — and then catalogue the three most-widely-used devices (cyclones, fabric filters/baghouses, wet scrubbers) with their operating principles, advantages/disadvantages, selection, design equations, and performance data. The second half surveys emission control in selected industries (minerals, chemicals, pharmaceuticals, food/agriculture), showing how the generic devices are combined into compliance trains. The central commercial message — that "the cost of the equipment needed to comply with regulations can exceed that of the dryer itself" — and the VOC-recovery logic are the parts most transferable to hygiene converting lines.

### 核心观点标题

Dryers are a primary emission source and control is now mandatory

Organic-liquid removal demands solvent recovery economics, not just destruction

Condensers are the first stage of any VOC/odor train

Control-capital can exceed dryer-capital

Baghouses give the highest particulate capture but carry fire/explosion duty

- 

Pharmaceutical/VOC control menu applies directly to coated-web odour

### 在书中的作用

Ch45 is the Handbook's plant-engineering / environmental-compliance capstone. It complements the unit-operation chapters (spray, fluid-bed, flash, rotary) by treating the exhaust side every dryer needs. Its Table 45.2–45.3 and the industry survey directly extend the air-quality obligations a buyer must impose on a coating-oven, airlaid, or defibration supplier. It pairs naturally with Ch44 (feeding, which sets the dust/loading the collector must handle) and with the spray-drying chapters referenced for detergent/pharma layouts (Table 45.20, Figures 45.7–45.10).

### 卫材行动卡

Overall relevance: ★★★★★ (highest in this batch — direct compliance/odour/particulate transfer to converting lines).

Action Card H45-1 — Demand the condenser-first VOC train on any coating/lotion/airlaid line. Insight: p.1042 — organic/odorous exhaust "should first be passed through a condenser … allows recovery of a costly solvent." Action: In supplier audits, require the abatement flow diagram; reject any design that feeds VOC-laden air straight to an oxidiser without a condenser/recovery stage. → 卫材相关性★★★★★｜Directly governs odour, VOC compliance and solvent-cost recovery on lotion/adhesive/printing dryers.

Action Card H45-2 — Specify particulate control for airlaid/fluff-defibration exhaust as baghouse + explosion protection. Insight: p.1044 Table 45.2 (baghouse >99% on <1 µm); p.1049/p.1052 baghouses need explosion panels, grounding, spark protection for combustible dust. *Action:* Require supplier to certify baghouse efficiency ≥99%, explosion-relief panels, carbon/steel-wire grounded cloth, and spark arrestor upstream. → 卫材相关性★★★★★｜Cellulosic + SAP fines are combustible; capture efficiency and explosion safety are non-negotiable.

**Action Card H45-3 — Use Table 45.20 to set an exhaust-PM acceptance limit.** *Insight:* p.1066 — open-cycle cyclone layout >250 mg/Nm³; bagfilter + absolute filter 0.1–5; recycled systems "Negligible." Action: Set a contractual particulate-emission limit (e.g., ≤20 mg/Nm³ for a bag-filtered line) referencing the achievable layout classes. → 卫材相关性★★★★★｜Converts invisible exhaust dust into a measurable, enforceable spec.

Action Card H45-4 — Interrogate odour control chemistry on soap/detergent-style spray lines. Insight: p.1063 — "The main atmospheric pollution problem in soap manufacturing is odor" controlled by "scrubbing with an acid solution"; surfactant organics "vaporized in the spray dryer … condense in the tower exhaust air stream into droplets," paraffin alcohols/amides give "a highly visible plume." Action: For any surfactant-containing or fragranced web, ask what scrubber chemistry (acid/water/activated-carbon) suppresses odour and plume. → 卫材相关性★★★★★｜Fragrance and surfactant carry-over is the dominant odour source on hygiene lines.

Action Card H45-5 — Ask recovery vs destruction on solvent streams. Insight: p.1040 — "recovery of the solvent is frequently desirable … to lower costs, prevent a safety hazard, and eliminate air pollution." Action: Require the supplier to state whether coating/printing solvents are recovered (closed-loop/condenser + carbon) or destroyed (thermal/catalytic incineration), and the associated OPEX. → 卫材相关性★★★★☆｜Recovery vs destruction changes both compliance risk and unit cost you pay.

Action Card H45-6 — Require dew-point/condensation discipline on baghouse exhaust. Insight: p.1052 — baghouses operating "below the dew point … with high water vapor content" cause condensation, especially outdoors in winter; p.1059 asphalt/cement note condensation on fabric "poses a serious fire hazard." Action: Verify the collector is insulated/heated and runs above dew point; request the exhaust dew-point vs operating-temperature margin. → 卫材相关性★★★★☆｜Prevents plugging, corrosion and fire on humid fluff/airlaid exhaust.

Action Card H45-7 — Evaluate closed-cycle drying for solvent/odour-critical webs. Insight: p.1065 — closed-cycle recommended for flammable/toxic/valuable solvents, no atmospheric release permitted, or powder–air explosion risk. Action: Where lotion/solvent or fine powder dominates, ask whether a closed-cycle or indirect-fired layout (Figures 45.7–45.9) was considered. → 卫材相关性★★★★☆｜Eliminates both odour escape and powder-explosion pathways.

======================================================================

## Chapter 46 — Energy Aspects in Drying

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 46 (Strumiłło, Jones & Zyłła) treats the drying plant as a major, and largely under-optimised, industrial energy consumer. The authors argue that energy costs are structurally rising and that drying deserves a process-oriented, not industry-specific, treatment. They open with the scale of the problem (12% of manufacturing energy on average; paper ≈33%), then build a quantitative framework: unit energy consumption (kJ/kg water), energy efficiency η=E_ev/E_t, thermal efficiency, and Kudra's instantaneous drying efficiency. The heart of the chapter is a databank of savings — Table 46.5 (13→71% stepwise savings) and Table 46.6 (national potential by option) — followed by heat-recovery hardware (wheels, plates, heat pumps, MVR), non-conventional sources, new techniques (two-stage, superheated-steam, RF/microwave), process control, and worked industrial case studies. The through-line: most drying inefficiency is avoidable, and cheap operational fixes (leaks, insulation, airflow) yield 25–50%, while heat recovery reaches 60–71%.

### 核心观点标题

Drying is a top-tier industrial energy consumer

The thermodynamic minimum is far below practice

Energy efficiency has a clean definition

Most heat is wasted in the exhaust, not the walls

Cheap operational fixes give 25–53%, heat recovery gives 64–71%

- 

Heat pumps and MVR are order-of-magnitude better per kWh

### 在书中的作用

Ch46 is the Handbook's energy/economics capstone. It sits between the unit-operation chapters and the plant-engineering chapters (emission control Ch45, cost estimation Ch53, safety Ch48, control Ch49). Tables 46.5–46.8 are the quantitative backbone that Ch53's cost methods build upon, and the "improved dewatering of feedstock = 4% potential" row (Table 46.6) directly motivates Ch50 (mechanical dewatering). It pairs with Ch47 (heat pumps) and Ch49 (control) as the three high-leverage energy chapters for a buyer.

### 卫材行动卡

Overall relevance: ★★★★★ (highest — direct energy-cost argument for pulp/paper, nonwoven and coating lines).

Action Card H46-1 — Benchmark every supplier quote against the 2200–2700 kJ/kg evaporative floor. Insight: p.1079 — theoretical 2200–2700 kJ/kg; actual 2700–8000 kJ/kg. Action: Require suppliers to state specific energy consumption (kJ/kg water evaporated) and reject/penalise offers that cannot justify a gap above the floor. → 卫材相关性★★★★★｜Turns drying-energy cost into a measurable, comparable procurement metric per tonne of pulp/nonwoven.

Action Card H46-2 — Demand the Table 46.5 savings ladder in the bid. Insight: p.1080 — staged 13%→71% savings; heat exchange with condensation reaches 71%. Action: In the technical bid, ask which of schemes 1–8 the design includes; treat omission of exhaust recycle/heat exchange as a cost/quality red flag. → 卫材相关性★★★★★｜Quantifies how much steam (€/tonne) a better design would save on a fluff/paper dryer.

Action Card H46-3 — Specify exhaust-air heat recovery (wheel/plate ≥70–90%). Insight: p.1082 — thermal wheel 75–90%, plate ≥70%, heat pipe/scrubber ≥60%. Action: For any new coating/airlaid/drying oven, require a heat-recovery device with stated efficiency and ask for the energy-balance measurement points (Fig 46.4). → 卫材相关性★★★★★｜Exhaust is the 15–40% loss bucket; recovery is the biggest single saving on hygiene lines.

Action Card H46-4 — Apply the cheap fixes first (leaks, insulation, airflow). Insight: p.1080 — rectify steam leak 13%, reduce air leaks 18%, insulation 26%, insulation+airflow 50%. Action: Before capital projects, audit steam leaks, dryer insulation and airflow rate on existing lines; these need little/no capital. → 卫材相关性★★★★★｜Low-cost, fast-payback wins on running fluff/paper dryers.

Action Card H46-5 — Evaluate heat pump / MVR where low-temperature drying is needed. Insight: p.1085 — SMER heat pump 3 kg/kWh vs convective 0.5–1; MVR 134 kJ/kg, "20 times better than typical adiabatic spray drying" (p.1086). Action: For heat-sensitive webs (lotion, actives, SAP) or where electricity-vs-gas price favours it, ask suppliers about heat-pump/MVR and payback (India 1.5–3 y; Poland marginal). → 卫材相关性★★★★★｜Protects heat-sensitive substrates while cutting energy per kg water.

Action Card H46-6 — Use SMER/COP to compare fuel-type-agnostic bids. Insight: p.1085 — SMER = kg evaporated/kWh; theoretical max 1.55, heat pump 3, convective 0.5–1. Action: Require all bidders to report SMER (or equivalent water/kg-energy) so gas, steam and electric dryers are compared on one denominator. → 卫材相关性★★★★★｜Enables apple-to-apple energy comparison across fuel types.

Action Card H46-7 — Push dewatering upstream (links to Ch50). Insight: p.1081 — "Improved dewatering of feedstock: 5.3×10⁹ MJ/y, 4%, High" penetration. Action: Where the line includes a press/centrifuge/Thune section, demand the highest feasible mechanical dewatering before the dryer; it is a high-penetration, low-cost lever. → 卫材相关性★★★★★｜Mechanical water removal is far cheaper than evaporation — the dominant cost lever before the dryer.

Action Card H46-8 — Insist on finishing at max acceptable final moisture. Insight: p.1090 — "the drying should be finished at the maximum material moisture content that is acceptable"; over-drying wastes energy and raises explosion risk. Action: Set the residual-moisture spec deliberately (not conservatively) and require control to hold it (see Ch49). → 卫材相关性★★★★☆｜Over-drying fluff/SAP wastes energy and increases dust-explosion hazard.

======================================================================

## Chapter 47 — Heat Pump Drying Systems

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 47 (Chou & Chua) presents the heat-pump dryer (HPD) as an energy-recovering, low-temperature drying route whose two decisive advantages are (a) recovery of latent heat from the moisture-laden exhaust and (b) precise control of drying-gas temperature and humidity (p.1101). The authors build from refrigeration basics (COP, Carnot limit, SMER) through configurations (batch/continuous, single/two-stage), real-time quality control, time-varying operating schemes (intermittent, cyclic — saving 25–61% drying time), and industrial applications (timber, food, fluids, RF/IR/solar-assist, vacuum). Table 47.1 is the headline comparison: HPD SMER 1.0–4.0 kg/kWh and drying efficiency 95% vs hot-air 0.12–1.28 and 35–40%. The economics section shows HPD can cut operating cost up to 70% versus a recuperative dryer, with payback 2–3 y (p.1126). For hygiene lines, HPD is the route that protects heat-sensitive substrates (lotion, actives, SAP) while recovering energy.

### 核心观点标题

HPD's edge is exhaust energy recovery + humidity/temperature control

HPD beats hot-air drying on SMER and efficiency by a wide margin

Low temperature protects heat-sensitive products

Practical COP is only 40–50% of Carnot

Time-varying (intermittent/cyclic) operation saves time and energy

- 

HPD cuts operating cost up to 70% with 2–3 y payback

### 在书中的作用

Ch47 is the practical energy-efficiency chapter that operationalises Ch46's heat-recovery principle via a concrete technology, and the low-temperature counterpart to Ch48's safety concerns (low-temp drying also reduces fire/explosion risk). It complements Ch46 (energy) and Ch53 (cost) by giving both the SMER/efficiency evidence and the payback economics a strategist needs to choose HPD over convection. Its quality-control sections (§47.8, §47.9.6) also foreshadow Ch49 (control).

### 卫材行动卡

Overall relevance: ★★★★☆ (genuine energy-efficiency + low-temperature route that protects heat-sensitive substrates; slightly below Ch46/Ch50/Ch53 because HPD suits low-airflow ovens, not high-volume spray).

Action Card H47-1 — Specify HPD where low-temperature drying protects actives/lotion/SAP. Insight: p.1104 — HPD dries at –20 to 100°C, RH 15–80%, "significantly improve product quality by drying at low temperatures." Action: For coating/airlaid lines carrying heat-sensitive lotion or actives, require an HPD (or low-temp dehumidifying) option and compare against convection on product quality, not just cost. → 卫材相关性★★★★★｜Low-temp HPD avoids thermal degradation of actives and lotion on hygiene webs.

Action Card H47-2 — Benchmark bids on SMER (kg water/kWh), not COP. Insight: p.1104 — actual COP is only 40–50% of Carnot; HPD SMER 1.0–4.0 (Table 47.1). Action: Require every HPD bid to state SMER and discount any COP claim by ~50%; compare to convective 0.5–1 kg/kWh (Ch46). → 卫材相关性★★★★★｜Common denominator to rank HPD vs convection per kg water.

Action Card H47-3 — Use Table 47.1 to justify HPD capital on efficiency. Insight: p.1107 — HPD drying efficiency 95% vs hot-air 35–40%; running cost Low vs High. Action: In the capital request, cite the 95% vs 35–40% efficiency gap as the OPEX-saving basis for the higher HPD capital. → 卫材相关性★★★★★｜Quantifies the efficiency premium justifying HPD spend.

Action Card H47-4 — Exploit the 70% OPEX-cut / 2–3 y payback economics. Insight: p.1126 — HPD "reduce the operating cost as much as 70%"; 200 kg/h unit payback 2–3 y; payback shortens as exhaust RH rises 0.4→0.7 (3.2→2.0 y). Action: Model HPD payback using your line's exhaust humidity (more recoverable moisture = faster payback); pair with Ch53 FCI method. → 卫材相关性★★★★★｜Turns HPD into a defensible energy-saving capital case.

Action Card H47-5 — Use time-varying drying to cut time and protect quality. Insight: p.1111 — intermittent profiles save 25–61% drying time; §47.9.6 reduces colour change up to 87% and AA loss up to 20%. Action: For quality-critical webs, request an intermittent/cyclic temperature schedule with feedback control rather than fixed-temperature operation. → 卫材相关性★★★★☆｜Cuts energy/time and reduces heat-induced quality damage on coated webs.

Action Card H47-6 — Prefer ammonia/propane/CO₂ refrigerants. Insight: p.1123–1124 — natural fluids (NH₃ R717, propane R290, CO₂, steam/air) have zero ODP/GWP; ammonia favourable 30–80°C. Action: Specify ozone-friendly refrigerant in any HPD purchase to avoid CFC/HCFC phase-out risk. → 卫材相关性★★★★☆｜Future-proofs the refrigerant choice against regulation.

Action Card H47-7 — Consider one-HP-multiple-chamber architecture. Insight: p.1128 — single low-capacity HP serving several chambers cuts capital; HP runs near-optimal while chambers dry at different rates. Action: Where several low-temp ovens exist, evaluate a shared HP with sequential air scheduling instead of per-oven units. → 卫材相关性★★★★☆｜Capital-saving deployment for multi-oven hygiene plants.

Action Card H47-8 — Verify HPD suitability (low airflow) before specifying. Insight: p.1102 — HPD "not suited for HP operation" for dryers needing large drying air (flash/spray). Action: Confirm the target hygiene oven is low-airflow (coating chamber, airlaid, tray) before committing to HPD; otherwise use Ch46 exhaust recovery. → 卫材相关性★★★★☆｜Avoids misapplying HPD to high-airflow dryers.

======================================================================

## Chapter 48 — Safety Aspects of Industrial Dryers

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 48 (Markowski & Mujumdar) treats dryer safety as a three-factor problem — process, engineering, and management — and argues that drying is "particularly prone to fire and explosion hazards because it is a process in which external heat sources are applied." It first establishes the fire-triangle (fuel, oxygen, ignition source), then gives a material-characterization procedure: explosibility (oxygen balance, flammability), combustibility (CIBA-Geigy rating), dust-explosion characteristics (MEC, MIT, MIE, P_max, (dP/dt)_max, K_st) with an extensive dust table, and thermal-decomposition/self-heating onset (T_A/T_L/T_B via DTA/DSC). The engineering factor covers prevention (inerting, dust-cloud avoidance, ignition-source exclusion) and protection (venting, suppression, containment, isolation). The management factor closes the loop with operation, maintenance, training, ATEX, and SIL-rated reliability. For a hygiene reader the chapter is a direct hazard handbook for fluff-pulp defibration dust and polyacrylate SAP powder.

### 核心观点标题

Drying is inherently fire/explosion-prone; dryers are a top dust-explosion location

Three conditions must coincide for fire/explosion

Most dried powders are type-3 (combustible) and dryable only with control

Dust-explosion violence is quantified by P_max, (dP/dt)_max, and K_st

Polymer dusts are low-MIE, easily ignited by static; bag filters need conductive fibers

Inerting and self-inertizing remove the oxygen leg

Thermal-decomposition onset (T_A/T_L/T_B) sets the safe operating temperature

- 

Build safety in at design; retrofit is costly; secondary dust explosion is devastating

### 在书中的作用

Ch48 is the plant-safety capstone paired with Ch49 (control), Ch44 (feeding), and the emission-control Ch45. It supplies the hazard vocabulary (MIE, MEC, K_st, MIT, T onset) that Ch49's spray-dryer safety interlocks (p.1169) assume. For the hygiene reader it is the reference for two real line hazards — fluff-pulp defibration dust and SAP powder — and complements procurement specs that must demand venting/isolation/inerting rather than hope.

### 卫材行动卡

Overall relevance: ★★★★★ (direct, quantified hazard data for fluff-pulp defibration dust and SAP/polymer powder — two real hazards on hygiene lines).

Action Card H48-1 — Require a dust-explosion data sheet (MEC/MIT/MIE/K_st) for every powder handled. Insight: p.1138 K_st = (dP/dt)_max·V^(1/3); Table 48.4 gives PE St2 (516), PP St1 (356), cellulose acetate, nylon, PVA. Action: Demand suppliers certify MEC, MIT, MIE, P_max, (dP/dt)_max and St class for fluff pulp, SAP, and any polymer fines; treat untested SAP as ≥St1. → 卫材相关性★★★★★｜Defines the legal/engineering explosion-protection basis for SAP/fluff powder handling.

Action Card H48-2 — Ground all synthetic-fibre filter bags and bonding; conduct static audit. Insight: p.1138 "majority of incidents occur with sparks having ignition energy below 25 mJ"; p.1147 "synthetic fibres used in bag filters may be reduced [in resistance] by adding some steel or carbon fibers." Action: Specify bag filters with steel/carbon fibres and verified grounding; audit for MIE<25 mJ spark sources (SAP MIE ~10 mJ class). → 卫材相关性★★★★★｜SAP/PP/PE fines + synthetic nonwoven bags are a static-ignition dust-explosion pair.

Action Card H48-3 — Size vents by K_st / cube-root law, not by guess. Insight: p.1148–1149 Table 48.8 plastics → 1/5 vent ratio; K-factor and cube-root scaling from 1.2-L Hartmann to plant volume. Action: In dryer/cyclone/baghouse specs, require vent area sized to the powder's K_st (plastics 1/5), with P_stat ≈ 10 kPa. → 卫材相关性★★★★★｜Converts abstract explosion risk into a dimensioned, code-grade requirement.

Action Card H48-4 — Specify inerting or self-inertizing for solvent/closed powder loops. Insight: p.1146 inerting with N₂/CO₂ "decreases the maximum explosion pressure and retards the rate of pressure rise"; exhaust recycle "self-inertizing" also improves thermal efficiency. Action: For coating-oven or SAP spray dryers using solvent, require N₂/closed-cycle or exhaust-recycle inerting to MOC. → 卫材相关性★★★★★｜Removes the oxygen leg for solvent-borne coatings and fine powders.

Action Card H48-5 — Set operating-temperature margins from thermal-onset data. Insight: p.1140 DTA/DSC onset T_A/T_L/T_B; p.1144 Table 48.7 layer T_L−20°C, bulk T_B−50°C, vapour VC<25% LFL. Action: Require the dryer spec to state the material's decomposition/MIT onset and operate with the prescribed margin (e.g., 50–80°C below MIT). → 卫材相关性★★★★★｜Prevents thermal decomposition of SAP/PP/PE during drying.

Action Card H48-6 — Mandate explosion isolation + housekeeping against secondary explosions. Insight: p.1157 "The secondary explosion … caused by dust deposition on surrounding surfaces, is always devastating; the importance of good housekeeping cannot be overemphasized." Action: Require fast knife-gate isolation between interconnected vessels (dryer→cyclone→baghouse) and a written deposit-cleaning schedule. → 卫材相关性★★★★★｜Secondary dust explosion is the real killer; isolation+cleaning is daily defense.

Action Card H48-7 — Demand SIL3-rated protection and ATEX categorization. Insight: p.1153 "category 1 (dryers) … SIL3 is assigned, i.e., probability of failure on demand is from 10⁻⁴ to 10⁻³/y"; p.1154 EU ATEX 94/9/EC mandatory risk assessment. Action: Make SIL3 and ATEX risk-assessment documentation a contractual acceptance criterion for any dryer on a hygiene line. → 卫材相关性★★★★☆｜Aligns supplier with regulatory and reliability expectations.

======================================================================

## Chapter 49 — Control of Industrial Dryers

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 49 (Jumah, Mujumdar & Raghavan) frames dryer control as the discipline of holding exit-product quality — above all residual moisture — within specification despite disturbances, at minimum cost and energy. It opens by noting most industrial dryers still use simple strategies (e.g., exhaust-gas temperature for a direct dryer) while large, fast, or tight-spec units need automatic control; drying is "inherently self-regulating" only when inputs are invariant. The authors then define control objectives (accuracy, stability, speed of response, robustness), synthesise multivariable loops, and survey conventional schemes (manual, feedback, feedforward, feedforward–feedback, model-based, microprocessor) plus per-dryer implementations (batch, rotary, spray, conveyor, flash, fluid-bed, grain). The chapter closes with intelligent-control outlooks (expert, fuzzy, neural). Its central, hygiene-relevant thesis: product moisture is the right controlled variable but is hard to sense online, so plants fall back on indirect temperature/humidity control that "usually results in poor control."

### 核心观点标题

Most dryers still use crude, indirect control; tight-spec lines need automation

Drying only "self-regulates" when everything is invariant

Moisture is the right output but is hard to measure; indirect control is poor

Indirect temperature control correlates weakly with moisture

Dead time defeats feedback; feedforward/predictive is the remedy

Model-based control beats PID under feed-moisture swings

- 

Spray dryers carry explosion/flooding interlocks, not just temperature control

### 在书中的作用

Ch49 is the control/automation capstone of the Handbook. It complements the unit-operation chapters (spray, fluid-bed, flash, rotary, conveyor, grain) by treating the feedback layer every production dryer needs and by explicitly referencing those dryer types. It pairs with Ch48 (safety interlocks appear here as alarm/feed-failure duties) and with Ch44 (feeding sets the load/disturbance the controller must reject). For the hygiene reader it is the bridge between the drying physics of earlier chapters and the line-level spec compliance (residual moisture, throughput, energy) a procurement strategist must demand.

### 卫材行动卡

Overall relevance: ★★★★★ (highest in this batch — directly governs how a residual-moisture spec is held on a running line; applicable to airlaid ovens, coating dryers, pulp dryer sections, SAP/spray steps).

Action Card H49-1 — Demand a real moisture loop, not a temperature-only loop. Insight: p.1162 — indirect temperature/humidity control "usually results in poor control"; exhaust-T-alone "may even lead to serious failure." Action: In supplier audits, require a measured product-moisture or at minimum concurrent exhaust-T + humidity control; reject temperature-only loops for tight-spec webs. → 卫材相关性★★★★★｜Holding residual moisture on fluff/SAP/coated web is the spec; a thermocouple alone cannot guarantee it.

Action Card H49-2 — Specify feedforward on measured feed moisture for pulp/airlaid lines. Insight: p.1163 — large dead time defeats feedback; feedforward measures disturbance and compensates pre-emptively; p.1173 MBC avoids instabilities from "frequent and large variations in the feed moisture content." Action: Require the control narrative to show a feed-moisture sensor feeding a feedforward or MBC term. → 卫材相关性★★★★★｜Variable lap-pulp/airlaid feed moisture is the dominant disturbance; feedforward prevents under/over-dry.

Action Card H49-3 — Apply the Shinskey wet-bulb rule if forced to control on temperature. Insight: p.1170 — X_p = K ln[(T_i−T_w)/(T_o−T_w)]; hold (T_o−T_w)/(T_i−T_w) constant. Action: Where a moisture analyzer is not yet installed, insist the temperature loop also tracks humidity (wet-bulb) so it respects Eq 49.5. → 卫材相关性★★★★☆｜Interim safeguard that avoids the p.1162 single-instrument failure mode.

Action Card H49-4 — Couple safety interlocks into the dryer control spec. Insight: p.1169 — spray/flash loops need feed-failure shutdown, water-to-nozzle on over-temp, and alarms for "explosion, product plugging, flooding, high temperature, and loss of airflow." Action: Make explosion/feed-loss/alarm interlocks a contractual control requirement (links to Ch48). → 卫材相关性★★★★★｜SAP/spray/fines steps are combustible-dust and feed-loss risks; control and safety must be one package.

Action Card H49-5 — Use MBC/inferential as the upgrade target for off-spec/rework reduction. Insight: p.1173 — MBC "functions better than either PID feedback control or lead/lag feedforward control" under feed swings; p.1166 Kalman observer estimates moisture from T/flow under noise. Action: Frame any capex for an analyzer + model-based controller as rework/off-spec reduction, quantified against current PID variance. → 卫材相关性★★★★★｜Directly reduces off-spec SAP/fluff and drying energy.

Action Card H49-6 — Set the dead-time expectation for fluff-pulp dryer sections. Insight: p.1163 — rotary/floater/pulp-sheet and Yankee/tissue contact dryers have long thermal inertia/dead time that breaks simple feedback. Action: When specifying pulp dryer sections, require feedforward or model-based compensation and a stated dead-time handling, not naive PID. → 卫材相关性★★★★☆｜Fluff-pulp drying lines have exactly the dead-time pathology the chapter warns about.

======================================================================

## Chapter 50 — Solid–Liquid Separation for Pretreatment of Drying Operation

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 50 (Shirato & Iwata) argues that mechanical solid–liquid separation is the most powerful pretreatment of a drying operation: removing water mechanically is vastly cheaper than evaporating it thermally. The authors frame the field via Table 50.1 (conditioning → concentration → separation → posttreatment), then present the selection logic keyed to cake-formation rate (Table 50.2), the Ruth filtration theory (Eqs 50.1–50.7, including cake compressibility α=α₀pⁿ), and a practitioner's catalogue of batch, semi-continuous and continuous filters, centrifugal filters, and expression (pressing) equipment. The economic spine is explicit: "it is essential to balance the additional cost of producing a dry cake against the thermal requirements of dryers" (p.1183). For pulp/paper and wet-laid/hydroentangled nonwoven lines, this is the press-section-vs-dryer-section trade-off made quantitative — every kilogram of water squeezed out upstream never has to be evaporated downstream.

### 核心观点标题

Dewatering and drying are complementary; dewatering is the cheap half

The central economic rule: balance dewatering cost against dryer thermal load

Filtration resistance is governed by cake compressibility

Smaller particles mean wetter cake and slower filtration

Expression (pressing) removes extra water by compression, not pumping

- 

Selection is dictated by cake-formation rate

### 在书中的作用

Ch50 is the upstream economic lever that Ch46 (energy) and Ch53 (cost) depend on: lower evaporation load W → smaller, cheaper dryer (Ch53 scaling) and lower thermal energy (Ch46). It is the quantitative anchor for the Table 46.6 "Improved dewatering of feedstock: 4% national potential, High penetration" row. Paired with Ch46 it gives the complete energy story: dewater mechanically, then evaporate the remainder efficiently.

### 卫材行动卡

Overall relevance: ★★★★★ (the single biggest lever in drying economics — mechanical dewatering is far cheaper than evaporation).

Action Card H50-1 — Treat the press/centrifuge as stage 1 of the dryer, optimise the boundary. Insight: p.1183 — "balance the additional cost of producing a dry cake against the thermal requirements of dryers." Action: Model the line as dewatering+drying; move the dewatering/drying boundary until marginal press cost = marginal dryer thermal saving (using Ch46 kJ/kg and Ch53 $/t). → 卫材相关性★★★★★｜Every kg mechanically removed never gets evaporated — the dominant cost lever.

Action Card H50-2 — Use Table 50.2 to right-size the dewatering stage. Insight: p.1184 — selection by cake-formation rate: fast (>1 cm/min, >20%) → continuous vacuum/belt; slow (<0.12 cm/min) → pressure; dilute → thickening first. Action: Characterise your slurry's cake-formation rate and concentration, then pick the filter class from the matrix; avoid over-specifying a pressure filter for a fast slurry. → 卫材相关性★★★★★｜Matches dewatering equipment to actual fluff/SAP/nonwoven slurry.

Action Card H50-3 — Check cake compressibility before buying higher pressure. Insight: p.1185 — α=α₀pⁿ; n 0.1–0.8; for compressible cakes rate is pressure-independent (Eq 50.5). Action: Determine n for your slurry; if compressible, invest in conditioning (flocculant/pH/temperature) rather than a higher-pressure press. → 卫材相关性★★★★★｜Avoids wasteful high-pressure capital on fine cellulose/SAP flocs.

Action Card H50-4 — Add a mechanical-expression stage for fine cakes. Insight: p.1183 — vacuum filter alone limited on small particles "unless an additional unit for mechanical expression was available"; expression 0.6–2.5 MPa (p.1197). Action: For fine pulp/SAP cakes, specify a membrane/diaphragm filter-press (two-step filtration then consolidation, p.1197) to reach low residual moisture. → 卫材相关性★★★★★｜Last cheap water before the expensive dryer.

Action Card H50-5 — Condition the slurry to enlarge particles. Insight: p.1185 — flocculation/coagulation, polyelectrolytes, pH, temperature, freezing increase particle size → higher filtration rate, lower cake moisture. Action: Trial flocculant/pH adjustment on the wet-laid or pulp slurry to cut downstream dryer load. → 卫材相关性★★★★★｜Cheapest moisture reduction is at the feed, not the dryer.

Action Card H50-6 — Consider centrifugal dewatering for high-throughput solids. Insight: p.1196 — peeler/siphon centrifuges give "large throughput capacities"; siphonic action accelerates filtration (10-m water-column suction at 500g, p.1196). Action: For continuous high-volume dewatering (e.g., pulp), evaluate pusher/peeler centrifuges against filters on $/t and residual moisture. → 卫材相关性★★★★☆｜High-capacity mechanical dewatering option for pulp lines.

Action Card H50-7 — Specify cake washing where product purity matters. Insight: p.1183 — cake washing by displacement or reslurry; plate-and-frame "most cost-effective" for high washing (p.1183). Action: For SAP or surfactant-containing streams, require a wash stage in the filter spec to remove soluble impurities before drying. → 卫材相关性★★★★☆｜Washing at dewatering stage protects final product purity.

Action Card H50-8 — Use the cost-balance to defend dewatering capex in the bid. Insight: p.1183 balance rule + Ch46 energy floor 2200–2700 kJ/kg. Action: In capital requests, quantify the dryer-energy saved (kg water × 2200–2700 kJ) by the proposed dewatering upgrade to justify the press/centrifuge spend. → 卫材相关性★★★★★｜Turns a dewatering purchase into a defensible energy-saving investment.

======================================================================

## Chapter 51 — Industrial Crystallization

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 51 (Palosaari, Louhi-Kultanen & Sha) is an overview of industrial crystallization from solution, written from the perspective of facilitating downstream operations — especially filtration and drying. Its organizing thesis (p.1202) is that "the easy dewatering and drying of crystals requires that the crystals be of a uniform and sufficiently large size." The chapter develops the fundamentals (solubility/supersaturation, metastable zone, nucleation, CSD, crystal shape, purity, polymorphism), then the control levers for CSD and habit (supersaturation programming, seeding, precipitation, continuous schemes such as clear-liquor advance, fines destruction, classified removal, mixing intensity), then industrial crystallizer types (batch, FC/DTB/FB), filtration of crystal suspensions, and finally crystal drying and CFD/advances. For the hygiene reader this is not a drying process; its value is conceptual — nucleation/growth kinetics, supersaturation control, and habit/polymorph modification transfer as the small-molecule analogue of polymer crystallization and of solid-form control for actives.

### 核心观点标题

Crystal size & uniformity are set for the sake of downstream drying/filtration

Supersaturation drives growth, nucleation, agglomeration, shape, and purity

Small crystals are hard to dewater/dry; porosity/roughness matter

Slow growth yields purer crystals; inclusions lower purity

Polymorphism: same composition, different solid form and properties

Seeding with the right size/mass controls nucleation

Fines destruction widens CSD but grows larger mean crystals

- 

Drying favours ~1 mm crystals; above that is harmful

### 在书中的作用

Ch51 is the sole solids-formation chapter adjacent to the drying unit operations. It complements Ch52 (frying) and the spray/flash/fluid-bed chapters by treating the upstream particle-generation step whose output those dryers would handle. Where Ch49 (control) and Ch48 (safety) govern the dryer, Ch51 governs the crystalline feedstock's size/purity/habit — relevant to any hygiene line that receives or produces a crystalline active, salt, or filler.

### 卫材行动卡

Overall relevance: ★★☆☆☆ (weak-to-moderate — not a drying process; value is conceptual transfer of nucleation/growth, supersaturation control, habit/polymorph thinking, and the size↔filterability↔drying trade-off to polymer crystallization and powder-product design).

Action Card H51-1 — Use the nucleation/growth lens for polymer crystallization on cooling. Insight: p.1203–1204 supersaturation drives nucleation vs growth; metastable-zone width sets nucleation ease; L₅₀ = 3.67 Gτ (Eq 51.8). Action: When specifying cooling of PP/PET/PLA (PoP Ch1/Ch7/Ch8), treat undercooling as the supersaturation analogue and use nucleating agents/seeds to set crystalline structure rather than accepting random spherulites. → 卫材相关性★★★｜Reframes polymer crystallisation as a controllable nucleation/growth problem.

Action Card H51-2 — Respect the ~1 mm sizing window for powders/granules. Insight: p.1218 crystals best ~1 mm+ but ">1 mm tend to be harmful" (centrifuge breakage, lost supersaturation surface). Action: Set SAP/actives granule-size spec inside a band where filtration, drying, and attrition are all acceptable rather than "as large as possible." → 卫材相关性★★★｜Concrete sizing-band lesson portable to powder-product specs.

Action Card H51-3 — Expect mother-liquor/solvent inclusions to raise impurity. Insight: p.1206 agglomeration "may contain inclusions of the mother liquor, which decreases the purity"; slow growth = purer. Action: For spray-crystallized or precipitated actives on a hygiene line, control growth rate and wash the cake to minimize trapped solvent (VOC/residual concern). → 卫材相关性★★☆｜Analogue of residual monomer/solvent in polymer particles.

Action Card H51-4 — Apply the Kozeny–Carman scale to fine-powder filtration. Insight: p.1216 "If the particle diameter drops to 10% of its original value, the pressure drop increases by 100-fold." Action: When a fine SAP/actives fraction is generated, anticipate a 100× filtration-pressure penalty and size the filter or coarsen the fraction accordingly. → 卫材相关性★★☆｜Quantifies why sub-10 µm fractions are costly to separate.

Action Card H51-5 — Note polymorphism thinking for solid-form actives. Insight: p.1206 polymorphism = same composition, different solid form/dissolution; supersaturation can select polymorph (p.1221). Action: If a hygiene actives ingredient crystallizes, document its polymorphic form and the cooling/solvent path that locks it in, to keep dissolution stable. → 卫材相关性★★☆｜Solid-form control concept, not a drying lever.

Note: No operational dryer-control or safety content here; pair this chapter with Ch49 (control) and Ch48 (safety) for the actual drying line, and with the PoP cross-reference below for the polymer-crystallization link.

======================================================================

## Chapter 52 — Frying of Foods

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 52 (Oreopoulou, Krokida & Marinos-Kouris) treats deep-fat frying as an industrial unit operation built on simultaneous heat and mass transfer: a hot-oil bath heats the food surface by convection, conducts heat inward, vaporizes internal water that escapes as bubbles, and lets oil migrate into the vacated pore space. Its spine is the four-stage Farkas picture — initial heating, surface boiling, falling-rate, bubble-end-point — in which a dry crust nucleates at the surface, thickens inward, and pins the core near the boiling plateau while the dried region runs above 100°C. The chapter then develops transport models (1-D conduction, moving-boundary crust/core), mass-transfer kinetics for moisture loss and oil uptake, oil thermo-physical/chemical properties, industrial fryer hardware, process windows, and shelf life. For the hygiene reader this is the weakest chapter in the book: except for the crust-formation / case-hardening mechanism, its content (food, oil, flavour, nutrition) has essentially no substrate relevance, and Sections 5 and 11 say so plainly.

### 核心观点标题

Frying is simultaneous heat & mass transfer with a moving evaporation front

The process runs through four stages, ending in a falling-rate period

The crust/core interface sits near 102–103°C while the core is pinned at the boiling point

Crust formation is coupled to oil penetration: ingress competes with egress

Case-hardening: a surface skin seals the interior before it is done (the one transferable idea)

- 

Temperature/rate sets crust thickness versus interior cook

### 在书中的作用

Ch52 is the single food-specific, oil-medium drying chapter and closes the set. It sits beside Ch51 (crystallization) and the spray/flash/fluid-bed chapters as another non-conventional drying mode, but unlike them it shares almost none of the hygiene reader's concerns: no web, no fluff pulp, no SAP, no air/contact dryer, no through-dry or impingement control. Its only honest contribution to the book's hygiene arc is conceptual — the crust-formation / case-hardening mechanism as a transport-phenomenon archetype (see Section 9 and 11). It does not parallel Ch49 (control) or Ch48 (safety) in any operational sense.

### 卫材行动卡

Overall relevance: ★☆☆☆☆ (weakest chapter in the book for this reader). Substrate relevance is otherwise low — frying is hot-oil cooking of food, not web/air/contact drying of fluff pulp, SAP, or nonwovens. The only transferable idea is the crust-formation / case-hardening mechanism (rated up to ★★★ as a concept), used below as a defect-mode lens. No diaper/fried-food application is invented.

Action Card H52-1 — Use case-hardening as a drying-defect diagnostic. Insight: p.1234 "food begins to case harden"; p.1225 crust "moves towards inside" while core stays at boiling point. Action: When a coated web or thick core shows a set surface over a moist interior, diagnose it as case-hardening (a surface skin whose falling permeability throttles interior egress) rather than "under-drying time," and relax the surface heat flux / slow the ramp. → 卫材相关性★★★｜The one portable mechanism: surface-barrier choke of interior drying.

Action Card H52-2 — Control surface-barrier formation via rate, not just time. Insight: p.1234 "crust thickness … depend greatly on frying temperature. Higher temperatures result in a thinner crust layer"; p.1239 too-low T "allows too much fat to penetrate the crust before the interior is cooked." Action: Tune the drying ramp so the surface does not skin over before the interior is processed; treat crust thickness as a rate variable, not a fixed outcome. → 卫材相关性★★★｜Rate/barrier trade-off applies to hot-surface drying of hygiene layers.

Action Card H52-3 — Expect a boiling plateau in thick wet substrates. Insight: p.1225 "moist core … cannot exceed the boiling point of the liquid phase"; p.1227 interface held at 102°C. Action: When drying thick cores, assume the centre sits near the boiling/wet-bulb plateau while the shell heats; size residence time for interior removal, not shell temperature. → 卫材相关性★★☆☆☆｜Falling-rate / plateau thinking, not a hygiene number.

Note: No operational dryer-control, safety, or fluff/SAP content here. Pair any real drying work with Ch49 (control), Ch48 (safety), and the air/through-dry chapters; treat Ch52 only as the case-hardening analogy in Section 9.

======================================================================

## Chapter 53 — Cost-Estimation Methods for Drying

### 概述

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 53 (Sztabert & Kudra) turns drying engineering into a purchasable, defensible estimate. The authors note that reliable fixed-capital-investment (FCI) and operating-cost estimates are essential for equipment selection and competitive comparison, and that the dryer is only one component of a system that may include preprocessing, feeders, gas cleaners and solvent recovery. They present shortcut empirical methods: inflation correction via the Marshall & Swift (M&S) and Chemical Engineering (CE) indices (Table 53.1), capacity scaling with exponent n (Eq 53.2; n≈0.6 default; Table 53.2), installed-cost factors (2.25× FOб for carbon steel, 2.75× for stainless), and a full fixed/variable cost factor method (§53.3–53.4). The chapter culminates in a complete worked example — a spray dryer for laundry detergent — that produces a bottom-line $0.089/kg unit drying cost (fixed $41.09/t + variable $47.78/t). The through-line for a buyer: every quote can be normalised to FCI, annual fixed cost, and unit cost per tonne, then benchmarked.

### 核心观点标题

The dryer is only one part of a costed system

Inflation must be corrected before any number is reused

Capacity scales with a sub-unity exponent

Installed cost is ~2.25–2.75× the equipment FOB price

Material of construction is a 1.5–3× cost multiplier

- 

The worked example yields a fully-loaded unit cost

### 在书中的作用

Ch53 is the procurement/economics capstone. It operationalises the energy data of Ch46 (specific energy → utility cost) and the dewatering lever of Ch50 (lower evaporation load → smaller, cheaper dryer) into dollars. It pairs with Ch46 (energy) and Ch47 (heat-pump economics) and underpins any "should we buy/recover/upgrade" decision a strategist faces. It closes the loop the rest of the book opens: unit operation → energy → cost → decision.

### 卫材行动卡

Overall relevance: ★★★★★ (turns drying engineering into a purchase argument — the procurement strategist's core chapter).

Action Card H53-1 — Demand the full cost ladder, not just an equipment price. Insight: p.1250 — total direct cost ≈ 2.25× (CS) or 2.75× (SS) FOB; FCI can be 3× equipment (p.1250). Action: Require every bid to state FOB, installed, direct and FCI separately; rebuild the ladder yourself from any lone FOB number. → 卫材相关性★★★★★｜Prevents under-scoped bids on coating/airlaid/drying systems.

Action Card H53-2 — Index-correct every historical or competitor quote. Insight: p.1246 — Updated cost = Original × (M&S_now / M&S_then); M&S 895 (1989) → 1178 (2004). Action: Before comparing suppliers or old internal estimates, normalise all to the current M&S/CE index. → 卫材相关性★★★★★｜Apples-to-apples cost comparison across years and vendors.

Action Card H53-3 — Use n≈0.6 to right-size and challenge linear pricing. Insight: p.1246 — cost scales as capacity^n, n≈0.6; Table 53.2 gives device-specific n. Action: When a supplier prices per-tonne linearly with capacity, apply the 0.6 exponent to test realism; use it to choose between one large vs two small dryers. → 卫材相关性★★★★★｜Avoids overpaying for scale; supports right-sizing fluff/nonwoven lines.

Action Card H53-4 — Quantify the stainless premium explicitly. Insight: p.1249 — 304-SS costs 1.5–1.7× carbon steel; titanium 2–3×. Action: In specs, separate "carbon-steel-equivalent" base price from the material upcharge so the corrosion/residue justification is visible. → 卫材相关性★★★★★｜Hygiene lines need stainless/clad; makes the premium a negotiable, justified line item.

Action Card H53-5 — Require the fixed+variable unit-cost decomposition ($/t dry product). Insight: p.1257 — example totals $41.09/t fixed + $47.78/t variable = $0.089/kg. Action: Mandate that each bid report annual fixed cost, annual variable cost, and unit cost per tonne of dry product, so offers are comparable regardless of dryer type. → 卫材相关性★★★★★｜Single normalised metric to rank fluff-pulp / nonwoven dryer options.

Action Card H53-6 — Separate the energy line to link with Ch46 savings. Insight: p.1256 — fuel $1,004,400 + electricity $86,184 dominate variable cost; energy price volatile (Eq 53.6). Action: In the variable-cost table, isolate fuel and electricity so Ch46 heat-recovery / exhaust-recycle savings can be dropped straight into the model. → 卫材相关性★★★★★｜Directly quantifies payback of energy-saving retrofits in $/t.

Action Card H53-7 — Apply the labor rule to compare batch vs continuous. Insight: p.1251 — batch: 2 man-h/m³ + 1/3 man/dryer/shift; continuous automatic: 1/2 man/dryer/shift. Action: Use the rule to estimate labor cost difference between batch and continuous drying of the same hygiene product. → 卫材相关性★★★★☆｜Labor is a real variable-cost differentiator for sizing/automation decisions.

Action Card H53-8 — Use contingencies and owner costs to set a bid tolerance. Insight: p.1251 — contractor fee 10–27%, contingencies 10–30%, owner costs 5–15% of direct cost. Action: Build a +30% pessimistic band on any preliminary FCI (per p.1257 reliability) before committing capital. → 卫材相关性★★★★☆｜Sets realistic capital envelope and guards against surprise overruns.


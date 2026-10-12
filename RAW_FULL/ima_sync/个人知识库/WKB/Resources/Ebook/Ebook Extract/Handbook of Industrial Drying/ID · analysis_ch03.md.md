---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_d94d7f0bfd0f33b272343dc285c3b836001a693ee6c0644e"
source_file: "ID · analysis_ch03.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch03.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch03.md.md

# Chapter 3 — Basic Process Calculations and Simulations in Drying

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21 (the source's own embedded print p.X markers use this offset; e.g., PDF page 72 → print p.51); this is an estimate and should be spot-checked against the print edition.

Chapter 3 (Z. Pakowski & A.S. Mujumdar) is the computational engineering chapter: it teaches the reader to build a mathematical model of a dryer and solve it. It replaces the older graphical/shortcut culture with a computer-oriented methodology (Excel, Mathcad, MATLAB, Mathematica) while insisting the computer "will not relieve one from thinking" (p.52). The chapter is structured as a modeling cookbook: (1) classify the process into one of 16 generic dryer cases by operation type, flow geometry, and flow pattern; (2) assemble the five parts of a deterministic model — balance equations, constitutive (kinetic) equations, equilibrium relations, property equations, geometric relations; (3) solve steady-state input–output or distributed-parameter (DPM) models for cocurrent/countercurrent/cross-flow, including the solid phase with and without shrinkage; (4) apply shortcut methods and software tools. For the hygiene-materials reader this is the chapter that turns Ch.1's definitions and Ch.2's measured coefficients into an actual dryer-size and drying-time calculation — the quantitative core of any new line specification.

## 2. Key Viewpoints (each with page + verbatim quote + interpretation)

### Viewpoint 1 — Drying calculation has migrated to the computer, but judgment remains

- Page: p.52
- Quote: > "Computer tools have become easily available and have replaced the old graphical methods. An entirely new discipline of computer-aided process design (CAPD) has emerged … dedicated software for this process is still scarce. However, general computing tools including Excel, Mathcad, MATLAB, and Mathematica are easily available … we have decided to present here a more computer-oriented calculation methodology and simulation methods than to rely on old graphical and shortcut methods. This does not mean that the computer will relieve one from thinking."
- Interpretation: The chapter's tone is modernising but skeptical of black boxes. For a hygiene engineer, the takeaway is: build your own spreadsheet/Matlab model from the balances here rather than trusting a vendor's sizing; the model is only as good as the Ch.2-measured coefficients you feed it.
### Viewpoint 2 — Three reasons you calculate: design, simulation, optimization

- Page: p.52–53
- Quote: > "Before going into details of process calculations we need to determine when such calculations are necessary in industrial practice. The following typical cases can be distinguished: Design—(a) selection of a suitable dryer type and size … (b) specification of all process parameters … Simulation—for a given dryer, calculation of dryer performance … Optimization—in design and simulation an optimum … is sought."
- Interpretation: These map directly onto a hygiene-line project: (1) pick & size a through-air or fluid-bed dryer, (2) predict throughput/moisture on an existing line, (3) tune temperature/airflow for minimum energy. All three start from the same model.
### Viewpoint 3 — Every model is built from the master balance: Inputs − Outputs = Accumulation

- Page: p.53
- Quote: > "Two classes of processes are encountered in practice: steady state and unsteady state (batch). The difference can easily be seen in the form of general balance equation of a given entity … Inputs − outputs = accumulation (3.1)."
- Interpretation: This is the spine of the whole chapter. In steady state the accumulation term vanishes (algebraic equations); in batch it is an ODE in time; in a distributed model it becomes a PDE. Recognising which case you are in is the first step of any dryer calculation.
### Viewpoint 4 — Lumped vs. distributed: geometry dictates the math

- Page: p.54
- Quote: > "If a property varies continuously along the flow direction … the balance equation can only be written for a differential space element … This is a distributed parameter model (DPM) … in steady state … the model becomes an ODE with respect to space coordinate, and in unsteady state it becomes a PDE. When the volume … is perfectly mixed, all phases inside this volume will have the same property as that at the output. This is the principle of a lumped parameter model (LPM)."
- Interpretation: A thin nonwoven web on a cylinder dryer can be LPM (well-mixed air, uniform web); a deep bed of fluff or a packed SAP column needs DPM. Choosing wrongly mis-sizes the dryer by orders of magnitude.
### Viewpoint 5 — Kinetics enter through the characteristic drying curve or a thin-layer equation

- Page: p.56–57
- Quote: > "In this approach the measured drying rate is represented as a function of the actual moisture content (normalized) and the drying rate in the constant drying rate period: F = f(F) (3.29)." … "Lewis (1921) dX/dt = −k(X − X*) (3.32)" … "Page (1949) … F = exp(−(kt)^n) (3.36)."
- Interpretation: This is where Ch.2's experimental rate curve becomes a constitutive equation. The Lewis (first-order) and Page (empirical) thin-layer equations are the workhorses for simulating a batch of fluff/SAP/nonwoven once X_cr, X*, and k are measured.
### Viewpoint 6 — Psychrometric arithmetic underpins every model

- Page: p.58–59
- Quote: > "The ability to perform psychrometric calculations forms a basis on which all drying models are built … Equation 3.46 and Equation 3.47 are sufficient to find any two missing humid gas parameters from Y, w, t, i, if the other two are given … traditionally done graphically using a psychrometric chart, but they are easy to perform numerically."
- Interpretation: The humid-gas property block (RH, absolute humidity, enthalpy, dew point, adiabatic-saturation and wet-bulb temperatures, Lewis number) is the shared utility routine every balance calls. For a hygiene engineer the practical message: code these once in Excel/Matlab and reuse for every dryer type.
## 3. Research Method & Data Sources

This is a modeling-methodology chapter: it derives and assembles equations rather than reporting experiments, but it is grounded in a large cited literature (Pakowski & Mujumdar's own dryPAK/PAK codes; Lewis 1921; Page 1949; Crank 1975 on diffusion; Langrish et al. 1991 two-segment CDC; Keey 1978; Treybal 1980; Iglesias & Chirife 1984 food isotherms; GAB model; Hasatani & Itaya 1996 drying-induced strain; Perre & Turner 1999 TransPore 3D). Worked numerical examples anchor each model class (e.g., cocurrent flash drying of clay spheres, Fig. 3.16; batch oven dryer, Fig. 3.18; batch fluid bed, Fig. 3.20).

||||||
|---|---|---|---|---|
|Classification|16 generic cases (Fig. 3.1)|Conceptual|Flow-sheet|Exact taxonomy|
|LPM balance|Eqs 3.5–3.8, 3.113–3.120|Ch.2 coefficients|Excel/Matlab ODE|Perfectly-mixed assumption|
|DPM (gas/solid)|Eqs 3.9–3.11, 3.91+|Ch.4 transport + Ch.2 kinetics|PDE/FDM solver|1-D/2-D, continuum|
|Constitutive|CDC (3.29–3.30); Lewis/Page (3.32, 3.36)|Lab rate curve (Ch.2)|Curve-fit|Material-specific|
|Psychrometrics|Eqs 3.45–3.53; GAB (3.56)|Property DB (Tables 3.1–3.2)|Numerical|Ideal gas  bar; air–water only for 3.50|
|Shortcut|Free/bound moisture split (3.10.1)|X*, X_cr|Hand calc|Approximate|

## 4. Argumentation Process

The authors build the modeling edifice in a strict layered order:

- Classify (§3.3): identify operation type (batch/continuous/semicontinuous), flow geometry (parallel/cocurrent/countercurrent/cross), and flow pattern (plug/perfectly mixed) → one of 16 generic cases (Fig. 3.1). This pre-selects the equation template.
- Write balances (§3.4.1): mass (solid Eq. 3.5, gas Eq. 3.6) and energy (solid Eq. 3.7, gas Eq. 3.8; DPM forms Eqs 3.9–3.11). The accumulation term decides ODE vs. algebraic vs. PDE.
- Add constitutive/kinetic equations (§3.4.2): the drying rate is closed by the characteristic drying curve (Eqs 3.29–3.30) or a thin-layer equation (Lewis 3.32, Page 3.36); volumetric rate from TLE (Eqs 3.37–3.40).
- Add auxiliary relations (§3.4.3): psychrometrics (Eqs 3.45–3.53), wet-solid isotherms incl. GAB (Eq. 3.56), and property databases (Tables 3.1–3.2, Antoine/Watson polynomials).
- Solve (§3.5–3.9): steady-state input–output and DPM for cocurrent/countercurrent/cross-flow (§3.6), solid-phase DPM with/without shrinkage (§3.7), batch (oven/fluid-bed/deep-bed, §3.8) and semicontinuous (§3.9) models.
- Shortcut & software (§3.10–3.11): free/bound-moisture split for quick sizing; dryPAK/Matlab/Mathcad tools.
- Conclusion (§3.12): general software makes modeling accessible, but materials databases remain the bottleneck — property data are scattered and often require experimental determination (tying back to Ch.2).
## 5. Role in the Book

Chapter 3 is the quantitative engine of the handbook. It converts Ch.1's vocabulary (X*, X_cr, characteristic curve, bound/unbound moisture) and Ch.2's measured coefficients (h, K, k_m, isotherms) into solvable models, and it supplies the balance/psychrometric subroutines that Ch.5 (spreadsheet-aided design) automates and that Ch.6 (indirect dryers) specialises to conduction heating. It is the chapter a hygiene engineer uses to answer "what size dryer do I need and how long will it take?" for a fluff line, a SAP fluid bed, or a nonwoven through-air oven.

## 6. Strengths & Weaknesses

✅ Strengths:
- A clean, reusable classification scheme (16 generic cases, Fig. 3.1) that removes ambiguity about which equations apply — a genuine practical aid.
- Self-contained balance + constitutive + psychrometric toolkit: a reader can code the whole model from this one chapter.
- Explicit treatment of shrinkage (§3.7.1.2, Fig. 3.15: unrestrained vs. restrained) — rare and directly relevant to drying polymer/film/coating webs that contract.
- Honest about the materials-database gap in the conclusion (p.77–78): "very little has been done in the area of materials databases … an experimental determination of the missing data is necessary" — re-anchoring the whole chapter to Ch.2.

⚠️ Limitations / contestable:
- The psychrometric Lewis-relation shortcuts (Eqs 3.50, 3.52) are air–water only; for other gas–vapor systems "the deviation of WBT from AST is noticeable and can reach several degrees Celsius" (p.59) — a real trap if anyone models solvent (e.g., ethanol/isopropanol) drying of a coated web.
- Continuum assumption throughout ("we will consider each phase as a continuum unless stated otherwise", p.53); bubbling-fluid-bed and pneumatic-conveying are mentioned as exceptions but not modelled — limits direct use for a real SAP fluid bed without the two-phase corrections the authors footnote.
- Shrinking-solids DPM is illustrated but not given in closed form (only the finite-difference mesh, Fig. 3.15); the actual deformation-coupled equations are deferred to the references (Hasatani & Itaya 1996; Kechaou & Roques 1990).
- No validation/uncertainty guidance: the chapter shows "exemplary results" (Figs 3.16–3.25) but gives no rules for how much error to expect when coefficients are uncertain — important because Ch.2 warned those coefficients carry error.
- Examples are agricultural/mineral (clay spheres, grapes, corn, shelled corn), not hygiene materials; a reader must substitute fluff/SAP/nonwoven properties, which the chapter does not supply.

## 7. Key Terms / Concepts

- Deterministic vs. stochastic model: (p.53) "When all process parameters are determined with a probability equal to 1 we have a deterministic model, otherwise stochastic."
- Lumped parameter model (LPM): (p.54) perfectly-mixed volume; ODE in time (batch) or algebraic (steady state).
- Distributed parameter model (DPM): (p.54) property varies along flow; PDE in unsteady state, ODE in space for steady state.
- 16 generic dryer cases: (p.54) combinations of operation type × flow geometry × flow pattern (Fig. 3.1); type-1 (no accumulation) "do not exist in industry."
- Constitutive equation: (p.54) "connect fluxes in the system to respective driving forces" — e.g., the drying-rate expression.
- Characteristic drying curve (CDC): (p.56) F = f(F), with Langrish two-segment form (Eq. 3.30) splitting the falling rate at F_B.
- Thin-layer equation (TLE): (p.56–57) Lewis first-order dX/dt = −k(X−X*); Page empirical F = exp(−(kt)^n).
- Volumetric drying rate: (p.57) w_D·A_V = −(1−«)ρ_S·d/d t(X−X*)·V; links TLE to balance equations.
- Psychrometric core: (p.58–59) RH ω = p_s(t)/P (Eq. 3.45); Y from ω (Eq. 3.46); enthalpy i_g = c_A·Y + c_B·t + Δh_v0·Y (Eq. 3.47); adiabatic-saturation (Eq. 3.49); wet-bulb (Eqs 3.50, 3.52); Lewis number Le = λ/(ρ·c_p·D_AB) (Eq. 3.53).
- GAB isotherm: (p.60) X* = (a·b·c·(a_w)²)/(1−b·a_w)·(1−b·a_w+c·b·a_w) — implicit form solvable for water activity a_w.
- Shrinkage DPM: (p.69) finite-difference mesh with unrestrained vs. restrained shrinkage (Fig. 3.15).
## 8. Micro close-reading (ONE key paragraph)

Source paragraph (p.70, batch-drying oven model setup, §3.8.1):

"The simplest batch dryer is a tray dryer shown in Figure 3.17. Here wet solid is placed in thin layers on trays and on a truck, which is then loaded into the dryer. The fan is started and a heater power turned on. A certain air ventilation rate is also determined. Let us assume that the solid layer can be described by an LPM. The same applies to the air inside the dryer; because of internal fan, the air is well mixed and the case corresponds to case 2d in Figure 3.1. Here, the air humidity and temperature inside the dryer will change in time as well as solid moisture content and temperature."

Sentence-by-sentence breakdown:
1. "The simplest batch dryer is a tray dryer … wet solid is placed in thin layers on trays … loaded into the dryer." — Defines the physical system and the thin-layer geometry.
2. "The fan is started and a heater power turned on. A certain air ventilation rate is also determined." — Fixes the two control inputs (heat duty, airflow) that appear in the energy/mass balances.
3. "Let us assume that the solid layer can be described by an LPM." — The pivotal modeling decision: treat the solid as perfectly mixed (spatially uniform), so its balance is an ODE in time only (Eq. 3.113).
4. "The same applies to the air inside the dryer; because of internal fan, the air is well mixed and the case corresponds to case 2d in Figure 3.1." — The gas phase is also LPM; this pins the model to generic case 2d, selecting the algebraic/ODE template from §3.3.
5. "Here, the air humidity and temperature inside the dryer will change in time as well as solid moisture content and temperature." — States the four unknowns the ODE system (Eqs 3.113–3.120) solves; the gas is fast (small mass) so it is later asymptotically reduced to algebraic form (Eqs 3.117–3.120).

💡 Standout line: "Let us assume that the solid layer can be described by an LPM" — this single assumption is the make-or-break modeling choice. For a thin nonwoven or fluff layer on a tray it is legitimate; for a deep bed or a contracting SAP gel it is not, and the model would have to become a DPM (§3.7). The chapter's whole taxonomy exists to force you to make this call consciously.

## 9. Concept deep-dive

### Core concept A — The 16-case classification and the LPM/DPM decision (§3.3–3.4)

- Definition: every dryer is located by three axes — operation type (batch / continuous / semicontinuous), flow geometry (parallel / cocurrent / countercurrent / cross-flow), and flow pattern (plug / perfectly mixed) — yielding 16 generic cases (Fig. 3.1). Combined with the master balance Inputs − Outputs = Accumulation (Eq. 3.1), this decides whether each phase is an LPM (algebraic/ODE) or a DPM (ODE in space / PDE).
- Operational? Yes — this is the chapter's most reusable procedural step. Before writing any equation, you classify; the classification selects the template.
- Link to other chapters: feeds Ch.5 (spreadsheet design picks the same case) and Ch.6 (indirect dryers are mostly continuous DPM or batch LPM).
- Hygiene implication: a through-air nonwoven oven = continuous, cross- or cocurrent, plug/mixed → pick the matching DPM/LPM; a SAP fluid bed = batch, solid LPM + gas DPM (§3.8.2). Getting the case right is prerequisite to a correct size.
### Core concept B — Closing the model with a kinetic equation: CDC vs. thin-layer (§3.4.2)

- Definition: the drying rate N (or dimensionless F) must be supplied as a constitutive equation. Two routes: (i) the characteristic drying curve F = f(F) (Eq. 3.29), split into two falling-rate segments by Langrish et al. (Eq. 3.30); (ii) a thin-layer equation such as Lewis dX/dt = −k(X−X*) (Eq. 3.32) or Page F = exp(−(kt)^n) (Eq. 3.36). The volumetric rate is then derived (Eqs 3.37–3.40) to enter the balances.
- Operational? Yes — both routes are curve-fits to the Ch.2 experimental rate curve. The Lewis/Page forms are easiest to implement in a spreadsheet; the CDC is more accurate across the full moisture range.
- Link to Ch.1/Ch.2: F and (X−X)/(X_0−X) are exactly Ch.1's normalised variables; the coefficients come from Ch.2's lumped experiment.
- Hygiene implication: for a new fluff or SAP grade, fit a Page equation to the Ch.2 rate test and drop it into the §3.8 batch or §3.6 continuous model to predict drying time and size.
## 10. Academic critique & open questions

- Theoretical: The psychrometric shortcuts are air–water only. Eq. 3.50 (WBT≈AST) and Eq. 3.52 are explicitly flagged as inaccurate for other systems (p.59). Any hygiene line drying a solvent-coated web (alcohol-based lotion, adhesive) needs the general WBT equation and cannot use the air–water simplification — a point the chapter raises but does not solve for the reader.
- Methodological: All models assume a continuum; real SAP fluid beds and pneumatic conveyors are two-phase (bubbling/heterogeneous) and need the corrections the authors footnote but do not derive. The shrinkage DPM (§3.7.1.2) is shown only as a mesh picture (Fig. 3.15), not as closed equations — the deformation-coupled math is deferred to references.
- Scope / validation: No uncertainty or validation guidance is given despite Ch.2's caution that measured coefficients carry error; "exemplary results" (Figs 3.16–3.25) illustrate but do not quantify model fidelity. Examples are agricultural/mineral, never hygiene polymers.
- Open questions:

- Q1 — Can the §3.4.3 psychrometric block be extended to organic-solvent drying of coated wipes/films without re-deriving the wet-bulb/adiabatic-saturation relations from first principles (the chapter only warns of the gap)?
- Q2 — The shrinkage-coupled solid DPM is open (Fig. 3.15 only). For a swelling SAP gel the boundary moves outward while drying — does the restrained/unrestrained shrinkage framework (p.69) extend to a swelling front, or is a new constitutive law needed?
- Q3 — The conclusion's materials-database gap (p.77–78) is acute for hygiene polymers: where does an engineer obtain GAB/CDC/Page parameters for a specific fluff grade, SAP, or PP/PE nonwoven without running the full Ch.2 battery? Is a shared hygiene-materials property database feasible/desirable?
## 11. Hygiene-Materials Relevance & Action Cards

Chapter 3 is the sizing-and-simulation chapter: it is where the hygiene engineer computes dryer size, residence time, and energy from Ch.1 definitions and Ch.2 coefficients. Every hygiene drying operation — fluff-pulp oven, SAP fluid bed, nonwoven through-air oven, wipes tunnel dryer — is one of the 16 generic cases and can be built from the balances here.

### 11.1 Mapping chapter constructs onto hygiene workflows

|||||
|---|---|---|---|
|Size a new fluff/SAP/nonwoven line|16-case classification → model template|p.53–54|Picks LPM vs. DPM and cocurrent/countercurrent before any equation|
|Predict drying time of a batch|LPM balances + kinetic closure (Eqs 3.113–3.120)|p.70|Batch oven/fluid-bed time from measured coefficients|
|Simulate continuous through-air web|Steady-state DPM cocurrent/cross-flow (§3.6.2)|p.63–65|Web on cylinder/through-air oven = continuous DPM|
|Fit a rate law to Ch.2 data|Lewis (3.32) / Page (3.36) / CDC (3.29–3.30)|p.56–57|Empirical kinetics for spreadsheet scale-up|
|Compute humid-gas state|Psychrometric core (Eqs 3.45–3.53)|p.58–59|Shared routine for every balance; code once in Excel|
|Set equilibrium moisture in model|GAB isotherm (Eq. 3.56)|p.60|X*(a_w) for fluff/SAP from measured isotherm|
|Model web contraction during drying|Shrinkage DPM (Fig. 3.15, p.69)|p.69|Nonwoven/film webs shrink; restrained vs. unrestrained matters|
|Quick first-pass size|Shortcut free/bound-moisture split (§3.10.1)|p.76|Order-of-magnitude size before full model|

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

## 12. Book-Map Quotes (how Ch.3 seeds the rest of the deliverable)

- Seed → Ch.1 & Ch.2 (inputs): the dimensionless F = (X−X)/(X_0−X) and the characteristic curve are Ch.1's normalised variables; the coefficients (h, K, k_m, X*, X_cr, isotherm) are Ch.2's measurements. Ch.3 is where they are consumed.
- Seed → Ch.5 (spreadsheet design): the chapter's computer-oriented stance ("Excel, Mathcad, MATLAB", p.52) and its dryPAK/Matlab/Mathcad deliverables (p.77) are the direct ancestor of Ch.5's spreadsheet-aided design; Ch.5 automates these very balances.
- Seed → Ch.4 (transport properties): the DPM balance terms (Eqs 3.9–3.11) contain the diffusivity D and permeability k that Ch.4 derives from transport theory; Ch.3 uses them, Ch.4 explains them.
- Seed → Ch.6 (indirect dryers): the steady-state and batch model templates (§3.6, §3.8) are reused for conduction/contact dryers, with the heat flux term q supplied by the indirect heating surface rather than hot gas.
- Bridge → Handbook of Nonwovens (sibling): the shrinkage DPM (Fig. 3.15, p.69) and the "drying-induced strain and stress" literature (Hasatani & Itaya 1996, cited p.77) are exactly the nonwoven-web contraction problem the nonwovens handbook engineers — Ch.3 supplies the drying-side model.
- Bridge → Handbook of Plastic Films (sibling): solvent-coated or printed film webs dried in a tunnel/oven are a continuous DPM (§3.6.2) with possible solvent vapor — the chapter's warning that psychrometric shortcuts are air–water only (p.59) is the critical caveat for film dryers.


---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_351caf170a46de1d066d8d8eac8b2e43001a693ee6c0644e"
source_file: "ID · analysis_ch04.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch04.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch04.md.md

# Analysis of Chapter 4 — Transport Properties in the Drying of Solids

Handbook of Industrial Drying, 4th ed. (Mujumdar, CRC Press)
Authors of chapter: Dimitris Marinos-Kouris and Z.B. Maroulis
Target reader: hygiene-materials R&D (disposable diapers, wipes, absorbent cores, fluff-pulp procurement)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

## 1. Overview (范围、对象与定位)

Chapter 4 sits at the property layer of the drying knowledge stack. Whereas Ch.1 (classification/selection), Ch.2 (experimental techniques for moisture/isotherms), and Ch.3 (process calculations/simulation) frame the problem, Ch.4 supplies the five transport/thermodynamic properties that every drying model must contain as parameters:

- Effective moisture diffusivity, D (internal mass transfer)
- Effective thermal conductivity, k (internal heat transfer)
- Air-boundary heat-transfer coefficient, *h*ₕ (external heat transfer)
- Air-boundary mass-transfer coefficient, *h*ₘ (external mass transfer)
- Drying constant, K (a lumped, thin-layer proxy)
- Equilibrium material moisture content, *X*ₑ (drives the mass-transfer potential)
The chapter is organized strictly per-property: Definition → Experimental method → Data compilation → Factors affecting → Theoretical estimation. This is the single most data-dense chapter in the assignment — it carries 18 tables and ~24 figures, with large literature compilations (Tables 4.2, 4.6, 4.13, 4.15–4.18). For the hygiene reader the chapter is decisive because four of the six properties are measured almost entirely on polymer systems (Crank & Park Diffusion in Polymers, Frisch & Stern Diffusion of small molecules in polymers) and the data tables explicitly list cellulose acetate, polyvinyl alcohol, polyolefins, Avicel (microcrystalline cellulose), and starch gels — i.e. the exact chemistries of fluff pulp, nonwoven webs, SAP carriers, and tissue.

Print-page span: p.79–p.113 (PDF p.100–134).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — Drying is model-ready but property-starved. The authors open with the central tension of industrial dryer design:
> "Nowadays, more and more sophisticated drying models are becoming available, but a major question that still remains is the measurement or determination of the parameters used in the models." (p.79)
> "a lack of data is expected to continue and, as noted by Keey, 'it is probably unrealistic to expect complete hygrothermal data for materials of commercial interest'." (p.79–80)
Implication for hygiene R&D: SAP/fluff blends are "materials of commercial interest" with essentially no published hygrothermal data — the reader must generate D, k, and h in-house.

V2.2 — Moisture diffusivity is defined via Fick's 2nd law with an effective coefficient. (p.81)
> "Diffusion in solids during drying is a complex process that may involve molecular diffusion, capillary flow, Knudsen flow, hydrodynamic flow, or surface diffusion. If we combine all these phenomena into one, the effective diffusivity can be defined from Fick's second law"
> "@X/@t = D ∇²X  (4.1) where D (m²/s) is the effective diffusivity, X (kg/kg db) is the material moisture content, and t (s) is the time." (p.81)
Implication: "effective" = heterogeneous structure collapsed into one number; the same D that governs fluff-pulp web drying.

V2.3 — Which property must be accurate depends on the controlling resistance. (p.81–82)
> "If, for example, drying is controlled by the internal moisture diffusion, then the effective moisture diffusivity must be known with high accuracy. This situation is valid when large particles are drying with air of high velocity. Drying of small particles with low velocity of air is controlled by the external mass transfer... But there are situations in which heat transfer is the controlling resistance. This happens, for example, in drying of solids with high porosity, in which high mass and low heat transfer rates are obtained." (p.81–82)
Implication: Through-circulation drying of loose fluff/SAP granulate → internal heat may control; thin nonwoven web on a cylinder dryer → external mass transfer may control. The property you must measure precisely flips with geometry.

V2.4 — Diffusivity methods were built for polymers, borrowed by foods. (p.82)
> "The diffusivity in solids can be determined using the methods presented in Table 4.1. These methods have been developed primarily for polymeric materials [7–9]." (p.82)
References [8] Crank & Park, Diffusion in Polymers (1968); [9] Frisch & Stern, Diffusion of small molecules in polymers (1983).

V2.5 — "Effective diffusion coefficients are available for inorganic materials[20], polymers[8], and foods[21,22]." (p.84)
Table 4.2 then lists Cellulose acetate (2.0E-12–3.2E-12 m²/s at 25°C), Avicel/FMC (5.0E-9–5.0E-8), starch gel/granular — the fluff/tissue/SAP feedstocks.

V2.6 — Diffusivity is strongly moisture- and temperature-dependent, except in some polymers. (p.85)
> "The temperature dependence of the diffusivity can generally be described by the Arrhenius equation, D = D₀ exp(−E/RT) (4.2)" (p.85)
> "in certain categories of polymers, deviation from this kind of behavior has been observed. For instance, for several of the less hydrophilic polymers (e.g., polymethacrylates and polyacrylates) the moisture diffusivity decreases with increasing water content. On the other hand, the moisture diffusivity appears to be independent of the concentration—and hence constant—for some hydrophobic polyolefins." (p.85–86)
Implication: This is the Fickian-vs-anomalous-sorption fingerprint (see POP block): polyacrylate = SAP chemistry; a falling D with rising water is the swelling/hydrogel signature.

V2.7 — Thermal conductivity defined by Fourier's law; used when Biₕ, Biₘ > 1 (internally controlled). (p.88–89)
> "@T/@t = (k/(ρ cₚ)) ∇²T  (4.4)... Equation 4.4 is used in cases in which heat transfer during drying takes place through conduction (internally controlled drying)... the drying process is internally controlled whenever the respective Biot number (Biₕ, Biₘ) is greater than 1[5]." (p.88–89)

V2.8 — Boundary coefficients obey Newton's law and the heat/mass analogy. (p.94)
> "Q = hₕ A (Tₐ − Tₐ) (4.5)... By analogy, a surface mass transfer coefficient can be defined... J = hₘ A (Xₐₛ − Xₐ) (4.6)... Equation 4.5 and Equation 4.6 are used in cases in which the drying is externally controlled. This occurs when the Biot number (Biₕ, Biₘ) for heat and mass transfer is less than 0.1[5]." (p.94)
> "In air conditioning processes, the heat and mass transfer analogy is usually expressed using the Lewis relationship hₘ/h = 1/cₚ (4.13)" (p.97)

V2.9 — The drying constant K is a lumped, phenomenological stand-in. (p.98)
> "Lewis suggested that during the drying of porous hygroscopic materials, in the falling rate period, the rate of change in material moisture content is proportional to the instantaneous difference between material moisture content and the expected material moisture content when it comes into equilibrium with the drying air... dX/dt = −K(X − Xₑ) (4.14)" (p.98)
> "The drying constant K is the most suitable quantity for purposes of design, optimization, and any situation in which a large number of iterative model calculations are needed... the drying constant embodies all the transport properties into a simple exponential function." (p.98–99)

V2.10 — K collapses to D/L² for diffusion-controlled slabs. (p.99)
> "K = π²D/L²  (4.15) where D (m²/s) is the effective diffusivity and L (m) is the thickness of the slab." (p.99)

V2.11 — Equilibrium moisture is a thermodynamic prerequisite; desorption isotherm governs drying. (p.100)
> "The moisture content of the material when it comes into equilibrium with drying air is a useful property... The relation between equilibrium material moisture content and the corresponding water activity for a given temperature is known as the sorption isotherm." (p.100)
> "It is clear from Figure 4.11 that the desorption isotherm is the curve to use for the process of drying." (p.100)

V2.12 — Sorption isotherm types map onto polymer hydrophilicity; GAB is the design standard. (p.100–102)
> "The sorption isotherms of the hydrophilic polymers, such as natural fibers and foods, are of type II. The isotherms of the less hydrophilic rubbers, plastics, synthetic fibers, and foods rich in insoluble components are of type III." (p.100)
> "The Guggenheim–Anderson–de Boer (GAB) equation is considered as the most versatile model, capable of application to situations over a wide range of water activities (0.1 < a_w < 0.9) and to various materials... The GAB equation is probably the most suitable for process analysis and design of drying because of its reliability, its simple mathematical form, and its wide use." (p.102)

V2.13 — All transport properties can be estimated simultaneously from one drying experiment. (p.103–104, 106)
> "The method uses a drying experimental apparatus and estimates the heat and mass transport properties as parameters of a drying model that incorporates these properties[28,43,176–180]." (p.103)
> "Theoretically, all the properties describing the drying kinetics could be estimated simultaneously." (p.104)
The process model (Eqs 4.16–4.23) couples moisture diffusion (4.16), boundary vapor transfer (4.18), heat conduction (4.20), and boundary heat transfer (4.22) into one regression.

V2.14 — Food-diffusivity data compiled into a universal Arrhenius × moisture model. (p.107–109)
> "A total of 175 papers were retrieved from the literature from which 1773 data were obtained. These data refer to more than 100 food materials... D = D₀ exp(−E₀/RTᵣ)1 + (X/X₀) exp(−Eᵢ/R(1/T − 1/Tᵣ))" (p.108)
Parameter tables (4.15, 4.16) give D₀, Dᵢ, E₀, Eᵢ for cereals, fruits, vegetables, model foods (Amioca, Hylon-7 starch), etc.

## 3. Research Method (研究方法)

The chapter is a structured property review, not an experiment. Method per property:

- Definition — state the governing PDE/rate law (Fick 4.1, Fourier 4.4, Newton 4.5/4.6, Lewis thin-layer 4.14, sorption isotherm).
- Experimental measurement — enumerate techniques in a table (Table 4.1 diffusivity; Table 4.5 thermal conductivity; Table 4.8 h/hₘ; gravimetric/hygrometric for isotherms).
- Data compilation — large literature tables with ranges and references (Tables 4.2, 4.4, 4.6, 4.13, 4.15–4.18).
- Factors affecting — temperature/moisture/structure; Arrhenius (4.2), polynomial, structural models (Table 4.7), empirical equations (Tables 4.3, 4.9, 4.11).
- Theoretical estimation — Chapman–Enskog, Stokes–Einstein, pore models (Eq 4.3: D = (ε/τ²) d Dₐ), effective-medium/Maxwell models, and the simultaneous-regression method of §4.7.
The §4.7 method is the methodological centerpiece: a single lab dryer (Fig 4.15) with controlled T, Xₐ, uₐ and monitored X(t), T(t); a mechanistic process model (Fig 4.16); and regression (Fig 4.17) that returns D, k, hₕ, hₘ as fitted parameters. Relative residuals (Eq 4.24/4.25) and Sₓ, S_T (Eq 4.26/4.27) validate the fit. This is exactly the protocol a hygiene lab should adopt to characterize fluff/SAP webs.

## 4. Argumentation (论证逻辑)

The chapter's argument is reductive but honest:

- Premise A: Every drying model needs a small set of transport/thermo properties (§4.1).
- Premise B: Each property has a clean definition (a PDE or rate law) — so in principle it is measurable.
- Premise C: In practice the data are scattered, method-dependent, and absent for commercial materials (Keey quote, p.80).
- Step: Therefore, for each property, lay out (i) definition, (ii) how to measure it, (iii) what little data exist, (iv) empirical/theoretical correction factors, and (v) — for the data-rich food case — a fitted universal model.
- Resolution: When direct measurement is impractical, estimate all properties at once from one drying curve via the §4.7 regression framework.
The logic is internally consistent and conservative: the authors repeatedly flag that empirical correlations "have limited practical utility" (thermal conductivity, p.93) and that equations "should be avoided" with indirect regression (GAB, p.102). The through-line for the hygiene reader: you cannot buy these numbers; you must measure or regress them per your own web.

## 5. Role of This Chapter in the Book (在全书中的角色)

Ch.4 is the parameter dictionary of the handbook. Ch.1 tells you which dryer; Ch.2 gives you how to measure moisture/isotherms; Ch.3 gives you mass/energy balances and simulators; Ch.4 gives you the coefficients those balances and simulators consume. Ch.5 (spreadsheet design) and Ch.6 (indirect dryers) then use Ch.4's h, hₘ, k, D, Xₑ. For hygiene R&D, Ch.4 is the bridge from "we dried a sample" to "we can simulate/scale a nonwoven through-dryer or an SAP contact dryer."

## 6. Strengths and Weaknesses (贡献与局限)

Strengths
- The only chapter that consolidates all dryer-relevant properties in one place with consistent notation.
- Polymer-first measurement heritage (Crank & Park, Frisch & Stern) makes the data tables directly usable for fluff/SAP/nonwoven chemistries.
- §4.7 simultaneous-estimation method is a genuine engineering deliverable, not just a literature dump.
- Explicit Biot-number rule (Eq 4.5/4.6 vs 4.4 contexts: Bi1 internal) directly tells the reader which property matters.

Weaknesses
- Data are overwhelmingly foods/ceramics; "Other materials" polymer rows are sparse (cellulose acetate only, polyolefins mentioned but not tabulated with values).
- The polymer diffusion anomaly (D falling with water for polyacrylates, p.85) is noted but never explained mechanistically — no mention of swelling, free volume, or glass transition (the missing polymer-science layer is supplied in the POP block).
- Thermal-conductivity theoretical estimation admitted as "little, if any, meaning" for solids (p.93–95); no usable predictive tool.
- Tables 4.15–4.18 are foods-only; no analogous universal model for polymer mats.

## 7. Key Terms (关键术语)

||||
|---|---|---|
|Effective moisture diffusivity|D|"effective diffusivity can be defined from Fick's second law" (p.81); m²/s|
|Effective thermal conductivity|k|from Fourier's law (4.4); kW/(m K)|
|Air-boundary heat-transfer coeff.|*h*ₕ|Newton's law (4.5); kW/(m² K)|
|Air-boundary mass-transfer coeff.|*h*ₘ|analogy to Newton (4.6); kg/(m² s)|
|Drying constant|K|thin-layer lumped coefficient (4.14); 1/s|
|Equilibrium moisture content|*X*ₑ|"moisture content... in equilibrium with drying air" (p.100); kg/kg db|
|Water activity|a_w|"equal to the relative humidity of air" (p.100)|
|Biot number (heat/mass)|Biₕ, Biₘ|dimensionless; 1 internal control (p.89,94)|
|Sorption isotherm|—|*X*ₑ vs a_w at fixed T (p.100)|
|Hysteresis|—|adsorption vs desorption loop (p.100)|
|Arrhenius factor|*D*₀|pre-exponential in Eq 4.2|
|Activation energy (diffusion)|E|in Eq 4.2; kJ/kmol|
|GAB model|—|most versatile isotherm, 0.1<a_w (p.102)|
|Tortuosity / porosity / constrictivity|τ, ε, δ|pore-model parameters in Eq 4.3|
|Lewis relationship|—|*h*ₘ/h = 1/*c*ₚ (4.13)|

## 8. Micro close-reading (微观精读)

8.1 — The polymer diffusion anomaly sentence (p.85–86). The authors write: "for several of the less hydrophilic polymers (e.g., polymethacrylates and polyacrylates) the moisture diffusivity decreases with increasing water content." This single clause is the most important sentence in the chapter for the hygiene reader. Polyacrylate = the backbone chemistry of SAP (crosslinked sodium polyacrylate). A decreasing D with rising water content is the opposite of the food/cellulose behavior (D rises with water) and is the textbook signature of anomalous / Case-II / swelling-controlled diffusion in glassy polymers. The chapter reports the phenomenon but offers no mechanism — the POP block supplies it.

8.2 — Eq 4.3 pore model (p.87). D = (ε/τ²) δ Dₐ collapses vapor diffusion in a porous solid to porosity ε, tortuosity τ, constrictivity δ, and free-vapor diffusivity Dₐ. For a fluff-pulp mat or a SAP/glued core, ε and τ are the design levers; this equation says D scales with ε/τ² — i.e. open, straight pores dry fast.

8.3 — The Biot-number switch (p.89 vs p.94). Internal control when Biₕ,Biₘ > 1 (Fourier/Fick govern, Eq 4.4/4.1); external control when < 0.1 (Newton governs, Eq 4.5/4.6). This single threshold dictates whether you tune D/k (material) or h/hₘ (air) — the difference between reformulating the web and re-specifying the dryer.

8.4 — GAB vs desorption (p.100, 102). "the desorption isotherm is the curve to use for the process of drying" — because desorption has more active sites (hysteresis, p.100). For an SAP particle losing water in a dryer, you must use the desorption branch, not the adsorption (rewetting) branch.

8.5 — §4.7 regression residual definitions (p.109). e_Xᵢ = (Xᵢ − Xᵢ,꜀)/Xᵢ, e_Tᵢ = (Tᵢ − Tᵢ,꜀)/Tᵢ (Eq 4.24, 4.25); Sₓ, S_T (4.26, 4.27). Validation is by relative deviation, not absolute — appropriate because X spans orders of magnitude during a drying run.

## 9. Concept deep-dive (概念深掘)

9.1 Effective moisture diffusivity as a "lumped" internal property. Fick's 2nd law (4.1) assumes a homogeneous solid. Real fluff/SAP webs are three-phase (dry fiber + water + air/vapor). The authors resolve this by folding all sub-mechanisms (molecular, capillary, Knudsen, hydrodynamic, surface diffusion) into one effective D (p.81). For design this is pragmatic; for diagnosis it hides which sub-mechanism limits you. A web that dries slowly because of capillary blockage vs molecular resistance both show "low D" — you need the §4.7 discrimination procedure (p.106) to tell them apart.

9.2 Arrhenius for D and its polymer twist. Eq 4.2 (D = D₀ exp(−E/RT)) works for most materials, but the activation energy E and pre-factor D₀ can themselves be moisture-dependent (Table 4.3, T3.1–T3.4). For "less hydrophilic polymers" D even falls with water (p.85). Food model (4.28) makes E split into E₀ (dry) and Eᵢ (wet) and D into D₀, Dᵢ — a template the hygiene reader can fit to fluff/SAP data.

9.3 Thermal conductivity of heterogeneous mats. Structural models (Table 4.7: perpendicular/parallel/mixed/Maxwell/effective-medium) bracket k between series and parallel limits based on void fraction ε. For a porous fiber mat, parallel model ≈ upper bound, perpendicular ≈ lower. The chapter's starch example (parallel best, p.92) is directly analogous to a fluff-pulp pad: treat dry-starch/water as the two phases, then the granule-air as a second level.

9.4 Boundary coefficients and dimensionless groups. Tables 4.9–4.10 give j-factors, Nu, Sh, Bi, Re, Pr, Sc, Gu, St correlations for packed/fluidized/spray/pneumatic/impingement dryers. The Lewis relation (4.13, *h*ₘ/h = 1/*c*ₚ) lets you get *h*ₘ from h — critical when only heat-transfer correlations exist for your dryer type. Figures 4.8/4.9 plot h and hₘ vs air velocity for typical dryers (particle size 10 mm, 80°C, *X*ₐ=10 g/kg) — a first-cut estimator before you build the §4.7 rig.

9.5 The drying constant as a design shortcut. Eq 4.14 (Lewis thin-layer) and Eq 4.15 (K = π²D/L²) mean: if you know D and slab half-thickness L, you have K without a fitting run; conversely, a thin-layer drying run gives you K (hence D if L is known). This is the fastest path to a first dryer sizing for a new nonwoven basis weight.

9.6 Equilibrium moisture & isotherm types for polymers. Type II = hydrophilic (natural fibers, foods); Type III = less hydrophilic (rubbers, plastics, synthetic fibers) (p.100). Cellulosic fluff → Type II (strong water binding, high *X*ₑ at moderate a_w); PP/PE nonwoven → Type III (weak binding, low *X*ₑ). GAB (Table 4.13/4.14) is the recommended design equation across 0.1<a_w

9.7 Simultaneous estimation (§4.7) — the reusable protocol. Process model couples four PDEs (4.16 moisture diffusion, 4.18 boundary vapor, 4.20 heat conduction, 4.22 boundary heat) with empirical property models (4.17, 4.19, 4.21, 4.23: D, hₘ, k, hₕ as functions of X,T,uₐ,a_w). One regression returns all four properties plus their empirical constants (a꜀,b꜀,c꜀,d꜀). This is the chapter's highest-value, most transferable method for a hygiene lab.

## 10. Critique (批判性评估)

- Mechanism gap on polymer anomaly. The chapter documents D-falling-with-water for polyacrylates (p.85) but never explains why — no swelling, free-volume, or Tg discussion. This is precisely where Principles of Polymerization (Odian) knowledge is required (POP block). A reader designing an SAP dryer who stops at Ch.4 will mis-model the falling-rate period.
- Polymer data poverty. Table 4.2's "Other materials" has only one true polymer row with values (cellulose acetate) plus Avicel and starch. Polyolefins are named (p.85–86) but never quantitatively tabulated. The hygiene reader cannot lift D for PP/PE nonwoven or SAP from this chapter — must measure.
- No universal polymer model. §4.8 builds a beautiful food model (4.28) with 100+ materials; no equivalent exists for polymer mats. The chapter implicitly concedes this ("it is expected that such a relation will be proposed soon," p.86).
- Theoretical estimation is weak for k and for solids generally. "It is impossible to estimate an empirical constant using theoretical arguments" (p.99–100) for K; thermal-conductivity theory "has little, if any, meaning" (p.93). The chapter is honest but leaves the reader with measurement as the only reliable route.
- OCR/notation noise. Source OCR merges words ("moisturecontent", "Knudsenflow") and drops some sub/superscripts; equations 4.1–4.30 were transcribed as faithfully as possible but should be re-checked against the print edition before use in a simulator.
## 11. Hygiene-Material Relevance & Action Cards (卫材相关性与行动卡)

H11.1 — Characterize fluff-pulp D before scaling a through-dryer. Fluff is "Other materials / cellulose" class; expect D ~10⁻¹²–10⁻⁹ m²/s (cf. cellulose acetate 2E-12, Avicel 5E-9). Action: run §4.7 regression rig on your specific pulp grade at 3–5 m/s, 60–120°C; do not borrow literature D.

H11.2 — Expect SAP to show anomalous (non-Fickian) drying. Polyacrylate chemistry ⇒ D may decrease as the gel hydrates (p.85). Action: model the falling-rate period with a swelling-controlled (Case-II) kernel, not pure Fick 4.1; use desorption isotherm branch.

H11.3 — Nonwoven PP/PE webs ≈ Type III isotherms, low *X*ₑ. Action: anticipate very low equilibrium moisture; on a cylinder/can dryer the web dries in  s (tissue analogy, Ch.3) and external *h*ₘ controls (Bi). Size the dryer from *h*ₘ via Lewis (4.13) + Table 4.9, not from D.

H11.4 — Use Biot threshold to choose your design lever. Action: compute Biₕ,Biₘ for your web; if >1 tune material (basis weight, porosity ε/τ² via Eq 4.3); if  tune air (velocity, temperature via Table 4.9/Fig 4.8–4.9).

H11.5 — Build the GAB isotherm for your core composite. Action: measure desorption isotherm (gravimetric, p.101–102) for fluff+SAP blend; fit GAB (Table 4.13) to get *X*ₑ(a_w,T); feed *X*ₑ into the dryer mass-balance (Ch.3) and the §4.7 model.

H11.6 — First-cut dryer sizing with thin-layer K. Action: run one constant-T constant-RH thin-layer drying of your web; fit Eq 4.14 → K; convert to D via Eq 4.15 if slab thickness known; iterate in Ch.5 spreadsheet.

H11.7 — Glass-transition discipline for polymer solids. SAP/nonwoven binders have a Tg; keep dryer temp below Tg-driven casehardening window (see POP). Action: set exhaust/dwell so the polymer does not approach its rubbery state mid-drying.

## 12. Book-Map Quotes (本书脉络引证)

- Ch.1 (p.3): classification/selection of dryers — Ch.4 supplies the properties those dryers consume.
- Ch.2 (p.31): experimental moisture/isotherm measurement — Ch.4 §4.2.2 and §4.6.2 reuse those same techniques (sorption balance, gravimetric/hygrometric).
- Ch.3 (p.51): mass/energy balances and simulators — require *D, k, h, hₘ, X*ₑ from Ch.4 as inputs.
- Ch.5 (p.119): spreadsheet-aided design — uses Ch.4's h/hₘ correlations (Tables 4.9–4.10) and *X*ₑ.
- Ch.6 (p.135): indirect (contact) dryers — rely on Ch.4 k and Biot rules for conductive heating of polymer solids.


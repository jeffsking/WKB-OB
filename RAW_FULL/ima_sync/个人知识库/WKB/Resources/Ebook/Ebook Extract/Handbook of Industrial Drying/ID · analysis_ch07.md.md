---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_a9438eb3af685699fc9f0453210358a9001a693ee6c0644e"
source_file: "ID · analysis_ch07.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch07.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch07.md.md

# Chapter 7 — Rotary Drying

## 1. Chapter Overview

Chapter 7 (Krokida, Marinos-Kouris & Mujumdar) is the mechanical-conveyance and design chapter of the Handbook's dryer catalogue. It treats the rotary dryer as a cylindrical, slightly inclined, slowly rotating shell that advances wet granular solids by rotation, slope and head effect while hot gas passes (cocurrent or countercurrent) to evaporate surface and bound moisture. The chapter's argument runs through five layers: (i) classification by heat-transfer mode (direct, indirect–direct, indirect, special types such as the Roto-Louvre); (ii) flight design as the device that lifts and showers the solids through the gas curtain; (iii) residence-time models built from the three particle motions — cascade, kiln action, bouncing; (iv) heat- and mass-transfer correlations, dominated by the volumetric coefficient Uₐ and the Chilton–Colburn analogy; and (v) a full mathematical design model with burner, dryer, kinetics, residence time and geometrical constraints, closed by two worked case studies (olive cake, catalyst pellets). For the hygiene reader the chapter is a capability reference: it defines the dryer class that post-dries free-flowing granular polymer products — SAP granules, cellulose-acetate flake, PP/polyolefin pellets, vinyl resins — and it supplies the residence-time and thermal-efficiency equations needed to size and cost such a unit. Direct, gentle, through-gas rotary drying is precisely the regime for heat-sensitive, free-flowing absorbent-material feeds.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

## 2. Key Viewpoints

### Viewpoint 1 — Cocurrent flow protects heat-sensitive solids.

- Page: p.149
- Quote: > "Cocurrent flow is used for heat-sensitive materials even for high inlet gas temperature due to the rapid cooling of the gas during initial evaporation of surface moisture, whereas for other materials countercurrent flow is desirable in order to …"
- Interpretation: The chapter's first design rule is gas/solid flow direction keyed to thermal sensitivity. A 800–1100 K inlet (p.161) is safe for heat-sensitive feeds only in cocurrent mode because the gas cools instantly on first evaporation. This is the governing choice for SAP granules or cellulose-acetate flake, which degrade at high skin temperature.
### Viewpoint 2 — The classification rests on where the heating medium contacts the solids.

- Page: p.150
- Quote: > "Rotary dryers are classified as direct, indirect–direct, indirect, and special types. This classification is based upon the method of heat transfer being direct when heat is added to or removed from the solids by direct exchange between gas and solids, and being indirect when the heating medium is separated from contact with the solids by a metal wall or tube."
- Interpretation: Four families; the direct-heat bare cylinder is "the simplest and most economical" (p.150). For SAP/fluff by-products that are dusty, direct heat risks entrainment loss of fines (p.150) — a real concern for superabsorbent powder.
### Viewpoint 3 — Polymer and granular chemicals are canonical rotary-dryer feeds.

- Page: p.151
- Quote: > "Representative materials dried in direct-heat rotary dryers are sand, stone, ilmenite ore, sodium sulfate, sodium chloride, and fluorspar, for which high temperatures are used, cellulose acetate, sodium chloride, styrene, copperas, cast-iron borings, and ammonium sulfate, for which medium temperatures are required, and urea prills, vinyl resins, oxalic acid …"
- Interpretation: The explicit listing of cellulose acetate, styrene, and vinyl resins proves the rotary dryer is a standard post-treatment unit for polymeric, free-flowing solids. SAP granules (crosslinked sodium polyacrylate) fall in the same free-flowing-granular class and are routinely post-dried in rotary or rotary-valve units.
### Viewpoint 4 — Flights exist to lift and shower the solids; under/over-loading ruins performance.

- Page: p.152
- Quote: > "Their purpose is to lift and shower the solid particles through the gas stream promoting intimate contact between wet solids and hot gases."
- Interpretation: Flight geometry (straight, angled, right-angled, semicircular, EAD, CBD) sets the cascading curtain. For sticky wet feeds (e.g. a moist SAP/cellulose blend) radial flights with a 90° lip are used; flat radial flights without lip for sticky ones (p.152).
### Viewpoint 5 — Optimal drum loading is 10–15% of volume.

- Page: p.153
- Quote: > "The total amount of solids contained in the drum is about 10–15% of its volume. It has been proved empirically that this loading gives the most efficient performance, therefore a sufficient number of flights must be provided to contain and distribute these solids."
- Interpretation: A design constraint the hygiene engineer can apply directly: a rotary post-dryer for SAP granules should hold 10–15% fill; below this the dryer is under-utilised, above it material bypasses by kiln action and contact with hot gas is lost (p.153).
### Viewpoint 6 — Residence time is holdup ÷ feed rate, and plug flow cannot be assumed.

- Page: p.154 & p.155
- Quote: > "The average residence time (or, time of passage) tₜ is defined as holdup H divided by the solids feedrate F" (p.154); and "it is not safe to assume plug flow of the particles in industrial dryers, because only narrowly sized materials were studied" (p.155).
- Interpretation: Residence time controls the final moisture spec. Because real feeds are wide-size-distributed, the maximum particle moisture (not the bulk mean) governs acceptability (p.155) — directly relevant to a mixed SAP-granule / fines distribution.
### Viewpoint 7 — Heat transfer is expressed by a volumetric coefficient Uₐ with strong scatter.

- Page: p.157–159
- Quote: > "Q = Uₐ V (Δt)ₘ (7.30) where Q is the rate of heat transfer … Uₐ is the volumetric heat transfer coefficient … V is the dryer volume." (p.157)
- Interpretation: Uₐ = U·(a/V) collapses the effective gas–solid contact area into one number. Miller et al. give Uₐ ∝ (n−1)·D⁻¹·G⁰·⁴⁶ (6 flights) / G⁰·⁶⁰ (12 flights) (Eq 7.33–7.34, p.158); for modern commercial dryers with 2.4–3.0 D flight count and 60–75 ft/min peripheral speed, Saeman–Mitchell and McCormick correlations apply (Eq 7.37, 7.40, p.159).
### Viewpoint 8 — The Chilton–Colburn analogy ties heat and mass transfer in one factor.

- Page: p.160
- Quote: > "The Chilton–Colburn analogy can be expressed as j_H = j_D = f/2 … where f is the friction factor, j_D is the mass transfer factor, and j_H is the heat transfer factor … j_H = St Pr²ᐟ³" (Eq 7.42–7.43).
- Interpretation: Once the heat-transfer factor j_H is known from Reynolds number (Fig 7.6–7.7), the mass-transfer factor j_D follows, enabling calculation of the diffusion coefficient. This unifies the two transport processes that occur "simultaneously" in rotary drying (p.160).
### Viewpoint 9 — A complete design model minimises unit cost over five free variables.

- Page: p.165
- Quote: > "A degree of freedom analysis suggests that five design variables are available … T_AC, u, H/V, L/D, and n_f/D, where the first and second express the operating conditions and the rest the dryer shape."
- Interpretation: The chapter closes the loop from §7.3–7.6 into a cost-minimising model (Eq 7.48–7.71). Geometrical constraints: 5% < H/V < 15%, 2 < L/D < 20, 5 < n_f/D < 10 (p.165). For an SAP post-dryer these bounds define the feasible design envelope.
## 3. Research Method & Data Sources

The chapter is a modelling + design review, not an experiment. Method per section:
| Paradigm | Method | Data source | Tool | Validity |
|---|---|---|---|---|
| Classification | Literature survey of dryer types | Perry & Chilton [35], vendor data | — | Descriptive |
| Flight holdup | Force balance on particle (gravity/centrifugal/friction) → Eq 7.1–7.16 | Schofield & Glikin [49], Kelly [19/20], Glikin [11] | Analytical + numerical integration | Valid 0.0025< n 100% at 3 m/s |
| Heat/mass transfer | Volumetric Uₐ, Chilton–Colburn j-factors | Miller et al. [30], Friedman & Marshall [9], Saeman & Mitchell [47] | Correlations, dimensionless groups | Scale-up "requires caution and experience" |
| Cost/design | Degree-of-freedom optimisation | Krokida et al. [28], McAdams [28], industrial quotes | Spreadsheet model | Two case studies validated vs. real units |

## 4. Argumentation Process

- Premise A: Rotary dryers are the workhorse for free-flowing granular solids; their behaviour is set by mechanical conveying + gas–solid contact.
- Premise B: Both are quantifiable — flight geometry fixes holdup/cascading; residence time = H/F; heat transfer = UₐVΔt.
- Step 1: Classify and show flights create the raining curtain (§7.2–7.3).
- Step 2: Derive residence time from the three particle motions, exposing model scatter (§7.4).
- Step 3: Quantify heat/mass transfer and collapse to Chilton–Colburn (§7.5).
- Step 4: Assemble a full cost-minimising design model with constraints, then validate on two case studies (§7.7–7.9).
- Conclusion (p.168): "the development of a universal model of the rotary dryer, that combines the cascading motion of the particles with the heat and mass transfer, is questionable" — the authors honestly cap claims; cascade + transfer耦合 remains unresolved.
## 5. Role in the Book

Chapter 7 is the first of the unit-operation-specific chapters (rotary, fluid bed, drum, spray, freeze, microwave) that operationalise the property layer of Ch.4 and the selection layer of Ch.1. It is the mechanical counterpart to Ch.8 (fluidized bed, also a convective granular dryer) and Ch.9 (drum, a conductive/contact alternative). For hygiene R&D it defines the convective post-drying option for granular SAP, cellulose-acetate, and pelletised polymer products.

## 6. Strengths & Weaknesses

✅ Strengths:
- Only chapter giving a closed, cost-minimising rotary-dryer design procedure with explicit geometrical constraints (p.165) and two validated case studies.
- Direct handling of heat-sensitive feeds via cocurrent flow (p.149) — the relevant mode for SAP/cellulose-acetate.
- Honest scatter reporting: residence-time correlations diverge >100% at 3 m/s (p.157); heat-transfer scale-up "requires caution" (p.159).

⚠️ Weaknesses / contestable points:
- Residence-time models are built on narrowly sized, mostly inorganic tracers (496-µm sand, p.154); extrapolation to polydisperse SAP granule + fines mixtures is unvalidated.
- "it is not safe to assume plug flow" (p.155) yet the design model (Eq 7.61 tₜ = M/F) treats the holdup as a single mean — an internal inconsistency the authors note but do not resolve.
- Polymer feeds (cellulose acetate, vinyl resins) are listed (p.151) but no polymer-specific drying data (no SAP row, no binder). The chapter is material-agnostic about polymer behaviour (see POP block).

## 7. Key Terms / Concepts

- Direct vs indirect rotary dryer (p.150): heat exchange direct (gas–solid) vs separated by metal wall/tube.
- Flights (p.152): peripheral lifters that shower solids; profiles: straight/angled/right-angled/semicircular/EAD/CBD.
- Holdup H (p.153): solids contained in drum, optimum 10–15% of volume.
- Residence time tₜ (p.154): H/F (Eq 7.17).
- Cascade / kiln action / bouncing (p.154–156): the three particle-transport mechanisms.
- Volumetric heat-transfer coefficient Uₐ (p.157): U·(a/V), W/(m³ K).
- Chilton–Colburn analogy (p.160): j_H = j_D = f/2; links heat & mass transfer.
- Number of heat-transfer units Nₜ (p.161): optimal range 1.5–2.5.
- Drying constant k_M (p.163): empirical k₀·T₀^k₁·Y₀^k₂·u₀^k₃ (Eq 7.49).
- L/D ratio (p.161, p.165): optimal 4–10 industrial; constraint 2–20.
## 8. Micro close-reading (ONE key paragraph)

The cocurrent / heat-sensitivity rule (p.149). Full verbatim:
> "The direction of gas flow through the cylinder relative to the solids is dictated mainly by the properties of the processed material. Cocurrent flow is used for heat-sensitive materials even for high inlet gas temperature due to the rapid cooling of the gas during initial evaporation of surface moisture, whereas for other materials countercurrent flow is desirable in order to …"
Sentence-by-sentence:
1. "gas flow … dictated mainly by the properties of the processed material" — establishes feed-property-led selection (links to Ch.1 classifier).
2. "Cocurrent flow is used for heat-sensitive materials even for high inlet gas temperature" — the counter-intuitive permission: high T inlet is allowed if cocurrent, because …
3. "due to the rapid cooling of the gas during initial evaporation of surface moisture" — mechanism: first surface evaporation quenches the hot gas, so the solid never sees the peak gas temperature.
4. "whereas for other materials countercurrent flow is desirable" — the trade-off: countercurrent gives higher thermal efficiency for robust feeds.
💡 Standout line: a 800–1100 K inlet (p.161) is survivable for heat-sensitive SAP/cellulose-acetate only in cocurrent mode — the single most important selection rule for a hygiene post-dryer.

## 9. Concept deep-dive

9.1 Flight design as the contact-enabler. Flights are "offset every 0.6–2 m" (p.152); their shape matches the solid: "Radial flights with a 90° lip are used for free-flowing materials and flat radial flights without lip for sticky ones" (p.152). Holdup per flight is geometry- and angular-position dependent; maximum loading at u=0° is given by Eq 7.7 (p.153). For an SAP granule post-dryer, free-flowing feed → 90° lip radial flight; a moist caked feed → flat lip. The k₀ factor (Table 7.1, p.154) quantifies mean fall distance per flight profile (CBD 0.902 highest).

9.2 Residence time from three motions. Cascade (lift+shower) advances particles by D·sin u/tan α (p.156); kiln action (slide along lower shell) dominates overloaded drums; bouncing contributes ~50% of advance in pilot, ~22% in industrial underloaded drums (p.157). The design model uses tₜ = M/F (Eq 7.61), with M = (1−ε)ρₚH (Eq 7.62). For SAP granules, the maximum-particle residence (wide PSD) governs the dry spec (p.155).

9.3 Volumetric heat-transfer coefficient Uₐ. Eq 7.30 Q = UₐV(Δt)ₘ. Friedman & Marshall: Uₐ ∝ (n−1)D⁻¹G⁰·⁴⁶ (6 flights) (Eq 7.33, p.158); Miller et al.: 6-flight equation "more representative for the design of industrial dryers" (p.158). Uₐ ∝ holdup⁰·⁵ and G⁰·¹⁶ (p.159) — gas rate helps twice: via a (contact area) and weakly via U. Relates to Ch.4 hₕ/hₘ boundary coefficients.

9.4 Chilton–Colburn unification. j_H = j_D = f/2 (Eq 7.42); valid for Pr 0.6–100, Sc 0.6–2500, laminar and turbulent (p.160). Once j_H(Re) is read from Fig 7.6, the diffusion coefficient follows — the chapter's bridge between heat and mass transfer, echoing the Lewis relation of Ch.4.

9.5 Drying kinetics & cost model. First-order thin-layer kernel (X−X_SE)/(X₀−X_SE) = exp(−k_M t) (Eq 7.56, p.164); k_M = k₀·T₀^k₁·Y₀^k₂·u₀^k₃ (Eq 7.49, p.163). The full model minimises unit cost C_P (Eq 7.65) over (T_AC, u, H/V, L/D, n_f/D); capital recovery e from interest i and loan N (Eq 7.67). Thermal efficiency η_th = (Q₁)/(Q₁+…+Q₅) (Eq 7.81, p.167).

## 10. Academic Critique & Open Questions

- The residence-time literature is sand/ore-centric; no validation for polydisperse, low-density SAP granules where fines entrainment (p.150) and bounce differ. A hygiene-specific RTD measurement (radioactive or inert tracer, p.155) is still required.
- The design model's plug-flow holdup (Eq 7.61) contradicts the authors' own "not safe to assume plug flow" (p.155). The 7.7 model therefore optimises the mean, not the moisture tail.
- Heat-transfer scale-up from pilot (large shell-area/volume, ~15% heat loss) to commercial (smaller losses) is "a lot better in commercial dryers" but "requires caution and experience" (p.159) — not a predictive tool.
- Open questions: (1) What is the Uₐ for a SAP-granule / cellulose-acetate / PP-pellet curtain at 2–5 m/s? (2) How does fines entrainment shift the optimal 10–15% fill for a dusty superabsorbent feed?

## 11. Hygiene-Material Relevance & Action Cards

Relevance to diaper/wipe/absorbent-core R&D: ★★★☆☆ (rotary drying is a post-treatment option for granular SAP and polymer flake, not for webs/fluff mats).

ACTION CARD H11.1 — Specify cocurrent flow for SAP/cellulose-acetate post-drying. Situation: drying heat-sensitive free-flowing SAP granules or cellulose-acetate flake. Apply: set cocurrent gas/solid flow so the high inlet temperature (up to 800–1100 K for fired burners, p.161) is quenched at first evaporation (p.149). Effect: avoids thermal degradation / crosslink scission of the polyacrylate network.

ACTION CARD H11.2 — Hold 10–15% drum fill, size flights to free-flowing feed. Situation: designing or auditing a rotary SAP post-dryer. Apply: 90° lip radial flights (free-flowing, p.152); verify holdup H/V ∈ [5,15]% (constraint p.165); L/D in [4,10]. Effect: maximises cascading contact, prevents bypass by kiln action and loss of hot-gas contact (p.153).

ACTION CARD H11.3 — Close the moisture tail, not the mean. Situation: setting the residence-time spec. Apply: compute tₜ = H/F (Eq 7.61) but qualify against the "maximum moisture of any particle" criterion (p.155); do not assume plug flow. Effect: guarantees no under-dried SAP granule reaches the packaging spec.

ACTION CARD H11.4 — Budget thermal efficiency 55–75% (fired) / 30–55% (steam). Situation: capex/opex estimate for a SAP post-dryer. Apply: use p.162 ranges; steam-heated air halves efficiency. Effect: realistic energy-cost-per-tonne for the absorbent-core line.

## 12. Book-Map Quotes

"Cocurrent flow is used for heat-sensitive materials even for high inlet gas temperature due to the rapid cooling of the gas during initial evaporation of surface moisture" — p.149 — the governing selection rule for an SAP/cellulose-acetate post-dryer.
"The total amount of solids contained in the drum is about 10–15% of its volume … this loading gives the most efficient performance" — p.153 — the single most actionable design constraint.
"it is not safe to assume plug flow of the particles in industrial dryers" — p.155 — caps the design model's plug-flow assumption and motivates RTD measurement.
"the development of a universal model of the rotary dryer, that combines the cascading motion of the particles with the heat and mass transfer, is questionable" — p.168 — honest scope limit of the whole chapter.

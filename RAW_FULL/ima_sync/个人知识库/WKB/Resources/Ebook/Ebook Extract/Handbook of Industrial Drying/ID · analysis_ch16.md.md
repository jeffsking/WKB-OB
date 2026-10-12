---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_1dba20ddf7923f440e1b6c9a4553717c001a693ee6c0644e"
source_file: "ID · analysis_ch16.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch16.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch16.md.md

# Chapter 16 — Pneumatic and Flash Drying

## 1. Chapter Overview (范围、对象与定位)

Chapter 16 (Irene Borde and Avi Levy) treats pneumatic (flash) drying as a gas–solid transport convective dryer in which wet particulates are suspended in a hot gas (usually air, sometimes superheated steam) and conveyed through a duct, with residence time in the drying section of only 0.5–10 s (p.395). The chapter's logical spine: because contact time is so short and flow is parallel (co-current), the material temperature stays always low (p.395), which makes flash drying suitable only for external/surface moisture and for thermolabile solids, but less suitable for internal moisture (p.395–396). The body then delivers (16.2) operation principle and application inventory, (16.3) a design procedure built on heat/mass/momentum balances plus transfer coefficients, (16.4) a long list of dried materials, (16.5) the modelling menu — empirical pressure-drop correlations, Rocha/DryPak models, and the two-fluid/Eulerian-granular/DEM frameworks with the full balance-equation set (16.5)–(16.25), and (16.6) expected developments (heat recovery, heat pumps, combined processes). For the hygiene reader this is a weak chapter: flash drying handles particulates and pastes, not the continuous webs, fluff fibre mats, or airlaid nonwovens that dominate diaper/wipe manufacture. The genuinely relevant threads are narrow but real — drying of SAP powder and polymer pellets, the dust-explosion safety limit on cellulosic/SAP powders, and superheated steam as an explosion-free medium.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.395–p.408 (PDF p.416–429).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — Short contact time keeps material temperature low; only surface moisture is removed.
> "One of the features of these types of dryers is the relatively short contact time between the hot air and the particulate materials (0.5–10 s) at the drying section. Because of this the material temperature stays always low in the drying process… flash dryers are most suitable for removal of external moisture (surface moisture) and are less suitable for removal of internal moisture." (p.395–396)
Interpretation: This is the governing capability boundary. A flash dryer is a surface-moisture dryer; bound/internal moisture (e.g. the falling-rate period of a fluff mat) cannot be removed here. Hygiene relevance is therefore to powders/pellets, not webs.

V2.2 — Parallel flow + short time permit thermolabile materials.
> "Short contact time and parallel flow make possible to dry thermolabile materials." (p.396)
Interpretation: The co-current geometry is what protects heat-sensitive polymer powders (SAP, PP/PE masterbatch) from thermal degradation — the same design logic later invoked for superheated-steam and infrared dryers.

V2.3 — Gas velocity must exceed the free-fall velocity of the largest particle (design gate).
> "The gas velocity must be greater than the free fall velocity of the largest particle to be dried." (p.396)
Interpretation: This single inequality sets duct diameter, fan power, and residence-time distribution; it is the first sizing constraint for any pneumatic line.

V2.4 — Dust fire/explosion is the safety red line.
> "There is a risk of fire and explosion, so care must be taken to avoid flammability limits in the dryer." (p.397)
> "Because of powder emission, the dryer cannot be used for toxic materials. In some cases this disadvantage can be avoided using superheated steam as a drying agent." (p.397)
Interpretation: Cellulosic fibre dust and SAP powder are combustible; the explosion/flammability limit is a hard operating constraint, and superheated steam is offered as the escape route.

V2.5 — Superheated steam removes fire/explosion risk but complicates the system.
> "Flash dryers using superheated steam as drying medium instead of air have some advantages such as no fire or explosion risk and higher efficiency (if exhaust steam is utilized elsewhere in the process)." (p.399)
> "The limitations of using superheated steam as drying medium are that the system itself and the operation of the system are more complex. Leaks are prohibited as noncondensables cause problems with energy recovery by condensation or compression of the exhaust steam. The feeding and discharge process must not allow infiltration of air and start-up and shutdown processes are more complex than for air dryers." (p.399)
Interpretation: Steam is the elegant answer to the explosion problem but demands air-tight feeding/discharge and makes energy recovery via condensation conditional on zero in-leakage.

V2.6 — Polymer/powder industries are a core application; PVC is the modelled case.
> "Flash dryers are widely used in the plastic and polymer industries." (p.400)
> "Andrieu and Bressat [16] presented a simple model for pneumatic drying of PVC particles." (p.401)
Interpretation: The only polymer-specific, quantitatively modelled example is PVC — directly relevant to thermoplastic pellet drying, and the design temperature is bounded by the solid's thermal sensitivity (p.397).

## 3. Research Method & Data Sources

The chapter is a review + design-method compilation + modelling survey (Borde & Levy's group supplies many of the references). Method:
- Empirical correlation route (16.3, 16.5.1): total pressure drop split as Δp = Δp_g + Δp_s (Eq.16.1); Muschelknautz & Wojahn, Pan & Wypych, Mason et al. for pipe/bend losses; Table 16.1 for h in gas–particle flows.
- Theoretical route (16.5.2): two-fluid theory, Eulerian granular (kinetic theory of granular flow), discrete element method (DEM, Lagrangian). Two-fluid and Eulerian-granular solve macroscopic mass/momentum/energy balances for both phases; DEM tracks each particle.
- Validation caveat: "It should be kept in mind that the developed mathematical model should be experimentally validated in order to use it as a design tool." (p.403)
No new hygiene empirical data; the value is the transfer correlations and the two-fluid equation set.

## 4. Argumentation Process

- Premise A: Drying = phase change + solid product; flash drying is a gas–solid transport system with very short contact (p.395).
- Premise B: Short co-current contact ⇒ low material temperature ⇒ good for surface moisture and thermolabile solids, poor for internal moisture (p.395–396).
- Step: Therefore size by free-fall velocity (p.396), run gas as hot as the solid's thermal sensitivity allows (p.397), manage dust/explosion risk (p.397), and recover height/time via recirculation or two-stage/ring/spin-flash variants (p.398–399).
- Resolution: For hazardous powders use superheated steam (p.399); for pastes/sludges use spin-flash (p.399); for scale-up use two-fluid/DEM models validated against data (p.402–407).
The argument is candid that residence time is non-uniform under recirculation (p.397) and that models need experimental validation (p.403) — appropriate scope honesty for a review.
## 5. Role in the Book

Ch.16 is the dilute-phase particulate convective dryer in the dryer taxonomy. It complements Ch.14 (spouted bed — dense-phase inert particles), Ch.15 (impingement — continuous sheets), Ch.17 (conveyor/belt — continuous webs), and Ch.18 (infrared — radiative). Its unique position is gas–solid suspension with second-scale residence; it is the only chapter whose primary feed is free-flowing powder/pellets, which is exactly why its hygiene relevance is narrow (SAP powder, polymer masterbatch) rather than web/fibre-centric.

## 6. Strengths & Weaknesses

Strengths
- States the surface-moisture / internal-moisture boundary and the thermolabile advantage explicitly (p.395–396).
- Gives a usable design procedure (heat/mass/momentum balances + transfer coefficients, p.397–399) and Table 16.1 Nu correlations (p.405).
- Treats dust fire/explosion and the superheated-steam escape route head-on (p.397, p.399).
- Provides the full two-fluid balance-equation set (16.5)–(16.25) as a scale-up kernel (p.403–406).

Weakes / contestable points
- No energy benchmark. Unlike Ch.15 (3100 kJ/kg water, 75–90 % efficiency), Ch.16 gives no specific-energy figure, so cross-chapter energy cost/tonne comparison is impossible. [inference]
- Feed-size unit inconsistency. The text states "The size of particulates to be dried is usually in the range of 10–500 mm" (p.395). A 10–500 mm range describes gravel/rocks, not the powders/pellets a flash dryer handles; this is almost certainly a typesetting error for µm (10–500 µm). Quoted verbatim per the hard rule; treat as [未找到原句/页码缺失]-free but physically suspect. [inference]
- No fibre/web relevance. Nothing on fluff, nonwoven, or tissue; the chapter is silent on the materials that dominate hygiene manufacture.
- Polymer treatment is one example deep. PVC is modelled (p.401) but Tg / melting / thermal-degradation of the polymer is not formulated into the design constraint (only the vague "thermal sensitivity of the solids", p.397).

## 7. Key Terms / Concepts

- Pneumatic / flash drying: gas–solid transport convective dryer; direct unit, co-current (p.395).
- Free-fall (terminal) velocity: gas must exceed it for the largest particle to stay suspended (p.396).
- Surface (external) moisture: the only moisture class flash dryers remove well (p.395–396).
- Thermolabile materials: dryable because of short contact + parallel flow (p.396).
- Flammability limits: the explosion/fire safety envelope for powders (p.397).
- Superheated steam medium: explosion-free, higher efficiency if exhaust steam is reused (p.399).
- Spin-flash dryer: mechanically agitated fluidized bed for pastes/sludges/filter cakes, no atomizer, up to 10 t/h (p.399).
- Two-fluid theory: macroscopic phase-averaged mass/momentum/energy balances for gas and solid (p.403–405).
- Dilute vs dense phase: transport velocity keeps majority of particles suspended (p.402).
## 8. Micro close-reading (微观精读)

8.1 — The capability boundary (p.395–396). "flash dryers are most suitable for removal of external moisture (surface moisture) and are less suitable for removal of internal moisture." This one sentence is the chapter's indispensable design gate for the hygiene engineer. SAP powder and polymer pellets carry essentially surface moisture → flash-dryable. A fluff-pulp mat or airlaid web carries bound moisture in its falling-rate period → flash drying would only scour the surface and leave the core wet. The corollary (p.395) is that material temperature stays always low precisely because the latent heat of the surface moisture dominates; once that moisture is gone the safety case weakens.

8.2 — The safety red line (p.397). "There is a risk of fire and explosion, so care must be taken to avoid flammability limits in the dryer… Because of powder emission, the dryer cannot be used for toxic materials. In some cases this disadvantage can be avoided using superheated steam as a drying agent." Cellulosic fibre fines and SAP dust are combustible particulates; this paragraph is the only place the chapter speaks directly to hygiene-relevant powder safety. Superheated steam is presented as the compliant alternative.

8.3 — The thermal-sensitivity constraint (p.397). "the temperature of the hot gas should be as high as possible without exceeding limits imposed by the thermal sensitivity of the solids or safety considerations." This is where polymer science should enter but does not: "thermal sensitivity" is left unquantified — see POP trailer.

8.4 — The scale-up kernel (p.403–404). The two-fluid continuity (16.5), momentum (16.6), and energy/enthalpy (16.15) equations, closed by the interphase heat-exchange term Q_gs = 6 ε_s(1−ε_s) λ_g (T_g − T_ss)/d_s² (16.16) and the drag law C_D = max[24(1+0.15Re^0.687)/Re, 0.44] (16.13), are what let a designer predict outlet moisture from inlet temperature and particle size.

💡 Standout line: "flash dryers are most suitable for removal of external moisture (surface moisture) and are less suitable for removal of internal moisture" (p.395–396) — the sentence that tells a hygiene engineer flash drying is a powder/pellet tool, not a web tool.

## 9. Concept deep-dive (概念深掘)

9.1 Two-fluid balance equations (16.5.2). Continuity for phase k (k = g or s):
∂(ε_k ρ_k)/∂t + ∇·(ε_k ρ_k V_k) = S_k  (16.5, p.403)
Momentum:
∂(ε_k ρ_k V_k)/∂t + ∇·(ε_k ρ_k V_k V_k) = −∇(ε_k P_k) + ∇·τ_k + ε_k ρ_k g + M_kj + S_k V_k  (16.6, p.403)
Energy (enthalpy):
∂(ε_k ρ_k h_k)/∂t + ∇·(ε_k ρ_k V_k h_k) = ε_k ∂P_k/∂t + τ_k:∇V_k − ∇·q_k + Q_k + Q_kj + S_k h_kj  (16.15, p.404)
Interphase heat exchange:
Q_gs = 6 ε_s (1−ε_s) λ_g (T_g − T_ss) / d_s²  (16.16, p.404)
with Nu = h_gs d_s / λ_g = F(Re, Pr), Re = ρ_g |V_g − V_s| d_s / μ_g, Pr = μ_g c_pg / λ_g (16.17–16.18, p.404). Single-particle evaporation in period 1: ṁ_s = h_m π d_s² (M_w p_vo/(R T_ss) − p_vg/(R T_g)) (16.20, p.405); period 2 (dry crust + wet core) is a Stefan-type diffusion (16.21, p.405–406). These close the loop inlet-T → residence → outlet-moisture.

9.2 Particle-size effect (p.403). "As the particle size was increased, the heat transfer rate decreases and the residence time increases… less permeable wood species or larger chips size leads to longer dryer." Direct scale-up lesson: larger/less-permeable particles need longer ducts or higher gas velocity — applicable to coarse SAP agglomerates.

9.3 Spin-flash (p.399). Mechanically agitated fluidized bed; handles sludge, pulps, pastes, filter cakes, high-viscosity liquids without an atomizer; up to 10 t/h. Relevant if a hygiene line must dry a high-solids SAP slurry or binder paste.

## 10. Academic critique & open questions

- Constant-rate framing only. The single-particle model (16.20) is first-period (gas-film controlled); period 2 is Stefan diffusion through a dry crust (16.21). No hygroscopic-equilibrium or bound-moisture treatment — exactly the regime fluff/SAP care about.
- No energy intensity. A dryer-selection chapter with no kJ/kg figure cannot support the energy-cost/tonne question the brief raises; Ch.15's 3100 kJ/kg is the only adjacent anchor.
- Feed-size typo. "10–500 mm" (p.395) is physically inconsistent with flash-dryer practice; should read µm. [inference]
- Open question: How does the two-fluid kernel behave for hygroscopic particles (SAP) where internal diffusion is bound-moisture controlled and the crust forms at a critical solid-to-liquid mass ratio j_cr from a minimum void fraction (p.405–406)? The chapter derives it for sand/wood, not for swellable superabsorbent.
- Open question: For polymer pellets, what is the quantitative link between inlet gas temperature and the polymer's Tg / thermal-degradation onset? The chapter says only "thermal sensitivity of the solids" (p.397).
## 11. Hygiene-material relevance & action cards

Relevance rating: ★★☆ (narrow). Flash drying is a particulate/paste dryer. It does not dry tissue, nonwoven webs, or fluff mats. The real hygiene hooks are SAP powder, polymer masterbatch, and powder-explosion safety — rated below.

H11.1 — Use flash drying only for surface-moisture powders (★★★★). Action: Route SAP powder, PP/PE masterbatch, and other free-flowing hygrology powders through flash/spin-flash lines sized by free-fall velocity (p.396); do not use it for bound-moisture fluff or web. Expect only surface-moisture removal (p.395–396).

H11.2 — Set inlet gas T from the polymer's thermal window, not just evaporation (★★★★). Action: Cap inlet temperature below the solid's thermal-degradation/Tg (p.397, "thermal sensitivity of the solids"); for PVC-like thermoplastics validate against a decomposition onset. See POP trailer.

H11.3 — Engineer the dust-explosion limit (★★★★★). Action: For cellulosic/SAP dust, stay outside flammability limits (p.397) via inerting or — preferably — superheated steam medium (p.399), which removes fire/explosion risk; if steam, enforce air-tight feed/discharge (p.399).

H11.4 — Consider spin-flash for high-solids slurries/pastes (★★★). Action: A binder or SAP slurry/paste that would otherwise need spray-atomization can be spin-flash dried without an atomizer, up to 10 t/h (p.399) — cheaper thermal energy than spray drying (p.399).

H11.5 — Predict scale-up with the two-fluid kernel (★★★). Action: Use Eqs. (16.5)–(16.25) to forecast that larger/coarser SAP agglomerates need longer residence or higher gas velocity (p.403); validate the model against pilot data first (p.403).

## 12. Book-map quotes (本书脉络引证)

- Ch.15 (p.383): impingement — the sheet/web convective dryer that flash drying cannot replace; flash is the powder counterpart.
- Ch.17 (p.409): conveyor/belt dryers — the continuous-web technology that actually dries nonwovens and airlaid mats.
- Ch.19 (p.437): superheated steam drying — the medium Ch.16 already recommends (p.399) to kill the explosion risk; Ch.19 generalizes it.
- Ch.14 (p.361): spouted bed — dense-phase alternative for particulates; flash is the dilute-phase counterpart.

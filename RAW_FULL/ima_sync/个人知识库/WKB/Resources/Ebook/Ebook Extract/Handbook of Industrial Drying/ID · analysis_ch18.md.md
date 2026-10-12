---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_01e0062270e836ca7ae1b56c7375cba4001a693ee6c0644e"
source_file: "ID · analysis_ch18.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch18.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch18.md.md

# Chapter 18 — Infrared Drying

## 1. Chapter Overview (范围、对象与定位)

Chapter 18 (Cristina Ratti and Arun S. Mujumdar) covers infrared (IR) radiative drying — supplying heat by electromagnetic radiation that needs no propagation medium and is absorbed/converted to heat at the product surface (§18.2). The argument: IR is "an increasingly popular, but not yet common" primary heat source whose strengths are direct volumetric/near-surface energy deposit, fast transient response, leveling of moisture profiles, and easy combination with convection or vacuum (p.421–422). The chapter delivers the radiative-transfer theory (black/gray body, Planck, Wien, Stefan–Boltzmann, Kirchhoff, Bouguer attenuation — §18.2), the radiation properties of materials and the critical need to match emitter wavelength to the product's absorption band (§18.2.2), a steady-IR modeling framework (semi-transparent "Hasatani" and opaque boundary models, §18.3.1), advantages/limitations (§18.3.2), industrial dryers and emitters (§18.4.2), costs (§18.4.3), and conclusions (§18.5). For the hygiene reader this is a ★★★★☆ chapter: the chapter opens by naming "dehydration of coated films and webs" and "correct moisture profiles in drying of paper and board" as the most common IR applications (p.421), and later shows an IR + impingement oven "specially for drying adhesives and inks on papers, foam and composite web substances" (p.432) — i.e. exactly the lotion/coating cure on wipes and the combination with Ch.15's impingement. The genuine limitation to state honestly: IR is "essentially surface dryers" (p.429) and penetration into thick porous webs is still underdeveloped.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.421–p.436 (PDF p.442–457; chapter body to ~p.434).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — Coated films/webs and paper moisture correction are the prime IR applications.
> "The most common current applications of IR drying are in dehydration of coated films and webs and to correct moisture profiles in drying of paper and board." (p.421)
Interpretation: Verbatim hygiene anchor — IR cures coatings on webs (wipe lotion, adhesive, print) and flattens moisture profiles on paper/board. This is the lotion-cure-on-wipes link named in the brief.

V2.2 — IR is combined with convection/vacuum; applied intermittently to save energy and improve quality.
> "combined convective and IR dryers have been shown to be very attractive. Also, IR heating can be coupled effectively with vacuum operation… IR heating may be applied continuously or intermittently (in space or time) to save energy and often to improve product quality." (p.422)
Interpretation: IR is almost never standalone; the productive configuration is hybrid (radiant + convective), which is the Ch.15/Ch.18 overlap used for web coating cure.

V2.3 — Opaque solids absorb in a thin surface layer ⇒ IR is a surface dryer.
> "Generally solid bodies absorb all of the radiation in a very narrow layer near the surface. This is a very important consideration in modeling the heat transfer process…" (p.422)
> "an 'opaque' solid absorbs radiation in a narrow zone near the surface rather than attenuating within its volume" (p.427)
Interpretation: The physics that makes IR fast for coatings also caps it: penetration is shallow for opaque webs, so IR cures the coating/surface, not the bulk. Directly supports the "essentially surface dryers" limitation (p.429).

V2.4 — Match emitter wavelength to the product's absorption band; adjust emitter T as moisture leaves.
> "For many materials, transmissivity is higher at lower wavelengths… Foods are complex mixtures of different large biochemical molecules and polymers, inorganic salts, and water… As drying proceeds, the material… increasing its reflectivity, and consequently lowering its absorptivity at low water contents. It is then possible to change adequately the temperature of the emitter in order to improve the absorption of radiation during drying." (p.424–425)
Interpretation: The emitter must be tuned to the coating/web absorption spectrum, and re-tuned as the wet coating dries (reflectivity rises). This is the coating-cure-kinetics design rule; see POP trailer for polymer IR bands.

V2.5 — Wrong emitter ⇒ surface scorching; pick source T for penetration vs peak absorption.
> "To avoid overheating of the surface and to allow the radiation to penetrate into the product it would be better to choose the heat source at 2500 K… On the other hand, if the lower heat source temperature is used, the surface may be damaged (scorched) due to intense surface heating." (p.425)
Interpretation: Emitter-temperature selection trades penetration depth against surface flux; too low a source T scorches the surface. For a heat-sensitive nonwoven/wipe coating this is the degradation-avoidance rule.

V2.6 — IR + impingement combo is the industrial web-coating cure.
> "a high velocity hot air impingement oven with IR electric heaters mounted between adjacent nozzles… specially for drying adhesives and inks on papers, foam and composite web substances." (p.432)
Interpretation: This is the literal unit operation for wipe lotion/print cure: radiant heaters interleaved with impingement nozzles (ties Ch.18 to Ch.15). The combination "has already proven to be industrially viable" (p.434).

## 3. Research Method & Data Sources

The chapter is a theory + equipment-design review (Ratti/Mujumdar; heavy food/paint/paper literature). Method:
- Radiative-transfer theory (§18.2): Planck (18.2), Wien (18.3), Stefan–Boltzmann (18.4), black-body exchange (18.5), reciprocity (18.6)/(18.7), gray-body net (18.8), Bouguer attenuation (18.9).
- Material-property tables (§18.2.2): Table 18.1/18.2 transmissivity of foods, paper, wool, wood; Sieber emissivity data.
- Steady-IR modeling (§18.3.1): energy balance modified to add q_r (18.12), semi-transparent (Hasatani) vs opaque (18.17/18.18) boundary; batch fixed-bed equations (18.22–18.25).
- Empirical/industrial: emitter efficiencies (Table 18.3), costs (Table 18.4), Figure 18.10 impingement-IR oven.
No hygiene-specific data; value is the radiative theory, the emitter-matching principle, and the hybrid-oven evidence.

## 4. Argumentation Process

- Premise A: Radiation deposits heat with no medium; opaque solids absorb in a thin surface layer (p.422) → fast surface heating, shallow penetration.
- Premise B: A material's a/r/t depend on wavelength (p.424); so emitter must match the product band and be re-tuned as it dries (p.425).
- Step: Pick emitter (electric quartz lamp / sheath / gas-fired) by absorption, power density, radiant/convected ratio (p.431); combine with convection (air cools walls, exhausts solvent) and/or vacuum; run intermittently to save energy (p.422, p.434).
- Resolution: IR dominates surface/coating cure on thin sheets, films, paper, textiles (p.421, p.429); hybrid impingement-IR ovens are industrially proven (p.432, p.434).
Honest scope note: penetration into thick porous webs "has not yet been fully developed" (p.430) and scale-up "is not always straightforward" (p.429).
## 5. Role in the Book

Ch.18 is the radiative dryer chapter — the counterpart to Ch.15 (convective impingement) and Ch.12 (microwave/dielectric). Its unique position is surface/coating cure with no medium, which is why it is the natural technology for lotion/ink/adhesive cure on wipes and for moisture-profile correction on paper/board. The hybrid IR + impingement oven (p.432) is where Ch.18 and Ch.15 physically merge.

## 6. Strengths & Weaknesses

Strengths
- Opens with the hygiene-relevant application verbatim: coated films/webs, paper moisture correction (p.421).
- Gives the full radiative-transfer toolkit (Planck/Wien/Stefan–Boltzmann/Kirchhoff/Bouguer) with a gray-body net equation (18.8).
- States the emitter-matching + moisture-dependent-retuning rule (p.424–425) and the scorch-vs-penetration trade (p.425).
- Shows the proven IR + impingement hybrid for adhesives/inks on web (p.432) and concrete cost comparisons (Table 18.4: IR 500 $/kW vs convection 300, RF 2000).

Weaknesses / contestable
- Surface-only. "Essentially surface dryers" (p.429); penetration into thick porous webs underdeveloped (p.430). For a bulky fluff core IR cures only the surface.
- Unit slips. Wavelengths are printed as "mm" (near IR 0.75–3.00 mm, λ_max T = 2897.6 µm·K in Eq.18.3) — the "mm" is inconsistent with Wien's law and should read µm. [inference] Quoted verbatim per the hard rule; treat as µm.
- No polymer-coating spectra. The chapter gives food/paper transmissivity (Table 18.1/18.2) but no IR absorption bands for the acrylic/PVA/PU coatings actually used on wipes; the hygiene engineer must supply those (see POP trailer).

## 7. Key Terms / Concepts

- Thermal radiation: 0.1–100 µm span (source prints "mm"); near/medium/far IR by wavelength (p.422) — unit should be µm.
- Black/gray body: ideal absorber (ε=1) vs wavelength-independent ε (p.422–424).
- Emissivity/absorptivity/reflectivity/transmissivity (ε,a,r,t): r+a+t=1; wavelength-dependent (p.424).
- Bouguer's law: I_λ(z)=I_λ(0)exp(−∫K_λ dz) — in-body attenuation (18.9, p.423).
- Semi-transparent vs opaque model: penetration vs surface absorption (p.427).
- Emitter: electric (metal sheath / quartz tube / quartz lamp) or gas-fired; quartz lamp radiant efficiency 86 % (Table 18.3, p.431).
- Moisture-profile leveling: a named IR advantage (p.428).
- Fire hazard: a listed IR limitation (p.429).
## 8. Micro close-reading (微观精读)

8.1 — The application sentence (p.421). "The most common current applications of IR drying are in dehydration of coated films and webs and to correct moisture profiles in drying of paper and board." This single clause is the hygiene charter for the chapter: IR = coating cure on a web + moisture leveling. A wipe is a "coated film on a web"; the lotion/cream layer is the coating, the nonwoven substrate is the web.

8.2 — The absorption-matching rule (p.424–425). "As drying proceeds, the material… increasing its reflectivity, and consequently lowering its absorptivity at low water contents. It is then possible to change adequately the temperature of the emitter in order to improve the absorption of radiation during drying." The coating's optical properties drift as water leaves; a fixed emitter wavelength over-cures late in the cycle. The control loop is: track reflectivity → shift emitter T. For a wipe lotion line this is the lehr-temperature ramp that protects the polymer film.

8.3 — Scorch vs penetration (p.425). "choose the heat source at 2500 K… allow the radiation to penetrate… if the lower heat source temperature is used, the surface may be damaged (scorched)." Counter-intuitive: a hotter source penetrates better (peak at shorter λ where the wet coating absorbs less intensely), while a cooler source dumps all energy into the surface and scorches it. Emitter T is an optical-design, not just a thermal, variable.

8.4 — Hybrid oven (p.432). "a high velocity hot air impingement oven with IR electric heaters mounted between adjacent nozzles… drying adhesives and inks on papers, foam and composite web substances." The radiant heater sits between impingement nozzles: radiation cures the coating, convection strips solvent/water and protects the substrate. This is the canonical wipe-coating-cure machine.

8.5 — Energy math (p.434, Table 18.4). IR capital cost 500 $/kW vs convection 300, RF 2000; quartz-lamp emitter 0.49 (equal basis), life 2000–3000 h. IR is mid-cost, low-footprint, but lamp replacement is the maintenance item — a lifecycle cost the brief's energy-question must include.

💡 Standout line: "dehydration of coated films and webs" (p.421) — the four words that make Ch.18 a wipe-lotion/coating-cure chapter, not just a food-dehydration chapter.

## 9. Concept deep-dive (概念深掘)

9.1 Radiative-transfer equations (§18.2). Black-body fraction: r + a + t = 1 (18.1, p.422). Wien displacement: λ_max T = 2897.6 µm·K (18.3, p.422) — fixes peak λ from source T. Stefan–Boltzmann: E_b = σT⁴ (18.4, p.422). Net gray-body exchange:
Q_r = (σ (T_i⁴ − T_j⁴)) / (1/ε_i A_i + F_ij (1/ε_j A_j − 1)/... ) (18.8, p.423–424). Bouguer attenuation in the body: I_λ(z) = I_λ(0) exp(−∫ K_λ dz) (18.9, p.423). These let the engineer size emitter power from source T and view factor.

9.2 Material-property dependence (§18.2.2). a, r, t depend on material, thickness, surface finish, and wavelength (p.424). Conductors' ε rises with λ; nonconductors fall. So an emitter must be chosen for the wavelength where the coating absorbs but the substrate does not (p.425, Fig.18.3).

9.3 Steady-IR process model (§18.3.1). Only the energy balance changes; mass balance unchanged (18.10, p.426). For an opaque particle: ρ C_p ∂T/∂t = k ∂²T/∂z² + ∂q_a/∂z (18.12, p.426–427) with q_a = Q_r exp(−∫ K dz) (18.16). Surface boundary carries the radiative term (18.15 → 18.18). Batch fixed-bed form: gas/solid mass + energy balances (18.22–18.25). The model is the scale-up kernel, but "testing of the equipment must be carried out in the plant" (p.429).

9.4 Emitter selection (§18.4.2). Five factors (p.431): absorption characteristics of heated material, power density seen by product, ratio of convected to radiant heat, installation nature, control type. Quartz lamp = highest efficiency (86 %), gold reflector directs flux (p.431).

## 10. Academic critique & open questions

- Penetration gap. "Essentially surface dryers" (p.429) and thick-porous "not yet fully developed" (p.430). The semi-transparent model (18.12/18.16) exists, but no validated penetration correlation for a nonwoven web whose porosity collapses during cure.
- No coating-polymer spectra. Tables 18.1/18.2 cover food/paper/wool/wood, not the acrylic/PVA/PU/EMA coatings on wipes. The emitter-matching rule (p.425) is given but the hygiene engineer must supply the band data.
- Unit error. Wavelengths printed as mm; Eq.18.3 (λ_max T = 2897.6 µm·K) and the near/medium/far IR ranges (0.75–100 µm) prove µm. [inference]
- Open question: For a lotion-coated wipe, what is the optimal emitter-T ramp that keeps the polymer film below its thermal-degradation onset while driving water/solvent out fastest? The chapter implies re-tuning (p.425) but gives no coating-cure-kinetics model.
- Open question: How does the IR + impingement hybrid (p.432) partition duty between radiant cure and convective solvent removal for a given coating thickness? Not quantified.
## 11. Hygiene-material relevance & action cards

Relevance rating: ★★★★☆ (strong for wipe lotion/coating cure; weaker for bulk cores).

H11.1 — Use IR for the lotion/print coating cure on wipes (★★★★★). Action: Deploy IR for dehydrating/curing the coated film on the wipe web (p.421); it is the right tool for thin coatings, not the bulk nonwoven.

H11.2 — Build the hybrid IR + impingement oven (★★★★★). Action: Mount IR electric heaters between impingement nozzles (p.432) — radiation cures the coating, convective jets strip solvent/water and protect the substrate; proven viable (p.434). Reuse Ch.15 nozzle design.

H11.3 — Match emitter wavelength to the coating band; ramp T as it dries (★★★★★). Action: Pick source T so the peak λ sits where the coating absorbs but the substrate does not (p.425, Fig.18.3); raise emitter T as reflectivity climbs during drying (p.425) to avoid late-cycle under-cure or scorch. See POP trailer for polymer bands.

H11.4 — Avoid scorch with a hotter, better-penetrating source (★★★★). Action: Counter-intuitively choose the higher source T for penetration (p.425); a cooler source dumps flux at the surface and scorches the polymer film.

H11.5 — Level the web moisture profile (★★★★). Action: Use IR's "leveling of the moisture profiles" advantage (p.428) to even cross-web moisture on coated/printed wipes; combine with humidity-controlled exhaust (p.430).

H11.6 — Engineer fire safety and solvent exhaust (★★★★). Action: IR carries a fire-hazard flag (p.429); size oven exhaust to remove solvent/smoke/moisture (p.430) for combustible nonwoven substrates and volatile coating carriers.

H11.7 — Cost at IR 500 $/kW, plan lamp replacement (★★★). Action: Budget IR capital at ~500 $/kW (Table 18.4, p.434), quartz-lamp life 2000–3000 h (p.433) as the maintenance line in the energy-cost/tonne model.

## 12. Book-map quotes (本书脉络引证)

- Ch.15 (p.383): impingement — the convective partner merged into the IR + impingement hybrid oven (p.432).
- Ch.17 (p.409): conveyor/through-circulation — the permeable-bed counterpart; IR is surface-only where Ch.17 is through-bed.
- Ch.12 (p.283): microwave/dielectric — alternative volumetric heating; Table 18.4 prices IR (500) between convection (300) and RF (2000).
- Ch.40 (p.929): Drying of Coated Webs — the chapter that generalizes the "coated films and webs" application named at p.421.

---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_02f09606422fd7fa75d2c6754bf9479b001a693ee6c0644e"
source_file: "ID · analysis_ch30.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch30.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch30.md.md

# Chapter 30 — Drying of Nanosize Products

## 1. Chapter Overview (范围、对象与定位)

Chapter 30 (Baohe Wang, Li Xin Huang, and Arun S. Mujumdar) is the book's nanomaterials-drying chapter, concerned with two failure modes that are absent or trivial at macroscopic scale: (i) cracking/collapse of the fragile porous gel skeleton and (ii) irreversible agglomeration of nanoparticles during solvent removal. The chapter's logic: nanomaterials are defined by their  nm features (p.711); because nanoparticles "tend to agglomerate and properties... are adversely affected if we do not choose appropriate drying methods" (p.712), drying must preserve dispersion. It first builds the solvent-evaporation mechanism (Scherer's three periods: constant-rate → first falling-rate → second falling-rate) and the capillary-pressure theory P = 2σ cosθ / r as the root cause of both cracking and agglomeration, then surveys direct, solvent-replacement, and modified drying families with quantitative product tables (TiO₂, MgO, BaTiO₃), and closes with selection rules and the open challenge of agglomeration + nanoparticle inhalation safety. For the hygiene reader this is a ★★★★ chapter: its capillary-pressure and particle–particle-force framework transfers directly to SAP (sodium polyacrylate) fines handling, nanocellulose/CMC dewatering, agglomerate control and redispersibility.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.711–p.726 (PDF p.732–747).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — Nanoparticle dispersion during drying is a vital, failure-prone requirement.
> "Nanoparticles tend to agglomerate and properties of nanoparticles are adversely affected if we do not choose appropriate drying methods. So to assure that nanoparticles are well dispersed during drying is a vital requirement in the preparation of such products." (p.712)
Interpretation: The core hygiene problem for SAP fines and nanocellulose — keep particles dispersed; wrong drying = hard agglomerates that never redissolve.

V2.2 — Solvent evaporation runs through three periods; the critical point is where liquid curvature radius equals pore size.
> "It is generally believed that solvent evaporation involves three periods, namely a constant rate drying, a first falling rate, and a second falling rate... At the critical point where the constant rate-drying period ends and the first falling rate-drying period begins, the radius of curved liquid is equal to the size of the gel pores... capillary tension reaches maximal value." (p.713)
Interpretation: The drying-rate-curve structure (also used in Ch.4/Ch.33) couples to a mechanical peak stress at the critical point — the exact moment gel/pad damage occurs.

V2.3 — Capillary pressure is the single cause of both cracking and agglomeration.
> "Capillary pressure is the major cause leading to cracking of the gel skeletons or agglomeration of nanoparticles during drying... P = 2σ cosθ / r_p." (p.714)
Interpretation: Eq. (30.1) is the master equation: capillary pressure scales with surface tension σ and inversely with pore/particle radius r_p — tiny pores ⇒ huge stresses. Directly governs SAP-fines clumping and nanocellulose mat densification.

V2.4 — Lowering σ, setting θ→90°, or enlarging r_p defeats capillary pressure.
> "in order to prevent nanoparticles from agglomerating or gels from collapsing, capillary pressure must be decreased to a minimum. The following means can decrease capillary pressure: Reducing surface tension (using supercritical drying, freeze-drying, and solvent-replacement drying); Changing wetting angle and making it approach 90° (surface modification drying); Enlarging pore size of gels properly... and making it uniformly." (p.714)
Interpretation: Three engineering levers — σ, θ, r — exactly the knobs for controlling SAP-fines/nanocellulose dewatering without caking.

V2.5 — Hard agglomerates arise from multiple bonds; nonbridging surface hydroxyls are the chemical source.
> "capillary pressure theory... chemical bond theory: nonbridging hydroxyls existing on a nanoparticle surface are the basic sources of hard agglomerates... Me–O–Me group accounts for the formation of agglomerates." (p.714–715)
Interpretation: Hard (irreversible) agglomerates need chemical, not just capillary, reversal — crucial for deciding whether a SAP/nanocellulose agglomerate can be redispersed by shear or is permanently damaged.

V2.6 — Solvent replacement demonstrably shrinks particle size and raises surface area vs direct oven drying.
> "strong capillary pressure pulls the particles into closer contact during oven drying without solvent exchange... more uniform particle size distributions are obtained due to fewer agglomerations" after ethanol replacement; Table 30.4: direct-oven TiO₂ 50–100 nm / 4.88 m²/g vs ethanol-replacement supercritical 10–20 nm / 113.8 m²/g. (p.722–723)
Interpretation: Quantitative proof that the drying route, not just the chemistry, sets final particle size and porosity — the agglomeration-control thesis in numbers.

## 3. Research Method (研究方法)

The chapter is a classified review + comparative case-study synthesis (Wang/Huang/Mujumdar). Method:
- Mechanism modeling: Scherer's three-period evaporation model (p.713) and capillary-pressure theory (Eq. 30.1, p.714); macroscopic vs microscopic cracking models (p.714–715).
- Agglomeration taxonomy: crystal-bridge, capillary-pressure, hydrogen-bond, chemical-bond (Me–O–Me) theories (p.715).
- Method classification: direct / solvent-replacement / modified drying, each with sub-types (p.717–721).
- Comparative evidence: replicated multi-method preparations of TiO₂ (Dong et al., Table 30.4), MgO (Zhang et al., 7 samples, Table 30.7), BaTiO₃, RF gels (Tamon), with TEM/SSA/porosity data.
No hygiene data; the value is the capillary-force framework and the comparative agglomeration data.

## 4. Argumentation (论证逻辑)

- Premise A: Nanoparticles/nanoporous gels must stay dispersed and porous through drying (p.711–712).
- Premise B: Evaporation creates a capillary-pressure peak at the critical point (p.713–714, Eq. 30.1); this is the root of cracking and agglomeration.
- Step: Reduce capillary pressure via σ (solvent exchange / supercritical / freeze), θ (surface modification), or r_p (larger/uniform pores, skeleton reinforcement via aging/DCCA); choose direct vs solvent-replacement vs modified method per product.
- Resolution: Comparative tables show solvent-replacement supercritical ≈ best quality, but cost/time drive interest in modified ambient/subcritical drying; "agglomeration remains a major challenge" (p.725) and inhalation/ingestion safety is a design constraint.
## 5. Role of This Chapter in the Book (在全书中的角色)

Ch.30 is the small-feature / colloidal-force / powder-agglomeration pole of the book, complementing Ch.31 (ceramics: shrinkage/cracking in rigid porous bodies — same capillary-stress family), Ch.33 (fibrous: bound water, inter-/intra-fibre, shrinkage/hornification), and Ch.4 (sorption, pore structure). Its capillary-pressure equation is the quantitative spine that Ch.31's cracking and Ch.33's shrinkage both implicitly use.

## 6. Strengths and Weaknesses (贡献与局限)

Strengths
- Gives the clean capillary-pressure master equation (30.1) with full symbol definitions (p.714).
- Three explicit engineering levers (σ, θ→90°, r_p) to defeat capillary stress (p.714).
- Multiple quantitative comparisons (Tables 30.3–30.7) proving method → particle size / SSA / porosity.
- Honest on agglomeration as unsolved and on inhalation/ingestion safety (p.725).

Weaknesses
- Purely inorganic/ceramic/sol–gel focus (TiO₂, SiO₂, MgO, BaTiO₃); no SAP, cellulose, or polymer-latex examples — hygiene transfer is by analogy.
- Agglomeration "no generally accepted views" (p.715): four competing theories, none complete (capillary theory fails to explain solvent-swap anomalies).
- Supercritical/CO₂ methods are cost/time-heavy; the chapter admits industrialization is immature (p.724–725).
- OCR rendered Eq. (30.1) symbols inconsistently (σ as "s", θ as "u"); verify against print.

## 7. Key Terms (关键术语)

|||
|---|---|
|Nanomaterial|clusters/particles  nm, fibres  nm dia., films  nm thick (p.711)|
|Critical point (drying)|where curved-liquid radius = gel pore size; capillary tension maximal (p.713)|
|Capillary pressure P|P = 2σ cosθ / r_p; major cause of cracking & agglomeration (p.714)|
|Surface tension σ|liquid–vapor interfacial energy; raising it raises P (p.714)|
|Wetting/contact angle θ|changing toward 90° lowers P (surface modification) (p.714)|
|Hard agglomerate|irreversible, often chemical-bond (Me–O–Me) source (p.715)|
|Nonbridging hydroxyl|surface –OH, "basic source of hard agglomerates" (p.715)|
|Solvent replacement|swap water for low-σ organic solvent to cut agglomeration (p.718)|
|Supercritical drying|removes capillary pressure entirely (CO₂ Tc 31°C, Pc 7.29 MPa) (p.717)|
|DCCA|drying-control chemical additives (formamide, glycerol) to strengthen skeleton (p.721)|

## 8. Micro close-reading (微观精读)

8.1 — The capillary-pressure equation (p.714). "Capillary pressure is the major cause leading to cracking of the gel skeletons or agglomeration of nanoparticles during drying: P = 2σ cosθ / r_p." This is the chapter's load-bearing equation. Because P ∝ 1/r_p, halving a pore/particle radius doubles the stress — which is why nanocellulose and SAP fines (sub-micron) agglomerate far more violently than fluff fibres. Every mitigation in the chapter reduces one term: σ (solvent swap), θ (modification), r_p (enlarge/uniform pores).

8.2 — The critical point as a stress peak (p.713). "At the critical point... the radius of curved liquid is equal to the size of the gel pores... capillary tension reaches maximal value, and the gel skeleton... may dilate slightly... various degrees of collapse may appear, micropores vanish." The critical point is where constant-rate ends; it is a mechanical peak, not just a rate change — the moment a pad or gel most risks cracking. This is the same "constant-rate → falling-rate transition" the hygiene reader meets in Ch.33/Ch.4.

8.3 — Why hard agglomerates are permanent (p.715). "chemical bond theory: nonbridging hydroxyls existing on a nanoparticle surface are the basic sources of hard agglomerates... Me–O–Me group accounts for the formation of agglomerates." Distinguishes reversible (capillary/H-bond) from irreversible (covalent/condensation) agglomerates. For SAP/nanocellulose this decides whether redispersion by shear recovers the product or the fines are permanently lost.

8.4 — Solvent replacement in numbers (p.722–723, Table 30.4). "strong capillary pressure pulls the particles into closer contact during oven drying without solvent exchange... CP1 direct oven 50–100 nm / 4.88 m²/g; CP2 ethanol-replacement supercritical 10–20 nm / 113.8 m²/g; CP3 ethanol-replacement oven 20–40 nm / 60.7 m²/g." A single study showing the drying route changes particle size ~5× and surface area ~23× — the clearest quantitative statement that method choice, not just formula, governs nanostructure.

8.5 — Safety close (p.725). "nanoparticles are difficult to collect if emitted in air. The fact that they can be easily inhaled or even ingested by the skin is especially worrisome and must be taken into account in the design and operation of any drying process." Flags inhalation/dermal exposure as a first-order design constraint — directly relevant to nanocellulose and fine SAP-dust handling in a converting plant.

## 9. Concept deep-dive (概念深掘)

9.1 Three-period evaporation model (§30.2.1, p.713–714). Constant-rate: pores liquid-filled, contraction rate = evaporation rate, capillary tension low. Critical point: liquid curvature radius = pore radius, tension maximal. First falling-rate: surface exposed, liquid recedes, flow + vapor diffusion. Second falling-rate: evaporation inside body, gel may dilate/collapse, skeleton compression asymmetric → deformation. Operational: damage concentrates at the critical point and second falling-rate.

9.2 Capillary pressure & mitigation (§30.2.2.1, p.714). Eq. (30.1) P = 2σ cosθ / r_p. Three levers: (a) reduce σ → supercritical / freeze / solvent-replacement; (b) θ → 90° via surface modification; (c) enlarge & uniformize r_p (uneven pores → differential stress → cracking). Microwave also shortens drying and heats evenly.

9.3 Cracking models (§30.2.2.2, p.714–715). Macroscopic: drying stress acts on whole body (explains cracking vs thickness/evaporation-rate, but not why cracking peaks at critical point). Microscopic: asymmetric pores cause local stress; wider pore-size distribution → more cracking. Neither complete.

9.4 Agglomeration theories (§30.2.2.3, p.715). Crystal-bridge (deposited surface hydroxyls crystallize, tighten); capillary-pressure (particles pulled together as walls shrink); hydrogen-bond (NP attach via H-bond, redispersible in water); chemical-bond (nonbridging surface –OH condense to Me–O–Me = hard, irreversible). Most authors attribute to capillary pressure, but solvent-swap anomalies show it is insufficient alone.

9.5 Drying families (§30.3, p.717, 30.3.1–30.3.3). Direct: oven (severe agglomeration, may take ~1 year safe), spray (simple, industrializable; pyrolysis variant), freeze (water expansion separates particles, prevents agglomeration; t-BuOH better than water), microwave (1/10–1/100 time, no gradient), supercritical (Kistler; eliminates capillary pressure; CO₂ Tc 31°C/Pc 7.29 MPa vs water 21.77 MPa; 4 stages), subcritical, direct calcining (particle size ↑ with T: TiO₂ 22.1 nm@450°C → 49.6 nm@900°C, Table 30.3). Solvent-replacement: wash with MeOH/EtOH/BuOH etc. (functional groups replace nonbridging hydroxyls, steric hindrance prevents agglomeration); azeotropic (BuOH most popular); CO₂ replacement. Modified: uniform pores (formamide slows hydrolysis), alter volatilization order (add DMF), surface modification (TMCS → θ→~90°, Table 30.6: ethanol contact angle 30°→78°), skeleton reinforcement (aging, DCCA).

9.6 Selection (§30.4, p.722–725). Quality ranking: solvent-replacement supercritical > solvent-replacement freeze/microwave > azeotropic > direct oven. Agglomeration remains the major challenge; safety (inhalation/ingestion) critical.

## 10. Critique (批判性评估)

- No polymer/SAP/cellulose content — the entire evidence base is oxide/sol–gel; hygiene transfer is analogical, exactly as the brief expects.
- Agglomeration mechanism unsettled (four theories, p.715) — the chapter gives no single predictive model, so the hygiene reader must test which bond type dominates for their powder.
- Capillary equation is isothermal/ideal; it ignores viscoelastic skeleton relaxation and rate-dependent modulus — which matter most for soft hydrogels (SAP) vs rigid silica.
- Industrial immaturity admitted (p.724–725): supercritical/CO₂ routes are slow and costly; the "best" method is not the deployable one at volume.
## 11. Hygiene-Material Relevance & Action Cards (卫材相关性与行动卡)

H11.1 — Use P = 2σ cosθ / r_p to size SAP-fines/nanocellulose agglomeration risk (★★★★★). Action: Treat sub-micron SAP fines and nanocellulose by Eq. (30.1): because r_p is tiny, capillary pressure is enormous at the falling-rate transition — keep σ low (avoid pure-water dewatering where possible) and/or raise θ (hydrophobic treatment) to suppress clumping during flash/pad dewatering.

H11.2 — Redispersibility depends on bond type — test before declaring "reversible" (★★★★). Action: Classify any observed agglomerate as H-bond/capillary (shear-redispersible) vs chemical Me–O–Me / crystal-bridge (permanent, p.715). For nanocellulose/SAP fines, validate redispersibility by mild shear rather than assuming it recovers.

H11.3 — Exchange water for low-surface-tension solvent or use freeze to protect nanostructure (★★★★). Action: Where nanocellulose/CMC gels must keep high surface area, apply solvent-replacement (EtOH) or freeze-drying (water expansion separates particles, p.716) instead of direct oven drying, which collapses pores (Table 30.4 proof).

H11.4 — Surface-modify to θ≈90° to minimize capillary pull (★★★★). Action: Mirror Deshpande/TMCS treatment (θ→~90°, Table 30.6, p.721): hydrophobically treat SAP-fine or nanocellulose surfaces so capillary pressure collapses and ambient-pressure drying yields aerogel-like low-bulk product.

H11.5 — Watch the critical point; it is a mechanical peak, not just a rate change (★★★). Action: In pad/film drying of fine-particulate coatings, expect max stress at the constant→falling-rate transition (p.713); back off flux there to avoid microcracking/collapse of the web.

H11.6 — Engineer dust-exposure controls for fine powders (★★★). Action: Treat SAP fines / nanocellulose as inhalable/dermally-ingestible (p.725): enclose dewatering/handling, collect emissions, and set PPE — the chapter's safety flag applies directly to plant converting.

## 12. Book-Map Quotes (本书脉络引证)

- Ch.4 (moisture/sorption): pore-size & capillary framework (Eq. 30.1) underlies isotherm and pore-structure reasoning.
- Ch.31 (ceramics): capillary-stress cracking in rigid porous bodies is the same P = 2σ cosθ / r_p family.
- Ch.33 (fibrous): bound water, inter-/intra-fibre shrinkage and hornification meet the same capillary-pressure peak.
- Ch.29 (pharmaceutical): spray/ freeze/ solvent drying overlap; colloidal powder agglomeration parallels tablet-excipient handling.


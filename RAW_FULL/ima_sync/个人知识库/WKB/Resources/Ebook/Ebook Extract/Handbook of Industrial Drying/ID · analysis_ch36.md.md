---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_a3c9c752b50bb56f5e0b0db6f314191b001a693ee6c0644e"
source_file: "ID · analysis_ch36.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch36.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch36.md.md

# Chapter 36 — Drying of Wood: Principles and Practices

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 36 (Perre´ & Keey) is the Handbook's definitive mechanistic treatment of wood drying and the upstream material source for fluff pulp. It progresses from wood structure (anatomy, knots, reaction/juvenile wood) → chemical composition (cellulose DP ~10,000, 50–70% crystalline; hemicellulose; lignin as the cementing amorphous polymer; extractives 5–30%) → board-scale physics (free vs bound water, fiber saturation point FSP ≈ 30–32%, differential heat of sorption, anisotropic shrinkage, Darcy/capillary/bound-water diffusion) → drying process (low-temperature convective with constant/falling rate; high-temperature internal overpressure; sapwood vs heartwood divergence) → mechanical aspects (shrinkage-driven stress, memory effect, case-hardening, checking) → kiln scale (lumber quality, design, operation, schedules). For the hygiene reader its value is mechanistic (bound-water diffusion below FSP, anisotropic shrinkage, lignin Tg) plus genuine pulpwood supply-chain relevance: juvenile/reaction wood and within-tree variability govern the feedstock that becomes fluff pulp.

## 2. Key Viewpoints (with verbatim quotes + print pages)

### Viewpoint 1 — Wood is a variable, anisotropic, polymer-composite material

- Page: p.825
- Quote: "Cellulose is a linear polymer with an average degree of polymerization of 10,000. These polymer chains are organized in elementary fibrils that are partly crystalline to the extent of 50 to 70%. … Lignin is often regarded as the cementing agent that binds individual cells together and is insoluble in most solvents."
- Interpretation: Wood = oriented semicrystalline cellulose reinforced in a lignin/hemicellulose amorphous matrix — the same composite picture as Ch33's fibre and the basis for every transport/shrinkage rule below.
### Viewpoint 2 — FSP ~30% bounds free/bound water; heat of sorption collapses to zero there

- Page: p.828
- Quote: "FSP of the wood may be defined as the equilibrium moisture content (EMC) in an environment of 99% relative humidity. This yields a value of 30 to 32% for most commercial species … FSP falls with increasing temperature. For a softwood such as Sitka spruce, FSP falls from about 31% at 25°C to 23% at 100°C."
- Interpretation: The FSP is the master split (free water above, bound below) that Ch33 applied to pulp; here it is quantified per species and shown temperature-dependent — directly relevant to chip/woodchip MC before pulping.
### Viewpoint 3 — Permeability is the dominant anisotropy (1000× to >10⁶×)

- Page: p.832
- Quote: "Wood has dramatic anisotropy ratios: the longitudinal permeability can be 1000 times greater than the transverse permeability for softwoods and more than a million-fold for hardwoods."
- Interpretation: Fluid egress is overwhelmingly longitudinal. This governs drying time and, upstream, the dewatering/pulping behaviour of the log; pit aspiration on drying (p.833, "impossible to avoid … when drying softwoods under normal conditions") locks in low permeability.
### Viewpoint 4 — Shrinkage is hydrogen-bond-driven and anisotropic; it creates drying stress

- Page: p.830
- Quote: "when sorbed water is removed from the cell wall, new hydrogen bonds form between the hydroxyl groups of the molecular chains and reduce the distance between the chains. This variation affects the dimension in a direction normal to the microfibril direction. This fact explains why the longitudinal shrinkage is usually negligible."
- Interpretation: Shrinkage = H-bond re-formation on desorption (the micro-mechanism of hornification). Transverse shrinkage dominates (tangential ≈ 2× radial, Table 36.6), and "Shrinkage is the 'driving' force for drying stress" (p.845).
### Viewpoint 5 — High-temperature drying uses internal overpressure; sapwood and heartwood diverge

- Page: p.841
- Quote: "To reduce the drying time without decreasing the quality … the temperature of the product is above the boiling point of water. Such conditions ensure that an overpressure exists within the material, which implies that a pressure gradient drives the moisture toward the exchange surfaces."
- Interpretation: Above 100°C internal vaporization accelerates drying; but heartwood (permeability ~10⁻¹⁶ m² vs sapwood 10⁻¹² m², Table 36.8) stays wet and develops higher overpressure — a quality/process divergence the kiln operator must manage.
### Viewpoint 6 — Juvenile and reaction wood degrade dried-wood quality (the pulpwood link)

- Page: p.859
- Quote: "The gradual exhaustion of natural forest resources has forced the industries to accept juvenile wood from plantations and second-growth forests. Although juvenile wood is often considered unsatisfactory … High moisture content in sapwood of young trees [→] Higher transport and drying-energy costs; Lower basic density [→] Increased potential for collapse during high-temperature drying."
- Interpretation: Fast-grown plantation feedstock (eucalyptus, radiata pine) carries more juvenile wood, higher shrinkage/warp and lower density — exactly the variability that propagates into pulp yield and uniformity a fluff-pulp buyer ultimately pays for.
## 3. Research Method & Data Sources

Mechanistic review + modeling.

||||||
|---|---|---|---|---|
|Anatomy/composition|Microscopy, tables|Panshin & de Zeeuw; Fengel & Wegener; Walker|Tables 36.1–36.2|Standard wood science|
|Sorption|Isotherms, Kelvin, Clausius–Clapeyron|Skaar (1988); Stamm; Rasmussen/Siau|Fig 36.9–36.10, Eq 36.3–36.4|Experimental fit|
|Transport|Darcy, generalized Darcy, capillary P, bound-water diffusion|Comstock; Spolek & Plumb; Perre´|Eq 36.5–36.17, Fig 36.14–36.16|Model + experiment|
|Drying kinetics|1/2/3-variable models, characteristic curve|Whitaker; Keey et al. (2000); van Meel|Eq 36.22–36.23, Fig 36.46–36.47|Industrial approximation|
|Mechanics|Viscoelastic + mechanosorptive, memory effect|Perre´; Ranta-Maunus; Arrhenius|Eq 36.18–36.21, S1–S4|Simulated, validated vs oak|

## 4. Argumentation Process

- Material — wood is anisotropic polymer composite; knots, reaction/juvenile wood add variability (§36.1).
- Water states — free (lumens) vs bound (cell wall); FSP; sorption hysteresis; heat of sorption (§36.2.1).
- Transport — single-phase Darcy → multiphase generalized Darcy; capillary pressure; bound-water diffusion with strong MC dependence (§36.2.2).
- Process — low-T convective (constant then falling rate); high-T internal overpressure; sapwood/heartwood divergence (§36.2.3).
- Mechanics — shrinkage drives stress; viscoelastic + mechanosorptive creep; memory effect; stress reversal / case-hardening; checking (§36.2.4).
- Quality — duration vs quality levers; Rules 1–3 (high RH, high T, high velocity); contradictory trade-offs (§36.2.5).
- Kiln — lumber quality (gross/intrinsic/sawing), design (airflow, evaporation, characteristic curve), operation, schedules, less-common methods (§36.3).
## 5. Role in the Book

Ch36 is the upstream "material source" anchor: it supplies the wood that Ch33/Ch35 turn into fibres and pulp. It is the most mechanistic chapter in the assignment — the only one deriving Darcy, capillary-pressure and bound-water-diffusion equations and a full viscoelastic/mechanosorptive stress formulation. It complements Ch33 (which treats fibres hygroscopically) and Ch35 (which treats the pulp/paper web industrially) by explaining why the raw material is so variable and how that variability is baked in at the tree level.

## 6. Strengths & Weaknesses

✅ Strengths: Genuine mechanistic depth — generalized Darcy with relative permeability, Kelvin/capillary-pressure functions, bound-water diffusivity correlation, and a rigorous drying-stress/memory-effect formulation. Excellent quantitative tables (composition, shrinkage, permeability anisotropy, green MC, juvenile/reaction-wood defects). Explicit sapwood/heartwood modeling contrast.
⚠️ Limitations/contestable: Focused on solid-wood lumber kiln drying, not on pulping or fluff-pulp feedstock — the hygiene transfer is upstream/indirect. Equations 36.3, 36.14, 36.16 and the S1–S4 tensor set are OCR-degraded (stray symbols); many constants require the print edition. The "memory effect" constitutive model is acknowledged as "very difficult to characterize" (p.847). No SAP, no nonwoven, no fluff-pulp specifics.

## 7. Key Terms / Concepts

- FSP (fiber saturation point): p.828, EMC at 99% RH ≈ 30–32% (most species); falls with temperature.
- Bound vs free water: p.828, free water in lumens (properties ≈ liquid); bound water in cell wall (activity ).
- Sorption hysteresis: p.829, desorption EMC higher than adsorption; ratio 0.75–0.88.
- Differential heat of sorption: p.830, "slightly higher than 1000 kJ kg⁻¹ for oven-dry wood … decreases rapidly … to reach zero … at the FSP."
- Anisotropic shrinkage: p.830, transverse shrinkage dominates; tangential ≈ 2× radial; longitudinal negligible (H-bond re-formation normal to microfibrils).
- Permeability anisotropy: p.832, longitudinal ≫ transverse (1000× softwood, >10⁶× hardwood); pit aspiration locks it in (p.833).
- Bound-water diffusivity: p.837, D_b rises sharply with bound-water content (Eq 36.14, OCR-degraded).
- Drying stress / memory effect: p.845–847, shrinkage drives stress; wood "memory" depends on the time-history of T and MC; stress reversal = case-hardening.
- Characteristic drying curve: p.863, N_v = β f_b (Y_W − Y_G) (Eq 36.22), normalized rate vs mean free MC.
- Juvenile / reaction wood: p.827–828, 859; fast-growth plantation wood carries more, degrading quality.
## 8. Micro close-reading (ONE key paragraph)

p.830 (Shrinkage mechanism — the hornification micro-mechanism):
> "In trees, the cell walls of wood are in a fully swollen condition. However, when sorbed water is removed from the cell wall, new hydrogen bonds form between the hydroxyl groups of the molecular chains and reduce the distance between the chains. This variation affects the dimension in a direction normal to the microfibril direction. This fact explains why the longitudinal shrinkage is usually negligible. In the transverse directions, the dimensional variations plotted against bound water content are very close to a straight line."

Sentence-by-sentence: (1) Baseline — green cell walls are fully swollen (bound water present). (2) Mechanism — desorption removes bound water and new H-bonds form between hydroxyls, pulling chains closer (the micro-event of hornification). (3) Anisotropy — shrinkage is normal to the microfibril (crystalline) direction, so longitudinal change ≈ 0. (4) Macroscopic law — transverse shrinkage is quasi-linear in bound-water content.
💡 Standout line: "new hydrogen bonds form between the hydroxyl groups of the molecular chains" — the molecular origin of irreversible shrinkage/hornification, identical in wood and in the redried pulp of Ch33/Ch35.

## 9. Concept deep-dive

Bound-water diffusion below FSP (the rate-limiting step). Eq 36.14 gives D_b increasing with bound-water content; the authors state bound-water diffusion "is always easier for higher bound-water contents" and that "diffusion becomes very slow when the bound-water content decreases toward zero" (p.854). This is the falling-rate mechanism for any cellulosic web: once below FSP, drying is governed by slow bound-water (activated) diffusion — the same regime Ch33 called "sorptive (activated) diffusion." For pulp chips, the FSP (~30%) is the MC below which thermal drying becomes rate-limited and energy-expensive.

The FSP / green-MC baseline for feedstock. Table 36.3 (p.828): green softwood sapwood 150–200%, heartwood 40–80%; hardwood sapwood 80–120%, heartwood 60–100% (dry basis). This is the water a pulp mill must remove before/while pulping — directly setting transport and energy cost (cf. Ch35's "drying is the costliest step" and juvenile wood's "higher transport and drying-energy costs," p.859).

Anisotropic shrinkage = oriented semicrystalline composite. Longitudinal shrinkage negligible because microfibrils (50–70% crystalline, p.825) resist; transverse shrinkage is H-bond-driven (p.830). Reaction wood exaggerates it: compression wood longitudinal shrinkage is "order of magnitude greater" and tension wood "~fivefold greater" than normal (Table 36.10, p.859). For a pulp buyer this means reaction-wood-rich feedstock yields more warp-prone, variable fibre.

Drying stress, memory effect and case-hardening. Shrinkage → surface tensile / core compressive stress (Fig 36.29); over time viscoelastic + mechanosorptive creep cause stress reversal (case-hardening, p.846) and, if internal tensile stress is too high, internal checking (p.845). The memory strain tensor "depends not only on the temperature and moisture content values but also on their variations in time" (p.847) — a hysteresis of mechanical state. This is the solid-wood analogue of the permanent set / hornification of Ch33.

Pulpwood supply-chain variability. Juvenile wood (plantations), reaction wood, knots, wetwood and within-tree density gradients (Fig 36.42–36.43; Tables 36.9–36.10) make the raw material "extremely difficult to characterize precisely" (p.822). Fast-grown feedstock → higher MC, lower density, more warp/collapse risk and more extractives — all propagating into pulp uniformity, yield and refining energy.

## 10. Academic critique & open questions

- Equations 36.3, 36.14, 36.16 and the S1–S4 tensor formulation are OCR-degraded; constants (e.g., the bound-water diffusivity pre-exponential and activation terms) need the print edition before reuse.
- The memory-effect constitutive law is admittedly "very difficult to characterize" (p.847); industrial schedules still rely on empirical Rules 1–3 rather than the full 3-variable model.
- No link to pulping or fluff-pulp; the hygiene transfer is entirely upstream (feedstock quality).
- Open question 1: Can the FSP (~30%) and bound-water diffusivity of Ch36 be used to predict the redry-energy penalty (hornification) of a market pulp, bridging to Ch35's flash-drying clause?
- Open question 2: Does juvenile/reaction-wood fraction in the pulpwood mix leave a measurable fingerprint in the delivered fluff pulp (refining energy, bulk, knot content) that a buyer could specify?

## 11. Hygiene-material relevance & action cards

Overall relevance: ★★★☆☆ (mechanistic value high; direct hygiene relevance is upstream/indirect).

Action Card H36-1 — Specify pulpwood feedstock mix, not just pulp specs. Insight: p.859 juvenile wood from plantations carries "higher transport and drying-energy costs" and "increased potential for collapse"; p.822 wood is "extremely difficult to characterize precisely." Action: When qualifying a fluff-pulp supplier, ask the fibre source (plantation vs old-growth, species, rotation age) and request data on juvenile-wood fraction; treat high-juvenile feedstock as a variability/uniformity risk. → 卫材相关性★★★★☆｜Feedstock variability propagates into pulp yield, bulk and refining energy you pay for.

Action Card H36-2 — Use FSP/green-MC to audit incoming chip and pulp MC. Insight: p.828 FSP ≈ 30–32%; Table 36.3 green MC 150–200% (softwood sapwood) must be removed before/at pulping. Action: Benchmark supplier chip/pulp MC against FSP and species green-MC tables; reject lots whose MC implies excessive evaporative energy or incomplete drying. → 卫材相关性★★★★☆｜Directly sizes the dewatering/drying energy embedded in your pulp cost.

Action Card H36-3 — Watch reaction-wood / knot indicators as quality proxies. Insight: p.859 Table 36.10 compression/tension wood = higher density, much greater longitudinal shrinkage, warp/collapse; p.858 large knots "treble the level of board rejection for unacceptable knot checks." Action: Request knot/shive and dirt content; correlate with upstream reaction-wood presence as a predictor of pad defects and refining load. → 卫材相关性★★★☆☆｜Knots/shives are the visible tail of reaction-wood variability.

Action Card H36-4 — Recognize H-bond hornification as the universal micro-mechanism. Insight: p.830 "new hydrogen bonds form between the hydroxyl groups … reduce the distance between the chains" on desorption; Ch33/Ch35 redry damage is the same event. Action: Unify your supplier-audit language: every redry/overdry = H-bond re-locking = lost swellability; apply Ch35's defibration-energy KPI. → 卫材相关性★★★★☆｜Gives a single molecular explanation across wood, pulp and web.

Action Card H36-5 — Expect permeability-driven dewatering limits. Insight: p.832 permeability anisotropy 1000×–10⁶×; p.833 pit aspiration locks low permeability on drying softwoods. Action: Anticipate that high-extractive/heartwood-rich feedstock dewaters and refined-pulps more slowly; factor into supplier capacity and lead-time. → 卫材相关性★★★☆☆｜Explains supplier throughput ceilings.

Action Card H36-6 — Apply the high-RH / high-T / high-velocity drying rules to any cellulosic drying you control. Insight: p.855 Rules 1–3 (high relative humidity to lower MC gradient; high temperature to accelerate internal transfer + viscoelastic creep; high air velocity for stack uniformity). Action: When specifying or auditing a converting/redry line, use these three levers as a checklist for fast-yet-good drying. → 卫材相关性★★★☆☆｜Portable rules for any thermal drying of cellulose.

## 12. Book-Map Quotes (Top representative quotes)

"Cellulose is a linear polymer with an average degree of polymerization of 10,000. These polymer chains are organized in elementary fibrils that are partly crystalline to the extent of 50 to 70%." — p.825 — the polymer-composite substrate of all fibre behaviour.
"when sorbed water is removed from the cell wall, new hydrogen bonds form between the hydroxyl groups of the molecular chains and reduce the distance between the chains." — p.830 — the molecular origin of hornification/shrinkage.
"the temperature of the product is above the boiling point of water. Such conditions ensure that an overpressure exists within the material." — p.841 — the high-T drying acceleration principle.

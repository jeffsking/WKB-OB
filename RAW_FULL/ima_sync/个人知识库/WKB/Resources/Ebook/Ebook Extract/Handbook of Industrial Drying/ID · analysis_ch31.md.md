---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_4a84ede7baaa76f774baa504ee8ac508001a693ee6c0644e"
source_file: "ID · analysis_ch31.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch31.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch31.md.md

# Chapter 31 — Drying of Ceramics

## 1. Chapter Overview (范围、对象与定位)

Chapter 31 (Yoshinori Itaya, Shigekatsu Mori, and Masanobu Hasatani) treats drying of molded ceramics — a rigid porous body whose shape must be preserved through drying, where the dominant failure modes are shrinkage, cracking, warping, sagging, and internal stress. The chapter's logic: ceramic drying "is usually carried out slowly in order to avoid undesirable cracks and deformations" (p.727); it is bottlenecked by four difficulties (limited initial rate, shrinkage-induced failure, mold-design prediction, nonuniform drying). The body then builds the suction-potential taxonomy (capillary vs osmotic), the shrinkage mechanism (water-film thickness between submicron particles, osmotic suction), the moisture-movement model (liquid/vapor diffusion, Darcy, effective diffusivity, full heat/mass-balance and constant/falling-rate design equations), the dryer families (tunnel, band, batch, IR, microwave, electric-current), and the failure/deformation mechanics (viscoelastic/plastic response, Biot/Lewis numbers, tensile-stress peaks from fast surface dry-up). For the hygiene reader this is a ★★★★ chapter: it is the book's clearest exposition of constant-rate→falling-rate transition, capillary/osmotic shrinkage stress, and case-hardening/cracking in a rigid porous sheet — the exact mechanistic family behind web cracking and case hardening in nonwovens/tissue.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.727–p.740 (PDF p.748–761).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — Ceramic drying is deliberately slow to avoid cracks and deformation.
> "the production processes still rely on old methods... drying is usually carried out slowly in order to avoid undesirable cracks and deformations. The reason is often attributed to the fact that ceramic drying involves maintaining a molded configuration." (p.727)
Interpretation: The "dry slow to hold shape" rule is the same constraint a nonwoven/tissue line faces to avoid web curl and crack — rate must be governed by shape retention, not throughput alone.

V2.2 — Four difficulties define ceramic-drying R&D; rate must be limited at the start.
> "(1) the rise in the drying rate must be naturally limited because the faster rate in the beginning of drying results in rapid attainment of the critical moisture content and then the remarkable reduction of the rate in the falling rate period; (2) failures and irregular deformation may be generated due to drying shrinkage and internal stress it induces; (3) molding must be designed with predicting the deformation; (4) uniform drying is difficult..." (p.728)
Interpretation: Point (1) is the constant-rate → falling-rate cap and point (2) the cracking source — the twin mechanisms of case hardening (fast surface set, interior wet).

V2.3 — Shrinkage is the central quality variable and couples to failure.
> "Shrinkage during drying is one of the most important factors for the quality control of molded products. It is not only related to the deformation and the generation of crack, warp, and sagging but also influences the drying process itself." (p.730)
Interpretation: Shrinkage is not cosmetic — it drives crack/warp/sag and feeds back on the process; directly transferable to web dimensional stability and curl.

V2.4 — Submicron particles shrink by osmotic (not capillary) suction; capillary dominates only >50 µm.
> "shrinkage due to drying generally arises particularly for materials including water by the osmotic suction potential within their internal voids as clay. while the capillary suction potential is affected by the capillary force in the materials consisting of particles larger than 50-µm order, the osmotic suction potential is brought about owing to an electrochemical effect between the water and the surface of particles smaller than micrometers or submicron order." (p.730)
Interpretation: This particle-size threshold is decisive for hygiene: cellulose/nanocellulose fibres are submicron, so their shrinkage is osmotic (double-layer/electrochemical), exactly as in clay — not the capillary mechanism of coarse sand.

V2.5 — Fast surface dry-up over a wet interior produces failure; this is the case-hardening mechanism.
> "If the drying of molded clay is conducted too quickly, it may result in rapid surface dry-up while keeping a wet state in the inside. A fall in the fast-drying rate often causes the failure or the generation of deformation. These phenomena appear during the low moisture-migration rate in the clay." (p.739)
Interpretation: Verbatim description of case hardening: a dry, stressed skin over a wet core. The remedy (raise internal moisture migration via auxiliary drying) is the design lever.

V2.6 — Higher Biot number raises stress; higher internal-diffusion (1/Le) relieves it.
> "Although a higher Bi results in remarkably stronger stress, the stress falls down with a larger 1/Le. Hence, heat-transfer enhancement in the dryer and uniform drying are not possible during ceramic drying unless the moisture-migration rate in the clay is actively or passively enhanced." (p.839)
Interpretation: The dimensionless design rule: push internal moisture mobility (not just external h) to avoid tensile-stress cracking — the quantitative basis for through-air/suction synergy in webs.

## 3. Research Method (研究方法)

The chapter is a mechanistic review + mathematical-modeling synthesis (Itaya/Mori/Hasatani). Method:
- Suction-potential taxonomy: capillary vs osmotic suction as driving forces; electrochemical (double-layer) origin for submicron particles (p.730–731).
- Shrinkage characterization: water-film thickness vs pressure (Norton & Johnson), osmotic-suction vs moisture curves (Newitt, Ohtani), shrinkage curves (Norton, Macey, Kamei & Toei) (p.731–732).
- Transport modeling: liquid + vapor diffusion with effective diffusivity D (Eq. 31.1–31.2, Carman k=5), multidimensional conservation equations (31.3–31.4), Darcy's law (31.8), pressure diffusivity D_p (31.9–31.10), capillary pressure from interfacial energies (p.732–733).
- Design equations: heat/mass balance (31.12–31.15), constant-rate zone length (31.16–31.22, Lewis relation 31.22), falling-rate zone (31.23–31.28), total length Z = z_c + z_d (31.29), drying time (31.30) (p.734–735).
- Failure mechanics: viscoelastic/plastic clay response; Biot/Lewis dimensionless analysis of max tensile stress (Fig. 31.14) (p.739).
No hygiene data; value is the shrinkage-stress and constant/falling-rate framework.

## 4. Argumentation (论证逻辑)

- Premise A: Molded ceramics must keep configuration; drying too fast → cracks/deformation (p.727–728).
- Premise B: Shrinkage is driven by loss of inter-particle water film under osmotic (submicron) or capillary (>50 µm) suction; volume lost = water removed until particles contact, then air enters (p.730–731).
- Step: Model moisture movement (liquid diffusion dominates to ~20–30% db; then vapor), set external h/m and internal D_p, size dryer by constant+falling-rate zones, choose IR/microwave/electric for internal or selective heating.
- Resolution: Failure is a stress problem governed by Bi (external heating rate) vs 1/Le (internal diffusion); relieve by enhancing moisture migration, not just external flux (p.739). The argument is candid that "there are few systematic investigations on the quality control of ceramics during drying" (p.740).
## 5. Role of This Chapter in the Book (在全书中的角色)

Ch.31 is the rigid-porous-body shrinkage/cracking reference — the constant/falling-rate + internal-stress family that Ch.30 (capillary cracking of gels), Ch.33 (fibrous shrinkage/hornification), and Ch.4 (moisture potential) all draw on. It supplies the mechanical (Biot/Lewis, tensile-stress) layer that the food/fibre chapters treat only phenomenologically.

## 6. Strengths and Weaknesses (贡献与局限)

Strengths
- Explicit constant-rate→falling-rate cap and its link to critical moisture (p.728).
- Particle-size threshold for osmotic vs capillary shrinkage (submicron = osmotic), with double-layer rationale (p.730).
- Full design equations (31.3–31.30) and dimensionless failure analysis (Bi/Le, Fig. 31.14).
- Honest that fast surface dry-up over wet interior = failure — the case-hardening definition in plain words (p.739).

Weaknesses
- Pure ceramic/clay focus; no fibre, paper, or nonwoven example — hygiene transfer is mechanistic analogy.
- Equations (31.1–31.10) are notation-dense with OCR garbling (e.g., "«" for ε, "tand" for tan δ); verify against print before reuse.
- Concludes "few systematic investigations on quality control during drying" (p.740) — the chapter is descriptive, not a validated control method.
- IR/microwave efficiency data are ceramic-specific; relevance to webs is by analogy.

## 7. Key Terms (关键术语)

|||
|---|---|
|Molded configuration|shape that must be preserved; drying done slowly to avoid cracks (p.727)|
|Critical moisture content|point where falling-rate reduction becomes "remarkable" (p.728)|
|Shrinkage|central QC factor; drives crack/warp/sagging (p.730)|
|Suction potential|capillary (coarse) + osmotic (submicron) driving force for moisture movement (p.730)|
|Osmotic suction potential|electrochemical double-layer effect for particles  µm; ∝ exponential of moisture (p.730–731)|
|Water film thickness|shrinks with osmotic suction; particles approach as water removed (p.731)|
|Effective diffusivity D|D = a K_g² r_v³ exp(K_w w)/… (Carman k=5) (p.732)|
|Biot number Bi|∝ heating rate; higher Bi → stronger tensile stress (p.839)|
|Lewis number Le|1/Le ∝ internal moisture diffusion; higher → lower stress (p.839)|
|Case-hardening (implied)|fast surface dry-up over wet interior → failure (p.739)|

## 8. Micro close-reading (微观精读)

8.1 — The four difficulties (p.728). "(1) the rise in the drying rate must be naturally limited because the faster rate in the beginning... results in rapid attainment of the critical moisture content and then the remarkable reduction of the rate in the falling rate period; (2) failures and irregular deformation may be generated due to drying shrinkage and internal stress it induces..." This is the design constraint in one paragraph: you cannot simply crank flux because the constant-rate window is short and the falling-rate regime punishes over-fast starts with shrinkage stress. Verbatim case-hardening logic for webs.

8.2 — Osmotic suction in submicron particles (p.730). "the osmotic suction potential is brought about owing to an electrochemical effect between the water and the surface of particles smaller than micrometers or submicron order." The particle-size cutoff ( µm) is the key: coarse granular beds shrink by capillarity, but clay — and by analogy cellulose/nanocellulose fibres — shrink by osmotic (double-layer) suction. This reframes fibre-web shrinkage as an electrochemically driven, not merely capillary, phenomenon.

8.3 — Shrinkage volume equals removed water until contact (p.731). "If all the clay particles are separated from one another by water films... the volume of the shrinkage may be equal to the volume of the removed water until particles contact with the neighbor particles and the removed water begins to be replaced in the void by air." Gives the geometric limit of reversible shrinkage (water-film collapse) and the onset of irreversible structure (air entry) — the analogue of fibre hornification at the point where pores empty.

8.4 — Case-hardening defined verbatim (p.739). "If the drying of molded clay is conducted too quickly, it may result in rapid surface dry-up while keeping a wet state in the inside. A fall in the fast-drying rate often causes the failure or the generation of deformation." This is the single cleanest statement of case hardening in the book — a dry, stressed skin over a wet core — and the chapter's strongest transfer to nonwoven/tissue web defects.

8.5 — Biot/Lewis relief rule (p.839). "Although a higher Bi results in remarkably stronger stress, the stress falls down with a larger 1/Le... heat-transfer enhancement in the dryer and uniform drying are not possible... unless the moisture-migration rate in the clay is actively or passively enhanced." The design conclusion: to avoid cracking, raise internal moisture mobility (through-air, steam, suction) rather than just external h — the quantitative justification for the impingement+suction synergy in Ch.15.

## 9. Concept deep-dive (概念深掘)

9.1 Suction-potential taxonomy (§31.3, p.730). Water held by: suction potential (granular beds: sand, powder, clay, brick), absorption potential (activated alumina/carbon), chemical bond (organic). Of suction, capillary (particles >50 µm) vs osmotic (submicron, electrochemical double-layer). Gradient of potential = moisture-movement driving force. Operational: submicron fibres → osmotic shrinkage.

9.2 Shrinkage mechanism (§31.3, p.730–732). Clay particle surface negatively charged (cation dissociation); H⁺ gathers near surface (Fig. 31.2). Water film between particles thins as osmotic suction pulls them together; volume lost = water removed until particles touch, then air enters (Fig. 31.4). Shrinkage curves (Fig. 31.5) clay-specific; orientation (Williamson, Cox) gives anisotropic shrinkage (perpendicular > parallel).

9.3 Moisture movement (§31.4, p.732–733). Liquid diffusion dominates to ~20% db (stoneware) / 30% (80% Kibushi + 20% feldspar); then vapor. Effective diffusivity D = a·K_g²·r_v³·exp(K_w·w)/… (Carman k=5; a=2.02×10¹¹ Pa, K=24.9 kg-solid/kg-water). Multidimensional conservation (31.3–31.4); Darcy (31.8); pressure diffusivity D_p = k_s/μ (31.9). Capillary pressure from interfacial energies + wetting angle + pore radii.

9.4 Dryer design (§31.5, p.733–735). Heat/mass balance (31.12–31.15). Constant-rate zone length via R_c = k_H(H_s−H) = (h/c_p)(T_g−T_s)/λ (31.19–31.22, Lewis relation k_H≈h/c_p). Falling-rate zone with R_d = R_c·(w−w_e)/(w_c−w_e) (31.26); total Z = z_c+z_d (31.29); t_d = m_d Z/(a F_d0) (31.30). Hot-air 370–470 K; log-mean ΔT 30–70 K; ha 230–350 W/(K·m³).

9.5 Dryer families (§31.6, p.737–739). Tunnel (long residence, multiway flow); band (cross-flow, ha 45–95 parallel); batch (trays, 370–420 K, ha 230–350). IR: surface T > wet-bulb enhances rate but "rapid drying rate may result in failure due to shrinkage"; IR+convective in falling rate effective; efficiency open 25–35% / tunnel 45–50% / closed 50–65% (Table 31.2). Microwave (2450/915 MHz): internal heating, P = 5×10¹⁰ ε_r f E² tanδ (31.34), half-power depth D (31.35); internal T may exceed surface → explosive vapor expansion → control power; uniform honeycomb drying via profile control. Electric-current (100–400 V): selective internal heating inhibits hood cracking in insulators.

9.6 Failure mechanics (§31.7, p.739–740). Wet clay = viscoelastic/plastic, moisture-dependent. Strain–stress analysis needed. Biot Bi (heating rate) and Lewis Le (internal diffusion). Higher Bi → stronger stress; higher 1/Le → relief. Fast surface dry-up over wet interior = failure (Fig. 31.14, 60×60×24 mm slab). Conclusions: drying must be careful; few systematic QC studies exist.

## 10. Critique (批判性评估)

- Ceramic-only evidence. All data (china clay, Kibushi, feldspar, honeycomb insulators) are inorganic; fibre/paper transfer is mechanistic, as the brief intends.
- OCR/notation damage in Eqs. 31.1–31.10 and 31.34 ("«", "tand") — symbol set must be re-derived from print before any quantitative reuse.
- Descriptive failure control. The Bi/Le analysis is diagnostic, not prescriptive; the chapter admits no validated QC method (p.740).
- No energy benchmark beyond IR efficiency table — unlike Ch.15/Ch.28, no kJ/kg anchor for the hygiene reader.
## 11. Hygiene-Material Relevance & Action Cards (卫材相关性与行动卡)

H11.1 — Cap the initial drying rate to protect web shape (★★★★). Action: Honor difficulty (1) (p.728): don't over-drive flux at line start; the constant-rate window is short and over-fast starts cause falling-rate stress — set impingement/through-air ramp so the nonwoven/tissue web doesn't curl or crack.

H11.2 — Treat submicron fibre shrinkage as osmotic, not capillary (★★★★★). Action: For cellulose/nanocellulose mats (fibres  µm), use the osmotic-suction model (p.730): shrinkage is double-layer/electrochemical, so manage it via electrolyte/charge and drying-rate, not just pore-capillary thinking.

H11.3 — Avoid case hardening: no fast surface dry-up over a wet core (★★★★★). Action: Implement the verbatim rule (p.739): prevent rapid surface set while interior stays wet; if surface dries first, back off flux and switch to gentler/falling-rate conditions to avoid crack/warp.

H11.4 — Relieve stress by raising internal moisture mobility, not just h (★★★★). Action: Apply the Bi/Le rule (p.839): add through-air/suction/steam to boost internal 1/Le (moisture migration) rather than only increasing external heat-transfer — the justification for impingement+suction synergy on heat-sensitive webs.

H11.5 — Use IR in the falling-rate period only, with power control (★★★). Action: Mirror ceramic IR practice (p.737): apply IR/convective boost in the falling-rate period for rate without case hardening; control power so surface doesn't over-dry — relevant to wipe coating cure.

H11.6 — Expect anisotropic shrinkage from fibre orientation (★★★). Action: Note Williamson/Cox finding that shrinkage is greater perpendicular than parallel to particle orientation (p.732); for oriented nonwoven webs, anticipate MD/CD dimensional differences and design mold/draw accordingly.

## 12. Book-Map Quotes (本书脉络引证)

- Ch.4 (moisture properties): suction-potential / capillary-osmotic driving-force language (p.730) is the isotherm/potential basis.
- Ch.15 (impingement): case-hardening/cracking from fast flux (p.384) is the nonwoven instantiation of Ch.31's surface dry-up failure (p.739).
- Ch.30 (nanosize): capillary-pressure cracking of gels shares the P = 2σ cosθ / r_p family with Ch.31's capillary suction.
- Ch.33 (fibrous): submicron osmotic shrinkage and hornification are the fibre-level embodiment of Ch.31's shrinkage/stress mechanism.


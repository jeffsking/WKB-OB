---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_91c4b5b69fb3bd0eede011831e65d83a001a693ee6c0644e"
source_file: "ID · analysis_ch08.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch08.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch08.md.md

# Chapter 8 — Fluidized Bed Dryers

## 1. Chapter Overview

Chapter 8 (Law & Mujumdar) is the particulate-solids convective chapter and, for the hygiene reader, the single most process-relevant unit in the assignment: it is the drying/agglomeration/granulation technology that post-treats free-flowing superabsorbent polymer granules. The chapter opens with the fluidization principle (minimum fluidization velocity u_mf, dense phase + freeboard, elutriation, Geldart powder classes A/B/C/D), then states advantages/limitations (high heat/mass transfer, low maintenance, but attrition and fines entrainment), then quantifies heat transfer (single-particle h_p 1–700 W/(m²K) yet system rates enormous due to 3,000–45,000 m²/m³ interfacial area), then builds five drying model families (diffusion, empirical, kinetic, single-phase, two-phase), then examines operating parameters, then surveys ~15 dryer variants (batch, well-mixed, plug-flow, multistage, hybrid, pulsating, immersed-tube, vibrated, agitated, inert-solids, spouted, recirculating, jetting, baffled, superheated-steam, fluidized-bed freeze, heat-pump), then closes with a design procedure and a worked sample. Two statements make the chapter decisive for SAP: (i) "spray drying alone is not energy efficient to remove all … internal moisture. Fluidized bed drying can be incorporated as the second-stage drying" (p.175) — exactly the industrial SAP route — and (ii) superheated-steam FBD is reported for "paper and pulp" (p.189), i.e. fluff-pulp drying.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

## 2. Key Viewpoints

### Viewpoint 1 — Fluidized beds process polymers, resins and healthcare products.

- Page: p.171
- Quote: > "Fluidized bed dryers (FBD) are used extensively for the drying of wet particulate and granular materials that can be fluidized … They are commonly used in processing many products such as chemicals … polymer and resins … healthcare products … detergents and surface-active agents, fertilizers …"
- Interpretation: The chapter's own product list puts SAP (a polymer/resin and a healthcare product) squarely in the FBD feed class. Crosslinked sodium-polyacrylate granules are exactly the free-flowing granular solid this technology post-dries and agglomerates.
### Viewpoint 2 — Wet feed fluidizes poorly; only the top layer lifts initially.

- Page: p.173
- Quote: > "Particles with high initial moisture content require a higher minimum fluidization velocity than similar bed of dry particles. Due to dominant cohesive forces exerted by wetted surfaces, only the top layer of the bed of solids is fluidized. The bottom layers may remain stationary during the initial stage of drying when the solids are quite wet."
- Interpretation: A freshly spray-formed, still-wet SAP granule bed behaves as a sticky, cohesive mass (Geldart C-like) until surface moisture is gone. Design must either pre-dry the feed (flash stage) or use mechanically assisted/vibrated FBD — directly relevant to SAP post-treatment.
### Viewpoint 3 — Enormous interfacial area gives near-isothermal, very fast heat transfer.

- Page: p.176
- Quote: > "The value of heat transfer coefficient of a single particle in a fluidized bed system is generally not high. It is in the range of 1 to 700 W/(m² K). However, due to the large interfacial surface area, in the order of 3,000 to 45,000 m²/m³, extremely high rates of heat transfer are achieved in this system … In designing fluidized bed dryers, an isothermal condition is often assumed."
- Interpretation: The rate advantage of FBD over a rotary or conveyor dryer for SAP granules comes from this surface-area density, which justifies the isothermal-bed assumption used in the single-phase model (§8.4.4).
### Viewpoint 4 — Spray dryer + fluid bed is the energy-optimal two-stage route for internal moisture.

- Page: p.175
- Quote: > "In most cases, spray drying alone is not energy efficient to remove all moisture content inside the solids. This is because considerable amount of heat and time is needed to remove internal moisture that is trapped inside the solids internal. Fluidized bed drying can be incorporated as the second-stage drying to remove the internal moisture."
- Interpretation: This is the canonical SAP manufacturing description (the prompt notes SAP uses "spray drying … and fluidized-bed post-treatment"). The spray step forms the granule; the fluid bed removes internal (bound) moisture and performs agglomeration/coating cheaply.
### Viewpoint 5 — FBD simultaneously granulates, agglomerates and coats.

- Page: p.175
- Quote: > "Beside drying, fluidized bed has found wide ranges of industrial applications … for mixing, dedusting, granulation, coating, agglomeration, cooling, chemical reactions … In coating, a layer of expensive active agent can be coated on a less expensive substrate, or to add a surface agent on solid particles, which is needed for downstream processing."
- Interpretation: SAP surface treatment (anti-caking, fragrance, skin-friendly coating) can be done in the same fluid bed as post-drying — a unit-operation consolidation the hygiene formulator should exploit.
### Viewpoint 6 — Geldart classification governs which variant you need.

- Page: p.174
- Quote: > "powders can be classified into four groups: group A (aeratable particles, easy-to-fluidize when dry), group B (sandlike particles, easy-to-fluidize when dry), group C (fine and ultrafine particles, difficult-to-fluidize due to dominated cohesive forces between particles), and group D (large and dense particles, poor fluidization)."
- Interpretation: SAP product is a Group-A/B granule with a Group-C fine fraction. The fine cut is cohesive and entrains; the coarse cut is Group D-like. Variant choice (vibrated/agitated for C, baffled/spouted for D) follows directly (Table 8.3, p.181).
### Viewpoint 7 — Ion-exchange resin is the analogue material named in the chapter.

- Page: p.180
- Quote: > "For materials with high mobility of internal moisture such as iron ore, ion-exchange resins, silica gel, most drying takes place close to the distributor plate. Bed height has no effect on its drying rate."
- Interpretation: Ion-exchange resin is a crosslinked polymer bead with internal moisture mobility — the structural twin of SAP. Any FBD data or correlation developed for ion-exchange resin transfers to SAP granule drying (see POP block).
### Viewpoint 8 — Multistage spray-fluidized bed = the SAP reactor.

- Page: p.184
- Quote: > "When solid powders are formed in the spray dryer, these powders still contain some internal moisture. It is costly to use a spray dryer to remove all of the internal moisture. Instead, using a second-stage fluidized bed dryer is more cost-effective."
- Interpretation: The multistage spray-fluidized-bed dryer (Fig 8.13) is precisely the two-stage SAP line: spray form → fluid-bed post-dry/agglomerate → (optionally) fluid-bed cool.
### Viewpoint 9 — Vibrated FBD extends to fragile, heat-sensitive, attrition-prone solids.

- Page: p.185
- Quote: > "application of fluidized bed can be extended to fragile, abrasive, and heat-sensitive materials. The problem of fine particle entrainment is also avoided. For polydisperse powders, low gas velocity fluidizes the fine particles gently whereas vibration keeps the coarse particles in a mobile state."
- Interpretation: SAP granules are friable; attrition creates dust (a packaging/safety hazard). The vibrated FBD is the low-attrition option for the final post-treatment of a fragile superabsorbent.
### Viewpoint 10 — Superheated-steam FBD is used for paper and pulp.

- Page: p.189
- Quote: > "The application of superheated steam fluidized bed dryer has been reported for drying of paper and pulp, wood-based biofuels … sugar beet pulp, and paddy."
- Interpretation: Fluff-pulp (cellulosic) drying is an established FBD application — connects this chapter to the fluff-pulp procurement side of the hygiene reader's remit.
## 3. Research Method & Data Sources

The chapter is a review + design synthesis.
| Paradigm | Method | Data source | Tool | Validity |
|---|---|---|---|---|
| Fluidization fundamentals | Force/voidage regimes, u_mf correlations (Gupta & Sathiyamoorthy [1]) | Geldart [2,3] | Regime map (Fig 8.1–8.2) | u_mf correlations exclude wetness effect (p.173) |
| Heat transfer | h_p = k_g Nu_p/d_p (Eq 8.2), Vreedenberg [7] for immersed tubes | literature correlations | h_p tables (Table 8.2) | valid per Re_p band; radiation negligible °C |
| Drying kinetics | Diffusion (Eq 8.8), empirical (Eq 8.12–8.15), kinetic (Chandran [35]), single/two-phase balances | Zahed, Martinez-Vera, Toomey & Johnstone | PDE/ODE models | "constants … empirical" → require lab test (p.179) |
| Variant selection | Typology (Table 8.3) + selection guide (Fig 8.26) | industrial practice | decision tree | multiple types may give same performance |
| Design | Lab→pilot scale-up (Fig 8.25), residence-time equations (Table 8.4), sample calc | Reay/Baker [79–84] | mass/energy balances (Eq 8.22–8.33) | shallow-bed plug-flow correlation limited to 0.10 m depth (p.192) |

## 4. Argumentation Process

- Premise: FBDs give the highest rates for granular solids because of huge gas–solid area, but they damage friable/cohesive powders and lose fines.
- Step 1: Define fluidization (u_mf, phases, Geldart) so the designer knows if the solid will fluidize at all (§8.1–8.1.x).
- Step 2: Quantify transfer (h_p, isothermal assumption) → justifies modelling the bed as one well-mixed continuum (§8.3–8.4).
- Step 3: Offer a model family from simple (diffusion/empirical) to complex (two-phase bubble/emulsion) — designer picks by data availability (§8.4).
- Step 4: Map operating parameters and the ~15 variants so the right hardware matches the solid (§8.5–8.8).
- Step 5: Give a lab-anchored design procedure and a sample calc (§8.9).
- Conclusion (p.197): FBDs have displaced rotary/conveyor dryers; but "the presence of moisture on particle surface can cause major changes to fluidization quality … most of the available literature is applicable [only] to dry particles" — a candid caveat for wet SAP feed.
## 5. Role in the Book

Chapter 8 is the granular-counterpart to Ch.7 (rotary) and the convective sibling of Ch.9 (drum, conductive). It is the technology chapter most aligned with Ch.10 (spray drying) via the two-stage route, and with Ch.12 (dielectric) via the noted "microwave energy field … in a fluidized or spouted bed" future direction (p.197). For hygiene R&D it is the operative chapter for SAP granule post-treatment, agglomeration, and coating.

## 6. Strengths & Weaknesses

✅ Strengths:
- Directly names polymers/resins, healthcare products, detergents, fertilizers as FBD feeds (p.171) — the SAP/nonwoven-binder feed class.
- Explicit two-stage spray→fluid-bed logic (p.175, p.184) mirroring real SAP manufacture.
- Honest coverage of attrition, elutriation, and wet-feed fluidization breakdown (p.173, p.197).
- Lab-anchored design procedure (Fig 8.25) the hygiene lab can copy.

⚠️ Weaknesses / contestable points:
- All drying constants are "empirical and depend on the type of materials, operating conditions as well as dryer dimensions" (p.179) — no SAP data; the reader must measure k on their own granule.
- u_mf correlations "have limitations … the effect of wetness of the particles is, however, not included" (p.173) — exactly the wet-SAP regime.
- Diffusion model assumes constant D, no shrinkage, negligible temperature gradient (p.177) — violated by a swelling SAP granule; requires the polymer-science correction in the POP block.
- Shallow-bed plug-flow correlation only validated to 0.10 m depth (p.192); deeper SAP beds may have D an order of magnitude larger (p.192).

## 7. Key Terms / Concepts

- Minimum fluidization velocity u_mf (p.172): gas velocity at which the bed weight is fully supported.
- Dense phase / freeboard (lean phase) (p.173): bottom particle-rich zone vs. upper disengaging region.
- Elutriation (p.173): carry-over of fines whose terminal velocity < operating gas velocity; sets TDH.
- Geldart groups A/B/C/D (p.174): fluidizability classes; C = cohesive fines (SAP fine cut), D = large/dense.
- Transport disengagement height (TDH) (p.173): height above which solids hold-up is constant.
- Single-particle h_p (p.176): 1–700 W/(m²K); system rate huge due to area density 3,000–45,000 m²/m³.
- Isothermal-bed assumption (p.176): justified by rapid thermal equilibrium.
- Diffusion model (p.177, Eq 8.8): spherical Fickian kernel for single-particle drying.
- Two-phase model (p.179): bubble (dilute) + emulsion (dense) phases; gas > u_mf flows as bubbles.
- Cut size (p.183): critical size separating elutriated fines from retained coarse — the classifier setting.
- Multistage spray-fluidized bed (p.184): spray form → FBD post-dry/agglomerate → cool.
## 8. Micro close-reading (ONE key paragraph)

The two-stage spray→fluid-bed principle (p.175). Verbatim:
> "In most cases, spray drying alone is not energy efficient to remove all moisture content inside the solids. This is because considerable amount of heat and time is needed to remove internal moisture that is trapped inside the solids internal. Fluidized bed drying can be incorporated as the second-stage drying to remove the internal moisture. This can be followed by a third-stage fluidized bed cooling to avoid the condensation problem during packaging in some applications."
Sentence-by-sentence:
1. "spray drying alone is not energy efficient to remove all moisture content inside the solids" — spray drying is excellent for surface moisture and granule formation but thermodynamically costly for bound water.
2. "considerable amount of heat and time is needed to remove internal moisture that is trapped inside the solids internal" — internal (bound) moisture is the rate-limiting, energy-intensive step.
3. "Fluidized bed drying can be incorporated as the second-stage drying to remove the internal moisture" — the fluid bed, with its huge area density, removes bound water far more cheaply than prolonging the spray.
4. "followed by a third-stage fluidized bed cooling to avoid the condensation problem during packaging" — the same technology cools the granule before bagging.
💡 Standout line: this single paragraph is the industrial SAP process in miniature — spray-form the crosslinked polyacrylate, fluid-bed post-dry the internal moisture, fluid-bed cool — and it is the chapter's strongest hygiene-relevant statement.

## 9. Concept deep-dive

9.1 Fluidization quality of wet SAP feed. u_mf rises with moisture and cohesive forces can freeze the lower bed (p.173). The remedy the chapter offers: pre-remove surface moisture in a flash/cyclone stage, then fluid-bed (p.184, hybrid), or use mechanically assisted/vibrated FBD (p.185, p.187). For a moist SAP granule stream this dictates a two-stage or vibrated design, not a plain bubbling bed.

9.2 Why FBD beats rotary for SAP granules. Single-particle h_p is modest (1–700), but the interfacial area 3,000–45,000 m²/m³ makes the volumetric rate enormous and the bed effectively isothermal (p.176). Contrast Ch.7's Uₐ (W/(m³K)) which depends on flight count and gas rate; FBD's area density is intrinsic to the suspended state. This is why FBD "has replaced some of the conventional dryers, e.g., rotary or conveyor dryers" (p.197).

9.3 Drying model hierarchy. Diffusion model (Eq 8.8, spherical Fick) assumes constant D, isotropic, no shrinkage — a poor fit for a swelling SAP granule whose D is moisture-dependent (cf. Ch.4 polyacrylate anomaly). Empirical exponential (Eq 8.12 (X−X_eq)/(X_ind−X_eq)=e^{−kt}) and the Henderson–Pabis/H-page variants (Eq 8.13–8.15) are fitted to data; the kinetic model (Chandran [35]) splits constant + falling rate. The two-phase model (Eq 8.22–8.27) is the most physical (bubble/emulsion mass & energy balances) but needs K_c, d_bb, Y_bb — properties the SAP lab must measure.

9.4 Operating-parameter physics. Bed height: no effect when internal-moisture mobility is high (ion-exchange resin, silica gel analogue, p.180). Particle size: drying time ∝ d_p² for Group B, weaker for Group A (p.180) — so a tighter SAP PSD dries more uniformly. Gas velocity: dominates surface-moisture removal, negligible once internal resistance controls (p.180). Bed temperature: higher T raises h (via k_g) up to radiative regime (>700°C negligible) (p.176–177, Table 8.2).

9.5 Extended variants for hygiene solids. Vibrated FBD → fragile/heat-sensitive, low attrition, polydisperse-friendly (p.185). Inert-solids FBD → dries pastes/slurries/enzymes by coating inert particles (p.187) — route for SAP slurry or binder solutions. Superheated-steam FBD → paper/pulp, no oxidative damage (p.189). Fluidized-bed freeze dryer → heat-sensitive bio products, 35% heat saving with adsorbent (p.190). Heat-pump FBD → 20–110°C, bio-origin/heat-sensitive (p.192).

9.6 Design procedure (lab-anchored). Fig 8.25: set up lab FBD → determine fluidization characteristics → set u_g, bed depth z, T_g, batch dry → build design curve → estimate residence time t_R → fix A, G_g → check RH/condensation/explosion/hazard. Sample calc (p.194–196): 6000 kg/h, 20→4% db, 125°C, u_g=0.70 m/s, bed 20 cm → t_R=800 s, A=11.11 m², G_g=7.777 kg/s, Y_out=0.0336, T_out≈44.6°C, no condensation. Directly scalable to an SAP line.

## 10. Academic Critique & Open Questions

- The diffusion model's constant-D, no-shrinkage, isothermal-solid assumptions (p.177) are violated by swelling SAP granules; the falling-rate period is governed by the hydrogel's moisture-dependent D (Ch.4) and crosslink-set free volume (POP). A hygiene model must use a swelling/relaxation kernel.
- u_mf correlations exclude wetness (p.173); yet SAP enters the bed wet. The chapter offers work-arounds (pre-dry, vibrate) but no predictive wet-u_mf equation — an open modelling gap.
- "most of the available literature is applicable [to] dry particles" (p.197): the entire transfer-correlation base under-represents the wet, cohesive, swelling SAP regime.
- Open questions: (1) What is u_mf and the attrition rate of a moist crosslinked-polyacrylate granule at 10–30% db? (2) How does SAP crosslink density (a polymerization variable) set granule friability and thus the fines-elutriation cut size?

## 11. Hygiene-Material Relevance & Action Cards

Relevance to diaper/wipe/absorbent-core R&D: ★★★★★ (fluid-bed post-treatment, agglomeration and coating of SAP granules; superheated-steam pulp drying).

ACTION CARD H11.1 — Adopt the two-stage spray→fluid-bed SAP route. Situation: building or auditing an SAP line. Apply: spray-dry to form granules, then fluid-bed for internal moisture (p.175, p.184); add a third fluid-bed cooling stage to prevent package condensation (p.175). Effect: removes bound moisture far more cheaply than prolonging the spray; yields a free-flowing, low-dust granule.

ACTION CARD H11.2 — Choose variant by Geldart cut. Situation: a SAP product has a cohesive fine fraction (Group C) and a denser granule (Group A/B/D). Apply: use vibrated or agitated FBD for the fine/cohesive cut (p.185, p.187); baffled or spouted FBD for the large/dense cut (p.189). Effect: avoids channeling, reduces fines entrainment and attrition dust.

ACTION CARD H11.3 — Exploit in-bed coating/agglomeration. Situation: adding anti-caking, skin-friendly or fragrance layer to SAP. Apply: spray binder/active onto the fluidized bed in the same unit as post-drying (p.175). Effect: one unit performs dry + agglomerate + coat, cutting capex and handling.

ACTION CARD H11.4 — Pre-dry wet feed or vibrate. Situation: moist SAP feed fluidizes poorly (only top layer lifts, p.173). Apply: flash/cyclone pre-remove surface moisture then fluid-bed (p.184), or use vibrated FBD (p.185). Effect: stable fluidization, no stationary wet heel, uniform drying.

ACTION CARD H11.5 — Use superheated-steam FBD for fluff pulp. Situation: drying fluff/cellulosic pulp. Apply: superheated-steam FBD — reported for paper and pulp, no oxidative damage (p.189). Effect: no fire/explosion hazard, pasteurizable, better pulp brightness retention.

## 12. Book-Map Quotes

"Fluidized bed dryers (FBD) are used extensively for the drying of wet particulate and granular materials … polymer and resins … healthcare products" — p.171 — establishes SAP as a canonical FBD feed.
"spray drying alone is not energy efficient to remove all moisture content inside the solids … Fluidized bed drying can be incorporated as the second-stage drying to remove the internal moisture" — p.175 — the industrial SAP two-stage route in one sentence.
"only the top layer of the bed of solids is fluidized. The bottom layers may remain stationary during the initial stage of drying when the solids are quite wet" — p.173 — the wet-SAP fluidization failure mode and its design consequence.
"Fluidized bed dryers have replaced some of the conventional dryers, e.g., rotary or conveyor dryers in many instances" — p.197 — the chapter's verdict on FBD's industrial ascendancy.


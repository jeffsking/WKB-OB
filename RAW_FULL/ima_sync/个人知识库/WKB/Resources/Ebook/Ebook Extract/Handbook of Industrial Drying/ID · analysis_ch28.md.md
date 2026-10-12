---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_a6839fd2af02c83ac958d16299ce8b2c001a693ee6c0644e"
source_file: "ID · analysis_ch28.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch28.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch28.md.md

# Chapter 28 — Osmotic Dehydration of Fruits and Vegetables

## 1. Chapter Overview (范围、对象与定位)

Chapter 28 (Lewicki & Lenart) is the handbook's most physically-fundamental water-removal chapter: it treats osmotic dehydration (OD) — the removal of water from plant tissue immersed in a hypertonic solution — as a countercurrent mass-transfer process across a semipermeable boundary driven by osmotic pressure. Its logic is built on chemical-potential/osmotic-pressure thermodynamics (§28.2.1), plant-cell anatomy as the transport architecture (§28.2.2–28.2.3), and a candid review of why simple Fickian diffusion models only partly capture the process (§28.2.4). The body then covers design (predehydration pretreatment, osmoactive substance, processing parameters, solution management, energy, §28.3) and equipment (immersed/sprayed/solid/reduced-pressure, §28.4) and product characteristics (§28.5). For the hygiene reader this is a ★★★★★ chapter: it is the single most direct bridge to superabsorbent-polymer (SAP) science. The osmotic pressure Π = RT·ln a_w, the semipermeable membrane, and the electrolyte/ion effect on Π are exactly the physics family of SAP swelling/deswelling governed by Flory–Rehner equilibrium and Donnan osmotic pressure in a crosslinked polyelectrolyte network. The "water-out / solute-in" countercurrent flux with osmotic pressure as the driver is the same phenomenon as SAP taking up water against an elastic network resistance.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.663–p.679 (PDF p.684–700; REFERENCES to p.686).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — Osmotic dehydration removes water without a phase change, by crossing a semipermeable boundary. This is the thermodynamic definition of the whole method.
> "Water, on the other hand, is removed by osmosis and the cell sap is concentrated without a phase transition of the solvent. This makes the process favorable from the energetic point of view. The flux of water is much larger than the countercurrent flux of osmoactive substance. For this reason the process is called osmotic dehydration or osmotic dewatering." (p.663)
Interpretation: The water leaves as liquid, not vapour — no latent-heat penalty. This is the same "no phase change" advantage SAP exploits when it absorbs liquid water directly into the network.

V2.2 — Osmotic pressure is the motive power, expressed by the chemical potential of water. The chapter gives the canonical equations.
> "The thermodynamic state of water in solution is characterized by water interactions with solute... This state referred to one mole of the substance is called the chemical potential." (p.664)
> "μ_w = μ⁰_w + R T ln a_w" — Eq. (28.1), where μ_w = chemical potential of water, μ⁰_w = standard-state value, R = gas constant, T = absolute temperature, a_w = water activity (p.664)
> "Π V_w = R T ln a" — Eq. (28.2), osmotic pressure × molar volume of water = RT ln a (p.664)
> "Π = 4.6063×10⁵ · T · ln a_w" — Eq. (28.3) (p.664)
Interpretation: Π is the swelling/driving pressure set by the solvent chemical-potential difference. This is the identical quantity that, inside an SAP, is the swelling pressure of the crosslinked polyelectrolyte network.

V2.3 — Electrolytes generate higher osmotic pressure than nonelectrolytes (ion effect). A direct statement of the ionic contribution to Π.
> "Osmotic pressure is related to molar mass of the solute; the smaller the mass, the higher will be the pressure at the same concentration. Electrolytes show higher osmotic pressure than nonelectrolytes because each ion affects the chemical potential of a solvent." (p.664)
Interpretation: This is the seed of Donnan equilibrium — mobile ions distributed across a charged, semipermeable matrix raise Π. It is precisely why SAP (a固定-charge polyelectrolyte) swells in water but deswells in saline: the fixed –COO⁻ groups plus counterions create a Donnan osmotic pressure that is suppressed by external salt.

V2.4 — High osmotic pressure inhibits microorganisms. A quantitative microbiology threshold.
> "Most bacteria, yeasts, and moulds do not proliferate at P > 12.7 MPa, P > 17.3 MPa, and P > 30.1 MPa, respectively." (p.664)
Interpretation: The same osmotic-pressure number that drives SAP uptake also sets the antimicrobial window of a hypertonic brine — a useful cross-link to preservative-free stabilization.

V2.5 — Plant cell: a semipermeable membrane (plasmalemma) wrapping a pressurized vacuole. The anatomical analogue of an SAP particle.
> "The plasmalemma is a protein–lipid layer... It is 7.5–10 nm thick, permeable to water, and selectively permeable to other substances." (p.665)
> "A solution in a vacuole has an osmotic pressure that pushes protoplasm and plasmalemma toward the cell wall... The difference between the osmotic pressure in the cell and in its surroundings is called the turgor pressure." (p.665)
Interpretation: A water-permeable / solute-impermeable skin around an internal osmotic reservoir — structurally the same role as the crosslinked gel matrix of an SAP granule.

V2.6 — Hypertonic surroundings pull water out; plasmolysis detaches the membrane. The deswelling analogue.
> "A cell placed in a hypertonic solution (osmotic pressure higher than that of the cell) will lose water. The dehydration of a protoplast causes decrease of its volume and, in consequence, detachment of plasmalemma from the cell wall. This process is called plasmolysis." (p.666)
Interpretation: Raising external Π reverses the flux and collapses the internal volume — directly analogous to SAP deswelling under load or in brine.

V2.7 — Countercurrent flux: water-out dominates while osmotic pressure flow acts, then impregnation takes over. The kinetic picture.
> "As long as the mass transfer processes are not strongly dependent on the symplasmic pathway, the water flux will predominate over the osmoactive substance flux. This is due to osmotic pressure flow, which will reduce the countercurrent diffusion of osmoactive substance but it will not strongly affect the diffusive flux of water as the self-diffusion of water in a solution is of the same order of magnitude as that for solute. When plasmolysis occurs... the flux of osmoactive substance will be equal to or will surpass the flux of water." (p.667)
Interpretation: Osmotic-pressure-driven water flux dominates initially; once the boundary is bypassed (plasmolysis/impregnation) solute catches up. For SAP this maps onto the initial fast water uptake (osmotic) vs later ion-exchange/leakage.

V2.8 — The cell membrane (network) is the major resistance to mass transfer; extracellular space limits thick samples. Resistance analogy for SAP elasticity.
> "The models based on the irreversible process thermodynamics show that the cell membrane (plasmalemma) represents the major resistance to mass transfer... When the thickness of the sample increases, the extracellular space may become the limiting factor." (p.669)
Interpretation: The semipermeable boundary is the rate-limiting resistance — exactly as the crosslinked network's elastic modulus is the resistance that caps SAP swelling rate/capacity.

V2.9 — Water-binding forces drop far more under osmotic removal than under convective drying to the same moisture. A unique structural signature.
> "Osmotic dehydration done for 0.5 h led to a sixfold decrease of water-binding forces at the surface of apple in comparison to the raw material. Water removal from the tissue by osmosis shows a much stronger effect on water-binding forces than by the convection drying done to the same final water content." (p.678)
Interpretation: The osmotic route reorganizes the water-binding structure differently — relevant to understanding how an SAP-bonded core "holds" water vs a thermally-dried web.

V2.10 — OD is a pretreatment, not a preservation step; it saves energy vs convection drying. The process economics.
> "osmotic dehydration cannot be treated as a food preservation process per se. It is a pretreatment that removes a certain amount of water from the material; to achieve shelf stability, a further processing of the product is needed." (p.678)
> "Osmotic dehydration is distinctive in that water is removed from the product without undergoing the phase change. It offers a considerable potential for energy saving in comparison with convection drying... convection drying needs some 5 MJ/kg of evaporated water, which is at least twice as much as is needed in osmotic dehydration." (p.674–675)
Interpretation: OD is a front-end dewatering helper (as seen in Ch.27's potato use); its energy advantage comes from skipping the vaporization latent heat — the same reason liquid-water absorption by SAP is "free" of a drying-energy cost.

## 3. Research Method (研究方法)

The chapter is a physical-chemistry review + transport-modeling survey + process-design guide. Method:
- Thermodynamic derivation (§28.2.1): chemical-potential and osmotic-pressure equations (28.1–28.3) as the motive force; relation of Π to solute molar mass and electrolyte ionization.
- Structural anatomy (§28.2.2–28.2.3): plant cell as apoplast/symplast networks; plasmolysis sequence; enumeration of transport pathways (capillary suction, xylem/phloem penetration, cell-wall diffusion, symplasmic movement).
- Modeling critique (§28.2.4): second-Fick's-law pseudo-diffusion, irreversible-process thermodynamics, compartmental / advancing-disturbance-front models; explicit admission that countercurrent water+solute fluxes interacting cannot be captured by simple effective diffusivity.
- Design variables (§28.3): pretreatment (permeability enhancement), osmoactive substance (sucrose/NaCl/glucose), static vs dynamic, temperature/pressure, solution reuse.
- Energy accounting (§28.3.5): itemized energy terms; benchmark 100–2400 kJ/kg removed vs ~5 MJ/kg convection.

No hygiene data; value is the transferable osmotic-pressure framework and its direct analogy to SAP.

## 4. Argumentation (论证逻辑)

- Premise A: Water stability/texture is governed by water activity (a_w), not quantity; lowering a_w stabilizes food (p.663).
- Premise B: A difference in osmotic pressure across a semipermeable boundary is the motive power for mass transfer; Π = RT ln a_w (p.664).
- Step: Immerse tissue in a hypertonic solution → water flows out (osmotic pressure flow), solute partly in; manage by pretreatment (raise permeability), substance choice (sucrose/NaCl), temperature (20–40°C best for water-loss:solids-gain), and dynamic/reduced-pressure operation.
- Resolution: OD is energy-favorable (no phase change) and quality-preserving (less shrinkage, better colour/vitamin retention, p.679) but only a pretreatment; finish with convection/freeze/vacuum drying. The chapter is candid that tissue variability makes the process "still somewhat empirical" (p.669) and that simple diffusion models are inadequate (p.667–668).
The argument is rigorous thermodynamics applied to a messy biological substrate — and the thermodynamics is substrate-independent, which is why it transfers to polymeric SAP systems.
## 5. Role of This Chapter in the Book (在全书中的角色)

Ch.28 sits at the physics core of the handbook's water-removal science, complementing Ch.26 (herbal/tea convective+IR) and Ch.27 (potato, where OD appears only as a brief pretreatment). It is the chapter that actually explains why OD works — osmotic pressure across a semipermeable boundary — and therefore it is the missing-link chapter for the hygiene reader: it supplies the exact physical vocabulary (Π = RT ln a_w, chemical potential, semipermeable membrane, semipermeable boundary, countercurrent flux, ion/electrolyte effect on Π) that describes SAP behaviour. It pairs with the dryer-engineering chapters (Ch.14–18) by showing a non-thermal, phase-change-free dewatering alternative. Substrate note: here the semipermeable boundary is the plasmalemma and the osmotic reservoir is the vacuole; in an SAP the boundary is the crosslinked polyelectrolyte network and the reservoir is the gel phase. The governing equations are identical. No diaper "application" is fabricated; the linkage is mechanistic.

## 6. Strengths and Weaknesses (贡献与局限)

Strengths
- Gives the canonical osmotic-pressure equations (28.1–28.3) and ties Π to solute molar mass and electrolyte ionization (p.664) — directly the SAP/Donnan science.
- Explicitly frames OD as water-out/solute-in countercurrent flux with osmotic pressure as driver (p.667) — the same description as SAP swelling under load.
- Quantifies the energy advantage (no phase change; ~½ to 1/5 of convection drying energy, p.674–675).
- Honest about model limits: Fickian effective diffusivity cannot capture interacting countercurrent fluxes (p.667–668).
- Covers artificial semipermeable membranes (pectin/starch/alginate) that selectively block solute — a literal "engineered semipermeable boundary" (p.670–671).

Weaknesses
- Plant-tissue-specific anatomy (apoplast/symplast, plasmolysis) has no direct analogue in a synthetic SAP granule, though the physics does.
- Numerical process data (sucrose concentrations, 20–40°C optimum, 10 mm max thickness) are food-specific and do not transfer.
- The chapter does not itself invoke polymer science (Flory–Rehner, Donnan) — the linkage to SAP must be made by the reader (supplied in the POP block below).
- "Still somewhat empirical" admission (p.669) — tissue variability blocks a universal predictive model.

## 7. Key Terms (关键术语)

|||
|---|---|
|Water activity a_w|thermodynamic state of water; 0 dry, 1 pure water (p.663)|
|Chemical potential μ_w|μ_w = μ (standard) + RT ln a_w; drives solvent transfer (Eq.28.1)|
|Osmotic pressure Π|Π·V_w = RT·ln a; motive power across semipermeable boundary (Eq.28.2)|
|Semipermeable membrane|permeable to solvent, impermeable to solute (p.664)|
|Plasmalemma|7.5–10 nm protein–lipid layer; water-permeable, selectively solute-permeable (p.665)|
|Turgor pressure|Π(cell) − Π(surroundings); cell rigidity source (p.665)|
|Plasmolysis|hypertonic shrinkage detaching membrane from wall (p.666)|
|Apoplast / symplast|cell-wall continuum / protoplast+plasmodesmata network (p.666)|
|Countercurrent flux|water-out + solute-in simultaneously (Fig.28.6, p.667)|
|Donnan seed|"Electrolytes show higher osmotic pressure... each ion affects chemical potential" (p.664)|
|HTST osmotic|65–90°C, 1–20 min; equivalent to 2 h at 20°C (p.672)|

## 8. Micro close-reading (微观精读)

8.1 — The motive-power equation (p.664). "Π V_w = R T ln a" (Eq.28.2) and "Π = 4.6063×10⁵ · T · ln a_w" (Eq.28.3). Osmotic pressure is not a vague "concentration effect" — it is the solvent chemical-potential difference made explicit. For an SAP this same Π is the swelling pressure of the crosslinked network; Flory–Rehner writes equilibrium swelling as the balance between this mixing/osmotic pressure and the elastic retractive pressure of the network. Ch.28 hands the hygiene engineer the exact driving-force law.

8.2 — The ion/electrolyte statement is the Donnan germ (p.664). "Electrolytes show higher osmotic pressure than nonelectrolytes because each ion affects the chemical potential of a solvent." This is the qualitative statement of Donnan equilibrium: mobile ions distributed across a charged semipermeable boundary raise the osmotic pressure. In SAP, fixed –COO⁻ anionic groups plus their counterions produce exactly this Donnan osmotic pressure — which is why SAP swells enormously in pure water yet collapses in saline (the external ions short-circuit the internal Donnan potential). Ch.28 names the mechanism; polymer physics supplies the math.

8.3 — Plasmolysis = deswelling (p.666). "A cell placed in a hypertonic solution... will lose water... detachment of plasmalemma from the cell wall. This process is called plasmolysis." Reverse the sign of the boundary osmotic-pressure difference and the internal reservoir collapses — the precise mechanical analogue of an SAP granule deswelling when external Π (e.g., from urine/brine/salt) exceeds the network's swelling pressure.

8.4 — Osmotic flow dominates, then impregnation takes over (p.667). "the water flux will predominate over the osmoactive substance flux. This is due to osmotic pressure flow... When plasmolysis occurs... the flux of osmoactive substance will be equal to or will surpass the flux of water." The initial fast, water-selective phase is osmotic-pressure-driven; only after the semipermeable barrier is compromised does solute leak in. For an SAP the parallel is clear: initial fast water uptake (osmotic) is followed by slower ion-exchange/leakage once the gel is saturated.

8.5 — Boundary is the resistance (p.669). "the cell membrane (plasmalemma) represents the major resistance to mass transfer... When the thickness of the sample increases, the extracellular space may become the limiting factor." The semipermeable boundary, not the bulk, sets the rate — exactly as the crosslinked network's elastic modulus is the rate/capacity-limiting resistance in SAP swelling. Raoult-Wack et al. (p.669) even show the membrane is not necessary — diffusive properties of the matrix alone suffice, reinforcing that the network itself is the semipermeable element.

8.6 — Energy: no phase change (p.674–675). "water is removed from the product without undergoing the phase change... convection drying needs some 5 MJ/kg of evaporated water, which is at least twice as much as is needed in osmotic dehydration." Skipping vaporization latent heat is the entire energy story — and it is the same reason a SAP core absorbs liquid urine/water with zero drying-energy cost compared with a thermally re-dried fluff web.

## 9. Concept deep-dive (概念深掘)

9.1 Osmotic-pressure thermodynamics (§28.2.1, p.664). Three equations: (28.1) μ_w = μ⁰_w + RT ln a_w (solvent chemical potential); (28.2) Π·V_w = RT ln a (van't Hoff in activity form); (28.3) Π = 4.6063×10⁵·T·ln a_w. Π rises as a_w falls (more concentrated external solution) and as solute molar mass falls; electrolytes exceed nonelectrolytes because each ion contributes. This is the identical set of relations used in polymer-solution thermodynamics (Flory–Huggins solvent chemical potential) and in SAP swelling-pressure calculations.

9.2 Semipermeable boundary & turgor (§28.2.2, p.665). Plasmalemma = 7.5–10 nm protein–lipid layer, water-permeable, selectively solute-permeable; vacuole holds the osmotic reservoir; turgor pressure = Π(cell) − Π(surroundings). The "pressurized internal reservoir behind a selective skin" is the structural archetype of an SAP gel particle (internal gel phase behind a crosslinked skin).

9.3 Mass-transfer sequence & plasmolysis (§28.2.3, p.666–667). Contact with hypertonic solution triggers: capillary suction fills intercellular spaces → xylem/phloem penetrate with osmoactive substance → cell walls lose water by diffusion+osmotic flow → symplasmic water movement → plasmolysis. The countercurrent water-out/solute-in fluxes (Fig.28.6) interact and cannot be separated into independent effective diffusivities.

9.4 Modeling limits (§28.2.4, p.667–669). Pseudo-diffusion (Hawkes & Flink: normalized solids vs √t → "mass transfer coefficient") works empirically; irreversible-process thermodynamics and compartmental/ADF models capture more; but the chapter concedes Fickian effective diffusivity "cannot be used to predict the contribution of each flux" and that tissue variability keeps the field "somewhat empirical." The honest lesson: countercurrent, interacting fluxes need coupled models — the same caveat applies to SAP uptake under competing salt/load.

9.5 Pretreatment = permeability engineering (§28.3.1, p.669–671). NaOH+ethyl oleate raises skin permeability (tomato, strawberry); CaCl₂ firms texture; high-pressure and electric-field pulses raise water/solute diffusivity "exponentially with electric field strength"; artificial semipermeable membranes (pectin/starch/alginate/low-methoxyl pectin) reduce solute incorporation while keeping water flux. This is literally designing the semipermeable boundary — directly analogous to engineering SAP crosslink density / surface coating to tune uptake rate vs leakage.

9.6 Processing window (§28.3.3, p.671–673). Static (higher resistance) vs dynamic (mixing); rate of motion barely matters once motion exists; centrifugal force → larger water flux / smaller solids gain; reduced/pulsed vacuum improves rate; temperature 30–80°C shortens time but also drives more solute in; best water-loss:solids-gain ratio at 20–40°C; HTST (65–90°C, 1–20 min) gives blanching-like effect. Material thickness should not exceed 10 mm (Lenart & Lewicki). These are the operating-lever analogues for any osmotic/dewatering pre-step.

9.7 Energy accounting (§28.3.5, p.674–675). Itemized: heating (heat loss), mixing/pumping (4.3–17.2 kJ/kg at 20–40°C), dissolution (~1 kJ/kg, negligible), evaporation of surplus (~1.8 MJ/kg evaporated water in the reconcentrator). Total 100–2400 kJ/kg removed vs ~5 MJ/kg for convection. The evaporator, not the osmosis, dominates — highlighting that OD is cheap because it avoids vaporizing the water it removes.

9.8 Product character (§28.5, p.678–679). Penetration depths: sugars 2–3 mm, water-content change to 5 mm, NaCl >12 mm in carrot. Osmotic removal cuts surface water-binding forces sixfold in 0.5 h — far more than convective drying to the same moisture. OD + convection/freeze gives less shrinkage, better colour/flavour/vitamin retention, and (with microwave assist) higher overall quality. OD is a pretreatment, never standalone preservation.

## 10. Critique (批判性评估)

- Plant anatomy is a metaphor, not a model, for SAP. Apoplast/symplast/plasmolysis describe living tissue; an SAP granule has no vacuole or plasmalemma. The physics (Π across a semipermeable boundary) transfers; the geometry does not.
- No polymer-science linkage is drawn. The chapter never mentions Flory–Rehner, Donnan, or crosslinked gels — yet its equations are the exact foundation of SAP swelling science. The reader must make the bridge (done in the POP block).
- Food-specific constants don't transfer. Sucrose/NaCl concentrations, 20–40°C optimum, 10 mm max thickness, 0.65–0.90 final a_w — all food process numbers.
- Countercurrent-flux modeling is admittedly incomplete (p.667–668): effective diffusivity cannot separate the two fluxes; the field stays empirical. The same incompleteness haunts SAP uptake-under-load modelling.
- Energy benchmark is OD-specific. The 100–2400 kJ/kg vs 5 MJ/kg comparison is for food OD vs convection; an SAP core's "energy saving" is conceptual (no vaporization), not a like-for-like process number.
- OCR/units noise. Eq.(28.3) constant "4.6063×10⁵" and scattered "8C" (= °C) artefacts; re-verify equations against print.
## 11. Hygiene-Material Relevance & Action Cards (卫材相关性与行动卡)

Rating for this chapter: ★★★★★ — it is the direct physical-chemistry bridge to SAP (crosslinked polyelectrolyte superabsorbent) behaviour; the osmotic-pressure/semipermeable-boundary/ion-effect framework is substrate-independent and maps one-to-one onto SAP swelling/deswelling.

H11.1 — Use Π = RT·ln a_w as the SAP swelling driver (★★★★★). Action: When scoping SAP uptake capacity/rate, start from the osmotic-pressure law Ch.28 derives (Eq.28.1–28.3, p.664) and the Flory–Rehner balance (mixing/osmotic pressure vs network elastic pressure). Treat external salt/urine Π as the counter-pressure that caps swell — the same role Ch.28 assigns to surround Π in plasmolysis (p.666).

H11.2 — Engineer the semipermeable boundary like the artificial membranes (★★★★★). Action: Ch.28 shows pectin/starch/alginate coatings reduce solute incorporation while keeping water flux (p.670–671). Mirror this when tuning SAP: surface crosslink density / coating controls uptake-rate vs leakage (gel-blockage, bleeding) — the boundary, not the bulk, is rate-limiting (p.669).

H11.3 — Expect electrolyte (Donnan) collapse, not just dilution (★★★★★). Action: Ch.28's "electrolytes give higher osmotic pressure because each ion affects solvent chemical potential" (p.664) is the Donnan principle. Predict that SAP capacity collapses in saline/urine not by simple dilution but by Donnan osmotic-pressure neutralization of the fixed –COO⁻ charges; validate against AUL (absorption under load) in synthetic urine.

H11.4 — Countercurrent flux ⇒ model water-in and ion-exchange together (★★★★). Action: As Ch.28 warns that water-out and solute-in fluxes interact and can't be split into independent diffusivities (p.667), model SAP uptake and salt/ion ingress as coupled countercurrent fluxes, not separate steps — especially under load where the network resistance dominates (p.669).

H11.5 — Osmotic pre-dewatering saves latent heat (★★★★). Action: Ch.28's energy result (no phase change; ~½–1/5 of convection energy, p.674–675) supports using a liquid-water removal / dewatering pre-step (e.g., mechanical press, membrane, or osmotic contact) ahead of any thermal dryer in fluff/pulp lines, exactly as Ch.27 used OD as a potato pretreatment.

H11.6 — 20–40°C is the selective window; raise T only if solute-ingress is acceptable (★★★). Action: Ch.28's best water-loss:solids-gain ratio sits at 20–40°C, with higher T driving more solute in (p.672). For any temperature-sensitive hygiene dewatering, keep to the lower window unless the co-transferred species is benign.

H11.7 — Cap sample/bed thickness to keep boundary-limited flow (★★★). Action: Lenart & Lewicki's "thickness should not exceed 10 mm" (p.670) and the extracellular-space-limiting effect (p.669) argue for thin, high-surface-area forms (e.g., airlaid/through-air mats, thin SAP layers) so osmotic/boundary transport, not bulk diffusion, sets the rate.

## 12. Book-Map Quotes (本书脉络引证)

- Ch.4 (p.81): effective diffusivity / Fick — the second-Fick foundation Ch.28 uses then critiques for countercurrent fluxes (p.667–668).
- Ch.26 (p.633): herbal/tea drying — sibling food chapter; no osmotic mechanism, contrast with Ch.28's physics.
- Ch.27 (p.645): potato drying — where OD appears only as a one-paragraph load-reducing pretreatment (p.654); Ch.28 is the mechanism behind that note.
- Ch.15 (p.383): impingement/convective high-flux drying — the thermal dryer OD offloads; Ch.28's energy comparison (~5 MJ/kg convection vs 100–2400 kJ/kg OD, p.674–675) is the cost argument.

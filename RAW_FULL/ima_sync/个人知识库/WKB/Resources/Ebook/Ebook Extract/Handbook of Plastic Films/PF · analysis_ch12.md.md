---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_f73cda1f7fa8b599522a37df5a0e0fc1001a693ee6c0644e"
source_file: "PF · analysis_ch12.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Plastic Films/PF · analysis_ch12.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# PF · analysis_ch12.md.md

# Chapter 12 — Testing of Plastic Films

## 1. Chapter Overview

Chapter 12 (E. M. Abdel-Bary & G. Akovali) is a comprehensive catalog of standardized test methods for plastic films, anchored on the premise that films are defined by viscoelastic behaviour absent in metals/paper. The authors first frame why testing is hard — polymer properties swing with temperature, rate and humidity across glassy→leathery→rubbery→flow regimes within  °C. They then survey mechanical tests (tensile, impact, tear, flexural, DMA), physical/chemical/physicochemical tests (density, haze, ignition/OI, friction, wetting tension, shrinkage, blocking, composition by ¹³C NMR, creep, weathering, abrasion, ESCR, WVTR, OTR), and close with ASTM material specifications for PET, LDPE, MDPE, PE, OPP and crosslinkable ethylene films. The dominant lens is packaging, but nearly every method maps onto hygiene-film quality control (backsheet, topsheet, printed/breathable films, converting). The chapter is reference-oriented rather than argumentative: its value is the inventory of measurable, standardised parameters a film developer must control.

## 2. Key Viewpoints

### Viewpoint 1 — Films are defined by viscoelasticity

- Page: p.329
- Quote: > "The word 'viscoelastic' is used to describe behaviour that shows both viscous and elastic characteristics even at ambient conditions, when stressed. This behaviour is a direct result of the long-chain nature of the polymeric molecules that constitute the plastic material."
- Interpretation: The chapter's founding concept: a film cannot be treated like paper/metal; time-, temperature- and rate-dependent response must be measured. This is the theoretical justification for most of the tests that follow.
### Viewpoint 2 — A polymer changes state within  °C

- Page: p.331
- Quote: > "a polymer, being viscoelastic, may change from a glassy solid through a leathery and then a rubbery stage to a sticky liquid in a temperature range of less than 100 °C."
- Interpretation: Sets the service-window problem: a hygiene film must perform from cold storage (−30 °C) to hot display (>60 °C). Test conditions must bracket the real-use temperature range.
### Viewpoint 3 — Molecular orientation makes films anisotropic

- Page: p.335
- Quote: > "tensile properties are higher in the direction of the covalent C–C bond in the chain than in the transverse direction, which is dominated by the much weaker van der Waals' bonds."
- Interpretation: Explains why blown/oriented films are stronger in the machine direction and why MD/TD properties must both be specified — directly relevant to backsheet tear/convertibility.
### Viewpoint 4 — Surface treatability is quantified by wetting tension

- Page: p.344
- Quote: > "A wetting tension of 3.5 × 10-2 N/m or higher has generally been found to reveal a degree of treatment normally regarded as acceptable for tubular film made from PE and intended for commercial flexographic printing."
- Interpretation: Gives a hard acceptance number for corona/plasma-treated PE/PP surfaces (linking to Ch.8); essential for printable, coatable, heat-sealable hygiene films.
### Viewpoint 5 — Detergents crack ethylene plastics (ESCR)

- Page: p.348
- Quote: > "in the presence of soaps, wetting agents and detergents, ethylene plastics may exhibit mechanical failure by cracking."
- Interpretation: A critical failure mode for any PE/PET film contacting surfactants — i.e., wipe substrates and cleaning-product packaging.
### Viewpoint 6 — WVTR/OTR are the barrier-defining metrics

- Page: p.348–349
- Quote: > "ASTM D3079 [59] and E96 [60]/F372 [61]/F1249 [62] cover standard test methods for plastic packaging films and plastics for water vapour permeability."
- Interpretation: Names the exact standards to quantify breathable vs barrier backsheet performance — the single most important functional test for hygiene films.
## 3. Research Method & Data Sources

||||||
|---|---|---|---|---|
|Mechanical|Tensile (ASTM D882), impact (D1709/D256), tear (D1922/D1938), flexural (D747/D790)|Film specimens|Universal tester, dart, pendulum|Rate/temp dependent; report MD & TD|
|Dynamic|DMA (ASTM D4065)|Tg, Tm, tan δ|Dynamic mechanical analyser|Elastic modulus 0.5 MPa–100 GPa|
|Surface|Wetting tension (D2578), friction (D1894), gloss (D2457)|PE/PP surfaces|Formamide/cellosolve drops, sled|Wetting tension ≥3.5×10⁻² N/m = print-ready|
|Barrier|WVTR (E96/F1249), OTR (D3985/D1434)|Permeation rate|IR/coulometric sensors|Airtight seal is the main difficulty|
|Durability|ESCR (D1693), weathering (D1435), abrasion (D1044)|Cracking/aging|Surfactant bath, carbon-arc chamber|Accelerated ≠ absolute lifetime|
|Composition|¹³C NMR (D5017), density (D1505)|Branch/composition|NMR, density-gradient column|LLDPE short-chain branches quantified|

## 4. Argumentation Process

The chapter does not argue a thesis so much as build a taxonomy: (1) state that films are viscoelastic → therefore properties are rate/temp/humidity sensitive → therefore a controlled, standardised test set is mandatory; (2) enumerate tests grouped by property class; (3) for each, give the ASTM/ISO code, the physical quantity measured, and a representative data point or caveat. Rhetorical move: constant cross-referencing to Ch.2 (processing→properties) and Ch.8 (surface treatment), positioning testing as the feedback loop that validates those upstream choices. Limitations are flagged per method (e.g., friction reproducibility hurt by blooming slip agents; accelerated weathering cannot predict absolute lifetime).

## 5. Role in the Book

Ch.12 is the "how do we verify it" companion to Ch.8 (modifications), Ch.9 (packaging/applications) and Ch.13 (recycling). It translates the material science of the earlier chapters into measurable acceptance criteria. For the hygiene expert it is the QC/QA backbone: every claim about a backsheet, breathable film or printed web must ultimately be confirmed by one of these ASTM methods.

## 6. Strengths & Weaknesses

✅ Strengths:
- Breedth and precision: "The ASTM D1894-95 test method [41] covers determination of the coefficients of starting and sliding friction of plastic film and sheeting" (p.343) — concrete, implementable.
- Explicit service-window warning: "packages that can be used in environments ranging from cold storage at –30 °C to a window display in hot sunshine, where the temperature can exceed 60 °C" (p.331).

⚠️ Limitations:
- Packaging/agriculture bias; hygiene-specific tests (e.g., SAP gel-block, rewet, strikethrough) are absent.
- Some tests are empirical/relative: "The choice of type and concentration of reagent, duration of immersion and temperature are all arbitrary, and this poses the main limitation of the method" (chemical resistance, p.341).
- Accelerated weathering "cannot be used to predict the absolute long-term performance" (p.347).

## 7. Key Terms / Concepts

- Viscoelasticity: (p.329) "behaviour that shows both viscous and elastic characteristics even at ambient conditions, when stressed."
- Damping: (p.329) "The ratio of viscous and elastic components, termed 'damping', can vary greatly over quite a narrow temperature range."
- Wetting tension: (p.344) "The wetting tension of the PE or PP film surface will be approximated by the surface tension of this particular mixture."
- Blocking: (p.345) "Blocking (unwanted adhesion) is a problem with plastic films … when touching layers of films are in intimate contact with almost complete exclusion of air."
- ESCR: (p.348) "The ability of a polymer surface to withstand an aggressive medium under load is known as environmental stress-cracking resistance (ESCR)."
- WVTR / OTR: (p.348–349) standard permeation test methods for water vapour and oxygen.
- Biaxially oriented PP: (p.351) "If the film tensile strengths in both the machine and transverse directions exceed 103 MPa, it is biaxially oriented PP."
## 8. Micro close-reading

Paragraph (p.331, §12.2.2, PS viscoelastic stages):
> "Taking polystyrene (PS) as an example of a simple amorphous polymer, one finds that the elastic modulus is constant in the temperature range up to about 100 °C, which is the glassy region. Increasing the temperature above 100 °C leads to a drastic decrease in the elastic modulus, as it exists in the leathery region. Further increase in temperature has no effect on the elastic modulus as PS falls in the rubbery region. In all these three regions – glassy, leathery and rubbery – the moduli of commercially useful polymers are independent of molecular chain length."

- Sentence 1 — Anchor: PS glassy region, constant E below ~100 °C. Function: baseline.
- Sentence 2 — Transition: above 100 °C E drops sharply (leathery). Technique: modulus-vs-T curve.
- Sentence 3 — Rubbery plateau: E constant again.
- Sentence 4 — Generalisation: three regions share chain-length independence.
- Logic: concrete PS example → abstract staged model of viscoelastic response. This is the conceptual hinge explaining why test temperature must be specified.
💡 Standout: "a polymer, being viscoelastic, may change from a glassy solid through a leathery and then a rubbery stage to a sticky liquid in a temperature range of less than 100 °C" — the single sentence that justifies every temperature-controlled test in the chapter.
## 9. Concept deep-dive

### 9.1 Viscoelasticity & DMA (Tg, Tm, tan δ)

- Definition (p.329): quoted in §2 VP1; operationalised by DMA (p.339): "Tests by dynamic mechanical analysis (DMA) provide the elastic and loss moduli as well as the loss tangent (damping) as functions of temperature, frequency and/or time."
- Operational? Yes — ASTM D4065, −160 °C to degradation, 0.01–1000 Hz.
- Usage: determines Tg/Tm, phase separation, crystallinity, filler effects (p.339–340).
- Relation: underpins the whole "test at use temperature" thesis; ties to PoP free-volume/transition theory.
### 9.2 Wetting tension & surface treatment (links Ch.8)

- Definition (p.344): drops of formamide/cellosolve mixtures; surface wets if film intact ≥2 s.
- Operational? Yes — ASTM D2578; acceptance ≥3.5×10⁻² N/m for PE flexo printing.
- Usage: "The ability of PE and PP films to retain inks, coating, adhesives … can be improved by one of several surface-treatment techniques mentioned in Chapter 8" (p.344) — explicit bridge to corona/plasma/oxidation.
### 9.3 Water-vapour / oxygen transmission (barrier design)

- Definition (p.348–349): WVTR via D3079/E96/F372/F1249 (desiccant + IR detection); OTR via D1434/D3985 (manometric / coulometric).
- Operational? Yes; reports g/30 days or g/cycle; steady-state rate.
- Usage: "In the packaging of hygroscopic materials … the permeability properties of the film to water vapour and other gases is very important" (p.348) — identical need for breathable hygiene backsheets.
### 9.4 Biaxial orientation (OPP)

- Definition (p.351): biaxially oriented PP = both MD & TD tensile >103 MPa.
- Operational? Yes — ASTM D2673, 10–50 µm.
- Usage: orientation raises tensile but can increase MD/TD anisotropy; balanced OPP defined by ≤55 MPa strength spread (p.351).
## 10. Academic critique & open questions

- Hygiene blind spot: no tests for rewet, strikethrough, SAP gel-block, or skin-contact comfort — the metrics that actually define a diaper/wipe.
- Empirical limits: friction, chemical resistance and weathering tests are flagged as reproducibility-limited or arbitrary (p.341, p.343, p.347).
- Single-polymer focus: mostly PE/PP/PET; multilayer (e.g., PE/EVOH/PE breathable laminates) permeation needs layered models not covered.
- Open Q1: Can DMA tan-δ peaks predict the in-use softness/stiffness feel of a topsheet across the −30→60 °C window?
- Open Q2: For breathable backsheets (microporous/monolithic), which WVTR standard (E96 vs F1249) best correlates with wearer comfort?
## 11. Hygiene-material relevance & action cards

Relevance to diaper / wipe / absorbent-core R&D: ★★★★★ (almost every test is a QC gate for backsheet, topsheet, printed/breathable film and converting).

ACTION CARD 1 — Specify breathable vs barrier backsheet by WVTR
- Situation: Choosing/claming a backsheet film.
- Apply: Run ASTM E96 or F1249 (p.348–349) to set water-vapour transmission; pair with ASTM D3985 for OTR. Use the result to tier "impermeable PE" vs "breathable microporous/monolithic".
- Expected effect: Evidence-based comfort-vs-leakage trade-off; rejects films that are "breathable" only by marketing claim.

ACTION CARD 2 — Make wetting tension ≥3.5×10⁻² N/m a print/coat acceptance limit
- Situation: Printed or adhesive-laminated backsheet/web.
- Apply: Use ASTM D2578 (p.344); require surface wetting tension ≥3.5×10⁻² N/m after corona/plasma treatment (Ch.8 link) before printing or coating.
- Expected effect: Reliable ink/adhesive retention; prevents delamination and print dropout on converted rolls.

ACTION CARD 3 — Screen wipe/cleaner films for ESCR against surfactants
- Situation: Films or laminates contacting detergents/surfactants (wipes, cleaning packs).
- Apply: ASTM D1693 ESCR (p.348): bent specimen + surfactant, report % cracking in given time; raise polymer MW to improve ESCR (p.348).
- Expected effect: Prevents in-use brittle cracking of PE-based wipe substrates and pouches.

ACTION CARD 4 — Control coefficient of friction for converting machinability
- Situation: High-speed converting/rolling of backsheet.
- Apply: ASTM D1894 (p.343) static/kinetic µ; account for slip-agent blooming time-dependence before testing.
- Expected effect: Avoid web jams/slip and blocking on converting lines.

## 12. Book-map quotes

"The word 'viscoelastic' is used to describe behaviour that shows both viscous and elastic characteristics even at ambient conditions, when stressed." — p.329 — the chapter's founding concept, the reason films need their own test regime.
"A wetting tension of 3.5 × 10-2 N/m or higher has generally been found to reveal a degree of treatment normally regarded as acceptable for tubular film made from PE …" — p.344 — the quantified link between Ch.8 surface treatment and printable/coatable film.
"in the presence of soaps, wetting agents and detergents, ethylene plastics may exhibit mechanical failure by cracking." — p.348 — the ESCR warning that governs any surfactant-exposed hygiene film.

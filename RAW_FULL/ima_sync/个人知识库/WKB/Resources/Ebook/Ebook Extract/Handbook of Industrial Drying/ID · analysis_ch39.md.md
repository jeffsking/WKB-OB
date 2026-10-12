---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_eda56a79240a43b1bcb665632f679369001a693ee6c0644e"
source_file: "ID · analysis_ch39.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch39.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch39.md.md

# Chapter 39 — Drying of Biotechnological Products

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 39 (Adamiec, Kamiński, Markowski & Strumiłło) treats drying as preservation of biologically active material — microorganism cultures, enzymes, antibiotics, vitamins, proteins — rather than as bulk water removal. The authors frame the core problem: in these colloidal-capillary-porous substances, water is both solvent and a structural element of the particle, so drying must preserve activity/storage life, not merely hit a moisture target. They classify products by thermal lability (thermo-/xerolabile vs thermo-/xerostable) and by whether water is life-sustaining or merely a solvent, then derive first-order activity-loss kinetics via the Arrhenius equation (Table 39.3 gives activation energies). Method sections cover spray, jet-spouted-bed, impingement-stream, fluidized/vibrofluidized, fixed-bed, drum, freeze/vacuum, carrier, and encapsulated drying. The chapter closes with the three design levers: shorten high-temperature exposure, enable frequent parameter control, and use carriers/sorbents plus protective additives (glycerin, sugars). For hygiene, this is the home chapter for probiotic/active-ingredient wipes and enzyme-containing formulations.

## 2. Key Viewpoints (with verbatim quotes + print pages)

### Viewpoint 1 — Water is both solvent and structural element; drying must preserve activity

- Page: p.905
- Quote: "In the process of concentration and drying of these materials, attention cannot be paid only to the removal of water, which is the medium and solvent of a substance, but also to the removal of water, which is a constructional element of the product particle. The presence or absence of such water is of fundamental importance for biotechnological product storage life, its activity, and applicability."
- Interpretation: The design objective is activity retention, not just final MC. Directly relevant to any active/probiotic ingredient we dry into a wipe or formulation.
### Viewpoint 2 — Products split into thermolabile (life-sustaining water) vs thermostable (water as solvent)

- Page: p.908
- Quote: "1. Materials nonresistant thermally… bacterial cultures, enzymes, viruses, yeast, and fungi are included. 2. Biotechnological products of high thermal resistance… This group contains the products of microbiological synthesis and spores (e.g., amino acids, antibiotics, and selected bacterial strains)."
- Interpretation: The lability classification dictates allowable temperature. Enzymes and live cultures (probiotic wipes) sit in the fragile group (critical ~60°C, 35–40% wb); antibiotics/vitamins are far more robust (~150°C, 5–7% wb).
### Viewpoint 3 — Activity loss follows first-order Arrhenius kinetics

- Page: p.910
- Quote: "In majority of qualitative changes it is assumed that their kinetics corresponds to the first-order reaction and can be described by the following equation: dA/dt = −k_d A… The reaction rate constant k_d, as a function of temperature, is determined by the Arrhenius equation: kd = k{d,0} exp(−E_a/(R_u T))."
- Interpretation: Gives a quantitative handle: activity decay rate is exponential in 1/T with an activation energy E_a. Table 39.3 lists E_a per organism/enzyme, enabling time–temperature budgeting for a drying step.
### Viewpoint 4 — Freeze/vacuum drying excludes thermal inactivation but is slow and energy-heavy

- Page: p.917
- Quote: "In freeze and vacuum drying, drying takes place at low temperatures, below 0°C… The process has the following advantages: Moisture is removed at low temperature, which in fact excludes thermal inactivation of the product. The material structure is maintained (particles and cells are not damaged)."
- Interpretation: The quality-preserving route for the most labile actives; trade-off is process duration, energy, and equipment complexity. Relevant when a wipe/active formulation must keep live cells intact.
### Viewpoint 5 — Protective additives and vitrification protect cells during freezing

- Page: p.918
- Quote: "The presence of protective substances in dried material, such as glycerin and sugars (fructose, saccharose, lactose, or specially prepared compositions…) has influence on the eutectic temperature and the applicability of elevated temperatures during freeze drying. The substances protect microorganisms against too high salt concentration and provide more favorable conditions for ice crystallization during freezing."
- Interpretation: Formulation (cryoprotectants) is part of the drying design. Glycerin is described as forming "vitreous structures" — a glassy (vitrified) matrix that spares cell membranes.
### Viewpoint 6 — Spray drying works for thermolabile material if done at the wet-bulb temperature

- Page: p.914
- Quote: "spray drying can also be applied to thermolabile substances provided the sprayed material is highly dispersed and the drying agent has a high temperature (the drying process takes place immediately at a wet bulb temperature). Thus, the product quality is not deteriorated."
- Interpretation: High inlet air + tiny droplets keeps the particle at wet-bulb (evaporative cooling) so the active never sees the gas temperature. The same principle Ch40 uses for coatings; here it preserves activity.
## 3. Research Method & Data Sources

Mechanistic + empirical review: degradation kinetics modeled via chemical-reaction-rate theory, validated against literature data.

||||||
|---|---|---|---|---|
|Quality-degradation kinetics|First-order + Arrhenius (Eq 39.2–39.3); alternative k=k₁exp(zT) (Eq 39.10)|Tutova & Kuts (1987), Luyben et al. (1982), Kerkhof & Schoeber (1974)|ODE models|Experimental vs calculated discrepancy 20–30% (p.910)|
|Activation-energy tables|Fitted E_a, k from isothermal data|Tutova & Kuts Table 39.3|Regression|Representative per organism/enzyme|
|Droplet/sublimation modeling|Heat/mass transfer in droplet (Eq 39.9), sublimation front (Fig 39.16)|Kerkhof & Schoeber, Popovski et al.|Numerical|Mechanism sound|
|Carrier/sorbent selection|Relative absorptivity K = a_s/a_r (Eq 39.20), Fig 39.22|Tutova & Kuts|Equilibrium sorptivity|Empirical ranking|
|Encapsulation|Spray/freeze dry of microcapsules (~10 µm)|Benita (1996), Gander (1996), Re (1998)|Lab-scale|Mostly lab scale (p.923)|

## 4. Argumentation Process

- Scope — biotechnology = drying for preservation (p.903–904).
- Material nature — colloidal-capillary-porous; free vs bound water; water as structural element (p.905–906).
- Degradation taxonomy — biochemical/enzymatic/chemical/physical; Table 39.1–39.2 (p.906–907).
- Classification by lability — two groups by critical T & MC; water-as-life vs water-as-solvent (p.908–909).
- Kinetic modeling — first-order + Arrhenius; Table 39.3 E_a; moisture-dependent k (p.910–913).
- Methods — spray → JSB → ISD → fluidized/vibro → fixed → drum → freeze/vacuum → carrier → encapsulated (p.914–923).
- Design levers & conclusion — shorten high-T, control, carriers + protective substances (p.924).
## 5. Role in the Book

Ch39 is the "biological activity preservation" chapter, complementary to Ch41 (polymer resins), Ch42 (enzymes specifically), and Ch40 (coated webs). Where Ch42 focuses on enzyme activity-loss, Ch39 generalizes to whole cells, spores, antibiotics and encapsulated actives. For the hygiene reader it is the bridge from bulk/material drying to keeping a living or bioactive ingredient alive through a converting/drying step (probiotic wipes, enzyme-based stain-removal wipes, vitamin/active coatings).

## 6. Strengths & Weaknesses

✅ Strengths: Unusual in giving a quantitative activity-loss model (first-order + Arrhenius, Table 39.3 E_a values) rather than only qualitative advice. The water-as-structural-element framing and the lability classification are procurement/process-useful. Protective-additive and carrier/sorbent strategies are concrete. The spray-at-wet-bulb rule (p.914) is a clean, transferable design principle.
⚠️ Limitations/contestable: Empirical vs calculated discrepancy of 20–30% is admitted (p.910). The Arrhenius alternative k=k₁exp(zT) (Eq 39.10) is used for some systems where Arrhenius fits poorly. Encapsulation section is largely lab-scale and cosmetic/pharma-oriented (p.923). No direct hygiene (diaper/wipe) examples; relevance is by analogy to active/probiotic ingredients.

## 7. Key Terms / Concepts

- Water as structural element: p.905, "removal of water, which is a constructional element of the product particle."
- Free vs bound water: p.905, "free water… in the cells of microorganisms… bound water… in the macromolecules of biopolymers." Live cell water 70–98%; bound only 15–18% (p.905).
- Four change types: p.906, Table 39.1 — biochemical (microbiological), enzymatic, chemical, physical.
- Lability groups: p.908, Group 1 thermolabile (critical T ~60°C, MC 35–40% wb); Group 2 thermostable (critical T ~150°C, MC 5–7% wb).
- First-order + Arrhenius: p.910, Eq 39.2 dA/dt=−k_d A; Eq 39.3 kd=k{d,0}exp(−E_a/(R_u T)).
- Activation energies: p.911, Table 39.3 — e.g., Lactobacillus plantarum 428 kJ/mol, Bacillus thuringiensis (spore) 33, Bacitracin 68, Lysine 107.
- Multistage recommendation: p.914, "first stage is a spray dryer… predried… second and third stages are fluidized or vibrofluidized bed dryers."
- Freeze/vacuum advantages: p.917, low-T excludes thermal inactivation; structure/cells maintained; sterile product.
- Self-freezing/vitrification: p.917, ultra-swift cooling (10,000°/min) → "amorphous ice is formed (transformation into a vitreous form, termed vitrification), which does not cause mechanical damage of cells."
- Protective substances: p.918, glycerin/sugars protect against high salt concentration; form "vitreous structures."
- Carrier/sorbent: p.920, carrier "protects cells or biopolymers against mechanical or thermal destruction… takes over part of moisture from biomass."
- Encapsulation: p.922, "encapsulation of valuable substances and next drying of these systems so that they could be stored in a stable state"; dry spheres ~10 µm via spray/freeze dryers.
## 8. Micro close-reading (ONE key paragraph)

p.905–906 (water as structural element + change taxonomy):
> "In the process of concentration and drying of these materials, attention cannot be paid only to the removal of water, which is the medium and solvent of a substance, but also to the removal of water, which is a constructional element of the product particle. The presence or absence of such water is of fundamental importance for biotechnological product storage life, its activity, and applicability. … A variety of biotechnological products… do not allow precise specification of the form of material-moisture binding. In general, it is assumed that these materials belong to colloidal-capillary-porous substances in which all forms of material-moisture bonds are possible. Apart from water solvent, there are also free water and bound water."

Sentence-by-sentence: (1) Reframe — drying goal is not just stripping solvent water but also structural water. (2) Stakes — that structural water decides storage life, activity, applicability. (3) Caveat — precise moisture-binding form is often unknowable per product. (4) Model — treat as colloidal-capillary-porous with all bond types possible. (5) Split — free water (solvent) vs bound water (in biopolymers). The conceptual move is from "dry to X% MC" to "preserve the water that matters for activity."
💡 Standout line: "removal of water, which is a constructional element of the product particle… of fundamental importance for… activity, and applicability" — the thesis that reframes drying as activity preservation.

## 9. Concept deep-dive

Activity-loss kinetics as a design budget (the quantitative core). The chapter models quality degradation as first-order (p.910): dA/dt = −k_d A with kd = k{d,0} exp(−E_a/(R_u T)), and even lets k_d depend on moisture X (Eq 39.4, 39.6). Table 39.3 gives concrete E_a: living nonspore bacteria are highly activation-energy-dependent (Lactobacillus plantarum 428 kJ/mol, Lactobacillus acidophilus 142), spores are remarkably stable (Bacillus thuringiensis 33), and small molecules like lysine sit at 107, bacitracin 68. [inference] This lets a process engineer trade temperature against residence time: a higher inlet temperature is tolerable only if the particle sees it briefly (spray at wet-bulb, p.914) or if E_a is low (thermostable antibiotic). For an enzyme- or probiotic-containing wipe, this is the equation that bounds the converting-line temperature profile.

Vitrification = the biopolymer glass state (the freeze-drying safeguard). p.917–918: ultra-rapid self-freezing (10,000°/min) yields "amorphous ice… transformation into a vitreous form, termed vitrification," which avoids the mechanical membrane damage caused by slow large-crystal freezing. Protective glycerin/sugars "shift the coordinates of eutectic borders and contribute to the formation of vitreous structures." This is a polymer-glass-transition phenomenon: the frozen matrix enters a glassy (non-crystalline) state that immobilizes reactants and spares cells. The glycerin mechanism (dissolves salts, restores osmotic balance, makes crystallization reversible) is exactly a plasticizer/stabilizer role.

Carrier/sorbent as a moisture-sink and protective matrix. p.920: a carrier "protects cells or biopolymers against mechanical or thermal destruction during drying" and "takes over part of moisture from biomass and thus the amount of water to be evaporated is smaller." Relative absorptivity K (Eq 39.20, Fig 39.22) ranks zeolite/silica-gel/activated-carbon (high K, humidity-dependent) against maize meal/potato flour/peat (K≈1–1.5, humidity-independent). For a hygiene active, a food-grade carrier (skim milk, maltodextrin/starch — see encapsulation refs) doubles as protectant and lowers drying energy.

## 10. Academic critique & open questions

- The admitted 20–30% discrepancy between experimental and calculated degradation (p.910) limits quantitative use of Table 39.3 for precise process design; E_a values are product- and batch-specific.
- Eq 39.10 k=k₁exp(zT) is an empirical stand-in where Arrhenius fails; the chapter does not resolve which regime governs a given system.
- Encapsulation discussion is cosmetic/pharma-centric and lab-scale (p.923); translation to industrial hygiene active-wipe lines is asserted, not demonstrated.
- Open question 1: Can the first-order/Arrhenius model (p.910, Table 39.3) be extended to a multi-strain probiotic consortium in a wipe substrate, where each strain has a different E_a and the local temperature/MC vary through the web?
- Open question 2: For a glycerin/sugar-protected active encapsulated in a starch–chitosan matrix (p.922, refs 79/85/88), what is the storage-MC window that keeps the vitreous protectant stable without re-crystallization that releases the active prematurely?

## 11. Hygiene-material relevance & action cards

Overall relevance: ★★★ (moderate — probiotic/active-ingredient wipes, enzyme formulations; not core structural materials).

Action Card H39-1 — Treat active-ingredient drying as activity preservation, not MC targeting. Insight: p.905 water is "a constructional element… of fundamental importance for… activity." Action: For probiotic/enzyme/ vitamin wipes, set the drying spec from an activity-retention target (% viable cells / % enzyme activity remaining), not just final MC. → 卫材相关性★★★★☆｜Converts invisible activity loss into the real acceptance criterion.

Action Card H39-2 — Use first-order/Arrhenius to budget line temperature. Insight: p.910 dA/dt=−k_d A, kd=k{d,0}exp(−E_a/(R_u T)); Table 39.3 E_a per organism/enzyme. Action: When designing or auditing an active-coating/impregnation dryer, compute the allowable product-temperature × residence-time envelope from the active's E_a; require the line stay inside it. → 卫材相关性★★★★☆｜Prevents thermal kill of probiotic/enzyme actives on the line.

Action Card H39-3 — Prefer spray-at-wet-bulb or freeze-dry for labile actives. Insight: p.914 spray drying works for thermolabile material "at a wet bulb temperature"; p.917 freeze/vacuum "excludes thermal inactivation." Action: For live-culture or high-value enzyme wipes, qualify a spray dryer run at wet-bulb (high dispersion, high inlet air) or a freeze-dry step; avoid sustained high-T hovering. → 卫材相关性★★★★☆｜Keeps the most fragile actives alive through drying.

Action Card H39-4 — Add cryo/protective substances to the active formulation. Insight: p.918 glycerin/sugars protect cells, form "vitreous structures," buffer salt concentration. Action: Require protective additives (glycerin, trehalose/sucrose, skim milk, maltodextrin) in any freeze- or spray-dried active system; verify they are skin-contact-compliant. → 卫材相关性★★★★☆｜Formulation-side lever to survive drying and storage.

Action Card H39-5 — Use a food-grade carrier/sorbent for delicate actives. Insight: p.920 carrier "protects cells or biopolymers… takes over part of moisture"; Fig 39.22 ranks sorbents. Action: For powdered active premixes for wipes, specify a food-grade carrier (starch/maize meal/skim milk) that buffers moisture and lowers drying energy. → 卫材相关性★★★｜Two benefits: protection + energy saving in the active premix.

Action Card H39-6 — Consider encapsulation for stabilized, delayed-release actives. Insight: p.922 encapsulation "stored in a stable state… action is prolonged to many hours"; dried as ~10 µm spheres via spray/freeze. Action: For fragrance/active wipes wanting delayed or protected release, evaluate spray-dried microcapsules (starch/chitosan matrix, refs 79/85/88). → 卫材相关性★★★｜Enables stabilized, controlled-release active delivery in wipes.

## 12. Book-Map Quotes (Top representative quotes)

"attention cannot be paid only to the removal of water, which is the medium and solvent of a substance, but also to the removal of water, which is a constructional element of the product particle." — p.905 — the activity-preservation thesis.
"In majority of qualitative changes it is assumed that their kinetics corresponds to the first-order reaction and can be described by… kd = k{d,0} exp(−E_a/(R_u T))." — p.910 — the quantitative activity-loss model.
"The presence of protective substances in dried material, such as glycerin and sugars… contributes to the formation of vitreous structures." — p.918 — the stabilization/vitrification mechanism.


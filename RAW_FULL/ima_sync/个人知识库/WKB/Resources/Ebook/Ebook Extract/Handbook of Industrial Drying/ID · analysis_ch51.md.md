---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_850f5e71e6b6b8017afc68685ea89ba2001a693ee6c0644e"
source_file: "ID · analysis_ch51.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch51.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch51.md.md

# Chapter 51 — Industrial Crystallization

## 1. Chapter Overview (100–200 words)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Chapter 51 (Palosaari, Louhi-Kultanen & Sha) is an overview of industrial crystallization from solution, written from the perspective of facilitating downstream operations — especially filtration and drying. Its organizing thesis (p.1202) is that "the easy dewatering and drying of crystals requires that the crystals be of a uniform and sufficiently large size." The chapter develops the fundamentals (solubility/supersaturation, metastable zone, nucleation, CSD, crystal shape, purity, polymorphism), then the control levers for CSD and habit (supersaturation programming, seeding, precipitation, continuous schemes such as clear-liquor advance, fines destruction, classified removal, mixing intensity), then industrial crystallizer types (batch, FC/DTB/FB), filtration of crystal suspensions, and finally crystal drying and CFD/advances. For the hygiene reader this is not a drying process; its value is conceptual — nucleation/growth kinetics, supersaturation control, and habit/polymorph modification transfer as the small-molecule analogue of polymer crystallization and of solid-form control for actives.

## 2. Key Viewpoints (with verbatim quotes + print pages)

### Viewpoint 1 — Crystal size & uniformity are set for the sake of downstream drying/filtration

- Page: p.1202
- Quote: "The easy dewatering and drying of crystals requires that the crystals be of a uniform and sufficiently large size. This is, therefore, the major theme of this chapter."
- Interpretation: The entire chapter is framed around making a particulate that is easy to separate and dry — the same design goal a hygiene powder (SAP, actives) engineer faces, even though the mechanism (crystallization) differs from drying.
### Viewpoint 2 — Supersaturation drives growth, nucleation, agglomeration, shape, and purity

- Page: p.1203
- Quote: "Supersaturation is the main parameter in determining the rate of crystal growth and nucleation … the level of supersaturation is the main parameter that determines the agglomeration, shape, and purity of the crystals."
- Interpretation: One knob — supersaturation — governs every product attribute. Conceptually parallel to how undercooling drives polymer crystallization and final crystallinity.
### Viewpoint 3 — Small crystals are hard to dewater/dry; porosity/roughness matter

- Page: p.1205
- Quote: "the smaller the size of the crystals, the more difficult the dewatering and drying. The effect of a wide distribution of crystal sizes is the same. Especially in precipitation, where agglomerates are formed, the porosity and roughness of the crystal surface may also affect dewatering and drying."
- Interpretation: Directly analogous to fine SAP/actives powder: sub-10 µm fractions are hard to handle, filter, and dry, and surface roughness traps mother liquor/solvent.
### Viewpoint 4 — Slow growth yields purer crystals; inclusions lower purity

- Page: p.1206
- Quote: "As a general rule for purification by crystallization, the slower the crystal growth rate, the purer the crystal … If agglomeration takes place, the secondary crystals may contain inclusions of the mother liquor, which decreases the purity of the crystalline product."
- Interpretation: Growth-rate/purity trade-off and mother-liquor inclusion are the small-molecule analogue of residual monomer/solvent trapped in polymer particles (a VOC/drying concern).
### Viewpoint 5 — Polymorphism: same composition, different solid form and properties

- Page: p.1206
- Quote: "A chemical may have several crystal structures; the chemical compositions of these polymorphs are identical. This phenomenon is called polymorphism … The various melting points and the difference in dissolution rates from one polymorph to another are the main factors that have to be taken into account in the pharmaceutical industry."
- Interpretation: The conceptual bridge to polymer crystalline form (e.g., isotactic PP, crystalline vs amorphous regions) where solid form dictates dissolution, mechanical response, and stability.
### Viewpoint 6 — Seeding with the right size/mass controls nucleation

- Page: p.1208
- Quote: "in practice, 0.1 to 0.3 times the final size and 0.1 to 3% of the final mass of the seed area are good choices for the seed size and mass, respectively … seed crystals of 20 to 50 mm are appropriate for the production of final crystals of 500 to 1000 mm."
- Interpretation: Quantified seeding rule that prevents runaway nucleation — analogous in spirit to nucleating agents/seeds used to set polymer crystalline structure.
### Viewpoint 7 — Fines destruction widens CSD but grows larger mean crystals

- Page: p.1210
- Quote: "This operation is very useful in increasing the size of crystals in a system that has a high rate of nucleation. This method does, however, lead to a wide particle size distribution."
- Interpretation: The recurring tension — bigger mean size vs narrower distribution — is exactly the granule-sizing trade-off in SAP/powder product design.
### Viewpoint 8 — Drying favours ~1 mm crystals; above that is harmful

- Page: p.1218
- Quote: "From the viewpoint of drying, it would be best that the crystals be large, within the range of about 1 mm or above … crystal sizes above approximately 1 mm tend to be harmful. For crystals larger than 1 mm, it may be difficult to maintain the steady state in a continuous process, due to the decreased overall crystal surface required for releasing supersaturation."
- Interpretation: A concrete sizing window — too small filters poorly, too large breaks and destabilizes the process — the same band a powder-product spec must respect.
## 3. Research Method & Data Sources

Review/chapter-survey drawing on Mullin, Randolph & Larson, Mersmann, Myerson, Tavare, Davey & Garside, Söhnel & Garside, plus population-balance theory, CFD studies, and equipment handbooks (Wakeman & Tarleton, Svarovsky).

||||||
|---|---|---|---|---|
|Fundamentals|Solubility/supersaturation/metastable zone|Mullin; Mersmann|Eqs 51.1–51.3|Textbook standard|
|CSD kinetics|Population balance, nucleation/growth empirical|Randolph–Larson; Toyokura; Palosaari|Eqs 51.6–51.12|Requires empirical kinetics|
|Habit/polymorph|Molecular modeling (Cerius2, HABIT95)|Davey–Garside; Winn–Doherty|Attachment-energy, BFDH|Approximate; solvent effect hard|
|Crystallizer design|FC/DTB/FB operation tables|Mersmann Table 51.1–51.2|Table 51.1|Industrial data|
|Filtration|Kozeny–Carman, equipment indices|Wakeman–Tarleton Table 51.3|Eq. pressure ∝ d⁻²|Empirical|
|CFD|Multi-scale fluid dynamics + population balance|Garside; Zauner–Jones; Wei–Garside|CFX/MUSIC|Still under development|

## 4. Argumentation Process

- Why size matters — downstream drying/filtration need large uniform crystals (p.1202).
- Fundamentals — supersaturation as the master variable; nucleation (primary/secondary); CSD; shape; purity; polymorphism (p.1203–1206).
- Control levers — program cooling, seeding, precipitation, continuous schemes (clear-liquor, fines destruction, classified removal), mixing intensity (p.1207–1212).
- Equipment & separation — crystallizer selection by solubility slope; batch vs continuous; filtration (Kozeny–Carman, media, Table 51.3); crystal drying window (p.1213–1219).
- Advances — CFD for local supersaturation; polymorph control via supersaturation/additives (p.1220–1221).
The logic is product-driven: define the ideal crystalline particle, then enumerate every lever that produces it.
## 5. Role in the Book

Ch51 is the sole solids-formation chapter adjacent to the drying unit operations. It complements Ch52 (frying) and the spray/flash/fluid-bed chapters by treating the upstream particle-generation step whose output those dryers would handle. Where Ch49 (control) and Ch48 (safety) govern the dryer, Ch51 governs the crystalline feedstock's size/purity/habit — relevant to any hygiene line that receives or produces a crystalline active, salt, or filler.

## 6. Strengths & Weaknesses

✅ Strengths: Clear, quantitative CSD relations (L₅₀ = 3.67 Gτ, L_d = 3 Gτ, Eq 51.8–51.9); practical seeding/fines-destruction rules; the Kozeny–Carman filtration insight (d→10% ⇒ ΔP ×100); the honest drying window (~1 mm optimum, >1 mm harmful); the polymorphism discussion. The crystallization↔drying coupling (size/purity/habit) is the genuinely transferable part.
⚠️ Limitations/contestable: This is not a drying process — the chapter's relevance to a hygiene drying reader is conceptual, not operational. OCR garbling of equations (Eq 51.4–51.5 programed-cooling profiles, p.1207; power-input notation "10(cid:2) 4–10(cid:2) 2" for L₅₀ in Table 51.1, p.1213). The "more an art than science" admission (p.1216) and the repeated "prediction of CSD is still quite difficult" (p.1205) signal weak predictive power. CFD "still at an initial stage" (p.1212). No hygiene-substrate treatment.

## 7. Key Terms / Concepts

- Supersaturation: p.1203, Δc = c − c* (Eq 51.1); S = c/c* (Eq 51.2, S>1); relative s = (c−c)/c (Eq 51.3).
- Metastable zone: p.1204, "concentration is higher than in saturation but below the one where spontaneous nucleation occurs. Therefore, the crystal growth is mainly occurring in the metastable zone."
- Primary vs secondary nucleation: p.1204, primary "in the absence of other substances" (homogeneous) or "in the presence of other substances" (heterogeneous); secondary "with the presence of crystals … the nuclei are crystal fragments or added seed crystals."
- Population balance: p.1205, Eq 51.6 (∂n/∂t + G ∂n/∂L = 0); median L₅₀ = 3.67 G τ (Eq 51.8); dominant L_d = 3 G τ (Eq 51.9).
- Healing effect: p.1206, tiny attrition fragments "tend to initially obtain a more regular morphology at a relatively high growth rate" — explains impurity in small fraction.
- Polymorphism / enantiotropy / monotropy / pseudopolymorphism: p.1206, "A chemical may have several crystal structures … polymorphism"; reversible = enantiotropy, irreversible = monotropy; pseudopolymorphism "when a solvent enters the crystal lattice and forms … a hydrate … or a solvate."
- Seeding rules: p.1208, seed 20–50 mm for final 500–1000 mm; small crystals dissolve via "Ostwald ripening effect."
- Kozeny–Carman / filtration: p.1216, "If the particle diameter drops to 10% of its original value, the pressure drop increases by 100-fold"; "If the viscosity increases tenfold, the pressure drop also increases tenfold."
- Drying window: p.1218, "crystals be large, within the range of about 1 mm or above … above approximately 1 mm tend to be harmful."
- Filter media: p.1217, "synthetic fibres, such as nylon, polyester, polypropylene, polyethylene, or fluorocarbon."
## 8. Micro close-reading (ONE key paragraph)

p.1218 (the drying-window paragraph — the most transferable sentence in the chapter):
> "From the viewpoint of drying, it would be best that the crystals be large, within the range of about 1 mm or above. After the filtration stage, the amount of mother liquor in the crystals is low. The large crystal size also improves purity because the same thickness of the attached mother liquor on the surface, which contains impurities, results in a lower level of impurities in large crystals. … crystal sizes above approximately 1 mm tend to be harmful. For crystals larger than 1 mm, it may be difficult to maintain the steady state in a continuous process, due to the decreased overall crystal surface required for releasing supersaturation. Furthermore, large crystals may break in the centrifuge."

Sentence-by-sentence: (1) Optimum — ~1 mm+ is best for drying. (2) Low mother liquor — big crystals retain less interstitial liquor after filtration. (3) Purity lever — same surface-liquid thickness covers proportionally less mass, so large crystals are purer. (4) Upper bound — >1 mm becomes harmful. (5) Process reason — less surface area means less capacity to consume supersaturation in continuous mode. (6) Mechanical reason — large crystals fracture in the centrifuge. This is the chapter's sharpest statement of the size band a powder product must sit within.
💡 Standout line: "crystal sizes above approximately 1 mm tend to be harmful" — the upper bound that makes "as large as possible" wrong, a lesson directly portable to granule/SAP sizing.

## 9. Concept deep-dive

Nucleation–growth kinetics as the small-molecule analogue of polymer crystallization. The chapter's core mechanism — supersaturation (undercooling analogue) drives primary (homogeneous/heterogeneous) and secondary nucleation, then growth in the metastable zone, with the metastable-zone width setting how easily new nuclei form (p.1203–1204) — is precisely the nucleation-and-growth picture of polymer crystallization on cooling. The kinetics are captured by the population balance (∂n/∂t + G ∂n/∂L = 0, Eq 51.6) and mean-size relations L₅₀ = 3.67 Gτ, L_d = 3 Gτ (Eq 51.8–51.9): bigger crystals come from slower nucleation or longer growth time (residence time τ). For a polymer, undercooling ΔT below T_m plays the role of supersaturation, and nucleation density sets spherulite size — the same levers, different physics.

Habit/polymorph modification. The chapter shows crystal shape is governed by face-specific growth (interaction-energy / attachment-energy models; "the greater the surface density of molecules on a face, the stronger the lateral interactions … and the more stable and slow the crystal growth," p.1205) and that polymorphism lets one composition adopt multiple solid forms with different dissolution rates (p.1206). Supersaturation can even select the polymorph (Finnie; Ma & Braatz, p.1221). This is the conceptual template for understanding how a polymer's crystalline form (isotactic vs atactic, crystalline vs amorphous) and additive/nucleating agents set its properties.

Where transfer stops (honesty). Crystallization produces a crystalline solid from solution via phase change; hygiene drying removes liquid from an already-solid particulate. The chapter gives no drying-rate equations, no moisture-transport model, and no relevance to fluff-pulp or web drying. Its numbers (MEC/K_st/MIE of Ch48, control loops of Ch49) do not appear. The value is limited to: (a) thinking in nucleation/growth/metastable-zone terms when a hygiene material crystallizes on cooling (polymer, fat, wax), and (b) the size/purity/filterability trade-offs that apply to any powder including SAP and actives.

## 10. Academic critique & open questions

- The chapter repeatedly concedes weak predictability: "prediction of CSDs is still quite difficult" (p.1205); crystallizer selection "more an art than science" (p.1216); CFD nucleation modeling "still at an initial stage" (p.1212). So it is a qualitative guide, not a design manual.
- OCR garbling: Eq 51.4–51.5 cooling-profile formulas (p.1207); Table 51.1 power/size notation (p.1213). Verify against Mersmann before use.
- Polymorph control via supersaturation/additives is described as "early results" (p.1221) — not yet a reliable toolkit.
- Open question 1: For a hygiene polymer that crystallizes on cooling (PP, PET, PLA), can the chapter's metastable-zone / seeding / nucleation-rate framework be mapped quantitatively onto undercooling-driven spherulitic crystallization?
- Open question 2: Does the "≈1 mm optimum, >1 mm harmful" drying window (p.1218) translate to a granule-size band for SAP/actives where filtration, drying, and attrition are all acceptable?

## 11. Hygiene-material relevance & action cards

Overall relevance: ★★☆☆☆ (weak-to-moderate — not a drying process; value is conceptual transfer of nucleation/growth, supersaturation control, habit/polymorph thinking, and the size↔filterability↔drying trade-off to polymer crystallization and powder-product design).

Action Card H51-1 — Use the nucleation/growth lens for polymer crystallization on cooling. Insight: p.1203–1204 supersaturation drives nucleation vs growth; metastable-zone width sets nucleation ease; L₅₀ = 3.67 Gτ (Eq 51.8). Action: When specifying cooling of PP/PET/PLA (PoP Ch1/Ch7/Ch8), treat undercooling as the supersaturation analogue and use nucleating agents/seeds to set crystalline structure rather than accepting random spherulites. → 卫材相关性★★★｜Reframes polymer crystallisation as a controllable nucleation/growth problem.

Action Card H51-2 — Respect the ~1 mm sizing window for powders/granules. Insight: p.1218 crystals best ~1 mm+ but ">1 mm tend to be harmful" (centrifuge breakage, lost supersaturation surface). Action: Set SAP/actives granule-size spec inside a band where filtration, drying, and attrition are all acceptable rather than "as large as possible." → 卫材相关性★★★｜Concrete sizing-band lesson portable to powder-product specs.

Action Card H51-3 — Expect mother-liquor/solvent inclusions to raise impurity. Insight: p.1206 agglomeration "may contain inclusions of the mother liquor, which decreases the purity"; slow growth = purer. Action: For spray-crystallized or precipitated actives on a hygiene line, control growth rate and wash the cake to minimize trapped solvent (VOC/residual concern). → 卫材相关性★★☆｜Analogue of residual monomer/solvent in polymer particles.

Action Card H51-4 — Apply the Kozeny–Carman scale to fine-powder filtration. Insight: p.1216 "If the particle diameter drops to 10% of its original value, the pressure drop increases by 100-fold." Action: When a fine SAP/actives fraction is generated, anticipate a 100× filtration-pressure penalty and size the filter or coarsen the fraction accordingly. → 卫材相关性★★☆｜Quantifies why sub-10 µm fractions are costly to separate.

Action Card H51-5 — Note polymorphism thinking for solid-form actives. Insight: p.1206 polymorphism = same composition, different solid form/dissolution; supersaturation can select polymorph (p.1221). Action: If a hygiene actives ingredient crystallizes, document its polymorphic form and the cooling/solvent path that locks it in, to keep dissolution stable. → 卫材相关性★★☆｜Solid-form control concept, not a drying lever.

Note: No operational dryer-control or safety content here; pair this chapter with Ch49 (control) and Ch48 (safety) for the actual drying line, and with the PoP cross-reference below for the polymer-crystallization link.

## 12. Book-Map Quotes (Top representative quotes)

"The easy dewatering and drying of crystals requires that the crystals be of a uniform and sufficiently large size. This is, therefore, the major theme of this chapter." — p.1202 — the downstream-driven design goal that makes the chapter relevant to any powder product.
"Supersaturation is the main parameter in determining the rate of crystal growth and nucleation … the level of supersaturation is the main parameter that determines the agglomeration, shape, and purity of the crystals." — p.1203 — the single knob governing every attribute; the undercooling analogue for polymers.
"From the viewpoint of drying, it would be best that the crystals be large, within the range of about 1 mm or above … crystal sizes above approximately 1 mm tend to be harmful." — p.1218 — the sizing band that caps "bigger is better."

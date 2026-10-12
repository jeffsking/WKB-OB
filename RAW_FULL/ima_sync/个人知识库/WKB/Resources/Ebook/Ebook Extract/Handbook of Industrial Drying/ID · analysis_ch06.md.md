---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_cdbc847ae89f2d1c8ab4eaa915b1588b001a693ee6c0644e"
source_file: "ID · analysis_ch06.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch06.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch06.md.md

# Analysis of Chapter 6 — Indirect Dryers

Handbook of Industrial Drying, 4th ed. (Mujumdar, CRC Press)
Authors of chapter: Sakamon Devahastin and Arun S. Mujumdar
Target reader: hygiene-materials R&D (disposable diapers, wipes, absorbent cores, fluff-pulp procurement)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

## 1. Overview (范围、对象与定位)

Chapter 6 covers indirect (contact / conductive) dryers — equipment where the heating medium (steam, hot oil, molten salt, electricity) never touches the product; heat reaches the wet solids by conduction through a heated wall (p.135). This is the dryer class most relevant when (a) the product must stay hygienic/closed-system, (b) the material is heat-sensitive or solvent-wet, (c) emissions/fines must be near zero, or (d) you want the highest thermal efficiency. The chapter gives: definition + advantages/limitations (§6.1), selection tables by feedstock and duty (§6.2, Tables 6.1–6.3), a tour of five dryer families (§6.3: tray, steam-tube rotary, rotating-batch-vacuum, agitated, other), and a quantitative design/modeling section (§6.4, Eqs 6.1–6.37) built on the overall heat-transfer coefficient U and its five resistances.

For the hygiene reader this chapter is decisive: contact dryers are exactly how SAP granules, polymer flakes, and heat-sensitive nonwoven binders are dried in a closed, low-oxygen, low-emission environment — and the chapter contains the single most important polymer-science warning in the assignment (p.142: glass transition of the solid during contact drying).

Print-page span: p.135–p.148 (PDF p.156–169).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — Definition: conduction through a separating wall. (p.135)
> "Indirect (or contact or conductive) dryers... are dryers in which the heating medium (e.g., steam, hot gas, thermal fluids) does not come into contact with the product being dried. Instead, wet material is dried by contact with a heated surface; heat transfer to the wet material is mainly by conduction from this surface."
> "The temperature of heat transfer surfaces may range from 40°C (as in freeze drying) to about 300°C."

V2.2 — Higher energy efficiency, lower emissions, but higher capex. (p.135–136)
> "Generally, indirect dryers have higher energy efficiency than the direct dryers, because the energy lost through the exhaust gas stream is greatly reduced"
> "the typical energy consumption is in the range of 2800–3600 kJ/kg of water evaporated compared to direct dryers, which consume 4000–6000 kJ/kg of water evaporated."
> "indirect dryers have typically higher capital costs than equivalent direct dryers due to the need for heat exchange surfaces." (p.136)

V2.3 — Hygiene / low-emission advantage for sensitive products. (p.135–136)
> "Indirect dryers also need minimal cleaning of the exhaust gas as the exhaust flow is low... Additional relevant benefits are very low emission of fines and particles from the dryer; this is especially beneficial when drying toxic, explosive, flammable, or dusty products. Any vapors released can be condensed easily... Vacuum drying can also be accommodated easily... ideal for heat-sensitive materials such as foods, pharmaceuticals, and other biomaterials."
> "The final achievable moisture content of the product is also not limited by the state of the heating medium as in the case of direct dryers." (p.136)

V2.4 — Limitation: limited heat-transfer area and mostly batch. (p.136)
> "accompanying the above advantages... are several limitations such as their limited ability to enhance the drying rates due to their limited availability of the heat transfer areas, especially in large-scale equipment... Many types of indirect dryers can only be operated in batch mode; hence they have lower production capabilities than direct dryers."

V2.5 — Selection by feedstock and duty. (p.137, Tables 6.1–6.2)
> Table 6.1 maps dryer types (thin-film contact, cone batch, drum, steam-jacket rotary, tray batch/continuous) onto feed forms (solutions, slurries, pastes, powders, granules, fragile fiber). Table 6.2 scores Plate/Drum/Tumbling/Vibrating/Conical/Thin-film/Paddle/Mixer-kneader dryers on continuous/discontinuous, vacuum, surface/volume, capacity, friability, fluid/viscous/crusty handling.
> "An indirect dryer that uses high heat-source temperature should be operated in such a way that the residence time of the drying material within it is minimized" (p.137).

V2.6 — Tray dryers: shallow load, vacuum for heat-sensitive. (p.138–139)
> "each tray may be loaded up to a depth of about 40 mm giving a loading of approximately 40 kg of wet material/m² of tray area (Oakley, 1997)."
> "This type of dryers, along with the use of vacuum, is used extensively for drying heat-sensitive or easily oxidized materials. They are particularly well suited for materials, which require gentle handling and where material loss must be minimized. Hygroscopic materials may also be dried completely at temperatures lower than the maximum permissible temperatures of those materials." (p.139)

V2.7 — Steam-tube rotary: 70–90% efficiency, U = 30–85 W/(m²K). (p.140)
> "The length to diameter ratio of the rotating shell can vary from 4:1 to 10:1. Steam-heated tubes... typical steam pressure used may be in the range of 4–10 bar... Lifting flights are usually inserted behind the tubes to aid agitation."
> "The thermal efficiency of steam-tube dryers is in the range of 70–90%, if well insulated... Heat transfer coefficients in steam-tube dryers may range from 30 to 85 W/(m² K) and these values increase with increasing steam temperature due to an increased effect of radiation." (p.140)
> Table 6.4 gives performance data: e.g. Type-1 high-moisture organic (distillers' grains, citrus pulp): feed 223% d.b., product 11% d.b., heat load 4950 kJ/kg product, heating surface 0.34 m²/kg.

V2.8 — Vacuum rotating (double-cone): U ≈ 35, fouling drops to 5–10. (p.141)
> "The overall heat transfer coefficients of this type of dryer, which may vary near 35 W/(m² K)... The overall heat transfer coefficients may drop considerably if the dryer walls are fouled; the values in the range of 5–10 W/(m² K) are not uncommon." (p.141)

V2.9 — Agitated dryers: cone (≈60) and horizontal paddle (≈50 W/(m²K)). (p.142)
> "For design purposes the values of the heat transfer coefficients can be assumed to be around 60 W/(m² K) (Moyers and Baldwin, 1997)." (cone)
> "the overall heat transfer coefficients of this type of dryer... can be assumed to be around 50 W/(m² K)... However, higher values are expected for products that have surface moisture." (horizontal paddle, p.142)

V2.10 — Polymer glass-transition warning (the key POP sentence). (p.142)
> "Materials that may undergo glass transition over temperature ranges encountered may pose unexpected problems. In addition, significant differences between the heat transfer coefficients as well as thermal contact resistance between the wall and the material being heated may occur for pasty materials and materials that have tendency to form large lumps." (p.142)

V2.11 — Design core: Q = UAΔT with five resistances. (p.143, Eqs 6.1–6.2)
> "Q = UA(T₁ − T₂) (6.1) where Q is the heat transfer rate, U is the overall heat transfer coefficient, A is the heat transfer area, T₁ is the temperature of the heat transfer medium, and T₂ is the temperature of the drying particles."
> "1/U = 1/h_h + 1/h_w + 1/h_f + 1/h_m + 1/h_v (6.2)... there are indeed only two main resistances, i.e., the resistance between the wall and the surface of the bed of drying material (or contact resistance) as well as the resistance across the bed of drying material (or bulk penetration resistance)." (p.143)

V2.12 — Hygroscopic bound moisture enters via the isotherm slope. (p.146, Eq 6.32)
> "For hygroscopic materials the effect of bound moisture can be taken into account, for example in the case of vacuum drying, by the use of an effective heat capacity of the hygroscopic bed as (Tsotsas and Schlu¨nder, 1987) c_p,bed,h = c_p,bed + c_p,L X_h (∂X_h/∂T)_p (6.32)... where (∂X_h/∂T)_p is the slope of the sorption isobar and X_h is the bound moisture." (p.146)

V2.13 — Sizing by integral of 1/drying-rate. (p.146, Eqs 6.35–6.37)
> "I = ∫_{Xout}^{Xin} dX / m˙(X) (6.35)... For the calculation of the drying rates of granular beds... For a batch dryer this integral yields the product of the required contact surface area A and the required residence time t_dry: A·t_dry = M_dry·I (6.36). For a continuous dryer operating at a throughput M˙_dry the required contact area is A = M˙_dry·I (6.37)."

V2.14 — Constant vs falling rate dictates dryer choice. (p.146–147)
> "During the constant rate period, when heat transfer dominates the drying process, a dryer with a large heating surface is preferred. On the other hand, during the falling rate period when internal resistances control the rate of drying, a dryer that allows a longer residence time of the drying material within it is recommended." (p.147)

## 3. Research Method (研究方法)

This chapter is descriptive + semi-empirical design. Method:

- Define the contact-drying concept and enumerate advantages/limitations (§6.1).
- Select by feedstock form (Table 6.1) and duty matrix (Table 6.2), with residence-time range (Table 6.3).
- Characterize each dryer family (§6.3) with geometry, operating ranges, typical U values, and performance tables (6.4).
- Model via the generalized conduction equation Q = UAΔT (6.1) and the resistance network (6.2). The stirred/packed-bed heat-penetration theory (Eqs 6.3–6.8, mixing number 6.7) and Schlu¨nder packed-bed conductivity (6.16–6.24, Table 6.5) give U; radiation (6.14) and contact resistance (6.10) refine it.
- Handle hygroscopicity by the isotherm-slope effective heat capacity (6.32–6.34).
- Size by integrating 1/drying-rate (6.35–6.37) for batch or continuous contact area.
The hygiene reader applies step 4–6 with their own measured U (from a small heated-plate device, p.145 Lecomte et al.) and their own sorption isobar slope (from Ch.4 §4.6 GAB).

## 4. Argumentation (论证逻辑)

The chapter argues contact drying is the efficiency/purity choice with a wall-fouling and batch-throughput penalty:

- Premises: conduction isolates product from heating medium ⇒ low exhaust, low emissions, high efficiency (2800–3600 vs 4000–6000 kJ/kg), vacuum-compatible for heat/solvent-sensitive goods.
- Cost: needs heat-exchange surface ⇒ higher capex; limited area ⇒ lower rate/throughput; mostly batch.
- Design response: decompose U into 5 resistances (6.2), of which 2 dominate (contact + bulk penetration); correlate both from particle/bed physics (Schlu¨nder); size area via the 1/rate integral.
- Polymer caveat (the hidden premise): if the solid is near its glass transition, the "contact resistance" term blows up (sticking/fouling), so the elegant U-correlations fail — the material itself, not the geometry, becomes the limit. This is the bridge to polymer science (POP block).
## 5. Role of This Chapter in the Book (在全书中的角色)

Ch.6 opens Part II ("Description of Various Dryer Types", p.134) and is the first detailed dryer family chapter. It operationalizes Ch.4's k, h and Biot rules (conduction-controlled, Bi>1) and Ch.3's balances, and it is the dryer class most amenable to the Ch.5 spreadsheet (conduction instead of convection). For hygiene, it precedes the convective/through-circulation families the reader will more often use for webs, but it is the right tool for SAP granule drying, polymer flake/sludge drying, and any heat-sensitive binder.

## 6. Strengths and Weaknesses (贡献与局限)

Strengths
- Explicit energy-efficiency comparison (2800–3600 vs 4000–6000 kJ/kg) quantifies the contact-dryer advantage.
- Gives U values for every family (tray/vacuum ≈35, rotary 30–85, cone ≈60, paddle ≈50, drum 105–345 W/(m²K)) — directly usable for first sizing.
- The §6.4 resistance network (6.1–6.2) and 1/rate sizing integral (6.35–6.37) are genuine, reusable engineering tools.
- Contains the only glass-transition warning (p.142) in the assignment — the critical polymer-science flag for contact drying.

Weaknesses
- U correlations are particle/bed-centric (Schlu¨nder sphere models); little guidance for fibrous/mat hygroscopic solids (fluff pulp pad, nonwoven web) where contact is partial and anisotropic.
- Hygroscopic treatment (6.32) requires the sorption-isobar slope — which Ch.4 says is unmeasured for commercial polymers.
- Fouling/glass-transition is named but not modeled; no Tg-based design rule is given (left to the POP layer).
- Batch dominance limits throughput discussion; continuous contact dryers for high-rate hygiene lines are lightly covered.

## 7. Key Terms (关键术语)

||||
|---|---|---|
|Indirect/contact/conductive dryer|—|heating medium separated from product by a conducting wall (p.135)|
|Overall heat-transfer coeff.|U|from Q=UAΔT (6.1); W/(m²K)|
|Resistance network|1/U = Σ1/hᵢ|h_h wall-medium, h_w wall, h_f contact, h_m bulk, h_v evaporative (6.2)|
|Contact resistance|1/h_f|wall↔bed surface (dominant)|
|Bulk penetration resistance|1/h_m|across the bed of solids|
|Mixing number|N_mix|Eq 6.7, N_mix = C·Frˣ; governs stirred-bed U|
|Heat penetration coeff.|h_m|Eq 6.3, packed bed|
|Thermal efficiency|—|70–90% for steam-tube (p.140)|
|Bound moisture|X_h|hygroscopic water; enters via (∂X_h/∂T)_p (6.32)|
|Drying-rate integral|I|∫dX/m˙(X); sizes area (6.35–6.37)|
|Glass transition (warning)|Tg|p.142 — contact-drying failure mode for polymers|

## 8. Micro close-reading (微观精读)

8.1 — The 2800–3600 vs 4000–6000 kJ/kg line (p.136). This single comparison justifies contact drying on energy alone: ~30% less specific energy than convective dryers. For a SAP/flake drying line running continuous tonnes/h, that gap is the difference between viable and punitive opex.

8.2 — The five-resistance collapse (p.143). Eq 6.2 lists 1/h_h + 1/h_w + 1/h_f + 1/h_m + 1/h_v, but the text states only two dominate: contact (wall↔bed) and bulk penetration (across bed). For a hygiene granular product (SAP), the contact resistance is the one you can lose if particles soften and bridge the gap — which is exactly the glass-transition failure (8.3).

8.3 — The glass-transition sentence (p.142). "Materials that may undergo glass transition over temperature ranges encountered may pose unexpected problems." This is the chapter's most important clause for the hygiene reader. SAP (crosslinked sodium polyacrylate) and PP/PE binders each have a Tg; if the heated wall exceeds it, the particle softens, adheres, and the contact resistance (8.2) skyrockets — the U correlations (which assume rigid particles) no longer apply. The chapter names it but cannot explain it; the POP block does.

8.4 — Eq 6.32 hygroscopic effective heat capacity (p.146). c_p,bed,h = c_p,bed + c_p,L·X_h·(∂X_h/∂T)_p. The term (∂X_h/∂T)_p is the slope of the sorption isobar — i.e. the derivative of your Ch.4 GAB/Oswin isotherm (Eq T10.3 in Ch.5) with respect to temperature. This is the explicit mathematical bridge: contact-drying rate of a hygroscopic polymer = its isotherm derivative. SAP's steep isotherm slope (strong water binding) directly slows its contact-drying rate.

8.5 — Fouling collapses U by ~3–7× (p.141, Table 6.6). Clean double-cone U≈35; fouled drops to 5–10 W/(m²K). Table 6.6 shows h_f ranges 2.8 (dry solid) to 280 (50% paste) — a 100× spread driven purely by moisture/contact state. Design must use the dry/contact-limited value (the chapter advises using abundant dry-particle data for conservative estimates, p.146), which for a softening polymer is the glass-transition regime.

## 9. Concept deep-dive (概念深掘)

9.1 Conduction-dominated drying ⇒ Ch.4 Biot rule applies. Contact drying heats internally through the solid/mat, so Biₕ,Biₘ > 1 (Ch.4 p.89) and Fourier's law (Ch.4 Eq 4.4) governs — U here is the wall-side lump of that internal resistance. The hygiene reader sizes contact area from U (this chapter) and moisture removal from D/Xₑ (Ch.4).

9.2 The resistance network and where polymers fail. Eq 6.2's five terms reduce to contact (1/h_f) + bulk (1/h_m). For free-flowing glassy granules both are stable. As wall T → Tg of a polymer particle, the particle skin softens, conforms, then sticks — contact resistance first drops (better contact) then spikes (fouling layer, p.141). The net is non-monotonic and unpredictable without Tg knowledge.

9.3 Mixing number and stirred beds (Eq 6.7). N_mix = C·Frˣ with C,x from Table 6.5 (disc 25/0.20, rotary drum 16/0.20, paddle 9/0.05). This lets you predict U for an agitated contact dryer from rotation speed/Froude — useful when scaling a paddle dryer for sticky SAP/flake blends, provided the material stays below Tg.

9.4 Hygroscopic bound-moisture coupling (Eq 6.32–6.34). The effective heat capacity adds c_p,L·X_h·(∂X_h/∂T)_p. For a strongly binding polymer (SAP, cellulose), (∂X_h/∂T)_p is large near the isotherm knee, so the "thermal" model must carry the sorption thermodynamics. This is why Ch.4 §4.6 (GAB) and Ch.5 T10.3 are not optional for contact-dryer design — they feed Eq 6.32.

9.5 Sizing by the rate integral (Eq 6.35–6.37). Whether batch (A·t_dry = M_dry·I) or continuous (A = M˙_dry·I), the required contact area is the drying-rate integral. The rate m˙(X) itself follows the constant-rate → falling-rate split (p.147): large area for constant-rate, long residence for falling-rate. For SAP (falling-rate, internally controlled), you need long residence / low wall T — i.e. stay below Tg and accept lower throughput.

9.6 Energy and emissions case. 2800–3600 kJ/kg and near-zero fines/exhaust make contact drying the choice for closed-loop SAP solvent recovery or heat-sensitive binder drying; the penalty is capex (heat-exchange surface) and batch throughput. A hygiene plant drying SAP granules in inert (nitrogen) atmosphere at low O₂ is the textbook use case (p.135–136).

## 10. Critique (批判性评估)

- No fiber/mat model. The U and h_m correlations assume spherical/monodisperse particles (Schlu¨nder). A fluff-pulp pad or nonwoven web is an anisotropic fibrous mat with partial, evolving wall contact — the chapter's models do not cover it, and no correction factor is offered.
- Glass transition named, not solved. p.142 flags Tg as a problem but gives no Tg-based design rule, no safe-ΔT window, no stickiness index. The reader must import polymer science (POP block) to act on the warning.
- Hygroscopic coupling needs unmeasured data. Eq 6.32 requires (∂X_h/∂T)_p — the isotherm derivative — which (per Ch.4) is unavailable for commercial polymers. The method is correct but data-starved for hygiene materials.
- Throughput emphasis is batch-centric. Continuous contact dryers for high-rate hygiene lines (drum, thin-film) are mentioned but lightly quantified; Table 6.3 residence times (0–10 s thin-film to 1–6 h tray) show the spread but not how to hit a tonnes/h target.
- OCR noise. Equations 6.3–6.15 lost radicals/subscripts in OCR (e.g. "pffiffiffi" artifacts). Reconstructed from Schlu¨nder (1984) context; verify against print before use.
## 11. Hygiene-Material Relevance & Action Cards (卫材相关性与行动卡)

H11.1 — Use contact drying for SAP granules in inert/N₂ atmosphere. Action: SAP is heat-sensitive + dust-prone + benefits from closed, low-O₂, fume-recoverable drying (p.135–136). Select steam-tube rotary or agitated paddle; keep wall T below SAP's Tg to avoid sticking.

H11.2 — Honor the glass-transition warning (p.142). Action: measure/look up Tg of your SAP and PP/PE binder; set heated-wall temperature a safe margin below Tg; expect U to collapse if exceeded (fouling 5–10 W/(m²K), p.141). This is the single most common contact-dryer failure for polymers.

H11.3 — Size from the rate integral with your own U. Action: run a small heated-plate device (Lecomte et al., p.145) on your SAP/flake to get h_f; compute I = ∫dX/m˙(X); batch area A·t = M_dry·I (6.36) or continuous A = M˙_dry·I (6.37). Do not take U from the food/sludge tables blindly.

H11.4 — Feed GAB isotherm derivative into Eq 6.32. Action: differentiate your Ch.4 §4.6 GAB (or Ch.5 T10.3 Oswin) isotherm w.r.t. T to get (∂X_h/∂T)_p; plug into the hygroscopic effective heat capacity so the contact-drying rate of moisture-binding SAP is correct.

H11.5 — Exploit the 30% energy advantage for capex decisions. Action: compare contact (2800–3600 kJ/kg) vs convective (4000–6000) on opex; if energy and emissions dominate, accept higher heat-exchange capex (p.136) for a closed SAP/ binder dryer.

H11.6 — Match dryer to rate period (p.147). Action: SAP is falling-rate/internally-controlled ⇒ choose a contact dryer allowing long residence, low wall T (rotating vacuum, gentle paddle), not a large-area constant-rate machine.

H11.7 — Use vacuum for heat/solvent-sensitive webs. Action: tray or double-cone vacuum (U≈35, p.141) for nonwoven binder pre-drying or solvent-wet polymer flake; recover solvent via condenser (p.139). Watch fouling if the polymer approaches Tg mid-cycle.

## 12. Book-Map Quotes (本书脉络引证)

- Ch.4 (p.88–89): Fourier law & Biot rule (Bi>1 internal/conductive control) — the regime contact dryers operate in; k, D, Xₑ feed §6.4.
- Ch.4 §4.6 (p.100): sorption isotherm / GAB — its derivative is (∂X_h/∂T)_p in Eq 6.32 here.
- Ch.5 (p.125): T10.3 Oswin isotherm — differentiate for Eq 6.32; Ch.5 spreadsheet can host the §6.4 conduction model.
- Ch.3 (p.51): mass/energy balances — the Q=UAΔT (6.1) is the conductive counterpart to Ch.3's convective balances.
- Part II (p.134): "Description of Various Dryer Types" — Ch.6 is the first and most polymer-relevant family chapter.

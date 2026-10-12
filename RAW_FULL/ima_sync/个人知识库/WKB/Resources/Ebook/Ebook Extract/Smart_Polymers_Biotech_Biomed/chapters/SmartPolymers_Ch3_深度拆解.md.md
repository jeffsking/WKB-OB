---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_60a006b4585ccd132304e2122ea1b3e3001a693ee6c0644e"
source_file: "SmartPolymers_Ch3_深度拆解.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Smart_Polymers_Biotech_Biomed/chapters/SmartPolymers_Ch3_深度拆解.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# SmartPolymers_Ch3_深度拆解.md.md

# Chapter 3 — Conformational Transitions in Cross-Linked Ionic Gels: Theoretical Background, Recent Developments, and Applications

Source: Galaev, I. & Mattiasson, B. (eds.) Smart Polymers: Applications in Biotechnology and Biomedicine, 2nd Ed., CRC Press. Chapter by S. Starodubtsev, V. Vasilevskaya, A. Khokhlov.
Coverage of this deep-read report: L1–L1483 (chapter body; L1488+ = references).

## Module 1: Core Arguments

Volume phase transition (VPT) is the defining "smart" behavior. Stimulus-responsive gels undergo sharp, often discontinuous volume changes under small changes of pH, ionic strength, temperature, light, electric current, or mechanical force. VPT was first theoretically predicted by Dusek & Patterson and first experimentally observed by Tanaka (1979) for slightly cross-linked PAM gels in water–acetone; pronounced VPT requires low monomer concentration at synthesis, low cross-link density, and a fraction of charged monomer units. (L102–153)

Free-energy profile with two minima explains discontinuous collapse. For a neutral gel, collapse is possible only if there is chain attraction ($F{int} < 0$). Networks cross-linked in the melt give a single-minimum free energy; networks cross-linked in a large amount of good solvent have reference conformations near the coil/excluded-volume state, so both additional swelling and shrinking raise $F{el}$ — summing with $F_{int}$ produces a curve with two minima and a first-order-like transition. (L184–218)

A general four-term free-energy theory governs charged networks. The total free energy of a charged gel is $F = F{el} + F{int} + F{tr-en} + F{elect}$ (Eq 3.3). Three swelling regimes emerge depending on the noncompensated charge spacing $\sigma_1$: polyelectrolyte ($\sigma<\sigma_1<\sigma_2$, swollen, VPT far below $\Theta$), intermediate ($\sigma_2<\sigma_1<\sigma_3$, VPT above $\Theta$), and isoelectric ($\sigma_1>\sigma_3$, electrostatic attraction dominates → collapse even in polar media). (L277–443)

Polyampholytes exhibit an isoelectric-point minimum and antipolyelectrolyte behavior. PA gels (both cationic + anionic units) show a swelling-ratio minimum at equal +/− charge content; at the isoelectric point (IEP) salt increases swelling (antipolyelectrolyte behavior), opposite to normal polyelectrolyte collapse. (L448–548)

The ionomer effect (multiplet formation) is a second, independent route to strong collapse, and multivalent counterions dominate. Beyond osmotic-pressure-driven swelling, counterion–monomer Coulomb attraction forms ion pairs/multiplets that act as extra cross-links; low dielectric constant triggers a positive-feedback collapse. Divalent and trivalent counterions collapse gels at far lower concentrations than univalents, with reentrant reswelling at high salt. (L621–799, L803–960)

## Module 2: Key Concepts with Operational Definitions

### 1. Volume Phase Transition (VPT) — 体积相转变

- Definition (EN): Sharp, often discontinuous change of the gel volume triggered by a small change of an external parameter (pH, ionic strength, temperature, light, electric/magnetic field, mechanical force).
- Operational definition / measurement: Quantified by the swelling ratio $m/m_d$ (mass of equilibrium gel ÷ mass of dried gel) or the swelling coefficient $\alpha$. A sharp jump in $m/m_d$ versus the stimulus marks the transition (e.g., Figure 3.4 L872–881; Figure 3.5 collapse between $10^{-5}$–$10^{-4}$ M L948–950).
- Original excerpt: "Stimulus-responsive or 'smart' polymer gels undergo sharp, often discontinuous conformational transitions under small changes of external conditions, such as pH, ionic strength, the action of light, electric current, mechanical force, etc." (L102–104)
### 2. Free-Energy Profile with Two Minima — 双极小值自由能剖面

- Definition (EN): The total free energy $F(V)$ of a network as a function of gel volume can possess two local minima, giving a first-order-like volume phase transition.
- Operational definition / measurement: Construct $F = F{int} + F{el}$. $F{int} < 0$ (attraction, Figure 3.1a) summed with $F{el}$ curve 2 (network prepared in large amount of good solvent) yields two minima; criterion = synthesis in the presence of a large amount of good solvent so the reference state is near coil/excluded-volume (L207–218).
- Original excerpt: "the sum of the functions described by the curve in Figure 3.1a and curve 2 in Figure 3.1b will produce a curve with two minima." (L216–218)
### 3. Swelling Coefficient α — 溶胀系数

- Definition (EN): $\alpha$ is the linear swelling/deswelling coefficient of the network; the reference (preparation) state corresponds to $\alpha = 1$.
- Operational definition / measurement (judgment formula): From classic rubber elasticity,
$$F{el} = \frac{3NT}{m}\left(\alpha^2 + \frac{1}{\alpha}\right) \quad \text{(Eq 3.5, L337)}$$
Minimum at $\alpha=1$. Judge collapse/swelling by the deviation of $\alpha$ from 1; for melt-cross-linked networks swelling raises $F{el}$, for good-solvent-cross-linked networks both swelling and shrinking raise $F_{el}$ (L340–360).
- Original excerpt: "It is very important that the minimum of $F_{el}$ ($\alpha = 1$) corresponds to the reference state, which is usually the state that the network had under the preparation conditions." (L340–341)
### 4. Polyelectrolyte Gel vs Isoelectric Gel — 聚电解质凝胶 vs 等电凝胶

- Definition (EN): Polyelectrolyte gel = network carrying charges of one sign with freely moving oppositely charged counterions; isoelectric gel = network with equal numbers of + and − bound charges and no counterions.
- Operational definition / measurement (judgment formula): Classified by $\sigma_1$ = mean number of noncompensated charges per chain:

- polyelectrolyte: $\sigma_1 = \sigma$
- isoelectric: $\sigma_1 = \infty$
- general PA: $\sigma < \sigma_1 < \infty$ (L313–317)
- Original excerpt: "Such gels will be called polyelectrolyte gels. In the opposite case, when the number of positively and negatively charged ions of the network is equal and there are no counterions in the gel, the network will be called isoelectric gels." (L300–303)
### 5. Polyampholyte (PA) — 两性聚电解质

- Definition (EN): Polyions containing both cationic and anionic monomer units in the same network.
- Operational definition / measurement: Identified by presence of both sign charges; the swelling ratio reaches a minimum at equal + and − charge content (IEP), then rises (L476–479).
- Original excerpt: "Polyampholytes (PA) are the polyions containing both cationic and anionic monomer units." (L449)
### 6. Antipolyelectrolyte Behavior — 反聚电解质行为

- Definition (EN): Gel swelling increases with increasing low-molecular-weight salt concentration — the opposite of normal polyelectrolyte collapse.
- Operational definition / measurement: At the IEP, add NaCl → swelling ratio rises (L484–500). Measured as $m/m_d$ vs. [NaCl]. Holds for PAM/AMPS/zwitterion systems and PA gels in water, water–salt, and water–organic mixtures (L498–501).
- Original excerpt: "antipolyelectrolyte behavior was observed at the isoelectric point (IEP). The addition of low-molecular-weight salt resulted in the gel swelling." (L484–485)
### 7. Ionomer Effect — 离聚物效应

- Definition (EN): Interaction of counterions with oppositely charged monomer units forms ion pairs/multiplets that act as additional cross-links, shrinking the gel; amplified by a positive-feedback loop as polymer volume fraction rises and dielectric constant drops.
- Operational definition / measurement: Observed as sharp collapse in low-dielectric media; onset tied to a threshold degree of ionization during neutralization (L705–714); collapse is more pronounced for slightly charged gels and for highly charged networks (Manning condensation). Presence of multiplets evidenced by SAXS maxima (L647–651, L684–685).
- Original excerpt: "During the transition from polyelectrolyte to ionomer regime, the gel shrinks; the osmotic pressure of the counterions becomes smaller, and the multiplets begin to play the role of additional cross-links... the process is developing via the positive-feedback mechanism and leads to a strong gel collapse." (L653–685)
### 8. Multiplet (Ion-Pair Multiplet) — 离子多联体

- Definition (EN): Aggregates of contact ion pairs formed in low-dielectric-constant media; function as physical, additional cross-links of the network.
- Operational definition / measurement: Detectable by SAXS characteristic maxima in scattering curves. Reported aggregate sizes: dense Cu(II)–PSMA complexes $d = 8–18$ nm (L815–817); PDADMAC–hydrotype-yellow complex $d = 2.2$ nm (L957–958).
- Original excerpt: "The multiplet formation can be observed by small angle X-ray scattering (SAXS) when the characteristic maxima appear in the scattering curves." (L647–651)
### 9. Manning Condensation — 曼宁凝聚

- Definition (EN): Counterion condensation onto highly charged polymer chains, raising effective local charge density and reinforcing collapse.
- Operational definition / measurement: Becomes significant at high network charge density; "charging of the network due to change of pH or chemical modification... can induce gel collapse. For gels with a high charge density, the latter effect is increased due to Manning condensation of the counterions." (L695–698)
- Original excerpt: "For gels with a high charge density, the latter effect is increased due to Manning condensation of the counterions." (L697–698)
### 10. Polyelectrolyte Gel–Surfactant Complex (PSC) — 聚电解质凝胶-表面活性剂复合物

- Definition (EN): Complex formed when oppositely charged surfactant ions act as counterions; hydrophobic aggregation of surfactant ions inside the gel causes sharp collapse and often highly ordered supramolecular structures.
- Operational definition / measurement: Collapse upon adding the oppositely charged surfactant; SAXS sharp peaks (L893–897). PSCs can be dissociated remotely (surfactant–surfactant complex more stable than PSC) causing the two gels to swell and, if in direct contact, to glue together (L916–923).
- Original excerpt: "The formation of polyelectrolyte gel–surfactant complexes (PSC) is accompanied by an aggregation of surfactant ions in the gel phase due to hydrophobic interactions and gel collapse." (L893–895)
### 11. Amphiphilic Co-networks (APCN) — 两亲共网络

- Definition (EN): Cross-linked polymers with covalently bonded, otherwise immiscible hydrophilic and hydrophobic chains; chemically bonded so they undergo nanophase (not macro) separation and swell in both hydrophilic and hydrophobic solvents.
- Operational definition / measurement: Swelling in both solvent types; nano-phase-separated morphology verified by architecture; examples PMAA-PIB and PHEMA-PIB polyelectrolyte APCNs show reversible pH-responsive behavior (L1081–1104).
- Original excerpt: "APCNs are new materials composed of covalently bonded and otherwise immiscible hydrophilic and hydrophobic polymer chains." (L1083–1085)
### 12. Gel–Clay Nanocomposite / Superabsorbent — 凝胶-黏土纳米复合材料 / 超吸水性材料

- Definition (EN): Hydrogel loaded with dispersed layered clays (e.g., montmorillonite, MONT) that combines gel elasticity/permeability with the clay's high adsorption capacity; durable → usable as superadsorbents.
- Operational definition / measurement: Clay surface area up to 800 m²/g (L1203–1204); platelet dimensions ≈30 nm (lateral) × ≈1 nm (thick) (L1201–1203); responsiveness judged by sensitivity to ionic strength, pH (Si–O⁻ ionization), cationic surfactants, polycations, and drugs (L1245–1266).
- Original excerpt: "Their durable properties make them suitable for use as superadsorbents." (L1197–1199)
## Module 3: Evidence Tables

### Table 3.1 — Three swelling regimes of charged networks (theory)

Source: L388–405 (Fig. 3.2). $\sigma_1$ = mean number of noncompensated charges per chain.

|||||
|---|---|---|---|
|1. Polyelectrolyte|$\sigma < \sigma_1 < \sigma_2$|$F_{tr-en}$ (counterion osmotic) dominates|Strongly swollen in polar solvents; collapses as VPT at $T \ll \Theta$|
|2. Isoelectric|$\sigma_1 > \sigma_3$|Electrostatic attraction dominates|Few counterions → collapse even in polar media|
|3. Intermediate|$\sigma_2 < \sigma_1 < \sigma_3$|$F{elect} \approx F{tr-en}$|VPT at $T > \Theta$|

### Table 3.2 — Factors favorable for a pronounced volume phase transition

Source: L150–153.

|||
|---|---|
|Monomer concentration at synthesis|low|
|Cross-linked density|low|
|Charged monomer unit fraction|some (nonzero)|

### Table 3.3 — Dielectric constant of solvent vs swelling of slightly charged AAM-SA gel

Source: L704–707. Collapse occurs earlier in lower-$\varepsilon$ media.

||||
|---|---|---|
|Methanol|32.6|highest|
|Ethanol|24.3|medium|
|Dioxane|2.2|lowest (collapse occurs earliest)|

### Table 3.4 — Swelling ratio $m/m_d$ vs salt concentration (Figure 3.4 data)

Source: L872–890. PAMPS gel unless noted; $m$ = equilibrium mass, $m_d$ = dried mass.

||||||
|---|---|---|---|---|
|NaCl (PAMPS)|moderate shrink|—|univalent|
|CaCl₂ (PAMPS)|stronger shrink than univalent|—|divalent, much stronger|
|Cu(NO₃)₂ (PSA gel)|collapse|reswell|bridge formation then competition|
|Co hexamine trichloride (PAMPS)|collapse|reswell (~0.3 M)|trivalent cation, no sulfonate complex|
|FeCl₃ (PAMPS)|collapse|reswell|trivalent cation|

### Table 3.5 — Montmorillonite (MONT) clay platelet properties

Source: L1201–1204. Basis for superabsorbent nanocomposites.

|||
|---|---|
|Platelet lateral size|≈ 30 nm|
|Platelet thickness|≈ 1 nm|
|Specific surface area|up to 800 m²/g|
|Surface charge|negative (Si–O⁻ on surface)|

### Table 3.6 — Counterion valence effect on collapse threshold

Source: L434–443.

|||
|---|---|
|Univalent (Na⁺, K⁺)|collapse needs higher concentration|
|Bivalent (Ca²⁺, etc.)|collapse at much smaller concentration than univalent|
|Trivalent (Fe³⁺, Co-hexamine³⁺)|collapse at low conc.; reentrant reswell at high conc. (≈0.3 M)|

## Module 4: Chapter Connections

### 4.1 Mechanism differences vs the baseline (simplest neutral gel) used in this chapter

Note: The prior chapter is not included in this workspace, so the "mechanism difference" is drawn from the chapter's own baseline contrast — Section 3.2.1 (neutral gel) vs Section 3.2.2 (charged ionic gel). Prior-chapter-specific claims are marked [未找到原句/行号缺失].

|||
|---|---|
|Free energy|$F = F{int} + F{el}$ (Eq 3.1, L196)|$F = F{el} + F{int} + F{tr-en} + F{elect}$ (Eq 3.3, L322)|
|Collapse driver|Short-range attraction only ($F_{int}$)|Attraction + electrostatic term + counterion osmotic pressure|
|Reference state|$\alpha=1$ (preparation state)|$\alpha=1$ but preparation in good solvent → two-minimum profile (L207–218)|
|Two minima?|Only if cross-linked in good solvent (curve 2)|Inherent via counterion/electrostatic terms; polyelectrolyte/intermediate/isoelectric regimes (L388–405)|
|Salt response|Not addressed|Strong suppression of swelling; divalent > univalent (L431–443)|

### 4.2 Connection points to other chapters (cross-references inside Ch3)

- Chapter 6 — "Protein-Based Smart Polymers": polypeptide elastin networks (L1059) and macroporous stimulus-responsive gels (L1175) are deferred to Ch6; the biopolymer + synthetic macromolecule trend is the modern direction (L1481–1483).
- Chapter 7 — "Imprinting Using Smart Polymers": metal-ion "imprinting" of PA gels (L594–602) and molecular imprinting in PAM–MONT nanocomposites (L1210–1215) are elaborated in Ch7.
### 4.3 Cross-chapter formula / concept links

- Free-energy extension: Eq 3.1 ($F = F{int} + F{el}$) is generalized to Eq 3.3 ($F = F{el} + F{int} + F{tr-en} + F{elect}$); the elastic term is the same classic rubber-elasticity expression (Eq 3.5; de Gennes scaling, ref 15 L1537).
- $\Theta$-point / coil–globule link: $B \approx a^3\tau,\; C \approx a^6$ with $\tau=(T-\Theta)/T$ (Eq 3.2, L310) connects gel VPT to the single-macromolecule coil–globule transition (Lifshitz et al. ref 6; Dusek & Patterson ref 5, L138–140).
- Swelling coefficient $\alpha$ and regimes (Fig. 3.2, L404–425) are reused whenever later chapters discuss thermo/pH-responsive collapse amplitudes.
## Module 5: Business Connections (Hygiene / Sanitary Materials R&D)

Target domain: baby diapers, sanitary pads, adult incontinence; SAP (superabsorbent polymers), nonwovens, adhesives, smart packaging, sensing.

5.1 SAP swelling physics → counterion osmotic pressure
- Chapter + concept: Ch3 §3.2.2, counterion translational entropy $F{tr-en}$ (L361–372).
- Key formula/data: $F{tr-en}/T = (N/\sigma_1)\ln(n/\sigma_1)$ (Eq 3.6, L364–366); in salt-free polar media charged-network volume can be 2–3 orders of magnitude higher than neutral gel (L428–430).
- Action: Model new SAP grades as charged networks; maximize noncompensated charge spacing $\sigma_1$ (i.e., free counterion fraction) to raise osmotic swelling pressure without external salt.

5.2 Urine / body-fluid ions → VPT threshold
- Chapter + concept: Ch3 §3.2.2 & §3.5, divalent/trivalent counterion collapse (L434–443, L831–890).
- Key formula/data: "bivalent counterions initiate collapse of the gels at much smaller concentrations than do univalent ions" (L441–443); Ca²⁺/Fe³⁺ collapse PAMPS at low conc. then reswell at ~0.3 M (L881–890).
- Action: Account for Ca²⁺/Mg²⁺ in urine when specifying SAP free-swell capacity and gel-bed stiffness; expect reversible stiffening at high ionic load (reentrant reswelling).

5.3 High-saline body fluids → antipolyelectrolyte PA behavior
- Chapter + concept: Ch3 §3.3, antipolyelectrolyte behavior at IEP (L484–500).
- Key formula/data: At IEP, increasing NaCl increases swelling ratio (L484–500).
- Action: Explore PA-type superabsorbents for high-electrolyte fluids (sweat, urine) where conventional anionic SAP loses capacity — a PA composition could gain capacity with salt.

5.4 Clay-based superabsorbents → SAP replacement / booster
- Chapter + concept: Ch3 §3.7, gel–clay nanocomposite / superabsorbent (L1182–1204).
- Key formula/data: Montmorillonite surface up to 800 m²/g; platelets ≈30 nm × ≈1 nm; composites are durable superadsorbents (L1197–1204); AM-DADMAC-clay shows antipolyelectrolyte swelling with salt (L1252–1254).
- Action: Pilot MONT-loaded SAP composites to cut polyacrylate content (cost + biodegradability) while retaining uptake; leverage 800 m²/g adsorption for odor/NH₃ binding.

5.5 Fast uptake / rewet → macroporous & imprinted architectures
- Chapter + concept: Ch3 §3.6, macroporous gels (L1163–1176) and colloidal-crystal-imprinted mesoporous gels (L1301–1310).
- Key formula/data: BAM (N,N′-methylenebisacrylamide) macroporous PNIPAM with pore radius ≈ 0.1 mm (L1165–1166); silica-templated periodic pores give fast temperature response (L1305–1310).
- Action: Translate macroporosity (pore radius ~0.1 mm) and ordered pores into SAP for faster acquisition rate and lower rewet; relevant to thin-core diaper designs.

5.6 Ionic-strength / pH sensing → smart packaging & wetness indicators
- Chapter + concept: Ch3 §3.5 (PSC, L893–923), §3.8.2 thermochromic/responsive indicators (L1418–1434).
- Key formula/data: PSC collapse + SAXS ordering (L893–897); thermochromic gels with DTPP / cresol red shift color via proton-dissociation equilibrium (L1418–1425); PNIPAM/PVME thermotropic windows switch optically (L1426–1434).
- Action: Develop low-cost wetness indicators (color shift on ionic-strength/pH jump of urine) and smart-packaging freshness cues using PSC or thermochromic hydrogel patches on pads/diapers.

5.7 Glucose / biomarker-sensitive membranes → diagnostic hygiene
- Chapter + concept: Ch3 §3.8.1, glucose-sensitive dextran/Con A membrane (L1374–1382) and NAD⁺-displacement lysozyme membrane (L1383–1390).
- Key formula/data: 0.1 M D-glucose substantially increases diffusion of insulin & lysozyme; glycerol / L-glucose controls show no effect (L1379–1382).
- Action: Adapt competitive-binding hydrogel membranes as point-of-care urine metabolite indicators embedded in adult-incontinence products.

5.8 Adhesion & actuation → tabs and smart fastening
- Chapter + concept: Ch3 §3.5 (PSC contact gluing, L922–923) and §3.8.2 electric-field-bending IPN (alginate/PDADMAC) (L1444–1448).
- Key formula/data: Oppositely charged PSC gels "glue together like oppositely charged polyelectrolyte gels" on contact (L922–923); IPN bends under applied electric field (L1447–1448).
- Action: Investigate PSC-based resealable diaper-tab adhesives and electrically tunable stiffening for adaptive-fit closures.

5.9 Actuator water transport → "smart" fluid handling
- Chapter + concept: Ch3 §3.8.2, osmotic water transport in charged gels (L1435–1443).
- Key formula/data: "one elementary charge can move up to 10⁴ molecules of water from the gel" (L1442–1443).
- Action: Benchmark energy-per-volume fluid pumping of hydrogel actuators vs current ADL (acquisition-distribution layer) nonwoven wicking for next-gen fluid management.

### Formulas / data directly usable for process-parameter selection

- Swelling-ratio metric: $m/m_d$ (equilibrium mass ÷ dry mass) — standard QC metric (L872–881, L948–950).
- Elastic reference: $F_{el} = \frac{3NT}{m}\left(\alpha^2 + \frac{1}{\alpha}\right)$ (Eq 3.5, L337) → choose cross-link density $1/m$ for target $\alpha$.
- Counterion osmotic term: $F_{tr-en}/T = (N/\sigma_1)\ln(n/\sigma_1)$ (Eq 3.6, L364–366) → maximize free counterion fraction $\sigma_1$ for higher SAP swelling pressure.
- Valence rule: bivalent counterions collapse at much smaller concentration than univalent (L441–443) → design for Ca²⁺/Mg²⁺ tolerance.
- Reentrant reswelling: collapse at low [multivalent salt], reswell near ~0.3 M (L881–890) → set fluid-load上限 before capacity recovers.
- Dielectric effect: swelling order methanol($\varepsilon$=32.6) > ethanol(24.3) > dioxane(2.2) (L704–707) → solvent/plasticizer choice shifts VPT.
- Ionization threshold: degree of ionization > 0.4 triggers reswelling of PAA (L739–741) → neutralization window in SAP manufacture.
- Antipolyelectrolyte: swelling rises with NaCl at IEP (L484–500) → formulate PA-SAP for saline fluids.
- Clay loading: montmorillonite surface up to 800 m²/g (L1203–1204) → adsorption/binding budget for odor control.
- Macroporosity: pore radius ≈ 0.1 mm BAM/PNIPAM (L1165–1166) → acquisition-rate target for thin-core SAP.
- LCST tuning: PNIPAM-based hybrid LCST adjustable to body temperature ~37 °C (L1065–1068) → indicator trigger temperature.
- Multivalent dye/ion collapse window: collapse region $10^{-5}$–$10^{-4}$ M, reswell at high conc. (L949–955) → sensitivity range for sensors.

## Module 6: Key Quotes Index

L102–104 — "Stimulus-responsive or 'smart' polymer gels undergo sharp, often discontinuous conformational transitions under small changes of external conditions, such as pH, ionic strength, the action of light, electric current, mechanical force, etc."
中文：刺激响应或"智能"聚合物凝胶在pH、离子强度、光、电流、机械力等外部条件的微小变化下，会发生剧烈且常不连续的构象转变。
Why remember: 这是全章对"smart gel"的定义性开篇，界定了后续所有机理的触发条件。

L136–137 — "The most striking feature of stimulus-responsive gels is their ability to undergo volume phase transition."
中文：刺激响应凝胶最显著的特征，是它们能够发生体积相转变。
Why remember: 点明体积相转变（VPT）是智能凝胶的核心标志，全章围绕它展开。

L141–143 — "The volume phase transition was first experimentally observed for slightly cross-linked poly(acrylamide) (PAM) gels swollen in water–acetone mixtures by Tanaka in 1979."
中文：体积相转变最早由Tanaka于1979年在溶胀于水-丙酮混合溶剂中的轻度交联聚丙烯酰胺（PAM）凝胶中实验观察到。
Why remember: 关键史实与模型体系（PAM + 少量电荷单体），是实验起点的基准。

L150–153 — "the factors favorable for the pronounced volume phase transition are: a low concentration of monomers at synthesis, a low cross-linked density, and the presence of some fraction of the charged monomer units in the network."
中文：有利于显著体积相转变的因素是：合成时单体浓度低、交联密度低，以及网络中存在一定比例的带电单体单元。
Why remember: 三条可直接用于配方设计的工艺准则（浓度/交联/电荷），高度可操作。

L196 — "$F = F{int} + F{el}$" (Eq 3.1)
中文：凝胶自由能 = 体积相互作用自由能 + 弹性自由能。
Why remember: 最简自由能分解，是后续四项式（Eq 3.3）的基础。

L322 — "$F = F{el} + F{int} + F{tr-en} + F{elect}$" (Eq 3.3)
中文：带电网络总自由能 = 弹性项 + 体积相互作用项 + 抗衡离子平动熵项 + 静电项。
Why remember: 全章理论骨架，四个贡献项分别解释溶胀、收缩、渗透压与静电坍塌。

L449 — "Polyampholytes (PA) are the polyions containing both cationic and anionic monomer units."
中文：两性聚电解质（PA）是同时含有阳离子和阴离子单体单元的多离子。
Why remember: 定义两性网络，引出等电点与反聚电解质行为。

L484–485 — "antipolyelectrolyte behavior was observed at the isoelectric point (IEP). The addition of low-molecular-weight salt resulted in the gel swelling."
中文：在等电点（IEP）观察到反聚电解质行为：加入低分子盐反而使凝胶溶胀。
Why remember: 反直觉现象，对高盐体液（尿/汗）下的SAP设计有直接启发。

L645 — "The charged network is thus in the polyelectrolyte regime of swelling."
中文：因此该带电网络处于聚电解质溶胀区。
Why remember: 区分聚电解质区与离聚物区，是理解盐响应与坍塌的枢纽。

L684–685 — "the process is developing via the positive-feedback mechanism and leads to a strong gel collapse." (ionomer effect)
中文：该过程通过正反馈机制发展，并导致凝胶的强烈坍塌。
Why remember: 离聚物效应的本质——低介电→多联体→更强坍塌的自放大回路。

L697–698 — "For gels with a high charge density, the latter effect is increased due to Manning condensation of the counterions."
中文：对于高电荷密度的凝胶，由于抗衡离子的曼宁凝聚，该效应会增强。
Why remember: 高电荷密度下坍塌被放大的机理，关联SAP电荷密度上限。

L833–835 — "in the case of multivalent cations, even in a polar medium, the electrostatic attraction of univalent monomer units of the charged polymer to the cations with valence 3 or higher is very strong, and $e\psi > kT$."
中文：对于多价阳离子，即使在极性介质中，带电聚合物单元与三价及以上阳离子的静电吸引也非常强，且 $e\psi > kT$。
Why remember: 多价离子（如尿中的Ca²⁺/Fe³⁺）强效坍塌的定量判据。

L1197–1199 — "Their durable properties make them suitable for use as superadsorbents."
中文：它们耐久的特性使其适合用作超吸水性材料。
Why remember: 凝胶-黏土纳米复合材料与SAP使命直接对接的关键一句。

L1442–1443 — "one elementary charge can move up to $10^4$ molecules of water from the gel."
中文：一个元电荷可从凝胶中驱动多达 $10^4$ 个水分子。
Why remember: 量化凝胶电驱动水传输效率，是执行器/流体管理的能量基准。

L1475–1477 — "This chapter has reviewed the state of investigation in the field of polyelectrolyte smart gels, a field that has been intensively developed over the past 30 years. The main features of polyelectrolyte-gel behavior are well understood..."
中文：本章综述了聚电解质智能凝胶领域的研究现状——该领域在过去30年迅速发展，聚电解质凝胶行为的主要特征已得到较好理解。
Why remember: 章节结论，确认理论成熟度，为工程化应用（含卫生材料）提供信心背书。

End of deep-read report. All line numbers refer to /sandbox/workspace/Ebook_Extract/Smart_Polymers_Biotech_Biomed/chapters/ch3.txt. Claims without a verifiable source line are marked [未找到原句/行号缺失].

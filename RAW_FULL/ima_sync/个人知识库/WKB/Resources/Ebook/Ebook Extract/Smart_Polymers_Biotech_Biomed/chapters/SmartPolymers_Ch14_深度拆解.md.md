---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_f6be12184559654614a78d5d1e92b6d0001a693ee6c0644e"
source_file: "SmartPolymers_Ch14_深度拆解.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Smart_Polymers_Biotech_Biomed/chapters/SmartPolymers_Ch14_深度拆解.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# SmartPolymers_Ch14_深度拆解.md.md

# Chapter 14 — Hydrogels in Microfluidics

Author (verified, line 5): Jaisree Moorthy
Source file: /sandbox/workspace/Ebook_Extract/Smart_Polymers_Biotech_Biomed/chapters/ch14.txt
Line range covered: 1–1220 (chapter body 1–1019; Acknowledgment 1024–1027; References 1032–1220; the book Index begins at line 1231 — Ch. 14 is the final chapter of the book)
Printed page span (from the chapter TOC, lines 10–26): pp. 437–457
Note on formulas: the chapter contains no numbered equations; all "formulas" below are explicitly labelled as reconstructions of textual scaling statements. [原文无公式编号]

## Module 1: Core Arguments

Hydrogels are the enabling material for autonomous microfluidics because they are simultaneously soft (good sealing, biomimetic) and responsive (self-sensing). Earlier silicon/glass devices suffered "the long fabrication process and the difficulty in obtaining good seals (for valves)"; PDMS solved softness but still "external methods such as pneumatic, electric, and magnetic signals were required to control … the microfluidic components." Hydrogels remove the external controller: "these materials can sense the local environment and undergo phase transition, such as an abrupt swelling." (lines 125–135; motivation lines 53–60)

The core functional mechanism is chemo-mechanical transduction by volume phase transition — up to a 1000-fold volume expansion that generates usable mechanical force. "The volume expansion, which can be as high as 1000-fold, can produce a mechanical force, resulting in transduction from a chemical stimulus to a mechanical action (as in muscles), and this force has been exploited in designing valves and pumps." (lines 146–154)

Component performance is a designable trade-off between response time and mechanical stability, governed by a defined parameter space (geometry/size, pore size and distribution, chain elasticity, cross-link density, distribution of ionizable groups, side-chain and cross-link chemistry). Extent of swelling is limited by chain elasticity + cross-link density; rate of swelling is diffusion-limited and depends on initial size, diffusion constant and pore size. (lines 167–190, Figure 14.1 caption lines 215–219)

Composition and polymerization rate are the two practical tuning knobs, and they pull response time and strength in opposite directions. Pure HEMA is nonresponsive; adding acrylic acid makes it pH-responsive; increasing UV intensity gives "a large number of small polymer chains … The response time of such a structure is improved …, while the mechanical strength of the structure is compromised." (lines 250–259)

The same material family covers the whole device chain — sensing, valving, pumping, clutching, optics, active assembly and separation — and can be integrated in situ ("microfluidic tectonics", Lego-block paradigm), producing a multiscale molecular→nano→micro→macro functional hierarchy. Demonstrated end product: an integrated device detecting botulinum neurotoxin from whole blood (porous filter + one-way check valves + antibody-coated agarose beads). (applications overview lines 383–391; integration lines 934–994)

Durability is the principal unsolved engineering weakness: hydrogel parts are co-fabricated "along with other rigid materials that are not able to withstand repeated cycles (greater than ten). This mismatch results in delamination of channels and other complications." (lines 178–184)

## Module 2: Key Concepts with Operational Definitions

1. 芯片实验室 / Lab on a chip (microfluidic device)
- Definition (operational): A microfabricated device that downsizes laboratory workspace and transports/manipulates nanoliter-to-microliter fluid volumes through micron-sized conduits; its essential components are valves and pumps (transport), filters (sample preparation) and sensors (detection), and it is made by microfabrication techniques that permit mass production and point-of-care use.
- Excerpt: "Efficient transport and manipulation of small volumes (nanoliters to microliters) of fluids is a necessity in these devices; hence they are also called microfluidic devices." (lines 35–37, 53) + "The essential components of a microfluidic device include valves and pumps to transport fluid efficiently through microchannels, filters for sample preparation, and sensors for detection." (lines 121–123)

2. 层流与扩散限制混合 / Laminar flow and diffusion-limited mixing
- Definition (operational): At the microscale viscous forces dominate over inertial forces, so flow "is free of fluctuations and is predictable"; adjacent streams do not turbulently mix — particles "redistribute via diffusion," so mixing time scales with particle size and concentration gradients can be created on purpose. Test of the definition: larger particles take longer to mix (line 705).
- Excerpt: "viscous forces dominate at the microscale, as opposed to inertial forces at the macroscale. … The fluid flow in microchannels is described as laminar flow, as it is free of fluctuations and is predictable. Particles in adjacent laminar streams redistribute via diffusion." (lines 69–75; consequence restated lines 703–707)

3. 表面积/体积比 / Surface-to-volume ratio (S/V)
- Definition (operational): The ratio that "increases dramatically" on going from a large vessel to a microdevice, with three measurable consequences: (i) more particles contact the channel wall/detector → better detection; (ii) fast heat dissipation → good against Joule heating in electrokinetic systems; (iii) fast heat loss → problem when high temperature is needed (e.g., PCR).
- Excerpt: "In going from a large vessel to a microfluidic device, the surface-to-volume ratio increases dramatically … A high ratio of surface area to volume is beneficial in detection because more particles can make contact with the detector. Quick heat dissipation is another consequence …" (lines 91–97, 110–111)

4. 水凝胶 / Hydrogel
- Definition (operational): "Polymers with high water content" whose chains are "cross-linked into a network to form a porous sieve-like structure that can be used to separate particles based on size (e.g., gel electrophoresis)"; the hydrophilic interior "preserves the integrity of cells and biomolecules," hence use in tissue engineering and drug delivery.
- Excerpt: "Hydrogels are polymers with high water content. The polymer chains are cross-linked into a network to form a porous sieve-like structure …" (lines 141–146)

5. 体积相变 / 化学-机械转换 / Volume phase transition & chemo-mechanical transduction
- Definition (operational): The responsive subclass of hydrogels changes volume abruptly on exposure to pH, temperature, electric or magnetic fields, or specific chemicals/biomolecules; the expansion — "as high as 1000-fold" — produces mechanical force, i.e., a chemical input is converted to mechanical output "as in muscles."
- Excerpt: "A subclass of hydrogels includes polymers that can undergo phase transition in the presence of stimuli such as pH, temperature, electric or magnetic fields, and specific chemicals (or biomolecules). … The volume expansion, which can be as high as 1000-fold, can produce a mechanical force …" (lines 146–154)

6. 响应时间参数空间 / Response-time parameter space (Figure 14.1)
- Definition (operational): The measurable design variables that jointly fix the response time and the stimulus type of a hydrogel component: component geometry (size, shape), pore size and distribution, chain elasticity / distance between cross-links, cross-link type and density, side-chain type and density, and the distribution of ionizable chemical groups.
- Excerpt: "Parameter space governing the property of hydrogel. The geometry of the final component, pore size of the matrix, chain elasticity, cross-link density, and distribution of ionizable chemical groups, determines the response time. The chemical groups on the side chains and at the cross-linking positions determine the type of the stimuli." (Figure 14.1 caption, lines 215–219; body statement lines 167–177)

7. 交联密度 / Cross-link density
- Definition (operational): The network parameter that (a) limits the extent of swelling together with chain elasticity, (b) sets the rate of degradation of cleavable gels ("less-cross-linked structures degrade faster"), and (c) is therefore the knob used to program response time of a peptide–hydrogel sensor; also a listed pore-size control variable in emulsion photopolymerization.
- Excerpt: "The extent of swelling is limited by the elasticity of the polymer chains and the cross-link density." (lines 168–169) + "The degree of degradation depends on the cross-link density of the hydrogel, i.e., less-cross-linked structures degrade faster." (lines 476–477)

8. 原位光聚合 / In-situ photopolymerization
- Definition (operational): Fabrication route in which a prepolymer mixture (monomer + cross-linker + photo-initiator) is introduced into a microchannel cavity and irradiated with UV through a transparency mask; exposed regions polymerize into 3-D structures, unpolymerized mixture is flushed and the channel washed — giving free choice of component location inside the channel labyrinth.
- Excerpt: "In photopolymerization, the hydrogel structures are fabricated from a prepolymer mixture consisting of a monomer, cross-linker, and a photo-initiator. The mixture is introduced into a cavity of a microfluidic channel and irradiated with UV light through a transparency mask." (lines 237–245)

9. 预聚体配方 / Prepolymer mixture (constituents and functions, Table 14.1)
- Definition (operational): The recipe whose six constituent classes each carry a defined function: monomer (main framework, primary properties such as surface energy), cross-linker (mechanical strength, durability, responsiveness), co-monomer (additional properties, e.g., responsiveness), initiator (starts polymerization), co-initiator (mediates energy transfer from initiator to monomer), porogen (creates pores, e.g., filters made by emulsion photopolymerization).
- Excerpt: "List of Prepolymer Constituents and Their Function during Polymerization or in the Final Hydrogel Structure … Cross-linker — Added for mechanical strength, durability, and responsiveness" (Table 14.1, lines 356–367)

10. 梯度水凝胶 / Gradient hydrogel
- Definition (operational): A hydrogel with internal spatial gradients of properties (e.g., porosity from different cross-linking densities, or co-monomer concentration), made by first generating a gradient in one prepolymer constituent with a T-junction or gradient generator and then polymerizing; verified by asymmetric swelling in the presence of the stimulant (pH).
- Excerpt: "These hydrogels have internal spatial gradients of properties such as porosity due to different cross-linking densities or co-monomer concentrations." (lines 275–278) + "In the presence of the stimulant (pH), asymmetry in swelling and in the final structure was observed." (line 371)

11. 可溶解/可酶切水凝胶传感器 / Dissolvable & enzymatically cleavable hydrogel sensor (responsive cross-linker)
- Definition (operational): A sensor made "by designing a cross-linker that is responsive to a specific chemical or a biomolecule," so that recognition destroys the network and produces a visible physical change. Rate-controlling variables are explicitly listed: initial hydrogel diameter, reducing-agent concentration, cross-link density, temperature. Chemistry examples: disulfide cross-linker N,N′-cystamine-bisacrylamide (cleaved by DTT/glutathione); peptide cross-linkers Cys-Tyr-Lys-Cys (chymotrypsin) and a 19-mer (botulinum neurotoxin), coupled via disulfide exchange through an included cysteine.
- Excerpt: "The factors that affect the rate of dissolution are: the initial diameter of the hydrogel, concentration of the reducing agent, cross-link density, and temperature." (lines 423–425; sensor principle lines 414–418; peptide cross-linkers lines 425–428, 470–475)

12. 乳液光聚合大孔整体柱 / Emulsion photopolymerization → macroporous monolith
- Definition (operational): Agitating a mixture of monomer + cross-linker + photo-initiator + porogen (e.g., water) creates an emulsion of monomer droplets in water; UV polymerization inside the channel yields "a contiguous polymer network surrounded by interconnected paths or pores." Pore size/distribution is controlled by emulsion composition (e.g., cross-linker concentration), polymerization technique, and surface energy of the channel walls; pore sizes attainable in hydrogels range from a few nanometers to tens of microns.
- Excerpt: "Macroporous hydrogels have been fabricated inside microchannels by emulsion photopolymerization of a mixture containing monomer, cross-linker, photo-initiator, and porogen (e.g., water)." (lines 867–877; pore range line 829)

## Module 3: Evidence Tables

### Table 3.1 — Hydrogel-based microfluidic components: mechanism, stimulus, hard data

||||||
|---|---|---|---|---|
|Sensor — dissolvable gel (14.4.1)|Disulfide cross-linker (N,N′-cystamine-bisacrylamide) cleaved → gel degrades|Reducing agent: DTT, glutathione|Rate set by initial diameter, reducing-agent conc., cross-link density, temperature; figure features 500 µm / 300 µm|419–425; 434, 439|
|Sensor — enzyme-cleavable (14.4.1)|Peptide cross-linker cleaved by protease|Chymotrypsin (tetramer Cys-Tyr-Lys-Cys); botulinum neurotoxin (19-mer)|Less-cross-linked gels degrade faster; sensitivity programmed by peptide length/sequence|425–428; 470–479|
|Sensor — antigen-responsive (14.4.1)|Antigen–antibody pair used as cross-linker; free antigen competes → cross-links weaken → gel expands|Antigen|Reversibly antigen-responsive hydrogel (Miyata et al., ref. 39)|480–483; 1144–1145|
|Sensor/display — colorimetric (14.4.1)|pH-sensitive dye powder mixed into prepolymer, immobilized in poly(HEMA); sequential photopolymerization → combinatorial display|Local pH|"The hydrogel posts changed color based on the local pH"; single unit = sensor + display|414–417; 486–490|
|Sensor — bead immunoassay (14.4.1)|Biotin–avidin capture of antibody on agarose beads|Antigen binding|"each avidin can bind to four biotins" → dense antibody coverage|496–501|
|Valve — biomimetic bi-strip check valve (14.4.2)|Responsive + nonresponsive hydrogel bi-strip bends on swelling → one-way flow|pH|Fig. 14.4A scale bar 500 µm; mimics xylem/vein valves|510–516; 545, 567–570|
|Valve — arrowhead check valve (14.4.2)|Gel elongates; head contacts valve neck; soft seal better than rigid|pH|Fig. 14.4B scale bar 250 µm|529–533; 545|
|Valve — simple cylinder (14.4.2)|Cylinder at channel intersection swells and blocks channel|pH or temperature|Beebe et al., Nature 404, 588 (2000)|596–598; 575, 1160–1161|
|Valve — light-activated (14.4.2)|Gold colloids/nanoshells embedded in thermoresponsive gel absorb light → local heating → chain response|Light at 532 nm and 832 nm|Independent optical control of two valve populations (ref. 48)|598–602; 1164–1166|
|Valve — self-regulating (14.4.2)|Gel swelling displaces PDMS membrane → opens/closes an orifice → compensating buffer flow|pH (HEMA-based gel); glucose + pH (phenylboronic gel)|Fig. 14.4D scale bar 50 µm; maintains constant pH; drug-release version|603–617; 561, 576–580|
|Pump / dispenser (14.4.3)|Array of pH-sensitive gels on flexible membrane deforms it → fluid dispensed from reservoir|pH; target molecule (glucose) for closed loop|2 µl/min over 12 h open-loop infusion; valved version stores pressure in a "pumping chamber"|620–637|
|Clutch / programmable mixer & pump (14.4.4)|Gel post photopolymerized at the centre of a Ni rotor; on swelling it presses the rotor and stops rotation despite the rotating magnetic field|pH or temperature (different gels for different posts)|Array of micromixers "respond to different pH" (Fig. 14.5C,D)|703–736; 692–697|
|Lens (14.4.5)|Hydrogel ring below aperture encloses water pinned against oil; swelling changes interface geometry → focal length ("like the ciliary muscles")|Temperature or pH|Two microlenses with different stimuli = "compound eyes"; exploits increased surface tension at microscale|739–755; 806–811|
|Active assembly (14.4.6)|Gel bar swells/elongates to close channel sections and to move objects between channels|Local environment / specific molecules|Detector moved to adjoining channel "thus reducing background interference"|758–765; 816–823|
|Separation — gel electrophoresis on chip (14.4.7)|Photopolymerized polyacrylamide sieve + electric field|Electric field|DNA separation (ref. 59); native-protein separation, tetanus toxin & antibody quantified (ref. 60)|843–852|
|Separation — nanoporous T-sensor enhancement (14.4.7)|Free vs bound protein diffuse differently; gel greatly reduces diffusion in a size-dependent way|Antigen–antibody complex formation|"better resolution was achieved, allowing for more accurate detection"|856–866|
|Separation — macroporous HEMA monolith filter (14.4.7)|Emulsion photopolymerization → interconnected pores; removes cells from whole blood|Passive (flow)|Efficiency "comparable with that of centrifugation … using no external power supply"; Fig. 14.7 bars 10 µm / 50 µm|867–886; 913–914|
|Integrated device (14.5)|"Microfluidic tectonics" — components as in-situ photopolymerized "Lego blocks"|Assay-specific|Botulinum-neurotoxin detection from whole blood: porous filter + one-way check valves + antibody-coated agarose beads|934–947; 983–989|

### Table 3.2 — Table 14.1 (verbatim): prepolymer constituents and their functions (lines 356–367)

|||
|---|---|
|Monomer|"Forms the main framework and gives primary properties such as surface energy"|
|Cross-linker|"Added for mechanical strength, durability, and responsiveness"|
|Co-monomer|"Can be added for additional properties, e.g., responsiveness"|
|Initiator|"Initiates the polymerization process"|
|Co-initiator|"Mediates transfer of energy from initiator to monomer"|
|Porogen|"Provides additional properties such as pores for the filter in emulsion photopolymerization"|

### Table 3.3 — Composition / process → property trade-offs (the design levers)

||||||
|---|---|---|---|---|
|Monomer chemistry|Pure HEMA|Nonresponsive|—|252|
|Co-monomer|HEMA + acrylic acid (AA)|pH-responsive; "it swells under basic conditions"|Responsiveness gained|252–254|
|Polymerization rate|↑ UV intensity|Many short chains → response time improved (faster swelling)|Mechanical strength compromised|255–259|
|Cross-link density|↓ cross-linking|Faster degradation; larger swelling extent|Lower strength/durability|168–169, 476–477|
|Cross-linker chemistry|Peptide / disulfide / antigen–antibody cross-linker|Converts recognition event into network breakdown or expansion|Specificity vs stability|417–418, 425–428, 480–483|
|Ionizable-group distribution|Spatial distribution of ionizable groups|Sets the rate of swelling (diffusion-limited)|—|171–172, 217–218|
|Initial size / geometry|Micron-sized structures|"diffusion is rapid and the response time is usually within a few minutes"|Small parts = small force/stroke|184–185|
|Porogen + emulsion composition|Cross-linker concentration, polymerization technique, channel-wall surface energy|Controls pore size and distribution ("tuning" the material)|Permeability vs strength|873–877|
|Ionic (physical) cross-linking|Ca²⁺ + alginate|"Temporary hydrogel networks"; avoids radical toxicity to cells|Temporary, not permanent|262–266|
|Enzymatic cross-linking|Gelatin + transglutaminase poured into a silicone mold|Biocompatible channels suitable for adherent cell culture|Requires incubation|268–274|

### Table 3.4 — Quantitative data inventory (every number, with line)

||||
|---|---|---|
|15 years|Duration of "lab on a chip" downsizing effort at time of writing|32|
|nanoliters to microliters|Fluid volumes handled|36|
|1000-fold|Maximum volume expansion of responsive hydrogel|152|
|> ten cycles|Swelling/shrinking cycles that co-fabricated rigid materials cannot withstand → delamination|182|
|a few minutes|Typical response time of micron-sized hydrogel structures|185|
|0.1 to ≈100,000 sec|Range of response times of plant/fungal swelling–shrinking movements (µm–mm parts)|187–188|
|500 µm / 300 µm|Feature scale bars, dissolvable & enzyme-cleavable sensors (Fig. 14.3)|434, 439|
|500 µm / 250 µm / 50 µm|Scale bars: biomimetic check valve / hydrogel check valve / self-regulating orifice (Fig. 14.4)|545, 561|
|532 nm and 832 nm|Absorption wavelengths of gold colloids/nanoshells for light-actuated valves|601|
|2 µl/min over 12 h|Demonstrated dispenser flow rate, open-loop infusion system|627|
|four biotins per avidin|Basis of dense antibody coverage on agarose beads|499|
|few nanometers to tens of microns|Achievable hydrogel pore-size range|828–829|
|10 µm / 50 µm|SEM scale bars: emulsion-polymerized beads / blood-cell filter edge (Fig. 14.7)|913–914|
|pp. 437–457|Printed extent of the chapter (TOC + running heads)|10–26, 1197|

### Table 3.5 — Fabrication routes compared (§14.3.1)

||||||
|---|---|---|---|---|
|Photopolymerization|Free-radical, photo-initiator + UV through transparency mask|High — in situ, any location in channel labyrinth|"the radicals formed from the initiators are toxic to the cells"|237–245, 260–262|
|Thermally initiated polymerization|Free-radical, heat source, initiator swapped in prepolymer mix|Low — "less control in defining size and location"|Needs heat source|246–249|
|Ionic cross-linking|Ca²⁺ + alginate electrostatic bridging of negative chains|Moderate (T-junction / interfacial)|Networks are temporary|262–268|
|Interfacial polymerization|Reagents delivered in adjacent laminar streams (T-junction)|Interface-defined|Limited to interface geometry|266–268, 326–334|
|Enzymatic cross-linking|Gelatin + transglutaminase, cast in silicone mold, incubated|Mold-defined|Incubation time; protein-based|268–274|
|Microfluidics + photopolymerization (gradient)|Gradient generator/T-junction then UV cure|Graded properties inside one part|— ("not possible using traditional fabrication methods")|275–278, 339–343, 376–378|

## Module 4: Chapter Connections

### 4.1 Mechanism differences vs the prior chapter (Ch. 13, "Smart Polymers in Affinity Precipitation of Proteins", ch13.txt lines 1–3)

|||
|---|---|---|
|Polymer architecture|Soluble–insoluble linear smart polymers carrying affinity ligands ("affinity ligands are covalently coupled to soluble–insoluble polymers to form a macroligand", ch13 lines 211–213)|Covalently/ionically cross-linked networks fixed in place ("cross-linked into a network to form a porous sieve-like structure", ch14 line 142)|
|Physical transition used|Phase separation / precipitation of the polymer from solution (ch13 lines 12, 14–17: homo-/heterobifunctional modes, pH- and thermo-responsive polymers)|Volume phase transition of a bound network — swelling/shrinking, not dissolution (ch14 lines 146–154)|
|Output of the transition|Chemical/biochemical separation — the target protein is captured and recovered ("The basic idea of affinity precipitation involves the use of a macroligand", ch13 line 128)|Mechanical work / actuation — "transduction from a chemical stimulus to a mechanical action (as in muscles)" (ch14 lines 152–153)|
|Scale & container|Bulk stirred/batch liquid volumes, crude extracts (ch13 lines 808–810)|Confined microchannels, nL–µL, viscous/laminar regime (ch14 lines 36, 66–73)|
|Recognition strategy|Affinity ligand attached to the polymer (metal chelate, sugars, dyes — ch13 TOC line 18)|Recognition built into the cross-link (peptide, disulfide, antigen–antibody) so binding changes network topology (ch14 lines 417–418, 480–483)|
|Reversibility/durability metric|Recyclability of the polymer over precipitation cycles|"> ten" swelling cycles already break rigid co-materials → delamination (ch14 line 182)|
|Shared ancestry|Both use pH- and temperature-responsive acrylic chemistry (PAA, NIPAM — ch13 lines 14–15, 37–38)|pH-responsive HEMA-co-AA, thermoresponsive gels (ch14 lines 252–254, 597)|

One-line synthesis: Ch. 13 uses the smart-polymer transition as a separation engine in bulk; Ch. 14 uses the same class of transition as an actuation and sensing engine in confinement. The conceptual bridge is that both convert a chemical signal into a phase change — the difference is whether the polymer is free (precipitates) or tethered (swells and pushes).

### 4.2 Connection to the "next chapter"

There is no Chapter 15 of text: Ch. 14 is the final chapter. In the source file the reference list ends at line 1220 and the book Index starts at line 1231 (Index, followed by index columns through line 2087). The forward links are therefore (a) the chapter's own outlook and (b) the Index's cross-chapter page pointers:

- Outlook (lines 999–1019): "As microfluidic devices find more applications in cellular studies, hydrogels are also likely to be more widely used. The polymer chain network provides a biomimetic framework to contain the cells… In combining microchannels and hydrogels, both micro- and nanoenvironments can be finely tuned to realize in vivo settings." (i.e., the book closes pointing to hydrogel/microchannel tissue-mimetic platforms, refs 30, 64–66 at lines 1106–1107, 1215–1220.)

### 4.3 Cross-chapter concept links (verifiable via the book Index inside this file)

|||||
|---|---|---|---|
|"Acrylic acid 140, 150, 161, 352, 441, 442"|441–442 (HEMA-co-AA gels, gradient gels)|140, 150, 161, 352|1247|
|"Alginate 362, 370, 371, 388, 411, 414, 417, 441"|441 (Ca²⁺–alginate temporary network)|362–417 (delivery/bioseparation chapters)|1235|
|"Agarose beads 316, 445, 453"|445, 453 (immunoassay beads)|316|1273|
|"Antibodies 416, 427, 445, 451, 453"|445/451/453|416, 427 (affinity chapters)|1259|
|"Antigene antibody binding 445 … complex 451; sensitive hydrogels 257"|445, 451|257 (antigen-sensitive hydrogels, earlier chapter)|1261–1264|
|"Actuator 258, 259, 262" & "Artificial muscles 248, 259, 263"|— (Ch. 14 restates the muscle analogy at line 153)|248–263|1256, 1272|
|"Swelling rate 149, 276, 440"; "Swelling/deswelling 303, 440"; "Swelling/shrinking … 440"|440 (§14.3 kinetics)|149, 276, 303|2024, 2029, 2033–2034|
|"Volume expansion 439"; "Volume phase transition 83, 84, 89, 93, 157, 158, 161, 211, 225"|439 (1000-fold)|83–225 (physical-chemistry chapters)|2051–2053|
|"Surface tension 438"; "Surface-to-volume ratio 438"|438|—|2015–2016|
|"Hydrogel cylinders 446, 449"; "Sensor 443, 444"; "Valves 443, 445–448"|Ch. 14 only|—|1546, 1968, 2072|
|"Diapers 161, 170"|not in Ch. 14|161, 170 (SAP/diaper discussion in an earlier chapter)|1419|

### 4.4 Cross-chapter "formula" links (reconstructions — the chapter prints no equations)

- Diffusion-limited response time (reconstruction of lines 171–175): $\; t_{\text{resp}} \sim \dfrac{L^{2}}{D_{\text{eff}}}$, where $L$ = initial size/half-thickness of the gel, $D_{\text{eff}}$ = effective diffusion constant of water/ions, itself increasing with pore size. Textual basis: "the time scales for the volume change will depend on the distance traveled …, which in turn depends on the initial size of the hydrogel, the diffusion constant of the species, and pore size." [公式为文本关系重构，原文未给出方程]
- Swelling extent limit (reconstruction of lines 168–169): $\; Q_{\max} \propto \dfrac{1}{\nu_{c}}$ (extent of swelling falls as cross-link density $\nu_{c}$ / chain elasticity constraint rises). [重构，原文未给出方程]
- Rate–strength antagonism (reconstruction of lines 255–259): $\; \uparrow I_{\text{UV}} \Rightarrow \downarrow \overline{M_{n}} \Rightarrow \downarrow t_{\text{resp}} \; \text{and}\; \downarrow \sigma_{\text{mech}}$. [重构，原文未给出方程]
- Degradation rate of cleavable gels (reconstruction of lines 423–425, 476–477): $\; r_{\text{diss}} = f\big(d_{0}^{-1},\, C_{\text{reductant}},\, \nu_{c}^{-1},\, T\big)$. [重构，原文未给出方程]
- Low-Reynolds-number framing is only cited, not derived (refs 8, 9, 18 at lines 1048–1050, 1083–1084) — no Reynolds/capillary number formula appears in the chapter text. [行号缺失：本章无公式]
## Module 5: Business Connections — hygiene / sanitary materials (SAP, nonwovens, adhesives, smart hygiene)

Read-across logic: a diaper core is a confined microfluidic system made of a superabsorbent hydrogel plus fibrous channels. Ch. 14's parameter space (pore size, cross-link density, ionizable-group distribution, geometry) is exactly the SAP/ADL parameter space, and its sensor/valve concepts are directly transplantable to wetness/health indicators.

B1 — SAP absorption-rate engineering = the chapter's diffusion-limited response-time law.
Concept: response-time parameter space (Ch. 14 §14.3, lines 167–177; Fig. 14.1 caption lines 215–219).
Key relation: $t_{\text{resp}} \sim L^{2}/D_{\text{eff}}$ [reconstruction of lines 173–175]; micron-scale structures respond "within a few minutes" (line 185).
Action: Treat particle-size distribution (L) and internal porosity as the primary levers for vortex/FSR absorption speed, ahead of chemistry changes; a 2× reduction in effective particle radius predicts ~4× faster uptake. Specify a tightened PSD band (fewer coarse >600 µm particles) when rewet/acquisition speed is the failing KPI.

B2 — Swelling force is usable work — and a destructive load on the construction.
Concept: chemo-mechanical transduction, "volume expansion … as high as 1000-fold … can produce a mechanical force" (lines 151–154).
Action: (i) Positively: design self-actuating features driven by urine loading — e.g., a gel strip that swells to close a leak-guard gap or to open a vent (direct analogue of the bi-strip check valve, lines 513–516). (ii) Defensively: budget SAP swelling pressure into core-wrap tensile and adhesive shear specs; the chapter's own failure mode is exactly this mismatch (see B3).

B3 — Cycling durability: rigid components fail after "greater than ten" swell/shrink cycles → delamination.
Concept: lines 178–184 ("This mismatch results in delamination of channels and other complications").
Action: For adult incontinence and reusable/multi-insult products, define an ≥10-cycle wet/dry cyclic test on the SAP–adhesive–nonwoven laminate (not just single-insult), and prefer elastomeric hot-melt or discontinuous (spiral/curtain) adhesive patterns that tolerate gel expansion strain rather than continuous rigid slot-coat films.

B4 — Cross-link density: the CRC ↔ gel-strength trade-off, stated as a law.
Concept: "The extent of swelling is limited by the elasticity of the polymer chains and the cross-link density" (lines 168–169); less-cross-linked networks degrade/deform faster (lines 476–477).
Key relation: $Q_{\max}\propto 1/\nu_{c}$ [reconstruction].
Action: Use it to justify the core–shell (surface post-cross-linking) architecture: low bulk $\nu_c$ for capacity (CRC), high surface $\nu_c$ for gel strength/AUL and anti-gel-blocking. Set surface-cross-linker dosage by target AUL, not by CRC.

B5 — Polymerization-rate lever: faster response but weaker gel.
Concept: "At increased rate, a large number of small polymer chains are formed. The response time … is improved …, while the mechanical strength … is compromised." (lines 255–259).
Action: In SAP gel polymerization, treat initiator dose / UV or thermal ramp rate as a response-time knob with a known penalty in gel strength and extractables; pair any rate increase with compensating cross-linker or surface treatment. Also applies to UV-cured constructions/coatings on topsheets.

B6 — Ionizable-group distribution sets the swelling rate (not just capacity).
Concept: "The rate of swelling depends on the distribution of ionizable chemical groups and is limited by diffusion." (lines 171–172).
Action: Exploit gradient neutralization of poly(acrylic acid) SAP (surface vs core degree of neutralization) as a rate-shaping tool — the polymer analogue of the chapter's gradient hydrogels (lines 275–278, 339–343), which achieve asymmetric swelling within one part (line 371).

B7 — pH-responsive HEMA-co-AA: the chemistry of a urine/skin-pH indicator.
Concept: "hydrogel composed of purely HEMA is nonresponsive. With the addition of acrylic acid (AA), the hydrogel is responsive to pH, i.e., it swells under basic conditions." (lines 252–254).
Action: Because ammoniacal urine drifts basic, an AA-containing gel dot is a passive, power-free actuator/indicator for "soiled + alkaline = dermatitis risk" rather than mere "wet". Combine with B8 for visual output.

B8 — Power-free colorimetric readout: one unit = sensor + display.
Concept: "hydrogel-based sensors undergo a perceptible physical change that provides visual evidence of the detection. Thus, a single unit essentially performs both the sensor and display functions." (lines 414–417); made "by immobilizing pH-sensitive dyes inside HEMA hydrogels by mixing dye powder in the prepolymer mixture" (lines 486–488); combinatorial multi-dye display by sequential photopolymerization (lines 489–490).
Action: Highest-ROI transplant for hygiene: a printed/dot-coated dye-loaded gel array on the backsheet or inside the acquisition layer giving a graded colour scale (wet / alkaline / protease-positive) with no electronics, no battery, no NFC. Manufacturing route = mix dye powder into the coating formulation; multi-zone = sequential cure.

B9 — Enzyme-cleavable gels: a protease indicator for diaper dermatitis and infection.
Concept: peptide cross-linkers cleaved by a specific enzyme (chymotrypsin tetramer Cys-Tyr-Lys-Cys; 19-mer for botulinum neurotoxin), with "sensitivity … by varying the length (or sequence) of the peptide and the response time by adjusting the cross-link density" (lines 425–428, 470–479).
Action: Fecal proteases are the accepted aggressor in diaper rash — a peptide-cross-linked gel dot that dissolves/decolours on protease exposure yields a "change now" signal for mixed stool insults; tune trigger threshold by peptide sequence, tune latency by cross-link density (avoid false positives from a single small insult).

B10 — Antigen-responsive gels: biomarker sensing in pads.
Concept: antigen–antibody binding used as the cross-link; "a hydrogel that expands in the presence of the antigen … free antigen molecules compete for the antibody, which weakens the cross-linking" (lines 480–483).
Action: Concept basis for a UTI / vaginal-infection biomarker zone in incontinence or feminine pads, where swelling or dye release is the readout. Note manufacturing constraint: antibody stability through converting lines — position as an insert applied cold, not in-line cured.

B11 — Macroporous monolith by emulsion photopolymerization = tunable absorbent/ADL foam.
Concept: monomer + cross-linker + photo-initiator + porogen (water), agitated to an emulsion and cured → "contiguous polymer network surrounded by interconnected paths or pores"; pore size/distribution controlled by cross-linker concentration, polymerization technique, and surface energy of the channel walls (lines 867–877); pore range few nm → tens of µm (line 829).
Action: Direct recipe framework for HIPE/foam absorbent cores or gel-coated ADLs: use porogen ratio + cross-linker concentration as the two-factor DOE for permeability (SFC analogue) vs capacity, and remember the third factor — substrate surface energy — i.e., the nonwoven's finish alters the cured pore structure at the interface. Corona/surfactant choices on the carrier web are therefore part of the gel formulation.

B12 — Passive, power-free separation replacing centrifugation → in-pad diagnostics.
Concept: HEMA-based porous monolith removed blood cells from whole blood; "efficiency of separation was comparable with that of centrifugation, with the added advantages of working with small volumes and using no external power supply" (lines 879–886); "centrifugal forces do not scale well with size" (lines 881–883).
Action: Enables the "smart sanitary pad": a monolith/porous-gel window that separates cells from plasma in menstrual blood (or cells from urine) and feeds a lateral-flow immunoassay — anaemia, HPV/hormone or infection screening — entirely passively. Also a QC read-across: gel filters can replace centrifuge steps in lab testing of body-fluid simulants.

B13 — Self-regulating (closed-loop) dosing of actives from the product.
Concept: "the swelling of the hydrogel is coupled to the displacement of a PDMS membrane. The membrane is actuated to open and close an orifice" to admit compensating buffer and hold pH constant (lines 603–611); glucose+pH-sensitive phenylboronic gel releases drug on concentration oscillation (lines 612–614); design parameters: membrane size and thickness, channel depth, orifice shape (lines 614–616).
Action: Architecture for skin-pH-buffered topsheets and odour control: a gel/membrane micro-reservoir that releases a citrate/lactate buffer, zinc oxide dispersion or odour-neutraliser only when urine raises pH, instead of dosing continuously. Dose rate is set geometrically (orifice + membrane thickness), which is a coatable/laminatable design space.

B14 — Dispenser flow rate as a benchmark for controlled active release.
Concept: "A flow rate of 2 µl/min over 12 h was demonstrated for use in an open-loop infusion system" (lines 627–628).
Action: ≈1.44 mL per 12 h per dispenser unit is a realistic order of magnitude for gel-actuated release; use it to size lotion/emollient or buffer reservoirs for an overnight (8–12 h) wear cycle and to decide how many discrete dispenser zones a pad needs.

B15 — "Microfluidic tectonics" + multiscale hierarchy = a modular smart-hygiene platform.
Concept: components "considered analogous to 'Lego blocks' and fabricated in situ (via photopolymerization) at any location in the device", allowing an assay-specific device to be built ad hoc (lines 943–947); "Hydrogel functionality is essentially multiscale; molecular events result in changes at the nanoscale (polymer chains) … microscale … macroscale" (lines 990–993).
Action: Adopt as the roadmap for smart hygiene: define a small library of printable gel functional dots (wetness indicator, pH indicator, protease indicator, buffer dispenser, swell-actuated leak guard) that a converting line can place at any position in the pad by the same coat-and-cure station. Product differentiation then = placement pattern, not new chemistry.

B16 — Capillarity and S/V: passive fluid distribution in nonwovens.
Concept: "The capillary forces resulting from the liquid–air interface are strong enough to move fluid through micron-sized conduits" (lines 85–87); high S/V improves contact with detectors (lines 91–94); "virtual wall" and controlled interfaces (lines 87–90).
Action: Confirms the physics baseline for ADL/distribution-layer design by capillary gradient (fine→coarse pore sequence) and for the "virtual wall" idea: surface-energy patterning (hydrophobic printed lines) can steer fluid without physical embossed channels — a cheaper route to directional distribution than mechanical channelling.

### Formulas / data directly usable for process-parameter selection

||||
|---|---|---|---|
|1|$t_{\text{resp}} \sim L^{2}/D_{\text{eff}}$ (initial size, diffusion constant, pore size) [reconstruction]|171–175|SAP particle size / PSD; gel-dot thickness; target absorption speed|
|2|Micron-scale gel → response time "within a few minutes"|184–185|Acceptance criterion for indicator/actuator latency|
|3|$Q_{\max}\propto 1/\nu_{c}$ — swelling extent limited by cross-link density & chain elasticity [reconstruction]|168–169|Bulk cross-linker dosage (CRC target)|
|4|Less-cross-linked → faster degradation/deformation|476–477|Surface post-cross-linking level (AUL/gel strength)|
|5|↑UV intensity → short chains → faster response, lower strength|255–259|UV lamp power / line speed / initiator dose in gel or coating cure|
|6|Swelling rate ∝ distribution of ionizable groups|171–172|Degree of neutralization & its gradient in PAA SAP|
|7|Pure HEMA nonresponsive; +AA → swells under basic conditions|252–254|Choice of pH-trigger comonomer & trigger direction (alkaline urine)|
|8|Dissolution rate $= f(d0^{-1}, C_{\text{reductant}}, \nu_c^{-1}, T)$|423–425|Indicator-dot diameter, trigger concentration threshold, temperature spec|
|9|Pore size/distribution controlled by emulsion composition (cross-linker conc.), polymerization technique, substrate surface energy|873–877|Foam/HIPE core DOE; corona or surfactant treatment of carrier nonwoven|
|10|Achievable pore range few nm → tens of µm|828–829|Permeability (SFC) vs filtration/sieving target|
|11|Porogen (e.g., water) as the pore-forming constituent|366–367, 869|Water/monomer ratio in foam recipes|
|12|Dye powder mixed into prepolymer mixture → immobilized colorimetric readout|486–488|Indicator coating formulation (no separate print step)|
|13|Dispenser output 2 µl/min for 12 h (≈1.44 mL)|627–628|Reservoir sizing for actives; number of dispenser zones|
|14|Self-regulating valve geometry factors: membrane size & thickness, channel depth, orifice shape|614–616|Laminate thickness and orifice die design for controlled release|
|15|Light-actuated gels via absorbers at 532 nm / 832 nm|598–602|Wavelength selection for optically triggered (NIR, through-body) actuation|
|16|Rigid co-materials fail beyond >10 swell/shrink cycles → delamination|181–183|Cyclic wet/dry test protocol; adhesive pattern & modulus selection|
|17|Plant/fungal actuation spans 0.1 – ≈100,000 s|187–188|Feasible design window for slow (odour/lotion release) vs fast (indicator) functions|
|18|4 biotins per avidin → dense ligand coverage|499|Sensitivity budgeting for any bead-based in-pad assay|
|19|Passive porous filter ≈ centrifuge efficiency, no power supply|883–886|Feasibility gate for in-pad diagnostic sample prep|
|20|Max volume expansion 1000-fold|151–152|Upper bound for swell-actuated mechanical features; swelling-pressure load case|

## Module 6: Key Quotes Index

"Hydrogel materials are both soft and responsive, which makes them ideal candidates in designing biomimetic components (e.g., valves, sensors) for use in microfluidic devices." (lines 56–59)
中文： 水凝胶材料既柔软又具响应性，因此是设计微流控器件中仿生元件（如阀门、传感器）的理想候选材料。
Why remember: The one-sentence value proposition of smart hydrogels — softness (sealing/comfort) and responsiveness (self-control) in a single material.

"viscous forces dominate at the microscale, as opposed to inertial forces at the macroscale. Therefore, the fluid (and particles therein) in a microwell is analogous to a swimming pool filled with honey." (lines 69–72)
中文： 在微尺度下黏性力占主导，而宏观尺度下是惯性力主导；因此微孔中的流体（及其中的颗粒）就像一个装满蜂蜜的游泳池。
Why remember: The most memorable image for why microscale intuition (and pore-scale fluid transport in a diaper core) is not macroscale intuition.

"The capillary forces resulting from the liquid–air interface are strong enough to move fluid through micron-sized conduits." (lines 85–87)
中文： 由液–气界面产生的毛细力足以驱动流体通过微米级通道。
Why remember: Capillarity alone can pump — the physical licence for entirely passive, power-free distribution layers.

"A high ratio of surface area to volume is beneficial in detection because more particles can make contact with the detector." (lines 93–94)
中文： 高的表面积/体积比对检测有利，因为更多颗粒能与检测器接触。
Why remember: Explains why fine fibres/fine gel particles boost sensing and uptake — and, inversely, why they lose heat and dry out fast.

"With the advent of hydrogels, smart and autonomous components could be created, because these materials can sense the local environment and undergo phase transition, such as an abrupt swelling." (lines 132–134)
中文： 随着水凝胶的出现，可以制造智能、自主的元件，因为这些材料能感知局部环境并发生相变（如突然溶胀）。
Why remember: Defines "autonomous" = no external pneumatic/electric/magnetic controller; the target state for smart hygiene products.

"The volume expansion, which can be as high as 1000-fold, can produce a mechanical force, resulting in transduction from a chemical stimulus to a mechanical action (as in muscles), and this force has been exploited in designing valves and pumps." (lines 151–154)
中文： 体积膨胀最高可达 1000 倍，能够产生机械力，从而实现由化学刺激到机械动作的转换（如同肌肉），这一力已被用于设计阀门和泵。
Why remember: The headline number and the core mechanism: SAP swelling is not just capacity, it is available mechanical work (and a structural load).

"The chemical composition of the polymer matrix determines the type of stimuli to which the hydrogel can respond. The extent of swelling is limited by the elasticity of the polymer chains and the cross-link density." (lines 167–169)
中文： 聚合物基体的化学组成决定水凝胶能响应的刺激类型；溶胀程度则受聚合物链弹性和交联密度的限制。
Why remember: Cleanly separates the two design axes — chemistry chooses the trigger, cross-linking chooses the amplitude (CRC).

"The rate of swelling depends on the distribution of ionizable chemical groups and is limited by diffusion. Therefore, the time scales for the volume change will depend on the distance traveled (by ions and water molecules), which in turn depends on the initial size of the hydrogel, the diffusion constant of the species, and pore size." (lines 171–175)
中文： 溶胀速率取决于可电离化学基团的分布，并受扩散限制；因此体积变化的时间尺度取决于（离子和水分子）迁移的距离，而该距离又取决于水凝胶的初始尺寸、物种的扩散系数和孔径。
Why remember: The kinetic master relation — the textual basis for $t\sim L^2/D$ and hence for SAP particle-size and porosity specifications.

"hydrogel components are usually fabricated along with other rigid materials that are not able to withstand repeated cycles (greater than ten). This mismatch results in delamination of channels and other complications." (lines 181–183)
中文： 水凝胶元件通常与其他刚性材料一起制造，而这些刚性材料无法承受十次以上的反复循环；这种失配会导致通道分层等问题。
Why remember: The durability ceiling, quantified — a ready-made ≥10-cycle wet/dry test rationale for SAP–adhesive–nonwoven laminates.

"plants and fungi use a swelling/shrinking mechanism for moving small parts (micrometer to millimeter range). They display a range of response times, from 0.1 to ≈100,000 sec." (lines 186–188)
中文： 植物和真菌利用溶胀/收缩机制来移动微米至毫米级的小部件，其响应时间跨度从 0.1 秒到约 100,000 秒。
Why remember: Nature's benchmark window — proves one mechanism can serve both instant indicators and multi-hour release.

"hydrogel composed of purely 2-hydroxyethylmethacrylate (HEMA) is nonresponsive. With the addition of acrylic acid (AA), the hydrogel is responsive to pH, i.e., it swells under basic conditions." (lines 252–254)
中文： 纯 2-羟乙基甲基丙烯酸酯（HEMA）构成的水凝胶无响应性；加入丙烯酸（AA）后，水凝胶即对 pH 有响应，即在碱性条件下溶胀。
Why remember: Minimal recipe change that installs a pH trigger — and the trigger direction (alkaline) matches ammoniacal urine.

"In photopolymerization, this is achieved by increasing the intensity of UV radiation. At increased rate, a large number of small polymer chains are formed. The response time of such a structure is improved (i.e., shorter time required to swell), while the mechanical strength of the structure is compromised." (lines 255–259)
中文： 在光聚合中，通过提高紫外辐照强度实现（提高聚合速率）。速率提高时会形成大量短聚合物链，这种结构的响应时间得到改善（即溶胀所需时间更短），但结构的机械强度会被削弱。
Why remember: The explicit speed-vs-strength trade-off — a process (not formulation) lever, with a stated penalty.

"In contrast, hydrogel-based sensors undergo a perceptible physical change that provides visual evidence of the detection. Thus, a single unit essentially performs both the sensor and display functions." (lines 414–417)
中文： 相比之下，基于水凝胶的传感器会发生可感知的物理变化，为检测提供可视化证据；因此单一单元实质上同时完成传感与显示两种功能。
Why remember: Why hygiene indicators should be gels, not electronics — sensor + display + power supply collapse into one printed dot.

"The degree of degradation depends on the cross-link density of the hydrogel, i.e., less-cross-linked structures degrade faster. The ability to create peptide–hydrogel hybrids allows for programming the sensitivity of the sensor by varying the length (or sequence) of the peptide and the response time by adjusting the cross-link density of the hydrogel." (lines 476–479)
中文： 降解程度取决于水凝胶的交联密度，即交联度较低的结构降解更快。构建"多肽–水凝胶"杂化体的能力使得可以通过改变多肽的长度（或序列）来编程传感器的灵敏度，并通过调节交联密度来编程响应时间。
Why remember: Two orthogonal programming knobs — sequence sets what is detected, cross-linking sets how fast: ideal for tuning a protease/dermatitis indicator's threshold and latency.

"The pore size and its distribution are controlled by many parameters: composition of the emulsion mixture (e.g., concentration of cross-linker), polymerization technique, and the surface energy of the channel walls. This breadth in parameter space allows for 'tuning' of the material as per the needs of the application." (lines 873–877)
中文： 孔径及其分布由多种参数控制：乳液混合物的组成（如交联剂浓度）、聚合工艺，以及通道壁的表面能。参数空间之广使材料可按应用需求进行"调谐"。
Why remember: Includes the counter-intuitive third factor — the substrate's surface energy changes the cured pore structure, so nonwoven finish is part of the gel formulation.

"Using the porous filter, efficiency of separation was comparable with that of centrifugation, with the added advantages of working with small volumes and using no external power supply." (lines 883–886)
中文： 使用该多孔过滤器，其分离效率与离心相当，并且还具备可处理小体积样品、无需外部电源的额外优势。
Why remember: Power-free blood-cell/protein separation is the technical gate that makes an in-pad diagnostic (menstrual or urine screening) plausible.

"Hydrogel functionality is essentially multiscale; molecular events result in changes at the nanoscale (polymer chains), and these are harnessed to create components at the microscale, and integrating the individual parts leads to a functional microfluidic device at the macroscale." (lines 990–993)
中文： 水凝胶的功能本质上是多尺度的：分子事件引起纳米尺度（聚合物链）的变化，这些变化被用于构建微尺度的元件，而将各个部件集成起来便得到宏观尺度上可工作的微流控器件。
Why remember: The scaling ladder for R&D planning — monomer choice → chain/pore → functional dot → finished hygiene product.

### Verification & anti-fabrication notes

- All line numbers refer to ch14.txt (as printed by cat -n), except Section 4.1, which cites ch13.txt line numbers explicitly.
- The chapter contains no numbered equations and no tabulated numerical datasets other than Table 14.1 (qualitative, lines 356–367). All LaTeX expressions in Modules 4–5 are labelled reconstructions of textual scaling statements. [原文无公式]
- No page numbers are invented: the only page references used (437–457) come from the chapter TOC (lines 10–26), running heads (e.g., line 1197) and the book Index columns (lines 1231–2087).
- Business items in Module 5 are explicitly separated into chapter-sourced facts (line-cited) and action suggestions (analyst's read-across to hygiene materials, not claims of the source text). The book's own diaper/SAP discussion is not in Chapter 14 — the Index locates it at pp. 161 and 170 ("Diapers 161, 170", line 1419).

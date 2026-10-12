---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_a3db8339927bd9557f39540234844e3f001a693ee6c0644e"
source_file: "Handbook of Polymer Testing_ch10_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Polymer Testing/Handbook of Polymer Testing_ch10_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Handbook of Polymer Testing_ch10_report.md.md

# Chapter 10 Deep-Dive Report — Impact Strength

Book: Handbook of Polymer Testing – Short-Term Mechanical Tests (2002)
Author: Edward N. Brown (Rapra)
Chapter: 10 – Impact Strength
Source: Ebook_Extract/Handbook_of_Polymer_Testing/chapters/Handbook of Polymer Testing_ch10.txt

## 1. Core Arguments（核心论点）

Impact testing exists to measure toughness – the actual work done to break a test piece.
"The decidedly ad hoc field of impact testing has received considerable attention in official standards, materials data sheets and the literature because the impact properties of plastics materials are directly related to the overall toughness of the material." [Line 10-12]
"The one advantage impact tests offer is a ready measure of the actual energy required to break the test piece." [Line 16-17]

Impact tests remain justified because high-speed tensile/flexural testing is technically complex, and toughness under rapid deformation matters most.
"the area under a conventional tensile or bending test curve is of limited value because in practice one is frequently interested in toughness under conditions of rapid deformation. There is, however, much technical complexity in carrying out tensile tests and other modes of deformation at high speed. Thus, the concept of impact resistance or 'strength' and the introduction of impact or shock resistance tests, and its assessment follow naturally from these concerns." [Line 22-27]

Impact energy comprises two distinct contributions: crack initiation energy and crack propagation energy.
"Energy is required both to create a crack and to allow this crack to be propagated through the material. The energy to initiate a crack is called the crack initiation energy." [Line 38-39]
"Thus, both crack initiation and crack propagation contribute to the measured impact energy." [Line 46-48]

Different failure modes must NOT be pooled together when interpreting results.
"It is important in interpreting the results of a test that test pieces exhibiting different kinds of failure are not pooled together." [Line 49-51]

All polymer materials have a critical velocity above which they behave as glassy, brittle materials – material selection based on standard impact tests can be dangerous for real high-speed applications.
"All polymer materials seem to have a critical velocity above which they behave as glassy, brittle materials." [Line 94-96]
"If in a particular application the product will 'see' impact speeds of 50 m/s then it is dangerous to base a material selection on normal impact tests like Charpy or Falling Weight because the impact velocities are an order of magnitude lower and a material which may behave in a tough manner at these speeds may become brittle at the application speed." [Line 97-101]

Temperature and loading rate are coupled: there is no single temperature of brittleness, but a locus of temperature/speed values for each polymer.
"Note that increasing temperature has the opposite effect of increasing speed and so there is not a single temperature at which brittleness occurs, but a locus of temperature/speed values where the transition from ductile to brittle behaviour takes place. Every polymer has its own characteristic locus." [Line 117-120]

Notches create massive localised stress concentrations that dramatically lower impact strength; all plastics are notch-sensitive.
"a notch creates a localised stress concentration where the true stress can be many times higher than the bulk stress being imposed on the test piece or object as a whole." [Line 129-131]
"All plastics are notch-sensitive, but the notch sensitivity varies with the type of plastic being considered." [Line 132-133]

Fillers and modifiers can improve OR impair impact strength depending on type and coupling.
"Polymeric impact modifiers may be incorporated to act as barriers or crack blunting regions to the advancing crack front." [Line 152-153]
"Other fillers may be used simply to make the product cheaper and typically these result in some impairment of impact strength compared to the base resin." [Line 163-164]

Molecular orientation makes impact strength anisotropic – it is always higher in the direction of flow.
"the impact strength is always higher in the direction of flow." [Line 179-186]
"at right angles to the flow or drawing direction the impact properties can be significantly reduced as it is predominantly inter-molecular forces rather than intra-molecular forces that are involved." [Line 187-189]

Different impact methods (Charpy vs Izod vs Falling Dart) cannot be directly compared; results are method-, size-, and orientation-dependent.
"different types of pendulum test, e.g., Charpy and Izod, also produce different results and there is no simple correlation between them." [Line 236-238]
"for this reason results obtained from test pieces of different size cannot be compared." [Line 358-360]
"even when simply comparing databases for materials we must be sure we are comparing like with like or false conclusions will inevitably follow." [Line 242-245]

## 2. Key Concepts with Operationalized Definitions

### 2.1 Toughness

- English original definition: "a broadly accepted definition is the work done in breaking a test piece or object." [Line 13-14]
- Position: Section 10.1.1 Introduction
- Usage excerpt: "The impact properties of plastics materials are directly related to the overall toughness of the material." [Line 11-12]
### 2.2 Crack Initiation Energy

- English original definition: "The energy to initiate a crack is called the crack initiation energy." [Line 38-39]
- Position: Section 10.1.2 Modes of Failure
- Usage excerpt: "If the available energy in the system undergoing impact exceeds the crack initiation energy, the crack will continue to propagate and complete failure will occur if the system has sufficient energy to also exceed the crack propagation energy." [Line 45-47]
### 2.3 Crack Propagation Energy

- English original definition: implicit – "the energy to … allow this crack to be propagated through the material" [Line 38-39]; also "the crack propagation energy" [Line 47]
- Position: Section 10.1.2 Modes of Failure
- Usage excerpt: "Thus, both crack initiation and crack propagation contribute to the measured impact energy." [Line 46-48]
### 2.4 Four Modes of Impact Failure (Vincent [1])

- English original definitions [Line 53-64]:

- "Brittle fracture is where the part fractures extensively without yielding and typically has sharp 'glassy' edges." [Line 53-54]
- "Ductile failure is where there is a definite yielding of material, often indicated by stress whitening, along with cracking." [Line 57-58]
- "Yielding is where the part exhibits obvious and permanent deformation and stress whitening but no cracking takes place." [Line 60-61]
- "Slight cracking is where the part shows evidence of some cracking and yielding but without losing its shape or integrity." [Line 63-64]
- Position: Section 10.1.2
- Usage excerpt: "It is important in interpreting the results of a test that test pieces exhibiting different kinds of failure are not pooled together." [Line 50-51]
### 2.5 Charpy / Izod Failure Codes (C / H / P / NB)

- English original definitions [Line 71-79]:

- "C complete break; a break in which the specimen separates into two or more pieces." [Line 71-72]
- "H hinge break; an incomplete break such that both parts of the specimen are held together only by a thin peripheral layer in the form of a hinge having no residual stiffness." [Line 73-74]
- "P partial break; an incomplete break that does not meet the definition for a hinge break." [Line 76-77]
- "NB non-break; in the case where there is no break, and the specimen is only bent, possibly combined with stress whitening." [Line 78-79]
- Position: Section 10.1.2
- Usage excerpt: "for Charpy and Izod tests, for example, the following definitions along with their letter abbreviations need to be adopted" [Line 68-70]
### 2.6 Notch Sensitivity

- English original definition: operationalised through definition of notch effect – "A sharp corner in a fabricated part or a notch in a test specimen can dramatically lower the impact strength of the material." [Line 128-129]
- Position: Section 10.1.3.3
- Usage excerpt: "Notches of different base radius are useful for more extensive characterisation of plastics than a simple quality test or data sheet entry, in that they enable an estimate of the notch sensitivity of the plastic to be investigated" [Line 311-314]
### 2.7 Critical Velocity

- English original definition: "All polymer materials seem to have a critical velocity above which they behave as glassy, brittle materials." [Line 94-96]
- Position: Section 10.1.3.1 Rate of Loading
- Usage excerpt: "a material which may behave in a tough manner at these speeds may become brittle at the application speed." [Line 100-101]
### 2.8 Ductile-to-Brittle Transition Locus

- English original definition: "a locus of temperature/speed values where the transition from ductile to brittle behaviour takes place. Every polymer has its own characteristic locus." [Line 118-120]
- Position: Section 10.1.3.2 Temperature
- Usage excerpt: "increasing temperature has the opposite effect of increasing speed" [Line 116-117]
### 2.9 Impact Modifier (Crack Blunting)

- English original definition: "Polymeric impact modifiers may be incorporated to act as barriers or crack blunting regions to the advancing crack front." [Line 152-153]
- Position: Section 10.1.3.4 Fillers
- Usage excerpt: "A good example of this is the addition of polybutadiene (PB) rubber to styrene-acrylonitrile (SAN) plastics to produce ABS." [Line 154-155]
### 2.10 Molecular Orientation Anisotropy

- English original definition: "the manner in which the polymer molecules are oriented in a part will have a major effect on the impact behaviour of the polymer – the impact strength is always higher in the direction of flow." [Line 178-186]
- Position: Section 10.1.3.5 Orientation
- Usage excerpt: "Impact stresses are usually multiaxial and so tend to automatically 'find' the weakest direction in the moulding." [Line 191-192]
### 2.11 Charpy Impact Strength (normalised)

- English original definition: "The impact strength is the energy removed from the pendulum as a result of work done in breaking the test piece divided by the cross sectional area of the test piece in the direction of swing." [Line 355-357]
- Position: Section 10.2.1.1 Charpy Test
- Usage excerpt: "the test piece is bending during the impact event, there is a deformation volume rather than simply an area and so test pieces of different size do not give results which are proportional to the cross-sectional area" [Line 357-360]
### 2.12 Instrumented Falling Dart Test

- English original definition: operationalised – "The essential difference to the non-instrumented variant is that some load sensing transducer is built into the dart" [Line 673-674]; transducer "generally a resistive or piezo-electric device, the latter being preferred as it has a higher natural frequency" [Line 677-679]
- Position: Section 10.2.2.1 Falling Dart Methods
- Usage excerpt: "In addition to the impact energy, this test is also capable of delivering the peak force, the energy to peak force and the displacement at peak force." [Line 703-704]
## 3. Evidence Tables

### 3.1 Material Examples & Failure Modes

|||||
|---|---|---|---|
|Material → Failure Mode|General-purpose PS under impact|"General-purpose PS typically exhibits this type of failure [brittle fracture] under impact conditions."|Line 54-55|

|Material → Failure Mode|Polyolefins|"Polyolefins are generally considered to be ductile materials."|Line 58|

|Polymer → Moisture effect|Nylons 6 & 6-6|"Very dry Nylons like Nylon 6 and 6-6 are quite brittle and sufficient time must be allowed for them to gain atmospheric moisture prior to testing if the 'equilibrium' impact strength is to be measured."|Line 157-160|

|Modifying additive|PB rubber in SAN → ABS|"the addition of polybutadiene (PB) rubber to styrene-acrylonitrile (SAN) plastics to produce ABS."|Line 154-155|

|Plasticiser|PVC|"lower molecular weight plasticisers are added (for example to polyvinyl chloride (PVC)) to improve the impact behaviour."|Line 155-156|

|Fibrous filler|Stress-transfer agents|"fibrous fillers that appear to act as stress transfer agents. Good coupling between the fibre and the polymer matrix is necessary for the effect to take place."|Line 162-163|

|Cost filler|Typically impairs toughness|"Other fillers may be used simply to make the product cheaper and typically these result in some impairment of impact strength compared to the base resin."|Line 163-164|

|Case study|Crystallinity in semi-crystalline plastics|"increasing the percentage crystallinity decreases the impact resistance and increases the probability of brittle failure" [Line 220-222]; "Material that has been quenched from the melt will be tougher than the same material that has been allowed to cool slowly." [Line 222-224]|Line 220-224|

|Case study|Nylon 6 + ABS blends, testing speed|"Otterson and co-workers [2] report the effect of testing speed on blends of Nylon 6 and acrylonitrile-butadiene-styrene (ABS) for crack growth resistance"|Line 102-104|

|Case study|PEEK crystallinity & MW|"The crystallinity and molecular weight effects for polyether ether ketone (PEEK) is dealt with in a paper by Chivers and Moore [36]."|Line 224-225|

### 3.2 Test Methods Comparison

|||||
|---|---|---|---|
|Standard|Charpy – ISO|"BS EN ISO 179-1 [41], and the related ASTM D6110 [42]."|Line 265-266|

|Standard|Izod – ISO|"BS EN ISO 180 [49] and ASTM D256 Method A [50]"|Line 404-405|

|Standard|Tensile impact|"BS EN ISO 8256 [57] and ASTM D1822 [58]."|Line 510-511|

|Standard|Falling dart – general plastics|"BS EN ISO 6603-1 [61]."|Line 615-616|

|Standard|Falling dart – instrumented|"BS EN ISO 6603-2 [69] for general purpose plastics testing and ISO 7765-2 [70] for films and sheeting."|Line 670-671|

|Standard|Films / sheeting (non-instrumented)|"ISO 7765-1 [66], and the identical BS 2782 Method 352E [67], and in ASTM D1709 [68]."|Line 664-665|

|Standard|Gardner impact (ASTM)|"ASTM D5420 [64] … the so-called Gardner impact test"|Line 649-653|

|Standard|Small-specimen Izod-like|"ASTM D4508 [52] is an Izod-like cantilever beam test but using a small test piece, 19.05 mm long by 12.7 mm wide and 1.02 to 3.18 mm thick" [Line 489-491] "particularly favoured for assessing the effect of weathering on the impact resistance of plastics and for testing test pieces taken from finished products" [Line 491-493]|Line 489-493|

|Standard|Blow-moulded container drop|"ASTM D2463 [78] is applied to blow-moulded containers"|Line 758-760|

|Standard|Pipe round-the-clock|"BS EN 744 [73] which is the same as BS 2782 Method 1108C [74]"|Line 727-728|

|Methodology|Charpy specimen|"The standard test bar is 80 x 10 x 4 mm which can be cut from the centre parallel portion of the multipurpose test specimen"|Line 286-287|

|Methodology|Charpy impact velocity|"The one most frequently used has an impact velocity of 2.9 m/s and five pendulums having energies of 0.5, 1.0, 2.0, 4.0 and 5.0 J are specified."|Line 351-353|

|Methodology|Izod impact velocity|"The impact velocity for the test is 3.5 m/s and pendulums of energy 1.0, 2.7, 5.5, 11.0, and 22.0 J are used."|Line 437-439|

|Methodology|Charpy vs Izod – clamping|"Certain plastics can give results which vary according to clamping pressure, a problem from which the Charpy test is free" [Line 441-442]; "The test is often applied to plastics at sub-ambient temperatures but is far from ideal for this. Again, the Charpy test is preferred." [Line 447-448]|Line 441-448|

|Methodology|Falling dart (non-instrumented) specimen|"Test pieces of preferred size 60 mm square (or circular) by 2 mm thick are supported on an annular base of inside diameter 40 mm and the dart with a 20 mm diameter striker is released from a preferred height of one metre."|Line 616-620|

|Methodology|Round-the-clock TIR|"The impact 'resistance' is measured as the true impact rate (TIR) which is the total number of failures divided by the total number of blows, expressed as a percentage." [Line 725-727]; "the maximum acceptable value for TIR is 10%." [Line 729-730]|Line 725-730|

### 3.3 Statistical Analysis Methods

|||||
|---|---|---|---|
|Statistical method|Staircase (Bruceton)|"The preferred method is the 'staircase' method in which the mass of the dart is varied in given increments according to whether the test piece previously tested passed or failed."|Line 622-626|

|Statistical method|Probit|"In Method B, the 'statistical' or 'probit' method, a minimum of 40 test pieces is required" [Line 628-629]; "plotting the percentage passes (or failures) against impact parameter … on probability paper and finding the best fit straight line."|Line 642-647|

|Statistical method|Method C – 'toss' energy correction|"Method C … attempts to make a correction for the energy required to 'toss' the test piece."|Line 467-468|

|Statistical method|Method D – notch sensitivity index|"Method D deals with the estimation of notch sensitivity by having the test carried out at two notch radii, 0.25 mm and 1.0 mm. The ratio of the difference in the two energy values to the difference in notch radii is then taken as the index of notch sensitivity."|Line 477-479|

|Statistical method|50% failure threshold|"The parameter which corresponds to the 50% failure probability is the mean value and the difference between the 50% and the 16% (or the 84%) probabilities is the standard deviation."|Line 646-647|

### 3.4 Numerical Thresholds & Critical Values

|||||
|---|---|---|---|
|Critical velocity example|50 m/s application vs standard test|"if the product will 'see' impact speeds of 50 m/s then it is dangerous to base a material selection on normal impact tests … because the impact velocities are an order of magnitude lower"|Line 97-99|

|Charpy energy range|Absorbed energy 10–80%|"the energy absorbed by the impact should be between 10% and 80% of the capacity of the pendulum."|Line 438-439|

|Notch radii|Type A / B / C|"0.25 mm (the type A notch) … 1.0 mm (type B notch) … 0.1 mm (type C)"|Line 309-310|

|Falling dart minimum specimens|Staircase|"At least 20 test pieces are required plus an additional 10 used as preliminary specimens"|Line 626-627|

|Falling dart minimum specimens|Probit|"a minimum of 40 test pieces is required, although in practice 60 or more tend to be needed."|Line 629-630|

|Instrumented dart velocity loss|<20%|"the dart should have a large excess of energy so that the reduction in velocity during impact is small (less than 20%)."|Line 694-695|

|Round-the-clock confidence|90% / TIR ≤ 10%|"the maximum acceptable value for TIR is 10%." [Line 729-730]; "must be established with at least a 90% level of confidence" [Line 730-731]|Line 729-732|

|Blow-moulded container drop|Method A n=20|"In Method A, 20 containers are released from an agreed height and the number of failures recorded"|Line 761-763|

## 4. Chapter Connections

Upstream links (Chapters 1–9):
- Chapter 6 (Tensile) and Chapter 9 (Flexural) are explicitly referenced as alternative sources of work-energy data: "This information can of course be calculated from stress-strain diagrams in, say, tensile (Chapter 6) or flexural (Chapter 9) tests." [Line 17-20] Chapter 10 argues that despite this, high-speed mechanical testing is complex, which justifies dedicated impact methods.
- The chapter assumes the reader already understands the fundamental viscoelastic and stress-strain framework established in earlier chapters; impact is positioned as a point on "the general curve of studying strength properties as a function of speed of testing" [Line 29-31] – conceptually linking back to the strain-rate dependence discussed elsewhere in the book.

Internal structure of Chapter 10:
- §10.1 General Considerations sets the conceptual stage: definitions of toughness, failure modes, and eight factors that affect impact strength (loading rate, temperature, notch sensitivity, fillers, orientation, processing conditions, molecular weight/crystallinity, impact methodology).
- §10.2 Specific Tests then operationalises the concepts by describing concrete test families: pendulum methods (Charpy §10.2.1.1, Izod §10.2.1.2, Tensile §10.2.1.3) and drop methods (Falling Dart §10.2.2.1, Falling Product §10.2.2.2). The general concepts from §10.1 (notch sensitivity, critical velocity, orientation, crystallinity) are repeatedly invoked as interpretive keys when describing each specific test.

Cross-references to adjacent chapters / book framework:
- Multipurpose specimen is traced to ISO 3167 [43] – used throughout the book.
- Fracture-mechanics treatment is deferred: "The science of fracture mechanics seeks to quantify these types of effects and the interested reader is referred to [7] … [8] … [9-17]" [Line 143-146] – indicating a companion Chapter 11 on Fracture Mechanics within the larger Rapra testing book series.
- ISO 10350 (single-point data) and ISO 11403-1 (multipoint data) [37, 38] tie Chapter 10 into the book's broader theme of standardised material-data acquisition.

Downstream implications (for Chapters 11+ / practice):
- Chapter 10 deliberately stops at "short-term" impact; it flags that more-sophisticated characterisation (e.g., instrumented tests delivering force-time/force-deflection curves) bridges into fracture-mechanics and viscoelastic-modelling chapters. The closing statement on the cost-vs-data trade-off of instrumented testing ("The negative side, of course, is that the apparatus is much more expensive and cannot be put together with a minimum of workshop facilities" [Line 709-711]) hands the reader toward more-specialised methods.

## 5. Business Connections – Application to the Hygiene / Absorbent Materials Industry

The hygiene-material supply chain (feminine / incontinence / diaper) uses polymer-intensive inputs: fluff pulp & SAP core (芯体), nonwoven (无纺布), adhesives (胶黏剂), and various films/thermoplastics in distribution packaging. Chapter 10's framework translates directly into procurement-quality and design criteria.

### 5.1 芯体 (Core) – SAP + Fluff Pulp Composite

- Impact resistance of the core under handling drops: cores are shipped and dropped (warehouse → pallet → packer). §10.2.2.2 (Falling Product Methods) is the exact methodology: containers "are frequently tested by loading the object in a way that simulates service and then releasing them from a given height – often at various angles, for corner, edge and face impacts" [Line 752-755]. Procurement should require suppliers to report round-the-clock / drop-test data (per §10.2.2.1 ASTM D2463 / BS EN 744) alongside standard SAP absorbency specs.
- Moisture & SAP behaviour: §10.1.3.4 notes that moisture dramatically improves toughness of polyamides – the same principle applies to cellulose-based fluff: equilibrium moisture content affects drop behaviour of the core. Test specification must state conditioning regime.
### 5.2 SAP (Super-Absorbent Polymer)

- Notch sensitivity is SAP packaging-critical: SAP bags suffer "fissures" and dusting at sharp corners. §10.1.3.3 – "A sharp corner … can dramatically lower the impact strength … failure under impact loading is promoted" [Line 128-132]. Procurement should reject SAP bags with sharp creases / corners; favour rounded geometry or polymeric impact modifiers.
- Temperature / rate coupling (§10.1.3.1–.3.2): cold-chain warehousing (winter) will shift SAP films toward brittle failure even at moderate drop speeds. Procurement test protocols must include sub-ambient drop testing.
### 5.3 无纺布 (Nonwoven – spunbond/meltblown)

- Orientation anisotropy is the central issue for nonwovens (§10.1.3.5): "the impact strength is always higher in the direction of flow" [Line 179-186] and "at right angles to the flow or drawing direction the impact properties can be significantly reduced" [Line 187-189]. Since nonwovens are directionally laid (MD/CD), impact/drape performance will differ by up to orders of magnitude across directions. Procurement acceptance should specify MD and CD separately, not a single average.
- Falling-dart (§10.2.2.1) is the industry-standard puncture test for nonwovens/films (ISO 7765-1 / ASTM D1709). The staircase / probit statistics (Table 3.3) tell QA how many specimens to run for a robust specification.
### 5.4 胶黏剂 (Adhesives – hot-melt / acrylic / epoxy on release liner)

- Coating / film orientation (§10.1.3.5) affects edge-peel and drop resistance of coated materials.
- Processing conditions (§10.1.3.6) – "Poor processing conditions may create voids … high processing temperatures may cause thermal degradation and, therefore, reduce the impact strength; inadequate drying of plastics that have a tendency to absorb moisture can have a dramatic effect in reducing the resulting impact strength." [Line 199-203] This directly governs hot-melt application windows on production lines: temperature, moisture content of the base, and void formation (from trapped air) all degrade toughness.
- Charpy / Izod methodology (§10.2.1.1–.2) used for evaluating impact-modified PS/PP in adhesive backing layers – ABS toughening (§10.1.3.4) is a textbook case study of adding polybutadiene to SAN to improve impact.
### 5.5 采购成本 (Procurement / Cost Control)

- Methodology comparability warning (§10.1.3.8): "even when simply comparing databases for materials we must be sure we are comparing like with like or false conclusions will inevitably follow" [Line 242-245]. Different suppliers may quote Charpy (ISO) vs Izod (ASTM) vs Falling Dart; procurement must normalise to a single method before comparing bids, otherwise cost-per-J can be misleading.
- Filler cost vs performance trade-off (§10.1.3.4): "Other fillers may be used simply to make the product cheaper and typically these result in some impairment of impact strength compared to the base resin." [Line 163-164] – a direct warning that the cheapest quoted SAP / nonwoven / film may hide filler-induced brittleness; acceptance specs must include an impact/drop pass criterion.
- Instrumented vs non-instrumented (§10.2.2.1): instrumented dart delivers far more data (peak force, energy to peak force, displacement) from as few as 5–10 specimens vs 20–60 for non-instrumented. For high-value procurement decisions (e.g., SAP core change-out), instrumented testing is cost-effective despite higher equipment cost.
- Round-the-clock / TIR for distribution packs (§10.2.2.1): TIR ≤ 10% at 90% confidence with ≥25 impacts [Line 729-732] gives a quantitative pass/fail criterion for cartons, trays and bulk packs – useful as a vendor-scorecard KPI.
### 5.6 Bottom-line Procurement Checklist (from Chapter 10)

- Require suppliers to state the specific test method, specimen size and impact velocity on every quote (avoids the "compare apples to oranges" trap).
- Specify conditioning (T, RH) and demand sub-ambient drop data for cold-chain products.
- For nonwovens and films, request MD and CD results separately (orientation anisotropy).
- For SAP films and edge-sensitive components, add a notch-sensitivity test (ASTM D256 Method D or Charpy Type A/B/C comparison).
- For bulk packs, require a round-the-clock / drop test with documented TIR ≤ 10%.

## 6. Key Quotes Index（金句索引）

"The impact properties of plastics materials are directly related to the overall toughness of the material."
中文：塑料材料的冲击性能与材料的整体韧性直接相关。
[Line 11-12]

"The one advantage impact tests offer is a ready measure of the actual energy required to break the test piece."
中文：冲击试验的一个优势在于它能直接测得破坏试样所需的真实能量。
[Line 16-17]

"All polymer materials seem to have a critical velocity above which they behave as glassy, brittle materials."
中文：所有高分子材料似乎都存在一个临界速度，超过该速度材料即表现为玻璃态、脆性状态。
[Line 94-96]

"Note that increasing temperature has the opposite effect of increasing speed and so there is not a single temperature at which brittleness occurs, but a locus of temperature/speed values where the transition from ductile to brittle behaviour takes place."
中文：升温对韧性的影响与提速相反，因此并不存在某一个导致脆性的单一温度，而是一系列温度/速度组合构成了韧性-脆性转变轨迹。
[Line 116-120]

"A notch creates a localised stress concentration where the true stress can be many times higher than the bulk stress being imposed on the test piece or object as a whole."
中文：缺口造成局部应力集中，使真实应力远高于试样整体所受的名义应力。
[Line 129-131]

"The impact strength is always higher in the direction of flow."
中文：冲击强度在流动方向上总是最高。
[Line 179-186]

"Polymeric impact modifiers may be incorporated to act as barriers or crack blunting regions to the advancing crack front."
中文：可加入聚合物冲击改性剂，作为前进裂纹前沿的屏障或钝化区。
[Line 152-153]

"Different types of pendulum test, e.g., Charpy and Izod, also produce different results and there is no simple correlation between them."
中文：不同类型的摆锤试验（如 Charpy 与 Izod）得出的结果也不同，二者之间并不存在简单的对应关系。
[Line 236-238]

"Even when simply comparing databases for materials we must be sure we are comparing like with like or false conclusions will inevitably follow."
中文：即便只是在比较材料数据库，也必须确保同类比较，否则不可避免地得出错误结论。
[Line 242-245]

"Failure is not a single event – energy is required both to create a crack and to allow this crack to be propagated through the material."
中文：失效并非单一事件——产生裂纹需要能量，裂纹在材料中的扩展也需要能量。
[Line 38-39]

Report generated for Handbook of Polymer Testing Chapter 10 – Impact Strength. All line numbers refer to the source file Ebook_Extract/Handbook_of_Polymer_Testing/chapters/Handbook of Polymer Testing_ch10.txt.


---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_73a77e46fc5a752eeffeb7521a953cbe001a693ee6c0644e"
source_file: "Handbook of Polymer Testing_ch6_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Polymer Testing/Handbook of Polymer Testing_ch6_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Handbook of Polymer Testing_ch6_report.md.md

# Handbook of Polymer Testing – Chapter 6 Deep-Reading Report

Book: Handbook of Polymer Testing – Short-Term Mechanical Tests
Author: Edward N. Brown (Rapra, 2002)
Chapter: 6 – Tensile Stress-Strain
Source file: /sandbox/workspace/Ebook_Extract/Handbook_of_Polymer_Testing/chapters/Handbook of Polymer Testing_ch6.txt

## 1. Core Arguments（核心论点）

Tensile stress-strain is the single most widely used short-term property and directly feeds design decisions.
"The short-term tensile characteristics of a material are probably the most commonly derived of all the properties that can be determined … they all endeavour to quantify a number of specific characteristics which relate to the strength and deformation of a material. Knowledge of these characteristics can give materials scientists, technologists, materials specifiers and designers an insight into the potential performance of a material." [Line 9-15]

Engineering stress vs. true stress must be distinguished because cross-section shrinks during elongation.
"the 'stress' that is normally measured in a tensile test is based upon the original dimensions of the material prior to the application of any force and that this is commonly known as 'engineering stress'. However, under an applied tensile force, a material … would undergo a contraction of its cross sectional area … resulting in an actual stress in the material greater than that indicated by an 'engineering stress' calculation … what is termed the 'true stress' will be calculated." [Line 28-45]

Polymers are fundamentally non-linear and viscoelastic – their modulus is not a constant, unlike ideal elastic solids.
"Unfortunately, polymeric materials are non-linear and consequently their stress-strain characteristic is not as simple as that shown in Figure 6.4 and hence their modulus is not a constant. The stress strain characteristics of polymeric materials are quite diverse and the four main generic types are discussed in Sections 6.1.1-6.1.4." [Line 92-95]

Four generic stress-strain behaviours exist for polymers: (a) yield > failure, (b) failure > yield (strain-hardening), (c) yield = failure (no drop), (d) brittle.
"The stress strain characteristics of polymeric materials are quite diverse and the four main generic types are discussed in Sections 6.1.1-6.1.4." [Line 92-95]; "if however, the material is not a tough ductile material, but brittle, then the stress strain curve of the material may look like the idealised curve presented in Figure 6.8." [Line 198-200]

For non-linear polymers, the choice of modulus method (tangent vs. secant) and the strain point for secant modulus materially changes the value – comparability requires method disclosure.
"It is also important to remember that the strain at which the secant modulus is taken can have a significant effect on the modulus value determined." [Line 249-253]

Strain rate controls polymer behaviour: increasing rate raises strength/modulus, induces a yield point, and can turn a ductile material brittle.
"the strength, and as a consequence the modulus of the material appears to increase with increasing rate of test … as the rate of extension increases so does the propensity of the material to form a yield point; in fact if the rate of extension was increased sufficiently the material would start to exhibit brittle behaviour." [Line 278-287]

Tensile data are only meaningful/comparable when test speed, conditioning, and equipment grade are disclosed.
"In addition to being non-linear, plastics are also viscoelastic and as a consequence exhibit time dependent behaviour. This can cause problems with tensile testing and care should be taken to establish the rate of extension that tests were conducted at if meaningful comparable data are to be generated." [Line 255-259]

## 2. Key Concepts with Operationalized Definitions

### 2.1 Stress (Engineering vs. True)

- Original definition: "Stress (MPa) = Force (N) / Area (mm²)" [Line 22]
- Position: Chapter 6.1, opening fundamentals.
- Engineering-stress caveat: "the 'stress' that is normally measured in a tensile test is based upon the original dimensions of the material prior to the application of any force and that this is commonly known as 'engineering stress'." [Line 28-30]
- True stress: "if the actual cross sectional area of the material under the applied force is monitored and a stress calculation made based upon the observed dimensions then what is termed the 'true stress' will be calculated." [Line 43-45]
- Operational use: All routine ISO 527 reporting uses engineering stress; true stress matters only when comparing polymer response under large deformation (necking, drawing) – e.g. when a nonwoven web or film necks in-line.
### 2.2 Strain & Strain (%)

- Original definition: "Strain = Extension δl (mm) / Original Length l₀ (mm)" [Line 49] and "Strain (%) = (Extension δl (mm) / Original length l₀ (mm)) × 100" [Line 71]
- Position: Chapter 6.1.
- Operational use: Elongation-at-break figures on SAP bead datasheets, nonwoven fabrics, bond-line peels are all reported as % strain derived from this definition.
### 2.3 Elastic Modulus (Young's Modulus)

- Original definition: "Modulus (GPa) = Stress (MPa) / Strain" [Line 90] and standardised: "Modulus of Elasticity in Tension (Young's Modulus): the ratio of the stress difference to the corresponding strain difference. These strains are defined in the standard as being 0.05% and 0.25%." [Line 367-369]
- Position: Chapter 6.1 (intro) and ISO 527 definitions [Line 367-370].
- Operational use: Stiffness of core (cellulose pulp) vs. SAP composite vs. spunlace nonwoven – a key spec when selecting materials for a diaper/panty-liner that must balance softness and shape retention.
### 2.4 Tangent Modulus vs. Secant Modulus

- Original definitions: "the tangent modulus, which is taken as the slope (stress/strain) of the best straight line that can be fitted to the initial portion of the curve and passes through the origin of the graph" [Line 224-228]; "the secant modulus, which is the modulus value that is calculated at a specified strain value, 1% being the most common for rigid materials." [Line 238-239]
- Example: "Tangent Modulus (ET) = 16.5 / 0.005 = 3300 MPa = 3.30 GPa … 1% Secant Modulus (E1%S) = 11.2 / 0.010 = 1120 MPa = 1.12 GPa" [Line 243-245]
- Position: Chapter 6.1 (end), Figures 6.9 & 6.10.
- Operational use: Two suppliers quoting "modulus" may differ by 3× for the same film if one reports tangent and the other 1% secant – procurement must lock the method into the contract.
### 2.5 Yield Stress / Yield Point

- Original definition: "the lowest stress at which strain increases without increase in stress" [Line 102-103]; ISO version: "Tensile Stress at Yield (Yield Stress): the first stress at which an increase in strain occurs without an increase in stress." [Line 328-329]
- Position: Sections 6.1.1 & 6.1.2.
- Operational use: Defines the elastic-to-plastic transition of a nonwoven fabric under tensile load – important for predicting whether a fabric will recover after handling/transport or will permanently deform.
### 2.6 Failure Stress / Tensile Stress at Break

- Original definition: "Tensile Stress at Break (Failure Stress): the tensile strength of the material at failure." [Line 125-127]; ISO: "Tensile Stress at Break: the tensile stress at which the test specimen ruptures." [Line 331]
- Position: Sections 6.1.1-6.1.4.
- Operational use: Minimum-spec threshold for SAP-agglomerate compressive integrity (converted via tensile analogy) and for bond-line adhesion of adhesives.
### 2.7 Failure Strain / Elongation at Break

- Original definition: "Tensile Strain at Break (Failure Strain): The corresponding tensile strain of the material at the failure stress." [Line 133-135]
- Position: Sections 6.1.1-6.1.4.
- Operational use: High failure strain (Figure 6.6 type, >4%) is desirable in elastic waistbands; low failure strain (Figure 6.8 brittle type, ~1.6%) is characteristic of over-cross-linked SAP beads under impact.
### 2.8 Cold Flow

- Original description: "the material is exhibiting cold flow, caused because the molecules of the HDPE, at this rate of extension, have sufficient time to align themselves just enough to accept the increase in deformation, whilst maintaining a constant resistance to the applied force (constant tensile stress)." [Line 281-284]
- Position: Section 6.1.2 (Figure 6.11 discussion).
- Operational use: Predicts long-term creep of HDPE/PP film wraps and adhesive films under sustained low loads (e.g. backsheet held under weight of wet core).
### 2.9 Gauge Length

- Original definition: "Gauge Length: the initial distance between the gauge marks on the central part of the test specimen." [Line 320-321]
- Operational use: Must be fixed in any tender for nonwovens/films – changing gauge length at constant mm/min changes the nominal strain rate (see 6.2.3.1 example, Line 664-669).
### 2.10 Speed of Testing (Strain Rate)

- Original definition: "Speed of Testing: the rate of separation of the grips of the testing machine during test." [Line 323]
- Operational use: Because polymers are viscoelastic, tensile data without stated speed are not comparable (Line 255-259); this is critical when benchmarking SAP, pulp, or nonwoven suppliers.
### 2.11 Poisson's Ratio

- Original definition: "Poission's Ratio: the negative ratio of tensile strain in one of the two axis normal to the direction of pull to the corresponding strain in the direction of pull within the initial linear portion of the longitudinal versus normal strain curve." [Line 372-374]
- Operational use: Describes lateral contraction of nonwoven/film under tension – relevant to predicting how much a web will narrow under a tension stand during converting.
### 2.12 Force-Measurement Grade (ISO 5893)

- Original definition: "The accuracy of the force measuring capability of machines complying to ISO 5893 is designated as either grade A or B … ISO 527 calls for ±1% which equates with grade A." [Line 391-394]
- Operational use: When auditing a third-party lab (or a supplier's QC lab), Grade A is required for contractual tensile sign-off; Grade B tolerances (±2%) are too loose for spec-limited purchases.
## 3. Evidence Tables

### 3.1 Formulae / Definitions

|||||
|---|---|---|---|
|Formula|Stress|"Stress (MPa) = Force (N) / Area (mm²)"|[Line 22]|
|Formula|Strain|"Strain = Extension δl (mm)/Original Length l₀ (mm)"|[Line 49]|
|Formula|Strain (%)|"Strain (%) = (Extension δl (mm) / Original length l₀ (mm)) x 100"|[Line 71]|
|Formula|Modulus|"Modulus (GPa) = Stress (MPa) / Strain"|[Line 90]|
|Definition|Gauge Length|"the initial distance between the gauge marks on the central part of the test specimen"|[Line 320-321]|
|Definition|Speed of Testing|"the rate of separation of the grips of the testing machine during test"|[Line 323]|
|Definition|Tensile Stress (engineering)|"the tensile force per unit area of the original cross section within the gauge length"|[Line 325-326]|
|Definition|Tensile Strength|"the maximum tensile stress sustained by the test specimen during a tensile test"|[Line 333-334]|
|Definition|Young's Modulus (ISO 527)|"the ratio of the stress difference to the corresponding strain difference … 0.05% and 0.25%"|[Line 367-369]|
|Definition|Poisson's Ratio|"the negative ratio of tensile strain in one of the two axis normal to the direction of pull to the corresponding strain in the direction of pull"|[Line 372-374]|

### 3.2 Material Behaviour Types (the four generic curves)

|||||
|---|---|---|---|
|Tough, yield > failure|Example σy=18 MPa, σf=12 MPa|"Yield Stress (σy) = 18 MPa … Failure Stress (σf) = 12 MPa"|[Line 121-127]|
|Tough, failure > yield (strain-hardening)|σy=18 MPa, σf=28 MPa, εf=4.7%|"Failure Stress (σf) = 28 MPa … Failure Strain (εf) = 4.7%"|[Line 159-173]|
|Tough, yield = failure (no drop)|"An interesting and sometimes perplexing characteristic … the material that does not show a drop in stress at yield point"|[Line 183-186]||
|Brittle|"only the failure stress and failure strain would be determined … Failure Stress (σf) = 15 MPa … Failure Strain (εf) = 1.6%"|[Line 201-210]||

### 3.3 Modulus – Numerical Example

|||||
|---|---|---|---|
|Tangent modulus|3.30 GPa|"Tangent Modulus (ET) = 16.5 / 0.005 = 3300 MPa = 3.30 GPa"|[Line 243]|
|1% Secant modulus|1.12 GPa|"1% Secant Modulus (E1%S) = 11.2 / 0.010 = 1120 MPa = 1.12 GPa"|[Line 245]|
|Method sensitivity|"the strain at which the secant modulus is taken can have a significant effect on the modulus value determined"|[Line 250-253]||

### 3.4 Strain-Rate Effect (HDPE, 23 °C)

|||||
|---|---|---|---|
|Strength vs rate|"the strength, and as a consequence the modulus of the material appears to increase with increasing rate of test"|[Line 278-279]||
|Yield emergence|"as the rate of extension increases so does the propensity of the material to form a yield point"|[Line 285-287]||
|Brittle onset|"if the rate of extension was increased sufficiently the material would start to exhibit brittle behaviour"|[Line 286-287]||
|Cold flow (low rate)|"the material is exhibiting cold flow"|[Line 281-284]||

### 3.5 Standards & Apparatus

|||||
|---|---|---|---|
|Standard set|ISO 527 family|"a comprehensive set of standards … covered in the various parts of ISO 527 [1-5]"|[Line 294-298]|
|ASTM equivalents|D638 / D882|"D638 [6] for general purpose plastics and D882 [7] for films and sheeting"|[Line 300-307]|
|Microtensile|ASTM D1708|"ASTM D1708 [8] where only small quantities of material are available"|[Line 309-311]|
|Machine grade|ISO 5893, Grade A = ±1%|"ISO 527 calls for ± 1% which equates with grade A"|[Line 391-394]|
|Machine types|Electromechanical & Servohydraulic|"only two types of tensile testing machines used commercially, electromechanical and servohydraulic"|[Line 436-437]|
|Speed table|Table 6.2|"1 … 2 … 5 … 10 … 20 … 50 … 100 … 200 … 500 mm/min"|[Line 478-488]|
|Extensometer accuracy|ISO 5893|"measure the change in gauge length with an accuracy of 1% of the relevant value or better"|[Line 532-533]|
|Extensometer types|Optical / Laser / Video|"three primary types of non-contacting extensometer, optical, laser and video"|[Line 568-569]|
|Test-piece count|≥5 per direction|"A minimum of 5 test pieces are required by ISO 527-1 for each direction tested"|[Line 630-631]|
|Specimen types|1A, 1B, 1BA, 1BB, 2, 4, 5, 5A, 5B|"the preferred test specimens that are applicable to this standard are either Type 1A or 1B"|[Line 656-662]|
|Nominal strain-rate rule|Adjust speed if gauge length changes|"the speed of test would have to be dropped from 50 mm/min … to 10 mm/min"|[Line 664-669]|

### 3.6 Sample-Specific & Procedural Rules

|||||
|---|---|---|---|
|Sample rejection|Yield/break outside parallel portion|"The results from test pieces that yield or break outside of the parallel portion are rejected"|[Line 813]|
|Film & sheet weight|Extensometer weight|"the specimen shall not carry the weight of the extensometer"|[Line 781-782]|
|Poisson's ratio rarity|"not common and requires a means of accurately recording the change in width or thickness"|[Line 849-851]||
|Standard atmosphere|ISO 291|"reference is made to ISO 291 [11]"|[Line 776-777]|

## 4. Chapter Connections

### 4.1 Position within the handbook

- Chapter 6 sits inside the "Short-Term Mechanical Tests" section of the handbook. It follows the introductory chapters that established general measurement principles and opens the core mechanics discussion.
- Tensile stress-strain is positioned by the author as the most universal first-order mechanical test: "the most commonly derived of all the properties that can be determined" [Line 9-10] – making it a prerequisite chapter for interpreting all subsequent tests (flexural, impact, fatigue,蠕变).
### 4.2 Forward linkages to later chapters

- Flexural testing (Ch 7, implied): The same ISO 5893 apparatus serves flexure ("which generally can also be used for compression, flexural and shear tests" [Line 380-381]); modulus definitions carry over.
- Thermal-mechanical testing: Viscoelastic caveat ("plastics are also viscoelastic and as a consequence exhibit time dependent behaviour" [Line 255-256]) foreshadows DMA / TMA chapters where time-temperature superposition is formalised.
- Environmental/long-term testing: Cold flow [Line 281-284] directly bridges to creep and stress-cracking chapters.
- Composite testing: ISO 527-4/-5 for fibre-reinforced plastics [Line 740-744] bridge to composite chapters.
### 4.3 Backward linkages to prior chapters

- Relies on the definitions of force, area, and displacement introduced in the handbook's opening chapters on general test philosophy.
- Uses ISO 291 (standard atmospheres) [Line 776-777], which is likely detailed in a prior conditioning chapter.
### 4.4 Internal structure of Ch 6

- 6.1 General Considerations [Line 7-254] – physics of stress/strain, four generic curves, modulus methods, strain-rate effect.
- 6.1.1 – 6.1.4 [Line 98-220] – the four generic stress-strain families.
- 6.2 Test Methods [Line 290-901]

- 6.2.1 Standard Methods (ISO 527 family, ASTM D638/D882) [Line 292-374]
- 6.2.2 Test Apparatus (machines, grips, extensometers, speeds) [Line 378-624]
- 6.2.3 Test Pieces (Type 1A/1B/1BA/1BB/2/4/5/5A/5B, ISO 527-2/3/4/5) [Line 628-896]
- 6.2.4 Procedure [Line 747-851]
- References [Line 904-936] – 11 standards.
### 4.5 Conceptual thread

- Physics definitions (stress, strain, modulus) → behavioural typology (4 curves) → measurement methodology (apparatus, specimens, speeds) → data interpretation cautions (tangent vs. secant, strain rate, cold flow, brittle onset).
## 5. Business Connections (卫材行业 – 芯体 / SAP / 无纺布 / 胶黏剂 / 采购成本)

以下将 Chapter 6 的力学概念转化为卫材产品 (diapers, panty-liners, AF, incontinence) 的工程与采购判断依据。

### 5.1 芯体 (Core – pulp/SAP composite)

- Young's modulus & 4-curve typology [Line 90, 92-220]：芯体的拉伸-压缩响应决定其在吸收液体后的形状保持和"回弹"能力。芯体属于柔性非均匀复合材料，落在 6.1.2 (strain-hardening) 或 6.1.3 (yield = failure) 类型，其 1% secant modulus 是判断"吸收液体后芯体是否过软导致渗漏"的关键指标。
- Strain rate [Line 255-287]：芯体在婴儿突然翻身/跳跃时承受高应变率冲击，需按图 6.11 逻辑评估高应变率下的 σf 和 εf，而非仅参考慢速拉伸数据——直接影响防反渗和防侧漏设计。
### 5.2 SAP (Super-Absorbent Polymer)

- Brittle behaviour [Line 198-210]：过交联或受潮的 SAP 颗粒在压缩下表现出 6.1.4 脆性类型 (εf ≈ 1.6%)，表现为颗粒粉化、回弹失效。供应商数据中 "compression recovery after compression" 本质上是 SAP 弹性模量的表现。
- Secant vs tangent modulus [Line 243-253]：SAP 是典型非线性材料，若供应商用 tangent modulus 报价、买方验收用 1% secant modulus，两者差异可达 3 倍 (同 [Line 243-245])——采购合同必须锁定方法，否则成本核算失准。
- Engineering vs true stress [Line 28-45]：SAP 在高吸液压缩下截面积显著变化，使用 engineering stress 会低估真实应力，影响对 SAP 填充密度的结构评估。
### 5.3 无纺布 (Nonwoven – spunlace, SMS, Meltblown)

- Anisotropy & ISO 527-4/-5 [Line 740-744]：无纺布是典型 orthotropic 材料 (MD 与 CD 方向性能不同)——必须采用 ISO 527-4，且至少 5 个样品/方向 [Line 630-631]，否则单方向测试会低估最差方向的失效风险。
- Extensometer selection [Line 561-614]：无纺布是"low modulus and/or thin materials"，"the weight of a clip on the extensometer would significantly distort the specimen" [Line 561-563]——必须使用 video extensometer (Figure 6.19) 或 optical extensometer，否则应变测量失真。
- Yield stress & yield strain [Line 121-135, 159-173]：无纺布在腰围/腰贴位置的反复拉伸后是否可恢复，取决于 σy 和 εy；若使用 6.1.3 类型材料 (无应力下降)，腰贴区域舒适度最佳。
- Nominal tensile strain [Line 356-365]：超出屈服点后的应变只能用 nominal strain (基于夹持位移) 描述——在评估拉伸网 (spunlace stretch web) 的回弹性时是行业标准指标。
### 5.4 胶黏剂 (Adhesive – hot melt, acrylic)

- Cold flow [Line 281-284]：热熔胶和背胶在长期低载荷下发生蠕变 (cold flow)，导致腰贴/魔术贴脱胶——这是 cold flow 概念的直接工程应用，评估胶黏剂必须做长时间低温拉伸。
- Speed-of-testing discipline [Line 255-259, 323]：胶黏剂黏弹特性强烈，不同速度下的 σf 差异巨大——供应商报价单必须注明速度，否则验收时不可比，直接导致来料质量纠纷。
- Grip system [Line 495-518]：胶黏剂试样薄、软、易脱夹，楔形夹持 [Line 510-514] 容易撕坏试样，应改用气爪 (pneumatic pressure) [Line 517-518]。
### 5.5 采购成本与供应链管理

- ISO 527 Grade A (±1%) vs Grade B (±2%) [Line 391-394, Table 6.1]：审计供应商实验室时要求 Grade A 设备，否则 ±2% 的误差带在规格线附近 (如 SAP compression strength 3.5 kPa ± 0.5 kPa) 会让合格/不合格判定失效，导致质量成本 (COQ) 上升。
- Nominal strain-rate 一致性 [Line 664-669]：如果供应商用 1BB (L₀=10 mm, 10 mm/min) 而买方用 1A (L₀=50 mm, 50 mm/min)，两者名义应变率相同 (100%/min) 但测试条件表面不同——采购规范中必须统一试样类型和速度，否则不同供应商数据不可比，议价基础失真。
- Test-piece count [Line 630-631]：最少 5 件/方向，供应商若只提交 3 件数据，统计置信度不足，来料质量波动风险被掩盖。
- Conditioning & ISO 291 [Line 776-777]：温湿度预处理标准化是保证供应商间数据可比的前提，否则南方湿度 vs 北方干燥环境测出的同一 SAP/无纺布拉伸强度差异可达 15-20%。
- Rejection rules [Line 813-817]：规范化的判废规则 ("yield or break outside of the parallel portion are rejected") 必须写入采购 AQL 检验标准，防止供应商用非代表性数据通过检验。
### 5.6 卫材综合应用矩阵

||||
|---|---|---|
|芯体|Modulus 4-curve, strain rate|结构选型、防渗漏|
|SAP|Brittle (6.1.4), secant vs tangent|供应商数据可比性、合同方法锁定|
|无纺布|Anisotropy (ISO 527-4), non-contact extensometer|MD/CD 双方向测试、腰围舒适度|
|胶黏剂|Cold flow, strain rate, pneumatic grips|长期脱胶风险评估|
|采购成本|Grade A machine, ISO 291, strain-rate rule|实验室审计、议价基础、AQL 标准|

## 6. Key Quotes Index

### Quote 1

- English: "The short-term tensile characteristics of a material are probably the most commonly derived of all the properties that can be determined."
- Chinese: "材料的短期拉伸特性可能是所有可测定性能中最常被获取的一种。"
- Position: [Line 9-10]
### Quote 2

- English: "Knowledge of these characteristics can give materials scientists, technologists, materials specifiers and designers an insight into the potential performance of a material."
- Chinese: "了解这些特性，可以让材料科学家、技术专家、材料选型者和设计者洞察材料的潜在性能。"
- Position: [Line 13-15]
### Quote 3

- English: "Unfortunately, polymeric materials are non-linear and consequently their stress-strain characteristic is not as simple as that shown in Figure 6.4 and hence their modulus is not a constant."
- Chinese: "不幸的是，高分子材料是非线性的，因此它们的应力-应变特性不像图 6.4 中那样简单，其模量也不是常数。"
- Position: [Line 92-93]
### Quote 4

- English: "the material is exhibiting cold flow, caused because the molecules of the HDPE, at this rate of extension, have sufficient time to align themselves just enough to accept the increase in deformation, whilst maintaining a constant resistance to the applied force."
- Chinese: "材料表现出冷流现象，这是因为在该拉伸速率下 HDPE 的分子有足够时间重新排列，足以接受形变的增加，同时维持对施加力的恒定抵抗。"
- Position: [Line 281-284]
### Quote 5

- English: "as the rate of extension increases so does the propensity of the material to form a yield point; in fact if the rate of extension was increased sufficiently the material would start to exhibit brittle behaviour."
- Chinese: "随着拉伸速率增加，材料形成屈服点的倾向也增强；事实上，如果拉伸速率足够大，材料会开始表现出脆性行为。"
- Position: [Line 285-287]
### Quote 6

- English: "In addition to being non-linear, plastics are also viscoelastic and as a consequence exhibit time dependent behaviour. This can cause problems with tensile testing and care should be taken to establish the rate of extension that tests were conducted at if meaningful comparable data are to be generated."
- Chinese: "除了非线性之外，塑料还是黏弹性的，因此表现出时间依赖性。这会给拉伸测试带来问题，如果要产生有意义的可比数据，就必须明确测试时所采用的拉伸速率。"
- Position: [Line 255-259]
### Quote 7

- English: "It is also important to remember that the strain at which the secant modulus is taken can have a significant effect on the modulus value determined."
- Chinese: "还必须记住，取割线模量时所对应的应变值会对最终得到的模量数值产生显著影响。"
- Position: [Line 250-253]
### Quote 8

- English: "A minimum of 5 test pieces are required by ISO 527-1 for each direction tested."
- Chinese: "ISO 527-1 要求每个测试方向至少使用 5 个试样。"
- Position: [Line 630-631]
### Quote 9

- English: "The results from test pieces that yield or break outside of the parallel portion are rejected."
- Chinese: "在平行段之外发生屈服或断裂的试样结果予以剔除。"
- Position: [Line 813]
### Quote 10

- English: "when testing thin sheets or film material, the specimen shall not carry the weight of the extensometer."
- Chinese: "在测试薄片或薄膜材料时，试样不得承受引伸计自身的重量。"
- Position: [Line 781-782]

Report end. All line references refer to the source text file Handbook of Polymer Testing_ch6.txt in Ebook_Extract/Handbook_of_Polymer_Testing/chapters/.


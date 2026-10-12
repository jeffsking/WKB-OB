---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_935a22f4065bdea29598dc2b9533d4b4001a693ee6c0644e"
source_file: "Handbook of Polymer Testing_ch9_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Polymer Testing/Handbook of Polymer Testing_ch9_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Handbook of Polymer Testing_ch9_report.md.md

# Handbook of Polymer Testing – Chapter 9 深度拆书报告

书名：Handbook of Polymer Testing – Short-Term Mechanical Tests
作者：Edward N. Brown (Rapra, 2002)
章节：Chapter 9 — Flexural Stress-Strain（弯曲应力-应变）
原始文件：Handbook of Polymer Testing_ch9.txt

## 1. Core Arguments（核心论点）

本章围绕"弯曲应力-应变"这一短时力学测试展开，核心论点可归纳如下：

弯曲测试与拉伸测试几乎同等常见，因为实际部件多承受复合载荷
"The short-term flexural characteristics of a material are almost as commonly measured as the tensile properties considered in Chapter 6. This is not surprising considering the fact that most components are subject to a mixture of loading modes, and flexing or bending often occurs by intent or accident." [Line 8-13]

弯曲试验的实操优势：试样更易制备，且无夹具问题
"Flexural tests also have the advantage that a strip test piece is easier to produce than a dumbbell and there are no gripping problems as can occur in tensile tests." [Line 11-13]

弯曲应力/应变代表的是外层纤维（outer fibre），而非整体材料，且仅在纤维应变 ≤ 5% 时公式才有效
"It should be noted, that the stress and strain that are calculated are the maximum outer fibre stresses and strains and that the stress calculations given later in the chapter are only valid up to a maximum fibre strain of 5%. … they refer to the outer layer of the material rather than the bulk." [Line 18-23]

因厚度方向各向异性，弯曲结果只能近似对应拉伸结果
"Because plastics are seldom completely isotropic through the thickness, the results will only approximately equate to those from tensile tests." [Line 23-24]

载荷方式有三种，三点弯曲最常用
"The mode of loading can take one of three forms: Three point / Four point / Simple cantilever. By far the most common is three point loading." [Line 26-35]

四点弯曲的优势：载荷支间应力分布均匀，而非像三点弯曲那样在中心点应力最大
"The advantage of four point loading is that the stress is uniformly distributed between the loading supports rather than being a maximum at the central loading point in three point bending." [Line 109-112]

悬臂弯曲已过时
"A third type of loading is a simple cantilever with the test piece fixed at one end and loaded at the other. This was relatively popular at one time … but is now rarely seen." [Line 168-170]

ISO 178 是弯曲性能的国际标准，且目前仅考虑三点弯曲
"The international standard for flexural properties is ISO 178 [1] and the British and European standards are identical. Currently, ISO 178, only considers three point bending tests although four point bending is said to be under consideration for certain textile-fibre-reinforced plastics." [Line 183-186]

"常规挠度 (Conventional Deflection, sC)"是弯曲测试独有的参数
"The term stress at the conventional deflection is unique to the flexural test." [Line 233-234]

柔性材料的测试面临严重的设备精度挑战
"This places very severe constraints on the accuracy of the test equipment and the test piece itself. For the standard test piece, 0.05% strain corresponds to a deflection of the outer surface of only 0.08 mm from its starting point." [Line 374-378]

## 2. Key Concepts with Operationalized Definitions（关键概念及其操作化定义）

### 2.1 Flexural Stress-Strain（弯曲应力-应变）

- 英文原文定义：
"Flexural stress-strain characteristics are derived by monitoring both the force required to flex a material and the displacement that the material undergoes as a result of the applied force at a constant deformation rate." [Line 15-17]
- 位置：[Line 15-17]
- 使用场景摘录：
"As with the case of tensile testing, to obtain any comparative data, the force and displacement has to be converted into stress-strain characteristics." [Line 52-54]
### 2.2 Maximum Outer Fibre Stress and Strain（最大外层纤维应力与应变）

- 英文原文定义：
"the stress and strain that are calculated are the maximum outer fibre stresses and strains and that the stress calculations given later in the chapter are only valid up to a maximum fibre strain of 5%." [Line 18-22]
- 位置：[Line 18-22]
- 使用场景摘录：
"they refer to the outer layer of the material rather than the bulk. Because plastics are seldom completely isotropic through the thickness, the results will only approximately equate to those from tensile tests." [Line 22-24]
### 2.3 Three-Point Bending（三点弯曲）

- 英文原文定义：
"this mode of loading is achieved by applying the force to the specimen at three points … The central loading point being equidistant from the outer two supporting points." [Line 32-34]
- 位置：[Line 32-34]
- 使用场景摘录：
"In practice the specimen usually sits on the two outer supporting rods and the force is applied through the central loading rod, which will have both a force transducer and some form of displacement measuring device attached." [Line 36-38]
### 2.4 Four-Point Bending（四点弯曲）

- 英文原文定义：
"this mode of loading is achieved by applying the force to the specimen at four points, usually with the loading span set to either one-third or one-half the support span." [Line 107-109]
- 位置：[Line 107-109]
- 使用场景摘录：
"The advantage of four point loading is that the stress is uniformly distributed between the loading supports rather than being a maximum at the central loading point in three point bending." [Line 110-112]
### 2.5 Simple Cantilever（简单悬臂）

- 英文原文定义：
"a simple cantilever with the test piece fixed at one end and loaded at the other." [Line 168-169]
- 位置：[Line 168-169]
- 使用场景摘录：
"The greater the angle of bend, the lower the stiffness and hence modulus of the material. The test is better suited to estimating relative modulus than in making absolute determinations." [Line 195-197]（ASTM D747 相关）
### 2.6 Flexural Stress Formula — 3-point, Rectangular（三点弯曲矩形梁弯曲应力）

- 英文原文定义：
"Flexural stress (σf) = 3Fl/2bh²" [Line 56]
- 位置：[Line 56]
- 使用场景摘录：
"More accurate expression … σF = 3Fl/2bh² (1 + 4s²/l²). Since s is typically very much less than L the second term in brackets makes only a very small contribution to the stress and can be ignored." [Line 81-92]
### 2.7 Flexural Modulus（弯曲模量 Ef）

- 英文原文定义：
"Ef = (l³ / 4bh³) × slope, where slope is the slope of force-deflection curve between reference strains (0.05% and 0.25% in ISO 178 [1])." [Line 68-75]
- 位置：[Line 68-75]
- 使用场景摘录：
"Modulus is defined in a similar way to tensile tests with strains of 0.05% and 0.25% again taken as the limiting values between which it is determined." [Line 373-374]
### 2.8 Flexural Strain Formula（弯曲应变）

- 英文原文定义：
"Flexural strain (εf) = 6hs/l²" [Line 57]
- 位置：[Line 57]
- 使用场景摘录：
"Flexural stress-strain characteristics are derived by monitoring both the force required to flex a material and the displacement that the material undergoes as a result of the applied force." [Line 15-17]
### 2.9 Circular Rod Formulae（圆棒公式）

- 英文原文定义：
"σF = 8Fl / πD³; Ef = (4l³ / 3πD⁴) × slope. Where D is the diameter of the rod." [Line 94-105]
- 位置：[Line 94-105]
- 使用场景摘录：直接给出圆棒形试样（而非矩形条）的专用计算公式。
### 2.10 Conventional Deflection, sC（常规挠度）

- 英文原文定义：
"Conventional deflection, sC: Deflection equal to 1.5 times the thickness, h, of the specimen. It is expressed in millimetres (mm)." [Line 226-228]
- 位置：[Line 226-228]
- 使用场景摘录：
"The conventional deflection is defined as 1.5 times the test piece thickness, which for the standard span of 16 times the thickness, equates to a strain of 3.5%." [Line 236-238]
### 2.11 Flexural Stress at Conventional Deflection, σfc（常规挠度下的弯曲应力）

- 英文原文定义：
"Flexural stress at conventional deflection, σfc: Flexural stress at the conventional deflection sC. Using the span l = 16h, the conventional deflection corresponds to a flexural strain of 3.5%." [Line 229-231]
- 位置：[Line 229-231]
- 使用场景摘录：
"The stress at this point forms a useful, if arbitrary, characteristic for ductile materials which occurs before the peak in the force-deflection curve is reached." [Line 237-239]
### 2.12 Toe Compensation（ toe 补偿）

- 英文原文定义：
"an appendix which advises on dealing with toe compensation. This is where there is an artifact at the beginning of the stress-strain curve due to take up of slack in the test system." [Line 189-191]
- 位置：[Line 189-191]
- 使用场景摘录：属于 ASTM D790 附录中的专门条款，用于修正应力-应变曲线起始段的伪影。
### 2.13 ISO 178 适用范围（覆盖材料）

- 英文原文定义：
"Thermoplastic moulding and extrusion materials, including filled and reinforced compounds … Thermosetting materials … Fibre reinforced thermoset and thermoplastic composites … Thermotropic liquid crystal polymers." [Line 199-218]
- 位置：[Line 199-218]
- 使用场景摘录：
"The method is not normally suitable for use with rigid cellular materials and sandwich structures containing cellular material." [Line 219-220]
### 2.14 Preferred Test Piece & Span Ratio（首选试样与跨厚比）

- 英文原文定义：
"Length: l = 80.0 ± 2.0 mm; Width: b = 10.0 ± 0.2 mm; Thickness: h = 4.0 ± 0.2 mm." [Line 310-312]
"The span is normally set to 16 ± 1 times the thickness." [Line 355-356]
- 位置：[Line 307-312]、[Line 355-356]
- 使用场景摘录：
"The length to thickness ratio shall be 20 (l/h = 20 ± 1)" [Line 325]
### 2.15 Strain Rate & Test Speed（应变速率与试验速度）

- 英文原文定义：
"In the absence of a material specification, the test speed is selected to give a strain rate as near as possible to 1% per minute which for the standard test piece is 2 mm/min." [Line 367-368]
- 位置：[Line 367-368]
- 使用场景摘录：表 9.1 给出推荐速度与容差：2 mm/min (±20%)、5 mm/min (±20%)、10 mm/min (±20%)、20 mm/min (±10%)、50 mm/min (±10%)、100 mm/min (±10%)、200 mm/min (±10%)、500 mm/min (±10%) [Line 256-269]
### 2.16 ISO 178 Jig Dimensions（夹具几何尺寸）

- 英文原文定义：
"R1 = 5.0 mm ± 0.1 mm (striking edge); R2 = 2.0 mm ± 0.2 mm for thickness ≤ 3 mm; R2 = 5.0 mm ± 0.1 mm for thickness > 3 mm." [Line 278-285]
- 位置：[Line 278-285]
- 使用场景摘录：配合 Figure 9.3 ISO 178 test arrangement 使用。[Line 301]
## 3. Evidence Tables（证据表）

### 表 3.1 公式与计算（Equations & Calculations）

|||||
|---|---|---|---|
|公式|三点弯曲 - 矩形梁应力|"Flexural stress (σf) = 3Fl/2bh²"|[Line 56]|
|公式|三点弯曲 - 矩形梁应变|"Flexural strain (εf) = 6hs/l²"|[Line 57]|
|公式|三点弯曲 - 矩形梁模量|"Ef = (l³ / 4bh³) × slope"|[Line 68-72]|
|公式|精确应力修正（含水平分量）|"σF = 3Fl/2bh² (1 + 4s²/l²)"|[Line 85-87]|
|公式|四点弯曲（载荷跨 = 支跨 1/3）应力|"Flexural Stress (σf) = Fl/bh²"|[Line 123-125]|
|公式|四点弯曲（载荷跨 = 支跨 1/3）应变|"Flexural Strain (εf) = 4.7hs/l²"|[Line 139]|
|公式|四点弯曲（载荷跨 = 支跨 1/2）应力|"Flexural Stress (σf) = 3Fl/4bh²"|[Line 141-143]|
|公式|四点弯曲（载荷跨 = 支跨 1/2）应变|"Flexural Strain (εf) = 4.36hs/l²"|[Line 145]|
|公式|Heap & Norman 应变公式|"εf = 4hs/lL²"|[Line 161-163]|
|公式|悬臂弯曲 - 矩形梁应力|"σf = 6Fl/bh²"|[Line 173]|
|公式|悬臂弯曲 - 矩形梁应变|"εf = 4Fl³/bh²s"|[Line 175]|
|公式|圆棒应力|"σF = 8Fl / πD³"|[Line 96-98]|
|公式|圆棒模量|"Ef = (4l³ / 3πD⁴) × slope"|[Line 101-103]|

### 表 3.2 参数定义（Parameter Definitions）

|||||
|---|---|---|---|
|参数|l — 支跨|"Support span - the length of the beam between the centres of the two outer supporting rods (mm)"|[Line 59-60]|
|参数|h — 梁厚|"The thickness of the beam (mm)"|[Line 61]|
|参数|b — 梁宽|"The width of the beam (mm)"|[Line 62]|
|参数|F — 力|"Force (N)"|[Line 63]|
|参数|s — 挠度|"Deflection of the specimen at mid span (mm)"|[Line 64]|
|参数|lL — 载荷跨|"Loading span – the distance between the centres of the two loading rods (mm)"|[Line 149]|
|参数|D — 圆棒直径|"Where D is the diameter of the rod."|[Line 105]|

### 表 3.3 标准与方法（Standards & Methods）

|||||
|---|---|---|---|
|国际标准|ISO 178 弯曲性能|"The international standard for flexural properties is ISO 178 [1]"|[Line 183-184]|
|ASTM 标准|ASTM D790 三点弯曲|"The corresponding ASTM standard is D790 [4] … an appendix which advises on dealing with toe compensation."|[Line 188-191]|
|ASTM 标准|ASTM D6272 四点弯曲|"a four point loading method given in ASTM D6272 [3] which uses a configuration with the loading span half of the support span."|[Line 192-193]|
|ASTM 标准|ASTM D747 悬臂表观弯曲模量|"ASTM D747 [5] … a strip of material is clamped in a vice and the load applied through a pivot point"|[Line 193-196]|
|设备标准|ISO 5893 试验机|"a test machine complying with ISO 5893 [7] with force measurement to grade A"|[Line 245-247]|
|预处理标准|ISO 291|"ISO 178 does not give specific recommendations for conditioning but reference is made to ISO 291 [8]."|[Line 364-365]|
|拉伸通则|ISO 527-1|"flexural definitions … are analogous to the tensile test definitions set out in ISO 527-1 General Principles"|[Line 222-224]|

### 表 3.4 材料适用范围（Applicable Materials）

|||||
|---|---|---|---|
|适用|热塑性注塑/挤出材料（含填充、增强）|"Thermoplastic moulding and extrusion materials, including filled and reinforced compounds in addition to unfilled types; rigid thermoplastic sheets"|[Line 201-203]|
|适用|热固性材料及层压板|"Thermosetting materials, including filled and unreinforced compounds; thermosetting sheets, including laminates"|[Line 209-211]|
|适用|纤维增强复合材料|"Fibre reinforced thermoset and thermoplastic composites, incorporating unidirectional or non-unidirectional reinforcements such as mat, woven fabrics, woven rovings, chopped strands, combination and hybrid reinforcements, rovings and milled fibres; sheets made from pre-impregnated materials (prepregs)"|[Line 212-215]|
|适用|热致液晶聚合物|"Thermotropic liquid crystal polymers."|[Line 217-218]|
|不适用|硬质泡沫/夹层结构|"The method is not normally suitable for use with rigid cellular materials and sandwich structures containing cellular material."|[Line 219-220]|

### 表 3.5 试样尺寸与试验条件（Test Piece Specs & Test Conditions）

|||||
|---|---|---|---|
|试样数|最少 5 件|"A minimum of five test pieces are required by ISO 178 for each direction tested."|[Line 307]|
|首选尺寸|长/宽/厚|"Length: l = 80.0 ± 2.0; Width: b = 10.0 ± 0.2; Thickness: h = 4.0 ± 0.2"|[Line 310-312]|
|厚度公差|中段 1/3 偏差不超 2%|"The thickness of the central third of the specimen length shall not deviate by more than 2%."|[Line 316-317]|
|宽度公差|中段 1/3 偏差不超 3%|"The width of the central third of the specimen length shall not deviate by more than 3%."|[Line 319]|
|截面要求|矩形、无圆角边|"The specimen must have a rectangular cross section with no rounded edges."|[Line 321]|
|长厚比|l/h = 20 ± 1|"The length to thickness ratio shall be 20 (l/h = 20 ± 1)"|[Line 325]|
|跨厚比|16 ± 1 倍|"The span is normally set to 16 ± 1 times the thickness"|[Line 355-356]|
|速度|标准应变速率 ~1%/min|"the test speed is selected to give a strain rate as near as possible to 1% per minute which for the standard test piece is 2 mm/min"|[Line 367-368]|
|刚度精度|力/位移精度 1% F.S.|"The requirements for measurement of force and deflection are given as within 1% of full scale."|[Line 246-248]|

### 表 3.6 夹具几何参数（Jig Geometry）

|||||
|---|---|---|---|
|加载边半径 R1|5.0 ± 0.1 mm|"R1 = 5.0 mm ± 0.1 mm"|[Line 281]|
|支撑半径 R2 (≤3 mm)|2.0 ± 0.2 mm|"R2 = 2.0 mm ± 0.2 mm for thicknesses of test specimen ≤ 3 mm"|[Line 283]|
|支撑半径 R2 (>3 mm)|5.0 ± 0.1 mm|"R2 = 5.0 mm ± 0.1 mm for thicknesses of the test specimen > 3 mm"|[Line 285]|

## 4. Chapter Connections（章节衔接分析）

本章 "Flexural Stress-Strain" 在书整体结构中的位置与关联如下：

与 Chapter 6 (Tensile Stress-Strain) 的对偶关系
本章开篇即明确点出与 Chapter 6 拉伸测试的关系："… almost as commonly measured as the tensile properties considered in Chapter 6." [Line 8-9]。文中多处与拉伸测试对照："as in the case of tensile testing" [Line 52]；"modulus is defined in a similar way to tensile tests with strains of 0.05% and 0.25%" [Line 373-374]；"flexural definitions … are analogous to the tensile test definitions set out in ISO 527-1" [Line 222-224]。这种"拉伸-弯曲"的双轴对偶结构，构成了短时力学测试章节的核心框架。

拉伸模量 (Ch6) 与弯曲模量 (Ch9) 的"同一参数、不同层次"关系
两者虽参数体系相同（应力、应变、模量），但弯曲测试测的是外层纤维，"they refer to the outer layer of the material rather than the bulk" [Line 22-23]，因各向异性"the results will only approximately equate to those from tensile tests" [Line 23-24]。这种"近似对应"是理解整本书力学测试章节的关键。

与 Chapter 10 (Compression, 推测) 的载荷模式序列
文件末尾 [Line 419] 出现 "10"，预示 Chapter 10 主题。本章覆盖的三种弯曲载荷模式（三点/四点/悬臂）与 Ch6 拉伸、Ch10 压缩共同构成"基本机械载荷测试家族"。

标准体系的横向呼应
本章引用的标准（ISO 178、ASTM D790、ASTM D6272、ASTM D747、ISO 5893、ISO 527-1、ISO 291）与拉伸测试章节使用的标准（ISO 527 系列、ASTM D638 等）形成完整的测试标准族。ISO 5893 试验机标准、ISO 291 预处理标准是跨章节共用的基础设施。

"Conventional Deflection" 是弯曲章节独有的术语创新
文中明确指出："The term stress at the conventional deflection is unique to the flexural test." [Line 233-234]。这一概念在拉伸/压缩章节中不存在，是本章独有的概念贡献。

从"绝对测定"到"相对估算"的方法光谱
悬臂法（ASTM D747）"better suited to estimating relative modulus than in making absolute determinations" [Line 196-197]，与 ISO 178 三点弯曲的绝对测定形成精度光谱的两端——这种光谱在其他载荷模式章节中也反复出现。

## 5. Business Connections（卫材行业应用价值分析）

本章讨论的弯曲应力-应变测试在卫生材料（卫材）行业有重要的实际意义，特别是对于湿巾/卫生巾的芯体、SAP、无纺布、胶黏剂以及采购成本管控。

### 5.1 芯体（Composite Body / Fluff-SAP Composite）

- 芯体刚性评价：湿巾或卫生用品芯体在包装、运输和消费者使用中的"挺括感"（body feel）直接取决于弯曲刚度。ISO 178 三点弯曲提供的 Ef（弯曲模量） 是芯体设计的关键指标。
- 外层 vs 整体的意义：文中强调弯曲测的是"the outer layer of the material rather than the bulk" [Line 22-23]。芯体（绒毛纤+SAP 混合层）的厚度方向各向异性显著，外层纤维（靠近无纺布面层）的刚度往往与芯部不同——这解释了为什么弯曲测试数据对芯体更有预测价值，而拉伸数据可能低估芯体表面行为。
- 各向异性预警："plastics are seldom completely isotropic through the thickness, the results will only approximately equate to those from tensile tests" [Line 23-24]。芯体是典型的多层复合材料（无纺布+纤维+SAP+无纺布），各向异性更强，采购/品质评估时不能直接用拉伸数据替代弯曲数据。
### 5.2 SAP（Superabsorbent Polymer 高吸水性树脂）

- SAP 粉末/粒子的弯曲行为：SAP 吸水后的凝胶颗粒在芯体中呈现软质、类泡沫的行为，ISO 178 明确"not normally suitable for use with rigid cellular materials and sandwich structures containing cellular material" [Line 219-220]。这提示：对纯 SAP 凝胶态不宜直接使用标准弯曲测试，但对其在芯体中的应用，跨厚比 l/h = 20 ± 1 [Line 325] 或调整跨厚比 [Line 355-356] 可能成为变通方案。
- 湿态模量评价：SAP 吸水后整个芯体变软，弯曲模量下降。弯曲测试可以作为"吸水前后刚度保持率"的量化指标——对湿巾行业来说，这是使用体验（wiping performance）的核心 KPI。
### 5.3 无纺布（Nonwoven）

- 无纺布的弯曲刚度直接关联手感：消费者"摸"到的柔软度主要反映在弯曲性能上，而非拉伸。ISO 178 覆盖"rigid thermoplastic sheets" [Line 202]，无纺布虽常为柔性，但通过调整 span-to-thickness ratio（文中允许"higher span to thickness ratios" [Line 356]）可以适应。
- 常规挠度 sC 的应用：对柔韧无纺布材料，通常不会断裂："with ductile materials the test piece does not reach a point of fracture, it simply keeps bending" [Line 234-235]。此时 σfc（常规挠度下的弯曲应力） 是比"断裂强度"更有意义的指标，可作为无纺布柔软度/挺度分级的采购规格参数。
- 四点弯曲优势：对纺织纤维增强复合材料，ISO 178 明确"four point bending is said to be under consideration for certain textile-fibre-reinforced plastics" [Line 185-186]。无纺布在本质上是纺织纤维材料，使用四点弯曲时"the stress is uniformly distributed between the loading supports" [Line 110-112]，更接近其实际使用中的载荷模式。
### 5.4 胶黏剂（Adhesive / Hotmelt）

- 层间粘结质量评价：芯体-无纺布-胶黏剂的复合层压结构在使用中受弯。弯曲测试可间接反映胶黏剂的层间结合强度——若胶黏剂失效，弯曲模量会显著下降，且可能出现脱层（delamination）。文中提到纤维复合材料中"to avoid delamination"需要调整跨厚比 [Line 356]。
- 胶黏剂本身作为薄层材料：胶黏剂涂布层的厚度通常 < 3 mm，对应 R2 = 2.0 ± 0.2 mm 的支撑半径 [Line 283]，且 span 需按跨厚比 16:1 设定 [Line 355]。
### 5.5 采购成本（Procurement Cost）

- 用弯曲模量替代拉伸模量作为采购验收指标：由于芯体/无纺布在实际使用中的载荷以弯曲为主（被折叠、被揉捏、被包装挤压），"most components are subject to a mixture of loading modes, and flexing or bending often occurs by intent or accident" [Line 9-11]。以弯曲模量为验收规格比拉伸模量更能反映实际使用体验，从而避免因过度依赖拉伸数据而导致的"表面合格、实际不佳"采购风险。
- 试样制备成本优势：文中提到"a strip test piece is easier to produce than a dumbbell and there are no gripping problems" [Line 12-13]。对供应商/采购方来说，弯曲试样更容易制备、测试更稳定、人工/设备成本更低，有利于高频次的来料抽检。
- 精度约束带来的成本权衡：文中指出对柔性材料"0.05% strain corresponds to a deflection of the outer surface of only 0.08 mm"，对设备精度要求极严 [Line 376-378]。这提示：采购时若需严格区分供应商的细微差异，需投资高精度（Grade A，1% F.S. [Line 246-248]）测试设备，这是一项资本性支出 (CAPEX) 决策。
- 相对 vs 绝对测定的成本-精度平衡：悬臂法（ASTM D747）适合"relative modulus"快速筛查 [Line 196-197]，可在供应商端作为低成本快速筛除工具，而 ISO 178 用于关键供应商的绝对确认，形成两级采购质量控制体系。
## 6. Key Quotes Index（金句索引）

### Quote 1

- 英文原文："The short-term flexural characteristics of a material are almost as commonly measured as the tensile properties considered in Chapter 6. This is not surprising considering the fact that most components are subject to a mixture of loading modes, and flexing or bending often occurs by intent or accident." [Line 8-13]
- 中文翻译：材料的短时弯曲特性几乎和拉伸特性一样经常被测量。这并不令人惊讶，因为大多数部件都会受到多种载荷模式的共同作用，弯曲或折弯往往是有意为之或意外发生的。
### Quote 2

- 英文原文："Flexural tests also have the advantage that a strip test piece is easier to produce than a dumbbell and there are no gripping problems as can occur in tensile tests." [Line 11-13]
- 中文翻译：弯曲测试还有一个优点：条状试样比哑铃形试样更容易制备，而且不会出现拉伸测试中常见的夹持问题。
### Quote 3

- 英文原文："The stress and strain that are calculated are the maximum outer fibre stresses and strains and that the stress calculations given later in the chapter are only valid up to a maximum fibre strain of 5%. … they refer to the outer layer of the material rather than the bulk." [Line 18-23]
- 中文翻译：计算出的应力和应变是最大外层纤维的应力和应变，本章后面给出的应力计算公式仅在纤维应变不超过 5% 时才有效。……它们对应的是材料的外层，而不是整体。
### Quote 4

- 英文原文："Because plastics are seldom completely isotropic through the thickness, the results will only approximately equate to those from tensile tests." [Line 23-24]
- 中文翻译：因为塑料在厚度方向上很少是完全各向同性的，弯曲测试结果只能近似等同于拉伸测试结果。
### Quote 5

- 英文原文："The advantage of four point loading is that the stress is uniformly distributed between the loading supports rather than being a maximum at the central loading point in three point bending." [Line 110-112]
- 中文翻译：四点弯曲的优点是：应力在两个加载支撑点之间均匀分布，而不是像三点弯曲那样在中心加载点达到最大值。
### Quote 6

- 英文原文："The term stress at the conventional deflection is unique to the flexural test. Generally with ductile materials the test piece does not reach a point of fracture, it simply keeps bending until eventually is slips from the outer supports." [Line 233-236]
- 中文翻译：常规挠度下的应力这一术语是弯曲测试独有的。通常对于韧性材料，试样并不会达到断裂点，而是一直弯折，直到最终从外侧支撑上滑落。
### Quote 7

- 英文原文："The conventional deflection is defined as 1.5 times the test piece thickness, which for the standard span of 16 times the thickness, equates to a strain of 3.5%." [Line 236-238]
- 中文翻译：常规挠度被定义为试样厚度的 1.5 倍；对于 16 倍厚度的标准跨距，这对应于 3.5% 的应变。
### Quote 8

- 英文原文："The test is better suited to estimating relative modulus than in making absolute determinations." [Line 196-197]
- 中文翻译：该测试（ASTM D747 悬臂法）更适合用于估算相对模量，而非进行绝对测定。
### Quote 9

- 英文原文："This places very severe constraints on the accuracy of the test equipment and the test piece itself. For the standard test piece, 0.05% strain corresponds to a deflection of the outer surface of only 0.08 mm from its starting point." [Line 374-378]
- 中文翻译：这对测试设备的精度和试样本身都提出了非常严格的要求。对于标准试样，0.05% 的应变对应于外表面仅有 0.08 mm 的位移。
### Quote 10

- 英文原文："By far the most common is three point loading. As the name implies, this mode of loading is achieved by applying the force to the specimen at three points." [Line 32-33]
- 中文翻译：迄今为止最常见的是三点加载。顾名思义，这种加载方式是通过在试样的三个点上施加力来实现的。

报告结束。


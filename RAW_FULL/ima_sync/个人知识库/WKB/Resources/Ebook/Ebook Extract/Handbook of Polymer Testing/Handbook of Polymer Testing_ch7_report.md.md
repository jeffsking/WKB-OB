---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_e3424865e6c03babd04102ec10526583001a693ee6c0644e"
source_file: "Handbook of Polymer Testing_ch7_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Polymer Testing/Handbook of Polymer Testing_ch7_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Handbook of Polymer Testing_ch7_report.md.md

# Chapter 7 Deep-Reading Report: Compression Stress-Strain

Source: Handbook of Polymer Testing – Short-Term Mechanical Tests
Author: Edward N. Brown (Rapra, 2002)
Chapter: 7 – Compression Stress-Strain

## 1. Core Arguments（核心论点）

||||
|---|---|---|
|1|"It is logical to determine compression stress-strain characteristics of materials when they are to be used in this mode of deformation. For softer materials such as foams and rubbers this is often the case and the experimental approach is relatively straightforward, although complicated by shape factor effects."|[Line 9-12]|
|2|"Rigid plastics are also frequently subjected to compressive stresses but in most applications, shear or tensile stresses are more important. However, even if the shear modulus is not of prime interest the geometry of components can be such that buckling is a potential problem."|[Line 12-15]|
|3|"Because the stress-strain relationship is generally not linear and because of shape factor effects, care must be taken to compare only measures of compressive stiffness defined in the same way."|[Line 28-30]|
|4|"This geometry will improve the accuracy of modulus measurements of stiff materials where the strains are small but the slenderness ratio must be chosen to avoid buckling at the strains likely to be reached during the test."|[Line 34-37]|
|5|"Short, squat, test pieces are much less prone to buckling than tall, slender, test pieces and hence there are certain restrictions placed on the ratio of key dimensions."|[Line 88-90]|
|6|"ASTM D695 gives rather more information on the nature of compression stress-strain curves and more detail of suitable compression devices... The expression of results is different to ISO, in particular modulus is obtained from a tangent to the initial linear portion of the stress-strain curve."|[Line 177-184]|

## 2. Key Concepts with Operationalized Definitions

### 2.1 Shape Factor Effects

- 英文定义： "Although buckling is not then an issue, the ratio of height to area is important, together with whether or not the test piece is lubricated, because of shape factor effects." [Line 17-20]
- 场景摘录： "If there were perfect slippage, every element of the test piece would be subjected to the stress and strain and a cylindrical test piece would remain a true cylinder without barrelling." [Line 22-26] — Shape factor determines whether the specimen remains a uniform cylinder or exhibits barrelling (lateral bulging), directly affecting stress distribution accuracy.
- 操作含义：在对比压缩刚度数据时，必须确保测试件的高/面积比和润滑条件一致，否则数据不可比。
### 2.2 Buckling（屈曲/失稳）

- 英文定义： "The relationship between the parameters which govern buckling is given as: εc* ≤ 0.4(x/l)²" [Line 99-102]
- 场景摘录： "As mentioned earlier, buckling is an important consideration in compression tests. Short, squat, test pieces are much less prone to buckling than tall, slender, test pieces." [Line 87-90]
- 操作含义：测试件长细比 x/l 须满足标准推荐值——测模量时 ≥ 0.08，其他测试 ≥ 0.4 [Line 114-117]，否则屈曲会导致数据失效。
### 2.3 Compressive Strain vs. Nominal Compressive Strain

- 英文定义： "A distinction is made between compressive strain (based on the change in length between gauge marks) and nominal compressive strain (based on change in length of the test piece), but the significance of this is not obvious." [Line 77-81]
- 场景摘录： "Gauge marks are required to measure compressive modulus if an optical method is used to measure change in length but the magnitude of the gauge length is not specified." [Line 128-130]
- 操作含义：真应变（基于标距标记）与名义应变（基于试件全长）的差异在聚合物中可能因大变形而显著，选择哪种定义直接影响模量计算结果。
### 2.4 Slenderness Ratio（长细比）

- 英文定义： "The two key dimensions are the test piece length (the direction along which the compressive force is applied) and the critical dimension at right angles to this." [Line 95-97]
- 场景摘录： "The smaller ratio for the modulus test is given since the strain range required for the test is so small and hence the point of buckling is unlikely to be reached." [Line 115-117]
- 操作含义：长细比直接决定测试模式（压缩 vs. 屈曲 vs. 剪切破坏），ISO 604 对模量和强度测试分别规定了不同的试件尺寸偏好。
### 2.5 Lubrication / End-Face Treatment（端面试件润滑处理）

- 英文定义： "The effect of whether or not the ends of test pieces are lubricated is mentioned in a note and for most precise measurements it is recommended that they are either lubricated or discs of fine abrasive paper be used between test piece and platens!" [Line 154-156]
- 场景摘录： "either with perfect slippage between the test piece and compressing members of the apparatus or with complete absence of slip." [Line 22-24]
- 操作含义：两端润滑消除摩擦约束（模拟纯压缩），砂纸则强制固结（模拟无滑移边界条件）。两种极端分别对应不同应力状态，不可混用。
### 2.6 Compressive Modulus Definition

- 英文定义： "The only compression modulus considered is that obtained from the difference between the stresses at 0.05 and 0.25% strain, which would only be reasonable for materials within a particular band of stiffness." [Line 160-162]
- 场景摘录： ASTM D695 采用不同方法： "modulus is obtained from a tangent to the initial linear portion of the stress-strain curve." [Line 183-184]
- 操作含义：ISO 604 的割线法（0.05%–0.25%应变差）与 ASTM D695 的切线法本质不同，跨标准比较模量数据时必须注意定义差异。
## 3. Evidence Tables

### 3.1 标准与规范对比

|||||
|---|---|---|---|
|ISO 标准|ISO 604 覆盖塑料压缩性能测量，但不覆盖纺织增强塑料、蜂窝材料和夹层结构|"The measurement of compressive properties of plastics generally is covered by ISO 604 [3]. It is specifically not intended to cover textile reinforced plastics, cellular materials and sandwich constructions involving cellular materials"|[Line 72-75]|
|国家标准|BS EN ISO 604 与 ISO 604 完全一致|"The corresponding standard British standard is identical and numbered as BS EN ISO 604 [3]"|[Line 168-169]|
|ASTM 标准|ASTM D695 技术上与 ISO 等价但存在多项差异|"The ASTM standard is D695 [5] which is said to be technically equivalent to the ISO method but, as is often the case with ASTM standards so described, has a number of differences."|[Line 169-171]|
|ASTM 差异|试件形状、测试速度、模量定义均不同|"The test pieces are different and include provision for fibre reinforced materials and syntactic foam as well as a dumbbell shape (with supporting jig) for thin materials... The standard test speed is 1.3 mm/min."|[Line 178-182]|
|特种标准|BS 2782-3 Method 346A 测量层压管层间黏聚力|"BS 2782-3 Method 346A [6] has a compression test which measures the cohesion between layers of laminated tube."|[Line 186-187]|

### 3.2 试件尺寸与测试参数

|||||
|---|---|---|---|
|试件尺寸（模量）|首选尺寸|"for modulus: length = 50 mm, width = 10 mm and thickness = 4 mm"|[Line 121]|
|试件尺寸（强度）|首选尺寸|"for strength: length = 10 mm, width = 10 mm and thickness = 4 mm"|[Line 122]|
|端面对齐|平行度要求|"Test pieces for compression testing must have very flat and parallel end faces, parallelism to 0.025 mm normal to the long axis of the test piece being required."|[Line 85-86]|
|测试速度（模量）|与试件长度相关|"For modulus, the speed should be that closest in value to 5% of the specimen length."|[Line 136-137]|
|测试速度（脆性材料）|与试件长度相关|"For strength tests on brittle materials the speed should be closest to 10% of the specimen length"|[Line 137-138]|
|测试速度（韧性材料）|与试件长度相关|"and for ductile materials to 50% of this length."|[Line 138]|
|屈曲临界公式|εc* ≤ 0.4(x/l)²|"This equation is based on linear stress-strain behaviour"|[Line 99-112]|
|长细比推荐|模量 ≥ 0.08；其他 ≥ 0.4|"an x/l ratio of not less than 0.08 is recommended for measuring modulus and for other tests not less than 0.4."|[Line 114-115]|

### 3.3 设备与测试方法

|||||
|---|---|---|---|
|测试设备|通用试验机配合压缩力传感器|"There are test machines available which are specifically designed for compression testing but generally a universal test machine, also used for tensile, flexural tests, etc., is used."|[Line 49-50]|
|对中重要性|压板对中极其关键|"It will be appreciated that the alignment of the loading platens is extremely important."|[Line 52-54]|
|设备刚度|需要高刚度|"Because of the high forces and relatively small deformations it is also necessary that the machine has high stiffness."|[Line 60-61]|
|应变测量|首选压板位移或标距标记|"Strain is preferably measured by movement of the compression platens (or gauge marks on the test piece) by means of a convenient transducer, which in its simplest form could be a dial gauge."|[Line 63-65]|
|橡胶/泡沫测试|可借用橡胶测试方法|"For soft plastics, compressive stress-strain properties are sensibly made by adaptation of rubber testing methods [2]."|[Line 32-33]|
|柔性材料试件|高度小于压缩面积|"Standard compression tests on rubbers and foams are carried out on test pieces with height significantly smaller than compressed area, usually a disk or short cylinder."|[Line 17-18]|

### 3.4 其他/特殊测试方法

|||||
|---|---|---|---|
|平面应变压缩|Williams & Ford (1960s) 开发，通过润滑金属条施加厚度方向压缩|"Williams and Ford [9] evaluated the plain strain compression test, which was developed for metals, for determining total and residual deformation in plastics up to high levels of stress"|[Line 199-203]|
|体积模量压缩|Warfield 等人封装试件同时测量压缩与体积模量|"Warfield and co-workers [10] devised a compression test where the test piece was enclosed such that both compression and bulk modulus could be measured"|[Line 206-208]|
|环形直径压缩|用于复合圆柱结构的完整性评估|"A particular form of test for composite cylindrical structures is to load a ring diametrically in compression."|[Line 210-212]|
|层间黏聚力|BS 2782-3 层压管压缩|"measures the cohesion between layers of laminated tube"|[Line 186-187]|

## 4. Chapter Connections

本章位于 Handbook of Polymer Testing – Short-Term Mechanical Tests 的中间位置，其章节衔接关系如下：

与前章的衔接：
- 本书前几章已覆盖拉伸（Tensile）、弯曲（Flexural）和剪切（Shear）等短期力学测试。本章作为压缩应力-应变专题，逻辑上承接"当材料将以压缩方式变形时，测定其压缩特性是合乎逻辑的"这一基本前提 [Line 9-10]。
- 第 7.1 节明确对比了压缩与拉伸/弯曲测试的差异：刚性塑料"在大多数应用中，剪切或拉伸应力更为重要" [Line 12-14]，但几何因素（如屈曲）使得压缩测试具有不可替代的工程价值。
- 章节提到对软质塑料，压缩测试方法"通过改造橡胶测试方法来合理实现" [Line 32-33]，暗示了对前文橡胶测试章节的方法学延续。

与后章的衔接：
- 第 7.4 节"Other Tests"部分讨论了纤维增强复合材料的压缩测试 [Line 193-197]，这为后续涉及复合材料专项测试的章节做了过渡铺垫。
- ISO 604 修订正在"考虑中" [Line 164-166]，暗示标准演化的动态性，可能指向后续章节对标准更新的讨论。

内部结构：
- 7.1 Introduction（理论框架与形状因子）→ 7.2 Test Apparatus（设备与精度要求）→ 7.3 Standard Tests（ISO 604 / ASTM D695 / BS 标准的系统对比）→ 7.4 Other Tests（扩展方法与历史发展），形成从原理→设备→标准化→拓展的完整知识链。
- 作者对 ISO 604 的试件设计提出明确批评："This treatment of test pieces could hardly be called elegant standardisation." [Line 132]，这一评价贯穿全文，体现了作者对标准化一致性的核心关切。

## 5. Business Connections（卫材行业应用分析）

卫生用品行业（纸尿裤、卫生巾、失禁用品等）的核心材料体系——芯体吸收树脂（SAP）、无纺布（纺粘/水刺）、胶黏剂、背层膜——在生产和使用工况中均涉及压缩行为，本章内容在以下维度具有直接应用价值：

### 5.1 SAP 芯体压缩回弹与形状因子

- 应用场景：SAP 凝胶体在尿吸收后承受人体坐姿/卧姿压缩载荷。本章强调的"shape factor effects" [Line 11, 17-20, 28-30] 直接影响 SAP 芯体在包装形态（长条形 vs. 块状）下的压缩行为。
- 操作启示：SAP 凝胶压缩时高/面积比极小（类似本章所述泡沫/橡胶测试条件），应参照 ISO 7743（橡胶压缩）[Line 36-37, 236-237] 的方法进行表征。润滑/无润滑边界条件的选择 [Line 154-156] 对应芯体在干态（无纺布包裹、近似无滑移）与湿态（凝胶液相润滑）下的不同应力状态。
- 价值点：避免不同供应商提供的 SAP 压缩回弹数据因测试条件不一致而导致的选型误判。
### 5.2 无纺布层间黏合力与压纹压缩

- 应用场景：卫生用品面层/导流层通过超声波或热压形成点状/线状压纹结构，其功能本质是局部压缩成型。层间黏合力直接受层压管压缩测试（BS 2782-3 Method 346A）[Line 186-187] 方法启发。
- 操作启示：本章对试件端面平行度（0.025 mm）[Line 85-86] 和压板对中的严苛要求 [Line 52-54]，可类比到压纹辊筒的平行度与对中控制——若对中公差超标，压纹深度不均将导致导流失效。
- 价值点：将实验室压缩测试的精度要求迁移到生产设备（压纹机）的公差管理，提升产品一致性。
### 5.3 复合结构屈曲与芯体支撑

- 应用场景：多层复合结构（面层/导流层/SAP 芯/防漏层/底膜）在受压时存在屈曲风险，尤其是窄幅产品（如护垫）。本章屈曲公式 εc* ≤ 0.4(x/l)² [Line 99-102] 可定性评估不同芯体长宽比设计下的结构稳定性。
- 操作启示：当芯体设计为长条形且宽度较小时（小 x/l 比），即使材料本身压缩性能良好，几何屈曲仍可能导致使用中塌陷。推荐 x/l ≥ 0.4 的经验值 [Line 114-115] 可作为芯体设计的初步几何准则。
- 价值点：在 SAP 用量和芯体尺寸的设计平衡中，将屈曲风险量化纳入工程决策。
### 5.4 胶黏剂压缩剥离与层间完整性

- 应用场景：腰围贴、防漏隔边胶等胶黏件在穿戴状态下承受循环压缩载荷，其层间完整性（cohesion）评估可借鉴 BS 2782-3 层压管压缩方法 [Line 186-187]。
- 操作启示：本章提出的环形直径压缩法 [Line 210-212] 可直接映射到腰围/护围的环状压缩完整性测试——"stiffness can be derived but such a test can be considered as a practical evaluation of integrity" [Line 211-212]。
- 价值点：为胶黏剂选型提供超越"初黏/持黏"的第三维度——压缩工况下的层间保持力。
### 5.5 采购成本与供应商数据可比性

- 应用场景：采购部门对比不同供应商的 SAP 压缩回弹、无纺布挺度等数据时，常遇到数据不可比的问题。本章明确指出"care must be taken to compare only measures of compressive stiffness defined in the same way" [Line 28-30]。
- 操作启示：ISO 604 的模量定义（0.05%–0.25% 割线法）[Line 160-162] 与 ASTM D695 的切线法 [Line 183-184] 本质不同，速度选择（1, 2, 5, 10, 20 mm/min 中依材料特性选定）[Line 134-139] 也显著影响结果。
- 价值点：在供应商 RFP 中强制统一测试标准（方法、试件尺寸、速度、润滑条件），避免因数据不可比导致的采购误判和成本浪费。本章对 ISO 604 试件标准不统一的批评 [Line 132] 正是供应商管理中的典型陷阱。
### 5.6 材料刚度与模量表征的一致性

- 应用场景：不同批次的无纺布/底膜供应商需提供一致的压缩模量数据。本章对测试机刚度的要求——"it is also necessary that the machine has high stiffness" [Line 60-61]——直接适用：若企业实验室设备刚度不足，测得的模量将系统性偏高。
- 价值点：在采购实验室设备（如万能试验机）时，将"压缩工况下的刚度要求"纳入技术规格，避免因设备选型不当导致的来料检验数据失真。

## 6. Key Quotes Index（金句索引）

|||||
|---|---|---|---|
|1|"For softer materials such as foams and rubbers this is often the case and the experimental approach is relatively straightforward, although complicated by shape factor effects."|对于泡沫和橡胶等较软的材料，这种情况经常出现，实验方法相对简单，但会因形状因子的影响而变得复杂。|[Line 10-12]|
|2|"Because the stress-strain relationship is generally not linear and because of shape factor effects, care must be taken to compare only measures of compressive stiffness defined in the same way."|由于应力-应变关系通常是非线性的，且存在形状因子效应，在比较时必须谨慎，只能比较以相同方式定义的压缩刚度测量值。|[Line 28-30]|
|3|"The alignment of the loading platens is extremely important."|加载压板的对中极其重要。|[Line 52-54]|
|4|"Short, squat, test pieces are much less prone to buckling than tall, slender, test pieces and hence there are certain restrictions placed on the ratio of key dimensions."|矮胖的试件比细长的试件更不容易发生屈曲，因此对关键尺寸之比有一定的限制。|[Line 88-90]|
|5|"This treatment of test pieces could hardly be called elegant standardisation."|这种试件的处理方式实在很难称得上是优雅的标准化。|[Line 132]|
|6|"For most precise measurements it is recommended that they are either lubricated or discs of fine abrasive paper be used between test piece and platens!"|对于最精确的测量，建议试件要么润滑，要么在试件和压板之间使用细砂纸圆盘！|[Line 154-156]|
|7|"The only compression modulus considered is that obtained from the difference between the stresses at 0.05 and 0.25% strain, which would only be reasonable for materials within a particular band of stiffness."|唯一考虑的压缩模量是从 0.05% 和 0.25% 应变处的应力差获得的，这只对特定刚度范围内的材料是合理的。|[Line 160-162]|
|8|"ASTM D695 gives rather more information on the nature of compression stress-strain curves and more detail of suitable compression devices."|ASTM D695 提供了更多关于压缩应力-应变曲线特性的信息以及更详细的合适压缩设备细节。|[Line 177-178]|
|9|"Although it appears to be a useful practical test it has not been taken up by standards committees."|尽管它似乎是一个有用的实用测试，但并未被标准委员会采纳。|[Line 203-204]|
|10|"A particular form of test for composite cylindrical structures is to load a ring diametrically in compression. Stiffness can be derived but such a test can be considered as a practical evaluation of integrity."|复合圆柱结构的一种特殊测试形式是对环进行径向往复压缩加载。可以推导出刚度，但这样的测试可被视为对结构完整性的实用评估。|[Line 210-212]|

Report generated for Chapter 7 – Compression Stress-Strain. Total lines analyzed: 270. All citations reference original text line numbers from the source file.


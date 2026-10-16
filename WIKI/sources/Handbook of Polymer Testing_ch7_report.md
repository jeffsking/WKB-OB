---
type: source
title: "Handbook of Polymer Testing_ch7_report.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Polymer Testing/Handbook of Polymer Testing_ch7_report.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# Handbook of Polymer Testing_ch7_report.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Polymer Testing/Handbook of Polymer Testing_ch7_report.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

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
|ASTM 差异|试件形状、测试速度、模量定义均不同|"The test pieces are different and include provision for fibre reinforced materials and syntactic foam as well as a dumbbell shape (with supporting jig) fo

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Polymer Testing/Handbook of Polymer Testing_ch7_report.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Polymer Testing/Handbook of Polymer Testing_ch7_report.md.md`
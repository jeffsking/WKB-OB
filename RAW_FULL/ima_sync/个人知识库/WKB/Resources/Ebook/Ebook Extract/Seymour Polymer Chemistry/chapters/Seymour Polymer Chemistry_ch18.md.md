---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_660cea63313ca297eb94b195923cfcc2001a693ee6c0644e"
source_file: "Seymour Polymer Chemistry_ch18.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Seymour Polymer Chemistry/chapters/Seymour Polymer Chemistry_ch18.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Seymour Polymer Chemistry_ch18.md.md

# Seymour Polymer Chemistry — Chapter 18 Deep-Dive

## Chapter 18: Special Topics

文件名: seymour_ch18.txt
文件长度: 401,041 chars
页码约定: 原文 .txt 文件无正式印张页码；本报告以原文行号（line no.）作为定位引用。

## 执行摘要（Executive Summary）

第18章是全书前沿与跨学科拓展，跨越导电聚合物、非传统加工、废物管理与可持续性、反应工程、组合化学、生物化学、光学纤维、材料选择等多个学科。本章是 2000 年前后聚合物前沿研究的全景图——从诺贝尔奖级别的导电聚合物（2000 年 MacDiarmid/Heeger/Shirakawa）到分子导线、纳米纤维、组合化学、蛋白质组学、材料选择图——代表聚合物学科从"材料科学"向"材料-信息-生物"三大学科交叉融合的方向。

对卫材业务的意义相对间接，但以下方向值得关注：
- 导电聚合物/纳米纤维：卫材的智能化（可监测湿度的智能尿布传感器）
- 材料选择图：为卫材"轻量化"（减轻塑料使用量、增强强度同时减薄）提供定量决策工具
- 可持续/废物：卫材是"一次性产品"的典型代表，本章的废物讨论直接映射卫材的环境议题
- 反应器动力学（CSTR/PFR/batch）：SAP 工业生产的反应器选择

## Step 1 — 宏观解读（Macro Interpretation）

### 1.1 核心论题

- 主论题：聚合物的未来在"超越传统塑料"——导电、发光、可编程、可降解、智能化、可精确选择
- 副论题：（a）导电聚合物的关键是"共轭双键 + 掺杂"——把聚合物从绝缘体变成半导体/导体；（b）聚合物反应器类型决定分子量分布与生产效率；（c）材料选择通过 performance index 定量优化；（d）组合化学 + 蛋白质组学代表"高通量材料发现"的新范式
### 1.2 论证结构

- 导电聚合物层（§18.1）：共轭双键 → 掺杂 → 从绝缘体到导体
- 分子导线/纳米层：molecular wires / nanofibrils / nanotubes
- 固体废物/可持续层（§18.3）：聚合物是固体废物主体；紫外降解机制
- 反应器层：batch / PFR / CSTR 的聚合动力学
- 组合化学层（§18.8）：大规模高通量材料发现
- 蛋白质组学层（§18.11）：基因组-药物活性之间的桥接
- 光学纤维层（§18.12）：全反射原理、step/graded/single-mode
- 材料选择层（§18.14）：performance index 与材料选择图
### 1.3 学术贡献

- 诺贝尔奖级突破：polyacetylene 电导率从绝缘体跃升至 10³ S/m（原文）
- 工程贡献：performance index P = (shear stress)^(2/3) / density 是材料选型的定量工具
- 反应器工程：batch / PFR / CSTR 聚合动力学的数学描述
## Step 2 — 章节级拆解（Section-level Decomposition）

### §18.1 CONDUCTIVE POLYMERIC MATERIALS

诺贝尔奖里程碑：
> "The Nobel Prize in Chemistry for 2000 was given to Alan MacDiarmid, Alan Heeger, and Hideki Shirakawa for the discovery and development of electrically conductive polymers."

polyacetylene 掺杂实验：
> "In 1977, using techniques MacDiarmid and Heeger developed for poly(sulfur nitride), Shirakawa, MacDiarmid, and Heeger were able to increase the conductivity of trans-polyacetylene samples, after doping, to a conductivity of about 10³ S/meter, or 1 S/cm."

" They found that oxidation with chlorine, bromine, or iodine vapor made polyacetylene film 10⁹ times more conductive than the nontreated film. This treatment with a halogen was called 'doping' by analogy with the doping employed with semiconductors."

" This chemical doping transforms the polyacetylene from an insulator or semiconductor to a conductor."

共轭双键机制：
> "A critical structural feature for conductive polymers is the presence of conjugated double bonds."

" For polyacetylene, every backbone carbon is connected by a stronger localized σ bond. They are also connected by a network of alternating less localized and weaker π bonds."

" The dopants cause the introduction of sites of increased or deficiency of electrons. When there is a deficiency of electrons, or a hole, created, electrons flow to fill this hole with the newly created hole causing other electrons to flow to fill the new hole, etc., allowing a charge to migrate within and between the polyacetylene chains."

" In general, the Huckel theory predicts that π electrons can be delocalized over an entire chain containing adjacient π bonds with the activation energy for delocalization decreasing as the chain length increases."

### 分子导线 / 纳米导线（约 line 232-242）

" Part of the nano revolution involves the electronics industry and the synthesis of so-called 'nano' or molecular wires for electronic applications."

" Basically, molecular wires contain a series of double or double and triple bonds that have what can be referred to as 'whole-chain' resonance."

" While we call these materials polymeric, in truth they are oligomeric, often intentionally made to be oligomers with specific lengths intended to connect other molecules or molecular devices."

" Thus, we can design molecules with particular lengths, conductivity, and the ability to molecularly connect to other molecules."

### §18.3 SOLID WASTE

固体废物的聚合物主体：
> "Polymers are giant molecules and macromolecules. They include natural organic (proteins, nucleic acids, polysaccharides such as starch and cellulose, wool, hair, skin, teeth, lignin), inorganic (sand, granite, quartz), and synthetic [plastics, elastomers (rubbers), fibers, concrete (cement), glass, paper] polymers. They compose the large bulk by weight and by volume of what is termed solid waste."

美国消费量：
> "In today's marketplace, the United States consumes about 75 billion lb. of synthetic polymers (plastics and synthetic fibers and rubbers) annually, or 300 lb. per person. Paper products are produced at a rate almost double this yearly."

Norrish 反应：[未找到原句] —— 原文 §18.3 讨论聚合物在紫外辐射下的降解（Norish 反应、主链断裂、交联、键重排）—— 但原文 .txt 文件中"Norrish"字样未出现；该主题在其他章节（如 Ch.15 §15.8 降解）讨论。

### §18.8 COMBINATORIAL CHEMISTRY

组合化学定义：
> "Combinatorial chemistry is an approach whereby compounds are synthesized and/or treated en masse."

" Combinatorial chemistry is a result of a number of factors including computerization of testing so that a single or small batch of tests can be carried out rapidly and the development of good separation tools (e.g., chromatographic methods) that allow the ready separation of materials."

" Its aim is to discover materials more quickly and inexpensively by creating and evaluating materials on a large (numberwise) scale."

术语表：
> "combinatorial chemistry: Approach whereby materials are developed and tested in an almost assembly line fashion, allows the ready determination of specific properties for a number of similar but unlike materials."

### §18.11 PROTEOMICS

蛋白质组学定义：
> "One such subdivision has been given the name 'proteomics,' which deals with the interfacing or bridging between genomics or gene information and drug or target molecule activity."

### §18.12 OPTICAL FIBERS

光纤结构：
> "The optical fiber is formed from a combination of polymeric materials. It typically consists of a core, cladding, and coating. The core does the actual transmission of the photons; the cladding constrains the light so it will travel within the core with little signal power loss and little pulse distortion; and the coating helps protect the inner material from damage and external pressures."

" Based on the core-cladding combination, there are three types of optical systems: the step-index, the graded index, and single-mode fibers."

" Most of the 'long-distance' systems use high-purity silica glass as the core material."

" Containment and retention of the signal is made possible because of the use of laser light and its total reflectance as it travels through the fiber. This containment is accomplished by using cladding and coating materials of differing refractive indexes from the core material."

" In the step-index approach, the index of refraction of the cladding is slightly less than that of the core."

### 聚合物反应器（Batch / PFR / CSTR）

Batch（间歇）：
> "In batch reactions, the reactants are added (charged) to the reactor, mixed for a specific time and temperature, and then removed (discharged)."

" Batch reactors are generally simple and can vary from being relatively small (such as gallon size) to large (several hundred gallon size) with the reaction occurring under varying conditions throughout the reaction vessel with time giving products that vary with time and secondarily, location within the vessel. This second condition is referred to as the polymerization occurring under non-steady-state or unsteady-state conditions."

PFR（平推流/管式）：
> "A plug flow or tubular flow reactor is tubular in shape with a high length to diameter, 1/d, ratio."

" In an ideal case (as in most ideal cases such as an ideal gas, this only approached reality), flow is orderly with no axial diffusion and no difference in velocity of any members in the tube. Thus, the time a particular material remains within the tube is the same as that of any other material."

CSTR（连续搅拌釜）：
> "In the continuous stirred-tank reactor (CSTR), instant mixing to achieve a homogeneous reaction mixture is assumed so that the composition throughout the reactor is uniform."

" During the reaction, monomer is fed into the system at the same rate as polymer is withdrawn."

" In a CSTR, unlike the tubular and batch systems, the residence time is variable."

" The residence time distribution influences the mixing effectiveness, which in turn determines the uniformity of the composition and temperature of the reactants in the reactor and ultimately the primary and secondary polymer structure."

### §18.14 MATERIAL SELECTION CHARTS

Performance index：
> "Mass is proportional to [density/(shear stress)^(2/3)] × some safety factors"

" This tells us that the best lightweight material to make our shaft out of a material with a low density/(shear stress)^(2/3) ratio."

" Often, the inverse of this ratio is employed and given the name performance index, P."

" P = (shear stress)^(2/3) / density"

" Taking the log of both sides gives log P = 2/3 log shear stress – log density"

" Such plots of one material property versus another material property are called materials selection charts and are important in eliminating or including materials for specific application."

### 纳米纤维/纳米管（补充，约 §18.1 末尾）

" The search for flexible, noncorrosive inexpensive conductive materials has recently focused on polymeric materials. This search has increased to include, for some applications, nano-sized fibrils and tubes."

## Step 3 — 概念定义（Definitions & Terminology）

|||||
|---|---|---|---|
|1|Conductive Polymer|导电聚合物|"A critical structural feature for conductive polymers is the presence of conjugated double bonds"|
|2|Doping|掺杂|"oxidation with chlorine, bromine, or iodine vapor made polyacetylene film 10⁹ times more conductive... This treatment with a halogen was called 'doping'"|
|3|Conjugated Double Bonds|共轭双键|"the presence of conjugated double bonds"|
|4|Hückel Theory|休克尔理论|"π electrons can be delocalized over an entire chain containing adjacient π bonds with the activation energy for delocalization decreasing as the chain length increases"|
|5|Molecular Wire|分子导线|"contain a series of double or double and triple bonds that have what can be referred to as 'whole-chain' resonance"|
|6|Solid Waste|固体废物|"They compose the large bulk by weight and by volume of what is termed solid waste"|
|7|Combinatorial Chemistry|组合化学|"approach whereby compounds are synthesized and/or treated en masse"|
|8|Proteomics|蛋白质组学|"deals with the interfacing or bridging between genomics or gene information and drug or target molecule activity"|
|9|Optical Fiber (Core/Cladding/Coating)|光纤（芯/包层/涂覆）|"The optical fiber is formed from a combination of polymeric materials. It typically consists of a core, cladding, and coating"|
|10|Step-Index / Graded-Index / Single-Mode|阶跃/渐变/单模|"Based on the core-cladding combination, there are three types of optical systems"|
|11|Total Reflectance|全反射|"containment is made possible because of the use of laser light and its total reflectance"|
|12|Batch Reactor|间歇反应器|"In batch reactions, the reactants are added (charged)... mixed for a specific time and temperature, and then removed (discharged)"|
|13|Plug Flow / Tubular Reactor (PFR)|平推流/管式反应器|"tubular in shape with a high length to diameter, 1/d, ratio"|
|14|Continuous Stirred-Tank Reactor (CSTR)|连续搅拌釜|"instant mixing to achieve a homogeneous reaction mixture is assumed"|
|15|Residence Time Distribution|停留时间分布|"The residence time distribution influences the mixing effectiveness"|
|16|Performance Index (P)|性能指数|"P = (shear stress)^(2/3) / density"|
|17|Material Selection Chart|材料选择图|"plots of one material property versus another material property are called materials selection charts"|

## Step 4 — 关键方程 / 数据

|||
|---|---|
|Polyacetylene 掺杂后电导率|~10³ S/m = 1 S/cm|从绝缘体到导体|
|掺杂前后电导率比|10⁹ 倍|化学掺杂的戏剧性效果|
|美国合成聚合物年消耗|~750 亿磅（人均 ~300 磅）|固体废物体量|
|光纸年产量|几乎两倍于合成聚合物|包装/卫生制品|
|Performance Index P|(shear stress)^(2/3) / density|材料轻量化选型|
|log P|2/3 log shear stress – log density|材料选择图|
|CSTR 特征|residence time variable|聚合物分子量分布|

## Step 5 — 原文摘选（Excerpts, Original English）

导电聚合物诺贝尔奖（原文综合）：
" The Nobel Prize in Chemistry for 2000 was given to Alan MacDiarmid, Alan Heeger, and Hideki Shirakawa for the discovery and development of electrically conductive polymers."

Polyacetylene 掺杂（原文综合）：
" They found that oxidation with chlorine, bromine, or iodine vapor made polyacetylene film 10⁹ times more conductive than the nontreated film. This treatment with a halogen was called 'doping' by analogy with the doping employed with semiconductors."

共轭双键（原文综合）：
" A critical structural feature for conductive polymers is the presence of conjugated double bonds."

Hückel 理论（原文综合）：
" In general, the Huckel theory predicts that π electrons can be delocalized over an entire chain containing adjacient π bonds with the activation energy for delocalization decreasing as the chain length increases."

固体废物（原文综合）：
" Polymers are giant molecules and macromolecules... They compose the large bulk by weight and by volume of what is termed solid waste."

美国消费量（原文综合）：
" In today's marketplace, the United States consumes about 75 billion lb. of synthetic polymers (plastics and synthetic fibers and rubbers) annually, or 300 lb. per person."

组合化学（原文综合）：
" Combinatorial chemistry is an approach whereby compounds are synthesized and/or treated en masse."

蛋白质组学（原文综合）：
" One such subdivision has been given the name 'proteomics,' which deals with the interfacing or bridging between genomics or gene information and drug or target molecule activity."

光纤结构（原文综合）：
" The optical fiber is formed from a combination of polymeric materials. It typically consists of a core, cladding, and coating."

CSTR（原文综合）：
" In the continuous stirred-tank reactor (CSTR), instant mixing to achieve a homogeneous reaction mixture is assumed so that the composition throughout the reactor is uniform."

Performance Index（原文综合）：
" P = (shear stress)^(2/3) / density"

## Step 6 — RIA 实践转化

### 卡片 1：智能卫材的导电聚合物可能性

- Read：原文 "oxidation with chlorine, bromine, or iodine vapor made polyacetylene film 10⁹ times more conductive" + "We can design molecules with particular lengths, conductivity, and the ability to molecularly connect to other molecules"
- Interpret：导电聚合物 + 分子导线技术为"功能性聚合物传感器"奠定基础；Seymour 2003 年出版时 polyacetylene 已获诺贝尔奖，但实际应用仍受限于空气稳定性
- Apply：

- 智能尿布传感器：可用导电聚合物薄膜（如 PEDOT:PSS，虽不在原文中但属于同族共轭体系）检测湿度/皮肤接触
- 卫材抗静电层：原文 Ch.14 §14.9 抗静电剂吸湿薄膜 → 进阶方案是掺杂型导电聚合物涂层（导电率可控）
- 抗菌功能：共轭聚合物的光催化特性可用于"光激活抗菌"卫生用品
### 卡片 2：卫材轻量化——Performance Index 的定量选型

- Read：原文 "P = (shear stress)^(2/3) / density" + "log P = 2/3 log shear stress – log density"
- Interpret：材料选择图通过 P 值定量评估"强度/密度"比；P 值越高，越适合轻量化应用
- Apply：

- 卫材减薄设计：在保持相同湿强度的前提下，通过 Kelly–Tyson（Ch.13）+ Performance Index（Ch.18）双工具，选 aspect ratio 更高的纤维（如 PE 超细纤维）替代传统 PP 纺粘
- 减薄-强化的定量路径：log P 图中，PP（δ ~0.9 g/cm³，剪切强度 ~30 MPa）vs PE（δ ~0.95，剪切 ~25 MPa）——PE 的 log P 稍低；改用高取向 PE 超纤（剪切强度可 > 100 MPa），P 值显著提升
- 湿巾包装：用 Performance Index 评估纸浆 vs PE vs PP 三种材料，选 P 值最优者
### 卡片 3：SAP 生产的反应器选择

- Read：原文 CSTR "instant mixing... composition throughout the reactor is uniform" vs PFR "flow is orderly with no axial diffusion... the time a particular material remains within the tube is the same"
- Interpret：SAP 的工业生产通常在凝胶反应器（batch 半间歇）中进行——原文指出 batch 反应器"反应在非稳态下进行"，这正对应 SAP 凝胶聚合的特性
- Apply：

- SAP 生产：通常采用 batch/semi-batch 搅拌反应器（原文所述 "non-steady-state or unsteady-state conditions"）——因为需要精确控制放热与凝胶化时间
- MWD 控制：CSTR 的 variable residence time 会影响 PDI——若 SAP 需窄 MWD，用 PFR 或 semi-batch 更优
- 放大：从"几加仑"到"几百加仑"的 batch 反应器（原文所述 "can vary from being relatively small (such as gallon size) to large (several hundred gallon size)"）
### 卡片 4：卫材的环境议题与固体废物

- Read：原文 "75 billion lb. of synthetic polymers (plastics and synthetic fibers and rubbers) annually, or 300 lb. per person"
- Interpret：美国人均年消耗合成聚合物 300 磅——一次性卫生制品（纸尿裤、卫生巾、湿巾）是"300 磅"的重要组成
- Apply：

- 卫材的塑料消耗：全球纸尿裤/卫生用品每年消耗数百万吨塑料（PP 纺粘、PE 底膜、SAP）
- 可持续方向：
- 可降解塑料（PLA/PHA）：替代 PP/PE 无纺布
- 纳米纤维层析：Ch.18 讨论的纳米纤维技术可用于"超细纤维可降解无纺布"
- 组合化学（原文 §18.8 "discover materials more quickly and inexpensively"）：快速筛选环保配方
### 卡片 5：组合化学与蛋白质组学——卫材功能创新的未来

- Read：原文组合化学 "creating and evaluating materials on a large (numberwise) scale" + 蛋白质组学 "bridging between genomics... and drug or target molecule activity"
- Interpret：这两种方法学代表"高通量"的新范式——组合化学在材料层面，蛋白质组学在生物界面层面
- Apply：

- 卫材抗菌/护肤添加剂的快速筛选：组合化学方法学可用于从数百种分子中快速筛选低刺激、高效能的抗菌剂
- 皮肤敏感人群研究：蛋白质组学方法学可识别"皮肤接触-蛋白质反应"的靶点，指导低过敏配方设计

## Step 7 — 合成报告

### 7.1 章节地图

Ch.18 Special Topics
├── §18.1 Conductive Polymers
│   ├── 2000 年诺贝尔奖: MacDiarmid/Heeger/Shirakawa
│   ├── Polyacetylene 掺杂: Cl₂/Br₂/I₂ → 10⁹× 电导率提升
│   ├── 电导率: 绝缘体 → 10³ S/m = 1 S/cm
│   ├── 共轭双键: σ 键 + π 键交替
│   ├── Hückel 理论: π 电子离域, 活化能随链长降低
│   └── 分子导线: oligomeric wires with whole-chain resonance
├── 分子导线 / 纳米导线
│   ├── "whole-chain" resonance 的 double/triple bonds
│   └── 设计长度/导电性/分子连接能力
├── §18.3 Solid Waste
│   ├── 聚合物分类: natural organic / inorganic / synthetic
│   ├── 美国: 750 亿磅/年; 人均 300 磅
│   ├── 纸产品: 几乎两倍
│   └── UV 降解机制: Norrish / 主链断裂 / 交联 / 键重排 (Norrish 原文未出现, 见 [未找到原句])
├── 聚合物反应器 (Batch / PFR / CSTR)
│   ├── Batch: non-steady-state
│   ├── PFR: high l/d, no axial diffusion, uniform residence time
│   └── CSTR: instant mixing, uniform composition, variable residence time
├── §18.8 Combinatorial Chemistry
│   └── 大规模合成+测试; computerized testing; chromatographic separation
├── §18.11 Proteomics
│   └── bridging genomics ↔ drug/target molecule activity
├── §18.12 Optical Fibers
│   ├── Core / cladding / coating
│   ├── Step-index / graded-index / single-mode
│   └── Total reflectance; silica core for long-distance
└── §18.14 Material Selection Charts
    ├── Performance Index: P = (shear stress)^(2/3) / density
    ├── log P = 2/3 log shear stress – log density
    └── Material selection charts: 材料属性两两作图

### 7.2 概念索引

||||||
|---|---|---|---|---|
|1|Conductive Polymer|导电聚合物|§18.1|Ch.13 (nanotubes), Ch.18|
|2|Doping|掺杂|§18.1|Ch.18|
|3|Conjugated Double Bonds|共轭双键|§18.1|Ch.18|
|4|Hückel Theory|休克尔理论|§18.1|Ch.18|
|5|Molecular Wire|分子导线|§18.1 补|Ch.18|
|6|Solid Waste|固体废物|§18.3|Ch.18|
|7|Combinatorial Chemistry|组合化学|§18.8|Ch.18|
|8|Proteomics|蛋白质组学|§18.11|Ch.18|
|9|Optical Fiber|光纤|§18.12|Ch.18|
|10|Step-Index / Graded-Index / Single-Mode|阶跃/渐变/单模|§18.12|Ch.18|
|11|Batch Reactor|间歇反应器|§18 (反应器)|Ch.17 (reactive extrusion)|
|12|Plug Flow Reactor (PFR)|平推流反应器|§18|Ch.18|
|13|CSTR|连续搅拌釜|§18|Ch.6 (聚合动力学)|
|14|Performance Index (P)|性能指数|§18.14|Ch.13 (Kelly-Tyson), Ch.18|
|15|Material Selection Chart|材料选择图|§18.14|Ch.18|

### 7.3 原文摘选索引

|||||
|---|---|---|
|~82|"The Nobel Prize in Chemistry for 2000 was given to Alan MacDiarmid, Alan Heeger, and Hideki Shirakawa"|导电聚合物里程碑|
|~85|"conductivity of trans-polyacetylene samples, after doping, to a conductivity of about 10³ S/meter, or 1 S/cm"|电导率数据|
|~87|"oxidation with chlorine, bromine, or iodine vapor made polyacetylene film 10⁹ times more conductive... This treatment with a halogen was called 'doping'"|掺杂机制|
|~91|"This chemical doping transforms the polyacetylene from an insulator or semiconductor to a conductor"|掺杂效果|
|~93|"A critical structural feature for conductive polymers is the presence of conjugated double bonds"|共轭双键|
|~95|"connected by a network of alternating less localized and weaker π bonds"|电子结构|
|~98|"The dopants cause the introduction of sites of increased or deficiency of electrons"|空穴传导|
|~103|"the Huckel theory predicts that π electrons can be delocalized over an entire chain containing adjacient π bonds with the activation energy for delocalization decreasing as the chain length increases"|休克尔理论|
|~232-242|"molecular wires contain a series of double or double and triple bonds that have what can be referred to as 'whole-chain' resonance"|分子导线|
|§18.3|"They compose the large bulk by weight and by volume of what is termed solid waste"|固体废物|
|§18.3|"75 billion lb. of synthetic polymers (plastics and synthetic fibers and rubbers) annually, or 300 lb. per person"|美国消费量|
|§18.8|"Combinatorial chemistry is an approach whereby compounds are synthesized and/or treated en masse"|组合化学|
|§18.11|"proteomics, which deals with the interfacing or bridging between genomics or gene information and drug or target molecule activity"|蛋白质组学|
|§18.12|"The optical fiber is formed from a combination of polymeric materials. It typically consists of a core, cladding, and coating"|光纤结构|
|§18.12|"In the step-index approach, the index of refraction of the cladding is slightly less than that of the core"|阶跃折射率|
|反应器段|"In batch reactions, the reactants are added (charged)... mixed for a specific time and temperature, and then removed (discharged)"|Batch|
|反应器段|"A plug flow or tubular flow reactor is tubular in shape with a high length to diameter, 1/d, ratio"|PFR|
|反应器段|"In the continuous stirred-tank reactor (CSTR), instant mixing to achieve a homogeneous reaction mixture is assumed"|CSTR|
|反应器段|"The residence time distribution influences the mixing effectiveness, which in turn determines the uniformity of the composition and temperature of the reactants"|RTD 效应|
|§18.14|"P = (shear stress)^(2/3) / density"|性能指数|
|§18.14|"log P = 2/3 log shear stress – log density"|log P 方程|
|§18.14|"Such plots of one material property versus another material property are called materials selection charts"|材料选择图|

注：原文 §18.3 讨论聚合物 UV 降解机制，但"Norrish reaction"字样在原文 .txt 中未出现，标注 [未找到原句]。
注：Nanocomposites 主题在 Ch.18 中仅有两处简短提及（"nano-sized fibrils and tubes" 与一篇文献引用），未有专门讨论。

End of Chapter 18 Deep-Dive Report

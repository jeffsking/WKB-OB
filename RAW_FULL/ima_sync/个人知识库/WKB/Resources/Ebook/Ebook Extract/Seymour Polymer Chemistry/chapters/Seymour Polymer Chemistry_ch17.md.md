---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_27eee76c178f9386c89c9127fb5780a0001a693ee6c0644e"
source_file: "Seymour Polymer Chemistry_ch17.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Seymour Polymer Chemistry/chapters/Seymour Polymer Chemistry_ch17.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Seymour Polymer Chemistry_ch17.md.md

# Seymour Polymer Chemistry — Chapter 17 Deep-Dive

## Chapter 17: Polymer Technology

文件名: seymour_ch17.txt
文件长度: 160,245 chars
页码约定: 原文 .txt 文件无正式印张页码；本报告以原文行号（line no.）作为定位引用。

## 执行摘要（Executive Summary）

第17章是全书聚合物加工工艺的百科全书，覆盖纤维（§17.1）、弹性体（§17.2）、薄膜（§17.3）、泡沫（§17.4）、复合材料/层压（§17.5）、模塑（§17.6）、浇铸（§17.7）、挤出（§17.8）、涂料（§17.9）、粘合剂（§17.10）十大加工技术。这是将"聚合物分子"转化为"聚合物产品"的工程手册——每一节都包含工艺原理、关键参数、年产量数据、以及材料-工艺配对关系。

对 SAP/PP 卫材业务，本章具有直接工艺映射：
- 无纺布（spunbond / meltblown）：§17.1 melt spinning 是直接工艺基础
- PE 熔喷+水刺无纺布：§17.1（纺丝）+ §17.3（薄膜/拉伸）
- 湿巾防水底膜：§17.3（calendering/薄膜）+ §17.8（挤出）
- 弹性腰围/搭扣：§17.2（弹性体 compounding & vulcanization）
- PP 硬制品（湿巾盖）：§17.6（injection molding）+ §17.8（extrusion）
- 纸尿裤复合结构：§17.5（laminates）+ §17.9（coatings）+ §17.10（adhesives）

## Step 1 — 宏观解读（Macro Interpretation）

### 1.1 核心论题

- 主论题：聚合物产品的性能不仅取决于分子结构，更取决于加工过程中的取向、冷却、交联与复合——加工即"分子排列的工程化"
- 副论题：（a）纤维强度来自"熔体挤出 → 单轴拉伸 → 链取向"的能量学；（b）弹性体性能来自"填料/硫化度/交联密度"的配方；（c）模塑工艺的选择（injection / compression / rotational / thermoforming）取决于材料类型（thermoplastic vs thermoset）与几何复杂度；（d）加工温度需精确位于 Tg 与 Tm 之间的窗口
### 1.2 论证结构

- 纤维层（§17.1）：melt / dry / wet / gel spinning + 拉伸取向 + 纤维强度（tenacity）
- 弹性体层（§17.2）：SBR/NBR/neoprene/butyl/EPDM + Banbury 混合 + 硫化
- 薄膜层（§17.3）：cast / extrusion / calendering / drawing / permeability
- 泡沫层（§17.4）：unicellular / multicellular + PU foam + EPS
- 复合材料层（§17.5）：filament winding / prepreg / pultrusion / lamination
- 模塑层（§17.6）：injection / blow / rotational / compression / thermoforming
- 其他层（§17.7-17.10）：casting / extrusion / coatings / adhesives
### 1.3 学术贡献

- 工艺-结构映射贡献：gel spinning 通过"超高分子量 + 低浓度 + 高温溶剂 → 高取向"实现超高强度纤维
- 反应纺丝贡献：PU 反应纺丝是"纺丝与反应同时进行"的前沿工艺，直接对应 SAP 的"原位交联"逻辑
## Step 2 — 章节级拆解（Section-level Decomposition）

### §17.1 FIBERS

Melt spinning（熔体纺丝）：
> "Melt spinning was developed in the 1930s. In melt spinning, the polymer is melted or extruded, clarified by filtration, and pumped through a die having one or more small holes. The die is called a spinneret."

Dry spinning（干纺）：
> "In the dry spinning process, the solution is filtered and then forced through a spinneret into a spinning cabinet through which heated air is passed to dry the filament."

Wet spinning（湿纺/再生）：
> "Wet spinning is similar to dry spinning except that fiber formation results from the coagulation of the polymer solution as it is introduced into a nonsolvent bath."

Gel spinning（凝胶纺丝）：
> "Gel spinning is used to produce high strength and modulus fibers. High-molecular-weight (such as 10⁶ Daltons for polyethylene) polymer is dissolved in a high-temperature solvent at low concentration (ca 1%). The hot solution is extruded into a cooling zone..."

纤维细度：
> "One tex is 1 g per 1000 m or 10⁻⁶ kg/m. The tex has replaced denier as a measure of the density of the fiber."

> "One denier is 1 g per 9000 m, so 1 denier = 0.1111 tex."

反应纺丝（PU）：
> "The most important example is the production of selected segmented polyurethane elastomeric fibers. Here, the prepolymer is the soft segment generally a low-molecular-weight polyether or polyester. Reaction with an aromatic diisocyanate converts the end groups, generally hydroxyls, into isocyanate groups. The bath contains a diamine such as 1,2-diaminoethane. The reaction between the amine and isocyanate forms the hard urea linkages."

主要合成纤维产量：
- Polyester：~400 亿磅/年（熔纺）
- Nylon-6/66：> 100 亿磅/年（熔纺）
- Acrylic：> 70 亿磅/年（干纺）

### §17.2 ELASTOMERS

SBR 与弹性体合成：
> "The most widely used elastomer, SBR, is obtained by coagulation of an emulsion of a copolymer of butadiene and styrene. In addition to being produced by the free radical emulsion polymerization technique, elastomers are also produced by cationic copolymerization (butyl rubber) and by anionic polymerization (polybutadiene)."

Mastication（炼胶/塑炼）：
> "Mastication is intended to bring the material to the necessary consistency to accept the compounding ingredients. Mastication results in a lowering of chain size to an average chain length on the order of 10⁴ carbons."

Banbury 混合机：
> "The Banbury has rotors rotating at different speeds creating a 'kneading' action such as that employed in handling bread dough. A shearing action between the rotors and the walls of the mixer is also achieved."

硫化（Vulcanization）：
> "Between 1–5% of sulfur (by weight) is added in typical black rubber mixes giving a vulcanized material with an average of about 500 carbon atoms between crosslinks. Larger amounts of sulfur will give a tougher material eventually giving a somewhat brittle, but quite strong, ebonite as the amount of sulfur is increased to about 40%."

### §17.3 FILMS AND SHEETS

- Cast films：regenerated cellulose via slit die；cellulose acetate from solution
- Extrusion films：flat slit die or air-blowing tubular
- Calendering：counter-rotating rolls for mixing, lamination, coating, embossing
- PVC 板材配方：plasticizer + pigment + filler + lubricant + stabilizer
- Drawing/Orientation：PVC 160-180°C 定向；> 190°C 无法定向
### §17.4 POLYMERIC FOAMS

- ** Unicellular (closed-cell)**：insulation, buoyancy
- Multicellular (open-cell)：upholstery, carpet backing
- Expanded PS：K 值 ~0.24 Btu
- PU foam：polyol + diisocyanate 反应发泡
- 年产量 > 150 万吨，增速 ~10%/年
### §17.5 REINFORCED PLASTICS & LAMINATES

- Filament winding：纤维蘸预聚体缠绕 mandrel 后固化
- Prepreg：预浸料带
- Pultrusion：连续纤维+热固性树脂拉挤成型
- Laminating：层压板（phenolic, epoxy, polyester）
### §17.6 MOLDING

Injection molding（注塑）：
> "Injection molding involves forcing (injecting) a molten polymer into a mold where it cools, becoming solid; the mold separates, allowing the molded material to be released."

> "A patent was issued in 1872 for an injection molding machine for camphor-plasticized cellulose nitrate, celluloid."

Compression molding（压缩模塑）：
> "The most widely employed molding process is compression molding, where the material is placed in the bottom half of an open, heated mold. The second half of the mold is closed and brings heat and pressure against the material, softening the material further and eventually allowing it to crosslink, if it is a thermoset."

Thermoforming（热成型）：
> "Thermoforming involves heating a sheet or thick film just above its Tg or Tm, stretching it against a rigid mold, cooling, and trimming the formed part. Inexpensive aluminum, wood, epoxy, and steel molds are often employed."

材料选择：
- PS/HIPS：包装
- ABS：耐用件
- HDPE：车箱衬里
- PET：可微波托盘
- PC/PMMA：采光顶/展示

### §17.7-17.10 CASTING / EXTRUSION / COATINGS / ADHESIVES

Extrusion（挤出）：
> "Extruders can be described in terms of their length, l, and screw diameter, d, by the ratio l/d."

> "Melt-fed extruders have a l/d ratio of about 8; solid-fed extruders often have l/d's in the range of 20–40. Large extruders can produce 20 tons per h of extruded material."

> "Reactive extrusion is the term used to describe the use of an extruder as a continuous reactor such as polymerization or polymer modification."

Adhesives（粘合剂）：
> "Pressure-sensitive adhesives: These are actually viscous polymer melts at room temperature. The polymers must be applied at temperatures above their Tg to permit rapid flow."

> "Hot-melt adhesives: Thermoplastics often form good adhesives simply by melting, followed by subsequent cooling after the plastic has filled surface voids. Nylons are frequently employed in this manner."

> "Reactive adhesives: These additives are either low molecular weight polymers or monomers that solidify by polymerization and/or crosslinking reactions after application."
## Step 3 — 概念定义（Definitions & Terminology）

|||||
|---|---|---|---|
|1|Melt Spinning|熔体纺丝|"the polymer is melted or extruded, clarified by filtration, and pumped through a die having one or more small holes"|
|2|Dry Spinning|干纺|"forced through a spinneret into a spinning cabinet through which heated air is passed to dry the filament"|
|3|Wet Spinning|湿纺|"fiber formation results from the coagulation of the polymer solution as it is introduced into a nonsolvent bath"|
|4|Gel Spinning|凝胶纺丝|"produce high strength and modulus fibers... High-molecular-weight... polymer is dissolved in a high-temperature solvent at low concentration"|
|5|Tex / Denier|特克斯/旦尼尔|"One tex is 1 g per 1000 m"; "One denier is 1 g per 9000 m"|
|6|Spinneret|喷丝板|"The die is called a spinneret"|
|7|Mastication|塑炼|"bring the material to the necessary consistency to accept the compounding ingredients"|
|8|Vulcanization|硫化|"giving a vulcanized material with an average of about 500 carbon atoms between crosslinks"|
|9|Calendering|压延|material squeezed between counter-rotating parallel rolls|
|10|Injection Molding|注塑|"forcing (injecting) a molten polymer into a mold where it cools, becoming solid"|
|11|Compression Molding|压缩模塑|"material is placed in the bottom half of an open, heated mold. The second half of the mold is closed and brings heat and pressure"|
|12|Thermoforming|热成型|"heating a sheet or thick film just above its Tg or Tm, stretching it against a rigid mold"|
|13|Extrusion (l/d ratio)|挤出（长径比）|"Melt-fed extruders have a l/d ratio of about 8; solid-fed extruders often have l/d's in the range of 20–40"|
|14|Reactive Extrusion|反应挤出|"the use of an extruder as a continuous reactor such as polymerization or polymer modification"|
|15|Pressure-Sensitive Adhesive|压敏胶|"viscous polymer melts at room temperature. The polymers must be applied at temperatures above their Tg"|
|16|Hot-Melt Adhesive|热熔胶|"Thermoplastics often form good adhesives simply by melting, followed by subsequent cooling"|
|17|Reactive Adhesive|反应型粘合剂|"low molecular weight polymers or monomers that solidify by polymerization and/or crosslinking reactions after application"|
|18|Reaction Spinning|反应纺丝|PU 预聚体纺丝过程中与胺反应形成硬段|

## Step 4 — 关键方程 / 数据

|||
|---|---|
|1 tex|1 g / 1000 m|纤维细度|
|1 denier|1 g / 9000 m = 0.1111 tex|纤维细度（旧制）|
|Polyester 年产量|~400 亿磅|涤纶纤维|
|Nylon-6/66|> 100 亿磅|锦纶纤维|
|Acrylic|> 70 亿磅|腈纶纤维|
|Vulcanization sulfur|1-5%（常规）/ ~40%（ebonite）|交联密度控制|
|硫化交联间隔|~500 carbons between crosslinks|硫化程度|
|Mastication 后链长|~10⁴ carbons|塑炼目标|
|l/d ratio (melt-fed)|~8|挤出机参数|
|l/d ratio (solid-fed)|20-40|挤出机参数|
|大型挤出机产能|20 tons/h|挤出规模|
|PU foam 年产量|> 150 万吨；增速 ~10%/年|泡沫工业|

## Step 5 — 原文摘选（Excerpts, Original English）

Melt spinning（原文综合）：
"Melt spinning was developed in the 1930s. In melt spinning, the polymer is melted or extruded, clarified by filtration, and pumped through a die having one or more small holes. The die is called a spinneret."

Dry vs Wet spinning（原文综合）：
"In the dry spinning process, the solution is filtered and then forced through a spinneret into a spinning cabinet through which heated air is passed to dry the filament."

"Wet spinning is similar to dry spinning except that fiber formation results from the coagulation of the polymer solution as it is introduced into a nonsolvent bath."

Gel spinning（原文综合）：
"Gel spinning is used to produce high strength and modulus fibers. High-molecular-weight (such as 10⁶ Daltons for polyethylene) polymer is dissolved in a high-temperature solvent at low concentration (ca 1%)."

Tex/Denier（原文综合）：
"One tex is 1 g per 1000 m or 10⁻⁶ kg/m. The tex has replaced denier as a measure of the density of the fiber."

SBR 与弹性体（原文综合）：
"The most widely used elastomer, SBR, is obtained by coagulation of an emulsion of a copolymer of butadiene and styrene."

Mastication（原文综合）：
"Mastication is intended to bring the material to the necessary consistency to accept the compounding ingredients. Mastication results in a lowering of chain size to an average chain length on the order of 10⁴ carbons."

Banbury 混合（原文综合）：
"The Banbury has rotors rotating at different speeds creating a 'kneading' action such as that employed in handling bread dough."

Vulcanization（原文综合）：
"Between 1–5% of sulfur (by weight) is added in typical black rubber mixes giving a vulcanized material with an average of about 500 carbon atoms between crosslinks."

Injection molding（原文综合）：
"Injection molding involves forcing (injecting) a molten polymer into a mold where it cools, becoming solid; the mold separates, allowing the molded material to be released."

Thermoforming（原文综合）：
"Thermoforming involves heating a sheet or thick film just above its Tg or Tm, stretching it against a rigid mold, cooling, and trimming the formed part."

Extrusion l/d（原文综合）：
"Melt-fed extruders have a l/d ratio of about 8; solid-fed extruders often have l/d's in the range of 20–40."

Pressure-sensitive adhesive（原文综合）：
"Pressure-sensitive adhesives: These are actually viscous polymer melts at room temperature. The polymers must be applied at temperatures above their Tg to permit rapid flow."

## Step 6 — RIA 实践转化

### 卡片 1：PP/PE 熔体纺丝——卫材无纺布的核心工艺

- Read：原文 "In melt spinning, the polymer is melted or extruded, clarified by filtration, and pumped through a die having one or more small holes. The die is called a spinneret." + "gel spinning is used to produce high strength and modulus fibers"
- Interpret：卫材无纺布（spunbond + meltblown）是 melt spinning 的工程化应用；PP 熔体纺丝后经高速气流拉伸（meltblown）得到亚微米级超细纤维——这是熔纺原理在"极致细度"方向的延伸
- Apply：
  - Spunbond 无纺布：PP 熔体 → 喷丝板 → 单轴拉伸 → 卷曲 → 铺网 → 热轧/水刺
  - Meltblown 熔喷布：PP 熔体 → 特殊喷丝板（孔径更小）+ 高速热气流牵伸 → 亚微米纤维（0.5-5 μm）→ 静电驻极处理（增强过滤效率）
  - 工艺窗口：PP 熔融温度 220-260°C（Tm 165°C），纺丝温度需高于 Tm 以保证低熔体黏度（Ch.5 流变理论）
### 卡片 2：弹性腰围的硫化/热塑性弹性体设计

- Read：原文 "Between 1-5% of sulfur (by weight) is added... average of about 500 carbon atoms between crosslinks"
- Interpret：传统硫化橡胶的交联密度通过硫磺用量控制——500 碳/交联点；卫材腰围更常用 TPE/TPU/热塑性氨纶（不需要硫化）
- Apply：
  - 氨纶弹性腰围：§17.1 反应纺丝描述 PU 硬段（脲键）+ 软段（聚醚/聚酯）——软段提供弹性，硬段提供物理交联点（氢键聚集区）
  - SBR/NBR 腰围垫：需炭黑增强（Ch.13）+ 硫磺硫化 + 主副抗氧剂（Ch.14）
  - 硫化度控制：交联点过多（> 5% S）→ ebonite（硬而脆）；过少（< 1%）→ 弹性差
### 卡片 3：卫材注塑硬制品（湿巾盖/婴儿用品）

- Read：原文 "Injection molding involves forcing (injecting) a molten polymer into a mold where it cools, becoming solid"
- Interpret：湿巾翻盖、婴儿用品外壳等多采用注塑成型；材料选择由机械性能（刚性/韧性/耐化学）决定
- Apply：
  - PP（HIPS/ABS/HDPE/PET/PC/PMMA/PVC）——根据 Table 17.9 的 tensile/flexural/heat deflection/dielectric 数据选择
  - 湿巾盖：PP（成本低）或 ABS（表面质量+韧性）
  - 婴儿安全剪刀/卡扣：ABS（耐冲击）
  - 高温消毒部件：PC/PP（heat deflection point 高）
### 卡片 4：纸尿裤的复合结构——Laminates + Coatings + Adhesives

- Read：原文 17.5 laminates（"stacking impregnated sheets... between polished metal plates under high pressure and heat"）+ 17.9 coatings + 17.10 adhesives
- Interpret：纸尿裤是多层复合结构（表层无纺布 + SAP 芯层 + 底膜 + 热熔胶粘合 + 透气底膜），涉及三种加工工艺
- Apply：
  - Laminating（层压）：无纺布+PE 透气膜层压
  - Coating（涂布）：PE 涂布无纺布（防水底膜）
  - Adhesive（粘合）：热熔胶（§17.10 hot-melt，"Thermoplastics often form good adhesives simply by melting"）用于侧边/腰围粘合；EVA 热熔胶年用量 > 2 亿磅
### 卡片 5：挤出工艺——卫材 PE 膜与 PP 异型材

- Read：原文 "Melt-fed extruders have a l/d ratio of about 8; solid-fed extruders often have l/d's in the range of 20–40" + "Reactive extrusion is the term used to describe the use of an extruder as a continuous reactor"
- Interpret：挤出机 l/d 比值决定熔体均化程度；反应挤出允许"边挤出边反应"（如 PP 接枝 MAH 改性）
- Apply：
  - PE 防水底膜：单螺杆挤出（solid-fed，l/d = 20-30）→ T-die → 吹膜或平挤
  - PP 异型材（湿巾盖边框）：l/d = 20-30 的 solid-fed 挤出
  - 反应挤出改性：PP-g-MAH 是"反应挤出"典型——用马来酸酐在挤出过程中接枝到 PP 上，改善 PP 与极性材料（如纤维、矿物填料）的界面相容性——直接呼应 Ch.13 的"interfacial forces enhanced by polar functional groups"
## Step 7 — 合成报告

### 7.1 章节地图

Ch.17 Polymer Technology
├── §17.1 Fibers
│   ├── FTC/ISO 纤维命名法规；tex (1g/1000m)；denier (1g/9000m)
│   ├── Melt spinning (1930s; PP/PE/PET/PA)
│   ├── Dry spinning (溶液+热风)
│   ├── Wet spinning (溶液+凝固浴；viscose/aramid)
│   ├── Gel spinning (超高分子量+低浓度→高强高模)
│   ├── 非纺丝: 静电纺丝(~5000V), 薄膜分裂, 界面法, 切削(PTFE)
│   ├── 再生纤维素 (viscose rayon)
│   └── 主纤维: PET(400B lb), PA-6/66(>100B lb), acrylic(>70B lb)
├── §17.2 Elastomers
│   ├── SBR (butadiene+styrene, 乳液聚合), NBR, neoprene, butyl (cationic), EPDM
│   ├── Polymer-polymer immiscible: HIPS (SBR domains + PS)
│   ├── Mastication (Banbury; 链长 ~10⁵→10⁴)
│   ├── Compounding: carbon black, accelerators, age resistors, sulfur
│   └── Vulcanization (1-5% S; ~500C/交联点; ebonite ~40% S)
├── §17.3 Films and Sheets
│   ├── Cast films, extrusion films, calendering
│   ├── PVC 配方: plasticizer + pigment + filler + lubricant + stabilizer
│   ├── Drawing (160-180°C for PVC; >190°C no orientation)
│   └── Gas permeability (Table 17.8); 折射率/隐藏力
├── §17.4 Polymeric Foams
│   ├── Unicellular (closed) / Multicellular (open)
│   ├── EPS (Styrofoam, K ~0.24 Btu)
│   ├── PU foam (polyol + diisocyanate)
│   └── >1.5M tons/yr; ~10%/yr growth
├── §17.5 Reinforced Plastics & Laminates
│   ├── Filament winding, prepreg, pultrusion, lamination
├── §17.6 Molding
│   ├── Injection (1872 专利; celluloid)
│   ├── Blow molding
│   ├── Rotational molding
│   ├── Compression molding (thermosets)
│   └── Thermoforming (Tg<T<Tm; PS/HIPS/ABS/HDPE/PET/PC/PMMA/PVC)
├── §17.7 Casting (wheel/belt, precipitation)
├── §17.8 Extrusion
│   ├── l/d ratio: melt-fed ~8; solid-fed 20-40
│   ├── Die types: circular/flat/profile
│   └── Reactive extrusion (PP-g-MAH)
├── §17.9 Coatings
│   ├── Types: oil paint, varnish, lacquer, enamel, latex, plastisol
│   ├── Drying: chemical (alkyds, epoxies, PU) vs evaporation
│   ├── Processes: roll, blade, curtain coating
│   └── Hiding power: 折射率差 (TiO₂ 2.8 vs CaCO₃ 1.6)
└── §17.10 Adhesives
    ├── Pressure-sensitive (Tg<ambient)
    ├── Hot-melt (Nylon, EVA >200M lb/yr)
    ├── Reactive (cyanoacrylate, phenolics, epoxies, PU)
    ├── Thermoset (phenolic/urea/UP/PU/epoxy)
    ├── Thermoplastic (PA, EVA, MMA copolymers)
    ├── Contact (SBR, neoprene/terpene)
    └── Anaerobic (dimethacrylate)

### 7.2 概念索引

||||||
|---|---|---|---|---|
|1|Melt Spinning|熔体纺丝|§17.1|Ch.13 (fiber aspect), Ch.17|
|2|Dry Spinning|干纺|§17.1|Ch.17|
|3|Wet Spinning|湿纺|§17.1|Ch.17|
|4|Gel Spinning|凝胶纺丝|§17.1|Ch.17|
|5|Tex / Denier|特克斯/旦尼尔|§17.1|Ch.17|
|6|Reaction Spinning|反应纺丝|§17.1|Ch.6 (step-reaction)|
|7|Mastication|塑炼|§17.2|Ch.17|
|8|Vulcanization|硫化|§17.2|Ch.1, Ch.17|
|9|Calendering|压延|§17.3|Ch.17|
|10|Injection Molding|注塑|§17.6|Ch.17|
|11|Compression Molding|压缩模塑|§17.6|Ch.17|
|12|Thermoforming|热成型|§17.6|Ch.17|
|13|Reactive Extrusion|反应挤出|§17.8|Ch.15 (polymer reaction)|
|14|Pressure-Sensitive Adhesive|压敏胶|§17.10|Ch.17|
|15|Hot-Melt Adhesive|热熔胶|§17.10|Ch.14 (EVA)|
|16|Reactive Adhesive|反应型粘合剂|§17.10|Ch.6, Ch.17|

### 7.3 原文摘选索引

|||
|---|---|
|§17.1|"In melt spinning, the polymer is melted or extruded, clarified by filtration, and pumped through a die having one or more small holes"|熔纺定义|
|§17.1|"In the dry spinning process, the solution is filtered and then forced through a spinneret into a spinning cabinet through which heated air is passed"|干纺|
|§17.1|"Wet spinning is similar to dry spinning except that fiber formation results from the coagulation of the polymer solution as it is introduced into a nonsolvent bath"|湿纺|
|§17.1|"Gel spinning is used to produce high strength and modulus fibers. High-molecular-weight (such as 10⁶ Daltons for polyethylene) polymer is dissolved in a high-temperature solvent at low concentration (ca 1%)"|凝胶纺丝|
|§17.1|"One tex is 1 g per 1000 m or 10⁻⁶ kg/m. The tex has replaced denier as a measure of the density of the fiber"|纤维细度|
|§17.1|"Reaction between the amine and isocyanate forms the hard urea linkages"|反应纺丝 (PU)|
|§17.2|"The most widely used elastomer, SBR, is obtained by coagulation of an emulsion of a copolymer of butadiene and styrene"|SBR|
|§17.2|"Mastication results in a lowering of chain size to an average chain length on the order of 10⁴ carbons"|塑炼|
|§17.2|"The Banbury has rotors rotating at different speeds creating a 'kneading' action such as that employed in handling bread dough"|Banbury|
|§17.2|"Between 1–5% of sulfur (by weight) is added in typical black rubber mixes giving a vulcanized material with an average of about 500 carbon atoms between crosslinks"|硫化|
|§17.3|PVC 160-180°C for orientation, >190°C no orientation|拉伸定向|
|§17.6|"Injection molding involves forcing (injecting) a molten polymer into a mold where it cools, becoming solid"|注塑|
|§17.6|"Thermoforming involves heating a sheet or thick film just above its Tg or Tm, stretching it against a rigid mold"|热成型|
|§17.8|"Melt-fed extruders have a l/d ratio of about 8; solid-fed extruders often have l/d's in the range of 20–40"|l/d 比值|
|§17.8|"Reactive extrusion is the term used to describe the use of an extruder as a continuous reactor"|反应挤出|
|§17.10|"Pressure-sensitive adhesives: These are actually viscous polymer melts at room temperature"|压敏胶|
|§17.10|"Hot-melt adhesives: Thermoplastics often form good adhesives simply by melting, followed by subsequent cooling"|热熔胶|

End of Chapter 17 Deep-Dive Report

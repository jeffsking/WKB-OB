---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_1bf3deafbfaf4ff092878e72f653248e001a693ee6c0644e"
source_file: "Ebewole Polymer Science Technology_ch10.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch10.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Ebewole Polymer Science Technology_ch10.md.md

# 第 10 章 · Polymer Reaction Engineering（聚合反应工程）

源文件：/sandbox/workspace/deepread/chapters/ebewole_ch10.txt（98,921 chars, pp. 249–280）
语言规则：框架中文 · 概念定义与原文引文保留英文 · 术语首次出现「英文 + 中文释义」

## 一、执行摘要（Executive Summary）

本章从聚合机理（Ch.1–8）跃迁到工程化生产：反应器选型、聚合工艺、传热传质、动力学控制。核心论点："the performance of a product from a polymerization process is inadequate, it is virtually impossible to upgrade its quality by subsequent processing"（p. 250）——聚合产品质量一旦偏离，无法像小分子那样靠蒸馏、结晶返工。全章围绕两大分类：均相/非均相聚合工艺（bulk / solution / suspension / emulsion / precipitation / interfacial）与三大反应器类型（batch / plug flow / CSTR）。工业重点包括乳液聚合的 Smith–Ewart 动力学、悬浮聚合的"粘性相"问题、以及不同反应器对分子量分布（MWD）的影响。

## 二、章节概览（Chapter Overview）

||||
|---|---|---|
|I|INTRODUCTION|249|
|II|POLYMERIZATION PROCESSES|250|
|II.A|HOMOGENEOUS SYSTEMS|250|
|II.A.1|Bulk (Mass) Polymerization|250|
|II.A.2|Solution Polymerization|253|
|II.B|HETEROGENEOUS POLYMERIZATION|253|
|II.B.1|Suspension Polymerization|253|
|II.B.2|Emulsion Polymerization|259|
|II.B.3|Precipitation Polymerization|267|
|II.B.4|Interfacial and Solution Polycondensations|269|
|III|POLYMERIZATION REACTORS|271|
|III.A|Batch Reactors|272|
|III.B|Tubular or Plug Flow Reactor|274|
|III.C|Continuous Stirred Tank Reactor (CSTR)|276|
|IV|PROBLEMS|279|

关键公式

||||
|---|---|---|
|(10.1)|R_p = ½ k_p[M]N|乳液聚合速率|
|(10.2)|r_p = k_p[M·]|单颗粒内聚合速率|
|(10.3)|r_c = r_i/N|初级自由基捕获速率|
|(10.4)|X_n = k_p[M]N / r_i|乳液聚合平均聚合度|
|(10.5)|N = k (r_i/μ_s²)^(1/3) (a_s[E])^(2/3)|乳液粒子数（Smith–Ewart）|
|(10.6)|Rate_in = Rate_out + Rate_reaction + Rate_accumulation|物料衡算|
|(10.10)|R_p = k[M], k = k_p(f k_d[I]/k_t)^(1/2)|自由基聚合速率（对单体一阶）|
|(10.12)–(10.14)|ln([M]/[M]₀) = −kt ; %Conv = 100(1 − e^(−kt))|间歇反应器积分|
|(10.16)|R(t) = (1/τ)e^(−t/τ)|CSTR 停留时间分布|

关键表格：Table 10.1（聚合热）、10.2（溶液聚合）、10.3（悬浮聚合组成）、10.4（乳液聚合各阶段）、10.5（界面/溶液缩聚）、10.6（各聚合类型特征）、10.7（工艺-反应器匹配）、10.8（产物示例）。
关键图：Fig. 10.1（苯乙烯连续本体聚合塔）、10.4（乳液聚合工厂流程）、10.5–10.6（乳液聚合阶段）、10.7（50°C 异戊二烯乳液聚合）、10.8（理想反应器 RTD）。

## 三、原文摘选与批注（English Excerpts with Citations）

### 3.1 聚合工程四要素（Introduction）

"Generally, polymers of industrial interest have high molecular weights, usually in the range of 10⁴ to 10⁷."（p. 249）

"In solution polymerization of styrene, the viscosity can increase by over six orders of magnitude as the degree of conversion increases from zero to 60%."（p. 249）

"The formation of a large polymer molecule from small monomer results in a decrease in entropy. It follows therefore from elementary thermodynamic considerations that the driving force in the conversion process is the negative enthalpy gradient."（p. 250）

"Consequently, heat removal is imperative in polymerization reactions — a problem that is accentuated by the high medium viscosity that leads to low heat transfer coefficients in stirred reactors."（p. 250）

"the steady-state concentration of chain carriers in chain and ionic polymerization is usually low. These polymerization reactions are therefore highly sensitive to impurities."（p. 250）

"if the performance of a product from a polymerization process is inadequate, it is virtually impossible to upgrade its quality by subsequent processing."（p. 250）

### 3.2 分类与均相体系

"Polymerization processes may be conveniently classified as homogeneous or heterogeneous."（p. 250）

"In homogeneous polymerization … all the reactants, including monomers, initiators, and solvents, are mutually soluble and compatible with the resulting polymer."（p. 250）

"Bulk polymerization is ideally suited for making pure polymeric products, as in the manufacture of optical grade poly(methyl methacrylate) or impact-resistant polystyrene, because of minimal contamination of the product."（p. 252）

"The solvent acts as an inert diluent, increasing overall heat capacity without contributing to heat generation."（p. 253）

### 3.3 悬浮聚合

"Suspension polymerization generally involves the dispersion of the monomer, mainly as a liquid in small droplets, into an agitated stabilizing medium usually consisting of water containing small amounts of suspension and dispersion agents."（p. 253）

"Kinetically, therefore, each of the suspended particles has the characteristics of a miniature bulk reactor."（p. 253）

"The 'sticky phase' problem in the polymerization of a hydrophobic monomer such as styrene is the major obstacle to obtaining uniform particle size distribution."（p. 254）

"Particles become sticky at about 10 to 20% conversion and remain so until about 75 to 80% conversion."（p. 254）

"Suspension polymerization is the most widely used technique for the production of thermoplastics."（p. 257）

### 3.4 乳液聚合

"Emulsion polymerization takes place in aqueous media in the presence of water-soluble initiators and surfactants (emulsifiers)."（p. 259）

"The polymerization of water-insoluble monomers that is carried out in an aqueous phase can proceed through emulsion or suspension polymerization."（p. 259）

"Each polymer particle is a locus of polymerization."（p. 260）

"The viscosity of the reaction mass is relatively much less than that of a comparable true solution of polymers in the same molecular weight range. This … results in excellent heat transfer and creates a physical state that is much easier to control."（p. 266）

### 3.5 沉淀/界面缩聚

"Precipitation polymerization is practiced when the monomer is soluble in the medium but the polymer is not."（p. 267）

"Most industrial transition-metal catalysts are insoluble, and consequently polymerization occurs in a multiphase system and may be controlled by mass transfer."（p. 267）

"Interfacial polycondensation is a rapid and low-temperature polymerization."（p. 269）

### 3.6 反应器类型

"The batch reactor is the simplest and least expensive of the three types of reactors."（p. 272）

"In a batch reactor, all variables, for example, temperature, pressure, and concentration, vary with time."（p. 272）

"The tubular reactor is a long narrow tube … and may have a length-to-diameter ratio ranging from a few hundred to several thousand."（p. 274）

"A plug flow reactor is best suited for polymerization reactions in which heat generation and heat transfer are important."（p. 275）

"The CSTR has the same characteristics as the batch reactor except that it operates in the steady state."（p. 276）

"CSTR's yield a narrower MWD than either batch or plug flow reactors for chain-reaction polymerization."（p. 277）

"For step-growth polymerization in batch and tubular reactors, narrow MWD with increasing X_n is generated with increasing conversion."（p. 279）

## 四、概念定义表（Concept Definitions）

||||||
|---|---|---|---|---|
|C1|Homogeneous polymerization|均相聚合|"all the reactants, including monomers, initiators, and solvents, are mutually soluble and compatible with the resulting polymer"|p.250|
|C2|Heterogeneous polymerization|非均相聚合|"the catalyst, the monomer, and the polymer product are mutually insoluble"|p.250|
|C3|Bulk (mass) polymerization|本体聚合|"the reaction mixture consists essentially of the monomer and … a soluble initiator and possibly modifiers"|p.250|
|C4|Solution polymerization|溶液聚合|"the monomer, initiator, and resulting polymer are all soluble in the solvent"|p.253|
|C5|Suspension polymerization|悬浮聚合|"dispersion of the monomer, mainly as a liquid in small droplets, into an agitated stabilizing medium usually consisting of water"|p.253|
|C6|Sticky phase problem|粘性相问题|"Particles become sticky at about 10 to 20% conversion and remain so until about 75 to 80% conversion"|p.254|
|C7|Emulsion polymerization|乳液聚合|"takes place in aqueous media in the presence of water-soluble initiators and surfactants"|p.259|
|C8|Micelle|胶束|"surfactant molecules form micelles when the emulsifier concentration exceeds the critical micelle concentration (CMC)"|p.259|
|C9|Smith–Ewart kinetics|乳液聚合动力学|"each particle contains zero or one radical at any time … rate proportional to [M] and N"|p.263|
|C10|Precipitation polymerization|沉淀聚合|"practiced when the monomer is soluble in the medium but the polymer is not"|p.267|
|C11|Interfacial polycondensation|界面缩聚|"a rapid and low-temperature polymerization"（两不相溶液体界面处反应）|p.269|
|C12|Batch reactor|间歇反应器|"all variables, for example, temperature, pressure, and concentration, vary with time"|p.272|
|C13|Plug flow reactor (PFR)|平推流反应器|"a long narrow tube … length-to-diameter ratio ranging from a few hundred to several thousand"|p.274|
|C14|CSTR|连续搅拌釜式反应器|"operates in the steady state … back-mixed"|p.276|
|C15|Residence time distribution|停留时间分布|CSTR: R(t) = (1/τ)e^(−t/τ)|p.276|

## 五、原文关键引句速查（Key Quotations Index）

|||||
|---|---|---|---|
|产品质量不可返工|"virtually impossible to upgrade its quality by subsequent processing"|250|聚合工程核心约束|
|热移除|"heat removal is imperative … low heat transfer coefficients in stirred reactors"|250|反应器设计首要问题|
|Bulk 优势|"ideally suited for making pure polymeric products … minimal contamination"|252|PMMA/PS 实例|
|Solution 中溶剂作用|"acts as an inert diluent, increasing overall heat capacity"|253|溶剂型 PVAc/PVC|
|悬浮"微小本体"|"miniature bulk reactor"|253|悬浮聚合本质|
|粘性相|"sticky at about 10 to 20% conversion"|254|悬浮颗粒尺寸控制|
|乳液优势|"excellent heat transfer and creates a physical state that is much easier to control"|266|乳液 vs. 溶液|
|Interfacial|"rapid and low-temperature polymerization"|269|PC/PA66/芳纶|
|Batch|"all variables … vary with time"|272|间歇特点|
|PFR|"best suited for polymerization reactions in which heat generation and heat transfer are important"|275|PFR 应用|
|CSTR MWD|"CSTR's yield a narrower MWD than either batch or plug flow reactors for chain-reaction polymerization"|277|MWD 控制要点|

## 六、概念聚类（Concept Clusters）

### 聚类 A · 均相工艺

C1（均相）→ C3（Bulk）/ C4（Solution）

### 聚类 B · 非均相工艺

C2（非均相）→ C5（悬浮）+ C6（粘性相）→ C7（乳液）+ C8（胶束）+ C9（Smith–Ewart）→ C10（沉淀）→ C11（界面）

### 聚类 C · 反应器

C12（Batch）↔ C13（PFR）↔ C14（CSTR）→ C15（RTD）
- 核心判据：CSTR 对链式聚合给出最窄 MWD；Batch/PFR 对逐步聚合给出最窄 MWD

## 七、业务价值判断（Business Relevance — 卫材非织造布）

直接相关性
- Suspension polymerization：是卫材用 PP（等规）、PE、PVC 粒料的主流生产工艺。"Sticky phase"控制直接决定颗粒粒径分布，进而影响纺丝熔体均匀性。
- Interfacial polycondensation：用于生产芳纶（Nomex）、PC——芳纶在高端防护服、过滤材料中的应用。
- Emulsion polymerization：用于丙烯酸乳液粘合剂（水刺工艺粘合胶、湿法非织造布粘合）、PVDC（阻隔涂层）。
- Reactor 选型：卫材用 PP（MWD 窄以改善纺丝稳定性）——按原书结论，链式聚合在 CSTR 中获得更窄 MWD。

间接相关性
- 本章未覆盖连续纺粘/熔喷的螺杆反应-挤出——见第 11 章与工程实践文献。
- "Product quality cannot be upgraded by subsequent processing"对卫材品控有直接警示意义：纺丝原料的分子量分布偏差无法靠下游弥补。

报告结束。所有英文引句均取自 ebewole_ch10.txt 原文。


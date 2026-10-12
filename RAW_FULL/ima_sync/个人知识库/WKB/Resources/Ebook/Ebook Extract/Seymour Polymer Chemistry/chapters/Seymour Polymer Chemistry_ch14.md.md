---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_b6dec02e8981ef151d44589d76ee0e5e001a693ee6c0644e"
source_file: "Seymour Polymer Chemistry_ch14.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Seymour Polymer Chemistry/chapters/Seymour Polymer Chemistry_ch14.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Seymour Polymer Chemistry — Chapter 14 Deep-Dive

## Chapter 14: Plasticizers and Additives

文件名: seymour_ch14.txt
文件长度: 44,026 chars
页码约定: 原文 .txt 文件无正式印张页码；本报告以原文行号（line no.）作为定位引用。

## 执行摘要（Executive Summary）

第14章是全书卫材配方化学的核心手册，系统梳理 14 类聚合物添加剂（additives）——从塑料化、稳定化到阻燃、抗菌、润滑、发泡、相容、增韧、加工助剂——构成聚合物由原料到成品的"配方学"全谱系。本章对卫材业务具有直接映射价值：PP 无纺布的抗静电剂（antistat）与润滑剂（lubricant）决定生产良率；PE 熔喷无纺布与湿巾的抗氧化剂（antioxidant）与热稳定剂（heat stabilizer）决定货架寿命；PVC 涂层尿布的增塑剂（plasticizer，如 DOP 毒性迁移）与抗静电剂直接决定产品安全性与用户体验；抗菌剂（biocide）与抗静电剂在一次性卫生制品中的使用受限于生物相容性法规。Seymour 以"配方即配方学"的工程视角把每类添加剂的机理、分子结构、应用剂量/年用量、毒性/法规问题一次讲透。

## Step 1 — 宏观解读（Macro Interpretation）

### 1.1 核心论题

- 主论题：聚合物的工业可用性能由其添加剂配方决定——添加剂是"分子层级的配方调料"，每一类对应一项具体的加工或使用问题
- 副论题：（a）增塑剂通过降低 Tg 和熔体黏度使聚合物可加工（internal vs external）；（b）稳定剂（anti-oxidant, heat, UV）阻断自由基链式降解；（c）阻燃剂通过自由基终止、成炭、稀释三种机制破坏"燃料-氧气-高温"三角；（d）相容剂（compatibilizer）通过降低界面张力使不相容聚合物共混；（e）每类添加剂都存在毒性/迁移/法规权衡（DOP → 寡聚聚酯增塑剂；PCB → 禁用）

### 1.2 论证结构

- 增塑剂层（§14.1）：内部/外部塑料化 → 邻苯二甲酸酯（DOP）谱系 → 溶度参数匹配 → 毒性与迁移
- 抗氧化剂层（§14.2）：自由基降解机理 → 主抗氧剂（H 供体）/ 副抗氧剂（分解）/ 协同
- 热稳定剂层（§14.3）：PVC 脱 HCl 机理（脱卤化氢）→ 金属盐/HCl 清除剂
- UV 稳定剂层（§14.4）：能量转移剂 / 自由基清除剂 / 屏蔽剂
- 阻燃剂层（§14.5）：燃料-氧气-高温三角 → ATH 稀释 / 成炭 / 自由基终止 / 协同（Sb₂O₃ + Br）
- 应用添加剂层（§14.6–14.14）：抗菌、润滑、固化、抗静电、发泡、相容、增韧、加工助剂

### 1.3 学术贡献

- 配方学贡献：首次按"问题—添加剂—机理—剂量"四元组系统呈现聚合物配方学
- 安全性贡献：DOP → 寡聚聚酯增塑剂的替代案例是"安全性驱动材料换代"的经典范例
- 毒理学贡献：原文指出 "average person takes in about 2 g a year of external plasticizers"，定量揭示添加剂的人体暴露

## Step 2 — 章节级拆解（Section-level Decomposition）

### §14.1 PLASTICIZERS

ASTM 定义（约 line 63-65）：
> "According to the ASTM D-883 definition, a plasticizer is a material incorporated in a plastic to increase its workability and flexibility or distensibility. The addition of a plasticizer may lower the melt viscosity, elastic modulus, and glass transition temperature (Tg) of a plastic."

内部增塑（约 line 45-49）：
> "Internal plastization can be produced through copolymerization giving a more flexible polymer backbone or by grafting another polymer onto a given polymer backbone. Thus, poly(vinylchloride-co-vinyl acetate) is internally plasticized because of the increased flexibility brought about by the change in structure of the polymer chain."

"The presence of bulky groups on the polymer chain increases segmental motion and placement of such groups through grafting acts as an internal plasticizer."

外部增塑（约 line 50-51）：
> "External plasticization is achieved through incorporation of a plasticizing agent into a polymer through mixing and/or heating."

DOP 历史（约 line 74-76, 94-95）：
> "Waldo Semon patented the use of tricresyl phosphate as a plasticizer for poly(vinyl chloride) (PVC) in 1933. This was later replaced by the less toxic di-2-ethylhexyl phthalate (DOP), which is now the most widely used plasticizer."

"The most used phthalate ester is di-2-ethylhexyl phthalate, DOP, made from the reaction of 2-ethyl hexanol with phthalic anhydide."

溶度参数匹配（约 line 105-108）：
> "A good approach to measure likelihood of compatibility is solubility parameters (Sec. 3.2). Plasticizers with solubility parameters and type of bonding similar to those of the polymer are more apt to be compatible than when the solubility parameters are different. The solubility parameter for PVC (9.66) is near that of good plasticizers for PVC such as DOP (8.85)."

毒性/迁移问题（约 line 114-119）：
> "The development of plasticizers has been plagued with toxicity problems. Thus, the use of highly toxic polychlorinated biphenyls (PCBs) has been discontinued. Phthalic acid esters, such as DOP, may be extracted from blood stored in plasticized PVC blood bags and tubing. These aromatic esters are also distilled from PVC upholstery in closed automobiles in hot weather. These problems have been solved by using oligomeric polyesters as nonmigrating plasticizers, instead of DOP."

人体暴露数据（约 line 128-130）：
> "Experimental investigations and assessments show that the average person takes in about 2 g a year of external plasticizers. Most of this is from traces of DOA migrating from food packaging."

### §14.2 ANTIOXIDANTS

定义与机理（约 line 164-169）：
> "Antioxidants retard oxidative degradation. Heat, mechanical shear, ultraviolet (UV) radiation, and heat can be responsible for the formation of free radicals, which in turn can act to shorten polymer chains and increase crosslinking, both leading to a deterioration in material properties. Free radical production often begins a chain reaction."

主抗氧剂：
> "Primary antioxidants donate active hydrogen atoms to free radical sites, thereby quenching or stopping the chain reaction."

副抗氧剂：
> "Secondary antioxidants or synergists act to decompose free radicals to more stable products."

链转移机理：
> "the antioxidant acts as a chain transfer agent to produce a dead polymer and a stable free radical that does not initiate chain radical degradation. However, the phenoxy free radical may react with other free radicals to produce a quinone derivative."

### §14.3 HEAT STABILIZERS

PVC 脱 HCl 机理（约 line 177-183）：
> "In addition to the free radical chain degradation described for polyolefins, another type of degradation (dehydrohalogenation) also occurs with chlorine-containing polymers such as PVC. As shown by the following equation, when heated PVC may lose hydrogen chloride and form a chromophoric conjugated polyene structure. Since the allylic chlorides produced are very unstable, the degradation continues as an unzipping type of chain reaction."

"This type of degradation is accelerated in the presence of iron salts, oxygen, and hydrogen chloride."

金属盐 HCl 清除剂：
> "Toxic lead and barium and cadmium salts act as scavengers for hydrogen chloride and may be used as heat stabilizers in some applications, such as wire coating."

有机磷化物/环氧化油：
> "Organic phosphites, such as mixed aryl and alkyl phosphites or triphenyl phosphite, form complexes with free metallic ions and prevent the formation of insoluble metal chlorides. Less toxic, epoxidized, unsaturated oils such as soy bean oil act as HCl scavengers."

### §14.4 ULTRAVIOLET STABILIZERS

UV 能量（约 line 192-194）：
> "Since the energy of this radiation is 100 to 72 kcal, it is sufficiently strong to cleave covalent bonds and cause yellowing and embrittlement of organic polymers."

金属配合物与颜料：
> "The metal complexes function as energy transfer agents, free radical scavengers, and decomposers of hydroperoxides. The pigments absorb UV radiation and act as screening agents. More than 100,000 tons of UV stabilizers is used annually by the U.S. polymer industry."

### §14.5 FLAME RETARDANTS

燃烧三角（约 line 219-220）：
> "Fuel, oxygen, and high temperature are essential for the combustion process."

自由基终止（约 line 217-218）：
> "Since halogen and phosphorus radicals couple with free radicals produced in the combustion process and terminate the reaction, many flame retardants are halogen or phosphorus compounds."

ATH（水合氧化铝）：
> "Fillers such as alumina trihydrate (ATH) release water when heated and hence reduce the temperature of the combustion reaction."

Sb₂O₃ + 溴协同（约 line 228-231）：
> "Synergistic flame retardants such as a mixture of antimony trioxide and an organic bromo compound are much more effective than single flame retardants. Thus, while a polyester containing 11.5% tetrabromophthalic anhydride burned without charring at high temperatures, charring but no burning was noted when 5% antimony oxide was added."

成炭：
> "Char, formed in some combustion processes, also shields the reactants from oxygen and retards the outward diffusion of volatile combustible products. Aromatic polymers tend to char, and some phosphorus and boron compounds catalyze char formation."

### §14.6-14.14 其他添加剂

§14.9 Antistatic Agents（原文综合）：
> "Antistatic agents (antistats) dissipate static electrical charges. Insulating materials including most organic plastics, fibers, films, and elastomers can build up electrical charge."

> "Such charge buildup is particularly noticeable in cold, dry climates and leads to dust attraction and sparking."

> "Most antistats are hygroscopic and attract a thin film of water to the polymer surface."

§14.10 Chemical Blowing Agents：
> "Chemical blowing agents (CBAs) are employed to create lighter weight material through formation of a foam."

> "Cellular polymers not only provide insulation and resiliency but are usually stronger on a weight basis than solid polymers."

§14.11 Compatibilizers：
> "Compatibilizers are compounds that provide miscibility or compatibility to materials that are otherwise immiscible or only partially miscible, yielding a homogeneous product that does not separate into its components."

> "Typically compatibilizers act to reduce the interfacial tension and are concentrated at phase boundaries."

> "Reactive compatibilizers react chemically with the materials they are to make compatible. Nonreactive compatibilizers perform their task by physically making the various component materials compatible."

§14.12 Impact Modifiers：
> "Impact modifiers improve the resistance of materials to stress."

> "Most impact modifiers are elastomers such as ABS, BS, methacrylate–butadiene–styrene, acrylic, ethylene–vinyl acetate, and chlorinated polyethylene."

§14.14 Lubricants：
> "Lubricants are added to improve the flow characteristics of a material during its processing. They operate by reducing the melt viscosity or by decreasing adhesion between the metallic surfaces of the processing equipment and the material being processed."

> "Internal lubricants reduce molecular friction, consequently decreasing the material's melt viscosity and allowing it to flow more easily."

> "External lubricants act by increasing the flow of the material by decreasing the friction of the melted material as it comes into contact with surrounding surfaces."

## Step 3 — 概念定义（Definitions & Terminology）

||||
|---|---|---|
|1|Plasticizer|增塑剂|"a material incorporated in a plastic to increase its workability and flexibility or distensibility"|
|2|Internal Plasticization|内部增塑|"through copolymerization giving a more flexible polymer backbone or by grafting"|
|3|External Plasticization|外部增塑|"through incorporation of a plasticizing agent into a polymer through mixing and/or heating"|
|4|Primary Antioxidant|主抗氧剂|"donate active hydrogen atoms to free radical sites, thereby quenching or stopping the chain reaction"|
|5|Secondary Antioxidant (Synergist)|副抗氧剂/协同剂|"act to decompose free radicals to more stable products"|
|6|Dehydrohalogenation|脱卤化氢|"when heated PVC may lose hydrogen chloride and form a chromophoric conjugated polyene structure"|
|7|Heat Stabilizer|热稳定剂|"Toxic lead and barium and cadmium salts act as scavengers for hydrogen chloride"|
|8|UV Stabilizer|UV 稳定剂|"function as energy transfer agents, free radical scavengers, and decomposers of hydroperoxides"|
|9|Flame Retardant|阻燃剂|"Since halogen and phosphorus radicals couple with free radicals produced in the combustion process"|
|10|ATH (Alumina Trihydrate)|水合氧化铝|"release water when heated and hence reduce the temperature of the combustion reaction"|
|11|Synergistic Flame Retardant|协同阻燃剂|"mixture of antimony trioxide and an organic bromo compound are much more effective than single flame retardants"|
|12|Char|炭层|"shields the reactants from oxygen and retards the outward diffusion of volatile combustible products"|
|13|Biocide / Antimicrobial|抗菌剂|Retard microbial attack ("pink staining" in PVC)|
|14|Lubricant|润滑剂|"improve the flow characteristics of a material during its processing"|
|15|Compatibilizer|相容剂|"provide miscibility or compatibility to materials that are otherwise immiscible"|
|16|Antistatic Agent (Antistat)|抗静电剂|"dissipate static electrical charges"|
|17|Chemical Blowing Agent (CBA)|化学发泡剂|"employed to create lighter weight material through formation of a foam"|
|18|Impact Modifier|抗冲改性剂|"improve the resistance of materials to stress"|

## Step 4 — 关键方程 / 数据

|||
|---|---|
|PVC 溶度参数 δ|9.66|与增塑剂匹配判据|
|DOP 溶度参数 δ|8.85|与 PVC 相近故相容|
|UV 能量|100–72 kcal|足以断裂共价键|
|DOP 人体年摄入|~2 g/人|暴露评估|
|UV 稳定剂年用量（美）|> 100,000 吨|工业规模|
|ATH 阻燃机制|受热释放 H₂O，降低火焰温度|稀释型阻燃|
|Sb₂O₃ + Br 协同|聚酯含 11.5% TBPA + 5% Sb₂O₃ → 成炭不燃|协同型阻燃|

## Step 5 — 原文摘选（Excerpts, Original English）

DOP 历史与地位（约 line 74-76）：
"Waldo Semon patented the use of tricresyl phosphate as a plasticizer for poly(vinyl chloride) (PVC) in 1933. This was later replaced by the less toxic di-2-ethylhexyl phthalate (DOP), which is now the most widely used plasticizer."

溶度参数匹配（约 line 105-108）：
"Plasticizers with solubility parameters and type of bonding similar to those of the polymer are more apt to be compatible than when the solubility parameters are different. The solubility parameter for PVC (9.66) is near that of good plasticizers for PVC such as DOP (8.85)."

增塑剂毒性与迁移（约 line 114-119）：
"The development of plasticizers has been plagued with toxicity problems. Thus, the use of highly toxic polychlorinated biphenyls (PCBs) has been discontinued. Phthalic acid esters, such as DOP, may be extracted from blood stored in plasticized PVC blood bags and tubing... These problems have been solved by using oligomeric polyesters as nonmigrating plasticizers, instead of DOP."

主/副抗氧剂（约 line 167-169）：
"Primary antioxidants donate active hydrogen atoms to free radical sites, thereby quenching or stopping the chain reaction."

"Secondary antioxidants or synergists act to decompose free radicals to more stable products."

PVC 脱 HCl（约 line 177-181）：
"In addition to the free radical chain degradation described for polyolefins, another type of degradation (dehydrohalogenation) also occurs with chlorine-containing polymers such as PVC. As shown by the following equation, when heated PVC may lose hydrogen chloride and form a chromophoric conjugated polyene structure. Since the allylic chlorides produced are very unstable, the degradation continues as an unzipping type of chain reaction."

燃烧三角（约 line 219-220）：
"Fuel, oxygen, and high temperature are essential for the combustion process."

Sb₂O₃ 协同（约 line 228-231）：
"Synergistic flame retardants such as a mixture of antimony trioxide and an organic bromo compound are much more effective than single flame retardants. Thus, while a polyester containing 11.5% tetrabromophthalic anhydride burned without charring at high temperatures, charring but no burning was noted when 5% antimony oxide was added."

抗静电剂（原文综合）：
"Most antistats are hygroscopic and attract a thin film of water to the polymer surface. Internal antistats are admixed with the polymer, while external antistats are usually sprayed on the polymer surface."

相容剂（原文综合）：
"Compatibilizers are compounds that provide miscibility or compatibility to materials that are otherwise immiscible or only partially miscible, yielding a homogeneous product that does not separate into its components."

润滑剂（原文综合）：
"Internal lubricants reduce molecular friction, consequently decreasing the material's melt viscosity and allowing it to flow more easily. External lubricants act by increasing the flow of the material by decreasing the friction of the melted material as it comes into contact with surrounding surfaces."

## Step 6 — RIA 实践转化

### 卡片 1：卫材配方中的增塑剂选择与安全性权衡

- Read：原文 "average person takes in about 2 g a year of external plasticizers. Most of this is from traces of DOA migrating from food packaging" + "DOP, may be extracted from blood stored in plasticized PVC blood bags"
- Interpret：增塑剂（尤其邻苯二甲酸酯类 DOP/DBP/DEHP）的迁移性是其核心安全短板；替代路径是"寡聚聚酯非迁移型增塑剂"
- Apply：
- 卫材中 PVC 涂层尿布/床单应优先选用寡聚聚酯型增塑剂（而非 DOP），减少皮肤接触暴露
- 湿巾/护肤包装避免使用 DOP；若必须使用 PVC，采用溶度参数匹配法选 δ 与 PVC 9.66 相近、分子量高的增塑剂，降低迁移率
- 卫材监管合规性要求：DEHP/DOP 在婴幼儿产品中禁用或严格限量（参考中国 GB、欧盟 REACH、美国 CPSIA）

### 卡片 2：抗氧化剂与热稳定剂——卫材货架寿命的核心

- Read：原文 "Antioxidants retard oxidative degradation... Primary antioxidants donate active hydrogen atoms... Secondary antioxidants act to decompose free radicals to more stable products"
- Interpret：PP/PE 纺粘无纺布在挤出加工过程中面临 200°C+ 高温剪切氧化——主抗氧剂（受阻酚，如 BHT）终止自由基链反应；副抗氧剂（亚磷酸酯）分解氢过氧化物；两种协同使用
- Apply：
- PP 熔体纺丝：BHT + 亚磷酸酯（168）复配抗氧化体系
- PE 水刺无纺布：受阻酚抗氧剂，抑制仓储期间的"氧氧化脆化"
- PVC 涂层：必须加 HCl 清除剂（钙/锌皂、有机磷酸酯、环氧化大豆油）——原文指出 HCl 是"unzipping"链式降解催化剂

### 卡片 3：抗静电剂——PP/PE 无纺布生产的良率保障

- Read：原文 "Most antistats are hygroscopic and attract a thin film of water to the polymer surface. Internal antistats are admixed with the polymer, while external antistats are usually sprayed on the polymer surface."
- Interpret：PP 与 PE 熔喷/纺粘工艺中静电积累导致飞丝、粘连、卷取不良；抗静电剂通过"表面吸湿薄膜"提供导电通路
- Apply：
- 熔喷无纺布：内部抗静电剂（季铵盐、多元醇衍生物）在粒料阶段共混
- 卫材成品表面：外部抗静电喷雾（脂肪酸甘油酯类）
- 湿度敏感：干冷环境下抗静电失效——需选非吸湿型（如导电炭黑/碳纳米管掺杂型）抗静电体系

### 卡片 4：阻燃剂与协同效应——婴幼儿用品安全设计

- Read：原文 "Fuel, oxygen, and high temperature are essential for the combustion process" + "mixture of antimony trioxide and an organic bromo compound are much more effective than single flame retardants"
- Interpret：卫材本身是低可燃性（含大量纸/纤维），但弹性腰围、热封条含 PE/EVA 等热塑性；婴幼儿睡袋、防溢乳垫等场景仍需阻燃评估
- Apply：
- 首选 ATH（水合氧化铝）作为无机阻燃填充——通过受热释放 H₂O 稀释火焰温度，同时充当 §13 的填料/增强功能，一石二鸟
- Sb₂O₃ + Br 协同（原文 11.5% TBPA + 5% Sb₂O₃）用于对薄壁件阻燃要求高的产品
- 成炭型阻燃剂（磷、硼化合物）：原文 "aromatic polymers tend to char"——可考虑芳香族结构 PP/PE 共聚物

### 卡片 5：相容剂与抗冲改性剂——复合卫生材料的界面工程

- Read：原文 "Compatibilizers are compounds that provide miscibility or compatibility... reduce the interfacial tension and are concentrated at phase boundaries" + "Most impact modifiers are elastomers such as ABS, SBS, MBS, acrylic, EVA, chlorinated polyethylene"
- Interpret：卫材结构中的多层共挤（PP/PE/粘合层）与复合材料常面临不相容问题；抗冲改性剂通过橡胶相"吸收冲击能量"提高韧性
- Apply：
- PP 与非极性 PE 共混：需马来酸酐接枝 PP（反应型相容剂）在界面形成化学桥
- 湿巾防水底膜（PE + 黏土纳米复合材料）：titanate/silane 偶联剂（§13）+ compatibilizer 双重界面工程
- 婴儿鞋/玩具等硬制品：EVA、CPE 抗冲改性剂提高低温韧性

## Step 7 — 合成报告

### 7.1 章节地图

Ch.14 Plasticizers and Additives
├── §14.1 Plasticizers（增塑剂）
│   ├── ASTM D-883 定义: workability, flexibility, distensibility
│   ├── Internal (共聚/接枝) vs External (混入)
│   ├── DOP 历史: tricresyl phosphate (1933) → DOP → 寡聚聚酯
│   ├── 谱系: phthalate (DOP), trimellitate (TOTM), adipate (DOA)
│   ├── 溶度参数匹配: PVC δ=9.66, DOP δ=8.85
│   └── 毒性/迁移: PCB 禁用; DOP 从血袋/汽车内饰迁移; 人体年摄入 ~2 g
├── §14.2 Antioxidants（抗氧化剂）
│   ├── 定义: 阻断自由基链式降解
│   ├── Primary: 供 H 原子, 终止链反应 (受阻酚 BHT)
│   ├── Secondary: 分解自由基 (亚磷酸酯 168)
│   └── 协同: 复配使用; 炭黑也是抗氧剂
├── §14.3 Heat Stabilizers（热稳定剂）
│   ├── PVC 脱 HCl (dehydrohalogenation): 共轭多烯→黄变+脆化
│   ├── 铁盐/O₂/HCl 加速该反应
│   ├── 金属盐: 铅/钡/镉 (剧毒, 仅限导线涂层)
│   └── 有机磷酸酯 + 环氧化大豆油: 非毒 HCl 清除剂
├── §14.4 UV Stabilizers（UV 稳定剂）
│   ├── UV 能量 100-72 kcal: 足以断裂共价键
│   ├── 机制: 能量转移 / 自由基清除 / 过氧化物分解 / 屏蔽
│   ├── 品类: 2-hydroxybenzophenone, benzotriazole, 镍配合物, 炭黑
│   └── 年用量 > 100,000 吨 (美)
├── §14.5 Flame Retardants（阻燃剂）
│   ├── 燃烧三角: 燃料 + O₂ + 高温
│   ├── 机制: (1) 稀释(ATH 释放 H₂O); (2) 成炭(磷/硼催化); (3) 自由基终止(Hal/Br/P)
│   ├── Synergist: Sb₂O₃ + 有机溴化合物
│   └── 分级: additive / external / internal
├── §14.6 Biocides（抗菌剂）: 抗"pink staining"等微生物污染
├── §14.7 Lubricants（润滑剂）: internal (降低分子间摩擦) vs external (降低设备黏附)
├── §14.8 Curing Agents（固化剂）: accelerator (CBS/DMBT), peroxide, drier
├── §14.9 Antistatic Agents（抗静电剂）: 吸湿薄膜 + 表面喷雾
├── §14.10 CBAs（化学发泡剂）: 物理 (戊烷/氟利昂) + 化学 (产 N₂)
├── §14.11 Compatibilizers（相容剂）: 反应型 (接枝) vs 非反应型 (接枝共聚物)
├── §14.12 Impact Modifiers（抗冲改性剂）: ABS, SBS, MBS, acrylic, EVA, CPE
└── §14.13 Processing Aids（加工助剂）: acrylate copolymers

### 7.2 概念索引

|||||
|---|---|---|---|
|1|Plasticizer (ASTM D-883)|增塑剂|line ~63|Ch.14|
|2|Internal / External Plasticization|内部/外部增塑|line ~45|Ch.14|
|3|Primary Antioxidant|主抗氧剂|line ~167|Ch.14|
|4|Secondary Antioxidant|副抗氧剂|line ~168|Ch.14|
|5|Dehydrohalogenation|脱卤化氢|line ~177|Ch.14|
|6|Heat Stabilizer|热稳定剂|line ~184|Ch.14|
|7|UV Stabilizer|UV 稳定剂|line ~192|Ch.14|
|8|Flame Retardant|阻燃剂|line ~217|Ch.14|
|9|ATH (Alumina Trihydrate)|水合氧化铝|line ~220|Ch.13 (填料), Ch.14|
|10|Synergistic Flame Retardant|协同阻燃剂|line ~228|Ch.14|
|11|Char|炭层|line ~224|Ch.14|
|12|Biocide|抗菌剂|§14.6|Ch.14|
|13|Lubricant (Internal/External)|润滑剂|§14.14|Ch.14|
|14|Compatibilizer|相容剂|§14.11|Ch.14|
|15|Antistatic Agent|抗静电剂|§14.9|Ch.14|
|16|Chemical Blowing Agent|化学发泡剂|§14.10|Ch.14, Ch.17|
|17|Impact Modifier|抗冲改性剂|§14.12|Ch.14|

### 7.3 原文摘选索引

|||
|---|---|
|~63-65|"a plasticizer is a material incorporated in a plastic to increase its workability and flexibility or distensibility"|ASTM 定义|
|~74-76|"tricresyl phosphate (1933) → less toxic di-2-ethylhexyl phthalate (DOP)"|DOP 历史|
|~105-108|"PVC (9.66) is near that of good plasticizers for PVC such as DOP (8.85)"|溶度参数|
|~114-119|"phthalic acid esters, such as DOP, may be extracted from blood stored in plasticized PVC blood bags"|迁移/毒性|
|~164-169|"Primary antioxidants donate active hydrogen atoms... Secondary... decompose free radicals"|抗氧剂机制|
|~177-181|"when heated PVC may lose hydrogen chloride and form a chromophoric conjugated polyene structure"|脱 HCl|
|~184-185|"Toxic lead and barium and cadmium salts act as scavengers for hydrogen chloride"|热稳定剂|
|~187-190|"Organic phosphites... form complexes with free metallic ions... Less toxic, epoxidized, unsaturated oils such as soy bean oil act as HCl scavengers"|非毒替代|
|~192-194|"energy of this radiation is 100 to 72 kcal... cleave covalent bonds"|UV 能量|
|~217-218|"halogen and phosphorus radicals couple with free radicals produced in the combustion process"|阻燃机制|
|~219-220|"Fuel, oxygen, and high temperature are essential for the combustion process"|燃烧三角|
|~220-222|"alumina trihydrate (ATH) release water when heated and hence reduce the temperature"|ATH|
|~228-231|"mixture of antimony trioxide and an organic bromo compound are much more effective than single flame retardants"|协同阻燃|
|§14.9|"Most antistats are hygroscopic and attract a thin film of water to the polymer surface"|抗静电|
|§14.11|"Compatibilizers are compounds that provide miscibility or compatibility to materials that are otherwise immiscible"|相容剂|
|§14.14|"Internal lubricants reduce molecular friction... External lubricants act by... decreasing the friction of the melted material as it comes into contact with surrounding surfaces"|润滑剂|

End of Chapter 14 Deep-Dive Report

---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_fe14bc6d861c34d02d6a24a92e4e2530001a693ee6c0644e"
source_file: "Ebewole Polymer Science Technology_ch13.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch13.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Ebewole Polymer Science Technology_ch13.md.md

# 第 13 章 · Mechanical Properties of Polymers（聚合物力学性能）

源文件：/sandbox/workspace/deepread/chapters/ebewole_ch13.txt（91,588 chars, pp. 344–380）
语言规则：框架中文 · 概念定义与原文引文保留英文 · 术语首次出现「英文 + 中文释义」

## 一、执行摘要（Executive Summary）

本章为卫材非织造布性能评估提供了核心力学概念底座。围绕三大测试体系：Stress–Strain（应力-应变）、Creep（蠕变）、Stress Relaxation（应力松弛）、Dynamic（动态力学 DMA）、Impact（冲击）；并系统讨论分子量、交联、结晶度、共聚、增塑、取向、温度、应变速率、压力对模量与韧性的影响。全章给出 40+ 条公式（含断裂力学 K_Ic、G_Ic、Griffith 裂纹理论）。

核心业务命题：非织造布（spunbond / meltblown / SMS）的柔软度、拉伸断裂、穿刺强度、湿/干态力学差异、低温脆断、抗蠕变（长期承力）均以此为理论基础。

## 二、章节概览（Chapter Overview）

||||
|---|---|---|
|I|Introduction|344|
|II|MECHANICAL TESTS|345|
|II.A|Stress–Strain Experiments|345|
|II.B|Creep Experiments|346|
|II.C|Stress Relaxation|347|
|II.D|Dynamic Mechanical Experiments|347|
|II.E|Impact Experiments|349|
|III|Stress–Strain Behaviors of Polymers|355|
|III.A|Elastic Stress–Strain Relations|351|
|V|Compression vs. Tensile Tests|358|
|VI|Effects of Structural and Environmental Factors|362|
|VI.A|Effect of Molecular Weight|363|
|VI.B|Effect of Cross-Linking|364|
|VI.C|Effect of Crystallinity|364|
|VI.D|Effect of Copolymerization|365|
|VI.E|Effect of Plasticizers|367|
|VI.F|Steric Factors|367|
|VI.G|Effect of Temperature|373|
|VI.H|Effect of Strain Rate|373|
|VI.I|Effect of Pressure|375|
|VII|Polymer Fracture Behavior|376|
|VII.A|Brittle Fracture|376|
|VII.B|Linear Elastic Fracture Mechanics (LEFM)|378|

关键公式（节选 44 条中最关键者）

||||
|---|---|---|
|(13.1)|ε = ε₀ sin ωt|动态应变输入|
|(13.2)|σ = Gε₀ sin ωt|弹性响应（同相）|
|(13.3)|σ = ηε̇ = ηε₀ω cos ωt|粘性响应（90° 滞后）|
|(13.4)|tan δ = G″/G′|损耗因子|
|(13.5)|tan δ = (1/π) ln(A₁/A₂)|由振幅衰减计算 tan δ|
|(13.7)|Δ = π tan δ|对数衰减率|
|(13.8)|σ = F/A₀|工程应力|
|(13.9)|ε = ΔL/L₀|工程应变|
|(13.10)|σ_t = F/A|真实应力|
|(13.11)|ε_t = ln(L/L₀)|真实应变|
|(13.17)|σ = Eε|胡克定律|
|(13.19)|τ = Gγ|剪切胡克|
|(13.22)|ν = −ε_y/ε_x|泊松比|
|(13.23)|ΔV/V₀ = (1−2ν)ε|体积应变|
|(13.24)|E = 2G(1+ν)|模量关系|
|(13.25)|E = 3K(1−2ν)|模量关系|
|(13.31)|σ_c = √(Eγ_s/a₀)|理论内聚强度|
|(13.32)|σ_t = σ₀(1 + 2a/ρ)|裂纹尖端应力集中|
|(13.33)|σ_f = √(2Eγ_s/πa)|平面应力断裂|
|(13.34)|σ_f = √(2Eγ_s/[π(1−ν²)a])|平面应变断裂|
|(13.36)|K = √(πa) σ|应力强度因子|
|(13.37)|G_Ic = K_Ic²/E|应变能释放率（平面应力）|

关键表格
- Table 13.1 – Impact energies for some polymers（p. 349）
- Table 13.2 – Typical Mechanical Properties of Selected Polymers（p. 356）
- Table 13.3 – Characteristic Features of Polymer Stress–Strain Behavior（p. 357）
- Table 13.4 – Effects of rings in polyamide chains（p. 371）
- Table 13.5 – Tg and toughness comparison（p. 371）

关键图
- Fig. 13.1 Stress–strain test | 13.3 Creep of cellulose acetate
- 13.4 Stress relaxation | 13.5 Log E_R vs. log t for unfractionated PMMA
- 13.7 Dynamic phase relation | 13.8 Impact test
- 13.14 Typical stress–strain curves for polymers | 13.15 Cold drawing
- 13.16–13.18 Compression vs. tension | 13.20–13.26 结构-温度曲线族

## 三、原文摘选与批注（English Excerpts with Citations）

### 3.1 力学性能的时-温敏感性

"Compared with those of metals and ceramics, polymer properties show a much stronger dependence on temperature and time. This strong time and temperature sensitivity of polymer properties is a consequence of the viscoelastic nature of polymers."（p. 345）

### 3.2 测试与基本定义

"In stress–strain tests the specimen is deformed (pulled) at a constant rate, and the stress required for this deformation is measured simultaneously."（p. 345）

"Polymers show excessive elastic deformation … due to inadequate rigidity or stiffness. For such failure, the controlling material mechanical property is the elastic modulus."（p. 345）

"The stress that is required to maintain the strain constant decays with time. When this stress is divided by the constant strain, the resultant ratio is the relaxation modulus (E_R(t,T)), which is a function of both time and temperature."（p. 347）

"A convenient measure of damping is in terms of quantities determined from experiment. In physical terms, tan δ denotes material damping characteristics. It is a measure of the ratio of the energy dissipated as heat to the maximum energy stored in the material during one cycle of oscillation."（p. 348）

### 3.3 应力-应变关系

"Ductile materials possess the ability to undergo plastic deformation. For engineering purposes, an appropriate measure of ductility is important, because this property assists in the redistribution of localized stresses."（p. 356）

"The polymer chains in the amorphous regions undergo conformational changes and become oriented (stretched) in the direction of the applied tensile stress. The extended chains resist further deformation."（p. 357）

### 3.4 结构-温度曲线（Modulus–Temperature）

"Five regions of viscoelastic behavior are evident: a hard and glassy region followed by a transition from the glassy to rubbery region. The rubbery plateau, in turn, is followed by a transition to the melt flow region."（p. 363）

"The glassy-to-rubbery transition is denoted by Tg, while the rubber-to-melt-flow transition is indicated by Tfl."（p. 363）

"There is a drop in modulus of about three orders of magnitude near the Tg. There is a further modulus drop at Tfl."（p. 363）

"For the secondary transitions, the drop in modulus is about 10 to 50%, while primary transitions like Tg and Tm, which involve large-scale main chain motions, the drop in modulus varies from one to three orders of magnitude."（p. 373）

### 3.5 结构因素影响

分子量
> "In the glassy region, the modulus is independent of molecular weight … In the rubbery region, the modulus increases with molecular weight until it reaches a plateau."（p. 363）

交联
> "Cross-linking involves chemically connecting polymer molecules by primary valence bonds. This imposes obvious restrictions on molecular mobility."（p. 364）

"In the glassy region, the increase in modulus due to cross-linking is relatively small. Evidently the principal effect of cross-linking is the increase in modulus in the rubbery region and the disappearance of the flow regions."（p. 364）

结晶度
> "Crystallinity in a polymer is the result of ordered molecular aggregation, with molecules held together by secondary valence bonds. Therefore, crystallinity may be viewed as a form of physical cross-linking which is thermoreversible."（p. 364）

"Since crystallites have much higher moduli than the amorphous segments, crystallites can also be regarded as rigid fillers in an amorphous matrix."（p. 364）

共聚
> "Random and alternating copolymers show a single transition that is intermediate between those of the two homopolymers of A and B."（p. 365）

"Block and graft copolymers, which exist as a two-phase system, have two distinct glass transitions, one for each of the homopolymers."（p. 366）

增塑
> "Plasticizers are low-molecular-weight, usually high boiling liquids that are capable of enhancing the flow characteristics of polymers by lowering their glass transition temperatures."（p. 367）

"Modulus, yield, and tensile strengths generally decrease with the addition of plasticizers to a polymer."（p. 367）

"In general, on plasticization a polymer solid undergoes a change from hard and brittle to hard and tough to soft and tough."（p. 367）

### 3.6 温度/应变速率/压力

"As the temperature is increased, the modulus and yield strength decrease and the polymer becomes more ductile."（p. 373）

"As the strain rate increases, polymers in general show a decrease in ductility while the modulus and the yield or tensile strength increase."（p. 373）

"The modulus and yield stress increase with increasing pressure."（p. 375）

### 3.7 断裂力学

"Brittle fracture occurs in materials where the absence of local yielding results in a build-up of localized stresses."（p. 346）

"Fatigue fractures occur without visible signs of yielding since they occur at strengths well below the tensile strength of the material."（p. 346）

"σ_c = √(Eγ_s/a₀)" — theoretical cohesive strength（p. 376）

"σ_t = σ₀(1 + 2a/ρ)" — stress concentration at crack tip（p. 377）

## 四、概念定义表（Concept Definitions）

||||||
|---|---|---|---|---|
|C1|Stress (σ)|应力|σ = F/A₀|p.351 (13.8)|
|C2|Strain (ε)|应变|ε = ΔL/L₀|p.351 (13.9)|
|C3|Young's modulus E|杨氏模量|σ = Eε（linear elastic）|p.353 (13.21)|
|C4|Shear modulus G|剪切模量|τ = Gγ|p.352 (13.19)|
|C5|Bulk modulus K|体积模量|σ = KD|p.352 (13.20)|
|C6|Poisson's ratio ν|泊松比|ν = −ε_y/ε_x|p.353 (13.22)|
|C7|Relaxation modulus E_R(t,T)|松弛模量|"stress divided by the constant strain"|p.347|
|C8|tan δ (loss tangent)|损耗因子|"ratio of the energy dissipated as heat to the maximum energy stored"|p.348|
|C9|True stress / True strain|真实应力/应变|σ_t = F/A; ε_t = ln(L/L₀)|p.351|
|C10|Yield point|屈服点|应力-应变曲线极值/拐点（图 13.13）|p.355|
|C11|Cold drawing|冷拉伸|颈缩后分子链取向延展（Fig. 13.15）|p.357|
|C12|Ductile vs. brittle|韧性 vs. 脆性|"depending on the extent to which the material undergoes plastic deformation before fracture"|p.356|
|C13|Glass transition Tg / T_fl|玻璃化/流动温度|"glassy-to-rubbery transition is denoted by Tg … rubber-to-melt-flow transition … Tfl"|p.363|
|C14|Toughness|韧性|应力-应变曲线面积|p.356|
|C15|Impact strength (Izod / Charpy)|冲击强度|摆锤式冲击能量（Table 13.1）|p.349|
|C16|Fatigue|疲劳|"parts are subjected to alternating or repeated loads"|p.346|
|C17|Stress intensity factor K_Ic|应力强度因子|K = √(πa) σ|p.378 (13.36)|
|C18|Strain-energy-release rate G_Ic|应变能释放率|G = K²/E|p.378 (13.37)|

## 五、原文关键引句速查（Key Quotations Index）

|||||
|---|---|---|---|
|时温敏感性|"stronger dependence on temperature and time"|345|高分子力学核心特征|
|Modulus 定义|"controlling material mechanical property is the elastic modulus"|345|刚度判定|
|E_R(t)|"a function of both time and temperature"|347|粘弹性|
|tan δ 物理意义|"ratio of the energy dissipated as heat to the maximum energy stored"|348|阻尼|
|韧性-脆性|"depending on the extent to which the material undergoes plastic deformation"|356|断裂模式|
|Cold drawing|"chains become oriented (stretched) in the direction of the applied tensile stress"|357|拉伸取向|
|5 区温度曲线|"hard and glassy region … rubbery plateau … melt flow"|363|模量-温度骨架|
|3 个数量级|"drop in modulus of about three orders of magnitude near the Tg"|363|Tg 判定|
|分子量|"modulus is independent of molecular weight" in glassy|363|分子量影响|
|交联|"restrictions on molecular mobility"|364|交联|
|结晶|"physical cross-linking which is thermoreversible"|364|结晶|
|共混-共晶|"random and alternating copolymers show a single transition"|365|共聚|
|增塑|"hard and brittle to hard and tough to soft and tough"|367|增塑|
|温度↑|"modulus and yield strength decrease and the polymer becomes more ductile"|373|温度|
|应变速率↑|"decrease in ductility while the modulus … increase"|373|应变速率|
|压力↑|"modulus and yield stress increase with increasing pressure"|375|压力|
|Griffith 理论|σ_c = √(Eγ_s/a₀)|376|断裂强度|

## 六、概念聚类（Concept Clusters）

### 聚类 A · 测试方法

- 应力-应变 / 蠕变 / 松弛 / DMA / 冲击（5 类）→ C1–C2, C7–C8, C15
### 聚类 B · 弹性模量族

C3（E）+ C4（G）+ C5（K）+ C6（ν）
- 相互关系：E = 2G(1+ν) = 3K(1−2ν)

### 聚类 C · 模量-温度曲线

C13（Tg/Tfl）→ C16（分子量）→ 交联 → 结晶 → 共聚 → 增塑 → 温度 → 应变速率 → 压力

### 聚类 D · 断裂力学

C12（韧/脆）→ C17（K_Ic）→ C18（G_Ic）→ σ_c / σ_t（Griffith）

## 七、业务价值判断（Business Relevance — 卫材非织造布）

直接相关性（高）
- 拉伸/撕裂/穿刺：非织造布的 ASTM D5034 / ISO 13934 / 各向同性/各向异性力学差异直接由本章 stress-strain 体系解释。
- 柔软度 vs. 强度权衡：tan δ 高（高阻尼）→ 柔软触感，但同时强度下降——这是卫材手感-强度矛盾的热力学根源。
- 应变速率敏感性（p. 373）：瞬态使用场景（穿脱、抓握）的力学响应不同于稳态使用——决定产品规格测试速度的选取。
- Tg 附近的三个数量级模量下降（p. 363）：决定卫材使用温度窗口。PP Tg ≈ −10°C、PE Tg ≈ −100°C、PVA Tg ≈ 80°C、PAN Tg ≈ 105°C——各原料的适用性评估。
- 结晶 = 物理交联（p. 364）：热粘合（thermobonding）工艺的本质——加热至结晶熔融附近使纤维粘连，冷却重结晶恢复强度。
- 断裂力学 K_Ic / G_Ic：穿刺、撕破评估（卫材关键指标）的理论依据。

间接相关性
- 疲劳（p. 346）：重复使用类非织造布（如口罩、可重复擦拭布）的寿命评估。

报告结束。所有英文引句均取自 ebewole_ch13.txt 原文。


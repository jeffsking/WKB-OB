---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_48296e723386f58cc9bf5269a66c84b4001a693ee6c0644e"
source_file: "Ebewole Polymer Science Technology_ch14.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch14.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Ebewole Polymer Science Technology_ch14.md.md

# 第 14 章 · Polymer Viscoelasticity（聚合物粘弹性）

源文件：/sandbox/workspace/deepread/chapters/ebewole_ch14.txt（46,534 chars, pp. 390–411）
语言规则：框架中文 · 概念定义与原文引文保留英文 · 术语首次出现「英文 + 中文释义」

## 一、执行摘要（Executive Summary）

本章为卫材非织造布粘弹性评估提供核心理论：从理想弹性（Hooke）、理想粘性（Newton）、橡胶弹性三种极限响应，到 Maxwell 模型、Voigt（Kelvin–Voigt）模型、四参数模型、Maxwell–Weichert 松弛谱、Boltzmann 叠加原理、时温等效（WLF 方程）与主曲线构建。全章是第 13 章"modulus–temperature 曲线"的分子化与数学化延伸。

业务定位：卫材柔软度、压缩回复、压痕持久性、拉伸后回缩、长期承重下蠕变均直接受粘弹性支配。

## 二、章节概览（Chapter Overview）

||||
|---|---|---|
|I|Introduction|390|
|II|SIMPLE RHEOLOGICAL RESPONSES|390|
|II.A|Ideal Elastic Response|390|
|II.B|Pure Viscous Flow|391|
|II.C|Rubberlike Elasticity|391|
|III|VISCOELASTICITY|392|
|IV|MECHANICAL MODELS FOR LINEAR VISCOELASTIC RESPONSE|393|
|IV.A|Maxwell Model|393|
|IV.B|Voigt Element|396|
|IV.C|Four-Parameter Model|401|
|V|MATERIAL RESPONSE TIME — THE DEBORAH NUMBER|404|
|VI|RELAXATION AND RETARDATION SPECTRA|404|
|VI.A|Maxwell–Weichert (Relaxation)|404|
|VI.B|Voigt–Kelvin (Creep)|405|
|VII|SUPERPOSITION PRINCIPLES|407|
|VII.A|Boltzmann Superposition|407|
|VII.B|Time–Temperature Superposition|408|
|VIII|Problems|410|

关键公式（49 条中节选）

||||
|---|---|---|
|(14.1)|σ = Eε|Hooke's law|
|(14.2)|τ = η(dγ/dt)|Newton's law|
|(14.7)|ε̇_T = σ̇/E + σ/η|Maxwell 流变方程|
|(14.9)|ε(t) = σ₀[1/E + t/η]|Maxwell 蠕变|
|(14.12)|σ = σ₀exp(−Et/η)|Maxwell 松弛|
|(14.13)|σ = σ₀exp(−t/τ), τ = η/E|松弛时间|
|(14.14)|E_r(t) = Eexp(−t/τ)|Maxwell 松弛模量|
|(14.17)|tan δ = τω|Maxwell 动态响应|
|(14.20)|σ_T = Eε + η(dε/dt)|Voigt 流变方程|
|(14.22)|ε(t) = (σ₀/E)[1 − exp(−Et/η)]|Voigt 蠕变|
|(14.25)|E' = E; E'' = ηω|Voigt 复模量|
|(14.26)|tan δ = ηω/E = τω|Voigt 损耗因子|
|(14.27)|ε(t) = σ₀[1/E₁ + t/η₂ + 1/E₃(1−exp(−E₃t/η₃))]|四参数蠕变|
|(14.30)|Dn = (material response time)/(experimental time scale)|Deborah 数|
|(14.35)|E_r(t) = Σᵢ Eᵢexp(−t/τᵢ)|离散松弛谱|
|(14.36)|E_r(t) = ∫ E(τ)exp(−t/τ)dτ|连续松弛谱|
|(14.39)|J(t) = Σᵢ Jᵢ[1−exp(−t/τᵢ)]|离散蠕变谱|
|(14.41)|ε(t) = σ₀J(t) + Σ(σᵢ − σᵢ₋₁)J(t−tᵢ)|Boltzmann 叠加（离散蠕变）|
|(14.42)|ε(t) = σ(0)J(t) + ∫J(t−θ)σ̇(θ)dθ|Boltzmann 叠加（连续蠕变）|
|(14.45)|E_r(T₁, t) = E_r(T₂, t/a_T)|时温等效|
|(14.46)|a_T = tT/t{T₀}|移动因子定义|
|(14.47)|log a_T = −C₁(T−T₀)/(C₂+T−T₀)|WLF 方程（一般式）|
|(14.48)|log a_T = −17.44(T−T_g)/(51.6+T−T_g)|WLF（以 Tg 为参考）|
|(14.49)|E_r(reduced) = (T₀ρ₀/Tρ)·E_r(t)|温度-密度修正|

关键图：Fig. 14.1 Ideal elastic | 14.2 Pure viscous | 14.3 Rubber elasticity | 14.4 Maxwell element | 14.5 Maxwell creep/recovery | 14.7 Voigt element | 14.8 Voigt creep | 14.9 Four-parameter | 14.11 Maxwell–Weichert | 14.12 Voigt–Kelvin | 14.13 Time–temperature superposition for polyisobutylene

## 三、原文摘选与批注（English Excerpts with Citations）

### 3.1 粘弹性基本定位

"The behavior of polymeric materials falls between these two extremes."（p. 390）

"The mechanical properties of solid polymers show marked sensitivity to time compared with traditional materials like metals and ceramics."（p. 390）

"Viscoelastic material such as polymers combine the characteristics of both elastic and viscous materials."（p. 392）

"They often exhibit elements of both Hookean elastic solid and pure viscous flow depending on the experimental time scale."（p. 392）

### 3.2 线性粘弹性条件

"The term linear refers to the mechanical response in which the ratio of the overall stress to strain is a function of time only and is independent of the magnitudes of the stress or strain (i.e., independent of stress or strain history)."（p. 390）

"Linear viscoelastic behavior is observed with polymers only under limited conditions involving homogeneous, isotropic, amorphous samples under small strains and at temperatures close to or above the T_g."（p. 390）

### 3.3 Maxwell 模型

"Maxwell suggested a simple series combination of both elements. This model, referred to as the Maxwell element."（p. 393）

"In the Maxwell element, both the spring and the dashpot support the same stress."（p. 393）

"In the Maxwell model, E, the instantaneous tensile modulus, characterizes the response of the spring while the viscosity, η, defines viscous response."（p. 393）

### 3.4 Voigt 模型

"it seems logical to consider a parallel arrangement of the spring and the dashpot. This is the so-called Voigt or Voigt–Kelvin element."（p. 396）

"The total stress supported by the Voigt element is the sum of the stresses in the spring and the dashpot."（p. 396）

"The application of an instantaneous strain induces an infinite resistance in the dashpot."（p. 398）

### 3.5 四参数模型

"Various combinations of these two models may more appropriately simulate real material behavior."（p. 401）

"instantaneous elastic strain, retarded elastic strain, viscous flow, instantaneous elastic recovery, retarded elastic recovery, and plastic deformation (permanent set)."（p. 402）

### 3.6 Deborah 数

"Dn = (material response time)/(experimental time scale)"（p. 404）

### 3.7 松弛谱

"no real material is characterized by a simple response time. Therefore, a more realistic description of materials involves the use of a distribution or continuous spectrum of relaxation or retardation times."（p. 404）

"Real polymers are not characterized by a simple response time. Instead, a distribution or continuous spectrum of relaxation or retardation times is required for a more accurate description of real polymers."（p. 404）

"If one of the Maxwell elements in the Maxwell–Weichert model is replaced with a spring or a dashpot of infinite viscosity, then the stress in such a model would decay to a finite value rather than zero. This would approximate the behavior of a cross-linked polymer."（p. 405）

### 3.8 时温等效（WLF）

"Viscoelastic properties of linear amorphous polymers show time–temperature equivalence. This constitutes the basis for the time–temperature superposition principle."（p. 408）

"The equivalence of time and temperature permits the extrapolation of short-term test data to several decades of time by carrying out experiments at different temperatures."（p. 408）

"Relaxation curves obtained at different temperatures can be superimposed on data at a reference temperature by horizontal shifts along the time scale."（p. 408）

"An important empirical relation correlating the shift factor with temperature changes has been developed by Williams, Landel, and Ferry, the so-called WLF equation."（p. 409）

"Valid between T_g and T_g + 100°C"（p. 409）

### 3.9 Boltzmann 叠加

"The strain at any time t is the sum of the strains produced by all of the stresses applied up to time t."（p. 407）

## 四、概念定义表（Concept Definitions）

||||||
|---|---|---|---|---|
|C1|Viscoelasticity|粘弹性|"combine the characteristics of both elastic and viscous materials"|p.392|
|C2|Linear viscoelasticity|线性粘弹性|"the ratio of the overall stress to strain is a function of time only"|p.390|
|C3|Hookean elastic response|胡克弹性|σ = Eε；"material responds instantaneously to applied stress"|p.390|
|C4|Newtonian viscous flow|牛顿粘性|τ = η(dγ/dt)；"no elastic character"|p.391|
|C5|Maxwell model|麦克斯韦模型|"series combination of both elements"; σ 相等，ε 相加|p.393|
|C6|Relaxation time τ|松弛时间|τ = η/E|p.395 (14.13)|
|C7|Voigt (Kelvin–Voigt) element|沃伊特元素|"parallel arrangement … strain in each element is the same"|p.396|
|C8|Four-parameter model|四参数模型|"series combination of the Maxwell and Voigt models"|p.401|
|C9|Deborah number Dn|德博拉数|Dn = material response time / experimental time scale|p.404|
|C10|Relaxation spectrum|松弛谱|"distribution or continuous spectrum of relaxation or retardation times"|p.404|
|C11|Maxwell–Weichert model|麦克斯韦-韦彻特模型|Σᵢ Eᵢexp(−t/τᵢ)|p.404|
|C12|Boltzmann superposition|玻尔兹曼叠加|"strain at any time t is the sum of the strains produced by all of the stresses"|p.407|
|C13|Time–temperature superposition (TTSP)|时温等效|"superimposed on data at a reference temperature by horizontal shifts"|p.408|
|C14|Shift factor a_T|移动因子|a_T = tT/t{T₀}|p.409|
|C15|WLF equation|WLF 方程|log a_T = −C₁(T−T₀)/(C₂+T−T₀)|p.409|

## 五、原文关键引句速查（Key Quotations Index）

|||||
|---|---|---|---|
|粘弹性定位|"falls between these two extremes"|390|高分子本质|
|时间敏感性|"marked sensitivity to time compared with traditional materials"|390|工程意义|
|定义|"combine the characteristics of both elastic and viscous materials"|392|核心定义|
|线性条件|"ratio of the overall stress to strain is a function of time only"|390|线性|
|小应变限制|"small strains and at temperatures close to or above the T_g"|390|适用边界|
|Maxwell|"series combination of both elements"|393|串联|
|Voigt|"parallel arrangement"|396|并联|
|蠕变六分量|"instantaneous elastic strain, retarded elastic strain, viscous flow, instantaneous elastic recovery, retarded elastic recovery, and plastic deformation"|402|完整响应|
|Deborah 数|Dn = response time / experimental scale|404|时间尺度判据|
|连续谱|"distribution or continuous spectrum of relaxation or retardation times"|404|谱|
|交联-平衡模量|"decay to a finite value rather than zero … cross-linked polymer"|405|交联|
|时温等效|"superimposed on data at a reference temperature by horizontal shifts"|408|TTSP|
|WLF|"Williams, Landel, and Ferry, the so-called WLF equation"|409|移动因子|
|WLF 范围|"between T_g and T_g + 100°C"|409|适用边界|
|Boltzmann|"strain at any time t is the sum of the strains produced by all of the stresses"|407|叠加原理|

## 六、概念聚类（Concept Clusters）

### 聚类 A · 极限响应

C3（胡克弹性）↔ C4（牛顿粘性）→ C1（粘弹性）

### 聚类 B · 机械模型

C5（Maxwell）↔ C7（Voigt）→ C8（四参数）→ C11（Maxwell–Weichert）
- Maxwell：描述应力松弛/粘性流动
- Voigt：描述蠕变/延迟弹性
- 四参数：同时包含瞬态+延迟+粘性流

### 聚类 C · 谱与叠加

C10（松弛谱）+ C12（Boltzmann）+ C9（Deborah）

### 聚类 D · 时温等效

C13（TTSP）→ C14（a_T）→ C15（WLF）

## 七、业务价值判断（Business Relevance — 卫材非织造布）

直接相关性（高）
- 柔软度 / 手感：本质是储能模量 E' 与损耗因子 tan δ 的组合。卫材要求 E' 适中（支撑力）+ tan δ 较高（柔软触感）。
- 压缩持久性：Maxwell 模型预测"永久变形"（粘性流），Voigt 模型预测"可回复蠕变"。非织造布长期使用（如纸尿裤、防护服）的压缩回复是 Maxwell–Voigt 竞争的结果。
- 拉伸回缩（如口罩弹性带）：四参数模型同时预测"瞬态弹性回复 + 延迟弹性回复 + 永久形变"——设计弹性带时控制 t/η 比。
- 短期-长期预测：TTSP + WLF 允许通过短时间高温测试外推长时间常温行为——非织造布货架寿命、耐储存评估。
- 温度窗口：卫材（体温 32–35°C、洗衣 60°C、消毒 70°C）落在多数热塑性 Tg 以上（PP Tg ≈ −10°C），因此处于橡胶-粘流过渡区——粘弹性效应显著。
- Deborah 数：快速穿脱（低 Dn，材料表现"液态"）vs. 静态承重（高 Dn，材料表现"固态"）——同一材料在不同使用场景下表现不同。

间接相关性
- 交联聚合物松弛谱（p. 405）：用于解释化学粘合（chem-bonding）非织造布在应力下的长期表现。

报告结束。所有英文引句均取自 ebewole_ch14.txt 原文。


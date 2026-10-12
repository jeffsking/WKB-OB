---
type: source
title: "Ebewole Polymer Science Ch14 Polymer Viscoelasticity"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch14.md.md
date_published: 1997
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "The behavior of polymeric materials falls between these two extremes. … Viscoelastic material such as polymers combine the characteristics of both elastic and viscous materials. (Ch.14, p.390, p.392)"
  - "Linear viscoelastic behavior is observed with polymers only under limited conditions involving homogeneous, isotropic, amorphous samples under small strains and at temperatures close to or above the T_g. (Ch.14, p.390)"
  - "Maxwell suggested a simple series combination of both elements. … In the Maxwell element, both the spring and the dashpot support the same stress. (Ch.14, p.393)"
  - "No real material is characterized by a simple response time. Therefore, a more realistic description of materials involves the use of a distribution or continuous spectrum of relaxation or retardation times. (Ch.14, p.404)"
  - "Viscoelastic properties of linear amorphous polymers show time–temperature equivalence. This constitutes the basis for the time–temperature superposition principle. … The equivalence of time and temperature permits the extrapolation of short-term test data to several decades of time by carrying out experiments at different temperatures. (Ch.14, p.408)"
  - "An important empirical relation correlating the shift factor with temperature changes has been developed by Williams, Landel, and Ferry, the so-called WLF equation. … Valid between T_g and T_g + 100°C. (Ch.14, p.409)"
summary_cn: "《Ebewole 高分子科学与技术》第 14 章聚合物黏弹性：从胡克弹性、牛顿黏性、橡胶弹性三种极限响应出发，建立 Maxwell（串联）、Voigt（并联）、四参数与 Maxwell–Weichert 松弛谱等机械模型，引入 Deborah 数作为时间尺度判据，并以 Boltzmann 叠加原理与 WLF 时温等效方程实现短期数据向长期行为的外推。"
tags: ["source/book", "polymer-science", "viscoelasticity", "Maxwell-model", "Voigt-model", "four-parameter-model", "relaxation-spectrum", "Deborah-number", "Boltzmann-superposition", "time-temperature-superposition", "WLF-equation", "creep"]
tags_zh: ["黏弹性", "麦克斯韦模型", "沃伊特模型", "四参数模型", "松弛谱", "德博拉数", "玻尔兹曼叠加", "时温等效", "WLF方程", "蠕变与回复"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]", "[[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]", "[[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]]", "[[Elastic Tension & Creep（橡筋张力与回缩率）]]", "[[Elastic Strand Snicking（弹性橡筋断丝失效化）]]", "[[APAO（非晶态聚α-烯烃）]]"]
---

# Ebewole Polymer Science Ch14 Polymer Viscoelasticity

> Source: Ebewole, *Polymer Science and Technology*, Ch.14 (Polymer Viscoelasticity), pp. 390–411. 章节主题：三种极限响应、机械模型、松弛谱、Boltzmann 叠加、时温等效（WLF）。

Chapter 14 is the **mathematisation and molecularisation 数学化与分子化延伸** of the modulus–temperature curve introduced in Ch.13.

## Positioning Viscoelasticity 黏弹性的定位

> "The behavior of polymeric materials falls between these two extremes." (Ch.14, p.390)

> "The mechanical properties of solid polymers show marked sensitivity to time compared with traditional materials like metals and ceramics." (Ch.14, p.390)

> "Viscoelastic material such as polymers combine the characteristics of both elastic and viscous materials." (Ch.14, p.392)

> "They often exhibit elements of both Hookean elastic solid and pure viscous flow depending on the experimental time scale." (Ch.14, p.392)

### Three limiting responses 三种极限响应

| Response 响应 | Constitutive law 本构关系 | Character 特征 |
|---|---|---|
| Ideal elastic (Hookean) 理想弹性 | σ = Eε (14.1) | responds instantaneously 瞬时响应、能量储存 |
| Pure viscous (Newtonian) 纯黏性流动 | τ = η(dγ/dt) (14.2) | no elastic character 无弹性、能量耗散 |
| Rubberlike elasticity 橡胶弹性 | §II.C, p.391 | 熵弹性 |

### Linearity condition and its limits 线性黏弹性的条件与边界

> "The term linear refers to the mechanical response in which the ratio of the overall stress to strain is a function of time only and is independent of the magnitudes of the stress or strain (i.e., independent of stress or strain history)." (Ch.14, p.390)

> "Linear viscoelastic behavior is observed with polymers only under limited conditions involving homogeneous, isotropic, amorphous samples under small strains and at temperatures close to or above the T_g." (Ch.14, p.390)

（中文：线性黏弹性只在**均质、各向同性、非晶、小应变、T≥Tg** 条件下成立 —— 非织造布是各向异性多孔纤网，严格套用线性理论须谨慎。）

## Mechanical Models 机械模型

### Maxwell model 麦克斯韦模型（串联）

> "Maxwell suggested a simple series combination of both elements. This model, referred to as the Maxwell element." (Ch.14, p.393)

> "In the Maxwell element, both the spring and the dashpot support the same stress." (Ch.14, p.393)

> "In the Maxwell model, E, the instantaneous tensile modulus, characterizes the response of the spring while the viscosity, η, defines viscous response." (Ch.14, p.393)

| Eq. | Expression 表达式 | Meaning 含义 |
|---|---|---|
| (14.7) | ε̇_T = σ̇/E + σ/η | rheological equation 流变方程 |
| (14.9) | ε(t) = σ₀[1/E + t/η] | creep 蠕变（含永久流动项） |
| (14.12) | σ = σ₀ exp(−Et/η) | stress relaxation 应力松弛 |
| (14.13) | σ = σ₀ exp(−t/τ), **τ = η/E** | relaxation time 松弛时间定义 |
| (14.14) | E_r(t) = E exp(−t/τ) | relaxation modulus 松弛模量 |
| (14.17) | tan δ = τω | dynamic response 动态响应 |

### Voigt (Kelvin–Voigt) element 沃伊特元素（并联）

> "it seems logical to consider a parallel arrangement of the spring and the dashpot. This is the so-called Voigt or Voigt–Kelvin element." (Ch.14, p.396)

> "The total stress supported by the Voigt element is the sum of the stresses in the spring and the dashpot." (Ch.14, p.396)

> "The application of an instantaneous strain induces an infinite resistance in the dashpot." (Ch.14, p.398)

| Eq. | Expression 表达式 | Meaning 含义 |
|---|---|---|
| (14.20) | σ_T = Eε + η(dε/dt) | rheological equation 流变方程 |
| (14.22) | ε(t) = (σ₀/E)[1 − exp(−Et/η)] | creep 蠕变（延迟弹性，无永久流动） |
| (14.25) | E′ = E ; E″ = ηω | complex modulus 复模量 |
| (14.26) | tan δ = ηω/E = τω | loss tangent 损耗因子 |

### Four-parameter model 四参数模型

> "Various combinations of these two models may more appropriately simulate real material behavior." (Ch.14, p.401)

> "instantaneous elastic strain, retarded elastic strain, viscous flow, instantaneous elastic recovery, retarded elastic recovery, and plastic deformation (permanent set)." (Ch.14, p.402)

**ε(t) = σ₀[1/E₁ + t/η₂ + 1/E₃(1 − exp(−E₃t/η₃))]** (Eq. 14.27)

（中文：四参数模型的蠕变六个分量 = **瞬态弹性应变 + 延迟弹性应变 + 黏性流动**；卸载后对应 **瞬态弹性回复 + 延迟弹性回复 + 永久变形（permanent set）** —— 这是"拉伸后回缩"与"压缩永久变形"的标准分解。）

## Deborah Number 德博拉数

> "Dn = (material response time)/(experimental time scale)" (Ch.14, p.404)

（中文：**Dn 大 → 材料表现固态；Dn 小 → 材料表现液态**。同一材料在快速穿脱（短实验时间尺度）与静态长期承重（长时间尺度）下表现不同 —— 这是卫材"手感"与"耐久"难以同时评价的根源。）

## Relaxation and Retardation Spectra 松弛谱与延迟谱

> "No real material is characterized by a simple response time. Therefore, a more realistic description of materials involves the use of a distribution or continuous spectrum of relaxation or retardation times." (Ch.14, p.404)

> "Real polymers are not characterized by a simple response time. Instead, a distribution or continuous spectrum of relaxation or retardation times is required for a more accurate description of real polymers." (Ch.14, p.404)

| Eq. | Expression 表达式 | Form 形式 |
|---|---|---|
| (14.35) | E_r(t) = Σᵢ Eᵢ exp(−t/τᵢ) | discrete relaxation spectrum 离散松弛谱 |
| (14.36) | E_r(t) = ∫ E(τ) exp(−t/τ) dτ | continuous spectrum 连续松弛谱 |
| (14.39) | J(t) = Σᵢ Jᵢ[1 − exp(−t/τᵢ)] | discrete retardation (creep) spectrum 离散延迟谱 |

> "If one of the Maxwell elements in the Maxwell–Weichert model is replaced with a spring or a dashpot of infinite viscosity, then the stress in such a model would decay to a finite value rather than zero. This would approximate the behavior of a cross-linked polymer." (Ch.14, p.405)

（中文：**交联聚合物的应力衰减到有限值而非零** —— 即存在平衡模量，这是区分化学交联与热塑性流动的标志。）

## Superposition Principles 叠加原理

### Boltzmann superposition 玻尔兹曼叠加

> "The strain at any time t is the sum of the strains produced by all of the stresses applied up to time t." (Ch.14, p.407)

| Eq. | Expression 表达式 |
|---|---|
| (14.41) | ε(t) = σ₀J(t) + Σ(σᵢ − σᵢ₋₁)J(t − tᵢ) |
| (14.42) | ε(t) = σ(0)J(t) + ∫J(t − θ)σ̇(θ)dθ |

### Time–temperature superposition 时温等效（TTSP）

> "Viscoelastic properties of linear amorphous polymers show time–temperature equivalence. This constitutes the basis for the time–temperature superposition principle." (Ch.14, p.408)

> "The equivalence of time and temperature permits the extrapolation of short-term test data to several decades of time by carrying out experiments at different temperatures." (Ch.14, p.408)

> "Relaxation curves obtained at different temperatures can be superimposed on data at a reference temperature by horizontal shifts along the time scale." (Ch.14, p.408)

**WLF equation WLF 方程**:

| Eq. | Expression 表达式 |
|---|---|
| (14.45) | E_r(T₁, t) = E_r(T₂, t/a_T) |
| (14.46) | a_T = t_T/t_{T₀} |
| (14.47) | log a_T = −C₁(T − T₀)/(C₂ + T − T₀) |
| (14.48) | **log a_T = −17.44(T − T_g)/(51.6 + T − T_g)** |
| (14.49) | E_r(reduced) = (T₀ρ₀/Tρ)·E_r(t) |

> "An important empirical relation correlating the shift factor with temperature changes has been developed by Williams, Landel, and Ferry, the so-called WLF equation." (Ch.14, p.409)

> "Valid between T_g and T_g + 100°C" (Ch.14, p.409)

（中文：**WLF 以 Tg 为参考时 C₁ = 17.44、C₂ = 51.6 K，适用区间 Tg ~ Tg+100 °C** —— 这是用短期高温测试外推数年常温行为的经典工具。）

## Academic Context and Critique 学术对话与批判

- **WLF 的"通用常数"是近似**：C₁ = 17.44、C₂ = 51.6 是 Williams–Landel–Ferry 对多体系的平均结果，**实际每种聚合物有自己的 C₁、C₂**；超出 Tg ~ Tg+100 °C 区间（尤其接近 Tm 或进入玻璃态）WLF 失效，需改用 Arrhenius 型关系。
- **线性黏弹性的适用边界在本章被明确限定**：均质、各向同性、非晶、小应变、T ≥ Tg（p.390）。非织造布是**各向异性、多孔、半结晶**体系，且使用中常处大变形；因此本章模型只能作为机理语言与定性框架，不能直接作为织物级定量本构。
- **机械模型是现象学的**：Maxwell / Voigt / 四参数用弹簧与黏壶拟合宏观响应，**不提供分子量、缠结、结晶度等结构参数与 τ 的定量映射**；要连接结构需另引 reptation / Rouse 等分子理论。
- **时温等效对半结晶聚合物的限制**：TTSP 严格适用于**线性非晶聚合物**（本章原话）；PP、PE 等半结晶体系在 Tm 以下存在结晶相约束，主曲线构建需谨慎。[待验证]

## Hygiene Implication 卫材关联

1. **Elastic strand tension decay 橡筋张力衰减 = 应力松弛.** 纸尿裤/裤式产品的弹性腰围与橡筋在使用期内的张力衰减，本质即 Maxwell 型的 **σ = σ₀ exp(−t/τ)**；τ = η/E 决定衰减快慢，"回缩率不足"即松弛过快或永久变形过大。参见 [[Elastic Tension & Creep（橡筋张力与回缩率）]]、[[Elastic Strand Snicking（弹性橡筋断丝失效化）]]。
2. **Compression set and recovery 压缩回复 = 蠕变六分量.** 芯体与非织造层的长期使用压缩回复是 Maxwell（黏性流动 → 永久变形）与 Voigt（延迟弹性 → 可回复）竞争的结果；四参数模型的 permanent set 项即"压痕持久性"的定量表达。
3. **TTSP + WLF → 货架寿命外推.** 用不同温度下的短期松弛/蠕变数据沿时间轴平移构建主曲线（p.408），可在数周内评估数年尺度的常温行为 —— 适用于包装受压、长期储存的形变评估。注意 WLF 的 Tg~Tg+100 °C 适用边界。
4. **Deborah 数 → 使用场景决定材料表现.** Dn = 材料响应时间 / 实验时间尺度（p.404）：瞬态穿脱（短尺度 → 低 Dn，偏"液态"响应）与静态承重（长尺度 → 高 Dn，偏"固态"）结论不同，规格测试必须匹配实际使用的时间尺度。
5. **Hot-melt adhesive 热熔胶的黏弹窗口.** 胶黏剂的开放时间、初粘与持粘本质是 E′、E″ 与 tan δ 随温度/频率的变化；本章的复模量（E′ = E, E″ = ηω）与 tan δ = τω 给出定性框架。参见 [[APAO（非晶态聚α-烯烃）]]、[[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]。
6. **Not covered 本章未涉及**: 熔体（非零剪切）流变本构、熔体强度与纺丝稳定性；非织造纤网层面的各向异性黏弹性与纤维间摩擦；填料的体积填充对谱的影响仅间接涉及（见 Ch.9）。模量-温度曲线与 Tg/Tm 的热力学基础见 [[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]；力学测试方法与断裂行为见 [[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]]。

## Related Sources 关联来源

- [[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]
- [[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]
- [[Ebewole Polymer Science Ch13 Mechanical Properties of Polymers]]
- [[Elastic Tension & Creep（橡筋张力与回缩率）]]
- [[Elastic Strand Snicking（弹性橡筋断丝失效化）]]
- [[APAO（非晶态聚α-烯烃）]]

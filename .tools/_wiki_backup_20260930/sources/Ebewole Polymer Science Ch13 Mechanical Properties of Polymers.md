---
type: source
title: "Ebewole Polymer Science Ch13 Mechanical Properties of Polymers"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch13.md.md"
date_published: 1997
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Compared with those of metals and ceramics, polymer properties show a much stronger dependence on temperature and time. This strong time and temperature sensitivity of polymer properties is a consequence of the viscoelastic nature of polymers. (Ch.13, p.345)"
  - "The stress that is required to maintain the strain constant decays with time. When this stress is divided by the constant strain, the resultant ratio is the relaxation modulus (E_R(t,T)), which is a function of both time and temperature. (Ch.13, p.347)"
  - "In physical terms, tan δ denotes material damping characteristics. It is a measure of the ratio of the energy dissipated as heat to the maximum energy stored in the material during one cycle of oscillation. (Ch.13, p.348)"
  - "Five regions of viscoelastic behavior are evident: a hard and glassy region followed by a transition from the glassy to rubbery region. The rubbery plateau, in turn, is followed by a transition to the melt flow region. … There is a drop in modulus of about three orders of magnitude near the Tg. (Ch.13, p.363)"
  - "Crystallinity in a polymer is the result of ordered molecular aggregation … crystallinity may be viewed as a form of physical cross-linking which is thermoreversible. (Ch.13, p.364)"
  - "Random and alternating copolymers show a single transition that is intermediate between those of the two homopolymers of A and B. … Block and graft copolymers, which exist as a two-phase system, have two distinct glass transitions, one for each of the homopolymers. (Ch.13, p.365–366)"
summary_cn: "《Ebewole 高分子科学与技术》第 13 章聚合物力学性能：以黏弹性的时-温敏感性为总纲，系统展开应力-应变、蠕变、应力松弛、动态力学（tan δ）、冲击五类测试，给出模量-温度五区曲线与分子量/交联/结晶/共聚/增塑/温度/应变速率/压力八类结构-环境因素的影响规律，并以 Griffith 裂纹理论与 LEFM（K_Ic、G_Ic）收尾于断裂行为。"
tags: ["source/book", "polymer-science", "mechanical-properties", "stress-strain", "creep", "stress-relaxation", "dynamic-mechanical", "tan-delta", "viscoelasticity", "fracture-mechanics", "LEFM", "impact-strength"]
tags_zh: ["力学性能", "应力应变", "蠕变", "应力松弛", "动态力学", "损耗因子", "黏弹性", "冷拉伸", "断裂力学", "冲击强度", "时温敏感性"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]", "[[Ebewole Polymer Science Ch08 Copolymerization]]", "[[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]", "[[Characterisation, testing and modelling of nonwoven fabrics]]", "[[FZ-T 64112-2024 Nonwovens for Baby Diapers（婴幼儿纸尿裤用非织造布）]]", "[[Handbook of Nonwovens]]"]
---

# Ebewole Polymer Science Ch13 Mechanical Properties of Polymers

> Source: Ebewole, *Polymer Science and Technology*, Ch.13 (Mechanical Properties of Polymers), pp. 344–380. 章节主题：五类力学测试、模量-温度五区曲线、结构-环境因素影响、断裂力学。

Chapter 13 provides the **mechanical concept base 力学概念底座** for evaluating nonwoven performance. Its organising principle is the time–temperature sensitivity of viscoelastic materials.

## Time–Temperature Sensitivity 时-温敏感性（总纲）

> "Compared with those of metals and ceramics, polymer properties show a much stronger dependence on temperature and time. This strong time and temperature sensitivity of polymer properties is a consequence of the viscoelastic nature of polymers." (Ch.13, p.345)

（中文：金属/陶瓷可比，聚合物的力学性能**对温度与时间强烈依赖** —— 所有卫材力学测试必须同时记录温度与速率。）

## Mechanical Tests 五类力学测试

| Test 测试 | Definition / measurable 定义与可观测量 | Source wording 原文表述 |
|---|---|---|
| Stress–strain 应力-应变 | 恒速率拉伸，同步测应力 | "In stress–strain tests the specimen is deformed (pulled) at a constant rate, and the stress required for this deformation is measured simultaneously." (p.345) |
| Creep 蠕变 | 恒应力下应变随时间增长 | §II.B, p.346 |
| Stress relaxation 应力松弛 | 恒应变下维持应力随时间衰减 → **relaxation modulus E_R(t,T)** | "The stress that is required to maintain the strain constant decays with time. When this stress is divided by the constant strain, the resultant ratio is the relaxation modulus (E_R(t,T)), which is a function of both time and temperature." (p.347) |
| Dynamic mechanical (DMA) 动态力学 | 正弦应变输入，测相位滞后 → tan δ | §II.D, p.347–349 |
| Impact 冲击 | 摆锤式（Izod / Charpy）冲击能量 | §II.E, p.349; Table 13.1 |

> "Polymers show excessive elastic deformation … due to inadequate rigidity or stiffness. For such failure, the controlling material mechanical property is the elastic modulus." (Ch.13, p.345)

**Damping 阻尼（tan δ）**:

> "A convenient measure of damping is in terms of quantities determined from experiment. In physical terms, tan δ denotes material damping characteristics. It is a measure of the ratio of the energy dissipated as heat to the maximum energy stored in the material during one cycle of oscillation." (Ch.13, p.348)

**Dynamic relations 动态力学关系**:

| Eq. | Expression 表达式 | Meaning 含义 |
|---|---|---|
| (13.1) | ε = ε₀ sin ωt | dynamic strain input 动态应变输入 |
| (13.2) | σ = Gε₀ sin ωt | elastic response 弹性响应（同相） |
| (13.3) | σ = ηε̇ = ηε₀ω cos ωt | viscous response 黏性响应（滞后 90°） |
| (13.4) | tan δ = G″/G′ | loss tangent 损耗因子 |
| (13.5) | tan δ = (1/π) ln(A₁/A₂) | from amplitude decay 由振幅衰减求 tan δ |
| (13.7) | Δ = π tan δ | logarithmic decrement 对数衰减率 |

## Elastic Constants 弹性常数族

| Quantity 量 | Relation 关系 | Eq. |
|---|---|---|
| Engineering stress 工程应力 | σ = F/A₀ | (13.8) |
| Engineering strain 工程应变 | ε = ΔL/L₀ | (13.9) |
| True stress / strain 真实应力/应变 | σ_t = F/A ; ε_t = ln(L/L₀) | (13.10)–(13.11) |
| Hooke's law 胡克定律 | σ = Eε | (13.17) |
| Shear 剪切 | τ = Gγ | (13.19) |
| Poisson's ratio 泊松比 | ν = −ε_y/ε_x | (13.22) |
| Volumetric strain 体积应变 | ΔV/V₀ = (1 − 2ν)ε | (13.23) |
| Modulus relations 模量关系 | **E = 2G(1+ν) = 3K(1−2ν)** | (13.24)–(13.25) |

## Stress–Strain Behaviour 应力-应变行为

> "Ductile materials possess the ability to undergo plastic deformation. For engineering purposes, an appropriate measure of ductility is important, because this property assists in the redistribution of localized stresses." (Ch.13, p.356)

> "The polymer chains in the amorphous regions undergo conformational changes and become oriented (stretched) in the direction of the applied tensile stress. The extended chains resist further deformation." (Ch.13, p.357)

（中文：**冷拉伸（cold drawing）** 的本质 = 非晶区链构象改变并沿拉伸方向取向，取向后的伸展链抵抗进一步变形 —— 这是非织造布牵伸与热轧后强度提升的分子机制。）

## Modulus–Temperature Curve 模量-温度五区曲线

> "Five regions of viscoelastic behavior are evident: a hard and glassy region followed by a transition from the glassy to rubbery region. The rubbery plateau, in turn, is followed by a transition to the melt flow region." (Ch.13, p.363)

> "The glassy-to-rubbery transition is denoted by Tg, while the rubber-to-melt-flow transition is indicated by Tfl." (Ch.13, p.363)

> "There is a drop in modulus of about three orders of magnitude near the Tg. There is a further modulus drop at Tfl." (Ch.13, p.363)

> "For the secondary transitions, the drop in modulus is about 10 to 50%, while primary transitions like Tg and Tm, which involve large-scale main chain motions, the drop in modulus varies from one to three orders of magnitude." (Ch.13, p.373)

（中文：区分主转变与次级转变的定量判据 —— **次级转变模量下降 10–50%；Tg/Tm 主转变下降 1–3 个数量级**。）

## Effects of Structural and Environmental Factors 结构与环境因素的影响

| Factor 因素 | Effect 影响规律 | Source wording 原文表述 |
|---|---|---|
| Molecular weight 分子量 | 玻璃态区模量与分子量无关；橡胶态区模量随分子量上升至平台 | "In the glassy region, the modulus is independent of molecular weight … In the rubbery region, the modulus increases with molecular weight until it reaches a plateau." (p.363) |
| Cross-linking 交联 | 限制分子运动；橡胶区模量上升、**流动区消失** | "Cross-linking involves chemically connecting polymer molecules by primary valence bonds. This imposes obvious restrictions on molecular mobility." (p.364); "the principal effect of cross-linking is the increase in modulus in the rubbery region and the disappearance of the flow regions." (p.364) |
| Crystallinity 结晶度 | **物理交联（热可逆）**；微晶亦可视为刚性填料 | "crystallinity may be viewed as a form of physical cross-linking which is thermoreversible." (p.364); "Since crystallites have much higher moduli than the amorphous segments, crystallites can also be regarded as rigid fillers in an amorphous matrix." (p.364) |
| Copolymerisation 共聚 | 无规/交替 → 单一中间转变；嵌段/接枝 → 两个 Tg | "Random and alternating copolymers show a single transition that is intermediate between those of the two homopolymers of A and B." (p.365); "Block and graft copolymers, which exist as a two-phase system, have two distinct glass transitions, one for each of the homopolymers." (p.366) |
| Plasticizers 增塑剂 | 降 Tg、增流动；模量/屈服/拉伸强度下降 | "Plasticizers are low-molecular-weight, usually high boiling liquids that are capable of enhancing the flow characteristics of polymers by lowering their glass transition temperatures." (p.367); "Modulus, yield, and tensile strengths generally decrease with the addition of plasticizers." (p.367) |
| Temperature 温度 | 升温 → 模量与屈服强度下降、延性上升 | "As the temperature is increased, the modulus and yield strength decrease and the polymer becomes more ductile." (p.373) |
| Strain rate 应变速率 | 提速 → 延性下降、模量与强度上升 | "As the strain rate increases, polymers in general show a decrease in ductility while the modulus and the yield or tensile strength increase." (p.373) |
| Pressure 压力 | 增压 → 模量与屈服应力上升 | "The modulus and yield stress increase with increasing pressure." (p.375) |

> "In general, on plasticization a polymer solid undergoes a change from hard and brittle to hard and tough to soft and tough." (Ch.13, p.367)

（中文：**增塑三态序列 = 硬而脆 → 硬而韧 → 软而韧**，是手感-强度权衡的定性标尺。）

## Fracture Behaviour 断裂行为

> "Brittle fracture occurs in materials where the absence of local yielding results in a build-up of localized stresses." (Ch.13, p.346)

> "Fatigue fractures occur without visible signs of yielding since they occur at strengths well below the tensile strength of the material." (Ch.13, p.346)

| Relation 关系 | Expression 表达式 | Eq. |
|---|---|---|
| Theoretical cohesive strength 理论内聚强度 | σ_c = √(Eγ_s/a₀) | (13.31) |
| Crack-tip stress concentration 裂尖应力集中 | σ_t = σ₀(1 + 2a/ρ) | (13.32) |
| Griffith fracture stress (plane stress) 平面应力断裂 | σ_f = √(2Eγ_s/πa) | (13.33) |
| Griffith fracture stress (plane strain) 平面应变断裂 | σ_f = √(2Eγ_s/[π(1−ν²)a]) | (13.34) |
| Stress intensity factor 应力强度因子 | K = √(πa)·σ | (13.36) |
| Strain-energy release rate 应变能释放率 | G_Ic = K_Ic²/E | (13.37) |

## Academic Context and Critique 学术对话与批判

- **"模量在玻璃区与分子量无关"是教学简化**：实际玻璃态模量对分子量有弱依赖（链端效应、自由体积），本章取一阶近似。
- **tan δ 高 ≠ 柔软**：把 tan δ 直接当作"手感柔软度"指标是常见误用 —— tan δ 是**耗散/储能之比**，与模量大小是两个独立维度；手感由低模量 + 低摩擦共同决定。[待验证] 卫材柔软度的量化需用 Handle-O-Meter / 弯曲刚度等指标，本章未涉及。
- **提取件的业务批注给出的具体 Tg 数值（PP ≈ −10 °C、PE ≈ −100 °C、PVA ≈ 80 °C、PAN ≈ 105 °C）来自本章摘要的评注段落，并非正文原文** —— [待验证] 引用前须回到 Ch.4 或数据表核对。
- **本章未覆盖**：非织造布专用的各向异性（MD/CD）力学、纤网层面的纤维间滑移与粘合点失效、湿态力学、多孔介质的压缩回弹；这些属织物力学范畴，非本章的块体聚合物力学。
- **LEFM 的适用边界**：K_Ic / G_Ic 建立在小范围屈服与线弹性假设上；非织造布的大变形、纤维拔出与桥联机制不满足该假设，只能作定性参考。

## Hygiene Implication 卫材关联

1. **Tear / tensile / puncture 撕裂、拉伸与穿刺的理论底座.** 非织造布的拉伸断裂、撕破、穿刺强度评估全部落在本章的 stress–strain 体系内；K_Ic / G_Ic 为穿刺与撕破提供断裂力学的定量语言。参见 [[Characterisation, testing and modelling of nonwoven fabrics]]、[[FZ-T 64112-2024 Nonwovens for Baby Diapers（婴幼儿纸尿裤用非织造布）]]。
2. **Softness vs. strength trade-off 手感-强度矛盾.** "Modulus, yield, and tensile strengths generally decrease with the addition of plasticizers"（p.367）与增塑三态序列（硬脆→硬韧→软韧）是**柔软化必然伴随强度损失**的定性根据；但如 §批判所述，tan δ 不应被当作柔软度代理指标。
3. **Strain-rate sensitivity → 测试速度的选择.** "As the strain rate increases … decrease in ductility while the modulus … increase"（p.373）意味着**产品规格必须规定测试速率**：穿脱、抓握等瞬态场景的响应不同于稳态。参见 [[Characterisation, testing and modelling of nonwoven fabrics]]。
4. **Crystallinity = thermoreversible physical cross-linking → 热粘合的本质.** "crystallinity may be viewed as a form of physical cross-linking which is thermoreversible"（p.364）直接解释**热粘合（thermal bonding）**机理：加热至结晶熔融附近使纤维表面粘连、冷却重结晶恢复强度；而"交联使流动区消失"（p.364）解释了化学交联体系无法热粘合。参见 [[Handbook of Nonwovens]]、[[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]。
5. **Copolymer architecture → 单一 vs. 双重 Tg.** "Random and alternating … single transition" vs. "Block and graft … two distinct glass transitions"（p.365–366）是判定共聚型粘合剂/弹性体相结构的依据；与 Ch.8 的序列分布分析互为表里。参见 [[Ebewole Polymer Science Ch08 Copolymerization]]。
6. **Plasticiser and additive packages 助剂影响.** 增塑剂与 Ch.9 的助剂体系共同决定最终力学表现；迁移导致的助剂流失会使产品在使用期内变脆。参见 [[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]。

## Related Sources 关联来源

- [[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]
- [[Ebewole Polymer Science Ch08 Copolymerization]]
- [[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]
- [[Characterisation, testing and modelling of nonwoven fabrics]]
- [[FZ-T 64112-2024 Nonwovens for Baby Diapers（婴幼儿纸尿裤用非织造布）]]
- [[Handbook of Nonwovens]]

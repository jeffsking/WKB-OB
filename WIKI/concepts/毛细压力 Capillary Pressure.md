---
type: concept
title: "毛细压力 Capillary Pressure"
domain: [卫材研发, SAP与流体]
status: growing
updated: 2026-09-30
tags: [capillary-pressure, young-laplace, wicking, pore-size, wettability, rewet, desorption, absorbent-core, hygiene-materials]
---

# 毛细压力 Capillary Pressure
> 📌 **Page completed 2026-09-30** from 3 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

- **毛细压力是吸收的主要驱动力**：吸收由毛细压力驱动，外部施加的重力/压力只起次要作用 —— "Absorption is driven primarily by **capillary pressure** (p_c = 2γcosθ/r); externally imposed gravity or pressure plays only a secondary role"（源：[[Porous Structure and Liquid Flow Models]]）。
- **物理基础是 Young-LaPlace 方程**：ΔP = −2γcosθ / R（ΔP 毛细压、γ 表面张力、θ 接触角、R 孔隙半径）；**毛细压由润湿性（θ）与孔径（R）共同决定**（源：[[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]）。因此测到的毛细压差异**只能归因于这两者之一** —— 这是用它做根因诊断（润湿性 vs 孔径二分）的根据。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 毛细压力公式 | p_c = 2γcosθ/r（亦记 ΔP = −2γcosθ/R） | [[Porous Structure and Liquid Flow Models]]、[[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]] |
| 浸润前沿规律 Wicking front | x_v ∝ t^(1/2)（Washburn / Rudd） | [[Porous Structure and Liquid Flow Models]] |
| 典型扩散率 F₁ | 0.20 cm²/s（paper-like material，L₀ = 20 cm） | [[Porous Structure and Liquid Flow Models]] |
| 纤维堆积分数 φ | 0.025–0.10（2.5 %–10 %） | [[Porous Structure and Liquid Flow Models]] |
| 纤维素密度 ρ_f | ~1.5 g/cc | [[Porous Structure and Liquid Flow Models]] |
| 聚烯烃密度 ρ_f | ~0.92 g/cc（密度低但亲水性差，毛细压力几乎不启动） | [[Porous Structure and Liquid Flow Models]] |
| Kozeny–Carman 常数 k″ | ≈5（k = Φ³/[k″S₀²(1−Φ)²]） | [[Porous Structure and Liquid Flow Models]] |
| Darcy 适用临界雷诺数 | 0.1–75（Scheidegger） | [[Porous Structure and Liquid Flow Models]] |
| 最大吸收容量 C | C = ρ_L·Φ/[ρ·(1−Φ)] | [[Porous Structure and Liquid Flow Models]] |
| 解吸毛细压代表值 | **半饱和（halfway saturated）**处的单一毛细压力，用于代码间比较 | [[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]] |
| 解吸能量 | **height–saturation 曲线下的面积**，单位 **ergs** | [[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]] |
| 解吸能量实测（ATH SAM Relocation） | 6.67E+04 / 6.52E+04 ergs（含绒毛浆层）vs 1.83E+04 / 1.78E+04 ergs（LSE+CW）；**试样质量混淆（0.42 g vs 0.21 g），不可横向比较** | [[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]] |
| 竞品克重对照 | AD surge **49.95 gsm** vs Depend surge **76.97 gsm**（AD 特征毛细压略高但解吸能更低） | [[Rewet Competitive Analysis - Depend vs Always Discreet Intake System（回渗竞品分析 · 2025-09-11）]] |
| 芯体 BET 比表面积 | AD 芯体约为 POISE 的 **12.8×**（高比表面来自复合层而非 SAP 颗粒） | [[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]] |
| 润湿性改动的耦合代价 | 去面层润湿处理：回渗 0.26 → 0.20 g，但**漏液率 3.2 % → 4.6 %** | [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]] |

## Method / Mechanism 方法 / 机理

- **毛细压力法（Capillary Pressure Method）**：试样置于与储液池恒连通的载物台上，垂直移动载物台改变**静水压头**，同步称量持液量并归一化为**饱和度 saturation（g/g）**，得 **height–saturation** 曲线；**下降台面得吸收支（absorption），上升台面得解吸支（desorption）**（源：[[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]）。
- **读数规则**：**毛细压越高 → 孔越想把液体留住**；**解吸能量越低 → 纤维越容易"晾干"**。设计原则：**摄入层（面层/导流层）的毛细性与润湿性必须低于液体最终被锁住的地方（芯体）**（源：[[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]）。
- **速率与容量解耦**：**孔径控制吸收速率（经 Hagen–Poiseuille ∝ r²），孔体积控制容量** —— 优化其一必罚另一个，需中值最优化（源：[[Porous Structure and Liquid Flow Models]]）。
- **解吸 vs 回流的机制划分**：回渗由**两种机制驱动 —— 解吸（Desorption）与回流（Flowback）**；在 POISE 的 FIUP 测试中**解吸主导回渗**；解吸由**摄入系统控制**：摄入系统中的**高毛细压力与界面会截留液体，被截留的液体在受压时表达为回渗**（源：[[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]]）。
- **孔径分布（PSD）比平均孔径更重要**：假说是液体滞留在极小孔里（旁边没有足够大的孔把它拉出来）；对策是**让纤维尺寸趋同以收窄分布**并**减少孔的总数以减少拘留位点**（源：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]）。
- **压力可替代亲水化**：一旦 θ ≥ 90°，毛细拉力为零，只有外加压力能破局；反之亲水表面在零压下换回渗透 —— 两者是工程替代（源：[[Computational Modeling in Absorbent Technology]]）。
- **SAP 侧的对照**：SAP 溶胀由 **Donnan 渗透压**驱动（固定 −COO⁻ 与反离子），故 SAP 在水中溶胀、在盐水中**去溶胀**（源：[[Cross-linked Cellulose and Its Derivatives]]）。

## Hygiene Relevance 卫材关联

- **回渗根因诊断的逐层流程**：① 确认结果指标（Closed Cradle / Cradle 回渗）由**解吸**驱动；② 逐层测毛细压力与解吸能量，找出哪一层偏向竞品；③ 该层按**润湿性 vs 孔径**二分定位根因，孔径路径下再细分平均孔径 vs PSD；④ 改材料 → 回产品台架验回渗，形成闭环（源：[[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]）。
- **实测应用（2025-12-02，Depend 拆解）**：面层与导流层的**毛细压力与解吸能量两项都偏向 Always Discreet**，根因分别定为**润湿性**（面层）与**孔径分布**（导流层）；且 Depend 面层"把液体留得更久"（源：[[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]、[[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]）。
- **反直觉缺口**：AD 摄入系统毛细压力更高 → 按机理**应回渗更高**，但实测 POISE 并未在回渗上被碾压 —— 机理与实测之间存在未解释缺口（源：[[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]]）。
- **低压 / 高压回渗分工**：LPR（常压，主要由摄入层残液决定，归因面层润湿性 + 导流层孔径分布）与 HPR（加压，主要由芯体内可挤出液体决定，归因 SAM 用量/位置）（源：[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]）。
- **"干"与"漏"必须成对验收**：润湿性与孔径两条杠杆各自同时影响回渗与漏液，单指标改动会把结论误导（源：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]）。

## Open Questions 待补

- **毛细压相近 ≠ 孔径结构相近**：半饱和处的单一代表值会吞掉分布信息 `[待补]`（源：[[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]）。
- **归一化基准**：饱和度按试样重量归一化，跨克重比较是否应改用面积/体积基准未决 `[待补]`。
- Depend / Always Discreet 毛细压力与解吸能量的**具体数值未以文本落地**，对外引用须脱敏且不得补写数值（源：[[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]）。
- ⚠️ 库内同时存在 [[Cross-linked Cellulose and Its Derivatives]] 与 [[Cross-linked Cellulose and Its Derivatives]] 两个疑似重复页面，**去重待决** `[待补]`。

## Related Sources 关联来源

- Citing sources（3）: [[Computational Modeling in Absorbent Technology]]、[[Cross-linked Cellulose and Its Derivatives]]、[[Porous Structure and Liquid Flow Models]]
- 测试 / 机理: [[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]、[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]、[[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]]、[[Rewet Competitive Analysis - Depend vs Always Discreet Intake System（回渗竞品分析 · 2025-09-11）]]、[[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]
- 回渗与残液: [[回渗 Rewet]]、[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]、[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]、[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- 方程与相邻概念: [[Laplace Pressure]]、[[达西定律 Darcy's Law]]、[[Washburn Equation]]、[[接触角 Contact Angle]]、[[孔隙率 Porosity]]
- 材料 / 结构: [[SAP（高吸水树脂）]]、[[绒毛浆（Fluff Pulp）]]、[[ADL（导流层）]]、[[吸收芯体]]、[[Resilient Surge（PET 回弹导流层）]]、[[Absorbent Technology]]
- [[Cross-linked Cellulose and Derivatives]]
- [[Liquid Flow in Porous Structures]]


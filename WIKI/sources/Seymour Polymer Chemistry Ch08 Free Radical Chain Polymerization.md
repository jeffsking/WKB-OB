---
type: source
title: "Seymour Polymer Chemistry Ch08 Free Radical Chain Polymerization"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Seymour Polymer Chemistry/chapters/Seymour Polymer Chemistry_ch08.md.md
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Free radical initiation can occur through application of heat (thermal), ultraviolet and visible light (photochemical), ionizing light, redox reagents, electricity (electrochemical), etc."
  - "The initiator efficiency is seldom 100%; an efficiency factor f is employed, with typical values f ≈ 0.3–0.8 (中文：引发效率因子，受笼效应与溶剂粘度影响)."
  - "Under the steady-state assumption the overall rate of polymerization scales as Rp ∝ [M][I]^(1/2), and the kinetic chain length is ν = kp[M] / (2(kt f kd [I])^(1/2)); DP = 2ν for termination by combination and DP = ν for disproportionation."
  - "The Mayo equation 1/DP = 1/DP₀ + Cs[S]/[M] (Eq. 8.36) with Cs = ktr/kp (Eq. 8.37) is the core tool for molecular weight control; thiols are efficient chain transfer agents with Cs of order 10⁵ (1-octanethiol Cs × 10⁴ = 190,000; 1-dodecanethiol Cs × 10⁴ = 148,000; water Cs = 0)."
  - "Autoacceleration, called the Norris-Trommsdorff or gel effect, causes the formation of unusually high molecular weight polymers (中文：自动加速/凝胶效应)."
  - "In emulsion polymerization the concentration of micelles (about 10²¹/L) is high compared with the concentration of monomer droplets (about 10¹⁴/L), which is the physicochemical origin of simultaneously high rate and high molecular weight."
summary_cn: "第8章是自由基链式聚合：以引发剂分解（热/光/辐射/氧化还原/电化学）、稳态假设速率方程与动力学链长、Mayo 方程链转移分子量控制为定量骨架，并比较本体/溶液/悬浮/乳液四种工艺，其中乳液聚合是 SAP 的工业核心路线。"
tags: ["source/book", "free-radical-polymerization", "initiator", "kinetics", "mayo-equation", "chain-transfer", "emulsion-polymerization", "gel-effect", "SAP"]
tags_zh: ["自由基聚合", "引发剂", "聚合动力学", "Mayo方程", "链转移", "乳液聚合", "凝胶效应", "分子量控制", "高吸水树脂"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Seymour Polymer Chemistry Ch03 Molecular Weight of Polymers]]", "[[Seymour Polymer Chemistry Ch06 Step-Reaction Polymerization]]", "[[Seymour Polymer Chemistry Ch07 Ionic and Coordinative Chain Polymerization]]", "[[Seymour Polymer Chemistry Ch09 Copolymerization]]", "[[Acrylic-Based Superabsorbent Polymers]]", "[[A review on superabsorbent polymers]]"]
---

# Seymour Polymer Chemistry Ch08 Free Radical Chain Polymerization

> Source: Seymour/Carraher, *Polymer Chemistry*, Ch.8 — Free Radical Chain Polymerization (Addition Polymerization).
> Citation convention 引用约定: 源文件为 .txt 抽取件，**无正式印张页码**，本页以源文件的行号（line no.）定位；原书页码缺失处标注 [待验证]。

## Executive Summary 内容概要

Chapter 8 covers **free radical chain polymerization（自由基链式聚合）— 据原文为全球合成聚合物产量占比最大的工业聚合技术（原文 Step 1 称约 50%，口径见 [待验证]）**. It builds a complete quantitative chain: **initiator decomposition → steady-state kinetics → kinetic chain length → Mayo equation molecular-weight control → process selection (bulk/solution/suspension/emulsion) → products**. 对卫材的直接意义：SAP（superabsorbent polymer 高吸水树脂，丙烯酸/丙烯酰胺基）在工业上几乎全部通过自由基（乳液或反相悬浮）聚合 + 交联生产。

## Initiators 引发剂

> *"Free radical initiation can occur through application of heat (thermal), (ultraviolet and visible) light (photochemical), (ionizing) light, redox reagents, electricity (electrochemical), etc."* (line 49)

Five initiation modes 五种引发方式：thermal 热、photochemical 光化学、ionizing radiation 辐射、redox 氧化还原、electrochemical 电化学。

| 引发剂类别 Class | 代表 Representative | 分解温度 / 备注 Decomposition |
|---|---|---|
| Azo compounds 偶氮化合物 | AIBN（2,2′-azobis-isobutyronitrile） | 70–80 °C |
| Peroxides 过氧化物 | BPO（benzoyl peroxide） | 60–140 °C |

- **键解离能趋势 Bond dissociation trend**: C–H > C–C > C–N > O–O（过氧键最弱，故过氧化物易热分解）。
- **引发效率 Initiator efficiency**: *"the initiator efficiency is seldom 100%. Hence, an efficiency factor (f) is employed."* (line 59) — 常用 **f ≈ 0.3–0.8**，受 **cage effect 笼效应**、溶剂粘度与引发剂结构影响。
- **分解动力学**: **kd = A·e^(−Ea/RT)**；半衰期 **t₁/₂ = ln2/kd = 0.693/kd** (§8.1)。

Table 8.2 — Rate Constants for Common Initiators（line 533-587，原文摘录；列依次为引发剂/溶剂/温度 °C/kd /Ea kcal·mol⁻¹ [待验证单位口径]）：

| 引发剂 Initiator | 溶剂 Solvent | T (°C) | kd | Ea |
|---|---|---|---|---|
| AIBN | Benzene | 40 | 5.4 × 10⁻⁷ | 30.7 |
| BPO | Benzene | 30 | 4.8 × 10⁻⁸ | 27.8 |
| t-Butyl peroxide | Benzene | 80 | 7.8 × 10⁻⁸ | 34 |
| Acetyl peroxide | Benzene | 35 | 9.5 × 10⁻⁵ | 32.3 |

## Mechanism and Kinetics 机理与动力学

Three elementary steps 三步骤：(1) **Initiation** I → 2R⋅；R⋅ + M → RM⋅；(2) **Propagation** RM⋅ + M → RM₂⋅ → RM₃⋅…；(3) **Termination** by **combination（偶合终止）** or **disproportionation（歧化终止）**.

- 引发速率 **Ri = 2 f kd [I]** (line 74)
- 总聚合速率（稳态假设）: 原文记为 **Rp = kp·M^(1/2)** (line 76)；展开形式为 **Rp = kp[M][M⋅] = kp[M]·(f kd[I]/kt)^(1/2)** (line 163) — 即 **Rp ∝ [M]·[I]^(1/2)**（[I] 的 1/2 次方是双分子终止 + 稳态假设的直接结果）。
- **稳态假设 Steady-state assumption**: *"the number of growing chains remains approximately constant throughout the duration of most copolymerizations"* (line 159)，即 Ri = Rt。
- **动力学链长 Kinetic chain length ν**: **ν = Rp/Rt = kp[M] / (2(kt f kd [I])^(1/2))** (line 81, 169) — ν 正比于 [M]、反比于 [I]^(1/2)。

| 终止方式 Termination | 链长关系 DP vs ν | 中文含义 |
|---|---|---|
| Combination 偶合 | DP = 2ν | 两条链自由基偶合成一条死链 |
| Disproportionation 歧化 | DP = ν | 氢转移生成两条死链（一条带不饱和端基） |

## Chain Transfer and the Mayo Equation 链转移与 Mayo 方程

> *"In chain transfer, the growing macroradical abstracts an atom from a chain transfer agent, S, thus generating a new radical S⋅ and a dead polymer chain."* (line 92)

> **Mayo 方程 Eq. 8.36**：**1/DP = 1/DP₀ + Cs[S]/[M]** (line 97)

> **链转移常数 Eq. 8.37**：**Cs = ktr/kp** — *"The ratio of the rate of cessation or termination by transfer to the rate of propagation is called the chain transfer constant (Cs)."* (line 102)

Table 8.5 — Chain Transfer Constants to Styrene at 60 °C（line 1035-1080；原文表头为 Cs × 10⁴）：

| 链转移剂 Chain transfer agent | Cs × 10⁴ |
|---|---|
| Carbon tetrachloride 四氯化碳 | 84 |
| Carbon tetrabromide 四溴化碳 | 18,000 |
| 1-Dodecanethiol 十二硫醇 | 148,000 |
| 1-Octanethiol 辛硫醇 | 190,000 |
| Toluene 甲苯 | 0.105 |
| Benzene 苯 | 0.01 |
| Water 水 | 0 |

- **硫醇是高效链转移剂**：含 S–H 键的硫醇 Cs 达 10⁵ 量级，因为 S–H 键弱且生成的新自由基稳定（line 115）。
- **Telomerization 调聚反应**: *"When used in large proportions, they are called telogens, since they produce low molecular weight polymers (telomers)."* (line 118)

## Polymerization Techniques 聚合工艺

| 工艺 Technique | 优点 Advantages | 缺点 Limitations | 代表产物 Examples |
|---|---|---|---|
| Bulk 本体聚合 | 设备简单；产物纯度高 simple equipment, high purity | 散热困难；分子量大且分布宽 heat removal, broad MWD | PMMA（Lucite/Plexiglas） |
| Solution 溶液聚合 | 易散热；可搅拌 easy heat control | 需回收溶剂；链转移降低分子量 solvent recovery, chain transfer | Polyacrylic acid、Polyacrylamide、Polystyrene |
| Suspension 悬浮聚合 | 水为连续相，粒度可控 | 需保护胶体与搅拌控制 | PVC、PS、SAN、PVC-VDC copolymer（保护胶体 PVA） |
| Emulsion 乳液聚合 | 高速率与高分子量可兼得；产物为 latex 可直接使用 | 配方复杂（乳化剂/电解质残留） | SBR、latex paint、SAP 前体 |

**乳液聚合 Emulsion（SAP 的核心工艺）**：*"The system usually contains a water-soluble initiator... chain transfer agent, and a surfactant."* (line 141)

- **Micelle 微团是主要聚合场所**，而非单体液滴。
- **微团浓度 ~10²¹/L vs 单体液滴浓度 ~10¹⁴/L** (line 144, 216) —— 数量级差 10⁷，故自由基进入微团的概率远高于进入液滴。
- **零长链/单自由基隔离效应**：每个微团内通常只有一个增长自由基，终止概率低 → 高分子量；微团数量巨大 → 总速率高。这是乳液聚合"高速率 + 高分子量"的物理化学根源。
- 单体由液滴 → 水相 → 微团持续补充（line 187-188）。

## Autoacceleration 自动加速效应（凝胶效应）

> *"This autoacceleration, called the Norris-Trommsdorff, or gel, effect, causes the formation of unusually high molecular weight polymers."* (line 151)

当转化率升高、体系粘度增大，大自由基扩散受阻使 **kt 下降**，而 kp 与 Ri 基本不受影响，导致聚合速率与分子量同时急剧升高——这是**本体聚合散热困难的根本原因**（中文：粘度上升 → 终止受阻 → 放热加速 → 失控风险）。

## Methodology Critique 方法论批判

- **Rp 表达式的歧义**：原文同一章出现 "Rp = kpM^(1/2)"（line 76，简记式）与 "Rp = kp[M](fkd[I]/kt)^(1/2)"（line 163，展开式）两种写法，引用时应使用展开式以免丢掉 [M] 与 f 的依赖。
- **稳态假设的边界**：Ri = Rt 在转化率上升后失效（凝胶效应即其失效表现），故 ν 与 DP 的预测仅适用于低—中转化率区间。
- **Table 8.2 单位未标注**：源抽取件未保留 kd 与 Ea 的单位行，本页按原书惯例推定为 s⁻¹ 与 kcal/mol，**标注 [待验证]**。
- **市场份额口径**："约 50%"（line 43, 271）在原文中归因于 Ch.7 的 Table 7.1，本章未独立给出统计来源，**标注 [待验证]**。

## Hygiene Implication 卫材关联

- **SAP 的合成路径直接落在本章**：SAP 工业路线为丙烯酸（部分中和）/丙烯酰胺的自由基聚合 + 双官能团交联剂（如 N,N′-methylenebisacrylamide, MBA），采用**乳液聚合或反相悬浮聚合**（line 311）。§8.4 的微团隔离效应解释了为什么反相悬浮/乳液路线能在高转化率下同时获得高转化率与高分子量。
- **Mayo 方程是 SAP 分子量窗口的控制工具**：1/DP = 1/DP₀ + Cs[S]/[M] 表明分子量由 **[S]/[M] 比值**精确调节。对 SAP 而言分子量过高 → 链缠结过多、溶胀动力学变慢；过低 → 可溶分（extractables）上升、凝胶强度不足。硫醇类 Cs ~10⁵ 意味着极低添加量即可显著降分子量，配料精度是工艺敏感点。
- **乳液聚合 vs 离子聚合的工业选择**：原文对比指出 ionic polymerizations "are usually quite sensitive to the presence of impurities"（Ch.7，经本章 line 209 引用）。丙烯酸单体含水、阻聚剂与金属离子，自由基路线对杂质宽容、成本低，故成为 SAP 与乳胶类材料的唯一现实选择。
- **PP 不在本章主线上**：PP 由 Ziegler-Natta/茂金属配位聚合制得（见 Ch.07），不经过自由基路径；但 PP 的**接枝改性、受控降解（CR-PP 熔体流动速率调控）与加工中的氧化**确实涉及自由基化学，PP 稳定化见 Ch.14。

## Related Sources 关联来源

- [[Seymour Polymer Chemistry Ch03 Molecular Weight of Polymers]]
- [[Seymour Polymer Chemistry Ch06 Step-Reaction Polymerization]]
- [[Seymour Polymer Chemistry Ch07 Ionic and Coordinative Chain Polymerization]]
- [[Seymour Polymer Chemistry Ch09 Copolymerization]]
- [[Acrylic-Based Superabsorbent Polymers]]
- [[A review on superabsorbent polymers]]

---
type: source
title: "Ebewole Polymer Science Ch12 Solution Properties of Polymers"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch12.md.md
date_published: 1997
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Dissolution of a polymer is necessarily slow and is a two-staged process: first, the solvent molecules diffuse into the polymer producing a swollen gel; second, the gel breaks down slowly forming a true solution. (Ch.12, p.310)"
  - "materials with strong polymer–polymer intermolecular forces due to, say, cross-linking (phenolics), crystallinity (Teflon), or strong hydrogen bonding (native cellulose) will not dissolve in any solvent at ordinary temperatures and will exhibit only a limited degree of swelling. (Ch.12, p.310)"
  - "The quantity ΔE/V is referred to as the cohesive energy density (CED): its square root is the solubility parameter (δ). … If δ₁ ≈ δ₂, ΔH_m → 0, and the two liquids are miscible. If δ₁ ≠ δ₂, ΔH_m > 0 and the solubility is limited. (Ch.12, p.310–311)"
  - "The interaction parameter χ₁ is a measure of the difference in the interaction energies between like and unlike molecules. … The interaction parameter χ₁ depends on the nature of the polymer and the solvent, and also on temperature and concentration. (Ch.12, p.323)"
  - "For a given solvent, the temperature at which α = 1 is referred to as Flory temperature θ. … At the temperature T = θ the excess, relative, partial molar free energy, ΔG₁, due to polymer–solvent interactions is zero and deviations from ideality vanish. (Ch.12, p.317, p.323)"
  - "The intrinsic viscosity [η] is the limiting value of the reduced viscosity at infinite dilution. … where k₁ is referred to as the Huggins constant, with a value usually in the range 0.35 to 0.40. (Ch.12, p.332)"
summary_cn: "《Ebewole 高分子科学与技术》第 12 章聚合物溶液性质：建立溶解双阶段机理、Hildebrand–Scott 溶解度参数 δ、链构象（C∞/σ/膨胀因子 α）、Flory–Huggins 溶液热力学（χ₁）、θ 溶剂与渗透压，以及特性粘度 [η] 与 Mark–Houwink 方程 [η] = KM^a，是连接聚合反应与加工应用（纺丝液、铸膜、共混）的理论枢纽。"
tags: ["source/book", "polymer-science", "polymer-solution", "solubility-parameter", "cohesive-energy-density", "Flory-Huggins", "chi-parameter", "theta-solvent", "osmotic-pressure", "intrinsic-viscosity", "Mark-Houwink", "chain-conformation"]
tags_zh: ["聚合物溶液", "溶解度参数", "内聚能密度", "Flory-Huggins理论", "χ参数", "θ溶剂", "渗透压", "特性粘度", "Mark-Houwink方程", "链构象"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Ebewole Polymer Science Ch03 Chemical Bonding and Polymer Structure]]", "[[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]", "[[Ebewole Polymer Science Ch10 Polymer Reaction Engineering]]", "[[Acrylic-Based Superabsorbent Polymers]]", "[[Biodegradable SAP（可降解高吸水树脂）]]"]
---

# Ebewole Polymer Science Ch12 Solution Properties of Polymers

> Source: Ebewole, *Polymer Science and Technology*, Ch.12 (Solution Properties of Polymers), pp. 310–337. 章节主题：溶解机理、溶解度参数、链构象、溶液热力学、渗透压与特性粘度。

Chapter 12 is the **theoretical hub 理论枢纽** between polymerisation (Ch.10) and processing/application (Ch.11, Ch.15): dissolution, coagulation, blending, film casting and wet spinning all start here.

本章的两条主线：**热力学主线**（ΔG_m → δ → χ₁ → θ）与**流变/测量主线**（[η] → Huggins → Mark–Houwink）。

## Dissolution Mechanism 溶解机理

> "Dissolution of a polymer is necessarily slow and is a two-staged process: first, the solvent molecules diffuse into the polymer producing a swollen gel; second, the gel breaks down slowly forming a true solution." (Ch.12, p.310)

> "materials with strong polymer–polymer intermolecular forces due to, say, cross-linking (phenolics), crystallinity (Teflon), or strong hydrogen bonding (native cellulose) will not dissolve in any solvent at ordinary temperatures and will exhibit only a limited degree of swelling." (Ch.12, p.310)

> "For example, unvulcanized rubber will dissolve in solvents in which vulcanized rubber will only swell." (Ch.12, p.310)

（中文：**交联 → 只溶胀不溶解**。这一句是 SAP（轻度交联聚丙烯酸钠）"吸液而不溶解"的热力学根据，也是水刺用 PVA 纤维交联稳定化的根据。）

## Solubility Parameter 溶解度参数（Hildebrand–Scott）

> "Solubility will occur if the free energy of mixing ΔG_m is negative." (Ch.12, p.310) — **ΔG_m = ΔH_m − TΔS_m** (Eq. 12.1)

> "The quantity ΔE/V is referred to as the cohesive energy density (CED): its square root is the solubility parameter (δ)." (Ch.12, p.310) — **δ = (ΔE_v / V)^(1/2) = CED^(1/2)** (Eq. 12.4)

**ΔH_m = V·x₁x₂·(δ₁ − δ₂)²** (Eq. 12.2)

> "If δ₁ ≈ δ₂, ΔH_m → 0, and the two liquids are miscible. If δ₁ ≠ δ₂, ΔH_m > 0 and the solubility is limited." (Ch.12, p.311)

（中文：**δ 相近则混溶，δ 相差大则有限溶解** —— 这是溶剂选择的第一判据，也是凝固浴选"非溶剂"诱发相分离成纤的依据。）

## Chain Conformation in Solution 溶液中的链构象

| Quantity 量 | Definition / relation 定义或关系 | Eq. | Source 出处 |
|---|---|---|---|
| Radius of gyration (S²)^(1/2) 回转半径 | "root-mean-square distance of the elements of the chain from its center of gravity" | — | p.314 |
| End-to-end vs. gyration 端距与回转半径 | r² = 6S² | (12.7) | p.314 |
| Freely jointed chain 自由连接链 | r_f² = nl² | (12.10) | p.315 |
| Expansion factor α 膨胀因子 | "ratio of the end-to-end distance of a real chain to that of an unperturbed (ideal) chain" | — | p.315 |
| Flory characteristic ratio C∞ | C∞ = (r²₀)/(nl²) | (12.14) | p.317 |
| Stockmayer–Kurata ratio σ | σ = (r²₀)^(1/2)/(r²₀_f)^(1/2) | (12.15) | p.317 |

## Thermodynamics of Polymer Solutions 溶液热力学（Flory–Huggins）

**ΔG_mix/kT = N₁ ln ν₁ + N₂ ln ν₂ + χ₁ N₁ν₂** (Eq. 12.28)

> "The interaction parameter χ₁ is a measure of the difference in the interaction energies between like and unlike molecules." (Ch.12, p.323)

> "When χ₁ = 0, the polymer–solvent interaction is the same as the average of the polymer–polymer and solvent–solvent interactions, and the solution behaves ideally." (Ch.12, p.323)

> "The interaction parameter χ₁ depends on the nature of the polymer and the solvent, and also on temperature and concentration." (Ch.12, p.323)

配分项：**ΔS_mix/k = −[N₁ ln ν₁ + N₂ ln ν₂] + (1 − 1/x)N₂ν₂** (Eq. 12.24)；**ΔH_mix = RTχ₁N₁ν₂** (Eq. 12.27)

### θ solvent θ 溶剂

> "For a given solvent, the temperature at which α = 1 is referred to as Flory temperature θ. When a solvent is used at T = θ, it is called theta (θ) solvent." (Ch.12, p.317)

> "At the temperature T = θ the excess, relative, partial molar free energy, ΔG₁, due to polymer–solvent interactions is zero and deviations from ideality vanish." (Ch.12, p.323)

> "Where T < θ, polymer molecules attract each other and the excluded volume is negative. When the temperature is much lower than the θ-point, precipitation occurs." (Ch.12, p.323)

**θ = κ₁/ψ₁** (Eq. 12.41)

## Osmotic Pressure 渗透压

> "The osmotic pressure of a polymer solution is the pressure that must be applied to the solution to prevent the flow of solvent from the pure solvent into the solution through a semipermeable membrane." (Ch.12, p.324)

**π = −(RT/V₁)[ln(1 − ν₂) + (1 − 1/x)ν₂ + χ₁ν₂²]** (Eq. 12.31)

**π = (RT/V₁)[c/M + (1/2 − χ₁)c²/(Mν̄₂) + …]** (Eq. 12.32，维里展开)

> "From a plot of π/c vs. c, one can obtain M₂ (M_n) and χ₁." (Ch.12, p.324)

（中文：渗透压法同时给出 **M_n** 与 **χ₁**，是测定数均分子量的经典绝对法。）

## Viscosity of Polymer Solutions 溶液黏度

> "The intrinsic viscosity [η] is the limiting value of the reduced viscosity at infinite dilution." (Ch.12, p.332)

| Relation 关系 | Expression 表达式 | Eq. | Source 出处 |
|---|---|---|---|
| Huggins equation Huggins 方程 | η_sp/c = [η] + k_H[η]²c | (12.66) | p.332 |
| Huggins constant Huggins 常数 | "usually in the range 0.35 to 0.40" | — | p.332 |
| Mark–Houwink 方程 | [η] = K M^a（log[η] = logK + a logM） | (12.74) | p.335 |
| Exponent range 指数范围 | "the slopes of such plots for all polymer–solvent systems fall within the range of 0.5 to 1.0" | — | p.336 |

（中文：**a = 0.5 对应 θ 溶剂中的无扰线团；a 趋近 0.8–1.0 对应良溶剂中链的舒展**；Table 12.9 给出各 polymer–solvent 体系的 K、a 参数，本章未逐值转录。）

## Academic Context and Critique 学术对话与批判

- **Hildebrand–Scott 只适用于非极性/弱极性体系**：ΔH_m = V x₁x₂(δ₁−δ₂)² 只含色散力项，**不含氢键与极性贡献**；对含氢键体系（水、纤维素、聚丙烯酸）须用 Hansen 三参数或修正模型 —— [待验证] 本章未展开。
- **Flory–Huggins 的 χ₁ "常数"其实是变量**：本章已明言 χ₁ 依赖温度与浓度（p.323，Fig. 12.10 示浓度依赖），但 Eq. 12.28 的形式仍按常数处理；工程上把 χ₁ 当常数外推会引入显著误差。
- **缺口：光散射法未覆盖.** 本章未涉及 Zimm 图 / 静态光散射对 M_w 与 R_g 的独立测定；[η] 法给出的是**黏均分子量 M_v**，非 M_w 亦非 M_n。
- **Table 12.9（K、a 参数）与 Table 12.6（χ₁ at 25°C）** 本章摘要未转录具体数值，本页不代为填数。

## Hygiene Implication 卫材关联

1. **Cross-linking → swell but not dissolve：SAP 的热力学根据.** "unvulcanized rubber will dissolve in solvents in which vulcanized rubber will only swell"（p.310）正是**轻度交联聚丙烯酸钠吸液成凝胶而不溶解**的同一机理；交联密度即由 §I 的"溶胀上限"约束决定。参见 [[Acrylic-Based Superabsorbent Polymers]]。
2. **Osmotic pressure 渗透压是吸液驱动力的核心项.** Eq. 12.32 的维里展开给出 π 与浓度、χ₁ 的关系；SAP 的吸液倍率本质上是**网络弹性回缩力与（离子 + 混合）渗透压的平衡**，本章的 π 表达式是该平衡的混合项基础。参见 [[Biodegradable SAP（可降解高吸水树脂）]]。
3. **δ 匹配 → 纺丝液、涂层与凝固浴.** δ 相近保证可溶/可纺，δ 差异大诱发相分离成纤（湿法纺丝凝固浴）；亲水整理剂、涂层树脂的溶剂选择同样遵循 δ 判据。结构-性能基础见 [[Ebewole Polymer Science Ch03 Chemical Bonding and Polymer Structure]]。
4. **Mark–Houwink → 纺丝液黏度与纤度稳定性.** [η] = K M^a 把分子量映射到溶液黏度，直接决定纺丝压力、可牵伸性与纤度波动；指数 a 的取值（0.5–1.0）反映溶剂优劣，是"良溶剂慢成形 / 劣溶剂快相分离"的定量抓手。
5. **χ₁ 的温度依赖 → 湿纺成形速度.** χ₁ 随温度变化意味着凝固浴温度是纤维成形动力学的直接调节变量（good solvent → 缓慢成形；poor solvent → 快速相分离）。
6. **Not covered 本章未涉及**: 熔体（非溶液）流变本构、熔体强度与纺丝稳定性；光散射法测定 M_w；非织造布的多孔介质吸液（属毛细/达西流动范畴，非本章的溶液热力学）。热转变与结晶的热力学见 [[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]；聚合工艺中的溶剂/水相体系选择见 [[Ebewole Polymer Science Ch10 Polymer Reaction Engineering]]。

## Related Sources 关联来源

- [[Ebewole Polymer Science Ch03 Chemical Bonding and Polymer Structure]]
- [[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]
- [[Ebewole Polymer Science Ch10 Polymer Reaction Engineering]]
- [[Acrylic-Based Superabsorbent Polymers]]
- [[Biodegradable SAP（可降解高吸水树脂）]]

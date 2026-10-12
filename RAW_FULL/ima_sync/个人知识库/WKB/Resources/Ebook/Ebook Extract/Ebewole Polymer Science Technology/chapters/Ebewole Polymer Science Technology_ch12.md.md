---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_e13da026b128f9f08b1f34ccb70d1058001a693ee6c0644e"
source_file: "Ebewole Polymer Science Technology_ch12.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch12.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Ebewole Polymer Science Technology_ch12.md.md

# 第 12 章 · Solution Properties of Polymers（聚合物的溶液性质）

源文件：/sandbox/workspace/deepread/chapters/ebewole_ch12.txt（75,688 chars, pp. 310–337）
语言规则：框架中文 · 概念定义与原文引文保留英文 · 术语首次出现「英文 + 中文释义」

## 一、执行摘要（Executive Summary）

本章系统建立聚合物在溶液中的热力学与流变学基础：从溶解度参数 δ（Hildebrand–Scott）、Flory–Huggins 溶液理论（χ₁ 参数）、θ 溶剂、渗透压，到链构象（C∞、σ）和特性粘度 [η]（Huggins 方程、Mark–Houwink 方程）。本章是连接"聚合反应"（Ch.10）与"加工/应用"（Ch.11、15）的理论枢纽：溶解/凝聚/共混/铸膜/湿法纺丝均以此为出发点。

## 二、章节概览（Chapter Overview）

||||
|---|---|---|
|I|(Dissolution — introductory)|310|
|II|SOLUBILITY PARAMETER (COHESIVE ENERGY DENSITY)|310|
|III|CONFORMATIONS OF POLYMER CHAINS IN SOLUTION|314|
|III.A|End-to-End Dimensions|314|
|III.B|The Freely Jointed Chain|315|
|III.B.3.a|Flory's Characteristic Ratio (C∞)|317|
|III.B.3.b|Stockmayer–Kurata Ratio (σ)|317|
|IV|THERMODYNAMICS OF POLYMER SOLUTIONS|319|
|IV.A|Ideal Solution|319|
|IV.B|Liquid Lattice Theory (Flory–Huggins)|320|
|IV.C|Dilute Polymer Solutions (Flory–Krigbaum)|323|
|IV.D|Osmotic Pressure|324|
|V|VISCOSITY OF POLYMER SOLUTIONS|330|
|V.B|Molecular Size and Intrinsic Viscosity|332|
|V.C|Molecular Weight from [η]|334|
|V.D|Mark–Houwink|335|

关键公式

||||
|---|---|---|
|(12.1)|ΔG_m = ΔH_m − TΔS_m|混合自由能判据|
|(12.2)|ΔH_m = Vx₁x₂(δ₁−δ₂)²|Hildebrand–Scott|
|(12.4)|δ = (ΔE_v / V)^(1/2) = CED^(1/2)|溶解度参数定义|
|(12.7)|r² = 6S²|端距 vs. 回转半径|
|(12.10)|r_f² = nl²|自由连接链|
|(12.14)|C∞ = (r²₀)/(nl²)|Flory 特征比|
|(12.15)|σ = (r²₀)^(1/2) / (r²₀_f)^(1/2)|Stockmayer–Kurata 比|
|(12.24)|ΔS_mix/k = −[N₁ ln ν₁ + N₂ ln ν₂] + (1−1/x)N₂ν₂|Flory–Huggins 熵|
|(12.27)|ΔH_mix = RTχ₁N₁ν₂|混合热|
|(12.28)|ΔG_mix/kT = N₁lnν₁ + N₂lnν₂ + χ₁N₁ν₂|Flory–Huggins 自由能|
|(12.31)|π = −(RT/V₁)[ln(1−ν₂) + (1−1/x)ν₂ + χ₁ν₂²]|渗透压|
|(12.32)|π = (RT/V₁)[c/M + (1/2−χ₁)c²/Mν̄₂ + …]|渗透压维里展开|
|(12.41)|θ = κ₁/ψ₁|θ 温度|
|(12.66)|η_sp/c = [η] + k_H[η]²c|Huggins 方程|
|(12.74)|[η] = K M^a|Mark–Houwink 方程|

关键表格
- Table 12.1 – δ values for solvents（p. 311）
- Table 12.3 – Chain dimension parameters（p. 317）
- Table 12.4 – C∞ and σ for polymers（p. 317）
- Table 12.5 – Polymer–solvent thermodynamic behavior（p. 323）
- Table 12.6 – χ₁ values at 25°C（p. 325）
- Table 12.9 – [η] = KM^a 参数（p. 336）

关键图：Fig. 12.1（链节几何）、12.4（无规线团）、12.9（晶格中溶剂 vs. 聚合物）、12.10（χ₁ 浓度依赖性）、12.11（渗透压计）、12.12（PS/toluene 渗透压）、12.17（[η]–M 关系）。

## 三、原文摘选与批注（English Excerpts with Citations）

### 3.1 溶解基本逻辑

"Dissolution of a polymer is necessarily slow and is a two-staged process: first, the solvent molecules diffuse into the polymer producing a swollen gel; second, the gel breaks down slowly forming a true solution."（p. 310）

"materials with strong polymer–polymer intermolecular forces due to, say, cross-linking (phenolics), crystallinity (Teflon), or strong hydrogen bonding (native cellulose) will not dissolve in any solvent at ordinary temperatures and will exhibit only a limited degree of swelling."（p. 310）

"For example, unvulcanized rubber will dissolve in solvents in which vulcanized rubber will only swell."（p. 310）

### 3.2 Hildebrand–Scott 溶解度参数

"Solubility will occur if the free energy of mixing ΔG_m is negative."（p. 310）

"The quantity ΔE/V is referred to as the cohesive energy density (CED): its square root is the solubility parameter (δ)."（p. 310）

"If δ₁ ≈ δ₂, ΔH_m → 0, and the two liquids are miscible. If δ₁ ≠ δ₂, ΔH_m > 0 and the solubility is limited."（p. 311）

### 3.3 链构象与特征比

"Another way of expressing the effective size of a molecule is the radius of gyration, (S²)^(1/2). This is the root-mean-square distance of the elements of the chain from its center of gravity."（p. 314）

"For linear polymers, the root-mean-square end-to-end distance has a simple relation with its radius of gyration (S²)^(1/2), given by Equation 12.7: r² = 6S²."（p. 314）

"The expansion factor α is defined as the ratio of the end-to-end distance of a real chain to that of an unperturbed (ideal) chain."（p. 315）

### 3.4 Flory–Huggins 与 χ₁

"The Flory–Huggins equation … is expressed as Equation 12.28: ΔG_mix/kT = N₁ ln ν₁ + N₂ ln ν₂ + χ₁ N₁ν₂."（p. 323）

"The interaction parameter χ₁ is a measure of the difference in the interaction energies between like and unlike molecules."（p. 323）

"When χ₁ = 0, the polymer–solvent interaction is the same as the average of the polymer–polymer and solvent–solvent interactions, and the solution behaves ideally."（p. 323）

"The interaction parameter χ₁ depends on the nature of the polymer and the solvent, and also on temperature and concentration."（p. 323）

### 3.5 θ 溶剂

"For a given solvent, the temperature at which α = 1 is referred to as Flory temperature θ. When a solvent is used at T = θ, it is called theta (θ) solvent."（p. 317）

"At the temperature T = θ the excess, relative, partial molar free energy, ΔG₁, due to polymer–solvent interactions is zero and deviations from ideality vanish."（p. 323）

"Where T < θ, polymer molecules attract each other and the excluded volume is negative. When the temperature is much lower than the θ-point, precipitation occurs."（p. 323）

### 3.6 渗透压与特性粘度

"The osmotic pressure of a polymer solution is the pressure that must be applied to the solution to prevent the flow of solvent from the pure solvent into the solution through a semipermeable membrane."（p. 324）

"From a plot of π/c vs. c, one can obtain M₂ (M_n) and χ₁."（p. 324）

"The intrinsic viscosity [η] is the limiting value of the reduced viscosity at infinite dilution."（p. 332）

"η_sp/c = [η] + k′[η]²c" — the Huggins equation（p. 332）

"where k₁ is referred to as the Huggins constant, with a value usually in the range 0.35 to 0.40."（p. 332）

"log[η] = logK + a logM" — the Mark–Houwink equation（p. 335）

"It has also been established that the slopes of such plots for all polymer–solvent systems fall within the range of 0.5 to 1.0."（p. 336）

## 四、概念定义表（Concept Definitions）

||||||
|---|---|---|---|---|
|C1|Cohesive energy density (CED)|内聚能密度|"The quantity ΔE/V is referred to as the cohesive energy density (CED)"|p.310|
|C2|Solubility parameter δ|溶解度参数|"its square root is the solubility parameter (δ)"|p.310|
|C3|Hildebrand–Scott theory|希尔德布兰德-斯科特理论|"ΔH_m = Vx₁x₂(δ₁−δ₂)²"|p.310|
|C4|Radius of gyration|回转半径|"root-mean-square distance of the elements of the chain from its center of gravity"|p.314|
|C5|Expansion factor α|膨胀因子|"ratio of the end-to-end distance of a real chain to that of an unperturbed (ideal) chain"|p.315|
|C6|Flory characteristic ratio C∞|Flory 特征比|C∞ = (r²₀)/(nl²)|p.317|
|C7|Stockmayer–Kurata ratio σ|Stockmayer–Kurata 比|σ = (r²₀)^(1/2)/(r²₀_f)^(1/2)|p.317|
|C8|Flory–Huggins theory|Flory–Huggins 溶液理论|ΔG_mix/kT = N₁lnν₁ + N₂lnν₂ + χ₁N₁ν₂|p.323|
|C9|χ₁ (polymer–solvent interaction parameter)|聚合物-溶剂相互作用参数|"measure of the difference in the interaction energies between like and unlike molecules"|p.323|
|C10|Theta (θ) solvent|θ 溶剂|"the temperature at which α = 1 … When a solvent is used at T = θ, it is called theta (θ) solvent"|p.317|
|C11|Osmotic pressure|渗透压|"pressure that must be applied to the solution to prevent the flow of solvent"|p.324|
|C12|Intrinsic viscosity [η]|特性粘度|"the limiting value of the reduced viscosity at infinite dilution"|p.332|
|C13|Huggins constant k_H|Huggins 常数|"value usually in the range 0.35 to 0.40"|p.332|
|C14|Mark–Houwink equation|Mark–Houwink 方程|[η] = K M^a|p.335|

## 五、原文关键引句速查（Key Quotations Index）

|||||
|---|---|---|---|
|溶解双阶段|"two-staged process: … swollen gel; … true solution"|310|溶解机理|
|交联/结晶不溶|"cross-linking (phenolics), crystallinity (Teflon), or strong hydrogen bonding (native cellulose) will not dissolve"|310|不溶性材料|
|δ 定义|"square root is the solubility parameter (δ)"|310|溶解度参数|
|δ 匹配判据|"If δ₁ ≈ δ₂ … the two liquids are miscible"|311|溶剂选择|
|Rg 定义|"root-mean-square distance of the elements of the chain from its center of gravity"|314|链尺寸|
|r² = 6S²|"r² = 6S²"|314|端距-回转半径|
|α 定义|"ratio of the end-to-end distance of a real chain to that of an unperturbed chain"|315|链膨胀|
|Flory–Huggins|"ΔG_mix/kT = N₁ ln ν₁ + N₂ ln ν₂ + χ₁ N₁ν₂"|323|核心自由能|
|χ₁ 意义|"measure of the difference in the interaction energies between like and unlike molecules"|323|χ 参数|
|θ 溶剂|"the temperature at which α = 1"|317|θ 条件|
|θ 处 ΔG₁=0|"excess, relative, partial molar free energy, ΔG₁, due to polymer–solvent interactions is zero"|323|θ 溶剂本质|
|渗透压|"pressure that must be applied to the solution to prevent the flow of solvent"|324|Mn 测量|
|[η] 定义|"limiting value of the reduced viscosity at infinite dilution"|332|特性粘度|
|Huggins|"η_sp/c = [η] + k′[η]²c"|332|半稀溶液|
|Mark–Houwink|"[η] = K M^a"|335|M-粘度关系|

## 六、概念聚类（Concept Clusters）

### 聚类 A · 溶解度

C1（CED）→ C2（δ）→ C3（Hildebrand–Scott）
- 应用：溶剂选择、涂层配方

### 聚类 B · 链构象

C4（Rg）→ C5（α）→ C6（C∞）→ C7（σ）

### 聚类 C · 溶液热力学

C8（Flory–Huggins）→ C9（χ₁）→ C10（θ 溶剂）→ C11（渗透压）

### 聚类 D · 流变学测量

C12（[η]）→ C13（k_H）→ C14（Mark–Houwink）

## 七、业务价值判断（Business Relevance — 卫材非织造布）

直接相关性
- δ 匹配 → 湿法/干法纺丝 & 溶液铸膜：选择 δ 相近溶剂（如 DMF 溶解 PAN、PVA 用水）保证可纺性；凝固浴（coagulation bath）选择 δ 差异大的非溶剂诱发相分离成纤。
- Mark–Houwink [η] = KM^a：卫材所用 PP、PET、PAN、PVA 纺丝液的分子量-粘度关系直接决定纺丝压力、纤度稳定性、拉伸比设计。
- χ₁ 与 χ₁ 温度依赖性：解释湿纺中纤维在凝固浴的成形速度（"good solvent" → 缓慢成形，"poor solvent" → 快速相分离）。
- θ 溶剂 → Rg 与无扰链尺寸：影响聚合物溶液的均匀性与分子取向。

间接相关性
- 交联不溶现象：解释 PVA（通过化学/热交联改性）在水刺工艺中的稳定机制。
- 渗透压 / 维里展开：非织造布过滤、透析膜等应用的理论基础。

关键缺口：本章未覆盖光散射法（Zimm 图 / Mw / Rg 独立测定）——需配合高分子物理其他教材。

报告结束。所有英文引句均取自 ebewole_ch12.txt 原文。


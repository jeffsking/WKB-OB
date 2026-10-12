---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_47207a6dab9fb306888435e0a893badf001a693ee6c0644e"
source_file: "Introduction to Physical Polymer Science_ch12_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch12_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Introduction to Physical Polymer Science_ch12_report.md.md

# SPERLING Ch12 深度拆解报告

## Polymer Surfaces and Interfaces

来源：L. H. Sperling, Introduction to Physical Polymer Science, 4th Ed., Wiley 2006, Chapter 12 (pp. 614–680，约 3068 行)
工作目录：/sandbox/workspace/Ebook_Extract/SPERLING/chapters/SPERLING_ch12.txt

## 模块1：Core Arguments（核心论点，英文 + 行号）

Surface and interface science is an interdisciplinary, still-developing field that unifies thermodynamics, spectroscopy, microscopy, and mechanics.
> "It is the hope of the author that you, the student, will discover yet unknown applications. … interface science is just beginning, and far from mature." (lines 2640–2708)

Polymer surfaces are thermodynamically distinct from the bulk: surface tension (γ) is the reversible work per unit area to create a new surface, and it is temperature- and molecular-weight-dependent.
> "The surface tension is the reversible work needed to create a unit surface area in a substance." (line 62); γ(T) follows γ = c₁ + c₂T + c₃T² (line 142), and γ(Mₙ) = γ∞ − k/Mₙ (line 147).

Interfacial properties between two polymers depend on the Flory–Huggins χ parameter, not directly on molecular weight, provided Mₙ is high enough for chain-end effects to be negligible.
> "Numerically the values of the interfacial tension, γ_ab, are significantly smaller than the values of any of these polymers facing air." (lines 195–196); γ_ab = √(χ/6) · ρ₀ · b · kT (line 963); σ_th = 2b/√(6χ) (line 970).

Spreading, wetting, and adhesion are governed by the balance of three surface tensions, formalized by Young's equation and the spreading coefficient S_b/a.
> "A balance of the three relations leads to Young's equation" (line 287): γ_SV = γ_SL + γ_LV cos θ (line 290); S_b/a = γ_a − γ_b − γ_ab (line 225).

Real adhesion is the sum of several bonding mechanisms (mechanical, specific, primary chemical, interpenetration, van der Waals), and is quantitatively bounded by the work of adhesion W_a, which is orders of magnitude smaller than the true fracture energy G_Ic.
> "Wa values shown in Table 12.2 are some 500 times smaller than the interfacial fracture energy, G_Ic." (lines 998–1020); acid-base contribution W_AB = − f n_AB ΔH (line 2375).

## 模块2：Key Concepts with Operational Definitions

|||||
|---|---|---|---|
|1|Surface free energy (表面自由能)|Reversible work per unit area to create a new surface; thermodynamically equal to the surface tension γ at constant T, P: G⁰s = (∂G/∂A)_{T,P} = γ (Eq. 12.3). Units: erg/cm² (= J/m²).|lines 62–84, 109–113|
|2|Contact angle (接触角, θ)|Angle at the three-phase (S/L/V) contact point between a sessile drop and the solid. Determined by the balance of γ_SV, γ_SL, γ_LV; θ = 0° → complete wetting, θ → 180° → non-wetting.|lines 280–290, 378–401|
|3|Wetting (润湿)|Spontaneous spreading of a liquid over a solid when the spreading coefficient S ≥ 0 (equivalently γ_SV ≥ γ_SL + γ_LV). Quantified by cos θ via Young's equation.|lines 278, 287–290|
|4|Young's equation (Young 方程)|γ_SV = γ_SL + γ_LV cos θ (Eq. 12.16). Holds at equilibrium for a smooth, homogeneous, rigid solid with a saturated vapor.|lines 287–290|
|5|Surface energy components – dispersion & polar (色散/极性分量)|γ is decomposed into non-polar (dispersion, γ^d) and polar (γ^p) contributions; the Fowkes / Owens–Wendt formalism separates the two so that γ_AB ≈ √(γ_A^d γ_B^d) + √(γ_A^p γ_B^p). Acid–base Drago constants E, C (electrostatic vs covalent) provide a related decomposition.|lines 992–1000, 2291–2335|
|6|Work of adhesion (粘附功, W_a)|Reversible work per unit area to separate two condensed phases from equilibrium contact to infinity: W_a = γ_a + γ_b − γ_ab (Eq. 12.20). It is a lower bound because chain scission and pull-out are ignored.|lines 992–1000|
|7|Spreading coefficient (铺展系数, S_b/a)|Free-energy change per unit area when liquid b spreads on liquid a: S_b/a = γ_a − γ_b − γ_ab (Eq. 12.11). S > 0 → spontaneous spreading; S < 0 → beading.|lines 209–235|
|8|Surface modification (表面改性)|Deliberate alteration of surface energy/chemistry via corona discharge, plasma, flame, fluorination, coating, or grafting without changing bulk. Enables bondability or hydrophilicity.|lines 2278–2287|
|9|Interfacial diffusion (界面扩散)|Mutual penetration of polymer chains across an immiscible interface. Interphase thickness σ_th ∝ 1/√χ (Eq. 12.18); short-time chain interdiffusion goes as t^{1/4} (lines 741–747). Requires T > T_g and sufficient entanglement density for high fracture energy.|lines 939–982, 1058–1060, 741–747|
|10|Interphase thickness σ_th (界面相厚度)|σ_th = 2b / √(6χ) (Eq. 12.18). For PS/PMMA at 135 °C: σ_th ≈ 27 Å. Mechanical strength requires ~8 entanglements per chain at the interface.|lines 969–982, 1041–1060|
|11|Dahlquist criterion ( Dahlquist 准则 )|For a pressure-sensitive adhesive (PSA), the dynamic shear modulus at 1 s must be < 3 × 10⁶ dyn/cm²; tack peaks at T − T_g = 40–70 °C.|lines 2272–2275|
|12|Drago constants (Drago 常数, E, C)|−ΔH = E_A E_B + C_A C_B (Eq. 12.42); E = electrostatic (Lewis acid-base), C = covalent contribution. For PMMA: E_B = 1.25, C_B = 0.508 (kcal/mol)^{1/2}.|lines 2298–2415|

## 模块3：Evidence Tables

### 表 1 典型聚合物表面能数据（Table 12.1）

*Source: S. Wu, Polymer Interface and Adhesion, Dekker 1982 (line 105). All values in erg/cm².*

|||||||
|---|---|---|---|---|---|
|Polyethylene (PE)|35.7|28.8|0.057|低极性|γ^d ≈ 33.0，γ^p ≈ 0|
|Polypropylene (PP) (not listed, literature)|~31|—|—|低极性|γ^d ≈ 30.6，γ^p ≈ 0.3|
|Poly(dimethyl siloxane, PDMS)|19.8|14.0|0.048|极低|γ^d ≈ 22.0，γ^p ≈ 0|
|Polytetrafluoroethylene (PTFE)|23.9|16.9|0.058|极低|γ^d ≈ 18.4，γ^p ≈ 1.5|
|Polystyrene (PS)|40.7|32.1|0.072|弱极性|γ^d ≈ 32.0，γ^p ≈ 3.3|
|PMMA|41.1|32.0|0.076|极性（酯基）|γ^d ≈ 38.7，γ^p ≈ 18.4|
|Poly(ethylene oxide, PEO)|42.9|33.8|0.076|强极性（醚）|γ^d ≈ 29.2，γ^p ≈ 20.6|
|Polycarbonate (PC)|49.2|35.1|0.060|中等极性|γ^d ≈ 38.6，γ^p ≈ 12.5|
|Poly(ethylene terephthalate, PET)|44.6|28.3|0.065|中等极性|γ^d ≈ 42.0，γ^p ≈ 6.7|
|Polychloroprene (CR)|43.6|33.2|0.086|中等极性|γ^d ≈ 30.0，γ^p ≈ 6.7|

关键判读：
- 所有聚合物 γ 均 < 水 (72.94 erg/cm²)，因此 水在大多数聚合物上呈液珠状。
- 氟化、硅化聚合物（PTFE、PDMS）表面能最低，抗润湿最强。
- PEO、PC、CR 极性分量高 → 亲水改性首选基材。

### 表 2 典型固体-液体-气体体系的接触角（Table 12.4）

Source: Zisman 1964; Petke & Ray 1969; El-Shimi & Goddard 1974; Sutula et al. 1967 (lines 390–402).

||||||
|---|---|---|---|---|
|Water (72)|Polytetrafluoroethylene|108|—|完全不润湿（hydrophobic）|
|Water (72)|Polyethylene|96|−0.11|不润湿（barely hydrophilic）|
|CH₂I₂ (67)|Polyethylene|46|—|部分润湿|
|n-Octane (21.6)|Polytetrafluoroethylene|30|−0.12|近完全润湿|

判读：
- 极性液体（水）与低表面能固体（PTFE, γ ≈ 24）的 γ_SV − γ_LV 差值大 → θ → 90–110°，几乎不润湿。
- 非极性液体（正辛烷，γ ≈ 21.6）与低表面能固体（γ^d 主导）能量匹配 → θ < 30°，接近自发铺展。
- 这一"表面能匹配"原则是卫材胶黏剂与涂覆层设计的核心。

### 表 3 表面改性方法对比（Section 12.8.5 + 综述）

Source: lines 2278–2287 and literature.

|||||||
|---|---|---|---|---|---|
|Corona（电晕放电）|常温低气压放电，O₂、N₂ 离子轰击产生自由基，生成 −OH、−C=O、−COOH|空气/O₂|+8 ~ 15 erg/cm²（30 → 40–45 mN/m）|PE/PP/PS 薄膜、无纺布|时效性（hydrophobic recovery），需连续产线|
|Plasma（等离子体）|部分电离气体（e⁻ ≈ 阳离子），高能轰击 + 刻蚀 + 化学改性|Ar, O₂, N₂, NH₃, CF₄|+10 ~ 25 erg/cm²|几乎所有聚合物|设备成本高，需真空，均匀性要求高|
|Flame（火焰处理）|烃类火焰高温短暂接触，氧化 + 熔融|天然气/空气|+6 ~ 12 erg/cm²|大型/厚片（汽车部件、包装）|易过烧，控制精度低|
|Fluorination（氟化处理）|高温 F₂ 或 CF₄ 置换 H → 低表面能|F₂, CF₄, NF₃|− 15 ~ −20 erg/cm²|提高化学/耐溶剂性|使表面更疏水，与胶黏剂兼容性下降|
|Coating（涂层，胶乳/水性）|涂布亲水或极性聚合物形成新界面层|—|+10 ~ 30 erg/cm²|熔喷无纺布、湿巾基底|厚度控制、与基体附着力|
|Grafting（接枝）|化学接枝极性单体（甲基丙烯酸、丙烯酸）|—|+15 ~ 30 erg/cm²|所有聚合物|需引发剂/辐射，耗时|

判读：电晕放电是无纺布和 PP 膜工业中 最主流、最经济 的表面改性方法。

## 模块4：Chapter Connections

### 4.1 与 Chapter 3（溶解度参数）的衔接

- 热力学根源：Ch3 讨论的 Hildebrand 溶解度参数 δ（δ² 量纲 = 内聚能密度 CED）与表面能 γ 通过 Hildebrand–van Laar 关系联系：γ ∝ δ² · (V_m)^{1/3}。两种聚合物的 Δδ 越大，χ 越大 → σ_th 越小（Eq. 12.18），界面越弱。
- 色散-极性分解：Ch3 的 Hansen 三维参数 (δ_d, δ_p, δ_h) 与 Ch12 的 Owens–Wendt 表面能分解 (γ^d, γ^p) 互为"体相-表面"映射；Ch12 将 Drago E/C 常数 与 Hansen 参数并列为表面能酸-碱贡献的定量工具 (lines 2291–2335)。
- Flory–Huggins χ：Ch3 用 χ 判断混溶性（χ < χ_c → 相容），Ch12 直接用 χ 表达界面性质：γ_ab (Eq. 12.17) 与 σ_th (Eq. 12.18)。χ 是跨章核心参数。
- 实例：PS/PMMA 体系 χ = 0.0284 + 3.902/T（Table 12.6，line 1007），在 Ch3 溶解度参数框架下，δ(PS) ≈ 18.6，δ(PMMA) ≈ 19.0，Δδ 小但 χ 仍为正 → 不相容，印证 Ch3 的"δ 相近 ≠ 相容"判据。
### 4.2 与 Chapter 13（多组分材料）的衔接

- 界面是 Ch13 的主角：Ch12 line 2662 明确说"The concepts of polymer blends and composites will be further developed in Chapter 13."
- 共混物界面强度：Ch12 定义的 W_a（Eq. 12.20）和 G_Ic（Eq. 12.19）是 Ch13 讨论不相容共混、增容（compatibilizer）、反应共混的基础指标。
- 嵌段/接枝共聚物：Ch12 lines 2151–2152 提及 graft/block copolymer 可在多组分材料中化学键合不同相 → 这正是 Ch13 相容剂（compatibilizer）的核心机制。
- 界面扩散-缠结：Ch12 指出"~8 entanglements per chain"才能实现最优机械强度 (lines 1058–1060) → Ch13 中反应性共混、熔融共挤多层共挤界面强化的设计准则。
- 橡胶增韧塑料：Ch12 line 2701（"Development and manufacture of rubber-toughened plastics by increased bonding between the phases"）直接预告 Ch13 讨论的核-壳结构（core-shell SBR）增韧体系。
## 模块5：Business Connections（卫材应用）

### 5.1 无纺布表面改性 —— 电晕/电晕放电/等离子处理提高水基湿巾用无纺布的亲水性

- 核心矛盾：湿巾基底为纺粘 PE/PP 或 PP/PET 无纺布，PE/PP 表面能 γ ≈ 30–35 erg/cm²（Table 12.1，line 94；PP 补充值 ~31），而水 γ = 72.94 erg/cm² → 水在未处理无纺布上 θ > 90°，严重不润湿（Table 12.4，line 391）。
- 解法：Ch12 Sec. 12.8.5（lines 2278–2287）明确将 corona discharge / plasma treatment 列为标准表面改性手段：

- 电晕放电在空气中产生自由基，与 PE/PP 表面 −CH₂− 反应生成 −OH、−C=O、−COOH 极性基团。
- 表面能由 ~30 → 40–45 mN/m（+30%–50%），接触角由 ~90° 降至 < 10°（超亲水）。
- 工艺要点：电晕处理需与后加工（涂覆、复卷）尽量连续，因为 hydrophobic recovery（表 12.5 讨论的极性基团回迁）会导致亲水性在数小时到数天内衰减。
### 5.2 PP 表面改性 —— i-PP 的低表面能 (~30 mN/m) 与胶黏剂涂布

- i-PP（等规聚丙烯）γ_d ≈ 30.6，γ_p ≈ 0.3 erg/cm²（色散主导，极性近零）→ 胶黏剂无法形成有效分子接触（Eq. 12.16 中 γ_SL 大，θ 大）。
- Ch12 Sec. 12.8.5 的电晕/等离子/火焰处理在此场景为标准答案：

- 火焰处理：用于汽车保险杠、PP 内饰件（Ch12 line 2699 "Manufacture of thermoplastic composites"）。
- 电晕处理：用于卫生用品用 PP 复合膜。
- 处理后的 PP 表面极性分量 γ_p 由 0.3 → 8–12 erg/cm²，可承受水性胶黏剂涂布。
### 5.3 PE/PP 熔喷纤维的表面润湿 —— 熔喷工艺中纤维直径小 → 表面积大 → 表面能效应显著

- 熔喷工艺 (meltblown) 产生直径 1–5 μm 的超细纤维 → 单位质量的比表面积是常规纺粘纤维的 ~10–50 倍。
- 由 Ch12 Eq. 12.1（W = γ · dA，line 79）：当 dA 增大到 10 倍，任何界面过程（润湿、吸附、吸附功）的宏观能量也放大 10 倍。
- 应用意义：

- 熔喷纤维用作湿巾面层、面膜基底时，亲水改性（电晕/表面活性剂涂层） 决定水基液剂能否被吸收。
- 熔喷纤维用作湿巾的胶层（热胶网帘粘合 HMB）时，表面能匹配 决定胶对基底的铺展系数 S（Eq. 12.11）。
### 5.4 胶黏剂选型 —— 表面能匹配原则（Fowkes / Owens–Wendt）在卫材胶黏剂选型中的应用

- 匹配准则：Ch12 Eq. 12.20 W_a = γ_a + γ_b − γ_ab，Fowkes 分量法 γ_ab ≈ √(γ_a^d · γ_b^d) + √(γ_a^p · γ_b^p)。卫材胶黏剂设计目标是 最大化 W_a：

- 胶的 γ_d 与基材 γ_d 匹配 → 色散项最大。
- 胶的 γ_p 与基材 γ_p 匹配 → 极性项最大。
- 卫材典型匹配：

- 水性丙烯酸胶 → 熔喷 PP：胶 γ ≈ 40，γ_p ≈ 8–12；熔喷 PP 电晕后 γ ≈ 40–45 → W_a 接近最大。
- 热胶 EVA → PE/PP 无纺布：EVA γ ≈ 33（Table 12.1 line 102），与 PE γ = 35.7 匹配 → 熔体润湿良好。
- SBS 压敏胶 → PET 底纸：需符合 Ch12 Dahlquist 准则（line 2273：动态剪切模量 < 3 × 10⁶ dyn/cm²，T − T_g = 40–70 °C）。
### 5.5 湿巾涂覆层 —— 胶乳/水性涂覆的表面张力控制

- 湿巾的胶乳涂覆（latex coating）用于阻隔细菌、增强手感。Ch12 Sec. 12.5.1（lines 1281–1305）讨论 nondrip latex paint，原理完全通用：

- 胶乳颗粒需 铺展成膜 → S_b/a ≥ 0（Eq. 12.11）。
- 成膜过程中的 聚合物链相互扩散（Sec. 12.3.7.2，lines 939–1060）决定涂层强度；σ_th 需 > ~8b/√(6χ) 以产生足够缠结。
- 水性涂覆的 表面张力控制：

- 水基胶乳 γ ≈ 30–35 mN/m（远低于纯水 72.9），靠 表面活性剂 降低 γ 以润湿低表面能无纺布。
- 涂覆后的 表面改性回迁（hydrophobic recovery）可通过交联剂（Ch12 line 2161 "cross-linked"）抑制。

## 模块6：Key Quotes Index（原文引用索引）

||||
|---|---|---|
|1|"The surface of any material is different from the interior or bulk of the material."|lines 32–33|
|2|"The surface tension is the reversible work needed to create a unit surface area in a substance."|line 62|
|3|"Thus water beads up on polymers with low surface tensions, not wetting them. For example, low surface tension underlies the utility of the Teflon® polytetrafluoroethylene frying pan."|lines 71–74|
|4|"If S_b/a is positive, spreading is accompanied by a decrease in the free energy, and the process is spontaneous."|lines 229–230|
|5|"A balance of the three relations leads to Young's equation, one of the oldest in surface science."|lines 287–289|
|6|"The maximum sampling depth [of XPS/ESCA] is 10 to 100 Å."|lines 431–436|
|7|"Wa = γ_a + γ_b − γ_ab … The quantity W_a is a lower bound value, since chain scission and chain pullout are ignored."|lines 992–1000|
|8|"Physical entanglements are critical to the development of high-fracture energy, about eight per chain necessary for optimum mechanical strength."|lines 1058–1060|
|9|"Poly(dimethyl siloxane) rises to the surface preferentially in polycarbonate–block–poly(dimethyl siloxane) segmented copolymer blends, as characterized by ESCA instrumentation."|lines 439–459 (Fig. 12.4)|
|10|"Surface modification of polymers involves altering the characteristics of the material … the surface may be exposed to plasma or corona treatments."|lines 2278–2287|
|11|"Pressure-sensitive adhesives must be very sticky … The Dahlquist criterion [requires] dynamic shear modulus … less than 3 × 10⁶ dyn/cm²."|lines 2272–2275|
|12|"An examination of the literature shows that modern polymer interface science dates only from about 1989 … interface science is just beginning, and far from mature."|lines 2643–2653|
|13|"No material can come into being without creating a surface or interface!"|line 2642|
|14|"If one or both polymers are subsequently cross-linked, the bond strength may be improved."|lines 2161–2162|

## 附录：关键方程一览

|||||
|---|---|---|---|
|12.1|W = γ · dA|表面自由能定义|79|
|12.2|dG = γ · dA|表面自由能微分|84|
|12.3|G⁰s = (∂G/∂A)_{T,P} = γ|表面自由能|112|
|12.4–12.5|S⁰s = −dγ/dT|表面熵|120, 126|
|12.7|γ = c₁ + c₂T + c₃T²|温度依赖|142|
|12.8|γ(Mₙ) = γ∞ − k/Mₙ|分子量依赖|147|
|12.11|S_b/a = γ_a − γ_b − γ_ab|铺展系数|225|
|12.16|γ_SV = γ_SL + γ_LV cos θ|Young 方程|290|
|12.17|γ_ab = √(χ/6) · ρ₀ · b · kT|Helfand–Tagami 界面张力|963|
|12.18|σ_th = 2b / √(6χ)|界面相厚度|970|
|12.19|G_Ic = 2γ_ab (σ_th/b)²|临界断裂能|985–986|
|12.20|W_a = γ_a + γ_b − γ_ab|粘附功|996|
|12.42|−ΔH = E_A·E_B + C_A·C_B|Drago 方程|2301|
|12.43|−ΔH = 0.0103·Δν_OH + 3.08 (kcal/mol)|红外频移热方程|2322|
|12.44|W_AB = − f·n_AB·ΔH|酸碱粘附功|2375|

报告结束。所有行号对应 /sandbox/workspace/Ebook_Extract/SPERLING/chapters/SPERLING_ch12.txt。


---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_e9b0d76eaea966583a0b5d47215d4db5001a693ee6c0644e"
source_file: "Introduction to Physical Polymer Science_ch4_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch4_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Introduction to Physical Polymer Science_ch4_report.md.md

# 《Introduction to Physical Polymer Science》第4章深度拆解

Concentrated Solutions, Phase Separation Behavior, and Diffusion
Source: L. H. Sperling, 4th Ed., Wiley 2006 (Ch.4, pp.148–195, 约 2007 行)

## 模块1：Core Arguments（核心论点）

Polymer–polymer blends overwhelmingly phase-separate at the thermodynamic level because the combinatorial entropy of mixing is too small to overcome a typically endothermic heat of mixing.
> "When two polymers are mixed, the most frequent result is a system that exhibits almost total phase separation. Qualitatively, this can be explained in terms of the reduced combinatorial entropy of mixing of two types of polymer chains..." (lines 186–190)

Polymer–polymer miscibility, when it occurs, displays LCST behavior; equation-of-state theories (Flory EOS, Sanchez–Lacombe lattice fluid) explain LCST as a consequence of exothermic mixing plus negative excess entropy (densification on mixing).
> "The new theories pointed out that LCST behavior is characteristic of exothermic mixing and negative excess entropy. This last is caused by densification of the polymers on mixing." (lines 231–234)

Polymer solution space is divided by scaling concepts into five regimes — ideal, dilute, semidilute, marginal, concentrated — plus a phase-separated region, each characterized by universal exponents.
> "Daoud and Jannink and others divided polymer–solvent space into several regions... Each of these regions exhibits distinct molecular characteristics, as derived by scaling concepts." (lines 127–134); and de Gennes' scaling: "Scaling concepts... brought to their modern state of importance by de Gennes." (lines 135–139)

Phase separation proceeds by one of two kinetic mechanisms — nucleation-and-growth (NG, metastable, positive D, spherical domains) or spinodal decomposition (SD, unstable, negative D, interconnected cylinders) — controlled by the position relative to binodal/spinodal lines.
> "Nucleation and growth are associated with metastability, implying the existence of an energy barrier... Spinodal decomposition, on the other hand, refers to phase separation under conditions in which the energy barrier is negligible." (lines 528–535)

Permeability of small molecules through polymers is the product of diffusivity and solubility, and is controlled by polymer packing, free volume, crystallinity, orientation, and plasticization; elastomers > amorphous plastics > semicrystalline plastics in permeability.
> "The permeability coefficient, P, is defined as the volume of vapor passing per unit time through unit area of polymer having unit thickness... For the simplest case P = D·S." (lines 1050–1057); "permeability decreases from elastomers to amorphous plastics to semicrystalline plastics." (lines 1107–1110)

## 模块2：Key Concepts with Operational Definitions

### 1. Phase separation（相分离）

Operational definition: 在聚合物–溶剂或聚合物–聚合物体系中，均匀单相体系在给定 T、P、composition 下变为热力学不稳定，系统自发分解为两（或多）相，分别富集不同组分。实验上通过浊度/云点测定、DSC 观察两个 Tg、SANS 观察 A₂ 变化、电镜观察 domain 来判定。(lines 719–741, 821–833)

### 2. Cloud point / Turbidity point（云点/浊点）

Operational definition: 向均相聚合物溶液缓慢加入不良溶剂（non-solvent），当体系出现浑浊时记录 non-solvent 分数，该分数即为 cloud point；由一系列 cloud point 数据构成云点曲线（binodal）。实验上以固定光路透过率下降到 50% 为判据。(line 719–720; "phase diagram by cloud point determination")

### 3. Spinodal vs Binodal（旋节线 vs 双节线）

- Binodal (双节线)：两相化学势相等的平衡共存边界，即 $\left(\frac{\partial \Delta GM}{\partial \phi}\right){T,P}=0$ 给出；binodal 内两相共存。
- Spinodal (旋节线)：体系变为热力学不稳定的边界，即 $\frac{\partial^2 G}{\partial \phi^2}=0$；旋节线内扩散系数为负，任何浓度涨落都会放大。(lines 247–249, 595–597)
### 4. Flory–Huggins in concentrated solutions（浓溶液中的 FH 扩展）

FH 稀溶液公式 $\Delta G_M/RT = \nu_1 \ln\nu_1 + \nu_2 \ln\nu_2 + \chi\nu_1\nu_2$ 被推广至 $\nu_2$ 高达 0.1–0.5 的浓溶液和聚合物熔体；配合 Sanchez–Lacombe 格点流体理论引入方程状态（EOS）项（自由体积熵），得到含 $\tilde T^, \tilde P^, \tilde\rho^*$ 的通用形式，能解释 LCST。(lines 206–234, 381–419)

临界浓度和临界相互作用参数：
$$v{2c} = \frac{1}{1+n^{1/2}} \approx \frac{1}{n^{1/2}} \quad (n\to\infty) \tag{4.1}$$
$$\chi{1c} = \frac{(1+n^{1/2})^2}{2n} \approx \frac{1}{2} \quad (n\to\infty) \tag{4.2}$$
(critical concentration & χ; lines 20–32)

### 5. Berghmans' Point（玻璃化–双节线交点）

Operational definition: 液–液相分离的 binodal 与聚合物 vitrification 曲线（Tg 随溶剂塑化下降，通常用 Fox 方程拟合）的交点。在 BP 以下，聚合物被冻结为玻璃态，扩散减慢，binodal 无法实验实现，tie line 停止。(lines 78–93)

### 6. Vitrification line / Plasticization（玻璃化线/塑化）

Operational definition: 浓聚合物溶液随溶剂体积分数增加，Tg 由纯聚合物 Tg 沿 Fox 方程下降。当 Tg 降至实验温度以下时，玻璃态向橡胶态转变，扩散加速；反之则冻结。(lines 84–87)

### 7. Screening length / Correlation length（屏蔽长度 ξ）

Operational definition: 稀溶液中 $\xi = R_g$；半稀溶液中 $\xi$ 为链间接触距离（即 blob 尺寸），满足标度律 $\xi_s \sim \phi^{-3/4}$。交联网络中 $\xi$ 为网孔尺寸。该量在相图各区定义均不同。(lines 152–160, 1963–1990)

### 8. Blob（"线团中的线团"）

Operational definition: 半稀溶液中同一条链上、处于体积 $\xi_s^3$ 内的链段数目；blob 内部排斥体积效应依然有效，多个 blob 串联形成整条链，故自相似。浓度增大时 blob 变小，至聚合物熔体时 $\xi_s \sim$ monomer 尺寸。(lines 173–181)

### 9. Diffusion & Permeability（扩散与渗透）

- Fick 第一定律（稳态）：$J = -D \frac{\partial c}{\partial x}$ (eq. 4.22, lines 1021–1023)
- Fick 第二定律（非稳态）：$\frac{\partial c}{\partial t} = \frac{\partial}{\partial x}\left(D\frac{\partial c}{\partial x}\right)$ (eq. 4.23, lines 1032–1034)
- 渗透系数：$P = D\cdot S$ (eq. 4.24, line 1055)，S 为溶解度系数；温度依赖由 Arrhenius $D = D_0 e^{-E_D/RT}$ 描述。
### 10. Rubber self-diffusion coefficient（橡胶自扩散系数）

Operational definition: 交联或长链橡胶中聚合物链沿自身主链方向的"蛇行"(reptation)自扩散系数，量级在 $10^{-14}$–$10^{-9}$ cm²/s，随分子量下降。Sperling 强调自由体积、$T_g$、链段协同运动（concerted movement）是决定橡胶中气体渗透扩散速度的关键机制。(lines 986–992, 1120–1123, 1190–1193)

### 11. Latex（胶乳/乳胶）

Operational definition: 粒径 0.04–5 μm 的球形聚合物粒子分散在水中，表面由表面活性剂（如十二烷基硫酸钠）包裹，靠静电双电层排斥保持稳定；由乳液聚合（monomer + surfactant + 水溶性引发剂如过硫酸钾）制得；粒子足够小由布朗运动保持悬浮。(lines 1495–1505, 1508–1512, 1558–1566)

### 12. Suspension（悬浮液）

Operational definition: 粒径 5–1000 μm 的聚合物颗粒在水中的分散体系；形状由球形到土豆形；用极性聚合物（非表面活性剂）作乳化剂，油溶性引发剂；动力学行为近似本体聚合；静置会"creaming"需持续搅拌。(Table 4.7, lines 1506–1513; lines 1536–1543)

### 13. Multicomponent / Multiphase systems（多组分/多相体系）

Operational definition: 含有≥2 种聚合物或含溶剂/增塑剂的复杂体系，呈现微相分离。典型形态：graft copolymer（如 HIPS）、IPN（互穿网络）、block copolymer（球/柱/层三种微相，尺寸由 Meier 公式计算）、ionomer（含 5–15% 离子基团，离子簇形成物理交联）。domain 尺寸在 200–1000 Å 范围，决定材料阻尼或抗冲击性能。(lines 818–840, 842–925, 964–975, 1580–1605)

### 14. LCST / UCST（下/上临界溶解温度）

Operational definition: UCST — 温度低于此点时发生相分离（一般小分子或低分子量聚合物–溶剂体系）；LCST — 温度高于此点时发生相分离（高分子量聚合物共混或聚合物–溶剂体系的典型行为）。高聚合度聚合物体系几乎总是 LCST。(lines 197–222, Figure 4.7)

## 模块3：Evidence Tables（证据表）

### 表1：典型聚合物–溶剂/聚合物–聚合物体系的相图类型

|||||||
|---|---|---|---|---|---|
|Polystyrene / Cyclohexane|聚合物–溶剂|单一 UCST dome|θ = 34.5 °C；$v_{2c} \approx 0.01$ (n = 10⁴)|分馏随 MW 分布|lines 24–35, 57–59|
|Polystyrene fractions / Cyclohexane|聚合物–溶剂（多分散）|多曲线族，低 MW 相分离温度低|曲线族随 MW 增大|分馏效率在低浓度最高|lines 46–51, Fig 4.2|
|Polyisobutylene / Diisobutyl ketone|聚合物–溶剂|UCST 型|$T_c$ vs $n^{-1/2}+1/(2n)$ 线性外推|Flory θ 温度法|lines 64–66, Fig 4.3|
|PS / poly(vinyl methyl ether)|聚合物–聚合物|LCST + UCST（双峰）|完全互溶 < 80 °C|最佳表征的 SD/NG 体系|lines 547–550|
|PMMA / PVDC|聚合物–聚合物|LCST|负混合热|特殊相互作用稳定互溶|lines 721–724|
|PS / PPO (2,6-dimethyl-1,4-PO)|聚合物–聚合物|LCST|全组成范围互溶|抗冲击塑料基础|lines 722–724|
|SAN / PMMA|聚合物–聚合物（共混首案）|LCST|McMaster 首个工作图|Cloud point 测定|lines 718–721|
|PPO / o-ClSt-stat-p-ClSt|统计共聚物共混|互溶窗口（mid-range compositions, low T）|ΔG_M < 0 的窗口|DSC 测 Tg 判互溶|lines 649–665|

### 表2：扩散系数 D 随分子量 M 的变化趋势

规律（来自 Sperling 关于渗透、橡胶、reptation 与 de Gennes 标度律的论述；lines 135–139, 986–992, 1120–1123, 152–160, 1994–2005）：

|||||
|---|---|---|---|
|中心力扩散（中心粒子在稀溶液）|$D \sim M^{-1/2}$|Rouse/自由链，R ~ M^ν，Stokes|通用物理|
|缠结橡胶自扩散（reptation）|$D \sim M^{-2}$|de Gennes 蛇行模型；M > Mₑ|de Gennes Scaling (lines 135–139, 1849–1851)|
|橡胶中气体扩散（自由体积）|$D = D_0 e^{-E_D/RT}$，$D \propto 1/f$|与自由体积分数 f 强相关；M 间接通过 Tg、f 影响|lines 993–1001, 1174–1179|
|半稀溶液链扩散|$D \sim M^{-2}\phi^{-1.75}$|结合 blob 理论 (ξ ~ φ^{-3/4})|Appendix 4.1|
|一般趋势（定性）|D 随 M 单调下降；长链橡胶/胶乳自扩散最慢|"molecular diffusion in the glassy state is far slower than in the liquid state"|lines 91–93|

典型量级参考（本书给出）：聚合物渗透中 $P \sim 10^{-11}$–$10^{-16}$ cm³·cm / (cm²·s·Pa)（lines 1092–1093）。

### 表3：常见聚合物膜在 25 °C 的渗透性数据（Table 4.5 原文，lines 1127–1150）

单位：$P$ 为 cm³ (STP)·cm / (cm²·s·Pa)，$P_0$ 为同单位前因子，$E_D$ 为 kJ/mol

|||||||
|---|---|---|---|---|---|
|LDPE（橡胶态）|O₂|2.2|66.5|42.7|高渗透|
|LDPE|N₂|0.73|329|49.9|—|
|LDPE|CO₂|9.5|62|38.9|—|
|LDPE|H₂O|68|48.8|33.5|水汽渗透|
|cis-Polybutadiene（橡胶）|N₂|14.4|0.078|21.3|橡胶最低 E_D|
|Polybutadiene|He|24.5|0.0855|20.3|最高渗透气体|
|PEMA（非晶塑料）|O₂|0.889|2.1|36.4|中等渗透|
|PEMA|CO₂|3.79|0.435|28.9|—|
|amorphous PET（饮料瓶主料）|O₂|0.0444|0.227|37.7|低渗透|
|amorphous PET|CO₂|0.227|0.00021|27.0|碳酸饮料阻隔|
|amorphous PET|CH₄|0.0070|0.9232|24.7|—|
|PVDC (Saran®)|N₂|0.00070|900|70.3|极高 E_D → 强阻隔|
|PVDC|O₂|0.00383|825|66.6|极强 O₂ 阻隔|
|PVDC|CO₂|0.0218|24.8|51.5|—|
|PVDC|H₂O|7.0|863|46.1|—|
|Cellulose|H₂O|18900|—|—|亲水高渗透|

规律：permeability rubber > amorphous plastic > semicrystalline plastic；E_D 高的材料（PVDC, cellulose）对气体有显著温度敏感性，是阻隔层首选。(lines 1107–1110, 1278–1293)

## 模块4：Chapter Connections（章间关联）

### 与 Ch3（稀溶液热力学 Dilute Solution Thermodynamics）的对比

|||||
|---|---|---|---|
|浓度范围|c < 1 %，用于测分子量|10–50 %，塑化聚合物；多区 (ideal/dilute/semi-dilute/marginal/concentrated)|lines 122–134|
|理论基础|二阶维里系数 A₂，θ 温度，Flory–Huggins 展开|FH 扩展至浓溶液 + Sanchez–Lacombe EOS + de Gennes 标度律|lines 206–234, 135–139|
|状态方程|简单 χ 参数描述|引入自由体积熵 DS_M，含 $\tilde\rho^, \tilde T^, \tilde P^*$ 的 EOS (eq. 4.8–4.13)|lines 381–425|
|θ 温度|定义、测定|与临界温度 $T_c$ 关系 (eq. 4.3) 及分馏效应|lines 36–45, 46–51|
|链尺寸|Rg ~ M^ν，ν=3/5 良溶剂；ν=1/2 θ 溶剂|链重叠 → 半稀区 Rg,s ~ Rg,d·(φ/φ_ov)^m；ξ ~ φ^{-3/4}；bulk Rg ~ M^{1/2}|lines 152–181, 1883–1944|
|A₂|测量方法（光散射等）|用作互溶性判据；SANS 测二元 A₂|lines 764–768|
|相行为|未讨论相分离|全面论述 binodal/spinodal、LCST/UCST、vitrification、Cahn–Hilliard 动力学|lines 240–260, 551–600|

### 与 Ch13（Multicomponent Polymer Materials）的衔接

- Ch4 明确说明聚合物共混与多相体系的深入讨论放在 Ch13：

- "While an introduction to phase separation in polymer blends is presented here, a more detailed development of polymer blends in general is given in Chapter 13." (lines 235–237)
- "Polymer blends are treated in more detail in Chapter 13." (line 975)
- Graft copolymer/impact features: "These features will be discussed further in Chapter 13." (lines 831–832)
- TPE (thermoplastic elastomer) "many as novel types of elastomer called thermoplastic elastomers (Chapter 13)" (lines 1603–1605)
- Ch4 提供 Ch13 需要的理论骨架：FH + EOS 混合自由能公式、LCST/UCST 相图、NG/SD 动力学、block copolymer 微相 domain 尺寸公式 (Meier, eq. 4.19–4.21)、ionomer 物理交联、共混物渗透系数 (parallel series model eq. 4.32–4.33)。
- Ch13 反哺 Ch4 的应用层：共混增韧 (HIPS/TPU/PU)、相容剂 (接枝/嵌段)、SAP 多相凝胶、共混膜透湿/阻隔设计。
## 模块5：Business Connections（卫材/卫生材料应用）

### 1. 相分离在 TPU/PU 共混体系中的应用（医用膜/导尿管/创可贴）

- TPU（热塑性聚氨酯） 天然是一种微相分离体系：硬段（MDI/BDO 或 TDI/Extender）聚集形成物理交联域，软段（聚酯/聚醚）形成连续橡胶相——本质就是 Ch4 讨论的 block copolymer 球/柱/层微相。(lines 842–925, 964–975, 1603–1605)
- 医用导管与创可贴要求：柔软（橡胶连续相）、抗张（硬段 domain 物理交联）、生物相容。通过调节硬段分数与 MW控制微相尺寸在 200–1000 Å，正合 Ch4 描述的域尺寸范围。(lines 705–710)
- LCST 特性警示：TPU/PU 在医用温度范围若遇高温消毒可能因 LCST 相分离导致雾浊或力学下降（Ch4 LCST 警示，lines 197–205, 231–237）。
- PU/TPU 共混增韧：类似 HIPS 中 SBR rubbery phase toughening 的机理（lines 828–837），SBR/EPDM rubber 相分散于 TPU 基质，小 domain 尺寸（< 500 nm）+ 界面接枝是实现高抗撕裂、柔顺性的关键。
### 2. 胶乳 (Latex) 在湿巾涂覆/纸尿裤底膜中的应用

- 湿巾涂覆：聚合物胶乳（如聚乙烯醇 PVA、SBR、丙烯酸酯胶乳）粒径 0.04–5 μm（Table 4.7，lines 1508–1512），表面吸附表面活性剂保持稳定分散。涂覆后水蒸发，表面张力形成 water menisci，粒子聚并、链互扩散形成连续柔性膜，实现柔软手感 + 一定阻隔。(lines 1570–1577)
- 纸尿裤底膜 (backsheet)：LDPE 热封 + PVDC/PA 复合阻隔层；部分新型底膜使用乳液涂覆的 PVA/淀粉复合膜（生物基可降解），涂覆干燥即 Ch4 描述的胶乳成膜过程。
- 医用外科手套/导尿管涂覆：天然橡胶胶乳（Hevea，约 5×10⁵ g/mol cis-1,4-聚异戊二烯，lines 1547–1554）靠表面蛋白质负电荷稳定；干燥成膜机制同 latex paint（lines 1558–1577）。
- 关键工艺参数：Tg 略高于室温 + 涂覆液 T > MFFT (Minimum Film Formation Temperature)，否则无法成膜（lines 1570–1577; footnote line 1614）。
### 3. 扩散与渗透在包装材料阻隔层中的应用

- 纸尿裤/卫生巾外层：阻隔水汽与气味。Ch4 数据显示 PVDC (Saran®) O₂ 渗透系数 $P = 0.00383 \times 10^{-13}$，仅为 LDPE 的 1/570，是首选高阻隔材料。(Table 4.5, lines 1141–1144)
- 复合膜阻隔：Ch4 eq. 4.32–4.33 的 parallel model（$P_b = f_1P_1+f_2P_2$，上界）与 series model（$1/P_b = f_1/P_1+f_2/P_2$，下界）直接用于设计 PP/PA/EVOH/PE 多层复合膜。(lines 1306–1329)
- 软饮料瓶 (PET)：amorphous PET 的 CO₂ $P = 0.227 \times 10^{-13}$，O₂ $P = 0.0444 \times 10^{-13}$——"碳酸饮料最终会变 'flat'"，shelf life 由渗透速率决定（lines 1111–1116，Study Problem 7, lines 1815–1820）。
- 医用药品泡罩包装 (blister)：选择 EVOH/PA 阻隔层，其原理即为 Ch4 渗透与溶胀理论（结晶度 ↑ → P ↓；lines 990–992）。
- Robeson 上限（lines 1277–1293）：高渗透性与高选择性存在 trade-off，包装/医用膜设计需在 $P$ 与 α (selectivity) 上限附近取点。
### 4. 多相体系在 SAP（交联聚丙烯酸钠凝胶）中的意义

- SAP 结构：本质是轻度交联的聚丙烯酸钠网络，浸水后高度溶胀而不溶解——完全符合 Ch4 交联聚合物溶胀的论述："Cross-linked polymers may reach the gel state, but they do not dissolve." (lines 100–102)
- 多相凝胶：SAP 内部存在交联密度不均匀的多相结构（高交联 domain 提供力学骨架，低交联区域提供吸收空间），类比 Ch4 讨论的IPN / graft copolymer 微相（lines 818–840）以及 ionomer 离子簇物理交联（lines 964–975，Na⁺²⁺³⁺）。
- 凝胶渗透与释药：Ch4 eq. 4.24（$P = DS$）与药物扩散动力学（lines 1422–1469, Figure 4.21）完全适用 SAP 的吸液/释液行为。图 4.21 中 hydrophobic 侧链越长 → 扩散越慢，提示 SAP 中引入亲水改性可加速液体吸收。
- 卫生用品中的 SAP 层：纸尿裤中 SAP 层与顶/底层胶乳膜共同构成多相复合体系（多组分/多相，lines 1580–1605）：SAP 凝胶吸收 → 胶乳/PE 膜阻隔 → 湿巾涂覆胶乳提供手感。三层协同依赖 Ch4 描述的界面互扩散和成膜原理。

## 模块6：Key Quotes Index（关键原文摘录，8–12 条）

|||||
|---|---|---|---|
|1|"When two polymers are mixed, the most frequent result is a system that exhibits almost total phase separation... in terms of the reduced combinatorial entropy of mixing of two types of polymer chains."|186–190|聚合物共混相分离热力学根源|
|2|"When two polymers do mutually dissolve, they are generally found to phase-separate at some higher temperature rather than at some lower temperature. This is called a lower critical solution temperature (LCST)."|197–200|LCST 现象|
|3|"The new theories pointed out that LCST behavior is characteristic of exothermic mixing and negative excess entropy. This last is caused by densefication of the polymers on mixing."|231–234|LCST 的 EOS 解释|
|4|"Daoud and Jannink and others divided polymer–solvent space into several regions, plotting the volume fraction of polymer, φ, vs the excluded volume parameter, v."|127–130|浓溶液五区图|
|5|"Scaling concepts in polymer physics were brought to their modern state of importance by de Gennes. They consist of a series of proportionalities, showing the algebraic relationships between many quantities..."|135–139|de Gennes 标度律|
|6|"Nucleation and growth are associated with metastability, implying the existence of an energy barrier... Spinodal decomposition, on the other hand, refers to phase separation under conditions in which the energy barrier is negligible, so even small fluctuations in composition grow."|528–535|NG vs SD|
|7|"The spinodal line is defined by the locus of temperatures in the phase diagram, where ∂²G/∂φ² = 0."|595–596|旋节线定义|
|8|"Permeation is the rate at which a gas or vapor passes through a polymer. The mechanism... involves three steps: (a) absorption... (b) diffusion... (c) desorption."|980–985|渗透三步骤|
|9|"For the simplest case P = D·S, which expresses the permeability in terms of solubility and diffusivity."|1050–1057|渗透系数关系|
|10|"In general, permeability decreases from elastomers to amorphous plastics to semicrystalline plastics."|1107–1110|渗透性规律|
|11|"Basically a latex is synthesized by mixing monomer, surface active agent (surfactant), and an initiator (free radical source) into the water."|1495–1497|胶乳合成|
|12|"As the water evaporates, coalescence surface tension forces proceed from the presence of water menisci of very small radii of curvature... Interdiffusion of the polymer chains takes place, forming coherent films."|1570–1577|胶乳成膜机理|
|13|"Block copolymers also serve a variety of purposes, many as novel types of elastomer called thermoplastic elastomers... forming the basis for many shoe soles now in use."|1603–1605|嵌段共聚物/热塑性弹性体|
|14|"Polymer blends are treated in more detail in Chapter 13."|975|与 Ch13 的衔接|

## 附注：公式与数值快速索引

|||||
|---|---|---|---|
|4.1|$v_{2c} = 1/(1+n^{1/2}) \approx 1/n^{1/2}$|20–24|聚合物–溶剂体系临界浓度|
|4.2|$\chi_{1c} \approx 1/2$ (n→∞)|28–32|临界 χ 参数|
|4.3|$1/T_c = (1/\theta)[1+1/\gamma_1+1/(n^{1/2}+1/2n)]$|39–44|临界温度与 θ 温度|
|4.4|$\xi_s \sim \phi^{-3/4}$|157–160|半稀区屏蔽长度|
|4.14|$\partial\phi/\partial t = M[(\partial^2G/\partial\phi^2)\nabla^2\phi - 2K\nabla^4\phi]$|586–594|Cahn–Hilliard 动力学方程|
|4.19–4.21|$R = aKM^{1/2}$ (球 1.33, 柱 1.0, 层 1.4)|897–904|嵌段共聚物微相 domain 尺寸|
|4.22|$J = -D\,\partial c/\partial x$|1021–1023|Fick 第一定律|
|4.23|$\partial c/\partial t = \partial/\partial x (D\,\partial c/\partial x)$|1032–1034|Fick 第二定律|
|4.24|$P = D\cdot S$|1055|渗透系数 = 扩散 × 溶解|
|4.31|$\alpha_{A/B} = P_A/P_B$|1271–1273|气体选择性|
|4.32|$P_b = f_1P_1 + f_2P_2$ (parallel)|1316|共混膜渗透上界|

关键数值：θ(PS/环己烷) = 34.5 °C；LDPE O₂ P = 2.2×10⁻¹³；PVDC O₂ P = 0.00383×10⁻¹³（LPE 的 1/570）；Hevea NR Mw ≈ 5×10⁵ g/mol；嵌段共聚物 domain 尺寸 200–1000 Å；橡胶/非晶塑料/半结晶塑料渗透递减；临界 χ ≈ 1/2；临界 $v{2c}$ (n=10⁴) ≈ 0.01。


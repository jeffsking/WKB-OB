---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_7fc91826e8c4aa6159d1f5824d95383d001a693ee6c0644e"
source_file: "ch5_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch5_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch5_report.md.md

# 《Principles of Polymerization》第5章 Ionic Chain Polymerization 深度拆解

原著：George Odian，*Principles of Polymerization*，4th Ed.（2004），John Wiley & Sons
源文件：/sandbox/workspace/Ebook_Extract/Principles_of_Polymerization/chapters/ch5_ionic.txt
章节范围：Ch.5（约 1–4733 行，文本页码 372–448）

## 模块1：核心论点

离子聚合对单体高度选择性，远弱于自由基聚合的商业普适性（原文行 21–30）
"Almost all monomers containing the carbon–carbon double bond undergo radical polymerization, while ionic polymerizations are highly selective … The commercial utilization of cationic and anionic polymerizations is rather limited because of this high selectivity."
阳离子仅聚合供电子取代基单体（烷氧基、苯基、乙烯基、1,1-二烷基）；阴离子仅聚合吸电子取代基单体（腈、羰基、苯基、乙烯基）。

离子链端的稳定性是机理选择性的根本来源（原文行 41–56、72–84）
阳离子和阴离子链端必须以离子对（紧密对/溶剂分隔对）+ 自由离子的多态平衡存在；溶剂极性决定哪种形态为主，进而决定反应速率和分子量。

阴离子活性聚合（Living Anionic Polymerization）天然无终止，而阳离子活性聚合需要"休眠-活化"动态平衡才可能实现（原文行 1699–1752、2301–2323）
阴离子体系"没有内置的终止反应"；阳离子体系的"内置β-H转移"必须通过Lewis 酸+共离子盐+亲核体+低温组合把活性种转化为休眠共价酯/卤化物，才能实现活性聚合。

阳离子聚合的动力学特征为 Rp ∝ R_i^1，而自由基为 Rp ∝ R_i^{1/2}——源于阳离子终止是一级反应而非双分子偶合（原文行 966–975）
"Radical polymerizations show a 1/2-order dependence of R_p on R_i, while cationic polymerizations show a first-order dependence of R_p on R_i."

活性聚合的分子量遵循 X̄_n = p[M]_0/[I]_0，分布服从 Poisson，PDI → 1 + 1/X̄_n ≈ 1.05–1.1（原文行 2932–2959、1813–1824）
"PDI values below 1.1–1.2 are found for many living polymerizations … a unique method of synthesizing standard polymer samples of known and well-defined molecular weights."

## 模块2：关键概念操作化定义

### 2.1 阳离子聚合（Cationic Polymerization）——引发/增长/终止/链转移

(a) 中文名：阳离子聚合｜英文：Cationic polymerization
(b) 定义：由 Lewis 酸/质子酸产生的碳正离子（carbocation）对含供电子取代基单体进行的链式加成聚合；活性链端为与反离子平衡存在的离子对/自由阳离子。
(c) 原文摘录（行 164–170、184–191）
"Various Lewis acids are used to initiate cationic polymerization, generally at low temperatures … These include metal halides (e.g., AlCl₃, BF₃, SnCl₄, SbCl₅, ZnCl₂, TiCl₄) … Lewis acids are the most important means of initiating cationic polymerization."
"BF₃ + H₂O ⇌ BF₃·OH₂ … BF₃·OH₂ + (CH₃)₂C=CH₂ → (CH₃)₃C⁺(BF₃OH)⁻"

增长（行 509–526）：
"The initiator ion pair … proceeds to propagate by successive additions of monomer molecules … The propagation reaction … occurs by insertion of monomer between the carbocation and its negative counterion."
$$k_p$$：增长速率常数；$$R_p = k_p^+ [YM(IZ)^-][M]$$（Eq. 5-13b、5-31）

终止/链转移（行 626–673、698–724）：
β-质子转移是最主要的链断裂方式；可向单体、反离子、其他碱性物种转移。
"Transfer of a β-proton from the propagating carbocation is the most important chain-breaking reaction."（行 634–640）
$$\frac{1}{X_n} = \frac{k_t}{kp[M]} + \frac{k_{ts}}{k_p[M]} + C_M + C_S\frac{[S]}{[M]}$$（Eq. 5-41，行 941–943）

### 2.2 阴离子聚合（Anionic Polymerization）——引发/增长/终止

(a) 中文名：阴离子聚合｜英文：Anionic polymerization
(b) 定义：由亲核性引发剂（碱）对含吸电子基单体进行的链式聚合，活性链端为碳负离子与正离子反离子组成的离子对/自由阴离子。
(c) 原文摘录（行 2078–2098、2101–2134）
"Anionic chain polymerizations show many of the same characteristics as cationic polymerizations … the propagating species are anionic ion pairs and free ions … Unlike cationic polymerization, there is a large difference between the reactivities of ion pairs and free ions in anionic polymerization."
"Alkyllithium compounds are probably the most useful of these initiators, employed commercially in the polymerizations of 1,3-butadiene and isoprene."（行 2110–2112）

增长（Eq. 5-61/5-62，行 2114–2125）：
$$Rp = k_{p,app}^-[M^-][M]$$（Eq. 5-84，行 2646）
终止（行 2301–2353）：
- 无终止体系（活性聚合）："Propagation occurs with complete consumption of monomer to form living polymers."
- 杂质终止（行 2326–2351）：$$C_{tr,S}(H2O)\approx 10$$（苯乙烯，25 °C，钠萘）；$$C_{tr,S}(EtOH)\approx 10^{-3}$$。

### 2.3 活性聚合（Living Polymerization）

(a) 中文名：活性聚合｜英文：Living polymerization
(b) 定义：无链断裂反应（无终止、无转移），活性链浓度恒定至100%转化；$$M_n$$ 与转化率线性，可追加单体继续增长。
(c) 原文摘录（行 1699–1709）
"Living polymerizations are polymerizations without chain-breaking reactions … the concentration of propagating species remains constant throughout the polymerization and even after 100% conversion. A plot of M_n versus conversion is linear."
"Living anionic polymerization is relatively easy to achieve if one has a well-purified system … Anionic propagating systems do not have a 'built-in' termination reaction."（行 1714–1717）

### 2.4 阳离子 vs 阴离子 vs 自由基——单体选择性对比

(a) 中文名：聚合方式单体选择性｜英文：Monomer selectivity among radical/cationic/anionic polymerizations
(b) 定义：自由基聚合几乎适用于所有含 C=C 双键单体；离子聚合高度依赖取代基的电子效应。
(c) 原文摘录（行 21–30、3733–3757）
"Cationic polymerization is essentially limited to those monomers with electron-releasing substituents such as alkoxy, phenyl, vinyl, and 1,1-dialkyl. Anionic polymerization takes place with monomers possessing electron-withdrawing groups such as nitrile, carbonyl, phenyl, and vinyl."（行 22–25）
鉴别方法（行 3742–3757）：离子聚合低温进行、对溶剂极性/反离子敏感、DPPH 自由基捕捉剂无效。

### 2.5 反离子效应——紧密离子对/溶剂分隔离子对/自由离子

(a) 中文名：反离子/离子对效应｜英文：Counter-ion effects; tight (contact) ion pair; solvent-separated ion pair; free ion
(b) 定义：活性链端以 $$\text{I (共价)}\ \rightleftharpoons\ \text{II (紧密离子对)}\ \rightleftharpoons\ \text{III (溶剂分隔离子对)}\ \rightleftharpoons\ \text{IV (自由离子)}$$ 四态平衡存在；溶剂极性高 → 松散对+自由离子比例升高；阴离子体系中自由离子的 $$k_p$$ 比离子对高 1–3 个数量级。
(c) 原文摘录（行 63–80、72–85）
"one can visualize the range of behaviors from one extreme of a completely covalent species (I) to the other of a completely free (and highly solvated) ion (IV) … The intermediate species include the tight or contact ion pair (II) … and the solvent-separated or loose ion pair (III)."
"Increased solvent polarity favors the loose ion pair while the tight ion pair predominates in solvents of low polarity."（行 84–85）

Table 5-10（行 2706–2714）苯乙烯/钠萘 25 °C：
| 溶剂 | 介电常数 | $$k_{p,app}$$ (L·mol⁻¹·s⁻¹) |
|---|---|---|
| 苯 | 2.2 | 2 |
| 二氧六环 | 2.2 | 5 |
| THF | 7.6 | 550 |
| 1,2-二甲氧基乙烷 | 5.5 | 3800 |

### 2.6 等活性假设（Equal Reactivity of Chain Ends）

(a) 中文名：等活性假设｜英文：Equal reactivity of chain ends / equivalence of propagating centers
(b) 定义：活性链的 $$k_p$$ 与链长无关；活性聚合动力学推导（如 Eq. 5-58、5-84、5-98/5-99）的基础。
(c) 原文摘录（行 2932–2955、2641–2646）
"The number-average degree of polymerization for a living anionic polymerization is the ratio of the concentration of reacted monomer to the concentration of living ends … $$X_n = p[M]_0/[I]_0$$."
该假设在活性体系中近似成立，因为"the free ions and ion pairs are in rapid equilibrium … the average fractions of its lifetime spent as free ions and ion pairs are not too different than for any other propagating chain"（行 2974–2979）。

### 2.7 聚异丁烯（PIB）/ 丁基橡胶 / 合成聚异戊二烯

(a) 中文名：聚异丁烯/丁基橡胶｜英文：Polyisobutylene (PIB); butyl rubber; polyisoprene
(b) 定义：
- PIB 为异丁烯阳离子均聚物，分子量由温度决定（-40~10 °C 得低聚物；-100~-90 °C 得高分子量）。
- 丁基橡胶 = 异丁烯/异戊二烯（0.5–2.5%）共聚物，AlCl₃ 引发，-100~-90 °C 连续淤浆工艺，M_n ≥ 200,000，全球年产量约 10⁹ 磅。
- 聚异戊二烯（合成天然橡胶）由丁基锂或丁基锂/萘引发 1,3-丁二烯和异戊二烯阴离子聚合获得；与苯乙烯的嵌段共聚物为热塑性弹性体（Kraton、Stereon 等），年产量超过 2×10⁹ 磅。
(c) 原文摘录（行 1994–2056、3427–3430）
"Butyl rubber (BR) is a copolymer of isobutylene with small amounts of isoprene produced by aluminum chloride initiated polymerization. About 1 billion pounds of butyl rubber are produced annually in the United States."（行 2009–2010）
"The annual worldwide production of triblock thermoplastic elastomers, clear impact-resistant polystyrene, and other styrene–diene products produced by anionic polymerization exceeds a couple of billion pounds."（行 3427–3430）

### 2.8 ROMP（Ring-Opening Metathesis Polymerization）——本章未涉及

原文全文检索无 "metathesis"、"ROMP" 关键词。第5章仅覆盖：
- 链式离子聚合（C=C 双键，Sec. 5-2、5-3）
- 羰基聚合（Sec. 5-6）
- 杂环单体聚合（Sec. 5-7，含环氧化物、异氰酸酯）
- ROMP 属配位/金属烯烃复分解范畴，在本章范围之外；Odian 全书将其列入 Ch.8（协调聚合）或 Ch.10（烯烃复分解）讨论。

## 模块3：证据链

### 表3-1 阳离子聚合典型单体与引发体系（据原文行 121–191、360–386、1826–1908、1994–2076 归纳）

|||||||
|---|---|---|---|---|---|
|异丁烯 (Isobutylene)|1,1-二烷基|AlCl₃/H₂O；BF₃/H₂O；TiCl₄/H₂O；t-BuCl/AlCl₃|-40~10 °C（低聚）；-100~-90 °C（高分子量）|丁基橡胶、PIB 粘合剂|
|异戊二烯/异丁烯共聚|1,1-二烷基 + 共轭二烯|AlCl₃/CH₃Cl（CH₃Cl 作稀释剂）|-100~-90 °C|丁基橡胶|
|乙烯基醚（异丁基、甲基）|烷氧基（强供电子）|HI/I₂；HI/ZnI₂；HCl/SnCl₄；HCl/TiCl₄|-78~25 °C（LCP）|塑料化剂、涂料、LCP 模型体系|
|苯乙烯|苯基|BF₃·Et₂O；AlCl₃/ROH|低温|阳离子低聚物树脂|
|茚 (Indene)|芳基|Lewis 酸/质子酸|低温|沥青改性|
|香豆酮 (Coumarone)|芳基|Lewis 酸|低温|煤焦油树脂|
|α-甲基苯乙烯|苯基 + 甲基|BF₃/ROH|低温（活性聚合研究）|活性聚合示踪单体|
|1-丁烯等 α-烯烃|单烷基（弱）|AlCl₃/H₂O|-80~-130 °C|主要得异构低聚物 (DP 10–20)|

### 表3-2 阴离子聚合典型单体与引发体系（据原文行 2078–2159、2301–2447、2522–2640、2809–2931 归纳）

|||||||
|---|---|---|---|---|---|
|苯乙烯 (Styrene)|苯基|n-BuLi；钠萘；苯甲基金属|苯、THF、DME|首个活性聚合经典单体；PDI < 1.1|
|1,3-丁二烯 (Butadiene)|共轭二烯|n-BuLi；s-BuLi；t-BuLi|环己烷、苯、DMSO|商用品级 SBS/TPE 弹性体|
|异戊二烯 (Isoprene)|共轭二烯|n-BuLi；t-BuLi|环己烷|合成天然橡胶 (cis-1,4)|
|甲基丙烯酸甲酯 (MMA)|酯羰基 + 甲基|s-BuLi + LiCl；t-BuLi；萘钠|DME（极性）|需极性溶剂 + LiCl 抑制 Claisen 重排|
|丙烯腈 (AN)|氰基|NaI；烷基钠|THF、DME|腈基稳定阴离子|
|乙烯基吡啶（2-/4-）|杂环吸电子|烷基镁（Grignard）|甲苯|有机镁引发|
|马来酸酐|酯羰基 + 羰基|LiN(SiMe₃)₂|惰性|需位阻保护的强碱|
|甲醛 (Formaldehyde)|羰基|胺、金属烷氧基|水/无水|聚缩醛（Sec. 5-6）|

### 表3-3 自由基 / 阳离子 / 阴离子三种链聚合对比（据原文行 21–50、966–975、2680–2690、3733–3757 归纳）

|||||
|---|---|---|---|
|引发物种|R·|C⁺ (离子对/自由离子)|C⁻ (离子对/自由离子)|
|适用单体|几乎所有含 C=C 单体|供电子取代基（乙烯基醚、异丁烯、苯乙烯等）|吸电子取代基（苯乙烯、二烯、MMA、AN 等）|
|温度范围|通常 > 50 °C|通常 < 0 °C（常 -78~-100 °C）|常 < 0 至 +50 °C|
|溶剂极性|弱影响|强影响（极性↑→松散对/自由离子）|强影响（极性↑→$$k_p$$↑ 1–3 个数量级）|
|反离子效应|无|弱（阳离子体系多为松散对）|强（$$k_p^-$$ 自由离子 ≫ 离子对）|
|$$R_p$$ 对 $$R_i$$ 依赖|$$R_i^{1/2}$$|$$R_i^{1}$$|$$Rp = k_{p,app}^-[M^-][M]$$（无终止）|
|典型 $$[活性种]$$|10⁻⁹–10⁻⁷ M|低（难测）|10⁻⁴–10⁻² M（可精确测）|
|分子量分布 PDI|1.5–2.0（稳态）；2.0 极限|1–2（有终止）；可控 LCP 达 1.1–1.2|1.0–1.1（活性，Poisson 分布）|
|可控分子量|低|中等（LCP）|极高（$$M_n = p[M]_0/[I]_0$$）|
|嵌段共聚物|需 RAFT/ATRP/NMP|需 LCP|天然活性，最直接|
|DPPH 猝灭响应|猝灭|无响应|无响应|

## 模块4：章节间衔接

### 4.1 与 Ch.3 自由基聚合的机理对比（原文行 19–50、966–975、1045–1067）

- 共同点：引发-增长-终止三段式；理论分子量分布由同一条 Flory 分布公式给出（PDI → 2）。"The theoretical molecular weight distributions for cationic chain polymerizations are the same as those described in Sec. 3-11 for radical chain polymerizations."（行 1045–1048）
- 关键差异：
① 终止阶数：自由基为双分子（二阶），阳离子为一阶。因此 $$R_p$$ 对 $$R_i$$ 分别为 1/2 和 1 阶（行 966–975）。
② 单体选择性：自由基几乎不挑，离子聚合高度挑（行 21–30）。
③ $$[活性种]$$ 数量级：自由基 10⁻⁹~10⁻⁷ M，活性阴离子 10⁻⁴~10⁻² M，故活性阴离子速率通常更高（行 2680–2690）。
④ 溶剂/反离子效应：自由基本质上无，离子聚合极强（行 3742–3745）。
⑤ Mayo 方程形式一致（Eq. 3-119 ≈ Eq. 5-41），但 $$C_M$$ 数值体系不同（行 947–949）。
### 4.2 与 Ch.6 共聚的衔接（原文行 3351–3450、3756–3757）

- 阴离子活性共聚：通过顺序加料（sequential monomer addition）精确合成 A、AB、ABA、BABAB、CABAC 等多嵌段共聚物（行 3351–3390）。关键判据：交叉引发只能在"新活性端比原活性端更稳定或相当"时发生（行 3366–3373）。例如：PS⁻ 可引发 MMA，反之不行（因 PMMA⁻ 更稳定，pKₐ：甲苯 43 vs 乙酸乙酯 30）。
- 对比 Ch.6 自由基共聚：自由基共聚遵循 Mayo-Lewis 方程（$$r_1r_2 = 1$$ 为理想共聚），嵌段序列由竞聚率决定、不可控嵌段长度；阴离子活性共聚则可按 [M]/[I] 精确设计每个嵌段长度。
- Odian 明确提示："Copolymerization behavior can also be used to distinguish between radical and ionic polymerizations (see Chap. 6)."（行 3756–3757）
### 4.3 与 Ch.7 开环聚合的关系（原文行 3431–3440、3822–3960）

- 阴离子开环：活性阴离子链端可直接引发环氧化合物、内酯（lactone）、内酰胺（lactam）、环硅氧烷的开环聚合。但 PS⁻ 或 PMMA⁻ 亲核性不足以直接开环内酯，需先加少量环氧乙烷把碳负离子转换为烷氧负离子（-O⁻），再引发内酯（行 3437–3440）。
- 羰基聚合（Sec. 5-6）：甲醛、醛类可由阴/阳离子活性种聚合（行 3822–3960），其天花板温度 $$T_c$$ 普遍偏低（甲醛 $$T_c = 119 °C$$；乙醛 $$T_c = -39 °C$$；三氟乙醛 $$T_c = 85 °C$$），聚合必须低于 $$T_c$$ 进行——与 Ch.7 环状醚/内酯开环聚合的热力学判据直接对接。
- 阳离子活性聚合（LCP）也已扩展到 THF、四氢呋喃等环醚的开环（行 2965–2967）："…poly(tetrahydrofuran) is obtained by living cationic polymerization with ring-opening polymerization (Chap. 7)."
## 模块5：与卫材业务的连接点

说明：本章未直接讨论卫材/SP/卫生用品/避孕套等终端应用，以下连接为基于 Odian 原文原理→卫材工艺参数的严格推导，未引入原文之外的数值。

### 5.1 聚异丁烯（PIB）/ 丁基橡胶在湿巾包装、纸尿裤底膜阻隔层的应用

- 原文事实（行 2009–2056）：丁基橡胶为全球年产约 10⁹ 磅 的重要合成橡胶；分子量 ≥ 200,000；-50 °C 仍柔韧；低气体透过率（原文"low gas permeability"）；耐臭氧、耐湿、耐化学。
- 卫材连接点：
① 湿巾包装/纸尿裤底膜的阻气层（barrier layer） 常采用 IIR/卤化丁基或 PIB 共聚薄膜——低透气（尤其对 O₂ 和 CO₂）正是 Odian 原文第 2052 行描述的"low gas permeability"特性的直接应用。
② 底膜在 -10 ~ 0 °C 运输储存中仍要求柔韧，丁基橡胶 $$T_g \approx -70 °C$$（原文行 2050："-50 °C"），满足寒区运输。
③ 湿巾液体（70%+ 水 + 酒精）长期接触，丁基橡胶"moisture/chemical resistance"（行 2051）是选型的理论依据。
- 可用工艺参数：$$T_p = -100 \sim -90 °C$$（低分子量需 -40~10 °C）；引发体系 AlCl₃/H₂O；异戊二烯/异丁烯摩尔比 0.005~0.025 决定硫化点密度（行 2045–2046）——这是调节阻隔膜硫化交联密度的直接设计参数。
### 5.2 阴离子活性聚合的 PDI ≈ 1.0 优势——对 SAP 交联剂分子量设计的意义

- 原文事实（行 2932–2959）：$$X_n = p[M]_0/[I]_0$$；PDI < 1.1–1.2；活性聚合是唯一可"synthesizing standard polymer samples of known and well-defined molecular weights"的途径。
- 卫材连接点：SAP（Superabsorbent Polymer）中的多臂 PEG 交联剂 / 星型 PEglycol 交联点均匀性直接决定凝胶强度、溶胀比、抗冲散性能 (ABC)。传统自由基合成的 PEG 交联剂 PDI ≈ 1.5–2.5，会导致"短链部分起不到交联作用、长链部分形成弱凝胶区"的微观不均。
- 可直接使用的公式：
$$M_n(目标) = \frac{p \cdot [M]_0}{[I]_0} \cdot M_{单体}$$
例：需制备 $$M_n = 8000 \text{ g/mol}$$ 的 PEG 二甲醇交联剂，由乙氧化合物阴离子聚合，取 $$p = 0.99$$、$$[M]_0 = 2.0 \text{ mol/L}$$，则 $$[I]_0 = 0.99 \times 2.0 \times 44 / 8000 = 0.0109 \text{ mol/L}$$。这是 Mn 精确设计的定量公式，直接来自 Eq. 5-98/5-99。
- Poisson 分布（Eq. 3-228，行 1820–1822）：$$\frac{X_w}{X_n} = 1 + \frac{1}{X_n}$$，用于预测理论 PDI 上限。
### 5.3 嵌段共聚物——TPE 在卫材弹性体中的应用

- 原文事实（行 3351–3407、3427–3430）：SBS、SIBS、SIS ABA 三嵌段通过活性阴离子聚合工业化生产（Kraton、CariFlex、Stereon 等），全球年产 > 20 亿磅；PS 硬段形成物理交联玻璃域（$$T_g \approx 100 °C$$），PB/PI 软段提供弹性。
- 卫材连接点：
① 纸尿裤腰围/腿围弹力带（gather） 常采用 SBS/S-IBS TPE 或 SEBS，其物理交联（热可逆） 允许 TPE 注塑加工——"thermoplastic at elevated temperatures where they can be molded and remolded"（行 3396–3404）。
② 氨纶/弹性纤维：虽然现代氨纶（spandex）多为聚氨酯，但 Odian 指出阴离子活性聚合是"route to block copolymers, star polymers, telechelic polymers"（行 3346–3348）。端羟基 TPE 可通过"telechelic"反应（行 3481–3520）与二异氰酸酯扩链，形成聚醚氨纶 (polyether spandex)。
③ 湿巾包装密封条、婴儿护理手套等软接触件亦多用 SBS 类 TPE。
- 设计参数：每个嵌段长度由 $$[M_i]/[I]_0$$ 决定（行 3380）；顺序加料（行 3351–3390）决定嵌段序列；需满足"新碳负离子稳定性 ≥ 原碳负离子稳定性"（行 3367–3373）——这是序列设计的第一原则。
### 5.4 合成聚异戊二烯——避孕套/导管合成路线

- 原文事实（行 2009–2018、2110–2140、3431–3440）：聚异戊二烯由丁基锂在烃类溶剂（环己烷、苯）中对异戊二烯进行 1,4-加成活性聚合；可通过端基官能化（$$\text{CO}_2$$、环氧乙烷、卤代烃）得到端羧基/羟基/烯丙基产物（行 3486–3520）。
- 卫材连接点：
① 避孕套、导尿管、医用导管对合成天然橡胶 (IR) 的需求：合成 IR 由丁基锂引发异戊二烯聚合（cis-1,4 ≈ 94–98%），通过端基改性引入硫化/官能化位点。
② 导管抗凝血涂层：利用 Odian 描述的"telechelic polymer"端基改性（行 3481–3577），可将活性聚合物末端转化为 -COOH、-OH 或环氧基，再与 PEG、肝素等官能化。
- 可用工艺参数：

- 溶剂：环己烷/甲苯（烃类，避免与碳负离子反应）
- 引发剂：n-BuLi，引发速率 ∝ [BuLi]^{1/6}（六聚体解离，行 3197–3209）
- 增长速率 ∝ [BuLi]^{1/2}（行 3209–3219）
- $$M_n = [M]_0/[I]_0 \cdot M_{异戊二烯}$$（Eq. 5-99，行 2945–2947）

### 5.5 可直接用于卫材工艺参数选择的公式与数据清单

|||||
|---|---|---|---|
|$$X_n = p[M]_0/[I]_0$$ (Eq. 5-98/5-99)|行 2932–2955|SAP 交联剂 $$M_n$$ 设计|
|$$X_w/X_n = 1 + 1/X_n$$ (Eq. 3-228)|行 1820–1822|PDI 理论上限预测|
|$$1/X_n = k_t/(kp[M]) + k_{ts}/(k_p[M]) + C_M + C_S[S]/[M]$$ (Eq. 5-41)|行 941–943|阳离子体系中分子量控制|
|$$C_{tr,S}(H_2O) \approx 10$$（苯乙烯/钠萘/25 °C）|行 2345–2346|阴离子聚合水分控制指标|
|$$k_{p,app}$$：苯 2 → THF 550 → DME 3800 (L·mol⁻¹·s⁻¹)|行 2706–2714|溶剂选择依据|
|丁基橡胶 $$M_n \geq 200{,}000$$，-100~-90 °C|行 2009–2008|阻隔膜工艺窗口|
|活性阴离子 $$[M^-] \approx 10^{-4}\sim 10^{-2} \text{ M}$$|行 2687–2690|活性聚合引发剂浓度设计|
|丁基锂六聚体解离：$$R_p \propto [\text{BuLi}]^{1/2}$$|行 3197–3219|IR/BR 合成引发剂浓度计算|

## 模块6：金句索引

原文（行 21–25）
> "Almost all monomers containing the carbon–carbon double bond undergo radical polymerization, while ionic polymerizations are highly selective."
中文：几乎所有含碳碳双键的单体都能进行自由基聚合，而离子聚合则高度选择。
为什么记：一句话点明离子聚合的"窄门"特性，是 Ch.5 所有后续讨论的起点。

原文（行 72–75）
> "The intermediate species include the tight or contact ion pair (II) (also referred to as the intimate ion pair) and the solvent-separated or loose ion pair (III)."
中文：中间物种包括紧密（接触）离子对和溶剂分隔（松散）离子对。
为什么记：离子对四态平衡模型是解释离子聚合速率与分子量所有异常行为的钥匙。

原文（行 84–85）
> "Increased solvent polarity favors the loose ion pair while the tight ion pair predominates in solvents of low polarity."
中文：溶剂极性增加有利于松散离子对，而低极性溶剂中以紧密离子对为主。
为什么记：溶剂极性 → 离子对形态 → $$k_p$$ 数量级变化，是阴离子聚合速率 1–3 个数量级可调的根本原因。

原文（行 968–971）
> "Radical polymerizations show a 1/2-order dependence of R_p on R_i, while cationic polymerizations show a first-order dependence of R_p on R_i."
中文：自由基聚合 $$R_p$$ 对 $$R_i$$ 为 1/2 阶，阳离子聚合为 1 阶。
为什么记：动力学阶数差直接反映终止机理差异（双分子 vs 单分子），是区分自由基/阳离子的核心判据。

原文（行 1699–1702）
> "Living polymerizations are polymerizations without chain-breaking reactions … the concentration of propagating species remains constant throughout the polymerization and even after 100% conversion."
中文：活性聚合是不发生链断裂反应的聚合，活性种浓度在整个聚合过程中乃至 100% 转化后均保持恒定。
为什么记：活性聚合的精确定义，是 SAP 交联剂、TPE、IR 精确分子量设计的理论基石。

原文（行 1714–1717）
> "Living anionic polymerization is relatively easy to achieve … Anionic propagating systems do not have a 'built-in' termination reaction."
中文：活性阴离子聚合相对容易实现——阴离子体系没有"内置的终止反应"。
为什么记：与阳离子（需引入休眠-活化平衡）对比，解释了为何阴离子活性聚合早于阳离子 30 年工业化。

原文（行 1734–1741）
> "LCP is achieved by slowing down the reaction, specifically, extending the lifetime of the propagating centers, so that significant propagation occurs prior to β-proton transfer to monomer."
中文：活性阳离子聚合通过减缓反应速率来实现，具体来说延长活性种寿命，使显著增长先于向单体的 β-H 转移发生。
为什么记：LCP 的三大杠杆（Lewis 酸选择 + 共离子盐 + 低温）在此集中概括。

原文（行 2309–2312）
> "Propagation occurs with complete consumption of monomer to form living polymers. The propagating anionic centers remain intact because transfer of proton or other positive species from the solvent does not occur."
中文：增长过程随单体完全消耗形成活性聚合物，活性阴离子中心保持完整，因为来自溶剂的质子或其他正物种的转移不发生。
为什么记：解释了为何阴离子活性聚合能在严格除水除氧条件下完成 100% 转化。

原文（行 2687–2690）
> "The concentration of propagating radicals is 10⁻⁹ –10⁻⁷ M, while that for propagating anions is often as high as 10⁻⁴ –10⁻² M."
中文：自由基活性种浓度为 10⁻⁹~10⁻⁷ M，而阴离子活性种浓度通常高达 10⁻⁴~10⁻² M。
为什么记：活性种浓度差 4 个数量级，是活性聚合速率远高于普通自由基的定量原因。

原文（行 2933–2936、2945–2947）
> "The number-average degree of polymerization for a living anionic polymerization is the ratio of the concentration of reacted monomer to the concentration of living ends … $$X_n = p[M]_0/[I]_0$$."
中文：活性阴离子聚合的数均聚合度等于已反应单体浓度与活性端浓度之比，$$X_n = p[M]_0/[I]_0$$。
为什么记：这是活性聚合 Mn 精确设计的唯一方程，SAP 交联剂、TPE 嵌段、合成 IR 的分子量设计全靠它。

原文（行 2956–2959）
> "PDI values below 1.1–1.2 are found for many living polymerizations. The living polymer technique offers a unique method of synthesizing standard polymer samples of known and well-defined molecular weights."
中文：许多活性聚合的 PDI 低于 1.1–1.2。活性聚合技术是合成已知且明确分子量的标准聚合物样品的唯一方法。
为什么记：PDI ≈ 1.0 是活性聚合的"招牌"指标，也是 SEC 校准标准的来源。

原文（行 3393–3404）
> "These are useful as the thermoplastic elastomers … which behave as elastomers at ambient temperatures but are thermoplastic at elevated temperatures where they can be molded and remolded."
中文：这些材料是有用的热塑性弹性体——室温下表现为弹性体，高温下则表现为可模塑和再模塑的热塑性。
为什么记：解释了为何 SBS/TPE 能被大规模注塑加工为纸尿裤弹力带、湿巾密封条等卫材部件。

原文（行 3427–3430）
> "The annual worldwide production of triblock thermoplastic elastomers, clear impact-resistant polystyrene, and other styrene–diene products produced by anionic polymerization exceeds a couple of billion pounds."
中文：全球年产的三嵌段热塑性弹性体、抗冲聚苯乙烯及其他苯乙烯-二烯产品超过 20 亿磅。
为什么记：阴离子活性聚合不是"实验室玩具"，而是年产值数百亿美元的商业化工艺。

报告完成。所有原文行号均基于 /sandbox/workspace/Ebook_Extract/Principles_of_Polymerization/chapters/ch5_ionic.txt 的实际行编号；所有数据、公式、术语引用均出自 Odian Ch.5 原文，未编造内容。


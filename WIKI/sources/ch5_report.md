---
type: source
title: "ch5_report.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch5_report.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
key_claims: []
pages_linked: []
compile_mode: extractive
---

# ch5_report.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch5_report.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

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
"The number-average degree of polymerization for a living anionic polymerization is the ratio of the concentration of reacted monomer to

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch5_report.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch5_report.md.md`
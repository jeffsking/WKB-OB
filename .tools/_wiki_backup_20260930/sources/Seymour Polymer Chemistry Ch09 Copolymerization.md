---
type: source
title: "Seymour Polymer Chemistry Ch09 Copolymerization"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Seymour Polymer Chemistry/chapters/Seymour Polymer Chemistry_ch09.md.md"
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Copolymers may be alternating, random, block, or graft copolymers; copolymer composition is governed by the reactivity ratios r₁ = k₁₁/k₁₂ and r₂ = k₂₂/k₂₁, not simply by the feed ratio."
  - "Copolymer composition equation: d[M₁]/d[M₂] = [M₁]/[M₂] × (r₁[M₁] + [M₂]) / ([M₁] + r₂[M₂]); when copolymer composition n equals feed composition x the product is an azeotropic copolymer."
  - "The Alfrey–Price Q–e scheme (1947) predicts reactivity ratios: r₁ = (Q₁/Q₂)exp[−e₁(e₁−e₂)] and r₂ = (Q₂/Q₁)exp[−e₂(e₂−e₁)], where Q reflects resonance stability of the macroradical and e reflects monomer polarity."
  - "Representative reactivity ratios at 60 °C (Table 9.1): styrene/maleic anhydride r₁ = 0.04, r₂ = 0.02 (r₁r₂ = 0.0008, strictly alternating); styrene/butadiene r₁ = 1.39, r₂ = 0.78 (r₁r₂ = 1.08, near ideal); MMA/styrene r₁ = r₂ = 0.50."
  - "SBS block copolymers differ from the structurally related random copolymer SBR: styrene domains act as physical crosslinks, while random SBR requires chemical crosslinking; dynamic vulcanization gives a finely dispersed discontinuous crosslinked elastomer phase (TPV)."
  - "Worldwide sales of thermoplastic elastomers are on the order of one and a half million tons with a value of about $5 billion; over 8 million tons of SBR were produced worldwide in 1995."
summary_cn: "第9章讲共聚：以竞聚率 r₁/r₂ 与共聚物组成方程、Alfrey-Price Q-e 预测方案为定量骨架，区分交替/无规/嵌段/接枝四类序列，并落到 SBR、ABS、EPM/EPDM、离子聚合物与热塑性弹性体（含 Spandex 氨纶）的分子设计。"
tags: ["source/book", "copolymerization", "reactivity-ratio", "Q-e-scheme", "block-copolymer", "graft-copolymer", "TPE", "SBS", "SBR", "ionomer"]
tags_zh: ["共聚", "竞聚率", "Q-e方案", "嵌段共聚物", "接枝共聚物", "热塑性弹性体", "离子聚合物", "氨纶"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Seymour Polymer Chemistry Ch02 Polymer Structure and Morphology]]", "[[Seymour Polymer Chemistry Ch07 Ionic and Coordinative Chain Polymerization]]", "[[Seymour Polymer Chemistry Ch08 Free Radical Chain Polymerization]]", "[[Acrylic-Based Superabsorbent Polymers]]", "[[A review on superabsorbent polymers]]"]
---

# Seymour Polymer Chemistry Ch09 Copolymerization

> Source: Seymour/Carraher, *Polymer Chemistry*, Ch.9 — Copolymerization（共聚）.
> Citation convention 引用约定: 源文件为 .txt 抽取件，**无正式印张页码**，本页以源文件行号（line no.）定位；原书页码缺失处标注 [待验证]。

## Executive Summary 内容概要

Chapter 9 elevates copolymerization（共聚）from "mixing two homopolymers" to **controlled sequence design（可控序列设计）**: sequence classification → reactivity-ratio kinetics → Q–e semi-quantitative prediction → commercial copolymers → thermoplastic elastomer (TPE) molecular design. 对卫材的意义有两条主线：**SAP 本质是交联共聚物（丙烯酸 + 双官能团交联剂）**，其组成由竞聚率而非投料比决定；**弹性腰围/防漏侧边用的弹性纤维与 TPE** 直接落在本章 §9.4。

## Sequence Architecture 共聚物序列分类

> *"Copolymers may be alternating copolymers... random copolymers... block copolymers... or graft copolymers"* (line 49)

| 序列类型 Type | 中文 | 结构特征 Feature | 合成策略 Route |
|---|---|---|---|
| Alternating 交替 | 交替共聚物 | ABABAB 严格交替 | 电荷转移络合物；r₁, r₂ → 0 |
| Random 无规 | 无规共聚物 | 序列随机，服从统计分布 | 自由基共聚，r₁r₂ → 1 |
| Block 嵌段 | 嵌段共聚物 | 长 A 段 + 长 B 段 | 活性聚合（living），见 Ch.07 |
| Graft 接枝 | 接枝共聚物 | 主链 A + 支链 B | 主链接枝 / 大单体法 |

## Reactivity Ratios and Composition 竞聚率与共聚物组成

> **r₁ = k₁₁/k₁₂ 与 r₂ = k₂₂/k₂₁** (line 54) — 竞聚率是「同单体自聚速率常数」与「交叉增长速率常数」之比。

| r₁ 取值 Value | 物理含义 Meaning | 中文 |
|---|---|---|
| r₁ = 1 | M₁⋅ 对两单体无选择性 | 理想无规 |
| r₁ > 1 | M₁⋅ 倾向与自身单体反应 | 自聚序列倾向 |
| r₁ < 1 | M₁⋅ 倾向与 M₂ 反应 | 交替倾向 |
| r₁ = 0 | M₁⋅ 不与 M₁ 反应（r₂ = 0 时为完美交替） | 严格交替 |

**共聚物组成方程 Copolymer composition equation**：

> **d[M₁]/d[M₂] = [M₁]/[M₂] × (r₁[M₁] + [M₂]) / ([M₁] + r₂[M₂])** (line 59)

**Composition drift 组成漂移**：*"the composition of the copolymer (n) may be different from that of the reactant mixture or feed (x)."* (line 64) — 两种单体消耗速率不同，进料组成随转化率变化，共聚物组成随之漂移，这是工业上必须做**单体补加（semi-batch feed）**的原因。

**Azeotropic copolymer 共沸共聚物**：*"When x equals n, the product is said to be an azeotropic copolymer."* (line 69)

**极限判据 Limiting cases**：

| 判据 Criterion | 序列倾向 Tendency | 中文 |
|---|---|---|
| r₁r₂ = 1 | Ideal copolymer 理想共聚（无规） | 两单体选择性相当 |
| r₁ ≈ r₂ ≈ 0 | Alternating 交替 | 交叉增长远快于自聚 |
| r₁r₂ → 0 | 交替趋势 | — |
| r₁r₂ → 1 | 无规趋势 | — |

> 原文提示该判据为经验性：*"The value of r₁r₂ for most copolymerizations is between 1 and 0, and thus this value may be used with discretion for estimating the extent of randomness in a copolymer."* (line 174)

Table 9.1 — Typical Free Radical Chain Copolymerization Reactivity Ratios at 60 °C（line 220-412，部分）：

| 单体 M₁ | 单体 M₂ | r₁ | r₂ | r₁r₂ | 序列判定 |
|---|---|---|---|---|---|
| Styrene 苯乙烯 | Maleic anhydride 马来酸酐 | 0.04 | 0.02 | 0.0008 | 严格交替 strictly alternating |
| Styrene | Acrylonitrile 丙烯腈 | 0.41 | 0.04 | 0.016 | 交替倾向 |
| Styrene | Butadiene 丁二烯 | 1.39 | 0.78 | 1.08 | 接近理想 near ideal |
| Chlorotrifluoroethylene | Tetrafluoroethylene | 1.0 | 1.0 | 1.0 | 完美理想 |
| Methyl methacrylate MMA | Styrene | 0.50 | 0.50 | 0.25 | 无规 |

## The Q–e Scheme（Alfrey–Price, 1947）

> *"A useful scheme for predicting r₁ and r₂ values for free radical copolymerizations was proposed by Alfrey and Price in 1947."* (line 82)

> **r₁ = (Q₁/Q₂)·exp[−e₁(e₁ − e₂)]**；**r₂ = (Q₂/Q₁)·exp[−e₂(e₂ − e₁)]** (line 87-88)

> *"the reactivity is related to resonance stability of the macroradical M₁⋅, the composition of the copolymer is related to the relative polarity of the two monomers M₁ and M₂."* (line 101)

Table 9.2 — **Q（共振因子 resonance factor）** 与 **e（极性因子 polarity factor）**（line 502-577）：

| 单体 Monomer | Q | e | 中文 |
|---|---|---|---|
| Styrene 苯乙烯 | 1.00 | −0.80 | 自由基共振稳定，富电子 |
| Acrylonitrile 丙烯腈 | 0.60 | 1.20 | 强吸电子、缺电子 |
| Methyl methacrylate MMA | 0.74 | 0.40 | 中等极性 |
| Vinyl acetate 醋酸乙烯酯 | 0.026 | −0.22 | 自由基不稳定、活性低 |
| Acrylic acid 丙烯酸 | 0.40 | 0.60 | **SAP 主单体** |
| Maleic anhydride 马来酸酐 | 0.10 | −0.70 | 1,2-二取代，不自聚 |

**设计规则**：e 值差异大的单体对（如丙烯腈 e = +1.20 与苯乙烯 e = −0.80）倾向交替；e 值相近者倾向无规（line 189）。

**Charge-transfer complex 电荷转移络合物**：*"It is now believed that a charge-transfer complex is the active species in alternating copolymerization."* (line 193) — 解释了为什么马来酸酐这类「本身不聚合」的 1,2-二取代单体仍能参与严格交替共聚。

## Commercial Copolymers 商业共聚物

- **SBR（styrene-butadiene rubber 丁苯橡胶）**：*"Over 8 million tons of SBR were produced worldwide in 1995."* (line 110)；*"Often preferred because of its greater uniformity and cleanliness"* (line 211) —— 一致性与纯净度优于天然橡胶，但耐磨与回弹略逊。
- **ABS**：*"A widely used plastic (ABS) is a copolymer or blend of polymers of acrylonitrile, butadiene, and styrene."* (line 114)
- **SAN（styrene-acrylonitrile）**：耐化学性优于 PS (line 118)。
- **Vinylite（VYHH）**：氯乙烯 87%–醋酸乙烯酯 13% 共聚物，1928 年引入 (line 121)。
- **Ionomers 离子聚合物**：*"Copolymers of ethylene and methacrylic acid (ionomers) also have good adhesive properties and transparency."* (line 124) — 加入 Zn/Li/Na 金属盐后，室温呈热固性而加工温度下呈热塑性。
- **EPM / EPDM**：*"EPMs are produced by solution polymerization employing Ziegler-Natta catalysts."* (line 129)；EPDM 含 3–9% 二烯烃以供硫化 (line 130)。
- **Spandex（氨纶）**：*"A special fiber called Spandex is a block copolymer of a stiff polyurethane and a flexible polyester."* (line 133)

## Thermoplastic Elastomers 热塑性弹性体

> *"Thermoplastic elastomers contain two or more distinct phases and their properties depend on these phases being intimately mixed and small."* (line 139)

| 实现策略 Strategy | 中文 | 代表 Examples |
|---|---|---|
| Block copolymer 嵌段共聚 | 硬-软段嵌段 | SBS（Kraton）、SIS、SEBS |
| Graft copolymer 接枝共聚 | 软主链 + 硬支链 | Table 9.5 [数据未在本源文件内展开] |
| Physical blend + dynamic vulcanization 物理共混/动态硫化 | 热塑性相 + 硫化橡胶相 | PP/EPDM TPV |

**硬-软段设计 Hard/soft segment design**（line 199-204）：

- 硬段（high Tg / high Tm）在使用温度下为固态 → **物理交联点 physical crosslinks**；
- 软段（low Tg）在使用温度下为橡胶态 → 提供弹性；
- **Microphase separation 微相分离**：硬段聚集为微区（domain），软段构成连续相；
- 加工原理：加热至硬段 Tm 以上 → 物理交联解离 → 可流动加工 → 冷却后硬段微区重建 → 恢复弹性。

**SBS vs SBR —— 结构决定性能的经典案例**：

> *"Styrene-butadiene-styrene (SBS) block copolymers differ from the structurally related random copolymer of styrene and butadiene (SBR)."* (line 149)

| 对比维度 | SBS（嵌段） | SBR（无规） |
|---|---|---|
| 交联方式 | 苯乙烯玻璃态微区（Tg ≈ 100 °C）作物理交联 | 需化学交联（硫化） |
| 加工性 | 热塑性，可重复加工 | 热固性橡胶，不可重复加工 |

**动态硫化 Dynamic vulcanization**：*"At times the phases are crossedlinked during the mechanical mixing. This process is referred to as 'dynamic vulcanization' and produces a finely dispersed discontinuous crosslinked elastomer phase."* (line 154)

**市场规模**：*"Worldwide sales of thermoplastic elastomers are on the order of one and a half million tons with a value of about $5 billion."* (line 159) — 约 150 万吨 / 约 50 亿美元（原文未给出统计年份，[待验证]）。

## Methodology Critique 方法论批判

- **Q–e 方案是半定量的**：它把竞聚率拆成共振项与极性项两个参数，忽略了位阻（steric）与电荷转移络合物的贡献；对严格交替体系（如苯乙烯/马来酸酐）预测偏差最大。
- **Mayo–Lewis 方程的简化写法易被误引**：源文件 §7.2 公式汇总将组成方程简写为 "d[M₁]/d[M₂] = M₁/(M₂)"（line 299），与 §9.1 的完整式（line 59）不等价；**引用时必须使用完整式**。
- **年份口径混杂**：SBR 800 万吨对应 1995 年（line 110），TPE 150 万吨未标年份（line 159），两者不可直接比较。
- **r₁r₂ 判据的局限**：原文自称 "with discretion"，r₁r₂ 只在同一反应条件（温度、溶剂、引发方式）下可比，温度改变会显著改变 r 值。

## Hygiene Implication 卫材关联

- **SAP 是交联共聚物，组成由竞聚率决定**：SAP 合成中丙烯酸（AA, Q = 0.40 / e = 0.60，line 97）为主单体，双官能团交联剂（如 N,N′-methylenebisacrylamide, MBA）与功能单体（如 AMPS）为共聚单体。因 AA 的均聚倾向强，AA 含量通常占绝对多数；**组成漂移（composition drift）意味着不加控制的批次投料会导致产物组成随转化率漂移**，这是 SAP 批次稳定性（CRC/AAP 波动）的分子层根源之一。
- **离子聚合物的物理交联原理可类比 SAP**：原文指出乙烯-甲基丙烯酸离聚物靠金属离子簇形成物理交联点，室温呈热固性、加工温度下呈热塑性（line 124-126）。SAP 中部分中和的羧酸钠同样形成离子缔合区，与化学交联共同决定凝胶模量与保水量。
- **弹性纤维与 TPE 直接对应卫材弹性件**：Spandex（聚氨酯-聚酯嵌段共聚物，line 133）与 SBS/SEBS 类 TPE 是纸尿裤弹性腰围、防漏侧边、弹性耳贴的材料基础；硬-软段微相分离（line 199-204）决定了弹性回复与耐热蠕变，也决定了热熔胶粘接与 ultrasonic bonding 时的热敏感窗口。
- **PP 抗冲改性与共混**：PP/EPDM 动态硫化 TPV（line 154, 286）属本章物理共混策略；PP 本身为配位聚合产物（见 Ch.07），其共聚改性（乙烯-丙烯无规/嵌段共聚）直接改变纺粘-熔喷纤维的柔顺性与熔点。

## Related Sources 关联来源

- [[Seymour Polymer Chemistry Ch02 Polymer Structure and Morphology]]
- [[Seymour Polymer Chemistry Ch07 Ionic and Coordinative Chain Polymerization]]
- [[Seymour Polymer Chemistry Ch08 Free Radical Chain Polymerization]]
- [[Acrylic-Based Superabsorbent Polymers]]
- [[A review on superabsorbent polymers]]

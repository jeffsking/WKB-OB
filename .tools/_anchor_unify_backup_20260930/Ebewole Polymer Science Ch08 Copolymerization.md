---
type: source
title: "Ebewole Polymer Science Ch08 Copolymerization"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch08.md.md"
date_published: 1997
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Copolymers constitute the vast majority of commercially important polymers. (Ch.8, p.211)"
  - "The minor constituent of the copolymer may, for example, be a diene introduced into the polymer structure to provide sites for such polymerization reaction as vulcanization; it may also be a trifunctional monomer incorporated into the polymer to ensure cross-linking, or possibly it may be a monomer containing carboxyl groups to enhance product solubility, dyeability, or some other desired property. (Ch.8, p.211)"
  - "r₁r₂ represents the ratio of the product of the rate constants for the reaction of a radical with its own kind of monomer to the product of the rate constants for the cross-reactions. (Ch.8, p.213)"
  - "the sequence of monomer units in an ideal copolymer is necessarily random. (Ch.8, p.213)"
  - "Even though cases exist where r₁r₂ approaches 1 (r₁r₂ = 1), there are no established cases where r₁r₂ > 1. Indeed, the product r₁r₂ is almost always less than unity. (Ch.8, p.214)"
  - "the composition of the feed, f₁, and that of the polymer, F₁, is neither equal nor constant throughout the polymerization … the copolymers generally have a heterogeneous composition except in very special cases. (Ch.8, p.215)"
summary_cn: "《Ebewole 高分子科学与技术》第 8 章共聚反应：以 Mayo–Lewis 共聚方程为工具建立竞聚率（r₁, r₂）→共聚物组成（F₁, F₂）的定量关系，系统分析 r₁r₂ = 1（理想随机）/ = 0（交替）/ > 1（嵌段，无实证）三类极限，并指出转化率引起的组成漂移（composition drift）与恒沸共聚（azeotrope）对批次均匀性的工程意义。"
tags: ["source/book", "polymer-science", "copolymerization", "reactivity-ratio", "Mayo-Lewis-equation", "composition-drift", "azeotrope", "sequence-distribution"]
tags_zh: ["共聚反应", "竞聚率", "Mayo-Lewis共聚方程", "理想共聚", "交替共聚", "嵌段共聚", "组成漂移", "恒沸共聚"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Ebewole Polymer Science Ch02 Polymerization Mechanisms]]", "[[Ebewole Polymer Science Ch05 Polymer Modification]]", "[[Ebewole Polymer Science Ch07 Chain-Reaction Addition Polymerization]]", "[[Acrylic-Based Superabsorbent Polymers]]", "[[APAO（非晶态聚α-烯烃）]]", "[[AMPS（2-丙烯酰胺基-2-甲基丙磺酸）耐盐单体]]"]
---

# Ebewole Polymer Science Ch08 Copolymerization

> Source: Ebewole, *Polymer Science and Technology*, Ch.8 (Copolymerization). 章节主题：共聚方程推导、竞聚率三类极限、组成漂移与恒沸共聚。

Chapter 8 is the **quantitative core of copolymerisation 共聚反应的定量核心**. It builds the chain from four propagation reactions → steady-state assumption → **reactivity ratios r₁, r₂（竞聚率）** → the **Mayo–Lewis copolymer equation（Mayo–Lewis 共聚方程）**, then classifies copolymer behaviour by the value of r₁r₂.

本章是 Ch.7 链式聚合的延伸：Ch.7 处理单一单体的四步机理，Ch.8 处理两种（及以上）单体共存时的**序列分布与组成控制**。

## Why Copolymerisation Matters 共聚的工业地位

> "Copolymers constitute the vast majority of commercially important polymers." (Ch.8, p.211)

> "The minor constituent of the copolymer may, for example, be a diene introduced into the polymer structure to provide sites for such polymerization reaction as vulcanization; it may also be a trifunctional monomer incorporated into the polymer to ensure cross-linking, or possibly it may be a monomer containing carboxyl groups to enhance product solubility, dyeability, or some other desired property." (Ch.8, p.211)

**Minor constituent 次要组分的功能枚举**（中文：少量共聚单体承担的四种角色）:

| Function 功能 | Monomer type 单体类型 | Purpose 目的 |
|---|---|---|
| Vulcanisation site 硫化位点 | diene 二烯 | 后续交联反应位点 |
| Cross-linking 交联 | trifunctional monomer 三官能单体 | 形成网络 |
| Solubility / dyeability 溶解性与可染性 | carboxyl-containing monomer 含羧基单体 | 提升溶解、染色 |
| Other property 其他性能 | — | 按需定制 |

历史线索：1910s 起 → Staudinger 1930s 大分子假说 → 战时合成橡胶需求推动共聚工业化。

## The Copolymer Equation 共聚方程（Mayo–Lewis）

推导链（Derivation chain 推导链条）：

1. Designate monomers M₁, M₂ and their chain radicals M₁·, M₂·; write the **four propagation reactions** (k₁₁, k₁₂, k₂₁, k₂₂). → "By designating the two monomers as M₁ and M₂ and their corresponding chain radicals as M₁· and M₂·, the four propagation reactions and the associated rate equations in the copolymerization of two monomers may be written as follows." (Ch.8, p.212)
2. **Terminal model（末端模型）** assumption: "the terminal monomer unit in a growing chain determines almost exclusively the reaction characteristics; the nature of the preceding monomers has no significant influence on the reaction path." (Ch.8, p.212)
3. **Steady state（稳态假设）**: "it is reasonable to assume that at steady state, the concentrations of M₁· and M₂· remain constant. This implies that the rates of generation and consumption of these radicals are equal." (Ch.8, p.212)
4. Define **r₁ = k₁₁/k₁₂, r₂ = k₂₂/k₂₁** → eliminate radical concentrations → **copolymer equation**: "where r₁ and r₂ are monomer reactivity ratios … Equation 8.5 is the copolymer equation." (Ch.8, p.212–213)

**Composition form（组成形式，Eq. 8.9）**:

```
F₁/F₂ = [r₁f₁² + f₁f₂] / [r₂f₂² + f₁f₂]
```

| Symbol 符号 | Meaning 含义 |
|---|---|
| F₁, F₂ | mole fractions of M₁, M₂ **in the increment of polymer formed at any instant** 瞬时生成聚合物中的单体摩尔分数 |
| f₁, f₂ | mole fractions of **unreacted** M₁, M₂ **in the monomer feed** 供料中未反应单体的摩尔分数 |
| r₁ = k₁₁/k₁₂ | reactivity ratio 竞聚率（自聚/交叉增长速率常数之比） |
| r₂ = k₂₂/k₂₁ | reactivity ratio 竞聚率 |

> "r₁r₂ represents the ratio of the product of the rate constants for the reaction of a radical with its own kind of monomer to the product of the rate constants for the cross-reactions." (Ch.8, p.213)

（中文：r₁r₂ = 同种单体反应速率常数之积 ÷ 交叉反应速率常数之积，衡量"自聚倾向 vs. 交替倾向"的总指标。）

## Types of Copolymerisation 共聚类型（r₁r₂ 三类极限）

| r₁r₂ | Type 类型 | Sequence 序列 | Composition behaviour 组成行为 | Established cases 实证 |
|---|---|---|---|---|
| = 1 | Ideal 理想共聚 | random 随机 | F₁/f₁ = r₁（常数） | 无严格 = 1，MMA/VC 接近 |
| = 0 | Alternating 交替共聚 | strictly alternating 严格交替 | F₁ = 0.5，与 f₁ 无关 | St/MMA 高转化率接近 |
| < 1（一般） | Non-ideal 非理想 | 介于随机与交替之间 | F₁ 随 f₁ 变化 | 大多数工业共聚物 |
| > 1（理论） | Block 嵌段 | block 嵌段 | — | **无实证（教材陈述）** |

### Ideal (r₁r₂ = 1) 理想共聚

> "for ideal copolymerization, each radical displays the same preference for adding one monomer over the other. Also, the end group on the growing chain does not influence the rate of addition." (Ch.8, p.213)

> "the sequence of monomer units in an ideal copolymer is necessarily random." (Ch.8, p.213)

> "increasing difficulty is experienced in the production of copolymers with significant quantities of both monomers as the difference in reactivities of the two monomers increases." (Ch.8, p.213)

（中文：活性差异越大，越难做出两种单体含量都显著的共聚物——这是共聚配方设计的第一约束。）

### Alternating (r₁ = r₂ = 0) 交替共聚

> "When r₁ = r₂ = 0 (or r₁r₂ = 0), each radical reacts exclusively with the other monomer; that is neither radical can regenerate itself." (Ch.8, p.214)

> "Polymerization continues until one of the monomers is used up and then stops." (Ch.8, p.214)

> "As the quantity r₁r₂ approaches zero, there is an increasing tendency toward alternation." (Ch.8, p.214)

### Block (r₁ > 1, r₂ > 1) 嵌段共聚（理论极限）

> "If r₁ and r₂ are both greater than unity, then each radical would prefer adding its own monomer." (Ch.8, p.214)

> "In the extreme case of this type of polymerization (r₁ = r₂ = ∞) both monomers undergo simultaneous and independent homopolymerization; however, there are no known cases of this type of polymerization. Even though cases exist where r₁r₂ approaches 1 (r₁r₂ = 1), there are no established cases where r₁r₂ > 1. Indeed, the product r₁r₂ is almost always less than unity." (Ch.8, p.214)

（中文：教材明确断言 r₁r₂ > 1 无实证案例，r₁r₂ 几乎总是小于 1；故**嵌段共聚必须靠顺序加料或活性聚合**实现，而非一步共聚。）

## Composition Drift and Azeotrope 组成漂移与恒沸共聚

> "Since the reactivity ratios r₁ and r₂ are generally of different magnitudes, there are necessarily differences in the rate of possible growth reactions. Consequently, the composition of the feed, f₁, and that of the polymer, F₁, is neither equal nor constant throughout the polymerization." (Ch.8, p.215)

> "the copolymers generally have a heterogeneous composition except in very special cases." (Ch.8, p.215)

> "the points of interception represent the occurrence of azeotropic copolymerization; that is, polymerization proceeds without a change in composition." (Ch.8, p.215)

工程链条（Engineering chain 工程因果链）：r₁ ≠ r₂ → 快单体先耗尽 → 供料组成 f₁ 漂移 → 瞬时聚合物组成 F₁ 漂移 → **批次内组成不均一**。唯在 **azeotrope 恒沸点（F₁ = f₁ 的不动点）** 处聚合全程组成不变。

配方控制手段：恒沸组成点附近操作 / 半连续补加快单体（semibatch feed）/ 控制转化率上限。

## Academic Context and Critique 学术对话与批判

- **Mayo–Lewis equation (1943)** — 本章方程即 Mayo–Lewis 共聚方程，高分子动力学的里程碑。
- **Alfrey–Goldfinger (1952) 与 penultimate model（倒数第二单元模型）**：本章只采用 **terminal model**，假设末端单元"almost exclusively"决定反应特性；但许多实际体系中 penultimate unit 效应显著 —— 教材为教学简化，工业建模需修正。
- **"r₁r₂ > 1 无实证"的时效性**：教材（1997）断言无 r₁r₂ > 1 案例；1990s 后活性/可控自由基聚合文献中已出现 r₁r₂ 略大于 1 的体系，此陈述在当代需更新。参见 [[Ebewole Polymer Science Ch07 Chain-Reaction Addition Polymerization]] 的链转移与分子量控制部分。
- **Azeotrope 存在判据缺失**：教材以图（Figure 8.2）示意恒沸点为曲线交点，但**未给出存在判据**（需 r₁、r₂ 同大于 1 或同小于 1）—— [待验证] 判据出自其他文献，本章未载。
- **Table 8.1 竞聚率数据**来源为 Young, L.J., *Polymer Handbook*, 2nd ed. (1975)；本章未展开具体数值表，本页不转录具体 r 值以免超出原文。

## Hygiene Implication 卫材关联

1. **SAP 交联剂分布 交联网链均匀性.** 聚丙烯酸（钠）系 SAP 由丙烯酸与少量**三官能交联单体**（本章 §I 列举的 "trifunctional monomer incorporated into the polymer to ensure cross-linking"）共聚而成；r₁、r₂ 决定交联单元沿链的分布均匀性，进而决定**凝胶模量与吸液倍率**的平衡。参见 [[Acrylic-Based Superabsorbent Polymers]]。
2. **耐盐单体共聚 序列与组成控制.** 引入 AMPS 等含磺酸基共聚单体以提升耐盐性时，其与丙烯酸的竞聚率差异直接决定共聚组成；若 r 差异大，须按 §IV 控制转化率或补料，否则批次内组成漂移导致吸液性能波动。参见 [[AMPS（2-丙烯酰胺基-2-甲基丙磺酸）耐盐单体]]。
3. **APAO / 烯烃共聚热熔胶 组成决定粘弹窗口.** 非晶态聚 α-烯烃（乙烯-丙烯-丁烯共聚）用于卫材热熔胶/结构胶，其**共聚组成与序列分布**决定 Tg、软化点与开放时间；本章的组成漂移分析对应胶黏剂批间一致性问题。参见 [[APAO（非晶态聚α-烯烃）]]。
4. **Minor-constituent 思路的直接迁移.** 本章枚举的"少量功能单体"策略（交联位点 / 羧基增溶 / 染色位点）正是卫材功能化（亲水改性、抗菌、可降解）树脂设计的通用范式；与 Ch.5 改性章节互为表里。参见 [[Ebewole Polymer Science Ch05 Polymer Modification]]。
5. **Not covered 本章未涉及**: 三元以上共聚方程、嵌段共聚的实验实现（顺序加料 / 活性聚合，本章仅指出理论无实证）、Tg 与共聚组成的定量关系（Fox 方程等，见 Ch.4）。

## Related Sources 关联来源

- [[Ebewole Polymer Science Ch02 Polymerization Mechanisms]]
- [[Ebewole Polymer Science Ch05 Polymer Modification]]
- [[Ebewole Polymer Science Ch07 Chain-Reaction Addition Polymerization]]
- [[Acrylic-Based Superabsorbent Polymers]]
- [[APAO（非晶态聚α-烯烃）]]
- [[AMPS（2-丙烯酰胺基-2-甲基丙磺酸）耐盐单体]]

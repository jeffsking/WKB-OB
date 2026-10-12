---
type: source
title: "Seymour Polymer Chemistry Ch06 Step-Reaction Polymerization"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Seymour Polymer Chemistry/chapters/Seymour Polymer Chemistry_ch06.md.md"
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "The terms addition and condensation polymers were first proposed by Carothers: an addition polymer has the same atoms as the monomer in its repeat unit, whereas condensation polymers contain fewer atoms in the repeat unit because by-products form during polymerization."
  - "Stepwise (step-growth) kinetics refers to polymerizations in which the molecular weight increases in a slow, step-like manner with reaction time; chain growth reactions require initiation and occur only at active chains."
  - "Carothers equation: DPN = 1/(1−p); at p = 0.9999 the DP is approximately 10,000, and useful high molecular weight linear polymers require p at least 0.990 (DP greater than 100)."
  - "When the average functionality is greater than 2, crosslinking occurs; the critical branching coefficient for incipient gelation is αc = 1/(f−1), so when f = 2.2, αc = 0.83."
  - "Activation energies are about 30 kcal/mole (120 kJ/mole) for direct esterification and transesterification, versus about 15–20 kcal/mole (60–80 kJ/mole) for anhydride and acid chloride reactions with alcohols."
  - "Flory's statistical distribution for step-growth gives pn = (1−p) p^(n−1) and Nn = N₀(1−p)² p^(n−1)."
summary_cn: "第6章是合成化学核心：以 Carothers 方程 DPN=1/(1-p) 与 Flory 统计分布为定量骨架，区分逐步聚合与链增长聚合、加成型与缩合型聚合物，并展开官能度 f>2 的交联凝胶化判据 αc=1/(f-1) 及聚酯/聚酰胺/聚氨酯等缩聚物谱系。"
tags: ["source/book", "step-growth-polymerization", "polycondensation", "carothers-equation", "gelation", "functionality", "polyester", "polyamide"]
tags_zh: ["逐步聚合", "缩聚反应", "卡罗瑟斯方程", "凝胶化", "官能度", "交联", "聚酯", "聚酰胺"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Seymour Polymer Chemistry Ch03 Molecular Weight of Polymers]]", "[[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]]", "[[Seymour Polymer Chemistry Ch07 Ionic and Coordinative Chain Polymerization]]", "[[A review on superabsorbent polymers]]", "[[Acrylic-Based Superabsorbent Polymers]]"]
---

# Seymour Polymer Chemistry Ch06 Step-Reaction Polymerization

> Source: Seymour/Carraher, *Polymer Chemistry*, Ch.6 — Step-Reaction Polymerization or Polycondensation Reactions.
> 定位说明 / Citation convention: 原文为 .txt 抽取件，**无正式印张页码**，本报告以文件行号（line no.）定位；原书页码缺失处标注 [待验证]。

## Executive Summary 内容概要

Chapter 6 is the synthesis-chemistry core. It separates **step-growth（逐步聚合）from chain-growth（链增长）**, then quantifies step-growth with the **Carothers equation** and **Flory's statistical distribution**, extends to **functionality f > 2 → crosslinking → gelation**, and closes with the product spectrum: polyester / polyamide / polyurethane / polycarbonate / polysulfide / polysiloxane / alkyd. 本章把聚合反应从经验工艺提升为可定量预测的统计动力学体系——这也是 SAP（交联聚电解质网络）合成的理论基石。

## Addition vs Condensation, Step vs Chain 分类与动力学

> *"The terms addition and condensation polymers were first proposed by Carothers and are based on whether the repeat unit of the polymer contains the same atoms as the monomer. An addition polymer has the same atoms as the monomer in its repeat unit."* (line 11-14)

> *"Condensation polymers contain fewer atoms within the polymer repeat unit than the reactants because of the formation of byproducts during the polymerization process, and the polymer backbone usually contains atoms of more than one element."* (line 15-18)

**逐步动力学 / Stepwise kinetics**：*"The term stepwise kinetics, or step-growth kinetics, refers to polymerizations in which the polymer's molecular weight increases in a slow, step-like manner as reaction time increases."* (line 28-31) — *"Polymer formation begins with one dialcohol (diol) molecule reacting with one diacid molecule..."* → *"dimer, trimer, tetramer, etc., molecules are formed as the reaction progresses."* → *"the reactants are consumed with very few long chains being formed throughout the system until the reaction progresses toward total reaction of the chains with themselves."*

**链增长动力学 / Chain-growth kinetics**：*"Chain growth reactions require initiation to begin chain growth."*；*"Since polymerization occurs only with active chains (i.e., chains containing an unpaired electron), since the activation energy for chain growth is low, and since the concentration of growing chains is maintained at a low concentration at any given time..."* (line 76-96)

| 维度 Dimension | Step-growth 逐步聚合 | Chain-growth 链增长聚合 |
|---|---|---|
| 分子量增长 MW build-up | 缓慢、阶梯式 slow, step-like | 引发后链迅速长成 rapid |
| 单体消耗 Monomer consumption | 早期即大量消耗，长链后期才形成 | 单体逐步消耗，链长几乎立即达终值 |
| 是否需要引发 Initiation | 不需要（官能团自发反应） | 必需 requires initiation |
| 产物谱系 Examples | PET、nylon、PU、PC | PE、PP、PS、PVC |

## Carothers Equation 卡罗瑟斯方程

> **Eq. 6.29**：**DPN = 1/(1−p)**

> *"For an essentially quantitative synthesis of polyamides where p is 0.9999, the DP was found to be approximately equal to 10,000"* → *"DPN = 1/(1-p) = 1/(1-0.9999) = 1/0.0001 = 10,000"* (line 822-833)

> *"Useful high molecular weight linear polymers are not obtained unless the value for the fractional conversion p is at least 0.990, i.e., a DP greater than 100."* (line 894-895)

- **催化体系 / Catalysis**：*"For catalyzed systems since the added acid or base is a catalyst, its apparent concentration does not change with time; thus it need not be included in the kinetic rate expression."* **Rate of polycondensation = −d[A]/dt = k[A][B]** (Eq. 6.33, line 852-865)
- **Flory 统计分布**：*"The probability of finding a repeating unit AB in the polymer is p, and the probability of finding n−1 of these repeating units in the polymer chain is p^(n−1). Likewise, the probability of finding an unreacted molecule of A or B is 1−p."* → **pn = (1−p) p^(n−1)** (Eq. 6.40)；**Nn = N₀(1−p)² p^(n−1)** (Eq. 6.43)（line 914-934）

## Functionality, Crosslinking and Gelation 官能度、交联与凝胶化

> *"When the average functionality is greater than 2 crosslinking occurs."* (line 1166)

> *"The critical value for incipient gelation (αc) is the probability that one or more of the f−1 chain segments on the branch unit will be connected to another branch unit, i.e., αc = (f−1)⁻¹ or 1/(f−1). Thus, when f = 2.2, αc = 0.83."* (line 1179-1183)

| 参数 Parameter | 含义 Meaning | 工程后果 Consequence |
|---|---|---|
| f̄ = 2 | 双官能，线型增长 | 线型热塑聚合物，可熔融加工 |
| f̄ > 2 | 平均官能度超过 2 | 发生交联 crosslinking |
| α < αc | 支化系数低于临界值 | 体系仍可溶、可熔，未凝胶 |
| α ≥ αc = 1/(f−1) | 达到凝胶点 | 形成不溶不熔三维网络（凝胶） |

## Step-Polymerization Product Spectrum 缩聚物谱系

**聚酯合成路径 / Polyester routes（line 1140-1159）**：

> *"Today, we know that Carothers would of had greater success in producing high molecular weight material had his group employed transesterification, ring opening (of the 'diol' derived moiety), or the reaction of diols with acyl dichlorides (Schotten-Baumann reaction) or anhydrides."* — *"Each of these reactions involve the nucleophilic addition to the carbonyl group."*

> *"Reaction with anhydrides and acid chlorides are more rapid and can occur in an essentially nonreversible fashion. But anhydrides and acid chlorides are considered so-called 'high energy' reactants..."*

> *"The activity energies for direct esterification and transesterification are on the order of 30 kcal/mole (120 kJ/mole), while the activation energies for anhydride and acid chloride reaction with alcohols are on the order of 15–20 kcal/mole (60 to 80 kJ/mole)."*

**醇酸树脂 / Alkyd（line 1184-1198）**：*"Glyptal polyesters were produced in 1901 by heating glycerol and phthalic anhydride."*；*"The terms short oil, medium oil, and long oil alkyd are used to signify the 'oil length' obtained by use of 30–50%, 50–65%, and 65–80% of unsaturated oil, respectively."*

本章 Tables 6.1-6.2 系统列出缩聚物的重复单元、原料、性能与应用。

## Methodology Critique 方法论批判

- **Addition vs Condensation 分类存在交叉**：Seymour 自己承认 "There is a large but not total overlap" —— 聚氨酯是加成聚合但产物含"缩合型"重复单元；环氧化合物开环聚合是加成但无副产物。提示**反应机理**比**产物类型**更本质。
- **Carothers 方程的理想化假设**：DPN = 1/(1−p) 假设等摩尔、无副反应、官能团等活性；实际体系中 stoichiometric imbalance（r ≠ 1）会显著降低 DPN。
- **凝胶点预测的偏差**：Flory-Stockmayer 理论忽略分子内环化（intramolecular cyclization），实际凝胶点通常晚于理论预测。

## Hygiene Implication 卫材关联

- **SAP 的交联网络就是本章的凝胶化问题**：SAP 是交联聚丙烯酸（部分中和）网络，其合成属逐步聚合 + 交联体系。原文判据"average functionality > 2 → crosslinking"与"αc = 1/(f−1)"直接给出交联剂用量的理论边界：交联剂太少（α < αc）→ 聚合物可溶、凝胶强度不足、易渗出；交联剂太多 → 网络致密、溶胀空间被压缩、保水量（CRC）下降。这正是 SAP 交联度窗口设计的定量依据。
- **高转化率是硬性门槛**：Carothers 方程要求 p ≥ 0.990（DP > 100）才有实用高分子量。对 SAP 前体聚丙烯酸意味着残留单体控制不只是安全/气味问题，更是分子量与凝胶强度问题——残留单体的波动会直接改变 p 与 DPN。
- **PP 是本章的对照体系**：PP 属 chain-growth（加成型，重复单元与单体原子相同），分子量在引发后迅速达终值，转化率只影响产量不影响链长。因此 PP 的质量控制聚焦于催化剂选择性与等规度，而 SAP 的质量控制聚焦于转化率 p 与交联度 α——两者是两套完全不同的控制逻辑。
- **表层亲水整理剂/热熔胶的缩聚化学**：聚酯型聚氨酯热熔胶、聚酯亲水整理剂均属本章谱系；其主链含酯/酰胺等缩合键，按 Ch.4 的结论对极性试剂与酸碱只有中等或较差稳定性，这在尿液/经血的复杂化学环境中是选材时必须权衡的。

## Related Sources 关联来源

- [[Seymour Polymer Chemistry Ch03 Molecular Weight of Polymers]]
- [[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]]
- [[Seymour Polymer Chemistry Ch07 Ionic and Coordinative Chain Polymerization]]
- [[A review on superabsorbent polymers]]
- [[Acrylic-Based Superabsorbent Polymers]]

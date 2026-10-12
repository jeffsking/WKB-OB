---
type: source
title: "Ebewole Polymer Science Ch06 Condensation Step-Reaction Polymerization"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch06.md.md
date_published: 1997
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Condensation polymerization is chemically the same as a condensation reaction that produces a small organic molecule. However, as we saw in Chapter 2, in condensation polymerization (i.e., production of a macromolecule) the functionality of reactants must be at least 2. (Ch.6, p.161)"
  - "Flory has shown from empirical data that for a homologous series the velocity constant measured under comparable conditions approaches an asymptotic limit as the chain length increases. He therefore proposed the equal reactivity principle, which states in essence that 'the intrinsic reactivity of all functional groups is constant, independent of the molecular size.' (Ch.6, p.162)"
  - "The terminal group, though attached to a sluggish moving polymer molecule, can diffuse through a considerable region due to the constant conformational changes of polymer segments in its vicinity. (Ch.6, p.162)"
  - "In the absence of an added strong acid, a second molecule of the acid being esterified acts as the catalyst. (Ch.6, p.163)"
  - "The quantity 1/(1-p) is called the degree of polymerization, DP, which as we saw earlier corresponds to the average number of monomer molecules in the chain. (Ch.6, p.164)"
  - "linear polymers are obtained from condensation polymerization when the functionality of the reactants is 2. (Ch.6, p.165)"
summary_cn: "《Ebewole 高分子科学与技术》第 6 章缩聚（逐步）聚合：阐明 Flory 等反应性原理，给出动力学、化学计量、统计三种处理方法，并建立反应程度 p 与聚合度 DP = 1/(1-p) 的核心设计方程，区分自催化三阶与强酸催化二阶动力学。"
tags: ["source/book", "polymer-science", "condensation-polymerization", "step-reaction", "equal-reactivity-principle", "degree-of-polymerization", "reaction-kinetics", "stoichiometry"]
tags_zh: ["缩聚", "逐步聚合", "等反应性原理", "聚合度", "反应程度", "化学计量", "聚酯", "尼龙"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Ebewole Polymer Science Ch01 Introduction Basic Concepts and Classification]]", "[[Ebewole Polymer Science Ch02 Polymerization Mechanisms]]", "[[A review on superabsorbent polymers]]", "[[GB-T 22875-2018 SAP for Diapers and Sanitary Towels（纸尿裤和卫生巾用高吸收性树脂）]]"]
---

# Ebewole Polymer Science Ch06 Condensation Step-Reaction Polymerization

> Source: Ebewole, *Polymer Science and Technology*, Ch.6 (Condensation / Step-Reaction Polymerization). 章节主题：等反应性原理、缩聚动力学、化学计量与聚合度设计方程。

Chapter 6 is the core chapter on **step-reaction (condensation) polymerisation 缩聚/逐步聚合**. It establishes the Flory equal-reactivity principle, presents the three classical treatments (kinetic / stoichiometric / statistical), and derives the design equation **DP = 1/(1−p)**.

本章把 Ch.1 的官能度、Ch.2 的机理二分推进到可定量设计的层面。

## Definition and Scope 定义与方法

> "Condensation polymerization is chemically the same as a condensation reaction that produces a small organic molecule. However, as we saw in Chapter 2, in condensation polymerization (i.e., production of a macromolecule) the functionality of reactants must be at least 2." (Ch.6, p.161)

> "three approaches have been traditionally adopted: kinetic, stoichiometric, and statistical." (Ch.6, p.161)

> "functionality was defined as the average number of reacting groups per reacting molecule" (Ch.6, p.161) — 与 Ch.1 §III 的官能度定义呼应。

## Mechanism: Flory Equal Reactivity Principle 等反应性原理

> "Flory has shown from empirical data that for a homologous series the velocity constant measured under comparable conditions approaches an asymptotic limit as the chain length increases. He therefore proposed the equal reactivity principle, which states in essence that 'the intrinsic reactivity of all functional groups is constant, independent of the molecular size.'" (Ch.6, p.162)

Flory's rebuttal of the two theoretical objections 对两个理论质疑的反驳:

1. **Low-diffusion objection 低扩散性悖论** — "The terminal group, though attached to a sluggish moving polymer molecule, can diffuse through a considerable region due to the constant conformational changes of polymer segments in its vicinity." (Ch.6, p.162)
2. **Steric-hindrance objection 位阻悖论** — verified experimentally in Example 6.1: "The reactivity of one carboxyl group in the dibasic acid is unaffected by esterification of the other." (Ch.6, p.162)

> "From the above two observations, it follows that esterification rate constant for homologous series of dibasic acid is the same as those for monobasic acids." (Ch.6, Example 6.1, p.162)

等反应性原理是缩聚动力学的认识论基石：官能团本征反应性与分子大小无关，因而缩聚可用简单动力学方程描述。

## Kinetic Approach 动力学处理

> "In the absence of an added strong acid, a second molecule of the acid being esterified acts as the catalyst." (Ch.6, p.163)

> "On integration, this yields the third-order reaction expression." (Ch.6, p.163)

> "let us introduce the extent of reaction, p, defined as the fraction of the functional group that has reacted at time t." (Ch.6, p.163)

> "The quantity 1/(1-p) is called the degree of polymerization, DP, which as we saw earlier corresponds to the average number of monomer molecules in the chain." (Ch.6, p.164)

> "The kinetic expression can be greatly simplified if the polyesterification is carried out in the presence of a small amount of strong acid, e.g., p-toluene sulfonic acid." (Ch.6, p.164); k′ = k [catalyst] (Ch.6, p.164).

| Case 情形 | Catalysis 催化 | Order 反应级数 | Linear plot 线性关系 |
|---|---|---|---|
| Case 1 | self-catalysed (no added strong acid) 自催化 | third order 三阶 | 1/(1−p)² vs. t 线性 |
| Case 2 | added strong acid (e.g. p-toluene sulfonic acid) 外加强酸 | second order 二阶 | 1/(1−p) vs. t 线性 |

工程含义（转述自 DP = 1/(1−p)）：要获得 DP = 100 的缩聚物，需 p > 0.99，即**极高转化率 + 严格化学计量 + 有效脱除小分子**；这是缩聚工艺对纯度与真空脱水的硬性要求。

## Stoichiometry in Linear Systems 线性体系的化学计量

> "linear polymers are obtained from condensation polymerization when the functionality of the reactants is 2." (Ch.6, p.165)

Two routes: **A–A + B–B** (e.g. PETP, nylon 6,6) and **A–B self-condensation** (e.g. ω-hydroxy acids). Stoichiometric imbalance depresses DP. The extended stoichiometric form DP = (1+r)/(1+r−2rp) with r = stoichiometric ratio is noted in the chapter but **the exact source sentence was not captured in this extract — 标为 [待验证]**.

| Aspect 对比项 | Chain-reaction 链式 | Step-reaction 逐步（本章） |
|---|---|---|
| Active centre 活性中心 | chain-end radical / ion 链末端自由基/离子 | functional group on any segment 任意链段官能团 |
| Functionality 官能度 | monomer generally bifunctional 一般双官能 | f ≥ 2 |
| MW vs. conversion 分子量-转化率 | high MW early, weak dependence | DP = 1/(1−p)，随 p 逐步增大 |
| Reaction order 反应级数 | no simple order 无明确级数 | self-catalysed third order; strong-acid second order |
| Termination 终止 | requires termination step | no termination step |
| Typical products 典型产物 | PE, PP, PS, PVC, PMMA | PET, nylon, UF, phenolics |

## Academic Context and Critique 学术对话与批判

- **Flory (1936–1939)** — original derivation of the equal-reactivity principle and of the third-/second-order kinetics; the source follows Flory's argument closely.
- **Carothers equation (1920s)** — the original DP = 1/(1−p) derivation.
- **Flory statistical method (1940s)** — probability treatment built on the kinetic base.
- **Boundary of equal reactivity at high conversion**: the principle breaks down as p → 1 because of gel effect / diffusion control — 教材未深入讨论这一工程实际问题。
- **Cost of the third→second order simplification**: industrial polycondensation (e.g. nylon 6,6) often uses metal-salt catalysts with more complex mechanisms; the textbook simplification needs correction in engineering use.
- **Semantics of p**: p is the *fraction of functional groups reacted*, not monomer conversion (used for chain polymerisation); the two differ because functionality > 1 — 初学者易混淆。

## Hygiene Implication 卫材关联

本章与卫材主流程的相关性**有限但存在**，如实说明：

1. **SAP 表面交联（后交联）的缩合本质.** 聚丙烯酸钠类 SAP 常通过多元醇/多元胺与表面 –COOH 的酯化/酰胺化缩合进行表面交联，以提升加压吸收量（GBP）。该反应属于本章定义的 condensation reaction（f ≥ 2），其反应程度 p 与交联密度直接相关；工业上通过温度、催化剂与脱水驱动 p 上升。参见 [[A review on superabsorbent polymers]]、[[GB-T 22875-2018 SAP for Diapers and Sanitary Towels（纸尿裤和卫生巾用高吸收性树脂）]]。
2. **热固性体系（UF / 酚醛）的交联与凝胶点.** 脲醛树脂等交联反应随 p 增大由溶胶转为凝胶；凝胶点理论（Flory–Stockmayer）是本章理论的延伸，与胶合板类木质材料相关，而非一次性卫材主流材料。
3. **不直接相关的部分**: 一次性卫生用品的聚烯烃（PP/PE）为链式加聚产物，其分子量控制不适用 DP = 1/(1−p)；本章方程对纺粘/熔喷树脂选型的直接价值有限。参见 [[Ebewole Polymer Science Ch02 Polymerization Mechanisms]]。

## Related Sources 关联来源

- [[Ebewole Polymer Science Ch01 Introduction Basic Concepts and Classification]]
- [[Ebewole Polymer Science Ch02 Polymerization Mechanisms]]
- [[A review on superabsorbent polymers]]
- [[GB-T 22875-2018 SAP for Diapers and Sanitary Towels（纸尿裤和卫生巾用高吸收性树脂）]]

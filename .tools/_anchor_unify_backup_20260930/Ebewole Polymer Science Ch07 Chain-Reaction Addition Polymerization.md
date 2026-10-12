---
type: source
title: "Ebewole Polymer Science Ch07 Chain-Reaction Addition Polymerization"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch07.md.md"
date_published: 1997
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "In chain polymerization processes, the active center is retained at the end of a growing polymer chain and monomers are added to this center in rapid succession. (Ch.7, p.182)"
  - "high-molecular-weight polymers are generated even while most of the monomers remain intact. … in a partially polymerized mixture, only high-molecular-weight polymers and unchanged monomers are present with virtually no intermediates between these ends of the molecular weight spectrum. (Ch.7, p.182)"
  - "Monomers with an electron-withdrawing group can proceed by an anionic pathway; those with an electron-donating group by a cationic pathway. Some monomers with a resonance-stabilized substituent group — for example, styrene — can be polymerized by more than one mechanism. (Ch.7, p.182)"
  - "These species are frequently but erroneously also called catalysts. Initiators are consumed in the reaction while catalysts are regenerated after the reaction. (Ch.7, p.182)"
  - "The initiation step in free-radical polymerization in the presence of thermal initiators is a two-step process: first is the homolysis of the relatively weak covalent bond in the initiator. … The first step is the rate-limiting step in the initiation process. (Ch.7, p.183)"
  - "In 1,2 addition, the unsaturation is part of the pendant group. In 1,4 addition, however, the unsaturation is part of the backbone. Two configurations are possible — trans or cis. (Ch.7, p.184)"
summary_cn: "《Ebewole 高分子科学与技术》第 7 章链式（加聚）聚合：阐明活性中心保持在链末端、高分子量在低转化率即生成的链式特征，给出乙烯基单体电子效应与自由基/阴离子/阳离子/配位四类活性中心的匹配矩阵（Table 7.1），并展开引发—增长—终止—链转移四步机理与二烯 1,2 / 1,4 加成立体化学。"
tags: ["source/book", "polymer-science", "chain-reaction", "addition-polymerization", "vinyl-monomer", "free-radical", "coordination-polymerization", "Ziegler-Natta"]
tags_zh: ["链式聚合", "加聚", "乙烯基单体", "活性中心", "引发效率", "配位聚合", "链转移", "立体化学"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Ebewole Polymer Science Ch02 Polymerization Mechanisms]]", "[[Ebewole Polymer Science Ch06 Condensation Step-Reaction Polymerization]]", "[[Polypropylene Handbook Spunbond and Meltblown Nonwoven Resins]]", "[[Manufactured Fibre Technology Ch19 Spunbonding and Melt-Blowing Processes]]", "[[Acrylic-Based Superabsorbent Polymers]]"]
---

# Ebewole Polymer Science Ch07 Chain-Reaction Addition Polymerization

> Source: Ebewole, *Polymer Science and Technology*, Ch.7 (Chain-Reaction / Addition Polymerization). 章节主题：链式聚合特征、乙烯基单体与活性中心匹配、四步机理、二烯加成立体化学。

Chapter 7 is the core chapter on **chain-reaction (addition) polymerisation 链式/加聚聚合**. It delivers the full four-step kinetic picture, the **active-centre × monomer matching matrix (Table 7.1)**, and the 1,2 vs. 1,4 diene stereochemistry.

本章是 Ch.2 机理导论的定量深化：Ch.2 给出分类与概念，Ch.7 给出动力学表达式与工业选型矩阵。

## Essence of Chain Polymerisation 链式聚合的本质

> "In chain polymerization processes, the active center is retained at the end of a growing polymer chain and monomers are added to this center in rapid succession." (Ch.7, p.182)

> "high-molecular-weight polymers are generated even while most of the monomers remain intact." (Ch.7, p.182)

> "Thus in a partially polymerized mixture, only high-molecular-weight polymers and unchanged monomers are present with virtually no intermediates between these ends of the molecular weight spectrum." (Ch.7, p.182)

与 Ch.6 的逐步聚合形成鲜明对照：链式聚合在**低转化率即得高分子量**，体系中只有"高分子量聚合物 + 未反应单体"，几乎无中间分子量产物；而缩聚的分子量随反应程度 p 逐步增大（DP = 1/(1−p)）。

## Vinyl Monomers and Active-Centre Matching 乙烯基单体与活性中心匹配

> "These compounds constitute the so-called vinyl monomers where X and Y may be halogen, alkyl, ester, phenyl, or other groups." (Ch.7, p.182)

> "The active centers … may be free radicals, carbanions, carbonium ions, or coordination complexes among the growing chain, the catalyst surface, and the adding monomer." (Ch.7, p.182)

> "Monomers with an electron-withdrawing group can proceed by an anionic pathway; those with an electron-donating group by a cationic pathway. Some monomers with a resonance-stabilized substituent group — for example, styrene — can be polymerized by more than one mechanism." (Ch.7, p.182)

> "These species are frequently but erroneously also called catalysts. Initiators are consumed in the reaction while catalysts are regenerated after the reaction." (Ch.7, p.182)

| Mechanism 机理 | Typical initiator / catalyst 引发剂或催化剂 | Monomer electronics 单体电子效应 | Stereo control 立体控制 | Typical products 典型产物 |
|---|---|---|---|---|
| Free radical 自由基 | peroxide, AIBN, KPS | electron-withdrawing or -donating 吸/给电子均可 | low 低 | LDPE, PS, PVC, PMMA, PVAc |
| Anionic 阴离子 | n-BuLi, alkali metal | electron-withdrawing 吸电子 | medium 中 | polystyrene, BR (high cis-1,4) |
| Cationic 阳离子 | Lewis acid (BF₃, AlCl₃) | electron-donating 给电子 | low 低 | isobutene (butyl rubber) |
| Coordination 配位 | Ziegler–Natta, metallocene | ethylene, propylene 乙烯、丙烯 | high 高 | HDPE, isotactic PP 等规 PP |

**Table 7.1** of the chapter gives a "+" / "–" applicability matrix for olefin monomers against the four mechanisms. 该表是工业单体-机理选型的快速查表工具。

## Mechanism: Four Steps 四步机理

### A. Initiation 引发

> "The initiation step in free-radical polymerization in the presence of thermal initiators is a two-step process: first is the homolysis of the relatively weak covalent bond in the initiator." (Ch.7, p.183)

> "The first step is the rate-limiting step in the initiation process." (Ch.7, p.183)

> "The efficiency with which radicals initiate chains can be estimated by comparing the amount of initiator decomposed with the number of polymer chains formed." (Ch.7, p.183)

引发剂均裂（homolysis）是速率控制步骤；**引发效率 initiator efficiency** = 有效链数 / 已分解引发剂分子数，是工业引发剂选型的关键指标。常用引发剂：BPO, AIBN, KPS, t-BuOOH。

### B. Propagation 增长

> "The free radical generated in the initiation step adds monomers in very rapid succession. Again, this consists of an attack of the free radical on one of the carbon atoms in the double bond." (Ch.7, p.183)

> "In this way the active center is transferred uniquely to the newly added monomer. This process then continues until termination sets in." (Ch.7, p.183)

> "In 1,2 addition, the unsaturation is part of the pendant group. In 1,4 addition, however, the unsaturation is part of the backbone. Two configurations are possible — trans or cis." (Ch.7, p.184)

二烯加成：1,2 加成的双键留在**侧基**，1,4 加成的双键进入**主链**并产生 cis / trans 两种构型——这是弹性体低温性能设计的结构根源（与 Ch.2 §E、Ch.4 的 cis-trans–Tg 关系呼应）。

### C. Termination 终止

> "The termination steps can occur by either of two mechanisms: combination (coupling) or disproportionation." (Ch.7, p.184)

> "Combination or coupling — Two growing polymer chains yield a single polymer molecule terminated at each end by an initiator fragment." (Ch.7, p.184)

> "Disproportionation — This involves hydrogen transfer with the formation of two polymer molecules, one with a saturated end and the other with an unsaturated terminal olefin and each with an initiator fragment." (Ch.7, p.184)

两种终止方式都留下**引发剂残基 initiator fragment** 作为链端标记；combination 生成一分子，disproportionation 生成两分子（一饱和端、一不饱和端）。温度效应见 Ch.2, p.29：低温以偶合为主，高温歧化更显著。

### D. Chain Transfer 链转移

> "Chain transfer involves the transfer of radical reactivity to another species, which may be a monomer, a polymer, a solvent, an initiator, or an impurity." (Ch.7, p.185)

> "This creates a new species that is capable of further propagation but terminates the growth of the original chain." (Ch.7, p.185)

链转移是工业上控制 Mn 的核心手段（Mayo 链转移方程，1944：1/Mn = 1/Mn₀ + Cs[S]/[M] + Cm + Ci[I]/[M]）。

## Academic Context and Critique 学术对话与批判

- **Mayo chain-transfer equation (1944)** — quantitative basis of §D; **Bamford–Stewart steady-state assumption (1948)** — steady free-radical concentration; **Ziegler–Natta catalysis (1953–55)** — the core of the "Coordination" column.
- **Initiator ≠ catalyst in industrial reality**: the text insists "initiators are consumed", but real catalysts (e.g. Ziegler–Natta) are also partially consumed/deactivated; 语义边界在工业文献中并不绝对。
- **Absoluteness of Table 7.1**: the "+" / "–" entries are binary, yet many monomers polymerise by more than one mechanism (styrene is "+" in all four columns) — 教材未区分"工业可行"与"理论可能"。
- **1,2 vs. 1,4 kinetic control**: the source states both configurations are possible but gives no quantitative model (e.g. activation-energy difference) — 教学简化，工程应用需另引数据。

## Hygiene Implication 卫材关联

1. **Why PP must use coordination polymerisation 等规 PP 的机理强制约束.** propylene 对 free-radical / anionic / cationic 均不适用，仅 **coordination（Ziegler–Natta / metallocene）** 可行（Table 7.1）；这决定了聚烯烃树脂的立体规整度、结晶度与熔点，进而决定纺粘/熔喷的可纺性与热轧粘合窗口。参见 [[Polypropylene Handbook Spunbond and Meltblown Nonwoven Resins]]、[[Manufactured Fibre Technology Ch19 Spunbonding and Melt-Blowing Processes]]。
2. **Acrylic SAP via free-radical polymerisation 丙烯酸类 SAP 的自由基路线.** 丙烯酸及其盐对 free-radical 适用（Table 7.1 中 acrylate 类为 "+"），故 SAP 主流采用水相自由基（含 redox 低温引发）路线；链长与交联通过链转移剂、单体浓度与引发剂效率调节。参见 [[Acrylic-Based Superabsorbent Polymers]]。
3. **Chain transfer and resin MWD 链转移与树脂分子量分布.** 对聚烯烃而言，链转移是调控 Mn 与 Mw/Mn 的工业手段，直接映射到熔体流动速率与熔体强度——熔喷工艺对高 MFR 窄分布树脂的依赖即由此而来。参见 [[Ebewole Polymer Science Ch02 Polymerization Mechanisms]]。
4. **Not covered 本章未涉及**: Tg/Tm 数值与结晶动力学（见 Ch.4），粘弹性与熔体流变本构。缩聚体系对比见 [[Ebewole Polymer Science Ch06 Condensation Step-Reaction Polymerization]]。

## Related Sources 关联来源

- [[Ebewole Polymer Science Ch02 Polymerization Mechanisms]]
- [[Ebewole Polymer Science Ch06 Condensation Step-Reaction Polymerization]]
- [[Polypropylene Handbook Spunbond and Meltblown Nonwoven Resins]]
- [[Manufactured Fibre Technology Ch19 Spunbonding and Melt-Blowing Processes]]
- [[Acrylic-Based Superabsorbent Polymers]]

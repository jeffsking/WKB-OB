---
type: source
title: "ch3_report.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch3_report.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
key_claims: []
pages_linked: []
compile_mode: extractive
---

# ch3_report.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch3_report.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# ch3_report.md.md

# Ch3 Radical Chain Polymerization 深度拆书报告

源文件: /sandbox/workspace/Ebook_Extract/Principles_of_Polymerization/chapters/ch3_radical.txt（Odian, Principles of Polymerization, 4th Ed., 2004, Ch.3, 约 7688 行）

## 模块1：核心论点

### 论点1｜链聚合与逐步聚合的根本区别：高分子聚合物"即时"生成

- 原文（第 48–56 行，约原书 p.199）："Chain polymerization proceeds by a distinctly different mechanism from step polymerization. The most significant difference is that high-molecular-weight polymer is formed immediately in a chain polymerization… The monomer concentration decreases throughout the course of the reaction… The molecular weight of the polymer is relatively unchanged during the polymerization, although the overall percent conversion of monomer to polymer increases with reaction time."
- 精炼概括：链式聚合中一旦引发中心产生，链即迅速增长到高分子量；体系始终只含单体、高分子和增长链，分子量基本恒定，而转化率随时间上升。这与逐步聚合"任何两种分子都可反应、分子量随时间逐步增长、需长时间才能获得高分子量"形成对比。
### 论点2｜自由基引发剂对单体选择性最低：几乎所有 C=C 双键均可自由基聚合

- 原文（第 214–241 行，约原书 p.202）："Contrary to the high selectivity shown in cationic and anionic polymerization, radical initiators bring about the polymerization of almost any carbon–carbon double bond. Radical species are neutral and do not have stringent requirements for attacking the π-bond or for the stabilization of the propagating radical species. Resonance stabilization of the propagating radical occurs with almost all substituents."
- 精炼概括：阳离子/阴离子聚合对单体有强烈选择性（见表 3-1，第 95–115 行），但自由基引发剂对几乎所有 C=C 双键有效——这是自由基聚合在工业应用中最广泛的原因。
### 论点3｜稳态假设导出 Rp 对 [I]^{1/2} 的平方根依赖：倍增加速剂只能使 Rp 增加 √2 倍

- 原文（第 509–548 行，约原书 p.207–208）："The rate of change of the concentration of radicals quickly becomes and remains zero… Ri = Rt = 2kt[M•]²… Rp = kpM^{1/2}… Doubling the rate of initiation does not double the polymerization rate; the polymerization rate is increased only by the factor √2."
- 关键公式（第 791–796 行，约 p.212）：
$$R_p = k_p[M]\left(\frac{f k_d[I]}{k_t}\right)^{1/2}$$
### 论点4｜动力学链长 ν 反比于自由基浓度：提高速率必牺牲分子量

- 原文（第 2037–2045 行，约原书 p.237）："The kinetic chain length is inversely dependent on the radical concentration or the polymerization rate. This is of great practical significance—any attempt to increase the polymerization rate by increasing the radical concentration comes at the expense of producing smaller polymer molecules."
- 公式（第 1978–1987 行）：
$$\bar{\nu} = \frac{k_p^2[M]^2}{2k_t R_p} = \frac{k_p[M]}{2(fk_dk_t[I])^{1/2}}$$
### 论点5｜Trommsdorff/gel 效应（自加速）来自扩散控制的终止：kp 几乎不变而 kt 下降 2 个数量级

- 原文（第 4316–4349 行，约原书 p.282–283 起）："A typical example is shown in Fig. 3-15 for the polymerization of methyl methacrylate… The plot for neat (pure) monomer shows a dramatic autoacceleration in the polymerization rate. Such behavior is referred to as the gel effect… the terms Trommsdorff effect and Norrish–Smith effect are also used."
- 机理（第 4435–4445 行，约 p.285）：高转化率下体系粘度↑和链缠结↑使平动扩散↓，从而 kt 急剧下降；而 kp 因单体分子小受影响小（kp 与 kt 差 10⁴–10⁵ 倍），故 kp/kt^{1/2} 上升，Rp 上升。
### 论点6｜链转移不改变 Rp（Case 1）但决定分子量上限；硫醇类为最强链转移剂（CS 可达 480,000×10⁻⁴）

- 原文（第 2100–2124 行，约 p.239；表 3-6，第 2487–2517 行，约 p.247）："Chain transfer is a chain-breaking reaction; it results in a decrease in the size of the propagating polymer chain. The effect of chain transfer on the polymerization rate is dependent on whether the rate of reinitiation is comparable to that of the original propagating radical." 硫醇的 S–H 键最弱，转移常数最大（第 2569 行）。
## 模块2：关键概念操作化定义（含原文摘录）

### 2.1 Rate of polymerization Rp（聚合速率）

- 定义：单位时间内单体消耗（即聚合物生成）的速率；因引发步消耗的单体极少，Rp 可等同于传播速率。
- 原文（第 478–494 行，约 p.207）："The rate of monomer disappearance, which is synonymous with the rate of polymerization, is given by −d[M]/dt = Ri + Rp… To a very close approximation the former can be neglected and the polymerization rate is given simply by the rate of propagation −d[M]/dt = Rp."
### 2.2 Kinetic chain length ν（动力学链长）

- 定义：每个引发自由基所聚合的单体分子平均数 = Rp/Ri = Rp/Rt。
- 原文（第 1961–1968 行，约 p.236）："The kinetic chain length ν of a radical chain polymerization is defined as the average number of monomer molecules consumed (polymerized) per each radical, which initiates a polymer chain… ν = Rp/Ri = Rp/Rt."
### 2.3 Degree of polymerization DP̄ₙ（数均聚合度 Xn）

- 定义：每个聚合物分子所含单体单元平均数，与动力学链长关系由终止方式决定：偶合终止 Xn = 2ν（第 1997 行）；歧化终止 Xn = ν（第 2002 行）。
- 原文（第 1992–2002 行，约 p.237）："The number-average degree of polymerization Xn, defined as the average number of monomer molecules contained in a polymer molecule, is related to the kinetic chain length… coupling… Xn = 2ν… disproportionation… Xn = ν."
### 2.4 Initiator efficiency f（引发剂效率）

- 定义：引发剂均裂产生的自由基中真正引发聚合链的分数；通常 f < 1，主因是笼效应。
- 原文（第 780–783 行，约 p.212）："where [I] is the concentration of the initiator and f is the initiator efficiency. The initiator efficiency is defined as the fraction of the radicals produced in the homolysis reaction that initiate polymer chains. The value of f is usually less than unity due to wastage reactions."
### 2.5 Cage effect（笼效应）

- 定义：引发剂均裂产生的初级自由基对被困在"溶剂笼"内，相互再结合或发生其他副反应而失效，使 f < 1。
- 原文（第 1659–1667 行，约 p.230）："Lowering of f by reactions analogous to Eq. 3-68 is referred to as the cage effect… It is a general phenomenon observed in almost all initiation systems. About the only exceptions are the initiation systems such as Fe²⁺ + H₂O₂ → Fe³⁺ + HO• + HO⁻ which do not produce radicals in pairs."
- AIBN 实例（第 1677–1698 行）：AIBN 均裂生成 N₂ 与 2-cyano-2-propyl 自由基，可偶合为 tetramethylsuccinodinitrile（Eq. 3-84a）或 dimethyl-N-(2-cyano-2-isopropyl)ketenimine（Eq. 3-84b）。
### 2.6 Trommsdorff effect / gel effect / autoacceleration（凝胶效应/自加速）

- 定义：等温条件下，随转化率上升 Rp 反而上升的现象；本质是终止反应从动力学控制转为扩散控制，kt 下降远快于 kp。
- 原文（第 4316–4330 行，约 p.282–283）：*"the exact opposite behavior is observed in many polymerizations—the reaction rate increases with conversion… Such behavior is referred to as the gel effect… The terms Trommsdorff effect and Norrish–Smith effect are also used… The gel effect is observed under isothermal reaction conditions."*（第 4346–4349 行）
- 定量证据（表 3-17，第 4469–4482 行，22.5 °C MMA 本体聚合）：

- 转化率 0% → 50%：kp 变化不大（384→258），kt 从 4.42×10⁻⁴ → 4.03×10⁻⁶（下降约 2 个数量级），(kp/kt)^{1/2} 从 5.78×10⁻² → 40.6×10

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch3_report.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch3_report.md.md`
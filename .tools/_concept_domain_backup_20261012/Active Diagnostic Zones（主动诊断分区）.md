---
type: concept
title: "Active Diagnostic Zones（主动诊断分区）"
domain: [卫材研发, 变色与智能材料]
status: growing
updated: 2026-09-29
tags: [诊断分区, 力致变色, 防勒伤, 压力分布, 无源传感, 婴儿安全, HPC]
---

# Active Diagnostic Zones（主动诊断分区）

> One-line definition 一句话定义：把**力响应、无源**的可视化传感按**产品分区**布置的诊断架构——用最小的功能单元解决两类人因问题：**腰围耳贴的过紧（防勒伤）** 与 **体表压力分布的局部热点**。（中文：不追求整件「智能」，而是按分区放最小传感单元。）

## Mechanism / Structure 机理 / 结构拆解

1. **The framing idea 命题**：integrating **force-responsive, power-free** sensors turns commodity diapers into "smart" safety devices, solving complex human-factors challenges **without expensive electronics**。可译作：**无源 = 无电池、无芯片、无电子件**，这是它能进入一次性用品的先决条件。
2. **Zone 1 · Waistband tabs（防勒伤）**：integrated visual indicators trigger a high-visibility signal **when tensile force exceeds safe physiological thresholds**，providing immediate over-tightness warnings。（中文：拉力超阈值即显色报警，防勒伤。）
3. **Zone 3 · Surface area（压力分布）**：identifies **localised pressure "hot spots" across the entire product chassis** to optimise future product design and user safety。（中文：把整件产品的局部压力热点可视化，主要用于设计优化与安全评估。）
4. **Why zones rather than a "smart diaper" 为什么是分区而不是「智能纸尿裤」**：它把昂贵的全域电子方案替换为**按部位布置的无源指示单元**——每格只回答一个物理量（拉力 / 压力），因此不需要供能、不需要读数器、不需要回收电子件。
5. **The force gap is the central engineering problem 力值缺口是核心工程问题**：industrial mechanophores require extreme force（**40,000 PSI**）while the hygiene target range is **20–150 kPa**（microactuator range）；activation curves are annotated around **25–27 % strain**。因此必须**下移阈值**——原文给出的修法是 **"stabilization bridge"**：integrating gelling agents（e.g. **gelatin**）to tune rheology and lock signal stability across the product lifecycle。（中文：把力色团的工作力值从工业级降到卫材级。）
6. **Reversibility is a hard requirement for fit monitoring 可逆性是贴合监测的硬要求**：continuous fit monitoring **requires reversibility**；structural-colour materials（HPC）provide a **predictable power-law relationship** for real-time adjustment，而 naphthopyrans 提供的是**瞬态（modular）信号**——两类材料的用途不同，见 [[Printable Pressure-Activated Inks vs Covalent Mechanophores（力致变色两条落地路线）]]。
7. **Safety is the gatekeeper, and the gate is ingestion 安全闸门是「误食」**：the ultimate risk is **infant oral exposure and ingestion of diaper tabs / waistbands**。因 HPC 为 edible、non-toxic、biodegradable，原文把它称为**战略黄金标准**：它充当 **immediate regulatory shield**，可「**bypassing years of safety trials**」——即 **SAFETY = SPEED**。
8. **Where these zones land in the library's functional map 与库内功能层图谱的对应**：Zone 3（压力分布）与既有的压力传感功能层同类（[[智能尿裤功能层]] ②）；Zone 1（腰围拉力）对应「穿戴张力/贴合指示」，是力致变色相对热致变色的差异化落点（见 [[Mechanochromic变色纤维]]）。

## Key Parameter Table 关键参数表

| Parameter 参数 | Typical value / rule 典型值 / 规则 | Source 出处 |
|---|---|---|
| Architecture 架构 | force-responsive, **power-free** sensors；zonal deployment，无电子件 | [[Active Hygiene Roadmap（力致变色材料商业化路线图）]] |
| Zone 1 分区 1 | waistband tabs，anti-strangulation；indicator triggers when tensile force > safe physiological threshold | 同上 |
| Zone 3 分区 3 | surface-area pressure mapping；identifies localised pressure hot spots across the chassis | 同上 |
| Target force range 目标力值区间 | **20–150 kPa**（microactuator / hygiene range） | 同上 |
| Industrial mechanophore force 工业力色团力值 | 40,000 PSI（≈ 276 MPa） | 同上 |
| Activation strain annotation 激活应变标注 | 25–27 % strain；failure regime / signal loss 在卫生区间之外 | 同上（图注，OCR 残片） |
| Threshold down-shift method 阈值下移方法 | "stabilization bridge"：集成胶凝剂（e.g. gelatin）调流变、锁定全生命周期信号稳定性 | 同上 |
| Reversibility requirement 可逆性要求 | continuous fit monitoring **requires reversibility**；HPC 提供 predictable power-law relationship | 同上 |
| Preferred material (structural colour) 首选材料（结构色） | HPC（hydroxypropyl cellulose）：edible / non-toxic / biodegradable | 同上 |
| Ultimate safety risk 终极安全风险 | infant oral exposure & ingestion of tabs / waistbands | 同上 |
| Regulatory strategy 监管策略 | 用可食材料作 **immediate regulatory shield**，bypassing years of safety trials（SAFETY = SPEED） | 同上 |
| Clearance claims（源文声称） | EU 10-2011 migration（"zero skin migration verified"）；FDA 21 CFR；non-sensitization；oral toxicity | 同上 —— **声明，无报告** `[待验证]` |
| Cost 成本 | **来源未提供**（原文只称路径选择决定最终 COGS，无数字） | `[待验证]` |
| Supplier 供应方 | 材料侧候选见 [[CTI (Chromatic Technologies)]]、[[Henan Jiayida（河南嘉亿达）]]（均为库内既有页，本批不新建） | 见源页 manual_review |

> ⚠️ **No unsourced parameters 禁止无来源参数**：上表的力值区间（20–150 kPa / 40,000 PSI）、应变标注（25–27 %）均取自源演示稿的**图注**，源文本为 OCR 残片，**未给测试方法与样品定义**；合规四项以 **✓ 勾选清单**出现，**未附检测报告、限值与实验室名称**——在本库中一律标 `[待验证]`，**不得据此认为法规问题已解决**。

> 🔴 **manual_review（2026-09-29）**：本页涉及**面向婴儿的安全合规声明**（EU 10-2011 / FDA 21 CFR / 非致敏 / 口服毒性）。依 AGENTS.md §5，**此类合规结论属「跨来源矛盾取舍 / 核心结论」范畴，不得由 AI 自动采纳**；本页只记录源文声称并标注未验证。另：源页列出的**具名合作方管道与并购/收购标的**已按商务敏感处理，**不页面化**。

## Adjacent Concepts 相邻概念

- 材料与技术路线 材料与技术路线：[[Mechanochromic变色纤维]]、[[变色油墨]]、[[Printable Pressure-Activated Inks vs Covalent Mechanophores（力致变色两条落地路线）]]
- 并发批次已立页的相关概念（2026-09-29 追加交叉链接）：[[Mechanophore Mechanochromism（机械力致变色分子）]]、[[Structural Colour Mechanochromism（结构色力致变色）]]、[[Geometric Optical Mask（几何光学掩膜）]]、[[Chromism Taxonomy（变色现象分类）]]、[[Wetness Indicator Ladder（尿湿指示阶梯）]]、[[Signal Comprehension Gate]]
- 并发批次已立页的相邻对比（2026-09-29 追加）：[[Mechanochromic Routes Comparison（力致变色技术路线对比）]]（带成本指数与 TRL）、[[Mechanochromic Ink Supplier Comparison（力致变色油墨供应商对比）]]
- 功能层图谱 功能层图谱：[[智能尿裤功能层]]、[[智能尿裤功能层专利地图]]
- 材料载体 材料载体：[[细菌纳米纤维素]]、[[纳米纤维素（CNC、CNF、BNC）]]
- 供应侧候选 供应侧候选：[[CTI (Chromatic Technologies)]]、[[Henan Jiayida（河南嘉亿达）]]、[[Mechanophore Mechanochromism（机械力致变色分子）]]

## Lessons Learned 经验教训

> ✅ Verification（2026-09-29，source [[Active Hygiene Roadmap（力致变色材料商业化路线图）]]）：本页与库内 [[Mechanochromic变色纤维]]（seed 页，来源为 [[智能尿裤功能层专利地图]] 的引用）**互证并推进**——既有页指出力致变色对应「穿戴张力/贴合指示」且 K-C US7704589B2 拉伸变色专利**已失效**（即该方向有早期探索与 FTO 空间）；本批路线图进一步给出**分区落地方式（Zone 1/Zone 3）与力值缺口量化（40,000 PSI → 20–150 kPa）**。既有结论未被修正，属补充。（中文：既有「力致变色可用于贴合指示」的判断被本批数据细化到分区与力值。）

- **Lesson 1（把「智能」拆成无源单格）**：无源 + 分区是这套方案能进入一次性用品的根本原因。评审时应先问「是否引入电子件/电源/回收义务」，而不是先问变色性能。
- **Lesson 2（阈值下移是化学问题，不是器件问题）**：40,000 PSI → 20–150 kPa 的缺口约 **3 个数量级**，原文明示修法是胶凝剂等「稳定化桥」调流变，而不是灵敏度更高的传感器。
- **Lesson 3（安全闸门是误食，不是接触）**：终极风险被明确定义为**婴儿误食耳贴/腰围**。这改变了材料筛选项——**可食性（edibility）成为一等指标**，也是 HPC 被称为黄金标准的唯一理由。
- **Lesson 4（可逆 vs 不可逆是两种产品）**：贴合监测要「可逆」（HPC 结构色的幂律关系），而事件记录可用「不可逆」（naphthopyrans 的模块化信号）。选型前必须先确定是要**监测**还是要**记录**。
- **待补 `[待验证]`**：20–150 kPa 区间的**实测**激活/回复曲线与循环寿命；"stabilization bridge"（胶凝剂）的配方与迁移安全；合规四项的检测报告、限值与实验室；分区传感器的**成本量级**与印刷工序兼容性；婴儿误食场景的暴露评估。

## Sources 来源

- [[Active Hygiene Roadmap（力致变色材料商业化路线图）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Active Hygiene/Active_Hygiene_Roadmap.pptx.md`
- [[Mechanochromic变色纤维]] —— 库内页（力致变色材料侧基线）
- [[智能尿裤功能层专利地图]] —— 库内页（功能层与 FTO 基线）

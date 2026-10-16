---
type: concept
title: "回渗 Rewet"
domain: [卫材研发, 芯体与吸收]
status: growing
updated: 2026-09-30
tags: [rewet, 回渗, absorption-testing, capillary, desorption, SAP, ADL, liner]
---

# 回渗 Rewet

> 📌 **Page completed 2026-09-30** from 10 citing sources in the vault. All figures traced to their source pages. Anything not evidenced in the vault is marked `[待补]`.

## Definition 定义

Rewet（回渗）is the liquid that returns out of an absorbent article toward the skin under load. The vault's physical account: after being taken up by SAP, part of the liquid still sits as **毛细水 / 颗粒间隙水** in the topsheet and the top of the core; under skin pressure this fraction is **squeezed out onto the filter paper** — so the rewet reading is **extremely sensitive to load and to waiting time**（源：[[Rewet Test（回渗测试）]]）。回渗与滑渗是**互补指标而非重复**：回渗量液体「返出」，滑渗量液体「漏走」（源：[[Rewet Test（回渗测试）]]）。A mechanistic refinement from the 2025-12 study is that the **主贡献者是「本来就留在面层的液体」，而不是压力下从芯体挤出的液体**（源：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Methods benchmarked 方法数（参数矩阵） | 11 种方法（KC Lo/Hi、KC FIUP、KC Closed Cradle、P&G Duck、P&G Collagen BCC/AFC、China U Rewet、Diaper Testing Intl、NWSP 070.9.R1、Costco FQ Demo） | [[Rewet Method Parameter Matrix (xlsx)（回渗测试方法参数矩阵·11 方法）]] |
| Dosing-pressure range 加液压力跨方法范围 | 0 – 0.53 psi | [[Rewet Method Parameter Matrix (xlsx)（回渗测试方法参数矩阵·11 方法）]] |
| Dosing pressure 加液压力（分档） | KC Lo/Hi 低档 0.02 / 高档 0.4 psi；KC FIUP 0.25；KC Closed Cradle ~0.25；P&G Duck 0；P&G Collagen BCC 0.53；Collagen AFC 0.25 或 0.30；China U Rewet 0.29（psi） | [[Rewet Method Parameter Matrix (xlsx)（回渗测试方法参数矩阵·11 方法）]] |
| Liquid / temperature 液体与温度 | 仅 P&G Collagen BCC 用 Synthetic Urine，其余 10 种用 Saline（KC Closed Cradle 用 STCH Saline）；室温或 37 °C；China U Rewet 36 °C；Diaper Testing Intl 23 °C | [[Rewet Method Parameter Matrix (xlsx)（回渗测试方法参数矩阵·11 方法）]] |
| Load tiers 载荷三档（不可互换） | 国标 1.20 kg（直径 100 mm 压块）；U Rewet 国标回渗压块（1 min）；2×4 kg（合计 8 kg） | [[Rewet Test（回渗测试）]] |
| Single-hydrophilic topsheet 单亲面层 | first absorption ≈ 0.86–1.24 s，fifth 7.39–8.62 s；rewet 3.89–6.17 g（20 g/m², 5 specimens） | [[ES Fibre Hydrophilic Function and Applications]] |
| Multi-hydrophilic topsheet 多亲面层 | first absorption 1.39–1.86 s，fifth 1.96–2.41 s；rewet 0.84–1.32 g | [[ES Fibre Hydrophilic Function and Applications]] |
| AD liner + surge swap-in 互换 AD 面层+导流层 | Depend rewet ~0.51 g → 0.15–0.17 g（降幅约 3 倍） | [[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]] |
| TTM-00672 Closed Cradle 基准 | Always Discreet ≈ 0.4 g；AT Hybrid CD-Rod 变体 ≈ 0.1–0.3 g | [[2025.03.13 - GML update.pptx]] |
| TTM-00672 per-product rewet | DFF ≈ 0.44 g；DPP ≈ 0.46 g（最高）；AD 与 Kirkland ≈ 0.11–0.12 g（最低） | [[NWSP and ISO Test Methods Comparison 11-10-2022 updated.docx]] |
| BUFF BABY targets 双目标 | LPR 0.15 g / HPR 0.30 g（HPR 的 <0.3 g 机理未确认） | [[Rewet Quarterly Update 2025-08（设计原则落地与五个项目战绩）]] |
| Five-project measured gains 五项目实测 | GRIFFIN 0.26→0.20；LUGH 0.41→0.34；LOKI 0.62→≤0.32；AC4 4U 3.8→1.6 g | [[Rewet Quarterly Update 2025-08（设计原则落地与五个项目战绩）]] |

## Method / Mechanism 方法 / 机理

- **Capillary-pressure account 毛细压力解释.** Rewet in the closed-cradle configuration is **解吸（desorption）驱动**，解吸主要由**毛细作用**驱动，因此需逐层测毛细性；residual-fluid drivers are **wettability (θ)** and **pore radius (R)** via **Young–Laplace ΔP = −2γcosθ/R**（源：[[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]、[[2026-05-05 - QUINN.pptx]]）。
- **Two principle sets 两套机理原则.** Rewet = **Flowback + Desorption** 两套机理，各有原则集；贯穿原则是评估变异与能力（源：[[Rewet Quarterly Update 2025-08（设计原则落地与五个项目战绩）]]）。
- **Waiting time defines what is measured 等待时间决定测的是什么.** 注液后立即测（短等）读到**面层残液**；等待 10–15 min 后测读到**压力下长期未吸收液**——**2 min 与 15 min 是场景差别，不是严格程度差别**（源：[[Rewet Test（回渗测试）]]）。
- **Load is the first attribute 载荷是第一属性.** **8 kg（TTM-00623 高压段）与 1.20 kg（GB 国标）读到的不是同一个物理量**；引用回渗门槛前必须写明是哪一套（源：[[Rewet Test（回渗测试）]]）。
- **MicroCT localisation 残液定位.** 「MicroCT showed liner is holding fluid」——**残液不只存在于 surge/芯体，面层自身就是一个持液库**（源：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]）。
- **Pore-size distribution, not just average size 孔径分布同等重要.** AD 与 Depend 平均孔径相近，但 AD 分布窄、Depend 分布更宽、大孔更多；**小孔中的液体不会被非常大的孔拉出来**，从而把液体滞留（stranded）在导流层内——**Size distribution is just as important as overall size**（源：[[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]）。

## Hygiene Relevance 卫材关联

- **Method identity governs the number 方法身份决定数值.** K-C internal STM/TTM numbers are **not** directly interchangeable with ISO/NWSP external numbers; any competitive benchmark must state the method（源：[[NWSP and ISO Test Methods Comparison 11-10-2022 updated.docx]]）。这与 Cradle 协议的「注液点必须带产品类型与性别」同一逻辑（源：[[Cradle Intake Test（Cradle 摄入测试）]]）。
- **Liner + surge are the primary lever 面层与导流层是主杠杆.** 互换实验证明 **AD 的面层 + 导流层单独就足以把 Depend 回渗降到 AD 水平**，且 **AD 的卷曲纤维没有额外的回渗收益**（只利于摄入）——回渗差距定位在摄入系统（liner+surge），不在芯体（源：[[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]）。
- **Fibre size lever 纤维尺寸杠杆.** 大纤维（**1.3 d → 2.0 d**）降高压回渗（源：[[Rewet Quarterly Update 2025-08（设计原则落地与五个项目战绩）]]）。
- **Thinner core, rewet trade-off 薄芯体的回渗权衡.** AT Hybrid 较 SAM/fluff 减少木浆（**8.5→3.8 g**）与 SAP（**19.9→15.3 g**），回渗可通过面层键合开放度与 Lertisan 处理量调控，存在明确的摄入/防漏权衡（源：[[2025.03.13 - GML update.pptx]]）。
- **Competitive frame 竞争口径.** AD 打出「40% DRIER」竞品宣称（加载 160 mL、等待 50 s）；surge 材料中回渗最优为 Strahag SS7CT8H60（源：[[2026-05-05 - QUINN.pptx]]）。
- **Upstream/material basis 物质基础.** AUL / GBP 是回渗的物质基础（源：[[SAP性能指标（CRC AUL GBP Vortex）]]）；回渗量亦随面层亲水整理的耐久性（多亲 vs 单亲）而显著变化（源：[[ES Fibre Hydrophilic Function and Applications]]）。

## Open Questions 待补

- **U Rewet 国标回渗压块与 TTM-00623 低压段反渗板**的**实际质量 / 压强**——两份原文均未给出（源：[[Rewet Test（回渗测试）]]）。
- **STM-00059-2 的完整操作规程**未在摘要中给出（源：[[Rewet Test（回渗测试）]]）。
- **HPR 的 <0.3 g 机理未确认**（源：[[Rewet Quarterly Update 2025-08（设计原则落地与五个项目战绩）]]）。
- **毛细测试结果未给出**：12/8/25 完成的是材料属性与显微表征，毛细测试结果本件未给出（源：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]）。
- 本页数值来自**多套不可互换的方法口径**（Closed Cradle / FIFE / NWSP / 国标），跨行比较前须人工确认方法与载荷档位。

## Related Sources 关联来源

- [[Rewet Test（回渗测试）]]
- [[Rewet Method Parameter Matrix (xlsx)（回渗测试方法参数矩阵·11 方法）]]
- [[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]
- [[Rewet Quarterly Update 2025-08（设计原则落地与五个项目战绩）]]
- [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]
- [[ES Fibre Hydrophilic Function and Applications]]
- [[Cradle Intake Test（Cradle 摄入测试）]]
- [[2025.03.13 - GML update.pptx]]
- [[2026-05-05 - QUINN.pptx]]
- [[NWSP and ISO Test Methods Comparison 11-10-2022 updated.docx]]
- [[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]
- [[Rewet Protocols Compared（回渗测试口径对比）]]
- [[Absorbent Product Testing]]
- [[Absorbent Technology]]
- [[Absorbent Technology Introduction]]
- [[Ancient Organic Dyes and Pigments Chemistry]]
- [[Characterisation, testing and modelling of nonwoven fabrics]]
- [[Cross-linked Cellulose and Derivatives]]
- [[Fluid Absorption in High Bulk Nonwovens]]
- [[Handbook of Nonwovens]]
- [[Liquid Flow in Porous Structures]]
- [[Nonwoven fabric finishing]]
- [[Nonwovens in Absorbent Materials]]
- [[Products and Technology Perspective]]
- [[The Role of Surfactants]]


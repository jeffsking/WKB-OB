---
type: source
title: "Mechanochromic Fluorescent Polymers with AIE Features"
source_type: book
source_path: RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mechanochromic_Fluorescent_Polymers_AIE/Mechanochromic_AIE_深度拆解.md.md
original_link: ""
date_published: 2019
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
author: "Andrea Pucci"
edition: ""
publisher: "Sensors (MDPI), 19, 4969"
year: 2019
isbn: ""
original_language: "EN"
parent_book: "[[Mechanochromic Photonic Sensors]]"
key_claims:
  - "AIE (aggregation-induced emission) solves ACQ, the bottleneck that made solid-state fluorescent sensors impossible before 2001."
  - "Mechanochromic fluorescence = force -> change in AIEgen aggregation extent -> optical read-out; ON-OFF is often invisible, OFF-ON (turn-on) is the commercially viable read-out."
  - "Best current architecture: AIEgen in core-shell microcapsules — OFF until rupture, 10 um resolution, damage sizes 94-376 um resolved, stable to 220 C."
  - "Turn-on onset at epsilon = 0.13% strain, 7x intensity at 65% strain (TPE-4N, 1 um coating) — the field's hardest sensitivity number."
  - "Covalent bonding beats dispersion for skin-contact products: covalent probes are homogeneous and prevent diffusion/segregation over time and use."
pages_linked: ["[[Mechanochromic Photonic Sensors]]", "[[机械变色 Mechanochromic]]", "[[聚集诱导发光 AIE]]", "[[TPE Tetraphenylethylene]]", "[[微胶囊 Microencapsulation]]", "[[变色油墨 Color-Changing Ink]]", "[[结构色 Structural Color]]"]
---

# Mechanochromic Fluorescent Polymers with Aggregation-Induced Emission Features

## One-line Position 一句话定位
The reference review (Pucci, Sensors 2019) for converting mechanical stress into optical output using AIE fluorophores — and the most manufacturing-relevant source in this vault for self-diagnosing film/laminate defects and strain-threshold indicators.

## Key Numbers & Conclusions 提炼数字与结论

| 项目 Item | 数值/结论 Value | 备注 Note |
|---|---|---|
| AIE 发现 | Tang 等, 2001 | RIM（分子内运动受限）机理 |
| SBS 中 TPE 分散添加量 | 0.01 wt % | λ_em ≈ 460 nm；draw ratio 1→3 可检测；可逆 |
| PU 中共价 TPE-diol | 0.02–0.1 wt % | 479→468 nm 蓝移；寿命 1.32→0.89 ns；应变至 213 % |
| PU 配方 | PCL-diol Mn=4000 + HDI + BDO，硬段 ≈25 % | DMF 浇铸 70 °C / 12 h，膜 0.1 mm |
| 微胶囊 | 核=1 wt % TPE/乙酸己酯；双层 PU/脲醛壳；112±10 µm | 稳定至 220 °C；环氧中用量 10 wt % |
| 微胶囊传感 | OFF→ON ≈450 nm，室温 ≈5 min 达最大；分辨率 10 µm | 分辨 94 / 140 / 171 / 222 / 376 µm 损伤 |
| 共聚 PDMS | 最高 7.8 wt % 四乙烯基 TPE | 氢硅化键合 |
| 开点灵敏度基准 | ε = 0.13 % 起；20 % 内持续增强；65 % 时 7× | TPE-4N，涂层 1 µm，λ_em 520 nm；150 °C/20 min 定 OFF 态 |
| 交叉响应（PMMA） | 125 °C/10 s → 536→458 nm；CH₂Cl₂ 蒸气 30 s 消色 | 说明机敏/热敏/汽敏必须解耦 |
| 自愈耦合 | 修复剂存储模量 →10⁵ Pa，与蓝色发光同步上升 | 光学信号作为过程控制变量 |

## Core Mechanism 核心机理

- **ACQ 是旧世界的天花板** — "the aggregation of aromatic planar fluorophores usually suffers from emission quenching phenomena in concentrated solutions and in the solid state, known as aggregation-caused quenching (ACQ), which strongly limits the number of accessible fluorophores" (L36-L38)
- **AIE 的反向开关** — "arises from the restriction of fluorophore intramolecular motions (RIM) that are typical of those molecules whose structure consists of two or more units that can dynamically rotate against each other" (L43-L45)
- **力→聚集→光的因果链** — "optical responses towards mechanical stimuli can be greatly amplified upon changes in the aggregation extent of AIEgens in the polymeric matrix" (L107-L110)
- **OFF-ON 优于 ON-OFF** — ON-OFF "appears sometimes scarcely detectable by the naked eye" (L432-L435)；OFF-ON 由"压缩 + 无定形松散堆积 → 结晶诱导增强"实现 (L176-L183)
- **最终技术路线判决** — "The extreme sensitivity of the AIEgen core to the minimum deformation extent combined with their encapsulation within ductile microcapsules appear so far the best solution … with a ratiometric response that gives access to quantitative assessment" (L634-L638)
- **可执行的分子改造策略** — "Innovation would be in the chemical transformation of the typical ACQ fluorophores into AIE emitters by functionalizing the planar chromophoric nuclei with twisted propeller-shaped moieties" (L641-L643)

## Business Connection Points 业务连接点

- **热熔胶 / 弹性体自诊断（最可直接迁移）** — 基准体系正是 SBS 苯乙烯类嵌段共聚物，与卫生用品热熔胶（HMA）和弹性体条/层压弹性膜同族。ppm 级 AIE 示踪剂可报告胶层应变、弹性条过拉伸、以及相形态变化（即胶的老化），免破坏剥离测试；响应可逆，与反复穿戴循环兼容。
- **复合层微孔/泄漏自报警** — 微胶囊体系 220 °C 热稳定余量高于典型 HMA 涂布温度（~150–170 °C），有机会在狭缝涂布/喷涂下存活；划伤即点亮，可作透气背膜与膜-无纺布层压件的在线光学质检。约束：112 µm 与无纺布纤维直径同级，用于 <50 µm 薄膜需缩小。
- **消费品指示器必须是点亮式** — 湿/饱和/泄漏指示要"出现"而非"消失"：无信号与产品失效或传感器失效无法区分。
- **比率型 = 分级而非报警** — 荧光强度随 TPE 浓度与胶囊数目定量变化，可做干/部分/满的分级指示（而非单条湿敏线），对机构护理监测与相机式智能尿裤读取有直接价值。
- **防伪与开包历史指示** — 微囊化 AIE 可作防篡改/开包历史指示，0.01–0.1 wt % 染料成本可忽略，366 nm 长波 UV 即可读出。
- **共价 vs. 分散的选型规则** — 皮肤接触产品有染料迁移与析出风险，共价键合（PU + HDI/BDO/PCL-diol，0.02–0.1 wt %）路线已验证且与卫生用 PU 弹性膜化学完全兼容；分散法适合包装但不宜用于皮肤面层。
- **SAP 方向假设（外推，原文未涉及）** — AIE 发光报告局部黏度/自由体积与网络约束；共价挂接到交联聚丙烯酸 SAP 网络上的探针在吸水溶胀（约束丧失）时应转 OFF，原理上可可视化凝胶堵塞、溶胀梯度与未利用芯层容量。**属研究假设，非原文结论。**

## Gaps / Risks 缺口与风险
原文未提供：湿度/尿液电解质干扰、TPE/TPE-4N 的生物相容性与法规状态、成本、货架期光稳定性、在无纺布或纤维（而非薄膜/涂层/块体树脂）中的响应，以及任何定量应力-光学本构方程。

## Related Pages 关联页面
- 同域合集 Sibling collection：[[Mechanochromic Photonic Sensors]]
- 概念 Concepts：[[机械变色 Mechanochromic]]、[[聚集诱导发光 AIE]]、[[变色油墨 Color-Changing Ink]]、[[结构色 Structural Color]]、[[微胶囊 Microencapsulation]]
- 相关主题：[[SAP]]（吸水树脂网络，外推假设）、热敏变色解耦

## Source 原文
- 本地路径 Local path：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mechanochromic_Fluorescent_Polymers_AIE/Mechanochromic_AIE_深度拆解.md.md`
- 原文链接 Original link：doi:10.3390/s19224969

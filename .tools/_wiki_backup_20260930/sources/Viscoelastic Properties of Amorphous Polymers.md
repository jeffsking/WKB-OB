---
type: source
title: "Viscoelastic Properties of Amorphous Polymers"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Viscoelastic Properties/Viscoelastic Properties_report.md.md"
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "The modulus–temperature (or modulus–time) curve of an amorphous polymer divides into four regions: Glassy State → Tg Transition → Rubbery Plateau → Terminal Flow."
  - "In the Tg region 'cooperative motions of segments now occur, but the motions are sluggish (a maximum in tan δ curves are observed in DMA experiments)' — the tan δ peak is the DMA signature of Tg."
  - "The Maxwell model gives exponential stress relaxation: 'σt = σ0 exp[−t/τ], where τ = η/E, Relaxation time' (source lines L356–L369)."
  - "Maxwell constitutive equation: 'dε/dt = dσ/(E dt) + σ/η'; the single-exponential prediction cannot fit the real sigmoidal data, implying a continuous relaxation spectrum / generalized Maxwell model."
  - "Definitions: 'G(t) = σ(t) / γ0 — Relaxation modulus', 'J(t) = γ(t) / σ0 — Creep compliance', with G(t) = 1/J(t) stated in the source."
  - "Time–temperature equivalence permits building a master curve from short-time variable-temperature experiments instead of long-time isothermal tests."
summary_cn: "无定形聚合物粘弹性讲义拆解：模量-温度曲线四区域（玻璃态/Tg转变/橡胶平台/末端流动）、Maxwell 模型应力松弛 σt=σ0·exp(−t/τ) 与 τ=η/E、G(t)/J(t) 定义与时温等效原理；对热熔胶与弹性纤维的黏弹性表征有直接方法论价值。"
tags: ["source/book", "viscoelasticity", "glass-transition", "Maxwell-model", "relaxation-modulus", "creep-compliance", "time-temperature-equivalence", "DMA", "tan-delta"]
tags_zh: ["粘弹性", "玻璃化转变", "麦克斯韦模型", "松弛模量", "蠕变柔量", "时温等效", "动态力学分析"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Adhesive Handbook Part 2 Fundamental Aspects]]", "[[Odour Management & Polyolefin Hot Melt Adhesive Platform — Henkel Tech Seminar（气味管理技术介绍·汉高技术交流）]]", "[[EP2456819B1 Olefin Block Copolymer Hot Melt Adhesive (Bostik)]]", "[[Pin-Hole Module, Targeted Fluff Distribution & Elastic Recovery Process Review（新材料开发与弹性恢复工艺探讨）]]", "[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]"]
---

# Viscoelastic Properties of Amorphous Polymers 无定形聚合物的粘弹性

> Source: lecture notes / chapter-type teaching material *Viscoelastic Properties of Amorphous Polymers* (无定形聚合物的粘弹性), compiled in `Viscoelastic Properties_report.md.md`; the report indexes the original text line by line (L21–L416). No publication year is stated in the source → `date_published: 0`. The only dated literature reference in the source is *H. A. Flocke, Kolloid–Z. Z. Polym., 180, 188 (1962)* (semicrystalline section, L148–L149).

## Scope and method 范围与方法

Document type 文档类型：聚合物粘弹性教学讲义（lecture notes），组织方式为"定义—模型—公式—图示"层级。

- Experimental side 实验侧：DMA（Dynamic Mechanical Analysis 动态力学分析）— tan δ 曲线在 Tg 处出现峰值；拉伸-松弛实验 σ(t)/ε；蠕变-恢复（Creep and Recovery）。
- Theoretical side 理论侧：基于 Hooke's Law（弹簧）与 Newtonian fluid（阻尼）的线性叠加，构建 Maxwell 微分模型并求解。
- Key question 核心问题：为什么聚合物的模量 E(t) 会跨越十几个数量级的时间尺度？温度与时间如何等效？

Measurement definition 测量定义 (L76–L80)：
> "Stretch sample an arbitrary Amount, then measure the Stress required to maintain This strain. Then E(t) = σ(t)/ε"

## Four regions of amorphous behaviour 无定形粘弹性四区域（L100–L135）

| Region 区域 | Source wording 原文描述 | Line 行号 |
| --- | --- | --- |
| Glassy State 玻璃态 | "conformational changes severely inhibited"（构象变化被严重抑制） | L123–L124 |
| Tg Region 玻璃化转变区 | "cooperative motions of segments now occur, but the motions are sluggish (a maximum in tan δ curves are observed in DMA experiments)" | L125–L129 |
| Rubbery Plateau 橡胶平台区 | "τ becomes shorter, but still longer than the time scale for disentanglement"（τ 变短但仍长于解缠结时间尺度） | L130–L133 |
| Terminal Flow 末端流动区 | "the time scale for disentanglement becomes shorter and the melt becomes more fluid like in its behaviour" | L134–L135 |

## Relaxation mechanism 松弛的微观机理（L85–L98）

> "First consider a hypothetical isolated chain in space, then imagine stretching this chain instantaneously so that there is a new end-to-end distance. The distribution of bond angles (trans, gauche, etc) changes to accommodate the conformations that are allowed by the new constraints on the ends."

> "we say the chain RELAXES to the new state and the relaxation is described by a characteristic time τ"

Microscopic picture 微观图像：孤立链被瞬时拉伸 → 产生新的端到端距离 → 键角分布（trans/gauche 等）重新平衡以达到新约束允许的构象。

## Constitutive definitions 本构定义（L152–L169）

| Quantity 量 | Definition 定义 | Meaning 含义 |
| --- | --- | --- |
| Relaxation modulus 松弛模量 | "G(t) = σ(t) / γ0" | 恒定应变下应力随时间的衰减 |
| Creep compliance 蠕变柔量 | "J(t) = γ(t) / σ0" | 恒定应力下应变随时间的增长 |
| Relation 关系 | "G(t) = 1 / J(t)" | 源文本给出的互逆关系（仅在线性单 Maxwell 元情形严格成立，[待验证]） |

Linearity premise 线性前提：
> "We will only consider LINEAR MODELS ie if we double G(t) [or σ(t)], then γ(t) [or ε(t)] also increases by a factor of 2 (small loads and strains)."

## Mechanical elements and Maxwell model 机械单元与 Maxwell 模型（L172–L416）

Basic elements 基本单元：Hooke spring 弹簧 σ = Eε；Newtonian dashpot 阻尼 τ_xy = ηγ̇（串联 = Maxwell）。

Constitutive equation 微分方程 (L271–L275)：
> "dε/dt = dσ/(E dt) + σ/η"

Stress relaxation 应力松弛（核心推导, L356–L369）：
> "σt = σ0 exp[−t/τ], where τ = η/E, Relaxation time"

Model limits 模型局限：
- Creep 蠕变：Maxwell 模型只给出瞬时弹性 + 恒定速率粘流，**无法**描述延迟弹性与恢复；
- Stress relaxation 应力松弛：单指数预测**无法**拟合真实的 S 形 Log E(t) vs Log time 曲线（原文 L396–L416 的"Maxwell model / Real data"对比图）；
- Conclusion 结论：真实聚合物需要**广义 Maxwell 模型 / 连续松弛时间谱**。

Typical experimental curves 典型实验曲线：Creep & Recovery = 弹性响应 + 延迟弹性响应 + 永久形变（L175–L190）；Stress Relaxation = Log E(t) vs Log time(sec) 的 S 形曲线（L195–L220）。

## Time–temperature equivalence 时温等效（L21–L82）

- Chart 图表：Log E vs Temperature（10 sec modulus），标注 Glassy region / Rubbery plateau / Cross-linked elastomers / Melt / Low molecular weight.
- Principle 原理：升高温度等价于拉长观察时间；可用短时间的变温实验代替长时间等温实验来构造主曲线（master curve）。

## Semicrystalline polymers 半结晶聚合物（L138–L149）

- 非晶域运动被晶区（crystallites）约束 constrained by crystallites；
- Tg 以上出现结晶/非晶耦合过程；
- 难以一概而论，需逐聚合物分析 case-by-case；
- Data source 数据来源：*H. A. Flocke, Kolloid–Z. Z. Polym., 180, 188 (1962)*.

## Concept index 概念索引

| Concept 概念 | Definition 定义 | Source note 来源注记 |
| --- | --- | --- |
| Viscoelasticity 粘弹性 | 同时表现弹性与粘性响应的力学行为；文中以 spring + dashpot 串/并联体现 | §3.1 |
| Glass transition Tg 玻璃化转变 | 无定形聚合物由玻璃态向高弹态过渡的温度区间；DMA 中 tan δ 峰值即标志 | §3.2 |
| E' / E" 储能/损耗模量 | 原文未直接出现 E'/E" 符号，通过 tan δ 峰值与 G(t)、E(t) 间接使用；tan δ = E"/E'，Tg 处取最大 | §3.3 |
| Amorphous polymer 无定形聚合物 | 无长程有序结构；模量-温度曲线分为四区域 | §3.4 |
| Maxwell model 麦克斯韦模型 | 弹簧与阻尼串联；σt = σ0·exp(−t/τ)，τ = η/E | §3.8 |

## Hygiene implication 卫材关联

Relevant, mainly as **methodology** rather than as product data:
1. **热熔胶（hot-melt adhesive）表征**：EVA/SBC/烯烃基热熔胶的开放时间、初粘与持粘本质是粘弹性松弛谱问题；τ = η/E 说明粘度与模量共同决定松弛快慢——配方调整任一参数都会移动粘合窗口。可用 DMA 的 tan δ 峰值定义胶的 Tg，据此判定低温脆断风险。
2. **蠕变/应力松弛测试**：弹性腰围、皮筋（spandex）与拉伸复合材料的"拉力衰减"即应力松弛，J(t)/G(t) 是可直接套用的评价量；本源给出的线性前提（small loads and strains）提醒测试载荷必须落在小应变区。
3. **时温等效的实用价值**：用短时变温 DMA 主曲线预测长期蠕变，可显著缩短材料筛选周期（尤其对加速老化与货架期评估）。

## Related Sources 关联来源

- [[Adhesive Handbook Part 2 Fundamental Aspects]] — 胶黏剂基础原理，粘弹性在粘接中的工程化表述。
- [[Odour Management & Polyolefin Hot Melt Adhesive Platform — Henkel Tech Seminar（气味管理技术介绍·汉高技术交流）]] — 聚烯烃热熔胶平台的产业侧数据。
- [[EP2456819B1 Olefin Block Copolymer Hot Melt Adhesive (Bostik)]] — 烯烃嵌段共聚物热熔胶专利，粘弹性配方实例。
- [[Pin-Hole Module, Targeted Fluff Distribution & Elastic Recovery Process Review（新材料开发与弹性恢复工艺探讨）]] — 弹性恢复工艺，对应蠕变-恢复与永久形变议题。
- [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] — 粘度（η）作为 τ = η/E 中的关键参数，与成本耦合。

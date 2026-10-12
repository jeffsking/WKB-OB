---
type: source
title: "Manufactured Fibre Technology Ch04 Melt-Spinning Processes"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Manufactured_Fibre_Technology/Manufactured Fibre Technology · analysis_ch04.md.md
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Melt-spinning is the simplest method of fibre manufacture, mainly because it does not involve problems associated with the use of solvents."
  - "A major development was the 1970s transition from conventional spinning at wind-up speeds of around 1000 m/min to high speed spinning at 3000 m/min and above."
  - "Efficient filtration brings the breakage rate below six breaks per 1000 kg production and reduces the frequency of nubs or undrawn portions in the spun filament."
  - "Spinning dynamics switches with speed: up to 1000-2000 m/min it is considerably affected by the rheological force; at high velocities the dominant role is played by the air drag force."
  - "Induced crystallinity results in an abrupt rise of velocity, i.e. an almost instantaneous change from a viscous melt to a semicrystalline solid, consistent with the observed necking of the spinline."
  - "A 1% variation in extrusion temperature can result in a 10% variation in spinline stress, which can significantly increase the coefficient of variation of filament denier."
summary_cn: "熔体纺丝工艺总纲：从挤出机/喷丝组件/冷却/上油/卷绕的产线构成，到常速与高速纺（1000 → 3000 m/min 以上）的受力机制切换（流变力主导 → 空气阻力主导）、应力诱导结晶引发颈缩，以及 1% 挤出温度波动放大为 10% 纺丝线应力的均匀性铁律。"
tags: ["source/book", "melt-spinning", "spinline", "POY", "high-speed-spinning", "spinneret", "process-control", "Manufactured Fibre Technology"]
tags_zh: ["源摘要/书", "熔体纺丝", "纺丝线", "预取向丝", "高速纺丝", "喷丝板", "工艺控制", "人造纤维技术"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Manufactured Fibre Technology]]", "[[Manufactured Fibre Technology Ch03 Fluid Flow in Fibre Spinning]]", "[[Meltblown Nonwoven（熔喷非织造布）]]", "[[Nonwoven Process Classification（非织造布工艺分类）]]", "[[PPC 纺粘试产记录（2026-05-01）]]", "[[Coform Composite Nonwoven（熔喷-木浆复合非织造）]]"]
---

# Melt-Spinning Processes 熔体纺丝工艺

> Source: Manufactured Fibre Technology, Ch.04, pp.67–95.

## Scope 本章范围

全书的**工艺执行层总纲**：从挤出机（extruder 挤出机）、纺丝歧管（spin manifold 纺丝歧管）、喷丝组件与喷丝板（spinneret 喷丝板）、冷却（quenching 冷却固化）、上油（finish application 上油）到卷绕（winder 卷绕），并重点对比**常速纺丝与高速纺丝（high speed spinning 高速纺丝）**。子节：4.1 引言、4.2 熔纺生产线、4.3 变量与无断头条件、4.4 高速纺特征、4.5 关键参数沿纺丝线变化、4.6 纺丝中结构形成、4.7 集成纺拉（SD, spin-draw 纺拉一步法）、4.8 其他纤维制备技术。

>"melt-spinning is the simplest method of fibre manufacture, mainly because it does not involve problems associated with the use of solvents." (p.67)

## Speed Regimes 速度区间与产品等级

>"A major development in the area of melt-spinning was the transition in the 1970s from conventional spinning at wind-up speeds of around 1000mmin-1 to high speed spinning at speeds of 3000mmin-1 and above." (p.67)

| 产品等级 Grade | 中文 | 卷绕速度区间 Wind-up speed | 结构特征 Structure | 页码 p. |
|---|---|---|---|---|
| LOY | 低取向丝 | 低速（常速区） | 低取向 | 81 |
| MOY | 中取向丝 | 中速 | 中取向 | 81 |
| POY | 部分取向丝（partially oriented yarn） | **2800–4000 m/min** | 高取向、近乎无结晶 | 81 |
| HOY | 高取向丝 | 超高速 | 高取向 | 81–82 |
| FOY | 全取向丝 | 超高速 | 高取向 + 结晶 | 81–82 |

## Production Line 产线构成与工艺规范

| 单元 Unit | 中文 | 关键规范 Specification | 页码 p. |
|---|---|---|---|
| Extruder 挤出机 | 挤出机 | 单螺杆；直径 **45–300 mm**；长径比 **L/D 28–33**；含三区与混合区 | 71 |
| Spin manifold 纺丝歧管 | 纺丝歧管 | 熔体分配与保温 | 72 |
| Metering pump 计量泵 | 计量泵 | 精度约 **±3 %** | 73 |
| Spinning pack / spinneret 纺丝组件与喷丝板 | 喷丝组件 | 过滤 + 分配 + 挤出成孔 | 73–74 |
| Quenching 冷却系统 | 冷却固化 | cross-flow / in-flow / out-flow 三类 | 75 |
| Finish application 上油 | 上油 | 集束、抗静电、摩擦控制 | 76 |
| Winder 卷绕装置 | 卷绕 | 有无导丝盘（godet 导丝盘）两种路线 | 77 |

- **过滤决定断头率**：>"Efficient filtration brings down the breakage rate to below six breaks per 1000 kg production and also reduces the frequency of nubs or undrawn portions in the spun filament." (p.69)
- **模口膨胀（dieswell 模口膨胀）**：>"The molten polymer, on emerging from the spinneret, bulges slightly due to release of elastic energy stored during shear flow" (p.69) —— 承接第 3 章的弹性储能释放机理。
- **纺丝线（spinline 纺丝线）**：从喷丝孔出口到卷绕点的熔体流/纤维流全程，是本章核心研究对象（p.83）。

## Spinline Dynamics 纺丝线动力学：受力机制随速度切换

>"For low velocities (up to 1000-2000mmin-1), spinning dynamics is considerably affected by the rheological force... For high velocities, the dominant role is played by the air drag force." (p.84)

即：**低速段流变力主导 → 高速段空气阻力主导**（Fig. 4.8 各张力分量贡献，p.84）。这决定了冷却方式与束丝设计的差异。

### 应力诱导结晶与颈缩

>"the induced crystallinity results in an abrupt rise of velocity, suggesting an almost instantaneous change from a viscous melt to a semicrystalline solid; this is consistent with the observed necking of the spinline." (p.87)

颈缩（necking 颈缩）= 结晶诱发的纺丝线直径急剧突变（p.87）；高速下成核方式为**行列成核（row nucleation 行列成核）**——沿应力方向形成、垂直生长为片晶（p.92）。

## Process Sensitivity 工艺敏感度铁律

>"Even a variation of 1 % in extrusion temperature, for example, can result in a 10% variation in spinline stress, which in turn can give rise to a significant increase in the coefficient of variation of filament denier." (p.89)

**1 % 温度波动 → 10 % 纺丝线应力波动 → 纤度 CV 显著恶化**（约 10 倍放大）。严格温控是产品均匀性的先决条件。

无断头纺丝（break-free spinning 无断头纺丝）的两条件与 Ziabicki/Walczak 变量三分法（独立变量 / 次级变量 / 结果变量，p.79–80）构成工艺量化框架；卷绕速度（take-up velocity 卷绕速度）属独立变量，是决定取向与产品等级的关键参数（p.79）。

## Source Quality 源文质量注记

- ✅ 亮点：以"状态变量耦合（coupling of state variables）"统一表达复杂纺丝过程；"低速流变主导—高速空气阻力主导"的切换规律具工程洞察；Table 4.1 以成本指数对比三工艺（p.95）。
- ⚠️ 不足：Fig. 4.9、4.12、4.13 因文本提取失真，曲线细节难以复原 —— 沿程分布定量值需回查原书 [待验证]；SD 工艺仅 "briefly described"（p.69）；Table 4.1 成本为"calculated costs... assuming the cost of the conventional two-step process to be 100"（p.94），属示例性计算而非实测，外推需谨慎。
- 数据性质：温度与速度梯度分布为"based on simulation using the energy balance equation and the constitutive equation"（p.86）—— **模型计算值**，非实测。

## Hygiene Implication 卫材关联

- **纺粘（spunbond 纺粘）就是熔纺 + 直接成网**：本章的挤出—计量—喷丝—冷却—牵伸链条即纺粘线的工程骨架；POY 概念（2800–4000 m/min，高取向近乎无结晶，p.81）对应纺粘"高速牵伸取得取向但结晶度低"的状态，是纺粘布强力与热收缩行为的来源。见 [[Nonwoven Process Classification（非织造布工艺分类）]]。
- **空气阻力主导区 = 熔喷与高速纺粘的提速瓶颈**：速度进入 1000–2000 m/min 以上后空气阻力成为主控力（p.84），意味着提速必须同步重设计冷却风场与牵伸器，而非单纯加大卷绕速度。见 [[Meltblown Nonwoven（熔喷非织造布）]]。
- **1 % → 10 % 的放大律是克重 CV 的根因线索**：挤出温度/熔体温度的小幅波动被放大为纺丝线应力波动，最终表现为纤度与克重 CV 恶化 —— 对超低克重（<10 gsm）纺粘与熔喷尤为致命，是 REL 超薄芯体包覆层均匀性的上游约束。
- **过滤与断头率**：<6 断头/1000 kg（p.69）是连续生产指标；凝胶与气泡造成的 nubs（未牵伸点）在无纺布上表现为硬点与强力薄弱点。
- **熔纺无需溶剂 = 聚烯烃纤维的成本与环保优势**：PP/PE 纺粘与熔喷全流程无溶剂回收，这是其相对溶液法（如部分纤维素纤维）成本领先的结构性原因，也解释了为何 PP 熔喷料对熔指（MFR）与分子量分布如此敏感。
- **试产与工艺窗口**：[[PPC 纺粘试产记录（2026-05-01）]] 与本节的挤出机 L/D、计量泵精度、冷却方式等规范可直接对照。
- **颈缩与应力诱导结晶**：熔喷超细旦化时的直径突变与结晶瞬变，参见 [[Coform Composite Nonwoven（熔喷-木浆复合非织造）]]。

## Related Sources 关联来源

- [[Manufactured Fibre Technology]] — book index
- [[Manufactured Fibre Technology Ch03 Fluid Flow in Fibre Spinning]] — 上一章：剪切流/拉伸流与可纺性
- [[Meltblown Nonwoven（熔喷非织造布）]]
- [[Nonwoven Process Classification（非织造布工艺分类）]]
- [[PPC 纺粘试产记录（2026-05-01）]]
- [[Coform Composite Nonwoven（熔喷-木浆复合非织造）]]

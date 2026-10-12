---
type: source
title: "SAP Grade Selection - Three-PPT Comparison（SAP 选型三份 PPT 对比 · 中文版）"
source_type: 提案
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP选型分析_三PPT对比_中文版.docx.md
original_link: ""
date_published: 2026-09
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "Recommended architecture is a three-grade layered structure: LG LK804ND as an independent thin skin-side layer, plus a poly-side blend of Nuoer KC-511 (fast swelling) and Nuoer NR-950 (delayed swelling) at a 36:64 ratio, with a REL five-fibre TAB layer (24 gsm) in between（中文：推荐三牌号分层——皮侧 LK804ND 独立薄层 + 聚侧 KC-511/ NR-950 按 36:64 错峰混合 + 中间 REL 五纤 TAB 层 24 gsm）"
  - "The core mechanism is staggered swelling kinetics in the TIME dimension (not spatial layering): the fast grade handles insults 1-2 while the delayed grade (51 s vortex) only engages at insults 3-4, so the gel bed is never blocked at once（中文：核心机理是时间维度的错峰膨润，而非空间分层）"
  - "Single-point free-swell values can mislead: two very different formulations can show identical single-point numbers; only a sequential 4-insult (gush) test reveals whether staggering works（中文：单点自由溶胀会骗人，只有顺序 4 次冲击测试能暴露错峰是否真生效）"
  - "PPT 3 designs 13.5 g total SAP with 387 mL capacity at 1.6x safety factor (62% utilisation), versus PPT 2's ~14.9 g / 286 mL / 1.3x; the insult protocols also differ (40/50/60/70 = 220 mL incremental vs 60x4 = 240 mL at real intervals)（中文：PPT 3 为 13.5 g / 387 mL / 1.6× 安全系数、利用率 62%；PPT 2 约 14.9 g / 286 mL / 1.3×；冲击协议亦不同）"
  - "Main residual risk: SAP3 (NR-950) has GBP 8 and vortex 51 s and relies entirely on REL layer activation (TAB Zone 2 at 138-143 C with strong cooling below 40 C); if REL activation drifts, the PPT 2 N8+710 architecture is the fallback（中文：主要遗留风险——NR-950 GBP 仅 8、vortex 51 s，导流完全依赖 REL 活化窗口，一旦漂移则退回 PPT 2 架构）"
pages_linked: ["[[SAP Architecture Options - Three PPT Routes（三份 PPT SAP 架构路线对比）]]", "[[SAP错峰膨胀]]", "[[Multilayer SAP Core（多层SAP芯体）]]", "[[REL增强层]]", "[[Gel Blocking（凝胶阻塞）]]", "[[SAP性能指标（CRC AUL GBP Vortex）]]", "[[LG Chem（LG 化学）]]", "[[诺尔（Nuoer）]]", "[[Satellite Chemical（卫星化学）]]", "[[巴斯夫欧洲公司（BASF SE）]]"]
---

# SAP Grade Selection - Three-PPT Comparison（SAP 选型三份 PPT 对比 · 中文版）

## 一句话定位 One-line Positioning

本批**纸尿裤吸收芯体 SAP 选型的三份 PPT 横向裁决报告**：把方法论规格书（PPT 1）、首过仿真（PPT 2）、集成可执行设计（PPT 3）三条轨道压成一条主推路线与一条退路。是本库回答「多 SAP 分层结构该怎么选牌号、为什么」的决策来源。

## 摘要 Summary

**执行摘要**：最终架构建议采用「**3 牌号分层结构**」——**皮侧独立薄层**用 **LG LK804ND**，**聚侧混合层**用 **Nuoer KC-511（快膨）× Nuoer NR-950（延迟膨润）**。该方案来自 **PPT 3（5-Zone Core SAP REL Simulation）**，是三份中最完整、可执行的一版，建议作为主推路线推进至 Stage 1 验证。核心机理是「**错峰膨润动力学**」在多重复冲击下击败凝胶堵塞（gel blocking）；性能收益方向为 **SAP 成本、累计返渗、末次下渗时间三降 + 设计容量一升**，且 SAP 用量更少。

**选定牌号与角色**：**SAP1 皮侧** —— LK804ND（LG Chem），CRC 31.5、AUL₀.₇ 18.0、GBP 53、Vortex 36 s，用量 4.0 g，定位"独立薄层；快下渗 + 低返渗 + 皮触安全"。**SAP2 快膨** —— KC-511（Nuoer），CRC 30.9、AUL₀.₇ 18.4、GBP 24、Vortex 29 s，用量 3.4 g，定位"处理 1–2 次冲击；CRC 刻意封顶"。**SAP3 延迟** —— NR-950（Nuoer），CRC 36.7、AUL₀.₇ 19.4、GBP 8、Vortex 51 s，用量 6.1 g，定位"高 CRC + 高 AUL 储库；慢 vortex = 天然延迟"。**SAP2:SAP3 混合比 = 36:64**（向延迟储库倾斜以匹配 4 次冲击曲线）；SAP1 为独立薄层，不参与混合。

**备援与双源**：SAP3 主用 NR-950、备份 BASF 9635（CRC 38），以双源认证对冲 Nuoer 交付（OTIF）风险；SAP1 备选 Satellite CR740（区域成本方案）。**关键结构增量**：在皮侧 SAP 与混合层之间夹一层 **REL 五纤 TAB 层（24 gsm）**，提供毛细梯度与单向 z 向流——这正是 PPT 2 用"混合层内高 GBP 牌号"来实现的导流/抗凝胶堵塞功能。

**五条选型主线**：① **皮侧 ≠ 储侧，分而治之**（皮侧只需快 + 干 + 安全，容量与成本压在聚侧，三份 PPT 共识）；② **错峰膨润打败凝胶堵塞（时间维度）**——核心不是空间分层而是**时间错位**，SAP2 先吃 1–2 次冲击、SAP3（51 s vortex）晚至 3–4 次才发力，两者永不同时封死凝胶床，**PPT 1 明确"快慢比（ratio）才是设计杠杆，而非位置"**；③ **单一自由膨润值会骗人**——两份策略文件均强调两个截然不同的配方单点 free-swell 可能相同，只有顺序 4 次冲击测试才能暴露错峰是否真生效，因此**bench 序列测试是硬门槛**；④ **成本杠杆 = 亚洲高 CRC / 高 AUL 牌号**——SAP2/SAP3 用国产诺尔压成本，SAP1 用全球供应 LG（因皮触安全限值——残留单体、萃取物——在直接接触层最严）；⑤ **分区匹配湿区**——5 区中 Z2（靶心湿区）最重、Z4（后储）次之，Z1/Z5 仅皮侧防漏；已优化男孩前偏湿型，女孩中心偏湿型需做 Z2/Z3 的 SKU 变体。

**三份 PPT 的共同观点**：核心理念（多 SAP / 混合结构以错峰或分区击败凝胶堵塞）、结构骨架（皮侧独立快吸层 + 聚侧储库层；6 月龄婴儿、385×110 mm 芯体、4 次冲击仿真）、方法论自觉（均承认单点 free-swell 不足、需多冲击验证，均标注"仿真/首过设计，需中试确认"）、安全系数思维（PPT 2 为 1.3×、PPT 3 为 1.6×）、风险意识（粒子偏析、延迟错配婴儿排尿节奏、延迟组分凝胶强度不足）。

**三份 PPT 的差异**：性质——PPT 1 为方法论/规格书（无具体牌号、无成本）、PPT 2 为首过仿真（标注"线性估算，需实验室确认"）、PPT 3 为集成可执行设计（"可冻结 Stage 1"）。聚侧混合哲学——PPT 1 为错峰（时间：快 + 延迟）、PPT 2 为"储 + 通"（N8 高 CRC 低 GBP + Satellite 710 高 GBP 低 AUL）、PPT 3 为错峰 + REL 层补通道。牌号组合——PPT 1 仅定义角色、PPT 2 为皮侧 N511 + 聚侧 N8/710（60/40）、PPT 3 为皮侧 LK804ND + 聚侧 KC-511/NR-950。冲击协议——PPT 2 用 40/50/60/70 mL = 220 mL（递增累计）、PPT 3 用 60×4 = 240 mL（0/0.5/3.5/6 h 真实间隔）。REL 层——仅 PPT 3 有（5 纤 TAB，24 gsm）。用量/容量——PPT 2 约 14.9 g / 286 mL / 1.3×；PPT 3 为 13.5 g / 387 mL / 1.6×（利用率 62%）。成本/风险/路线图——PPT 1 仅原则、PPT 2 仅建议下一步、PPT 3 有完整成本拆分 + 风险登记 + 4 阶段验证路线。结构关系上，PPT 3 在 GOVERNING METHODS 中明以 PPT 1 + REL 仿真方法论为基准；PPT 2 是一条更早/平行的仿真轨道（沙漏形、无 REL），本质是 PPT 3 的"前身上位版"——PPT 3 用 REL 层替代了 PPT 2 里高 GBP 牌号的导流功能并锁定牌号。

**顾问判断与关键风险**：① **两份仿真给出不同牌号答案，不能假装一致**——PPT 2 皮侧 N511 的 GBP 仅 26、PPT 3 的 LK804ND 为 53，按 PPT 1"皮侧低载下须保孔隙"标准，LK804ND 明显更优。② **PPT 3 最大隐患**：SAP3（NR-950）GBP 仅 8、Vortex 51 s，本身几乎不透气，导流完全寄托于 **REL 层活化（TAB Zone 2 须达 138–143 ℃，强冷 <40 ℃）**；一旦 REL 活化窗口漂移，PPT 2 靠 Satellite 710（GBP 75）在混合层直接补通道的方案反而更抗造，**建议保留为"无 REL 或 REL 不稳时的备选架构"**。③ **62% 利用率是保守余量不是缺陷**——低于单 SAP 基线（80%/84%），但以更少 SAP 实现更高容量，是为最差工况留头量；若量产发现湿区更集中，Z4 的 47% 利用率偏低可下调用量再降本。④ **一切建立在"KC-511 与 NR-950 真实存在可复现的膨润速率差"这一假设上**——PPT 3 风险登记已标 High（粒子偏析）与 Med（延迟错配婴儿 30 min–3 h 间隔），**Stage 1 的 bench 动力学验证（30 s→3 h）是冻结 spec 前的硬门槛，没过不能进中试**。

**结论**：主推 PPT 3 的 LK804ND / KC-511 / NR-950 三牌号方案（皮侧独立 + 聚侧 36:64 错峰混合 + REL 层），**须在 Stage 1 动力学 bench 验证通过后推进**，并将 PPT 2 的 N8+710 架构作为 REL 无法规模化稳定活化时的退路。

> 🔴 **manual_review（2026-09-29）**：本资料含**各牌号单价（$/MT）、单片 SAP 成本、成本敏感度（换供应商的成本增幅）与用量配比下的商务成本拆分**，属报价与商务条款类内容，依 AGENTS.md §5 **不页面化**，原文留存于 `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP选型分析_三PPT对比_中文版.docx.md`。本页与派生对比页仅保留**成本杠杆的方向性结论**（国产源为首要成本杠杆、皮侧必须用全球供应），**不落任何单价与单片成本数值**。具名供应商（LG Chem、Nuoer、BASF、Satellite）为公开供应商名称，仅记录角色不记商务条件。

## 提炼的数字与结论 Key Numbers and Conclusions

| 项目 Item | 数值 / 结论 Value / Conclusion | 备注 Note |
|---|---|---|
| 皮侧 SAP1 | LK804ND（LG Chem）：CRC 31.5、AUL₀.₇ 18.0、**GBP 53**、Vortex 36 s、4.0 g | 独立薄层；快下渗 + 低返渗 + 皮触安全 |
| 聚侧 SAP2（快膨） | KC-511（Nuoer）：CRC 30.9、AUL₀.₇ 18.4、GBP 24、Vortex 29 s、3.4 g | CRC 刻意封顶 |
| 聚侧 SAP3（延迟） | NR-950（Nuoer）：CRC 36.7、AUL₀.₇ 19.4、**GBP 8**、**Vortex 51 s**、6.1 g | 高 CRC + 高 AUL 储库；慢 vortex = 天然延迟 |
| 混合比 | **SAP2 : SAP3 = 36 : 64**（向延迟储库倾斜） | 匹配 4 次冲击曲线 |
| 结构增量 | 皮侧与混合层之间夹 **REL 五纤 TAB 层 24 gsm** | 提供毛细梯度与单向 z 向流 |
| 皮侧 GBP 对比 | PPT 2 的 N511 **26** vs PPT 3 的 LK804ND **53** | 按"皮侧低载须保孔隙"标准，LK804ND 更优 |
| REL 活化窗口 | **TAB Zone 2 须达 138–143 ℃，强冷 <40 ℃** | 活化窗口漂移是 PPT 3 最大隐患 |
| 混合层补通道备选 | PPT 2 用 Satellite 710（**GBP 75**）直接在混合层补通道 | REL 不稳时的退路 |
| PPT 2 用量/容量 | 约 **14.9 g / 286 mL / 1.3×** 安全系数 | 沙漏形、无 REL |
| PPT 3 用量/容量 | **13.5 g / 387 mL / 1.6×**（利用率 **62%**） | 集成可执行设计 |
| 冲击协议差异 | PPT 2：40/50/60/70 mL = 220 mL（递增累计）；PPT 3：60×4 = 240 mL（0/0.5/3.5/6 h 真实间隔） | 口径不同，容量不可直接比 |
| 分区湿区 | Z2（靶心湿区）最重、Z4（后储）次之；Z1/Z5 仅皮侧防漏 | 女孩中心偏湿型需 Z2/Z3 SKU 变体 |
| 安全系数思维 | PPT 2 1.3×；PPT 3 1.6×（62% 利用率为最差工况留头量） | 单 SAP 基线利用率 80%/84% |
| 硬门槛 | Stage 1 **bench 动力学验证（30 s→3 h）** | 未过不得进中试 |
| 风险等级 | High：粒子偏析；Med：延迟错配婴儿 30 min–3 h 间隔 | PPT 3 风险登记 |
| 双源安排 | SAP3 主用 NR-950、备份 BASF 9635（CRC 38）；SAP1 备选 Satellite CR740 | 对冲 OTIF 风险（**商务条件未页面化**） |

## 关键论断（key_claims）

- **错峰膨润是时间维度的设计杠杆（快慢比），不是空间分层的位置问题** —— 支撑页：[[SAP错峰膨胀]]、[[Multilayer SAP Core（多层SAP芯体）]]
- **单点 free-swell 会骗人，顺序多冲击 bench 测试是冻结 spec 的硬门槛** —— 支撑页：[[SAP性能指标（CRC AUL GBP Vortex）]]
- **皮侧与储侧的评判标准不同：皮侧保孔隙（高 GBP）优先，储侧保容量（高 CRC/AUL）优先** —— 支撑页：[[Gel Blocking（凝胶阻塞）]]、[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]
- **REL 层把"导流"从牌号属性转移为结构属性，也把风险转移到工艺活化窗口** —— 支撑页：[[REL增强层]]、[[SAP Architecture Options - Three PPT Routes（三份 PPT SAP 架构路线对比）]]

## 关联页面

- 概念：[[SAP错峰膨胀]]、[[Multilayer SAP Core（多层SAP芯体）]]、[[Gel Blocking（凝胶阻塞）]]、[[SAP性能指标（CRC AUL GBP Vortex）]]、[[REL增强层]]、[[分区密度设计]]、[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]
- 实体：[[LG Chem（LG 化学）]]、[[诺尔（Nuoer）]]、[[巴斯夫欧洲公司（BASF SE）]]、[[Satellite Chemical（卫星化学）]]
- 对比：[[SAP Architecture Options - Three PPT Routes（三份 PPT SAP 架构路线对比）]]、[[SAP 四牌号性能对比（KC511 vs NR-610S vs NR-950 vs Code X）]]、[[单牌号全511 vs 分层多SAP混底（性能·成本·供应链）]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP选型分析_三PPT对比_中文版.docx.md`
- 原文链接：（无；内部分析报告）
- 同族文档：`.../SAP选型分析_三PPT对比_EN.docx.md`（已编译）、[[Three-Way SAP Design Comparison（三方案 SAP 设计仿真对比）]]

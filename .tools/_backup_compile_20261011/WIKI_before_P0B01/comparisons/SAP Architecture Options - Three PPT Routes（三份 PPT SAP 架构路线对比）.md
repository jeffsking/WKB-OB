---
type: comparison
title: "SAP Architecture Options - Three PPT Routes（三份 PPT SAP 架构路线对比）"
subjects: ["[[SAP错峰膨胀]]", "[[Multilayer SAP Core（多层SAP芯体）]]", "[[REL增强层]]"]
dimension: 综合
updated: 2026-09-29
tags: [SAP, 选型, 错峰膨润, REL, 仿真, 供应链风险]
---

# SAP Architecture Options - Three PPT Routes（三份 PPT SAP 架构路线对比）

## 对比维度表 Comparison Matrix

> 必含「成本 Cost」与「供应链风险 Supply Chain Risk」两列。

| 维度 Dimension | PPT 1 — 选型策略（方法论/规格书） | PPT 2 — 芯体仿真①（首过仿真） | PPT 3 — 五区 + REL 仿真（集成可执行） | 依据 Source |
|---|---|---|---|---|
| 性质 | 方法论 / 规格书（**无具体牌号、无成本**） | 首过仿真（标注"线性估算，需实验室确认"） | 集成可执行设计（"可冻结 Stage 1"） | [[SAP Grade Selection - Three-PPT Comparison（SAP 选型三份 PPT 对比 · 中文版）]] |
| 聚侧混合哲学 | **错峰膨润（时间维度）**：快 + 延迟 | **储 + 通**：N8（高 CRC 低 GBP）+ Satellite 710（高 GBP 低 AUL） | **错峰膨润 + REL 层补通道** | 同上 |
| 牌号组合 | 仅定义 SAP1/SAP2/SAP3 **角色** | 皮侧 N511；聚侧 N8 + Satellite 710（60/40） | 皮侧 **LK804ND**；聚侧 **KC-511 + NR-950（36:64）** | 同上 |
| 皮侧 GBP | 只给标准（低载下须保孔隙） | **26**（N511） | **53**（LK804ND） | 同上 |
| REL 层 | 未涉及 | **无** | **有（5 纤 TAB，24 gsm）** | 同上 |
| 冲击协议 | 概念（多次冲击） | 40/50/60/70 mL = 220 mL（递增累计） | **60×4 = 240 mL（0/0.5/3.5/6 h 真实间隔）** | 同上 |
| 用量 / 容量 / 安全系数 | — | 约 14.9 g / 286 mL / **1.3×** | **13.5 g / 387 mL / 1.6×**（利用率 62%） | 同上 |
| 导流实现方式 | 未指定 | **牌号属性**（混合层内高 GBP 牌号补通道，Satellite 710 GBP 75） | **结构属性**（REL 层提供毛细梯度与单向 z 向流） | 同上 |
| **成本 Cost** | 仅原则，无数字 | 仅建议下一步，无成本拆分 | **完整成本拆分**；成本杠杆方向明确——**SAP2/SAP3 用国产高 CRC/高 AUL 牌号压成本，SAP1 用全球供应（皮触安全限值最严）** | 同上（🔴 **具体单价与单片成本属商务敏感，见源摘要页 manual_review，本表不落数**） |
| **供应链风险 Supply Chain Risk** | 未涉及 | 依赖 Satellite 高 GBP 牌号（单一功能牌号） | **双源设计**：SAP3 主用 NR-950、备份另一牌号对冲交付（OTIF）风险；SAP1 另有区域成本备选 | 同上（"备援/双源"节） |
| **最大风险** | 无牌号落地风险（本就是方法论层） | 皮侧 GBP 26 偏低，按 PPT 1 标准不够优 | **SAP3（NR-950）GBP 仅 8、Vortex 51 s，本身几乎不透气**，导流完全寄托于 **REL 活化（TAB Zone 2 138–143 ℃、强冷 <40 ℃）**；窗口漂移即失效 | 同上（6.1–6.2） |
| 成熟度 / 定位 | 共识底座（被 PPT 3 在 GOVERNING METHODS 中引为基准） | **PPT 3 的"前身上位版"**：更早/平行轨道（沙漏形、无 REL） | **主推路线**；PPT 2 作为"无 REL 或 REL 不稳时"的退路 | 同上（5–7 节） |

> 尾注 Footnote：本表所有数值与判读均来自 [[SAP Grade Selection - Three-PPT Comparison（SAP 选型三份 PPT 对比 · 中文版）]]；**成本**列仅保留方向性结论，**不含单价、单片成本与成本敏感度数值**（商务敏感，见源摘要页 🔴 manual_review）。三份 PPT 的**冲击协议与容量口径不同**（220 mL 递增累计 vs 240 mL 真实间隔），容量数字**不可直接横比**。

## 各自适用场景 Where Each Route Fits

- **PPT 1（方法论）**：作为**评判标准**使用——其"皮侧低载下须保孔隙""快慢比才是设计杠杆"两条准则是裁决 PPT 2 与 PPT 3 分歧的依据。
- **PPT 2（N8 + Satellite 710）**：**备选架构**。当 REL 层无法规模化稳定活化（活化窗口 138–143 ℃、强冷 <40 ℃ 漂移）时，其"用高 GBP 牌号直接在混合层补通道"的方案更抗造；缺点是皮侧 GBP 仅 26。
- **PPT 3（LK804ND + KC-511/NR-950 + REL）**：**主推路线**。皮侧 GBP 53 明显更优、完整成本与风险登记齐备；但**必须在 Stage 1 bench 动力学验证（30 s→3 h）通过后**才能推进中试。

## 结论 Conclusion

三条轨道的关系是"**方法论 → 平行仿真 → 集成设计**"而非并列竞争：裁决分歧的标准来自 PPT 1，皮侧牌号由 GBP（26 vs 53）决出胜负，真正的选择落在**"导流靠牌号属性（PPT 2）还是靠结构属性（PPT 3 的 REL 层）"**——选择 PPT 3 即接受"性能更高但风险转移到工艺活化窗口"，因此必须保留 PPT 2 作为退路。

## 来源 Sources

- [[SAP Grade Selection - Three-PPT Comparison（SAP 选型三份 PPT 对比 · 中文版）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP选型分析_三PPT对比_中文版.docx.md`

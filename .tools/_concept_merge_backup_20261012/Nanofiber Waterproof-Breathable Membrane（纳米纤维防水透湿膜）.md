---
type: concept
title: "Nanofiber Waterproof-Breathable Membrane（纳米纤维防水透湿膜）"
domain: [卫材研发, 材料]
status: growing
updated: 2026-09-30
tags: [纳米纤维, 静电纺丝, electrospinning, PU, 防水透湿, 底膜, 热熔胶复合, 克重]
aliases: ["Nanofibre WBM", "静电纺丝防水透湿膜"]
---

# Nanofiber Waterproof-Breathable Membrane（纳米纤维防水透湿膜）

> **Definition 定义**：以**高压静电纺丝（electrospinning）** 把 PU（聚氨酯）溶液喷到金属收集器上、在电场中被拉伸成纳米级纤维并随机沉积成膜的**防水透湿膜**。它的孔径介于"液态水滴"与"水蒸气分子"之间，因此同时做到**阻液**与**透汽**——与 PE 拉伸微孔膜（先成膜、再双向拉伸）属**不同材料族**。

## Mechanism 机理

1. **尺寸筛选原理（原文口径）**：孔径远小于液态水滴（约 **100 µm**）→ 阻挡雨水 / 液体渗透（waterproof）；孔径远大于水蒸气分子（约 **0.0004 µm**）→ 汗气快速逸出（breathable）。
2. **工艺五步（原文）**：① 聚合物溶液装入注射器 → ② 针头与收集器间加高压电场 → ③ 电场力克服表面张力形成射流 → ④ 射流拉伸、鞭动、溶剂挥发固化 → ⑤ 固化纳米纤维随机沉积成膜。
3. **超薄是结构效应**：纤维直径在纳米级 → 达到同等阻隔所需克重极低（**4 gsm 级**），这与 PE 膜"越薄越易破"的权衡逻辑不同。
4. **必须复合才有结构**：膜本身极薄（3–4 g），无法独立承受转化线张力，因此以**热熔胶与无纺布复合**成 15–20 g 的复合体使用。

## Key parameter table 关键参数表

| Parameter 参数 | Value 值 | Note 备注 | Source 出处 |
|---|---|---|---|
| Material 材料 | **PU**（聚氨酯） | 对照 PE 膜 | [[August R&D Meeting 2026（华峰研发会议）]] |
| Process 工艺 | High-voltage electrospinning | 对照 dry/wet + 双向拉伸 | 同上 |
| Max hydrostatic pressure 最大静水压 | **8,000 mmH₂O** | 对照 PE 膜 625–1,620（Brand A/B/C） | 同上 |
| Air permeability 透气性 | **3 CFM** | 对照 PE 膜 0.0556–0.10297 CFM | 同上 |
| Basis weight 克重 | **4 GSM** | 对照 PE 膜 >25 GSM | 同上 |
| Thickness 厚度 | **8 µm** | 对照 PE 膜 >20 µm | 同上 |
| WVTR | **>100,000 g/m²/24h** | 对照 PE 膜 8,000–10,000 | 同上 |
| Membrane weight (meeting口径) | 最低可做 **3 g**，样品约 **4 g** | 与上表 4 GSM 同源 | [[与华峰集团会晤纪要（2026-07-29）]] |
| Air permeability (meeting口径) | 实测 **约 50 万以上**（日本 **B-1 法**标准 >10 万；**A-1 法** >1.2 万） | **单位未标注，与 CFM 口径不可直接比较** `[待验证]` | 同上 |
| Water resistance 防水性 | **>1/2**（相对 PE 膜，原文口径） | 口径模糊 `[待验证]` | 同上 |
| Composite weight 复合无纺布克重 | **15–20 g**，本次约 **18 g** | — | 同上 |
| Lamination 复合方式 | **热熔胶（hot melt adhesive）** | — | 同上 |
| Open issue 未解问题 | **纳米膜起皱**（持续跟进解决方案） | — | 同上 |

> ⚠️ **Two sources, two measurement systems 两来源两套口径**：`静水压/CFM/GSM/µm/WVTR` 五元组来自研发材料；`50 万以上 / B-1 法 / A-1 法` 来自会晤纪要。**两套数字无法直接换算**，引用时必须注明来源，禁止混算 `[待验证]`。
> ⚠️ 本页所有数字均为**供应商自测或供方口径**，库内**无第三方检测报告**。

## Adjacent concepts 相邻概念

- 使能工艺：[[Meltblown Nonwoven（熔喷非织造布）]]（另一条超细纤维成网路线）
- 膜材对照：[[Film-Free Backsheet（无膜背层）]]
- 对比：[[SMMMS Film-Free vs Microporous Film Backsheet（无膜背层 vs 微孔膜背层）]]
- 测试口径：[[WVTR 测试口径（失重法 vs 增重法）]]
- 复合工艺：[[热风粘合无纺布]]、[[Hot-Melt Slot Coating（热熔狭缝涂布）]]
- 供应方：[[华峰集团（Huafon Group）]]

## Lessons learned 经验教训

> ✅ 验证（2026-09-29，来源 [[与华峰集团会晤纪要（2026-07-29）]]、[[August R&D Meeting 2026（华峰研发会议）]]）：两份同批来源对同一技术给出**互相印证的方向**（超薄 + 高透湿 + 防水），但**测量口径不一致**。本页据此把两套数字**并列而非合并**——这是本库处理"同物不同测法"的标准做法（参见 [[WVTR 测试口径（失重法 vs 增重法）]]）。

- **要点**：纳米纤维膜的竞争力不来自"膜更薄"，而来自**"薄到可以当功能层而不是结构层"**——它必须与无纺布体系绑定评估，单看膜指标会高估其可落地性。
- **待补 `[待验证]`**：复合体的**水洗/摩擦后阻隔衰减**、**起皱问题的解决路径**、以及产线速度可行性。

## Sources 来源

- [[August R&D Meeting 2026（华峰研发会议）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/August R&D Meeting.pdf.md`
- [[与华峰集团会晤纪要（2026-07-29）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/与华峰集团会晤纪要_20260729.docx.md`

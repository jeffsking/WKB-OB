---
type: comparison
title: "REL vs ADL（收集传递层 vs 导流层）"
subjects: ["[[REL增强层]]", "[[ADL（导流层）]]"]
dimension: 综合
updated: 2026-09-29
tags: [REL, ADL, 导流层, 芯体结构, 渗透, 回渗, 供应链]
---

# REL vs ADL（收集传递层 vs 导流层）

## 对比维度表 Comparison matrix

> 必含「成本 Cost」与「供应链风险 Supply chain risk」两列 (Required columns per AGENTS.md §2.4)。

| Dimension 维度 | REL（Reception & Transfer Layer，收集/传递层） | ADL（Acquisition & Distribution Layer，导流层） | Source 依据 |
|---|---|---|---|
| 功能侧重 Function | **垂直方向的「收」**：瞬间承接涌流（gush）、暂存、向下传递 | **水平方向的「导」**：沿 MD 纵向扩散、均匀分配至 SAP | [[Diaper Structure & ADL-REL Compendium（纸尿裤结构·ADL与REL辨析）]] |
| 密度与孔径 Density / pore | **低密度、大孔径**，需极大空隙体积容纳瞬时涌流 | **中等密度、定向孔径**（贯通孔/漏斗孔），控制流向与扩散速度 | 同上 |
| 典型材料 Material | 粗梳合成纤维网；含中空/卷曲纤维的**空气铺网**（SBR 胶乳 → VAE 可交联分散体） | **高蓬松热风粘合（ATB）非织造布**；三维膜/打孔非织造布 | 同上；[[ADL（导流层）]] |
| 粘合剂逻辑 Binder logic | 侧重**湿态结构锚固**（SBR/VAE），防受力塌缩 | 侧重**低粘着**，保证多孔表面与低回渗；过粘合会提高滞留液量 | 同上；[[ADL（导流层）]] |
| 工艺实现 Process | 梳理 + 穿透热风粘合（TAB）；本库为 **24 gsm 五纤维配方**（Zone1 128–132 ℃ / Zone2 138–143 ℃） | 主流为穿透热风粘合，焙烘窗口按皮层聚合物切换（PE/PET 约 130 ℃；CoPET/PET 110–180 ℃ 可调） | [[REL增强层]]；[[CoPET ADL 转型蓝图（皮层聚合物替代评估）]] |
| 性能表现 Performance | 首次穿透 **0.65 s**；第 3 次分布 **54 cm²**；第 3 次回渗 **0.10 g**；湿态 MD **78 N/m**；SAP 隔离 **98%**（模拟口径） | CoPET vs PE/PET：第 3 次摄入 **−16%**、MD 铺展 **+17%**、第 3 次回渗 **−24%**（模拟口径） | [[REL增强层]]；[[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]] |
| 失效风险 Failure mode | **受压塌缩或吸水软化** → 失去瞬间接收能力 → 溢漏 | **导流不足或凝胶堵塞** → 局部过载 → 回渗、侧漏 | [[Diaper Structure & ADL-REL Compendium（纸尿裤结构·ADL与REL辨析）]] |
| **成本 Cost** | **更高**：本库 REL 成本阶梯为**方案 A +RMB 500/t、方案 B +RMB 1,400/t**（vs Variant C）；另外 ADL 被移除的结构（全芯体 v2.0 Route A）需以 REL 承担其功能 | **更低 baseline**：常规 ES PE/PET-ATB 为成本基线；换 CoPET/PET 属近似平价的内部替代（CoPET/PET 总制造成本约 9,528 元/吨 vs PE/PET 约 9,772 元/吨，**CoPET 反而低约 2.5%**） | [[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]]；[[CoPET 采购蓝图：成本拆解与供应分层]] |
| **供应链风险 Supply chain risk** | **高（单点）**：REL 在本库已变为**单选项直采**（闽瑞 28 gsm、6 卷 145 mm×300 m），**不进入选择矩阵**；且关键纤维 PTT、PVA（Kuraray KURALON™ K-II）、三叶 PET 为专用规格 | **中（可分层）**：ES 双组分纤维可选 PE/PET 或 CoPET/PET，且已建立 A/B/C 层供应分层地图；但 CoPET 存在 IPA 价格波动（30 天内 4,800 → 9,700 元/吨）与无锑切片产能受限（仅天津石化、恒逸等少数位点） | [[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]]；[[CoPET 采购蓝图：成本拆解与供应分层]] |
| 适用场景 Application fit | 超薄芯体、需同时承担**快速输运 + 结构支撑**的场景；以及「移除 ADL」的全芯体路线（Route A） | 混合/复合芯体中承担摄入-铺展-下送三段职责；以及在触感优先时贴近面层保留 PE/PET | [[ADL（导流层）]]；[[REL增强层]] |

> 尾注 Endnote：本表「成本」「供应链风险」两项的数据来自 [[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]]（REL 成本阶梯与单选项直采）与 [[CoPET 采购蓝图：成本拆解与供应分层]]（CoPET vs PE/PET 制造成本、IPA 波动、无锑切片位点）；结构与失效项来自 [[Diaper Structure & ADL-REL Compendium（纸尿裤结构·ADL与REL辨析）]]。**标注为模拟口径的性能值不得作为量产承诺**（源均为归档/规划性质的工作文档）。

## 各自适用场景 Where each wins

- **[[REL增强层]]**：当设计目标是**更薄 + 更快 + 更强的组合**（超薄芯体、结构上不能依赖木浆），或明确走「**移除 ADL 与亲水剂**」的全芯体 v2.0 Route A 时，REL 是唯一承重层——代价是更高的材料成本与单点供应链。
- **[[ADL（导流层）]]**：当产品仍为混合/复合芯体、需要在面层与芯体之间做**摄入-铺展-下送**的解耦时，ADL 更经济且供应面更宽；通过皮层聚合物切换（PE/PET → CoPET/PET）还能在近似成本下拿到 −16% 摄入 / +17% 铺展 / −24% 回渗的模拟收益。

## 结论 Conclusion

一句话结论 One-sentence conclusion：**REL 与 ADL 不是替代关系而是分工关系——REL 管"接得住"（容得下、不塌陷），ADL 管"散得开"（导得快、分得匀）；合并成一层的前提是做出密度梯度，而合并的代价是成本上升（+RMB 500–1,400/t）与供应链单点化（REL 单选项直采）。**

## Sources 来源

- [[Diaper Structure & ADL-REL Compendium（纸尿裤结构·ADL与REL辨析）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Structure/纸尿裤结构.md`
- [[REL增强层]] —— 既有概念页（五纤维配方、工艺窗口、成本阶梯）
- [[ADL（导流层）]] —— 既有概念页（ATB 结构、CoPET 模拟）
- [[CoPET 采购蓝图：成本拆解与供应分层]] —— 既有源摘要页（成本与供应链分层）
- [[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]] —— 既有源摘要页（REL 成本阶梯与采购形态）

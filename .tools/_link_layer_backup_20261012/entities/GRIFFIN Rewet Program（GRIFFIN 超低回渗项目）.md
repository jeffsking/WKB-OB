---
type: entity
title: "GRIFFIN Rewet Program（GRIFFIN 超低回渗项目）"
category: 项目
relationship: 内部研发项目
updated: 2026-09-29
tags: [回渗, rewet, Depend, 成人失禁, ADT, 项目代号]
---

# GRIFFIN Rewet Program（GRIFFIN 超低回渗项目）

## 基本盘 Basics

| 项目 Item | 内容 Content |
|---|---|
| 主营 / 定位 | Depend（成人失禁）品类**超低回渗**攻坚项目，ADT 主导，问题陈述作者 Kerry Clemmer（ADT） |
| 目标产品 | Depend Fresh Protection（对标 P&G Always Discreet） |
| 关键指标 | closed cradle 回渗 ≤0.15 g（立项目标） |
| 生产 / 测试 | 芯体由 ADL 生产、成品由 GML 生产、在 GADT 实验室测试 |
| 角色 | 本库回渗机理与项目史的主线证据链 |

## 项目沿革 Timeline

- **ATACAMA+ 之前**：Depend 回渗约 1.6 g；Always Discreet 为 0.20 g 且对我们持有 BV（better-than 宣称）。
- **ATACAMA+**：把回渗改善到与 Always Discreet 持平；根因调查确认绝大部分回渗来自**导流层（surge）与摄入层界面**；关键工艺抓手为面层-导流层压花（liner-surge embossing, LSE）。
- **SIROCCO（前序项目）**：Always Discreet 降至 0.16–0.18 g，Depend 停留在 0.25 g，不再持平。沿用 ATACAMA+ 经验先攻 surge，结果 CT8 surge（Shalag 3）虽改善回渗但**摄入变差**；进一步改芯体已来不及验证，项目在可用时间窗内未成功。
- **Post-SIROCCO**：CRO 继续追查，发现液体积聚点已从 surge 转移到 **liner（面层）**。
- **GRIFFIN 立项（2025-01，更新 2025-02-12）**：目标 ≤0.15 g；两条工作流并行——Workstream 1 面层（4 条假设，2025-02 GML 试验，3 月中出结果）、Workstream 2 ActivTech 芯体（2 月 GML 生产带 LSE 样品重评差距，并做动态渗透率、STEWIE 微气候与液体分布测试）。

## 关键代码与配置 Codes Tested

| 代码 Code | 包裹 Wrapsheet | 面层 Liner | 导流层 Surge | 面层-导流层压花 LSE |
|---|---|---|---|---|
| SAM/Fluff | 17 gsm tissue | 12 gsm SB，未印花 | Shalag SS7CT5H80 | 有 |
| ActivTech Hybrid | 12 gsm dSB | 12 gsm SB，印花 | （本页来源未列） | **无** |

> 注：ActivTech hybrid 从未被用于如此严苛的超低回渗场景，早期数据偏高但该代码缺 LSE，**不构成同条件对比**。

## 面层假设矩阵 Liner Hypothesis Matrix（2025-02 GML 试验）

| 材料 Material | 粘合花型 Bond | 亲水剂 Lertisan | 假设 Hypothesis |
|---|---|---|---|
| Fitesa 12 gsm SB | Oval bond 18% | 0.65% | 对照组 Control |
| Fitesa 12 gsm SB | CD Rod bond 10% | 0.65% | 更开放的花型 = 更少滞留残液的小口袋 |
| Fitesa 12 gsm SB | CD Rod bond 10% | 0.3% | 降低处理量以排斥残余液（冒摄入/渗漏风险） |
| Fitesa 12 gsm SB | CD Rod bond 10% | 0% | 无亲水处理以排斥残余液（摄入/渗漏风险更高） |
| Fitesa 22 gsm TS3 开孔膜面层 | — | — | 非纤维 + 开孔 = 更少滞留小口袋 |

## Evidence Update 证据追加（2026-09-29 · 学习周期复盘与重整）

> ✅ 追加（2026-09-29，source [[GRIFFIN Learning Cycle Check In（GRIFFIN 学习周期复盘 · 2025-06-25）]]）：
> - **Liner**：GRIFFIN HUT 已投放**未处理面层**（渗漏结果 7 月底）；"用 SF19 改盐水表面张力研究摄入/回渗权衡"的实验**未能完成**；AD 面层看起来**胶更多**；**Summit 喷头可能带来增量改善**；**更多批次下 AD 持续更不亲水**；**AD 同一时段不同机台有 2 种胶型**；**摄入系统互换假设：AD 优势来自面层/导流层，而非卷曲纤维**。
> - **Core**：**ATH（无 SAM）芯体回渗高于 SAM/fluff**，已在 GML 成功生产；测试手段含 **MicroCT、毛细压力**（先整体后拆分）；**绒毛浆层加 SAM 以脱水**的假设待验；**1 gsm dSB vs 20 gsm BCW 包裹层**（若增加摄入时间则搭配更低克重导流层）；卷曲纤维材料 **50/50 Helix 混纺**与 **90 gsm 卷曲纤维/PET 复合纤网**，目标 7 月 GML 试验（7/14–8/1）。
> - **Adhesives**：SIROCCO 三处施胶试验中**唯一统计显著改善 = 降低 LTD add-on**；**亲水胶在三处均增加回渗**；去掉 PAA 中央 50 mm 条带方向性改善；**Signature 喷头优于 Summit**。
>
> ✅ 追加（2026-09-29，source [[GRIFFIN Regroup - Depend Rewet Update（GRIFFIN 重整更新 · 2025-08-28）]]）：摄入系统互换实验**已取得结果**——把 AD 面层/导流层装入 DPU2 **显著降低回渗**，**卷曲纤维无增量贡献**（验证了 6/25 的假设）。同时首次提出**回渗变异性**问题：批次间 0.39 vs 0.35 g、测试请求间 0.44 vs 0.36 g，且与干厚度（7.04/5.96、7.45/6.08）同向。
>
> ✅ 追加（2026-09-29，source [[GRIFFIN Female DPU2 AT Hybrid Rewet Summary（女性 DPU2 AT Hybrid 回渗总结）]]）：项目扩展至**女性 DPU2 平台**，形成一轮多代码回渗排序（550 g 加载，Closed Cradle）：AT Fluffless VONN（带 surge）**0.39750 g** > AT Fluffless dSB **0.32250 g** ≈ AT Hybrid dSB **0.30750 g** > AT Fluffless TABCW **0.28750 g** > AT Hybrid dSB（450 g）**0.28000 g** > **SAM/Fluff Control 0.23000 g**（Std Error 0.02407）。**AT 系普遍高于 SAM/Fluff 对照**，与 6/25 复盘"ATH（无 SAM）芯体回渗高于 SAM/fluff"一致——**两条独立来源互证**。
> - **AT Hybrid dSB 550 g 平均比对照高 0.07 g，但 95% CI 下不显著**（GADT 口径）。
> - **AT Fluffless VONN（不带 surge）回渗 0.17 g（本组最低）却因摄入时间过高被排除**——再次印证"回渗与摄入必须同轮判读"。
> - **材料配置缺口被补齐**：AT Hybrid 侧导流层同为 **Shalag White SS7CT5H80**；AT 系包裹层为 c-wrap（dSB **12 gsm CM7** / TABCW **20 gsm Shalag** / VONN **35 gsm MOJAVE 2.35v2**），面层为 **Honeycomb 印刷 Fitesa 12 gsm SB**；**AT 代码仍无 LSE**（与上方代码表一致）。
> - **新增风险：测试路径可翻转结论**——AT Hybrid dSB 550 g 走 **LabVantage 研究放行 0.40875 g** vs 走 **GADT 0.30750 g**（Std Error 0.02249），95% CI 下显著；且 **Study Release 口径下代码间显著、GADT 口径下不显著**；对竞品 **Assurance** 的结论也随路径改变（研究放行下 AT Hybrid 差于 Assurance，GADT 下不显著）。见 [[Rewet Measurement Variability（回渗测试变异性）]]。
> - **后续**：**SAM/Fluff Control** 与 **AT Hybrid dSB 550 g** 两个代码已进入**女性 HUT**，结果预计 **mid-Feb**；源文要求把**无 surge VONN 与 Always Discreet** 一并加入本组作参照。
>
> ⚠️ **口径提示（2026-09-29）**：本节两轮数据表 Std Error 不同（0.02407 / 0.02249），**非同一次方差分析**，跨表不可换算；来源未标注样本量与 Closed Cradle 具体参数。

## Evidence Update 证据追加（2026-09-29 · AC Brand Connect）

> ✅ Verification（2026-09-29，source 来源 [[2025.09.02 - AC Brand Connect.pptx]]）：**untreated liner 方向的首轮量化结果落地**——HUT rewet code（Fitesa 12gsm SB, CD rod, **0% Lertisan**）closed cradle 回渗 **0.19–0.20 g**，与 0.3% 组（0.19 g）同档，优于 control（oval, 0.65% Lertisan zoned）组；**leakage 影响筛查在女性 HUT 进行中**，HUT 目前在 Fitesa 面层上运行，后续试产工作将并入 Fibertex 学习。同期 intake system swap 实验确认 **AD liner/surge 装上 Depend core 即降回渗、curly fiber 单独无效**——支持 liner 作为最大降回渗杠杆的既有判断。HSBL trial（9/29 当周）针对 liner-surge interface，对应本库 [[Full Results.xlsx]] 矩阵。

## 追加：假设地图历史线索（2026-09-29 追加 · 来源：Hypothesis Map.xlsx）

> ✅ Verification（2026-09-29，source 来源 [[Hypothesis Map.xlsx]]）：GRIFFIN 假设地图（六档影响分类 × Depend-Historical/Proposed/Baby-Child Care 三板块）披露两条与上方内容相关的历史线索：① **39840 实验——untreated liner 曾伴更高 leakage**（No Change 档），为上方 2025-09 untreated liner 回渗优势（0.19-0.20 g）补充了 leakage 风险前史，与"HUT leakage 筛查"互为因果线索；② **Shalag 3 是否促进单向流**列入 Not Tested——单向流是 Flowback 支柱的明确杠杆但历史材料未验证。另：Pre-ATACAMA surges（Ct8/CT9/双层）评为 Lower-to-No-Change；BONNIE 项目（Liz Bradley）为 Higher-Rewet 线索待挖。Proposed 板块与 Baby-Child Care 板块在提取件中为空框架 `[待验证]`。

## 相关概念 Related Concepts

- [[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]
- [[Rewet Test（回渗测试）]]、[[Intake System（摄入系统）]]
- [[Liner-Surge Embossing（面层-导流层压花）]]、[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]
- [[IPC BCC OI Portfolio（开放创新项目组合）]]

## 来源 Sources

- [[GRIFFIN Rewet Technical Problem Statement（GRIFFIN 回渗技术问题描述 · 2025-01-31）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.01.31 - GRIFFIN Rewet.pptx.md`

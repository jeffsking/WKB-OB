---
type: source
title: "GRIFFIN Rewet Technical Problem Statement（GRIFFIN 回渗技术问题描述 · 2025-01-31）"
source_type: 提案
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.01.31 - GRIFFIN Rewet.pptx.md
original_link: ""
date_published: 2025-01-31
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Depend current DPU rewet is 0.25 g versus P&G Always Discreet 0.18 g; the program target is ≤0.15 g on Depend Fresh Protection measured by closed cradle（中文：当前 DPU 回渗 0.25 g，对标 Always Discreet 0.18 g，目标 ≤0.15 g，闭式摇篮法测）"
  - "Rewet has two mechanisms: desorption (fluid trapped in the intake system) and flowback (fluid escaping back from the wetted core)（中文：回渗双机理——摄入系统滞留液解吸，与湿芯体回流）"
  - "ATACAMA+ cut Depend rewet from ~1.6 g to parity with Always Discreet by fixing surge and liner-surge interfaces; post-SIROCCO work identified liner as the new fluid congregation point（中文：ATACAMA+ 把回渗从约 1.6 g 降到对标持平，SIROCCO 之后发现液体积聚点转移到面层）"
  - "SIROCCO failed on timeline because the surge solution traded off against intake; CT8 surge (Shalag 3) improved rewet but worsened intake（中文：SIROCCO 因导流层方案与摄入性能互斥而未能按期达成）"
  - "ActivTech hybrid is an un-optimized opportunity area; early AT hybrid data shows higher rewet but that code lacked liner-surge embossing（中文：ActivTech 混合芯体尚未针对超低回渗优化，早期偏高但缺面层-导流层压花）"
pages_linked: ["[[GRIFFIN Rewet Program（GRIFFIN 超低回渗项目）]]", "[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]", "[[Liner-Surge Embossing（面层-导流层压花）]]", "[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]", "[[Shalag（Shalag 导流层与面层材料）]]", "[[Fitesa（Fitesa 非织造布）]]", "[[IPC BCC OI Portfolio（开放创新项目组合）]]"]
---

# GRIFFIN Rewet Technical Problem Statement（GRIFFIN 回渗技术问题描述 · 2025-01-31）

## 一句话定位 One-line Positioning

本批**成人失禁品类超低回渗项目的立项问题陈述（英文原件，Kerry Clemmer / ADT）**：把 Depend 与 Always Discreet 的回渗差距量化为明确目标（≤0.15 g），并给出「逐层清除每一滴水」的系统性技术路径。是本库回答「回渗为什么降不下来、先动哪一层」的机理与项目史来源。

## 摘要 Summary

问题陈述开门见山：此前 Depend 项目已改善回渗但**未达优越**——当前 DPU 回渗 0.25 g，P&G Always Discreet 为 0.18 g。目标是在 Depend Fresh Protection 上以闭式摇篮法（closed cradle）测得 **≤0.15 g**。方法不是单点优化，而是「系统性地识别并消除每一层中的每一滴水」。

项目史三段：**ATACAMA+ 之前** Depend 回渗约 1.6 g，Always Discreet 0.20 g 且对我们有 BV（better-than 宣称）；ATACAMA+ 把回渗改善到与 Always Discreet 持平，根因调查发现绝大部分回渗来自**导流层（surge）与摄入层界面**。**SIROCCO** 阶段 Always Discreet 又把回渗降到 0.16–0.18 g，Depend 停在 0.25 g 不再持平；SIROCCO 沿用 ATACAMA+ 的成功经验先攻导流层，结果**导流层方案与摄入性能互斥**（CT8 surge / Shalag 3 回渗改善但摄入变差），进一步改芯体已来不及测试，项目在可用时间窗内未成功。**Post-SIROCCO** 由 CRO 继续追查，发现液体积聚的位置已从导流层转移到**面层（liner）**。

机理框架给出两条回渗通路：**Desorption 解吸**（滞留在摄入系统内的液体）与 **Flowback 回流**（从已润湿芯体返逃的液体），并列出回渗设计原则的三组抓手——摄入材料不拉住/滞留液体并促排（毛细/粘附、孔隙网络连通性）、有足够且及时可得的容量锁住液体（容量、分区/分布、速度、单向流、缓冲）、芯体中未锁住的液体与皮肤/吸墨纸隔离。

前瞻部分指向 **ActivTech Hybrid**：该芯体从未被用于如此严苛的超低回渗场景，可能尚未充分优化；早期数据显示 AT hybrid 回渗偏高，但该代码缺少对 ATACAMA 回渗改善至关重要的**面层-导流层压花（liner-surge embossing）**。对比表给出 Nov 2024 GRIFFIN HUT 产品的两个代码：SAM/Fluff（17 gsm tissue 包裹、12 gsm SB 未印花面层、Shalag SS7CT5H80 导流层、有压花）vs AT Hybrid（12 gsm dSB 包裹、12 gsm SB 印花面层、无压花）；芯体由 ADL 生产、成品由 GML 生产，在 GADT 实验室测试。

下一步两条工作流：**Workstream 1 面层**——2 月 GRIFFIN GML 试验验证 4 条假设（Fitesa 12 gsm SB：对照组 oval bond 18% + 0.65% Lertisan；CD Rod bond 10% + 0.65% Lertisan → 更开放的粘合花型减少滞留小口袋；CD Rod bond 10% + 0.3% / 0% Lertisan → 不做亲水处理以排斥残余液，但冒摄入/渗漏风险；以及 Fitesa 22 gsm TS3 开孔膜面层 → 非纤维 + 开孔减少滞留小口袋）；同时由 GR&D 评估 Always Discreet 面层的解吸驱动因素。**Workstream 2 ActivTech 芯体**——2 月在 GML 生产带 LSE 的 Depend 样品以重评是否真有回渗差距，并用动态渗透率测试、STEWIE 微气候与液体分布评估回渗驱动因素；若有差距则依托物性测试结果继续做假设映射。

## 提炼的数字与结论 Key Numbers and Conclusions

| 项目 Item | 数值 / 结论 Value / Conclusion | 备注 Note |
|---|---|---|
| ATACAMA+ 前 Depend 回渗 | 约 1.6 g | 历史基线 |
| ATACAMA+ 后 | 与 Always Discreet 持平 | 根因：surge 与摄入层界面 |
| Always Discreet（SIROCCO 期） | 0.16–0.18 g | 竞品再改进 |
| 当前 DPU 回渗 | 0.25 g | vs Always Discreet 0.18 g |
| **项目目标** | **≤0.15 g**（Depend Fresh Protection，closed cradle） | 立项指标 |
| 回渗双机理 | Desorption 解吸 / Flowback 回流 | 见关联概念页 |
| CT8 surge（Shalag 3） | 回渗改善但摄入变差 | SIROCCO 失败的直接原因 |
| 液体积聚点迁移 | surge → liner | Post-SIROCCO 关键发现 |
| SAM/Fluff 代码 | 17 gsm tissue 包裹 / 12 gsm SB 未印花面层 / Shalag SS7CT5H80 / 有压花 | Nov 2024 GRIFFIN HUT |
| AT Hybrid 代码 | 12 gsm dSB 包裹 / 12 gsm SB 印花面层 / **无压花** | 未见导流层规格 |
| 面层假设变量 | 粘合花型（oval 18% vs CD Rod 10%）× 亲水剂 Lertisan（0.65% / 0.3% / 0%） | 另含 22 gsm TS3 开孔膜 |
| 生产与测试 | ADL 产芯体、GML 产成品、GADT 实验室测试 | 结果窗口：3 月中 |

## 关键论断（key_claims）

- **回渗是系统性残液问题，不是单点材料问题** —— 支撑页：[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]
- **面层-导流层压花（LSE）是 ATACAMA+ 回渗改善的关键工艺，AT Hybrid 早期数据不可直接对比** —— 支撑页：[[Liner-Surge Embossing（面层-导流层压花）]]
- **导流层优化与摄入性能存在结构性互斥，必须同轮验证** —— 支撑页：[[Intake System（摄入系统）]]、[[Shalag（Shalag 导流层与面层材料）]]
- **液体积聚点会随方案迭代迁移（surge → liner），每轮须重新定位** —— 支撑页：[[GRIFFIN Rewet Program（GRIFFIN 超低回渗项目）]]

## 关联页面

- 概念：[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]、[[Rewet Test（回渗测试）]]、[[Intake System（摄入系统）]]、[[Liner-Surge Embossing（面层-导流层压花）]]、[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]、[[IPC BCC OI Portfolio（开放创新项目组合）]]
- 实体：[[GRIFFIN Rewet Program（GRIFFIN 超低回渗项目）]]、[[Shalag（Shalag 导流层与面层材料）]]、[[Fitesa（Fitesa 非织造布）]]
- 对比：（本页未提供可直接落表的成本/供应链数据；竞品回渗对标见下节结论）

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.01.31 - GRIFFIN Rewet.pptx.md`
- 原文链接：（无；内部资料）
- 同族文档：[[2025.06.25 - Learning Cycle Check In（GRIFFIN 学习周期复盘）]]、[[2025.08.28 - GRIFFIN Regroup（GRIFFIN 重整与再聚焦）]]

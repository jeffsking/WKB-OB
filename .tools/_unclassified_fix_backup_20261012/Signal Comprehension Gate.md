---
type: concept
title: "Signal Comprehension Gate"
domain: [卫材研发, 待归类]
status: growing
updated: 2026-09-29
tags: [解读率, 消费者测试, MVP门, 语义分离, 信任落差]
aliases: ["Signal Comprehension Gate 信号解读门"]
---

# Signal Comprehension Gate 信号解读门

> **Definition 定义**：The **≥70% correct-decode** acceptance threshold applied to any consumer-visible indicator (temperature or wetness) — the single gate that decides whether a technically working indicator is allowed to become a product claim.（适用于任何面向消费者的指示信号（温度或湿态）的 **≥70% 正确解读**验收门槛——决定一个"技术上可行"的指示层能否成为产品宣称的唯一致命关卡。）

## Why it dominates 为何它是主导因素

> **The biggest risk is not chemical — it is consumer perception.** 最大风险不在化学，而在消费者感知。

- The **trust gap**: the diaper may look hot while feeling cool to the touch (exterior temperature vs perceived skin feel). Phase 4 comprehension testing is therefore non-negotiable.（**信任落差**：尿裤外观可能显示"热"，而触感偏凉——外部温度与主观肤感不一致。因此第四阶段解读测试不可省略。）
- **Overpromising kills the claim**: the deliverable is a visual cue that helps caregivers know *when to act*, not a precision clinical thermometer.（**过度承诺会毁掉宣称**：交付物是帮助看护者判断"何时该处理"的视觉提示，而非精密临床温度计。）
- The gauge is bound to the **bench** as well: the bench protocol must test dry **and** wet states and quantify the **false-trigger rate** — the single most important MVP exit gate.（该门同时绑定台架：台架方案必须测**干态与湿态**，并量化**误触发率**——这是最重要的 MVP 出口门。）

## Gate definitions 门定义

| Gate 门 | Threshold 门槛 | Applies to 适用 | Source 出处 |
|---|---|---|---|
| Caregiver correct-decode 看护者正确解读 | **≥70%** correctly read "too hot / too cold / just right" | MVP A thermochromic | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| Signal decoding (Phase 4) 信号解读 | ≥70% correct decoding of "too hot/cold" **or** "wet exposure" **without confusing the signals** | MVP A + MVP B (+ C) | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| Differentiation 差异化 | Signal must be distinctly different from the traditional wetness indicator to prevent semantic confusion | MVP B, MVP C | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| False-trigger rate 误触发率 | Quantified; no dry false trigger in hot/humid storage | All MVPs (bench) | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| Response-time legibility 响应可辨识 | ≤120 s (temp) / ≤60 s (hydro) to a recognisable state | Bench gates | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| Combinatorial exit rule 复合退出规则 | If comprehension fails or error rates are high in Phase 4, halt the combo and revert to single-function MVP | MVP C (P2 learning prototype) | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| Core-function override 核心功能优先 | If at any point the technology compromises absorbency, fit, cost or skin safety, the MVP is immediately halted | All MVPs | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |

## How the gate reshapes the programme 该门如何改写项目设计

1. **Sequencing rule 排序规则**：do **not** replace the existing wetness indicator — use it as differentiation learning; run MVP C (combo) only after single-function validation, and fall back to single-function if the misread rate is high.（**不**替代现有尿显，先用它做差异化学习；复合方案（C）只在单功能验证通过后启动，若误读率高则回退单功能。）
2. **Option value 期权价值**：the combo is framed as a **learning prototype**, not a launch candidate — it exists to test whether caregivers can decode two simultaneous signals without semantic fighting.（复合方案被定义为**学习型原型**而非量产候选——用于验证看护者能否在不产生语义冲突的情况下解读两个并行信号。）
3. **Claim discipline 宣称纪律**：keep the product positioned as a "**reason to believe**", so that a bounded benefit does not have to carry a clinical-level claim.（坚持把产品定位为"**可信理由**"，从而不必用临床级宣称去背一个有限收益。）

## Adjacent concepts 相邻概念

- Objects 对象：[[Thermochromic Microcapsule (Leuco Dye System)]]、[[Wetness Indicator Glue]]
- Application 应用：[[Diaper Microclimate]]、[[智能尿裤功能层]]、[[变色油墨]]
- Comparison 对比：[[Thermochromic vs Hydrochromic Wetness-Comfort Indicators]]
- Acceptance baseline 验收基线：[[芯体测试方法与验收基准（STM）]]

## Lessons learned 经验教训

> ✅ **Validation（2026-09-29）**：本批两份来源把**同一个 ≥70% 解读门槛**同时写进市场评估与技术路线页（[[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] 记为"the real feasibility risk"；[[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] 记为 MVP A/Phase 4 的验证门），并都把"信任落差/感知"列为首要风险——本页表述与两者一致。

- **要点**：指示类功能层的验收**不在材料指标上闭合**，而在消费者解读率上闭合；材料与台架工作只是入场的必要非充分条件。
- **风险**：**语义重叠**（与现有尿显混淆）与**误触发**（干态/储存期提前触发）是两个会直接判死的失效模式。
- **待补 `[待验证]`**：≥70% 门槛的样本量与统计功效口径；不同市场/文化下的解读率差异。

## Sources 来源

- [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/ThermoHydro_TechReview_EN_v3_2026-08-05.pptx.md`
- [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/Diaper_Microclimate_Visualization_Feasibility.pptx.md`

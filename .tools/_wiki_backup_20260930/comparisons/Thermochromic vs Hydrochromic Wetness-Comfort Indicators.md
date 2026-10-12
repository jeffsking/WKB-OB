---
type: comparison
title: "Thermochromic vs Hydrochromic Wetness-Comfort Indicators"
subjects: ["[[Thermochromic Microcapsule (Leuco Dye System)]]", "[[Wetness Indicator Glue]]"]
dimension: 综合
updated: 2026-09-29
tags: [热致变色, 湿致变色, 尿显, 成本, 供应链风险, MVP, 安全合规]
aliases: ["Thermochromic vs Hydrochromic Wetness-Comfort Indicators（温度 vs 湿度视觉提示）"]
---

# Thermochromic vs Hydrochromic Wetness-Comfort Indicators（温度 vs 湿度视觉提示）

> **Compared objects 对比对象**：面向尿裤的两条视觉提示路线 —— **R1 温致变色（温度 / 热舒适）** vs **R2/R3 湿致变色（湿度与尿湿）**。
> **Question answered 回答的问题**：MVP 阶段应该先做哪一条；两条路线的成本与供应链风险差在哪里。
> 数据基准：本批 Thermal Comfort 3 份来源（2026-07 ~ 2026-09）；数字全部溯源至源摘要页，无来源项标 `[待验证]`。

## Comparison table 对比维度表

> 必含「成本」「供应链风险」两列。

| Dimension 维度 | **R1 Thermochromic 温致变色** | **R2 Hot-melt wetness glue 热熔尿显胶**（及 R3 水基湿致油墨） | Evidence 依据 |
|---|---|---|---|
| **Signal meaning 信号含义** | Thermal comfort / "too hot / too cold / just right" —— 现有尿显**无法**表达的维度 | "Wetness has occurred"（热熔胶不可逆）／R3 可做成"实时湿量水平"（可逆定制微胶囊） | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]、[[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| **Product form 产品形态** | 外层印刷条或复合标签片（芯体中线 / 裆部面板）；可逆 | 底膜内面**胶线**（热熔胶）；或直接印于 PE 透气膜/非织造布（水基油墨） | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| **Mechanism 机理** | Leuco 染料 + 显色剂 + 溶剂微胶囊；阈值上下发生电子转移/相变；降温可逆 | 尿液溶解/重置树脂 → 黄/橙→蓝（不可逆）；水基油墨由液体接触触发显色/透明 | [[Thermochromic Microcapsule (Leuco Dye System)]]、[[Wetness Indicator Glue]] |
| **Activation / response 激活与响应** | 激活带 30–37 ℃ 可定制；显示点 32/34/36 ℃；响应 ≤120 s 可读；≥10 次热循环 | 首次显色 ≤60 s；最小可检出 5/10/20 mL；面积随冲击增长（非线性） | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| **Technical risk 技术风险** | **高**：干态热信号技术难度大；无尿裤专用 SKU；UV 稳定性与长期漂移；储存/运输期提前触发 | **低**：热熔路线已工业化（占产品形态 84.1%），液体接触触发远较 RH 传感器现实；R3 水基油墨略增工序复杂度 | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]、[[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| **Comprehension risk 解读风险** | 需 **>70%** 正确解读"过热/过冷/舒适"；存在**信任落差**（外观显示热、触感偏凉） | 需 **>70%** 正确解读且**与传统尿显明确区分**（语义重叠是首要失效模式）；尿 pH、面层乳液、SAP 粉尘为干扰源 | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]]、[[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| **Cost 成本** | `[待验证]`——本批**未给出温变油墨/标签的成本口径**；成本结论仅为"市场属定制开发，合作深度优先于价格" | **热熔胶 = 成熟主流（成本已释放）**；**水基湿致油墨相对热熔胶约 2–3 倍成本差**，须由消费者测试的差异化提升来证明合理性 | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| **Supply-chain risk 供应链风险** | **中-高（合规驱动）**：温变一级供方集中于 CTI（美）与 Matsui（日，**部分产品含微量甲醛、排除婴儿直接接触**）；OliKrom 为 Tier-2 定制温带；国内有千色变、名博、长沙新诺等可作成本/交期补充 | **低-中**：热熔胶由 Bostik / Henkel / H.B. Fuller / Nan Pao / 3M 多家供应，代表已工业化 84% 主流；国内有科维尔（水基湿显油墨）、千色变等，交期与成本更灵活 | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]、[[CTI (Chromatic Technologies)]]、[[Matsui Shikiso (松井)]]、[[Bostik]]、[[汉高]] |
| **Also measured 亦须测量** | 干态本底低干扰（避免误读为湿）；耐层压；无迁移/渗色（硬底线） | 色牢度：无渗色、无回渗；机械：无掉粉/掉色；干态（高温高湿储存）无假触发；耐乳液与 SAP 粉尘 | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| **Safety & compliance 安全合规** | 共用硬门：100% 无 BPA、零甲醛、零重金属；ISO 10993 / REACH / FDA / GB/T 35613-2017。**温变侧额外受 Matsui 甲醛告警约束** | 同左；粉末形态在验证前**禁止**用于皮肤层；**绝对禁止**回渗、可见渗色与直接皮肤接触 | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]、[[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| **Placement 位置** | 外层 / 底膜窗口（非皮肤接触面）；MVP A 位于芯体中线外表面（前下/裆部） | 底膜内面（热熔胶）／与现有尿显相邻（水基窗口片） | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]、[[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| **MVP priority 优先级** | **MVP A · P1**（难度 medium） | **MVP B · P1**（难度 low–medium）；复合 MVP C · **P2**（med–high，仅学习型原型） | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| **Market anchor 市场锚** | 差异化前沿：无尿裤专用 SKU，"先定义阈值与合规标准者占 IP 护城河" | 已工业化主流：全球尿显市场 $506M（2025）→ $774M（2032E），CAGR 6.28%；婴儿尿裤占下游 62.9%；热熔形态 84.1%；亚太占 42% | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |

> **Footnote 尾注**：本表所有信息来自 [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]、[[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] 两份源摘要页，供方属性另经 [[CTI (Chromatic Technologies)]]、[[Matsui Shikiso (松井)]]、[[Bostik]]、[[汉高]] 页追溯。原文对市场与供方信息标注证据等级（`[F]` 事实 / `[I]` 推断 / `[A]` 假设 / `[E]` 估算）；本表的"台架门槛"均为 `[A]` 一版假设。

> 🔴 **manual_review（2026-09-29）**：本表引用了**水基湿致油墨相对热熔胶"约 2–3 倍"的成本倍数**与**供应商评估/门控状态**，属商务敏感信息（AGENTS.md §5 边界）。页面只保留**相对倍数与路线结论**，**不展开具体报价**；对外引用前须人工确认。

## Fit by scenario 各自适用场景

- **Thermochromic（温致变色）**：适合作为**差异化前沿**的探索项——它覆盖现有尿显无法表达的"热舒适/湿度积累"维度，但必须先在台架上证明**干态可读、无假触发、耐层压**，并用消费者测试跨过 >70% 解读率与**信任落差**两道关。
- **Hot-melt wetness glue（热熔尿显胶）**：适合作为**低风险试点与量产基线**——已工业化、适配现有转化线、多家供方；但**不得替代**现有尿显，只能做叠加式差异化，且必须解决与既有尿显的**语义区分**问题。
- **Water-based hydro ink（水基湿致油墨）**：适合作为**第二阶段的差异化/环保选项**（图形可定制、工序简化、可设计为可逆），代价是约 2–3 倍成本，须由消费者测试的差异化提升来证明。

## Conclusion 结论

**先湿后温、两条并行但不同风险等级**：湿敏路线（热熔胶）是**已工业化、低风险的量产基线**，温敏路线是**无专用 SKU 的差异化前沿**；MVP 阶段按"两个独立视觉信号 + 复用现有尿显"的低后悔组合推进，**不替代**现有尿显，并用同一条 **≥70% 解读率 + 干/湿双态 + 误触发率**出口门统一裁判。

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · 20 家供应商矩阵与五阶段推进路线）

> 追加来源 `[[Thermochromic and Hydrochromic Materials Feasibility Review（温变湿变材料可行性分析·中文版）]]`（卫材研发中心 2026-08-04，内部参考）。本段**只补"供应商格局与推进路线"，不改动上方对比维度表、适用场景与结论**。

### 1. 供应商分层与场景推荐（本批新增的落地层）

| Tier | 供应商 | 定位 |
|---|---|---|
| **Tier 1 主接触** | **Matsui（松井）、CTI、DaeHyun** | 温变工业化最强 / 全品类标杆 / 温+湿微胶囊 |
| Tier 2 | **OliKrom** | 定制温区配方 |
| Tier 3 | New Prismatic | 高温阈值示范补充 |

| 应用场景 | 首选 | 备选 | 理由 |
|---|---|---|---|
| **温变 MVP（P1）** | CTI + Matsui（定制） | OliKrom、广州乐迪、千色变 | 工业化温变最强；需解决婴儿安全（Matsui 部分含微量甲醛） |
| **湿变 MVP（P1）** | **Bostik / Henkel / H.B. Fuller** | 科维尔（水性）、MicroCapsule（韩） | 热熔胶 84% 主流成熟，风险最低 |
| 组合版（P2） | CTI（温）+ Bostik（湿） | DaeHyun（双能力） | 双能力覆盖，分阶段整合 |
| 国产替代 / 成本敏感 | 千色变 / 广州乐迪 / 科维尔 | 格林春天、名博、长沙新诺 | 性价比高、本地交付快 |

- **评选维度（权重）**：技术成熟度 **高** ｜ **安全合规 高（硬性：BPA-Free / 无甲醛 / ISO 10993 / REACH / GB）** ｜ 卫品应用经验 **高** ｜ 产能与交付 中 ｜ 成本 中 ｜ Lead time / MOQ 中 ｜ 技术支持 中。
- **新增候选（本批首次入库）**：Intellego（瑞典，光敏湿显）、Nan Pao 南宝（台湾，HM-895 橙→蓝绿）、SUNREE 三瑞卫护（<30 s 变色）、崇裕科技 Spindrift（台湾，皮肤接触级认证、恒安/尤妮佳供应链）、深圳市变色科技（垂直整合）。
- **不宜用于大批量消费品的路线**：LCR Hallcrest / SpotSee（TLC 液晶高精度，偏科研/工业，成本高）。

### 2. 五阶段推进与退出门（本批新增）

| 阶段 | 目标 | Gate |
|---|---|---|
| Phase 0 | Desk research + 短名单（5–8 家） | 候选清单 + **RFQ 发出**；≥5 家回样承诺（M0–1） |
| Phase 1 | 离体片材 coupon 打样 | 稳定显色体系 **≥2**（M2–3） |
| Phase 2 | 纸尿裤外层 dummy build（**不上人体 / 不做 full claim**） | 可读 + converting 兼容（M3–5） |
| Phase 3 | bench insult + thermal map，**dry/wet 双态** | 响应 / 对比度达标（M5–7） |
| Phase 4 | quick consumer comprehension | **≥70% 正确解码**（M7–9） |
| — | 组合版（若单功能达标） | 理解错误率高则**拆回单功能**（M9–11） |
| — | 量产可行性：BOM / 成本 / 合规路径 | **Go / No-Go**（M11–12） |

### 3. ✅ 与上方表的互证 / ⚠️ 一处新增强调

- ✅ **市场锚一致**：本源给湿敏指示胶 2025 年 **$506M → 2032 年 $774M（CAGR 6.28%）**、婴儿尿裤占下游 **62.92%**、热熔形态 **84%** —— 与上方表"Market anchor"列**数值同源、口径一致**。
- ✅ **优先级一致**：温变 MVP A · P1 / 湿变 MVP B · P1 / 组合 MVP C · P2 —— 与上方表"MVP priority"列一致。
- ⚠️ **本批新增强调**：**false trigger（误触发）率的量化是 MVP 退出的最关键门槛之一**——上方表把"误触发率"列在出口门内，本源进一步把它提升为**最关键单项**；并明确 **dry 与 wet 双态均须测试**。
- ⚠️ **叙事风险（新增）**：妈妈对 *"actively maintaining a just-right zone"* 这类**强 claim 接受度不足** —— 更适合从 *"help you know when to act"* 的**视觉 cue** 切入，而非宣称精确控温。这与上方结论"不替代现有尿显、只做叠加式差异化"**同向**。

> ✅ 验证（2026-09-29）：本追加段**未修正**上方任何结论；上方对比维度表（含成本与供应链风险两列）**继续有效**，本批补的是**供应商格局、推进路线与叙事风险**。
> 🔴 **manual_review（2026-09-29）**：本源供应商矩阵源自含**潜在供应商联系人清单**的内部 Brief，且含 **$/unit 或 $/kg、MOQ、lead time** 等商务维度。依 AGENTS.md §5，**本页只记能力矩阵、权重与选型结论，不落报价、联系人与商务条款**。

## Sources 来源

- [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/ThermoHydro_TechReview_EN_v3_2026-08-05.pptx.md`
- [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/Diaper_Microclimate_Visualization_Feasibility.pptx.md`
- [[Thermochromic and Hydrochromic Materials Feasibility Review（温变湿变材料可行性分析·中文版）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/温变湿变材料可行性分析报告_2026-08-04.docx.md`（2026-09-29 追加）

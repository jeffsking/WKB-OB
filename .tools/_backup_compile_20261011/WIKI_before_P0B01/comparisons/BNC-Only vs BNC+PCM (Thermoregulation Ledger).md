---
type: comparison
title: "BNC-Only vs BNC+PCM (Thermoregulation Ledger)"
subjects: ["[[PCM-Free Thermoregulation]]", "[[细菌纳米纤维素]]"]
dimension: 成本
updated: 2026-09-29
tags: [BNC, PCM, 相变微胶囊, 调温, 成本, 供应链风险, 克重]
aliases: ["BNC-Only vs BNC+PCM（Thermoregulation Ledger）"]
---

# BNC-Only vs BNC+PCM（Thermoregulation Ledger）

> **Compared objects 对比对象**：尿裤调温层的两种实现 —— **纯 BNC 纳米纤维网络（无相变化学）** vs **BNC + PCM 微胶囊复合**。
> **Question answered 回答的问题**：去掉微胶囊后，调温能力损失多少、成本与供应链风险省下多少。
> 数据基准：[[PCM-Free Thermoregulation with BNC Nanofiber Network]]（v1，2026-07-31）。**原文自述全部数值为文献推导估算（≈），非实测**。

## Comparison table 对比维度表

> 必含「成本」「供应链风险」两列。

| Dimension 维度 | **BNC-only 纯 BNC** | **BNC + PCM 微胶囊** | Evidence 依据 |
|---|---|---|---|
| **Mechanism 机理** | Structure-intrinsic（孔隙 + Knudsen + 点接触 + 结合水 + IR 散射） | Latent-heat additive（在设定温度以潜热吸收热事件） | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| **Functions covered 覆盖功能** | 隔热 + 缓冲 + 散热（**3/4 功能**） | 上述三项 + **尖峰吸收** | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| **Energy density 能量密度** | Sensible（低） | Latent ≈100–200 J/g | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| **Thermal performance 热性能** | k ≈0.035 W/m·K（气凝胶级）；贴肤侧初始升温速率 **−58% dT/dt** vs 对照（模型）；三条曲线最终收敛到同一稳态 | 在转变窗口出现相变平台；稳态与纯 BNC 相同 | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| **Honest gap 诚实差距** | 首窗 ΔT **落后 PCM 约 1–2 分钟**（模型）；无恒温平台（rate-based） | 设定点以上同样**不额外贡献**（差距有界，非开放） | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| **Cost 成本（单位增量）** | **0**（复用现有 BNC）；结构升级成本 ≈$0.002–0.004/unit | **+≈$0.008–0.015/unit**（微胶囊）+ 壳层/封装 ≈$0.001–0.003 + QA/批次波动缓冲 ≈$0.001 | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| **Cost 成本（净结果）** | **净节省 ≈$0.006–0.011/unit**；约 **0.6–0.9% of BOM**；在 ≈10⁹ 件/年规模下约 **$6–11 M/年**（未计 QA 与复杂度节省） | 基准（分母） | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| ** Basis weight 克重** | **+0 gsm**（沿用既有 BNC） | **+≈15–40 gsm** | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| **Leakage / rupture risk 泄漏与破裂风险** | 无 | 壳脆性 → 破裂与批次波动；破裂胶囊污染 SAP 并放宽控制限；游离 PCM 提高皮肤风险、恶化回渗与气味 | [[PCM-Free Thermoregulation with BNC Nanofiber Network]]、[[Microencapsulation]] |
| **Supply-chain risk 供应链风险** | **低**：单一纤维素体系，链条更简单；无专用封装环节 | **中-高**：增加专用封装层级，多供应商、脆弱、带库存与 QA 负担 | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| **Sustainability 可持续性** | 可冲散、生物基 | 石化壳层，存在微塑料风险 | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| **Setpoint precision 设定点精度** | 无（纯结构，速率型调节） | 在 Tm 处精确 | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| **Verdict 结论** | 多小时稳态舒适下 **PCM 属冗余 → 默认路线** | **仅对瞬态有边际价值** | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| **Gate 门** | AUL/CRC ≥ 现状；回渗 ≤ 现状；皮肤模型 ΔT/dt ≤ 目标 | 仅当上述门失败时启用；门为"规模化后成本可接受" | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |

> **Footnote 尾注**：本表所有数值来自单一源摘要页 [[PCM-Free Thermoregulation with BNC Nanofiber Network]]（口径 v1，2026-07-31），并回链至 [[PCM-Free Thermoregulation]]、[[细菌纳米纤维素]]、[[Microencapsulation]]。原文注明：**所有数值为文献推导估算（≈），须在 Gate 阶段以内部实测替换**。

## Fit by scenario 各自适用场景

- **BNC-only（纯结构）**：适合**多小时稳态微气候舒适**（这正是纸尿裤的主要工况）——用 0 gsm 增量、0 泄漏风险、生物基链条覆盖 4 项功能中的 3 项；短板在**瞬态尖峰与设定点精度**，需用结构补偿（Z 向孔隙梯度、贴肤侧更高 BNC 克重、结合水管理、透气底膜 + ADL 协同、REL 增强层）补足。
- **BNC + PCM（复合）**：仅为**兜底方案（fallback）**——只在结构补偿路线未通过门时启用；其边际价值限于温热排液后的最初约 60 秒。

## Conclusion 结论

对多小时穿着的纸尿裤而言，**去 PCM 是默认路线**：微胶囊只在瞬态尖峰上提供边际价值，却同时带来 +15–40 gsm、+$0.008–0.015/件、壳脆/泄漏风险与一层多供应商封装环节；纯 BNC 结构路线可省下**约 $0.006–0.011/件（0.6–0.9% BOM）**，代价是瞬态响应落后约 1–2 分钟且无恒温平台——结论是**用结构补偿补差，而非回退到化学方案**。

## Sources 来源

- [[PCM-Free Thermoregulation with BNC Nanofiber Network]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/BNC_PCMfree_Thermoregulation_v1_20260731.pptx.md`

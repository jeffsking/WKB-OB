---
type: concept
title: "Blowout Leakage Test（爆漏测试）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-30
tags: [测试方法, 爆漏, 稀便, Blowout, 效率因子, 腰围力]
aliases: ["Blowout Method", "爆漏测试"]
---

# Blowout Leakage Test（爆漏测试）

> One-line definition 一句话定义：用**人造稀便（artificial BM）**加载吸收制品、量取渗漏到配衡纸巾上的克重，并按公式算出**爆漏百分比（Blowout Percent Leakage）**的测试方法——用于量化后腰口对低黏度排泄物的防漏能力。

## Definition / Mechanism 定义与机理拆解

1. **测量量**：渗漏到**已配衡（tared）纸巾**上的人造 BM 克重。
2. **计算公式（来源原文口径）**：

   `Blowout Percent Leakage [%] = (gram leaked artificial BM collected on the tared paper towel / total gram artificial BM applied) × 100`

3. **重复与精度**：同一型号制品测 **3–4 次**，报告均值，精度 **±0.01 %**。
4. **配套派生指标**：
   - **Efficiency Factor 效率因子** = (Blowout Leakage Weight / Diaper Weight) × 100 —— 把制品自重纳入考虑，避免"用更厚的材料换低漏量"；
   - **Waist Circumference Force 腰围力**（另有独立测试方法）——把防漏与腰围贴合/上拉手感并列约束。
5. **相关测试（同一专利文件内）**：**Belt Zone Tensile Stress Measurement**（腰带区拉伸应力测定）——用于定义护挡弹性部的 20–70 N/m。
6. **干态重量条件**：测试前制品须在 **23 ℃ ±3 ℃、相对湿度 50 % ±2 %** 下**至少平衡 2 小时**。

## Key parameters 关键参数表

| Parameter 参数 | Typical value / range 典型值 / 范围 | Source 出处 |
|---|---|---|
| 加载介质 | Artificial BM（人造稀便） | [[US2022-0339044A1 Pant-Type Absorbent Article with Waist Guard (P&G)]] |
| 收集件 | Tared paper towel（配衡纸巾） | 同上 |
| 重复次数 / 精度 | 3–4 次 / ±0.01 % | 同上（[0100]） |
| 平衡条件 | 23 ℃ ±3 ℃、50 % ±2 % RH，≥2 h | 同上（[0014]） |
| 实施例结果（爆漏率） | 0.53 % / 0.17 % / 0.90 % | 同上（Table 1） |
| 对比例结果（爆漏率） | 9.35 % / 10.84 % / 9.33 % / 5.82 % / 4.43 % | 同上 |
| 实施例爆漏重量 | 0.67 g / 0.17 g / 0.90 g | 同上 |
| 对比例爆漏重量 | 14.02 g / 10.84 g / 14.00 g / 8.93 g / 6.20 g | 同上 |
| 效率因子（实施例） | 2.33 % / 0.56 % / 3.01 % | 同上 |
| 效率因子（对比例） | 42.49 % / 38.73 % / 43.34 % / 23.70 % / 16.15 % | 同上 |
| 干态制品重量 | 实施例 28.6 / 29.8 / 29.9 g；对比例 33 / 28 / 32.3 / 37.7 / 38.4 g | 同上 |
| 护挡弹性部拉伸应力 | 实施例 57 / 29 / 57 N/m；对比例 NA | 同上（Belt Zone Tensile Stress Measurement） |
| 后腰带宽度 / 制品长度 | 实施例 380–410 mm / 440–450 mm | 同上 |

> ⚠️ **禁止无来源参数**：本表数字全部来自 [[US2022-0339044A1 Pant-Type Absorbent Article with Waist Guard (P&G)]]。**来源未给出人造 BM 的确切配方、黏度、加载量、加载速度与加载位置**，标 `[待验证]`——这些参数是复现该测试的必要条件。

## Adjacent concepts 相邻概念

- 被测结构：[[Waist Guard（腰围护挡）]]
- 其他芯体/结构测试：[[芯体测试方法与验收基准（STM）]]、[[SAP性能指标（CRC AUL GBP Vortex）]]
- 同类"用户体验"指标：[[Skin Contact Pressure（皮肤接触压力）]]、[[Diaper Microclimate]]
- 权利人：[[The Procter & Gamble Company（宝洁）]]

## 经验教训

> ✅ 验证（2026-09-29，来源 [[US2022-0339044A1 Pant-Type Absorbent Article with Waist Guard (P&G)]]）：本页记录的方法把"**爆漏**"从主观描述转为**可复现的百分比指标**，并配了**效率因子**（对自重归一）与**腰围力**（对贴合归一）两项约束。这修正了"防漏只能靠加厚"的评价习惯——效率因子正是用来惩罚"加厚换低漏"。

- **教训一（指标组合）**：单一爆漏率不足以评价设计，须与**效率因子 + 腰围力**联看，否则容易得出"越厚越好"的错误结论。
- **教训二（复现性）**：引用该测试结果前，须确认人造 BM 配方/黏度、加载量与加载位置——来源未给这些参数，**跨企业比较须谨慎**，标 `[待验证]`。
- **待补 `[待验证]`**：人造 BM 配方与黏度；加载速度与位置；与本库其他湿性测试（回渗、Vortex）的相关性。

## Sources 来源

- [[US2022-0339044A1 Pant-Type Absorbent Article with Waist Guard (P&G)]] —— `RAW/ima_sync/个人知识库/WKB/Areas/IP/四-2_Pant-type_absorbent_article_with_waist_guard.pdf.md`

> 🔴 **manual_review（2026-09-29）**：本页为**专利申请公开文本所载测试方法的客观摘录**；方法细节在来源中并不完整，实施前须回原文核对。

## Related Sources 关联来源

- [[US2022-0339044A1 Pant-Type Absorbent Article with Waist Guard (P&G)]]

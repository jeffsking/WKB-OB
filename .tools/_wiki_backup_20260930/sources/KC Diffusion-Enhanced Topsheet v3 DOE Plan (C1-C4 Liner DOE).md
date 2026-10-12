---
type: source
title: "KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Projects/Liner/KC_Diffusion_Enhanced_Topsheet_v3.xlsx.md
original_link: ""
date_published: 2026-08-14
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "Four candidate topsheet configs (C1 Lenzing Lyocell trilobal / C2 Fudi trilobal ES / C3 Suzhou mono-PET spindle / C4 cross PET) are screened at 3 oven temperatures (126/128/130 °C) and 2 loading levels — 33 runs over 3 stages（四配置 × 三温度 × 两载荷，共 33 次试验，分 3 阶段）"
  - "Final pass/fail is set by the finished-diaper enterprise standard: rewet <5.9 g @0.5 kPa, SAP utilization ≥63%, wet tensile ≥75 N/m, STT ≤0.8 s（终判以成品尿裤企业标准为准，材料级仅作筛选门）"
  - "C1 (Lyocell trilobal) is expected to win surface area and hand feel but carries the highest cost; the cost ceiling is ≤20% premium over C3（C1 性能最优但成本最高，成本上限为相对 C3 溢价 ≤20%）"
  - "PE sheath at ~130 °C is the process risk anchor: too hot flattens the trilobal section and destroys surface area（PE 皮层 130 ℃ 附近存在扁平化风险，是温度窗口的核心约束）"
  - "KB anchors carried into the design: v11 SAP utilization 63.6% / MD spread 34.9%; CoPET/PET ADL −24% 3rd rewet at +16% price（沿用 KB 既有锚点：v11 SAP 利用率 63.6%、MD 铺展 34.9%；CoPET/PET ADL 第三次回渗 −24%、价格 +16%）"
pages_linked: ["[[ATB双梳理面层（Dual-Card Topsheet）]]", "[[三叶形截面纤维（Trilobal Fibre）]]", "[[Shaped PET Add-On Window]]", "[[Diffusion-Enhanced Topsheet C1-C4 (Cost-Performance-Supply Chain)]]", "[[Pentagram PET (Star Cross-Section Fibre)]]", "[[热风粘合无纺布]]", "[[亲水整理耐久性]]", "[[延江（Yanjan）]]", "[[兰精集团]]", "[[福地（Fudi）]]", "[[Suzhou Yimeng (Mono-PET Spinner)]]"]
---

# KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)

## One-line positioning 一句话定位

The **test-planning page for the 4-configuration diffusion-enhanced topsheet DOE** — it defines the candidate fibre systems, the temperature/loading process window, the acceptance metrics and the 3-stage, 33-run test architecture for the REL ultra-thin core topsheet (50 gsm dual-card ATB). It is the batch's answer to "**which fibre goes on top, at what oven temperature, and how do we know it worked**".
本页是本批**「扩散增强面层 4 配置 DOE」的试验设计页**：锁定候选纤维体系、温度/载荷工艺窗口、验收指标与「3 阶段 33 次试验」架构，服务于 REL 超薄芯体面层（50 gsm 双梳理 ATB）。

## Summary 摘要

The workbook (v3, dated 2026-08-14, 7 sheets: Notes / Overview / DOE_Matrix / Characterization / Schedule / Risk / Gantt) evaluates four topsheet configurations on a **50 gsm dual-card air-through-bonded (ATB) web** built as 25 gsm upper + 25 gsm lower, with durable hydrophilic finish and **no increase in oven temperature**.
本表格（v3，2026-08-14，含 7 个工作表）在 **50 gsm 双梳理穿透热风粘合（ATB）网**（上 25 gsm + 下 25 gsm、耐久亲水整理、**不提高烘箱温度**）上评估 4 种配置。

Four configurations: **C1 "Optimal"** — upper card 10% Lenzing Lyocell (trilobal, 2D) + 90% ES, lower card 50% Fudi ES + 50% own ES; best surface area and hand feel, highest cost. **C2 "Alternative"** — upper card 10% Fudi trilobal ES (3D) + 90% 2D ES, lower card 50% 3D Fudi trilobal + 50% 4D own ES; balanced cost/performance. **C3 "Suzhou"** — upper card 10% Suzhou Yimeng mono-PET spindle (3.5D) + 90% 2D ES, lower card same as C3-family; positioned as the cost-effective PET alternative. **C4 "Cross"** — upper card 10% 1.5D 4D cross-shaped PET + 90% 2D ES; skin feel still pending.
四配置：C1 最优解（上层 10% 兰精莱赛尔三叶形 2D + 90% ES，下层 50% 福地 ES + 50% 自有 ES；表面积与手感最佳、成本最高）；C2 备选（上层 10% 福地三叶形 ES 3D + 90% 2D ES；成本/性能平衡）；C3 苏州方案（上层 10% 苏州益盟单组分 PET 纺锭型 3.5D + 90% 2D ES；成本导向的 PET 替代）；C4 十字方案（上层 10% 1.5D 4D 十字截面 PET + 90% 2D ES；手感待定）。

Process variables are **temperature (X2, 3 levels: 126 / 128 / 130 °C)** — the PE sheath melts/flows near 130 °C while PET stays stable to ~220 °C, so the window exists to find the "strength vs flattening" balance — and **loading (X3, 2 levels: Low / High)**, which affects acquisition rate and bonding strength.
工艺变量为**温度**（3 水平：126/128/130 ℃；PE 皮层约 130 ℃ 流动、PET 约 220 ℃ 稳定，该窗口用于寻找「强度 vs 扁平化」平衡点）与**载荷**（2 水平：低/高，影响摄入速率与粘合强度）。

Acceptance is graded in two tiers: **PRIMARY = finished-diaper enterprise standard** (rewet <5.9 g @0.5 kPa after 2 insults, core stain uniformity ≥A, SAP utilization ≥63%, wet tensile ≥75 N/m), and **material-level = screening gate only** (STT ≤0.8 s, 3rd rewet ≤0.5 g with target 0.30 g, MD spread ≥34% vs 34.9% anchor, caliper retention ≥92%, TS7 softness ≥50, fuzz ≤2, D_aniso ≥2.5, bonding strength ≥10 N/cm).
验收分两档：**PRIMARY 为成品尿裤企业标准**（0.5 kPa 双次冲击回渗 <5.9 g、芯体染色均匀度 ≥A、SAP 利用率 ≥63%、湿拉伸 ≥75 N/m）；**材料级仅作筛选门**（STT ≤0.8 s、第三次回渗 ≤0.5 g（目标 0.30 g）、MD 铺展 ≥34%（锚点 34.9%）、厚度保持 ≥92%、TS7 柔软度 ≥50、起毛 ≤2、D_aniso ≥2.5、粘合强度 ≥10 N/cm）。

The test architecture is a 3-stage randomized DOE (seed 20260814) totalling 33 runs: **Stage 1** configuration screen (4 configs × 3 temps × medium load = 12, plus 3 centre runs = 15), **Stage 2** temperature × loading optimization on the top-2 configs (12 + 2 = 14), **Stage 3** confirmation (top-2 × 2 replicates = 4), plus 1 anchor run (C1 at 128 °C). Schedule is 14 weeks (W1–W14) starting 2026-08-17, with milestones M1–M7 and 3 acceptance gates.
试验架构为三阶段随机化 DOE（随机种子 20260814），共 33 次：阶段 1 配置筛选 15 次、阶段 2 温度×载荷优化 14 次、阶段 3 确证 4 次，另加 1 次锚点（C1 @128 ℃）。排期为 14 周（W1–W14，起 2026-08-17），含 M1–M7 里程碑与 3 道验收门。

## Extracted numbers and conclusions 提炼的数字与结论

| Item 项目 | Value 数值 / conclusion 结论 | Note 备注 |
|---|---|---|
| Total basis weight 总克重 | 50 gsm (25 upper + 25 lower) | Fixed across all runs 全试验固定 |
| Upper-card shaped fibre dosage 上层异形纤维剂量 | 10% (all four configs) | C1 Lyocell / C2 Fudi trilobal ES / C3 mono-PET spindle / C4 cross PET |
| Lower-card trilobal dosage 下层三叶形剂量 | 50% (50% Fudi + 50% own ES) | C2 uses 50% 3D Fudi + 50% 4D own |
| Oven temperature levels 烘箱温度水平 | 126 / 128 / 130 °C | Covering the PE melt window 覆盖 PE 熔融窗口 |
| Loading levels 载荷水平 | Low / High (medium in Stage 1) | Affects acquisition rate and tensile |
| DOE run count 试验次数 | 33 (15 + 14 + 4) + 1 anchor | Seed 20260814；3 blocks per stage |
| Plan duration 计划周期 | 14 weeks (W1–W14 from 2026-08-17) | M1–M7 milestones |
| Rewet target (finished diaper) 回渗目标 | <5.9 g @0.5 kPa, 2 insults | PRIMARY final gate 终判门 |
| SAP utilization target SAP 利用率 | ≥63% (v11 anchor 63.6%) | PRIMARY final gate |
| Wet tensile target 湿拉伸目标 | ≥75 N/m (from 58 N/m) | PRIMARY；also ≥70 N/m sheet-level secondary 另设 ≥70 N/m 次级 |
| STT target STT 目标 | ≤0.8 s (from 0.9 s) | Screening gate 筛选门 |
| 3rd rewet target 第三次回渗 | ≤0.5 g (target 0.30 g); baseline 0.04 g | GB/T 13662-1992 |
| MD spread target MD 铺展 | ≥34% (anchor 34.9%, D_aniso = 3) | GB/T 8939-2008 |
| Caliper retention 厚度保持 | ≥92% (loss ≥8% kills the ADL) | Flattening check 扁平化检查 |
| Softness 柔软度 | TS7 ≥50 (higher = softer) | EDANA 801.1-02 |
| Fuzz score 起毛评分 | ≤2 (0–3 scale; >~15% profiled = risk) | GB/T 8939-2008 |
| D_aniso target 各向异性比 | ≥2.5 (optimal = 3) | Drape test 悬垂试验 |
| Bonding strength 粘合强度 | ≥10 N/cm | Peel test, "strength vs flattening" key metric 关键平衡指标 |
| Cost target 成本目标 | ≤20% premium over C3 (Suzhou) | User-confirmed ceiling 用户确认上限 |
| Temperature control 温度控制 | Oven stable within ±1 °C (±2 °C across positions) | Calibrate 3 positions per run 每次试验前校准 |
| Standards applied 引用标准 | GB/T 8939 / 13662 / 13663 / 15593 (fluff) / 17297 (SAP); INDA 12.007 / 104.020; EDANA 801.1-02; ISO 4819 (MD/CD) / 11500 (tensile) / 12947 (absorption) / 15379 (safety) / 9001 | Sheet 6 第 6 表 |
| Trial material volumes 试料量 | 100 kg/month (Suzhou) + 200 kg/month (Fudi) | W3–W6 + W9–W11 |

> 🔴 **manual_review（2026-09-29）**：本资料含**试验预算与分配置月度材料成本估算（C1–C4 各约 ¥1.8–3.0 万/月，合计约 ¥11.5–15 万 [TBD]）**、**专利起草安排（关系式可能披露 IP，须先行起草）**与**内部人员姓名（审批人 / 第一发明人）**，属商务敏感信息与个人身份信息，依 AGENTS.md §5 **不页面化**——本页只登记"存在该估算与安排"这一事实，具体数字与姓名留存于原文。原文：`RAW/ima_sync/个人知识库/WKB/Projects/Liner/KC_Diffusion_Enhanced_Topsheet_v3.xlsx.md`

## Key claims 关键论断

- **Final pass/fail sits at the finished-diaper level, not the material level** —— 支撑页：[[ATB双梳理面层（Dual-Card Topsheet）]]、[[MD Liquid Distribution]]
- **The 126–130 °C window is the real design variable** (PE sheath flow vs trilobal flattening) —— 支撑页：[[热风粘合无纺布]]、[[三叶形截面纤维（Trilobal Fibre）]]
- **Cost is a first-class ranking dimension, not an afterthought** (≤20% premium over the Suzhou PET route) —— 支撑页：[[Diffusion-Enhanced Topsheet C1-C4 (Cost-Performance-Supply Chain)]]
- **Supplier maturity is a schedule risk**: the mono-PET spindle route is a new supplier with 4–6 week qualification —— 支撑页：[[Suzhou Yimeng (Mono-PET Spinner)]]、[[福地（Fudi）]]
- **Durable hydrophilic finish is a fixed factor, not a variable** in this DOE —— 支撑页：[[亲水整理耐久性]]

## Related pages 关联页面

- Concepts 概念：[[ATB双梳理面层（Dual-Card Topsheet）]]、[[三叶形截面纤维（Trilobal Fibre）]]、[[Shaped PET Add-On Window]]、[[MD Liquid Distribution]]、[[Pentagram PET (Star Cross-Section Fibre)]]、[[热风粘合无纺布]]、[[亲水整理耐久性]]
- Entities 实体：[[福地（Fudi）]]、[[Suzhou Yimeng (Mono-PET Spinner)]]、[[延江（Yanjan）]]、[[兰精集团]]
- Comparisons 对比：[[Diffusion-Enhanced Topsheet C1-C4 (Cost-Performance-Supply Chain)]]

## Original 原文

- Local path 本地路径：`RAW/ima_sync/个人知识库/WKB/Projects/Liner/KC_Diffusion_Enhanced_Topsheet_v3.xlsx.md`
- Original link 原文链接：（无；内部工作簿）

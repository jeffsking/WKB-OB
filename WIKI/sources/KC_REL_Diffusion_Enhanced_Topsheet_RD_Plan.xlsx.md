---
type: source
title: "KC_REL_Diffusion_Enhanced_Topsheet_RD_Plan.xlsx"
source_type: 研发计划
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/KC_REL_Diffusion_Enhanced_Topsheet_RD_Plan.xlsx.md
original_link: ""
date_published: 2026-08-14
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "REL ultra-thin core diffusion-enhanced topsheet plan: dual-card 25 gsm architecture (skin card + core-side diffusion card), anchor formula = 10% Lenzing Lyocell trilobal + 90% ES top, 50% Fudi ES + 50% base ES bottom (REL 超薄芯体双梳理扩散增强面层方案)"
  - "KPI gates: 1st STT <0.8 s, loaded rewet <0.03 g (0.5 kPa/5 min), enterprise diaper rewet <5.9 g, MD spread >=30% (target 34.9%), SAP utilization >=63%, wet tensile >=75 N/m, caliper loss <8%"
  - "PE sheath melts ~130 °C: over-temp rounds trilobal profile and loses surface-area benefit; Yanjiang oven Delta-T study (130/128/126 °C) required (PE 皮层过温会使三叶形截面圆化)"
  - "CoPET/PET blend option (30% CoPET / 70% PE) gives -24% 3rd-insult rewet and +17% core utilization but +16% price; caliper loss >=8% zeroes the rewet benefit"
  - "Enterprise low-load multi-insult protocol is PRIMARY judge; high-load short-interval protocol can mask true wearing performance (企业低载多次标准为一审门)"
pages_linked: ["[[ATB双梳理面层（Dual-Card Topsheet）]]", "[[福地（Fudi）]]", "[[兰精集团]]", "[[诺尔（Nuoer）]]", "[[Diffusion-Enhanced Topsheet C1-C4 (Cost-Performance-Supply Chain)]]", "[[CoPET（低熔点共聚酯）]]"]
---

# KC REL Diffusion-Enhanced Topsheet R&D Plan（REL 扩散增强面层研发计划）

## Positioning 定位

Full-English R&D plan workbook (Deliverable 1/2 foundation sheet, prepared 2026-08-14) for a **diffusion-enhanced topsheet（扩散增强面层：下渗快 + 面内扩散）** for the REL ultra-thin core diaper. It is the REL-track sibling of the Liner C1–C4 DOE plan — same dual-card architecture, different product target and KPI baseline. All assumptions are explicitly traced to meeting minutes 2026-08-13 and KB sources; [TBD] items require confirmation.（REL 超薄芯体配套的扩散增强面层六页规划：方案、DOE 矩阵、表征指标、排程、风险与预算。）

## Summary 摘要

Scope defines the layer as a functional topsheet-to-core interface layer responsible for fast acquisition（下渗）+ in-plane lateral distribution（面内扩散）; whether it replaces the current ADL or integrates topsheet+ADL is [TBD]. Architecture: dual-card system — skin-side card = 2D ES + optional 10% Lenzing Lyocell (trilobal) for softness/hydrophilicity; core-side card = profiled fiber + ES (50/50 Fudi ES anchor). Backup formula uses 3D Fudi trilobal ES top + 4D base ES bottom; cross-section (十字) PET fiber stays PENDING on skin-roughness reports. Key carried facts: PE sheath melts ~130 °C so oven Delta-T validation (130/128/126 °C at Yanjiang/沿江 line) is mandatory; profiled fiber loading capped ≤15% (launch zone 5–12%, 20% stress-only) to avoid fuzz/tensile loss/rewet; CoPET/PET option (-24% 3rd-insult rewet, +17% core util, +16% price) zeroed if caliper loss ≥8%; v11 simulation anchors SAP utilization 63.6% and MD spread 34.9%. DOE: Stage 1 = 2^(5-1) fractional factorial (16 runs + 3 centers) on X1 fiber type / X2 loading / X3 sheath / X4 Lyocell / X5 surface structure; Stage 2 = 2^3 full factorial; Stage 3 = control + top-2 on pilot line + diaper bench. 14-week back-planned schedule from QQV6 (end-Sep) to the Angela meeting (Nov); total budget ~¥157,575 (engineering estimate, excl. internal labor).（REL 版方案与 Liner 版同架构，新增 REL 基线 KPI 与沿江烘箱温度窗口验证。）

## Key Numbers & Conclusions 提炼的数字与结论

| 项目 Item | 数值 / 结论 Value | 备注 Notes |
|---|---|---|
| Total basis weight | 25 gsm (12.5 + 12.5) | [TBD] confirm |
| Profiled fiber loading | 10% primary; DOE 0/5/10/15/20%; cap ≤15% | launch zone 5–12% |
| 1st strike-through | <0.8 s（current ~0.9 s） | WSP 70.3 |
| Loaded rewet (0.5 kPa/5 min) | <0.03 g（current 0.04 g） | REL target |
| Enterprise diaper rewet | <5.9 g | low-load multi-insult, PRIMARY gate |
| MD spread / SAP utilization | ≥30%（sim 34.9%）/ ≥63%（sim 63.6%） | v11 ML+Xdiff |
| Wet tensile MD | ≥75 N/m（current 58 N/m） | ISO 9073-3 |
| Caliper loss | <8%（≥8% zeroes CoPET benefit） | [K2] |
| CoPET/PET blend | 30% CoPET / 70% PE：-24% 3rd-insult rewet，+17% core util，+16% price | optional under-layer |
| PE vs PET sheath | PE melts ~130 °C（profile-loss risk）；PET ~220 °C（bonding via ES only） | oven Delta-T 130/128/126 °C |
| Timeline anchors | QQV6 material validation ~end-Sep；Angela meeting Nov | 14-week back-plan |
| Budget total | ¥157,575（engineering estimate [TBD]，excl. labor） | pending procurement quotation |

> 🔴 **manual_review（2026-09-29）**：本表为内部工程估算预算（含专利撰写 4 万、沿江产线试车 5 万等分项），非采购报价；若需进入页面化商务口径请人工确认。原文留存于 `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/KC_REL_Diffusion_Enhanced_Topsheet_RD_Plan.xlsx.md`。

## Key Claims 关键论断

- **同一双梳理架构服务两条产品线（Liner C1–C4 与 REL 25 gsm），KPI 基线不同** —— 支撑页：[[Diffusion-Enhanced Topsheet C1-C4 (Cost-Performance-Supply Chain)]]、[[ATB双梳理面层（Dual-Card Topsheet）]]
- **温度窗口是异形纤维方案的第一工艺风险** —— 支撑页：[[ATB双梳理面层（Dual-Card Topsheet）]]
- **回渗门槛双轨制（材料级 0.03 g vs 成品级 5.9 g）须在 Kickoff 锁定一审门** —— 支撑页：[[Dryness Measure System（干爽度量三分）]]

## Linked Pages 关联页面

- 概念 Concepts：[[ATB双梳理面层（Dual-Card Topsheet）]]、[[CoPET（低熔点共聚酯）]]、[[Dryness Measure System（干爽度量三分）]]
- 实体 Entities：[[福地（Fudi）]]、[[兰精集团]]、[[诺尔（Nuoer）]]
- 对比 Comparisons：[[Diffusion-Enhanced Topsheet C1-C4 (Cost-Performance-Supply Chain)]]

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/KC_REL_Diffusion_Enhanced_Topsheet_RD_Plan.xlsx.md`
- 原文链接：（无；内部资料）
- 关系说明：Liner 版同族计划见 [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]]

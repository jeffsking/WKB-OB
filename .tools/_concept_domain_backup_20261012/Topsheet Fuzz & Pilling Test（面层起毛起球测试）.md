---
type: concept
title: "Topsheet Fuzz & Pilling Test（面层起毛起球测试）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-30
tags: [面层, topsheet, 起毛起球, fuzz, pilling, TTM-00609, 材料级筛选门, 待补]
---

# Topsheet Fuzz & Pilling Test（面层起毛起球测试）

> 📌 **Page completed 2026-09-30** from 4 citing sources（digest 命中 9 页含摘录）。All figures traced to their source pages. Anything not evidenced is marked `[待补]`。

## Definition 定义

定义待补（引用来源未给出明确定义）。

⚠️ **Scope caveat 口径提示**：the method text of the primary source [[TTM-00609 面层材料起毛起球测试.doc]] is **not present in this digest's excerpts**。The only content in the excerpts that directly concerns fuzz is its appearance as a **material-level screening gate** in the diffusion-enhanced-topsheet DOE acceptance system（源：[[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]]）；the test principle, specimen size, rating method and instrument are `[待补]`。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Fuzz gate（material-level screening）起毛验收门 | ≤2（no unit stated in source 原文未注单位） | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Same gate — STT 下渗时间 | ≤0.8 s | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Same gate — 3rd rewet 第 3 次回渗 | ≤0.5 g（target 0.30 g） | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Same gate — MD spread MD 铺展 | ≥34 %（vs 34.9 % anchor） | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Same gate — caliper retention 厚度保持 | ≥92 % | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Same gate — TS7 softness 柔软度 | ≥50 | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Same gate — D_aniso | ≥2.5 | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Same gate — bonding strength 粘合强度 | ≥10 N/cm | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| PRIMARY（finished-diaper）gate — rewet | <5.9 g @0.5 kPa，after 2 insults 双次冲击 | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Test web 受试网材 | 50 gsm dual-card air-through-bonded（ATB）= 25 gsm upper + 25 gsm lower；durable hydrophilic finish；**no increase in oven temperature** | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |

## Method / Mechanism 方法 / 机理

- **Two-tier acceptance 验收双档制**：PRIMARY = **finished-diaper enterprise standard**（rewet <5.9 g @0.5 kPa after 2 insults、core stain uniformity ≥A、SAP utilization ≥63 %、wet tensile ≥75 N/m）；the **material level is a screening gate only** — fuzz ≤2 belongs to the material-level tier（源：[[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]]）。
- **Test architecture 试验架构**：a 3-stage randomised DOE（seed 20260814）totalling 33 runs — Stage 1 configuration screen（4 configs × 3 temps × medium load = 12, plus 3 centre runs = 15）；Stage 2 temperature × loading optimisation on the top-2 configs（12 + 2 = 14）；Stage 3 confirmation（top-2 × 2 replicates = 4），plus 1 anchor run（C1 at 128 °C）。Schedule 14 weeks（W1–W14）from 2026-08-17, milestones M1–M7, 3 acceptance gates（源：[[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]]）。
- **Dual-track threshold 双轨门槛**：the REL topsheet R&D plan records a dual-track rewet threshold — **material level 0.03 g vs finished-product level 5.9 g** — to be locked at the Kickoff first review gate（源：[[KC_REL_Diffusion_Enhanced_Topsheet_RD_Plan.xlsx]]）。
- ⚠️ The "material level 0.03 g" and the "3rd rewet ≤0.5 g（target 0.30 g）" rows come from two different pages with different conventions — **this page does not merge-interpret them**；the standalone rating method of the fuzz & pilling test is `[待补]`。

## Hygiene Relevance 卫材关联

- Fuzz & pilling is a direct quality gate for skin-contact **feel and fibre shedding**，so it is placed in the material-level screening gate of the diffusion-enhanced topsheet, alongside softness（TS7 ≥50，源：[[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]]）。
- Process linkage：the ATB dual-card architecture and **no increase in oven temperature** are fixed factors（源：[[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]]）；a higher trilobal-fibre ratio improves in-plane distribution but makes the skin side feel harder, an upstream variable in the fuzz/feel trade-off（源：[[三叶形截面纤维（Trilobal Fibre）]]）。
- Related concepts（navigational；no fuzz figures in the digest）：[[ATB双梳理面层（Dual-Card Topsheet）]]、[[热风粘合无纺布]]、[[3D In-line Embossing Topsheet（3D 在线压花面层）]]、[[Dryness Measure System（干爽度量三分）]]、[[Nonwoven Deformation Force Test（无纺布形变力测试）]]。
- Method indexes 方法学上位表：[[Finished Product Testing Method Summary（成品测试方法汇总表）]]、[[Raw Material Testing Method Summary（原材料测试方法汇总表）]]。

## Open Questions 待补

- **Definition, specimen, rating method, instrument and tolerance of the topsheet fuzz & pilling test** —— `[待补]`（must be checked against [[TTM-00609 面层材料起毛起球测试.doc]]）。
- The unit of "fuzz"（whether it links to TS7 / a visual rating）is not given in the digest `[待补]`。
- Quantitative relation between fuzz & pilling and TS7 softness / topsheet free-fibre shedding `[待补]`。
- Whether this gate has entered the KC global STM/TTM method system, or remains a project-level screening convention `[待补]`。

## Related Sources 关联来源

- [[TTM-00609 面层材料起毛起球测试.doc]]
- [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]]
- [[KC_REL_Diffusion_Enhanced_Topsheet_RD_Plan.xlsx]]
- [[ATB双梳理面层（Dual-Card Topsheet）]]
- [[热风粘合无纺布]]
- [[3D In-line Embossing Topsheet（3D 在线压花面层）]]
- [[Dryness Measure System（干爽度量三分）]]
- [[Nonwoven Deformation Force Test（无纺布形变力测试）]]
- [[三叶形截面纤维（Trilobal Fibre）]]
- [[皮芯复合纤维]]
- [[GB-T 30133-2022 Topsheet for Disposable Sanitary Products（一次性卫生用品用面层）]]
- [[Finished Product Testing Method Summary（成品测试方法汇总表）]]
- [[Raw Material Testing Method Summary（原材料测试方法汇总表）]]

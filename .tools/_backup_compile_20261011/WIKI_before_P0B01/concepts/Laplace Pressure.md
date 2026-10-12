---
type: concept
title: "Laplace Pressure"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [concept, 毛细作用, capillary-pressure, young-laplace, rewet, surge-liner]
---

# Laplace Pressure
> 📌 **Page completed 2026-09-30** from 2 citing sources（另经 7 个库内页面交叉取证，见 Related Sources）。All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义
定义待补（引用来源未给出明确定义）。The vault does not state a standalone definition sentence; it consistently **uses the Young–Laplace relation as the operative form** of Laplace (capillary) pressure:

- **ΔP = −2γcosθ / R**（源：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]）
- Written with named symbols as **Δp = −2γcosθ / R**, where p = pressure, γ = surface tension, θ = contact angle, R = pore radius（源：[[Rewet Competitive Analysis - Depend vs Always Discreet Intake System（回渗竞品分析 · 2025-09-11）]]）
- The same relation is called the **capillarity** lever in the competitive program deck（源：[[2026-05-05 - QUINN.pptx]]）

## Key Parameters and Data 关键参数与数据
| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Young–Laplace equation 杨-拉普拉斯方程 | ΔP = −2γcosθ / R | [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]] |
| Symbol set 符号口径 | p 压力 / γ 表面张力 / θ 接触角 / R 孔隙半径 | [[Rewet Competitive Analysis - Depend vs Always Discreet Intake System（回渗竞品分析 · 2025-09-11）]] |
| Capillary pressure vs pore radius 毛细压与孔径 | p_c ∝ 1/r（孔径越大，毛细压越低） | [[Porous Structure and Liquid Flow Models]] |
| Flow vs pore radius 流速与孔径 | flow ∝ r²（Hagen–Poiseuille；孔径 ×2 → 流量 ×16） | [[Porous Structure and Liquid Flow Models]] |
| Zero capillary pull 毛细牵引为零 | θ ≥ 90° 时毛细牵引为零 | [[Computational Modeling in Absorbent Technology]] |
| Driving force 吸液驱动力 | capillary pressure 是主体吸液的驱动力；重力/外压为次要 | [[Porous Structure and Liquid Flow Models]]（p. 19） |

## Method / Mechanism 方法 / 机理
- **Two levers, one equation 两个杠杆同出一式**：residual fluid is held by **wettability (θ)** and **pore radius (R)** jointly — higher capillary pressure means the pore holds liquid harder, and higher desorption energy means fibres dry out less easily（源：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]）。So only two routes exist: **reduce wettability（raise θ）** or **enlarge R**（源：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]）。
- **Hydrophilisation and imposed pressure are substitutes 亲水化与外加压互为替代**：once θ ≥ 90° capillary pull is zero and only imposed pressure breaks the deadlock; conversely a hydrophilic surface buys back penetration at zero pressure（源：[[Computational Modeling in Absorbent Technology]]）。
- **Rate–capacity antagonism 速率-容量对抗**：bigger pores raise flow (∝ r²) but lower capillary pressure (∝ 1/r), so the optimum sits mid-range, not at either extreme（源：[[Porous Structure and Liquid Flow Models]]）。
- **Monotonic parameter mapping 参数单调映射**：pore radius, depth, contact angle, viscosity and external pressure each map monotonically onto penetration time, so the space can be scanned by model before spinning a pilot line（源：[[Computational Modeling in Absorbent Technology]]）。
- **Quantification route 量化路径**：representative capillary pressure is read at half-saturation, and desorption energy is the area under the height–saturation curve; lower desorption energy → fibres dry out easier（源：[[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]）。

## Hygiene Relevance 卫材关联
- **The rewet–leak trade is a θ conflict 干爽与漏液的 θ 冲突**：removing the liner's wettability treatment did lower rewet (0.26 → 0.20 g) but pushed leakage from 3.2% to 4.6%, because a non-hydrophilic liner cannot stop surge flow — so the same change must be accepted **pairwise (干 + 漏)**（源：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]）。
- **Enlarging pores is the safer route 加大孔径相对安全**：coarse-fibre, large-pore liners are flagged as safe on the R route; wettability changes differ by category (an untreated liner was feasible in BCC but not in adult care)（源：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]）。
- **Competitive framing 竞品对标**：K-C lags Always Discreet on rewet and AD runs a "40% DRIER" claim (160 mL loading, 50 s wait), with capillarity (Young–Laplace) named as the engineering lever to close the gap（源：[[2026-05-05 - QUINN.pptx]]）。
- **LPR vs HPR attribution 低压/高压回渗归因**：LPR is attributed to liner wettability + surge pore-size distribution, while HPR is attributed to SAM amount/location（源：[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]）。

## Open Questions 待补
- `定义待补`：本页仅登记公式形式与用法；形式化定义需回 [[Surface Tension and Surface Energy]] 原文核对。
- 符号与量纲口径（γ 单位、R 定义：孔径 vs 孔喉半径）未在摘录中出现 `[待补]`。
- 毛细压的绝对值口径与测量方法（解吸支 vs 吸收支）需回 [[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]] 原文核对 `[待补]`。

## Related Sources 关联来源
- [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]] — Young-Laplace 式与残液两出口条件
- [[Computational Modeling in Absorbent Technology]] — 参数单调映射、θ ≥ 90° 死锁
- [[Porous Structure and Liquid Flow Models]] — 毛细压为驱动力（p. 19）、p_c ∝ 1/r、flow ∝ r²
- [[Rewet Competitive Analysis - Depend vs Always Discreet Intake System（回渗竞品分析 · 2025-09-11）]] — Δp = −2γcosθ/R 符号口径
- [[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]] — 代表毛细压、解吸能量
- [[2026-05-05 - QUINN.pptx]] — capillarity 作为工程杠杆
- [[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]] — 分档归因

> 注：digest 中 [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]（Laplace 变换）与 [[Mechanochromic Materials Technical Review（EN v3, 2026-08）]]（工业测压材料阈值）为关键词误命中，与本概念无关，未采信。

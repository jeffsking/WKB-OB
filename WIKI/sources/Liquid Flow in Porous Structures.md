---
type: source
title: "Liquid Flow in Porous Structures"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Absorbent Technology (Chatterjee & Gupta)/chapters/Absorbent Technology_ch01_report.md.md
original_link: ""
date_published: 2002
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
author: "Pronoy K. Chatterjee & Bhupender S. Gupta"
edition: "revised & expanded (from 1985 Absorbency)"
publisher: "Elsevier (Academic Press)"
year: 2002
isbn: ""
original_language: "EN"
parent_book: "[[Absorbent Technology]]"
key_claims:
  - "Capillary pressure is the primary driving force for absorption; gravity/pressure are secondary."
  - "Liquid transport in absorbent media is unsteady-state flow mathematically analogous to diffusion (x_v ∝ t^(1/2), Washburn-type)."
  - "Pore size governs absorption RATE while pore volume governs absorption CAPACITY — the central design tradeoff."
  - "Lower fiber density (e.g. cellulose ~1.5 g/cc) yields higher specific pore volume and capacity at equal basis weight."
pages_linked: ["[[Absorbent Technology]]", "[[SAP（高吸水树脂）]]", "[[吸收芯体]]", "[[毛细压力 Capillary Pressure]]", "[[达西定律 Darcy's Law]]", "[[孔隙率 Porosity]]", "[[绒毛浆（Fluff Pulp）]]"]
status: merged
---

> 🔴 **治理合并（2026-09-30）**：Absorbent Technology 同章 IMA 重同步双编译。已并入：
> 入链已全量改写；本页保留为**指针页**（未删除，原文存档于下方）。

本主题正文见：
- [[Porous Structure and Liquid Flow Models]]


---

## 📦 原始内容存档（合并前，2026-09-30）

# Liquid Flow in Porous Structures

## One-line Position 一句话定位

Chapter I establishes the physical foundation of absorbent technology — capillary-driven, unsteady-state liquid flow in porous media — providing the mathematical tools (Darcy, Washburn, diffusivity factor) that govern wicking rate and capacity in diaper/incontinence cores.

本章是整书的物理基石，建立了多孔介质中毛细压力驱动、非稳态液体流动的统一理论框架，为芯体的吸收速率与容量设计提供方法论根底。

## Summary 摘要

- Absorption is driven primarily by **capillary pressure** (p_c = 2γcosθ/r); externally imposed gravity or pressure plays only a secondary role (p. 19).
- Flow in porous media follows **Darcy's law** (q = -K·∇P, K = k/μ) and, under unsteady conditions, is mathematically identical to a diffusion process; the advancing wicking front distance obeys **x_v ∝ t^(1/2)** (Washburn / Rudd relation, p. 24, 37).
- The **diffusivity factor** F(s) = (k/μΦ)(dp_c/ds) links permeability and capillary gradient; a constant F gives the error-function solution s = 1 − erf(x/√(4F₁t)) (Eq. 23, 25).
- **Pore structure** is modeled geometrically: three fibers form an equilateral-triangle capillary; pore size Y is computable from fiber diameter, linear density, packing fraction and binder volume; **Kozeny–Carman** k = Φ³/[k″S₀²(1-Φ)²] (k″≈5) estimates permeability (p. 33).
- **Fiber density** sets capacity: specific air volume Vs = (1/φ)(1/ρ_f − 1); low-density cellulose (~1.5 g/cc) beats polyolefin (~0.92 g/cc) on capacity when wettability is equivalent (p. 53–54). The authors pose the next-gen challenge: "materials that have the densities of polyolefins but the hydrophilicities of celluloses."
- **SAP swelling** is a diffusion process spanning Fickian (V ∝ t^(1/2)) to Case II (V ∝ t, sharp front); real gels follow mixed V = K₁t^(1/2) + K₂t (Eq. 38, p. 49). Equilibrium swell is controlled by cross-link density ↑ (↓swell), ionization ↑ (↑swell), ionic strength ↑ (↓swell) — directly relevant to urine (high ionic strength) capacity loss.

## Key Numbers & Conclusions 提炼数字与结论

| 项目 | 数值/结论 | 备注 |
|---|---|---|
| 浸润前沿规律 Wicking front | x_v ∝ t^(1/2) | Washburn/Rudd; 吸收速率随时间衰减，需固定测试时间窗 |
| 典型扩散率 F₁ | 0.20 cm²/s | paper-like material; L₀ = 20 cm 下饱和曲线演化 (p. 37) |
| 纤维堆积分数 Packing fraction φ | 0.025–0.10 (2.5%–10%) | Gupta 实测，取决于材料/克重/粘合法 (p. 53) |
| 纤维素密度 Cellulose ρ_f | ~1.5 g/cc | 同克重下较聚烯烃提供更高孔隙体积 |
| 聚烯烃密度 Polyolefin ρ_f | ~0.92 g/cc | 密度低但亲水性差，毛细压力几乎不启动 |
| Kozeny–Carman 常数 k″ | ≈5 | k = Φ³/[k″S₀²(1-Φ)²] |
| Darcy 适用临界雷诺数 Re_crit | 0.1–75 | Scheidegger; 突发大流量可能超达西范围 (p. 35) |
| 最大吸收容量 C | C = ρ_L·Φ/[ρ·(1-Φ)] | 干态单位质量吸液量 (Eq. 10, p. 30) |

## Key Claims 关键论断

- Absorption rate and capacity are decoupled structural parameters: **pore size controls rate (∝ r² via Hagen–Poiseuille), pore volume controls capacity** — optimizing one penalizes the other, requiring mid-range optimization (gel-blocking avoided by balanced design).
- The **1/2-power law** is the physical basis for fixed-time-window absorbency testing (e.g. 60 s uptake), not equilibrium measurement — early uptake dominates total.
- **Liquid redistribution** in finite cores (small pores fill first, large pores drain later) justifies an acquisition layer (large pores, fast spread) over a storage layer (small pores, high capacity).

## Related Pages 关联页面

- 父书 Parent book：[[Absorbent Technology]]
- 概念 Concepts：[[SAP（高吸水树脂）]]、[[吸收芯体]]、[[ADL（导流层）]]、[[毛细压力 Capillary Pressure]]、[[达西定律 Darcy's Law]]、[[孔隙率 Porosity]]、[[绒毛浆（Fluff Pulp）]]、[[回渗 Rewet]]

## Source 原文

- 本地路径 Local path：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Absorbent Technology (Chatterjee & Gupta)/chapters/Absorbent Technology_ch01_report.md.md`
- 原文链接 Original link：

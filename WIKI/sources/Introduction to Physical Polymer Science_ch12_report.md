---
type: source
title: "Introduction to Physical Polymer Science_ch12_report.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch12_report.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
key_claims: []
pages_linked: []
compile_mode: extractive
---

# Introduction to Physical Polymer Science_ch12_report.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch12_report.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# Introduction to Physical Polymer Science_ch12_report.md.md

# SPERLING Ch12 深度拆解报告

## Polymer Surfaces and Interfaces

来源：L. H. Sperling, Introduction to Physical Polymer Science, 4th Ed., Wiley 2006, Chapter 12 (pp. 614–680，约 3068 行)
工作目录：/sandbox/workspace/Ebook_Extract/SPERLING/chapters/SPERLING_ch12.txt

## 模块1：Core Arguments（核心论点，英文 + 行号）

Surface and interface science is an interdisciplinary, still-developing field that unifies thermodynamics, spectroscopy, microscopy, and mechanics.
> "It is the hope of the author that you, the student, will discover yet unknown applications. … interface science is just beginning, and far from mature." (lines 2640–2708)

Polymer surfaces are thermodynamically distinct from the bulk: surface tension (γ) is the reversible work per unit area to create a new surface, and it is temperature- and molecular-weight-dependent.
> "The surface tension is the reversible work needed to create a unit surface area in a substance." (line 62); γ(T) follows γ = c₁ + c₂T + c₃T² (line 142), and γ(Mₙ) = γ∞ − k/Mₙ (line 147).

Interfacial properties between two polymers depend on the Flory–Huggins χ parameter, not directly on molecular weight, provided Mₙ is high enough for chain-end effects to be negligible.
> "Numerically the values of the interfacial tension, γ_ab, are significantly smaller than the values of any of these polymers facing air." (lines 195–196); γ_ab = √(χ/6) · ρ₀ · b · kT (line 963); σ_th = 2b/√(6χ) (line 970).

Spreading, wetting, and adhesion are governed by the balance of three surface tensions, formalized by Young's equation and the spreading coefficient S_b/a.
> "A balance of the three relations leads to Young's equation" (line 287): γ_SV = γ_SL + γ_LV cos θ (line 290); S_b/a = γ_a − γ_b − γ_ab (line 225).

Real adhesion is the sum of several bonding mechanisms (mechanical, specific, primary chemical, interpenetration, van der Waals), and is quantitatively bounded by the work of adhesion W_a, which is orders of magnitude smaller than the true fracture energy G_Ic.
> "Wa values shown in Table 12.2 are some 500 times smaller than the interfacial fracture energy, G_Ic." (lines 998–1020); acid-base contribution W_AB = − f n_AB ΔH (line 2375).

## 模块2：Key Concepts with Operational Definitions

|||||
|---|---|---|---|
|1|Surface free energy (表面自由能)|Reversible work per unit area to create a new surface; thermodynamically equal to the surface tension γ at constant T, P: G⁰s = (∂G/∂A)_{T,P} = γ (Eq. 12.3). Units: erg/cm² (= J/m²).|lines 62–84, 109–113|
|2|Contact angle (接触角, θ)|Angle at the three-phase (S/L/V) contact point between a sessile drop and the solid. Determined by the balance of γ_SV, γ_SL, γ_LV; θ = 0° → complete wetting, θ → 180° → non-wetting.|lines 280–290, 378–401|
|3|Wetting (润湿)|Spontaneous spreading of a liquid over a solid when the spreading coefficient S ≥ 0 (equivalently γ_SV ≥ γ_SL + γ_LV). Quantified by cos θ via Young's equation.|lines 278, 287–290|
|4|Young's equation (Young 方程)|γ_SV = γ_SL + γ_LV cos θ (Eq. 12.16). Holds at equilibrium for a smooth, homogeneous, rigid solid with a saturated vapor.|lines 287–290|
|5|Surface energy components – dispersion & polar (色散/极性分量)|γ is decomposed into non-polar (dispersion, γ^d) and polar (γ^p) contributions; the Fowkes / Owens–Wendt formalism separates the two so that γ_AB ≈ √(γ_A^d γ_B^d) + √(γ_A^p γ_B^p). Acid–base Drago constants E, C (electrostatic vs covalent) provide a related decomposition.|lines 992–1000, 2291–2335|
|6|Work of adhesion (粘附功, W_a)|Reversible work per unit area to separate two condensed phases from equilibrium contact to infinity: W_a = γ_a + γ_b − γ_ab (Eq. 12.20). It is a lower bound because chain scission and pull-out are ignored.|lines 992–1000|
|7|Spreading coefficient (铺展系数, S_b/a)|Free-energy change per unit area when liquid b spreads on liquid a: S_b/a = γ_a − γ_b − γ_ab (Eq. 12.11). S > 0 → spontaneous spreading; S < 0 → beading.|lines 209–235|
|8|Surface modification (表面改性)|Deliberate alteration of surface energy/chemistry via corona discharge, plasma, flame, fluorination, coating, or grafting without changing bulk. Enables bondability or hydrophilicity.|lines 2278–2287|
|9|Interfacial diffusion (界面扩散)|Mutual penetration of polymer chains across an immiscible interface. Interphase thickness σ_th ∝ 1/√χ (Eq. 12.18); short-time chain interdiffusion goes as t^{1/4} (lines 741–747). Requires T > T_g and sufficient entanglement density for high fracture energy.|lines 939–982, 1058–1060, 741–747|
|10|Interphase thickness σ_th (界面相厚度)|σ_th = 2b / √(6χ) (Eq. 12.18). For PS/PMMA at 135 °C: σ_th ≈ 27 Å. Mechanical strength requires ~8 entanglements per chain at the interface.|lines 969–982, 1041–1060|
|11|Dahlquist criterion ( Dahlquist 准则 )|For a pressure-sensitive adhesive (PSA), the dynamic shear modulus at 1 s must be < 3 × 10⁶ dyn/cm²; tack peaks at T − T_g = 40–70 °C.|lines 2272–2275|
|12|Drago constants (Drago 常数, E, C)|−ΔH = E_A E_B + C_A C_B (Eq. 12.42); E = electrostatic (Lewis acid-base), C = covalent contribution. For PMMA: E_B = 1.25, C_B = 0.508 (kcal/mol)^{1/2}.|lines 2298–2415|

## 模块3：Evidence Tables

### 表 1 典型聚合物表面能数据（Table 12.1）

*Source: S. Wu, Polymer Interface and Adhesion, Dekker 1982 (line 105). All values in erg/cm².*

|||||||
|---|---|---|---|---|---|
|Polyethylene (PE)|35.7|28.8|0.057|低极性|γ^d ≈ 33.0，γ^p ≈ 0|
|Polypropylene (PP) (not listed, literature)|~31|—|—|低极性|γ^d ≈ 30.6，γ^p ≈ 0.3|
|Poly(dimethyl siloxane, PDMS)|19.8|14.0|0.048|极低|γ^d ≈ 22.0，γ^p ≈ 0|
|Polytetrafluoroethylene (PTFE)|23.9|16.9|0.058|极低|γ^d ≈ 18.4，γ^p ≈ 1.5|
|Polystyrene (PS)|40.7|32.1|0.072|弱极性|γ^d ≈ 32.0，γ^p ≈ 3.3|
|PMMA|41.1|32.0|0.076|极性（酯基）|γ^d ≈ 38.7，γ^p ≈ 18.4|
|Poly(ethylene oxide, PEO)|42.9|33.8|0.076|强极性（醚）|γ^d ≈ 29.2，γ^p ≈ 20.6|
|Polycarbonate (PC)|49.2|35.1|0.060|中等极性|γ^d ≈ 38.6，γ^p ≈ 12.5|
|Poly(ethylene terephthalate, PET)|44.6|28.3|0.065|中等极性|γ^d ≈ 42.0，γ^p ≈ 6.7|
|Polychloroprene (CR)|43.6|33.2|0.086|中等极性|γ^d ≈ 30.0，γ^p ≈ 6.7|

关键判读：
- 所有聚合物 γ 均 < 水 (

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch12_report.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch12_report.md.md`
---
type: source
title: "Smart Polymers Ch11 Smart Polymer Drug Delivery"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Smart_Polymers_Biotech_Biomed/chapters/SmartPolymers_Ch11_深度拆解.md.md"
date_published: 2008
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Intelligent or smart polymers are biocompatible polymeric materials that respond to the physiological or biological environment by expanding or contracting at different rates; hydrogels — three-dimensional hydrophilic networks able to imbibe large amounts of water or biological fluids — are described as the simplest carriers used as intelligent systems (lines 28–37)."
  - "Swelling ratio changes drastically as a function of pH, ionic strength, temperature and electromagnetic radiation (lines 67–69); network structure is quantified by three parameters — polymer volume fraction in the swollen state υ2,s, molecular weight between cross-links Mc, and mesh size ξ — via Flory–Rehner equilibrium swelling and rubber elasticity theory (lines 93–272)."
  - "Controlled release falls into three classes set by the rate-limiting step: diffusion-controlled (reservoir, zero-order; matrix, Mt/M∞ ∝ t^1/2), chemically controlled (erosion or pendant-chain cleavage), and swelling-controlled (glassy–rubbery moving front; Ritger–Peppas Mt/M∞ = k·t^n) (lines 769–791, 956–1147)."
  - "PNIPAAm collapses at about 32 °C while PMAA is virtually temperature-independent but pH-dependent; P(NIPAAm-co-MAA) copolymers combine both, and macromolecular actives such as streptokinase are released only once the mesh size expands past a critical value (lines 386–394, 1008–1013)."
  - "Water diffusion time scales with the square of the specimen's characteristic length (t_diff ∝ L²) (lines 552–553), and effective diffusivity in porous media follows D_eff = D_iw·(ε/τ)·K_p·K_r (Table 11.1, Eq. 11.19)."
  - "Interpolymer complexes are reversible and environment-tunable; the critical PEG molecular weight required for complexation is 2000 g/mol for PMAA and 6000 g/mol for PAA, with PMAA gel collapse below 5 wt% PEG and re-swelling at about 5–10 wt% (lines 1237–1247, 1318–1321)."
summary_cn: "第11章建立智能水凝胶定量结构-性能-释放框架：Mc/ξ/υ₂,ₛ 三个网络参数、Flory–Rehner 与橡胶弹性理论、三类释放机制（扩散/化学/溶胀控制），并以 P(NIPAAm-co-MAA) 双响应与可逆聚合物间复合为例。"
tags: ["source/book", "smart-polymers", "hydrogel", "drug-delivery", "mesh-size", "Flory-Rehner", "diffusion", "PNIPAAm", "stimuli-responsive", "controlled-release"]
tags_zh: ["源/书籍", "智能聚合物", "水凝胶", "控释", "网孔尺寸", "扩散", "复合物"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Smart Polymers Ch01 Phase Transitions and Light Scattering]]", "[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]", "[[Smart Polymers Ch10 Boronate Copolymers and Gels]]", "[[Smart Polymers Ch12 Polymeric Carriers Regional Therapy]]", "[[Smart Polymers Ch13 Affinity Precipitation of Proteins]]", "[[Smart Polymers Ch14 Hydrogels in Microfluidics]]", "[[Hydrogel-based Superabsorbent Polymers]]", "[[Acrylic-Based Superabsorbent Polymers]]"]
---

# Smart Polymers Ch11 Smart Polymer Drug Delivery

> Source: Smart Polymers — Applications in Biotechnology and Biomedicine, 2nd ed. (CRC Press, **2008**), Ch.11 — *Drug Delivery Using Smart Polymers: Recent Advances* (Nicholas A. Peppas; chapter body L1–L1462).

## Scope 范围

Chapter 11 moves from "smart materials that respond" to **quantitative structure–property–release modelling**. It supplies the canonical toolbox for any cross-linked hydrophilic network — including SAP: network characterization (Mc, ξ, υ₂,ₛ), equilibrium swelling (Flory–Rehner 平衡溶胀), diffusivity in porous media, and the three release-mechanism classes. Its own framing: "Intelligent or smart polymers are biocompatible polymeric materials that can respond to the physiological or biological environment by expanding or contracting at different rates" (L28–30).

## Network Structure Parameters 网络结构三参数

| Parameter 参数 | Definition 定义 | Source |
|---|---|---|
| υ₂,ₛ (polymer volume fraction in swollen state 溶胀态聚合物体积分数) | A measure of the amount of biological fluid imbibed by the hydrogel | L109–113 |
| Mc (molecular weight between cross-links 交联点间分子量) | Mass of chain segment between two consecutive cross-links; a direct measure of cross-linking degree. Only **average** values can be calculated because polymerization is random | L110–118 |
| ξ (mesh size / correlation length 网孔尺寸) | Linear distance between two adjacent cross-links — the space available for drug diffusion. ξ = υ₂,ₛ^(−2/3)·(2C_n·Mc/M_r)^(1/2)·l | L119–121, L320–375 |

**Flory–Rehner equilibrium swelling** (Flory–Rehner 平衡溶胀理论): an immersed equilibrium gel is subject to only two opposing forces — "the thermodynamic force of mixing and the retractive force of the polymer chains" (L126–134), giving ΔG_total = ΔG_elastic + ΔG_mixing. Mc relations appear as Eq. 11.3 (neutral network prepared without solvent, L173–181) and Eq. 11.4 (with the relaxed volume fraction υ₂,ᵣ, L190–202). Ionic networks add a ΔG_ionic term.

**Rubber elasticity theory** (橡胶弹性理论) recovers the equilibrium modulus and, via tensile testing, backs out Mc: τ = (ρRT/Mc)(1 − 2Mc/Mn)(α − α⁻²)(υ₂,ₛ/υ₂,ᵣ)^(1/3) (L276–307).

**Pore classification** used by the author: "Depending upon the size of these pores, hydrogels can be conveniently classified as macroporous, microporous, or nonporous" (L319–320). Mesh size of P(NIPAAm-co-MAA) spans roughly 0–150 Å as a function of temperature and pH (Figure 11.4, L526–530).

## Release Mechanism Classes 释放机制分类

Source: §11.3.2–11.3.5 (L769–1179).

| Class 类别 | Rate-limiting step 限速步骤 | Behaviour 行为 | Source |
|---|---|---|---|
| Diffusion-controlled — reservoir 储库型 | Membrane transport | Drug core behind a polymer membrane; release rate **independent of time (zero-order)** | L956–990 |
| Diffusion-controlled — matrix 基质型 | Network diffusion | Drug dissolved/dispersed in the network; Mt/M∞ ∝ t^1/2 | L998–1004 |
| Chemically controlled — erodible 可侵蚀型 | Degradation/dissolution | Hydrophilic → homogeneous erosion; hydrophobic → heterogeneous (surface) erosion; surface erosion gives near zero-order | L1016–1086 |
| Chemically controlled — pendant-chain 悬挂链型 | Bond cleavage | Drug tethered via hydrolytically/enzymatically labile bonds | L1016–1070 |
| Swelling-controlled 溶胀控制型 | Glassy→rubbery moving front | Inner glassy phase + outer swollen rubbery phase; drug exits only from the rubbery region; macromolecular relaxation matters | L1133–1179 |

Fick's law underlies transport throughout: j_i = −D_ip·dc_i/dx and ∂c_i/∂t = D_ip·∂²c_i/∂x² (Eqs. 11.15–11.16, L796–812). The **Ritger–Peppas** diagnostic Mt/M∞ = k·t^n applies to the first ~60% of release, with n the diffusional exponent separating Fickian from relaxation-controlled behaviour (L1149–1169).

Key quote for the moving front: "the polymer matrix begins to swell, and two distinct phases can be observed … an inner glassy phase and a swollen rubbery phase. Drug molecules are able to diffuse out of the rubbery phase … no drug diffuses out of the glassy region" (L1137–1143).

## Diffusivity vs Structure 扩散系数与结构关系

Source: Table 11.1, L849–925. Variables: ε porosity, τ tortuosity, K_p partition coefficient, K_r constriction factor, Mc the critical molecular weight between cross-links below which a drug of radius r_s cannot diffuse.

| Regime | Eq. | Relation 关系式 |
|---|---|---|
| Porous | 11.18 | D_ip = λ²v / 6 (Eyring jump model; λ = jump length, v = jump frequency) |
| Porous | 11.19 | D_eff = D_iw · (ε/τ) · K_p · K_r |
| Microporous | 11.20 | D_ip/D_b = (1 − λ)²(1 + αλ + βλ³ + γλ⁵) (Faxén; λ = r_s/r_p) |
| Nonporous | 11.21 | D_ip = D₀·exp(−k/v_f) (Fujita free-volume) |
| Nonporous | 11.22 | D₂,₁,₃/D₂,₁ = φ(q_s)·exp[−B(q_s/V_f,1)(1/H − 1)] |
| Nonporous, highly swollen | 11.23 | D₂,₁,₃/D₂,₁ = k₁·[(M − Mc)/(Mc − Mc)]·exp[−k₂·(r_s²/(Q − 1))] |

**Scaling law for geometry:** "the characteristic water diffusion time is proportional to the square of the specimen's characteristic length" — t_diff ∝ L² (L552–553).

## Responsiveness Data 响应性数据

| Polymer | Temperature response 温度响应 | pH response | Source |
|---|---|---|---|
| PNIPAAm (homopolymer) | Collapses at ≈ 32 °C | ~independent over the studied range | L386–390, L415–418 |
| PMAA (homopolymer) | Virtually temperature-independent | Swells with increasing pH | L386–390, L455–458 |
| P(NIPAAm-co-MAA) | Synergistic with pH; T_g-dependent | Synergistic with T; raising pH 5 → 7.4 increases swelling | Tunable by composition (100% → 0% NIPAAm) (L391–394, L487–492, L533–538) |

**Mesh-size gating (网孔门控).** "The release of an incorporated enzyme, streptokinase … is possible only when the mesh size attains a certain value that will allow the relatively large-molecular-weight enzyme to be released" (L1008–1013). 中文：只有网孔涨到足够大，大分子活性物才放得出来——这是"按需触发释放"的设计原型。

**Interpolymer complexes (聚合物间复合物)** are classified by secondary binding force:

| Type | Force 作用力 | Example | Source |
|---|---|---|---|
| Polyelectrolyte complex | Coulomb | Two oppositely charged polyelectrolytes | L1198–1203 |
| Hydrogen-bonding complex | H-bond | Lewis acid (proton donor) + Lewis base (proton acceptor) macromolecules | L1199–1206 |
| Stereocomplex | van der Waals | isotactic + syndiotactic PMMA | L1200–1208 |
| Charge-transfer complex | Electron donor/acceptor | Electron-accepting + electron-donating polymers | L1201–1221 |

Experimentally: PEG critical MW for complexation = **2000 g/mol (PMAA)** and **6000 g/mol (PAA)** (L1237–1247); a PMAA gel collapses at PEG < 5 wt% and re-swells at ≈5–10 wt% (L1318–1321); FT-IR shows the PMAA dimer band at 1700 cm⁻¹ shifting to 1733 cm⁻¹ in the PMAA–PEG complex (L1309–1312).

## Hygiene implication 卫材关联

This chapter is **one of the most transferable in the book** for SAP and absorbent-core work, because it treats exactly the same cross-linked hydrophilic network:

1. **SAP design as a mesh-size problem.** ξ = υ₂,ₛ^(−2/3)(2C_n·Mc/M_r)^(1/2)·l and Mc from Flory–Rehner are the proper language for the free-swell vs. gel-strength trade-off: lower Mc ⇒ tighter network, higher modulus, slower uptake. Map ξ against fluid-uptake rate to select SAP grade per layer (acquisition vs. anti-gel-blocking).
2. **Acquisition/distribution nonwovens.** D_eff = D_iw·(ε/τ)·K_p·K_r makes porosity ε and tortuosity τ explicit process levers for fiber denier, basis weight and calendering.
3. **Core geometry scaling.** t_diff ∝ L² predicts how core thickness and SAP layer geometry move acquisition time; use it with the matrix law Mt/M∞ ∝ t^1/2 to bound transient behaviour.
4. **Dual pH/temperature cues in-product.** PNIPAAm collapses near 32 °C and PMAA responds to pH, so P(NIPAAm-co-MAA)-type layers can act as wetness indicators or, for adult incontinence, flag pH/fever shifts; the mesh-gating principle converts those cues into triggered release of skin-care actives. Relevant to the owner's chromic/colour-change indicator work only through the **swelling-to-optical** route — the chapter contains no chromic-moiety chemistry.
5. **Reversible absorbency for smart packaging.** Critical PEG MW thresholds (2000/6000) and the collapse/re-swell window (< 5 wt% vs 5–10 wt%) are quantitative switch points for a reversibly switched wrapper.
6. **Skin-friendly adhesives.** PEG "stealth" behaviour (L83–88) and carboxyl/hydroxyl hydrogen-bonding mucoadhesion (L76–79) support low-irritation wet-tack coating design.

Caution: every quantitative figure above comes from drug-release experiments in buffer/media, not from urine or hygiene-product testing. Direct translation to product performance is unsupported — treat values as design anchors only. 中文：所有数据来自药物释放实验，请勿直接等同产品质量指标。

## Data Integrity Notes 数据完整性说明

- Edition year 2008 (CRC Press) is stated explicitly in the source header → `date_published: 2008`.
- All claims cite source line numbers L1–L1462; printed page numbers are unavailable — [待验证].
- Prior-/next-chapter cross-references are absent from this extraction; the source itself flags [未找到原句/行号缺失]. The reference list mentions Brannon-Peppas & Harland, *Absorbent Polymer Technology* (refs 2, 20), indicating topical linkage to superabsorbent swelling without citable line-level content here.
- One tabulated entry for highly swollen networks (Eq. 11.23) reproduces the source's own typographically ambiguous term `(Mc − Mc)` verbatim rather than guessing a correction.

## Related Sources 关联来源

- [[Smart Polymers Ch01 Phase Transitions and Light Scattering]] — same nonergodic hydrogel systems, characterized by light scattering rather than release modelling.
- [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] — the surface-grafted counterpart of the same networks.
- [[Smart Polymers Ch10 Boronate Copolymers and Gels]] — alternative recognition-driven cross-linking for the same gel platform.
- [[Smart Polymers Ch12 Polymeric Carriers Regional Therapy]]
- [[Smart Polymers Ch13 Affinity Precipitation of Proteins]]
- [[Smart Polymers Ch14 Hydrogels in Microfluidics]]
- [[Hydrogel-based Superabsorbent Polymers]]
- [[Acrylic-Based Superabsorbent Polymers]]

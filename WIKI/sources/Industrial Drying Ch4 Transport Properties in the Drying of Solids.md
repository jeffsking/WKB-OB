---
type: source
title: "Industrial Drying Ch4 Transport Properties in the Drying of Solids"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch04.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Effective moisture diffusivity is defined from Fick's second law by combining molecular diffusion, capillary flow, Knudsen flow, hydrodynamic flow and surface diffusion into one coefficient (Eq. 4.1, p.81)."
  - "Which property must be accurate depends on the controlling resistance: internal control when Biot number > 1 (Eq. 4.4 context), external control when Bi < 0.1 (Eqs 4.5–4.6) (p.81–82, 88–89, 94)."
  - "Temperature dependence of diffusivity generally follows Arrhenius D = D₀ exp(−E/RT) (Eq. 4.2), but for less hydrophilic polymers (polymethacrylates, polyacrylates) 'the moisture diffusivity decreases with increasing water content', and for some hydrophobic polyolefins it is concentration-independent (p.85–86)."
  - "'the desorption isotherm is the curve to use for the process of drying' (p.100); GAB is 'probably the most suitable for process analysis and design of drying' over 0.1 < a_w < 0.9 (p.102)."
  - "For diffusion-controlled slabs the drying constant collapses to K = π²D/L² (Eq. 4.15, p.99); the drying constant 'embodies all the transport properties into a simple exponential function' (p.98–99)."
  - "All transport properties (D, k, h_h, h_M) can be estimated simultaneously from one drying experiment by regression of a coupled process model (Eqs 4.16–4.23, §4.7, p.103–106)."
summary_cn: "按性质逐项给出干燥模型的六大传输/热力学参数（有效扩散系数、导热系数、边界传热传质系数、干燥常数、平衡水分）的定义、测量方法、文献数据与估算途径。"
tags: ["source/book", "drying/transport-properties", "drying/diffusivity", "drying/sorption-isotherm", "materials/cellulose", "materials/sap"]
tags_zh: ["来源/书籍", "干燥/传递性质", "干燥/扩散系数", "干燥/吸附等温线", "材料/纤维素", "材料/SAP"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch2 Experimental Techniques in Drying]]", "[[Industrial Drying Ch3 Basic Process Calculations and Simulations in Drying]]", "[[Industrial Drying Ch33 Drying of Fibrous Materials]]", "[[Industrial Drying Ch41 Drying of Polymers]]"]
---

# Chapter 4 — Transport Properties in the Drying of Solids

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.4, pp.79–113. (Authors: Dimitris Marinos-Kouris & Z.B. Maroulis)

## Overview 概述

Chapter 4 sits at the property layer of the drying knowledge stack: Ch.1 selects the dryer, Ch.2 measures moisture/isotherms, Ch.3 writes the balances — Ch.4 supplies the coefficients those balances consume. Organized strictly per-property (Definition → Experimental method → Data compilation → Factors affecting → Theoretical estimation) for six properties: effective moisture diffusivity D, effective thermal conductivity k, air-boundary heat/mass transfer coefficients h_H/h_M, lumped drying constant K, and equilibrium moisture content X_e. The measurement heritage is polymer-first (Crank & Park, Diffusion in Polymers; Frisch & Stern), and the data tables list cellulose acetate, PVA, polyolefins, Avicel (microcrystalline cellulose), and starch gels — the chemistries of fluff pulp, nonwovens, and SAP carriers.

## Definition 定义

- **Effective moisture diffusivity 有效水分扩散系数** (p.81): "Diffusion in solids during drying is a complex process that may involve molecular diffusion, capillary flow, Knudsen flow, hydrodynamic flow, or surface diffusion. If we combine all these phenomena into one, the effective diffusivity can be defined from Fick's second law" ∂X/∂t = D∇²X (Eq. 4.1); units m²/s.
- **Pore model 孔隙模型** (p.87, Eq. 4.3): D = (ε/τ²)·δ·D_A — diffusivity scales with porosity over tortuosity squared; "open, straight pores dry fast."
- **Effective thermal conductivity 有效导热系数** (p.88–89): from Fourier's law ∂T/∂t = (k/ρc_p)∇²T (Eq. 4.4); used "in cases in which heat transfer during drying takes place through conduction (internally controlled drying)" — i.e. when Biot number > 1.
- **Boundary coefficients 边界传热/传质系数** (p.94): Q = h_H·A·(T_A − T) (Eq. 4.5); J = h_M·A·(X_AS − X_A) (Eq. 4.6); used when drying is externally controlled (Bi < 0.1). Lewis relationship h_M/h = 1/c_p (Eq. 4.13, p.97).
- **Drying constant 干燥常数** (p.98): Lewis thin-layer law dX/dt = −K(X − X_e) (Eq. 4.14); "the drying constant embodies all the transport properties into a simple exponential function" (p.98–99); K = π²D/L² for slabs (Eq. 4.15, p.99).
- **Equilibrium moisture & isotherm 平衡水分与吸附等温线** (p.100): X_e vs water activity a_w at fixed T; "It is clear from Figure 4.11 that the desorption isotherm is the curve to use for the process of drying." Type II isotherms = hydrophilic polymers (natural fibers, foods); type III = less hydrophilic (rubbers, plastics, synthetic fibers) (p.100). GAB is "probably the most suitable for process analysis and design of drying" (0.1 < a_w < 0.9, p.102).

## Key Claims 核心观点

1. **Models are ready, properties are not** (p.79–80): "more and more sophisticated drying models are becoming available, but a major question that still remains is the measurement or determination of the parameters used in the models"; Keey: "it is probably unrealistic to expect complete hygrothermal data for materials of commercial interest."
2. **The Biot switch dictates the design lever** (p.81–82, 89, 94): internal control (Bi > 1) → you must know D/k precisely (large particles, high-velocity air; high-porosity solids may be heat-controlled); external control (Bi < 0.1) → h_M/h_H and air-side correlations govern.
3. **Polymer diffusion anomaly** (p.85–86): "for several of the less hydrophilic polymers (e.g., polymethacrylates and polyacrylates) the moisture diffusivity decreases with increasing water content" — the swelling-controlled signature; for some hydrophobic polyolefins D is concentration-independent. Arrhenius D = D₀exp(−E/RT) otherwise holds (Eq. 4.2).
4. **Desorption branch for drying** (p.100): adsorption branch for rewetting, desorption for drying — hysteresis must be respected.
5. **Simultaneous estimation protocol** (§4.7, p.103–106): one drying experiment (Fig. 4.15 rig) + coupled process model (moisture diffusion 4.16, boundary vapor 4.18, heat conduction 4.20, boundary heat 4.22) regressed to return D, k, h_H, h_M at once; validated by relative residuals (Eqs 4.24–4.27).
6. **Honest limits of estimation** (p.93, 99–100): thermal-conductivity theory "has little, if any, meaning" for solids; K cannot be estimated theoretically — measurement is the only reliable route.

## Limitations 局限

- Data overwhelmingly foods/ceramics; polymer rows sparse (cellulose acetate tabulated: 2.0E-12–3.2E-12 m²/s at 25°C; Avicel 5.0E-9–5.0E-8); polyolefins named but not quantitatively tabulated.
- The polyacrylate anomaly (D falling with water) is reported without mechanism — no swelling, free-volume, or Tg discussion.
- Tables 4.15–4.18 universal Arrhenius × moisture model (1773 data from 175 papers, p.107–109) is foods-only; no equivalent for polymer mats.
- OCR/notation noise in the source; equations should be re-checked against the print edition before simulator use [待验证].

## Hygiene Implication 卫材关联

- **绒毛浆 D 必须自测**: 绒毛浆属纤维素类，预期 D ~10⁻¹²–10⁻⁹ m²/s 量级（对照 cellulose acetate 2E-12、Avicel 5E-9，p.84）；不要借用文献值，用 §4.7 回归装置在产线对应风速/温度下实测本牌号。
- **SAP 干燥预期非 Fickian**: 聚丙烯酸盐化学 ⇒ 凝胶水合时 D 可能随含水率上升而下降 (p.85) —— 降速段应以溶胀控制（Case-II）核建模，而非纯 Fick Eq. 4.1；并使用脱附支等温线。
- **PP/PE 非织造布 = Type III 等温线**: 亲水性弱、X_e 极低，干燥由外部 h_M 控制（Bi < 0.1）——按 Lewis 关系 (Eq. 4.13) + 边界层关联式 (Tables 4.9–4.10) 从空气侧定尺寸，而非从 D。
- **Biot 阈值选设计杠杆**: Bi > 1 → 调材料（定量、孔隙率 ε/τ²，Eq. 4.3）；Bi < 0.1 → 调空气（风速、温度）。这决定了是改网布配方还是改烘箱规格。
- **复合芯体 GAB 等温线**: 对 fluff+SAP 混合物测脱附等温线（重量法，p.101–102），拟合 GAB 得 X_e(a_w, T)，喂给 Ch3 衡算与 §4.7 模型；仓库规格则须用吸附支（参见 Ch2 滞后讨论）。
- **薄层 K 快速估算**: 一次恒定温/湿薄层干燥 → 拟合 Eq. 4.14 得 K → 已知厚度时经 Eq. 4.15 反推 D —— 新定量非织造布最快捷的一阶干燥机选型路径。

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch2 Experimental Techniques in Drying]]
- [[Industrial Drying Ch3 Basic Process Calculations and Simulations in Drying]]
- [[Industrial Drying Ch33 Drying of Fibrous Materials]]
- [[Industrial Drying Ch41 Drying of Polymers]]

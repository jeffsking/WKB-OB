---
type: source
title: "Industrial Drying Ch2 Experimental Techniques in Drying"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch02.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Drying-process characteristics (material properties, transfer coefficients, shrinkage) 'cannot be calculated by analysis … can be determined only by adequate experiments' (p.31)."
  - "Direct (reference) moisture method: disintegrate sample to 1–2 mm³, 4–5 g in pre-weighed container, dry at 102–105°C, complete when two consecutive measurements agree within ±0.05% (p.32); faster 130–150°C variant deviates 0.5–1.0% and is only approximate (p.32)."
  - "Industrial in-line moisture uses electrical methods — ohmic dc resistance, dielectric capacitance, ac loss — plus Karl–Fischer, toluene distillation, ethanol extraction for water-specific needs (p.33)."
  - "Sorption hysteresis: for capillary-porous materials equilibrium vapor pressure depends on the direction of approach, so adsorption and desorption equilibrium moisture must be distinguished (p.33)."
  - "Scale-up validity requires the lab sample not be too small, placement be similar, and drying-to-nondrying surface ratio be identical to the industrial unit (p.39–40)."
  - "Receding-front model: in the falling-rate period an evaporation front penetrates inward; both the evaporated moisture and the drying heat must pass through the already dried layer (p.44)."
summary_cn: "系统讲解干燥实验测量技术——平衡含水量与吸附等温线、干燥速率曲线、传热传质系数提取及床层体积系数——是干法设计参数唯一可靠的获取途径。"
tags: ["source/book", "drying/experimental-techniques", "drying/moisture-measurement", "drying/sorption-isotherm", "drying/scale-up", "qa/characterization"]
tags_zh: ["来源/书籍", "干燥/实验技术", "干燥/水分测定", "干燥/吸附等温线", "干燥/放大", "质检/表征"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch1 Principles and Classification]]", "[[Industrial Drying Ch33 Drying of Fibrous Materials]]", "[[Industrial Drying Ch35 Drying of Pulp and Paper]]", "[[Industrial Drying Ch40 Drying of Coated Webs]]"]
---

# Chapter 2 — Experimental Techniques in Drying

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.2, pp.31–49. (Author: K. Molnár)

## Overview 概述

Chapter 2 is the measurement chapter of the handbook: it catalogues the laboratory and pilot-scale experimental techniques needed to obtain the material and transport parameters that every dryer design calculation consumes — moisture content, sorption-equilibrium isotherms, drying-rate curves, and heat/mass transfer and diffusivity coefficients of wet and dry solids. It operationalises Ch.1's abstract definitions (bound/unbound moisture, X*, characteristic curve) as lab procedures, and supplies the coefficient inputs that Chs.3–5 plug into balances.

## Definition 定义

- **Direct moisture method 直接水分测定法** (p.32): oven/vacuum drying of a disintegrated sample to constant mass — "dried at 102–105°C. The drying process may be considered complete when the difference between the values obtained for the moisture content … by two consecutive measurements does not exceed ±0.05%."
- **Indirect moisture method 间接（在线）水分测定法** (p.33): "electrical methods of which three main varieties have become widespread: moisture determination based on the change of the ohmic dc resistance, a measurement of the electrostatic capacitance (dielectric constant of the material), and a measurement of the loss in an ac field"; plus Karl–Fischer titration, toluene distillation, and absolute-ethanol extraction for water-specific determination.
- **Sorption hysteresis 吸附滞后** (p.33): "the value of equilibrium vapor pressure generally depends, for capillary-porous materials, upon the direction of the approximation … This phenomenon is known as sorption hysteresis. For this reason it is necessary to distinguish adsorption equilibrium moisture from desorption equilibrium moisture."
- **Drying rate N 干燥速率** (p.40): N = −(1/A_s)·dm_SW/dt = (m_S/A_s)·dX/dt (Eq. 2.6); gas-side coefficients h from j_q = h(T_G − T_W) (Eq. 2.7) and K from N = K(Y_W − Y_G) (Eq. 2.10).
- **Volumetric transfer coefficients 体积传质/传热系数** (p.46): h_V = h·dA_s/dV, K_V = K·dA_s/dV (Eqs 2.37–2.38), for beds of unknown interfacial area (fixed/moving/through-circulation dryers, Eqs 2.46–2.53).
- **Receding/penetrating front model 蒸发前沿（退缩前沿）模型** (p.44): "an evaporation front penetrates from the surface of the material into the interior … The moisture evaporated at the plane of phase change must pass through the pores of the already dried layer … At the same time the heat required for drying has to pass through the already dried layer."

## Key Claims 核心观点

1. **Parameters must be measured, not calculated** (p.31): "In most cases these characteristics cannot be calculated by analysis … these characteristics can be determined only by adequate experiments." This is the chapter's governing thesis — no generic literature value for "pulp" or "SAP" substitutes for measurement on the actual grade, binder, and geometry.
2. **Five aims of drying experiments** (p.32): (1) choice of adequate drying equipment, (2) data for planning, (3) efficiency/capacity of existing equipment, (4) effect of operational conditions on product shape and quality, (5) study of drying mechanism.
3. **Isotherm methods** (p.36–39): constant vapor-pressure technique via saturated-salt solutions (Table 2.3) and developed vapor-pressure technique (manometer, psychrometer, isotonic method); both branches must be measured because of hysteresis (p.33).
4. **Scale-up prerequisites** (p.39–40): "the sample must not be too small and the conditions of drying must if possible be identical to the conditions anticipated in the industrial unit … The ratios of the drying surface to the nondrying surface must be identical."
5. **Coefficient extraction ladder** (§2.4): constant-rate period → gas-side h, K; falling-rate period → internal k_h, k_m via eigenvalue fits (Eqs 2.12–2.25) or receding-front effective diffusivity D_a = D_VG·m (Eq. 2.26) for porous solids; double-layer slabs treated at p.44–45.

## Method Ladder 方法阶梯

| Level | Technique | Output |
|---|---|---|
| Equilibrium | Oven / vacuum desiccator; Karl–Fischer | Reference moisture content (±0.05% convergence, p.32) |
| Equilibrium | Saturated-salt / developed-p_v isotherm | X*(ads), X*(des) — branch-dependent |
| Kinetics (lumped) | Convection rig, continuous weighing | Rate curve N vs. X → N_c, X_cr, X* (Figs 2.6–2.9) |
| Kinetics (distributed) | Thermocouples in plane slab | k_h, k_m via eigenvalue fits (Eqs 2.12–2.25) |
| Bed | Rotary / through-circulation rig | Volumetric h_V, K_V (Eqs 2.37–2.53); rotary correlation Eq 2.45 flagged "not generally applicable" (p.46) |

## Limitations 局限

- Entirely 1-D homogeneous-slab oriented; does not address anisotropic, multi-component webs and cores (airlaid web + SAP + adhesive + PE film).
- Heterogeneous mixtures: the through-circulation section (p.48, alfalfa stems vs. leaves) says "care must be exercised" but gives no quantitative method for multi-component furnishes.
- No uncertainty/error analysis on the eigenvalue fits (Eqs 2.19–2.25); constant k_h, k_m assumed while fluff shrinks and SAP swells.
- Silent on real-time in-line moisture distribution in moving webs at line speed.

## Hygiene Implication 卫材关联

- **进厂水分放行标准**: 采用直接法全流程作为 fluff/SAP/非织造布残留水分的审计标准 —— 1–2 mm³ 碎样、4–5 g 样品、102–105°C 烘干、连续两次称量差 ≤±0.05% (p.32)。对已溶胀 SAP 用 Karl–Fischer 而非烘箱法，避免交联网络降解 (p.33)。
- **等温线必须测双支**: 干燥机产出的是脱附支（desorption），仓储再吸湿走吸附支（adsorption）；两支的 X* 不同，仓库稳定水分规格应从吸附支设定，干燥终点从脱附支设定 (p.33–36)。两支混用会系统性错设水分下限。
- **放大保真实验**: 表征新绒毛浆/无尘纸牌号时，用与产线相同定量、开孔面积和厚度比的样片做集中参数干燥速率实验 (p.39–40)，提取 N_c、X_cr、X* 供 Ch3/Ch5 设计输入；切勿用揉散的松散样品。
- **退缩前沿 = 干壳阻力**: 蒸发前沿内移后，热与蒸汽都必须穿过已干层 (p.44) —— 这正是 falling-rate 段缓慢的物理原因，也是热风穿透（through-air）非织造布应保持薄而开放结构、缩短干区路径的依据。双层模型 (p.44–45) 是涂层/复合_web 干燥受阻的最接近类比。
- **在线水分交叉校验**: 产线用介电/电容传感器 (p.33) 做实时控制，但须周期性用烘箱/KF 基准法标定；传感器读数为相对值，实验室方法为绝对值。

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch1 Principles and Classification]]
- [[Industrial Drying Ch33 Drying of Fibrous Materials]]
- [[Industrial Drying Ch35 Drying of Pulp and Paper]]
- [[Industrial Drying Ch40 Drying of Coated Webs]]

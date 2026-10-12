---
type: source
title: "Industrial Drying Ch3 Basic Process Calculations and Simulations in Drying"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch03.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Drying calculation has migrated from graphical methods to computer-oriented methodology (Excel, Mathcad, MATLAB, Mathematica), but 'This does not mean that the computer will relieve one from thinking' (p.52)."
  - "Every dryer model is built from the master balance Inputs − Outputs = Accumulation (Eq. 3.1, p.53); the accumulation term decides algebraic vs. ODE vs. PDE."
  - "A 16-case classification (operation type × flow geometry × flow pattern, Fig. 3.1, p.54) pre-selects the model template; lumped vs. distributed depends on whether properties vary along the flow direction (p.54)."
  - "Kinetics are closed by the characteristic drying curve F = f(Φ) (Eq. 3.29) or thin-layer equations — Lewis dX/dt = −k(X−X*) (Eq. 3.32) and Page F = exp(−(kt)^n) (Eq. 3.36) (p.56–57)."
  - "Psychrometric calculations 'form a basis on which all drying models are built' (p.58–59); the air–water wet-bulb shortcut is inaccurate for other vapor systems, where WBT deviates from AST 'by several degrees Celsius' (p.59)."
  - "The conclusion flags a materials-database gap: 'very little has been done in the area of materials databases … an experimental determination of the missing data is necessary' (p.77–78)."
summary_cn: "干燥过程计算的建模方法学——16 类干燥机分类、质量/能量衡算、特征干燥曲线与薄层方程封闭、湿度学核心程序——把测量系数转化为干燥机尺寸与干燥时间。"
tags: ["source/book", "drying/process-calculations", "drying/modeling", "psychrometrics", "drying/kinetics", "simulation"]
tags_zh: ["来源/书籍", "干燥/过程计算", "干燥/建模", "湿度学", "干燥/动力学", "仿真"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch1 Principles and Classification]]", "[[Industrial Drying Ch2 Experimental Techniques in Drying]]", "[[Industrial Drying Ch35 Drying of Pulp and Paper]]", "[[Industrial Drying Ch41 Drying of Polymers]]"]
---

# Chapter 3 — Basic Process Calculations and Simulations in Drying

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.3, pp.51–78. (Authors: Z. Pakowski & A.S. Mujumdar)

## Overview 概述

Chapter 3 is the computational engineering chapter: it teaches the reader to build and solve a mathematical model of a dryer. It replaces the older graphical/shortcut culture with a computer-oriented methodology while insisting the computer "will not relieve one from thinking" (p.52). Structure: (1) classify the process into one of 16 generic dryer cases; (2) assemble the five parts of a deterministic model — balances, constitutive (kinetic) equations, equilibrium relations, property equations, geometric relations; (3) solve steady-state input–output or distributed-parameter models for cocurrent/countercurrent/cross-flow including shrinkage; (4) shortcut methods and software tools.

## Definition 定义

- **Master balance 总衡算** (p.53): "Inputs − outputs = accumulation" (Eq. 3.1). Steady state → algebraic; batch → ODE in time; distributed → PDE.
- **LPM vs. DPM 集中/分布参数模型** (p.54): "If a property varies continuously along the flow direction … the balance equation can only be written for a differential space element … This is a distributed parameter model (DPM)"; "When the volume … is perfectly mixed … This is the principle of a lumped parameter model (LPM)."
- **16 generic cases 16 类通用工况** (p.54, Fig. 3.1): operation type (batch/continuous/semicontinuous) × flow geometry (parallel/cocurrent/countercurrent/cross) × flow pattern (plug/perfectly mixed).
- **Characteristic drying curve (CDC) 特征干燥曲线** (p.56): F = f(Φ) (Eq. 3.29), with Langrish two-segment form (Eq. 3.30) splitting the falling rate at Φ_B.
- **Thin-layer equations (TLE) 薄层方程** (p.56–57): Lewis (1921) dX/dt = −k(X − X*) (Eq. 3.32); Page (1949) F = exp(−(kt)^n) (Eq. 3.36).
- **Psychrometric core 湿气体性质核心** (p.58–59): RH ω = p_s(t)/P (Eq. 3.45), humidity Y (Eq. 3.46), enthalpy (Eq. 3.47), adiabatic saturation (Eq. 3.49), wet-bulb (Eqs 3.50, 3.52), Lewis number (Eq. 3.53). "The ability to perform psychrometric calculations forms a basis on which all drying models are built."
- **GAB isotherm GAB 等温线** (p.60, Eq. 3.56): implicit form solvable for water activity a_w; used to set X* in models.

## Key Claims 核心观点

1. **Three reasons to calculate** (p.52–53): Design — "selection of a suitable dryer type and size" and "specification of all process parameters"; Simulation — "for a given dryer, calculation of dryer performance"; Optimization — seeking an optimum in either.
2. **Classify before you calculate** (p.53–54): the 16-case grid pre-selects the equation template; type-1 cases (no accumulation) "do not exist in industry."
3. **LPM/DPM is a make-or-break choice** (p.54, p.70): a thin layer on a tray may legitimately be LPM; a deep bed or shrinking solid requires DPM. The tray-dryer example (§3.8.1) shows both solid and air as LPM (case 2d), solved by ODEs 3.113–3.120.
4. **Kinetic closure from experiment** (p.56–57): CDC and Lewis/Page equations are curve-fits to the measured rate curve; volumetric drying rate links the TLE to the balances (Eqs 3.37–3.40).
5. **Air–water-only shortcuts are a trap** (p.59): for other gas–vapor systems (e.g., solvent drying of coated webs) the WBT≈AST relation deviates "several degrees Celsius" — use the general wet-bulb equation.
6. **Materials data are the bottleneck** (p.77–78): property databases are sparse; missing parameters must be measured (tying the whole chapter back to Ch.2).

## Model Assembly Sequence 建模流程

1. Classify (§3.3): 16 cases → equation template.
2. Write balances (§3.4.1): mass (Eqs 3.5–3.6), energy (Eqs 3.7–3.8); DPM forms Eqs 3.9–3.11.
3. Close kinetically (§3.4.2): CDC (Eqs 3.29–3.30) or TLE (Lewis 3.32, Page 3.36).
4. Add auxiliary relations (§3.4.3): psychrometrics (Eqs 3.45–3.53), GAB isotherm (Eq. 3.56), property tables (Tables 3.1–3.2).
5. Solve (§3.5–3.9): continuous DPM (§3.6), solid-phase DPM with/without shrinkage (§3.7), batch oven/fluid-bed/deep-bed (§3.8), semicontinuous (§3.9).
6. Shortcut & software (§3.10–3.11): free/bound-moisture split for quick sizing; dryPAK/Matlab/Mathcad.

## Limitations 局限

- Psychrometric shortcuts (Eqs 3.50, 3.52) are air–water only; solvent systems need re-derivation (p.59).
- Continuum assumption throughout (p.53); bubbling fluid beds and pneumatic conveying are mentioned but not modelled.
- Shrinkage DPM shown only as a finite-difference mesh (Fig. 3.15, p.69); deformation-coupled equations deferred to references (Hasatani & Itaya 1996; Kechaou & Roques 1990).
- No validation/uncertainty guidance despite Ch.2's warning that coefficients carry measurement error.
- Worked examples are agricultural/mineral (clay spheres, corn, grapes) — hygiene properties must be substituted by the reader.

## Hygiene Implication 卫材关联

- **先分类再建模门槛**: 任何新卫材干燥单元（热风穿透烘箱、SAP 流化床、无尘纸烘缸）先在 16 类网格中定位 (p.53–54) —— 连续/间歇 × 顺/逆/错流 × 平推/全混 —— 再写衡算；拒绝未声明模型假设的供应商选型。
- **按牌号建物性库**: 每个绒毛浆/SAP/PP 非织造布牌号维护一行内部数据库：GAB 系数 (Eq. 3.56)、Page 参数 k、n (Eq. 3.36)、X*、X_cr、收缩因子 —— 结论明确指出这些无法从文献借用 (p.77–78)，须由 Ch2 实验供给。
- **溶剂体系警报**: 含醇/丙酮类整理剂或胶黏剂的擦拭布/膜状网干燥不能用空气-水湿球简化式 (Eq. 3.50)，须用通用湿球方程 (Eq. 3.52, p.59)。
- **收缩/溶胀耦合**: 非织造布干燥收缩时勿用刚性几何 DPM；Fig. 3.15 (p.69) 的受约束/自由收缩网格逻辑须与传热传质方程耦合，否则停留时间与水分剖面预测错误。对溶胀 SAP 凝胶该框架是否可推广为溶胀前沿，本章未解决 [待验证]。
- **快捷估算**: 自由水/结合水分割法 (§3.10.1, p.76) 可作新产线一阶数量级估算，再回归完整模型。

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch1 Principles and Classification]]
- [[Industrial Drying Ch2 Experimental Techniques in Drying]]
- [[Industrial Drying Ch35 Drying of Pulp and Paper]]
- [[Industrial Drying Ch41 Drying of Polymers]]

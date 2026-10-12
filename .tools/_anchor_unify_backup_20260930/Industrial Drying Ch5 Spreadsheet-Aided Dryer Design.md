---
type: source
title: "Industrial Drying Ch5 Spreadsheet-Aided Dryer Design"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch05.md.md"
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Microsoft Excel with VBA 'is an effective tool for process design' because 'Spreadsheets offer sufficient process model hospitality' — models, charts, Solver optimization and databases in one environment (p.119–120)."
  - "Degrees of freedom govern solvability: 'M variables … N equations; generally, M is greater than or equal to N, and the difference M–N corresponds to the degrees of freedom of the process'; design variables D = F − K (p.121, Table 5.4)."
  - "The worked belt-dryer model is a 37-variable / 24-equation system with 13 degrees of freedom, 9 specifications and 4 design variables — drying-air humidity Y, temperature T, velocity V, belt width D (Tables 5.10, 5.14–5.15)."
  - "Required drying time integrates the Lewis thin-layer form: t = t_c·ln[(X₀ − X_e)/(X − X_e)] with time constant t_c as a function of air velocity, temperature and humidity (T10.4–T10.5, p.126)."
  - "Optimization objective is total annual cost: TAC = e·C_eq + C_op with equipment cost scaled by area/power exponents (Table 5.17); the numerical example yields L = 12.6 m, A_b = 25.3 m², Q = 0.91 MW, η = 0.69, TAC = 357 k$/y (p.129–131)."
summary_cn: "将干燥物理模型转化为 Excel+VBA 可运行模拟器的实施章节——自由度分析、四表架构、六步构建法，并以完整的带式干燥机 37 变量模型与 TAC 年化成本优化作示范。"
tags: ["source/book", "drying/dryer-design", "simulation/spreadsheet", "drying/cost-estimation", "engineering/optimization"]
tags_zh: ["来源/书籍", "干燥/干燥机设计", "仿真/电子表格", "干燥/成本估算", "工程/优化"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch3 Basic Process Calculations and Simulations in Drying]]", "[[Industrial Drying Ch4 Transport Properties in the Drying of Solids]]", "[[Industrial Drying Ch17 Conveyor Dryers]]", "[[Industrial Drying Ch53 Cost Estimation]]"]
---

# Chapter 5 — Spreadsheet-Aided Dryer Design

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.5, pp.119–134. (Authors: Z.B. Maroulis, G.D. Saravacos & Arun S. Mujumdar)

## Overview 概述

Chapter 5 is the how-to-implement chapter: it converts the physical models of Chs.1–4 into a working Microsoft Excel + VBA simulator. Thesis: spreadsheet software is "an indispensable tool for engineers" (p.119). Two parts: (1) §5.2 principles — a six-step recipe (workbook → model → Solver → charts → dialog boxes → integrated GUI) plus degrees-of-freedom analysis; (2) §5.3–5.4 a complete worked conveyor belt dryer — 37 variables / 24 equations (Table 5.10, Eqs T10.1–T10.24) covering psychrometrics, drying kinetics, mass/energy balances, belt and fan sizing, performance indices, and a TAC objective, fully implemented in Excel.

## Definition 定义

- **Modeling / Simulation / Design 建模/仿真/设计** (p.120, Table 5.1): "Modeling: is the procedure to translate the physical laws of a process to mathematical equations"; "Simulation: is the appropriate software which predicts the real performance of a process"; "Design: is a procedure to size and rate a process in order to obtain a specific goal." Sizing = compute equipment size from specs; Rating = compute operating conditions from specs + size.
- **Degrees of freedom 自由度** (p.121, Table 5.4): F = M − N; "Design variables D = F − K" where K = problem specifications.
- **Four-unit simulator architecture 四表架构** (p.121–122, Fig 5.2): Graphics interface / Problem solution (VBA) / Database / Process model — "'Process Model Worksheet' is the heart of the system calculations."
- **Required drying time 所需干燥时间** (p.126, T10.5): t = t_c·ln[(X₀ − X_e)/(X − X_e)], with t_c = d₀·V^c₂·T^c₃·Y^c₄ (T10.4) — the integrated Lewis thin-layer solution (cf. Ch.4 Eq 4.14).
- **Balances 衡算** (p.126): W = F(X₀ − X) (T10.6, solid moisture); W = F_a(Y − Y₀) (T10.7, air moisture); Q = Q_we + Q_sh + Q_ah (T10.11); heater area A_s = Q_s/(U(T_s − T)) (T10.12).
- **Belt/fan sizing 带与风机** (p.126): A_b = L·D (T10.16), u_b = L/t (T10.17), ΔP = f₁·Z₀·V² (T10.18), E_f = ΔP·F/r (T10.20).
- **TAC 年化总成本** (p.128, Table 5.17): C_eq = C_bel·A_b^n_bel + C_exc·A_s^n_exc + C_fan·E_f^n_fan (T17.1); "TAC = e·C_eq + C_op" (T17.3), e = capital recovery factor.

## Key Claims 核心观点

1. **Spreadsheets are the default design environment** (p.119–120): "Microsoft Excel with Visual Basic for Applications is an effective tool for process design … connected easily and online with charts and graphic objects, resulting in powerful and easy-to-use graphical interfaces."
2. **DOF analysis prevents ill-posed problems** (p.121): the worked case has M = 37, N = 24 ⇒ F = 13; with K = 9 specs ⇒ only 4 design variables (Y, T, V, D). You cannot meaningfully "optimize" more knobs than D.
3. **The equation chain is fully deterministic** (p.125–126): Antoine (T10.1) → psychrometrics (T10.2) → a_w → Oswin X_e (T10.3) → t_c (T10.4) → t (T10.5) → balances (T10.6–T10.12) → holdup → belt → fan → performance indices η, r (T10.23–24).
4. **Cost closes the loop** (p.128–131): Solver minimizes TAC over {Y, T, V, D}; the worked example (F = 0.1 ton/h db, X₀ = 10 → X = 0.1 kg/kg db, T = 90°C, V = 1.5 m/s) yields L = 12.6 m, A_b = 25.3 m², W = 0.99 ton/h, Q = 0.91 MW, η = 0.69, r = 39.1 kg/h·m², TAC = 357 k$/y.
5. **Six-step build recipe** (p.122–127, Table 5.6): workbook prep → process modeling → Solver optimization → tables/charts → dialog boxes → integrated GUI.

## Limitations 局限

- Legacy VBA: the DialogSheets() calls (Table 5.9) were removed after Excel 2003; a modern rebuild must use UserForm objects — the logic survives, the printed code does not run [待验证 against current Excel].
- The example material is anonymous with X₀ = 10 kg/kg db — unrealistically high for hygiene webs (fluff pulp enters ~1–3 kg/kg db wet; SAP granules are pre-dried).
- No uncertainty/sensitivity beyond one-way/two-way tables (Figs 5.7–5.8); no error propagation from measured properties into TAC.
- The simulator is only as good as X_e (T10.3), t_c (T10.4), heats, densities — exactly the properties Ch.4 says are missing for commercial polymers; the chapter assumes you have them.

## Hygiene Implication 卫材关联

- **首个绒毛浆/非织造布干燥机选型器**: 不要先买商用模拟软件 —— 按 §5.2 六步构建带式干燥机电子表格，把 Technical Data 块替换为自测的等温线常数（GAB/Oswin，Ch4）与动力学常数（K → t_c = 1/K），即可获得本牌号的停留时间与带长预测。
- **带式/穿透式干燥机直接对应**: 输送带式干燥机正是绒毛浆纤维垫、非织造布网与芯体复合材料干燥的设备类别；T10.1–T10.24 方程链可整体复用，仅需替换物性块。
- **自由度纪律防过度设计**: 对新非织造布干燥线先列 M/N，确认 D = F − K ≤ 实际可调旋钮数（空气温度、湿度、风速、带几何）—— 试图"优化"超过 D 个变量在数学上无意义 (p.121)。
- **等温线换源**: T10.3 的 Oswin 形式应替换为自有 GAB 参数（纤维素 Type II vs PP/PE Type III 差异巨大），这是把模拟器重定向到 fluff/SAP 的唯一必改项。
- **用 TAC 而非纯物理做方案裁决**: 编入本地区公用工程价格后让 Solver 最小化 TAC，在同一口径下比较 conveyor vs 流化床 vs 接触式（Ch6）；这为极薄芯体产线的 capex/opex 拆分提供第一道 go/no-go 依据。

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch3 Basic Process Calculations and Simulations in Drying]]
- [[Industrial Drying Ch4 Transport Properties in the Drying of Solids]]
- [[Industrial Drying Ch17 Conveyor Dryers]]
- [[Industrial Drying Ch53 Cost Estimation]]

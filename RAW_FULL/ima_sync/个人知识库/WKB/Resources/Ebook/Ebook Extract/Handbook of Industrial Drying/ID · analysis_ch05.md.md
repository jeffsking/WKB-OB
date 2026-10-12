---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_0b63c66f41babb310aad1fa558dec201001a693ee6c0644e"
source_file: "ID · analysis_ch05.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch05.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch05.md.md

# Analysis of Chapter 5 — Spreadsheet-Aided Dryer Design

Handbook of Industrial Drying, 4th ed. (Mujumdar, CRC Press)
Authors of chapter: Z.B. Maroulis, G.D. Saravacos, and Arun S. Mujumdar
Target reader: hygiene-materials R&D (disposable diapers, wipes, absorbent cores, fluff-pulp procurement)

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

## 1. Overview (范围、对象与定位)

Chapter 5 is the how-to-implement chapter: it converts the physical models of Ch.1–Ch.4 into a working Microsoft Excel + VBA simulator. Its thesis is that spreadsheet software is now an "indispensable tool for engineers" (p.119) and that Excel with Visual Basic for Applications (VBA) "is an effective tool for process design" because "Spreadsheets offer sufficient process model 'hospitality'" (p.119–120) — i.e. they connect models, charts, Solver optimization, and databases into one environment.

The chapter has two parts:
- §5.2 Principles and Techniques — a six-step recipe (workbook → model → Solver → charts → dialog boxes → integrated GUI) and the foundational concepts of modeling / simulation / design, plus a degrees-of-freedom analysis (M variables, N equations, F = M−N, D = F−K) that frames every dryer problem.
- §5.3–§5.4 A worked conveyor belt dryer — a complete 37-variable / 24-equation model (Table 5.10, Eqs T10.1–T10.24) covering psychrometrics, drying kinetics, mass/energy balances, belt and fan sizing, performance indices, and an annualized-cost (TAC) objective, fully implemented in Excel (Figures 5.5–5.10).

For the hygiene reader this is the directly actionable deliverable: a conveyor/through-belt dryer is exactly the class of equipment used to dry fluff-pulp mats, nonwoven webs, and diaper core composites. The supplied spreadsheet skeleton can be re-pointed at your own material's psychrometric, isotherm, and kinetic parameters (the very properties Ch.4 says you must measure).

Print-page span: p.119–p.134 (PDF p.140–155).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — Spreadsheets are now the default design environment. (p.119)
> "Spreadsheet software has become an indispensable tool for engineers, because of the availability of personal computers, ease of use, and adaptability to many types of problems."
> "Microsoft Excel with Visual Basic for Applications is an effective tool for process design. Spreadsheets offer sufficient process model 'hospitality.' They are connected easily and online with charts and graphic objects, resulting in powerful and easy-to-use graphical interfaces." (p.119–120)

V2.2 — The three core definitions: modeling, simulation, design. (p.120, Table 5.1)
> "Modeling: is the procedure to translate the physical laws of a process to mathematical equations"
> "Simulation: is the appropriate software which predicts the real performance of a process"
> "Design: is a procedure to size and rate a process in order to obtain a specific goal"
Plus two sub-actions: "Sizing: given the process specifications calculate the equipment size... Rating: given the process specifications and the equipment size... calculate the operating conditions."

V2.3 — Degrees of freedom govern what you can solve. (p.121, Table 5.4)
> "Suppose that M variables are incorporated into the mathematical model of N equations; generally, M is greater than or equal to N, and the difference M–N corresponds to the degrees of freedom of the process." (Table 5.4: F = M – N; "Design variables D = F – K" where K = problem specifications.)
Implication: You cannot simultaneously solve for more than D = F − K design variables; the rest are fixed specs. This is the discipline that prevents an under/over-specified diaper-dryer model.

V2.4 — A simulator has a fixed four-unit architecture. (p.121–122, Fig 5.2)
> "The resulting simulator has generally the outline presented in Figure 5.2. Four different units are distinguished, with each one developed in a different sheet... 'Process Model Worksheet' is the heart of the system calculations. It contains the process model." The four units: Graphics interface, Problem solution (VBA), Database, Process model.

V2.5 — The six-step Excel implementation recipe. (p.122–127, Table 5.6)
> "Step 1: Workbook Preparation... Step 2: Process Modeling in a Spreadsheet... Step 3: Using 'Solver' for Process Optimization... Step 4: Using Excel Tables and Charts for Presentation of the Results... Step 5: Introducing Dialog Boxes and Controls to Modify Data... Step 6: Toward an Integrated Graphics Interface."

V2.6 — Solver drives optimization via a named objective and variables. (p.123, Table 5.8)
> "Sub optimum()... SolverOk SetCell: Range('objective'), MaxMinVal: 1, ByChange: Range('variables')... Statement 4 suggests that all cells in the range 'constraints' must be greater than zero." (Table 5.8 VBA skeleton.)
Implication: The hygiene engineer encodes TAC as objective, belt/air specs as variables, and physical limits as constraints.

V2.7 — The belt dryer model is fully equation-driven (T10.1–T10.24). (p.125–126, Table 5.10)
> "Equation T10.1 calculates the vapor pressure at drying temperature, whereas Equation T10.2 is the psychrometric equation. Equation T10.1 and Equation T10.2 are used to calculate the water activity at drying conditions... Equation T10.3 calculates the equilibrium material moisture content at drying conditions, whereas Equation T10.4 estimates the drying time constant at drying conditions. Both Equation T10.3 and Equation T10.4 are used in Equation T10.5, which calculates the required drying time." (p.125)

V2.8 — Drying time integrates from the Lewis thin-layer form. (p.126, Table 5.10)
> "t = t_c ln(X₀ − Xₑ)/(X − Xₑ)" with t_c from T10.4 (t_c = d₀·V^c₂·T^c₃·Y^c₄). This is the integrated constant-rate/falling-rate thin-layer solution (cf. Ch.4 Eq 4.14).

V2.9 — Mass and energy balances close the model. (p.126, Table 5.10)
> "W = F(X₀ − X)  (T10.6) ... W = Fₐ(Y − Y₀)  (T10.7)" (solid and air moisture balances)
> "Q_we = F(X₀ − X)ΔH₀ − (C_PL − C_PV)T" (water vaporization energy), with Q_sh (solid heating, T10.9), Q_ah (air heating, T10.10), Q = Q_we+Q_sh+Q_ah (T10.11), and heater area A_s = Q_s/(U(T_s−T)) (T10.12).

V2.10 — Belt geometry and fan are sized explicitly. (p.126, Table 5.10)
> "A_b = L·D  (T10.16)... u_b = L/t  (T10.17)" (belt area, velocity); "ΔP = f₁·Z₀·V²  (T10.18)... Fᵢ = ρₐ·V·D·L  (T10.19)... E_f = ΔP·F/r  (T10.20)" (fan pressure drop, flow, power).

V2.11 — The worked problem fixes 37 variables, 24 equations, 4 design variables. (p.127, Table 5.14)
> "Process variables 37 / Degrees of freedom 13 / Specifications 9 / Design variables 4." Design variables (Table 5.15): Y (drying-air humidity), T (drying-air temperature), V (air velocity), D (belt width).

V2.12 — Cost is the optimization objective via TAC. (p.128, Table 5.17)
> "Equipment cost: C_eq = C_bel·A_b^n_bel + C_exc·A_s^n_exc + C_fan·E_f^n_fan  (T17.1)"
> "Total annual cost (objective function): TAC = e·C_eq + C_op  (T17.3)" where e is the capital recovery factor (T17.4).

V2.13 — A complete numerical example is supplied. (p.129–131, Fig 5.5/5.9)
> Example: feed F = 0.1 ton/h db, X₀ = 10 kg/kg db, X = 0.1 kg/kg db, d = 0.01 m, T = 90°C, V = 1.5 m/s, D = 2 m → L = 12.6 m, A_b = 25.3 m², W = 0.99 ton/h, Q = 0.91 MW, thermal efficiency η = 0.69, specific evaporation r = 39.1 kg/h·m², TAC = 357 k$/y.

## 3. Research Method (研究方法)

This is a methodology / software-engineering chapter, not an experimental one. The method is:

- Define modeling vocabulary (Table 5.1) and a simulation procedure (Table 5.2).
- Degrees-of-freedom analysis (Table 5.4, Fig 5.1) to classify variables into specs (K) and design variables (D = F − K).
- Architect the simulator into four sheets (Fig 5.2): Process Model (formulas), Database (data lists), Problem Solution (VBA/Solver), Graphics Interface.
- Implement in six steps (§5.2, Tables 5.6–5.9): name cells (Ctrl+Shift+F3), write model formulas, write a VBA optimum() calling Solver, build Excel Tables/Charts, add dialog boxes/scroll bars, integrate into a GUI.
- Validate on a worked belt-dryer case (§5.3–5.4) with full numeric input/output (Fig 5.5–5.10), including a cost analysis (Table 5.17) and a 5-page report (Fig 5.9).
The method is reproducible: any hygiene material substitutable by replacing the technical-data block (isotherm constants, kinetic constants, specific heats, densities) with your own measured values from Ch.4.

## 4. Argumentation (论证逻辑)

The argument is pragmatic and tool-centric:

- Claim: Good dryer design needs simulation, and simulation needs a friendly, cheap, widely available environment.
- Evidence: Spreadsheets meet all criteria (cost, ease, graphical hospitality, Solver, VBA, databases) — p.119–120.
- Method: Decompose design into modeling → DOF analysis → four-sheet architecture → six-step build → worked example.
- Proof of concept: The belt-dryer simulator (§5.3–5.4) solves a 37-variable problem, optimizes TAC over 4 design variables, and emits a full costed report — demonstrating the method scales to real equipment.
- Conclusion: The reader can replicate this skeleton for any dryer type (conveyor, through-circulation, fluidized) by swapping the process model equations.
For hygiene R&D the logic is: don't buy a $50k simulator to first-size a fluff through-dryer — build the Ch.5 spreadsheet, plug in Ch.4 properties, optimize TAC. Only escalate to commercial software once the physics is validated.

## 5. Role of This Chapter in the Book (在全书中的角色)

Ch.5 is the implementation bridge between theory (Ch.1–4) and the dryer-type catalog (Part II, starting p.134). Ch.1–4 give you definitions, properties, and balances; Ch.5 gives you a working calculator; Ch.6+ describe individual dryer classes you can then model in that calculator. It is the only chapter that is explicitly software-oriented, and it is the most directly reusable artifact in the assignment for a hygiene process engineer.

## 6. Strengths and Weaknesses (贡献与局限)

Strengths
- Gives a complete, copy-pasteable Excel+VBA skeleton (Tables 5.6–5.9, VBA in 5.8/5.9) — rare in a handbook.
- Degrees-of-freedom framing (Table 5.4) prevents ill-posed design problems.
- The belt-dryer model is self-contained and numerically validated (Fig 5.5/5.9), so the reader has a known-good reference.
- TAC objective (T17.3) embeds economics, not just physics.

Weaknesses
- Entirely Excel/VBA-centric; macros are legacy (pre-2007 dialog sheets, DialogSheets) and will not run unmodified in modern Excel/LibreOffice.
- The example material is anonymous ("Material xxxxxxx", p.130) with extreme X₀ = 10 kg/kg db; no hygiene-relevant material is demonstrated.
- No uncertainty/sensitivity quantification beyond one-way/two-way tables (Fig 5.7/5.8); Monte-Carlo or statistical propagation absent.
- Depends entirely on externally supplied properties (isotherm/kinetic constants) — which, per Ch.4, are missing for most commercial polymers.

## 7. Key Terms (关键术语)

||||
|---|---|---|
|Modeling|—|translate physical laws to equations (Table 5.1)|
|Simulation|—|software that predicts real process performance|
|Design|—|size & rate a process to meet a goal|
|Sizing / Rating|—|compute equipment size / operating conditions|
|Degrees of freedom|F = M − N|#variables − #equations (Table 5.4)|
|Design variables|D = F − K|free variables the engineer sets|
|Water activity|a_w|from Antoine (T10.1) + psychrometric (T10.2)|
|Equilibrium moisture|Xₑ|Oswin isotherm (T10.3)|
|Drying time constant|t_c|T10.4, function of V,T,Y|
|Required drying time|t|t = t_c·ln(X₀−Xₑ)/(X−Xₑ)|
|Evaporation rate|W|W = F(X₀−X) (T10.6)|
|Thermal load|Q|Q_we+Q_sh+Q_ah (T10.8–11)|
|Belt area / velocity|A_b, u_b|A_b=L·D, u_b=L/t (T10.16–17)|
|Specific evaporation|r|r = W/A_b (T10.24)|
|Thermal efficiency|η|η = Q_we/Q (T10.23)|
|Total annual cost|TAC|TAC = e·C_eq + C_op (T17.3)|

## 8. Micro close-reading (微观精读)

8.1 — The DOF line that prevents wasted work (p.121). "Suppose that M variables are incorporated into the mathematical model of N equations... the difference M–N corresponds to the degrees of freedom." For the belt dryer, M=37, N=24 ⇒ F=13; with K=9 specs ⇒ D=4 design variables (Table 5.14). Translation: you may optimize at most four knobs (Y,T,V,D). Trying to "optimize" more than four is mathematically meaningless — a common trap when scoping a new nonwoven dryer.

8.2 — T10.5 is the Lewis thin-layer integrated solution. "t = t_c ln[(X₀ − Xₑ)/(X − Xₑ)]" is exactly the time-integral of Ch.4 Eq 4.14 (dX/dt = −K(X−Xₑ)) with t_c = 1/K. The chapter thus reuses Ch.4's drying constant as the time constant — confirming the cross-chapter consistency the hygiene reader should exploit: measure K (Ch.4 §4.5) → feed t_c into this spreadsheet.

8.3 — Oswin isotherm as the equilibrium source (T10.3). The model computes Xₑ from an Oswin-type equation (b₁,b₂,b₃ in Table 5.12) rather than GAB (Ch.4 §4.6). The hygiene reader should substitute their own GAB/Oswin parameters (from Ch.4 §4.6 or in-house sorption balance) into the Technical Data block — the only edit needed to retarget the simulator to fluff/SAP.

8.4 — The costed example makes TAC tangible (p.131). Equipment 599 k$, operating 207 k$/y, TAC 357 k$/y, with belt dryer dominating equipment (538 k$) and electricity dominating operating (182 k$). For a hygiene plant this is the kind of first-cut capital/opex split that justifies or kills a dryer investment before any detailed engineering.

8.5 — Legacy VBA caveat (Table 5.9). The DialogSpecifications() subroutine uses DialogSheets(...), a feature removed after Excel 2003. A modern rebuild must use UserForm objects. The logic (sync edit boxes ↔ named cells) is unchanged; only the syntax is legacy.

## 9. Concept deep-dive (概念深掘)

9.1 Degrees-of-freedom as the design-compass. F = M − N tells you how many independent choices exist; D = F − K tells you how many the engineer makes. Specifying too many (K too high) over-constrains (no solution); too few leaves ambiguity. For a hygiene conveyor/through-dryer, typical specs are feed rate, initial/final moisture, ambient, steam T; design variables are air T, air humidity, air velocity, belt width/length. The chapter's 4-variable result is a template.

9.2 The four-sheet simulator architecture. Process Model (formulas only — auto-recalc on any input change) is the calculation core; Database holds data lists; Problem Solution holds VBA/Solver; Graphics Interface is human-facing. This separation is what makes the tool maintainable: change a property in Database, the Process sheet recomputes, charts/GUI refresh. The hygiene lab should adopt this exact separation so material-property updates don't break the model.

9.3 Belt-dryer model equation chain. Antoine (T10.1) → psychrometrics (T10.2) → a_w → Oswin Xₑ (T10.3) → t_c (T10.4) → t (T10.5) → material balance W (T10.6) → air balance (T10.7) → energy Q (T10.8–11) → heater A_s (T10.12) → holdup M,H (T10.13–15) → belt A_b,L,u_b (T10.16–17) → fan ΔP,Fᵢ,E_f (T10.18–20) → belt driver E_b (T10.21) → total E (T10.22) → indices η,r (T10.23–24). Every hygiene dryer reduces to a subset of this chain.

9.4 Optimization loop. optimum() sets objective=TAC, variables={Y,T,V,D}, constraints≥0, runs Solver. Press the "optimizer" button → optimum in seconds (p.124). This is the scaling/rating engine: rating = fix equipment, solve operating conditions; sizing = fix conditions, solve equipment. Both are just different K/D assignments.

9.5 Cost model. T17.1 scales equipment cost by area/power with exponents (n_bel, n_exc, n_fan); T17.2 operating = energy×utility cost; T17.3 TAC = e·C_eq + C_op with capital recovery factor e (T17.4) from interest i_r and lifetime l_f. The hygiene reader gets a full capex/opex/TAC view to compare dryer concepts (conveyor vs fluidized vs contact).

## 10. Critique (批判性评估)

- Legacy software. The VBA relies on DialogSheets (pre-2007 Excel). A 2026 reader must port to UserForm. The methodology survives; the code does not run as printed.
- Anonymous example material. X₀ = 10 kg/kg db is unrealistically high for most hygiene webs (fluff pulp enters ~1–3 kg/kg db wet; SAP granules are pre-dried). The numeric example is pedagogically fine but not a hygiene case.
- Property dependency unaddressed. The whole simulator is only as good as Xₑ(T10.3), t_c(T10.4), specific heats, densities — exactly the data Ch.4 says are missing for commercial polymers. The chapter assumes you have them; it does not tell the hygiene reader how scarce they are (that warning lives in Ch.4 §4.1).
- No validation/uncertainty. Single deterministic point solution; no propagation of property measurement error into TAC. For a go/no-go capex decision this is a real gap.
- OCR noise. Some equations (T10.3) lost subscripts/operators in OCR; the Oswin form was reconstructed from the named model in Table 5.12. Re-check against print before use.
## 11. Hygiene-Material Relevance & Action Cards (卫材相关性与行动卡)

H11.1 — Build the Ch.5 belt-dryer spreadsheet as your first fluff/SAP dryer sizer. Action: create BeltDryer.xls per §5.2 Steps 1–3; replace the Technical Data block with your measured Oswin/GAB constants (Ch.4 §4.6) and kinetic constants (Ch.4 §4.5 K or t_c).

H11.2 — Use DOF analysis before modeling any nonwoven dryer. Action: list M variables / N equations for your through-circulation or conveyor line; confirm D = F − K ≤ number of knobs you actually control (air T, humidity, velocity, belt geometry). Avoid over-specifying.

H11.3 — Retarget T10.3 to your own isotherm. Action: substitute GAB parameters (Ch.4 Table 4.13/4.14 style) for the Oswin b₁,b₂,b₃; keep the rest of the chain intact. This makes Xₑ physically correct for cellulose (Type II) vs PP/PE (Type III).

H11.4 — Feed Ch.4's drying constant into T10.5. Action: set t_c = 1/K from your thin-layer run (Ch.4 Eq 4.14/4.15); the spreadsheet then predicts residence time and belt length for your web basis weight.

H11.5 — Optimize TAC, not just physics. Action: encode utility costs (C_e, C_s) and equipment costs (C_bel, C_exc, C_fan) for your region; let Solver minimize TAC over {Y,T,V,D}. Compare conveyor vs fluidized vs contact (Ch.6) on equal TAC footing.

H11.6 — Modernize the VBA. Action: replace DialogSheets (Table 5.9) with UserForm; keep the sync logic (edit box ↔ named cell). Otherwise the GUI steps (5–6) will not run in current Excel.

H11.7 — Add uncertainty after first build. Action: once deterministic TAC works, wrap the Technical Data inputs in a one-way/two-way table (Fig 5.7/5.8) to see TAC sensitivity to your measured D, Xₑ, t_c — the properties Ch.4 flags as uncertain.

## 12. Book-Map Quotes (本书脉络引证)

- Ch.4 (p.79): transport properties (D, k, h, hₘ, Xₑ) — the Technical Data inputs of Ch.5's spreadsheet.
- Ch.4 §4.5 (p.98): drying constant K → becomes t_c in T10.5 here.
- Ch.4 §4.6 (p.100): sorption isotherm / GAB → becomes Xₑ source (T10.3, Oswin) here.
- Ch.3 (p.51): mass/energy balances and simulators — the conceptual parent of the Ch.5 spreadsheet.
- Ch.6 (p.135): indirect (contact) dryers — an alternative dryer class you can model in the same Ch.5 architecture by swapping T10.x equations.
- Part II (p.134): "Description of Various Dryer Types" — the catalog you size using this chapter's tool.


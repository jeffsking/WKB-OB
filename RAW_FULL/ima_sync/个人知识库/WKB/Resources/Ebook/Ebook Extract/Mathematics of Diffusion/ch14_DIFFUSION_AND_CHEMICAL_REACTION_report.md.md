---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_35c9ab49683e012a0f5731d0ce38b820001a693ee6c0644e"
source_file: "ch14_DIFFUSION_AND_CHEMICAL_REACTION_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch14_DIFFUSION_AND_CHEMICAL_REACTION_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch14_DIFFUSION_AND_CHEMICAL_REACTION_report.md.md

# Chapter 14 — Diffusion and Chemical Reaction 深度拆解报告

## 模块 1：本章核心内容概览

定位：扩散 + 化学反应耦合——SAP 交联网络中"水被固定化"、湿巾中抗菌剂缓释、芯体中酶/化学剂扩散反应等场景的理论框架。

### 核心观点/结论

观点 1：瞬时线性反应 → 等效 D_eff = D/(R+1)。
- 页码：p.327（§14.2）
- 原文摘选："S = RC… dC/dt = D/(R+1) d²C/dx²… the effect of the instantaneous reaction is to slow down the diffusion process."
- 业务解读：SAP 交联网络吸水——水被"固定化"在凝胶网络中（S = 固定量，R = 固定/自由比），等效 D 下降 (R+1) 倍。这是 SAP 吸水"慢"的分子尺度原因之一。

观点 2：非线性等温线 S = R Cⁿ → 等效 D_eff(C)。
- 页码：p.328（§14.2.1）
- 原文摘选："if n is fractional, e.g. as in the well-known Freundlich type of adsorption isotherm, then the effective diffusion coefficient… increases as the concentration S is increased. If on the other hand n > 1, the effective diffusion coefficient decreases as the concentration is increased."
- 业务解读：SAP 吸水的非线性"表观加速"——若 n<1（Freundlich 型），等效 D 随含水率上升，对应 SAP 后期吸液加速；若 n>1，等效 D 下降，对应"吸水饱和减速"。

观点 3：一级不可逆反应 → 稳态浓度指数衰减。
- 页码：p.335–336（§14.3.2）
- 原文摘选："C/C₀ = exp(−x√(k/D))… the rate of sorption and the concentration at any point tend to steady values"
- 业务解读：湿巾中抗菌剂缓释——抗菌剂从湿巾纤维扩散到皮肤，同时被细菌消耗（一级反应），有效浓度沿扩散距离指数衰减。

观点 4：一级可逆反应 → 完全解析解（Wilson 1948, Crank 1948c）。
- 页码：p.338（§14.4）
- 原文摘选："The most general case for which formal mathematical solutions have so far been obtained is that in which the reaction is first-order and reversible."
- 业务解读：SAP 中水的"物理吸附-脱附"平衡（可逆），给出稳态通量与浓度的完整解析描述。

观点 5：稳态解可用 Laplace 变换从非稳态解直接得到。
- 页码：p.337（§14.3.3）
- 原文摘选："On putting t → ∞ in (14.13) and (14.21) we find… The expressions on the right-hand sides of these equations are the Laplace transforms of C₁ and F₁ respectively."
- 业务解读：稳态浓度分布 = 非稳态解的 Laplace 变换在 p=k 处的值——计算捷径。

## 模块 2：研究方法与数据来源

- 数学方法：

- 等效 D 方法（§14.2 线性反应）
- 变量替换 + 级数解（§14.3 不可逆）
- Wilson-Crank 完全解（§14.4 可逆）
- Laplace 变换（§14.3.3 稳态）
- 实验数据：引用 Crank 1948b, Crank & Godson 1947, Standing-Warwicker-Willis 1948, Wilson 1948, Danckwerts 1951。
- 局限性：

- 一级反应假设（SAP 中水-凝胶相互作用可能非线性）；
- 不处理多步反应（酶催化等）；
- 不处理反应热（需 Ch 15）。
## 模块 3：论证过程

推导链（线性瞬时反应）：
1. 质量守恒：∂(C+S)/∂t = D ∂²C/∂x²；
2. 线性等温：S = RC；
3. 代入：∂C/∂t(1+R) = D ∂²C/∂x² → ∂C/∂t = [D/(1+R)] ∂²C/∂x²；
4. 结论：等效 D_eff = D/(1+R)。

推导链（非线性 Freundlich 型）：
1. S = R Cⁿ；
2. ∂(C + RCⁿ)/∂t = D ∂²C/∂x²；
3. 若 RCⁿ >> C（n 接近 1）：nRCⁿ⁻¹ ∂C/∂t = D ∂²C/∂x²；
4. D_eff = D/(nRCⁿ⁻¹)，依赖 C。

推导链（一级不可逆）：
1. ∂C/∂t = D ∂²C/∂x² − kC；
2. 变量替换 C = e^(−kt)u → u 满足 Laplace 变换方程；
3. 解：C/C₀ = exp(−x√(k/D))（稳态）。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 1–7 的扩散框架、Ch 8 数值方法。
- 后续影响：

- Ch 15 湿热耦合中"反应热"项即本章化学反应的推广；
- SAP 交联网络吸水、湿巾抗菌缓释均引用本章。
## 模块 5：亮点与不足

- 亮点：

- 等效 D 方法简洁直观；
- 非线性等温线的 Freundlich 型与 SAP 实验吻合；
- Laplace 变换捷径。
- 不足：

- 一级反应假设过于简化；
- 未处理酶催化、自催化、多步反应；
- 不讨论反应对介质结构的影响（SAP 溶胀本身改变 D）。
## 模块 6：关键术语与公式

|||
|---|---|
|Instantaneous reaction|"reaction proceeds very rapidly compared with the diffusion process" (p.327)|
|Linear adsorption isotherm|S = RC (p.327)|
|Freundlich isotherm|S = RCⁿ, n (p.328)|

核心公式：
- 线性瞬时反应：∂C/∂t = D/(R+1) · ∂²C/∂x²  (14.3)
- 非线性：D_eff = D/(1 + nRCⁿ⁻¹)  (14.5)
- 一级不可逆稳态：C = C₀ exp(−x√(k/D))  (14.49)
- 一级不可逆稳态通量：F = C₀√(kD)  (14.50)

无量纲参数：Da = ka²/D（Damköhler 数，反应/扩散速率比）

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|等效 D_eff = D/(R+1)|§14.2|p.327|线性反应的核心结论|高|
|Freundlich 型 D_eff(C)|§14.2.1|p.328|非线性反应等效 D|高|
|稳态指数衰减 (14.49)|§14.3.2|p.335|抗菌剂缓释模型|高|

## 模块 8：段落级微观精读

### 关键段落：§14.2 线性瞬时反应（p.327）

"In the simplest case, the concentration S of immobilized substance is directly proportional to the concentration C of substance free to diffuse, i.e. S = RC."
- 句子功能：线性等温假设
- 关键词：directly proportional
- 业务对应：SAP 中水与凝胶网络的"物理固定"

"When diffusion is accompanied by absorption, the usual equation for diffusion in one dimension has to be modified to allow for this, and becomes ∂C/∂t = D ∂²C/∂x² − ∂S/∂t."
- 句子功能：修改 PDE
- 关键词：modified
- 论证技术：质量守恒扩展

"which is seen to be the usual form of equation for diffusion governed by a diffusion coefficient given by D/(R+1). Clearly the effect of the instantaneous reaction is to slow down the diffusion process."
- 句子功能：核心结论
- 关键词：slow down
- 业务对应：SAP 吸水速率比"纯水扩散"慢 (1+R) 倍

业务关联总结：本章解释了 SAP 吸水"为什么慢"（等效 D 下降 (1+R) 倍）和湿巾抗菌剂"为什么缓释"（指数衰减稳态）。SAP 中水-凝胶相互作用若符合 Freundlich 型（n），则等效 D 随含水率上升——这与实测的 SAP D(C) 上升趋势一致（Ch 9 图 9.4）。湿巾功能化学品的缓释设计直接依赖式 (14.49-50)。


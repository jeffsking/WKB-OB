---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_e80f65eb4ab51704097abea6d9d45ab3001a693ee6c0644e"
source_file: "ch12_DIFFUSION_IN_HETEROGENEOUS_MEDIA_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch12_DIFFUSION_IN_HETEROGENEOUS_MEDIA_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch12_DIFFUSION_IN_HETEROGENEOUS_MEDIA_report.md.md

# Chapter 12 — Diffusion in Heterogeneous Media 深度拆解报告

## 模块 1：本章核心内容概览

定位：复合芯体（多层结构、层状/颗粒状介质）的扩散理论——直接对应纸尿裤芯体（顶表层+导流层+绒毛浆+SAP层+底膜）、湿巾（面层+无纺布层+功能涂层）。

### 核心观点/结论

观点 1：层状介质稳态传质 → 串联阻力模型。
- 页码：p.267–268（§12.2(i)）
- 原文摘选："1/R_L = 1/R_L1 + 1/R_L2 + ⋯ + 1/R_Ln = Σ P_i = Δp"（式 12.4）
- 业务解读：芯体总传质阻力 = 各层阻力之和——与 Ch 4 §4.2.3 的复合膜完全一致，但推广到 v=1,2,3 维（片/柱/球壳）：
  - 片层：Σ(lᵢ/Pᵢ) = l/P_total
  - 圆柱壳：Σ(ln(Rᵢ/Rᵢ₋₁)/Pᵢ) = ln(R_n/R₀)/P_total
  - 球壳：Σ((1/Rᵢ₋₁ − 1/Rᵢ)/Pᵢ) = (1/R₀ − 1/R_n)/P_total

观点 2：层状介质 D(C) 情形需积分扩散系数 D̄ᵢ。
- 页码：p.268（§12.2(i)）
- 原文摘选：D̄ᵢ = (1/(C₂ᵢ − C₂ᵢ₋₁)) ∫_{C₂ᵢ₋₁}^{C₂ᵢ} Dᵢ dC （12.7a）
- 业务解读：芯体各层 D 若依赖浓度，需用 Barrer 积分定义各层 D̄ᵢ 后再求串联——SAP 层 D̄ 强烈依赖含水率，这是芯体吸水速率非线性的重要来源。

观点 3：层状介质时间滞后有通用公式。
- 页码：p.269–270（§12.2(ii)）
- 原文摘选：L = ½ Σ [(lᵢ)²/D̄ᵢ] × 修正因子（12.15，Ash et al. 1965）
- 业务解读：芯体整体时间滞后 = 各层 Lᵢ 的加权组合——可用于芯体整体吸水动力学的解析估算。

观点 4：颗粒状介质（乳液/多相分散）的有效扩散系数需修正。
- 页码：p.274–276（§12.3）
- 原文摘选：Maxwell (1972) 公式——离散粒子在连续介质中，有效 D_eff = D_m · (2D_m+D_p)/(2D_p+D_m)（Maxwell 等效模型）
- 业务解读：SAP 颗粒在绒毛浆中的有效扩散——绒毛浆（D_m）连续介质中分散 SAP 颗粒（D_p，通常 D_p > D_m），Maxwell 公式给出 D_eff 的上限/下限估计。

观点 5：层间界面阻力可包含在模型中。
- 页码：p.268（§12.2 讨论 Ash-Bauer-Palmer 1965）
- 业务解读：芯体层间压和不充分润湿引入界面接触电阻 R_contact——这是"防回渗"层间设计的核心参数。

## 模块 2：研究方法与数据来源

- 数学方法：

- 串联阻力公式（§12.2）
- Maxwell 等效介质理论（§12.3）
- Jaeger Laplace 变换法（§12.2 时间滞后）
- Frisch 方法（§12.2）
- 实验数据：引用 Ash-Bauer-Palmer 1965, Ash-Barrer-Petropoulos 1963, Barrie et al. 1963, Jaeger 1950 的方法论文献。
- 局限性：

- 层状假设排除颗粒状复合（SAP 颗粒在浆层中）；
- Maxwell 模型假设球形、均匀分散、稀浓度；
- 未讨论层间界面化学（湿巾涂层-纤维界面）。
## 模块 3：论证过程

推导链（层状稳态）：
1. 第 i 层通量 Fᵢ = Pᵢ·ΔCᵢ/lᵢ；
2. 稳态 F₁ = F₂ = … = Fₙ = F；
3. Σ(lᵢ/Pᵢ)·F = ΣΔCᵢ = ΔC_total → P_total = l/Σ(lᵢ/P�_i)；
4. 推广到 D̄ᵢ（Barrer 积分）情形。

推导链（Maxwell）：
1. 假设球形粒子均匀分散；
2. 求解粒子外部的 Laplace 方程（稳态）；
3. 匹配边界条件 → D_eff = D_m·(2D_m+D_p)/(2D_p+D_m)（稀浓度极限）。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 4（复合膜）、Ch 10（时间滞后）、Ch 2（Laplace 变换）。
- 后续影响：

- Ch 15 湿热耦合在多层介质中的推广；
- SAP 复合材料（SAP+绒毛浆）的 D_eff 估算。
## 模块 5：亮点与不足

- 亮点：

- 串联阻力公式通用（片/柱/球壳）；
- Maxwell 等效模型给出颗粒复合的解析 D_eff；
- 时间滞后公式直接可应用于芯体。
- 不足：

- Maxwell 模型仅适用于球形稀浓度；
- 层间界面阻力未形式化；
- 未讨论动态边界（SAP 溶胀导致层厚变化）。
## 模块 6：关键术语与公式

|||
|---|---|
|Laminates|"layers of different properties sandwiched together" (p.267)|
|Particulates|"discrete particles of one phase are dispersed in a continuum of another" (p.267)|
|Maxwell's formula|颗粒复合有效扩散系数 (p.274–276)|

核心公式：
- 片层串联：Σ(lᵢ/Pᵢ) = l/P_total  (12.6)
- 圆柱壳：Σ(ln(Rᵢ/Rᵢ₋₁)/Pᵢ) = ln(R_n/R₀)/P_total  (12.6)
- 球壳：Σ((1/Rᵢ₋₁−1/Rᵢ)/Pᵢ) = (1/R₀−1/R_n)/P_total  (12.6)
- 积分扩散系数：D̄ᵢ = (1/ΔCᵢ) ∫Dᵢ dC  (12.7a)
- Maxwell 等效：D_eff = D_m·(2D_m+D_p)/(2D_p+D_m)

无量纲参数：D_p/D_m（颗粒/基质扩散系数比）；体积分数 φ

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|串联阻力公式 (12.4)|§12.2|p.268|多层芯体建模|高|
|Maxwell 等效公式|§12.3|p.274–276|颗粒复合 D_eff|高|
|层状时间滞后 (12.15)|Ash et al. 1965|p.270|芯体 L 估算|高|

## 模块 8：段落级微观精读

### 关键段落：§12.2 层状稳态（p.267–268）

"In the steady state, the flow through the i-th lamina is the same as for any other lamina and is given by F = −ωᵣ^(v−1) Dᵢ dCᵢ/dr."
- 句子功能：通量守恒陈述
- 关键词：steady state, same
- 论证技术：稳态连续性

"It follows immediately that 1/R_L = 1/R_L1 + 1/R_L2 + ⋯ = Σ Pᵢ = Δp"
- 句子功能：核心结果
- 关键词：sum of resistances
- 业务对应：芯体总阻力 = 各层阻力之和

"Barrer (1968) draws attention to an important property of a laminate in which the diffusion coefficient of each lamina is a function of concentration… D̄ᵢ = (1/(C₂ᵢ−C₂ᵢ₋₁)) ∫Dᵢ dC."
- 句子功能：推广到 D(D) 情形
- 关键词：function of concentration
- 业务对应：SAP 层 D̄ 的 Barrer 积分定义

业务关联总结：本章是复合芯体设计的核心理论。
- 芯体总阻力 = 各层串联（式 12.6）→ 直接用于芯体吸液/防回渗设计；
- SAP 颗粒在绒毛浆中的 D_eff 用 Maxwell 公式估算；
- 层间界面阻力（R_contact）需作为附加项加入模型；
- 时间滞后 (12.15) 给出芯体整体吸水速率的解析估算。

设计优化方向：降低 SAP 层的 l/D̄（核心吸水层）+ 提高导流层的 P（快速横向展布）+ 降低界面 R_contact（改善层间接触）。


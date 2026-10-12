---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_de455b84e104d43ca9ec15313fe03fb3001a693ee6c0644e"
source_file: "ch04_DIFFUSION_IN_A_PLANE_SHEET_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch04_DIFFUSION_IN_A_PLANE_SHEET_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch04_DIFFUSION_IN_A_PLANE_SHEET_report.md.md

# Chapter 4 — Diffusion in a Plane Sheet 深度拆解报告

## 模块 1：本章核心内容概览

定位：一维有限域（两片平行平面 x=0 与 x=l 之间）扩散问题——这是纸尿裤芯体层、湿巾、SAP 片层、复合膜的最直接对应几何。时间滞后法（time lag）在此章正式建立，是 SAP/纸尿裤行业测量 D 的核心实验方法。

### 核心观点/结论

观点 1：稳态下片层中浓度线性分布，通量 F = D(C₁−C₂)/l。
- 页码：p.44–45（§4.2）
- 原文摘选："F = −D dC/dx = D(C₁ − C₂)/l"（eqn 4.4）
- 业务解读：芯体顶层到 PP 底膜的水蒸气稳态透过率直接由该公式给出；多层片层（顶表层 + 导流层 + SAP 层 + 底膜）可视为串联电阻，总 R = Σ(lᵢ/Dᵢ)。

观点 2：渗透常数 P = DS，是 D 与溶解度的乘积。
- 页码：p.46（§4.2.1）
- 原文摘选："If the diffusion coefficient is constant, and if the sorption isotherm is linear… P = DS."
- 业务解读：湿巾/纸尿裤防回渗层的"水蒸气透过率"（MVTR）与"水液态阻隔率"差异本质是 P 的不同（DS 中的 S 由材料亲/疏水性决定）。

观点 3：复合膜总阻力是各层阻力之和。
- 页码：p.47（§4.2.3）
- 原文摘选："the resistance to diffusion of the whole membrane is simply the sum of the resistances of the separate layers"
- 业务解读：芯体多层结构（顶表层/纺粘导流层/绒毛浆/SAP 层/PP 底膜）的总传质阻力 = Σ(lᵢ/Dᵢ)——这是芯体吸水速率/防回渗能力建模的基础公式。

观点 4：时间滞后 L = l²/6D（恒 D 情形）。
- 页码：p.51–52（§4.3.3）
- 原文摘选："L = l²/6D … Following Daynes (1920), Barrer (1951) has used (4.26) as the basis of a method for obtaining the diffusion constant"
- 业务解读：这是 SAP 与纤维材料 D 测量的行业标准方法——测出湿流稳态段的 t 轴截距 L，除以 6/l² 得 D。纸尿裤行业"有效扩散系数"测量普遍基于此。

观点 5：非稳态解 Mt/M∞ 有级数形式（大 t）和 √t 形式（小 t）。
- 页码：p.48（§4.3.2）
- 原文摘选：Mt/M∞ = 1 − (8/π²) Σ [1/(2n+1)²] exp{−D(2n+1)²π²t/4l²}（eqn 4.18）
- 业务解读：SAP 片层吸液曲线的"初期 √t 段"（未饱和前沿未到达反侧）与"末期指数趋近段"（饱和扩散波衰减）由两个公式分别描述。

## 模块 2：研究方法与数据来源

- 数学推导方法：

- 稳态：直接积分；
- 非稳态：分离变量法（三角级数）、Laplace 变换、Hankel 变换；
- 时间滞后法（Daynes-Barrer）——从非稳态通量曲线的渐近线性段外推 t 轴截距。
- 实验数据来源：本章无直接实验数据，全部为解析解与文献引用（Barrer 1951, Daynes 1920, Carslaw & Jaeger 1959, Jenkins et al. 1970 等）。
- 方法论局限：

- 恒 D 假设（SAP 在高度溶胀区间不成立）；
- 一维假设（芯体 MD/CD 差异需各向异性扩展）；
- 片层几何不处理 SAP 颗粒状离散结构。
## 模块 3：论证过程

核心方程推导逻辑链：
1. 稳态：∂²C/∂x² = 0 → C 线性 → F = D(C₁−C₂)/l；
2. 引入蒸发边界（Robin 型）→ F = D(C₁−C₂)/(l+D/h)；
3. 浓度依赖 D：F = −D(C) dC/dx = const → 积分得 D̄ = (1/(C₁−C₂)) ∫_{C₂}^{C₁} D dC（Barrer 均值）；
4. 复合膜：n 层串联 → 1/F = Σ(lᵢ/(Dᵢ·ΔCᵢ))；
5. 非稳态：C(x,t) = Σ Aₙ sin(nπx/l) exp(−Dn²π²t/l²)（分离变量）；
6. 时间滞后：稳态 Q(t) 曲线的渐近线 → t 轴截距 = l²/6D。

关键假设：D 恒定、片层无限宽（一维）、表面浓度给定或线性 Robin 型。

边界条件：Dirichlet（C=const）、Robin（蒸发）、Neumann（不透）。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 1 PDE、Ch 2 分离变量/Laplace 方法。
- 后续影响：

- Ch 10 §10.6.2 时间滞后法详解；
- Ch 12 §12.2 层状介质直接推广本章公式；
- Ch 13 动边界、Ch 14 化学反应、Ch 15 湿热耦合均以此几何为基础。
## 模块 5：亮点与不足

- 亮点：

- 时间滞后法（L = l²/6D）简洁可操作，成为行业标准；
- 稳态+非稳态+复合膜三种情况体系完整；
- 明确给出 D̄ 的积分定义（Barrer 均值），为浓度依赖 D 提供测量基础。
- 不足：

- 线性浓度分布假设对 D(D) 不成立；
- 未讨论界面接触电阻（芯体层间压和、湿迁移的界面阻力）；
- 对"动态边界"（SAP 溶胀导致片层厚度变化）无处理。
## 模块 6：关键术语与公式

|||
|---|---|
|Steady state|"After a time, a steady state is reached in which the concentration remains constant at all points of the sheet" (p.44)|
|Permeability constant P|"the rate of transfer in the steady state… and the constant P is referred to as the permeability constant" (p.46)|
|Time lag L|"the intercept L is referred to as the 'time lag'" (p.52)|
|Composite membrane|"composite membrane composed of n sheets of thicknesses l₁, l₂, …, lₙ, and diffusion coefficients D₁, D₂, …, Dₙ" (p.47)|

核心公式：
- 稳态通量：F = D(C₁ − C₂)/l  (4.4, p.45)
- 渗透常数：P = DS  (4.7, p.46)
- Barrer 平均扩散系数：D̄ = (1/(C₁−C₂)) ∫_{C₂}^{C₁} D dC  (4.11)
- 复合膜串联：Σ(lᵢ/Dᵢ) = l/D̄  (4.12)
- 非稳态通量：Mt/M∞ = 1 − (8/π²) Σ[1/(2n+1)²] exp{−D(2n+1)²π²t/4l²}  (4.18)
- 时间滞后：L = l²/6D  (4.26)

无量纲参数：T = Dt/l², X = x/l, c = C/C₀  (4.21)

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|L = l²/6D 推导|Daynes 1920, Barrer 1951|p.51–52|D 测量的实验方法学基础|高——被行业 70 年验证|
|复合膜串联阻力公式 (4.12)|§4.2.3|p.47|多层芯体建模|高|
|非稳态通量级数 (4.24)|§4.3.3|p.52|稳态过渡的动态行为|高|
|Holstein 小 t 近似 (4.27)|Rogers et al. 1954|p.52|早期吸液速率|高|

## 模块 8：段落级微观精读

### 关键段落：§4.3.3 时间滞后法的建立（p.51–52）

"By integrating then with respect to t, we obtain the total amount of diffusing substance Q_t which has passed through the membrane in time t."
- 句子功能：方法学转换（从瞬时通量到累积量）
- 关键词：Q_t, total amount
- 论证技术：积分累积

"which, as t → ∞, approaches the line Q_t = (D(C₁ − C₂)t)/l − l²(C₁ − C₂)/(6D). This has an intercept L on the t-axis given by L = l²/6D."
- 句子功能：核心结果陈述
- 关键词：intercept, t-axis
- 论证技术：渐近线性外推
- 业务对应：SAP 时间滞后测量法核心公式

"Following Daynes (1920), Barrer (1951) has used (4.26) as the basis of a method for obtaining the diffusion constant, the permeability constant, and the solubility of a gas by analysing stationary and non-stationary flow through a membrane."
- 句子功能：方法学应用归因
- 关键词：Daynes, Barrer
- 论证技术：历史引用 + 方法论确立

"To within the accuracy of plotting the steady state is achieved when Dt/l² = 0.45 approximately."
- 句子功能：经验判据
- 关键词：steady state, Dt/l² = 0.45
- 业务对应：判断 SAP 吸水实验何时进入稳态段（D·t/l² > 0.45）

业务关联总结：本章是纸尿裤芯体设计的"公式库"。芯体多层阻力的计算、SAP D 值的时间滞后测量法、湿巾均匀性的判据（Dt/l² > 0.45 达到稳态）、复合膜 MVTR 的 P = DS 公式——都在本章首次以标准形式给出。

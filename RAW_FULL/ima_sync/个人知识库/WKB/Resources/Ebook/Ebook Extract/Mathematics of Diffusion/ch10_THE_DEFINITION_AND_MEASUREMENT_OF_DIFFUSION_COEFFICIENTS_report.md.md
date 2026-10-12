---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_fe02e8ea37862f4ad6839ec3a0d99889001a693ee6c0644e"
source_file: "ch10_THE_DEFINITION_AND_MEASUREMENT_OF_DIFFUSION_COEFFICIENTS_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch10_THE_DEFINITION_AND_MEASUREMENT_OF_DIFFUSION_COEFFICIENTS_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch10_THE_DEFINITION_AND_MEASUREMENT_OF_DIFFUSION_COEFFICIENTS_report.md.md

# Chapter 10 — The Definition and Measurement of Diffusion Coefficients 深度拆解报告

## 模块 1：本章核心内容概览

定位：D 的定义体系 + 测量方法学的百科全书。涵盖参考系选择（体积/质量/溶剂固定）、稳态法、非稳态法、时间滞后法、动态法、D(C) 反演——SAP D 测量的行业标准方法全部在此。

### 核心观点/结论

观点 1：D 的定义依赖于参考系的选择。
- 页码：p.203–204（§10.1–10.2）
- 原文摘选："the diffusion coefficient is defined as the rate of transfer of the diffusing substance across unit area of a section, divided by the space gradient of concentration at the section. Thus… F = −D dC/dx"
- 业务解读：SAP 中水的 D 定义必须指定参考系——通常用"质量固定"（因 SAP 溶胀体积剧变），否则 D 值无法比较。

观点 2：二元体系中 D_A^V = D_B^V = D（体积固定参考系）。
- 页码：p.204（§10.2）
- 原文摘选："In order that (10.4) and (10.6) shall both be satisfied it follows that D_A^V = D_B^V, or else that V_A = 0 or V_B = 0. … This coefficient is familiar in the interdiffusion of gases… Its physical significance is considered later in §10.4."
- 业务解读：SAP（A）+ 水（B）的二元体系中"互扩散系数" D_V 唯一——无需分别定义 D_SAP 与 D_水，简化实验。

观点 3：时间滞后法 L = l²/6D 可推广到 D(D) 情形（Frisch 方法）。
- 页码：p.224–225（§10.6.2）
- 原文摘选："Frisch (1958) showed that from measurements of L and the steady-state flow F at different pressures, both the parameters in the D(C) functional relationship and the solubility coefficient can be found without resource to a separate measurement of solubility."
- 业务解读：SAP D(C) 实验测量的核心方法——测多组 (L, F) 于不同浓度/压力 → 同时反演 D(C) 参数与 S。

观点 4：时间滞后可分解为 Fickian 部分 + 非 Fickian 部分。
- 页码：p.227（§10.6.2 末段）
- 原文摘选："L(l) can be written as the sum of a 'Fickian' time lag L_F(l) and a 'non-Fickian' or 'time-dependent' contribution L_T which is independent of l."
- 业务解读：判断 SAP 是否"非菲克"的实验判据——若不同厚度 l 的 L 值与 l² 的关系偏离直线，截距 L_T ≠ 0 即存在非菲克行为。

观点 5：动态法（振动膜）给出 D 与 S 的联合测量。
- 页码：p.218（§10.6）
- 原文摘选："Evnochides and Henley conclude that a single experiment in which both Δ and ψ are measured suffices to determine both K and ξ."
- 业务解读：湿巾 MVTR 动态测量、SAP 快速 D 测试的替代方法——振动膜法同时得 K（溶解度）与 ξ（扩散参数）。

观点 6：化学势梯度 → 热力学 D_T 与动力学 D_0 分离。
- 页码：p.227（§10.6.2）
- 原文摘选："Petropoulos and Roussis (1967) introduce the gradient of chemical potential into the diffusion equation… D_T is the 'thermodynamic diffusion coefficient', and D_0 the corresponding kinetic coefficient."
- 业务解读：SAP 中水的"表观 D"是热力学驱动力（化学势梯度）与动力学摩擦（网链粘度）的乘积——高温/高含水率同时改变两者，需在建模中区分。

## 模块 2：研究方法与数据来源

- 数学方法：

- 稳态法（§10.6.1）
- 非稳态法（§10.6）
- 时间滞后法 Daynes-Barrer（§10.6.2）
- Frisch 推广到 D(C)
- 振动膜动态法（Evnochides-Henley）
- Ash-Barrer 稳态浓度分布反演（§10.6.1）
- 实验数据：引用 Barrer 1951, Frisch 1958–1962, Petropoulos & Roussis 1967, Ash & Barrer 1971 等方法论文献；无直接原始数据。
- 方法论的局限性与适用条件：

- 稳态法需长时间达到平衡，不适合慢扩散体系；
- 时间滞后法需线性边界条件；
- 动态法需假设线性响应（小振幅振荡）。
## 模块 3：论证过程

推导链（时间滞后法 Frisch 推广）：
1. 从 Ch 4 L = l²/6D（恒 D）出发；
2. 引入 D = D(C) → 时间滞后 L 依赖于浓度分布；
3. Frisch (1958) 给出 D = D₀exp(βC) 时的 L(C) 表达式 (10.86)；
4. L(l) = L_F(l) + L_T 分解 → 用多厚度测量分离 Fickian 与非 Fickian 贡献；
5. 用 ΔL = L_d − L_a = l(C₁²−C₂²)/2F 检验 Fickian 假设。

关键假设：
- 二元体系；
- 体积/质量守恒；
- 边界条件线性。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 4（时间滞后 L = l²/6D）、Ch 7（D(C)）、Ch 9（D(C) 图形结果）。
- 后续影响：

- Ch 11 非菲克扩散的实验判据（L_T 判据）；
- Ch 12 层状结构的时间滞后公式；
- Ch 15 湿热耦合 D 的测量需此框架。
## 模块 5：亮点与不足

- 亮点：

- 参考系讨论系统（体积/质量/溶剂固定）——解决"哪个 D"的歧义；
- Frisch 方法学（L_F + L_T 分解）是非菲克判据的核心；
- 稳态法（Ash-Barrer）给出浓度分布的反演方法。
- 不足：

- 未讨论现代方法（核磁共振 PFG、红外光谱原位测量、AFM 纳米滴）；
- 未涉及 SAP 具体参数；
- 动态法假设线性响应，对高度非线性 D(C) 需谨慎。
## 模块 6：关键术语与公式

|||
|---|---|
|Diffusion coefficient D|"the rate of transfer… divided by the space gradient of concentration" (p.203)|
|Volume-fixed frame|体积固定参考系 (p.203–204)|
|Mutual diffusion coefficient D_V|"the behaviour of a two-component system… may be described in terms of a single diffusion coefficient" (p.204)|
|Time lag L|L = l²/6D (p.205, 4.26)|
|Frisch time lag|L_F(l) + L_T (p.227)|
|Thermodynamic D_T|热力学扩散系数 (p.227)|

核心公式：
- Fick 定义：F = −D dC/dx  (10.1)
- 体积守恒：D_A^V V_A (dC_A/dx) + D_B^V V_B (dC_B/dx) = 0  (10.4)
- 时间滞后：L = l²/6D  (4.26, 10.6.2)
- Frisch 分解：L(l) = L_F(l) + L_T  (p.227)
- 吸/脱滞后差：δL = L_d − L_a = l(C₁²−C₂²)/2F  (10.92)

无量纲参数：D_T/D_0（热力学 vs 动力学比）

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|参考系选择论证|§10.2|p.203–204|D 定义的唯一性|高|
|Frisch L_F+L_T 分解|§10.6.2|p.227|非菲克实验判据|高|
|吸脱滞后差 δL (10.92)|§10.6.2|p.227|Fickian 假设检验|高|
|Ash-Barrer 稳态反演|§10.6.1|p.219–220|浓度分布重构|高|

## 模块 8：段落级微观精读

### 关键段落：§10.6.2 时间滞后的 Frisch 推广（p.224–227）

"Frisch (1958) showed that from measurements of L and the steady-state flow F at different pressures, both the parameters in the D(C) functional relationship and the solubility coefficient can be found without resource to a separate measurement of solubility."
- 句子功能：方法学突破陈述
- 关键词：without resource to a separate measurement
- 论证技术：联立方程法

"Thus in general L(l) can be written as the sum of a 'Fickian' time lag L_F(l) and a 'non-Fickian' or 'time-dependent' contribution L_T which is independent of l."
- 句子功能：核心判据建立
- 关键词：independent of l
- 业务对应：SAP 非菲克诊断——测不同厚度 SAP 片 L 值，若与 l² 偏离线性，截距即为 L_T

"So far, we have considered only the time lag measured at the 'downstream' boundary… Frisch (1962b) used his technique to obtain expressions for L(x) and in particular L(0) measured at the 'upstream' face of the membrane."
- 句子功能：方法学扩展
- 关键词：upstream, downstream
- 业务对应：芯体"入口端"vs"出口端"时间滞后差异——反映芯体内部浓度分布的非对称性

业务关联总结：本章是 SAP D 测量的行业标准方法大全。SAP 行业常用的方法：(1) 稳态透过法（Ch 4 §4.3.3）测 D̄；(2) 时间滞后法（Daynes-Barrer）测恒 D 近似；(3) Frisch 多厚度法测 D(C) 与非菲克诊断；(4) 吸脱滞后差法检验 Fickian 假设。湿巾 MVTR 测试、芯体防回渗评估均需此框架。

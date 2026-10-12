---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_cb2ccb28d5f2bdc6640aeaab7fa2d852001a693ee6c0644e"
source_file: "ch05_DIFFUSION_IN_A_CYLINDER_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch05_DIFFUSION_IN_A_CYLINDER_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch05_DIFFUSION_IN_A_CYLINDER_report.md.md

# Chapter 5 — Diffusion in a Cylinder 深度拆解报告

## 模块 1：本章核心内容概览

定位：柱坐标系下的扩散问题——对应纸尿裤中的圆柱状纤维（木浆纤维、纺粘纤维、涤纶纤维）、SAP 圆柱颗粒、湿巾纤维束；稳态解给出对数分布而非线性。

### 核心观点/结论

观点 1：柱坐标下稳态浓度分布是对数型，而非线性。
- 页码：p.70（§5.2）
- 原文摘选："The concentration distribution defined by (5.4) is not linear, as it is for the plane sheet."
- 业务解读：纤维轴向/径向水扩散在径向截面内呈 ln(r) 分布——这对解释纤维端部与中心水含量差异、湿巾纤维束内部均匀性至关重要。

观点 2：柱壁厚度对稳态传质率存在"最优点"（当 ah < 1 时）。
- 页码：p.70–71（§5.2）
- 原文摘选："if ah < 1 the rate first increases and later decreases, passing through a maximum when b = 1/h."
- 业务解读：纤维表面蒸发/传质系数 h 与内半径 a 决定最优纤维壁厚——可指导纺粘纤维直径设计以最大化芯体导流效率。

观点 3：非稳态解用 Bessel 函数（J₀）展开。
- 页码：p.72–73（§5.3）
- 原文摘选："C = Σ Aₙ J₀(αₙr/a) exp(−Dαₙ²t/a²), provided the αₙ are roots of J₀(αₙ) = 0."
- 业务解读：纤维内部水分分布的时间演化——用 Bessel 级数描述，可直接用于建模"单纤维吸液动力学"。

观点 4：小 t 近似用 erfc 表示，但收敛范围不如片层情形。
- 页码：p.74（§5.3.1）
- 原文摘选："Clearly these solutions are not as valuable as the corresponding ones for the plane sheet."
- 业务解读：纤维小 t 段的 √t 近似可用但精度有限——需数值解或有限元处理。

观点 5：有限体积搅拌液中的扩散有解析解。
- 页码：p.77（§5.3.3）
- 原文摘选：M_t/M_∞ = 4a(1+a) Σ exp(−Dqₙ²t/a²)/(qₙ(4a²+qₙ²))
- 业务解读：SAP 颗粒在有限体积尿液中的吸液动力学——α = A/(πa²) 是溶液体积与颗粒体积比，本公式直接给出 Mt/M∞ 曲线。

## 模块 2：研究方法与数据来源

- 数学方法：分离变量法 + Bessel 方程、Laplace 变换、稳态直接积分。
- 实验数据：无；引用 Carsten & McKerrow 1944、Williamson & Adams 1919 的数值表。
- 局限性：恒 D 假设；纤维实际为多孔弹性体，溶胀后几何变化需动边界处理（Ch 13）。
## 模块 3：论证过程

推导链：
1. ∂C/∂t = (D/r) ∂/∂r(r ∂C/∂r) 是柱坐标扩散 PDE；
2. 稳态：r² d²C/dr² + r dC/dr = 0 → C = A + B ln r；
3. 边界 C(r=a)=C₁, C(r=b)=C₂ → 确定 A,B；
4. 非稳态：分离变量 C = u(r)exp(−Dα²t) → Bessel 方程 r²u'' + ru' + α²r²u = 0；
5. 边界 C(r=a)=0 → J₀(αₙa)=0 → 本征值 αₙ；
6. 正交性求 Fourier-Bessel 系数。

关键假设：径向均匀、长柱（端效应忽略）、D 恒定。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 1 PDE、Ch 2 分离变量法、Bessel 函数知识。
- 后续影响：

- Ch 6 球体问题借鉴 Bessel → 球 Bessel 思路；
- Ch 10 §10.6.3 时间滞后法对圆柱的推广；
- Ch 12 §12.2 层状介质包含圆柱壳的推广公式。
## 模块 5：亮点与不足

- 亮点：

- 对数稳态分布揭示柱几何的独特性质；
- ah 参数控制的最优壁厚结果具有直接工程意义；
- 有限体积解（5.33）可直接用于 SAP 吸液实验。
- 不足：

- 纤维实际存在孔隙与表面粗糙度，本模型过于理想；
- 恒 D 假设对湿纤维（D 随含水率剧烈变化）不适用；
- 柱端效应被忽略，但对短纤维（如绒毛浆）需考虑。
## 模块 6：关键术语与公式

|||
|---|---|
|Cylinder|"a long circular cylinder in which diffusion is everywhere radial" (p.70)|
|Bessel's equation of order zero|r²u'' + ru' + α²r²u = 0 (p.72)|
|Surface evaporation condition|dC/dr + h(C−C₂) = 0 at r = b (p.70)|

核心公式：
- 稳态浓度分布：C = [C₁ ln(b/r) + C₂ ln(r/a)] / ln(b/a)  (5.4)
- 稳态通量：Q_t = 2πDt(C₁−C₂)/ln(b/a)  (5.5)
- 非稳态解（小 t 表面恒定）：Mt/M∞ = 1 − Σ4/(αₙ²) exp(−Dαₙ²t/a²)
- 有限体积解：M_t/M_∞ = 4a(1+a) Σ exp(−Dqₙ²t/a²)/(qₙ(4a²+qₙ²))

无量纲参数：Dt/a², r/a

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|对数稳态分布 (5.4)|§5.2|p.70|揭示柱几何特性|高|
|ah 参数最优壁厚判据|§5.2|p.71|指导纤维直径设计|高|
|有限体积解 (5.33)|Wilson 1948|p.77|SAP 吸液实验直接应用|高|

## 模块 8：段落级微观精读

### 关键段落：§5.2 稳态圆柱（p.70–71）

"If the medium is a hollow cylinder whose inner and outer radii are a and b respectively, and if the diffusion coefficient is constant, the equation describing the steady-state condition is r²d²C/dr² + rdC/dr = 0."
- 句子功能：稳态 PDE 陈述
- 关键词：hollow cylinder, inner and outer radii
- 论证技术：从 PDE 出发

"The general solution of this is C = A + B ln r, where A and B are constants to be determined from the boundary conditions at r = a, r = b."
- 句子功能：通解形式
- 关键词：ln r
- 论证技术：直接积分

"The concentration distribution defined by (5.4) is not linear, as it is for the plane sheet."
- 句子功能：与 Ch 4 对比
- 关键词：not linear
- 业务对应：湿巾纤维束内部水分布不均匀

"it is easily seen that if ah > 1 the rate of diffusion decreases steadily as b increases from a, but if ah < 1 the rate first increases and later decreases, passing through a maximum when b = 1/h."
- 句子功能：关键判据
- 关键词：maximum, b = 1/h
- 论证技术：微分求极值
- 业务对应：纤维外径设计

业务关联总结：本章直接对应纸尿裤中的"纤维"单元——木浆纤维（径向吸液）、纺粘纤维（非织造布湿迁移）、涤纶纤维（干爽层）。SAP 圆柱颗粒的非稳态吸液、有限体积下的 Mt/M∞ 曲线、纤维最优直径（ah 判据）均可由本章公式给出。湿巾纤维束的径向均匀性由对数分布解释。


---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_e718fa0d0f987e02ba95075b56072f60001a693ee6c0644e"
source_file: "ch06_DIFFUSION_IN_A_SPHERE_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch06_DIFFUSION_IN_A_SPHERE_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch06_DIFFUSION_IN_A_SPHERE_report.md.md

# Chapter 6 — Diffusion in a Sphere 深度拆解报告

## 模块 1：本章核心内容概览

定位：球坐标系扩散——SAP 颗粒的核心几何模型（SAP 通常为粒径 0.2–2 mm 的不规则球体），是本书对纸尿裤行业最直接的几何模型章。

### 核心观点/结论

观点 1：球坐标 PDE 通过 u = Cr 变换可化为一维线性 PDE。
- 页码：p.90（§6.1）
- 原文摘选："On putting u = Cr, (6.1) becomes ∂u/∂t = D ∂²u/∂r². Since this is the equation for linear flow in one dimension, the solutions of many problems in radial flow in a sphere can be deduced immediately from those of the corresponding linear problems."
- 业务解读：SAP 溶胀动力学模型的关键数学技巧——把球坐标问题映射到片层一维问题，直接借用 Ch 4 的所有解。

观点 2：球体稳态解 C = B + A/r，与柱的 ln(r) 解结构相似。
- 页码：p.90–91（§6.2）
- 原文摘选："the general solution is C = B + A/r"
- 业务解读：SAP 稳态吸液梯度在球内呈 1/r 分布，球心浓度最高——解释 SAP 颗粒"芯部最后饱和"的实验观察。

观点 3：非稳态解用正弦级数，球心浓度有简化式 (6.19)。
- 页码：p.91（§6.3.1）
- 原文摘选："(C−C₁)/(C₀−C₁) at r=0 = 1 + 2 Σ(−1)ⁿ exp(−Dn²π²t/a²)"
- 业务解读：SAP 颗粒球心浓度随时间的演化——可直接用于评估"颗粒饱和程度"。

观点 4：ah 判据推广为 ah < 2 时传质率有最优 b = 2/h。
- 页码：p.91（§6.2）
- 原文摘选："If ah > 2, the rate of diffusion decreases steadily as b increases, but if ah < 2 the rate first increases and later decreases, passing through a maximum when b = 2/h."
- 业务解读：SAP 涂层/包膜厚度设计——当表面传质系数 h 与核半径 a 满足 ah，存在最优涂层厚度。

观点 5：有限体积球形吸液有解析 Mt/M∞ 表达式。
- 页码：p.92（§6.3.3）
- 原文摘选：M_t/M_∞ = 1 − (6/π²) Σ [1/n² · (1+3α)/(1+3αn²) · exp(−Dn²π²t/a²)]
- 业务解读：SAP 在有限尿液量中的吸水动力学标准公式——α 为体积比参数，可直接拟合实验 Mt-t 曲线得 D。

## 模块 2：研究方法与数据来源

- 数学方法：u=Cr 变换、分离变量（正弦级数）、Laplace 变换、有限体积边界（Wilson 1948）。
- 实验数据：无直接实验；引用 Carslaw & Jaeger 1959 p.235 的数值图。
- 局限性：恒 D、理想球体（实际 SAP 形状不规则）；溶胀导致 a 变化需动边界（Ch 13）。
## 模块 3：论证过程

推导链：
1. ∂C/∂t = (D/r²) ∂/∂r(r² ∂C/∂r) 是球坐标扩散 PDE；
2. u = Cr 代换 → ∂u/∂t = D ∂²u/∂r²（与片层 PDE 同形）；
3. 稳态：r² d²C/dr² + 2r dC/dr = 0 → C = B + A/r；
4. 非稳态：u 满足片层问题 → 正弦级数解；
5. 边界 u(r=0)=0, u(r=a)=aC₀ → sin(nπr/a) 本征函数。

关键假设：球对称、D 恒定、无对流。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 1–4 的片层解（通过 u=Cr 映射）、Ch 2 分离变量法。
- 后续影响：

- Ch 11 非菲克扩散中 SAP 的球体实验数据大量使用本章解作为参照；
- Ch 12 §12.2 层状介质包含球壳公式 (12.6)；
- Ch 13 动边界中 Stefan 问题（冰融化、SAP 凝胶-玻璃界面）用本章球体解。
## 模块 5：亮点与不足

- 亮点：

- u=Cr 变换是数学美感与实用性的完美结合；
- 有限体积解 (6.3.3) 直接对应 SAP 吸液实验；
- 球心浓度解析式简洁实用。
- 不足：

- SAP 颗粒不规则形状（棱角、裂纹）需修正；
- 溶胀过程 a 变化未考虑（需 Ch 13）；
- D 浓度依赖强烈（Ch 7、Ch 9）。
## 模块 6：关键术语与公式

|||
|---|---|
|Sphere|"cases in which the diffusion is radial" (p.90)|
|u = Cr substitution|球 → 线 的变换 (p.90)|

核心公式：
- 球坐标 PDE：∂C/∂t = (D/r²) ∂/∂r(r² ∂C/∂r)  (6.1)
- u=Cr 变换后：∂u/∂t = D ∂²u/∂r²  (6.3)
- 稳态通解：C = B + A/r  (6.5)
- 稳态通量：Q_t = 4πDtab(C₁−C₂)/(b−a)  (6.7)
- 非稳态（表面恒定）：(C−C₁)/(C₀−C₁) = (a/r) Σ[(−1)ⁿ/n sin(nπr/a)] exp(−Dn²π²t/a²)  (6.18)
- 球心简化：1 + 2 Σ(−1)ⁿ exp(−Dn²π²t/a²)  (6.19)
- 有限体积：M_t/M_∞ = 1 − (6/π²) Σ1/n² · (1+3α)/(1+3αn²) · exp(−Dn²π²t/a²)

无量纲参数：Dt/a², r/a

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|u=Cr 变换|§6.1|p.90|简化球坐标问题|高——关键数学技巧|
|球心简化式 (6.19)|§6.3.1|p.91|SAP 球心浓度演化|高|
|有限体积解 (6.3.3)|Wilson 1948|p.92|SAP 吸液动力学标准公式|高|

## 模块 8：段落级微观精读

### 关键段落：§6.1 u=Cr 变换（p.90）

"On putting u = Cr, (6.1) becomes ∂u/∂t = D ∂²u/∂r²."
- 句子功能：方法学转换（数学魔法）
- 关键词：u = Cr
- 论证技术：变量代换降阶

"Since this is the equation for linear flow in one dimension, the solutions of many problems in radial flow in a sphere can be deduced immediately from those of the corresponding linear problems."
- 句子功能：方法论意义陈述
- 关键词：immediately deduced
- 业务对应：SAP 问题 → 借用 Ch 4 片层解

### 关键段落：§6.3.1 球心简化（p.91）

"The concentration at the centre is given by the limit as r → 0, that is by (C−C₁)/(C₀−C₁) = 1 + 2 Σ(−1)ⁿ exp(−Dn²π²t/a²)."
- 句子功能：特例解析简化
- 关键词：limit, centre, r→0
- 论证技术：极限取法（用 sin(nπr/a)/(nπr/a)→1）
- 业务对应：SAP 颗粒中心吸水进度可直接测量

业务关联总结：本章是 SAP 颗粒建模的"主战场"。u=Cr 变换、球心简化式 (6.19)、有限体积公式 (6.3.3) 三件工具已足够支撑 SAP 吸水动力学的解析建模——只要假定恒 D（或分段恒 D）。实际 SAP 中 D(C) 强烈依赖（见 Ch 7、Ch 9），需数值解配合。


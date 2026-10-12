---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_a1db49790a2a091b465190edad44f6a7001a693ee6c0644e"
source_file: "ch09_SOME_CALCULATED_RESULTS_FOR_VARIABLE_DIFFUSION_COEFFICIENTS_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch09_SOME_CALCULATED_RESULTS_FOR_VARIABLE_DIFFUSION_COEFFICIENTS_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch09_SOME_CALCULATED_RESULTS_FOR_VARIABLE_DIFFUSION_COEFFICIENTS_report.md.md

# Chapter 9 — Some Calculated Results for Variable Diffusion Coefficients 深度拆解报告

## 模块 1：本章核心内容概览

定位：把 Ch 7 的方法论 + Ch 8 的数值方法具体应用到 D = D(C) 的实际问题，给出可直接查阅的图表——SAP D(C) 建模的核心参考章。

### 核心观点/结论

观点 1：稳态 D(D) 情形的浓度分布解析形式 F(C)。
- 页码：p.161（§9.1.1）
- 原文摘选："D₀∫{1+f(C)}dC = Ax + B … eqn (9.2) becomes C₁ + F(C₁) − C₂ − F(C₂) = Fl/D₀"
- 业务解读：SAP 稳态吸液梯度——D 随浓度增加则分布凸向浓度轴；D 随浓度减小则分布凹向浓度轴（Barrer 结论），这是 SAP 稳态水分布形态的判据。

观点 2：非稳态的"等效扩散系数"与积分定义。
- 页码：p.166–167（§9.2 图 9.4）
- 原文摘选：D/D₀ = 1 + 10(1−e^−2.303c) 等典型曲线形式
- 业务解读：SAP 实测 D(C) 常呈指数上升型（图 9.4 曲线 1）——对应高分子溶胀导致自由体积增加的物理图像。

观点 3：对数浓度线性分布（"溶剂固定"参考系）。
- 页码：p.167（§9.1.4 后段）
- 原文摘选："the gradient of the logarithm of concentration of the latter is linear and hence the concentration itself varies exponentially with distance"
- 业务解读：湿巾/芯体中"含水率"对数分布的解析基础——用于评估芯体横向湿分布均匀性。

观点 4：停止稳态流动后浓度分布的整体移动。
- 页码：p.169（§9.1.4 末段）
- 原文摘选："at the instant when A ceases to flow through, the whole concentration-distance distribution commences to move backwards at the velocity with which substance A previously passed through the membrane."
- 业务解读：芯体停止吸收后残留水的"逆流"——对应"防回渗"性能评估。

观点 5：水在含盐蒸气层中的扩散速率与溶质浓度成反比。
- 页码：p.168（§9.1.4）
- 原文摘选："the rate of transfer of B will be, to a first approximation, dependent on A·C_A only"
- 业务解读：纸尿裤使用场景下（尿液含盐分、有机物），芯体上方空气层中水蒸气的透过速率受溶质影响——指导防回渗气相层的材料选择。

## 模块 2：研究方法与数据来源

- 数学方法：Ch 7 Boltzmann 变换 + Ch 8 Crank-Nicolson 数值方法。
- 实验数据：无直接实验；引用 Barrer (1946) 的数值曲线。
- 局限性：仅一维、仅片层几何的图形结果；柱/球结果有限。
## 模块 3：论证过程

推导链：
1. 从 §9.1.1 稳态 ∂/∂x(D dC/dx) = 0 直接积分得 (9.2)；
2. 用 Barrer 函数 F(C) = ∫f(C)dC 表示积分结果；
3. 图 9.1/9.2 给出 6 种 f(C) 形式的典型曲线（线性、指数、幂次、衰减型）；
4. §9.1.2 讨论 D = D(x) 情形（空间依赖）；
5. §9.1.4 讨论双组分情形（体积固定参考系）；
6. §9.2 用 Ch 8 数值方法计算非稳态曲线。

关键假设：D 只依赖 C 或 x；片层几何；稳态或非稳态。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 7 Boltzmann 变换 + Ch 8 数值方法 + Ch 4 片层。
- 后续影响：

- Ch 11 非菲克扩散的 Case I 参考本章 D(C) 结果；
- Ch 13 动边界的两步 D 近似直接引用本章曲线。
## 模块 5：亮点与不足

- 亮点：

- 图形化结果可直接查阅，节省计算；
- Barrer F(C) 函数定义清晰；
- 双组分情形（§9.1.4）揭示反直觉结论（浓度分布的移动）。
- 不足：

- 图形结果有限（当时计算能力）；
- 无 SAP 具体参数案例；
- 未讨论温度与浓度的耦合 D(C,T)。
## 模块 6：关键术语与公式

|||
|---|---|
|Barrer's nomenclature F(C)|F(C) = ∫f(C')dC'  (p.161)|
|Volume-fixed frame|体积固定参考系下定义的扩散系数 D_V (p.166)|

核心公式：
- 稳态解：D₀∫{1+f(C)}dC = Ax + B  (9.2)
- 通量：F = −D̄(C₁−C₂)/l，D̄ = (1/(C₁−C₂)) ∫_{C₂}^{C₁} D dC  (9.19)
- 典型 D(C) 曲线：D/D₀ = 1 + 10(1−e^−2.303c), D/D₀ = e^(−2.303c), 等 (图 9.4)

无量纲参数：c = C/C₀（无量纲浓度）；F(C) 归一化值

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|Barrer F(C) 函数|§9.1.1|p.161|稳态 D(C) 解的参数化|高|
|图 9.1 六型 D(C) 曲线|Barrer 1946|p.161|定性对比不同 D(C) 形态|高|
|图 9.4 五种典型 D(C)|§9.2|p.170|非稳态数值计算输入|高|

## 模块 8：段落级微观精读

### 关键段落：§9.1.1 D = D(C) 的稳态解（p.161–162）

"If D is a given function of concentration, i.e. D = D₀{1+f(C)}, the general solution of (9.1) can be written as D₀∫{1+f(C)}dC = Ax + B."
- 句子功能：一般解形式
- 关键词：given function of concentration
- 论证技术：直接积分（因为稳态下 dC/dx 与 D 乘积为常数）

"They illustrate the general conclusion that when D increases as C increases the concentration-distance curves in the steady state are convex away from the distance axis; but when D decreases as C increases the curves are convex towards that axis."
- 句子功能：核心定性判据
- 关键词：convex away, convex towards
- 业务对应：SAP 稳态水分布形态的判断——D 随含水率上升时曲线凸，对应"前沿推进快、尾部稀疏"的实验观察

业务关联总结：本章是 SAP D(C) 建模的"图表面板"。实际 SAP 中 D(C) 随含水率上升 2–4 个数量级（指数型，类似图 9.4 曲线 1）——这解释了 SAP 吸水"初期慢、后期突然加速"的非线性动力学。芯体湿迁移的稳态梯度形状直接由本章曲线形态给出。Ch 8 数值方法 + Ch 9 图形 + Ch 7 Boltzmann 变换三件套构成 SAP 建模的完整工具链。


---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_9e2deef2995b0835634f3114c837a9bb001a693ee6c0644e"
source_file: "ch13_MOVING_BOUNDARIES_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch13_MOVING_BOUNDARIES_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch13_MOVING_BOUNDARIES_report.md.md

# Chapter 13 — Moving Boundaries 深度拆解报告

## 模块 1：本章核心内容概览

定位：SAP 溶胀前沿、Case II 湿前沿、Stefan 相变问题的统一数学框架。本章的动边界模型是 SAP 从干态到湿态过渡区（Ch 11 的 Case II/非菲克）的定量实现。

### 核心观点/结论

观点 1：动边界 = "不可逆瞬时固定反应"的数学等价。
- 页码：p.287–288（§13.1）
- 原文摘选："An essential feature of the idealized problem of diffusion accompanied by the instantaneous and irreversible immobilization of a limited number of the diffusing molecules is that a sharp boundary surface moves through the medium."
- 业务解读：SAP 溶胀前沿（凝胶-玻璃界面）正是这种"尖锐边界"——前沿后面是全湿凝胶（D 大），前面是干态玻璃（D≈0），边界以恒定或变速推进。

观点 2：动边界 = Stefan 相变问题。
- 页码：p.287（§13.1）
- 原文摘选："The same mathematical problem is presented by heat flow in a medium which undergoes a phase change at some fixed temperature… Such problems are often referred to as 'Stefan problems' after J. Stefan (1890)."
- 业务解读：SAP 溶胀前沿的数学结构 = 冰融化前沿的数学结构——可用成熟 Stefan 问题工具（erfc 解、守恒条件）处理。

观点 3：D 在临界浓度 C₁ 处不连续跳跃 → 动边界。
- 页码：p.288（§13.2.1）
- 原文摘选："over the concentration range C₂ > c > C₁ for which D is zero, the concentration gradient is infinite and there is no penetration into the sheet."
- 业务解读：SAP 在低含水率区 D≈0（玻璃态）→ 高含水率区 D↑↑（橡胶态）——两步 D(C) 近似直接给出动边界解析解。

观点 4：动边界守恒条件（Stefan 条件）。
- 页码：p.297（§13.3）
- 原文摘选："−D₁ dC/dx = C₁ dX/dt"
- 业务解读：SAP 溶胀前沿推进速度的核心公式——前沿通量 = 前沿固定浓度 × 前沿速度。这是 Case II "匀速前沿"的定量实现。

观点 5：两步 D(C) 模型可拟合连续 D(C) 曲线。
- 页码：p.298（§13.2.3 末段）
- 原文摘选："for any further extension to a three- or more step diffusion coefficient the numerical work would probably be prohibitive. However, the two-step form includes several interesting types of diffusion coefficient and by suitable choice of D₁, D₂, D₃ and C₁, C₂ a reasonable approximation to many continuously varying diffusion coefficients can be obtained."
- 业务解读：SAP D(C) 的"分段常数"近似——用两步或三步 D 值拟合实测 D(C) 曲线，即可获得解析动边界解，无需全数值解。

## 模块 2：研究方法与数据来源

- 数学方法：

- erfc 解析解（§13.2.2–13.2.3）
- Danckwerts 一般动边界理论（§13.4）
- 守恒条件（Stefan 条件）
- 实验数据：引用 Hartley 1946（聚合物中湿前沿显微镜观察）、Muehlbauer & Sunderland 1965（Stefan 问题综述）。
- 局限性：

- 尖锐边界是理想化（实际为连续过渡）；
- 反应假设为"瞬时不可逆"（实际有松弛时间）；
- 不处理多孔介质中的毛细力。
## 模块 3：论证过程

推导链（§13.2.2 单步 D 模型）：
1. D = D₁ (c > C₁)，D = 0 (c < C₁)；
2. 假设解形式 c = C₁ erfc(α/x/√t)/erfc(α/√(4D₁t))；
3. 边界 c(x=0)=C₁, c(x>X)=0；
4. 守恒条件：−D₁ ∂c/∂x|_{x=X} = C₁ dX/dt；
5. 得 α 的超越方程 → 数值求解 → X(t) = α√(4D₁t)。

推导链（§13.4 Danckwerts 一般理论）：
1. 两介质相对运动（如冰-水界面）；
2. 各自坐标系中的扩散方程 (13.40-41)；
3. 界面平衡关系 c₂(X₂) = Qc₁(X₁) + R (13.42)；
4. 界面守恒（质量/能量） → dX/dt 的耦合方程。

关键假设：D 为分段常数；边界浓度给定；无对流。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 2 误差函数解、Ch 11 Case II、Ch 7 D(C)。
- 后续影响：

- Ch 14 化学反应中的动边界（固定化反应）；
- Ch 15 湿热耦合的相变情形。
## 模块 5：亮点与不足

- 亮点：

- Stefan 问题框架与 SAP 溶胀直接对应；
- 两步 D 模型实用且解析可解；
- Danckwerts 一般理论数学严格。
- 不足：

- 尖锐边界假设过于简化（实际 SAP 前沿为渐变）；
- 不处理多孔介质毛细力（湿巾/纸尿裤中重要）；
- 无多相耦合（水蒸气-液态水-凝胶）。
## 模块 6：关键术语与公式

|||
|---|---|
|Stefan problem|"heat flow in a medium which undergoes a phase change at some fixed temperature" (p.287)|
|Sharp boundary|"a sharp boundary surface moves through the medium. It separates a region in which all the sites are occupied from one in which none of them are" (p.287)|
|Immobilizing reaction|不可逆固定反应 (p.297)|

核心公式：
- 单步 D 前沿位置：X(t) = α√(4D₁t)
- Stefan 守恒条件：−D₁ dC/dx|_{x=X} = C₁ dX/dt  (13.33 对应)
- 两步 D 常数确定：k₁, k₂ 满足两个超越方程 (13.38-39)

无量纲参数：α（Stefan 数，决定前沿位置）

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|动边界 = Stefan 问题|§13.1|p.287|方法学归类|高|
|Stefan 守恒条件|§13.3|p.297|前沿推进速度|高|
|两步 D 近似|§13.2.3|p.298|拟合连续 D(C)|高|

## 模块 8：段落级微观精读

### 关键段落：§13.1 引言（p.287–288）

"In one general class of problem some of the diffusing molecules are immobilized and prevented from taking further part in the diffusion process. This may be due to a chemical reaction… Alternatively, we may have a less specific type of adsorption on fixed sites."
- 句子功能：问题域定义
- 关键词：immobilized, adsorption on fixed sites
- 业务对应：SAP 凝胶网络"固定"吸水分子（化学交联）

"An essential feature of the idealized problem… is that a sharp boundary surface moves through the medium. It separates a region in which all the sites are occupied from one in which none of them are."
- 句子功能：核心特征陈述
- 关键词：sharp boundary, occupied, none
- 业务对应：SAP 溶胀前沿（凝胶 | 玻璃界面）

"The same mathematical problem is presented by heat flow in a medium which undergoes a phase change at some fixed temperature… Such problems are often referred to as 'Stefan problems' after J. Stefan (1890)."
- 句子功能：数学等价性建立
- 关键词：Stefan problems
- 论证技术：类比（扩散 ↔ 传热相变）

"The occurrence of a sharp boundary does not necessarily imply a chemical reaction. When a liquid penetrant diffuses into a polymer sheet or filament, sharp boundaries are frequently observed under a microscope."
- 句子功能：经验事实佐证
- 关键词：microscope, sharp boundaries
- 业务对应：SAP 溶胀前沿的显微镜观察（文献中有报道）

业务关联总结：本章是 SAP 溶胀动力学的定量核心。SAP 从干态（DR=0）到饱和（DR_max）的吸液过程：
1. 初期（DR<5）：Case II 匀速前沿（Stefan 条件 v = −D₁C₁/C₁ × √(D₁/t) 的渐近形式）；
2. 中期（DR 5–15）：非菲克过渡区（动边界 + 松弛耦合）；
3. 后期（DR>15）：Fickian 饱和（动边界消失，D 连续）。

工程意义：缩短 SAP 吸水"启动时间"（从接触水到前沿到达颗粒中心）→ 提高 SAP 颗粒溶胀前沿推进速度 v → 由 Stefan 条件 v = D₁∂C/∂x|_front / C₁ 指导——提高 D₁（橡胶态 D）或增大前沿浓度梯度。

---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_0cf157d2a933005f64ef5df6852c1d02001a693ee6c0644e"
source_file: "ch02_METHODS_OF_SOLUTION_WHEN_THE_DIFFUSION_COEFFICIENT_IS_CONSTANT_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch02_METHODS_OF_SOLUTION_WHEN_THE_DIFFUSION_COEFFICIENT_IS_CONSTANT_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch02_METHODS_OF_SOLUTION_WHEN_THE_DIFFUSION_COEFFICIENT_IS_CONSTANT_report.md.md

# Chapter 2 — Methods of Solution When the Diffusion Coefficient is Constant 深度拆解报告

## 模块 1：本章核心内容概览

定位：提供恒 D 情形下解析解的三套"工具箱"——反射与叠加法、分离变量法、Laplace 变换法，确立"两类标准解（误差函数类 vs 三角函数级数/Bessel 级数）"的分类体系。

### 核心观点/结论

观点 1：两类标准解的分工——小时间用误差函数，大时间用级数。
- 页码：p.12（§2.1）
- 原文摘选："Either it is comprised of a series of error functions or related integrals, in which case it is most suitable for numerical evaluation at small times… or it is in the form of a trigonometrical series which converges most satisfactorily for large values of time."
- 业务解读：SAP 吸液初期（小 t，未饱和前沿）用误差函数类解；稳态接近（大 t）用傅里叶级数；这是计算 SAP 吸液动力学曲线的两种算法分支。

观点 2：平面源格林函数是基本"砖块"。
- 页码：p.12（§2.2.1）
- 原文摘选："C = (M/2(πDt)^½) exp(−x²/4Dt), and this is therefore the solution which describes the spreading by diffusion of an amount of substance M deposited at time t = 0 in the plane x = 0."
- 业务解读：SAP 单个微球体可视为"瞬时点源"，多个 SAP 粒子的湿迁移场可通过该格林函数叠加得到。

观点 3：反射法利用线性方程的叠加性构造半无限域解。
- 页码：p.13（§2.2.2）
- 原文摘选："Since this equation is linear the sum of the two solutions is itself a solution… the condition to be satisfied at the impermeable boundary is dC/dx = 0, x = 0."
- 业务解读：芯体底层不透水膜（PP 底膜）对应 dC/dx=0 边界；顶表层（透湿）对应 dC/dx+hc=0 边界；反射法给出解析构造方式。

观点 4：Laplace 变换是最强工具。
- 页码：p.12（§2.1）
- 原文摘选："It is the most powerful of the three, particularly for more complicated problems."
- 业务解读：复合芯体多层结构的拉氏变换解析对湿迁移建模尤其关键。

## 模块 2：研究方法与数据来源

- 数学推导方法：解析法（反射、分离变量、Laplace 变换）；级数展开与 Fourier-Bessel 系数正交性计算。
- 实验数据来源：无实验数据，纯数学方法。
- 方法论的局限性与适用条件：

- 仅适用于恒 D 与线性边界条件（§2.1 声明）；
- 级数解收敛性依赖几何；
- 复杂几何（如 SAP 颗粒形状）需简化为一维/柱/球。
## 模块 3：论证过程

核心方程推导逻辑链：
1. 从恒 D 的一维 PDE ∂C/∂t = D ∂²C/∂x² 出发；
2. 试探解形式 C = A t^(-½) exp(−x²/4Dt) → 代入验证；
3. 利用总质量 M 守恒定出 A；
4. 用反射+叠加（线性叠加原理）构造边界解；
5. 推广到扩展初值分布（线源叠加 → 积分表达式，误差函数出现）；
6. 分离变量法：C = u(x) exp(−Dα²t)，得到 Bessel/三角本征值问题；
7. Laplace 变换：p 域 → 求像函数 → 逆变换给出时间域解。

关键假设：D 恒定、介质均匀、边界线性（Dirichlet/Neumann/Robin）。

边界条件类型：
- 第一类（Dirichlet）：C = const（§2.2.3、§2.3.2）
- 第二类（Neumann）：dC/dx = 0（不透）
- 第三类（Robin）：dC/dx + h(C−C₂)=0（蒸发/表面传质）

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 1 的扩散 PDE。
- 后续影响：

- Ch 3–6 全部应用本章三种方法在无限/半无限域与有限几何中求解；
- Ch 10 的时间滞后法建立在 §2.3.3 的拉氏变换框架上；
- Ch 12 层状结构中 Jaeger 的方法直接引用 §2.3 的 Laplace 变换。
## 模块 5：亮点与不足

- 亮点：

- 三类方法分工清晰（反射物理性最强、分离变量系统性最强、Laplace 通用性最强）；
- 反射法物理直观；
- 对 Bessel 级数解的正交性证明给出完整引用。
- 物理直觉与数学严谨性：反射法的物理图像极佳；但级数收敛域证明引用 Carslaw & Jaeger，未完全给出。
- 局限性：无非线性、无常数边界变化情形；实际芯体中边界浓度随时间变化（如 SAP 溶胀导致界面移动），需 Ch 13 动边界处理。
## 模块 6：关键术语与公式

|||
|---|---|
|Plane source|"describes the spreading by diffusion of an amount of substance M deposited at time t = 0 in the plane x = 0" (p.12)|
|Reflection at a boundary|通过 x=0 的对称反射叠加构造半无限域解 (p.13)|
|Separation of variables|C = u(x)exp(−Dα²t) 代入 PDE 分离出空间本征值问题 (p.17)|
|Laplace transform method|对时间做拉氏变换，像函数域求解，再逆变换 (p.12)|

核心公式：
- 瞬时平面源：C = M/[2(πDt)^(½)] exp(−x²/4Dt)  (2.6, p.12)
- 扩展初值（误差函数解）：C = (C₀/2)[erfc(x/2√(Dt)) + erfc((2l−x)/2√(Dt))]（§2.2.3）
- 反射法边界：dC/dx = 0 at x=0（不透）(2.8, p.13)
- 分离变量形式：C = Σ Aₙ sin(nπx/l) exp(−Dn²π²t/l²)

无量纲参数：Dt/l²（后续 §8.2 正式命名 T）；在 §2.2 中隐式使用 x²/4Dt。

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|瞬时平面源解析解 (2.6)|§2.2.1|p.12|验证试探解为 PDE 的解|高——直接可微分验证|
|反射法满足不透边界条件|§2.2.2|p.13|证明 dC/dx=0 在反射叠加后仍成立|高|
|分离变量法满足齐次 Dirichlet 边界|§2.3|p.17|通过 sin(nπx/l) 满足 C(x=0)=C(x=l)=0|高|

## 模块 8：段落级微观精读

### 关键段落：§2.2.2 Reflection at a boundary（p.13）

"If, however, we have a semi-infinite cylinder extending over the region x > 0 and with an impermeable boundary at x = 0, all the diffusion occurs in the direction of positive x."
- 句子功能：问题设定（情境化）
- 关键词：semi-infinite, impermeable boundary
- 逻辑关系：从对称问题过渡到不对称问题

"We can consider the solution for negative x to be reflected in the plane x = 0 and superposed on the original distribution in the region x > 0."
- 句子功能：方法论提出
- 关键词：reflected, superposed
- 论证技术：对称性构造法

"This procedure of reflection and superposition is mathematically sound, for reflection at x = 0 means the adding of two solutions of the diffusion equation. Since this equation is linear the sum of the two solutions is itself a solution"
- 句子功能：数学严谨性证明
- 关键词：linear, sum
- 论证技术：线性叠加原理应用

"Furthermore, the condition to be satisfied at the impermeable boundary is dC/dx = 0, x = 0, since this is the mathematical condition for zero flow across a boundary."
- 句子功能：物理条件→数学条件的翻译
- 关键词：zero flow, impermeable
- 业务对应：纸尿裤 PP 底膜、湿巾包装内壁

业务关联总结：本章是芯体建模的算法库。纸尿裤吸液速率的解析近似可基于 (2.6) 构造（SAP 单颗粒视为源）；多层芯体边界条件的设定直接依赖反射法。湿巾均匀性评价中的"湿扩散半时间"可由误差函数解反推 D。


---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_4a9ac3654ceef22cb6838d55204dd2c6001a693ee6c0644e"
source_file: "ch07_CONCENTRATION-DEPENDENT_DIFFUSION_METHODS_OF_SOLUTION_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch07_CONCENTRATION-DEPENDENT_DIFFUSION_METHODS_OF_SOLUTION_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch07_CONCENTRATION-DEPENDENT_DIFFUSION_METHODS_OF_SOLUTION_report.md.md

# Chapter 7 — Concentration-Dependent Diffusion: Methods of Solution 深度拆解报告

## 模块 1：本章核心内容概览

定位：D 不再是常数，而是浓度 C 的函数 D(C)——SAP 与湿巾高分子纤维在此章获得首个系统性数学处理。Boltzmann 变换是本章方法学核心。

### 核心观点/结论

观点 1：Boltzmann 变换 η = x/2√t 将 PDE 化为 ODE。
- 页码：p.106（§7.2.1）
- 原文摘选："Boltzmann (1894) showed that for certain boundary conditions, provided D is a function of C only, C may be expressed in terms of a single variable x/2√t… d²C/dη² + 2η d/dη(D dC/dη) = 0"
- 业务解读：SAP 吸液问题（D 强烈依赖浓度）的核心数学工具——把二阶 PDE 化为二阶 ODE，解析或数值可解。

观点 2：Boltzmann 变换的适用条件严格——初始/边界须可表为 η 的函数。
- 页码：p.107（§7.2.1）
- 原文摘选："It is only when the initial and boundary conditions are expressible in terms of η alone, and x and t are not involved separately, that the transformation (7.6)… can be used."
- 业务解读：对半无限 SAP 颗粒表面有效；对有限厚 SAP 片层（边界含 t）不直接适用，需数值方法。

观点 3：Crank-Henry 迭代积分法是求解 ODE 的数值方法。
- 页码：p.107（§7.2.2）
- 原文摘选："Crank and Henry (1949a,b) gave a method of solving (7.10)… based on iterative quadrature."
- 业务解读：SAP 实验测出浓度分布 C(x,t) 后，用 Crank 方法反推出 D(C) 函数——SAP D(C) 曲线的行业标准反演法。

观点 4：时间依赖 D(t) 可通过变量 T = ∫D(t')dt' 归约到恒 D 情形。
- 页码：p.105（§7.1）
- 原文摘选："on writing dT = D(t)dt… equation (7.1) reduces to dC/dT = D₀ d²C/dx²."
- 业务解读：温度变化导致 D 变化的场景（如热水洗涤/加温处理 SAP）可直接借用恒 D 解。

观点 5：非线性 D(C)（如指数、线性）有特定闭式解。
- 页码：p.108–114（§7.2.3, §7.2.4）
- 原文摘选：D = D₀ exp(αC) 情形下 C/C₀ = erfc(η/2√D₀ exp(αC₀)) / erfc(√(αC₀))
- 业务解读：SAP 中水的 D(C) 通常随浓度指数上升（高分子溶胀），该解给出 SAP 湿前沿演化的解析近似。

## 模块 2：研究方法与数据来源

- 数学方法：

- Boltzmann 变换（§7.2.1）
- Crank-Henry 迭代积分（§7.2.2）
- 特殊 D(C) 形式的解析解（§7.2.3–7.2.5）
- 实验数据：无直接数据；引用 Crank & Henry 1949a,b 的方法论。
- 局限性：

- Boltzmann 变换仅适用半无限/无限域；
- 迭代积分需多次数值积分，计算量大（当时无计算机，现今已不成问题）；
- 假设 D 只依赖 C，不依赖 t、x。
## 模块 3：论证过程

推导链（Boltzmann 变换）：
1. 从 ∂C/∂t = ∂/∂x(D(C) ∂C/∂x) 出发；
2. 引入 η = x/2√t；
3. 计算 ∂C/∂t = −(η/2t) C', ∂C/∂x = (1/2√t) C'；
4. 代入得 2η C' + d/dη(D C') = 0；
5. 积分得 D C' = 2η C' + const → ODE 形式。

关键假设：
- D = D(C) only；
- 初始浓度均匀；
- 半无限/无限域。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 1 PDE（变系数形式）、Ch 2 恒 D 解作基准。
- 后续影响：

- Ch 9 用本章方法计算 D(C) 的数值结果；
- Ch 10 时间滞后法在 D(C) 情形下的推广；
- Ch 11 非菲克扩散中的 Case I 与 Case II 分类用到本章的 D(C) 概念；
- Ch 14 化学反应伴随扩散中 S = R Cⁿ 导致等效 D_eff = D/(1+nRCⁿ⁻¹)。
## 模块 5：亮点与不足

- 亮点：

- Boltzmann 变换数学优美且实用；
- Crank-Henry 迭代法是 D(C) 反演的先驱方法；
- 显式给出 D(t) 归约法。
- 不足：

- Boltzmann 变换对有限域不适用；
- 迭代法收敛速度依赖初始猜测；
- 未考虑 D 对温度、应力的依赖（湿巾/纸尿裤中的应力驱动湿迁移）。
## 模块 6：关键术语与公式

|||
|---|---|
|Boltzmann transformation|"C may be expressed in terms of a single variable x/2√t… η = x/2√t" (p.106)|
|Concentration-dependent D|"the diffusion coefficient D depends only on the concentration of diffusing substance" (p.106)|

核心公式：
- 变系数 PDE：∂C/∂t = ∂/∂x(D(C) ∂C/∂x)  (7.5)
- Boltzmann 变换：η = x/2√t  (7.6)
- 变换后 ODE：D C'' + (dD/dC) (C')² + 2η C' = 0  (7.10)
- 时间依赖 D(t) 归约：T = ∫D(t')dt'  (7.3)
- 指数 D 解析解（§7.2.3）：C/C₀ = erfc(η/2√(D₀e^{αC₀}))/erfc(√(αC₀))

无量纲参数：η = x/2√t；αC₀（指数 D 的强度参数）

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|Boltzmann 变换推导|§7.2.1|p.106–107|方法学核心|高——严格微分推导|
|适用条件声明|§7.2.1|p.107|限定 Boltzmann 方法|高|
|Crank-Henry 迭代法|§7.2.2|p.107|数值求解 D(C)|高——被行业沿用|

## 模块 8：段落级微观精读

### 关键段落：§7.2.1 Boltzmann 变换引入（p.106）

"The equation for one-dimensional diffusion when the diffusion coefficient D is a function of concentration C is ∂C/∂t = ∂/∂x(D ∂C/∂x)."
- 句子功能：问题陈述
- 关键词：function of concentration
- 业务对应：SAP 中水的 D(C)

"Boltzmann (1894) showed that for certain boundary conditions, provided D is a function of C only, C may be expressed in terms of a single variable x/2√t."
- 句子功能：方法学提出
- 关键词：single variable
- 论证技术：相似性变量引入

"η = x/2√t. Thus we have ∂C/∂t = −(η/2t) dC/dη and ∂C/∂x = (1/2√t) dC/dη."
- 句子功能：链式法则计算
- 关键词：∂C/∂t, ∂C/∂x
- 论证技术：显式偏微分

"It is only when the initial and boundary conditions are expressible in terms of η alone… that the transformation can be used. They cannot be used, for example, when diffusion occurs in a finite sheet of thickness l."
- 句子功能：适用性警告
- 关键词：cannot be used, finite sheet
- 业务对应：有限厚 SAP 片层需 Ch 8 数值方法

业务关联总结：SAP 中水的扩散系数 D 随含水率变化 3–4 个数量级——恒 D 假设失效。本章的 Boltzmann 变换与 Crank-Henry 迭代法是 SAP D(C) 反演的数学基础。湿巾高分子纤维中的湿前沿也需此框架。实际建模中，Ch 8 数值方法（有限差分）配合本章 Boltzmann 分析解使用效果最佳。


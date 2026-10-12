---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_1362d97872f10db8d28f3e85e69554cd001a693ee6c0644e"
source_file: "ch03_INFINITE_AND_SEMI-INFINITE_MEDIA_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch03_INFINITE_AND_SEMI-INFINITE_MEDIA_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch03_INFINITE_AND_SEMI-INFINITE_MEDIA_report.md.md

# Chapter 3 — Infinite and Semi-Infinite Media 深度拆解报告

## 模块 1：本章核心内容概览

定位：在无限与半无限介质中求解扩散方程，涵盖瞬时点源/面源/球源/柱源四类"源"以及连续源，是 SAP 颗粒单球溶胀与非织造布纤网湿迁移场的理论基础。

### 核心观点/结论

观点 1：瞬时点源、面源、球源、柱源构成完整的"源函数族"。
- 页码：p.29–30（§3.2）
- 原文摘选："The solution for an instantaneous plane source in an infinite medium has already been given in Chapter 2, eqn (2.6). The corresponding solution for an instantaneous point source on an infinite plane surface is obtained in the same way…"
- 业务解读：SAP 颗粒可近似为瞬时球源（eqn 3.8），单个 SAP 微球在芯体中扩散的水蒸气/自由水场的解析形式可直接引用。

观点 2：球源在轴心处简化为 C = C₀{1−exp(−a²/4Dt)}。
- 页码：p.30（§3.2）
- 原文摘选："The integral in (3.10) has to be evaluated numerically except on the axis r = 0, where (3.10) becomes C = C₀{1−exp(−a²/4Dt)}."
- 业务解读：单个 SAP 微球（半径 a）在吸收水后，球心浓度随时间的指数演化直接给出，用于估算 SAP 吸水饱和速率的初段。

观点 3：圆盘源的剩余量 Q(t) 有解析级数形式。
- 页码：p.31（§3.2）
- 原文摘选："Rideal and Tadayon also give an expression for the total amount of diffusing substance Q remaining on the disc after time t, which is Q = 2πa²C₀ ∫₀^∞ [J₁(ωa)]² exp(−Dτω²)dω."
- 业务解读：湿巾湿斑扩散模型可用圆盘源描述——湿巾局部湿润后的横向扩展即"圆盘源扩散"。

## 模块 2：研究方法与数据来源

- 数学推导方法：多变量积分、Bessel 函数（I₀, J₀, J₁）、高斯积分、Carslaw & Jaeger 结果引用。
- 实验数据：无。
- 局限性：介质为无限或半无限，实际芯体（厚度 ~1–2 mm）有限，需配合 Ch 4。
## 模块 3：论证过程

核心方程推导逻辑链：
1. 从恒 D 二维/三维扩散 PDE 出发；
2. 试探解形式 C = A t^(-n/2) exp(−r²/4Dt)（n=1,2,3 对应不同维度）；
3. 用总质量 M 守恒定出 A；
4. 对有限初始分布（球、柱）用 Bessel 变换；
5. 圆盘源用 Hankel 变换（Rideal & Tadayon 方法）。

关键假设：介质无限/半无限、初始浓度均匀分布、D 恒定。

边界条件：r→∞ 时 C→0；r=0 处 C 有限（Bessel 函数 J₀ 满足）。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 1 PDE + Ch 2 反射法。
- 后续影响：

- Ch 4 的有限片层解在小 t 极限退化到本章结果；
- Ch 6 球体问题的 u=Cr 变换等价于一维问题，引用本章解；
- SAP 溶胀模型的起始"点源"假设源于本章。
## 模块 5：亮点与不足

- 亮点：

- 系统给出 1D/2D/3D 源函数的统一形式；
- 圆盘源结果直接可应用于湿巾；
- 球源轴心简化式计算友好。
- 不足：无限/半无限假设对湿巾（有限尺寸）、纸尿裤（有限芯体）有偏差。
## 模块 6：关键术语与公式

|||
|---|---|
|Instantaneous source|"all problems in which an amount of diffusing substance is deposited within a certain restricted region at time t = 0" (p.29)|
|Point source on infinite plane|面源在 2D 平面的 3D 扩散|

核心公式：
- 平面源（1D）：C = M/[2(πDt)^(½)] exp(−x²/4Dt)
- 面源（2D）：C = M/[4πDt] exp(−r²/4Dt)
- 体源（3D 点源）：C = M/[8(πDt)^(3/2)] exp(−r²/4Dt)
- 球源：C = (C₀/a) ∫[exp{−(a−r)²/4Dt} − exp{−(a+r)²/4Dt}] dr （3.8）
- 圆盘源剩余量：Q = 2πa²C₀ ∫₀^∞ [J₁(ωa)]² exp(−Dτω²)dω

无量纲参数：(Dt/a²)^(½)（球源）；(Dt/a²)（柱源）

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|球源解 (3.8)|§3.2|p.30|给出有限球初始分布的解析解|高|
|球源轴心简化 (3.11)|§3.2|p.30|特例解析形式，便于数值比较|高|
|圆盘源剩余量 (3.10b)|Rideal & Tadayon 1954|p.31|湿巾湿斑扩散直接应用|高|

## 模块 8：段落级微观精读

### 关键段落：§3.2 球源解的推导（p.30）

"If the diffusing substance is initially distributed uniformly through a sphere of radius a, the concentration C at radius r, and time t is given by C = (C₀/a) ∫_r^a [exp{−(a−r')²/4Dt} − exp{−(a+r')²/4Dt}] dr'."
- 句子功能：结果陈述
- 关键词：uniformly, sphere, radius a
- 论证技术：构造法——用球内每一点作为瞬时点源叠加
- 业务对应：SAP 微球溶胀

"The integral in (3.10) has to be evaluated numerically except on the axis r = 0, where (3.10) becomes C = C₀{1−exp(−a²/4Dt)}."
- 句子功能：特例简化（数学直觉）
- 关键词：numerically, axis r = 0
- 论证技术：奇点处的解析简化

"These expressions may be applied, for example, to the diffusion of a sphere or cylinder of solute into a large volume of solvent."
- 句子功能：应用场景举例
- 关键词：sphere, cylinder, large volume
- 业务对应：SAP 颗粒→尿液（大体积溶剂）

业务关联总结：纸尿裤中 SAP 颗粒（直径 ~0.2–1 mm）在芯体内均匀分布，可视为离散球源的叠加；湿巾中的湿斑横向扩展对应圆盘源；本章给出的源函数是建立芯体/湿巾"有效扩散场"模型的基本元素。


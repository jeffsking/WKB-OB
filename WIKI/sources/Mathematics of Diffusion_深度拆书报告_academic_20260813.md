---
type: source
title: "Mathematics of Diffusion_深度拆书报告_academic_20260813.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion_深度拆书报告_academic_20260813.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
key_claims: []
pages_linked: []
compile_mode: extractive
---

# Mathematics of Diffusion_深度拆书报告_academic_20260813.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion_深度拆书报告_academic_20260813.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# Mathematics of Diffusion_深度拆书报告_academic_20260813.md.md

# 《The Mathematics of Diffusion》深度拆书报告（Academic 完整版）

原书：J. Crank，《The Mathematics of Diffusion》，Second Edition，Clarendon Press/Oxford University Press，1975
ISBN：0 19 853344 6
页数：约 421 页（正文 1–406 + Tables 375–398 + References 399–406）
工作文本：/tmp/diffusion_fitz.txt（22,898 行 / 687K 字符）
报告日期：2026-08-13
报告作者：学术级拆解（academic 完整版，7 步骤）

## 一、书籍信息卡（Book Identity Card）

|||
|---|---|
|Title|The Mathematics of Diffusion|
|Author|John Crank，Brunel University, Uxbridge|
|Edition|Second Edition（First Ed. 1956，Second Ed. 1975）|
|Publisher|Clarendon Press / Oxford University Press|
|Chapters|15 章 + Tables + References + Author Index + Subject Index|
|学科坐标|Transport Phenomena / Chemical Engineering / Polymer Physics / Materials Science / Heat Transfer 类比体系|
|学术地位|扩散数学方程解析解的 "encyclopaedic handbook"；与 Carslaw & Jaeger《Conduction of Heat in Solids》并列，是工程师与物理学家测量/计算扩散系数的标准引用|
|作者权威|Crank 是迭代法（Crank-Nicolson 差分法，本章 §8）、Boltzmann 变换求解（Crank & Henry 1949a,b）的原始贡献者|
|本次聚焦|卫材（吸收卫生用品）相关：平板/膜 + time-lag、Boltzmann 变换、非 Fickian 扩散、非均匀介质（Maxwell/Fricke/Tsao）、移动边界（Stefan/Frank）、反应-扩散耦合|

核心论点（Core Thesis）（原文，p.11-12，行 53–61）：

"The book contains a collection of mathematical solutions of the differential equations of diffusion and methods of obtaining them. They are discussed against a background of some of the experimental and practical situations to which they are relevant."

方法论贡献：
1. 将扩散方程统一为热传导方程的数学同构（Fick 1855 ↔ Fourier 1822，§1.2，行 262–281）；
2. 建立"解 = 几何（球/柱/板）× 边界条件（Dirichlet/Neumann/Robin/移动边界）× 系数类型（常数/浓度相关/非 Fickian/非均匀）"的三维解库；
3. 对每个卫材关键场景给出可直接代入工程参数的闭合公式与表格。

## 二、逐章深度拆解（卫材相关六章）

### ▶ Chapter 1 — The Diffusion Equations（§1.1–§1.4*2，行 218–562）

1.1 核心论点
- Fick 定律 F = −D dC/dx（1.1，行 270）是扩散数学理论的基本假设，类比于 Fourier 热传导方程。
- 各向同性介质假设下该式成立；各向异性介质（无纺布、取向聚合物、晶体）必须使用广义扩散张量（§1.4，行 417–498）。
- 扩散系数量纲为 (length)²(time)⁻¹，如 cm² s⁻¹（行 278–280）。

1.2 关键概念操作化定义

||||
|---|---|---|
|Fick's First Law|F = −D dC/dx|270|
|Diffusion coefficient D|使通量与浓度梯度成正比的标量/张量|273|
|Random walk|单个分子运动描述（mean-square distance 可算，瞬时方向不可预测）|241–245|
|Anisotropic media|F_x = −(D₁₁ ∂C/∂x + D₁₂ ∂C/∂y + D₁₃ ∂C/∂z)（1.9）|424–437|
|Principal diffusion coefficients D₁, D₂, D₃|主轴扩散系数；通过坐标变换 (1.14) 可将各向异性问题归约为各向同性问题|464–480|
|Dₙ 方向依赖|Dₙ = D₁/l² + D₂/m² + D₃/n²（1.16），l,m,n 为方向余弦|489–491|

1.3 证据链表格

||||
|---|---|---|
|各向同性三维扩散方程|∂C/∂t = D(∂²C/∂x² + ∂²C/∂y² + ∂²C/∂z²)（1.5）|~330–350|
|球坐标（径向）扩散方程|∂C/∂t = (D/r²) ∂/∂r (r² ∂C/∂r)（1.8）|402–406|
|各向异性一般方程|∂C/∂t = D₁₁ ∂²C/∂x² + D₂₂ ∂²C/∂y² + D₃₃ ∂²C/∂z² + (D₁₂+D₂₁) ∂²C/∂x∂y + ...（1.10）|445–451|
|向同性归约|∂C/∂t = D(∂²C/∂ξ² + ∂²C/∂η² + ∂²C/∂ζ²)（1.15）|468–470|

1.4 章节衔接
- §1.2 → Ch.2（常数 D 解法）
- §1.4 → Ch.12（各向异性复合/多孔介质推广为 Maxwell/Fricke/Tsao 模型）
- (1.8) 球坐标 → Ch.6（球坐标扩散，SAP 吸水核心）

1.5 业务连接点（卫材）
- 无纺布（Nonwoven）各向异性：分子优先取向方向 + 平面内定向 → 三主轴扩散系数不同（行 518–523）；测量沿法向、平面内平行/垂直取向方向分别得到不同 D 值，不能简单用一个 D 表示。
- 复合膜（Barrier layer + SAP）：Ch.1 提供各向异性张量框架，Ch.12 Tsao 公式提供具体计算。

1.6 金句索引（中英对照）
- *"DIFFUSION is the process by which matter is transported from one part of a system to another as a result of random molecular motions."*（行 220–221）→ 扩散即由随机分子运动驱动的跨系统物质传输过程。
- *"D can reasonably be taken as constant, while in others, e.g. diffusion in high polymers, it depends very markedly on concentration."*（行 274–276）→ 稀溶液中 D 可视为常数，但在高分子中 D 强烈依赖浓度（对 SAP 高分子/水的核心警示）。

1.7 段落级微观精读（行 424–491，§1.4 各向异性方程）

*"Anisotropic media have different diffusion properties in different directions. Some common examples are crystals, textile fibres, and polymer films in which the molecules have a preferential direction of orientation."*（行 418–420）

逐句拆解：
1. "Anisotropic media have different diffusion properties in different directions" — 一句话给出 定义性命题。
2. "textile fibres, and polymer films" — 直接点名卫材：纺粘/熔喷无纺布属于典型 textile fibre，SAP 上层薄网属于 polymer film，均可能呈各向异性。
3. "This means that (1.1) must be replaced in general by the assumptions (1.9)" — 数学后果：Fick 简单标量形式失效，必须使用二阶张量。
4. "Dₙ = D₁/l² + D₂/m² + D₃/n²"（行 491）— 关键工程公式：测量方向的方向余弦 (l, m, n) 决定测得的 Dₙ；无纺布法向测量只得到 D₃（假设 z 为法向），而实际横向扩散由 D₁, D₂ 控制。

1.8 概念使用场景分析
- 各向异性张量：所有具有取向结构的非织造材料（纺粘 PP、SMS 复合、水刺布），液体在其中横向扩散速度显著大于纵向。
- Dₙ 公式：设计液体传输层时决定测试方向与产品取向角的关系。

1.9 概念演变微观轨迹
Fick 1855（一维各向同性标量）→ 1.9 广义张量形式（各向异性）→ 1.11 主轴变换 → 1.16 Dₙ 方向余弦公式（测量理论）→ Ch.12 Maxwell/Fricke（颗粒相各向异性推广）。

### ▶ Chapter 4 — Diffusion in a Plane Sheet（§4.1–§4.3，行 ~1400–2700）

2.1 核心论点
- 平板（membrane / sheet）是卫材最接近的几何原型：复合膜、表层/底层、SAP 颗粒均可近似为平板。
- Time-lag 方法（Barrer 1951，§4.3.3，行 2413–2421）是测量平板中扩散系数 D、渗透系数 P 和溶解度 S 的工程标准方法。
- Daynes-type time-lag 测量中常误认为稳态在 3×L 时建立，实际上低估 time-lag 约 4%（Jenkins et al. 1970，行 2465–2467）。

2.2 关键概念操作化定义

||||
|---|---|---|
|Time lag L|L = l²/(6D)（4.26）|2413|
|Steady-state flow Q∞|Q∞ = AD(C₁ − C₂)t/l（4.5）|~2370|
|Permeability P|P = DS|~2380|
|Holstein small-time solution|速率 F(t) 展开为指数级数（4.27）|2439–2445|
|Sigmoid sorption|表面浓度非瞬变时，吸收曲线出现拐点|2517–2523|

2.3 证据链表格

||||
|---|---|---|
|Time-lag|L = l²/(6D)|(4.26), 行 2413|
|稳态建立判据|Dt/l² ≈ 0.45|行 2424|
|稳态建立约 3L 时 → 实际 time-lag 被低估约 4%|Jenkins et al. 1970 结论|行 2465–2467|
|Sigmoid 吸收曲线条件|表面浓度指数上升 φ(t) = C₀(1 − e^(−βt))|(4.28), 行 2484|
|小时间 Holstein 展开|PF = 2C₁/√(πDt) · [1 − ...]|(4.27), 行 2439–2445|

2.4 章节衔接
- §4.3.3 time-lag → Ch.12 §12.2(ii) 复合膜 time-lag（Jaeger 1950b, Ash-Barrer-Petropoulos 1963/1965）
- 平板几何 → Ch.5 圆柱/Ch.6 球（坐标变换）
- 平板 + 变量表面浓度 → Ch.11 非 Fickian §11.2 sigmoid sorption

2.5 业务连接点（卫材）
- SAP 颗粒渗透测试：把单颗粒近似为平板，用 time-lag 反推等效 D。
- 复合底膜（PE 膜 + SMS）：Ch.12 laminate 时间延滞公式（12.15）直接用于复合膜整体传输评估。
- Sigmoid 曲线：实验中如果未等表面浓度瞬时平衡，SAP 吸水曲线呈 S 形——可能被误判为 Case II 非 Fickian 扩散（§11.2，行 2520–2523，§11.2 中 Rogers 分类）。

2.6 金句索引
- *"Following Daynes (1920), Barrer (1951) has used (4.26) as the basis of a method for obtaining the diffusion constant, the permeability constant, and the solubility of a gas by analysing stationary and non-stationary flow through a membrane."*（行 2415–2419）→ 平板 time-lag 方法是工程上同时确定 D、P、S 三个参数的标准程序。
- *"they concluded that the time lag is underestimated by about 4 per cent by making this assumption."*（行 2465–2467）→ 工程警

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion_深度拆书报告_academic_20260813.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion_深度拆书报告_academic_20260813.md.md`
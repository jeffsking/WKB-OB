---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_d4fd63a607fc337f25df55b68c04ed74001a693ee6c0644e"
source_file: "ch15_SIMULTANEOUS_DIFFUSION_OF_HEAT_AND_MOISTURE_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch15_SIMULTANEOUS_DIFFUSION_OF_HEAT_AND_MOISTURE_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch15_SIMULTANEOUS_DIFFUSION_OF_HEAT_AND_MOISTURE_report.md.md

# Chapter 15 — Simultaneous Diffusion of Heat and Moisture 深度拆解报告

## 模块 1：本章核心内容概览

定位：湿热耦合扩散——纸尿裤/湿巾在实际使用中（体温 37°C、空气湿度变化、尿液放热）的核心传质框架。Chapter 15 是本书对湿巾/纸尿裤应用最直接的实用章。

### 核心观点/结论

观点 1：水分传递与热传递耦合，不可独立处理。
- 页码：p.353（§15.1）
- 原文摘选："We thus have two processes, the transfer of moisture and the transfer of heat, which are coupled together, and we cannot in general consider one process without considering the other simultaneously."
- 业务解读：纸尿裤使用时——体温热传导 + 尿液放热（稀释热）+ 蒸发吸热三者耦合，必须联合求解。这是"湿冷感"（wet-cool）现象的物理根源。

观点 2：羊毛纤维吸湿实验揭示耦合效应的量级。
- 页码：p.353–354（§15.2）
- 原文摘选："Because the temperature rose to over 65 °C, however, the uptake immediately acquired was much less than 30 per cent. A temporary equilibrium is reached… Subsequently heat is lost and as cooling proceeds the uptake of moisture increases. The uptake curve observed by King and Cassie was thus essentially a cooling curve."
- 业务解读：实验证据——水分吸收放出热量 → 温度上升 → 平衡含水率下降 → 观察到的"吸湿"曲线实际上是"冷却"曲线。这解释了为什么纸尿裤在大量吸液后局部温度下降（感觉凉），而蒸发后又感觉更凉。

观点 3：耦合方程组可解耦为"正常坐标"。
- 页码：p.360–362（§15.4–15.6）
- 原文摘选："AM = ΔAC − ωΔT"（式 15.36）
- 业务解读：耦合方程组通过线性组合解耦为两个独立扩散方程——"永久波"（解耦主波）+ "暂态波"（耦合修正）。这是解析处理湿热耦合的数学关键。

观点 4：有效扩散系数 D' = D(1+γα) 与 0' = 0(1+εω)。
- 页码：p.364（§15.6.3）
- 原文摘选："D' = D(1+γα), and from (15.11) and (15.13) 0' = 0(1+εω)."
- 业务解读：耦合有效扩散系数——湿热耦合使"表观扩散系数"比纯扩散情形大（γ>0, ε>0），这解释了湿巾/纸尿裤中"湿迁移比纯 Fick 扩散更快"的实验观察。

观点 5：p 参数（湿热耦合强度）可用 nomogram 计算。
- 页码：p.365（§15.6.4）
- 原文摘选："(2p−1)² = u/(u−1)² + 4uωΔν"（式 15.45）
- 业务解读：Henry 1948 定标图给出 p（耦合强度参数）——p 越大，耦合越显著，湿迁移越偏离纯 Fick 扩散。

观点 6：压棉 baled cotton 的 γ₀ ≈ 7000，说明吸附主导。
- 页码：p.364（§15.6.3）
- 原文摘选："if γ₀ is large, i.e. if much more diffusing substance is absorbed by the solid than is contained in the pores, M' is nearly equal to M… Henry points out that this is so for baled cotton, for example, for which γ₀ may be as much as 7000."
- 业务解读：纤维材料的 γ₀ 参数极大——说明纤维素/粘胶纤维（湿巾、绒毛浆的主要成分）的吸附量 >> 孔隙含量，这解释了为什么湿巾"持水量"远大于"液态水含量"。

## 模块 2：研究方法与数据来源

- 数学方法：

- 耦合 PDE 方程组（水分 + 热量）
- 正常坐标解耦（§15.4–15.6）
- Henry 1939/1948 解析解
- Nomogram 定标
- 实验数据：引用 King & Cassie 1940（羊毛吸湿）、Cassie 1940a、Henry 1939/1948（压棉）、Higbie & Squire 1953。
- 方法论的局限性：

- 线性化假设（耦合系数 γ, ω, ε 恒定）；
- 不处理相变潜热（水蒸气→液态水）；
- 不处理多组分（尿液含盐/尿素）。
## 模块 3：论证过程

推导链（耦合 PDE 系统）：
1. 水分方程：∂C/∂t = D ∂²C/∂x² + γ ∂T/∂t（水分受温度影响）；
2. 热量方程：∂T/∂t = 0 ∂²T/∂x² + ω ∂C/∂t（热量受水分变化影响，含吸附热）；
3. 引入"正常坐标"：
   - M₁ = C + αT, M₂ = C + βT
   - α, β 由耦合系数 γ, ω, ε 决定；
4. M₁, M₂ 各自满足独立扩散方程（扩散系数分别为 D', D''）；
5. 反变换得 C, T。

关键假设：
- 耦合系数 γ, ω, ε 为常数（线性化）；
- 片层/柱/球几何；
- 边界条件 Dirichlet 型。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 1–14 的扩散框架、Ch 8 数值方法（用于复杂情形）。
- 后续影响：无（本章是全书末页）。
## 模块 5：亮点与不足

- 亮点：

- 耦合方程组的解耦方法（正常坐标）数学优美；
- Henry 定标图实用；
- 羊毛/压棉实验直接支撑理论。
- 不足：

- 线性化假设在极端温度/湿度变化时失效；
- 未处理相变（液态-气态）；
- 未讨论纤维素/SAP 的具体参数；
- 未处理尿液多组分。
## 模块 6：关键术语与公式

|||
|---|---|
|Coupled diffusion|"two processes, the transfer of moisture and the transfer of heat, which are coupled together" (p.353)|
|Normal coordinates|解耦后的独立扩散坐标 M₁, M₂ (p.360)|
|Permanent wave|解耦主波 (p.363)|
|Temporary wave|耦合修正波 (p.363)|

核心公式：
- 耦合水分方程：∂C/∂t = D ∂²C/∂x² + γ ∂T/∂t
- 耦合热量方程：∂T/∂t = 0 ∂²T/∂x² + ω ∂C/∂t
- 正常坐标：AM = ΔAC − ωΔT  (15.36)
- 有效扩散系数：D' = D(1+γα), 0' = 0(1+εω)  (15.38-39)
- 耦合强度参数：(2p−1)² = u/((u−1)² + 4uωΔν)  (15.45)

无量纲参数：p（耦合强度）、u = D/0（扩散/热扩散比）、γ₀（吸附/孔隙比）

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|羊毛吸湿温度上升实验|King & Cassie 1940|p.353–354|耦合效应的实验证据|高|
|正常坐标解耦|Henry 1939|p.360|数学方法学|高|
|Henry 定标图 (15.45)|Henry 1948|p.365|耦合参数 p 的实用计算|高|
|压棉 γ₀ ≈ 7000|Henry 1939|p.364|纤维吸附主导的证据|高|

## 模块 8：段落级微观精读

### 关键段落：§15.2 羊毛吸湿实验（p.353–354）

"King and Cassie (1940) attempted to demonstrate this conclusion experimentally by measuring the rate of sorption of water vapour by a small mass of wool (0.25 g) suspended by a sensitive spring-balance in an evacuated chamber into which water vapour was introduced at 23.5 mm pressure."
- 句子功能：实验设计描述
- 关键词：evacuated chamber, spring-balance
- 论证技术：排除空气扩散干扰，直接测纤维内扩散

"This does not appear to be at first sight supported by the uptake curve they observed, which reached 80 per cent only after an hour or so."
- 句子功能：矛盾/悬念
- 关键词：does not appear
- 论证技术：提出"实验 vs 理论"的矛盾

"We must remember, however, that when water vapour is absorbed by wool a large amount of heat is evolved which produces a considerable increase in temperature."
- 句子功能：矛盾解释
- 关键词：heat is evolved, temperature
- 论证技术：引入耦合效应解释矛盾

"The uptake curve observed by King and Cassie was thus essentially a cooling curve."
- 句子功能：结论
- 关键词：essentially a cooling curve
- 业务对应：湿巾"吸湿曲线"实际上混入了温度效应——评估湿巾含水率时必须控制温度

### 关键段落：§15.6.3 正常坐标解耦（p.363–364）

"The first term on the right-hand side of each equation represents the 'wave' which would result if there were no coupling between the diffusion processes and which may be referred to as the 'permanent wave'. The second term represents the result of the coupling and may be called the 'temporary wave' since it starts at zero, increases to a maximum, and then diminishes to zero again."
- 句子功能：物理图像建立
- 关键词：permanent wave, temporary wave
- 论证技术：波分解类比
- 业务对应：芯体湿迁移 = "主波"（纯扩散）+ "耦合波"（湿热交互）

业务关联总结：本章是湿巾/纸尿裤实际使用场景的物理模型。
- 湿冷感（wet-cool）：尿液放热 → 温度上升 → 蒸发吸热 → 表面温度下降；
- 防回渗失败：湿热耦合使湿迁移速率大于纯 Fick 预测（D' > D），设计防回渗层时必须考虑 γ、ω 参数；
- 湿巾均匀性：局部湿热耦合产生"热点"（温度不均 → 含水率不均）；
- SAP 干爽性：SAP 溶胀放热（稀释热）→ 芯体局部温度变化 → 影响表层手感。

实际建模需：耦合 PDE + Henry 定标 + Ch 12 层状介质方法。


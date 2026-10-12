---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_eb62100cf9dad450463a21f6dcc8d7f3001a693ee6c0644e"
source_file: "concept_index.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/concept_index.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# concept_index.md.md

# Concept Index — 《Mathematics of Diffusion》核心概念词典

## 1. 概念总览表

|||||||
|---|---|---|---|---|---|
|1|扩散|Diffusion|Ch1|全书|芯体吸水/湿迁移/SAP 溶胀|
|2|Fick 第一定律|Fick's First Law|Ch1 §1.2|全书|所有吸液/传质模型的本构方程|
|3|扩散系数 D|Diffusion Coefficient|Ch1 §1.2|全书|SAP 材料的核心参数|
|4|各向同性介质|Isotropic Medium|Ch1 §1.2|Ch12, Ch15|理想芯体层假设|
|5|各向异性介质|Anisotropic Medium|Ch1 §1.4|Ch12|非织造布 MD/CD 差异|
|6|瞬时平面源|Instantaneous Plane Source|Ch2 §2.2.1|Ch3|SAP 颗粒近似|
|7|反射法|Reflection Method|Ch2 §2.2.2|Ch3|边界条件构造|
|8|分离变量法|Separation of Variables|Ch2 §2.3|Ch3–6|解析解工具箱|
|9|Laplace 变换法|Laplace Transform|Ch2 §2.4|Ch4, Ch10, Ch12|复杂边界问题|
|10|稳态|Steady State|Ch4 §4.2|Ch4–6, Ch9|芯体稳态传质|
|11|渗透常数 P|Permeability Constant|Ch4 §4.2.1|Ch10|湿巾 MVTR|
|12|复合膜|Composite Membrane|Ch4 §4.2.3|Ch12|芯体多层结构|
|13|时间滞后 L|Time Lag|Ch4 §4.3.3|Ch10, Ch12|SAP D 测量标准法|
|14|浓度依赖 D(C)|Concentration-Dependent D|Ch4 §4.2.2|Ch7–9, Ch11|SAP 溶胀动力学|
|15|Barrer 平均 D̄|Barrer's Mean D̄|Ch4 §4.2.2|Ch9, Ch10|D(C) 的积分定义|
|16|Boltzmann 变换|Boltzmann Transformation|Ch7 §7.2.1|Ch9|D(C) 的数学处理|
|17|Crank-Henry 迭代法|Crank-Henry Method|Ch7 §7.2.2|Ch9|D(C) 反演|
|18|无量纲变量|Non-dimensional Variables|Ch8 §8.2|全书|数值模拟基础|
|19|显式有限差分|Explicit FDM|Ch8 §8.4|Ch9|数值方法|
|20|Crank-Nicolson 法|Crank-Nicolson|Ch8 §8.5|Ch9|数值方法首选|
|21|互扩散系数 D_V|Mutual Diffusion Coefficient|Ch10 §10.2|Ch9, Ch15|SAP-水二元体系|
|22|热力学 D_T / 动力学 D_0|Thermodynamic/Kinetic D|Ch10 §10.6.2|Ch15|SAP 参数分离|
|23|Frisch 分解 L_F+L_T|Frisch Decomposition|Ch10 §10.6.2|Ch11|非菲克实验判据|
|24|Case I (Fickian)|Case I|Ch11 §11.1|Ch13|SAP 橡胶态饱和|
|25|Case II|Case II|Ch11 §11.1|Ch13|SAP 玻璃态快速溶胀|
|26|非菲克扩散|Non-Fickian|Ch11 §11.1|Ch13|SAP 过渡区|
|27|Mt ∝ tⁿ 判据|Power-law Index|Ch11 §11.1|Ch13|扩散机制实验判据|
|28|层状介质|Laminates|Ch12 §12.2|Ch4, Ch15|芯体多层结构|
|29|颗粒状介质|Particulates|Ch12 §12.3|Ch3, Ch6|SAP 在绒毛浆中|
|30|Maxwell 等效模型|Maxwell's Formula|Ch12 §12.3|—|复合 D_eff|
|31|动边界|Moving Boundary|Ch13 §13.1|Ch11, Ch14|SAP 溶胀前沿|
|32|Stefan 问题|Stefan Problem|Ch13 §13.1|Ch11, Ch15|相变/溶胀前沿|
|33|Stefan 守恒条件|Stefan Condition|Ch13 §13.3|Ch11|前沿推进速度|
|34|等效 D_eff = D/(R+1)|Effective D with Reaction|Ch14 §14.2|Ch11, Ch15|SAP 交联网络|
|35|Freundlich 等温线|Freundlich Isotherm|Ch14 §14.2.1|Ch9|非线性 D_eff(C)|
|36|Damköhler 数|Damköhler Number|Ch14|—|反应/扩散速率比|
|37|湿热耦合|Heat-Moisture Coupling|Ch15 §15.1|Ch10, Ch12|湿巾/纸尿裤使用场景|
|38|正常坐标|Normal Coordinates|Ch15 §15.6|—|耦合方程解耦|
|39|永久波/暂态波|Permanent/Temporary Wave|Ch15 §15.6.3|—|耦合扩散的物理图像|
|40|Henry 耦合参数 p|Henry's p|Ch15 §15.6.4|—|耦合强度定量|

## 2. 每个概念详解

### 2.1 Fick 第一定律（Fick's First Law）

原始定义（Ch1 p.2 §1.2）："the rate of transfer of diffusing substance through unit area of a section is proportional to the concentration gradient measured normal to the section, i.e. F = −D dC/dx"

操作化定义：通量 F [mol m⁻² s⁻¹] = −D [m² s⁻¹] × 浓度梯度 dC/dx [mol m⁻⁴]。负号表示从高浓度向低浓度流动。

评估：
- 各向同性介质下严格成立（Ch1 §1.2 声明）；
- D 恒定 → 线性本构；D = D(C) → 非线性本构（Ch7）；
- 不适用于：Case II 前沿（Ch11）、动边界（Ch13）、强对流场景。

使用场景：
- SAP 吸液：F = −D(C) dC/dx，D(C) 强烈依赖；
- 芯体湿迁移：F = −D_eff ∇C，各向异性 D_eff；
- 湿巾均匀性：F 决定湿扩散速率。

概念演变：
- Fick 1855（首提）→ Fourier 1822 类比 → Crank 1956 系统化（Ch1）→ Ch7 变系数推广 → Ch11 非菲克偏离。

### 2.2 扩散系数 D（Diffusion Coefficient）

原始定义（Ch10 p.203 §10.1）："the diffusion coefficient is defined as the rate of transfer of the diffusing substance across unit area of a section, divided by the space gradient of concentration at the section. Thus, if the rate of transfer is F, and C the concentration… F = −D dC/dx."

操作化定义：D = |F|/|dC/dx|。量纲：[length]²[time]⁻¹，如 cm² s⁻¹ 或 m² s⁻¹。

评估：
- 依赖参考系选择（体积固定 D_V、质量固定 D_M、溶剂固定 D_S）——Ch10 §10.3 详细讨论；
- 可依赖 C, T, x, t；
- SAP 中 D 跨越 10⁻¹² 到 10⁻⁸ cm²/s（干态到饱和）。

使用场景：
- SAP 材料筛选：比较 D 值评估吸水速率；
- 芯体设计：D_eff 决定湿迁移时间；
- 湿巾均匀性：D 值决定"湿半时间"。

概念演变：
- Fick 1855（常数 D）→ Barrer 1946（D(C) 积分定义）→ Crank 1956（D 依赖 C, T, x 系统处理）→ Frisch 1958（时间滞后法测 D(C)）→ Petropoulos & Roussis 1967（D_T vs D_0 分离）。

### 2.3 时间滞后法（Time Lag Method）

原始定义（Ch4 p.52 §4.3.3）："L = l²/6D… Following Daynes (1920), Barrer (1951) has used (4.26) as the basis of a method for obtaining the diffusion constant."

操作化定义：稳态透过曲线 Q(t) vs t 的渐近线性段向 t 轴外推，截距 L 即为时间滞后。恒 D 情形 L = l²/(6D)。

评估：
- 恒 D 精确；D = D(C) 时需 Frisch 修正；
- 非菲克体系 L 与 l² 关系偏离线性 → 截距 L_T ≠ 0（Frisch 判据）；
- 实验简便，被行业 70 年沿用。

使用场景：
- SAP D 测量（行业标准）；
- 湿巾 MVTR 快速评估；
- 芯体防回渗层 P 值测定。

概念演变：
- Daynes 1920（原始）→ Barrer 1951（推广）→ Frisch 1958–1962（D(C) 推广 + 非菲克判据）→ Ash et al. 1965（多层推广）→ Barrer 1969（汇总）。

### 2.4 非菲克扩散（Non-Fickian Diffusion）

原始定义（Ch11 p.256 §11.1）："Non-Fickian or anomalous diffusion which occurs when the diffusion and relaxation rates are comparable."

操作化定义：Mt ∝ tⁿ，0.5 < n < 1；或 Mt-t 曲线呈 S 形（Sigmoid）；或时间滞后与 l² 关系偏离线性（L_T ≠ 0）。

评估：
- 定性分类清晰（Alfrey-Gurnee-Lloyd 三分类）；
- 定量模型不成熟（Ch11 未给严格 PDE）；
- 与动边界（Ch13）和化学反应（Ch14）有内在联系。

使用场景：
- SAP 吸液过渡区（DR 5–20）；
- 湿巾纤维湿迁移延迟；
- 聚氨酯/橡胶材料的气体透过。

概念演变：
- Rogers 1965（术语"anomalous"首次系统化）→ Alfrey-Gurnee-Lloyd 1966（三分类）→ Park 1968（Sigmoid 描述）→ Stannet et al. 1972（实验汇总）→ Crank 1975 Ch11（理论框架）。

### 2.5 动边界（Moving Boundary）/ Stefan 问题

原始定义（Ch13 p.287 §13.1）："a sharp boundary surface moves through the medium. It separates a region in which all the sites are occupied from one in which none of them are."

操作化定义：界面位置 X(t) 由 Stefan 守恒条件决定：−D₁ ∂C/∂x|_{x=X} = C₁ dX/dt。

评估：
- 数学严格（erfc 解析解 + Danckwerts 一般理论）；
- 假设尖锐边界（实际为连续过渡）；
- 与 Case II 完全对应。

使用场景：
- SAP 溶胀前沿推进；
- 湿巾"湿前沿"扩展；
- 冻结-融化（芯体在低温储存）。

概念演变：
- Stefan 1890（冰融化问题）→ Crank 1956 Ch13（扩散中的 Stefan 问题）→ Danckwerts 1950（一般理论）→ Rubenstein 1971（系统数学呈现）。

### 2.6 湿热耦合（Heat-Moisture Coupling）

原始定义（Ch15 p.353 §15.1）："two processes, the transfer of moisture and the transfer of heat, which are coupled together, and we cannot in general consider one process without considering the other simultaneously."

操作化定义：耦合 PDE 系统：∂C/∂t = D ∂²C/∂x² + γ ∂T/∂t；∂T/∂t = 0 ∂²T/∂x² + ω ∂C/∂t。

评估：
- Henry 1939 正常坐标解耦方法完整；
- 线性化假设（γ, ω, ε 恒定）在极端条件下失效；
- 未处理相变潜热。

使用场景：
- 纸尿裤湿冷感；
- 湿巾使用中的温度变化；
- 纤维材料（羊毛、棉、粘胶）的含水率-温度关系。

概念演变：
- Cassie 1940（羊毛耦合实验）→ King & Cassie 1940（真空吸湿实验）→ Henry 1939（正常坐标解耦）→ Henry 1948（耦合参数 p 定标图）→ Crank 1975 Ch15（系统呈现）。

### 2.7 Boltzmann 变换（Boltzmann Transformation）

原始定义（Ch7 p.106 §7.2.1）："Boltzmann (1894) showed that for certain boundary conditions, provided D is a function of C only, C may be expressed in terms of a single variable x/2√t."

操作化定义：η = x/(2√t)，将 PDE ∂C/∂t = ∂/∂x(D(C)∂C/∂x) 化为 ODE：D C'' + (dD/dC)(C')² + 2η C' = 0。

评估：
- 数学优美，将 PDE 降阶为 ODE；
- 仅适用于半无限/无限域（边界须可表为 η 的函数）；
- 有限域（如 SAP 片层）不适用。

使用场景：
- SAP D(C) 定性分析；
- 湿前沿形状解析近似；
- 与 Crank-Henry 迭代法配合做 D(C) 反演。

概念演变：
- Boltzmann 1894（原始）→ Crank 1956 Ch7（系统化）→ Crank-Henry 1949（迭代求解法）。

### 2.8 Case I / Case II 分类（Alfrey-Gurnee-Lloyd）

原始定义（Ch11 p.255–256 §11.1）：
- Case I (Fickian)："rate of diffusion is much less than that of relaxation" → Mt ∝ t^(½)
- Case II："diffusion is very rapid compared with the relaxation processes" → Mt ∝ t¹
- Non-Fickian："diffusion and relaxation rates are comparable" → Mt ∝ tⁿ, 0.5 < n < 1

操作化定义：无量纲数 Pe = τ_relax/τ_diff 决定分类：
- Pe ≪ 1 → Case I
- Pe ≫ 1 → Case II
- Pe ~ 1 → Non-Fickian

评估：
- 行业共识分类，可操作；
- Pe 数定义隐含"单一特征松弛时间"假设（实际为宽谱）；
- 与 Ch13 动边界（Case II）和 Ch10 Frisch 判据（非菲克）对应。

使用场景：
- SAP 吸液机制诊断（测量 n 值）；
- 湿巾纤维湿迁移分类；
- 高分子渗透物-聚合物体系通用分类。

### 2.9 Maxwell 等效模型（Maxwell's Formula）

原始定义（Ch12 §12.3）：颗粒状复合介质的等效扩散系数 D_eff = D_m · (2D_m + D_p)/(2D_p + D_m)（稀浓度球形粒子）。

操作化定义：连续介质（基质 D_m）中分散球形颗粒（D_p），体积分数 φ → D_eff。

评估：
- 稀浓度极限解析精确；
- 高 φ 需修正（Bruggeman、Effective Medium Theory）；
- 假设球形、均匀分散、无界面阻力。

使用场景：
- SAP 颗粒在绒毛浆中的有效 D_eff；
- 复合芯体吸液速率估算。

### 2.10 Crank-Nicolson 法

原始定义（Ch8 p.145 §8.5）："The Crank-Nicolson method has the strong advantage of remaining stable for all values of r. We can thus proceed with larger and hence fewer time steps."

操作化定义：隐式有限差分格式，空间用 (j + (j+1))/2 平均，得无条件稳定的二阶精度格式。

评估：
- SAP 数值模拟首选方法；
- 每步需解三对角方程组（计算量 O(N)）；
- 二阶精度 O(Δt² + Δx²)。

使用场景：
- SAP D(C) 数值解；
- 芯体多层湿迁移；
- 湿热耦合 PDE 数值解。

## 3. 概念演变的微观轨迹

### 3.1 D 从"常数"到"函数"的演变

Ch1 §1.2: D = const (Fick 1855)
    ↓
Ch4 §4.2.2: D = D(C), D̄ = (1/ΔC)∫DdC (Barrer 1946)
    ↓
Ch7 §7.2.1: Boltzmann 变换处理 D(C) (Boltzmann 1894, Crank 系统化)
    ↓
Ch7 §7.2.2: Crank-Henry 迭代法反演 D(C) (Crank-Henry 1949)
    ↓
Ch9 §9.1-9.2: D(C) 的稳态/非稳态图形结果
    ↓
Ch10 §10.6.2: Frisch 时间滞后法测 D(C) (Frisch 1958)
    ↓
Ch10 §10.6.2: D_T vs D_0 分离 (Petropoulos-Roussis 1967)

### 3.2 Fick 定律的偏离路径

Ch1 §1.2: Fick 定律（严格成立条件：各向同性、恒 D、无对流）
    ↓ (Ch11)
玻璃态高分子 → 松弛时间 τ_relax 不可忽略
    ↓ (Pe 数分类)
Case I (Fickian, Pe≪1)
Case II (Pe≫1, 前沿匀速)
Non-Fickian (Pe~1, 0.5<n<1)
    ↓ (Ch13)
动边界（Stefan 问题）：D 在 C₁ 处不连续
    ↓ (Ch15)
湿热耦合：F = −D∇C + γ∇T（耦合修正）

### 3.3 几何扩展路径

Ch1: 一般 PDE（3D 各向异性）
    ↓
Ch3: 无限/半无限介质（1D/2D/3D 源函数）
    ↓
Ch4: 片层（1D 有限）→ 时间滞后法
Ch5: 圆柱（径向）→ Bessel 函数
Ch6: 球（径向）→ u=Cr 变换
    ↓
Ch12: 层状（多层串联）+ 颗粒状（Maxwell）
    ↓
Ch15: 湿热耦合（任意几何 + 耦合）

## 4. SAP/纸尿裤业务概念映射表

|||||
|---|---|---|---|
|D|SAP 吸水扩散系数|D(C)|10⁻¹² – 10⁻⁸ cm²/s|
|时间滞后 L|SAP D 测量|L = l²/6D|秒–分钟|
|非菲克 n|SAP 吸液指数|n|0.5–1.0|
|Case II|SAP 初期快速溶胀|v (前沿速度)|μm/s – mm/s|
|复合膜|芯体多层|Σ(lᵢ/Dᵢ)|—|
|Maxwell D_eff|SAP+绒毛浆复合|D_eff|—|
|动边界|SAP 溶胀前沿|X(t) = α√(Dt)|—|
|等效 D_eff|交联网络|D/(1+R)|—|
|湿热耦合|湿冷感/防回渗|γ, ω, p|—|
|渗透 P|湿巾 MVTR|P = DS|—|

Concept Index 完成。共 40 个核心概念，覆盖 Ch1–Ch15 全书。


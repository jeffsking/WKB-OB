---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_2360fcd2e579013ccb920232025357d7001a693ee6c0644e"
source_file: "synthesis.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/synthesis.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# synthesis.md.md

# Synthesis — 《Mathematics of Diffusion》(Crank, 1975) 全书合成报告

## 一、全书理论地图（Theoretical Map）

                    ┌─────────────────────────────────────────────────────┐
                    │                  Chapter 1                          │
                    │  The Diffusion Equations (PDE + Fick's Law)         │
                    │  核心：F = −D∇C, ∂C/∂t = ∇·(D∇C)                    │
                    └───────────────────────┬─────────────────────────────┘
                                            │
                    ┌───────────────────────▼─────────────────────────────┐
                    │                Chapter 2                             │
                    │  Methods of Solution (恒 D)                          │
                    │  反射法 · 分离变量 · Laplace 变换                    │
                    └───────┬──────────┬──────────────┬───────────────────┘
                            │          │              │
         ┌──────────────────▼──┐  ┌────▼───────┐  ┌──▼──────────────┐
         │    Chapter 3        │  │  Chapter 4 │  │  Chapter 5/6    │
         │ Infinite/Semi-inf.  │  │ Plane Sheet│  │ Cylinder / Sphere│
         │ (源函数)            │  │(时间滞后法)│  │(Bessel/u=Cr)    │
         └─────────────────────┘  └────┬───────┘  └─────────────────┘
                                       │
                    ┌──────────────────▼────────────────────────────────┐
                    │                Chapter 7                           │
                    │  Concentration-Dependent D                        │
                    │  Boltzmann 变换 + Crank-Henry 迭代                 │
                    └──────────┬───────────────────────┬────────────────┘
                               │                       │
                    ┌──────────▼──────────┐    ┌──────▼─────────────┐
                    │    Chapter 8        │    │   Chapter 9        │
                    │  Numerical Methods  │    │  Calculated Results│
                    │  FDM/Crank-Nicolson│    │  (D(C) 图形)       │
                    └─────────────────────┘    └────────────────────┘

                    ┌──────────────────────────────────────────────────┐
                    │                Chapter 10                         │
                    │  Definition & Measurement of D                    │
                    │  参考系 · 时间滞后 · Frisch · 动态法              │
                    └───────────────────────┬──────────────────────────┘
                                            │
                    ┌───────────────────────▼──────────────────────────┐
                    │                Chapter 11                         │
                    │  Non-Fickian Diffusion                            │
                    │  Case I/II/Non-Fickian · Mt∝tⁿ                   │
                    └───────────────────────┬──────────────────────────┘
                                            │
              ┌─────────────────────────────┼──────────────────────────┐
              │                             │                          │
    ┌─────────▼────────┐        ┌──────────▼─────────┐   ┌────────────▼────────┐
    │   Chapter 12     │        │   Chapter 13       │   │   Chapter 14       │
    │ Heterogeneous    │        │ Moving Boundaries  │   │ Diffusion + Chem.   │
    │ (层状+颗粒)      │        │ (Stefan 问题)      │   │ Reaction            │
    └──────────────────┘        └────────────────────┘   └─────────────────────┘
              │                             │                          │
              └──────────────┬──────────────┴──────────────────────────┘
                             │
              ┌──────────────▼────────────────────────────────────────┐
              │                Chapter 15                              │
              │  Simultaneous Diffusion of Heat and Moisture           │
              │  耦合 PDE · 正常坐标 · Henry 定标                      │
              └───────────────────────────────────────────────────────┘

地图解读：
- 底层（Ch1）：公理化基础——Fick 定律 + 扩散 PDE。
- 工具箱（Ch2）：解析解的三套方法。
- 几何扩展（Ch3–6）：从无限域到片/柱/球有限域。
- 变系数（Ch7–9）：D 从常数到 D(C)，解析 + 数值。
- 测量方法学（Ch10）：实验到 D 的桥梁。
- 偏离 Fick（Ch11）：高分子非菲克行为——本书对 SAP 应用最关键的章。
- 复杂介质（Ch12–15）：多层、动边界、化学反应、湿热耦合——本书对纸尿裤/湿巾应用最直接的章。

## 二、概念索引（按理论层级组织）

### 层级 0：公理层

- 扩散过程（Ch1 §1.1）
- Fick 第一定律（Ch1 §1.2）
- 扩散 PDE / Fick 第二定律（Ch1 §1.3）
- 各向同性/各向异性（Ch1 §1.2–1.4）
### 层级 1：解法层

- 反射法（Ch2 §2.2）
- 分离变量法（Ch2 §2.3）
- Laplace 变换法（Ch2 §2.4）
- Boltzmann 变换（Ch7 §7.2.1）
- Crank-Henry 迭代法（Ch7 §7.2.2）
- 有限差分法（Ch8）
- Crank-Nicolson 法（Ch8 §8.5）
### 层级 2：几何层

- 瞬时点/面/球/柱源（Ch3）
- 片层（Ch4）：稳态 + 非稳态 + 时间滞后
- 圆柱（Ch5）：Bessel 函数
- 球（Ch6）：u=Cr 变换
### 层级 3：参数层

- 扩散系数 D（Ch1, Ch10）
- 渗透常数 P（Ch4 §4.2.1）
- Barrer 积分 D̄（Ch4 §4.2.2, Ch9）
- 有效扩散系数 D_eff（Ch14 §14.2）
- 热力学 D_T / 动力学 D_0（Ch10 §10.6.2）
### 层级 4：测量层

- 稳态透过法（Ch4 §4.2）
- 时间滞后法 L = l²/6D（Ch4 §4.3.3, Ch10）
- Frisch 分解 L_F+L_T（Ch10 §10.6.2）
- 动态振动膜法（Ch10 §10.6）
- Ash-Barrer 稳态反演（Ch10 §10.6.1）
### 层级 5：偏离层

- 非菲克扩散（Ch11）
- Case I / Case II / Non-Fickian（Ch11 §11.1）
- Mt ∝ tⁿ 判据（Ch11）
- 动边界（Ch13）
- Stefan 问题（Ch13 §13.1）
### 层级 6：耦合层

- 层状介质串联（Ch12 §12.2）
- Maxwell 等效（Ch12 §12.3）
- 扩散-化学反应（Ch14）
- 湿热耦合（Ch15）
- 正常坐标解耦（Ch15 §15.6）
## 三、原文摘选索引（CSV 格式）

完整版 CSV 见 index.csv，共 48 条记录，涵盖 Ch1–Ch15 每章 3–4 条关键原文。

索引字段说明：
- 章节：Ch1–Ch15
- 页码：原文页码
- 原句：英文原文摘选
- 引用目的：该摘选在拆解中的论证功能

按业务主题分组的关键摘选：

||||
|---|---|---|
|SAP 吸水|u=Cr 变换（球→线）|Ch6 p.90|
|SAP 吸水|Mt ∝ tⁿ, 0.5<1|Ch11 p.256|
|SAP 吸水|Case II 匀速前沿|Ch11 p.256|
|SAP 溶胀前沿|−D₁dC/dx = C₁dX/dt|Ch13 p.297|
|SAP 等效 D|D/(R+1)|Ch14 p.327|
|芯体多层|串联阻力 Σ(lᵢ/Dᵢ)|Ch4 p.47|
|芯体多层|层状串联 (12.4)|Ch12 p.268|
|湿迁移|时间滞后 L = l²/6D|Ch4 p.52|
|湿迁移|稳态判据 Dt/l²=0.45|Ch4 p.52|
|湿巾 MVTR|P = DS|Ch4 p.46|
|防回渗|耦合 D' = D(1+γα)|Ch15 p.364|
|湿冷感|吸湿曲线实为冷却曲线|Ch15 p.354|
|D(C) 反演|Frisch 时间滞后法|Ch10 p.225|
|非菲克诊断|L_F + L_T 分解|Ch10 p.227|
|纤维吸液|对数分布非線性|Ch5 p.70|
|抗菌剂缓释|exp(−x√(k/D))|Ch14 p.335|

## 四、阅读路线图（Reading Roadmap）

### 4.1 面向 SAP 研发工程师的路线

必读路径（核心 8 章）：
Ch1 → Ch4 → Ch7 → Ch9 → Ch10 → Ch11 → Ch13 → Ch14

可选路径（按需要）：
Ch2 (方法论背景) → Ch3 (源函数) → Ch5/6 (几何扩展)
Ch8 (数值方法) → Ch12 (多层) → Ch15 (湿热耦合)

阅读顺序理由：
1. Ch1：公理化基础（20 分钟）
2. Ch4：片层问题 + 时间滞后法（SAP D 测量标准法）
3. Ch7：Boltzmann 变换（D(C) 数学处理）
4. Ch9：D(C) 图形结果（SAP D(C) 形态识别）
5. Ch10：D 定义 + Frisch 方法（D(C) 实验反演 + 非菲克判据）
6. Ch11：非菲克扩散（SAP 吸液机制核心）
7. Ch13：动边界（SAP 溶胀前沿）
8. Ch14：扩散+反应（SAP 交联网络等效 D）

### 4.2 面向芯体设计工程师的路线

必读路径：
Ch1 → Ch4 → Ch12 → Ch15

重点章节：
Ch4 §4.2.3 复合膜（芯体多层串联）
Ch12 §12.2 层状介质（芯体多层 D_eff）
Ch12 §12.3 Maxwell 等效（SAP+绒毛浆复合）
Ch15 湿热耦合（使用场景）

### 4.3 面向湿巾研发工程师的路线

必读路径：
Ch1 → Ch4 → Ch10 → Ch11 → Ch14

重点章节：
Ch4 §4.2.1 渗透常数 P = DS（MVTR 基础）
Ch10 时间滞后法（D 测量）
Ch11 非菲克（湿迁移延迟）
Ch14 §14.3 一级不可逆（抗菌剂缓释）

### 4.4 数学深度路线（理论研究）

Ch1 → Ch2 → Ch3 → Ch7 → Ch8 → Ch10

重点：
Ch2 三种解析方法
Ch7 Boltzmann 变换推导
Ch8 Crank-Nicolson 格式稳定性证明
Ch10 Frisch 时间滞后理论

## 五、业务应用总矩阵

|||||||
|---|---|---|---|---|---|
|Ch1 Fick 定律|★★★★★|★★★★|★★★★|★★★★|★★★|
|Ch2 解法|★★★|★★★|★★|★★|★|
|Ch3 源函数|★★★★|★★|★★★|★|★|
|Ch4 片层|★★★★|★★★★★|★★★★|★★★★|★★|
|Ch5 圆柱|★★★|★★|★★★|★★|★|
|Ch6 球|★★★★★|★|★|★|★|
|Ch7 Boltzmann|★★★★★|★★★|★★★|★★★|★★|
|Ch8 数值|★★★★★|★★★★★|★★★★|★★★★|★★★|
|Ch9 D(C) 结果|★★★★★|★★★★|★★★★|★★★|★★|
|Ch10 D 测量|★★★★★|★★★★★|★★★★★|★★★★|★★|
|Ch11 非菲克|★★★★★|★★★|★★★★|★★|★|
|Ch12 多层|★★★|★★★★★|★★★★|★★★★★|★★|
|Ch13 动边界|★★★★★|★★|★★★|★★|★|
|Ch14 反应|★★★★|★|★★|★|★★★★★|
|Ch15 湿热耦合|★★★|★★★★|★★★★★|★★★★|★★|

★ 数量 = 该章对该业务主题的理论支撑强度

## 六、全书关键公式速查表

|||||
|---|---|---|---|
|1|F = −D ∂C/∂x|Ch1 §1.2|本构方程|
|2|∂C/∂t = D ∂²C/∂x²|Ch1 §1.3|扩散 PDE|
|3|C = M/[2(πDt)^(½)] exp(−x²/4Dt)|Ch2 §2.2.1|瞬时平面源|
|4|F = D(C₁−C₂)/l|Ch4 §4.2|片层稳态|
|5|P = DS|Ch4 §4.2.1|渗透常数|
|6|Σ(lᵢ/Dᵢ) = l/D̄|Ch4 §4.2.3|复合膜串联|
|7|D̄ = (1/ΔC)∫DdC|Ch4 §4.2.2|Barrer 积分|
|8|L = l²/6D|Ch4 §4.3.3|时间滞后|
|9|D_eff = D_m(2D_m+D_p)/(2D_p+D_m)|Ch12 §12.3|Maxwell 等效|
|10|Mt = K tⁿ, n∈[0.5,1]|Ch11 §11.1|非菲克判据|
|11|η = x/2√t|Ch7 §7.2.1|Boltzmann 变换|
|12|−D₁∂C/∂x = C₁dX/dt|Ch13 §13.3|Stefan 条件|
|13|D_eff = D/(R+1)|Ch14 §14.2|等效 D（线性反应）|
|14|C = C₀exp(−x√(k/D))|Ch14 §14.3.2|一级不可逆稳态|
|15|D' = D(1+γα)|Ch15 §15.6.3|耦合有效 D|
|16|L = L_F + L_T|Ch10 §10.6.2|Frisch 分解|
|17|r = Dδt/δx² ≤ ½|Ch8 §8.4|显式稳定性|
|18|u = Cr (球→线变换)|Ch6 §6.1|几何简化|

## 七、方法学演进时间线

|||||
|---|---|---|---|
|1822|热传导方程|Fourier|Ch1|
|1855|Fick 定律|Fick|Ch1|
|1890|Stefan 问题|Stefan|Ch13|
|1894|Boltzmann 变换|Boltzmann|Ch7|
|1910|柱壁最优厚度|Porter-Martin|Ch5|
|1920|时间滞后法|Daynes|Ch4|
|1940|羊毛吸湿-温度耦合|King-Cassie|Ch15|
|1946|D(C) 积分定义|Barrer|Ch4, Ch9|
|1948|Wilson 可逆反应解|Wilson|Ch14|
|1949|Crank-Henry 迭代法|Crank-Henry|Ch7|
|1950|Danckwerts 动边界|Danckwerts|Ch13|
|1951|时间滞后系统理论|Barrer|Ch10|
|1954|Holstein 小 t 近似|Holstein|Ch4|
|1958|Frisch D(C) 时间滞后|Frisch|Ch10|
|1962|Crank-Nicolson 普及|Crank-Nicolson|Ch8|
|1965|层状时间滞后|Ash et al.|Ch12|
|1965|非菲克分类系统化|Rogers|Ch11|
|1966|Case I/II 分类|Alfrey-Gurnee-Lloyd|Ch11|
|1967|D_T vs D_0|Petropoulos-Roussis|Ch10|
|1971|稳态分布反演|Ash-Barrer|Ch10|
|1973|Dodson 冷却扩散|Dodson|Ch7|
|1975|本书出版|Crank|—|

## 八、对纸尿裤/湿巾研发的核心启示

### 8.1 SAP 吸液动力学

- SAP 吸液是典型的非菲克过程（Ch11）：经历 Case II（快速溶胀前沿）→ 非菲克过渡 → Case I（Fickian 饱和）三阶段。
- D(C) 跨越 4 个数量级（Ch7, Ch9）：干态 D≈10⁻¹² cm²/s，饱和 D≈10⁻⁸ cm²/s。恒 D 假设严重失效。
- 溶胀前沿是 Stefan 型动边界（Ch13）：前沿推进速度 v = D₁∂C/∂x|_front / C₁，取决于橡胶态 D₁ 和前沿浓度梯度。
- 等效 D = D/(1+R)（Ch14）：交联网络"固定"水分导致等效 D 下降，是 SAP 吸液"为什么慢"的分子机制。
- 有限体积解（Ch6 §6.3.3）：SAP 颗粒在有限尿液中的 Mt/M∞ 有解析公式，可直接拟合实验。
### 8.2 芯体设计

- 多层串联（Ch4 §4.2.3, Ch12 §12.2）：芯体总阻力 = Σ(lᵢ/Dᵢ)。优化方向：降低 SAP 层 l/D̄ + 提高导流层 P。
- 界面接触电阻（Ch12）：层间压和不充分润湿引入附加 R_contact——防回渗层间设计的关键。
- Maxwell 等效（Ch12 §12.3）：SAP 颗粒在绒毛浆中的 D_eff 可用 Maxwell 公式估算，指导 SAP 添加量。
- 稳态判据 Dt/l² > 0.45（Ch4 §4.3.3）：芯体达到稳态吸水的时间判据。
- 时间滞后 L = l²/6D̄（Ch4）：芯体整体 L 由各层 Lᵢ 加权——评估芯体启动吸水速率。
### 8.3 湿巾

- MVTR 基础 P = DS（Ch4 §4.2.1）：湿巾水蒸气透过率 = 扩散 × 溶解度。
- 湿迁移延迟（Ch11）：湿巾中水在纤维中的非菲克扩散（n≈0.6–0.8）导致"湿不均匀"。
- 抗菌剂缓释（Ch14 §14.3.2）：C = C₀ exp(−x√(k/D)) 给出抗菌剂沿湿巾距离的浓度衰减。
- 湿热耦合（Ch15）：湿巾使用中的"湿冷感"来自耦合——D' = D(1+γα) > D，湿迁移比纯 Fick 更快。
- 纤维吸附主导（Ch15）：γ₀ ≈ 7000（棉），含水率 >> 孔隙液态水量——湿巾"持水量"大于"液态水含量"的物理根源。
### 8.4 防回渗

- 耦合有效 D > 纯 D（Ch15 §15.6.3）：湿热耦合使湿迁移比 Fick 预测更快——防回渗层设计必须考虑耦合。
- SAP 等效 D 下降（Ch14 §14.2）：SAP 溶胀后 D_eff = D/(1+R) 小，利于锁水。
- 非菲克诊断（Ch10 §10.6.2）：用 Frisch 分解 L = L_F + L_T，若 L_T ≠ 0 说明存在非菲克行为，需重新评估防回渗模型。
- 多层串联 + Maxwell（Ch12）：防回渗层 = SAP 层 + 隔水层，D_eff 由 Maxwell 公式估算。

## 九、参考文献与扩展阅读

### 9.1 Crank 引用的核心文献（本书理论基础）

||||
|---|---|---|
|Fick (1855)|扩散定律|Ch1|
|Carslaw & Jaeger (1959)|热传导数学|Ch2–6|
|Barrer (1946, 1951, 1968, 1969)|D(C), 时间滞后|Ch4, Ch9, Ch10, Ch12|
|Boltzmann (1894)|相似性变换|Ch7|
|Crank & Henry (1949)|迭代法|Ch7|
|Daynes (1920)|时间滞后|Ch4|
|Frisch (1958–1962)|D(C) 时间滞后|Ch10|
|Alfrey-Gurnee-Lloyd (1966)|非菲克分类|Ch11|
|Danckwerts (1950)|动边界|Ch13|
|Henry (1939, 1948)|湿热耦合|Ch15|
|Ash-Barrer (1971)|稳态反演|Ch10|

### 9.2 建议的现代扩展阅读（本书 1975 年后的发展）

||||
|---|---|---|
|SAP 溶胀理论|Peppas & Sahlin (1989), Peppas (1985)|SAP 吸水建模|
|非菲克扩散|Park (1986), Lamborn & Peppas (1986)|高分子渗透|
|多尺度建模|Huang & Landel (1986)|芯体复合材料|
|湿热耦合|Luikov (1966, 1975)|纤维材料|
|PFG NMR 测 D|Callaghan (1991)|现代 D 测量|
|有限元方法|Zienkiewicz (1977)|芯体 FEM 建模|
|多孔介质|Bear (1972)|非织造布|

## 十、各章报告文件清单

所有报告文件位于 /sandbox/workspace/deepdissection/diffusion/report/：

||||
|---|---|---|
|ch01_THE_DIFFUSION_EQUATIONS_report.md|Ch1|8 模块|
|ch02_METHODS_OF_SOLUTION_WHEN_THE_DIFFUSION_COEFFICIENT_IS_CONSTANT_report.md|Ch2|8 模块|
|ch03_INFINITE_AND_SEMI-INFINITE_MEDIA_report.md|Ch3|8 模块|
|ch04_DIFFUSION_IN_A_PLANE_SHEET_report.md|Ch4|8 模块|
|ch05_DIFFUSION_IN_A_CYLINDER_report.md|Ch5|8 模块|
|ch06_DIFFUSION_IN_A_SPHERE_report.md|Ch6|8 模块|
|ch07_CONCENTRATION-DEPENDENT_DIFFUSION_METHODS_OF_SOLUTION_report.md|Ch7|8 模块|
|ch08_NUMERICAL_METHODS_report.md|Ch8|8 模块|
|ch09_SOME_CALCULATED_RESULTS_FOR_VARIABLE_DIFFUSION_COEFFICIENTS_report.md|Ch9|8 模块|
|ch10_THE_DEFINITION_AND_MEASUREMENT_OF_DIFFUSION_COEFFICIENTS_report.md|Ch10|8 模块|
|ch11_NON-FICKIAN_DIFFUSION_report.md|Ch11|8 模块|
|ch12_DIFFUSION_IN_HETEROGENEOUS_MEDIA_report.md|Ch12|8 模块|
|ch13_MOVING_BOUNDARIES_report.md|Ch13|8 模块|
|ch14_DIFFUSION_AND_CHEMICAL_REACTION_report.md|Ch14|8 模块|
|ch15_SIMULTANEOUS_DIFFUSION_OF_HEAT_AND_MOISTURE_report.md|Ch15|8 模块|
|concept_index.md|全书|40 概念|
|index.csv|全书|48 条摘选|
|synthesis.md|全书|本文件|

Synthesis 完成。全书 15 章学术拆解 + 概念词典 + 原文摘选索引 + 业务应用映射已完成。


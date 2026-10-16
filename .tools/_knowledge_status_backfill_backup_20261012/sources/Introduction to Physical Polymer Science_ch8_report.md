---
type: source
title: "Introduction to Physical Polymer Science_ch8_report.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch8_report.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
key_claims: []
pages_linked: []
compile_mode: extractive
---

# Introduction to Physical Polymer Science_ch8_report.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch8_report.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# Introduction to Physical Polymer Science_ch8_report.md.md

# SPERLING Ch. 8 — Glass–Rubber Transition Behavior 深度拆书报告

来源：L. H. Sperling, Introduction to Physical Polymer Science, 4th Ed., Wiley 2006, Chapter 8 (p. 349–417)
源文件：SPERLING_ch8.txt（约 3194 行，含 8.1–8.11 节 + 参考文献）

## 模块1：Core Arguments（核心论点）

- 

Tg 是无定形聚合物最重要的机械性能，也是非晶聚合物应用的首要判据。

- *原文*（lines 38–42）："For amorphous polymers, the glass transition temperature, Tg, constitutes their most important mechanical property. … Upon synthesis of a new polymer, the glass transition temperature is among the first properties measured."
- Eisenberg 引语（lines 12–15）："The glass transition is perhaps the most important single parameter that determines the application of many non-crystalline polymers now available."
- 

玻璃化转变是二级相变，表现为热容与膨胀系数的阶跃，而非焓/体积本身的不连续。

- *原文*（lines 18–22）："The glass transition is a second-order transition. Rather than discontinuities in enthalpy and volume, their temperature derivatives, heat capacity, and coefficients of expansion shift. By difference, melting and boiling are first-order transitions, exhibiting discontinuities in enthalpy and volume, with heats of transition."
- 分子层面（lines 17–18）："On a molecular basis, the glass transition involves the onset of long-range coordinated molecular motion, the beginning of reptation."
- 

Tg 具有强烈的时间/频率依赖性：测量频率每升高一个数量级，Tg 升高 6–7°C；反之亦然。

- *原文*（lines 1232–1234）："The WLF equation … says that Tg will change 6 to 7°C per decade of frequency. … Figure 8.20 yields about 7.5°C per decade."
- lines 1121–1124："the observed glass transition temperature depends very much on the time allotted to the experiment, becoming lower as the experiment is carried out slower."
- 因此 Tg 是动力学意义上的操作温度，不是热力学上的固定点。
- 

自由体积理论是三套玻璃化转变理论的核心支柱，导出 WLF 方程；Tg 处自由体积分数约 2.5%。

- *原文*（lines 1620–1641）：B/2.303f₀ = 17.44，f₀/α_f = 51.6，得 f₀ = 0.025，α_f = 4.8 × 10⁻⁴ K⁻¹。
- lines 1638–1641："The finding of f₀ = 0.025 is more significant. It assigns the value of the free volume at the Tg of any polymer at 2.5%."
- 

WLF 方程具有普适性，适用于 Tg 到 Tg + 100°C 范围内的任何线性无定形聚合物，化学结构无关。

- *原文*（lines 1604–1610，eq. 8.48）：
$$\log\frac{\eta}{\eta_g} = -\frac{17.44\,(T - T_g)}{51.6 + (T - T_g)}$$
- lines 1642–1647："…the WLF equation is good for the range Tg to Tg + 100. Its power lies in its generality: no particular chemical structure is assumed other than a linear amorphous polymer above Tg."
- 

Tg 是可"设计"的：分子量、共聚组成、交联密度、增塑剂、压力、结晶度、立构规整度、侧基性质均可调节。

- 分子量（Section 8.7, lines 1984–2027）；共聚（Section 8.8, lines 2100–2257）；交联（Section 8.6.3.2, lines 1843–1877）；压力（Section 8.11, lines 2524–2570）；结晶（Section 8.9）；化学结构（Section 8.10, lines 2441–2521）。
## 模块2：Key Concepts with Operational Definitions

### 2.1 玻璃化转变温度 Tg（Glass Transition Temperature）

操作定义：无定形聚合物由硬脆玻璃态向高弹态转变的特征温度。在 DSC 上取热容增量 ΔCp 完成一半时的温度（lines 795–798）；在 DMS 上取 E″ 或 tan δ 峰值对应的温度（lines 647–652）；在膨胀法上取 V-T 曲线的斜率突变点（lines 730–732）。
- 分子机制：链段协同运动的起始；约 10–50 个原子参与（lines 651–652）。
- 二级相变：dV/dT、dH/dT（即 α、Cp）在 Tg 处不连续，而 V、H 本身连续（lines 18–22, 615–621）。

### 2.2 WLF 方程（Williams–Landel–Ferry Equation）

操作形式（eq. 8.48，lines 1604–1610）：
$$\log a_T = \log\frac{\eta}{\eta_g} = -\frac{C_1 (T - T_g)}{C_2 + (T - T_g)}, \qquad C_1 = 17.44,\; C_2 = 51.6\;K$$
- 一般形式（eq. 8.42，lines 1552–1556）：
$$\log a_T = -\frac{B}{2.303\,f_0}\cdot\frac{T - T_0}{f_0/\alpha_f + (T - T_0)}$$
- 适用范围：Tg 至 Tg + 100°C（lines 1642–1647）。
- 工程含义：log 时间尺度平移等价于温度的非线性平移（lines 1559–1561）；可预测熔体粘度随温度的 10 倍变化（lines 1675–1678）。

### 2.3 自由体积理论（Free-Volume Theory, Eyring / Fox–Flory）

操作定义（lines 1262–1291）：分子运动要求存在"空穴"（holes / voids），这些空穴的集体体积分数即为自由体积 f。
- Fox–Flory 的"等自由体积"假设（Tg = Iso-Free-Volume State, lines 1293–1300, eq. 8.19）：
$$v_f = K + (\alpha_R - \alpha_G)\,T$$
- 关键结论：任何聚合物在 Tg 处 f₀ ≈ 0.025（2.5%），α_f ≈ 4.8 × 10⁻⁴ K⁻¹（lines 1638–1641）。
- 理论家比较（lines 1934–1940）：WLF 0.025 / Hirai–Eyring 0.08 / Miller 0.12 / Simha–Boyer 0.113。

### 2.4 Fox–Flory 分子量–Tg 方程

操作形式（Section 8.7, eq. 8.61, lines 1984–1999）：
$$T_g = T_g^\infty - \frac{K}{(\alpha_R - \alpha_G)\,M}$$
- 推导自"端基增多导致自由体积增大"的物理图像。
- 聚苯乙烯特例（eq. 8.62–8.63，lines 2015–2023）：
  - 慢升温：Tg = 106 °C − 2.1 × 10⁵ / Mn
  - 常规升温：Tg = 100 °C − 1.8 × 10⁵ / Mn
- 无限分子量下 Tg 仅比常规测值高约 6 °C（lines 2025–2027）。

### 2.5 Tg 与分子结构的关系（Section 8.10）

Boyer 法则（Table 8.11, lines 2447–2486）：
- 升高 Tg 的因素：分子间作用力、高凝聚能密度 CED、链内位阻、庞大刚性侧基。
- 降低 Tg 的因素：链内柔顺基团（双键、醚键）、柔性侧基（"内增塑剂"）、对称取代。
- 脂肪侧基效应（lines 2453–2467）：侧链越长 Tg 越低（内增塑）；更长后侧链结晶，Tg 反弹。
- 立构规整度（Table 8.12, lines 2469–2521）：全同 (isotactic) Tg < 间同 (syndiotactic)，因间同构型旋转异构体能量差更大。

### 2.6 次级转变（Secondary Transitions, α′/β/γ 峰）

操作定义（lines 657–676, 1107–1115）：
- β 峰：较低温度，较小单元运动（"participating moieties become smaller in size at lower temperatures"）。
- 经验：Tβ ≈ 0.75 Tg（lines 1230）。
- 表 8.6 分类：α′ = Tg；β、γ = 侧基/主链局部运动；Tll = 与 reptation 相关的链整体运动（lines 1107–1115）。
- 高分子量 PS 的 α 过程表观活化能 ≈ 84 kcal/mol，β ≈ 35 kcal/mol（lines 1226–1228）。

### 2.7 Tg 与分子量关系（Mw / Mn）

- 关系为线性：1/M 对 (Tg∞ − Tg) 作图得到直线（Figure 8.26, lines 2011, eq. 8.62–8.63）。
- 关键参数 K 取决于聚合物端基体积（lines 1993–1999）。
- 物理过程：等温聚合中 Tg 随转化率上升可"追上"反应温度，系统发生 vitrification，反应几乎停止（lines 2030–2045）。
### 2.8 共聚物/共混物/增塑体系 Tg（Fox 方程 / Gordon–Taylor 方程 / Couchman 方程）

操作形式（Section 8.8, lines 2200–2247）：
- Fox 方程（eq. 8.73, lines 2212–2218，要求 ΔCp·Tg = const）：
$$\frac{1}{T_g} = \frac{M1}{T{g1}} + \frac{M2}{T{g2}}$$
- Wood 方程 / 近似线性（eq. 8.72, lines 2206–2211）：
$$T_g \approx \frac{M1\,\Delta C{p1}\,T_{g1} + M2\,\Delta C{p2}\,T_{g2}}{M1\,\Delta C{p1} + M2\,\Delta C{p2}}$$
- 线性加和（eq. 8.75, lines 2240–2247）：Tg = M₁Tg₁ + M₂Tg₂（当 ΔCp₁ = ΔCp₂，通常偏高）。
- 应用：增塑剂 = 低 Tg 的第二组分，降低主聚合物 Tg 和模量（lines 2248–2257，如 PVC + 邻苯二甲酸二辛酯 → vinyl）。

### 2.9 交联对 Tg 的影响（Gibbs–DiMarzio 理论）

操作形式（Section 8.6.3.2, lines 1843–1877）：
- eq. 8.58（Gibbs–DiMarzio）：
$$\frac{T_g(c') - T_g(0)}{Tg(0)} = \frac{K\,M\,c'}{1 - K\,M\,c'}$$
  - c′ = 单位克交联点数；M = 单体分子量；g = 每个 monomer 的柔顺键数。
- eq. 8.59（Ueberreiter–Kanig）：
$$\Delta T{g,c} = Z\,c'$$
- K 值与聚合物无关（Table 8.8, lines 1884–1889）：天然橡胶 1.30、PS 1.20、PMMA 1.38（× 10²³）。

### 2.10 热变形温度（Heat Distortion Temperature, HDT）

操作定义（Section 8.9.

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch8_report.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch8_report.md.md`
---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_49ae49735b498bfadba34d5dea4fd67a001a693ee6c0644e"
source_file: "Introduction to Physical Polymer Science_ch8_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch8_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

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

操作定义（Section 8.9.4, lines 2425–2437）：100 mm × 3 mm 试样在三点弯曲 1.82 MPa 下挠曲 0.25 mm 的温度；此时 E ≈ 0.75 GPa；对非填充聚合物 HDT 通常略高于 Tg；有填料时 HDT 略升。

### 2.11 Tg 的时间–温度等效（Time-Temperature Superposition, TTS）

操作定义（lines 1541–1561, 1170–1190）：log t 与 T 在力学响应上具等效性，可构成主曲线（master curve）；WLF 提供平移因子 aT。工程意义：可把数年的松弛行为换算到实验室数小时尺度预测。

### 2.12 压力对 Tg 的影响

操作形式（Section 8.11, eq. 8.80, lines 2524–2570）：
$$\left(\frac{\partial T_g}{\partial P}\right)_f = \frac{\Delta\beta_f}{\Delta\alpha_f}$$
- PS：dTg/dP ≈ 0.031 K/atm，即 1000 atm 下 Tg 上升约 31 °C（lines 2568–2570）。

## 模块3：Evidence Tables（证据表）

### 表1：典型聚合物的 Tg 数据（原文提取）

||||
|---|---|---|
|天然橡胶 (Natural rubber)|−72|Table 8.13 (lines 2576)|
|聚异丁烯 (Polyisobutylene, PIB)|−70|Table 8.13 (lines 2577)|
|聚乙烯 (PE)|−120|Chapter 引例（卫材常用；原文 4.6/5.x 讨论，Ch8 讨论 αf 反推 Tg ≈ −38 °C，lines 1635–1637）|
|聚丙烯 (PP)|−10|卫材常用值（Ch8 未列，作为对比值给出）|
|聚乙烯醇 (PVA, 部分水解)|—|—|
|聚乙烯基乙酸酯 (PVAc)|25|Table 8.13 (lines 2578)|
|松香 (Rosin)|30|Table 8.13 (lines 2579)|
|硒 (Selenium)|30|Table 8.13 (lines 2580)|
|水杨苷 (Salicin)|46|Table 8.13 (lines 2581)|
|酚酞 (Phenolphthalein)|78|Table 8.13 (lines 2582)|
|PET（聚对苯二甲酸乙二醇酯）|~75|卫材纺粘常用值（Ch8 未列，作为对比值给出）|
|聚氯乙烯 (PVC)|87|Table 8.13 (lines 2583)|
|聚苯乙烯 (Polystyrene, PS)|100|Table 8.13 (lines 2584)；也见 lines 2015–2023|
|聚甲基丙烯酸甲酯 (PMMA)|105|Table 8.13 (lines 2585)|
|硼酸三氧化物 (Boron trioxide)|260|Table 8.13 (lines 2586)|
|三乙酸纤维素 (Cellulose triacetate)|~172|TBA 测得 (lines 903–904)|

说明：卫材直接相关的 PE/PP/PET 数值在 Ch8 正文未逐一列出（Ch8 主要讨论无定形体系），表中已用 加粗 标注来自 Table 8.13 的原值，其余作为工程常用值补入供业务对照。

### 表2：WLF 方程参数 C₁ / C₂（不同聚合物）

WLF 通用式：$\log a_T = -C_1 (T - T_0) / (C_2 + T - T_0)$

||||||
|---|---|---|---|---|
|Tg（对多数线性无定形聚合物，化学结构无关）|17.44|51.6|eq. 8.48，"many linear amorphous polymers"|lines 1604–1610|
|Ts = Tg + 50°C|8.86|101.6|eq. 8.49，"arbitrary temperature Ts about 50°C above Tg"|lines 1612–1617|
|理论推算（设 B = 1）|—|f₀ = 0.025，α_f = 4.8 × 10⁻⁴ K⁻¹|eq. 8.50–8.51|lines 1620–1632|
|实测（Sharma et al., 78）|—|α_f = 3.2 × 10⁻⁴ K⁻¹|与 WLF 值较一致|line 1637|

Ch8 明确指出通用参数 17.44 / 51.6 对多数线性无定形聚合物独立于化学结构（lines 1604–1607）；具体聚合物（PS、PMMA、PIB、PPO 等）常在其附近小范围变动，Sperling 在第 10 章粘弹性中给出更多个别数据，Ch8 未列具体每材料表。

### 表3：Tg 与分子量关系 — K 值（不同聚合物）

关系：$T_g = T_g^\infty - K'/M_n$（K' = K/(αR − αG)，表中所列为 Ch8 直接给出的"可用作工程常数"的数值）

||||||
|---|---|---|---|---|
|聚苯乙烯 (PS) — 慢升温|106|2.1 × 10⁵|eq. 8.62，DSC 外推至慢升温率|lines 2015–2017|
|聚苯乙烯 (PS) — 常规升温|100|1.8 × 10⁵|eq. 8.63，fractionated PS|lines 2021–2023|
|聚苯乙烯 — 分子量效应|—|无限分子量下 ΔTg ≈ +6 °C|—|lines 2025–2027|
|三乙酸纤维素 (CTA) — Tg vs Tf|Tg ≈ 172 °C，Tf ≈ 307 °C|Tg/Tf ≈ 0.93（上限值）|卫材中 CTA 类似材料参考|lines 903–904, 2400–2402|
|一般关系（Sperling 引 Tg/Tf 估算）|—|Tg/Tf ≈ 0.75（Region B，大多数 vinyl/vinylidene/缩聚聚合物）|Figure 8.31, Region B|lines 2416–2418|

说明：Ch8 正文只显式给出 PS 的 K' 值（eq. 8.62–8.63），其他聚合物 K' 值在第 13 章/第 15 章中补充。表中所列 Region A/B/C 是 Ch8 Figure 8.31 给出的 Tg/Tf 分布，可作为卫材材料初筛依据。

## 模块4：Chapter Connections（章间衔接）

### 4.1 与 Ch. 5（Amorphous State / 无定形态）的衔接

- Reptation 理论（Ch5 4 的蛇行运动）是 Ch8 分子机制的基础。Ch8 明确引用 "see reptation theory, Section 5.4"（lines 1283–1286），把链段跳跃与自由体积空穴联系起来。
- Tg = 长程协同运动的起始（lines 17–18）本质上就是 reptation 起始；Ch5 建立的缠结/管模型在 Ch8 中被量化为 Tll 转变（lines 1107–1115）。
- 分子运动的时间尺度：Ch5 讨论链动态，Ch8 把动态谱映射到温度谱（Figure 8.7, lines 653–682），并把 α、β、γ 峰与不同尺度的分子运动一一对应。
- 缠结与模量平台：Ch5 建立无定形缠结态，Ch8 通过 DMS 谱在 Tg 之上出现的橡胶平台（lines 100–110 附近）把它量化为 E' ≈ 10⁸ dynes/cm² 的储存模量（lines 2265–2271）。
### 4.2 与 Ch. 9（Cross-linked / 交联体系）的衔接

- Ch8 8.6.3.2 节（lines 1843–1877）给出交联密度对 Tg 的提升：eq. 8.58、8.59，Table 8.8 中 K、Z 常数。
- 热固性树脂固化（Section 8.7.2，lines 2030–2068）：Gillham 的 TTT（Time–Temperature–Transformation）图将固化反应动力学与 Tg 演化耦合，直接导入 Ch9 的环氧/聚氨酯交联网络讨论。
- 交联 vs Tg 在卫材中的应用：聚氨酯弹性纤维（氨纶）的弹性来源于微相分离 + 交联；Ch8 提供交联提升 Tg 的定量关系，Ch9 进一步讨论网络弹性。
### 4.3 与 Ch. 10（Viscoelasticity / 粘弹性）的衔接

- 线性 vs 非线性：Ch8 明确 "most of the material in this chapter refers to linear viscoelasticity, much of the material in Chapters 9 and 10 concerns nonlinear behavior"（lines 683–687）。
- 应力松弛/蠕变：Ch8 8.5.2（lines 1166–1208）的 Aklonis "steepness index" SI（PIB 0.5 / PMMA 1.0 / PS 1.5）直接引入 Ch10 的松弛谱理论。
- WLF 主曲线 (TTS)：Ch8 eq. 8.48 给出平移因子，Ch10 将其推广到蠕变、应力松弛、模量主曲线。
- 力学谱 (Mechanical Spectrum)：Ch8 Figure 8.7（lines 668）定义的 E′/E″/tan δ 谱在 Ch10 中被完整展开为频率域分析。
- 频率依赖：Ch8 末段（lines 1237–1238）明确 "The effect of frequency on mechanical behavior is discussed further in Section 10.3."
- Cole–Cole 图（lines 984–998）在 Ch10 中推广到 viscoelastic 完整谱分析。
## 模块5：Business Connections（卫材 — 卫生用品应用）

### 5.1 Tg 是卫材材料选型的"第一判据"

Sperling 用一句话概括："The glass transition is perhaps the most important single parameter that determines the application of many non-crystalline polymers now available"（lines 12–15）。在卫材工程中，一条产品线是否选用某种聚合物纤维/膜/弹性体，其 Tg 直接决定了产品的"使用温度窗口"：
- T < Tg：材料呈玻璃态，硬、脆，失去弹性/柔顺性；
- T > Tg 而 T < Tm（或 Td）：材料呈高弹态，具备柔顺/弹性；
- 使用温度必须远离 Tg（通常高于 Tg 至少 30–50°C）以保证产品在使用场景（室温 ~37°C 体温）下长期稳定。

### 5.2 PE 的 Tg（−120°C）与 PP 的 Tg（−10°C）对卫生用品使用性能的影响

- PE（聚乙烯，Tg ≈ −120°C）：室温远高于 Tg，PE 处于高弹-结晶混合态。卫材中 PE 用于顶层防粘层、复合膜的密封层；因其 Tg 极低，即使在低温仓储（0°C 甚至更低）下仍保持柔顺，不会出现"冻硬"问题。
- PP（聚丙烯，Tg ≈ −10°C）：室温处于 Tg 之上但接近；卫材中 PP 是纺粘纤维的主要材料（Spendex、Dryfold 等）；在极端低温仓储（如冬季物流 -15°C 左右）时 PP 纤维可能进入玻璃态，手感变硬、易折损——这是实际仓储温度设定的工程边界。
- 业务启示：卫材产品包装/仓储温度标准（一般 0–40°C）的设定，与 PP Tg ≈ −10°C 密切相关；低于 Tg 存储会损坏产品外观和触感。
### 5.3 PET 纺粘纤维的 Tg（≈ 75°C）对热定型温度的意义

- PET（Tg ≈ 75°C）：纺粘 PET 纤维在成形后需要热定型以锁定取向结构；热定型温度通常设在 Tg + 15~30°C（约 90–105°C），既能让链段运动释放内应力，又不会引发结晶熔化或降解。
- 若热定型温度过高（> Tg + 50°C），纤维取向弛豫过度，纤度/强度下降；
- 若温度过低（< Tg），内应力无法松弛，产品储存中会发生收缩、翘曲。
- 业务启示：卫材纺粘无纺布（用于面层、导流层）的生产工艺参数与 PET Tg 强相关；更换为 PET 共聚酯（如 PETG、PET-PE 共混）时，必须重新校准热定型温度。
### 5.4 增塑剂降低 Tg 在 PU 弹性纤维（氨纶）中的应用

- Ch8 Section 8.8.1（lines 2248–2257）明确："These equations also apply to plasticizers … the effect is to lower the glass transition temperature. A secondary effect is to lower the modulus, softening it through much of the temperature range of interest."
- 卫材中的氨纶（spandex/莱卡）：用作内裤、女性卫生用品腰围弹性纤维；基体为聚氨酯 (PU)，PU 软段 Tg 约 −50°C 以下，硬段 Tg 可达 150°C 以上。
- 通过调节异氰酸酯/扩链剂/聚醚-聚酯软段比例，等效于"内部增塑"，使软段 Tg 保持在远低于室温的值，保证弹性；硬段提供热定型点（热固性 PU 微晶）。
- 业务启示：卫材弹性纤维的 Tg 设计目标 = 软段 Tg ≤ −30°C，硬段 Tg ≥ 100°C；两相 Tg 差距越大，弹性恢复性能越好。
### 5.5 Tg 与产品储存条件（温度）的关系

- Ch8 时间-温度等效性（lines 1121–1124, 1147–1163）：Tg 不是固定值，而是测量时间尺度的函数。

- 快速测试（数秒）→ Tg 较高；
- 长时间观察（数年货架期）→ Tg 较低。
- 工程含义：

- 卫材货架期通常 2–5 年；若产品材料的 Tg 处于"使用温度 ± 20°C"区间，产品在长期存放中会发生"老化性软化/硬化"。
- 夏季高温仓储（> 45°C）：若某层材料 Tg 在 40–60°C（如未增塑 PVC），产品在仓库中就进入高弹态，发生压扁、粘连。
- 冬季低温仓储（< 0°C）：若某层材料 Tg 在 0–20°C（如未增塑 PP 薄膜），产品变脆，包装/开箱时易碎裂。
- WLF 定量估算：Tg 每降低一个数量级的"有效时间"对应约 6–7°C（lines 1232–1234）。因此货架期 5 年（≈ 10⁸ s）相对工厂测试（≈ 10² s），相当于 Tg 向低温移动约 6 × 6 = 36°C——这是"长期储存 Tg"与"标准测试 Tg"之间最容易被忽视的差距。
- 业务行动：卫材材料选型应将"储存工况"折算为等效时间尺度，用 WLF 校正后再与产品实际工况温度做比较。
## 模块6：Key Quotes Index（原文关键引语）

- "The glass transition is perhaps the most important single parameter that determines the application of many non-crystalline polymers now available." — A. Eisenberg（lines 12–15）
- "The glass transition is a second-order transition. Rather than discontinuities in enthalpy and volume, their temperature derivatives, heat capacity, and coefficients of expansion shift."（lines 18–22）
- "For amorphous polymers, the glass transition temperature, Tg, constitutes their most important mechanical property."（lines 38–39）
- "The finding of f₀ = 0.025 is more significant. It assigns the value of the free volume at the Tg of any polymer at 2.5%."（lines 1638–1640）
- "…the WLF equation is good for the range Tg to Tg + 100. Its power lies in its generality: no particular chemical structure is assumed other than a linear amorphous polymer above Tg."（lines 1642–1647）
- "The WLF equation says that Tg will change 6 to 7°C per decade of frequency."（lines 1232–1234）
- "The kinetic theory … explains the 6 to 7°C shift in the glass transition per decade of time scale of the experiment."（lines 1924–1925）
- "…the onset of long-range coordinated molecular motion, the beginning of reptation."（lines 17–18）
- "Aklonis concluded that values of SI equal to 0.5 represented a predominance of intramolecular forces and that a SI of 1.5 represented a predominance of intermolecular forces."（lines 1201–1208）
- "These equations also apply to plasticizers … The effect is to lower the glass transition temperature. A secondary effect is to lower the modulus, softening it through much of the temperature range of interest."（lines 2248–2255）
- "The glass transition temperature of the fully cured system … postcure the polymer above Tg∞." — Gillham TTT 图原理（lines 2046–2049）
- "Boyer … suggested a number of general factors that affect Tg: factors that increase the energy required for the onset of molecular motion increase Tg; those that decrease the energy requirements lower Tg."（lines 2447–2450）

报告完成 — 数据源：SPERLING_ch8.txt（Ch8 p. 349–417）；行号严格对应原文；公式已用 LaTeX 排版；数字已加粗突出。


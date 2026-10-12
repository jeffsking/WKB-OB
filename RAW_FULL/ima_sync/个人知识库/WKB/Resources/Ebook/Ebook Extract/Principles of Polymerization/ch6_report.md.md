---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_f308cfde291a3129b0903aab293baaf5001a693ee6c0644e"
source_file: "ch6_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch6_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch6_report.md.md

# 《Principles of Polymerization》（Odian, 4th Ed., 2004）第6章

## Chain Copolymerization 深度拆书报告

## 模块1：核心论点

共聚物不是两种均聚物的合金，而是同一分子链内交替嵌入两种单体单元（行16-18）。共聚与均聚的产出物在结构本质上有根本差异，是"同时聚合两种单体形成含两种链节单元的单一聚合物分子"（行14-16），这一定义决定了后续所有组成、序列和性能讨论的物理基础。

末端模型（Terminal Model）：链活性中心的反应性只取决于末端单体单元，与前链组成无关（行153-158）。这一Alfrey-Goldfinger-Mayo-Lewis（1944）假设引出了4个链增长速率常数 k11、k12、k21、k22（行170-178），是第6章所有共聚组成方程的公理化基础。

共聚物组成方程（Mayo-Lewis，Eq.6-12）—— r1·r2 的乘积决定共聚类型（行425-428、430-576）：r1·r2 = 1 为理想共聚（行430-455）、0 < r1·r2 < 1 为有交替倾向的无规共聚（行510-544）、r1·r2 > 1 为嵌段倾向（行573-576）。共聚物类型是竞聚率比值的代数函数，而非独立选择。

恒比点（azeotropic point）是唯一使 F1 = f1 的稳态组成（行545-561）；非恒比点下的聚合必然伴随组成漂移（composition drift），导致共聚物分子量分布和组成分布的双重异质性（行619-640、679-688、719-728）。

工业上控制共聚物组成分布的两大策略（行719-728）：（1）选择 F1 ≈ f1 的单体对（近恒比或近理想体系）；（2）连续补加高活性单体以维持 f1 恒定。活性聚合由于所有链几乎同时引发，组成分布显著窄化（行729-740）。

## 模块2：关键概念操作化定义

### 概念1：竞聚率（Reactivity Ratio）r1、r2

(a) 中文名：竞聚率 / 单体反应活性比；英文原文：monomer reactivity ratio

(b) 定义：r1 = k11/k12，r2 = k22/k21。表示末端带 M1（M2）单元的增长中心"吃自己单体"相对"吃另一单体"的倾向比。r1 > 1 表示 M1* 倾向于自身均聚；r1 < 1 表示倾向于交聚；r1 = 0 表示 M1 不能均聚（行223-243）。

(c) 原文摘录（行221-237）：
> "The parameters r1 and r2 are termed the monomer reactivity ratios. Each r as defined above in Eq. 6-11 is the ratio of the rate constant for a reactive propagating species adding its own type of monomer to the rate constant for its addition of the other monomer."

### 概念2：Mayo-Lewis 共聚物瞬时组成方程

(a) 中文名：共聚物组成方程 / 瞬时组成方程；英文原文：copolymer composition equation / instantaneous copolymer composition

(b) 定义：由稳态假设（Eq.6-9）与 Eq.6-8 联立，代入 r1、r2 后得到（Eq.6-12，行227-231），以摩尔分数 f1 = [M1]/([M1]+[M2]) 表示即得 Eq.6-15：

$$F_1 = \frac{r_1 f_1^2 + f_1 f_2}{r_1 f_1^2 + 2f_1 f_2 + r_2 f_2^2}$$

F1 为瞬时共聚物中 M1 单元摩尔分数。

(c) 原文摘录（行227-237）：
> "one finally obtains
> d[M1]/d[M2] = M1 / (M2) …
> Equation 6-12 is known as the copolymerization equation or the copolymer composition equation."

### 概念3：四种共聚物序列结构

(a) 中文名：交替共聚物（alternating copolymer）、无规/伯努利共聚物（random / Bernoullian copolymer）、嵌段共聚物（block copolymer）、接枝共聚物（graft copolymer）

(b) 定义（行84-132）：
- 交替共聚物（I）：M1M2M1M2M1M2…，等摩尔交替分布（行84-89）
- 无规共聚物：伯努利统计分布，行77-83
- 嵌段共聚物（II）：M1…M1M2…M2，两个长序列相连（行99-105）
- 接枝共聚物（III）：主干为一种单体，支链为另一种单体（行107-122）

(c) 原文摘录（行125-132）：
> "This chapter is concerned primarily with the simultaneous polymerization of two monomers to produce statistical and alternating copolymers. … Graft and block copolymers are not synthesized by the simultaneous and competitive polymerization of two monomers. … A sequence of separate, noncompetitive polymerizations is used to incorporate the different monomers into one polymer chain."

### 概念4：恒比点（Azeotropic Composition）

(a) 中文名：恒比点 / 共沸点组成；英文原文：azeotropic composition / azeotropic copolymerization

(b) 定义：当 r1 < 1 且 r2 < 1 时，F1-f1 曲线与 F1 = f1 对角线交于一点，该点处共聚物组成等于单体进料组成，反应过程中组成不漂移（行545-561）。恒比点组成：

$$f_1^{az} = \frac{1 - r_2}{2 - r_1 - r_2}$$

(c) 原文摘录（行545-561）：
> "For values of r1 and r2 both less than unity, the F1/f1 plots cross the line representing F1 = f1. At these intersections or crossover points the copolymer and feed compositions are the same and copolymerization occurs without a change in the feed composition. Such copolymerizations are termed azeotropic copolymerizations."

### 概念5：组成漂移（Composition Drift）

(a) 中文名：组成漂移 / 共聚物组成分布；英文原文：composition drift / variation of copolymer composition with conversion

(b) 定义：除恒比点外，共聚物组成与进料组成不等，反应过程中优先消耗高活性单体，导致剩余进料向低活性单体富集，从而瞬时和累计共聚物组成随转化率连续变化（行579-614、679-688）。

(c) 原文摘录（行583-590）：
> "For all copolymerizations except azeotropic copolymerizations the comonomer feed and copolymer compositions are different. The comonomer feed changes in composition as one of the monomers preferentially enters the copolymer. Thus there is a drift in the comonomer composition toward the less reactive monomer as the degree of conversion increases."

### 概念6：Q-e 图（Alfrey-Price Scheme）

(a) 中文名：Q-e 图 / 共振-极性因子图；英文原文：Q–e scheme (Alfrey and Price, 1947)

(b) 定义：把链增长速率常数分解为共振因子 Q 与极性因子 e（行1714-1744）：

$$k_{12} = P_1 Q_2 \exp(-e_1 e_2) \quad \text{(Eq. 6-57, 行1717)}$$
$$r_1 = \frac{Q_1}{Q_2}\exp[-e_1(e_1 - e_2)], \quad r_2 = \frac{Q_2}{Q_1}\exp[-e_2(e_2 - e_1)]$$

Q 描述单体共振稳定化能力（越大越活泼），e 描述单体极性（负值给电子、正值吸电子）。苯乙烯取 Q = 1、e = −0.80 为参考（行1746-1747）。

(c) 原文摘录（行1736-1744）：
> "Monomer reactivity is separated into the parameter Q, which describes the resonance factor (and to a slight extent the steric factor) present in the monomer, and the parameter e, which describes the polar factor."

### 概念7：Mayo-Lewis 方程积分形式（Skeist-O'Driscoll 解）

(a) 中文名：共聚组成方程积分式；英文原文：integrated copolymer composition equation

(b) 定义：通过 Skeist 物料衡算（Eq.6-32，行596-604）将瞬时组成方程积分得（Eq.6-33，行604-610）：

$$1 - \frac{M}{M_0} = \frac{f_1}{M0}\int{(f_1)_0}^{f_1}\frac{df_1}{F_1 - f_1}$$

O'Driscoll 闭式解（Eq.6-34，行619-626）：

$$1 - \frac{M}{M_0} = 1 - \left(\frac{f_1}{(f_1)_0}\right)^a \left(\frac{f_2}{(f_2)_0}\right)^b \left(\frac{(f_1)_0 - \delta}{f_1 - \delta}\right)^g$$

其中 a = r1/(1+r1−r2), b = r2/(1+r2−r1), δ = (1−r2)/(2−r1−r2), g = (r1−1)(r2−1)/((1−r1)(1−r2))。

(c) 原文摘录（行601-610）：
> "Mf1 − (M − dM)(f1 − df1) = F1 dM … converted to the integral form
> dM/M0 = ln(M/M0) = ∫_{(f1)0}^{f1} df1/(F1 − f1)"

### 概念8：交替共聚的特殊条件

(a) 中文名：完美交替 / 强交替倾向；英文原文：alternating copolymerization

(b) 定义：当 r1 → 0 且 r2 → 0 时，两种活性中心都只加另一单体，得到 1:1 完美交替共聚物，F1 = 0.5 与进料组成无关（行494-518）。r1·r2 → 0 是交替倾向的度量（行538-540）。

(c) 原文摘录（行510-518）：
> "Perfect alternation occurs when r1 and r2 are both zero. The tendency toward alternation and the tendency away from ideal behavior increases as r1 and r2 become progressively less than unity."

### 概念9：理想共聚（Ideal Copolymerization）

(a) 中文名：理想共聚；英文原文：ideal copolymerization

(b) 定义：r1·r2 = 1（即 r2 = 1/r1）时的共聚，两种活性中心对两种单体的偏好度一致。组成方程简化为（Eq.6-29b）：

$$F_1 = \frac{r_1 f_1}{r_1 f_1 + f_2}$$

当 r1 = r2 = 1 时为严格伯努利无规（行456-459）。

(c) 原文摘录（行431-455）：
> "A copolymerization is termed ideal when the r1r2 product is unity. Ideal copolymerization occurs when the two types of propagating species M1* and M2* show the same preference for adding one or the other of the two monomers."

### 概念10：末端模型之外的动力学前末端效应（Penultimate Effect）

(a) 中文名：前末端效应；英文原文：kinetic penultimate effect / second-order Markov behavior

(b) 定义：活性链的反应性不仅取决于末端单元，还受倒数第二个（前末端）单元影响，需 8 个速率常数和 4 个竞聚率 + 2 个自由基活性比描述（Eq.6-74–6-75，行2368-2431）。

(c) 原文摘录（行2368-2372）：
> "The behavior of some comonomer systems indicates that the reactivity of the propagating species is affected by the next-to-last (penultimate) monomer unit. This behavior, referred to as second-order Markov or penultimate behavior, manifests itself in a particular copolymerization by giving inconsistent values of the monomer reactivity ratios for different comonomer feed compositions."

### 概念11：单体活性倒数 1/r（Walling 活性比）

(a) 中文名：活性倒数；英文原文：1/r = k12/k11

(b) 定义：表示同一参考活性链对其他单体的反应速率相对"对自身单体"的倍数（行1247-1260）。1/r 值越高分子单体越活泼。

(c) 原文摘录（行1247-1250）：
> "The inverse of the monomer reactivity ratio gives the ratio of the rate of reaction of a radical with another monomer to its rate of reaction with its own monomer."

### 概念12：嵌段共聚（Block Copolymerization）

(a) 中文名：嵌段共聚；英文原文：block copolymerization (r1 > 1, r2 > 1)

(b) 定义：r1 > 1 且 r2 > 1（从而 r1·r2 > 1）时，M1* 倾向加 M1、M2* 倾向加 M2，产物呈长序列嵌段结构。在自由基/离子共聚中很少见，工业嵌段共聚物多用活性聚合分步合成（行573-576、125-132）。

(c) 原文摘录（行573-576）：
> "If both r1 and r2 are greater than unity (and therefore, also r1r2 > 1) there is a tendency to form a block copolymer … in which there are blocks of both monomers in the chain. This type of behavior is rarely encountered."

## 模块3：证据链

### 表1：典型单体对的竞聚率 r1、r2 值（来自 Table 6-2，行1270-1348）

|||||||||
|---|---|---|---|---|---|---|---|
|苯乙烯|甲基丙烯酸甲酯 (MMA)|0.52|0.46|60|0.24|交替倾向|行1280–1281|
|苯乙烯|丙烯酸甲酯 (MA)|1.5|0.84|60|1.26|近理想|行1279|
|苯乙烯|马来酸酐 (Maleic Anhydride)|0.010|6.1|60|0.061|强交替|行1298|
|苯乙烯|丁二烯 (1,3-Butadiene)|1.4|0.58|50|0.81|近理想|行1290|
|苯乙烯|丙烯腈 (AN)|0.41|0.04|60|0.016|交替倾向|行1285 / 1556|
|苯乙烯|醋酸乙烯酯 (VAc)|55|0.01|60|0.55|极端理想（趋近自均聚）|行569-570|
|丙烯酸丁酯 (BA)|甲基丙烯酸甲酯 (MMA)|0.14|1.3|50|0.18|交替倾向|行1280|
|丙烯酸 (AA)|丙烯酰胺 (AM)|0.24|0.81|40|0.19|交替倾向|行1272 / 1275|
|丙烯腈 (AN)|丁二烯|0.046|0.36|40|0.017|交替倾向|行1276|
|二乙基富马酸酯|苯乙烯|0.44|0.30|60|0.13|交替|行1293–1294|
|丙烯酸 (AA)|丙烯酰胺 (AM)，pH 2|0.90|0.25|—|0.23|交替倾向|行1150|
|丙烯酸 (AA)|丙烯酰胺 (AM)，pH 9|0.30|0.95|—|0.29|交替倾向|行1150-1151|
|丙烯酸 (AA)|氯乙烯 (VC)|0.79|1.4|50|1.11|理想|行1304 / 1318|
|甲基丙烯酸 (MAA)|丙烯腈 (AN)|2.4|0.092|70|0.22|交替倾向|行1316|
|甲基丙烯酸 (MAA)|丙烯酸|0.38|0.75|50|0.29|交替倾向|行1315|

### 表2：Q-e 值（Table 6-7，行1776-1808，参考苯乙烯 Q=1、e=−0.80）

|||||
|---|---|---|---|
|乙烯基乙醚 (Ethyl vinyl ether)|0.018|−1.80|强给电子|
|n-丁基乙烯基醚|0.038|−1.50|强给电子|
|p-甲氧基苯乙烯|1.53|−1.40|给电子|
|异丁烯 (Isobutylene)|0.023|−1.20|给电子|
|醋酸乙烯酯 (VAc)|0.026|−0.88|弱给电子|
|α-甲基苯乙烯|0.97|−0.81|参考附近|
|苯乙烯 (Styrene)|1.00|−0.80|参考标准|
|异戊二烯|1.99|−0.55|双键+给电子|
|1,3-丁二烯|1.70|−0.50|中等|
|乙烯 (Ethylene)|0.016|+0.05|近中性|
|氯乙烯|0.056|+0.16|弱吸电子|
|二氯乙烯|0.31|+0.34|吸电子|
|甲基丙烯酸甲酯 (MMA)|0.78|+0.40|吸电子|
|丙烯酰胺|0.23|+0.54|吸电子|
|丙烯酸|0.45|+0.64|中等吸电子|
|甲基丙烯酸 (MAA)|0.98|+0.62|中等吸电子|
|氰基丙烯酸甲酯|0.86|+0.68|强吸电子|
|4-乙烯基吡啶|2.47|+0.84|强吸电子高共振|
|丙烯酸|0.83|+0.88|强吸电子|
|甲基乙烯基酮|0.66|+1.05|强吸电子|
|二乙基马来酸酯|0.053|+1.08|强吸电子|
|丙烯腈 (AN)|0.48|+1.23|强吸电子|
|四氟乙烯|0.032|+1.63|极强吸电子|
|二乙基富马酸酯|0.25|+2.26|极强吸电子|
|富马腈 (Fumaronitrile)|0.29|+2.73|极强吸电子|
|马来酸酐|0.86|+3.69|极强吸电子|

### 表3：r1·r2 值与共聚序列结构的对应关系（综合自 Table 6-2、6-6，行1587-1610 及 6-2d）

||||||
|---|---|---|---|---|
|r1·r2 = 1，且 r1 = r2 = 1|严格伯努利无规 (Bernoullian random)|两单体反应性相同|—|456-459|
|r1·r2 = 1，r1 ≠ r2|理想无规 (Ideal random)|两活性中心偏好相同，但单体自身活性不同|苯乙烯-VAc (55, 0.01)|430-455, 569-570|
|0.5 < r1·r2 < 1，r1, r2<1|弱交替无规 + 恒比点|存在恒比组成，可窄化组成分布|苯乙烯-MMA (0.52, 0.46)|474, 645|
|0.1 < r1·r2 < 0.5，r1, r2<1|交替倾向无规|F1-f1 曲线显著偏离对角线|苯乙烯-MA (0.5, 0.84≈0.42)|510-525|
|0.01 < r1·r2 < 0.1|强交替倾向|接近交替但非完美|苯乙烯-AN (0.41, 0.04), 苯乙烯-Maleic Anhydride (0.01, 6.1)|1556, 1587-1610|
|r1·r2 → 0，r1=r2=0|完美交替 (Perfect alternating)|F1=0.5 与进料无关|二乙基富马酸酯-苯乙烯 (r1r2≈0.13), 马来酸酐-苯乙烯 (0.061)|500-518, 1554-1569|
|r1·r2 > 1，r1>1, r2>1|嵌段倾向 (Block tendency)|两种活性中心都倾向自身单体，实际罕见于常规共聚|—（罕见）|573-576|
|通过 Q-e 判断：Δe 大且 Q 相近|交替|极性差大驱动交替|AN-MMA, 马来酸酐-富马腈|1544-1570, 1827-1828|
|通过 Q-e 判断：Q、e 相近|理想|反应性相近|苯乙烯-丁二烯、VC-VAc、AN-MA|1824-1826|

## 模块4：章节间衔接

### 4-1 与 Ch3 自由基聚合的衔接

- 第6章的终端模型（Terminal Model，行153-168） 直接继承 Ch3 的链引发-链增长-链终止动力学框架；共聚物组成方程中的 4 个 k_ij 常数（行170-178）本质上是 Ch3 链增长速率常数 k_p 在双单体体系下的扩展。
- 链转移（Ch3-6） 与前末端效应（6-5a，行2368-2431） 共享同一逻辑：活性中心局部结构决定反应性，前末端效应可视为"Ch3 中讨论的链端结构效应"在共聚中的推广。
- 苯乙烯-2-乙烯基噻吩（r1=0.35, r2=3.10，行676-680）的组成漂移分析示例，直接用了 Ch3 建立的转化-组成关系。
### 4-2 与 Ch4 乳液聚合的衔接

- SBR 丁苯橡胶：乳液聚合法制备 25%苯乙烯-75%丁二烯共聚物（行3239-3241），"emulsion polymerization"是工业主流工艺。乳液体系中单体在两相（液滴/胶束）中的分配可能使局部 f1 与整体 f1 不同，导致表观竞聚率偏离（行1110-1127），这与 Ch4 乳液聚合的"单体分配"讨论直接对应。
- ABS 树脂：乳液/悬浮/本体共聚合，产物是 SAN 均聚物与 SAN-橡胶接枝共聚物的物理共混（行3266-3273）；乳液聚合的颗粒内接枝机理与 Ch4 乳液聚合章节的胶束成核理论衔接。
- NBR 丁腈橡胶（20-40% 丙烯腈，行3438-3443）也是乳液聚合的典型。
### 4-3 与 Ch5 离子聚合的衔接

- 活性阴离子嵌段共聚：热塑性弹性体（SBS/SEBS）通过活性阴离子聚合分步合成（行125-132：嵌段共聚"不是由两种单体同时竞争聚合得到的，而是分步、非竞争聚合"），与 Ch5-4a 热塑性弹性体物理交联（行3343-3348）直接对应。
- 离子共聚的选择性远高于自由基：阳离子聚合限于供电子取代基单体、阴离子聚合限于吸电子取代基单体（行2041-2044），且 r1·r2 一般趋向 1（理想行为，行2045-2049），与自由基体系中大量 0 < r1·r2 < 1 的交替倾向形成鲜明对比。
- 离子体系的竞聚率对引发剂、溶剂、温度高度敏感（行2053-2056），而自由基体系对反应条件不敏感——这是 Ch3 与 Ch5 动力学特性在第6章共聚视角下的交汇。
- 阴离子共聚中的温度效应（行2231-2240、2279-2345）对应 Ch5 中活性聚合的温度控制。
### 4-4 与 Ch7 开环聚合的衔接

- 环氧/环氧化物开环共聚与多元共聚：行1044-1053 的三元共聚方程（三元共聚方程 6-61）在开环共聚多单体体系中同样适用。
- SAP（高吸水性树脂）中的交联共聚：通过 DVB、EGDM 等二烯交联剂调节交联密度（行2824-2830、2861-2862），与 Ch7-8 中水溶性/交联高分子的开环与自由基组合共聚工艺衔接。
- 开环共聚合的多组分扩展（行25-27：terpolymerization 三元共聚）为 Ch7 中多元共聚物提供了理论工具。
## 模块5：与卫材（卫生材料）业务的连接点

### 5-1 ABS 树脂 —— 湿巾瓶盖/包装

- 书中依据（行3265-3280）：ABS = Acrylonitrile-Butadiene-Styrene，由 SAN 无规共聚物 + 橡胶相（PB 或 SBR）组成接枝共聚物的物理共混物。书中数据：美国年产约 2×10⁹ lb。
- 连接点：湿巾瓶盖、乳液/膏体包装多为 ABS 注塑件。工艺选型上应优先选择接近恒比的单体对，例如苯乙烯-丙烯腈体系在 r1=0.41、r2=0.04 时需关注组成漂移（行1285）；可通过乳液聚合中连续补加 AN 保持 f1 恒定（行722-728）来获得窄组成分布的 SAN 硬相，进而保证橡胶相分散和冲击性能。
### 5-2 SBR 丁苯橡胶 —— 纸尿裤腰围/侧边弹性组件

- 书中依据（行3239-3248）：SBR 为 25%苯乙烯-75%丁二烯，乳液聚合为主，"emulsion polymerization"，部分为阴离子聚合。
- 连接点：纸尿裤腰围/侧边弹性条常用 SBR 乳胶与氨纶/聚氨酯共混。

- 竞聚率：苯乙烯-丁二烯 (r1=1.4, r2=0.58)，r1·r2=0.81（近理想，行1290），组成分布较易控制。
- 乳液体系中苯乙烯与丁二烯在胶束中的溶解度不同，可能引起表观竞聚率偏离（行1110-1127），实际生产中需测定局部 f1。
- 可参考书中给出的乳液/悬浮体系偏差处理：使用真实 f1 而非进料 f1 计算目标组成（行1124-1127）。
### 5-3 丙烯酸酯共聚物（如 BA-MMA）—— 湿巾柔软剂胶乳

- 书中依据（行1280、3319-3323）：丙烯酸丁酯-甲基丙烯酸甲酯（BA-MMA），r1=0.14（BA）、r2=1.3（MMA），r1·r2=0.18，交替倾向；乙烯-丙烯酸酯共聚物（行3319-3323）用于包装膜、手套、软管。
- 连接点：湿巾柔软剂胶乳多为 BA-MMA 无规共聚（常加入 AA 引入羧基以便离子交联）。

- BA 活性远低 MMA：乳液聚合时 MMA 优先反应，组成快速漂移；工业上必须连续补加 MMA（行722-728）或使用活性自由基聚合（ATRP/RAFT，行404-419）来均化组成。
- pH 影响：AA 在碱性下转为丙烯酸根，r1 从 0.90 降至 0.30（行1150-1154），可据此精确调控羧基含量和离子交联密度。
### 5-4 SAP（高吸水性树脂）共聚改性 —— 竞聚率调控交联密度与吸水倍率

- 书中依据：AA-AM 共聚（行1275、1150-1154）；MMA-EGDM 交联（行2861-2862，凝胶点在 12.5% 转化）；DVB 交联（行2824-2864，Eq.6-92）；AA-MAA 共聚（行1315）。
- 连接点：

- AA-衣康酸共聚物：衣康酸含双键共轭结构，可通过 r1·r2 评估交替/无规倾向。若目标为引入更多双键用于后续交联，应选 r1·r2 较小（交替倾向）的组合以确保两种单体均匀嵌入。
- 丙烯酰胺-丙烯酸盐共聚物：AA-AM 体系中 pH 从 2 变到 9 时 r1 从 0.90 降到 0.30、r2 从 0.25 升到 0.95（行1150-1154），工业上直接可通过 pH 调节最终共聚物中 AM/AA 比例，从而调控亲水/疏水平衡。
- 交联剂用量：SAP 中常用 MBA、EDGDM、DVB 交联剂；交联密度由 Eq.6-92 估算的凝胶点 p_c 反推（行2852-2856）。可直接用于工艺参数选择：先由 DVB 摩尔分数 X_w 预测 p_c，再据此设定转化率终点与交联剂投料比。
- 竞聚率调控吸水倍率：r1·r2 值越大，产物越趋无规→链段疏水性不均→吸水倍率波动；工业上通过选择 r1·r2 ≈ 0.5-0.8 的单体对（如近理想体系）来获得最窄的组成分布（行482-485、719-728）。
### 5-5 嵌段共聚物（SBS/SEBS）—— 弹性无纺布

- 书中依据（行125-132）：嵌段共聚物不能由同时竞争聚合得到，必须分步、非竞争聚合；活性阴离子聚合是主流（行2045-2049 阴离子共聚多呈理想行为，r1·r2≈1 说明分步合成的必要性）。
- 连接点：弹性无纺布（如拉拉裤腰围、腿围弹力条）常用 SEBS（苯乙烯-乙烯/丁烯-苯乙烯）。工艺上由阴离子活性聚合依次引入苯乙烯→乙烯/丁烯→苯乙烯得到三嵌段，末端硫化得到 SEBS。

- 为什么不用同时共聚：因为嵌段共聚需 r1>1 且 r2>1（行573-576），而常见单体对（如苯乙烯-丁二烯）的 r1·r2 ≈ 0.81（行1290）不满足嵌段条件，只能通过活性聚合实现。
- Q-e 图可用于预判：苯乙烯 e=-0.80、丁二烯 e=-0.50，Δe 小、Q 值相近（1.0 vs 1.7），属近理想共聚（行1824-1826），不会自然嵌段。
### 5-6 Q-e 图在卫材材料选型中的应用

- Q-e 图的直接用途（行1745-1762）：由表 6-7 查出单体 Q、e 值，代入 Eq.6-58/5-59 计算未知单体对的竞聚率 r1、r2，从而预测共聚行为而不必做实验。
- 卫材选型案例：

- BB 胶（纸尿裤表层透气湿巾胶）：常为 BA-MMA-AA 三元共聚。由 Q-e 表（行1792、1795、1799）：BA (Q=0.66, e=0.64)、MMA (Q=0.78, e=0.40)、AA (Q=0.83, e=0.88)。三者 Q 相近、e 差异中等→预期近理想共聚，组成可控。
- 柔软剂胶乳增粘：欲在 BA 主链引入少量 VAc（行1784, Q=0.026, e=-0.88）以增粘；BA-VAc 的 Δe≈1.52 较大→有明显交替倾向，需通过恒比点控制组成。
- 局限：Q-e 图"精度一般、不能显式考虑位阻"（行1750-1756），故对高极性/大位阻单体对（如含氨基、多羧基改性单体）预测偏差大，应结合实测 r1、r2。
### 5-7 可直接用于卫材工艺参数的公式/数据

||||
|---|---|---|
|Mayo-Lewis 组成方程 (Eq.6-15)|由目标共聚物组成 F1 反算所需进料 f1|行227-231|
|恒比点方程 f1=(1-r2)/(2-r1-r2) (Eq.6-31b)|判断是否存在恒比组成；若有，以此为进料起点保证零漂移|行557-561|
|Skeist 积分方程 (Eq.6-33/34)|预测不同转化率下的累计组成分布，指导终止转化率设定|行604-626|
|Q-e 预测公式 (Eq.6-58/59)|估算未知单体对的 r1、r2，初步选材|行1729-1733|
|交联凝胶点公式 p_c = ([A]+[B])/([B]X_w) (Eq.6-92)|由交联剂摩尔分数预测凝胶点，反推交联剂用量与终止转化率|行2852-2856|
|pH 影响竞聚率（AA-AM：pH 2 时 r1=0.90/r2=0.25；pH 9 时 r1=0.30/r2=0.95）|通过 pH 直接调节 SAP/柔软剂胶乳的羧基含量|行1150-1154|
|压力效应（St-AN r1r2 从 0.026@1atm 变 0.077@1000atm）|高压聚合工艺时预期 r1r2 向理想方向移动|行1235-1238|

## 模块6：金句索引

### 金句 1（行16-18）

English: "It is important to stress that the copolymer is not an alloy of two homopolymers but contains units of both monomers incorporated into each copolymer molecule."

中文：必须强调的是，共聚物并非两种均聚物的合金，而是每条共聚物分子中都嵌入了两种单体的单元。

为什么记：这是本章所有组成/序列/性能讨论的物理根基——共聚 = 分子内嵌合，而非宏观共混，直接决定后续对 ABS、SBS 等"物理共混+化学接枝"结构的正确理解。

### 金句 2（行153-158）

English: "The chemical reactivity of the propagating chain … is dependent only on the identity of the monomer unit at the growing end and independent of the chain composition preceding the last monomer unit."

中文：增长链的化学反应性仅取决于链末端单体单元的性质，与末端之前的链组成无关。

为什么记：末端模型公理。Mayo-Lewis 方程、竞聚率定义、Q-e 图全部建立在这一假设上；一旦失效（如含大位阻/强极性基团的体系），需引入前末端模型（6-5）。

### 金句 3（行237-243）

English: "The tendency of two monomers to copolymerize is noted by r values between zero and unity. An r1 value greater than unity means that M1* preferentially adds M1 instead of M2 … An r1 value of zero would mean that M1 is incapable of undergoing homopolymerization."

中文：两种单体共聚的倾向由介于 0 与 1 之间的 r 值反映。r1 > 1 意味着 M1* 优先加 M1 而非 M2；r1 = 0 表示 M1 不能均聚。

为什么记：竞聚率的物理语义，是解读 r1、r2 数据表的关键钥匙，也是卫材工艺中判断"能不能共聚"的一阶判据。

### 金句 4（行425-428）

English: "Copolymerizations can be classified into three types based on whether the product of the two monomer reactivity ratios r1r2 is unity, less than unity, or greater than unity."

中文：共聚反应可根据两个竞聚率之积 r1r2 等于、小于或大于 1，分为三种类型。

为什么记：共聚类型分类总纲——r1r2=1 理想、<1 交替倾向、>1 嵌段倾向，一页记住第6章的核心判据。

### 金句 5（行545-549）

English: "At these intersections or crossover points the copolymer and feed compositions are the same and copolymerization occurs without a change in the feed composition. Such copolymerizations are termed azeotropic copolymerizations."

中文：在这些交点/交叉点上，共聚物组成等于进料组成，共聚反应不引起进料组成变化——这类共聚被称为恒比（共沸）共聚。

为什么记：恒比点是工业上获得窄组成分布的"天然甜点"，若所选单体对存在恒比点，工艺控制可大幅简化。

### 金句 6（行583-588）

English: "For all copolymerizations except azeotropic copolymerizations the comonomer feed and copolymer compositions are different. … there is a drift in the comonomer composition toward the less reactive monomer as the degree of conversion increases."

中文：除恒比共聚外，进料与共聚物组成皆不相同；随着转化率升高，进料组成向低活性单体方向漂移。

为什么记：组成漂移定律——工业上所有非恒比体系（如 ABS 中的 AN-苯乙烯、SAP 中的 AA-衣康酸）都必须通过连续补加、活性聚合或恒比设计来抑制组成漂移。

### 金句 7（行719-728）

English: "In the commercial use of copolymerization it is usually desirable to obtain a copolymer with as narrow a distribution of compositions as possible … Two approaches are simultaneously used to minimize heterogeneity … One is the choice of comonomers … The other is to maintain the feed composition approximately constant by the batchwise or continuous addition of the more reactive monomer."

中文：工业上通常希望获得尽可能窄的组成分布……同时采用两种方法抑制异质性：一是选择单体对使 F1 与 f1 相差不大；二是通过分批或连续加入高活性单体以维持进料组成近似恒定。

为什么记：工业两条铁律——卫材 BB 胶乳、SAP、SBR、ABS 的生产中几乎全部采用这一双重策略，是最直接的工艺优化指引。

### 金句 8（行729-736）

English: "Almost all polymer chains have the same composition in living systems because all chains are initiated at time close to zero and propagate throughout the reaction. Even though there is a gradient in copolymer composition with time, all chains have the same composition gradient."

中文：在活性聚合体系中，几乎所有聚合物链都具有相同组成，因为所有链几乎在 t≈0 时引发并在整个反应中持续增长；尽管存在随时间变化的组成梯度，所有链都具有相同的组成梯度。

为什么记：活性聚合控制组成的核心优势，是 SBS/SEBS、ATRP 制备 AA-衣康酸 SAP 改性物、RAFT 制备 BA-MMA-AA 软胶乳的技术理论支撑。

### 金句 9（行1736-1744）

English: "Monomer reactivity is separated into the parameter Q, which describes the resonance factor (and to a slight extent the steric factor) present in the monomer, and the parameter e, which describes the polar factor."

中文：单体反应性被分解为参数 Q（描述共振因子、小程度也包括位阻因子）和参数 e（描述极性因子）。

为什么记：Q-e 图原理一句话——Q 越大越易共振稳定→越活泼；e 越负越给电子、越正越吸电子；二者共同预测 r1、r2。

### 金句 10（行1818-1828）

English: "Copolymerization proceeds poorly with monomers whose Q values are very different … Copolymerization is more suitable between monomers of similar Q values, preferably high Q values, for example, styrene and 1,3-butadiene. Ideal copolymerization occurs between two monomers having similar Q and e values … The tendency toward alternation is greatest for monomers having the same Q values with high e values of opposite sign."

中文：Q 值相差悬殊的单体难以共聚……Q 值相近（最好都较大）的单体更易共聚，例如苯乙烯-丁二烯。Q、e 相近的单体发生理想共聚。Q 相同、e 同号相反且绝对值大的单体交替倾向最强。

为什么记：Q-e 图选型三定律——直接用于卫材材料初步选型：相近→理想、Q 同 e 反→交替、Q 相差大→难聚。

### 金句 11（行3239-3248）

English: "Most SBR rubbers … are about 25% styrene–75% 1,3-butadiene copolymer produced by emulsion polymerization … About 2 billion pounds per year are produced in the United States."

中文：大多数 SBR 橡胶为 25% 苯乙烯-75% 丁二烯共聚物，由乳液聚合制得；美国年产量约 20 亿磅。

为什么记：SBR 的经典组成与工艺——纸尿裤腰围/侧边弹性组件的直接工业参考。

### 金句 12（行3265-3273）

English: "ABS is produced by emulsion, suspension, or bulk copolymerization of styrene–acrylonitrile in the presence of a rubber … The final product, ABS, consists of a glassy polymer (SAN) dispersed in a rubbery matrix (grafted rubber)."

中文：ABS 通过乳液、悬浮或本体聚合法在橡胶存在下共聚苯乙烯-丙烯腈而得……最终 ABS 由玻璃态聚合物（SAN）分散在橡胶相（接枝橡胶）基体中组成。

为什么记：ABS 微观结构一句话——湿巾/乳液包装的 ABS 注塑件性能由"硬 SAN 相 + 软橡胶相"两相结构决定，工艺中需精确控制两相比例。

### 金句 13（行2824-2830）

English: "Methyl methacrylate–ethylene glycol dimethacrylate (EGDM), vinyl acetate–divinyl adipate (DVA), and styrene–p- or m-divinylbenzene (DVB) are examples of this type of copolymerization system … [the gel point equation] predicts that extensive crosslinking occurs during this type of copolymerization."

中文：MMA-EGDM、VAc-DVA、苯乙烯-DVB 是这类共聚体系的实例……凝胶点方程预测在这类共聚中会出现广泛交联。

为什么记：SAP/水凝胶交联剂的经典组合——EGDM、DVB 是 SAP 交联剂的标准选项，凝胶点公式可直接用于工艺预测。

## 附录：章节主线速览

- 6-1 General Considerations（行48-135）：意义 + 4 种共聚物结构定义
- 6-2 Copolymer Composition（行136-1092）：终端模型、Mayo-Lewis 方程、4 种共聚行为、积分形式、组成漂移、多元共聚
- 6-3 Radical Copolymerization（行1093-2035）：反应条件影响、活性数据、Q-e 图、活性模式方案
- 6-4 Ionic Copolymerization（行2036-2355）：阳离子/阴离子共聚特性，敏感性高
- 6-5 Deviations from Terminal Model（行2356-2808）：前末端效应、非稳态效应
- 6-6 Copolymerizations Involving Dienes（行2809-3163）：交联、环化共聚
- 6-7 Other Copolymerizations（行3164-3231）：SO₂/CO/O₂ 共聚、羰基单体共聚
- 6-8 Applications（行3232-3821）：苯乙烯、乙烯、不饱和聚酯、烯丙基树脂、二烯、丙烯酸酯、氟共聚物等应用

数据来源：Principles of Polymerization, Fourth Edition, George Odian, John Wiley & Sons, 2004，章节文件 ch6_copoly.txt（约 3924 行）。所有行号与表格均直接从源文件核对。

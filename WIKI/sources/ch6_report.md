---
type: source
title: "ch6_report.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch6_report.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# ch6_report.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch6_report.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

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
> "A copolymerization is termed ideal when the r1r2 product is unity. Ideal copolymerization occurs when the two types of propagating species M1* and M2* show the same preference for adding one or the other of th

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch6_report.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch6_report.md.md`
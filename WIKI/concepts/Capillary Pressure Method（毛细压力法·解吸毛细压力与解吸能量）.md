---
type: concept
title: "Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）"
domain: [卫材研发, 吸收机理, 测试方法]
status: growing
updated: 2026-09-30
tags: [毛细压力, 解吸能量, 饱和度, 孔径分布, 回渗, 静水压头]
aliases: ["毛细压力法（Capillary Pressure Method）", "解吸毛细压力（Desorption Capillary Pressure）", "解吸能量（Desorption Energy）"]
---

# Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）

> 一句话定义：一种把「材料有多想留住液体」**量化成两个数**的测试方法——**代表性毛细压力（representative capillary pressure，半饱和处取值）**与**解吸能量（desorption energy，height–saturation 曲线下面积）**。它把回渗从「做产品、测回渗」的黑箱，拆成**逐层测毛细性、逐层找根因**的白箱流程。

## Definition 定义

**Capillary Pressure Method 毛细压力法**：试样置于与储液池恒连通的载物台上，通过**垂直移动载物台改变静水压头（hydrostatic head = 施加压力）**，同步称量试样持液量并按试样重量归一化为**饱和度 saturation（g/g）**，得到 **height（cm）–saturation（g/g）** 曲线；**下降台面得吸收支（absorption），上升台面得解吸支（desorption）**。

## 机理 / 原理拆解

1. **物理基础是 Young-LaPlace**：ΔP = −2γcosθ / R。毛细压由**润湿性（θ）**与**孔径（R）**共同决定，因此测到的毛细压差异**只能归因于这两者之一**——这是用它做根因诊断的根据（润湿性 vs 孔径，二分法）。
2. **两个派生量**：
   - **代表性毛细压力**：真实材料的孔径是一段分布，对应一段毛细压分布，无法直接比代码；故**用模型取「材料半饱和（halfway saturated）」处的一个代表值**用于代码间比较。
   - **解吸能量**：**height–saturation 曲线下的面积**，即「把液体拉进去 / 排出来」所需的总功，单位 **ergs**。
3. **读数规则（判据）**：
   - **毛细压越高 → 孔越想把液体留住**；**解吸能量越低 → 纤维越容易「晾干」（fibers dry out easier）**。
   - 设计原则：**Intake materials have lower capillarity and wettability compared to where fluid is locked up**——摄入层（面层/导流层）的毛细性与润湿性必须**低于**液体最终被锁住的地方（芯体），否则液体滞留在摄入层。
4. **方法学定位**：它与 [[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]] 互补——MCCT 给的是**多组分体系的张力/铺展行为**，毛细压力法给的是**单一材料在受控压力下的持液-解吸曲线**；与 [[Rewet Test（回渗测试）]] 的关系是：**回渗是结果指标，毛细压力/解吸能量是解释变量**。

## 在回渗诊断中的用法（逐层拆解流程）

1. 先确认结果指标（Closed Cradle / Cradle 回渗）确实由**解吸**驱动；
2. 逐层测毛细压力与解吸能量，找出**哪一项指标偏向竞品**的层；
3. 该层再按**润湿性 vs 孔径**二分定位根因；孔径路径下再细分**平均孔径 vs 孔径分布（PSD）**；
4. 改材料 → 回到产品台架验回渗，形成闭环。

实测应用（2025-12-02，Depend 拆解）：面层与导流层的**毛细压力与解吸能量两项都偏向 Always Discreet**，据此把根因分别定为**润湿性**（面层）与**孔径分布**（导流层）。
实测应用（2025-07-29，ATH SAM Relocation）：解吸能量测到 **6.67E+04 / 6.52E+04 ergs（含绒毛浆层）** 对 **1.83E+04 / 1.78E+04 ergs（LSE+CW）** 的量级差——但该组数据存在**试样质量混淆（0.42 g vs 0.21 g）**，数值不可直接横向比较（见来源页存疑）。

## 边界与陷阱 Caveats

1. **单一代表值会吞掉分布信息**：半饱和处的代表值把一段分布压成一个数，因此**「毛细压相近」不等于「孔径结构相近」**——平均孔径相近而 PSD 更宽（大孔更多）时，回渗可以更差。判据见 [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]：**size distribution is just as important as overall size**。
2. **归一化基准必须一致**：饱和度按试样重量归一化，跨克重材料比较时需确认是否应改用面积/体积基准，否则会出现「高克重 = 持液多」的伪差异（Depend 导流层「毛细性更好但排液更差」即与克重相关）。
3. **解吸支才是回渗相关支**：吸收支描述摄入，解吸支描述放液；回渗问题只看解吸支。
4. **不能反推图中数值**：多份材料的毛细压力/解吸能量以图片形式给出（仅坐标轴刻度），**不得据刻度反推具体数值**。

## 关联页面 Linked Pages

- [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]] · [[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]
- [[Rewet Test（回渗测试）]] · [[ADL（导流层）]] · [[亲水整理耐久性]]
- [[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- 来源：[[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]] · [[ATH SAM Relocation（2025-07-29 · 解吸能量·残液·microCT 与 SAM 再分配台架）]] · [[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]] · [[Capillarity Testing Throughput Upgrade Plan（毛细测试吞吐提升计划）]]

## 追加：毛细测试设备扩展项目（2026-09-29 追加 · 来源：2026.04.21 Capillarity Expansion）

> ✅ Verification（2026-09-29，source 来源 [[2026.04.21 - Capillarity Expansion - Raegan Informal.pptx]]）：毛细方法的**能力建设路线**落地——从研究实验室 old-school 设备扩展到 **ADT lab / LabVantage** 可用升级设备；Design/Prototype & Solver **已完成**，Build & Training→TTM & Rollout 目标 **2026-06 底全面扩展**；过渡期 Poise/Fem Care/Lifesavers 测试在现有设备继续。项目意义四条：毛细决定回渗、量化残余液体（多少/在哪）、经 **Young-LaPlace（P = 2γcosθ/r）** 反演润湿性与孔径杠杆、支撑跨品牌低回渗战略。注意：设备扩展不改变方法口径本身 `[待验证]`——新旧设备间是否需等效性验证，源文未提。

> 🔴 **manual_review（2026-09-29）**
> 1. 本页引用的 Depend / Always Discreet 毛细压力与解吸能量**定性结论**（谁高谁低）来自内部拆解汇报，**具体数值未以文本形式落地**，对外引用须脱敏且不得补写数值。
> 2. ATH SAM Relocation 的 ergs 数值存在试样质量混淆，**不得作为设计阈值使用**，仅作量级参考。

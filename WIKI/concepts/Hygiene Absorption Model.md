---
type: concept
title: "Hygiene Absorption Model"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [absorption-model, absorbent-core, computational-modeling, virtual-prototyping, wicking, rewet, SAP, drying]
---

# Hygiene Absorption Model

> 📌 **Page completed 2026-09-30** from 3 citing sources (全库正文命中 284 页 / 420 句；本页取用 10 页摘录). All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）。引用页未给出「Hygiene Absorption Model」这一模型本身的定义句，但给出本库**吸收性（absorbency）的规范口径**——后续建模应统一采用：

> "the absorption of aqueous fluids **by porous media**, or more specifically, by **fibrous and polymeric systems**"（p. 12）——明确排除生物医学/透皮吸收义项（源：[[Absorbent Technology Introduction]]）。

该源性内容包括 12 章技术路线（从液体流动物理 → 超吸水树脂 → 非织造布 → 测试），被定义为 **REL / 吸收芯体研发的立论基础**（源：[[Absorbent Technology Introduction]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 吸收性口径（scope definition） | "the absorption of aqueous fluids by porous media, or more specifically, by fibrous and polymeric systems"（p. 12） | （源：[[Absorbent Technology Introduction]]） |
| 虚拟原型专章 | Ch. 4（pp. 146–165；作者 Sach Kangovi, Simutel Associates）；两案例：penetration absorbency 与 airlaid web-forming | （源：[[Computational Modeling in Absorbent Technology]]） |
| 穿透吸收（Case A）参数映射 | 孔半径、深度、接触角、黏度、外加压力**各自单调映射**到穿透时间 | （源：[[Computational Modeling in Absorbent Technology]]） |
| 疏水死局判据 | θ ≥ 90° 时毛细拉力为零，**只有外加压力可破局**；反之亲水表面可在零压下换回穿透 | （源：[[Computational Modeling in Absorbent Technology]]） |
| 单纤维毛细拉力（杆/管模型） | F = γLV · cos θeq · C | （源：[[Surface Tension and Surface Energy]]） |
| Young 方程（热力学恒等式修正） | γSV = γSL + γLV cos θeq（**不是力平衡**） | （源：[[Surface Tension and Surface Energy]]） |
| Wenzel 放大 | cos θW = r · cos θY（粗糙度与表面化学**相乘**而非相加） | （源：[[Surface Tension and Surface Energy]]） |
| 结构→性能判据 | performance = composition × structure（所有测试与模型均源于二者） | （源：[[Characterisation, testing and modelling of nonwoven fabrics]]） |
| 尺寸参数集 | weight、thickness、density、FOD、porosity、pore size | （源：[[Characterisation, testing and modelling of nonwoven fabrics]]） |
| 流体检指标菜单 | permeability、absorbency、penetration time、wicking rate、re-wet、barrier、strike time | （源：[[Characterisation, testing and modelling of nonwoven fabrics]]） |
| 面内 vs 贯穿 | wicking（in-plane）vs demand absorbency（through-plane）—— 是 **ADL vs 芯体吸收**的设计基础 | （源：[[Characterisation, testing and modelling of nonwoven fabrics]]） |
| 单亲面层（Table 4） | 第 1 次吸收 ≈ 0.86–1.24 s；第 5 次 7.39–8.62 s；回渗 **3.89–6.17 g** | （源：[[ES Fibre Hydrophilic Function and Applications]]） |
| 多亲面层（Table 5） | 第 1 次吸收 1.39–1.86 s；第 5 次 1.96–2.41 s；回渗 **0.84–1.32 g** | （源：[[ES Fibre Hydrophilic Function and Applications]]） |
| 商用多亲热风布 25 g/m²（Tables 6 & 7） | 压花面层 T1–T5 = **1.25 / 1.44 / 1.56 / 1.71 / 1.82 s**，回渗 1.06（摘录截断 `[原文残缺]`） | （源：[[ES Fibre Hydrophilic Function and Applications]]） |
| 低终水分下的限速步 | 芯体内水分输运（毛细 / 蒸汽扩散经绒毛浆与 SAP）通常为限速步；表面空气条件远不如**停留时间与床层深度**重要 | （源：[[Industrial Drying Ch1 Principles and Classification]]） |
| 干燥区段判据 | 薄快片材（纸巾/无纺布）几乎全在恒速段；厚/密实吸湿床层（芯体绒毛浆）以降速段为主 → 主张薄层 / 搅动 | （源：[[Industrial Drying Ch1 Principles and Classification]]） |
| 生物基纤维素气凝胶吸水 | **153 g/g**（CMC-Na 吸水主体 + CNF 骨架 + 柠檬酸交联；冷冻干燥 48 h → 160 ℃ 热交联成网） | （源：[[CMC-Na CA CNF SAP original article.pdf]]） |
| 纳米纤维素 vs SAP 吸水口径 | BCNF **60–120 g/g** vs SAP **300–500 g/g**；价值在 **SAP 减量 30–50%**，而非吸水倍率 | （源：[[纳米纤维素纤维技术及应用深度研究报告]]） |
| 纳米纤维素三档尺寸 | CNC 3–20 nm 棒状（模量 100–150 GPa）/ CNF 10–100 nm 成网 / BNC 20–100 nm（纯度 99%） | （源：[[纳米纤维素纤维技术及应用深度研究报告]]） |
| 调温层验收门槛（模型 KPI 口径） | AUL/CRC ≥ current；rewet ≤ current；skin-model ΔT/dt ≤ target | （源：[[PCM-Free Thermoregulation with BNC Nanofiber Network]]） |

## Method / Mechanism 方法 / 机理

**1. 口径先行（define before design）：** absorbency/absorption 的语义歧义必须在术语层收口，否则**所有下游指标都会继承语义混乱**（源：[[Absorbent Technology Introduction]]）。

**2. 科学缺位是绑定约束：** "The development of the majority of those products was not based on a scientific or mechanistic approach, but on trial and error techniques and on the intuitive imagination of innovative tech…"；**真正瓶颈是科学缺位而非资金**，仿真/计算机辅助设计是低成本出路（源：[[Absorbent Technology Introduction]]）。

**3. 虚拟原型（virtual prototyping）路线：** 基于物理定律的建模在精度、成本与效率上优于实验 —— "Computational modeling, when applicable, is a powerful and cost-effective tool to study a problem with considerable accuracy in a short time"，且实验"would require building many such expensive machines"；并以**高速摄像、Fiberscope / Videoimagescope、静压探针**闭环验证（源：[[Computational Modeling in Absorbent Technology]]）。

**4. 微尺度热力学与宏尺度水力学对接：** 以**杆/管模型**取代教科书平面座滴法，给出**单根纤维的毛细拉力** F = γLV·cos θeq·C —— 即「**不要在平板上测吸收性**」，纤维级毛细拉力须用杆模型评估；这一处修正改变了「接触角测试」对芯体的含义（源：[[Surface Tension and Surface Energy]]）。

**5. 结构→性能：** performance = composition × structure，尺寸参数 + 测试标准汇编 + 建模三段式构成量化工具体系（源：[[Characterisation, testing and modelling of nonwoven fabrics]]）。

**6. 干燥耦合（drying coupling）：** 结合水（bound moisture）决定平衡含水率，从而决定纤维素绒毛浆与 SAP 可达干度的**下限**；热风对流是纸浆/纸巾/无纺布穿透干燥的默认方式（源：[[Industrial Drying Ch1 Principles and Classification]]）。

**7. SAP 选型必须按载荷条件：** 因为 SAP 的独特性在于**受压下的保持能力**，供应商选型不能只看自由溶胀倍率（源：[[Absorbent Technology Introduction]]）。

## Hygiene Relevance 卫材关联

- **面层亲水类型直接决定回渗与多次吸收**：单亲型（single-hydrophilic）**第 1 次快、衰减快**（第 5 次 7.39–8.62 s、回渗 3.89–6.17 g），源文评为 **质量档次不高**；多亲型（multi-hydrophilic）兼顾快吸与低回渗（回渗 0.84–1.32 g），是**高档纸尿裤主流原料与发展方向**（源：[[ES Fibre Hydrophilic Function and Applications]]）。
- **常见框架被证伪**：源文量化了回渗/速度 trade-off，并**反驳**「首次穿透越快 ⇒ 越好」的通常假设（源：[[ES Fibre Hydrophilic Function and Applications]]）。
- **ADL 与芯体的分工来自几何**：面内芯吸 vs 贯穿吸收（demand absorbency）决定 ADL 与芯体摄入设计的分工（源：[[Characterisation, testing and modelling of nonwoven fabrics]]）。
- **压力可替代亲水化**：一旦 θ ≥ 90°，毛细拉力为零，只有外加压力可破局；反之亲水表面可在零压下换回穿透 —— 两者是工程的**可替代手段**（源：[[Computational Modeling in Absorbent Technology]]）。
- **亲水化是复配而非叠加**：接枝 −OH/−COOH 降低 θeq，Wenzel 再经粗糙度**相乘**放大收益 —— 表面化学与微粗糙度同时工程化严格更优（源：[[Surface Tension and Surface Energy]]）。
- **薄型化 / 生物基化的吸水账要算清**：纳米纤维素（BCNF 60–120 g/g）**不以吸水倍率为卖点**，价值在 SAP 减量 30–50%、柔软度、可降解与结构稳定；成本闸门为 $40–100+/kg → 需降 60–70%，**$5/kg 是进入主流卫材的临界量级**（源：[[纳米纤维素纤维技术及应用深度研究报告]]）。
- **调温层的模型验收口径**：以 AUL/CRC、rewet 与皮肤模型 ΔT/dt 作开发闸门，是「吸收模型指标 ↔ 热舒适指标」并联的实例（源：[[PCM-Free Thermoregulation with BNC Nanofiber Network]]）。
- （相邻口径）**粘接侧同样影响芯体固持**：温度与剥离速率直接决定 core retention；配方核心是设计 ψ(v,T) 峰，而非仅界面热力学（源：[[Handbook of Adhesive Technology Full Report]]）。

## Open Questions 待补

- `[待补]`：**「Hygiene Absorption Model」作为模型的自身定义、状态变量与支配方程组**在引用来源中均未给出；现有摘录只提供吸收性口径与建模方法论。
- `[原文残缺]`：`Computational Modeling in Absorbent Technology` 摘录中 "One-dimensional Washburn is a lowe…" 一句被截断，未予补写（源：[[Computational Modeling in Absorbent Technology]]）。
- `[原文残缺]`：`ES Fibre Hydrophilic Function and Applications` 中 25 g/m² 商用样回渗值（1.06 …）截断（源：[[ES Fibre Hydrophilic Function and Applications]]）。
- `[待补]`：本页摘录中 `Handbook of Adhesive Technology Full Report` 的命中属**粘接侧**内容（core retention 与 ψ(v,T)），非吸收模型正文，未作为本页主体证据。
- `[待补]`：三条原始引用来源（[[Handbook of Industrial Drying]]、[[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]]、[[Industrial Drying Ch50 Solid-Liquid Separation]]）**在本批摘录中无对应正文句**；其与吸收模型的关联待回原文核对后补充。
- `[待补]`：模型与既有仿真页（[[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]、[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]）的**口径关系**未在引用页中说明。

## Related Sources 关联来源

**原始引用来源（Cited by, 3 处）**
- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]]
- [[Industrial Drying Ch50 Solid-Liquid Separation]]

**提供正文摘录的库内页面**
- [[Absorbent Technology Introduction]]
- [[Computational Modeling in Absorbent Technology]]
- [[Characterisation, testing and modelling of nonwoven fabrics]]
- [[Surface Tension and Surface Energy]]
- [[ES Fibre Hydrophilic Function and Applications]]
- [[Industrial Drying Ch1 Principles and Classification]]
- [[PCM-Free Thermoregulation with BNC Nanofiber Network]]
- [[纳米纤维素纤维技术及应用深度研究报告]]
- [[CMC-Na CA CNF SAP original article.pdf]]
- [[Handbook of Adhesive Technology Full Report]]

**延伸关联**
- [[Absorbent Technology]]
- [[Porous Structure and Liquid Flow Models]]
- [[Fluid Absorption in High Bulk Nonwovens]]
- [[Dry-laid web formation]]
- [[SAP（高吸水树脂）]]
- [[吸收芯体]]
- [[ADL（导流层）]]
- [[绒毛浆（Fluff Pulp）]]
- [[复合材料 Composite]]
- [[回渗 Rewet]]
- [[Rewet Test（回渗测试）]]
- [[AUL 加压吸水率]]
- [[CRC 离心保持能力]]
- [[Dryness Measure System（干爽度量三分）]]
- [[FIFE Test（FIFE 摄入-回渗评价）]]
- [[Acquisition Test STM-00060（导流性能测试）]]
- [[SAP 溶胀 SAP Swelling]]
- [[Flory- Rehner Theory]]
- [[达西定律 Darcy's Law]]
- [[Washburn Equation]]
- [[Hagen-Poiseuille Equation]]
- [[Laplace Pressure]]
- [[毛细压力 Capillary Pressure]]
- [[接触角 Contact Angle]]
- [[Young's Equation]]
- [[Wenzel Equation]]
- [[Work of Adhesion]]
- [[三相接触线 TPL]]
- [[亲水化 Hydrophilisation]]
- [[表面活性剂 Surfactant]]
- [[润湿 Wetting]]
- [[湿热耦合 Heat-Moisture Coupling]]
- [[CFD 计算流体力学]]
- [[Navier-Stokes Equation]]
- [[有限差分法 Finite Difference]]
- [[有限元法]]
- [[有限体积法]]
- [[k-ε 湍流模型]]
- [[Stokes Number]]
- [[Lagrangian Particle Tracking]]
- [[虚拟原型 Virtual Prototyping]]
- [[气铺 Airlaid]]
- [[Fiberscope]]
- [[Videoimagescope]]
- [[纳米纤维素（CNC、CNF、BNC）]]
- [[三类纳米纤维素对比（CNC、CNF、BNC）]]
- [[Biodegradable SAP（可降解高吸水树脂）]]
- [[BNC 与绒毛浆和 SAP 定位对比]]

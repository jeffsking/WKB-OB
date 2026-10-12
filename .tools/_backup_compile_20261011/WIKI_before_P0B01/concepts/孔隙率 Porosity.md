---
type: concept
title: "孔隙率 Porosity"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [porosity, porous-media, absorbent-core, SAP, gel-blocking, BNC, electrospinning, void-volume]
---

# 孔隙率 Porosity

> 📌 **Page completed 2026-09-30** from 4 citing sources (10 vault pages carry verbatim excerpts). All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）。本库引用页未就「孔隙率」给出独立的定义句；仅在模型与换算语境下给出**可操作的表达式**与输出口径：

- 溶胀态孔隙率由 qw/qv 计算孔分率：$P_s = 1 - q_v [1 + \rho(q_w - 1)/d_1]^{-1}$（Eq 9.1）（源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]）。
- 冷冻凝胶法中由初始单体浓度 $c_0$ 与制备温度 Tprep 设定孔隙率：冰分率 $f_{ice} = 1 - c_0/c$（Eq 9.4）（源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]）。
- 工程口径下，孔隙率是压缩层属性计算的一个输出项（与 Thickness、Permeability、Volumetric Strain、Void Volume 并列，随载荷而变）（源：[[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]）；`[待补]`：引用页未给出该输出的公式来源。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Swollen-state porosity 溶胀态孔隙率 P_s | $P_s = 1 - q_v [1 + \rho(q_w-1)/d_1]^{-1}$（Eq 9.1） | （源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]） |
| Ice fraction / porosity 冰分率（= 设定孔隙率） | $f_{ice} = 1 - c_0/c$（Eq 9.4） | （源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]） |
| Hydrogel water uptake 水凝胶吸水倍率 | 10–1000 × 干体积（原文："10 to 1000 times their dry volume of water without dissolving."） | （源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]） |
| Macroporous hydrogel channel size 大孔水凝胶通道尺寸 | 纳米级—微米级（原文："nanometer- to micron-size liquid channels"） | （源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]） |
| Crosslinker threshold for convective transport 对流传输交联剂阈值 (PNIPA) | BAAm > 5% | （源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]） |
| Maximum macroporosity 最大大孔率制备条件 | 30% BAAm / 20% 单体 | （源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]） |
| Response-rate scaling 响应速率标度 | rate ∝ 1/(粒径)² | （源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]） |
| K-C compressed-layer calculator example 压缩层算例 @ 2.0 kPa | Porosity 0.9514；Thickness 0.137 cm；Volumetric Strain −0.707；Void Volume 0.130 cm³/cm² | （源：[[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]） |
| REL void-volume target REL 的 VV 目标 | 80–117 cm³/g @ 0.5 kPa（实现路径 = 降堆密度） | （源：[[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]） |
| Core porosity before/after SAP swelling 吸收前的芯体孔隙率 | 0.42 | （源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]；[[Gel Blocking（凝胶阻塞）]]） |
| Minimum porosity — fine grid 细网格最低孔隙率 | 0.284（粗网格 0.347） | （源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]；[[Gel Blocking（凝胶阻塞）]]） |
| Permeability drop from gel blocking 凝胶阻塞致渗透率下降 | 约 2–5 倍 | （源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]） |
| BNC nanofiber-mat porosity 细菌纳米纤维毡孔隙率 | ≈ 85–95% | （源：[[BNC PCM-Free Thermoregulation v1（无微胶囊温控·细菌纳米纤维素）]]；[[PCM-Free Thermoregulation with BNC Nanofiber Network]]） |
| BNC inter-fiber pore size BNC 纤维间孔径 | ≈ 20–200 nm（fibril ribbon 宽 ≈ 50–100 nm；tortuosity τ ≈ 1.5–3） | （源：[[BNC PCM-Free Thermoregulation v1（无微胶囊温控·细菌纳米纤维素）]]） |
| BNC porosity (rounded, thermal mapping) | ≈ 90% | （源：[[PCM-Free Thermoregulation]]） |
| Electrospinning porosity window 静电纺丝孔隙率窗口 | 30%–99%（可调） | （源：[[Electrospinning（静电纺丝）]]） |
| Electrospun aerogel core porosity 电纺气凝胶芯体孔隙率 | > 95% | （源：[[Electrospinning Technology Analysis - Diaper Application 2026-05-20（静电纺丝技术深度分析·纸尿裤应用）]]） |
| Nanofiber fibre diameter window 纳米纤维直径窗口 | 10 nm – 10 µm | （源：[[Electrospinning Technology Analysis - Diaper Application 2026-05-20（静电纺丝技术深度分析·纸尿裤应用）]]；[[Electrospinning（静电纺丝）]]） |
| ADL pore-size target window ADL 孔径目标窗口 | 10–50 µm → 0.1–5 µm | （源：[[Electrospinning Technology Analysis - Diaper Application 2026-05-20（静电纺丝技术深度分析·纸尿裤应用）]]） |

## Method / Mechanism 方法 / 机理

**1. 孔隙率—渗透率动态耦合（凝胶阻塞）：** 由**颗粒填充床微观流道理论**（Carman-Kozeny）推导，模型自动捕捉凝胶膨胀导致的孔隙堵塞 —— SAP 溶胀 → 降低孔隙率 → 降低渗透率 → 限制后续液体到达更深层，形成**自限性机制**（源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]；[[Gel Blocking（凝胶阻塞）]]）。细网格能更精确解析 SAP 颗粒附近的**局部孔隙结构**，因而解析出更低的局部孔隙率（0.284 vs 0.347）（源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]）。

**2. 大孔水凝胶的两条制备主线：** 反应诱导相分离（RIPS）与冷冻凝胶化（cryogelation）；制备过程中的相分离是形成大孔的主因（源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]）。冷冻凝胶反应区聚合物浓度 $c = \nu_2 \rho$，凝固关系见 Eq 9.2（$T_{prep}$、$T_f^0$、$\nu_2$、$\nu_e$、$\chi$ 诸项）（源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]）。交联剂浓度、惰性稀释剂（造孔剂）用量与种类、温度三者共同决定不均一性/孔隙率，并与溶胀和力学耦合（源：[[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]）。

**3. 压缩 → 孔隙的换算数据流（TTM-00038）：** 多循环压缩得到零载厚度与各压力点厚度（取稳态/末循环以消除塑性形变）→ 输入 Compressed Layer Properties Calculator（Pore Space Modulus、Zero-load thickness、Applied Load、Fiber Density、Fiber Radius）→ 逐压力点同时输出 Thickness、Permeability、Strain、Available Void Volume、Porosity 随载荷的函数（源：[[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]）。建模端用面积基准（cm³/cm²），工程端用质量基准（cm³/g），两者除以 gsm 即可互换（源：[[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]）。

**4. 低孔隙率介质的传热机制（BNC）：** ≈90% 孔隙率 → 捕获静止空气（k_air ≈ 0.026）→ 有效导热极低；纳米孔 ≈20–200 nm 接近空气平均自由程（≈68 nm）→ **Knudsen 效应抑制气相导热**；点接触纤维网络 → 最小固相导热路径 + 声子边界散射（源：[[BNC PCM-Free Thermoregulation v1（无微胶囊温控·细菌纳米纤维素）]]；[[PCM-Free Thermoregulation]]）。

## Hygiene Relevance 卫材关联

- **"高 SAP 含量反而易侧漏"** —— 溶胀降孔隙率 → 降渗透率 → 后续液体到不了深层；⚠️ 本页摘录标注此为**模型推论，无实验验证**（源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]；[[Gel Blocking（凝胶阻塞）]]）。
- **软化 = VV 损失**：surge 做得更软（pore space modulus 降低），同一应力下 void volume 直接下降（K-C 案例：应力 1.5 → 2.73 kPa，VV 从 ~0.22 掉到 ~0.12 cm³/cm²）；「首次尿后 void volume 崩了，什么纤维工程都救不了第二、三次」（源：[[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]）。
- **多循环是核心口径**：模拟 4 次尿次（体重 0.5–1 kPa 反复加载），看的是**末循环残余厚度**而非首循环（源：[[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]）。
- **Z 向孔隙率梯度**：致密贴肤侧 / 蓬松芯侧，用于减缓皮肤侧 dT/dt（承接既有 REL 工作）（源：[[BNC PCM-Free Thermoregulation v1（无微胶囊温控·细菌纳米纤维素）]]；[[PCM-Free Thermoregulation]]）。
- **纳米纤维落点优先级**：ADL > 面层 > 芯体 > 底膜；ADL 孔径从 10–50 µm 降到 0.1–5 µm 带来毛细梯度（源：[[Electrospinning Technology Analysis - Diaper Application 2026-05-20（静电纺丝技术深度分析·纸尿裤应用）]]）。
- **气凝胶芯体路线**：孔隙率 > 95% 时厚度可降至传统芯体的 1/3，但源文自陈**单次吸液总量可能不及 SAP 体系**（源：[[Electrospinning Technology Analysis - Diaper Application 2026-05-20（静电纺丝技术深度分析·纸尿裤应用）]]）。

## Open Questions 待补

- **收敛性尚未确认**：孔隙率下限从 0.347 降到 0.284，源文建议再试 60×24 网格 —— 说明尚未收敛；「细网格结果更可信」是源文判断，**无实验佐证**（源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]）。
- **v9 不含反渗**（不含二次加载后的反渗），故本页结论**不能外推到回渗**（源：[[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]）。
- **渗透率下降倍数与实测对应关系未明确**：「渗透率下降约 2–5 倍」与细网格 20.3%（≈5×）、粗网格 44.6%（≈2.2×）的对应关系源文未明确（源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]）。
- **自由液体最终 0.0 mL（细网格）** 是否意味着全部被 SAP 吸收？源文未说明 SAP 是否已饱和（源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]）。
- `[待补]`：本体定义与常规测定口径（如压汞/BET/液体置换）在引用来源中均未给出。
- `[待补]`：TTM-00038 中 Porosity 输出的计算公式未在引用页给出（源：[[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]）。

## Related Sources 关联来源

**原始引用来源（Cited by, 4 处）**
- [[Characterisation, testing and modelling of nonwoven fabrics]]
- [[Fibers and Fibrous Materials]]
- [[Porous Structure and Liquid Flow Models]]
- [[Porous Structure and Liquid Flow Models]]

**提供正文摘录的库内页面**
- [[Smart Polymers Ch09 Macroporous Hydrogels from Smart Polymers]]
- [[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]
- [[Gel Blocking（凝胶阻塞）]]
- [[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]
- [[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]
- [[BNC PCM-Free Thermoregulation v1（无微胶囊温控·细菌纳米纤维素）]]
- [[PCM-Free Thermoregulation with BNC Nanofiber Network]]
- [[PCM-Free Thermoregulation]]
- [[BNC-Only vs BNC+PCM (Thermoregulation Ledger)]]
- [[Electrospinning Technology Analysis - Diaper Application 2026-05-20（静电纺丝技术深度分析·纸尿裤应用）]]
- [[Electrospinning（静电纺丝）]]

**延伸关联**
- [[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- [[Void Volume 与压缩模量两条孔隙表征路线对比]]
- [[湿态压缩模量]]
- [[Pore Size Distribution Monodispersity（孔径分布单分散性）]]
- [[渗透率 Permeability]]
- [[达西定律 Darcy's Law]]
- [[吸收芯体]]
- [[SAP（高吸水树脂）]]
- [[ADL（导流层）]]
- [[REL增强层]]
- [[毛细梯度设计]]
- [[分区密度设计]]
- [[细菌纳米纤维素]]
- [[Rewet Test（回渗测试）]]

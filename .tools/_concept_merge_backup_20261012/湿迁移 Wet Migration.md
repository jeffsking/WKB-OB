---
type: concept
title: "湿迁移 Wet Migration"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [wet-migration, diffusion, fick-law, absorbent-core, SAP-swelling, drying, binder-migration]
---

# 湿迁移 Wet Migration

> 📌 **Page completed 2026-09-30** from 4 citing sources (库内正文命中 32 页；本页取用 8 页摘录). All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）。引用页未给出「湿迁移」的独立定义句；相关表述均以**扩散数学**为母体：Fick 定律（一维/标量形式）被建立为数学公理，并由其导出 Fick 第二定律（扩散 PDE），再延伸到各向异性介质与多组分情形；**SAP 溶胀动力学、芯体吸液速率、湿迁移模型的本原公式均源于此章**（源：[[Diffusion Equations (Crank Ch.1)]]）。

⚠️ 口径提示：「migration 迁移」在本库至少存在**三种不同指代**，不可混引：
- **湿迁移（水分/液体在介质内的输运）** —— 本页主题，理论根基为 Fick 定律（源：[[Diffusion Equations (Crank Ch.1)]]）。
- **助剂/粘合剂迁移（物料在干燥或老化中向表面富集）** —— 见 [[Chemical bonding]]、[[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]。
- **化学物迁移量（可萃取/可迁移物向模拟体液的溶出）** —— 见 [[GB-T 34405-2017 Determination of Acrylamide Migration in Household Papers（家用纸制品中丙烯酰胺迁移量的测定 LC-MS-MS法）]]。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Governing law 支配定律 | Fick 定律（一维/标量形式）+ Fick 第二定律（扩散 PDE）；延伸至各向异性介质与多组分 | （源：[[Diffusion Equations (Crank Ch.1)]]） |
| D(C) dynamic range after swelling 溶胀后变系数扩散跨度 | D(C) 跨 3–4 个数量级（低吸水比时 D ≈ 常数 → 线性；溶胀后非线性） | （源：[[Diffusion Equations (Crank Ch.1)]]） |
| Dimensionless groups 无量纲化 | T = Dt/l²，X = x/l，c = C/C₀ —— 不同粒径/D/厚度可从同一组无量纲解缩放 | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| Explicit finite-difference scheme 显式差分格式 | cᵢ^(j+1) = r·cᵢ₋₁^j + (1−2r)·cᵢ^j + r·cᵢ₊₁^j | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| Stability condition 稳定性条件 | r ≤ ½ | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| SAP 高 D 区间后果 | 溶胀后期时间步必须极小，计算量剧增 | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| Mathematics of Diffusion 覆盖面 | 15 章：Fick 定律、解析/数值解法、D(C) 变系数扩散、非菲克扩散、复合介质、动边界、反应-扩散耦合、湿热耦合 | （源：[[Mathematics of Diffusion]]） |
| 迁移量口径测试温度与时长（丙烯酰胺，GB/T 34405-2017） | 37 ± 2 ℃；10 min（纸巾/湿巾）或 4 h（纸尿裤与卫生巾**仅护肤接触覆盖层**） | （源：[[GB-T 34405-2017 Determination of Acrylamide Migration in Household Papers（家用纸制品中丙烯酰胺迁移量的测定 LC-MS-MS法）]]） |
| 迁移量口径校准与检出（同上） | 校准 0.05–5.0 µg / 50 mL；LOD 0.005 mg/kg（LOQ 段落截断） | （源：[[GB-T 34405-2017 Determination of Acrylamide Migration in Household Papers（家用纸制品中丙烯酰胺迁移量的测定 LC-MS-MS法）]]） |

## Method / Mechanism 方法 / 机理

**1. 扩散数学的建立路径（Crank Ch.1）：** 以 Fick 定律为唯一核心假设 → 推导 Fick 第二定律 → 各向异性介质与多组分延伸。**Fick 定律是扩散数学的唯一核心假设**——SAP 溶胀、芯体吸液、湿迁移、湿巾均匀性模型均基于此（源：[[Diffusion Equations (Crank Ch.1)]]）。

**2. 非线性化的数学根源：** **D(C) 剧烈变化是 SAP 吸液速率非线性化的数学根源**——低吸水比时 D ≈ 常数（线性），溶胀后 D(C) 跨 3–4 个数量级（非线性）（源：[[Diffusion Equations (Crank Ch.1)]]）。

**3. 各向异性处理：** **复合芯体是典型各向异性介质**——MD/CD 性能差异需在模型中用**扩散张量**取代标量 D（源：[[Diffusion Equations (Crank Ch.1)]]）。

**4. 数值求解（Crank Ch.8）：** 无量纲化 T=Dt/l² 使不同参数问题可缩放复用；显式差分稳定性条件 r ≤ ½ 决定时间步长；**绝大多数工程实际问题靠本章方法求解**（SAP 建模、芯体湿迁移 FEM）（源：[[Numerical Methods for Diffusion (Crank Ch.8)]]）。

**5. 假设边界：** **无对流假设**的局限——湿巾擦拭等强制对流场景需**附加对流项**（源：[[Diffusion Equations (Crank Ch.1)]]）。

**6. 干燥过程中的迁移（另一口径）：** 干燥中粘合剂迁移形成**表富里贫（binder-rich skin / starved core）**，导致**分层风险**（源：[[Chemical bonding]]）。同一章对聚合物型增塑剂的表述为 "less susceptible to migration, and less extractible"，未给出迁移速率模型或萃取限量数值（源：[[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]）。

## Hygiene Relevance 卫材关联

- **芯体吸液的液体输运**：绒毛浆在传统芯体里提供 **capillary wicking and temporary void volume**，在 SAM 溶胀并固定液体**之前**支撑快速初始摄入 —— 绒毛浆是「SAM 膨胀前那几秒」的通道与空间提供者，是**时间装置**而非单纯填充物（源：[[Blizzard Core（Blizzard 芯体结构）]]）。
- **复合芯体的建模要求**：MD/CD 性能差异必须用扩散张量，标量 D 不足（源：[[Diffusion Equations (Crank Ch.1)]]）。
- **数值建模的时间步代价**：溶胀后期高 D 区间时间步必须极小，直接决定 SAP 建模与芯体湿迁移 FEM 的计算量（源：[[Numerical Methods for Diffusion (Crank Ch.8)]]）。
- **薄型化的另一类「迁移」**：**Thinning creates SAP migration（变薄带来 SAP 移位）** —— 这是 **SAP 颗粒的物理移位**，与水分输运口径不同；配套手段是固结（热风穿刺熔融）与分层导流，不能只减厚度（源：[[可降解生物基材料与薄且强芯体技术深度解析]]）。
- **化学迁移量是卫材合规项**：GB/T 34405-2017 采用**模拟汗液 37 ℃ 萃取**（GB/T 3922-2013 配方）+ 同位素稀释 LC-MS/MS，是与 GB/T 37859 **含量口径**对应的**迁移量口径**方法（两者互为 counterpart，非替代）（源：[[GB-T 34405-2017 Determination of Acrylamide Migration in Household Papers（家用纸制品中丙烯酰胺迁移量的测定 LC-MS-MS法）]]）。

## Open Questions 待补

- `[待补]`：湿迁移的**定义句与量纲口径**（含水量 / 饱和度 / 迁移通量）在引用来源中均未给出。
- `[待补]`：本库尚无把「湿迁移」与回渗（rewet）定量关联的摘录；湿迁移 ≠ 回渗，引用时不可混用（源：[[Diffusion Equations (Crank Ch.1)]]）。
- `[待补]`：微胶囊语境下的迁移表述在摘录中**被截断**（"Migration is the hard …"），原文残缺，不予补写（源：[[Microencapsulation]]）。
- `[待补]`：助剂迁移「未被量化」——原章只定性给出 less susceptible to migration / less extractible，**未给出迁移速率模型或萃取限量数值**（源：[[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]）。
- `[待补]`：GB/T 34405-2017 的 LOQ 数值在摘录中被截断（LOD 0.005 mg/kg 可读，LOQ 不可读）（源：[[GB-T 34405-2017 Determination of Acrylamide Migration in Household Papers（家用纸制品中丙烯酰胺迁移量的测定 LC-MS-MS法）]]）。

## Related Sources 关联来源

**原始引用来源（Cited by, 4 处）**
- [[Diffusion Equations (Crank Ch.1)]]
- [[Handbook of Industrial Drying]]
- [[Infinite and Semi-Infinite Media (Crank Ch.3)]]
- [[Mathematics of Diffusion]]

**提供正文摘录的库内页面**
- [[Numerical Methods for Diffusion (Crank Ch.8)]]
- [[Chemical bonding]]
- [[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]
- [[GB-T 34405-2017 Determination of Acrylamide Migration in Household Papers（家用纸制品中丙烯酰胺迁移量的测定 LC-MS-MS法）]]
- [[Blizzard Core（Blizzard 芯体结构）]]
- [[可降解生物基材料与薄且强芯体技术深度解析]]
- [[Microencapsulation]]

**延伸关联**
- [[Fick 定律]]
- [[Non-Fickian Diffusion (Crank Ch.11)]]
- [[Diffusion in Heterogeneous Media (Crank Ch.12)]]
- [[Moving Boundaries (Crank Ch.13)]]
- [[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]
- [[湿热耦合 Heat-Moisture Coupling]]
- [[反应-扩散耦合 Reaction-Diffusion]]
- [[Case II 扩散]]
- [[SAP 溶胀 SAP Swelling]]
- [[SAP（高吸水树脂）]]
- [[吸收芯体]]
- [[孔隙率 Porosity]]
- [[达西定律 Darcy's Law]]
- [[Darcy Flow in Fibrous Porous Media（纤维多孔介质达西流动）]]
- [[MD Liquid Distribution]]
- [[回渗 Rewet]]
- [[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]
- [[Fluff-Free 4th-Gen Absorbent Core（无木浆第四代芯体）]]
- [[Migratable Fluorescent Whitening Agents（可迁移性荧光增白剂）]]

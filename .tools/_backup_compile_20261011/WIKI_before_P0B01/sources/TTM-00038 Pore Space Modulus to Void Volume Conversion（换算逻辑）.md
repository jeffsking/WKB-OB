---
type: source
title: "TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）"
source_type: 技术说明（内部换算逻辑拆解）
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/TTM-00038_Pore_Space_Modulus_to_Void_Volume_换算逻辑.docx.md
original_link: ""
date_published: 2021
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "本文件解开了本批 [[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] 留下的缺口：**TTM-00038 本身不输出 void volume，它输出的是「厚度-压力」曲线，VV 是从该曲线换算出来的**"
  - "换算走「Compressed Layer Properties Calculator」：输入五件套 = Pore Space Modulus、Zero-load thickness（cm）、Applied Load（kPa）、Fiber Density（g/cm³）、Fiber Radius（μm）"
  - "K-C 官方算例（2.0 kPa）：Applied Load 2.0 kPa → Porosity 0.9514、Thickness 0.137 cm、Volumetric Strain −0.707、**Void Volume 0.130 cm³/cm²**"
  - "两种基准：面积基准（建模端）VV = h(P) × Φ(P)，单位 cm³/cm²；质量基准（REL/工程端）VV_g = VV / (gsm/1000)，单位 cm³/g，**REL 目标 80–117 cm³/g @ 0.5 kPa**"
  - "理论纽带：比空隙体积 Vₛ = AT/W − Σ(w_i/ρ_i) = Φ/[ρ_av(1−Φ)]（Absorbent Technology, Eq. 39/47）"
  - "孔隙率并行算法：Φ(P) = 1 − ρ_bulk(P)/ρ_fiber，其中 ρ_bulk(P) = gsm / h(P)；压缩越狠 → h 下降 → ρ_bulk 上升 → Φ 与 VV 同步下降"
  - "REL 工程经验映射：PTT 含量 28%→32% 使 VV +8~12 cm³/g；双层结构 +10~15；Hollow ratio 28%→32% +5~8；PVA 细旦化 1.5D→1.2D +3~5；Variant C 现状 ε ≈ 92–94%（VV ~95–105 cm³/g），要到 117 cm³/g 需 ε ≈ 96–97%"
pages_linked: ["[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]", "[[REL增强层]]", "[[ADL（导流层）]]", "[[芯体测试方法与验收基准（STM）]]", "[[PTT（聚对苯二甲酸丙二醇酯）]]", "[[PVA纤维（湿强骨架）]]"]
---

# TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）

## 一句话定位

一份**内部换算逻辑拆解**，把 [[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] 输出的「厚度-压力」曲线，翻译成建模与工程两端各自需要的**孔隙体积（Void Volume, VV）**；并给出 REL 层的 VV 目标区间与四条提升路径。

## 摘要

文件自述来源为 K-C *Absorbent System Test Methods / Modeling*（2021）与 *Absorbent Technology*（2002），适用于吸收芯体、ADL/Surge、REL 等蓬松材料的 VV 表征。

**测试本身测什么**：TTM-00038 / TTM-00437（Pore Space Modulus，孔隙模量）测量吸收芯体与导入系统材料在多次压缩循环后的**回弹性（resiliency）**；直接输出是**厚度随压力的函数曲线 Thickness as f(Pressure)**，VV 由后处理换算得到。典型加载为**多循环压缩（如 3-Cycle）**，HPP 参考样品如 85 gsm，加载至 **10 kPa**。用途是吸收系统建模输入，以及评估材料变更对 VV 的影响。

**换算数据流**：
1. **原始数据**：多循环压缩得到零载厚度（cm）与各压力点厚度 h(P)（多循环取**稳态/末循环**，以消除塑性形变）。
2. **输入计算器**（Compressed Layer Properties Calculator）五件套：Pore Space Modulus（由曲线拟合，与 basis weight、fiber density 一同输入）、Zero-load thickness（cm）、Applied Load（kPa）、Fiber Density（g/cm³）、Fiber Radius（μm）。
3. **逐压力点输出**：K-C 官方算例在 2.0 kPa 下给出 Porosity 0.9514、Thickness 0.137 cm、Volumetric Strain −0.707、**Void Volume 0.130 cm³/cm²**。即同一台压缩数据换算后同时输出 Thickness、Permeability、Strain、Available Void Volume、Porosity 随载荷的函数。
4. **两种基准**：面积基准（K-C 建模端）**VV = h(P) × Φ(P)**，单位 cm³/cm²——受压厚度 × 该压力下孔隙率；质量基准（REL / 工程端）**VV_g = VV / (gsm/1000)**，单位 cm³/g，**REL 目标 80–117 cm³/g @ 0.5 kPa**。
5. **理论纽带**：比空隙体积 **Vₛ = AT/W − Σ(w_i/ρ_i) = Φ/[ρ_av(1−Φ)]**（*Absorbent Technology* Eq. 39/47）——孔隙率除以质量基准即得比空隙体积。
6. **Porosity 并行计算**：**Φ(P) = 1 − ρ_bulk(P)/ρ_fiber**，其中 **ρ_bulk(P) = gsm / h(P)**。压缩越狠 → h 下降 → ρ_bulk 上升 → Φ 与 VV 同步下降。

**三条解读要点**：① **软化 = VV 损失**——surge 做得更软（pore space modulus 降低），同一应力下 VV 直接下降（K-C 案例：应力 1.5 → 2.73 kPa，VV 从 ~0.22 掉到 ~0.12 cm³/cm²）。② **多循环是核心**——模拟 4 次尿次（体重 0.5–1 kPa 反复加载），看的是**末循环残余厚度**而非首循环；原文警句：「首次尿后 void volume 崩了，什么纤维工程都救不了第二、三次」。③ **配套测试**——Gel Bed Permeability（SAP 侧）、Composite Porosity（复合芯体）、开发中的 Functional Void Volume，共同构成 VV 测试矩阵。

**REL 工程映射**：PTT 含量 28%→32%（弹性恢复↑ → 压缩后厚度↑）+8~12 cm³/g；双层结构（功能解耦、整体蓬松度↑）+10~15；Hollow ratio 28%→32%（中空 lumen 直接贡献体积）+5~8；PVA 细旦化 1.5D→1.2D（纤维根数↑、支撑更均匀）+3~5。Variant C 现状 ε ≈ 92–94%（VV ~95–105 cm³/g）；要到 117 cm³/g 需 ε ≈ 96–97%，路径是**降堆密度（同 gsm 做更大厚度）**。

## 提炼的数字与结论

### K-C 官方算例（2.0 kPa）

| 属性 Property | 算例值 Value | 单位 Unit |
|---|---|---|
| Applied Load 施加载荷 | 2.0 | kPa |
| Porosity 孔隙率 | 0.9514 | — |
| Thickness 厚度 | 0.137 | cm |
| Volumetric Strain 体积应变 | −0.707 | — |
| **Void Volume 孔隙体积** | **0.130** | **cm³/cm²** |

### 换算公式族（Formulas）

| 量 Quantity | 公式 Formula | 适用端 User |
|---|---|---|
| 面积基准 VV | VV = h(P) × Φ(P)，cm³/cm² | K-C 建模端 |
| 质量基准 VV | VV_g = VV / (gsm/1000)，cm³/g | REL / 工程端 |
| 孔隙率 | Φ(P) = 1 − ρ_bulk(P)/ρ_fiber | 通用 |
| 体积密度 | ρ_bulk(P) = gsm / h(P) | 通用 |
| 比空隙体积 | Vₛ = AT/W − Σ(w_i/ρ_i) = Φ/[ρ_av(1−Φ)] | 理论（Absorbent Technology Eq. 39/47） |
| REL 目标 | **80–117 cm³/g @ 0.5 kPa** | REL 工程 |

### REL 参数 → VV 经验映射

| 参数调节 Adjustment | 机理 Mechanism | VV 影响 ΔVV |
|---|---|---|
| PTT 含量 28% → 32% | 弹性恢复↑ → 压缩后厚度↑ | **+8 ~ 12 cm³/g** |
| 双层结构 | 功能解耦，整体蓬松度↑ | **+10 ~ 15 cm³/g** |
| Hollow ratio 28% → 32% | 中空 lumen 直接贡献体积 | **+5 ~ 8 cm³/g** |
| PVA 细旦化 1.5D → 1.2D | 纤维根数↑，支撑更均匀 | **+3 ~ 5 cm³/g** |

> Variant C 现状：**ε ≈ 92–94%（VV ~95–105 cm³/g）**；目标 117 cm³/g 需 **ε ≈ 96–97%**，实现路径为**降堆密度（同 gsm 做更大厚度）**。

### 测试矩阵（VV Test Matrix）

| 方法 Method | 对象 Object | 状态 Status |
|---|---|---|
| Gel Bed Permeability（凝胶床渗透性） | SAP 侧 | 在册 |
| Composite Porosity（复合孔隙率） | 复合芯体 | 在册 |
| Pore Space Modulus（孔隙空间模量） | 芯体 / 导入系统 | 在册（TTM-00038 / TTM-00437） |
| Functional Void Volume（功能孔隙体积） | — | **开发中（WIP）** |

> ⚠️ **单源数值标注（2026-09-29）**：本文件为内部换算说明（credibility 中），其 REL VV 目标区间（80–117 cm³/g）、四条提升路径的 ΔVV 幅度、以及 Variant C 的 ε/VV 现状，**在本批其他资料中均无第二来源**；2.0 kPa 算例虽标为「K-C 官方算例」，但未附原始文件名。上述数值对外引用须回溯 _12 / _13 / NEW REL 4 三份原始文档 `[待验证]`。

> ✅ **与既有页的一致点**：本文件「VV 由厚度-压力曲线换算、需输入固相/纤维密度」的说法，与 [[STM-00429 Void Volume as a Function of Saturation（方法正文）]]「VV = 总体积 − 液体体积 − 固体体积」在物理上完全自洽——**两条路线共享同一个固相密度接口**。

## 关键论断（key_claims）

- **TTM-00038 输出的是力学曲线，VV 是后处理产物** —— 支撑页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- **建模端用面积基准（cm³/cm²），工程端用质量基准（cm³/g），两者除以 gsm 即可互换** —— 支撑页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- **多循环看末循环残余厚度，首循环不代表使用寿命** —— 支撑页：[[ADL（导流层）]]
- **软化 = VV 损失，是 surge/ADL 设计的核心权衡** —— 支撑页：[[ADL（导流层）]]
- **REL 的 VV 目标是 80–117 cm³/g @ 0.5 kPa，实现路径是降堆密度** —— 支撑页：[[REL增强层]]、[[PTT（聚对苯二甲酸丙二醇酯）]]、[[PVA纤维（湿强骨架）]]
- **VV 测试矩阵含 Gel Bed Permeability / Composite Porosity / PSM / Functional VV（WIP）** —— 支撑页：[[SAP性能指标（CRC AUL GBP Vortex）]]

## 关联页面

- 概念：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]、[[REL增强层]]、[[ADL（导流层）]]、[[芯体测试方法与验收基准（STM）]]、[[PTT（聚对苯二甲酸丙二醇酯）]]、[[PVA纤维（湿强骨架）]]、[[并列复合自卷曲纤维]]、[[SAP性能指标（CRC AUL GBP Vortex）]]、[[COCO芯体平台]]
- 实体：[[Kimberly-Clark（金佰利）]]
- 对比：[[Void Volume 与压缩模量两条孔隙表征路线对比]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/TTM-00038_Pore_Space_Modulus_to_Void_Volume_换算逻辑.docx.md`
- 原文链接：（无；内部换算逻辑拆解）
- 引用来源（文件自述）：_12 Absorbent System Test Methods (Urine Only), K-C 2021；_13 Absorbent System Modeling, K-C 2021；Urine Leakage Design Principles, K-C 2021；NEW REL 4；Absorbent Technology, Textile Science and Technology, 2002（Eq. 39/47）

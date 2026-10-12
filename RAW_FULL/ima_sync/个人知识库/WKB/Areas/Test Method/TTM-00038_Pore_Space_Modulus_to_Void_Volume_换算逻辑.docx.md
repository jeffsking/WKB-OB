---
media_id: "word_3867e2b60070d7dc3f413086d0b0036e_53b6f6b0c6fc0e7fde42e3396bc8e9f6001a693ee6c0644e"
source_file: "TTM-00038_Pore_Space_Modulus_to_Void_Volume_换算逻辑.docx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Areas/Test Method/TTM-00038_Pore_Space_Modulus_to_Void_Volume_换算逻辑.docx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# TTM-00038_Pore_Space_Modulus_to_Void_Volume_换算逻辑.docx.md

8
# TTM-00038：Pore Space Modulus → Void Volume 换算逻辑拆解

来源：K-C Absorbent System Test Methods / Modeling（2021）+ Absorbent Technology (2002) 适用：吸收芯体、ADL/Surge、REL 等蓬松材料的 void volume 表征

# 一、测试本身测什么

TTM-00038 / TTM-00437（Pore Space Modulus，孔隙模量）：

# •测试描述：测量吸收芯体和导入系统材料在多次压缩循环后的回弹性（resiliency）

# •直接输出：试样厚度随压力的函数曲线（Thickness as f(Pressure)）

# •输出可后处理换算出 void volume

# •典型加载：多循环压缩（如 3-Cycle），HPP 参考样品如 85 gsm，加载至 10 kPa

# •关键用途：吸收系统建模输入；评估材料变更对 void volume 的影响

要点：TTM-00038 本身不直接输出 void volume，它输出的是“厚度-压力”力学数据，void volume 是从这条曲线换算出来的。

# 二、换算逻辑（数据流）

# Step 1：原始数据

多循环压缩得到： - 零载厚度（zero-load thickness，cm） - 各压力点下的厚度 h(P)（多循环取稳态/末循环，消除塑性形变）

# Step 2：输入计算器（Compressed Layer Properties Calculator）

标准输入五件套： 1. Pore Space Modulus（材料压缩刚度，由曲线拟合得到，与 basis weight、fiber density 一起输入） 2. Zero-load thickness（cm） 3. Applied Load（kPa） 4. Fiber Density（g/cm³） 5. Fiber Radius（μm）

# Step 3：逐压力点输出（K-C 官方算例，2.0 kPa 示例）

|属性|算例值|单位|
|---|---|---|
|Applied Load|2.0|kPa|
|Porosity|0.9514|—|
|Thickness|0.137|cm|
|Volumetric Strain|−0.707|—|
|Void Volume|0.130|cm³/cm²|

即同一台压缩数据，换算后同时输出：Thickness、Permeability、Strain、Available Void Volume、Porosity 随载荷的函数。

# Step 4：两种基准换算

# •面积基准（K-C 建模端）：VV = h(P) × Φ(P)，单位 cm³/cm²——即受压厚度 × 该压力下孔隙率

•质量基准（REL/工程端）：VV_g = VV / (gsm/1000)，即每克材料的空隙体积，单位 cm³/g；REL 目标 80–117 cm³/g @ 0.5 kPa

•理论纽带：比空隙体积 Vₛ = AT/W − Σ(w_i/ρ_i) = Φ/[ρ_av(1−Φ)]（Absorbent Technology, Eq. 39/47）——porosity 除以质量基准即得比空隙体积

# Step 5：Porosity 的并行计算

Φ(P) = 1 − ρ_bulk(P)/ρ_fiber，其中 ρ_bulk(P) = (gsm/h(P))。压缩越狠 → h 下降 → ρ_bulk 上升 → Φ 与 VV 同步下降。

# 三、解读要点

1.软化 = void volume 损失：surge 材料做得更软（pore space modulus 降低），同一应力下 void volume 直接下降（K-C 案例：应力从 1.5→2.73 kPa，VV 从 ~0.22 掉到 ~0.12 cm³/cm²）

2.多循环是核心：模拟 4 次尿次（body weight 0.5–1 kPa 反复加载），看的是末循环残余厚度，不是首循环——“首次尿后 void volume 崩了，什么纤维工程都救不了第二、三次”

3.配套测试：Gel Bed Permeability（SAP 侧）、Composite Porosity（复合芯体）、开发中的 Functional Void Volume，共同构成 void volume 测试矩阵

# 四、REL 工程映射（延伸应用）

REL 参数 → VV 的经验映射：

|参数调节|机理|VV 影响|
|---|---|---|
|PTT 含量 28%→32%|弹性恢复↑ → 压缩后厚度↑|+8~12 cm³/g|
|双层结构|功能解耦，整体蓬松度↑|+10~15 cm³/g|
|Hollow ratio 28%→32%|中空 lumen 直接贡献体积|+5~8 cm³/g|
|PVA 细旦化 1.5D→1.2D|纤维根数↑，支撑更均匀|+3~5 cm³/g|

Variant C 现状：ε ≈ 92–94%（VV ~95–105 cm³/g）；要到 117 cm³/g 需 ε ≈ 96–97%，路径是降堆密度（同 gsm 做更大厚度）。

# 五、来源

•_12 Absorbent System Test Methods (Urine Only), K-C, 2021 —— TTM-00038 测试描述、输出与参考数据图（Normalized HPP Thickness as f(Pressure)）

•_13 Absorbent System Modeling, K-C, 2021 —— Compressed Layer Properties Calculator 输入/输出结构与 2.0 kPa 算例

•Urine Leakage Design Principles, K-C, 2021 —— void volume 测试方法矩阵（Gel Bed Permeability / Composite Porosity / Pore Space Modulus / Functional Void Volume WIP）与主影响变量

# •NEW REL 4 —— void volume 定义（cm³/g @ 0.5–1 kPa）、目标 80–117 cm³/g、4 次尿次生命周期

•Absorbent Technology, Textile Science and Technology, 2002 —— 比空隙体积 Vₛ 与孔隙率换算公式（Eq. 39, 47）、多组分密度法


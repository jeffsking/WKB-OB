---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_59fe727848c17cb64b6b6246025736bf001a693ee6c0644e"
source_file: "Handbook of Polymer Testing_full_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Polymer Testing/Handbook of Polymer Testing_full_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Handbook of Polymer Testing_full_report.md.md

# Handbook of Polymer Testing – Short-Term Mechanical Tests

## 全局综合报告（Full Consolidated Report）

书: Handbook of Polymer Testing – Short-Term Mechanical Tests
作者: Edward N. Brown
出版社: Rapra (2002)
页数 / 章数: 210 页 / 12 章
合成日期: 2026-06-27
输出文件: Ebook_Extract/Handbook_of_Polymer_Testing/Handbook of Polymer Testing_full_report.md

# 1. Executive Summary（执行摘要）

## 1.1 全书定位与核心贡献

本书是一部聚焦聚合物短期机械测试（Short-Term Mechanical Tests）的系统性手册，覆盖了从"为什么要测"到"怎么测才可比"，再到 8 大基础力学性能测试方法（质量/密度/尺寸 → 硬度 → 拉伸 → 压缩 → 剪切 → 弯曲 → 冲击 → 撕裂 → 断裂韧性）的完整链条。作者 Brown 反复强调一个跨章节的元命题：聚合物测试数值从来不是绝对事实，其可比性依赖取样方式、制样工艺、预处理、测试条件和统计方法的全链条一致性。

对卫生材料（卫生巾 / 纸尿裤 / 成人失禁用品）供应链而言，本书的价值在于：它给 SaaS 行业的 QA / SQE / 材料工程师提供了一套"如何向供应商索要可比数据 + 如何判定供应商报告有效"的方法论框架，其核心覆盖 SAP 拉伸、无纺布拉伸/撕裂、芯体纸浆压缩、胶黏剂剪切与剥离等所有关键测试环节。

## 1.2 12 章内容概览表

|||||
|---|---|---|---|
|Ch1|Introduction（导论）|提出"测试目的决定测试方法"、属性三分法（Fundamental / Apparent / Functional）、加速测试陷阱、溯源与认可体系|★★★★★ — 直接用于与供应商谈判测试方案|
|Ch2|Test Piece Preparation（试样制备）|模塑 vs. 切割、ISO 3167 多用途试样、冲压与裁切误差来源|★★★★ — 决定实验室制样 SOP|
|Ch3|Conditioning（调湿/预处理）|ISO 291 标准大气（23/50 与 27/65）、±2% RH 不可达、水分/时间/平衡判定、机械预处理|★★★★★ — 卫材环境极其敏感，尤其无纺布和 SAP 吸液后状态|
|Ch4|Mass, Density and Dimensions（质量/密度/尺寸）|密度（真密度/视密度/梯度柱法）、几何尺寸精度、面积测量误差放大效应|★★★★ — SAP 珠粒堆积密度、无纺布定量（gsm）、厚度是关键验收参数|
|Ch5|Hardness（硬度）|Shore A/D、Durometer、Ball Indentation（ISO 2039）、Rockwell、维氏微硬度、硬度不是本征属性|★★ — 卫材核心材料很少涉及硬度测试（仅弹性胶圈等辅助件）|
|Ch6|Tensile Stress-Strain（拉伸）|工程应力 vs. 真应力、割线模量、四种典型应力-应变形态、应变率效应|★★★★★ — 无纺布 MD/CD 拉伸、芯体湿态强度、SAP 拉伸是核心验收|
|Ch7|Compression Stress-Strain（压缩）|形状因子（shape factor）、屈曲判据（εc* ≤ 0.4(x/l)²）、长细比、润滑端部效应、ISO 604|★★★★★ — 芯体纸浆垫压缩/蓬松度、SAP 堆积压缩直接相关|
|Ch8|Shear Properties（剪切）|简单剪切 vs. 纯剪切、Punch Shear、Iosipescu、Clash & Berg 低温测试、ISO 458|★★★★ — 胶黏剂接头（lap shear / punch shear）关键|
|Ch9|Flexural Stress-Strain（弯曲）|三点弯曲（ISO 178）、四点弯曲、悬臂、外层纤维应力上限 5%、柔性材料精度挑战|★★★ — 主要用于卫生用品护围、底膜等薄膜硬挺度测试|
|Ch10|Impact Strength（冲击）|韧性 = 断裂做功、裂纹起始 vs. 扩展能量、临界冲击速度、缺口敏感性、温度-速率耦合|★★★ — 主要用于包装、硬挺部件；无纺布/薄膜可参考缺口韧性|
|Ch11|Tear Properties（撕裂）|撕裂 ≠ 拉伸、撕裂能（fracture-mechanics 本征量）、起始 vs. 扩展力、Trouser / Elmendorf / Angle tear|★★★★★ — 无纺布湿态撕裂、防漏围、表面层撕裂是卫材典型验收项|
|Ch12|Fracture Toughness（断裂韧性）|LEFM / KIC / GIC / CTOD / J-Integral / R-curve；ISO 13586、ASTM D5045、D6068、D5639|★★ — 卫材工程应用尚少，但作为"本征属性"研究工具值得保留|

## 1.3 全书最重要的 5 个跨章节结论

Test results are not absolute — they are a chain-dependent observation.  测试结果的有效性由 sampling → fabrication → conditioning → measurement → statistics 全链条决定，任何一环失控，数据即失去可比性。【跨 Ch1 / Ch2 / Ch3 / Ch6】

Property classification determines which test is appropriate.  根据"Fundamental / Apparent / Functional"三种属性类型匹配测试目的（设计 / 质量控制 / 服役预测），不同目的不能混用同一组数据。【Ch1】

Accelerated testing always introduces artifacts.  加速测试必然引入使用环境中不会发生的效应（升温、升频、极端湿度），因此加速数据只能作为指南，不能替代真实服役测试。【Ch1 / Ch3 / Ch10】

Different methods for the same property cannot be intercompared.  Shore A vs. Durometer、Charpy vs. Izod、Trouser vs. Elmendorf vs. Angle tear、ISO 604 vs. ASTM D695 — 每种测试体系的数值只在自身体系内有效。【Ch5 / Ch7 / Ch8 / Ch10 / Ch11】

Anisotropy & viscoelasticity dominate polymer behaviour.  注塑/纺丝/水刺方向、含水率、应变率、温度共同决定同一材料的力学响应；"材料牌号 = 性能常数"是错觉。【Ch1 / Ch2 / Ch3 / Ch6 / Ch10 / Ch11】

# 2. Cross-Chapter Concept Map（跨章节概念地图）

### 2.1 反复出现的关键概念及其章节分布

||||
|---|---|---|
|Conditioning / Standard Atmosphere|Ch1, Ch3, Ch6, Ch7, Ch8, Ch9|决定所有测试结果起点；ISO 291 是其他章测试方法的"前置依赖"|
|Anisotropy（各向异性）|Ch1, Ch2, Ch6, Ch10, Ch11|与取向（flow direction）、制样工艺耦合；解释 MD/CD 性能差异|
|Viscoelasticity / Time-temperature superposition|Ch1, Ch3, Ch5, Ch6, Ch8, Ch10|导致模量随速率变化、硬度随加载时间衰减、冲击韧性随速率反转|
|Notch sensitivity（缺口敏感性）|Ch2, Ch10, Ch11, Ch12|缺口几何决定冲击/撕裂/断裂韧性起始点|
|Fundamental vs. Apparent vs. Functional properties|Ch1, Ch5, Ch11, Ch12|是全书测试选择与数据解释的方法论骨架|
|Geometry / Test piece design|Ch2, Ch4, Ch5, Ch6, Ch7, Ch8, Ch9, Ch11, Ch12|试样形状、长细比、面积/厚度比直接决定数据可比性|
|Buckling & Shape Factor|Ch7（主要）, Ch6, Ch8|压缩测试核心判据；与拉伸（长细比/屈曲）和剪切（跨度/厚度比）相通|
|Crack initiation vs. propagation|Ch10, Ch11, Ch12|从冲击能 → 撕裂能 → Gc / Jc，是断裂力学从表观到本征的演进|
|Statistical significance / Reproducibility|Ch1, Ch3, Ch5, Ch8, Ch10, Ch11|贯穿全章：数据必须带 n、置信区间、条件参数|
|Cross-standard comparability（ISO vs ASTM vs BS vs JIS）|Ch2, Ch4, Ch5, Ch6, Ch7, Ch8, Ch9, Ch10, Ch11, Ch12|几乎所有测试方法章都强调跨标准不可直接比较|
|Traceability & Accreditation (UKAS / ISO 17025)|Ch1, Ch3, Ch5|溯源与认可贯穿测试体系|

### 2.2 概念网络图（文本呈现）

[Ch1 元命题]
   │ 测试目的 → 属性类型 → 方法选择
   │
   ├──→ [Ch3 Conditioning] ◄──► [Ch2 Test Piece Preparation]
   │       │                              │
   │       └── 平衡、湿度、机械预处理 ───── 制样、切割、模塑、缺口
   │                                        │
   └── 所有性能测试 ─────────────────────────┘
            │
            ├─── 密度/尺寸 [Ch4] ────── 面积 → 拉伸强度换算
            ├─── 硬度 [Ch5] ──────────── 弹簧 vs. 砝码加载
            ├─── 拉伸 [Ch6] ──────────── 四种形态 / 割线模量
            ├─── 压缩 [Ch7] ──────────── 形状因子 / 屈曲
            ├─── 剪切 [Ch8] ──────────── Punch / Iosipescu / Torsion
            ├─── 弯曲 [Ch9] ──────────── 三点/四点/悬臂
            ├─── 冲击 [Ch10] ─────────── 韧性 = 断裂做功
            ├─── 撕裂 [Ch11] ─────────── Trouser / Elmendorf / Angle
            └─── 断裂韧性 [Ch12] ──────── LEFM / KIC / GIC / CTOD / J

# 3. Consolidated Evidence Index（合并证据索引）

### 3.1 按"标准"归类（去重后 ISO / ASTM / BS / JIS / 其他）

||||
|---|---|---|
|ISO 291|Plastics – Standard atmospheres for conditioning and testing|Ch3|
|ISO 1110|Accelerated conditioning (70°C / 62% RH) for hygroscopic plastics (PA)|Ch3|
|ISO 293|Compression moulding of thermoplastic materials|Ch2|
|ISO 294-1/-2/-3|Injection moulding of thermoplastics (general / small bars / plates)|Ch2|
|ISO 295|Compression moulding of thermosets (phenolics, epoxies, UP)|Ch2|
|ISO 3167|Multipurpose tensile dumbbell test pieces|Ch2|
|ISO 1875|Test pieces for impact tests — injection moulded|Ch2|
|ISO 1876|Stamping test pieces from sheet/film|Ch2|
|ISO 3165|Sawing procedures for test pieces|Ch2|
|ISO 3166|Machining procedures for test pieces|Ch2|
|ISO 2811|Measurement of dimensions of test pieces|Ch4|
|ISO 2782|Measurement of mass / volumetric mass|Ch4|
|ISO 1183-1|Density — immersion method|Ch4|
|ISO 1183-2|Density — density column (gradient)|Ch4|
|ISO 1183-3|Density — density gradient column for small films|Ch4|
|ISO 2782-1|Dimensional measurement of test pieces|Ch4|
|ISO 48|Rubber – hardness (IRHD scale, equivalent to Shore A)|Ch5|
|ISO 2039-1|Plastics – Ball indentation hardness|Ch5|
|ISO 2039-2|Plastics – Rockwell hardness|Ch5|
|ISO 527-1/-2/-3/-4|Tensile properties – general / injection / extrusion / thermosets|Ch6|
|ISO 604|Compression stress-strain of plastics (excludes textile-reinforced, cellular, sandwich)|Ch7|
|ISO 458-1|Torsional stiffness (general plastics)|Ch8|
|ISO 458-2|Torsional stiffness of coated fabrics (Clash & Berg)|Ch8|
|ISO 7209|Simple torsion for vulcanised rubber/elastomers|Ch8|
|ISO 178|Flexural properties (3-point)|Ch9|
|ISO 180|Charpy impact – notched and unnotched|Ch10|
|ISO 179-1|Charpy pendulum impact|Ch10|
|ISO 179-2|Charpy tensile impact|Ch10|
|ISO 4665|Tensile impact|Ch10|
|ISO 1144|Izod impact|Ch10|
|ISO 6603|Falling-weight impact on plastic sheeting|Ch10|
|ISO 7765|Falling-weight impact on plates|Ch10|
|ISO 6383-1|Trouser tear (plastics films/sheets)|Ch11|
|ISO 1922|Elmendorf tear (paper/board)|Ch11|
|ISO 11340|Angle tear (initiation)|Ch11|
|ISO 11341|Trapezoid tear (propagation)|Ch11|
|ISO 11342|Crescent tear|Ch11|
|ISO 13586|Fracture mechanics — Plastics – Determination of critical strain energy release rates|Ch12|
|ASTM D1682|Notch-toughness (Tantus impact)|Ch10|
|ASTM D256|Izod impact|Ch10|
|ASTM D4812|High-speed impact on plastics sheet|Ch10|
|ASTM D3029|Falling weight impact|Ch10|
|ASTM D5420|Tensile impact of injection-moulded specimens|Ch10|
|ASTM D4541|Reverse Charpy|Ch10|
|ASTM D3162|Dart impact (falling dart)|Ch10|
|ASTM D3763|Dart impact, high-speed|Ch10|
|ASTM D1004|Falling dart, instrumented|Ch10|
|ASTM D3420|Dart impact (plastics films)|Ch10|
|ASTM D6207|Dart impact (flexible packaging)|Ch10|
|ASTM D1003|Elmendorf tear (plastics films)|Ch11|
|ASTM D1938|Trouser tear|Ch11|
|ASTM D1922|Trapezoid tear|Ch11|
|ASTM D1424|Crescent tear|Ch11|
|ASTM D624|Tear of vulcanised rubber (trouser / tongue / straight)|Ch11|
|ASTM D5440|Tear of flexible sheets|Ch11|
|ASTM D3038|Puncture tear|Ch11|
|ASTM D5045|Fracture toughness – critical stress intensity (KIC)|Ch12|
|ASTM D6068|Fracture toughness – J-R curves (elastic-plastic)|Ch12|
|ASTM D5639|Fracture toughness – K-curve|Ch12|
|ASTM D695|Compression of rigid plastics|Ch7|
|ASTM D732|Punch shear of plastics|Ch8|
|ASTM D2344|Short beam shear of composites|Ch8|
|ASTM D6790|Iosipescu shear of plastics|Ch8|
|ASTM D3039|Iosipescu shear of composites|Ch8|
|ASTM D747|Cantilever flexural test|Ch9|
|ASTM D790|Flexural properties of plastics|Ch9|
|BS 2782-360A|Elmendorf tear|Ch11|
|BS 2782-360B|Trouser tear|Ch11|
|BS 2782-360C|Trapezoid tear|Ch11|
|BS 2782-360D|Crescent tear|Ch11|
|BS 2782-360E|Dart tear|Ch11|
|BS 2782-360F|Tensile tear|Ch11|
|JIS K7111-1/-2|Charpy impact (JIS, separate from ISO 180)|Ch10|

### 3.2 按"公式/物理判据"归类

||||
|---|---|---|
|Stress (MPa) = Force (N) / Area (mm²) [工程应力]|Ch6|无纺布拉伸、芯体拉伸基础|
|Strain (%) = δl / l₀ × 100|Ch6|拉伸率、湿态应变基础|
|Modulus (GPa) = Stress / Strain；割线模量 (0.05%→0.25%)|Ch6|无纺布/薄膜刚度|
|3-point flexural stress: σf = 3Fl / 2bh²|Ch9|护围、底膜硬挺度|
|4-point flexural stress: σf = Fl / bh²|Ch9|同上|
|3-point flexural strain: εf = 6hd / l²|Ch9|柔性材料变形|
|Buckling判据: εc* ≤ 0.4(x/l)²|Ch7|芯体纸浆柱、SAP 堆积压缩|
|长细比 x/l ≥ 0.08 (模量) / ≥ 0.4 (其他)|Ch7|芯体压缩试样设计|
|τ = P/A (Iosipescu pure shear)|Ch8|胶黏剂/复合材料剪切|
|τ = 3F / 2Rt (Punch shear)|Ch8|无纺布湿态剪切|
|G = 32πnN / d⁴ (Clash & Berg torsion)|Ch8|胶黏剂低温柔韧|
|G = (πd⁴/32) × (θ/L) (circular torsion)|Ch8|同上|
|Kc = (E × Gc)⁰·⁵ (Levinson关系)|Ch12|断裂力学本征属性换算|
|Shore A: F = 550 + 75 Ha (N)|Ch5|弹性胶圈、防漏胶|
|Shore D: F = 445 Hd (N)|Ch5|硬塑料部件|
|Ball hardness HBN = F/A (reduced load & depth)|Ch5|硬塑部件|
|Rockwell HRR = 130 – (R – 0.002)/0.002|Ch5|同上|
|Durometer D = 100 – 500h / s|Ch5|弹性件|

### 3.3 按"数据/参数"归类（含关键数值）

|||||
|---|---|---|---|
|标准大气 A: 23°C / 50% RH（优选）|ISO 291|Ch3|与大部分实验室空调匹配|
|标准大气 B: 27°C / 65% RH（热带）|ISO 291|Ch3|华南、东南亚工厂常用|
|温度均衡时间下限|≥ 4 h|Ch3|卫材需按材料吸湿性加长|
|温湿度均衡时间下限|≥ 88 h|Ch3|无纺布/纸浆通常需要|
|RH 控制精度：±2% RH|不可达|Ch3|供应商报告若标 ±2% 需质疑|
|RH 控制精度：±5% RH|常有争议|Ch3|实际可达|
|拉伸模量割线应变点|0.05% 与 0.25%|Ch6|卫材无纺布验收常用|
|弯曲应力计算上限纤维应变|≤ 5%|Ch9|底膜、护围|
|4-point 载荷跨距|1/3 或 1/2 支距|Ch9|需明确报告|
|Shore A 试样最小厚度|6 mm|Ch5|卫材弹性胶圈可考虑|
|Shore A 距边缘最小距离|12 mm|Ch5|同上|
|冲击能 20-80% 摆锤容量窗口|Elmendorf|Ch11|湿态/干态无纺布撕裂测试|
|Charpy 冲击速度 4.5–5.5 m/s|ISO 180 / D256|Ch10|材料牌号冲击标准值|
|临界冲击速度（材料反转至脆性）|随材料而异，一般 > 数十 m/s|Ch10|说明标准冲击测试不代表极端工况|
|弯曲刚度柔性材料精度挑战|0.05% 应变 ↔ 仅 0.08 mm 挠度|Ch9|卫材底膜测试精度警戒线|
|拉伸强度中面积测量误差放大|±1% 面积 → ±2% 面积 → 等比例误差到强度|Ch4|gsm、厚度测量决定后续所有换算|

### 3.4 按"案例/方法"归类（重点标注卫材行业价值 ★）

||||
|---|---|---|
|Trouser tear（裤管撕裂）测撕裂能|Ch11|★★★★★ 无纺布湿态撕裂 / 表面层|
|Elmendorf 摆锤撕裂|Ch11|★★★★★ 无纺布、纸浆垫、护围定性对比|
|Angle tear（起始撕裂）|Ch11|★★★★ 防漏围起始点敏感|
|Trouser tear J-integral 分析|Ch11|★★ 学术研究|
|Falling dart / Elmendorf 结果矛盾案例 (Dawson & Bowes)|Ch11|★★★★★ 提醒供应商报告需说明方法|
|CTOD / J-R curve 弹性-塑性断裂|Ch12|★★★ 长期研究|
|SENB / Compact tensile (CT) 断裂试样|Ch12|★★|
|Iosipescu 剪切|Ch8|★★★★ 胶黏剂接头剪切|
|Punch shear (ASTM D732)|Ch8|★★★★★ 无纺布、胶黏剂压切测试|
|Clash & Berg 低温扭转|Ch8|★★★ 胶黏剂低温性能|
|Ball indentation (ISO 2039-1)|Ch5|★★ 硬质塑料部件|
|Durometer Shore A/D|Ch5|★★★ 弹性胶圈（防漏胶、腰部松紧带）|
|3-point flex (ISO 178)|Ch9|★★★★★ 底膜、护围|
|Compression (ISO 604)|Ch7|★★★★★ 芯体蓬松度、SAP 堆积压缩|
|Multi-purpose test piece (ISO 3167)|Ch2|★★★★ 一次制样支持多测试|
|Density column|Ch4|★★★★★ SAP 珠粒堆积密度/粒度分析|
|Accelerated conditioning 70°C/62% RH (ISO 1110)|Ch3|★★★ PA 类工程塑料件|

# 4. Business Integration（卫材行业综合应用）

## 4.1 四大核心材料领域测试方案

### 4.1.1 芯体结构（Core – 木浆 + SAP 复合体）

|||||
|---|---|---|---|
|芯体定量（gsm）|面积/质量测量 [Ch4]|ISO 2782 / ISO 2811|报告 gsm 时必须带面积测量方法；面积 ±1% → gsm ±1%|
|芯体厚度 / 蓬松度|尺寸测量 [Ch4]，注意触压标准压力|ISO 2782-1|明确触压压力值；无纺布/纸浆差异大，需注明|
|芯体湿态/干态压缩应力-应变|压缩应力-应变 [Ch7]|ISO 604；ASTM D695（若为刚性件）|必须报长细比 x/l 及润滑状态；SAP 湿态需等化时间|
|SAP 堆积密度|视密度 [Ch4]|ISO 1183-3|报堆积密度必须带振动/静置条件|
|SAP 珠粒粒度/密度分布|密度梯度柱 [Ch4]|ISO 1183-2 / -3|密度分辨率 ±0.002 mg/ml 可分级|
|芯体拉伸（湿态强度）|拉伸应力-应变 [Ch6]|ISO 527 变形；专用芯体标准|必须披露拉伸速率、含水率、预处理时间|
|芯体剥离（胶带剥离胶）|剪切/剥离 [Ch8, Ch11]|ASTM D3330 类；Ch8 Punch Shear|报告剥离速率与方向|
|芯体弯曲刚度（整体蓬松感）|弯曲 [Ch9]|ISO 178 / ASTM D790|注意厚度方向各向异性|

### 4.1.2 SAP（Super Absorbent Polymer）

|||||
|---|---|---|---|
|SAP 真密度 / 堆积密度|密度 [Ch4]|ISO 1183|区分真密度与视密度，报告时分开|
|SAP 粒度分布|密度梯度柱 [Ch4]|ISO 1183-2/-3|分级粒度分布是验收核心|
|SAP 拉伸强度（湿凝胶态）|拉伸 [Ch6]|ISO 527-3（挤出件/薄膜）；专用测试|明确凝胶含水率与平衡时间|
|SAP 湿凝胶压缩|压缩 [Ch7]|ISO 604 变形|报告形状因子、湿态预处理|
|SAP 冲击行为（脆-韧转换）|冲击 [Ch10]|ISO 180|说明测试速率与临界冲击速度|
|预处理|[Ch3]|ISO 291（23/50）；ISO 1110（加速）|SAP 对湿度敏感，预处理时间 ≥ 88 h|

### 4.1.3 无纺布（Spunlace / Meltblown / Bonded carded）

|||||
|---|---|---|---|
|MD / CD 拉伸强度与断裂延伸率|拉伸 [Ch6]|ISO 527-3（薄膜）；专用纺粘/水刺标准|必须区分 MD/CD 方向；报速率；报预处理|
|割线模量（0.05%-0.25%）|拉伸 [Ch6]|ISO 527|定义割线点|
|湿态拉伸|拉伸 + 预处理 [Ch6, Ch3]|专用|明确含水率/预处理时间|
|Elmendorf 撕裂（干/湿态）|撕裂 [Ch11]|ISO 1922 / ASTM D1003|摆锤能量窗口 20-80%|
|Angle tear（起始撕裂）|撕裂 [Ch11]|ISO 11340 / ASTM D1424|用于防漏围起始点|
|定量 gsm|面积/质量 [Ch4]|ISO 2782|精度 ±1%|
|厚度|尺寸测量 [Ch4]|ISO 2811|压力参数必须披露|
|冲击/缺口韧性|冲击 [Ch10]|ISO 180 / ASTM D256|用于对比不同基料|
|预处理|[Ch3]|ISO 291|平衡时间；湿度敏感|

### 4.1.4 胶黏剂（胶条 / 点胶 / 复膜胶）

|||||
|---|---|---|---|
|接头剪切强度（lap / punch shear）|剪切 [Ch8]|ASTM D732 / D2344|报告加载速率、试样厚度、失效模式|
|剥离强度（180° / 90°）|拉伸（变形）[Ch6]|ASTM D3330 类；Ch6 拉伸原理|剥离速率；预处理湿度|
|剪切模量（低温）|Clash & Berg [Ch8]|ISO 458-2|低温柔韧性验收|
|胶黏剂硬度（固化后）|硬度 [Ch5]|ISO 2039-1/-2；Shore A/D|固化时间、厚度 ≥ 6 mm|
|弯曲（胶线硬挺度）|弯曲 [Ch9]|ISO 178|用于护围胶线|
|断裂韧性（研究阶段）|[Ch12]|ASTM D5045|高端胶黏剂|
|预处理（温湿度敏感）|[Ch3]|ISO 291|胶黏剂对 RH 敏感，控制严格|

## 4.2 卫材采购验收建议矩阵（综合）

|||||
|---|---|---|---|
|拉伸强度 (MD/CD)|Ch6|ISO 527-3 / ASTM D882|报速率、预处理、模量定义（割线/切线）、失效模式|
|拉伸模量|Ch6|ISO 527|明确 0.05%→0.25% 割线或切线|
|湿态拉伸强度|Ch6 + Ch3|专用 / ISO 527 变形|含水率、预处理时间、速率|
|压缩强度 / 蓬松度|Ch7|ISO 604|长细比、形状因子、润滑状态|
|弯曲刚度|Ch9|ISO 178 / ASTM D790|三点 vs 四点、载荷跨距、厚度|
|剪切强度|Ch8|ASTM D732 / D2344 / D6790|加载速率、试样厚度、失效模式|
|冲击强度|Ch10|ISO 180 / D256 / D6207|缺口尺寸、速率、温度、能量窗口|
|撕裂强度 (Trouser)|Ch11|ISO 6383-1 / ASTM D1938|速度、厚度归一化|
|撕裂强度 (Elmendorf)|Ch11|ISO 1922 / ASTM D1003|摆锤容量窗口 20-80%|
|起始撕裂 (Angle)|Ch11|ISO 11340|角度尺寸、速度|
|密度（真/视）|Ch4|ISO 1183|温度、方法、分级粒度|
|厚度|Ch4|ISO 2811 / ISO 2782-1|触压压力值|
|gsm / 定量|Ch4|ISO 2782|面积测量方法|
|硬度（弹性胶件）|Ch5|ISO 48 / ISO 2039-1/-2 / Shore|加载时间、厚度、离边距|
|预处理|Ch3|ISO 291（23/50）；ISO 1110|RH 精度 ±5%；均衡时间 ≥ 88 h（吸湿材料）|
|断裂韧性（研发）|Ch12|ISO 13586 / ASTM D5045 / D6068|试样缺口精度、加载速率、失效模式|

# 5. Standards & Methods Reference（标准与方法速查）

## 5.1 标准汇总（按组织）

### ISO 系列

|||
|---|---|
|ISO 291|塑料调湿和测试标准大气|
|ISO 293|热塑性塑料压缩模塑试样|
|ISO 294-1/-2/-3|热塑性塑料注塑试样（通用/小棒/小板）|
|ISO 295|热固性塑料压缩模塑试样|
|ISO 2782-1|塑料试样尺寸测量|
|ISO 2811|塑料试样尺寸测量|
|ISO 1183-1/-2/-3|密度（浸入法/梯度柱法/薄膜）|
|ISO 3167|多用途拉伸哑铃试样|
|ISO 1875/1876|冲击试样（注塑/片材）|
|ISO 3165/3166|切割/机加工试样|
|ISO 48|橡胶硬度 IRHD（= Shore A）|
|ISO 2039-1/-2|塑料硬度（球压入/洛氏）|
|ISO 527-1/-2/-3/-4|拉伸性能（通用/注塑/挤出/热固）|
|ISO 604|塑料压缩应力-应变|
|ISO 458-1/-2|塑料/涂层织物扭转刚度|
|ISO 7209|橡胶/弹性体简单扭转|
|ISO 178|塑料弯曲性能（三点）|
|ISO 179-1/-2|Charpy 摆锤冲击（常规/拉伸冲击）|
|ISO 180|Charpy 冲击（缺口/无缺口）|
|ISO 4665|拉伸冲击|
|ISO 1144|Izod 冲击|
|ISO 6603|落锤冲击（片材）|
|ISO 7765|落锤冲击（板）|
|ISO 6383-1|Trouser 撕裂|
|ISO 1922|Elmendorf 撕裂（纸/纸板）|
|ISO 11340/11341/11342|角度/梯形/月牙撕裂|
|ISO 13586|塑料断裂力学（临界能量释放率）|
|ISO 1110|加速预处理|

### ASTM 系列

|||
|---|---|
|D695|刚性塑料压缩|
|D732|冲压剪切|
|D2344|复合材料短梁剪切|
|D6790|Iosipescu 剪切|
|D3039|复合材料 Iosipescu 剪切|
|D790 / D747|弯曲 / 悬臂弯曲|
|D5045 / D5639 / D6068|断裂韧性 KIC / K-curve / J-R|
|D256 / D1822 / D4541|Izod / 高冲击 Izod / 反向 Charpy|
|D4812|高速冲击片材|
|D3029 / D3420 / D6207 / D1003 / D3763 / D5420|落锤/飞镖冲击（多类）|
|D1003|Elmendorf 撕裂|
|D1938 / D1922 / D1424 / D624 / D5440 / D3038|Trouser / 梯形 / 月牙 / 橡胶 / 柔性片 / 穿刺撕裂|
|D1682|Tantus 缺口韧性|
|D5420|注塑件拉伸冲击|
|D2223|MDR 硬度|
|D1415|IRHD|
|D2240|Shore|

### BS / JIS

- BS 2782-360 A–F：Elmendorf / Trouser / Trapezoid / Crescent / Dart / Tensile tear
- JIS K7111-1/-2：Charpy 冲击（JIS，与 ISO 180 区分）
## 5.2 测试方法对照表

|||||
|---|---|---|---|
|拉伸强度/模量|ISO 527-2/3；ASTM D638|注塑件、薄膜、挤出件、无纺布|高（A 级机）|
|拉伸强度（热固）|ISO 527-4；ASTM D695（压缩）|酚醛、环氧、UP|中|
|压缩强度/模量|ISO 604；ASTM D695|刚性塑料、泡沫（除外）|中；注意形状因子|
|弯曲刚度/强度|ISO 178；ASTM D790|硬质/半硬质塑料、薄板|高|
|悬臂弯曲（低模量估计）|ASTM D747|硬挺度对比|低-中|
|剪切（接头）|Punch shear ASTM D732；Iosipescu D6790|塑料、复合材料、胶黏剂|高（Iosipescu 最纯）|
|扭转刚度/低温|Clash & Berg (ISO 458-2)；简单扭转 (ISO 7209)|涂层织物、橡胶|中-高|
|冲击（刚性件）|Charpy (ISO 180/179)；Izod (D256/ISO 1144)；Tantus (D1682)|注塑件、板材|中（速率固定）|
|冲击（薄膜/软片）|Falling dart (D3420/7765/6603/1003)；落锤 (D3029/6207/4812)|薄膜、包装膜、柔性片|中；能量窗口敏感|
|撕裂（软片/薄膜）|Trouser (D1938/ISO 6383-1)；Elmendorf (D1003/ISO 1922)；Angle (D1424/ISO 11340)|薄膜、无纺布、纸浆|高（Trouser 可算撕裂能）|
|硬度（软塑/橡胶）|Durometer Shore A；IRHD (ISO 48)|弹性胶圈、橡胶|中|
|硬度（硬塑）|Shore D；Ball (ISO 2039-1)；Rockwell (ISO 2039-2)；Vickers (微)|硬塑料、工程塑料|高（球压/维氏）|
|密度（真密度）|浸入法 (ISO 1183-1)|注塑/挤出件|高（±1 mg 天平）|
|密度（分级粒度）|梯度柱 (ISO 1183-2/-3)|SAP 珠粒、薄膜|高（±0.002）|
|尺寸/厚度|接触/非接触 (ISO 2811 / 2782-1)|所有材料|中；需报告触压|
|断裂韧性 KIC|SENB / CT (ASTM D5045/ISO 13586)|塑料（含半结晶）|高；多试样|
|断裂韧性 GIC (弹性)|SENB / CT (ISO 13586)|塑料|高|
|断裂韧性 J-R (弹-塑性)|ASTM D6068；CTOD|韧性塑料|高；多试样|
|预处理|ISO 291（23/50 或 27/65）；ISO 1110 加速|所有|温度 ±1°C；湿度 ±5% RH|

# 6. Consolidated Key Quotes（合并金句索引）

以下 20 条金句从 12 章中精选，均为全书最具普适性、方法论价值或卫材行业应用价值的原文。

### 1. 测试目的决定测试方法

- 英文原文："The fundamental importance of the reason for testing is that to a considerable extent the choice of test method and test conditions depends on the purpose of the test."
- 中文：测试目的的根本重要性在于，在很大程度上，测试方法和测试条件的选择取决于测试目的。
- 来源：[Ch1, Line 85-90]
### 2. 测试数据从来不是绝对事实

- 英文原文："A material has a tensile strength of 10 units" is not an absolute fact. The result is limited by how the material was sampled, how it was fabricated, how the test pieces were formed, what conditioning it received, the dimensions of the test piece and the test conditions such as temperature and strain rate.
- 中文："材料的拉伸强度为 10 个单位"并不是绝对事实——结果受取样、制样、试样成型、预处理、尺寸以及温度与应变率等条件限制。
- 来源：[Ch1, Line 343-348]
### 3. 加速测试的陷阱

- 英文原文："Trouble-free service over a period of years may be essential, yet tests have lasted but a few seconds or minutes. … These necessary changes may in themselves induce effects which would never occur at the usual ambient temperature, etc., and thus misleading data may result."
- 中文：虽然可能需要多年无故障服役，但测试仅持续数秒或数分钟。必要的加速变量改变本身可能引入实际环境中不会发生的效应，从而产生误导性数据。
- 来源：[Ch1, Line 415-423]
### 4. 测试结果取决于试样如何成型

- 英文原文："The properties of a material, and hence the test results, are dependent on how the material was formed, not only on whether there was any cutting or machining involved but on the details of mould configuration and moulding conditions."
- 中文：材料性能以及测试结果依赖于材料的成型方式，不仅取决于是否经过切割或机加工，还取决于模具配置与成型条件的细节。
- 来源：[Ch2, Line 17-18]
### 5. 注塑与压缩模塑取向差异

- 英文原文："The orientation produced in an injection moulded test piece may yield very different results from those from a relatively non-oriented compression moulding process."
- 中文：注塑试样中产生的取向可能与压缩模塑（相对无取向）过程产生截然不同的测试结果。
- 来源：[Ch2, Line 70-73]
### 6. 切割刀具对可重复性的致命影响

- 英文原文："It cannot be over-emphasised that many low results and cases of poor reproducibility are caused by blunt or chipped cutting dies."
- 中文：必须再三强调：许多偏低结果与可重复性差的案例都源于钝刀或崩刃的切割模具。
- 来源：[Ch2, Line 300-304]
### 7. 预处理的目标是建立参考点

- 英文原文："The process of conditioning test pieces is aimed at providing a reference point for the measurement of properties."
- 中文：试样预处理的过程旨在为性能测量提供一个参考点。
- 来源：[Ch3, Line 11-13]
### 8. 湿度控制精度的物理极限

- 英文原文："The latest ISO 291 recognises the fact that ± 2% RH is effectively impossible to attain and ± 5% RH is often debatable."
- 中文：最新版 ISO 291 承认：±2% RH 实际上不可能达到，而 ±5% RH 也常常存疑。
- 来源：[Ch3, Line 102-109]
### 9. 温度与湿度的均衡时间下限

- 英文原文："The plastics standard requires not less than 4 hours for temperature alone and not less than 88 hours for temperature and humidity."
- 中文：塑料标准要求仅温度均衡不少于 4 小时，温湿度均衡不少于 88 小时。
- 来源：[Ch3, Line 125-135]
### 10. 横截面积误差直接传递到强度

- 英文原文："Taking the example of the determination of tensile strength, any error in the measurement of the cross section directly results in an equivalent percentage error in the strength measurement."
- 中文：以拉伸强度测定为例，横截面积测量的任何误差都会直接转化为同等百分比的强度测量误差。
- 来源：[Ch4, Line 23-29]
### 11. 硬度不是本征属性

- 英文原文："Hardness is by no means a fundamental property. The result depends on the indentor geometry and degree of indentation as well as the time of indentation after which the measurement is made."
- 中文：硬度绝不是什么本征属性——其结果取决于压头几何形状、压入深度以及测量时的加载时间。
- 来源：[Ch5, Line 11-14]
### 12. 拉伸——应用最广的短时性能

- 英文原文："The short-term tensile characteristics of a material are probably the most commonly derived of all the properties that can be determined … Knowledge of these characteristics can give materials scientists, technologists, materials specifiers and designers an insight into the potential performance of a material."
- 中文：材料的短时拉伸特性可能是所有可测定性能中最常测得的——了解这些特性可为材料科学家、技术人员、规格制定者和设计师提供洞察。
- 来源：[Ch6, Line 9-15]
### 13. 聚合物非线性与黏弹性

- 英文原文："Unfortunately, polymeric materials are non-linear and consequently their stress-strain characteristic is not as simple as that shown in Figure 6.4 and hence their modulus is not a constant."
- 中文：遗憾的是，聚合物材料是非线性的，因此其应力-应变特性不像理想弹性体那样简单，模量并非常数。
- 来源：[Ch6, Line 92-95]
### 14. 应变率控制聚合物行为

- 英文原文："The strength, and as a consequence the modulus of the material appears to increase with increasing rate of test … if the rate of extension was increased sufficiently the material would start to exhibit brittle behaviour."
- 中文：随着试验速率增大，材料强度及模量随之升高；若速率足够大，材料将开始表现出脆性行为。
- 来源：[Ch6, Line 278-287]
### 15. 压缩测试的屈曲判据

- 英文原文："The relationship between the parameters which govern buckling is given as: εc ≤ 0.4(x/l)²."*
- 中文：控制屈曲的参数关系为：εc* ≤ 0.4(x/l)²（x 为临界截面尺寸，l 为长度）。
- 来源：[Ch7, Line 99-102]
### 16. 剪切测试的标准化之困

- 英文原文："Shear stresses are involved in many applications of plastics but very little shear testing is carried out except on fibre reinforced materials."
- 中文：剪切应力存在于许多塑料应用中，但除了纤维增强材料外，很少有实际进行剪切测试。
- 来源：[Ch8, Line 25-26]
### 17. Iosipescu 剪切应力是纯剪切

- 英文原文："Perhaps surprisingly, the stress across the test piece between the notches is pure shear and is uniform. The shear stress is simply given by τ = P/A."
- 中文：令人惊讶的是，缺口之间的应力是均匀的纯剪切，剪切应力简单地由 τ = P/A 给出。
- 来源：[Ch8, Line 233-238]
### 18. 弯曲应力只代表外层纤维

- 英文原文："It should be noted, that the stress and strain that are calculated are the maximum outer fibre stresses and strains … they refer to the outer layer of the material rather than the bulk."
- 中文：须注意：计算得到的应力与应变是最大外层纤维应力与应变——它们指的是材料的外层，而不是整体。
- 来源：[Ch9, Line 18-23]
### 19. 冲击——韧性的直接度量

- 英文原文："The one advantage impact tests offer is a ready measure of the actual energy required to break the test piece."
- 中文：冲击测试唯一（也是最核心的）优势在于：它可以直接测量断裂试样所需的实际能量。
- 来源：[Ch10, Line 16-17]
### 20. 所有聚合物都存在临界冲击速度

- 英文原文："All polymer materials seem to have a critical velocity above which they behave as glassy, brittle materials."
- 中文：所有聚合物材料似乎都存在一个临界速度，超过该速度，材料就会表现为玻璃态的脆性材料。
- 来源：[Ch10, Line 94-96]
### 21. 缺口敏感性

- 英文原文："A notch creates a localised stress concentration where the true stress can be many times higher than the bulk stress being imposed on the test piece or object as a whole."
- 中文：缺口产生局部应力集中，此处真实应力可能是施加在试样整体上的表观应力的数倍。
- 来源：[Ch10, Line 129-131]
### 22. 温度-速率耦合的脆-韧转换

- 英文原文："Note that increasing temperature has the opposite effect of increasing speed and so there is not a single temperature at which brittleness occurs, but a locus of temperature/speed values where the transition from ductile to brittle behaviour takes place."
- 中文：升高温度与提高速度效果相反，因此脆性并非发生在某个单一温度，而是一系列温度/速度组合构成的转变轨迹。
- 来源：[Ch10, Line 117-120]
### 23. 分子取向导致冲击各向异性

- 英文原文："The impact strength is always higher in the direction of flow … at right angles to the flow or drawing direction the impact properties can be significantly reduced."
- 中文：冲击强度在流动方向上总是更高；垂直于流动/拉伸方向时冲击性能会显著降低。
- 来源：[Ch10, Line 179-189]
### 24. 撕裂能是本征属性

- 英文原文："The tearing energy is in theory a basic material property and independent of test piece geometry so that if the tearing energy and the elastic characteristics of the material are known the force needed to tear a given geometry can be predicted."
- 中文：撕裂能在理论上是一种基本材料属性，与试样几何形状无关——只要知道撕裂能及材料弹性特性，即可预测给定几何形状的撕裂力。
- 来源：[Ch11, Line 24-29]
### 25. 起始力与扩展力必须分开

- 英文原文："A very important distinction can be made between the force to initiate a tear as opposed to that to propagate a tear … the propagation force can be very much smaller."
- 中文：必须严格区分撕裂起始力与撕裂扩展力——后者可能比前者小得多。
- 来源：[Ch11, Line 54-59]
### 26. 传统测试的根本缺陷

- 英文原文："All the traditional standard stress-strain tests for plastics have a severe handicap for design purposes because the results are geometry dependent and they do not yield fundamental properties."
- 中文：所有传统的塑料应力-应变标准测试在设计用途上都有严重缺陷，因为结果是几何形状依赖的，不能得到本征属性。
- 来源：[Ch12, Line 8-9]
### 27. 断裂力学的基本判据

- 英文原文："The crack will grow when the stress intensity at the tip of the crack exceeds the cohesive strength of the material."
- 中文：当裂纹尖端的应力强度超过材料的内聚强度时，裂纹就会扩展。
- 来源：[Ch12, Line 27-28]
### 28. 统计与变异

- 英文原文："The basic fact is that all measurements are subject to variability and the sources of variability are numerous."
- 中文：基本事实是：所有测量都受变异性影响，且变异来源众多。
- 来源：[Ch1, Line 379-380]

报告完

本综合报告基于《Handbook of Polymer Testing – Short-Term Mechanical Tests》（Brown, Rapra, 2002）12 章深度拆书报告合成，所有章节报告源文件位于 /sandbox/workspace/Ebook_Extract/Handbook_of_Polymer_Testing/reports/。

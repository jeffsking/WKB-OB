---
type: source
title: "Polymer Testing Handbook Short-Term Mechanical Tests"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Polymer Testing/Handbook of Polymer Testing_full_report.md.md
date_published: 2002
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "'A material has a tensile strength of 10 units\" is not an absolute fact. The result is limited by how the material was sampled, how it was fabricated, how the test pieces were formed, what conditioning it received, the dimensions of the test piece and the test conditions such as temperature and strain rate.' (Ch1)"
  - "'The latest ISO 291 recognises the fact that ± 2% RH is effectively impossible to attain and ± 5% RH is often debatable.' Conditioning requires 'not less than 4 hours for temperature alone and not less than 88 hours for temperature and humidity.' (Ch3)"
  - "'Taking the example of the determination of tensile strength, any error in the measurement of the cross section directly results in an equivalent percentage error in the strength measurement.' (Ch4)"
  - "'Hardness is by no means a fundamental property. The result depends on the indentor geometry and degree of indentation as well as the time of indentation after which the measurement is made.' (Ch5)"
  - "Compression buckling criterion: 'εc* ≤ 0.4(x/l)²'; slenderness x/l ≥ 0.08 for modulus and ≥ 0.4 otherwise (Ch7). Iosipescu shear gives pure, uniform shear: 'τ = P/A' (Ch8)."
  - "'A very important distinction can be made between the force to initiate a tear as opposed to that to propagate a tear … the propagation force can be very much smaller.' Tearing energy 'is in theory a basic material property and independent of test piece geometry' (Ch11)."
  - "'All polymer materials seem to have a critical velocity above which they behave as glassy, brittle materials'; 'increasing temperature has the opposite effect of increasing speed' — ductile-to-brittle is a temperature/speed locus, not a single temperature (Ch10)."
summary_cn: "Brown《Handbook of Polymer Testing – Short-Term Mechanical Tests》（Rapra, 2002, 12 章 210 页）综合拆解：核心元命题是"测试结果不是绝对事实"，可比性依赖取样→制样→调湿→测量→统计全链条一致；覆盖密度/尺寸、硬度、拉伸、压缩、剪切、弯曲、冲击、撕裂、断裂韧性九类方法，给出卫材（芯体/SAP/无纺布/胶黏剂）来料验收的口径与标准清单。"
tags: ["source/book", "polymer-testing", "short-term-mechanical-tests", "conditioning", "ISO-291", "tensile", "compression", "shear", "tear", "impact", "fracture-toughness", "incoming-QC"]
tags_zh: ["聚合物测试", "短期力学测试", "调湿预处理", "拉伸", "压缩", "剪切", "撕裂", "冲击", "断裂韧性", "来料检验"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Raw Material STM - Nanjing Plant（原材料STM-NJ）]]", "[[Absorbent Product Testing]]", "[[Characterisation, testing and modelling of nonwoven fabrics]]", "[[NWSP and ISO Test Methods Comparison 11-10-2022 updated.docx]]", "[[Raw Material Testing Method Summary（原材料测试方法汇总表）]]"]
---

# Polymer Testing Handbook Short-Term Mechanical Tests 聚合物测试手册：短期力学测试

> Source: *Handbook of Polymer Testing – Short-Term Mechanical Tests*, Edward N. Brown, Rapra, 2002; 210 pages / 12 chapters. Compiled from the consolidated full-book report `Handbook of Polymer Testing_full_report.md.md` (synthesised 2026-06-27 from the 12 chapter-level deep-read reports).
> Central meta-claim 全书元命题：聚合物测试数值从来不是绝对事实，其可比性依赖 sampling → fabrication → conditioning → measurement → statistics 全链条的一致性。

## Five cross-chapter conclusions 五大跨章节结论

1. **Test results are not absolute 测试结果非绝对**：有效性由取样 → 制样 → 调湿 → 测量 → 统计全链条决定，任何一环失控，数据即失去可比性。【Ch1/2/3/6】
2. **Property classification determines the test 属性分类决定方法**：Fundamental / Apparent / Functional 三类属性分别对应设计 / 质量控制 / 服役预测三种目的，不同目的不能混用同一组数据。【Ch1】
3. **Accelerated testing always introduces artifacts 加速测试必然引入伪影**：升温、升频、极端湿度会引入使用环境中不会发生的效应，加速数据只能作指南，不能替代真实服役测试。【Ch1/3/10】
4. **Same property, different method → not intercomparable 同属性不同方法不可互比**：Shore A vs Durometer、Charpy vs Izod、Trouser vs Elmendorf vs Angle tear、ISO 604 vs ASTM D695 —— 数值只在自身体系内有效。【Ch5/7/8/10/11】
5. **Anisotropy & viscoelasticity dominate 各向异性与黏弹性主导**：取向、含水率、应变率、温度共同决定响应；"材料牌号 = 性能常数"是错觉。【Ch1/2/3/6/10/11】

## Chapter map 12 章概览

| Ch | Topic 主题 | Core content 核心内容 | Hygiene relevance 卫材相关度 |
| --- | --- | --- | --- |
| 1 | Introduction 导论 | 测试目的决定方法；属性三分法；加速测试陷阱；溯源与认可 | ★★★★★ 供应商测试方案谈判 |
| 2 | Test piece preparation 试样制备 | 模塑 vs 切割；ISO 3167 多用途试样；冲压与裁切误差 | ★★★★ 实验室制样 SOP |
| 3 | Conditioning 调湿 | ISO 291 标准大气（23/50 与 27/65）；±2% RH 不可达；均衡时间；机械预处理 | ★★★★★ 无纺布与 SAP 极其敏感 |
| 4 | Mass, density, dimensions | 真密度/视密度/梯度柱；几何精度；面积误差放大 | ★★★★ SAP 堆积密度、无纺布 gsm、厚度 |
| 5 | Hardness 硬度 | Shore A/D、IRHD、Ball indentation（ISO 2039）、Rockwell、维氏 | ★★ 仅弹性胶圈等辅助件 |
| 6 | Tensile stress-strain 拉伸 | 工程 vs 真应力；割线模量；四种应力-应变形态；应变率效应 | ★★★★★ 无纺布 MD/CD、芯体湿强 |
| 7 | Compression stress-strain 压缩 | 形状因子；屈曲判据；长细比；润滑端部效应；ISO 604 | ★★★★★ 芯体蓬松度、SAP 堆积压缩 |
| 8 | Shear properties 剪切 | 简单 vs 纯剪切；Punch、Iosipescu、Clash & Berg；ISO 458 | ★★★★ 胶黏剂接头 |
| 9 | Flexural stress-strain 弯曲 | 三点/四点/悬臂；外层纤维应力上限 5% | ★★★ 护围、底膜硬挺度 |
| 10 | Impact strength 冲击 | 韧性 = 断裂做功；起始 vs 扩展能量；临界冲击速度；缺口敏感性 | ★★★ 薄膜/无纺布缺口韧性参考 |
| 11 | Tear properties 撕裂 | 撕裂 ≠ 拉伸；撕裂能是本征量；起始 vs 扩展力；Trouser/Elmendorf/Angle | ★★★★★ 无纺布湿态撕裂、防漏围 |
| 12 | Fracture toughness 断裂韧性 | LEFM / K_IC / G_IC / CTOD / J-Integral / R-curve | ★★ 本征属性研究工具 |

## Conditioning 调湿（Ch3）—— 所有测试的前置依赖

| Parameter 参数 | Value 数值 | Source 出处 |
| --- | --- | --- |
| Standard atmosphere A 标准大气 A | 23°C / 50% RH（优选） | ISO 291 |
| Standard atmosphere B 标准大气 B | 27°C / 65% RH（热带） | ISO 291 |
| Temperature equilibration 温度均衡 | ≥ 4 h | Ch3 |
| Temperature + humidity equilibration 温湿度均衡 | ≥ 88 h | Ch3 |
| RH control ±2% | 不可达 effectively impossible | ISO 291（最新版承认） |
| RH control ±5% | 常有争议 often debatable | ISO 291 |
| Accelerated conditioning 加速预处理 | 70°C / 62% RH（吸湿性塑料如 PA） | ISO 1110 |

> "The process of conditioning test pieces is aimed at providing a reference point for the measurement of properties."

## Key formulas and criteria 关键公式与判据

| Item 项目 | Formula / criterion 公式或判据 | Ch |
| --- | --- | --- |
| Engineering stress 工程应力 | σ (MPa) = Force (N) / Area (mm²) | 6 |
| Strain 应变 | ε (%) = δl / l₀ × 100 | 6 |
| Secant modulus 割线模量 | Stress / Strain，割线点 0.05% → 0.25% | 6 |
| 3-point flexural stress 三点弯曲应力 | σ_f = 3Fl / 2bh² | 9 |
| 4-point flexural stress 四点弯曲应力 | σ_f = Fl / bh² | 9 |
| 3-point flexural strain 三点弯曲应变 | ε_f = 6hd / l² | 9 |
| Buckling criterion 屈曲判据 | ε_c* ≤ 0.4(x/l)² | 7 |
| Slenderness 长细比 | x/l ≥ 0.08（模量）/ ≥ 0.4（其他） | 7 |
| Iosipescu pure shear 纯剪切 | τ = P/A | 8 |
| Punch shear 冲压剪切 | τ = 3F / 2Rt | 8 |
| Clash & Berg torsion 扭转 | G = 32πnN / d⁴ | 8 |
| Circular torsion 圆轴扭转 | G = (πd⁴/32) × (θ/L) | 8 |
| Levinson relation | K_c = (E × G_c)^0.5 | 12 |
| Shore A load | F = 550 + 75 H_a (N) | 5 |
| Shore D load | F = 445 H_d (N) | 5 |
| Rockwell HRR | HRR = 130 – (R – 0.002)/0.002 | 5 |

## Key data and thresholds 关键数值与阈值

| Item 项目 | Value 数值 | Ch |
| --- | --- | --- |
| Secant strain points 割线应变点 | 0.05% 与 0.25% | 6 |
| Max outer-fibre strain in flexure 弯曲外层纤维应变上限 | ≤ 5% | 9 |
| 4-point load span 四点载荷跨距 | 1/3 或 1/2 支距（须明确报告） | 9 |
| Shore A min specimen thickness 最小厚度 | 6 mm | 5 |
| Shore A min distance to edge 距边缘最小距离 | 12 mm | 5 |
| Elmendorf pendulum capacity window 摆锤容量窗口 | 20–80% | 11 |
| Charpy impact velocity 冲击速度 | 4.5–5.5 m/s | 10 |
| Critical impact velocity 临界冲击速度 | 随材料而异，一般 > 数十 m/s | 10 |
| Flexural precision warning 弯曲精度警戒 | 0.05% 应变 ↔ 仅 0.08 mm 挠度 | 9 |
| Area error propagation 面积误差传递 | ±1% 面积 → 等比例强度误差 | 4 |
| Density column resolution 密度梯度柱分辨率 | ±0.002 mg/ml 可分级 | 4 |

## Key quotes 金句索引（原文摘录）

- 测试目的（Ch1）："The fundamental importance of the reason for testing is that to a considerable extent the choice of test method and test conditions depends on the purpose of the test."
- 非绝对事实（Ch1）："A material has a tensile strength of 10 units" is not an absolute fact. The result is limited by how the material was sampled, how it was fabricated, how the test pieces were formed, what conditioning it received, the dimensions of the test piece and the test conditions such as temperature and strain rate."
- 加速陷阱（Ch1）："Trouble-free service over a period of years may be essential, yet tests have lasted but a few seconds or minutes. … These necessary changes may in themselves induce effects which would never occur at the usual ambient temperature, etc., and thus misleading data may result."
- 成型决定结果（Ch2）："The properties of a material, and hence the test results, are dependent on how the material was formed, not only on whether there was any cutting or machining involved but on the details of mould configuration and moulding conditions."
- 切割刀具（Ch2）："It cannot be over-emphasised that many low results and cases of poor reproducibility are caused by blunt or chipped cutting dies."
- 硬度非本征（Ch5）："Hardness is by no means a fundamental property. The result depends on the indentor geometry and degree of indentation as well as the time of indentation after which the measurement is made."
- 非线性（Ch6）："Unfortunately, polymeric materials are non-linear and consequently their stress-strain characteristic is not as simple as that shown in Figure 6.4 and hence their modulus is not a constant."
- 应变率（Ch6）："The strength, and as a consequence the modulus of the material appears to increase with increasing rate of test … if the rate of extension was increased sufficiently the material would start to exhibit brittle behaviour."
- 剪切测试之困（Ch8）："Shear stresses are involved in many applications of plastics but very little shear testing is carried out except on fibre reinforced materials."
- 弯曲只代表外层（Ch9）："It should be noted, that the stress and strain that are calculated are the maximum outer fibre stresses and strains … they refer to the outer layer of the material rather than the bulk."
- 冲击价值（Ch10）："The one advantage impact tests offer is a ready measure of the actual energy required to break the test piece."
- 临界速度（Ch10）："All polymer materials seem to have a critical velocity above which they behave as glassy, brittle materials."
- 缺口（Ch10）："A notch creates a localised stress concentration where the true stress can be many times higher than the bulk stress being imposed on the test piece or object as a whole."
- 温度-速率耦合（Ch10）："Note that increasing temperature has the opposite effect of increasing speed and so there is not a single temperature at which brittleness occurs, but a locus of temperature/speed values where the transition from ductile to brittle behaviour takes place."
- 撕裂能（Ch11）："The tearing energy is in theory a basic material property and independent of test piece geometry…"
- 起始 vs 扩展（Ch11）："A very important distinction can be made between the force to initiate a tear as opposed to that to propagate a tear … the propagation force can be very much smaller."
- 传统测试缺陷（Ch12）："All the traditional standard stress-strain tests for plastics have a severe handicap for design purposes because the results are geometry dependent and they do not yield fundamental properties."
- 变异性（Ch1）："The basic fact is that all measurements are subject to variability and the sources of variability are numerous."

## Standards index 标准清单（按组织）

- **ISO**：291（调湿）、293/294-1~3/295（制样）、3167（多用途哑铃）、1875/1876（冲击试样）、3165/3166（切割/机加工）、2782-1/2811（尺寸）、1183-1/-2/-3（密度）、48（IRHD 硬度）、2039-1/-2（球压入/洛氏）、527-1~-4（拉伸）、604（压缩）、458-1/-2（扭转）、7209（橡胶扭转）、178（三点弯曲）、179-1/-2、180（Charpy）、4665（拉伸冲击）、1144（Izod）、6603/7765（落锤）、6383-1（Trouser 撕裂）、1922（Elmendorf）、11340/11341/11342（角度/梯形/月牙）、13586（断裂力学）、1110（加速预处理）。
- **ASTM**：D695（压缩）、D732（冲压剪切）、D2344、D6790/D3039（Iosipescu）、D790/D747（弯曲/悬臂）、D5045/D5639/D6068（K_IC / K-curve / J-R）、D256/D1822/D4541（Izod/反向 Charpy）、D4812、D3029/D3420/D6207/D1003/D3763/D5420（落锤/飞镖）、D1003/D1938/D1922/D1424/D624/D5440/D3038（各类撕裂）、D1682（Tantus）、D2240（Shore）、D1415（IRHD）。
- **BS / JIS**：BS 2782-360 A–F（六类撕裂）；JIS K7111-1/-2（Charpy，与 ISO 180 区分）。

## Hygiene implication 卫材关联

Directly relevant — this is the methodology backbone for incoming QC (来料检验) and supplier data adjudication. 四条可落地口径：
1. **向供应商索要可比数据的检查表**：任何拉伸/压缩/撕裂报告都必须带——取样方式、制样工艺（模塑 vs 切割、刀具状态）、预处理（ISO 291 大气 + ≥88 h 温湿度均衡）、试样尺寸与面积测量方法、测试速率与温度、n 与置信区间、失效模式。缺任一项即可质疑报告有效性。
2. **调湿是卫材的第一风险点**：无纺布与 SAP 对湿度极敏感；供应商报告若标 ±2% RH 应直接质疑（ISO 291 已承认不可达）；吸湿材料均衡时间应 ≥88 h。
3. **面积/厚度误差直接线性传递到强度**：±1% 面积 → ±1% 强度，故 gsm 与厚度的触压压力必须写入 SOP。
4. **撕裂必须区分起始力与扩展力**：防漏围与面层的撕裂验收尤其如此；Trouser 法可得本征撕裂能，Elmendorf 只能做同体系内定性对比（注意 20–80% 摆锤容量窗口）。另外，MD/CD 方向必须分开报，升温与提速对脆-韧转变效果相反，不能只用单一温度条件判定。

## Related Sources 关联来源

- [[Raw Material STM - Nanjing Plant（原材料STM-NJ）]] — 南京厂原材料标准测试方法，本手册口径的落地对照。
- [[Raw Material Testing Method Summary（原材料测试方法汇总表）]] — 原材料测试方法汇总，可用于逐项核对条件披露完整性。
- [[Absorbent Product Testing]] — 吸收产品测试方法，与力学测试形成完整验收链。
- [[Characterisation, testing and modelling of nonwoven fabrics]] — 非织造布表征与测试，MD/CD 与各向异性议题的延伸。
- [[NWSP and ISO Test Methods Comparison 11-10-2022 updated.docx]] — NWSP 与 ISO 方法对比，对应"跨标准不可直接比较"的告诫。

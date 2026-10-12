---
type: source
title: "Industrial Drying Ch21 Drying of Foodstuffs"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch21.md.md"
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "水分活度阈值：a_w > 0.4 才可能发生氧化；微生物失活要求 a_w ≤ 0.7；a_w 0.1–0.3 下酶活仍可低速持续（p.522）"
  - "水分以不同方式键合于产物：离子基团（羧基、氨基酸）与氢键基团（羟基、酰胺）（p.521）——与纤维素 OH / SAP 羧酸盐一一对应"
  - "热灭菌窗口：≥60 °C 持续 3–5 min 可杀灭昆虫与微生物；低至 48 °C 需 ≥24 h 用于除虫（p.522）"
  - "过热蒸汽干燥食品优势：能耗最多省 50%、'No product oxidation, because there is no direct contact of hot oxygen with the product'、植物检疫级灭菌（p.538–539）"
  - "乳粉赖氨酸损失：喷雾干燥 3–10%，滚筒干燥 5–40%——低水分下与热表面接触最大化热损伤（p.540）"
  - "非酶褐变符合 Arrhenius 动力学 k = k0·exp(−E/RT)，脱脂乳 35–130 °C、3–5% db 水分区间 E ≈ 90816.51 J/mol（p.542–543）"
summary_cn: "本章为食品脱水自足式教程，其水分活度/GAB 平衡水分框架、恒速-降速干燥模型与 Arrhenius 降解动力学可迁移用于绒毛浆残余水分规格与白度回变加速老化设计，但内容整体为食品专属、卫材直接相关性最低。"
tags: ["source/book", "drying", "water-activity", "food", "degradation-kinetics"]
tags_zh: ["来源/书籍", "干燥", "水分活度", "食品", "降解动力学"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch8 Fluidized Bed Dryers]]", "[[Industrial Drying Ch9 Drum Dryers]]", "[[Industrial Drying Ch10 Industrial Spray Drying Systems]]", "[[Industrial Drying Ch17 Conveyor Dryers]]", "[[Industrial Drying Ch19 Superheated Steam Drying]]"]
---

# Chapter 21 — Drying of Foodstuffs

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.21, pp.515–543. (起始页 p.515 由 Ch.20 止于 p.513 推断；正文引证实测范围 p.521–543。)

(Sokhansanj & Jayas 执笔。页码由 PDF 页 − 21 推算，应与印刷版抽查核对。)

**相关度声明**：食品章 — 对卫材**直接相关性低**，价值在于可迁移框架（水分活度、GAB、恒速/降速模型、Arrhenius 动力学），不是可直接套用的案例。诚实评级为六章中最弱（★★★☆☆）。

## Scope 范围与定位

Self-contained food-dehydration primer: objectives, water-activity theory, psychrometrics, full drying-model derivation, physical/thermal properties, dryer catalog, nutrient-loss section. 面向农业/食品工程师，非纤维工程师。

## Water Activity 水分活度框架（最可迁移）

> "Oxidation activity is only possible at water activities higher than 0.4 and the rate of inactivation of other organisms requires a water activity of 0.7 or lower. Some enzymatic activities may continue at low levels of water activities of 0.1–0.3 but their reaction rate decreases at low water activities." (p.522)

GAB equation: > "M/M_s = C K a_w / [(1 − K a_w)(1 − K a_w + C K a_w)] where C, K, and M_s are constants." (p.522)

解读：绒毛浆/芯体包裹材料残余水分规格的科学根据——**规格本质是伪装成含水率的 a_w 规格**；用 GAB 把目标 a_w 换算成当地储存 RH 下的工程含水率数字。

## Bound Water Taxonomy 结合水分类

> "Moisture, in the form of water molecules, is bonded to various parts of the product in varying ways as follows: (a) ionic groups, such as carboxyl and amino acids and (b) hydrogen groups, such as hydroxyl and amides." (p.521)

解读：与纤维素（羟基）和交联聚丙烯酸钠 SAP（羧酸盐）一一对应——区分吸收芯体中"自由表面水"（驱动微生物生长）与"结合水"（不驱动）时的现成词汇。

## Thermal Lethality 热灭菌窗口

> "The temperature should be at least 60°C for a short duration of 3 to 5 min. Lower temperatures, to a minimum of 48°C, can be used for disinfestation but the treatment duration should last at least for 24 h or longer." (p.522)

解读：若 pulp/网材菌落控制走热处理路线的时间-温度参照点 `[待验证]`（食品物料数据，迁移到纤维素需自行验证）。

## Superheated Steam in Food 过热蒸汽（呼应 Ch19）

> "Superheated steam drying has been credited with the following advantages: 1. Improved drying efficiency, as much as 50% less than conventional systems; 3. No product oxidation, because there is no direct contact of hot oxygen with the product; 4. Phytosanitary; steam heat is superior to dry air in destroying all stages of insects, molds, and other microorganisms." (p.538–539)

解读："no oxidation"正是纸浆白度回变的抑制机理 — 与 [[Industrial Drying Ch19 Superheated Steam Drying]] 的纸/浆论证互为印证。

## Heat Damage by Dryer Type 干燥器类型决定热损伤

> "The loss of milk lysine in spray drying ranges from 3 to 10%, whereas in drum drying the loss ranges from 5 to 40%… In drum drying, the milk particles at medium to low moistures are in contact with the hot drum, and therefore the loss of lysine is greater." (p.540)

解读：低水分 + 热表面接触 = 最大热损伤 — 热粘合/轧光产线避免热缸长驻留、优先 through-air/低表面温度路线的教科书式论据（与 [[Industrial Drying Ch9 Drum Dryers]]、[[Industrial Drying Ch10 Industrial Spray Drying Systems]] 对照）。

## Browning Kinetics 褐变动力学 → 白度回变类比

Arrhenius: > "k = k_0 exp(−E/RT) where k_0 is the constant, E is the activation energy of the reaction, R is the gas constant, and T is the absolute temperature." (p.540); skim-milk browning model E = 90816.51 J/mol (p.542–543).

解读：Maillard 化学与纤维素水热黄变机理不同，但动力学治理（活化能、水分依赖、低温偏好）完全同构 — 可直接借用来设计白度稳定性加速老化试验（等温湿热老化 + 拟合 k(T)），代替 ad-hoc pass/fail。

## Fluid-Bed & Vacuum Constraints 流化床与真空约束

Fluid-bed 适用颗粒：平均粒径 10–20 mm、窄粒径分布、规则形状、易散开 (p.538) — 决定粉碎纤维素或颗粒 SAP 能否流化干燥的同类判据（详见 [[Industrial Drying Ch8 Fluidized Bed Dryers]]）。真空干燥产品强吸湿需密封包装、35–60 °C、"one of the most expensive methods of drying" (p.536–537)。

## Method & Limits 方法与局限

教学法推导章：从热平衡 (Eq 21.3)、水分平衡 (Eq 21.9) 到恒速 (Eq 21.10) 与降速扩散 (Eq 21.14–21.17) 的分层干燥模型，再汇编 ASAE 标准与实验数据（Tables 21.4–21.8）。诚实边界：**OCR 源文件中 Eq 21.1（BET）与 Eq 21.2（Henderson）公式乱码**，使用前必须查印刷版或 ASAE/ASABE 标准 `[待验证]`；营养损失百分比是食品化学，不得直接移植到纤维素/SAP — 只有动力学框架可迁移。

## Hygiene Implication 卫材关联

- **残余水分规格**：用 a_w ≤ 0.7 / >0.4 阈值 + GAB 把绒毛浆与芯体水分限值表达为 a_w 并换算 %wb (p.521–522)。
- **白度回变**：以 Arrhenius 框架设计加速老化，拟合 E 与 k0 而非拍脑袋判定 (p.540–543)。
- **SSD 候选名单**：评估能耗+白度时保留 SSD，引用"no oxidation/phytosanitary"作为白度回变缓解 (p.538–539)。
- **产线工艺**：低水分段避免热缸/热表面长驻留 (p.540)。
- **自由水语言**：用离子/氢键结合水分类区分芯体中驱动微生物生长的水分 (p.521)。

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch8 Fluidized Bed Dryers]]
- [[Industrial Drying Ch9 Drum Dryers]]
- [[Industrial Drying Ch10 Industrial Spray Drying Systems]]
- [[Industrial Drying Ch17 Conveyor Dryers]]
- [[Industrial Drying Ch19 Superheated Steam Drying]]

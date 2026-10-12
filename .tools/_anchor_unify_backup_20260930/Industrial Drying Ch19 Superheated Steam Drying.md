---
type: source
title: "Industrial Drying Ch19 Superheated Steam Drying"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch19.md.md"
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "SSD 净能耗为 1000–1500 kJ/kg 水，对应热风干燥为 4000–6000 kJ/kg（p.438）——前提是排汽潜热被回收利用"
  - "SSD 中无氧气：无火灾/爆炸风险，且多数产品不会形成'表面结皮'（case-hardened skin）（p.438）"
  - "蒸汽干燥纸浆纤维性能：抗张指数提升 20–30%、耐破度提升 20%、Scott 内结合强度提升 10–20%、结晶度无可测变化；高于 300 °C 时白度略差（Table 19.2, p.446）"
  - "在操作压力对应的蒸汽饱和温度下会熔融或发生玻璃化转变的产品不能用 SSD 干燥，即使只含表面水分（p.439）"
  - "尚无商业化过热蒸汽纸页直接干燥设备；Mujumdar 提出多种直接/直接-间接组合构型，卫生纸（tissue）冲击+穿透干燥（Papridryer）被认为是最临近工业化的应用（p.444–445）"
  - "纸页干燥的节能潜力随系统集成度在 15–85% 之间（p.450）"
summary_cn: "本章系统论证过热蒸汽干燥（SSD）以可回收潜热实现 3–4 倍于热风干燥的能效并消除氧化/火灾风险，蒸汽干燥可增强纸浆纤维强度而结晶度不变，但对纸页/卫生纸而言仍处于商业化前夜。"
tags: ["source/book", "drying", "superheated-steam", "pulp", "energy", "fibre-properties"]
tags_zh: ["来源/书籍", "干燥", "过热蒸汽", "纸浆", "能耗", "纤维性能"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch15 Impingement Drying]]", "[[Industrial Drying Ch17 Conveyor Dryers]]", "[[Industrial Drying Ch35 Drying of Pulp and Paper]]", "[[Industrial Drying Ch46 Energy Aspects]]", "[[Industrial Drying Ch48 Safety Aspects]]"]
---

# Chapter 19 — Superheated Steam Drying

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.19, pp.437–450.

(Arun S. Mujumdar 执笔。页码由 PDF 页 − 21 推算，锚定 Ch.1 = p.1，应与印刷版抽查核对。)

## Scope 范围与定位

Chapter 19 replaces hot air / combustion gas with superheated steam (SSD) as the convective drying medium (p.437). Because the exhaust is itself steam, its latent heat is recoverable by condensation or mechanical/thermocompression — the source of SSD's energy advantage. 卫材视角：这是绒毛浆/纸页干燥的**能耗杠杆章**，同时给出蒸汽 vs 热风对纤维性能的量化证据（★★★★★）。

## Energy Economics 能耗经济学

- > "the net energy consumption chargeable to the steam dryer can be very low… the 1000–1500 kJ/kg water removed for SSD compared with 4000–6000 kJ/kg water removed in a corresponding hot-air dryer. Thus, reduced energy consumption is a clear advantage of SSD." (p.438)
- Paper drying net energy as low as 1500 kJ/kg if exhaust fully reused, vs 4800–5700 kJ/kg for air (p.445); overall paper savings "can range from 15 to 85%" (p.450) — 依赖蒸汽汇（steam sink）的 mill 集成度，无排汽去处则优势消失 (p.437–438).
- Beet pulp: 2900 vs 5000 kJ/kg (p.441). 辅机成本（密封、排汽回收）通常高于干燥机本体，SSD "justifiable only for very large tonnage, continuously operated systems" (p.438)。

## Oxygen-Free Medium 无氧介质

> "No oxidation or combustion reactions are possible in SSD. This means no fire or explosion hazards and often also a better quality product… many products that form 'case-hardened skin' in rapid drying do not form such water-impermeable skins in SSD." (p.438)

解读：可燃网材的火灾风险（Ch.15/Ch.48 议题）消失，且不结皮意味着内部水分迁出通道不被堵死 — 与 [[Industrial Drying Ch48 Safety Aspects]] 的安全议题直接互补。

## Inversion Temperature 转化温度

Above the inversion temperature steam's higher thermal conductivity and heat capacity give faster surface-moisture removal; below it air is faster (p.438). Indirect heating lowers the inversion point 250→170 °C (p.439) — 一个可设计的热输入杠杆。转化温度概念与 [[Industrial Drying Ch15 Impingement Drying]] 的冲击干燥速率框架同一量纲。

## Polymer Limits 聚合物温度边界

> "Products that may melt, undergo glass transitions, or be otherwise damaged at the saturation temperature of steam at the dryer operating pressure cannot clearly be dried in superheated steam even if they contain only surface moisture." (p.439)

解读：1 bar 饱和 100 °C（对多数粘合剂安全）；5 bar ≈150 °C 已接近 PP 皮层熔点。对 Tg 敏感产品推荐低压 SSD (p.446)。含 SAP / 双组分纤维的网材需按此边界核算 `[待验证]`（章节未给卫材专属窗口）。

## Paper / Tissue Status 纸页与卫生纸现状

> "No commercial dryers exist for direct drying of paper webs with superheated steam. For the first time, Mujumdar proposed a variety of possible configurations for direct and direct/indirect drying of paper using superheated steam… Application to tissue drying (impingement and through drying) appears to be the more imminent industrial-scale operation." (p.444–445)

Papridryer（蒸汽冲击+穿透）= Ch.15 冲击 + Ch.17 穿透在无氧介质下的合并构型；tissue 正是 diaper 面材同源的高渗透等级。深度关联见 [[Industrial Drying Ch35 Drying of Pulp and Paper]]。

## Fibre-Property Evidence 纤维性能证据（Table 19.2, p.446）

| Property | Effect vs air drying |
|---|---|
| Burst | +20% (typical) |
| Tensile index | +20–30% improvement |
| Scott internal bond | +10–20% higher |
| Crystallinity | No measurable change |
| Brightness | Above 300 °C, a little worse |

> "Tensile index 20–30% improvement … Crystallinity No measurable change" (Table 19.2, p.446)

解读：蒸汽干燥强化纸页（无氧化断链、无结皮）而纤维素结晶结构不动；唯一代价是 >300 °C 的水热黄变。Salin 数据：蒸汽干燥木片制刨花板可省胶 9% (p.446)。对绒毛浆采购，这是"强度↑、白度需控温"的量化取舍。

## Method & Limits 方法与局限

工业综述+可行性评审（McGill 手抄纸冲击试验、芬兰中试、供应商数据），无新基础建模。诚实边界：纸页 SSD 前商业化 (p.444)；黄变机理（戊聚糖/半纤维素水解）未分析；节能区间宽（15–85%）说明高度依赖集成 `[待验证]`（对具体产线需自行建模）。

## Hygiene Implication 卫材关联

- **能耗**：绒毛浆/纸页产线评估 SSD 时以 1000–1500 kJ/kg 为基准，但必须先确认蒸汽汇存在 (p.437–438)。
- **纤维强度**：蒸汽干燥路线带来 tensile +20–30%、内结合 +10–20%（Table 19.2, p.446）；白色绒毛浆须把蒸汽温度压在 ~300 °C 以下防黄变 (p.446)。
- **安全合规**：无氧介质消除可燃网材火灾/爆炸风险 (p.438)。
- **聚合物边界**：PP/PET 皮层或 SAP 临近饱和温度时用低压 SSD (p.439, p.446) `[待验证]`。
- **现实定位**：tissue SSD 是"imminent"而非现役技术 (p.444–445) — 作为前瞻技术储备，不是当期工艺选项。

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch15 Impingement Drying]]
- [[Industrial Drying Ch17 Conveyor Dryers]]
- [[Industrial Drying Ch35 Drying of Pulp and Paper]]
- [[Industrial Drying Ch46 Energy Aspects]]
- [[Industrial Drying Ch48 Safety Aspects]]

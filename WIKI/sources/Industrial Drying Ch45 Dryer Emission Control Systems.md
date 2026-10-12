---
type: source
title: "Industrial Drying Ch45 Dryer Emission Control Systems"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch45.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Dryers are one of the major sources of atmospheric emission of dust, gases, and odors (p.1039)"
  - "Emission control equipment groups into three classes: particulate matter (PM), gaseous emissions, and odor emissions (p.1040)"
  - "Organic/odor-laden exhaust should first pass through a condenser to remove condensable VOCs, minimizing downstream load or allowing solvent recovery (p.1042)"
  - "In some drying installations the cost of emission-control equipment can exceed the dryer itself (p.1041)"
  - "Baghouses collect >99% of particles >1 µm (Table 45.2, p.1044) but require explosion-relief panels for combustible dust holdup (p.1049, p.1052)"
  - "Closed-cycle drying is recommended when flammable, toxic, or valuable solvents are used or powder-air explosion risks exist (p.1065)"
summary_cn: "系统论述干燥器粉尘/气体/气味三类排放的控制系统（旋风、布袋、湿式洗涤器）与选型设计，其冷凝器优先的VOC处理链和布袋防爆要求可直接迁移到卫材涂布与 airlaid 产线的排放合规。"
tags: ["source/book", "emission-control", "VOC", "particulate-matter", "cyclone", "baghouse", "wet-scrubber", "odor-control", "solvent-recovery", "explosion-protection", "compliance"]
tags_zh: ["排放控制", "挥发性有机物", "颗粒物", "旋风分离", "布袋除尘", "湿式洗涤", "气味控制", "溶剂回收", "防爆", "合规"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["Handbook of Industrial Drying", "Industrial Drying Ch33 Drying of Fibrous Materials", "Industrial Drying Ch40 Drying of Coated Webs", "Industrial Drying Ch46 Energy Aspects", "Industrial Drying Ch48 Safety Aspects"]
---

# Ch45: Dryer Emission Control Systems

> Source: Mujumdar (ed.), *Handbook of Industrial Drying*, 4th ed., CRC Press, 2014, Ch.45, pp.1039–1073. (Jumah & Mujumdar)

Relevance to hygiene REL absorbent-core engineering: **low-moderate** 低-中相关。The chapter is plant environmental compliance, not web physics — but its condenser-first VOC architecture, baghouse selection for combustible cellulosic/SAP fines, and achievable particulate-emission limits transfer directly to coating-oven and airlaid/defibration exhaust on hygiene converting lines. 译注：本章属于工厂环保合规内容，与卫材芯体物理无直接关系，但排放链架构与防爆除尘选型对涂布烘干和气流成网排风有直接参考价值。

---

## 1. Framing: Dryers Are a Primary Emission Source 排放源定位

> "Dryers are one of the major sources of atmospheric emission of dust, gases, and odors." (p.1039)

> "More stringent demands governing environmental aspects of the plant operations have resulted in better compliance." (p.1039)

Control targets grouped as three classes (p.1040):
1. Particulate matter (PM) 颗粒物
2. Gaseous emissions 气态排放
3. Odor emissions 气味排放

---

## 2. Condenser-First Principle 冷凝器优先原则

> "moisture-laden or organic vapor emissions should first be passed through a condenser that is capable of removing a high percentage of the water vapor or condensable volatile organic compounds (VOCs). This minimizes the odorous gas stream to be treated or allows recovery of a costly solvent." (p.1042)

Dual payoff 双重收益 (译注): (1) shrink the burden on downstream odor treatment; (2) recover the solvent as an asset. Architecture: condenser → adsorber / scrubber / oxidiser.

> "recovery of the solvent is frequently desirable in order to lower costs, prevent a safety hazard, and eliminate air pollution." (p.1040)

Pharma VOC control menu (p.1065): condensation, absorption, adsorption (activated carbon beds), thermal destruction (flares, thermal/catalytic incinerators), vapor containment. "Water- or brine-cooled condensers are the most common control devices."

---

## 3. Economics of Compliance 合规成本

> "In some drying installations, the cost of the equipment needed to comply with regulations can exceed that of the dryer itself." (p.1041)

Procurement signal 采购信号 (译注): a supplier's abatement spend reveals whether the line was designed clean from the start.

Closed-cycle drying is recommended when (p.1065):
1. Flammable, toxic, or valuable solvents are used
2. No atmospheric pollution is permitted
3. Powder–air explosion/fire risks exist

---

## 4. Particulate Control Ladder 除尘设备阶梯

Table 45.2 performance classes (p.1044):

| Device | Efficiency | Range | Caveat |
|---|---|---|---|
| Cyclone 旋风 | 50–90% | 10–100 µm | Useless below 5–10 µm; saltation limit (p.1043) |
| Fabric filter / baghouse 布袋 | >99% | >1 µm | Fire/explosion + dew-point duty |
| Wet scrubber 湿洗 | 80–99% | — | Wastewater + corrosion; venturi class reaches 99.5% at 0.5 µm |

Baghouse design numbers (p.1050–1052):
- Gas-to-cloth ratio design factor: "4 (ft³/min)/ft² of cloth area (1.2 (m³/min)/m² of cloth area)" (p.1050)
- "Collection efficiency 99 to 99.9%"; ΔP "500 to 2500 Pa"; bag life "1 to 4 y" (p.1052)
- Dennis–Klemm cake pressure drop: ΔP = S_E + k₂·c_i·V²·t (p.1051) — pressure drop dominated by cake build-up, so cleaning method and gas-to-cloth ratio govern both capture and fan power
- Explosion protection: "Baghouses must be safeguarded against dust explosions because considerable dust holdup in the baghouse can occur. Explosion panels that relieve directly … are normal features of baghouses." (p.1049, p.1052)
- Dew-point discipline: operating below dew point causes condensation; on fabric it "poses a serious fire hazard" (p.1052, p.1059)

Wet scrubber energy classes (p.1054): low energy 1–5 in H₂O (250–1250 Pa); high-energy/venturi 15–35 in H₂O (3750–8750 Pa), particles to 0.5 µm at 99.5%.

Achievable exhaust-PM limits by spray-dryer layout, Table 45.20 (p.1066):
- Open-cycle + cyclone: >250 mg/Nm³
- Bagfilter + absolute filter: 0.1–5 mg/Nm³
- Recycled systems: "Negligible"

Odor note from the detergent survey (p.1063): "The main atmospheric pollution problem in soap manufacturing is odor", controlled by "scrubbing with an acid solution"; surfactant organics "vaporized in the spray dryer … condense in the tower exhaust air stream into droplets", giving "a highly visible plume".

---

## 5. Method & Limitations 方法与局限

Review/design-survey chapter built on equipment handbooks, EPA AP-42 emission factors, and vendor bulletins; design equations embedded (cyclone grade-efficiency models, Dennis–Klemm baghouse correlations, scrubber penetration models). Limitations 局限 (译注):
- 2006-vintage review; "emission standards are different in different countries" (p.1056) — AP-42 factors are US-centric, must re-anchor to local jurisdiction
- Dust-specific constants (S_E, k₂) need experimental fitting; provided defaults are for woven glass/flyash (p.1051)
- Equation blocks partially OCR-degraded (p.1043, p.1051) — formulas cannot be used verbatim
- No odor-threshold data, no VOC-species inventory, no hygiene-substrate treatment

---

## 6. Hygiene Implication 卫材关联

Moderate-low but specific transfer points 可迁移点 (译注):

1. **Coating-oven VOC train**: condenser-first architecture (p.1042) plus the pharma control menu (p.1065) is the template for lotion/adhesive/fragrance dryer exhaust — audit suppliers for the abatement flow diagram and whether solvent is recovered or destroyed (p.1040).
2. **Airlaid / fluff-defibration dust**: fine cellulosic + SAP fines are combustible; the chapter's own logic points to baghouses with explosion-relief panels, grounded cloth, spark arrestor, and dew-point margin above the exhaust (p.1049, p.1052, p.1059).
3. **Contractual PM limits**: Table 45.20 classes (p.1066) convert exhaust dust into an enforceable spec, e.g. ≤20 mg/Nm³ for a bag-filtered line.
4. **Odor chemistry**: acid-scrubbing precedent for surfactant/fragrance plumes (p.1063) applies to fragranced webs.
5. Combustible-dust safety detail intersects [[Industrial Drying Ch48 Safety Aspects]]; energy cost of abatement airflow intersects [[Industrial Drying Ch46 Energy Aspects]].

---

## 7. Related Sources 关联来源

- [[Handbook of Industrial Drying]] — Full book index
- [[Industrial Drying Ch48 Safety Aspects]] — Combustible-dust and fire safety duty
- [[Industrial Drying Ch46 Energy Aspects]] — Energy cost of abatement airflow and heat recovery
- [[Industrial Drying Ch40 Drying of Coated Webs]] — Coated-web drying where VOC/odor originates
- [[Industrial Drying Ch33 Drying of Fibrous Materials]] — Fibre fines source in through-air drying

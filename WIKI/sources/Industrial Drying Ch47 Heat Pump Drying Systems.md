---
type: source
title: "Industrial Drying Ch47 Heat Pump Drying Systems"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch47.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Heat pump dryer advantages emerge from recovering energy from exhaust gas and controlling drying-gas temperature and humidity (p.1101)"
  - "Table 47.1: heat pump SMER 1.0–4.0 kg water/kWh and drying efficiency 95%, vs hot-air drying 0.12–1.28 kg/kWh and 35–40% (p.1107)"
  - "Actual heat pump efficiency is usually 40–50% of theoretical Carnot efficiency (p.1104)"
  - "HPD operating range is –20°C to 100°C (with auxiliary heating) at relative humidity 15–80% (p.1104)"
  - "Intermittent/cyclic temperature profiles save 25–61% drying time depending on cycle fraction (p.1111)"
  - "Heat pump dryers can reduce operating cost up to 70% vs a recuperative dryer, with payback of 2–3 years for a 200 kg/h unit (p.1126)"
summary_cn: "热泵干燥凭排气潜热回收与低温精确控温控湿实现 SMER 1.0–4.0 kg/kWh、干燥效率95%，运行成本最多降70%、回收期2–3年，是热敏性卫材基材低温烘干的候选路线。"
tags: ["source/book", "heat-pump-drying", "SMER", "COP", "Carnot", "energy-recovery", "low-temperature-drying", "intermittent-drying", "refrigerant", "payback"]
tags_zh: ["热泵干燥", "单位除湿能耗", "性能系数", "卡诺极限", "能量回收", "低温干燥", "间歇干燥", "制冷剂", "投资回收期"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["Handbook of Industrial Drying", "Industrial Drying Ch46 Energy Aspects", "Industrial Drying Ch48 Safety Aspects", "Industrial Drying Ch49 Control of Industrial Dryers", "Industrial Drying Ch53 Cost Estimation"]
---

# Ch47: Heat Pump Drying Systems

> Source: Mujumdar (ed.), *Handbook of Industrial Drying*, 4th ed., CRC Press, 2014, Ch.47, pp.1097–1130. (Chou & Chua)

Relevance to hygiene REL absorbent-core engineering: **moderate** 中等相关。Not web physics, but the energy/SMER benchmarks and the low-temperature (10–65°C) band are the reference points for heat-sensitive hygiene webs (lotion, actives, SAP) in low-airflow ovens. 译注：本章与芯体物理无关，但其能效基准与低温干燥区间是含 lotion/活性物卫材网低风量烘干的直接参照。

---

## 1. The HPD Thesis 热泵干燥核心主张

> "The principal advantages of heat pump dryers emerge from the ability of the heat pumps to recover energy from the exhaust gas as well as their ability to control the drying gas temperature and humidity." (p.1101)

Mechanism 机理 (译注): evaporator dehumidifies the exhaust; condenser returns the recovered latent heat to the incoming air — closing the energy loop that a convective dryer vents away.

Caveat 适用边界: HPD is not suited for dryers needing large air volumes (flash/spray, p.1102). Applies to low-airflow ovens only.

---

## 2. Headline Performance Comparison 关键性能对比

Table 47.1 (p.1107):

| Parameter | Hot Air Drying | Vacuum Drying | Heat Pump Drying |
|---|---|---|---|
| SMER (kg water/kWh) | 0.12–1.28 | 0.72–1.2 | **1.0–4.0** |
| Drying efficiency (%) | 35–40 | 70 | **95** |
| Operating temperature (°C) | 40–90 | 30–60 | **10–65** |
| Capital cost | Low | High | Moderate |
| Running cost | High | Very high | **Low** |

> "Drying efficiency(%) … Heat Pump 95" (p.1107) — HPD recovers enough latent heat to reach 95% drying efficiency versus 35–40% for hot air.

Cross-check with [[Industrial Drying Ch46 Energy Aspects]]: convective norm 0.5–1 kg/kWh, typical heat-pump value ~3 kg/kWh — consistent with Table 47.1.

---

## 3. COP Reality Check COP 现实折扣

Definitions (p.1104):
- COP = useful heat output / power input (Eq 47.1)
- COP_carnot = T_condenser / (T_condenser − T_evaporator) (Eq 47.2)
- SMER = water evaporated / energy input (kg/kWh) (Eq 47.3)

> "In practice, the actual efficiency of the heat pump is usually 40 to 50% of the theoretical Carnot efficiency (Geeraert, 1976; Strumiłło and Zyłła, 1985)." (p.1104)

Procurement rule 采购规则 (译注): discount any vendor COP claim by ~50% and rank bids on SMER instead.

---

## 4. Low-Temperature Quality Regime 低温质量区间

> "Heat pump dryers can significantly improve product quality by drying at low temperatures. At low temperatures, the drying potential of the air can be maintained by further reduction of the air humidity." (p.1104)

Operating window (p.1104): –20 to 100°C with auxiliary heating; RH 15–80%.

Time-varying operation 时变运行: fixed conditions are sub-optimal because material properties shift as moisture leaves (p.1110). Intermittent profiles — "employing intermittent temperature drying profile can result in saving drying time by about 25, 48 and 61% for a 1/4, a 1/2, and a 2/3" cycle fraction (p.1111). Real-time control (thermovision + PID) holds surface temperature below thresholds that trigger heat-induced degradation (§47.9.6).

Two-stage and multi-chamber: two-stage HPD gives "significant improvement in the heat pump energy efficiency from a single to two-stage dryer" (Fig 47.9, p.1108); one HP serving multiple chambers sequentially cuts capital while running near-optimal (p.1128).

---

## 5. Economics 经济性

> "heat pump dryers can reduce the operating cost as much as 70% in comparison to a recuperative heating dryer. … a heat pump dryer designed for a drying capacity of 200 kg/h has a payback period of 2 to 3 y." (p.1126)

Payback shortens as exhaust humidity rises: 3.2 → 2.0 y when exhaust RH goes 0.4 → 0.7 — more recoverable moisture = faster payback. Capital evaluation method pairs with [[Industrial Drying Ch53 Cost Estimation]].

Refrigerants (p.1123–1124): CFC/HCFC phase-out creates selection risk; natural fluids (ammonia R717, propane R290, CO₂, steam/air) endorsed, ammonia favourable at 30–80°C.

---

## 6. Method & Limitations 方法与局限

Synthesis of refrigeration theory plus experimental HPD studies (Chou/Chua/Hawlader/Mujumdar group; Alves-Filho & Strømmen) and economic analyses (Zylla et al. 1982; Pendyalala et al. 1986). Limitations 局限 (译注):
- Eq 47.4 (SEC–COP relation) OCR-scrambled (p.1105) — only Eqs 47.1–47.3 usable
- All performance data are food/marine/timber; no lotion/SAP/nonwoven-web HPD data — hygiene transfer is by analogy [待验证]
- Capital cost higher than convection (p.1106); excludes high-airflow dryers (p.1102)

---

## 7. Hygiene Implication 卫材关联

Moderate 中等相关 (译注):
1. **Low-temp route for sensitive webs**: the 10–65°C band (Table 47.1) is the candidate regime for lotion-laden or actives-bearing webs where convection at 40–90°C risks thermal degradation — though no hygiene-web data exists, so transfer is by analogy.
2. **Benchmark bids on SMER**: require SMER statements and compare against convective 0.5–1 kg/kWh; treat COP claims with the 40–50%-of-Carnot discount (p.1104).
3. **Payback model**: use the 70% OPEX / 2–3 y payback frame and the exhaust-RH sensitivity (p.1126) when evaluating a retrofit; more recoverable moisture favours HPD.
4. **Intermittent schedules**: 25–61% time savings (p.1111) suggest cyclic temperature profiles as a quality + energy lever on coated webs.
5. Safety co-benefit: low-temperature drying also reduces fire/explosion duty — intersects [[Industrial Drying Ch48 Safety Aspects]]; control loops foreshadow [[Industrial Drying Ch49 Control of Industrial Dryers]].

---

## 8. Related Sources 关联来源

- [[Handbook of Industrial Drying]] — Full book index
- [[Industrial Drying Ch46 Energy Aspects]] — Convective SMER 0.5–1 vs HPD benchmarks
- [[Industrial Drying Ch53 Cost Estimation]] — Capital/payback methodology
- [[Industrial Drying Ch48 Safety Aspects]] — Low-temp drying reduces fire/explosion duty
- [[Industrial Drying Ch49 Control of Industrial Dryers]] — Control loops for intermittent schedules

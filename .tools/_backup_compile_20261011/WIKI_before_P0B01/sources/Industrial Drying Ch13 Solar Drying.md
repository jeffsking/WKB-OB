---
type: source
title: "Industrial Drying Ch13 Solar Drying"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch13.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Solar drying is the utilization of solar energy for the removal of moisture from solids; an old method of preservation of agricultural products but a relatively new field of technical development (p.305)."
  - "Inherent limitations include high labor costs, large area requirement, lack of control; the low energy density of solar radiation requires the use of large energy-collecting surfaces (p.306)."
  - "Economic evaluation of solar dryers usually aims at determining the payback time; the dynamic method takes the influence of inflation into consideration (p.319)."
  - "Some significantly good payback times (1–7 years) have been achieved, mainly with simple and cheap dryers (p.353)."
  - "Solar dryers of high performance or for drying of quality-sensitive materials should be well directed; higher investment and maintenance costs can be balanced by better dried-product quality and longer annual operation time (p.341)."
  - "Recirculation to hold constant inlet air temperature is possible only as a precondition that the atmospheric air be of lower absolute water content than the outlet air (p.350)."
summary_cn: "太阳能干燥章节把不可调度、低能流密度的太阳辐射作为最坏边界条件，建立收集器效率（Hottel–Whillier–Bliss）、热储能解耦、MFN/HFN网络仿真与PID/h-x图调控的完整工程方法，结论是经济性取决于D/C动态回收期（1–7年回收主要靠简单廉价干燥器）——方法学可迁移，但对卫材工艺实质关联很低。"
tags: ["source/book", "drying/solar", "intermittent-drying", "heat-storage", "payback-economics", "process-control"]
tags_zh: ["太阳能干燥", "间歇干燥", "热储能", "回收期经济性", "过程控制", "收集器效率"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch15 Impingement Drying]]", "[[Industrial Drying Ch17 Conveyor Dryers]]", "[[Industrial Drying Ch46 Energy Aspects]]"]
---

# Solar Drying (Ch.13)

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.13, pp.305–360 (László Imre).

## Chapter Overview 章节概览

Chapter 13 treats solar drying as an energy-system chapter: engineering dryers around intermittent, low-flux, non-dispatchable irradiation. Logic: limitations → construction principles (three dryer classes) → economics (dynamic payback) → key elements (collectors, heat storage) → simulation methodology (mass-flow network MFN + heat-flow network HFN) → direction/control strategy → prospects. Its intellectual center is not a drying mechanism but matching a stochastic, low-density heat source to a batch load via collectors, storage, recirculation, and PID control.

> Note: page numbers derived from PDF-page − 21; spot-check against print edition.

## Key Viewpoints 关键观点

### 1. Definition and limitations 定义与局限

> "Solar drying is the utilization of solar energy for the removal of moisture from solids. It is an old method of preservation of agricultural products but a relatively new field of technical development." (p.305)

> "Among these are high labor costs, large area requirement, lack of control. Another problem is caused by the low energy density of solar radiation, which requires the use of large energy-collecting surfaces (collectors)." (p.306)

### 2. Economics is a D/C payback problem 经济性是D/C回收期问题

> "Economic evaluation of solar dryers usually aims at determining the payback time. The dynamic method of calculations takes the influence of inflation into consideration." (p.319)

> "Some significantly good payback times (1–7 years) have been achieved [14,17,133], mainly with simple and cheap dryers." (p.353)

The economic case rests on low capital cost, not collector sophistication.

### 3. Collector efficiency trade-off 收集器效率权衡

η = Fᵣ[τα − Uₗ(T_in − T_o)/I] (Eq. 13.15, p.325); "The coefficient Fᵣ takes into consideration the relative decrease of efficiency caused by the increase of absorber mean temperature compared with T_in." (p.325)

A collector's useful efficiency falls linearly with (T_in − T_o)/I — a direct efficiency–temperature trade-off present in every convective air heater.

### 4. Energy effectiveness via recirculation and intermittency 有效能与再循环

> "The energy effectiveness of solar dryers depends also on the exit energy losses, which can be reduced by applying a proper direction and control." (p.339)

Regulating recirculation of the air and regulating the intermittent drying process (determining the beginning and the interval) are the two levers (p.340). Recirculation precondition: "point 0 … should be of lower absolute water content than that of the outlet air" (p.350).

### 5. Quality-led direction 质量导向调控

> "Solar dryers of high performance or for drying of quality-sensitive materials should be well directed. The higher investment and maintenance costs can be balanced by the better quality of the dried product and by the longer annual operation time." (p.341)

### 6. Control-mode selection by time window 控制模式选择

"PI controllers can be applied with t_c > 6·t₁. PID controllers are recommended in the range of 4·t₁ < t_c < 6·t₁." (p.349) — controller class chosen by the permitted control-time window.

## Key Terms & Process Details 关键术语

- Dryer classes: solar natural dryer (passive, no fan; cabinet/tent/shelf/chimney, p.310); semiartificial solar dryer (forced air, solar-only heat, physical heat storage, p.312); solar-assisted artificial dryer (solar + auxiliary/fossil/heat-pump backup, p.315).
- Heat storage: sensible (rock-bed, water tank), latent (PCM: Na₂SO₄·10H₂O, CaCl₂·6H₂O, paraffin), sorptive (adsorption); 3–5 operating modes selected by microprocessor from T and U sensors (p.351–352).
- MFN/HFN: mass-flow network + heat-flow network discrete-time simulation (p.335), validated against alfalfa drying curves (Fig. 13.36).
- Mixing point M: h–x node where fresh and recirculated air mix; b/a ratio variation holds inlet temperature (p.350).
- Quantitative datum: chimney dryer for 1000-kg rice — 0.1-m static bed, 5-m chimney, ≈5.7 m³/min per m³ rice, non-uniform bed requiring turning (p.311).

## Strengths & Weaknesses 优劣评估

- Strengths: unusually complete control/direction treatment (h–x logic, recirculation, PID); inflation-aware dynamic payback method; reusable, data-validated MFN/HFN simulation; taxonomy spans natural → semiartificial → solar-assisted.
- Weaknesses: heavy OCR degradation — several equations garbled [待验证 against print]; evidence base almost entirely agricultural/forest products, no fibre/web/polymer processing; PCM and adsorption storage named but not deeply simulated; D/C heuristic underweights fan electricity.

## Hygiene Implication 卫材关联

Relevance: ★☆☆☆☆ — plainly low: solar drying does not appear in tissue, airlaid, or SAP process trains, and none of its failure modes map onto tissue curl, brightness reversion, or SAP integrity. Do not cite Ch.13 for fibre-damage, curl, brightness, residual-moisture, or web-defect mechanisms. Only methodological cross-links hold:

- Storage-decoupling template: if piloting low-grade thermal recovery on a hygiene line (exhaust-air heat wheels, warm-water buffers feeding a thermobond oven), the rock-bed/water-tank operating-mode logic (p.351) is a direct template for dispatchable-vs-stored energy switching.
- Payback discipline: justify capital dryer upgrades (impingement hood, IR cure, through-air oven) with the D/C + dynamic-payback method (p.319) rather than peak-efficiency claims.
- Generic control rule: PID selection by control-time window (p.349) applies to any dryer temperature/flow loop on a converting line.
- Efficiency–temperature trade-off: Eq. 13.15's logic applies to combustion air heaters on Yankee/thermobond lines — raising supply-air temperature lowers heater efficiency (p.325).

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch15 Impingement Drying]]
- [[Industrial Drying Ch17 Conveyor Dryers]]
- [[Industrial Drying Ch46 Energy Aspects]]

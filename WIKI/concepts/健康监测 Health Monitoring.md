---
type: concept
title: "健康监测 Health Monitoring"
domain: [卫材研发, 变色与智能材料]
status: growing
updated: 2026-09-30
tags: [health-monitoring, wearable-sensor, wetness-indicator, skin-health, absorbent-article-sensing]
---

# 健康监测 Health Monitoring

> 📌 **Page completed 2026-09-30** from 11 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）。

The vault records health monitoring only as a **cross-over point of the wearable-sensor reference**, never as a defined function: the cited source lists its hygiene intersection as **健康监测传感（心率 / 体温 / 活动量）、智能包装传感、湿感指示条**（源：[[Wearable Sensors Fundamentals Implementation and Applications]]、[[可穿戴传感器 Wearable Sensor]]）.

（中文：库内没有"健康监测"的定义句；它只作为可穿戴传感器参考书第五章的**卫材交叉点**出现——心率、体温、活动量三类信号 + 智能包装 + 湿感指示。）

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Cited reference（被引专著） | Sazonov & Neuman (eds.), *Wearable Sensors: Fundamentals, Implementation and Applications*, **CRC Press 2015, ISBN 978-1-4665-7154-9** | [[Wearable Sensors Fundamentals Implementation and Applications]] |
| Monitored signals（监测信号） | heart rate / body temperature / activity（心率 / 体温 / 活动量） | [[Wearable Sensors Fundamentals Implementation and Applications]] |
| Non-electronic read-out window（非电子目视指示） | removable **thermochromic** sensor read through an outer-surface window; claim window **~99.5–102 °F** | [[US8273939 Windowed Removable Sensor Absorbent Article]] |
| Quantified hygiene implementation | **none recorded** — no e-textile hygiene-product data, no cost or lifetime figure at disposable scale | [[电子纺织品 E-textile]] |

## Method / Mechanism 方法 / 机理

1. **Two read-out architectures are distinguished in the vault.**
   - **Electronic / wearable-sensor route** — sensor integrated into a garment, textile or substrate worn on the body, monitoring a physiological or environmental signal（源：[[可穿戴传感器 Wearable Sensor]]）.
   - **Non-electronic chromic route** — P&G **US8273939**: a **window** in the article's outer surface lets a **removable thermochromic sensor** be read from outside; the source characterises it as a **battery-free, circuit-free visual readout**, i.e. the same value proposition as a chromic wetness/comfort indicator（源：[[US8273939 Windowed Removable Sensor Absorbent Article]]）.
2. **Two hygiene integration positions**：(1) **in-article sensor** — a windowed, removable sensor in the absorbent article itself (e.g. P&G US8273939B2); (2) **separate detection garment** worn outside the article (e.g. K-C US11013641B2). Stated pain point: caregiver burden（源：[[可穿戴传感器 Wearable Sensor]]）. The K-C garment route is carried in the vault as [[US11013641 Garment for Detecting Absorbent Article Leakage]] — a **resistive sensing** scheme: in the dry state the reading is ≈ full-scale, and when exudate wets the path the measured potential collapses（源：[[导电纱线 Conductive Yarn]]）.
3. **Reversibility decides whether monitoring is even possible.** Continuous monitoring requires a **reversible** chromic route; a single alarm may use a semi-reversible or irreversible one — *"this is the axis that eliminates designs, not the chemistry family"*（源：[[Chromism Taxonomy（变色现象分类）]]）.
4. **Wet-state visualisation as the practical hygiene read-out**：an internal review covers 湿态可视化（**Video Q**，接触水 / 尿液后显图案）alongside botanical-extract actives and tri-zone lotion（源：[[Botanical Extract Efficacy, Wetness Visualisation & Tri-Zone Lotion Review（植物提取物功效测试与验证）]]）.
5. **Sensing as reassurance, not diagnostics**：the odour programme names a **Perception 感知** route — a *"sensorial reassurance cue"*, i.e. a dual track of **technical fix + emotional fix**（源：[[Odour Management Routes（气味管理技术路线）]]）.

## Hygiene Relevance 卫材关联

- **The need being monitored is skin health.** In the intake-workshop frame, **Rash-Free Skin Health is the #1 Unmet Need**, and the three unmet-need spaces rank **1 Prevent Rash & Irritation → 2 Strengthen & Nurture → 3 Treat & Restore**（源：[[Global Overview - Intake Workshop（摄入系统研讨会·全球品牌与区域概览）]]）.
- **The gap between need and measurable endpoint is explicit.** The vault states *"rash-free skin health is the world's #1 unmet need"* is a **demand judgement, not an acceptance criterion**; converting it requires **clinically measurable endpoints** — listed as an opportunity but **no method is given**（源：[[Intake System（摄入系统）]]）.
- **Regulatory consequence of a health claim**：*"Depending on technology, claim, + intent of use, FDA may consider product with skin health treatments as an OTC Drug or Cosmetic"*（源：[[Intake Systems Tech Pipeline - Archive（摄入系统技术管线·汇编存档）]]）.
- **Differentiation lever**：DSU differentiation via **skin-health additives**, with DPU upgrade judged *"unlikely to use skin health additives"*（源：[[Liner Differentiation Discussion v2（面层分层与产品档位差异化讨论）]]）.
- **Adjacent vault pages**：[[智能包装 Smart Packaging]]、[[湿感指示条 Wetness Indicator]]、[[Skin Health Treatment on Nonwoven（无纺布护肤处理）]]（源：[[Wearable Sensors Fundamentals Implementation and Applications]]）.

## Open Questions 待补

- **No hygiene-product sensor spec**（sensitivity, drift, lifetime, power budget, cost）exists anywhere in the digest（源：[[可穿戴传感器 Wearable Sensor]]）.
- **e-textile → health-monitoring transfer is unquantified**：the vault records only conceptual adjacency（源：[[电子纺织品 E-textile]]）.
- **No clinically measured skin-health endpoint is defined**（源：[[Intake System（摄入系统）]]）.
- **Recyclability / e-waste conflict with single-use hygiene** is flagged but unresolved（源：[[可穿戴传感器 Wearable Sensor]]）.
- Windowed-sensor patent **freedom-to-operate not assessed**（源：[[US8273939 Windowed Removable Sensor Absorbent Article]]）.

## Related Sources 关联来源

- [[Wearable Sensors Fundamentals Implementation and Applications]]（本页原始 Cited-by 来源）
- [[可穿戴传感器 Wearable Sensor]] · [[电子纺织品 E-textile]] · [[智能包装 Smart Packaging]] · [[湿感指示条 Wetness Indicator]]
- [[US8273939 Windowed Removable Sensor Absorbent Article]] · [[US11013641 Garment for Detecting Absorbent Article Leakage]] · [[导电纱线 Conductive Yarn]] · [[Chromism Taxonomy（变色现象分类）]]
- [[Global Overview - Intake Workshop（摄入系统研讨会·全球品牌与区域概览）]] · [[Intake System（摄入系统）]]
- [[Botanical Extract Efficacy, Wetness Visualisation & Tri-Zone Lotion Review（植物提取物功效测试与验证）]] · [[Odour Management Routes（气味管理技术路线）]]
- [[Intake Systems Tech Pipeline - Archive（摄入系统技术管线·汇编存档）]] · [[Liner Differentiation Discussion v2（面层分层与产品档位差异化讨论）]]

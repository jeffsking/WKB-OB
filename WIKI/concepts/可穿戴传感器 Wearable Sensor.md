---
type: concept
title: "可穿戴传感器 Wearable Sensor"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [wearable, sensor, e-textile, flexible-electronics, hygiene-sensing, wetness-indicator, pressure-sensing]
---

# 可穿戴传感器 Wearable Sensor

> 📌 **Page completed 2026-09-30** from 7 citing sources in the vault. All figures traced to their source pages. Anything not evidenced in the vault is marked `[待补]`.

## Definition 定义

**可穿戴传感器（wearable sensor）** is a sensing function **integrated into a garment, textile or substrate worn on the body**, used to monitor a physiological or environmental signal. The vault frames the field as **wearable electronics**, "a cross-disciplinary field of chemistry / physics / materials science & engineering / electrical engineering / biomedical engineering" with two mainstream directions — **thin-film devices** (reduce one dimension) and **fibre-form devices**（纤维形态，further reduce two dimensions, weavable into breathable textiles that can be **washed hundreds of times**）（源：[[Wearable Electronics (National Science Review 2023)]]）. In the textile literature the carrier is the garment itself — **textiles and clothing as "meta-wearables"** — and the hygiene cross-points are named as **health monitoring (heart rate / temperature / activity), smart packaging and wetness indicators**（源：[[Wearable Sensors Fundamentals Implementation and Applications]]）.

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Two directions 两大方向 | thin-film（减一维，最佳柔性）vs fibre-form（减两维，可织入透气纺织品） | [[Wearable Electronics (National Science Review 2023)]] |
| Fibre-form washability 纤维形态可水洗性 | **hundreds of times**（如普通衣物） | [[Wearable Electronics (National Science Review 2023)]] |
| NSR special-issue scope 特刊构成 | 10 papers: 4 perspective, 1 research, 4 review, 1 interview | [[Wearable Electronics (National Science Review 2023)]] |
| Textile taxonomy 智能纺织品分级 | passive（sense）/ active（sense+respond）/ ultra-smart（sense+respond+adapt） | [[Smart Textiles Review]] |
| Implementation routes 实现路径 | inherent fabric conductivity / post-fabrication circuit attachment / hybrid | [[Smart Textiles Review]] |
| Main manufacturing methods 主要制法 | conductive yarns（weave/knit/embroider/laminate/stitch）、printing（screen/inkjet）、component interconnect | [[Smart Textiles Review]] |
| Hygiene sensor cross-points 卫材传感交叉点 | health monitoring（心率/体温/活动量）、smart packaging、wetness indicator | [[Wearable Sensors Fundamentals Implementation and Applications]] |
| Smart-textiles market 市场口径 | CAGR ~25%（2021–2031）→ US$23.82 Bn by 2031；hygiene ≈ **50%** of medical-textiles market | [[Smart Textiles Review]] |
| Skin-contact pressure sensing 皮肤接触压力测试 | 气囊式传感器 + 主机记录仪；稳定读数 **×10**，单位 V（SOP WI-65030） | [[Pressure Sensory Test（压力触感测试）]] |
| Smart-diaper IoT monitoring dims 智能尿裤监测维度 | 湿度 / 温度 / 尿量（源页标注为 Workshop 材料口径 `[待验证]`） | [[Sensor-Equipped Absorbent Article（含传感器吸收性物品）]] |

## Method / Mechanism 方法 / 机理

- **Core components & stimuli.** Smart textiles are built from **sensors, actuators and control units**; external stimuli are mechanical, thermal, magnetic, chemical and electrical（源：[[Smart Textiles Review]]）.
- **Two hygiene integration positions.** (1) **In-article sensor** — a windowed, removable sensor in the absorbent article itself (e.g. P&G US8273939B2); (2) **separate detection garment** — an independent garment worn outside the article (e.g. K-C US11013641B2). The stated pain point: caregivers cannot readily detect leakage/wetness; sensing turns "passive discovery" into "active alert"（源：[[Sensor-Equipped Absorbent Article（含传感器吸收性物品）]]）.
- **Electronic vs passive-material sensing.** The sensing branch is electronic/structural or window-observation based and differs from chromic indicators; the two are positioned as **alternatives** (active electronic sensing vs passive material sensing)（源：[[Sensor-Equipped Absorbent Article（含传感器吸收性物品）]]）.
- **One transferable architectural idea from flexible electronics.** Rigid functional islands connected by compliant geometry and embedded in a soft elastomer — the same strain-management principle behind elastic-thread / elastic-laminate design（源：[[Flexible and Stretchable Electronics]]）.
- **Pressure sensing chain.** An air-bag sensor + multi-channel host logger converts local pressure to a voltage reading (stable reading **×10**, unit V); elastic samples are normalised by 松弛长度 =  circumference ÷ stretch ratio（源：[[Pressure Sensory Test（压力触感测试）]]）.

## Hygiene Relevance 卫材关联

- **The main deployment battleground.** Hygiene products are ≈ **50% of the global medical-textiles market**, and "the most important feature is comfort" — the decisive acceptance factor for any wearable function（源：[[Smart Textiles Review]]）.
- **Direct hygiene sensing routes** in the vault: windowed removable sensor (P&G) and leakage-detection garment (K-C)（源：[[Sensor-Equipped Absorbent Article（含传感器吸收性物品）]]）；plus the smart-diaper IoT parameter pack（湿/温/尿量）（源：[[Sensor-Equipped Absorbent Article（含传感器吸收性物品）]]）.
- **Comfort quantification.** The Pressure Sensory Test (WI-65030) is the vault's method for turning "fit/comfort" into a measurable skin-contact pressure（源：[[Pressure Sensory Test（压力触感测试）]]）.
- **Six core challenges flagged before deployment:** textile–electronics incompatibility, lack of regulations/standards, washability, recyclability, scale-up, and biocompatibility & comfort（源：[[Smart Textiles Review]]）.

## Open Questions 待补

- **No source read here integrates a wearable sensor into a disposable hygiene core with validated detection accuracy, power budget or cost** `[待补]`.
- The wearable-electronics market and hardware figures are field-level; no hygiene-product-specific sensor spec (sensitivity, drift, lifetime) is present `[待补]`.
- Recyclability / e-waste conflict with single-use hygiene is flagged as a structural obstacle but unresolved `[待补]`.
- Freedom-to-operate of the cited sensor patents is **not** assessed（源：[[Sensor-Equipped Absorbent Article（含传感器吸收性物品）]]）`[待补]`.

## Related Sources 关联来源

- [[Wearable Electronics (National Science Review 2023)]] — two directions (thin-film / fibre-form); washability
- [[Wearable Sensors Fundamentals Implementation and Applications]] — "meta-wearable" textiles; hygiene cross-points
- [[Smart Textiles Review]] — passive/active/ultra-smart taxonomy; routes; market; six challenges
- [[Smart Textiles & Wearables]] — parent collection index for the smart-textiles / wearables knowledge set
- [[Sensor-Equipped Absorbent Article（含传感器吸收性物品）]] — in-article sensor vs separate detection garment; hygiene sensing
- [[Pressure Sensory Test（压力触感测试）]] — skin-contact pressure via air-bag sensor (WI-65030)
- [[Flexible and Stretchable Electronics]] — rigid-islands-in-elastomer architectural idea
- 相关概念：[[电子纺织品 E-textile]]、[[湿感指示条 Wetness Indicator]]、[[智能织物 Smart Textile]]、[[US8273939B2 Disposable Absorbent Articles Having a Windowed Removable Sensor (P&G)]]、[[US11013641 Garment for Detecting Absorbent Article Leakage]]、[[Smart Fabric Textiles Recent Advances and Challenges]]、[[Smart Fabrics and Networked Clothing]]、[[Smart Textiles and Their Applications]]、[[导电纱线 Conductive Yarn]]

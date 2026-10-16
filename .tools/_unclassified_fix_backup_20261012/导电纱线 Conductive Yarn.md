---
type: concept
title: "导电纱线 Conductive Yarn"
domain: [卫材研发, 待归类]
status: growing
updated: 2026-09-30
tags: [conductive-yarn, e-textile, conductive-thread, silver-plated, resistive-sensing, wetness-detection, CNT]
---

# 导电纱线 Conductive Yarn

> 📌 **Page completed 2026-09-30** from 6 citing sources in the vault. All figures traced to their source pages. Anything not evidenced in the vault is marked `[待补]`.

## Definition 定义

**导电纱线（conductive yarn）** is a yarn that carries an electrical function — used in e-textiles as **wiring and/or as the sensing transducer**. In the vault's one hygiene-grade application it is the **conductive element of an electronic wetness-detection system**: the conductive materials listed are **conductive threads, conductive tape, conductive rubber, conductive wires**, with the preferred element being a **silver-plated conductive thread at 60 ohms/meter**（源：[[US11013641 Garment for Detecting Absorbent Article Leakage]]）. In the textile literature, conductive yarn is one of the main implementation routes for smart textiles（weave / knit / embroider / laminate / stitch）（源：[[Smart Textiles Review]]）.

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Conductive element forms 导电元件形态 | conductive threads / conductive tape / conductive rubber / conductive wires | [[US11013641 Garment for Detecting Absorbent Article Leakage]] |
| Preferred conductive thread 优选导电纱 | silver-plated conductive thread at **60 ohms/meter** | [[US11013641 Garment for Detecting Absorbent Article Leakage]] |
| Exemplar thread 示例牌号 | Shieldex® 110/34 dtex 2 ply HC Premium Line；polyamide 6.6 trilobal filament，**99% silver plating** | [[US11013641 Garment for Detecting Absorbent Article Leakage]] |
| Drive voltage 驱动电压 | **3.3 VDC** applied across the conductive thread | [[US11013641 Garment for Detecting Absorbent Article Leakage]] |
| Read-out 读出 | dry ≈ full-scale 3.3 V；wet voltage drops significantly（导电通道被液体桥接/加载） | [[US11013641 Garment for Detecting Absorbent Article Leakage]] |
| Conductive-yarn resistivity range 电阻率跨度 | **0.5 Ω/m to several kΩ/m** | [[Smart Textiles Review]] |
| Conductive-yarn manufacturing 制法 | weave / knit / embroider / laminate / stitch | [[Smart Textiles Review]] |
| Antistatic fibre routes 抗静电纤维三路线 | chemical modification / physical blending / conductive particles（carbon, metal or metal-oxide powders） | [[Manufactured Fibre Technology Ch14 Speciality Polyamide and Polyester Yarns]] |
| Conductive-particle caveat 导电粒子注意 | needs **conjugated bicomponent filament spinning** to retain strength；chemical bonding gives best wash durability, physical blending the worst（p. 374–377） | [[Manufactured Fibre Technology Ch14 Speciality Polyamide and Polyester Yarns]] |
| Conductive polymer (polyacetylene) 导电聚合物 | after halogen **doping** ~**10³ S/m（1 S/cm）**；doping raised conductivity **10⁹×**（Shirakawa/MacDiarmid/Heeger, 1977） | [[Seymour Polymer Chemistry Ch18 Special Topics]] |
| CNT fibre properties CNT 纤维 | elastic modulus **>1 TPa**；thermal conductivity **~2× diamond**；current capacity **1,000× copper wire**；single-walled strength **10–100× steel**（at a fraction of the weight） | [[Smart Fabrics and Networked Clothing]] |

## Method / Mechanism 方法 / 机理

- **Resistive (conductive) sensing.** A controller applies voltage across a conductive thread and monitors the voltage at its ends; in the dry state the reading is ≈ full-scale, and when exudate wets the path the measured potential collapses（源：[[US11013641 Garment for Detecting Absorbent Article Leakage]]）.
- **How fibres are made conductive.** Synthetic fibres are poor conductors and build up electrostatic charge (p. 374); three routes are named — **chemical modification, physical blending, and adding conductive particles** (carbon, metal or metal-oxide powders). Wash durability ranks chemical bonding best and physical blending worst, and conductive particles need **conjugated bicomponent filament spinning** to keep strength（源：[[Manufactured Fibre Technology Ch14 Speciality Polyamide and Polyester Yarns]]）.
- **Doping as the conductive-polymer mechanism.** Treating a polymer film with a halogen (chlorine, bromine or iodine) — **"doping", by analogy with semiconductors** — made polyacetylene film **10⁹× more conductive**（源：[[Seymour Polymer Chemistry Ch18 Special Topics]]）.
- **CNT-fibre route — a negative result.** As-prepared CNT fibres are reported to **fail on softness and processability**, which the vault reads as evidence that a CNT-based route is premature for a disposable（源：[[Smart Fabrics and Networked Clothing]]）.

## Hygiene Relevance 卫材关联

- **The vault's hygiene use-case is a conductive-thread wetness sensor.** K-C's leakage-detection garment uses a silver-plated conductive thread (60 Ω/m) + controller + ADC read-out to answer "is it wet / did it leak" — but the claimed article is the **garment**, not the absorbent article, i.e. the yarn sits on an over-garment rather than in the core（源：[[US11013641 Garment for Detecting Absorbent Article Leakage]]）.
- **Electronic vs chromic branch.** This conductive-thread route is the **electronic** branch; the vault's **chromic** branch (thermochromic / hydrochromic) answers the same question **without power, electronics or an app** — the two are complementary rather than substitutable（源：[[US11013641 Garment for Detecting Absorbent Article Leakage]]）.
- **Deployable integration methods.** For a textile-borne conductor, the named routes are weave / knit / embroider / laminate / stitch（源：[[Smart Textiles Review]]）.

## Open Questions 待补

- **No hygiene-grade conductive-yarn spec** (wash durability under urine, skin contact, silver-plating biocompatibility) appears in the read sources `[待补]`.
- The textile resistivity range spans ~4 orders of magnitude (0.5 Ω/m to kΩ/m); **no selection criterion for a hygiene sensor** is given `[待补]`.
- Cost and supply of silver-plated thread for a disposable are **not** addressed `[待补]`.

## Related Sources 关联来源

- [[Smart Textiles & Wearables]] — cited-by: parent index of the smart-textiles / wearables collection
- [[Smart Textiles Review]] — cited-by: conductive-yarn resistivity range 0.5 Ω/m to kΩ/m; integration methods
- [[US11013641 Garment for Detecting Absorbent Article Leakage]] — silver-plated conductive thread 60 Ω/m; Shieldex® exemplar; 3.3 VDC resistive sensing
- [[Manufactured Fibre Technology Ch14 Speciality Polyamide and Polyester Yarns]] — antistatic / conductive-fibre routes and their wash-durability ranking
- [[Seymour Polymer Chemistry Ch18 Special Topics]] — conductive-polymer doping mechanism (polyacetylene, 10⁹×)
- [[Smart Fabrics and Networked Clothing]] — CNT-fibre properties and the softness/processability negative result
- 相关概念：[[智能织物 Smart Textile]]、[[电子纺织品 E-textile]]、[[Interactively Mechanochromic Electronic Textile Sensor]]、[[US11013641B2 Garment for Detecting Absorbent Article Leakage (Kimberly-Clark)]]、[[Kimberly-Clark（金佰利）]]、[[Sensor-Equipped Absorbent Article（含传感器吸收性物品）]]、[[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]

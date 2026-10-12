---
type: source
title: "Industrial Drying Ch16 Pneumatic and Flash Drying"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch16.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Pneumatic/flash dryers have a relatively short contact time between hot air and particulate materials (0.5–10 s) at the drying section; because of this the material temperature stays always low, making flash dryers most suitable for removal of external (surface) moisture and less suitable for internal moisture (p.395–396)."
  - "Short contact time and parallel flow make it possible to dry thermolabile materials (p.396)."
  - "The gas velocity must be greater than the free fall velocity of the largest particle to be dried (p.396)."
  - "There is a risk of fire and explosion, so care must be taken to avoid flammability limits in the dryer; the dryer cannot be used for toxic materials because of powder emission; superheated steam can avoid this disadvantage (p.397)."
  - "Flash dryers using superheated steam instead of air have no fire or explosion risk and higher efficiency if exhaust steam is utilized elsewhere, but the system and its operation are more complex — leaks are prohibited, and air-tight feeding/discharge is required (p.399)."
  - "Flash dryers are widely used in the plastic and polymer industries; Andrieu and Bressat presented a simple model for pneumatic drying of PVC particles (p.400–401)."
summary_cn: "气流/闪蒸干燥章节确立'0.5–10 s短接触+并流→料温恒低→只除表面水分'的能力边界，给出自由沉降速度设计门槛、粉尘燃爆红线与过热蒸汽介质方案，以及双流体/Eulerian/DEM完整方程组——对卫材只在与SAP粉末、聚合物母粒及粉尘安全相关的窄通道内有实质价值，对网材/绒毛毡不适用。"
tags: ["source/book", "drying/flash", "drying/pneumatic", "surface-moisture", "dust-explosion", "superheated-steam"]
tags_zh: ["闪蒸干燥", "气流干燥", "表面水分", "粉尘燃爆", "过热蒸汽", "双流体模型"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch14 Spouted Bed Drying]]", "[[Industrial Drying Ch15 Impingement Drying]]", "[[Industrial Drying Ch17 Conveyor Dryers]]", "[[Industrial Drying Ch50 Solid-Liquid Separation]]"]
---

# Pneumatic and Flash Drying (Ch.16)

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.16, pp.395–408 (Borde & Levy).

## Chapter Overview 章节概览

Chapter 16 treats pneumatic (flash) drying as a gas–solid transport convective dryer in which wet particulates are suspended in a hot gas (air or superheated steam) and conveyed through a duct, with residence time in the drying section of only 0.5–10 s. Logical spine: short contact + parallel (co-current) flow → material temperature stays always low → suitable only for external/surface moisture and thermolabile solids, less suitable for internal moisture. Sections: operation principle and applications, design procedure (heat/mass/momentum balances + transfer coefficients), dried-material list, modelling menu (pressure-drop correlations, two-fluid/Eulerian-granular/DEM frameworks, Eqs 16.5–16.25), and expected developments (heat recovery, heat pumps, combined processes).

> Note: page numbers derived from PDF-page − 21; spot-check against print edition.

## Key Viewpoints 关键观点

### 1. Capability boundary: surface moisture only 能力边界

> "One of the features of these types of dryers is the relatively short contact time between the hot air and the particulate materials (0.5–10 s) at the drying section. Because of this the material temperature stays always low in the drying process … flash dryers are most suitable for removal of external moisture (surface moisture) and are less suitable for removal of internal moisture." (p.395–396)

A flash dryer is a surface-moisture dryer; bound/internal moisture (e.g. the falling-rate period of a fluff mat) cannot be removed here.

### 2. Co-current geometry protects thermolabile solids 并流保护热敏物料

> "Short contact time and parallel flow make possible to dry thermolabile materials." (p.396)

### 3. Free-fall velocity design gate 设计门槛

> "The gas velocity must be greater than the free fall velocity of the largest particle to be dried." (p.396)

This single inequality sets duct diameter, fan power, and residence-time distribution.

### 4. Dust fire/explosion is the safety red line 粉尘燃爆红线

> "There is a risk of fire and explosion, so care must be taken to avoid flammability limits in the dryer." (p.397)

> "Because of powder emission, the dryer cannot be used for toxic materials. In some cases this disadvantage can be avoided using superheated steam as a drying agent." (p.397)

Cellulosic fibre dust and SAP powder are combustible particulates — a hard operating constraint.

### 5. Superheated steam: explosion-free but complex 过热蒸汽

> "Flash dryers using superheated steam as drying medium instead of air have some advantages such as no fire or explosion risk and higher efficiency (if exhaust steam is utilized elsewhere in the process)." (p.399)

Limitations: "Leaks are prohibited as noncondensables cause problems with energy recovery by condensation or compression of the exhaust steam. The feeding and discharge process must not allow infiltration of air and start-up and shutdown processes are more complex than for air dryers." (p.399)

### 6. Polymer industries are a core application 聚合物应用

> "Flash dryers are widely used in the plastic and polymer industries." (p.400); "Andrieu and Bressat [16] presented a simple model for pneumatic drying of PVC particles." (p.401)

## Key Terms & Process Details 关键术语

- Free-fall (terminal) velocity: gas must exceed it for the largest particle to stay suspended (p.396).
- Spin-flash dryer: mechanically agitated fluidized bed for sludge, pulps, pastes, filter cakes without an atomizer; up to 10 t/h (p.399).
- Two-fluid balance set: continuity (16.5), momentum (16.6), energy (16.15), interphase heat exchange Q_gs = 6ε_s(1−ε_s)λ_g(T_g − T_ss)/d_s² (16.16), drag law (16.13), single-particle evaporation (16.20) and period-2 Stefan-type diffusion (16.21) — the kernel predicting outlet moisture from inlet temperature and particle size (p.403–406).
- Particle-size lesson: "As the particle size was increased, the heat transfer rate decreases and the residence time increases … less permeable wood species or larger chips size leads to longer dryer." (p.403) — larger/coarser particles need longer ducts.
- Model caveat: "the developed mathematical model should be experimentally validated in order to use it as a design tool." (p.403)
- Feed-size typo: text states particulate size "usually in the range of 10–500 mm" (p.395) — physically inconsistent with flash-dryer practice; almost certainly 10–500 µm [待验证 against print].

## Strengths & Weaknesses 优劣评估

- Strengths: explicit surface/internal-moisture boundary and thermolabile advantage (p.395–396); usable design procedure and Nu correlations (Table 16.1); dust fire/explosion and superheated-steam route treated head-on (p.397, p.399); full two-fluid equation set as scale-up kernel.
- Weaknesses: no specific-energy benchmark (unlike Ch.15's 3100 kJ/kg water); polymer thermal sensitivity left unquantified ("thermal sensitivity of the solids", p.397); nothing on fluff/nonwoven/tissue; constant-rate framing only — no hygroscopic/bound-moisture treatment, exactly the regime fluff/SAP care about.

## Hygiene Implication 卫材关联

Relevance: ★★☆☆☆ — narrow: flash drying handles particulates and pastes, not the continuous webs, fluff fibre mats, or airlaid nonwovens that dominate diaper/wipe manufacture. The genuinely relevant threads are SAP powder, polymer pellets, and powder-explosion safety:

- Use flash/spin-flash only for surface-moisture powders: route SAP powder and PP/PE masterbatch through lines sized by free-fall velocity (p.396); do not use it for bound-moisture fluff or webs (p.395–396).
- Dust-explosion engineering (highest-priority hook): cellulosic/SAP dust must stay outside flammability limits (p.397); superheated steam medium removes the fire/explosion risk (p.399) but demands air-tight feed/discharge.
- Inlet temperature cap: set gas temperature from the polymer's thermal-degradation/Tg window, not just evaporation needs (p.397) — the chapter leaves "thermal sensitivity" unquantified [待验证].
- Spin-flash option: a high-solids SAP slurry or binder paste can be spin-flash dried without an atomizer, up to 10 t/h (p.399).
- Scale-up: use the two-fluid kernel (Eqs 16.5–16.25) to predict that coarser SAP agglomerates need longer residence, and validate against pilot data first (p.403).

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch14 Spouted Bed Drying]]
- [[Industrial Drying Ch15 Impingement Drying]]
- [[Industrial Drying Ch17 Conveyor Dryers]]
- [[Industrial Drying Ch50 Solid-Liquid Separation]]

---
type: source
title: "BM Indicator Design — Viscosity & Cost（便指示·流变与成本）"
source_type: 技术方案（内部工艺开发，2026-07）
source_path: RAW/ima_sync/个人知识库/WKB/Projects/BM/BM_Indicator_Design_Viscosity_Cost.pptx.md
original_link: ""
date_published: 2026-07
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "The BM lane keys off soluble protein via the protein-error of a sulfonephthalein dye — a binding effect, not a pH effect（中文：便指示通道以磺酞类染料的「蛋白误差」响应可溶性蛋白——是结合效应而非 pH 效应）"
  - "Trip point is set by dye loading alone: D × C* ≈ 2,500 (µg/cm² · mg/L); the design point 0.50 µg/cm² trips at 5,000 mg/L, i.e. 33× above healthy infant urine and 34× below the 17 µg/cm² skin-safety cap（中文：触发点仅由染料负载决定——D × C* ≈ 2,500；设计点 0.50 µg/cm² 对应 5,000 mg/L 触发，为健康婴儿尿的 33 倍、低于 17 µg/cm² 皮肤安全上限 34 倍）"
  - "An alkaline odour-control granular can titrate the BM lane's buffer from the inside — the No. 1 risk in the programme（中文：碱性除臭颗粒会从内部滴定便通道缓冲体系——本项目第一大风险）"
  - "The melt must be designed near-Newtonian on purpose: Cross index n = 0.88, spec n ≥ 0.85, so the 9,000–40,000 s⁻¹ slot shear does not cause ribbing and edge bleed（中文：熔体须刻意设计为近牛顿流体——Cross 指数 n = 0.88，规范 n ≥ 0.85，以免 9,000–40,000 s⁻¹ 的狭缝剪切造成条纹与边缘溢流）"
  - "A free-gap pre-metered slot die cannot run this: Ca = 272 at 400 m/min and 125 °C forces a maximum free gap of 44 µm, against web flutter of ±150 µm — use a contact (wiped) slot nozzle instead（中文：自由间隙预计量狭缝模头无法跑此工艺——400 m/min、125 ℃ 下 Ca=272，最大自由间隙仅 44 µm，而幅材抖动达 ±150 µm——须改用接触（刮涂）式狭缝喷嘴）"
  - "The breathable film, not the chemistry, sets the temperature ceiling: a microporous CaCO₃-filled PE film loses WVTR irreversibly above ~90 °C, capping application at 125 °C (115–132 °C)（中文：温度上限由透气膜而非化学决定——微孔碳酸钙填充 PE 膜在约 90 ℃ 以上不可逆损失 WVTR，故施胶温度上限为 125 ℃（115–132 ℃））"
  - "All-in cost US$0.567 per 1,000 diapers (0.057 ¢/diaper); the dominant cost is OEE given up to a fourth applicator (US$0.240/1,000), not the dye (US$0.02/1,000)（中文：全含成本 US$0.567/千片（0.057 美分/片）；主要成本是让给第四套涂布装置而失去的 OEE（US$0.240/千片），而非染料（US$0.02/千片））"
pages_linked: ["[[Protein Error of pH Dye（pH 染料的蛋白误差）]]", "[[Odour-Control Granular Interference（除臭颗粒干扰）]]", "[[Hot-Melt Slot Coating（热熔狭缝涂布）]]", "[[Wetness Indicator Ladder（尿湿指示阶梯）]]", "[[Titratable Acidity Lane（可滴定酸度通道）]]", "[[Urine Indicator vs BM Indicator（尿湿指示 vs 便指示）]]"]
---

# BM Indicator Design — Viscosity & Cost（便指示·流变与成本）

## One-line Positioning 一句话定位

The **second-generation BM indicator design** for a composite breathable backsheet — it replaces the two-lane concept with a single protein-error lane, and works the problem from the other end: dye loading as the only selectivity knob, melt rheology, slot geometry, thermal load on the breathable film, and a full cost model.

（中文：面向复合透气底膜的**第二代便指示设计**——以单条「蛋白误差」通道取代双通道概念，并从另一端切入：染料负载作唯一选择性旋钮、熔体流变、狭缝几何、透气膜热负荷，以及完整成本模型。）

## Summary 摘要

The design rule is stated first: the BM lane must key off a molecule abundant in stool and effectively absent from urine, through a mechanism that is **not pH, not humidity, not temperature**. Four reasons are given — urine arrives first and often (6–8 voids per 12 h) so any moisture/pH lane is saturated before the first stool; stool carries very little free water so the liquid must be transported to the lane; ammonia rewrites the pH landscape (urea → NH₃ pushes a used diaper to pH 8–9 within hours); and body heat is always present, so a 31–34 °C temperature lane is permanently ON.

Five candidate triggers are scored. **Soluble protein** (protein-error of a pH dye, 10,000–40,000 mg/L in faecal liquid vs < 150 mg/L in healthy urine) is SELECTED; bilirubin/bile pigment (diazonium coupling) is confirmatory tier 2 because diazonium salts are light- and heat-labile in a 125 °C melt; faecal protease (cleavable chromogen) is R&D only on cost and melt-survival grounds; faecal lipase is rejected for slow kinetics and no aqueous phase; conductivity/ionic strength is rejected for overlapping urine and needing electronics.

The mechanism is worked out in detail: the lane is buffered hard to pH 3.0 with a citrate / stearyl-phosphate acid system so the dye sits fully in its yellow protonated form; free amino groups on the polypeptide bind the dye anion electrostatically and stabilise it, shifting the apparent pKa down so the dye ionises and turns violet **while the bulk pH is still 3**. Trip point is set by dye loading alone via D × C* ≈ 2,500. Four independent defences against a false BM signal are listed (protein binding not pH; a 5,000 mg/L threshold; a micro-environment with 1.94 µeq H⁺/cm² of accessible acid against ~0.0055 µeq of alkali ingress → 350× margin; and lane placement/geometry), with the honest note that a false positive needs all four to fail at once while a false negative needs only the geometry to fail.

Micro-environment spec: equilibrium water uptake ≤ 5 wt % at 37 °C/95 % RH/24 h, accessible acid ≥ 1.8 µeq H⁺/cm² (titrated pH 2.5 → 4.5). The formulation is a rosin/wax matrix (pentaerythritol rosin ester 34 %, polymerised rosin 14 %, Fischer-Tropsch wax C40–C60 26 %, hydrogenated C5 9 %, micronised citric acid 6 %, monostearyl citrate 3.5 %, stearyl phosphate 2 %, C12-14 alcohol ethoxylate 3 %, organoclay 1.2 %, AO 1.25 %, bromocresol purple 0.025 %, Solvent Red 24 0.025 %) at a blended cost of US$3.56/kg.

Two critical formulation warnings: **never use a soluble quat** (it mimics protein and develops the violet in the pack — use a cationic organoclay ≤ 1.5 %), and every solid must satisfy shim ≥ 10 × d90, which at a 200 µm shim caps d90 at 20 µm.

Rheology is specified as near-Newtonian on purpose: 3,200 mPa·s @ 120 °C (2,100 @ 130 °C, 1,400 @ 140 °C), Cross index n = 0.88 (spec ≥ 0.85), λ ≤ 2 × 10⁻⁴ s, flow activation energy 56 kJ/mol, no high-MW styrenic block copolymer. Slot geometry matters because pressure scales with 1/t³: a 200 µm shim gives 13.6 bar over a 5 mm land at 400 m/min, while a 100 µm shim would give 99.7 bar and stall the existing pump. Because Ca = 272, a contact (wiped) slot nozzle on a chilled backing roll is mandatory, with a servo speed-following gear pump and 2–4 N/cm nozzle contact pressure.

Thermal load is the binding constraint: the contact interface reaches 69 °C at a 125 °C melt (comfortable), but the bulk equilibrium temperature reaches 85 °C at 125 °C and 90 °C at 135 °C — and a microporous CaCO₃-filled PE film loses WVTR irreversibly once the drawn structure anneals above ~90 °C. A chilled backing roll moves the ceiling up by ~15 K. Nominal set point 125 °C, window 115–132 °C (lower ≈112 °C by die pressure, upper ≈134 °C by film pore collapse; viscosity floor ≈136 °C).

Cost: US$0.567 per 1,000 diapers all-in (material 0.142, capex amortised 0.109 over 707 M diapers/3 y, OEE allowance 0.240 at 0.30 %), i.e. 0.056–0.057 ¢/diaper. Net new hardware ≈ US$77 k core / US$109 k with in-line colour verification. Test plan covers a protein challenge ladder (0 / 150 / 1,000 / 5,000 / 10,000 / 40,000 mg/L bovine albumin), urine at pH 5.5 and 9.0, aged urine, stability (40 °C/75 % RH 8 weeks; 8 h melt at 130 °C; light; dye leach), process/product (Cpk ≥ 1.33 on 20 ± 3 gsm; WVTR and hydrohead at every set point; a real-stool panel of 20 breast-fed + 20 formula-fed with ≥ 95 % detection at 15 min; caregiver comprehension 40 mothers ≥ 90 %). A 90-day plan runs from granular screening (weeks 1–2) to a single-lane line trial (weeks 10–13).

（中文摘要：设计铁律先立——便通道须以「便中丰富、尿中基本不存在」的分子为触发，且机制**不得是 pH、湿度或温度**。四条理由：尿先到且频繁（12 h 内 6–8 次），任何湿度/pH 通道在首次排便前就饱和；粪便自由水极少，液体须被输运到通道；氨改写了 pH 格局（尿素→NH₃ 使使用中纸尿裤数小时内 pH 8–9）；体温恒在，31–34 ℃ 温度通道一直处于导通态。五候选打分：**可溶性蛋白**（pH 染料蛋白误差，粪便液 10,000–40,000 mg/L vs 健康尿 <150 mg/L）中选；胆红素/胆色素（重氮偶联）列为二级确认项（重氮盐在 125 ℃ 熔体中光热不稳）；粪便蛋白酶仅作研发；脂肪酶因动力学慢且熔体无连续水相被否；电导/离子强度因与尿重叠且需电子件被否。机理细节：通道用柠檬酸/硬脂基磷酸把微环境缓冲到 pH 3.0，使染料处于完全质子化黄色态；多肽游离氨基以静电结合染料阴离子、稳定之并下移表观 pKa，染料电离转为紫色，**而本体 pH 仍为 3**；触发点仅由染料负载决定，D × C* ≈ 2,500。四重防假阳性（蛋白结合非 pH；5,000 mg/L 阈值；微环境中可及酸 1.94 µeq H⁺/cm² 对抗约 0.0055 µeq 碱进入 → 350 倍余量；通道位置与几何），并诚实指出：假阳性需四者同时失效，假阴性只需几何失效。微环境规范：37 ℃/95% RH/24 h 平衡吸水 ≤5 wt%，可及酸 ≥1.8 µeq H⁺/cm²。配方为松香/蜡基体（季戊四醇松香酯 34%、聚合松香 14%、FT 蜡 C40–C60 26%、氢化 C5 9%、微粉柠檬酸 6%、单硬脂酰柠檬酸酯 3.5%、硬脂基磷酸 2%、C12-14 醇醚 3%、有机黏土 1.2%、抗氧剂 1.25%、溴甲酚紫 0.025%、溶剂红 24 0.025%），混配成本 US$3.56/kg。两条关键配方警示：**禁用可溶性季铵盐**（会模拟蛋白、在包内即显紫——改用阳离子有机黏土 ≤1.5%）；所有固体须满足垫片 ≥10×d90，200 µm 垫片对应 d90 ≤20 µm。流变刻意做成近牛顿：120 ℃ 下 3,200 mPa·s（130 ℃ 2,100、140 ℃ 1,400），Cross 指数 n=0.88（规范 ≥0.85），活化能 56 kJ/mol，禁用高分子量苯乙烯嵌段共聚物。狭缝几何因压降 ∝1/t³ 而关键：200 µm 垫片在 5 mm 台面、400 m/min 下降 13.6 bar，而 100 µm 会到 99.7 bar 并憋停泵。因 Ca=272，必须用接触（刮涂）式狭缝喷嘴 + 冷却背辊 + 伺服随速齿轮泵 + 2–4 N/cm 接触压。热负荷是硬约束：接触界面在 125 ℃ 熔体下仅 69 ℃（舒适），但本体平衡温度 125 ℃ 时 85 ℃、135 ℃ 时 90 ℃，而微孔碳酸钙填充 PE 膜在约 90 ℃ 以上退火即不可逆损失 WVTR；加冷却背辊可把上限抬高约 15 K。标称 125 ℃，窗口 115–132 ℃。成本 US$0.567/千片全含（材料 0.142、capex 摊销 0.109、OEE 让渡 0.240）；新增硬件约 7.7 万美元（含在线色彩验证 10.9 万）。测试计划含蛋白阶梯、pH 5.5/9.0 与老化尿挑战、稳定性与工艺产品项，以及 90 天从颗粒筛查到单通道产线试产的计划。）

## Extracted Numbers and Conclusions 提炼的数字与结论

### A. Six headline numbers 六个核心数字

| Item 项目 | Value 数值 | Note 备注 |
|---|---|---|
| TRIGGER 触发 | Soluble protein > 5,000 mg/L | Protein-error of a sulfonephthalein dye — a binding effect, not pH |
| DYE LOADING 染料负载 | 0.50 µg/cm² = 0.025 wt % | Sets the trip point; 34× below the 17 µg/cm² skin-safety cap |
| MELT VISCOSITY 熔体黏度 | 3,200 mPa·s @ 120 °C | 2,100 @ 130 °C, 1,400 @ 140 °C; Cross index n = 0.88 |
| APPLICATION 施胶温度 | 125 °C（window 115–132 °C） | Ceiling is the breathable film, not the chemistry |
| COAT WEIGHT 涂布量 | 20 gsm，10 × 200 mm = 40 mg/diaper | On the skin side of the backsheet |
| COST IMPACT 成本 | 0.057 ¢/diaper；US$0.57 / 1,000 all-in | 含 capex 摊销与 OEE |

### B. Mechanism screening 机理筛查

| Mechanism 机理 | Why it discriminates 判别依据 | Practical limit 实践局限 | Call 裁决 |
|---|---|---|---|
| Soluble protein 可溶性蛋白 | 10,000–40,000 mg/L in faecal liquid vs < 150 mg/L in healthy urine | Melt-stable, cheap, dye already qualified for hygiene | **SELECTED 选用** |
| Bilirubin / bile pigment 胆红素 | Very high in infant stool; essentially zero in urine | Diazonium salts light- and heat-labile in a 125 °C melt | Confirmatory tier 2 |
| Faecal protease 粪便蛋白酶 | Trypsin / chymotrypsin / elastase are faecal markers | Highest specificity but substrate cost and melt survival | R&D only |
| Faecal lipase 粪便脂肪酶 | Lipase abundant in stool | Slow kinetics; needs an aqueous phase | **Rejected** |
| Conductivity / ionic strength 电导 | Stool differs in ionic strength and rheology | Overlaps urine almost completely; needs electronics | **Rejected** |

*(原文对五项均给 ◆◆◆◆◆ 满星，故本表只记「CALL」列，星级不重复标注。)*

### C. Selectivity margin 选择性余量

| Margin 余量 | Value 数值 | Basis 依据 |
|---|---|---|
| Design point 设计点 | 0.50 µg/cm² = 0.025 wt % of a 20 gsm coat | D × C* ≈ 2,500 (µg/cm² · mg/L) |
| vs healthy infant urine 对健康婴儿尿 | **33×**（trip 5,000 vs < 150 mg/L） | — |
| vs faecal liquid 对粪便液 | **2×**（trip 5,000 vs > 10,000 mg/L） | — |
| vs safety cap 对安全上限 | **34×**（0.50 vs 17 µg/cm²） | — |
| Edge case 边界案例 | Nephrotic urine — verify with a 10,000 mg/L albumin challenge | `[待验证]` |
| Buffer margin 缓冲余量 | 350×（1.94 µeq H⁺/cm² vs ~0.0055 µeq alkali ingress） | 8 h ammoniacal urine at 55 mmol/L base |

> ⚠️ 判据边界提醒：对粪便液仅 **2×** 余量，意味着阈值设定容错很小；对健康尿 33× 余量则较宽。原文同时指出「假阴性只需几何失效」，故流体输运工程比化学更硬。

### D. Formulation 配方（BM indicator hot melt）

| Component 组分 | wt % | Function 功能 |
|---|---|---|
| Pentaerythritol rosin ester, SP ≈ 98 °C | 34.0 | 1st binder；把染料锁在黄色态；酸性 |
| Polymerised rosin 聚合松香 | 14.0 | 色深、内聚、酸储备 |
| Fischer-Tropsch wax, C40–C60 | 26.0 | 定黏度与开放时间；保持 n 近 1 |
| Hydrogenated C5 hydrocarbon resin | 9.0 | 柔韧、对 PE 膜附着、抗掉屑 |
| Citric acid, micronised d90 < 15 µm | 6.0 | 缓冲酸腿，把通道钉在 pH 3.0 |
| Monostearyl citrate | 3.5 | 熔体可溶缓冲腿；无颗粒负荷 |
| Stearyl phosphate free acid | 2.0 | 抗湿热储存的强酸稳定剂 |
| C12-14 alcohol ethoxylate (7 EO) | 3.0 | 润湿；加速显色动力学 |
| Organoclay (quaternised bentonite) | 1.2 | 锚定紫色阴离子（**替代可溶性季铵盐**） |
| Hindered phenol AO + phosphite | 1.25 | 130 °C、8 h 停留稳定 |
| Bromocresol purple | 0.025 | 蛋白误差染料；20 gsm 下 0.50 µg/cm² |
| Solvent Red 24 (oil-soluble tint) | 0.025 | 把变色前色相与尿通道区分 |
| **Blended cost 混配成本** | **US$3.56 / kg** | 40 mg/片 → US$0.142 / 1,000 |

- 🔴 **DO NOT USE A SOLUBLE QUAT（禁用可溶性季铵盐）**：标准尿显配方用可溶季铵盐锚定染料，但在蛋白误差通道中该盐会模拟蛋白并在包内显紫 → 改用阳离子有机黏土 ≤ 1.5 %。
- 📏 **PARTICLE-SIZE RULE（粒径规则）**：每一切固体须满足 shim ≥ 10 × d90 → 200 µm 垫片对应 d90 ≤ 20 µm；柠檬酸须微粉化、有机黏土须过 25 µm 筛后才进熔化罐。

### E. Rheology and slot geometry 流变与狭缝几何

| Spec 规格 | Value 数值 | Note 备注 |
|---|---|---|
| Brookfield viscosity @ 140 °C | 3,200 / 2,092 / 1,396 mPa·s（120/130/140 °C） | Spec band ± 18 % |
| Cross index n | 0.88（spec n ≥ 0.85） | Deliberately near-Newtonian；10–50,000 s⁻¹ 毛细管流变仪 @ 125 °C |
| Relaxation time λ | ≤ 2 × 10⁻⁴ s | — |
| Flow activation energy | 56 kJ/mol | — |
| Slot shear rate 狭缝剪切 | 9,000–40,000 s⁻¹ | 125–300 µm shim, 200–500 m/min |
| Melt density @ 125 °C / surface tension | 0.90 g/cm³ / 30 mN/m | — |
| Shim thickness 垫片厚度 | 200 µm | 100 µm 会到 99.7 bar，超出现有 HMA 系统上限 |
| Wall shear rate @ 400 m/min | 22,200 s⁻¹ | Viscosity at that shear 1,225 mPa·s |
| Pressure drop over 5 mm land | 13.6 bar | Existing HMA system ceiling 40 bar |
| Ca at 400 m/min, 125 °C | 272 | 深度高 Ca 区 |
| Max free gap 最大自由间隙 | H ≤ 44 µm | 而幅材抖动 ±150 µm → 不可行 |
| Required wet film | h = 22.2 µm | = 20 gsm ÷ 900 kg/m³ |

> 结论：必须用**接触（刮涂）式狭缝喷嘴**（唇口在硬化冷却背辊上的膜面运行，有效间隙≈0）+ 冷却背辊 15–20 °C + 伺服随速齿轮泵 + 喷嘴接触压 2–4 N/cm。

### F. Process window and thermal load 工艺窗口与热负荷

| Limit 边界 | Value 数值 | Cause 成因 |
|---|---|---|
| Nominal set point 标称设定点 | 125 °C | 膜上限下方约 13 K、压力上限上方约 13 K |
| Lower temperature limit 下限 | ≈ 112 °C | 模头压力超过 40 bar 系统上限 |
| Upper temperature limit 上限 | ≈ 134 °C | 膜本体温度达 90 °C，微孔结构开始闭合 |
| Viscosity floor 黏度地板 | ≈ 136 °C | 低于 800 mPa·s 胶珠破裂、边缘溢流 |
| Contact interface temp 接触界面温度 | 69 °C @ 125 °C melt | 由热扩散系数决定，舒适 |
| Film bulk equilibrium 膜本体平衡温度 | 85 °C @ 125 °C；90 °C @ 135 °C | **闭合微孔的临界量** |
| Pore-collapse threshold 塌孔阈值 | ~90 °C | 微孔 CaCO₃ 填充 PE 膜退火即不可逆损失 WVTR |
| Chilled backing roll benefit | + ~15 K headroom | 比重新配方降施胶温度便宜得多 |
| Mandatory test 必修测试 | WVTR (ASTM E96) + hydrohead，coated vs uncoated，窗口内每一个设定点 | — |

### G. Cost model 成本模型（per 1,000 diapers）

| Item 项目 | Value 数值 |
|---|---|
| Blended melt cost | US$3.56 / kg |
| Coat weight per diaper | 40 mg |
| Material 材料 | US$0.142 / 1,000 |
| Capex, core scope | US$76,900 |
| Capex with colour verification | US$108,900 |
| Capex amortised over 707 M diapers (3 y) | US$0.109 / 1,000 |
| OEE allowance, 0.30 % | US$0.240 / 1,000 |
| **TOTAL** | **US$0.567 / 1,000 = 0.057 ¢/diaper** |

> 原文结论：**主导成本不是化学，而是让给第四套涂布装置的 OEE**（染料仅 US$0.02/千片）。工程投入应放在通道可靠性而非熔体成本上。

### H. Test plan 测试计划（要点）

| Group 组 | Items 项 |
|---|---|
| Chemistry 化学 | Protein ladder 0 / 150 / 1,000 / 5,000 / 10,000 / 40,000 mg/L bovine albumin（record ΔE* at 2, 5, 15 min）；synthetic urine pH 5.5 & 9.0, 3 × 40 mL insults → no change at 15 min & 4 h；8 h ureolysed urine at 55 mmol/L base；buffer titration pH 2.5 → 4.5 |
| Stability 稳定性 | 40 °C / 75 % RH 8 weeks graded weekly 0–5（reject at grade 1）；8 h melt-pot residence at 130 °C then re-run the ladder；light 24 h @ 6,500 K, 1,000 lux；dye leach 16 h weighted contact |
| Process & product 工艺与产品 | Cpk ≥ 1.33 on 20 ± 3 gsm across 200–500 m/min；WVTR + hydrohead at every set point；real-stool panel 20 breast-fed + 20 formula-fed with ≥ 95 % detection at 15 min；caregiver comprehension 40 mothers unprompted ≥ 90 % correct action |

### I. Top risks and 90-day plan 主要风险与 90 天计划

| Risk 风险 | Level | Mitigation 缓解 |
|---|---|---|
| Alkaline odour granular pre-develops the lane 碱性除臭颗粒预显色 | **HIGH** | Screen in week 1（slurry pH ≤ 7.5 且可滴定碱 ≤ 0.2 mmol/g 才可接受）；barrier or encapsulate；**不得以加酸抵消** |
| Faecal liquid never reaches the lane 粪便液到不了通道 | **HIGH** | 12 mm SAP-free conduit through the core + diffusion layer；用真实粪便而非模拟液验证 |
| Soluble quat carried over from a WI base 尿显基料携带的可溶季铵盐 | MEDIUM | Specify organoclay；audit the supplier's base formulation |
| Film WVTR loss from thermal load 热负荷致 WVTR 损失 | MEDIUM | Chilled backing roll；cap at 132 °C；WVTR at every set point |
| FTO around granted faeces-indicator claims 专利自由度 | MEDIUM | Formal FTO on US 12,396,899 and family before pilot spend |

- 90-day plan：W1–2 screen the odour granular（go/no-go before any spend）→ W3–6 bench formulation（three dye loadings × two buffer levels）→ W7–9 pilot coater（capillary rheometer + 100–200 m/min + WVTR/hydrohead）→ W10–13 line trial（contact nozzle + chilled roll on one lane；Cpk、8-week ageing pull、stool panel）。
- Odour-granular chemistry screen（risks）：Zeolite 4A/13X pH 9–11 HIGH；sodium bicarbonate pH 8.3 HIGH；activated carbon pH 6–10 MEDIUM（还会吸附染料）；cyclodextrin pH 6–7 LOW（兼容选择）；ion-exchange resin H⁺ form pH 4–6 LOW（有助益）。

（中文：主要风险与缓解见表；90 天计划为 W1–2 颗粒筛查（先做 go/no-go 再花钱）→ W3–6 台式配方（3 染料负载 × 2 缓冲水平）→ W7–9 中试涂布 → W10–13 产线试产（接触喷嘴 + 冷却辊，单通道）。除臭颗粒碱度筛查：沸石 4A/13X pH 9–11 高、碳酸氢钠 pH 8.3 高、活性炭 pH 6–10 中（且会吸染料）、环糊精 pH 6–7 低（兼容）、H⁺ 型离子交换树脂 pH 4–6 低（有益）。）

## Key Claims 关键论断

- **触发分子必须是便中丰富、尿中不存在的蛋白** —— pH/湿度/温度全部不可用（假阴性风险）。支撑页：[[Protein Error of pH Dye（pH 染料的蛋白误差）]]
- **染料负载是唯一的选择性旋钮** —— 想改触发阈值只能改负载量。支撑页：[[Protein Error of pH Dye（pH 染料的蛋白误差）]]
- **碱性除臭颗粒是头号风险** —— 会从内部滴定缓冲体系；缓解须靠阻隔/包覆而非加酸。支撑页：[[Odour-Control Granular Interference（除臭颗粒干扰）]]
- **几何（流体输运）比化学更难** —— 假阴性只需几何失效。支撑页：[[Hot-Melt Slot Coating（热熔狭缝涂布）]]
- **温度上限由透气膜的 WVTR 决定** —— 线上看不出来，一周后的恒温恒湿箱里才发作。支撑页：[[Hot-Melt Slot Coating（热熔狭缝涂布）]]
- **成本主体是 OEE 而非染料** —— 第四套涂布装置的可靠性才是工程重点。

## Related Pages 关联页面

- Concepts 概念：[[Protein Error of pH Dye（pH 染料的蛋白误差）]]、[[Odour-Control Granular Interference（除臭颗粒干扰）]]、[[Hot-Melt Slot Coating（热熔狭缝涂布）]]、[[Wetness Indicator Ladder（尿湿指示阶梯）]]、[[Titratable Acidity Lane（可滴定酸度通道）]]
- Comparisons 对比：[[Urine Indicator vs BM Indicator（尿湿指示 vs 便指示）]]
- Existing pages 既有页：[[智能尿裤功能层]]、[[变色油墨]]

## Source 原文

- Local path 本地路径：`RAW/ima_sync/个人知识库/WKB/Projects/BM/BM_Indicator_Design_Viscosity_Cost.pptx.md`
- Original link 原文链接：（无；内部资料）
- Header 页眉信息：`PROCESS DEVELOPMENT · ABSORBENT HYGIENE · JULY 2026`
- Patent cited 引用专利（原文，仅记编号与状态主张）：US 12,396,899 and family（feces-indicator claims，原文标为需在 spend 前做正式 FTO）
- Sibling document 同族文档：[[BM Urine Indicator Concept（尿+便双指示概念）]]

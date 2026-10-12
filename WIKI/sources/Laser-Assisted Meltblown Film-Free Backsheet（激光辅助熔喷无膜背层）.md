---
type: source
title: "Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）"
source_type: 技术评估
source_path: RAW/ima_sync/个人知识库/WKB/Projects/Film/Laser_Meltblown_Film_Free_Backsheet.pptx - 已修复.pptx.md
original_link: ""
date_published: "[待验证]"
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "The laser does not make finer fibres: in the industrial window fibre diameter is drag-limited by throughput per hole and jet velocity, and raising tip temperature 250 → 300 °C changes the simulated diameter by < 1%（激光并不使纤维变细：工业窗口内直径受每孔产量与射流速度的阻力限制，模头温度 250→300 ℃ 对模拟直径的改变 <1%）"
  - "The anti-ageing case is real and large: heating only the tip lets the bulk melt run at 245 °C instead of 285 °C, and simulated MFR drift falls from 1.67× to 1.08×, with the 320 °C tip itself contributing 0.004%（抗降解收益真实且可观：只加热模头使主体熔体从 285 ℃ 降到 245 ℃，MFR 漂移由 1.67× 降至 1.08×，320 ℃ 模头本身仅贡献 0.004%）"
  - "A film-free backsheet works outside the crotch: SMMMS at 30 gsm reaches 141 mbar hydrohead clean and 121 mbar against synthetic urine, versus 88 mbar of sitting pressure from a 9 kg infant, but collapses to 55 mbar against runny stool and 14 mbar against barrier cream, while film holds > 1000 mbar regardless（无膜背层在裆部以外可行：30 gsm SMMMS 静水压 141 mbar（清水）/121 mbar（合成尿），9 kg 婴儿坐压 88 mbar；遇稀便降至 55 mbar、遇护臀膏降至 14 mbar，而膜层在任何一列均 >1000 mbar）"
  - "Nonwoven barrier is formation-limited, not pore-limited: an ideal-pore model over-predicts by 15×, and breakthrough occurs at the weakest local basis-weight patch (a Gumbel minimum about 3.74 SD below the mean over 10⁴ patches per 100 cm²)（阻隔受成形均一性限制而非孔径限制：理想孔模型高估 15 倍，击穿发生在最弱局部克重斑；每 100 cm² 约 10⁴ 个斑块的 Gumbel 最小值约为均值下方 3.74 个标准差）"
  - "Splitting the meltblown across independent beams buys barrier for free: one beam at 15 % CV retains 44 % of its weight at the weakest patch, four beams retain 72 % — the same polymer, same grams, 64 % more barrier（把熔喷拆成多束可白拿阻隔：单束 15 % CV 在最弱处仅保住 44 % 克重，四束保住 72%——同聚合物、同克重，阻隔 +64%）"
  - "SMMSMMS adds 8 gsm and ~27 % cost for no barrier gain; the inner spunbond only helps where the web is mechanically activated (ring-rolled ears, pant side panels)（SMMSMMS 多 8 gsm、成本高约 27% 而阻隔无增益；内层纺粘仅在机械活化区（环辊耳、裤侧片）有用）"
  - "Recommendation: zone the backsheet rather than swap it wholesale — roughly 62 % of backsheet area goes film-free now, and the crotch over the core footprint keeps film until contamination transport data improves（建议：背层分区而非整体替换——约 62% 面积可去膜，芯体足迹内的裆部暂留膜，待污染物输运数据改善再议）"
pages_linked: ["[[Meltblown Nonwoven（熔喷非织造布）]]", "[[Film-Free Backsheet（无膜背层）]]", "[[Formation-Limited Barrier（阻隔的成形受限机理）]]", "[[Laser-Assisted Die Tip（激光辅助模头）]]", "[[SMMMS Film-Free vs Microporous Film Backsheet（无膜背层 vs 微孔膜背层）]]", "[[SMMMS vs SMMSMMS（成本·性能·供应链）]]", "[[SMS复合结构]]", "[[熔融指数与化学降解]]", "[[无纺布五大工艺对比]]"]
---

# Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）

## One-Line Positioning 一句话定位

A **physics-based feasibility study** asking whether an all-PP SMMMMS structure can replace the breathable backsheet film. Its purpose in this library is to supply the quantitative barrier, attenuation and degradation limits behind any "drop the film" proposal, and to supply a **zoning** answer instead of a yes/no answer.
（本页回答「全 PP 的 SMMMMS 结构能否替代透气背层膜」，属**基于物理模型的可行性研究**。在本库中的用途是：为任何「去膜」提案提供量化的阻隔／拉伸衰减／降解边界，并把答案从「行不行」改成**分区**。）

## Summary 摘要

1. The deck opens with an executive verdict of three findings, and its first finding is **negative**: in the industrial window fibre diameter is drag-limited — set by throughput per hole and jet velocity, not by melt viscosity — so the stated premise that better melt flow at the nozzle gives finer fibres does not hold（模头温度 250 → 300 °C 使模拟直径变化 < 1%）.
2. Its second finding is the **real prize**: capillary residence time is 4–20 ms against 480 s for the rest of the melt path, so heating only the tip lets the bulk run at 245 °C instead of 285 °C, cutting simulated MFR drift from **1.67× to 1.08×**, with the hot tip contributing **0.004 %** of total drift. That headroom is what allows a 450 MFR resin at 130 holes/inch.（只加热模头把主体熔体降到 245 ℃，MFR 漂移 1.67× → 1.08×，模头本身仅贡献 0.004%，由此获得 450 MFR + 130 hpi 的运行空间。）
3. Its third finding is the boundary condition：SMMMS at 30 gsm reaches **141 mbar** clean hydrohead and **121 mbar** against synthetic urine, against **88 mbar** sitting pressure from a 9 kg infant — a real margin outside the crotch — but it collapses to **55 mbar** against runny stool and **14 mbar** against barrier cream, where microporous film holds **> 1000 mbar** regardless.（无膜结构在裆部外有真实裕度，但遇稀便/护臀膏即失效。）
4. The landscape section records that production dies have moved from **35 hpi to 70–100 hpi**, that die-tip patents now target air *uniformity* around the tip rather than higher air rates, that CO₂ laser supersonic drawing really does make **250–600 nm** PP/PET/PA66/PPS fibres — but **off-line**, on an already-spun filament in a vacuum chamber — and that barrier nonwovens are already displacing film at the edges（SMS support layers specified above 150 mm H₂O appear in breathable backsheet assemblies today）.
5. Model architecture: Cross-model rheology with Arrhenius shift（Ea = 42 kJ/mol; 1200 MFR → 55 Pa·s at 230 °C, 450 MFR → 136 Pa·s）、generalised Hagen–Poiseuille with a 6τv Bagley entrance term、a 1-D filament attenuation ODE（Matsui skin friction, Kase-Matsuo cooling, twin-slot jet decay）、random chain scission（1/Mn linear in time, MFR ∝ Mv^−3.4, Ea = 120 kJ/mol, anchored so a 480 s path at 285 °C gives 1.67× MFR rise）and a formation-limited barrier model（Gumbel minimum, beam averaging as 1/√n）.
6. Two of the physics findings carry the commercial argument: barrier is **formation-limited**（the ideal-pore Laplace estimate on a 1.5 µm web's median pore ≈ 800 mbar, real webs 40–140 mbar, a 15× over-prediction），and **beam splitting** converts that into a free gain（1 beam at 15 % CV retains 44 % at the weakest patch; 4 beams 72 %; +64 % barrier at identical grams）.
7. The recommendation is to **zone**：~62 % of backsheet area film-free now; SMMSMMS for pant side panels and ears; keep film in the crotch over the core footprint; upgrade the leg cuff to the same 1.2 µm meltblown grade rather than treating it as a separate material.
8. Credibility: **medium**。This is an internal, self-consistent first-principles model rather than measured data. The deck itself lists the three calibrated constants that the answer rests on（Λ = 6 whipping amplification、A = 24.5 mbar·µm/gsm barrier constant、CV = 15 % per beam at 1 mm²）and a "honest limits" section. Its conclusions are treated as **modelled**, not measured.（可信度判断依据：内部自洽的物理模型而非实测数据；作者自陈三个拟合常数与五条局限，故结论按「模拟值」而非「实测值」引用。）

## Extracted Data and Conclusions 提炼的数字与结论

### Executive verdict 核心结论

| Item 项目 | Value 数值 | Note 备注 |
|---|---|---|
| Tip temperature effect on diameter 模头温度对直径影响 | < 1 %（250 → 300 °C） | 直径受阻力（per-hole throughput × jet velocity）限制 |
| Capillary residence time 毛细管停留时间 | 4–20 ms（die-tip table: 5.9 ms） | vs 480 s for the rest of the melt path |
| Bulk melt temperature 主体熔体温度 | 245 °C（laser tip）vs 285 °C（conventional） | 只加热模头 |
| MFR drift 模拟 MFR 漂移 | 1.67×（285 °C bulk）→ 1.08×（245 °C bulk） | 模头自身贡献 0.004 % |
| Resin enabled 由此可用的树脂 | 450 MFR at 130 holes/inch | 抗降解预算换来的空间 |
| Hydrohead, clean 静水压（清水） | 141 mbar（film > 1000 mbar） | SMMMS 30 gsm |
| Hydrohead, synthetic urine 静水压（合成尿） | 121 mbar | — |
| Sitting pressure, 9 kg infant 9 kg 婴儿坐压 | 88 mbar | 裕度 2.3×（对清水尿浆） |
| Hydrohead, runny stool 静水压（稀便） | 55 mbar | 裕度消失 |
| Hydrohead, barrier cream 静水压（护臀膏） | 14 mbar | 比水低 3.7× |
| Barrier cream surface tension 护臀膏表面张力 | 33 mN/m（water 72 / urine ~66 / urine+sebum 58 / runny stool 48 / residue 40） | 击穿图（kill chart）横轴 |

### Landscape 行业现状

| Item 项目 | Value 数值 | Note 备注 |
|---|---|---|
| Production die capillary density 量产模头孔密度 | 35 hpi → 70–100 hpi | multi-row cassette 可换装于复合线 |
| Die-tip patent focus 模头专利焦点 | 尖端周围高速气流的**均匀性**（而非更大风量） | 限制阻隔的是纤维 CV 而非平均直径 |
| CO₂ laser supersonic drawing CO₂ 激光超声拉伸 | 250–600 nm PP/PET/PA66/PPS | 拉伸比 > 10⁵；**离线**，真空中已纺长丝 |
| Barrier nonwoven incumbent use 阻隔无纺布既有应用 | SMS 支撑层 > 150 mm H₂O 已见于透气背层组件 | 模块化熔喷束可在纺粘束间加装 |

### Model architecture 模型架构

| Module 模块 | Basis 依据 |
|---|---|
| A Melt rheology 熔体流变 | Cross model + Arrhenius shift，Ea = 42 kJ/mol；1200 MFR → 55 Pa·s @230 °C；450 MFR → 136 Pa·s |
| B Capillary flow 毛细管流动 | Generalised Hagen–Poiseuille + 6τv Bagley entrance term |
| C Fibre attenuation 纤维拉伸衰减 | 1-D filament ODE：dF/dz = ṁ dv/dz − Λ f_drag；Matsui 表皮摩擦、Kase-Matsuo 冷却、双槽射流衰减；对模口张力 shooting 求解 |
| D Chain scission 链断裂 | 随机断链，1/Mn 随时间线性；MFR ∝ Mv^−3.4；Ea = 120 kJ/mol；锚定于 285 °C / 480 s → 1.67× MFR |
| E Liquid barrier 液体阻隔 | Formation-limited：最弱局部斑击穿；每 100 cm² 10⁴ 斑块上的 Gumbel 最小值；束间平均按 1/√n |
| Calibration Λ 校准值 Λ | 6（whipping amplification，纤维弧长/轴向长；不设置则 1-D 模型欠拉伸 4–5×；设定为 0.5 g/hole/min @ 250 m/s → 3.1 µm） |
| Calibration A 校准值 A | 24.5 mbar·µm/gsm（设定为 10 gsm / 2.4 µm 单束熔喷 → 45 mbar，与已发表 SMS 数据吻合） |
| Calibration CV 校准值 CV | 15 %（单熔喷束 1 mm² 尺度局部克重 CV；**整个多束阻隔论证由这一个数驱动**） |

### Finding 1–5 发现 1–5

| Finding 发现 | Number 数值 | Note 备注 |
|---|---|---|
| 1 · Attenuation 拉伸 | melt viscosity only changes how fast velocity-matching is reached（2.4 mm from tip at 285 °C；2.7 mm at 250 °C） | 三曲线重叠 |
| 1 · Levers to 1.5 µm | g/hole/min 0.73 → 0.20（fixed line output → 35 → 130 hpi）；jet 150 → 250 m/s buys 2.85 → 2.21 µm then saturates；tip temperature, MFR and hole diameter move nothing | — |
| 2 · Pressure wall 压力墙 | 450 MFR at conventional tip temperature crosses the die-tip pressure limit at about **160 hpi** | 常规解：MFR 提到 1200（损 Mv/熔体强度/成形 CV）；主体升到 300 °C+（热剂量陡增）；**只加热模头**（同样泄压，暴露 4–20 ms 而非 480 s） |
| 3 · Polymer ageing 聚合物老化 | capillary raises the degradation rate by 8× at 320 °C but shortens exposure by 80,000× → product negligible | 省下的热预算三种用法：跑 450 MFR（更高 Mv、更少断头/飞絮）、劈半抗氧剂（700–800 → 350 ppm 受阻酚）、多容忍一次热历史（回收边料） |
| 4 · Structure 结构 | SMMSMMS = same beams, same 12 gsm MB, same barrier, **+8 gsm and 27 % more cost** | 仅机械活化区值得用内层纺粘锚定抗分层 |
| 4 · Breathability 透气 | WVTR 18,000 g/m²/day vs 3,000 for film；air permeability 52 L/m²·s vs effectively zero | 对流干燥而非仅扩散干燥 = 真正的消费者收益 |
| 5 · Multi-beam 多束 | 1 beam 15 % CV → 44 % weight retained at weakest patch；4 beams → 72 %；+64 % barrier | 图上 3/4/5/6 束约 138 / 155 / 171 / 176（口径见表注） |

### Design · material 设计·材料

| Component 组分 | Specification 规格 | Level 用量 | Rationale 理由（原文） |
|---|---|---|---|
| Base resin 基础树脂 | Metallocene PP homopolymer，reactor-grade 茂金属 PP 均聚（聚合直出） | 450 g/10 min | Not peroxide-visbroken；narrow PDI 2.2–2.6 → uniform attenuation；no peroxide residue to seed further scission at the hot tip |
| Callback resin 回退树脂 | Same family, higher flow 同族更高流动 | 900 g/10 min | Drops die pressure 22 %；只在激光模头未投用时使用——代价是熔体强度与成形 CV |
| Hydrophobic additive 疏水助剂 | PFAS-free alkyl-modified polyolefin masterbatch 无氟烷基改性聚烯烃母粒 | 2.0 wt % | Advancing water contact angle 105° → 118–122°；worth about 35 % on hydrohead；成本 3.5 EUR-c/kg；no C6 fluorochemistry |
| Primary antioxidant 主抗氧剂 | Hindered phenolic（Irganox 1010 type）受阻酚 | 350 ppm | Halved from a conventional 700–800 ppm load because the melt path runs 40 K cooler；fewer extractables on a skin-adjacent article |
| Secondary antioxidant 辅抗氧剂 | Phosphite（Irgafos 168 type）亚磷酸酯 | 500 ppm | Protects during the short high-temperature excursion in the capillary；phosphite for a spike, phenolic for the long soak |
| Acid scavenger 酸吸收剂 | Hydrotalcite（DHT-4A type）水滑石 | 250 ppm | Replaces calcium stearate；Ca-stearate is the single largest source of die drool and plate-out on a hot tip — unacceptable at 300 °C |
| Nucleating agent 成核剂 | None in the meltblown beams | — | Nucleation raises crystallisation temperature and freezes the filament earlier, shortening the attenuation window；nucleate spunbond beams only |
| Slip / antistat 爽滑/抗静电 | None | — | Migratory amides destroy the hydrophobic surface and contaminate the die tip |

### Design · hardware 设计·硬件

| Parameter 参数 | Value 数值 | Basis 依据 |
|---|---|---|
| Laser zones 激光分区 | 32 independently driven CD segments of 100 mm；976 nm diode bars；DLC absorbing coating on the last 3 mm of the nose | base tip load by induction；laser trims ±10 K |
| Capillary density 孔密度 | 130 hpi（production point） | 1.94 µm at 60 kg/h·m |
| Strength density 高强档 | 160 hpi | 1.75 µm, 55 bar with the laser tip |
| Callback density 回退档 | 100 hpi | 2.21 µm, safe on any existing beam |
| Capillary diameter 孔径 | 0.130 mm | hole α tracks density to hold land ratio |
| L/D ratio | 15 | 6 × τv entrance loss included in 51 bar |
| Throughput per hole 每孔产量 | 0.195 g/min | **the variable that actually sets diameter** |
| Wall shear rate 壁面剪切速率 | 20,400 s⁻¹ | inside the shear-thinning plateau |
| Capillary residence 毛细管停留 | 5.9 ms | why the hot tip costs almost no degradation |
| Tip temperature 模头温度 | 300–320 °C | decoupled from a 245 °C distribution beam |
| Primary air 一次风 | 250 m/s at 290 °C | above 300 m/s the diameter gain saturates |
| Die-to-collector 模头-收集距离 | 180–220 mm | long enough to lay down without shot |
| Enthalpy to lift 192 kg/h by 55 K 提升 192 kg/h 55 K 的焓 | 13.3 kW（whatever the heater） | 不可回避的能量账单 |
| Diode array watt density 二极管阵列功率密度 | 4 kW/m on the last 3 mm of a 60° nose | 药筒塞不进 60° 鼻尖最后 3 mm |
| Recommended hybrid build 推荐混合构型 | resistive/induction base + laser apex/trim ≈ **2 kW** laser（not 13 kW） | PP transparent at 976 nm；beam cannot travel down a 0.13 mm capillary；absorbing coating → conduction over the last 2 mm |

### Design · structure 设计·结构（SMMMS 30 gsm）

| Layer 层 | Spec 规格 |
|---|---|
| S1 spunbond 纺粘 | 9 gsm, 1.8 dpf, 35 MFR mPP + nucleator |
| M1–M4 meltblown 熔喷 | 3.0 gsm each, 1.5 µm, 450 MFR mPP |
| S2 spunbond 纺粘（body side 贴身侧） | 9 gsm, 1.8 dpf |
| Calendar bond 热轧粘合 | 16 % area, 0.35 mm² dots, 148/150 °C（低粘合面积是有意的：每个粘点都是刚性无孔岛，对阻隔零贡献、对粗糙感全贡献；16 % 是仍能通过转化张力的下限） |

| Property 性能 | Target 目标 | Status 状态 |
|---|---|---|
| Hydrohead, clean 静水压·清水 | ≥ 130 mbar | 141 modelled |
| Hydrohead, synthetic urine 静水压·合成尿 | ≥ 110 mbar | 121 modelled |
| Air permeability 透气量 | 40–65 L/m²·s | 52 modelled |
| WVTR | ≥ 12,000 g/m²·d | ≥ 18,000 |
| Basis weight 克重 | 30 ± 1.5 gsm | — |
| MD tensile MD 拉伸 | ≥ 32 N / 50 mm | spunbond-carried |
| CD elongation CD 伸长 | ≥ 55 % | spunbond-carried |
| Formation CV per beam 单束成形 CV | ≤ 15 % at 1 mm² | **gates everything above** |
| Handle-o-meter 柔软度 | ≤ 0.9 × film laminate | softness claim |
| Opacity 遮盖率 | ≥ 88 % | no TiO₂ needed — meltblown scatters |

### Commercial reality 商业现实

| Item 项目 | Value / Conclusion 数值 / 结论 | Note 备注 |
|---|---|---|
| Cost vs incumbent 相对现有方案 | SMMMS lands **within 5 %** of the incumbent — not cheaper, not a blocker | 图轴数值 11.02 / 8.26 `[口径待确认]` |
| Lamination adhesive 复合胶 | film route carries 1.8 EUR-cents that the all-nonwoven route does not | strip it out → gap closes to **under 1 %** |
| Mono-material PP 单一材质聚丙烯 | removes the PE/PP split that blocks mechanical recycling of the chassis | "the strategic prize, worth more than the 0.4 cents" |
| Two extra meltblown beams 多两束熔喷 | capital and floor space；new composite line = configuration choice；existing SMS line = rebuild | modular beam inserts between spunbond beams = realistic retrofit |
| Line speed exposure 线速暴露 | meltblown is the slowest beam；4 beams at 3 gsm means the meltblown section sets the ceiling | model line balance before the material |
| Odour 气味 | 52 L/m²·s air permeability lets ammonia out as freely as vapour | **unpriced risk**；no model predicts consumer response — needs a panel, early |

### Roadmap 阶段计划（with explicit kill criteria 带明确终止判据）

| Stage 阶段 | Timeline 周期 | Content 内容 | Kill criterion 终止判据 |
|---|---|---|---|
| Bench 台架 | 0–3 mo | pilot 4-beam laydown at 3 gsm/beam, 1.5 µm；measure formation CV at 1 mm²；hydrohead vs surface tension curve 33–72 mN/m | KILL if formation CV > 20 % per beam, or hydrohead at 66 mN/m below 90 mbar |
| Die tip 模头 | 3–9 mo | single-zone laser nose on a 400 mm lab die, 130 hpi；melt-path GPC and MFR before/after at 245 vs 285 °C；die drool and plate-out over 200 h at 320 °C tip | KILL if measured MFR drift reduction < 30 %, or drool forces cleaning more than weekly |
| Product 产品 | 9–18 mo | zoned backsheet on converting trial, film strip in crotch lane；contamination panel（BM, wipe residue, barrier cream）；odour panel first | KILL if the odour panel is negative against the film control |
| Scale 放大 | 18–30 mo | CD-zoned laser array, 32 segments over 3.2 m；line balance study；mono-material recycling claim substantiation | GO/NO-GO on cost parity at full line speed, not at pilot speed |

### Honest limits 作者自陈局限（原文）

| Limit 局限 | Consequence 后果 |
|---|---|
| Whipping factor Λ = 6 is a **fitted** constant | absolute diameters move by ±20 % if the real arc-length ratio is 4 or 9；the "temperature does not change diameter" conclusion is robust, the absolute numbers are not |
| Formation CV = 15 % is **assumed, not measured** | it drives the entire multi-beam argument；at 10 % single-beam SMS looks far better and the four-beam case weakens |
| Contamination transport was **not modelled** | slide 11 shows hydrohead at low surface tension, not whether bile salts or lotion actually reach the backsheet；it is an experiment, and it decides the crotch zone |
| Fibre diameter distribution collapsed to a mean | real meltblown is log-normal with CV ≈ 0.5, and the coarse tail is where shot and large pores live；a mean model flatters barrier |
| Laser coupling efficiency is a guess | 55 % absorption into a coated nose is plausible but unvalidated；at 35 % the hybrid case holds；at 20 % the laser stops being worth its capital against induction |
| No creep or wet-collapse model | under sustained sitting load the web compacts, solidity rises and pores shrink（helps barrier）but bond points concentrate stress — neither effect is in the numbers |

> 🔴 **manual_review（2026-09-29）**：本资料含**具体原料规格与成本单价（疏水母粒 3.5 EUR-c/kg）、成本对标结论（相对现有方案 ±5%、去胶后 <1%）、模头与主机改造档位（130/160/100 hpi、32 分区激光阵列）及项目终止判据**。其中**喷丝板孔密度档位、激光分区数与终止判据**属我方工艺配置与项目决策参数，依 AGENTS.md §5 **列为需人工确认后方可对外引用**；本页只保留用于技术判断的数值，**不页面化任何供应商报价或合同条款**。原文完整内容留存于 `RAW/ima_sync/个人知识库/WKB/Projects/Film/Laser_Meltblown_Film_Free_Backsheet.pptx - 已修复.pptx.md`。

## Key Claims（key_claims）

- **Fibre fineness is bought with throughput per hole and jet velocity, not with temperature.** —— 支撑页：[[Meltblown Nonwoven（熔喷非织造布）]]
- **Thermal decoupling of the die tip is the real benefit of the laser**, because degradation is dose = rate × time and the capillary shortens the time by 80,000×. —— 支撑页：[[Laser-Assisted Die Tip（激光辅助模头）]]、[[熔融指数与化学降解]]
- **Barrier is formation-limited**, so beam count and local basis-weight CV — not median pore size — set hydrohead. —— 支撑页：[[Formation-Limited Barrier（阻隔的成形受限机理）]]
- **The answer is zoning, not replacement**：film is unbeatable under contamination and peak sitting load. —— 支撑页：[[Film-Free Backsheet（无膜背层）]]、[[SMMMS Film-Free vs Microporous Film Backsheet（无膜背层 vs 微孔膜背层）]]
- **SMMSMMS buys nothing but 8 gsm and ~27 % cost** unless the web is mechanically activated. —— 支撑页：[[SMMMS vs SMMSMMS（成本·性能·供应链）]]

## Related Pages 关联页面

- Concepts 概念：[[Meltblown Nonwoven（熔喷非织造布）]]、[[Film-Free Backsheet（无膜背层）]]、[[Formation-Limited Barrier（阻隔的成形受限机理）]]、[[Laser-Assisted Die Tip（激光辅助模头）]]、[[SMS复合结构]]、[[熔融指数与化学降解]]、[[茂金属聚丙烯]]
- Comparisons 对比：[[SMMMS Film-Free vs Microporous Film Backsheet（无膜背层 vs 微孔膜背层）]]、[[SMMMS vs SMMSMMS（成本·性能·供应链）]]、[[无纺布五大工艺对比]]
- Sibling project directory 同目录项目：`RAW/ima_sync/个人知识库/WKB/Projects/Film/`

## Source 原文

- Local path 本地路径：`RAW/ima_sync/个人知识库/WKB/Projects/Film/Laser_Meltblown_Film_Free_Backsheet.pptx - 已修复.pptx.md`
- Original link 原文链接：（无；内部资料）
- Source file size 源文件大小（源 front matter 记录）：8 MB（PPTX 提取）

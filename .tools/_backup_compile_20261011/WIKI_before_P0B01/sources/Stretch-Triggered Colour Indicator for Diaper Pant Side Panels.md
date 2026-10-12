---
type: source
title: "Stretch-Triggered Colour Indicator for Diaper Pant Side Panels"
source_type: 技术方案（内部 R&D 概念研究）
source_path: RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Stretch-Triggered Colour Indicator for Diaper Pant Side Panels.pptx.md
original_link: ""
date_published: 2026
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "The literature answer fails on the line: mechanophores and photonic crystals cannot pass a hot-melt applicator; a geometry-gated optical mask succeeds（中文：文献答案过不了产线——机械力致变色分子与光子晶体无法通过热熔涂布机；几何光学掩膜可行）"
  - "All-in add-on cost ≈ US$0.90 per 1,000 pants (0.09 ¢/pant) with US$38 k new capex, one shim, no new station and zero new chemistry classes（中文：全含新增成本约 US$0.90/千片，capex 3.8 万美元，仅一块垫片，不新增工位、不引入新化学品类别）"
  - "Three separable states at 38 / 67 / 101 % panel strain, ΔE*ab > 18 between states, fully reversible because the mechanism is geometric, not fracture（中文：面板应变 38/67/101% 三个可分辨状态，状态间 ΔE*ab＞18；机制为几何遮光而非断裂，故完全可逆）"
  - "Panel elongation is a usable proxy for force, but the panel band is not the red-mark source: at 101 % strain it delivers only ~4.3 mmHg against a 20–30 mmHg sustained capillary-occlusion threshold（中文：面板伸长可替代力读数，但面板本身非红印来源——101% 应变仅约 4.3 mmHg，远低于 20–30 mmHg 持续毛细血管闭塞阈值）"
  - "The control point is upstream: thresholds are set by the incoming laminate's pre-stretch ratio and relaxed corrugation pitch, so SPC belongs on the panel supply, not the coater（中文：控制点在来料——阈值由层压预拉伸比与松弛波纹间距决定，SPC 应放在面板来料而非涂布机）"
  - "K-C disclosed the umbrella concept (US 7,704,589 B2, adjusted expiry 2026-10-04) — free to practise, but not patentable as a concept（中文：K-C 已公开上位概念专利（2026-10-04 到期）——可自由实施，但概念本身不可专利）"
pages_linked: ["[[Geometric Optical Mask（几何光学掩膜）]]", "[[TB-A Opaque Mask Hot Melt（TB-A 遮光热熔胶）]]", "[[Panel Hysteresis and Threshold Calibration（面板回滞与阈值标定）]]", "[[Skin Contact Pressure（皮肤接触压力）]]", "[[Mechanophore Mechanochromism（机械力致变色分子）]]", "[[Structural Colour Mechanochromism（结构色力致变色）]]", "[[Hot-Melt Slot Coating（热熔狭缝涂布）]]", "[[Mechanochromic Routes Comparison（力致变色技术路线对比）]]", "[[Kimberly-Clark（金佰利）]]", "[[Mechanochromic变色纤维]]"]
---

# Stretch-Triggered Colour Indicator for Diaper Pant Side Panels

## One-line Positioning 一句话定位

The engineering deep-dive behind the pull-strain fit meter on elastic side panels — it fixes the seven hard requirements, screens seven mechanochromic families, and lands on a single-pass slot-coated **geometric optical mask** with cost, safety and FTO closed out. This is the most implementation-complete document of the Mechanochromic block.

（中文：弹性侧片「拉伸式合身指示器」的工程深化报告——定下 7 条硬约束、筛查 7 大变色族，最终落到「单道狭缝涂布 + 几何光学掩膜」方案，并把成本、安全与 FTO 一并向内闭环。是本批 Mechanochromic 落地度最高的一份。）

## Summary 摘要

The brief fixes seven requirements: discrete strain-keyed colour states (not a smooth fade), compatibility with the installed HMA slot die (140–170 °C, 20–70 bar, 2–8 k s⁻¹ shear), a force-relevant reading, baby-safe outer-face chemistry (EN 71-3 Cat III, REACH, CPSIA), one printing pass, reversibility over tens of don/doff cycles, and < 0.2 ¢/pant all-in.

Part One proves strain is a usable proxy for force: for a 2.2× SEBS laminate, 38 / 67 / 101 % panel strain map to 1.4 / 2.5 / 3.9 N retraction force; converting tension to skin pressure (P = T/(r·w)) shows a broad 85 mm panel delivers only ~4.3 mmHg at 101 % strain, so the panel band is **not** the red-mark source — the risk is the ~10 mm waist elastic downstream, which reaches ~20–29 mmHg. Hence the indicator is positioned as a **fit and containment guide, never a pressure-safety claim**.

Part Two screens seven families against applicator, cycle life, cost and tox. Only the geometric optical mask survives (TRL 8, native slot-coatable, 1.0× cost index, no new tox package); craze/cavitation whitening is Phase 2 (1.4×), interference pigment is backup (3×); polymer opal (25×), stretchable DBR (15×), cholesteric LCE (40×) and molecular mechanophores (60×) are rejected — the latter because ~240 pN per bond demands covalent incorporation into a cross-linked network, fades after ~3 cycles, and cannot survive a hot melt.

Part Three specifies the selected design: the elastic laminate's own corrugation (2.2× bonded, 1.2 mm relaxed pitch) acts as a mechanical shutter under a rigid, CD-zoned opaque hot melt (TB-A). One equation, φ(ε) = 1 − 2a/[λ₀(1+ε)], sets all three thresholds, and the three coat weights (7.5 / 9.0 / 11.0 g/m²) come from one shim whose land lengths (18.0 / 15.0 / 12.0 mm) give a 1.00 : 1.20 : 1.50 flow ratio — within 2 % of the required 1.00 : 1.20 : 1.47.

Part Four covers the process: contact slot die, 200 µm shim (a 100 µm gap would have driven 165 bar and stalled the pump), 400 m/min, 12 °C chill roll, 0.4 s dwell, and a full setpoint table. Sensitivity analysis concludes that three variables matter (panel lamination pre-stretch, coat weight, web tension) and melt viscosity is self-compensating.

Part Five closes cost (US$0.90/1,000 pants, US$38 k capex, 1:4 versus a typical wetness-indicator stripe), safety ("nothing new": every component already sits in diaper construction adhesives or printed backsheets), FTO (K-C US 7,704,589 B2 lapsed, adjusted expiry 2026-10-04 → free to practise, novel only in the coating architecture), a risk register, a measurement protocol (ΔE*ab = 6 crossing on the cycle-2 retraction branch) and a 24-week four-gate plan.

（中文摘要：报告先立 7 条硬约束（离散应变色态、兼容现有热熔狭缝模头、与力相关、婴儿安全外表面、单道印刷、数十次可逆、<0.2 ¢/片）。第一部分证明应变可替代力读数：2.2× SEBS 层压件在 38/67/101% 应变下回弹力为 1.4/2.5/3.9 N；换算皮肤压力后宽 85 mm 面板仅约 4.3 mmHg，故面板非红印来源，风险在约 10 mm 腰弹性体（约 20–29 mmHg），产品定位只能是「合身与防漏指引」而非压力安全声明。第二部分筛查 7 大变色族，仅几何光学掩膜存活（TRL 8、天然可狭缝涂布、成本指数 1.0×、无新毒理包），空洞化增白列为 Phase 2，干涉颜料为后备，聚合物蛋白石/可拉伸 DBR/胆甾相 LCE/分子力致变色均被否决。第三部分给出选定设计：利用弹性层压件自身 1.2 mm 波纹作机械快门，覆以刚性分区分重遮光热熔胶 TB-A，一个方程定三个阈值，一块垫片经 18/15/12 mm 台面长度给出 7.5/9.0/11.0 g/m² 三档涂布量。第四部分给出工艺窗口与全套设定值。第五部分收口成本、安全、FTO、风险、测量方法与 24 周四门径计划。）

## Extracted Numbers and Conclusions 提炼的数字与结论

### A. Requirements and cost 需求与成本

| Item 项目 | Value 数值 / 结论 | Note 备注 |
|---|---|---|
| Panel strain design points 面板应变设计点 | 38 / 67 / 101 % → 1.4 / 2.5 / 3.9 N retraction force（回弹力） | 85 mm panel, 2.2× SEBS laminate |
| Industry elastic-panel design window 行业设计窗 | 250–500 gf at 6–19 mm extension | 替代口径 |
| Skin pressure at 101 % strain | ~4.3 mmHg | 远低于 20–30 mmHg 持续闭塞阈值 |
| Skin pressure, 10 mm waist elastic @ 2.5 N | ~29 mmHg | **真正的红印来源** |
| Hysteresis 回滞 | 35–55 % for an SEBS panel（100 % 应变下拉力 5.2 N vs 持续佩戴 3.9 N） | 须按卸载支校准 |
| Stress relaxation 应力松弛 | 首小时损失 12–20 % 张力 → 「正确」带需 30 点宽 | [[Panel Hysteresis and Threshold Calibration（面板回滞与阈值标定）]] |
| Add-on cost 新增成本 | US$0.90 / 1,000 pants = 0.09 ¢/pant | 441 M 片/年、1,200 ppm、70 % OEE、capex 3 年摊销 |
| Cost ratio 成本比 | 1 : 4 vs a typical wetness-indicator stripe | — |
| New capex 新增资本支出 | US$38 k（3 区垫片+模体 14 k、冷却辊+冷水机 16 k、线扫视觉 8 k） | — |
| TiO₂ share of ink cost | 43 % | TiO₂-free 变体 5.20 US$/kg，但对比度降至 0.79 |

（中文：成本 0.09 美分/片，为常规尿显条的 1/4；新增 capex 3.8 万美元；回滞 35–55%、首小时应力松弛 12–20%，故「正确」带须 30 点宽。）

### B. Technology screening 技术路线筛查

| Family 族 | Mechanism 机理 | Usable strain | Reversible | Slot-coatable | Cost idx 成本指数 | New tox pkg | TRL | Verdict 裁决 |
|---|---|---|---|---|---|---|---|---|
| Geometric optical mask 几何光学掩膜 | Opaque print un-covers printed under-colour by area | 10–150 % | ∞ cycles | Native | 1.0× | None | 8 | **SELECT 选用** |
| Craze / cavitation whitening 空洞化增白 | Interfacial debond → Mie scatter | 40–120 % | Thermal reset | Yes | 1.4× | Minor | 5 | Phase 2 |
| Interference pigment 干涉颜料 | Mica-TiO₂ flake re-orientation | 30–200 % | Yes | Yes | 3× | Minor | 4 | Backup 后备 |
| Polymer opal / colloidal PC 胶体光子晶体 | Bragg peak blue-shift, 127 nm demonstrated | 0–60 % | > 100 cyc | Needs shear ordering | 25× | Minor | 3 | Watch |
| Stretchable DBR | Multilayer Bragg stack, NIR → visible | 0–50 % | Yes | Co-extruded film | 15× | Minor | 3 | **Reject** |
| Cholesteric LCE 胆甾相液晶弹性体 | Helix pitch compression | > 100 % for full sweep | Yes | Alignment + UV cure | 40× | Full package | 2–3 | **Reject** |
| Molecular mechanophore 分子机械力致变色 | C–O scission → merocyanine, ~240 pN/bond | Network-dependent | ~3 cycles | Must be covalent | 60× | Full package | 2 | **Reject** |

> Cost index = delivered cost per pant relative to the geometric mask baseline; TRL assessed for a 1,200 ppm variable-hygiene context.
> （中文：成本指数以几何掩膜为 1.0× 基准；TRL 按 1,200 ppm 卫品产线口径评估。）

### C. Selected design parameters 选定设计参数

| Parameter 参数 | Value 数值 | Note 备注 |
|---|---|---|
| Mask modulus 掩膜模量 | ≈ 85 MPa（约 40× panel） | 刚性快门而非可拉伸膜 |
| Modulus ratio 模量比 | ≥ 35 : 1 (ink : panel) | **保读出的关键规格** |
| Zone widths 分区宽度 | 3 × 18 mm = 54 mm coated width | 分区由垫片加工定型 |
| Target strain ε* per zone | 38 / 67 / 101 % | 对应第一绿条/第二绿条/红条 |
| Required ink arc 2a per zone | 1.39 / 1.68 / 2.03 mm | Arc coverage 53 / 64 / 77 % |
| Coat weight per zone | 7.5 / 9.0 / 11.0 g/m² | Ratio fixed by land length, ± 0.6 g/m² |
| Shim land length 垫片台面长度 | 18.0 / 15.0 / 12.0 mm | Flow ∝ 1/L → 1.00 : 1.20 : 1.50 |
| Relaxed corrugation pitch λ₀ | 1.2 mm（2.2× laminate） | 由来料提供 |
| Visual threshold φ* | 0.30（validated by ΔE*ab ≥ 6） | 约 3 个恰可辨差 |
| Threshold tolerance 阈值允差 | 38 / 67 / 101 % ± 7 pts | ΔE*ab = 6 交点，第 2 循环卸载支 |
| State separation 状态分离度 | ΔE*ab ≥ 18 | 强制分离度 |
| Cycle durability 循环耐久 | 20 don/doff cycles to 100 % → drift ≤ ±8 pts | — |
| Wear hold 佩戴保持 | 8 h @ 33 °C / 85 % RH @ 67 % strain → drift ≤ ±5 pts | — |
| Wet robustness 耐湿 | 4 h synthetic urine soak (0.9 % NaCl) → ΔE change ≤ 3 | — |

（中文：模量比 ≥35:1 是保护读出的关键；三区 3×18 mm，涂布量 7.5/9.0/11.0 g/m² 由垫片台面长度比固定；阈值 38/67/101% ±7 点，状态分离 ΔE*ab≥18。）

### D. Process setpoints 工艺设定值（节选）

| Parameter | Setpoint / tolerance | Control note |
|---|---|---|
| Melt tank 熔胶罐 | 155 ± 3 °C | 48 h max hold; auto-purge at stops > 90 s |
| Hose 软管 | 158 ± 3 °C | 升温剖面防冷胶段 |
| Manifold 模头歧管 | 160 ± 2 °C | Sets the 2,900 mPa·s design viscosity |
| Die / shim | 162 ± 2 °C | 高于歧管 2 °C，消除边缘条纹 |
| Pump speed 泵速 | 576 rpm ± 2 % | **唯一的涂布量变量，须做 SPC** |
| Manifold pressure | 34.8 ± 4 bar | 上升趋势 = 滤网堵塞而非黏度 |
| Die gap (shim) | 200 ± 5 µm | 由压降驱动，非膜厚驱动 |
| Web speed 车速 | 400 m/min（250–500） | — |
| MD web tension | 25 ± 3 N/m | 高于 40 N/m 会把波纹拉平 |
| Chill roll 冷却辊 | 12 ± 2 °C，180° wrap | 0.4 s dwell |
| Max downstream nip | 0.5 bar | 超过则掩膜涂抹、阈值偏低 |

（中文：熔胶罐 155 ℃、歧管 160 ℃、模头/垫片 162 ℃；泵速 576 rpm 是唯一涂布量变量；垫片间隙 200 µm；MD 张力 25 N/m，>40 N/m 会拉平波纹。）

## Key Claims 关键论断

- **几何遮光优于任何变色化学** —— 过不了热熔涂布机与数十次循环，是文献方案的共同死因。支撑页：[[Geometric Optical Mask（几何光学掩膜）]]、[[Mechanochromic Routes Comparison（力致变色技术路线对比）]]
- **面板伸长可用，但面板不是压迫源** —— 指示器只能定位为合身/防漏指引。支撑页：[[Skin Contact Pressure（皮肤接触压力）]]
- **阈值标定必须落在卸载支（回弹曲线）** —— 否则舒适度被高估约 30 %。支撑页：[[Panel Hysteresis and Threshold Calibration（面板回滞与阈值标定）]]
- **控制点在上游来料** —— 预拉伸比与松弛波纹间距须写进面板采购规格（Cpk ≥ 1.33 + 逐批证书）。支撑页：[[Geometric Optical Mask（几何光学掩膜）]]
- **不新增任何化学品类别** —— 全部组分已存在于纸尿裤结构胶或印刷底膜中。支撑页：[[TB-A Opaque Mask Hot Melt（TB-A 遮光热熔胶）]]

## Related Pages 关联页面

- Concepts 概念：[[Geometric Optical Mask（几何光学掩膜）]]、[[TB-A Opaque Mask Hot Melt（TB-A 遮光热熔胶）]]、[[Panel Hysteresis and Threshold Calibration（面板回滞与阈值标定）]]、[[Skin Contact Pressure（皮肤接触压力）]]、[[Mechanophore Mechanochromism（机械力致变色分子）]]、[[Structural Colour Mechanochromism（结构色力致变色）]]、[[Hot-Melt Slot Coating（热熔狭缝涂布）]]
- Entities 实体：[[Kimberly-Clark（金佰利）]]
- Comparisons 对比：[[Mechanochromic Routes Comparison（力致变色技术路线对比）]]
- Existing pages 既有页：[[Mechanochromic变色纤维]]、[[变色油墨]]、[[智能尿裤功能层]]

## Source 原文

- Local path 本地路径：`RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Stretch-Triggered Colour Indicator for Diaper Pant Side Panels.pptx.md`
- Original link 原文链接：（无；内部资料）
- Date note 日期说明：文档未标注发布日期，参考同族文档（2026-08-02 / 2026-08-19）标为 2026，精确月份 `[待验证]`。
- Sibling documents 同族文档：[[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]]、[[Mechanochromic Materials Technical Review（EN v3, 2026-08）]]

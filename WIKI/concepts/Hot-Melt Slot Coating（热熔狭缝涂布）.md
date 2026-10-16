---
type: concept
title: "Hot-Melt Slot Coating（热熔狭缝涂布）"
domain: [卫材研发, 表面处理与胶黏剂]
status: growing
updated: 2026-09-29
tags: [热熔胶, 狭缝涂布, 流变, Cross指数, 压降, 冷却辊, 垫片]
---

# Hot-Melt Slot Coating（热熔狭缝涂布）

> One-line definition 一句话定义：Applying a molten adhesive through a **slot die** onto a moving web — in this library it is the shared delivery platform for both blocks: three CD-zoned indicator stripes for the fit meter, and a contact-mode single lane for the BM indicator on a composite breathable backsheet.
> （中文：通过**狭缝模头**把熔融胶涂覆到移动幅材上——在本库中它是两个项目共用的涂布平台：合身指示器的三条 CD 分区条带，以及复合透气底膜上便指示器的接触式单通道。）

## Mechanism / Structure 机理 / 结构拆解

1. **The governing slot equations（狭缝的支配方程）**：wall shear rate = 6Q/(w·t²); pressure drop over the land ΔP = 12·η·Q·L/(w·t³). **Pressure scales with 1/t³ — so halving the shim to gain a crisper edge multiplies die pressure by eight.**
2. **Zoning without control loops（无需控制回路的分区）**：flow through a rectangular land is Q ∝ ΔP·g³·b/(12·η·L). With g, b and ΔP common to all zones, the ratio is purely **1/L**. Land lengths machined to ± 0.05 mm fix the coat-weight ratio to better than 1 % for the life of the shim; a viscosity excursion moves all zones together, so the ratio (and therefore the thresholds) is self-compensating. **Absolute** coat weight is set by pump rpm — one variable, one setpoint, one SPC chart.
3. **Design the melt near-Newtonian, on purpose（刻意把熔体设计成近牛顿流体）**：in the slot the melt sees 9,000–40,000 s⁻¹. A strongly shear-thinning hot melt loses more than half its viscosity there and then recovers on the web — and that mismatch is what produces ribbing and edge bleed. Published slot-die work shows shear-thinning fluids roughly **double** the minimum stable wet thickness versus a Newtonian fluid at the same capillary number, while shear-thickening fluids reduce it by ~10 %. Hence specify the Cross index, not just the Brookfield number: **n ≥ 0.85**, λ ≤ 2 × 10⁻⁴ s → practically a wax-and-rosin matrix with no high-MW styrenic block copolymer.
4. **Contact mode is mandatory at this capillary number（此毛细数下必须接触式）**: Ca = ηV/σ = 272 at 400 m/min and 125 °C, deep in the high-Ca regime where viscocapillary theory says minimum wet thickness plateaus at t/H ≈ 0.45–0.55. With a required wet film h = 22.2 µm, the maximum free gap is H ≤ 44 µm — and **a 44 µm free span on a diaper line is not achievable; web flutter alone is ±150 µm**. Specify instead: contact (wiped) slot nozzle, chilled backing roll 15–20 °C, servo-metered speed-following gear pump, bead-on-demand valve, nozzle contact pressure 2–4 N/cm.
5. **Thermal load is set by the substrate, not the chemistry（热负荷由基材而非化学决定）**：the contact interface reaches 69 °C at a 125 °C melt (comfortable), but the **bulk equilibrium temperature** of coating plus film reaches 85 °C at 125 °C and 90 °C at 135 °C. A microporous CaCO₃-filled PE film loses WVTR irreversibly once the drawn structure anneals, typically above 90 °C — **you will not see it on the line; you will see it in the humidity chamber a week later.** A chilled backing roll moves the ceiling up by ~15 K.
6. **Corrugation-gated coating needs low web tension（波纹门控涂布需要低幅材张力）**：in the fit-meter application the incoming laminate is relaxed and gathered at the coater, and MD tension above 40 N/m pulls the corrugation out before the die — hence MD 25 ± 3 N/m with a hard alarm.
7. **What stays unchanged（保持不变的部分）**：both projects deliberately target a formulation and a setpoint that sit inside the normal envelope of a standard diaper hot-melt system — melter platform, controller, hose architecture, gear-pump technology and pressure class — so the trial risk sits in the incoming web, not in the coater.

（中文：①支配方程——壁面剪切率 6Q/(w·t²)，台面压降 ΔP=12ηQL/(w·t³)，**压降 ∝1/t³，垫片减半则模头压力×8**；②无控制回路分区——矩形台面流量 Q∝ΔP·g³·b/(12ηL)，在 g、b、ΔP 相同时比值纯为 1/L；台面机加工 ±0.05 mm 使涂布量比值在垫片寿命内优于 1%，黏度波动时三区同向移动而自补偿；**绝对**涂布量由泵速设定——一个变量、一个设定点、一张 SPC 图；③刻意近牛顿——熔体在狭缝中承受 9,000–40,000 s⁻¹ 剪切，强剪切变薄的热熔胶在此处损失一半以上黏度、到幅材上再恢复，这种错配正是条纹与边缘溢流的来源；文献显示同毛细数下剪切变薄流体的最小稳定湿膜厚约为牛顿流体的**两倍**，而剪切增稠流体降低约 10%；故须规范 Cross 指数而非只看 Brookfield 值：n ≥ 0.85、λ ≤ 2×10⁻⁴ s——实践上即「蜡+松香基体、不含高分子量苯乙烯嵌段共聚物」；④此毛细数下必须接触式——400 m/min、125 ℃ 下 Ca=272，深处高 Ca 区，粘毛细理论在此最小湿膜厚平台为 t/H≈0.45–0.55；要求湿膜 h=22.2 µm 时最大自由间隙 H≤44 µm，而**纸尿裤产线上 44 µm 的自由跨距不可能实现——仅幅材抖动就 ±150 µm**；故须指定接触（刮涂）式狭缝喷嘴 + 15–20 ℃ 冷却背辊 + 伺服随速齿轮泵 + 按需胶珠阀 + 2–4 N/cm 接触压；⑤热负荷由基材决定——接触界面在 125 ℃ 熔体下 69 ℃（舒适），但涂膜+膜的本体平衡温度在 125 ℃ 时 85 ℃、135 ℃ 时 90 ℃；微孔 CaCO₃ 填充 PE 膜在约 90 ℃ 以上退火即不可逆损失 WVTR，**线上看不出来，一周后的恒温恒湿箱里才发作**；加冷却背辊可把上限抬高约 15 K；⑥波纹门控涂布需低张力——涂布处来料处于松弛收拢态，MD 张力高于 40 N/m 会在到模头前把波纹拉平，故取 25±3 N/m 并设硬报警；⑦不变的部分——两个项目都刻意把配方与设定点落在标准纸尿裤热熔系统的常规包络内（熔化平台、控制器、软管架构、齿轮泵技术与压力等级），使试产风险落在来料而非涂布机上。）

## Key Parameters 关键参数表

### A. Fit-meter line 合身指示器产线（3 区，非接触需求下的接触式）

| Parameter 参数 | Setpoint / value | Source 出处 |
|---|---|---|
| Melt tank 熔胶罐 | 155 ± 3 °C（48 h max hold；停机 > 90 s 自动清洗） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Hose 软管 | 158 ± 3 °C | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Manifold 歧管 | 160 ± 2 °C | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Die / shim 模头/垫片 | 162 ± 2 °C | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Gear pump 齿轮泵 | 0.30 cc/rev | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Pump speed 泵速 | 576 rpm ± 2 %（唯一的涂布量变量） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Volumetric delivery 体积流量 | 173 cm²/min ± 3 %（= 199 g/min @ 1.15 g/cm³） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Manifold pressure 歧管压力 | 34.8 ± 4 bar（上升趋势 = 滤网堵塞） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Filter 滤网 | 100 mesh, dual（ΔP > 6 bar 时不停线更换） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Coated width 涂布幅宽 | 54 mm（3 × 18 mm）± 0.5 | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Coat weight by zone | 7.5 / 9.0 / 11.0 g/m²（± 0.6） | [[Geometric Optical Mask（几何光学掩膜）]] |
| Die gap (shim) | 200 ± 5 µm（压降驱动，非膜厚驱动） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Die-to-web 模头—幅材 | contact, 6 ± 1° wrap | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Web speed 车速 | 400 m/min（250–500） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| MD web tension | 25 ± 3 N/m（> 40 N/m 拉平波纹） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Web temp at die | 22–28 °C（> 32 °C 掩膜下探过深） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Chill roll 冷却辊 | 12 ± 2 °C, 180° wrap, 0.4 s dwell | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Max downstream nip | 0.5 bar（超过则掩膜涂抹、阈值偏低） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Shim design 垫片 | 3-zone, 200 µm stainless, laser-cut, coat-hanger manifold, single feed 34.8 bar | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Shear rate / wall shear stress at 8,000 s⁻¹ | ΔP = 2τL/g, L = 15 mm | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Design decision recorded 记录的设计决策 | 100 µm 垫片会驱动 165 bar 并憋停泵 → 200 µm 间隙是本方案能跑起来的关键决策 | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |

### B. BM-indicator lane 便指示通道（接触式，排气底膜）

| Parameter 参数 | Setpoint / value | Source 出处 |
|---|---|---|
| Brookfield viscosity | 3,200 / 2,092 / 1,396 mPa·s（120 / 130 / 140 °C），spec band ± 18 % | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Cross index n | 0.88（spec n ≥ 0.85；10–50,000 s⁻¹ 毛细管流变仪 @ 125 °C） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Relaxation time λ | ≤ 2 × 10⁻⁴ s | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Flow activation energy | 56 kJ/mol | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Melt density / surface tension @ 125 °C | 0.90 g/cm³ / 30 mN/m | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Shim / land 垫片/台面 | 200 µm shim, 5 mm land, 10 mm lane | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Wall shear rate @ 400 m/min | 22,200 s⁻¹（黏度 1,225 mPa·s） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Pressure drop over land | 13.6 bar（系统上限 40 bar）；100 µm 垫片则 99.7 bar ✗ | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Melt throughput | 80 g/min | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Capillary number Ca @ 400 m/min, 125 °C | 272 | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Required wet film h | 22.2 µm（= 20 gsm ÷ 900 kg/m³） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Max free gap H | ≤ 44 µm（h ÷ 0.50）— 不可行 | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Application window | 115–132 °C（标称 125 °C） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Lower / upper limit | ≈112 °C（die pressure）；≈134 °C（film pore collapse）；viscosity floor ≈136 °C | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Chilled backing roll | 15–20 °C, hardened surface（+ ~15 K headroom） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Nozzle contact pressure | 2–4 N/cm | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Coat weight capability | 20 ± 3 gsm，Cpk ≥ 1.33 across 200–500 m/min | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Mandatory test 必修测试 | WVTR (ASTM E96) + hydrohead，coated vs uncoated，窗口内每一个设定点 | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |

> ⚠️ **No unsourced parameters**：以上全部来自本批源摘要页。**两种应用在同一产线上的切换时间与清洗（purge）损失**库内无数据 → `[待验证]`（原文仅提到 BM 通道须独立低温熔化罐、10 L、独立回路，且不得与温度通道共用软管）。

## Adjacent Concepts 相邻概念

- 涂布对象：[[Geometric Optical Mask（几何光学掩膜）]]、[[TB-A Opaque Mask Hot Melt（TB-A 遮光热熔胶）]]、[[Protein Error of pH Dye（pH 染料的蛋白误差）]]
- 既有页对照：[[热风粘合无纺布]]、[[REL增强层]]、[[无锑聚酯]]
- 数值判据：[[SAP性能指标（CRC AUL GBP Vortex）]]（性能口径对照，非本主题）

## Lessons 经验教训

> ✅ Verification（2026-09-29，来源 [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]）：两份来自不同项目的文档在**同一工艺结论**上互证——(i) 200 µm 垫片是 100 µm 方案不可行的替代（避免 165 bar / 99.7 bar 超压）；(ii) 必须接触式涂布以规避幅材抖动；(iii) 冷却辊同时服务于设定与热保护。本页结论与来源一致。

- **教训一（几何换控制）**：先用**垫片台面长度**把分区比值做进金属里，再用**泵速**控绝对值——这样产线上就没有需要实时控制的变量。是「用设计换控制」的教科书范例。
- **教训二（压降是 1/t³）**：为了边缘更锐利而减薄垫片，会把模头压力乘 8 并憋停泵。边缘锐度应用**台面几何**买，不要用垫片厚度买。
- **教训三（基材决定上限）**：透气膜约 90 ℃ 以上塌孔即不可逆损失 WVTR，**而且线上看不出来**。加冷却背辊比重新配方降施胶温度便宜得多。
- **教训四（流变规范要写 Cross 指数）**：只写 Brookfield 黏度会漏掉剪切变薄行为，而条纹与边缘溢流正是由它产生的；须同时规范 n 与 λ。
- **教训五（颗粒）**：每一切固体须满足垫片 ≥ 10 × d90 —— 200 µm 垫片对应 d90 ≤ 20 µm。这是「流变规范」之外的第二条硬门槛，也是最容易在配方阶段被忽略的一条。

## 追加：Meeting Minutes 批（2026-09-29 追加 · 护肤活性物涂布的工艺路线之争与 add-on 上限）

> 来源：[[Botanical Extract Efficacy, Wetness Visualisation & Tri-Zone Lotion Review（植物提取物功效测试与验证）]]（内部研发评审会 ASR 转写，会议日期 [待验证]）。本批只**追加**，不修改既有结论。

**三条涂布路线的对比（本批新增）：**

| 路线 | 优点 | 限制 |
| --- | --- | --- |
| **丝网印刷**（screen printing） | 实验室可控、可做图案 | **速度太慢**；对材料**粘性要求非常高**；add-on 有限 |
| **柔性印刷**（flex printing） | 高速、ink 近乎水性 | **add-on 有上限**；有效转移量下的有效物质受限 |
| **狭缝涂布 / 刮枪**（slot die，复用现有 capex） | 可**高速在线**，是最理想路线 | 要求物料为**高粘度油剂或固态**，与当前**水性体系相悖** |

**关键约束（本批新增）：**

1. **add-on 上限是硬约束** —— 湿态可视化配方在工厂放大三次失败，根因即"工艺带不上足够的量"（调粘度、定制网纹辊、加深网纹辊深度、换基布均无效）。
2. **水性与油性的路线分野** —— 水性体系适配丝网/柔性印刷但 add-on 低；要走高速狭缝涂布，物料必须是高粘度油剂或固态。
3. **转移率决定成败** —— 护肤活性物从无纺布转移到皮肤的比率，同类产品（M3）仅约 **2%**；油脂类转移相对容易，活性成分难。必须建立「添加量 → 转移量 → 最低起效量」的反推链。
4. **中期设想（技术早期）** —— 若能把 **98% 含水量的水凝胶**转化为 **master batch / 类 hot melt** 形态，则可走在线涂布；会中判断该技术**非常初期**，建议引入外部团队评估。
5. **平台化诉求** —— 涂布工艺应尽快**固定下来**（fix 不动），后续只更换活性物质，从而加快新品开发。

> 🔴 **manual_review（2026-09-29）**：供应商名单、设备改造与商务条件属商务敏感信息，本页不展开。请回原文核对：
> `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/植物提取物功效测试与验证.md`

✅ **验证记录（2026-09-29）**：三条路线的对比为会中判断；2% 转移率为同类产品的历史口径 [待验证]，非本批实测。参见 [[Skin Health Treatment on Nonwoven（无纺布护肤处理）]]、[[Botanical Extract Efficacy Verification（植物提取物功效验证）]]、[[Ultra-Low Add-On Adhesive Application（超低添加量施胶）]]。

## Sources 来源

- [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Stretch-Triggered Colour Indicator for Diaper Pant Side Panels.pptx.md`
- [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/BM/BM_Indicator_Design_Viscosity_Cost.pptx.md`
- [[BM Urine Indicator Concept（尿+便双指示概念）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/BM/BM_Urine_Indicator_Concept.pptx.md`

## Related Sources 关联来源

- [[Adhesive Feasibility & Action Plan（亲水SAP·烯烃基结构胶·低粘度水溶胶）]]
- [[BCC Pants Waist Break Study（Pants 产品拉断研究与两项新方法创建）]]
- [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]
- [[BM Urine Indicator Concept（尿+便双指示概念）]]
- [[Botanical Extract Efficacy, Wetness Visualisation & Tri-Zone Lotion Review（植物提取物功效测试与验证）]]
- [[GRIFFIN Learning Cycle Check In（GRIFFIN 学习周期复盘 · 2025-06-25）]]
- [[Henkel 议题补充：超低添加量与智能响应胶（2026-05-26 交流背景）]]
- [[Personal Care Process 101 - How It's Made（卫品加工工艺入门）]]
- [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]]
- [[US5266394A Disposable Articles Containing SIS Block Copolymers (Dow)]]

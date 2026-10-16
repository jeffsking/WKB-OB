---
type: concept
title: "Geometric Optical Mask（几何光学掩膜）"
domain: [卫材研发, 无纺布工艺]
status: growing
updated: 2026-09-29
tags: [Mechanochromic, 几何掩膜, 应变指示, 合身指示器, 热熔狭缝涂布, 波纹快门]
---

# Geometric Optical Mask（几何光学掩膜）

> One-line definition 一句话定义：A strain-triggered colour read-out achieved **by geometry, not by chemistry** — a rigid, opaque, CD-zoned hot-melt mask is slot-coated over a pre-gathered elastic laminate; as the laminate's own corrugation flattens under stretch, a printed under-colour is progressively revealed between the mask islands.
> （中文：一种**靠几何而非化学**实现应变触发读数的结构——在预收拢的弹性层压件上涂覆刚性、遮光的 CD 分区热熔胶掩膜；拉伸时层压件自身波纹被展平，底印颜色从掩膜岛之间按面积渐次露出。）

## Mechanism / Structure 机理 / 结构拆解

1. **The corrugation is a free mechanical shutter（波纹是免费的机械快门）.** A 2.2× bonded elastic laminate arrives with a relaxed corrugation pitch λ₀ of 1.2 mm. Nobody uses it; the mask does.
2. **Three-layer stack（三层结构）** — (i) the elastic panel laminate (SEBS meltblown or SBL, 2.2× bonded) supplies elasticity *and* the corrugation that gates the read-out; (ii) a supplier-applied CD-continuous flexo **under-print** in three bands (green ✓ / green ✓ / red ✗) — no registration to our coater required; (iii) a **slot-coated opaque mask** (TB-A ink) at 7.5–11 g/m² in three CD zones.
3. **The mask must be rigid, not stretchy（掩膜必须刚硬而不可拉伸）.** Film modulus ≈ 85 MPa, roughly 40× the panel; the ink:panel modulus ratio ≥ 35 : 1 is the release-critical specification. If the mask softens toward the panel modulus it stretches with the substrate and the bars stop appearing.
4. **One equation sets all three thresholds（一个方程定三个阈值）**：

   φ(ε) = 1 − 2a / [λ₀ (1 + ε)]

   where φ = exposed under-print fraction at panel strain ε; 2a = the arc of the corrugation covered by ink (set by coat weight); λ₀ = relaxed corrugation pitch; φ* = visual threshold, set at 0.30 (validated by ΔE*ab ≥ 6).

   Rearranged for design: **2a = λ₀ (1 − φ\*) (1 + ε\*)** — pick the strain at which a bar should light up, and the equation returns the ink arc, which the shim delivers as a coat weight.
5. **Zoning is machined, not controlled（分区是加工出来的，不是控制出来的）.** One manifold pressure feeds three CD zones whose ratio is fixed by land length (Q ∝ 1/L at constant gap, width and ΔP). Land lengths are machined to ± 0.05 mm, so the coat-weight ratio holds to better than 1 % for the life of the shim; a viscosity excursion moves all three zones together (self-compensating).
6. **Hysteresis-blind by design（天然对回滞不敏感）.** The indicator reads position, which is identical on the loading and unloading branches — so only the calibration branch has to be chosen.
7. **Phase-2 material variant: TB-B strain-triggered whitening（Phase 2 材料变体：TB-B 形变增白）.** Glassy microspheres in an elastomeric matrix with deliberately weak interfacial adhesion debond above an onset strain, opening 0.3–1 µm voids whose refractive-index discontinuity turns the film opaque white. Onset is a stress criterion and therefore a bulk property — coat weight barely moves it, so TB-B delivers **one** threshold, not three. Use it as a dedicated over-tension alarm layered on top of the TB-A meter, not as a replacement.

（中文：①波纹即免费快门——2.2× 层压件自带 1.2 mm 松弛波纹间距 λ₀；②三层结构——弹性层压件（供给弹性与波纹）、供应商柔印 CD 连续底印三色带（绿✓/绿✓/红✗，无需与本涂布机套准）、分区涂布的遮光掩膜（TB-A，7.5–11 g/m²）；③掩膜须刚硬——膜模量约 85 MPa（约面板 40 倍），墨:板模量比 ≥35:1 是放行关键规格；④一个方程 φ(ε)=1−2a/[λ₀(1+ε)] 定三个阈值，反解 2a=λ₀(1−φ*)(1+ε*) 由垫片以涂布量兑现；⑤分区由垫片台面长度机制定型（Q∝1/L），机加工 ±0.05 mm，比值寿命内优于 1%，黏度波动时三区同向移动而自补偿；⑥读出的是位置量，加载/卸载支相同，故对回滞不敏感；⑦Phase 2 的 TB-B 走「空洞化增白」——应力判据决定其只能给单一阈值，宜作 TB-A 之上的过紧专用报警层。）

## Key Parameters 关键参数表

| Parameter 参数 | Typical value / range 典型值/范围 | Source 出处 |
|---|---|---|
| Relaxed corrugation pitch λ₀ | 1.2 mm（2.2× laminate） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Visual threshold φ* | 0.30（validated by ΔE*ab ≥ 6） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Target strains per zone ε* | 38 / 67 / 101 % | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Required ink arc 2a | 1.39 / 1.68 / 2.03 mm | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Arc coverage 覆盖比 | 53 / 64 / 77 % | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Coat weight per zone | 7.5 / 9.0 / 11.0 g/m²（± 0.6） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Shim land length | 18.0 / 15.0 / 12.0 mm（machined to ± 0.05 mm） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Flow ratio delivered | 1.00 : 1.20 : 1.50 vs required 1.00 : 1.20 : 1.47（within 2 %） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Coated width | 3 × 18 mm = 54 mm（± 0.5） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Mask film modulus | ≈ 85 ± 15 MPa | [[TB-A Opaque Mask Hot Melt（TB-A 遮光热熔胶）]] |
| Modulus ratio ink : panel | ≥ 35 : 1 | [[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]] |
| Contrast ratio @ 9 g/m² | ≥ 0.86 | [[TB-A Opaque Mask Hot Melt（TB-A 遮光热熔胶）]] |
| Reversibility 可逆性 | ∞ cycles（mechanism is geometric, not fracture） | [[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]] |
| Cycle durability requirement | 20 don/doff cycles to 100 % → drift ≤ ±8 pts | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| TRL | 8（near production deployment） | [[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]] |
| Process window | contact slot die, 200 µm shim, 160 °C melt, 12 °C chill roll, 0.4 s dwell, 400 m/min | [[Hot-Melt Slot Coating（热熔狭缝涂布）]] |
| Control point（上游） | lamination pre-stretch ratio + relaxed corrugation pitch，Cpk ≥ 1.33 + per-lot certificate | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Web tension limit | MD 25 ± 3 N/m；above 40 N/m the corrugation is pulled out | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |

> ⚠️ **No unsourced parameters（禁止无来源参数）**：表中每个数字均来自本批源摘要页。掩膜与层压件的**长期老化后波纹稳定性曲线**库内无数据，标 `[待验证]`——这正是原文指定的头号风险（R1 阈值漂移）。

## Sensitivity 敏感度（控制资源该投在哪）

| Variable 变量 | Sensitivity | Why 原因 |
|---|---|---|
| Panel lamination pre-stretch 层压预拉伸 | **HIGH** | 预展平波纹；决定 λ₀ |
| Coat weight 涂布量 | **HIGH** | 决定 2a |
| Web tension at the die 模头处幅材张力 | **HIGH** | > 40 N/m 掩膜下探到侧翼过深，全部阈值后移 |
| Melt viscosity 熔体黏度 | LOW | 自补偿——三区同向移动，比值保持 |
| Line speed 车速 | Low | 涂布量由泵速/线速比保持；仅极端车速影响润湿 |
| Ambient humidity 环境湿度 | **NEGLIGIBLE** | 机制是几何的，墨中无吸湿组分 |

> Control conclusion（控制结论）：**put the SPC on the incoming panel laminate, not on your own coater**（把 SPC 放在来料面板上，而不是自己的涂布机上）。

## Adjacent Concepts 相邻概念

- Chemistry it replaces 被它替代的化学路径：[[Mechanophore Mechanochromism（机械力致变色分子）]]、[[Structural Colour Mechanochromism（结构色力致变色）]]
- Ink and process 墨与工艺：[[TB-A Opaque Mask Hot Melt（TB-A 遮光热熔胶）]]、[[Hot-Melt Slot Coating（热熔狭缝涂布）]]
- Calibration 标定：[[Panel Hysteresis and Threshold Calibration（面板回滞与阈值标定）]]、[[Skin Contact Pressure（皮肤接触压力）]]
- Decision 选型：[[Mechanochromic Routes Comparison（力致变色技术路线对比）]]

## Lessons 经验教训

> ✅ Verification（2026-09-29，来源 [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]]、[[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]]）：两份独立文档（工程深化报告与立项提案）对同一架构给出**一致结论**——TRL 8、无限循环、零新化学品、成本指数 1.0×。本页「几何遮光优于变色化学」的表述与来源一致。

- **教训一（工艺）**：本方案的全部风险在**来料**。面板预拉伸比与松弛波纹间距必须写进面板采购规格（Cpk ≥ 1.33 + 逐批证书），否则 Stage 3 会以「看起来像涂布问题」的方式失败。
- **教训二（白墨的意义）**：掩膜刻意做成**白色**、颜色全部放在供应商柔印底印里——白色掩膜不需要与本涂布机的热熔胶做色匹配，能扛过批次间颜料漂移，且在任何育婴室灯光下都能被手机拍准。色彩准确度因此成为面板供应商的**既有问题**，而不是新增问题。
- **教训三（计数优于比色）**：「两个绿条、无红条」的**计数式读出**优于色相匹配：凌晨三点在暗房间里，家长无法可靠区分紫色与紫红色，但永远能数出条数；计数式读出还能扛过色觉缺陷与手机拍照。
- **待补 `[待验证]`**：波纹结构在 8 h / 33 °C / 85 % RH 佩戴与 40 °C 仓储后的**稳定性曲线**；TB-B 空洞化增白的真实 onset 应变分布（原文只给设计目标）。

## Sources 来源

- [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Stretch-Triggered Colour Indicator for Diaper Pant Side Panels.pptx.md`
- [[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Mechanochromic_Waistband_Tension_Indicator_Proposal_2026-08-19.pptx.md`
- [[Mechanochromic Materials Technical Review（EN v3, 2026-08）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Mechanochromic_TechReview_EN_v3_2026-08-02_fixed.pptx.md`

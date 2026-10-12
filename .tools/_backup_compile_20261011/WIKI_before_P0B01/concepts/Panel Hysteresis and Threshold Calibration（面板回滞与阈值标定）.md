---
type: concept
title: "Panel Hysteresis and Threshold Calibration（面板回滞与阈值标定）"
domain: [卫材研发, 测试方法, 应变指示]
status: growing
updated: 2026-09-29
tags: [回滞, 应力松弛, 阈值标定, ΔE, 合身指示器, 测试方法]
---

# Panel Hysteresis and Threshold Calibration（面板回滞与阈值标定）

> One-line definition 一句话定义：The practice of **setting a strain indicator's colour bands on the unloading (retraction) branch, not the extension branch** — because what the baby feels for the next eight hours is the sustained worn tension, and for a SEBS panel that is 35–55 % lower than the peak pull force.
> （中文：把应变指示器的颜色带**标定在卸载（回弹）支而非加载支**的做法——因为婴儿接下来八小时感受到的是持续佩戴张力，而对 SEBS 面板而言该值比峰值拉力低 35–55 %。）

## Mechanism / Structure 机理 / 结构拆解

1. **Mom pulls on, then lets go（妈妈拉上后松手）**：the donning motion loads the panel; the wear state sits on the unloading branch. Any threshold published against the extension curve therefore describes a state the baby never occupies.
2. **The magnitude of the error（误差幅度）**：for an SEBS panel at 100 % strain the pull force is 5.2 N but the sustained worn tension is 3.9 N — publishing thresholds against the extension curve would **overstate comfort by ~30 %**.
3. **A geometric read-out is hysteresis-blind — and that is a feature（几何读出对回滞不敏感，且这是优点）**：the indicator reads *position*, which is the same on both branches. Only the calibration reference has to be chosen; the sensor does not have to resolve the branch. A chemistry- or force-based read-out would have to.
4. **Set the band on the retraction curve（把带设在回弹曲线上）**：design point 67 % strain → 2.5 N sustained → ~2.8 mmHg mean panel pressure. Comfortable, secure, and 5× below the marking threshold.
5. **Add a stress-relaxation correction（叠加应力松弛修正）**：SEBS panels lose 12–20 % of tension in the first hour. The "correct" band must be wide enough that an hour of relaxation does not drop the reading out of it — hence a **30-point-wide window**, not a single line.
6. **How a threshold is actually measured（阈值到底怎么测）**：the read-out is perceptual, so the test method must be colorimetric and defined against a perception threshold — ΔE*ab of each zone against its own relaxed state, on the **second cycle, retraction branch**.
7. **Why ΔE = 6 and not ΔE = 2（为什么用 ΔE=6 而非 2）**：ΔE*ab ≈ 2 is the laboratory just-noticeable difference under controlled side-by-side viewing; a parent sees the panel alone, at arm's length, in a dim room, at an angle, possibly one-handed. Setting acceptance at **three JNDs** is the difference between a specification that passes on a spectrophotometer and one that passes in a nursery — and it is also what forces the state separation of 18 rather than a marginal 8.

（中文：①穿上时加载、佩戴时落在卸载支，按加载曲线公布阈值等于描述一个婴儿从未经历的状态；②误差幅度——SEBS 面板在 100% 应变下拉力 5.2 N，而持续佩戴张力仅 3.9 N，用加载曲线标定会把舒适度高估约 30%；③几何读出只读位置量，两支出相同，故「对回滞不敏感」，这是优点——只有标定参考支需要选，传感器不必分辨支路；而化学或力基读出则必须分辨；④把「正确」带设在回弹曲线上——设计点 67% 应变 → 2.5 N 持续 → 均值约 2.8 mmHg，舒适、可靠，且低于留痕阈值 5 倍；⑤叠加应力松弛修正——SEBS 面板首小时损失 12–20% 张力，故「正确」带须足够宽，使一小时松弛不会让读数掉出该带，这正是**30 点宽窗口**而非单线的来由；⑥阈值实测方法——读出是感知性的，故测试方法必须是比色的、并锚定在感知阈值上：各区相对自身松弛态的 ΔE*ab，取**第 2 循环、卸载支**；⑦为什么定 ΔE=6——ΔE*ab≈2 是受控并排观察下的实验室恰可辨差，而家长是在昏暗房间、一臂距离、有倾角、可能单手的情况下单看面板；把验收定在**三个恰可辨差**，是「在分光光度计上通过」与「在育婴室里通过」的分野，也正是它强制状态分离度取 18 而非勉强 8。）

## Key Parameters 关键参数表

| Parameter 参数 | Value / range 数值/范围 | Source 出处 |
|---|---|---|
| Hysteresis, SEBS panel 回滞 | 35–55 % | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Pull force vs worn tension @ 100 % strain | 5.2 N（loading）vs 3.9 N（sustained） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Comfort overstatement if calibrated on extension | ~30 % | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Design point 设计点 | 67 % strain → 2.5 N sustained → ~2.8 mmHg mean | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Stress relaxation, first hour | 12–20 % tension loss | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| "Correct" band width | 30 strain points | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Perception threshold 感知阈值 | ΔE*ab = 6（≈ three just-noticeable differences） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| State separation required 状态分离度 | ΔE*ab ≥ 18 between adjacent bands | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Threshold accuracy acceptance | 38 / 67 / 101 % ± 7 pts（cycle 2, retraction） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Cycle durability acceptance | 20 don/doff cycles to 100 % → drift ≤ ±8 pts | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Wear-condition hold acceptance | 8 h @ 33 °C / 85 % RH @ 67 % strain → drift ≤ ±5 pts | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Wet robustness acceptance | 4 h synthetic urine soak (0.9 % NaCl) → ΔE change ≤ 3 | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Measurement setup 测量配置 | 25 mm panel strip, tensile frame, D65 booth, 45°/0° geometry, calibrated camera; extend at 500 mm/min to 130 %, hold 5 s per 5 % step | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Panel hysteresis test method | EDANA cyclic, 2 cyc to 100 %, 500 mm/min | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Consumer read accuracy endpoint | n = 120 in-home, unaided first use → ≥ 85 % correct band | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Related construction parameter | lamination pre-stretch ratio；relaxed corrugation pitch；Cpk ≥ 1.33 + per-lot certificate | [[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]] |
| Model vs measurement | 本批的力值均为**建模值**，原文 Stage 1 要求「measure real panel hysteresis and replace the modelled force numbers」 | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |

> ⚠️ **禁止无来源参数**：本页全部数字来自源摘要页；**1.4 / 2.5 / 3.9 N 与 4.3 / 2.8 / 29 mmHg 均为模型值，须实测替换** —— 原文列为 Stage 1 门径任务，库内标 `[待验证]`。

## Adjacent Concepts 相邻概念

- 上游架构：[[Geometric Optical Mask（几何光学掩膜）]]
- 物理量来源：[[Skin Contact Pressure（皮肤接触压力）]]
- 既有页对照：[[芯体测试方法与验收基准（STM）]]、[[热风粘合无纺布]]
- 选型：[[Mechanochromic Routes Comparison（力致变色技术路线对比）]]

## Lessons 经验教训

> ✅ Verification（2026-09-29，来源 [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]]、[[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]]）：两份文档一致给出「按卸载支标定 + 30 点宽窗口」的做法，且立项提案把它写进风险 R2 的缓解措施（「geometric mask is inherently stable（no chemical relaxation）」）。本页结论与来源一致。

- **教训一（标定支路）**：**公布阈值前先问「这个状态婴儿会遇到吗」**。加载曲线上的数值是瞬间峰值，不是佩戴状态；两者差 35–55%，直接决定舒适度是被高估还是被正确描述。
- **教训二（窗口宽度）**：单线阈值在真实佩戴中会失效——须留出**应力松弛 + 回滞 + 来料波动**的复合余量，这就是 30 点宽窗口的物理来源。
- **教训三（验收口径）**：ΔE 阈值必须定在**真实使用场景的感知条件**（一臂距离、昏暗、有倾角、单手），而非实验室并排比对条件；ΔE=6 与 ΔE=18 不是保守，是「能通过」与「看起来通过」的分界。
- **教训四（模型诚实）**：本批全部力值均为模型值，原文明确要求在 Stage 1 用实测替换 —— 引用本页数字对外时须注明「建模值」。

## Sources 来源

- [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Stretch-Triggered Colour Indicator for Diaper Pant Side Panels.pptx.md`
- [[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Mechanochromic_Waistband_Tension_Indicator_Proposal_2026-08-19.pptx.md`

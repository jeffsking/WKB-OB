---
type: concept
title: "Film-Free Backsheet（无膜背层）"
domain: [卫材研发, 芯体与吸收]
status: growing
updated: 2026-09-29
tags: [背层, 底膜, 无膜, SMMMS, 透气, 单一材质, 分区设计]
---

# Film-Free Backsheet（无膜背层）

> One-line definition 一句话定义：以**高阻隔熔喷复合无纺布**（如 30 gsm SMMMS）替代一次性卫生用品中「微孔透气膜 + 纺粘」背层组件，从而取消 PE/PP 复合结构的做法；本库结论是**分区去膜**可行，**整体替换**不可行。（中文：能去膜的是裆部以外的机身，裆部芯体足迹区必须留膜。）

## Mechanism / Structure 机理 / 结构拆解

1. **Two barrier mechanisms, not one 两种阻隔机理**：the film's barrier is a **solid wall**；the nonwoven's barrier is a **capillary**。That is why the film holds **> 1000 mbar in every contamination column** while the nonwoven collapses as surface tension falls。中文：膜是实壁、无纺布是毛细——所以污染物一进场，两者不是「差一点」，而是「差两个数量级」。
2. **Where it wins unconditionally 无条件胜出的位置**：chassis outside the core footprint（芯体足迹以外的机身）——no free liquid ever reaches it, breathability is a pure win, and the softness/drape gain is what the consumer actually notices。模型建议约 **62 % 的背层面积**可即刻去膜。
3. **Where it fails 失效位置**：crotch over the core footprint — 这是 free liquid、contamination 与 peak sitting pressure 三者交汇处。Benchmarks: **141 mbar** clean、**121 mbar** synthetic urine vs **88 mbar** sitting pressure from a 9 kg infant（2.3× margin），but **55 mbar** against runny stool and **14 mbar** against barrier cream（裕度消失/反转）。
4. **How contamination arrives 污染物如何到达背层**：cream is applied to skin, so the core stands between it and the barrier — that helps。What does not help: **bile salts in loose stool tracking around the core edge**，and **wipe-lotion carryover at the leg cuff** — exactly where the seal matters most。（中文：护臀膏被芯体挡住是帮助下；稀便胆汁盐绕芯体边缘、湿巾液在腿围残留是坏事。）
5. **Why partitioning is a cost decision too 分区同时是成本决策**：the film route carries **1.8 EUR-cents of lamination adhesive** that the all-nonwoven route does not；strip it out and the cost gap closes to **under 1 %**。SMMMS lands **within 5 %** of the incumbent — not cheaper, not a blocker。
6. **The strategic prize is mono-material PP 战略收益是单一材质**：a PP-only backsheet removes the **PE/PP split that blocks mechanical recycling** of the chassis；原文称这「比那 0.4 分钱更值」。
7. **Structural variants 结构变体**：SMMMS（4 熔喷束）carries the barrier；**SMMSMMS adds 8 gsm and ~27 % cost for no barrier gain** and is justified only where the web is mechanically activated（ring-rolled ears, pant side panels），because the inner spunbond anchors the meltblown against delamination。Leg cuff：upgrade to the same **1.2 µm** meltblown grade rather than treating it as a separate material。

## Key Parameter Table 关键参数表

| Parameter 参数 | Value 数值 | Source 出处 |
|---|---|---|
| Modelled structure 建模结构 | SMMMS 30 gsm（S1 9 / M1–M4 3.0 each / S2 9） | [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]] |
| Hydrohead, clean 静水压·清水 | 141 mbar modelled（target ≥ 130） | 同上 |
| Hydrohead, synthetic urine 静水压·合成尿 | 121 mbar modelled（target ≥ 110） | 同上 |
| Sitting pressure, 9 kg infant 9 kg 坐压 | 88 mbar（margin 2.3×） | 同上 |
| Hydrohead, runny stool 静水压·稀便 | 55 mbar | 同上 |
| Hydrohead, barrier cream 静水压·护臀膏 | 14 mbar（3.7× under water） | 同上 |
| Film comparison 膜对照 | > 1000 mbar in every column | 同上 |
| WVTR | ≥ 18,000 vs 3,000 g/m²/day for film | 同上 |
| Air permeability 透气量 | 52 L/m²·s vs effectively zero（film） | 同上 |
| Film-free area share 可去膜面积占比 | ~62 % of backsheet area | 同上 |
| Cost vs incumbent 相对现有方案 | within 5 %；去胶后 < 1 % | 同上（图轴值 11.02 / 8.26 `[口径待确认]`） |
| Lamination adhesive avoided 省下的复合胶 | 1.8 EUR-cents | 同上 |
| Calendar bond 热轧粘合 | 16 % area / 0.35 mm² dots / 148–150 °C | 同上 |
| Softness 柔软度 | Handle-o-meter ≤ 0.9 × film laminate | 同上 |
| Opacity 遮盖率 | ≥ 88 %（无需 TiO₂，熔喷散射） | 同上 |
| Odour 气味 | 52 L/m²·s 让氨气与蒸汽一样自由逸出——**unpriced risk** | 同上 |

> ⚠️ **No unsourced parameters 禁止无来源参数**：上表静水压/透气量为**模拟值**（源页自陈 Λ = 6 为拟合、CV = 15 % 为假设、污染输运未建模）；`[口径待确认]` 的成本图轴值不得直接对外引用。真实尿裤中胆汁盐/湿巾液是否到达背层**未建模**，属实验问题。

## Adjacent Concepts 相邻概念

- 支配机理 支配机理：[[Formation-Limited Barrier（阻隔的成形受限机理）]]
- 载体工艺 载体工艺：[[Meltblown Nonwoven（熔喷非织造布）]]、[[SMS复合结构]]
- 硬件 硬件：[[Laser-Assisted Die Tip（激光辅助模头）]]
- 对照 对照：[[SMMMS Film-Free vs Microporous Film Backsheet（无膜背层 vs 微孔膜背层）]]、[[SMMMS vs SMMSMMS（成本·性能·供应链）]]
- 相邻结构议题 相邻结构议题：[[亲水-疏水梯度设计]]、[[分区密度设计]]、[[热风粘合无纺布]]

## Lessons Learned 经验教训

> ✅ Verification（2026-09-29，source [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]]）：本页「分区而非整体替换」的结论直接来自该评估的 Recommendation 章；同时与库内既有风险提示互补——[[SMS复合结构]] 记录的**驻极助剂含氟（PFAS）风险**提醒：无膜背层的疏水化须走**无氟（PFAS-free）**路线，源文亦明确要求 alkyl-modified polyolefin 而非 C6 氟化学。（中文：与本库既有 PFAS 风险提示一致。）

- **Lesson 1（把「阻隔」拆成两种机理）**：膜是实壁、无纺布是毛细。任何「膜换成无纺布」的提案都必须先给出**最低表面张力场景**（稀便 48 mN/m、护臀膏 33 mN/m）下的静水压，而不是清水值。
- **Lesson 2（分区是工程解，不是妥协）**：约 62 % 面积去膜 + 裆部留膜 + 腿围用同级熔喷，三件事在同一份评估里同时成立，比任何「全换」或「不换」的二元结论更有执行价值。
- **Lesson 3（多两束熔喷是产线问题不是材料问题）**：熔喷是复合线上最慢的一束，四束 3 gsm 意味着**熔喷段而非纺粘段决定产线天花板**——材料评估之前必须先做线平衡。
- **Lesson 4（气味是未计价风险）**：52 L/m²·s 的透气量让氨气自由逸出，无模型能预测消费者反应，须**尽早做气味评审**（源文把它列为 S3 阶段第一件要做的事）。
- **待补 `[待验证]`**：真实尿裤中稀便胆汁盐/湿巾液向背层的输运实验；熔喷网在持续坐压下的蠕变/湿塌缩（compaction）对阻隔与粘点应力的双向影响；单一材质 PP 回收声明的实证。

## Sources 来源

- [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Film/Laser_Meltblown_Film_Free_Backsheet.pptx - 已修复.pptx.md`
- [[SMS复合结构]] —— 库内页（PFAS 风险基线）

## Related Sources 关联来源

- [[CN 111890767 A（一种超薄聚乙烯微孔透气膜及其制备方法）]]
- [[CN 112778606 A（一种分区透气底膜及其制备方法、纸尿裤）]]
- [[Composite Nonwoven Types Processes and Applications 2026（主流复合无纺布种类·工艺·应用）]]
- [[Handbook of Plastic Films]]
- [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]]
- [[US11612524B2 Breathable Diaper Backsheet (Colormasters)]]
- [[US7195621B2 Disposable Garment Comprising Meltblown Nonwoven Backsheet (P&G)]]
- [[mocon底膜透气率测试.docx]]

---
type: concept
title: "Formation-Limited Barrier（阻隔的成形受限机理）"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-29
tags: [阻隔, 静水压, 成形CV, Gumbel, 多束, 克重, 极值统计]
---

# Formation-Limited Barrier（阻隔的成形受限机理）

> One-line definition 一句话定义：非织造布的液体阻隔**不是由平均孔径决定，而是由整片材料上最薄的那一块局部克重决定**——因此阻隔可用「极值统计 + 多束平均」直接优化，而不必改变化学或纤维直径。（中文：阻隔 = 最弱局部克重 × 表面张力 ÷ 纤维直径，不是「中位孔径」的函数。）

## Mechanism / Structure 机理 / 结构拆解

1. **The ideal-pore model over-predicts by 15× 理想孔模型高估 15 倍**：Laplace on the median pore of a 1.5 µm web gives roughly **800 mbar**；real webs deliver **40–140 mbar**。The gap is not pore size — it is that **liquid finds the thinnest patch on the sheet and breaks through there**。（中文：差距不在孔径，而在液体总从最薄处击穿。）
2. **The governing relation 支配关系式**：P ∝ weakest local gsm × γ |cos θ| ÷ fibre diameter。Note that this makes surface tension（γ）与接触角（θ）与克重均一性**同位阶**的杠杆，而不是并列的三个独立变量。
3. **The weakest patch is an extreme-value problem 最弱斑是极值问题**：the weakest local basis weight is the lowest over the 100 cm² test area — a **Gumbel minimum over 10⁴ patches, about 3.74 standard deviations below the mean** — not the sheet average。（中文：取的是 10⁴ 个斑块的最小值，约均值下方 3.74 个标准差。）
4. **Splitting the meltblown converts formation noise into barrier 拆束把成形噪声换成阻隔**：independent beams average their formation noise as **1/√n**。One beam at 15 % CV retains **44 %** of its weight at the weakest patch；four beams retain **72 %** — same polymer, same grams, **64 % more barrier**。（图上 3/4/5/6 束约 138 / 155 / 171 / 176，口径见源页。）
5. **Why this matters commercially 为什么这在商业上重要**：barrier is carried entirely by meltblown grams and **beam count** — which is why SMMSMMS（same four beams, same 12 gsm MB）lands on exactly the same number while costing **+8 gsm and ~27 %**。它把「阻隔」从材料化学问题变成**布网与统计问题**。
6. **Two levers, one cheap and one structural 两个杠杆**：① 提高疏水助剂把 advancing contact angle 从 105° 拉到 118–122°（worth about **35 % on hydrohead** for 3.5 EUR-c/kg）；② 增加独立熔喷束数（同克重下最多 +64 %）。二者叠加时不冲突。
7. **The mechanism also defines the failure boundary 该机理同时定义失效边界**：as γ falls（water 72 → urine ~66 → urine+sebum 58 → runny stool 48 → residue 40 → barrier cream 33 mN/m），the weakest-patch breakthrough moves from a margin to a deficit；这是为什么同一张 30 gsm SMMMS 对清水有 2.3× 裕度、对护臀膏却是 3.7× 亏欠。

## Key Parameter Table 关键参数表

| Parameter 参数 | Value 数值 | Source 出处 |
|---|---|---|
| Governing relation 支配关系式 | P ∝ weakest local gsm × γ \|cos θ\| ÷ fibre diameter | [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]] |
| Ideal-pore (Laplace, median pore) 理想孔（中位孔径 Laplace） | ~800 mbar（1.5 µm web） | 同上 |
| Real webs 真实网材 | 40–140 mbar（15× 高估） | 同上 |
| Weakest-patch statistic 最弱斑统计量 | Gumbel minimum over 10⁴ patches per 100 cm²；≈ 3.74 SD below the mean | 同上 |
| Beam averaging 束间平均 | noise ∝ 1/√n | 同上 |
| Weight retained at weakest patch 最弱处保住克重 | 44 %（1 beam, 15 % CV）→ 72 %（4 beams） | 同上 |
| Barrier gain from splitting 拆束阻隔增益 | +64 %（same polymer, same grams） | 同上 |
| Barrier constant A 阻隔常数 A | 24.5 mbar·µm/gsm（校准锚：10 gsm / 2.4 µm 单束 → 45 mbar） | 同上 |
| Formation CV assumption 成形 CV 假设 | 15 % per beam at 1 mm²（**drives the entire argument**） | 同上 |
| Hydrophobic additive gain 疏水助剂增益 | 接触角 105° → 118–122°，约 +35 % hydrohead | 同上 |
| Surface-tension columns 表面张力列 | 72（water）/ 66（urine）/ 58（urine+sebum）/ 48（runny stool）/ 40（residue）/ 33（barrier cream）mN/m | 同上 |
| Structural consequence 结构后果 | SMMSMMS 同束数同克重 → 同阻隔，成本 +27 % | 同上 |

> ⚠️ **No unsourced parameters 禁止无来源参数**：CV = 15 %、Λ = 6、A = 24.5 均为**拟合/假设常数**（源页自陈），Gumbel 3.74 SD 为统计推算值。**本库暂无实测的单束成形 CV 或击穿位置观测**，标 `[待验证]`；引用本页结论时必须声明其为模型推断，不得当作实测性能承诺。

## Adjacent Concepts 相邻概念

- 载体工艺 载体工艺：[[Meltblown Nonwoven（熔喷非织造布）]]、[[SMS复合结构]]
- 应用 应用：[[Film-Free Backsheet（无膜背层）]]
- 对照 对照：[[SMMMS vs SMMSMMS（成本·性能·供应链）]]、[[无纺布五大工艺对比]]
- 相邻性能议题 相邻性能议题：[[SAP性能指标（CRC AUL GBP Vortex）]]（同属「用哪一类指标才能判别性能」的方法论问题）
- 材料 材料：[[茂金属聚丙烯]]（450 MFR 而非 1200 MFR 的理由 = 降成形 CV）

## Lessons Learned 经验教训

> ✅ Verification（2026-09-29，source [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]]）：本页机理**修正**了库内既有的「熔喷阻隔=纤维细/孔径小」直觉表述——[[无纺布五大工艺对比]] 以「过滤精度星级」描述熔喷，其适用场景是**颗粒物过滤**；对**液体阻隔**，支配量是**局部克重极值**。（中文：属补充与细化，不改既有过滤结论。）

- **Lesson 1（选树脂的标准随之改变）**：既然阻隔挂在最弱斑上，**熔体强度（成形均一性）比流动性更值钱**——这正是 450 MFR 优于 1200 MFR 的理由，也是「MFR 越高越好纺」这一直觉在阻隔场景下的反例（见 [[熔融指数与化学降解]]）。
- **Lesson 2（多束是「免费的阻隔」）**：同聚合物、同克重、同纤维直径，仅拆分束数即可 +64 % 阻隔。任何「阻隔不够就加克重」的方案，应先检查是否可拆束。
- **Lesson 3（测什么决定能不能判）**：验收必须测 **1 mm² 尺度局部克重 CV** 与 **33–72 mN/m 表面张力扫描曲线**；只测清水静水压等于漏掉真实的失效场景（源页 kill criteria 即挂在此两项）。
- **待补 `[待验证]`**：单束实测 CV（若为 10 %，单束 SMS 明显优于模型所示、四束论证减弱）；击穿位置是否真的落在最薄斑（需可视化验证）；纤维直径分布（实测 log-normal CV≈0.5）对模型的影响。

## Sources 来源

- [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Film/Laser_Meltblown_Film_Free_Backsheet.pptx - 已修复.pptx.md`
- [[无纺布五大工艺对比]] —— 库内页（过滤精度视角的对照基线）

## Related Sources 关联来源

- [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]]
- [[Raw Material STM - Nanjing Plant（原材料STM-NJ）]]
- [[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]]
- [[US7195621B2 Disposable Garment Comprising Meltblown Nonwoven Backsheet (P&G)]]

---
type: concept
title: "BM Simulant A（便液模拟液 A）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-30
tags: [BM, 便液模拟液, simulant, 配方, BM gun, 稀便, 3:1]
aliases: ["BM Simulant A", "便液模拟液", "Bowel Movement Simulant"]
---

# BM Simulant A（便液模拟液 A / Bowel Movement Simulant A）

> One-line definition 一句话定义：**模拟婴儿稀便的实验室配方液体（酸奶基 + 表面活性剂）**，配合 **BM gun（便液注射枪）**使用，是 BM 摄入、BM 滑渗、BM 假人三类测试的共同基础设施——**母液须熟化 24 h，使用时按 3:1 与生理盐水稀释才代表"稀便"**。
> (A yogurt-based simulant for runny stool, dosed with a BM gun; must rest 24 h and is diluted 3:1 with saline before use.)

## Definition 定义

尿液可以用盐水近似（见 [[尿液模拟液（Urine Analog）]]），**便液不行**：便液是含蛋白、脂肪与固体颗粒的**非牛顿流体**，其滑渗与吸收行为由**黏度与屈服应力**主导，而非芯体的吸收速度。因此便液测试必须单独建立模拟液体系。

本库目前只有 **Simulant A** 一条配方谱系，全部 BM 方法（[[TTM-00445 BM Run-off.docx]]、[[TTM-00466 BM Benefit Visualization Validation.docx]]、[[TTM-00467 BM Mannequin Absorption NB-S2（BM 假人吸收测试）]]）都建立在它之上。

## Mechanism 机理拆解

1. **四种成分各司其职**：**酸奶**提供脂肪与乳固体基质（2% 脂肪、无蔗糖，避免糖改变黏度）；**姜黄根粉**提供颜色与颗粒感（便于摄像判读铺展范围）；**蛋白液**提供蛋白组分；**明胶**提供黏弹性与屈服应力。
2. **DAWN 餐具清洁剂是"表面活性剂"的替代方案**：加入 1.3% DAWN 溶液（每 200 g 混合物加 2 g）以模拟真实便液对材料表面的润湿行为——**这一步最容易被漏做，漏做即改变表面张力**。
3. **熟化 24 h 是流变建立过程，不是等待**：明胶水合与蛋白网络需要时间，**未熟化的模拟液流变未定，读数不可复现**。
4. **稀释比定义便型**：**Simulant A : 生理盐水 = 3 : 1**（300 mL : 100 mL）= **"稀便（runny）"**；改变配比即改变流体，**跨配比的结果不可比较**。
5. **温度与时效是硬约束**：配制在 **21–25 ℃**；储存 **7 ℃ ≤ 7 天**；**每次用前室温静置 1 h**。冷液直接使用会因黏度偏高而低估吸收、高估滑渗。
6. **BM gun 把"吸便/吸尿"并入一台设备**：**接大口测吸便能力、接小口测吸尿能力**；装填至管口下约 **2 cm**、**上限 400 mL**；**余量不得低于圆管底部上方 5 cm**，否则须重新走一遍重置流程。

## Key Parameters 关键参数表

| 项目 Item | 数值 / 口径 Value | 出处 Source |
|---|---|---|
| 配方比 Recipe（w/w） | 酸奶 : 姜黄根粉 : 蛋白液 : 明胶 = **57 : 3 : 39.6 : 0.4** | [[BM simulant A配方 & BM gun操作.docx]] |
| 200 g 示例 Batch example | 酸奶 **114.00 g** + 姜黄根粉 **6.00 g** + 蛋白液 **79.20 g** + 明胶 **0.80 g** | 同上 |
| 表面活性剂 Surfactant | **1.3% DAWN 溶液**（1.30 g DAWN + 98.70 g 纯水）；**每 200 g 混合物加 2 g** | 同上 |
| 混合条件 Mixing | 室温 **21–25 ℃**；**50 RPM × 5 min**；加 DAWN 后再 **50 RPM × 2 min**；杯壁须刮净 | 同上 |
| 熟化 Rest | **静置 24 h**后方可使用 | 同上 |
| 储存 Storage | **7 ℃，最长 7 天**；用前**室温静置 1 h** | 同上 |
| 稀便稀释比 Dilution | **Simulant A : 生理盐水 = 3 : 1（300 mL : 100 mL）**，350 rpm × 30 s 混匀 | [[TTM-00445 BM Run-off.docx]] |
| BM gun 装填 Fill | 至管口下约 **2 cm**，**上限 400 mL**；**余量 ≥ 圆管底部上方 5 cm** | [[BM simulant A配方 & BM gun操作.docx]] |
| BM gun 接口 Port | **大口 = 吸便能力；小口 = 吸尿能力** | 同上 |
| 设备 Equipment | 恩培 5-450 低速搅拌机；BM gun（建议接 GFI 接地保护） | 同上 |
| 合格阈值 Threshold | 无（模拟液本身无合格阈值；黏度验收口径原文未给）`[待验证]` | — |

> ⚠️ **禁止无来源参数**：全部数值来自上述两份 SOP；**Simulant A 本库仅此一条配方谱系**，无第二条来源可交叉印证，配方类结论标 `[待验证]`；模拟液的**黏度/屈服应力验收方法原文未给**。

## 相邻概念

- 对应概念：[[尿液模拟液（Urine Analog）]]（尿用盐水基，便用酸奶基，两条体系不可混用）
- 下游方法：[[Run-off & Leakage Test（滑渗与渗漏测试）]]（BM Run-off 属其第四条路径）、[[Mannequin BM Test（BM 假人测试）]]
- 对比：[[BM Run-off 与尿滑渗测试方法对比（TTM-00445 vs 30° 尿滑渗）]]
- 指示相关：[[Urine Indicator vs BM Indicator（尿湿指示 vs 便指示）]]

## 来源

- [[BM simulant A配方 & BM gun操作.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/BM测试方法/BM simulant A配方 & BM gun操作.docx.md`
- [[TTM-00445 BM Run-off.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/BM测试方法/TTM-00445 BM Run-off.docx.md`

> 🔗 治理合并（2026-09-30）：[[稀释便液 BM simulant A]] 已并入本页（指针页保留，原文存档于指针页）。同名对象双页（命名变体），并入高入链页

## Related Sources 关联来源

- [[BM simulant A配方 & BM gun操作.docx]]
- [[IMA知识库索引_20261002]]
- [[Product Report-Out FB.xlsx]]
- [[TTM-00445 BM Run-off.docx]]

---
type: concept
title: "Mannequin BM Test（BM 假人测试）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-29
tags: [BM, 便便, mannequin, 假人, 模拟便液, TTM-00234, TTM-00466, 可视化, 感官测试]
aliases: ["BM 假人测试（便液可视化与量化）", "Mannequin BM Test"]
---

# Mannequin BM Test（BM 假人测试 / Mannequin BM Test）

> 一句话定义：用**模拟便液（BM Simulant A）** 替代尿液来评价纸尿裤吸便能力的一族方法，两条实现路径并行——**假人 + 动作可视化**（[[TTM-00234 Rock N Roll Mannequin BM Test With Movement.docx]]，产出照片）与**平铺台架 + 恒定压力称重**（[[TTM-00466 BM Benefit Visualization Validation.docx]]，产出回渗/吸收克数）。

## 机理 / 结构拆解 Mechanism

1. **为什么 BM 要单独一套方法**：便液与尿液的流变、颗粒物、黏度不同，SAP 对便液基本不吸收（吸收主要靠**绒毛浆/无纺布的毛细与过滤**）；因此 BM 测试考察的是**"封住 / 摊开 / 不让返出"**的能力，而不是容量。
2. **两条路径各自的定位**：
   - **可视化路径（TTM-00234）**：假人穿着 → 标准动作（摇动 + 坐起）→ 拍照。用途明确写为**照片分析、消费者测试、感官测试**——**没有数值门槛**；
   - **量化路径（TTM-00466）**：平铺在亚克力板上 → BM gun 注液 → 0.25 PSI 滤纸反渗 → 称重，得到**回渗 BM 量**与**吸收 BM 量**。
3. **两条路径共用 BM Simulant A**（见 [[BM Simulant A（便液模拟液 A）]]），但稀释与注液量档位各自定义。
4. **注液量档位对应两个场景**：`insult`（宝宝单次平均，TTM-00466 为 11 mL）与 `blowout`（大量涌出，TTM-00466 为 30 mL；TTM-00234 的 BM gun 键名相同）。
5. **定位基准两套并存**：假人路径用"**纸尿裤后端边缘距 mannequin 后边缘**"（NB 13.9 / 1 号 20 / 2 号 24.3 mm）；台架路径用"**注液点距纸尿裤后边缘**"（NB 118 / 1 号 171 / 2 号 192 / 3 号 207 mm）。
6. **动作协议是可视化路径的可比性来源**：摇动 5 次来回 → 坐起 15 s → 重复 → 保持躺姿至注液后 5 min。

## 关键参数表 Key Parameters

| 参数 | 假人可视化（TTM-00234） | 台架量化（TTM-00466） | 出处 |
|---|---|---|---|
| BM 配方 | BM simulant A（配方按文内配方，原文未抄录） | BM simulant A : 生理盐水 = 3:1（稀便 Runny） | [[TTM-00234 Rock N Roll Mannequin BM Test With Movement.docx]]、[[TTM-00466 BM Benefit Visualization Validation.docx]] |
| 搅拌 | 原文未提 | 350 rpm × 30 s | [[TTM-00466 BM Benefit Visualization Validation.docx]] |
| 注液量 | Large 30 cc（Blowout）/ Small 1 cc（Insult），BM gun | 11 mL（insult）/ 30 mL（blowout） | [[TTM-00234 Rock N Roll Mannequin BM Test With Movement.docx]]、[[TTM-00466 BM Benefit Visualization Validation.docx]] |
| 注液位置 | 穿着位置：后端边缘距 mannequin 后边缘 13.9 / 20 / 24.3 mm（NB / 1 / 2） | 注液点距纸尿裤后边缘 118 / 171 / 192 / 207 mm（NB / 1 / 2 / 3） | [[TTM-00234 Rock N Roll Mannequin BM Test With Movement.docx]]、[[TTM-00466 BM Benefit Visualization Validation.docx]] |
| 等待时间 | 5 min（注液后） | 5 min（注液后） | 同上 |
| 载荷 / 动作 | 摇动 5 次来回 + 坐起 15 s（两轮） | 0.25 PSI 滤纸，压 30 s | 同上 |
| 喷嘴距离 | — | 约 240 mm | [[TTM-00466 BM Benefit Visualization Validation.docx]] |
| 液温 | — | 生理盐水 37±1 ℃ | [[TTM-00466 BM Benefit Visualization Validation.docx]] |
| 输出 | 干/湿重（纸尿裤、擦手纸）+ 照片 | 回渗 BM 量 = 滤纸湿−干；吸收 BM 量 = 纸尿裤湿−干 | 同上 |

> ⚠️ **禁止无来源参数**：表中数字均来自本 block 两份源摘要页。**BM 的两条路径均无通过门槛**（无 BM 泄漏量阈值、无回渗阈值），标 `[待验证]`。
> ⚠️ **同类方法差异（2026-09-29）**：两份方法**同日发布（2021-02-28）、同一第 0 版**，但注液量档（30 cc / 1 cc vs 11 mL / 30 mL）与定位基准（后边缘距 mannequin vs 注液点距后边缘）不同——**不可把两者当作同一实验的两种呈现**。

## 相邻概念 Adjacent Concepts

- 配方口径：[[BM Simulant A（便液模拟液 A）]]
- 尿液对应方法：[[Rewet Test（回渗测试）]]（公式同构、载荷不同）、[[Cradle Intake Test（Cradle 摄入测试）]]
- 部件侧：[[绒毛浆（Fluff Pulp）]]（BM 主要靠绒毛浆/无纺布滞留）、[[ADL（导流层）]]、[[分区密度设计]]
- 上位索引：[[芯体测试方法与验收基准（STM）]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[TTM-00234 Rock N Roll Mannequin BM Test With Movement.docx]]、[[TTM-00466 BM Benefit Visualization Validation.docx]]）：两份来源互证"BM 测试自成口径族"——同一天同一版本发布、共用 BM Simulant A 与 5 min 等待，但分别承担**可视化取证**与**量化读数**两种职能；本页结论与来源一致。

- **教训一（口径）**：**BM 的 Rewet 公式与尿液 Rewet 同构（湿−干），但压力（0.25 PSI）与压合时间（30 s）都更轻更短**；直接套用尿液回渗门槛会误判。
- **教训二（口径）**：**BM 注液点以"距后边缘"定位，与尿液的"距产品中心"不同基准**，换算前须核实产品几何。
- **教训三（用途）**：**假人路径的产出是照片，不是合格/不合格判定**；把它当验收门槛使用属误用。
- **待补 `[待验证]`**：BM gun 注液的速度/加速度列含义（提取件列对应不清）；BM Simulant A 的完整配方；两条路径与消费者实测的相关性。


> ✅ 验证（2026-09-29，来源 [[TTM-00467 BM Mannequin Absorption NB-S2（BM 假人吸收测试）]]）：本页「BM 测试自成口径族」再添一支，且**口径与既有来源显著不同**——TTM-00467 第 0 版（2021-02-28）用 **BM simulant A 400 mL（Normal）**或 **3:1 兑盐水 Runny（350 rpm × 30 s 配制）**，测试温度 **22 ± 1 ℃**（非 37 ℃），加载 **10 ± 1 英尺水柱**（同文件步骤 8 又写 10 **英寸**水柱，内部冲突，标 `[待验证]`），穿着位置 **13.9 / 20 / 24.3 mm**，盐水 **40 / 40 / 45 mL @ 4.1 mL/s** + BM **11 mL @ 20 mL/s**。**温度、压力、用量三项均不可与本页既有 0.25 PSI / 30 s 口径互比。**

## 来源 Sources

- [[TTM-00234 Rock N Roll Mannequin BM Test With Movement.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/BM测试方法/TTM-00234 Rock N Roll Mannequin BM Test With Movement.docx.md`
- [[TTM-00466 BM Benefit Visualization Validation.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/BM测试方法/TTM-00466 BM Benefit Visualization Validation.docx.md`
- [[TTM-00467 BM Mannequin Absorption NB-S2（BM 假人吸收测试）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/BM测试方法/TTM-00467 BM Mannequin Absorption NB-S2.docx.md`

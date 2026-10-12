---
type: concept
title: "Motion Mannequin Test（动态假人测试）"
domain: [卫材研发, 测试方法与表征]
status: growing
updated: 2026-09-29
tags: [假人, 漏尿性, 合身性, WI-63849, TTM-00318, 模拟液]
---

# Motion Mannequin Test（动态假人测试）

> 一句话定义：**动态假人测试**是在会行走/爬行的 mannequin（人体模型）上穿著真实产品，按预设「注液—运动」脚本运行，用**漏尿位置分区**与**合身性尺寸变化**两类读数，同时评价产品的**漏尿性（leakage）与合身性（fit）**。

## Definition 定义

与 [[Static Mannequin Test（静态假人测试）]]（TTM-00459-7 强制失效法）和 [[Mannequin BM Test（BM 假人测试）]]（TTM-00467 BM 吸收）并列，动态假人是本库第三条假人路线，也是**唯一带运动**的成品评价方法。

本体文件为 **WI-63849（第 0 版，2024-02-20）**，参考文稿为 **TTM-00313-8 Mannequin Wet and Dry Motion Fit Test**（[[Finished Product Testing Method Summary（成品测试方法汇总表）]] 中列作 **TTM-00318-8**，二者差一位数字，待人工核对）。

测试分两部分：**漏尿性**与**合身性**，参数与动作脚本在 Rockwell 平台的 Study Manager 中设定。

## 机理 / 结构拆解 Mechanism

1. **为什么必须运动**：静态载荷下芯体的吸收与贴合表现，与行走/爬行时的反复剪切、腿围开合完全不同；腿部间隙（LegGap）与耳贴束绳（Ear Roping）只在运动后出现。
2. **双轨校准**：液体校准（Volume 70 mL，允差 **± 3%**）与蠕动泵管路校准（管路尺寸 **17**，允差 **± 1%**）**每次测试前必做**；润洗用 300 mL 且**润洗液不可再用**，而校准流出液**可回倒贮存容器**。
3. **诊断价值在位置而非总量**：漏尿按 **17 个分区**记录（裆部/前/后腿、下/上侧、前/后腰中心与左右、外层），位置分布直接指向结构缺陷部位。
4. **合身性测的是「运动前后之差」**：前部下坠、后部下坠、裆部下坠、Tab-to-Tab 四项均须**测试前后各测一次**，差值才是运动的影响。
5. **模拟液不是纯盐水**：用 **0.1 g 牛黄酸胆酸钠（sodium taurocholate）+ 1 L 生理盐水**，搅拌 5–10 min，加热至 **37 ± 1 ℃**——表面活性剂改变了液体的表面张力与芯体润湿行为。

## 关键参数表 Key Parameters

| 参数 Parameter | 口径 / 数值 Value | 出处 Source |
|---|---|---|
| 模拟液 Simulant | 0.1 g 牛黄酸胆酸钠 + 1 L 生理盐水，磁力搅拌 5–10 min | [[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]] |
| 液温 Temperature | **37 ± 1 ℃** | 同上 |
| 润洗 Rinse | Station Delay 10 s、Flow Rate 15 mL/s、Volume **300 mL**；润洗液不可再用 | 同上 |
| 液体校准 Calibration | Volume **70 mL**；允差 **± 3%**；超差按 (Target WT − Actual WT)/Target WT 修正 Calibration 值 | 同上 |
| 手动校准触发 | 校准数值接近 **0.8 或 1.2** 时须手动校准蠕动泵 | 同上 |
| 蠕动泵管路 Tubing | 尺寸 **17**；管路校准误差须 ≤ **± 1%** | 同上 |
| 注液 Insult | **70 mL @ 15 mL/s** | 同上 |
| 时序 Sequence | Insult(1 s) → Crawl(30.0) → Insult(2 s) → Crawl → Insult(2 s) → Loop(Step 2, Count 2) → Insult(30 s) → Complete | 同上 |
| 漏尿分区 Leak locations | **17 区** | 同上 |
| Tab Spacing | Koopa(Step 2) **20**；Yoshi **19**；Mario **22**；Luigi **30**；Kirby **38 mm**；Pants 跳过 | 同上 |
| Panel shift 标记 | 上下各一条 **10 mm** 垂直线，测试后测两线间距 | 同上 |
| 适用形态 Scope | 合身性**主要针对 Diaper**；Pants 需另议；**不含 FIA** | 同上 |

> ⚠️ **禁止无来源参数**：表中数字全部来自 [[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]]。漏尿性判定门槛、合身性六项的合格范围、Crawl 速度 30.0 的单位，原文均未给出 `[待验证]`。

## 相邻概念 Related Concepts

- 上位 / 相关：[[Static Mannequin Test（静态假人测试）]]、[[Mannequin BM Test（BM 假人测试）]]、[[芯体测试方法与验收基准（STM）]]
- 平台：[[Mannequin Lab（Rockwell 假人平台）]]
- 机理相关：[[尿液模拟液（Urine Analog）]]、[[Run-off & Leakage Test（滑渗与渗漏测试）]]、[[Skin Contact Pressure（皮肤接触压力）]]、[[Elastic Tension & Creep（橡筋张力与回缩率）]]
- 对比：[[GB-T 28004.1-2021 与 KC STM 成品吸收性能测试方法对比]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]]、[[Finished Product Testing Method Summary（成品测试方法汇总表）]]）：两份来源互证「动态假人是独立于静态假人与 BM 假人的第三条路线」，且成品总表确认其在 OD 与 Pants 两形态均适用。

- **教训一（口径）**：**模拟液必须写明是否含牛黄酸胆酸钠**。「盐水」与「含胆盐的尿液模拟液」在芯体润湿行为上不同，漏尿数据不可跨体系比较。
- **教训二（流程）**：**校准是双轨的，只做一轨等于没校准**。± 3%（液体）与 ± 1%（管路）是两个独立允差。
- **教训三（设计）**：**合身性的读数是差值不是绝对值**。只报「下坠 X mm」而无运动前基准，无法判断是产品问题还是穿戴问题。
- **待补 `[待验证]`**：TTM-00313-8 与 TTM-00318-8 的编号分歧；漏尿判定门槛；Crawl 速度单位；FIA（WI-45237）与本方法的关系。

## 来源 Sources

- [[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/WI-63849 Motion mannequin.docx.md`
- [[Finished Product Testing Method Summary（成品测试方法汇总表）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/Finished Product Testing Method Summary.xlsx.md`

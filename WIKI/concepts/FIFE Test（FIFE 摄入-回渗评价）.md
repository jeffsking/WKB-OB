---
type: concept
title: "FIFE Test（FIFE 摄入-回渗评价）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-29
tags: [FIFE, STM-00034, 摄入时间, 回渗, 溢出量, SAT CAP, 吸收性能, 目标区]
aliases: ["Fluid Intake Flowback Evaluation", "FIFE 法", "STM-00034"]
---

# FIFE Test（FIFE 摄入-回渗评价 / Fluid Intake Flowback Evaluation）

> 一句话定义：**FIFE** = Fluid Intake Flowback Evaluation（液体摄入—回渗评价），KC 成品吸收性能的**母方法**：在 FIFE 板上按体重档位做多次定量注液并计时（摄入），再转移到 **SAT CAP**（Saturated Capacity，饱和容量）测试仪上于负压下压 2 min 用滤纸增重测**回渗（flowback）**，同时用侧漏滤纸捕获**溢出量（run-off）**。

## Definition 定义 / Principle 原理

FIFE 把「穿在身上的吸收体验」拆成三个可测输出：**吸收时间（intake time）**、**溢出量（run-off / 侧漏）**、**回渗量（flowback）**。一次实验即产出三次吸收时间、每次的溢出量与一次回渗量，是成品放行与配方对比的主力方法（编号 **STM-00034**）。

两段结构：

1. **FIFE 板段（摄入）**——底板中央 **75 × 150 mm（3 × 6 in）凸台**，试样**面层朝上**、目标区对准凸台中央，上盖板圆柱开口插入漏斗居中注液；底板凸台两侧各放一张预称重溢出滤纸（**88 × 300 ± 13 mm**）收集侧流液体。
2. **SAT CAP 段（回渗）**——第二次注液后转移到 SAT CAP，面层朝上居中，放 **1 张 238 × 300 ± 13 mm** 或 **2 张 88 × 300 ± 13 mm** 预称重回渗滤纸（距前端绒毛边缘约 **6 mm**），盖乳胶膜抽真空至 **14 ± 1 inH₂O（= 3.4 kPa / 3447 Pa）**维持 **2 min**；回渗量 = 湿滤纸重 − 干滤纸重。

## 方法口径 Caliber（引用必须带口径）

| 项目 Item | 口径 Condition | 出处 Source |
|---|---|---|
| 加液量 Insult amount | 按体重分档 **35 / 50 / 65 / 80 / 100 mL**（各 ± 0.5 mL） | [[STM-00034 FIFE - Fluid Intake Flowback Evaluation Rev.5（FIFE 摄入-回渗评价全球方法）]] |
| 目标真空 Target vacuum | **14 ± 1 inH₂O = 3.4 kPa**（南京译本写 3447 Pa） | 同上、[[STM-00034 FIFE Nanjing Edition（FIFE 吸收时间与溢出量·南京厂第5版）]] |
| 回渗判定载荷 Flowback loading | **0.5 psi** | [[STM-00034 FIFE - Fluid Intake Flowback Evaluation Rev.5（FIFE 摄入-回渗评价全球方法）]] |
| 设备安全上限 Equipment limit | **> 2.0 psi 有内爆（implode）风险** | 同上 |
| 保压时间 Hold time | **2 min**；legacy 控制器含升压时间（≤ 30 s），触屏版 10 inH₂O 起计时 | 同上 |
| 目标区 Target zone | 全球版按**体重 × 性别**三档（Unisex 89–146、Male 76–114、Female 121–152 mm，± 6 mm）；**中国区 Unisex 102 / 114 / 127 / 146 / 146 mm（ST1–ST5）** | 同上、[[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] |
| 吸收时间判据 Criterion | **圆柱孔边缘的测试液颜色消失**即停表，精度 **0.01 s**；计时起点为溶液接触漏斗壁 | [[STM-00034 FIFE Nanjing Edition（FIFE 吸收时间与溢出量·南京厂第5版）]] |
| 注液间隔 Interval | 第二次距第一次 **1 min ± 5 s**；第三次在**释放压力 1 min 后** | 同上 |
| 测试液 Test liquid | **0.9% 盐水** + 染色液（粉体染料约 1 g 溶于 1 L 蒸馏水，取约 4 mL 加入 1 L 盐水） | 同上 |
| 密封液 Sealant | SAT CAP 与乳胶膜密封**仅可用 0.9% 盐水**，禁自来水 / 蒸馏水 | 同上 |
| 弹性处理 Elastics | 腿部与折页松紧带**每隔 0.5 in 剪开**（不剪掉、不伤密封线与绒毛） | 同上 |

## 三份文件的加液档位分歧 Version Discrepancy

| 版本 Version | Step1 | Step2 | Step3 | Step4 | Step5 | Step6 |
|---|---|---|---|---|---|---|
| 全球版 Rev.5（按体重分档） | 35 | 50 | 65 | 80 | 100 | — |
| WI-56234 第 5 版（2020-09-28） | 35 | 50 | 65 | 80 | 100 | 100 |
| **南京厂第 5 版（2021-08-24）** | **50** | **65** | **80** | **100** | **100** | **100** |

> 🔴 **manual_review（2026-09-29）**：同为 STM-00034「第 5 版」，南京厂文件与 WI-56234 的加液档位**整体错开一档**（南京厂取消 35 mL 档）。可能原因：适用尺码范围不同 / 本地化改档未同步 / 其中一份旧版误标。**在人工核对 EtQ 方法主档前，引用 FIFE 加液量必须注明具体文件与修订日期**——依 AGENTS.md §5 仅标记，不裁决。

## 与相邻方法的边界 Boundary

- **FIFE vs Cradle**：Cradle（TTM-00148）在模拟穿着姿态的弧形槽上注液，偏**姿态敏感性**；FIFE 在水平凸台上注液，偏**标准化可比性**。两者的吸收时间不可互换（详见 [[Cradle Intake Test（Cradle 摄入测试）]]）。
- **FIFE vs 单纯回渗法**：FIFE 的回渗是「三次注液后的饱和态回渗」，与 [[Rewet Test（回渗测试）]] 中按固定注液次数的回渗不是同一状态。
- **FIFE vs 国标**：GB/T 28004.1-2021 用 **36 ± 1 ℃、40/60/80 mL、2.0/4.0 kPa、5 片均值**，与 FIFE 的 **37 ℃、35–100 mL、3.4 kPa** 不可互比（详见 [[GB-T 28004.1-2021 与 KC STM 成品吸收性能测试方法对比]]）。

## 经验教训 Lessons

- **教训一（单位）**：**14 ± 1 inH₂O = 3.4 kPa = 3447 Pa** 是本库压力换算锚点；0.5 psi 回渗载荷仅见于全球版，中文译本未出现，对外引用建议核对 SAT CAP 设备铭牌 `[待验证]`。
- **教训二（判据）**：吸收时间的终点是「**圆柱孔边缘颜色消失**」，是**表观摄入时间**而非完全吸收——跨实验室比较时必须确认判据一致。
- **教训三（安全）**：乳胶膜堵住通气孔会内爆；SAT CAP 按 0.5 psi 设计，**2.0 psi 为硬上限**。
- **教训四（版本）**：目标区全球版允许「国际变体」（Note 18），中国区取值不同，**引用须注明全球版或中国版**。
- **待补 `[待验证]`**：南京厂第 2、3 次吸收是否使用相同液量档位；SAT CAP 加载面积。

## 相邻概念 Related

- 同类摄入：[[Cradle Intake Test（Cradle 摄入测试）]]、[[Acquisition Test STM-00060（导流性能测试）]]
- 输出项：[[Rewet Test（回渗测试）]]、[[Run-off & Leakage Test（滑渗与渗漏测试）]]、[[Retention Capacity Test（滞留能力测试）]]
- 上位索引：[[芯体测试方法与验收基准（STM）]]
- 试剂：[[尿液模拟液（Urine Analog）]]
- 对比：[[GB-T 28004.1-2021 与 KC STM 成品吸收性能测试方法对比]]

## 来源 Sources

- [[STM-00034 FIFE - Fluid Intake Flowback Evaluation Rev.5（FIFE 摄入-回渗评价全球方法）]] —— 全球母版，Rev.5
- [[STM-00034 FIFE Nanjing Edition（FIFE 吸收时间与溢出量·南京厂第5版）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-00034 FIFE.docx.md`
- [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/BCC成品STM-南京南厂 1.pdf.md`

## Related Sources 关联来源

- [[CI-06 COCO V6 3rd round trial-10.10]]
- [[CI-06 COCO V6 3rd round trial-9.30]]
- [[COCO_V6_第三轮trial_两组对照分析_20261010]]
- [[History of FIUP TTM-00643（FIUP 测试方法沿革史）]]
- [[IMA知识库索引_20261002]]
- [[Intake Systems Development Pathway 2023（摄入系统开发通路）]]
- [[MD Pants innovation_YK R&E]]
- [[TTM-00302 面层干爽性.doc]]
- [[满足要求的四大组件性能指标与测试方法]]

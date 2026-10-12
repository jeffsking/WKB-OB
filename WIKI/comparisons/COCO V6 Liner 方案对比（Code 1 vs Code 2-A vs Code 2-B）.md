---
type: comparison
title: "COCO V6 Liner 方案对比（Code 1 vs Code 2-A vs Code 2-B）"
subjects: ["[[ATB双梳理面层（Dual-Card Topsheet）]]", "[[三叶形截面纤维（Trilobal Fibre）]]"]
dimension: 综合
updated: 2026-09-29
tags: [Liner, 面层, 对比, ATB, 三叶形, 成本, 供应链风险, COCO V6]
---

# COCO V6 Liner 方案对比（Code 1 vs Code 2-A vs Code 2-B）

> 对比对象：COCO V6 试产的三个面层方案。回答"50 gsm 还是 30 gsm、上层要不要保留三叶形、哪个先上机"。
> 数据口径 2026-09-11 准备会 + 2026-09 CI-06 试产实测。

## 对比维度表

> 必含「成本」与「供应链风险」两列。

| 维度 | Code 1 | Code 2-A（优先） | Code 2-B（备选） | 依据 |
|---|---|---|---|---|
| **结构：总克重** | 50 gsm | 30 gsm | 30 gsm | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| **结构：上层 15/25 gsm 组成** | 25 gsm = 10% 三叶形 + 90% 2D Bico PE/PET | 15 gsm = 10% 三叶形 + 90% 2D（同 Code 1 半克重） | 15 gsm = **100% 2D（去除三叶形）** | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| **结构：下层组成** | 25 gsm = 50% 三叶形 + 50% 4D | 15 gsm = 50% 三叶形 + 50% 4D | 15 gsm = 50% 三叶形 + 50% 4D | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| **规格：宽 × 长** | 102 mm × >100 m（3″ core，卷径 ≤700 mm） | 82 mm × 6 km（含 spooling，core ≤600 mm） | 82 mm × 6 km（同上） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| **生产 / 交付站点** | 天津 | 川越 | 川越 | [[COCO V6 试产原料准备会（英文版，2026-09-11）]] |
| **优先级（原文）** | — | **优先** | 备选 | [[COCO V6 试产原料准备会（英文版，2026-09-11）]] |
| **性能（设计口径）** | 三叶形 30%（15 gsm），皮肤侧 5%；MD 分布增益 +30%（v2 Final）/ +15%（Summary）⚠️；CD 拉伸 9.3 N/50mm | 同配方半克重，**设计口径指标未单独给出** `[待验证]` | 上层去三叶形 → MD 沟槽导流**弱于 A**（推断，非原文结论） | [[COCO V6 试产原料准备会（v2 Final）]]、[[COCO V6 试产原料准备会（Summary 版）]] |
| **性能（实测，CI-06）** | 基重 **45.222 gsm**（标称 50）、厚度 1.721 mm、STT 0.874 s、返渗 0.0382 g、层间剥离 115.276 N、pH 7.112 | **未到货，暂不测试** | **不测试** | [[CI-06 COCO V6 第三轮试产测试结果]] |
| **成本** | `[待验证]`——本批**无任何 Liner 报价数据** | `[待验证]` | `[待验证]`（克重减半预期省料，但原文未给成本结论，**不做推断**） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| **供应链风险（到货）** | **低**：按期到天津，且完成实测 | **高：截至数据导出仍未到货** | **高：标注"不测试"** | [[CI-06 COCO V6 第三轮试产测试结果]] |
| **供应链风险（关键原料依赖）** | **高：依赖三叶形纤维（福地）供给** | 高：同上 | **中低：上层去掉三叶形，正是为样本量不足准备的降级方案** | [[COCO V6 试产原料准备会（英文版，2026-09-11）]]、[[福地（Fudi）]] |
| **供应链风险（克重偏离）** | **高：实测 45.222 vs 标称 50，偏离约 -9.6%** | 未见数据 | 未见数据 | [[CI-06 COCO V6 第三轮试产测试结果]] |
| **适用场景** | 全功能验证件（三叶形完整、克重高） | **优先验证件**（省料、便于上机） | 异型纤维供应不足时的**替代/放量件** | [[COCO V6 试产原料准备会（英文版，2026-09-11）]] |

> 尾注：本表数字来自 [[Coco V6 试产原料清单（Raw material list v3.0）]]、[[COCO V6 试产原料准备会（英文版，2026-09-11）]]、[[COCO V6 试产原料准备会（v2 Final）]]、[[COCO V6 试产原料准备会（Summary 版）]]、[[CI-06 COCO V6 第三轮试产测试结果]] 五份源摘要页。**成本维度无来源，全部标 `[待验证]`。**

> ⚠️ **跨来源差异（2026-09-29，待人工确认）**：面层 **MD 分布增益**在 v2 Final 记 **+30%**、Summary 记 **+15%**，两版同日期，**本页不裁决**。

> 🔴 **manual_review（2026-09-29）**：本表含**试产配方比例、供应关系与"哪个方案优先"的选择倾向**（AGENTS.md §5 边界）。页面按内部追溯保留；对外引用前须人工确认。

## 各自适用场景

- **Code 1（50 gsm）**：三叶形配比完整（30%）、克重最高——**用来看"设计上限"与手感/导流的最优组合**；本批唯一完成来料实测的 Liner 方案。
- **Code 2-A（30 gsm，优先）**：Code 1 的**半克重版**，配方不变——省料、卷长 6 km 适合上机，是**优先验证件**；但截至数据导出**尚未到货**，"优先"与实际进度存在落差。
- **Code 2-B（30 gsm，备选）**：**上层去掉三叶形**——本质是"三叶形纤维不够时"的降级方案，代价是牺牲上层 MD 沟槽导流。

## 结论

三个方案的差异只有两点：**总克重（50 vs 30）** 与 **上层是否用三叶形**。Code 2-A 被标为优先，但因为**关键原料（三叶形纤维）样本量受限**，Code 2-B 的降级路径必须与 A 并行推进；同时 **Code 1 实测克重比标称低约 9.6%**，说明来料克重管控本身就是一个独立风险点——**在补齐 Code 2-A / 2-B 数据前，Liner 方案无法定论**。

## 来源

- [[Coco V6 试产原料清单（Raw material list v3.0）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Raw material list for Coco V6 trial.xlsx.md`
- [[COCO V6 试产原料准备会（英文版，2026-09-11）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_EN.pptx.md`
- [[COCO V6 试产原料准备会（v2 Final）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_v2_Final.pptx.md`
- [[COCO V6 试产原料准备会（Summary 版）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_Summary.pptx.md`
- [[CI-06 COCO V6 第三轮试产测试结果]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/CI-06 COCO V6 3rd round trial.xlsx.md`

---
type: comparison
title: "SAP Zoned Blend vs Mono Design（分区混掺 vs 单牌号均布 · SAP 设计对比）"
subjects: ["[[Multilayer SAP Core（多层SAP芯体）]]", "[[分区密度设计]]"]
dimension: 综合
updated: 2026-09-29
tags: [SAP, 分区布点, 混掺, 单牌号, 容量裕度, 供应链复杂度]
---

# SAP Zoned Blend vs Mono Design（分区混掺 vs 单牌号均布 · SAP 设计对比）

## 对比维度表 Comparison Matrix

> 必含「成本 Cost」与「供应链风险 Supply Chain Risk」两列。

| 维度 Dimension | Design A（分区 · NR-610S/NR-950） | Design C（分区 · KC511/NR-950） | Design B（单牌号 KC511 均布） | 依据 Source |
|---|---|---|---|---|
| 结构 | 分区靶向（insult-targeted zoning） | 分区靶向（与 A 同图形） | 按面积均布、无靶向 | [[Three-Way SAP Design Comparison（三方案 SAP 设计仿真对比）]] |
| poly 混掺 | 40% NR-610S + 60% NR-950 | 40% KC511 + 60% NR-950 | 100% KC511 | 同上 |
| 总添加量 | 15.0 g | 15.0 g | 15.0 g | 同上（等量对照） |
| 峰值分区饱和度 | 76%（Back） | **67%（Back）** | **129%（Crotch 溢出）** | 同上 |
| 混掺 AUL（0.7 psi） | 16.5 g/g | **19.0 g/g** | 18.4 g/g | 同上 |
| 混掺 GBP | 7.2 | 14.4 | **24（本组最佳）** | 同上 |
| 快吸组分 vortex | **19 s（可得最快）** | 29 s | 29 s | 同上 |
| 摄入速度（模型外） | 最快（模型未计分） | 次快 | 次快 | 同上（caveat） |
| **成本 Cost** | 3 个牌号并行，认证与切换成本最高 | **2 个牌号，容量裕度更好 → 单位性能成本更优** | 1 个牌号（采购最简），但裆部溢出 129% → **仅作成本备选（cost fallback）** | 同上（SKU 数 + "carry forward only as a cost fallback"原文判读） |
| **供应链风险 Supply Chain Risk** | **3 个 SKU 需认证**，供应商与批次管理面最广 | **2 个 SKU**，比 A 少一个牌号，认证与供货风险同步下降 | **1 个 SKU 风险最低**，但**性能风险最高**：裆部溢出是漏尿信号，与混掺选择无关 | 同上（"SKUs to qualify"行 + B 的溢出判读） |
| 适用场景 | 摄入速度被证实为瓶颈时（面层湿感、strike-through 敏感） | 摄入时间达标时的**首选默认** | 仅作成本备选；不得作为主方案 | 同上（决策规则） |

> 尾注 Footnote：本表所有数字均来自 [[Three-Way SAP Design Comparison（三方案 SAP 设计仿真对比）]]，为**仿真模型口径**（385×110 mm 沙漏芯体、6 月龄婴儿、3 次连续排尿、总添加量 15.0 g 等量对照），非实测；**成本**列不含任何报价，仅以需认证 SKU 数与原文"cost fallback"判读表征。

## 各自适用场景 Where Each Design Fits

- **Design A**：当台架 cGAM-LTD 测试证明**摄入速度差确实转化为面层湿感/strike-through 差异**时的方案——用 NR-610S 的 19 s vortex 换首次瞬吸，代价是容量裕度（76%）与渗透（GBP 7.2）较弱、且要多认证一个牌号。
- **Design C**：**默认首选**——若其摄入时间仍在规格内，则以更少 SKU 换更好的容量裕度（67%）与渗透（GBP 14.4），且把快吸组分统一为 KC511 简化采购。
- **Design B**：**不得作为主方案**。单牌号均布在裆部溢出 129%，原文明确其"无论混掺如何都是漏尿风险信号"，仅保留为成本备选。

## 结论 Conclusion

在总添加量相同的等量对照下，**分区靶向是必要条件，混掺组分是优化变量**：均布单牌号（B）会溢出裆部，而把混掺中的快吸组分由 NR-610S 换成 KC511（A→C）可在少一个 SKU 的同时全面改善容量与渗透，唯一代价是摄入速度——因此**最终选择取决于台架摄入时序测试，而非容量模型本身**。

## 来源 Sources

- [[Three-Way SAP Design Comparison（三方案 SAP 设计仿真对比）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP_Three_Way_Design_Comparison.pptx.md`

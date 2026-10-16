---
type: concept
title: "结构性常数 K"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [K-constant, capillary-flow, absorbency-rate, nonwovens, modeling]
---

# 结构性常数 K

> 📌 **Page completed 2026-09-30** from 1 citing source. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

Structural constant K：在高蓬松非织造布吸液速率模型 Q = (π·γ·r·cosθ·T)/(K·η·W)（Eq. 11）中，表征实际毛细网络偏离理想 Washburn 毛细管程度的经验常数。K = 1 为理想值；实测 K ≈ 4–10（源：[[Fluid Absorption in High Bulk Nonwovens]]）。来源页明确承认 K 无理论预测模型。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 实测 K 范围 | ≈ 4–10（理想 K = 1）；理想模型高估速率 0.5–1 个数量级 | （源：[[Fluid Absorption in High Bulk Nonwovens]]） |
| 面密度影响 | 40 g/m² K ≈ 4.4；160 g/m² K ≈ 5.4 | （源：[[Fluid Absorption in High Bulk Nonwovens]]） |
| 针刺影响（NI 0 → N3） | 平均 K 5.3 → 4.8 | （源：[[Fluid Absorption in High Bulk Nonwovens]]） |
| 纤维类型 | PP（假设）50–70；rayon ~30 | （源：[[Fluid Absorption in High Bulk Nonwovens]]） |
| 验证工况 | PP(9)/RT(3) 50/50, 120 g/m²：实测 3.13，预测 23.8–29.7，K ≈ 7.6–9.5（Table 20） | （源：[[Fluid Absorption in High Bulk Nonwovens]]） |

## Method / Mechanism 方法 / 机理

K 偏离 1 的三个来源（原文列举）：(1) 真实纤网孔径/形状分布不均且孔壁不完整；(2) 毛细通道曲折（tortuous）而非直管；(3) 流体渗入并使纤维溶胀。与 [[Washburn Equation]] 的理想直管假设对立；容量 C 由 [[每克厚度 T／W]] 干净预测，速率 Q 必须引入 K 才能闭合（源：[[Fluid Absorption in High Bulk Nonwovens]]）。

## Hygiene Relevance 卫材关联

- 芯体设计准则：Q 的一阶原理预测只能当上界使用，速率必须靠实验标定 K（源：[[Fluid Absorption in High Bulk Nonwovens]]）。
- 适度针刺降低 K（提速且更可预测），过度针刺堵塞通道（源：[[Fluid Absorption in High Bulk Nonwovens]]）。
- 测试需用 1% NaCl 而非纯水（GATS：[[GATS 重力吸收测试]]），水体系系统性高估速率（源：[[Fluid Absorption in High Bulk Nonwovens]]）。

## Open Questions 待补

- K 与纤维截面形状（三叶形 rayon 等）的定量关系
- 复合芯体（SAP + 绒毛浆）中 K 的取值方法

## Related Sources 关联来源

- [[Fluid Absorption in High Bulk Nonwovens]]
- 父书：[[Absorbent Technology]]
- 相关联概念：[[Washburn Equation]]、[[每克厚度 T／W]]、[[GATS 重力吸收测试]]、[[SAP（高吸水树脂）]]、[[绒毛浆（Fluff Pulp）]]

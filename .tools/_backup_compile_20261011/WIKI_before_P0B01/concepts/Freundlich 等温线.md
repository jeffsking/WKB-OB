---
type: concept
title: "Freundlich 等温线"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [sorption-isotherm, diffusion, reaction-diffusion, SAP, Crank]
---

# Freundlich 等温线

> 📌 **Page completed 2026-09-30** from 1 citing source. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

Freundlich 等温线指扩散-化学反耦合框架中**非线性等温线** `S = R·Cⁿ` 的 **n < 1** 情形（幂律型）；此时等效扩散系数 `D` 随含水率上升，表现为**后期加速**（源：[[Diffusion and Chemical Reaction (Crank Ch.14)]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 非线性等温线形式 | `S = R·Cⁿ` | [[Diffusion and Chemical Reaction (Crank Ch.14)]] |
| n < 1（Freundlich 型） | 等效 D 随含水率上升 → 后期加速 | [[Diffusion and Chemical Reaction (Crank Ch.14)]] |
| n > 1 | 等效 D 下降 → 饱和减速 | [[Diffusion and Chemical Reaction (Crank Ch.14)]] |
| 线性等温线（瞬时线性反应） | `S = R·C`，等效 `D_eff = D/(R+1)` | [[Diffusion and Chemical Reaction (Crank Ch.14)]] |
| SAP 交联网络水固定化 | 等效 D 下降 `(R+1)` 倍 | [[Diffusion and Chemical Reaction (Crank Ch.14)]] |

## Method / Mechanism 方法 / 机理

- **瞬时线性反应**：`S = R·C` → 等效 `D_eff = D/(R+1)`；SAP 交联网络把水**固定化**，使等效扩散系数下降 `(R+1)` 倍（源：[[Diffusion and Chemical Reaction (Crank Ch.14)]]）。
- **非线性等温线决定加速/减速**：`n < 1` 对应后期加速（Freundlich 型），`n > 1` 对应饱和减速（源：[[Diffusion and Chemical Reaction (Crank Ch.14)]]）。
- 吸附等温线亦可用于提取平衡吸附常数（Langmuir Eq 7.2，由等温线提取 SK ≡ Q）（源：[[Smart Polymers Ch07 Imprinting Using Smart Polymers]]）。

## Hygiene Relevance 卫材关联

- **SAP 吸水「慢」的分子尺度原因**：水被固定化在交联网络中，等效 D 下降，故吸液呈现时间依赖（源：[[Diffusion and Chemical Reaction (Crank Ch.14)]]）。
- **应用场景**：SAP 交联网络水固定化、**湿巾抗菌剂缓释**、**芯体酶/化学剂扩散反应**（源：[[Diffusion and Chemical Reaction (Crank Ch.14)]]）。

## Open Questions 待补

- 卫材体系（绒毛浆 / SAP / 芯体）中 `R`、`n` 的实测取值：[待补]
- 与毛细压力 / 达西流模型的耦合口径：[待补]

## Related Sources 关联来源

- [[Diffusion and Chemical Reaction (Crank Ch.14)]]
- [[Mathematics of Diffusion]]
- [[反应-扩散耦合 Reaction-Diffusion]]
- [[SAP（高吸水树脂）]]
- [[Smart Polymers Ch07 Imprinting Using Smart Polymers]]
- [[Absorbent Product Testing]]

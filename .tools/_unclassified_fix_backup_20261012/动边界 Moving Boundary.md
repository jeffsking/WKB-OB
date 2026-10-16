---
type: concept
title: "动边界 Moving Boundary"
domain: [卫材研发, 待归类]
status: growing
updated: 2026-09-30
tags: [diffusion, sap-swelling, stefan-problem, non-fickian, absorbency-modelling]
---

# 动边界 Moving Boundary

> 📌 **Page completed 2026-09-30** from 5 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**动边界（moving boundary）**, as recorded in the vault：**'不可逆瞬时固定反应'的数学等价** —— 一个**尖锐边界表面在介质中移动**（源：[[Moving Boundaries (Crank Ch.13)]]）.

Its mathematical structure is the **Stefan problem**（相变问题）—— equivalent to an **ice-melting front** — so it can be handled with mature Stefan tools（erfc solutions, conservation conditions）（源：[[Moving Boundaries (Crank Ch.13)]]、[[Stefan 问题]]）.

（中文：动边界 = "不可逆瞬时固定反应"的数学等价——尖锐边界在介质中移动；数学结构 = Stefan 相变问题（冰融化前沿），可用成熟 Stefan 工具处理。）

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Moving-boundary equivalence | **不可逆瞬时固定反应**（§13.1） | [[Moving Boundaries (Crank Ch.13)]] |
| Stefan-problem equivalence | **数学结构等价**（§13.1） | [[Moving Boundaries (Crank Ch.13)]]、[[Stefan 问题]] |
| SAP swelling front | **凝胶–玻璃界面**（gel–glass interface） | [[Moving Boundaries (Crank Ch.13)]] |
| Behind the front | **全湿凝胶，D 大**（fully wet gel） | [[Moving Boundaries (Crank Ch.13)]] |
| Ahead of the front | **干态玻璃，D ≈ 0**（dry glass） | [[Moving Boundaries (Crank Ch.13)]] |
| Front motion | 边界以**恒定或变速**推进 | [[Moving Boundaries (Crank Ch.13)]] |

## Method / Mechanism 方法 / 机理

1. **Reuse mature Stefan machinery.** Because the moving-boundary structure equals an ice-melting front, the vault reads it as solvable with established Stefan tools — **erfc solutions and conservation conditions** — rather than developing new mathematics（源：[[Moving Boundaries (Crank Ch.13)]]、[[Stefan 问题]]）.
2. **SAP mapping — the swelling front is a phase front.** The **gel–glass interface** is the moving boundary: behind it the polymer is a **fully wet gel（D large）**, ahead it is **dry glass（D ≈ 0）**; the front advances at constant or variable speed（源：[[Moving Boundaries (Crank Ch.13)]]、[[SAP（高吸水树脂）]]）.
3. **It is the quantitative realisation of the Case II / non-Fickian transition.** The moving-boundary model **supplements the deficiency of the D(C) form of Fick's law in the glassy state** — the vault positions it as the numerical implementation of the Ch.11 Case II / non-Fickian transition zone（源：[[Moving Boundaries (Crank Ch.13)]]、[[Non-Fickian Diffusion (Crank Ch.11)]]、[[Case II 扩散]]）.
4. **Position within the diffusion text.** *Mathematics of Diffusion* organises Ch.13 as *"动边界/Stefan 问题：SAP 溶胀前沿的定量实现"* — item 8 of its 15-chapter map（源：[[Mathematics of Diffusion]]）.

## Hygiene Relevance 卫材关联

- **SAP swelling kinetics.** This is the vault's chosen quantitative route for the **dry→wet transition of a SAP particle** — the front where superabsorbent swelling actually happens, which a plain Fickian D(C) model cannot describe（源：[[Moving Boundaries (Crank Ch.13)]]、[[SAP（高吸水树脂）]]）.
- **Absorbent-core modelling.** Along with Fick's laws, D(C) methods and non-Fickian classification, the moving-boundary chapter is listed as part of the theoretical foundation for **SAP swelling kinetics, absorbent-core modelling and wet-migration simulation**（源：[[Mathematics of Diffusion]]、[[Fick 定律]]、[[湿迁移 Wet Migration]]）.
- **Neighbouring vault pages**：[[Non-Fickian Diffusion (Crank Ch.11)]]、[[Case II 扩散]]、[[Fick 定律]]、[[Stefan 问题]]、[[SAP（高吸水树脂）]]（源：[[Moving Boundaries (Crank Ch.13)]]）.

## Open Questions 待补

- **No parameterised Stefan problem for a real SAP / urine system** is recorded in the vault's excerpt `[待补]`.
- **No measured front velocity, D value behind/ahead of the front, or gel–glass interface thickness** is given（源：[[Moving Boundaries (Crank Ch.13)]]）.
- **How the front interacts with gel blocking / salt** is not addressed in the cited excerpt `[待补]`.

## Related Sources 关联来源

- [[Moving Boundaries (Crank Ch.13)]]（本页主体来源）
- [[Mathematics of Diffusion]] · [[Non-Fickian Diffusion (Crank Ch.11)]] · [[Case II 扩散]] · [[Fick 定律]]
- [[SAP（高吸水树脂）]] · [[Stefan 问题]] · [[湿迁移 Wet Migration]]

---
type: concept
title: "Case II 扩散"
domain: [卫材研发, SAP与流体]
status: growing
updated: 2026-09-30
tags: [diffusion, non-fickian, sap-swelling, glassy-polymer, absorbency-modelling]
---

# Case II 扩散

> 📌 **Page completed 2026-09-30** from 5 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**Case II diffusion** is one class in the **Alfrey–Gurnee–Lloyd three-way classification** of sorption kinetics, defined by the ratio of diffusion to relaxation rate：**Case II = 扩散速率 >> 松弛速率**（rapid solvation／快速溶剂化）（源：[[Non-Fickian Diffusion (Crank Ch.11)]]）.

（中文：Case II 是 Alfrey–Gurnee–Lloyd 三分类中的一类——**扩散速率远大于松弛速率**（快速溶剂化）。）

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Three-way classification | **Case I / Case II / 非菲克**（§11.1） | [[Non-Fickian Diffusion (Crank Ch.11)]] |
| Case I（Fickian） | **扩散 << 松弛** | [[Non-Fickian Diffusion (Crank Ch.11)]] |
| **Case II** | **扩散 >> 松弛**（快速溶剂化） | [[Non-Fickian Diffusion (Crank Ch.11)]] |
| 非菲克（non-Fickian） | **扩散 ≈ 松弛** | [[Non-Fickian Diffusion (Crank Ch.11)]] |
| SAP phase sequence | **干态玻璃态 → Case II → 非菲克 → 橡胶态 Case I** | [[Non-Fickian Diffusion (Crank Ch.11)]] |

## Method / Mechanism 方法 / 机理

1. **It is the physical root of the S-shaped sorption curve.** SAP maps onto the sequence **干态玻璃态 → Case II → 非菲克 → 橡胶态 Case I**, and these three stages correspond to different segments of the **S 形吸液曲线**（S-shaped absorption curve）（源：[[Non-Fickian Diffusion (Crank Ch.11)]]、[[Fick 定律]]）.
2. **The underlying physics is a glass → rubber transition.** SAP's dry state is a **glass（T_g above ambient）**; swelling drops T_g and moves the material into the **rubbery state** — the two regions have *completely different* D and transport mechanisms（源：[[Non-Fickian Diffusion (Crank Ch.11)]]、[[SAP（高吸水树脂）]]）.
3. **Key limit — a glassy polymer cannot be described by the D(C) form of Fick's law**; the rubbery state is generally Fickian（源：[[Non-Fickian Diffusion (Crank Ch.11)]]、[[Fick 定律]]）.
4. **It needs the moving-boundary model to close.** The vault states that the glassy-state gap is filled by the **moving-boundary model（Ch 13）**, i.e. the **Stefan-problem** treatment of the swelling front（源：[[Non-Fickian Diffusion (Crank Ch.11)]]、[[Moving Boundaries (Crank Ch.13)]]、[[动边界 Moving Boundary]]、[[Stefan 问题]]）.

## Hygiene Relevance 卫材关联

- **SAP absorption kinetics.** Case II is the early, fast-solvation stage of a SAP particle's uptake — the segment that sets how quickly a dry particle starts to swell（源：[[Non-Fickian Diffusion (Crank Ch.11)]]、[[SAP（高吸水树脂）]]）.
- **Absorbent-core modelling.** The non-Fickian classification sits with Fick's laws, D(C) methods and moving boundaries as part of the theoretical foundation for **SAP swelling kinetics and absorbent-core modelling**（源：[[Mathematics of Diffusion]]、[[湿迁移 Wet Migration]]）.
- **Modelling caveat for engineers.** Because a glassy polymer is not D(C)-Fickian, a single diffusion coefficient fitted at high moisture will misrepresent dry-state uptake `[待补]` — record the regime, not one D（源：[[Non-Fickian Diffusion (Crank Ch.11)]]）.
- **Neighbouring vault pages**：[[Non-Fickian Diffusion (Crank Ch.11)]]、[[动边界 Moving Boundary]]、[[Fick 定律]]、[[SAP（高吸水树脂）]]（源：[[Non-Fickian Diffusion (Crank Ch.11)]]）.

## Open Questions 待补

- **No SAP-specific Case II front velocity or transition-concentration value** is recorded in the vault's excerpt `[待补]`.
- **The exact boundaries（concentration / time）between Case II, non-Fickian and Case I for a real SAP** are not quantified（源：[[Non-Fickian Diffusion (Crank Ch.11)]]）.
- **How salt / gel blocking shifts the Case II window** is not addressed in the cited excerpt `[待补]`.

## Related Sources 关联来源

- [[Non-Fickian Diffusion (Crank Ch.11)]]（本页主体来源）
- [[Fick 定律]] · [[Mathematics of Diffusion]] · [[Moving Boundaries (Crank Ch.13)]] · [[动边界 Moving Boundary]] · [[Stefan 问题]]
- [[SAP（高吸水树脂）]] · [[湿迁移 Wet Migration]]

---
type: concept
title: "热传递 Heat Transfer"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [heat-transfer, thermoregulation, heat-moisture-coupling, thermal-bonding, knudsen-effect]
---

# 热传递 Heat Transfer

> 📌 **Page completed 2026-09-30** from 4 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义
Heat transfer — transport of thermal energy — is treated in the vault **not as a standalone subject but as one half of a coupled heat-and-moisture transport problem**. The primary citing source states that moisture transfer and heat transfer are **coupled and cannot be considered independently**（源：[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]] §15.1）. A standalone definition of heat transfer as a physical quantity is not given in the cited sources → 定义待补（引用来源未给出明确定义）.

## Key Parameters and Data 关键参数与数据
| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Coupling relation 耦合关系 | moisture transfer coupled with heat transfer（不可单独求解） | [[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]] §15.1 |
| Wool-fibre experiment temperature 羊毛实验温度 | 65 °C | 同上 §15.2 |
| Moisture uptake at 65 °C 该温度下吸湿量 | <30% | 同上 §15.2 |
| Air thermal conductivity 空气导热系数 k_air | ≈0.026 W/m·K | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| Air mean free path 空气平均自由程 | ≈68 nm | 同上 |
| Nanopore size range 纳米孔尺寸 | ≈20–200 nm（近平均自由程 → Knudsen 抑制） | 同上 |
| Fibril-network index 纤丝网络点接触指标 τ | ≈1.5–3 | 同上 |
| BNC porosity 细菌纤维素孔隙率 | ≈85–95%（traps still air） | 同上 |

## Method / Mechanism 方法 / 机理
- **Coupled heat–moisture transport 湿热耦合**：the observed 'sorption' curve in the wool-fibre experiment is in fact a **'cooling' curve** — the coupling is strong enough to invert the apparent interpretation（源：[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]] §15.2）.
- **Thermoregulation as four separable physical functions**（源：[[PCM-Free Thermoregulation with BNC Nanofiber Network]]）: insulation (resist conductive heat flow, high R-value) · buffering (raise thermal mass, slow dT/dt) · dissipation (evaporative + radiative pathways) · spike absorption (latent heat at a setpoint).
- **Conduction suppression routes**: Knudsen suppression of gas-phase conduction in nanopores sitting near the air mean free path; a point-contact fibril network minimising solid conduction paths plus phonon boundary scattering（源：同上）.
- **Convective heat transfer in process**: air-through bonding passes hot air through the web（热风穿透）, relying on partial melting of the fibre sheath（源：[[热风粘合无纺布]]）.
- **Dry vs wet heat 干热与湿热**: under the heat-setting source, wet heat gives stronger set development in nylon than dry heat（源：[[Manufactured Fibre Technology Ch09 Heat-setting of Thermoplastic Fibres]] pp.198–199）.

## Hygiene Relevance 卫材关联
- Diaper use couples three heat terms — body-heat conduction + urine heat release (dilution heat) + evaporative heat absorption — which must be solved jointly（源：[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]）.
- The **'wet-cool' 湿冷感** sensation (local temperature drop after liquid uptake, colder still after evaporation) is stated to be the physical root of this coupling（源：同上；参见 [[湿冷感 Wet-Cool]]、[[湿热耦合 Heat-Moisture Coupling]]）.
- Thermoregulation routes bear directly on absorbent-core / REL heat management（源：[[PCM-Free Thermoregulation with BNC Nanofiber Network]]）.

## Open Questions 待补
- Standalone definition / governing equations of heat transfer are not given in the cited sources → 定义待补（引用来源未给出明确定义）.
- No measured thermal conductivity or R-value for a hygiene core or nonwoven is recorded in the cited sources `[待补]`.

## Related Sources 关联来源
- [[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]
- [[PCM-Free Thermoregulation with BNC Nanofiber Network]]
- [[热风粘合无纺布]]
- [[Manufactured Fibre Technology Ch09 Heat-setting of Thermoplastic Fibres]]
- [[湿冷感 Wet-Cool]]
- [[湿热耦合 Heat-Moisture Coupling]]

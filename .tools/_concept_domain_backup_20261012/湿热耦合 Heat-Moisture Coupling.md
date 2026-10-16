---
type: concept
title: "湿热耦合 Heat-Moisture Coupling"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [heat-moisture-coupling, diffusion, microclimate, wet-cool, transport-modeling]
---

# 湿热耦合 Heat-Moisture Coupling
> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义
Heat-moisture coupling is the **coupled transport of heat and moisture**, in which the two cannot be treated independently: in a diaper in use, **body-heat conduction + urine heat release + evaporative cooling** act together and must be solved jointly.（湿热耦合是不可以独立处理水分传递与热传递的**耦合传质框架**：纸尿裤使用时**体温热传导 + 尿液放热 + 蒸发吸热**三者耦合，必须联合求解。）
It is described as the **实际使用的核心传质框架** for diapers and wipes.（源：[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]）

## Key Parameters and Data 关键参数与数据
| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Governing framework | simultaneous diffusion of heat and moisture (Crank, Ch.15) | （源：[[Mathematics of Diffusion]]）；（源：[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]） |
| Coupled heat terms | body-heat conduction + urine heat release + evaporative cooling | （源：[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]） |
| Observed effect (wool-fibre experiment) | the measured "sorption" curve is actually a "cooling" curve; coupling magnitude is significant | （源：[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]） |
| Polymer analogue (nylon 6 Tg–moisture) | Tg ≈ 50 °C shifted strongly by regain; 2.0–3.5 % window of minimum Tg sensitivity | （源：[[Manufactured Fibre Technology Ch13 Nylon 6 and Nylon 66 Fibres]]） |

## Method / Mechanism 方法 / 机理
- **Independence is not permitted（不可独立处理）**: moisture transport and heat transport must be solved as a coupled system. The library frames this under Crank Ch.15, "Simultaneous Diffusion of Heat and Moisture".（源：[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]）
- **Coupled heat budget（耦合热平衡）**: three heat terms — body-heat conduction, exothermic urine wetting, and evaporative cooling — act simultaneously.（源：[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]）
- **Evidence of the coupling（耦合证据）**: in the wool-fibre experiment the externally observed "moisture sorption" curve is in fact a "cooling" curve — the coupled effect is large enough to masquerade as the sorption signal itself.（源：[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]）
- **Polymer-level analogue（聚合物层面的同类耦合）**: any hydrophilic polymer whose stiffness and set behaviour move with ambient humidity obeys the same Tg–moisture coupling (nylon 6 is the cited example).（源：[[Manufactured Fibre Technology Ch13 Nylon 6 and Nylon 66 Fibres]]）

## Hygiene Relevance 卫材关联
- **'湿冷感' wet-cold is the physical manifestation（湿冷感即湿热耦合的物理表现）**: after heavy liquid uptake the local temperature drops (feels cool); after evaporation it feels even cooler.（源：[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]）
- **Theoretical foundation for core/perception modelling（芯体与感知建模的理论基础）**: the coupled framework underpins SAP swelling kinetics, absorbent-core modelling and wet-migration simulation.（源：[[Mathematics of Diffusion]]）

## Open Questions 待补
- No quantitative coupling coefficients, temperature deltas or working numeric values are supplied by the cited excerpts — `[待补]`
- No direct diaper-bench measurement of the wet-cool effect magnitude in the cited pages — `[待补]`

## Related Sources 关联来源
- [[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]
- [[Mathematics of Diffusion]]
- [[湿冷感 Wet-Cool]]
- [[热传递 Heat Transfer]]
- [[SAP（高吸水树脂）]]
- [[吸收芯体]]
- [[Moisture-Responsive Fibre（湿敏变形纤维）]]
- [[Manufactured Fibre Technology Ch13 Nylon 6 and Nylon 66 Fibres]]

---
type: concept
title: "Work of Adhesion"
domain: [卫材研发, 表面处理与胶黏剂]
status: growing
updated: 2026-09-30
tags: [surface-energy, adhesion, wetting, absorbency, contact-angle]
---

# Work of Adhesion

> 📌 **Page completed 2026-09-30** from 1 citing source. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**Work of adhesion WA** is the interfacial (thermodynamic) work that must be supplied to separate a liquid from a solid over unit area. The citing source gives it directly in the Dupré form（源：[[Surface Tension and Surface Energy]]）:

- WA = γLV + γSV − γSL = γLV(1 + cos θeq)

中文：附着功 = 分离单位面积液/固界面所需的自由能，由液-气表面张力 γLV 与固-气、固-液界面能之差给出；它随平衡接触角 θeq 减小而单调升高。源页强调它是由能量（标量）定义的**热力学**量，而非力平衡（源：[[Surface Tension and Surface Energy]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Work of adhesion (Dupré) 附着功 | WA = γLV + γSV − γSL = γLV(1 + cos θeq) | [[Surface Tension and Surface Energy]] |
| Work of cohesion 内聚功 | WC = 2γLV | [[Surface Tension and Surface Energy]] |
| Zero-contact-angle condition 零接触角条件 | θeq = 0 ⇒ WA = WC = 2γLV（完全铺展 complete spreading） | [[Surface Tension and Surface Energy]] |
| Water surface tension 水表面张力 | 72.8 dynes/cm @ 20 °C（Harkins & Brown, 1919） | [[Surface Tension and Surface Energy]] |
| Contact-angle span 接触角范围 | 0°（完全铺展）→ 180°（完全不润湿） | [[Surface Tension and Surface Energy]] |
| Diaper core fibre/water θ 芯体纤维-水目标 | < 30° | [[Surface Tension and Surface Energy]] |
| SAP particle wet-state θ | < 10°，θeq = 0 为理想 | [[Surface Tension and Surface Energy]] |
| Rod capillary pull 单纤维毛细拉力 | F = γLV·cos θeq·C（C = 纤维周长, p. 95） | [[Surface Tension and Surface Energy]] |
| Sanitary-pad backsheet apparent θ 卫生巾底膜表观 | > 100° | [[Surface Tension and Surface Energy]] |

## Method / Mechanism 方法 / 机理

- **Energy identity, not force balance.** 源页明确 Young's equation γSV = γSL + γLV cos θeq "is not a force balance"，而是标量能量间的热力学关系——这是 WA 定义的基础（源：[[Surface Tension and Surface Energy]]）。
- **Adhesion rises as contact angle falls.** 因 WA = γLV(1 + cos θeq)，θ 降低则胶接/粘合强度单调升高，故胶黏剂与被粘基材的表面能必须成对匹配，而非各自独立选择（源：[[Surface Tension and Surface Energy]]）。
- **Fibre geometry correction.** 平面液滴不代表吸收场景；纤维级毛细拉力应取 F = γLV·cos θeq·C（源：[[Surface Tension and Surface Energy]]）。
- **Non-equilibrium reality.** 尿液为多组分流体（盐、蛋白、内源性表面活性剂），实际达不到平衡态 WA，Marangoni 效应会复杂化毛细行为（源：[[Surface Tension and Surface Energy]]）。

## Hygiene Relevance 卫材关联

- 芯体纤维/水目标 θ < 30°、SAP 湿态 θ < 10°（θeq = 0 为理想）——这些是最大化 WA、从而最大化芯吸与持液的设计目标（源：[[Surface Tension and Surface Energy]]）。
- 表观 θ > 100° 的结构化底膜利用 Cassie–Baxter 几何——用结构让中等亲水聚合物表现出疏水性，是抗回渗底膜结构的设计原理（源：[[Surface Tension and Surface Energy]]）。
- 因粘合强度随 cos θeq 上升，芯体用胶的选型本质是胶与基材的表面能匹配（源：[[Surface Tension and Surface Energy]]）。

## Open Questions 待补

- 未读到任何具名 KC 浆 / SAP / 面层材料的 WA 数值 [待补]。
- WA 与实测回渗 / 干爽之间的定量关系在库内未建立 [待补]。

## Related Sources 关联来源

- [[Surface Tension and Surface Energy]]
- Adjacent concepts 相邻概念：[[接触角 Contact Angle]]、[[Young's Equation]]、[[Wenzel Equation]]、[[Cassie-Baxter Equation]]、[[Laplace Pressure]]、[[三相接触线 TPL]]、[[Marangoni Effect]]、[[亲水化 Hydrophilisation]]
- Application pages 应用页：[[卫材胶黏系统 Hygiene Adhesive Systems]]、[[压敏胶 PSA]]、[[Chemical bonding]]

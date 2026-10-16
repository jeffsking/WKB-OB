---
type: concept
title: "毛细芯吸 Capillary Wicking"
domain: [卫材研发, SAP与流体]
status: growing
updated: 2026-09-30
tags: [毛细芯吸, 毛细压力, 多孔介质, 芯体, 面层, wicking, capillary]
---

# 毛细芯吸 Capillary Wicking

> 📌 **Page completed 2026-09-30** from 7 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**定义待补（引用来源未给出明确定义）。**

本库未对「毛细芯吸」下形式化定义；只以其**驱动力 + 动力学**形态出现：吸收由**毛细压力**驱动，外加重力 / 外压仅起次要作用（源：[[Porous Structure and Liquid Flow Models]]，p. 19；[[Porous Structure and Liquid Flow Models]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 毛细压力 p_c | p_c = 2γcosθ/r | [[Porous Structure and Liquid Flow Models]] |
| Young–Laplace 形式 | ΔP = −2γcosθ / R | [[毛细压力 Capillary Pressure]] |
| 达西定律 | q = −K·∇P，K = k / μ | [[Porous Structure and Liquid Flow Models]] |
| Kozeny–Carman | k ∝ Φ³/(1−Φ)² | [[Porous Structure and Liquid Flow Models]] |
| 芯吸前沿动力学 | x_v ∝ t^(1/2)（Washburn / Rudd） | [[Porous Structure and Liquid Flow Models]]（p. 24, p. 37）、[[Washburn Equation]] |
| 速率-容量拮抗 | 流速 ∝ r²（Hagen–Poiseuille）；p_c ∝ 1/r；Y×2 → 流速 ×16 | [[Porous Structure and Liquid Flow Models]] |
| 三叶形沟槽表面积 | ≈ 圆纤维的 300 %（等旦数） | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 异形 PET 面层 MD 铺展提升 | 约 10–25 % | [[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]] |

## Method / Mechanism 方法 / 机理

- **驱动力 = 毛细压力**："The driving force for absorption of the bulk of the liquid into an absorbing material ... is the capillary pressure"（源：[[Porous Structure and Liquid Flow Models]]，p. 19）。
- **非稳态流动 ≈ 扩散**：控制方程 ∂s/∂t = ∇·[F(s)∇s]，扩散因子 F(s) = (k/μΦ)(dp/ds)（源：[[Porous Structure and Liquid Flow Models]]，p. 36）；由此推进的芯吸前沿随时间以 t^(1/2) 增长（源：[[Porous Structure and Liquid Flow Models]]、[[Washburn Equation]]）。
- **结构给出速率与容量的分工**：孔径控制速率（Hagen–Poiseuille ∝ r²），孔体积控制容量；渗透率随孔隙率经 Kozeny–Carman 杠杆放大（源：[[Porous Structure and Liquid Flow Models]]）。
- **沟槽导引**：三叶形沿纤维轴向的沟槽是一条**不沿轴断裂的毛细管**——大孔排空后沟槽仍持续抽吸；等旦数下沟槽纤维表面积约为圆纤维的 300 %（源：[[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]]）。
- **非织造布的多孔介质处理**：达西定律被列为非织造织物表征与建模的关联概念（源：[[Characterisation, testing and modelling of nonwoven fabrics]]）。

## Hygiene Relevance 卫材关联

- **芯体设计核心矛盾**：速率与容量互为拮抗且都由几何决定，最优落于中值——直接把「吸得快」翻译为毛细压力 / 渗透率 / 孔隙体积三个可测量（源：[[Porous Structure and Liquid Flow Models]]）。
- **面层 / 导流层沟槽芯吸**：全圆截面网面在 MD 铺展差，因液体每跨一孔都要**重建弯月面**，每次跳动损失压力；轴向沟槽提供连续 MD 通道（源：[[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]]）。
- **沟槽收益以低接触角为前提**：形状只是修正项，取向与亲水整理仍控制 MD/CD 平衡（源：[[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]]）。
- 关联页：[[Groove Capillary Suction]]、[[三叶形截面纤维（Trilobal Fibre）]]、[[MD Liquid Distribution]]、[[ADL（导流层）]]、[[Shaped PET Add-On Window]]。

## Open Questions 待补

- Depend / Always Discreet 毛细压力与解吸能量的**具体数值未以文本落地**，对外引用须脱敏（源：[[毛细压力 Capillary Pressure]]、[[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]）。
- 饱和度按试样重量归一化的跨克重比较基准（面积 / 体积）未决（源：[[毛细压力 Capillary Pressure]]）。
- 沟槽芯吸在真实重复冲击下的定量 MD 增益（10–25 % 为预期值而非实测）`[待补]`。

## Related Sources 关联来源

- [[Characterisation, testing and modelling of nonwoven fabrics]] — cited-by 来源
- [[Porous Structure and Liquid Flow Models]]
- [[Porous Structure and Liquid Flow Models]]
- [[毛细压力 Capillary Pressure]]
- [[Washburn Equation]]
- [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]]
- [[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]]

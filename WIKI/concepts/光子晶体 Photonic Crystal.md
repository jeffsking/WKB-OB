---
type: concept
title: "光子晶体 Photonic Crystal"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [photonic-crystal, structural-color, bragg-diffraction, mechanochromic, chromic-materials, hygiene-materials]
---

# 光子晶体 Photonic Crystal
> 📌 **Page completed 2026-09-30** from 3 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

- Photonic crystals are **periodically ordered nanostructures whose interaction with incident light produces structural colour** — the source wording is: "Structural colors, arising from light interaction with periodically ordered nanostructures that are widely known as photonic crystals (PEs), are widespread in nature"（源：[[Interactively Mechanochromic Electronic Textile Sensor]]）。
  （中文：光子晶体 = 与光相互作用的**周期性有序纳米结构**，由此产生的颜色即**结构色**；该定义直接来自引文原文。）
- In the chromic-materials taxonomy, photonic crystals sit at the **supramolecular / structural level** — the third of three engineering levels (molecular → particulate → supramolecular), where "λ 由结构决定" rather than by dye molecules. Chromatic change is "engineered at three levels: molecular (photo/thermo/pressure-responsive dyes), particulate (pearl/lustre pigments by thin-film interference), and supramolecular (liquid crystals, photonic crystals)"（源：[[Chromic Phenomena]]）。
- In the force/strain (mechanochromic) context the material is classified as the **M2 photonic-crystal structural-colour route**（源：[[Mechanochromic Materials Technical Review（EN v3, 2026-08）]]），and the polymer-opal / colloidal-PC family is filed under **结构色（布拉格）** among the mechanochromic routes（源：[[Chromism Taxonomy（变色现象分类）]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Photonic-crystal / polymer-opal core–shell particles | PS/PEA 颗粒 ~200–300 nm，剪切组装成弹性蛋白石 | [[Structural Colour Mechanochromism（结构色力致变色）]] |
| Reflection peak after elastomer infiltration (PE) | 527 nm → 604 nm（折射率增大 + 晶格间距增大） | [[Interactively Mechanochromic Electronic Textile Sensor]] |
| Stretch-induced blue shift | 0 % → 51.6 % 应变 λmax 单调下降；< 15.9 % 为快速变化段 | [[Interactively Mechanochromic Electronic Textile Sensor]] |
| Finger-bending demo (λmax) | 604 nm → 571 nm（橙红 → 绿） | [[Interactively Mechanochromic Electronic Textile Sensor]] |
| Sensor toughness (MET) | 35.6 kJ/m³（对比 PTIP 17.6 / PE 20.7 / CPT 24.9 kJ/m³） | [[Interactively Mechanochromic Electronic Textile Sensor]] |
| Optical response / recovery | ≈ 0.30 s / < 0.22 s（与电信号同步，5 % 应变下） | [[Interactively Mechanochromic Electronic Textile Sensor]] |
| Cycling durability | 30,000 次拉伸–释放循环（30 % 应变，2 Hz）无迟滞、无退化 | [[Interactively Mechanochromic Electronic Textile Sensor]] |
| Opal ordering condition (route cost) | 加热辊间**约 300 % 应变幅**的振荡剪切（专用产线，非狭缝模头） | [[Structural Colour Mechanochromism（结构色力致变色）]] |
| Roll-to-roll opal throughput | > 100 m 蛋白石膜（弯曲诱导振荡剪切） | [[Structural Colour Mechanochromism（结构色力致变色）]] |
| Colloidal-PC route cost index (relative) | 25×；可逆 > 100 cycles | [[Chromism Taxonomy（变色现象分类）]] |

## Method / Mechanism 方法 / 机理

- **Bragg diffraction from a tunable lattice.** The colour is set by the lattice spacing: "when the MET sensor is stretched in the horizontal direction, the lattice spacing d is reduced from d0 to d in the vertical direction, thus resulting in a decrease in λmax"（源：[[Interactively Mechanochromic Electronic Textile Sensor]]）。拉伸压缩竖直方向晶格间距 → λmax **蓝移**；渗入弹性体使折射率与间距同时增大 → 反射峰**红移**（源：[[Interactively Mechanochromic Electronic Textile Sensor]]）。
- **Periodic structures are assembled, not slit-cast.** Polymer-opal photonic crystals are made by shear-assembling core–shell PS/PEA particles, and the ordering step needs **oscillating shear at ~300 % strain amplitude between heated rollers — a dedicated line, not a slot die**（源：[[Structural Colour Mechanochromism（结构色力致变色）]]）。
- **Two structural-colour failure modes (shared with the whole structural-colour family):** (1) **moisture and UV** degradation of the colour unit, and (2) **angle dependence (iridescence)** — a Bragg colour shifts with viewing angle, so a tilted viewer sees a colour change that is *not* caused by strain（源：[[Structural Colour Mechanochromism（结构色力致变色）]]、[[结构色 Structural Color]]）。
- **Manufacturing maturity is the open gap.** For photonic band-gap materials the source states plainly: "Whilst true 3D photonic band gap materials operating in the microwave and millimetre range have been produced, those operating in the visible region of the spectrum are still awaited. When this eventually happens the optical computer will no longer be a pipe dream."（源：[[Chromic Phenomena Solar Energy and Liquid Crystals]]）

## Hygiene Relevance 卫材关联

- **Fit / tension indication（合身可视化）**：光子晶体结构色属**可逆**力致变色路线（M2），是连续合身监测的候选之一；可逆性在一次性卫品场景被列为不可让步的要求（"reversibility is a non-negotiable requirement"，源：[[Mechanochromic Materials Technical Review（EN v3, 2026-08）]]、[[Structural Colour Mechanochromism（结构色力致变色）]]）。
- **Strain → colour coupling can be coupled to SAP swelling (推演, unverified)**：变色机制是"应变 → 晶格间距调控 → λmax 蓝移"，响应区间 0–51.6 %；若与 SAP 层复合，吸水膨胀本身即应变源，可发展为"尿量可视化指示贴"——**须验证膨胀方向与变色区间匹配**（源：[[Interactively Mechanochromic Electronic Textile Sensor]]）。
- **Two blocking constraints for disposable hygiene.** 结构色路线的否决来自**工艺原生性**（蛋白石需加热辊间振荡剪切）与**角度依赖（虹彩）**；结论是**「等工艺，不等性能」**，列入 **2028 复审**（源：[[Mechanochromic Routes Comparison（力致变色技术路线对比）]]、[[结构色 Structural Color]]）。
- **Interface / lamination durability**：photonic-elastomer 半嵌入导电织物形成一体化结构，30,000 次循环不退化，对尿裤腰贴、弹性耳贴等反复拉伸部位的功能层附着工艺有借鉴价值（源：[[Interactively Mechanochromic Electronic Textile Sensor]]）。
- **Urine-environment stability**：尿液环境下结构色单元 / 器件的稳定性是所有变色路线共同的**未验证项** `[待补]`（源：[[结构色 Structural Color]]）。

## Open Questions 待补

- 温/湿/UV 与尿汽长期作用下的**结构色漂移定量数据**库内未见 `[待补]`。
- **非虹彩（angle-independent）光子晶体变体**的色差与工艺窗口尚无数据；仅提"非晶光子"变体值得在 2028 平台门径复审（源：[[Structural Colour Mechanochromism（结构色力致变色）]]）。
- 上述定量数据在来源中的**页码/行号待核** `[待补]`（本页所记行号取自来源页转写）。
- 「光子晶体」在 [[Chromic Phenomena]] 书中的**独立定义段落**尚未逐字摘录 —— 库里只见其作为 Ch.5 主题之一出现 `[待补]`。

## Related Sources 关联来源

- [[Interactively Mechanochromic Electronic Textile Sensor]]（结构色定义、Bragg 晶格调控与全部 MET 定量数据）
- [[Chromic Phenomena]]（三工程层级：supramolecular = 液晶 / 光子晶体；λ 由结构决定）
- [[Chromic Phenomena Solar Energy and Liquid Crystals]]（Ch.5 光子晶体；可见光区 3D 光子带隙材料尚待实现）
- [[结构色 Structural Color]]、[[Structural Colour Mechanochromism（结构色力致变色）]]（结构色总纲、共同失效模式、蛋白石工艺）
- [[Chromism Taxonomy（变色现象分类）]]、[[Mechanochromic Materials Technical Review（EN v3, 2026-08）]]、[[Mechanochromic Routes Comparison（力致变色技术路线对比）]]（M1–M4 分类与路线裁决）
- 相邻条目：[[机械变色 Mechanochromic]]、[[Mechanochromic变色纤维]]、[[液晶 Liquid Crystal]]、[[胆甾相液晶 Cholesteric Liquid Crystal]]、[[珠光颜料 Lustre Pigment]]、[[全息存储 Holographic Storage]]、[[变色油墨]]
- 同族对照：[[Mechanochromic Photonic Sensors]]、[[Holographic Structurally Colored Mechanochromic Films]]

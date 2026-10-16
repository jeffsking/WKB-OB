---
type: concept
title: "浊点 Cloud Point"
domain: [卫材研发, 待归类]
status: growing
updated: 2026-09-30
tags: [cloud-point, 浊点, nonionic-surfactant, LCST, phase-transition, light-scattering, rewetting-agent]
---

# 浊点 Cloud Point

> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.
> 中文：本库「浊点」存在**两个口径**——表面活性剂口径（非离子表活失溶温度）与聚合物溶液口径（相分离混浊温度），不可混引。

## Definition 定义

**口径一 · 表面活性剂（surfactant）**：非离子型表面活性剂随温度失去溶解性，在 **"well below 100 °C"** 的温度下沉淀为**巨型胶束（giant micelles）**，此温度即称 **cloud point**（源：[[The Role of Surfactants]]，p.171）。

**口径二 · 聚合物溶液（polymer solution）**：cloud point（浊点）是出现**乳白色乳光（visual milky opalescence）**的温度；严格定义为 **T_cp = argmax_T (dI/dT)**，用以消除「起始点（point 1）」与「平台点（point 2）」之间的歧义（源：[[Smart Polymers Ch01 Phase Transitions and Light Scattering]]，L1944–1957）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Cloud point 定义（非离子表活） | 温度升高失溶，"well below 100 °C" 沉淀为巨型胶束；此温度即 cloud point | [[The Role of Surfactants]]（p.171） |
| Cloud point 严格定义（聚合物溶液） | visual milky opalescence；**T_cp = argmax_T (dI/dT)** | [[Smart Polymers Ch01 Phase Transitions and Light Scattering]]（L1944–1957） |
| Cloud-point 方法精度排序 | **visual < UV-VIS < SLS/DLS** | [[Smart Polymers Ch01 Phase Transitions and Light Scattering]]（L1944–2042） |
| LCST 定义 | 下临界溶解温度：低于 T_c 互溶、高于 T_c 分相 | [[Smart Polymers Ch01 Phase Transitions and Light Scattering]]（L233–234） |
| PNIPA LCST（纯水） | ≈ **34.9 ± 0.1 °C** | [[Smart Polymers Ch01 Phase Transitions and Light Scattering]]（L1976） |
| 共存曲线族 coexistence curves | UCST / LCST / closed-loop / overlapping gaps / 最多三个临界点 | [[Smart Polymers Ch01 Phase Transitions and Light Scattering]]（L200–230） |

## Method / Mechanism 方法 / 机理

- **测量优先于预测.** 共存曲线高度多样，"no existing microscopic or phenomenological theory can analytically represent the coexistence curve over a wide parameter range"——经验相图是任何生物工艺设计的先决条件（源：[[Smart Polymers Ch01 Phase Transitions and Light Scattering]]，L200–230）。
- **Cloud-point 测定方法比较.** 源列有 cloud-point determination methods（比较 visual / UV-VIS / SLS / DLS 的精度），精度排序为 visual < UV-VIS < SLS/DLS（源：[[Smart Polymers Ch01 Phase Transitions and Light Scattering]]，L1944–2042）。
- **平顶 LCST 曲线.** 对 PNIPA、PVCL，共存曲线顶部平坦：相分离温度在宽浓度范围内不变、与 LCST 相等，且 spinodal 与 binodal 无法实验区分——使触发对局部浓度变化不敏感（源：[[Smart Polymers Ch01 Phase Transitions and Light Scattering]]，L2052–2063）。
- **CMC 的盐/温度敏感.** CMC 对单价反离子浓度敏感（每单位摩尔浓度约 ÷3）；非离子型随温度失溶——这与其 cloud point 行为相关（源：[[The Role of Surfactants]]）。

## Hygiene Relevance 卫材关联

- **再润湿剂施用窗口.** 好的再润湿剂应在**近浊点（near cloud point）**施用，且**干燥时不得结晶**——"surfactants which are liquids or amorphous solids when dry make better rewetting agents than those which are crystalline"；这是直接影响涂布烘干设定的工艺窗口要求（源：[[The Role of Surfactants]]，p.171 附近）。
- **体温/尿液附近的热响应层.** 平顶 LCST 意味着触发与浓度无关；设计设定点应在 **T_LCST ≈ 32–35 °C**，即在与约 37 °C 皮肤/尿液接触时发生去溶胀响应（源：[[Smart Polymers Ch01 Phase Transitions and Light Scattering]]，L2052–2063）。
- 参见 [[再润湿剂 Rewetting Agent]]、[[润湿剂 Wetting Agent]]、[[表面活性剂 Surfactant]]。

## Open Questions 待补

- 非离子表活的**具体浊点数值（℃）**在引用来源中仅表述为 "well below 100 °C"，**无数值**。
- cloud-point 测定方法（L1944–2042）的**逐条参数（如 UV-VIS 波长、扫描速率）**在本库摘录中未展开。
- 浊点与卫材配方（芯体/ADL 表面活性剂）的**定量关联**：来源未给。

## Related Sources 关联来源

- [[The Role of Surfactants]]
- [[Smart Polymers Ch01 Phase Transitions and Light Scattering]]
- 相关概念：[[表面活性剂 Surfactant]]、[[胶束 Micelle]]、[[CMC 临界胶束浓度]]、[[润湿剂 Wetting Agent]]、[[再润湿剂 Rewetting Agent]]、[[两亲吸附 Amphipathic Adsorption]]

---
type: concept
title: "83 Changeover Four-Layer Architecture（换型要素四层分层与变更控制）"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [changeover, converting, forming-drum, ups, repitch, sleeve, change-control, pattern-core]
---

# 83 Changeover Four-Layer Architecture（换型要素四层分层与变更控制）

> 📌 **Page completed 2026-09-30** from 4 citing sources in the vault（10 处引用）. All figures traced to their source pages. Anything not evidenced in the vault is marked `[待补]`.

## Definition 定义

The vault's cited statements describe this architecture as a **four-layer stratification of changeover elements with change control（换型要素四层分层与变更控制）**. Its stated root principle is an **orthogonal split between 「定相位」(phase-fixed) and 「定尺寸」(dimension-fixed)** variables — "「定相位 vs 定尺寸」的正交切分是全部换型设计的根", attributed to this page's own source page（源：[[83 Changeover Four-Layer Architecture and Change Control（换型要素四层分层与变更控制）]]）. The four individual layers are **定义待补（引用来源未给出明确定义）** — the citing excerpts state the principle and the cost logic, but not the layer-by-layer enumeration.

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Design root principle 设计根原则 | 「定相位 vs 定尺寸」正交切分 = the root of all changeover design（全部换型设计的根） | [[83 Changeover Four-Layer Architecture and Change Control（换型要素四层分层与变更控制）]] |
| CD changeover route 横向换型路径 | CD 走 chute 插片（chute insert）— described as the architecture's most important cost design | [[83 Changeover Four-Layer Architecture and Change Control（换型要素四层分层与变更控制）]] |
| Width-family extension marginal cost 宽度族扩展边际成本 | Reduced to "只剩一片插片"（one insert only） | [[83 Changeover Four-Layer Architecture and Change Control（换型要素四层分层与变更控制）]] |
| `ups` scope 作用域 | 整线级参数（line-level parameter）：双鼓必须同 ups（both drums must share the same ups），不是单鼓参数 | [[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]] |
| Change effort for `ups` 换 ups 需改项 | 真正需要改的只有 Recipe 一列（+ 换 sleeve） | [[Repitch（鼓距与产品节距解耦）]] |

## Method / Mechanism 方法 / 机理

**Architecture-defect detector（架构缺陷检测器）：** the digest records a **Q4 "不能"（cannot）branch** that acts as a defect detector — "任何『随尺寸变、又必须换实体件、且换起来很贵』的量，都是设计没做干净"（any quantity that *varies with size*, *requires swapping a physical part*, and is *expensive to change* is a design that was not done cleanly）（源：[[83 Changeover Four-Layer Architecture and Change Control（换型要素四层分层与变更控制）]]）.

**Consequence for `ups`:** because `ups` is a line-level parameter shared by both forming drums, changing it is asserted to touch only the Recipe column plus a sleeve change（源：[[Repitch（鼓距与产品节距解耦）]]）; this is the mechanism that keeps gear-pitch changeover cheap under this architecture.

## Hygiene Relevance 卫材关联

The architecture governs **changeover design for the patterned SAP core forming line** — it is the change-control framework behind drum-pitch selection（[[81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）]]）, drum-to-chassis pitch decoupling（[[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]]）and sleeve changeover（[[84 Sleeve 工程规格与换装防错设计]]）. Its stated value to the REL absorbent core is **lower marginal cost when extending the width family**, and a design rule that keeps size-dependent quantities out of expensive part swaps.

## Open Questions 待补

- The four individual layers are not enumerated in the citing excerpts — layer-by-layer definition `[待补]`.
- No numeric ratios, timing, or acceptance thresholds are given for the Q4 "不能" branch `[待补]`.
- The relationship to the sibling concept page [[Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]] is unstated and needs de-duplication review `[待补]`.

## Related Sources 关联来源

- [[83 Changeover Four-Layer Architecture and Change Control（换型要素四层分层与变更控制）]]
- [[81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）]]
- [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]]
- [[82 鼓距与产品节距解耦 repitch 选型]]
- [[84 Sleeve 工程规格与换装防错设计]]
- [[80 高速pattern芯体成型工程总纲（导航·速查·口径·分歧·验收）]]
- [[03_卫材产线约束常量表（准入校验工具）]]
- [[Repitch（鼓距与产品节距解耦）]]
- [[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]
- [[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]

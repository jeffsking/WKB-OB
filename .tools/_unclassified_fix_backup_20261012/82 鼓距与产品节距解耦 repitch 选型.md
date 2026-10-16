---
type: concept
title: "82 鼓距与产品节距解耦 repitch 选型"
domain: [卫材研发, 待归类]
status: growing
updated: 2026-09-30
tags: [repitch, 鼓距, chassis-pitch, 成型鼓, 换型, converting, pattern-SAP]
---

# 82 鼓距与产品节距解耦 repitch 选型

> 🔴 **manual_review（2026-09-30）**：本页与 [[Repitch（鼓距与产品节距解耦）]] 主题重复，**双方均有实质内容**，未自动合并。请人工裁决保留哪一版或人工并入。

> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**Repitch（鼓距与产品节距解耦）** 指在成型鼓与后道之间，把成型鼓上的节距过渡到后道所需产品节距的单元 —— 中文口径「成型鼓上的节距与后道要的节距不一样，中间靠什么单元过渡」（源：[[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]]）。

- **鼓距 Drum pitch P = πD/n**：成型线由鼓径 D 与 ups n 决定的离散量。
- **产品节距 Chassis pitch C**：后道（复合 / 折叠 / 切断 / 包装）要求的产品中心距，由 11 个产品规格各自决定。
- **两者没有理由相等**：若强制 P = C，则 πD/n = C 会对 11 个规格给出 11 个不同的 D，与「单一鼓体」前提直接矛盾 → **repitch 单元是「一鼓多规格」的必要条件**。
  （源：[[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]]）

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Drum pitch P 鼓距 | P = πD/n (drum diameter ÷ ups) | [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]] |
| cut-and-slip ratio window 切滑可行窗口 | ≈1.03 ≤ ratio ≤ 1.30（仅加速 accelerate only） | [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]] |
| Servo repitch turret ratio 伺服转塔节距比 | 0.85–1.40（双向 bidirectional） | [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]] |
| Pick-up line speed 取片线速 | 396 或 462 m/min（= 鼓面线速） | [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]] |
| Place pitch 放片节距 | = chassis pitch（按规格 per spec） | [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]] |
| Cam count 凸轮数 | 每规格一份凸轮（recipe + 换件） | [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]] |
| Unit position 单元位置 | 双鼓压合点之下（切断 → 修边 → repitch 依次在压合后） | [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]] |
| repitch ratio semantics 比值含义 | ratio < 1 ⇒ 芯体需**减速**；ratio > 1 ⇒ 需**加速** | [[Repitch（鼓距与产品节距解耦）]] |

## Method / Mechanism 方法 / 机理

两条路线对比（源：[[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]]）：

| Route 路线 | Direction 方向 | Ratio window | Cams 凸轮 |
|---|---|---|---|
| cut-and-slip（加速带 / 夹辊送单片芯体） | 仅加速 | ≈1.03–1.30 | 通用凸轮 generic |
| 伺服 repitch 转塔（独立 puck 沿各自凸轮取片再放置） | 双向 | 0.85–1.40 | 每规格一份 |

- **源文件判据（P6 标题）**：*"A servo repitch turret, not cut-and-slip — because NB needs the core slowed down"*（NB 需要芯体**降速**，cut-and-slip 只能加速，故必须用伺服转塔）。
- **转塔只认「取片线速 + 目标节距」，不感知 ups**（ups 影响的是取片线速）（源：同上）。
- 本单元补的是 **Gap G16（鼓距—产品节距解耦单元完全缺失，零覆盖，严重程度高，P0 批次）**，副交付 **G15（chip trim 与「芯长 > 产品节距」处置规则）**（源：同上）。

## Hygiene Relevance 卫材关联

- repitch 是「**一鼓多规格**」成型架构的必要条件，直接支撑 11 码单鼓方案的落地（源：[[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]]）。
- 与换型架构耦合：repitch 转塔凸轮属于 Recipe 层（cams），**换 ups 时真正需要改的只有 Recipe 一列（+ 换 sleeve）**；repitch 转塔与 ups 归属同层（源：[[Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]]、[[Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]]）。
- 相邻工程页：[[81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）]]、[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]、[[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]、[[Pad Zoning：Flat vs Pocketed（成型分区：平区 vs 袋区）]]。
- 结构性缺口：本地唯一的成型设备培训文档（2021 KC 培训）**完全没有** repitch 解耦等 pattern-SAP 量产方法（源：[[80 高速pattern芯体成型工程总纲（导航·速查·口径·分歧·验收）]]）。

## Open Questions 待补

- [[Repitch（鼓距与产品节距解耦）]] 中 repitch ratio 的定义句原文残缺 `[原文残缺]`，仅比值增减方向可用 `[待补]`。
- 87 页登记 G16（repitch）与 chassis pitch 落库的合并脚本，需核对最新口径与数值 `[待补]`。
- 本页与源页 [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]] 同主题，合并 / 去重方案待定 `[待补]`。

## Related Sources 关联来源

- [[81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）]]
- [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]]
- [[Repitch（鼓距与产品节距解耦）]]
- [[Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]]
- [[80 高速pattern芯体成型工程总纲（导航·速查·口径·分歧·验收）]]
- [[87 Hygiene Line Constraint Constants（待并入补充行·合并脚本）]]

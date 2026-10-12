---
type: concept
title: "Repitch（鼓距与产品节距解耦）"
domain: [卫材研发, 设备工程, 芯体工艺]
status: seed
updated: 2026-09-29
tags: [repitch, 再分距, 节距, 转塔, cut-and-slip, chip trim, 成型鼓]
---

# Repitch（鼓距与产品节距解耦）

> One-line definition 一句话定义：**鼓距（drum pitch，P = πD/n）与产品节距（chassis pitch，后道要求的中心距）是两个独立的量**，中间必须有一个"节距重排（repitch）"单元把两者解耦，否则"一鼓多规格"不成立。（中文：鼓上排布的间距 ≠ 后道要的间距，必须有个单元在中间"重新排间距"。）

## Definition 定义：为什么必须解耦

| 量 | 定义 | 由谁决定 |
|---|---|---|
| **鼓距 drum pitch P** | 鼓面圆周上相邻两 pattern 中心距 = **πD/n** | 成型线：鼓径 D + ups n（**离散量**） |
| **产品节距 chassis pitch C** | 后道（复合 / 折叠 / 切断 / 包装）要求的产品中心距 | 产品规格：芯长 + 股间间隙 |

> **关键**：P 只能取 πD/n 这组离散值；C 由 11 个规格各自决定。**两者没有理由相等**。若强制 P = C，则 πD/n = C 对 11 个规格给出 11 个不同 D，与「单一鼓体」前提直接矛盾 → **repitch 是必要条件，不是可选优化项**。

## Mechanism 机理：两条解耦路线与判据

| | **cut-and-slip（切断滑移）** | **伺服 repitch 转塔（servo repitch turret）** |
|---|---|---|
| 原理 | 切断后由加速带 / 夹辊把单片芯体**加速**送到下道 | 转塔上独立 **puck（托块）**沿各自凸轮轨迹取片、再放到目标节距 |
| 节距比范围 | **≥ ~1.03**（上限 ~1.30） | **0.85 – 1.40** |
| 方向性 | **只能加速，不能减速** | **双向**（可加速、可减速） |
| 换件 / 凸轮 | 通用 | **每规格一份凸轮**（recipe 项） |
| Open NB（ratio 0.99） | ✗ **失效** | ✓ |
| 源文件结论 | 不采用 | **采用** |

> **判据原句**（源文件 P6 标题）：*"A servo repitch turret, not cut-and-slip — because NB needs the core slowed down."*
> **稳健性条件**（P6 脚注）：*"the recommendation holds as long as any size needs a ratio below ~1.03 or above ~1.3."* → **只要任一规格落在 [1.03, 1.30] 窗口之外，就必须用伺服转塔**。

**repitch ratio 定义**：`ratio_s = chassis pitch_s / drum pitch_group(s)`；ratio < 1 ⇒ 芯体需**减速**；ratio > 1 ⇒ 需加速。

## Key Parameter Table 关键参数表

| Parameter 参数 | Value 数值 | 出处 |
|---|---|---|
| 转塔节距比范围 | **0.85 – 1.40** | [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]] |
| cut-and-slip 可行窗口 | **~1.03 – ~1.30**（⚠️ 两边界无出处，B 级） | 同上 |
| 取片线速 | **396 / 462 m/min**（= 鼓面线速） | 同上 |
| 换规格方式 | 每规格一份凸轮（recipe + 换件） | 同上 |
| 位置 | 双鼓压合点**之下**（切断 → 修边 → repitch 依次在压合后） | 同上 |
| 11 规格 ratio 跨度 | **0.985 – 1.251** | 同上 |
| 唯一越界者 | **Open NB = 0.985**（<1.03） | 同上 |
| chassis pitch 假设式 | C = 芯长 + k；**k_open = 110 mm / k_pants = 130 mm**（⚠️ 假设值） | 同上 |
| 反向校核靶 | NB 需 C ≥ **407.7 mm** ⇒ **k_open ≥ 127.7 mm** 才可能回到 cut-and-slip | 同上 |
| chip trim 判据 | 端区 **E > 80 mm → 切回 60 mm** | 同上 |
| chip trim 实际切除 | Open NB **56 mm**（芯长变 340 mm）；Open S **22 mm**（变 374 mm）；其余 9 规格不触发 | 同上 |

> ⚠️ **No unsourced parameters 禁止无来源参数**：上表全部来自上列源摘要页；**chassis pitch 全为 B 级假设值**，引用 ratio 表**必须携带该标注**；**1.03 / 1.30 与 80 / 60 mm 阈值均无推导出处** → `[待验证]`。

## Adjacent Concepts 相邻概念

- 上游：[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]（鼓距来源）、[[81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）]]
- 同层：[[83 Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]]（ups / cams / chute 的层级归属）
- 下游：[[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]（落料速度随线速）
- 易混：[[GB-T 28004.1-2021（纸尿裤国标）]]——**尺寸标准给成品外形（长×宽），不是工艺节距**；用尺寸标准推 chassis pitch 会引入系统性误差。
- 易混：**17 片**是换型后**相位闭环收敛**的片数，不是换型总废片（见 [[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]）

## 经验教训

- **Lesson 1（离散量 vs 连续量）**：P 是**离散**的（n 为整数），C 是**连续**的（产品规格）。二者的鸿沟只能靠"转换单元"弥合 —— 凡遇到"离散机构 + 连续规格"的组合，先问解耦单元在哪，而不是试图让机构去适配规格。
- **Lesson 2（一个越界即否决）**：11 个规格中**只有 1 个（Open NB）越界**，但已足以否决 cut-and-slip。**做架构选型时不能按"多数规格满足"来裁决** —— 必须按"是否全部落在窗口内"裁决。
- **Lesson 3（ups 分配的双目标）**：**ups 加多 → 鼓距减小 → 端区减小（省包覆）但 ratio 也减小**；ratio 下界构成 ups 选择的**隐藏约束**。故 81 的 ups 分配**不能只看端区**，必须同时校核 ratio。
- **Lesson 4（chip trim 的双重理由）**：不只是省材料——**NB 的硬冲突是「芯长 > 产品节距」（395.8 > 390 mm），不修剪则在物理上放不进自己的节距**。修剪到 340 mm 才闭合。
- **待补 `[待验证]`**：chassis pitch 实测值（最高优先）；1.03/1.30 边界出处；80/60 mm 阈值推导；NB 剪短到 340 mm 后后道（折叠/包装）的位置约束。

> 🔴 **manual_review（2026-09-29）**：本源含**可直接写入 RFQ 的转塔规格条目**与**待索取清单**（JOA、恒昌、HCH 的 repitch 单元配置）。依 AGENTS.md §5，**只记技术规格与缺口，不落商务条款与定点结论**；全部为 **B 级一阶模型值**。

## 来源

- [[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/82-鼓距与产品节距解耦repitch选型.md.md`

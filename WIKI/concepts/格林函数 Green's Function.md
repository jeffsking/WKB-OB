---
type: concept
title: "格林函数 Green's Function"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [格林函数, 点源解, 扩散建模, SAP建模, Crank]
---

# 格林函数 Green's Function

> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**定义待补（引用来源未给出形式化定义）**。两处引用来源均以**平面源格林函数**的形式给出唯一可溯源口径：

- 平面源格林函数 `C = (M/2(πDt)^½)·exp(−x²/4Dt)` —— 基本"砖块"（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。
- 该来源的定位表述：平面源格林函数是 **SAP 建模的原子单元** —— 单个 SAP 微球可视为瞬时点源，多粒子场可叠加（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 平面源格林函数 Plane-source Green's function | C = (M/2(πDt)^½)·exp(−x²/4Dt) | [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] |
| n 维源函数推广 | C = A·t^(−n/2)·exp(−r²/4Dt) | [[Infinite and Semi-Infinite Media (Crank Ch.3)]] |
| 球源轴心解 | C = C₀{1 − exp(−a²/4Dt)} | [[Infinite and Semi-Infinite Media (Crank Ch.3)]] |
| 圆盘源剩余量 | Q(t) = 2πa²C₀ ∫₀^∞ [J₁(ωa)]²·exp(−Dτω²)dω | [[Infinite and Semi-Infinite Media (Crank Ch.3)]] |
| 不透水边界（反射条件） | dC/dx = 0 | [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] |
| 透湿边界（反射条件） | dC/dx + hc = 0 | [[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]] |
| Half-space validity 半无限域适用条件 | 介质无限 / 半无限 | [[Infinite and Semi-Infinite Media (Crank Ch.3)]] |

## Method / Mechanism 方法 / 机理

- **三类解析方法**：① 反射与叠加法 —— 利用线性方程叠加性构造边界解；② 分离变量法 —— `C = u(x)exp(−Dα²t)`，得到 Bessel/三角本征值问题；③ **Laplace 变换法** —— 最强工具，p 域求像函数 → 逆变换给出时间域解（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。
- **源函数族（点 / 面 / 球 / 柱）**：瞬时点源（n 维推广 `C = A t^(−n/2) exp(−r²/4Dt)`）、瞬时面源（一维基本解）、瞬时球源（三维有限初始分布）、瞬时柱源（二维有限初始分布）（源：[[Infinite and Semi-Infinite Media (Crank Ch.3)]]）。
- **反射法直接编码边界条件**：不透水膜（PP 底膜）对应 `dC/dx = 0`；透湿膜（顶表层）对应 `dC/dx + hc = 0`（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。
- **推导逻辑链**：恒 D PDE → 试探解 → 质量守恒定 A → 反射+叠加 → 扩展初值 → 分离变量 → Laplace 变换（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。
- **柱/球坐标工具**：Bessel 函数（I₀, J₀, J₁）是柱/球坐标下的标准工具（源：[[Infinite and Semi-Infinite Media (Crank Ch.3)]]）。

## Hygiene Relevance 卫材关联

- **SAP 单球溶胀有解析解。** 球源轴心解 `C = C₀{1 − exp(−a²/4Dt)}` 直接给出单个 SAP 微球（半径 a）球心浓度的指数演化，可估算 SAP 吸水饱和速率初段（源：[[Infinite and Semi-Infinite Media (Crank Ch.3)]]）。
- **单球=原子单元，多粒子场可叠加。** 平面源格林函数被直接用作 SAP 建模的"原子单元"，多个 SAP 颗粒场按叠加原理合成（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。
- **湿巾湿斑扩散=圆盘源问题。** `Q(t)` 的解析级数形式（Rideal & Tadayon 方法）可用于湿巾湿斑扩散（源：[[Infinite and Semi-Infinite Media (Crank Ch.3)]]）。
- **反射法映射芯体分层结构。** 芯体的不透水 PP 底膜与透湿顶表层分别对应两类反射边界（源：[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]）。
- **半无限域是芯体建模的有效近似。** 芯体厚度（约 1–2 mm）远大于初期扩散长度时，半无限域解适用（源：[[Infinite and Semi-Infinite Media (Crank Ch.3)]]）。

## Open Questions 待补

- 形式化定义缺失：本库来源页只给出**平面源/点源/球源/圆盘源**的具体表达式与用法，未给出格林函数的一般定义 `[待补]`。
- 未见到把格林函数解与本库**实测**芯体/SAP 数据对照的算例 `[待补]`。
- 叠加原理在**非线性（D 随浓度变化）** 情形下的适用性边界未在引用来源中讨论 `[待补]`。

## Related Sources 关联来源

- Citing sources 引用来源：[[Infinite and Semi-Infinite Media (Crank Ch.3)]]、[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]
- Parent book 父书：[[Mathematics of Diffusion]]
- Adjacent concepts 相邻概念：[[Fick 定律]]、[[Laplace 变换]]、[[Bessel 函数]]、[[时间滞后法 Time Lag Method]]、[[湿迁移 Wet Migration]]
- Application pages 应用页：[[SAP（高吸水树脂）]]、[[吸收芯体]]、[[水凝胶 Hydrogel]]

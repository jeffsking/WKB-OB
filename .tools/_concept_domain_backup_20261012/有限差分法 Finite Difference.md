---
type: concept
title: "有限差分法 Finite Difference"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [finite-difference, explicit-scheme, numerical-stability, diffusion, SAP-modeling, grid-convergence]
---

# 有限差分法 Finite Difference

> 📌 **Page completed 2026-09-30** from 1 citing source (4 vault pages carry verbatim excerpts). All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）。库内给出的是**可执行的格式口径**：

- 有限差分法在库内以**显式差分格式**出现——把扩散方程的导数用网格差分替代，逐时层推进；其可用性由**稳定性条件**约束（源：[[Numerical Methods for Diffusion (Crank Ch.8)]]）。
- 方法族定位：库内把"有限差分法"与 CFD、Navier-Stokes、有限元法、有限体积法、k-ε 湍流模型、Stokes Number、Lagrangian Particle Tracking、虚拟原型并列为数值模拟方法（源：[[Computational Modeling in Absorbent Technology]]）。
- `[待补]`：引用页未给出"有限差分法"的词典式定义。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 显式差分格式 explicit scheme | $c_i^{j+1} = r\,c_{i-1}^{j} + (1-2r)c_i^{j} + r\,c_{i+1}^{j}$ | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| 稳定性条件 stability | $r \le \tfrac12$（即 $\delta T \le \tfrac12(\delta X)^2$） | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| 无量纲化 scaling | $T = Dt/l^2$、$X = x/l$、$c = C/C_0$ | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| SAP 高 D 区间的时间步 | δt 必须极小 → 计算量剧增 | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| 网格收敛（吸收模型 v9，孔隙率） | 粗网格 0.347 → 细网格 0.284（**尚未收敛**） | （源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]） |
| 有限厚 SAP 片层的适用性 | Boltzmann 变换只对半无限 SAP 颗粒表面有效；**有限厚 SAP 片层需改用数值方法** | （源：[[Concentration-Dependent Diffusion Methods (Crank Ch.7)]]） |

## Method / Mechanism 方法 / 机理

- **显式推进 + 硬稳定性约束**：格式由空间二阶差分 + 时间前差构成，$r\le\tfrac12$ 是硬约束，直接决定时间步长上限（源：[[Numerical Methods for Diffusion (Crank Ch.8)]]）。
- **无量纲化使解可复用**：不同 SAP 粒径 / D / 厚度可从同一组无量纲解缩放，极大节省计算量（源：[[Numerical Methods for Diffusion (Crank Ch.8)]]）。
- **各向异性须用张量**：复合芯体 MD/CD 性能差异不能用标量 D，Fick 定律只适用于各向同性介质（源：[[Fick 定律]]；[[Diffusion Equations (Crank Ch.1)]]）。
- **方法选择由几何决定**：半无限域可用 Boltzmann 变换降为 ODE；有限厚片层改用数值方法（源：[[Concentration-Dependent Diffusion Methods (Crank Ch.7)]]）。

## Hygiene Relevance 卫材关联

- **工程落点**：SAP 建模与吸收芯体湿迁移 FEM——"绝大多数工程实际问题靠本章方法求解"（源：[[Numerical Methods for Diffusion (Crank Ch.8)]]）。
- **时间步代价即算力成本**：溶胀后期高 D 区间时间步必须极小，直接决定 SAP 建模与芯体湿迁移 FEM 的计算量（源：[[Numerical Methods for Diffusion (Crank Ch.8)]]）。
- **网格无关性验证是独立动作**：细化 ≠ 已收敛，收敛性需专门排期与自动化脚本（源：[[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]）。

## Open Questions 待补

- **收敛性未证实**：孔隙率下限从 0.347 降到 0.284 仍未收敛；"细网格更可信"是源文判断、**无实验佐证**（源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]）。
- 库内未给出"有限差分法"的独立定义句，也未给出显式/隐式格式在本库算例中的误差量级对比 `[待补]`。

## Related Sources 关联来源

- [[Numerical Methods for Diffusion (Crank Ch.8)]]（主要引用来源）
- [[数值模拟 Numerical Simulation]]、[[Mathematics of Diffusion]]、[[Concentration-Dependent Diffusion Methods (Crank Ch.7)]]
- [[Computational Modeling in Absorbent Technology]]、[[有限元法]]、[[有限体积法]]、[[CFD 计算流体力学]]、[[虚拟原型 Virtual Prototyping]]
- [[Fick 定律]]、[[Diffusion Equations (Crank Ch.1)]]、[[Boltzmann 变换]]、[[格林函数 Green's Function]]、[[Bessel 函数]]
- [[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]、[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]
- [[SAP（高吸水树脂）]]、[[吸收芯体]]

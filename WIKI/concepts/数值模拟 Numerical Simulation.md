---
type: concept
title: "数值模拟 Numerical Simulation"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [numerical-simulation, diffusion, SAP, core-modeling, grid-convergence, differentiable-CFD, finite-difference]
---

# 数值模拟 Numerical Simulation

> 📌 **Page completed 2026-09-30** from 1 citing source (10 vault pages carry verbatim excerpts). All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）。本库引用页只给出**定位式口径**而非定义句：

- 数值方法是 **SAP 建模与芯体湿迁移 FEM 的工程基础**；"绝大多数工程实际问题靠本章方法求解"（源：[[Numerical Methods for Diffusion (Crank Ch.8)]]）。
- 库内把"数值模拟"作为一个**方法族**与 CFD、Navier-Stokes、有限差分法、有限元法、有限体积法、k-ε 湍流模型、Stokes Number、Lagrangian Particle Tracking、虚拟原型并列登记（源：[[Computational Modeling in Absorbent Technology]]）。
- `[待补]`：引用页未给出"数值模拟 vs 解析解 vs 实验"的边界定义。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 无量纲时间 dimensionless time | $T = Dt/l^2$ | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| 显式差分稳定性条件 stability | $r \le \tfrac12$（即 $\delta T \le \tfrac12(\delta X)^2$） | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| 显式差分格式 explicit scheme | $c_i^{j+1} = r\,c_{i-1}^{j} + (1-2r)c_i^{j} + r\,c_{i+1}^{j}$ | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| SAP 溶胀后期的时间步代价 | 高 D 区间 δt 必须极小 → 计算量剧增 | （源：[[Numerical Methods for Diffusion (Crank Ch.8)]]） |
| 芯体孔隙率收敛下限（v9 模型）| 粗网格 0.347 → 细网格 0.284（源文建议再试 60×24 网格，**尚未收敛**） | （源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]） |
| 网格收敛验证排期 | Phase 0.2 单独立项 0.5 天，并需自动化运行脚本 | （源：[[v10 优化执行方案建议（Claude Code + Gemini CLI 分工评估 · 2026-06-16）]]） |

## Method / Mechanism 方法 / 机理

- **无量纲化是工程效率核心**：$T=Dt/l^2$、$X=x/l$、$c=C/C_0$ 使不同 SAP 粒径 / D / 厚度可从同一组无量纲解缩放复用（源：[[Numerical Methods for Diffusion (Crank Ch.8)]]）。
- **稳定性条件是硬约束**：显式格式 $r\le\tfrac12$ 决定时间步长；SAP 高 D 区间时间步必须极小，直接决定计算量（源：[[Numerical Methods for Diffusion (Crank Ch.8)]]）。
- **各向异性必须用张量**：复合芯体 MD/CD 性能差异不能用标量 D，须用**扩散张量**（源：[[Diffusion Equations (Crank Ch.1)]]；[[Fick 定律]]）。
- **可微分求解器路线**：把传统 CFD 求解流程包裹进 PyTorch/JAX 的自动微分图，使整个数值模拟可微分，梯度可从物理模拟反向传播到神经网络，用于训练与优化（源：[[Open-Source AI-CFD Frameworks Landscape（开源 AI+流体仿真框架调研）]]）。
- **"仿真替代试错"方法论**：先建模 → 敏感性排序 → 界定实验范围，可把工艺开发从试错转为定向搜索（源：[[Manufactured Fibre Technology Ch05 Computer Simulation of Melt Spinning]]）。

## Hygiene Relevance 卫材关联

- 库内落点明确为 **SAP 建模与吸收芯体湿迁移 FEM**（源：[[Numerical Methods for Diffusion (Crank Ch.8)]]）。
- 二维吸收模型（v8/v9/v11）即数值模拟产物；v9 **不含反渗**，其结论**不能外推到回渗**（源：[[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]）。
- 代理模型路线：卫材仿真落点为 2D Absorption Model v11 / v8 与 REL 芯体模拟（源：[[Open-Source AI-CFD Frameworks Landscape（开源 AI+流体仿真框架调研）]]）。

## Open Questions 待补

- **网格收敛未获证实**：孔隙率下限从 0.347 降到 0.284 仍未收敛，"细网格更可信"是源文判断、**无实验佐证**（源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]）。
- "渗透率下降约 2–5 倍"与细网格 20.3%（≈5×）、粗网格 44.6%（≈2.2×）的对应关系源文未明确（源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]）。
- 库内未给出"数值模拟"的独立定义句 `[待补]`。

## Related Sources 关联来源

- [[Numerical Methods for Diffusion (Crank Ch.8)]]（主要引用来源）
- [[Diffusion Equations (Crank Ch.1)]]、[[Fick 定律]]
- [[有限差分法 Finite Difference]]、[[有限元法]]、[[有限体积法]]、[[CFD 计算流体力学]]、[[虚拟原型 Virtual Prototyping]]
- [[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]、[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]、[[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]
- [[Computational Modeling in Absorbent Technology]]、[[Open-Source AI-CFD Frameworks Landscape（开源 AI+流体仿真框架调研）]]、[[Manufactured Fibre Technology Ch05 Computer Simulation of Melt Spinning]]
- [[SAP（高吸水树脂）]]、[[吸收芯体]]

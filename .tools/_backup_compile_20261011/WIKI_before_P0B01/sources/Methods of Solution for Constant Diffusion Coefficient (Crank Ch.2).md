---
type: source
title: "Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch02_METHODS_OF_SOLUTION_WHEN_THE_DIFFUSION_COEFFICIENT_IS_CONSTANT_report.md.md
original_link: ""
date_published: 1975
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
author: "J. Crank"
edition: "2nd"
publisher: "Clarendon Press, Oxford"
year: 1975
isbn: ""
original_language: "EN"
parent_book: "[[Mathematics of Diffusion]]"
key_claims:
  - "三类解析解工具箱：反射与叠加法、分离变量法、Laplace 变换法（最强工具）"
  - "两类标准解分工：小时间用误差函数类（数值评估方便），大时间用三角函数级数（收敛性最好）"
  - "平面源格林函数 C = (M/2(πDt)^½) exp(-x²/4Dt) 是基本'砖块'——SAP 单个微球可视为瞬时点源"
  - "反射法利用线性方程叠加性构造半无限域解——不透水膜 dC/dx=0，透湿膜 dC/dx+hc=0"
  - "Laplace 变换对复合芯体多层结构建模尤其关键"
pages_linked: ["[[Mathematics of Diffusion]]", "[[SAP（高吸水树脂）]]", "[[Fick 定律]]", "[[格林函数 Green's Function]]", "[[Laplace 变换]]"]
---

# Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)

*J. Crank — The Mathematics of Diffusion, 2nd ed., Clarendon Press 1975 · Ch.2 · 8 KB*

## One-line Position 一句话定位

**恒 D 情形下解析解的三类工具箱**——反射与叠加法、分离变量法、Laplace 变换法，确立误差函数类与三角函数级数两类标准解的分类体系，为 SAP 溶胀动力学与芯体湿迁移建模提供解析基础。

## Summary 摘要

- **三类解析方法**：
  1. 反射与叠加法——利用线性方程叠加性构造边界解
  2. 分离变量法——C = u(x) exp(-Dα²t)，得到 Bessel/三角本征值问题
  3. Laplace 变换法——最强工具，p 域求像函数→逆变换给出时间域解
- **两类标准解**：
  - 误差函数类：小时间数值评估方便
  - 三角函数级数：大时间收敛性最好
- **平面源格林函数**：C = (M/2(πDt)^½) exp(-x²/4Dt)——基本"砖块"。
- **反射法**：不透水边界 dC/dx=0（PP 底膜）；透湿边界 dC/dx+hc=0（顶表层）。
- **推导逻辑链**：恒 D PDE→试探解→质量守恒定 A→反射+叠加→扩展初值→分离变量→Laplace 变换。

## Key Numbers & Conclusions 提炼数字与结论

| 项目 | 数值/结论 | 来源 |
|---|---|---|
| 三类方法 | 反射/分离变量/Laplace | §2.1 |
| 两类标准解 | 误差函数 vs 三角级数 | §2.1 |
| 平面源格林函数 | C = (M/2(πDt)^½)exp(-x²/4Dt) | §2.2.1 |
| 不透水边界 | dC/dx = 0 | §2.2.2 |
| 透湿边界 | dC/dx + hc = 0 | §2.2.2 |
| Laplace 变换 | 最强工具 | §2.1 |

## Key Claims 关键论断

- **Laplace 变换是最强工具**——对复杂问题（多层复合芯体）尤其关键。
- **两类标准解分工明确**——小时间（SAP 吸液初期）用误差函数，大时间（稳态接近）用级数。
- **平面源格林函数是 SAP 建模的原子单元**——单个 SAP 微球=瞬时点源，多粒子场可叠加。
- **反射法直接映射芯体结构**——不透水膜（PP 底膜）与透湿膜（顶表层）分别对应 dC/dx=0 与 dC/dx+hc=0。

## Related Pages 关联页面

- [[Mathematics of Diffusion]]
- [[SAP（高吸水树脂）]]
- [[Fick 定律]]
- [[格林函数 Green's Function]]
- [[Laplace 变换]]

## Source 原文

- 本地路径 Local path：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch02_METHODS_OF_SOLUTION_WHEN_THE_DIFFUSION_COEFFICIENT_IS_CONSTANT_report.md.md`
- 原文链接 Original link：

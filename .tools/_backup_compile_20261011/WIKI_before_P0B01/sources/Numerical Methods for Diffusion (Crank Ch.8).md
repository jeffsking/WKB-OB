---
type: source
title: "Numerical Methods for Diffusion (Crank Ch.8)"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch08_NUMERICAL_METHODS_report.md.md
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
  - "无量纲化 T=Dt/l², X=x/l, c=C/C₀——不同粒径/D/厚度的吸液曲线可从同一组无量纲解缩放得到"
  - "显式有限差分格式稳定性条件 r≤½（δT≤½(δX)²）——SAP 高 D 区间时间步必须极小，计算量剧增"
  - "工程实际中（SAP 建模、芯体湿迁移 FEM）绝大多数问题靠本章方法"
pages_linked: ["[[Mathematics of Diffusion]]", "[[SAP（高吸水树脂）]]", "[[有限差分法 Finite Difference]]", "[[数值模拟 Numerical Simulation]]"]
---

# Numerical Methods for Diffusion (Crank Ch.8)

*J. Crank — The Mathematics of Diffusion, 2nd ed., Clarendon Press 1975 · Ch.8 · 8 KB*

## One-line Position 一句话定位

**数值方法体系——SAP 建模与芯体湿迁移 FEM 的工程基础**——无量纲化 T=Dt/l² 使不同参数问题可缩放复用；显式差分稳定性条件 r≤½ 决定时间步长；绝大多数工程实际问题靠本章方法求解。

## Summary 摘要

- **无量纲化**：T=Dt/l², X=x/l, c=C/C₀——不同粒径/D/厚度可从同一组无量纲解缩放。
- **显式差分**：cᵢ^(j+1) = rcᵢ₋₁^j + (1-2r)cᵢ^j + rcᵢ₊₁^j，稳定性 r≤½。
- **SAP 影响**：高 D 区间（溶胀后期）时间步必须极小，计算量剧增。
- **工程应用**：SAP 建模、芯体湿迁移 FEM 绝大多数问题靠本章方法。

## Key Numbers & Conclusions 提炼数字与结论

| 项目 | 数值/结论 | 来源 |
|---|---|---|
| 无量纲时间 | T = Dt/l² | §8.2 |
| 稳定性条件 | r ≤ ½ (δT ≤ ½(δX)²) | §8.4 |
| 显式差分格式 | cᵢ^(j+1) = rcᵢ₋₁^j + (1-2r)cᵢ^j + rcᵢ₊₁^j | §8.4 |
| SAP 影响 | 高 D 区间 δt 必须极小 | 业务解读 |

## Key Claims 关键论断

- **无量纲化是工程效率核心**——不同 SAP 粒径/D/厚度可从同一组解缩放，极大节省计算量。
- **稳定性条件 r≤½ 是硬约束**——SAP 高 D 区间时间步必须极小，计算量剧增。

## Related Pages 关联页面

- [[Mathematics of Diffusion]]
- [[SAP（高吸水树脂）]]
- [[有限差分法 Finite Difference]]
- [[数值模拟 Numerical Simulation]]

## Source 原文

- 本地路径 Local path：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch08_NUMERICAL_METHODS_report.md.md`
- 原文链接 Original link：

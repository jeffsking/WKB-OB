---
type: source
title: "Diffusion Equations (Crank Ch.1)"
source_type: book
source_path: RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch01_THE_DIFFUSION_EQUATIONS_report.md.md
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
  - "Fick 第一定律 F = -D dC/dx 是扩散数学理论的核心假设——类比热传导的线性本构关系"
  - "Fick 第二定律 ∂C/∂t = D ∂²C/∂x² 是全书唯一核心 PDE，所有后续 14 章都在此框架上展开"
  - "D 的浓度依赖性决定 Fick 定律能否'常 D'近似——SAP 低吸水比时 D≈常数，溶胀区间后 D(C) 可跨 3-4 个数量级"
  - "各向同性假设决定方程形式——复合芯体（顶表层/纺粘/木浆/SAP/底膜）MD/CD 性能差异显著，需张量 D_ij"
  - "无对流假设排除强制对流主导场景——湿巾擦拭动作中的动压驱进需额外项"
pages_linked: ["[[Mathematics of Diffusion]]", "[[SAP（高吸水树脂）]]", "[[吸收芯体]]", "[[Fick 定律]]", "[[湿迁移 Wet Migration]]"]
---

# Diffusion Equations (Crank Ch.1)

*J. Crank — The Mathematics of Diffusion, 2nd ed., Clarendon Press 1975 · Ch.1 · 12 KB*

## One-line Position 一句话定位

**扩散数学理论奠基章**——建立 Fick 定律（一维/标量形式）作为数学公理，推导 Fick 第二定律（扩散 PDE），延伸到各向异性介质与多组分情形。SAP 溶胀动力学、芯体吸液速率、湿迁移模型的本原公式均源于此章。

## Summary 摘要

- **扩散定义**：扩散是分子随机运动驱动的物质从系统一部分传输到另一部分的过程。
- **Fick 第一定律**：F = -D dC/dx——传递速率正比于浓度梯度；类比热传导（Fourier 定律）。
- **D 的浓度依赖性**：稀溶液中 D≈常数；高分子（SAP）中 D(C) 剧烈变化，可跨 3-4 个数量级。
- **Fick 第二定律**：∂C/∂t = D ∂²C/∂x²（一维恒 D）——全书唯一核心 PDE。
- **各向异性介质**：Fick 定律仅适用于各向同性介质；复合芯体需扩散张量 D_ij。
- **推导逻辑链**：物理动机→分子随机行走→统计平均给出净通量→Fick 假设→微元体质量守恒→保守形式→恒 D 化简。

## Key Numbers & Conclusions 提炼数字与结论

| 项目 | 数值/结论 | 来源 |
|---|---|---|
| Fick 第一定律 | F = -D dC/dx | §1.2 |
| Fick 第二定律 | ∂C/∂t = D ∂²C/∂x² | §1.3 |
| SAP D(C) 变化范围 | 3-4 个数量级 | 业务解读 |
| SAP 低吸水比阈值 | DR < 20 | 业务解读 |
| 恒 D 适用性 | 稀溶液/低吸水比 | §1.2 |
| 各向异性要求 | 张量 D_ij | §1.4 |

## Key Claims 关键论断

- **Fick 定律是扩散数学的唯一核心假设**——SAP 溶胀、芯体吸液、湿迁移、湿巾均匀性模型均基于此。
- **D(C) 剧烈变化是 SAP 吸液速率非线性化的数学根源**——低吸水比时 D≈常数（线性），溶胀后 D(C) 跨 3-4 个数量级（非线性）。
- **复合芯体是典型各向异性介质**——MD/CD 性能差异需在模型中用扩散张量取代标量 D。
- **无对流假设的局限**——湿巾擦拭等强制对流场景需附加对流项。

## Related Pages 关联页面

- [[Mathematics of Diffusion]]
- [[SAP（高吸水树脂）]]
- [[吸收芯体]]
- [[Fick 定律]]
- [[湿迁移 Wet Migration]]

## Source 原文

- 本地路径 Local path：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch01_THE_DIFFUSION_EQUATIONS_report.md.md`
- 原文链接 Original link：

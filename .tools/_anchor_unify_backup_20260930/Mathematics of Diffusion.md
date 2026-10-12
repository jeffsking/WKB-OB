---
type: source
title: "Mathematics of Diffusion"
source_type: book-index
author: "J. Crank"
edition: "2nd"
publisher: "Clarendon Press, Oxford"
year: 1975
isbn: "978-0-19-852113-0"
original_language: "EN"
source_path: RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/THE_MATHEMATICS_OF_DIFFUSION_CLARENDON_P.pdf.md
date_published: 1975
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
summary_cn: "扩散数学经典参考书（Crank 第2版，Clarendon 1975）——15章完整覆盖Fick定律、解析/数值解法、D(C)变系数扩散、非菲克扩散、复合介质、动边界、反应-扩散耦合、湿热耦合；SAP溶胀动力学、芯体吸液、湿迁移建模的理论基础"
key_claims:
  - "全书唯一核心PDE：Fick第二定律 ∂C/∂t = D∂²C/∂x²——所有14章都在此框架上展开"
  - "SAP溶胀动力学核心数学技巧：u=Cr变换将球坐标映射到一维线性PDE"
  - "SAP'S形'吸液曲线物理根源：Alfrey-Gurnee-Lloyd三分类（Case II→非菲克→Case I）"
  - "SAP D测量行业标准方法：时间滞后法 L=l²/6D（Daynes 1920, Barrer 1951）"
  - "复合芯体串联阻力模型：总R = Σ(lᵢ/Pᵢ)——芯体吸水速率/防回渗建模基础"
  - "湿热耦合：'观察到的吸湿曲线实际是冷却曲线'——湿冷感物理根源"
pages_linked: ["[[Diffusion Equations (Crank Ch.1)]]", "[[Methods of Solution for Constant Diffusion Coefficient (Crank Ch.2)]]", "[[Infinite and Semi-Infinite Media (Crank Ch.3)]]", "[[Diffusion in a Plane Sheet (Crank Ch.4)]]", "[[Diffusion in a Cylinder (Crank Ch.5)]]", "[[Diffusion in a Sphere (Crank Ch.6)]]", "[[Concentration-Dependent Diffusion Methods (Crank Ch.7)]]", "[[Numerical Methods for Diffusion (Crank Ch.8)]]", "[[Calculated Results for Variable Diffusion Coefficients (Crank Ch.9)]]", "[[Definition and Measurement of Diffusion Coefficients (Crank Ch.10)]]", "[[Non-Fickian Diffusion (Crank Ch.11)]]", "[[Diffusion in Heterogeneous Media (Crank Ch.12)]]", "[[Moving Boundaries (Crank Ch.13)]]", "[[Diffusion and Chemical Reaction (Crank Ch.14)]]", "[[Simultaneous Diffusion of Heat and Moisture (Crank Ch.15)]]", "[[SAP（高吸水树脂）]]", "[[吸收芯体]]", "[[Fick 定律]]", "[[湿迁移 Wet Migration]]"]
---

# Mathematics of Diffusion

*J. Crank — 2nd ed., Clarendon Press, Oxford, 1975 · 15 章 · 扩散数学经典参考*

## Book Metadata 书籍元数据

| 字段 | 值 |
|---|---|
| Author 作者 | J. Crank |
| Edition 版次 | 2nd |
| Publisher 出版商 | Clarendon Press, Oxford |
| Year 年份 | 1975 |
| ISBN | 978-0-19-852113-0 |
| Original Language 原始语言 | EN |
| Relevance 相关度 | P0（卫材主线：SAP 溶胀动力学、芯体吸液、湿迁移建模的理论基础） |
| Chapters 章节数 | 15 |

## One-line Summary 一句话综述

**EN**: The classic reference for the mathematics of diffusion. 15 chapters cover Fick's laws, analytical and numerical solution methods, concentration-dependent diffusion, non-Fickian diffusion, heterogeneous media, moving boundaries, reaction-diffusion coupling, and simultaneous heat-moisture diffusion — the theoretical foundation for SAP swelling kinetics, absorbent core modeling, and wet migration simulation.

**中文**: 扩散数学经典参考书——15 章完整覆盖 Fick 定律、解析/数值解法、D(C) 变系数扩散、非菲克扩散、复合介质、动边界、反应-扩散耦合、湿热耦合。SAP 溶胀动力学、芯体吸液、湿迁移建模的理论基础。

## Key Themes 核心主题

1. **Fick 定律与扩散 PDE**（Ch 1）：F = -D dC/dx 是核心假设；∂C/∂t = D∂²C/∂x² 是全书唯一核心 PDE
2. **恒 D 解析解法**（Ch 2-3）：反射/叠加、分离变量、Laplace 变换；误差函数类与三角函数级数
3. **三维几何模型**（Ch 4-6）：片层（芯体/湿巾）、柱（纤维）、球（SAP 颗粒）——u=Cr 变换是关键技巧
4. **D(C) 变系数扩散**（Ch 7-9）：Boltzmann 变换、数值方法、等效扩散系数——SAP D(C) 常呈指数上升型
5. **D 测量方法学**（Ch 10）：时间滞后法 L=l²/6D 是行业标准；SAP 必须用质量固定参考系
6. **非菲克扩散**（Ch 11）：Alfrey-Gurnee-Lloyd 三分类——SAP S 形吸液曲线的物理根源
7. **复合介质**（Ch 12）：串联阻力模型 Σ(lᵢ/Pᵢ)——芯体多层结构建模基础
8. **动边界/Stefan 问题**（Ch 13）：SAP 溶胀前沿的定量实现
9. **反应-扩散耦合**（Ch 14）：SAP 交联网络水固定化→等效 D 下降 (R+1) 倍
10. **湿热耦合**（Ch 15）：'湿冷感'物理根源——观察到的吸湿曲线实际是冷却曲线

## Key Claims 关键论断

1. **Fick 第二定律是全书唯一核心 PDE**——所有 14 章都在此框架上展开，SAP/芯体/湿巾建模均基于此。
2. **SAP 溶胀动力学核心数学技巧是 u=Cr 变换**——球坐标映射到一维线性 PDE，直接借用片层解。
3. **SAP S 形吸液曲线的物理根源是 Case II→非菲克→Case I 三阶段**——干态玻璃态快速溶剂化到橡胶态慢扩散的过渡。
4. **时间滞后法 L=l²/6D 是 SAP 行业 D 测量标准**——Daynes 1920, Barrer 1951 确立的行业标准方法。
5. **SAP 必须用质量固定参考系定义 D**——因溶胀体积剧变，否则 D 值无法比较。
6. **复合芯体串联阻力模型 Σ(lᵢ/Pᵢ) 是吸水速率建模基础**——每层独立贡献传质阻力。
7. **SAP 交联网络水固定化使等效 D 下降 (R+1) 倍**——这是 SAP 吸水'慢'的分子尺度原因。
8. **'湿冷感'是湿热耦合的物理表现**——观察到的吸湿曲线实际是冷却曲线，耦合效应量级显著。

## Related Pages 关联页面

- [[SAP（高吸水树脂）]]
- [[吸收芯体]]
- [[Fick 定律]]
- [[湿迁移 Wet Migration]]
- [[SAP 溶胀 SAP Swelling]]
- [[Non-Fickian Diffusion (Crank Ch.11)]]
- [[湿热耦合 Heat-Moisture Coupling]]

## Source 原文

- 本地路径 Local path：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/THE_MATHEMATICS_OF_DIFFUSION_CLARENDON_P.pdf.md`
- 原文链接 Original link：

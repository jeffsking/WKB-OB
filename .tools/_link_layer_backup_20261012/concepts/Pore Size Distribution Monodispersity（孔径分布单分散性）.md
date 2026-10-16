---
type: concept
title: "Pore Size Distribution Monodispersity（孔径分布单分散性）"
domain: [卫材研发, 芯体与吸收]
status: growing
updated: 2026-09-30
tags: [孔径分布, 单分散, 孔隙连通性, 解吸能, 回渗, 非织造布]
---

# Pore Size Distribution Monodispersity（孔径分布单分散性）

> 一句话定义 One-line definition：孔径分布的**宽窄程度**——分布越窄（越 monodisperse，单分散），孔径越均一；与"最可几孔径（mode pore size）"是**两个独立变量**，回渗差异往往由前者而非后者驱动。

## 机理 / 结构拆解 Mechanism and Structure

1. **mode 相同 ≠ 性能相同**：Depend 与 Always Discreet 的面层/导流层**最可几孔径基本相同**（面层相当；surge 320 vs 315 μm），但 AD 的**分布更单分散**。因此"用孔径解释回渗"的假设被原文明确否证。
2. **窄分布 → 孔隙连通性**：原文提出的待验证机制是——更窄的孔径分布可能支持导流层内部的**孔隙连通性（pore connectivity）**，从而降低滞留与回渗。这是**假设**，不是已证结论。
3. **解吸能的真实驱动量是克重，不是孔径**：AD surge 的特征毛细压力略高于 Depend，但**解吸能更低**（8.26E+03 vs 1.23E+04），原因是 AD surge 克重显著更低（49.95 vs 76.97 gsm）。即"液体滞留量"由材料体积决定，不由孔径决定。
4. **Young-LaPlace 框架下的解释力边界**：Δp = −2γcosθ / R 给出单个孔的压力，但真实材料是孔径分布 + 连通性网络；**分布宽度决定网络行为**，这是方程覆盖不到的部分。
5. **与界面间隙并列**：孔径分布（材料内部）与层压界面间隙（层间，见 [[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]）是两条独立的回渗通道，须分别治理。

## 关键参数表 Key Parameters

| 参数 Parameter | 典型值 / 范围 Typical Value | 出处 Source |
|---|---|---|
| AD Surge mode / median / mean 孔径 | 320 / 331 / 530 μm | [[Rewet Competitive Analysis - Depend vs Always Discreet Intake System（回渗竞品分析 · 2025-09-11）]] |
| Depend Surge mode / median / mean 孔径 | 315 / 432 / 535 μm | 同上 |
| 面层孔径对比 | mode 相当；AD 分布更窄（更单分散） | 同上 |
| AD Surge 克重 | 49.95 gsm | 同上 |
| Depend Surge 克重 | 76.97 gsm | 同上 |
| 解吸能（des） | AD 8.26E+03 vs Depend 1.23E+04 | 同上 |
| 特征毛细压力 | AD 略高于 Depend | 同上 |
| 实测表面张力 | AD 48.87 vs Depend 48.00 dynes/cm | 同上 |

> ⚠️ **禁止无来源参数 No unsourced numbers**：表中数字均来自上列源摘要页；"窄分布 → 连通性更好"的因果链原文以问句形式提出（"Could these lead to better pore connectivity…?"），**库内尚无验证数据**，标 `[待验证]`。

## 相邻概念 Adjacent Concepts

- 上位：[[Intake System（摄入系统）]]、[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]
- 表征方法：[[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]、[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]、[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- 滞留机理：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]、[[亲水-疏水梯度设计]]、[[毛细梯度设计]]
- 材料侧：[[ADL（导流层）]]、[[热风粘合无纺布]]、[[无纺布五大工艺对比]]
- 对比：[[Depend vs Always Discreet Intake System（摄入系统回渗竞品对比）]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[Rewet Competitive Analysis - Depend vs Always Discreet Intake System（回渗竞品分析 · 2025-09-11）]]）：本页**修正了一个常见直觉**——竞品孔径"更小"是误判，真实差异在分布宽度与克重。这是本批最有价值的负面证据（negative evidence）。

- **教训一（先测分布再测均值）**：只报 mode/mean 孔径会把团队带向"改孔径"的错误方向；必须同时看分布宽度（单分散性）。
- **教训二（克重是解吸能的一阶量）**：降 surge 克重可同时降低解吸能与材料成本，但**必须同轮验证摄入速度**（否则重演 SIROCCO 的"回渗改善、摄入变差"）。
- **教训三（假设要标注）**：原文对"窄分布 → 连通性"用了问句，编译为页面时须保留 `[待验证]` 标记，不得升格为结论。

## 来源 Sources

- [[Rewet Competitive Analysis - Depend vs Always Discreet Intake System（回渗竞品分析 · 2025-09-11）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Rewet Competitive Analysis 9-11-25-1.pptx.md`

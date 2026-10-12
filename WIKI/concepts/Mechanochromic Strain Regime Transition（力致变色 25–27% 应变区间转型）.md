---
type: concept
title: "Mechanochromic Strain Regime Transition（力致变色 25–27% 应变区间转型）"
domain: [卫材研发, 力致变色, 材料表征]
status: growing
updated: 2026-09-30
tags: [力致变色, mechanochromic, 应变区间, 剪切变稀, 信号完整性]
---

# Mechanochromic Strain Regime Transition（力致变色 25–27% 应变区间转型）

> 一句话定义 One-line definition：力致变色材料在**约 25–27% 应变**处发生的**流变区间切换**——低于该值处于黏弹区（Zone 1，信号稳定可逆），高于该值进入非弹性流动区（Zone 2，灵敏度见顶但信号衰减）；配方必须把自己锁在 Zone 1 才有工程可用性。

## 机理 / 结构拆解 Mechanism and Structure

1. **Zone 1（<25% 应变，黏弹区 Viscoelastic Regime）**：材料呈弹性响应。特征为**高稳定性、可靠的方波状（square-like）输出信号、一致的颜色松弛（color relaxation）**——即受力变色、卸载复色可重复。
2. **Zone 2（>25% 应变，非弹性流动区 Inelastic Flow Regime）**：剪切变稀（shear-thinning）导致横向流动（lateral flow）。此时**灵敏度最大化，但信号稳定性下降，出现假阴性颜色衰减（false-negative color attenuation）**——看上去"没变色"，实为信号被流动抹平。
3. **转型带 25–27%**：两区之间的过渡是材料设计的临界带，也是工程上最需要精确标定的区域；文件把「掌握 25–27% 应变区间转型」列为推进的**准确前置条件（exact prerequisite）**。
4. **工程结论（Engineering Takeaway）**：信号完整性**完全取决于**把材料配方设计为严格工作在 Zone 1——不是"尽量"，而是配方边界的硬约束。
5. **与激活阈值的关系**：本页讲**应变轴**的可用窗口，[[Mechanochromic Activation Threshold Down-Shifting（力致变色激活阈值下调）]] 讲**应力轴**的激活窗口（儿科 20–150 kPa）；两者共同构成力致变色配方的"双窗口"约束。

## 关键参数表 Key Parameters

| 参数 Parameter | 典型值 / 范围 Typical Value | 出处 Source |
|---|---|---|
| Zone 1 上限（工作区） | <25% 应变 | [[Scaling Visible Force in Consumer Hygiene v2（可见力可视化放大路线 v2）]] |
| 转型带 | 25–27% 应变 | 同上 |
| Zone 2 起始 | >25% 应变 | 同上 |
| Zone 1 输出形态 | 方波状（square-like）信号、颜色松弛一致 | 同上 |
| Zone 2 失效形态 | 剪切变稀 → 横向流动 → 假阴性颜色衰减 | 同上 |
| 宏观架构应变上限 | 25%（"operating within 25% strain limits"） | 同上 |

> ⚠️ **禁止无来源参数 No unsourced numbers**：表中数字均来自上列源摘要页；不同聚合物体系（HPC 结构色 vs 萘并吡喃共价体系）各自的转型应变值、温度与速率依赖性库内暂无来源，标 `[待验证]`。

## 相邻概念 Adjacent Concepts

- 上位：[[Mechanochromic变色纤维]]、[[Chromism Taxonomy（变色现象分类）]]
- 并列窗口：[[Mechanochromic Activation Threshold Down-Shifting（力致变色激活阈值下调）]]
- 路线相关：[[Structural Colour Mechanochromism（结构色力致变色）]]、[[Mechanophore Mechanochromism（机械力致变色分子）]]、[[Printable Pressure-Activated Inks vs Covalent Mechanophores（力致变色两条落地路线）]]
- 流变与施加工艺：[[Ultra-Low Add-On Adhesive Application（超低添加量施胶）]]、[[Hot-Melt Slot Coating（热熔狭缝涂布）]]
- 应用：[[Front Belt Force Window（前腰带弹性力窗口）]]、[[Active Diagnostic Zones（主动诊断分区）]]、[[Skin Contact Pressure（皮肤接触压力）]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[Scaling Visible Force in Consumer Hygiene v2（可见力可视化放大路线 v2）]]）：本页结论为原文明确的工程指令——信号完整性完全取决于 Zone 1 配方；尚未有第二条独立来源，故 `status: seed`，后续须以实测数据复核。

- **教训一（别把灵敏度当指标）**：Zone 2 灵敏度最高却不可用——追求"更灵敏"会把配方推进假阴性区。指标应是**可逆性与信号一致性**，不是灵敏度上限。
- **教训二（前置条件排序）**：文件把掌握该区间转型列为 Phase 2 的"准确前置条件"，意味着放大（柔印打样、人因测试）之前必须先解决流变窗口。
- **待补 `[待验证]`**：HPC 体系与萘并吡喃体系各自的实际转型应变；加载速率与温度对转型带的漂移；非织造布基材约束下的有效应变分布。

## 来源 Sources

- [[Scaling Visible Force in Consumer Hygiene v2（可见力可视化放大路线 v2）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/X-Chromic/Scaling_Visible_Force v2.pptx.md`

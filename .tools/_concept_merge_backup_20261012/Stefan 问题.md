---
type: concept
title: "Stefan 问题"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [stefan-problem, moving-boundary, sap-swelling, diffusion, non-fickian]
---

# Stefan 问题

> 📌 **Page completed 2026-09-30** from 1 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义
Stefan 问题是一类**相变动边界问题**——其数学结构等价于**冰融化前沿**，可用成熟的 Stefan 工具（erfc 解、守恒条件）处理（源：[[Moving Boundaries (Crank Ch.13)]]）。

在库内它被用作 **SAP 溶胀前沿的定量实现框架**：SAP 凝胶-玻璃界面是"不可逆瞬时固定反应"的数学等价——尖锐边界表面在介质中移动（源：[[Moving Boundaries (Crank Ch.13)]]）。

## Key Parameters and Data 关键参数与数据
| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 数学等价 | 动边界数学结构 = **冰融化前沿**（Stefan 相变问题） | [[Moving Boundaries (Crank Ch.13)]] |
| 动边界定义 | "不可逆瞬时固定反应" 的数学等价 —— 尖锐边界表面在介质中移动 | [[Moving Boundaries (Crank Ch.13)]] |
| SAP 映射 | 溶胀前沿（凝胶-玻璃界面）：前沿**后面**为全湿凝胶（D 大），**前面**为干态玻璃（D ≈ 0） | [[Moving Boundaries (Crank Ch.13)]] |
| 求解工具 | erfc 解、守恒条件等成熟 Stefan 工具 | [[Moving Boundaries (Crank Ch.13)]] |
| 所属章节 | *Mathematics of Diffusion* 第 13 章（动边界 / Stefan 问题） | [[Mathematics of Diffusion]] |
| 扩散分类 | Alfrey-Gurnee-Lloyd 三分类：Case I（Fickian）/ Case II / 非菲克 | [[Fick 定律]] |

## Method / Mechanism 方法 / 机理
- **动边界模型**：尖锐边界表面在介质中移动，数学上等价于不可逆瞬时固定反应（源：[[Moving Boundaries (Crank Ch.13)]]）。
- **边界推进**：SAP 溶胀前沿以恒定或变速推进；前沿后为全湿凝胶（D 大），前沿前为干态玻璃（D ≈ 0）（源：[[Moving Boundaries (Crank Ch.13)]]）。
- **补齐玻璃态不足**：动边界模型是 **Case II / 非菲克过渡区的定量实现**，补充 D(C) Fick 定律在玻璃态的不足（源：[[Moving Boundaries (Crank Ch.13)]]）。
- **序列映射**：SAP 对应 干态玻璃态 → Case II → 非菲克 → 橡胶态 Case I，是 S 形吸液曲线的物理根源（源：[[Fick 定律]]）。

## Hygiene Relevance 卫材关联
- **SAP 溶胀动力学**：Stefan 问题框架用于定量描述 SAP 颗粒溶胀前沿的推进（源：[[Moving Boundaries (Crank Ch.13)]]）。
- **吸收芯体（REL core）建模**：作为 *Mathematics of Diffusion* 中与 SAP 溶胀前沿直接对应的定量工具，服务于芯体吸液过程建模（源：[[Mathematics of Diffusion]]）。

## Open Questions 待补
- 前沿推进速度（恒定 / 变速）的具体判据与取值 `[待补]`。
- 具体 D 值与 Stefan 解的数值标定 `[待补]`。

## Related Sources 关联来源
- [[Moving Boundaries (Crank Ch.13)]]
- [[Mathematics of Diffusion]]
- [[Fick 定律]]
- [[Non-Fickian Diffusion (Crank Ch.11)]]
- [[动边界 Moving Boundary]]
- [[Case II 扩散]]
- [[SAP 溶胀 SAP Swelling]]
- [[SAP（高吸水树脂）]]

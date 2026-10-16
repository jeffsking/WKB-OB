---
type: concept
title: "Pressure Sensory Test（压力触感测试）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-30
tags: [Pressure Sensory, 皮肤接触压力, WI-65030, 舒适度, 橡筋]
---

# Pressure Sensory Test（压力触感测试 / WI-65030）

> 一句话定义：用**气囊式传感器（air-bag sensor）**连接多通道主机记录仪，量化成品与橡筋材料在穿着状态下的**皮肤接触压力（Skin-Contact Pressure）**，是纸尿裤/拉拉裤舒适度评价的核心方法之一。

## Definition 定义 / Principle 原理

本方法不直接测"硬度"，而是测**局部压强**：把半充气的气囊传感器贴在标记点位（人体模型上的产品、或绕在手臂上的橡筋环），传感器受压后主机通道输出一个电压值，稳定后读取并 **×10** 得到最终读数（单位 V，作为相对压强指标）。其物理本质是**气囊形变 → 电压**的标定映射，因此读数一致性高度依赖气囊充气状态与贴附位置。

## 方法口径（Caliber 标定）

| 参数 | 典型值 / 范围 | 出处 |
|---|---|---|
| 仪器 | 主机记录仪 + 气囊式传感器（3 通道任选） | [[Pressure Sensory 测试方法.docx]] |
| 读数单位 | V（伏特），稳定后读数 **×10** | [[Pressure Sensory 测试方法.docx]] |
| 橡筋松弛长度 | 松弛长度 = 身体周长 ÷ 拉伸倍率（腰围为松弛宽度） | [[Pressure Sensory 测试方法.docx]] |
| 数据上限 | 单通道 ≤ 6000 点，满存需 CLEAR 后重测 | [[Pressure Sensory 测试方法.docx]] |
| 可比性前提 | 橡筋未拉伸、同位置、同处理条件 | [[Pressure Sensory 测试方法.docx]] |

> ⚠️ **禁止无来源参数**：上表均为单一 SOP（WI-65030）口径；库内暂无该传感器的电压—压强绝对标定曲线，压强定量换算标 `[待验证]`。

## 相邻概念

- 物理量：[[Skin Contact Pressure（皮肤接触压力）]]
- 橡筋力学：[[Elastic Tension & Creep（橡筋张力与回缩率）]]
- 同类穿戴评价：[[Mannequin BM Test（BM 假人测试）]]

## 经验教训

- **读数须 ×10 且点位一致**：原文强调"同一测试样品需要处理条件保持一致、测试期间保持同一位置"，否则电压读数不可比。
- **待补 `[待验证]`**：气囊传感器的电压—压强标定系数；不同尺寸/部位（腰围、腿围、折页）的合格阈值。

## 来源

- [[Pressure Sensory 测试方法.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/Pressure Sensory 测试方法.docx.md`

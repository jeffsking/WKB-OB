---
type: concept
title: "Glueless Bonding（无胶粘合工艺族）"
domain: [卫材研发, 表面处理与胶黏剂]
status: growing
updated: 2026-09-30
tags: [无胶, 热封, 超声波, 降本, 腿围, ADL, 弹性腰围]
---

# Glueless Bonding（无胶粘合工艺族）

> One-line definition 一句话定义：**用热封（thermo-sealing）或超声波焊接（ultrasonic bonding）取代热熔胶完成部件固定**的工艺族，覆盖腿围（cuffs）、导流层贴合（ADL application）与弹性腰围包覆（elastics entrapment）三个应用位。（中文：不是"少打胶"，而是"不打胶也能粘住"。）

## Definition 定义与三个应用位

| 应用位 | 取代的胶 | 替代工艺 | 量化收益 |
|---|---|---|---|
| **Glueless™ cuffs / narrow cuffs** | 弹性丝与内外无纺布之间的胶 | **间歇式热封（BLC thermo-sealing 双辊单元）** | 收口宽度 **15 mm → 8 mm**；无胶污染；原料节省 |
| **Glueless™ ADL application** | ADL 与面层之间的胶 | **超声波焊接** | 剥离力 **>0.6 N/50 mm**（= 目标值） |
| **Glueless Elastics Entrapment** | 弹性腰围（chassis waistband）上的胶 | 热粘合（已开发待产业化）/ 超声波（正与 Herrmann、Dukane 测试中） | 消除胶污染 |

## Mechanism 机理与前置条件

1. **超声波可焊性的硬前提**：**两种材料必须含同种或可相容的聚合物**。源文给的唯一判据示例 —— **ADL（含 PP 的双组分热风材料）+ PP 基非织造面层**可焊；跨聚合物体系（如 PP 面层 × PET 基 ADL）不能直接焊。
   > 对照：[[Ultrasonic Bonding of PET-Containing Topsheet]] —— 含 PET 面层的超声波焊接是另一套难点。
2. **热封路线的材料窗口**：SMS（spunmelt）**13–20 gsm**；弹性丝 **680–800 dtex**（此范围内可用同一花型，即花型不随 dtex 改）。
3. **过程控制**：热封后需**视觉系统（每侧一台相机）检查弹性丝完整性** —— 因为"断丝"在去胶后不再被胶固定，风险上移。
4. **与传统关系**：本工艺族与 [[Ultra-Low Add-On Adhesive Application（超低添加量施胶）]] 是**两条不同的降胶路线**——后者是"少打胶但仍用胶"，本族是"完全不用胶"。二者**不可混引**。
5. **⚠️ 未验证项**：热封剥离强度、长期老化、超声波在 450 m/min 以上的稳定性 —— 源文均未给 `[待验证]`。

## Key Parameter Table 关键参数表

| Parameter 参数 | Value 数值 | 出处 |
|---|---|---|
| Cuff 收口宽度 | **15 mm → 8 mm** | [[Fameccanica Innovations 2026（婴儿·巾·成人护理技术与创新总览）]] |
| Cuff 材料窗口 | SMS **13–20 gsm**；弹性丝 **680–800 dtex**（同花型） | 同上 |
| ADL-面层剥离力 | **>0.6 N/50 mm**（目标值） | 同上 |
| ADL / 面层克重 | ADL **30–50 gsm**（另处 50–140 gsm）；面层 **min 10 gsm** | 同上 |
| 在线粘扣（hook）成形 | 超声波局部熔融 + 砧面孔型决定钩型 | 同上 |
| 无胶三层复合（IN-LINE-FLS） | 无纺布 + 弹性膜 + 无纺布，超声波，**已量产** | 同上 |

> ⚠️ **No unsourced parameters 禁止无来源参数**：全部来自 Fameccanica 单方披露（credibility 中）。

## Adjacent Concepts 相邻概念

- 对照路线：[[Ultra-Low Add-On Adhesive Application（超低添加量施胶）]]、[[Polyolefin Hot Melt Adhesive（聚烯烃热熔胶）]]
- 工艺基础：[[Pressure vs Thermal vs Ultrasonic Bonding（压力·热·超声波粘合对比）]]、[[Ultrasonic Bonding of PET-Containing Topsheet]]
- 应用对象：[[ADL（导流层）]]、[[SMS复合结构]]、[[Elastic Strand Snicking（弹性橡筋断丝失效化）]]
- 设备方：[[Fameccanica（Angelini Technologies）]]
- OI 关联：[[IPC BCC OI Portfolio（开放创新项目组合）]]（"超声波升为降本主线"路线级方向）

## 经验教训

- **Lesson（可焊性是材料体系属性，不是工艺参数）**：能否去胶**在选材阶段就决定了**——面层与 ADL 若不同聚合物体系，超声波焊接无从谈起。因此"去胶化"必须**前移到材料规格**，而不是留给工艺调试。
- **Lesson（去胶把风险从"胶"转移到"过程控制"）**：胶原本同时承担固定与容错；去胶后断丝不再被粘住，故必须补**视觉检测**。这是"降本项自带新增成本项"的典型例子。
- **待补 `[待验证]`**：热封 vs 超声波的剥离强度与老化对比；PP/PE 双组分热风材料的可焊窗口（温度/压力/时间）；与 [[Elastic Tension & Creep（橡筋张力与回缩率）]] 的交互。

## 来源

- [[Fameccanica Innovations 2026（婴儿·巾·成人护理技术与创新总览）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/Innovation 2026 - Overall_with Detials.pptx.md`

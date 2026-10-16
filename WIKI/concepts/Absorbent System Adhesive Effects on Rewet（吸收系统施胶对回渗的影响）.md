---
type: concept
title: "Absorbent System Adhesive Effects on Rewet（吸收系统施胶对回渗的影响）"
domain: [卫材研发, 芯体与吸收]
status: growing
updated: 2026-09-30
tags: [施胶, 热熔胶, 回渗, LTD, PAA, SLA, 亲水胶, 覆盖率]
---

# Absorbent System Adhesive Effects on Rewet（吸收系统施胶对回渗的影响）

> 一句话定义 One-line definition：吸收系统内三处施胶——**LTD（面层固定胶）**、**PAA（吸收体附着胶）**、**SLA（导流层胶）**——通过**施胶量、花型/喷头、覆盖面积与胶的亲水性**四个变量影响回渗；其中**"少胶"与"非亲水胶"是两个独立且方向一致的有利变量**。

## 机理 / 结构拆解 Mechanism and Structure

1. **LTD 施胶量（唯一统计显著的杠杆）**：**降低 LTD add-on 降低回渗**，假设是 **LTD 胶阻碍了液体向下层流动**（即胶本身成了"拦水坝"）。这是三处施胶中**唯一取得统计显著改善**的改动。
2. **亲水胶的反直觉效应**：在 **LTD、PAA、SLA 三处**试用的亲水胶**均方向性乃至统计显著地增加回渗**——三处结论一致，是本批最稳健的一条负面知识（negative knowledge）。直觉上"亲水胶帮助导水"，实测相反。
3. **PAA 花型/位置**：**去掉 pad 中央 50 mm 条带的 PAA** 方向性降低回渗——与 LTD 同源：**减少液体通路上的胶量是有利的**。
4. **SLA 喷头与覆盖面积**：**Signature 喷头（随机纤维）相对 Summit（漩涡）方向性降低回渗**，给出的机理是 **Signature 的表面覆盖面积更高**。注意这与 HSBL 附着强度结果中"Signature 44.119 vs Summit 24.097"的排序**同向**（Signature 剥离强度更高 = 界面间隙更小）。
5. **分区/TRIO 施加的资本教训**：理论上最优，但**测试中并不总是带来回渗改善，因此资本开支未被证明合理**——即"理论最优 ≠ 可复现改善"，投资决策须以测试稳定性为准。

## 关键参数表 Key Parameters

| 参数 Parameter | 典型值 / 范围 Typical Value | 出处 Source |
|---|---|---|
| 三处施胶 | **LTD**（liner tack down）/ **PAA**（pad attachment）/ **SLA**（surge adhesive） | [[GRIFFIN Learning Cycle Check In（GRIFFIN 学习周期复盘 · 2025-06-25）]] |
| **LTD 施胶量效应** | **降低 add-on → 回渗降低（唯一统计显著）** | 同上 |
| **亲水胶效应（三处）** | **方向性至统计显著增加回渗**（LTD / PAA / SLA 一致） | 同上 |
| PAA 位置变量 | 去掉中央 **50 mm** 条带 → 方向性降低回渗 | 同上 |
| SLA 喷头对比 | **Signature（随机纤维、覆盖面积更大）** vs 对照 **Summit（漩涡）** → 方向性降低回渗 | 同上 |
| 喷头与剥离强度（旁证） | Signature **44.119** vs Summit **24.097**（LS Means） | [[HSBL Attachment Strength Results（HSBL 附着强度结果 · 2025-11-18）]] |
| 分区/TRIO 施加 | 理论最优但**未稳定改善** → 资本开支未获授权 | [[GRIFFIN Learning Cycle Check In（GRIFFIN 学习周期复盘 · 2025-06-25）]] |

> ⚠️ **禁止无来源参数 No unsourced numbers**：表中数字均来自上列源摘要页；各胶型的具体 add-on（gsm）最优值、以及亲水胶增加回渗的定量幅度，库内暂无来源，标 `[待验证]`。

## 相邻概念 Adjacent Concepts

- 上位：[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]、[[Intake System（摄入系统）]]
- 胶黏剂：[[Polyolefin Hot Melt Adhesive（聚烯烃热熔胶）]]、[[Styrenic Block Copolymer Hot Melt（SIS-SBS 苯乙烯嵌段共聚物热熔胶）]]、[[APAO（非晶态聚α-烯烃）]]、[[Hydrophilic SAP Wrapping Adhesive（亲水SAP包裹胶）]]
- 施胶工艺：[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]、[[Hot-Melt Slot Coating（热熔狭缝涂布）]]、[[Ultra-Low Add-On Adhesive Application（超低添加量施胶）]]、[[Liner-Surge Interstitial Space（面层-导流层界面间隙）]]
- 项目：[[GRIFFIN Rewet Program（GRIFFIN 超低回渗项目）]]、[[IPC BCC OI Portfolio（开放创新项目组合）]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[GRIFFIN Learning Cycle Check In（GRIFFIN 学习周期复盘 · 2025-06-25）]]）：本页结论在**三处独立施胶位置（LTD/PAA/SLA）上一致复现**（亲水胶增加回渗），属**多位置互证**；"降低 LTD add-on"为三处中唯一的统计显著改善。

- **教训一（把亲水胶列为红线）**：三处一致的反直觉结果足以把"吸收系统内不使用亲水胶"作为**默认约束**，而不是每次重新论证。
- **教训二（胶是拦水坝，不是导水管）**：LTD 与 PAA 两条证据同源——**通路上的胶越少越好**；这与"多上胶以固定的更牢"的装配直觉冲突。
- **教训三（理论最优要过稳定性关）**：分区/TRIO 施加理论上最优但未稳定改善，故资本未被授权；**投资决策的门槛是"可复现"，不是"理论更优"**。
- **教训四（喷头排名跨文档同向）**：Signature 在回渗（本页）与剥离强度（HSBL）两个独立指标上都优于 Summit，两条证据互为旁证——但仍需注意 HSBL 曾提示 Summit 偏低**可能源于花型质量异常**。
- **待补 `[待验证]`**：各位置 add-on 的最优值与下限（降低到多少会危害结构完整性与渗漏）；亲水胶增加回渗的定量幅度与机理（是滞留还是改变接触角）。

## 来源 Sources

- [[GRIFFIN Learning Cycle Check In（GRIFFIN 学习周期复盘 · 2025-06-25）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.06.25 - Learning Cycle Check In.pptx.md`
- [[HSBL Attachment Strength Results（HSBL 附着强度结果 · 2025-11-18）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/Surge-Liner Interface/Test Results/HSBL Attachment Strength Results.pptx.md`（喷头排序旁证）

## Related Sources 关联来源

- [[GRIFFIN Learning Cycle Check In（GRIFFIN 学习周期复盘 · 2025-06-25）]]

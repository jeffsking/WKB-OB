---
type: concept
title: "Elastic Strand Snicking（弹性橡筋断丝失效化）"
domain: [卫材研发, 芯体与吸收]
status: growing
updated: 2026-09-30
tags: [橡筋, 弹性件, 断丝, snicking, 非弹性区, 加压加热, idle elastic]
aliases: ["Snicking", "弹性橡筋断丝失效化", "idle elastic members"]
---

# Elastic Strand Snicking（弹性橡筋断丝失效化）

> One-line definition 一句话定义：在裤型纸尿裤外装中，把**横跨吸收体区域的弹性橡筋局部切断（snicking）**，使其在**非弹性区**内不再产生收缩力，从而避免吸收体被横向收缩、起皱或开裂；被切断后失去张力的橡筋段称为**失效橡筋（idle elastic members）**。

## Definition / Mechanism 定义与机理拆解

1. **为什么必须断丝**：吸收体（含 SAP + 绒毛浆）有一定刚度，弹性件若持续横跨吸收体收缩，会**限制其延伸**，导致腰围贴合不良、外观不佳，或使吸收体**起皱、开裂而降低吸收能力**。
2. **断丝不是"抽掉橡筋"，而是"留下失效段"**：被切断后橡筋分为两类——自弹性区延续过来的**残余段**与与弹性区脱开的**切断碎段**；两者共同构成失效橡筋，定义非弹性区。
3. **切断方式（不开孔口径）**：来源强调切断应采用**不在内外片层上形成孔洞**的工艺；示例是**在橡筋内外两面所对应的切断位置加压 + 加热**（即夹住内片层内面与外片层外面、对夹层施压加热）。
4. **切断力学的关键约束——厚度一致性**：压力直接作用于层叠体；**某处少一层（如缺图形片）会降低该处实际压力 → 橡筋切不断**。因此切断位置应设在**层厚一致的无夹层区**（见 [[Graphic Sheet in Non-Stretch Zone（非弹性区图形片）]]）。
5. **切断痕的意义**：切断痕（cut marks）本身是**可检出的结构特征**；专利把它作为权利要求的限定要素（图形片覆盖区无痕、无夹层区有痕）。同时，前后外装分离式结构中应在**失效橡筋的裆侧设焊接部**，否则层间开口外露、失效橡筋可能**凸出或掉出**。
6. **横向切断的两种做法（背景技术）**：一是大部分压在吸收体上的弹性件近乎全部"snicked"（失效化）；二是不固定于外装、并在宽度方向某一中间位切断。

## Key parameters 关键参数表

| Parameter 参数 | Typical value / range 典型值 / 范围 | Source 出处 |
|---|---|---|
| 切断对象 | 在外装宽度方向横跨、沿前后方向间隔排布的细长弹性件 | [[US11071659B2 Underpants-Type Disposable Diaper with Graphic Sheet (Daio Paper)]] |
| 切断方式 | 夹住内片层内面 + 外片层外面，加压 + 加热；不开孔 | 同上 |
| 失效橡筋构成 | 自弹性区延续的残余段（residual portion）+ 与弹性区脱开的切断碎段（cut fragment） | 同上（权利要求 1） |
| 切断痕连续性（优选） | 沿前后方向**至少从最靠近腰口的橡筋切断位**连续到**最靠近裆部的橡筋切断位** | 同上（权利要求 2） |
| 焊接部位置（优选） | 失效橡筋的**裆侧**；优选由一处切断痕经裆侧连续 **U 形**焊至另一处 | 同上（权利要求 3–4） |
| 固定用胶（分支方案） | 切前先用**防偏移热熔胶**把橡筋固定在含切断位置的区域，再在胶带宽度方向中间位切断，令橡筋凭自身收缩力对抗胶力回缩 | 同上（权利要求 8） |
| 施加方向 | 前后方向连续线状图样（前后方向覆盖腰口侧→裆侧切断位） | 同上（权利要求 7、9） |
| 弹性件固定原则 | 弹性区至少两端边缘部固定于内外片层；非弹性区**不固定** | 同上（权利要求 1） |

> ⚠️ **禁止无来源参数**：本页口径来自 [[US11071659B2 Underpants-Type Disposable Diaper with Graphic Sheet (Daio Paper)]]。**来源未给出断丝温度、压力、时间、切断痕宽度或橡筋规格（dtex 等）**，标 `[待验证]`。

## Adjacent concepts 相邻概念

- 配套机理：[[Graphic Sheet in Non-Stretch Zone（非弹性区图形片）]]
- 相邻结构：[[Co-extruded Elastic Film Feature（共挤弹性膜弹性部件）]]、[[Waist Guard（腰围护挡）]]、[[REL增强层]]
- 材料：[[Polyolefin Hot Melt Adhesive（聚烯烃热熔胶）]]（弹性粘合胶）、[[并列复合自卷曲纤维]]
- 权利人：[[Daio Paper Corporation（大王製紙）]]、[[The Procter & Gamble Company（宝洁）]]

## 经验教训

> ✅ 验证（2026-09-29，来源 [[US11071659B2 Underpants-Type Disposable Diaper with Graphic Sheet (Daio Paper)]]）：本页关键机理——"**切断工位的实际压力取决于该处层叠厚度**"——由专利背景技术明确给出，并解释了既有工艺"提高压力会压伤片材"的两难。这是本库首次把**层叠厚度 → 压力 → 切断有效性**这一链条写清。

- **教训一（工艺排查顺序）**：出现"部分橡筋没断"时，先查**该位置的层叠结构是否少/多了一层**，而不是先调压力。
- **教训二（外观与掉落）**：前后外装分离结构下，断丝后须在**裆侧补焊接部**，否则失效橡筋会从层间开口**凸出或掉出**。
- **待补 `[待验证]`**：断丝工艺参数（温度/压力/时间）、橡筋规格与 dtex、失效橡筋段长度对腰围力的影响。

## Sources 来源

- [[US11071659B2 Underpants-Type Disposable Diaper with Graphic Sheet (Daio Paper)]] —— `RAW/ima_sync/个人知识库/WKB/Areas/IP/四-3_Underpants-style_disposable_diaper_and_manufacturing_method_therefor.pdf.md`

> 🔴 **manual_review（2026-09-29）**：本页为**专利技术方案的客观摘录**，不构成侵权或 FTO 判断；实施前须比对权利要求原文并由专利代理/法务独立评估。

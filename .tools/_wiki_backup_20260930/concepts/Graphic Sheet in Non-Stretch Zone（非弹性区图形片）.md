---
type: concept
title: "Graphic Sheet in Non-Stretch Zone（非弹性区图形片）"
domain: [卫材研发, 结构设计]
status: seed
updated: 2026-09-29
tags: [图形片, graphic sheet, 非弹性区, 裤型纸尿裤, 外装, 印刷]
aliases: ["Graphic Sheet", "非弹性区图形片"]
---

# Graphic Sheet in Non-Stretch Zone（非弹性区图形片）

> One-line definition 一句话定义：在裤型纸尿裤外装的**非弹性区（non-stretchable region）**内、夹在内外片层之间、透过外层可见的**印刷图形片**；利用非弹性区不产生收缩皱褶这一特性，使印刷图案清晰可视。

## Definition / Mechanism 定义与机理拆解

1. **为什么要把图形放在非弹性区**：外装若全为弹性区，收缩皱褶会使印刷图案失真、模糊；非弹性区因弹性件不产生收缩力、几乎无收缩皱褶，**透光率高**，因此适合放图形片。
2. **图形的可视路径**：图形片置于**内外片层之间**、透过外层面材观察——所以必须考虑面材的光学透过率与图形件的层间位置。
3. **图形片与弹性件的相处原则**：因两者相邻，来源指出弹性件**不应固定**到图形片、或只做**弱固定**（易脱开），以彻底消除弹性件收缩力对图形片的影响。
4. **带来的制造难题（本库关键机理）**：若把图形片与待切断弹性件同置于内外片层之间，则在**图形片不覆盖的区段**，受压力的层厚度少了图形片那一层 → 实际压力偏小 → 该处弹性件**切不断**（见 [[Elastic Strand Snicking（弹性橡筋断丝失效化）]]）。
5. **解法是几何分离**：另设**无夹层区（no-extra-sheet region）**——该区内外片层之间**不夹任何其他片材**——把切断工位移到无夹层区，使**图形片覆盖区无切断痕**、无夹层区带切断痕。加压厚度在前后方向因此一致。
6. **不可用"加压"硬解**：来源明确提高切断压力**不可取**，因为会**部分切伤片层并留下明显切断痕**。

## Key parameters 关键参数表

| Parameter 参数 | Typical value / range 典型值 / 范围 | Source 出处 |
|---|---|---|
| 图形片位置 | 置于内外片层之间，非弹性区内，透过外层面可见 | [[US11071659B2 Underpants-Type Disposable Diaper with Graphic Sheet (Daio Paper)]] |
| 非弹性区构成 | 内外片层（自弹性区延续）+ 图形片 + **失效橡筋**（残余段与/或切断碎段） | 同上（权利要求 1） |
| 无夹层区定义 | 自图形片一侧沿宽度方向向外延伸、内外片层之间**不含其他片材** | 同上（权利要求 1） |
| 切断痕分布限定 | 图形片覆盖区**无切断痕**；无夹层区**有切断痕** | 同上（权利要求 1） |
| 优选布置 | 图形片宽度方向两侧各一个无夹层区；失效橡筋裆侧设内外片层焊接部；优选由一处切断痕经裆侧**连续 U 形焊**至另一处 | 同上（权利要求 3–4） |
| 图形片与弹性件关系 | 不固定或仅弱固定（易脱开） | 同上（背景技术） |
| 图形片厚度带来的压力损失 | 未给定量值；来源仅作机理性描述（"thickness of the layers to receive the pressure is smaller by the thickness of the graphic sheet"） | 同上 |

> ⚠️ **禁止无来源参数**：本页数字/口径来自 [[US11071659B2 Underpants-Type Disposable Diaper with Graphic Sheet (Daio Paper)]]。**来源未给出图形片的克重、厚度、材质或印刷工艺参数**，标 `[待验证]`。

## Adjacent concepts 相邻概念

- 配套机理：[[Elastic Strand Snicking（弹性橡筋断丝失效化）]]
- 同族视觉设计：[[Informational Image on Pull-On Article（可穿脱制品信息图形）]]、[[Geometric Optical Mask（几何光学掩膜）]]、[[Wetness Indicator Ladder（尿湿指示阶梯）]]
- 结构语境：[[分区密度设计]]、[[芯体通道花型设计]]、[[REL增强层]]
- 权利人：[[Daio Paper Corporation（大王製紙）]]
- 对比/相邻专利：[[US10905605B2 Pull-On Wearable Article with Informational Image (P&G)]]

## 经验教训

> ✅ 验证（2026-09-29，来源 [[US11071659B2 Underpants-Type Disposable Diaper with Graphic Sheet (Daio Paper)]]）：本页把"图形片"从**印刷/视觉**议题延伸到**工艺压力**议题——同一张图形片同时决定了图案清晰度与切断工位的压力分布。这修正了"图形片只是装饰件"的简化认知。

- **教训一（工艺耦合）**：任何"在内外片层之间增加一片材"的设计，都会改变**热压/超声切断工位的实际压力**，必须复核该工位的切断有效性。
- **教训二（不可硬加压）**：切不断时的第一反应不应是提高压力（会压伤片材、留下压痕），而是**把切断点移到无夹层区**。
- **待补 `[待验证]`**：图形片的克重/厚度/材质；面材透光率要求；该结构在高速线上的实际节拍影响。

## Sources 来源

- [[US11071659B2 Underpants-Type Disposable Diaper with Graphic Sheet (Daio Paper)]] —— `RAW/ima_sync/个人知识库/WKB/Areas/IP/四-3_Underpants-style_disposable_diaper_and_manufacturing_method_therefor.pdf.md`

> 🔴 **manual_review（2026-09-29）**：本页为**专利技术方案的客观摘录**，不构成侵权或 FTO 判断；实施前须比对权利要求原文并由专利代理/法务独立评估。

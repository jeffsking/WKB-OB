---
type: concept
title: "柔性电子 Flexible Electronics"
domain: [卫材研发, 变色与智能材料]
status: growing
updated: 2026-09-30
tags: [flexible-electronics, stretchable-electronics, UTCP, imec, wearable, smart-textiles]
---

# 柔性电子 Flexible Electronics

> 📌 **Page completed 2026-09-30** from 11 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）。

The vault carries **no standalone definition sentence**. The nearest framing is **contrastive**: conventional electronics are *"packaged components assembled on flat, rigid printed circuit boards"*, while demand is growing for **2.5D（free-form surface）and full 3D circuits**（源：[[Flexible and Stretchable Electronics]]）. In the wearables landscape, **flexible electronics is a named function family** alongside stimuli-responsive polymers, wearable sensing/electronics, e-textiles, chromic / PCM / shape-memory functions and thermoelectric harvesting（源：[[Smart Textiles & Wearables]]、[[热电现象 Thermoelectric]]）.

（中文：库内无独立定义句；最近的口径是"相对刚硬 PCB 而言的 2.5D/3D 电路需求"，并在智能纺织品框架中作为一个功能族登记。）

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| UTCP bare-die thinning（裸片减薄） | **20–30 μm** Si / inorganic-semiconductor | [[Flexible and Stretchable Electronics]] |
| UTCP total package thickness（封装总厚） | **< 100 μm** | [[Flexible and Stretchable Electronics]] |
| UTCP construction（构造） | spin-on polyimide stack + fan-out metallisation | [[Flexible and Stretchable Electronics]] |
| Stretchable-circuit elastic embedment（弹性埋置） | PDMS (silicone rubber) or PU (polyurethane) | [[Flexible and Stretchable Electronics]] |
| Stretchable interconnect geometry（互连几何） | meander-shaped thin-film or PCB-based metal wiring | [[Flexible and Stretchable Electronics]] |
| Demonstration circuit | **15-LED** stretchable circuit, photographed before / during extreme deformation | [[Flexible and Stretchable Electronics]] |
| Metal yield strain（金属屈服应变，路线 D 口径） | **Cu ≈ 0.2–0.5%** — serpentine geometry absorbs macro-strain to protect the interconnect | [[Elastic Tension Visualization Technology Assessment（拉力松紧可视化技术评估）]] |
| Wearable-electronics two directions | thin film（reduce one dimension）+ fibre（reduce two dimensions） | [[Wearable Electronics (National Science Review 2023)]] |
| Fibre-form launder durability | **washable hundreds of times** | [[Wearable Electronics (National Science Review 2023)]] |

⚠️ **Source-thinness caveat**：the vault's root file for the imec contribution is **a single abstract page（~1.9 KB）**; the announced **process-flow, reliability data and applications are not in the file**（源：[[Flexible and Stretchable Electronics]]）. Do not treat the table above as a full process spec.

## Method / Mechanism 方法 / 机理

1. **Route 1 — UTCP（超薄芯片封装）addresses the *rigid component*.** Bare Si or other inorganic-semiconductor chips are thinned to 20–30 μm, embedded in a stack of spin-on polyimide layers and given fan-out metallisation, yielding a flexible package below 100 μm total（源：[[Flexible and Stretchable Electronics]]）.
2. **Route 2 — meander interconnect + elastic embedment addresses the *interconnect and substrate*.** Component islands are wired with meander-shaped thin-film or PCB-based metal wiring and embedded in PDMS or PU; the serpentine geometry accommodates elastic strain so the metal stays under its yield strain（源：[[Flexible and Stretchable Electronics]]、[[Elastic Tension Visualization Technology Assessment（拉力松紧可视化技术评估）]]）.
3. **Value proposition is manufacturability, not a lab demo**：the stated industrial target is *"randomly deformable circuits produced by industrial methods"*（源：[[Flexible and Stretchable Electronics]]）.
4. **Application drivers named**: comfort & ergonomics（wearable / implantable circuits）、design & aesthetics（2.5D/3D light sources）、ecology（more efficient materials use, lower CO₂ in automotive）（源：[[Flexible and Stretchable Electronics]]）.
5. **Fibre-level integration is the competing philosophy**：rather than bolting electronics onto cloth, make the fibre itself the device — the honest negative result recorded is that as-prepared **CNT fibres fail on softness and processability**, marking a CNT route as premature for a disposable（源：[[Smart Fabrics and Networked Clothing]]）.
6. **End-state framing**：表皮级柔性电子（epidermal flexible electronics, John A. Rogers）is recorded as **the ultimate form of wearable electronics**（源：[[Wearable Electronics (National Science Review 2023)]]）.

## Hygiene Relevance 卫材关联

- **No hygiene-product flexible-electronics implementation is evidenced** in the digest — only adjacency（源：[[可穿戴传感器 Wearable Sensor]]、[[电子纺织品 E-textile]]）.
- **One vault source does land the technology in a diaper scenario**: [[Smart Sensing Diaper Technology Research Report（智能感知纸尿裤技术研究报告 · 2026-04）]] is named as the only vault material that genuinely applies flexible / wearable electronics to a diaper（源：[[Flexible and Stretchable Electronics]]）.
- **Cost model conflict（决定性的商业化短板）**：route D（柔性电子传感）的 **cost far exceeds the single-use hygiene per-piece model**; plus battery and skin-contact safety / recycling questions — usable **only for a premium line or a reusable product**（源：[[Elastic Tension Visualization Technology Assessment（拉力松紧可视化技术评估）]]）.
- **Structural obstacle**：recyclability / e-waste conflicts with single-use hygiene and is **flagged but unresolved**（源：[[可穿戴传感器 Wearable Sensor]]）.
- **Elastic-part material adjacency**：PDMS/PU embedding meets the vault's [[聚氨酯 Polyurethane]] elastic-part page, i.e. the same polymer family used for elastic waist / leak-guard cuffs（源：[[聚氨酯 Polyurethane]]）.
- **Structural-colour / mechanochromic adjacency**：the vault treats flexible electronics as a sibling route to its chromic programme in the same smart-textiles frame（源：[[Smart Textiles & Wearables]]、[[结构色 Structural Color]]）.

## Open Questions 待补

- **No hygiene-grade sensor spec**（sensitivity, drift, lifetime）exists in the digest — the wearable-electronics market and hardware figures are field-level（源：[[可穿戴传感器 Wearable Sensor]]）.
- **UTCP process flow and reliability data are missing** from the vault file（only the abstract survived）（源：[[Flexible and Stretchable Electronics]]）.
- **Freedom-to-operate is not assessed** for the cited sensor patents `[待补]`.
- Whether a flexible-electronic route can be costed **inside a disposable** at all — the source answers only "premium/reusable"（源：[[Elastic Tension Visualization Technology Assessment（拉力松紧可视化技术评估）]]）.

## Related Sources 关联来源

- [[Flexible and Stretchable Electronics]]（Cited-by 来源；imec/Vanfleteren 摘要）
- [[Wearable Electronics (National Science Review 2023)]]（本页原始 Cited-by 来源）
- [[可穿戴传感器 Wearable Sensor]] · [[电子纺织品 E-textile]] · [[智能织物 Smart Textile]] · [[Smart Textiles & Wearables]]
- [[Flexible Stretchable Electronics (imec)]] · [[热电现象 Thermoelectric]] · [[Smart Fabrics and Networked Clothing]] · [[Intelligent Textiles and Sports Clothing]]
- [[Elastic Tension Visualization Technology Assessment（拉力松紧可视化技术评估）]] · [[Smart Sensing Diaper Technology Research Report（智能感知纸尿裤技术研究报告 · 2026-04）]]
- [[聚氨酯 Polyurethane]] · [[结构色 Structural Color]] · [[Interactively Mechanochromic Electronic Textile Sensor]]

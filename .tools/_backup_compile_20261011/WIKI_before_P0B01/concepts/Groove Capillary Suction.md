---
type: concept
title: "Groove Capillary Suction"
domain: [卫材研发, 导流机理]
status: growing
updated: 2026-09-29
tags: [毛细, 沟槽, 异形截面, 导流, 面层, Liner]
aliases: ["Groove Capillary Suction 沟槽毛细吸力"]
---

# Groove Capillary Suction 沟槽毛细吸力

> **Definition 定义**：The capillary pressure generated inside an **axial surface groove** of a profiled fibre — a channel whose hydraulic radius is one to two orders of magnitude smaller than an inter-fibre pore, hence whose suction is correspondingly larger.（异形截面纤维**轴向表面沟槽**内产生的毛细压力；其水力半径比纤维间孔隙小 1–2 个数量级，因此吸力相应更大。）

## Mechanism 机理

1. **Two capillary paths in parallel（两条并联毛细路径）**：`Δp = 2γcosθ / r`。For a 3.3 dtex trilobal, `r_groove ≈ 2–3 µm`; for the inter-fibre pore network, `r ≈ 40–80 µm`. With a wetting finish (`θ → 20°`) and `γ ≈ 66 mN/m`, groove suction lands near **40–50 kPa** versus roughly **1–2 kPa** in the pore network.（3.3 dtex 三叶形 r_沟槽 ≈2–3 µm，纤维间孔径 40–80 µm；θ→20°、γ≈66 mN/m 时沟槽吸力约 40–50 kPa，孔隙网络仅约 1–2 kPa。）
2. **Why the slow path wins late（慢路径为何在后段胜出）**：`L(t) = √(γ·r·cosθ·t / 2µ)` — big pores move the wicking front fast but cannot hold it (they drain to the core first); grooves start slower and then carry the front on alone. That late-stage tail is exactly the MD length being bought.（大孔推动前沿快但握不住——先排入芯体；沟槽起步慢，随后独自承接前沿。这段"后段尾巴"正是所要购买的 MD 长度。）
3. **Where the gain comes from（收益拆解）**：In the 45 gsm Option B build, roughly **two-thirds** of the modelled MD gain comes from the groove network itself and **one-third** from raising MD fibre orientation on card 2.（45 gsm Option B 构造中，模拟 MD 收益约三分之二来自沟槽网络本身，三分之一来自第二梳理的 MD 取向提升。）
4. **Strike-through is not set by cross-section（穿透时间不由截面决定）**：First-insult acquisition is governed by pore size, so groove suction leaves first strike-through essentially unchanged — the benefit shows up in late-stage spreading.（首次摄入由孔径决定，因此沟槽吸力基本不改变首次穿透时间，收益体现在后段铺展。）

## The counter-risk 反向风险

> ⚠️ **High-suction grooves can hold fluid you wanted in the core.** 高吸力沟槽可能截留本该进入芯体的液体。

A groove network at 40–50 kPa suction is a genuine reservoir. If it out-competes the layer beneath, fluid stays in the liner and returns under load as rewet. **More profiled fibre is not monotonically better.** The safety margin comes from the swollen SAP core, whose suction is well above the groove range — but that margin **narrows as the core approaches saturation**, which is exactly the third-insult condition to test.
40–50 kPa 的沟槽网络是一个真实的储液体。若其吸力压过下层，液体驻留于面层并在受压时以回渗形式返回。**异形纤维并非越多越好。** 安全余量来自已膨胀的 SAP 芯体（吸力远高于沟槽区间），但该余量**随芯体接近饱和而收窄**——这正是第三次冲击须验证的工况。

## Key parameter table 关键参数表

| Parameter 参数 | Value 典型值 | Source 出处 |
|---|---|---|
| Groove radius 沟槽半径 | ≈2–3 µm (3.3 dtex trilobal) | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Inter-fibre pore radius 纤维间孔径 | 40–80 µm | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Groove suction 沟槽吸力 | ≈40–50 kPa (θ→20°, γ≈66 mN/m) | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Pore-network suction 孔隙网络吸力 | ≈1–2 kPa | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Groove-to-pore suction ratio 吸力倍数 | 10–30× | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Surface area gain 表面积增益 | ≈300% of a round fibre at equal denier | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Published wicking rank 已发表芯吸排序 | 4DG > trilobal > round | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Section geometry 截面几何 | Groove radius sets the suction — specify the **lobe profile**, not just "trilobal" | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Durability condition 耐久条件 | Groove suction is worthless once θ climbs back above 60° on insults 2–3 | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Shape factor (star) 星形形状因子 | +25–35% effective surface vs round PET at equal denier | [[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]] |
| Capillary edge logic 毛细边缘逻辑 | Open grooves add continuous lanes; rounded profiles create repeatable channels without sharp stress points | [[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]] |

> ⚠️ **No unsourced parameters 禁止无来源参数**：上表均来自本批 Liner 源摘要页；库内无「沟槽几何参数（叶长比、沟深、圆角半径）↔ 实测吸力」的定量函数，标 `[待验证]`。

## Adjacent concepts 相邻概念

- Carrier fibres 载体纤维：[[三叶形截面纤维（Trilobal Fibre）]]、[[Pentagram PET (Star Cross-Section Fibre)]]、[[原纤化]]
- Application 应用：[[ATB双梳理面层（Dual-Card Topsheet）]]、[[MD Liquid Distribution]]
- Sibling mechanism 同族机理：[[毛细梯度设计]]、[[分区密度设计]]
- Durability coupling 耐久耦合：[[亲水整理耐久性]]

## Lessons learned 经验教训

> ✅ **Validation（2026-09-29）**：本批三份来源在"沟槽/异形截面提供轴向毛细通道"这一机理上互证（[[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] 给出定量吸力，[[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]] 与 [[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]] 给出定性机理与排序）。同时三份来源一致强调：**截面形状只是改性项，网面取向与亲水整理仍主导最终 MD/CD 铺展**。

- **教训一（评估口径）**：沟槽吸力的收益是**方向性的**——必须用 MD 铺展类指标衡量，用各向同性指标会系统性低估。
- **教训二（反向风险）**：吸力越强越需要同时检查**回渗与第三次冲击**；沟槽网络在芯体接近饱和时会转为"抢液方"。
- **待补 `[待验证]`**：沟槽几何参数与吸力的实测标定曲线；商业级纤维的沟槽半径批次一致性。

## Sources 来源

- [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/Trilobal_PET_Liner_MD_Distribution.pptx.md`
- [[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/pentagram_PET_diaper_liner_deep_dive 1.pptx.md`
- [[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/pentagram_free_shaped_PET_alternatives_8slides.pptx.md`

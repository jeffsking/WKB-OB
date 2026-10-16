---
type: concept
title: "Specific Air Volume"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [nonwoven, porosity, absorbent-core, capacity-parameter, specific-air-volume, packing-fraction]
---

# Specific Air Volume

> 📌 **Page completed 2026-09-30** from 5 citing sources in the vault. All figures traced to their source pages. Anything not evidenced in the vault is marked `[待补]`.

## Definition 定义

**Specific air volume（比空气体积，V_s）** is the air/void volume per unit mass of an open fibrous web — i.e. the mass-basis capacity parameter of a nonwoven. In *Absorbent Technology* Ch.1 it is defined by the relation `V_s = (1/φ)(1/ρ_f − 1)`, where **φ = fibre packing fraction** and **ρ_f = fibre density**（源：[[Porous Structure and Liquid Flow Models]]）. The same relation is carried in the chapter's own extraction as "specific air volume Vs = (1/φ)(1/ρ_f − 1)"（源：[[Porous Structure and Liquid Flow Models]]）. The chapter calls it "the single most useful relation … for areal-density-based design" and states it lets **REL teams predict capacity from fibre density and packing fraction before any prototype is spun**（源：[[Porous Structure and Liquid Flow Models]]）.

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Specific air volume 比空气体积 | `V_s = (1/φ)(1/ρ_f − 1)`（Eq. 46, p. 54） | [[Porous Structure and Liquid Flow Models]] |
| Packing fraction φ 纤维堆积分数 | 0.025–0.10（2.5%–10%），Gupta 实测；随材料/克重/粘合法变化 | [[Porous Structure and Liquid Flow Models]] |
| Fibre density ρ_f, cellulose 纤维素 | ~1.5 g/cc（较低 ρ → 较高 V_s） | [[Porous Structure and Liquid Flow Models]] |
| Fibre density ρ_f, polyolefin 聚烯烃 | ~0.92 g/cc（ρ 更低，但润湿性差，毛细压力几乎不启动） | [[Porous Structure and Liquid Flow Models]] |
| Porosity from density 由密度算孔隙率 | `Φ = 1 − ρ_bulk/ρ`（Eq. 9, p. 30） | [[Porous Structure and Liquid Flow Models]] |
| Max absorption capacity 最大吸液容量 | `C = ρ_L·Φ / [ρ(1−Φ)]`（Eq. 10, p. 30） | [[Porous Structure and Liquid Flow Models]] |
| Denier → V_s 旦数与比空气体积 | 线性密度越低 → 比空气体积越高、毛细性越强（代价：可加工性与价格） | [[Fibers and Fibrous Materials]] |
| Capacity vs areal density 容量-面密度 | C 由 T/W 预测；40→160 g/m² 使 C −34%、Q −54% | [[Fluid Absorption in High Bulk Nonwovens]] |

## Method / Mechanism 方法 / 机理

- **Two terms set V_s: packing fraction and fibre density.** Lower-density fibre gives more void per gram at equal areal density — **but only if wettability is comparable**; polyolefin's 0.92 g/cc is "a trap without a hydrophilic surface"（源：[[Porous Structure and Liquid Flow Models]]）.
- **Rate and capacity are antagonists, both geometric.** Pore **size** sets rate (Hagen–Poiseuille: flow ∝ r²); pore **volume** — hence V_s — sets capacity（源：[[Porous Structure and Liquid Flow Models]]）.
- **The denier lever.** "Denier is the bulk dial": lowering linear density raises specific air volume **and** capillarity at the same time, at the cost of processing difficulty and price — a three-axis trade for core spec（源：[[Fibers and Fibrous Materials]]）.
- **Binder is a capacity tax.** Binder volume is subtracted directly from pore volume, so glue loading must be co-designed against capacity（源：[[Porous Structure and Liquid Flow Models]]）.
- **Stated material frontier:** the chapter closes on the challenge of *"materials that have the densities of polyolefins but the hydrophilicities of celluloses"*（p. 53）（源：[[Porous Structure and Liquid Flow Models]]）.

## Hygiene Relevance 卫材关联

- **REL / absorbent-core pre-design.** V_s is the mass-basis capacity predictor used before prototyping: pick fibre density and packing fraction to reach the required void volume per gram（源：[[Porous Structure and Liquid Flow Models]]）.
- **REL void-volume target.** The REL enhancement-layer project states a **void-volume target of 80–117 cm³/g @ 0.5 kPa** (OI-02 aims at 108–117 cm³/g), i.e. a per-mass void-volume figure on the same conceptual basis as V_s（源：[[REL增强层]]）.
- **Bulk is a performance argument, not comfort.** Thinning the core (40 → 160 g/m²) costs 34% capacity and 54% rate — so areal density / bulk is the design variable to lock in early（源：[[Fluid Absorption in High Bulk Nonwovens]]）.

## Open Questions 待补

- **Terminology — is "specific air volume" identical to the vault's "void volume"?** The two are used on a per-mass (cm³/g) basis in adjacent pages, but no source read here states they are the same quantity; keep them distinct until a source defines the equivalence（相关页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]、[[REL增强层]]）`[待补]`.
- No source read here gives an absolute measured **V_s value (cm³/g)** for a KC core or a named commercial nonwoven `[待补]`.
- The packing-fraction range 0.025–0.10 is quoted for webs generally (Gupta); no paper/nonwoven-specific φ is given for a diaper core `[待补]`.

## Related Sources 关联来源

- [[Porous Structure and Liquid Flow Models]] — defines `V_s = (1/φ)(1/ρ_f − 1)` (Eq. 46, p. 54); packing fraction; fibre-density comparison
- [[Porous Structure and Liquid Flow Models]] — same relation; cellulose ~1.5 vs polyolefin ~0.92 g/cc on capacity
- [[Fibers and Fibrous Materials]] — "Denier is the bulk dial": lower linear density → higher specific air volume
- [[Fluid Absorption in High Bulk Nonwovens]] — capacity C ∝ T/W; areal-density penalty
- [[REL增强层]] — REL void-volume target 80–117 cm³/g @ 0.5 kPa
- 相关概念：[[孔隙率 Porosity]]、[[达西定律 Darcy's Law]]、[[吸收芯体]]、[[ADL（导流层）]]、[[绒毛浆（Fluff Pulp）]]、[[双组分纤维 Bicomponent]]、[[毛细压力 Capillary Pressure]]、[[渗透率 Permeability]]、[[每克厚度 T／W]]、[[结构性常数 K]]、[[Gel Blocking（凝胶阻塞）]]、[[交联密度 Crosslink Density]]

---
type: concept
title: "交联密度 Crosslink Density"
domain: [卫材研发, 变色与智能材料]
status: growing
updated: 2026-09-30
tags: [crosslink-density, SAP, hydrogel, swelling, Flory-Rehner, CRC-AUL]
---

# 交联密度 Crosslink Density

> 📌 **Page completed 2026-09-30** from 6 citing sources in the vault. All figures traced to their source pages. Anything not evidenced in the vault is marked `[待补]`.

## Definition 定义

**交联密度 ν_c** is the density of cross-link junction points in a three-dimensional polymer network, and it is the **pivotal control parameter** of SAP / hydrogel design（源：[[Acrylic-Based Superabsorbent Polymers]]）。Its governing relationship is **Q_max ∝ 1/ν_c** — swelling extent falls as cross-link density (and the chain-elasticity constraint) rises（源：[[Smart Polymers Ch14 Hydrogels in Microfluidics]]）。For cellulose derivatives, **cross-link density fixes the swelling ceiling while DS fixes the solubility ceiling; together they determine whether a cellulose derivative is a superabsorbent at all, and both must be tuned jointly**（源：[[Cross-linked Cellulose and Its Derivatives]]）。定义待补（引用来源未给出 ν_c 的数值定义或单位口径）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Swelling ↔ cross-link density law | Q_max ∝ 1/ν_c | [[Smart Polymers Ch14 Hydrogels in Microfluidics]] |
| Cross-linked CMC etherification | monochloroacetic acid up to 8 mol/mol cellulose; neutralisation ~0.5 mol caustic/mol cellulose; DS ≈ 0.4 or above | [[Cross-linked Cellulose and Its Derivatives]] |
| DS dissolution switch | below ~0.4 the material dissolves; at ~0.4 it is insoluble and highly absorbent | [[Cross-linked Cellulose and Its Derivatives]] |
| Epichlorohydrin cross-linker dose (CMC) | ~0.5 mol/mol | [[Cross-linked Cellulose and Its Derivatives]] |
| Acrylic-acid monomer concentration | 10–40 wt%; higher concentration → denser network, lower porosity, absorption falls sharply | [[Acrylic-Based Superabsorbent Polymers]] |
| Citric-acid cross-linker loading (cellulose SAH) | 1.5% — claimed novelty: maximise swelling while minimising cross-linker | [[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]] |
| Hydrogel water uptake | 20–100× its own weight, structure-dependent | [[Hydrogels in Regenerative Medicine]] |
| O-CNF loading effect (starch-CMC-NC) | O-CNF 0 → 1 → 2 wt% ⇒ 35.3 → 43.6 → 45.8 g/g; gel window widens from 6:4–8:2 to 4:6–9:1 | [[KR 10-2205294 B1（氧化淀粉-CMC-球形纳米纤维素高吸水体·Asiananotech）]] |
| Starch-CMC-NC peak performance | 0.9% saline uptake 45.8 g/g; retention 37.5 g/g (both exceed the synthetic SAP control 41.5 / 34.1 g/g) | [[KR 10-2205294 B1（氧化淀粉-CMC-球形纳米纤维素高吸水体·Asiananotech）]] |
| SAP dry-hydrogel imbibition range | 10–20% up to thousands of times dry weight | [[Smart Polymers Ch12 Polymeric Carriers Regional Therapy]] |

## Method / Mechanism 方法 / 机理

**The double-sided effect — there is an optimum.** Cross-link density too low → gel exudation (凝胶层析出), swelling collapse and rising system viscosity; too high → too many cross-link points, insufficient porosity and inadequate absorbency — **存在最优值**（源：[[Acrylic-Based Superabsorbent Polymers]]）。Stated independently for hydrogels: low cross-linking → high absorbency but poor structural stability; high cross-linking → good retention but restricted absorbency（源：[[Hydrogel-based Superabsorbent Polymers]]）。

**Two opposing structural levers.** Hydrophilic-group content ↑ ⇒ swelling ↑; cross-link density ↑ ⇒ chain mobility ↓, flexibility ↓, swelling ↓ — the same trade-off that governs SAP design（源：[[Hydrogels in Regenerative Medicine]]）。

**Cross-linking routes.** Chemical cross-linking (bifunctional/multifunctional cross-linkers, chain-transfer cross-linking) plus radiation cross-linking (β-ray, UV)（源：[[Acrylic-Based Superabsorbent Polymers]]）。For hydrogel SAP the routes are chemical cross-linking, **physical cross-linking** (hydrogen bonding; e.g. chitosan with calcium alginate, cellulose) and composite modification with nanomaterials（源：[[Hydrogel-based Superabsorbent Polymers]]）。**Green-synthesis note:** microwave polymerisation gives a **more uniform cross-link density**（源：[[Acrylic-Based Superabsorbent Polymers]]）。

**Negotiate against load.** Cross-link density buys strength and insolubility **at the price of capacity**; because a real absorbent core is compressed, the optimum shifts **higher** than free-swell testing implies（源：[[Cross-linked Cellulose and Its Derivatives]]）。

**Two orthogonal design axes.** The chemical composition of the polymer matrix determines the **type** of stimulus the hydrogel responds to; the **extent** of swelling is limited by the elasticity of the network — i.e. by ν_c（源：[[Smart Polymers Ch14 Hydrogels in Microfluidics]]）。Higher UV intensity shortens chain length, lowering both response time and mechanical strength（源：[[Smart Polymers Ch14 Hydrogels in Microfluidics]]）。

**Acrylic-SAP double-essence.** High absorption/retention comes from **hydrophilic carboxyl/hydroxyl groups + a 3-D cross-linked network skeleton**, both indispensable; the network is the ν_c-bearing structure（源：[[Acrylic-Based Superabsorbent Polymers]]）。

## Hygiene Relevance 卫材关联

- **It is the枢纽 of the SAP formulation playbook.** The REL project's core material SAP is treated with **cross-link density as the pivotal parameter** connecting monomer system, initiation/cross-linking route, absorption kinetics (diffusion + swelling coupling) and green/structured 2024 strategies（源：[[Acrylic-Based Superabsorbent Polymers]]）。
- **Simulation interface.** Cross-link density feeds directly into the **Flory-Rehner swelling model** as a parameter interface（源：[[Acrylic-Based Superabsorbent Polymers]]）→ see [[Flory- Rehner Theory]]。
- **Processed into product KPIs.** The cross-link-density / hydrophilic-group opposition is the two-lever structure–property relationship used to reason about **CRC (centrifuge retention capacity) vs modulus vs absorption-under-load**（源：[[Hydrogels in Regenerative Medicine]]）。
- **Cellulose-SAP design rule.** For a cellulose superabsorbent, DS and cross-link density are the two control variables that must be set jointly（源：[[Cross-linked Cellulose and Its Derivatives]]）。
- **Formal product exit.** GB-T 22875-2018 for diapers/sanitary towels is the formal standard into which SAP swelling behaviour is written as product specification（源：[[Hydrogels in Regenerative Medicine]]）。

## Open Questions 待补

- **No numeric ν_c values or units** (mol/cm³ or mol/g) appear in any excerpt — the vault states only the directional laws `[待补]`。
- **No dedicated measurement method** for ν_c (e.g. swelling-ratio / modulus method) is documented；the vault only cites the direction of the relationship `[待补]`。
- **The citing page [[Ancient Organic Dyes and Pigments Chemistry]] supplied no excerpt in the digest** — its specific use of the concept is unverified here `[待补]`。
- **No reconciled number between the 45.8 g/g starch-CMC-NC claim and commercial SAP CRC values** — the patent's synthetic-SAP control is a single unlabelled sample, so the "exceeds synthetic SAP" conclusion is a single-comparison result, not a category-wide one（源：[[KR 10-2205294 B1（氧化淀粉-CMC-球形纳米纤维素高吸水体·Asiananotech）]]）`[待补]`。

## Related Sources 关联来源

- [[Absorbent Technology]]
- [[Acrylic-Based Superabsorbent Polymers]]
- [[Cross-linked Cellulose and Its Derivatives]]
- [[Hydrogel-based Superabsorbent Polymers]]
- [[Fibers and Fibrous Materials]]
- [[Ancient Organic Dyes and Pigments Chemistry]]
- [[Smart Polymers Ch14 Hydrogels in Microfluidics]]
- [[Hydrogels in Regenerative Medicine]]
- [[Starch-CMC Acetal Crosslinked Superabsorbent（淀粉-CMC 缩醛交联高吸水体）]]
- [[Citric Acid Crosslinked Cellulose SAH（柠檬酸交联纤维素超吸水凝胶）]]
- [[Flory- Rehner Theory]]
- [[SAP性能指标（CRC AUL GBP Vortex）]]

---
title: "Industrial Drying Ch33: Drying of Fibrous Materials"
type: source
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch33.md.md
chapter: 33
book_title: "Handbook of Industrial Drying"
editor: "Arun S. Mujumdar"
author: "Roger B. Keey"
publisher: "CRC Press"
year: 2014
edition: "4th"
pages: "753-776"
lang: "en"
tags: ["source/book", "fibre-drying", "pulp", "fluff-pulp", "hornification", "lignin-Tg", "bound-free-water", "FSP", "anisotropic-swelling", "permanent-set", "sorptive-diffusion", "steam-drying", "TAD", "superheated-steam"]
tags_zh: ["纤维干燥", "木浆", "绒毛浆", "角质化", "木质素Tg", "结合水自由水", "纤维饱和点", "各向异性收缩", "永久变形", "吸附扩散", "蒸汽干燥", "穿流干燥", "过热蒸汽"]
domain: "hygiene-materials"
priority: "P0"
relevance_to_rel: "★★★★★ Core chapter. The definitive reference for fluff-pulp behaviour: FSP bound/free water split, anisotropic swelling (50-100x across vs along fibre), sorptive diffusion at low MC = hornification mechanism, lignin Tg as bonding switch (150°C), steam inversion temperature (160-230°C). Every mechanism transfers directly to fluff pulp and cellulosic nonwovens."
date_published: 2014
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Wood fibre water is held by cell-wall bonding; the differential heat of sorption for most woods is about half the heat of vaporization, falling to about one quarter at complete dryness"
  - "Loose fibres do NOT constitute a simple capillary-porous body -- constant-rate behaviour needs a different mechanism than neat porous media"
  - "Single-fibre diffusion is fast (wool ~1e-11 m2/s); macroscopic drying is controlled by the bed, not the fibre"
  - "Press drying bonds fibres when held 25 to 50 degC above the lignin glass-transition temperature"
  - "Critical moisture content X_cr and superheated-steam inversion temperature govern whether a fibre bed shrinks or case-hardens"
pages_linked: ["Handbook of Industrial Drying", "Industrial Drying Ch34 Drying of Textile Products", "Industrial Drying Ch35 Drying of Pulp and Paper", "Industrial Drying Ch15 Impingement Drying", "Industrial Drying Ch17 Conveyor Dryers", "SAP"]
---

# Ch33: Drying of Fibrous Materials

> **Source:** Keey, R.B., in Mujumdar (ed.), *Handbook of Industrial Drying*, 4th ed., CRC Press, 2014. Ch.33, pp.753–776.

---

## 1. Fibre-Water Physics 纤维-水物理

### Fibres Are Polymeric, Anisotropic, Lignin-Bonded 纤维是多晶的、各向异性的、木质素粘结的

> "Wood consists of a large number of fibers, together with cells of other types, bonded together by **lignin** to form a solid and rigid structure. The fibers are hollow, cylindrical structures, typically 1 to 4 mm in length, with walls composed mainly of cellulose and its associated polysaccharides. Most woods shrink and swell with moisture content, but the dimensional change is **much smaller along the fiber length compared with the changes across the fiber by a factor of 50 to 100**." (p.754)

### Water = Swelling; Loss = Shrinkage; Stress = Permanent Set 水=溶胀；失去=收缩；应力=永久变形

> "Water imbibed by the cell walls of fibers causes swelling and moisture loss causes shrinkage. Loading, including the development of drying stresses, introduces a creep strain that may not fully recover when the load is released. This is known as **permanent set**. With hygroscopic materials, moisture is found to reduce stiffness and increase creep, possibly as a result of plasticization." (p.756)

### Bound Water vs Free Water 结合水与自由水

> "For most woods the differential heat of sorption is about **half** that of vaporization, falling to about **one quarter** of that value when a complete monolayer is formed at about 4 to 5% moisture content." (p.756)

**Procurement implication:** Below FSP, water is bound in the cell wall (heat of sorption ≈ ½–¼ ΔH_vap) and **cannot be pressed out**. Above FSP it is free liquid removable by mechanical pressing. Specify bale MC against this split.

### Loose Fibres ≠ Simple Capillary-Porous Bodies 松散纤维≠简单毛细孔结构

> "A mass of loose fibers do **not** constitute a simple capillary-porous body, and the mechanisms that give rise to a constant-rate period in a porous network do not arise in a touching fibrous assembly. Recent experiments on the transport of water and n-propanol through samples of Kraft pulp and filter paper **confirm lack of importance of capillarity**." (p.762)

**Critical for modelling:** Do NOT use simple capillary-porous models for fluff pulp or airlaid webs.

### Single-Fibre Diffusion Is Fast; Mass Is Slow 单纤维扩散快，群体慢

> "The moisture diffusion coefficient within a single wool fiber is of the order 10⁻¹¹ m² s⁻¹... for fiber diameters, typically 20 µm for wool, the fiber will respond to a change in moisture conditions **very quickly, being about 98% complete within 2.5 s**." (p.759)

Yet a bale penetrates only **150 mm/day** (p.761).

### Press-Drying Bonds Above Tg 压制干燥在Tg之上形成粘结

> "The main effect of press drying is the thermal softening of lignin and cellulose components. If temperatures **25 to 50°C above the glass-transition point of lignin** is reached, then bonding can take place. This condition entails a temperature in the order of **150°C or above** in the wet web." (p.773)

---

## 2. Key Equilibrium Data 关键平衡数据

### Table 33.1: Equilibrium Moisture Content at Various RH 不同湿度下的平衡含水率

| Material 材料 | RH 0.2 | RH 0.5 | RH 1.0 |
|---|---|---|---|
| **Woodpulp** | 0.034 | 0.062 | 0.25 kg/kg |
| **Cotton** | 0.0305 | 0.0565 | 0.23 kg/kg |
| **Viscose** | 0.0555 | 0.101 | 0.46 kg/kg |

**Procurement use:** Use these equilibrium values to predict in-package MC drift and SAP–pulp partitioning under storage RH.

### Critical Moisture Content X_cr 临界含水率

| Material | X_cr (kg/kg) |
|---|---|
| Textile fabric | ~0.41 |
| Paper tissue | 2.6–4.0 |

### Inversion Temperature (Superheated Steam) 反转温度（过热蒸汽）

- Experimental range: **160–230°C**
- Point-inversion: 155–300°C
- Above inversion: steam drying outpaces air

---

## 3. Hygiene-Materials Action Cards 卫材应用卡

| Card | Insight | Action | Relevance |
|---|---|---|---|
| **H33-1** | Bound water (½–¼ ΔH_vap) cannot be pressed out; free water can (p.755–756) | Set fluff-pulp acceptance MC so incoming water is predominantly free (above FSP). Reject "dry but bound-water-rich" claims by measuring equilibrium MC, not just oven MC | ⭐⭐⭐⭐⭐ |
| **H33-2** | Woodpulp 0.034/0.062/0.25 vs viscose 0.0555/0.101/0.46 at RH 0.2/0.5/1.0 (p.755) | Use equilibrium values to predict in-package MC drift and SAP–pulp partitioning | ⭐⭐⭐⭐⭐ |
| **H33-3** | Sorptive (activated) diffusion + strong bonds at low MC (p.757); "permanent set" irreversible creep (p.756) | Minimise pulp re-wetting/redrying cycles. Audit supplier drying history as a quality attribute | ⭐⭐⭐⭐⭐ |
| **H33-4** | Press-drying bonds at lignin Tg+25–50°C ≈ 150°C (p.773) | Cap thermal exposure of non-bonded airlaid/woodpulp at 150°C. Reserve ≥150°C for deliberately bonded structures | ⭐⭐⭐⭐⭐ |
| **H33-5** | Shrinkage 50–100× greater across than along fibre (p.754) | Predict in-plane vs through-thickness dimensional change for core stability | ⭐⭐⭐⭐ |
| **H33-6** | Steam inversion 160–230°C; thermal damage increases with T, time, pH; water enhances degradation (p.773) | Caution for steam-drying cellulosic hygiene stock | ⭐⭐⭐ |

---

## 4. Related Sources 关联来源

- [[Handbook of Industrial Drying]] — Full book index
- [[Industrial Drying Ch34 Drying of Textile Products]] — Nonwoven textiles
- [[Industrial Drying Ch35 Drying of Pulp and Paper]] — Machine-scale pulp drying
- [[Industrial Drying Ch15 Impingement Drying]] — Surface drying
- [[Industrial Drying Ch17 Conveyor Dryers]] — Through-air TAD
- [[SAP（高吸水树脂）]] — Super Absorbent Polymer

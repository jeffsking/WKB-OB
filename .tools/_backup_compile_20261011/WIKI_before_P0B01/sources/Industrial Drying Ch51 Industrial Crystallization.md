---
type: source
title: "Industrial Drying Ch51 Industrial Crystallization"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch51.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Easy dewatering and drying of crystals requires uniform, sufficiently large crystal size — the chapter's organizing theme (p.1202)"
  - "Supersaturation is the main parameter determining crystal growth rate, nucleation, agglomeration, shape, and purity (p.1203)"
  - "Smaller crystals and wide size distributions make dewatering and drying harder; agglomerate porosity/roughness also affect dewatering (p.1205)"
  - "Kozeny–Carman: if particle diameter drops to 10% of original value, filtration pressure drop increases 100-fold (p.1216)"
  - "From the drying viewpoint crystals of about 1 mm or above are best, but sizes above approximately 1 mm tend to be harmful — steady-state and centrifuge breakage issues (p.1218)"
  - "Slower crystal growth yields purer crystals; agglomeration traps mother-liquor inclusions that decrease purity (p.1206)"
summary_cn: "溶液工业结晶综述，核心是让晶体尺寸均匀足够大以便下游过滤与干燥（约1mm为最优窗口），其过饱和/成核/生长逻辑与粒径-过滤-干燥权衡对聚合物结晶和 SAP 粉体设计仅有概念性迁移价值。"
tags: ["source/book", "crystallization", "supersaturation", "nucleation", "CSD", "polymorphism", "seeding", "filtration", "Kozeny-Carman", "powder-sizing"]
tags_zh: ["结晶", "过饱和", "成核", "粒径分布", "多晶型", "晶种", "过滤", "粉体粒径"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["Handbook of Industrial Drying", "Industrial Drying Ch50 Solid-Liquid Separation", "Industrial Drying Ch41 Drying of Polymers", "Industrial Drying Ch29 Drying of Pharmaceutical Products"]
---

# Ch51: Industrial Crystallization

> Source: Mujumdar (ed.), *Handbook of Industrial Drying*, 4th ed., CRC Press, 2014, Ch.51, pp.1200–1221. (Palosaari, Louhi-Kultanen & Sha)

Relevance to hygiene REL absorbent-core engineering: **low** 低相关。Not a drying process — value is conceptual: nucleation/growth kinetics as the analogue of polymer crystallization, and the size ↔ filterability ↔ drying trade-off for any powder (SAP, actives). 译注：本章非干燥过程，与卫材芯体工程仅概念性相关——成核/生长逻辑对应聚合物结晶，粒径权衡对应 SAP 粉体规格。

---

## 1. Downstream-Driven Design Goal 下游导向的设计目标

> "The easy dewatering and drying of crystals requires that the crystals be of a uniform and sufficiently large size. This is, therefore, the major theme of this chapter." (p.1202)

> "the smaller the size of the crystals, the more difficult the dewatering and drying. The effect of a wide distribution of crystal sizes is the same. Especially in precipitation, where agglomerates are formed, the porosity and roughness of the crystal surface may also affect dewatering and drying." (p.1205)

---

## 2. Supersaturation as the Master Variable 过饱和为主变量

> "Supersaturation is the main parameter in determining the rate of crystal growth and nucleation … the level of supersaturation is the main parameter that determines the agglomeration, shape, and purity of the crystals." (p.1203)

Fundamentals (p.1203–1206): Δc = c − c*; S = c/c*; crystal growth occurs mainly in the metastable zone; primary (homo/heterogeneous) vs secondary nucleation; population balance (∂n/∂t + G·∂n/∂L = 0) with median size L₅₀ = 3.67·G·τ — bigger crystals come from slower nucleation or longer residence time.

Purity rule (p.1206): "the slower the crystal growth rate, the purer the crystal"; agglomeration "may contain inclusions of the mother liquor, which decreases the purity."

Polymorphism (p.1206): same composition, multiple solid forms with different melting points and dissolution rates — the pharmaceutical industry's central solid-form concern; supersaturation can even select the polymorph (p.1221).

---

## 3. Quantified Levers 量化杠杆

| Lever | Rule | Page |
|---|---|---|
| Seeding | Seed 0.1–0.3× final size, 0.1–3% of final mass; 20–50 µm seed for 500–1000 µm final | p.1208 |
| Fines destruction | Increases mean crystal size in high-nucleation systems, but "does … lead to a wide particle size distribution" | p.1210 |
| Filtration scale | "If the particle diameter drops to 10% of its original value, the pressure drop increases by 100-fold"; 10× viscosity → 10× ΔP | p.1216 |
| Drying window | Crystals best at ~1 mm or above, but "crystal sizes above approximately 1 mm tend to be harmful" (steady-state surface-area loss; centrifuge breakage) | p.1218 |

The drying-window paragraph (p.1218) is the chapter's sharpest statement: large crystals retain less mother liquor and are purer (same surface-liquid thickness over more mass), but beyond ~1 mm the reduced crystal surface cannot release supersaturation in continuous mode and crystals may break in the centrifuge.

---

## 4. Method & Limitations 方法与局限

Review drawing on Mullin, Randolph & Larson, Mersmann, Myerson, Tavare, Davey & Garside; population-balance theory and CFD studies. Limitations 局限 (译注):
- Predictive power is weak by the authors' own admission: "prediction of CSDs is still quite difficult" (p.1205); crystallizer selection "more an art than science" (p.1216); CFD "still at an initial stage" (p.1212)
- OCR garbling in Eq 51.4–51.5 (p.1207) and Table 51.1 notation (p.1213) — verify against Mersmann before use
- No drying-rate equations, no moisture-transport model, no hygiene-substrate content

---

## 5. Hygiene Implication 卫材关联

Low 低相关 (译注) — conceptual transfer only:
1. **Polymer crystallization lens**: for PP/PET/PLA cooling in hygiene substrates, undercooling plays the role of supersaturation and nucleating agents/seeds set crystalline structure — the same nucleation/growth framework ([[Industrial Drying Ch41 Drying of Polymers]]).
2. **Powder sizing band**: the ~1 mm optimum with an upper bound ("bigger is better" is wrong, p.1218) is a portable lesson for SAP/actives granule specs.
3. **Fine-fraction penalty**: the Kozeny–Carman 10% size → 100× ΔP rule (p.1216) quantifies why sub-10 µm fractions are costly to separate — mechanical dewatering context in [[Industrial Drying Ch50 Solid-Liquid Separation]].
4. **Solid-form control**: polymorphism and mother-liquor inclusion matter for crystallized actives on hygiene lines ([[Industrial Drying Ch29 Drying of Pharmaceutical Products]]) — residual solvent inclusions are a VOC/drying concern.
5. No operational dryer-control or safety content here; those live in Ch49 and Ch48.

---

## 6. Related Sources 关联来源

- [[Handbook of Industrial Drying]] — Full book index
- [[Industrial Drying Ch50 Solid-Liquid Separation]] — Filtration of crystal suspensions, Kozeny–Carman scale
- [[Industrial Drying Ch41 Drying of Polymers]] — Polymer crystallization analogue
- [[Industrial Drying Ch29 Drying of Pharmaceutical Products]] — Solid-form/actives context

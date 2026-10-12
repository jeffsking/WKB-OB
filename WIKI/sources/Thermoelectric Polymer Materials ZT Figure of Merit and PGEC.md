---
type: source
title: "Thermoelectric Polymer Materials ZT Figure of Merit and PGEC"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Thermoelectric_Phenomena_DeepBook/Thermoelectric_AnnualReview_深度拆解.md.md
date_published: 2011
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "'The best TE materials that are currently used in devices have a value of ZT ≈ 1. Previous to the mid-1990s, this value had been a practical upper limit for more than 30 years, yet there were no theoretical or thermodynamic reasons for ZT ≈ 1 as an upper barrier.' (lines 348–350)"
  - "Figure of merit and its couplings: 'ZT = α²σT / κ = α²T / ρκ'; total thermal conductivity κ = κ_L + κ_E; and 'σ is tied to κE through the Wiedemann-Franz relationship' (κ_E = L₀σT), so raising σ necessarily raises κ_E."
  - "PGEC design paradigm: 'Slack suggested that the best TE material would behave as a phonon glass–electron crystal (PGEC) material; that is, it would have the electrical properties of a crystalline material and the thermal properties of an amorphous or glass-like material.' (lines 534–537)"
  - "Screening thresholds stated in the source: thermopower α ≥ 150 µV K⁻¹ is necessary for ZT ≈ 1; good TE materials have κ < 2 W m⁻¹ K⁻¹ with κ_L ≈ κ_E; optimal carrier concentration ≈ 10¹⁹ carriers cm⁻³; mobility ≈ 2,000 cm²(V·s)⁻¹; band gap E_G ≈ 0.25 eV at 300 K."
  - "Material benchmarks: Bi₂Te₃ ZT ≈ 0.6 at room temperature (~0.8 optimised) with anisotropic κ (κ⊥c ≈ 1.5, κ∥c ≈ 0.7 W/mK); PbTe ≈ 1.0 at 600–800 K; skutterudites ≈ 1.2 at 600–800 K; AgPbMTe (LAST) > 2 at high temperature; SiGe ≈ 0.6–0.8 at 900–1200 K."
  - "'Slack's (24) PGEC methodology and the advent of TE nanocomposites hold promising potential for achieving materials that possess ZT values of the order of 2–3...' (lines 840–842); device conversion efficiency quoted at 7–8% and above."
summary_cn: "Tritt（Clemson）Annual Review of Materials Research 2011 综述拆解：热电材料优劣由 ZT = α²σT/κ 决定，商用材料长期停滞于 ZT ≈ 1（非理论上限）；α、σ、κ 通过 Wiedemann-Franz 耦合，须以 PGEC（声子玻璃-电子晶体）与纳米复合解耦电热输运，远景 ZT 2–3。"
tags: ["source/book", "thermoelectric", "Seebeck", "figure-of-merit", "ZT", "PGEC", "Wiedemann-Franz", "thermal-conductivity", "nanocomposite", "energy-harvesting"]
tags_zh: ["热电材料", "塞贝克系数", "热电优值", "声子玻璃电子晶体", "维德曼-弗兰兹定律", "热导率", "纳米复合", "能量收集"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Thermoelectric Materials and Applications Review]]", "[[Smart Textiles & Wearables]]", "[[Flexible Stretchable Electronics (imec)]]", "[[Wearable Electronics (National Science Review 2023)]]", "[[Smart Textile Visual Perception (GRID)]]"]
---

# Thermoelectric Polymer Materials ZT Figure of Merit and PGEC 热电材料：ZT 优值与 PGEC 设计理念

> Source: Terry M. Tritt (Clemson University), "Thermoelectric Phenomena, Materials, and Applications", *Annual Review of Materials Research* 2011, Vol. 41, pp. 433–448; DOI 10.1146/annurev-matsci-062910-100453; source text ~1,055 lines. Compiled from the 深度拆解报告 `Thermoelectric_AnnualReview_深度拆解.md.md`, whose line-number citations are reproduced below.
> Scope note 范围说明：本综述的主体材料体系是**无机半导体**（Bi₂Te₃、PbTe、SiGe、skutterudites、clathrates、half-Heusler、氧化物），**并未讨论导电聚合物热电材料**；文件名中的 "Polymer Materials" 沿用本批次的命名约定，实际内容以无机 TE 材料与器件物理为主，向柔性/纺织基体迁移的部分属于报告的推论（模块 5），非原文结论。

## Five core arguments 五大核心论点

1. **Decade-scale progress 十年进展**：
   > "Over the past 10–15 years, there have been significant advances in the scientific understanding as well as in the performance of thermoelectric (TE) materials."
   > "The conversion of waste heat into electrical energy will certainly play a role in our current challenge for alternative energy technologies to reduce our dependence on fossil fuels and to reduce greenhouse gas emissions."
2. **ZT ≈ 1 is a practical, not theoretical, ceiling**：
   > "The best TE materials that are currently used in devices have a value of ZT ≈ 1. Previous to the mid-1990s, this value had been a practical upper limit for more than 30 years, yet there were no theoretical or thermodynamic reasons for ZT ≈ 1 as an upper barrier."
3. **PGEC paradigm 范式**：
   > "Slack suggested that the best TE material would behave as a phonon glass–electron crystal (PGEC) material; that is, it would have the electrical properties of a crystalline material and the thermal properties of an amorphous or glass-like material."
4. **Parameter coupling 参数耦合**：
   > "The interrelationship of the properties of these materials makes it very difficult to find materials that can achieve high ZT values, i.e., ZT > 1."
   > "However, σ is tied to κE through the Wiedemann-Franz relationship, and the ratio of κE/σ is essentially constant at a given temperature for the majority of TE materials."
5. **Outlook 展望**：
   > "A multidisciplinary approach will be required to develop higher-efficiency TE materials and devices."
   > "Slack's (24) PGEC methodology and the advent of TE nanocomposites hold promising potential for achieving materials that possess ZT values of the order of 2–3 and that are thermally stable over the range of temperatures in which they are to be used."

## Operational definitions 关键概念定义

| # | Concept 概念 | Definition / quote 定义与原文 | Line 行号 |
| --- | --- | --- | --- |
| 1 | Seebeck coefficient α / thermopower | "α ≈ C/q, where C is the specific heat and q is the charge of the carrier" | 417–419 |
| 2 | Thermal conductivity κ | "κ = κ_L + κ_E, where κ_L and κ_E are the lattice and electronic contributions" | 208–210 |
| 3 | Figure of merit ZT | "ZT = α²σT / κ = α²T / ρκ" | 200–209 |
| 4 | Power factor PF | "α²σT (or α²T/ρ), is typically optimized through doping in narrow-gap semiconducting materials as a function of carrier concentration (typically approximately 10¹⁹ carriers cm⁻³)" | 210–212 |
| 5 | PGEC | "the electrical properties of a crystalline material and the thermal properties of an amorphous or glass-like material" | 535–537 |
| 6 | Minimum lattice thermal conductivity κ_min | achieved "when all the phonons have a mean free path that is essentially equal to the interatomic spacing" | 543–546 |
| 7 | TE couple 热电电对 | n-type + p-type; ZT = (α_p − α_n)²T / [(ρ_nκ_n)^½ + (ρ_pκ_p)^½]² | 215–223 |
| 8 | COP φ / efficiency η_TE | "directly related to the ZT" | 225–227 |
| 9 | Wiedemann–Franz | "κ_E = L_0 σ T" | 356 |
| 10 | Classical electron gas thermopower | "approximately k_B/e ≈ 87 µV K⁻¹" | 420–422 |
| 11 | Narrow-band-gap threshold | "E_G ≈ 10 k_B T₀ or ≈ 0.25 eV at 300 K" | 521–522 |

## Material systems and ZT benchmarks 材料体系与 ZT 基准

| System 体系 | Composition 组成 | ZT | Temperature 温度 | Note 备注 |
| --- | --- | --- | --- | --- |
| Bi₂Te₃ alloys | p-type / n-type Bi₂Te₃ | ≈ 0.6（室温）；优化后 ~0.8 | ~300 K | 六方层状 a = 3.8 Å, c = 30.5 Å；κ⊥c ≈ 1.5、κ∥c ≈ 0.7 W/mK；κ_p,n ≈ 1.9 W/mK |
| PbTe | doped PbTe | ≈ 1.0 | 600–800 K | 中高温经典 TE 材料 |
| Si₁₋yGe_y | Si-Ge 合金 | ≈ 0.6–0.8 | 900–1200 K | 常用于 RTG（Voyager, Cassini） |
| Skutterudites 笼合物 | CoSb₃ 基 + Ce/Yb/Ba filler + In 掺杂 | ≈ 1.2 | 600–800 K | "rattling" 原子散射声学声子 |
| Half-Heusler | Zr₀.₅Hf₀.₅Ni₀.₅Pd₀.₅Sn₀.₉₉Sb₀.₀₁ | ≈ 0.7 | ≈ 800 K | MNiSn 通式，M = Zr/Hf/Ti |
| AgPbMTe (LAST) | AgPb₁₀SbTe₁₂ | > 2（部分 > 1.7） | 高温 | 低热导率源于 nanodot 组分调制 |
| NaCo₂O₄ 氧化物 | NaCo₂O₄ | 0.7–0.8 | 1000 K | 强关联层状氧化物 |
| β-Zn₄Sb₃ | Zn₄Sb₃ | — | 中温 | JPL 再调研发电应用 |
| 超晶格/纳米薄膜 | Bi/Sb、PbSe/Te 超晶格 | > 1（部分薄膜） | 宽温域 | 界面声子散射降低 κ_L |
| TE nanocomposites | 传统基体 + 纳米颗粒 | 显著提升 | 宽温域 | 纳米界面声子散射 |

## Screening thresholds 关键性能阈值（原文提取）

| Threshold 阈值 | Value 数值 | Line 行号 |
| --- | --- | --- |
| Commercial ZT ceiling 商用上限 | ZT ≈ 1 | 348–350 |
| Long-term target 远景目标 | ZT ≈ 2–3（PGEC + 纳米复合） | 840–842 |
| Power-generation efficiency 发电效率 | 7–8% 及以上 | 346–347 |
| Cooling benefit 制冷潜力 | 冷计算可使 CMOS 提速 30%–200% | 90–91 |
| Thermal conductivity 好 TE 材料热导率 | κ < 2 W m⁻¹ K⁻¹，且通常 κ_L ≈ κ_E | 504–505 |
| Thermopower floor 最低热电势门槛 | α ≥ 150 µV K⁻¹（ZT ≈ 1 的必要条件） | 601–603 |
| Carrier concentration 理想载流子浓度 | ~10¹⁹ cm⁻³ | 211–212, 610 |
| Mobility 理想迁移率 | μ ≈ 2,000 cm²(V·s)⁻¹ | 522 |
| Band gap 理想带隙 | E_G ≈ 0.25 eV @ 300 K | 521–522 |

Decisive screening sentence 关键筛选句（line 601–603）：
> "Whether a material has a κL ≈ κmin does not matter. If a material cannot be tuned or doped to attain a minimum thermopower (150 µV K⁻¹), then it cannot achieve ZT ≈ 1."

## Logical chain 逻辑链条

现象（Seebeck / Peltier / Thomson 三效应）→ 参数（α、σ、ρ、κ）→ ZT 公式的强耦合 → "ZT ≈ 1 陷阱" → Wiedemann–Franz 约束要求解耦电热输运 → PGEC 范式 → 材料策略（rattling 声子散射 / κ_min 声子工程 / 能带与掺杂工程）→ 应用落地（低温 Bi₂Te₃ 用于芯片与生物冷点冷却；中温 skutterudites / half-Heusler 用于汽车尾气；高温 SiGe / NaCo₂O₄ 用于 RTG 与工业废热）。

Bridge quotes 桥接句：
> "This approach works especially well in highly covalent semiconductor materials based on clathrates (Si, Ge, or Sn) and void structures formed by heavy elements..." (728–730)
> "Several automotive applications are beginning to use thermoelectric materials either for climate-controlled cooling in automotive cabins or for waste heat recovery from automobile exhaust systems." (837–839)

## Limitations stated in the source 原文自陈的限制

- Efficiency 效率："low efficiency (<10%)"（833–834），应用被作者归入 "niche applications"；
- Bulk materials 体材料："higher-performance bulk materials will have to be developed"（802–804）；
- Thermal stability 热稳定性：必须 "thermally stable over the range of temperatures in which they are to be used"（841–842）。

## Hygiene implication 卫材关联

Not directly relevant. 本综述讨论的是无机热电半导体与废热发电/固态制冷器件，与纸尿裤芯体、SAP、无纺布、热熔胶无直接技术接口。仅有的间接价值：
1. **智能卫品的可穿戴供电概念**：人体皮肤约 33°C 与环境约 20°C 的温差可驱动柔性 TE 发电（报告模块 5.2 的推论，非原文数据），若未来在纸尿裤集成湿度/温度传感器，TE 自供电是一条免电池路径；但原文明确效率 <10%，短期不具备量产经济性。
2. **局部制冷/温控纺织**：原文 "small-scale, localized cooling" 与 "seat coolers for comfort" 可对应温控服装方向，与卫品的热舒适诉求有弱关联。
结论：本页对当前卫材研发**不构成可落地输入**，保留作为智能卫品（传感 + 自供电）方向的技术背景资料。

## Related Sources 关联来源

- [[Thermoelectric Materials and Applications Review]] — 同主题的另一篇热电材料与应用综述。
- [[Smart Textiles & Wearables]] — 智能纺织与可穿戴，TE 柔性化的应用载体。
- [[Flexible Stretchable Electronics (imec)]] — 柔性可拉伸电子，柔性 TE 单元的集成路径。
- [[Wearable Electronics (National Science Review 2023)]] — 可穿戴电子综述，自供电与传感的背景。
- [[Smart Textile Visual Perception (GRID)]] — 智能纺织视觉感知，与卫品传感化方向相邻。

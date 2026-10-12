---
type: source
title: "Industrial Drying Ch36 Drying of Wood Principles and Practices"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch36.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Cellulose is a linear polymer with an average degree of polymerization of 10,000, organized in elementary fibrils that are partly crystalline to the extent of 50–70%; lignin is the cementing agent binding individual cells (p.825)"
  - "FSP (fiber saturation point) is the EMC at 99% RH, ≈30–32% for most commercial species, and falls with temperature (Sitka spruce ~31% at 25°C → 23% at 100°C) (p.828)"
  - "Wood's permeability anisotropy is dramatic: longitudinal permeability can be 1000× transverse for softwoods and more than a million-fold for hardwoods; pit aspiration on drying locks in low permeability (p.832–833)"
  - "Removing sorbed water from the cell wall forms new hydrogen bonds between hydroxyl groups of molecular chains, reducing inter-chain distance — shrinkage is normal to the microfibril direction, so longitudinal shrinkage is negligible; tangential ≈ 2× radial (p.830)"
  - "High-temperature drying (product above water's boiling point) creates internal overpressure that drives moisture to the surfaces; heartwood (permeability ~10⁻¹⁶ m² vs sapwood 10⁻¹² m², Table 36.8) stays wet and develops higher overpressure (p.841)"
  - "Juvenile wood from plantations carries higher sapwood MC (higher transport/drying-energy costs), lower basic density (increased collapse potential in high-temperature drying) and more warp — quality variability baked in at the tree level (p.859)"
summary_cn: "木材干燥的机理权威章：从聚合物复合材料结构、FSP 自由/结合水分界、各向异性渗透与收缩，到干燥应力/记忆效应与窑炉实践，为绒毛浆提供'原料变异性如何在树级固化'的上游解释。"
tags: ["source/book", "drying/wood", "hornification", "fiber-saturation-point", "anisotropy", "fluff-pulp-upstream"]
tags_zh: ["书籍来源", "木材干燥", "角化机理", "纤维饱和点", "各向异性", "绒毛浆上游"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch31 Drying of Ceramics]]", "[[Industrial Drying Ch33 Drying of Fibrous Materials]]", "[[Industrial Drying Ch35 Drying of Pulp and Paper]]", "[[Industrial Drying Ch41 Drying of Polymers]]", "[[Industrial Drying Ch4 Transport Properties in the Drying of Solids]]"]
---

# Chapter 36 — Drying of Wood: Principles and Practices

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.36, pp.822–863 (span derived from quoted pages; to be verified against print).
> Authors: Patrick Perré & Roger B. Keey.
> 注：页码按 PDF 页 − 21 推算（锚定 Ch.1 = p.1），与印刷版核对前属推算值。

## Scope & Position 范围与定位

The Handbook's definitive mechanistic treatment of wood drying — and the **upstream material source for fluff pulp**. Progression: anatomy → chemical composition → board-scale physics (free/bound water, FSP, anisotropic shrinkage, Darcy/capillary/bound-water diffusion) → drying process (low-T convective; high-T internal overpressure) → mechanics (shrinkage stress, memory effect, case-hardening, checking) → kiln practice.
定位：全书"原料源"锚点 — Ch36 供木材，Ch33/Ch35 把它变成纤维与浆页。它是本批六章中机理最深的一章：唯一完整推导 Darcy、毛细压力、结合水扩散方程与黏弹/力吸应力本构的章节。

## Material Structure 材料结构 (§36.1–36.2.1)

"Cellulose is a linear polymer with an average degree of polymerization of 10,000. These polymer chains are organized in elementary fibrils that are partly crystalline to the extent of 50 to 70%. … Lignin is often regarded as the cementing agent that binds individual cells together and is insoluble in most solvents." (p.825)
→ 木材 = 取向半结晶纤维素 + 木质素/半纤维素无定形基体的复合材料 — 与 [[Industrial Drying Ch41 Drying of Polymers]] 的聚合物图景同构。抽提物 5–30%。

**FSP（纤维饱和点）— 自由/结合水的主分界**：
"FSP of the wood may be defined as the equilibrium moisture content (EMC) in an environment of 99% relative humidity. This yields a value of 30 to 32% for most commercial species … FSP falls with increasing temperature. For a softwood such as Sitka spruce, FSP falls from about 31% at 25°C to 23% at 100°C." (p.828)
- 绿材含水率基线（Table 36.3, p.828）：软材边材 150–200%、心材 40–80%；硬材边材 80–120%、心材 60–100%（干基）— 制浆前必须移除的水。
- 吸附滞后：脱附 EMC > 吸附 EMC，比值 0.75–0.88（p.829）。
- 微分吸附热："slightly higher than 1000 kJ kg⁻¹ for oven-dry wood … decreases rapidly … to reach zero … at the FSP." (p.830) → 结合水越少越贵。

## Transport 传递 (§36.2.2, p.832–837)

"Wood has dramatic anisotropy ratios: the longitudinal permeability can be 1000 times greater than the transverse permeability for softwoods and more than a million-fold for hardwoods." (p.832)
- 流体排出压倒性沿纵向；软材干燥中纹孔闭塞（pit aspiration）"impossible to avoid … when drying softwoods under normal conditions" (p.833) — 渗透率被永久锁低。
- 传递路径：单相 Darcy → 多相广义 Darcy（相对渗透率）→ 毛细压力 → 结合水扩散；D_b 随结合水含量陡增（Eq 36.14，OCR 受损）。
- "diffusion becomes very slow when the bound-water content decreases toward zero" (p.854) → 低于 FSP 后干燥速率由慢速活化结合水扩散主导 — 任何纤维素网降速段的共同机制。

## Drying Process & Mechanics 干燥过程与力学 (§36.2.3–36.2.5, p.841–855)

**高温干燥 — 内部过压原理**：
"the temperature of the product is above the boiling point of water. Such conditions ensure that an overpressure exists within the material, which implies that a pressure gradient drives the moisture toward the exchange surfaces." (p.841)
但心材（渗透率 ~10⁻¹⁶ m² vs 边材 10⁻¹² m², Table 36.8）保持湿润并发展更高过压 — 边/心材工艺分歧。

**收缩与应力**：
"when sorbed water is removed from the cell wall, new hydrogen bonds form between the hydroxyl groups of the molecular chains and reduce the distance between the chains. This variation affects the dimension in a direction normal to the microfibril direction. This fact explains why the longitudinal shrinkage is usually negligible." (p.830)
- 纵向收缩可忽略；横向主导，切向 ≈ 2× 径向（Table 36.6）。"Shrinkage is the 'driving' force for drying stress" (p.845)。
- 应力反转 = case hardening（p.846）；内拉应力过高 → 内部开裂（p.845）。
- 记忆效应：应变张量 "depends not only on the temperature and moisture content values but also on their variations in time" (p.847) — 力学状态的时间滞后，原文承认 "very difficult to characterize"。
- 应力木放大异常：压缩木纵向收缩"order of magnitude greater"、张力木 "~fivefold greater"（Table 36.10, p.859）。

## Kiln Practice & Quality 窑干实践 (§36.3, p.855–863)

- 快而好的三条经验规则（p.855）：高相对湿度（降低 MC 梯度）、高温度（加速内部传递+黏弹蠕变）、高风速（堆垛均匀性）— 但三者间存在矛盾权衡。
- 特性干燥曲线 N_v = β f_b (Y_W − Y_G)（Eq 36.22, p.863）— 工业近似。
- 质量三分：gross / intrinsic / sawing；大节子 "treble the level of board rejection for unacceptable knot checks" (p.858)。

## Feedstock Variability 原料变异性（浆木链条）

"The gradual exhaustion of natural forest resources has forced the industries to accept juvenile wood from plantations and second-growth forests. Although juvenile wood is often considered unsatisfactory … High moisture content in sapwood of young trees [→] Higher transport and drying-energy costs; Lower basic density [→] Increased potential for collapse during high-temperature drying." (p.859)
速生人工林原料（桉树、辐射松）幼龄材比例高 → 收缩/翘曲更大、密度更低 — 正是浆得率与均匀性变异性的树级来源。木材本身 "extremely difficult to characterize precisely" (p.822)。

## Limitations 局限

- 聚焦实体木材窑干，不涉及制浆或绒毛浆原料工艺 — 卫材迁移完全在上游/间接层面。
- Eq 36.3、36.14、36.16 与 S1–S4 张量组 OCR 受损；结合水扩散系数的指前/活化常数须对照印刷版才能复用。
- 记忆效应本构模型自认难以表征（p.847）；工业排程仍靠经验规则而非三变量全模型。
- 无 SAP、无非织造、无绒毛浆专门内容。

## Hygiene Implication 卫材关联

**总评：本批最高价值章（机理深度 ★★★★☆；与绒毛浆直接相关性为上游供应链 ★★★★☆）。** 木材/纤维物理与绒毛浆一一映射：角化、纤维塌缩、水分吸附行为。

- **★★★★★ 氢键角化的分子机理在本章被逐句讲透**："new hydrogen bonds form between the hydroxyl groups of the molecular chains"（p.830）= 脱附→羟基间新氢键→链距缩短 = 不可逆收缩 = hornification 微观事件。木材、商品浆再干（Ch33/Ch35）发生的是**同一个事件**。行动：统一供应商审计语言 — 每一次再干/过干 = 氢键重新锁定 = 膨润度损失；引用 Ch35 的疏解能耗 KPI 量化该损失。
- **★★★★☆ 用 FSP 与绿材含水率审计来料**：FSP ≈ 30–32%（99% RH 定义，p.828）是自由/结合水分界 — 也是热干燥变得受速率限制、能耗陡增的拐点。把供应商木片/浆板 MC 基准对标 FSP 与树种绿材表（Table 36.3），拒绝隐含过高蒸发能量或干燥不充分的批次。
- **★★★★☆ 审浆木来源，不只审浆指标**：幼龄材/应力木比例（p.859, Table 36.10）向浆得率、蓬松度、疏解能耗传导变异性。认证绒毛浆供应商时追问纤维来源（人工林/天然林、树种、轮伐期），索取幼龄材比例数据；高幼龄材进料按变异性/均匀性风险处理。
- **★★★☆ 应力木与节子是可查询的质量前兆**：压缩木纵向收缩大一个量级、张力木约 5 倍（Table 36.10）；节子使拒收率升三倍（p.858）。索取节子/杂质（shive）含量数据，与上游应力木关联，作为垫材缺陷与疏解负荷的预测因子。
- **★★★☆ 渗透率各向异性解释供应商产能天花板**：纵向/横向 1000×–10⁶×（p.832）+ 软材干燥纹孔闭塞（p.833）→ 高抽提物/富心材进料脱水与疏解更慢 — 计入供应商产能与交期评估。
- **★★★☆ 高RH/高温/高风速三规则移植到纤维素热干燥**（p.855）：凡我方控制的转换/再干线，用三杠杆做"快而不坏"检查单 — 高湿降低 MC 梯度防开裂，高温借黏弹蠕变松弛应力，高风速保堆垛均匀。
- 开放问题：①能否用 FSP 与结合水扩散系数预测商品浆再干能耗罚金，桥接 Ch35 闪干条款？②浆木中幼龄/应力木比例是否在交付绒毛浆上留下可测指纹（疏解能耗、蓬松度、节子含量）可写入采购规格？[待验证]

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch31 Drying of Ceramics]]
- [[Industrial Drying Ch33 Drying of Fibrous Materials]]
- [[Industrial Drying Ch35 Drying of Pulp and Paper]]
- [[Industrial Drying Ch41 Drying of Polymers]]
- [[Industrial Drying Ch4 Transport Properties in the Drying of Solids]]

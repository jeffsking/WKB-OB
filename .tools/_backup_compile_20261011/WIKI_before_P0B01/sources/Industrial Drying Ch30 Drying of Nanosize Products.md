---
type: source
title: "Industrial Drying Ch30 Drying of Nanosize Products"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch30.md.md
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Nanoparticles tend to agglomerate and properties are adversely affected if inappropriate drying methods are chosen; keeping nanoparticles well dispersed during drying is a vital requirement (p.712)"
  - "Solvent evaporation proceeds through three periods (constant rate → first falling rate → second falling rate); at the critical point the radius of curved liquid equals the gel pore size and capillary tension reaches its maximal value (p.713)"
  - "Capillary pressure P = 2σ cosθ / r_p is the major cause of both gel-skeleton cracking and nanoparticle agglomeration (p.714, Eq. 30.1)"
  - "Hard agglomerates are chemically irreversible: nonbridging surface hydroxyls condensing to Me–O–Me groups are the basic source of hard agglomeration (p.714–715)"
  - "Drying route sets final nanostructure: oven-dried TiO₂ gave 50–100 nm / 4.88 m²/g vs ethanol-replacement supercritical 10–20 nm / 113.8 m²/g (Table 30.4, p.722–723)"
  - "Nanoparticles are difficult to collect if emitted in air and can be easily inhaled or even ingested by the skin — a first-order design constraint for any drying process (p.725)"
summary_cn: "系统论述纳米材料干燥中的毛细压力机理（P=2σcosθ/r_p）与团聚四大理论，并给出直接干燥/溶剂置换/改性干燥三大方法族的定量对比与选择规则。"
tags: ["source/book", "drying/nanomaterials", "mechanism/capillary-pressure", "agglomeration", "nanocellulose-relevant"]
tags_zh: ["书籍来源", "纳米材料干燥", "毛细压力机理", "团聚控制", "纳米纤维素相关"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch29 Drying of Pharmaceutical Products]]", "[[Industrial Drying Ch33 Drying of Fibrous Materials]]", "[[Industrial Drying Ch35 Drying of Pulp and Paper]]", "[[Industrial Drying Ch41 Drying of Polymers]]"]
---

# Chapter 30 — Drying of Nanosize Products

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.30, pp.711–726.
> Authors: Baohe Wang, Li Xin Huang, Arun S. Mujumdar.
> 注：页码按 PDF 页 − 21 推算（锚定 Ch.1 = p.1），与印刷版核对前属推算值。

## Scope & Position 范围与定位

The book's nanomaterials-drying chapter. Two failure modes absent at macro scale dominate: (i) cracking/collapse of the fragile porous gel skeleton, (ii) irreversible agglomeration of nanoparticles during solvent removal.
" nanoparticles tend to agglomerate and properties of nanoparticles are adversely affected if we do not choose appropriate drying methods. So to assure that nanoparticles are well dispersed during drying is a vital requirement in the preparation of such products." (p.712)
逻辑链：nm 级特征（p.711）→ 蒸发三阶段机理 → 毛细压力 master equation → 团聚四理论 → 三大干燥方法族 → 选择规则与安全。

## Mechanism 机理

### Three-period evaporation model (§30.2.1, p.713–714)
- Constant-rate period: pores liquid-filled; contraction rate = evaporation rate; capillary tension low.
- "At the critical point where the constant rate-drying period ends and the first falling rate-drying period begins, the radius of curved liquid is equal to the size of the gel pores... capillary tension reaches maximal value." (p.713)
  → 关键点是一个**力学峰值**而不只是速率拐点；微孔消失、骨架塌缩多发生于此及第二降速段。
- Second falling-rate: evaporation inside the body; asymmetric skeleton compression → deformation.

### Capillary pressure — the master equation (§30.2.2.1, p.714)
"Capillary pressure is the major cause leading to cracking of the gel skeletons or agglomeration of nanoparticles during drying: P = 2σ cosθ / r_p." (Eq. 30.1)
- P ∝ 1/r_p：孔/颗粒半径减半，应力加倍 — 亚微米粉体（SAP fines、纳米纤维素）团聚远比绒毛浆纤维剧烈的定量原因。
- 三条工程杠杆（p.714）：(a) 降 σ — 超临界/冷冻/溶剂置换；(b) θ→90° — 表面改性；(c) 增大并均匀化 r_p（陈化、DCCA 骨架强化）。
- 注意：OCR 中 Eq. 30.1 符号有损（σ 作 "s"、θ 作 "u"），引用前核对印刷版。

### Cracking & agglomeration theories (§30.2.2.2–3, p.714–715)
- Cracking: macroscopic (整体干燥应力) 与 microscopic (孔径不均→局部应力) 两类模型，均不完整。
- Agglomeration 四理论（p.715）：晶桥 / 毛细压力 / 氢键（水中可再分散）/ 化学键。
  "chemical bond theory: nonbridging hydroxyls existing on a nanoparticle surface are the basic sources of hard agglomerates... Me–O–Me group accounts for the formation of agglomerates."
  → 硬团聚不可逆；区分"剪切可再分散"与"永久损失"的判据。原文承认"No generally accepted views"。

## Drying Method Families 干燥方法族 (§30.3, p.717–721)

| Family | Variants | Key quantitative notes |
|---|---|---|
| Direct 直接 | oven / spray / freeze / microwave / supercritical (CO₂) / subcritical / calcining | supercritical CO₂: Tc 31°C, Pc 7.29 MPa (vs water 21.77 MPa) (p.717); microwave 时间 1/10–1/100 无梯度；TiO₂ 煅烧 22.1 nm@450°C → 49.6 nm@900°C (Table 30.3) |
| Solvent replacement 溶剂置换 | MeOH/EtOH/BuOH 洗涤、共沸、CO₂ 置换 | 官能团取代非桥羟基 + 空间位阻防团聚；BuOH 共沸最常用 |
| Modified 改性 | 均匀孔（甲酰胺）、改变挥发顺序（加 DMF）、表面改性（TMCS）、骨架强化（陈化/DCCA） | TMCS 处理后乙醇接触角 30°→78°（Table 30.6，p.721） |

Quality ranking (§30.4, p.722–725): solvent-replacement supercritical > solvent-replacement freeze/microwave > azeotropic > direct oven. 但超临界路线成本/周期高，工业化不成熟（p.724–725）；"agglomeration remains a major challenge" (p.725)。

## Quantitative Evidence 定量证据

"strong capillary pressure pulls the particles into closer contact during oven drying without solvent exchange" — Table 30.4 (p.722–723), TiO₂ (Dong et al.):
- CP1 direct oven: 50–100 nm / 4.88 m²/g
- CP2 ethanol-replacement supercritical: 10–20 nm / 113.8 m²/g
- CP3 ethanol-replacement oven: 20–40 nm / 60.7 m²/g

单一研究显示干燥路线改变粒径 ~5×、比表面积 ~23× — "方法选择（而非仅仅配方）决定纳米结构"的最清晰定量表述。同族对比还有 MgO 7 样品（Table 30.7）、BaTiO₃、RF 凝胶（Tamon），均附 TEM/SSA/孔隙率数据。

## Safety 安全 (p.725)

"nanoparticles are difficult to collect if emitted in air. The fact that they can be easily inhaled or even ingested by the skin is especially worrisome and must be taken into account in the design and operation of any drying process."
→ 吸入/皮肤摄入被列为干燥工艺设计的一阶约束。

## Limitations 局限

- 证据全部为无机氧化物/溶胶-凝胶体系（TiO₂、SiO₂、MgO、BaTiO₃），无 SAP/纤维素/聚合物乳胶案例 — 卫材迁移只能靠类比。
- 毛细方程是等温理想模型，忽略黏弹性骨架弛豫与速率相关模量 — 而这对软水凝胶（SAP）恰恰最重要。
- 团聚机理四理论并存、无单一预测模型（p.715）。

## Hygiene Implication 卫材关联

- **★★★★★ 用 P = 2σ cosθ / r_p 定量估算 SAP 细粉/纳米纤维素团聚风险**：亚微米 r_p 使降速段毛细压力极大。尽量降低 σ（避免纯水脱水场景）和/或提高 θ（疏水化处理）以抑制闪蒸/毛毡脱水中的结块。
- **★★★★ 再分散性取决于键型，先测再下结论**：把观察到的团聚体归类为 H 键/毛细型（剪切可再分散）vs 化学键 Me–O–Me/晶桥型（永久损伤，p.715）；对纳米纤维素/SAP 细粉用温和剪切验证再分散性，不要默认可恢复。
- **★★★★ 保住高比表面积必须换脱水路径**：纳米纤维素/CMC 凝胶需保持高孔隙时，用溶剂置换（EtOH）或冷冻干燥（水结冰膨胀分隔颗粒，p.716），避免直接烘箱干燥塌孔 — Table 30.4 的 5×/23× 差距就是证据。
- **★★★★ θ≈90° 表面改性是常压制备低密度产品的钥匙**：对标 TMCS 处理（θ→~90°，Table 30.6）；SAP 细粉/纳米纤维素疏水化后毛细拉力坍缩，常压干燥也能得气凝胶级蓬松结构。
- **★★★ 关键点=力学峰值**：细颗粒涂层纸幅/垫材干燥中，恒速→降速转折处应力最大（p.713），该处应降低热通量以防微裂纹/塌缩。
- **★★★ 粉尘暴露工程控制**：SAP 细粉/纳米纤维素按可吸入/可皮肤摄入管理（p.725）——密闭脱水与输送、排放收集、PPE。
- 适用性边界：本章无聚合物/纤维素实测数据，以上全部为框架性类比迁移 [待验证 — 需在本厂 SAP 细粉上实测键型与再分散率]。

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch29 Drying of Pharmaceutical Products]]
- [[Industrial Drying Ch33 Drying of Fibrous Materials]]
- [[Industrial Drying Ch35 Drying of Pulp and Paper]]
- [[Industrial Drying Ch41 Drying of Polymers]]

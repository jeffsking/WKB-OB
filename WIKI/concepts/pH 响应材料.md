---
type: concept
title: "pH 响应材料"
domain: [卫材研发, 变色与智能材料]
status: growing
updated: 2026-09-30
tags: [concept, pH-responsive, stimuli-responsive, microgel, polyelectrolyte, wetness-indication, urine-ph]
---

# pH 响应材料
> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.
> ⚠️ Seed digest 中本主题仅有链接条目（无正文摘录）；以下事实取自引用来源页与库内刺激响应聚合物簇的源摘要页，逐条附源。

## Definition 定义
定义待补（引用来源未给出明确定义）。The vault's clearest operational statement is the **microgel mechanism**: `"A pH- and temperature-sensitive microgel can be prepared by copolymerizing NIPAM with acrylic acid."` and `"At a pH value above that of the pKa, the polymer chains of the microgel become ionized, forcing the microgel to adopt a more extended conformation as a result of intramolecular charge repulsion. At a pH below the pKa, the microgel particles adopt a compact structure."`（源：[[Smart Polymers Ch05 Microgels from Smart Polymers]]，lines 636–637、767–771）

## Key Parameters and Data 关键参数与数据
| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Polyacid brush mass-action law 弱聚酸刷电离 | α/(1−α) = K/c_H⁺，c_H⁺ = 10^{−pH}（Eq 2.32） | [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] |
| Weak polyacid pK 弱聚酸 pK 下限 | pK ≥ 4.5 | [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] |
| P2VP brush thickness 刷厚响应 | **22 nm → 7 nm**（pH 3.8 ± 0.5） | [[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]] |
| SPR shift SPR 位移 | ~50 nm | [[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]] |
| Comonomer loading 共聚单体用量 | **1–5% w/w** 即产生显著性能变化（NIPAM + 丙烯酸 → pH/温度双敏） | [[Smart Polymers Ch05 Microgels from Smart Polymers]] |
| Osmotic-pressure balance 渗透压平衡 | Πin + Πel = Πout（Eq 5.1）——pH 响应溶胀的设计式 | [[Smart Polymers Ch05 Microgels from Smart Polymers]] |
| PVA/PAA valve (pH/alcohol) | 循环 **25 s（开）/ 35 s（关）** | [[Smart Polymers Ch08 Smart Hydrogels]] |
| CLC pH-responsive coating 涂层响应方向 | pH↑ → 去质子化 → 溶胀 → **红移** | [[Stimuli-Responsive Photonic Polymer Coatings (ChemComm 2014)]] |

## Method / Mechanism 方法 / 机理
- **Ionization → charge repulsion → expansion 电离驱动伸展**：above pKa the network ionizes and expands by intramolecular charge repulsion; below pKa it collapses to a compact structure（源：[[Smart Polymers Ch05 Microgels from Smart Polymers]]）。
- **Three regimes for pH brushes 刷的三区制**：high ionic strength (α ≈ α_bulk), osmotic annealing (α ∝ [α_b/(1−α_b)·Σc_bj/c]^½), and a nonmonotonic regime at pH ≤ pK — trapped counterions decouple **local pH from bulk pH**（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]，L1380–1445）。
- **Osmotic balance as the design equation 以渗透压平衡作设计式**：Πin + Πel = Πout is the equilibrium relation the vault proposes for a **urine-pH-responsive core**（源：[[Smart Polymers Ch05 Microgels from Smart Polymers]]）。
- **Photonics route 光子学路径**：pH-responsive CLC coatings convert a pH shift into a **visible colour shift**, the same read-out logic as humidity-responsive CLC used for wetness-indicator strips（源：[[Stimuli-Responsive Photonic Polymer Coatings (ChemComm 2014)]]）。
- **Selection rule 选型规则（负面约束）**：`"Precipitation of non-charged thermosensitive polymers shows very low nonspecific coprecipitation of proteins compared with pH-sensitive polymers, where ionic interactions can contribute to the unwanted protein–polymer interactions"` — i.e. charged pH-responsive polymers carry higher non-specific interaction risk（源：[[Smart Polymers Ch13 Affinity Precipitation of Proteins]]，L841–843）。

## Hygiene Relevance 卫材关联
- **Read-out target 读出目标**：pH-responsive CLC coatings are explicitly framed as able to indicate **infection or urine pH change**（源：[[Stimuli-Responsive Photonic Polymer Coatings (ChemComm 2014)]]）。
- **Wetness indication without electronics 无电子湿显**：embedding pH-responsive microgels in the **ADL（导流层）** is proposed, using pH > pKa extension vs pH < pKa compaction plus Eq 5.1, for electronic-free wetness indication（源：[[Smart Polymers Ch05 Microgels from Smart Polymers]]）。
- **Transfer claim 迁移性**：pH-responsive colour change is stated as directly transferable to hygiene wetness indication, alongside waterproof–breathable pore design（源：[[Smart Fabric Textiles Recent Advances and Challenges]]）。
- **Smart adhesive 智能胶**：the frontier is stated as **temperature/pH-responsive smart adhesives** that automatically lower tack on skin, within a roadmap where adhesive is ~**3% of diaper weight**（源：[[Diaper NPD Workshop Prep — Absorbency, Skin Health & Comfort Feature Map（2026-06-05）]]）。
- **Status 研发状态**：pH-responsive colour change sits in the nanocellulose roadmap as **方向八（S3/远期储备）**, explicitly **not yet resourced** until directions 1–5 land（源：[[Nanocellulose Hygiene Application Roadmap（纳米纤维素卫材应用路线图）]]）。
- **体系位置 定位**：本页与 [[PNIPAAM]]、[[刺激响应聚合物 Stimuli-Responsive Polymer]] 同属体温窗口/刺激响应指示剂的候选族（源：[[刺激响应聚合物 Stimuli-Responsive Polymer]]）。

## Open Questions 待补
- `定义待补`：库内无 pH 响应材料的形式化定义与材料清单（弱酸/弱碱基团种类、交联体系）`[待补]`。
- pH 响应窗口与尿液/皮肤 pH 实况的匹配（人体尿液 pH 范围、皮肤酸性膜）在库内未给出可引用数值 `[待补]`；相关但**非同一概念**的页面见 [[Protein Error of pH Dye（pH 染料的蛋白误差）]]。
- 卫材法规（皮肤接触、可迁移物）对 pH 响应组分的约束未在库内成文 `[待补]`。
- 动力学预测能力不足：理论可预测平衡态但动力学仍靠试错（源：[[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]]）→ 响应速率设计 `[待补]`。

## Related Sources 关联来源
- [[Stimuli-Responsive Photonic Polymer Coatings (ChemComm 2014)]] — 引用来源；pH 响应 CLC 涂层
- [[Handbook of Cosmetic Science]] — 引用来源；pH/渗透压与皮肤屏障交叉点
- [[Smart Polymers Ch05 Microgels from Smart Polymers]] — pH/温度双敏微凝胶、Eq 5.1、尿液 pH 响应芯体
- [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] — pH 刷电离-构象耦合与三区制
- [[Smart Polymers Ch08 Smart Hydrogels]] — PVA/PAA pH 阀开关时间
- [[Smart Polymers Ch13 Affinity Precipitation of Proteins]] — 带电 pH 响应材料的非特异相互作用风险
- [[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]] — P2VP 刷响应幅度、动力学瓶颈
- [[刺激响应聚合物 Stimuli-Responsive Polymer]] · [[PNIPAAM]] — 同一功能族
- [[Nanocellulose Hygiene Application Roadmap（纳米纤维素卫材应用路线图）]] · [[Diaper NPD Workshop Prep — Absorbency, Skin Health & Comfort Feature Map（2026-06-05）]] · [[Smart Fabric Textiles Recent Advances and Challenges]] — 卫材落地与状态

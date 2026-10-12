---
type: concept
title: "PNIPAAM"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [concept, PNIPAAm, thermoresponsive, LCST, smart-hydrogel, macroporous, wetness-indication]
---

# PNIPAAM
> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.
> ⚠️ Seed digest 中未给出定义句；以下事实取自引用来源页与库内 Smart Polymers 源摘要页，逐条附源。全库拼写混用 **PNIPAAM / PNIPAAm / PNIPA / pNIPAAM**（同一聚合物）。

## Definition 定义
定义待补（引用来源未给出明确定义）；the closest vault definition is: `"Poly(N-isopropyl-acrylamide) (PNIPAAm) is the most widely studied temperature-responsive polymer. Hydrogels from PNIPAAm exhibit a transition temperature of approximately 32°C in aqueous solution."`（源：[[Smart Polymers Ch08 Smart Hydrogels]]，Lines 65–67）

## Key Parameters and Data 关键参数与数据
| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Transition temperature (hydrogel) 水凝胶转变温度 | **≈ 32 °C** in aqueous solution（最广泛研究的温敏聚合物） | [[Smart Polymers Ch08 Smart Hydrogels]] |
| LCST — brush 刷体系 | **≈ 28 °C**（"transition below body temperature"，作热阀用） | [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] |
| LCST — 涂层口径 | **30–35 °C**，接近体温的天然阈值 | [[Stimuli-Responsive Photonic Polymer Coatings (ChemComm 2014)]] |
| LCST — 原型体系 | **≈ 32 °C**，described as "rather sharp" | [[Smart Polymers Ch12 Polymeric Carriers Regional Therapy]] |
| PNIPAAM 刷行为 | LCST ≈ 32 °C；温度↑ → 脱水坍塌 | [[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]] |
| 大孔 PNIPAAm 溶胀比 SR | **60–80**（对照无孔 ≈ 15） | [[Smart Polymers Ch08 Smart Hydrogels]]（Lines 179–181） |
| PEG 致孔剂 → 孔径 | MW **2000 → 10–20 µm**；**4000 → 30–40 µm**；**6000 → 60–80 µm** | [[Smart Polymers Ch08 Smart Hydrogels]]（Lines 178–186） |
| THF 发泡 PNIPAAm 消溶胀 | **90 s 失水 90%**，约 10 min 达稳定收缩态（常规需数周） | [[Smart Polymers Ch08 Smart Hydrogels]]（Lines 209–215） |
| 辐射交联（γ/电子束） | 消溶胀动力学约为常规的 **100 倍** | [[Smart Polymers Ch08 Smart Hydrogels]]（Lines 405–411） |
| PNIPAAm 颗粒微阀 | **300 ms 开 / ~2 s 关**，~1.5 bar | [[Smart Polymers Ch08 Smart Hydrogels]] |
| 溶胀比定义 | SR = (W_s − W_d)/W_d | [[Smart Polymers Ch08 Smart Hydrogels]]（Lines 158–160） |

## Method / Mechanism 方法 / 机理
- **LCST 相变即开关**：below the transition temperature the network absorbs and retains a large amount of water; above it the hydrogel **shrinks to a dense state and loses much water**（源：[[Smart Polymers Ch08 Smart Hydrogels]]，Lines 67–69）。
- **大孔化 = 快响应**：macroporous hydrogels are defined as having pores **larger than 50 nm**, with deswelling within minutes vs hours-days for conventional gels（源：[[Smart Polymers Ch08 Smart Hydrogels]]，Lines 36–37、54–56）；the governing rule is `"To obtain a fast-responsive hydrogel with macroporous structures, a phase separation must occur during the network formation process."`（源：同上，Lines 88–89）。
- **致孔剂有平台期**：response rate ∝ PEG MW up to ~2000 and **stops improving above MW 2000**（源：[[Smart Polymers Ch08 Smart Hydrogels]]，Lines 188–190）。
- **同一物理机制跨领域复用**：NIPAAM 温敏水凝胶在 **SAP 与光子涂层**中是同一机制（LCST 相变 → 溶胀/收缩），技术可双向迁移（源：[[Stimuli-Responsive Photonic Polymer Coatings (ChemComm 2014)]]）。
- **可做成双敏体系**：copolymerizing NIPAM with acrylic acid 得到 pH + 温度双敏微凝胶（源：[[Smart Polymers Ch05 Microgels from Smart Polymers]]）。

## Hygiene Relevance 卫材关联
- **体温窗口就是阈值**：LCST 落在 30–35 °C / ≈32 °C，是温致变色、温响应涂层的**天然阈值，无需外部加热即可响应体温**（源：[[Stimuli-Responsive Photonic Polymer Coatings (ChemComm 2014)]]）；[[刺激响应聚合物 Stimuli-Responsive Polymer]] 亦记录体温工作窗口 ~37 °C 最有用（源：[[Smart Polymers Ch01 Phase Transitions and Light Scattering]]）。
- **热阀构想**：LCST ≈ 28 °C 的 PNIPAAm 刷层在接触温热皮肤/尿液时坍塌，可作**渗透率热阀**（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]，L628–629）。
- **摄入速率与凝胶阻塞**：大孔化可在保持平衡吸收量的同时压缩液体摄入时间并缓解 [[Gel Blocking（凝胶阻塞）]]；SR 口径与 SAP 常规吸收量 QC 一致（源：[[Smart Polymers Ch08 Smart Hydrogels]]）；芯体设计落点见 [[Baby Diaper Absorbent Core Design（五层无浆 SAP 芯体设计方案与仿真 KPI）]]。
- **回渗方向相反需取舍**：快速消溶胀（THF 体系 90 s 失水 90%）是"表面干爽"的另一条杠杆，方向与吸收相反，须按目标功能取舍（源：[[Smart Polymers Ch08 Smart Hydrogels]]）。
- **⚠️ 皮肤接触警示**：Poly-NIPAAM LCST 约为 32 °C（"rather sharp"），但源文明确称其 **"unsuitable for biomedical use because of its cytotoxicity and non-biodegradability"**（源：[[Smart Polymers Ch12 Polymeric Carriers Regional Therapy]]，L1767–1772）——卫材选型时必须先解决细胞毒性与不可降解问题。

## Open Questions 待补
- **⚠️ LCST 跨源不一致（库内已登记为 [待验证]，本页不裁决）**：Ch01 给出 PNIPA **≈34.9 ± 0.1 °C**、Ch02 给出 PNIPAAm **≈28 °C**、Ch12 给出 poly-NIPAAM **≈32 °C**（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]、[[Smart Polymers Ch12 Polymeric Carriers Regional Therapy]]）。

> ✅ **裁决（2026-09-30，跨源一致多数 + 教科书口径）**：PNIPAM（N-异丙基丙烯酰胺）**均聚物水溶液 LCST 以 ≈32 °C 为库内主口径**（Ch08 / Ch12 / Nature Materials 刷体系三源一致，亦为文献最广引值）。**34.9 °C 与 28 °C 判为体系依赖变体**而非矛盾：LCST 对共聚组成、端基、接枝密度/刷结构、分子量敏感（Ch01 的 34.9 ± 0.1 °C 与 Ch02 刷体系 28 °C 各为其体系实测值），引用时须注明体系条件。两值保留为来源专属口径，不再挂 [待验证]。
- `定义待补`：库内无 PNIPAAM 的化学结构式/分子量口径（M_n、合成路线）引用 `[待补]`。
- 与 [[SAP（高吸水树脂）]] 的定量耦合（交联密度、网孔尺寸 ξ、SR 与 CRC/AUL 口径换算）未在库内成文 `[待补]`；参见 [[Flory- Rehner Theory]]、[[交联密度 Crosslink Density]]、[[CRC 离心保持能力]]。
- 人体尿液离子强度下（如 1.0 M NaCl 级别）的 LCST/溶胀漂移仅有一处数据（15 °C 下 SR ≈70）（源：[[Smart Polymers Ch08 Smart Hydrogels]]，Lines 305–308），卫材实况外推 `[待补]`。

## Related Sources 关联来源
- [[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]] — 引用来源；PNIPAAM 刷 LCST≈32 °C
- [[Stimuli-Responsive Photonic Polymer Coatings (ChemComm 2014)]] — 引用来源；LCST=30–35 °C、SAP 与光子涂层同机制
- [[Smart Polymers Ch08 Smart Hydrogels]] — 转变温度≈32 °C、大孔路线、SR、消溶胀动力学
- [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] — LCST≈28 °C、热阀、χ'(c) 判据
- [[Smart Polymers Ch12 Polymeric Carriers Regional Therapy]] — LCST≈32 °C 与细胞毒性警示
- [[Smart Polymers Ch05 Microgels from Smart Polymers]] — NIPAM + 丙烯酸双敏微凝胶
- [[刺激响应聚合物 Stimuli-Responsive Polymer]] · [[温度响应材料]] · [[Hydrogel-based Superabsorbent Polymers]] — 同族页面

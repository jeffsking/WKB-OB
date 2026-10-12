---
type: concept
title: "SAP 溶胀 SAP Swelling"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [concept, SAP, swelling, CRC, AUL, Flory-Rehner, Donnan, crosslink-density]
---

# SAP 溶胀 SAP Swelling
> 📌 **Page completed 2026-09-30** from 2 citing sources（另经多个库内页面交叉取证，见 Related Sources）。All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义
定义待补（引用来源未给出明确定义）。The vault's operative framing: swelling is set by **two opposing structural levers** — `"when the amount of cross-linking agent increases, the hydrogel becomes less flexible, and the swelling ability is reduced"`，而链亲水性提高溶胀（源：[[Hydrogels in Regenerative Medicine]]）。Hydrogels generally hold **20–100× their own weight** in water, structure-dependent（源：[[Hydrogels in Regenerative Medicine]]）。

## Key Parameters and Data 关键参数与数据
| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Water uptake (general hydrogels) 吸水倍率 | **20–100×** own weight | [[Hydrogels in Regenerative Medicine]] |
| Classification by water content 含水量分级 | low 20–50% / medium 50–90% / high 90–99.5% / **superabsorbent >99.5%** | [[Hydrogels in Regenerative Medicine]] |
| Swelling vs cross-link density 溶胀-交联密度 | **Q_max ∝ 1/ν_c**（交联密度↑ → 溶胀度↓） | [[Smart Polymers Ch14 Hydrogels in Microfluidics]] |
| Response time 溶胀响应时间 | t_resp ~ L²/D_eff（由初始尺寸 L 与有效扩散系数决定） | [[Smart Polymers Ch14 Hydrogels in Microfluidics]] |
| Volume expansion 体积膨胀上限 | 可高达 **1000 倍**（化学→机械转导） | [[Smart Polymers Ch14 Hydrogels in Microfluidics]] |
| Cross-linked CMC absorbency 交联 CMC 吸水率 | **5–25 g/g**（盐水 5–10 g/g）vs 普通浆 1–2 g/g | [[Cross-linked Cellulose and Its Derivatives]]（p. 278） |
| CMC 水不溶性临界 DS | **≈ 0.35–0.40** | [[Cross-linked Cellulose and Its Derivatives]]（p. 278） |
| Q_eq saline @38 ℃（CMC–1.5% CA） | **110 g/g**（商用聚丙烯酸钠 93 g/g） | [[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]] |
| Q_eq DI water @38 ℃ | 164 g/g（CMC–1.5% CA）vs **593 g/g**（商用聚丙烯酸钠，约 3.6×） | [[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]] |
| AUL, 0.9% saline（0.154 M NaCl） | 47.0 g/g（CMC–1.5% CA）vs 27.9 g/g（商用聚丙烯酸钠） | [[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]] |
| Load-induced loss 加压损失率 | 32–39%（CMC–1.5% CA）vs **81.6%**（商用聚丙烯酸钠） | [[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]] |
| pH sensitivity 酸碱敏感性（saline@38 ℃） | pH 5.1 → 106 g/g；pH 6.4 → 110；pH 8.3 → 114 g/g（尿液 pH 4.5–8.5） | [[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]] |

## Method / Mechanism 方法 / 机理
- **Two-lever structure–property relation 双杠杆关系**：charged groups raise hydrophilicity ⇒ higher water absorption, and their **electrostatic repulsion raises solubility and swelling ratio**；pH 响应方向明确——**acid-group hydrogels swell more in basic media**（源：[[Hydrogels in Regenerative Medicine]]）。
- **Hydrophilic groups 亲水基团**：−SO₃H、−COOH、−CONH₂、−OH、−NH₂；三种结构类型——neutral (nonionic)、ionic (polyelectrolyte)、interconnected network（源：[[Hydrogels in Regenerative Medicine]]）。
- **Thermodynamic equilibrium 热力学平衡**：Flory–Rehner equilibrium swelling balances only two opposing forces — `"the thermodynamic force of mixing and the retractive force of the polymer chains"`，ΔG_total = ΔG_elastic + ΔG_mixing；ionic networks add a ΔG_ionic term（源：[[Smart Polymers Ch11 Smart Polymer Drug Delivery]]）。
- **Network language 网络语言**：ξ = υ₂,ₛ^(−2/3)(2C_n·Mc/M_r)^(1/2)·l；lower Mc ⇒ tighter network, higher modulus, **slower uptake**（源：[[Smart Polymers Ch11 Smart Polymer Drug Delivery]]）；另见 [[Flory- Rehner Theory]]、[[交联密度 Crosslink Density]]。
- **Osmotic/Donnan route 渗透压路径**：SAP 溶胀压即交联聚电解质网络的 swelling pressure，由溶剂化学势差设定（源：[[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]]）；另见 [[Donnan 溶胀]]。
- **Ion shielding 离子屏蔽**：Na⁺ 屏蔽电离的 −COO⁻ 基团，**使吸液量相对 DI 水下降三倍以上**（源：[[SAP（高吸水树脂）]]，转引自 [[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]]）。
- **Kinetics toolbox 动力学工具箱**：Crank 的扩散数学（Fick 定律、moving boundaries、non-Fickian）被列为 **SAP swelling kinetics** 的理论基础（源：[[Mathematics of Diffusion]]）；球对称解析解见 [[Diffusion in a Sphere (Crank Ch.6)]]。

## Hygiene Relevance 卫材关联
- **CRC / AUL 口径**：源文指出 §2.4「is, in effect, a general SAP swelling primer」——low/medium/high/superabsorbent (>99.5% water) 分级加上"交联密度压制溶胀、提高刚性"的表述，正是推理 **CRC vs modulus vs absorption-under-load** 的双杠杆关系（源：[[Hydrogels in Regenerative Medicine]]）→ [[SAP性能指标（CRC AUL GBP Vortex）]]、[[CRC 离心保持能力]]、[[AUL 加压吸水率]]。
- **DS 与交联密度是两大控制变量**：DS fixes the solubility ceiling, cross-link density fixes the swelling ceiling；**both must be tuned jointly**（源：[[Cross-linked Cellulose and Its Derivatives]]）。
- **纤维素路线与盐环境取舍**：in DI water commercial polyacrylate is ~3.6× better, but in 0.9% saline the CA-crosslinked cellulose hydrogel slightly exceeds it；该优势是**盐水特异的、非普适的**（源：[[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]]）→ [[Biodegradable SAP（可降解高吸水树脂）]]、[[Sodium Polyacrylate SAP vs Cellulose-Based SAH（成本·性能·供应链）]]。
- **加压下的表现**：cellulose-based SAH 的加压损失更小（32–39% vs 81.6%），是该文对纸尿裤 AUL 最有迁移价值的一条（源：[[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]]）。
- **结构解法对抗凝胶阻塞**：burst-fiber 与 MFC 结构提高表面积、避免 gel-blocking（源：[[Cross-linked Cellulose and Its Derivatives]]，p. 278）→ [[Gel Blocking（凝胶阻塞）]]。

## Open Questions 待补
- `定义待补`：库内无「SAP 溶胀」的形式化定义与标准测试口径（自由溶胀速度、溶胀动力学常数）`[待补]`。
- 吸水倍率口径换算：QC(free swell) / SR / Q_eq / WRV / CRC 之间的关系在库内未统一成文 `[待补]`；参见 [[WRV 水保留值]]。
- **源内数字不一致（照录，不裁决）**：加压试验载荷正文写 ~170 g、图注写 ~320 g；CMC–1.5% CA 加压损失率原文出现 32% 与 39% 两值（源：[[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]]）。
- 交联纤维素 SAH 的实验室结论**不等于商业成熟度或供货能力**，转化评估须独立进行（源页已标 manual_review）。

## Related Sources 关联来源
- [[Diffusion in a Sphere (Crank Ch.6)]] · [[Mathematics of Diffusion]] — 引用来源（SAP 溶胀动力学理论基础）
- [[Hydrogels in Regenerative Medicine]] — 吸水倍率分级、双杠杆关系、pH 响应方向
- [[Smart Polymers Ch14 Hydrogels in Microfluidics]] — Q_max ∝ 1/ν_c、t_resp ~ L²/D_eff、1000 倍体积膨胀
- [[Smart Polymers Ch11 Smart Polymer Drug Delivery]] — Flory–Rehner 平衡溶胀、Mc 与 ξ
- [[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]] — 盐水 AUL 对照数据
- [[Cross-linked Cellulose and Its Derivatives]] · [[Cross-linked Cellulose and Its Derivatives]] — DS×交联密度控制变量、CMC 吸水率
- [[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]] · [[Donnan 溶胀]] · [[Flory- Rehner Theory]] — 驱动力理论
- [[SAP（高吸水树脂）]] · [[SAP性能指标（CRC AUL GBP Vortex）]] · [[Hydrogel-based Superabsorbent Polymers]] · [[吸收芯体]] · [[湿迁移 Wet Migration]] — 库内相邻页面

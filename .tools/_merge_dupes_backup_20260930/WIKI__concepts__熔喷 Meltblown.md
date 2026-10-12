---
type: concept
title: "熔喷 Meltblown"
domain: hygiene-materials
status: growing
updated: 2026-09-30
tags: [nonwoven, meltblown, barrier, backsheet, hygiene-materials]
---

# 熔喷 Meltblown
> 📌 **Page completed 2026-09-30** from 6 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

- 熔喷（meltblown）与纺粘（spunbond）同属**一体化熔融挤出（integrated melt-extrusion）成网工艺**：**树脂分子结构决定工艺窗口，工艺窗口决定纤维架构与终端性能**（卫材 / 医用一次性用品）。（源：[[Polymer-laid web formation]]）
- 熔喷非织造布即 **meltblown nonwoven / 熔喷 PP 纤维（meltblown polypropylene）**，以高速热气流牵伸熔融聚合物形成超细纤维网。（源：[[Coform Composite Nonwoven（熔喷-木浆复合非织造）]]、[[Polymer-laid web formation]]）
- **树脂牌号分野**：纺粘用 ~35 MFR 的 CR 均聚物；熔喷用 **≥500 MFR、窄分子量分布（narrow-MWD）** 牌号 —— 这是熔喷与纺粘在树脂选型上的分界。（源：[[Handbook of Polypropylene and Polypropylene Composites]]）

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 熔喷树脂 MFR | ≥500 MFR，窄 MWD（对照纺粘 ~35 MFR CR 均聚物） | [[Handbook of Polypropylene and Polypropylene Composites]] |
| 无膜背层纤维直径窗口 | 3–10 µm（刻意反向于先行技术的 0.5–2.5 µm） | [[US7195621B2 Disposable Garment Comprising Meltblown Nonwoven Backsheet (P&G)]] |
| 无膜背层模量 | 230–650 gf/mm | [[US7195621B2 Disposable Garment Comprising Meltblown Nonwoven Backsheet (P&G)]] |
| 10 psi 不漏测试 | 3 个实施例通过 | [[US7195621B2 Disposable Garment Comprising Meltblown Nonwoven Backsheet (P&G)]] |
| 1.5 µm 熔喷网阻隔（Laplace 理想孔模型） | ~800 mbar（理想孔模型）vs 实测 40–140 mbar，**高估 15×** | [[Formation-Limited Barrier（阻隔的成形受限机理）]] |
| 模头温度 250 → 300 °C | 模拟直径变化 < 1%（直径不受熔体粘度支配） | [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]] |
| 毛细管停留时间（capillary residence time） | 4–20 ms（熔体其余路径为 480 s） | [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]] |
| 射流速度 150 → 250 m/s | 纤维直径 2.85 → 2.21 µm，随后饱和 | [[Meltblown Nonwoven（熔喷非织造布）]] |
| 单孔产量 0.73 → 0.20 g/hole/min | 固定线产量下 35 → 130 hpi | [[Meltblown Nonwoven（熔喷非织造布）]] |
| 速度匹配距离（velocity-matching） | 2.4 mm（285 °C）；2.7 mm（250 °C） | [[Meltblown Nonwoven（熔喷非织造布）]] |
| 无氟疏水母粒接触角 | 105° → 118–122°，约 +35% 静水压（hydrohead）；成本 3.5 EUR-c/kg | [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]] |

## Method / Mechanism 方法 / 机理

- **阻力限制牵伸（drag-limited attenuation）**：纤维与空气射流达到**速度匹配**后，质量守恒即锁定直径（d ∝ v /(m·Λ·v_a)·…）`[原文残缺]`；**熔体粘度只改变「多快达到匹配」**，不改变最终直径 —— 285 °C 时距模头 2.4 mm、250 °C 时 2.7 mm 达到匹配。（源：[[Meltblown Nonwoven（熔喷非织造布）]]）
- **三个真实杠杆**：降低单孔产量（cut g/hole/min，0.73 → 0.20，固定线产量下对应 35 → 130 hpi）、提高射流速度（150 → 250 m/s 带来 2.85 → 2.21 µm，随后饱和），以及「nothing else」`[原文残缺]`。（源：[[Meltblown Nonwoven（熔喷非织造布）]]）
- **纤维细度不由温度买来**：在工业窗口内纤维直径受**阻力限制**（由单孔产量与射流速度设定，非熔体粘度）；模头温度 250 → 300 °C 使模拟直径变化 < 1%。（源：[[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]]）
- **热解耦（thermal decoupling）**：激光加热只作用于模头尖端，因毛细管把停留时间从 480 s 缩短到 4–20 ms（约 80,000×），**降解剂量 = 速率 × 时间**由此大幅下降 —— 这是激光辅助模头的真正收益。（源：[[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]]）
- **阻隔是「成形受限」的**：支配关系式为 **P ∝ weakest local gsm × γ |cos θ| ÷ fibre diameter**；即表面张力 γ、接触角 θ 与克重均一性**同位阶**，而**最薄处（weakest patch）**才是击穿点 —— 故决定静水压的是**束数与局部克重 CV，而非中值孔径**。（源：[[Formation-Limited Barrier（阻隔的成形受限机理）]]）
- **树脂—工艺—性能链条**：§4.2 先讲聚合物科学（聚烯烃立构：等规 / 间规 / 无规 PP，HDPE / LDPE / LLDPE，PET、PA、TPU；决定可纺性的树脂属性；茂金属单活性中心催化剂革命），随后是熔喷工艺工程（§4.9–4.13 含大量参数 / 建模文献）。（源：[[Polymer-laid web formation]]）

## Hygiene Relevance 卫材关联

- **芯体包裹层（core wrap）**：Coform 把**熔喷 PP 纤维与木浆纤维在同一成形过程中直接复合** —— 木浆提供吸收与蓬松，熔喷纤维提供连续相与强度；原用于湿巾基材，本库关注其在**纸尿裤芯体包裹层**上的迁移可行性。（源：[[Coform Composite Nonwoven（熔喷-木浆复合非织造）]]）
- **无膜背层（film-free backsheet）**：以熔喷无纺布**替代 PE 膜**作为一次性衣物的阻隔 / 透气组件，是"去膜背层"最早且参数最硬的一手出处（四参数窗口 = 纤维直径 / 克重 / 透气度 / 透湿度）。（源：[[US7195621B2 Disposable Garment Comprising Meltblown Nonwoven Backsheet (P&G)]]）
- **SMS / SSMMS 载体**：熔喷是 SMS 复合结构中的阻隔层；纺粘 / 熔喷的 MFR 分野（~35 vs ≥500 MFR）正是 SSMMS 线在两批不同树脂上的采购口径。（源：[[Handbook of Polypropylene and Polypropylene Composites]]、[[SMS复合结构]]）
- **PFAS 隐藏风险**：熔喷布的**驻极助剂（electret aids）**常含含氟电荷俘获剂，是最容易被忽视的隐藏 PFAS 来源；常规质检思路常遗漏，应对方向为驻极助剂专项核查并转向 **C0 无氟体系**，落点是无氟烷基改性聚烯烃母粒。（源：[[SMS复合结构]]）

## Open Questions 待补

- SMS 各层的**克重配比与阻隔性能的定量关系**，本库暂无来源 `[待补]`。（源：[[SMS复合结构]]）
- SMMMS 的**实测（非模拟）静水压**与单束成形 CV 仍缺 `[待补]`。（源：[[SMS复合结构]]）
- **专利范围警示**：US7195621B2 摘要 / SUMMARY 讲的是 backsheet，而**唯一授权权利要求把熔喷网放在弹性腿围（elasticized leg cuff）**上 —— 读范围时须注意 `[待补]`。（源：[[US7195621B2 Disposable Garment Comprising Meltblown Nonwoven Backsheet (P&G)]]）
- 上述数据在来源中的**页码待核** `[待补]`。

## Related Sources 关联来源

- [[Polymer-laid web formation]]（熔喷作为一体化熔融挤出成网；§4.9–4.13 工艺工程）
- [[Handbook of Polypropylene and Polypropylene Composites]]（纺粘 / 熔喷 MFR 树脂分野的一手出处）
- [[Meltblown Nonwoven（熔喷非织造布）]]、[[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]]、[[Laser-Assisted Die Tip（激光辅助模头）]]（牵伸机理与激光加热）
- [[Formation-Limited Barrier（阻隔的成形受限机理）]]、[[Film-Free Backsheet（无膜背层）]]、[[SMS复合结构]]、[[SMS 纺粘熔喷复合]]（阻隔与载体）
- [[Coform Composite Nonwoven（熔喷-木浆复合非织造）]]、[[绒毛浆（Fluff Pulp）]]、[[ADL（导流层）]]（芯体包裹层相关）
- [[US7195621B2 Disposable Garment Comprising Meltblown Nonwoven Backsheet (P&G)]]（无膜背层专利）
- [[ES 纤维热风非织造布驻极性能初探]]、[[驻极体 Electret]]（驻极与 PFAS 议题）
- [[Absorbent Technology]]、[[Fluid Absorption in High Bulk Nonwovens]]、[[Handbook of Nonwovens]]、[[Nonwovens in Absorbent Materials]]（概念并列登记）

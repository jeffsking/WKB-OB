---
type: concept
title: "聚合物刷 Polymer Brush"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [polymer-brush, stimuli-responsive, surface-grafting, polyelectrolyte, LCST, PNIPAAm, SCF-theory]
---

# 聚合物刷 Polymer Brush
> 📌 **Page completed 2026-09-30** from 2 citing sources in the vault. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

**Polymer brushes（聚合物刷） are chains covalently end-grafted to an impermeable surface**（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。

Responsiveness comes from **crowding, not from the single chain**: 「An inherent feature of a polymer brush with high surface coverage is strong intermolecular interaction that governs chain conformation and ensures stimuli-responsive behavior」（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。The high grafting density → excluded-volume chain extension → **conformational change amplified into a macroscopic, measurable change in thickness / wetting / permeability**（源：[[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]]）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Planar-brush scaling 平面刷标度 | 链延伸 **H ∼ N**；刷层平均单体浓度 **c ≅ N/Hs 不随聚合度 N 变化** | [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] |
| Practical response modes 实际响应机制 | 收敛为 **thermosensitive** 或 **ionic pH-sensitive** 两条主线 | [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] |
| PNIPAAM 刷 LCST | **≈32 °C**（Nature Materials 2010）；Ch02 引 **≈28 °C** | [[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]] · [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] |
| PEO / PEG LCST | **≈100 °C** | [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] |
| P2VP 刷厚度变化（pH 响应） | **22 nm → 7 nm**（pH 3.8 ± 0.5） | [[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]] |
| P2VP SPR 位移 | **~50 nm** | [[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]] |
| Polyelectrolyte brush height（osmotic） | **H_osm = 3^{−1/2} α^{1/2} Na** — 与接枝密度无关 | [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] |
| Salted brush height 盐态刷高 | **H ∝ (Σc_bj)^{−1/3}**；v_eff = α²/(2Σc_bj) | [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] |
| Weak polyacid pK | **≥ 4.5** | [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] |
| Surfactant complexation threshold | **CAC < CMC**（协同结合） | [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] |
| Response-time trade-off 响应时间权衡 | 本体聚合物 **分钟~数十小时**；薄膜（<10 μm）**~秒级**（Tanaka-Fillmore t ∝ L²） | [[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]] |

## Method / Mechanism 方法 / 机理

- **Grafting-from beats grafting-to（"从表面长出"优于"接到表面"）**：surface-initiated controlled radical polymerization 避免 "grafting to" 的空间位阻，并实现位置可控的单体嵌入（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。
- **Three theories agree on exponents, disagree on internal structure**：Alexander–de Gennes 标度、mean-field boxlike、self-consistent field（SCF）；只有 SCF 能解出非均匀密度 c(z) 与非均匀链拉伸（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。
- **Collapse modes 塌缩模式**（几何控制，非单链 coil→globule）：渐进式（progressive）、跃变·垂直相分离（jumplike / vertical phase separation）、稀疏接枝下的章鱼状胶束（octopus micelles）、极高接枝密度下保持伸展（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。
- **3D / particle extension（三维延展）**：Pickering 乳液稳定与刺激触发破乳；温敏壳层催化活性开关；空芯 LbL 胶囊 pH / 激光触发释药（源：[[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]]）。

## Hygiene Relevance 卫材关联

- **SAP as a salted polyelectrolyte brush（把溶胀 SAP 当作盐态聚电解质刷）**：(Σc_bj)^{−1/3} 标度与 v_eff = α²/(2Σc_bj) 给出高盐尿液中吸液损失的定量修正；电荷密度 α 与交联点间链长是直接旋钮（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。
- **Thermoresponsive gating 热响应阀**：PNIPAAm 的 LCST 低于皮肤温度 37 °C → 刷层接触温热皮肤/尿液即坍塌，可作渗透调节的热阀；PEO（LCST ≈ 100 °C）在体温下保持稳定亲水涂层（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。
- **pH / urinalysis stripes 尿液分析显色条**：弱聚酸（PAA/PMAA）指示层的标定曲线为 α/(1−α) = K·10^{pH}，pK ≥ 4.5；pH ≤ pK 附近的非单调溶胀可在尿液 pH ≈ 6 附近放大信号（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。
- **Surfactant contamination 表面活性剂污染**：因 CAC < CMC，湿巾/沐浴残留表面活性剂会在阈值以上协同结合并使刷状涂层增塑 → 预判 SAP 吸收漂移与胶黏 tack 损失（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。
- **Durable functional coatings 耐久功能涂层**：grafting-from 路线可在无纺布/薄膜上做抗菌、防污、抗炎响应表面（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。
- ⚠️ Note 注：库内**无**把聚合物刷直接用于吸收芯体 / ADL 的实测数据 — 芯体关联仍属**建模级**接口（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。

## Open Questions 待补

- PNIPAAM 的 LCST 口径冲突（Ch01 ≈34.9 °C / Ch02 ≈28 °C / Nature Materials ≈32 °C）未解决 — `[待验证]`（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。
- 全部定量陈述按行号（L-numbers）引用，印刷页码不可得 — `[待验证]`（源：[[Smart Polymers Ch02 Responsive Polymer Brush Theory]]）。
- 动力学（响应速率）预测能力不足，工业「设计→制造→验证」仍需大量试错（源：[[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]]）。
- 聚合物刷与吸收芯体 / ADL 的直接性能关联：库内无证据 `[待补]`。

## Related Sources 关联来源

- [[Emerging Applications of Stimuli-Responsive Polymer Materials (Nature Materials 2010)]] — 唯一引用来源
- [[Smart Polymers Ch02 Responsive Polymer Brush Theory]] — 聚合物刷理论主来源
- [[刺激响应聚合物 Stimuli-Responsive Polymer]] · [[PNIPAAM]] · [[pH 响应材料]] · [[水凝胶 Hydrogel]]
- [[LbL 自组装 Layer-by-Layer]] · [[Hydrogel-based Superabsorbent Polymers]] · [[Acrylic-Based Superabsorbent Polymers]]

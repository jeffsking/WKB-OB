---
type: source
title: "PCM-Free Thermoregulation with BNC Nanofiber Network"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/BNC_PCMfree_Thermoregulation_v1_20260731.pptx.md
original_link: ""
date_published: 2026-07-31
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "Thermoregulation decomposes into four separable physical functions — insulation, buffering, dissipation and spike absorption — and 3 of the 4 are structural, not chemical（调温可分解为四个可分离的物理功能：隔热、缓冲、散热、尖峰吸收；其中 3 项是结构性的、非化学的）"
  - "BNC nanofiber network insulates at aerogel levels: ≈90% porosity, k ≈0.035 W/m·K, specific surface area ≈150 m²/g（BNC 纳米纤维网达到气凝胶级隔热：孔隙率约 90%、导热系数约 0.035 W/m·K、比表面积约 150 m²/g）"
  - "BNC-only cuts the initial skin-side warming rate by ≈58% versus control and reaches the same steady state as BNC+PCM; the PCM plateau is the only marginal advantage（仅用 BNC 可使贴肤侧初始升温速率较对照下降约 58%，并与 BNC+PCM 收敛到同一稳态；PCM 的相变平台是其唯一的边际优势）"
  - "Microcapsules cost ≈$0.008–0.015/unit plus 15–40 gsm of added basis weight, while BNC-only adds 0 gsm and no leakage risk; net saving ≈$0.006–0.011/unit（微胶囊增加约 $0.008–0.015/件、15–40 gsm 克重，而纯 BNC 方案零额外克重、无泄漏风险；净节省约 $0.006–0.011/件）"
  - "PCM-free is the default, gated path — not a universal answer: BNC-only lags PCM by ≈1–2 min in the first-window ΔT and cannot lock a setpoint（无 PCM 是默认的、带门路线而非万能答案：纯 BNC 在首窗 ΔT 上落后 PCM 约 1–2 分钟，且无法锁定恒定温度点）"
pages_linked: ["[[PCM-Free Thermoregulation]]", "[[Diaper Microclimate]]", "[[细菌纳米纤维素]]", "[[BNC-Only vs BNC+PCM (Thermoregulation Ledger)]]", "[[毛细梯度设计]]", "[[REL增强层]]", "[[分区密度设计]]", "[[热风粘合无纺布]]"]
---

# PCM-Free Thermoregulation with BNC Nanofiber Network

## One-line positioning 一句话定位

The **"remove the microcapsules" feasibility review**: engineered bacterial-nanocellulose (BNC) nanofiber networks as a standalone thermal-management layer for absorbent hygiene products, with no phase-change chemistry. It is the batch's cost-and-mechanism counterweight to microcapsule-based thermal comfort, and the bridge between [[细菌纳米纤维素]] and [[Diaper Microclimate]].
本页是**「去掉微胶囊」的可行性评审**：以工程化细菌纳米纤维素（BNC）纳米纤维网络作为吸收性卫生用品的独立调温层，完全不使用相变化学。它是本批针对微胶囊路线的**成本—机理对照页**，也是 [[细菌纳米纤维素]] 与 [[Diaper Microclimate]] 之间的桥梁。

## Summary 摘要

The problem is framed as "**the microcapsule tax**": phase-change microcapsules solve a heat spike and then charge for it four times over — every gram is paid for in **mass** (+gsm, +cost per unit, every cycle), **risk** (shell fragility → rupture and lot variance; broken capsules contaminate SAP and widen process control limits), **liquid leakage** (free PCM raises skin risk and worsens rewet/odour) and **complexity** (a specialty encapsulation tier is added to the supply chain with inventory and QA burden and, being petro-shell, a microplastic/sustainability burden).
问题被概括为**「微胶囊税」**：相变微胶囊解决一次热尖峰，却要为此付四次账——**质量**（每件每周期增加克重与成本）、**风险**（壳脆→破裂与批次波动；破裂胶囊污染 SAP 并放宽工艺控制限）、**液体泄漏**（游离 PCM 提高皮肤风险、恶化回渗与气味）、**复杂度**（供应链多出一层脆弱的专用封装环节，含库存与 QA 负担，且石化壳体带来微塑料/可持续性负担）。

The function decomposition then shows that thermoregulation is **four separable physical functions**: insulation (resist conductive heat flow, high R-value), buffering (raise thermal mass so dT/dt is slow), dissipation (move heat out via evaporative and radiative pathways) and spike absorption (absorb a discrete thermal event at a setpoint via latent heat). For multi-hour wear, comfort is a **steady-state** problem — insulation + buffering + dissipation — and spike absorption only matters for the first ~60 s after a warm void. **Three of the four functions are structural, not chemical.**
功能分解随后表明调温是**四个可分离的物理功能**：隔热（阻导热电、高 R 值）、缓冲（提高热质量使 dT/dt 变慢）、散热（通过蒸发与辐射通路移热）、尖峰吸收（在设定点以潜热吸收一次热事件）。对多小时穿着，舒适是**稳态**问题——隔热 + 缓冲 + 散热——尖峰吸收仅在温热排液后的最初约 60 秒有意义。**四项功能中有三项是结构性的，而非化学的。**

BNC's thermal behaviour is presented as a direct consequence of its nanofiber geometry: ≈85–95% porosity trapping still air (k_air ≈ 0.026 W/m·K); nano-pores ≈20–200 nm sitting near the air mean free path (≈68 nm) producing Knudsen suppression of gas-phase conduction; a point-contact fibril network (τ ≈ 1.5–3) minimising solid conduction paths plus phonon boundary scattering; a hydroxyl-rich surface whose bound water adds sensible-heat thermal mass; and a nanofiber mat that scatters IR radiation (low-emittance path). It adds two dissipative loops: bound-water sensible buffering (slows dT/dt without latent heat) and evaporative dissipation (moisture-vapour transmission sheds heat when wet).
BNC 的热行为被表述为其纳米纤维几何的直接结果：约 85–95% 孔隙率封存静止空气（k_空气 ≈0.026 W/m·K）；约 20–200 nm 的纳米孔接近空气分子平均自由程（约 68 nm），产生 Knudsen 气相传导抑制；点接触纤维网络（τ ≈1.5–3）最小化固相传导路径并带来声子边界散射；富羟基表面的结合水提供显热热质量；纳米纤维垫散射红外辐射（低发射率通路）。另加两个耗散回路：结合水显热缓冲（不靠潜热即降低 dT/dt）与蒸发散热（湿态下经水汽传递散热）。

## Extracted numbers and conclusions 提炼的数字与结论

### BNC structure and thermal data (`≈` = literature-derived estimates) BNC 结构与热数据

| Item 项目 | Value 数值 | Note 备注 |
|---|---|---|
| Fibril ribbon width 纤维带宽度 | ≈50–100 nm | Schematic, not to scale |
| Inter-fibre pore size 纤维间孔径 | ≈20–200 nm | ≈ air mean free path (≈68 nm) → Knudsen effect |
| Porosity 孔隙率 | ≈85–95% (headline ≈90%) | Trapped still air k ≈0.026 W/m·K |
| Specific surface area 比表面积 | ≈100–200 m²/g (headline ≈150) | — |
| Contact type 接触类型 | Point contact (τ ≈ 1.5–3) | Minimal solid conduction path |
| Water-holding 持水 | ≈100× dry mass | — |
| Effective thermal conductivity 有效导热系数 | **≈0.035 W/m·K** | Aerogel-level; PCM microcapsules raise k by adding solid shell mass (slightly worse insulation) |
| Thermal-conductivity series 导热系数序列 | still air 0.026 · BNC ≈0.035 · also listed 0.045 / 0.055 / 0.060 for the BNC+PCM / fluff pulp / SAP gel / solid cellulose series | ⚠️ Bar-to-series mapping ambiguous in extraction — treat individual values as `[待验证]` |
| Initial skin-side warming rate 贴肤侧初始升温速率 | **−58% dT/dt vs control** (model) | BNC-only; all three curves converge to the same steady state |
| PCM energy density PCM 能量密度 | latent ≈100–200 J/g | vs BNC sensible (low) |
| PCM added basis weight PCM 增加克重 | +≈15–40 gsm | BNC-only: 0 gsm |

### BNC-only vs BNC + PCM ledger 全账本对比

| Dimension 维度 | BNC-only | BNC + PCM microcapsules |
|---|---|---|
| Mechanism 机理 | Structure-intrinsic | Latent-heat additive |
| Functions covered 覆盖功能 | Insulation + buffering + dissipation | + spike absorption |
| Energy density 能量密度 | Sensible (low) | Latent ≈100–200 J/g |
| Added basis weight 增加克重 | 0 (uses existing BNC) | +≈15–40 gsm |
| Unit cost add 单位成本增加 | 0 | +≈$0.008–0.015 |
| Leakage / rupture risk 泄漏/破裂风险 | None | Shell fragility |
| Supply chain 供应链 | Simpler (cellulose) | Multi-supplier |
| Sustainability 可持续性 | Flushable, bio-based | Petro-shell, microplastic risk |
| Setpoint precision 设定点精度 | None (structural) | Sharp at Tm |
| Verdict 结论 | Redundant for steady-state comfort → **the default** | Marginal for transients only |

### Honest limits 诚实的边界

1. **Transient spike absorption** — BNC-only lags PCM by ≈1–2 min in the first-window ΔT (model, indicative).
2. **Setpoint precision** — no sharp isothermal hold at Tm; regulation is rate-based, not temperature-locked.
3. **Above-window performance** — above the setpoint PCM contributes nothing extra either, so the gap is bounded, not open-ended.

### Design compensation (close the gap by structure, not chemistry) 结构补偿

1. Z-direction porosity gradient (dense skin / lofty core) — slows skin-side dT/dt further, builds on REL work.
2. Higher BNC basis weight in the skin-facing zone — adds sensible thermal mass where it matters.
3. Bound-water management (humectant tuning) — extends the buffering window past the void event.
4. Breathable backsheet + ADL synergy — evaporative dissipation offsets the acute spike.
5. REL reinforcement layer — mechanical robustness with no extra gsm.
*Net result: PCM-free parity is achievable within the current cellulose material set — no new chemistry required.*

### Economics 经济性

| Item 项目 | Add-on 增量 | $/unit |
|---|---|---|
| PCM microcapsules | +15–40 gsm | ≈$0.008–0.015 |
| Shell / encapsulation overhead | — | ≈$0.001–0.003 |
| QA / lot-variance buffer | — | ≈$0.001 |
| BNC-only upgrade (structure) | repurpose existing BNC | ≈$0.002–0.004 |
| **Net saving 净节省** | — | **≈$0.006–0.011** |

Headline: net saving ≈$0.01/unit ≈ **0.6–0.9% of BOM**; at ≈10⁹ units/yr the removed line-item is worth **≈$6–11 M/yr** before counting QA and complexity savings.

### Feasibility verdict and gates 结论与门

- **RECOMMENDED · BNC-only (steady-state)** for multi-hour microclimate comfort. Gate: AUL/CRC ≥ current; rewet ≤ current; skin-model ΔT/dt ≤ target.
- **NOT ALONE · BNC-only (acute spikes)** — needs structural compensation. Gate: gradient + evaporative DOE passes wear trial.
- **FALLBACK · BNC + PCM hybrid** — only if gates fail. Gate: cost-acceptable at scale; otherwise iterate structure.
- Validation roadmap: P1 material characterisation (k_eff, DSC bound water, SSA; k_eff ≤0.04) → P2 bench thermal tests (guarded hot plate + skin-model dT/dt) → P3 product integration DOE (porosity gradient + breathable synergy; AUL/CRC/rewet hold) → P4 wear trial / manikin (comfort parity vs PCM baseline).

> ⚠️ **估算而非实测（原文自述）**：deck 明确声明"All numeric values in this deck are literature-derived estimates (≈) for hypothesis support. Replace with internal test data at the Gate stages."

## Key claims 关键论断

- **Four functions, three of them structural** — microcapsules address only the fourth —— 支撑页：[[PCM-Free Thermoregulation]]
- **Insulation at aerogel level is a geometry effect** (porosity + Knudsen + point contact) —— 支撑页：[[细菌纳米纤维素]]
- **For multi-hour wear, PCM is redundant; for transients it is marginal** —— 支撑页：[[BNC-Only vs BNC+PCM (Thermoregulation Ledger)]]
- **The compensation levers are the same structures the REL/capillary work already develops** —— 支撑页：[[毛细梯度设计]]、[[REL增强层]]、[[分区密度设计]]

## Related pages 关联页面

- Concepts 概念：[[PCM-Free Thermoregulation]]、[[Diaper Microclimate]]、[[细菌纳米纤维素]]、[[毛细梯度设计]]、[[分区密度设计]]、[[REL增强层]]、[[热风粘合无纺布]]
- Comparisons 对比：[[BNC-Only vs BNC+PCM (Thermoregulation Ledger)]]
- Sibling sources 同批来源：[[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]、[[Diaper Microclimate Visualization Feasibility (Dual-MVP)]]

## Original 原文

- Local path 本地路径：`RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/BNC_PCMfree_Thermoregulation_v1_20260731.pptx.md`
- Original link 原文链接：（无；内部项目材料）
- Literature base 文献基础：Heath et al. *Cellulose* 27 (2020) k ≈0.03–0.05; Zhao et al. *ACS Sustain. Chem. Eng.* 9 (2021) Knudsen effect; Kaviany *Principles of Heat Transfer in Porous Media*; Müller et al. *Carbohydr. Polym.* 215 (2019) bound water; Sharma et al. *Appl. Therm. Eng.* 204 (2022) PCM microcapsules in hygiene; KC IPC internal REL feasibility study 2026.

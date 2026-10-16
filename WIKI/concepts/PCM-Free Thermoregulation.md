---
type: concept
title: "PCM-Free Thermoregulation"
domain: [卫材研发, 变色与智能材料]
status: growing
updated: 2026-09-29
tags: [PCM, 相变, BNC, 调温, 隔热, 结构补偿, 成本]
aliases: ["PCM-Free Thermoregulation 无 PCM 结构调温"]
---

# PCM-Free Thermoregulation 无 PCM 结构调温

> **Definition 定义**：Achieving multi-hour diaper microclimate comfort by **structural** means alone — insulation, sensible buffering and evaporative dissipation built into the cellulose/nanofiber layer — **without** phase-change (PCM) microcapsules.（仅以**结构**手段实现多小时尿裤微气候舒适——把隔热、显热缓冲与蒸发散热建进纤维素/纳米纤维层，**不使用**相变（PCM）微胶囊。）

## Function decomposition 功能分解

Thermoregulation is **four separable physical functions**, not one trick:（调温是**四个可分离的物理功能**，而非一个技巧：）

| Function 功能 | Physics 物理含义 | Structural or chemical? |
|---|---|---|
| Insulation 隔热 | Resist conductive heat flow (high R-value) | **Structural** |
| Buffering 缓冲 | Raise thermal mass so temperature changes slowly (low dT/dt) | **Structural** |
| Dissipation 散热 | Move heat out — evaporative and radiative pathways | **Structural** |
| Spike absorption 尖峰吸收 | Absorb a discrete thermal event at a setpoint via latent heat | Chemical (PCM) |

For multi-hour wear, comfort is a **steady-state** problem (insulation + buffering + dissipation); spike absorption matters only for the first **~60 s** after a warm void. **Three of the four functions are structural.**（多小时穿着的舒适是**稳态**问题（隔热 + 缓冲 + 散热）；尖峰吸收仅对温热排液后最初约 **60 秒**有意义。**四者中有三项是结构性的。**）

## The BNC mechanism 结构实现路径

A bacterial-nanocellulose (BNC) nanofiber mat suppresses every conductive/radiative route and adds two dissipative loops:（BNC 纳米纤维垫抑制所有传导/辐射路径，并增加两个耗散回路：）

1. **Solid conduction** — point-contact fibril skeleton (τ ≈1.5–3) minimises solid path + phonon boundary scattering.
2. **Gas conduction** — nano-pores ≈20–200 nm sit near the air mean free path (≈68 nm) → **Knudsen suppression**.
3. **Radiation** — nanofiber mat scatters IR; low-emittance tortuous path.
4. **Convection** — sealed, sub-mm pores block air movement within the layer.
5. **Loop A · bound-water sensible buffering** — hydroxyl-bound water raises thermal mass and slows dT/dt **without latent heat**.
6. **Loop B · evaporative dissipation** — moisture-vapour transmission through the porous mat sheds heat when wet.

## Honest limits 诚实的边界

> **PCM-free is the default, not the universal, answer.** 无 PCM 是默认路线，而非万能答案。

1. **Transient spike absorption** — no latent plateau; BNC-only lags PCM by **≈1–2 min** in first-window ΔT (model, indicative).
2. **Setpoint precision** — no sharp isothermal hold at Tm; regulation is **rate-based, not temperature-locked**.
3. **Above-window performance** — above the setpoint PCM contributes nothing extra either, so the gap is **bounded, not open-ended**.

## Design compensation 结构补偿（用结构而非化学补差）

1. Z-direction porosity gradient (dense skin / lofty core) — slows skin-side dT/dt further.
2. Higher BNC basis weight in the skin-facing zone — adds sensible thermal mass where it matters.
3. Bound-water management (humectant tuning) — extends the buffering window past the void event.
4. Breathable backsheet + ADL synergy — evaporative dissipation offsets the acute spike.
5. REL reinforcement layer — mechanical robustness with no extra gsm.

## Key parameter table 关键参数表

| Parameter 参数 | Value 典型值 | Source 出处 |
|---|---|---|
| Effective thermal conductivity 有效导热系数 | ≈0.035 W/m·K (BNC); ≈0.026 W/m·K still air | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| Porosity 孔隙率 | ≈85–95% (headline ≈90%) | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| Specific surface area 比表面积 | ≈100–200 m²/g | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| Fibril ribbon / pore 纤维带宽 / 孔径 | ≈50–100 nm / ≈20–200 nm | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| Initial skin-side warming rate 贴肤侧初始升温速率 | **−58% dT/dt vs control** (model) | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| PCM comparison PCM 对照 | +≈15–40 gsm, +≈$0.008–0.015/unit, latent ≈100–200 J/g, shell fragility | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| Net saving 净节省 | ≈$0.006–0.011/unit; ≈0.6–0.9% of BOM; ≈$6–11 M/yr at 10⁹ units/yr | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| Recommended gate 推荐门 | AUL/CRC ≥ current; rewet ≤ current; skin-model ΔT/dt ≤ target | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| Validation path 验证路径 | P1 k_eff (≤0.04) + DSC bound water + SSA → P2 guarded hot plate + skin-model dT/dt → P3 porosity gradient DOE (AUL/CRC/rewet hold) → P4 wear trial / manikin | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |
| Fallback 兜底 | BNC + PCM hybrid only if gates fail; otherwise iterate structure | [[PCM-Free Thermoregulation with BNC Nanofiber Network]] |

> ⚠️ **No unsourced parameters 禁止无来源参数**：本页所有数值均为**文献推导估算（≈）**，原文自述"Replace with internal test data at the Gate stages"；库内无 BNC 调温层的实测 k_eff、DSC 与 ΔT/dt 数据，标 `[待验证]`。

## Adjacent concepts 相邻概念

- Material platform 材料平台：[[细菌纳米纤维素]]、[[纳米纤维素（CNC、CNF、BNC）]]
- Application 应用：[[Diaper Microclimate]]、[[REL增强层]]、[[智能尿裤功能层]]
- Compensation levers 补偿杠杆：[[毛细梯度设计]]、[[分区密度设计]]、[[热风粘合无纺布]]
- Cost frame 成本框架：[[Microencapsulation]]
- Comparison 对比：[[BNC-Only vs BNC+PCM (Thermoregulation Ledger)]]

## Lessons learned 经验教训

> ✅ **Validation（2026-09-29）**：本来源与既有 [[细菌纳米纤维素]] 页结论**一致**——BNC 的价值在"结构/网络"，不在替代吸收材料；本页新增的是**热管理维度的功能分解与定量对照**（四功能、−58% dT/dt、≈$0.006–0.011/件净节省）。既有结论未被修正。

- **要点**：调温评估应先问"**这是稳态问题还是瞬态问题**"——多小时穿着属稳态，结构性手段（隔热+缓冲+散热）覆盖其中 3/4 功能。
- **风险**：结构路线的短板是**瞬态与设定点精度**（落后 PCM 约 1–2 分钟、无恒温平台），因此需要结构补偿组合而非单一材料。
- **待补 `[待验证]`**：BNC 调温层的产线可制造性（含水凝胶干燥塌孔约束）；真实穿着条件下的舒适度等效性。

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · X-Chromic 目录副本：四条热通路与三条残余差距）

> 追加来源 `[[BNC PCM-Free Thermoregulation v1（无微胶囊温控·细菌纳米纤维素）]]`（同一 deck 的 `Resources/Open Innovation/Material/X-Chromic/` 副本，v1 / 2026-07-31）。本段**只补"热通路机理与诚实边界"，不改动上方任何结论**。
> ⚠️ **同文档异路径**：该 deck 另有 `Projects/Thermal Comfort/` 副本（`[[PCM-Free Thermoregulation with BNC Nanofiber Network]]`，即上方主来源）。两副本**并列保留**，引用须注明路径。

### 1. 四条热通路 + 两个消散回路（本批补全的机理层）

| 通路 / 回路 | 机制 |
|---|---|
| **1 · 固相导热** | 点接触骨架最小化固相路径 + **声子边界散射** |
| **2 · 气相导热** | 纳米孔 ≈20–200 nm 通过 **Knudsen 效应**抑制气相导热（≈空气平均自由程 ≈68 nm） |
| **3 · 辐射** | 纳米纤维毡散射 IR；低发射率曲折路径 |
| **4 · 对流** | 亚毫米封闭孔**阻断层内空气运动** |
| **Loop A · 结合水感热缓冲** | 富羟基结合水提高热质量 → **不用潜热**即可减缓 dT/dt |
| **Loop B · 蒸发消散** | 湿态下透湿通过多孔毡排热 |

- **结构 → 热性能五条映射**：① ≈90% 孔隙率 → 捕获静止空气（k_air ≈0.026）；② 纳米孔 ≈ 空气 MFP → Knudsen 抑制；③ 点接触 → 最小固相路径；④ 富羟基 → 大感热热质量；⑤ 纳米纤维毡 → IR 散射。
- **BNC 结构参数**：ribbon **≈50–100 nm**；孔 **≈20–200 nm**；孔隙率 **≈85–95%**；SSA **≈100–200 m²/g**；tortuosity **τ ≈1.5–3**；持水 **≈100× 干重**。
- 出处：多孔介质传热理论（Kaviany；Zhao et al.）。

### 2. ⚠️ 三条残余差距（"诚实限制"，且**有界**）

| # | 差距 | 量化 | 边界 |
|---|---|---|---|
| 1 | **瞬态尖峰吸收** | 无潜热平台；BNC-only 在第一窗口 ΔT **落后 PCM ≈1–2 min**（模型） | 仅最初 ~60 s 有意义 |
| 2 | **设定点精度** | 无 Tm 处锐利等温保持；BNC 调节是**速率型（rate-based）**，非温度锁定 | — |
| 3 | **超窗口表现** | 超出设定窗口后 **PCM 同样无额外贡献** | ⇒ **差距是有界的，不是开放式** |

> 源件原话框架："*PCM-free is the default, not the universal, answer*"（去 PCM 是默认解，不是通用解）。

### 3. 用结构而非化学补差距（五条杠杆，与三条差距 1:1 对应）

1. **Z 向孔隙率梯度**（致密贴肤侧 / 蓬松芯侧）→ 进一步减缓皮肤侧 dT/dt（承接既有 REL 工作）；
2. **贴肤区提高 BNC 克重** → 在关键处增加感热热质量；
3. **结合水管理（保湿剂调节）** → 把缓冲窗口延伸到排尿事件之后；
4. **透气背层 + ADL 协同** → 用蒸发消散抵消急性尖峰；
5. **REL 增强层** → 不增 gsm 前提下提供机械鲁棒性。
> **净结论**：PCM-free 的对等性**可在现有纤维素材料集内实现，无需新化学**。

### 4. 验证路线 P1–P4（本批新增）

| 阶段 | 内容 | Gate |
|---|---|---|
| P1 材料表征 | k_eff、DSC 结合水、SSA | **k_eff ≤ 0.04**；结合水 ≥ 目标 |
| P2 台架热测试 | 防护热板 + 皮肤模型 ΔT/dt | **ΔT/dt ≤ 目标 vs 对照** |
| P3 产品集成 DOE | 孔隙率梯度 + 透气协同 | **AUL / CRC / 回渗保持** |
| P4 试穿 / 假人 | 真实使用舒适度评估 | **舒适度与 PCM 基准对等** |

> ✅ 验证（2026-09-29）：本追加段**未修正**上方任何结论（四功能分解、−58% dT/dt、≈$0.006–0.011/件净节省均未被改动）；本批补的是**热通路机理、三条残余差距的有界性、五条结构补偿杠杆与 P1–P4 Gate**。上方 `[待验证]` 项（产线可制造性、真实穿着等效性）**在本批仍未闭环**，但 P4 试穿 Gate 已给出闭合路径。
> 🔴 **manual_review（2026-09-29）**：本源含 **$/unit 级成本拆解、BOM 占比（0.6–0.9%）与年化金额（≈$6–11 M/yr @10⁹ units/yr）**。依 AGENTS.md §5，本页**只记量级与结构判断，不落成本模型与定价结论**；全部数值为**文献推导估算（≈）**，须在 Gate 阶段以内部实测替换。

## Sources 来源

- [[PCM-Free Thermoregulation with BNC Nanofiber Network]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/BNC_PCMfree_Thermoregulation_v1_20260731.pptx.md`
- [[BNC PCM-Free Thermoregulation v1（无微胶囊温控·细菌纳米纤维素）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/X-Chromic/BNC_PCMfree_Thermoregulation_v1_20260731.pptx.md`（2026-09-29 追加）

## Related Sources 关联来源

- [[BNC PCM-Free Thermoregulation v1（无微胶囊温控·细菌纳米纤维素）]]
- [[Diaper Market Claims and Marketing Concept Landscape（市场宣称与营销概念全景）]]
- [[GHC 福建冠泓·冠和 公司介绍（KC 2026）]]
- [[New Core Concepts and Claims Draft（芯体新概念与市场宣称草案·8 概念）]]
- [[PCM-Free Thermoregulation with BNC Nanofiber Network]]

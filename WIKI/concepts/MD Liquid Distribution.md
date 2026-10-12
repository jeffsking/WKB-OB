---
type: concept
title: "MD Liquid Distribution"
domain: [卫材研发, 面层结构]
status: growing
updated: 2026-09-29
tags: [MD铺展, 各向异性, 面层, 取向, Liner, 侧漏]
aliases: ["MD Liquid Distribution 机向液体铺展"]
---

# MD Liquid Distribution 机向液体铺展

> **Definition 定义**：How far liquid is carried **along the machine direction (MD)** of a carded nonwoven before it is absorbed, expressed as a spread length or spread percentage. It is the metric that shaped/fine-fibre designs are bought for, and it is **directional by construction** — an isotropic metric will systematically under-report their value.（液体在梳理非织造布上被沿**机向（MD）**输送的距离，用铺展长度或铺展百分比表征。它是以异形/细旦纤维设计所"购买"的指标，且**天然具方向性**——用各向同性指标评估会系统性低估其价值。）

## Mechanism 机理

1. **Carded webs are anisotropic by construction（梳理网的各向异性来自工艺）**：fibres are laid with a partial MD orientation, so the pore network is not isotropic. MD:CD orientation ratio can be tuned by the doffer-to-condenser draft on each card.（纤维带有部分 MD 取向，孔径网络各向异性；MD:CD 取向比可由各梳理的道夫—凝聚牵伸调节。）
2. **Two levers, one drum（两个杠杆，同一个锡林）**：raising MD alignment buys MD wicking **and** removes CD-oriented fibre spans at the same time — the two objectives pull against each other **only if both cards do the same job**.（提高 MD 取向同时带来 MD 芯吸并减少 CD 取向纤维跨距——**只有当两张梳理承担同一职责时**，两个目标才互相拉扯。）
3. **Decoupled card duties（双梳理职责解耦）**：card 1 (top) low draft ≈2:1 MD/CD to carry CD tensile and cross-web integrity; card 2 (bottom) high draft ≈4:1 MD/CD to buy MD wicking — with the skin-side card chemically identical to today.（第 1 梳理低牵伸 MD/CD≈2:1 承担 CD 拉伸与横向完整性；第 2 梳理高牵伸 ≈4:1 换取 MD 芯吸；贴肤侧梳理化学组成与现状完全一致。）
4. **Secondary prize（次要收益）**：CD spread narrows as MD spread grows → an expected measurable drop in side-leak incidents at equal core geometry. The thing to watch is the front approaching the core ends (188 mm on a 385 mm core) — re-check leg-cuff and end-seal wicking.（MD 铺展增长时 CD 铺展会收窄 → 等芯体几何下侧漏事件预计可测下降。需关注前沿接近芯体端部（385 mm 芯体上达 188 mm），复核腿围与端封芯吸。）
5. **What it does *not* change（不会改变什么）**：first-insult strike-through is set by pore size, not by cross-section or orientation.（首次穿透由孔径决定，与截面或取向无关。）

## Key parameter table 关键参数表

| Parameter 参数 | Value 典型值 | Source 出处 |
|---|---|---|
| Modelled MD spread after 3rd insult 第三次冲击后模拟 MD 铺展 | 145 mm (all-ES) / 163 mm (Option A, 15% trilobal) / 188 mm (Option B, 26%) | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Expected MD benefit (25 gsm star PET) 预期 MD 收益 | +15–25% at P10 vs control (simulated) | [[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]] |
| Expected MD gain (rounded trilobal / 4-groove) | ~+10–25% | [[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]] |
| Directional coupling 方向耦合 | MD/CD orientation ≈2:1 (card 1) and ≈4:1 (card 2) | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| MD spread acceptance gate 验收门 | ≥34% (anchor 34.9%, D_aniso = 3); D_aniso target ≥2.5 | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Modelling anchor 建模锚点 | v11 KB: SAP utilization 63.6%, MD spread 34.9% (D_aniso = 3) | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Measurement set 测量集合 | MD/CD wicking length, horizontal spread area, liquid front speed, core stain map | [[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]] |
| Tuning levers 调优杠杆 | Card draft, cut length (longer = longer uninterrupted groove), crimp (crimp bends the groove out of MD) | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Web build anchor 网面构造锚点 | Fine-over-coarse stacking puts the highest capillary suction at the skin — an inverted Z-gradient | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |

> ⚠️ **No unsourced parameters 禁止无来源参数**：上表数值均为**模拟或设计门限**，本批未提供产线实测 MD 铺展数据，实测值标 `[待验证]`。

## Adjacent concepts 相邻概念

- Mechanism 机理：[[Groove Capillary Suction]]、[[毛细梯度设计]]
- Carriers 载体：[[三叶形截面纤维（Trilobal Fibre）]]、[[Pentagram PET (Star Cross-Section Fibre)]]、[[ATB双梳理面层（Dual-Card Topsheet）]]
- Dosage frame 剂量框架：[[Shaped PET Add-On Window]]
- Adjacent layers 相邻层：[[ADL（导流层）]]、[[REL增强层]]
- Acceptance 验收：[[芯体测试方法与验收基准（STM）]]

## Lessons learned 经验教训

> ✅ **Validation（2026-09-29）**：本批四份 Liner 来源一致把 MD 铺展作为面层改良的**主收益指标**，并把"网面取向 + 亲水整理"与"纤维截面"并列为三个控制项（[[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]]、[[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]]、[[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]]、[[ATB Topsheet with Bico Spunbond for 600 mpm Ultrasonic Lamination]]）。与既有 [[三叶形截面纤维（Trilobal Fibre）]] 页"收益是方向性的"判断一致，未出现矛盾。

- **要点**：评估 MD 收益时必须同时读 **CD 铺展与回渗**——MD 变好但 CD 变窄、回渗变差，等于把问题从漏液换成了湿感。
- **待补 `[待验证]`**：本批 MD 铺展增益全部为模型值；产线实测（含 385 mm 芯体端部效应）缺失。

## 追加：Open Innovation 批（2026-09-29 追加 · v11 仿真给出的 MD 铺展量化边界）

> 追加来源 `[[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]`（2026-07-08）。本段**只补"MD 铺展在吸收模型侧能被推到多高、以及它的理论上限是什么"，不改动上文任何面层侧结论**。

### 1. MD spread 的三档结果与理论上限

| 场景 Scenario | 结构 | D_aniso | **MD spread** | SAP 利用率 |
|---|---|---|---|---|
| **Uniform（凝胶阻塞基准）** | 均匀无分层 | 1 | **0.9%** | 48.1% |
| ML+Drain | 4 层 ADL + 8 层 Core，仅排水 | 1 | **31.9%** | 63.6% |
| **ML+Xdiff（最优）** | 同上 + ADL 横向扩散 | **3** | **34.9%** | 63.6% |
| — | **理论极限** | — | **36.7%** | — |

- **理论极限的口径**：**(Nx − inj)/Nx = 21/30 = 36.7%** —— 即**注入区之外的网格占比**。⚠️ 这是**网格离散口径的极限，不是物理极限**，引用时须带口径。
- **提升倍数**：**0.9% → 34.9%，约 38 倍**；其中**分层的贡献远大于横向扩散**（31.9% 来自"垂向均匀分到 8 层 Core 后的固有分散"，横向扩散只再加了 **3.0 pp**）。

### 2. ⚠️ D_aniso 的稳定边界（不要把数值边界读成最优值）

| D_aniso | MD spread | 质量误差 | 稳定性 |
|---|---|---|---|
| 1（各向同性） | 31.9% | −0.014 mL | OK |
| **3（推荐）** | **34.9%** | −0.014 mL | **OK** |
| 10 | 40.0% | **+1,374 mL** | **不稳定** |
| 30 | 36.9% | **+4,229 mL** | **不稳定** |

- **D_aniso = 3 是显式方案的稳定上限**，**≥10 即发散**（ADL 层 k = 5e-11 产生 D_cap ≈ 3e-4 m²/s，通量限制器每步 40% 不足以维持稳定）。
- **D_aniso ≥ 10 的两个 MD spread 值（40.0% / 36.9%）来自不稳定运行，不可作为有效结果引用。**
- **改进方向**：隐式/半隐式（Crank-Nicolson）扩散方案，方可支持 D_aniso ≥ 10。

### 3. 与上文的关系：方向一致，但**仍未闭环**

| 上文（面层侧） | 本批（吸收模型侧） |
|---|---|
| 把 **MD 铺展**作为面层改良的**主收益指标**；三个控制项为"网面取向 + 亲水整理"与"纤维截面" | 把 **MD spread** 作为**结构方案**的主收益指标；控制项为**分层 + ADL 排水 + 横向扩散** |
| ⚠️ **"本批 MD 铺展增益全部为模型值；产线实测缺失"** | ⚠️ **本批同样是模型值**：参数**未实验标定**（Brooks-Corey 取自文献），**实验验证（ISO 11948）仍在 P2 待办** |

> ✅ **同向、非冲突**：面层侧与芯体侧**都把 MD 铺展当作第一收益指标**，且**都受"模型值待实测"的同一限制**。本追加段**不改变**上文的 `[待验证]` 状态——**产线实测仍然缺失**。

### 4. ⚠️ 上文"要点"在本批仍未被检核

- 上文要点：**"评估 MD 收益时必须同时读 CD 铺展与回渗"**。
- 本模型为 **2D（MD × Z）**，**无 CD 维度**（3D 扩展在 P2），**且无 rewet 模型**（P0 待办）。
- **结论**：**本批无法检核"MD 变好是否伴随 CD 变窄或回渗变差"** —— 上文的警告**依然有效且未被闭合**。

> 🔴 **manual_review（2026-09-29）**：本源为自研仿真报告，**无实验标定与实验验证**；本页**只记方向与相对比较，绝对数值不得作为产品性能数据引用**。

## 追加：Open Innovation 批（2026-09-29 追加 · v9 的网格收敛警示：MD 扩散与 SAP 利用率随网格分辨率大幅变化）

来源：[[2D Absorption Model v9 Red-Teaming Optimization Report（二维吸收模型v9红蓝对抗优化报告）]]（2026-06-10，自研仿真，未实验验证）。

### 1. ⚠️ 同一模型、同一物理参数，换网格后 MD 扩散与 SAP 利用率双双改变

| 指标 | Coarse 15×6（dx=6.67 mm）| Fine 30×12（dx=3.33 mm）| 中文 |
|---|---|---|---|
| **MD 扩散 [%]** | **3.5** | **2.3** | MD 铺展 |
| **SAP 利用率 [%]** | **97.8** | **57.8** | SAP 利用率 |
| 自由液体最终 [mL] | **2.6** | **0.0** | 残液 |
| 计算可信度（源文）| **低（数值扩散严重）** | **高（网格收敛）** | 可信度 |

> ⚠️ **源文结论（原文）**：*"在 15×6 粗网格下，**约 30 个百分点的 SAP 利用率来自数值扩散而非真实物理扩散**。这意味着如果直接使用粗网格结果指导产品设计（如 **SAP 用量优化**），可能会**过高估计材料利用率，导致实际产品吸收性能不达标**。建议以 **30×12（或更高分辨率）作为仿真基准**。"*

### 2. 对本页既有结论的关系（**不修正，只加约束**）

- 上文 v11 追加给出的 **MD spread 0.9% → 34.9%（理论极限 36.7%）** 是 **v11 模型**的结果；本批 v9 给出 **3.5% → 2.3%**。两者**代次不同、网格不同（v11 为 8 层结构）**，**本页并列不换算**。
- ⚠️ **两条共同的方法论约束**：① **MD 铺展数值是网格依赖的**，引用时必须带**网格分辨率**；② **"网格收敛"在本系列中尚未确认** —— v9 源文自身建议再试 **60×24**。
- **方向一致**：v9 与 v11 都显示**细化网格后 MD 铺展下降**（v9：3.5%→2.3%；v11 的 34.9% 为**理论极限**而非细网格实测）—— **"粗网格高估铺展"这一方向在两代模型间一致**。

> ✅ 验证（2026-09-29）：本追加段**未修正**本页任何既有结论；上文"MD 铺展三档""理论极限 36.7% 为网格口径""D_aniso 稳定边界"**均未被触及**，本批补的是**网格分辨率对 MD 铺展与 SAP 利用率的双重影响**。
> 🔴 **manual_review（2026-09-29）**：源文为**自研仿真报告（未实验验证）**；本页**只记相对关系与量级**，**不作产品设计判定**；**图数据存在内部不一致（2.3 vs 2.5），引用以正文汇总表为准**。

## Sources 来源

- [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/Trilobal_PET_Liner_MD_Distribution.pptx.md`
- [[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/pentagram_PET_diaper_liner_deep_dive 1.pptx.md`
- [[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/pentagram_free_shaped_PET_alternatives_8slides.pptx.md`
- [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/KC_Diffusion_Enhanced_Topsheet_v3.xlsx.md`
- [[ATB Topsheet with Bico Spunbond for 600 mpm Ultrasonic Lamination]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/ATB_topsheet_600mpm_ultrasonic_8slides.pptx.md`

---

## 追加：Open Innovation 批（2026-09-29 追加 · v8：粗网格下的「87% 利用率」与 v9 网格收敛警示的交叉检验）

> 追加来源：[[2D Absorption Model v8 Simulation Report（二维吸收模型 v8 仿真报告）]]（`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/2D_v8_模拟结果完整报告.pdf.md`，2026-06-08，网格 **15×6**）。
> **本追加不修正上文任何结论**；上文已有 v11（MD spread 34.9%、利用率 63.6%）与 v9（网格收敛警示）两段，此处补入**被 v9 点名批评的「15×6 粗网格」正是 v8 所用网格**这一事实——**v8 的绝对值须按 v9 的结论打折理解**。

### 追加-1 · v8 的原生结果（15×6 网格）

| 指标 | v8（15×6） | 备注 |
|---|---|---|
| **SAP 利用率** | **87%（78/90 单元）** | 报告的核心结论：**1D 高估 13%** |
| **MD 铺展** | **±40 mm（±6 切片）** | 覆盖 15 格中的 12 格 |
| 吸收量 / 质量误差 | 201 mL（100.5%）/ ~0 mL | 守恒闭环 |
| 50% / 80% 吸收时间 | 9.5 s / 16.0 s | — |
| 终态自由液 | 3.99 mL（1.9%） | — |
| 毛细扩散系数 D_cap | **1e-9 m²/s（常数）** | ±40 mm 铺展约需 **30 s** |

### 追加-2 · ⚠️ 与 v9 网格收敛警示的交叉检验（**本追加的关键**）

上文 v9 追加给出的源文结论是：*"在 **15×6 粗网格**下，**约 30 个百分点的 SAP 利用率来自数值扩散而非真实物理扩散**……建议以 **30×12（或更高分辨率）作为仿真基准**。"

> ⚠️ **直接推论**：**v8 所用的正是 15×6 网格**，因此其 **87% 的 SAP 利用率中，有相当部分可能来自数值扩散**。按 v9 的量级提示，**v8 的「真实」利用率可能显著低于 87%**。
>
> **本页不裁决具体数值**，但给出**引用约束**：
> 1. **v8 的 87% 不可直接用于 SAP 用量优化**——它很可能是**粗网格的数值假象**；
> 2. **v8 的 ±40 mm MD 铺展同样是网格依赖量**，且 v9 显示**细化网格后铺展下降**（3.5% → 2.3%）⇒ **v8 的铺展值应视为上界**；
> 3. **v8 唯一不依赖网格分辨率的稳健结论是「质量守恒已闭环」（误差 ~0 mL）** —— 这是数值方法正确性，不是物理量。

### 追加-3 · 三代模型的网格—利用率对照（并列，不换算）

| 版本 | 日期 | 网格 / 结构 | SAP 利用率 | MD 铺展 | 本页备注 |
|---|---|---|---|---|---|
| **v8** | 2026-06-08 | **15×6**（单层口径） | **87%** | ±40 mm（±6 切片） | **受 v9 的粗网格警示覆盖** |
| **v9** | 2026-06-10 | 15×6 vs 30×12 对比 | 97.8% → 57.8%（换网格后**降 40 个百分点**） | 3.5% → 2.3% | 源文自陈「约 30 个百分点来自数值扩散」 |
| **v11** | 2026-07-08 | 8 层结构，30×? 口径 | 63.6% | 34.9%（理论极限 36.7%） | 上文已有 |

> 📌 **方向一致性检查**：v9 与 v11 均显示**细化网格/改进结构后铺展与利用率下降**；v8 的 87% 处在**最高位**，与「粗网格高估」的方向**一致**。三代**不可互相换算**（网格、层数、参数均不同），仅作趋势参照。

### 追加-4 · v8 对 MD 铺展机理的独立贡献（**不受网格问题影响的部分**）

1. **铺展速度瓶颈在 D_cap**：`D_cap = 1e-9 m²/s` 下 ±40 mm 需 **~30 s**；原文明确"**更快的输运需要更高的 k0 或更低的 μ**" ⇒ **MD 铺展不能靠延长时间解决，只能改渗透率或黏度侧**。
2. **D_cap 为常数是已知缺陷**：原文 §7 建议改为由 `k/μ · dPc/dSw` 计算 ⇒ 上文的 D_aniso 校准议题（v11）与此处**同源**。
3. **边缘旁通**：最外侧 2 个切片（各 6.7 mm）240 s 时近乎零吸收 ⇒ 与 [[Core Channel Pattern（芯体通道花型设计）]] 的"横向导流槽不超出 pad 边缘、预留数毫米"**互相呼应**——**边缘既不能浪费（未激活 SAP），也不能成为旁通通路**。

> ✅ 验证（2026-09-29）：本追加段**未修正**本页任何既有结论；上文「MD 铺展三档」「理论极限 36.7% 为网格口径」「D_aniso 稳定边界」均未被触及，本批补的是**v8 与 v9 网格警示之间的交叉检验**。

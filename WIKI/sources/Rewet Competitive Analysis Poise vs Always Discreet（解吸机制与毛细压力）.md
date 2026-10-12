---
type: source
title: "Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）"
source_type: 提案
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Poise Rewet/Rewet Competitive Analysis - POISE and ALWAYS DISCREET-1.pptx.md
original_link: ""
date_published: 2025-11-20
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "回渗由两种机制驱动——解吸（Desorption）与回流（Flowback）；在 POISE 的 FIUP 测试中，**解吸主导回渗**，且解吸机制由摄入系统（intake system）控制"
  - "解吸机理：摄入系统中的高毛细压力与界面会截留液体，被截留的液体在受压时表达为回渗"
  - "反直觉实测结果：ALWAYS DISCREET 的摄入系统（Liner+Surge、Liner、Surge 三个层面）毛细压力都**显著高于** POISE，按机理应回渗更高，但实测并未被 POISE 大幅拉开"
  - "毛细压力数据（Bn-abs1 / Bn-des1）：Liner+Surge POISE 3.54 / 11.58 vs AD 8.58 / 22.60；Liner POISE 3.22 / 14.90 vs AD 6.02 / 18.84；Surge POISE 3.22 / 10.38 vs AD 5.62 / 24.39"
  - "更难解吸的双重原因：Young-LaPlace Δp = −2γcosθ/R —— AD 的**模态孔径更小**且**润湿性更高**（滴液润湿性 Liner：POISE 2.4→4.7 vs AD 8.4→9.5；Surge：POISE 8.4→9.2 vs AD 9.6→9.8）"
  - "BET 比表面积：AD Core 17.48 m²/g（六层复合：composite 1-胶-SAM 1-中层 NW-胶-SAM 2-composite 2）vs POISE Core 仅 1.37 m²/g（绒毛浆 + SAM）；AD 单层 composite 达 56.25 / 47.57 m²/g，SAM 颗粒仅 0.70 m²/g"
  - "三个解释性假说（未证实）：① AD surge 与 liner 等长等宽（POISE surge 仅 50 mm 宽、长度约为护垫一半）② AD surge 芯吸好，可能反而降低回渗 ③ 高比表面积材料的作用未知"
  - "⚠️ AD 芯材中两层内的涂层与球形结节（coating and spherical nodules）**尚未被鉴定**；SEM 提问「是否为 HIPE 泡沫？若是，孔在哪里？」——未解答"
pages_linked: ["[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]", "[[Intake System（摄入系统）]]", "[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]", "[[Rewet Test（回渗测试）]]", "[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]", "[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]", "[[The Procter & Gamble Company（宝洁）]]", "[[Kimberly-Clark（金佰利）]]", "[[ADL（导流层）]]", "[[IPC BCC OI Portfolio（开放创新项目组合）]]"]
---

# Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）

## 一句话定位

**POISE（K-C）vs ALWAYS DISCREET（P&G）的回渗竞品机理分析（英文）**：用 BET 比表面积、毛细压力（吸收/解吸）、孔径分布、润湿性、Micro-CT 与 SEM 五种手段，回答"**为什么 POISE 在回渗测试中没有碾压 AD**"。本库价值：给出**回渗的两种机制划分（解吸 vs 回流）**与**摄入系统控制解吸**这一因果链，是本库 [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]] 的**竞品实证来源**。

## 摘要

**机制划分**：回渗由**两种机制驱动——解吸（Desorption）与回流（Flowback）**；在 **POISE 的 FIUP 测试中，解吸主导回渗**。解吸机制**由摄入系统（intake system）控制**：摄入系统中的**高毛细压力与界面会截留液体**，被截留的液体**在受压时表达为回渗**。机理要素为：解吸毛细张力 / 界面 / 回渗 / 液体可得性 / 润湿性 / 与芯体的分离 / 双向流动。

**反直觉的核心发现**：按机理，AD 的摄入系统毛细压力显著更高 → **应表现出更高回渗**；但**实测中 POISE 并未在回渗上碾压 AD**。原文自设问题："*Why is POISE not crushing ALWAYS DISCREET in rewet tests?*"

**三层毛细压力实测（Bn = 特征毛细压力）**：

| 层位 | 产品 | Bn-abs1 | Bn-des1 | 吸收能（ergs） | 解吸能（ergs） | 平均克重 | G/g abs1 |
|---|---|---|---|---|---|---|---|
| **Liner + Surge** | Poise | **3.54** | **11.58** | 5.79E+03 | 1.92E+04 | 77.72 | 12.47 |
| | Always Discreet | **8.58** | **22.60** | 7.57E+03 | 1.78E+04 | 79.39 | 6.29 |
| **Liner** | Poise | **3.22** | **14.90** | 9.09E+02 | 3.69E+03 | 25.07 | 5.87 |
| | Always Discreet | **6.02** | **18.84** | 1.69E+03 | 4.96E+03 | 19.22 | 8.49 |
| **Surge** | Poise | **3.22** | **10.38** | 4.40E+03 | 1.41E+04 | 56.82 | 14.08 |
| | Always Discreet | **5.62** | **24.39** | 4.35E+03 | 1.67E+04 | 58.07 | 7.75 |

**为什么 AD 更难解吸（Young-LaPlace）**：`Δp = −2γ·cosθ / R` —— 两个因素同时作用：① **孔径 R 更小**（AD liner 与 surge 的**模态孔径**均明显小于 POISE）；② **润湿性更高（接触角 θ 更小）**。滴液润湿性测试（0 s → 60 s）：**Liner POISE 2.4 → 4.7 vs AD 8.4 → 9.5**；**Surge POISE 8.4 → 9.2 vs AD 9.6 → 9.8**。

**BET 比表面积（结构性差异最大的一项）**：

| 组分 | Unscented Discreet（m²/g） | Poise（m²/g） |
|---|---|---|
| BSL（面层） | 2.22 | 1.53 |
| Surge（导流层） | 1.43 | 1.87 |
| **Core（芯体）** | **17.48**（六层复合：composite 1 - 胶 - SAM 1 - 中层 NW - 胶 - SAM 2 - composite 2） | **1.37**（绒毛浆 + SAM） |

- AD 进一步拆分：**Core 1 复合层 56.25**、**Core 2 复合层 47.57**、**Core 1/2 的 SAM 颗粒（带胶涂层）仅 0.70**。→ **AD 的高比表面积来自复合层（composite），不是来自 SAP 颗粒**。

**Micro-CT（10 cm / 0.14 psi 受压下）**：**两个面层都没有被很好地解吸**，但 **AD 的 surge 非常湿**。

**三个解释性假说（原文自列，未证实）**：① 尺寸差异——POISE surge 蓬松度约为 AD 的 2 倍但**易解吸**；**AD surge 与 liner 等长等宽**，而 POISE surge 仅 **50 mm 宽**（芯体最窄处 80 mm）、长度约为护垫的一半（6-drop long）；② **AD surge 芯吸好，是否反而降低回渗？** ③ **高比表面积材料的作用是什么？**

**未鉴定项**：SEM 显示 AD 芯材的**涂层（coating）与球形结节（spherical nodules）**——关键问题"**涂层与结节是否同一材料？是否为 HIPE 泡沫？若是，孔在哪里？**"**尚未解答**。

## 提炼的数字与结论

| 项目 | 数值 / 结论 | 备注 |
|---|---|---|
| 机制划分 | **解吸 + 回流**；**POISE 的 FIUP 中解吸主导** | 解吸由摄入系统控制 |
| Liner+Surge 特征 Pc（abs/des） | POISE **3.54 / 11.58** vs AD **8.58 / 22.60** | AD 约 2× |
| Liner 特征 Pc | POISE **3.22 / 14.90** vs AD **6.02 / 18.84** | AD 更高 |
| Surge 特征 Pc | POISE **3.22 / 10.38** vs AD **5.62 / 24.39** | AD 解吸压力约 2.3× |
| 滴液润湿性（0→60 s） | Liner：POISE **2.4→4.7** vs AD **8.4→9.5**；Surge：POISE **8.4→9.2** vs AD **9.6→9.8** | AD 更润湿 |
| 孔径 | AD liner 与 surge **模态孔径更小** | 孔径分布图对比 |
| **BET Core** | AD **17.48** vs POISE **1.37 m²/g** | **约 12.8×** |
| BET 拆分（AD） | composite 1 **56.25**；composite 2 **47.57**；SAM 颗粒（带胶）**0.70** | **高比表面积来自复合层** |
| BET BSL / Surge | AD 2.22 / 1.43；POISE 1.53 / 1.87 | Surge 侧 POISE 更高 |
| 蓬松度 | **POISE surge 约为 AD 的 2 倍** | 但更易解吸 |
| 覆盖度 | **AD surge = liner 等长等宽**；**POISE surge = 50 mm 宽、约半个护垫长** | 关键结构差异 |
| Micro-CT @10 cm（0.14 psi） | 两个 liner 都未很好解吸；**AD surge 非常湿** | — |
| ⚠️ 未鉴定 | AD 芯材的**涂层与球形结节**未鉴定；HIPE 泡沫假说未验证 | SEM 5000× |

> ⚠️ **credibility 高但结论未闭合**：本资料为 K-C 内部竞品分析（一手实测），但**核心问题（为何 POISE 未碾压 AD）未获解答**——原文只列出三个假说与两个未鉴定项，**不得当作结论引用**。

> 🔴 **manual_review（2026-09-29）**：本资料为 **K-C 竞品拆解内部分析**，含**竞品（P&G Always Discreet）结构拆解、SEM/Micro-CT 图像结论与未鉴定材料推测**。依 AGENTS.md §5，本页**只记机理、参数与已公开的方法学事实**，**不落竞品配方推断与未鉴定材料的定性结论**（HIPE 泡沫假说仅作"未验证问题"登记）；**不外发**。

## 关键论断（key_claims）

- **回渗 = 解吸 + 回流两种机制；POISE 的 FIUP 中解吸主导** —— 支撑页：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]
- **解吸由摄入系统控制：高毛细压力与界面截留液体，受压时表达为回渗** —— 支撑页：[[Intake System（摄入系统）]]
- **AD 的摄入系统毛细压力全面更高（更难解吸），按机理应回渗更高——但实测未如此 ⇒ 机理与实测之间存在未解释的缺口** —— 支撑页：[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]
- **更难解吸是双重原因：更小孔径 + 更高润湿性（Young-LaPlace 的 R 与 θ 同时作用）** —— 支撑页：[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]
- **AD 芯体 BET 比表面积约为 POISE 的 12.8×，且高比表面积来自复合层而非 SAP 颗粒** —— 支撑页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- **"蓬松度"与"解吸难易"是两回事：POISE surge 蓬松度 2× 于 AD 但更易解吸** —— 支撑页：[[Resilient Surge（PET 回弹导流层）]]、[[ADL（导流层）]]

## 关联页面

- 概念：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]、[[Intake System（摄入系统）]]、[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]、[[Rewet Test（回渗测试）]]、[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]、[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]、[[ADL（导流层）]]、[[Resilient Surge（PET 回弹导流层）]]、[[Formation-Limited Barrier（阻隔的成形受限机理）]]
- 实体：[[The Procter & Gamble Company（宝洁）]]、[[Kimberly-Clark（金佰利）]]
- 源：[[Rewet Method Comparison（回渗测试方法横向对比·K-C vs P&G）]]、[[FIUP Insult Amounts（FIUP 加液量阶梯与 TL 溯源）]]、[[Depend Rewet Update 2025-04-04（LUGH 与 GRIFFIN 回渗进展）]]
- 对比：[[Rewet Method Comparison（回渗测试方法横向对比）]]
- 组合：[[IPC BCC OI Portfolio（开放创新项目组合）]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Poise Rewet/Rewet Competitive Analysis - POISE and ALWAYS DISCREET-1.pptx.md`
- 原文链接：（无；K-C 内部竞品分析，2025-11-20）
- 汇报人：Richmond Cohen、Matt Valaskey、Kaiyuan Yang、Dave Biggs、Paul Smith、Almon Benton
- 后续步骤（原文）：探索 micro-CT 条件（吸水纸与替代物）以关联竞品回渗实验；经分析科学鉴定 AD 的 surge 与 liner 材料；鉴定 AD airlaid 中浆纤维上的涂层与结节并判断是否影响回渗；做 X 射线分析查明 AD surge 优异铺展能力与回渗的关联；分析 liner 与 surge 之间的界面间隙

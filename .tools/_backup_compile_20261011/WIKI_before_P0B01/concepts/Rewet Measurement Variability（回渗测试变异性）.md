---
type: concept
title: "Rewet Measurement Variability（回渗测试变异性）"
domain: [卫材研发, 回渗, 测试方法]
status: growing
updated: 2026-09-30
tags: [回渗, 测试变异, 干厚度, 批次差异, 统计口径]
---

# Rewet Measurement Variability（回渗测试变异性）

> 一句话定义 One-line definition：回渗（rewet）读数在**批次（lot）之间**与**测试请求（test request）之间**都会发生**统计显著**的漂移，且该漂移与产品的**干厚度（dry thickness）**同向变化——因此回渗比较必须在同一干厚度口径下进行，否则"改善"可能只是厚度差。

## 机理 / 结构拆解 Mechanism and Structure

1. **两类变异源并存**：① **批次间**——同一机台生产的两个批次就有差异；② **测试请求间**——同一 RSR（retained sample）产品在不同 LabVantage 请求中复测也会差异。二者叠加后，单次读数的可比性很弱。
2. **与干厚度耦合**：进一步分析显示不同批次/请求间存在明显的**干厚度差异**，且**厚者回渗高**。干厚度因此成为回渗的**混淆变量（confounder）**，而非噪声。
3. **对判读的直接影响**：若两组样品干厚度不同，则回渗差异可能全部（或部分）由厚度贡献，而非材料或结构方案；这与 [[Pore Size Distribution Monodispersity（孔径分布单分散性）]] 中"克重驱动解吸能"是同一类问题的两种表现——**材料体积（厚度/克重）是回渗的一阶量**。
4. **统计口径**：本批所有对比均以 **Tukey-Kramer 0.05** 分组（A/B/C 字母标记），这是本库回渗数据的默认显著性口径。
5. **治理方向**：把干厚度作为**分层变量或协变量**纳入测试设计（配对取样、同厚度分层比较），而不是事后用均值比较。

## 关键参数表 Key Parameters

| 参数 Parameter | 典型值 / 范围 Typical Value | 出处 Source |
|---|---|---|
| 批次间回渗差异（同机台两批次） | 0.39 g vs 0.35 g（L14 - DPU2 M, Female，(101) vs (126)） | [[GRIFFIN Regroup - Depend Rewet Update（GRIFFIN 重整更新 · 2025-08-28）]] |
| 对应干厚度差异 | 7.04 vs 5.96 | 同上 |
| 测试请求间回渗差异（同一 RSR） | 0.44 g（Old）vs 0.36 g（New） | 同上 |
| 对应干厚度差异 | 7.45 vs 6.08 | 同上 |
| 统计口径 | Tukey-Kramer 0.05（A/B/C 分组） | 同上 |
| 市售竞品分组（对照） | Always Discreet 0.19 g（B）< Depend Fresh Protect 0.31 g（A）< Assurance 0.36 g（A） | 同上 |
| 面层方案在多轮测试中的幅度波动 | 0.44→0.35 / 0.36→0.33 / 0.28→0.25（三轮 R25 请求） | 同上（LUGH 12 gsm Fibertex vs 对照） |

> ⚠️ **禁止无来源参数 No unsourced numbers**：表中数字均来自上列源摘要页；干厚度与回渗之间的**定量斜率**、以及厚度公差带内回渗的敏感系数库内暂无来源，标 `[待验证]`。

## 相邻概念 Adjacent Concepts

- 上位：[[Rewet Test（回渗测试）]]、[[Dryness Measure System（干爽度量三分）]]
- 机理：[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]、[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]
- 同源问题（材料体积作为一阶量）：[[Pore Size Distribution Monodispersity（孔径分布单分散性）]]、[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- 表征方法：[[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]、[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]
- 项目：[[GRIFFIN Rewet Program（GRIFFIN 超低回渗项目）]]、[[LUGH Liner Program（LUGH 面层项目）]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[GRIFFIN Regroup - Depend Rewet Update（GRIFFIN 重整更新 · 2025-08-28）]]）：本页为原文明确提出的独立问题（"Rewet can vary significantly between lots and test requests"），并由两组配对数据（批次、测试请求）与干厚度共同佐证；尚无第二条独立来源，故 `status: seed`。

- **教训一（先配平厚度再谈改善）**：任何面层/导流层方案的回渗改善，都要先确认两组样品干厚度一致，否则可能只是"薄了所以看起来好"。
- **教训二（幅度比方向更可信）**：LUGH 12 gsm Fibertex 在三轮测试中方向一致（均低于对照）但幅度波动（−0.09 / −0.03 / −0.03），说明**方向可复现、幅度不可复现**，汇报时应给区间而非单点。
- **教训三（复测要同 RSR）**：同一 RSR 在两次请求中回渗差 0.08 g，提示跨请求比较需以同一保留样做锚。
- **待补 `[待验证]`**：干厚度→回渗的定量敏感系数；厚度公差范围内回渗的允许波动带；是否应对干厚度做统计协变量校正。

## Evidence Update 证据追加（2026-09-29 · 测试路径可翻转显著性）

> ✅ Verification（2026-09-29，source 来源 [[GRIFFIN Female DPU2 AT Hybrid Rewet Summary（女性 DPU2 AT Hybrid 回渗总结）]]）：本页"回渗读数在批次与测试请求之间漂移"的判断得到**更强的同类证据**——漂移不只改变**幅度**，还能**翻转统计显著性判定**。

1. **新增变异源：测试路径（lab routing）**——同一批样品分两套：一套在 **GADT 实验室**测，另一套按研究要求走 **LabVantage 研究放行（Study Release）**；补充的 GADT 结果在**约 2.5–3 个月后**才测得。
   - AT Hybrid dSB 550 g：GADT **0.30750 g** vs Study Release **0.40875 g**（Std Error 0.02249），**95% CI 下显著不同**。
   - SAM/Fluff Control：GADT **0.23000 g** vs Study Release **0.20775 g**，方向**相反**（路径使对照略降、使 AT Hybrid 明显升）。
2. **显著性被路径翻转（最关键的判读风险）**——**Study Release 口径下各代码间存在显著差异；GADT 口径下各代码彼此不显著**。即同一批样品"有没有差异"取决于走哪条路径。
3. **竞品结论也随路径改变**——AT Hybrid 在 **Study Release 数据下差于 Assurance**；若改用 **GADT 数据则二者不显著**。因此**任何"我们 vs 竞品"的回渗结论都必须标注测试路径**。
4. **与上节干厚度混淆变量的叠加关系**——此前已确认干厚度为混淆变量；本次说明**测试路径是同一层级的第二个混淆变量**。二者可叠加：**路径差（0.10 g 量级）与批次/请求差（0.08 g 量级）同量级**，都大于常见方案改善幅度（0.03 g 量级）。
5. **"回渗最低"也可能是坏方案**——AT Fluffless VONN（Without Surge）回渗 **0.17 g**（本组最低）却**因摄入时间过高被排除**。**判据：回渗必须与摄入时间同轮判读，单看回渗会选中不可用方案。**
6. **另一个口径陷阱**——首轮表 Std Error **0.02407**、次轮表 Std Error **0.02249**，说明**两表不是同一次方差分析**，跨表数值**不可互相换算**。

> ⚠️ **口径提示（2026-09-29）**：来源未标注**样本量、加载液体、温湿度与 Closed Cradle 具体参数**；文中"550 g / 450 g"为加载量口径。本页此前以 **Tukey-Kramer 0.05** 为默认显著性口径，本次来源仅称 "95% CI"，二者**未声明为同一方法** `[待验证]`。
> ✅ 验证（2026-09-29）：本节为**追加**，**未修正上方任何既有结论**；"干厚度为混淆变量""批次间 0.39 vs 0.35 g""测试请求间 0.44 vs 0.36 g"均保持原样。

## Evidence Update 证据追加（2026-09-29 · AC Brand Connect）

> ✅ Verification（2026-09-29，source 来源 [[2025.09.02 - AC Brand Connect.pptx]]）：本页两例波动数据在源头获得**同源复证**——LUGH RSR 同 RSR 跨 LabVantage 请求 **0.44（R25-0274）vs 0.36 g（R25-0491）**、GRIFFIN 同机两批同请求 **0.39 vs 0.35 g**（L14 DPU2 Female M，TMA-D0672 closed cradle）。新增事实：**Gauge R&R 于 2025-09 初启动**（方法侧调查），ADT 同时协助 BizCon 做产品侧原因调查（首轮结果 9/12 回收）。竞品排序（AD 0.19 < Depend FP 0.31 ≈ Assurance 0.36 g，Female Large，Tukey-Kramer 0.05）亦出自该页。

## Evidence Update 证据追加（2026-09-29 · 介质接触失真源）

> ✅ Verification（2026-09-29，source 来源 [[FIUP collagen Testing Victoria Maria.pptx]]）：新增一类**系统性变异性来源**——介质-样品接触失真：AD 产品 **doming（穹起）** + 吸墨纸刚度 → 重量与表面**接触不全** → blotter 读数被人为压低且波动大（"very variable due to doming and not full contact"）。collagen 介质（10 片，容量 0.269 g @ 1"×2" 0.5PSI）可全接触，但**产品排序随介质翻转**（blotter: AD Old 0.898 最差 → collagen: AD New 0.147 最优）。与上方"测试路径可翻转结论"的既有判断同构，新增"介质本身"为第三个翻转维度（前两为干厚度、LabVantage/GADT 路径）。

## Evidence Update 证据追加（2026-09-29 · 方法改进设想清单）

> ✅ Verification（2026-09-29，source 来源 [[Experiments to parallel Poise studies.docx]]）：针对上方失真源的两条**在议方法改进**（规划清单，未落地）：① **接触面积归一化**——测量实际接触面积并将回渗值表示为 **g/cm² 接触面积**（blotter 与 collagen 双路线均列出），直接回应 doming/接触不全的系统性偏差；② **FIUP 盒内用 blotter**——借 FIUP 结构获得更一致/更大的纸-垫接触。同清单还开放 collagen 路线的口径问题集（P&G 复制 vs FIUP、单次 vs 反复 blot、15 s vs 2 min、权重位置、closed cradle vs FIUP）与液体属性（表面张力/离子组成）。落地前均属提议 `[待验证]`。

## 来源 Sources

- [[GRIFFIN Female DPU2 AT Hybrid Rewet Summary（女性 DPU2 AT Hybrid 回渗总结）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/GRIFFIN - Female DPU2 AT Hybrid Rewet Summary.pptx.md`
- [[GRIFFIN Regroup - Depend Rewet Update（GRIFFIN 重整更新 · 2025-08-28）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.08.28 - GRIFFIN Regroup.pptx.md`

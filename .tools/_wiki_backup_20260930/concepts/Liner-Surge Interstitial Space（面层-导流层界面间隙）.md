---
type: concept
title: "Liner-Surge Interstitial Space（面层-导流层界面间隙）"
domain: [卫材研发, 摄入系统, 回渗]
status: seed
updated: 2026-09-29
tags: [界面间隙, 剥离强度, 施胶花型, 面层, 导流层, 回渗]
---

# Liner-Surge Interstitial Space（面层-导流层界面间隙）

> 一句话定义 One-line definition：面层（liner）与导流层（surge）之间未被粘合占据的**层间空隙**——它是回渗的一条独立通道（滞留间隙液），可用**剥离强度（peel strength）**反向代理：**剥离强度越高，界面间隙越小**。

## 机理 / 结构拆解 Mechanism and Structure

1. **代理关系**：剥离强度与界面间隙量负相关——**高剥离强度 = 少界面间隙**。这使"看不见的层间空隙"变成可测量的工程指标。
2. **假设（尚未验证）**：界面间隙更小的产品会滞留更少间隙液，因此回渗更低。**原文明确标注 hypothesis (yet to be validated)，须待 MicroCT 结果验证**——即实验只证明了"怎么改间隙"，尚未证明"改了间隙就改了回渗"。
3. **五个因子的效应排序（Logworth）**：**施胶花型 Nozzle-OP 14.020** ≫ **施胶基材 4.376** > **压合 3.632** > **施胶量 1.304** > **胶型（最小，p=0.0496）**。即**花型是第一杠杆，胶型是最后一位**。
4. **施胶花型排序**：**Minibead 最高**、CF Swirl ≈ Signature 居中、**Summit 最低**；但 **Minibead 的剥离强度变异也最大**——原文提出这**可能是 Depend 回渗值更不稳定的一个来源**（把"材料机制"与"数据变异"两个问题连起来）。另注：Summit 历史上 ≥ Signature，本次偏低疑为花型质量异常。
5. **施胶基材**：胶施加在**导流层（surge）**上剥离强度**408.19**，施加在**面层（liner）**上仅 **230.09**（Tukey-Kramer 0.05 显著不同）——**施胶位置是仅次于花型的杠杆**。
6. **压合的双向效应（被量化的权衡）**：PICASSO 压合会形成**更小的口袋从而滞留液体、理论上恶化回渗**；但同时**改善面层-导流层的液体通路，使压花对回渗的净效果为正**。即**同一工艺既有负向机制又有正向机制，净值为正**——这是本批最值得记取的权衡结构。
7. **施胶量的非线性疑点**：add-on ↑ → 剥离强度 ↑，但在已压合样品中 **2.8 与 3.9 gsm 之间存在明显落差**，提示相关**可能非线性**（原文以问号标注）。

## 关键参数表 Key Parameters

| 参数 Parameter | 典型值 / 范围 Typical Value | 出处 Source |
|---|---|---|
| 效应量 Logworth（花型） | **14.020**（p 0.00000） | [[HSBL Attachment Strength Results（HSBL 附着强度结果 · 2025-11-18）]] |
| 效应量 Logworth（基材 / 压合 / 施胶量） | 4.376（p 0.00004）/ 3.632（p 0.00023）/ 1.304（p 0.00548） | 同上 |
| 花型均值（LS Means） | CF Swirl **52.879** / Signature **44.119** / Summit **24.097** | 同上 |
| 施胶基材均值 | Surge **408.19**（SE 29.750）/ Liner **230.09**（SE 26.434） | 同上 |
| 压合效应 | 压合 > 不压合（**p = 0.0002**） | 同上 |
| 胶型均值 | Henkel 5402 **133.985** vs Rextac RT-8723 **94.117**（**p = 0.0496**） | 同上 |
| 施胶量档位（同族密度表） | 1.7 / 2.8 / 3.9 gsm | [[Liner-Surge Rewet Density Testing（面层-导流层密度测试数据）]] |
| 层压厚度 / 密度区间 | 平均厚度 1.2234–1.4850 mm；密度 0.0638–0.0784 g/cc（12 gsm liner + 80 gsm surge） | 同上 |

> ⚠️ **禁止无来源参数 No unsourced numbers**：表中数字均来自上列源摘要页；**"间隙→回渗"的定量关系库内暂无来源，标 `[待验证]`**；同族密度表**不含回渗列**，不得据此推断密度→回渗因果。

## 相邻概念 Adjacent Concepts

- 上位：[[Intake System（摄入系统）]]、[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]
- 工艺：[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]、[[Liner-Surge Embossing（面层-导流层压花）]]、[[Ultra-Low Add-On Adhesive Application（超低添加量施胶）]]、[[Hot-Melt Slot Coating（热熔狭缝涂布）]]
- 滞留机理：[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]、[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- 表征与变异：[[Peel Test STM-00438（剥离强度测试）]]、[[Rewet Measurement Variability（回渗测试变异性）]]、[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]
- 材料侧：[[ADL（导流层）]]、[[亲水-疏水梯度设计]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[HSBL Attachment Strength Results（HSBL 附着强度结果 · 2025-11-18）]]）：本页为单因子 DOE 的一手结果；"剥离强度↑ = 间隙↓"为原文确立的代理关系，"间隙↓ → 回渗↓"**仍为未验证假设**（原文明确标注），故 `status: seed`。

- **教训一（先改花型，别先换胶）**：五个因子中花型的效应量是胶型的**两个数量级之差**（14.020 vs p=0.0496 的最小项）；资源应投在花型与施胶位置，胶型除非 microCT 有异常否则不动。
- **教训二（异常点会伪装成结论）**：Summit 本次最低，但历史上 ≥ Signature——**先怀疑工艺执行质量（花型质量），再怀疑花型本身**。
- **教训三（变异也是信息）**：Minibead 剥离强度变异最大，被提出为 Depend 回渗值波动的可能解释——**追求最高均值时 simultaneously 要监控方差**。
- **教训四（净效应思维）**：压合同时有"更小口袋滞留液体（负）"与"改善通路（正）"两种机制，**净值为正**；单一机制的推理会得出相反结论。
- **待补 `[待验证]`**：MicroCT 对"间隙→回渗"假设的验证结果；剥离强度与界面间隙的定量标定曲线；施胶量与剥离强度的非线性的确认。

## 来源 Sources

- [[HSBL Attachment Strength Results（HSBL 附着强度结果 · 2025-11-18）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/Surge-Liner Interface/Test Results/HSBL Attachment Strength Results.pptx.md`
- [[Liner-Surge Rewet Density Testing（面层-导流层密度测试数据）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/Surge-Liner Interface/Test Results/Liner-Surge Rewet - Density Testing.xlsx.md`

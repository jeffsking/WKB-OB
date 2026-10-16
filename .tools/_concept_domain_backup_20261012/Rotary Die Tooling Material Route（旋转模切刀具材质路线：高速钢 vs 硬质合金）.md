---
type: concept
title: Rotary Die Tooling Material Route（旋转模切刀具材质路线：高速钢 vs 硬质合金）
category: 工艺 / 刀具与工装
updated: 2026-09-30
tags: [rotary die, 模切, 高速钢, 硬质合金, tungsten carbide, 花型, pinhole, Kirigami, tooling]
domain: [卫材研发, 无纺布工艺]
status: growing
---

# Rotary Die Tooling Material Route（旋转模切刀具材质路线：高速钢 vs 硬质合金）

**一句话定义**：旋转模切 / 打孔刀具的**材质路线选择** —— **高速钢（high speed steel, HSS）易加工、可做出任意花型，用于打样与原型**；**硬质合金（tungsten carbide）耐磨、用于量产刀具，但花型自由度受限（须规避刚性角度与刚性边）**。二者构成"**原型材质 ≠ 量产材质**"的经典可行性陷阱。

> 名称说明：ASR 转写中作「constant carbide / tompson car / carbon carbide / tosson carbide」，还原为 **tungsten carbide（硬质合金）**；「Thompson」疑为刀具品牌 **[待验证]**。本页由 2026-09-29 编译的三份供应商会议纪要汇成，参数均为**供应商口径**，未见第三方验证。

## 机理 / 结构拆解

### 1. 为什么材质决定花型（可制造性链条）

**花型设计 → 刀具材质可加工性 → 能否量产**

- 高速钢**易切削/易成形** → **任意花型都能做** → 适合**打样（prototype）**与快速迭代。
- 硬质合金**硬度高、难加工**（须磨削成形）→ **不是所有花型都能做** → 需要**规避某些角度与刚性边（rigid angles / rigid edges）**。
- 因此：**原型做得出来 ≠ 量产做得出来**。若在高速钢阶段不按硬质合金的约束收敛花型，会把不可量产的方案带进量产段。

### 2. 标准路线（本方与供应商达成的打样流程）

| 阶段 | 材质 | 目的 |
| --- | --- | --- |
| ① 打样 / 原型 | **高速钢（HSS）** | 快速验证花型外观与功能 |
| ② 确认原型 | — | 双方 agree 后才转量产材质 |
| ③ 量产刀具 | **硬质合金（Thompson carbide）** | 耐磨、长寿命 |

### 3. 硬质合金的产业稀缺性

- 全球**仅约 3 家**能**自行研磨**硬质合金模具（供应商自述，其为之一）—— 该能力被作为**差异化能力**提出，本方对此表示惊讶并认可难度。
- 推论：硬质合金路线的**供应链极窄**，换供应商/并行开发的空间小 → **花型冻结时点应提前**。

### 4. 刀具材质的另一处应用：分切刀（slitting blade）

| 材质 | 换刀频次影响 | 备注 |
| --- | --- | --- |
| **steel blades（钢刀）** | 基线 | — |
| **carbide or ceramic（硬质合金 / 陶瓷）** | **换刀频次 +30–40%** | 原因：**PET abrasive（PET 磨蚀性强）** |

→ 材质选择在开孔/模切之外同样影响**耗材与停机**，是同一类"材质—寿命—成本"权衡。

## 关键参数表

| Item 项目 | Value 数值 | Note 备注 |
| --- | --- | --- |
| 打样材质 | **高速钢（HSS）** | 任意花型可做 |
| 量产材质 | **硬质合金（tungsten carbide）** [待验证] | 花型受限 |
| 硬质合金禁区 | **刚性角度 / 刚性边（rigid angles / rigid edges）** | 具体禁区清单**未获供应商答复** [待验证] |
| 自研磨硬质合金能力 | 全球约 **3 家** | 供应商自述，无第三方验证 |
| 分切刀材质增益 | 硬质合金/陶瓷 vs 钢：**换刀频次 +30–40%** | 因 PET 磨蚀性 |
| 刀具寿命与花型 | 花型越复杂 → 加工与磨削难度越高 | 推论，未量化 |
| 共同开发的费用原则 | **本方承担一定比例，非 100%** | 具体比例未谈（商务，见 manual_review） |
| 共同开发对价 | **模块/刀具不得售予他人** | 供应商当场接受 [待验证] |

## 相邻概念

- [[Kirigami Apertured Nonwoven（切割拉伸开孔工艺）]]
- [[Core Channel Pattern（芯体通道花型设计）]]
- [[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]
- [[Laser-Assisted Die Tip（激光辅助模头）]]
- [[三叶形截面纤维（Trilobal Fibre）]]

## 经验教训

1. **原型材质 ≠ 量产材质，是开孔/模切类项目最常见的可行性陷阱** —— 高速钢能做的花型，硬质合金未必能做；**必须在设计输入阶段就索取"不能做什么"的负面清单**，而不是等到转量产才发现。
2. **索取指引的顺序应为：先负面清单、后正面设计**。本方在会中连续两次追问"哪些花型在硬质合金上做不出来"，说明**负面清单是启动设计的前置条件**。
3. **能力边界（孔径上下限、孔—孔间距、异形孔可行性）属于设计输入，不是设计输出** —— 拿不到边界就开工，等于把返工风险后置。
4. **硬质合金供应链极窄（全球约 3 家可自研磨）** → 花型冻结时点应提前，且**换供应商的备选空间小**，工装投资的风险高于钢刀路线。
5. **共同开发的本质是"用费用分担换独家性"** —— 分担比例的谈判筹码是**独家不售他人**，二者绑定，缺一项则共同开发不成立。
6. **材质选择同时是耗材与停机问题**（分切刀换刀频次 +30–40%），评估工装材质时应把**寿命增益**计入，而非只比采购价。

> 🔴 **manual_review（2026-09-29）**：本主题涉及**模具/工装（tooling）成本、共同开发的费用分摊比例、供应商独家承诺与报价** —— 按 AGENTS.md §5，**报价与商务条款不得页面化**；本页只保留"按比例分担、非 100%"这一机制性表述与"不售他人"的对价关系，**不记录任何金额**。请回原文核对：
> `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/合作开发新模具设计.md`
> `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/公司介绍与业务交流.md`
> 另：「Thompson carbide」是否指刀具品牌、以及硬质合金花型禁区的具体条目**均未获供应商答复** [待验证]。

## 来源

- [[Co-Development Tooling Design Review — Kirigami Pattern, Pin-Hole Module & Carbide Guidance（合作开发新模具设计）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/合作开发新模具设计.md`
- [[Precision Rotary Die & Module Supplier Review — Stretch Cutting, SAP Dosing & Layer Config（公司介绍与业务交流）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/公司介绍与业务交流.md`
- [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/Trilobal_PET_Liner_MD_Distribution.pptx.md`（分切刀材质口径：steel vs carbide/ceramic）

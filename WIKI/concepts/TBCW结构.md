---
type: concept
title: "TBCW结构"
domain: [卫材研发, 芯体结构]
status: growing
updated: 2026-09-30
tags: [TBCW, TABCW, 超声波复合, 纺粘底层, 降本]
aliases: ["TBCW 结构（在线超声波复合）"]
---

# TBCW 结构（在线超声波复合）

> 一句话定义：一种以**在线超声波复合**为固结手段的芯体/无纺布复合结构，其底层为纺粘（Span Bond）；在本库中是低温 PP 纺粘替代 Bico 降本方案的应用载体。

## 机理 / 结构拆解

1. **结构分层**：TBCW 结构底层为 Span Bond（纺粘），原克重 20 gsm；降本路径第一步是降至 12 gsm，第二步是材料替换。
2. **粘合方式决定材料选择**：TBCW 采用在线超声波复合。现有方案中，纺粘底层**必须用 Bico（PE/PP 皮芯）**，靠外皮 PE 实现粘合；若能改用低温 PP（熔点约 140°C）单组份纺粘，则可直接与 TBCW 低熔点层热粘合，省掉 Bico 成本与 PE 表皮工艺。
3. **为什么想摆脱 Bico**：PE 皮太嫩、表面难处理，做上色、Kirigami 类工艺不如纯 PP 好做；Bico 后续处理麻烦。
4. **技术争议点**：福建兴泰认为低温 PP 纤维偏硬、影响柔软度，主张用超声波焊接解决 PP 粘合问题而非改材料；且三层纤维结构中**中间层粘合强度仍是未知数**。
5. **REL 关联**：TBCW 与 REL（增强层）项目相关——OI-02 即「PVA Fibre for TABCW (REL)」，说明 TABCW 是 REL 的应用场景之一。

## 关键参数表

| 参数 | 数值 | 出处 |
|---|---|---|
| 底层原克重 | 20 gsm | [[低温PP纺粘与TBCW低成本方案]] |
| 降本目标克重 | 12 gsm | [[低温PP纺粘与TBCW低成本方案]] |
| 现有底层结构 | Bico（PE/PP 皮芯，PE 在外） | [[低温PP纺粘与TBCW低成本方案]] |
| 目标替代材料 | 低温 PP（熔点约 140°C）单组份纺粘 | [[低温PP纺粘与TBCW低成本方案]] |
| 粘合方式 | 在线超声波复合 | [[低温PP纺粘与TBCW低成本方案]] |
| 理论可行门槛 | 改性 PP 至约 130°C（接近 Bico 中 PE 熔点） | [[低温PP纺粘与TBCW低成本方案]] |
| 关联项目 | OI-02 PVA Fibre for TABCW (REL) | [[OI项目清单与优先级]] |

## 相邻概念

- 关键材料：[[低熔点聚丙烯]]、[[皮芯复合纤维]]
- 关联网结构：[[REL增强层]]
- 工艺争议方：[[福建兴泰]]

## 经验教训

> ⚠️ 本页为 seed 状态：库内关于 TBCW 的信息来自录音纪要归拢稿，**结构与工艺参数未获技术文件级来源**，引用前需回源确认。

- **要点**：TBCW 降本是「克重 + 材料」两步组合拳，评审时应把两步的成本与风险分开衡量（克重降本确定性强，材料替换依赖低温 PP 供应成熟度）。
- **待补 `[待验证]`**：TBCW 完整结构剖面与各层克重/材料；中间层粘合强度的量化基线。

> ✅ 追加（2026-09-29，来源 [[PPC&PGA 基无纺布开发方案（第二版）]]）：TABCW 的**皮层**新增一项候选材料——**PPCP + PBAT + PLA 复合料，熔点 130 ℃**（可家庭堆肥取向，成本口径 < RMB 15/kg），与 **PGA 芯层（约 220 ℃）**组合为「130 ℃ 皮 + 220 ℃ 芯」的皮芯纤维；该纤维估成本 ≈ **RMB 22.5/kg**（含 +5 RMB/kg 加工费，口径截至 2026-01）。原文将该组合标注为「尚待深度技术评估的新材料组合」。另记：PPC-P 系纺粘（30% PPC-P + 70% PBAT）为**平行路线**，非 TABCW 结构。**本节为追加，未改动本页既有结论。**

## 追加：Meeting Minutes 批（2026-09-29 追加 · TBCW 在 Kirigami / Bay Max v2 / BA 项目中的角色与已知波动）

> 来源：[[Kirigami Process, LSE Bonding & Pattern Pitch Review（不同人员自我介绍交流）]]（K-C 内部现场交流会 ASR 转写，会议日期 [待验证]）。本批只**追加**，不修改既有结论。

**TBCW 在本批项目中的角色（本批新增）：**

| 项目 / 议题 | TBCW 的角色 | Note 备注 |
| --- | --- | --- |
| Kirigami 工艺 | 讨论中作为开孔工艺的**基材**候选；会中提及 TBCW **30 GSM** 规格 | 与 adhesive 路线对比时提及 [待验证] |
| 项目 **Bay Max v2** | 考虑**把层换成 TBCW**（v2 版本的层结构变更方向） | 会议中提出，未定 |
| 项目 **BA** | **TBCW liner 与 spunbond 层压**，用**低 capex 超声波**实现 | 与 Bay Max 并行 |
| 项目定位 | Bay Max 为 IPC innovation accelerator 获奖项目、**IPC 全球最高优先级项目之一** | ⚠️ 内部项目信息 |

**TBCW 的已知波动问题（本批新增）：**

- **GSM 波动**：TBCW 有时存在 GSM 波动，其 band（克重控制带）由 signal 控制。
- **CD 方向差异**：与 MD 相比，CD 方向**略有不同**。
- 运营侧的应对：运营团队有时会到现场做 traceability 排查。

**实践含义（本批新增）：**

- 因为 TBCW 存在 GSM 波动与 CD 方向差异，**Kirigami 的拉伸比必须在线根据材料调整**，无法固化为固定的一步/多步拉伸工艺卡。

✅ **验证记录（2026-09-29）**：TBCW 30 GSM 与项目代号（Bay Max / BA）均来自 ASR 转写，**未经核实**；GSM 波动与 CD 差异为会中口径，无实测数据。参见 [[Kirigami Apertured Nonwoven（切割拉伸开孔工艺）]]、[[Ultrasonic Bonding of PET-Containing Topsheet]]、[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]。

## 追加：Meeting Minutes 批 2（2026-09-29 追加 · 彩色印刷位置改到 TBCW 覆盖区以规避转移与堆积）

> 来源：[[Be Max Platform — Trilobal Fibre Ratio, Ultrasonic Bonding & MD Distribution Target（纤维加工温度与成本验证）]]（跨团队技术交流，英文 ASR 转写，会议日期 [待验证]）。本批只**追加**，不修改既有结论。

**印刷位置的改变（本批新增）：**

| | 原方案 | 改后方案 |
| --- | --- | --- |
| 位置 | 在 **LSE 区域**做不同颜色的印刷 | 在**被 TBCW 覆盖的区域**印刷 |
| 判断 | — | 因为**被 TBCW 覆盖**，高速下**不会有转移（transfer）或油墨堆积（build-up）问题** |

- 触发点：本次访问之后改变了想法（"before today's visit… after today's visit maybe we are thinking about using color printing at this"）。
- 顶层还有一层 **LSE 制作的结构**（"on the top layer we have this kind of … made by the LSE"）[待验证]。

**由此得到的认知（本批新增）：**

1. **把印刷藏在覆盖层之下，是解决"高速印刷质量 / 油墨堆积 / 单侧可见性"三大障碍的结构性办法** —— 与 [[Chromism Taxonomy（变色现象分类）]] 中"在非贴肤面印刷以制造深度感"的思路同源，本批补充了**为什么可行**：覆盖层同时解决了**油墨转移**与**堆积**两个失效模式。
2. **代价是可见度**：被覆盖意味着颜色是"透出来"的，因此**对 TBCW 的透光度有要求** —— 与"上层 30 gsm TBCW 透色度非常好"的判断相互呼应。
3. 该方案被排在 **Kirigami 与印刷之外**的初始样品之后（**10 月**先拿不含 Kirigami 与印刷的样品）→ 属**第二阶段**内容。

✅ **验证记录（2026-09-29）**："不会有转移/堆积问题"为会中判断，**未见高速实测**；顶层 LSE 结构的具体表述在 ASR 中不完整 [待验证]。参见 [[Chromism Taxonomy（变色现象分类）]]、[[Kirigami Apertured Nonwoven（切割拉伸开孔工艺）]]、[[三叶形截面纤维（Trilobal Fibre）]]。

## 来源

- [[低温PP纺粘与TBCW低成本方案]] —— `raw/ima_sync/个人知识库/WKB/低温PP相关的纺粘布讨论主要集中在TBCW低成本方案.md`
- [[OI项目清单与优先级]] —— `raw/ima_sync/个人知识库/WKB/好，资料已经齐了。根据知识库中最新（2026-09-18）的.md`
- [[PPC&PGA 基无纺布开发方案（第二版）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/PPC/PPC&PGA based NW development 2.pptx.md`（2026-09-29 追加）

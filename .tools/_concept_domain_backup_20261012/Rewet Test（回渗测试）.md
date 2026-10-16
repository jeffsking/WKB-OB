---
type: concept
title: "Rewet Test（回渗测试）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-29
tags: [回渗, Rewet, Flowback, 反渗, GB-T28004, STM-00059-2, 测试口径, 载荷]
aliases: ["回渗测试（Rewet / Flowback）", "Rewet 测试"]
---

# Rewet Test（回渗测试 / Rewet / Flowback）

> 一句话定义：把已知干重的滤纸（吸水纸）压在已被液体浸湿的产品表面上、施加规定载荷并保持规定时间，以**滤纸增重**表征"液体从产品返回到皮肤侧的量"。**Rewet 值本身不是可比量——载荷、等待时间与压合时长共同定义它**（中文：回渗值必须连载荷与时间一起引用）。

## 机理 / 结构拆解 Mechanism

1. **回渗的物理来源**：液体被 SAP 吸收后仍有一部分以**毛细水 / 颗粒间隙水**形式停留在面层与芯体表层；受皮肤压力时，这部分水被挤出到滤纸上。因此回渗量对**载荷**与**等待时间**极度敏感。
2. **等待时间决定"自由回渗"的量**：注液后立即测（短等）读到的是面层残液；等待 10–15 min 后测读到的是"压力下长期未吸收液"。前者对应溢奶/快速活动的体感，后者对应久坐/夜间的体感。
3. **载荷决定测量档位**：本库出现三档——国标 1.20 kg（直径 100 mm 压块）、U Rewet 的国标回渗压块（1 min）、高低压反渗的 2×4 kg（合计 8 kg）。**三档不可互相替代**。
4. **读数计算在三种方法中高度一致**：`回渗 = 湿滤纸重 − 干滤纸重`（BM 便液版本同构）。
5. **回渗与滑渗是互补指标而非重复**：回渗量液体"返出"，滑渗量液体"漏走"（见 [[Run-off & Leakage Test（滑渗与渗漏测试）]]）。

## 关键参数表 Key Parameters

| 方法 | 载荷 | 等待时间 | 压合时间 | 液体 / 温度 | 出处 |
|---|---|---|---|---|---|
| STM-00059-2 Flowback（芯体/产品级主 KPI） | 14±1 in WC（≈3.4 kPa） | 3 min + 2 min | 2 min | — | [[芯体测试方法与验收基准（STM）]]（既有页，非本批来源） |
| **STM-00059 反渗（第 3 版，母本）** | **真空 14 ± 1 inH₂O = 3447 Pa（乳胶膜覆盖）** | **3 min ± 15 s** + 等待 **1 min** | **2 min ± 15 s** | 0.9% 盐水；ST2 **150** / ST3·Med **180** / ST4·L **210** / ST5·XL **240 mL**（±0.5 mL） | [[STM-00059 反渗.docx]] |
| KC U Rewet | 国标回渗压块（原文未给质量） | 第二次注液后 5 min | 1 min | 0.9% 盐水 + 蓝粉，37 ℃ | [[KC U Rewet测试.docx]] |
| TTM-00623 高低压反渗 · 低压段 | 反渗板（未给板重）`[待验证]` | 注液后 2 min | 2 min | 37 ℃ 盐溶液 | [[TTM-00623高低压反渗测试.docx]] |
| TTM-00623 高低压反渗 · 高压段 | **2 × 4 kg（合计 8 kg）** | 注液后 15 min | 2 min | 37 ℃ 盐溶液 | [[TTM-00623高低压反渗测试.docx]] |
| GB/T 28004-2011 回渗 | **1.20 kg / 直径 100 mm 压块** | 10 min（0 min + 5 min 两次注液后） | 1 min | 生理盐水 | [[GB-T28004-2011 回渗渗漏.doc]] |
| TTM-00466 BM 回渗 | 0.25 PSI | 注液后 5 min | 30 s | BM simulant A : 生理盐水 = 3:1 | [[TTM-00466 BM Benefit Visualization Validation.docx]] |

| 参数 | 通用口径 | 出处 |
|---|---|---|
| 滤纸尺寸 | GB/T 28004-2011 用直径 110 mm；以最上层无吸液为止 | [[GB-T28004-2011 回渗渗漏.doc]] |
| 增重精度 | 0.001 g（滤纸） | [[TTM-00623高低压反渗测试.docx]] |
| 产品称重精度 | 0.01 g（U Rewet 段）；0.001 g（高低压段） | [[TTM-00623高低压反渗测试.docx]]、[[KC U Rewet测试.docx]] |
| 计算式 | 回渗 = 湿滤纸重 − 干滤纸重 | [[KC U Rewet测试.docx]]、[[GB-T28004-2011 回渗渗漏.doc]] |
| 液温 | 37 ℃（尿）/ 37±1 ℃（BM 段生理盐水） | [[TTM-00148 Cradle测试.doc]]、[[TTM-00466 BM Benefit Visualization Validation.docx]] |

> ⚠️ **禁止无来源参数**：本表所有数字均来自本 block 的源摘要页；库内**没有** STM-00059-2 的完整操作规程原文（既有页仅记编号与门槛），其载荷换算 `14±1 in WC ≈ 3.4 kPa` 标 `[待验证]`。
> ⚠️ **跨来源同类方法差异（2026-09-29）**：三档载荷（1.20 kg / 国标压块 / 8 kg）与三种等待（2 / 5 / 10–15 min）**不可混为一条口径**，比较回渗数字前必须先对齐载荷与等待。

## 相邻概念 Adjacent Concepts

- 上游指标：[[Cradle Intake Test（Cradle 摄入测试）]]（吸收时间）、[[SAP性能指标（CRC AUL GBP Vortex）]]（AUL / GBP 是回渗的物质基础）
- 互补指标：[[Run-off & Leakage Test（滑渗与渗漏测试）]]（滑渗 / 渗漏）
- 同族口径：[[Liquid Diffusion Test（液体扩散测试）]]（扩散长度）
- 便液版本：[[Mannequin BM Test（BM 假人测试）]]
- 上位索引：[[芯体测试方法与验收基准（STM）]]
- 对比：[[Rewet Protocols Compared（回渗测试口径对比）]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[KC U Rewet测试.docx]]、[[TTM-00623高低压反渗测试.docx]]、[[GB-T28004-2011 回渗渗漏.doc]]）：本 block 三份来源的 `回渗 = 湿滤纸重 − 干滤纸重` 计算式完全一致，但**载荷与等待时间三份三样**——证实"回渗值不可裸引"是本库的硬约束，与既有页 [[芯体测试方法与验收基准（STM）]]「回渗要挑对协议」的结论方向一致。

- **教训一（口径）**：**载荷是回渗的第一属性**。8 kg（TTM-00623 高压段）与 1.20 kg（GB 国标）读到的不是同一个物理量；引用回渗门槛前必须写明是哪一套。
- **教训二（口径）**：**等待时间决定测的是"面层残液"还是"未吸收液"**。2 min 与 15 min 的差别是场景差别，不是严格程度差别。
- **待补 `[待验证]`**：U Rewet 国标回渗压块与 TTM-00623 低压段反渗板的**实际质量 / 压强**（两份原文均未给出）；STM-00059-2 的完整操作规程。


> ✅ 验证（2026-09-29，来源 [[GB-T 28004.1-2021 Absorption Tester SOP（国标吸收性能测试仪操作步骤）]]）：国标仪器 SOP 给出**与厂内手册不同的滤纸与加压口径**——滤纸须 **23 ℃、50% RH 恒温恒湿 16 h**（天津原材料册为 **6 h**），回渗用 **10 张/片**、渗漏用 **3 张/片**，**16 min 时开始加压、加压 1 min**，结果取平均并**精确至 0.1 g**（非 0.01 g）。加液量 **NB/S 40 mL、M 60 mL、L 及以上 80 mL（± 2 mL）**，测试液 **36 ± 1 ℃**。**滤纸调湿时长与加压时点不同，回渗读数不可与厂内 STM 口径直接对比。**

## 追加：Open Innovation 批（2026-09-29 追加 · 方法参数沿革）

> 追加来源：[[Rewet Method Parameters（回渗测试方法参数沿革）]]。**不改动上文既有结论**；本批首次给出**压力/加液/时序三类参数"为什么是这个值"的决策史**——包括一处记录在案的参数错误。

### 1. 分产品形态的典型压力（Summary）

| Product Form | Typical（psi） | Peak（psi） | Notes |
|---|---|---|---|
| **BCC 婴儿** | **0.3** | 1.0–2.5 | — |
| **Adult Pads** | **0.6–2** | 2–6 | — |
| **Adult Pants** | **?** | **?** | 源文自设未解问题："Is this similar to Adult Pads?" |

> 中文：**成人裤至今没有可用的消费者压力数据**——TL-10149（2004）在股薄肌腱处的实测**因压力低于传感器量程且噪声大而失败**。这是本页"回渗值不可裸引"之外的**第二条硬约束**：**成人裤的回渗压力档位本身缺乏依据**。

### 2. 压力档位沿革（本页此前未记录）

| 品类 / 时间 | 压力 | 记录下来的理由 |
|---|---|---|
| BCC 最早（~1991） | **0.5 psi** | 压力由**真空饱和压帽箱**施加 |
| **BCC 2015 TTM-00623 Lo/High** | **设计 0.46 psi，实际 0.24 psi** | ⚠️ 见下 |
| AFC 最初 | 0.5 psi（flowback） | 与婴儿共用方法 |
| **AFC 2004**（TR-3006 / TL-11230） | **1.0 psi** | "更高压力反映成人用户而非婴儿所受压力" |
| **AFC 2015 FIUP** | **0.7 psi** | 与宽松内裤对卫生巾的压力相近 |
| **AFC 2020**（TTM-00643v4 GR&R） | **0.5 psi** | "更大直径压块……更好模拟真实消费者体验" |

> ⚠️ **记录在案的错误（源文原文，照录不裁决）**：*"When Lo/High Rewet (TTM-00623) is developed in 2015 it intends to use 0.46 psi for rewet, but it actually uses 0.24 psi (TL-15701). **It's not clear where the error is – perhaps a calculation error?**"*
> 源文推测低压来源为 **Surface Moisture**（约在 **PICASSO 压花面层/导流层体系**时期发明）。**该错误是否已被纠正需人工确认**。

### 3. 加液与时序的"选择依据"（可直接用于方法设计）

| 参数 | 依据（源文） |
|---|---|
| **加液位置（FIUP）** | 卫生巾长度"中心 4 点除以 6"——**计入产品在内裤中放置方式的变化**（Anthro 研究 AF32161-00, 2008） |
| **加液位置（Closed Cradle）** | **"judgement call"**——取 TTM-00148 中按性别最常见的加液位置 |
| **加液量（FIUP 2014）** | **Urine Loss Spectrum Study IT-34734 的总负载 75 分位**——"确保在比平均更重的日子里仍能交付干爽"；分 **3 次**加液 |
| **加液量（Closed Cradle）** | 起初沿用 FIUP，后改为**女性 L 码单次加液的中位数**（HUT 35732 / 35740） |
| **回渗时长 2 min（BCC TTM-00623）** | 由**吸水纸的垂直芯吸试验**确定 |
| **2 min / 15 min 双档** | 由**回渗随加液后时间的变化**确定——此时变化趋缓且**变异更小** |
| **回流从第 2 次→第 3 次加液后** | 因**更换产品做最后一次加液会带来变异**（TTM-0001/0002） |

### 4. 两个数字符号性的事实（供跨源核对）

- **回渗压力跨度**：从 **TTM-00623 低压档 0.005 psi** 到 **成人护理 1.0 psi**，相差 **约 200 倍**。
- **加液压力跨度**：**0.1 psi**（最初）→ **1.2 psi**（2004）→ **膀胱箱 0.25 psi**。

> ✅ 验证（2026-09-29）：本追加段**未修正**本页任何既有结论；上文"回渗值不可裸引"的硬约束**不但未被触及，反而被方法史进一步坐实**——**同一公司、同一指标，30 年间用过 0.005 / 0.05 / 0.24 / 0.5 / 0.7 / 1.0 psi 六档压力**，且多数变更理由被源文记为"唯一给出的理由"或"判断性选择"。

> 🔴 **manual_review（2026-09-29）**：本源含大量内部方法编号（STP/STM/TTM/TR/TL/HUT/Anthro），本页仅作追溯引用；**TTM-00623 参数错误不页面化整改责任**；竞品动态（2013/4 P&G 干爽宣称）仅记因果。

## 追加：Open Innovation 批（2026-09-29 追加 · Closed Cradle 与 NWSP 070.9 的整表差异）

> 追加来源 `[[Depend Rewet Update 2025-04-04（LUGH 与 GRIFFIN 回渗进展）]]`（2025-04-04）。本段**只补"KC Closed Cradle 与客户指定 NWSP 070.9 的逐参数对照"，不改动上文任何方法沿革、压力锚点与结论**。

### 1. 逐参数对照表（源文原表）

| 参数 Parameter | **KC Closed Cradle** | **NWSP 070.9 R(15)** |
|---|---|---|
| Position 位置 | **Anatomical, Cradle（解剖体位 / Cradle）** | **Center Pad, Flat（垫片中心 / 平放）** |
| Insult Amount 加液量 | **3 insults × 50 mL** | **1 insult × 105 mL** |
| Wait Time 等待 | **15 min** | **10 min** |
| Insult Pressure 加液压力 | **0.25 psi** | **None（无）** |
| Blotter Media 吸墨介质 | **2 sheets blotter paper, 88×300 mm** | **10 g stack filter paper, Ø90 mm** |
| Rewet Pressure 回渗压力 | **0.5 psi** | **1.0 psi** |
| Rewet Duration 回渗时长 | **2 min** | **1 min** |

> ⚠️ **七个参数中六项不同**——这解释了源文的判断："Very different from our method, so need to submit for testing to understand differences（差异极大，须送测以理解差异）"。**本页不推断两种方法的数值换算关系。**

### 2. Closed Cradle 方法卡（源文补充字段）

| 项 | 值 |
|---|---|
| 加液位置 | **F: 95 mm / M: 200 mm forward of center**（按消费者研究确定） |
| 流体 / 温度 | 盐水；**37 °C** |
| 加液口 | 1 in 直径、4×4 in 底座的加液管 |
| Blotter 材质 | **100 lb verigood blotter**；滤纸 **Grade 950** |
| 回渗压块 | **Ø61 mm（KC）vs Ø90 mm（NWSP）** |
| 时程序列 | T=0 加第 1 次液 → T=10 min → T=15 min → T=30 min 移出 Cradle → **T=32 min 置于吸墨纸 + 回渗压块，等待 2 min 后称盐水重量** |

### 3. 为什么这条对照对本页重要

- 上文已确立的硬约束是 **"回渗值不可裸引"**（同一公司 30 年间用过 0.005 / 0.05 / 0.24 / 0.5 / 0.7 / 1.0 psi 六档压力）。本追加段把这条约束**从"纵向的历时变化"扩展到"横向的跨组织方法"**：**客户（Walmart 训练裤招标）指定的是另一套标准**，其加液量、压力、介质与时长全部不同。
- **成人产品此前从未与客户讨论过台架测试**（源文原话：*"Never discussed bench testing on adult products with Walmart previously"*）——这意味着**成人护理品类首次面临外部标准对齐问题**。

> ✅ 验证（2026-09-29）：本追加段**未修正**本页任何既有结论；上文的压力换算锚点（14 ± 1 inH₂O = 3.4 kPa / 0.5 psi / SAT CAP 上限 2.0 psi）**均未被触及**，本批补的是**跨组织方法差异**维度。

> 🔴 **manual_review（2026-09-29）**：本源含竞品实测数据与内部编号（HUT / TTM / LabVantage）；本页**只记方法参数与流程，不落竞品性能全表**。

## 追加：Open Innovation 批（2026-09-29 追加 · Closed Cradle 变异调查的否定性结果）

> 追加来源 `[[Rewet Learning Plan（回渗学习计划工作表）]]`（推断 2026-02 前后）。本段**只补"同一方法内部的变异来源排查记录"，不改动上文任何方法沿革、跨方法对照与结论**。

### 1. 变异排查的四步与结果

| 步骤 | 内容 | 状态 / 时间 |
|---|---|---|
| 1 | Brainstorm（头脑风暴） | Complete & shared / **09/04/25** |
| 2 | **Identify top 3–4 causes（识别前 3–4 个成因）** | Complete & shared / **09/05/25** |
| 3 | Test identified causes for impact（验证成因影响） | Complete & shared / **09/18/25** |
| 4 | **Gauge R&R（量具重复性与再现性）** | Complete & shared / **09/30/25**；11/14/25 analyzed |
| 5 | Learning cycle | 进行中 |

### 2. ⚠️ 三项方法修改"无改善"（本批最关键的一条）

> 源文原文：*"**1/27/26 - tested modifications to method (standardizes stretch, removed immediately from cradle, smaller blotter) with no improvement**"*

| 修改项 Modification | 结果 |
|---|---|
| **Standardizes stretch（标准化拉伸）** | **无改善** |
| **Removed immediately from cradle（立即从 Cradle 中取出）** | **无改善** |
| **Smaller blotter（更小的吸墨纸）** | **无改善** |

- **下一步**：调查 **blotter / weight 的尺寸与位置**、**timing（时序）**。
- ⚠️ **判读纪律**：这是**"这三项不是变异源"的否定性证据**，**不等于"变异来自产品"已被证明**。源文的下一步仍在方法侧（尺寸/位置/时序），**未转向产品侧**。

### 3. 与上文的关系：把"不可裸引"从跨方法推进到同方法内部

| 上文（既有） | 本批追加 |
|---|---|
| **时间维度**：同一公司 30 年间用过 0.005 / 0.05 / 0.24 / 0.5 / 0.7 / 1.0 psi 六档压力 | — |
| **跨组织维度**：KC Closed Cradle vs 客户指定 NWSP 070.9（七项中六项不同） | — |
| — | **同方法内部维度**：即使固定为 Closed Cradle，**数据变异本身也大到"难以判读变化"**（源文假说原文：*"Variability in test results make it difficult to interpret changes"*） |

> ✅ **同向、非冲突**：三个维度**共同坐实**上文的硬约束 —— **回渗值不可裸引**。本追加段**未修正**任何既有结论，也未改变上文的压力换算锚点。

### 4. 附带的资源/人力事实

- 该工作流的明确障碍是 **"Someone needs to drive the work, coach Mark"**（需要有人推动并辅导）—— 即**变异调查的瓶颈之一是人力和组织，不是方法本身**。
- ⚠️ **不作技术结论**：这是**组织层面的记录**，**不得解读为"方法无需改进"**。

> 🔴 **manual_review（2026-09-29）**：本源为内部工作计划表，含**负责人姓名与团队分工**；本页**只记工作流、状态与方法学事实，不转述竞品技术细节，不页面化组织安排的细节**。

## 追加：Open Innovation 批（2026-09-29 追加 · 回渗的正式定义句与方法参数清单）

来源：[[Rewet Principles（回渗设计原则与测试方法关联）]]（K. Clemmer – ADT / I. Hoeger – Absorbent Systems，Updated 10/22/25）。

### 1. 正式定义句（本页判据的原文出处）

> **"Rewet is the mass of fluid that transfers into a blotter media from a product over a given time and under a specified applied pressure."**
> （中文：回渗 = 在**给定时间**与**规定压力**下，从产品转移到**吸墨介质**的液体质量。）

本页一贯的硬约束——**回渗值不可裸引**——在此得到**原文级支撑**：定义句本身就把 **时间 / 压力 / 介质**三项写进了量的定义。

### 2. 影响回渗的测试方法参数（源文清单，七类）

| 参数 | 取值 / 说明 | 中文 |
|---|---|---|
| 摄入期与回渗期压力 | **Low / High** | 低压 / 高压 |
| 加液方式 Insult method | Loading / Rate / Location / Pressure / Type（**Flat, cradle**）| 液量 / 速率 / 位置 / 压力 / 类型 |
| 等待时间 | 加液之间及加液到回渗之间 | 时序 |
| 吸墨介质 | blotter paper / **collagen sheets** | 吸墨纸 / 胶原片 |
| 尺寸与形状 | **吸墨纸**的、**以及压块**的 | ⚠️ 两者是**两个独立变量** |
| 流体 | **salinity 盐度** | — |
| 温度 | — | — |

> ⚠️ **"压块尺寸/形状"被单列为独立参数** —— 这正是上一段（Closed Cradle 变异调查）在**三项方法修改均无改善**之后列出的**下一步**（调查吸墨纸/压块的尺寸与位置）所对应的变量；本件把它提升到了**参数清单层面**。

### 3. 两大机制的官方二分（本页未使用 LPR/HPR 术语）

| 机制 | 源文 | 中文 |
|---|---|---|
| **Flowback 回流** | *"fluid that isn't locked up, so can flow back to the blotter/skin"*；*"Often concentrated in the core, as that's where fluid settles (via gravity)"* | 未被锁住的液体被压回；常集中在**芯体**（重力沉降）|
| **Desorption 解吸** | *"fluid trapped in the intake layers (against gravity) … expressed back under the pressure of a blot"*；摄入材料空隙构成一串**孔隙**，**材料之间的空隙同理** | 摄入层**逆重力**滞留，受压后释放 |

> ⚠️ 与 [[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]] 的关系属**本页并置**：本源**未出现 LPR/HPR 字样**，机制二分方向一致但**无源文互证**，**不合并、不换算**。

### 4. 每条原则绑定的三类方法（节选，Materials / Products / Modeling）

- 容量：**CRC（STM-00219）** / **Functional capacity（TTM-00638）**、**Retention Capacity（STM-00033）**、Target zone capacity / Virtual functional capacity
- 可达性：**GBP（STM-00229）**、**Composite permeability（TTM-00006）** / **X-ray imaging（TTM-00631）**、**Bromocresol SAM 分布（JA-22229）**、**Mannequin Forced Failure（TTM-00459 / TTM-00200 / TTM-00660）**\* / AFEA
- 受压持液：**AUL under pressure at rewet pressure**；⚠️ **"SAM deswelling at rewet pressure"= under development**、**"AUL Core deswelling test"= needed**
- 及时锁液：**Vortex（STM-00428）**、AUL under pressure / AFEA / ALBA / UniSPAM
- 毛细与润湿：**Capillary Pressure Quantachrome（TTM-00132）**、**Liquid Drop Test（TTM-00382）**、**Air permeability / falling head permeability Lister（STM-00151）**
- 抗压：**Compression Resilience（STM-00398）**、**Cyclic compression（TTM-00437）**
- 孔数：**Basis weight（STM-00109）**、Micro CT、Fiber size & mass ratio（microscopy）

> ✅ 验证（2026-09-29）：本追加段**未修正**本页任何既有结论——"回渗值必须连载荷与时间一起引用"**未被触及**，本批补的是**定义句的原文出处**与**参数清单（含压块尺寸/形状这一常被忽略的独立变量）**。
> 🔴 **manual_review（2026-09-29）**：源文为 **K-C 内部原则草稿（Draft 1/2/3 并存）**，含内部方法编号与"*We think not currently happening in our products & test methods*"等**内部自评句**；本页**只登记方法编号作追溯**，**不据此判定任何产品合格与否**。

## 来源 Sources

- [[KC U Rewet测试.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/KC U Rewet测试.docx.md`
- [[Rewet Learning Plan（回渗学习计划工作表）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Learning Plan.xlsx.md`（2026-09-29 追加）
- [[Depend Rewet Update 2025-04-04（LUGH 与 GRIFFIN 回渗进展）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.04.04 - Discover-DC Connect - Depend Rewet.pptx.md`（2026-09-29 追加）
- [[Rewet Method Parameters（回渗测试方法参数沿革）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Test Methods/Rewet Method Parameters.pptx.md`（2026-09-29 追加）
- [[TTM-00623高低压反渗测试.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/TTM-00623高低压反渗测试.docx.md`
- [[GB-T28004-2011 回渗渗漏.doc]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/GB-T28004-2011 回渗渗漏.doc.md`
- [[TTM-00466 BM Benefit Visualization Validation.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/BM测试方法/TTM-00466 BM Benefit Visualization Validation.docx.md`
- [[STM-00034 FIFE - Fluid Intake Flowback Evaluation Rev.5（FIFE 摄入-回渗评价全球方法）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/STM-00034 FIFE/STM-00034.pdf.md`
- [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/STM-00034 FIFE/BCC成品STM-南京南厂 1.pdf.md`
- [[Quality Finished Product STM - Tianjin Plant（质量成品标准测试方法-TJ）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/质量成品标准测试方法-TJ.pdf.md`

> ✅ 验证（2026-09-29，来源 [[STM-00034 FIFE - Fluid Intake Flowback Evaluation Rev.5（FIFE 摄入-回渗评价全球方法）]]、[[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]]）：本批补齐了本页长期缺失的**压力换算锚点**——14 ± 1 inH₂O = **3.4 kPa**（全球版）/ **3447 Pa**（南京译本），且回渗判定载荷明写为 **0.5 psi**，SAT CAP 设备上限为 **2.0 psi**（超过有内爆风险）。同时确认：**复合芯体进厂回渗用 1.20 kg / φ100 mm 压块（天津厂），成品 FIFE 用 0.5 psi 真空**——进一步坐实本页「回渗值不可裸引」的硬约束。
- [[GB-T 28004.1-2021 Absorption Tester SOP（国标吸收性能测试仪操作步骤）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/GBT28004.1-2021纸尿裤国标吸收性能测试仪操作步骤.doc.md`

---

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · ★ 回渗不是单向指标：Pull-Ups 的「反向设计」）

> 追加来源：[[Rewet Principles History and Opportunity（2025-03-04 回渗总纲与历史沿革）]]（`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.03.04 - Rewet - Josie update.pptx.md`）。
> **本追加不修正上方任何结论**；上方已确立「**回渗值不可裸引**」的硬约束，本批补入一条**更根本的约束**——**回渗连「越低越好」都不是普适的**。
> 🔴 **manual_review（2026-09-29）**：含竞品实测回渗值与内部项目代号，属竞争性技术情报，**不得对外引用**。

### 追加-1 · ★ 反向范式：Pull-Ups「LIFESAVERS」刻意**制造**回渗

| 常规降回渗设计 | **Pull-Ups 反向设计** |
|---|---|
| **更大**的孔 | **更小**的孔 |
| **更不润湿**的纤维 | **更润湿**的纤维 |
| **耐压**材料 | **可压缩**材料 |
| **足够**的容量 | **受限**的容量 |

**目的**：*"Pull-Ups is searching to **flip the normal rewet work on its head** and **intentionally create higher rewet as a learning cue**"* —— **把「湿润感」当作如厕训练的学习线索**。

**约束**：*"Goal is to identify technologies that **won't negatively impact leakage**"* ⇒ **回渗可以升高，渗漏不可以**。

> 📌 **对本页的根本性补充（最重要的一条）**：**回渗不是一个单向指标**。其**最优值取决于产品目的**——
> - **成人护理（Depend / Poise）**：追求干爽 ⇒ **越低越好**（目标 ≤0.15 g 闭式 Cradle）；
> - **训练裤（Pull-Ups）**：追求**可感知的湿润反馈** ⇒ **需要适度升高**。
>
> 因此**任何「回渗目标值」的设定都必须先声明产品目的**；把一个品类的目标值照搬到另一个品类，是**比「单位不统一」更严重的误用**。

### 追加-2 · 两大机理的位置区分（**解吸 vs 回流的分水岭**）

| 机理 | 液体在哪里 | 为何会回到吸墨介质 |
|---|---|---|
| **Flowback 回流** | **已在芯体内** | **没被锁住**（容量不足/不可达/不够快），因重力沉降在芯体 ⇒ 受压后流出 |
| **Desorption 解吸** | **卡在吸收系统（面层/导流层）里，没进芯体** | 在**压块压力下**被挤出 |

> 📌 **对本页的方法学含义**：**同一个回渗数值可能来自两个完全不同的位置**。若不清楚是哪一个，**降回渗的手段会选错**（回流要加容量/隔离，解吸要改孔径/润湿性/连通性）。这进一步**强化**上方「回渗值不可裸引」的约束——**裸引的不只是单位，还有机理归属**。

### 追加-3 · 解吸侧的两个旋钮与「孔必须连通」

| 旋钮 | 方向 | 手段 |
|---|---|---|
| **孔径（主驱动）** | 越大 → 毛细力越低 | 纤维更大 / 材料更耐压 / 克重更低（孔更少）/ **薄膜近乎无孔** |
| **润湿性（另一旋钮）** | 越不润湿 → 越不易爬升 | 整理剂水平、纤维表面能 |
| **孔网连通性** | **不连通 = dead ends 截留液体** | **面层-导流层压花**改善连通 |

> 📌 **ATACAMA+ 的「解法→原则」映射（可直接用作降回渗的检索表）**：
> | 解法 | 原则 |
> |---|---|
> | **CT5 弹性导流层** | 更大的孔 + 抗压 ⇒ 更低的持液毛细力 |
> | **更低克重导流层** | 更少的孔 ⇒ 更少可被困住的位置 |
> | **面层-导流层压花** | 孔网连通良好 ⇒ 有效排液 |

### 追加-4 · ⚠️ 竞品赛跑：目标值是移动的（**对标型指标的通用陷阱**）

| 时点 | Depend（KC） | Always Discreet（P&G） |
|---|---|---|
| ATACAMA+ 前 | **~1.6 g** | **0.20 g** |
| ATACAMA+ 后 | **统计等效** | 0.20 g |
| SIROCCO 阶段 | **0.25 g** | **0.16–0.18 g** |
| 目标 | **≤0.15 g** | — |

> ⚠️ **引用约束**：**「追平竞品当前值」不等于「取得优势」**——竞品在我方追平后仍在改进。**以竞品当前值为目标设定的验收线，在验证完成时可能已经失效**。这与本库登记的「台架最优 ≠ 使用测试最优」同属**指标外推陷阱**家族。

### 追加-5 · 影像判读的方法学注记（若用 X 光观察持液）

> *"**Water and nonwovens have the same radio opacity**, so both appear as white. **The water disappears after blotting.**"*

⇒ **不能凭亮度区分水与纤维**，只能靠**吸墨前后的差值**判读。此为**持液可视化方法的固有局限**，引用此类影像结论时须注明。

> ✅ 验证（2026-09-29）：本追加段**未修正**上方任何结论；上方「回渗值不可裸引（须带时间/压力/介质/载荷）」的硬约束**被保留并加强**，本批补的是**机理归属、目标值的品类依赖性与移动目标陷阱**。

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · 吸墨纸介质本身是结果的一部分）

> 来源：[[War on Rewet Update 2026-01-21（Depend · Poise · Huggies 三条战线基准与假设台账）]]（K-C 内部汇报）。

1. **吸墨纸（blotter）不是中性测量工具** —— 源文将「**Different blotter media collects different residual fluid, giving different test results**」单列为一个假设项。**不同介质收集到的是不同的残液 ⇒ 给出不同的结果**。**这意味着"换了一种吸墨纸"与"改了一个设计"在结果上不可区分。**
2. **该假设已进入验证阶段** —— 状态为「Testing on small scale to confirm hypothesis」，下一步是**评审 microCT 测试结果**；**用 microCT 去验证吸墨纸差异，说明怀疑的是"介质选择性收集"这一物理过程本身**。
3. **对上方"不可裸引"清单的直接补充** —— 上方已要求回渗值须带**时间 / 压力 / 介质 / 载荷**；本源把其中的"**介质**"从背景条件升级为**待验证的主效应**。**⇒ 引用回渗值时，"用了什么吸墨纸"必须与数值一起记录，且**不同介质的数值不可直接相减**。**
4. **测试变异性已被单独立项** —— 源文在 Depend 线另列「**Test method investigation**」：结果变异性使变更难以解读，**已识别变异来源，方法修改在测**。**⇒ 回渗测试的变异不只是噪声，而是足以掩盖真实设计差异的量级。**
5. **一条阴性结果（对"降润湿性"路线的决定性判据）** —— Depend 线「**Reduced liner wettability**」假设（降润湿性 ⇒ 降毛细性与残液）**因 HUT 显示泄漏升高而被移出 GRIFFIN 范围**。**这是本库第二次、也是最正式的一次否决**（前一次为 SIROCCO 的历史教训）。
6. **成人线的量级基准（供交叉索引）** —— **Depend 多在 0.25–0.35 g，Always Discreet 约 0.18 g**（**TIM-00672 Closed Cradle**，2022–2025 大批量请求，inco pants / Female Large）；**Poise 的研究级 FIUP 回渗优于其他品牌**，例外为 **Equate 4 drop 与 Poise 相近**（2025 年，inco pads 全码）。
7. **"回渗无变化但可能改善感知"的退路逻辑** —— Poise 线「**SAM in fluff layer**」假设测得**回渗无变化**，仍被推进到 **HUT 看是否改善感知**。**⇒ 当回渗不再是灵敏指标时，感知测试是合法的下一站；不应因为"回渗没动"就终止方案。**

> ✅ 验证（2026-09-29）：本节为**追加**，**未修正上方任何既有结论**（含 Pull-Ups 反向设计与"不可裸引"硬约束）。
> 🔴 **manual_review（2026-09-29）**：来源为 **K-C 内部汇报**，含**竞品实测回渗（AD 0.18 g、Depend 0.25–0.35 g）与竞品拆解判断**（"AD 不是为回渗而设计"）；**属竞品内部分析，不外发、不作对外宣称依据**。三张基准图在源文中**已退化为图注**，本页**只引用正文明确写出的两个量级**，**未提取图中数值**。

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · ★ 客户方法 NWSP 070.9 与 KC Closed Cradle 的七参数全差异）

> 来源：[[Depend Rewet Update 2025-04-04（成功标准 · LUGH-GRIFFIN-ATH 进展 · Walmart NWSP 070.9 方法对比）]]（K-C 内部汇报，2025-04-04）。

**背景**：**Walmart 就训练裤投标要求采用 NWSP 070.9.R(15)**；源文判断「**Very different from our method**，so need to submit for testing to understand differences」，并送测 **Depend Fresh Protection / Assurance / Always Discreet / LUGH 软面层** 四个产品。

| 参数 | **KC Closed Cradle** | **NWSP 070.9** | 差异性质 |
|---|---|---|---|
| **位置** | **解剖位，Cradle** | **中央垫片，平板** | **几何/受力状态不同** |
| **加液量** | **3 次 × 50 mL** | **1 次 × 105 mL** | **多次冲击 vs 单次大剂量** |
| **等待时间** | **15 分钟** | **10 分钟** | **平衡程度不同** |
| **加液压力** | **0.25 psi** | **无** | **有无外压** |
| **吸墨介质** | **2 张吸墨纸，88 × 300 mm** | **10 g 滤纸叠，直径 90 mm** | **介质种类 + 面积 + 质量均不同** |
| **回渗压力** | **0.5 psi** | **1.0 psi** | **压力翻倍** |
| **回渗时长** | **2 分钟** | **1 分钟** | **时长减半** |

1. **七个参数无一相同** —— **位置 / 加液量 / 等待 / 加液压力 / 吸墨介质 / 回渗压力 / 回渗时长**。**⇒ 两套方法测的不是同一个物理量，数值之间不存在换算关系。**
2. **压力与时长方向相反** —— **NWSP 压力更高（1.0 vs 0.5 psi）但时间更短（1 vs 2 min）**。**⇒ 不能凭"压力更高"就推断 NWSP 一定更严苛，冲量（压力 × 时间）需要计算而非直觉。**
3. **加液方式的差异最致命** —— **3×50 mL 分次 vs 1×105 mL 单次**：**前者考验多次摄入与累积残液，后者考验单次持留能力**。**⇒ 在这两套方法上排序相反是完全可能的。**
4. **吸墨介质差异已被本库独立怀疑** —— 上一节已登记「不同 blotter media 收集不同残液 ⇒ 不同结果」；本表给出**具体的介质对比（2 张 88×300 mm 吸墨纸 vs 10 g 直径 90 mm 滤纸叠）**，**介质在种类、面积、质量三个维度都不同**。**⇒ "介质"必须作为回渗值的必录字段。**
5. **可迁移判据（对任何跨方法比较）** —— **比较两套回渗方法时，先列出"位置 / 加液量 / 次数 / 等待 / 加液压力 / 介质 / 回渗压力 / 回渗时长"八项；只要有 3 项以上不同，就应视为两套不同的测试，而非同一指标的两个版本。**
6. **客户方法可以倒逼方法学建设** —— 源文的处理是**送测四个产品以理解差异**，而不是争论哪个方法更对。**⇒ 面对客户指定方法，正确动作是建立双侧数据，而不是单侧换算。**

> ✅ 验证（2026-09-29）：本节为**追加**，**未修正上方任何既有结论**（含"不可裸引"硬约束、Pull-Ups 反向设计与吸墨纸介质怀疑）。
> 🔴 **manual_review（2026-09-29）**：来源为 **K-C 内部汇报**；**Walmart 投标属客户商务活动**，本页**只记方法参数差异，不涉任何报价、投标条款或商务条件**；源文含**竞品回渗均值（AD 0.19 / Depend 0.31 / Assurance 0.36 g）与对标品牌 Tena**，**属竞品内部分析，不外发**。

## 追加：STM-00059 母本口径（2026-09-29 追加，不改动上方既有结论）

> 本节为 **Areas / Test Method 批次 06** 编译时的追加记录。上方「回渗值必须连载荷与时间一起引用」的结论**未被修改**；本节补入 **STM-00059（第 3 版）** 的完整口径，把既有"STM-00059-2 Flowback"一行从转引升级为**有源可溯**。

### STM-00059 口径明细

| 参数 Parameter | 数值 / 口径 Value | 出处 Source |
|---|---|---|
| 加载方式 Loading | **真空 14 ± 1 inH₂O = 3447 Pa**，乳胶膜覆盖；**升压时间 ≤ 30 s** | [[STM-00059 反渗.docx]] |
| 第一段 First press | **3 min ± 15 s**（含升压时间） | 同上 |
| 中间等待 Wait | **1 min** → 覆盖滤纸 | 同上 |
| 第二段 Second press | **2 min ± 15 s** | 同上 |
| 滤纸 Filter paper | **3.5 in × 12 in**；称重 **0.01 g** | 同上 |
| 滤纸定位 Position | **距绒毛前端 6 mm** | 同上 |
| 注液量（按 Size） | ST2 **150** / ST3·Med **180** / ST4·L **210** / ST5·XL **240 mL**（±0.5 mL） | 同上 |
| 靶长 Target length（自绒毛前端） | ST2 **114** / ST3 **127** / ST4 **140** / ST5&6 **146 mm** | 同上 |
| 放置 Orientation | **底膜层向下**，置于测试仪中心 | 同上 |
| 弹性处理 Elastics | 每隔 **1 in 剪开**，不剪掉、不入密合缝/绒毛区 | 同上 |
| 计算式 Formula | **反渗量 = 湿滤纸重 − 干滤纸重**（精度 0.01 g） | 同上 |
| 安全 Safety | 乳胶膜堵住通气孔有**内爆**风险 | 同上 |

> ✅ 验证（2026-09-29，来源 [[STM-00059 反渗.docx]]）：上方既有表把 STM-00059-2 记为「14±1 in WC · 3 min + 2 min」——**本次母本 SOP 将其确认为「真空 14 ± 1 inH₂O、3 min ± 15 s + 等待 1 min + 2 min ± 15 s」**，**原结论未被修正，仅补齐中间等待段与精度**。
> ⚠️ **口径差异（2026-09-29）**：STM-00059 的**注液量 150–240 mL 显著高于 FIFE 的 35–100 mL 档**，且**放置方向为底膜朝下**（与 FIFE 面层朝上相反）——**同产品跨方法读数会差一个量级，不可互推**。
> ⚠️ **待验证 `[待验证]`**：STM-00059 原文未给合格阈值（Pass/Excellent 门槛）。

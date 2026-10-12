---
type: concept
title: "Liner-Surge Embossing（面层-导流层压花）"
domain: [卫材研发, 摄入系统, 工艺工程]
status: seed
updated: 2026-09-29
tags: [LSE, 压花, 摄入, 回渗, 空体积, 图案设计]
aliases: ["LSE（Liner-Surge Embossing）", "面层-导流层压花", "PICASSO 压花图案"]
---

# Liner-Surge Embossing（面层-导流层压花，LSE）

> One-line definition 一句话定义：把**面层（liner）与 surge（面层侧顶层导流材料）压合在一起的花纹压花工艺**——它既是外观，也是摄入性能的控制变量：**压花决定了摄入系统在受压后还能保留多少空体积（void volume）**。
> (A patterned embossing bonding liner and surge together: simultaneously a visual cue and the controlling variable for how much void volume the intake system retains under load.)

## Mechanism 机理拆解

1. **空体积是唯一主控变量 Working variable = void volume**：bond 面积越大、bond 点间距越小，压合吃掉的有效空隙越多，结果是**摄入变慢、回渗升高**。
2. **强度与渗透的取舍 Strength–permeability trade-off**：更强的层间结合有利于后加工产线（converting）稳定，但以牺牲空隙为代价；因此 bond 面积与点间距必须双参数同给，不能只描述图案名称。
3. **视觉功能 Visual function**：压花在产品表面形成可见图案与"导液沟渠"的观感，可以 **替换外购供应商压花工序**而做出差异化外观。
4. **图案更换＝性能调优而非纯外观**：同一 baseline 上换图案即改变 A—C 的显著性分组（见下表），因此图案评审必须与 bench 数据同批进行。

## Key data 关键参数表

| Item 项目 | No LSE 无压花 | PICASSO | RENOIR | Source 出处 |
|---|---|---|---|---|
| FIUP 摄入 1st (s) | 21.9（分组 C） | 30.9（A） | 28.0（B） | [[Intake Tech One-Pagers（摄入系统技术一页纸管线）]] |
| FIUP 摄入 2nd (s) | — | 32.9（B） | 54.2（A） | 同上 |
| FIUP 摄入 3rd (s) | — | 38.5（B） | 65.5（A） | 同上 |
| FIUP 回渗 (g) | — | 1.42（B） | 3.14（A） | 同上 |
| 测试方法 Test method | Poise FIUP，方法号 TL-22118 | 同左 | 同左 | 同上 |
| 在役历史 Track record | — | T5 尿裤沿用约 12 年的标准图案 | 候选替代图案 | 同上 |

> ⚠️ **禁止无来源参数**：表中数据转载自上列源摘要页的 Test Results 段；字母为原表显著性分组标记（同一指标内字母不同表示统计上有差异）。该源为 PPT 抽取件，正式采用前须回原文核对。

## Design notes 设计要点

- **典型取舍 Any gain has a price**：RENOIR 相对 PICASSO 摄入更快、**回渗更高**（3.14 g vs 1.42 g）——即第 1 次摄入与回渗之间的此消彼长，须按产品定位选工作点。
- **沿用价值 Carry-over value**：新图案可在**不额外支付外部 vendor 压花成本**的前提下实现差异化外观；但同时要求 IPC 具备对应的对花（register）能力。
- **几何参数优于图案名 Geometric specs over pattern names**：设计输出应包含 bond 面积率与 bond 间距两项几何参数，使结果可被复算与跨产品追溯。

## Adjacent concepts 相邻概念

- 上位 Upstream：[[ADL（导流层）]]、[[分区密度设计]]（同样以空体积为主控变量）
- 平行 Parallel：[[ATB双梳理面层（Dual-Card Topsheet）]]、[[热风粘合无纺布]]（粘合面积面临同一 trade-off）
- 组合 Portfolio：[[IPC BCC OI Portfolio（开放创新项目组合）]]

## Verification log 验证记录

> ✅ 建立（2026-09-29，来源 [[Intake Tech One-Pagers（摄入系统技术一页纸管线）]]）：本页「bond 面积↑ → 空体积↓ → 摄入↓ / 回渗↑」的机理与该来源原文表述一致；三图案对照数据为其 Test Results 段转载。
> ⚠️ **manual_review（2026-09-29）**：同源资料含内部产品代号（T5/T6）与单位节省数值，本页不承接任何商务数据。

## 追加：Open Innovation 批（2026-09-29 追加）

> 本节为 **Resources / Open Innovation 批（批次 S4_Resources_Open Innovation_05）** 编译时的追加记录，**不改动上方既有结论**。上方「bond 面积↑ → 空体积↓ → 摄入↓ / 回渗↑」的趋势判断在本批得到**独立佐证**，但也补上了此前缺失的**净效应判断**。

### 1. 本批新增：LSE 的净效应为正，但压合会造出小空腔

- **原文判断**（[[War on Wetness - Adult Care Rewet Update（成人护理回渗进展 2026-03）]]，Teardown: Interstitial 段）：**LSE 为 Depend 建立面层—导流层连接，**压合会产生小空腔（small pockets），这对回渗不利**，但 **LSE 整体仍是净正向（net positive）**。
- **与上方可衔接之处**：本页上方机理是"bond 面积↑ → 空体积↓ → 回渗↑"（因果链为**整体压缩**）；本批补的是另一条**局部效应**——压花点周围会形成**局部空腔**，成为新的储液位置。**两条并不矛盾：整体变薄与局部空腔可以同时发生**，都会抬高残液。
- **由此得到的判据**：这一界面的最优解是**「强而均匀的结合」**，而不是「更强的压合」——HSBL DOE 在该界面上给出的结论正是"**加压合差别不大，不压合略好**"，且"**能提高结合强度的花型最好**"。详见 [[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]。

### 2. 本批新增参数

| 参数 | 数值 / 结论 | 出处 |
|---|---|---|
| LSE 的净效应 | **净正向**（压合造空腔不利，但整体仍优于不连接） | [[War on Wetness - Adult Care Rewet Update（成人护理回渗进展 2026-03）]] |
| 层间空隙的作用 | **AD 的结合强度高于 Depend（层间空隙更小）**，推测同时改善面层排空 | 同上 |
| 加压合在 DOE 中的表现 | **差别不大，但不压合略好** | 同上（HSBL DOE 结果表） |
| 花型判据 | **能给出更高结合强度的花型最好** | 同上 |
| 结合强度 vs 回渗 | **不成正比**：剥离强度最高的胶种（Henkel 5402）在残液/回渗上劣于 Rextac RT-8723 | 同上 + [[HSBL Peel Test Results（面层-导流层剥离强度实测）]] |

> ⚠️ **注意（2026-09-29）**：上表最后一行涉及**两份资料给出不同排序**——剥离强度以 Henkel 5402 最高（[[HSBL Peel Test Results（面层-导流层剥离强度实测）]]），而残液/回渗以 Rextac RT-8723 更好（[[War on Wetness - Adult Care Rewet Update（成人护理回渗进展 2026-03）]]）。**两者测的不是同一指标，不构成矛盾**；本页照录，不裁决。

### 3. 验证记录

> ✅ 验证（2026-09-29，来源 [[War on Wetness - Adult Care Rewet Update（成人护理回渗进展 2026-03）]]）：本页上方"空体积↓ → 回渗↑"的机理在本批被**独立复现并细化**——压花在**减少整体空体积**的同时还会**在压点周围造出局部空腔**，两者都是残液的藏身处。原页结论**未被修正**，但需补一条**净效应判断**：即便有这两项副作用，**建立层间连接整体仍优于不连接**。

- **追加 `[待验证]`**：压花花型（形状/深度/密度）与"局部空腔体积"的定量关系；是否存在既保证结合强度又不产生空腔的花型。

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · 同一机理在婴儿线"已证明"、在成人线"不鼓舞"）

> 来源：[[War on Rewet Update 2026-01-21（Depend · Poise · Huggies 三条战线基准与假设台账）]]（K-C 内部汇报）。

| 产品线 | LSE 假设 | 状态 | 下一步 |
|---|---|---|---|
| **Huggies（婴儿）** | 面层与 surge 更好的连接 ⇒ 排空面层 ⇒ 减少残液 | **连接已证明（Connection proved）** | **与 BB T5 一同推广（Roll out with BB T5）** |
| **Poise（成人垫）** | 同上 | **早期结果有希望，但最近的数据不太鼓舞** | 深挖最新数据以理解 |
| **Depend（成人裤）** | **LSE 净效果是回渗正向，但换一种施胶配置可能更好** | Code 已产出，分析进行中 | 2/13 评审，确定完整产品 code 以验证假设 |

1. **LSE 首次被明确标记为"已证明"** —— Huggies 线状态栏直接写 **"Connection proved"**，下一步是**商业化推广**。**这是本页迄今最强的正向证据。**
2. **⚠️ 但同一机理在另一条线上结论相反** —— **Poise 线"早期有希望、最近的数据不太鼓舞"**。**⇒ 同一机理的结论不可跨产品线平移**，必须**逐线验证**。
3. **机理表述在三处完全一致** —— "Better connection between liner and surge will allow draining of liner, reducing residual fluid"（**排空面层**而非"阻挡液体"）。**说明 LSE 的作用是排水，不是隔水**。
4. **Depend 线的推进方向从"压花"转到了"施胶"** —— 源文在 Depend 线把抓手改写为**"LSE 净正向，但换一种 adhesive setup 可能更好"**，即**在压花已成立的前提下，继续优化粘接配置**。
5. **可迁移判据** —— **评价任何"层间连接"类改进时，判据应是"能否排空面层"，而不是"是否增加了结合强度"**；**连接强度与排水能力不是同一指标**。

> ✅ 验证（2026-09-29）：本节为**追加**，**未修正上方任何既有结论**（含上一节 LSE 净效应与压合副作用）。
> 🔴 **manual_review（2026-09-29）**：来源为 **K-C 内部汇报**，含**竞品回渗基准与内部项目代号**（BUFF BABY、BB T5、GRIFFIN 等）；本页**只记 LSE 机理与状态**，**不落竞品数值、不外发**。三张基准图在源文中已退化为图注，**本页未提取图中数值**。

## Sources 来源

- [[War on Wetness - Adult Care Rewet Update（成人护理回渗进展 2026-03）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Updates and Presentations/2026.03.16 - Adult Care Manager Rewet Update.pptx.md`（2026-09-29 追加：LSE 净效应与压合副作用）
- [[Intake Tech One-Pagers（摄入系统技术一页纸管线）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Intake/Tech One Pagers.pptx.md`
- [[Topical liner Supporting layer Embossing pressure.pdf]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/Topical liner Supporting layer Embossing pressure.pdf.md`（2026-09-29 追加）

## 追加：压花强度的厂内量化方法（2026-09-29 追加，不改动上方既有结论）

> 本节为 **Areas / Test Method 批次 05** 编译时的追加记录。上方 LSE 机理与"判据应是能否排空面层"的结论**未被修改**；本节补入把**压花结合强度**变成可验收数字的方法 **WI-57507**。

### WI-57507 口径（3D 面层 ↔ 支持层 压纹压合强度）

| 参数 Parameter | 数值 / 口径 Value | 出处 Source |
|---|---|---|
| 方法编号 Method ID | **WI-57507**（第 1 版，2022-10-17） | [[Topical liner Supporting layer Embossing pressure.pdf]] |
| 被测界面 Interface | **Topical / 3D liner ↔ Supporting layer** 的压纹压合 | 同上 |
| 环境 Conditioning | **23.0 ± 1.0 ℃ / 50.0 ± 2.0% RH 恒温恒湿** | 同上 |
| 程序 Programme | **复用 STM-00078**，夹具距离 **2 in** | 同上 |
| 夹具气压 Clamp pressure | **≤ 0.6 MPa** | 同上 |
| 取样定位 Positioning | Pad 前端下 **50 mm** 起剪；再下 **50 mm**（起点）/ **150 mm**（终点）→ 测试区 **100 mm** | 同上 |
| 试样宽度 Width | 纵向剪 **15 mm（CD）**，并**移除吸收体** | 同上 |
| 预制剥离 Pre-peel | 自 50 mm 端撕开 3D 面层与支持层至 50 mm 标记，形成夹持端 | 同上 |
| 读数 Readout | **峰值 gf** | 同上 |
| 合格阈值 Threshold | 原文未给 `[待验证]` | 同上 |

> ✅ 验证（2026-09-29，来源 [[Topical liner Supporting layer Embossing pressure.pdf]]）：本页既有结论「**连接强度与排水能力不是同一指标**」在厂内方法中得到印证——压花强度被做成**独立的峰值 gf 验收项**（WI-57507），**与摄入/回渗类指标分开测量**，说明厂内也是"强度归强度、排水归排水"两条线。
> ⚠️ **待验证 `[待验证]`**：WI-57507 未给出合格阈值，也未给出"压花强度 ↔ 空体积"的定量关系；上方 PICASSO / RENOIR 数据来自另一条来源，**两者不可直接换算**。
> 📌 同族方法：[[Seal Strength Test（端封·侧封强度测试）]]（母方法 STM-00078）、[[Product Waist Break Test（产品腰围拉断测试）]]（派生 STM-01086）——见 [[峰值 gf 粘合强度方法族对比（端封 vs Pants 拉断 vs 面层压纹）]]。

## 追加：同一界面的第二条方法 WI-56934（2026-09-29 追加，不改动上方既有结论）

> 本节为 **Areas / Test Method 批次 06** 编译时的追加记录。上方 WI-57507 与 LSE 机理结论**未被修改**；本节补入**同一界面（3D 面层 ↔ 支持层）的第二条方法**，并明确两者差异。

| 参数 Parameter | **WI-56934**（在线复合） | **WI-57507**（压纹压合，上一节） | 出处 Source |
|---|---|---|---|
| 名称 Name | CIDER 3D Embossing Lamination Strength | Topical liner / Supporting layer Embossing pressure | [[面层粘合强度测试方法.pdf]]、[[Topical liner Supporting layer Embossing pressure.pdf]] |
| 夹具间距 Gauge | **50 mm** | **2 in（≈50.8 mm）**，复用 STM-00078 | 同上 |
| 拉伸速度 Speed | **300 mm/min** | 未明示（继承 STM-00078）`[待验证]` | 同上 |
| 试样 Specimen | **2 in × 200 mm（MD）**，只含 3D 压花、**不含侧封边** | **100 mm × 15 mm（CD）**，移除吸收体 | 同上 |
| 终止条件 Stop | **两层完全分开时自动停止返回** | 由 STM-00078 程序控制 | 同上 |
| 环境 Conditioning | 未明示 | **23 ± 1 ℃ / 50 ± 2% RH** | 同上 |
| 读数 Readout | 峰值 **gf** | 峰值 **gf** | 同上 |

> ⚠️ **同一界面两套方法说明什么（2026-09-29）**：厂内是**按工序建方法**而非按界面建方法——**在线复合**归 WI-56934、**压花压合**归 WI-57507。**引用必须写清 WI 号与试样尺寸**，否则两个 gf 值会被误当成同一指标的趋势数据。详见 [[3D 面层-支持层结合强度两法对比（WI-56934 vs WI-57507）]]。

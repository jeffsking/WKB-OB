---
type: concept
title: "ActiveTech Platform（ActiveTech 在线薄芯体平台）"
domain: [卫材研发, 芯体工艺]
status: growing
updated: 2026-09-29
tags: [ActiveTech, 在线成型, 无绒毛浆, 真空成垫, D-wrap, SAP 计量, 芯体工艺]
---

# ActiveTech Platform（ActiveTech 在线薄芯体平台）

> One-line definition 一句话定义：**在线连续生产薄型无绒毛浆吸收芯体**的制造平台与工艺能力——它产出的芯体构造即 [[Blizzard Core（Blizzard 芯体结构）]]，其产品实现即 [[ROTC（Real Online ThinTech Core）]]。（中文：平台 = 工艺能力；构造 = Blizzard；产品 = ROTC。）

## Mechanism / Structure 机理 / 结构拆解

1. **Scope 定义范围**：ActiveTech enables **continuous, online formation** of Blizzard-type cores。在 ROTC 实现中包含：**ACF module**、**SAP feeding and metering**、**vacuum-assisted formation and transfer**、**wrapping/folding**、**core sealing**。
2. **Critical process control 1 — SAP metering and distribution SAP 计量与分布**：ROTC uses **volumetric feeding** and **can employ two feeders**。（中文：体积式供料，可用双供料器——对应 SAP 分层/配比可编程。）
3. **Critical process control 2 — Vacuum and web transfer 真空与转移**：low-fluff or fluffless structures are **sensitive to vacuum conditions and pad formation**。（中文：低浆/无浆结构对真空条件与成垫状态更敏感，是无浆工艺的稳定性瓶颈。）
4. **Critical process control 3 — D-wrap folding and containment D-wrap 折叠与包裹**：SAP loss or **"flying"** at the conveyor and folding zones must be controlled。中文：输送与折叠区的**SAP 飞失**是无浆工艺特有的物料损失与洁净风险。
5. **Critical process control 4 — Adhesive selection and add-on 胶的选择与添加量**：too little adhesive risks poor integrity；too much can **reduce accessible void volume and slow intake**。（中文：与 [[Blizzard Core（Blizzard 芯体结构）]] 的 ≈5 % of SAM weight 配置互为呼应。）
6. **Why "online" is the whole point 为什么「在线」是关键**：Blizzard 的价值不止于去浆，而是**在线**制造出「薄、柔、结构稳固」的 SAP/胶芯体——即把原本需要离线工序（如 [[BNC-PEG 母粒（干态可复水中介体）]] 那类中间体路线）承担的结构功能，用**连续成型 + 胶固 + 包裹**在同一条线上完成。
7. **Known failure modes are all kinetic 已知失效模式都属动力学**：实测的代价项为**第三次摄入变慢**与**漏尿趋势上升**（见 [[ROTC（Real Online ThinTech Core）]]），说明平台的难点在**摄入/导流**而非容量。
8. **Library positioning 库内定位**：与 [[COCO芯体平台]]、[[TBCW结构]] 同属「芯体平台」类页面——本页是库内**唯一以「无绒毛浆 + 在线成型」为特征的芯体平台**。

## Key Parameter Table 关键参数表

| Parameter 参数 | Typical value / range 典型值 / 范围 | Source 出处 |
|---|---|---|
| Process modules 工艺模块 | ACF module；SAP feeding & metering；vacuum-assisted formation & transfer；wrapping/folding；core sealing | [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]] |
| SAP feeding SAP 供料方式 | volumetric feeding；can employ **two feeders** | 同上 |
| Vacuum sensitivity 真空敏感性 | low-fluff / fluffless structures 对真空条件与成垫敏感 | 同上 |
| SAP loss 物料损失 | "flying" at conveyor and folding zones（D-wrap 折叠/包裹须控制） | 同上 |
| Adhesive control 胶控制 | selection + add-on；过少损整体性、过多减空隙体积与摄入 | 同上 |
| Output construction 产出构造 | Blizzard：顶面层/包裹 → SAM + 胶 → 底面层/包裹 | 同上 |
| Product implementations 产品实现 | ROTC Slim / Fluffless；ROTC HBC（hybrid core + pad channel） | 同上 |
| Measured outcome (adult HBC) 实测结果 | 厚度 5.5 → 4.4 mm；高压回渗 2.67 → 0.40 g；保液 ≈700 g；第三次摄入变慢 | 同上 |
| Measured outcome (baby Slim) 实测结果 | 厚度与回渗改善；cradle intake 变慢；漏尿趋势上升 | 同上 |
| Line speed 线速 | **来源未提供** | `[待验证]` |
| Cost 成本 | **来源未提供** | `[待验证]` |
| Supplier / equipment vendor 设备供应方 | **来源未提供** | `[待验证]` |

> ⚠️ **No unsourced parameters 禁止无来源参数**：本批来源**完全没有提供线速、产能、设备供应方与成本数据**——这三项是本库对「芯体平台」类页面最关心、也最常被用于选型比较的信息，现全部标 `[待验证]`。上表实测值属内部测试口径，未标样本量与测试方法。

> 🔴 **manual_review（2026-09-29）**：源文提及 **ACF 模块、双供料器与 D-wrap 折叠/密封的具体产线实现**，属工艺配置信息；依 AGENTS.md §5，**具体设备型号、产线布局与设备供应关系不页面化**，本页仅保留功能性描述。

## Adjacent Concepts 相邻概念

- 产出构造与产品 产出构造与产品：[[Blizzard Core（Blizzard 芯体结构）]]、[[ROTC（Real Online ThinTech Core）]]
- 材料侧材料侧：[[绒毛浆（Fluff Pulp）]]、[[SAP性能指标（CRC AUL GBP Vortex）]]、[[SAP错峰膨胀]]
- 结构设计 结构设计：[[分区密度设计]]、[[ADL（导流层）]]、[[毛细梯度设计]]、[[亲水-疏水梯度设计]]
- 库内同类平台 库内同类平台：[[COCO芯体平台]]、[[TBCW结构]]
- 对照：[[芯体测试方法与验收基准（STM）]]

## Lessons Learned 经验教训

> ✅ Verification（2026-09-29，source [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]]）：本页的四项关键工艺控制与源文一一对应，未作外推。其中两条与库内既有经验互证——①「胶用量过多减空隙体积、拖慢摄入」与 [[ADL（导流层）]] 的**空隙体积不可让步**判断同向；②「无浆结构对真空与成垫敏感」与 [[Formation-Limited Barrier（阻隔的成形受限机理）]] 的**成形均一性决定性能**逻辑同构（不同工序，同一规律）。（中文：均为同向印证，无矛盾。）

- **Lesson 1（无浆平台的瓶颈在物料搬运，不在配方）**：四项关键控制里三项是「搬运与成型」（SAP 计量、真空/转移、D-wrap 包裹与飞失），只有一项是配方（胶）。评估此类平台时应把**物料平衡与洁净**放在化学之前。
- **Lesson 2（「在线」是差异化来源）**：与离线的中间体路线（如 BNC-PEG 干颗粒）相比，ActiveTech 的差异化是把结构稳定性做在**同一条连续线上**——因此它的风险不在工艺复杂度，而在**线速与成垫稳定性**（本批未给数据，须补）。
- **Lesson 3（不要用容量指标验收薄芯体）**：实测显示保液容量基本不变（≈700 g）而摄入变慢——**薄芯体的验收指标应放在摄入动力学与防漏上**。
- **待补 `[待验证]`**：线速与产能（与库内 [[COCO芯体平台]]/[[TBCW结构]] 可比口径）；设备供应方与改造成本；真空/成垫的工艺窗口（真空度-线速-克重）；双供料器下的 SAP 分层配比能力上限。

## 追加：Open Innovation 批（2026-09-29 追加 · Spring Portfolio 2026 路线图）

> 追加来源：[[ActivTech Spring Portfolio 2026（ActivTech 春季组合评审）]]（2026-04 创新评审）。本次追加补齐本页原先标 `[待验证]` 的**路线图、线速与成本口径**，**不改动上文任何既有结论**。

### A. Platform positioning 平台在代际框架中的位置

| Generation 代际 | 构型 | ActivTech 的位置 |
|---|---|---|
| Gen 1 Blends（Legacy） | 在线气流成形 SAM/fluff | 不适用（前代） |
| **Gen 2 Laminates（Ready now）** | 层压结构，兼顾防漏与轻薄/柔性 | **在线：ActivTech、Coco**；离线：Spinform、Spinflex、BONNIE |
| Gen 3 Engineered unitary composites（Ready next/future） | 工程化整体复合材料 | 离线 BONNIE（GoodNites 2028+；Poise/Kotex/Depend 2028） |
| Gen 4 | BONNIE 延续 | 2028+ |

> 中文：ActivTech 在库内定位由"无浆在线平台"进一步明确为 **Gen 2 的在线分支**——与 [[COCO芯体平台]] 并列为在线路线，与 Spinform/Spinflex/BONNIE 等离线路线分庭。

### B. Roadmap 路线图（AT 2.0 / AT 3.0 / Next Gen）

| 版本 | 技术手段 | 目标 | Readiness |
|---|---|---|---|
| AT 2.0 **SAM Zoning** | SAM 流**每秒脉冲 21 次**实现策略性分区投放 | 最多**去 2 g SAM/片**，节省 **$2–4/SU** | **Product TRL 4 / Process TRL 5**；on track **$2/SU by 2028** |
| AT 3.0 **Shaping/Patterning** | 芯体成型 / 通道 / 图案 | 2028+；须**维持与 AT1.0 持平的渗漏与台架** | 额外收益待验证 |
| Next Gen AT | — | **最低成本下最佳性能；渗漏稳定 ≤4%** | 2026 平台 → AT2.0 2028 Battleship（中国 2027）→ AT3.0 2028+ |

> ⚠️ **重要边界（2026-09-29）**：HUT 40835 中"去 2 g 的 AT 2.0 **未对渗漏产生负面影响**"与"**整体渗漏高于预期**（约 5.7%–7.2%）"两句**并存于源文**。前者是相对判定、后者是绝对水平，二者不矛盾，但**是否与 ≤4% 目标相容需人工确认**——本页照录，不裁决、不换算。

### C. 补齐此前的 `[待验证]` 项

| 此前待验证项 | 本次追加的取值 | 备注 |
|---|---|---|
| **Line speed 线速** | 试产 **ADL 1000+ ppm**；**B15 @ 1281 ppm** | 试产口径，非量产保证值 |
| **Cost 成本** | AT2.0 Zoning 节省 **$2–4/SU**（MD Zoning 口径 $2–3/SU，年 $6–12MM）；Capex **$0.4–0.5MM/asset** | 🔴 商务敏感，仅记量级 |
| **Supplier / equipment vendor 设备供应方** | 仍**未提供** | 保持 `[待验证]` |

### D. 与既有经验的互证 / 张力

- **同向**：AT 3.0 要求"成型不得劣化防漏"，与上文 **Lesson 3（不要用容量指标验收薄芯体，验收看摄入动力学与防漏）** 完全同向。
- **同向**：AT 2.0 靠**减 SAM 而非减结构**换成本（去 2 g），与上文 Lesson 1 的"瓶颈在物料搬运与成型、不在配方"并不冲突——分区改变的是**分布控制**，仍属成型侧。
- **新增张力（不裁决）**：源文把分区（Zoning）列为**最大单项降本杠杆**（-$1.55/SU，含 $0.12/SU 资本），而库内 [[分区密度设计]] 页把分区定位为**方向级架构调整**（服务于输运与 SAP 分布）。二者视角不同（成本 vs 结构），**并列记录，不合并**。

> ✅ Verification（2026-09-29，source [[ActivTech Spring Portfolio 2026（ActivTech 春季组合评审）]]）：本次追加的四项内容（代际定位、AT2.0/AT3.0 路线图、线速、成本量级）均直接引自源文，未作外推；成本与资本数据已按 AGENTS.md §5 降级为量级并标 manual_review。

## 追加：Meeting Minutes 批（2026-09-29 追加 · 2026-09-03 全球对齐会）

> 本节为 **S5_Areas_Meeting Minutes_01 批次（[[Global Online Embossing Platform & Active Tech Direction Review（录音纪要 2026-09-03）]]）** 编译时的追加记录，**不改动上方既有结论**。

### 1. 2.0 / 3.0 的物理边界（本批首次量化）

| 版本 | 路线 | 本批判断 |
|---|---|---|
| **2.0** | 用**气吹**把堵住的 SAP 吹掉来形成 pattern；系统复杂、可控度不高 | 对比另一种方式（**机械手「撸掉」**）更安全；报价量级约 **400 k**（各国摊派口径）`[待验证]` |
| **3.0** | solar valve **on/off**，类似 3D 打印逐单元投放 | 单元尺寸现 **14 mm** → 目标 **7 mm**、想做 **2 mm**；但受限于 ① 开关速度、② 下落精度、③ **SAP 固化/受潮后不能干净落下**（需要时间才落得下）→ **判断实际做不到 2 mm**，且**能耗更高** |

### 2. 方向决策的时机与组织现实（本批新增）

- **北美**仍在研究 3.0 并拟 **11 月决策**；我方（亚太侧）内部已倾向放弃，但**当前不是告知北美的合适时机**，拟于 **10 月 workshop 之后**再谈，且需论证「转向 active 方向 capex 更低」。KC 侧方向**尚未确认**。
- **平台化的真正缺口是可交付性**：global 在没有产品设计时先开发平台（属工程技术准备），**local 以落地为主**；缺一名**专职工程资源**作为全球开发方与各市场 local 团队之间的固定接口，用于把方案标准化并交付执行 → **目前没有这个资源**。
- **不可能为每个市场单独开发工程方案**，也不能只做一套不顾差异 → 需要定义「可 handed over、便于 local 改装（retrofit）」的技术就绪度门槛，**该门槛未定义**。

> ⚠️ **矛盾记录（2026-09-29）**：本批对 3.0 的判断（「做不到 2 mm / 能耗高」）与北美仍在推进 3.0 并于 11 月决策的立场**存在张力**；本页**不裁决**，仅登记待人工确认。

> 🔴 **manual_review（2026-09-29）**：本批含模块与平台报价量级、北美决策时点与全球方向对齐信息，**本页不复制报价**；要点留存于源摘要页。

## 追加：Meeting Minutes 批（2026-09-29 追加 · ROTC 的离线/在线分工与三类产品产出）

> 来源：[[Kirigami Process, LSE Bonding & Pattern Pitch Review（不同人员自我介绍交流）]]（K-C 内部现场交流会 ASR 转写，会议日期 [待验证]）。本批只**追加**，不修改既有结论。

**ROTC 的工艺分工（本批新增）：**

| 环节 | 执行方式 | Note 备注 |
| --- | --- | --- |
| ROTC 工艺本身 | **离线（offline）** 执行 | 会中明确 "we make the ROTC process offline" |
| 与常规产线结合 | **在线（in line）** 与 conventional floor plan 结合 | — |
| 结果 | 可产出**三类产品**：① conventional（常规）产品；② **hybrid（混合）**产品；③ 另一类产品（转写不清，[待验证]） | — |

- 表述口径："我们是 Active Technology，幸运地应用了我们的 active technology，offline not in line……我们把 ROTC 工艺放在离线，在线上则是与常规产线结合，这样我们可以生产三类产品。"
- 会中另提及一个数值「nineteen degree / 十九度」，上下文不足，**含义待核** [待验证]。

**与 Kirigami 的关系（本批新增）：**

- Kirigami（切割 + 拉伸开孔）工艺在本批讨论中**独立于 ROTC**，且**只用于 surge**、从未用于面层；两者属于不同的工艺路线，未在本批中被合并。
- 共同点：二者都涉及**拉伸带来的形变**，且都需要**在线根据材料调整**参数。

✅ **验证记录（2026-09-29）**：ROTC 离线执行的分工为会中口径；「三类产品」中第三类的具体所指转写不清，标 `[待验证]`。参见 [[ROTC（Real Online ThinTech Core）]]、[[Kirigami Apertured Nonwoven（切割拉伸开孔工艺）]]、[[TBCW结构]]。

## 追加：Meeting Minutes 批（2026-09-29 追加 · ActivTech 的专利属性、自研替代与"薄型化—凝胶阻塞"矛盾）

> 来源：[[Diaper NPD Workshop Prep — Absorbency, Skin Health & Comfort Feature Map（2026-06-05）]]（Workshop 准备材料 v1.0，2026-06-05）。本批只**追加**，不修改既有结论。

**ActivTech 的定位（本批新增，外部视角）：**

| Item 项目 | 内容 |
| --- | --- |
| 原理 | **100% SAP 在线制造吸收芯体** |
| 适用 | **无木浆（Woodpulp-Free）** 与**混合型**两种方案 |
| 属性 | **KC 专有技术，需规避专利** |
| 自研替代路径 | **Blizzard 技术**（文档给出的对标自研方向） |
| 目标 | 芯体厚度 **<2.0 mm**；生产成本 **-10–15%** |
| 优先级 | ⭐⭐ **中**（被**专利风险**拉低） |

**薄型化的核心矛盾（本批新增，是本平台的关键工程约束）：**

> **薄型化 → SAP 载荷密度↑ → 凝胶阻塞风险↑**
> 文档给出的解法：**多 SAP 层系统 + GBP 优化 SAP 牌号选型**。

- 与本页既有记录的衔接：本页已记 AT 的在线成形与薄型化特征；本批补充了**薄型化的代价是凝胶阻塞**，以及**用分层 + GBP 选型对冲**的具体路径。
- 行业标杆（文档口径）：**花王妙而舒 0.1 cm（1.0 mm）超薄芯**。

**由此得到的认知（本批新增）：**

1. **ActivTech 的价值不在"薄"，而在"成本 -10–15%"** —— 薄是手段，成本才是差异化；这也解释了为什么自研路线（Blizzard）值得投入。
2. **专利属性改变了优先级排序**：技术本身评级高，但因"KC 专有、需规避专利"被 Workshop 降到 ⭐⭐ —— **专利风险可以独立否决一个高性能方案**。
3. **"薄"有一个物理下限，由凝胶阻塞决定** —— 减薄不是无代价的；评估超薄方案时必须同时评估 **GBP**（[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]）。
4. **去木浆 + 在线制造 = 双刃**：省掉木浆与离线成型环节，但把**渗透性的重任**全部压到 SAP 本身 → 这也是为什么 GBP 优化选型会成为解法的关键一环。

> 🔴 **manual_review（2026-09-29）**：本页涉及成本降幅（-10–15%）、竞品定位与专利规避策略，属商务与 IP 敏感信息；按 AGENTS.md §5 只保留机制性结论。请回原文核对：
> `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/Workshop_Prep_Absorbency_SkinHealth_Comfort_2026.md.md`

✅ **验证记录（2026-09-29）**：以上为 **Workshop 准备材料 v1.0** 口径（属**外部/竞品视角**的描述），引用 `references/51`、`references/52` **原始文件未随本批次提供**；"KC 专有需规避专利"与 Blizzard 对标为文档判断 [待验证]。参见 [[COCO芯体平台]]、[[Composite Core Patent Clearance（复合芯体专利规避审查）]]、[[Multilayer SAP Core（多层SAP芯体）]]、[[Fluff-Free 4th-Gen Absorbent Core（无木浆第四代芯体）]]。

## Sources 来源

- [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Active Hygiene/blizzard_activetech_explained.md.md`
- [[ActivTech Spring Portfolio 2026（ActivTech 春季组合评审）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Structure/ActivTech Spring Portfolio 2026.pptx.md`（2026-09-29 追加）
- 源文引用的内部资料：ROTC Operations Training；YK Absorbent Core_Global ActiveTech Forum_May 2024；ROTC HBC POV_Mar.2026

---

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · AT Hybrid 回渗归因）

> 追加来源：[[Depend Ultra-Low Rewet M2M Learning Share（2025-04-22 面层与 ActivTech 芯体）]]（`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.04.22 - M2M learning share - Depend ultra low rewet.pptx.md`）。
> **本追加不修正上方任何结论**；上方为平台**路线与组织决策**层面，此处补入平台在**超低回渗（≤0.15 g 闭式 Cradle）**场景下的**技术表现与未解耦归因**。
> 🔴 **manual_review（2026-09-29）**：本追加涉及**成人护理竞品（Always Discreet / Depend 主线）实测对比**与内部项目代号（GRIFFIN / ATACAMA+ / MOJAVE / SIROCCO），属竞争性技术情报，不得对外引用。

### 追加-1 · 头对头结果：AT Hybrid **确实抬高回渗**

在带 LSE 的 Depend 样品上做头对头（芯体由 ADL 产出、成品由 GML 产出、GADT 实验室测试），**AT Hybrid 芯体系统使回渗升高**。同时变化的差异项：

| 差异项 | SAM/Fluff | AT Hybrid |
|---|---|---|
| 包裹层 Wrapsheet | 17gsm tissue | 12gsm dSB |
| 面层 Liner | 12gsm SB，未印花 | 12gsm SB，印花 |
| 导流层 Surge | Shalag SS7CT5H80 | Shalag SS7CT5H80（**相同**） |
| Liner-Surge 压花 | Yes（2024 GRIFFIN HUT 产品） | **Light** |

> ⚠️ **归因未解耦**：包裹层、面层印花、压花强度**三者同时变化**，任一项都可能是成因。见 [[Liner-Surge Embossing（面层-导流层压花）]]。

### 追加-2 · 六条候选归因与本批证据状态

| 候选归因 | 本批证据 | 状态 |
|---|---|---|
| **层数更多 ⇒ 更多持液位点** | 机理假设「more layers = more places fluid can be trapped」；**需无 SAM 样品做诊断** | 待验 |
| **绒毛浆自身持液** | 提出「应把绒毛浆视为 AT 系统**吸收系统的一部分**」，而非仅结构填充 | 待验（**关键**） |
| **少量 SAM 能否解吸绒毛浆持液** | 明确提出该机理问题，尚未有数据 | 待验 |
| 包裹层 dSB vs tissue | SIROCCO 测试**未发现差异**；TABCW 包裹层曾在 BUFF BABY 与 KCM（尿片）有效 | 弱证据，待复验 |
| 卷曲纤维加入包裹层 | 尚无样品，仅列为候选 | 未验 |
| **总容量更低** | AT Hybrid 容量低于 SAM/Fluff；**低容量是 GRIFFIN 上市的不可让步项**；SAM/Fluff 体系中容量对比**未显示影响回渗** | **矛盾未决** |

### 追加-3 · 下一步诊断矩阵（2025-03 芯体 / 2025-04—05 成品）

| 包裹层 | 绒毛浆 | SAM | 设计意图 |
|---|---|---|---|
| 12gsm dSB | Standard | Standard | 基线 |
| 20gsm BCW | Standard | Standard | 包裹层变量 |
| 12gsm dSB | Standard | **None** | **诊断组**：隔离绒毛浆持液 |
| 20gsm BCW | Standard | **None** | **诊断组**：包裹层 × 绒毛浆交互 |
| 12gsm dSB | **+30% SAM** | Standard | **机理验证**：检验 SAM 是否解吸绒毛浆持液 |

> 📌 **方法学要点**：矩阵中**两组「No SAM」是纯诊断组**（成品层面不可用，仅作机理隔离），**「+30% SAM」是机理验证组**。这是本批中**结构最清晰的一次「先解耦、再优化」设计**，可作为薄芯体类项目 DOE 的模板。
>
> ⚠️ **与上方路线的张力（2026-09-29 登记，不裁决）**：上方记录 AT 3.0 方向存在「做不到 2 mm / 能耗更高」的判断与北美推进立场的张力；本追加显示，**即便成型路线可行，AT 芯体在超低回渗场景下仍存在尚未归因的性能代价**。二者**不构成因果**，但共同指向：AT 平台的**性能边界尚未闭合**。

---

### 追加 B：Resources/Open Innovation 批（2026-09-29 追加 · AT vs 外部复合芯体的工艺根源）

> 追加来源：[[ADT POV 2025 Complex Core Strategy（ActivTech vs 外部复合芯体）]]（`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Structure/Complex Core Strategy ADT 2025.docx.md`，2025）。
> **本追加不修正上方任何结论**；上方为**路线与组织**层面，此处补入**「AT 与外部复合芯体为何性能可比而成本不同」的工艺根源**——这是上方成本讨论中缺失的一环。
> 🔴 **manual_review（2026-09-29）**：本节涉及**资产投资额、年度物耗增量、ECM 名单与 IP 释放策略**，仅保留**技术判据与相对关系**，具体金额与伙伴名单不页面化。

#### 追加 B-1 · 工艺根源：**喷什么、按什么顺序喷**

| 要素 | ActivTech / Blizzard | 外部复合芯体（如 Zuiko） |
|---|---|---|
| **成芯方式** | **SAM/胶网络整体喷涂到基材** | **先喷胶到基材 → 再把 SAM 落到胶上** |
| **胶添加量** | **2.5~5%**（AT Hybrid，Buff Baby） | **11~12%**（印尼 Zuiko，为维持完整性） |
| **所需非织造布** | **最多 2 层** | **需额外非织造布**才能走通工艺 |
| **结果** | 芯体一致性好、SAM 固定化好、速度高 | **同等性能下物耗更高**（胶 + 面层/包覆） |

> 📌 **机理读法**：外部路线「**先胶后 SAM**」意味着 **SAM 落在胶层之上**，需要**足够厚的胶层**才能抓住颗粒（⇒ 胶添加量高），并需**额外包覆层**防止掉粉与走机（⇒ 非织造布多）。AT 的「**SAM/胶共喷成网**」把两个功能合成为一次沉积 ⇒ **同样性能、更少物料**。这是「**工艺顺序决定物耗**」的教科书式案例。

#### 追加 B-2 · 性能对比模式：外部芯**不吃亏在回渗，吃亏在摄入**

| 时间 | 对比 | 结果 |
|---|---|---|
| 2025-01 | 越南 ActivTech vs 印尼 **Zuiko** 复合芯 | AT **摄入更快**，**回渗相当** |
| 2024-11 | 中国 **豪悦**复合芯 vs AT Hybrid | 外部芯**摄入更差**、**容量更高**、**高压回渗更低**，但**成本更高** |
| 2024 | **Winsun** 复合芯（配中国产线绒毛浆）vs AT Hybrid | **假人测试相当** |

> ⚠️ **与本节「追加 A」的方向关系（重要，避免误读矛盾）**：
> - **追加 A**：AT Hybrid **相对 SAM/绒毛浆芯** → **回渗更高**（AT 的代价）
> - **追加 B**：外部复合芯 **相对 AT** → **摄入更差、回渗相当甚至更低**
>
> 二者**参照系不同（AT 的对手分别是 SAM/绒毛浆芯与外部复合芯）**，**不构成矛盾**；合起来可读出：**回渗排序大致为「外部复合芯 ≤ AT Hybrid」而「SAM/绒毛浆芯 ≤ AT Hybrid」，AT 的相对短板在回渗，相对长板在摄入速度与物耗效率**。

#### 追加 B-3 · 速度能力与资产门槛

| 项 | ActivTech | 外部复合芯体 |
|---|---|---|
| **分区（zoning）速度** | **1000 ppm**（AT 2.0 已达成；更高速度开发中） | **400 ppm**（Zuiko 印尼启动） |
| 无分区商业化速度 | **1100 ppm**（AT 1.0，U03/U04/U07） | — |
| **增量资产成本** | **~$1.2 MM/组件/产线**（假设产线已有绒毛浆与 SAM 端） | **无**（利用 ECM 现有设备） |

> 📌 **决策结构**：**一次性资产投入（$1.2 MM/线）** 换 **持续性物耗节约**；外部路线的「零资产成本」前提是**整只产品在 ECM 生产**，且**以每年多耗的胶与包覆材料为代价**。

#### 追加 B-4 · ⚠️ SWOT 自陈劣势（原文列出，对本平台的能力边界有直接约束力）

| 劣势 | 含义 |
|---|---|
| AT 无绒毛浆版**相对 SAM/绒毛浆芯上机成本更高** | 与上方「AT 具有成本优势」的说法**限定条件不同**——成本优势是**相对离线 SAM 贴合/复合芯**，**不是相对在线 SAM/绒毛浆芯** |
| **首次摄入时间与液体扩散更差** | 与追加 A 的「AT Hybrid 抬高回渗」**同向**：AT 的短板集中在** intake 侧** |
| 部分实现**手感偏沙砾感（grittier feel）** | 消费者可感知风险 |
| **BLIZZARD 层的 SAM 无法回收（no solution for reclaiming SAM）** | **废料回收的可持续性缺口**，与单一材质/可回收叙事冲突 |
| **专利保护范围有限**；P&G 已在北美商业化 SAM 相位分布 | 竞争壁垒的现实上限 |

> ⚠️ **与上方路线判断的一致性检查**：上方记「AT 3.0 做不到 2 mm / 能耗更高」「北美 11 月决策、我方倾向放弃」；本追加的 SWOT 显示 **AT 2.0 分区已达 1000 ppm 且被视为机会（RPoS 可解锁成本节约）**。二者**一为单元尺寸极限、一为分区速度**，**不冲突**；但**共同提示**：AT 的**价值主张集中在分区能力与物耗效率**，而非回渗。

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · ATH 回渗升高的系统级归因：绒毛浆变成了摄入系统）

> 来源：[[Depend Rewet Update 2025-04-04（成功标准 · LUGH-GRIFFIN-ATH 进展 · Walmart NWSP 070.9 方法对比）]]（K-C 内部汇报，2025-04-04）。

1. **ATH 推高回渗已被"确认"** —— 源文用词为 **"Confirmed ActivTech Hybrid core system is increasing rewet"**，归因指向两点：**不同的包裹层（wrapsheet）**与**不同的 SAM/绒毛浆配置**。**这比上一节的"AT Hybrid 回渗归因"更进一步：从推断变为确认。**
2. **核心机理是"系统边界变了"** —— **「Fluff becomes part of the intake system in ATH system」**：**在 ATH 体系里，绒毛浆不再属于吸收部分，而属于摄入系统的一部分**。**⇒ 同一个材料在不同结构中属于不同功能域，回渗归因必须先划边界。**
3. **第二机理是"层数"** —— **「More layers = more places fluid can be trapped」**。**⇒ ATH 的结构复杂度本身就是持液点的来源，不是某个材料单方面的问题。**
4. **对策方向是"内移吸收剂"** —— **在绒毛浆中加入少量 SAM，把该层解吸（该层在 ATH 中被视为摄入层）**。**⇒ 当持液点在系统内部时，解法是把吸收能力移进去，而不是继续改面层。**
5. **诊断必须先做减法** —— **「Need products without SAM for diagnosis」**：**有 SAM 时液体位置无法定位**。**⇒ 可复用诊断设计：先拆掉最会吸水的组分，才看得见液体停在哪。**
6. **结构对照（源文示意）** —— **SAM/Fluff 体系**：Liner / Surge / Wrapsheet (Tissue) / Fluff / SAM，分为 **Intake System** 与 **Retention System**；**ATH 体系**：Liner / Surge / Wrapsheet (**SMS**) / Fluff / **SAM / SAM**。**⇒ 差异在包裹层材质（Tissue → SMS）与 SAM 的层数/位置。**
7. **与上方判断的关系** —— 上方记「AT 的价值主张集中在分区能力与物耗效率，而非回渗」；本源进一步给出**回渗侧的确认为负**。**二者一致：ATH 的收益在结构与成本侧，回渗是需要额外治理的代价。**

> ✅ 验证（2026-09-29）：本节为**追加**，**未修正上方任何既有结论**（含 AT Hybrid 回渗归因与 ROTC 分工两节）。
> 🔴 **manual_review（2026-09-29）**：来源为 **K-C 内部汇报**；含**竞品回渗均值（AD 0.19 / Depend 0.31 / Assurance 0.36 g）**与内部项目代号（GRIFFIN、LUGH、ALD GML）；**本页只记 ATH 机理与对策，不落竞品数值、不外发**。

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · ★ 机理 Supported 但对策失败：SAM 再分配与 ATH 出局）

> 来源：[[ATH SAM Relocation（2025-07-29 · 解吸能量·残液·microCT 与 SAM 再分配台架）]]（K-C 内部研究 + 台架）。

**总假设（源文原话）**：「AT hybrid core products will have **parity or higher rewet** than SAM/fluff products because **the pulp layer is part of the intake system**」。

**三条基础工具假设全部 Supported**：① **解吸能量更高**；② **残液质量更高**；③ **microCT 显示含绒毛浆的摄入系统有额外湿润**。第四条（面层湿润度无差异）为 **Likely Supported 待跟进**。

**解吸能量实测（ergs）**：

| 产品 | 样品质量 (g) | des1 解吸能量 (ergs) |
|---|---|---|
| Code 31 — **Whole Absorbent System** | 0.42 | **6.67E+04** |
| Code 32 — **Whole Absorbent System** | 0.42 | **6.52E+04** |
| Code 31 — LSE+CW，12 gsm dSB | 0.21 | 1.83E+04 |
| Code 32 — LSE+CW，20 gsm TABCW | 0.21 | 1.78E+04 |

**SAM 再分配台架（把 30% / 47% 的 SAM 搬进绒毛浆层）：**

| 指标 | Always Discreet | ATH 550g | **+30% SAM** | **+47% SAM** |
|---|---|---|---|---|
| **Closed Cradle Rewet (g)** | **0.17** | **0.34** | **0.38** | **0.40** |
| **Open Cradle 3rd Intake (s)** | **34.80** | **65.93** | **150.58** | **142.62** |

1. **对策在台架上彻底失败** —— 源文原话：「**Bench testing did not show improved rewet by relocating SAM into ActivTech hybrid fluff layer**」；回渗从 **0.34 → 0.38 / 0.40 g（更差）**。**⇒ 依据正确机理设计的对策仍然可能无效。**
2. **失败主要发生在摄入端，不是回渗端** —— **Open Cradle 第 3 次摄入由 65.93 s 恶化到 150.58 / 142.62 s（约 2.3 倍）**。**⇒ SAM 进入绒毛浆层破坏了液体的进入通道（结构/渗透性），而不是"没把水吸走"。**
3. **回渗与摄入在此处同向恶化** —— 这**打破**了"回渗↓ ⇒ 摄入↑"的常规权衡预期。**⇒ 当改动堵塞了入口，两个指标会一起变差。**
4. **源文自己列出了三个未解问题** —— 「**Is SAM relocation not doing that for some reason? Time scale? Other causes?**」**⇒ "加 SAM 就脱水"隐含了"时间足够"的假设，而台架等待时间可能不满足；时间尺度是一个被显式怀疑的变量。**
5. **项目处置：ATH 被移出 GRIFFIN 范围** —— 「**GRIFFIN has eliminated ActivTech hybrid from scope**」，但仍保留后续优先级跟进。**⇒ 机理成立、工程失败时的正确动作是降级，不是立刻终止。**
6. **结论有明确边界** —— 源文自陈：「**Alternate AT Hybrid designs might alter the conclusions in this deck.**」**⇒ 本结论只针对当前 ATH 设计，不是对 ATH 这一类芯体的判决。**
7. **与上方各节的关系** —— 上方已记"ATH 确认推高回渗""绒毛浆在 ATH 中属于摄入系统"；本节补上**三条工具的独立验证**与**一次对策失败**，**⇒ ATH 的回渗问题已被充分确证，但解法仍未找到。**

> ✅ 验证（2026-09-29）：本节为**追加**，**未修正上方任何既有结论**。
> 🔴 **manual_review（2026-09-29）**：**⚠️ 解吸能量存在未控制混淆** —— **WAS 样品 0.42 g vs LSE+CW 0.21 g（差 2 倍）**，源文未说明是否归一化，**"3.6 倍"不得直接解读为层数效应**。回渗图注的统计阈值源文写 **0.7**（疑为 0.05 识别错误）。源文含**竞品 AD 实测（0.17 g）**，**属竞品内部数据，不外发**；**人事安排仅作追溯，不页面化为联系信息**。

## 追加：摄入侧改进成果与 SAM 迁移的方向性张力（2026-09-29 追加 · 来源：BIG LEAGUE One Pager 2026-04）

> ✅ Verification（2026-09-29，source 来源 [[BIG LEAGUE - Cradle Intake Improvements Across BCC One Pager (April 2026).pptx]]）：**摄入目标下的 SAM 迁移获得商业化级成功**——Training Pants（SAM 由 ATH 层移入 fluff 层 + 宽度 80→100 mm + 胶 4.0%→3.2%）cradle intake **25s-25s-220s → 15s-15s-30s**；Youth Pants（+MACH 5）**25s-15s-40s → 15s-10s-20s**（XS 码）；Open Diapers（fluff +0.5 g + MACH 4）**15s-15s-60s+ → 10s-10s-40s**。
>
> **与上方"对策失败"节的方向性张力（不构成矛盾，需并读）**：上方台架测试以**回渗**为判据——SAM 迁移后回渗 0.34→0.38/0.40 g 恶化；本页以**摄入**为判据——同一迁移手段（配以宽度/胶量/克重协同改动）带来大幅摄入改善。⇒ **SAM 迁移是"摄入↑ / 回渗↑"的同向双刃改动**，目标函数决定取舍；两轮改动都不是单因子实验，迁移本身的净效应无法从本页拆分 `[待验证]`。设计原则四条：增加 void volume、更快锁液、SAM 更可及且更快溶胀、更充分覆盖 target zone。

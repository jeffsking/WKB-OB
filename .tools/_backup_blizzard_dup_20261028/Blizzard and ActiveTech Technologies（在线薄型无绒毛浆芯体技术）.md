---
type: source
title: "Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）"
source_type: 技术说明
source_path: RAW/ima_sync/个人知识库/WKB/Projects/Active Hygiene/blizzard_activetech_explained.md.md
original_link: ""
date_published: "[待验证]"
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "ActiveTech is the manufacturing platform and process capability for producing thin, fluffless absorbent cores online; Blizzard is the resulting core construction — a fully wrapped, 100% SAM core stabilized with adhesive（ActiveTech 是在线生产薄型无绒毛浆芯体的制造平台与工艺能力；Blizzard 是其所产出的芯体构造：全包裹、100% SAM、以胶黏剂稳定）"
  - "A Blizzard core is not merely 'a core without fluff': it replaces fluff's structural role through deliberate control of SAP distribution, adhesive bonding and wrap/facing construction（Blizzard 不是「去掉绒毛浆的芯体」，而是用 SAP 分布、胶黏与包裹构造替代绒毛浆的结构角色）"
  - "One cited configuration uses adhesive at approximately 5% of SAM weight; too little risks poor integrity, too much reduces accessible void volume and slows intake（一种配置的胶用量约为 SAM 重量的 5%；过少则整体性差，过多则减少可及空隙体积并拖慢摄入）"
  - "Measured trade-off (adult-care ROTC HBC): thickness 5.5 mm → 4.4 mm and high-pressure rewet 2.67 g → 0.40 g, while retention capacity held around 700 g; the third intake was slower（成人护理 ROTC HBC 实测权衡：厚度 5.5→4.4 mm，高压回渗 2.67→0.40 g，保液容量维持约 700 g，但第三次摄入变慢）"
  - "Measured trade-off (baby-care ROTC Slim): thickness and rewet improved as expected, but cradle intake slowed and urine leakage trended upward — so a hybrid architecture with pad channels was retained for ROTC 2.0（婴儿护理 ROTC Slim 实测：厚度与回渗如期改善，但托架式摄入变慢、漏尿趋势上升，故 ROTC 2.0 保留带导流槽的混合构型）"
  - "The value is not merely removing fluff: it is the ability to manufacture a thin, flexible, structurally robust SAP/adhesive core online; the hard part is preserving intake speed, fluid distribution and leakage protection without surrendering thinness（价值不在去绒毛浆本身，而在「在线制造薄、柔、结构稳固的 SAP/胶芯体」；难点是在不牺牲薄度下保住摄入速度、液体分布与防漏）"
pages_linked: ["[[Blizzard Core（Blizzard 芯体结构）]]", "[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]", "[[ROTC（Real Online ThinTech Core）]]", "[[芯体测试方法与验收基准（STM）]]", "[[SAP性能指标（CRC AUL GBP Vortex）]]", "[[SAP错峰膨胀]]", "[[绒毛浆（Fluff Pulp）]]", "[[分区密度设计]]", "[[ADL（导流层）]]", "[[亲水-疏水梯度设计]]"]
---

# Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）

## One-Line Positioning 一句话定位

A **technical explainer** separating three things that are routinely conflated in the fluffless-core discussion：the **process platform**（ActiveTech）、the **core construction**（Blizzard）、and the **product implementation**（ROTC）。Its purpose in this library is to supply the structural definition and the measured trade-off curve behind any "thinner core" proposal.
（本页为**技术说明**，把常被混为一谈的三件事分开：**工艺平台**（ActiveTech）、**芯体构造**（Blizzard）、**产品实现**（ROTC）。在本库中的用途是提供「更薄芯体」提案背后的结构定义与**实测权衡曲线**。）

## Summary 摘要

1. **Why move beyond a conventional SAM/fluff core**：in a conventional core, fluff pulp provides **capillary wicking and temporary void volume**, supporting rapid initial fluid intake before the SAM swells and immobilises the fluid。A Blizzard core reduces or eliminates fluff, buying a thinner / softer / more flexible pad with **stronger pad integrity**。The engineering trade-off is explicit：**SAM, adhesive, facings and wrap construction must now carry much more of the fluid-management load**。（传统芯体里绒毛浆提供毛细导液与临时空隙体积；去浆后这些负荷转移给 SAM、胶、面层与包裹构造。）
2. **Blizzard construction is a three-layer stack**：top facing / wrap → **SAM + adhesive layer** → bottom facing / wrap。SAM is the primary absorbent and fluid-locking component；adhesive immobilises the SAM and supports pad integrity（one cited configuration ≈ **5 % of SAM weight**）；a full wrap contains the absorbent layer, limits particle migration and maintains thin-core geometry。
3. **Blizzard is therefore not simply "a core without fluff."** It replaces fluff's structural role through deliberate control of **SAP distribution, adhesive bonding, and wrap/facing construction**。
4. **What ActiveTech does**：it enables **continuous, online formation** of Blizzard-type cores。In the ROTC implementation this includes an **ACF module**、SAP feeding and metering、vacuum-assisted formation and transfer、wrapping/folding、and core sealing。Critical process controls are listed as：SAP metering and distribution（volumetric feeding，can employ **two feeders**）、vacuum and web transfer（low-fluff structures are sensitive to vacuum conditions and pad formation）、D-wrap folding and containment（SAP loss or "flying" at conveyor and folding zones must be controlled）、and adhesive selection and add-on。
5. **ROTC = Real Online ThinTech Core**，the product application。Two common configurations：**ROTC Slim / Fluffless**（all- or nearly all-fluffless, for maximum thinness and flexibility）and **ROTC HBC (Hybrid Core)**（a bottom 100 % fast-SAM ROTC layer combined with a SAM/fluff top layer and pad channel，restoring capacity and fluid-handling margin while retaining much of the thin-core benefit）。
6. **Performance balance is a classic trade-off, and the source gives measured numbers**。Adult-care ROTC HBC：thickness **5.5 mm → 4.4 mm**，high-pressure rewet **2.67 g → 0.40 g**，retention capacity held around **700 g**，but **the third intake was slower**。Baby-care ROTC Slim：thickness and rewet improved as expected, but **cradle intake slowed and urine leakage trended upward** — therefore the team **retained a hybrid architecture with pad channels for ROTC 2.0**。
7. **Engineering takeaway**：the value is not merely removing fluff；it is the ability to manufacture a **thin, flexible, structurally robust SAP/adhesive core online**。The hard part is preserving **intake speed, fluid distribution and leakage protection** without surrendering the thinness advantage。
8. Credibility：**medium**。The document is a structured technical explainer citing internal sources（ROTC Operations Training、YK Absorbent Core_Global ActiveTech Forum_May 2024、ROTC HBC POV_Mar.2026），and it carries measured values with stated units — but it **cites no external literature and gives no test-method reference**, so the numbers are treated as **internal test data**。（可信度判断依据：结构化技术说明，引用三份内部资料，数值含单位但是内部测试口径、无第三方或标准方法引用，故按「中」处理。）

## Extracted Data and Conclusions 提炼的数字与结论

| Item 项目 | Value / Conclusion 数值 / 结论 | Note 备注 |
|---|---|---|
| Platform vs construction vs product 平台/构造/产品 | ActiveTech（process platform）→ Blizzard（core construction）→ ROTC（product implementation） | 三者不可混用 |
| Blizzard stack Blizzard 叠层 | Top facing / wrap → SAM + adhesive → Bottom facing / wrap | 全包裹 |
| Adhesive add-on 胶用量 | ≈ 5 % of SAM weight（one cited configuration） | 过少→整体性差；过多→空隙体积↓、摄入↓ |
| Why fluff is there at all 绒毛浆的原始作用 | capillary wicking + temporary void volume，支撑 SAM 膨胀前的快速初摄入 | 去浆须另行承担 |
| ROTC configurations 配置 | ROTC Slim / Fluffless（近乎全无浆）；ROTC HBC（底层 100 % fast-SAM + 上层 SAM/fluff + pad channel） | 混合构型保容量裕度 |
| Adult-care ROTC HBC · thickness 成人 HBC 厚度 | 5.5 mm → **4.4 mm** | 内部实测口径 |
| Adult-care ROTC HBC · high-pressure rewet 高压回渗 | **2.67 g → 0.40 g** | 显著改善 |
| Adult-care ROTC HBC · retention 保液容量 | ≈ **700 g**（基本维持） | — |
| Adult-care ROTC HBC · intake 摄入 | **第三次摄入变慢** | 代价项 |
| Baby-care ROTC Slim · outcome 婴儿 Slim 结果 | 厚度与回渗如期改善，但 **cradle intake 变慢、漏尿趋势上升** | → ROTC 2.0 保留 pad channel 混合构型 |
| ActiveTech process modules 工艺模块 | ACF module、SAP feeding & metering、vacuum-assisted formation and transfer、wrapping/folding、core sealing | — |
| SAP feeding SAP 供料 | volumetric feeding；**can employ two feeders** | 双供料器 |
| Critical process controls 关键工艺控制 | SAP metering/distribution；vacuum & web transfer；D-wrap folding & containment；adhesive selection & add-on | 四项 |
| SAP loss risk SAP 飞失 | "flying" at conveyor and folding zones must be controlled | 低浆结构对真空与成垫敏感 |
| Cited internal sources 引用的内部资料 | ROTC Operations Training；YK Absorbent Core_Global ActiveTech Forum_May 2024；ROTC HBC POV_Mar.2026 | 三份 |
| Cost / supply-chain data 成本与供应链数据 | **本页来源未提供** | `[待验证]` |

> ⚠️ **No unsourced parameters 禁止无来源参数**：上表数值均为源文所引**内部测试口径**（成人 HBC 一组、婴儿 Slim 一组），**未标注样本量、测试方法或置信区间**；本库暂无对应标准方法（见 [[芯体测试方法与验收基准（STM）]]）的交叉核验，标 `[待验证]`。**本页来源完全不涉及成本与供应商信息**，相关格一律 `[待验证]`，不得外推。

> 🔴 **manual_review（2026-09-29）**：源文提及 **ACF 模块、双供料器配置、D-wrap 折叠与密封的具体产线实现**，属我方/合作方**工艺配置**信息；依 AGENTS.md §5，**具体设备型号、产线布局与供应关系不页面化**，本页只保留用于技术判断的功能性描述。

## Key Claims（key_claims）

- **Separate platform from construction from product before arguing about fluffless cores.** ActiveTech（能力）/ Blizzard（构造）/ ROTC（产品）三者被混用是讨论失焦的主因。 —— 支撑页：[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]、[[Blizzard Core（Blizzard 芯体结构）]]、[[ROTC（Real Online ThinTech Core）]]
- **Fluff's real job is void volume for the first seconds.** 去浆真正要补的是「SAM 膨胀前的临时空隙体积」，因此混合构型（HBC + pad channel）是工程上的保底解。 —— 支撑页：[[Blizzard Core（Blizzard 芯体结构）]]、[[绒毛浆（Fluff Pulp）]]
- **The measured trade-off is favourable but not free**：厚度 −20 %、高压回渗 −85 %，代价是**第三次摄入变慢**与婴儿形态下的**漏尿趋势上升**。 —— 支撑页：[[ROTC（Real Online ThinTech Core）]]、[[芯体测试方法与验收基准（STM）]]
- **Adhesive add-on is a two-sided control**：过少损整体性、过多损空隙体积与摄入速度。 —— 支撑页：[[Blizzard Core（Blizzard 芯体结构）]]、[[SAP错峰膨胀]]

## Related Pages 关联页面

- Concepts 概念：[[Blizzard Core（Blizzard 芯体结构）]]、[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]、[[ROTC（Real Online ThinTech Core）]]、[[绒毛浆（Fluff Pulp）]]、[[SAP错峰膨胀]]、[[分区密度设计]]、[[ADL（导流层）]]、[[亲水-疏水梯度设计]]
- Test methods 测试方法：[[芯体测试方法与验收基准（STM）]]、[[SAP性能指标（CRC AUL GBP Vortex）]]
- Sibling source 同批源：[[Active Hygiene Roadmap（力致变色材料商业化路线图）]]

## Source 原文

- Local path 本地路径：`RAW/ima_sync/个人知识库/WKB/Projects/Active Hygiene/blizzard_activetech_explained.md.md`
- Original link 原文链接：（无；内部资料）
- Source's own references 源文列出的引用：ROTC Operations Training；YK Absorbent Core_Global ActiveTech Forum_May 2024；ROTC HBC POV_Mar.2026

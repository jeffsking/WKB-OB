---
type: source
title: "US5197958 Wetness Indicating Diaper"
source_type: patent
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/US_Patents_智能织物传感_拆解/US5197958_纸尿裤湿态指示_拆解.md.md
date_published: 1993
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "US 5,197,958 'WETNESS INDICATING DIAPER', inventor Wesley A. Howell (individual; NO assignee recorded — '[未找到原文]'). Appl. No. 861,475 filed Apr. 1, 1992; granted Mar. 30, 1993. 23 Claims, 3 Drawing Sheets. Certificate of Correction signed 1994-07-12 (e.g. 'internal indicators' -> 'thermal indicators')."
  - "Claim 1 core: an intermediate material that, when DRY, is insufficiently thermally conductive for normal body temperature to raise the outer surface above a threshold, but when WET is sufficiently thermally conductive to do so — plus a thermal indicator on the outer surface, the threshold chosen so the indication is generally absent when dry and present when the baby secretes waste."
  - "Claim 2: the material WICKS moisture toward the outer layer. Claims 3-6: threshold above 60/70/80/87 degrees Fahrenheit. Claim 7: indicator no longer visible below threshold (reversible). Claim 8: thermochromic ink. Claim 9: mixture of thermochromic inks, one becoming colorless above the threshold."
  - "Thermochromic ink three-component system (citing US 4,826,550, Sakura Color Corporation): (1) electron-donating colouring organic compound determining the colour, (2) electron-accepting compound (phenol) determining colour concentration, (3) a fatty acid determining the colour-change temperature. General ratio: colouring matter 1 : phenols 5 : fatty acids 50."
  - "Fatty acid transition temperatures: capric acid (C10) 31 °C; lauric (C12) 44 °C; myristic (C14) 53 °C; palmitic (C16) 63 °C; stearic (C18) 69 °C; behenic (C22) 79 °C — mixable to finely regulate the transition temperature."
  - "Ink performance: discoloring temperature freely settable in the range -30 °C to +80 °C; discoloration sensitivity 1 to 2 °C; repeatability of the colour change 'potentially tens of thousands of times'. Microencapsulation by in-situ polymerization with urea-formalin resin wall; TC slurry about 45% wt capsule particles, formulated with a water-based binder."
summary_cn: "Howell US 5,197,958：以「隔热层干湿导热差异 + 外表面热致变色油墨 + 温度阈值」实现尿布湿态指示，给出 leuco 染料／酚／脂肪酸 1:5:50 三组分体系、脂肪酸调温表与脲醛微胶囊工艺，是变色油墨项目最直接的配方级技术底稿。"
tags: ["source/patent", "Howell", "wetness indicator", "thermochromic ink", "leuco dye", "fatty acid", "microencapsulation", "thermal insulation"]
tags_zh: ["专利", "湿态指示", "热致变色油墨", "隐色染料", "脂肪酸", "微胶囊", "隔热"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[US5197958A & US5389093A Wetness Indicating Diaper (Howell)]]", "[[US20070270773A1 Thermochromic Wetness Indicator]]", "[[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]", "[[温变湿变微胶囊技术参数对比表（X-Chromic 版 · 2026-06-18）]]", "[[Hygiene Chromic Ink Supplier Landscape（卫生护理变色油墨供应商调研 · 2026-06-12）]]", "[[Diaper Structure & ADL-REL Compendium（纸尿裤结构·ADL与REL辨析）]]"]
---

# US5197958 — Wetness Indicating Diaper（湿态指示尿布 · Howell）

> Source: US patent **5,197,958**, "WETNESS INDICATING DIAPER"（OCR 拼写 "DAPER"），inventor **Wesley A. Howell, Alto Loma, Calif.**；**assignee [未找到原文]**（首页仅载发明人及地址，个人申请）. Appl. No. **861,475**, filed **Apr. 1, 1992**; **Date of Patent: Mar. 30, 1993**. Int. Cl. A61F 3/15; U.S. Cl. 604/361, 604/385.1. **23 Claims, 3 Drawing Sheets.** Cited US patents: 14. **Certificate of Correction（更正证书，1994-07-12 签署）**: "a back on"→"a back portion"; "surface"→"surfaces"; "internal indicators"→"**thermal indicators**".
>
> 拆解说明：依据 USPTO 扫描 OCR 文本，**OCR 个别字符有误**，引用处已注明；厚度分数在 OCR 中丢失，标 `[待验证]`.

## Technical Field 技术领域

**Thermal-mediation wetness indication for diapers（以温度为媒介的尿布湿态指示）** — a *reusable cloth diaper* carrying a thermochromic ink on its **outer surface**, triggered by the heat of the excreted liquid conducted through a layer whose thermal conductivity changes on wetting.

## Problem Solved 解决的问题

| Problem 问题 | Source wording 原文表述 | Note 备注 |
|---|---|---|
| Single-point indicator fails when wetting is remote or small 单点指示在远湿点/小湿量时失灵 | "The prior art diapers are particularly unadvantageous when the **original wetting location is significantly far from the indicator location and the amount of wetness is not substantial**." | 核心失效模式 |
| Single-point indicator hard to see / ugly 单点指示难观察、不美观 | "In many cases, the baby has to be **virtually undressed** to find the indicator mark, thus greatly limiting the utility of a wetness indicator. Furthermore, these single location indicators are **not aesthetically pleasing**." | 催生"全表面多点指示" |
| Electronic circuits complex + safety fear 电子方案复杂且有安全顾虑 | on US 4,356,818 (Macias): "These electronic wetness detectors are **elaborate designs which require the addition of multiple components** to the assembly and use of the diaper."; "mothers may fear **possible electrocution** of the child" | 与电子传感路线的对照 |
| Disposable indicating systems not wash-durable 一次性指示系统不耐洗涤 | "The washing process repeatedly subjects the diapers to detergents and heat, and the indicating systems of the prior art are **not able to withstand these harsh environments**." | 耐洗需求 |
| Reusability requirement 可复用需求 | "A reusable cloth diaper needs a wetness indicating system that **after drying will reindicate a dry condition and then reindicate a wet condition** when the diaper is again wet." | **可逆性（reversibility）是明确设计要求** |
| Environmental driver 环保动因 | "the disposable diapers of the prior art are not reusable and therefore not recyclable." | — |

## Core Mechanism 核心机理

**Dry/wet thermal-conductivity switch + thermal threshold indicator（干湿导热开关 + 温度阈值指示）** — the physical core of the invention:

1. **Insulating interlayer（隔热中间层）** — material between the inner (skin-facing) and outer surfaces that **at least partially thermally insulates** the outer surface from the inner surface. **When DRY its thermal conductivity is too low for normal body temperature to raise the outer surface above the threshold; when WET it becomes sufficiently conductive to do so.** （E4 of Claim 1）
2. **Wicking（导流）** — Claim 2: "said material **wicks moisture** secreted from said baby toward said outer layer"; the wicking layer "quickly brings the waste into **thermal contact** with the heat sensitive ink on the outer shell".
3. **Thermal indicator（热指示器）** — on the **outer surface**, gives a visual indication when the surface temperature exceeds the threshold.
4. **Threshold selection（阈值选取）** — "said threshold being chosen such that said visual indication will **generally not be present when a baby wearing said diaper is dry**, but will **generally be present when said baby secretes waste material** into said diaper."
5. **Method claim 23（方法三步）** — thermally insulate inner from outer → wick moisture toward the outer surface into thermal contact with the indicator → provide a visual indication above threshold.
6. **Anti-false-trigger design（防误触发）** — "the inner pad 10 of the diaper is designed to **insulate the baby's skin temperature from contacting the outer shell 5** where the heat sensitive dye is located, while still **allowing the wetness to be drawn into thermal contact with the outer shell 5**"; the inner pad is attached **only at the front and back portions**, leaving a ventilation channel that "allows the heat from the child's body to escape ... and helps prevent the heat sensitive wetness indicating ink from changing color when the diaper is not wet".

**This is the thermochromic route, not hydrochromic** — the trigger is *temperature*, and the chromic material is **thermochromic ink**（Claim 8）.

## Key Embodiments 关键实施例

### Chromic ink system 变色油墨体系（最接近变色油墨项目的部分）

Ink source: "The thermochromic ink that is used is similar to the thermochromic ink of **U.S. Pat. No. 4,826,550, assigned to Sakura Color Corporation**."

**Three-component system（三组分体系，Table 1）**: "(1) an **electron donating coloring organic compound** for determining the color, (2) an **electron accepting compound** for determining the concentration of the color, and (3) a **fatty acid** for determining the color-change temperature."

| Component 组分 | Role 作用 | General ratio 通用配比 |
|---|---|---|
| Coloring matter（显色物质 / leuco dye） | determines the colour 决定颜色 | **1** |
| Phenols（酚类 / electron accepting） | determines colour concentration 决定浓度 | **5** |
| Fatty acids（脂肪酸） | determines the colour-change temperature 决定变色温度 | **50** |

**Fatty acid transition-temperature table（脂肪酸转变温度表，Table 2）** — the temperature-tuning switch:

| Fatty acid 脂肪酸 | Carbon No. 碳数 | Transition temp 转变温度 |
|---|---|---|
| Capric acid 癸酸 | 10 | **31 °C** |
| Lauric acid 月桂酸 | 12 | **44 °C** |
| Myristic acid 肉豆蔻酸 | 14 | **53 °C** |
| Palmitic acid 棕榈酸 | 16 | **63 °C** |
| Stearic acid 硬脂酸 | 18 | **69 °C** |
| Behenic acid 山嵛酸 | 22 | **79 °C** |

> "it is possible to **minutely regulate the discoloring temperature by using two or more kinds of fatty acids mixedly**（混合两种以上脂肪酸可精细调节变色温度）."

**Colour formers and hues（显色物质与色相）**: 3,6-dimethoxyfluoran (yellow 黄); 3-cyclohexylamino-6-chlorofluoran (orange 橙); 3-diethylamin-6-methyl-7-chlorofluoran (vermilion 朱红); 3-diethylaminobenzfluoran (pink 粉); rhodamine B lactam (red 红); **crystal violet lactone（结晶紫内酯, blue 蓝）**; 3-diethylamino-7-dibenzylaminofluoran (green 绿); 3-diethylamino-6-methyl-7-anilinofluoran (black 黑); "if these compounds are mixed, their mixed colors can also be obtained".

**Microencapsulation（微胶囊化）** — required because the fatty acid is liquid and would otherwise be lost: "In-situ polymerization with **urea formalin resin** used as wall material"; the TC slurry is an aqueous dispersion containing about **"45% wt. of capsule particles"**, then formulated with a **water-based binder** into a water-based thermochromic ink. Table 3 lists chemical (interfacial/in-situ polymerization), physico-chemical (coacervation, organic-solution coacervation) and mechano-chemical (spray drying) encapsulation routes.

**Ink performance（油墨性能）**:

| Property 性能 | Value 数值 |
|---|---|
| Settable discoloring temperature 可设定变色温度范围 | **-30 °C to +80 °C** |
| Discoloration sensitivity 变色灵敏度 | **1 to 2 °C** |
| Repeatability 重复性 | "**potentially tens of thousands of times**"（可达数万次） |
| Base transition 基础变色 | colour ↔ colourless; also colour A ↔ colour B possible |
| Available colours 可选颜色 | orange, pink, red, purple, blue, green, black |

### Threshold and colour modes 阈值与配色模式

> "It has been determined that the temperature threshold is **advantageously about 60 F.**, is **desirably above 70 F.**, is **more desirably above 80 F.** and is **preferably above 87 F.**"（≈ **30.6 °C** 优选下限）

Three ink modes: ① a mixture of two thermochromic inks, one becoming **colourless above** the threshold; ② **colourless below** the threshold and **colourful above**（干燥无色、湿时有色）; ③ **colourless above** the threshold and therefore **colourful below**（湿时无色、干燥有色）.

### Structure 结构实施例

| Layer 层 | Material 材料 | Note 备注 |
|---|---|---|
| Outer shell 外壳 5 | non-absorbent durable soft fabric; preferred "Dupont style #22-2 material which is **97% Dacron and 6% Lycra**" | 源文注明 OCR 数字存疑，可能实为 97% Dacron + 3% Lycra |
| Protective covering 贴肤层 55 | "a layer of **BIRDSEYE 100% cotton**" | forms the inner surface |
| Sorbent layer 吸收层 50 | "**looped terry 100% cotton** having a thickness of at least [fraction lost in OCR]" | 源文推演约 1/4 英寸 → `[待验证]` |
| Wicking layer 导流层 60 | "DuPont style #1178B" material（OCR 拼写存疑） | wicks moisture from the buttocks to the sorbent layer and into thermal contact with the ink |
| Fastening 搭扣 | VELCRO tabs; wash inside-out to protect the hook side | — |

Reversibility claim（可逆性，Claim 7）: "wherein said thermal indicator is **no longer visible when said outer shell has a temperature which falls below said threshold**." Claims 19–22: indicators form a **repeating pattern**; visible above threshold / not visible above threshold; and **one colour above threshold, another colour below**.

Patterned printing rationale: "by screening the thermochromic inks onto the garment in a **repeated pattern, such as a cartoon type design**, it allows the color change to be limited to a controlled area" — avoids the unaesthetic full-sheet blotch of prior art.

Figures: FIG.1 bottom plan view (outer surface); FIG.2 top plan view; FIG.3 cross-sectional view showing outer shell 5 and inner pad 10 (sorbent 50 / protective covering 55 / wicking 60) plus VELCRO tabs. Application method: **silk screening（丝网印刷）**.

## Claims Coverage 权利要求覆盖范围

| Claim | Scope 范围 |
|---|---|
| **Claim 1**（product, core） | A diaper for indicating wetness: inner surface (against baby's skin) + outer surface (exterior) + **intermediate material with the dry/wet thermal-conductivity differential that at least partially thermally insulates** + **a thermal indicator on the outer surface** + **threshold chosen so indication is generally absent when dry, present when waste is secreted**. Functional, mechanism-level claim. |
| **Claims 2–9** | 2 wicking; 3–6 threshold **>60 / >70 / >80 / >87 °F**; 7 reversible (not visible below threshold); 8 indicator = **thermochromic ink**; 9 mixture of thermochromic inks, one colourless above threshold. |
| **Claim 10** | Outer shell + "an inner pad attached to said outer shell **solely at said front portion and said back portion**" + outer-surface thermal indicator + threshold selection. |
| **Claims 11–13** | inner pad includes a sorbent layer; protective cover forms the inner surface; cover **surrounds** the sorbent layer separating it from the outer shell. |
| **Claim 14–16** | Three-layer inner pad: "a sorbent layer; a protective cover defining an inner surface; and, a layer of **wicking material** between said protective cover and said sorbent layer"; 16 inner pad minimum thickness (fraction lost in OCR → `[待验证]`). |
| **Claim 17**（simplified product） | inner + outer surface + "a layer positioned between said inner and outer surfaces providing **at least some thermal insulation capacity when dry and a lower thermal insulation capacity when wet**" + thermal indicator on the outer surface. |
| **Claim 18**（reusable cloth diaper） | "a **cloth sufficiently durable to withstand multiple washings**" + front portion / back portion with laterally extending tabs / connecting portion + fasteners + "**a plurality of discrete thermal indicators distributed over substantially the entire outer surface**". |
| **Claim 23**（method） | Thermally insulate inner from outer → **wick** moisture toward the outer surface into thermal contact with the indicator → visual indication above threshold. |

Boundary notes recorded from the source: the claims are limited to a **diaper**（not pads/bandages）; they require a **thermal indicator + temperature threshold**, so non-thermal mechanisms fall outside; Claim 18 additionally requires **wash-durable cloth**.

## Hygiene Implication 卫材关联

**The single most useful source in this batch for the chromic-ink programme** — it is the only one with formulation-level detail.

1. **Direct formulation starting point（配方级起点）.** The **leuco dye : phenol : fatty acid = 1 : 5 : 50** three-component system, with the **fatty acid as the colour-change temperature switch**, is a concrete, quotable specification to take to chromic-ink suppliers. Cross-check against [[温变湿变微胶囊技术参数对比表（X-Chromic 版 · 2026-06-18）]] and [[Hygiene Chromic Ink Supplier Landscape（卫生护理变色油墨供应商调研 · 2026-06-12）]] — the question to put to suppliers is whether their TC slurry matches the **~45% wt capsule / urea-formalin wall / water-based binder** architecture described here.
2. **Temperature down-tuning（变色点下调）.** The owner's body-temperature target is **35–40 °C**. The disclosed fatty-acid table brackets that range with **lauric acid 44 °C (C12)** and **capric acid 31 °C (C10)**; mixing two or more fatty acids is explicitly taught for fine regulation. Combined with the stated **-30 °C to +80 °C** settable range and **1–2 °C** sensitivity, a narrow 35–40 °C window is a design target that can be specified numerically to a supplier. Compare with the 95–104 °F window claimed in [[US20070270773A1 Thermochromic Wetness Indicator]].
3. **Thermochromic vs hydrochromic decision（热变 vs 湿变路线决策）.** This patent's whole logic depends on **dry/wet thermal-conductivity differential + anti-false-trigger insulation** — i.e. the engineering burden is entirely about stopping *body heat* from firing the indicator. That burden disappears on a **hydrochromic / water-activated** route. This is the central trade-off to evaluate in [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]].
4. **Integration into the layer stack（集成到层结构）.** The disclosed stack — skin-side cover → sorbent → **wicking layer** → outer shell carrying the ink — maps onto a modern diaper as topsheet → core → **ADL/REL** → backsheet-with-printed-chromic. The "wicking into thermal contact" function is exactly what an **ADL/REL** would provide; use [[Diaper Structure & ADL-REL Compendium（纸尿裤结构·ADL与REL辨析）]] when judging whether the existing ADL/REL can serve as the thermal bridge, and whether a bulky core can double as the insulating interlayer.
5. **Reversibility（可逆性）is claimed, and quantified.** Claim 7 requires the indicator to become invisible again below the threshold, and the ink is stated to be repeatable "**potentially tens of thousands of times**" and wash/heat durable. Note the context is a **reusable, washable cloth diaper** — durability against detergents and heat is a requirement there that a single-use product does not share, so treat the wash-durability data as **out-of-context for disposable** rather than as a validated disposable spec.
6. **Multi-point, full-surface, patterned printing.** Claim 18's "**plurality of discrete thermal indicators distributed over substantially the entire outer surface**" plus the repeating cartoon-pattern teaching directly addresses the "must undress the baby to find the mark" pain point — a product-design rationale that still holds, and a caution that a full-sheet colour change looks like a blotch.
7. **Safety/regulatory: NOT addressed by this source.** The document discloses **no migration, skin-contact, sensitisation or toxicology data**. Any skin-contact or indirect-contact chromic layer must be qualified by supplier dossiers and internal testing; this patent supplies none of that evidence.
8. **Freedom-to-operate（自由实施）: NOT assessed — no conclusion is drawn.** Facts recorded from the source only: filed 1992-04-01, granted 1993-03-30, individual inventor with **no assignee recorded**. The source's §8 contains **推算（推演）** expiry estimates and design-around commentary; **that analysis is deliberately not reproduced or adopted here**. Expiry, maintenance, continuation/foreign-family status are **not established by this document** and are flagged `[待验证]` / manual review — route to IP counsel.

## Related Sources 关联来源

- [[US5197958A & US5389093A Wetness Indicating Diaper (Howell)]] — Howell 两案的既有合并摘要页
- [[US20070270773A1 Thermochromic Wetness Indicator]] — 后案（品类扩展至失禁裤/卫生巾/绷带），直接引证本案
- [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] — 本库热变/湿变路线可行性评审（主线）
- [[温变湿变微胶囊技术参数对比表（X-Chromic 版 · 2026-06-18）]] — 微胶囊参数对比，核对 45% wt 胶囊/脲醛壁材口径
- [[Hygiene Chromic Ink Supplier Landscape（卫生护理变色油墨供应商调研 · 2026-06-12）]] — 变色油墨供应商能力
- [[Diaper Structure & ADL-REL Compendium（纸尿裤结构·ADL与REL辨析）]] — ADL/REL 与芯体结构，用于判断导热桥与隔热层可行性

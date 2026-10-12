---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_4a410e750a5846dd3a0a7269d236d2cb001a693ee6c0644e"
source_file: "Gravure_Roll_101_ch1_Fundamentals_拆解报告.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch1_Fundamentals_拆解报告.md.md"
extracted: "2026-09-30"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
---

# Gravure_Roll_101_ch1_Fundamentals_拆解报告.md


章节：Ch1 Fundamentals ｜ 覆盖幻灯片：1–9 ｜ 文档：Gravure Roll 101 (KC, Capability Days 2025) ｜ 拆解日期：2026-08-30

# Gravure Roll 101 — Ch1 Fundamentals：学术级章节拆解报告

Source integrity rules applied in this report（本报告引用的证据标注规则）
- Every claim is tagged with its evidence: SLIDE N（slide text layer）, SLIDE N — SPEAKER NOTES（presenter notes）, or SLIDE N — 图像内容补充（data extracted from rendered slide images; treated as a reliable source per task specification）.
- Where the chapter contains no supporting statement, the tag [未找到原句] is used and no data is invented.
- Where a number or a relation is counted / derived by this report, the tag [本报告推导] is used, with the counting or arithmetic basis shown.
- Where content comes from another chapter of the same deck, it is tagged with its own slide number and explicitly marked 跨章引用 — it is never presented as Ch1 content.
- Where content comes from outside the four chapter files, it is tagged 外部背景，非本章内容.

⚠️ Chapter data-density warning（本章数据密度声明）：Ch1 is a qualitative, concept-defining chapter. It contains no coating weights, no line speeds, no viscosities, no cell volumes, no costs, and no tolerances. Every quantitative field asked for in this report that Ch1 does not supply is answered with [未找到原句] rather than filled with plausible numbers. Where quantification is required, it is imported from Ch2/Ch3/Ch4 and labelled as cross-chapter.

## 模块 1：核心论点（Core Arguments）

### A1. A gravure roll is defined by function, not by hardware — the product being sold is a metered quantity of fluid, not a cylinder



English thesis：The chapter's one-sentence definition of a gravure roll is entirely functional: "Engraved roll that delivers a precise amount of fluid to a substrate" (SLIDE 2). The two operative words are precise and amount. The roll is therefore specified downstream from the dose, never upstream from the geometry — geometry is only the means of holding the dose.

- SLIDE 2："Engraved roll that delivers a precise amount of fluid to a substrate"
- 支撑依据（递进证据链）：



- SLIDE 2 — 图像内容补充：the three images on the page walk a single zoom-in path — 凹版辊实物（带轴头）→ 微观表面（蜂窝/棱锥网穴）→ 网穴特写（可见网穴内残留液体）. The endpoint of the zoom is liquid retained inside a cell, i.e. the chapter visually defines the roll by what it carries.
- SLIDE 5：the coating process is defined as producing "Consistent coating weights" — the roll's function is re-stated at the process level as a weight-control capability, not a pattern-transfer capability.
- Cross-check：Ch2 SLIDE 18 defines volume as "Total volume of all the engraved cells on the roll surface per unit area of the surface" — i.e. the entire Ch2 specification apparatus (BCM, LPI, cell geometry) is the quantification of the single word "precise" on SLIDE 2. Ch1 states the requirement; Ch2 supplies the metrology. 跨章引用
### A2. "Gravure roll" and "anilox roll" are functionally the same object; the distinction is a convention — and this chapter does not itself obey that convention



English thesis：The presenter states the two terms are "pretty much the same thing" and that the difference is only an industry connotation（gravure = direct + patterned；anilox = indirect + simple engraving）(SLIDE 2 — SPEAKER NOTES). This is a naming convention, not a technical classification — and the chapter's own drawings contradict it.

- SLIDE 2 — SPEAKER NOTES："Gravure roll and anilox roll – pretty much the same thing. Gravure roll has an industry connotation of direct to substrate and patterned. Anilox roll is more indirect and common/simple engraving"
- 支撑依据（章内自相矛盾的实证，共 3 处）：
| # | Location | How it violates the SLIDE 2 connotation rule | Evidence |
|---|---|---|---|
| 1 | ELC indirect stack | The connotation says indirect pairs with anilox, yet the indirect ELC winder's roll is labelled "Gravure Roll" | SLIDE 7 text layer + SLIDE 7 — 图像内容补充 |
| 2 | Facial indirect line | Same violation in caps: "GRAVURE ROLL" inside a "Facial OLP = Indirect Gravure Coating" diagram | SLIDE 8 + SLIDE 8 — 图像内容补充 |
| 3 | Doctor blade chamber | The chamber detail drawing labels the same functional position "Anilox Roll" | SLIDE 9 — 图像内容补充 |
- ⚠️ 这是本拆解最重要的发现之一：the deck uses "Gravure Roll" in the two indirect process diagrams (SLIDE 7, SLIDE 8) and "Anilox Roll" in the component diagram (SLIDE 9) — while SLIDE 2 — SPEAKER NOTES claims anilox is the indirect term. The terminology is unstable inside a 9-slide chapter. See C1 / C2 in 模块 2 and the T5 evidence table in 模块 3.
### A3. KC's business justification for gravure is premiumization, not cost reduction — the roll is positioned as a margin instrument



English thesis：SLIDE 4 gives four value statements and four premium SKUs. Every one of the four statements is a value-capture statement（Premium products / differentiation / consumer value and growth / Higher margins）。None is a cost statement. Gravure is justified to KC as a revenue-and-margin technology.

- SLIDE 4："Enhanced properties create Premium products / Enable product differentiation / Create consumer value and drive growth / Higher margins"
- SLIDE 4 — 图像内容补充：the four statements are each illustrated by a specific commercial SKU：Cottonelle Luxe／Kleenex soothing lotion（8 盒装 / 960 抽）／Viva Signature Cloth／Scott Shop Original
- 支撑依据（叙事结构）：SLIDE 3 is an image-only slide captioned "Ordinary to Extraordinary"，showing 普通冰淇淋圣代 → 辊体加工/镀层工业照 → 精致巧克力圣代（SLIDE 3 — 图像内容补充）。The chapter therefore places a transformation metaphor between the technical definition (SLIDE 2) and the business case (SLIDE 4)：the roll is the agent that converts a commodity substrate into a premium product. The argument structure is：definition → transformation → premiumization.
- 反向印证（跨章）：Ch2 SLIDE 20 closes the loop — *"Not just printing/coating …. Creating product properties"*。Ch1's "Enhanced properties" and Ch2's "Creating product properties" are the same proposition stated at two levels. 跨章引用
### A4. The entire chapter is organised around one binary — Direct vs Indirect — and that binary is used to partition KC's whole asset portfolio



English thesis：SLIDE 5 introduces exactly two forms of gravure coating and immediately maps each onto named KC assets：Direct → DRC and OLU；Indirect → Facial and Embossing winders. The next three slides (SLIDE 6, 7, 8) are then simply the worked examples of that binary — one Direct asset group, two Indirect asset groups. The chapter has no third category.

- SLIDE 5："Main Forms of Gravure Coating / Direct = gravure roll to substrate …… DRC and OLU / Indirect = gravure roll to applicator roll to substrate…. Facial and  Embossing winders"
- SLIDE 6："OLU/DRC - Direct Gravure Coating"
- SLIDE 7："2 Ply Winder ELC = Indirect Gravure Coating"
- SLIDE 8："Facial OLP = Indirect Gravure Coating"
- 支撑依据（资产覆盖度清点） [本报告推导]：KC line codes appearing in Ch1 = OLU, DRC, ELC, Facial（4 个），plus the generic class Embossing winders。The binary therefore accounts for every asset named in the chapter — the taxonomy is exhaustive by construction, with zero residual/uncategorised cases. This exhaustiveness is why the Direct/Indirect axis is the correct primary key for the rest of the deck.
- ⚠️ 重要的非对称警告：the binary is not symmetric with the engraving-platform binary of Ch2. Ch2 assigns Facial → Chrome, OLU/DRC/ELCs → Ceramic。Since ELC is Indirect (SLIDE 7) yet sits in the Ceramic group, "Indirect" does not imply "Chrome"。The two binaries are crossed, not nested — developed in 模块 4.
### A5. A gravure roll never works alone — it is always one element of a roll stack plus a doctor blade chamber



English thesis：In all three process diagrams of the chapter, the gravure roll appears embedded in a multi-roll arrangement and always coupled to a doctor blade chamber. The roll is presented as a system component, never as a standalone part. SLIDE 2's "Heart" metaphor is therefore literal: a heart is only meaningful inside a circulatory system.

- SLIDE 2："Considered the 'Heart' of printing/coating process"
- 支撑依据（三张图的构件清点）：
| Diagram | Rolls / stations shown | Doctor blade chamber present? | Evidence |
|---|---|---|---|
| Direct（OLU/DRC） | Backing Roll（上, 绿）+ Gravure Roll（下, 蓝）+ Doctor Blade Chamber（左下） | 是 | SLIDE 6 — 图像内容补充 |
| Indirect（ELC 2-ply winder） | 8 stations top-to-bottom, of which 7 are rolls + 1 cleaning system | 是（attached at the Gravure Roll） | SLIDE 7 — 图像内容补充 |
| Indirect（Facial OLP） | DOCTOR CHAMBER → GRAVURE ROLL → RUBBER ROLL → WEB（4 段） | 是（first element in the chain） | SLIDE 8 — 图像内容补充 |
- 附加依据（腔体内部结构）：SLIDE 9 — 图像内容补充 labels three components inside the chamber — Metering Blade（计量刮刀）／Anilox Roll／Containment Blade（密封刮刀）。The chamber is itself a 3-part sub-assembly, i.e. the "system" claim holds at the second level of decomposition as well.
- 失效链条（跨章闭合）：Ch2 SLIDE 14 states "Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear" — i.e. cell geometry → blade wear is a documented causal chain。Ch1's chamber is where that cost is actually incurred. 跨章引用
## 模块 2：关键概念操作化定义（Key Concepts with Operational Definitions）



Count note：the task's mandatory coverage list resolves to 14 entries when the four line codes are counted as one concept. Coverage of the mandatory list takes precedence over the suggested 8–12 range, so this module delivers 14 concepts（C1–C14）。Every (d) item is a verbatim English extract with its slide tag; every missing quantity is marked [未找到原句]。

### C1. Gravure Roll ｜ 凹版辊

(a) 中文名 + English term：凹版辊 / Gravure Roll

(b) English definition
> An engraved roll that delivers a precise amount of fluid to a substrate. It is "Considered the 'Heart' of printing/coating process". Per the presenter, it carries an industry connotation of being used direct-to-substrate and patterned (SLIDE 2 — SPEAKER NOTES).

(c) 操作化定义（Operational definition）
- 判定维度（4 项，全部来自 SLIDE 2）：① the surface is engraved（i.e. it carries cells; a smooth roll is excluded）; ② its function is delivery of fluid（not embossing, not calendering, not conveying）; ③ the delivered quantity is precise / metered（not a flooded or unmetered application）; ④ there is a receiving substrate.
- 量化指标：Ch1 supplies none. No cell volume, no LPI, no cell depth, no tolerance appears anywhere in slides 1–9 → [未找到原句]（quantification is deferred entirely to Ch2: BCM, LPI, cell geometry, 跨章引用 Ch2 SLIDE 16/18）。
- 物理识别式（来自图像） [本报告推导]：a roll can be visually confirmed as a gravure roll by the presence of a periodic cell pattern on its surface（SLIDE 2 — 图像内容补充：微观表面呈蜂窝/棱锥网穴），and by visible liquid residue retained inside the cells in the extreme close-up.
- 术语边界：the term is conventional, not technical — see C2 and the ambiguity discussion below.

(d) 原文英文摘录
> "Engraved roll that delivers a precise amount of fluid to a substrate" — SLIDE 2
> "Considered the 'Heart' of printing/coating process" — SLIDE 2
> "Gravure roll has an industry connotation of direct to substrate and patterned." — SLIDE 2 — SPEAKER NOTES

### C2. Anilox Roll ｜ 网纹辊（柔印/涂布网纹辊）

(a) 中文名 + English term：网纹辊 / Anilox Roll

(b) English definition
> Per the presenter, functionally the same object as a gravure roll, differing only by industry connotation: "Anilox roll is more indirect and common/simple engraving" (SLIDE 2 — SPEAKER NOTES). In this deck the term is used only once, in the doctor-blade-chamber component drawing (SLIDE 9 — 图像内容补充).

(c) 操作化定义
- 判定维度（按 SLIDE 2 notes 的约定）：① used indirectly（fluid is handed off to an intermediate roll before the substrate）; ② engraving is common / simple（i.e. a standard catalogue engraving rather than a bespoke engineered pattern）。
- ⚠️ 操作性警示（本概念的关键结论）：neither dimension is usable as a reliable discriminator in this deck。See the ambiguity discussion below — the deck violates its own rule 3 times。
- 量化指标：[未找到原句] —— Ch1 gives no engraving parameter, volume value, or line-screen value attached to the word "anilox"。
- 唯一出现位置：SLIDE 9 — 图像内容补充（Doctor Blade Chamber 部件标注：Metering Blade / Anilox Roll / Containment Blade）。

(d) 原文英文摘录
> "Gravure roll and anilox roll – pretty much the same thing. … Anilox roll is more indirect and common/simple engraving" — SLIDE 2 — SPEAKER NOTES
> "Doctor Blade Chamber 部件标注：Metering Blade（计量刮刀）、Anilox Roll、Containment Blade（密封刮刀）" — SLIDE 9 — 图像内容补充

### 🔴 C1/C2 必含讨论：Gravure vs Anilox 区分的模糊性（The Ambiguity of the Gravure/Anilox Distinction）



The task requires this discussion. It is the single most consequential finding of Ch1, because terminology instability is a direct commercial risk in specification, sourcing and contracting.

1. What the presenter actually claims（原文主张）
> "Gravure roll and anilox roll – pretty much the same thing. Gravure roll has an industry connotation of direct to substrate and patterned. Anilox roll is more indirect and common/simple engraving" — SLIDE 2 — SPEAKER NOTES

Note the hedging architecture of the sentence: "pretty much", "industry connotation", "more". All three are vague quantifiers. The presenter is explicitly signalling that this is social usage, not engineering definition — there is no threshold, no test, and no measurable boundary offered.

2. The chapter contradicts its own rule — 3 documented violations

||||||
|---|---|---|---|---|
|V1|Gravure ⇢ direct|SLIDE 7：*"2 Ply Winder ELC = Indirect Gravure Coating"*，and the roll in that indirect stack is labelled "Gravure Roll"|Gravure + Indirect = contradiction|SLIDE 7 + SLIDE 7 — 图像内容补充|
|V2|Anilox ⇢ indirect|SLIDE 8：*"Facial OLP = Indirect Gravure Coating"*；diagram reads DOCTOR CHAMBER → GRAVURE ROLL → RUBBER ROLL → WEB|Indirect + Gravure, again；anilox is not used where the rule predicts|SLIDE 8 + SLIDE 8 — 图像内容补充|
|V3|Gravure ⇢ patterned / Anilox ⇢ simple|SLIDE 9 chamber drawing labels the roll "Anilox Roll"，yet this is the same component class serving the patterned KC assets|Term swap on identical hardware|SLIDE 9 — 图像内容补充|


3. The contradiction extends into Ch2（跨章，进一步放大模糊性） 跨章引用

||||
|---|---|---|
|Same assets, two names|Ch2 SLIDE 11："Laser Engraved Ceramic Rolls (OLU/DRC/ELCs)" vs. Ch2 SLIDE 13 title：*"Standard Ceramic Anilox Roll Engravings"*|OLU/DRC/ELC rolls are called both "ceramic rolls" and "anilox rolls"|
|"Simple engraving" is false for KC|Ch2 SLIDE 20："Outside the engravers comfort zones / 'Deep' engravings / 'Large' cells"|KC's engravings are explicitly not "common/simple" — so calling them "anilox" by the SLIDE 2 rule is wrong, yet Ch2 SLIDE 13 does exactly that|
|KC had an open, unresolved internal debate|Ch2 SLIDE 13 — SPEAKER NOTES：*"Anilox vs Gravure and Apex Owner Discussion this week"*|KC had not settled this terminology at the time of writing — it was a live agenda item|


4. Conclusion（可操作结论） [本报告推导]
- The distinction has zero discriminating power in this deck. Positionally, "gravure roll" and "anilox roll" denote the same component in the same location（the engraved roll served by the doctor blade chamber）。
- Therefore：specifications, RFQs, contracts and spare-part orders must never rely on the noun. They must be written on the measurable parameters alone（cell geometry + line screen + volume, per Ch2 SLIDE 16; plus cell diameter / depth / volume and pattern details, per Ch2 SLIDE 21）。The noun is cosmetic; the numbers are binding.
- Practical rule for documentation [本报告推导]：in any internal or supplier document, write the term once as "gravure/anilox roll (engraved metering roll)" and thereafter use only the asset + parameter identifier（e.g. OLU VIVA GR#5 — 27 dpi dot, 2:1 spacing, 27.6 BCM, per Ch3 SLIDE 28 — 图像内容补充）。

### C3. Gravure Coating ｜ 凹版涂布

(a) 中文名 + English term：凹版涂布 / Gravure Coating

(b) English definition
> *"Process that uses a gravure roll to apply a thin, uniform liquid film to a moving substrate"*，characterised by "Consistent coating weights" and being "Suitable for high-speed processes" (SLIDE 5).

(c) 操作化定义
- 判定维度（3 项，全部来自 SLIDE 5）：① the applicator is a gravure roll；② the deposited film is thin and uniform；③ the substrate is moving（i.e. continuous web, not sheet-fed）。
- 性能判据（2 项，章节自述）：Consistent coating weights（weight uniformity, across-web and along-web）＋ suitable for high-speed processes。
- 量化指标：Ch1 supplies none. No film thickness value, no coat weight value（g/m²）, no speed value（m/min or fpm）, no viscosity value, and no uniformity tolerance（±%）→ 全部 [未找到原句]。
- ⚠️ 不可外推警告："thin" 与 "high-speed" 在本章均无量纲、无数值、无参照系。Any attempt to state "gravure coats ≤ X µm at ≥ Y m/min" is fabrication and is not supported by this chapter.
- 跨章可得的量化入口 跨章引用：Ch2 SLIDE 18 gives the volume→thickness conversion basis（1 BCM/in² = 1.55 cm³/m²；hence 1 BCM ⇒ 1.55 µm equivalent average wet film thickness, [本报告推导] from Ch2 SLIDE 18）；Ch3 SLIDE 28 gives a real KC volume target（27.6 BCM）。

(d) 原文英文摘录
> "Process that uses a gravure roll to apply a thin, uniform liquid film to a moving substrate / Consistent coating weights / Suitable for high-speed processes" — SLIDE 5

### C4. Direct Gravure Coating ｜ 直接凹版涂布

(a) 中文名 + English term：直接凹版涂布 / Direct Gravure Coating

(b) English definition
> The form of gravure coating in which the fluid path is "gravure roll to substrate" — i.e. no intermediate transfer roll. KC assigns this form to the DRC and OLU assets (SLIDE 5), and devotes SLIDE 6 to it as a standalone diagram.

(c) 操作化定义
- 判定式（路径判据，决定性）：fluid path length = 1 hop。Gravure Roll → Substrate。If an applicator roll appears in the path, the process is by definition NOT direct（SLIDE 5）。
- 构型判据（来自 SLIDE 6 — 图像内容补充）：① Backing Roll on top（green）；② Gravure Roll below（blue）；③ Doctor Blade Chamber at lower-left；④ the web passes horizontally through the nip；⑤ the Gravure Roll rotates clockwise。
- 资产判据：DRC and OLU (SLIDE 5, SLIDE 6)。
- 量化指标：[未找到原句] —— no nip load, no wrap angle, no speed, no coat weight is given for the direct configuration in Ch1.
- 工程含义 [本报告推导]：because the gravure roll contacts the substrate directly, the nip is a coating nip — the substrate is pressed against the engraved surface. This is the structural reason the direct route is sensitive to substrate strength（developed as a selection criterion in 模块 5, 连接点 2）。Note: Ch1 states the geometry but does not state this consequence → the consequence is [本报告推导], the geometry is SLIDE 6 — 图像内容补充。

(d) 原文英文摘录
> "Direct = gravure roll to substrate …… DRC and OLU" — SLIDE 5
> "OLU/DRC - Direct Gravure Coating" — SLIDE 6
> "Direct Gravure Coating 示意：上 Backing Roll（绿）／下 Gravure Roll（蓝），左下 Doctor Blade Chamber；基材水平穿过两辊 nip；Gravure Roll 顺时针旋转" — SLIDE 6 — 图像内容补充

### C5. Indirect Gravure Coating ｜ 间接凹版涂布

(a) 中文名 + English term：间接凹版涂布 / Indirect Gravure Coating

(b) English definition
> The form of gravure coating in which the fluid path is "gravure roll to applicator roll to substrate" — i.e. one intermediate transfer roll is inserted. KC assigns this form to the Facial and Embossing winders assets (SLIDE 5), illustrated by two distinct configurations: the 2 Ply Winder ELC (SLIDE 7) and the Facial OLP (SLIDE 8).

(c) 操作化定义
- 判定式（路径判据，决定性）：fluid path length = 2 hops。Gravure Roll → Applicator Roll → Substrate。
- 构型判据 A（ELC，SLIDE 7 — 图像内容补充）：an 8-station vertical stack, top-to-bottom = Upper Rubber Roll → Embossing Cleaning System → Embossing Roll → Marrying Roll → Applicator Roll → Gravure Roll（highlighted yellow, coupled to the Doctor Blade Chamber）→ Steel Calendar Roll → Rubber Calendar Roll。
- 构型判据 B（Facial OLP，SLIDE 8 — 图像内容补充）：a 4-element chain = DOCTOR CHAMBER → GRAVURE ROLL → RUBBER ROLL → WEB。
- 资产判据：Facial（SLIDE 5, SLIDE 8）／Embossing winders（SLIDE 5）／2 Ply Winder ELC（SLIDE 7）。
- 量化指标：[未找到原句] —— no speed, no coat weight, no nip load, no transfer ratio is given for either indirect configuration in Ch1.
- ⚠️ 关键结构观察 [本报告推导]：the two indirect diagrams do not have the same roll count（8 stations for ELC vs 4 elements for Facial OLP）。Therefore "indirect" describes the fluid path only — it does not describe a fixed machine layout. Do not use "indirect" as a shorthand for a specific roll stack.

(d) 原文英文摘录
> "Indirect = gravure roll to applicator roll to substrate…. Facial and  Embossing winders" — SLIDE 5
> "2 Ply Winder ELC = Indirect Gravure Coating" — SLIDE 7
> "Facial OLP = Indirect Gravure Coating" — SLIDE 8

### C6. Backing Roll ｜ 背压辊（支撑辊）

(a) 中文名 + English term：背压辊 / Backing Roll

(b) English definition
> In the Direct gravure coating configuration, the upper roll（shown green）that forms the nip against the Gravure Roll（shown blue）, with the web passing horizontally between them (SLIDE 6 — 图像内容补充)。The chapter gives no written definition — this concept exists only in the diagram.

(c) 操作化定义
- 判定式（位置判据）：in the direct diagram, the roll positioned above the gravure roll and in contact with it across the web = the Backing Roll。
- 结构判据：the nip (web passage point) is located between Backing Roll and Gravure Roll（SLIDE 6 — 图像内容补充）。
- 功能判据 [本报告推导]：its function is to press the substrate into contact with the engraved roll（backing / pressure), enabling transfer. ⚠️ Ch1 does not state this function → [未找到原句] for any written functional description.
- 量化指标：[未找到原句] —— no diameter, no covering material/hardness, no nip pressure, no wrap angle.
- ⚠️ 跨章命名提示：the pressure/backing roll concept appears under different names in different chapters — Ch3 SLIDE 26 — 图像内容补充 labels the OLU line's equivalent "Printer Backing Roll", and lists a separate "Pressure Roll". Ch1 shows only "Backing Roll". Therefore the naming is not standardised across the deck → [本报告推导], and a spare-part specification must identify this roll by asset + position, not by name.

(d) 原文英文摘录
> *"Direct Gravure Coating 示意：上 Backing Roll（绿）／下 Gravure Roll（蓝），左下 Doctor Blade Chamber；基材水平穿过两辊 nip；Gravure Roll 顺时针旋转"* — SLIDE 6 — 图像内容补充
> ⚠️ SLIDE 6 text layer contains only the title "OLU/DRC - Direct Gravure Coating"; the roll names exist only in the rendered image.

### C7. Doctor Blade Chamber ｜ 刮刀腔（封闭式刮刀腔）

(a) 中文名 + English term：刮刀腔 / Doctor Blade Chamber（in the Facial OLP diagram, written in caps as DOCTOR CHAMBER）

(b) English definition
> A 3-component sub-assembly attached to the engraved roll, comprising the Metering Blade（计量刮刀）, the Anilox / Gravure Roll it acts upon, and the Containment Blade（密封刮刀）(SLIDE 9 — 图像内容补充)。It appears in all three process diagrams of the chapter and is therefore a mandatory, non-optional element of every gravure coating configuration shown.

(c) 操作化定义
- 存在性判据（最强判据）：every gravure configuration in Ch1 includes a doctor blade chamber. Direct: attached at lower-left of the gravure roll（SLIDE 6 — 图像内容补充）。ELC: attached at the Gravure Roll（highlighted yellow）（SLIDE 7 — 图像内容补充）。Facial OLP: the first element of the chain, feeding the gravure roll（SLIDE 8 — 图像内容补充）。→ If there is no chamber, it is not a gravure station as KC defines it.
- 组成判据：3 parts（Metering Blade / roll / Containment Blade）（SLIDE 9 — 图像内容补充）。
- 量化指标：[未找到原句] —— no blade angle, no blade thickness, no blade pressure/loading, no chamber pressure, no blade material, no change interval, no wear rate. Ch1 is entirely silent on every quantitative aspect of the chamber.
- ⚠️ 唯一可得的量化关联（跨章） 跨章引用：Ch2 SLIDE 14 — *"Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear"*。This is the only place in the deck that links a cell-geometry condition to a blade-life consequence. It establishes that blade wear is a function of roll surface finish, not merely of blade setup — which is why chamber consumables and roll re-polishing must be procured/managed as one coupled system（developed in 模块 5, 连接点 3）。

(d) 原文英文摘录
> "Doctor Blade Chamber" — SLIDE 7（text layer, listed as a component of the ELC stack）
> *"Doctor Blade Chamber 部件标注：Metering Blade（计量刮刀）、Anilox Roll、Containment Blade（密封刮刀）"* — SLIDE 9 — 图像内容补充
> *"Facial OLP 示意为 DOCTOR CHAMBER → GRAVURE ROLL → RUBBER ROLL → WEB"* — SLIDE 8 — 图像内容补充

### C8. Metering Blade ｜ 计量刮刀

(a) 中文名 + English term：计量刮刀 / Metering Blade

(b) English definition
> One of the two blades inside the Doctor Blade Chamber, named in the SLIDE 9 component drawing. The chapter provides no written definition of its function — the name is the only information given.

(c) 操作化定义
- 判定式（位置/命名判据）：the chamber blade identified in the drawing as "Metering Blade"（SLIDE 9 — 图像内容补充）。
- 功能判据 ⚠️：[未找到原句] —— Ch1 states nothing about what the metering blade does, its setting, or its effect on coat weight. The inference that it *meters*（i.e. doctors the roll surface down to the cell volume, thereby setting the delivered quantity）is etymological and [本报告推导], not chapter content.
- 量化指标：全部 [未找到原句] —— no blade angle, thickness, pressure, material, or expected life.
- ⚠️ 章节间的功能归属 跨章引用：the metering/dosing function is attributed elsewhere in the deck to the cell volume of the roll rather than to the blade（Ch2 SLIDE 18：volume = *"Total volume of all the engraved cells on the roll surface per unit area"*）。Therefore：the delivered quantity is set by the roll's engraving; the blade's role is to realise that quantity by clearing the land area. This division of authority is [本报告推导] and is NOT stated in Ch1.

(d) 原文英文摘录
> *"Doctor Blade Chamber 部件标注：Metering Blade（计量刮刀）、Anilox Roll、Containment Blade（密封刮刀）"* — SLIDE 9 — 图像内容补充

### C9. Containment Blade ｜ 密封刮刀

(a) 中文名 + English term：密封刮刀 / Containment Blade

(b) English definition
> The second of the two blades inside the Doctor Blade Chamber, named in the SLIDE 9 component drawing. As with C8, the chapter provides no written definition of its function.

(c) 操作化定义
- 判定式（位置/命名判据）：the chamber blade identified in the drawing as "Containment Blade"（SLIDE 9 — 图像内容补充）。
- 区分判据（C8 vs C9） [本报告推导]：the two blades are structurally paired and functionally opposite — the chamber is a closed system, so one blade works against the roll's rotation direction（metering / doctoring）and the other works with it（containment / sealing, retaining fluid inside the chamber）。⚠️ This opposition is inferred from the word "containment" and from closed-chamber engineering practice; it is [未找到原句] in this chapter.
- 量化指标：全部 [未找到原句] —— no angle, thickness, pressure, material, or life.
- 采购含义 [本报告推导]：because the two blades are functionally different but physically similar and co-located, they are a high-risk mis-installation / mis-ordering pair. Spare-part numbering must never rely on a shared "chamber blade" description — each must carry a distinct part number tied to its position（metering vs containment）。

(d) 原文英文摘录
> *"Doctor Blade Chamber 部件标注：Metering Blade（计量刮刀）、Anilox Roll、Containment Blade（密封刮刀）"* — SLIDE 9 — 图像内容补充

### C10. Applicator Roll ｜ 涂布转移辊

(a) 中文名 + English term：涂布转移辊 / Applicator Roll

(b) English definition
> The intermediate roll that defines the Indirect form: the path is *"gravure roll to applicator roll to substrate"*（SLIDE 5）。In the ELC stack it sits directly above the Gravure Roll, with the Marrying Roll above it（SLIDE 7 — 图像内容补充）。

(c) 操作化定义
- 判定式（路径判据）：the roll that receives fluid from the gravure roll and delivers it to the substrate；its presence converts a Direct process into an Indirect one（SLIDE 5）。
- 位置判据（ELC，SLIDE 7 — 图像内容补充）：station 5 of 8, i.e. immediately above the Gravure Roll（station 6), immediately below the Marrying Roll（station 4）。Note the roll is listed in the SLIDE 7 text layer as "Applicator Roll" — one of the few roll names that appears in text rather than only in the image。
- 量化指标：[未找到原句] —— no diameter, no covering material or hardness, no nip load, no speed ratio to the gravure roll, no transfer efficiency（% of picked-up fluid handed to the substrate）。
- ⚠️ 关键未知：transfer efficiency is never quantified anywhere in Ch1。This is the single most important missing number for the Indirect route, because with a 2-hop path the delivered coat weight depends on two transfer steps, not one → [未找到原句]，且不得以任何"典型值"填补。

(d) 原文英文摘录
> *"Indirect = gravure roll to applicator roll to substrate…. Facial and  Embossing winders"* — SLIDE 5
> "Applicator Roll" — SLIDE 7（text layer）
> *"自上而下：Upper Rubber Roll → Embossing Cleaning System → Embossing Roll → Marrying Roll → Applicator Roll → Gravure Roll → Steel Calendar Roll → Rubber Calendar Roll"* — SLIDE 7 — 图像内容补充

### C11. Marrying Roll ｜ 贴合辊

(a) 中文名 + English term：贴合辊 / Marrying Roll

(b) English definition
> A roll in the 2 Ply Winder ELC stack, positioned directly above the Applicator Roll (SLIDE 7 — 图像内容补充) and listed in the text layer (SLIDE 7). The chapter gives no written definition of its function.

(c) 操作化定义
- 判定式（位置判据）：in the ELC stack, station 4 of 8, immediately above the Applicator Roll（SLIDE 7 — 图像内容补充）。
- 功能判据 ⚠️：[未找到原句]。The inference that it marries（plies/bonds）two tissue plies together is etymological and [本报告推导]。It is strongly suggested by the asset name — the slide title is "2 Ply Winder ELC"（SLIDE 7) — but the chapter never states what the marrying roll marries, to what, or how。
- 量化指标：全部 [未找到原句] —— no diameter, no covering, no nip load, no bond-strength metric.
- ⚠️ 结构性观察 [本报告推导]：the Marrying Roll appears in the ELC stack but NOT in the Facial OLP chain（SLIDE 8 — 图像内容补充 = DOCTOR CHAMBER → GRAVURE ROLL → RUBBER ROLL → WEB）。Its presence is therefore a ply-count-dependent element: it is needed where 2 plies are combined, absent where a single web is treated. This is consistent with the asset being a "2 Ply Winder". This correlation is [本报告推导]；the causal statement is [未找到原句]。

(d) 原文英文摘录
> "Marrying Roll" — SLIDE 7（text layer）
> *"自上而下：Upper Rubber Roll → Embossing Cleaning System → Embossing Roll → Marrying Roll → Applicator Roll → Gravure Roll → Steel Calendar Roll → Rubber Calendar Roll"* — SLIDE 7 — 图像内容补充

### C12. Embossing Roll ｜ 压花辊

(a) 中文名 + English term：压花辊 / Embossing Roll

(b) English definition
> A roll in the 2 Ply Winder ELC stack, positioned below the Upper Rubber Roll / Embossing Cleaning System and above the Marrying Roll (SLIDE 7 — 图像内容补充), and listed first in the SLIDE 7 text layer. The chapter gives no written definition of its function.

(c) 操作化定义
- 判定式（位置判据）：in the ELC stack, station 3 of 8（SLIDE 7 — 图像内容补充）。
- 配对判据 [本报告推导]：an embossing roll works against a compliant counter-roll; in this stack the Upper Rubber Roll（station 1）is the compliant partner above it, and the Embossing Cleaning System（station 2）sits between them. This rubber-above / embossing-below arrangement is drawn, but the pairing is not stated → the geometry is SLIDE 7 — 图像内容补充, the functional pairing is [本报告推导]。
- 量化指标：全部 [未找到原句] —— no pattern type, no depth, no nip load, no rubber hardness.
- ⚠️ 关键区分（避免与凹版辊混淆） [本报告推导]：the Embossing Roll and the Gravure Roll are both patterned rolls in the same stack, but they do fundamentally different jobs — the gravure roll carries and meters fluid（SLIDE 2）, while the embossing roll deforms the sheet mechanically。⚠️ Ch1 never states this distinction → [未找到原句]；it is inferred from the two names and from SLIDE 2's definition of the gravure roll。
- 与涂布的关系 [本报告推导]：the presence of an Embossing Cleaning System as a dedicated station（station 2）indicates the embossing roll accumulates deposit and requires in-line cleaning — an operational cost element not otherwise mentioned in the chapter。

(d) 原文英文摘录
> "Embossing   Roll" — SLIDE 7（text layer）
> *"自上而下：Upper Rubber Roll → Embossing Cleaning System → Embossing Roll → Marrying Roll → Applicator Roll → Gravure Roll → Steel Calendar Roll → Rubber Calendar Roll"* — SLIDE 7 — 图像内容补充

### C13. Calendar Roll (Steel / Rubber) ｜ 压光辊（钢 / 橡胶）

(a) 中文名 + English term：压光辊（钢辊 / 胶辊）/ Calendar Roll — Steel Calendar Roll ／ Rubber Calendar Roll

(b) English definition
> The lowest two rolls of the 2 Ply Winder ELC stack: Steel Calendar Roll（station 7）above Rubber Calendar Roll（station 8）（SLIDE 7 — 图像内容补充）；both also listed in the SLIDE 7 text layer. The chapter gives no written definition of their function.

(c) 操作化定义
- 判定式（位置 + 材质判据）：the bottom-most pair in the ELC stack；one hard（steel）+ one compliant（rubber）, i.e. a hard/soft nip。The steel roll is above the rubber roll（SLIDE 7 — 图像内容补充）。
- 构型判据：a steel-rubber pair is the classic calendering nip — one hard roll sets the surface, one resilient roll distributes the load. ⚠️ This is [本报告推导]；Ch1 states only the names and positions.
- 序列判据（重要） [本报告推导]：the calendar rolls sit at the very bottom of the stack, downstream of the Gravure Roll → Applicator → Marrying → Embossing sequence. Therefore, in the ELC line, coating/embossing happens first and calendering happens last — i.e. the calender acts on an already-coated, already-embossed sheet. This ordering is read directly off the drawing（SLIDE 7 — 图像内容补充）; the chapter gives no statement about its purpose → the ordering is evidence-based, the rationale is [未找到原句]。
- 量化指标：全部 [未找到原句] —— no diameters, no rubber hardness（P&J / Shore）, no nip load, no temperature, no gloss/bulk/caliper targets.
- ⚠️ 与 Ch4 的张力（值得一记） 跨章引用：Ch4 SLIDE 35 states "High Z direction penetration can also negatively impact bulk/caliper" — i.e. caliper/bulk is a managed product property downstream. The calendar rolls are plausibly the actuator for that property. ⚠️ This link is [本报告推导]；Ch1 does not state it.

(d) 原文英文摘录
> "Steel Calendar Roll" / "Rubber Calendar Roll" — SLIDE 7（text layer）
> *"自上而下：Upper Rubber Roll → Embossing Cleaning System → Embossing Roll → Marrying Roll → Applicator Roll → Gravure Roll → Steel Calendar Roll → Rubber Calendar Roll"* — SLIDE 7 — 图像内容补充

### C14. OLU / DRC / ELC / Facial ｜ KC 产线代号

(a) 中文名 + English term：KC 产线代号 / Production line codes — OLU ／ DRC ／ ELC ／ Facial（含 OLP 与 Embossing winders 两个相关写法）

(b) English definition
> KC's internal asset identifiers for its gravure-equipped lines. SLIDE 5 uses them to map the Direct/Indirect taxonomy onto real plant assets: Direct = DRC and OLU; Indirect = Facial and Embossing winders. SLIDE 7 adds ELC = 2 Ply Winder; SLIDE 8 adds OLP = Facial。

(c) 操作化定义
- 判定式（涂布形式映射，来自 SLIDE 5/6/7/8）：
  | Code | Coating form | Stated as | Evidence |
  |---|---|---|---|
  | DRC | Direct | "DRC and OLU" / "OLU/DRC - Direct Gravure Coating" | SLIDE 5, SLIDE 6 |
  | OLU | Direct | same as above | SLIDE 5, SLIDE 6 |
  | ELC（2 Ply Winder） | Indirect | "2 Ply Winder ELC = Indirect Gravure Coating" | SLIDE 7 |
  | Facial（OLP） | Indirect | "Facial and Embossing winders" / "Facial OLP = Indirect Gravure Coating" | SLIDE 5, SLIDE 8 |
- ⚠️ 缩写展开：Ch1 never expands any of these acronyms. OLU, DRC, ELC, OLP are used as opaque identifiers → 全部 [未找到原句] for their full forms. Do not guess expansions.
- ⚠️ "Embossing winders" vs "ELC" 的关系：SLIDE 5 says *Indirect = … Embossing winders*；SLIDE 7 titles the ELC slide *"2 Ply Winder ELC"*。Whether ELC is one of the "Embossing winders" or a third category is not stated → [未找到原句]。The ELC stack does contain an Embossing Roll（SLIDE 7）, which suggests ELC belongs to the embossing-winder family — but this is [本报告推导], not chapter text.
- 跨章交叉验证（产线→雕刻平台的映射） 跨章引用：
  | Code | Engraving platform（Ch2） | Coating form（Ch1） | Evidence |
  |---|---|---|---|
  | OLU | Laser Engraved Ceramic | Direct | Ch2 SLIDE 11 + Ch1 SLIDE 5/6 |
  | DRC | Laser Engraved Ceramic | Direct | Ch2 SLIDE 11 + Ch1 SLIDE 5/6 |
  | ELC(s) | Laser Engraved Ceramic | Indirect | Ch2 SLIDE 11 + Ch1 SLIDE 7 |
  | Facial | Electro-mechanical Engraved Chrome | Indirect | Ch2 SLIDE 10 + Ch1 SLIDE 5/8 |
- ⚠️ 结论（本表最重要的读法）：the two binaries are crossed, not nested. Coating form does NOT determine engraving platform: ELC is Indirect yet Ceramic, while Facial is Indirect and Chrome. The only clean correlation in the deck is Direct ⇒ Ceramic（OLU, DRC）。See 模块 4 for the full treatment.

(d) 原文英文摘录
> *"Direct = gravure roll to substrate …… DRC and OLU"* — SLIDE 5
> *"Indirect = gravure roll to applicator roll to substrate…. Facial and  Embossing winders"* — SLIDE 5
> "OLU/DRC - Direct Gravure Coating" — SLIDE 6
> *"2 Ply Winder ELC = Indirect Gravure Coating"* — SLIDE 7
> *"Facial OLP = Indirect Gravure Coating"* — SLIDE 8

## 模块 3：证据链（Evidence Tables）



本模块共 5 张表（T1–T5），超出"至少 3 张"的要求。T1–T4 为任务指定；T5 为本次拆解新增，用于固化 模块 1 A2 与 模块 2 C1/C2 所提出的术语不稳定实证。

### T1 — Direct vs Indirect Gravure Coating：路径 / 应用产线 / 辊系组成 全字段对比

Evidence：SLIDE 5 + SLIDE 6 + SLIDE 7 + SLIDE 8 + 各页 图像内容补充

||||||
|---|---|---|---|---|
|1|Fluid path（路径）|gravure roll → substrate（1 hop）|gravure roll → applicator roll → substrate（2 hops）|SLIDE 5|
|2|Defining element|no intermediate roll|an Applicator Roll is mandatory|SLIDE 5|
|3|应用产线（KC assets）|DRC and OLU|Facial and Embossing winders；worked examples = 2 Ply Winder ELC and Facial OLP|SLIDE 5, SLIDE 7, SLIDE 8|
|4|Dedicated slide|SLIDE 6 — "OLU/DRC - Direct Gravure Coating"|SLIDE 7 — *"2 Ply Winder ELC = Indirect Gravure Coating"*；SLIDE 8 — "Facial OLP = Indirect Gravure Coating"|SLIDE 6/7/8|
|5|辊系组成（Direct 构型）|Backing Roll（上, 绿）+ Gravure Roll（下, 蓝）+ Doctor Blade Chamber（左下）；web 水平穿过两辊 nip；Gravure Roll 顺时针旋转|—|SLIDE 6 — 图像内容补充|
|6|辊系组成（Indirect 构型 A：ELC）|—|8 stations top-to-bottom：Upper Rubber Roll → Embossing Cleaning System → Embossing Roll → Marrying Roll → Applicator Roll → Gravure Roll（黄高亮，接 Doctor Blade Chamber）→ Steel Calendar Roll → Rubber Calendar Roll|SLIDE 7 — 图像内容补充|
|7|辊系组成（Indirect 构型 B：Facial OLP）|—|4-element chain：DOCTOR CHAMBER → GRAVURE ROLL → RUBBER ROLL → WEB|SLIDE 8 — 图像内容补充|
|8|Roll count / chain length|2 rolls + 1 chamber（最简构型）|7 rolls + 1 cleaning system + 1 chamber（ELC）；2 rolls + 1 chamber（Facial OLP，最简形式）|本报告推导，清点自 SLIDE 6/7/8 — 图像内容补充|
|9|Doctor Blade Chamber present?|Yes（lower-left of gravure roll）|Yes（ELC：coupled at the Gravure Roll；Facial OLP：first element in the chain）|SLIDE 6/7/8 — 图像内容补充|
|10|Engraving platform（跨章）|Laser Engraved Ceramic（OLU/DRC）|Ceramic for ELCs；Electro-mechanical Chrome for Facial → ⚠️ not one-to-one|Ch2 SLIDE 10/11|
|11|Substrate contact with engraved roll|Yes — the web passes through the gravure-roll nip|No — the web contacts the applicator/rubber roll, not the engraved roll|本报告推导，读自 SLIDE 6/7/8 — 图像内容补充；原文未作此陈述 → 因果说明 [未找到原句]|
|12|Configurations documented per form|1|2（ELC 与 Facial OLP 的辊系不同构）|本报告推导|
|13|Quantitative data given in Ch1|None — no speed, no coat weight, no nip load, no film thickness|None — same gaps|全部 [未找到原句]|


T1 关键读数（Key readings） [本报告推导]
1. The binary is defined by path length, not by hardware count. Indirect does not imply "more rolls" in general — the Facial OLP indirect chain is as short as the direct one（4 elements vs 3）。The only universal difference is the presence of the applicator roll.
2. Indirect is a family, not a machine. ELC（8 stations）and Facial OLP（4 elements）are both "indirect" yet structurally unrelated. Any equipment specification must name the asset, not the form.
3. The chamber is the invariant. It appears in 3/3 configurations — the only component that is truly universal across the chapter.

### T2 — ELC 二层和纸复卷机辊系表（2 Ply Winder ELC Roll Stack，自上而下）

Evidence：SLIDE 7 text layer + SLIDE 7 — 图像内容补充

⚠️ 计数修正（Counting correction）：the task describes this as "8 个辊"。Precisely, the image gives 8 stations top-to-bottom, of which 7 are rolls and 1 is a cleaning system（Embossing Cleaning System）。This report preserves the 8-station ordering exactly as drawn and flags the non-roll station. [本报告推导]

||||||||
|---|---|---|---|---|---|---|
|1|Upper Rubber Roll|上胶辊|✅ 辊|✅|❌ [未找到原句]|SLIDE 7 + 图像内容补充|
|2|Embossing Cleaning System|压花辊清洗系统|❌ 系统，非辊|✅|❌ [未找到原句]|SLIDE 7 + 图像内容补充|
|3|Embossing Roll|压花辊|✅ 辊|✅|❌ [未找到原句]（名称自明）|SLIDE 7 + 图像内容补充|
|4|Marrying Roll|贴合辊|✅ 辊|✅|❌ [未找到原句]（名称自明）|SLIDE 7 + 图像内容补充|
|5|Applicator Roll|涂布转移辊|✅ 辊|✅|✅ 间接涂布的中介辊（SLIDE 5 定义）|SLIDE 5 + SLIDE 7|
|6|Gravure Roll|凹版辊|✅ 辊|✅|✅ "Heart"（SLIDE 2）；黄高亮|SLIDE 2 + SLIDE 7 — 图像内容补充|
|—|（Doctor Blade Chamber）|刮刀腔|❌ 部件（非工位）|✅|✅ 三部件（Metering/Containment Blade）|SLIDE 7 + SLIDE 9 — 图像内容补充|
|7|Steel Calendar Roll|钢压光辊|✅ 辊|✅|❌ [未找到原句]|SLIDE 7 + 图像内容补充|
|8|Rubber Calendar Roll|橡胶压光辊|✅ 辊|✅|❌ [未找到原句]|SLIDE 7 + 图像内容补充|


T2 关键读数
| Reading | Statement | Type | Evidence |
|---|---|---|---|
| R1 | The Gravure Roll is station 6 of 8 — i.e. in the lower half of the stack, and is the only station drawn highlighted in yellow | 事实 | SLIDE 7 — 图像内容补充 |
| R2 | The fluid path（Gravure Roll → Applicator Roll）runs upward（station 6 → station 5） | 事实（读图） | SLIDE 7 — 图像内容补充 |
| R3 | The Doctor Blade Chamber is attached at the Gravure Roll, not at the applicator roll — confirming the chamber serves the metering roll specifically | 事实（读图） | SLIDE 7 — 图像内容补充 |
| R4 | Coating/embossing occur in the upper-mid stack; calendering occurs at the bottom. Calendering is the last operation | [本报告推导] | SLIDE 7 — 图像内容补充 |
| R5 | Only 2 of 8 stations have any functional description in the deck（Applicator Roll via SLIDE 5; Gravure Roll via SLIDE 2）。The other 6 stations are named but never explained | [本报告推导] | SLIDE 7 + SLIDE 2 + SLIDE 5 |
| R6 | ⚠️ No quantitative parameter exists for any of the 8 stations — no diameter, no covering hardness, no nip load, no speed | [未找到原句] | 全章 |
| R7 | The stack contains a dedicated cleaning station（#2）for the embossing roll but none for the gravure roll — an asymmetry in maintenance provisioning that the chapter never comments on | [本报告推导] | SLIDE 7 — 图像内容补充 |

### T3 — DRC 工艺流程序列表（Marinette DRC Process）



⚠️ 来源边界声明（Source boundary）：DRC 工艺流程不在 Ch1 内。 Ch1（幻灯片 1–9）没有任何 DRC 工序内容。本节全部内容来自 Ch3 SLIDE 23，标记 跨章引用。按任务要求纳入，但不得被误读为 Ch1 内容。
Evidence：Ch3 SLIDE 23 — 图像内容补充（原始图注：*Marinette DRC Process（From VULCAN Presentation 1-30-2003）*）

#### T3-a — 提取文档记录的工序顺序（Extraction-documented sequence）

||||||
|---|---|---|---|---|
|1|Vertical Run|垂直段（立式走纸段）|Web transport|Ch3 SLIDE 23 — 图像内容补充|
|2|Former|成形器|Forming|Ch3 SLIDE 23 — 图像内容补充|
|3|Felt Section|毛毯段|Dewatering|Ch3 SLIDE 23 — 图像内容补充|
|4|Yankee Dryer|扬克烘缸|Drying|Ch3 SLIDE 23 — 图像内容补充|
|5|Latex Print (Side 1)|乳胶印刷（第一面）|Gravure 涂布|Ch3 SLIDE 23 — 图像内容补充|
|6|After Dryer|后干燥|Drying|Ch3 SLIDE 23 — 图像内容补充|
|7|Recrepe Dryer #1|再起皱烘缸 1 号|起皱（1st crepe）|Ch3 SLIDE 23 — 图像内容补充|
|8|Recrepe Dryer #2|再起皱烘缸 2 号|起皱（2nd crepe）|Ch3 SLIDE 23 — 图像内容补充|
|9|Latex Cure|乳胶固化|Curing|Ch3 SLIDE 23 — 图像内容补充|
|10|Cool|冷却|Conditioning|Ch3 SLIDE 23 — 图像内容补充|
|11|Reel|卷取|Reeling|Ch3 SLIDE 23 — 图像内容补充|
|—|3-layer H-box|三层流浆箱|Forming（流浆箱）|Ch3 SLIDE 23 — 图像内容补充|


#### T3-b — ⚠️ 两种顺序记录的差异与判定（Discrepancy between the two recorded orderings）

The task specifies one ordering; the extraction file records another. Both are reproduced verbatim below. Neither is altered.

||||
|---|---|---|
|① 任务给定顺序（Task-specified）|Vertical Run → Recrepe Dryer #1 → Latex Print (Side 1) → After Dryer → Yankee Dryer → Felt Section → Former → 3-layer H-box → Latex Print (Side 2) → Recrepe Dryer #2 → Latex Cure → Cool → Reel|13|
|② 提取文件记录顺序（Ch3 SLIDE 23 — 图像内容补充）|Vertical Run → Former → Felt Section → Yankee Dryer → Latex Print (Side 1) → After Dryer → Recrepe Dryer #1 → Recrepe Dryer #2 → Latex Cure → Cool → Reel；含 3-layer H-box 流浆箱|11（+ 1 部件）|


差异判定表
| # | 差异点 | 说明 | 判定 |
|---|---|---|---|
| D1 | 共有单元 | 两版本共享 12 个相同单元（Vertical Run, Former, Felt Section, Yankee Dryer, Latex Print (Side 1), After Dryer, Recrepe Dryer #1, Recrepe Dryer #2, Latex Cure, Cool, Reel, 3-layer H-box） | 一致 |
| D2 | "Latex Print (Side 2)" | 仅出现在①任务版本；提取文件中未出现该单元标注 → [未找到原句]（Ch3 SLIDE 23 — 图像内容补充） | ⚠️ 存疑单元 |
| D3 | 顺序 | ① 将 Recrepe Dryer #1 置于 Latex Print (Side 1) 之前、将 Yankee Dryer 置于 After Dryer 之后、将 Former 置于 Felt Section 之后 —— 三处均在物理上不成立（成形必须先于毛毯段；扬克烘缸必须先于后干燥） | [本报告推导]：① 更可能是原始图面标签的读取顺序，非工艺顺序 |
| D4 | 采用 | 本报告 T3-a 采用 ②（提取文件记录顺序），因其物理顺序自洽，且是拆解管线已留档的读图结果 | 采用 ② |
| D5 | 建议 | 若 "Latex Print (Side 2)" 对结论关键，应回访原始幻灯片第 23 页渲染图复核，不应据任一版本单方定案 | 待核验 |

#### T3-c — "Double ReCrepe" 本质的证据拆解



任务要求：指出"两次起皱 + 两面乳胶印刷"的 Double ReCrepe 本质。

|||||
|---|---|---|---|
|① 两次起皱（Double Re-Crepe）|Recrepe Dryer #1 ＋ Recrepe Dryer #2 —— 两个独立编号的再起皱烘缸|✅ 成立（直接证据）|Ch3 SLIDE 23 — 图像内容补充|
|② 两面乳胶印刷|Latex Print (Side 1) 明确标注 "Side 1"（即存在 Side 概念）；提取文件的总结句明确写 "即 Double ReCrepe：两次起皱 + 两面乳胶印刷"|⚠️ 间接成立 —— "两面"来自提取文件的概括句，而 "Latex Print (Side 2)" 这一具体单元标注在提取文件中 [未找到原句]|Ch3 SLIDE 23 — 图像内容补充|
|③ 产线名|Marinette DRC Process|✅ 成立|Ch3 SLIDE 23 — 图像内容补充|
|④ 来源与时间|From VULCAN Presentation 1-30-2003|✅ 成立|Ch3 SLIDE 23 — 图像内容补充|
|⑤ 与 Gravure 的连接|DRC = Direct Gravure Coating（Ch1 SLIDE 5/6），因此 Latex Print (Side 1) 站即 Direct 凹版涂布站|✅ 成立（跨章合成）|Ch1 SLIDE 5 + Ch1 SLIDE 6 + Ch3 SLIDE 23|
|⑥ 乳胶固化的位置|Latex Cure 位于 Recrepe Dryer #2 之后、Cool 之前 —— 即两次起皱完成后才固化|✅ 成立|Ch3 SLIDE 23 — 图像内容补充|


T3 关键结论（Key conclusions）
1. "Double ReCrepe" 的命名在原文中由两个独立烘缸（#1 / #2）直接支撑，这是本章/本材料中唯一一处工艺命名具有直接硬件证据的地方 —— 名称与设备一一对应，不是营销修辞。跨章引用 Ch3 SLIDE 23
2. "两面乳胶印刷" 的硬件证据弱于"两次起皱"。 "Side 1" 的标注隐含存在第二面，但未在该提取文件中找到 "Latex Print (Side 2)" 的独立标注。⚠️ 判定：结论方向可信，但证据等级为"间接"，需回访原图。
3. 工艺逻辑自洽性检验 [本报告推导]：在 ② 的顺序下，Latex Print (Side 1) 位于 Yankee Dryer 之后、After Dryer 之前，且 Recrepe Dryer #1/#2 紧随其后。这构成一个清晰结构：成形→干燥→印刷→再起皱→固化→卷取。乳胶在起皱前施加、起皱后固化，这与 "ReCrepe"（再起皱）的工艺目的一致——乳胶在起皱过程中起到结构粘结/定型作用。⚠️ 此工艺解释为 [本报告推导]；原文未作任何工艺目的说明 → [未找到原句]。
4. 对 Ch1 的意义：DRC 是 Ch1 中 Direct Gravure Coating 的两条产线之一（SLIDE 5/6）。T3 表明 Direct 路线被用在纸机主线（online，位于 Yankee 之后），而非后加工复卷机 —— 这与 ELC / Facial 的 Indirect 路线位于 winder（复卷机） 形成位置上的根本分野。⚠️ 该"位置分野"为 [本报告推导]：Ch1 称 Indirect 用于 *"Facial and Embossing winders"*（SLIDE 5）而 Direct 用于 OLU/DRC（SLIDE 5/6），Ch3 SLIDE 26 — 图像内容补充 显示 OLU 流程含 *"Tissue Machine → Unwind → Printer Backing Roll → Gravure Roll → …"*。

### T4 — KC 高端产品与凹版辊关系表

Evidence：SLIDE 4 + SLIDE 4 — 图像内容补充 + 跨章映射 Ch1 SLIDE 5/6/7/8、Ch2 SLIDE 10、Ch3 SLIDE 24/28

|||||||||
|---|---|---|---|---|---|---|---|
|1|Cottonelle Luxe|未给出|❌ [未找到原句]|❌ [未找到原句] —— Ch1 未将任何 SKU 映射到产线|❌ 未知|❌ 未知|SLIDE 4 — 图像内容补充|
|2|Kleenex soothing lotion|8 盒装 / 960 抽|❌ [未找到原句]|⚠️ 间接推断："lotion" 对应 Facial 线的乳液涂布；Ch2 SLIDE 10 — SPEAKER NOTES 记 "Jenks Facial Lotion GR – alternating bands of 2 BCM and 6 BCM and some dead bands"|Indirect（若归属 Facial）|Electro-mechanical Engraved Chrome（Ch2 SLIDE 10，若归属 Facial）|SLIDE 4 — 图像内容补充 + Ch2 SLIDE 10 notes（跨章引用）|
|3|Viva Signature Cloth|未给出|❌ [未找到原句]|⚠️ 间接推断：Ch3 SLIDE 28 标题 "OLU – VIVA Gravure Roll Pattern"；Ch3 SLIDE 24 — 图像内容补充 记 "#1 Printer pattern (VIVA® Towel)"|Direct（若归属 OLU）|Laser Engraved Ceramic（Ch2 SLIDE 11，OLU/DRC/ELCs）|SLIDE 4 — 图像内容补充 + Ch3 SLIDE 24/28（跨章引用）|
|4|Scott Shop Original|未给出|❌ [未找到原句]|❌ [未找到原句]|❌ 未知|❌ 未知|SLIDE 4 — 图像内容补充|


T4 关键读数
| Reading | Statement | Type | Evidence |
|---|---|---|---|
| R1 | SLIDE 4 places 4 premium SKUs under a 4-statement value claim（Premium products / differentiation / consumer value and growth / Higher margins）— a 1:1 illustration structure | 事实 | SLIDE 4 + SLIDE 4 — 图像内容补充 |
| R2 | ⚠️ Ch1 never connects any SKU to any line, coating form, or roll. The product–technology link is asserted by layout adjacency, not by text. | [未找到原句] | SLIDE 4（全页无连接性文字） |
| R3 | The only product→technology links available anywhere in the deck are cross-chapter and inferential：Kleenex lotion → Facial（via Ch2 SLIDE 10 notes "Facial Lotion GR"）and Viva → OLU（via Ch3 SLIDE 24/28） | 跨章推断 | Ch2 SLIDE 10 notes, Ch3 SLIDE 24/28 |
| R4 | Kleenex soothing lotion is the single most valuable precedent for the hygiene business：it is the only case in the deck where a lotion（护肤乳液）is applied by gravure, and Ch2 SLIDE 10 notes gives both the coat-weight bands（2 BCM / 6 BCM） and the pattern strategy（dead bands = zero-transfer zones） | 跨章推断 | Ch2 SLIDE 10 — SPEAKER NOTES |
| R5 | ⚠️ Cottonelle Luxe 与 Scott Shop Original 在本材料全四章中均无任何技术归属证据 | [未找到原句] | 全四章 |
| R6 | The "960 抽" / "8 盒装" on the Kleenex image is the only numeric figure on SLIDE 4 — it is a consumer pack count, not a process parameter，and must not be mis-read as such | 事实/防误读 | SLIDE 4 — 图像内容补充 |

### T5 — 🆕 术语不稳定实证表（Terminological Instability Evidence）— 支撑 A2 / C1 / C2

Evidence：SLIDE 2 — SPEAKER NOTES、SLIDE 7、SLIDE 8、SLIDE 9 — 图像内容补充、Ch2 SLIDE 11/13/20、Ch2 SLIDE 13 — SPEAKER NOTES（跨章）

||||||||
|---|---|---|---|---|---|---|
|1|SLIDE 7 (text + image)|Gravure Roll|Indirect（ELC）|gravure ⇢ direct|❌ 违反|SLIDE 7 + SLIDE 7 — 图像内容补充|
|2|SLIDE 8 (text + image)|GRAVURE ROLL|Indirect（Facial OLP）|gravure ⇢ direct|❌ 违反|SLIDE 8 + SLIDE 8 — 图像内容补充|
|3|SLIDE 9 (image)|Anilox Roll|（chamber detail；serves both forms）|anilox ⇢ indirect + simple|❌ 术语换用|SLIDE 9 — 图像内容补充|
|4|Ch2 SLIDE 11|Laser Engraved Ceramic Rolls (OLU/DRC/ELCs)|mixed（OLU/DRC = Direct；ELC = Indirect）|—|—|Ch2 SLIDE 11|
|5|Ch2 SLIDE 13|Standard Ceramic Anilox Roll Engravings|同上（同一批资产）|anilox ⇢ simple|❌ 与 #4 命名冲突|Ch2 SLIDE 13|
|6|Ch2 SLIDE 20|"Outside the engravers comfort zones / 'Deep' engravings / 'Large' cells"|同批资产|anilox ⇢ common/simple|❌ 与 "simple" 直接矛盾|Ch2 SLIDE 20|
|7|Ch2 SLIDE 13 — SPEAKER NOTES|"Anilox vs Gravure and Apex Owner Discussion this week"|—|—|🔴 KC 内部术语争议未决|Ch2 SLIDE 13 notes|


T5 结论 [本报告推导]
- 7 条证据中，5 条为直接违反或冲突，1 条为术语换用，1 条为 KC 内部未决争议。 The gravure/anilox distinction has no operational validity in this deck.
- Risk statement：any specification, RFQ, contract, or spare-part order that identifies the part by the noun rather than by asset + measurable parameters carries a real risk of supplying the wrong item, because KC itself uses both nouns for the same component.
- Mitigation（见 C1/C2 的操作化结论）：identify the roll by asset + parameter set（e.g. OLU VIVA GR#5 — 27 dpi dot, 2:1 spacing, 27.6 BCM），never by noun alone.

## 模块 4：章节间衔接（Chapter Connections）

### 4.1 与后章 Ch2（Engraving & Specs）：为何"涂布形式"决定"雕刻方式"



衔接命题：Ch1 establishes what the roll must deliver（a precise amount of fluid, via a Direct or Indirect path）。Ch2 establishes how that requirement is manufactured（chrome electro-mechanical vs ceramic laser）。The bridge is：the coating form sets the duty cycle and the pattern complexity, and those two variables select the engraving platform.

#### 4.1-a — 对应关系对比表

|||||||
|---|---|---|---|---|---|
|1|Direct / Indirect 二分|SLIDE 5|Chrome / Ceramic 二分|Ch2 SLIDE 10 / Ch2 SLIDE 11|⚠️ 交叉而非嵌套（见 4.1-b）|
|2|*"delivers a precise amount of fluid"*|SLIDE 2|Cell volume（BCM / cm³/m²）与 Line screen（LPI）|Ch2 SLIDE 16, Ch2 SLIDE 18|Ch1 提出"精确"的要求，Ch2 给出"精确"的度量|
|3|*"Consistent coating weights"*|SLIDE 5|Ceramic：*"more precise and consistent fluid transfer"；Chrome："variability due to plating inconsistency"*|Ch2 SLIDE 11 / Ch2 SLIDE 10|Ch1 的"一致性"诉求在 Ch2 被兑现为平台选择的判据|
|4|*"Engraved roll"*|SLIDE 2|Laser engraving（~10 μm 圆孔 → 六边形；角部 ≥3 次曝光）|Ch2 SLIDE 14|Ch1 只说"有雕刻"，Ch2 解释雕刻是怎么形成的|
|5|*"patterned"*（gravure 的行业内涵）|SLIDE 2 — SPEAKER NOTES|"Engineered patterns - DRC/OLU/Facial"；*"Not just printing/coating …. Creating product properties*|Ch2 SLIDE 20|Ch1 的"patterned"内涵在 Ch2 升级为 KC 的核心能力主张|
|6|*"common/simple engraving"*（anilox 的行业内涵）|SLIDE 2 — SPEAKER NOTES|"Outside the engravers comfort zones / 'Deep' engravings / 'Large' cells"|Ch2 SLIDE 20|🔴 直接矛盾 —— KC 的雕刻不简单（见 T5 #6）|
|7|Doctor Blade Chamber（三部件）|SLIDE 9 — 图像内容补充|*"Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear"*|Ch2 SLIDE 14|Ch1 画出腔体，Ch2 给出腔体耗材的失效机理|
|8|*"Enhanced properties create Premium products"*|SLIDE 4|*"Not just printing/coating …. Creating product properties"*|Ch2 SLIDE 20|同一命题的两个层面：业务层（Ch1）／工艺层（Ch2）|
|9|"Heart" of printing/coating process|SLIDE 2|10 道制造工序（雕刻仅为第 9 道）|Ch2 SLIDE 12|Ch2 把 Ch1 的"心脏"还原为一条 10 工序制造链|
|10|OLU / DRC / ELC / Facial 产线代号|SLIDE 5/6/7/8|代号被直接用作平台归属标签：(Facial) / (OLU/DRC/ELCs)|Ch2 SLIDE 10 / Ch2 SLIDE 11|产线代号是两章之间的主键（primary key）|


#### 4.1-b — ⚠️ 核心结论："涂布形式"并不完全决定"雕刻方式"

||||||
|---|---|---|---|---|
|OLU|Direct|Ceramic / Laser|✅ Direct ⇒ Ceramic|Ch1 SLIDE 5/6 + Ch2 SLIDE 11|
|DRC|Direct|Ceramic / Laser|✅ Direct ⇒ Ceramic|Ch1 SLIDE 5/6 + Ch2 SLIDE 11|
|ELC|Indirect|Ceramic / Laser|❌ Indirect ⇏ Chrome|Ch1 SLIDE 7 + Ch2 SLIDE 11|
|Facial|Indirect|Chrome / Electro-mechanical|✅ Indirect ⇒ Chrome|Ch1 SLIDE 5/8 + Ch2 SLIDE 10|


读法
- 成立的单向蕴含：Direct ⇒ Ceramic（OLU, DRC, 2/2 命中）。
- 不成立的蕴含：Indirect ⇏ Chrome —— ELC 是反例（Indirect 但用陶瓷）。
- 因此：涂布形式是必要但不充分的判据。雕刻平台的真正决定因素，Ch2 指向的是图案复杂度与寿命/一致性要求，而非路径长短：Ch2 SLIDE 20（*"Engineered patterns", "Deep engravings", "Large cells", "Outside the engravers comfort zones"）与 Ch2 SLIDE 11（"longer engraving life", "more engraving flexibility", "more precise and consistent fluid transfer"*）。
- ⚠️ 学术诚信声明：Ch1 与 Ch2 均未直接陈述"涂布形式决定雕刻方式"这一因果命题。 该命题是 [本报告推导]，由两章的资产标签一致性反推得出。必须标注为推断，不得作为原文主张引用。

#### 4.1-c — 为什么 Ch1 的"涂布形式"是 Ch2 的必要前置

||||
|---|---|---|
|Direct / Indirect 的资产归属|Ch2 的 (Facial) 与 (OLU/DRC/ELCs) 两个括号标签依赖 Ch1 的产线定义才能解读；若不知 ELC 是 Indirect，则 Ch2 SLIDE 11 的分组无从理解|Ch1 SLIDE 7 + Ch2 SLIDE 11|
|"precise amount" 的要求|Ch2 全部计量体系（BCM、LPI、cell geometry）都是为兑现这一要求而存在|Ch1 SLIDE 2 + Ch2 SLIDE 16/18|
|"Heart" 的定位|解释了为什么 Ch2 愿意为陶瓷支付 "Higher cost"（Ch2 SLIDE 11）——因为它是心脏部件|Ch1 SLIDE 2 + Ch2 SLIDE 11|
|Doctor Blade Chamber 的存在|使 Ch2 SLIDE 14 的 "eliminate excessive doctor blade wear" 有落点|Ch1 SLIDE 9 + Ch2 SLIDE 14|


### 4.2 与后章 Ch3（Vendors & Patterns）：Direct 路线的 DRC/OLU 为何必须用陶瓷激光辊



衔接命题：Ch1 assigns DRC/OLU to the Direct route; Ch2 assigns OLU/DRC/ELCs to laser-engraved ceramic; Ch3 then documents what that assignment costs in supplier-management terms。The chain is：Direct ⇒（Ch2）Ceramic ⇒（Ch3）hard-to-source, hard-to-engrave, production-critical.

#### 4.2-a — 三段式因果链证据表

||||||
|---|---|---|---|---|
|① Ch1|DRC/OLU = Direct|*"Direct = gravure roll to substrate …… DRC and OLU"；"OLU/DRC - Direct Gravure Coating"*|SLIDE 5, SLIDE 6|✅ 直陈|
|② Ch2|OLU/DRC/ELCs = Laser Engraved Ceramic|"Laser Engraved Ceramic Rolls (OLU/DRC/ELCs) — Pros - More resistant to corrosion and abrasion, longer engraving life, more engraving flexibility, more precise and consistent fluid transfer, vendor competition / Cons - Higher cost"|Ch2 SLIDE 11|✅ 直陈|
|③ Ch2|该批辊的图案超出雕刻商常规能力|*"Unique KC Gravure rolls — This is where the MAGIC happens / Engineered patterns - DRC/OLU/Facial / Outside the engravers comfort zones / 'Deep' engravings / 'Large' cells / Large amount of unengraved area = more complex polishing"*|Ch2 SLIDE 20|✅ 直陈|
|④ Ch3|供应商爬坡困难、周期极长|*"Harper took 9 months to engrave first roll and then had a large volume skew"*|Ch3 SLIDE 34 — SPEAKER NOTES|✅ 直陈|
|⑤ Ch3|雕刻一致性难以保证|"Engraved with 3 vendors and struggled with engraving consistency and quality until Pamarco came on line in Q3 2024"|Ch3 SLIDE 32 — SPEAKER NOTES|✅ 直陈|
|⑥ Ch3|产线级刚性依赖|"Tissue machine can't run without 2 functional gravure rolls"|Ch3 SLIDE 23 — SPEAKER NOTES|✅ 直陈|
|⑦ Ch3|需反复重抛光|"Re-Polish #1 / Re-Polish #2 / Re-Polish #3"（Apex VIVA Trial #2）|Ch3 SLIDE 31|✅ 直陈|
|⑧ Ch3|供应商池规模|4 家：Harper（Charlotte, NC）／Precision Roll Solutions / IR Engraving（Richmond, VA）／Pamarco（Atlanta, GA）／Apex（Pittsburgh, PA）|Ch3 SLIDE 22 — 图像内容补充|✅ 直陈|


#### 4.2-b — ⚠️ 关键学术诚信判定："为什么 Direct 必须用陶瓷"原文并未给出

||||
|---|---|---|
|Ch1 是否说明 Direct 需用陶瓷？|❌ [未找到原句]|Ch1 全章未提及陶瓷、激光、镀铬或任何雕刻方法|
|Ch2 是否说明"Direct ⇒ Ceramic"的原因？|❌ [未找到原句]|Ch2 SLIDE 11 只给出归属（OLU/DRC/ELCs = Ceramic）与优缺点，未解释为何如此分配|
|Ch1/Ch2 是否给出选型规则或判据？|❌ [未找到原句]|两章均无"若…则用陶瓷"形式的条件句|
|可确证的|✅ 归属关系本身|OLU/DRC/ELCs → Ceramic（Ch2 SLIDE 11）；OLU/DRC → Direct（Ch1 SLIDE 5/6）。归属是事实，原因未陈述。|



🔴 结论："Direct 路线的 DRC/OLU 为何必须用陶瓷激光辊"这一因果命题，在原材料中是一个[未找到原句]的空白。 本材料能确证的只有归属（assignment），不能确证机理（rationale）。任何"因为 Direct 是直接接触基材所以磨损大所以必须陶瓷"的表述，均为 [本报告推导]，不得作为原文主张引用。

#### 4.2-c — 可确证的 Ch3 后果链（不依赖上述未证因果）

|||||
|---|---|---|---|
|OLU/DRC = Direct（SLIDE 5/6）|Ceramic / Laser（Ch2 SLIDE 11）|图案超常规（Ch2 SLIDE 20）→ Harper 首件 9 个月（Ch3 SLIDE 34）→ 3 家供应商雕刻一致性失败，直到 Pamarco Q3 2024 上线（Ch3 SLIDE 32）|Direct 路线的陶瓷辊是长周期、高风险、供应商能力敏感的关键件|
|Doctor Blade Chamber（SLIDE 9）|抛光决定刀片磨损（Ch2 SLIDE 14）|Apex 需 3 次重抛光（Ch3 SLIDE 31）|抛光能力是与雕刻能力并列的供应商准入门槛|
|Gravure Roll = "Heart"（SLIDE 2）|10 道工序链（Ch2 SLIDE 12）|*"Tissue machine can't run without 2 functional gravure rolls"*（Ch3 SLIDE 23 notes）|雕刻辊是产线级刚性瓶颈件，须双源 + 备辊|
|ELC = Indirect（SLIDE 7）|ELC 同样归陶瓷组（Ch2 SLIDE 11）|ELC 图案为 2 PLY bath/towel embossing（Ch3 SLIDE 13 notes）|陶瓷平台并非 Direct 专属；采购应按平台而非按涂布形式建物料组|


#### 4.2-d — 与 Ch4 的延伸衔接（前瞻）

||||
|---|---|---|
|*"precise amount of fluid"*（SLIDE 2）|细胞直径 vs 细胞深度的取舍：*"Engraver must have at least 1 degree of freedom. Can only specify 2 from the key engraving parameters of volume, depth, and diameter"*（Ch4 SLIDE 36）|跨章引用|
|*"Enhanced properties"*（SLIDE 4）|属性→细胞维度的显式映射：*"X and Y direction sheet surface coverage - Key to GMT (Cell diameter) / Z direction sheet penetration - Key to VIVA/WypAll Z peel strength (Cell depth)"*（Ch4 SLIDE 35）|跨章引用|
|Direct/Indirect 二分（SLIDE 5）|带式辊加速迭代：*"Banded gravure rolls can help speed up the iterative process – typically don't produce sellable product – RSR not MSR"*（Ch4 SLIDE 36）|跨章引用|


## 模块 5：业务连接点（Business Connections）



业务背景：卫材（纸尿裤 / 湿巾）创新研发 ＋ 木浆与纸品战略采购
说明：本模块所有数值若非引自章节，均标 本报告推导；章节未覆盖的法规/市场/技术内容标 外部背景，非本章内容。
⚠️ Ch1 数据边界预警：Ch1 不含任何涂布量、线速度、粘度、刮刀角度、刮刀寿命、辊径、包胶硬度或张力数值。因此本模块的"关键数据"大量标 [未找到原句]。这是真实的材料缺口，不是遗漏。

### 连接点 1 — 凹版涂布在卫材领域的迁移可能：乳胶 / 功能性涂层（护肤乳液、抗菌剂、导流层亲水处理）能否用 gravure 精准定量涂布

涉及幻灯片：SLIDE 2（定义与"Heart"）、SLIDE 4（高端产品与价值主张）、SLIDE 5（Gravure Coating 的三项特性）、SLIDE 9（刮刀腔三部件）、Ch2 SLIDE 10 — SPEAKER NOTES（Facial Lotion GR 实例）、Ch4 SLIDE 35（属性→细胞维度映射）

核心概念：Gravure Roll（C1）；Gravure Coating（C3）；Doctor Blade Chamber（C7）；Metering Blade（C8）；Direct / Indirect（C4 / C5）；产线代号（C14）

关键数据
| 数据 | 值 | 来源 |
|---|---|---|
| 凹版涂布的定义性能力 | *"delivers a precise amount of fluid"* ／ *"Consistent coating weights"* ／ *"Suitable for high-speed processes"* | SLIDE 2, SLIDE 5 |
| 护肤乳液涂布的现成先例 | Jenks Facial Lotion GR — 交替条带 2 BCM 与 6 BCM，另设 dead bands（零转移区） | Ch2 SLIDE 10 — SPEAKER NOTES（跨章引用） |
| 该先例的涂布形式 | Indirect（Facial） | Ch1 SLIDE 5/8 |
| 该先例的雕刻平台 | Electro-mechanical Engraved Chrome | Ch2 SLIDE 10（跨章引用） |
| 体积→膜厚的换算基准 | 1 BCM/in² = 1.55 cm³/m² ⇒ 1 BCM ≈ 1.55 µm 等效平均湿膜厚 | Ch2 SLIDE 18 + [本报告推导] |
| 由 BCM 反推的乳液涂布量级 | 2 BCM ≈ 3.1 µm；6 BCM ≈ 9.3 µm 等效平均湿膜厚 | [本报告推导]（基于上两行） |
| KC 实测量级参照 | OLU VIVA 27.6 BCM；OLU VENUS 3,800,000 μm³ ± 5% | Ch3 SLIDE 28 / Ch3 SLIDE 32 — 图像内容补充（跨章引用） |
| 属性→细胞维度的映射规则 | X/Y 表面覆盖 ⇒ Cell diameter；Z 向渗透 ⇒ Cell depth；"High Z direction penetration can also negatively impact bulk/caliper" | Ch4 SLIDE 35（跨章引用） |
| 抗菌剂涂布 | ❌ [未找到原句] —— 全四章无抗菌剂相关内容 | 全四章 |
| 导流层 / 亲水处理（ADL, hydrophilic treatment） | ❌ [未找到原句] —— 全四章无导流层、亲水剂、表面活性剂相关内容 | 全四章 |
| 卫材（纸尿裤 / 湿巾）基材 | ❌ [未找到原句] —— 全四章全部案例均为生活用纸（tissue/towel/bath/facial），无卫材案例 | 全四章 |
| 涂液粘度/固含/表面张力 | ❌ [未找到原句] | 全四章 |

可行性判断表（本报告推导，非原文结论）
| 迁移对象 | 材料内证据强度 | 判断 | 依据与缺口 |
|---|---|---|---|
| 护肤乳液（lotion / 护肤剂） | 🟢 强 | 可直接迁移论证 | KC 已有商业化先例：Ch2 SLIDE 10 notes 的 Jenks Facial Lotion GR，且给出 2 / 6 BCM 与 dead band 图案策略。卫材的护肤乳液涂布在机理上同构（低涂布量、图案化、需零转移区避开吸收体/弹性体） |
| 乳胶（latex，用于结构粘结/定型） | 🟢 强 | 可直接迁移论证 | Ch3 SLIDE 23 的 Latex Print (Side 1) + Latex Cure；Ch3 SLIDE 24 的 Red dots = latex, Green = fiber。卫材中的结构胶/弹性体定位胶在定量与图案化需求上同构 |
| 抗菌剂 | 🔴 无 | 不可据本材料论证 | 全四章无相关内容。需新建证据：抗菌剂与陶瓷/镀铬表面的相容性、低涂布量下的均匀性、法规（生物杀灭剂）合规性 |
| 导流层亲水处理 | 🔴 无 | 不可据本材料论证 | 全四章无相关内容。且存在机理风险：亲水处理通常要求全幅均匀覆盖，而 gravure 的本质是网穴离散点阵转移（SLIDE 2 图像：蜂窝/棱锥网穴），与"全幅连续膜"存在原理性张力 |
| 共同的最大未知：基材 | 🔴 无 | ⚠️ 阻断性缺口 | 全部 KC 案例基材为干态生活用纸。卫材的 SAP/绒毛浆吸收芯、纺粘/热风非织造布、PE 底膜在强度、伸长率、孔隙率、热敏感性上与之差异极大。Ch1 SLIDE 6 — 图像内容补充 显示 Direct 路线基材需穿过压区，对低强度基材是明确风险 |

可执行行动建议
1. 【从乳液切入，不要从抗菌剂切入】 本报告推导：优先把 护肤乳液 作为 gravure 迁移的首个验证对象，因为它是全材料唯一有商业化先例 + 有具体 BCM 数值 + 有图案策略（dead band）的功能性涂布（证据：Ch2 SLIDE 10 notes）。抗菌剂与导流层处理在本材料中零证据，应先做文献/专利调研再立项。
2. 【以 2 / 6 BCM 作为涂料开发的起点区间，而非目标值】 本报告推导：把 2 BCM（≈3.1 µm） 与 6 BCM（≈9.3 µm） 作为初始 DOE 的两个水平，用于卫材护肤乳液的涂布量爬坡。⚠️ 注意：这是 Facial 线（Indirect, Chrome） 的数值，卫材需重新标定；且 Ch3 SLIDE 28 显示 OLU（Direct）的 VIVA 达 27.6 BCM —— 不同产线的量级差 4–14 倍，禁止跨线套用。
3. 【用 dead band 图案解决"避涂"需求】 本报告推导：Ch2 SLIDE 10 notes 的 "some dead bands designed for areas where no transfer will take place" 是图案化避涂的成熟方案。卫材中需在吸收芯区、弹性腰围、魔术贴区避免涂布时，应直接采用 dead band 设计，而非降低整体涂布量。这是本材料对卫材最有价值的单点可迁移技术。
4. 【先做"基材可穿越性"的独立验证，再谈涂布量】 本报告推导：因为 Direct 路线基材穿过 gravure 压区（SLIDE 6 — 图像内容补充），而 Indirect 路线基材不接触雕刻辊（SLIDE 7/8 — 图像内容补充）。卫材多为低强度非织造布，建议首轮验证直接排除 Direct，走 Indirect。理由见连接点 2。
5. 【把"Z 向渗透"设为首要失效模式做前期评估】 本报告推导：Ch4 SLIDE 35 明确 *"High Z direction penetration can also negatively impact bulk/caliper"*。卫材导流层/面层若涂液过度渗入，会堵塞孔隙、破坏导流结构。故在细胞设计上应优先约束 cell depth（Ch4 指出 Z 向渗透由 cell depth 决定），而非优先追求表面覆盖。
6. 【明确标注本材料的证据边界，避免内部决策被"KC 做过"误导】 ⚠️ 风险提示：KC 的案例全部是生活用纸。若内部立项书写"KC 已用 gravure 做功能性涂布"，应同时注明基材差异，否则会以错误的类比支撑投资决策。

### 连接点 2 — Direct vs Indirect 选择判据（涂层厚度、基材强度、线速度）

涉及幻灯片：SLIDE 5（定义与资产映射）、SLIDE 6（Direct 构型）、SLIDE 7（ELC Indirect 构型）、SLIDE 8（Facial OLP Indirect 构型）、Ch2 SLIDE 10/11（雕刻平台）、Ch4 SLIDE 35（渗透与厚度后果）

核心概念：Direct Gravure Coating（C4）；Indirect Gravure Coating（C5）；Backing Roll（C6）；Applicator Roll（C10）；Gravure Coating（C3）

⚠️ 严正的数据边界声明：Ch1 完全没有给出涂层厚度、基材强度、线速度的任何数值。 任务要求的三个判据，Ch1 一个都没有量化。以下表格中，只有"构型事实"来自原文；判据方向全部是 [本报告推导]，由 SLIDE 6/7/8 的物理构型反推。不得把推导当作原文主张引用。

判据对比表
| # | 判据 | Direct（SLIDE 6） | Indirect（SLIDE 7/8） | 构型事实证据 | 判据方向来源 |
|---|---|---|---|---|---|
| 1 | Fluid path | gravure roll → substrate（1 hop） | gravure roll → applicator roll → substrate（2 hops） | SLIDE 5 | ✅ 原文 |
| 2 | 基材是否接触雕刻辊 | ✅ 是 —— 基材水平穿过 Backing Roll / Gravure Roll 压区 | ❌ 否 —— 基材接触 Applicator / Rubber Roll，雕刻辊只与中介辊接触 | SLIDE 6 — 图像内容补充 vs SLIDE 7/8 — 图像内容补充 | ✅ 原文（读图） |
| 3 | 基材是否承受 nip 压力 | ✅ 是 | ✅ 是（但压区在 applicator/rubber roll 侧，且 rubber 为弹性体） | 同上 | [本报告推导] |
| 4 | 转移次数 | 1 次 | 2 次 | SLIDE 5 | [本报告推导] |
| 5 | 涂布量上限 | 推测更高（单次转移，无二次损失） | 推测更低（两次转移，各有损失） | ❌ 原文无数据 | [本报告推导] ⚠️ 无原文支撑 |
| 6 | 涂布均匀性 / 图案保真度 | 推测更高（无中介辊的图案平滑效应） | 推测较低（中介辊会平滑/扩散图案） | ❌ 原文无数据 | [本报告推导] ⚠️ 无原文支撑 |
| 7 | 对低强度基材的适用性 | 推测较差 | 推测较好 | ❌ 原文无数据 | [本报告推导] ⚠️ 无原文支撑 |
| 8 | 线速度 | ❌ [未找到原句] —— Ch1 仅称 gravure coating *"Suitable for high-speed processes"*，未区分 Direct/Indirect 的速度能力 | 同左 | SLIDE 5 | ⚠️ 速度判据在本材料中完全缺失 |
| 9 | 涂层厚度 | ❌ [未找到原句] —— Ch1 无涂布量数值，无膜厚数值 | 同左 | — | ⚠️ 厚度判据在本材料中完全缺失 |
| 10 | 基材强度 | ❌ [未找到原句] —— Ch1 未提基材强度 | 同左 | — | ⚠️ 强度判据在本材料中完全缺失 |
| 11 | 辊系复杂度 / 投资 | 2 辊 + 1 腔（最简） | 7 辊 + 1 清洗系统 + 1 腔（ELC）／2 辊 + 1 腔（Facial OLP） | SLIDE 6/7/8 — 图像内容补充 | ✅ 原文（读图清点） |
| 12 | 雕刻平台（跨章） | Ceramic / Laser（OLU, DRC） | Ceramic（ELC）或 Chrome（Facial） | Ch2 SLIDE 10/11 | ✅ 原文（跨章） |
| 13 | 产线位置（跨章推断） | 纸机主线（Ch3 SLIDE 23 DRC 位于 Yankee 后；Ch3 SLIDE 26 OLU 为 Tissue Machine → …） | 复卷机 / winder（Ch1 原文称 *"Facial and Embossing winders"*） | Ch1 SLIDE 5 + Ch3 SLIDE 23/26 | ✅ 部分原文 + 部分推导 |

可执行行动建议
1. 【卫材首轮验证：默认选 Indirect】 本报告推导：卫材基材（纺粘/热风非织造布、绒毛浆芯、PE 膜）强度与耐热性普遍低于生活用纸原纸。Direct 路线要求基材直接穿过雕刻辊压区（SLIDE 6 — 图像内容补充），风险显著更高。建议首轮全部走 Indirect（applicator roll 中转），把 Direct 留作已知高强度基材（如某些纺粘布）的第二阶段选项。
2. 【把"转移次数"写进 DOE，因为它是唯一的确定性差异】 本报告推导：SLIDE 5 确证的唯一硬差异是 1 hop vs 2 hops。因此涂布量标定必须按 hop 数分别做——Direct 只需标定"网穴容积→上料量"；Indirect 还需标定"两次转移效率"。⚠️ Ch1 未给出任何转移效率数值 → [未找到原句]，必须实测，不得引用行业典型值。
3. 【不要以线速度作为 Direct/Indirect 的选型依据】 ⚠️ 重要纠偏：SLIDE 5 只说 gravure coating 整体 *"Suitable for high-speed processes"*，从未说明 Direct 或 Indirect 谁更快。任何"Direct 速度更高/更低"的说法都是编造。 速度能力须向设备供应商取证。
4. 【不要以涂层厚度作为选型依据】 ⚠️ 同样的纠偏：Ch1 无涂布量/膜厚数值。厚度能力来自 cell volume（Ch2 的 BCM 体系），而非涂布形式。正确路径是：先定目标涂布量 → 反推 BCM → 再由 BCM 与基材强度共同决定 Direct/Indirect。⚠️ 这个决策顺序是 [本报告推导]，原文未给出。
5. 【辊系复杂度应计入 CAPEX 与备件库存】 本报告推导：ELC 的 8 工位 vs Facial OLP 的 4 单元 vs Direct 的 3 单元，意味着备件 SKU 数量、维护工时、校准复杂度差异巨大。Indirect（尤其 ELC 类）的隐性持有成本远高于 Direct。采购应在 TCO 模型中显式计入。
6. 【用 Ch1 的"产线位置"差异指导产能规划】 本报告推导：Direct（DRC/OLU）似位于纸机主线，Indirect（Facial/Embossing winders）位于复卷机（SLIDE 5 原文用词 *"winders"*）。若卫材产线为离线涂布（offline converting），则 Indirect 的组织形态更匹配；若追求在线集成，才需评估 Direct。⚠️ 该"位置分野"部分依赖 Ch3 SLIDE 23/26 的跨章读图，为 [本报告推导]。

### 连接点 3 — 刮刀腔三部件（Metering / Containment Blade）对涂布量与寿命的影响：设备选型与备件采购考量点

涉及幻灯片：SLIDE 9（三部件标注）、SLIDE 6（Direct 腔体位置）、SLIDE 7（ELC 腔体耦合于 Gravure Roll）、SLIDE 8（Facial OLP 腔体为链路首元素）、Ch2 SLIDE 14（抛光→刀片磨损）、Ch3 SLIDE 31（3 次重抛光）、Ch4 SLIDE 37（测量工具）

核心概念：Doctor Blade Chamber（C7）；Metering Blade（C8）；Containment Blade（C9）；Gravure Roll（C1）

⚠️ 数据边界：Ch1 对刮刀腔只给了 3 个名字，没有任何参数。 以下"影响"部分大量为 [未找到原句]；凡有原文支撑者均已标注。

关键数据
| 数据 | 值 | 来源 |
|---|---|---|
| 刮刀腔组成 | 3 部件：Metering Blade（计量刮刀）／Anilox Roll／Containment Blade（密封刮刀） | SLIDE 9 — 图像内容补充 |
| 腔体在三种构型中的出现率 | 3 / 3（Direct、ELC、Facial OLP 全部配置） | SLIDE 6/7/8 — 图像内容补充 |
| 腔体在 Direct 中的位置 | Gravure Roll 左下 | SLIDE 6 — 图像内容补充 |
| 腔体在 ELC 中的耦合对象 | Gravure Roll（黄高亮站） | SLIDE 7 — 图像内容补充 |
| 腔体在 Facial OLP 中的位置 | DOCTOR CHAMBER → GRAVURE ROLL → …，即链路首元素 | SLIDE 8 — 图像内容补充 |
| 唯一的刀片磨损机理（跨章） | *"Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear"* | Ch2 SLIDE 14（跨章引用） |
| 角部曝光不对称性（跨章） | *"Each corner is exposed to the laser a minimum of 3 times compared to the side walls"* | Ch2 SLIDE 14（跨章引用） |
| 抛光不足的实证（跨章） | Apex VIVA Trial #2 需 Re-Polish #1 / #2 / #3 | Ch3 SLIDE 31（跨章引用） |
| 抛光难度的结构性来源（跨章） | *"Large amount of unengraved area = more complex polishing"* | Ch2 SLIDE 20（跨章引用） |
| 计量工具（跨章） | Capatch strips ／ Impression strips ／ 3DQC measurement system | Ch4 SLIDE 37（跨章引用） |
| Metering Blade 的功能说明 | ❌ [未找到原句] | Ch1 仅有名称 |
| Containment Blade 的功能说明 | ❌ [未找到原句] | Ch1 仅有名称 |
| 刀片对涂布量的影响（定量） | ❌ [未找到原句] | 全四章无定量关系 |
| 刀片角度 / 厚度 / 压力 / 材质 | ❌ [未找到原句] | 全四章无 |
| 刀片寿命 / 更换周期 / 磨损率 | ❌ [未找到原句] | 全四章无 |
| 腔体压力 / 密封压差 | ❌ [未找到原句] | 全四章无 |
| Metering 与 Containment 的区分判据 | ❌ [未找到原句] | Ch1 只给名称，未给判别方法 |

因果链（唯一被原文闭合的一条）

Laser engraving (Ch2 SLIDE 14: ~10 μm round hole → hexagon)
   ↓  each corner exposed ≥ 3× (Ch2 SLIDE 14)
Raised peaks in the corners (Ch2 SLIDE 14)
   ↓  NOT removed by polishing
Excessive doctor blade wear (Ch2 SLIDE 14)
   ↓
Blade = consumable cost + changeover downtime (Ch1 SLIDE 9 chamber location)

⚠️ 链条的最后一环（磨损→成本/停机）是 [本报告推导]；前三环是 Ch2 SLIDE 14 原文。Ch1 在这条链中的位置是：它确定了"腔体必然存在且必然耦合于雕刻辊"（3/3 构型），因此 Ch2 的磨损机理在每一条产线上都必然发生。

可执行行动建议
1. 【把刮刀腔与辊作为"一个耦合系统"采购，而不是两个独立品类】 本报告推导：Ch2 SLIDE 14 证明刀片磨损由辊的表面状态（角峰）决定，而非由刀片自身决定。因此：① 辊的抛光验收标准应与刀片寿命指标绑定写入同一份技术协议；② 新辊入库应同时验收抛光质量，不能只验容积 BCM。依据：Ch2 SLIDE 14 + Ch3 SLIDE 31（Apex 需 3 次重抛光说明抛光不达标是真实且频发的）。
2. 【Metering 与 Containment 必须建立独立物料编码，禁止合并为"腔体刀片"】 本报告推导：两刀片功能相反、位置不同但外形相近，是典型的错装/错购高风险对。⚠️ 原文未给出两者的判别方法（[未找到原句]），因此必须在设备交付时向 OEM 索取带位置标注的爆炸图并固化为内部编码规则。这是本连接点中最紧迫、成本最低的一条行动。
3. 【向供应商索取的刮刀腔数据包（清单化）】 本报告推导：鉴于 Ch1 与全四章均未给出刀片参数，以下必须在设备选型阶段向 OEM 书面索取，不得默认：
   | 需索取项 | 原文状态 |
   |---|---|
   | 刀片材质（钢 / 碳钢 / 涂层 / 塑料） | [未找到原句] |
   | 刀片厚度、刃口角度、安装角度 | [未找到原句] |
   | 刀片加载方式（气压 / 弹簧 / 液压）与设定值 | [未找到原句] |
   | 腔体工作压力与密封压差 | [未找到原句] |
   | 预期刀片寿命（小时 / 万米）与失效判据 | [未找到原句] |
   | Metering 与 Containment 的位置判别图 | [未找到原句] |
   | 换刀工时与是否需停机 | [未找到原句] |
4. 【把"抛光一次通过率"设为供应商准入的独立 KPI】 本报告推导：依据链 Ch2 SLIDE 14（抛光不足 ⇒ 刀片过度磨损）→ Ch3 SLIDE 31（Apex 3 次重抛光）→ Ch2 SLIDE 20（KC 的大未雕刻区使抛光更复杂）。供应商审核中，抛光产能、抛光工艺能力与一次通过率应与雕刻能力并列评分。⚠️ 只看激光机台数量会系统性误判供应商。
5. 【备件库存策略：按"腔体必然存在"做全产线覆盖】 本报告推导：腔体在 3/3 构型中出现（SLIDE 6/7/8），且 Ch3 SLIDE 23 notes 称 "Tissue machine can't run without 2 functional gravure rolls"。因此刮刀腔耗材（两刀片 + 密封件）应按"产线级刚性备件"管理，对每条 gravure 产线建立最低安全库存 + 双源。⚠️ 刀片寿命本身 [未找到原句]，库存水位须以实际消耗数据标定，不得引用行业经验值。
6. 【验收量具必须与供应商一致，否则数据不可比】 本报告推导：Ch4 SLIDE 37 列出三种量具（Capatch strips / Impression strips / 3DQC），而 Ch4 SLIDE 34 notes 记录了惨痛教训："Did not measure volume with same tools so none of the data translated"。因此合同中必须写明验收量具型号与方法，并把它作为辊与刀片共同的验收基准。⚠️ 未锁定量具 = 验收数据无意义。
7. 【涂布量的责任划分必须在合同中写死】 本报告推导：本材料显示涂布量由网穴容积设定（Ch2 SLIDE 18：volume = 单位面积全部网穴容积），而刀片的作用是刮除网穴外的液体以实现该容积（此划分为 [本报告推导]，原文未陈）。由于Ch1 与全四章均未给出刀片对涂布量的定量影响（[未找到原句]），一旦出现涂布量偏差，责任归属将无据可依。建议合同中明确：涂布量超差时，先以 Capatch/3DQC 复测辊容积；容积合格则责任在腔体/刀片侧，容积超差则责任在辊侧。

### 模块 5 附：可直接用于决策的数据清单表（Ready-to-Use Data Sheet）

||||||
|---|---|---|---|---|
|1|Gravure 涂布的三项定义性能力|precise amount / Consistent coating weights / Suitable for high-speed|✅|SLIDE 2, SLIDE 5|
|2|涂布形式二分及资产映射|Direct = DRC, OLU；Indirect = Facial, Embossing winders (ELC)|✅|SLIDE 5, SLIDE 7, SLIDE 8|
|3|刮刀腔在全部构型中的覆盖率|3/3（100%）|✅|SLIDE 6/7/8 — 图像内容补充|
|4|刮刀腔部件数|3（Metering Blade / roll / Containment Blade）|✅|SLIDE 9 — 图像内容补充|
|5|护肤乳液涂布先例（量级 + 图案）|2 BCM / 6 BCM + dead bands；Indirect；Chrome|✅（需跨线标定）|Ch2 SLIDE 10 notes|
|6|体积→膜厚换算|1 BCM/in² = 1.55 cm³/m² ⇒ 1 BCM ≈ 1.55 µm|✅|Ch2 SLIDE 18 + [本报告推导]|
|7|KC 实测体积量级（Direct 参照）|OLU VIVA 27.6 BCM；OLU VENUS 3,800,000 μm³ ± 5%|✅|Ch3 SLIDE 28/32 — 图像内容补充|
|8|属性→细胞维度映射|X/Y 覆盖 ⇒ cell diameter；Z 向渗透 ⇒ cell depth|✅|Ch4 SLIDE 35|
|9|雕刻平台归属|OLU/DRC/ELCs = Ceramic；Facial = Chrome|✅|Ch2 SLIDE 10/11|
|10|供应商池|4 家（Harper / Precision Roll Solutions-IR Engraving / Pamarco / Apex）|✅|Ch3 SLIDE 22 — 图像内容补充|
|11|首件周期参照|Harper 首件 9 个月|✅|Ch3 SLIDE 34 notes|
|12|产线刚性|*"Tissue machine can't run without 2 functional gravure rolls"*|✅|Ch3 SLIDE 23 notes|
|13|雕刻规格自由度约束|*"Can only specify 2 from the key engraving parameters of volume, depth, and diameter"*|✅|Ch4 SLIDE 36|
|14|验收量具|Capatch strips / Impression strips / 3DQC|✅|Ch4 SLIDE 37|
|—|以下全部缺失，须实测或向供应商索取||||
|15|线速度（m/min 或 fpm）|❌|[未找到原句]|全四章|
|16|涂层厚度 / 涂布量（g/m²）数值（Ch1 内）|❌|[未找到原句]|Ch1|
|17|基材强度要求|❌|[未找到原句]|全四章|
|18|刀片角度 / 厚度 / 压力 / 材质|❌|[未找到原句]|全四章|
|19|刀片寿命 / 更换周期|❌|[未找到原句]|全四章|
|20|转移效率（Indirect 两次转移）|❌|[未找到原句]|全四章|
|21|辊径 / 包胶硬度 / 压区负荷 / 包角|❌|[未找到原句]|全四章|
|22|涂液粘度 / 固含 / 表面张力|❌|[未找到原句]|全四章|
|23|卫材（纸尿裤/湿巾）相关任何内容|❌|[未找到原句]|全四章|
|24|抗菌剂 / 导流层 / 亲水处理|❌|[未找到原句]|全四章|
|25|OLU / DRC / ELC / OLP 缩写全文|❌|[未找到原句]|全四章|


## 模块 6：金句索引（Key Quotes Index）



本模块共 12 条（Q1–Q11 出自本章 Ch1；Q12 为跨章锚点）。每条含：英文原文 + SLIDE N + 中文翻译 + 为什么记。

Q1
> "Engraved roll that delivers a precise amount of fluid to a substrate"
SLIDE 2
- 中文翻译：一种雕刻辊，用于向基材输送精确计量的流体。
- 为什么记：全章唯一的凹版辊定义，也是整个 38 页材料的总纲。三个关键词（Engraved / precise amount / substrate）分别对应后续三章：Engraved → Ch2 的雕刻方法与规格；precise amount → Ch2 的 BCM 计量体系 + Ch4 的直径/深度取舍；substrate → Ch1 的 Direct/Indirect 路径。任何关于凹版辊的讨论都应能回溯到这三个词。

Q2
> "Considered the 'Heart' of printing/coating process"
SLIDE 2
- 中文翻译：被视为印刷/涂布工艺的"心脏"。
- 为什么记：这是 KC 对凹版辊的战略定位，也是成本决策的正当性来源。它解释了三件事：① 为什么 KC 能为陶瓷辊接受 *"Higher cost"*（Ch2 SLIDE 11）；② 为什么雕刻辊是产线级瓶颈（"Tissue machine can't run without 2 functional gravure rolls"*，Ch3 SLIDE 23 notes）；③ 为什么值得投入 10 道工序去制造一根辊（Ch2 SLIDE 12`）。做 TCO 或供应商谈判时，这句话是对方定价逻辑的锚点。

Q3
> "Gravure roll and anilox roll – pretty much the same thing. Gravure roll has an industry connotation of direct to substrate and patterned. Anilox roll is more indirect and common/simple engraving"
SLIDE 2 — SPEAKER NOTES
- 中文翻译：凹版辊与网纹辊——几乎是同一样东西。凹版辊在行业内带有"直接接触基材且带图案"的含义；网纹辊则更偏"间接"且为"常见/简单雕刻"。
- 为什么记：⭐ 本拆解最重要的一条。 它是唯一一次对 gravure/anilox 作出区分的尝试，而它同时自我否定（*"pretty much the same thing"*）。更关键的是，本章自己的图违反了它 3 次（SLIDE 7/8 把 Indirect 路的辊叫 Gravure Roll；SLIDE 9 把同类辊叫 Anilox Roll），且 Ch2 SLIDE 13 notes 记录 "Anilox vs Gravure and Apex Owner Discussion this week" —— KC 内部当时尚未解决这个术语问题。记住它，是为了在写规格书、询价单、备件编码时，永远不用这两个名词去定义零件。

Q4
> "Enhanced properties create Premium products / Enable product differentiation / Create consumer value and drive growth / Higher margins"
SLIDE 4
- 中文翻译：增强的产品性能造就高端产品 / 实现产品差异化 / 创造消费者价值并驱动增长 / 更高的利润率。
- 为什么记：KC 对凹版技术的全部四条商业论证，且四条全是价值获取，没有一条是降本。这决定了凹版项目的评审口径：它应当以溢价能力、差异化、毛利率立项，而非以单机成本节约立项。同时它与 Ch2 SLIDE 20 的 "Not just printing/coating …. Creating product properties" 构成业务层与工艺层的同义反复——同一命题讲了两次，说明这是 KC 的核心信念。

Q5
> "Process that uses a gravure roll to apply a thin, uniform liquid film to a moving substrate"
SLIDE 5
- 中文翻译：一种使用凹版辊将薄而均匀的液膜施加到运行中的基材上的工艺。
- 为什么记：凹版涂布的正式定义，给出了三个判定条件（凹版辊 / 薄且均匀 / 连续运行基材）。⚠️ 同时要记住它的三个词没有数值："thin" 无量纲、"uniform" 无公差、"moving" 无速度。任何人引用这句话来支撑"凹版可做 X µm"都是过度解读。

Q6
> "Consistent coating weights / Suitable for high-speed processes"
SLIDE 5
- 中文翻译：涂布量一致性好 / 适用于高速工艺。
- 为什么记：这是凹版涂布仅有的两条性能主张，也是它区别于其他涂布方式的竞争基础。对卫材业务的直接意义："定量"与"高速"正是护肤乳液、抗菌剂等功能性涂层最需要的两个属性。⚠️ 但同样无任何数值 —— "high-speed" 在本材料中从未被量化**，[未找到原句]`。引用时必须向设备商取证具体速度**。

Q7
> "Direct = gravure roll to substrate …… DRC and OLU / Indirect = gravure roll to applicator roll to substrate…. Facial and  Embossing winders"
SLIDE 5
- 中文翻译：直接式 = 凹版辊 → 基材……应用于 DRC 与 OLU；间接式 = 凹版辊 → 涂布辊 → 基材……应用于 Facial 与压花复卷机。
- 为什么记：⭐ 全章的组织主轴，也是整份材料最重要的分类学句子。 它一次性完成了三件事：① 定义了 Direct/Indirect 的判据（路径跳数）；② 把分类映射到真实产线；③ 使后面三页（6/7/8）成为它的实例展开。⚠️ 同时必须记住它的边界：它只定义路径，不定义硬件数量（Facial OLP 的 Indirect 链路只有 4 个单元，比 Direct 还简单），也不决定雕刻平台（ELC 是 Indirect 却用陶瓷）。

Q8
> "2 Ply Winder ELC = Indirect Gravure Coating"
SLIDE 7
- 中文翻译：二层和纸复卷机 ELC = 间接凹版涂布。
- 为什么记：这句话是术语不稳定性的一号证据——它在一个 Indirect 工艺中把辊称为 Gravure Roll，直接违反 SLIDE 2 notes 的"gravure = direct"内涵。同时它给出了全章最复杂的辊系（8 工位），是理解"间接涂布 ≠ 一种固定机器"的关键反例。⚠️ 另记："2 Ply" 意味着这条线与多层复合**相关，是卫材（多层结构）唯一可能直接类比的产线形态。

Q9
> "Facial OLP = Indirect Gravure Coating"
SLIDE 8
- 中文翻译：Facial OLP = 间接凹版涂布。
- 为什么记：与 Q8 并列，构成 Indirect 的第二个、且结构完全不同的实例（DOCTOR CHAMBER → GRAVURE ROLL → RUBBER ROLL → WEB，仅 4 单元）。它证明了"Indirect"是一个路径概念，不是一个机器概念——同样是间接涂布，ELC 有 8 个工位，Facial OLP 只有 4 个单元。⚠️ 做设备选型或备件规划时，必须落实到产线，不能只说"我们要间接式"。 另记：Facial 正是护肤乳液涂布所在线（Ch2 SLIDE 10 notes 的 Jenks Facial Lotion GR），这条线对卫材护肤乳液迁移的参考价值最高。

Q10
> "Doctor Blade Chamber 部件标注：Metering Blade（计量刮刀）、Anilox Roll、Containment Blade（密封刮刀）"
SLIDE 9 — 图像内容补充
- 中文翻译：刮刀腔部件标注：计量刮刀、网纹辊、密封刮刀。
- 为什么记：⭐ 刮刀腔唯一的结构信息来源，也是本材料唯一一次出现 "Anilox Roll" 这个词。 三点必记：① 腔体是三部件子组件，不是单一零件 → 备件编码必须拆到部件级；② Metering 与 Containment 是两把功能相反的刀，外形相近，错装风险高；③ 它把辊称为 Anilox Roll，而 SLIDE 7/8 把同类辊称为 Gravure Roll —— 同一章内两个名字指同一个零件，这是术语风险的铁证。⚠️ 另记：Ch1 对这两把刀没有任何参数说明（角度/厚度/压力/材质/寿命全部 [未找到原句]）。

Q11
> *"Ordinary to Extraordinary"*（配图：普通冰淇淋圣代 → 辊体加工/镀层工业照 → 精致巧克力圣代）
SLIDE 3 — 图像内容补充
- 中文翻译：从平凡到非凡。
- 为什么记：全章唯一的纯图像页，也是唯一表达"转化"这一叙事的页面。它位于技术定义（SLIDE 2）与商业论证（SLIDE 4）之间，承担的是叙事桥梁：凹版辊就是把普通基材变成高端产品的那个"转化器"。⚠️ 记它有两个实用理由：① 它是理解 KC 内部如何讲述这项技术的最好样本（做内部分享时可直接借用这个框架）；② 它提醒我们 Ch1 有一整页是没有文字的——任何基于本页的引用都只能是图像证据，不能伪装成原文陈述。

Q12（🔗 跨章锚点金句，出自 Ch3，非本章）
> "Tissue machine can't run without 2 functional gravure rolls"
Ch3 SLIDE 23 — SPEAKER NOTES
- 中文翻译：纸机少了 2 根可用的凹版辊就无法运行。
- 为什么记：⭐ 整份材料中商业分量最重的一句话，也是把 Ch1 的概念（*"Heart"*）翻译成采购条款的那句话。它给出三个可直接落地的数字与结论：① "2 根" = 最低功能配置 → 备辊库存的下限；② "can't run" = 停机代价由整条产线承担 → 雕刻辊是产线级刚性瓶颈件，不是普通备件；③ 因此双源 + 安全库存不是优化项，是必要条件。配合 Ch3 SLIDE 34 notes（Harper 首件 9 个月）与 Ch3 SLIDE 22（供应商池仅 4 家），可直接推导出新供应商导入的完整商务模型。⚠️ 注意：这句话的语境是 tissue machine（生活用纸纸机），不是卫材产线——外推到卫材时必须重新验证。


## 附录：本报告的关键 [未找到原句] 汇总与风险提示



说明：本节是本次拆解的诚实性清单。Ch1 是一章定性概念定义页，数据密度极低。以下 26 项在 Ch1（以及在标注"全四章"时的整个材料）中均无原文支撑，报告中未以任何形式编造填充。

### A. Ch1 缺失（幻灯片 1–9 内无任何支撑）

||||
|---|---|---|
|1|涂布量 / 涂层厚度的任何数值|无法设定 gravure 的定量能力边界；须由 Ch2 的 BCM 体系间接推导|
|2|线速度的任何数值|"high-speed" 无法量化；卫材产线速度匹配无法评估|
|3|涂液粘度 / 固含 / 表面张力|涂料适配性无法判断|
|4|凹版辊的直径、面宽、材质|设备规格无从确认（Ch3 SLIDE 28 的 112" / 20" 仅为 OLU VIVA 单辊）|
|5|网穴容积 / LPI / 网穴几何|Ch1 完全未涉及（属 Ch2）|
|6|Metering Blade 的功能说明|只能按名称推断|
|7|Containment Blade 的功能说明|同上|
|8|刀片角度 / 厚度 / 压力 / 材质|备件规格无法编写|
|9|刀片寿命 / 更换周期 / 磨损率|备件库存水位无法计算|
|10|Metering 与 Containment 的位置判别方法|⚠️ 错装风险无法用文件规避|
|11|腔体工作压力 / 密封压差|无法设定工艺窗口|
|12|Backing Roll 的功能说明|只能按名称推断|
|13|Backing Roll 的直径 / 包胶 / 硬度|备件规格缺失|
|14|Applicator Roll 的材质 / 硬度 / 直径|同上|
|15|Applicator Roll 的转移效率|⚠️ Indirect 路线的涂布量无法理论计算，必须实测|
|16|Marrying Roll 的功能说明|只能按名称推断|
|17|Embossing Roll 的图案 / 深度 / 压区负荷|压花参数完全缺失|
|18|Calendar Roll 的直径 / 硬度 / 压区负荷 / 温度|压光参数完全缺失|
|19|ELC 8 个工位的任何量化参数|辊系无法规格化|
|20|"Embossing winders" 与 "ELC" 的关系|分类学上 ELC 是否属于 embossing winders 未决|
|21|OLU / DRC / ELC / OLP 的缩写全文|⚠️ 不得猜测展开|
|22|SKU → 产线 → 涂布形式 的映射|SLIDE 4 的四个产品全部无技术归属（Cottonelle Luxe 与 Scott Shop Original 甚至在全四章中零证据）|
|23|Direct vs Indirect 在速度 / 厚度 / 基材强度上的比较|⚠️ 任务要求的三个判据，Ch1 一个都没给出|
|24|涂布形式与雕刻平台的因果说明|只可证归属，不可证原因|
|25|"为什么 Direct 必须用陶瓷"|⚠️ 全材料无此因果陈述|
|26|刮刀腔对涂布量的定量影响|涂布量超差时的责任划分无据可依|


### B. 全四章均缺失（对本报告业务模块有直接影响）

||||
|---|---|---|
|27|卫材（纸尿裤 / 湿巾）的任何内容|⚠️ 所有 KC 案例均为生活用纸；卫材迁移的基材差异是阻断性缺口|
|28|抗菌剂涂布|无任何证据，不可据本材料论证|
|29|导流层 / 亲水剂 / 表面活性剂处理|无任何证据，且存在"离散网穴 vs 全幅连续膜"的原理性张力|
|30|GMT 等指标的定义|Ch4 SLIDE 29/30 出现 *"1100 GMT vs 1800 OLU GMT Target"*，但本材料从未定义 GMT → 不得解释该数值含义|


### C. 源数据一致性风险（需在后续核验）

||||
|---|---|---|
|R1|DRC 工艺流程有两种记录顺序，且任务版本含 "Latex Print (Side 2)" 而提取文件无此单元标注|🔴 回访原始幻灯片第 23 页渲染图复核，尤其确认是否存在 "Latex Print (Side 2)" 工位|
|R2|gravure / anilox 术语在本材料内不稳定（7 条证据，5 条直接冲突）|内部文件中统一以 "gravure/anilox roll (engraved metering roll)" 表述，并以 产线 + 参数集 作为唯一识别键|
|R3|Backing Roll 命名跨章不一致（Ch1 SLIDE 6 = "Backing Roll"；Ch3 SLIDE 26 = "Printer Backing Roll" + 独立 "Pressure Roll"）|备件编码按 产线 + 位置 建立，不依赖名称|
|R4|本报告大量结论依赖 图像内容补充（Ch1 的 9 页中有 4 页为纯图像或图像承载关键信息：SLIDE 3/6/7/8/9）|关键结论（尤其 ELC 8 工位顺序、刮刀腔三部件、Direct 构型）建议二次读图复核|




报告结束 ｜ 全部 6 个模块已覆盖 ｜ 证据标注规则：SLIDE N（文本层）／ SLIDE N — SPEAKER NOTES（演讲者备注）／ SLIDE N — 图像内容补充（渲染图提取）／ 本报告推导（本报告推导，附依据）／ [未找到原句]（原文无支撑，不编造）／ 跨章引用（引自 Ch2/Ch3/Ch4，已标注原幻灯片号）


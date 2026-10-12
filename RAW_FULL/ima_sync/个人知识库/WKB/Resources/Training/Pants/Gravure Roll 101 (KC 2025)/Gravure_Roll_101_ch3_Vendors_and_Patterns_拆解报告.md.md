---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_62063e6f59e5fad794814fc68f03a9d7001a693ee6c0644e"
source_file: "Gravure_Roll_101_ch3_Vendors_and_Patterns_拆解报告.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch3_Vendors_and_Patterns_拆解报告.md.md"
extracted: "2026-09-30"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
---

# Gravure_Roll_101_ch3_Vendors_and_Patterns_拆解报告.md


章节：Ch3 Vendors & Patterns ｜ 覆盖幻灯片：22–28 ｜ 文档：Gravure Roll 101 (KC, Capability Days 2025) ｜ 拆解日期：2026-08-30

# Gravure Roll 101 — Ch3 Vendors & Patterns：学术级章节拆解报告

Source integrity rules applied in this report（本报告遵循的学术诚信规则）
- 每条论断均标注证据来源：SLIDE N（幻灯片文本层）、SLIDE N — SPEAKER NOTES（演讲者备注）、SLIDE N — 图像内容补充（预先从渲染图提取的关键数据）、SLIDE N — 二次读图（本报告直接读取 PPTX 内嵌原图所得）、SLIDE N — 文本层（SmartArt）（本报告从 PPTX 的 ppt/diagrams/data*.xml 中恢复的 SmartArt 文本）。
- 章节内找不到支撑原句的统一标注 [未找到原句]，且不因此编造任何数据。
- 任何由本报告计算得出的数字，统一标注 [本报告推导] 并完整列出算式。
- 非本章内容（Ch1/Ch2/Ch4）引用时显式标注章节归属；一般工程背景显式标注 外部背景，非本章内容。
- 当不同证据源对同一字段给出互相冲突的数值时，本报告并列呈现全部读数并标注 ⚠️，不做单方面取舍。

## ⚠️ 来源校订说明（Read this first — 与既有提取相比的三处重要校正）

本报告在既有章节文件之外，直接读取了 Gravure Roll 101.pptx 内嵌的原始图片与 XML，得到三项既有提取未覆盖或被误读的证据。所有引用均已标注来源类型：

||||
|---|---|---|
|1|SLIDE 22 的「Key Vendors」实为 SmartArt 图形，其文本不在普通形状文本层中，故既有章节文本层为空。真实文本为：Harper - Charlotte, NC / Precision Roll Solutions/IR Engraving - Richmond, VA / Pamarco - Atlanta, GA / Apex - Pittsburgh, PA|SLIDE 22 — 文本层（SmartArt, ppt/diagrams/data2.xml）|证实了 SLIDE 22 — 图像内容补充 的四家名单，且给出了精确拼写（IR Engraving 与 Precision Roll Solutions 为同一实体的两个名称，原文写作 Precision Roll Solutions/IR Engraving）|
|2|SLIDE 28 图纸的 Deep Dot 尺寸、公差与全部点阵尺寸标注：既有 图像内容补充 记为 0.032" × 0.022" ±10%；本报告二次读图（对原图分块 ×2/×3 放大、四个象限独立读取、两次独立复核）一致读得 0.025" × 0.0227" ±5%（635 × 577 μm ±5%，公差区间 0.0237–0.0262" × 0.0216–0.0238"）|SLIDE 28 — 二次读图 vs SLIDE 28 — 图像内容补充|⚠️ 两组读数并列呈现，标注为待澄清。二次读图的数值内部自洽（公差区间与 ±5% 精确吻合、公制换算精确吻合），故本报告倾向于二次读图，但不单方面否定既有提取|
|3|SLIDE 28 图纸的 Shallow Dot 完整规格（既有提取完全缺失）：0.020" × 0.020" ±5%、10,200,000 cubic micrometers (10.2bcm)、上下限与 Test Burn Target、以及 0.033127" / 0.066254" / 0.265015" / 0.148148" 四个点阵尺寸标注、*Always tilt to the right unless requested otherwise.|SLIDE 28 — 二次读图|补充。这是判定「bcm」口径 1000× 矛盾的关键新证据（见 T7）|
|4|SLIDE 27 实为内嵌视频（ppt/media/media1.mp4，5.93 s，1350×1080，含音轨），非图片。逐帧读取后确认：画面为一条在产的 OLU 涂布/印刷工位（上方蓝色背压辊 + 下方深色凹版辊 + 穿过压区的幅材 + 大量干涸乳胶残留），全片无可辨识文字|SLIDE 27 — 二次读图（9 帧逐帧）|既有提取标注 [images: 0]，本报告确认该页介质为视频而非图片，且无文字层|


关于任务书中若干字段的说明（诚信标注）：任务书列举的 HARPERLASER 112x20、128x20、0.070" deep dots spacing、光面 3.050 与 3.0364、0.250" border、独立的 LOCATION 栏、以及「过去几年做过的辊」六条清单、「KC 各厂雕刻商分布表」、"Pictured below is the newest VIVA roll for Beech Island made by Harper" 等字段，经全 deck 全文检索（含文本层、SmartArt XML、全部 38 页图像、内嵌视频逐帧）确认：均不存在于本源材料，相关单元格一律标注 [未找到原句]，并在附录中集中列示。

## 模块 1：核心论点（Core Arguments）

### A1. KC's engraving supply base is four named North-American vendors — and one of the four is already compromised on measurement compatibility



English summary：Ch3 opens the "who can actually make these rolls" question with an explicit list of only four key vendors — Harper (Charlotte, NC), Precision Roll Solutions / IR Engraving (Richmond, VA), Pamarco (Atlanta, GA), Apex (Pittsburgh, PA). The list is not a market overview; it is the entire qualified supply base. Within this closed set, one member (IR Engraving) is later documented as metrologically incompatible with KC (Ch4 SLIDE 34), which mathematically reduces the usable base to three for new-pattern work.

||||
|---|---|---|
|Harper|Charlotte, NC|SLIDE 22 — 文本层（SmartArt）：*"Harper - Charlotte, NC"；SLIDE 22 — 图像内容补充："Harper – Charlotte, NC"*|
|Precision Roll Solutions / IR Engraving|Richmond, VA|SLIDE 22 — 文本层（SmartArt）："Precision Roll Solutions/IR Engraving - Richmond, VA"|
|Pamarco|Atlanta, GA|SLIDE 22 — 文本层（SmartArt）："Pamarco - Atlanta, GA"|
|Apex|Pittsburgh, PA|SLIDE 22 — 文本层（SmartArt）："Apex - Pittsburgh, PA"|


- 支撑依据 1：Ch4 SLIDE 34 — SPEAKER NOTES："Switched to IR Engraving because Jenks had used them for 2 VIVA rolls / Did not measure volume with same tools so none of the data translated" —— 供应商数量（4）与可用供应商数量（3）不是同一个数字。
- 支撑依据 2：Ch4 SLIDE 38 — 文本层（SmartArt, data3.xml）："New vendors are learning with KC as we attempt to get back to healthy gravure roll inventories and look to ignite innovation" —— 说明这 4 家并非成熟稳定供应，而是「正在与 KC 一起学习」。
- 支撑依据 3（[本报告推导]）：Ch3 内部即出现第 5 个雕刻方名称 —— SLIDE 25 的 *"Saueressig – KCP06"*，但它不在 SLIDE 22 的四家名单中。即：「有图案实绩的雕刻方」≥ 5 家，「Key Vendors」= 4 家，两者口径不同，须区分。
### A2. A "pattern" is not artwork on the roll — it is a measurable latex-placement geometry verified by destructive staining



English summary：Ch3 defines a gravure pattern by what it deposits and where, verified chemically: the DRC pattern is documented as a "#1 Printer pattern (VIVA® Towel)" whose physical result is read on a "Stained sample (DuPont Stain #4)" where "Red dots = latex" and "Green = fiber". The pattern is therefore an operational object with three coupled layers: (i) engraved cell geometry on the roll, (ii) transferred latex dots on the sheet, (iii) a stain-based read-out that makes (ii) visible.

- SLIDE 24 — 图像内容补充：*"#1 Printer pattern (VIVA® Towel)，Stained sample (DuPont Stain #4)，Red dots = latex，Green = fiber，尺寸标注 .047"、133°、.1884""*
- SLIDE 24 — 二次读图：尺寸标注精确读得 .0471"（垂直）、.1884"（垂直）、.133°（带角度符号，既有提取记为 133°）
- 支撑依据：Ch4 SLIDE 29 / SLIDE 30 把同一手法用作试车判据（*"Pamarco VIVA Trial #1 DuPont Stain Results"、"Apex VIVA Trial #1 DuPont Stain Results"*，均在 40X Zoom 下与 IR Engraving 的对照辊并排）。即 SLIDE 24 的判据方法在 Ch4 被直接复用为供应商验收方法 —— 图案定义与验收方法在本章是同一套东西。
- 量化推论 [本报告推导]：.1884" ÷ .0471" = 4.000 —— 图案的纵向重复节距恰为单元尺寸的 4 倍，即该 DRC 图案是一个 4×1 的规则阵列（与 SLIDE 28 图纸中 0.148148" = 0.033127" × √20 = 0.033127" × √(4²+2²) 所揭示的「4×2 矢量重复」同构，见 C9）。
### A3. The DRC and OLU process chains are structurally different, which is why one pattern cannot be copied across platforms



English summary：Ch3 documents two distinct process architectures: Marinette DRC (SLIDE 23) is a double-recrepe line with two latex print stations and two recrepe dryers; Jenks & BIL OLU (SLIDE 26) is a print-then-crepe line with a single printer station feeding a single crepe dryer. DRC prints both sides (SLIDE 24 — 二次读图："Engraving to be used on both sides"); OLU prints one side before creping.

|||||
|---|---|---|---|
|成形|Vertical Run → Former → Felt Section → 3-layer H-box 流浆箱 → Yankee Dryer|（图外，未画出）|SLIDE 23 — 图像内容补充|
|印刷站|2 站：Latex Print (Side 1) → After Dryer … （Double ReCrepe = 两次起皱 + 两面乳胶印刷）|1 站：Unwind → Printer（Backing Roll / Gravure Roll / Air Layer / Print Fluid Delivery / Print Fluid Make-up System）|SLIDE 23 / SLIDE 26 — 图像内容补充|
|干燥|Recrepe Dryer #1 → Recrepe Dryer #2 → Latex Cure → Cool → Reel|Heated Hood → Crepe Dryer → Crepe Blade → Reel → Converting Line|SLIDE 23 / SLIDE 26 — 图像内容补充|
|压区辊系|—|Backing Roll（绿）／Gravure Roll（蓝）／Pressure Roll|SLIDE 26 — 图像内容补充、SLIDE 26 — 二次读图|
|图案供应商|Harper 90x60 / IR Engraving 90x60 / Saueressig KCP06 / Pamarco KCP08 / APEX KCP09|VIVA（27 dpi，SLIDE 28）、VENUS（34.5 DPI，Ch4 SLIDE 32）|SLIDE 25、SLIDE 28、Ch4 SLIDE 32|


- 支撑依据：SLIDE 23 — SPEAKER NOTES："Incredibly complex process. Tissue machine can't run without 2 functional gravure rolls" —— DRC 需要 2 根可用辊才能开机，而 OLU 线（SLIDE 26）图上只有 1 个 Printer 站。这解释了为什么「辊库存健康度」是 Ch4 的战略议题。
- 操作化推论 [本报告推导]：DRC 的图案必须两面成对设计（*"Engraving to be used on both sides"*），OLU 的图案只需单面；因此 DRC 图案不可直接移植到 OLU，反之亦然，任何跨平台的图案复用都必须重做工艺验证。
### A4. The VIVA roll drawing is a complete, self-contained specification object — roughly 25 fields, of which volume is only one



English summary：SLIDE 28 shows a full Harper manufacturing drawing that specifies the roll across six independent field groups: (1) identity/custody, (2) mechanical envelope, (3) engraved-area geometry, (4) cell structure (dpi / spacing ratio / rotation), (5) per-tier cell dimensions and per-tier volumes with asymmetric tolerances, (6) a polishing target written as a volume, plus a process note. The chapter's implicit claim is that "the spec" is a system of ~25 coupled numbers, not a BCM value.

- SLIDE 28 — 图像内容补充 + SLIDE 28 — 二次读图（详见 T1）
- 支撑依据 1（跨章呼应）：Ch2 SLIDE 16：*"Standard Engraving Specifications — Cell geometry, lines per inch, cell volume"*；Ch2 SLIDE 21 — 图像内容补充：*紫框 Cell dimensions（Cell diameter / Cell depth / Cell volume）；绿框 Pattern details（Shapes, sizes, spacing）*。SLIDE 28 的图纸正是这七个参数类别的一次完整实例化：Cell diameter（0.025" × 0.0227"）／Cell depth（隐含于体积比）／Cell volume（27,600,000 μm³）／Shapes（dot）／sizes（0.020"、0.025"）／spacing（2:1，0.033127"）／+ 角度（19.6°）。
- 支撑依据 2（[本报告推导]）：图纸上有两级网点（shallow / deep），且两级的公差带方向相反：Shallow 为 −0% / +10%（只许偏大），Deep 为 ±5%（双向）。这是本章最精细的一处工程信息 —— 它意味着浅点与深点在抛光工序中的容忍方向不同（见 C10 与 T8）。
### A5. Vendor capability differences are visible at the cell level, and they are the direct upstream cause of trial outcomes



English summary：Ch3 does not merely list vendors — it shows their cells. SLIDE 25 places five engravings side by side and marks three red defect circles on the IR Engraving panel only; SLIDE 28 shows that a conforming VIVA roll is a Harper artifact. The chapter's claim is that vendor = a distribution of cell quality, and Ch4 converts that distribution into GMT numbers.

|||||
|---|---|---|---|
|Harper|Harper 90x60 Marinette Engraving；VIVA OLU 辊（KC GR#5）|未见缺陷圈|SLIDE 25 — 二次读图、SLIDE 28|
|IR Engraving|IR Engraving 90x60 Marinette Engraving|3 个红圈缺陷标记（本章唯一的缺陷标记）|SLIDE 25 — 二次读图、SLIDE 25 — 图像内容补充|
|Pamarco|Pamarco – KCP08|未见缺陷圈|SLIDE 25 — 二次读图|
|APEX|APEX – KCP09|未见缺陷圈|SLIDE 25 — 二次读图|
|Saueressig|Saueressig – KCP06（大图，六边形蜂窝）|未见缺陷圈（作为正面参照）|SLIDE 25 文本层 + SLIDE 25 — 二次读图|


- 支撑依据（下游兑现）：Ch4 SLIDE 34 — 图像内容补充：左 IR Engraving VENUS CT5 — *"Engraving – 1/3 of dot is still filled with ceramic 'shell'"*（红圈标缺陷）；右 Pamarco VENUS engraving CT9 — *"Dots are full circles and clean. No ceramic 'shell'."*。同为「红圈标缺陷」手法，Ch3 用在 IR Engraving 上，Ch4 再次用在 IR Engraving 上 —— 这是同一供应商在两个不同图案（Marinette 90x60 与 VENUS）上的一致性质量问题。
- 反向发现 [本报告推导]：雕刻质量排序 ≠ 试车结果排序。雕刻质量最好的 Pamarco（CT9 *"No ceramic 'shell'"*）在 VIVA Trial #1 的 GMT 为 1100（Ch4 SLIDE 29 notes），而 Apex 为 1550（Ch4 SLIDE 30 notes），目标均为 1800。即：微观雕刻最优者 GMT 最低（−38.9%），次优者反而更接近目标（−13.9%）。这说明「把网穴刻干净」不是「把产品性能做对」的充分条件（详见模块 4.2）。
## 模块 2：关键概念操作化定义（Key Concepts with Operational Definitions）



每个概念含：(a) 中文名 + English term｜(b) 英文定义（English definition）｜(c) 操作化定义（测量维度 / 判定式 / 量化指标）｜(d) 原文英文摘录 + SLIDE N。

### C1. Engineered Pattern ｜ 工程化图案（KC 定制雕刻图案）

- (b) English definition：A gravure pattern designed by KC to create product properties rather than to transfer a uniform film; it is explicitly not a standard anilox engraving and sits outside the engraving industry's normal process window.
- (c) 操作化定义：





- 判定式（4 选 3 即判为 Engineered）：① 出现在 DRC / OLU / Facial 三条产线之一；② 含 "Deep" engravings（深点雕刻）；③ 含 "Large" cells（大网穴）；④ 存在 large amount of unengraved area（大面积未雕刻区）。
- 量化指标（VIVA 实例）：深点 0.025" × 0.0227" ±5%（635 × 577 μm）；深点单穴容积 27,600,000 μm³ ±5%；点阵 27 dpi / 2:1 / 旋转 19.6°（SLIDE 28）。
- 过程指标："Not just printing/coating …. Creating product properties" —— 若图案的功能是产生性能（GMT、Z 向剥离、表面覆盖）而非均匀涂布，即为 Engineered。
- 责任判定式："KC has to be able to communicate the engraving specifications required to create product properties. Engravers have no insight beyond the cell dimensions" —— 规格翻译责任在 KC，不在雕刻商。
- (d) 原文：*"Unique KC Gravure rolls — This is where the MAGIC happens / Engineered patterns - DRC/OLU/Facial / Outside the engravers comfort zones / "Deep" engravings / "Large" cells / Large amount of unengraved area = more complex polishing / Not just printing/coating …. Creating product properties"* — Ch2 SLIDE 20；"KC has to be able to communicate the engraving specifications required to create product properties. Engravers have no insight beyond the cell dimensions" — Ch2 SLIDE 20 — SPEAKER NOTES。本章实例化："OLU – VIVA Gravure Roll Pattern" — SLIDE 28。
### C2. Decorative Pattern ｜ 装饰性图案

- (b) English definition：[未找到原句] — 本 deck（全部 38 页，含文本层、SmartArt XML、全部图像、内嵌视频逐帧）中不存在 "decorative" 一词，也不存在以「装饰性」为名的图案分类。
- (c) 操作化定义：



- 判定式：不可判定 / 不适用（N/A）。本源材料未提供任何区分「装饰性」与「功能性」图案的维度、参数或判据。
- 最接近的可操作替代 [本报告推导]：本章实际使用的分类轴是产品/产线（VIVA® Towel / DRC / OLU / Facial）与雕刻方图案代号（KCP06 / KCP08 / KCP09 / 90x60 Marinette），而不是「装饰 vs 功能」。
- 可迁移的判定式（借用 SLIDE 24 的染色法）：若一个图案的作用只是改变外观（红/绿染色图上不产生新增 latex 点、不改变点阵几何），方可归为装饰性；反之凡改变 Red dots = latex 分布者，一律归为 Engineered。该判定式为 [本报告推导]，源材料未如此表述。
- (d) 原文：[未找到原句]。可用的最接近原文为 "#1 Printer pattern (VIVA® Towel)" — SLIDE 24 — 图像内容补充。
### C3. Embossing（ELC / 2 Ply Winder）｜ 压花（压花复卷机，ELC）

- (b) English definition：In this deck, "embossing" names a converting platform (2 Ply Winder ELC) that uses gravure coating indirectly; its gravure application is explicitly "2 PLY bath/towel embossing" — i.e. embossing here is a product/process category that consumes gravure rolls, not a cell-geometry category.
- (c) 操作化定义：



- 判定式（工艺链位置）：Gravure Roll → Applicator Roll → substrate（Indirect）且产线为 Embossing winder / 2 Ply Winder ELC → 判为 Embossing 类应用。
- 辊系判定式（7 辊）：Upper Rubber Roll / Embossing Roll / Marrying Roll / Applicator Roll / Gravure Roll / Steel Calendar Roll / Rubber Calendar Roll（+ Embossing Cleaning System）。
- 量化指标：[未找到原句] —— 本章未给出 ELC 图案的 dpi / BCM 数值。跨章唯一数值参照为 Ch2 SLIDE 16 的 *"2 ply bath specification = 60 degree hex, 180 LPI, 6.0 BCM"*（该规格属 Ch2，非本章）。
- (d) 原文："Indirect = gravure roll to applicator roll to substrate…. Facial and Embossing winders" — Ch1 SLIDE 5；"2 Ply Winder ELC = Indirect Gravure Coating" — Ch1 SLIDE 7；"ELCs – 2 PLY bath/towel embossing" — Ch2 SLIDE 13 — SPEAKER NOTES。
### C4. Combining Patterns ｜ 组合图案（多图案/分区复合）

- (b) English definition：[未找到原句] — 本 deck 中不存在 "combining pattern(s)" 这一术语，也不存在对应的图案分类条目。
- (c) 操作化定义：







- 判定式：不可判定 / 不适用（N/A）。
- 最接近的可操作替代（有原文支撑）：本章与 Ch2/Ch4 实际记录了两种「在一根辊上组合多种雕刻」的做法，可直接作为替代判据：
- Banded roll（分段辊）：在同一辊面上并列不同雕刻，用于加速迭代。判定式：同一辊面存在 ≥2 个 BCM 分区。原文："Jenks Facial Lotion GR – alternating bands of 2 BCM and 6 BCM and some dead bands designed for areas where no transfer will take place" — Ch2 SLIDE 10 — SPEAKER NOTES；"Banded gravure rolls can help speed up the iterative process – typically don't produce sellable product – RSR not MSR" — Ch4 SLIDE 36。
- Two-tier dot pattern（深浅双级网点）：同一图案内同时存在 shallow dot 与 deep dot 两级（VIVA：0.020" 级 + 0.025" 级）。判定式：同一图案内 ≥2 个不同的单穴容积规格。原文见 C8 / C10。
- (d) 原文：[未找到原句]（术语本身）。替代条目原文见上。
### C5. Chrome engraving (Electro-mechanical Engraved Chrome Roll) vs Ceramic engraving (Laser Engraved Ceramic Roll) ｜ 镀铬机电雕刻 vs 陶瓷激光雕刻

- (b) English definition：KC runs two engraving platforms. Chrome = *Electro-mechanical Engraved Chrome Rolls (Facial)*；Ceramic = Laser Engraved Ceramic Rolls (OLU/DRC/ELCs). They are positioned as a five-axis managed trade-off, not as old-vs-new technology.
- (c) 操作化定义（五轴判定表，全部为原文 Pros/Cons 字段）：
||||
|---|---|---|
|Cost|lower cost|Higher cost|
|Engraving life|shorter engraving life|longer engraving life|
|Engraving flexibility|engraving limitations|more engraving flexibility|
|Transfer precision|variability due to plating inconsistency|more precise and consistent fluid transfer|
|Supply base|vendor options due to chrome 6|vendor competition|
|额外（材料/耐蚀）|[未找到原句]|More resistant to corrosion and abrasion|


- 平台判定式：产线 = Facial → Chrome；产线 ∈ {OLU, DRC, ELCs} → Ceramic。
- 本章落点判定式：Ch3 的 VIVA（OLU）与全部 DRC/OLU 图案 → 均为陶瓷激光雕刻平台；故 SLIDE 22 的四家供应商在本章语境下竞争的是陶瓷激光雕刻能力，SLIDE 28 图纸上的抛光注记（必须抛光）进一步佐证陶瓷平台（抛光是陶瓷激光雕刻的强制后工序，Ch2 SLIDE 14）。
- (d) 原文："Electro-mechanical Engraved Chrome Rolls (Facial) — Pros - lower cost / Cons - shorter engraving life, engraving limitations, variability due to plating inconsistency, vendor options due to chrome 6" — Ch2 SLIDE 10；"Laser Engraved Ceramic Rolls (OLU/DRC/ELCs) — Pros - More resistant to corrosion and abrasion, longer engraving life, more engraving flexibility, more precise and consistent fluid transfer, vendor competition / Cons - Higher cost" — Ch2 SLIDE 11；"Ceramic laser engraved rolls dominate the market" — Ch4 SLIDE 38 — 文本层（SmartArt）。
### C6. VIVA Signature Cloth (VSC) 27 dpi pattern ｜ VIVA Signature Cloth（VSC）27 dpi 图案

- (b) English definition：The OLU VIVA gravure pattern documented on SLIDE 28: a 27 dpi dot lattice with 2:1 dot spacing, rotated 19.6° from vertical, carrying two tiers of cells (shallow 0.020" / deep 0.025") at 10,200,000 μm³ and 27,600,000 μm³ respectively. The associated commercial product family is VIVA® (VIVA® Towel on SLIDE 24; Viva Signature Cloth appears as one of KC's four premium products in Ch1 SLIDE 4).
- (c) 操作化定义：







- 判定式（图案身份）：27 dpi dot ∧ 2:1 dot spacing ∧ Rotated 19.6° from vertical ∧ Deep Dot 27,600,000 μm³ ∧ Engraved Area 104.5" CENTERED on 112" face → 判为 OLU VIVA 图案。
- 量化指标全套：见 T1（约 25 个字段）。
- 点阵密度（[本报告推导]，两法互证）：
- 法一（由图纸标注反算）：1 ÷ (0.033127" × 0.066254") = 1 ÷ 0.00219480 in² = **455.65 dots/in²**
- 法二（由 dpi 与间距比正算）：27 dpi × (27 ÷ 2) = 27 × 13.5 = 364.5，× 1.25 = **455.6 dots/in²**（1.25 系数解释见 C9 / T8）
- 两法偏差：455.65 ÷ 455.625 − 1 = **+0.005%** → 高度自洽
- ⚠️ 术语校订 [本报告推导]：源材料从未把该 27 dpi 图案与 "VIVA Signature Cloth (VSC)" 直接关联。Viva Signature Cloth 仅作为产品照出现在 Ch1 SLIDE 4 — 图像内容补充；SLIDE 24 的染色样标注为 VIVA® Towel；SLIDE 28 标题为 OLU – VIVA Gravure Roll Pattern。故 "VSC = 27 dpi" 是本报告的合理推断（同属 VIVA 品牌 OLU 平台），但非原文直述，使用时须以「OLU VIVA 27 dpi 图案」为准。
- (d) 原文："OLU – VIVA Gravure Roll Pattern" — SLIDE 28；"27 dpi dot / 2:1 dot spacing / Rotated 19.6° from vertical" — SLIDE 28 — 图像内容补充 与 SLIDE 28 — 二次读图（两源一致）；"#1 Printer pattern (VIVA® Towel)" — SLIDE 24 — 图像内容补充；"p4 四大高端产品配图：Cottonelle Luxe、Kleenex soothing lotion、Viva Signature Cloth、Scott Shop Original" — Ch1 SLIDE 4 — 图像内容补充。
### C7. VENUS 34.5 dpi pattern ｜ VENUS 34.5 DPI 图案（跨章：Ch4 SLIDE 32）

- (b) English definition：The OLU VENUS pattern (Ch4 SLIDE 32, "OLU VENUS Pattern (Original Specs)"): 34.5 DPI / 1,488 DOTS/SQ-IN, Target 3,800,000 μm³ ±5%, Shallow Dot 0.02" = 0.508 mm, on a 112" face × 19.701" diameter roll with 104.5" centered engraved area.
- (c) 操作化定义：





- 判定式：34.5 DPI ∧ 1488 DOTS/SQ-IN ∧ Target 3,800,000 μm³ ±5% ∧ Shallow Dot 0.508 mm → 判为 OLU VENUS 图案（原始规格）。
- 点距一致性校验（[本报告推导]）：1 ÷ 34.5 dpi = 0.028985"；图纸标注水平点距 0.02926" → 偏差 0.02926 ÷ 0.028985 − 1 = **+0.95%** → DPI 与点距标注互洽（%）。
- 点阵密度校验（[本报告推导]）：1.25 × 34.5² = 1.25 × 1190.25 = **1487.8 ≈ 1488 DOTS/SQ-IN** → 与图纸直印值吻合（1.25 系数的同一解释见 C9）。
- 辊级容积（[本报告推导]）：1488 dots/in² × 3,800,000 μm³ ÷ 10⁹ = **5.654 BCM/in²**。
- ⚠️ 口径冲突：见 T7（与 Ch3 SLIDE 28 的 (27.6 bcm) 标签存在 1000× 量级矛盾）。
- (d) 原文："OLU VENUS Pattern (Original Specs)" — Ch4 SLIDE 32；"Pattern 34.5 DPI, 1488 DOTS/SQ-IN；Target Volume 3,800,000 μm³ ± 5%；Shallow Dot 0.02" = 0.508mm" — Ch4 SLIDE 32 — 图像内容补充（本报告二次读图复现一致）；"Engraved with 3 vendors and struggled with engraving consistency and quality until Pamarco came on line in Q3 2024" — Ch4 SLIDE 32 — SPEAKER NOTES。
### C8. BCM volume ｜ BCM 容积（Billion Cubic Microns per square inch）

- (b) English definition：*"Gravure Roll Volume — Total volume of all the engraved cells on the roll surface per unit area of the surface"；"USA = BCM/in² ……. More commonly just referred to as BCM"；"1 Billion Cubic Microns (Micrometers) — 1 BCM = 1,000,000,000 um³"*.
- (c) 操作化定义：







- 定义式：BCM/in² = Σ(单穴容积 μm³) per 1 in² ÷ 10⁹。
- 换算式：1 BCM/in² = 1.55 cm³/m²（原文）；1,000 μm = 1 mm（原文，用于体积量纲自检）。
- ⚠️ 本章暴露的口径分裂（[本报告推导]，核心发现）：
- Ch2 SLIDE 19 定义：1 BCM = 10⁹ μm³（每平方英寸的穴容积总和）
- Ch3 SLIDE 28 图纸用法：27,600,000 μm³ → 标签 "27.6 bcm"（= 单穴 μm³ ÷ 10⁶）；10,200,000 μm³ → 标签 "10.2 bcm"（同法）
- → 同一图纸内部的 (27.6 bcm) 标签相对 Ch2 SLIDE 19 定义偏大 1000 倍（27,600,000 ÷ 10⁹ = 0.0276 BCM/穴，而非 27.6）
- 校准判据（[本报告推导]，三方三角验证）：按点阵密度折算到辊级 BCM 后，VIVA ≈ 6.23 BCM、VENUS ≈ 5.65 BCM，与 Ch2 SLIDE 16/17 的行业基准 6.0 BCM 同一量级 → 证明图纸的 "bcm" 标签是错的，而 μm³ 数值是对的（详见 T7 / T8）。
- (d) 原文："Gravure Roll Volume — Total volume of all the engraved cells on the roll surface per unit area of the surface / USA = BCM/in2 ……. More commonly just referred to as BCM / European = cm3/m2 / Conversion: 1 BCM/in2 = 1.55 cm3/m2" — Ch2 SLIDE 18；"Cell Volume Terminology – BCM/in2 — 1 Billion Cubic Microns (Micrometers) — 1 BCM = 1,000,000,000 um3" — Ch2 SLIDE 19。本章实例：*"Volume 27,600,000 cubic micrometers (27.6 bcm)"*、"10,200,000 cubic micrometers (10.2bcm)"* —SLIDE 28 — 二次读图`。
### C9. DPI (dots per inch) & dot spacing & rotation ｜ 点密度、点间距与旋转角

- (b) English definition：DPI = dots (cells) counted per linear inch along a lattice axis; dot spacing = the ratio between the two lattice pitches (VIVA: 2:1); rotation = the angle of the lattice from vertical (VIVA: 19.6°). Together they define the 2-D lattice, which together with per-cell volume defines roll-level BCM.
- (c) 操作化定义：







- 主判定式：dots/in² ≈ 1.25 × (DPI)² ÷ spacing_ratio（经验关系，[本报告推导]，源材料未给出公式）
- VIVA 验算：1.25 × 27² ÷ 2 = 1.25 × 729 ÷ 2 = **455.6**，与图纸标注反算值 455.65 相差 0.005% ✓
- VENUS 验算：1.25 × 34.5² ÷ 1 = 1.25 × 1190.25 = **1487.8 ≈ 1488**，与图纸直印值一致 ✓
- 1.25 的最可能物理解释 [本报告推导]：总点数 = 浅点数 + 深点数，且 深点 = 浅点 ÷ 4（即 25% 为深点）。VIVA：364.5 浅点 + 91.1 深点 = 455.6 ✓。标记为待澄清（源材料未说明）。
- 旋转角的操作意义：Rotated 19.6° from vertical 决定网点行相对于纸机方向的倾斜，是避免与刮刀/幅材产生规则干涉（摩尔纹、条道）的设计手段；图纸另以红色垂直基准线 + 绿色角度标注双重标出，并附强制工艺注记 *"*Always tilt to the right unless requested otherwise."*（即倾斜方向本身是受控规格项）。
- 几何自洽校验（[本报告推导]）：0.148148" ÷ 0.033127" = 4.4721 = √20 = √(4² + 2²) → 图示的「对角网点尺寸」实为 4 个水平节距 + 2 个垂直节距的合矢量（考虑 VIVA 垂直节距 = 2 × 水平节距，即 4 水平 + 1 垂直行距）。图纸几何完全自洽，可作为读图正确性的内部证据。
- ⚠️ 27 dpi 与标注节距的偏差 [本报告推导]：1 ÷ 27 dpi = 0.037037"，而图纸标注水平节距 0.033127" → 0.037037 ÷ 0.033127 = **1.1180 = √1.25**。即实际节距 = 名义 dpi 节距 ÷ √1.25 → 与上述 1.25 系数为同一现象的两面。待澄清。
- (d) 原文：*"27 dpi dot / 2:1 dot spacing / Rotated 19.6° from vertical"、"19.6° Rotation From Vertical"、"0.033127" (841.4μm)"、"0.265015" (6731.4μm)"、"0.148148""、"*Always tilt to the right unless requested otherwise." — SLIDE 28 — 二次读图。VENUS："Pattern - 34.5DPI 1488 DOTS/SQ-IN"*、"0.02926"" — Ch4 SLIDE 32 — 二次读图。
### C10. Deep Dot / Shallow Dot（two-tier cell）｜ 深点 / 浅点（双级网穴）

- (b) English definition：The VIVA pattern carries two distinct cell tiers on the same roll: Shallow Dot 0.020" × 0.020" ±5% at 10,200,000 μm³, and Deep Dot at 27,600,000 μm³. The deep tier is the physical instantiation of Ch2 SLIDE 20's "Deep" engravings.
- (c) 操作化定义：





- 判定式：单穴容积_deep ÷ 单穴容积_shallow = 27,600,000 ÷ 10,200,000 = **2.706×** → 凡比值显著 >1（本报告建议阈值 ≥1.5×，[本报告推导]）即判为双级网穴结构。
- 深度比反算（[本报告推导]）：设两穴形貌因子相同、容积 ∝ 长 × 宽 × 深，则
深宽比 = 0.025" ÷ 0.020" = **1.250**；深高比 = 0.0227" ÷ 0.020" = **1.135**；
深度比 = 2.706 ÷ (1.250 × 1.135) = 2.706 ÷ 1.4188 = **1.907** → 深点约比浅点深 1.91 倍。
- 公差方向的操作意义（关键工程信息）：
| 层级 | 尺寸 | 容积 | 下限 | 上限 | Test Burn Target |
|---|---|---|---|---|---|
| Shallow | 0.020" × 0.020" ±5%（483–533 μm） | 10,200,000 μm³ | −0%（10,200,000） | +10%（11,220,000） | +12%（11,424,000） |
| Deep | 0.025" × 0.0227" ±5%（603–667 × 548–606 μm） | 27,600,000 μm³ | −5% | +5% | 标注 "-5%"、数值 28,980,000（= +5%，⚠️ 符号与数值矛盾，待澄清） |
- 自检算式（[本报告推导]）：10,200,000 × 1.10 = 11,220,000 ✓；10,200,000 × 1.12 = 11,424,000 ✓；27,600,000 × 1.05 = 28,980,000 ✓ → 三个 Test Burn 值均与名义值的百分比精确吻合，可作为二次读图正确性的算术证据。
- ⚠️ 冲突：既有 图像内容补充 记为 0.032" × 0.022" ±10%（0.813 × 0.559 mm）；二次读图记为 0.025" × 0.0227" ±5%（635 × 577 μm）。两者并列，不作取舍（见 T1 注）。
- (d) 原文：*"SHALLOW DOT 0.020" x 0.020" ±5% (0.019" to 0.021") (508 x 508 microns) ±5% (483μ to 533μ)"；"VOLUME 10,200,000 cubic micrometers (10.2bcm) • lower limit -0% (10,200,000) • upper limit +10% (11,220,000) (Test Burn Target +12% 11,424,000)"；"DEEP DOT 0.025" x 0.0227" ±5% (0.0237"- 0.0262" x 0.0216" - 0.0238") (635 x 577 microns) ±5% (603μ - 667μ x 548μ - 606μ)"；"VOLUME 27,600,000 cubic micrometers (27.6 bcm) • limit +/- 5% (Test Burn Target - 5% 28,980,000)"* — SLIDE 28 — 二次读图。既有提取："Deep Dot dimensions 0.032" × 0.022" ±10% (0.813 × 0.559mm)；Volume 27,600,000 cubic microns (27.6 BCM)" — SLIDE 28 — 图像内容补充。
### C11. Cell dimensions ｜ 网穴尺寸（Cell diameter / Cell depth / Cell volume 三参数）

- (b) English definition：Ch2 SLIDE 21 groups specification parameters into two boxes: Cell dimensions = *Cell diameter / Cell depth / Cell volume*；Pattern details = Shapes, sizes, spacing. SLIDE 28 instantiates all of them.
- (c) 操作化定义：



- 三参数判定式（自由度约束）：Ch4 SLIDE 36："Engraver must have at least 1 degree of freedom. Can only specify 2 from the key engraving parameters of volume, depth, and diameter" → 规格书最多只能锁定 3 个中的 2 个，第 3 个必须由雕刻商自由选定。
- 本章实例化（VIVA）：
| 参数类别 | 本章数值 |
|---|---|
| Cell diameter（长/宽） | Shallow 0.020" × 0.020"；Deep 0.025" × 0.0227" |
| Cell depth | [未找到原句] —— 图纸未直接标注深度；仅可由容积与口径反算（见 C10 深度比 1.907×，[本报告推导]） |
| Cell volume | 10,200,000 μm³（shallow）/ 27,600,000 μm³（deep） |
- 操作含义 [本报告推导]：VIVA 图纸锁定了 diameter（两级）+ volume（两级），把 depth 留给了雕刻商 —— 完全符合 Ch4 SLIDE 36 的「只能锁 2 个」规则。这是本章图纸与 Ch4 设计哲学之间的结构性自洽。
- (d) 原文："紫框 Cell dimensions（Cell diameter / Cell depth / Cell volume）；绿框 Pattern details（Shapes, sizes, spacing）" — Ch2 SLIDE 21 — 图像内容补充；"Engraver must have at least 1 degree of freedom. Can only specify 2 from the key engraving parameters of volume, depth, and diameter" — Ch4 SLIDE 36。本章实例见 SLIDE 28（T1）。
### C12. Pattern details（Shapes, sizes, spacing）｜ 图案细节（形状、尺寸、间距）

- (b) English definition：The second specification box on Ch2 SLIDE 21: Shapes, sizes, spacing — i.e. everything about the arrangement of cells as opposed to the geometry of a single cell.
- (c) 操作化定义：




- 三要素判定式（VIVA 实例）：
- Shapes：dot（圆形点，非 60° hex、非 Channelex、非 Trihelical —— 对比 Ch2 SLIDE 13 — 图像内容补充 的六种标准 anilox：60° Hex / GTT / 45° / Longcell / Channellox / Trihelical）→ VIVA 图案不属于任何标准 anilox 图案，构成 Ch2 SLIDE 20 "Engineered patterns" 的判定证据之一。
- sizes：0.020"（浅）/ 0.025" × 0.0227"（深）
- spacing：27 dpi + 2:1 + 0.033127" / 0.066254" / 0.265015" / 0.148148" + 19.6°
- 图案身份编码判定式：本章的图案以雕刻方 + 代号命名（Saueressig – KCP06 / Pamarco – KCP08 / APEX – KCP09 / Harper 90x60 Marinette Engraving / IR Engraving 90x60 Marinette Engraving）。→ KCPxx 是 KC 的图案代号，Marinette 90x60 是产线+规格代号；判定规则：同一 KCP 代号在不同雕刻方处应产生同一图案（这正是 Ch4 SLIDE 34 中 "IR Engraving did not do a good job repeating the preferred engraving" 的判定前提）。
- 验收判据（染色法，跨章）：40X Zoom 下与对照辊并排比较 DuPont Stain（Ch4 SLIDE 29/30）；缺陷以红圈标出（本章 SLIDE 25 即已使用此法）。
- (d) 原文："绿框 Pattern details（Shapes, sizes, spacing）" — Ch2 SLIDE 21 — 图像内容补充；"Saueressig – KCP06" — SLIDE 25；*"Harper 90x60 Marinette Engraving"、"Pamarco – KCP08"、"APEX – KCP09"、"IR Engraving 90x60 Marinette Engraving"* — SLIDE 25 — 二次读图；"#1 Printer pattern (VIVA® Towel) / Stained sample (DuPont Stain #4) / Red dots = latex / Green = fiber" — SLIDE 24 — 图像内容补充。
## 模块 3：证据链（Evidence Tables）

### T1 — Harper VIVA 辊图纸全字段表（"OLU – VIVA Gravure Roll Pattern"）SLIDE 28



图纸品牌：HARPER®（图纸右下角商标 + 六边形标识 + 50 周年徽标）。
⚠️ 任务书所述的标题字符串 HARPERLASER 112x20 与 128x20：[未找到原句] —— 图纸上可读到的品牌标识为 HARPER®，辊面规格为 112" × 20"（非 128"）。

||||
|---|---|---|
|1|TITLE（幻灯片标题）|OLU – VIVA Gravure Roll Pattern|SLIDE 28 文本层|
|2|BRAND / 图纸签发方|HARPER®（+ 六边形 logo；50 周年徽标，徽标年份两次读图分别为 1973-2023 与 1974-2024，⚠️ 待澄清）|SLIDE 28 — 二次读图|
|3|HARPERLASER 标识|[未找到原句]|全图检索未发现|
|4|CUSTOMER|Retroflex / KC|SLIDE 28 — 图像内容补充 + 二次读图（两源一致）|
|5|LOCATION 栏|[未找到原句] —— 图纸无独立 LOCATION 字段；可追溯字段为 Customer = Retroflex / KC|二次读图|
|6|ROLL#（辊号）|KC GR# 5（红色标注，二次读图另见 R#5）|两源一致|
|7|JOB#（工作号）|HCA Job# 111233501|两源一致|
|8|XDI #|XDI # 3|两源一致|
|9|DATE（出图日期）|8/30/23|两源一致（含签字栏手写日期）|
|10|Signature of Approval|手写签名 + 日期 8/30/23|二次读图|
|11|Roll Face Width（辊面宽）|112" (2,844.8 mm)|两源一致|
|12|Roll Diameter（辊径）|20" (508 mm)|两源一致|
|13|Rotation（旋向）|Counterclockwise（逆时针）|两源一致|
|14|Journal（轴头）|*Long Journal*（长轴头，带星号注记）；Drive Side（传动侧）|二次读图|
|15|Engraved Area（雕刻区）|CENTERED，104.5" Wide (2,654.3 mm)|两源一致|
|16|End margin（端部留边）|3.75" Both Ends (95.25 mm)；自检：112" − 104.5" = 7.5" = 2 × 3.75" ✓|两源一致|
|17|Top / Test Burn Area（试烧区）|⚠️ 冲突：图像内容补充：*Top Burn Area 3.5" Max Both Ends*；二次读图（两次独立）：*Test Burn Area 2.5" Max Both Ends (63.5mm)*|⚠️ 待澄清|
|18|Flat Burn Target（平整度目标）|< ±10%|SLIDE 28 — 图像内容补充（二次读图未复现，⚠️ 待复核）|
|19|DPI（点密度）|27 dpi dot|两源一致|
|20|Spacing（点间距比）|2:1 dot spacing|两源一致|
|21|Rotation（图案旋转角）|19.6° from vertical（红色参数字 + 绿色 19.6° Rotation From Vertical 双重标注 + 红色垂直基准线）|两源一致|
|22|Deep Dot dimensions（深点尺寸）|⚠️ 冲突：图像内容补充：0.032" × 0.022" ±10%（0.813 × 0.559 mm）；二次读图（两次独立、四象限分块）：0.025" × 0.0227" ±5%（0.0237"–0.0262" × 0.0216"–0.0238"；635 × 577 microns ±5%，603–667 μ × 548–606 μ）|⚠️ 待澄清（二次读图内部自洽）|
|23|Shallow Dot dimensions（浅点尺寸）|0.020" × 0.020" ±5%（0.019"–0.021"）；508 × 508 microns ±5%（483–533 μ）|二次读图（既有提取缺失此字段）|
|24|Deep Dot Volume（深点容积）|27,600,000 cubic micrometers (27.6 bcm)；limit ± 5%；(Test Burn Target - 5% 28,980,000) ⚠️ 标注 "-5%" 但数值为 +5%|两源一致（Test Burn 值仅见二次读图）|
|25|Shallow Dot Volume（浅点容积）|10,200,000 cubic micrometers (10.2bcm)；lower limit -0% (10,200,000)；upper limit +10% (11,220,000)；(Test Burn Target +12% 11,424,000)|二次读图（既有提取缺失）|
|26|Dot spacing callouts（点距标注）|0.033127" (841.4 μm)（水平）；0.066254" (1,682.8 μm / 1.682 mm)（垂直，= 2× 水平 ✓）；0.265015" (6,731.4 μm)；0.148148" (3,762.9 μm)（二次读图右边缘另读作 762.9 μm，疑缺首位，待澄清）|二次读图（既有提取缺失）|
|27|Deep dots spacing|[未找到原句] —— 任务书所述 0.070" 在全图及全 deck 检索中未确认|—|
|28|Border（边框）|[未找到原句] —— 任务书所述 0.250" 在全图及全 deck 检索中未确认|—|
|29|3.050 / 3.0364|[未找到原句] —— 全图（四象限 + 顶部分条 ×3 放大）检索未确认|—|
|30|BCM（辊级容积标签）|27.6 BCM（深点，图纸标签）/ 10.2 BCM（浅点，图纸标签）⚠️ 与 Ch2 SLIDE 19 定义冲突 1000×（见 T7）|两源一致（数值），⚠️ 口径存疑|
|31|POLISH GOAL（抛光目标）|POLISHING NOTE: Target <= 10,700,000 Shallow Dot Volume Average|两源一致（措辞完全一致）|
|32|Process note（工艺注记）|*Always tilt to the right unless requested otherwise.（倾斜方向为受控规格项）|二次读图（既有提取缺失）|

T1 派生自检 [本报告推导]
- 抛光余量 = (10,700,000 − 10,200,000) ÷ 10,200,000 = **+4.90%**（抛光前预留量）；抛光去除率 = (10,700,000 − 10,200,000) ÷ 10,700,000 = **−4.67%**
- 雕刻区面积 = 104.5" × (π × 20") = 104.5 × 62.8319 = **6,565.9 in²**
- 全辊网点总数 ≈ 6,565.9 in² × 455.65 dots/in² = **2,991,700 ≈ 299 万个网穴**
- 雕刻区占比 = 104.5 ÷ 112 = **93.30%**；端部留边占比 = 7.5 ÷ 112 = **6.70%**
### T2 — Harper VENUS 辊规格表（"OLU VENUS Pattern (Original Specs)"）⚠️ 跨章：Ch4 SLIDE 32，非本章



章节归属校订：任务书将本表列为 Ch3 内容。经核对，VENUS 34.5 DPI 图纸位于 Ch4 SLIDE 32，不在 Ch3 的 22–28 页范围内；Ch3 的 SLIDE 28 是 VIVA 图纸。本报告按原文实际位置标注，并保留任务要求的对比。

||||
|---|---|---|
|1|TITLE|OLU VENUS Pattern (Original Specs)|Ch4 SLIDE 32 文本层|
|2|Customer|Kimberly Clark|Ch4 SLIDE 32 — 二次读图|
|3|Job#|HC 110615901|同上|
|4|XDI #|XDI #2|同上|
|5|Date|10-16-2022|同上|
|6|Roll Face Width|112"|同上|
|7|Roll Diameter|19.701"|同上|
|8|Engraved area|104.5" wide，Engraving to be centered on roller|同上|
|9|Rotation|counterclockwise rotation|同上|
|10|Pattern（点密度）|34.5 DPI|Ch4 SLIDE 32 — 图像内容补充 + 二次读图|
|11|Dots per square inch|1,488 DOTS/SQ-IN|同上（原文直印 Pattern - 34.5DPI 1488 DOTS/SQ-IN）|
|12|Target Volume|3,800,000 μm³ ± 5%|同上|
|13|Shallow Dot|0.02" = 0.508 mm|同上|
|14|点距标注|0.02926"（水平）／0.051852"（行距）／0.14493"（对角）／0.25926"（图案总高）|Ch4 SLIDE 32 — 二次读图（既有提取记为 0.02926"/0.02926"/0.01463"，⚠️ 差异待澄清）|
|15|雕刻方（原文记录）|3 家（Harper → IR Engraving → Pamarco）|Ch4 SLIDE 34 — SPEAKER NOTES|
|16|一致性拐点|Pamarco came on line in Q3 2024|Ch4 SLIDE 32 — SPEAKER NOTES|

#### ⚠️ T2-b：1000 倍口径冲突（必须标注为待澄清）

||||
|---|---|---|
|VIVA|27,600,000 cubic micrometers （27.6 bcm） — Ch3 SLIDE 28|按 Ch2 SLIDE 19（1 BCM = 1,000,000,000 um³）折算：27,600,000 ÷ 10⁹ = **0.0276 BCM**|图纸标签 vs 本章（Ch2）定义：相差 1000 倍|
|VENUS|3,800,000 μm³ ± 5% — Ch4 SLIDE 32（无 bcm 标签）|同法折算：3,800,000 ÷ 10⁹ = **0.0038 BCM**|与 VIVA 若同为「单穴 μm³」则无 1000 倍冲突，仅相差 27,600,000 ÷ 3,800,000 = **7.26 倍**|
|行业基准|2 ply bath specification = 60 degree hex, 180 LPI, **6.0 BCM** — Ch2 SLIDE 16；BOTH "6 BCM VOLUME" — Ch2 SLIDE 17|—|辊级 BCM 的现实量级为 ~6 BCM|

- 结论 [本报告推导]：任务书所述「与 Ch2 SLIDE 28 的 27,600,000 cubic microns (27.6 BCM) 存在 1000 倍口径冲突」需作两处校正：


- 页码校正：27,600,000 (27.6 BCM) 位于 Ch3 SLIDE 28（VIVA），不在 Ch2（Ch2 覆盖 10–21 页）。
- 冲突对象校正：真正的 1000 倍冲突发生在 Ch3 SLIDE 28 图纸自身的 (27.6 bcm) 标签 与 Ch2 SLIDE 19 的 1 BCM = 10⁹ μm³ 定义 之间；而 VIVA 与 VENUS 之间（同为单穴 μm³ 口径）相差 7.26 倍，不是 1000 倍。
- 待澄清清单（建议向图纸签发方书面确认）：① VIVA 图纸的 (27.6 bcm) 究竟指单穴容积（μm³ ÷ 10⁶ 的错误标签）还是辊级 BCM/in²；② VENUS 的 3,800,000 μm³ 是单穴还是辊级；③ 若均为单穴，则点阵密度（455.6 / 1488 dots/in²）应否参与辊级 BCM 折算（见 T8 三方验证）。
### T3 — 四大雕刻供应商对比表（+ 第 5 家 Saueressig）

||||||
|---|---|---|---|---|
|Harper|Charlotte, NC|VIVA OLU 辊图纸签发方（112"×20"，KC GR#5）；Harper 90x60 Marinette Engraving（DRC）|在用：VIVA 辊（图纸 8/30/23）、Marinette DRC 图案、VENUS 首批雕刻|⚠️ VENUS 首根辊耗时 9 个月，之后出现大幅体积偏差：*"Harper took 9 months to engrave first roll and then had a large volume skew"*；本章 SLIDE 25 未见缺陷红圈|SLIDE 22、SLIDE 25、SLIDE 28、Ch4 SLIDE 34 notes|
|Precision Roll Solutions / IR Engraving|Richmond, VA|IR Engraving 90x60 Marinette Engraving（DRC）；Jenks 曾用其做 2 根 VIVA 辊；Jenks GR2 / GR3 在 Ch4 中被用作对照辊（Control）|在用（但角色降级为对照/备选）：Ch3 未见其 OLU 辊图纸；Ch4 中仅作为 Control 出现|⚠️ 本章 SLIDE 25 唯一被红圈标缺陷者（3 处）；*"Did not measure volume with same tools so none of the data translated"；"Struggled with low volumes"；"IR Engraving did not do a good job repeating the preferred engraving"*；VENUS CT5："1/3 of dot is still filled with ceramic 'shell'"|SLIDE 22、SLIDE 25、Ch4 SLIDE 29/30、Ch4 SLIDE 34|
|Pamarco|Atlanta, GA|Pamarco – KCP08（DRC）；VENUS、VIVA 雕刻|2024 Q3 上线（*"came on line in Q3 2024"*）；VIVA Trial #1（12/3/24）；VENUS CT9|✅ 目前质量最好：VENUS CT9 — *"Dots are full circles and clean. No ceramic 'shell'."；"Pamarco has shown promise with strong engraving plan and enforcement"*；⚠️ *"Moving fast to meet pre-determined trial dates has created some non-ideal engravings"*；⚠️ VIVA Trial #1 GMT 仅 1100（目标 1800）|SLIDE 22、SLIDE 25、Ch4 SLIDE 29 notes、Ch4 SLIDE 32 notes、Ch4 SLIDE 34|
|Apex|Pittsburgh, PA|APEX – KCP09（DRC）；VIVA 雕刻|在用：VIVA Trial #1（2/12/25）→ Trial #2（连续运行 24 h）|⚠️ Trial #2 需三次重抛光：Re-Polish #1 / #2 / #3；GMT 1550 vs 1800；Ch2 SLIDE 13 notes 另记 *"Anilox vs Gravure and Apex Owner Discussion this week"*（术语归属当时仍在讨论）|SLIDE 22、SLIDE 25、Ch4 SLIDE 30 notes、Ch4 SLIDE 31、Ch2 SLIDE 13 notes|
|Saueressig（第 5 家，不在 Key Vendors 名单内）|[未找到原句]（既有报告称「欧洲」，本章无原文支撑）|Saueressig – KCP06（DRC，本章作大图展示）|有图案实绩（SLIDE 25 的唯一正面展示对象）|本章未见缺陷标记（作为参照图案）|SLIDE 25|

T3 关键结构性发现 [本报告推导]
1. 「4 家 Key Vendors」≠「全部雕刻方」：SLIDE 22 列 4 家，SLIDE 25 出现 5 个雕刻方名称（多出 Saueressig）。
2. 可用供应基础实为 3 家：4 家中 IR Engraving 因测量工具不一致导致 "none of the data translated"（Ch4 SLIDE 34），对新图案开发不构成可用产能。
3. 地理集中度：4 家全部位于美国东部/东南部工业带（NC / VA / GA / PA），无任何非北美供应商进入 Key Vendors 名单 —— 与 Ch2 SLIDE 10 的 "vendor options due to chrome 6" 叠加，构成本章对供应基础收窄的完整证据链。

### T4 — 「过去几年做过的辊」清单表 ⚠️ 任务书所列 6 条条目：[未找到原句]



任务书要求列出：1 Specialty Coated Blue Wrap / 2 VIVA Signature Cloth / 3 VIVA Signature Cloth / 4 VIVA Signature Cloth / 5 VENUS Bath Tissue / 6 VENUS Bath Tissue。
经全 deck 检索（文本层 + SmartArt XML + 38 页全部图像 + 内嵌视频 9 帧）：上述六条清单、以及 "Specialty Coated Blue Wrap" 一词，均不存在于本源材料。 下表改以源材料实际记载的辊/图案清单呈现，逐条标注出处。

||||||
|---|---|---|---|---|
|1|OLU – VIVA Gravure Roll Pattern（KC GR# 5，XDI #3，HCA Job# 111233501）|OLU（Jenks / BIL）|Harper|8/30/23|SLIDE 28|
|2|OLU VENUS Pattern (Original Specs)（HC 110615901，XDI #2）|OLU|Harper → IR → Pamarco（3 家）|10-16-2022|Ch4 SLIDE 32|
|3|DRC #1 Printer pattern (VIVA® Towel)（DuPont Stain #4）|DRC（Marinette）|见下条 4–8|无日期|SLIDE 24|
|4|Harper 90x60 Marinette Engraving|DRC（Marinette）|Harper|无日期|SLIDE 25 — 二次读图|
|5|IR Engraving 90x60 Marinette Engraving（3 处红圈缺陷）|DRC（Marinette）|IR Engraving|无日期|SLIDE 25 — 二次读图|
|6|Pamarco – KCP08|DRC|Pamarco|无日期|SLIDE 25 — 二次读图|
|7|APEX – KCP09|DRC|Apex|无日期|SLIDE 25 — 二次读图|
|8|Saueressig – KCP06（大图，六边形蜂窝）|DRC|Saueressig|无日期|SLIDE 25|
|9|Jenks 的 2 根 VIVA 辊（IR Engraving 制作）|OLU（Jenks）|IR Engraving|无日期|Ch4 SLIDE 34 notes|
|10|Control IR Engraving Jenks GR2（对照辊）|OLU（Jenks）|IR Engraving|12/3/25|Ch4 SLIDE 29|
|11|Control IR Engraving Jenks GR3（对照辊）|OLU（Jenks）|IR Engraving|2/11/25|Ch4 SLIDE 30|
|12|Jenks L12 Bath Gravure Rolls（180 L/cm vs 180 L/in 单位事故）|Bath（Jenks L12）|未标注|Fall of 2022|Ch2 SLIDE 17|
|13|Jenks Facial Lotion GR（2 BCM / 6 BCM 交替条带 + 死区）|Facial（Jenks）|未标注|无日期|Ch2 SLIDE 10 notes|
|14|Banded roll（分段辊，VENUS 项目）|OLU|IR Engraving（*Ran a banded roll and then IR Engraving did not do a good job repeating the preferred engraving*）|无日期|Ch4 SLIDE 34 notes|

### T5 — KC 各厂 × 雕刻商分布表 ⚠️ 源材料未给出完整映射；下表为「有原文支撑的部分映射 + 明确标注的空缺」



任务书假设存在一张「Beech Island / Jenks / VENUS / VIVA → Harper；其他 → IR Engraving / Precision Roll Solutions / Pamarco / Apex」的分布表。该表不存在于源材料；且 Beech Island 一词在全 deck 中零命中。下表为可由原文直接支撑的映射（✅）与无原文支撑的空缺（❌ [未找到原句]）。

||||
|---|---|---|
|Marinette — DRC|Harper（90x60）、IR Engraving（90x60）、Pamarco（KCP08）、APEX（KCP09）、Saueressig（KCP06）|✅ 强|SLIDE 23（Marinette DRC Process）、SLIDE 25|
|Jenks & BIL — OLU|VIVA 图纸由 Harper 签发（KC GR#5）|✅ 强|SLIDE 26（Jenks & BIL OLU Process）、SLIDE 28（Customer Retroflex / KC，OLU VIVA）|
|Jenks — VIVA（历史 2 根辊）|IR Engraving|✅ 强|Ch4 SLIDE 34 notes："Switched to IR Engraving because Jenks had used them for 2 VIVA rolls"|
|Jenks — 对照辊 GR2 / GR3|IR Engraving|✅ 强|Ch4 SLIDE 29 / SLIDE 30|
|Jenks — L12 Bath（Fall 2022）|[未找到原句]|❌|Ch2 SLIDE 17 未标注雕刻方|
|Jenks — Facial Lotion GR|[未找到原句]|❌|Ch2 SLIDE 10 notes 未标注雕刻方|
|VENUS 项目（产线未注明）|Harper → IR Engraving → Pamarco（3 家）|✅ 强|Ch4 SLIDE 32 notes、 Ch4 SLIDE 34 notes|
|VIVA 项目（产线未注明）|Harper（图纸）/ Pamarco（Trial #1, 12/3/24）/ Apex（Trial #1, 2/12/25）+ IR Engraving 作为 Control|✅ 强|SLIDE 28、Ch4 SLIDE 29/30|
|Beech Island（BI / BIL）|[未找到原句] —— "Beech Island" 零命中；SLIDE 26 标题中的 BIL 在 Ch1 SLIDE 5 语境下与 OLU 并列，但源材料未展开 BIL 缩写|❌|—|
|各厂的「主供应商」指派|[未找到原句]|❌|源材料从未给出工厂→主供应商的指派表|

T5 的可操作结论 [本报告推导]：源材料提供的是「项目 × 雕刻方」映射（VENUS 3 家、VIVA 3 家 + 1 对照、DRC 5 家），而不是「工厂 × 雕刻方」映射。任何「某厂归某家」的指派，在本材料中均无据可依，须以采购记录另行核实。

### T6 — VIVA 辊影像记录表（照片 / 视频 / 图案实物）



⚠️ 任务书所述 "Pictured below is the newest VIVA roll for Beech Island made by Harper"：[未找到原句]（全 deck 零命中，含文本层、SmartArt、图像、视频逐帧）。

||||||
|---|---|---|---|---|
|1|SLIDE 27|内嵌视频（ppt/media/media1.mp4，5.93 s，1350×1080，含音轨）|一条在产的 OLU 涂布/印刷工位：上方蓝色背压辊 + 下方深色凹版辊 + 穿过压区的幅材；现场有大量干涸乳胶残留（管壁、软管、结构件、集液盘）；可见蓝色软管、米色波纹管、轴承座、金属框架|无（9 帧逐帧读取，全片无可辨识文字、无字幕、无标识牌）|SLIDE 27 — 二次读图|
|2|SLIDE 28|图片（1213×940 png）|Harper VIVA 辊制造图纸（T1 全字段）+ 点阵示意（黑实心点 = 图案边界/深点，白色空心点 = 图案内部/浅点，绿色连线 = 倾斜行结构，红色垂直基准线 = 19.6° 角基准）|有（约 25 个字段，见 T1）|SLIDE 28 — 二次读图|
|3|SLIDE 24|图片（801×469 png）|DRC VIVA® Towel 图案：① 40× 级染色样显微照（红色圆点 = 乳胶，绿色纤维背景，蓝圈标注单点）；② 低倍下红色乳胶点构成菱形/四叶 lattice、绿色纤维填充；③ 图案工程图（标注 .0471" / .1884" / .133°(133°)）；④ 辊体工程图（Engraved area - 112" wide / Brass Plate / Standard wrap / Drive Side / Operator Side / Engraving to be used on both sides）|有（标注文字；④ 组读数置信度中等，⚠️ 建议复核）|SLIDE 24 — 图像内容补充 + SLIDE 24 — 二次读图|
|4|SLIDE 25|图片 ×2（1298×328 对比条 + 420×508 大图）|对比条：Harper 90x60 Marinette Engraving（粗糙、网穴壁与穴底明显粗糙）／Pamarco – KCP08（洁净均匀六边形、穴底平整）／APEX – KCP09／IR Engraving 90x60 Marinette Engraving（3 处红圈缺陷）；大图：Saueressig – KCP06 六边形蜂窝显微形貌（图像内无文字，标题由页面文本框给出）|有（对比条各面板标题）；KCP06 大图无内置文字|SLIDE 25 — 二次读图|
|5|SLIDE 26|图片（806×414 png）|Jenks & BIL OLU Process 流程图：Tissue Machine ← Unwind → Printer（Backing Roll / Gravure Roll / Air Layer / Print Fluid Delivery / Print Fluid Make-up System）→ Pressure Roll → Crepe Dryer（Heated Hood）→ Crepe Blade → Reel → Converting Line|有|SLIDE 26 — 图像内容补充 + 二次读图|
|6|Ch4 SLIDE 29 / 30|图片|VIVA Trial #1 的 DuPont Stain 结果：试车辊 vs Control（IR Engraving Jenks GR2 / GR3），均 40X Zoom|有|Ch4 SLIDE 29/30|
|7|Ch4 SLIDE 31|图片 ×4|Apex VIVA Trial #2 – Ran for 24 Hours：3D Scan #2（30 lpi, 20 degrees），形貌尺寸 649 / 627 / 729 / 697 / 896 / 187 μm；右侧 Re-Polish #1 / #2 / #3 三次重抛光对比|有|Ch4 SLIDE 31 — 图像内容补充|
### T7 — ⚠️ 单位口径冲突专表（Unit Incident / Caliber Conflict）

|||||||
|---|---|---|---|---|---|
|U1|VIVA 图纸的 bcm 标签 vs BCM 定义|27,600,000 cubic micrometers **（27.6 bcm）**|1 BCM = 1,000,000,000 um³ → 27,600,000 ÷ 10⁹ = **0.0276 BCM**|1000×|发函图纸签发方确认口径|SLIDE 28 vs Ch2 SLIDE 19|
|U2|VIVA 浅点同法冲突|10,200,000 cubic micrometers **（10.2bcm）**|10,200,000 ÷ 10⁹ = **0.0102 BCM**|1000×|同上|SLIDE 28 — 二次读图 vs Ch2 SLIDE 19|
|U3|VIVA vs VENUS（若同为单穴 μm³）|27,600,000 μm³（VIVA 深点）|3,800,000 μm³ ±5%（VENUS）|7.26×（非 1000×）|属图案差异，非单位错误|SLIDE 28 vs Ch4 SLIDE 32|
|U4|VENUS 点距标注|既有提取 0.02926" / 0.02926" / 0.01463"|二次读图 0.02926"（水平）/ 0.051852"（行距）/ 0.14493"（对角）/ 0.25926"（总高）|口径不同（部分/整体尺寸）|待澄清：0.25926 ÷ 0.051852 = **5.000**（整倍数关系，自洽）|Ch4 SLIDE 32|
|U5|VIVA Deep Dot 尺寸|0.032" × 0.022" ±10%（0.813 × 0.559 mm）|0.025" × 0.0227" ±5%（635 × 577 μm，0.0237–0.0262" × 0.0216–0.0238"）|X 向 1.28×、公差 2×|并列呈现，待复核原图|SLIDE 28 — 图像内容补充 vs SLIDE 28 — 二次读图|
|U6|VIVA Top/Test Burn Area|Top Burn Area **3.5"** Max Both Ends|Test Burn Area **2.5"** Max Both Ends (63.5mm)|1.4×|待澄清（栏名与数值同时不同）|同上两源|
|U7|（跨章参照）LPI vs LPcm|180 Lines/cm 标 "6 BCM VOLUME"|180 Lines/inch 标 "6 BCM VOLUME"（180 LCM = 460 LPI；180 LPI = 70 LCM）|单穴容积差 6.45×（= 2.54²）|已发事故，规格书强制双单位并列|Ch2 SLIDE 17|
|U8|（跨章）测量工具不一致|IR Engraving 的量具|KC 的量具|不可比（*"none of the data translated"*）|合同锁定量具与方法|Ch4 SLIDE 34 notes|

### T8 — 派生量推导表（Derived Quantities，[本报告推导]，算式完整列出）

||||
|---|---|---|
|D1|VIVA 点阵密度（由图纸标注反算）|1 ÷ (0.033127" × 0.066254") = 1 ÷ 0.00219480|455.65 dots/in²|
|D2|VIVA 点阵密度（由 dpi 正算）|27 × (27 ÷ 2) × 1.25 = 27 × 13.5 × 1.25|455.6 dots/in²（与 D1 偏差 +0.005% ✓）|
|D3|VENUS 点阵密度（由 dpi 正算校验）|1.25 × 34.5² = 1.25 × 1190.25|1487.8 ≈ 1488 DOTS/SQ-IN（与图纸直印值一致 ✓）|
|D4|VENUS 点距校验|1 ÷ 34.5 = 0.028985" vs 标注 0.02926" → 0.02926 ÷ 0.028985 − 1|+0.95%（DPI 与点距互洽 ✓）|
|D5|VIVA 名义节距 vs 实际标注节距|(1 ÷ 27) ÷ 0.033127 = 0.037037 ÷ 0.033127|1.1180 = √1.25（与 1.25 系数为同一现象，待澄清）|
|D6|VIVA 几何自洽校验|0.148148 ÷ 0.033127 = 4.4721 = √20 = √(4² + 2²)|✓ 对角尺寸 = 4 水平节距 + 2 垂直节距的合矢量|
|D7|VENUS 辊级容积|1488 dots/in² × 3,800,000 μm³ ÷ 10⁹|5.654 BCM/in²|
|D8|VIVA 辊级容积（下界：全为浅点）|455.65 × 10,200,000 ÷ 10⁹|4.648 BCM/in²|
|D9|VIVA 辊级容积（上界：全为深点）|455.65 × 27,600,000 ÷ 10⁹|12.576 BCM/in²|
|D10|VIVA 辊级容积（中心估计：深:浅 = 1:4）|(91.13 × 27,600,000 + 364.5 × 10,200,000) ÷ 10⁹ = (2.5151×10⁹ + 3.7179×10⁹) ÷ 10⁹|6.233 BCM/in²|
|D11|★ 三方三角验证|D10 6.23 ／ D7 5.65 ／ Ch2 SLIDE 16 行业基准 6.0 BCM|同量级（±10% 内）→ 证明图纸的 μm³ 数值正确、而 "bcm" 标签错误（1000×）|
|D12|深/浅点容积比|27,600,000 ÷ 10,200,000|2.706×|
|D13|深/浅点深度比（等形貌因子假设）|2.706 ÷ (1.250 × 1.135) = 2.706 ÷ 1.4188|1.907×（深点约为浅点深度的 1.91 倍）|
|D14|抛光预留量 / 去除率|(10,700,000 − 10,200,000) ÷ 10,200,000；÷ 10,700,000|+4.90% 预留 / −4.67% 去除|
|D15|VIVA 雕刻区面积|104.5" × π × 20" = 104.5 × 62.8319|6,565.9 in²|
|D16|VIVA 全辊网点总数|6,565.9 × 455.65|≈ 2,991,700（约 299 万个网穴）|
|D17|VENUS 雕刻区面积与网点总数|104.5 × π × 19.701 = 104.5 × 61.8942 = 6,467.9 in²；6,467.9 × 1488|6,467.9 in²／≈ 9,624,300（约 962 万个网穴）|
|D18|VENUS / VIVA 网穴总数比|9,624,300 ÷ 2,991,700|3.22×（VENUS 网穴更密，但单穴容积仅为 VIVA 深点的 1/7.26）|
|D19|VIVA 图纸签发 → Pamarco 试车周期|8/30/23 → 12/3/24（366 + 95 天）|461 天 ≈ 15.1 个月|
|D20|VIVA 图纸签发 → Apex 试车周期|8/30/23 → 2/12/25（461 + 71 天）|532 天 ≈ 17.5 个月|
|D21|VENUS 图纸签发 → Pamarco 上线|10-16-2022 → Q3 2024（7–9 月）|≈ 21–23 个月|
|D22|试车 GMT 达标率|Pamarco 1100 ÷ 1800；Apex 1550 ÷ 1800|61.1% ／ 86.1%（缺口 −38.9% ／ −13.9%）|
|D23|Apex / Pamarco GMT 比|1550 ÷ 1100|1.409×（雕刻质量最优者 GMT 反而最低，见 A5）|

## 模块 4：章节间衔接（Chapter Connections）

### 4.1 与前章 Ch2（Engraving & Specs）："Outside the engravers comfort zones" → 本章供应商爬坡困难的兑现链

||||
|---|---|---|
|① "Outside the engravers comfort zones"|Harper 首根 VENUS 辊耗时 9 个月："Harper took 9 months to engrave first roll and then had a large volume skew"|强（原文直述）|Ch2 SLIDE 20 → Ch4 SLIDE 34 notes|
|② *"Engravers have no insight beyond the cell dimensions"*（KC 必须自己把产品性能翻译成雕刻规格）|本章 SLIDE 28 图纸即 KC 的翻译产物：约 25 个字段，把「产品性能」落成 dpi / 间距比 / 旋转角 / 双级穴尺寸 / 双级容积 / 抛光目标|强（图纸即证据）|Ch2 SLIDE 20 notes → SLIDE 28（T1）|
|③ "Large amount of unengraved area = more complex polishing"|本章图纸出现独立的抛光目标条款：POLISHING NOTE: Target <= 10,700,000 Shallow Dot Volume Average；Ch4 中 Apex Trial #2 需 Re-Polish #1/#2/#3|强|Ch2 SLIDE 20 → SLIDE 28 + Ch4 SLIDE 31|
|④ *"vendor options due to chrome 6"*（镀铬平台供应基础收窄）|本章 SLIDE 22：Key Vendors 仅 4 家，全部位于美国东部|强|Ch2 SLIDE 10 → SLIDE 22|
|⑤ "Cell geometry, lines per inch, cell volume" 三参数必须同锁|本章图纸同时给出 dpi（27）+ 间距比（2:1）+ 角度（19.6°）+ 双级容积（10.2M / 27.6M）|强|Ch2 SLIDE 16 → SLIDE 28|
|⑥ "180 Lines/cm vs 180 Lines/inch，BOTH '6 BCM VOLUME'" 单位事故|本章再次出现单位口径冲突：(27.6 bcm) vs 1 BCM = 10⁹ μm³ 的 1000 倍矛盾（T7-U1/U2）|强（同一失效模式复发）|Ch2 SLIDE 17 → SLIDE 28|
|⑦ *"KC's engineered patterns create a tight engraving window"*（Ch4 Summary 复述）|本章 SLIDE 25：四家雕刻方在同一个 DRC 图案族上的形貌差异肉眼可辨；IR Engraving 被红圈标缺陷 3 处|中强|Ch4 SLIDE 38 → SLIDE 25|
|⑧ Ch2 未预告的新变量：供应商测量体系不一致|"Did not measure volume with same tools so none of the data translated"|强（Ch2 完全未涉及）|Ch4 SLIDE 34 notes|

衔接结论 [本报告推导]：Ch2 的「越界 → 难做」是一个技术判断，本章+Ch4 把它兑现为三个可量化的商业后果：9 个月的周期（Harper）、15.1–17.5 个月的图纸→试车周期（D19/D20）、3 家可用供应商（4 家中 1 家测量不可比）。Ch2 说「难」，Ch3/Ch4 回答「难到什么程度」。

### 4.2 与后章 Ch4（Trials & Design）：供应商能力差异 → 试车结果差异（GMT 达标率）

|||||
|---|---|---|---|
|Harper|VIVA 图纸签发方；Marinette DRC 图案；SLIDE 25 无缺陷标记|VENUS："Harper took 9 months to engrave first roll and then had a large volume skew" → 转出|无 GMT 记录（项目转交 IR → Pamarco）|SLIDE 28、SLIDE 25、Ch4 SLIDE 34 notes|
|IR Engraving|本章唯一被红圈标缺陷者（3 处）；VENUS CT5："1/3 of dot is still filled with ceramic 'shell'"|未进入 VIVA 试车，仅作 Control 对照辊（Jenks GR2 / GR3）|不适用（作为基准）|SLIDE 25、Ch4 SLIDE 29/30、Ch4 SLIDE 34|
|Pamarco|Pamarco – KCP08；雕刻质量最优：VENUS CT9 *"Dots are full circles and clean. No ceramic 'shell'."；"strong engraving plan and enforcement"*|VIVA Trial #1（12/3/24）：1100 GMT vs 1800 OLU GMT Target|61.1%（缺口 −38.9%）❌|SLIDE 25、Ch4 SLIDE 29 notes、Ch4 SLIDE 34|
|Apex|APEX – KCP09；VIVA Trial #2 连续运行 24 h 后需 Re-Polish #1/#2/#3|VIVA Trial #1（2/12/25）：1550 GMT vs 1800 OLU GMT Target|86.1%（缺口 −13.9%）❌|SLIDE 25、Ch4 SLIDE 30 notes、Ch4 SLIDE 31|

★ 4.2 的核心反直觉发现 [本报告推导]：

雕刻质量排序（Pamarco > Apex > IR Engraving）与 GMT 排序（Apex 1550 > Pamarco 1100）不一致。
依据：Ch4 SLIDE 34 判定 Pamarco 的网穴 *"Dots are full circles and clean. No ceramic 'shell'."*（最优），而 Ch4 SLIDE 29 notes 记录其 GMT 仅 1100；Apex 的 Trial #2 需要三次重抛光（Ch4 SLIDE 31，工艺不稳定），但 Ch4 SLIDE 30 notes 记录其 GMT 1550（更接近 1800 目标）。
解释（[本报告推导]，需实验验证）：GMT 是 X/Y 方向表面覆盖率的函数，而覆盖率由 Cell diameter 主导（Ch4 SLIDE 35：*"X and Y direction sheet surface coverage - Key to GMT (Cell diameter)"*）。「网穴刻得干净」只保证形貌正确，不保证 diameter/volume 落在 GMT 最优点上。因此：
① 雕刻质量的合格判据（无陶瓷壳、圆整、尺寸在公差内）是必要但不充分条件；
② 试车 GMT 的驱动参数是 Cell diameter（Ch4 SLIDE 35）而非「形貌洁净度」；
③ 采购谈判中，不得以「微观形貌最优」作为免检或免试车理由。

4.3 与 Ch4 设计哲学的接口 [本报告推导]：Ch4 SLIDE 36 规定 *"Can only specify 2 from the key engraving parameters of volume, depth, and diameter"*。回看本章 SLIDE 28 图纸：它锁定了 diameter（两级）+ volume（两级），把 depth 留给了雕刻商 —— 完全遵守该规则。这意味着 depth 的自由度是雕刻商的工艺变量，也正是体积偏差（*"large volume skew"*）的来源之一：雕刻商在 depth 上的选择差异，会以容积偏差的形式暴露出来。
## 模块 5：业务连接点（Business Connections）



用户业务定位：卫材（纸尿裤 / 湿巾）创新研发 + 木浆与纸品战略采购。
本章对用户的价值不在纸巾本身，而在于：KC 把「一根辊的雕刻参数」当作产品性能的编程接口，并把这套接口的管理成本（爬坡、测量、图纸）全部内部化了。卫材的功能性涂布（护肤乳液、导流层处理剂、湿巾功能性添加剂）在工艺形态上与之高度同构。

### 连接点 1 — 雕刻辊供应商格局评估：北美 4 家闭环，与国内可替代性分析

涉及幻灯片：SLIDE 22（Key Vendors）、SLIDE 25（5 家图案对比）、SLIDE 28（Harper VIVA 图纸）、Ch4 SLIDE 32/34（VENUS 3 家）、Ch2 SLIDE 10（chrome 6）

核心概念：Key Vendors（A1）；Chrome vs Ceramic engraving（C5）；Engineered Pattern（C1）；Pattern details（C12）

关键数据
| 项 | 值 | 来源 |
|---|---|---|
| KC Key Vendors | 4 家，全部美国（NC / VA / GA / PA） | SLIDE 22 — 文本层（SmartArt） |
| 有图案实绩的雕刻方 | 5 家（+ Saueressig） | SLIDE 25 |
| 测量体系不可比而失效 | 1 家（IR Engraving）→ 可用 = 3 家 | Ch4 SLIDE 34 notes |
| 27 dpi 级深点雕刻的硬门槛 | 辊面 112"（2,844.8 mm）、辊径 20"（508 mm）、深点 0.025" × 0.0227" ±5%（635 × 577 μm）、单穴 27,600,000 μm³ ±5%、旋转 19.6°、双级网点、抛光目标 ≤10,700,000 μm³ | SLIDE 28（T1） |
| 上游强制工序 | 钢辊基体 → 耐蚀堆焊 → 动平衡 → 磨削 → 喷砂 → 等离子喷涂镍铬粘结层 → 等离子喷涂氧化铬/钛陶瓷层 → 磨削抛光 → 激光雕刻 → 最终抛光（10 道，雕刻仅第 9 道） | Ch2 SLIDE 12 |
| 激光物理下限 | ~10 μm 圆孔（相邻孔挤压成六边形，角部受照 ≥3 次 → 必须抛光） | Ch2 SLIDE 14 |
| 计量工具 | Capatch strips（容积/载墨量，可读 BCM/in² 或 cc/m²）／Impression strips（压印/接触）／3DQC measurement system（三维精确测量） | Ch4 SLIDE 37 |

国内可替代性分析 [本报告推导] + 外部背景，非本章内容（以下为评估框架与判定式，不含任何未经核实的国内厂商断言）

本章事实是：KC 的 4 家 Key Vendors 100% 位于北美，且 KC 自己在 VENUS 项目上换过 3 家才拿到合格雕刻。这本身即是「27 dpi 级深点雕刻不是通用能力」的强证据。

对国内承接能力，建议按以下四级判定式逐条实证核验（须由供应商提供实测数据，不得接受口头承诺）：

||||
|---|---|---|
|L0 尺寸能力|能否加工 辊面宽 ≥ 2,844.8 mm、辊径 508 mm 的辊体，并完成动平衡|SLIDE 28 112"×20"；Ch2 SLIDE 12 Dynamic balancing|
|L1 材料能力|是否具备 Bond Coat Plasma Spray = Nickel-Chrome + Ceramic Plasma Spray = Chromium Oxide/titanium 双涂层能力，且耐蚀/耐磨达标|Ch2 SLIDE 12|
|L2 雕刻能力|能否在 27 dpi / 2:1 / 19.6° 点阵上，稳定刻出 0.025"×0.0227" ±5%（635×577 μm ±5%） 的深点 + 0.020" ±5%（508 μm） 的浅点，双级同辊，且单穴容积分别达 27.6×10⁶ μm³ ±5% 与 10.2×10⁶ μm³（−0%/+10%）|SLIDE 28（T1 #19–#25）|
|L3 计量与抛光能力|① 是否具备 3DQC / Capatch / Impression 同等级计量；② 能否把抛光后的浅点平均容积控制在 ≤10,700,000 μm³；③ 能否出具与买方同法的容积报告|SLIDE 28 #31；Ch4 SLIDE 37；Ch4 SLIDE 34 notes|

判断结论 [本报告推导]：L0/L1 属大型辊体制造与热喷涂能力，在国内工业体系中并非稀缺；真正的门槛在 L2（双级网点 + ±5% + 大角度旋转 + 大辊面一致性）与 L3（计量同法）。KC 用 3 家供应商、9 个月首件、21–23 个月才拿到合格 VENUS 雕刻，说明 L2/L3 的爬坡不是采购问题，而是工艺知识积累问题。因此对国内供应商的正确策略不是「能否承接」的二元判断，而是「给多少爬坡周期 + 用哪套计量口径验收」的项目管理问题（见连接点 2、3）。

可执行行动建议
1. 【建立四级准入矩阵】 以上述 L0–L3 判定式为骨架，做成供应商准入打分表，每一级必须附实测报告（三坐标/3D 形貌图 + 容积分布直方图 + 抛光前后对比），不接受样本图片。依据：SLIDE 28 的双级公差与 Ch4 SLIDE 34 的 IR 教训（图片看不出"1/3 陶瓷壳"，必须量化）。
2. 【首件必须做带分级辊】 借鉴 Ch2 SLIDE 10 notes 的 "alternating bands of 2 BCM and 6 BCM" 与 Ch4 SLIDE 36 的 *"Banded gravure rolls can help speed up the iterative process"*：在同一根辊上刻 2–3 个候选规格分区，一次上机同时验证多个参数点，把迭代轮次从 N 次压缩到 1 次。注意 Ch4 SLIDE 36 的警告：*"typically don't produce sellable product – RSR not MSR"*（分段辊通常不产可售品，只做研发）。
3. 【双源 + 地理分离】 鉴于本章 4 家全部在美东，且 Ch2 SLIDE 10 明确 *"vendor options due to chrome 6"*（环保法规会继续压缩镀铬供应），建议：① 主供 + 备供必须分别具备 L0–L3 全能力；② 至少 1 家位于不同法规/物流辖区。
4. 【不要因为「能刻六边形」就认为「能刻 KC 级图案」】 SLIDE 25 证明：同为 90x60 Marinette Engraving，Harper 与 IR Engraving 的形貌差异肉眼可辨，且 IR 被标 3 处缺陷。同一图纸、不同供方、结果不同是本章的核心事实。

### 连接点 2 — 供应商爬坡周期即项目风险：从 9 个月与 15–17.5 个月倒推排期

涉及幻灯片：Ch4 SLIDE 34 notes（9 months）、Ch4 SLIDE 32 notes（Pamarco Q3 2024）、SLIDE 28（VIVA 图纸 8/30/23）、Ch4 SLIDE 29/30（试车日期）

核心概念：Engraving window（Ch2 SLIDE 20 *"Outside the engravers comfort zones"*）；Engineered Pattern（C1）；Banded roll（C4 替代判据）

关键数据
| 周期事件 | 起 → 止 | 时长 | 来源 |
|---|---|---|---|
| Harper 首根 VENUS 辊 | 启动 → 首件 | 9 个月 | Ch4 SLIDE 34 notes（原文） |
| VENUS 从图纸到供应商能力就位 | 10-16-2022 → Q3 2024 | ≈ 21–23 个月 | D21 [本报告推导] |
| VIVA 图纸 → Pamarco 试车 | 8/30/23 → 12/3/24 | 461 天 ≈ 15.1 个月 | D19 [本报告推导] |
| VIVA 图纸 → Apex 试车 | 8/30/23 → 2/12/25 | 532 天 ≈ 17.5 个月 | D20 [本报告推导] |
| 一致性改善拐点 | Pamarco 上线 | Q3 2024 | Ch4 SLIDE 32 notes |
| 试车后仍需返工 | Apex Trial #2（24 h）→ Re-Polish ×3 | 未知（未记录） | Ch4 SLIDE 31 |
| 全部试车结果 | 1100 / 1550 vs 1800 | 均未达标 | Ch4 SLIDE 29/30 notes |

可执行行动建议
1. 【把「雕刻辊」纳入项目关键路径，且按 T−15 个月倒排】 证据：图纸签发 → 首次试车实测 15.1 / 17.5 个月（D19/D20）。建议排期模板：
   - T−15 至 T−12 月：锁定供应商、签署测量协议、发出受控图纸；
   - T−12 至 T−9 月：首件雕刻（预留 9 个月，依据 Harper 实测值）；
   - T−9 至 T−6 月：首件计量 + 抛光迭代（预留 ≥1 轮 Re-Polish ×3，依据 Ch4 SLIDE 31）；
   - T−6 至 T−3 月：上机试车（DuPont Stain 40× + 3D 扫描 + GMT/性能判据）；
   - T−3 至 T0：性能达标确认或第二轮迭代。
2. 【新图案开发必须「先锁定供应商，再冻结设计」】 Ch4 SLIDE 36："Engraver must have at least 1 degree of freedom. Can only specify 2 from volume, depth, and diameter" —— 第三参数必须由供应商的能力决定。若先冻结设计再找供应商，等于把唯一的自由度也锁死，必然重演 *"large volume skew"*。
3. 【预留「并行双供方」预算，不要串行】 本章证据：Harper 失败 → 转 IR → 再转 Pamarco，串行的代价是 21–23 个月。建议：首轮即让 2 家并行刻同一图纸（成本约为串行的 1.5 倍，周期约为串行的 1/2）。SLIDE 25 的四家并排对比正是这种「并行验证」的低成本版本。
4. 【把「9 个月」写进项目风险登记册，并指定触发条件】 触发条件建议：首件容积偏差 > ±5%（SLIDE 28 深点公差）或 抛光后容积 > 10,700,000 μm³（SLIDE 28 抛光目标）→ 立即启动备选供应商。

### 连接点 3 — 测量口径不统一的致命性：IR Engraving 教训与「锁定测量标准」条款

涉及幻灯片：Ch4 SLIDE 34 notes（*"Did not measure volume with same tools so none of the data translated"*）、Ch4 SLIDE 37（Measurement tools）、SLIDE 28（图纸内部单位冲突）、Ch2 SLIDE 17（L/cm vs L/in 事故）、Ch2 SLIDE 19（1 BCM = 10⁹ μm³）

核心概念：BCM volume（C8）；Cell dimensions（C11）；Pattern details（C12）；Engraving window

关键数据
| 失效 | 后果（原文） | 来源 |
|---|---|---|
| 量具不一致 | *"Switched to IR Engraving because Jenks had used them for 2 VIVA rolls / Did not measure volume with same tools so none of the data translated / Struggled with low volumes"* | Ch4 SLIDE 34 notes |
| 换供应商 = 数据归零 | 上表导致 VENUS 项目额外换 2 次供应商（Harper → IR → Pamarco），累计 21–23 个月 | D21 |
| 单位标签错误（本章新发现） | 27,600,000 cubic micrometers **(27.6 bcm)** vs 1 BCM = 10⁹ μm³ → 1000 倍口径矛盾 | SLIDE 28 vs Ch2 SLIDE 19 |
| 历史同型事故 | 180 Lines/cm 与 180 Lines/inch 均标 "6 BCM VOLUME"；180 LCM = 460 LPI，180 LPI = 70 LCM（单穴容积差 6.45× = 2.54²） | Ch2 SLIDE 17 |

可执行行动建议
1. 【合同必须锁定「测量方法 + 量具型号 + 取样规则 + 报告格式」四项，缺一不签】 依据：Ch4 SLIDE 34 notes 的原文教训，以及 Ch4 SLIDE 37 给出的三类工具（Capatch strips / Impression strips / 3DQC）。
2. 【强制「双单位 + 双口径」书写】 任何容积数值必须写成 27,600,000 μm³/穴（= 0.0276 BCM/穴；= X.XX BCM/in² @ 455.65 穴/in²）。禁止裸写 "BCM" —— 依据：Ch2 SLIDE 18 原文即承认 *"More commonly just referred to as BCM"*（丢掉 /in² 正是事故温床），且本章 SLIDE 28 已实证发生 1000× 标签错误。
3. 【建立「 golden roll / golden coupon」传递标准】 用一根双方共同测量过的实体标准辊（或标准试片）作为量值传递基准：新供应商在报价前必须先测该标准件，偏差超 ±X% 即判定量值体系不兼容。这是把 Ch4 SLIDE 34 的教训反向工程为预防手段（[本报告推导]）。
4. 【首件验收做「交叉比对」而非「单方报告」】 要求供应商在首件上随机 3 个区域 × 每区 ≥30 个点出具容积分布（均值、σ、min/max），并由买方用自备量具在同一区域复测。依据：SLIDE 28 的双级公差（浅点 −0%/+10%、深点 ±5%）本身就要求分布级数据，而非单点数据。

### 连接点 4 — 图纸即知识产权：HARPER 图纸的 25 字段对本方建立自有雕刻规格库的意义

涉及幻灯片：SLIDE 28（HARPER VIVA 图纸全字段，见 T1）、Ch4 SLIDE 32（VENUS 图纸）、Ch2 SLIDE 21（参数分类框架）、Ch2 SLIDE 16（标准规格三要素）

核心概念：Pattern details（C12）；Cell dimensions（C11）；DPI / spacing / rotation（C9）；Deep Dot / Shallow Dot（C10）；BCM（C8）

关键数据：SLIDE 28 一张图纸即包含 约 25 个字段，可分为 6 组（T1）：身份与归属（Customer / HCA Job# / KC GR# / XDI # / Date / 签字）→机械包络（Face 112" / Dia 20" / 旋向 / 长轴头 / 传动侧）→雕刻区几何（CENTERED 104.5" / 端部 3.75" / 试烧区）→点阵结构（27 dpi / 2:1 / 19.6° / 四个点距标注 / 倾斜方向注记）→双级穴尺寸与容积 + 非对称公差 + Test Burn Target→抛光目标（以容积表达）。

可执行行动建议
1. 【照抄这 6 组 25 字段，建立本方《雕刻辊规格书模板》】 这是本章最高价值的可迁移资产：它把「一张图说了什么」变成了「一张图必须说什么」。模板建议直接采用 T1 的 #1–#32 字段编号，逐项留空。
2. 【把「抛光目标」写成容积条款】 POLISHING NOTE: Target <= 10,700,000 Shallow Dot Volume Average —— 抛光是可验收的量化条款，不是工艺建议。本方所有陶瓷辊规格书均应照此把抛光写成带数值的验收项（[本报告推导]：否则会重演 Ch4 SLIDE 31 的 Re-Polish ×3 无标准循环）。
3. 【把「倾斜方向」「旋向」「试烧区」这类「非性能字段」也写进规格库】 *Always tilt to the right unless requested otherwise.* / Counterclockwise Rotation / Test Burn Area 2.5" Max Both Ends —— 这些字段不影响性能，但决定装机的物理可用性；漏写会直接导致辊无法上机。
4. 【图纸编号体系自建，不沿用供应商编号】 本章存在两套编号：KC 的 KC GR#5 / XDI #3 与 Harper 的 HCA Job#111233501。本方应建立自有图号 + 供应商工号双轨对照表，避免供应商离职/更换后图纸失联。
5. 【把「双级网穴 + 非对称公差」作为核心 know-how 保护】 VIVA 图的浅点只许偏大（−0%/+10%）、深点双向（±5%）这一细节，是把抛光工艺窗口编码进公差带的做法（[本报告推导]，依据 C10 的抛光余量 +4.90%）。这类「公差带设计」是本方建立技术壁垒的低成本抓手：图纸可以外发，公差带的推导逻辑不外发。

### 模块 5 附：可直接用于供应商准入与采购谈判的条款清单（Clause Checklist）



每条均标注依据来源，可直接复制到 RFQ / 供应商质量协议 / 采购合同。

||||
|---|---|---|
|C-01 计量同法|供应商必须使用与买方同型号的容积测量系统，并提供量值溯源证书；买方有权用自备量具在同一区域复测。首次合作前须通过标准件比对，偏差 > ±5% 视为量值体系不兼容，不予准入。|Ch4 SLIDE 34 notes；Ch4 SLIDE 37；SLIDE 28 深点 ±5%|
|C-02 双单位 + 双口径|所有容积数值必须以 μm³/穴 与 BCM/in² 并列书写，并注明换算所用的点阵密度；禁止单独使用 "BCM" 简称。|Ch2 SLIDE 18/19；SLIDE 28 的 1000× 标签错误（T7-U1）|
|C-03 三参数同锁 + 一个自由度|规格书必须同时写明 Cell geometry（含角度）+ 线数/点密度（含单位）+ 容积（含单位）；最多锁定 {volume, depth, diameter} 中的 2 个，第 3 个由供应商申报其选定值及理由。|Ch2 SLIDE 16；Ch4 SLIDE 36|
|C-04 抛光量化验收|抛光为独立验收项，须以抛光后平均单穴容积表述并设定上限（参照 ≤10,700,000 μm³ 模式）；超过上限即判不合格，返抛光次数与费用归属须事前约定。|SLIDE 28 POLISHING NOTE；Ch4 SLIDE 31 Re-Polish ×3|
|C-05 首件周期与里程碑|合同须载明首件交付周期（建议按 9 个月上限设定，依据 Harper 实测），并设定里程碑违约金；逾期 X 天买方可无偿启用备选供应商。|Ch4 SLIDE 34 notes（9 months）|
|C-06 双源 / 并行首件|对 Engineered Pattern（新图案），买方可要求 2 家供应商并行制作首件，费用按约定分担；供应商不得因此主张排他。|SLIDE 25（四家并排对比）；D21 串行代价 21–23 个月|
|C-07 数据可传承|供应商须以买方指定格式（含均值、σ、min/max、取样位置图、3D 形貌文件）交付全部测量原始数据；换供应商时，买方有权将全部数据移交新供应商，原供应商不得主张数据专有。|Ch4 SLIDE 34 notes（"none of the data translated"）|
|C-08 图纸与 IP|图纸、公差带推导、图案代号（参照 KCP06/KCP08/KCP09）的知识产权归买方；供应商仅得为履行本合同而使用，不得用于其他客户或反向工程展示。|SLIDE 25；SLIDE 28|
|C-09 分段/候选辊|研发阶段供应商须按买方要求在同一辊上制作 ≥2 个规格分区（banded roll），并按分区分别出具测量报告；分段辊不用于商业销售（RSR not MSR）。|Ch2 SLIDE 10 notes；Ch4 SLIDE 36|
|C-10 缺陷判据与验收方法|验收采用染色法 + 3D 形貌双判据（参照 DuPont Stain + 40X Zoom 并排对照）；缺陷以网穴残留/陶瓷壳为否决项（参照 *"1/3 of dot is still filled with ceramic 'shell'"*）。|SLIDE 24；SLIDE 25；Ch4 SLIDE 29/30/34|
|C-11 变更与重复能力|供应商须承诺能重复自己的合格雕刻；因人员/设备/工艺变更导致无法复现者，视为能力缺失，买方有权取消合格供应商资格。|Ch4 SLIDE 34 notes（IR "did not do a good job repeating the preferred engraving"）|
|C-12 产能与库存健康|供应商须申报同规格辊的年产能与最短补货周期；买方有权按「辊库存健康度」设定安全库存并要求供应商寄售。|Ch4 SLIDE 38（"get back to healthy gravure roll inventories"）；SLIDE 23 notes（*can't run without 2 functional gravure rolls*）|
|C-13 环保合规|涉及镀铬平台的，供应商须提供六价铬（Chrome 6）相关合规证明与替代路线图。|Ch2 SLIDE 10（"vendor options due to chrome 6"）|
|C-14 单位事故追责|因单位/口径标注错误导致的返工、停机、报废，损失由标注方承担；买方有权追溯至图纸签发方。|Ch2 SLIDE 17；SLIDE 28（T7）|
## 模块 6：金句索引（Key Quotes Index）

Q1
> "Harper - Charlotte, NC ｜ Precision Roll Solutions/IR Engraving - Richmond, VA ｜ Pamarco - Atlanta, GA ｜ Apex - Pittsburgh, PA"
SLIDE 22 — 文本层（SmartArt, ppt/diagrams/data2.xml）
- 中文翻译：Harper —— 北卡罗来纳州夏洛特｜Precision Roll Solutions/IR Engraving —— 弗吉尼亚州里士满｜Pamarco —— 佐治亚州亚特兰大｜Apex —— 宾夕法尼亚州匹兹堡。
- 为什么记：整个供应基础的全部内容，就这四行。 这是全章唯一的「供应商名单」原文，且以 SmartArt 形式存在（普通文本提取会漏掉）。四个城市全部在美东工业带，零家非北美供应商 —— 这是「供应地理集中度」风险的最硬证据，也是「国产替代可行性」论证的起点。同时它给出关键拼写事实：Precision Roll Solutions 与 IR Engraving 是同一实体的两个名称。

Q2
> "Incredibly complex process. Tissue machine can't run without 2 functional gravure rolls"
SLIDE 23 — SPEAKER NOTES
- 中文翻译：极其复杂的过程。没有 2 根可用的凹版辊，纸机就开不起来。
- 为什么记：全章唯一把设备数量转化为停机风险的句子。2 functional（2 根可用）三个字定义了安全库存的物理下限：不是「有辊就行」，而是「有 2 根合格辊才行」。对采购而言，这直接否定了「单源 + 按需订制」的库存策略，并与 Ch4 SLIDE 38 的 "get back to healthy gravure roll inventories" 构成因果：库存不健康 = 停机风险敞口。

Q3
> "#1 Printer pattern (VIVA® Towel) ｜ Stained sample (DuPont Stain #4) ｜ Red dots = latex ｜ Green = fiber"
SLIDE 24 — 图像内容补充
- 中文翻译：1 号印刷图案（VIVA® 厨房纸巾）｜染色样（DuPont 4 号染色剂）｜红点 = 乳胶｜绿色 = 纤维。
- 为什么记：凹版图案验收方法的完整定义，四个短语讲完一套方法学。它说明图案不是靠肉眼审美评价的，而是靠化学染色 + 颜色编码（红=胶、绿=纤）判读的。这套方法在 Ch4 SLIDE 29/30 被直接复用为供应商试车判据（40× 并排对照）—— 也就是说，本章的图案定义方法 = 后章的供应商验收方法，是「设计即检验」的范例。对湿巾/卫材的功能性涂布同理：先把功能组分染色可见化，验收才有客观判据。

Q4
> "OLU – VIVA Gravure Roll Pattern"
SLIDE 28（幻灯片标题）
- 中文翻译：OLU —— VIVA 凹版辊图案。
- 为什么记：全章信息密度最高的一页的标题，也是本 deck 中唯一一张完整公开的 KC 雕刻制造图纸的索引。它把本章从「供应商名单」推进到「规格实体」：前面 6 页都在讲谁能做，这一页讲到底要做什么。任何建立自有雕刻规格库的工作，都应以这一页的字段结构（见 T1 的 6 组 25 字段）为模板。

Q5
> "27 dpi dot ｜ 2:1 dot spacing ｜ Rotated 19.6° from vertical"
SLIDE 28 — 图像内容补充 与 SLIDE 28 — 二次读图（两源一致）
- 中文翻译：27 dpi 点阵｜2:1 点间距｜相对垂直方向旋转 19.6°。
- 为什么记：KC 工程化图案的「三参数指纹」，也是判定一个图案属于 VIVA 族的唯一充分条件。这 13 个词里藏着三个层次的信息：① 27 dpi 是密度，决定穴数；② 2:1 是间距比，决定穴的形状取向（非等方）；③ 19.6° 是旋转角，决定与纸机/刮刀的干涉关系。三个参数缺一不可 —— 这正是 Ch2 SLIDE 16 三要素（geometry / LPI / volume）在真实图纸上的样子。

Q6
> "DEEP DOT 0.025" x 0.0227" ±5% (0.0237"- 0.0262" x 0.0216" - 0.0238") (635 x 577 microns) ±5% (603μ - 667μ x 548μ - 606μ)"
SLIDE 28 — 二次读图（⚠️ 与既有 图像内容补充 的 0.032" × 0.022" ±10%（0.813 × 0.559mm） 冲突，并列呈现）
- 中文翻译：深点 0.025 英寸 × 0.0227 英寸 ±5%（0.0237–0.0262 英寸 × 0.0216–0.0238 英寸）（635 × 577 微米）±5%（603–667 微米 × 548–606 微米）。
- 为什么记：本章最硬的一个数字串，也是本章最大的一处待澄清。 它同时证明了三件事：① KC 的深点是亚毫米级、双轴非对称（635 μm ≠ 577 μm）的精密特征；② 公差是 ±5%（这是 Ch2 SLIDE 20 "KC's engineered patterns create a tight engraving window" 的量化定义 —— 窗口就是 ±5%）；③ 公差区间与公制换算完全自洽，可作为读图正确性的内证。冲突处置：既有提取记为 0.032"×0.022"±10%，两组读数必须向图纸签发方书面澄清，在此之前不得用于任何设计输入。

Q7
> "VOLUME 27,600,000 cubic micrometers (27.6 bcm)"
SLIDE 28 — 图像内容补充 与 SLIDE 28 — 二次读图（数值一致）
- 中文翻译：容积 27,600,000 立方微米（27.6 bcm）。
- 为什么记：全 deck 最危险的一行字。 它把 27,600,000 与 27.6 bcm 并排写在一起，而按 Ch2 SLIDE 19 的定义（1 BCM = 1,000,000,000 um³），27,600,000 μm³ 只等于 0.0276 BCM —— 同一行内自相矛盾 1000 倍。这一行字同时是三种风险的证据：单位风险（1000×）、口径风险（单穴 vs 整辊未标注）、传承风险（若据此下发图纸，供应商必然做错）。对本方的直接价值：规格书里任何一个容积数字，都必须写明「每穴」还是「每平方英寸」，否则就是给下游埋雷。（本报告的处置与三方验证见 T7-U1 与 D7–D11）

Q8
> "VOLUME 10,200,000 cubic micrometers (10.2bcm) • lower limit -0% (10,200,000) • upper limit +10% (11,220,000) (Test Burn Target +12% 11,424,000)"
SLIDE 28 — 二次读图（既有提取缺失此字段）
- 中文翻译：容积 10,200,000 立方微米（10.2bcm）• 下限 −0%（10,200,000）• 上限 +10%（11,220,000）（试烧目标 +12%，11,424,000）。
- 为什么记：公差带设计的教科书级范例。 浅点的公差是非对称的（−0% / +10%），与深点的对称 ±5% 形成鲜明对比。为什么？因为浅点是抛光工序的消耗对象：抛光会减小容积，所以下偏差给 0（不许偏小），上偏差给 +10%（留出抛光余量）。更深一层：试烧目标 +12% 甚至超出生产上限 +10%，说明「试烧区」是一个有意放宽的参照区（[本报告推导]）。一句话包含三个层次的设计意图 —— 这正是「图纸即知识产权」的最佳注脚：把工艺窗口编码进公差带。

Q9
> "POLISHING NOTE: Target <= 10,700,000 Shallow Dot Volume Average"
SLIDE 28 — 图像内容补充 与 SLIDE 28 — 二次读图（两源措辞完全一致）
- 中文翻译：抛光注记：目标 —— 浅点平均容积 ≤ 10,700,000（立方微米）。
- 为什么记：把「抛光」从工艺建议变成合同条款的那一行字。 它做了三件事：① 抛光被写成验收项，不是推荐做法；② 验收量是抛光后的平均单穴容积（而非粗糙度、非外观）；③ 阈值 10,700,000 恰好是浅点名义值 10,200,000 的 +4.90%（[本报告推导]），即抛光余量被量化写进了图纸。对照 Ch4 SLIDE 31 的 Apex Re-Polish #1/#2/#3 —— 没有这种条款，抛光就是无限循环。

Q10
> *"Always tilt to the right unless requested otherwise."
SLIDE 28 — 二次读图（既有提取缺失）
- 中文翻译：除非另有要求，一律向右倾斜。
- 为什么记：最容易被规格库漏掉、却最常导致装机失败的一类字段。 它不影响任何产品性能（不影响 GMT、不影响涂布量），只影响图案在辊面上的物理取向；但漏写它，辊就可能装反、图案镜像、甚至与刮刀形成规则干涉。它证明了一件事：一份完整的雕刻规格 = 性能参数 + 物理取向参数 + 工艺注记，三者缺一不可。本方建规格库时，应单列「非性能字段」一栏专门收纳这类条款。

Q11
> "Saueressig – KCP06"
SLIDE 25（文本框原文）
- 中文翻译：Saueressig（绍尔西希）—— KCP06（图案代号）。
- 为什么记：整章最容易被忽略的结构性证据。 它出现在 SLIDE 25 的大图位（被当作正面参照展示），却不在 SLIDE 22 的 Key Vendors 四家名单里。这说明：「有图案实绩的雕刻方」≥ 5 家，「Key Vendors」= 4 家，两者是不同的口径。对采购的启示：评估供应基础时，不能只看合格供应商名录，还要统计「实际持有本方图案的厂商」—— 后者往往更大，也意味着图纸外流面比名录更广（IP 管理盲区）。

Q12
> "Harper 90x60 Marinette Engraving ｜ Pamarco – KCP08 ｜ APEX – KCP09 ｜ IR Engraving 90x60 Marinette Engraving"
SLIDE 25 — 二次读图
- 中文翻译：Harper 90x60 Marinette 雕刻｜Pamarco – KCP08｜APEX – KCP09｜IR Engraving 90x60 Marinette 雕刻。
- 为什么记：同一命题的四种答案，被并排放在一页上。 四个面板，四种形貌：Harper 粗糙、Pamarco 洁净均匀、APEX 独立代号、IR Engraving 被红圈标 3 处缺陷。这是全章对「同一图纸 ≠ 同一结果」最直观的证明，也是 Ch2 SLIDE 20 "Outside the engravers comfort zones" 的实物化：越界的东西，不同人会做成不同样子。对战略采购的直接含义：雕刻辊不能按通用件招标，必须按「谁做过这个图案」招标。

Q13
> "Jenks & BIL OLU Process: Tissue Machine ← Unwind → Printer (Backing Roll / Gravure Roll / Air Layer / Print Fluid Delivery / Print Fluid Make-up System) → Pressure Roll → Crepe Dryer → Crepe Blade → Reel → Converting Line"
SLIDE 26 — 图像内容补充 + SLIDE 26 — 二次读图
- 中文翻译：Jenks 与 BIL 的 OLU 工艺：纸机 ← 退卷 → 印刷站（背压辊 / 凹版辊 / 气垫层 / 印刷液输送 / 印刷液配制系统）→ 压辊 → 起皱烘缸 → 起皱刮刀 → 卷取 → 加工线。
- 为什么记：凹版辊的「工位全景图」，也是计算「一根辊撬动多少资产」的分母。 一条线上，凹版辊只是 11 个节点中的一个，但它前面的 Print Fluid Make-up System、后面的 Crepe Dryer → Crepe Blade → Reel → Converting Line 全部依赖它的输出质量。一根价值有限的辊，卡住的是整条线的产品性能与开机率 —— 这就是 Ch1 SLIDE 2 说它是 "Heart" of printing/coating process 的物理依据，也是「选供应商不能只看单价」的量化前提。

Q14（跨章锚点，VENUS 项目）
> "Harper took 9 months to engrave first roll and then had a large volume skew ｜ Switched to IR Engraving because Jenks had used them for 2 VIVA rolls ｜ Did not measure volume with same tools so none of the data translated ｜ Struggled with low volumes ｜ Ran a banded roll and then IR Engraving did not do a good job repeating the preferred engraving so switched to Pamarco ｜ Pamarco has shown promise with strong engraving plan and enforcement. Moving fast to meet pre-determined trial dates has created some non-ideal engravings"
Ch4 SLIDE 34 — SPEAKER NOTES（Ch4 内容，作为本章结论的下游兑现而引用）
- 中文翻译：Harper 花 9 个月刻出第一根辊，之后出现大幅体积偏差。因 Jenks 曾用 IR Engraving 做过 2 根 VIVA 辊而转投 IR；但 IR 用不同的工具测量体积，所以数据完全无法对应；体积持续偏低；试过一根分段辊，IR 未能很好地复现首选雕刻，于是转投 Pamarco。Pamarco 表现出希望，雕刻计划与执行都很强。但为赶既定试车日期而快速推进，产生了部分不理想的雕刻。
- 为什么记：整个 Gravure Roll 101 中信息量最大的一段备注，是理解本章供应格局的钥匙。 它用 6 句话讲完了一个 21–23 个月、换 3 家供应商的失败史，并点出四种不同的失效模式：① 周期失控（9 个月）；② 量值不可比（*"none of the data translated"*，最致命）；③ 不可重复性（*"did not do a good job repeating"*）；④ 进度压力压垮质量（*"Moving fast to meet pre-determined trial dates"*）。最后一条尤其反直觉：不是供应商能力不足，而是买方自己定的试车日期把质量压垮了 —— 这对任何做新图案开发的排期都是一记警钟。

Q15（跨章锚点，战略意图）
> "New vendors are learning with KC as we attempt to get back to healthy gravure roll inventories and look to ignite innovation"
Ch4 SLIDE 38 — 文本层（SmartArt, ppt/diagrams/data3.xml）
- 中文翻译：新供应商正在与 KC 一起学习，我们正试图恢复健康的凹版辊库存，并重新点燃创新。
- 为什么记：全 deck 最诚实的一句，也是本章供应格局的最终解释。 三个信息：① "New vendors are learning with KC" —— SLIDE 22 的 4 家不是成熟供应，是正在学习的新供方（KC 为此支付学费）；② "get back to healthy gravure roll inventories" —— 承认当前库存不健康，这是 SLIDE 23 notes "can't run without 2 functional gravure rolls" 的风险敞口；③ "ignite innovation" —— 把「辊库存」与「创新」直接挂钩：没有健康的辊供应，就没有新图案、新产品。对本方的战略映射：如果一个品类（如卫材的功能性涂布辊/网纹辊）的供应基础需要「边用边教」，那么创新节奏就由供应商的学习曲线决定，而不是由研发排期决定。


## 附录：本报告的 [未找到原句] 汇总与待澄清清单

### A. 源材料中不存在的字段（任务书提及，经全 deck 检索确认零命中）

||||
|---|---|---|
|1|HARPERLASER（图纸标识字符串）|SLIDE 28 全图（四象限 + 顶部分条 ×3 放大）|[未找到原句]（可读品牌为 HARPER®）|
|2|128x20（辊面规格）|同上|[未找到原句]（实际为 112" × 20"）|
|3|LOCATION（图纸独立字段）|同上|[未找到原句]（可追溯字段为 Customer Retroflex / KC）|
|4|0.070" deep dots spacing|同上|[未找到原句]（图纸可读点距为 0.033127" / 0.066254" / 0.265015" / 0.148148"）|
|5|0.250" border|同上|[未找到原句]|
|6|3.050 与 3.0364（光面尺寸）|同上|[未找到原句]|
|7|「过去几年做过的辊」六条清单（Specialty Coated Blue Wrap / VIVA Signature Cloth ×3 / VENUS Bath Tissue ×2）|文本层 + SmartArt XML + 38 页图像 + 视频 9 帧|[未找到原句]（"Specialty Coated Blue Wrap" 一词零命中）|
|8|Pictured below is the newest VIVA roll for Beech Island made by Harper|同上|[未找到原句]|
|9|Beech Island|同上|[未找到原句]（零命中）|
|10|KC 各厂 → 雕刻商的指派分布表|同上|[未找到原句]（源材料仅提供「项目 × 雕刻方」映射，见 T5）|
|11|Decorative pattern / Combining patterns（图案分类术语）|同上|[未找到原句]（deck 中的图案分类只有 Engineered patterns - DRC/OLU/Facial 与 6 种标准 anilox）|
|12|mechanical engraving 示意（本章）|SLIDE 27 视频 9 帧|[未找到原句]（视频为在产涂布工位，无雕刻设备、无文字）|
|13|Saueressig 的所在地|全部|[未找到原句]（既有报告称「欧洲」，本章无原文支撑）|
|14|VIVA 图纸的 Cell depth 直接标注|SLIDE 28 全图|[未找到原句]（仅可由容积反算，见 D13）|

### B. 待澄清清单（建议向图纸签发方 / KC 书面确认）

||||
|---|---|---|
|1|VIVA Deep Dot 尺寸|0.032"×0.022" ±10% vs 0.025"×0.0227" ±5%|倾向后者（公差区间与公制换算自洽），但不作单方取舍|
|2|VIVA Top / Test Burn Area|栏名 Top vs Test；数值 3.5" vs 2.5"|待定|
|3|VIVA 27.6 bcm 标签口径|图纸标签 vs 1 BCM = 10⁹ μm³|判定为 1000× 标签错误（三方验证：6.23 / 5.65 / 6.0 BCM 同量级）|
|4|VIVA Deep Dot Test Burn 符号|标注 -5%，数值 28,980,000（= +5%）|符号存疑，数值算术自洽|
|5|1.25 点阵系数的物理解释|两图案均满足 dots/in² = 1.25 × dpi² ÷ 间距比|假设：深点 = 浅点 ÷ 4（25%），[本报告推导]，需设计方确认|
|6|27 dpi vs 标注节距|(1/27) ÷ 0.033127 = √1.25|与 #5 同一现象|
|7|VENUS 点距标注口径|0.02926"/0.02926"/0.01463" vs 0.02926"/0.051852"/0.14493"/0.25926"|后者内部自洽（0.25926 = 5 × 0.051852）|
|8|VIVA Flat Burn Target < ±10%|仅见既有提取，二次读图未复现|待复核原图|
|9|Harper 50 周年徽标年份|两次读图分别为 1973-2023 与 1974-2024|不影响技术参数，仅作记录|

报告完成说明：本报告全部数据均来自 /sandbox/workspace/uploads/Gravure Roll 101.pptx（Gravure Roll 101, KC Capability Days 2025, 38 页）与 /sandbox/workspace/Ebook_Extract/Gravure_Roll_101/chapters/ 下的四个章节文件；涉及 Ch2 / Ch4 的引用均显式标注章节与页码。所有 [本报告推导] 数值均附完整算式（见 T8，D1–D23）。未在本源材料中出现的内容一律标注 [未找到原句]，不作任何补白或推测性填充。


---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_1168509591a5d3abb8b7e860030cb2a2001a693ee6c0644e"
source_file: "Gravure_Roll_101_ch2_Engraving_and_Specs_拆解报告.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch2_Engraving_and_Specs_拆解报告.md.md"
extracted: "2026-09-30"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
---

# Gravure_Roll_101_ch2_Engraving_and_Specs_拆解报告.md


章节：Ch2 Engraving & Specs ｜ 覆盖幻灯片：10–21 ｜ 文档：Gravure Roll 101 (KC, Capability Days 2025) ｜ 拆解日期：2026-08-30

# Gravure Roll 101 — Ch2 Engraving & Specs：学术级章节拆解报告

Source integrity rules applied in this report
- Every claim is tagged with its evidence: SLIDE N (slide text layer), SLIDE N — SPEAKER NOTES (presenter notes), or SLIDE N — 图像内容补充 (data extracted from rendered slide images).
- Where the chapter contains no supporting statement, the tag [未找到原句] is used and no data is invented.
- Where a number is calculated by this report, the tag [本报告推导] is used with the full arithmetic chain shown.
- Nothing outside the four chapter files is asserted as chapter content; general engineering/chemistry background is explicitly flagged as 本报告推导 / 外部背景，非本章内容.

## 模块 1：核心论点（Core Arguments）

### A1. KC runs a two-platform engraving strategy, and the split is a deliberate cost-vs-capability trade-off, not a legacy accident



英语原文摘要：KC's gravure fleet is deliberately split into Electro-mechanical Engraved Chrome Rolls (Facial) and Laser Engraved Ceramic Rolls (OLU/DRC/ELCs). The two platforms are positioned against each other on exactly five axes: cost, engraving life, engraving flexibility, transfer consistency, and vendor availability.

||||
|---|---|---|
|Cost|lower cost|Higher cost|
|Engraving life|shorter engraving life|longer engraving life|
|Engraving flexibility|engraving limitations|more engraving flexibility|
|Transfer precision|variability due to plating inconsistency|more precise and consistent fluid transfer|
|Supply base|vendor options due to chrome 6|vendor competition|


- SLIDE 10："Electro-mechanical Engraved Chrome Rolls (Facial) — Pros - lower cost / Cons - shorter engraving life, engraving limitations, variability due to plating inconsistency, vendor options due to chrome 6"
- SLIDE 11："Laser Engraved Ceramic Rolls (OLU/DRC/ELCs) — Pros - More resistant to corrosion and abrasion, longer engraving life, more engraving flexibility, more precise and consistent fluid transfer, vendor competition / Cons - Higher cost"
- 支撑依据：the two slides are structurally mirrored — ceramic carries 5 pros / 1 con, chrome carries 1 pro / 4 cons, and the two Cons lists are near-exact mirrors of each other. This symmetry is the chapter's explicit proposition that the choice is a managed trade, not a technology upgrade path.
### A2. Ceramic roll performance is manufactured, not merely engraved — laser engraving is only step 9 of 10



英语原文摘要：The performance of a laser-engraved ceramic roll is produced by a 10-step production chain in which laser engraving is only the 9th step. Four steps precede surface preparation (steel base → corrosion welding → dynamic balancing → grinding → sand blasting → bond coat → ceramic coat → grind/polish) and one step follows it (Final polishing). Engraving quality is therefore bounded upstream by coating adhesion and downstream by polishing capability.

- SLIDE 12："Ceramic Gravure Roll Production — Steel roll base / Corrosion resistance welding (if necessary) / Dynamic balancing / Grinding / Sand blasting / Bond Coat Plasma Spray = Nickel-Chrome / Ceramic Plasma Spray = Chromium Oxide/titanium / Grinding/Polishing / Laser engraving / Final polishing"
- SLIDE 12 — SPEAKER NOTES："Graphics programming and repeat calculations for complex patterns"
- SLIDE 15 — SPEAKER NOTES："Ceramic roll in the laser bed"
- 支撑依据：SLIDE 20 independently confirms that the downstream step is the constraint for KC: "Large amount of unengraved area = more complex polishing". The chapter thus argues that polishing is a co-equal process capability with engraving itself.
### A3. A gravure roll specification is three-dimensional; quoting volume alone is a specification failure



英语原文摘要：Cell geometry, lines per inch, and cell volume are three independent specification axes. Volume is an area-normalised integral and therefore collapses an infinite family of cell geometries into one number. Two rolls can both be "6 BCM" and be functionally unrelated.

- SLIDE 16："Standard Engraving Specifications — Cell geometry, lines per inch, cell volume" ＋ "2 ply bath specification = 60 degree hex, 180 LPI, 6.0 BCM"
- SLIDE 18："Total volume of all the engraved cells on the roll surface per unit area of the surface"
- 支撑依据（事故实证）：SLIDE 17 documents a real KC incident in which 180 Lines/cm and 180 Lines/inch were both labelled "BOTH '6 BCM VOLUME'" while the cell size and density were completely different. SLIDE 17 — SPEAKER NOTES："180 LCM = 460 LPI and 180 LPI = 70 LCM".
### A4. KC's rolls sit outside the engraving industry's normal process window, which forces KC to own the translation from product property to cell dimension



英语原文摘要：KC gravure rolls are characterised by engineered patterns, "Deep" engravings, "Large" cells, and large unengraved areas — all described as "Outside the engravers comfort zones". Because engravers see only cell dimensions, KC must communicate the engraving specifications required to create product properties.

- SLIDE 20："Unique KC Gravure rolls — This is where the MAGIC happens / Engineered patterns - DRC/OLU/Facial / Outside the engravers comfort zones / 'Deep' engravings / 'Large' cells / Large amount of unengraved area = more complex polishing / Not just printing/coating …. Creating product properties"
- SLIDE 20 — SPEAKER NOTES："KC has to be able to communicate the engraving specifications required to create product properties. Engravers have no insight beyond the cell dimensions"
- SLIDE 21："Engraving Specifications – Unique KC Engravings" — two parameter boxes: Cell dimensions (Cell diameter / Cell depth / Cell volume) and Pattern details (Shapes, sizes, spacing) SLIDE 21 — 图像内容补充
- 支撑依据：the chapter gives KC's specification vocabulary as 6 parameters across 2 boxes, i.e. KC's specification burden is structurally larger than the 3 standard parameters on SLIDE 16.
### A5. The laser process itself creates a mandatory, non-optional finishing step that links cell geometry directly to doctor blade wear



英语原文摘要：A circular laser beam creates a ~10 μm round hole; each subsequent hole pushes the cell walls into a hexagon; each corner is exposed to the laser a minimum of 3 times versus the side walls, creating raised peaks in the corners. Polishing is required to remove those peaks — otherwise excessive doctor blade wear.

- SLIDE 14："Circular laser beam that creates ~10 um round hole / Engraving each subsequent hole pushes the cell walls to create a hexagon shape / Each corner is exposed to the laser a minimum of 3 times compared to the side walls / Raised peaks are created in the corners / Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear"
- 支撑依据：this is the only place in the chapter where a physical mechanism (laser overlap geometry) is explicitly tied to an operating cost consequence (doctor blade wear) — i.e. cell geometry → maintenance cost is a documented causal chain, not an inference.
## 模块 2：关键概念操作化定义（Key Concepts with Operational Definitions）



本模块共 12 个概念，覆盖任务指定全部必含项。所有 (d) 项为英文原文摘录；推导项标 本报告推导。

### C1. Electro-mechanical Engraved Chrome Roll ｜ 机电雕刻镀铬辊

(a) 中文名 + English term：机电雕刻镀铬辊 / Electro-mechanical Engraved Chrome Roll（chapter sub-type: *(Facial)*）

(b) English definition
> A gravure roll whose cell pattern is cut mechanically (electro-mechanical stylus) into an electroplated chrome layer, used on KC's Facial assets. Positioned as the lower-cost platform with shorter engraving life, engraving limitations, and variability due to plating inconsistency.

(c) 操作化定义（Operational definition）
- 判定维度：① substrate/engraving layer = electroplated chrome (not plasma-sprayed ceramic); ② pattern generation = electro-mechanical (stylus), not laser; ③ application scope = Facial (SLIDE 10).
- 量化指标（原文给出，无数值）：cost ↓ / engraving life ↓ / engraving flexibility ↓ / transfer consistency ↓ / vendor options ↓.
- 一致性判据：SLIDE 10 attributes roll-to-roll variability to plating inconsistency — i.e. the measurable risk variable is plating bath/layer uniformity, and roll-to-roll volume scatter is the acceptance metric. The chapter gives no numeric tolerance for this platform → [未找到原句] for any tolerance value.

(d) 原文英文摘录
> "Electro-mechanical Engraved Chrome Rolls (Facial) — Pros - lower cost / Cons - shorter engraving life, engraving limitations, variability due to plating inconsistency, vendor options due to chrome 6" — SLIDE 10

### C2. Laser Engraved Ceramic Roll ｜ 激光雕刻陶瓷辊

(a) 中文名 + English term：激光雕刻陶瓷辊 / Laser Engraved Ceramic Roll（chapter sub-type: *(OLU/DRC/ELCs)*）

(b) English definition
> A gravure roll whose cells are ablated by a circular laser beam into a plasma-sprayed ceramic layer, used on KC's OLU / DRC / ELC assets. Positioned as higher cost but more resistant to corrosion and abrasion, longer engraving life, more engraving flexibility, more precise and consistent fluid transfer, and supported by vendor competition.

(c) 操作化定义
- 判定维度：① engraving layer = plasma-sprayed ceramic (Chromium Oxide/titanium over Nickel-Chrome bond coat, SLIDE 12); ② pattern generation = laser (SLIDE 14); ③ application scope = OLU/DRC/ELCs (SLIDE 11).
- 量化指标（原文给出）：laser spot ≈ 10 μm diameter; corner laser exposure ≥ 3× side-wall exposure (SLIDE 14).
- 强制后置工序：Final polishing (SLIDE 12) — a roll that has been laser-engraved but not finally polished is a non-conforming roll (corner peaks remain → excessive doctor blade wear, SLIDE 14).
- 与 C1 的互斥性：SLIDE 10/11 assign the two platforms to disjoint asset sets (Facial vs OLU/DRC/ELCs). Neither slide states a case where they are interchangeable → [未找到原句] for any stated substitution rule.

(d) 原文英文摘录
> "Laser Engraved Ceramic Rolls (OLU/DRC/ELCs) — Pros - More resistant to corrosion and abrasion, longer engraving life, more engraving flexibility, more precise and consistent fluid transfer, vendor competition / Cons - Higher cost" — SLIDE 11

### C3. BCM (Billion Cubic Microns) ｜ 十亿立方微米（美制凹版辊体积单位）

(a) 中文名 + English term：十亿立方微米 / BCM = Billion Cubic Microns (Micrometers)；完整单位为 BCM/in²

(b) English definition
> The USA unit for gravure roll volume: the total volume of all the engraved cells on the roll surface per unit area of the surface, expressed in billions of cubic microns per square inch. Commonly shortened to just "BCM", which drops the /in² and is therefore the root cause of the SLIDE 17 unit incident.

(c) 操作化定义
- 测量维度：volume of all cells ÷ roll surface area；单位 BCM/in²。
- 判定公式：
  - 1 BCM = 1,000,000,000 μm³ （SLIDE 19 原文）
  - 1,000 μm = 1 mm （SLIDE 19 原文）
  - 自洽性验证：1 BCM = 10⁹ μm³ = (10³ μm)³ = (1 mm)³ = 1 mm³ → 1 BCM = 1 mm³，自洽成立 本报告推导
  - 以 SI 复核 [本报告推导]：10⁹ μm³ × (10⁻⁶ m/μm)³ = 10⁹ × 10⁻¹⁸ m³ = 10⁻⁹ m³；1 mm³ = (10⁻³ m)³ = 10⁻⁹ m³ → 10⁻⁹ m³ = 10⁻⁹ m³ ✔ 完全自洽
- 量化指标：KC 实际使用值 = 2.0 BCM（Facial lotion band）、6.0 BCM（Facial lotion band 与 2-ply bath spec）（SLIDE 10 notes / SLIDE 16）

(d) 原文英文摘录
> "USA = BCM/in2 ……. More commonly just referred to as BCM" — SLIDE 18
> "1 Billion Cubic Microns (Micrometers) / 1 BCM = 1,000,000,000 um3 / 1000um / 1000 um / 1000 um / 1,000 um = 1 mm / 1 mm / 1 mm / 1 mm" — SLIDE 19

### C4. cm³/m² ｜ 立方厘米每平方米（欧制凹版辊体积单位）

(a) 中文名 + English term：立方厘米每平方米 / cm³/m²（European unit）

(b) English definition
> The European unit for gravure roll volume: the same physical quantity as BCM/in² — total engraved cell volume per unit surface area — expressed in cubic centimetres per square metre.

(c) 操作化定义
- 测量维度：identical physical dimension to BCM/in²（均为「体积/面积」= 长度）；两者仅差一个纯数换算因子。
- 判定公式（原文值）：1 BCM/in² = 1.55 cm³/m² （SLIDE 18）
- 完整换算推导 [本报告推导]（逐步算式）：
  1. 1 in = 25.4 mm = 2.54 cm（定义值）
  2. 1 in² = (2.54 cm)² = 6.4516 cm² = 6.4516 × 10⁻⁴ m²
  3. 1 BCM = 10⁹ μm³ = 1 mm³ = 10⁻³ cm³（见 C3 自洽验证）
  4. 1 BCM/in² = 10⁻³ cm³ ÷ (6.4516 × 10⁻⁴ m²)
  5. = 0.001 ÷ 0.00064516 = 1.55000310… cm³/m²
  6. → 1.5500 ≈ 1.55 cm³/m² ✔ 与 SLIDE 18 原文值一致，原文换算因子验证通过。
- 衍生工程解读 [本报告推导]：因 1 cm³/m² = 10⁻⁶ m³/m² = 10⁻⁶ m = 1 μm，故
  1 BCM/in² = 1.55 cm³/m² = **1.55 μm** 平均湿膜厚度（假设 100% 转移）
  → 6.0 BCM = 9.30 cm³/m² = 9.30 μm；2.0 BCM = 3.10 cm³/m² = 3.10 μm。
  该等式把「辊体积单位」直接翻译成「涂布量/克重的湿膜厚度」，是规格书可使用的交叉校验工具。
- ⚠️ 单位风险：美国用法把公制（micron）与英制（inch²）混在同一单位里 —— SLIDE 18 — SPEAKER NOTES：*"USA combines metric and English units"*。这是 SLIDE 17 事故的单位学根源。

(d) 原文英文摘录
> "Gravure Roll Volume — Total volume of all the engraved cells on the roll surface per unit area of the surface / USA = BCM/in2 ……. More commonly just referred to as BCM / European = cm3/m2 / Conversion: / 1 BCM/in2 = 1.55 cm3/m2" — SLIDE 18

### C5. Line Screen / LPI (Lines Per Inch) / LPcm (Lines Per cm) ｜ 网线数（每英寸线数 / 每厘米线数）

(a) 中文名 + English term：网线数 / Line Screen；单位 LPI = Lines Per Inch、LPcm (LCM) = Lines Per cm

(b) English definition
> Line Screen is the number of cells per linear inch — a count of cells along a straight line, not an area density.

(c) 操作化定义
- 测量维度：# of cells per linear inch（线密度，非面密度）。
- 判定公式：
  - 单位换算：LPI = LPcm × 2.54；LPcm = LPI ÷ 2.54 [本报告推导]
  - 原文验证 SLIDE 17 — SPEAKER NOTES："180 LCM = 460 LPI and 180 LPI = 70 LCM"
    - 180 × 2.54 = 457.2 → 原文取整为 460 LPI ✔（误差 +0.6%）
    - 180 ÷ 2.54 = 70.866 → 原文取整为 70 LCM ✔（误差 −1.2%）
  - 网穴中心距（pitch）：p = 25.4 mm ÷ LPI [本报告推导]
    - 180 LPI → p = 25.4 ÷ 180 = 0.14111 mm = 141.1 μm
    - 457.2 LPI → p = 25.4 ÷ 457.2 = 0.05556 mm = 55.56 μm
  - 60° 六边形阵列面密度：N = L² ÷ sin60° = L² ÷ 0.8660 = 1.1547 L²（cells/in²）[本报告推导]
    - 180 LPI → N = 1.1547 × 180² = 37,412 cells/in²
    - 457.2 LPI → N = 1.1547 × 457.2² = 241,369 cells/in²
    - 70.87 LPcm → N = 1.1547 × 70.866² = 5,799 cells/cm²
  - 单穴体积：V_cell = V_total ÷ N；因 V_cell ∝ 1/L²，当总 BCM 固定时，线数换算错误 ×2.54 会导致单穴体积错误 ×6.45（2.54² = 6.4516）[本报告推导]
- 量化指标（原文图注实例）：SLIDE 16 — 图像内容补充 给出点阵示例 12 lines per inch，并以 11 Cells Per Inch（黄） 与 7 Cells Per Inch（绿） 作对照，旁标注 *"Line Screen is the # of Cells per Linear Inch"*。

(d) 原文英文摘录
> "Line Screen is the # of Cells per Linear Inch" — SLIDE 16 — 图像内容补充（含 12 lines per inch 点阵与英寸刻度尺；11 Cells Per Inch 黄 / 7 Cells Per Inch 绿）

### C6. Cell geometry (60° hex) & Cell Wall ｜ 网穴几何（60° 六边形）与网穴壁

(a) 中文名 + English term：网穴几何（60° 六边形 / 60 degree hex）＋ 网穴壁 / Cell Wall

(b) English definition
> Cell geometry is the first of the three standard engraving specifications. KC's 2-ply bath specification is a 60 degree hex — a hexagonal cell array with a 60° included angle, in which the Cell Wall is the un-engraved ceramic ridge that separates adjacent cells. Under laser engraving the hexagon is not milled but formed: a ~10 μm round hole is pushed into a hexagon by the pressure of adjacent holes.

(c) 操作化定义
- 测量维度：① array angle (60 degree) ② cell wall width ③ 阵列拓扑（hex / trihelical / channellox 等）。
- 判定公式：
  - 60° hex 阵列中，相邻网穴中心距 p 与线数关系见 C5；六边形面积（across-flats = p）：A_hex = (√3/2) p² = 0.8660 p² [本报告推导]
  - 面密度交叉校验：N × 0.8660 p² = 1.1547 L² × 0.8660 × (1/L)² = 1.0 → 即 60° 六边形在零网穴壁理想下恰好铺满平面 [本报告推导]
  - 由此得一个强结论 [本报告推导]：理想铺满时，单位面积体积在数值上等于等效平均槽深。
    h = 6.0 BCM/in² = 6 × 10⁹ μm³ ÷ (25.4 × 10³ μm)² = 6×10⁹ ÷ 6.4516×10⁸ = **9.30 μm**
    → 与 C4 的 6 BCM = 9.30 μm 湿膜 完全一致，构成一条独立的自洽校验链。
- 量化指标（原文给出）：几何角 = 60 degree；阵列 = hex（SLIDE 16）。网穴壁宽度的具体数值本章未给出 → [未找到原句]。
- Cell Wall 的工艺角色：SLIDE 14 明确指出网穴壁是被后续孔挤压而形成的：*"Engraving each subsequent hole pushes the cell walls to create a hexagon shape"*。即网穴壁不是设计出来的余量，而是激光重叠的副产物，其完整性直接决定网穴能否保持容积。

(d) 原文英文摘录
> "2 ply bath specification = 60 degree hex, 180 LPI, 6.0 BCM" — SLIDE 16
> "Engraving each subsequent hole pushes the cell walls to create a hexagon shape" — SLIDE 14
> "60 度六边形几何（标注 Cell Wall、60 Degree Angle）" — SLIDE 16 — 图像内容补充

### C7. Cell diameter / Cell depth / Cell volume ｜ 网穴直径 / 网穴深度 / 网穴容积

(a) 中文名 + English term：网穴直径 / 网穴深度 / 网穴容积 / Cell diameter / Cell depth / Cell volume（SLIDE 21 紫框 Cell dimensions）

(b) English definition
> The three cell-dimension parameters that KC must specify for its unique engravings, grouped in the Cell dimensions box on SLIDE 21, as distinct from the Pattern details box (Shapes, sizes, spacing).

(c) 操作化定义
- 测量维度：① diameter = 网穴开口横向尺寸 ② depth = 网穴深度（Z 向） ③ volume = 单穴容积（μm³）。
- 三者关系：V = f(diameter, depth, shape) → 三个参数中只能独立指定两个，第三个由几何决定（该约束的明确表述在 Ch4 SLIDE 36：*"Engraver must have at least 1 degree of freedom. Can only specify 2 from the key engraving parameters of volume, depth, and diameter"*）。
- 产品属性映射 [本报告推导]，依据 Ch4 SLIDE 35：
  - Cell diameter → X/Y 方向表面覆盖 → GMT（Ch4 SLIDE 35：*"X and Y direction sheet surface coverage - Key to GMT (Cell diameter)"*）
  - Cell depth → Z 方向渗透 → VIVA/WypAll Z 剥离强度（Ch4 SLIDE 35：*"Z direction sheet penetration - Key to VIVA/WypAll Z peel strength (Cell depth)"*）
- 量化指标：SLIDE 21 — 图像内容补充 明确 该页无具体数值表，仅列参数类别 → 本章 Ch2 未给出 KC 独有雕刻的数值。跨章参照值（Ch3，非本章）：VIVA Deep Dot 0.032" × 0.022" ±10%（0.813 × 0.559 mm），Volume 27,600,000 cubic microns；VENUS Target Volume 3,800,000 μm³ ±5%。

(d) 原文英文摘录
> "Engraving Specifications – Unique KC Engravings" — SLIDE 21（紫框 Cell dimensions：Cell diameter / Cell depth / Cell volume；绿框 Pattern details：Shapes, sizes, spacing）
> "Standard Engraving Specifications — Cell geometry, lines per inch, cell volume" — SLIDE 16

### C8. Bond Coat Plasma Spray (Nickel-Chrome) ｜ 等离子喷涂粘结层（镍铬）

(a) 中文名 + English term：等离子喷涂粘结层（镍铬）/ Bond Coat Plasma Spray = Nickel-Chrome

(b) English definition
> Step 6 of the 10-step ceramic gravure roll production process: a Nickel-Chrome layer applied by plasma spray onto the prepared (ground + sand-blasted) steel roll base, serving as the bonding interlayer between the steel substrate and the ceramic topcoat.

(c) 操作化定义
- 测量维度：① 材料 = Nickel-Chrome ② 工艺 = Plasma Spray ③ 顺序位置 = Step 6 / 10，且必须在 Sand blasting（Step 5）之后、Ceramic Plasma Spray（Step 7）之前。
- 判定公式/量化指标：本章未给出粘结层厚度、结合强度或孔隙率数值 → [未找到原句]。
- 工艺必要性 [本报告推导]：Step 5（Sand blasting）与 Step 6（Bond Coat）在流程上直接相邻，且 Step 7 陶瓷层是脆性的；该顺序支持「喷砂 → 提高表面积/锚固 → 镍铬粘结层 → 陶瓷面层」这一功能链。但本章原文未陈述此机理，故标为推导。
- 失效模式 [本报告推导]：作为中间层，其质量不直接暴露，失效将表现为陶瓷面层剥落；Ch3 图像内容补充 中 *"1/3 of dot is still filled with ceramic 'shell'"*（IR Engraving VENUS CT5）与 *"No ceramic 'shell'"*（Pamarco CT9）反映的正是雕刻/后处理层质量差异，可作为面层-雕刻完整性的间接表征。

(d) 原文英文摘录
> "Bond Coat Plasma Spray = Nickel-Chrome" — SLIDE 12

### C9. Ceramic Plasma Spray (Chromium Oxide/titanium) ｜ 等离子喷涂陶瓷层（氧化铬/钛）

(a) 中文名 + English term：等离子喷涂陶瓷面层（氧化铬/钛）/ Ceramic Plasma Spray = Chromium Oxide/titanium

(b) English definition
> Step 7 of the 10-step process: the Chromium Oxide/titanium ceramic topcoat applied by plasma spray over the Nickel-Chrome bond coat. This is the layer that is subsequently ground/polished (Step 8) and laser-engraved (Step 9), and that delivers the platform's corrosion and abrasion resistance.

(c) 操作化定义
- 测量维度：① 材料 = Chromium Oxide/titanium ② 工艺 = Plasma Spray ③ 顺序 = Step 7 / 10 ④ 下游 = Grinding/Polishing → Laser engraving → Final polishing。
- 判定公式/量化指标：本章未给出陶瓷层厚度、硬度（HV）、孔隙率或厚度公差 → [未找到原句]。
- 性能判据（定性，原文）：SLIDE 11 — *"More resistant to corrosion and abrasion, longer engraving life"*。可操作化为：在腐蚀性或磨蚀性流体（如乳胶、起皱胶）工况下优先选陶瓷。
- ⚠️ 关于铬价态的重要区分 [本报告推导 / 外部化学常识，非本章内容]：本章 SLIDE 10 的 "vendor options due to chrome 6" 针对的是电镀铬辊（C1）的六价铬电镀工艺；而 SLIDE 12 陶瓷面层写的是 Chromium Oxide，通常指 Cr₂O₃（三价铬），与六价铬在法规上不属于同一物质。本章原文未做任何价态声明，因此不可据此宣称陶瓷辊「不含六价铬」——该结论需由供应商材料声明（RoHS/REACH/SDS）证实，见模块 5 连接点 2。

(d) 原文英文摘录
> "Ceramic Plasma Spray = Chromium Oxide/titanium" — SLIDE 12
> "Pros - More resistant to corrosion and abrasion, longer engraving life…" — SLIDE 11

### C10. Dynamic balancing & Sand blasting ｜ 动平衡 与 喷砂

(a) 中文名 + English term：动平衡 / Dynamic balancing；喷砂 / Sand blasting

(b) English definition
> Two of the four pre-coating steps in ceramic gravure roll production. Dynamic balancing (Step 3) is performed on the steel roll base — before grinding, blasting and coating — to correct mass distribution of the rotating body. Sand blasting (Step 5) is performed after grinding and immediately before the bond coat plasma spray, and is the last surface-preparation step before coating.

(c) 操作化定义
- 测量维度：
  - Dynamic balancing：顺序 = Step 3 / 10（在 Grinding 之前）；对象 = Steel roll base（含 *Corrosion resistance welding (if necessary)*，Step 2）。
  - Sand blasting：顺序 = Step 5 / 10；紧前 = Grinding（Step 4）；紧后 = Bond Coat Plasma Spray（Step 6）。
- 判定公式/量化指标：本章未给出动平衡的残余不平衡量（g·mm）、ISO 平衡等级（如 G2.5/G6.3）、或喷砂的磨料牌号/粒度/粗糙度 Ra 值 → 全部 [未找到原句]。
- 可执行判据（流程顺序型，可用作验收检查项） [本报告推导]：
  1. 动平衡必须发生在喷涂之前——喷涂后无法在不破坏陶瓷层的前提下校正基体不平衡；
  2. 喷砂必须发生在粘结层之前——顺序颠倒即构成工艺不合格；
  3. 因 KC 雕刻含 "Large amount of unengraved area"（SLIDE 20），陶瓷层去除量分布极不均匀，故最终抛光后是否需要复检动平衡是应写入规格书的开放项（本章未涉及 → [未找到原句]）。
- 与 KC 独特性的耦合 [本报告推导]：SLIDE 20 指出大量未雕刻区使抛光更复杂；抛光不均会引入新的质量分布偏差，而本章流程中动平衡仅出现在 Step 3。这是一处流程覆盖缺口，建议列入供应商技术问卷。

(d) 原文英文摘录
> "Dynamic balancing" / "Sand blasting" — SLIDE 12（流程顺序：Steel roll base → Corrosion resistance welding (if necessary) → Dynamic balancing → Grinding → Sand blasting → Bond Coat Plasma Spray）

### C11. Chrome 6 restriction ｜ 六价铬限制

(a) 中文名 + English term：六价铬限制 / Chrome 6（hexavalent chromium）restriction

(b) English definition
> An environmental/occupational restriction on hexavalent chromium that appears in this chapter only as a supply-base consequence: it is listed as a Con of electro-mechanical engraved chrome rolls, phrased as "vendor options due to chrome 6" — i.e. the regulation's effect on KC is a reduction in the number of qualified engraving vendors, not a product-property effect.

(c) 操作化定义
- 测量维度：本章唯一可测量维度是合格供应商数量（vendor options ↓）。
- 判定公式/量化指标：本章未给出任何法规名称（如 RoHS / REACH / ELV / OSHA PEL）、限值（ppm 或 μg/m³）、生效日期或地区范围 → 全部 [未找到原句]。
- 可操作的采购判据 [本报告推导]，依据 Ch3 SLIDE 22：KC 的 Key Vendors 仅列 4 家且全部位于美国——Harper（Charlotte, NC）、Precision Roll Solutions / IR Engraving（Richmond, VA）、Pamarco（Atlanta, GA）、Apex（Pittsburgh, PA）。在 SLIDE 10 明确 chrome 6 会压缩供应商选择的前提下，这 4 家名单是「供应基础收窄」的可核查证据。
- 风险表征：SLIDE 10 把 vendor options 与 variability due to plating inconsistency 并列在同一条 Cons 中 → 供应基础收窄与质量波动是并发风险，不可单独管理。
- ⚠️ 严格边界：任何关于「国内（中国）供应商是机会还是壁垒」的判断都不是本章内容，本报告在模块 5 中仅以 本报告推导 形式给出分析框架。

(d) 原文英文摘录
> *"Cons - shorter engraving life, engraving limitations, variability due to plating inconsistency, vendor options due to chrome 6"* — SLIDE 10

### C12. Engraving window ｜ 雕刻工艺窗口

(a) 中文名 + English term：雕刻工艺窗口 / engraving window（本章未出现该术语 → [未找到原句]）

(b) English definition（由本章证据归纳）
> The engraving window is the bounded region of the multi-dimensional specification space — cell geometry, line/screen count, cell volume, cell diameter, cell depth, pattern shape/size/spacing — within which an engraver can produce a roll that is repeatable, on-volume, and free of defects. KC's rolls lie outside this window: they are "Outside the engravers comfort zones" (SLIDE 20). The window is also geometrically closed by the fact that volume, depth and diameter cannot all be fixed at once (Ch4 SLIDE 36).

(c) 操作化定义
- 术语溯源：短语 "engraving window" 在本章及全书 4 个章节文件中均未出现 → [未找到原句]。以下操作化定义由 SLIDE 20 的 "Outside the engravers comfort zones" 与 Ch4 SLIDE 36 的自由度约束归纳而成 → 本报告推导。
- 维度 1 — 边界（boundary）：由 SLIDE 20 给出 4 个越界方向：
  | 越界维度 | 原文 | SLIDE |
  |---|---|---|
  | Pattern | "Engineered patterns - DRC/OLU/Facial" | 20 |
  | Process capability | "Outside the engravers comfort zones" | 20 |
  | Depth | "“Deep” engravings" | 20 |
  | Size | "“Large” cells" | 20 |
  | Post-process load | "Large amount of unengraved area = more complex polishing" | 20 |
- 维度 2 — 内部约束（closure）：Ch4 SLIDE 36 — *"Engraver must have at least 1 degree of freedom. Can only specify 2 from the key engraving parameters of volume, depth, and diameter"*。
  形式化 [本报告推导]：设规格向量 S = {geometry, screen, volume, diameter, depth, shape, size, spacing}，共 8 个参数（SLIDE 16 3 个 + SLIDE 21 6 个，其中 cell volume 重叠 → 去重后 8）。独立可控数 ≤ 8 − 1（volume-depth-diameter 闭合）− 1（geometry-screen 耦合）= ≤ 6。
- 维度 3 — 可测量失效（observable excursion）：越出窗口的可观测后果，本章/后续章给出 3 类：
  1. 容积偏差 — Ch4 SLIDE 29/30：Pamarco Trial 1100 GMT vs 1800 OLU GMT Target；Apex Trial 1550 GMT vs 1800 OLU GMT Target
  2. 雕刻未透/残留 — Ch3 SLIDE 34 图像内容补充：*"Engraving – 1/3 of dot is still filled with ceramic 'shell'"*（IR Engraving VENUS CT5）；对照 *"Dots are full circles and clean. No ceramic 'shell'."*（Pamarco VENUS CT9）
  3. 周期与一致性 — Ch4 SLIDE 34 — SPEAKER NOTES：*"Harper took 9 months to engrave first roll and then had a large volume skew"；SLIDE 32 notes："struggled with engraving consistency and quality until Pamarco came on line in Q3 2024"*
- 量化指标（本报告推导的窗口探针）：以 SLIDE 17 事故为标定，规格书写错误 → 单穴体积偏差 ×6.45；以 Ch4 SLIDE 29/30 为标定，供应商首次试雕的 GMT 达标率区间为 1100–1550 vs 1800 target，即 61%–86% → 首次试雕偏离目标 −14% 至 −39% [本报告推导]。

(d) 原文英文摘录
> *"Unique KC Gravure rolls / This is where the MAGIC happens / Engineered patterns - DRC/OLU/Facial / Outside the engravers comfort zones / “Deep” engravings / “Large” cells / Large amount of unengraved area = more complex polishing / Not just printing/coating …. Creating product properties"* — SLIDE 20
> "Gravure roll design is an iterative process … Engraver must have at least 1 degree of freedom. Can only specify 2 from the key engraving parameters of volume, depth, and diameter" — Ch4 SLIDE 36

## 模块 3：证据链（Evidence Tables）

### T1 — Electro-mechanical Engraved Chrome Roll vs Laser Engraved Ceramic Roll：Pros/Cons 全字段对比 SLIDE 10 + SLIDE 11

|||||||
|---|---|---|---|---|---|
|1|Initial cost|lower cost (Pro)|Higher cost (Con)|Chrome|SLIDE 10 / SLIDE 11|
|2|Engraving life|shorter engraving life (Con)|longer engraving life (Pro)|Ceramic|SLIDE 10 / SLIDE 11|
|3|Engraving flexibility|engraving limitations (Con)|more engraving flexibility (Pro)|Ceramic|SLIDE 10 / SLIDE 11|
|4|Transfer precision & consistency|variability due to plating inconsistency (Con)|more precise and consistent fluid transfer (Pro)|Ceramic|SLIDE 10 / SLIDE 11|
|5|Supply base / vendor competition|vendor options due to chrome 6 (Con)|vendor competition (Pro)|Ceramic|SLIDE 10 / SLIDE 11|
|6|Corrosion resistance|[未找到原句] — 本章未就镀铬辊耐腐蚀性表态|More resistant to corrosion (Pro)|Ceramic（单方声明）|SLIDE 11|
|7|Abrasion resistance|[未找到原句]|More resistant to … abrasion (Pro)|Ceramic（单方声明）|SLIDE 11|
|8|Engraving layer / material|electroplated chrome（层材料工序未在本章展开）|Bond Coat = Nickel-Chrome + Ceramic = Chromium Oxide/titanium，均 Plasma Spray|—|SLIDE 12|
|9|Engraving method|Electro-mechanical（机电，非激光）|Laser（*Circular laser beam that creates ~10 um round hole*）|—|SLIDE 10 / SLIDE 14|
|10|KC asset assignment|Facial|OLU / DRC / ELCs|—|SLIDE 10 / SLIDE 11|
|11|Coating process (direct/indirect)|Indirect（Ch1 SLIDE 5：*Indirect = gravure roll to applicator roll to substrate…. Facial and Embossing winders*；Ch1 SLIDE 8：*Facial OLP = Indirect Gravure Coating*）|Direct（OLU/DRC，Ch1 SLIDE 5/6）；ELCs 为 Indirect（Ch1 SLIDE 7：*2 Ply Winder ELC = Indirect Gravure Coating*）|⚠️ 非一一对应|Ch1 SLIDE 5, 6, 7, 8|
|12|Pro : Con 计数|1 Pro : 4 Cons|5 Pros : 1 Con|Ceramic|SLIDE 10 / SLIDE 11|
|13|Documented example spec|Jenks Facial Lotion GR — alternating bands of 2 BCM and 6 BCM + dead bands|2 ply bath — 60 degree hex, 180 LPI, 6.0 BCM|—|SLIDE 10 notes / SLIDE 16|




⚠️ 关键交叉发现 [本报告推导]：第 11 行显示 direct/indirect 与 chrome/ceramic 不是一一映射。ELC（2-ply embossing winder）在 Ch1 SLIDE 7 属 Indirect，却在 SLIDE 11 使用 激光陶瓷辊。因此「Facial 用镀铬」不能简单归因于「indirect 工艺」，必须另有解释 —— 见模块 4。

### T2 — 陶瓷辊制造 10 道工序表（Ceramic Gravure Roll Production）SLIDE 12

||||||||
|---|---|---|---|---|---|---|
|1|Steel roll base|钢辊基体|Substrate|—|（起点）|否 [未找到原句]|
|2|Corrosion resistance welding (if necessary)|耐腐蚀堆焊（如需要）|Substrate|原文标注 (if necessary) —— 条件性工序|1|否|
|3|Dynamic balancing|动平衡|Prep|—|2|否 [未找到原句]|
|4|Grinding|磨削|Prep|—|3|否|
|5|Sand blasting|喷砂|Prep|—|4|否 [未找到原句]|
|6|Bond Coat Plasma Spray = Nickel-Chrome|等离子喷涂粘结层（镍铬）|Coating|Nickel-Chrome|5|否|
|7|Ceramic Plasma Spray = Chromium Oxide/titanium|等离子喷涂陶瓷层（氧化铬/钛）|Coating|Chromium Oxide/titanium|6|否|
|8|Grinding/Polishing|磨削/抛光（陶瓷层）|Finishing|—|7|否|
|9|Laser engraving|激光雕刻|Engraving|~10 μm 圆孔；角部照射 ≥3 次|8|是（SLIDE 14）|
|10|Final polishing|最终抛光|Finishing|—|9|否|

T2-a 阶段结构 [本报告推导]
| Phase | Steps | Count | 说明 |
|---|---|---|---|
| Substrate（基体） | 1–2 | 2 | 含 1 道条件性工序 |
| Pre-coat preparation（喷涂前准备） | 3–5 | 3 | 动平衡、磨削、喷砂 |
| Coating（涂层） | 6–7 | 2 | 双层：粘结层 + 陶瓷层 |
| Pre-engrave finishing（雕刻前精整） | 8 | 1 | 决定雕刻面基准 |
| Engraving（雕刻） | 9 | 1 | 仅占 1/10 |
| Post-engrave finishing（雕刻后精整） | 10 | 1 | 去除角峰，防刮刀磨损 |

T2-b 顺序约束（可作为供应商工艺审核清单）[本报告推导]
1. 动平衡（3）必须早于全部涂层工序（6、7）—— 涂层后无法校正基体不平衡。
2. 喷砂（5）必须紧邻并早于粘结层（6）—— 顺序颠倒即为不合格。
3. 陶瓷层（7）必须早于雕刻（9）—— 雕刻对象就是陶瓷层。
4. 最终抛光（10）不可省略 —— SLIDE 14：*"Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear"*。
5. 对 KC 而言，Step 10 是难度放大器 —— SLIDE 20：*"Large amount of unengraved area = more complex polishing"*。

T2-c 补充证据
- SLIDE 12 — SPEAKER NOTES："Graphics programming and repeat calculations for complex patterns" —— 雕刻前的图形编程与重复周期计算是独立工作量，本章未计入 10 道工序。
- SLIDE 15 — SPEAKER NOTES："Ceramic roll in the laser bed" —— 确认 Step 9 的实机状态（SLIDE 15 为 image-only slide）。
- SLIDE 15 正文："(no text - image only slide)" —— 该页无文本层，仅图像。

### T3 — 激光雕刻机理表（Laser Engraving Mechanism）SLIDE 14 + SLIDE 14 — 图像内容补充

||||||||
|---|---|---|---|---|---|---|
|1|"Circular laser beam that creates ~10 um round hole"|圆形激光束打出约 10 μm 圆孔|~10 μm（孔径）|单发形成圆柱形初始孔|决定最小特征尺寸下限|SLIDE 14|
|2|"Engraving each subsequent hole pushes the cell walls to create a hexagon shape"|相邻孔逐个雕刻，挤压网穴壁形成六边形|—|六边形是挤压副产物，非直接铣削成形|网穴壁完整性由激光重叠率决定，非设计余量|SLIDE 14|
|3|"Each corner is exposed to the laser a minimum of 3 times compared to the side walls"|每个角部被激光照射至少 3 次（相对侧壁）|≥ 3×|角部能量密度显著高于侧壁 → 选择性熔融/再沉积|能量分布不均，是缺陷来源|SLIDE 14|
|4|"Raised peaks are created in the corners"|角部形成凸起峰|—|角峰高出雕刻面|直接威胁刮刀|SLIDE 14|
|5|"Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear"|必须抛光以去除角峰，消除过度刮刀磨损|—|抛光 = 强制工序（对应 T2 Step 10）|未抛光 = 刮刀过度磨损 = 停机 + 备件成本|SLIDE 14|
|6|显微形貌佐证：初始 ~10 μm 圆孔 → 相邻孔挤压成六边形；角部被照射 ≥3 次形成凸起；抛光前后对比（金色六边形）|抛光前/后形貌对比|—|抛光后六边形轮廓规整|抛光是形貌质量的显性变量|SLIDE 14 — 图像内容补充|

T3-a 因果链（Documented causal chain）

圆形激光束 (~10 μm)
   └─> 顺序雕刻相邻孔
         └─> 挤压 cell walls → 六边形 (SLIDE 14)
               └─> 角部重叠照射 ≥3× (SLIDE 14)
                     └─> 角部 raised peaks (SLIDE 14)
                           └─> 若不抛光 → 过度刮刀磨损 (SLIDE 14, 明确 "excessive")
                                 └─> 必须 Final polishing (SLIDE 12 Step 10)
                                       └─> 对 KC：未雕刻面积大 → 抛光更复杂 (SLIDE 20)

T3-b 与 KC 独特性的交互 [本报告推导]
SLIDE 20 的 "Deep" engravings 与 "Large" cells 意味着更高的材料去除量与更长的激光作用时间；若角部重叠照射仍保持 ≥3×（机理常量），则角峰体积随网穴尺寸放大，而 KC 的 "Large amount of unengraved area" 又使抛光接触面积分布极不均匀 → Step 10 对 KC 的难度是双重放大的。

T3-c 跨章验证 [本报告推导]
Ch3 SLIDE 31 图像内容补充 记录 Apex VIVA Trial #2 – Ran for 24 Hours 之后的 Re-Polish #1 / #2 / #3（三次重抛光，约 100 μm / 440 μm / 340 μm 级标注）—— 即 抛光是反复迭代、非一次通过的工序，直接印证 SLIDE 14 的抛光强制性。

### T4 — 单位换算表（Unit Conversion Table）SLIDE 18 + SLIDE 19 + 本报告推导

T4-a 基础定义（原文）
| Quantity | Value (原文) | Evidence |
|---|---|---|
| 1 BCM | 1,000,000,000 μm³（= 10⁹ μm³） | SLIDE 19 |
| 长度桥 | 1,000 μm = 1 mm | SLIDE 19 |
| BCM/in² → cm³/m² | 1 BCM/in² = 1.55 cm³/m² | SLIDE 18 |
| 物理定义 | "Total volume of all the engraved cells on the roll surface per unit area of the surface" | SLIDE 18 |
| 美制命名 | "USA = BCM/in2 ……. More commonly just referred to as BCM" | SLIDE 18 |
| 欧制命名 | "European = cm3/m2" | SLIDE 18 |
| 单位混杂警告 | "USA combines metric and English units" | SLIDE 18 — SPEAKER NOTES |

T4-b 自洽性验证：1 BCM = 10⁹ μm³ = 1 mm³ [本报告推导]

路径 A（以 μm→mm 桥接，依据 SLIDE 19 原文 "1,000 um = 1 mm"）：
  1 BCM = 1,000,000,000 μm³
        = (10³ μm)³
        = (1 mm)³
        = 1 mm³                                        ✔ 自洽成立
路径 B（SI 复核）：
  10⁹ μm³ × (10⁻⁶ m / 1 μm)³ = 10⁹ × 10⁻¹⁸ m³ = 1.0 × 10⁻⁹ m³
  1 mm³ = (10⁻³ m)³ = 1.0 × 10⁻⁹ m³
  → 1.0 × 10⁻⁹ m³ ≡ 1.0 × 10⁻⁹ m³                     ✔ 完全一致
结论：1 BCM = 10⁹ μm³ = 1 mm³ = 10⁻⁹ m³ = 10⁻³ cm³     （自洽，无矛盾）

T4-c 换算推导：1 BCM/in² = 1.55 cm³/m² [本报告推导]

已知：1 in = 25.4 mm = 2.54 cm（定义值）;  1 BCM = 1 mm³ = 10⁻³ cm³（见 T4-b）
第 1 步  1 in² = (25.4 mm)² = 645.16 mm² = 6.4516 cm²
第 2 步  1 in² = 6.4516 cm² × (1 m² / 10⁴ cm²) = 6.4516 × 10⁻⁴ m²
第 3 步  1 BCM/in² = 10⁻³ cm³ ÷ (6.4516 × 10⁻⁴ m²)
第 4 步            = 0.001 ÷ 0.00064516
第 5 步            = 1.5500031… cm³/m²
第 6 步            ≈ **1.55 cm³/m²**    ✔ 与 SLIDE 18 原文值 "1.55" 一致
换算常数：1 ÷ 0.00064516 = 1000 ÷ 0.64516 = **1.5500031**

T4-d 湿膜厚度等价（本次推导的增量工具）[本报告推导]

1 cm³/m² = 10⁻⁶ m³ / 1 m² = 10⁻⁶ m = **1 μm** 平均湿膜厚度（假设 100% 转移）
→ 1 BCM/in² = 1.55 cm³/m² = **1.55 μm**
→ 通用式：h(μm) = BCM × 1.55 = cm³/m²
交叉校验（60° hex 理想铺满，见 C6）：
  h = 6.0 BCM/in² = 6×10⁹ μm³ ÷ (25.4×10³ μm)² = 6×10⁹ ÷ 6.4516×10⁸ = **9.30 μm**
  与 6.0 × 1.55 = 9.30 cm³/m² = 9.30 μm 完全一致   ✔ 两条独立路径互证

T4-e 全单位换算速查表
| BCM/in² | μm³/in² | mm³/in² | cm³/m² | 等效平均湿膜厚度 (μm) | 本章/跨章出处 |
|---|---|---|---|---|---|
| 1 | 1 × 10⁹ | 1 | 1.55 | 1.55 | SLIDE 18 + 推导 |
| 2.0 | 2 × 10⁹ | 2 | 3.10 | 3.10 | SLIDE 10 notes (Facial lotion band) |
| 6.0 | 6 × 10⁹ | 6 | 9.30 | 9.30 | SLIDE 16 (2-ply bath) / SLIDE 17 |
| 5.65 | 5.65 × 10⁹ | 5.65 | 8.76 | 8.76 | [本报告推导] VENUS：1,488 dots/in² × 3.8×10⁶ μm³ ÷ 10⁹（Ch3 SLIDE 32 图像内容补充） |
| 27.6 | 2.76 × 10¹⁰ | 27.6 | 42.78 | 42.78 | Ch3 SLIDE 28 图像内容补充（VIVA，数值含义存疑，见 T4-f） |

T4-f ⚠️ 跨章数值口径存疑（必须记录）[本报告推导]
Ch3 SLIDE 28 图像内容补充 记 VIVA 图纸为 *"Volume 27,600,000 cubic microns (27.6 BCM)"*。按 SLIDE 19 的定义 1 BCM = 10⁹ μm³，则 27,600,000 μm³ = 0.0276 BCM，与括号中的 27.6 BCM 相差 1,000 倍。
- 若 27.6 BCM 为整辊体积 → 27.6 × 10⁹ μm³/in²；按该图纸 27 dpi dot、2:1 spacing 反算点密度 = 27² ÷ 2 = 364.5 dots/in² → 总容积 = 364.5 × 27.6×10⁶ = 1.006 × 10¹⁰ μm³/in² = 10.06 BCM，与 27.6 BCM 仍不相符。
- 若 27,600,000 μm³ 为单穴容积，则深穴尺寸 0.813 × 0.559 mm 对应等效深度 = 27.6×10⁶ μm³ ÷ (813 × 559 μm²) = 60.7 μm。
- 结论：该图纸的数值口径（单穴 vs 整辊、μm³ vs BCM）在本课程 4 个章节内无法自洽判定，属第三处单位风险，须向 Harper 图纸签发方书面澄清。本报告不对该数值做进一步推断。

### T5 — ⚠️ 单位事故表（Unit Incident）：Jenks L12 Bath, Fall 2022 SLIDE 17

T5-a 事故基本信息
| Field | Value | Evidence |
|---|---|---|
| 项目 | Jenks L12 Bath Gravure Rolls | SLIDE 17 |
| 时间 | Fall of 2022 | SLIDE 17 |
| 标题 | Importance of Line/Screen Count | SLIDE 17 |
| 背景 | "My first gravure roll project at KC" | SLIDE 17 — SPEAKER NOTES |
| 事故形态 | 同一 "6 BCM VOLUME" 标签下，180 Lines/cm 与 180 Lines/inch 两个规格被混淆 | SLIDE 17 |
| 视觉佐证 | 左 180 Lines/cm（网穴极密集细小）／右 180 Lines/inch（网穴明显更大更稀疏），黄色高亮 "BOTH '6 BCM VOLUME'" | SLIDE 17 — 图像内容补充 |

T5-b 单位换算（原文值）
| 换算 | 原文值 | 精算值 | 偏差 | Evidence |
|---|---|---|---|---|
| 180 LCM → LPI | 460 LPI | 180 × 2.54 = 457.2 LPI | +0.61%（原文取整） | SLIDE 17 — SPEAKER NOTES |
| 180 LPI → LCM | 70 LCM | 180 ÷ 2.54 = 70.87 LCM | −1.22%（原文取整） | SLIDE 17 — SPEAKER NOTES |

T5-c 两种解读的后果全字段对比 [本报告推导]（网穴尺寸/密度完全不同）
| # | Parameter | 180 Lines/cm（= 460 LPI） | 180 Lines/inch（= 70 LCM） | 比值 (in/cm) |
|---|---|---|---|---|
| 1 | 标称体积（两者相同！） | 6 BCM | 6 BCM | 1.00× |
| 2 | 标称体积（cm³/m²） | 9.30 | 9.30 | 1.00× |
| 3 | 等效平均湿膜厚度 | 9.30 μm | 9.30 μm | 1.00× |
| 4 | 网穴中心距 pitch | 25.4 mm ÷ 457.2 = 55.56 μm | 25.4 mm ÷ 180 = 141.11 μm | 2.54× |
| 5 | 网穴密度（60° hex，cells/in²） | 1.1547 × 457.2² = 241,369 | 1.1547 × 180² = 37,412 | 6.45× |
| 6 | 网穴密度（cells/cm²） | 1.1547 × 180² = 37,412 | 1.1547 × 70.87² = 5,799 | 6.45× |
| 7 | 单穴容积 @ 6 BCM | 6×10⁹ ÷ 241,369 = 24,858 μm³ | 6×10⁹ ÷ 37,412 = 160,375 μm³ | 6.45×（= 2.54²） |
| 8 | 相对激光孔径 ~10 μm 的开口尺度 | pitch 55.6 μm ≈ 5.6 × 孔径 | pitch 141.1 μm ≈ 14.1 × 孔径 | 2.54× |
| 9 | 对角峰/抛光的负荷（定性） | 网穴小、角峰密 → 抛光接触点多 | 网穴大、去除量大 → 单次去除量大 | — |



核心机理 [本报告推导]：V_cell = V_total ÷ N，而 N = 1.1547 L² → V_cell ∝ 1/L²。
因此 总 BCM 相同时，线数错 2.54 倍（in/cm）→ 单穴体积错 2.54² = 6.4516 倍。
规格书只写 "6 BCM" 而不写线数与单位，等于留下 6.45 倍的单穴容积自由度。 这就是 SLIDE 17 事故的物理本质。

T5-d 事故后的正确规格写法（由 SLIDE 16 + SLIDE 17 反推的规范）
| Field | 2-ply bath 正确规格 | Evidence |
|---|---|---|
| Cell geometry | 60 degree hex | SLIDE 16 |
| Line screen | 180 LPI | SLIDE 16 |
| Cell volume | 6.0 BCM | SLIDE 16 |
| 完整写法 | 60 degree hex, 180 LPI, 6.0 BCM | SLIDE 16 |

T5-e 同类风险在课程内的二次出现
| 风险点 | 内容 | Evidence |
|---|---|---|
| 单位混杂 | *"USA combines metric and English units"*（BCM 用 μm³，面积用 in²） | SLIDE 18 — SPEAKER NOTES |
| 简称丢单位 | *"More commonly just referred to as BCM"*（丢掉 /in²） | SLIDE 18 |
| 图纸口径 | VIVA "27,600,000 cubic microns (27.6 BCM)" 的 1,000 倍口径矛盾 | Ch3 SLIDE 28 图像内容补充 |
| 测量工具口径 | "Did not measure volume with same tools so none of the data translated" —— 不同量具的数据不可比 | Ch4 SLIDE 34 — SPEAKER NOTES |

### T6 — Standard Ceramic Anilox Roll Engravings：六种雕刻图案表 SLIDE 13 + SLIDE 13 — 图像内容补充

|||||||
|---|---|---|---|---|---|
|1|60° Hex|60° 六边形|否 — 仅列名；但 SLIDE 16 给出 60 degree hex 为 2-ply bath 正式规格|是（下方三张蓝色显微形貌图之一）|SLIDE 13 — 图像内容补充|
|2|GTT|GTT（Gould/太平软件开孔型，本章无展开）|否 [未找到原句]|是|SLIDE 13 — 图像内容补充|
|3|45°|45°（菱形/斜向阵列，本章无展开）|否 [未找到原句]|否|SLIDE 13 — 图像内容补充|
|4|Longcell|长网穴（本章无展开）|否 [未找到原句]|否|SLIDE 13 — 图像内容补充|
|5|Channellox|槽沟型网穴（本章无展开）|否 [未找到原句]|否|SLIDE 13 — 图像内容补充|
|6|Trihelical|三螺旋（本章无展开）|否 [未找到原句]|是|SLIDE 13 — 图像内容补充|

T6-a 该页的原文信息边界
- SLIDE 13 正文仅有标题：*"Standard Ceramic Anilox Roll Engravings"*。正文无任何图案描述文本。
- SLIDE 13 — SPEAKER NOTES："ELCs – 2 PLY bath/towel embossing" —— 明确 ELC 辊用于 2 层浴巾/纸巾压花。
- SLIDE 13 — SPEAKER NOTES："Anilox vs Gravure and Apex Owner Discussion this week" —— 记录 anilox 与 gravure 的术语/归属问题当时仍在讨论中（与 Ch1 SLIDE 2 的术语说明呼应）。
- 六种图案的几何定义、角度、容积范围、适用场景本章全部未给出 → 全部 [未找到原句]。本报告不为任何图案补充外部定义。

T6-b 术语背景（供交叉理解，非本章内容）
Ch1 SLIDE 2 — SPEAKER NOTES："Gravure roll and anilox roll – pretty much the same thing. Gravure roll has an industry connotation of direct to substrate and patterned. Anilox roll is more indirect and common/simple engraving"
→ 即 SLIDE 13 的六种「Standard Ceramic Anilox Roll Engravings」属于常规/简单（common/simple）雕刻范畴，与 SLIDE 20 的 "Unique KC Gravure rolls" / "Outside the engravers comfort zones" 构成标准 vs 定制的明确二分。

### T7 — Unique KC Gravure rolls 特征表 SLIDE 20 + SLIDE 21

T7-a 七项特征（原文全字段）
| # | 特征 (English, 原文) | 中文 | 可操作化解读 [本报告推导] | 影响环节 | Evidence |
|---|---|---|---|---|---|
| 1 | "This is where the MAGIC happens" | 差异化价值所在 | 定位语：雕刻规格 = KC 产品力来源 | 战略 | SLIDE 20 |
| 2 | "Engineered patterns - DRC/OLU/Facial" | 工程化图案（DRC/OLU/Facial） | 三条产线均有定制图案，非标准 anilox（对比 T6） | 图案设计 | SLIDE 20 |
| 3 | "Outside the engravers comfort zones" | 超出雕刻商舒适区 | 供应商能力边界 → 需爬坡期与试雕 | 供应商管理 | SLIDE 20 |
| 4 | "“Deep” engravings" | 深雕刻 | 材料去除量大 → 激光工时↑、角峰体积↑ | 雕刻 + 抛光 | SLIDE 20 |
| 5 | "“Large” cells" | 大网穴 | 单穴容积远超标准 anilox → 低线数 | 规格设定 | SLIDE 20 |
| 6 | "Large amount of unengraved area = more complex polishing" | 大量未雕刻区 → 抛光更复杂 | 唯一被原文明确为「因→果」的特征 | 抛光（T2 Step 10） | SLIDE 20 |
| 7 | "Not just printing/coating …. Creating product properties" | 不只是印刷/涂布……而是创造产品属性 | 规格语言必须从「印刷参数」转为「产品属性参数」 | 需求定义 | SLIDE 20 |
| 8 | "Engravers have no insight beyond the cell dimensions" | 雕刻商对网穴尺寸之外一无所知 | KC 必须自行完成「产品属性 → 网穴尺寸」的翻译 | 需求定义 | SLIDE 20 — SPEAKER NOTES |
| 9 | "KC has to be able to communicate the engraving specifications required to create product properties." | KC 必须能够沟通为创造产品属性所需的雕刻规格 | 组织能力要求（非设备要求） | 组织/人才 | SLIDE 20 — SPEAKER NOTES |

T7-b KC 独有雕刻参数两框（SLIDE 21 — *"Engraving Specifications – Unique KC Engravings"*）
| 框 | 框名 (English, 原文) | 中文 | 参数项 | 本章是否给出数值 |
|---|---|---|---|---|
| 🟣 紫框 | Cell dimensions | 网穴尺寸 | ① Cell diameter（网穴直径）② Cell depth（网穴深度）③ Cell volume（网穴容积） | 否 —— "该页无具体数值表，仅列参数类别" |
| 🟢 绿框 | Pattern details | 图案细节 | ① Shapes（形状）② sizes（尺寸）③ spacing（间距） | 否 —— 同上 |

- SLIDE 21 正文：*"Engraving Specifications – Unique KC Engravings"*；[images: 0]。
- SLIDE 21 — 图像内容补充：*"p21 Engraving Specifications 两框：紫框 Cell dimensions（Cell diameter / Cell depth / Cell volume）；绿框 Pattern details（Shapes, sizes, spacing）。该页无具体数值表，仅列参数类别"*
T7-c 标准规格 vs KC 独有规格：参数集对比 [本报告推导]
| 项目 | Standard Engraving Specifications（SLIDE 16） | Unique KC Engravings（SLIDE 21） |
|---|---|---|
| 参数组数 | 1 组 | 2 组 |
| 参数数量 | 3（Cell geometry, lines per inch, cell volume） | 6（diameter, depth, volume, shapes, sizes, spacing） |
| 是否已规格化 | 是 — 已给出完整实例：60 degree hex, 180 LPI, 6.0 BCM | 否 — 仅列类别，本章无数值 |
| 是否有公认术语 | 是（LPI/BCM 为行业通用） | 部分（spacing/pattern 需 KC 自定义） |
| 参数重叠 | cell volume（唯一交集） | cell volume（唯一交集） |
| 去重后总参数 | — | 3 + 6 − 1 = 8 |
| 独立可控数上限 | — | ≤ 6（见 C12 维度 2 闭合约束） |

T7-d KC 独有规格的跨章实证值（Ch3，供参照；非本章内容）
| 项目 | VIVA (OLU) | VENUS (OLU) | Evidence |
|---|---|---|---|
| 图纸方 | HARPER（HCA Job# 111233501，KC GR# 5，XDI #3，Date 8/30/23） | HC（HC 110615901，Date 10-16-2022） | Ch3 SLIDE 28 / 32 图像内容补充 |
| 辊面宽 / 直径 | 112" (2,844.8 mm) / 20" (508 mm) | 112" / 19.701" | 同上 |
| 雕刻区 | 104.5" (2,654.3 mm) centered | 104.5" wide，居中 | 同上 |
| 图案 | 27 dpi dot；2:1 dot spacing；Rotated 19.6° from vertical | 34.5 DPI, 1488 DOTS/SQ-IN | 同上 |
| 网穴尺寸 | Deep Dot 0.032" × 0.022" ±10%（0.813 × 0.559 mm） | Shallow Dot 0.02" = 0.508 mm | 同上 |
| 容积 | 27,600,000 cubic microns（27.6 BCM） | Target Volume 3,800,000 μm³ ±5% | 同上 |
| 抛光判据 | "POLISHING NOTE: Target <= 10,700,000 Shallow Dot Volume Average" | — | Ch3 SLIDE 28 图像内容补充 |
| 平整度 | "Flat Burn Target < ±10%" | — | 同上 |
| 未雕刻区 | *"Top Burn Area 3.5" Max Both Ends"*；3.75" Both Ends | — | 同上 |



注：VIVA/VENUS 的具体数值属 Ch3 内容，此处仅作 T7「参数类别」的实例化参照；其单位口径存疑见 T4-f。

## 模块 4：章节间衔接（Chapter Connections）

### 4.1 与前章 Ch1（Fundamentals）：Direct / Indirect 与 Chrome / Ceramic 的对应关系

#### 4.1-a 四象限对应表

|||||||
|---|---|---|---|---|---|
|DRC|Direct|"Direct = gravure roll to substrate …… DRC and OLU" (Ch1 SLIDE 5)|Laser Engraved Ceramic|"Laser Engraved Ceramic Rolls (OLU/DRC/ELCs)" (SLIDE 11)|✅ 一致|
|OLU|Direct|同上 (Ch1 SLIDE 5, 6)|Laser Engraved Ceramic|同上 (SLIDE 11)|✅ 一致|
|ELCs (2 Ply Winder)|Indirect|"Indirect = gravure roll to applicator roll to substrate…. Facial and Embossing winders" (Ch1 SLIDE 5)；"2 Ply Winder ELC = Indirect Gravure Coating" (Ch1 SLIDE 7)|Laser Engraved Ceramic|"(OLU/DRC/ELCs)" (SLIDE 11)|⚠️ Indirect 但用陶瓷|
|Facial (OLP)|Indirect|"Indirect = … Facial and Embossing winders" (Ch1 SLIDE 5)；"Facial OLP = Indirect Gravure Coating" (Ch1 SLIDE 8)|Electro-mechanical Engraved Chrome|"Electro-mechanical Engraved Chrome Rolls (Facial)" (SLIDE 10)|✅ 一致|

#### 4.1-b 关键结论：Direct/Indirect 不是 Chrome/Ceramic 的判据 [本报告推导]

||||
|---|---|---|
|ELC 与 Facial 同为 Indirect，却分别使用 陶瓷 与 镀铬|Ch1 SLIDE 5, 7, 8 + SLIDE 10, 11|涂布形式（是否经 applicator roll 中转）不决定雕刻平台|
|真正与平台完全对齐的是三条产线的图案复杂度：DRC / OLU / ELC 均有 Engineered patterns，Facial 被单独归为镀铬|SLIDE 20："Engineered patterns - DRC/OLU/Facial" —— 注意 Facial 也在 Engineered patterns 之内|故「图案复杂度」同样不能单独解释|
|Facial 的实际图案形态为 alternating bands of 2 BCM and 6 BCM + dead bands|SLIDE 10 — SPEAKER NOTES|Facial 的图案是带状（banded）+ 大量死区，而非全场连续网穴|

#### 4.1-c 为什么 Facial 仍保留镀铬辊（Why Facial still uses chrome rolls）

|||||
|---|---|---|---|
|1|成本优先：Facial 属大批量、对图案精度容忍度相对高的应用，镀铬的 lower cost 足以覆盖其需求|SLIDE 10：*"Pros - lower cost"；SLIDE 11："Cons - Higher cost"*|✅ 有直接原文支撑|
|2|图案形态适配机电雕刻：Facial 是带状 + 死区（2/6 BCM bands + dead bands），而非高密度精细网穴场 → 不触及镀铬辊的 engraving limitations|SLIDE 10 — SPEAKER NOTES：*"alternating bands of 2 BCM and 6 BCM and some dead bands designed for areas where no transfer will take place"；SLIDE 10："Cons - engraving limitations"*|✅ 有原文支撑（本报告推导其因果）|
|3|流体工况不要求陶瓷的耐腐蚀/耐磨优势：Facial 涂布的是护肤乳液（lotion），SLIDE 11 将陶瓷优势定位为 *"More resistant to corrosion and abrasion"*，暗示优势体现在腐蚀性/磨蚀性流体上|SLIDE 10 notes（*Facial Lotion*）；SLIDE 11（corrosion/abrasion）|⚠️ 部分支撑：本章未明确说明 lotion 为非腐蚀非磨蚀流体 → 关联为 本报告推导|
|4|转移一致性容忍度：镀铬的 variability due to plating inconsistency 对 Facial 可接受|SLIDE 10 Con|⚠️ 本章未说明 Facial 的公差容忍度 → [未找到原句]|
|5|规避陶瓷的抛光复杂度：Facial 有大量死区，若改用陶瓷，将落入 SLIDE 20 的 "Large amount of unengraved area = more complex polishing" 陷阱|SLIDE 10 notes（dead bands）+ SLIDE 20|✅ 有原文支撑（本报告推导其因果） —— 这是最被低估的一条|
|6|切换成本 / 既有资产惯性 / 供应商资质|—|❌ [未找到原句] —— 本章无任何切换成本或资产管理内容|
|7|线速度差异|—|❌ [未找到原句] —— 本章未提线速度|




综合判断 [本报告推导]：Facial 保留镀铬是 解释 1（成本）+ 2（图案形态不触碰机电雕刻的局限）+ 5（避开陶瓷抛光复杂度） 三者叠加的结果，而非「Indirect 工艺需要镀铬」。SLIDE 20 把 Facial 与 DRC/OLU 同列为 Engineered patterns，说明 Facial 并非「低技术」产线——它只是用带状+死区的复杂图案，换取了机电雕刻平台仍可覆盖的工艺难度。

#### 4.1-d 与 Ch1 的术语链条

||||
|---|---|---|
|凹版辊定义|"Engraved roll that delivers a precise amount of fluid to a substrate" (Ch1 SLIDE 2)|Ch2 把 "precise amount" 操作化为 BCM / cm³/m² / LPI 三个可测量轴（SLIDE 16, 18）|
|凹版辊 = 涂布心脏|"Considered the “Heart” of printing/coating process" (Ch1 SLIDE 2)|Ch2 揭示「心脏」的制造复杂度：10 道工序（SLIDE 12）|
|Gravure vs Anilox|"Gravure roll has an industry connotation of direct to substrate and patterned. Anilox roll is more indirect and common/simple engraving" (Ch1 SLIDE 2 notes)|Ch2 用 SLIDE 13（Standard Ceramic Anilox Engravings，6 种）vs SLIDE 20（Unique KC Gravure rolls）把该术语差异制度化为标准品与定制品的二分|
|商业价值|"Enhanced properties create Premium products… Higher margins" (Ch1 SLIDE 4)|Ch2 给出价值实现的技术路径："Not just printing/coating …. Creating product properties" (SLIDE 20)|

### 4.2 与后章 Ch3（Vendors & Patterns）："outside engravers comfort zones" → 供应商爬坡困难的因果链

#### 4.2-a 因果链全表

|||||
|---|---|---|---|
|① 因（Ch2）|KC 规格本质是 Outside the engravers comfort zones|SLIDE 20|原文|
|② 因（Ch2）|表现为 "Deep" engravings、"Large" cells|SLIDE 20|原文|
|③ 因（Ch2）|且 Large amount of unengraved area = more complex polishing（后处理难度独立放大）|SLIDE 20|原文|
|④ 因（Ch2）|雕刻商 have no insight beyond the cell dimensions → 无法自行优化|SLIDE 20 — SPEAKER NOTES|原文|
|⑤ 果（Ch3）|仅 4 家 Key Vendors，全部位于美国|Ch3 SLIDE 22 图像内容补充|原文（图像）|
|⑥ 果（Ch3）|产线对雕刻辊的依赖是刚性的： "Tissue machine can't run without 2 functional gravure rolls"|Ch3 SLIDE 23 — SPEAKER NOTES|原文|
|⑦ 果（Ch3）|雕刻质量缺陷："Engraving – 1/3 of dot is still filled with ceramic 'shell'"|Ch3 SLIDE 34 图像内容补充|原文（图像）|
|⑧ 果（Ch4）|首件周期极长："Harper took 9 months to engrave first roll and then had a large volume skew"|Ch4 SLIDE 34 — SPEAKER NOTES|原文|
|⑨ 果（Ch4）|换供应商即换量具体系："Did not measure volume with same tools so none of the data translated"|Ch4 SLIDE 34 — SPEAKER NOTES|原文|
|⑩ 果（Ch4）|一致性长期不达标，直到新供应商上线："struggled with engraving consistency and quality until Pamarco came on line in Q3 2024"|Ch4 SLIDE 32 — SPEAKER NOTES|原文|
|⑪ 果（Ch4）|首次试雕的定量缺口：1100 GMT vs 1800 目标；1550 GMT vs 1800 目标|Ch4 SLIDE 29 / 30 — SPEAKER NOTES|原文|

#### 4.2-b 因果强度评级表 [本报告推导]

|||||
|---|---|---|---|
|Outside the engravers comfort zones|VENUS 首件耗时 9 个月（Harper）|强|越界 → 需新工艺开发；Ch4 SLIDE 34 原文直接记录|
|"Deep" engravings + "Large" cells|1/3 网穴残留 ceramic 'shell'（雕刻未透）|强|深/大 → 去除量↑ → 未透风险↑；Ch3 SLIDE 34 图像内容补充|
|Large amount of unengraved area → more complex polishing|Re-Polish #1 / #2 / #3（三次重抛光）|中-强|抛光复杂 → 一次通过率低；Ch3 SLIDE 31 图像内容补充|
|Engravers have no insight beyond the cell dimensions|KC 必须自定 8 个参数中的 6 个|强（结构性）|SLIDE 20 notes + SLIDE 21 参数框|
|Vendor options due to chrome 6（另因）|Key Vendors 仅 4 家|中|SLIDE 10 + Ch3 SLIDE 22；但本章未证明二者直接因果 → 关联为推导|
|（Ch2 未涉及）|"Moving fast to meet pre-determined trial dates has created some non-ideal engravings"|—|Ch4 SLIDE 34 — SPEAKER NOTES —— 该后果的因在进度压力，不在 Ch2 的技术特性|

#### 4.2-c 供应商爬坡曲线（由 Ch4 试雕数据反推）[本报告推导]

||||||||
|---|---|---|---|---|---|---|
|VIVA Trial #1|Pamarco（12/3/24）|1100|1800|61.1%|−38.9%|Ch4 SLIDE 29 — SPEAKER NOTES|
|VIVA Trial #1|Apex（2/12/25）|1550|1800|86.1%|−13.9%|Ch4 SLIDE 30 — SPEAKER NOTES|
|VIVA Trial #2|Apex（Ran for 24 Hours）|—|—|—|需 Re-Polish ×3|Ch3 SLIDE 31|




爬坡结论 [本报告推导]：同一规格下不同供应商首件达标率差 25 个百分点（61% vs 86%），且第二名仍需 3 次重抛光。这与 SLIDE 20 的 "Outside the engravers comfort zones" 完全吻合：越界规格意味着供应商能力差异被放大，供应商选择从「商务决策」升级为「技术风险管理决策」。

### 4.3 与后章 Ch4（Trials & Design）：三参数只能锁两个的伏笔

#### 4.3-a 伏笔对照表

||||||
|---|---|---|---|---|
|标准规格 = 3 个参数|"Cell geometry, lines per inch, cell volume" (SLIDE 16)|其中 volume/depth/diameter 三选二|"Can only specify 2 from the key engraving parameters of volume, depth, and diameter" (Ch4 SLIDE 36)|参数集伏笔|
|KC 独有规格 = 6 个参数（2 框）|*"Cell dimensions: Cell diameter / Cell depth / Cell volume"；"Pattern details: Shapes, sizes, spacing"* (SLIDE 21)|设计是迭代过程，且需带式辊加速|*"Gravure roll design is an iterative process"；"Banded gravure rolls can help speed up the iterative process"* (Ch4 SLIDE 36)|方法论伏笔|
|雕刻商只看网穴尺寸|"Engravers have no insight beyond the cell dimensions" (SLIDE 20 notes)|因此必须由 KC 定义「什么网穴 → 什么产品属性」|"What cell design is necessary for desired product attributes" (Ch4 SLIDE 36)|责任归属伏笔|
|Cell diameter 与 Cell depth 被列为独立参数|SLIDE 21 紫框|二者映射到不同的产品属性：diameter → GMT；depth → Z 剥离强度|*"X and Y direction sheet surface coverage - Key to GMT (Cell diameter)"；"Z direction sheet penetration - Key to VIVA/WypAll Z peel strength (Cell depth)"* (Ch4 SLIDE 35)|属性映射伏笔（Ch2 埋参数，Ch4 埋语义）|
|Cell volume 单位定义（BCM）|SLIDE 18, 19|容积测量需专用量具，且不同量具数据不可比|"Capatch strips / Impression strips / 3DQC measurement system" (Ch4 SLIDE 37)；"Did not measure volume with same tools so none of the data translated" (Ch4 SLIDE 34 notes)|计量学伏笔|
|抛光 = 强制工序|"Polishing is required to remove the corner peaks" (SLIDE 14)|抛光是多次迭代、可改变容积的变量|"Re-Polish #1 / #2 / #3" (Ch3 SLIDE 31)；"POLISHING NOTE: Target <= 10,700,000 Shallow Dot Volume Average" (Ch3 SLIDE 28 图像内容补充)|工序变量伏笔|

#### 4.3-b 「同一容积可由不同直径/深度组合达成」——Ch2 与 Ch4 的闭环

||||
|---|---|---|
|1|Ch2 定义 volume 为单位面积积分量："Total volume of all the engraved cells on the roll surface per unit area of the surface"|SLIDE 18|
|2|因此 volume 不唯一决定 cell 的几何形状|本报告推导（由 1 直接得出）|
|3|Ch4 明确揭晓："Same volume from different combinations of diameter vs depth"|Ch4 SLIDE 36|
|4|且不同组合给出不同产品属性（diameter→GMT，depth→Z 剥离）|Ch4 SLIDE 35|
|5|故规格必须锁 volume + (diameter 或 depth) 二选一|Ch4 SLIDE 36|




闭环结论：Ch2 把 volume 定义为积分量（SLIDE 18），这在数学上就已经蕴含了 Ch4 的「三选二」约束。Ch2 SLIDE 18 是 Ch4 SLIDE 36 的数学前提，二者构成完整的逻辑链。

#### 4.3-c Ch2 SLIDE 17 事故与 Ch4 试雕偏差的量化对照 [本报告推导]

||||||
|---|---|---|---|---|
|单位错误（LPI vs LPcm）|单穴容积 ×6.45|✅ 完全可预防（纯文书错误）|规格书强制双单位标注 + 双复核|SLIDE 17|
|供应商能力差异|首件达标率差 25 个百分点|⚠️ 部分可预防|供应商技术评审 + 爬坡期|Ch4 SLIDE 29, 30|
|量具体系不一致|数据完全不可比（*"none of the data translated"*）|✅ 可预防|合同锁定测量方法与量具|Ch4 SLIDE 34 notes|
|进度压力|"created some non-ideal engravings"|⚠️ 管理问题|试雕日程预留爬坡裕度|Ch4 SLIDE 34 notes|




关键洞察 [本报告推导]：最严重的一类偏差（×6.45）恰恰是成本最低即可消除的一类——它不需要任何新技术、新设备或新供应商，只需要规格书的一个书写规范。这是 Ch2 对整份课程最具杠杆价值的结论。

## 模块 5：业务连接点（Business Connections）



业务背景：卫材（纸尿裤 / 湿巾）创新研发 ＋ 木浆与纸品战略采购
说明：本模块所有数值若非引自章节，均标 本报告推导；章节未覆盖的法规/市场内容标 外部背景，非本章内容。

### 连接点 1 — ⚠️ 单位陷阱 LPI vs LPcm：规格书的强制规范

涉及幻灯片：SLIDE 16、SLIDE 17（含 SPEAKER NOTES）、SLIDE 18（含 SPEAKER NOTES）、Ch4 SLIDE 34 — SPEAKER NOTES

核心概念：Line Screen / LPI / LPcm（C5）；BCM（C3）；cm³/m²（C4）；Cell volume（C7）

关键数据
| 数据 | 值 | 来源 |
|---|---|---|
| 事故 | Jenks L12 Bath Gravure Rolls – Fall of 2022 | SLIDE 17 |
| 混淆对 | 180 Lines/cm vs 180 Lines/inch，均标 "6 BCM VOLUME" | SLIDE 17 |
| 换算 A | 180 LCM = 460 LPI（精算 457.2） | SLIDE 17 notes |
| 换算 B | 180 LPI = 70 LCM（精算 70.87） | SLIDE 17 notes |
| 单穴容积比 | 6.45×（= 2.54²） | 本报告推导 |
| 正确规格范例 | 60 degree hex, 180 LPI, 6.0 BCM | SLIDE 16 |
| 二次风险 | "Did not measure volume with same tools so none of the data translated" | Ch4 SLIDE 34 notes |

可执行行动建议（可直接落地）
1. 【强制双单位】 规格书与图纸中的线数一律写成 180 LPI (= 70.9 LPcm) 或 180 LPcm (= 457.2 LPI)——括号内换算值必须并列印刷，不得只留其一。依据：SLIDE 17 事故 + SLIDE 18 notes *"USA combines metric and English units"*。
2. 【强制三参数同锁】 任何雕刻规格必须同时写明：① Cell geometry（含角度）+ ② Line screen（含单位）+ ③ Cell volume（含单位），三者缺一即退回。依据：SLIDE 16 *"Cell geometry, lines per inch, cell volume"*。
3. 【体积双单位并列】 体积写成 6.0 BCM/in² (= 9.30 cm³/m²)。禁止单独使用 "BCM" 简称，因为 SLIDE 18 原文即指出 "More commonly just referred to as BCM" —— 丢掉 /in² 正是事故温床。
4. 【加一道可复核的物理量】 增加 等效平均湿膜厚度 μm 一栏（h(μm) = BCM × 1.55，本报告推导）。因其量纲直观（9.30 μm），非专业人员也能立即识别数量级错误，是最廉价的兜底校验。
5. 【锁定测量方法与量具】 合同中写明体积测量方法（对应 Ch4 SLIDE 37 的 Capatch strips / Impression strips / 3DQC）与验收量具型号。依据：Ch4 SLIDE 34 notes 明确不同量具数据不可比。
6. 【图纸数值口径书面澄清】 针对 Ch3 SLIDE 28 的 "27,600,000 cubic microns (27.6 BCM)" 1,000 倍口径矛盾，向图纸签发方发函确认是单穴容积还是整辊 BCM（见 T4-f）。
7. 【来料检验加线数项】 入厂验收清单中，线数（LPI）与体积（BCM）并列检验，不得只测体积。因为 SLIDE 17 证明二者可独立偏离。

### 连接点 2 — 六价铬（Chrome 6）对供应商选择的限制：环保法规如何重塑雕刻辊供应链

涉及幻灯片：SLIDE 10（*vendor options due to chrome 6*）、SLIDE 11（*vendor competition*）、SLIDE 12（陶瓷层材料）、Ch3 SLIDE 22（Key Vendors）

核心概念：Chrome 6 restriction（C11）；Electro-mechanical Engraved Chrome Roll（C1）；Laser Engraved Ceramic Roll（C2）；Ceramic Plasma Spray = Chromium Oxide/titanium（C9）

关键数据
| 数据 | 值 | 来源 |
|---|---|---|
| 镀铬辊 Con（原文） | "vendor options due to chrome 6" | SLIDE 10 |
| 陶瓷辊 Pro（原文，镜像） | "vendor competition" | SLIDE 11 |
| KC Key Vendors 数量 | 4 家 | Ch3 SLIDE 22 图像内容补充 |
| 供应商清单 | Harper（Charlotte, NC）／Precision Roll Solutions / IR Engraving（Richmond, VA）／Pamarco（Atlanta, GA）／Apex（Pittsburgh, PA） | Ch3 SLIDE 22 图像内容补充 |
| 陶瓷面层材料 | Chromium Oxide/titanium | SLIDE 12 |
| 陶瓷粘结层材料 | Nickel-Chrome | SLIDE 12 |
| 镀铬辊另一 Con | "variability due to plating inconsistency" | SLIDE 10 |
| 产线刚性 | "Tissue machine can't run without 2 functional gravure rolls" | Ch3 SLIDE 23 notes |

⚠️ 法规边界声明：本章未给出任何法规名称、限值、生效日期或地区 → 全部 [未找到原句]。以下涉及具体法规的分析属 外部背景，非本章内容。

可执行行动建议
1. 【把 chrome 6 从「技术问题」重定义为「供应链集中度风险」】 本报告推导：SLIDE 10 把 chrome 6 表述为 vendor options ↓（而非产品性能问题），且与之并列的 Con 是 plating inconsistency。因此其真实业务影响是双重的：可选供应商变少 ＋ 质量波动变大，且二者同时发生。采购策略应按「单一来源风险」而非「合规事项」管理。
2. 【对两处「铬」做区分管理】 本报告推导：SLIDE 10 的 chrome 6 指向电镀铬辊；SLIDE 12 的陶瓷面层是 Chromium Oxide（通常为三价 Cr₂O₃）。但本章原文未做任何价态声明，因此不得据此宣称陶瓷辊即合规豁免——必须逐家供应商索取材料声明（RoHS / REACH / SDS）与电镀工艺说明，并写入采购技术协议。
3. 【对 4 家现有供应商做 chrome 6 敞口尽调】 本报告推导：用 Ch3 SLIDE 22 名单逐家核查：① 是否仍提供电镀铬辊；② 六价铬工艺的环保许可与废液处理能力；③ 是否已在向陶瓷/替代工艺转型。敞口高的供应商应触发备选开发。
4. 【国内供应商：机会与壁垒并存 — 分平台判断】 本报告推导 / 外部背景，非本章内容：
   | 维度 | 判断 | 依据 |
   |---|---|---|
   | 激光陶瓷辊（OLU/DRC/ELC 类） | 机会为主 | 陶瓷路线本就享有 *"vendor competition"*（SLIDE 11），不受 chrome 6 约束；瓶颈在雕刻能力而非法规 |
   | 机电镀铬辊（Facial 类） | 壁垒为主 | 受限的正是这条路（SLIDE 10）；国内供应商即便成本更低，也需先解决六价铬合规与** plating 一致性**（SLIDE 10 的并列 Con） |
   | 共同的真正壁垒 | 能力壁垒 >> 法规壁垒 | SLIDE 20：KC 规格 *"Outside the engravers comfort zones"*；Ch4 SLIDE 34：Harper 首件 9 个月。国内供应商的机会窗口在陶瓷，但爬坡曲线仍长 |
5. 【把「抛光能力」设为供应商准入的独立门槛】 本报告推导：SLIDE 20 指出 KC 的 *"Large amount of unengraved area = more complex polishing"*，且 Ch3 SLIDE 31 记录 Apex 需 3 次重抛光。故供应商审核中，抛光产能与一次通过率应与雕刻能力并列评估，不能只看激光机台。
6. 【战略采购的合同抓手】 依据 Ch3 SLIDE 23 notes（*"Tissue machine can't run without 2 functional gravure rolls"*）：雕刻辊是产线级刚性瓶颈件。建议对关键规格实行双源（dual-source）+ 备用辊库存，并把 首件周期（参照 Harper 的 9 个月）计入新供应商导入的商务模型。

### 连接点 3 — 镀铬 vs 陶瓷的 TCO 对比框架与选型决策树

涉及幻灯片：SLIDE 10、SLIDE 11、SLIDE 12、SLIDE 14、SLIDE 20、Ch3 SLIDE 31、Ch4 SLIDE 34

核心概念：C1 vs C2 全部 Pros/Cons 字段；Final polishing（T2 Step 10）；corner peaks → doctor blade wear（SLIDE 14）

⚠️ 数据边界：本章未给出任何成本金额、寿命小时数、磨损率、停机时长或次数 → 全部 [未找到原句]。以下为框架，不含编造数据。

TCO 框架表 [本报告推导]（四轴 + 两放大项，字段全部来自 SLIDE 10/11 原文）
| # | TCO 轴 | 镀铬（Electro-mechanical） | 陶瓷（Laser） | 数据来源 | 量化数据 |
|---|---|---|---|---|---|
| 1 | 初始成本 (Initial cost) | lower cost ✅ 优 | Higher cost ❌ 劣 | SLIDE 10 / SLIDE 11 | [未找到原句] 无金额 |
| 2 | 寿命 (Engraving life) | shorter ❌ 劣 | longer ✅ 优 | SLIDE 10 / SLIDE 11 | [未找到原句] 无小时数 |
| 3 | 一致性 (Transfer consistency) | variability due to plating inconsistency ❌ 劣 | more precise and consistent ✅ 优 | SLIDE 10 / SLIDE 11 | [未找到原句] 无公差 |
| 4 | 停机损失 (Downtime) | 由轴 2 派生：寿命短 → 换辊频次↑ → 停机↑ | 由轴 2 派生：寿命长 → 换辊频次↓ | 本报告推导（由 SLIDE 10/11 寿命字段推出） | [未找到原句] |
| 5 | 供应风险（放大项） | vendor options due to chrome 6 ❌ 劣 | vendor competition ✅ 优 | SLIDE 10 / SLIDE 11 | 供应商数 4（Ch3 SLIDE 22） |
| 6 | 图案能力（放大项） | engraving limitations ❌ 劣 | more engraving flexibility ✅ 优 | SLIDE 10 / SLIDE 11 | — |
| 7 | 耐腐蚀/耐磨（放大项） | [未找到原句] | More resistant to corrosion and abrasion ✅ | SLIDE 11 | — |
| 8 | 抛光迭代成本（KC 特有放大项） | 机电雕刻，无激光角峰机制 | Final polishing 必需（SLIDE 12 Step 10）+ 未雕刻面积大 → 抛光更复杂（SLIDE 20）；实证需 Re-Polish ×3（Ch3 SLIDE 31） | SLIDE 14 / SLIDE 20 / Ch3 SLIDE 31 | 重抛光次数 3（Apex VIVA Trial #2） |

TCO 判定逻辑式 [本报告推导]

TCO(平台) = C_initial
          + (T_horizon ÷ L_life) × (C_refurb + C_downtime_per_change)
          + C_quality(variability)
          + C_supply_risk
          + C_polish_iterations
其中（全部来自 SLIDE 10/11 的定性方向）：
  C_initial        : 镀铬 < 陶瓷          （原文 "lower cost" vs "Higher cost"）
  L_life           : 镀铬 < 陶瓷          （原文 "shorter" vs "longer engraving life"）
  C_quality        : 镀铬 > 陶瓷          （原文 "variability due to plating inconsistency" vs "more precise and consistent"）
  C_supply_risk    : 镀铬 > 陶瓷          （原文 "vendor options due to chrome 6" vs "vendor competition"）
  C_polish_itr     : 镀铬 ≈ 0 < 陶瓷      （陶瓷独有；实证 Re-Polish ×3，Ch3 SLIDE 31）
→ 结论：陶瓷在 5 项中占优 4 项，仅在 C_initial 与 C_polish_itr 两项处劣势。
→ 决策关键变量 = T_horizon ÷ L_life（换辊次数）。
   换辊次数越多，陶瓷的 life/consistency/supply 优势被放大得越充分；
   换辊次数极少（短周期、一次性、样品级）时，镀铬的 lower cost 才可能占优。
※ 本章未提供任何数值以解此式 → 需填入本方实际成本参数后方可量化。

选型决策树（Decision Tree）[本报告推导]

Q1 图案是否为 Engineered pattern（非标准 6 种 anilox）？          [SLIDE 13 vs SLIDE 20]
   ├─ NO  → Q1a 是否大批量/标准涂布？ → YES → 【镀铬】成本优先     [SLIDE 10 "lower cost"]
   └─ YES ↓
Q2 是否含 "Deep" engraving 或 "Large" cells？                     [SLIDE 20]
   ├─ YES → 【陶瓷】镀铬存在 "engraving limitations"              [SLIDE 10]
   └─ NO  ↓
Q3 流体是否腐蚀性 / 磨蚀性？                                      [SLIDE 11 "corrosion and abrasion"]
   ├─ YES → 【陶瓷】                                              [SLIDE 11]
   └─ NO  ↓
Q4 是否含大量未雕刻区（dead bands / banded pattern）？            [SLIDE 10 notes, SLIDE 20]
   ├─ YES → 重新评估【镀铬】—— 陶瓷将面临 "more complex polishing" [SLIDE 20]
   │        （这正是 Facial 保留镀铬的路径，见 4.1-c 解释 5）
   └─ NO  ↓
Q5 转移一致性是否为关键质量指标？                                 [SLIDE 10 vs SLIDE 11]
   ├─ YES → 【陶瓷】                                              [SLIDE 11 "more precise and consistent"]
   └─ NO  ↓
Q6 供应基础是否已受 chrome 6 压缩？                               [SLIDE 10]
   ├─ YES → 【陶瓷】+ 启动双源开发                                [SLIDE 10, Ch3 SLIDE 22]
   └─ NO  → 【镀铬】可作为成本方案，但需监控 vendor options 变化



决策树使用须知：Q4 是唯一的「回退到镀铬」分支，其依据是 SLIDE 10 notes 的 dead bands 与 SLIDE 20 的 more complex polishing 的组合。这是本决策树中最容易被忽略、但对本方（卫材常需分区/带状涂布）最关键的一条。

### 连接点 4 — 若导入功能性涂布（护肤乳液 / 导流层处理剂）：雕刻规格的初始设定建议

涉及幻灯片：SLIDE 10（含 notes）、SLIDE 16、SLIDE 18、SLIDE 20、SLIDE 21、Ch4 SLIDE 35、Ch4 SLIDE 36、Ch4 SLIDE 37

核心概念：C3–C7（BCM / cm³/m² / LPI / 60° hex / cell diameter-depth-volume）；C12（engraving window）；Ch4 SLIDE 35 的属性映射

关键数据（全部为章节内实证值，非编造）
| 应用 | 规格 | 换算（本报告推导） | 来源 |
|---|---|---|---|
| 护肤乳液（Facial Lotion） 低涂布带 | 2 BCM | 3.10 cm³/m² = 3.10 μm | SLIDE 10 notes |
| 护肤乳液（Facial Lotion） 高涂布带 | 6 BCM | 9.30 cm³/m² = 9.30 μm | SLIDE 10 notes |
| 护肤乳液 非转移区 | dead bands（*designed for areas where no transfer will take place*） | 0 | SLIDE 10 notes |
| 2-ply bath 通用起点 | 60 degree hex, 180 LPI, 6.0 BCM | pitch 141.1 μm；37,412 cells/in²；单穴 160,375 μm³ | SLIDE 16 + 推导 |
| 属性映射规则 | Cell diameter → X/Y 覆盖 → GMT；Cell depth → Z 渗透 → Z 剥离强度 | — | Ch4 SLIDE 35 |
| 过渗透风险 | "High Z direction penetration can also negatively impact bulk/caliper" | — | Ch4 SLIDE 35 |
| 自由度约束 | "Can only specify 2 from the key engraving parameters of volume, depth, and diameter" | — | Ch4 SLIDE 36 |
| 迭代加速手段 | "Banded gravure rolls can help speed up the iterative process – typically don't produce sellable product – RSR not MSR" | — | Ch4 SLIDE 36 |
| 量具 | Capatch strips / Impression strips / 3DQC measurement system | — | Ch4 SLIDE 37 |

可执行行动建议（初始设定方案）[本报告推导]

Step 1 — 选平台：功能性涂布若为分区/带状（导流层处理剂常见），走 Q4 分支 → 先评估镀铬（成本 + 规避抛光复杂度）；若为全场连续功能层或含深/大网穴 → 陶瓷。
> 依据：SLIDE 10（镀铬 lower cost + Facial 带状实证）、SLIDE 20（未雕刻区 → 抛光更复杂）。

Step 2 — 设定体积起点（锚定已知实证值，不外推）：
| 功能涂布类型 | 建议起始 BCM | 依据（章节内实证锚点） |
|---|---|---|
| 护肤乳液（lotion，低涂布） | 2.0 BCM（= 3.10 cm³/m² = 3.10 μm） | SLIDE 10 notes 的 Jenks Facial Lotion GR 2 BCM 带 |
| 护肤乳液（lotion，高涂布） | 6.0 BCM（= 9.30 cm³/m² = 9.30 μm） | SLIDE 10 notes 的 6 BCM 带 |
| 导流层处理剂（ADL treatment，通用起点） | 6.0 BCM（= 9.30 μm） | SLIDE 16 的 2-ply bath 6.0 BCM —— 本章唯一给出的完整标准规格 |
| 非涂布区 | dead bands（0 转移） | SLIDE 10 notes |

Step 3 — 设定线数与几何起点：直接采用 SLIDE 16 的完整三参数：60 degree hex, 180 LPI, 6.0 BCM。
> 理由（本报告推导）：这是本章唯一被完整规格化的实例，且覆盖 SLIDE 16 定义的全部三个标准参数轴。它同时给出了可复核的派生量：pitch 141.1 μm、37,412 cells/in²、单穴 160,375 μm³。用已知规格作起点，可把变量收敛到「只调体积」一维。

Step 4 — 遵守三选二约束，明确放弃哪一个自由度：
| 优先级 | 锁定组合 | 放弃项 | 适用场景 | 依据 |
|---|---|---|---|---|
| A（推荐） | volume + diameter | depth | 关注 GMT / 表面覆盖 的功能层 | Ch4 SLIDE 35：diameter → X/Y coverage → GMT |
| B | volume + depth | diameter | 关注 渗透 / Z 向强度 的功能层 | Ch4 SLIDE 35：depth → Z penetration → Z peel |
| A/B 的选择判据 | — | — | 导流层处理剂倾向 A（覆盖/导流均匀性）；护肤乳液倾向 A（表面驻留、低渗透） | 本报告推导 —— Ch4 SLIDE 35 同时警告 *"High Z direction penetration can also negatively impact bulk/caliper"*，故功能涂布普遍应避免过深渗透，优先锁 diameter |

Step 5 — 用带式辊（banded roll）加速迭代：一次上线 2 / 3 / 4.5 / 6 BCM 多条带（沿用 SLIDE 10 notes 的 banded precedent），一次试机覆盖多档涂布量。
> 依据：Ch4 SLIDE 36 *"Banded gravure rolls can help speed up the iterative process"*；SLIDE 10 notes *"alternating bands of 2 BCM and 6 BCM"*。
> ⚠️ 注意：Ch4 SLIDE 36 明确带状辊 "typically don't produce sellable product – RSR not MSR" → 只能用于研发，不可用于量产。

Step 6 — 锁定量具体系：从首件起即统一使用同一测量体系（Capatch strips / Impression strips / 3DQC 三选一并写进规格书）。
> 依据：Ch4 SLIDE 37；Ch4 SLIDE 34 notes "Did not measure volume with same tools so none of the data translated" —— 换量具即数据断裂。

Step 7 — 预留爬坡裕度：首件周期按 最坏 9 个月规划，首次试雕达标率按 61%–86% 规划（本报告推导，由 Ch4 SLIDE 29/30 的 1100/1550 vs 1800 反算）。
> 依据：Ch4 SLIDE 34 notes（Harper 9 个月）；Ch4 SLIDE 29/30 notes。

### 模块 5 附：可直接用于工艺参数选择的数据清单表（Ready-to-Use Data Sheet）

|||||||
|---|---|---|---|---|---|
|1|标准规格三要素|Cell geometry, lines per inch, cell volume|—|SLIDE 16|原文|
|2|2-ply bath 完整规格|60 degree hex, 180 LPI, 6.0 BCM|—|SLIDE 16|原文（推荐起点）|
|3|Facial Lotion 低带体积|2.0|BCM/in²|SLIDE 10 notes|原文|
|4|Facial Lotion 高带体积|6.0|BCM/in²|SLIDE 10 notes|原文|
|5|Facial Lotion 图案形态|alternating bands (2/6 BCM) + dead bands|—|SLIDE 10 notes|原文|
|6|BCM → cm³/m² 因子|1.55|—|SLIDE 18|原文（推导复核 ✔）|
|7|BCM → μm 湿膜因子|1.55|μm per BCM/in²|本报告推导|推导（双路径互证 ✔）|
|8|1 BCM|10⁹ μm³ = 1 mm³ = 10⁻³ cm³|—|SLIDE 19 + 推导|原文 + 自洽验证 ✔|
|9|1,000 μm = 1 mm|—|—|SLIDE 19|原文|
|10|LCM → LPI 因子|× 2.54（180 LCM = 460 LPI / 457.2）|—|SLIDE 17 notes|原文|
|11|LPI → LCM 因子|÷ 2.54（180 LPI = 70 LCM / 70.87）|—|SLIDE 17 notes|原文|
|12|60° hex 面密度公式|N = 1.1547 × L²（cells/in²）|—|本报告推导|推导|
|13|180 LPI 网穴中心距|141.1|μm|本报告推导|推导|
|14|457.2 LPI 网穴中心距|55.56|μm|本报告推导|推导|
|15|180 LPI 网穴密度|37,412|cells/in²|本报告推导|推导|
|16|457.2 LPI 网穴密度|241,369|cells/in²|本报告推导|推导|
|17|单穴容积 @180 LPI / 6 BCM|160,375|μm³|本报告推导|推导|
|18|单穴容积 @457.2 LPI / 6 BCM|24,858|μm³|本报告推导|推导|
|19|单位事故放大倍数|6.45（= 2.54²）|×|本报告推导|推导（由 SLIDE 17 标定）|
|20|6.0 BCM 等效湿膜|9.30|μm|本报告推导|推导|
|21|2.0 BCM 等效湿膜|3.10|μm|本报告推导|推导|
|22|激光初始孔径|~10|μm|SLIDE 14|原文|
|23|角部激光照射倍数|≥ 3|× vs side walls|SLIDE 14|原文|
|24|抛光|必需（去除角峰，消除过度刮刀磨损）|—|SLIDE 14|原文|
|25|陶瓷辊生产工序数|10（雕刻 = Step 9，最终抛光 = Step 10）|—|SLIDE 12|原文|
|26|Bond coat 材料|Nickel-Chrome（Plasma Spray）|—|SLIDE 12|原文|
|27|Ceramic coat 材料|Chromium Oxide/titanium（Plasma Spray）|—|SLIDE 12|原文|
|28|KC 独有规格参数数|6（紫框 3 + 绿框 3）；去重后总参数 8，独立可控 ≤ 6|—|SLIDE 21 + 推导|原文 + 推导|
|29|标准 anilox 图案数|6（60° Hex / GTT / 45° / Longcell / Channellox / Trihelical）|—|SLIDE 13 图像内容补充|原文（图像）|
|30|KC Key Vendors 数|4（Harper / Precision Roll Solutions-IR Engraving / Pamarco / Apex），全在美国|—|Ch3 SLIDE 22 图像内容补充|原文（图像）|
|31|首件周期（最坏实证）|9 个月（Harper，VENUS 首辊）|月|Ch4 SLIDE 34 notes|原文|
|32|首件达标率区间|61.1%（Pamarco 1100/1800）– 86.1%（Apex 1550/1800）|%|Ch4 SLIDE 29/30 notes + 推导|原文 + 推导|
|33|重抛光次数（实证）|3（Apex VIVA Trial #2，Re-Polish #1/#2/#3）|次|Ch3 SLIDE 31 图像内容补充|原文（图像）|
|34|三选二约束|volume / depth / diameter 只能锁 2 个|—|Ch4 SLIDE 36|原文|
|35|属性映射|diameter → GMT；depth → Z peel strength|—|Ch4 SLIDE 35|原文|
|36|过渗透警告|"High Z direction penetration can also negatively impact bulk/caliper"|—|Ch4 SLIDE 35|原文|
|37|量具清单|Capatch strips / Impression strips / 3DQC measurement system|—|Ch4 SLIDE 37|原文|
|38|量具一致性警告|不同量具数据不可比（*"none of the data translated"*）|—|Ch4 SLIDE 34 notes|原文|

## 模块 6：金句索引（Key Quotes Index）

Q1
> "Electro-mechanical Engraved Chrome Rolls (Facial) — Pros - lower cost / Cons - shorter engraving life, engraving limitations, variability due to plating inconsistency, vendor options due to chrome 6"
SLIDE 10
- 中文翻译：机电雕刻镀铬辊（Facial）— 优点：成本更低。缺点：雕刻寿命更短、雕刻存在局限、因电镀不一致而产生波动、因六价铬而导致供应商选择受限。
- 为什么记：这是全章对镀铬平台唯一且完整的定性定义，一句覆盖成本、寿命、能力、质量、供应链五个维度。任何 TCO 或选型论证都必须回到这五个字段，否则就是无据推断。

Q2
> "Jenks Facial Lotion GR – alternating bands of 2 BCM and 6 BCM and some dead bands designed for areas where no transfer will take place"
SLIDE 10 — SPEAKER NOTES
- 中文翻译：Jenks 护肤乳液凹版辊 —— 2 BCM 与 6 BCM 的交替条带，以及一些「死区」条带，专为不发生转移的区域而设计。
- 为什么记：唯一给出具体 BCM 数值 + 带状图案 + 死区三合一的实例。它同时回答了两个问题：护肤乳液的涂布量起点（2 / 6 BCM），以及 KC 如何在单辊上实现分区功能涂布。是本方导入功能涂布时最直接的先例。

Q3
> "Laser Engraved Ceramic Rolls (OLU/DRC/ELCs) — Pros - More resistant to corrosion and abrasion, longer engraving life, more engraving flexibility, more precise and consistent fluid transfer, vendor competition / Cons - Higher cost"
SLIDE 11
- 中文翻译：激光雕刻陶瓷辊（OLU/DRC/ELCs）— 优点：更耐腐蚀与磨损、雕刻寿命更长、雕刻柔性更大、流体转移更精确一致、供应商竞争充分。缺点：成本更高。
- 为什么记：与 Q1 构成镜像结构（1 Pro : 4 Cons 对 5 Pros : 1 Con），是本章论证「这是一个被管理的取舍、而非技术升级」的核心证据。同时它是陶瓷平台全部优势的唯一权威出处。

Q4
> "Ceramic Gravure Roll Production — Steel roll base / Corrosion resistance welding (if necessary) / Dynamic balancing / Grinding / Sand blasting / Bond Coat Plasma Spray = Nickel-Chrome / Ceramic Plasma Spray = Chromium Oxide/titanium / Grinding/Polishing / Laser engraving / Final polishing"
SLIDE 12
- 中文翻译：陶瓷凹版辊生产 —— 钢辊基体 / 耐腐蚀堆焊（如需要）/ 动平衡 / 磨削 / 喷砂 / 等离子喷涂粘结层 = 镍铬 / 等离子喷涂陶瓷层 = 氧化铬-钛 / 磨削抛光 / 激光雕刻 / 最终抛光。
- 为什么记：全章信息密度最高的一页。雕刻只占 10 道工序中的第 9 道，前面有 8 道、后面还有 1 道。它把「雕刻辊」从单一工序重新定义为一条 10 道工序的制造链，是供应商工艺审核清单的直接来源。

Q5
> "Circular laser beam that creates ~10 um round hole"
SLIDE 14
- 中文翻译：圆形激光束打出约 10 微米的圆孔。
- 为什么记：全章唯一的激光物理尺度参数。它设定了最小特征尺寸下限——任何小于约 10 μm 的网穴特征在物理上不可实现，这是判断雕刻商能否承接某规格的第一道硬门槛。

Q6
> "Engraving each subsequent hole pushes the cell walls to create a hexagon shape"
SLIDE 14
- 中文翻译：雕刻每一个后续孔时，会挤压网穴壁，从而形成六边形形状。
- 为什么记：揭示了六边形网穴的成因——它不是被铣削出来的，而是相邻孔挤压的副产物。这意味着网穴壁的完整性取决于激光重叠率，而非设计余量；也解释了为什么网穴壁是雕刻质量的关键变量。

Q7
> "Each corner is exposed to the laser a minimum of 3 times compared to the side walls"
SLIDE 14
- 中文翻译：每一个角部被激光照射的次数，相比侧壁至少多 3 倍。
- 为什么记：本章唯一给出激光能量分布定量不对称性的句子。它把「角峰 → 必须抛光」从经验之谈变成了可计算的几何事实，也为「KC 的大网穴/深雕刻会放大角峰与抛光难度」提供了推导起点。

Q8
> "Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear"
SLIDE 14
- 中文翻译：必须进行抛光，以去除角部的凸起峰，并消除过度的刮刀磨损。
- 为什么记：全章唯一把「网穴几何」直接连到「运营成本（刮刀磨损）」的因果句。其中 "required" 与 "excessive" 都是强限定词——抛光不是可选项，未抛光的后果不是轻微磨损而是过度磨损。这是把 Step 10 写入验收规范的原文依据。

Q9（SLIDE 16 —— 同页两句合并）
> "Standard Engraving Specifications — Cell geometry, lines per inch, cell volume"
> "2 ply bath specification = 60 degree hex, 180 LPI, 6.0 BCM"
SLIDE 16
- 中文翻译：（一）标准雕刻规格 —— 网穴几何、每英寸线数、网穴容积。（二）2 层浴巾规格 = 60 度六边形、180 LPI、6.0 BCM。
- 为什么记：第一句定义了规格书的最小完备参数集（3 个）——任何只写其中 1 或 2 个的规格书都是不完备的，SLIDE 17 的事故正是只写了第 3 个（6 BCM）而漏掉第 2 个的单位所致。第二句是全章唯一被完整规格化的实例、且三参数齐备，是新项目最安全的规格起点（本报告模块 5 连接点 4 即据此设定初始参数），并可派生出 pitch 141.1 μm、密度 37,412 cells/in²、单穴 160,375 μm³ 三套可复核量。一句给框架、一句给实例，同页必须成对记忆。

Q10（SLIDE 17 —— 正文与演讲者备注合并）
> "180 Lines/cm / 180 Lines/inch / BOTH “6 BCM VOLUME” / Jenks L12 Bath Gravure Rolls – Fall of 2022 / Importance of Line/Screen Count"
SLIDE 17
> "180 LCM = 460 LPI and 180 LPI = 70 LCM"
SLIDE 17 — SPEAKER NOTES
- 中文翻译：（正文）180 线/厘米 ／ 180 线/英寸 ／ 两者都是「6 BCM 容积」 ／ Jenks L12 浴巾凹版辊 —— 2022 年秋 ／ 线数/网线数的重要性。（备注）180 线/厘米 = 460 线/英寸；180 线/英寸 = 70 线/厘米。
- 为什么记：全章唯一的负面案例实证，也是全课最具商业价值的一页——它证明同一个体积数字可对应 6.45 倍差异的网穴结构（本报告推导），这是把「规格书必须双单位、三参数同锁」写进公司标准的唯一必要理由。备注句则是全章唯一的线数换算数值（精算值 457.2 / 70.87，原文取整），可直接用作规格书括号内换算值的原文出处，也是校验任何供应商报价单单位是否已混淆的最快工具。正文是事故，备注是解药，两句必须同记。

Q11（SLIDE 18 —— 正文与演讲者备注合并）
> "Gravure Roll Volume — Total volume of all the engraved cells on the roll surface per unit area of the surface / USA = BCM/in2 ……. More commonly just referred to as BCM / European = cm3/m2 / Conversion: / 1 BCM/in2 = 1.55 cm3/m2"
SLIDE 18
> "USA combines metric and English units"
SLIDE 18 — SPEAKER NOTES
- 中文翻译：（正文）凹版辊容积 —— 辊面上所有雕刻网穴的总容积，除以表面积。美制 = BCM/in²……通常简称为 BCM。欧制 = cm³/m²。换算：1 BCM/in² = 1.55 cm³/m²。（备注）美国的用法把公制和英制单位混在了一起。
- 为什么记：单位体系的宪法页。正文给出物理定义、两种单位与换算因子 1.55（本报告已用两条独立路径验证其正确），同时自己就埋了风险伏笔——"More commonly just referred to as BCM" 意味着 /in² 在日常使用中被丢弃，这正是 SLIDE 17 事故的语言学根源。备注句则是最短、最本质的风险说明：BCM 的体积部分是公制（μm³）、面积部分却是英制（in²），一旦任一环节默认「全部公制」，事故就会重演。建议把备注句直接印在规格书模板页眉作警示语。

Q12
> "1 Billion Cubic Microns (Micrometers) / 1 BCM = 1,000,000,000 um3 / 1,000 um = 1 mm"
SLIDE 19
- 中文翻译：十亿立方微米 —— 1 BCM = 1,000,000,000 μm³；1,000 μm = 1 mm。
- 为什么记：BCM 的定义页。由 1,000 μm = 1 mm 可直接推出 (10³ μm)³ = (1 mm)³，即 1 BCM = 1 mm³（本报告已用 SI 复核，完全自洽）。这是把 BCM 换算成任何体积单位的唯一基准，也是识别 Ch3 SLIDE 28 中 "27,600,000 cubic microns (27.6 BCM)" 存在 1,000 倍口径矛盾的判据。

Q16
> "Unique KC Gravure rolls / This is where the MAGIC happens / Engineered patterns - DRC/OLU/Facial / Outside the engravers comfort zones / “Deep” engravings / “Large” cells / Large amount of unengraved area = more complex polishing / Not just printing/coating …. Creating product properties"
SLIDE 20
- 中文翻译：KC 独有的凹版辊 / 魔力就发生在这里 / 工程化图案 —— DRC/OLU/Facial / 超出雕刻商的舒适区 / 「深」雕刻 / 「大」网穴 / 大量未雕刻区域 = 抛光更为复杂 / 不只是印刷与涂布……而是在创造产品属性。
- 为什么记：全章战略定位最高的一页，一次性给出 KC 雕刻的 5 项差异化特征 + 1 条明确因果（未雕刻区 → 抛光复杂）+ 1 句价值宣言。它是理解「为什么 KC 的供应商只有 4 家、为什么首件要 9 个月、为什么必须自定规格」的总纲。

Q17
> "KC has to be able to communicate the engraving specifications required to create product properties. Engravers have no insight beyond the cell dimensions"
SLIDE 20 — SPEAKER NOTES
- 中文翻译：KC 必须能够沟通「为创造产品属性所需的雕刻规格」。雕刻商对网穴尺寸之外一无所知。
- 为什么记：全章责任归属最明确的一句。它划定了 KC 与供应商的能力边界：供应商负责如何实现网穴，KC 负责需要什么网穴才能产生什么产品属性。这是「KC 必须自建规格翻译能力」这一组织要求的原文依据，也是本报告模块 5 连接点 4（KC 必须自行设定初始规格）的根本理由。

Q15
> "Engraving Specifications – Unique KC Engravings"
SLIDE 21
- 中文翻译：雕刻规格 —— KC 独有雕刻。（紫框 Cell dimensions：Cell diameter / Cell depth / Cell volume；绿框 Pattern details：Shapes, sizes, spacing）
- 为什么记：KC 独有规格的参数结构页，与 SLIDE 16 的 3 参数标准集形成对照（6 参数 / 2 组，去重后总 8 个）。注意该页只有参数类别、没有数值——这本身就是一条重要信息：KC 的独有规格尚未标准化，因此每一次新项目都需要从零定义，且必须遵守 Ch4 SLIDE 36 的「三选二」约束。



✅ 模块 6 正文共 15 条金句（Q1–Q15），全部出自本章 SLIDE 10–21。

### 模块 6 附录：跨章锚点金句（Cross-Chapter Anchor Quotes，出自 Ch4，非本章）



以下 2 条不属于本章，但它们是 Q9、Q15 与模块 4.3 的直接揭晓句，故附于此以便联读；引用时请标注 Ch4 而非本章。

A1（跨章锚点，供与 Q9 / Q15 联读）
> "Engraver must have at least 1 degree of freedom. Can only specify 2 from the key engraving parameters of volume, depth, and diameter"
Ch4 SLIDE 36
- 中文翻译：雕刻商必须至少拥有 1 个自由度。在容积、深度、直径这三个关键雕刻参数中，只能指定其中 2 个。
- 为什么记：这是 SLIDE 18（volume 是单位面积积分量）的数学必然结论，也是 SLIDE 21（KC 列了 6 个参数）的约束条件。它把 Ch2 埋下的伏笔正式揭晓，并直接决定新项目规格书该怎么锁参数（见模块 5 连接点 4 的 Step 4）。

A2（跨章锚点，供与 Q15 联读）
> "X and Y direction sheet surface coverage - Key to GMT (Cell diameter) / Z direction sheet penetration - Key to VIVA/WypAll Z peel strength (Cell depth) / High Z direction penetration can also negatively impact bulk/caliper"
Ch4 SLIDE 35
- 中文翻译：X 与 Y 方向的片材表面覆盖 —— 是 GMT 的关键（网穴直径）；Z 方向的片材渗透 —— 是 VIVA/WypAll Z 向剥离强度的关键（网穴深度）；过高的 Z 向渗透也会对松厚度/厚度产生负面影响。
- 为什么记：这是把 SLIDE 21 的 Cell diameter / Cell depth 两个参数翻译成产品属性的唯一原文。它使「三选二」从一个几何约束升级为一个产品战略选择；第三句警告（过渗透损害松厚度）对卫材尤为关键——功能涂布若追求渗透，可能牺牲纸尿裤/湿巾的蓬松手感。


## 附录：本报告的关键 [未找到原句] 汇总与风险提示（共 5 项）



说明：全文共出现 35 处 [未找到原句] 标记；下表汇总其中对结论影响最大的 5 项。

||||
|---|---|---|
|1|"engraving window" 术语在本章及全书 4 章中均未出现|该概念仅能由 SLIDE 20 + Ch4 SLIDE 36 归纳（见 C12），属本报告构造的术语|若需正式使用，应明确标注为引申定义，勿当作 KC 原文术语引用|
|2|Chrome 6 的具体法规名称、限值、生效日期、地区|无法量化合规边界|必须向供应商/法务索取具体法规映射，不可据本章做任何合规结论|
|3|陶瓷辊各工序的量化指标（动平衡等级、喷砂粗糙度、涂层厚度、抛光去除量、刮刀磨损率）|TCO 框架无法数值化|采购技术协议中逐项向供应商索取并写入验收标准|
|4|Cell Wall 宽度、六种 anilox 图案的几何定义|无法做图案选型的定量比较|向 Harper/Pamarco 索取图案技术手册|
|5|Ch3 SLIDE 28 "27,600,000 cubic microns (27.6 BCM)" 存在 1,000 倍口径矛盾（见 T4-f）|跨章数据不可互用|发函向图纸签发方书面澄清口径|

报告结束。全部数据均标注来源；所有推导均标 本报告推导 并附算式；章节无据处标 [未找到原句]，未作任何数据编造。
手册 |
| 5 | Ch3 SLIDE 28 "27,600,000 cubic microns (27.6 BCM)" 存在 1,000 倍口径矛盾（见 T4-f） | 跨章数据不可互用 | 发函向图纸签发方书面澄清口径 |

报告结束。全部数据均标注来源；所有推导均标 本报告推导 并附算式；章节无据处标 [未找到原句]，未作任何数据编造。


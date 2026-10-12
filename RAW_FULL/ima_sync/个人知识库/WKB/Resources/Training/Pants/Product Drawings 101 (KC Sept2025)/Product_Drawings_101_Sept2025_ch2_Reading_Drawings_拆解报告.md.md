---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_220f544f0d52c04707364ece299b4f09001a693ee6c0644e"
source_file: "Product_Drawings_101_Sept2025_ch2_Reading_Drawings_拆解报告.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch2_Reading_Drawings_拆解报告.md.md"
extracted: "2026-09-30"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
---

# Product_Drawings_101_Sept2025_ch2_Reading_Drawings_拆解报告.md


章节：Ch2 Reading Drawings ｜ 覆盖幻灯片：20–34 ｜ 文档：Product Drawings 101 (KC, Sept 2025) ｜ 拆解日期：2026-08-30

# Ch2 Reading Drawings — 深度学术级拆解报告

## 0. 方法与引用规范（Citation Protocol）

|||
|---|---|
|SLIDE N|该观点/数据直接来自第 N 页幻灯片文本层（含标题、项目符号、演讲者备注）|
|SLIDE N（图像）|该数据来自第 N 页渲染图读图结果，已记录在本章文件「图像内容补充」段，视为同等可靠来源|
|[未找到原句]|在本章（及全材料 Ch1–Ch5）中检索无此原句，该概念为外部工程常识或本报告补充，非 KC 材料主张|
|[本报告推导]|由本章数据经算式推导得出的结论，附完整算式|
|[外部参数]|本章材料中不存在的参数（如涂布克重、丝旦数、年产量），为行业典型值，用于量级估算|
|[数据不足] / [数据歧义]|源数据缺失或存在多种解读，不做强行计算|


本章数据可靠性分层声明：本章文本层极薄（SLIDE 20–34 的 15 页中，有 13 页仅为「Anatomy of a product drawing」+ 逐条累加的目录式标题），几乎全部商业情报密度集中于「图像内容补充」段的 BOM_A（11 行）与 p34 BOM（10 行）。因此本报告模块 3 的 T1/T2 完全依赖图像读图结果，已在每行标注 SLIDE N（图像）。

重大前提警告（必读）：T1 的 C153-FPS-01575-J-09 明确标识为 S1（Size 1，新生儿码）；T2 的 C153-FPS-01592 在本章材料中未见尺码标识。因此 T3/T4 的全部尺寸差异，可能同时包含「尺码差异」与「平台设计差异」两种解释。本报告在 T3 中给出双解释并列，并在模块 5 中据此约束结论强度。禁止将 T3 差异直接等同于竞品间的技术代差。 【本报告推导 · 方法论约束】

### 模块1：核心论点（Core Arguments）

#### ARGUMENT 1 — A KC product drawing is a six-zone information architecture, not a single picture.

KC 的产品图纸并非一张「图」，而是六个信息区块的标准组合，培训材料通过逐页累加的方式（SLIDE 21→32，每 2 页增加一个区块）强制建立这一心智模型。
- Verifiable evidence：SLIDE 21 仅列 Overhead View；SLIDE 23 累加 Cross Section；SLIDE 25 累加 Detail View(s)；SLIDE 27 累加 Bill of Materials；SLIDE 29 累加 Note(s) / Ref.(s)；SLIDE 31 累加 Title Block（且 Title Block 位于列表首位，暗示其为读图起点）。SLIDE 21–32
- 支撑依据：六个区块的累加顺序是严格单调、无回退、无跳序的（SLIDE 21/23/25/27/29/31 各新增一项，SLIDE 22/24/26/28/30/32 为对应区块的详述页），可逐页核验。

#### ARGUMENT 2 — The Overhead View is the operator's primary inspection interface; it is defined by function, not by geometry.

俯视图的定义不是「从上往下看」，而是「操作工最频繁检验的尺寸所在的那张视图」——即以质量检验行为定义视图。
- Verifiable evidence："Shows the product laid out flat with a top-down view of the body-facing side of the product." 与 "This view holds dimensions the operators will be checking most frequently." SLIDE 22
- 推论价值：这意味着 Overhead View 上的尺寸 = 在线/实验室 Dimensional Inspection 的抽检项目清单。【本报告推导】

#### ARGUMENT 3 — The Cross Section is where the adhesive architecture lives; it is the only view that exposes layer stack + glue layout.

- Verifiable evidence：p24–25 渲染图图纸标题原文为 "CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT" SLIDE 24（图像）；同一图纸可见 "UNISEX ABSORBENT"、"PAD, TRAINING"、"PRODUCTION: NEW LINE"、"SIZE 2 (17-31)"、图号 C192-FFS-1544 / C192-PT1-1344、"DRAWING UPDATED: 09-14-12"。
- 关键情报含义：「剖面图 = 胶路图」是 KC 的图纸惯例。对竞品分析而言，拿到剖面图即等于拿到该产品的胶路布局与层数结构。【本报告推导】
#### ARGUMENT 4 — The BOM is the authoritative, machine-readable item list that binds a find number to a child drawing number.

- Verifiable evidence：BOM_A 为 C153-FPS-01575-J-09 – DIAPER, BCM, SPDV, TOTAL, S1 的 CHILDREN 清单，共 11 行，每行含 S.G / Item / Qty / Ordering Description / Drawing Number SLIDE 33（图像）；p34 的 C153-FPS-01592-1-10 亦以 BOM 行项目形式给出全部尺寸 SLIDE 34（图像）。
- 结构性证据：11 个子件中 7 个为 FP1 级（C153-FP1-00031/00034/00035/00037/00052/00054/00178）、4 个为 FPM 级（C153-FPM-00154/00155/00156/00157）。FP1 对应结构件（ear / pad / outer cover / waistband / inner cover / flap / surge），FPM 对应胶与橡筋（pad-to-liner adhesive / ear adhesive / leg elastic adhesive / leg elastic strands）。这与 Ch1 SLIDE 17–18 的「FP1 = Assembly, Ex. Nonwoven + Adhesive」定义形成实践层面的精确映射。【本报告推导】
#### ARGUMENT 5 — In SolidWorks drawings, the drawing face is deliberately incomplete; BOM / Where Used is the navigation layer.

- Verifiable evidence："SolidWorks drawings rely on BOM / Where Used feature to find detailed dimensions" SLIDE 33；"SolidWorks drawings rely more on BOM / Where Used to highlight details." SLIDE 34
- 含义：KC 图纸刻意不在图面上堆砌全部尺寸（呼应 Ch1 SLIDE 16 的「Solidworks is LEGOs」），detail dimensions 需沿 BOM 下钻至 FPM 子图。这是「读图」与「看图」的分界线。【本报告推导】
#### ARGUMENT 6 — Drawings are governed objects with authorship and issue history, not static files.

- Verifiable evidence：DRCS File Information 字段样例：Drawing: C153-FPS-01575-J-09；Title: DIAPER；User Defined Title: BCM, SPDV, TOTAL, S1；Created by: Q06027 on Wed May 27 00:49:14 CDT 2020；Last Issued by: Q06411 on Thu Apr 6 08:45:31 CDT 2023 SLIDE 33（图像）；界面按钮 < Back / All Parents / All Children / Print / Help。
- 推论：Created by + Last Issued by 两个时间戳可用于判断该平台的图纸维护活跃度与技术迭代节奏（本例：2020-05 创建 → 2023-04 最后发行，跨度约 2.9 年）。【本报告推导】
### 模块2：关键概念操作化定义（Operational Definitions）



说明：(c) 操作化定义中，凡源材料存在判定依据者，直接引用；源材料无依据者，标注 [未找到原句] 并给出行业通用判定式，明确区分于 KC 材料主张。

#### 概念 1：Drawing 图框字段 / Title Block（图纸标题栏）

- (a) 中文名 + English term：图纸图框字段 / Drawing Title Block & Frame Fields
- (b) 英文定义：The lower-right-hand block on a drawing that identifies the drawing number, title, authorship, issue date, and approval status; formally added to the anatomy list at SLIDE 31.
- (c) 操作化定义：




- 位置判定式：Title Block 位于图纸右下角（SLIDE 31（图像），图像补充原文「Title Block 位于图纸右下角」）。
- 必备字段集（KC 实例可验证）：Drawing Number / Title / User Defined Title / Created by (人名+时间戳) / Last Issued by (人名+时间戳) SLIDE 33（图像）。
- 完整性判定：一张图纸可被判定为「可发行」的最小字段集 = 图号 ∧ 标题 ∧ 创建者 ∧ 发行者；缺任一即为未受控图纸。【本报告推导】
- 字段逐项说明见 T6。
- (d) 原文英文摘录：




- "Title Block" SLIDE 31（anatomy 列表中首次出现）
- "Drawing: C153-FPS-01575-J-09；Title: DIAPER；User Defined Title: BCM, SPDV, TOTAL, S1" SLIDE 33（图像）
- "右下角 \"Kimberly-Clark Corporation\"" SLIDE 24（图像）
- Part Name / Description / Drawn By / Date / Material / QUANTITY REQUIRED / APPROVALS / Tolerances / Projections 等字段：[未找到原句]（全材料 Ch1–Ch5 检索无此字段名）
#### 概念 2：Overhead View（俯视图 / 平铺图）★ 源材料核心术语

- (a)：俯视图（产品平铺俯视图）/ Overhead View
- (b) 英文定义："Shows the product laid out flat with a top-down view of the body-facing side of the product." — a flattened, body-facing-side-up orthographic view of the finished product. SLIDE 22
- (c) 操作化定义：




- 判定三要素：① 产品平铺展开（laid out flat，非立体穿着态）；② 视角为自上而下（top-down）；③ 可见面为贴身面（body-facing side，即面层/导流层侧，非底膜侧）。三要素同时成立 = Overhead View。
- 量化指标：该视图承载的尺寸集合 ∩ 产线检验频次最高的尺寸集合 ≈ 全集（"This view holds dimensions the operators will be checking most frequently." SLIDE 22）。
- 反向操作化：若某尺寸不在 Overhead View 上，则该尺寸大概率不在常规抽检清单内，需查 Detail View 或 FPM 子图。【本报告推导】
- (d) 原文英文摘录："Shows the product laid out flat with a top-down view of the body-facing side of the product." / "This view holds dimensions the operators will be checking most frequently." SLIDE 22
#### 概念 3：Front view / Top view / Side view（三视图）

- (a)：正视图 / 俯视图 / 侧视图 / Front view / Top view / Side view
- (b) 英文定义：Classic three-view orthographic projection (first-angle or third-angle) in which an object is described by its front, top and side elevations.
- (c) 操作化定义：




- 判定式：三视图 = 同一物体在三个互相垂直的投影面上的正投影，且三视图之间满足「长对正、高平齐、宽相等」的三等关系。
- 与本章的关系：本章仅使用 Overhead View 与 Cross Section 两类视图，Front view、Side view 字样在全材料 Ch1–Ch5 中 未出现；Top view 仅在短语 "top-down view" 中作为副词性描述出现（SLIDE 22），并非独立的 named view。
- 推论：KC 卫材图纸采用「平铺俯视 + 剖面 + 局部放大」的简化表达体系，而不采用传统机械制图的三视图体系——因为卫材产品为薄型柔性叠层件，厚度方向信息由 Cross Section 承载。【本报告推导】
- (d) 原文英文摘录："top-down view" SLIDE 22；Front view / Side view / Top view（作为独立视图名）：[未找到原句]
#### 概念 4：Cross Section（剖面图 / 截面图）

- (a)：剖面图（截面示意图）/ Cross Section
- (b) 英文定义：A cut-through view of the product showing the internal layer stack; in KC practice titled as "CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT". SLIDE 24（图像）
- (c) 操作化定义：




- 判定式：视图中出现沿产品 MD 或 CD 的剖切线，且露出 ≥2 个材料层与层间胶层 = Cross Section。
- 量化指标（KC 实例）：该视图上同时标注 "UNISEX ABSORBENT"（吸收芯体）、"PAD, TRAINING"、"PRODUCTION: NEW LINE"、"SIZE 2 (17-31)"（尺码与体重区间 17–31 lb）SLIDE 24（图像）。
- 情报操作化：剖面图的首要用途是表达胶路（adhesive layout），层数 = 材料层数，胶层数量 = 施胶工位数。【本报告推导】
- (d) 原文英文摘录："CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT" SLIDE 24（图像）；anatomy 列表中 "Cross Section" 首次出现于 SLIDE 23
#### 概念 5：Detailed view / Detail View(s)（局部放大图 / 细部图）

- (a)：局部放大图（细部视图）/ Detail View(s)
- (b) 英文定义：An enlarged sub-view of a localized region of the drawing, used to carry dimensions that are too dense or too small to be legible on the parent view.
- (c) 操作化定义：




- 判定式：视图带放大比例标记（如 2:1 / 5:1）或带圆形/矩形局部框（detail circle）并引出至独立视区 = Detail View。
- 量化指标（KC 实例）：p34 的 EAR PROFILE 细部尺寸 68 / 30 / 56 / 75 / 115 mm，20 mm OVERLAP SLIDE 34（图像） —— 即耳贴轮廓的 5 段局部尺寸以 Detail View 承载，证明了该视图的尺寸承载功能。
- 操作化判据：父视图无法在 ≥1:1 下清晰标注的尺寸，必须下沉至 Detail View。【本报告推导】
- (d) 原文英文摘录："Detail View(s)" SLIDE 25（anatomy 列表首次出现）；"EAR PROFILE 细部尺寸 68 / 30 / 56 / 75 / 115mm，20mm OVERLAP" SLIDE 34（图像）



- 关于 Detailed view 的通用定义（放大比例、detail circle 等）：[未找到原句]，为制图学通用惯例
#### 概念 6：Exploded view（爆炸图）

- (a)：爆炸视图 / Exploded view
- (b) 英文定义："The Explode section will let you separate individual parts to better show how the product is constructed" — a view in which components are displaced along an axis to reveal assembly order. SLIDE 59（属 Ch4 3D Viewer，非本章）
- (c) 操作化定义：




- 判定式：装配体各零件沿装配轴产生非零位移且零件间无干涉 = Exploded view；位移量由滑块连续控制。
- 量化指标：爆炸强度可用「相邻零件最小间隙 / 零件特征尺寸」比值度量，通常取值 0.2–1.0 以保证层序可读。【本报告推导，[未找到原句]】
- 在本材料中的定位：Exploded view 不是 2D 图纸上的视图，而是 eDrawings 3D 查看器中的交互模式（Ch4 SLIDE 59–60），辅以 Move（Free Drag / Position / Translate / Rotate）进行零件重定位。这是 KC 用 3D 交互替代 2D 爆炸图的设计选择。【本报告推导】
- (d) 原文英文摘录："The Explode section will let you separate individual parts to better show how the product is constructed" SLIDE 59（Ch4）；"Use the slider to separate individual components." SLIDE 59（Ch4）



- 本章（Ch2, SLIDE 20–34）内：[未找到原句]
#### 概念 7：3D view（三维视图）

- (a)：三维视图 / 3D view
- (b) 英文定义："To view the 3D version of drawings you will need to download the SolidWorks file and open in eDrawings" — the three-dimensional representation carried by .sldasm (assembly) and .sldprt (part) files, not by the 2D drawing file itself. SLIDE 50（Ch4）
- (c) 操作化定义：




- 文件类型判定式：.sldasm = 3D 装配图；.sldprt = 3D 零件图（SLIDE 50，Ch4）。文件类型即视图类型的判定代理变量。
- 交互功能集：Components（逐级下钻 / 左键双高亮 / 右键 Hide、Make Transparent、Hide Others=Isolate）SLIDE 52–54；Markup（Text / Shapes / Dimensions / Images / Comments）SLIDE 55–56；Measure（量测但不落图）SLIDE 57；Move SLIDE 58；Explode SLIDE 59–60；View Orientation / Normal To SLIDE 62；右键 → View → Reset 复位 SLIDE 61（均属 Ch4）。
- 关键区分：Dimensions（标注，记录在图上）vs Measure（量测，不记录在图上）—— 二者是评审留痕与临时量测的分界。SLIDE 56–57（Ch4）
- (d) 原文英文摘录：".sldasm = 3D Assembly drawing" / ".sldprt = 3D Part drawing" SLIDE 50（Ch4）；"The measuring tool works the same as the dimension tool, only the dimensions won't be recorded on the drawing" SLIDE 57（Ch4）



- 本章（Ch2）内：[未找到原句]
#### 概念 8：BOM（Bill of Materials，物料清单）

- (a)：物料清单 / Bill of Materials (BOM)
- (b) 英文定义：The structured list of all child drawings (CHILDREN) that make up a parent drawing, each row identified by find number, quantity, ordering description and child drawing number. SLIDE 27–28, SLIDE 33–34
- (c) 操作化定义：




- 结构判定式：一个合法 BOM 行 = Find No. ∧ Qty ∧ Ordering Description ∧ Drawing Number；本例 11 行的 Qty 全部 = 1（SLIDE 33（图像）），即每件成品消耗每个子件各 1 件（无备件/无双倍用量）。
- 量化指标（本例）：BOM 行数 = 11（C153-FPS-01575-J-09）；子件层级分布 = 7 × FP1 + 4 × FPM（见 ARGUMENT 4）。
- 命名规则操作化：Ordering Description 遵循 产品族, 平台, 尺码, 部件名, 关键尺寸 的逗号分隔层级编码（例："DIAPER, BCM, SMALL SURGE 100MM W, 236MM L"），尺寸被编码进物料描述本身 —— 这意味着 BOM 描述即技术规格，改尺寸 = 改物料号 = 触发新图纸。【本报告推导，关键结论】
- 导航操作化：BOM 行 → Drawing Number → 下钻至子图；反向为 All Parents 上溯。界面按钮 < Back / All Parents / All Children / Print / Help> SLIDE 33（图像）。
- (d) 原文英文摘录："Bill of Materials" SLIDE 27；"SolidWorks drawings rely on BOM / Where Used feature to find detailed dimensions" SLIDE 33；"1|2|1|DIAPER, BCM, S1, S2, EAR|C153-FP1-00031-B-01" 等 11 行 SLIDE 33（图像）
#### 概念 9：Find number（查找号 / 件号）

- (a)：查找号（BOM 项号 ↔ 图纸标注编号）/ Find number (item balloon number)
- (b) 英文定义：The sequential identifier in the BOM that corresponds one-to-one with the numbered callout balloon placed on the drawing view, enabling the reader to map a graphic entity to a BOM row.
- (c) 操作化定义：




- 判定式：Find No.(i) ↔ 图纸引线上编号 i ↔ BOM 第 i 行 ↔ Child Drawing Number(i)，四者构成双射（bijection）。
- 本例取值：Find No. = 1 … 11（对应 BOM_A 第一列 1–11）SLIDE 33（图像）；图面可见编号实例为 1 / 2 / 3（SLIDE 34 文本层出现 1、2、3 三行，即 p34 图面上的气球标注）。
- 列序歧义记录：源材料表头声明列为 S.G / Item / Qty，但第 1 行数据为 1|2|1，第 2–11 行为 n|1|1。若按表头解读，则 Item 列在第 1 行为 2、其余为 1，不自洽；若将第一列解读为 find number（1–11 连续递增、且与 Ordering Description 一一对应），则第二列（仅首行为 2、其余为 1）应解读为 S.G.（Specification Group / 分组标记）。本报告采用后者：第一列 = Find No.。【本报告推导 · 数据解读说明】
- 情报操作化：find number 是竞品拆解的最小可比单元 —— 拆解报告必须以 find number 为粒度对齐，否则尺寸无法归属到具体部件。【本报告推导】
- (d) 原文英文摘录："S.G / Item / Qty / Ordering Description / Drawing Number" 表头 + 11 行数据 SLIDE 33（图像）；SLIDE 34 文本层 "1" / "2" / "3"



- 术语 find number 字面：[未找到原句]（材料中使用 Item 列与图面阿拉伯编号，未出现 find number 词组）
#### 概念 10：Dimensional Inspection（尺寸检验）

- (a)：尺寸检验 / Dimensional Inspection
- (b) 英文定义：The set of measurements taken on the production line or in the lab to verify conformance to the dimensions specified on the drawing, concentrated on the Overhead View.
- (c) 操作化定义：




- 抽样框判定式：检验项目集 ≈ Overhead View 上标注的尺寸集（依据 "This view holds dimensions the operators will be checking most frequently." SLIDE 22）。
- 频次指标：most frequently（最高频）——材料给出定性频次，未给具体抽检频次（如每 X 分钟 N 片）。[未找到原句：无量化抽检频次]
- 判据来源：尺寸的合格判据来自图纸标注值 + 公差块（Tolerances）。本章未提供公差数值，故任何合格/不合格判定均不可从本章导出。[未找到原句：无公差数值]
- 反向操作化：凡进入 BOM Ordering Description 的尺寸（如 44MM WIDTH、100MM W, 236MM L），即为必检且可追溯到物料号的关键尺寸（CTQ 候选）。【本报告推导】
- (d) 原文英文摘录："This view holds dimensions the operators will be checking most frequently." SLIDE 22



- Dimensional Inspection 词组：[未找到原句]
#### 概念 11：Material spec（材料规格）

- (a)：材料规格 / Material specification
- (b) 英文定义：The material-level requirement attached to a component, encoded in KC practice within the BOM ordering description (substrate identity, basis weight class, treatment) and referenced to the child drawing.
- (c) 操作化定义：




- 编码位置判定式：材料规格信息不在独立的 MATERIAL 字段中，而内联于 Ordering Description（例："OUTER COVER NO IFIT" 中的 NO IFIT 为材料/结构特征限定；"SMALL SURGE" 中的 SMALL 为规格档位；"PICASSO EMBOSSING" 为加工/花纹规格；"PAD, DISCRETE" vs "PAD NONDISCRETE" 为芯体成型方式规格）。SLIDE 33（图像）、SLIDE 34（图像）
- 可枚举的材料规格维度（本例）：① 结构特征（NO IFIT、FIT LOOP 43MM W）；② 成型方式（DISCRETE / NONDISCRETE）；③ 花纹/加工（PICASSO EMBOSSING）；④ 尺寸档位（SMALL、S1）；⑤ 功能分区（INNER COVER EYESPOT ... BACK END、UMZ）。【本报告推导】
- 追溯操作化：材料规格 → Ordering Description → Drawing Number → FPM/FP1 子图（最小单元）→ 完整材料定义。
- MATERIAL 作为独立图框字段：[未找到原句]
- (d) 原文英文摘录："DIAPER, BCM, S1, OUTER COVER NO IFIT|C153-FP1-00035-J-03" SLIDE 33（图像）；"SURGE PICASSO EMBOSSING 74MM W × 197MM L" SLIDE 34（图像）；"PAD NONDISCRETE" SLIDE 34（图像）
#### 概念 12：Score 线（压痕线 / 撕开线）

- (a)：压痕线（撕开线、易撕线）/ Score line (tear line / perforation)
- (b) 英文定义：A mechanically or ultrasonically imposed line of weakness in a substrate (or a perforation pattern) that controls where and how easily a web or product can be folded or torn open.
- (c) 操作化定义：





- 判定式：基材上一条残余厚度 < 基材厚度的连续弱化线（压痕）或切口/连接比可控的不连续切口序列（打孔线）。
- 量化指标：① 压痕深度比 = 压痕处残余厚度 / 原始厚度（典型 30%–70%）；② 打孔线的 切口长度 / 连接桥长度（cut : tie）比（典型 2:1 – 6:1）；③ 撕开力（tear force，N/15mm 或 gf）；④ 撕开路线的偏移公差（mm）。
- 卫材场景：常见于耳贴易撕区、包装袋易撕口、训练裤侧边易撕缝。（以上全部为行业通用定义，[未找到原句]）
- 本章状态声明：score / SCORE 在 Ch1–Ch5 全材料检索中零命中（已对全文执行 score|Score|SCORE 正则检索，仅 Bill of Materials 等无关项命中）。本章的 BOM_A 与 p34 BOM 中均未列 score line 项。因此不能主张 KC 本平台产品含/不含 score 线。
- 反向操作化建议：若要在竞品拆解中核验 score 线，应在 Detail View 中查找（因压痕尺寸属局部尺寸，通常下沉至细部图），核验项 = 压痕深度比 / cut:tie 比 / 撕开力。【本报告推导】
- (d) 原文英文摘录：[未找到原句]（全材料无此术语；本概念的 (b)(c) 为外部工程惯例，非 KC 材料主张）
### 模块3：证据链（Evidence Chain）



全部表格均标注 SLIDE N。T1/T2 为【情报级】逐条 BOM 全量转录；T3/T4 为对比与反推；T5/T6 为方法与字段说明。

#### T1【情报级】C153-FPS-01575-J-09（DIAPER, BCM, SPDV, TOTAL, S1）完整 BOM 逐项表

源：BOM_A，SLIDE 33（图像）（DRCS Where Used 页，p13 渲染图）。列结构源文：S.G / Item / Qty / Ordering Description / Drawing Number。
Qty 列：11 行全部 = 1（即单片成品消耗每个子件各 1 件）。

|||||||||
|---|---|---|---|---|---|---|---|
|1|2|1|DIAPER, BCM, S1, S2, EAR|未标注尺寸|C153-FP1-00031-B-01|FP1|耳贴（ear）。描述中同时出现 S1 与 S2，疑为跨尺码共用件；第2列值=2，为 11 行中唯一异常（见概念 9 歧义说明）|
|2|1|1|DIAPER, BCM, S1, PAD, DISCRETE|未标注尺寸|C153-FP1-00034-D-02|FP1|吸收芯体（pad），DISCRETE = 离散式/分切式芯体（区别于 SS 平台的 PAD NONDISCRETE）|
|3|1|1|DIAPER, BCM, S1, OUTER COVER NO IFIT|未标注尺寸|C153-FP1-00035-J-03|FP1|底膜/外覆层，NO IFIT = 无 iFit 结构特征（材料规格内联于描述，见概念 11）|
|4|1|1|DIAPER, BCM, S1, WAISTBAND 44MM WIDTH|44 mm（宽/WIDTH）|C153-FP1-00037-D-02|FP1|腰带（waistband）。对比 SS 平台 58 mm，窄 14 mm|
|5|1|1|DIAPER, BCM, S1, INNER COVER EYESPOT 198MM BACK END 90MM|198 mm（总）；尾端 90 mm（BACK END）|C153-FP1-00052-J-02|FP1|内覆层 + EYESPOT（印刷对位点/眼标）；198MM 为片长方向尺寸，BACK END 90MM 为尾端分区尺寸|
|6|1|1|DIAPER, BCM, S1, FLAP 45MM HEIGHT|45 mm（高/HEIGHT）|C153-FP1-00054-D-04|FP1|护围/挡片（flap）。对比 SS 平台 37 mm，高 8 mm|
|7|1|1|DIAPER, BCM, SMALL SURGE 100MM W, 236MM L|100 mm（宽 W）× 236 mm（长 L）|C153-FP1-00178-D-04|FP1|导流层（surge），规格档位 SMALL。★ 与 Ch3 ER# 900200005649 红线的 C153-FP1-00178 为同一图纸（见模块 4）|
|8|1|1|DIAPER, PAD TO LINER, ADHESIVE, 125MM CD X 367MM MD|125 mm（CD）× 367 mm（MD）|C153-FPM-00154-B-01|FPM|芯体-底膜胶。CD=横向(cross direction)，MD=纵向(machine direction)。面积 = 45,875 mm²（见 T4）|
|9|1|1|DIAPER, EAR ADHESIVE, 202 OUTSIDE W, X 182 INSIDE W|202 mm（外宽 OUTSIDE W）× 182 mm（内宽 INSIDE W）|C153-FPM-00155-B-01|FPM|耳贴胶。仅给宽度两个值，未给长度 → 面积 [数据不足] 不可计算|
|10|1|1|DIAPER, LEG ELASTIC ADHESIVE, 199MM CD X 227MM MD, S1|199 mm（CD）× 227 mm（MD）|C153-FPM-00156-B-02|FPM|腿部橡筋包覆胶。面积 = 45,173 mm²（见 T4）。描述尾部显式带尺码 S1|
|11|1|1|DIAPER, LEG ELASTIC STRANDS, 152MM FRONT, 173.1MM REAR|前 152 mm / 后 173.1 mm|C153-FPM-00157-D-01|FPM|腿部橡筋丝。前/后两段长度差 21.1 mm（后段长 13.9%）。.1 级精度，说明该尺寸为设计计算值而非取整值|


BOM_A 结构统计【本报告推导】：11 项 = 7 × FP1（结构件）+ 4 × FPM（胶 3 项 + 橡筋 1 项）；其中含胶工件 3 项（pad-to-liner / ear / leg elastic adhesive），弹性件 1 项（leg elastic strands），非织造/膜类结构件 7 项。

配套治理元数据（SLIDE 33（图像），DRCS File Information）：

|||
|---|---|
|Drawing|C153-FPS-01575-J-09|
|Title|DIAPER|
|User Defined Title|BCM, SPDV, TOTAL, S1|
|Created by|Q06027 on Wed May 27 00:49:14 CDT 2020|
|Last Issued by|Q06411 on Thu Apr 6 08:45:31 CDT 2023|
|界面按钮|< Back / All Parents / All Children / Print / Help|
|维护跨度|2020-05-27 → 2023-04-06，约 2.86 年【本报告推导】|


图号结构解读【本报告推导】：C153 = 平台/项目前缀；FPS = Finished Product Specification（Ch1 SLIDE 17–19：工厂用全产品图）；01575 = 序列号；J = 版本字母；09 = 版本号。子件后缀规律：-B-01、-D-02、-J-03、-D-04 等，末段为修订序号（最大见 -D-04）。

#### T2【情报级】C153-FPS-01592-1-10（任务书标注为 SS 平台）完整 BOM 逐项表

源：SLIDE 34（图像）（p34 渲染图）。注：该页源材料以行项目散述形式给出，未提取到 find number 列 → Find No. 列标注 [未提取]。

|||||
|---|---|---|---|
|[未提取]|FLAP 37MM HEIGHT|37 mm（高）|护围。比 S1 的 45 mm 低 8 mm（−17.8%）|
|[未提取]|PAD NONDISCRETE|未标注尺寸|芯体：NONDISCRETE（连续式），与 S1 的 PAD DISCRETE 工艺路线不同|
|[未提取]|WAISTBAND 58MM HEIGHT|58 mm（高/HEIGHT）|腰带。比 S1 的 44 mm 高 14 mm（+31.8%）；注意 S1 用 WIDTH、此页用 HEIGHT，量纲口径可能为同一方向|
|[未提取]|INNER COVER EYESPOT 202MM BACK END 85MM|202 mm 总长；尾端 85 mm|比 S1（198 / 90 mm）总长 +4 mm，尾端 −5 mm|
|[未提取]|SURGE PICASSO EMBOSSING 74MM W × 197MM L|74 mm（宽）× 197 mm（长）|★ 导流层带 PICASSO EMBOSSING（毕加索压花） —— 明确的花纹/加工工艺规格。面积 14,578 mm²|
|[未提取]|OUTER COVER 295MM W [FIT LOOP 43MM W]|295 mm（宽）；FIT LOOP 43 mm（宽）|外覆层总宽 295 mm；含 FIT LOOP 结构（对比 S1 的 OUTER COVER NO IFIT，有无 iFit 是两平台的关键结构分野）|
|[未提取]|LEG ELASTIC STRANDS 165MM FRONT / 199MM REAR|前 165 mm / 后 199 mm|前/后差 34 mm（后段长 20.6%）。比 S1（152/173.1）前后各更长|
|[未提取]|PAD TO LINER ADHESIVE 125MM CD × 476MM MD|125 mm（CD）× 476 mm（MD）|芯体-底膜胶。面积 59,500 mm²。CD 与 S1 相同（125 mm），MD 长 +109 mm（+29.7%）|
|[未提取]|EAR REINFORCEMENT ADH 268 × 200 × 500MM MD|268 × 200 × 500 mm（MD）|[数据歧义]：三元组尺寸。可能为 268 mm CD × 200 mm（间隙/分段）× 500 mm MD 的分段涂布，或含加强片长度。不做面积计算|
|[未提取]|LEG ELASTIC ADHESIVE 232MM CD × 279MM MD|232 mm（CD）× 279 mm（MD）|腿部橡筋包覆胶。面积 64,728 mm²。比 S1（199×227）两向均更大|


Detail View 承载的局部尺寸（同页，属 Detail View(s) 概念实例，SLIDE 34（图像））：

||||
|---|---|---|
|EAR PROFILE（耳贴轮廓）|68 / 30 / 56 / 75 / 115 mm|5 段轮廓尺寸，共 5 个数值|
|EAR 搭接|20 mm OVERLAP|耳贴搭接量 20 mm|


图号：C153-FPS-01592-1-10。【本报告推导】与 S1 的 C153-FPS-01575-J-09 相比：序列号段 01592 vs 01575；版本段 -1-10 vs -J-09（格式不同：前者为 -数字-数字，后者为 -字母-数字），可能代表不同的发行/版本编码体系或不同时期的编码规范。

#### T3 两平台关键尺寸差异对比表

源：T1（SLIDE 33（图像））与 T2（SLIDE 34（图像））。差异列中 Δ = SS − S1；百分比 = Δ / S1。

|||||||
|---|---|---|---|---|---|
|SURGE 宽 W|100 mm|74 mm|−26 mm|−26.0%|SS 导流层显著收窄|
|SURGE 长 L|236 mm|197 mm|−39 mm|−16.5%|SS 导流层显著缩短|
|SURGE 面积|23,600 mm²【推导：100×236】|14,578 mm²【推导：74×197】|−9,022 mm²|−38.2%|★ 核心差异：SS 导流层面积仅为 S1 的 61.8%|
|SURGE 工艺|无压花标注（SMALL SURGE）|PICASSO EMBOSSING|—|—|★ SS 采用压花导流，S1 为素面|
|FLAP 高|45 mm|37 mm|−8 mm|−17.8%|SS 护围更低|
|WAISTBAND 宽/高|44 mm|58 mm|+14 mm|+31.8%|SS 腰带显著加宽|
|PAD ADH 宽 CD|125 mm|125 mm|0|0%|芯体宽度完全相同|
|PAD ADH 长 MD|367 mm|476 mm|+109 mm|+29.7%|SS 芯体显著加长|
|PAD ADH 面积|45,875 mm²【推导】|59,500 mm²【推导】|+13,625 mm²|+29.7%|胶面积同比放大|
|LEG ELASTIC 前段|152 mm|165 mm|+13 mm|+8.6%|SS 前腿围更长|
|LEG ELASTIC 后段|173.1 mm|199 mm|+25.9 mm|+15.0%|SS 后腿围更长|
|LEG ELASTIC 前后差|21.1 mm（后长 13.9%）|34.0 mm（后长 20.6%）|+12.9 mm|—|SS 前后非对称性更强|
|LEG ELASTIC ADH CD|199 mm|232 mm|+33 mm|+16.6%|SS 包覆胶更宽|
|LEG ELASTIC ADH MD|227 mm|279 mm|+52 mm|+22.9%|SS 包覆胶更长|
|LEG ELASTIC ADH 面积|45,173 mm²【推导】|64,728 mm²【推导】|+19,555 mm²|+43.3%|SS 腿部用胶面积大幅增加|
|INNER COVER 总长|198 mm|202 mm|+4 mm|+2.0%|基本持平|
|INNER COVER 尾端|90 mm|85 mm|−5 mm|−5.6%|SS 尾端分区略短|
|OUTER COVER|无 FIT LOOP（NO IFIT）|295 mm W，含 FIT LOOP 43MM W|—|—|★ 结构分野：SS 有 iFit 贴合环，S1 无|
|PAD 成型|DISCRETE|NONDISCRETE|—|—|★ 工艺分野：离散芯 vs 连续芯|
|EAR 胶|202 OUTSIDE W × 182 INSIDE W|EAR REINFORCEMENT ADH 268×200×500MM MD|—|—|表述体系不同，不可直接对比|
|EAR 轮廓|未提取|68/30/56/75/115 mm，20 mm OVERLAP|—|—|SS 耳贴为 5 段复杂轮廓|


★ 双解释并列（必读，见第 0 节警告）【本报告推导】：

|||
|---|---|
|S1 已确证为 Size 1（新生儿码）；SS 尺码未标注。若 SS 为更大尺码（如 S3/S4），则 pad 长 367→476 mm、leg elastic 全线加长、腰带 44→58 mm 均可由「尺码放大」单一因素解释|若两平台同尺码，则 NO IFIT → FIT LOOP、DISCRETE → NONDISCRETE、素面 surge → PICASSO EMBOSSING 属不可由尺码解释的定性结构分野，构成真正的代差|
|可由尺码解释的项：pad 长、leg elastic 长度、waistband、inner cover|不可由尺码解释的项：① iFit 有无；② PAD 离散/连续；③ PICASSO 压花有无；④ flap 反向变短（45→37 mm，尺码变大反而护围变矮，与尺码逻辑相悖）|
|证据强度：强（S1 已标尺码）|证据强度：中（flap 反向变化 + 三项定性分野，但缺乏 SS 尺码标注的直接反证）|


综合判定【本报告推导】：flap 45 → 37 mm 的反向变化是唯一与「尺码放大」假说相矛盾的数据点，加上 3 项定性结构分野，倾向解释 B（平台代差）占优，但不能排除尺码部分贡献。建议以「SS 平台 = 更大尺码 + 新一代结构」作为工作假设，待补齐 SS 尺码标注后定论。

产品定位差异推导【本报告推导】：
- S1 平台：小面积素面 surge（100×236，占 pad 面积 51.4%）+ 高护围（45 mm）+ 窄腰带（44 mm）+ 离散芯 + 无 iFit → 定位为经典/经济型纸尿裤，成本导向，导流依赖材料本体而非结构。
- SS 平台：压花 surge（74×197，占 pad 面积 24.5%）+ 低护围（37 mm）+ 宽腰带（58 mm）+ 连续芯 + 带 43 mm iFit 贴合环 + 大幅腿部包覆胶 → 定位为升级/贴合型纸尿裤：导流从「面覆盖」转向「结构导流（压花沟槽）」，防漏从「高护围」转向「iFit 贴合环 + 加宽腿部弹性包覆」，腰部舒适度通过加宽腰带补偿。

#### T4【本报告推导】从 BOM 反推产品结构表



全部为推导，算式明示。输入数据来自 T1（SLIDE 33（图像））/ T2（SLIDE 34（图像））。

(A) 由 pad adhesive 长度反推芯体长度差异

前提【本报告推导】：PAD TO LINER ADHESIVE 的 CD × MD 涂布矩形覆盖并近似等于芯体（pad）的平面轮廓，即 pad 宽 ≈ adhesive CD，pad 长 ≈ adhesive MD。

|||||
|---|---|---|---|
|芯体宽度|= pad adh CD|125 mm|125 mm|
|芯体长度|= pad adh MD|367 mm|476 mm|
|芯体长度差|476 − 367|+109 mm（+29.7%）||
|芯体平面面积|CD × MD|125 × 367 = 45,875 mm²|125 × 476 = 59,500 mm²|
|芯体长宽比|MD / CD|367 / 125 = 2.94|476 / 125 = 3.81|


结论 A：两平台芯体宽度严格相同（125 mm），差异全部集中在长度方向（+109 mm）。结合 pad 成型方式 DISCRETE → NONDISCRETE 的切换，反推：SS 平台在保持成型设备幅宽（CD 125 mm）不变的前提下，通过延长芯体 + 改用连续成型工艺来提升吸收容量。这是典型的「不改幅宽、只改节距」的产线兼容型升级路径 —— 对竞品分析的直接含义：SS 平台可在既有 CD 125 mm 的产线上切换生产，产线改造成本低。【本报告推导】

(B) 由 leg elastic 长度反推腿部弧线设计

|||||
|---|---|---|---|
|单侧橡筋总长（前+后）|front + rear|152 + 173.1 = 325.1 mm|165 + 199 = 364.0 mm|
|双侧总长（×2 侧）|× 2|650.2 mm|728.0 mm|
|前后非对称度|rear / front|173.1 / 152 = 1.139（+13.9%）|199 / 165 = 1.206（+20.6%）|
|前后长度差|rear − front|21.1 mm|34.0 mm|
|隐含包覆胶带宽|leg adh 面积 ÷ 双侧橡筋总长|45,173 mm² ÷ 650.2 mm = 69.5 mm|64,728 mm² ÷ 728.0 mm = 88.9 mm|


结论 B1（隐含包覆带宽）【本报告推导，假设：单侧 1 根橡筋且包覆胶沿全橡筋长度涂布】：SS 的腿部包覆胶带宽度 88.9 mm vs S1 的 69.5 mm，宽 +19.4 mm（+27.9%）。若单侧为 2 根橡筋，则带宽减半（S1 ≈ 34.7 mm，SS ≈ 44.5 mm），差值比例不变。这意味着 SS 的腿部弹性有效作用区更宽 —— 从「线密封」升级为「带密封」。

结论 B2（腿部弧线）【本报告推导】：橡筋前后段长度差反映腿围弧线的前后不对称程度。SS 的后/前比 1.206 显著高于 S1 的 1.139，反推：SS 产品的腿部开口弧线在后段（臀部侧）更外扩/更长，即腿洞重心后移。产品语义为 针对仰卧/后躺姿势的后漏防护强化（后腰部为仰卧位积液区）。同时前段 165 mm（vs S1 的 152 mm）也更长，说明 SS 腿洞整体更大，配合更宽的腰带（58 mm）形成「大开口 + 强弹性」的贴合策略，而 S1 为「小开口 + 高护围（45 mm）」的兜挡策略。

(C) 由 surge 宽度反推吸收目标

|||||
|---|---|---|---|
|Surge 面积|W × L|100 × 236 = 23,600 mm²|74 × 197 = 14,578 mm²|
|Surge 宽度 / 芯体宽度|surge W ÷ 125 mm|100 / 125 = 80.0%|74 / 125 = 59.2%|
|Surge 长度 / 芯体长度|surge L ÷ pad MD|236 / 367 = 64.3%|197 / 476 = 41.4%|
|Surge 面积 / 芯体面积|—|23,600 / 45,875 = 51.4%|14,578 / 59,500 = 24.5%|
|Surge 长宽比|L / W|236 / 100 = 2.36|197 / 74 = 2.66|


结论 C【本报告推导】：SS 的 surge 在绝对面积（−38.2%）和相对覆盖率（51.4% → 24.5%，腰斩）上双双大幅收缩，但同时引入 PICASSO EMBOSSING 压花。这一「面积减半 + 增加压花」的组合，是导流策略的范式切换：
- S1 = 大面积覆盖型导流：靠 surge 材料本体铺满芯体 51.4% 面积（宽向覆盖 80%）来实现液体铺展与快速下渗，材料用量换性能。
- SS = 局部压花导流型：surge 缩至芯体的 24.5%，窄至 59.2% 幅宽，靠压花沟槽（embossing channels）在更小的材料面积上建立定向导流通道，以结构换材料。
- 吸收目标反推：S1 的宽幅 surge（80% 幅宽覆盖）指向应对大面积、高瞬时流量的尿液冲击（新生儿频繁小量排尿，需快速铺展防回渗）；SS 的窄幅 + 压花 surge 指向应对集中、定向的较大单次尿量（通过沟槽将液体快速定向输送至芯体后段/全长，配合 476 mm 的加长芯体做纵深吸收）。SS 的「窄 surge + 长芯体」是一对自洽的设计组合：前端快速导流 → 后端纵深储存。【本报告推导】

(D) 派生：两大用胶面积合计对比（供模块 5 使用）

|||||
|---|---|---|---|
|pad adh + leg adh 面积|45,875 + 45,173 / 59,500 + 64,728|91,048 mm² = 0.091048 m²|124,228 mm² = 0.124228 m²|
|倍数|124,228 ÷ 91,048|1.3645（+36.5%）||

#### T5 图纸视图类型与用途表

|||||||
|---|---|---|---|---|---|
|Overhead View|SLIDE 21（定义于 SLIDE 22）|展示产品平铺展开、贴身面朝上的俯视形态；承载操作工最频繁检验的尺寸|产品的 MD/CD 主体轮廓尺寸|否|"Shows the product laid out flat with a top-down view of the body-facing side of the product." SLIDE 22|
|Cross Section|SLIDE 23（图标题于 SLIDE 24（图像））|展示内部层叠结构与胶路布局|层厚、层序、胶层位置与涂布范围|否|"CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT" SLIDE 24（图像）|
|Detail View(s)|SLIDE 25|放大局部、承载父视图无法清晰标注的尺寸|局部特征尺寸（如耳贴轮廓 5 段尺寸）|否|"EAR PROFILE 细部尺寸 68 / 30 / 56 / 75 / 115mm，20mm OVERLAP" SLIDE 34（图像）|
|Bill of Materials|SLIDE 27|列出全部子件及其图号、数量、订购描述（含关键尺寸）|尺寸以文本形式编码于 Ordering Description|是（本体）|BOM_A 11 行 SLIDE 33（图像）|
|Note(s) / Ref.(s)|SLIDE 29|承载说明性文字与引用参照|补充说明、非几何要求|否|SLIDE 29 anatomy 列表|
|Title Block|SLIDE 31（位于图框右下角）|承载图号、标题、作者、发行日期等治理元数据|无尺寸，全为标识与治理信息|否|"Title Block 位于图纸右下角" SLIDE 31（图像）|
|BOM / Where Used（导航层）|SLIDE 33|查找 detail dimensions 的入口（而非图面本身）|通过下钻至子图获取|是|"SolidWorks drawings rely on BOM / Where Used feature to find detailed dimensions" SLIDE 33|
|Front view|—|[未找到原句] KC 卫材图纸不采用|—|—|全材料检索无此术语|
|Top view|—|仅以副词短语 "top-down view" 出现，非独立 named view|—|—|SLIDE 22|
|Side view|—|[未找到原句] KC 卫材图纸不采用|—|—|全材料检索无此术语|
|Exploded view|Ch4 SLIDE 59|分离各零件以展示装配关系（eDrawings 交互模式，非 2D 图纸视图）|无新增尺寸|否|"The Explode section will let you separate individual parts to better show how the product is constructed" SLIDE 59（Ch4）|
|3D view|Ch4 SLIDE 50|打开 .sldasm / .sldprt 查看三维形态|可量测（Measure，不落图）或标注（Dimension，落图）|是（Components 面板）|".sldasm = 3D Assembly drawing" / ".sldprt = 3D Part drawing" SLIDE 50（Ch4）|


视图体系总结【本报告推导】：KC 卫材图纸的完整表达体系 = 2D 三件套（Overhead + Cross Section + Detail View）+ 1 个数据表（BOM）+ 2 个文本区（Notes/Refs + Title Block）+ 3D 交互层（eDrawings 的 Components/Explode/Measure）。传统机械制图的 Front/Top/Side 三视图被彻底弃用，由「平铺俯视 + 剖面」替代 —— 这是薄型柔性叠层产品的制图范式。

#### T6 Drawing 图框字段说明表

源：SLIDE 31–32（Title Block 概念）+ SLIDE 33（图像）（DRCS File Information 实例）+ SLIDE 24（图像）（图框落款）。

||||||
|---|---|---|---|---|
|Drawing Number|图号|是|C153-FPS-01575-J-09；C153-FPS-01592-1-10|全局唯一主键；结构 = 平台前缀 + 类型码（FPS/FP1/FPM）+ 序列号 + 版本段 SLIDE 33（图像）|
|TITLE|标题|是|Title: DIAPER|产品大类 SLIDE 33（图像）|
|User Defined Title|自定义标题|是|BCM, SPDV, TOTAL, S1|承载平台 / 变体 / 尺码三段信息；是本例中唯一标明尺码的字段 SLIDE 33（图像）|
|Drawn By（≡ Created by）|绘制/创建人|是（字段名作 Created by）|Q06027（工号制）|KC 以工号而非姓名落款，含精确到秒的时间戳 SLIDE 33（图像）|
|Date（≡ Created/Last Issued date）|日期|是（字段名作 Created by on <ts> / Last Issued by on <ts>）|Wed May 27 00:49:14 CDT 2020 / Thu Apr 6 08:45:31 CDT 2023|双时间戳：创建 + 最后发行。时区 CDT SLIDE 33（图像）|
|Last Issued by|最后发行人|是|Q06411|与 Created by 工号不同 → 该图纸曾被他人修订并重新发行 SLIDE 33（图像）|
|Company / Owner|归属|是（图框落款）|"Kimberly-Clark Corporation"（图纸右下角）|SLIDE 24（图像）|
|Part Name|零件名|[未找到原句]|—|本材料以 Ordering Description 承担此职能（如 DIAPER, BCM, S1, FLAP 45MM HEIGHT）。功能等价物 SLIDE 33（图像）|
|Description|描述|[未找到原句]（字段名）|DIAPER, BCM, S1, PAD, DISCRETE 等|同上，等价于 Ordering Description 列|
|Material|材料|[未找到原句]|—|无独立字段；材料规格内联于 Ordering Description（NO IFIT、DISCRETE、PICASSO EMBOSSING）【本报告推导，见概念 11】|
|QUANTITY REQUIRED|需求量|[未找到原句]（字段名）|BOM_A 的 Qty 列，11 行全部 = 1|功能等价物；含义为「每单位成品消耗子件数」SLIDE 33（图像）|
|APPROVALS|审批|[未找到原句]（Ch2 内）|—|Ch2 无；Ch3 SLIDE 45 提供完整审批矩阵：M(Part)→PD/PD；FP1/FP2→PD/PD；FPS→PD & Senior PD / Senior Quality Engineer。另 Rex Stuart is the only one who can approve a completed FPS drawing SLIDE 44（Ch3）|
|Tolerances|公差|[未找到原句]|无数值|本章未出现任何公差数值或公差块 → 不可从本章导出任何合格判据|
|Projections|投影法|[未找到原句]|无|本章未标注第一角/第三角投影符号|
|REV / 版本|版本|部分（图号末段）|-J-09、-1-10、-B-01、-D-04|版本信息编码于图号末段而非独立字段【本报告推导】|


字段完整性结论【本报告推导】：Ch2 可确证的图框字段共 7 个（Drawing Number、Title、User Defined Title、Created by、Last Issued by、Company、Qty/内嵌版本）；任务书点名的 11 个字段中，Part Name / Description / Material / QUANTITY REQUIRED 存在功能等价物（以 BOM 的 Ordering Description 与 Qty 列实现），APPROVALS / Tolerances / Projections 在本章完全缺失（APPROVALS 需引 Ch3）。

### 模块4：章节间衔接（Chapter Connections）

#### 4.1 与 Ch1（Finding Drawings, SLIDE 1–19）：「图号 → 图纸内容（BOM / 尺寸 / 材料）」的完整链路

|||||
|---|---|---|---|
|① 定位规格书|The SPOT → Variant Specification Search → SPOT Specifications → 用筛选器定位产品/变体 → 点 Variant Property Spec 号下载规格书|—|Ch1 SLIDE 4–6|
|② 取得图号|打开 Word 规格书 → 滚到底部找图纸与图号；或 Ctrl+F 搜 draw 跳转|图号是读图的唯一入口|Ch1 SLIDE 7|
|③ 进入 DRCS|DRCS – Drawing Release Control System（Central CAD 主页）；DRCS 首页图纸号输入框示例即 C153-FPS-01575|与 Ch2 的 BOM_A 父图号 C153-FPS-01575-J-09 完全一致 —— 同一张图贯穿两章|Ch1 SLIDE 8–9（图补充）；Ch2 SLIDE 33（图像）|
|④ 文件操作|Checkout/Release、Download copy、View image、Print file|取得图纸本体|Ch1 SLIDE 9–12|
|⑤ 取 BOM|Where Used and BOM information（导航 News / Search / Create / Change Title / Issue / Approve）|→ Ch2 的 BOM_A 11 行即为该功能的输出实例|Ch1 SLIDE 13 → Ch2 SLIDE 33（图像）|
|⑥ 取历史|Access back issues and drawing information|→ Ch2 的 Created by / Last Issued by 双时间戳|Ch1 SLIDE 14 → Ch2 SLIDE 33（图像）|
|⑦ 高级检索|Advanced Search，PREFIX 与 TYPE 两个筛选器最有用|按前缀（C153）+ 类型（FPS/FP1/FPM）定位 → 与 BOM 中的子图号体系对应|Ch1 SLIDE 15|
|⑧ 判别工具链|蓝 A = AutoCAD（layers）；红 S = SolidWorks（LEGOs）|→ Ch2 SLIDE 33–34 通篇讲 SolidWorks 的 BOM 逻辑|Ch1 SLIDE 16 → Ch2 SLIDE 33–34|
|⑨ 判别层级|FPM = Part（最小单元）／FP1 = Assembly（FPM 组合，例 Nonwoven + Adhesive）／FPS = Finished Product（工厂用）|→ BOM_A 实证：7×FP1（结构件）+ 4×FPM（胶/橡筋），父图为 FPS|Ch1 SLIDE 17–19 → Ch2 SLIDE 33（图像）|
|⑩ 回溯历史|Access back issues and drawing information|→ Last Issued by 时间戳|Ch1 SLIDE 14|


链路闭环结论【本报告推导】：Ch1 解决「拿到哪张图」（图号获取 + 层级判别 + 工具链识别），Ch2 解决「这张图里有什么」（六大区块 + BOM 尺寸 + 材料规格 + 治理元数据）。Ch1 的 SLIDE 13（Where Used and BOM）是两章的物理接口：Ch1 教你按这个按钮，Ch2 展示按完按钮看到的 11 行数据。且 Ch1 SLIDE 9 的示例图号 C153-FPS-01575 与 Ch2 BOM_A 父图 C153-FPS-01575-J-09 为同一图纸，证明两章使用同一实例贯穿教学。

#### 4.2 与 Ch3（Editing Drawings, SLIDE 35–46）：为什么读懂 BOM 是变更的前提

核心命题：改一个尺寸 = 改一个物料号 = 触发一张新图纸 = 波及多个父图。

||||
|---|---|---|
|能读 BOM 的 11 行结构与 Ordering Description 编码规则|填写 Redline 模板的 Product Description 列：必须写出 DIAPER, SURGE, 100MM WIDE X 236MM LONG 这样的完整物料描述，否则无法定位变更对象|Ch2 SLIDE 33（图像） 的 DIAPER, BCM, SMALL SURGE 100MM W, 236MM L ↔ Ch3 SLIDE 38 的 DIAPER, SURGE, 100MM WIDE X 236MM LONG|
|能读 Drawing Number 的层级（FPS/FP1/FPM）|填写 Redline 模板的 FPS or PDD Drawing Impacted / C153-FP1 Drawing Impacted / C153-FPM Drawing Impacted 三列 —— 三列正是 Ch1 的三层层级|Ch2 SLIDE 33（图像） ↔ Ch3 SLIDE 37–38 表头|
|能识别 find number ↔ 子图号的双射|反查受影响的父图集合（All Parents）|Ch2 SLIDE 33（图像） 按钮 All Parents / All Children ↔ Ch3 SLIDE 37 Notes："Before revising a drawing make sure you are OK that all Parents of the drawing will receive the change."|
|能读 Qty 与尺寸在描述中的编码|判断是 Revise 还是 New|Ch3 SLIDE 41："New drawings are required if the drawing you wish to edit is being used somewhere else that your edit(s) wouldn't apply to."|
|能判别 SolidWorks（红 S）与 BOM 导航|理解为何改一处要动多层|Ch2 SLIDE 34："SolidWorks drawings rely more on BOM / Where Used to highlight details." ↔ Ch3 SLIDE 37 Notes："A FPS or PDD drawing could have more than 1 FP1 or FPM drawing change."|


##### ★ 关键实例：一个 find number 的变更如何波及 5 张 FPS 图纸

这是全材料中「读懂 BOM 是变更前提」的最强实证：

||||
|---|---|---|
|Ch2 中的对象|BOM_A 第 7 行：DIAPER, BCM, SMALL SURGE 100MM W, 236MM L → 子图号 C153-FP1-00178-D-04|SLIDE 33（图像）|
|Ch3 中的变更|Redline 模板行：DIAPER, SURGE, 100MM WIDE X 236MM LONG → FP1 = C153-FP1-00178 → FPM = C153-FPM-00481（蓝底=修订）|SLIDE 38（Ch3）|
|受影响的 FPS 图纸|C153-FPS-01640、C153-FPS-01641、C153-FPS-01577、C153-FPS-01574、C153-FPS-01575 —— 共 5 张|SLIDE 38（Ch3）|
|闭环|5 张受影响 FPS 中，C153-FPS-01575 正是 Ch2 BOM_A 的父图|跨章精确对账|
|变更内容|"Remove apertures in the front / urine management zone."（移除前部 / 尿液管理区的开孔）；工程变更号 ER# 900200005649|SLIDE 38（Ch3）；SLIDE 39–40（Ch3）图注 "Remove smaller holes in the front along with the associated dimensions."|
|方案迭代|由「Revise 现有 FPM（蓝底 C153-FPM-00481）」改为「以 C153-FPM-00481 为基线新建 FPM（Peach 底 New – 1）」|SLIDE 42（Ch3）|


传导链量化【本报告推导】：

改 1 处几何（移除 surge 前部 UMZ 开孔）
  → 变 1 个 FPM 图纸（C153-FPM-00481 → New–1）
  → 变 1 个 FP1 组件图纸（C153-FP1-00178）
  → 波及 5 张 FPS 成品图纸（01640/01641/01577/01574/01575）
  → 每张图纸按 8 hrs 估算（Ch3 SLIDE 44）→ 若全部新建/修订，工时量级 ≈ 7 张 × 8 hrs = 56 hrs

结论【本报告推导】：Ch2 教的「读 BOM」不是阅读技能，而是「变更影响域建模」的前置能力。不读 BOM 就无法回答 Ch3 模板强制要求的三个问题：① 改哪个 Product Description；② 影响哪几张 FPS/FP1/FPM；③ 是 Revise 还是 New。BOM 中的 find number 是唯一能让「一个几何改动」与「N 张图纸」建立映射的索引键。

附加印证【本报告推导】：Ch2 BOM_A 第 7 行的 surge 描述为 SMALL SURGE 100MM W, 236MM L，而 Ch3 的变更正是移除该 surge 前部的 UMZ 开孔 —— 说明 Ch2 展示的 BOM 状态是「含 UMZ 开孔」的旧状态（图纸最后发行于 2023-04-06，SLIDE 33（图像）），而 Ch3 的 ER# 900200005649 是在其后的变更。两份材料一前一后，构成同一产品的版本演变证据链。

#### 4.3 与 Ch4（3D Viewer, SLIDE 47–66）的前瞻衔接

||||
|---|---|---|
|SolidWorks 图纸不在图面堆砌全部尺寸，需沿 BOM 下钻（SLIDE 33–34）|Components 面板逐级下钻，左键点击在列表与图形中同时高亮|Ch4 SLIDE 52–53|
|2D 图无爆炸图（本章无 Exploded view）|Explode 滑块分离零件|Ch4 SLIDE 59–60|
|2D 图尺寸需逐一标注|Measure 直接量测（不落图）vs Dimension（落图）|Ch4 SLIDE 55–57|
|胶路/层序需读 Cross Section|Make Transparent / Hide Others (Isolate) 透视层序|Ch4 SLIDE 54|

### 模块5：业务连接点（Business Connections）



业务背景：卫材（纸尿裤 / 湿巾）创新研发 + 木浆与纸品战略采购。
本章定位：全 5 章材料中商业情报密度最高的一章 —— Ch1 讲检索（无产品数据）、Ch3 讲流程（仅 1 个 surge 案例）、Ch4 讲软件操作、Ch5 讲权限；唯独 Ch2 给出了两个平台的完整 BOM 尺寸（T1 的 11 项 + T2 的 10 项 + 5 段耳贴轮廓），是唯一可用于竞品结构反演的数据源。

#### 连接点 1【★ 最高价值】竞品结构反演：从 BOM 尺寸反推 KC 纸尿裤的结构设计意图

涉及幻灯片：SLIDE 33（图像）（BOM_A，S1）、SLIDE 34（图像）（p34 BOM，SS）
核心概念：Surge（导流层）、Picasso Embossing（压花）、Absorption Target（吸收目标）、Find number
关键数据：SURGE 100 mm × 236 mm（S1，素面） vs 74 mm × 197 mm（SS，PICASSO EMBOSSING）

##### 两种导流策略的对比分析

||||
|---|---|---|
|代表规格|SMALL SURGE 100MM W, 236MM L|SURGE PICASSO EMBOSSING 74MM W × 197MM L|
|** Surge 绝对面积**|23,600 mm²|14,578 mm²（−38.2%）|
|** Surge / 芯体面积占比**|51.4%|24.5%（腰斩）|
|** Surge 幅宽覆盖率**|80.0%（100/125）|59.2%（74/125）|
|** Surge 长度覆盖率**|64.3%（236/367）|41.4%（197/476）|
|导流机制|靠 surge 非织造材料本体的面内毛细铺展；液体到达后被大面积材料迅速横向扩散并向下传递|靠压花沟槽（embossing channels）建立定向低阻力通道，将液体沿沟槽定向输送，材料用量小但方向性强|
|材料单耗|高（材料面积 +38.2% 相对量 ≈ surge 用量多约 62%）【推导：23,600/14,578 = 1.619】|低（surge 用量约为 S1 的 61.8%）|
|工艺复杂度|低（素面非织造裁切贴合）|高（需压花工位，压花辊成本与寿命为新增变量）|
|性能取向|快速铺展、防回渗、对多次小量排尿鲁棒|定向快速下渗、配合长芯体做纵深储存、对单次大量排尿鲁棒|
|与芯体的配合|宽 surge + 短芯（367 mm）：铺展后就近吸收|窄 surge + 长芯（476 mm）：前端集中导流 → 后端纵深储存（自洽设计）|
|成本结构迁移|材料成本主导（非织造用量大）|工艺/设备成本主导（压花辊、精度控制）+ 材料节约|


战略解读【本报告推导】：
1. KC 内部同时并存两套导流技术路线，且从 S1（老，无压花、图纸 2020 创建/2023 最后发行） 到 SS（新，PICASSO 压花） 呈现从「材料堆量」向「结构导流」的迁移。对本方研发的启示：压花导流是 KC 已验证的量产路线，可作为本方下一代产品的技术对标基准。
2. SS 的「窄 surge + 长芯 + 宽腰带 + iFit 环 + 宽腿部包覆」是一组高度自洽的设计包：节省的 surge 材料成本被投入到 iFit 贴合环、加宽腰带、加宽腿部弹性包覆上。这不是简单的降本，而是成本再分配（cost reallocation） —— 从「吸收材料」转移到「贴合与舒适」。
3. 对木浆与纸品战略采购的直接含义：SS 路线的 surge 用量下降 38.2%，若该路线在 KC 全线推广，导流层非织造（及其中可能含有的绒毛浆/木浆基材料）的单耗将系统性下降。采购侧应据此下调导流层相关材料的长期需求预测，并将预算重心转向弹性材料（橡筋）与热熔胶（见连接点 2、3 —— 二者在 SS 平台均为上升）。

可执行行动建议：
1. 建立「导流策略二维坐标」对标图：X 轴 = surge 面积 / 芯体面积（0–60%），Y 轴 = 是否有压花/沟槽结构。将 KC 的 S1（51.4%, 无）、SS（24.5%, 有）与本方主流产品、P&G、尤妮佳、大王的拆解数据一并打点，识别技术路线空位（本方应抢占的坐标区域）。
2. 立项验证压花导流的性价比：以 surge 面积减少 38% 为目标，测算材料节约额 vs 压花辊投资 + 工艺良率损失，输出盈亏平衡产量。
3. 采购侧联动预警：若本方跟进压花路线，需同步重签导流层非织造的长协量（可能下调 30%+），避免库存呆滞。

#### 连接点 2【★ 采购量级】胶用量估算：由涂布面积反推单片用胶量与年采购量级

涉及幻灯片：SLIDE 33（图像）（S1：pad adh 125×367、leg adh 199×227）、SLIDE 34（图像）（SS：pad adh 125×476、leg adh 232×279）
核心概念：PAD TO LINER ADHESIVE（芯体-底膜胶）、LEG ELASTIC ADHESIVE（腿部橡筋包覆胶）、涂布克重（basis weight / add-on）
关键数据：见下表面积

##### 步骤 1：涂布面积（源数据直算）

|||||||
|---|---|---|---|---|---|
|PAD TO LINER ADH|S1|125 × 367|45,875|458.75|0.045875|
|PAD TO LINER ADH|SS|125 × 476|59,500|595.00|0.059500|
|LEG ELASTIC ADH|S1|199 × 227|45,173|451.73|0.045173|
|LEG ELASTIC ADH|SS|232 × 279|64,728|647.28|0.064728|
|两项合计|S1|45,875 + 45,173|91,048|910.48|0.091048|
|两项合计|SS|59,500 + 64,728|124,228|1,242.28|0.124228|




不可计算的胶：① S1 的 EAR ADHESIVE, 202 OUTSIDE W × 182 INSIDE W（仅给宽度，缺长度）→ [数据不足]；② SS 的 EAR REINFORCEMENT ADH 268 × 200 × 500MM MD（三元组歧义）→ [数据歧义]。故下表的单片用胶量为「两类主胶的合计」，是全片用胶量的下界（lower bound），实际总用胶还需加上耳胶、腰胶、结构胶等。【本报告推导 · 边界声明】

##### 步骤 2：单片用胶量（三档克重情景）

外部参数 [外部参数]（本章材料未提供任何克重数据，以下为卫材热熔胶行业典型涂布克重区间，仅用于量级估算）：

||||
|---|---|---|
|低（Low）|8 g/m²|18 g/m²|
|基准（Base）|12 g/m²|25 g/m²|
|高（High）|16 g/m²|35 g/m²|




依据 [外部参数]：橡筋包覆胶克重通常显著高于结构胶，因须完全包覆并锚定橡筋丝以防止蠕变与脱胶。

单片用胶量 = 涂布面积（m²） × 涂布克重（g/m²）

||||||
|---|---|---|---|---|
|S1|PAD TO LINER|0.045875 × 8 = 0.367 g|0.045875 × 12 = 0.551 g|0.045875 × 16 = 0.734 g|
|S1|LEG ELASTIC|0.045173 × 18 = 0.813 g|0.045173 × 25 = 1.129 g|0.045173 × 35 = 1.581 g|
|S1|两项合计|1.180 g/片|1.680 g/片|2.315 g/片|
|SS|PAD TO LINER|0.0595 × 8 = 0.476 g|0.0595 × 12 = 0.714 g|0.0595 × 16 = 0.952 g|
|SS|LEG ELASTIC|0.064728 × 18 = 1.165 g|0.064728 × 25 = 1.618 g|0.064728 × 35 = 2.265 g|
|SS|两项合计|1.641 g/片|2.332 g/片|3.217 g/片|
|Δ（SS − S1）||+0.461 g/片（+39.1%）|+0.652 g/片（+38.8%）|+0.902 g/片（+39.0%）|




比例校验【本报告推导】：Δ% ≈ +36.5%（= 面积比 124,228 / 91,048 − 1），与三档情景算出的 +38.8%~+39.1% 的差异源于 pad 胶与 leg 胶克重不同。结论稳健：SS 平台这两类主胶的单耗比 S1 高约 36%–39%。

##### 步骤 3：采购量级估算（年采购量）

单片用胶量（Base 情景）：S1 = 1.680 g/片，SS = 2.332 g/片

|||||
|---|---|---|---|
|1 亿片/年|1.680 g × 1×10⁸ = 1.680×10⁸ g = 168.0 t|2.332 g × 1×10⁸ = 233.2 t|+65.2 t（+38.8%）|
|5 亿片/年|839.9 t|1,166.1 t|+326.2 t|
|10 亿片/年|1,679.8 t|2,332.2 t|+652.4 t|


三档情景下的「每亿片用胶量」速查表【本报告推导】：

||||
|---|---|---|
|Low|118.0|164.1|
|Base|168.0|233.2|
|High|231.5|321.7|


结论与可执行行动建议【本报告推导】：
1. 量级判断：单片纸尿裤的「芯体胶 + 腿部胶」合计用胶量约 1.2–3.2 g/片，对应每亿片 118–322 吨。这是热熔胶采购谈判的量级锚点，可用于校验供应商报价的合理性。
2. 平台切换的采购影响：若产线由 S1 类平台切换至 SS 类平台，每 10 亿片将新增约 652 吨热熔胶需求（Base 情景，+38.8%）。采购侧须提前 6–12 个月锁定增量供应，并重新谈判阶梯价。
3. 胶种结构迁移：SS 平台的腿部胶增幅（+43.3% 面积）大于芯体胶增幅（+29.7% 面积）【见 T3】。这意味着高价橡筋包覆胶在胶料结构中的占比上升 —— 即使总胶量上升 38.8%，胶料加权单价的涨幅将超过 38.8%。采购谈判应针对橡筋包覆胶单独议价。
4. 降本杠杆识别【本报告推导】：腿部包覆胶是最大单一胶耗项（Base 情景下 S1 占 67.2%、SS 占 69.4%）。降低腿部包覆胶带宽 10%（SS 从 88.9 mm → 80.0 mm）即可节省约 0.162 g/片 ≈ 16.2 t/亿片。建议将「腿部包覆胶窄幅化 + 提高克重」作为首选降本课题（保持总胶量不变但提升锚固力）。
5. 数据缺口补齐：本估算未含耳胶、腰胶、结构胶。建议通过实物拆解称重法实测全片总胶量（溶剂萃取或热失重），与本估算的下界交叉校验，反推出「其他胶」的占比。

#### 连接点 3 橡筋（LEG ELASTIC STRANDS）长度差异对腿部贴合与成本的影响

涉及幻灯片：SLIDE 33（图像）（S1：152 mm FRONT / 173.1 mm REAR）、SLIDE 34（图像）（SS：165 mm FRONT / 199 mm REAR）
核心概念：Leg Elastic Strands（腿部橡筋丝）、前/后非对称性、包覆带宽、腿部贴合
关键数据：见下表

##### 3.1 长度差异与贴合设计推导

||||||
|---|---|---|---|---|
|单侧总长|front + rear|152 + 173.1 = 325.1 mm|165 + 199 = 364.0 mm|+38.9 mm（+12.0%）|
|双侧总长|× 2|650.2 mm|728.0 mm|+77.8 mm（+12.0%）|
|后/前比|rear ÷ front|173.1 ÷ 152 = 1.139|199 ÷ 165 = 1.206|+0.067|
|前后差|rear − front|21.1 mm|34.0 mm|+12.9 mm（+61.1%）|
|隐含包覆带宽|leg adh 面积 ÷ 双侧总长|45,173 ÷ 650.2 = 69.5 mm|64,728 ÷ 728.0 = 88.9 mm|+19.4 mm（+27.9%）|


贴合解读【本报告推导】：
1. SS 的腿部弹性总长 +12.0%、包覆带宽 +27.9%，两者叠加意味着 SS 的腿部弹性有效作用区（面积）显著扩大：从 S1 的「窄带线密封」升级为 SS 的「宽带面密封」。
2. 前后非对称度从 13.9% 提升到 20.6%，反推 SS 的腿洞弧线更靠后、后段更外扩。产品语义为强化仰卧/后躺位的后漏防护（后腰-臀部为仰卧位主要积液区）。这与 SS 同时加宽腰带（44→58 mm）形成「后段强化」的一致设计意图。
3. 设计策略分野：S1 = 「小开口 + 高护围（45 mm）」 的机械兜挡；SS = 「大开口 + 强弹性 + 宽包覆」 的弹性跟随。后者对活动量大的婴儿适配性更好，前者对稀便兜挡更可靠 —— 这是年龄/使用场景分化的设计信号。

##### 3.2 成本影响估算

外部参数 [外部参数]：典型卫材腿部橡筋规格 620 dtex（莱卡/氨纶）。单位换算：620 dtex = 620 g / 10,000 m = 0.062 g/m。

假设：单侧 1 根橡筋（源材料未标注根数 → 给出 1/2/3 根三档敏感性）【本报告推导】

||||||
|---|---|---|---|---|
|1 根|S1 0.6502 m / SS 0.7280 m|0.6502 × 0.062 = 0.0403 g/片|0.7280 × 0.062 = 0.0451 g/片|+0.0048 g（+12.0%）|
|2 根|S1 1.3004 m / SS 1.4560 m|0.0806 g/片|0.0903 g/片|+0.0097 g|
|3 根|S1 1.9506 m / SS 2.1840 m|0.1209 g/片|0.1354 g/片|+0.0145 g|


采购量级（1 根/侧，Base）【本报告推导】：

|||||
|---|---|---|---|
|1 亿片/年|4.03 t|4.51 t|+0.48 t|
|10 亿片/年|40.3 t|45.1 t|+4.8 t|


关键成本洞察【本报告推导】：
1. 橡筋丝本身的质量成本极小（0.04–0.14 g/片，即 4–14 t/亿片），远小于其包覆胶的质量（1.13–2.27 g/片，即 113–227 t/亿片）。比值约 1 : 20 ~ 1 : 28。因此腿部弹性的成本主体是「胶」而非「丝」。
2. 降本杠杆应优先作用于包覆胶而非橡筋丝：减少橡筋根数可同时减少丝与胶，但降低包覆胶克重或带宽的杠杆更大。
3. SS 平台的腿部弹性总成本增幅【推导】：胶 +43.3%（面积）、丝 +12.0%（长度）→ 加权增幅约 +40%（胶占成本主体）。SS 平台在腿部弹性上是明显的成本加法，换取的是贴合与防漏性能 —— 印证了连接点 1 的「成本再分配」判断。
4. 橡筋丝径/根数的敏感性：源材料未标注 dtex 与根数，这是本估算的最大不确定源。建议在实物拆解中优先实测这两个参数（见连接点 4）。

可执行行动建议：
1. 在竞品拆解中，必测项：橡筋根数、单根 dtex、拉伸倍率（draw ratio）、包覆胶带宽、包覆胶克重。这 5 项决定腿部贴合性能与成本的 90%。
2. 建立「腿部弹性成本模型」：总成本 = 丝长 × 根数 × dtex线密度 × 丝单价 + 包覆面积 × 克重 × 胶单价。用该模型对 S1/SS 与本方产品做三方对标。
3. 采购侧：橡筋（氨纶）采购量级为 4–14 t/亿片，属小宗高单价材料，应关注氨纶价格波动而非量级谈判；热熔胶为 113–227 t/亿片，属大宗，应重点做量价挂钩。

#### 连接点 4 本方建立同等 BOM 拆解能力的建议：拿竞品实物拆到 find number 级，建立结构数据库

涉及幻灯片：SLIDE 27–28（BOM 概念）、SLIDE 33（图像）（BOM_A 结构：Find No. / Qty / Ordering Description / Drawing Number）、SLIDE 34（图像）（Detail View 承载局部尺寸）、SLIDE 22（Overhead View 承载检验尺寸）
核心概念：Find number（最小可比单元）、BOM 四元组、Dimensional Inspection、Material spec 编码规则

##### 4.1 能力差距诊断

|||||
|---|---|---|---|
|BOM 粒度|11 个 find number，每个部件独立图号，尺寸编码进物料描述|若仅有「规格书」而无 find number 级 BOM，则无法定位变更影响域|结构性差距|
|尺寸编码|尺寸写入 Ordering Description（WAISTBAND 44MM WIDTH、SURGE 100MM W, 236MM L）→ 改尺寸即改物料号|若尺寸独立于物料编码，则变更追溯链断裂|编码规则差距|
|层级体系|FPS / FP1 / FPM 三层，7 个 FP1 + 4 个 FPM|需建立等价的三层体系|体系差距|
|版本治理|双时间戳（Created by / Last Issued by）+ 版本段编码在图号|—|治理差距|
|变更影响域|All Parents / All Children 一键反查；实证「1 个 FPM → 5 张 FPS」|—|追溯能力差距|

##### 4.2 竞品实物拆解的 find number 级作业规范（建议）

目标：将竞品实物拆解为与 KC BOM_A 同构的表格，实现逐行对标。

必采字段（对应 KC 的四元组）【本报告推导，字段设计对标 SLIDE 33（图像）】：

||||||
|---|---|---|---|---|
|1|Find No.|Find No.|按由贴身面到外层的层序编号（建议 1 = 面层/贴身层，递增至底层）|★★★|
|2|部件名（EN）|Ordering Description|沿用 KC 命名体系（surge / pad / outer cover / inner cover / waistband / flap / ear / leg elastic strand / adhesive）|★★★|
|3|Qty|Qty|每片消耗件数（KC 全为 1；护围/耳贴常见 2）|★★|
|4|长（MD）× 宽（CD）× 厚|尺寸（编码于描述）|展开平铺后测量；厚用厚度计（±0.01 mm）|★★★|
|5|克重（g/m²）|Material spec|裁 100 cm² 称重|★★★|
|6|材料定性|Material spec（如 NO IFIT / DISCRETE）|FTIR / 显微镜 / 燃烧法|★★|
|7|加工特征|Material spec（如 PICASSO EMBOSSING）|压花深度、花纹周期、开孔率（UMZ）|★★★|
|8|胶：涂布面积 + 图案 + 克重|PAD TO LINER ADH 125×367 等|图像法测图案；溶剂萃取或热失重测克重|★★★|
|9|橡筋：根数 / dtex / 倍率|LEG ELASTIC STRANDS 152 F / 173.1 R|拆解计数 + 单丝线密度 + 标记间距法测倍率|★★★|
|10|局部特征尺寸|Detail View（如 EAR PROFILE 68/30/56/75/115）|二次元影像仪|★★|
|11|前/后分区尺寸|FRONT / REAR、BACK END 90MM|以产品几何中线为基准|★★★|
|12|版本号 / 生产批|Last Issued by 时间戳|包装喷码|★|


测量基准统一要求【本报告推导，依据 SLIDE 22 "laid out flat"】：
- 必须在产品平铺展开态下测量（与 KC Overhead View 同基准），否则所有 MD/CD 尺寸不可比。
- MD / CD 必须分别标注（KC 严格区分 125MM CD × 367MM MD），不得只给「长×宽」。
- 前/后段必须以同一基准线分割（KC 用 FRONT / REAR、BACK END）。

##### 4.3 结构数据库建设路径（三阶段）

|||||
|---|---|---|---|
|P1（0–3 月）：建标|完成 1 款本方产品 + 2 款竞品（建议含 KC 同平台产品）的 find number 级拆解|3 份 BOM 拆解表 + 测量 SOP + 术语对照表|≥ 3 款 × ~11 find number ≈ 33 行|
|P2（3–9 月）：扩面|覆盖主流竞品矩阵（按价位段 × 尺码分层抽样）|结构数据库 v1.0（含 surge 面积占比、胶面积、橡筋长度等派生指标）|≥ 15 款 ≈ 165 行|
|P3（9–18 月）：建模|建立「结构参数 → 性能 → 成本」回归模型|可对标预测模型 + 降本杠杆排序|≥ 40 款 ≈ 440 行|


数据库必备派生指标【本报告推导，全部由本章 T1/T2 的原始尺寸可算出，证明这些指标是 BOM 的天然导出量】：

||||
|---|---|---|
|Surge 覆盖率|surge W×L ÷ pad CD×MD|导流策略判别（S1 51.4% vs SS 24.5%）|
|芯体长宽比|pad MD ÷ pad CD|版型判别（S1 2.94 vs SS 3.81）|
|腿部前后非对称度|rear ÷ front|腿洞弧线判别（S1 1.139 vs SS 1.206）|
|隐含包覆带宽|leg adh 面积 ÷ 双侧橡筋长|密封形式判别（S1 69.5 mm vs SS 88.9 mm）|
|单片主胶用量|Σ(面积 × 克重)|成本对标（S1 1.68 g vs SS 2.33 g，Base）|
|胶/丝质量比|包覆胶质量 ÷ 橡筋质量|工艺取向（约 20–28 : 1）|
|护围/腰带比|flap H ÷ waistband W|防漏策略判别（S1 45/44 = 1.02 vs SS 37/58 = 0.64）|




注：最后一项 S1 = 1.02 → SS = 0.64，是「机械兜挡 → 弹性跟随」策略切换的单一数值判据，建议纳入数据库核心 KPI。【本报告推导】

可执行行动建议（汇总）：
1. 立即启动：采购 KC 同平台实物（优先对标 C153-FPS-01575 的 S1 与 C153-FPS-01592 的 SS 对应市售品），按上述 12 字段拆解，与本章 BOM 数据逐行交叉验证 —— 这是唯一能校验本报告推导假设（如「pad 胶矩形 ≈ 芯体轮廓」）的方法。
2. 术语对齐：将本方 BOM 命名体系统一为 KC 体系（surge / flap / waistband / eyespot / iFit / discrete / nondiscrete），否则跨公司对标不可行。
3. 建立双解释约束机制：数据库中必须强制记录尺码字段，避免重蹈本章「S1 vs SS 差异无法区分尺码效应与代差」的覆辙（见 T3 警告）。
4. 优先级排序：拆解资源应优先投入 surge（导流策略）+ leg elastic（贴合策略）+ 胶（成本主体） 三大件，这三项已由本章证明为区分产品代际的判别性变量。


#### 模块5 附：「可直接用于竞品分析」的数据清单表



下表汇总本章全部可直接引用的量化数据，每行标注来源幻灯片与竞品分析用途。全部为源材料直读或本报告明示算式推导，不含编造数据。

|||||||
|---|---|---|---|---|---|
|1|Surge 宽 × 长|100 × 236 mm|74 × 197 mm|SLIDE 33（图像） / SLIDE 34（图像）|导流策略判别|
|2|Surge 工艺|素面（SMALL SURGE）|PICASSO EMBOSSING|同上|工艺代际判别|
|3|Surge 面积|23,600 mm²|14,578 mm²|推导：1×1|材料单耗对标|
|4|Surge / 芯体面积比|51.4%|24.5%|推导|★ 导流策略核心 KPI|
|5|Pad（芯体）宽 CD|125 mm|125 mm|SLIDE 33/34（图像）|产线幅宽兼容性|
|6|Pad（芯体）长 MD|367 mm|476 mm|由 pad adh MD 反推|吸收容量对标|
|7|Pad 成型方式|DISCRETE|NONDISCRETE|SLIDE 33/34（图像）|★ 工艺路线分野|
|8|Flap 高|45 mm|37 mm|同上|兜挡策略（反向变化，判别力强）|
|9|Waistband 宽/高|44 mm|58 mm|同上|腰部舒适/贴合策略|
|10|护围/腰带比|1.02|0.64|推导：8 ÷ 9|★ 防漏策略单一判据|
|11|Inner cover 总长|198 mm|202 mm|同上|片长对标|
|12|Inner cover 尾端|90 mm|85 mm|同上|后段分区设计|
|13|Outer cover|NO IFIT|295 mm W + FIT LOOP 43 mm W|同上|★ 贴合结构有无|
|14|Leg elastic 前段|152 mm|165 mm|同上|前腿围|
|15|Leg elastic 后段|173.1 mm|199 mm|同上|后腿围|
|16|Leg elastic 前后比|1.139|1.206|推导：15 ÷ 14|★ 腿洞弧线不对称度|
|17|Leg elastic 双侧总长|650.2 mm|728.0 mm|推导：×2|橡筋用量|
|18|Leg elastic ADH CD × MD|199 × 227 mm|232 × 279 mm|SLIDE 33/34（图像）|腿部密封形式|
|19|Leg elastic ADH 面积|45,173 mm²|64,728 mm²|推导|用胶量（最大项）|
|20|隐含包覆带宽|69.5 mm|88.9 mm|推导：19 ÷ 17|★ 线密封 vs 面密封|
|21|Pad to liner ADH CD × MD|125 × 367 mm|125 × 476 mm|SLIDE 33/34（图像）|芯体尺寸反推|
|22|Pad to liner ADH 面积|45,875 mm²|59,500 mm²|推导|用胶量|
|23|两类主胶面积合计|91,048 mm²|124,228 mm²|推导：19 + 22|用胶量对标|
|24|两类主胶单片用量（Base）|1.680 g/片|2.332 g/片|推导（含 [外部参数]）|★ 采购量级锚点|
|25|每亿片用胶量（Base）|168.0 t|233.2 t|推导|★ 采购谈判锚点|
|26|橡筋质量（1 根/侧，620 dtex）|0.0403 g/片|0.0451 g/片|推导（含 [外部参数]）|橡筋采购量级|
|27|胶/丝质量比|≈ 28 : 1|≈ 36 : 1|推导：19项胶质量 ÷ 26|★ 降本杠杆定位|
|28|Ear adhesive|202（外宽）× 182（内宽）mm|EAR REINFORCEMENT 268×200×500 MD|SLIDE 33/34（图像）|耳贴结构（[数据不足/歧义]）|
|29|Ear profile 细部尺寸|未提取|68 / 30 / 56 / 75 / 115 mm|SLIDE 34（图像）|耳贴轮廓对标|
|30|Ear overlap|未提取|20 mm|SLIDE 34（图像）|耳贴搭接量|
|31|BOM 行数|11|10（find number 未提取）|SLIDE 33/34（图像）|结构复杂度对标|
|32|层级构成|7 FP1 + 4 FPM|未提取|推导|架构对标|
|33|Qty（全部子件）|1|未提取|SLIDE 33（图像）|装配结构|
|34|图纸创建 / 最后发行|2020-05-27 / 2023-04-06|未提取|SLIDE 33（图像）|技术迭代节奏|
|35|尺码标识|S1（Size 1）|未标注|SLIDE 33（图像）|⚠ 对标前提，须补齐|
|36|Cross Section 图纸实例|C192-FFS-1544 / C192-PT1-1344，SIZE 2 (17-31)|—|SLIDE 24（图像）|剖面-胶路图惯例|
|37|Ch3 变更案例（surge）|C153-FP1-00178 → 影响 5 张 FPS|—|SLIDE 38（Ch3）|★ 变更影响域实证|

### 模块6：金句索引（Key Quotes Index）

||||||
|---|---|---|---|---|
|1|"Shows the product laid out flat with a top-down view of the body-facing side of the product."|SLIDE 22|「展示产品平铺展开、自顶向下观察其贴身面的视图。」|Overhead View 的唯一权威定义。三个限定词（laid out flat / top-down / body-facing side）构成了竞品拆解的测量基准 —— 不按此基准测得的尺寸与 KC 数据不可比。|
|2|"This view holds dimensions the operators will be checking most frequently."|SLIDE 22|「该视图承载着操作工检验频次最高的那些尺寸。」|把「视图」与「质量检验行为」绑定。反向推论：Overhead View 上的尺寸集合 ≈ 在线 Dimensional Inspection 的抽检项目清单。这是从图纸反推竞品质量控制重点的钥匙。|
|3|"CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT"|SLIDE 24（图像）|「剖面示意图与胶路布局」|KC 的制图惯例：剖面图 = 胶路图。拿到竞品/自有产品的剖面图，即等于拿到层数结构与施胶布局。对胶用量估算与层数对标具有决定性价值。|
|4|"SolidWorks drawings rely on BOM / Where Used feature to find detailed dimensions"|SLIDE 33|「SolidWorks 图纸依靠 BOM / Where Used（用在何处）功能来查找详细尺寸。」|KC 图纸刻意不在图面堆砌全部尺寸。读图 = 沿 BOM 导航，而非看图面。这解释了为什么 BOM 是情报密度最高的区块。|
|5|"SolidWorks drawings rely more on BOM / Where Used to highlight details."|SLIDE 34|「SolidWorks 图纸更多地依靠 BOM / Where Used 来突出细节。」|与 #4 构成递进（rely → rely more）。再次确认：BOM 是 SolidWorks 图纸的主信息载体，图面只是索引。|
|6|"DIAPER, BCM, SMALL SURGE 100MM W, 236MM L"|SLIDE 33（图像）|「纸尿裤，BCM（平台），小型导流层，宽 100 mm × 长 236 mm」|尺寸被编码进物料描述本身。这意味着「改尺寸 = 改物料号 = 触发新图纸」—— 是 Ch3 变更管理链条的制度性根源，也是竞品拆解必须对齐命名体系的原因。|
|7|"DIAPER, PAD TO LINER, ADHESIVE, 125MM CD X 367MM MD"|SLIDE 33（图像）|「纸尿裤，芯体对底膜，胶，横向 125 mm × 纵向 367 mm」|MD/CD 严格区分的范例，且该矩形是反推芯体尺寸的唯一锚点（本报告 T4 全部推导的起点）。一行文字 = 一个可反推的产品结构。|
|8|"DIAPER, LEG ELASTIC STRANDS, 152MM FRONT, 173.1MM REAR"|SLIDE 33（图像）|「纸尿裤，腿部橡筋丝，前段 152 mm，后段 173.1 mm」|173.1 的小数位证明这是设计计算值而非取整值。前/后分段尺寸是反推腿部弧线非对称性的直接依据（后段长 13.9%）。|
|9|"SURGE PICASSO EMBOSSING 74MM W × 197MM L"|SLIDE 34（图像）|「导流层（毕加索压花），宽 74 mm × 长 197 mm」|全材料唯一出现的压花工艺名称。与 S1 的素面 surge 构成两种导流策略的直接对比（大面积覆盖 vs 局部压花导流）。竞品分析中最具判别力的单行数据。|
|10|"OUTER COVER 295MM W [FIT LOOP 43MM W]"|SLIDE 34（图像）|「外覆层，宽 295 mm [贴合环 43 mm 宽]」|FIT LOOP 是 SS 平台独有的贴合结构，与 S1 的 OUTER COVER NO IFIT 形成有无对照。这是不可由尺码解释的定性结构分野，是判定平台代差的关键证据。|
|11|"PAD TO LINER ADHESIVE 125MM CD × 476MM MD"|SLIDE 34（图像）|「芯体对底膜胶，横向 125 mm × 纵向 476 mm」|CD 与 S1 完全相同（125 mm）、MD 长 109 mm —— 反推出「不改幅宽、只改节距」的产线兼容型升级路径。产线改造成本极低，是 KC 的快速迭代策略。|
|12|"EAR PROFILE 细部尺寸 68 / 30 / 56 / 75 / 115mm，20mm OVERLAP"|SLIDE 34（图像）|「耳贴轮廓细部尺寸 68 / 30 / 56 / 75 / 115 mm，搭接 20 mm」|Detail View 的功能实证：5 段局部轮廓尺寸 + 搭接量，全部承载于细部图。证明局部特征尺寸必须从 Detail View 读取，而非父视图。|
|13|"Title Block"（位于图纸右下角）|SLIDE 31 / SLIDE 31（图像）|「标题栏」（位于图纸右下角）|图框字段的位置判定式。右下角落款 + Kimberly-Clark Corporation（SLIDE 24（图像））= 标准 KC 图框布局。读图第一步：定位右下角。|
|14|"Created by: Q06027 on Wed May 27 00:49:14 CDT 2020；Last Issued by: Q06411 on Thu Apr 6 08:45:31 CDT 2023"|SLIDE 33（图像）|「创建者：Q06027，2020-05-27 00:49:14 CDT；最后发行者：Q06411，2023-04-06 08:45:31 CDT」|创建者与发行人不同 → 该图纸曾被修订。双时间戳可用于反推竞品平台的技术迭代节奏与维护活跃度（本例跨度 2.86 年）。工号制落款亦可用于组织架构情报。|
|15|"1 / 2 / 3"（图面气球标注编号）|SLIDE 34|「1 / 2 / 3」（图面上的件号标注）|Find number 的最简实证：图面阿拉伯编号 ↔ BOM 行的双射关系。这是把「图纸上的图形」翻译成「BOM 里的数据行」的唯一索引键，也是竞品拆解必须建立 find number 级粒度的根本原因。|

## 附录 A：本报告未解决的数据缺口清单（Open Data Gaps）

|||||
|---|---|---|---|
|1|C153-FPS-01592 的尺码未标注|⚠ T3/T4 全部差异无法区分「尺码效应」与「平台代差」|查 User Defined Title 字段；或实物对标|
|2|无任何公差数值|无法导出任何合格/不合格判据|需取 FPM 子图或检验规范|
|3|无涂布克重数据|用胶量估算依赖 [外部参数]|实物萃取称重实测|
|4|无橡筋根数与 dtex|橡筋成本估算有 ±3 倍不确定度|实物拆解计数 + 线密度实测|
|5|S1 的 EAR ADHESIVE 缺长度|耳胶面积 [数据不足]|取 C153-FPM-00155-B-01 子图|
|6|SS 的 EAR REINFORCEMENT ADH 三元组歧义|无法计算面积|取对应子图确认量纲|
|7|SS 平台无 find number|无法与 S1 逐行对齐|重读 p34 渲染图|
|8|score（压痕/撕开线）全材料零命中|无法判断 KC 是否使用 score 线|在 Detail View 中专项查找|
|9|Front view / Side view 全材料零命中|证实 KC 弃用三视图体系（已作结论，非缺口）|—|
|10|SS 平台无层级（FP1/FPM）信息|无法做架构对标|查该图的 BOM 表头|

## 附录 B：全报告推导算式索引（Audit Trail）

||||
|---|---|---|
|T1 / 概念 8|11 行 Qty 求和|11 行全部 = 1|
|T1 元数据|2023-04-06 − 2020-05-27|≈ 2.86 年|
|T4-A|125 × 367 / 125 × 476|45,875 / 59,500 mm²|
|T4-A|(476−367) ÷ 367|+29.7%|
|T4-A|367÷125 / 476÷125|2.94 / 3.81|
|T4-B|152+173.1 / 165+199，再 ×2|650.2 / 728.0 mm|
|T4-B|173.1÷152 / 199÷165|1.139 / 1.206|
|T4-B|45,173÷650.2 / 64,728÷728.0|69.5 / 88.9 mm（隐含包覆带宽）|
|T4-C|100×236 / 74×197|23,600 / 14,578 mm²|
|T4-C|23,600÷45,875 / 14,578÷59,500|51.4% / 24.5%|
|T4-C|100÷125 / 74÷125|80.0% / 59.2%|
|T4-C|236÷367 / 197÷476|64.3% / 41.4%|
|T4-D|(45,875+45,173) / (59,500+64,728)|91,048 / 124,228 mm²；比值 1.3645|
|模块5-2|各面积 × 8/12/16 与 18/25/35 g/m²|S1 1.180 / 1.680 / 2.315 g；SS 1.641 / 2.332 / 3.217 g|
|模块5-2|1.680 g × 1×10⁸ ÷ 1×10⁶|168.0 t / 亿片（同理 SS 233.2 t）|
|模块5-3|620 dtex ÷ 10,000|0.062 g/m|
|模块5-3|0.6502 × 0.062 / 0.7280 × 0.062|0.0403 / 0.0451 g/片|
|模块5-3|1.129 g（S1 腿胶 Base）÷ 0.0403 g（S1 橡筋）|≈ 28 : 1|
|模块5-4|45÷44 / 37÷58|1.02 / 0.64（护围/腰带比）|

报告结束 ｜ 全部数据来源于 /sandbox/workspace/Ebook_Extract/Product_Drawings_101_Sept2025/chapters/Product_Drawings_101_Sept2025_ch2_Reading_Drawings.md（含幻灯片文本层、演讲者备注、图像内容补充），并交叉引用 Ch1 / Ch3 / Ch4 章节文件用于模块 4 衔接分析。



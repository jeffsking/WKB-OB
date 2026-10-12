---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_1aa66129573ca3592c5c85a6e9f76a9b001a693ee6c0644e"
source_file: "Product_Drawings_101_Sept2025_ch1_Finding_Drawings_拆解报告.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch1_Finding_Drawings_拆解报告.md.md"
extracted: "2026-09-30"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
---

# Product_Drawings_101_Sept2025_ch1_Finding_Drawings_拆解报告.md




章节：Ch1 Finding Drawings ｜ 覆盖幻灯片：1–19 ｜ 文档：Product Drawings 101 (KC, Sept 2025) ｜ 拆解日期：2026-08-30

学术诚信声明：本报告全部观点均可回溯至 SLIDE N（幻灯片文本层 / 演讲者备注 / 「图像内容补充」）。凡在本章及本套材料（Ch1–Ch5、pptx_dump.json、逐页渲染读图记录）中检索不到原句支撑的，一律标注 [未找到原句]，不做补全、不做推测性数字填充。凡属本报告推断的内容，均显式标注 【推断】 并与原文证据分离呈现。

## 模块1：核心论点（Core Arguments）

### 论点 1：KC 的图纸获取是「两段式」——先在 The SPOT 拿到图号，再去 DRCS 拿到图纸本体

英文概括：Drawing retrieval at K-C is a two-stage pipeline: The SPOT yields the drawing number, DRCS yields the drawing file.

支撑依据：
- SLIDE 4–7：The SPOT 路径的终点是 "Scroll to the bottom to find a copy of the drawing and the drawing number"（SLIDE 7）——即 SPOT 的产出是图号，不是可编辑的工程图。
- SLIDE 8："Detailed product drawings are found in DRCS"——详细图纸本体在 DRCS。
- SLIDE 9–14：DRCS 侧提供 Checkout/Release、Download copy、View image、Print file、Where Used and BOM、back issues 六类文件级操作（SLIDE 9/10/11/12/13/14）。
- 交叉印证（非本章）：SLIDE 63（Ch4 Final thoughts）把这条分工压缩成两句原文——"Found on last page of specs from The SPOT" / "Full drawings in DRCS"。

为什么重要：这条分工决定了两个系统的数据模型不同——SPOT 存的是"规格文档（MS Word）+ 内嵌图纸快照 + 图号"，DRCS 存的是"图纸文件 + 版本 + BOM 关系"。理解这一点才能理解为什么后面需要两套检索语法。

### 论点 2：SPOT 检索的最后一环是「下载 Word 规格文档并翻到最后一页」，这是一个低技术、高确定性的兜底设计

英文概括：The SPOT retrieval path terminates in a manual, human-readable step: download the Word spec, scroll to the bottom (or Ctrl+F → "draw") to read the drawing number.

支撑依据：
- SLIDE 6：Click the 'Variant Property Spec' number to download a copy of the specification。
- SLIDE 7："Open the specification (MS Word document)" → "Scroll to the bottom to find a copy of the drawing and the drawing number" → "Or press 'cntrl + F' to open the search bar and type in 'draw' to jump down to the drawing number"。
- 图像内容补充 p6：检索结果界面列名为 Variant Property Spec（可点击下载）、Specification Description、Effective、Asset、Brand …

为什么重要：Ctrl+F 搜 "draw" 是一个工程惯例级的技巧——它不是系统功能，而是利用"图纸一定贴在规格文档末尾"这一文档模板约定。这说明 KC 的稳定性靠的是模板纪律而非系统智能。

### 论点 3：DRCS 的检索入口是「图号直查 + Advanced Search（PREFIX/TYPE 双筛选）」

英文概括：DRCS offers two discovery modes: direct drawing-number lookup, and Advanced Search where PREFIX and TYPE are the decisive filters.

支撑依据：
- SLIDE 9 图像补充：DRCS 主页导航为 News | Search | Create | Change Title | Issue | Approve，并直接提供图纸号输入框（示例值 C153-FPS-01575）——即"已知图号直查"是首页一等公民。
- SLIDE 15："The 'Advanced Search' will let you search for drawings based off the title of the drawing." / "Use the filters to help narrow your search." / "PREFIX and TYPE are the 2 filters I find most useful." / "Use the drill-down menu to help you select the appropriate filters."
- SLIDE 13–14：DRCS 同时是关系型工具——"Where Used and BOM information"、"Access back issues and drawing information"。

为什么重要：PREFIX（= 图纸类型码，如 FPS/FP1/FPM）× TYPE 的组合，本质上是用编码体系替代全文检索。这是全章最有迁移价值的一条。

### 论点 4：KC 图纸体系是一个三层 BOM 式层级：FPM（最小单元）→ FP1（组件）→ FPS（工厂用成品图）

英文概括：K-C drawing architecture is a three-tier product structure: FPM = smallest part/detail, FP1 = assembly of FPMs, FPS = finished product drawing as used in the mill.

支撑依据：
- SLIDE 17："SolidWorks product drawings are a combination of many smaller drawing combined." + 类型定义 "FPM – Part / Detail / Smallest possible unit"、"FP1 – Assembly / Groupings of FPM drawings that are often associated together / Ex. – Nonwoven + Adhesive"、"FPS – Finished Product Specification / Drawing as would be used in the mill"。
- SLIDE 18–19：层级示意图由 FPM → FP1 → FPS 逐级向上（图像内容补充 p17-19 确认）。
- SLIDE 16："Solidworks is LEGOs"——用"积木"比喻点明成品图由小图组合而成。

为什么重要：这意味着一张 FPS 不是一张"图"，而是一棵图纸树。任何零件级变更（FPM）都会沿 BOM 向上传播到所有父级 FPS——这是 Ch3 变更管理（cascaded parts）复杂度的根源。

### 论点 5：图纸的「来源工具」（AutoCAD / SolidWorks）是一等元数据，用颜色字母直接标注在图号旁

英文概括：Authoring tool is first-class metadata: a blue "A" marks AutoCAD, a red "S" marks SolidWorks.

支撑依据：
- SLIDE 16："K-C uses AutoCAD and SolidWorks to create our product drawings" / "AutoCAD is layers" / "Solidworks is LEGOs" / "A blue 'A' next to a drawing means it's an AutoCAD drawing." / "A red 'S' next to a drawing means it's a SolidWorks drawing."
- 图像内容补充 p16：蓝色 "A" = AutoCAD（比喻 layers 图层）；红色 "S" = SolidWorks（比喻 LEGOs 积木）。

为什么重要：CAD 来源决定了下游查看器与信息密度——SolidWorks 三维图纸靠 BOM / Where Used 才能读出细节（Ch2 SLIDE 34："SolidWorks drawings rely more on BOM / Where Used to highlight details."），而 AutoCAD 二维图直接可读。找图阶段先看 A/S，是为了预判读图方式。

## 模块2：关键概念操作化定义



覆盖 12 个概念。凡本章无原句的术语，统一在概念 8 与概念 12 中集中做诚信标注。

### 概念 1｜Engineering Drawing（工程图纸）

(a) 工程图纸 · Engineering Drawing

(b) 英文定义（原文口径）：本章未给出抽象定义，而是以功能定义——KC 的产品图纸（product drawings）是可在 The SPOT 中通过规格文档检索到图号、并在 DRCS 中取回详细文件的工程对象；成品图 "as would be used in the mill"（SLIDE 17）即在生产现场被直接使用的图纸。

(c) 操作化定义：
- 判定式：一个对象属于 KC 工程图纸 ⟺ ①拥有形如 C###-<TYPE>-##### 的图号；② 在 DRCS 中具备版本/发布记录（SLIDE 9 Checkout/Release、SLIDE 14 back issues）；③ 在 DRCS 中可被 Download / View / Print（SLIDE 10–12）。
- 量化指标：全公司图纸与文件管理服务已运行 30+ 年（"over 30 years"，SLIDE 9 图像补充）；单张图纸创建/修订工时经验值 8 小时/张（Ch3 SLIDE 45，非本章）。

(d) 原文英文摘录：
> "Detailed product drawings are found in DRCS" — SLIDE 8
> "FPS – Finished Product Specification / Drawing as would be used in the mill" — SLIDE 17
> "Providing Drawing and File Management Services to the K-C community for over 30 years." — SLIDE 9 图像补充

### 概念 2｜Drawing Number（图号）——含逐段解析表 ⭐

(a) 图号 · Drawing Number

(b) 英文定义：本章未给出图号的正式编码规则定义 [未找到原句]。本章可确认的图号实例为 C153-FPS-01575（SLIDE 9 图像补充：DRCS 主页图纸号输入框示例值）；完整五段式实例 C153-FPS-01575-J-09 出现在本套材料的 Ch2 图像内容补充（p13 DRCS Where Used 页）。

(c) 操作化定义（完整逐段解析表见 模块3 / T4，此处给摘要）：
- 语法判定式：^[A-Z]\d{3}-[A-Z0-9]{3}-\d{5}(-[A-Z0-9]-\d{2})?$
- 段1（平台族）：C153 —— 同一产品平台共享，取值集合在样本中见 C153（纸尿裤/BCM 平台）与 C192（Ch2 图像补充，训练裤平台）。
- 段2（类型码）：FPS —— 必须与 SLIDE 17–19 的类型清单枚举匹配。
- 段3（流水号）：01575 —— 5 位，同平台内按变体/尺码分配，同系列多尺码呈连续号段（01574 / 01575 / 01576 / 01577，见 Ch3 图像补充）。
- 段4–5（-J-09）：官方定义 [未找到原句]；仅能给出观测值域与推断，见 T4。

(d) 原文英文摘录：
> 图纸号输入框示例值：C153-FPS-01575 — SLIDE 9 图像补充
> "Scroll to the bottom to find a copy of the drawing and the drawing number" — SLIDE 7
> "PREFIX and TYPE are the 2 filters I find most useful." — SLIDE 15



⚠️ 诚信提示：图号第 4、5 段（-J-09）的含义在本套材料中无任何原文定义。本报告在 T4 中给出的解释均为 【推断】，并同时列出竞争的备择假设，请读者按"未证实"处理。

### 概念 3｜Part / Part-Detail（零件 / 最小图元）

(a) 零件（最小图元）· Part / Detail

(b) 英文定义："FPM – Part / Detail / Smallest possible unit"（SLIDE 17）。即图纸层级中不可再分的最小单位。

(c) 操作化定义：
- 判定式：某图纸是 Part 级 ⟺ 其类型码为 FPM，且位于 BOM 树的叶子节点（在 Where Used / BOM 视图中无 CHILDREN）。
- 量化实例（Ch2 图像补充 BOM_A，C153-FPS-01575-J-09 的 11 行子件中 FPM 级共 4 行）：
  - C153-FPM-00154-B-01 PAD TO LINER, ADHESIVE, 125MM CD × 367MM MD
  - C153-FPM-00155-B-01 EAR ADHESIVE, 202 outside W × 182 inside W
  - C153-FPM-00156-B-02 LEG ELASTIC ADHESIVE, 199MM CD × 227MM MD
  - C153-FPM-00157-D-01 LEG ELASTIC STRANDS, 152MM front / 173.1MM rear
- 操作含义：Part 级图纸承载的是尺寸化工艺参数（胶的涂布幅宽 CD/MD、橡筋长度），这是研发知识的真正落点。

(d) 原文英文摘录：
> "FPM – Part / Detail / Smallest possible unit" — SLIDE 17
> "FPM – Part / Smallest possible unit" — SLIDE 18
> "Where Used and BOM information" — SLIDE 13

### 概念 4｜Assembly（组件）

(a) 组件 · Assembly

(b) 英文定义："FP1 – Assembly / Groupings of FPM drawings that are often associated together / Ex. – Nonwoven + Adhesive"（SLIDE 17）。

(c) 操作化定义：
- 判定式：某图纸是 Assembly 级 ⟺ 类型码为 FP1（或 FP2，见下文诚信提示）且在 BOM 中同时拥有 PARENT（至少一个 FPS/PDD）与 CHILDREN（至少一个 FPM）。
- 量化实例（BOM_A，FP1 级共 7 行）：C153-FP1-00031-B-01（EAR，数量 2）、00034-D-02（PAD, DISCRETE）、00035-J-03（OUTER COVER NO IFIT）、00037-D-02（WAISTBAND 44MM WIDTH）、00052-J-02（INNER COVER EYESPOT 198MM BACK END 90MM）、00054-D-04（FLAP 45MM HEIGHT）、00178-D-04（SMALL SURGE 100MM W, 236MM L）。
- 结构含义：Assembly 的语义是"经常一起出现"（often associated together），其经典组合 Nonwoven + Adhesive 揭示 KC 把"基材 + 胶"视为一个物料单元而非两个——这是卫材结构设计的通用范式。

(d) 原文英文摘录：
> "FP1 – Assembly / Groupings of FPM drawings that are often associated together / Ex. – Nonwoven + Adhesive" — SLIDE 17

### 概念 5｜Finished Product / Full Product（成品图）

(a) 成品图 · Finished Product Specification / Full Product

(b) 英文定义："FPS – Finished Product Specification / Drawing as would be used in the mill"（SLIDE 17）；"FPS – Full Product / Drawing as would be used in the mill"（SLIDE 18）。

(c) 操作化定义：
- 判定式：某图纸是成品级 ⟺ 类型码为 FPS 且在 Where Used 视图中位于 BOM 顶端（All Children 非空、作为 root）。
- 命名口径差异（重要）：SLIDE 17 写 Finished Product Specification，SLIDE 18/19 写 Full Product——同一缩写 FPS 在原文中有两种展开写法，检索与文档撰写时须同时接受两个词形。
- 量化实例：C153-FPS-01575-J-09 — Title: DIAPER；User Defined Title: BCM, SPDV, TOTAL, S1（Ch2 图像补充 DRCS File Information）。即同一平台一张 FPS 对应一个尺码/变体，S1（Size 1）。

(d) 原文英文摘录：
> "FPS – Finished Product Specification / Drawing as would be used in the mill" — SLIDE 17
> "FPS – Full Product / Drawing as would be used in the mill" — SLIDE 18

### 概念 6｜图纸类型前缀体系 FPM / FP1 / FP2 / FPS

(a) 图纸类型前缀 · Drawing Type Prefix（FPM / FP1 / FP2 / FPS）

(b) 英文定义：见 SLIDE 17–19 类型表（FPM = Part/Detail；FP1 = Assembly；FPS = Finished/Full Product）。关于 FP2：本章（SLIDE 1–19）未出现 FP2 【未找到原句】；FP2 仅出现在本套材料其他章节（Ch3 SLIDE 45 审批矩阵 "FP1 / FP2 (Sub-Assembly)"；Ch5 SLIDE 68 "Feminine Care does not have the option for FPM,FP1,FP2 drawing access"），口径为 Sub-Assembly（子组件），与 FP1 同级、同为 Assembly 层。

(c) 操作化定义：
- 判定式（层级）：Level(FPM) < Level(FP1) ≈ Level(FP2) < Level(FPS)。
- DRCS 检索式：在 Advanced Search 中以 PREFIX = FPM / FP1 / FP2 / FPS 直接切层级（SLIDE 15）。
- 权限式（Ch5 SLIDE 67，非本章）：FPM 与 FP1 的审批权归 Product Developer；FPS 的审批权归 Quality（Rex Stuart），Product Developer 仅为 Checker。

(d) 原文英文摘录：
> "Drawing Types / FPM – Part / Detail / FP1 – Assembly / FPS – Finished Product Specification" — SLIDE 17
> "FPM / FP1 / FPS" 层级示意图 — SLIDE 18、SLIDE 19
> "PREFIX and TYPE are the 2 filters I find most useful." — SLIDE 15

### 概念 7｜其他图纸前缀：PDD / LPA / PSD / DOC

(a) 其他图纸前缀 · Other Drawing Prefixes

(b) 英文定义（全部出自 SLIDE 17 演讲者备注，非幻灯片正文）：
- PDD = Product Development Drawing（产品开发图）
- LPA = Layout Pattern Drawing（排版/花型排列图）
- PSD = Process Schematic Drawing（工艺示意图）
- DOC = Miscellaneous Documentation（杂项文件）

(c) 操作化定义：
- 判定式：这些前缀与 FPM/FP1/FPS 并列，同属 DRCS PREFIX 筛选器的枚举域（依据 SLIDE 15 的 PREFIX 筛选器 + SLIDE 17 的类型清单）。
- 语义分工推断 【推断】：PDD 与 FPS 在变更流程中处于同一层级（Ch3 图像补充 Redline 模板表头列名为 "FPS or PDD Drawing Impacted"，即二者同为顶层受影响图），故推断 PDD 是量产前/开发中版本的顶层图，FPS 是量产版顶层图。此推断无本章原句直接支撑，依据为 Ch3 模板表头。
- LPA/PSD 的用途 【未找到原句】：本章仅给出名称展开，未说明适用范围与审批人。

(d) 原文英文摘录：
> "LPA = Layout Pattern Drawing / PSD = Process Schematic Drawing / PDD = Product Development Drawing / DOC = Miscellaneous Documentation" — SLIDE 17 SPEAKER NOTES

### 概念 8｜前缀 SPN / FRM / FLD ⚠️ 诚信标注

(a) SPN / FRM / FLD

(b) 英文定义：[未找到原句] —— 在 Ch1 文本层、Ch1 演讲者备注、Ch1 图像内容补充、以及本工作区全部材料（pptx_dump.json、Ch2–Ch5、KC_CapabilityDays2025_三份PPT深度拆解.md、逐页渲染读图记录）中均未检索到 SPN、FRM、FLD 三个前缀及其展开含义。

(c) 操作化定义：无法给出。为避免编造，本报告不对其含义作任何推测。

(d) 原文英文摘录：无。仅可确认 SLIDE 17 备注列出的"其他前缀"为 4 个（LPA / PSD / PDD / DOC），不含 SPN / FRM / FLD。



建议：若需补全这三个前缀，须回到原始 PPTX 的图像层（SLIDE 17 仅 1 张图，本章文本层未覆盖该图上的完整前缀表）或 KC 内部 DRCS 文档重新取证。

### 概念 9｜The SPOT

(a) The SPOT（规格与图号索引系统）

(b) 英文定义：
- 本章原句口径："Product drawings can be found in The SPOT"（SLIDE 4/5/6/7 重复出现，共 4 次）。本章对 The SPOT 的定义止于此句——它是一个"能找到产品图纸"的入口。
- 用户提供的背景定义（本章未证实）："The SPOT = system for part、whose sole purpose is tracking drawings"。[未找到原句] —— 在本套材料中检索 "system for part"、"sole purpose"、"tracking drawings" 均无命中。该定义可能来自 KC 其他内部材料或口头传承，本报告中按未证实背景信息处理，不作为分析前提。

(c) 操作化定义（本章可证实的全部事实）：
- 入口路径：The SPOT 主页 → Variant / Semi-Finished Team（SLIDE 4 图像补充红框） → Quick Links 区 SPOT Specifications（SLIDE 5 图像补充红框） → Variant Specification Search。
- 检索界面："Variant and Property Specification # Search"，结果列表列含 Variant Property Spec（可点击，下载）、Specification Description、Effective、Asset、Brand（SLIDE 6 图像补充）。
- 产出物：一份 MS Word 规格文档，图纸与图号位于文档末尾（SLIDE 7）。
- 定位技巧：Ctrl + F → 输入 "draw" → 直接跳到图号处（SLIDE 7）。
- 字段维度（用户指定项）：Product Development / Business Unit / eMARS number / BAPI / Business Warehouse Reporting —— 全部 [未找到原句]，见概念 12。

(d) 原文英文摘录：
> "Visit The SPOT / Select the 'Variant Specification Search'" — SLIDE 4
> "Select the 'SPOT Specifications'" — SLIDE 5
> "Use the filters to navigate to the product/variant you are looking for / Click the 'Variant Property Spec' number to download a copy of the specification" — SLIDE 6
> "Found on last page of specs from The SPOT" — SLIDE 63（Ch4 总结页，交叉印证）

### 概念 10｜DRCS（Documentum Records & Content Services / Drawing Release Control System）

(a) 图纸发布控制系统 · DRCS

(b) 英文定义："DRCS – Drawing Release Control System"（SLIDE 8）。
关于 Documentum Records & Content Services 这一展开：本章 [未找到原句] —— SLIDE 8 仅给出 "Drawing Release Control System" 一种展开；本套材料任何位置均未出现 "Documentum" 字样。因此本报告采用本章原文展开，并将 Documentum 展开标注为未证实。

(c) 操作化定义：
- 入口：Central CAD Homepage → 左侧 Applications 面板 → DRCS - Drawing Release Control System（SLIDE 8、图像补充 p8）。同面板另有 ECN (Engineering Change Notice)、BOM Report & Configuration（图像补充 p8）。
- 组织归属：Central CAD 页面标题为 "Drawing and File Management for Kimberly-Clark"，所属路径 Engineering & Research / Central CAD（图像补充 p8）；DRCS Owner: Bill Bacon（图像补充 p9）。
- 主导航：News | Search | Create | Change Title | Issue | Approve（图像补充 p9）。
- 六大能力（SLIDE 9–14，逐一对应）：Checkout/Release file、Download copy、View image、Print file、Where Used and BOM information、Access back issues and drawing information。
- 服务年限指标：服务 K-C 社区 超过 30 年（图像补充 p9）。

(d) 原文英文摘录：
> "Detailed product drawings are found in DRCS / You can find DRCS by navigating to the Central CAD Homepage and clicking 'DRCS – Drawing Release Control System'" — SLIDE 8
> "Where Used and BOM information" — SLIDE 13
> "The advanced search feature can help find product drawings in DRCS" — SLIDE 15

### 概念 11｜Product Development / Product Developer（产品开发职能）

(a) 产品开发（职能/角色）· Product Development

(b) 英文定义：本章未对 Product Development 作职能定义 [未找到原句]。本章仅出现其派生术语 PDD = Product Development Drawing（SLIDE 17 备注）。Product Developer 作为角色的定义出现在其他章节：Ch3 SLIDE 45 "Product developers or 'submitters' of SolidWorks drawing changes are the approvers for FPM and FP1 drawings."

(c) 操作化定义（跨章整合，均标注来源）：
- FPM / FP1 层：Checker = Product Developer；Approver = Product Developer（Ch3 SLIDE 45）。
- FPS 层：Checker = Product Developer & Senior Product Developer；Approver = Senior Quality Engineer（Ch3 SLIDE 45 表）；且 "Rex Stuart is the only one who can approve a completed FPS drawing."（Ch3 SLIDE 45）。
- 新流程变化（Ch5 SLIDE 67）："For the new SolidWorks product drawings product developers will be the approvers of diaper part 'FPM' and sub-assemblies 'FP1' within DRCS."；"For final FPS drawings product developers will remain a checker. Rex Stuart of Quality remains the Approver for FPS drawings supporting production."
- 业务单元差异（Ch5 SLIDE 68）："These steps are the same for Adult, Child, and Infant Care. Feminine Care does not have the option for FPM,FP1,FP2 drawing access."

(d) 原文英文摘录：
> "PDD = Product Development Drawing" — SLIDE 17 SPEAKER NOTES
> "FPS (Final Drawing) | Product Developer & Senior Product Developer | Senior Quality Engineer" — Ch3 SLIDE 45
> "Rex Stuart is the only one who can approve a completed FPS drawing." — Ch3 SLIDE 45

### 概念 12｜eMARS / BAPI / Business Warehouse Reporting / Business Unit ⚠️ 诚信标注

(a) eMARS 号 / BAPI / Business Warehouse Reporting（BW 报表）/ Business Unit（业务单元）

(b) 英文定义：[未找到原句] —— 四个术语在 Ch1 全量文本、Ch1–Ch5 全部章节、pptx_dump.json、以及本工作区全部拆解笔记中均无命中（检索式：eMARS|BAPI|Business Warehouse|Business Unit，仅命中 PDD = Product Development Drawing，与上述四者无关）。

(c) 操作化定义：无法给出。本报告不对其字段含义、取值范围、在 SPOT 界面中的位置作任何描述。

(d) 原文英文摘录：无。

关于 SPOT 字段的诚实替代方案：本章能证实的 SPOT 检索维度只有 3 类——
1. 导航/入口维度：Variant / Semi-Finished Team（SLIDE 4 图像补充）；
2. 结果列维度：Variant Property Spec、Specification Description、Effective、Asset、Brand（SLIDE 6 图像补充，"…" 表示渲染读图记录的列名清单未穷举，可能还有更多列）；
3. 泛指筛选维度：SLIDE 6 "Use the filters to navigate to the product/variant you are looking for" —— 原文只说 filters，未枚举 filter 名称。



取证建议：若确需 SPOT 的 Product Development / Business Unit / eMARS / BAPI / BW 字段表，需对 SLIDE 6 的渲染图做高分辨率重读（该页仅 1 张图，当前列名记录以 "…" 结尾，存在未读全的可能），或调取 KC 内部 SPOT 用户手册。

## 模块3：证据链（Evidence Chain）

### T1｜图纸类型全表（前缀 / 名称 / 适用范围 / 批准人 / 备注）

|||||||||
|---|---|---|---|---|---|---|---|
|FPM|Part / Detail|零件 / 最小图元|"Smallest possible unit"；BOM 叶子节点。实例：ADHESIVE 涂布范围、ELASTIC STRANDS 长度|Product Developer|Product Developer|承载 CD/MD 涂布尺寸等工艺参数|定义 SLIDE 17/18/19；审批 Ch3 SLIDE 45|
|FP1|Assembly|组件|"Groupings of FPM drawings that are often associated together / Ex. – Nonwoven + Adhesive"|Product Developer|Product Developer|BOM 中层；典型组合=基材+胶|定义 SLIDE 17；审批 Ch3 SLIDE 45|
|FP2|Sub-Assembly|子组件|与 FP1 同层（本章 [未找到原句]）|Product Developer|Product Developer|本章未出现；Feminine Care 无 FPM/FP1/FP2 权限|Ch3 SLIDE 45；Ch5 SLIDE 68|
|FPS|Finished Product Specification / Full Product|成品图|"Drawing as would be used in the mill"；BOM 根节点，一图对应一个尺码/变体|Product Developer & Senior Product Developer|Senior Quality Engineer（实操中 Rex Stuart 是唯一可批准 FPS 的人）|名称在 SLIDE 17 为 *Finished*、SLIDE 18/19 为 *Full*，两写法并存|定义 SLIDE 17/18/19；审批 Ch3 SLIDE 45、Ch5 SLIDE 67|
|PDD|Product Development Drawing|产品开发图|开发中/量产前的顶层图 【推断】|[未找到原句]|[未找到原句]|在 Redline 模板中与 FPS 同列（"FPS or PDD Drawing Impacted"），推断为同层|名称 SLIDE 17 备注；层级推断 Ch3 图像补充|
|LPA|Layout Pattern Drawing|排版/花型图|[未找到原句]|[未找到原句]|[未找到原句]|仅名称出现在演讲者备注|SLIDE 17 SPEAKER NOTES|
|PSD|Process Schematic Drawing|工艺示意图|[未找到原句]|[未找到原句]|[未找到原句]|仅名称出现在演讲者备注|SLIDE 17 SPEAKER NOTES|
|DOC|Miscellaneous Documentation|杂项文件|"Miscellaneous Documentation"|[未找到原句]|[未找到原句]|非图纸类文档|SLIDE 17 SPEAKER NOTES|
|SPN / FRM / FLD|—|—|[未找到原句]|[未找到原句]|[未找到原句]|本套材料中完全无此三前缀|—|
|FFS / PT1|—|—|[未找到原句]（观测值）|—|—|观测到 C192-FFS-1544、C192-PT1-1344（Ch2 图像补充）；4 位流水号、非 C153 系列，疑为不同平台/早期编号体系|Ch2 图像补充 p24-25|


关键数字：本章证实的前缀共 7 个（FPM / FP1 / FPS / PDD / LPA / PSD / DOC），其中幻灯片正文仅定义 3 个（FPM / FP1 / FPS），其余 4 个仅在 SLIDE 17 演讲者备注中给出名称展开。

### T2｜The SPOT 系统字段表（检索所需信息维度）



⚠️ 本表严格区分「原文可证实的字段」与「用户指定但原文缺失的字段」，后者全部标注 [未找到原句]，不作填补。

|||||||
|---|---|---|---|---|---|
|1|Variant Property Spec（变体属性规格号）|Variant Property Spec|✅ 可点击下载规格文档副本|强（正文）|SLIDE 6 + 图像补充 p6|
|2|Specification Description（规格描述）|Specification Description|结果列（只读）|强（图像层）|图像补充 p6|
|3|Effective（生效日期）|Effective|结果列（只读）|强（图像层）|图像补充 p6|
|4|Asset（资产）|Asset|结果列（只读）|强（图像层）|图像补充 p6|
|5|Brand（品牌）|Brand|结果列（只读）|强（图像层）|图像补充 p6|
|6|其余结果列（未穷举）|…|只读|弱（渲染读图记录以省略号结尾）|图像补充 p6|
|7|Filters（筛选器，未枚举）|"Use the filters to navigate to the product/variant you are looking for"|可操作|弱（原文只说 filters，未列名）|SLIDE 6|
|8|Product / Variant 导航目标|"navigate to the product/variant you are looking for"|概念维度|中|SLIDE 6|
|9|入口卡片：Variant / Semi-Finished Team|Variant / Semi-Finished Team|可点击|强（图像层红框）|图像补充 p4|
|10|Quick Links：SPOT Specifications|SPOT Specifications|可点击图标按钮|强（图像层红框）|图像补充 p5|
|11|检索界面标题：Variant and Property Specification # Search|Variant and Property Specification # Search|页面标题|强（图像层）|图像补充 p6|
|12|文档内定位键：draw（Ctrl+F 关键词）|"type in 'draw' to jump down to the drawing number"|Word 内查找|强（正文）|SLIDE 7|
|—|Product Development|—|—|[未找到原句]|全库检索无命中|
|—|Business Unit|—|—|[未找到原句]|全库检索无命中|
|—|eMARS number|—|—|[未找到原句]|全库检索无命中|
|—|BAPI|—|—|[未找到原句]|全库检索无命中|
|—|Business Warehouse Reporting|—|—|[未找到原句]|全库检索无命中|


结论：The SPOT 在本章可证实的检索维度是 "Variant / Semi-Finished" 语义轴 + 结果列表的 5 个已知列 + 未枚举的 filters，而非用户所列的企业系统字段组。两者不可混为一谈。

### T3｜The SPOT / DRCS 界面操作路径表（逐页）

Part A — The SPOT 路径（SLIDE 4 → 7，共 4 步 7 个动作）

|||||||
|---|---|---|---|---|---|
|0|SLIDE 4|The SPOT 主页|"Visit The SPOT"|导航栏 THE SPOT；红框指向 "Variant / Semi-Finished Team" 卡片|进入 SPOT|
|1|SLIDE 4|SPOT 主页|"Select the 'Variant Specification Search'"|—|进入变体规格检索|
|2|SLIDE 5|Quick Links 区|"Select the 'SPOT Specifications'"|红框指向 "SPOT Specifications" 图标按钮|进入规格库|
|3|SLIDE 6|"Variant and Property Specification # Search"|"Use the filters to navigate to the product/variant you are looking for"|列名：Variant Property Spec / Specification Description / Effective / Asset / Brand …|命中目标行|
|4|SLIDE 6|结果行|"Click the 'Variant Property Spec' number to download a copy of the specification"|Variant Property Spec 列为红框（可点击下载）|下载 Word 规格|
|5|SLIDE 7|MS Word 文档|"Open the specification (MS Word document)"|—|打开文档|
|6a|SLIDE 7|Word 文档末尾|"Scroll to the bottom to find a copy of the drawing and the drawing number"|—|获得图号|
|6b|SLIDE 7|Word 查找栏|"Or press 'cntrl + F' to open the search bar and type in 'draw' to jump down to the drawing number"|—|获得图号（快捷路径）|


Part B — DRCS 路径（SLIDE 8 → 15）

|||||||
|---|---|---|---|---|
|SLIDE 8|入口|"Detailed product drawings are found in DRCS / You can find DRCS by navigating to the Central CAD Homepage and clicking 'DRCS – Drawing Release Control System' or by using this link: DRCS (kcc.com)"|Central CAD 页："Engineering & Research / Central CAD / Drawing and File Management for Kimberly-Clark"；左侧 Applications 面板红框 DRCS（同列另有 ECN (Engineering Change Notice)、BOM Report & Configuration）|进入 DRCS|
|SLIDE 9|主页 / 签出发布|"Checkout/Release file"|主导航 News | Search | Create | Change Title | Issue | Approve；图纸号输入框示例 C153-FPS-01575；欢迎语 "over 30 years"；Owner Bill Bacon|图号直查 + 签出/发布|
|SLIDE 10|下载|"Download copy"|4 张图|取图纸副本|
|SLIDE 11|查看|"View image"|3 张图|在线预览|
|SLIDE 12|打印|"Print file"|3 张图|出图|
|SLIDE 13|关系查询|"Where Used and BOM information"|3 张图|反查父件 / BOM 子件|
|SLIDE 14|历史版本|"Access back issues and drawing information"|3 张图|历史版本与图档信息|
|SLIDE 15|高级检索|"The 'Advanced Search' will let you search for drawings based off the title of the drawing. / Use the filters to help narrow your search. / PREFIX and TYPE are the 2 filters I find most useful. / Use the drill-down menu to help you select the appropriate filters."|图上标注 1、2 两个序号|无图号时的检索|


关键数字：DRCS 在本章展示的能力共 6 项（Checkout/Release、Download、View、Print、Where Used & BOM、Back issues）+ 1 项检索增强（Advanced Search，含 2 个推荐筛选器 PREFIX / TYPE）。SPOT 路径共 4 页 / 7 个动作，终点是图号；DRCS 路径共 8 页 / 7 项能力，起点是图号。两段式衔接点正是「图号」这一个字段。

### T4｜图号结构逐段解析表 ⭐（本章最高迁移价值内容）

基准实例：C153-FPS-01575-J-09
- C153-FPS-01575 —— SLIDE 9 图像补充（DRCS 主页图纸号输入框示例值）✅ 本章原文
- C153-FPS-01575-J-09 —— Ch2 图像补充 p13（DRCS Where Used 页，Title: DIAPER / User Defined Title: BCM, SPDV, TOTAL, S1）⚠️ 非本章，但同套材料

|||||||||
|---|---|---|---|---|---|---|
|1|首段（第 1 个 - 前）|C153|产品平台/产品族前缀（Platform / Product Family）。C153 系列在本套材料中全部为 DIAPER / BCM 平台|SLIDE 9 图像补充；Ch2 图像补充（BOM_A 全部 11 行均为 C153-）；Ch3 图像补充（ER# 900200005649 中 5 张 FPS + 1 张 FP1 + 1 张 FPM 全部 C153-）|取首个 - 前子串；同平台内所有 FPM/FP1/FPS 必须取同一值；正则 [A-Z]\d{3}|🟢 强（实测 17+ 个样本全部一致）|
|2|第 1、2 个 - 之间|FPS|图纸类型码（Drawing Type Code），与 SLIDE 17–19 的类型清单枚举匹配|SLIDE 17 / SLIDE 18 / SLIDE 19；SLIDE 15（PREFIX 筛选器）|与枚举集 {FPM, FP1, FP2, FPS, PDD, LPA, PSD, DOC} 精确匹配；不匹配则记为"未登记前缀"（如观测到的 FFS、PT1）|🟢 强|
|3|第 2、3 个 - 之间|01575|流水号（Sequence Number），5 位定长，同平台内按变体/尺码逐个分配|SLIDE 9 图像补充；Ch3 图像补充（同一次变更影响 5 张 FPS：01640 / 01641 / 01577 / 01574 / 01575，号段连续）|正则 \d{5}；同平台内全局唯一；同系列多尺码呈连续号段|🟡 中（"连续号段"为观测规律，无官方规则原文）|
|4|第 3、4 个 - 之间|J|修订标识（Revision）【推断】|[未找到原句] —— 无任何原文定义|观测值域：{B, D, J}（来自 Ch2 BOM_A 11 行：-B-01×3、-D-0*×6、-J-0*×2）。因不连续（跳 C/E/F…），推断为修订级别字母而非序号|🔴 弱（纯推断）|
|5|末段|09|分页 / 子序号（Sheet / Issue Number）【推断】|[未找到原句] —— 无任何原文定义|观测值域：{01, 02, 03, 04, 09, 10}。与段 4 存在配对倾向（B→01、D→02/03/04、J→02/03/09），推断为该修订版本下的分页号或子件序号|🔴 弱（纯推断）|


#### T4-附：段 4 / 段 5 的竞争假设（均未证实，供后续取证）

||||||
|---|---|---|---|
|H1：修订字母 + 分页号|J = 第 10 次修订；09 = 第 9 页|成品图由多视图组成（Ch2：Overhead View / Cross Section / Detail Views / BOM / Notes / Title Block），多页合理；字母与数字可各自递增|段 4 与段 5 成对跳变（J 只配 02/03/09，B 只配 01），若彼此独立应出现 J-01、B-05 等——样本中未见|
|H2：修订字母 + 变体/尺码序号|09 = 该修订下的第 9 个变体|一张 FPS 对应一个尺码（User Defined Title 含 S1）；同平台 5 张 FPS 连号说明变体多|若 09 = 尺码序号，则与段 3 的流水号功能重复，且样本中 FP1/FPM 级也有 -D-04 这类大数（零件级通常无 4 个变体）|
|H3：检验/发布批次 + 图纸内序号|J = Checker/发布批次代码；09 = 该批次内序号|与 SLIDE 14 "Access back issues" 的版本批次语义相近|无任何原文把字母与 Checker 关联|


⚠️ 异常观测值（存疑，不作结论）：Ch2 图像补充中出现 C153-FPS-01592-1-10 —— 段 4 为数字 1 而非字母。可能原因：①原文即为数字（则 H1 的"字母=修订"假设被削弱）；②字体/OCR 把 I 或 J 读作 1。无法在现有材料中定论，标记为待取证。

#### T4-B：图号结构的工程价值小结

|||||
|---|---|---|
|平台与类型分离|C153（平台）× FPS（类型）独立成段|用 PREFIX 一个筛选器即可切出"某平台的全部成品图"（SLIDE 15）|
|层级由编码承载|FPM < FP1/FP2 < FPS 直接写在图号里|无需打开图纸即可判断层级，编码即索引|
|同平台号段连续|5 张 FPS 连号（01574–01577、01640–01641）|同系列变体可批量发现，一次变更能列出全部受影响图号|
|修订可辨|段 4/5 区分版本|支持 SLIDE 14 的 "back issues" 历史追溯|


## 模块4：章节间衔接（Chapter Connections）

### 4.1 衔接一：Ch1（Finding Drawings）→ Ch2（Reading Drawings）

衔接逻辑：Ch1 的终点是「拿到图号 + 拿到图纸文件」，Ch2 的起点是「打开图纸后读什么」。两者通过 DRCS 的 Where Used / BOM 与 CAD 来源（A/S） 两个接口耦合。

||||||
|---|---|---|---|
|核心问题|Where is the drawing?|What does the drawing say?|先定位、后解读|
|产出物|图号（C153-FPS-01575-J-09 形态）+ 图纸文件|尺寸、材料、BOM 明细|图号是 Ch2 展开 BOM 的主键|
|关键界面|The SPOT（规格 Word）、DRCS（Search / Advanced Search）|图纸本体（Overhead View / Cross Section / Detail Views / BOM / Notes / Title Block）|—|
|BOM 角色|SLIDE 13 把 BOM 作为检索能力："Where Used and BOM information"|Ch2 SLIDE 34 把 BOM 作为读图手段："SolidWorks drawings rely more on BOM / Where Used to highlight details."|同一功能，两种用途——找图时是导航，读图时是数据源|
|CAD 来源的作用|SLIDE 16：蓝色 A = AutoCAD，红色 S = SolidWorks|A（二维、layers）直接可读；S（三维、LEGOs）需借 BOM/Where Used 才能读出细节|Ch1 判 A/S → 决定 Ch2 用哪种读法|
|关键数据|图号 C153-FPS-01575；DRCS 服务 30+ 年|BOM_A 11 行子件（7 个 FP1 + 4 个 FPM）；SURGE 100MM W × 236MM L；LEG ELASTIC 152MM front / 173.1MM rear|Ch1 找到的 FPS → Ch2 拆出 11 行结构数据|


对读图的三条预判（基于 Ch1）：
1. 若图号旁是蓝色 A（AutoCAD / layers）→ 尺寸标注直接可读，优先看图层化的尺寸注记。
2. 若图号旁是红色 S（SolidWorks / LEGOs）→ 单张图信息不完整，必须打开 Where Used / BOM 才能看到零件级尺寸。
3. 若目标是材料/结构参数（如 SURGE 尺寸、LEG ELASTIC 长度、ADHESIVE 涂布范围）→ 顶层 FPS 只是索引，真正数据在 FPM 级子图（如 C153-FPM-00156-B-02 LEG ELASTIC ADHESIVE 199MM CD × 227MM MD）。

### 4.2 衔接二：Ch1（The SPOT）→ Ch5（DRCS Access）

衔接逻辑：Ch1 讲两个系统怎么配合找图；Ch5 讲谁有资格进 DRCS、进到哪一层。Ch5 把 Ch1 隐含的"图纸是受控资产"显性化为权限矩阵。

||||||
|---|---|---|---|
|职能|定位图号：规格文档中内嵌图纸副本|管理图纸文件：版本、发布、BOM、历史|索引 vs 存储分离|
|原文定位句|"Product drawings can be found in The SPOT"（SLIDE 4/5/6/7，共 4 次）|"Detailed product drawings are found in DRCS"（SLIDE 8）|关键词是 Detailed——SPOT 只有"图"，DRCS 才有"详细图"|
|总结页口径|"Found on last page of specs from The SPOT"（SLIDE 63）|"Full drawings in DRCS"（SLIDE 63）|一句对偶，定义清晰|
|文档形态|MS Word 规格文档（SLIDE 7）|图纸文件 + 版本记录（SLIDE 9–14）|Word 是只读快照，DRCS 是可签出/可改|
|检索方式|导航 + filters + 点 Variant Property Spec 下载（SLIDE 4–6）；Word 内 Ctrl+F 搜 "draw"（SLIDE 7）|图号直查（输入框示例 C153-FPS-01575，SLIDE 9 图像补充）+ Advanced Search（PREFIX / TYPE，SLIDE 15）|SPOT 靠文档模板约定，DRCS 靠编码筛选器|
|粒度|Variant / Semi-Finished（业务视角）|Drawing / BOM / Revision（工程视角）|两套元数据模型|
|权限（Ch5）|[未找到原句] —— Ch5 未涉及 SPOT 权限|View / Work / Approve 三级（Ch5 SLIDE 73）；按 Work Role, Business Sector, Reporting Work Location 授予（Ch5 图像补充 Step 2）；FPM/FP1/FP2 权限 Feminine Care 不开放（Ch5 SLIDE 68）|权限粒度落在存储系统上，索引系统相对开放|
|审批（Ch5 SLIDE 67）|—|FPM/FP1 → Product Developer 批准；FPS → Product Developer 为 Checker，Rex Stuart（Quality）为 Approver|越靠近生产，审批权越上收|
|服务/归属|—|Owner Bill Bacon；服务 K-C 超 30 年（SLIDE 9 图像补充）；归口 Engineering & Research / Central CAD|—|


架构启示（一句话）：SPOT 回答"哪个图号属于哪个产品"，DRCS 回答"这个图号的哪个版本是有效的、由谁批准、包含在哪些父件里"——前者是业务索引，后者是工程真相源（single source of truth）。

## 模块5：业务连接点（Business Connections）



业务背景：卫材（纸尿裤 / 湿巾）创新研发 + 木浆与纸品战略采购

### 连接点 1｜工程图纸体系是研发的隐性知识载体——把"手感经验"固化为可追溯资产

涉及幻灯片：SLIDE 3（Finding Drawings）、SLIDE 13（Where Used and BOM）、SLIDE 16（AutoCAD/SolidWorks 与 A/S 标识）、SLIDE 17（FPM/FP1/FPS 三层定义）、SLIDE 18–19（层级图）；核心数据来自 Ch2 BOM_A（C153-FPS-01575-J-09，非本章，标注引用）

核心概念：FPM（Part / Smallest possible unit）→ FP1（Assembly，Nonwoven + Adhesive）→ FPS（Finished/Full Product，as would be used in the mill）

关键数据（全部可回溯）：

||||||
|---|---|---|---|
|导流层|SMALL SURGE|C153-FP1-00178-D-04|100MM W × 236MM L|
|腿围橡筋|LEG ELASTIC STRANDS|C153-FPM-00157-D-01|152MM front / 173.1MM rear|
|腿围橡筋胶|LEG ELASTIC ADHESIVE|C153-FPM-00156-B-02|199MM CD × 227MM MD|
|芯体-面层胶|PAD TO LINER ADHESIVE|C153-FPM-00154-B-01|125MM CD × 367MM MD|
|耳贴胶|EAR ADHESIVE|C153-FPM-00155-B-01|202 outside W × 182 inside W|
|护围高度|FLAP|C153-FP1-00054-D-04|45MM HEIGHT|
|腰围|WAISTBAND|C153-FP1-00037-D-02|44MM WIDTH|


洞察：KC 把每一项设计决策都降维成「一个图号 + 一组可量化尺寸」：SURGE 100×236 mm 不是配方描述，而是图纸上的一条尺寸标注；LEG ELASTIC 152/173.1 mm 不是工艺记录，而是 FPM 级图纸的标题。这意味着——研发知识不存放在人的经验里，也不存放在 Word 报告里，而是存放在图号体系的节点上。人员流失带走的是解释能力，带不走的是尺寸与层级关系。同时，FP1 的组合范式 "Nonwoven + Adhesive"（SLIDE 17）揭示了一个行业通用事实：卫材的最小功能单元不是"材料"，而是"材料 + 把它粘上去的胶"。

可执行行动建议：
1. 建立"设计参数 → 图号节点"的强制映射表：对本方在研的每一款纸尿裤/湿巾，列出全部可量化设计参数（surge 长宽、leg elastic 前/后长度、各 adhesive 的 CD×MD 涂布范围、flap/waistband 高度、embossing 图案与尺寸），逐个分配内部图号节点，禁止参数只存在于打样记录或工艺单上。
2. 把"材料 + 胶"定义为一个图元：照抄 FP1 的 Nonwoven + Adhesive 范式——在内部 BOM 中，无纺布/木浆复合层与其对应的胶必须成对建图，胶的涂布幅宽（CD）与长度（MD）作为该图元的必填字段。这直接关联到胶耗成本与木浆用量的核算颗粒度。
3. 为木浆与纸品采购建立"图纸级用量口径"：当每种基材在图纸上都有明确的 CD×MD 尺寸与所属 FP1 图元后，单件产品基材用量可由图纸直接计算，而非依赖产线实测——这为战略采购的量价谈判与套期保值提供独立于供应商的用量基准。
4. 图纸节点必须带修订与生效信息：参考 DRCS 的 "back issues"（SLIDE 14）与 SPOT 结果列的 Effective 字段（图像补充 p6），确保任一历史批次的量产参数可回溯——这是客诉与质量追溯的取证基础。

### 连接点 2｜图号编码规则的可借鉴性——一套适用于国内卫材企业的图号编码建议

涉及幻灯片：SLIDE 9（图纸号输入框示例 C153-FPS-01575）、SLIDE 15（PREFIX / TYPE 双筛选器）、SLIDE 17–19（类型与层级）、Ch2 图像补充（C153-FPS-01575-J-09）、Ch3 图像补充（同次变更影响 5 张 FPS 连号）

核心概念：Drawing Number 作为唯一主键、PREFIX/TYPE 作为检索维度、层级码作为结构化索引

关键数据：KC 图号 = C153（平台）- FPS（类型，共 7 类前缀）- 01575（5 位流水）-J-09（修订/分页，未证实）；一次变更（ER# 900200005649）同时影响 5 张 FPS（01640 / 01641 / 01577 / 01574 / 01575）+ 1 张 FP1（C153-FP1-00178）+ 1 张 FPM（C153-FPM-00481）

洞察：KC 编码的真正价值不在于唯一性（任何流水号都能唯一），而在于三件事：①平台与类型分离，使 PREFIX 一个筛选器就能切出"某平台全部成品图"；②层级写进编码（FPM/FP1/FPS），无需打开文件即可判断该图在 BOM 树的哪一层；③同系列连号，使"一次设计变更影响哪些图"可以通过号段批量圈定，而不必逐张查 BOM。这三点共同把编码本身变成了检索与变更影响分析的工具。

可执行行动建议 —— 建议编码方案（本报告设计，非 KC 原文）：

[品类]-[平台]-[类型]-[流水]-[尺码/变体]-[版本]
  PP     B5     FPS    0157      S1         A/01

||||||
|---|---|---|---|
|品类|PP=纸尿裤 / WP=湿巾 / AF=成人裤 / FC=女性护理|2 位字母，先分大类|KC 用 C153 单段混合平台，此处建议显式拆出品类便于跨品类统计|
|平台|B5/B6… 平台代号|2 位，与品类组合形成产品族|对应 C153|
|类型|FPS（成品）/ FP1（组件）/ FPM（零件）/ PDD（开发中）/ LPA（花型排版）/ PSD（工艺示意）/ DOC（文档）|直接沿用 KC 类型码，降低沟通成本，且便于对标外部资料|对应 FPM/FP1/FPM/FPS/PDD/LPA/PSD/DOC|
|流水|4 位数字，同系列连号分配|同一设计的多个尺码分配连续号段，便于批量变更|对应 01575；关键改进：连号作为强制规则写入制度|
|尺码/变体|S1/M/L/XL…|显式写出尺码|KC 把变体藏在 5 位流水里（推测），且 User Defined Title 才写 S1——此处建议改进为显式段，可读性更强|
|版本|A/01… 或 -R03-S01（第 3 次修订，第 1 页）|必须显式定义并写进编码规范|KC 的 -J-09 定义 [未找到原句]，是本方必须自行补齐的缺口|


配套制度（3 条硬规则）：
1. 类型码即权限粒度：参考 Ch3 SLIDE 45 审批矩阵与 Ch5 SLIDE 68 的差异授权——FPM/FP1 由研发自批，FPS 需质量会签。编码里写了类型，权限就能按号段前缀自动匹配，无需人工判断。
2. 流水号连号分配 + 变体段显式化：同一设计的不同尺码必须连号，确保"改一次导流层"能用号段一次性列出全部受影响图（KC 实例：一次变更新增/修订 5 张 FPS）。
3. 版本段必须由编码规范定义，不留"约定俗成"：KC 交付给读者的最大教训是——修订段含义在整套培训材料中都没有定义（[未找到原句]）。本方在建体系第一天就必须把版本段的取值规则、递增条件、废止规则写成制度文件，否则 5 年后无人能解释。

### 连接点 3｜索引（SPOT）与存储（DRCS）分离的信息架构——对 PLM / 图文档系统选型的启示

涉及幻灯片：SLIDE 4–7（SPOT 路径）、SLIDE 8–15（DRCS 能力）、SLIDE 63（"Found on last page of specs from The SPOT / Full drawings in DRCS"）；权限部分引用 Ch5 SLIDE 67/68/73

核心概念：Index（业务索引）/ Repository（工程真相源）分离；Viewer（查看器）独立

关键数据：SPOT 路径 4 页 7 动作，终点为图号，文档形态为 MS Word；DRCS 6 项能力（Checkout/Release、Download、View、Print、Where Used & BOM、Back issues）+ Advanced Search（2 个核心筛选器 PREFIX/TYPE）；服务 30+ 年；权限 3 级（View / Work / Approve）；FPS 审批权归 Quality（Rex Stuart 为唯一批准人，Ch3 SLIDE 45）；Feminine Care 不开放 FPM/FP1/FP2 权限（Ch5 SLIDE 68）

洞察：KC 的架构是三件套而非两件套：SPOT（索引）→ DRCS（存储/受控）→ eDrawings / DWG TrueView（查看）（后两者见 SLIDE 63："eDrawings can be used to view SolidWorks drawings. Download from Software Center." / "DWG TrueView can be used to view AutoCAD drawings."）。关键在于——查看器是独立安装的（Software Center 下载），不依赖 PLM 系统本身。这带来三个可迁移结论：①索引系统可以"轻"（Word + 图号），只要模板纪律足够强（图纸永远贴在文档末页）；②重投入应集中在存储系统的版本/审批/BOM 关系上，而非全文检索；③权限只做在存储层，索引层保持宽入口，既降低使用门槛又守住核心资产。反过来看代价：SLIDE 63 演讲者自嘲 "It's confusing; I'm sorry." —— 说明系统割裂是有真实用户体验成本的，本方选型时应以"统一入口 + 后台分离"为目标，避免把割裂暴露给终端用户。

可执行行动建议：
1. 选型要求：索引层与存储层可分离部署，但必须统一入口。向 PLM/图文档供应商明确提出：业务侧检索（按品牌/品类/变体/生效日期）与工程侧受控存储（版本、签出/发布、BOM、审批）可为两套数据模型，但用户只看到一个搜索框——直接规避 KC 的 "It's confusing" 问题。
2. 用"模板纪律"替代"智能检索"作为阶段一方案。若短期内不上 PLM，可先用 KC 的 SPOT 模式：规格文档统一模板 + 图纸固定贴在末页 + Ctrl+F 搜 "draw"。这是零系统成本、高确定性的过渡方案（SLIDE 7 已验证可行）。
3. 审批矩阵必须与图纸层级绑定，且写进系统。照搬 KC 的分层授权思路：零件/组件级（FPM/FP1）由研发自批以提速（KC 明确说此举 "gives product developers more control and speed within the process"，Ch5 SLIDE 67），成品级（FPS）由质量批准以控风险。把审批规则配置在类型码（号段前缀）上，实现自动路由。
4. 查看器选型要按图纸来源分开：三维（SolidWorks 类）需支持 BOM/装配树浏览（KC 用 eDrawings，.sldasm/.sldprt）；二维（AutoCAD 类）需支持图层与尺寸标注浏览（KC 用 DWG TrueView）。选型评估清单里必须包含"能否读出装配体层级"这一条，否则三维图的零件级参数（如 adhesive 涂布尺寸）将无法被研发与采购复用。
5. 为采购职能配置 View 级只读权限。KC 的权限矩阵中 Research (Staff) 在 Global / Sector Drawings 上为 View 级别（Ch5 图像补充角色-权限表）——说明非工程职能也能持有查看权。对木浆与纸品战略采购而言，争取 View 权限即可获得图纸级基材用量与规格信息，无需 Work/Approve。


## 模块6：金句索引（Key Quotes Index）

||||||
|---|---|---|---|
|1|"Product drawings can be found in The SPOT"|SLIDE 4（亦见 5/6/7，共 4 次）|产品图纸可以在 The SPOT 中找到。|全章重复 4 次的锚句——SPOT 是"找图"的第一入口，也是 KC 把"业务索引"独立出来的证据。记住它，就记住了两段式流程的第一段。|
|2|"Click the 'Variant Property Spec' number to download a copy of the specification"|SLIDE 6|点击"Variant Property Spec"编号，即可下载一份规格文档副本。|这是 SPOT 路径的唯一可执行动作——可点击的是编号，不是图纸。它定义了 SPOT 的产出物形态：Word 文档。|
|3|"Or press 'cntrl + F' to open the search bar and type in 'draw' to jump down to the drawing number"|SLIDE 7|或者按 Ctrl + F 打开搜索栏，输入"draw"，直接跳到图号位置。|全章最"土"也最实用的一招。它证明 KC 的稳定性靠的是模板纪律（图纸永远贴在规格末页），不是系统智能——对企业建体系的启示极大。|
|4|"Detailed product drawings are found in DRCS"|SLIDE 8|详细的产品图纸在 DRCS 中。|关键词 Detailed。一个形容词划清了 SPOT 与 DRCS 的全部边界：SPOT 有"图"，DRCS 才有"详细图"。架构分工的判据句。|
|5|"PREFIX and TYPE are the 2 filters I find most useful."|SLIDE 15|PREFIX 和 TYPE 是我觉得最有用的两个筛选器。|全章检索部分的最高价值句。它告诉读者：在图纸库里，编码筛选比全文检索更有效——这是图号体系存在的根本理由，也是本方建编码规范的直接依据。|
|6|"AutoCAD is layers" / "Solidworks is LEGOs"|SLIDE 16|AutoCAD 是图层；SolidWorks 是乐高积木。|两个比喻讲清了两种 CAD 的本质差异：二维图层叠加 vs 三维零件装配。也预示了后续读图方式的差异（A 直读，S 需查 BOM）。|
|7|"A blue 'A' next to a drawing means it's an AutoCAD drawing. / A red 'S' next to a drawing means it's a SolidWorks drawing."|SLIDE 16|图纸旁的蓝色"A"表示这是 AutoCAD 图纸；红色"S"表示这是 SolidWorks 图纸。|一个颜色字母承载了"该用什么工具打开、信息密度如何"的判断。元数据的极简范式——低技术、高可靠，值得照抄到内部图文档系统。|
|8|"SolidWorks product drawings are a combination of many smaller drawing combined."|SLIDE 17|SolidWorks 产品图纸是由许多更小的图纸组合而成的。|点破"一张成品图 ≠ 一张图"——它是一棵图纸树。这是理解变更传播（改一个 FPM 影响多个 FPS）与 BOM 反查的前提。|
|9|"FPM – Part / Detail / Smallest possible unit"|SLIDE 17（亦见 18/19）|FPM——零件 / 详图，最小可能的单元。|定义了知识颗粒度的下限。卫材研发中真正值钱的参数（胶的 CD×MD 涂布、橡筋长度）就落在这一层。|
|10|"FP1 – Assembly / Groupings of FPM drawings that are often associated together / Ex. – Nonwoven + Adhesive"|SLIDE 17|FP1——组件，是经常一起出现的 FPM 图纸的组合；例：无纺布 + 胶。|全章对卫材行业最有行业洞察的一句："无纺布 + 胶"被定义为一个物料单元。这直接决定了 BOM 结构与成本核算的颗粒度。|
|11|"FPS – Finished Product Specification / Drawing as would be used in the mill"|SLIDE 17（SLIDE 18/19 作 "Full Product"）|FPS——成品规格图，即在生产现场被使用的那张图纸。|"as would be used in the mill" 定义了成品图的验收标准：工厂能用才算成品图。注意 SLIDE 17 写 *Finished*、SLIDE 18/19 写 *Full*，同一缩写两种展开，检索时须同时接受。|
|12|"Found on last page of specs from The SPOT / Full drawings in DRCS"|SLIDE 63（Ch4 总结页，交叉印证 Ch1）|SPOT 规格文档的最后一页能找到图纸；完整图纸在 DRCS。|全篇对 Ch1 最精炼的总结——两句对偶把 SPOT（索引）与 DRCS（存储）的职能分工一次说清。做架构汇报时可直接引用。|
|13|"It's confusing; I'm sorry. Step-by-step instructions are in the appendix."|SLIDE 63|这确实令人困惑，抱歉；逐步操作说明在附录里。|培训作者的自嘲，却是最有价值的架构警示：系统割裂会转嫁为全员学习成本。选型时必须以"统一入口 + 后台分离"规避。|
|14|"Providing Drawing and File Management Services to the K-C community for over 30 years."|SLIDE 9 图像补充|为 K-C 社区提供图纸与文件管理服务已超过 30 年。|30 年这个数字是体系可信度的量化锚点：它说明这套编码与两系统架构经过了长期演化验证，值得作为本方建体系的参考基线，而非临时方案。|
|15|"General rule of thumb for 'Estimated Hours' is 8 hrs per drawing to be created/revised."|Ch3 SLIDE 45（非本章，供成本测算引用）|经验法则是：创建或修订一张图纸约需 8 小时。|唯一可用于图纸工作量化的数字。做研发工时预算、外包制图报价、变更成本评估时的基准值（8 小时/张）。|


## 附：本报告取证状态汇总

|||||
|---|---|---|
|本章（SLIDE 1–19）有原句支撑的观点|全部模块 1–4 主体|均标注 SLIDE N|
|标注 [未找到原句] 的术语|8 项|SPN、FRM、FLD 三个前缀；eMARS、BAPI、Business Warehouse Reporting、Business Unit 四个字段；The SPOT 的 "system for part / sole purpose is tracking drawings" 定义；Documentum 展开|
|标注 【推断】 的内容|4 处|图号段 4（修订字母）、段 5（分页/子序号）、PDD 与 FPS 同层、FP1 组合范式的行业含义|
|引用非本章材料（已显式标注）|5 处|Ch2 BOM_A / File Information / SLIDE 34；Ch3 SLIDE 45 审批矩阵 / 图像补充 ER#；Ch4 SLIDE 63；Ch5 SLIDE 67/68/73 及图像补充|
|待取证项|3 项|① SLIDE 6 渲染图未读全的列名（记录以 "…" 结尾）；② C153-FPS-01592-1-10 的段 4 为何是数字；③ SLIDE 17 单张渲染图上是否还有本章未记录的前缀（SPN/FRM/FLD 可能来源）|



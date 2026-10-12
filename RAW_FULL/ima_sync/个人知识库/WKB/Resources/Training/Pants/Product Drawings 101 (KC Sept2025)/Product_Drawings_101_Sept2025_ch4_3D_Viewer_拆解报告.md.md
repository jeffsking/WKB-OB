---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_1e5971f18257d6ed79b93cb09edf2921001a693ee6c0644e"
source_file: "Product_Drawings_101_Sept2025_ch4_3D_Viewer_拆解报告.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch4_3D_Viewer_拆解报告.md.md"
extracted: "2026-09-30"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
---

# Product_Drawings_101_Sept2025_ch4_3D_Viewer_拆解报告.md


章节：Ch4 3D Viewer ｜ 覆盖幻灯片：47–66 ｜ 文档：Product Drawings 101 (KC, Sept 2025) ｜ 拆解日期：2026-08-30

## 阅读说明与证据规则

|||
|---|---|
|证据来源|①章节文件文本层（幻灯片文本 + 演讲者备注）；②文件末尾「图像内容补充（逐页渲染读图确认）」区块。二者均视为可靠来源，引用时后者标注为「图像补充」|
|引用标注|所有观点后附 SLIDE N；跨章引用附 ChN SLIDE N|
|缺失标注|原文无对应表述处标 [未找到原句]；属本报告推断而非原文者，明确标「【推断，非原文】」并给出推断所依据的原文条目|
|数据纪律|所有加粗数字均可回溯至原文；不做外推估算；不引入 KC 材料之外的产品数据|
|语言|模块 1–5 正文与定义保留英文原文；模块 6 金句附中文翻译|


本章幻灯片清单（用于核对覆盖完整性）

||||
|---|---|---|
|47|3D Viewer（章节封面）|标题|
|48|Download eDrawings — steps 1/2/3|步骤|
|49|Download eDrawings — step 4 + The DESK 兜底|步骤|
|50|Download the full SolidWorks file from DRCS；.sldasm / .sldprt；两种打开方式|步骤 + 格式|
|51|eDrawings will let you view the 3D version of drawings|断言|
|52–54|Components section（drill down / left-click / right-click 三项）|递进式功能|
|55–56|Markup section（5 类标注 + dimension 定义）|功能|
|57|Measure section（与 dimension 同功能、不落图）|功能|
|58|Move section（两种选件方式 + drag & drop）|功能|
|59–60|Explode section（slider + 4 种 Move 工具）|功能|
|61–62|Tips & tricks（Reset / View Orientation / Normal To）|技巧|
|63|Final thoughts（双查看器总结 + WI-36700）|收束|
|64|Questions|仅演讲者备注（图片署名）|
|65|APPENDIX|分隔页，无图像|
|66|Getting Access to Drawings|分隔页（指向 Ch5）|




覆盖说明：本章实质内容页为 SLIDE 47–63（17 页）；SLIDE 64–66 为 Q&A / 附录分隔页，其中 SLIDE 66 的标题 Getting Access to Drawings 在结构上引出 Ch5。本报告对 64–66 只做结构说明，不做论点提取。

# 模块1：核心论点（Core Arguments）

### A1｜3D viewing is a separate, self-installed capability layer — it is not a feature of DRCS, and it is split in two by source format.

英文概括：Viewing 3D is not something DRCS does for you. The user must (i) install a viewer locally and (ii) pull the native CAD file out of DRCS. KC operates a two-viewer topology: eDrawings for SolidWorks drawings, DWG TrueView for AutoCAD drawings — both obtained from the internal Software Center, i.e. no seat-license request, no engineering-ticket.

支撑依据
- SLIDE 63："eDrawings can be used to view SolidWorks drawings. Download from Software Center." / "DWG TrueView can be used to view AutoCAD drawings. Download from Software Center."
- SLIDE 50："You will need to download the full SolidWorks file from DRCS"
- 安装入口 SLIDE 48："Download eDrawings from the KC Software Center or Company Portal"
- 版本事实（图像补充）：软件中心可见 Autodesk DWG Trueview 2025、Dassault Systems eDrawings 2024

可验证推论：查看能力是零授权成本、自助获取的，因此它可以被下放到非工程岗——这是模块 5 业务建议 A 的直接依据。【推断，非原文】原文未出现 "free" / "no license" 字样，只说 "Download from Software Center"。

### A2｜The viewer is navigational + annotative, never authoring — the drawing of record still lives in DRCS and is still changed by others.

英文概括：eDrawings 在 Ch4 中呈现的全部能力（Components / Markup / Measure / Move / Explode）都是查看与表达动作，没有任何一处赋予用户改图能力。真正的变更通道在 Ch3：由 Jacobs Engineering 执行，内部交付物是 redline。

支撑依据
- 查看定位：SLIDE 51 *"eDrawings will let you view the 3D version of drawings"*；SLIDE 57 "the dimensions won't be recorded on the drawing"
- Move 只移动视图中的零件：SLIDE 58 *"The Move section will let you move individual parts within the drawing"*；可完全撤销（SLIDE 61 *"You can undo any part movements or camera angles at any time…"*）
- 改图在外部：Ch3 SLIDE 36 *"Product drawing edits are handled through Jacobs Engineering"*；Ch3 SLIDE 43 "Submit redlines through Jacobs Engineering to update drawings"
- [未找到原句]：Ch4 未出现 "save" / "edit" / "modify the drawing" / "write back to DRCS" 等表述。

可验证推论：3D 查看器是只读沙箱——任何在 eDrawings 里的移动、标注、测量都不会污染图纸版本。这对跨部门开放是安全前提。【推断，非原文】

### A3｜eDrawings converts the flat BOM of Ch2 into an interactive component tree — the single biggest value-add over 2D.

英文概括：Ch2 的 Bill of Materials 是一个静态表格（11 行子件，见 Ch2 SLIDE 33–34 图像补充）；eDrawings 的 Components 面板把同一个装配体变成可下钻、可定位、可显隐的结构树，并给出三个层次的操作：层级下钻 → 左键高亮定位 → 右键可见性控制。

支撑依据
- 全零件列出 + 下钻：SLIDE 52 "The components section will list all parts used in drawing" / "…you can drill down to see which parts make up each part in the list until"
- 左键定位（双向高亮）：SLIDE 53 "Left-clicking a part will highlight it in the list as well as in the drawing itself."
- 右键可见性三件套：SLIDE 54 Hide / Make Transparent / Hide Others (aka – Isolate)
- 右键菜单完整项（图像补充）：Hide / Make Transparent / Hide Others (aka Isolate) / Show All / Isolate / Properties...（较文本层多出 Show All / Isolate / Properties... 三项）

可验证推论：Make Transparent + Hide Others 是 2D 图纸里唯一无法实现的两种"透视"能力，直接对应 Ch2 的 Cross Section 需求（层序与胶路）。见模块 4 / M4-3。

### A4｜Measurement is deliberately split into two modes by persistence — a governance decision, not a UI duplication.

英文概括：Ch4 给出两套"量尺寸"工具，功能相同、留痕性相反：Dimension（Markup 内）会写入图纸并保留；Measure（独立 section）不记录。这是本章唯一一处显式的"轻/重"分级设计。

支撑依据
- 落图：SLIDE 56 "The dimension feature will add a dimension between two points/surfaces"
- 不落图：SLIDE 57 "The measuring tool works the same as the dimension tool, only the dimensions won't be recorded on the drawing"
- 量测对象：SLIDE 57 "You can measure between points/lines and/or between planes/surfaces"
- 实测样例（图像补充）：Dimension 示例标注值 749.000（红色显示）

可验证推论：Measure 的"不留痕"是双刃剑——它适合临时核对（如模块 5 的竞品对照），但不能作为可追溯证据，读数必须手工转录到外部记录表。【推断，非原文】

### A5｜The 3D environment is designed to be fully revertible and orientation-standardized — lowering the skill floor for non-experts.

英文概括：KC 用两条设计把 3D 的"高风险感"消掉：一是全局撤销（Reset 一键恢复所有零件移动与视角），二是标准化视角切换（View Orientation 常用视角 + Normal To 自动正视选中面）。配合 Ch5 的 View 权限即可开放给非工程角色。

支撑依据
- 全局 Reset：SLIDE 61、重申于 SLIDE 62："You can undo any part movements or camera angles at any time by right-clicking in open space, clicking 'View', clicking 'Reset'"
- 视角切换：SLIDE 62 "Use the 'View Orientation' tool to easily switch between common viewpoints in the drawing."
- 正视：SLIDE 62 "The 'Normal To' view will rotate the drawing to look down on the face/plane you currently have selected."
- 权限侧：Ch5 SLIDE 73 *"Place check 'View', 'Work', & 'Approve' square boxes."*；角色表（Ch5 图像补充）中 Research (Staff) | Global | Sector Drawings | View

可验证推论：Reset 的存在 = 允许"随便点"，这是把 3D 工具交给采购/质量/市场岗的心理与管理前提。【推断，非原文】

# 模块2：关键概念操作化定义（12 个）

### 概念 1：3D Viewer（三维查看器）

- (a) 中文名 + English term：三维查看器 / 3D Viewer
- (b) 英文定义：The capability of viewing the three-dimensional version of a product drawing, obtained by downloading the native CAD file from DRCS and opening it in a locally installed viewer, as opposed to reading the 2D drawing sheets.
- (c) 操作化定义




- 判定式：能同时满足 ①可旋转/切换视角；②可展开装配体零件列表；③可在模型上直接量取尺寸 → 即为 3D Viewer 能力。
- 量化指标：KC 实现中可从 DRCS 下载并打开的 3D 文件格式数 = 2（.sldasm / .sldprt，SLIDE 50）；底部功能标签总数 = 11（Play / Stop / Home / Previous / Next / Markup / Measure / Section / Annotations / Configurations / Components，图像补充）。
- (d) 原文英文摘录："To view the 3D version of drawings you will need to download the SolidWorks file and open in eDrawings" SLIDE 50；章节标题 "3D Viewer" SLIDE 47
### 概念 2：eDrawings（下载与安装）

- (a)：eDrawings（达索 3D/2D 查看器）/ eDrawings — download & installation
- (b) 英文定义：Dassault Systèmes' free viewer used at KC to open SolidWorks drawings; distributed through the internal KC Software Center / Company Portal as a self-service install, with The DESK as the fallback support channel.
- (c) 操作化定义



- 测量维度：安装步骤数 = 4（SLIDE 48 编号 1/2/3 + SLIDE 49 编号 4）；兜底通道 = 1（The DESK）；可用版本号 = eDrawings 2024（图像补充）。
- 判定式（安装成功）：在 Software Center / Company Portal 中搜到 eDrawings → 点击 Install → 完成后 .sldasm 文件可用 eDrawings 作为默认应用打开（SLIDE 50）。
- (d) 原文英文摘录："Download eDrawings from the KC Software Center or Company Portal" SLIDE 48；"If you are unable to find the app in the list, contact The DESK for help with installation." SLIDE 49；"eDrawings can be used to view SolidWorks drawings. Download from Software Center." SLIDE 63
### 概念 3：DWG TrueView（AutoCAD 图纸查看器）

- (a)：DWG TrueView（Autodesk DWG 查看器）/ DWG TrueView
- (b) 英文定义：Autodesk's viewer used at KC to open AutoCAD drawings, likewise downloaded from the Software Center; it is the 2D/CAD counterpart to eDrawings in KC's two-viewer topology.
- (c) 操作化定义




- 判定式（何时用哪个查看器）：图纸标识为红色 'S'（SolidWorks）→ eDrawings；图纸标识为蓝色 'A'（AutoCAD）→ DWG TrueView。依据 Ch1 SLIDE 16："A blue 'A' next to a drawing means it's an AutoCAD drawing." / "A red 'S' next to a drawing means it's a SolidWorks drawing."
- 量化指标：KC 软件中心可见版本 = Autodesk DWG Trueview 2025（图像补充）。
- 注意：Ch4 对 DWG TrueView 的记述仅 1 句（SLIDE 63），无安装步骤页、无功能清单页。
- (d) 原文英文摘录："DWG TrueView can be used to view AutoCAD drawings. Download from Software Center." SLIDE 63
### 概念 4：dwg 文件格式

- (a)：dwg 文件格式（AutoCAD 原生图纸格式）/ dwg file format
- (b) 英文定义：The native file format of AutoCAD drawings at KC, viewed with DWG TrueView; in this material it is referenced only through the tool name DWG TrueView, and is the counterpart format to SolidWorks' .sldasm / .sldprt.
- (c) 操作化定义




- 判定式：图纸在 DRCS/The SPOT 中带蓝色 'A' 标记 = AutoCAD/dwg 系 → 走 DWG TrueView 通道（Ch1 SLIDE 16）。
- 可确认事实：本章提到的文件扩展名共 4 个 —— .sldasm、.sldprt（SLIDE 50 文本层）与 .slddrw、TIF Image (*.tif)（图像补充，出现在文件对话框）。
- [未找到原句]：字面字符串 .dwg 在全材料（Ch1–Ch5 文本层 + 图像补充）中未出现；"DWG" 仅作为工具名 DWG TrueView 的一部分出现（SLIDE 63 与图像补充）。故"dwg 扩展名"属依据工具名反推，原文未直接陈述。
- (d) 原文英文摘录："DWG TrueView can be used to view AutoCAD drawings." SLIDE 63；字面 .dwg：[未找到原句]
### 概念 5：Measurement（测量）

- (a)：测量 / Measurement（Measure section）
- (b) 英文定义：A transient measuring action in eDrawings that returns dimensions between geometric entities without writing them onto the drawing, contrasted with the persistent Dimension annotation inside Markup.
- (c) 操作化定义




- 判定式：量测对象 ∈ {points, lines, planes, surfaces} 且结果不落图、不进版本 → Measure；量测对象 ∈ {two points/surfaces} 且结果写入图纸 → Dimension（SLIDE 56）。
- 量化指标：量测对象类别 = 4 类（points / lines / planes / surfaces，SLIDE 57）；示例中落图标注值 = 749.000（图像补充）。
- 操作路径：底部标签栏 → Measure（图像补充）。
- (d) 原文英文摘录："The Measure section will tell you dimensions in the drawing" SLIDE 57；"The measuring tool works the same as the dimension tool, only the dimensions won't be recorded on the drawing" SLIDE 57；"You can measure between points/lines and/or between planes/surfaces" SLIDE 57
### 概念 6：Cross-section（剖切）

- (a)：剖切（截面）/ Cross-section（Section tab）
- (b) 英文定义：In the 3D viewer, the Section capability on the eDrawings tab bar; in the 2D drawing set it is the Cross Section sheet — at KC titled "CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT" — which exposes the internal layer stack and adhesive layout.
- (c) 操作化定义





- 判定式（2D）：视图中出现沿 MD 或 CD 的剖切线且露出 ≥2 个材料层与层间胶层 = Cross Section。
- 判定式（3D）：启用底部 Section 标签后以平面切割模型、露出内腔/层序 = Cross-section；辅以 Make Transparent 可达同等"透视"效果（SLIDE 54）。
- 量化指标：eDrawings 底部标签栏中 Section 为 1 个独立标签（图像补充）。
- [未找到原句]：Ch4 文本层没有对 Section 标签的任何说明句——既无定义也无操作步骤；该标签的存在仅由图像补充确认。Ch4 中可用的"透视"能力，在文本层只有 SLIDE 54 的 Make Transparent 一句。
- (d) 原文英文摘录：3D 侧：标签名 "Section"（图像补充，eDrawings 底部标签栏）；功能说明句：[未找到原句]。2D 侧："Anatomy of a product drawing … Cross Section" Ch2 SLIDE 23；"CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT" Ch2 SLIDE 24（图像）
### 概念 7：Exploded view（爆炸图）

- (a)：爆炸视图 / Exploded view（Explode section）
- (b) 英文定义：An interactive mode in eDrawings that separates the individual parts of an assembly in order to show how the product is constructed, driven by a slider and refined with the Move tools.
- (c) 操作化定义





- 判定式：装配体各零件沿装配轴产生非零位移且零件间分离 → Exploded view；位移量由滑块连续控制。
- 量化指标：配套的精确定位工具 = 4 种（Free Drag / Position / Translate / Rotate，SLIDE 60）；滑块 = 1 个。
- 可逆性：全部位移可由 Reset 一次性撤销（SLIDE 61–62）。
- (d) 原文英文摘录："The Explode section will let you separate individual parts to better show how the product is constructed" SLIDE 59；"Use the slider to separate individual components." SLIDE 59；"Use tools from the 'Move' section to position the individual parts." SLIDE 60
### 概念 8：Markup（标注 / 批注）

- (a)：标注 / 批注 / Markup
- (b) 英文定义：The eDrawings section that lets the user add notes to the drawing, comprising five annotation types, of which Dimension is the only one that records a measured value on the drawing.
- (c) 操作化定义





- 判定式：由用户在查看器内后加、图层上可关闭、不改变 CAD 几何与图纸版本 → Markup（注意 KC 的工程变更另有通道，见下）。
- 量化指标：标注类型 = 5（Text / Shapes / Dimensions / Images / Comments，SLIDE 55）；其中落图留痕的子类型 = 1（Dimension，SLIDE 56）。
- 边界条件：Markup 不是 KC 的工程变更通道——正式变更须走 Ch3 SLIDE 36 的 FORM-48129 redline + Jacobs Engineering。【推断，非原文】原文未明说两者关系，但 Ch4 未给 Markup 任何"提交/发布"出口。
- (d) 原文英文摘录："The Markup section will let you add notes to the drawing" SLIDE 55；"You can add: Text / Shapes / Dimensions / Images / Comments" SLIDE 55；"The dimension feature will add a dimension between two points/surfaces" SLIDE 56
### 概念 9：SolidWorks

- (a)：SolidWorks（三维 CAD 建模软件）/ SolidWorks
- (b) 英文定义：KC's 3D CAD authoring system, described in Ch1 by the analogy "Solidworks is LEGOs"; its native files (.sldasm assembly / .sldprt part) are what must be downloaded from DRCS and opened in eDrawings to obtain the 3D view.
- (c) 操作化定义





- 判定式：DRCS 中图号旁为红色 'S'（Ch1 SLIDE 16）= SolidWorks 系 → 3D 可查看路径成立。
- 量化指标：KC 装配层级 = FPM（Part）→ FP1/FP2（Sub-Assembly）→ FPS（Final Drawing）（Ch1 SLIDE 17–19）；本章下载样例文件 = C153-FPS-01776-01.sldasm，4.42 MB，来源 cadkc.com（图像补充）。
- 权限事实：Ch5 图像补充 APPLICATIONS 列表标注 "SolidWorks (K-C Internal - North & South America Only)" —— SolidWorks 本体授权有区域限制，而查看器无此标注。
- (d) 原文英文摘录："To view the 3D version of drawings you will need to download the SolidWorks file and open in eDrawings" SLIDE 50；"Solidworks is LEGOs" Ch1 SLIDE 16；"SolidWorks drawings rely on BOM / Where Used feature to find detailed dimensions" Ch2 SLIDE 33
### 概念 10：Exporting Drawings（图纸导出）

- (a)：图纸导出 / Exporting Drawings
- (b) 英文定义：[未找到原句] — KC 材料未使用 "export" 作为流程术语。原文表述的实际动作是"从 DRCS 下载完整的 SolidWorks 文件"（download），以及从 The SPOT 下载规格副本（download a copy）。
- (c) 操作化定义





- 实际动作链（原文可证，共 4 步）：DRCS 定位图纸 → 下载 .sldasm / .sldprt → ①双击文件并选 eDrawings 为默认应用，或 ②先开 eDrawings 再 File > Open（SLIDE 50）。
- 量化指标：下载样例体积 = 4.42 MB（图像补充，C153-FPS-01776-01.sldasm）；打开方式 = 2 种（SLIDE 50）。
- [未找到原句]：export / save as / convert 等术语在全材料（Ch1–Ch5）中检索为 0 次；"DRCS → 导出"这一表述属本报告的流程归纳，非原文用语。
- (d) 原文英文摘录："You will need to download the full SolidWorks file from DRCS" SLIDE 50；"Either double-click the drawing file itself and select 'eDrawings' as the default application / Or open eDrawings first and use 'File > Open' to find and open the drawing you downloaded" SLIDE 50；"Click the 'Variant Property Spec' number to download a copy of the specification" Ch1 SLIDE 7（图像补充）
### 概念 11：Repositioning Models（模型重定位）

- (a)：模型重定位 / Repositioning Models（Move section）
- (b) 英文定义：The eDrawings Move section which lets the user move individual parts within the drawing for visual purposes, using either direct dragging or precise axis-constrained translation/rotation — always reversible via Reset.
- (c) 操作化定义





- 判定式：位移对象是单个零件而非整装；位移仅改变显示状态（可由 Reset 撤销）；提供 4 种精度档位。
- 量化指标：选件方式 = 2 种（①用 move 光标点零件；②选 move 光标后在 Components 列表中高亮零件，SLIDE 58）；移动模式 = 4 种 —— Free Drag（快速拖放）/ Position（沿特定轴的精确移动或旋转）/ Translate（沿轴精确移动）/ Rotate（沿轴精确旋转），SLIDE 60。
- 区别点：Position 是 4 种里唯一同时支持移动与旋转的；Translate 与 Rotate 各自只做一件事。
- (d) 原文英文摘录："The Move section will let you move individual parts within the drawing" SLIDE 58；"Simply drag and drop the selected part to move it" SLIDE 58；"Free Drag = Used for quick drag & drop movement. / Position = Used for precise movement or rotation along a particular axis. / Translate = Used for precise movement along an axis. / Rotate = Used for precise rotation along an axis." SLIDE 60
### 概念 12：Interference check（干涉检查）

- (a)：干涉检查 / Interference check
- (b) 英文定义：[未找到原句] — 本材料未定义、未提及该能力。
- (c) 操作化定义







- 检索结果：interference 一词在 Product_Drawings_101_Sept2025 全部 5 个章节文件（文本层 + 图像内容补充）中出现 0 次。
- eDrawings 中功能最接近的原文能力（供替代使用，但均非干涉检查）：
- Hide Others (aka – Isolate) SLIDE 54 —— 隔离单件，人工目视判别是否碰撞；
- Make Transparent SLIDE 54 —— 透视重叠区域；
- Explode SLIDE 59 —— 分离零件后观察装配间隙；
- Measure SLIDE 57 —— 量取面到面距离，人工判断是否 < 0（干涉）。
- 注意：以上 4 项是人工目视判读路径，不等于自动化的干涉检测；原文既未给出干涉检查功能，也未给出任何间隙/过盈的量化判据。
- (d) 原文英文摘录：[未找到原句]（术语与功能句均缺失）
# 模块3：证据链（Evidence Chain）

## T1｜eDrawings 下载与安装步骤表（逐页）

||||
|---|---|---|
|0|*"Download eDrawings from the KC Software Center or Company Portal"*（页面标题）|SLIDE 48|标题句在 SLIDE 48 与 SLIDE 49 重复出现，属同一页的两帧|
|1|"Click the 'Start' button"|SLIDE 48（编号 1）||
|2|"Type 'Software Center' or 'Company Portal' in the search and open the app"|SLIDE 48（编号 2）|两个入口名并列|
|3|"Scroll down or use the search function to find 'eDrawings'"|SLIDE 48（编号 3）||
|4|"Click 'Install' and follow the instructions."|SLIDE 49（编号 4）||
|兜底|"If you are unable to find the app in the list, contact The DESK for help with installation."|SLIDE 49|唯一的故障路径|
|版本|软件中心可见：Dassault Systems eDrawings 2024（同列可见 Autodesk DWG Trueview 2025、JMP 18）|图像补充|版本号仅由图像确认|
|重申|"eDrawings can be used to view SolidWorks drawings. Download from Software Center."|SLIDE 63|Final thoughts 中再次确认来源|


统计：安装主步骤 4 步 + 兜底 1 条；叙述覆盖 2 页（48、49）+ 重申 1 页（63）。

## T2｜3D 查看器功能清单表

||||
|---|---|---|
|Components|列出全部零件；可逐级 drill down；左键高亮（列表+图形同步）；右键 Hide / Make Transparent / Hide Others (Isolate)|底部标签 Components → 左/右键零件|SLIDE 52、53、54；完整右键菜单（+ Show All / Isolate / Properties...）图像补充|
|Markup|添加批注：Text / Shapes / Dimensions / Images / Comments；Dimension 在两点/两面间加尺寸并落图|底部标签 Markup|SLIDE 55、56；示例值 749.000（图像补充）|
|Measure|量取尺寸，与 Dimension 同功能但不记录到图上；可测 points/lines 与 planes/surfaces|底部标签 Measure|SLIDE 57|
|Move|移动视图中的单个零件；两种选件方式；drag & drop|底部标签 Move（推断）→ 选中零件 → 拖放|SLIDE 58|
|Explode|分离零件以展示构造；滑块控制分离量|底部标签 Explode → 拖动 slider|SLIDE 59、60|
|Move 四工具（配合 Explode）|Free Drag / Position / Translate / Rotate 四种精度档|Explode 后调用 Move 工具|SLIDE 60|
|Section|剖切（标签存在，文本层无说明）|底部标签 Section|图像补充（标签栏）；功能说明 [未找到原句]|
|Annotations|注释（标签存在，文本层无说明）|底部标签 Annotations|图像补充；功能说明 [未找到原句]|
|Configurations|配置（标签存在，文本层无说明）|底部标签 Configurations|图像补充；功能说明 [未找到原句]|
|Playback（Play / Stop / Home / Previous / Next）|播放/停止/回主视角/上一/下一视图|底部标签左侧 5 个按钮|图像补充；功能说明 [未找到原句]|
|View Orientation|在常用视角间快速切换|（工具）|SLIDE 62|
|Normal To|旋转图形，正视当前选中的面/平面|选中面 → Normal To|SLIDE 62|
|Reset（撤销）|一键撤销所有零件移动与相机视角|空白处右键 → View → Reset|SLIDE 61、62|


统计：底部标签栏合计 11 个标签；其中文本层有功能说明的 = 5 个（Components / Markup / Measure / Move / Explode），仅图像确认、无文字说明的 = 6 个（Section / Annotations / Configurations / Play / Stop / Home… 归并为 3 个功能标签 + 5 个播放按钮）。

## T3｜文件导出流程表（DRCS → 下载 → eDrawings / DWG TrueView）

|||||
|---|---|---|---|
|① 找图（索引层）|在 The SPOT 查规格；图纸贴在规格末页|The SPOT|"Found on last page of specs from The SPOT"|SLIDE 63|
|② 定位（存储层）|完整图纸在 DRCS；DRCS 入口位于 Central CAD Homepage|DRCS|*"Full drawings in DRCS"；"Detailed product drawings are found in DRCS"*|SLIDE 63；Ch1 SLIDE 8|
|③ 判别来源|蓝色 'A' = AutoCAD；红色 'S' = SolidWorks|DRCS 图号标识|"A blue 'A' next to a drawing means it's an AutoCAD drawing. / A red 'S' next to a drawing means it's a SolidWorks drawing."|Ch1 SLIDE 16|
|④ 下载（原文无 "export" 术语）|"download the full SolidWorks file from DRCS"|DRCS → 本地|"You will need to download the full SolidWorks file from DRCS"|SLIDE 50|
|⑤ 打开方式 A|双击文件，选 eDrawings 为默认应用|eDrawings|"Either double-click the drawing file itself and select 'eDrawings' as the default application"|SLIDE 50|
|⑤ 打开方式 B|先开 eDrawings，再 File > Open|eDrawings|"Or open eDrawings first and use 'File > Open' to find and open the drawing you downloaded"|SLIDE 50|
|⑥ 结果|看到 3D 版本|eDrawings|"eDrawings will let you view the 3D version of drawings"|SLIDE 51|
|⑥′ AutoCAD 支路|AutoCAD 图纸改用 DWG TrueView 打开（文本层未给出其打开步骤）|DWG TrueView|"DWG TrueView can be used to view AutoCAD drawings. Download from Software Center."|SLIDE 63|


术语纪律：export 全材料检索 0 次；流程中的"导出"实为 download（SLIDE 50）。DWG TrueView 支路在本章只有一句定位性描述，无步骤页（SLIDE 63）。

下载样例（图像补充）：C153-FPS-01776-01.sldasm（4.42 MB）from cadkc.com —— 这是全材料中唯一给出的 3D 文件体积数据点。

## T4｜文件格式与工具对应关系表

|||||
|---|---|---|---|
|.sldasm|"3D Assembly drawing"|eDrawings|扩展名定义 + "download the SolidWorks file and open in eDrawings"|SLIDE 50|
|.sldprt|"3D Part drawing"|eDrawings|同上|SLIDE 50|
|.slddrw|"SolidWorks Drawing"|eDrawings（推断）|仅出现于文件对话框的文件类型列表（图像补充）；原文未说明用何工具打开|图像补充|
|TIF Image (*.tif)|位图|图像查看器（未指明）|仅出现于文件对话框列表；原文未说明用何工具打开|图像补充|
|AutoCAD 图纸（dwg 系）|AutoCAD drawing（蓝色 'A'）|DWG TrueView|"DWG TrueView can be used to view AutoCAD drawings."|SLIDE 63；标识见 Ch1 SLIDE 16|
|SolidWorks 图纸（sld 系）|SolidWorks drawing（红色 'S'）|eDrawings|"eDrawings can be used to view SolidWorks drawings."|SLIDE 63；标识见 Ch1 SLIDE 16|
|规格文档（Word/spec）|规格书，图纸贴末页|The SPOT 下载|"Found on last page of specs from The SPOT"|SLIDE 63|


三工具分工（原文可证）

||||
|---|---|---|
|SolidWorks|创作端（建模/改图）|受控授权；APPLICATIONS 标注 "K-C Internal - North & South America Only"|Ch1 SLIDE 16；Ch5 图像补充|
|eDrawings|查看端（SolidWorks 系）|Software Center / Company Portal 自助安装（eDrawings 2024）|SLIDE 48、49、63|
|DWG TrueView|查看端（AutoCAD 系）|Software Center 自助安装（DWG Trueview 2025）|SLIDE 63；图像补充|


Interference check 位置：[未找到原句] —— 无任何文件类型/工具与该能力绑定。

## T5｜常见操作与动作路径表

||||
|---|---|---|
|高亮定位零件|"Left-clicking a part will highlight it in the list as well as in the drawing itself."|SLIDE 53|
|隐藏零件|右键零件 → Hide|SLIDE 54|
|透视零件|右键零件 → Make Transparent|SLIDE 54|
|隔离零件|右键零件 → Hide Others (aka – Isolate)|SLIDE 54|
|显示全部 / 属性|右键菜单 → Show All / Isolate / Properties...（仅图像确认）|图像补充|
|移动零件（选件方式 1）|"Clicking the part itself with the 'move' cursor" → drag & drop|SLIDE 58|
|移动零件（选件方式 2）|"Select the 'move' cursor and then highlight the part(s) you wish to move in the components list" → drag & drop|SLIDE 58|
|分离装配体|拖动 slider："Use the slider to separate individual components."|SLIDE 59|
|精确定位已分离零件|Free Drag / Position / Translate / Rotate|SLIDE 60|
|撤销一切（移动+视角）|空白处右键 → View → Reset|SLIDE 61、62|
|切换常用视角|View Orientation 工具|SLIDE 62|
|正视选中面|Normal To — "will rotate the drawing to look down on the face/plane you currently have selected"|SLIDE 62|
|打开文件的第二条路|File > Open|SLIDE 50|


键盘快捷键：[未找到原句] —— shortcut / Ctrl+ / hotkey 在全材料检索 0 次；本表全部为鼠标/界面动作路径。

# 模块4：章节间衔接（Chapter Connections）

## M4-1｜与 Ch3（Editing Drawings, SLIDE 35–46）：变更（redline）之后在 3D 中验证的流程闭环

||||
|---|---|---|
|谁来改|"Product drawing edits are handled through Jacobs Engineering" Ch3 SLIDE 36|查看器不改图（Ch4 无 save/edit 出口）|改图权外置、看图权内置，二者天然分离|
|改什么 / 载体|Redline Template FORM-48129（in EtQ）+ 三色语义 Green=Replace / Blue=Revise / Peach=New Ch3 SLIDE 37|—|变更意图在 2D 上表达|
|判定规则|"Before revising a drawing make sure you are OK that all Parents of the drawing will receive the change." Ch3 SLIDE 37|Components 面板可 drill down 查看父/子装配关系 SLIDE 52|3D 的零件树 = 判断"Parents 影响域"的可视化工具【推断，非原文】|
|成本|*"General rule of thumb for 'Estimated Hours' is 8 hrs per drawing to be created/revised."* Ch3 SLIDE 44|自查成本≈0（Reset 可逆、Measure 不落图）|先在 3D 里自查、再发 redline，可压低 8 hrs/张的返工次数【推断，非原文】|
|改完如何验证|改完回流 DRCS（Ch5 SLIDE 67 的 Checker/Approver 路由）|"You will need to download the full SolidWorks file from DRCS" → 用 eDrawings 打开 SLIDE 50|验证动作 = 重新下载 + 重新打开|
|闭环是否原文写明|—|—|[未找到原句]：Ch4 未出现 "verify the redline in 3D" / "check the change in eDrawings" 之类表述。"下载 → 打开 → 看"的机制是原文的，但用它做变更验证是本报告的归纳|


闭环要点（本报告归纳，非原文）：KC 的变更闭环实为 2D 提出（FORM-48129 redline）→ 外部执行（Jacobs，8 hrs/张）→ DRCS 回流 → 3D 复核（download .sldasm + eDrawings）。其中前两步有明确的工时与责任人，第四步无任何量化指标、无强制要求——这是流程上的薄弱环节，也是本方可补的管理动作（见模块 5 / 连接点 3）。

## M4-2｜与后章 Ch5（DRCS Access, SLIDE 67–80）：查看 3D 所需的权限等级

||||
|---|---|---|
|查看 3D（下载 .sldasm 并在 eDrawings 打开）|View|*"Place check 'View', 'Work', & 'Approve' square boxes."*（三档并列，View 为最低档）|Ch5 SLIDE 73|
|编辑 / 新建图纸|Work|同上；角色表中 Staff Global Engineer / Staff Engineer 等持 View, Work|Ch5 SLIDE 73 + 图像补充角色表|
|批准发布|Approve|同上|Ch5 SLIDE 73|
|研究岗可拿到的等级|Research (Staff) | Global | Sector Drawings | View —— 只有 View|角色-权限表|Ch5 图像补充（Step 2 页）|
|其他仅 View 的角色|Engineer（Regional / North America）、Maintenance（Plant）、Process Engineer (Regional)（Plant 与 Regional 两行）|角色-权限表|Ch5 图像补充|
|授权依据|*"Access is based on: Work Role, Business Sector, Reporting Work Location."*|Step 2 声明|Ch5 图像补充|
|创作端区域限制|"SolidWorks (K-C Internal - North & South America Only)"|APPLICATIONS 列表|Ch5 图像补充|
|Ch4 自身是否谈权限|—|[未找到原句]：Ch4 全文未出现 permission / access / View 等权限表述；仅 SLIDE 63 把 "DRCS Access" 列为四大主题之一，SLIDE 66 以 "Getting Access to Drawings" 过渡到 Ch5|SLIDE 63、66|


结论（本报告归纳）：看 3D 的门槛 = DRCS View 权限 + 本地装一个免费查看器；创作端（SolidWorks）才受区域与授权限制。这条不对称性，正是"把 3D 查看下沉到非工程岗"在制度上可行的原因。

## M4-3｜与前章 Ch2（Reading Drawings, SLIDE 20–34）：3D 视图与 2D 图纸视图的互补

|||||
|---|---|---|---|
|外形 / 平铺尺寸|Overhead View — *"Shows the product laid out flat with a top-down view of the body-facing side…"；"This view holds dimensions the operators will be checking most frequently."*|Measure（points/lines/planes/surfaces，不落图）SLIDE 57|2D 给权威尺寸，3D 给任意尺寸；产线仍以 2D 为准|Ch2 SLIDE 22；SLIDE 57|
|层序 / 胶路|Cross Section — 图纸标题 "CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT"|Make Transparent SLIDE 54；Section 标签（图像补充，无文字说明）|2D 是固定剖切位置的示意，3D 可任意位置/任意角度剖切并透视|Ch2 SLIDE 23–24（图像）；SLIDE 54|
|局部细部|Detail View(s) Ch2 SLIDE 25|Markup > Dimension（落图）+ Normal To 正视选中面 SLIDE 56、62|2D 细部图是制图者选的；3D 可自查者自选细部并留痕|Ch2 SLIDE 25；SLIDE 56、62|
|物料清单|Bill of Materials（静态表格；C153-FPS-01575 样例 11 行子件）Ch2 SLIDE 27、33–34|Components 面板：全零件列表 + drill down + 左键双向高亮 SLIDE 52–54|同一份 BOM，3D 版可点击、可定位、可显隐|Ch2 SLIDE 27；SLIDE 52–54|
|装配关系 / 爆炸|[未找到原句] —— Ch2 六件套视图中没有 Exploded view|Explode slider + Move 四工具 SLIDE 59–60|3D 独占：2D 图纸体系不含爆炸图|Ch2 SLIDE 21–32；SLIDE 59–60|
|Front / Top / Side 三视图|[未找到原句] —— Front view、Side view 全材料未出现；Top view 仅以副词短语 "top-down view" 出现，非独立 named view|View Orientation（常用视角切换）+ Normal To（自动正视）SLIDE 62|3D 用"自由视角"替代了传统三视图；这是薄型柔性叠层产品的制图范式|Ch2 SLIDE 22；SLIDE 62|
|图框 / 版本 / 签发|Title Block（位于图纸右下角）Ch2 SLIDE 31；Notes / Ref(s) Ch2 SLIDE 29|[未找到原句] —— eDrawings 未见标题栏/版本信息相关功能说明|2D 独占：3D 不承载版本与签发信息，版本权威仍在 DRCS/图纸|Ch2 SLIDE 29、31|


互补结论：KC 的完整表达体系 = 2D 三件套（Overhead + Cross Section + Detail View）+ 1 个数据表（BOM）+ 2 个文本区（Notes/Refs + Title Block）+ 3D 交互层（Components / Explode / Measure / Markup）。3D 层补足了装配关系与任意量测，但不替代 2D 的尺寸权威与版本权威——SLIDE 57 那句 "the dimensions won't be recorded on the drawing" 就是这条边界的技术表达。

# 模块5：业务连接点（Business Connections）


业务背景：卫材（纸尿裤/湿巾）创新研发 + 木浆与纸品战略采购

## 连接点 1｜3D 查看能力下沉到非工程岗（Democratizing 3D viewing）

涉及幻灯片：SLIDE 48、49、50、63；权限侧 Ch5 SLIDE 73 + Ch5 图像补充

核心概念：eDrawings（下载与安装）｜DWG TrueView｜Software Center 自助安装｜The DESK 兜底｜DRCS View 权限｜.sldasm / .sldprt

关键数据
| 数据 | 数值 | 来源 |
|---|---|---|
| 查看器数量 | 2（eDrawings 管 SolidWorks、DWG TrueView 管 AutoCAD） | SLIDE 63 |
| 安装步骤 | 4 步 + 1 条兜底 | SLIDE 48–49 |
| 版本 | eDrawings 2024；DWG TrueView 2025 | 图像补充 |
| 安装入口 | KC Software Center 或 Company Portal 双入口 | SLIDE 48 |
| 故障路径 | 找不到应用 → 联系 The DESK | SLIDE 49 |
| 典型 3D 文件体积 | 4.42 MB（C153-FPS-01776-01.sldasm，from cadkc.com） | 图像补充 |
| 最低权限档 | View（三档 View / Work / Approve 中最低） | Ch5 SLIDE 73 |
| 研究岗权限 | Research (Staff) → View | Ch5 图像补充 |
| 创作端区域限制 | "SolidWorks (K-C Internal - North & South America Only)" | Ch5 图像补充 |
| 授权依据 | Work Role / Business Sector / Reporting Work Location | Ch5 图像补充 |

对本方跨部门协作的意义
KC 的做法把"能不能看图"与"会不会用 CAD"彻底解耦：查看器从内部软件中心自助安装（SLIDE 48–49），权限最低到 View（Ch5 SLIDE 73），而创作端 SolidWorks 反而有区域限制（Ch5 图像补充）。这意味着：一个采购或质量岗同事，可以在不申请 CAD 授权、不依赖工程部排期的前提下，自己打开装配体看结构。对木浆与纸品战略采购而言，这直接消掉了"要看一张吸收芯体层序图必须等工程师导出截图"的等待成本。

可执行行动建议
1. 建立"只读查看岗"标准包：为本方采购、质量、市场岗统一配置 eDrawings + DWG TrueView 两个查看器，走内部软件分发渠道自助安装；不申请 CAD 创作端授权（KC 亦只对创作端设限，Ch5 图像补充）。
2. 权限最小化申请：只勾选 View（Ch5 SLIDE 73 三档中的最低档）；Work / Approve 一律不申请，避免越权与审计风险。
3. 版本锁定：在内部 IT 标准里写死版本号（KC 现役为 eDrawings 2024 / DWG TrueView 2025，图像补充），避免各岗版本漂移导致文件打不开。
4. 预设故障路径：照搬 KC 的兜底设计——装不上/搜不到时统一联系一个支持台（KC 为 The DESK，SLIDE 49），不要让各岗自行摸索。
5. 区域风险预案：若本方团队位于 KC 标注的 North & South America 之外，应优先争取查看器而非创作端；同时确认本方 PLM 是否有同等区域条款。
6. 文件传输可行性：4.42 MB 的装配体样例（图像补充）说明常规邮件/IM 即可传递，无需专用传输通道；但外发须先过保密评估（见连接点 2 的边界条款）。
7. 培训极简化：培训内容只需 4 条——安装 4 步（SLIDE 48–49）、下载并打开（SLIDE 50）、Components 左键高亮（SLIDE 53）、Reset 撤销（SLIDE 61）。Reset 的存在使"放心乱点"成为可承诺的用户体验。

## 连接点 2｜Markup 批注能力用于供应商沟通（Supplier communication via Markup）

涉及幻灯片：SLIDE 55、56、54、57、61；边界条款 Ch3 SLIDE 36/43、Ch5 图像补充（Step 2 保密声明）

核心概念：Markup（Text / Shapes / Dimensions / Images / Comments）｜Dimension（落图留痕）vs Measure（不落图）｜Hide Others (Isolate)｜Reset｜DRCS 版本权威

关键数据
| 数据 | 数值 | 来源 |
|---|---|---|
| Markup 标注类型 | 5 类：Text / Shapes / Dimensions / Images / Comments | SLIDE 55 |
| 落图留痕的子类型 | 1 类（Dimension） | SLIDE 56 |
| Dimension 的量测对象 | 两点 / 两面之间 | SLIDE 56 |
| 示例标注值 | 749.000（红色显示） | 图像补充 |
| 隔离方式 | Hide Others (aka – Isolate) | SLIDE 54 |
| 撤销 | 右键空白处 → View → Reset | SLIDE 61–62 |
| 正式变更通道 | Jacobs Engineering + FORM-48129 | Ch3 SLIDE 36、43 |
| 正式变更工时 | 8 hrs / 张 | Ch3 SLIDE 44 |

对供应商沟通的意义
Markup 的 Images + Comments 组合使"在 3D 上直接圈出问题"成为可能：研发把 .sldasm 打开、用 Hide Others (Isolate) 隔离到单一零件（SLIDE 54）、加 Text/Shapes 圈注、截图发出——比"第 3 层第 2 个零件疑似偏位"这类文字描述歧义小得多。Dimension（SLIDE 56）适合需要留档的技术确认，因为它落图；Measure（SLIDE 57）适合供应商临时核对，因为它不污染图纸。

可执行行动建议
1. 建立"3D 截图 + Markup 批注"的供应商沟通模板：固定为「整装视角 1 张 + Isolate 后局部 1 张 + Dimension 标注 + Comments 文字说明」，用 Markup 的 Images 能力把批注直接烧进图里（SLIDE 55）。
2. 先隔离、再标注：任何单点问题，先 Hide Others (aka – Isolate)（SLIDE 54），避免供应商在多零件重叠视图中误判位置。
3. 按"是否需留档"选择工具：需要对方书面确认的尺寸 → 用 Dimension（落图，SLIDE 56）；只是让对方核对 → 用 Measure（不落图，SLIDE 57）。这条纪律应写进供应商沟通 SOP。
4. 明确边界：Markup ≠ 变更指令。KC 的正式变更必须走 Jacobs Engineering + FORM-48129 redline（Ch3 SLIDE 36、43），Ch4 的 Markup 没有任何发布出口（[未找到原句]：Ch4 无 submit/release 类表述）。因此供应商的回标只能作为 redline 的输入素材，不能作为生产依据——这一点必须在与供应商的往来函件中写明。
5. 保密前置评估：KC 的 Step 2 声明原文 *"Creating Product Engineering drawings is K-C confidential information. Distribution must be limited, even with your manager, to your work role access requirements."*（Ch5 图像补充）。本方外发 3D 文件时，建议优先外发截图/导出的标注图，而非 .sldasm 原生文件；确需外发原生文件时，走签署过的 NDA + 一次性链接 + 到期失效。
6. 压低变更成本：Ch3 SLIDE 44 给出 8 hrs/张的变更工时。若结构变更在发出 redline 前已用 3D + Markup 与供应商对齐，可显著减少"改完发现理解不一致"的二次返工——8 hrs/张 × 返工次数就是这笔投入的量化收益口径。

## 连接点 3｜测量 / 剖切用于竞品实物反演的对照验证（Measure & Section for competitive teardown cross-check）

涉及幻灯片：SLIDE 57（Measure）、SLIDE 56（Dimension）、SLIDE 60（Explode + Move 四工具）、SLIDE 62（View Orientation / Normal To）、SLIDE 54（Make Transparent）、图像补充（Section 标签）；对照基准 Ch2 SLIDE 33–34（BOM 尺寸）

核心概念：Measurement（不落图）｜Cross-section / Section｜Exploded view｜Normal To（正视减误差）｜Make Transparent｜BOM 尺寸作为对照基准

关键数据
| 数据 | 数值 | 来源 |
|---|---|---|
| Measure 可量测对象 | 4 类：points / lines / planes / surfaces | SLIDE 57 |
| Measure 是否留痕 | 否（*"the dimensions won't be recorded on the drawing"*） | SLIDE 57 |
| 减少斜视误差的手段 | Normal To（自动正视选中面/平面） | SLIDE 62 |
| 视角切换 | View Orientation（常用视角） | SLIDE 62 |
| 层序验证手段 | Make Transparent / Hide Others / Section | SLIDE 54；图像补充 |
| 2D 对照基准（样例） | LEG ELASTIC STRANDS 152MM FRONT / 173.1MM REAR（S1）；SURGE 100MM W × 236MM L | Ch2 图像补充（SLIDE 33–34） |

能力边界（必须先声明）
实物拆解无法得到竞品的原始 3D 数模——拆解只能得到物性量测值（克重、厚度、层数、拉伸、尺寸），无法还原对方的参数化模型、设计意图与公差体系。因此本连接点的正确用法是：用 Measure / Section 验证"自己的设计意图是否被自己的图纸和实物正确实现"，并与竞品实物量测值做同名项对照，而不是"反演竞品 3D"。这一边界在 KC 材料中亦无反例支撑（[未找到原句]：全材料无任何 reverse engineering / 3D scan / point cloud 相关表述）。

可执行行动建议
1. 先对齐术语与量测口径：以 Ch2 的 BOM 尺寸为对照基准（如 LEG ELASTIC STRANDS 前/后长、SURGE 宽 × 长、FLAP 高度，Ch2 图像补充），建立一张「设计值（2D BOM）／3D 量测值／竞品实物量测值」三列对照表，逐项同名比对。
2. 用 Normal To 消除读数误差：量取面到面/面到线距离前，先选中该面并调用 Normal To 正视（SLIDE 62），避免在斜视角下产生投影误差；配合 View Orientation 在常用视角间切换复核。
3. 用 Section + Make Transparent 验证层序：对照自家吸收芯体的层序与胶路布局，用 Make Transparent（SLIDE 54）与 Section 标签（图像补充）逐层比对自家 3D 与实物切片；与 Ch2 的 *"CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT"*（Ch2 SLIDE 24（图像））互证。
4. 用 Explode + Move 复现装配顺序：用 Explode slider 分离（SLIDE 59）、再用 Free Drag / Position / Translate / Rotate 四工具精确定位（SLIDE 60），把自家装配顺序录屏，作为与竞品拆解顺序对照的定性材料。
5. 强制转录纪律（关键）：Measure 不落图（SLIDE 57），读数只存在于屏幕上。凡需作为证据的量测值，必须当场手工录入对照表并注明量测对象类型（point/line/plane/surface）；若需留痕在图上，改用 Dimension（SLIDE 56）。不要把 Measure 读数当作可追溯记录。
6. 给管理层的表述模板：对外汇报应表述为「以 3D 量测与剖切验证自有设计意图，并与竞品实物做同名项对照」，不应表述为「反演竞品 3D 模型」——后者超出工具与实物证据的能力边界。
7. 可复用的量化口径：KC 给出的可回溯尺寸精度样例为 173.1MM（Ch2 图像补充，LEG ELASTIC STRANDS rear），说明设计值可到 0.1 mm 级；本方对照表的量测精度应至少匹配到 0.1 mm，否则对照失去意义。


# 模块6：金句索引（Key Quotes Index）

|||||
|---|---|---|---|
|1|"To view the 3D version of drawings you will need to download the SolidWorks file and open in eDrawings"|SLIDE 50|要查看图纸的三维版本，你需要下载 SolidWorks 文件并在 eDrawings 中打开。|一句话定义 3D 查看的前置条件：文件必须从 DRCS 下来，查看器必须本地装。是整章的枢纽句。|
|2|"You will need to download the full SolidWorks file from DRCS"|SLIDE 50|你需要从 DRCS 下载完整的 SolidWorks 文件。|强调 full（完整）——不能只下图纸页。DRCS 是 3D 的唯一源头。|
|3|".sldasm = 3D Assembly drawing / .sldprt = 3D Part drawing"|SLIDE 50|.sldasm = 三维装配图；.sldprt = 三维零件图。|全材料唯一的 3D 扩展名词典。与 Ch1 的 FPM/FP1/FPS 层级直接对应。|
|4|"Left-clicking a part will highlight it in the list as well as in the drawing itself."|SLIDE 53|左键点击一个零件，会同时在列表和图形中高亮它。|定义了 Components 的双向联动，这是 3D 胜过 2D 静态 BOM 的核心机制。|
|5|"Right-clicking a part will open an additional set of options including: Hide / Make Transparent / Hide Others (aka – Isolate)"|SLIDE 54|右键点击零件会打开一组附加选项，包括：隐藏 / 设为透明 / 隐藏其他（亦称隔离）。|Make Transparent + Isolate 是 2D 图纸完全做不到的两种"透视"，也是剖切验证层序的替代路径。|
|6|"The measuring tool works the same as the dimension tool, only the dimensions won't be recorded on the drawing"|SLIDE 57|测量工具与尺寸工具功能相同，只是尺寸不会被记录到图纸上。|全章信息密度最高的一句：用"是否留痕"区分 Measure 与 Dimension，是一处刻意的治理设计，也是业务使用的纪律红线。|
|7|"You can measure between points/lines and/or between planes/surfaces"|SLIDE 57|你可以在点与点/线与线之间，以及/或者平面与平面/曲面与曲面之间测量。|给出量测对象的完整枚举（4 类），是竞品实物对照时选取量测基准的依据。|
|8|"Free Drag = Used for quick drag & drop movement. / Position = Used for precise movement or rotation along a particular axis. / Translate = Used for precise movement along an axis. / Rotate = Used for precise rotation along an axis."|SLIDE 60|Free Drag 用于快速拖放移动；Position 用于沿特定轴的精确移动或旋转；Translate 用于沿轴精确移动；Rotate 用于沿轴精确旋转。|四种精度档的完整定义，且暗示 Position 是唯一同时支持移动与旋转的。爆炸图定位的操作依据。|
|9|"The Explode section will let you separate individual parts to better show how the product is constructed"|SLIDE 59|Explode 分区可以让你分离各个零件，更好地展示产品是如何构成的。|3D 层独占的能力（Ch2 的 2D 视图体系中没有爆炸图），也是 KC 用 3D 交互替代 2D 爆炸图的设计选择。|
|10|"You can undo any part movements or camera angles at any time by right-clicking in open space, clicking 'View', clicking 'Reset'"|SLIDE 61|你可以随时撤销任何零件移动或相机视角：在空白处右键，点击 View，再点击 Reset。|Reset 是"允许非专业岗随意操作"的安全网，也是把 3D 下放给采购/质量/市场岗的管理前提。|
|11|"The 'Normal To' view will rotate the drawing to look down on the face/plane you currently have selected."|SLIDE 62|Normal To 视图会旋转图纸，使你正视当前选中的面/平面。|减少斜视投影误差的唯一原文手段；做精确量测/竞品对照前应先 Normal To。|
|12|"eDrawings can be used to view SolidWorks drawings. Download from Software Center. / DWG TrueView can be used to view AutoCAD drawings. Download from Software Center."|SLIDE 63|eDrawings 可用于查看 SolidWorks 图纸，从 Software Center 下载；DWG TrueView 可用于查看 AutoCAD 图纸，从 Software Center 下载。|双查看器拓扑的完整表述，且两处都点明"从软件中心下载"——零授权成本、自助获取，是能力下沉的制度依据。|
|13|"If you are unable to find the app in the list, contact The DESK for help with installation."|SLIDE 49|如果你在列表中找不到该应用，请联系 The DESK 获取安装帮助。|全章唯一的故障路径句。任何自助安装体系都必须预设兜底支持通道，本方复制时应照搬。|
|14|"It's confusing; I'm sorry. Step-by-step instructions are in the appendix."|SLIDE 63|这确实容易让人困惑，抱歉。逐步操作说明在附录里。|演讲者的自我坦白：KC 自己的图纸体系存在真实的认知成本。提醒本方选型时以"统一入口、后台分离"为目标，别把系统割裂暴露给终端用户。|


## 附：本章检索缺口清单（Terminology Gap Register）

||||
|---|---|---|
|export / Exporting Drawings|0 次|全材料（Ch1–Ch5）无此术语；实际动作为 download SLIDE 50|
|interference / Interference check|0 次|全材料无此术语与功能|
|字面 .dwg|0 次|仅 DWG TrueView 工具名含 DWG（SLIDE 63、图像补充）|
|shortcut / Ctrl+ / hotkey|0 次|无键盘快捷键；全为鼠标/界面动作路径|
|Section（eDrawings 剖切）功能说明句|[未找到原句]|标签名由图像补充确认；无任何文字定义或步骤|
|Annotations / Configurations 说明句|[未找到原句]|同上，仅标签名|
|Ch4 中的权限（permission / access level）表述|[未找到原句]|仅 SLIDE 63 列出 "DRCS Access" 主题名、SLIDE 66 过渡到 Ch5|
|"用 3D 验证 redline 变更"的明文流程|[未找到原句]|机制（下载→打开）为原文，"用于变更验证"为本报告归纳|

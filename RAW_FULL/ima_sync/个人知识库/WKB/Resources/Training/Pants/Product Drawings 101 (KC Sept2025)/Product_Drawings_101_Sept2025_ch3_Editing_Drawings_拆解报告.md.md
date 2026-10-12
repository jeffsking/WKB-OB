---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_759ec0ddda7ac7fbadfff67d4ee0fc08001a693ee6c0644e"
source_file: "Product_Drawings_101_Sept2025_ch3_Editing_Drawings_拆解报告.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch3_Editing_Drawings_拆解报告.md.md"
extracted: "2026-09-30"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
---

# Product_Drawings_101_Sept2025_ch3_Editing_Drawings_拆解报告.md


章节：Ch3 Editing Drawings ｜ 覆盖幻灯片：35–46 ｜ 文档：Product Drawings 101 (KC, Sept 2025) ｜ 拆解日期：2026-08-30

## 阅读说明与证据规则

|||
|---|---|
|证据来源|章节文件文本层（幻灯片文本 + 演讲者备注）＋文件末尾「图像内容补充（逐页渲染读图确认）」区块，二者均视为可靠来源|
|引用标注|所有观点后附 SLIDE N；跨章引用附 ChN SLIDE N|
|缺失标注|原文无对应表述处标 [未找到原句]；属本报告推断而非原文者，明确标「【推断，非原文】」并给出推断所依据的原文条目|
|数据纪律|所有加粗数字均可回溯至原文；工时推算类数字一律标注为「推算值」并列出假设|
|语言|模块 1–5 正文与定义保留英文原文；模块 6 金句附中文翻译|


本章幻灯片清单（用于核对覆盖完整性）：SLIDE 35（章节封面）／36（Jacobs 承接 + FORM-48129）／37（空白 Redline 模板）／38（已填模板 v1，Blue 修订）／39、40（红线圈注文字）／41（New 判定规则）／42（模板 v2，Peach 新建）／43（提交流程）／44（工时 + 批准人）／45（批准矩阵）／46（Drawing Checkers 名单，标题自带 "Needs updating"）。

# 模块1：核心论点（Core Arguments）

### A1｜Drawing edits are outsourced, not performed in-house — the internal deliverable is a redline, not a revised drawing.

英文概括：KC 内部人员不直接改图。Product drawing edits 全部由外部工程服务商 Jacobs Engineering 承接；内部角色（product developer / "submitter"）的交付物是「redlined drawings + 封面页模板」，通过 Jacobs Engineering Request Form 提交。

支撑依据：
- SLIDE 36：*"Product drawing edits are handled through Jacobs Engineering"；"Go to the Jacobs Engineering Request Form"；"Fill out the form and attach your redlined drawings"*
- SLIDE 43：*"Submit redlines through Jacobs Engineering to update drawings"；"Go through the form and fill out applicable sections"；"Attach redlined drawings"*
- 交接责任人有名有姓：Ch5 SLIDE 67 "Sara Schewe is in the loop and remains the Jacobs contact."

可验证推论：改图的前置周期 = 内部 redline 制作时间 + Jacobs 排队/执行时间，其中只有后者被量化（见 A4）。[未找到原句]：Jacobs 的 SLA / 排队时长原文未给出。

### A2｜Redlining is a form-governed act, not freehand markup — the unit of control is the FORM-48129 cover page with a color-coded impact matrix.

英文概括：Edits 必须落在标准化载体 Product Drawings Redline Template (FORM-48129, Rev.0, in EtQ) 上。该模板把一次变更强制拆成三层结构化信息：(i) ER# + Change Description 的封面识别信息；(ii) 一张 Product Description / FPS or PDD / C153-FP1 / C153-FPM / Comments 五列影响矩阵；(iii) 五条强制 Notes 规则。

支撑依据：
- SLIDE 36："Use the Product Drawings Redline Template (FORM-48129 in EtQ) to capture the edits you would like made"
- SLIDE 37／SLIDE 38：模板表头 + FORM-48129 Rev.0 页脚；"Actual detailed redlines follow this cover page."
- SLIDE 37 Notes 五条（原文见模块 3 / T2）

可验证推论：模板把「我改了什么」翻译成「哪些图受影响、以什么方式受影响」——这是下游工时估算（8 hrs/drawing）与批准路由（Checker/Approver）的唯一输入。

### A3｜The single intellectual decision in a redline is Replace (Green) vs Revise (Blue) vs New (Peach), and the decision rule is parent-scope: if not all Parents should receive the change, it must be a New drawing.

英文概括：颜色不是装饰，是变更语义。三色映射三种图纸生命周期动作；判定依据不是"改动大小"，而是父图（Parents）影响域是否可接受。

支撑依据：
- 颜色约定：SLIDE 37 Green = Replace Drawing / Blue = Revise Drawing / Peach = New Drawing
- 判定规则（原文决定性两句，均 SLIDE 37）：
  - "Before revising a drawing make sure you are OK that all Parents of the drawing will receive the change. If not, the change should be a new drawing change."
  - "Before making a new or revising a drawing make sure the changes/drawing you need does not already exist, utilize the replacement option."
- 独立重述：SLIDE 41 "New drawings are required if the drawing you wish to edit is being used somewhere else that your edit(s) wouldn't apply to."

可验证推论：本规则在真实案例 ER# 900200005649 中被现场执行并反转了方案（Revise → New），见 A5 与模块 3 T4。

### A4｜Change execution carries a hard, quantified cost floor of 8 hrs per drawing created/revised, and a two-gate (Checker → Approver) control that tightens sharply at the FPS level.

英文概括：SLIDE 44 给出唯一的硬量化指标：*"General rule of thumb for 'Estimated Hours' is 8 hrs per drawing to be created/revised."* 批准侧采用 Checker / Approver 双角色分离：M 与 FP1/FP2 两级由 Product Developer 自查自批；FPS 级必须双人 Check（submitter + fellow senior product developer）后由 Approver 放行。

支撑依据：
- 工时：SLIDE 44、重申于 SLIDE 45
- 角色：SLIDE 44 *"Product developers or 'submitters' of SolidWorks drawing changes are the approvers for FPM and FP1 drawings."；"Completed FPS drawings are checked by the submitter and a fellow senior product developer."*
- 矩阵：SLIDE 45（见模块 3 T3）
- 工单字段（图像补充 p43–45）：Scope of the request / Description of work / Status / Estimated Hours / Revised Estimated Hours / Status Comments / DRCS Checker/Approver / DRCS Approver —— 注意存在 Estimated Hours 与 Revised Estimated Hours 双字段，说明首估可被调用方修订

可验证推论：变更成本在提交前即可由「图纸张数 × 8」下界估计；"Revised Estimated Hours" 字段的存在意味着 8 hrs 是预算基准而非封顶价。[未找到原句]：Jacob 实际偏差率未给出。

### A5｜The governance system is visibly mid-transition: a role-based approval matrix coexists with a person-based single approver, and the supporting checker roster is self-flagged as stale.

英文概括：本章同时存在两套互斥表述——SLIDE 45 矩阵把 FPS 批准权赋予角色 "Senior Quality Engineer"，而 SLIDE 44 把同一权力归于个人 "Rex Stuart is the only one who can approve a completed FPS drawing."；SLIDE 46 的支撑名单标题直接写着 "List of Drawing Checkers – Needs updating"，且多条记录 Backup 为空。

支撑依据：
- SLIDE 44 vs SLIDE 45 矩阵（"Senior Quality Engineer" 列）
- SLIDE 46 标题原文 *"List of Drawing Checkers – Needs updating"*；名单中 Sara Rosack／Erica Mullen（Occasions、Retailer、Pants-Occasions、Pants-Retailer Branded）Backup 列为空
- 切换期旁证（跨章）：Ch5 SLIDE 67 "What will be new: For the new SolidWorks product drawings product developers will be the approvers of diaper part 'FPM' and sub-assemblies 'FP1' within DRCS. This gives product developers more control and speed within the process." ／ "What remains the same: For final FPS drawings product developers will remain a checker. Rex Stuart of Quality remains the Approver for FPS drawings supporting production."

可验证推论（体系切换期判定）：FPM/FP1 批准权已从 Quality 下放至 Product Developer（新状态），而 FPS 批准权仍锁在 Quality（旧状态），且当前落到单一自然人。这构成本章最显著的组织脆弱点（详见模块 5 连接点 4）。

# 模块2：关键概念操作化定义（Operational Definitions）



定义体例：(a) 中文名 + English term；(b) English definition；(c) 操作化定义（判定式 / 测量维度 / 量化指标）；(d) 原文英文摘录 + SLIDE N。
标注 定义原文未直接给出 者，其 (b) 为基于所引 SLIDE N 的归纳定义，非原文句子。

### 概念 1｜红线圈注（Redline / Redlined Drawing）

(a) 中文名：红线圈注（变更标注图）｜English term: Redline / Redlined Drawings

(b) 英文定义（定义原文未直接给出，归纳自 SLIDE 36/37/43）：A mark-up of an existing drawing that visually captures the edits a requester wants made to it, produced by the submitter and attached to a formal request so that a third party (Jacobs Engineering) can execute the drawing change.

(c) 操作化定义：
- 载体判定：一份合规 redline 交付包 = ① FORM-48129 封面页（ER# + Change Description + 影响矩阵 + 颜色标注）＋ ② 详细圈注图纸本体
- 完整性判据：封面页存在页脚字段 FORM-48129 Rev.0；封面页含 Actual detailed redlines follow this cover page. 声明；影响矩阵中每一行 FPS/PDD 均已映射到 FP1 与 FPM 列
- 量化指标：影响矩阵的行数 = 受影响的 FPS/PDD 图纸数；每行的 FPM/FP1 单元格数 = 需 create/revise 的图纸数 → 直接喂给 8 hrs/drawing
- 不合格判据：仅有图纸圈注、无 FORM-48129 封面 → 按 SLIDE 36 表述属不完整

(d) 原文摘录：
- "Use the Product Drawings Redline Template (FORM-48129 in EtQ) to capture the edits you would like made" —— SLIDE 36
- "Fill out the form and attach your redlined drawings" —— SLIDE 36
- "Actual detailed redlines follow this cover page." —— SLIDE 37
- 圈注文字实例："Remove smaller holes in the front along with the associated dimensions." —— SLIDE 39、SLIDE 40

### 概念 2｜红线圈注模板 FORM-48129（Product Drawings Redline Template, FORM-48129）

(a) 中文名：产品图纸红线圈注模板（表单号 FORM-48129）｜English term: Product Drawings Redline Template (FORM-48129 in EtQ)

(b) 英文定义（部分原文）："the Product Drawings Redline Template (FORM-48129 in EtQ)" —— the standardized cover page used to capture requested drawing edits; current revision Rev.0; hosted in EtQ.

(c) 操作化定义：
- 版本判据：页脚字面值 = FORM-48129 Rev.0（SLIDE 37／SLIDE 38／SLIDE 42）
- 存放位置判据：必须取自 EtQ（FORM-48129 in EtQ，SLIDE 37），不得使用本地副本
- 结构判据：四区齐全 —— Header（Template / ER# / Change Description）＋ Color Code 图例（3 行）＋ 影响矩阵（5 列 × N 行）＋ Notes（5 条规则）＋ 页脚版本号
- 填写密度判据（原文明确）：*"A FPS or PDD drawing could have more than 1 FP1 or FPM drawing change."；"If the FPS or PDD drawing has more than one FP1 or FPM drawing change please add information to the next available row before going to the next FPS or PDD drawing."* —— 即同一 FPS/PDD 的多条子变更占多行，不得压缩到一行

(d) 原文摘录：
- "Use the Product Drawings Redline Template (FORM-48129 in EtQ) to capture the edits you would like made" —— SLIDE 36
- "FORM-48129 Rev.0" ／ "FORM-48129 in EtQ" —— SLIDE 37
- "A FPS or PDD drawing could have more than 1 FP1 or FPM drawing change." —— SLIDE 37

### 概念 3｜EtQ 与 ER#（EtQ change system / ER number）

(a) 中文名：EtQ 变更系统；变更请求编号（ER#）｜English term: EtQ; ER# (Engineering/Change Request number)

(b) 英文定义（定义原文未直接给出，归纳自 SLIDE 36/37/38/42）：EtQ is the system of record in which the Redline Template (FORM-48129) resides and from which a change carries its ER# identity; a single ER# binds one change across multiple drawing revisions and across iterations of the redline itself.

(c) 操作化定义：
- 唯一性判据：一个变更 = 一个 ER#。实例：ER# 900200005649 在 SLIDE 38（Revise 方案）与 SLIDE 42（New 方案）中保持同一编号，而 Change Description 被改写 —— 即 ER# 是变更的身份锚，不是方案版本的锚
- 追溯维度：ER# → Change Description → 影响矩阵行 → 具体图号 → Checker/Approver
- 可审计性指标：同一 ER# 下 Change Description 的改写次数 = 方案迭代次数（本例 ≥ 2 次）

(d) 原文摘录：
- "FORM-48129 in EtQ" —— SLIDE 37
- "ER# ␋ Change Description: XXX" —— SLIDE 37（空白模板）
- "ER# 900200005649 ␋ Change Description: Removal of Urine Management Zone (UMZ) apertures from 236mm and 276mm Cleanshield Surge drawings." —— SLIDE 38
- "ER# 900200005649 ␋ Change Description: Create new FPM drawings for 236mm and 276mm Cleanshield Surge with the Urine Management Zone (UMZ) apertures removed." —— SLIDE 42

### 概念 4｜颜色约定（Color Code Convention: Green = Replace / Blue = Revise / Peach = New）

(a) 中文名：受影响图纸颜色编码约定（绿=替换／蓝=修订／桃=新建）｜English term: Color Code for Impacted Drawings

(b) 英文定义（原文，逐条）：
- Green = Replace Drawing（Replacement Drawing；Drawing to be replaced with another）
- Blue = Revise Drawing（Revise Drawing；Drawing # to be redlined / Drawing # to be revised）
- Peach = New Drawing（New Drawing；"New - X" in cell）

(c) 操作化定义（判定式，可直接落地为 checklist）：

|||||
|---|---|---|---|
|1|我需要的图/改动是否已存在？|走 Green（Replace），不新建、不修订|进入判定 2|
|2|修订该图后，该图的全部 Parents 都应接收此变更吗？|走 Blue（Revise）：单元格填原图号|走 Peach（New）：单元格填 "New - X"|
|3|若走 Peach，序号 X 如何取？|同一封面上按出现顺序递增：New – 1、New – 2 …|—|


- 量化指标：一张封面页上 Peach 单元格个数 = 需新建的图纸数；Blue 单元格个数 = 需修订的图纸数；两者合计（＋Green 关联的替换图） = 工时估算基数 N
- 标注一致性判据：Peach 单元格必须同时满足"格子填 New - X"且"底色涂 peach"两个条件，缺一不可（SLIDE 37 第三条 Note / SLIDE 42 实例）
- 文本提取注意：SLIDE 37 表格文本层字面为 "Peach+"，图像补充读作 "Peach"；两者同义，+ 疑为表单符号残留，判定不受影响
(d) 原文摘录：
- "Green= Replace Drawing / Replacement Drawing / Drawing to be replaced with another" —— SLIDE 37
- "Blue= Revise Drawing / Revise Drawing / Drawing # to be redlined / Drawing # to be revised" —— SLIDE 37
- "Peach+ New Drawing / New Drawing / "New - X" in cell" —— SLIDE 37
- "If your change requires a new drawing please place "New Drawing - 1" in the cell and shade it peach." —— SLIDE 37
- 实例：单元格由 C153-FPM-00481（Blue 修订）→ New – 1（Peach 新建）—— SLIDE 38 → SLIDE 42

### 概念 5｜父图影响域（Parents / All Parents）

(a) 中文名：父图（上层装配/成品图）影响域｜English term: Parents (All Parents of the drawing)

(b) 英文定义（定义原文未直接给出，归纳自 SLIDE 37 + Ch1/Ch2）：A Parent is any higher-level drawing (FP1 assembly, FPS finished-product specification) that consumes the drawing being edited as a child component; a revision to a child propagates to all of its Parents.

(c) 操作化定义：
- 测量方法（系统可操作）：DRCS 图纸详情页的 "All Parents" 按钮（Ch1/Ch2 图像补充：按钮组 < Back / All Parents / All Children / Print / Help）—— 点开即得父图清单
- 判定式：设 P(child) = 父图集合，S = 本次变更应生效的父图集合。若 P(child) ⊄ S 之外的元素存在（即存在不应接收变更的父图）→ 必须 New；若 P(child) ⊆ S → 可 Revise
- 案例实测：SLIDE 38/SLIDE 42 中，一张 FPM（C153-FPM-00481）在本封面内已挂 5 张 FPS 父图（C153-FPS-01640 / 01641 / 01577 / 01574 / 01575）；另一张（C153-FPM-00479）挂 5 张（C153-FPS-01665 / 01667 / 01566?→原文 01666 / 01576 / 01642）。注意：这 10 张是"本封面已识别到的父图"，并非其全部父图 —— 全部父图须以 DRCS All Parents 为准
- 跨章实证：Ch2 图像补充 BOM_A（C153-FPS-01575-J-09 子件清单）第 7 行 = *"DIAPER, BCM, SMALL SURGE 100MM W, 236MM L | C153-FP1-00178-D-04"* —— 与本章 SLIDE 38 Row 1 的 FP1 列 C153-FP1-00178 完全对上，且父图 C153-FPS-01575 正在该行 FPS 列表中。这是"BOM 决定 redline 影响域"的可验证硬证据

(d) 原文摘录：
- "Before revising a drawing make sure you are OK that all Parents of the drawing will receive the change. If not, the change should be a new drawing change." —— SLIDE 37
- "New drawings are required if the drawing you wish to edit is being used somewhere else that your edit(s) wouldn't apply to." —— SLIDE 41

### 概念 6｜工时经验值 8 hrs/drawing（Estimated Hours rule of thumb）

(a) 中文名：单图工时经验值（每新建/修订一张图纸 8 小时）｜English term: Estimated Hours — 8 hrs per drawing to be created/revised

(b) 英文定义（原文）：*"General rule of thumb for 'Estimated Hours' is 8 hrs per drawing to be created/revised."*

(c) 操作化定义：
- 计算式：Estimated Hours = 8 × N，其中 N = 需 create 或 revise 的图纸张数（＝影响矩阵中 Peach 与 Blue 单元格总数，Green 替换按新图计入另议）
- 性质判定：表述为 "rule of thumb"（经验值/粗略估计），且工单同时存在 Estimated Hours 与 Revised Estimated Hours 两个字段 → 它是预算基准（baseline）而非合同封顶值
- 适用范围：适用于提交给 Jacobs 的 SolidWorks 图纸 create/revise 工时估算；[未找到原句] 是否包含内部 redline 制作时间、Checker/Approver 复核时间
- 不含项（原文未列入，不可擅自计入）：内部圈注时间、批准等待时间、验证时间、试产/库存处理时间

(d) 原文摘录：
- "General rule of thumb for 'Estimated Hours' is 8 hrs per drawing to be created/revised." —— SLIDE 44（SLIDE 45 全文重复同一句）
- 字段上下文：Scope of the request / Description of work / Estimated Hours / Revised Estimated Hours / Status / Status Comments / DRCS Checker/Approver / DRCS Approver —— 图像补充 p43–45

### 概念 7｜批准矩阵（Approval Matrix: Drawing Level × Checker × Approver）

(a) 中文名：图纸批准矩阵（图纸层级 × 检查人 × 批准人）｜English term: Approval Matrix / Drawing Level – Checker – Approver

(b) 英文定义（定义原文未直接给出，归纳自 SLIDE 45）：A three-column control table binding each drawing level (M / FP1·FP2 / FPS) to the role that must check it and the distinct role that must approve it, enforcing separation of duties at the finished-drawing level.

(c) 操作化定义：

|||||
|---|---|---|---|
|M (Part)|Product Developer|Product Developer|无分离（自查自批）|
|FP1 / FP2 (Sub-Assembly)|Product Developer|Product Developer|无分离（自查自批）|
|FPS (Final Drawing)|Product Developer & Senior Product Developer|Senior Quality Engineer|强分离（双人 Check + 跨职能 Approve）|


- 层级释义（跨章，Ch1 SLIDE 17–19）：FPM = Part / Detail（最小单元）；FP1 = Assembly（FPM 的分组，例：Nonwoven + Adhesive）；FPS = Finished Product Specification / Full Product（工厂实际使用的图）
- 术语不一致（须记录）：矩阵写 "M (Part)"，而 Ch1 的图纸类型体系用 "FPM – Part"；矩阵行标题写 "FP1 / FP2" 但 Ch1 SLIDE 17 仅定义 FPM/FP1/FPS（FP2 与 PDD/LPA/PSD/DOC 仅出现在 Ch1 SLIDE 17 演讲者备注缩写表）。判定：矩阵中的 "M" 应读作 FPM
- SoD 量化指标：Checker 人数（1 或 2）× 是否跨职能（Product Development vs Quality）
(d) 原文摘录：
- 矩阵三行（逐字）：*"M (Part) | Product Developer | Product Developer"；"FP1 / FP2 (Sub-Assembly) | Product Developer | Product Developer"；"FPS (Final Drawing) | Product Developer & Senior Product Developer | Senior Quality Engineer"* —— SLIDE 45
- 层级定义：*"FPM – Part / Detail — Smallest possible unit"；"FP1 – Assembly — Groupings of FPM drawings that are often associated together"；"FPS – Finished Product Specification — Drawing as would be used in the mill"* —— Ch1 SLIDE 17

### 概念 8｜Product Developer（FPM / FP1 批准人）

(a) 中文名：产品开发人员（同时为"提交人"，FPM 与 FP1 图纸的批准人）｜English term: Product Developer / "submitter"

(b) 英文定义（原文）："Product developers or "submitters" of SolidWorks drawing changes are the approvers for FPM and FP1 drawings."

(c) 操作化定义：
- 权限边界：对 M/FPM（Part） 与 FP1/FP2（Sub-Assembly） 两级，同时拥有 Checker 与 Approver 两顶帽子（自查自批，无 SoD）
- 对 FPS 的权限边界：仅为 Checker 之一（*"Completed FPS drawings are checked by the submitter and a fellow senior product developer."*），不拥有 Approver 权限
- 权限获取路径（跨章可操作）：需在 DRCS 访问申请中勾选 "Approve" 框 —— *"Place check "View", "Work", & "Approve" square boxes."*（Ch5 SLIDE 73）；请求 "will be routed to your manager for approval"（Ch5 SLIDE 74）
- 制度变更状态（跨章）：Ch5 SLIDE 67 "What will be new: ... product developers will be the approvers of diaper part 'FPM' and sub-assemblies 'FP1' within DRCS. This gives product developers more control and speed within the process." → 这是新授予的权力，非既有惯例
- 量化指标：单个 Product Developer 可闭环的图纸层级数 = 2／3（M + FP1/FP2，不含 FPS）

(d) 原文摘录：
- "Product developers or "submitters" of SolidWorks drawing changes are the approvers for FPM and FP1 drawings." —— SLIDE 44（SLIDE 45 重复）
- "What will be new: For the new SolidWorks product drawings product developers will be the approvers of diaper part "FPM" and sub-assemblies "FP1" within DRCS. This gives product developers more control and speed within the process." —— Ch5 SLIDE 67

### 概念 9｜Senior Quality Engineer（FPS 批准角色）

(a) 中文名：高级质量工程师（FPS 成品图纸的批准角色）｜English term: Senior Quality Engineer（matrix role for FPS approval）

(b) 英文定义（定义原文未直接给出，由 SLIDE 45 矩阵直接给出角色名）：The role designated as Approver for FPS (Final Drawing) level, after the drawing has been checked by both the submitter and a fellow Senior Product Developer.

(c) 操作化定义：
- 触发条件：Drawing Level == FPS（Final Drawing）
- 前置门禁（缺一不可）：① submitter（Product Developer）已 Check；② a fellow senior product developer（同级资深产品开发人员，非提交人本人）已 Check
- 与"Rex Stuart"表述的冲突（须显式记录）：SLIDE 45 矩阵写角色 "Senior Quality Engineer"；SLIDE 44 同一页上方的要点写个人 "Rex Stuart is the only one who can approve a completed FPS drawing." → 同一 FPS 批准权在同一张幻灯片内存在"角色表述"与"个人表述"两种说法
- 体系切换期判定：Ch5 SLIDE 67 明确 "What remains the same: ... Rex Stuart of Quality remains the Approver for FPS drawings supporting production." → 说明当前处于角色化制度尚未生效、个人授权仍在运行的切换期；本概念（角色）是目标态，SLIDE 44 的 Rex Stuart 是当前态
- 量化指标：FPS 批准链上的独立人数 = ≥ 3（submitter + senior PD + Quality approver）

(d) 原文摘录：
- 矩阵行："FPS (Final Drawing) | Product Developer & Senior Product Developer | Senior Quality Engineer" —— SLIDE 45
- "Completed FPS drawings are checked by the submitter and a fellow senior product developer." —— SLIDE 44
- 切换期旁证："What remains the same: For final FPS drawings product developers will remain a checker. Rex Stuart of Quality remains the Approver for FPS drawings supporting production." —— Ch5 SLIDE 67

### 概念 10｜Rex Stuart 单点批准（Single-point FPS approval）

(a) 中文名：Rex Stuart 单点批准（唯一 FPS 批准人）｜English term: Rex Stuart — the only approver of a completed FPS drawing

(b) 英文定义（原文）："Rex Stuart is the only one who can approve a completed FPS drawing."

(c) 操作化定义：
- 集中度指标：FPS 批准人基数 = 1（单一自然人），无备份（backup）
- 与批准矩阵的一致性检查：不一致 —— SLIDE 45 矩阵把 FPS 批准权归给角色 "Senior Quality Engineer"，SLIDE 44 归给个人 "Rex Stuart"。本报告判定：这是体系切换期（role-based 目标态 vs person-based 当前态）的证据，属同一页内并存的制度过渡现象，非笔误
- 交叉验证：Ch5 SLIDE 67 同时确认 Rex Stuart 属 Quality 职能且为"remains"（延续）事项 → 与矩阵角色"Senior Quality Engineer"职能一致，但粒度不同（人 vs 角色）
- 名单陈旧性佐证：SLIDE 46 标题自带 *"Needs updating"*，且名单中多条 Backup 列为空（Sara Rosack / Erica Mullen 的多个平台）→ 支撑性人事数据未与制度同步
- 风险量化维度：FPS 批准环节的单点故障概率 = 1（无冗余）；可用备份数 = 0

(d) 原文摘录：
- "Rex Stuart is the only one who can approve a completed FPS drawing." —— SLIDE 44（SLIDE 45 重复）
- "Rex Stuart of Quality remains the Approver for FPS drawings supporting production." —— Ch5 SLIDE 67
- "List of Drawing Checkers – Needs updating" —— SLIDE 46

### 概念 11｜UMZ apertures（Urine Management Zone apertures / 尿液中转区开孔）

(a) 中文名：尿液管理区开孔（UMZ 开孔；文中亦作 "smaller holes in the front"）｜English term: UMZ (Urine Management Zone) apertures

(b) 英文定义（定义原文未直接给出；原文仅给出位置与处理动作）：Openings/holes located in the front / urine management zone of the Cleanshield Surge layer, together with their associated dimensions; the change under ER# 900200005649 removes them.

(c) 操作化定义：
- 部位判据：位于 front（前部） 且属于 urine management zone（尿液管理区） —— 即产品纵向（MD）前段的液体管理区域
- 形态判据：原文称 "smaller holes"（较小的孔），与 Surge 层上其他（较大）孔并存 → 说明该 Surge 层至少有两档开孔规格
- 几何可交付判据：删孔同时必须删除 "the associated dimensions"（关联尺寸）—— 即删孔不是单纯删特征，而是连带删除其标注尺寸链
- 对象范围判据：适用于 236mm 与 276mm 两个长度的 Cleanshield Surge；100mm 宽度为两规格共有
- 变更动作判据：*"Remove apertures in the front / urine management zone."*（删除）

(d) 原文摘录：
- "Remove apertures in the front / urine management zone." —— SLIDE 38（Row 1、Row 2 Comments 列）、SLIDE 42（并入 Comments）
- "Remove smaller holes in the front along with the associated dimensions." —— SLIDE 39、SLIDE 40（红线圈注文字）
- "Removal of Urine Management Zone (UMZ) apertures from 236mm and 276mm Cleanshield Surge drawings." —— SLIDE 38（ER# Change Description）
- "Create new FPM drawings for 236mm and 276mm Cleanshield Surge with the Urine Management Zone (UMZ) apertures removed." —— SLIDE 42
- [未找到原句]：原文未给出 UMZ 的功能定义、未给出开孔孔径/孔距数值、未说明移除的技术或商业原因

### 概念 12｜Cleanshield Surge 236mm / 276mm（受变更产品对象）

(a) 中文名：Cleanshield Surge 导流层，100mm 宽 × 236mm / 276mm 长｜English term: DIAPER, SURGE, 100MM WIDE X 236MM LONG / 100MM WIDE X 276MM LONG（Cleanshield Surge）

(b) 英文定义（原文，来自模板 Product Description 列）：Two product-level descriptions identifying the two Surge sub-components affected by ER# 900200005649: 100MM WIDE X 236MM LONG and 100MM WIDE X 276MM LONG.

(c) 操作化定义：

||||
|---|---|---|
|Product Description（原文）|DIAPER, SURGE, 100MM WIDE X 236MM LONG|DIAPER, SURGE, 100MM WIDE X 276MM LONG|
|受影响 FPS（5 张）|C153-FPS-01640 / 01641 / 01577 / 01574 / 01575|C153-FPS-01665 / 01667 / 01666 / 01576 / 01642|
|受影响 FP1|C153-FP1-00178|C153-FP1-00173|
|受影响 FPM（v1 Blue 修订）|C153-FPM-00481|C153-FPM-00479|
|处理后 FPM（v2 Peach 新建）|New – 1（base = C153-FPM-00481）|New – 2（base = C153-FPM-00479）|
|长度差|基准|+40mm（276 − 236）|
|宽度|100mm（两规格相同）|100mm（两规格相同）|


- 规模量化指标：单条 ER 覆盖 2 个产品规格 × 5 张 FPS = 10 张 FPS 父图；涉及 FP1 2 张、FPM 2 张（新建后为 2 张新图 + 2 张保留旧图）
- 跨章交叉：Ch2 图像补充 BOM_A 第 7 项 "DIAPER, BCM, SMALL SURGE 100MM W, 236MM L | C153-FP1-00178-D-04" 与本章 236mm 行 FP1 图号一致 → 该 Surge 在 C153-FPS-01575 中被使用，几何描述（100mm W × 236mm L）在 BOM 行与 redline 的 Product Description 中完全同源
(d) 原文摘录：
- "DIAPER, SURGE, 100MM WIDE X 236MM LONG" —— SLIDE 38、SLIDE 42
- "DIAPER, SURGE, 100MM WIDE X 276MM LONG" —— SLIDE 38、SLIDE 42
- "Use C153-FPM-00481 as a base and remove apertures in the front / urine management zone." —— SLIDE 42
- "Use C153-FPM-00479 as a base and remove apertures in the front / urine management zone." —— SLIDE 42

### 概念 13｜Jacobs Engineering Request Form（提交通道）

(a) 中文名：Jacobs 工程服务请求表单（图纸变更提交通道）｜English term: Jacobs Engineering Request Form

(b) 英文定义（定义原文未直接给出，归纳自 SLIDE 36/43 + 图像补充 p43–45）：The web form through which redlines are routed to Jacobs Engineering for execution; it carries scope, description, status, hour estimates, and the DRCS Checker/Approver fields.

(c) 操作化定义：
- 提交动作序列（SLIDE 36 + SLIDE 43 合并）：打开 Jacobs Engineering Request Form → 逐节填写适用部分 → 附上 redlined drawings → 提交
- 必填字段集（图像补充 p43–45）：Scope of the request / Description of work / Status / Estimated Hours / Revised Estimated Hours / Status Comments / DRCS Checker/Approver / DRCS Approver
- 工时字段判据：提交时填 Estimated Hours = 8 × N；执行后由调用方回填 Revised Estimated Hours + Status + Status Comments → 二者差额 = 计划偏差
- 接口人判据：*"Sara Schewe is in the loop and remains the Jacobs contact."*（Ch5 SLIDE 67）

(d) 原文摘录：
- "Go to the Jacobs Engineering Request Form" ／ "Fill out the form and attach your redlined drawings" —— SLIDE 36
- "Submit redlines through Jacobs Engineering to update drawings" ／ "Go through the form and fill out applicable sections" ／ "Attach redlined drawings" —— SLIDE 43
- "Sara Schewe is in the loop and remains the Jacobs contact." —— Ch5 SLIDE 67

# 模块3：证据链（Evidence Chain）

## T1｜Redline 颜色约定表（Color Code for Impacted Drawings）

|||||||
|---|---|---|---|---|---|
|Green|Replace Drawing（Replacement Drawing；Drawing to be replaced with another）|填替换后的目标图号（Replacement Drawing）|我需要的图/改动已存在：不新建、不修订，直接以既有图替换|已确认 "the changes/drawing you need does not already exist" 的反面成立（即确实已存在）|SLIDE 37|
|Blue|Revise Drawing（Drawing # to be redlined / to be revised）|填原图号（例：C153-FPM-00481）|改动应作用于该图本体，且该图全部 Parents 都应接收此变更|"you are OK that all Parents of the drawing will receive the change"|SLIDE 37、SLIDE 38（实例）|
|Peach（文本层作 Peach+）|New Drawing|填 New - X（X 递增：New – 1、New – 2 …）并涂 peach 底色|该图被用在变更不应生效的地方；或修订会让不应接收变更的 Parents 受影响|"If not, the change should be a new drawing change."|SLIDE 37、SLIDE 42（实例）|


配套强制规则（原文 5 条，均 SLIDE 37）

||||
|---|---|---|
|N1|"Before making a new or revising a drawing make sure the changes/drawing you need does not already exist, utilize the replacement option."|复用优先于新建/修订|
|N2|"Before revising a drawing make sure you are OK that all Parents of the drawing will receive the change. If not, the change should be a new drawing change."|父图全域一致性是 Revise/New 的分水岭|
|N3|"If your change requires a new drawing please place "New Drawing - 1" in the cell and shade it peach."|Peach = 文本 + 底色双条件|
|N4|"A FPS or PDD drawing could have more than 1 FP1 or FPM drawing change."|一对多关系合法|
|N5|"If the FPS or PDD drawing has more than one FP1 or FPM drawing change please add information to the next available row before going to the next FPS or PDD drawing."|同 FPS 多行填写，禁止合并单元格式压缩|


## T2｜FORM-48129 模板结构表（逐字段）


来源：SLIDE 37（空白模板，含全部字段与规则）、SLIDE 38／SLIDE 42（已填实例）、图像补充 p37–38（页头/页脚字面值）。
说明：该表在文本提取中呈现为重复列名（如 "FPS or PDD Drawing Impacted" 出现两次），系原表单合并单元格被扁平化所致；下表按逻辑列还原，并在备注中记录重复现象。

### 区块 A：封面识别区（Header）

||||||
|---|---|---|---|---|
|表单标题|Template|—|✓|图像补充 p37–38|
|表单号 + 版本|FORM-48129 Rev.0|FORM-48129 Rev.0|✓（页脚）|SLIDE 37、38、42|
|系统位置标注|FORM-48129 in EtQ|—|✓（取用路径）|SLIDE 37|
|ER#|ER# ␋|900200005649|✓|SLIDE 38、42|
|Change Description|Change Description: XXX|v1：Removal of Urine Management Zone (UMZ) apertures from 236mm and 276mm Cleanshield Surge drawings.；v2：Create new FPM drawings for 236mm and 276mm Cleanshield Surge with the Urine Management Zone (UMZ) apertures removed.|✓|SLIDE 37（占位）／38（v1）／42（v2）|
|附件声明|Actual detailed redlines follow this cover page.|同|✓|SLIDE 37|


### 区块 B：颜色图例区（Color Code for Impacted Drawings）

|||||||
|---|---|---|---|---|---|
|图例 1|Green=|Replace Drawing|Replacement Drawing|Drawing to be replaced with another|SLIDE 37|
|图例 2|Blue=|Revise Drawing|Revise Drawing|Drawing # to be redlined / Drawing # to be revised|SLIDE 37|
|图例 3|Peach+|New Drawing|New Drawing|"New - X" in cell|SLIDE 37|



注：文本层表头 "Color Code for Impacted Drawings" 重复出现两次，为合并单元格扁平化痕迹。

### 区块 C：影响矩阵区（Impact Table — 5 逻辑列 × N 行）

|||||||
|---|---|---|---|---|---|
|C1|Product Description|文本（规格描述）|DIAPER, SURGE, 100MM WIDE X 236MM LONG|DIAPER, SURGE, 100MM WIDE X 276MM LONG|38、42|
|C2|FPS or PDD Drawing Impacted|图号列表（可多行）|C153-FPS-01640 / 01641 / 01577 / 01574 / 01575（5 张）|C153-FPS-01665 / 01667 / 01666 / 01576 / 01642（5 张）|38、42|
|C3|C153-FP1 Drawing Impacted|图号|C153-FP1-00178|C153-FP1-00173|38、42|
|C4|C153-FPM Drawing Impacted|图号 或 New - X（带底色）|v1：C153-FPM-00481（Blue）→ v2：New – 1（Peach）|v1：C153-FPM-00479（Blue）→ v2：New – 2（Peach）|38（v1）／42（v2）|
|C5|Comments or Notes / Replacement drawing or Comments|文本|v1：Remove apertures in the front / urine management zone.；v2：Use C153-FPM-00481 as a base and remove apertures in the front / urine management zone.|v1：Remove apertures in the front / urine management zone.；v2：Use C153-FPM-00479 as a base and remove apertures in the front / urine management zone.|38、42|



头部平台硬编码（重要观察）：C3 与 C4 的列名带平台前缀 "C153-"（C153-FP1 Drawing Impacted / C153-FPM Drawing Impacted），而 C2 为通用（FPS or PDD Drawing Impacted）。→ 该模板版本对 C153 平台（Baby/Infant Care 系列） 有结构性绑定，跨平台复用需改表头。此为文本层与图像补充一致确认的结构事实。
术语补注：PDD = Product Development Drawing，LPA = Layout Pattern Drawing，PSD = Process Schematic Drawing，DOC = Miscellaneous Documentation —— Ch1 SLIDE 17 演讲者备注。

### 区块 D：Notes 规则区（5 条，见 T1 配套规则表）

### 区块 E：页脚

||||
|---|---|---|
|Form ID / Rev|FORM-48129 Rev.0|37、38、42|


### 附：Jacobs Engineering Request Form 字段（区别于 FORM-48129，属提交通道表单）

||||
|---|---|---|
|Scope of the request|变更范围|图像补充 p43–45|
|Description of work|工作内容描述|图像补充 p43–45|
|Status|状态跟踪|图像补充 p43–45|
|Estimated Hours|提交方估算（8 × N）|图像补充 p43–45|
|Revised Estimated Hours|执行方修订后估算|图像补充 p43–45|
|Status Comments|状态说明|图像补充 p43–45|
|DRCS Checker/Approver|记录检查人/批准人|图像补充 p43–45|
|DRCS Approver|记录批准人|图像补充 p43–45|


## T3｜批准矩阵表（Approval Matrix）

### T3-a 原表逐字还原

||||
|---|---|---|
|M (Part)|Product Developer|Product Developer|
|FP1 / FP2 (Sub-Assembly)|Product Developer|Product Developer|
|FPS (Final Drawing)|Product Developer & Senior Product Developer|Senior Quality Engineer|



来源：SLIDE 45。SLIDE 44 以要点形式给出同义表述。

### T3-b 矩阵 × 现行个人授权 双轨对照（含冲突标注）

|||||||
|---|---|---|---|---|---|
|M / FPM (Part)|Product Developer|Product Developer|Product Developer（"submitter"）|一致|SLIDE 44 + SLIDE 45|
|FP1 / FP2 (Sub-Assembly)|Product Developer|Product Developer|Product Developer（"submitter"）|一致|SLIDE 44 + SLIDE 45|
|FPS (Final Drawing)|Product Developer & Senior Product Developer|Senior Quality Engineer|Rex Stuart（*"the only one who can approve"*）|不一致 —— 体系切换期|SLIDE 44 vs SLIDE 45；Ch5 SLIDE 67|


冲突判定的三条硬证据
1. SLIDE 44："Rex Stuart is the only one who can approve a completed FPS drawing." —— 个人 + 唯一（无备份）
2. SLIDE 45（同一内容页，矩阵）：FPS Approver = "Senior Quality Engineer" —— 角色
3. Ch5 SLIDE 67：*"What remains the same: For final FPS drawings product developers will remain a checker. Rex Stuart of Quality remains the Approver for FPS drawings supporting production."* —— 确认 Rex 属 Quality 职能（与矩阵角色职能一致），且状态为 "remains"（旧制延续），与同页 "What will be new"（FPM/FP1 下放给 Product Developer）构成明确的过渡期叙述

→ 结论：SLIDE 44 描述当前态（person-based），SLIDE 45 矩阵描述目标态（role-based）；二者在同一页并存，属体系切换期的文档特征，非笔误。

### T3-c Drawing Checkers 名单（SLIDE 46，标题原文 *"List of Drawing Checkers – Needs updating"*）

||||||
|---|---|---|---|---|
|Baby Care|SNUG_DRY_SND|Diapers- Value|Adrienne Copa|Erica Mullen|
|（承上）|LITTLE_SNUGGLERS_HOSP_LS|Diapers- Premium|Adrienne Copa|Erica Mullen|
|（承上）|LITTLE_SNUGGLERS_HOSP_LS|Diapers- Premium|Adrienne Copa|Erica Mullen|
|（承上）|MICRO_NANO|Diapers- Micro/Nano|Adrienne Copa|Erica Mullen|
|（承上）|LITTLE_SNUGGLERS_HOSP_HOS|Diapers- Super Premium|Sara Rosack|（空）|
|（承上）|LITTLE_MOVERS_OCC_LM-OVN|Diapers- Occasions|Erica Mullen|（空）|
|（承上）|SNUG_DRY_CB|Diapers- Retailer|Erica Mullen|（空）|
|Child Care|LITTLE_MOVERS_OCC_SOD-HLS|Pants- Occasions|Erica Mullen|（空）|
|（承上）|CHILD_CARE_PU|Training Pants- Branded|Mayara Carvalho|Beth Johnson|
|（承上）|CHILD_CARE_CB|Pants- Retailer Branded|Erica Mullen|Beth Johnson|
|（承上）|CHILD_CARE_GN|Youth Pants- Branded|Janet Collins|Horacio Valenzuela|
|DEPEND|AFC Adult Garments|Depend|Kaitlyn Christensen|Yvette Hammonds|


数据质量观察（全部可回溯）
- 标题自承 "Needs updating" —— 名单处于待更新状态
- 重复行：LITTLE_SNUGGLERS_HOSP_LS | Diapers- Premium 出现 2 次（同一 Primary/Backup）→ 疑似未去重
- Backup 缺失：4 条记录 Backup 为空（Sara Rosack 的 Super Premium；Erica Mullen 的 Occasions、Retailer、Pants-Occasions）
- 人员负载集中：Erica Mullen 承担 5 条（4 条 Primary + 1 条 Backup），Adrienne Copa 4 条 Primary
- 覆盖缺口：名单按 Sector × Platform 组织，而批准矩阵按 Drawing Level（M/FP1/FP2/FPS） 组织 → 二者维度不匹配；[未找到原句] 说明二者如何映射（例如该名单是 Checker 池还是 Approver 池）

## T4｜真实案例 ER# 900200005649 全表

### T4-a 案例主表

||||
|---|---|---|
|ER#|900200005649|900200005649（同一编号，未变）|
|Change Description|"Removal of Urine Management Zone (UMZ) apertures from 236mm and 276mm Cleanshield Surge drawings."|"Create new FPM drawings for 236mm and 276mm Cleanshield Surge with the Urine Management Zone (UMZ) apertures removed."|
|FPM 单元格（236mm）|C153-FPM-00481（Blue = Revise）|New – 1（Peach = New）|
|FPM 单元格（276mm）|C153-FPM-00479（Blue = Revise）|New – 2（Peach = New）|
|Comments（236mm）|Remove apertures in the front / urine management zone.|Use C153-FPM-00481 as a base and remove apertures in the front / urine management zone.|
|Comments（276mm）|Remove apertures in the front / urine management zone.|Use C153-FPM-00479 as a base and remove apertures in the front / urine management zone.|
|图示红线圈注文字|*"Remove smaller holes in the front along with the associated dimensions."*（SLIDE 39、40）|同（SLIDE 39、40 位于模板 v1 与 v2 之间）|
|SLIDE|SLIDE 38|SLIDE 42|


### T4-b 受影响图纸全集（两版方案共用）

||||||
|---|---|---|---|---|
|DIAPER, SURGE, 100MM WIDE X 236MM LONG|C153-FPS-01640；C153-FPS-01641；C153-FPS-01577；C153-FPS-01574；C153-FPS-01575|C153-FP1-00178|C153-FPM-00481|New – 1|
|DIAPER, SURGE, 100MM WIDE X 276MM LONG|C153-FPS-01665；C153-FPS-01667；C153-FPS-01666；C153-FPS-01576；C153-FPS-01642|C153-FP1-00173|C153-FPM-00479|New – 2|
|合计|10 张 FPS|2 张 FP1|2 张 FPM|2 张新 FPM|


### T4-c 决策原因（Decision rationale）

||||
|---|---|---|
|原文直接给出的规则|*"Before revising a drawing make sure you are OK that all Parents of the drawing will receive the change. If not, the change should be a new drawing change."* —— SLIDE 37|原文|
|原文直接给出的规则（重述）|"New drawings are required if the drawing you wish to edit is being used somewhere else that your edit(s) wouldn't apply to." —— SLIDE 41|原文|
|原文对「本案例为何由 Revise 改为 New」的直接说明|无|[未找到原句]|
|可支持的推断|C153-FPM-00481 / 00479 除本封面列出的 10 张 FPS 外，还被其他父图使用，而那些父图不应接收"移除 UMZ 开孔"这一改动；因此按 SLIDE 37 注 2 与 SLIDE 41 规则，修订不可用，必须新建。旧图继续存活（v2 Comments 明确 *"Use C153-FPM-00481 as a base"*，即旧图保留为新图的建模母本）|【推断，非原文】 —— 依据 SLIDE 37 注 2 + SLIDE 41 + SLIDE 42 Comments|
|反向旁证（支持上述推断）|v2 的 Comments 措辞从"删除开孔"改为 "以旧图为 base 删除开孔" → 语义上确认旧图不被覆盖、被当作母本复制 → 与 "New" 语义一致|原文（SLIDE 42）+ 推断解读|


### T4-d 案例的工时含义（按 8 hrs/drawing 推算，推算值）

|||||
|---|---|---|---|
|最小口径|仅 2 张新 FPM（New – 1、New – 2）|2|16 hrs|
|中口径|+ 2 张 FP1 修订（C153-FP1-00178、00173）|4|32 hrs|
|满口径|+ 10 张 FPS 受影响图纸全部走修订/更新|14|112 hrs|




口径不确定性（不可回避）：模板中 FPS 列标注为 "Impacted"（受影响），而 8 hrs 规则对应的是 "created/revised"（新建/修订）。原文未说明"受影响的 FPS 是否都需 create/revise"——FPS 可能仅需更新 BOM 指针。→ 上表三档均为推算，实际 N 需以 Jacobs 工单的 Estimated Hours / Revised Estimated Hours 为准。

## T5｜EtQ 流程步骤表（Redline → Execution → Approval）


说明：本章未给出编号化的端到端流程清单。[未找到原句]：原文不存在 "Step 1…Step N" 式的 EtQ 操作说明。下表为基于原文散落指令与表单字段的重建，每一行的"依据"列标明该步骤是否有原文直接支撑。

|||||||
|---|---|---|---|---|---|
|1|发起/挂接 ER#|在 EtQ 中获得或关联变更请求编号|ER#（例：900200005649）|SLIDE 38、42 封面载 ER#；SLIDE 37 标注 FORM-48129 in EtQ|强（实例确证）|
|2|撰写 Change Description|一句话陈述变更内容（会随方案演进而改写）|Change Description 文本|SLIDE 37（占位 XXX）；SLIDE 38 v1；SLIDE 42 v2|强|
|3|取用 FORM-48129 Rev.0|从 EtQ 取模板，勿用本地旧版|空白封面页|SLIDE 36、37（FORM-48129 Rev.0 / in EtQ）|强|
|4|填写影响矩阵|逐行填 Product Description / FPS or PDD / C153-FP1 / C153-FPM / Comments；同 FPS 多变更占多行|影响矩阵（本例 2 行 × 10 FPS）|SLIDE 37 注 4、注 5；SLIDE 38、42|强|
|5|施加颜色语义|按 Green/Blue/Peach 对单元格赋义 + 涂色；Peach 须填 New - X|颜色编码完成的矩阵|SLIDE 37 图例 + 注 3|强|
|6|执行 Revise vs New 判定|查 DRCS "All Parents"；若存在不应接收变更的父图 → New|判定结论（本例：Blue → Peach 反转）|SLIDE 37 注 2；SLIDE 41；SLIDE 42|强（规则）／中（判定动作本身为推断）|
|7|制作详细圈注|在图本体上圈注（*"Remove smaller holes in the front along with the associated dimensions."*），置于封面页之后|Redlined drawings|SLIDE 37（*"Actual detailed redlines follow this cover page."*）；SLIDE 39、40|强|
|8|进入 Jacobs Request Form 并提交|逐节填写；填 Estimated Hours = 8 × N；附上 redlined drawings|已提交工单|SLIDE 36、43；SLIDE 44；图像补充 p43–45 字段|强|
|9|Jacobs 执行 + 回填|外部执行改图；回填 Status / Revised Estimated Hours / Status Comments|修订后图纸 + 实际工时|图像补充 p43–45 字段（字段存在性为强证据；执行方为 Jacobs 由 SLIDE 36、43、Ch5 SLIDE 67 确证）|中（流程步骤为重建）|
|10|Check → Approve 门禁|M/FP1：Product Developer 自查自批；FPS：submitter + fellow senior product developer 双人 Check，再经 Approver（Rex Stuart / 目标态 Senior Quality Engineer）批准|批准记录（DRCS Checker/Approver 字段）|SLIDE 44、45；图像补充 p43–45|强|
|11|发布 / 生效|图纸状态更新，Parents 随之更新|新版本图纸|[未找到原句]（本章未描述发布动作）|弱（无直接原文）|


流程关键特征：步骤 6（Revise/New 判定）是唯一可能反转方案的节点，且发生在提交前（本例在 SLIDE 38→SLIDE 42 之间发生反转，而 ER# 保持不变）→ 说明方案反转在 KC 体系内属低成本的提交前动作，不产生新 ER#。

## T6｜工时与资源估算表（8 hrs/drawing 的应用场景与推算）

### T6-a 规则的适用与不适用边界

||||
|---|---|---|
|新建一张 SolidWorks 图纸（New，Peach）|适用|SLIDE 44 *"8 hrs per drawing to be created/revised"*|
|修订一张 SolidWorks 图纸（Revise，Blue）|适用|同上（*"revised"*）|
|替换一张图纸（Replace，Green）|未明确 —— 替换是否计入 "created/revised" 原文未说|[未找到原句]|
|内部制作 redline 的时间|未明确 —— 原文未说是否包含|[未找到原句]|
|Checker / Approver 复核时间|未明确 —— 原文未说是否包含|[未找到原句]|
|3D 验证、试产、在制品/库存处理时间|未明确|[未找到原句]|
|批准等待（排队）时间|未明确 —— 尤其 FPS 须经唯一批准人|[未找到原句]|
|计划偏差|可测 —— 工单有 Estimated Hours 与 Revised Estimated Hours 双字段|图像补充 p43–45|


### T6-b 通用推算表（推算值，公式：Hours = 8 × N）

换算假设（显式声明）：1 人日 = 8 工时；1 周 = 5 人日；"理想排期"＝1 名 FTE 100% 投入；"现实排期"＝1 名 FTE 有效投入率 60% 计入（该 60% 为本报告假设，非原文数据）。

|||||||
|---|---|---|---|---|---|
|1|8|1|0.2|0.33|单张 FPM 零件微调|
|2|16|2|0.4|0.67|ER#900200005649 最小口径（New – 1、New – 2）|
|4|32|4|0.8|1.33|ER#900200005649 中口径（2 新 FPM + 2 FP1 修订）|
|8|64|8|1.6|2.67|中等复杂度平台变更|
|14|112|14|2.8|4.67|ER#900200005649 满口径（2 新 FPM + 2 FP1 + 10 FPS）|
|20|160|20|4.0|6.67|跨规格（尺码族）变更|
|30|240|30|6.0|10.0|大型平台/跨 Sector 变更|


### T6-c ER# 900200005649 三档口径的资源画像（推算值）

||||||||
|---|---|---|---|---|---|---|
|最小（仅建 2 张新 FPM）|2|16|2|0.4|0.67|不计 FP1/FPS 更新|
|中（+2 张 FP1 修订）|4|32|4|0.8|1.33|FP1 需重挂新 FPM|
|满（+10 张 FPS 更新）|14|112|14|2.8|4.67|FPS 是否真需 8h/张存疑|


### T6-d 关键比率（推算值，供排期用）

||||
|---|---|---|
|单位图纸成本|8 hrs／张|SLIDE 44（原文）|
|人日当量|1 张图 = 1 人日|由 8h/日 换算所得（推算）|
|每增加 1 张受影响图纸的边际成本|+8 hrs（+1 人日）|线性外推（推算）|
|中口径方案的"图纸层级放大系数"|FPM 2 张 → 含 FP1 后 ×2（2→4 张）；含 FPS 后 ×7（2→14 张）|由 T4-b 计数推算|
|排队/批准等待|不可量化|[未找到原句]|



重要提示：上述所有周数仅覆盖 Jacobs 改图工时（8N），不含内部 redline 制作、批准门禁、3D 验证、试产与库存处理。真实项目周期必大于表列值。

# 模块4：章节间衔接（Chapter Connections）

## 4.1 总览：Ch3 在全书链条中的位置

||||||
|---|---|---|---|---|
|① 找图|Ch1 Finding Drawings|1–19|The SPOT → DRCS；Advanced Search（PREFIX / TYPE）；AutoCAD(蓝 A) vs SolidWorks(红 S)|定位图号|
|② 读图|Ch2 Reading Drawings|20–34|Anatomy：Title Block / Overhead View / Cross Section / Detail View(s) / Bill of Materials / Note(s)；BOM & Where Used|理解结构与尺寸|
|③ 改图|Ch3 Editing Drawings|35–46|Redline（FORM-48129）→ Jacobs → Check/Approve|变更后的图纸|
|④ 验证|Ch4 3D Viewer|47–66|eDrawings；Components / Markup / Measure / Move / Explode|3D 可视化确认|
|⑤ 权限|Ch5 DRCS Access|67–80|View / Work / Approve 勾选；经理审批路由|可执行变更的权限|


## 4.2 与【前章 Ch2 Reading Drawings】的衔接：读懂 BOM 才能做 redline

### 对比表

|||||
|---|---|---|---|
|核心能力|看懂图纸构成与尺寸|表达"想改什么"|Ch2 是 Ch3 的输入资格|
|关键结构|Overhead View / Cross Section / Detail View(s) / Bill of Materials / Note(s)·Ref.(s) / Title Block（Ch2 SLIDE 21–32）|影响矩阵 5 列（Product Description / FPS or PDD / C153-FP1 / C153-FPM / Comments）（SLIDE 37）|BOM 的行 = redline 影响矩阵的列来源|
|定位工具|*"SolidWorks drawings rely on BOM / Where Used feature to find detailed dimensions"*（Ch2 SLIDE 33）；"SolidWorks drawings rely more on BOM / Where Used to highlight details"（Ch2 SLIDE 34）|*"Before revising a drawing make sure you are OK that all Parents of the drawing will receive the change"*（SLIDE 37）|BOM/Where Used 向下找子件；All Parents 向上找父图 —— 二者是同一棵树的两向遍历|
|系统按钮|DRCS 图纸页按钮组：< Back / **All Parents** / **All Children** / Print / Help（Ch1/Ch2 图像补充）|同（判定父图集合必须用 All Parents）|同一 UI 承载两章的判定动作|
|层级语言|FPM（最小单元）→ FP1（组件）→ FPS（成品，工厂用）（Ch1 SLIDE 17–19）|矩阵层级 M / FP1·FP2 / FPS（SLIDE 45）；模板列 C153-FP1 / C153-FPM（SLIDE 37）|Ch1/Ch2 的层级定义是 Ch3 批准路由的分类依据|


### 硬证据：Ch2 的 BOM 行就是 Ch3 的 redline 行

|||||
|---|---|---|---|
|父图|C153-FPS-01575-J-09 – DIAPER, BCM, SPDV, TOTAL, S1（Ch2 图像补充 BOM_A 图纸号）|C153-FPS-01575 出现在 SLIDE 38/42 的 236mm 行 FPS 列表（第 5 张）|完全命中|
|子件（第 7 行）|BOM_A item 7：*"DIAPER, BCM, SMALL SURGE 100MM W, 236MM L"* → C153-FP1-00178-D-04|SLIDE 38/42 236mm 行 FP1 列 = C153-FP1-00178；Product Description = "DIAPER, SURGE, 100MM WIDE X 236MM LONG"|图号与几何描述双命中|
|尺寸来源|*"This view holds dimensions the operators will be checking most frequently."*（Ch2 图像补充 p22，Overhead View 定义）|*"Remove smaller holes in the front along with the associated dimensions."*（SLIDE 39、40）|改图形必连带改尺寸标注 → 必须先在 Ch2 的视图/BOM 中找到这些尺寸的归属|




衔接结论（可验证）：不知道 find number / BOM 行，就无法填出 FORM-48129 的 C153-FP1 Drawing Impacted 与 C153-FPM Drawing Impacted 两列，也就无法估算 N，进而无法算出 8 × N。Ch2 → Ch3 是硬性的能力前置，不是软性建议。

### 反例校验：若跳过 Ch2 会怎样

|||
|---|---|
|未查 All Parents 就选 Blue（Revise）|违反 SLIDE 37 注 2 → 变更外溢到不应接收的父图；本例正因此由 SLIDE 38 的 Blue 反转为 SLIDE 42 的 Peach|
|未读 BOM 就填影响矩阵|FP1/FPM 列填不出或填错 → 影响矩阵行数错误 → Estimated Hours 估算错误|
|未定位尺寸标注|"the associated dimensions" 未被一并删除 → 图纸留下悬空尺寸，工厂检验项失效|


## 4.3 与【后章 Ch4 3D Viewer】的衔接：变更后如何在 3D 中验证

### 对比表

|||||
|---|---|---|---|
|状态|变更已提出（redline）→ 由 Jacobs 执行|变更已执行后的图纸验证|Ch3 输出 = Ch4 输入|
|工具|EtQ（FORM-48129）+ Jacobs Request Form|eDrawings（从 KC Software Center / Company Portal 安装；找不到联系 The DESK）（Ch4 SLIDE 48–49）|工具链分离：变更管理与可视化分属不同系统|
|操作对象|图纸语义（图号、尺寸、BOM 关系）|图纸几何（.sldasm / .sldprt）|语义变更 → 几何验证|
|文件类型|—|.sldasm = 3D Assembly；.sldprt = 3D Part（Ch4 SLIDE 50；图像补充另列 .slddrw / .tif）|验证需按图纸层级取对应文件|
|取数路径|DRCS（找图/查 Parents）|*"You will need to download the full SolidWorks file from DRCS"*（Ch4 SLIDE 50）|DRCS 是两章共同的数据源|


### 变更后的 3D 验证动作映射（Ch4 功能 → Ch3 验证需求）

||||
|---|---|---|
|移除 UMZ apertures（前部小孔）|Components 面板下钻定位 Surge 零件 → 左键点击在列表与图形中同时高亮 → 目视确认开孔已消失|Ch4 SLIDE 52–53|
|确认开孔所在层（Surge 在多层结构中的位置）|右键 → Make Transparent（透视外层）；Hide Others (aka – Isolate) 隔离 Surge；Hide 隐藏遮挡件|Ch4 SLIDE 54|
|检查被删孔的关联尺寸是否同步消失|Measure："The measuring tool works the same as the dimension tool, only the dimensions won't be recorded on the drawing" → 量测两点/面间距，且不污染图纸|Ch4 SLIDE 57|
|在 3D 上标注复核意见|Markup：Text / Shapes / Dimensions / Images / Comments；"The dimension feature will add a dimension between two points/surfaces"|Ch4 SLIDE 55–56|
|拆开 Surge 与邻接层，确认新 FPM（New – 1 / New – 2）与上下层配合|Explode（滑块分离）+ Move（Free Drag / Position / Translate / Rotate）；右键 → View → Reset 撤销所有移动与视角|Ch4 SLIDE 58–61|
|切换到正视角复核"front（前部）"区域|View Orientation；'Normal To'（旋转至正对所选面/平面）|Ch4 SLIDE 62|
|误操作回退|右键 → View → Reset|Ch4 SLIDE 61–62|


### 衔接判断

|||
|---|---|
|Ch4 是否覆盖 Ch3 的验证需求？|覆盖几何/装配/尺寸验证（Components / Measure / Markup / Explode / Move / View Orientation）|
|Ch4 是否覆盖 Ch3 的全部需求？|否 —— Ch4 不覆盖 BOM/Parents 一致性验证（变更是否外溢到不应接收的父图），该项仍须回 DRCS 用 All Parents / All Children 核查|
|原文是否明确要求"变更后做 3D 验证"？|否 —— [未找到原句]。Ch4 通篇未提 "verify after change" 或类似强制要求；上述映射是本报告基于两章功能互补性的推断编排，Ch4 功能本身有原文支撑，但"必须用于变更验证"这一规范性要求无原文|
|Ch4 提及的相关规范|*"Reference WI-36700 and 'Product Drawing Issue Checklist' for best practices."*（Ch4 SLIDE 63）—— 这是全书中唯一提到的图纸发布最佳实践文件，可能是变更后验证的规范出处|


## 4.4 与【后章 Ch5 DRCS Access】的衔接：变更批准所需的权限（Approve）

### 对比表

|||||
|---|---|---|---|
|规则内容|谁有资格 Check / Approve 哪一级图纸（SLIDE 44、45）|如何申请并获得这些资格（Ch5 SLIDE 68–74）|Ch3 定义"应有"，Ch5 定义"如何得到"|
|FPM/FP1 批准权|*"Product developers or 'submitters' ... are the approvers for FPM and FP1 drawings"*（SLIDE 44）|*"What will be new: ... product developers will be the approvers of diaper part 'FPM' and sub-assemblies 'FP1' within DRCS"*（Ch5 SLIDE 67）|Ch3 的规则 = Ch5 宣布的新政；Ch5 给出落地方式|
|FPS 批准权|*"Rex Stuart is the only one who can approve a completed FPS drawing"*（SLIDE 44）／矩阵写 Senior Quality Engineer（SLIDE 45）|*"What remains the same: For final FPS drawings product developers will remain a checker. Rex Stuart of Quality remains the Approver for FPS drawings supporting production."*（Ch5 SLIDE 67）|Ch3 的冲突在 Ch5 得到解释：属新旧制切换|
|权限粒度|3 级（M / FP1·FP2 / FPS）× 2 角色（Checker / Approver）|View / Work / Approve 三复选框（Ch5 SLIDE 73）|需勾选 Approve 才能行使 Ch3 矩阵中的 Approver 权限|
|审批链|—|申请提交后 *"will be routed to your manager for approval"*（Ch5 SLIDE 74）|权限本身也需审批 → 两级审批（权限审批 + 图纸审批）|
|申请理由|—|DRCS 会追问 *"Your name, project, why you are asking for the update"*（Ch5 SLIDE 74）|权限获取需业务理由|
|范围限定|—|*"These steps are the same for Adult, Child, and Infant Care. Feminine Care does not have the option for FPM, FP1, FP2 drawing access."*（Ch5 SLIDE 68）|Sector 间权限不一致|
|安全声明|—|*"Creating Product Engineering drawings is K-C confidential information. Distribution must be limited, even with your manager, to your work role access requirements. Before selecting drawing access, Access is based on: Work Role, Business Sector, Reporting Work Location."*（Ch5 图像补充 Step 2）|权限授予的三要素|
|申请界面|—|系统 *"Drawing and CAD Software Access"*；字段 Firstname / M.I. / Lastname / K-C ID / Manager / Business Group；DRCS Access: Standard / Projects Only / None；Sector Access 列表含 Nonwovens、Personal Care - Infant Care 等；Product Specifications (Additional endorsement required) 含 *Personal Care - Infant Care Product Drawings*（Ch5 图像补充 Step 3）|图纸类权限属需额外背书（additional endorsement）类别|


### 角色—权限矩阵（Ch5 图像补充 Step 2）与本方启示

|||||
|---|---|---|---|
|Staff Global Engineer|Global|Sector Drawings|View, Work|
|Staff Engineer|Plant|Plant Drawings|View, Work|
|Engineer|Regional|Regional Drawings|View|
|Engineer|NAR: EMEA, LAO, NA|Regional Drawings|View, Work|
|Engineer|North America|Sector Drawings|View|
|Research (Staff)|Global|Sector Drawings|View|
|Maintenance|Plant|Plant Drawings|View|
|Process Engineer (Regional)|Plant|Plant Drawings|View|
|Process Engineer (Regional)|Regional|Regional Drawings|View|
|Sector Designated Sector|Sector Location|Sector Drawings not including FPM, FP1, FPS, Special Access or Software|View, Work|
|ESHA Associates|Global Location|ESHA Projects only|View, Work|



对本方（卫材研发）的直接含义：角色 Research (Staff) 在 Global / Sector Drawings 上仅获 View —— 即研发岗默认无 Work/Approve 权限。若本方研发组织要行使 Ch3 中 Product Developer 的 FPM/FP1 批准权，必须在角色归类（Work Role）上落在 Product Developer / Engineer 序列，而非 Research 序列，或走 Additional endorsement 通道。这是权限设计中极易踩坑的一处。

### 三章衔接的合流点

||||
|---|---|---|
|想改图|定位图号 + 读 BOM/Parents|Ch1 + Ch2|
|表达改动|FORM-48129（EtQ）+ 颜色语义 + Revise/New 判定|Ch3|
|估算成本|8 hrs × N|Ch3（SLIDE 44）|
|执行改图|Jacobs Request Form + 附件|Ch3（SLIDE 36、43）|
|验证结果|eDrawings（Components / Measure / Markup / Explode）|Ch4|
|获得批准资格|DRCS Access 勾选 View / Work / Approve + 经理审批|Ch5（SLIDE 73–74）|
|行使批准|按层级路由（M/FP1 → PD；FPS → Quality／Rex Stuart）|Ch3（SLIDE 44–45）＋ Ch5（SLIDE 67）|


# 模块5：业务连接点（Business Connections）


业务语境：卫材（纸尿裤 / 湿巾）创新研发 ＋ 木浆与纸品战略采购。
体例：每个连接点 = 涉及幻灯片 ＋ 核心概念 ＋ 关键数据 ＋ 可执行行动建议。

## 连接点 1｜变更管理（ECN）的工时成本 —— 8 hrs/drawing 是硬约束

### 涉及幻灯片

SLIDE 36、SLIDE 43、SLIDE 44（工时）、SLIDE 45（重申）、图像补充 p43–45（工单字段）

### 核心概念

Estimated Hours = 8 × N（rule of thumb）｜Estimated Hours vs Revised Estimated Hours 双字段｜N = 需 create/revise 的图纸张数（＝影响矩阵中 Peach + Blue 单元格数）｜Jacobs 外部执行（内部不直接改图）

### 关键数据

||||
|---|---|---|
|单图工时经验值|8 hrs／drawing（created or revised）|SLIDE 44|
|本案例受影响图纸总数|14 张（10 FPS + 2 FP1 + 2 FPM）|SLIDE 38、42 计数|
|本案例最小口径工时|16 hrs（2 张新 FPM）|推算|
|本案例满口径工时|112 hrs|推算|
|图纸层级放大系数（FPM→+FP1→+FPS）|2 → 4 → 14（×7）|推算（基于 T4-b）|
|计划偏差可测性|工单存在 Revised Estimated Hours 字段 → 偏差可量化|图像补充 p43–45|
|批准等待时间|不可量化|[未找到原句]|


### 排期建议（推算，假设：1 人日 = 8h，1 周 = 5 人日，1 FTE 有效投入率 60%）

|||||||
|---|---|---|---|---|---|
|微小（单零件）|1–2|8–16 h|0.2–0.4 周|1 周|1 名 PD 兼办|
|小（单零件 + 组件）|3–4|24–32 h|0.6–0.8 周|2 周|1 名 PD|
|中（本案例量级）|8–14|64–112 h|1.6–2.8 周|4–6 周|1 名 PD + 0.5 名 Checker|
|大（跨尺码族）|20|160 h|4.0 周|7 周|2 名 PD + 专职 Checker|
|特大（跨 Sector）|30+|≥240 h|≥6.0 周|≥10 周|项目化团队 + 专项审批通道|


### 可执行行动建议

|||||
|---|---|---|---|
|1.1|建立"图纸影响数 N"的提交前强制清点：任何变更立项时，先用 DRCS All Parents / All Children 数出 N，再填 FORM-48129。N 未定 → 不许提交工单|研发项目经理 / PD|《变更影响图纸清单》（含 N）|
|1.2|把 8 hrs/drawing 写进项目 WBS 与预算模板，作为下界而非目标值；同时预留 Revised Estimated Hours 偏差缓冲（建议按 N 的规模分级：N≤4 缓冲 50%，N≥8 缓冲 30%）|研发 PMO / 财务 BP|变更工时预算表|
|1.3|按 N 设审批分流阈值：N ≤ 2 由 PD 直批；3 ≤ N ≤ 8 需 senior PD 会签；N > 8 进入项目化评审（因满口径工时已达 112 hrs ≈ 2.8 周，足以冲击量产排期）|研发负责人|变更分级授权表|
|1.4|记录并复盘 Estimated vs Revised 偏差：每次工单关闭时采集两个字段，按"图纸层级 × 变更类型（New/Revise/Replace）"归类，6 个月内建立本方自己的工时系数，替代 8 hrs 这个"rule of thumb"|研发运营 / 数据 BP|偏差率看板 + 内部工时系数表|
|1.5|压缩 N 本身：变更设计阶段即评估"能否只改 FPM 而不触发 FP1/FPS 更新"（例如把改动约束在父图以变量/配置方式吸收）。本案例中 FPM→FPS 的 ×7 放大是最大成本杠杆|结构设计 / 研发工程师|变更方案对比（N 最小化）|
|1.6|把批准等待纳入关键路径：尤其 FPS 级（唯一批准人）。排期时不要把 Ch3 的 8N 当作项目周期|项目经理|含门禁的项目甘特图|


## 连接点 2｜"修订 vs 新建"的决策逻辑 —— 为什么 KC 最终选择新建图号

### 涉及幻灯片

SLIDE 37（判定规则）、SLIDE 38（v1，Blue 修订）、SLIDE 41（New 条件独立重述）、SLIDE 42（v2，Peach 新建）

### 核心概念

Parents 全域一致性判定｜Blue = Revise / Peach = New｜"Use XXX as a base"（旧图作母本保留）｜ER# 不变而 Change Description 改写（方案反转不产生新 ER#）

### 关键数据

||||
|---|---|---|
|FPM 单元格|C153-FPM-00481 / 00479（Blue）|New – 1 / New – 2（Peach）|
|旧图命运|被覆盖（修订）|保留（v2 Comments：*"Use C153-FPM-00481 as a base"*）|
|受影响 FPS|10 张（5 + 5）|同（不变）|
|ER#|900200005649|900200005649（不变）|
|Change Description|Removal of UMZ apertures…|Create new FPM drawings … with the UMZ apertures removed.|
|决策原因（原文）|—|[未找到原句]（规则有、原因无）|


### 决策判据（从 KC 规则提炼为本方可复用形式）

KC 的原文规则只有两条，但极其锋利：
1. *"Before making a new or revising a drawing make sure the changes/drawing you need does not already exist, utilize the replacement option."*（SLIDE 37）—— 复用优先
2. *"Before revising a drawing make sure you are OK that all Parents of the drawing will receive the change. If not, the change should be a new drawing change."*（SLIDE 37）/ *"New drawings are required if the drawing you wish to edit is being used somewhere else that your edit(s) wouldn't apply to."*（SLIDE 41）—— 父图外溢即新建

本方可复用的三维判据表（KC 规则 + 制造业通用维度扩展，扩展部分已标注）

||||||
|---|---|---|---|---|
|① 影响范围（Scope）|该图号是否还被其他父图使用，且那些父图不应接收本变更？|否 → 全部 Parents 都应接收|是 → 必须 New|SLIDE 37 注 2、SLIDE 41（原文）|
|② 复用替代（Reuse）|我需要的图/改动是否已存在？|已存在 → 走 Replace（Green），都不用改|不存在 → 再进 ①|SLIDE 37 注 1（原文）|
|③ 追溯要求（Traceability）|变更是否属法规/客户/安全相关，需保留旧版本可追溯？|不需要|需要 → New 更安全|【扩展，本章无原文；KC 案例中由 v2 "as a base" 间接体现旧图保留】|
|④ 库存/在制品（WIP & Inventory）|现有库存、在制、已发运产品是否需区分"改前/改后"？|可自然切换、无需区分|需区分 → New（新旧图号并存，便于批次追溯）|【扩展，[未找到原句]——本章完全未提库存处理】|
|⑤ 切换时序（Timing）|新旧版本是否需要并行一段时间？|一刀切换|并行 → New|【扩展，[未找到原句]】|
|⑥ 成本（Cost）|8 hrs/drawing 下，哪种方案 N 更小？|通常 Revise 的 N 更小（不新增图号）|New 会增加图号总量，但可能避免 10 张 FPS 的返工|由 SLIDE 44 推得|




KC 本案例的经济学解读（【推断，非原文】）：v1 修订 FPM-00481/00479 时，其 10 张 FPS 父图全部被动接收变更；若其中任一 FPS 本不该改，则必须 New。New 之后，旧 FPM 保留、新 FPM 只被"需要的"FPS 引用 —— 代价是新增 2 个图号，收益是避免外溢 + 保留旧版可追溯。在 KC 的判据体系里，外溢风险 > 图号膨胀成本。

### 可执行行动建议

||||
|---|---|---|
|2.1|在变更评审模板中固化"Parents 全域核查"签字项：提交 FORM-48129 前，必须附 DRCS All Parents 截图，并逐行标注"应接收 / 不应接收"。只要有 1 个"不应接收" → 强制 New|直接移植 SLIDE 37 注 2 + SLIDE 41|
|2.2|建立"Reuse → Revise → New"三级决策树（KC 顺序：先查是否已存在→Replace；再查 Parents→Revise or New），并把 KC 的两条原文规则作为节点的判定文案|见上表 ①②|
|2.3|补齐 KC 未覆盖的三条判据（追溯 / 库存·在制品 / 切换时序）。本章原文完全未提库存与在制品处理 —— 对本方（卫材，库存与产线切换频繁）而言这是必补项，不得直接照搬 KC 规则|见上表 ③④⑤|
|2.4|把"方案反转"做成零成本动作：本案例中 Blue→Peach 反转未产生新 ER#，属提交前迭代。→ 在流程上鼓励提交前充分评审（成本低），而非提交后返工（成本高，涉及 Jacobs 工时与 Revised Estimated Hours）|依据 SLIDE 38→42 ER# 不变|
|2.5|命名与底色双条件写入 SOP：New 必须同时满足"单元格填 New - X"＋"涂 peach"，否则下游无法识别为新建 → 工时估算与批准路由都会错|依据 SLIDE 37 注 3|


## 连接点 3｜UMZ apertures 的技术含义 —— 移除前部开孔说明什么

### 涉及幻灯片

SLIDE 38（Change Description + Comments 首次出现）、SLIDE 39、SLIDE 40（圈注文字）、SLIDE 42（v2 表述）

### 核心概念

UMZ = Urine Management Zone（尿液管理区）｜apertures = 开孔（原文亦称 "smaller holes"）｜对象 = Cleanshield Surge，100mm 宽 × 236mm / 276mm 长｜删除范围 = 前部（front） 的较小孔 ＋ 关联尺寸

### 关键数据（全部来自原文，无加工）

||||
|---|---|---|
|变更动作|Remove（移除）|SLIDE 38、42|
|变更部位|front / urine management zone|SLIDE 38、42|
|孔的形态描述|"smaller holes"（较小的孔）|SLIDE 39、40|
|连带处理|"along with the associated dimensions"（连同关联尺寸）|SLIDE 39、40|
|产品规格|100MM WIDE × 236MM LONG；100MM WIDE × 276MM LONG|SLIDE 38、42|
|长度梯度|236mm 与 276mm（差 40mm）|推算|
|孔径 / 孔距 / 孔数|未提供|[未找到原句]|
|移除的技术或商业原因|未说明|[未找到原句]|
|UMZ 的功能定义|未给出|[未找到原句]|


### 技术解读（严格区分原文事实与本方推断）

A. 原文可确证的事实（4 条）
1. 变更对象是 Surge 层（导流/涌吸层，位于面层与芯体之间的典型结构位），几何为 100mm 宽，有 236 / 276mm 两种长度。
2. 该 Surge 层上存在开孔（apertures/holes），且至少分两档规格（原文称被删的是 "smaller holes"，隐含另有较大孔或主孔）。
3. 被删的孔位于 front（前部） 且属于 urine management zone —— 即产品 MD 方向前段的液体管理区域。
4. 删除孔必须同时删除其关联尺寸标注 —— 说明这些孔是受控的、带检验尺寸的几何特征，不是装饰性或工艺随机特征。

B. 原文可确证的流程事实（2 条）
5. 该变更最终采用 New（新建图号）而非 Revise —— 按 SLIDE 41 规则，意味着存在不该接收此变更的父图。
6. 变更同时覆盖 236mm 与 276mm 两个规格、牵动 10 张 FPS —— 属于平台级（跨尺码）变更，非单点试改。

C. 本方推断（【推断，非原文】，须以试验验证，不得当结论用）

||||
|---|---|---|
|C1：前部 UMZ 开孔的收益未被实测证实，或收益 < 其成本/风险|若为纯增益设计，不会在平台级变更中整体删除；且采用 New 说明要与旧版长期区分|查 KC 相关专利/试验报告；做开孔 vs 无孔的液体管理对比试验|
|C2：开孔可能与回渗/干爽性、结构完整性、或外观存在问题|Surge 层开孔的理论用途是加速液体下渗；若导致局部积液、回渗升高、或开孔处强度下降/透胶，则会被移除|测回渗（rewet）、多次液流穿透时间、开孔区 tensile|
|C3："smaller holes"被删而保留其他孔 → 开孔规格在收敛|原文明说是 "smaller" holes，说明同层存在多档孔；删小留大 = 参数简化|拆解竞品/KC 实物，测绘孔径与孔距|
|C4：删孔降低制造复杂度（少一组打孔工艺/刀具/检验项）|连带删除 "associated dimensions" → 直接减少工厂检验项|评估打孔工序成本与检验工时|


### 对本方芯体结构开发的启示

||||
|---|---|---|
|3.1|开孔类"导流增强"特征必须自带可测的收益证据，否则平台级变更一来就被当作成本项砍掉。→ 本方任何 Surge/ADL/导滤层开孔方案，立项时就要绑定量化指标（穿透时间、回渗、扩散长度、多次液流保持率）|建立《开孔类特征收益证据包》模板，作为立项准入件|
|3.2|警惕"多档开孔规格"的复杂度陷阱。KC 同层至少有大小两档孔；删小留大本质是参数收敛。→ 本方芯体设计应显式控制开孔规格数量，避免"孔越多越好"|设计评审中增设"特征规格数量"审查项|
|3.3|前部（front）是尿液管理的核心战场。变更精准落在 "front / urine management zone"，说明 KC 把前端液体管理视为独立功能区并单独调参。→ 本方芯体应按 MD 分区（前/中/后） 建立分区功能模型，而非整体均一设计|建立芯体 MD 分区性能指标矩阵（前段穿透 / 中段扩散 / 后段防漏）|
|3.4|尺寸标注即检验成本。"Remove ... along with the associated dimensions" 揭示了：每删一个几何特征，就少一组工厂检验项。→ 本方设计评审应把"该特征带来多少检验项"纳入成本模型|在 DFMEA/图纸评审中加入"检验项计数"|
|3.5|平台级（跨尺码）变更需预先设计"新图号"通道。236mm/276mm 同步改、牵动 10 张 FPS，最终走 New —— 说明跨尺码族的变更天然需要新图号分支。→ 本方在规划尺码族时，应为"可分支的共通层"预留图号策略|制定尺码族图纸策略（共通层 vs 规格层）|
|3.6|对木浆/纸品采购的连带含义：Surge 层开孔设计变更 → 该层材料（可能为含木浆的复合导流材料或纸基材料）的定量、孔隙率、打孔适应性要求随之变化。→ 战略采购应在图纸变更评审中提前介入，评估现有浆种/纸种是否仍适配新结构|建立"图纸变更 → 材料规格影响"联审机制（研发 + 战略采购）|


## 连接点 4｜批准权限集中化（Rex Stuart 单点）的风险 —— 对研发组织设计的反向启示

### 涉及幻灯片

SLIDE 44（Rex Stuart 唯一批准人）、SLIDE 45（矩阵写 Senior Quality Engineer）、SLIDE 46（Checkers 名单 + "Needs updating"）、Ch5 SLIDE 67（新旧制说明）、Ch5 SLIDE 73–74（权限申请）、Ch5 图像补充 Step 2（角色—权限表）

### 核心概念

单点批准（single-point approval）｜角色制 vs 个人制（role-based vs person-based）｜体系切换期（transition state）｜职责分离（SoD, separation of duties）｜Backup 覆盖率

### 关键数据

||||
|---|---|---|
|FPS 批准人基数|1（*"Rex Stuart is the only one who can approve"*）|SLIDE 44|
|FPS 批准备份数|0|由 SLIDE 44 "only" 推得|
|同页内的制度冲突|角色（Senior Quality Engineer）vs 个人（Rex Stuart）|SLIDE 44 vs SLIDE 45|
|支撑名单状态|标题原文 "Needs updating"|SLIDE 46|
|名单 Backup 缺失条数|4 条（Sara Rosack / Erica Mullen ×3 平台）|SLIDE 46 计数|
|名单重复行|1 条（LITTLE_SNUGGLERS_HOSP_LS Premium 出现 2 次）|SLIDE 46 计数|
|单人最大负载|Erica Mullen 承担 5 条（4 Primary + 1 Backup）|SLIDE 46 计数|
|权限下放（新制）|FPM/FP1 批准权 → Product Developer|Ch5 SLIDE 67|
|权限保留（旧制）|FPS 批准权 → Rex Stuart of Quality|Ch5 SLIDE 67|
|研发岗默认权限|Research (Staff) → Sector Drawings → 仅 View|Ch5 图像补充 Step 2|
|权限申请路由|提交后 *"routed to your manager for approval"*|Ch5 SLIDE 74|
|权限授予三要素|Work Role / Business Sector / Reporting Work Location|Ch5 图像补充 Step 2|


### 风险画像

||||
|---|---|---|
|R1 单点故障|FPS 唯一批准人，SLIDE 44|一名关键批准人休假/离职/调岗 → 全部 FPS 级变更停滞（本案例 10 张 FPS 全部卡住）|
|R2 知识单点依赖|同一人长期垄断 FPS 批准 → 隐性标准（judgement）无文档化|判据不可传承；新人无法判定，只能"问某人"|
|R3 制度与执行脱节|矩阵写角色、执行归个人（SLIDE 44 vs 45）|SOP 与实际两套，审计时无法对齐|
|R4 支撑数据腐烂|名单 "Needs updating"、4 条 Backup 空、1 条重复|岗位调动后名单失效，Checker 找不到人|
|R5 负载不均|Erica Mullen 5 条、Adrienne Copa 4 条|关键人成为瓶颈，且无备份|
|R6 研发岗权限不足|Research (Staff) 仅 View|研发只能看不能改不能批 → 变更必须借道 Product Developer，拉长链路|


### 反向启示：知识单点依赖 vs 流程效率（本方研发组织设计）

KC 的做法是效率优先的折中：
- 放权给 Product Developer（FPM/FP1） → Ch5 SLIDE 67 明说目的：*"This gives product developers more control and speed within the process."* —— 牺牲 SoD 换速度，因为零件/组件级改动影响域可控（Parents 少、后果局部）
- 收紧 FPS（成品图） → 双人 Check（submitter + fellow senior PD）+ 单一 Quality 批准人 —— 因为 FPS "Drawing as would be used in the mill"（Ch1 SLIDE 17），直接影响工厂生产，后果全局


这套折中在本方是否成立，取决于一个变量：批准权是"人"还是"角色"。

|||||
|---|---|---|---|
|Person-based（KC 当前态）|决策快、标准一致、责任清晰|单点故障、知识不可传承、规模不经济|不作为目标态；若过渡期采用，必须设强制 Backup + 最长任期|
|Role-based（KC 目标态，见 SLIDE 45 矩阵）|可扩展、可传承、可审计、可备份|需角色能力认证、需判据文档化|作为目标态；但必须以"判据文档化"为前提，否则角色化只是把人名换成岗位名，知识仍锁在原人脑中|


### 可执行行动建议

||||
|---|---|---|
|4.1|任何单点批准岗必须配 Backup，且 Backup 需通过同套认证。KC 名单中 4 条 Backup 为空是明确的反面教材|SLIDE 46|
|4.2|批准权角色化的前置条件 = 判据文档化。在把批准权从"人"迁到"角色"之前，先把该人脑中的隐性判据写成 check list（例如：FPS 批准要看哪 8 项）。否则角色化只是形式|由 SLIDE 44 vs 45 冲突反推|
|4.3|按影响域分级授权，而非按图纸层级一刀切。KC 的底层逻辑是"影响域小 → 放权；影响域大 → 收紧"。本方可直接复用：以 Parents 数量 而非图纸类型作为授权阈值（例：Parents ≤ 2 → PD 自批；Parents > 2 → 双人 Check；涉及成品/量产 → 质量批准）|Ch5 SLIDE 67 + SLIDE 37 注 2|
|4.4|研发岗权限要提前规划。KC 的 Research (Staff) → 仅 View 说明"研发"在权限体系里默认不是执行角色。本方若希望研发工程师能直接提交/批准变更，需在角色定义（Work Role）阶段就落在 Product Developer / Engineer 序列，或建立 Additional endorsement 通道 —— 事后补权限要走经理审批，链路长|Ch5 图像补充 Step 2、Ch5 SLIDE 74|
|4.5|建立 Checker 名单的强制复核节奏。KC 名单标题自带 "Needs updating"，说明名单腐烂是常态而非例外。→ 名单须挂 owner + 复核周期（建议季度）+ 与 HR 岗位变动联动|SLIDE 46|
|4.6|把单点岗位的"瓶颈指标"纳入管理看板：待批 FPS 数、平均批准时延、该岗在岗率。KC 未量化批准等待（[未找到原句]），本方应补上 —— 不可量化的瓶颈无法管理|由 SLIDE 44 + T6-a 缺口推得|
|4.7|为新旧制并存设明确 sunset 期。KC 的 "What will be new / What remains the same"（Ch5 SLIDE 67）是清晰的过渡叙述，但未给出切换时间点。本方在推行类似改革时，应为旧制授权设到期日，否则过渡期会无限延长|Ch5 SLIDE 67|


## 附：可直接用于研发管理的数据清单表


全部数值可回溯至本章原文；标注「推算」者为基于 8 hrs/drawing 的外推，标注「假设」者为本报告设定。

|||||||
|---|---|---|---|---|---|
|1|单图工时经验值|8 hrs／drawing（created/revised）|原文|SLIDE 44|变更工时预算、WBS 估算|
|2|工时公式|Hours = 8 × N|推算|SLIDE 44|排期模型|
|3|人日当量|1 张图 = 1 人日（按 8h/日）|推算|换算|资源计划|
|4|本案例受影响图纸总数|14 张（10 FPS + 2 FP1 + 2 FPM）|原文计数|SLIDE 38、42|规模基准|
|5|本案例 FPS 数|10 张（5 + 5）|原文|SLIDE 38、42|父图影响域基准|
|6|本案例最小/中/满口径工时|16 / 32 / 112 hrs|推算|SLIDE 44 + T4-b|三档预算|
|7|图纸层级放大系数|FPM 2 → +FP1 4（×2）→ +FPS 14（×7）|推算|T4-b|变更成本杠杆识别|
|8|变更单号（ER#）|900200005649|原文|SLIDE 38、42|案例索引|
|9|变更对象规格|100MM WIDE × 236MM LONG；100MM WIDE × 276MM LONG|原文|SLIDE 38、42|尺码族规划|
|10|尺码长度梯度|40mm（276 − 236）|推算|SLIDE 38、42|尺码台阶设计|
|11|变更部位|front / urine management zone|原文|SLIDE 38、42|芯体 MD 分区设计|
|12|被删特征|apertures / "smaller holes" + associated dimensions|原文|SLIDE 39、40|开孔类特征收益证据要求|
|13|模板表单号|FORM-48129 Rev.0（in EtQ）|原文|SLIDE 37|表单本地化蓝本|
|14|模板列数|5 逻辑列（Product Description / FPS or PDD / C153-FP1 / C153-FPM / Comments）|原文|SLIDE 37|影响矩阵设计|
|15|模板强制规则数|5 条 Notes|原文|SLIDE 37|SOP 条款|
|16|颜色语义|Green=Replace / Blue=Revise / Peach=New|原文|SLIDE 37|变更语义标准化|
|17|New 的填写约定|单元格填 New - X ＋ 涂 peach 底色（双条件）|原文|SLIDE 37 注 3|表单校验规则|
|18|Revise/New 判定规则|Parents 全域一致性（有不该接收的父图 → New）|原文|SLIDE 37 注 2、SLIDE 41|变更评审签字项|
|19|批准层级|M / FP1·FP2 / FPS（3 级）|原文|SLIDE 45|授权体系设计|
|20|职责分离（SoD）|M、FP1/FP2：无分离（PD 自查自批）；FPS：强分离（双人 Check + Quality 批准）|原文|SLIDE 45|内控设计|
|21|FPS 批准链独立人数|≥ 3（submitter + fellow senior PD + Quality approver）|原文|SLIDE 44、45|门禁设计|
|22|FPS 批准人基数 / 备份数|1 / 0（Rex Stuart 唯一）|原文|SLIDE 44|单点风险登记|
|23|制度冲突|角色 Senior Quality Engineer（SLIDE 45）vs 个人 Rex Stuart（SLIDE 44）|原文|SLIDE 44、45|体系切换期判定的证据样本|
|24|支撑名单状态|"Needs updating"；4 条 Backup 为空；1 条重复；单人最大 5 条|原文计数|SLIDE 46|名单治理反例|
|25|权限三档|View / Work / Approve|原文|Ch5 SLIDE 73|权限矩阵设计|
|26|研发岗默认权限|Research (Staff) → Sector Drawings → 仅 View|原文|Ch5 图像补充 Step 2|研发角色定位|
|27|权限授予三要素|Work Role / Business Sector / Reporting Work Location|原文|Ch5 图像补充 Step 2|权限申请设计|
|28|权限申请路由|提交后 routed to manager for approval|原文|Ch5 SLIDE 74|两级审批设计|
|29|工单双工时字段|Estimated Hours / Revised Estimated Hours|原文|图像补充 p43–45|偏差度量接口|
|30|工单字段全集|Scope of the request / Description of work / Status / Estimated Hours / Revised Estimated Hours / Status Comments / DRCS Checker/Approver / DRCS Approver|原文|图像补充 p43–45|工单系统字段设计|
|31|外部执行方|Jacobs Engineering（接口人 Sara Schewe）|原文|SLIDE 36、43；Ch5 SLIDE 67|外包策略参考|
|32|最佳实践文件|WI-36700；Product Drawing Issue Checklist|原文|Ch4 SLIDE 63|待获取的规范文件|
|33|有效投入率（本方排期用）|60%（本报告假设，非原文）|假设|—|现实排期换算|
|34|不可量化项（缺口清单）|批准等待时间、内部 redline 制作时间、复核时间、3D 验证时间、库存/在制品处理时间、Replace 是否计入 8h、UMZ 移除原因、孔径/孔距/孔数|缺口|[未找到原句]|本方须自建度量|


# 模块6：金句索引（Key Quotes Index）


体例：英文原文 ＋ SLIDE N ＋ 中文翻译 ＋ 「为什么记」。

### Q1｜"Product drawing edits are handled through Jacobs Engineering"

SLIDE 36
译：产品图纸的修改工作由 Jacobs Engineering 承接处理。
为什么记：本章的地基句。它一次性界定了"内部不直接改图"这一组织边界——研发交付的是 redline（意图），不是图纸（结果）。理解这句，才能理解为什么后面所有工作都要过 EtQ 表单、过外部工单、过批准门禁。对本方做自制/外包决策时，这是最直接的对照样本。

### Q2｜"Use the Product Drawings Redline Template (FORM-48129 in EtQ) to capture the edits you would like made"

SLIDE 36
译：使用《产品图纸红线圈注模板》（EtQ 系统中的 FORM-48129）来记录你希望做出的修改。
为什么记：表单号 + 系统位置 + 用途三合一。它把"改图"从个人行为升格为受控的记录行为——你要改什么，必须先写进一张有编号、有版本、有存放系统的表。本方建立变更管理体系时，这是最小可用的起点：一个编号表单 + 一个系统。

### Q3｜"Before making a new or revising a drawing make sure the changes/drawing you need does not already exist, utilize the replacement option."

SLIDE 37
译：在新建或修订图纸之前，先确认你需要的改动/图纸是否已经存在，优先使用「替换」选项。
为什么记：复用优先原则。绝大多数图号膨胀不是因为需求多，而是因为没查。这是控制图纸库存成本的第一道闸门，也是唯一一条指向 Green（Replace）的规则——三色体系中 Green 常被忽略，而它其实是最省钱的选项。

### Q4｜"Before revising a drawing make sure you are OK that all Parents of the drawing will receive the change. If not, the change should be a new drawing change."

SLIDE 37
译：在修订一张图纸之前，先确认你能接受该图纸的全部父图都接收到此变更。如果不能接受，那么这次变更就应该做成新建图纸变更。
为什么记：本章最锋利的一句，也是全套规则的判定核心。它把"修订 vs 新建"从"改动大不大"这个错误维度，扭转到"父图影响域是否可接受"这个正确维度。真实案例 ER# 900200005649 正是被这句规则从 Blue 逼成 Peach 的。可压缩为一句话：有不该接收变更的父图，就必须新建。

### Q5｜"New drawings are required if the drawing you wish to edit is being used somewhere else that your edit(s) wouldn't apply to."

SLIDE 41
译：如果你想修改的图纸还被用在其他地方、而你的修改并不适用于那些地方，那么就必须新建图纸。
为什么记：Q4 的独立重述版，且措辞更直白（*"used somewhere else"*）。KC 把它单独做成一页幻灯片，说明这是最常被违反、也最需要强调的规则。两句并置还有一个额外价值：同一规则用两种措辞各说一遍，是培训材料里"这句话很重要"的信号。

### Q6｜"If your change requires a new drawing please place "New Drawing - 1" in the cell and shade it peach."

SLIDE 37
译：如果你的变更需要新建图纸，请在单元格中填入「New Drawing - 1」，并将其底色涂为桃色。
为什么记：双条件约定的样板（文本内容 + 视觉底色）。这看似琐碎，实则关键：只填文字不涂色，下游读表的人就不会把它识别为"新建"，于是工时估算（8×N）与批准路由全错。本方设计任何变更表单时，都应学习这种"语义 + 视觉"双重编码的做法，降低误读率。

### Q7｜"A FPS or PDD drawing could have more than 1 FP1 or FPM drawing change." ／ "If the FPS or PDD drawing has more than one FP1 or FPM drawing change please add information to the next available row before going to the next FPS or PDD drawing."

SLIDE 37
译：一张 FPS 或 PDD 图纸可能对应多个 FP1 或 FPM 图纸变更。／ 如果一张 FPS 或 PDD 图纸有多个 FP1 或 FPM 图纸变更，请在切换到下一张 FPS 或 PDD 之前，把信息填到下一个可用行。
为什么记：一对多关系的填表纪律。它保证了影响矩阵的行数 = 变更条数，而不是"父图数"——这直接决定 8 × N 中的 N 是否准确。禁止合并填写，是防止成本被系统性低估的细节设计。

### Q8｜"Removal of Urine Management Zone (UMZ) apertures from 236mm and 276mm Cleanshield Surge drawings."

SLIDE 38（ER# 900200005649，方案 v1 的 Change Description）
译：从 236mm 与 276mm 的 Cleanshield Surge 图纸中移除尿液管理区（UMZ）开孔。
为什么记：技术变更内容的原始表述。三个信息密度极高：(i) UMZ 是 KC 认可的独立功能区术语；(ii) 变更同时覆盖两个尺码（平台级）；(iii) 术语缩写 UMZ 首次在此被展开定义。对本方做竞品技术跟踪，这是可检索的锚点句。

### Q9｜"Remove smaller holes in the front along with the associated dimensions."

SLIDE 39、SLIDE 40（红线圈注文字，重复出现两次）
译：移除前部较小的孔，连同其关联尺寸一并移除。
为什么记：本章唯一的"圈注层"原话，也是全章最贴近技术实质的一句。两个关键词："smaller holes"（说明同层存在多档开孔规格，被删的是小孔）与 "along with the associated dimensions"（尺寸标注是特征的附属物，删特征必须删尺寸）。后者揭示了一个常被忽略的成本真相：每个几何特征都携带工厂检验成本。

### Q10｜"Create new FPM drawings for 236mm and 276mm Cleanshield Surge with the Urine Management Zone (UMZ) apertures removed."

SLIDE 42（ER# 900200005649，方案 v2 的 Change Description）
译：为 236mm 与 276mm 的 Cleanshield Surge 创建新的 FPM 图纸，其中尿液管理区（UMZ）开孔已被移除。
为什么记：方案反转的文字证据。与 Q8 并读，可见 Change Description 的动词从 "Removal of ... apertures"（修订视角） 改为 "Create new FPM drawings ... with ... apertures removed"（新建视角），而 ER# 保持不变。这证明：在 KC 体系内，方案反转是提交前的低成本迭代，不产生新变更单——流程设计上鼓励"提交前想清楚，提交后少返工"。

### Q11｜"Use C153-FPM-00481 as a base and remove apertures in the front / urine management zone."

SLIDE 42
译：以 C153-FPM-00481 为基础（母本），移除前部／尿液管理区的开孔。
为什么记："as a base"是新建方案的经济学密码。它确认旧图不被覆盖、被当作母本复制——旧版本继续存活供其他父图引用。这一句同时解释了为什么 New 比 Revise 更安全：修订会摧毁旧版本，新建会保留它。对本方做"改款 vs 换代"决策，这是最精炼的表述范式。

### Q12｜"General rule of thumb for 'Estimated Hours' is 8 hrs per drawing to be created/revised."

SLIDE 44（SLIDE 45 全文重复）
译：「预估工时」的通用经验法则是：每新建或修订一张图纸按 8 小时计。
为什么记：全章唯一的硬量化数字，也是整个变更成本模型的基石。三点必须记住：(i) 它是 rule of thumb（经验值），不是承诺值；(ii) 单位是每张图，所以图纸数量 N 是成本的第一杠杆；(iii) 工单上同时存在 Estimated Hours 与 Revised Estimated Hours，说明它可被调用方修订。把这个数字乘以 N，你就有了变更预算的下界。

### Q13｜"Product developers or "submitters" of SolidWorks drawing changes are the approvers for FPM and FP1 drawings."

SLIDE 44（SLIDE 45 重复）
译：产品开发人员（即 SolidWorks 图纸变更的"提交人"）是 FPM 与 FP1 图纸的批准人。
为什么记：放权的边界句。它在零件级（FPM）与组件级（FP1）放弃了职责分离——提交人自己批自己。这是 KC 明确的速度优先选择，其正当性来自"影响域可控"。本方照搬前必须自问：我们的 FPM/FP1 影响域是否同样可控？ 若不可控，这条放权就是内控漏洞。

### Q14｜"Completed FPS drawings are checked by the submitter and a fellow senior product developer."

SLIDE 44（SLIDE 45 重复）
译：已完成的 FPS 图纸，由提交人本人以及另一位资深产品开发人员共同检查。
为什么记：成品级（FPS）的双人检查要求。关键词是 "a fellow senior product developer"——必须是同级资深人员，且是另一个人（自检 + 互检）。这条与 Q13 形成鲜明对照：零件级自查自批，成品级双人互检。差异的理由在 Ch1 SLIDE 17：FPS 是 *"Drawing as would be used in the mill"*（工厂实际使用的图）——影响域直抵产线。

### Q15｜"Rex Stuart is the only one who can approve a completed FPS drawing." ／ "List of Drawing Checkers – Needs updating"

SLIDE 44 ／ SLIDE 46
译：Rex Stuart 是唯一能够批准一张已完成 FPS 图纸的人。／ 图纸检查人名单——需要更新。
为什么记：本章最重要的两句，必须并读。第一句暴露单点风险：FPS 批准人基数 = 1、备份 = 0，且它与同页矩阵里的角色表述（Senior Quality Engineer）互相冲突——这是体系切换期的典型症状（目标态是角色制，当前态是个人制）。第二句则暴露支撑数据腐烂：连名单自己都承认待更新，其中 4 条 Backup 为空、1 条重复。两句合起来讲清了一个组织真理：流程的健壮性不取决于 SOP 写得多好，而取决于"人"这个环节有没有冗余、数据有没有维护。对本方研发组织设计，这是最有价值的一条反向教材——放权提效（Q13）与收权风控（Q15）必须成套设计，且收权点必须有备份。

## 附：本章未决问题清单（Open Questions）

||||
|---|---|---|
|1|"Impacted" 的 FPS 是否全部计入 8 hrs/drawing 的 N？FPS 是否可能仅需更新 BOM 指针？|[未找到原句]|
|2|Green（Replace）是否占用 8 hrs？|[未找到原句]|
|3|8 hrs 是否包含内部 redline 制作、Checker/Approver 复核、3D 验证时间？|[未找到原句]|
|4|Jacobs 的 SLA / 排队时长 / 计划偏差率？|[未找到原句]|
|5|ER# 900200005649 由 Revise 改为 New 的直接原因？|[未找到原句]（仅有规则，无原因陈述）|
|6|UMZ 的功能定义、孔径/孔距/孔数、移除的技术或商业理由？|[未找到原句]|
|7|SLIDE 46 的 Checker 名单与 SLIDE 45 的批准矩阵如何映射（按 Sector×Platform vs 按 Drawing Level）？|[未找到原句]|
|8|"M (Part)" 与 Ch1 的 "FPM – Part" 是否同义？矩阵中的 "FP2" 由谁定义？|[未找到原句]（Ch1 SLIDE 17 演讲者备注仅给出缩写表）|
|9|Senior Quality Engineer（角色）何时正式接替 Rex Stuart（个人）？切换是否有时间点？|[未找到原句]（Ch5 SLIDE 67 仅说明"remains"，未给时限）|
|10|变更后是否强制做 3D 验证？规范是否位于 WI-36700 / Product Drawing Issue Checklist？|[未找到原句]（仅 Ch4 SLIDE 63 提到文件名，内容未知）|
|11|变更对库存、在制品、已发运产品的处理规则？|[未找到原句]（本章完全未涉及）|


报告结束｜模块覆盖自检：模块 1（5 条核心论点）✅｜模块 2（13 个概念操作化定义，含全部 12 项必覆盖条目）✅｜模块 3（T1–T6 共 6 张表 + 3 张补充表，全部标注 SLIDE N）✅｜模块 4（Ch2 / Ch4 / Ch5 三段对比表衔接）✅｜模块 5（4 个业务连接点 + 34 项数据清单表）✅｜模块 6（15 条金句，英文原文 + SLIDE N + 中文翻译 + 为什么记）✅

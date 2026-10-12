---
type: source
title: "Product_Drawings_101_Sept2025_ch3_Editing_Drawings_拆解报告.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch3_Editing_Drawings_拆解报告.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
key_claims: []
pages_linked: []
compile_mode: extractive
---

# Product_Drawings_101_Sept2025_ch3_Editing_Drawings_拆解报告.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch3_Editing_Drawings_拆解报告.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

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

(b) 英文定义（定义原文未直接给出，归纳自 SLIDE 36/37/43）：A mark-up of an existing drawing that visually captures the edits a requester wants made to it, produced by the submitter and attached to a formal request so that a

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch3_Editing_Drawings_拆解报告.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch3_Editing_Drawings_拆解报告.md.md`
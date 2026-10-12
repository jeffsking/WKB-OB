---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_b37f1ed43ed51422cc36a2b5b4df1d18001a693ee6c0644e"
source_file: "Product_Drawings_101_Sept2025_ch5_Appendix_DRCS_Access_拆解报告.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch5_Appendix_DRCS_Access_拆解报告.md.md"
extracted: "2026-09-30"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
---

# Product_Drawings_101_Sept2025_ch5_Appendix_DRCS_Access_拆解报告.md










章节：Ch5 Appendix: DRCS Access ｜ 覆盖幻灯片：67–80 ｜ 文档：Product Drawings 101 (KC, Sept 2025) ｜ 拆解日期：2026-08-30

学术诚信声明：本报告全部观点均可回溯至 SLIDE N（幻灯片文本层 / 演讲者备注 / 「图像内容补充」）。凡在本章及本套材料（Ch1–Ch5、逐页渲染读图记录）中检索不到原句支撑的，一律标注 [未找到原句]，不做补全、不做推测性数字填充。凡属本报告推断的内容，均显式标注 【推断】 并与原文证据分离呈现。跨文档证据（如 Baby_Wipes_101 Ch4）单独标注来源，不与本章原句混同。

本章素材边界提示（务必先读）：Ch5 共 14 页（SLIDE 67–80），其中 SLIDE 76–79 为空白模板页（正文仅 TITLE / TEXT 占位符）、SLIDE 80 为纯图片页（无文本层）。因此本章有效信息全部集中在 SLIDE 67–75（9 页），且 SLIDE 69/70 的绝大部分语义来自「图像内容补充」。报告中凡涉及 SLIDE 76–80 的推断一律标注 [未找到原句]。

## 模块1：核心论点（Core Arguments）

### 论点 1：DRCS 访问授权是「三因子模型」——Work Role × Business Sector × Reporting Work Location，且默认立场是保密与最小授权

英文概括：DRCS access is granted on a three-factor model — Work Role, Business Sector, Reporting Work Location — under an explicit confidentiality-first, least-privilege default.

支撑依据：
- SLIDE 69（图像内容补充 Step 2 声明原文）：*"Creating Product Engineering drawings is K-C confidential information. Distribution must be limited, even with your manager, to your work role access requirements. Before selecting drawing access, Access is based on: Work Role, Business Sector, Reporting Work Location."*
- SLIDE 69（图像内容补充）：页面底部强制确认项 "☐ I acknowledge that I have read the content of this page" —— 申请流程内置知情确认门禁。
- SLIDE 70（图像内容补充 Step 3 界面）：表单字段 Firstname / M.I. / Lastname / K-C ID / Manager / Business Group，示例值 *Michael D Sperl*、K-C ID 869760、Manager *Lisa L Nickel*、Business Group Baby Child Care。

为什么重要：这是全套材料里唯一一处把"谁能看图纸"写成可审计的判定式。注意其措辞强度——*"Distribution must be limited, even with your manager"*，即上级身份不构成越权访问的理由。这是与"领导打招呼就能看图"式管理最直接的对立命题。

### 论点 2：权限不是"一个开关"，而是三条互相独立的轴：Access Level（三级）× Permission（三类）× Scope（Sector / Series / Applications）

英文概括：Entitlement in DRCS is three-dimensional, not binary: an Access Level (Standard / Projects Only / None) × a Permission set (View / Work / Approve) × a Scope (Sector Access list + Product Specifications + Special Senses + Applications).

支撑依据：
- 轴 1 — Access Level：SLIDE 70（图像补充）*"DRCS Access: (Select one) ○ Standard ○ Projects Only ○ None"* —— 单选、3 个层级。
- 轴 2 — Permission：SLIDE 70（图像补充）权限三列 View / Work / Approve；SLIDE 73 操作原文 *"Place check 'View', 'Work', & 'Approve' square boxes."*
- 轴 3 — Scope：SLIDE 70（图像补充）四组可勾选范围 —— Sector Access（12 项） / Product Specifications (Additional endorsement required)（4 项） / Special Senses (Additional endorsement required)（2 项） / APPLICATIONS（6 项）。

为什么重要：把"权限"拆成三条轴，才能解释为什么"能看 Infant Care 图纸"和"能改 Infant Care 图纸"和"能批 Infant Care FPS 图纸"是三次独立申请、三次独立背书。单轴权限模型（RBAC 只给角色）做不到这一点。

### 论点 3：Approve 权不在角色-权限表的默认映射里——11 行角色映射中 0 行含 Approve，批准权必须单独申请并经经理路由

英文概括：No role in the standard role-to-access matrix carries Approve; approval authority is an exception path, requested separately and routed to the manager.

支撑依据：
- SLIDE 69（图像补充，角色-权限表共 11 行）：Access 列取值只有 *View*（6 行）与 *View, Work*（5 行）两种 —— 含 Approve 的行数 = 0/11。
- SLIDE 73："Place check 'View', 'Work', & 'Approve' square boxes." —— Approve 需主动勾选，不由角色自动派生。
- SLIDE 74：*"Then you should be able to hit 'Submit' and the request will be routed to your manager for approval."* —— 申请统一路由至经理。
- SLIDE 69（图像补充，经理须知）：经理需在路由前复核 *(view, work, approve)*、复核 *Approval level*、超标准须有 *business justification*、确认申请人已通过 *Business Approver CBT*。

为什么重要：0/11 是本模块最硬的量化发现。它说明 KC 把"批准权"从角色默认包里摘出来了——角色只给你 View/Work，要 Approve 必须单独举证（project、justification）并留痕。这直接呼应 Ch3 里 FPS 批准权收缩到 Rex Stuart 一人的单点风险。

### 论点 4：审批权正在做「下放 + 上收」的双向重构——FPM/FP1 下放给 Product Developer 换速度，FPS 保留在 Quality 换风控

英文概括：KC is running a deliberate two-way re-balancing of approval authority: FPM/FP1 approval is delegated down to Product Developers for speed, while FPS approval is retained up in Quality for control.

支撑依据：
- SLIDE 67（What will be new）：*"For the new SolidWorks product drawings product developers will be the approvers of diaper part 'FPM' and sub-assemblies 'FP1' within DRCS. This gives product developers more control and speed within the process."*
- SLIDE 67（What remains the same）：*"For final FPS drawings product developers will remain a checker. Rex Stuart of Quality remains the Approver for FPS drawings supporting production."*
- SLIDE 67：*"The drawing redline process is largely the same but the burden should lessen due to the ability to indicate cascaded parts and assemblies. Sara Schewe is in the loop and remains the Jacobs contact."*
- 交叉印证（Ch3）：Ch3 SLIDE 45 矩阵 —— M (Part) → Checker Product Developer / Approver *Product Developer*；FP1 / FP2 (Sub-Assembly) → Product Developer / *Product Developer*；FPS (Final Drawing) → Product Developer & Senior Product Developer / Senior Quality Engineer。Ch3 SLIDE 44：*"Rex Stuart is the only one who can approve a completed FPS drawing."*

为什么重要：SLIDE 67 用 "What will be new" / "What remains the same" 的对仗结构，明确承认这是一次制度切换（transition），而不是稳态描述。Ch3 中"矩阵写 Senior Quality Engineer、同页又写 Rex Stuart 是唯一批准人"的矛盾，正是这次切换的过渡期症状——目标态是角色制，当前态是个人制。

### 论点 5：Sector 不是平等的——Feminine Care 被结构性排除在 FPM/FP1/FP2 权限之外

英文概括：Sector coverage is asymmetric: the request steps are identical for Adult, Child and Infant Care, but Feminine Care has no FPM/FP1/FP2 drawing access at all.

支撑依据：
- SLIDE 68：*"These steps are the same for Adult, Child, and Infant Care. Feminine Care does not have the option for FPM,FP1,FP2 drawing access."*
- SLIDE 69（图像补充，角色-权限表）：Sector Designated Sector | Sector Location | Sector Drawings **not including FPM, FP1, FPS, Special Access or Software** | View, Work —— 即便拿到 View+Work，也默认排除 FPM/FP1/FPS。
- SLIDE 70（图像补充）：Product Specifications 需额外背书的 4 项中，Feminine Care 与 Adult / Child / Infant Care 并列在列（*Personal Care - Feminine Care Product Drawings*）——即 Feminine Care 有产品图纸类别，但没有 FPM/FP1/FP2 这一层。

为什么重要：这是"权限矩阵是业务架构镜像"的直接证据——Feminine Care 在 KC 走的是不同的图纸体系（不进入 FPM→FP1→FPS 三层 BOM 结构）。对任何想照抄 KC 权限模型的组织，这意味着权限模型必须先冻结业务架构，否则权限表会随产品线无限膨胀。

## 模块2：关键概念操作化定义

### 概念 1｜DRCS Access Level：Standard / Projects Only / None（DRCS 访问等级）

(a) DRCS 访问等级（三级：标准 / 仅限项目 / 无）

(b) English definition. The top-level, single-select entitlement that determines whether and how broadly a user holds any DRCS access. The interface label is "DRCS Access: (Select one) ○ Standard ○ Projects Only ○ None" (SLIDE 70 图像补充). KC 在本章未为三个等级提供任何定义性文字 → 三级各自的语义定义 [未找到原句]。

(c) 操作化定义（判定式 / 量化指标）
- Level ∈ {Standard, Projects Only, None}，单选，互斥（|Level| = 1，由 "Select one" 与单选按钮 ○ 确定）。
- Level = None → Permission_set = ∅（对 DRCS 无任何 View/Work/Approve）。
- Level = Projects Only → 访问范围收敛到被指派的项目集合；旁证：角色表中 ESHA Associates | Global Location | **ESHA Projects only** | View, Work（SLIDE 69）——"Projects only" 作为范围限定后缀在原文中确有出现。【推断】 Projects Only ≈ 仅被指派项目可见。
- Level = Standard → 由角色-权限表按 Work Role × Location 自动映射出 Drawing Series 与 Access（SLIDE 69），即 Standard = 走默认角色映射。【推断】
- 反向判定（风险判据）：若 Level = Standard 但申请范围超出角色-权限表默认映射 → 触发 *business justification* 与 *Business Approver CBT* 要求（SLIDE 69 经理须知）。

(d) 原文英文摘录
> "DRCS Access: (Select one) ○ Standard ○ Projects Only ○ None" — SLIDE 70（图像内容补充 Step 3 界面）
>
> "ESHA Associates | Global Location | ESHA Projects only | View, Work" — SLIDE 69（图像内容补充 Step 2 角色-权限表）

### 概念 2｜Work Role（工作角色）

(a) 工作角色（权限判定的第一因子）

(b) English definition. The applicant's functional job role, used as the primary key into the role-to-access matrix. Access is *"based on: Work Role, Business Sector, Reporting Work Location"* (SLIDE 69). The matrix enumerates 11 role-location rows (SLIDE 69 图像补充).

(c) 操作化定义（判定式 / 量化指标）
- 判定式：Access_row = f(Work Role, Reporting Work Location) → 输出 (Drawing Series, Permission_set)。
- 角色全集（按原文逐行列出，11 行）：
  1. Staff Global Engineer — Global — Sector Drawings — View, Work
  2. Staff Engineer — Plant — Plant Drawings — View, Work
  3. Engineer — Regional — Regional Drawings — View
  4. Engineer — NAR: EMEA, LAO, NA — Regional Drawings — View, Work
  5. Engineer — North America — Sector Drawings — View
  6. Research (Staff) — Global — Sector Drawings — View
  7. Maintenance — Plant — Plant Drawings — View
  8. Process Engineer (Regional) — Plant — Plant Drawings — View
  9. Process Engineer (Regional) — Regional — Regional Drawings — View
  10. Sector Designated Sector — Sector Location — Sector Drawings not including FPM, FP1, FPS, Special Access or Software — View, Work
  11. ESHA Associates — Global Location — ESHA Projects only — View, Work
- 量化分布：View, Work = 5 行；View only = 6 行；含 Approve = 0 行。

(d) 原文英文摘录
> *"Before selecting drawing access, Access is based on: Work Role, Business Sector, Reporting Work Location."* — SLIDE 69（图像内容补充 Step 2 声明原文）
>
> *"Research (Staff) | Global | Sector Drawings | View"* — SLIDE 69（图像内容补充角色-权限表）

### 概念 3｜Research (Staff)（研发岗）

(a) 研发岗（Staff 级）

(b) English definition. A Work Role entry in the access matrix whose scope is Global / Sector Drawings and whose granted permission is View only (SLIDE 69 图像补充). KC 未在本章给出该角色的职责定义 [未找到原句]。

(c) 操作化定义（判定式 / 量化指标）
- Work Role = "Research (Staff)" ∧ Location = Global ∧ Drawing Series = Sector Drawings ⇒ Permission_set = {View}，即 Work ∉ Permission_set ∧ Approve ∉ Permission_set。
- 反向推论（对本方最关键）：研发岗在 KC 权限体系中默认不是执行角色——只能读、不能改、不能批。若研发要行使 Ch3 SLIDE 45 中 Product Developer 的 FPM/FP1 批准权，必须落在 Product Developer / Engineer 序列，或走 Additional endorsement 通道。【推断】
- 同一矩阵中同为 View only 的还有 Maintenance、Process Engineer (Regional)（Plant 与 Regional 两行）、Engineer（Regional / North America 两行）——共 6 行，说明"只读"是 KC 的默认档位。

(d) 原文英文摘录
> *"Research (Staff) | Global | Sector Drawings | View"* — SLIDE 69（图像内容补充角色-权限表）

### 概念 4｜Product Developer（产品开发岗）

(a) 产品开发岗 / 提交人（submitter）

(b) English definition. The role that KC is newly empowering as the approver of diaper part FPM and sub-assembly FP1 drawings in DRCS, and that remains only a checker for final FPS drawings. Defined operatively (not as a job description) across SLIDE 67 and Ch3 SLIDE 44–45. 本章未给出该角色的职责/职级定义 [未找到原句]。

(c) 操作化定义（判定式 / 量化指标）
- Drawing Level ∈ {FPM, FP1, FP2} ⇒ Checker = Product Developer ∧ Approver = Product Developer（Ch3 SLIDE 45 矩阵；SLIDE 67 以 "will be the approvers" 确认新制）。
- Drawing Level = FPS ⇒ Checker = Product Developer & Senior Product Developer，Approver ≠ Product Developer（Ch3 SLIDE 45）。
- 在访问矩阵层面：Product Developer 未作为行项出现在 SLIDE 69 的 11 行角色-权限表中 [未找到原句]——即其权限不由 Standard 映射直接给出，需另行申请/背书。【推断】
- 速度指标（原文定性）：下放的目的被明确写为 *"more control and speed within the process"*（SLIDE 67）；量化 SLA [未找到原句]。

(d) 原文英文摘录
> *"For the new SolidWorks product drawings product developers will be the approvers of diaper part 'FPM' and sub-assemblies 'FP1' within DRCS. This gives product developers more control and speed within the process."* — SLIDE 67
>
> *"For final FPS drawings product developers will remain a checker."* — SLIDE 67
>
> 交叉：*"Product developers or 'submitters' of SolidWorks drawing changes are the approvers for FPM and FP1 drawings."* — Ch3 SLIDE 44

### 概念 5｜Senior Quality Engineer（高级质量工程师）

(a) 高级质量工程师（FPS 图纸的目标态批准角色）

(b) English definition. The Approver role for the final FPS (Final Drawing) level in the checker/approver matrix (Ch3 SLIDE 45). In current practice the person holding this authority is named explicitly: *"Rex Stuart of Quality remains the Approver for FPS drawings supporting production"* (SLIDE 67), and "Rex Stuart is the only one who can approve a completed FPS drawing" (Ch3 SLIDE 44).

(c) 操作化定义（判定式 / 量化指标）
- Drawing Level = FPS ⇒ Approver = Senior Quality Engineer（角色制，目标态）。
- 当前态判定：Approver(FPS) = {Rex Stuart}，|Approver(FPS)| = **1**，备份人数 = 0（Ch3 SLIDE 44 的 *"the only one"*）。
- 体系切换判据：SLIDE 67 用 "remains" 描述 Rex Stuart 的批准人地位，与同页 "What will be new" 的 FPM/FP1 下放构成过渡期叙述；切换时间点 [未找到原句]。
- 风险量化：单点故障风险 = 1 − (备份批准人数 / 1) = 100%；且 Ch3 SLIDE 46 的 Checkers 名单标题自带 *"Needs updating"*，构成支撑数据腐烂的二次证据。

(d) 原文英文摘录
> *"Rex Stuart of Quality remains the Approver for FPS drawings supporting production."* — SLIDE 67
>
> 交叉：*"FPS (Final Drawing) | Product Developer & Senior Product Developer | **Senior Quality Engineer**"* — Ch3 SLIDE 45；*"Rex Stuart is the only one who can approve a completed FPS drawing."* — Ch3 SLIDE 44

### 概念 6｜ECM / External Contract Manufacturer（外部合同制造商）+ Vendor Drawings（供应商图纸）

(a) 外部合同制造商 / 代工厂；供应商图纸（Sector Access 条目）

(b) English definition. 本章（Ch5，SLIDE 67–80）中不存在 "ECM"、"External Contract Manufacturer"、"contract manufacturer" 任何原句 → 定义 [未找到原句]。本章唯一与"外部方"直接相关的原文证据是 Sector Access 列表中的条目 "Personal Care - Vendor Drawings" 与 APPLICATIONS 区块中的 "PARTNERS PORTAL"（SLIDE 70 图像补充）。
跨文档旁证（非本章，来源 Baby_Wipes_101 Sept2025）：Ch4 SLIDE 31 出现 *"Improve portfolio margins by mitigating incremental costs from ECMs and imported products"* 与 *"Differentiated ECM partnership to drive consumer-preferred Wipe"*；该文档 Ch2 SLIDE 10 列出具名代工厂 Merisco / Tufco（USA） 与 Nice Pack（U.K.） —— 即 KC 确实常态化使用外部代工。缩写展开 ECM = External Contract Manufacturer 为他章报告推导，原文未直接展开 [未找到原句]。

(c) 操作化定义（判定式 / 量化指标）
- 本章可验证的外部分区：Sector Access ∋ "Personal Care - Vendor Drawings" —— 供应商图纸是一个独立的 Sector 条目，与个人护理各业务板块（Adult/Child/Infant/Feminine Care）平级并列，需单独勾选。【推断】 这意味着"给外部方的图纸"在 KC 体系内是一个被隔离的图纸子集，而非从业务板块图纸里临时挑几张。
- PARTNERS PORTAL 判定：该入口与 SolidWorks (K-C Internal - North & South America Only) 同在 APPLICATIONS 区块；后者被显式标注 K-C Internal，前者未标注 Internal → 【推断】 PARTNERS PORTAL 为面向外部伙伴（含代工厂）的受控通道。Portal 内部的具体权限分级 [未找到原句]。
- 外发边界硬约束（本章唯一明文保密条款）：*"Distribution must be limited, even with your manager, to your work role access requirements."*（SLIDE 69）→ 判定式：外发范围 ⊆ 接收方的 work role access requirements，不由申请人的职级或关系决定。【推断】
- 代工厂身份与规模：具名代工厂 3 家（Merisco / Tufco / Nice Pack，Baby_Wipes_101 Ch2 SLIDE 10）；本章未给出"代工厂可访问 Sector 数量" [未找到原句]。

(d) 原文英文摘录
> "Personal Care - Vendor Drawings" — SLIDE 70（图像内容补充 Sector Access 列表）
>
> *"APPLICATIONS：AutoCAD-Canada / AutoCAD-Mexico / AutoCAD-United States / Research Files / SolidWorks (K-C Internal - North & South America Only)；PARTNERS PORTAL"* — SLIDE 70（图像内容补充）
>
> *"Creating Product Engineering drawings is K-C confidential information. Distribution must be limited, even with your manager, to your work role access requirements."* — SLIDE 69

### 概念 7｜Permissions：View / Work / Approve（权限三档）

(a) 权限三档：查看 / 作业 / 批准

(b) English definition. The three orthogonal permission columns presented both in the access-request UI (SLIDE 70 图像补充：*"View / Work / Approve") and as checkboxes in the request flow (SLIDE 73："Place check 'View', 'Work', & 'Approve' square boxes."*). KC 未在本章逐条定义三档的具体动作集 [未找到原句]。

(c) 操作化定义（判定式 / 量化指标）
- Permission_set ⊆ {View, Work, Approve}，由勾选决定，不由角色自动派生（角色表只到 View/Work 两档，Approve 出现 0 次）。
- View 的动作集（由 Ch1/Ch4 交叉还原）：Download copy（Ch1 SLIDE 10）/ View image（Ch1 SLIDE 11）/ Print file（Ch1 SLIDE 12）/ Where Used and BOM information（Ch1 SLIDE 13）/ Access back issues and drawing information（Ch1 SLIDE 14）。→ "下载原文件"属 View 档，这是 3D 查看链路成立的前提（见模块 4）。
- Work 的动作集：Checkout/Release（Ch1 SLIDE 9）+ 图纸创建/修订（对应 Ch3 SLIDE 44 的 8 hrs per drawing 工时经验值）。【推断】
- Approve 的动作集：在 DRCS 中作为 DRCS Checker/Approver / DRCS Approver 签署放行（Ch3 图像补充 p43-45 工单字段）。【推断】
- 逐级包含判定：原文未明示 Work ⊇ View、Approve ⊇ Work。由于三者为并列复选框，【推断】 三档相互独立、需分别勾选——即可能出现"Work 而无 View"的配置错误，实际由经理复核环节兜底（经理须知要求路由前复核 view/work/approve）。

(d) 原文英文摘录
> *"Place check 'View', 'Work', & 'Approve' square boxes."* — SLIDE 73
>
> *"权限三列：View / Work / Approve"* — SLIDE 70（图像内容补充 Step 3 界面）

### 概念 8｜Sector / Sector Access（业务板块）

(a) 业务板块（权限判定的第二因子）

(b) English definition. The business segment dimension of access scope, enumerated in the request UI as a checkable list. Per SLIDE 69, access is based on *"Work Role, Business Sector, Reporting Work Location"*; the UI also carries a separate Business Group field (example value: Baby Child Care, SLIDE 70).

(c) 操作化定义（判定式 / 量化指标）
- Scope_sector ⊆ Sector_Access_List，|Sector_Access_List| = **12**（按原文逐条列出，见模块 3 T3）：Air Systems, Misc. Process Support/Bldg. / Family Care / Health Care / K-C Professional / Nonwovens / Nonwovens - Process Support/Building Drawings / Personal Care - Adult Care / Personal Care - Child Care / Personal Care - Feminine Care / Personal Care - Infant Care / Personal Care - Process Support/Building Drawings / Personal Care - Vendor Drawings。
- 板块不平等判据（SLIDE 68）：FPM/FP1/FP2_Access(Adult Care) = FPM/FP1/FP2_Access(Child Care) = FPM/FP1/FP2_Access(Infant Care) = True；FPM/FP1/FP2_Access(**Feminine Care**) = **False**（原文：*"does not have the option"*）。
- 默认排除判据（SLIDE 69 角色表 Sector Designated Sector 行）：即便 Permission = View, Work，Drawing Series 仍为 *"Sector Drawings not including FPM, FP1, FPS, Special Access or Software"* → FPM/FP1/FPS/Special Access/Software 五类默认是"不随板块权限自动发放"的。
- 与业务板块平行的两套"需额外背书"范围（SLIDE 70）：Product Specifications (Additional endorsement required) = 4 项；Special Senses (Additional endorsement required) = 2 项。判定式：获得 Sector 权限 ≠ 获得该 Sector 的产品图纸权限。

(d) 原文英文摘录
> *"Sector Access 列表：Air Systems, Misc. Process Support/Bldg. / Family Care / Health Care / K-C Professional / Nonwovens / Nonwovens - Process Support/Building Drawings / Personal Care - Adult Care / Personal Care - Child Care / Personal Care - Feminine Care / Personal Care - Infant Care / Personal Care - Process Support/Building Drawings / Personal Care - Vendor Drawings"* — SLIDE 70（图像内容补充）
>
> *"Product Specifications (Additional endorsement required)：Health Care PQD, LFA, FPS, and PQD / Personal Care - Adult Care Product Drawings / Personal Care - Child Care Product Drawings / Personal Care - Feminine Care Product Drawings / Personal Care - Infant Care Product Drawings"* — SLIDE 70（图像内容补充）

### 概念 9｜Personal Care - Infant Care（个人护理—婴儿护理，示例操作板块）

(a) 个人护理 — 婴儿护理（Ch5 演示路径所选板块）

(b) English definition. One of the 12 entries in the Sector Access list (SLIDE 70), and the sector chosen for the worked example in the step-by-step request flow. It appears twice in the UI: once as a Sector Access entry, and once under Product Specifications (Additional endorsement required) as "Personal Care - Infant Care Product Drawings".

(c) 操作化定义（判定式 / 量化指标）
- 两阶段判定：① 勾选 Personal Care - Infant Care（Sector Access）⇒ 获得该板块非产品图纸类访问；② 另行勾选/背书 Personal Care - Infant Care Product Drawings（Product Specifications 区）⇒ 才获得 FPS/产品图纸访问。两阶段缺一不可。
- 地理下钻层级（SLIDE 71–72）：Product Specifications → Personal Care Infant Care（点 + 展开）→ North Atlantic（再点 + 展开）。即访问树至少 3 层：类别 → 板块 → 地理区域。
- 业务适用性判据（SLIDE 68）：Infant Care 与 Adult Care、Child Care 流程完全相同，且具备 FPM/FP1/FP2 权限选项（对比 Feminine Care 无此选项）。
- 与卫材业务的对接点：SLIDE 67 的批准权下放条款正是以 "diaper part 'FPM' and sub-assemblies 'FP1'" 表述 —— 即纸尿裤品类是新制的第一落点。

(d) 原文英文摘录
> *"Click the Personal Care Infant Care Plus Sign for drop Down Menu"* — SLIDE 71（另见 图像内容补充 图示操作提示）
>
> *"Click the North Atlantic Plus Sign for drop Down Menu"* — SLIDE 72
>
> *"Personal Care - Infant Care Product Drawings"（位于 Product Specifications (Additional endorsement required) 区）* — SLIDE 70（图像内容补充）

### 概念 10｜Special Senses（专项标准，需额外背书）：C079 / C800

(a) 专项标准（C079 胶设备与标准；C800 个人护理工程设计标准）

(b) English definition. A distinct scope category in the request UI, flagged *"(Additional endorsement required)"*, containing 2 numbered standards (SLIDE 70 图像补充)：
- C079 | Adhesive Equipment and Standards —— 胶（黏剂）设备与标准；
- C800 | Personal Care Engineering Design Standards —— 个人护理工程设计标准。
KC 未在本章说明 C079/C800 的编号规则、归口部门或内容范围 [未找到原句]。

(c) 操作化定义（判定式 / 量化指标）
- 独立范围判据：Special_Senses 是与 Sector Access、Product Specifications、APPLICATIONS 并列的第四个可勾选区块，且带 Additional endorsement required 标记 → 判定式：Special_Senses ⊄ Sector_Access，即勾选了 Personal Care - Infant Care 不等于可访问 C079/C800，必须单独背书。
- 编号判据：Code ∈ {C079, C800}，编号形态为 C + 3 位数字，与图纸号前缀（如 C153-FPS-01575，Ch1 SLIDE 9 图像补充）的 C + 3 位数字形态同构 → 【推断】 C079/C800 与图纸系列编号同属一套 C 系列编码体系，但独立于 Infant Care（C153）等板块图纸系列。
- 胶标准独立性量化：在 12 条 Sector Access 中，0 条以"Adhesive"命名；2 条 Special Senses 中有 1 条（C079，占 50%）专指胶设备与标准 → 胶设备标准在 KC 是跨板块、单列的横向标准，而非某个业务板块的下属文件。
- 与卫材胶黏剂的对接判据：Ch1 SLIDE 17 定义 FP1 – Assembly 时给出的示例恰是 *"Ex. – Nonwoven + Adhesive"*；Ch2 图像补充 p34 BOM 中出现 PAD TO LINER ADHESIVE 125MM CD × 476MM MD、LEG ELASTIC ADHESIVE 232MM CD × 279MM MD、EAR REINFORCEMENT ADH 268 × 200 × 500MM MD 等以尺寸定义的胶涂布项。→ 判定式：胶规格 = 图纸上的 CD/MD 涂布尺寸，因此胶设备标准（C079）是胶涂布尺寸可落地的前提。【推断】

(d) 原文英文摘录
> *"Special Senses (Additional endorsement required)：C079 | Adhesive Equipment and Standards；C800 | Personal Care Engineering Design Standards"* — SLIDE 70（图像内容补充）
>
> 交叉（胶与图纸的关系）：*"FP1 – Assembly / Groupings of FPM drawings that are often associated together / Ex. – Nonwoven + Adhesive"* — Ch1 SLIDE 17

### 概念 11｜Access Request 流程（权限申请七步流程 + 经理审批）

(a) 权限申请流程（Step 1–7；含经理审批、业务背书、CBT 前置）

(b) English definition. The seven-step, self-service procedure documented in the appendix for obtaining or updating DRCS access/approval level, terminating in a manager-routed approval: *"Then you should be able to hit 'Submit' and the request will be routed to your manager for approval."* (SLIDE 74)

(c) 操作化定义（判定式 / 量化指标）
- 步骤数 = 7（SLIDE 68–74，逐页对应，见模块 3 T5）。
- 浏览器约束：*"Via Microsoft Edge bring Up the CAD Home Page."*（SLIDE 68）→ 判定式：Browser = Microsoft Edge（硬约束，非建议）。
- 前置确认门禁：*"☐ I acknowledge that I have read the content of this page"*（SLIDE 69）→ Confirmed = True 才能进入下一步。
- 强制填写字段（SLIDE 74）：{Your name, project, why you are asking for the update} + 表单字段 {Firstname, M.I., Lastname, K-C ID, Manager, Business Group}（SLIDE 70）→ "业务理由（project / why）"是必填项，不是可选项。
- 经理侧门禁（7 条，其中 5 条可辨认）（SLIDE 69 图像补充）：① 由经理判断角色与访问需求；② 路由前复核 *view, work, approve*；③ 复核 *Approval level*；④ 超出标准须有 *business justification*；⑤ 确认申请人已通过 *Business Approver CBT*。其余 2 条原文未提供 [未找到原句]。
- 审批链路拓扑：申请人 → Submit → 经理审批 → 生效；是否为两级（经理 + Business Approver / 数据owner） [未找到原句]；SLA / 处理时长 [未找到原句]。
- 兜底支持：求助电话 (920)721-5555（SLIDE 70 图像补充）；培训文档入口 *'Training Resources' → 'Documents'*（SLIDE 75）。

(d) 原文英文摘录
> *"Then you should be able to hit 'Submit' and the request will be routed to your manager for approval."* — SLIDE 74
>
> *"DRCS may prompt you for additional information. Please fill out the boxes: Your name, project, why you are asking for the update, etc…."* — SLIDE 74
>
> *"Via Microsoft Edge bring Up the CAD Home Page."* — SLIDE 68

### 概念 12｜Cross Sector Access（跨板块访问）

(a) 跨业务板块访问

(b) English definition. 术语 "Cross Sector Access" 在本章及本套材料中均无原句 → 定义 [未找到原句]。本章可验证的相关事实是三条：① Sector Access 为可勾选列表（12 项并列），UI 层面允许同时选择多个板块；② 访问树存在地理维度下钻（Personal Care Infant Care → North Atlantic，SLIDE 71–72）；③ 经理须知要求超出标准须有 business justification（SLIDE 69）。

(c) 操作化定义（判定式 / 量化指标）
- 多板块判定：|Scope_sector| ≥ 1（列表式勾选，非单选；对比 DRCS Access 用 ○ 单选按钮 → 板块可多选、等级只能选一）。【推断】
- 跨板块合理性判据（唯一原文依据）：若 Scope_sector 超出 Work Role 的默认映射 ⇒ 需 business justification 且申请人须通过 Business Approver CBT（SLIDE 69 经理须知）。→ 判定式：Cross_Sector_Request = True ⇒ Justification_Required = True ∧ CBT_Completed = True。
- 跨板块的地理子维度：North Atlantic 出现在 Infant Care 之下（SLIDE 72）→ 跨板块申请还需指定地理范围（Reporting Work Location，三因子之一）。【推断】
- 反向证据（板块间的结构性差异）：SLIDE 68 明示 Feminine Care 无 FPM/FP1/FP2 → 【推断】 跨板块权限不是简单的集合并集，板块间图纸体系异构，跨板块申请必然落入 business justification 通道。
- 禁止推定：KC 未给出"允许/禁止跨板块"的明文规则、未给出跨板块申请的比例或审批通过率 → 上述数值一律 [未找到原句]。

(d) 原文英文摘录
> *"These steps are the same for Adult, Child, and Infant Care. Feminine Care does not have the option for FPM,FP1,FP2 drawing access."* — SLIDE 68
>
> *"Before selecting drawing access, Access is based on: Work Role, Business Sector, Reporting Work Location."* — SLIDE 69
>
> *"超标准须有 business justification；确认申请人已通过 Business Approver CBT"* — SLIDE 69（图像内容补充，经理须知）

## 模块3：证据链（Evidence Chain）

### T1 — 角色 × 权限矩阵表（Roles × View / Work / Approve）



数据来源：SLIDE 69（图像内容补充 Step 2 角色-权限表，共 11 行）。
说明：原文表列为 Location / Drawing Series / Access；本表原样保留原文字段，并将 Access 列按原文展开为 View / Work / Approve 3 个布尔列（✓ = 原文出现，— = 原文未出现）。原文未使用的单元格一律留 —，不做补全。

|||||||||
|---|---|---|---|---|---|---|---|
|1|Staff Global Engineer|Global|Sector Drawings|✓|✓|—|SLIDE 69|
|2|Staff Engineer|Plant|Plant Drawings|✓|✓|—|SLIDE 69|
|3|Engineer|Regional|Regional Drawings|✓|—|—|SLIDE 69|
|4|Engineer|NAR: EMEA, LAO, NA|Regional Drawings|✓|✓|—|SLIDE 69|
|5|Engineer|North America|Sector Drawings|✓|—|—|SLIDE 69|
|6|Research (Staff)|Global|Sector Drawings|✓|—|—|SLIDE 69|
|7|Maintenance|Plant|Plant Drawings|✓|—|—|SLIDE 69|
|8|Process Engineer (Regional)|Plant|Plant Drawings|✓|—|—|SLIDE 69|
|9|Process Engineer (Regional)|Regional|Regional Drawings|✓|—|—|SLIDE 69|
|10|Sector Designated Sector|Sector Location|*Sector Drawings not including FPM, FP1, FPS, Special Access or Software*|✓|✓|—|SLIDE 69|
|11|ESHA Associates|Global Location|ESHA Projects only|✓|✓|—|SLIDE 69|
|—|合计（11 行）|—|—|11/11|5/11|0/11|—|


表外角色（不在本矩阵内，由其他章节的审批矩阵给出）

|||||||
|---|---|---|---|---|---|
|Product Developer|FPM / FP1 / FP2 的 Checker 兼 Approver；FPS 仅 Checker|[未找到原句]|[未找到原句]|✓（FPM/FP1/FP2）|SLIDE 67；Ch3 SLIDE 44、45|
|Senior Product Developer|FPS 的 Checker 之一（与 submitter 双签）|[未找到原句]|[未找到原句]|—|Ch3 SLIDE 44、45|
|Senior Quality Engineer|FPS 的 Approver（角色制目标态）|[未找到原句]|[未找到原句]|✓（FPS）|Ch3 SLIDE 45|
|Rex Stuart（Quality，具名个人）|"the only one who can approve a completed FPS drawing"|[未找到原句]|[未找到原句]|✓（FPS，当前态唯一）|SLIDE 67；Ch3 SLIDE 44|
|ECM / External Contract Manufacturer|本章无该角色的任何权限行|[未找到原句]|[未找到原句]|[未找到原句]|Ch5 全章 [未找到原句]；跨文档旁证见概念 6|


### T2 — DRCS Access 三级定义表（Standard / Projects Only / None：谁能看到什么）



数据来源：SLIDE 70（图像内容补充 Step 3 界面）。
重要诚信说明：原文仅提供 3 个选项标签，未提供任何一级的定义文字。下表"原文可验证内容"列只填原文；"语义还原"列全部标注 【推断】；凡无原文的单元格标 [未找到原句]。

|||||||
|---|---|---|---|---|---|
|Standard|*"○ Standard"*（单选按钮标签）|由 Work Role × Reporting Work Location 自动映射出 Drawing Series 与 Access（View / View+Work），即走默认角色包|View / Work / Approve 三列均可申请，但 Approve 需单独勾选 + 经理路由|对应 SLIDE 69 角色表 11 行中除 #11 外的多数行（如 Staff Global Engineer → Sector Drawings → View, Work）|SLIDE 70（三级标签）；SLIDE 69（映射规则）|
|Projects Only|*"○ Projects Only"*；旁证措辞 *"ESHA Projects only"*（角色表 #11）|访问范围收敛到被指派的具体项目集合，非全板块、非全图纸系列|同上；范围由项目清单限定而非由板块限定|角色表 #11 `ESHA Associates|Global Location|
|None|"○ None"|不授予任何 DRCS 访问；Permission_set = ∅|三列均不适用|无对应角色行——角色表中无 None 档，【推断】 None 用于"曾持有、现需回收"或"仅用 SPOT 不需 DRCS"的人员|SLIDE 70|


三级的边界条件（原文 vs 推断，严格分离）

|||||
|---|---|---|
|三级各自的适用人群定义|无|[未找到原句]|
|Standard 与 Projects Only 的范围差|仅能从 ESHA Projects only 反推"项目限定"语义|【推断】|
|选择 None 后是否仍能用 The SPOT 看图纸快照|无（但 Ch1 SLIDE 4–7 的 SPOT 路径未提及任何 DRCS 权限）|[未找到原句] / 见模块 4|
|三级之间切换是否需要重新走 7 步流程|无|[未找到原句]|
|三级的有效期 / 复检周期|无|[未找到原句]|


### T3 — Sector 分类全表（按原文列出全部 Sector）



数据来源：SLIDE 70（图像内容补充 Step 3 界面）。原文以 / 分隔列出，共 12 项。

3-A｜Sector Access 列表（原文全量，12 项）

|||||||
|---|---|---|---|---|---|
|1|Air Systems, Misc. Process Support/Bldg.|空气系统 / 杂项工艺支持与厂房|否|否|SLIDE 70|
|2|Family Care|家庭护理|否|否|SLIDE 70|
|3|Health Care|健康护理|否|是（*Health Care PQD, LFA, FPS, and PQD*）|SLIDE 70|
|4|K-C Professional|K-C 专业（B2B）|否|否|SLIDE 70|
|5|Nonwovens|非织造布|否|否|SLIDE 70|
|6|Nonwovens - Process Support/Building Drawings|非织造布 — 工艺支持/厂房图纸|否|否|SLIDE 70|
|7|Personal Care - Adult Care|个人护理 — 成人护理|是|是（*Personal Care - Adult Care Product Drawings*）|SLIDE 70|
|8|Personal Care - Child Care|个人护理 — 儿童护理|是|是（*Personal Care - Child Care Product Drawings*）|SLIDE 70|
|9|Personal Care - Feminine Care|个人护理 — 女性护理|是|是（但无 FPM/FP1/FP2，见 SLIDE 68）|SLIDE 70；SLIDE 68|
|10|Personal Care - Infant Care|个人护理 — 婴儿护理|是|是（*Personal Care - Infant Care Product Drawings*）|SLIDE 70|
|11|Personal Care - Process Support/Building Drawings|个人护理 — 工艺支持/厂房图纸|是|否|SLIDE 70|
|12|Personal Care - Vendor Drawings|个人护理 — 供应商图纸|是|否|SLIDE 70|


3-B｜Product Specifications（Additional endorsement required）— 需额外背书的第二层范围（4 项）

|||||
|---|---|---|---|
|1|Health Care PQD, LFA, FPS, and PQD|健康护理 PQD、LFA、FPS 与 PQD|SLIDE 70|
|2|Personal Care - Adult Care Product Drawings|个人护理—成人护理产品图纸|SLIDE 70|
|3|Personal Care - Child Care Product Drawings|个人护理—儿童护理产品图纸|SLIDE 70|
|4|Personal Care - Feminine Care Product Drawings|个人护理—女性护理产品图纸|SLIDE 70|
|5|Personal Care - Infant Care Product Drawings|个人护理—婴儿护理产品图纸|SLIDE 70|




注：原文该区以 / 分隔共列出 5 个条目（Health Care 合并计为 1 项），其中 Personal Care 系占 4 项。此处按原文逐条如实列出，不合并。

3-C｜APPLICATIONS（软件与应用入口，6 项）

||||||
|---|---|---|---|---|
|1|AutoCAD-Canada|AutoCAD（加拿大）|未标注|SLIDE 70|
|2|AutoCAD-Mexico|AutoCAD（墨西哥）|未标注|SLIDE 70|
|3|AutoCAD-United States|AutoCAD（美国）|未标注|SLIDE 70|
|4|Research Files|研发文件|未标注|SLIDE 70|
|5|SolidWorks (K-C Internal - North & South America Only)|SolidWorks（K-C 内部 — 仅限北美与南美）|是|SLIDE 70|
|6|PARTNERS PORTAL|伙伴门户|未标注|SLIDE 70|


### T4 — Special Senses 表（编号 / 名称 / 适用范围）



数据来源：SLIDE 70（图像内容补充）。区块标题原文含 *"Additional endorsement required"*。

||||||||
|---|---|---|---|---|---|
|C079|Adhesive Equipment and Standards|胶（黏剂）设备与标准|原文仅给出名称，未写明适用范围 [未找到原句]|横向标准：覆盖胶黏剂施工设备（热熔胶喷枪/喷嘴/涂布头等）与胶相关标准；与 Sector 平级单列，故推断为跨 Personal Care 各板块通用而非板块下属文件|需额外背书（Additional endorsement required）|SLIDE 70|
|C800|Personal Care Engineering Design Standards|个人护理工程设计标准|原文仅给出名称，未写明适用范围 [未找到原句]|横向标准：覆盖个人护理工程设计的通用规范（推断为 Infant/Child/Adult/Feminine Care 共用的设计基线）|需额外背书（Additional endorsement required）|SLIDE 70|


T4 补充：胶相关证据在整套材料中的分布（用于判断 C079 的分量）

|||||
|---|---|---|---|
|FP1 的定义示例即"非织造布 + 胶"|*"FP1 – Assembly / Groupings of FPM drawings that are often associated together / Ex. – Nonwoven + Adhesive"*|Ch1 SLIDE 17|胶是 FP1 层的一等公民，C079 是该层的设备/标准依据|
|胶以 CD/MD 尺寸形式写进 BOM|*"PAD TO LINER ADHESIVE 125MM CD × 476MM MD"、"LEG ELASTIC ADHESIVE 232MM CD × 279MM MD"、"EAR REINFORCEMENT ADH 268 × 200 × 500MM MD"*|Ch2 图像补充 p34|胶规格 = 涂布尺寸，尺寸能否落地取决于胶设备能力（C079）|
|胶作为独立 FPM 图纸|*"DIAPER, PAD TO LINER, ADHESIVE, 125MM CD X 367MM MD | C153-FPM-00154-B-01"、"DIAPER, EAR ADHESIVE... | C153-FPM-00155-B-01"*|Ch2 图像补充 BOM_A|胶有独立图号，属 FPM 层 → 其变更走 Product Developer 批准（SLIDE 67 新制）|
|剖面图即"胶布置图"|图纸标题 *"CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT"*|Ch2 图像补充 p24-25|胶布置是剖面图的核心内容之一|
|Special Senses 中胶标准占比|2 项 Special Senses 中 1 项为胶（50%）|SLIDE 70|胶标准在 KC 横向标准体系中占比极高|


### T5 — 权限申请流程步骤表（Access Request，Step 1–7）



数据来源：SLIDE 68–SLIDE 74（每页对应一步）；界面字段来自 SLIDE 70、声明页来自 SLIDE 69（图像内容补充）。

|||||||
|---|---|---|---|---|---|
|1|SLIDE 68|*"Step 1 DRCS Home Page / Open Software Access Hyperlink / Via Microsoft Edge bring Up the CAD Home Page."*|从 DRCS 首页打开 Software Access 链接；须用 Microsoft Edge 打开 CAD 主页|CAD Home Page（另见 Ch1 图像补充 p8：Central CAD 主页 → *DRCS – Drawing Release Control System*）|浏览器约束（Edge）|
|2|SLIDE 69|*"Step 2 / Click Box and Hit Next"*|阅读保密声明页并勾选确认框，点击 Next|声明原文：*"Creating Product Engineering drawings is K-C confidential information. Distribution must be limited, even with your manager, to your work role access requirements. Before selecting drawing access, Access is based on: Work Role, Business Sector, Reporting Work Location."*；底部 *"☐ I acknowledge that I have read the content of this page"*；含经理须知 7 条|强制知情确认 + 三因子声明|
|3|SLIDE 70|*"Step 3 / Open Product Specifications Drop Down"*|打开 Product Specifications 下拉；进入系统 *"Drawing and CAD Software Access"*|表单字段：Firstname / M.I. / Lastname / K-C ID / Manager / Business Group（示例：Michael D Sperl，K-C ID 869760，Manager Lisa L Nickel，Business Group Baby Child Care）；DRCS Access: ○ Standard ○ Projects Only ○ None；三列权限 View / Work / Approve；四大范围区块|身份字段 + 三因子 + 三级 + 三权限在同一屏|
|4|SLIDE 71|*"Step 4 / Click the Personal Care Infant Care Plus Sign for drop Down Menu"*|展开 Personal Care Infant Care 节点|访问树第 2 层（类别 → 板块）|板块下钻|
|5|SLIDE 72|*"Step 5 / Click the North Atlantic Plus Sign for drop Down Menu"*|展开 North Atlantic 节点|访问树第 3 层（板块 → 地理区域）|地理下钻|
|6|SLIDE 73|*"Step 6 / Place check 'View', 'Work', & 'Approve' square boxes."* … *"When boxes have been checked hit the 'Next' icon."*|勾选所需权限复选框，点 Next|同一页附注："This may look a little different than your screen because I already had checked the boxes and went back into DRCS to take the screen shots."|权限勾选点（Approve 在此产生）|
|7|SLIDE 74|*"Step 7 / DRCS may prompt you for additional information. Please fill out the boxes: Your name, project, why you are asking for the update, etc…."* → *"Then you should be able to hit 'Submit' and the request will be routed to your manager for approval."*|补充业务理由信息，提交后路由至经理审批|经理须知（可辨认 5 条 / 共 7 条）：判断角色与访问需求；路由前复核 view/work/approve；复核 Approval level；超标准须 business justification；确认已通过 Business Approver CBT|经理审批 + 业务理由举证 + CBT 前置|


T5 附：流程的"原文未覆盖"清单（避免误用）

|||
|---|---|
|经理审批之后的环节（是否有二级审批、是否自动开通、开通耗时）|[未找到原句]|
|经理须知 7 条中未摘录的 2 条|[未找到原句]|
|申请被拒后的申诉/重申路径|[未找到原句]|
|权限的有效期与定期复检（recertification）机制|[未找到原句]|
|离职/转岗时的权限回收流程（对应 None 档的触发方式）|[未找到原句]|
|Additional endorsement 的具体背书人/背书流程|[未找到原句]|
|SLIDE 76–80 的内容（空白模板页 + 纯图片页）|[未找到原句]|


## 模块4：章节间衔接（Chapter Connections）

### 4-1｜与 Ch1（Finding Drawings，SLIDE 1–19）：SPOT（索引）与 DRCS（存储）的权限差异

核心判断：SPOT 是"公开的索引层"，DRCS 是"受控的存储层"——两层的权限门槛完全不同，Ch1 全程未提任何 DRCS 权限，Ch5 才补上这道门锁。

|||||
|---|---|---|---|
|系统定位|规格文档（MS Word）+ 内嵌图纸快照 + 图号|图纸文件本体 + 版本 + BOM 关系|Ch1 SLIDE 7（*"find a copy of the drawing and the drawing number"）vs Ch1 SLIDE 8（"Detailed product drawings are found in DRCS"*）|
|入口|The SPOT → Variant Specification Search → SPOT Specifications → 用筛选器导航 → 点 Variant Property Spec 号下载|Central CAD Homepage → DRCS – Drawing Release Control System|Ch1 SLIDE 4–6；Ch1 SLIDE 8 + 图像补充 p8|
|权限门槛（Ch1 描述）|Ch1 未提及任何权限要求 → [未找到原句]|Ch1 未提及权限，仅在导航条露出 News \| Search \| Create \| Change Title \| **Issue** \| **Approve**|Ch1 SLIDE 9 图像补充|
|权限门槛（Ch5 补齐）|本章未说明 SPOT 是否需要 DRCS 权限 → [未找到原句]|DRCS Access 三级 + View/Work/Approve 三档 + Work Role × Business Sector × Reporting Work Location 三因子|Ch5 SLIDE 69、70|
|产出物粒度|图纸的一份副本（copy）+ 图号，贴在规格文档最后一页|可 Download copy / View image / Print file / Where Used and BOM / back issues 的文件级操作|Ch1 SLIDE 7、9–14|
|文件类型|MS Word 文档（.docx）|.sldasm / .sldprt / .slddrw / DWG / TIF|Ch4 图像补充；Ch2 图像补充|
|检索语法|变体/属性规格号 + 筛选器|图号直查 + *Advanced Search*（PREFIX × TYPE 双筛选）|Ch1 SLIDE 6、15|
|Ch4 的一句话总结|*"Found on last page of specs from The SPOT"*|*"Full drawings in DRCS"*|SLIDE 63（Ch4 Final thoughts）|


衔接结论（【推断】）：
1. SPOT 是低门槛层，DRCS 是高门槛层——Ch1 教的是"怎么找"，Ch5 教的是"凭什么能看"。二者的分工在 SLIDE 63 被压缩成两句对仗原文。
2. Download copy 属 View 档（Ch1 SLIDE 10 是 DRCS 的文件级操作之一），而 View 是 SLIDE 69 角色表中 11/11 行都有的一档 → 只要拿到 DRCS 的 View，就走完了 Ch1 的全部动作。这是"最低可用权限 = View"的实证锚点。
3. 采购/战略职能的最小可行权限就是 View——不看 DRCS 也能从 SPOT 拿到图号与图纸副本（Ch1 SLIDE 7），但要拿原文件（做 BOM/用量分析、3D 查看）必须进 DRCS。


### 4-2｜与 Ch3（Editing Drawings，SLIDE 35–46）：变更批准（Approve）需要哪一级权限

核心判断：批准权按图纸层级分叉——FPM/FP1/FP2 下放给 Product Developer，FPS 上收至 Quality；而无论哪一级，Approve 都不在角色默认包里（0/11），必须单独申请并经理路由。

|||||
|---|---|---|---|
|FPM（Part）|Checker = Product Developer；Approver = Product Developer|Approve 需在 SLIDE 73 单独勾选，不由角色派生|新制下 Product Developer 自查自批（Ch3 SLIDE 45 + SLIDE 67：*"product developers will be the approvers"*）|
|FP1 / FP2（Sub-Assembly）|Checker = Product Developer；Approver = Product Developer|同上|同上；SLIDE 67 明确受益点是 *"more control and speed"*|
|FPS（Final Drawing）|Checker = Product Developer & Senior Product Developer（双人）；Approver = Senior Quality Engineer|FPS 类图纸位于 *"Product Specifications (Additional endorsement required)"* 区块（SLIDE 70）→ 除 Approve 勾选外还需额外背书|两级门禁：Approve 勾选 + Product Specifications 额外背书|
|当前态 vs 目标态|SLIDE 44：*"Rex Stuart is the only one who can approve a completed FPS drawing."*（个人制）|SLIDE 67：*"Rex Stuart of Quality remains the Approver for FPS drawings supporting production."（"remains"* = 旧制延续）|Ch3 的冲突在 Ch5 得到解释：这是新旧制切换，不是文档错误；切换时间点 [未找到原句]|
|Approve 是否为角色默认权限|矩阵只回答"谁批"，不回答"权限怎么开"|角色-权限表 11 行中 Approve 出现 0 次（SLIDE 69）；Approve 是 SLIDE 73 的一个复选框|批准权 = 例外路径，不是角色属性|
|审批链路|提交 → Jacobs（外包制图）→ Checker → Approver|申请 → Submit → 经理审批（SLIDE 74）|两条独立的审批链：一条批图纸内容（Ch3），一条批人的权限（Ch5）；互不为替代条件|
|成本/工时|*"General rule of thumb for 'Estimated Hours' is 8 hrs per drawing to be created/revised"*|未涉及时工|Ch3 SLIDE 44；Ch5 [未找到原句]|
|外包方|Jacobs Engineering（*Sara Schewe … remains the Jacobs contact*）|未涉及|SLIDE 67；Ch3 SLIDE 36、43|


回答"变更批准需要哪一级权限"（分层答案）

||||||
|---|---|---|---|---|
|FPM / FP1 / FP2 图纸|Product Developer（新制）|Approve（勾选）|未在原文明示 → [未找到原句]|SLIDE 67；Ch3 SLIDE 44、45|
|FPS 图纸|Senior Quality Engineer（目标态）／Rex Stuart（当前态唯一人）|Approve（勾选）|是（FPS 位于 *Product Specifications (Additional endorsement required)*）|SLIDE 67、70；Ch3 SLIDE 44、45|
|自己的 Approve 权限本身|—|—|是（经理审批 + business justification + Business Approver CBT）|SLIDE 73、74；SLIDE 69 经理须知|




⚠️ 关键歧义（不得省略）：SLIDE 70 的 Product Specifications (Additional endorsement required) 区块把 FPS 与四个 Personal Care 板块的产品图纸并列；而 Ch3 SLIDE 45 把 FPS 的批准权给 Quality。原文从未明说"勾选 Approve 且通过 Product Specifications 背书 = 获得 FPS 批准权"——【推断】 背书只是准入，具体能批 FPS 仍需 Senior Quality Engineer 角色。此链条的明文规则 [未找到原句]。

### 4-3｜与 Ch4（3D Viewer，SLIDE 47–66）：查看 3D 需要的最低权限

核心判断：3D 查看的技术链是「DRCS 下载原文件 → eDrawings 打开」，因此最低权限 = 对目标图纸系列持有 View；此外还需 SolidWorks 应用授权（受地域限制）与 eDrawings 客户端。

|||||
|---|---|---|---|
|第一步：客户端|从 KC Software Center / Company Portal 安装 eDrawings（找不到联系 The DESK）|eDrawings 不在 SLIDE 70 的 APPLICATIONS 列表中（该列仅 AutoCAD ×3 / Research Files / SolidWorks / PARTNERS PORTAL）|两套授权体系并行：软件分发（Software Center）与 DRCS 数据授权互不为前提；客户端安装无需 DRCS 权限|
|第二步：取文件|*"You will need to download the full SolidWorks file from DRCS"*；.sldasm = 3D 装配图，.sldprt = 3D 零件图|Download copy 是 DRCS 的文件级操作之一（Ch1 SLIDE 10），属 View 档；角色表 11/11 行均有 View|最低权限 = View（【推断】，因原文未把"下载"显式映射到 View/Work/Approve 三档）|
|第三步：软件授权|打开 .sldasm / .sldprt 需 eDrawings；创建/编辑需 SolidWorks|APPLICATIONS 中的 SolidWorks (K-C Internal - North & South America Only) —— 地域硬限制|在北美/南美之外即使是 View 也拿不到 SolidWorks 源文件（【推断】：源文件的产生依赖该应用授权）|
|能做什么（View 档内）|Components 逐级下钻、左键高亮、右键 Hide/Transparent/Isolate、Markup、Measure、Move、Explode、Section、Reset|全部为本地只读操作，不写回 DRCS|View 档即可完成 Ch4 全部功能 —— 这是"最低权限"的强证据|
|不能做什么|Ch4 未涉及编辑；Markup 标注为本地批注|修改图纸 = Work；放行 = Approve|3D 查看链路不产生任何写操作，故 View 足矣|
|典型文件|C153-FPS-01776-01.sldasm（4.42 MB，from cadkc.com）|该图号属 C153 系列 → 对应 Infant Care 板块图纸|示例文件落在 Personal Care - Infant Care 板块下（【推断】，因 C153-FPS-* 与 SLIDE 67 的 "diaper part" 及 Ch2 BOM_A 的 C153-* 一致）|


"查看 3D 的最低权限"判定式（合成）

|||||
|---|---|---|---|
|① DRCS Access Level ≠ None|是|SLIDE 70 三级；None ⇒ 无任何访问|原文|
|② 对目标 Drawing Series 持有 View|是（推断为最低）|Download copy（Ch1 SLIDE 10）是 3D 链路的必需动作（Ch4 SLIDE 50）；角色表 View 覆盖 11/11 行|原文（Download 在 View 档为 【推断】）|
|③ 目标 Sector 已被勾选（如 Personal Care - Infant Care）|是|SLIDE 70 Sector Access 列表；SLIDE 71 下钻 Infant Care|原文|
|④ Product Specifications 额外背书（若目标是 FPS 产品图纸）|是（仅 FPS 类）|SLIDE 70：FPS 属需额外背书区|原文|
|⑤ 本地已装 eDrawings|是|Ch4 SLIDE 48、50|原文（Ch4）|
|⑥ SolidWorks 应用授权（且位于北美/南美）|是（取源文件）|SLIDE 70：SolidWorks (K-C Internal - North & South America Only)|原文（地域限制）；与 View 的绑定关系 【推断】|
|⑦ 浏览器 = Microsoft Edge|是（申请/访问流程）|SLIDE 68|原文|
|⑧ 需要 Work 或 Approve|否|Ch4 全部功能均为本地只读，不写回 DRCS|【推断】；原文未明说|


## 模块5：业务连接点（Business Connections）



用户业务定位：卫材（纸尿裤 / 湿巾）创新研发 + 木浆与纸品战略采购。
以下三个连接点均遵循统一结构：涉及幻灯片 → 核心概念 → 关键数据 → 可执行行动建议。凡行动建议中标 【推断】 者，为基于 KC 证据的推演，非 KC 原文主张。

### 连接点 1：权限矩阵是研发组织设计的镜像——从 KC 的角色-权限表反推其研发协作模式（谁改、谁审、谁只看）

涉及幻灯片：SLIDE 67（审批权双向重构）、SLIDE 69（角色-权限表 11 行 + 三因子 + 经理须知 7 条）、SLIDE 70（三级 + 三权限 + 四范围）、SLIDE 73–74（申请与经理路由）；交叉 Ch3 SLIDE 44、45、46。

核心概念：Work Role × Business Sector × Reporting Work Location（三因子）；Permissions（View / Work / Approve）；Product Developer（FPM/FP1 批准）；Senior Quality Engineer（FPS 批准）；Research (Staff)（仅 View）。

关键数据

|||||
|---|---|---|
|角色-权限表行数|11|SLIDE 69|
|仅 View 的行数|6 / 11（Engineer-Regional、Engineer-North America、Research (Staff)、Maintenance、Process Engineer-Plant、Process Engineer-Regional）|SLIDE 69|
|View + Work 的行数|5 / 11|SLIDE 69|
|含 Approve 的行数|0 / 11|SLIDE 69|
|权限三档|3（View / Work / Approve）|SLIDE 70、73|
|访问等级三级|3（Standard / Projects Only / None）|SLIDE 70|
|权限判定因子|3（Work Role / Business Sector / Reporting Work Location）|SLIDE 69|
|FPS 批准人基数|1（Rex Stuart），备份 0|SLIDE 67；Ch3 SLIDE 44|
|图纸创建/修订工时经验值|8 hrs / drawing|Ch3 SLIDE 44|
|Checkers 名单自检状态|标题自标 *"Needs updating"*|Ch3 SLIDE 46|


反推出的 KC 研发协作模式（【推断】，逐条给出原文锚点）

|||||
|---|---|---|
|谁改？|落在 Engineer / Staff Engineer / Staff Global Engineer 序列（View+Work 共 5 行）；Product Developer 作为提交人（submitter）|SLIDE 69；Ch3 SLIDE 44|
|谁审？|分两层：FPM/FP1 由 Product Developer 自查自批（无独立 Checker）；FPS 由 submitter + fellow senior product developer 双人 Check|Ch3 SLIDE 44、45；SLIDE 67|
|谁批？|FPM/FP1 → Product Developer；FPS → Quality（当前为具名的 Rex Stuart）|SLIDE 67；Ch3 SLIDE 45|
|谁只看？|Research (Staff) 全局板块图纸仅 View；Maintenance、Process Engineer 亦仅 View|SLIDE 69|
|研发是不是执行角色？|不是——研发岗在权限体系中默认无 Work/Approve|SLIDE 69|
|权限怎么开？|不由角色自动发放，需本人申请 + 业务理由 + 经理审批 + CBT 前置|SLIDE 73、74；SLIDE 69|


⚠️ 最需要警惕的一条：Research (Staff) 在 Global / Sector Drawings 上仅 View。对本方（卫材研发）而言，这意味着——如果照抄 KC 的权限表，"研发"岗天然没有图纸修改与批准权，所有变更必须借道 Product Developer，链路被拉长。而 KC 自己的解法是把批准权下放给 Product Developer（SLIDE 67），即让执行者兼批准者。

可执行行动建议（本方可借鉴的权限设计框架）

||||||
|---|---|---|---|---|
|A1|不要把"研发"设成只读角色|在本方 PLM/图档系统的角色表里，把研发工程师归入"执行 + 批准"序列（对应 KC 的 Product Developer），而非"只读"序列（对应 KC 的 Research (Staff)）；若确需只读，单列"研究岗"角色并显式告知其权限边界|SLIDE 69（Research (Staff) → View）|【推断】|
|A2|按"风险半径"而非"组织层级"分配批准权|采用 KC 的分叉结构：零件/组件级（FPM/FP1）→ 提出者可自批；成品级（FPS，直接进产线）→ 质量职能批准。判定式：批准层级 = f(变更影响到的父级图纸数量)|SLIDE 67；Ch3 SLIDE 45|【推断】（KC 用 "control and speed" 明示其动机）|
|A3|把 Approve 从角色默认包里摘出来|参照 KC 的 0/11 设计：角色只发 View/Work，Approve 一律走单独申请 + 业务理由 + 上级审批的例外通道，并留痕|SLIDE 69（0/11）、SLIDE 73、74|【推断】|
|A4|批准点必须有备份，禁止单点|KC 的 FPS 批准人基数 = 1、备份 = 0（且 Checkers 名单自标 *Needs updating*）——这是反向教材。本方须为每个批准角色配置 Primary + Backup 双人，且备份需实际持有权限（不是只写名字）|SLIDE 67；Ch3 SLIDE 44、46|【推断】（反向借鉴）|
|A5|强制"业务理由"字段，而非只填工号|KC 的申请表单强制填 Your name, **project**, **why you are asking for the update**；经理侧还要求 business justification。本方权限申请表单建议照抄这三个必填项|SLIDE 74；SLIDE 69|【推断】|
|A6|设前置培训门禁（CBT 类比）|KC 要求申请人已通过 Business Approver CBT 才能获发超标准权限。本方可设"图纸规范/保密 线上考试通过"作为 Work/Approve 权限的前置条件|SLIDE 69（经理须知）|【推断】|
|A7|给战略采购单开只读通道|参照 KC 的 Research (Staff) → View：为木浆与纸品战略采购配置 View-only 角色，覆盖目标 Sector 的图纸系列。理由：图纸 BOM 里含基材用量与规格（如 Ch2 图像补充 p34 的 SURGE PICASSO EMBOSSING 74MM W × 197MM L、OUTER COVER 295MM W），View 即可支撑用量测算，无需 Work/Approve|SLIDE 69；Ch2 图像补充 p34|【推断】|


### 连接点 2：ECM（代工厂）的权限边界——外部合同制造商能看什么、不能看什么

涉及幻灯片：SLIDE 69（保密声明 + 三因子 + 经理须知）、SLIDE 70（Sector Access 含 *Personal Care - Vendor Drawings*；APPLICATIONS 含 PARTNERS PORTAL 与 *SolidWorks (K-C Internal…)*）、SLIDE 68（板块差异：Feminine Care 无 FPM/FP1/FP2）；跨文档旁证 Baby_Wipes_101 Ch4 SLIDE 31 与 Ch2 SLIDE 10。

核心概念：ECM / External Contract Manufacturer；Personal Care - Vendor Drawings；PARTNERS PORTAL；Additional endorsement；最小授权原则（*"Distribution must be limited, even with your manager, to your work role access requirements"*）。

关键数据

|||||
|---|---|---|---|
|Ch5 中 "ECM" / "External Contract Manufacturer" 原句|0 处|Ch5 全章检索|[未找到原句]|
|Sector Access 中与"外部方"直接相关的条目|1 条（*Personal Care - Vendor Drawings*），占 1/12|SLIDE 70|原文|
|APPLICATIONS 中未标注 Internal 的对外入口|1 个（*PARTNERS PORTAL*）；5 个未标注地域/内部限制的 AutoCAD ×3 / Research Files / PARTNERS PORTAL|SLIDE 70|原文|
|显式标注 K-C Internal 的应用|1 个（*SolidWorks (K-C Internal - North & South America Only)*）|SLIDE 70|原文|
|KC 具名代工厂数量（跨文档）|3 家：Merisco、Tufco（USA）、Nice Pack（U.K.）|Baby_Wipes_101 Ch2 SLIDE 10|非本章|
|KC 对 ECM 的战略表述（跨文档）|*"mitigating incremental costs from ECMs"；"Differentiated ECM partnership to drive consumer-preferred Wipe"*|Baby_Wipes_101 Ch4 SLIDE 31|非本章|
|保密条款强度|*"limited, even with your manager"*|SLIDE 69|原文，最强约束|
|超出标准的门槛条件|2 重：business justification + Business Approver CBT|SLIDE 69|原文|


可以直接读出的三条边界原则（【推断】，均锚定原文）

|||||
|---|---|---|---|
|B1|供应商图纸是一个被隔离的独立分区，不是从业务板块图纸里临时挑的|Sector Access 列表中 "Personal Care - Vendor Drawings" 与 Infant/Child/Adult/Feminine Care 平级并列（SLIDE 70）|KC 把"可给外部方的图纸"做成一个预定义的子集（【推断】），而非按需导出。这对本方是最有价值的一条——外发范围应先建库，再谈外发|
|B2|工程制图应用是内部资产，不随图纸外发|*"SolidWorks (K-C Internal - North & South America Only)"*（SLIDE 70）|源文件/编辑能力留在内部；外部方拿到的是图纸输出物，不是可编辑的工程源文件|
|B3|外发范围由"接收方的工作角色需要"决定，不由申请人的职级决定|*"Distribution must be limited, even with your manager, to your work role access requirements."*（SLIDE 69）|这条同时约束内部越权与外部外发：连直属经理都不构成扩权理由|


可执行行动建议（代工厂图纸外发范围建议）

||||||
|---|---|---|---|---|
|C1|建立"可外发图纸子集"（Vendor Drawings 库），与内部图纸库物理/逻辑隔离|在 PLM 中建一个 Vendor Drawings 分区，与 Infant Care / Adult Care 等板块平级（不是子目录）。只有进入该分区的图纸才可外发；进区需单独评审|SLIDE 70（Personal Care - Vendor Drawings 与板块平级）|【推断】|
|C2|外发三级白名单：可给 / 可给但需脱敏 / 不可给|建议分级（本方自定，KC 未给对应规则 [未找到原句]）：可给 = 外尺寸、装配关系、BOM 中的外购件规格；脱敏后给 = 涂布量/克重（可给范围、不给精确值或配方）；不可给 = FPS 成品图全图（KC 把 FPS 放 Additional endorsement 区）、胶设备标准（C079）、设计标准（C800）|SLIDE 70（FPS 与 Special Senses 均在 Additional endorsement required 区）|【推断】|
|C3|只外发"输出物"，不外发"源文件"|外发 PDF / 中性格式 / 图纸打印件；不外发 .sldasm / .sldprt / .slddrw / DWG 源档（若代工厂需用 3D，可外发 .sldasm 副本但不含 BOM 的父级关联）|SLIDE 70（SolidWorks 标注 *K-C Internal*）；Ch4 图像补充（.sldasm/.sldprt）|【推断】|
|C4|为代工厂开设独立通道，且通道内再做按人授权|参照 *PARTNERS PORTAL*：单独入口，不复用内部 DRCS 账号；每个代工厂账号绑定具体项目（对应 KC 的 Projects Only 语义）|SLIDE 70（PARTNERS PORTAL）；SLIDE 69（*ESHA Projects only*）|【推断】|
|C5|外发申请强制"业务理由 + 接收方角色"双字段|表单必填：接收方名称 / 项目 / 为什么需要 / 需要到哪一层（FPM/FP1/FPS）/ 有效期。审批人为业务负责人 + 保密负责人双签（KC 仅为经理单签，【推断】 本方宜加一级）|SLIDE 74（name/project/why）；SLIDE 69（business justification）|【推断】|
|C6|代工厂权限设有效期与项目绑定，项目结束自动回收|采用 Projects Only 语义：权限随项目清单发放，项目关闭触发回收。KC 未给出回收机制 [未找到原句]，此为补强项|SLIDE 70（Projects Only）；SLIDE 69（ESHA Projects only）|【推断】|
|C7|把"代工厂成本"与"代工厂权限"分开管理|KC 战略层把 ECM 当成本项（*"mitigating incremental costs from ECMs"*）与差异化伙伴（*"Differentiated ECM partnership"*）双轨看待；但权限层不给 ECM 任何特殊待遇（Ch5 全章无 ECM 权限行）。本方应同样做到：商务关系亲近 ≠ 权限放宽|Baby_Wipes_101 Ch4 SLIDE 31；Ch5 [未找到原句]|【推断】|
|C8|湿巾业务专项：因湿巾代工比例更高，优先把湿巾的 ECM 外发范围固化|湿巾代工厂（KC 侧具名 3 家）属于转换加工型外协，其必需图纸为"基材 + 折叠 + 包装"三层，通常不涉及 FPM 级的胶涂布细节 → 建议湿巾 ECM 默认只给 FP1/成品层，不给 FPM 层|Baby_Wipes_101 Ch2 SLIDE 10；SLIDE 70（FPS 需额外背书）|【推断】|


### 连接点 3：Special Senses（C079 胶设备标准 / C800 设计标准）——KC 有独立的胶设备标准体系

涉及幻灯片：SLIDE 70（Special Senses 区块：C079 | Adhesive Equipment and Standards、C800 | Personal Care Engineering Design Standards，均标 *Additional endorsement required*）；交叉 Ch1 SLIDE 17（FP1 = *Nonwoven + Adhesive）、Ch2 图像补充 p24-25（"CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT"*）、Ch2 图像补充 p34 与 BOM_A（胶以 CD/MD 尺寸写入 BOM 并拥有独立 FPM 图号）。

核心概念：Special Senses（横向标准，需额外背书）；C079 Adhesive Equipment and Standards；C800 Personal Care Engineering Design Standards；胶规格 = 图纸上的 CD/MD 涂布尺寸；胶有独立 FPM 图号 → 其变更走 Product Developer 批准。

关键数据

|||||
|---|---|---|
|Special Senses 条目数|2（C079、C800）|SLIDE 70|
|其中胶相关标准数|1（C079），占 50%|SLIDE 70|
|Sector Access 中以 "Adhesive" 命名的板块数|0 / 12|SLIDE 70|
|胶相关 FPM 图号（证据样本）|2 个：C153-FPM-00154-B-01（PAD TO LINER ADHESIVE）、C153-FPM-00155-B-01（EAR ADHESIVE）|Ch2 图像补充 BOM_A|
|胶涂布尺寸样例|125MM CD × 476MM MD（PAD TO LINER）、232MM CD × 279MM MD（LEG ELASTIC）、268 × 200 × 500MM MD（EAR REINFORCEMENT）、125MM CD × 367MM MD（p34 版本）|Ch2 图像补充 p34 / BOM_A|
|FP1 层的定义示例|*"Ex. – Nonwoven + Adhesive"* —— 胶与非织造布同为 FP1 层的构成要素|Ch1 SLIDE 17|
|C079 / C800 的适用范围原文|无|SLIDE 70 [未找到原句]|
|C079 / C800 的归口部门 / 版本 / 页数|无|[未找到原句]|


为什么这条对本方最重要（【推断】 的四层递进）

|||||
|---|---|---|
|① 存在性|KC 把"胶设备与标准"做成独立编号的横向标准（C079），与 Sector 平级、需额外背书|SLIDE 70|
|② 独立性|12 个 Sector 里没有一个以 Adhesive 命名 → 胶不是某个业务板块的附属文件，而是跨板块的公司级标准|SLIDE 70|
|③ 落地形态|胶在图纸上不是"材料名"，而是可测量的 CD/MD 涂布尺寸，且拥有独立 FPM 图号|Ch2 图像补充；Ch1 SLIDE 17|
|④ 治理含义|胶的 FPM 图纸变更后，批准权在新制下归 Product Developer（SLIDE 67）→ 胶规格变更不需要质量部签字即可生效（仅 FPS 层需要）|SLIDE 67；Ch3 SLIDE 45|




⚠️ 反向警示：第 ④ 层是双刃剑。KC 把胶（FPM 层）的批准权下放给 Product Developer，等于承认胶规格变更是"低风险半径"变更。但如果本方的胶供应商/胶设备未被标准化，这种下放会导致同一份图纸在不同产线上的实际涂布效果发散。→ 放权的前提是设备标准先行，这正是 C079 存在的理由。

可执行行动建议（胶黏剂 / 热熔胶设备选型）

||||||
|---|---|---|---|---|
|D1|建立本方的"C079 等价物"——《胶黏剂设备与施工标准》单列成册，不隶属于任何产品线|成册内容建议（本方自定，KC 未公开 C079 目录 [未找到原句]）：① 胶机/喷枪/喷嘴型谱与选型规则；② 开放时间、固化时间、施工温度窗口；③ 涂布精度与 CD/MD 尺寸公差带；④ 与图纸标注的映射关系（图纸写 125MM CD → 设备须能达到 ±X mm）；⑤ 不同基材（非织造布/木浆复合/薄膜）的胶型匹配表|SLIDE 70（C079 与 Sector 平级、需额外背书）|【推断】|
|D2|在图纸上以"尺寸"而非"材料牌号"定义胶|照抄 KC 的做法：BOM 行写成 XXX ADHESIVE 125MM CD × 476MM MD，而不是只写胶的品牌型号。好处：① 换胶供应商时图纸不必改版；② 采购可用尺寸反算用量|Ch2 图像补充 p34 / BOM_A|【推断】|
|D3|胶作为独立图元（FPM）建号，纳入 BOM 管理|给每一处胶分配独立 FPM 图号（KC 用 C153-FPM-00154 / 00155），纳入 BOM 与 Where Used；这样变更胶时可用 Where Used（Ch1 SLIDE 13）一次性列出受影响的全部父级图纸|Ch2 BOM_A；Ch1 SLIDE 13|【推断】|
|D4|设备选型前先定"涂布公差带"，而不是先选品牌|图纸上的胶尺寸是三位有效数字级（125 / 232 / 268 / 476 / 500 mm）。选型判定式：设备涂布精度 ≤ 图纸标注公差带的 1/3（行业通用 1/3 原则，KC 未给出该规则 [未找到原句]）。达不到精度的设备不得用于该产品|Ch2 图像补充 p34|【推断】|
|D5|把胶设备能力写进供应商准入条款|胶黏剂供应商投标时须提交：① 推荐施工温度/压力窗口；② 在本方指定设备上的实测涂布精度；③ 与本方基材的剥离强度数据。KC 的 Ch2 剖面图标题 *"CROSS SECTION SCHEMATIC & ADHESIVE LAYOUT"* 表明胶布置是图纸的正式组成 → 供应商数据是图纸输入|Ch2 图像补充 p24-25|【推断】|
|D6|把 C800 等价物（工程设计标准）作为跨产品线的共用基线|KC 把 *Personal Care Engineering Design Standards*（C800）做成跨 Infant/Child/Adult/Feminine Care 的横向标准。本方应为纸尿裤 + 湿巾建立统一的设计基线（圆角、压花、弹性体布置规则等），避免每条产品线各写一套|SLIDE 70（C800）|【推断】|
|D7|对 Special Senses 类的标准实行"独立背书、独立发放"|照抄 KC：标准类文件不随板块权限自动发放，需单独背书。标准的外发（尤其给代工厂/胶供应商）须走比图纸更严的通道——建议默认不外发|SLIDE 70（*Additional endorsement required*）|【推断】|
|D8|木浆与纸品采购对接：从 FP1 层反推基材-胶组合的用量结构|KC 的 FP1 定义示例是 *"Nonwoven + Adhesive"* → 基材与胶在 BOM 中成对出现。战略采购可用 FP1 层的 BOM 结构（含 SURGE PICASSO EMBOSSING 74MM W × 197MM L、OUTER COVER 295MM W、PAD NONDISCRETE 等）测算单位产品的基材面积与胶用量比，从而把木浆/非织造布采购量与胶采购量联动测算|Ch1 SLIDE 17；Ch2 图像补充 p34；SLIDE 69（View 权限可覆盖）|【推断】|


## 模块6：金句索引（Key Quotes Index）



每条含：英文原文 + SLIDE N + 中文翻译 + 「为什么记」。

||||||
|---|---|---|---|---|
|1|*"Creating Product Engineering drawings is K-C confidential information. Distribution must be limited, even with your manager, to your work role access requirements. Before selecting drawing access, Access is based on: Work Role, Business Sector, Reporting Work Location."*|69（图像补充 Step 2 声明）|「制作产品工程图纸属于 K-C 保密信息。分发必须被限制在工作角色的访问需求范围内——即便是给你的经理也不例外。 在选择图纸访问权限之前，访问权限基于：工作角色、业务板块、报告工作地点。」|本章最重的一句，也是全套材料的保密总纲。 两个信息点：① *"even with your manager"* —— 职级不构成越权理由，直接否定"领导打招呼就能看图"；② 三因子模型（Work Role × Business Sector × Reporting Work Location）是唯一可审计的权限判定式。|
|2|*"For the new SolidWorks product drawings product developers will be the approvers of diaper part 'FPM' and sub-assemblies 'FP1' within DRCS. This gives product developers more control and speed within the process."*|67|「对于新的 SolidWorks 产品图纸，产品开发人员将成为纸尿裤零件"FPM"与子组件"FP1"在 DRCS 内的批准人。这让产品开发在流程中获得更多的控制权与速度。」|权限下放的明文，且 KC 自己把动机写出来了——"control and speed"。这是"牺牲职责分离换速度"的自认。注意落点是 *diaper*（纸尿裤）——与卫材业务直接同构。|
|3|*"For final FPS drawings product developers will remain a checker. Rex Stuart of Quality remains the Approver for FPS drawings supporting production."*|67|「对于最终的 FPS 图纸，产品开发人员仍只是核对人。质量部的 Rex Stuart 仍是支持生产的 FPS 图纸的批准人。」|与 Q2 必须对读：同一页内，FPM/FP1 下放、FPS 上收。"remains" 一词同时暴露两件事：① 这是新旧制切换（过渡期）；② 批准权当前是个人制（Rex Stuart），目标是角色制（Senior Quality Engineer，见 Ch3 SLIDE 45）。|
|4|*"The drawing redline process is largely the same but the burden should lessen due to the ability to indicate cascaded parts and assemblies. Sara Schewe is in the loop and remains the Jacobs contact."*|67|「图纸红线（redline）流程大体不变，但由于能够标注级联的零件与组件，负担应当会减轻。Sara Schewe 在沟通环路中，仍是 Jacobs 的对接人。」|一句话点破 Ch3 变更管理复杂度的根源与解法：根源是"一张 FPS 是一棵图纸树，改一个 FPM 会向上传播"（Ch1 SLIDE 17/18/19）；解法是 redline 模板支持级联标注（Ch3 SLIDE 37/38 的模板行结构）。同时确认 Jacobs 是外包制图方。|
|5|*"These steps are the same for Adult, Child, and Infant Care. Feminine Care does not have the option for FPM,FP1,FP2 drawing access."*|68|「这些步骤对成人护理、儿童护理与婴儿护理是相同的。女性护理没有 FPM、FP1、FP2 图纸访问的选项。」|"权限矩阵是业务架构镜像"的最硬证据。 板块在权限体系里不平等——Feminine Care 根本不进入 FPM→FP1→FPS 三层 BOM 体系。对本方的警示：先冻结业务/产品架构，再设计权限模型，否则权限表会随产品线无限膨胀。|
|6|*"Research (Staff) | Global | Sector Drawings | View"*|69（图像补充角色-权限表）|「研发岗（Staff 级）｜全球｜板块图纸｜仅查看」|最短、但对本方杀伤力最大的一句。 它说明：在 KC 的权限体系里，"研发"默认不是执行角色——只能看、不能改、不能批。若本方照抄，研发的所有变更都要借道 Product Developer。角色归类（Work Role）是权限设计中极易踩坑的第一处。|
|7|*"Sector Designated Sector | Sector Location | Sector Drawings not including FPM, FP1, FPS, Special Access or Software | View, Work"*|69（图像补充角色-权限表）|「板块指定岗位｜板块所在地｜板块图纸（不包括 FPM、FP1、FPS、特殊访问或软件）｜查看、作业」|"默认不给"原则的原文。 即便拿到 View + Work，仍显式排除 5 类：FPM、FP1、FPS、Special Access、Software。→ 拿到板块权限 ≠ 拿到产品图纸权限。这是"分层授权"最干净的一处表述，可直接抄进本方权限设计。|
|8|*"ESHA Associates | Global Location | ESHA Projects only | View, Work"*|69（图像补充角色-权限表）|「ESHA 相关岗位｜全球所在地｜仅限 ESHA 项目｜查看、作业」|"Projects Only" 三级语义在原文中唯一的落点。 它证明 KC 的 Projects Only 档位是真实运行的机制，且用于按项目收敛范围——这正是本方给代工厂/外部伙伴授权时应采用的形态（项目绑定 + 项目结束即回收）。|
|9|*"Place check 'View', 'Work', & 'Approve' square boxes."*|73|「勾选"查看"、"作业"与"批准"的复选框。」|全章唯一一处把三个权限档并列的操作指令。 结合角色表 0/11 行含 Approve，可推出关键结论：Approve 是"例外路径"而非"角色属性"——必须主动勾选、单独举证、经理审批。这是本方权限框架中最该抄的一条设计。|
|10|*"DRCS may prompt you for additional information. Please fill out the boxes: Your name, project, why you are asking for the update, etc…. Then you should be able to hit 'Submit' and the request will be routed to your manager for approval."*|74|「DRCS 可能会提示你补充信息。请填写这些栏位：你的姓名、项目、你为什么申请这项变更等……然后你应该可以点击"提交"，申请将被路由给你的经理审批。」|权限治理的"理由留痕"设计。 三件事：① 业务理由是必填项（不是只填工号）；② 提交即路由经理，不存在自助开通；③ 与 SLIDE 69 的经理须知（business justification + Business Approver CBT）合起来构成完整的申请-举证-审批闭环。|
|11|*"Special Senses (Additional endorsement required)：C079 | Adhesive Equipment and Standards；C800 | Personal Care Engineering Design Standards"*|70（图像补充 Step 3 界面）|「专项标准（需额外背书）：C079 ｜ 胶设备与标准；C800 ｜ 个人护理工程设计标准」|对卫材/胶黏剂业务最有价值的一条。 三个信息点：① KC 有独立编号的胶设备标准（C079），且与 Sector 平级、需额外背书；② 12 个 Sector 里没有一个以 Adhesive 命名 → 胶是跨板块的公司级横向标准；③ 与 Ch1 SLIDE 17（*FP1 = Nonwoven + Adhesive*）和 Ch2 BOM 中的胶 CD/MD 尺寸连起来读：胶在 KC 是"有独立图号、以尺寸定义、有专门设备标准"的一等工程对象。|
|12|*"APPLICATIONS：AutoCAD-Canada / AutoCAD-Mexico / AutoCAD-United States / Research Files / SolidWorks (K-C Internal - North & South America Only)；PARTNERS PORTAL"*|70（图像补充 Step 3 界面）|「应用：AutoCAD（加拿大）/ AutoCAD（墨西哥）/ AutoCAD（美国）/ 研发文件 / SolidWorks（K-C 内部 — 仅限北美与南美）；伙伴门户」|外部分发的边界条款，写在应用授权层而非图纸层。 两点：① SolidWorks 被显式标注 K-C Internal 且限北美+南美 → 工程源文件的编辑能力是内部资产，并受地域限制；② PARTNERS PORTAL 是列表中唯一未标注 Internal 的对外入口，与 Personal Care - Vendor Drawings 一起构成 KC 面向外部方（含代工厂）的两条受控通道。|


## 附录：本章证据覆盖率自检

|||
|---|---|
|覆盖幻灯片|67–80，共 14 页|
|有实质内容的页|9 页（SLIDE 67, 68, 69, 70, 71, 72, 73, 74, 75）|
|空白模板页（正文仅 TITLE/TEXT）|4 页（SLIDE 76, 77, 78, 79）|
|纯图片无文本层页|1 页（SLIDE 80）|
|模块1 论点数|5 条（要求 3–5） ✔|
|模块2 概念数|12 个（要求 8–12） ✔；已覆盖 DRCS Access 三级 / Roles（Research (Staff)、Product Developer、Senior Quality Engineer、ECM）/ Permissions（View·Work·Approve）/ Sector（含 Infant Care、Adult Care、Family Care、K-C Professional）/ Special Senses（C079、C800）/ Access Request 流程 / Cross Sector Access|
|模块3 表格数|5 个（T1 角色×权限、T2 三级定义、T3 Sector 全表、T4 Special Senses、T5 申请流程），≥ 4 ✔|
|模块4 衔接|3 组对比表（Ch1 SPOT vs DRCS、Ch3 Approve、Ch4 3D 最低权限） ✔|
|模块5 业务连接点|3 个（权限矩阵＝组织镜像 / ECM 权限边界 / Special Senses 胶设备标准），每个含幻灯片 + 概念 + 数据 + 行动建议 ✔|
|模块6 金句数|12 条（要求 8–12） ✔，均附中文翻译与「为什么记」|
|标注 [未找到原句] 的主要项|ECM（Ch5 内）、三级的定义文字、经理须知未摘录的 2 条、C079/C800 的适用范围与归口、权限有效期/复检/回收机制、Additional endorsement 的具体流程、Additional endorsement 与 FPS 批准权的因果关系、SPOT 是否需要 DRCS 权限|
|标注 【推断】 的主要项|Projects Only 语义、Standard = 默认角色映射、Download 属 View 档、3D 查看最低权限 = View、PARTNERS PORTAL 为外部通道、C079/C800 为跨板块横向标准、全部"可执行行动建议"|


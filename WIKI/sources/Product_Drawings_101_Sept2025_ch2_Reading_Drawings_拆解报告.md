---
type: source
title: "Product_Drawings_101_Sept2025_ch2_Reading_Drawings_拆解报告.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch2_Reading_Drawings_拆解报告.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# Product_Drawings_101_Sept2025_ch2_Reading_Drawings_拆解报告.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch2_Reading_Drawings_拆解报告.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

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
- (d) 原文英文摘录："Shows the product laid out flat with a top-down view of the body-facing side of the product." / "This view holds dimensions the operators will be checking most frequently.

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch2_Reading_Drawings_拆解报告.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Training/Pants/Product Drawings 101 (KC Sept2025)/Product_Drawings_101_Sept2025_ch2_Reading_Drawings_拆解报告.md.md`

## 关联页面

- [[Kimberly-Clark（金佰利）]]

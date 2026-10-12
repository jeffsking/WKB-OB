---
type: source
title: "COCO_V6_第三轮trial_两组对照分析报告_20261006.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/COCO_V6_第三轮trial_两组对照分析报告_20261006.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
key_claims: []
pages_linked: []
compile_mode: extractive
---

# COCO_V6_第三轮trial_两组对照分析报告_20261006.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/COCO_V6_第三轮trial_两组对照分析报告_20261006.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# CI-06 COCO V6 第三轮 trial —— 两组对照比较分析

分析时点：2026年09月24日 22:01（首次，依据 9.24 版数据）；本轮更新：2026年10月06日 22:55（依据 9.30 版数据，GMT+8）
数据源（本轮更新依据）：本地《CI-06 COCO V6 3rd round trial-9.30.xlsx》（文件时间戳 2026-09-30，共 9 张 sheet）—— 本轮全部数值与结论均以此为准；数据覆盖的测试时间范围：芯体成品 2026-09-22 ~ 2026-09-30；原材料主体 2026-09-21 + 2026-09-30 前补测项（详见第六节 6.0）
数据源（上一轮基线）：IMA WKB《CI-06 COCO V6 3rd round trial.xlsx》（文件最后更新 2026-09-24 21:43）；REL 专项另加 IMA WKB《REL benchmark.png》
基准源：IMA WKB《SAP database for COCO.xlsx》、《满足要求的四大组件性能指标与测试方法》；本地《全芯体材料清单与实验计划_v3.xlsx》（2026-07-27）；IMA WKB《CO V6 新体机芯体验证实验方案评审》；REL 专项另加：IMA WKB《NEW REL 4.pptx》（KC REL Qualification Test Matrix）












更新记录（2026-09-24 22:56）：新增 第四节「第三组（REL 专项补充）」，基于《REL benchmark.png》的 REL 样品横向对比；同时新增第 1.3 节口径项 C7（材料级 vs 组装级口径错配）并据此修正第 3.2(a) 节与 3.4 节结论 1 中「达优秀档」的表述。

更新记录（2026-09-24 23:15）：将《REL benchmark.png》的 REL 数据接入第二组主表 —— Excel Sheet2「原材料vs基准」新增「REL 增强层 · 第二数据源」段（本方法指标 vs 常规方案基线均值，附 4 组基线各组原始值），并修正该表表头列名与数据列错位一格的问题；据用户确认「两套 REL 为不同试样」更新第 1.2 节覆盖范围表、Q9 与本节对照覆盖说明。第二组主表现在同时包含两套 REL 数据（并列、不合并）。

更新记录（2026-09-24 23:35）：按用户指令，将 28.8 gsm（Code A） 与 33.48 gsm（Code B） 作为两个独立 Code 并列纳入第三组 REL 横向比对 —— 样品数由 5 组扩为 6 组。同步更新：第四节的实验设置、基线/本文方法定义、对比表（改双 Code 并列 + 6 组位次）、差异分析与结论（新增 A↔B 直接配对）；5.1 汇总表与 5.2 缺口清单相应扩充；Excel Sheet2「REL 增强层 · 第二数据源」段改为双 Code 并列表 + A↔B 配对段，Sheet5–7 全部重算。第三组完整分析见独立报告 《REL增强层专项对比分析_6样品benchmark_20260924.md》。本轮同时记录 3 项新口径分歧：Code B 强度单位未标注、厚度测压口径不一致、两 Code 设计配方逐组分同构。

更新记录（2026-10-06 22:55）★ 本轮：依据 《CI-06 COCO V6 3rd round trial-9.30.xlsx》（2026-09-30 版） 更新全文数值、结论与图表。报告结构与分析框架保持不变。本轮变更概览（详见第六节）：
- 数据源版本更迭：9.30 版与 9.24 版逐格比对，差异集中在 2 张 sheet —— Lab data form（芯体成品测试，新增 351 格 / 变更 54 格）、Material Test（原材料测试，新增 9 格 / 变更 12 格）；其余 6 张 sheet（Product Test / Code list on site / Target Weight / Material List / Check before collecting / Lab tester）逐格零差异，相关结论不受影响；另删除空的 Sheet1。
- 芯体侧新增 5 个 Code：Code 8 / 9 / 10 / 11 / 12 首次录入成品测试数据（收样 9/24–9/28，手工样制作与测试 9/28–9/30）。芯体有数据的 Code 由 7 个增至 12 个（新增第一节配对 F–J）。
- 修正上一轮的一处数据缺失判定：Code 7 的 L-H 全项按原始样本重算恢复（源文件均值行为 #DIV/0!，但 4 个原始样本数据完整）→ 配对 E 由「无法评价」升级为可评价。
- 原材料侧 5 项更新：LSN-1 爬坡高度 170.6 → 137.2 mm（−19.6%）；LSN-2 新增液体穿透时间 2.83 s；SAP-1 NR950 的 AUL(0.7psi) 28.955 → 26.055；SAP-3 High GBP 与 SAP-5 610+950 的 AUL(0.7psi) 新增 29.985 / 19.31。
- 第三组（REL 专项）数据未变：9.30 版的 REL Minrui 段（Code B，n=5）与 4 组基线数据逐格一致 → 该节结论与图表沿用，仅补充版本核对说明。
- 新增 4 项口径与数据质量问题（Q13–Q16，见 1.3 节）：源文件均值行与原始样本不一致共 5 处；Code 9 的唯一变更变量在源文件中标注为占位文本「Code x」；同一工作簿内两处对 Code 8–10 的定义冲突；Code 11 的 L-H 仅 n=2。

更新记录（2026-10-07 09:45）★ 图表补充 + 工作簿并入：① 在 2.12 节追加 横向条形对比图（COCO_V6_全Code关键参数横向条形对比_vsControl2_20261007.png）——与热力图同源（同一 matrix_ctrl2.json），但改为「每参数一图 + 面板内按优势度降序」，便于读出每个参数的赢家排序（与热力图的「单 Code 整体画像」互补）。② 把该矩阵并入数据工作簿为 Sheet「7-全Code总览vsControl2」，含 7.1 优势幅度矩阵 / 7.2 逐 Code 优势结构汇总 / 7.3 逐指标明细长表（可追溯实测值）/ 7.4 口径声明 K1–K10。③ 因新增 Sheet 7，原「7-REL口径与缺口」顺延为「8-REL口径与缺口」（内部小节 7.x → 8.x，正文与脚本引用已同步）；工作簿现为 9 张 sheet，末位仍恒为口径与缺口。新增脚本 build_chart_allcode_bar.py、build_sheet_allcode_vs_ctrl2.py；工作簿重建顺序现为三步：build_report_coco_v6_r3.py → build_rel_benchmark.py → build_sheet_allcode_vs_ctrl2.py（顺序不可颠倒）。

## 一、分析口径与数据覆盖范围（阅读任何结论前请先看本节）

### 1.1 三组比较的定义

|||||
|---|---|---|---|
|第一组|本 trial 各 Code 芯体 + 各原材料实测|Control（本 trial 内部对照组）|同批次、同工艺、单变量；反映"改这一项到底有没有用"|
|第二组|本 trial 各原材料 / 芯体实测|常规材料 benchmark（KC 资质矩阵 + 常规材料对照值 + SAP 常规库值）|外部规范/历史值；反映"材料本身够不够格"|
|第三组（2026-09-24 补充）|REL 增强层 5 组样品实测|外部/候选 REL 方案（4 组基线）|横向 benchmark；反映"本方法相对同类方案处于什么位置"|






关键界定：第一组回答"相对本项目对照组是好是坏"；第二组回答"相对常规商用材料水平是好是坏"；第三组回答"相对同期的其他 REL 方案是好是坏"。三者结论可能相反（例：某材料相对 Control 变差，但仍优于常规基准），本报告对每一组分别给出结论，不做合并。

### 1.2 数据覆盖范围总表

① 芯体测试——截至本轮（9.30 版）12 个 Code 完成，5 个 Code 仍无数据

|||||||
|---|---|---|---|---|---|
|有数据|Code 1|亲水胶（芯片胶）3.5*4|国标重量/1st·2nd吸收时间/回渗/渗漏、Cradle（重量+1·2·3次摄入+扩散长度）、L-H（重量+L/H摄入·回渗·残留+扩散长度）|国标 n=5；Cradle n=4；L-H n=4|收样 9/21，测试 9/22|
|有数据|Code 2|亲水胶 2*4|同上|国标 n=5；Cradle n=4；L-H n=4|收样 9/21，测试 9/22|
|有数据|Control-1|Control胶 2*4|同上|国标 n=5；Cradle n=4；L-H n=4|收样 9/22，测试 9/23|
|有数据|Control-2|Control胶 3.5*4|同上|国标 n=5；Cradle n=4；L-H n=4|收样 9/22，测试 9/23|
|有数据|Code 5|PSS = 100% NR610|同上|国标 n=5；Cradle n=4；L-H n=4|收样 9/22，测试 9/23|
|有数据|Code 6|PSS = 100% NR950|同上|国标 n=5；Cradle n=4；L-H n=4|收样 9/23，测试 9/24|
|有数据 ★本轮恢复 L-H|Code 7|PSS = 50% NR610 + 50% NR511|国标、Cradle 全项；L-H 全项（本轮按原始样本重算恢复）|国标 n=5；Cradle n=4；L-H n=4|收样 9/23，测试 9/24|
|有数据 ★本轮新增|Code 8|PSS = 50% NR610 + 50% NR950（SAP 混配）|国标、Cradle、L-H 全项|国标 n=5；Cradle n=4；L-H n=4|收样 9/24，加工与测试 9/28|
|有数据 ★本轮新增|Code 9|LSS SAP = 源文件标注「Code x」（占位，型号未明确）；PSS 同 Control|国标、Cradle、L-H 全项|国标 n=5；Cradle n=4；L-H n=4|收样 9/24，加工与测试 9/28|
|有数据 ★本轮新增|Code 10|LSS SAP = NR950；PSS 同 Control|国标、Cradle、L-H 全项|国标 n=5；Cradle n=4；L-H n=4|收样 9/28，加工与测试 9/29–9/30|
|有数据 ★本轮新增|Code 11|LSN = Unikorn MPM 20gsm 200mm（降克重）|国标、Cradle 全项；L-H 仅 n=2|国标 n=5；Cradle n=4；L-H n=2|收样 9/28，加工与测试 9/29–9/30|
|有数据 ★本轮新增|Code 12|LSN = 王金 38gsm（含三叶草粘胶纤维）|国标、Cradle 全项；L-H 本批未做|国标 n=5；Cradle n=4|收样 9/28，加工与测试 9/30|
|无数据|Code 3|Liner = 延江 Code 1（50gsm 三叶形）|—|—|未收样|
|无数据|Code 4|Liner = 川越 Code 2（30gsm）|—|—|材料未到货|
|无数据|Code 13|PSN = Unikorn 20gsm 155mm|—|—|已收样 9/28，手工样制作中，结果未回填|
|无数据|Code 14|REL = Minrui（≈28gsm）|—|—|已收样 9/28，手工样制作中，结果未回填|
|无数据|Code 15–16|110mm pad 适配版|—|—|已收样 9/29，手工样制作中，结果未回填|
|无数据|Code 17|标准配置|—|—|已收样 9/30，结果未回填|









★本轮变化：上一轮（9.24 版）芯体仅 7 个 Code 有数据（Code 1/2/5/6/7 + Control-1/2）；9.30 版新增 Code 8–12 共 5 个，有数据的 Code 增至 12 个。收样与测试节奏见源文件 Daily Plan：Code 8/9 于 9/24 收样；Code 10/11/12 于 9/28 收样；Code 13–17 分别于 9/28–9/30 收样但手工样尚未出结果。

★变量定义口径提示：Code 8–12 的变量定义来自源文件 Product Test sheet（"CI-06 COCO V6 3rd round trial" 专表）。同一工作簿的 Code list on site sheet（标题为 "2nd round Trial Plan"）对 Code 8/9 给出的是通道结构类定义（Code 8 = 前端加横向通道；Code 9 = T5.6 Insert 145mm），与 Product Test 的 SAP 类定义冲突。两份定义在 1.3 节 Q15 中显式并列，本报告正文采用 Product Test（3rd round 专表）口径，建议向项目组确认编码表版本。

② 原材料测试——全部为候选材料，Control 材料未同步实测

||||||
|---|---|---|---|---|
|Liner-1|延江 50gsm（三叶形 3D Bico）|基重/厚度/MD·CD强度·伸长/穿透/返渗/层压强度/pH/Run off|n=5|9/21|
|Liner-2|川越 30gsm|未到货，全部空缺|0|—|
|REL · Code B|REL Minrui 33.48gsm（设计 28gsm；CI-06 Code 14）|基重/厚度/MD·CD拉伸·伸长/穿透/返渗/pH|n=5|9/21|
|REL · Code A|新开发 REL（闽瑞五组分）28.8gsm|克重/厚度/MD·CD 强度与伸长/孔隙率/穿透/We

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/COCO_V6_第三轮trial_两组对照分析报告_20261006.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/COCO_V6_第三轮trial_两组对照分析报告_20261006.md.md`
---
type: source
title: "COCO_V6_第三轮trial_两组对照分析_20261010.xlsx"
source_type: 报价单
source_path: RAW/ima_sync/个人知识库/WKB/Projects/COCO/COCO_V6_第三轮trial_两组对照分析_20261010.xlsx.md
original_link: ""
date_published: 2026-10-12
date_processed: 2026-10-12
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# COCO_V6_第三轮trial_两组对照分析_20261010.xlsx

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 报价单`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Projects/COCO/COCO_V6_第三轮trial_两组对照分析_20261010.xlsx.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# COCO_V6_第三轮trial_两组对照分析_20261010.xlsx

[0-说明与数据覆盖范围]
|CI-06 COCO V6 第三轮 trial —— 两组对照比较分析|||
|---|---|---|
||||
|数据源（本轮）|本地《CI-06 COCO V6 3rd round trial-10.10.xlsx》（2026-10-10 版）——本轮更新的唯一数据依据（芯体测试 2026-09-22 ~ 09-30）||
|数据源（上轮）|本地《CI-06 COCO V6 3rd round trial-9.30.xlsx》（2026-09-30 版）——上一轮分析所用基线||
|基准源|IMA WKB《SAP database for COCO.xlsx》；IMA WKB《满足要求的四大组件性能指标与测试方法》；本地《全芯体材料清单与实验计划_v3.xlsx》||
|分析时点|2026年09月24日 22:01（首次）→ 2026年10月06日 22:45（9.30 数据更新）→ 2026年10月10日 23:05（10.10 数据更新）→ 2026年10月11日 07:40（★噪声底撤回修订）||
|组1定义|本 trial 内部对照：各 Code 芯体 / 各原材料 vs Control（同批次、同工艺、单变量）||
|组2定义|外部基准对照：本 trial 实测 vs 常规材料 benchmark（KC 资质矩阵 / 常规定向材料对照值 / SAP 常规库值 / 供应商规格）||
|本轮新增|① 芯体侧新增 5 个 Code 的实测数据（Code 13/14/15/16/17，收样 9/29–9/30）；② Code 11 的 L-H 由 n=2 补齐至 n=4、Code 12 的 L-H 由「未做」补齐至 n=4；③ 新增测试项 Pad Integrity（仅 Code 1/2 与 Control-1/2 有数据）；④ 其余 8 张 sheet 逐格比对完全一致，原材料侧无任何变化。||
|★重大修订|2026-10-11：撤回噪声底体系。上一版将 Code 13/15 误判为「Control 全同配方复现样」并据此建立逐指标噪声底。经用户指正 + 源文件回查：Code 13 的 PSN 为 Unikorn 155mm（Product Test U13）；Code 15 存在 pad 宽幅 110mm + pattern + 胶宽 125mm + 换料四项变更（Product Test W21 Remark）。→ 本批无有效复现样，噪声底不可建立，全部结论回退至纯幅度判定标尺。||
|数据覆盖范围明细|① 截止本轮，17 个 Code 中 15 个完成芯体测试（Code 1/2/5/6/7/8/9/10/11/12/13/14/15/16/17 + Control-1/2），仅 Code 3/4 无数据；② 原材料侧未同步实测 Control 材料，故组1原材料部分为「规格+基准」对比，非同步实测对比；③ ★本批无全同配方复现样 → 无法建立过程噪声底，所有差异均无法区分材料效应与批次效应；④ Pad Integrity 仅 4 个 Code 有数据且源文件未标注单位；⑤ Code 15 为多变量试验，其差异不可归因任一单变量。||
|分类|对象|覆盖情况|
|芯体（有实测数据）|Code 1|胶变量（亲水胶3.5*4）：国标n=5、Cradle n=4、L-H n=4；收样9/21，测试9/22|
|芯体（有实测数据）|Code 2|胶变量（亲水胶2*4）：国标n=5、Cradle n=4、L-H n=4；收样9/21，测试9/22|
|芯体（有实测数据）|Control-1|对照组（Control胶2*4）：国标n=5、Cradle n=4、L-H n=4；收样9/22，测试9/23|
|芯体（有实测数据）|Control-2|对照组（Control胶3.5*4）：国标n=5、Cradle n=4、L-H n=4；收样9/22，测试9/23|
|芯体（有实测数据）|Code 5|PSS=100%NR610：国标n=5、Cradle n=4、L-H n=4；收样9/22，测试9/23|
|芯体（有实测数据）|Code 6|PSS=100%NR950：国标n=5、Cradle n=4、L-H n=4；收样9/23，测试9/24|
|芯体（有实测数据）|Code 7|PSS=50%610+50%511：国标n=5、Cradle n=4、L-H n=4（★9.30 版按原始样本重算恢复，源文件均值行为 #DIV/0!）；收样9/23，测试9/24|
|芯体（有实测数据）|Code 8|PSS=50%NR610+50%NR950（SAP混配）：国标n=5、Cradle n=4、L-H n=4；收样9/24，测试9/28 ★9.30 版新增|
|芯体（有实测数据）|Code 9|LSS SAP=源文件标注「Code x」（占位未明确）：国标n=5、Cradle n=4、L-H n=4；收样9/24，测试9/28 ★9.30 版新增|
|芯体（有实测数据）|Code 10|LSS SAP=NR950：国标n=5、Cradle n=4、L-H n=4；收样9/28，测试9/29–9/30 ★9.30 版新增|
|芯体（有实测数据）|Code 11|LSN=Unikorn MPM 20gsm 200mm（降克重）：国标n=5、Cradle n=4、★10.10 版 L-H 由 n=2 补齐至 n=4；收样9/28，测试9/29–9/30|
|芯体（有实测数据）|Code 12|LSN=王金38gsm(含三叶草粘胶纤维)+PSN改Unikorn 155mm：国标n=5、Cradle n=4、★10.10 版 L-H 由「未做」补齐至 n=4；收样9/28，测试9/30|
|芯体（有实测数据）|Code 13|★10.10 版新增：Control 全同配方复现（基线复现，用于评估过程变异性）；国标n=5、Cradle n=4、L-H n=4；收样9/29|
|芯体（有实测数据）|Code 14|★10.10 版新增：REL=Minrui REL（vs Control-40g）；国标n=5、Cradle n=4、L-H n=4；收样9/29|
|芯体（有实测数据）|Code 15|★10.10 版新增：Control 全同配方复现（基线复现，用于评估过程变异性）；国标n=5、Cradle n=4、L-H n=4；收样9/29|
|芯体（有实测数据）|Code 16|★10.10 版新增：胶宽 137.5→125mm（缩窄）；国标n=5、Cradle n=4、L-H n=4；收样9/29|
|芯体（有实测数据）|Code 17|★10.10 版新增：胶宽 137.5→125mm，与 Code 16 同配方（Remark: -16,17 在一个成型鼓）；国标n=5、Cradle n=4、L-H n=4；收样9/30|
|芯体（无数据）|Code 3|Liner=延江Code1 50gsm(三叶形)：未收样/未测|
|芯体（无数据）|Code 4|Liner=川越Code2 30gsm：材料未到货，未测|
|原材料（n=5）|Liner-1 延江50gsm|全指标 5 样本；9/21 完成|
|原材料（n=5）|REL Minrui|全指标 5 样本；9/21 完成|
|原材料（n=5）|LSN-1 王金(三叶草)|全指标 5 样本；9/21 完成|
|原材料（n=5）|SAP-1~SAP-5|各 5 样本（部分指标仅2样本）；9/21 完成|
|原材料（n=5）|亲水胶|5 样本；9/21 完成|
|原材料（数据不全）|Liner-2 川越30gsm|未到货，全项空缺|
|原材料（数据不全）|LSN-2 Unikorn|9.30 版已补全力学/穿透/返渗/爬坡（n=5）|
|原材料（数据不全）|PSN Unikorn|仅含水率+爬坡（n=5）|
|标记为 ○ 但未填数（截至 9/30）|Mannequins Side/Prone/Supine|仅 Control-2 与 Code 16/17 标记待测，结果为空|
|标记为 ○ 但未填数（截至 9/30）|surface moisture / Run off|Code 1、Code 2、Control-1、Control-2 已执行，源文件结果列仍为空|
|标记为 ○ 但未填数（截至 9/30）|SAM Density|仅 Control-2（9/23）与 Code 16 标记，结果为空|
|标记为 ○ 但未填数（截至 9/30）|FIFE intake / leakage / Rewet|全 code 列已建，V–AB 列结果仍为空|
|REL 增强层（第二数据源 · 双 Code 并列）|6 组样品同表横向对比：Code A = 新开发 REL 28.8gsm；Code B = REL Minrui 33.48gsm（CI-06 实测 n=5）；对照系 = 4 组常规 REL 方案（YJ DL24C / DY ND055 / ZB 箱式 / 芥东 箱式）|克重 / 厚度 / MD·CD 强度与伸长 / 堆密度 / 孔隙率 / VV 无压估算 / 归一化强度 / CD-MD 比 / 穿透时间 / Wet-back / Hold 住 SAM% / 3D 成像 / 截面。Code A 与 4 基线源《REL benchmark.png》（n 与测试日期未标注，按单批次观察处理）；Code B 源《CI-06》Material Test（n=5；缺 Hold 住 SAM% 与 3D 成像）。A↔B 直接配对、逐 Code 对基线的位次排名见 Excel Sheet5 与《REL增强层专项对比分析》报告|
|本轮更新依据与关键变化（2026-10-10 · 9.30 → 10.10）|||
|变化类型|对象|上一轮（9.30 版）→ 本轮（10.10 版）的变化与依据|
|芯体·新增数据|Code 13（PSN = Unikorn 155 mm）|无数据 → 国标 n=5 / Cradle n=4 / L-H n=4。收样 9/29。★变量（源文件 Product Test U13 = UNIKORN -155mm）：PSN 由 Control-26g 改为 Unikorn 20gsm PP+fluff 155mm 宽（Material List 第 11 项）；LSS/PSS SAP、LSN、REL、胶种、胶宽 137.5mm、成型条件均同 Control-2 → **单变量试验**|
|芯体·新增数据|Code 14（REL = Minrui）|无数据 → 国标 n=5 / Cradle n=4 / L-H n=4。收样 9/29。变量：REL 由 Control-40g 改为 Minrui；LSS/PSS 仍为 Control NR511|
|芯体·新增数据|Code 15（★多变量，仅记录不判定）|无数据 → 国标 n=5 / Cradle n=4 / L-H n=4。收样 9/29。★源文件 Product Test W4（Code Design）为 #VALUE! 定义失效；W21 Remark 明列四项变更：「-16,17 在一个成型鼓 / -PSN,REL需要换成适合110mm Pad / -胶宽需要减窄 / -需要两卷」→ pad 宽幅 110mm 配套换料 + pattern 改动 + 胶宽 125mm + 成型鼓变化，**不可归因任一单变量**|
|芯体·新增数据|Code 16（胶宽 137.5 → 125 mm）|无数据 → 国标 n=5 / Cradle n=4 / L-H n=4。收样 9/29。唯一变量：ADH width 缩窄 9.1%|
|芯体·新增数据|Code 17（胶宽 137.5 → 125 mm）|无数据 → 国标 n=5 / Cradle n=4 / L-H n=4。收样 9/30。与 Code 16 同配方（源文件 Remark：-16,17 在一个成型鼓）|
|芯体·补齐数据|Code 11 的 L-H（n=2 → n=4）|新增样本 3、4 共 8 项。上一轮因样本不足仅作方向参考，本轮可支撑完整配对评价|
|芯体·补齐数据|Code 12 的 L-H（未做 → n=4）|新增 4 个样本共 8 项。上一轮因完全缺失而无法评价，本轮已补齐；参与项数由 8 项增至 15 项，净优势分自此可与全项者直比|
|新增测试项|Pad Integrity|源文件新增第 29 列。仅 Code 1/Code 2/Control-1/Control-2 有数据（n=5）。单位未标注；Control-2 与 Code 1 为 5/5 达上限 300，Control-1 仅 1/5，Code 2 为 0/5|
|★★方法论撤回|逐指标过程噪声底（2026-10-11 全量撤回）|上一版以 Code 13/15 为「Control 全同配方复现样」建立噪声底并据此判定归因（169 项中 37 项超阈）。**该前提不成立**：Code 13 = PSN 换成 Unikorn 155mm；Code 15 = pad 宽幅 110mm + pattern + 胶宽 125mm + 换料（Tar.Weight 22.120 ≠ Control 的 22.817 亦为旁证）。→ 本批 15 个 Code 中**不存在任何全同配方复现样**，噪声底不可建立，结论强度回退至纯幅度判定标尺；所有差异均无法区分材料效应与批次效应|
|未变化|既有 Code 1–12 的全部原始样本|逐样本交叉验证（对 9.30 与 10.10 两版用同一脚本独立提取后逐格比对）：国标 / Cradle / L-H 原始样本零变化 → 上一轮全部数值与结论沿用|
|未变化|原材料侧全部数值|`Material Test ` 等 8 张 sheet 逐格零差异 → 第二组（vs benchmark）与第三组（REL 专项）全部结论沿用，无需重算|
|源文件修复|`Lab data form` 汇总行|167 格由 #DIV/0!

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Projects/COCO/COCO_V6_第三轮trial_两组对照分析_20261010.xlsx.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Projects/COCO/COCO_V6_第三轮trial_两组对照分析_20261010.xlsx.md`

## 关联页面

- [[FIFE Test（FIFE 摄入-回渗评价）]]　[[REL Splice Tensile Test（REL 拼接拉断力测试）]]　[[REL增强层]]　[[SAM Testing Methods（超级吸水材料测试方法）]]　[[SAP（高吸水树脂）]]　[[Unikorn]]　[[延江（Yanjan）]]

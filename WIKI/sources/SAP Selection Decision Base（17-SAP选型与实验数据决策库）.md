---
type: source
title: "SAP Selection Decision Base（17-SAP选型与实验数据决策库）"
source_type: 报价单
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/17-SAP选型与实验数据决策库.docx.md
original_link: ""
date_published: 2026-08-01
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "Test protocol decides the winner 测试协议决定胜负：高载短间隔（3.5 kg, 80 ml×3）为渗透 GBP 受限，全 511 最快；低载多次（1.2–2.0 kg, 60 ml×4，企标）为容量 CRC 受限，多 SAP 混底层全面反超（中文：所谓『全 511 最优』是高压短间隔协议的假象）"
  - "Enterprise rewet @34 min 主 KPI：930/住友 4.325 g < 511/951+959 5.582 g < 全511 5/5 8.363 g < 全511 3/7 11.270 g；门槛 < 5.9 g（= 全511 对照的 70%）"
  - "Three-role SAP architecture 三层角色分工：SAP1 皮侧快吸下单层 / SAP2 快膨 / SAP3 延迟储库；设计杠杆是溶胀快慢比 ratio 而非位置"
  - "Top/bottom split is the first dominant axis 顶/底比率第一主导轴：3/7 vs 5/5 → 扩散 +0.354、后期吸收 +0.101、留存 −0.351（回渗约 2.6×），速度↔留存为明确 trade-off"
  - "Zoned dosing beats uniform distribution 分区加料完胜均布：Design C（511/950）峰值饱和度 67%，Design B 纯 511 均布 Crotch 溢出 129% → 拒收"
  - "Confounding audit 混淆地图：8 单元中仅列 1/3/6/7/8 为 CLEAN 对比，列 4（511/951+N8）FULLY CONFOUNDED、列 5（930/住友）为结构离群点，N8 效应不可归因"
  - "Cost levers 成本杠杆：总 SAP 13.5 g/片、US¢1.90/片，较单 SAP 高端基线 −40% SAP 成本；LK804ND $1600/MT、KC-511 $1300/MT、NR-950 $1350/MT，国产源替换是首要杠杆"
  - "Caliber warning 口径警示：同一表内『吸水倍率 54–63』为去离子水自由溶胀，非 EDANA 盐水 CRC；后者为『离心保水率 30–37』，引用必须区分（AUL 为 Nuoer 0.7 psi 口径）"
pages_linked: ["[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]", "[[SAP错峰膨胀]]", "[[SAP性能指标（CRC AUL GBP Vortex）]]", "[[分区密度设计]]", "[[REL增强层]]", "[[COCO芯体平台]]", "[[IPC BCC OI Portfolio（开放创新项目组合）]]", "[[诺尔（Nuoer）]]", "[[LG Chem（LG 化学）]]", "[[Satellite Chemical（卫星化学）]]", "[[Sumitomo Seika（住友精化）]]"]
---

# SAP Selection Decision Base（17-SAP选型与实验数据决策库）

## 一句话定位 One-line positioning

本资料是本库 **SAP（高吸水树脂，Superabsorbent Polymer）选型／复配／测试的底层数据总仓**：一份内部汇编（internal compilation），合并 8 份同源文件（S1–S8），含 9 家供应商全牌号参数表、8 方案×3 法打样结果、DOE 混淆地图与成本敏感表。** Retrieve 任何 SAP 牌号参数、复配结论、测试口径冲突，都应先落到本页。**

## 摘要 Summary

文档上部是**参数底表**：按 BASF / Danson（丹森）/ Evonik / Formosa（台塑）/ LG Chem / Nippon Shokubai（日本触媒）/ Nuoer（诺尔）/ Satellite（卫星化学）/ SDP-Sandia / Sumitomo（住友精化）/ WanHua（万华）逐家列出 CRC（离心保留量）/ AUL（加压吸收量）/ GBP（凝胶床渗透率）/ Vortex（涡旋时间）与数据来源年份，另附 KCC-YJ 口径的**货架期（Shelf life，12–36 月）与在用产品（OEM-T5 / BCC / AC / EMEA / 墨西哥）**列。中部是**选型方法论**：9 牌号横评（吸水倍率 DI 54–63 vs 离心保水 30.6–36.7）、性能三象限（高容量型 / 平衡型 / 高渗透型）、按产品类型给出的推荐区间（薄型无绒毛浆婴儿裤 CRC 32–36 / AUL 24–28 / GBP ≥20 等）、多层角色定义（SAP1 皮侧快吸 / SAP2 快膨 / SAP3 延迟储库）。下部是**实验判决**：8 个配方单元 ×3 套测试协议的方法1 A（盐水三次加液）/ 方法2 B（新国标）/ 方法3 C（企标 Enterprise），以及 23 项归一化综合排名、因子分解、混淆地图与 CRITICAL/WARN 异常清单。结论层给出 PPT2/PPT3 成本口径、Design A/B/C 分区设计与仿真饱和度，以及 P0–P3 改进建议与「未获取数据」清单。

## 提炼的数字与结论 Key figures & conclusions

| Item 项目 | Value / Conclusion 数值·结论 | Note 备注 |
|---|---|---|
| 上游源件数 Upstream sources | 8 份（S1–S8），IMA + 本地同源 | 见表 S1–S8；IMA 原件未逐字核对 |
| SAM 等级数据源 | Global / Global v2 / KCC-YJ 三 sheet | 截止 2025-01，需注意时效 |
| 9 牌号 DI 自由溶胀 | 54.9（巴斯夫7059）–63.2（住友60S） | **非 EDANA CRC**，口径混用警示见下 |
| 离心保水率 ≈CRC | 30.6（NR-760H）–36.7（NR-950） | 本列才对应盐水 CRC |
| KC 511 GBP 真值 | 24（PDF/S1）｜25（Global NR511）｜26（KCC-YJ NR 511）｜35（Global v2 Nuoer 511） | **跨源四值冲突，引用必注来源** |
| 性能三象限 | 高容量型 CRC 38–45 / 平衡型 30–36 / 高渗透型 25–30 | GBP 分别 <10 / 10–30 / 30–50 |
| 主 KPI 企标回渗 @34 min | 门槛 < 5.9 g（全511 对照 8.363 g 的 70%），目标 ≤5.6 g | 量产决策门 G2 |
| 分区峰值饱和度 | Design C ≤67% 为基准；129% 溢出 = 拒绝 | 仿真第 3 次排尿后 |
| 顶层减薄红线 | 顶/底 split 禁 3/7（回渗约 2.6×恶化） | 5/5 为允许基线 |
| PPT3 总 SAP / 成本 | 13.5 g/片，US¢1.90/片 | 较单 SAP 高端基线 −40% SAP 成本、−59% 累计返渗 |
| SAP 单价 Unit price | LK804ND $1600/MT｜KC-511 $1300/MT｜NR-950 $1350/MT | 单价为 S2 §6.3 口径 |
| 价格敏感性 | SAP3 换日触 CAW → +10%；SAP1 换 BASF → +6% | 国产源（诺尔 $1,300–1,350/MT）为首要杠杆 |
| 批间一致性准入 | 3 批次 CRC/AUL/GBP/Vortex CV% ≤5% | S6/S7 §四 P3 |
| REL 五纤配方 | 2D ES 30% / 6D 偏心中空 ES 30% / 7D PTT-PET S/S 25% / 3D PE-PET 7% / 4D PVA 8% | Zone2 138–143 ℃ 激活 PTT 潜卷曲 |

> 🔴 **manual_review（2026-09-29）**：本资料含**供应商牌号单价（$1,300–1,600/MT）与单位成本（US¢1.90/片）**，属商务敏感价格信息。依 AGENTS.md §5「报价/合同条款类内容不得页面化」的红线，本页**只记要点与口径**（见上表），**不落完整价格表**；完整数据留存原文 `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/17-SAP选型与实验数据决策库.docx.md`，是否进一步页面化待人工确认。

## 测试协议 vs 选型结论 Test protocol decides the ranking

> 表头为「英文主 + 中文副」对照（Bilingual headers per AGENTS.md §2.0）。

| Condition 工况 | Governing mechanism 受限机制 | Who wins 谁占优 | Data 数据 |
|---|---|---|---|
| 高载短间隔 High-load short-interval（3.5 kg, 80 ml×3） | 渗透 Permeability（GBP）受限 | 高 GBP 全 511（KC511 GBP 24 最高，凝胶床不阻塞） | 0/20 min 吸速 20.83 / 18.50 s；混底底层 GBP 仅 2–6 普遍偏慢 |
| 低载多次 Low-load multi-dose（1.2–2.0 kg, 60 ml×4，企标） | 容量 Capacity（CRC）受限 | 多 SAP 混底全面反超 | 930/住友 4.325 g < 511/951+959 5.582 g < 全511 5/5 8.363 g < 3/7 11.270 g |
| 新国标 GB standard（4 kPa, 80 ml×2） | 综合 Mixed | 含住友或 959 的混底突出 | 1.120 < 1.482 < 1.620 < 1.647 < 1.820 < 2.118 < 4.315 < 5.312 g |

**推论 Conclusion**：原报告「全 511 最优」系**高压短间隔测试假象**；多 SAP 分层策略在贴近真实穿着的企标协议下获得实证支持——这正是本库 [[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]] 概念的原始证据。

## 关键论断（key_claims）

- **测试协议决定胜负，而非「单材 vs 多 SAP」本身** —— 支撑页：[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]
- **错峰膨润打败凝胶堵塞，但其 HYPERparameter 是溶胀快慢比 ratio 而非空间位置** —— 支撑页：[[SAP错峰膨胀]]、[[SAP性能指标（CRC AUL GBP Vortex）]]
- **分区加料完胜均布（Design C 67% vs Design B Crotch 129% 溢出）** —— 支撑页：[[分区密度设计]]、[[COCO芯体平台]]
- **8 单元中仅 5 组可作干净对比，N8 单元 FULLY CONFOUNDED → H3 假设失败且归因不安全** —— 支撑页：[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]
- **REL 存在双口径（Spunlace 35/26 gsm 打样 vs TAB 24 gsm 五纤仿真），官方未裁决** —— 支撑页：[[REL增强层]]
- **国产 SAP 源替换（诺尔 $1,300–1,350/MT）是首要成本杠杆** —— 支撑页：[[诺尔（Nuoer）]]、[[Satellite Chemical（卫星化学）]]、[[Sumitomo Seika（住友精化）]]

## 关联页面 Linked pages

- 概念 Concept：[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]、[[SAP错峰膨胀]]、[[SAP性能指标（CRC AUL GBP Vortex）]]、[[分区密度设计]]、[[REL增强层]]、[[芯体测试方法与验收基准（STM）]]
- 实体 Entity：[[诺尔（Nuoer）]]、[[LG Chem（LG 化学）]]、[[巴斯夫欧洲公司（BASF SE）]]、[[Satellite Chemical（卫星化学）]]、[[Sumitomo Seika（住友精化）]]、[[Nippon Shokubai（日本触媒）]]、[[IPC BCC（K-C Baby & Child Care 材料开发团队）]]
- 组合 Portfolio：[[IPC BCC OI Portfolio（开放创新项目组合）]]、[[COCO芯体平台]]

> 📌 OI 互链说明 Open Innovation linkage：本页所在的 Open Innovation 资料群为 OI 的材料/测试底座；涉及项目号时，**默认采用 `IPC BCC OI Portfolio（开放创新项目组合）` 页认定的重构版 19 项口径（`OI-1`~`OI-19`）**，若引用 `OI-01`~`OI-25` 形式必须同句注明出自年度汇报大纲 v7（2026-09-17）。

## 口径与存疑 Caliber warnings & open items

| 存疑项 Open item | 状态 Status | 说明 Note |
|---|---|---|
| 「吸水倍率」列口径混用 | 已识别 | S1 原文标注为 CRC，实为 DI 自由溶胀；与 S5 的盐水 CRC 31–36 不可混用 |
| KC 511 GBP 真值 | 跨源冲突 | 24 / 25 / 26 / 35 四值；引用须注明来源与年份 |
| N8(611) 参数 | 冲突/存疑 | Global 与 KCC-YJ 一致（CRC 40/39、AUL 12、GBP 3、Vortex 45），Global v2 记 Specs TBD |
| REL 双口径 | 未裁决 | Spunlace 35/26 gsm vs TAB 24 gsm；S8 决定以 REL sim 推进，安排对齐会 |
| 930 参数 | 部分补上 | SDP sheet 给 CRC 32 / AUL 19 / GBP 20 / Vortex 35（2001 spec, Legacy），数据陈旧 |
| 绒毛浆 / SAP 克重比 | 未获取 | 本体系为全芯体（fluff-free），仅蓬松棉 45 g |

## 原文 Source file

- 本地路径 Local path：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/17-SAP选型与实验数据决策库.docx.md`
- 原文链接 Original link：（无；IMA 内部知识文档 consolidated memo）
- 上游源件 Upstream sources：S1 `SAP选型策略与实验数据综合分析.md`（2026-07-21, v3）｜S2 `SAP选型分析_三PPT对比_中文版.docx`（2026-07-14~17）｜S3 `SAM_511_分析汇报.pptx`｜S4 `SAM_511_分析数据.xlsx`｜S5 `SAM Database-CW.xlsx`（2026-07-17）｜S6/S7 `SAP/SAM 知识储备诊断报告`｜S8 `全芯体材料清单与实验计划_v3.xlsx`（2026-07-29）

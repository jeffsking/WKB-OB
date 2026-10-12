---
type: source
title: High-Speed Core Forming Machine & SAP Dosing Design Review（录音纪要 2026-09-03 14-39）
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/录音纪要_260903143922.md
original_link: ""
date_published: 2026-09-03
date_processed: 2026-09-29
credibility: 内部一手（技术评审会 ASR 转写，英文为主，时间戳乱序）
knowledge_update_status: done
key_claims:
  - 高速芯体成型机项目：目标由 boss 推动 2028 年投产；pilot 线计划今年底（10–11 月）启动；成品目标为明年下半年
  - 成型鼓外径（OD）需基于产品全尺寸重新定义；同款 TBCW 材料可用两种不同的 forming drum 做出不同效果
  - 成型网（forming screen）最小孔间距可设计到 1.4 mm；单段成型所需真空约 8,500 CFM，建议加 40% buffer 至约 15,000 CFM，并用变频调速
  - 三区真空分工：high vacuum 成型图案 / sustained vacuum 保持图案不变形 / release vacuum（无真空）把图案转移到基材；liner 侧比 poly 侧复杂
  - 设计 4 套 SAP 计量系统：PSN 侧 2 套（用不同膨胀比自动抵消凝胶阻塞 hydro jump），liner 侧 1 套 + 预留 1 个功能颗粒位（未来气味控制 / 温度调节）
  - poly 侧计划加入约 40 GSM 绒毛浆，一是帮助毛细吸收，二是作为 SAP 之间的 spacer 以提升 SAP 利用率（V6 目标）
  - LSN 侧 SAP 采用更大粒径 + 更重壳交联以利于 intake；PSN 侧用两种不同膨胀比 SAP
  - 该机器本身只能做"平的"SAP 密度；分区（zoning）know-how 由本方自行掌握，不对设备商展示，属 black-box retrofit
  - 明确判断：该路线与现有 COCO 资产不可合并，必须二选一（either a or b）
  - 未知项：高速（800/900 ppm）下的 COV、以及未被真空 hold 住的 free SAP 量
pages_linked:
  - Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）
  - 分区密度设计
  - COCO芯体平台
  - SAP性能指标（CRC AUL GBP Vortex）
  - ActiveTech Platform（ActiveTech 在线薄芯体平台）
  - Kimberly-Clark（金佰利）
---

# High-Speed Core Forming Machine & SAP Dosing Design Review（录音纪要 2026-09-03 14-39）

> ASR 转写讹字说明：本稿为技术评审会录音自动转写，**英文为主**，且时间戳乱序（非按发言顺序）。已识别的讹字/音转：
> - **「HCH / HC」** = 设备合作方 [待验证]；「TSP / ts / Jacob ts」= **technical service provider（技术服务提供方）**
> - **「poly side / psn / PSS / PSN」** = 同一侧（poly 侧 / PSN）；「liner side / lss / LSN / lighter side」= liner 侧 / LSN
> - **「forming join / forming John / forming DRS / forming Dr」** = **forming drum（成型鼓）**；「OD」= 成型鼓外径
> - **「hydro jump / hydrogen blocks / hydro jumb」** = **凝胶阻塞（gel blocking / hydro-jump）**
> - **「free stand / frees stand / free s sap」** = **未被真空吸附的自由 SAP（free SAP）**；「stand density」= SAP density
> - **「zico machine / thrive machine / thrive z」** = 设备/工艺代号 [待验证]；「blazard」= Blizzard（芯体结构）[待验证]
> - **「sun cover / daihong / 大虹 / hundred」** = TSP 候选名 [待验证]；「ATV / ATT / AV」= 材料/技术代号 [待验证]；「Asahi / 三井花园」= 日本厂商 [待验证]
> - **「Tong / Craig / Jerry / JY / Outing / Liia / Han Wei」** 为人名音转 [待验证]
>
> ⛔ 本页只记录**已决**事项与**待决**问题；讨论中的想法一律归入 `Open issues 待决问题` 或 `Background 背景`。

## Attendees / Date 参会与日期

- Date 日期：**2026-09-03**（录音起始 14:39:22）
- 场景：高速芯体成型机（high-speed core forming machine）技术方案评审 + 材料侧 update
- 出席角色：机器/工艺方案主讲人（[待验证]）；材料侧同事；开放创新 / FEI 侧同事（[待验证]）；提及由亚洲区工程团队承接设备细节设计
- ⚠️ 具体人名一律 **[待验证]**，不做实名指派

## Key decisions 决策要点

1. **项目时间表（已定）**：由上级推动 **2028 年投产**；**pilot 线计划今年底（10–11 月）启动**；成品目标为**明年下半年**。
2. **成型鼓 OD 需基于产品全尺寸重新定义（已明确）**：目前只按某一尺码（air size）做过，需要拿到**全尺码的完整图**才能确定哪种成型鼓 OD 最合适。
3. **真空与成型网的设计口径（已给出）**：
   - 成型网（forming screen）**最小孔间距可设计到 1.4 mm**；
   - 单个成型段真空约 **8,500 CFM**，建议**加 40% buffer** → 约 **15,000 CFM** 风机；风机配变频器，可按实际表现加减速。
   - 三区真空分工（已明确）：**high vacuum** 成型图案；**sustained vacuum** 保持图案不变形；**release vacuum**（无真空）把图案转移到基材。
4. **SAP 计量系统布局（已设计）**：共 **4 套**。
   - **PSN 侧 2 套**：目的是用**不同膨胀比的 SAP** 来**自动抵消凝胶阻塞（hydro jump）**；
   - **liner 侧 1 套** + **预留 1 个位置给功能颗粒**（未来做气味控制 / 温度调节）。
5. **SAP 侧分工（已明确）**：**LSN 侧**用**更大粒径 + 更重壳交联**的 SAP，利于 **intake**；**PSN 侧**用两种不同膨胀比的 SAP。
6. **poly 侧加绒毛浆（已定方案）**：计划加入约 **40 GSM 绒毛浆**，双重目的 —— ① 帮助**毛细吸收**；② 作为 SAP 之间的 **spacer**，提升 SAP 利用率（对应 V6 目标"当前 SAP 设计过量"的问题）。配套开发小型 **hammer mill** 把绒毛浆投入 poly 侧。
7. **分区（zoning）know-how 不外泄（已明确）**：机器本身只能做"平的"SAP 密度；**分区的做法由本方工程师设计，对设备商保持 black box**（设备商交付模块后本方再改装）。设计工作由**亚洲区工程团队**承接（保密）。
8. **路线互斥（已明确判断）**：该路线与现有 COCO 资产**不可合并**，**必须二选一（either a or b）**；是否采用是业务决策。

## Open issues 待决问题

1. **SAP 分配比例未定**：目前口径是 liner 侧 : poly 侧 **50/50**，但实际需求可能不同（例如 liner 侧 3 g、poly 侧另几克）→ 需等 FEI 团队的最终选型输入，再决定成型鼓的不同 OD 设计。
2. **高速下的 COV 未知**：天津低速 pilot 线已验证机理可行，但**高速（800 / 900 ppm）下的 COV 未知**。
3. **高速下的 free SAP 未知**：不知有多少 SAP 未被真空 hold 住；若较多则回到常规 BC 工艺的问题。
4. **速度目标待定**：会中出现多个口径（100 / 300 / 400 / 800 / 900 ppm），低速 demo 线约 **400 ppm**，最终目标待定 [待验证]。
5. **liner 侧的真空方案更复杂**：poly 侧是"成型—保持—释放"三段；liner 侧还需要把图案从 PSN 转移并确保**不发生 SAP 变形**，方案更复杂。
6. **CD 分区 vs MD 分区**：CD 分区相对容易（分段计量即可）；**MD 分区更难**（需设计不同的真空段，且需要很好的 Allen-Bradley 伺服电机来保证 SAP "落在该落的地方、不会穿过去"）。
7. **P&G 的 SAP 印刷辊专利**：若采用类似 printing roll（可在 MD/CD 布 6 种 SAP），**需要付专利费**；本方倾向"**先留空间**"，是否采用未定。
8. **是否从设备商购买商业化机器**：会中明确"**不要从 HC 买商业化机器**"，但"目前仍在买其商业化机器" —— 存在矛盾，决策未定。
9. **验证与落地路径**：先在设备商侧（HCH）验证，合格后带回；可能**在南京厂腾出一条现有商业化产线**作为 machine bay —— 属计划，未定。
10. **TSP 候选未定**：技术服务提供方候选包括中国某公司、大虹、台湾某家等，均与 K-C 有长期关系；本方"**永远不会跟机器厂商碰这个**"，只与 TSP 合作 —— 最终选择未定。
11. **设备商合作边界**：会中提到对项目做减法（去掉一个 forming drum），并明确某些内容（如 Blizzard 施胶工艺）**不与设备商讨论**。
12. **材料侧方向待评估**：会上材料 update 涉及 —— 中空纤维、PCM 涂层、抗菌纤维、竹莱赛尔替代棉纤维、ATV/ATT（Asahi 被某日本公司收购，泰国有商业化线）、5 旦纤维用于强度、core 5 旦用于蓬松等；其中"** heavier 旦数更易传导尿液**"为观察口径，均**未定**。
13. **pilot 机的能力定位**：建议 pilot 机"尽可能交付全部能力与柔性"；但会中同时提醒 **成品性能 20% 来自工艺、80% 来自选什么材料** —— 二者如何权衡未定。
14. **是否替换现有 COCO**：明确回答"不会替换现有 COCO"，该路线是**新增技术路线的交付**，谁采用是业务决策。

## Action items 行动项

| Task 任务 | Owner 负责人 | Due 截止 | Status 状态 |
| --- | --- | --- | --- |
| 提供最终 SAP 选型输入，以便确定成型鼓 OD 与真空分配 | FEI 团队（ASR 提及 Jerry，[待验证]） | [待验证] | Open |
| 拿到全尺码产品图，据此设计成型鼓 OD 与 screen pattern | [待验证]（ASR 未指名） | [待验证] | Open |
| kick off pilot 线 | [待验证]（ASR 未指名） | 2026 年 10–11 月 | Open |
| 由亚洲区工程团队完成分区（zoning）设备细节设计（对设备商保密） | 亚洲区工程团队（ASR 未指名） | [待验证] | Open |
| 开发小型 hammer mill，把绒毛浆投入 poly 侧 | [待验证]（ASR 未指名） | [待验证] | Open |
| 评估 TSP 候选（中国某公司 / 大虹 / 台湾某家） | [待验证]（ASR 未指名） | [待验证] | Open |
| 评估是否采用 P&G 的 SAP 印刷辊方案（含专利费） | [待验证]（ASR 未指名） | [待验证] | Open |
| 会后发送 slides 给团队，收集具体兴趣点 | 主讲人（ASR 未指名） | 会后 | Open |
| 验证高速下的 COV 与 free SAP 量 | [待验证]（ASR 未指名） | pilot 线启动后 | Open |

## Background 背景

本次为高速芯体成型机（high-speed core forming machine）的技术方案评审会，议题覆盖成型鼓与成型网设计、真空系统分区、SAP 多通道计量与分区、poly 侧绒毛浆 spacer 方案、以及设备商合作边界与路线选择（与现有 COCO 的关系）；后半段为材料侧的 update。

## 提炼的数字与结论 Numbers & takeaways

| Item 项目 | Value 数值 | Note 备注 |
| --- | --- | --- |
| 成型网最小孔间距 | **1.4 mm** | 设计下限 |
| 单段成型真空 | 约 **8,500 CFM** | — |
| 建议风机容量 | 加 **40% buffer** → 约 **15,000 CFM** | 配变频器可调速 |
| 真空分区 | **high**（成型）/ **sustained**（保持）/ **release**（转移） | liner 侧更复杂 |
| SAP 计量系统 | **4 套**（PSN 侧 2 + liner 侧 1 + 预留功能颗粒位 1） | 预留位用于气味控制 / 温度调节 |
| SAP 分配比例 | 现状口径 liner : poly = **50/50**（可能变化） | 待 FEI 最终输入 |
| poly 侧绒毛浆 | 约 **40 GSM** | 毛细吸收 + SAP spacer |
| 低速 demo 线速度 | 约 **400 ppm** | 高速目标 800/900 ppm 未验证 |
| 单侧 SAP 种类上限 | 每层最多 **3 种**；PSN + LSN 合计最多 **6 种** | 需 printing roll（涉 P&G 专利） |
| 时间节点 | pilot 线 **2026 年 10–11 月**；投产目标 **2028** | 成品目标明年下半年 |
| 性能归因（会中口径） | 工艺 **20%** / 材料 **80%** | 强调材料选择的重要性 |

> 🔴 **manual_review（2026-09-29）**：本页涉及设备投资与采购决策、设备商与 TSP 名单、专利付费安排、南京厂产线腾挪规划、以及内部人事与时间要求。按 AGENTS.md §5，**价格 / 成本 / 合同条款 / 供应商与投资安排不得页面化**，此处仅保留机制性结论与量级。请回原文核对：
> `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/录音纪要_260903143922.md`
> 另：**分区（zoning）的设备细节被明确列为保密内容**，本页只记录"由本方自行设计、对设备商保持 black box"这一机制性事实，不记录任何具体设计参数。

## Sources 来源

- 原始记录：`RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/录音纪要_260903143922.md`（ASR 转写，2026-09-03 14:39:22）

## 关联页面 Related pages

- [[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]
- [[分区密度设计]]
- [[COCO芯体平台]]
- [[SAP性能指标（CRC AUL GBP Vortex）]]
- [[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]
- [[Blizzard Core（Blizzard 芯体结构）]]
- [[Kimberly-Clark（金佰利）]]

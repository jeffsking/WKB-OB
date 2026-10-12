---
type: source
title: Pin-Hole Module, Targeted Fluff Distribution & Elastic Recovery Process Review（新材料开发与弹性恢复工艺探讨）
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/新材料开发与弹性恢复工艺探讨.md
original_link: ""
date_published: "[待验证]（ASR 未标注会议日期；会中提及 Kirigami 与 pinhole 模块开发，疑为与同一家精密旋转模切供应商的后续会面）"
date_processed: 2026-09-29
credibility: 内部一手（供应商技术推荐会 ASR 转写，中英夹杂、时间戳乱序，转写质量差）
knowledge_update_status: done
key_claims:
  - 供应商向本方（**KC IPC + Casey China**）做了**六项技术推荐**，本页可辨识的三项为：**pinhole（打孔）模块**、**绒毛浆按工位差异化分布（targeted fluff distribution）**、**弹性恢复工艺（elastic recovery process）**
  - **Pinhole 模块**：已有模块**在机运行、已高速在线安装（inline）**；适用克重范围提及 **10–18 gsm**（另有 18 / 30 / 30 的口径）[待验证]
  - 高速打孔的两个关键工程点：① **DLC 涂层（类金刚石涂层）** —— 缓解发热、使运行更顺滑；② **孔—针间隙（hole-pin gap）** —— 决定 **pin 外径与孔内径**时必须做计算并留**安全余量（safety buffer）**
  - 高速下的失效风险：会产生**热 → 材料变形（critical）**；可通过**针的密度（density of pins）**来缓解
  - 两种针型：**carving（带雕刻）** 与 **tapered（锥形）**，**锥形更适合做小孔**
  - Pilot 模块速度可达 **500 m/min**，本方评价"**that's good enough**"
  - 本方需要供应商回复的两项数据：① 在 **500 m/min** 下可运行的**最小到最大 pinhole 尺寸**；② 可做哪些 **pin patterns**（目前只见到**圆孔**，本方问能否做**异形孔**）
  - **共同开发机制**：本方提供材料 → 供应商试切 → 若可行则考虑 **co-develop** 模块；采购将就模块成本单独联系
  - **绒毛浆按工位差异化分布**：不是把绒毛浆**均匀铺满**，而是**按各工位/部位的需要差异化分布**（如集中在目标区）→ 同时改善**性能、材料效率与舒适度**；已在 care 与 adult care 成功应用；绒毛浆与 SAP 的配比口径为 **50 / 50**
  - 该路线可**降低整体克重（BK）同时保持性能**
  - **弹性恢复工艺**：材料**拉伸 100% → 250%**，再**回复到 100%**，这个拉伸—回复循环即该工艺的定义；目的是**降低初次穿着时的僵硬感与不适（stiffness and discomfort）**
  - 应用对象为**成人产品**（抱怨穿着不舒服）；假设是"**如果不拉伸，损失很大**"；本方使用 **spandex（氨纶）** 而非另一种弹性材料 [待验证]
  - 本方确认供应商具备 **die cutter + 张力控制/拉伸**的能力 → 未来若开发 Kirigami 类项目会向其要方案
pages_linked:
  - Kirigami Apertured Nonwoven（切割拉伸开孔工艺）
  - 分区密度设计
  - Elastic Tension & Creep（橡筋张力与回缩率）
  - Kimberly-Clark（金佰利）
---

# Pin-Hole Module, Targeted Fluff Distribution & Elastic Recovery Process Review（新材料开发与弹性恢复工艺探讨）

> ASR 转写讹字说明：本稿为供应商技术推荐会的自动转写，**中英夹杂、时间戳乱序、转写质量差**，多处无法还原。已识别的还原与存疑：
> - **「pinho / pin hole / pinhole module」** = **针孔打孔模块**；「carving / uncarpeted」= 带雕刻 / 无雕刻；**「tapered」** = 锥形针
> - **「DLC coating / special coding / CI」** = **DLC（类金刚石）涂层** / 特殊涂层
> - **「hole pin gap」** = **孔—针间隙**；「safety buffer」= 决定针外径与孔内径时须留的安全余量
> - **「fluff formations specialist join type / distributing fluff uniformly across the full density to vary by job」** = **绒毛浆按工位差异化分布**（非均匀铺满）
> - **「BK」** = **basis weight（克重）**；「PLO / plot / miss techniques」= 绒毛浆与相关成形技术 [待验证]
> - **「elastic recovery / stretch and recovery cycle」** = **弹性恢复工艺**；「cyber / spanx」= 弹性材料种类（本方用 **spandex 氨纶**）[待验证]
> - **「Youhan Kimberley / Youhan」** = **Yuhan-Kimberly**；「Casey, China / K from IPC」= 本方团队
> - **「thosson carbide / dichoter」** = 硬质合金 / die cutter；「jerreds / Jerry」= 人名音转
> - **「Sam / S. Sam / 巴格森」** 含义不明 [待验证]
>
> ⛔ 本页只记录**已决**事项与**待决**问题；讨论中的想法一律归入 `Open issues 待决问题` 或 `Background 背景`。

## Attendees / Date 参会与日期

- Date 日期：**[待验证]** —— 转写未标注；会中提及 Kirigami 与 pinhole 模块开发，**疑为与同一家精密旋转模切/模块供应商的后续会面**
- 场景：供应商技术推荐会（六项推荐）+ 共同开发探讨 + 名片交换
- 供应商方：技术与业务主讲（未具名）[待验证]
- 本方：**KC IPC** 与 **Casey China**（K-C 中国）联合参与 —— 会中明确"若这个项目我们认为可以共同开发"
- ⚠️ 具体人名一律 **[待验证]**，不做实名指派

## Key decisions 决策要点

1. **Pinhole 模块已在线运行（供应商已确认）**：该模块**已经在机器上运行**，且是**高速、已在线安装（inline）**的状态，不是概念。
2. **高速打孔的两个关键工程点（供应商给出的两条 tips）**：
   - ① **DLC 涂层（类金刚石涂层）** —— 作用是**缓解发热（alleviate the heat）**并让运行**更顺滑（more smooth）**；
   - ② **孔—针间隙（hole-pin gap）** —— 决定 **pin 外径与孔内径**时**必须做计算**，并留出**安全余量（safety buffer）**。
3. **高速下的失效风险（已识别）**：高速下会产生**热 → 材料变形**，这是**关键（critical）**问题；可通过**针的密度（density of pins）**来缓解。
4. **两种针型（已给出）**：**carving（带雕刻）** 与 **tapered（锥形）** —— **锥形更适合做小孔（small hole）**。
5. **Pilot 能力（已给出）**：pilot 模块速度**可达 500 m/min**；本方评价"**that's good enough**"。
6. **共同开发机制（已建立）**：本方**提供材料** → 供应商**试切** → 若有前景则**共同开发（co-develop）**模块；采购将就模块成本单独联络。
7. **Kirigami 能力确认**：本方明确表示已知供应商具备 **die cutter + 张力控制 / 拉伸**的组合能力 → 未来若开发此类项目会向其征求方案。
8. **绒毛浆差异化分布（已应用）**：不是把绒毛浆**均匀铺满整个密度**，而是**按工位/部位需要差异化分布**（例如集中在目标区）→ **同时改善性能、材料效率与舒适度**；供应商称已在 **care 与 adult care** 成功应用；绒毛浆与 SAP 的配比口径为 **50 / 50**。
9. **该路线可降克重**：结合相应的成形方式，**可降低整体 BK（克重）同时保持性能**。
10. **弹性恢复工艺（第六项，已定义）**：材料**从 100% 拉伸到 250%**，再**回复到 100%** —— 这个**拉伸—回复循环即该工艺的定义**；目的是**降低初次穿着时的僵硬感与不适**。
11. **弹性恢复的应用对象（已明确）**：**成人产品** —— 抱怨"穿着不舒服"；供应商假设"**如果不拉伸，损失很大**"。本方使用 **spandex（氨纶）**。

## Open issues 待决问题

1. **本方明确要求的两项数据（尚未回复）**：
   - ① 在 **500 m/min** 下可运行的 **pinhole 尺寸范围（最小 → 最大）**；
   - ② 可做哪些 **pin patterns** —— 目前**只见到圆孔**，本方问能否做**异形孔（abnormal patterns）**。
2. **打孔 vs 热风的取舍**：会中出现"pinhole 还是 hot air 更好"的提问，**未获结论** [待验证]。
3. **模块成本未知**：本方问"完整 pinhole module 的成本是多少"，供应商未现场给出 → 转由**采购后续联系**。
4. **克重口径不一致**：转写中出现 **10–18 gsm** 与 **18 / 30 / 30** 两组数字，对应关系不明 [待验证]。
5. **"more than five hundred / less than two hundred" 的所指不明**：疑为速度或某种数量口径，**取决于材料** [待验证]。
6. **模块仍在开发中**：本方问"这个模块的开发计划是什么"，答"**只是个概念，可能两三年**" → 与"已在机运行"的表述存在**口径冲突**，需澄清（可能指**另一个新模块**）。
7. **能否在本方 machines 上安装 pilot 模块**：会中讨论"如果我们想在高速线上装这个模块做学习"，供应商给了肯定回应，但**排期未定**。
8. **清洗/维护问题**：会中提及"切了以后洗不掉、很难洗" → 打孔后的**清洁与残留**问题未展开 [待验证]。
9. **材料安全与环境**：会中就涂层的讨论提到两点顾虑 —— 该材料**直接接触**，需确认**对健康无害**；同时也关心**对环境是否有害** → **未获结论**。
10. **健康与环境两项均未闭环**（"They are for the health and the environment"）→ 需供应商补充资料。

## Action items 行动项

| Task 任务 | Owner 负责人 | Due 截止 | Status 状态 |
| --- | --- | --- | --- |
| 回复 500 m/min 下 pinhole 的尺寸范围（最小→最大） | 供应商（ASR 未指名） | 后续（非当日） | Open |
| 回复可实现的 pin patterns（圆孔之外能否做异形孔） | 供应商（ASR 未指名） | 后续 | Open |
| 就完整 pinhole module 的成本与供应商对接 | 本方采购（ASR 未指名） | [待验证] | Open |
| 本方提供材料 → 供应商试切，评估是否 co-develop | 双方（ASR 未指名） | [待验证] | Open |
| 澄清"已在机运行"与"只是概念、需两三年"两个口径 | 供应商（ASR 未指名） | [待验证] | Open |
| 补充涂层材料的健康与环境安全资料（直接接触材料） | 供应商（ASR 未指名） | [待验证] | Open |
| 未来 Kirigami 类项目向供应商征求方案 | 本方（ASR 未指名） | 未来 | Open |
| 会后整理并发出 follow-up 摘要 | 本方（ASR 未指名） | 会后 | Open |

## Background 背景

供应商向 KC IPC 与 K-C 中国团队做了一次技术推荐（共六项，转写可辨识三项）：核心是**高速 pinhole 打孔模块**的工程细节（涂层、孔针间隙、针密度、针型、pilot 速度），附带**绒毛浆按工位差异化分布**以降克重，以及**弹性恢复工艺**以改善成人产品的初次穿着不适。本方的立场是"对任何能做孔的工艺都很感兴趣"，并希望用本方材料去验证、进而共同开发模块。

## 提炼的数字与结论 Numbers & takeaways

| Item 项目 | Value 数值 | Note 备注 |
| --- | --- | --- |
| Pinhole 模块状态 | **已在机运行、高速在线（inline）** | 另有新模块"只是概念、可能两三年" [口径待澄清] |
| 克重范围 | **10–18 gsm**（另有 18 / 30 / 30 口径）[待验证] | 取决于材料 |
| Pilot 速度 | **可达 500 m/min** | 本方评价"good enough" |
| 关键工程点 1 | **DLC 涂层** —— 缓解发热、更顺滑 | 高速必备 |
| 关键工程点 2 | **孔—针间隙** —— 须计算并留**安全余量** | 决定针外径与孔内径 |
| 高速失效风险 | **热 → 材料变形（critical）** | 可用**针的密度**缓解 |
| 针型 | **carving（雕刻）** / **tapered（锥形）** | **锥形更适合小孔** |
| 孔型现状 | **仅圆孔** | 异形孔待确认 |
| 绒毛浆分布 | **按工位差异化**（非均匀铺满） | 已用于 care / adult care |
| 绒毛浆 : SAP | **50 / 50** [待验证] | — |
| 路线收益 | **降低整体 BK（克重）同时保持性能** | — |
| 弹性恢复工艺 | **100% → 拉伸 250% → 回复 100%** | 该循环即工艺定义 |
| 弹性恢复目的 | **降低初次穿着的僵硬感与不适** | 面向**成人产品** |
| 弹性材料 | 本方用 **spandex（氨纶）** | 未用另一种弹性材料 [待验证] |

> 🔴 **manual_review（2026-09-29）**：本页涉及**模块成本（转由采购对接）、供应商的开发计划与时间、以及涂层的健康与环境安全资料**。按 AGENTS.md §5，**报价与商务不得页面化**；此处只保留机制与量级。请回原文核对：
> `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/新材料开发与弹性恢复工艺探讨.md`
> 另：全文为**低质量 ASR**，多处口径冲突（"已在机运行" vs "只是概念、两三年"）与含义不明处（Sam / 巴格森 / plot / miss techniques）**必须回溯录音**；涂层为**直接接触材料**，健康与环境影响**尚未闭环**，引用前须确认。

## Sources 来源

- 原始记录：`RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/新材料开发与弹性恢复工艺探讨.md`（ASR 转写，会议日期 [待验证]）

## 关联页面 Related pages

- [[Kirigami Apertured Nonwoven（切割拉伸开孔工艺）]]
- [[分区密度设计]]
- [[Elastic Tension & Creep（橡筋张力与回缩率）]]
- [[Kimberly-Clark（金佰利）]]

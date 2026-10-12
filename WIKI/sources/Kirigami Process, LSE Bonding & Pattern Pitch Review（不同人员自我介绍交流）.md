---
type: source
title: Kirigami Process, LSE Bonding & Pattern Pitch Review（不同人员自我介绍交流）
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/不同人员自我介绍交流.md
original_link: ""
date_published: "[待验证]（ASR 未标注会议日期）"
date_processed: 2026-09-29
credibility: 内部一手（K-C 内部现场交流会 ASR 转写，中英夹杂，时间戳乱序）
knowledge_update_status: done
key_claims:
  - Kirigami（切割 + 拉伸开孔）工艺三支柱为 material / stretch / pattern；拉伸比越大开孔率越大，但存在破膜风险，实际首步只能开到 3–4%
  - Kirigami 目前只用于 surge（导流层），从未用于 topsheet / topical liner —— 切割边缘拉伸后变形、与皮肤摩擦是未解问题
  - Pattern pitch 最终定为 10 mm（曾比较 12 / 8 mm），由 RNE 团队决策，且与整体 CD 相关；另一处决策点为 14 mm vs 10 mm
  - LSE（超声波 bonding 模块）已试过 adhesive 与 ultrasonic 两条路线，两次 trial 均保留 ultrasonic；adhesive 在细线上不易施加，ultrasonic 因切割而建立强度，须保证 CD 方向线强度均匀，且存在 build-up（积料）问题
  - 产线资产：TJ 1、2 号机为 open diaper；21/22/23 号机为成人裤（Depends 类）；为控制项目范围，仅在 2、3 号机上应用该工艺
  - 项目 Bay Max 为 IPC innovation accelerator 获奖项目、IPC 全球最高优先级项目之一；其 v2 版本考虑把层换成 TBCW
  - Jerry 另有项目 BA：用低 capex 超声波把 TBCW liner 与 spunbond 层压
  - 与 ActiveTech 的 ROTC 工艺为离线执行，再与常规产线结合，可产出三类产品
pages_linked:
  - TBCW结构
  - ActiveTech Platform（ActiveTech 在线薄芯体平台）
  - ROTC（Real Online ThinTech Core）
  - Ultrasonic Bonding of PET-Containing Topsheet
  - ADL（导流层）
  - IPC BCC（K-C Baby & Child Care 材料开发团队）
---

# Kirigami Process, LSE Bonding & Pattern Pitch Review（不同人员自我介绍交流）

> ASR 转写讹字说明：本稿为 K-C 内部现场交流会录音自动转写，**中英夹杂**，且时间戳乱序（非按发言顺序）。已识别的讹字/音转：
> - **「kigami / kiligami / kindergarten」** = **Kirigami**（切割 + 拉伸成孔工艺）；「hyperion / hyperium / per s hyper」= 材料/牌号代号 [待验证]
> - **「LSE / LSD / LC / SLE」** = 同一 bonding 模块（**超声波**路线为主）[待验证]；「topic / topical / tropical liner」= **topsheet liner（面层）**
> - **「TBCW / TBCWK / TVCW」** = TBCW（through-air-bonded carded web，热风穿透粘合梳理网）
> - **「RNE / RNA / RY / K瑞mi / 凯瑞mi」** = 区域研发团队（R&E）[待验证]；「KCP」= K-C 工厂/产线 [待验证]
> - **「grid surgery / grid surging / surge liner」** = 网格状 surge（导流层）；「am depends」= 成人 Depends 类产品
> - **「Chris / Brian / Jerry / Harold / Li X / Mark」** 为人名音转 [待验证]，本页只保留角色，不做实名指派
> - **「nineteen degree / 十九度」** = [待验证]（疑为角度或工艺参数）
>
> ⛔ 本页只记录**已决**事项与**待决**问题；讨论中的想法一律归入 `Open issues 待决问题` 或 `Background 背景`。

## Attendees / Date 参会与日期

- Date 日期：**[待验证]** —— 转写未标注会议日期
- 场景：K-C 内部现场交流 + 参观车间（machine bay / shop floor）；会议含自我介绍环节（本文件标题即由此而来）
- 出席角色（ASR 可辨识，均为 [待验证]）：
  - **pre-FEI / Open Innovation（IPC）** 侧：一名负责 IPC 开放创新的同事（加入约 1.5 年，此前 12 年其他岗位）
  - **Open Innovation** 侧：一名负责 FEI 前段支持的同事（团队为去年新成立；此前在中国/韩国业务工作约 7–8 年）
  - **工艺 / 测试开发** 侧：一名工艺工程师出身（约 6 年工艺 → ID 部门 → 现负责 test development，兼 DNC 某产品项目在中国的负责人）
  - 另一名长期在职同事（自电气工程师起步，后转运营/采购/capex，现于 open innovation）
- ⚠️ 具体人名一律 **[待验证]**，不做实名指派；个人联系方式不入页面

## Key decisions 决策要点

1. **Kirigami 工艺的三支柱（已明确）**：**material（材料）/ stretch（拉伸）/ pattern（花型）** 三者构成"三角形"工艺；RNE 团队在此基础上做了改进。工艺版本为 **V1 / V2 / V3**，**V3 为当前在跑的工艺版本**。
2. **Kirigami 的应用边界（已明确）**：目前**只用于 surge（导流层）**，**从未用于 topsheet / topical liner**。
3. **LSE 路线已选定超声波**：已做过 **2 次 trial**，两个方案（adhesive 与 ultrasonic）对比后**两次都保留 ultrasonic**。
   - adhesive 在"很细的线"上不易施加；
   - ultrasonic **因切割而建立强度**，须保证 **CD 方向的线强度均匀**；
   - 已知问题：**build-up（积料）**。
4. **Pattern pitch 定为 10 mm**：曾比较 **12 mm / 8 mm**，最终由 RNE 团队决定 **10 mm**；该选择与**整体 CD** 相关。另一处决策点为 **14 mm vs 10 mm pitch**。
5. **项目范围控制（已决）**：为最小化项目范围，**只在 2 号与 3 号机**上应用该工艺（其余工序沿用既有）。
6. **项目 Bay Max 的定位（已明确）**：为 **IPC innovation accelerator 获奖项目**，属 **IPC 全球最高优先级项目之一**。其 **v2 版本考虑把层改为 TBCW**。

## Open issues 待决问题

1. **Kirigami 用于面层的未解问题（本方主动提出的开放问题）**：切割 Kirigami 时会**同时切割并拉伸材料**，材料中的纤维会发生形变；切边拉伸后**不平整、会变形**。若用作 surge 有利于创造 void volume（空隙体积），但若用于 **topical liner（面层）**，**如何降低与皮肤的摩擦**仍未解 —— 属开放问题，理论上取决于 draw（拉伸倍率）。
2. **开孔率与破膜的权衡**：拉伸比（stretch ratio）越大，开孔面积越大；但**有时会破**。若设定一步拉伸，实际第一步只能开到约 **3–4%**；拉伸比需**在线根据材料调整**，无法做成固定的一步/两三步拉伸。
3. **TBCW 的 GSM 波动**：TBCW 有时存在 **GSM 波动**（band 由 signal 控制），且 **CD 方向略有差异**；运营团队有时会到现场 traceability 排查。
4. **消费者可辨识度**：开口面积要"足够大到消费者能看见"，但要开到这个程度**对 first grade（一等品率）不易** —— 开孔率与一等品率之间存在冲突。
5. **LSE 的施加位置**：LSE 应在**直接切割后**施加，还是在**第一轮拉伸之后**施加 —— 会中提问，**未给出结论**。
6. **adhesive 路线是否被彻底放弃**：会中提到"KC 好像没试过 adhesive"，以及"ultrasonic the adhesive sometimes not easy to apply"，最终选择 ultrasonic；但**未明确 adhesive 是否被完全排除**。
7. **Pattern 保密与工程侧的知悉边界**：花型细节（角度、间距、pitch）**高度保密**，通常只在 RNE 与工艺人员范围内；工程团队往往只拿到"要什么"而**不知其背后的原因**。
8. **"直接拿来主义" vs 自主设计**：会上有人倾向**直接复制现有花型**（"这个 pattern 咱们也不要动脑筋了，直接拿来主义就好了"），另一观点强调需要**给出设计原则与 guideline** —— 未形成决定。
9. **Nina 团队（圣地亚哥）的花型设计可行性**：许多花型设计"第一眼就知道在高速 converting 上跑不通"，且存在 adhesive 限制；Nina 团队有 3D 打印模块用于验证。
10. **设计尺寸的对外交付边界**：本方倾向**把设计尺寸给出去，若对方认为有能力改，让其自行修改**；细节仍需自己把关（信任度约"八成透明度"）。
11. **Kirigami 设计落地地域受限**：该设计全球推了多年，**只在韩国落地**，其他地区未采用。
12. **是否采用 topical（面层）路线的 registration（对位精度）要求**：若走 topical 路线，对位必须更精确 —— 提及但未展开。

## Action items 行动项

| Task 任务 | Owner 负责人 | Due 截止 | Status 状态 |
| --- | --- | --- | --- |
| 会后分享本场材料给参会方 | [待验证]（ASR 未指名） | 会后即时 | Open |
| 参观车间（machine bay / shop floor） | 双方（ASR 未指名） | 当日（约 10:30） | Closed |
| 如需更详细的花型信息（角度、间距、pitch），联系图纸与资料持有方 | [待验证]（ASR 提及图纸持有者，未指名） | [待验证] | Open |
| 就 Kirigami 用于面层的摩擦问题给出回答 | [待验证]（ASR 未指名） | [待验证] | Open |
| 确认 LSE 的施加位置（切割后 vs 首轮拉伸后） | [待验证]（ASR 未指名） | [待验证] | Open |
| 就 Kirigami 相关材料与花型做进一步测试与问答（含周四线上会） | [待验证]（ASR 提及周四线上安排，未指名） | 周四 [待验证] | Open |

## Background 背景

本次为 K-C 内部现场交流会（含自我介绍环节），主题围绕 Kirigami（切割 + 拉伸开孔）工艺在 surge 上的应用现状、花型（pattern/pitch）设计、以及 LSE bonding 模块在 adhesive 与 ultrasonic 之间的路线选择；同时涉及 Bay Max、BA 等 IPC 项目与 ActiveTech 的 ROTC 工艺衔接。

## 提炼的数字与结论 Numbers & takeaways

| Item 项目 | Value 数值 | Note 备注 |
| --- | --- | --- |
| Kirigami 三支柱 | material / stretch / pattern | 三角工艺 |
| 工艺版本 | **V1 / V2 / V3**；**V3 为当前在跑** | RNE 团队改进 |
| 首步开孔率 | 约 **3–4%**（若设定一步拉伸） | 拉伸比越大开孔越大，但会破 |
| Pattern pitch | 最终 **10 mm**（曾比较 **12 / 8 mm**）；另一决策点 **14 mm vs 10 mm** | 与整体 CD 相关 |
| LSE 试错次数 | **2 次 trial**，两方案（adhesive / ultrasonic），两次均保留 **ultrasonic** | — |
| 应用范围控制 | 只在 **2 号、3 号机**上应用该工艺 | 最小化项目范围 |
| 产线资产 | TJ **1、2 号机** = open diaper；**21 / 22 / 23 号机** = 成人裤类 | [待验证] |
| TBCW 规格提及 | **30 GSM**（与 adhesive 路线对比时提及） | [待验证] |
| Kirigami 应用边界 | **只用于 surge**，从未用于 topsheet / topical liner | 摩擦与变形是障碍 |
| 开孔率 vs 一等品率 | 开孔要"大到消费者能看见"，但**对一等品率不易** | 存在冲突 |
| Bay Max 项目 | IPC innovation accelerator 获奖；**IPC 全球最高优先级项目之一** | v2 考虑改用 TBCW 层 |
| BA 项目 | TBCW liner + spunbond 层压，**用低 capex 超声波** | 与 Bay Max 并行 |
| Kirigami 落地地域 | 全球推多年，**只在韩国落地** | 其他地区未采用 |

> 🔴 **manual_review（2026-09-29）**：本页涉及 K-C 内部项目代号（Bay Max / BA）、产线资产编号与项目优先级，以及**个人姓名与联系方式**。按 AGENTS.md §5，个人联系方式不得页面化；项目与产线信息属内部运营信息，此处仅保留机制性结论与角色，不指名个人。请回原文核对：
> `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/不同人员自我介绍交流.md`
> 另：花型细节（角度、间距、pitch 图纸）为高度保密信息，**本页不记录任何图纸数值**，仅记录已披露的 pitch 决策（10 mm）。

## Sources 来源

- 原始记录：`RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/不同人员自我介绍交流.md`（ASR 转写，会议日期 [待验证]）

## 关联页面 Related pages

- [[TBCW结构]]
- [[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]
- [[ROTC（Real Online ThinTech Core）]]
- [[Ultrasonic Bonding of PET-Containing Topsheet]]
- [[ADL（导流层）]]
- [[IPC BCC（K-C Baby & Child Care 材料开发团队）]]
- [[Kimberly-Clark（金佰利）]]

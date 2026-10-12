---
type: source
title: "Global Online Embossing Platform & Active Tech Direction Review（录音纪要 2026-09-03）"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/录音纪要_260903154213.md
original_link: ""
date_published: 2026-09-03
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "在线压花（online embossing）的 pattern 设计原则：各 bonding 线的**bond area 必须等面积/等间距**，否则拉伸变形会破坏已形成的 3D 效果，且张力不均"
  - "设备商（传越）只提供机器与自有雕刻能力，**不具备 pattern 开发能力** —— pattern 必须由 KC 提供设计，对方按设计加工（并提供可选 pattern menu）"
  - "在线压花的目标车速为 450–500 m/min（现约 440）；embosser/anvil 的 pin 角度（非 90°、需带锥度）必须在特定车速下验证"
  - "Active Tech 2.0（气吹清除堵塞 SAP）与 3.0（solar valve on-off 类 3D 打印）均被我方判断为不成熟：3.0 想把单元从 14 mm 收到 7 mm 甚至 2 mm，但受限于开关速度、下落精度与 SAP 固化/受潮，实际做不到；且能耗更高"
  - "北美团队仍在研究 3.0 并拟于 11 月决策；我方认为 10 月 workshop 后再谈「是否转回 active 方向」更合适（需论证 capex 更低）"
  - "平台化与落地的组织缺口：缺一名专职工程资源作为全球开发方与各市场 local 团队之间的固定接口，用于把方案标准化并交付执行"
  - "低熔点 PP 方向：若 PP 熔点能比现有低约 30 ℃，纺粘可直接与 TBCW 粘合而不必用双组分（bico）结构"
pages_linked: ["[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]", "[[Ultrasonic Bonding of PET-Containing Topsheet]]", "[[分区密度设计]]", "[[COCO芯体平台]]"]
---

# Global Online Embossing Platform & Active Tech Direction Review（录音纪要 2026-09-03）

> 本页为 ASR 转写稿（soundrecording）的编译产物，文件名含录制时间戳 **260903154213（2026-09-03 15:42:13）**。会议为**中英夹杂**（全球团队参与），转写讹字极多（如「传越/穿云」「solar well / solar valve」「two point / 2.0」「three point / 3.0」等）。无法确证者标 `[待验证]`。

## Attendees / Date 参会与日期

| 项目 | 内容 |
|---|---|
| Date 会议日期 | **2026-09-03**（由文件名时间戳得出） |
| Location 地点 | 韩国 `[待验证]`（转写出现「第二次来韩国」，判断为 KC 韩国侧的面对面会议） |
| Attendees 参会 | `[待验证]` —— 转写中出现：Brian、Jerry、Scott、Chris、腾哥、彤彤、何叶、李想（Li X）、Mark，以及 **YK 团队、北美（North America）团队、ICT、high speed converting 团队**（线上或现场未明）。原文未署名，**不作实体页依据** |
| Format 形式 | 全球研发对齐会：在线压花平台 + Active Tech 路线方向 + 组织资源与会议机制 |

## 一句话定位

一次全球团队对齐会：确认在线压花（online embossing）的**设备能力边界与 pattern 设计原则**、评估北美主推的 **Active Tech 2.0/3.0** 是否值得跟、并讨论平台化之后**谁来负责落地**这一组织缺口。

## Key decisions 决策要点

> 只记会上明确「定了 / 达成共识」的事项。

1. **pattern 设计原则定案**：无论采用哪种 pattern，各 bonding 线（line 1–5）的 **bond area 必须相等**，否则拉伸时变形会把已形成的 3D 效果破坏、且张力不均。
2. **pattern 由 KC 自己设计**：设备商只提供机器与自有雕刻（in-house engraving）能力，**不具备 pattern 开发能力**；KC 出设计、对方按设计加工，对方也会提供可选 menu。
3. **在线压花的目标车速定为 450–500 m/min**（当前约 440，450 可接受）。
4. **双月（bi-monthly）电话会机制**：用于这些项目的进度更新（另有建议改为「每年一次 + 面对面周一次」，节奏未最终定）。
5. **10 月中旬举办 V6 专题 workshop**，拟邀请 YK、ICT、high speed converting 与 angels 团队参加。

## Open issues 待决问题

- **Active Tech 3.0 的物理可行性被质疑**：把单元从 **14 mm** 收到 **7 mm**、甚至想收窄到 **2 mm**；但受限于 ① 开关（on/off）速度、② 下落精度、③ **SAP 固化/受潮后不能干净落下**（需要时间才落得下）→ 判断**实际做不到 2 mm**；且能耗更高。
- **Active Tech 2.0 的清除方式不经济**：用气吹把堵住的 SAP 吹掉，系统复杂且可控度不高；对比之下，另一种方式（机械手「撸掉」）更安全。
- **方向决策的时机**：北美仍在研究 3.0 并拟 **11 月决策**；我方内部（彤彤、荷叶）已倾向放弃，但**当前不是告知北美的合适时机**，拟于 **10 月 workshop 之后**再谈，并需论证「转向 active 方向 capex 更低」。KC 侧方向**尚未确认**（产品归 Chris 团队、process 归另一团队）。
- **平台化 vs 落地的组织缺口**：global 在没有产品设计的情况下先开发平台（属工程技术准备），**local 以落地为主**；缺一名**专职工程资源**作为 Brian / Jerry 的固定对接人，负责把方案标准化并交付各市场执行 → **目前没有这个资源**。
- **各市场资产差异导致无法一套方案通吃**：不同市场 machine base、product format、loading 水平都不同；不可能为每个市场单独开发工程方案，也不能只做一套不管差异 → 需要「可 handed over 且便于 local 改装（retrofit）」的技术就绪度，但**到什么程度可以交付未定义**。
- **高速下的真空参数未知**：中国侧不明确基材在高速下应有的真空值；历史经验是把 forming fan 容量提升约 **1.5 倍**后 3D 外观明显改善 → 真空与 pattern 设计都关键。
- **embosser / anvil 的 pin 角度未验证**：pin 不是 90°，需带锥度（taper），其角度必须在特定车速下验证。
- **低熔点 PP 待推进**：若 PP 熔点可比现有低约 **30 ℃**，纺粘即可直接与 TBCW 粘合而不必用双组分（bico PE/PE）结构；候选供方（Sabic 一类）拟安排会议讨论 `[待验证]`。
- **弹性材料在中间层的方案**：参考 pampers 的做法——**弱粘合（poorly bonded）PP 面层 + 弹性膜**，拉伸时 PP 被「激活断裂」而露出弹性；但会破坏面层表面，且中间放弹性材料会破坏面层外观 → 未定。
- **微胶囊（microencapsulation）**：天然提取物（life science 方向）用于长效释放（水溶性，尿湿后释放）；国内供应商在做，**成本是否可承受、应用位置均未定**，属最早阶段。
- **除臭颗粒（沸石基 + 定制催化剂）**：目标是**并入 TBCW 的后处理油剂（aftertreatment oil）喷到 outer cover**；放在包装内只是为了先验证有效性。催化剂针对「胶味」与「塑料味」两类目标分别定制，但捕捉机理相同。
- **BNC 供应策略**：供应商仍是中式实验室级别（非工厂），只要能稳定供货即可，配方可外包给化学实验室/小厂做迭代；其核心优势是**用废水做碳源使成本能下来**。
- **pad 利用率的终极判据**：能否**去掉 set（集中区）**、让尿液分布到整个 pad（约 400 mm）才算成功；用 **screen depth（pocket）** 做 zone density 是被讨论的实现路径之一（而非只是缩小方块）。
- **Blizzard 的 air knife**：ND 方向形状很刚硬（rigid square），在找 curved 形状（version 7 方向）。

> 🔴 **manual_review（2026-09-29）**：本资料含**设备与模块报价量级（2.0 约 400k、模块 30–50k / 70k 量级）、供应商名称、北美决策时点与全球方向对齐的商务与组织信息**，属商务敏感与未公开决策（AGENTS.md §5）。本页只记**量级与决策流程**，**不落报价表与组织人事结论**；原文留存于 `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/录音纪要_260903154213.md`。

## Action items 行动项

| Task 任务 | Owner 负责人 | Due 截止 | Status 状态 |
|---|---|---|---|
| 提供设备商的公司介绍/手册供工程师评估 | `[待验证]`（原文：「Let me figure out and then send to you by next week」） | 次周 | 待启动 |
| 与设备商共享当前材料规格，确认是否适配其机器并安排试跑 | 双方（KC 提供 spec + 材料） | 9 月底（原文：「end of September」） | 进行中（材料是否充足待确认） |
| 准备两套 pattern（中国 TBCW 系 + 巴西另一组合）并共享 code 信息 | `[待验证]` | 未指定 | 待启动 |
| 10 月中旬 V6 专题 workshop（邀请 YK / ICT / high speed converting / angels 团队） | 组委会（Brian 发正式邀请） | 10 月中旬 | 待启动 |
| 设立双月电话会机制同步项目进展 | `[待验证]` | 未指定 | 待启动 |
| 与低熔点 PP 候选供方安排会议 | `[待验证]` | 未指定 | 待启动 |
| 明确各市场的目标车速与「高速」定义（用于 pin 角度与真空验证） | `[待验证]` | 未指定 | 待启动 |
| 明确「可 handed over」的技术就绪度门槛 | 全球 + local 工程 | 未指定 | 待启动 |

## Background 背景

在线压花/成型平台是全球多个市场共同的技术底座，但各市场的机器资产与产品形态差异大；同时北美主推的 Active Tech 2.0/3.0 与亚太的落地判断出现分歧，故召开本次对齐会。

## 提炼的数字与结论

| 项目 | 数值 / 结论 | 备注 |
|---|---|---|
| 在线压花目标车速 | **450–500 m/min**（当前约 440） | 450 可接受 |
| 设备商既有能力 | 低速机（约 **300 m/min**）在线 embossing 已有 ECM 应用 | 提供 pattern menu，但不做 pattern 开发 |
| forming fan 提升效果 | 容量提升约 **1.5 倍** → 3D 外观明显改善 | 真空是关键变量 |
| Active Tech 3.0 单元尺寸 | 现 **14 mm** → 目标 **7 mm**，想做 **2 mm** | 受开关速度/下落精度/固化限制，判断做不到 |
| Active Tech 2.0 报价量级 | 约 **400 k**（各国摊派口径）`[待验证]` | 北美推动 |
| 模块报价量级 | 约 **30–50 k**；整机/全模块约 **70 k** 量级 `[待验证]` | 转写不完整，只记量级 |
| 低熔点 PP 目标 | 熔点比现有低约 **30 ℃** | 使纺粘可直接粘合 TBCW |
| pad 利用率目标 | 尿液分布到整个 pad（约 **400 mm**）而非集中一处 | 去掉 set 才算成功 |

## 关键论断（key_claims）

- **3D 成败的一半在 pattern 设计原则（bond area 等面积），一半在真空容量** —— 支撑页：[[Ultrasonic Bonding of PET-Containing Topsheet]]
- **设备商只做机不做设计：pattern 开发能力必须留在 KC** —— 支撑页：[[Ultrasonic Bonding of PET-Containing Topsheet]]
- **Active Tech 3.0 的极限不是设计而是物理（开关速度 + SAP 下落）** —— 支撑页：[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]
- **平台化的真正缺口是「可交付性」与专职工程资源，不是技术本身** —— 支撑页：[[IPC BCC OI Portfolio（开放创新项目组合）]]
- **分区密度的实现路径是 screen depth（pocket），不只是缩小方块** —— 支撑页：[[分区密度设计]]

## 关联页面

- 概念：[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]、[[Ultrasonic Bonding of PET-Containing Topsheet]]、[[分区密度设计]]、[[Core Channel Pattern（芯体通道花型设计）]]、[[低熔点聚丙烯]]、[[Microencapsulation]]、[[Zeolite Odour Control（沸石除臭载体）]]
- 实体：[[GIC Korea（K-C 韩国 GIC）]]、[[Sabic]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/录音纪要_260903154213.md`
- 原文链接：（无；录音转写稿）

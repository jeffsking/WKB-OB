---
type: source
title: "High Speed Converting Meeting 南京 2026-10-27（COCO V6 成型工艺与设备方向）"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/会议纪要_HighSpeedConverting_20261027.md.md
source_paths:
  - RAW/ima_sync/个人知识库/WKB/会议纪要_HighSpeedConverting_20261027.md.md
  - RAW/ima_sync/个人知识库/WKB/High Speed Converting meeting.pdf.md
  - RAW/ima_sync/个人知识库/WKB/Decisions.pdf.md
  - RAW/ima_sync/个人知识库/WKB/Decisions.md
original_link: ""
date_published: 2026-10-27
date_processed: 2026-10-28
credibility: 中
credibility_note: "三份同场载体合并登记：①中文 v2 纪要（10-27 18:40 修订，仅作要点梳理）；②全程录音逐字转写（ASR，110k 字符，术语与人名需复核）；③英文决议记录 Decisions（19.5k 字符）。数字均来自现场口述，未以测试报告复核，页内标 [待验证]。整页含保密信息（开孔率-密度关系、上下层 SAP 选型、分区设计），KC internal only。"
knowledge_update_status: done
key_claims:
  - "**决策相位已锁定：产品要的是「任意位置、任意 SAP 密度的柔性给料能力」，不是某一款花型** —— 这是把设备规格从「买一台机器」转为「买一种能力」的口径转向，也决定了 HCH 会谈的提问方式（问能力与证据等级，不问花色）"
  - "**保留双层花型 SAM 是业务决策而非技术最优**：单层通道逻辑更简单，但实测更差；机理仅以「双层带来更多 void volume」为假设，**未被证实**（A1）。已与 China 领导团队及市场对齐，不再重开，但团队须准备统一叙事以应对反复质疑"
  - "**11 个尺寸 × 3 种宽度共线是设计第一风险**：不同 OD 改变 nip gap、放大 runout 与热变形（约 150 RPM）；约 11 尺寸对应 8 种鼓规格，收敛手段是「pad 长度做成鼓周长整数分之一」"
  - "**ND33 改造量被判定过大，倾向北京新建独立 pilot 线**：fiberizer、原料通道、真空系统、pulp 上料位均需新增；双鼓 COCO V6 与现有 Blizzard（2 套 SAM hopper）在 ND33 同空间共存**不可能**，旁路 core collector 离线供其他机台**也不可能**"
  - "**真正的商业化卡点是「第二道拉伸（second draw）」，不是密度或速度**；Bryan 现场归纳后要求核实该工艺来源与能否取消"
  - "**高蓬松 Aurelia 的蓬松度收益在成品之前就被卷绕压溃吃掉**：2 mm 厚度样品运抵天津 pilot 线已压扁；Ryan 明确组织内有收卷专家资源，并区分 core winding（近芯层更紧、张力不均）vs surface winding（张力更一致），后者对高蓬松 IEL 可能是关键"
  - "**10/29 HCH 会谈定位为「摸底 + 反向验证」而非技术交底**：只写通用能力要求 + 一个代表性简化产品做验收，不披露开孔率↔密度关系、上下层 SAP 选型、分区规格与 50–260 GSM 密度数据"
  - "**Aurelia 含 SAP 约 62%（对比材料约 24%），颗粒膨胀可能挤占自身 void volume** —— Ryan 要求在第二轮试验回答；验证方法是取「卷芯层 vs 表层」样品分别做成品对比"
pages_linked: ["[[COCO芯体平台]]", "[[Blizzard Core（Blizzard 芯体结构）]]", "[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]", "[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]", "[[SAP错峰膨胀]]", "[[Pilot Retrofit vs Greenfield Decision Framework（改造 vs 新建 pilot 线决策框架）]]"]
compile_mode: semantic
---

# High Speed Converting Meeting（南京）· 2026-10-27

## Positioning 一句话定位

The one meeting where the COCO V6 equipment question stopped being a machine-shopping exercise and became a **capability-procurement and gate-discipline exercise**: decide by mid-November whether ND33 can host two COCO V6 forming drums, and refuse to answer that with vendor narrative.

这场会议把 COCO V6 设备问题从「买一台机器」转成了**买一种能力 + 守一套闸门纪律**：11 月中前判定 ND33 能否容纳双鼓 COCO V6，且拒绝用供应商叙事来回答。

## Meeting Facts 会议事实

| 项 | 内容 |
|---|---|
| 时间 | 2026-10-27（周二）12:58—17:11（约 253 min，议程标注设备讨论 255 min） |
| 地点 | 南京（现场，含实物样品传阅） |
| 主线 | Bryan（战略判定、设计准则、HCH 策略）｜Ryan（材料与收卷）｜Claire（工艺，产品侧）｜Jerry（产品结构，Claire 上级） |
| 其他 | Gavin（工程）、Chris（材料/王总）、Lock 及工程/材料/采购同事 |
| 记录来源 | 全程录音转写（ASR）＋ 英文决议记录《Decisions》＋ 中文 v2 纪要 |

> **三源合并说明（§1.1.1 形态 2）**：中文纪要将该日《Decisions》记为「同日更早一场设备讨论」，但比对议程（Introductions/lunch + COCO V6 equipment discussion 255 min）、起始时刻（12:58）与全部关键数字（70/30、8 mm、11 尺寸、2029/2028、second draw）后判定：**三份文件是同一场会议的三种载体**（逐字转写 / 英文决议记录 / 中文 v2 纪要），故合并为一页，禁建平行页。

## Decisions 已决议（8 条）

| # | 决议 | 状态 |
|---|---|---|
| 1 | 保留双层图案 SAM 结构，并验证 **pressure bonding** 替代超声 bonding | 已定 |
| 2 | 商业化基线维持 **2029**，同时探索 2028 加速（不承诺） | 已定 |
| 3 | 对供应商只提**柔性给料与分区能力**要求，不披露密度对应关系 | 已定 |
| 4 | Phase 1 聚焦 **100% SAP 五层结构**（LSN + SAP1 + REL + SAP2 + PSN），SAP 上下分工、目标 **70/30** 分配（约 30% 高 AUL 置顶层） | 已定 |
| 5 | Phase 2 拟在 PSS 加最小 fluff 层（约 30 GSM / 约 1 g）建立毛细吸收 | 已定 |
| 6 | channel 几何基线：主/侧通道均 **8 mm**，8 mm 中央设 **3 mm 压花**；11 尺寸≈8 种鼓（待工程验证） | 已定（待验证） |
| 7 | **11 月中前**决定「ND33 改造 or 北京机湾新建 pilot 线」 | 已定 |
| 8 | 产品侧向本地市场输出花型设计原则（尺寸要求、主支与分支组合） | 已定 |

### SAP 上下分工（Phase 1 核心）

| 层位 | 功能诉求 | SAP 特性要求 |
|---|---|---|
| 顶层（LSS，skin/line side） | 调节与分配、intake | 高 AUL、高 GBT、**大 PSD** |
| 底层（PSS，polish side） | 快速吸收、抑制凝胶阻塞 | 高 CR、高 Vortex、**较小 PSD** |

> 两侧用同量 SAP = 牺牲吸收量；实际是「底层高 CRC/高克重、顶层高 AUL」的**不等克重**结构，这也是必须上**两套 SAP 给料系统**（并预留第三套给功能颗粒）的根本理由。

## The Five Phases 五阶段路线（Bryan 会前定调）

| Phase | 内容 | 备注 |
|---|---|---|
| 1 | 100% SAM + 成形花型 | 当前唯一优先级 |
| 2 | LSS/PSS 的 add-on 差异化 + 单/双侧 SAM 密度差异化 + 覆盖差异化 | 与 Phase 1 同为重点 |
| 3 | PSS 加入少量 fluff 提升毛细吸收 | **capex 允许则可提前并入** |
| 4 | REL pattern cut（带 trimming handle） | 后续 |
| 5 | PSS = fluff + SAM，双面 pattern，可全球扩展 | 后续 |

## Open Questions 未决不确定点（按责任线）

| # | 不确定点 | 归属 | 为何致命 |
|---|---|---|---|
| A1 | 双层为何优于单层（机理未证实） | 工艺 + 研发测试 | 无法向管理层立论，也无法给供应商提要求 |
| A2 | 必须收敛成「一句话设计原则 + 理论」 | 工艺主笔 | 缺此项则方案无法自证「这是最优设计」 |
| A3 | 开孔率 ↔ SAP 密度的定量对应 | 工艺 + 气路工程 | 「方向成立、数值无数据」，只能靠产线/pilot 试出 |
| A4 | 单层落料气流阻塞能否解（分层筛网 + 沙袋微坑侧向抽真空设想） | 工程 | 单一底部抽真空会被第一层堵死 |
| A5 | 落料角度（45° 仅为假设）与落料间距 | HCH + 现场测量 | 反弹与落料损失无法量化 |
| A6 | 胶黏剂按位置差异化施加（先上胶于 SAP vs 鼓面涂胶引 web handling） | 工程 + 工艺 | 鼓面涂胶上周末试过、清鼓 4 次 |
| A7 | 多规格共线的鼓径与 nip gap | 工程 + HCH | 已判定为**第一风险** |
| B2 | 3 套成型鼓空间不足 → 2 套是否够 | 工程 | HCH 原建议三套以摊薄单鼓 SAP 负载 |
| B3 | 喷嘴是否已有现成产品（目前仅概念） | HCH + 工程 | 追问「这个设想从哪来的」 |
| C1 | 高速连续运行的检测与闭环（7 天 × 4 h 如何控密度/分布/污染/幅面） | 工程 + 质量 | Bryan 定性为关键未知，**与 HCH 面对同一挑战** |
| C2 | 1000 PPM vs 900 PPM 口径 | 产品 + 工程 | 11 月中深入讨论后修正 |
| C3 | 商业化卡点是否仅为 **second draw** | 工艺 | 决定工艺是否可取消 |
| R1 | 高含量 SAP 是否挤占 Aurelia 自身 void volume（Aurelia 含 SAP ~62% vs 对比 ~24%） | 材料 | 直接吃掉蓬松度收益 |
| R2 | 卷绕张力是否已把高蓬松结构压塌 | 材料 + 收卷 | 验证法：卷芯层 vs 表层成品对比 |
| O3 | chamber 内部机理不明（「不知道里面发生什么」） | 工艺 + HCH | 只能靠试验反推 |

## Winding Support 收卷支持（Ryan 承诺，独立行动线）

| 行动 | 内容 | 责任 | 截止 |
|---|---|---|---|
| W1 | 与 Ryan follow up 收卷专家支持的组织形式（内部工时 / 外部服务 / 供应商辅导） | Chris → Ryan | 本周启动 |
| W2 | 收卷方式建议方案（表面卷绕 / box collector / 低张力）与改造代价 | Ryan 专家 + 工程 | 11 月上旬 |
| W3 | 卷芯层 vs 表层对比验证，量化压溃对蓬松度与三次回渗影响 | Chris | 样品到位后 2 周 |
| W4 | 对供应商的收卷工艺要求与验收口径（张力、卷径、包装） | 材料 + 采购 | 待确认 |
| W5 | 设备规格书加入「收卷张力可控 / 支持低张力与表面卷绕」硬性要求 | 工程 | 与 HCH spec 同步 |

> 技术要点：**core winding** 靠近芯层更紧、张力不均；**surface winding** 张力更一致。对常规 IEL 未必需改，**对高蓬松 IEL 很可能关键**。2 mm 样品运抵天津 pilot 线时已被压扁 —— 蓬松度收益在成品前即损耗。

## HCH Pre-Meeting Discipline 10/29 会谈纪律

| 项 | 口径 |
|---|---|
| 定位 | **摸底 + 反向验证，不做技术交底**；最多时间让对方讲，我方给最少信息 |
| 开场 | 先对齐「已披露了什么 / 对方知道什么 / 对方认为我们要什么」 |
| 核心问句 | 「你们如何说服我们这套工艺足够可靠？」＋ IP 安全边界 |
| 已披露 3 项 | ① 11 个尺寸（MD 长 / CD 宽 / 花型形状）；② 必须支持两套 SAP 给料 + 可能第三套（非 SAP 功能颗粒）；③ **一个** channel pattern 尺寸与概念（叶脉结构）；附带可能约 10% 少量 fluff |
| 保密红线 | ① 开孔率 ↔ SAP 密度对应关系；② 密度 / MD 分离 / 尿液积聚分区（含 70/30 分配）；③ 上下层 SAP 选型；④ 筛网开孔设计、分区规格、50–260 GSM 密度数据 |
| spec 颗粒度 | 只写能力项（速度、fluff 给料范围、SAP 给料范围、给料系统数、单 job 上限）＋ 一个代表性简化样品验收，**不写密度分区数值** |

### 必问清单（摘要，完整 16 条见原文 5.4）

1. 单 job 最大 SAP add-on（目标上限 260 GSM）及其对应鼓径/真空/落料高度/接收弧长
2. 11 尺寸 × 3 宽度共线的鼓径选择与 nip gap 控制、150 RPM 下 runout 与热变形
3. pattern-to-pattern 对齐制造精度；高速下 channel 形变与窜 SAP
4. **速度 ↔ SAP 密度 trade-off 曲线**（答不出 = 能力未量化）
5. 筛网方案：有无 3D 筛网 / 侧向抽真空能力（只问能力，不给参数）
6. 静态压力 / 风量（CFM）范围、风机容量与变频能力
7. 落料方式：chamber vs long-shoot 的边界与理想落料角度
8. 证据等级三连问：是否已商业化？做过哪些基础试验？属「已验证 / 开发中 / 未知风险」哪一档？
9. capex 与交期
10. ND33 排布与集成可行性（原料通道、夹层真空可能需两套 osprey、pulp 上料位、90° 走线）
11. **HCH 交付的是设备（pilot line），不是技术支持** —— 工艺开发由我方负责，须书面共识

## Numbers On The Record 现场口述数字（均 [待验证]）

| 指标 | 数值 | 出处 |
|---|---|---|
| strikethrough 提升 | 约 6% | 现场口述，待报告复核 |
| MD 分布提升 | 约 7% | 同上 |
| tri-level liner MD 分布提升 | 约 80% | 同上 |
| Aurelia 含 SAP | 约 62%（对比材料约 24%） | 同上 |
| 蓬松度等效 | 28 GSM ≈ 38 GSM | 同上 |
| 2029 产品量级 | 「约 7,000 products」 | 疑单位误识，未写入结论 |
| 速度 | 2029 起动 1000 PPM，设计留 +20% 余量（≈1200 PPM）；900 PPM 为内部备选 | 产品 + 工程口径 |

## Linked Pages 关联页面

- 概念：[[COCO芯体平台]]、[[Blizzard Core（Blizzard 芯体结构）]]、[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]、[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]、[[SAP错峰膨胀]]
- 框架：[[Pilot Retrofit vs Greenfield Decision Framework（改造 vs 新建 pilot 线决策框架）]]
- 同批文件：[[ND33 改造可行性评估·推进计划（20261028）]]、[[Gate 0 基线口径确认书（ND33-COCOV6-G0-001）]]、[[Key point for COCO V6 engineering plan（Bryan 五阶段路线）]]

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/会议纪要_HighSpeedConverting_20261027.md.md`（+ 同场 `High Speed Converting meeting.pdf.md`、`Decisions.pdf.md`、`Decisions.md`）
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/attachments/`

## Merge Record 并入记录（2026-10-30）

| 载体 | media 形态 | 验证方式 | 结论 |
|---|---|---|---|
| `Decisions.pdf.md`（10-28 入库） | PDF 文字层 | 与笔记版逐词 difflib = **0.894**（去空白后 0.819） | 同一文档：差异仅 PDF 连字（ﬂ/ﬁ）与笔记版丢失词间空格，正文内容一致 |
| `Decisions.md`（10-30 补齐正文） | IMA 笔记（note）的 REST `get_doc_content` 版 | 首段逐字相同（`Retain two patterned SAM layers and evaluate pressure bonding…`） | **同一文档的第二载体** → 并入本页 `source_paths`，未建平行页 |
| `High Speed Converting meeting ....md` | IMA 笔记版，正文仍卡 REST 日配额 | 标题与既有 `High Speed Converting meeting.pdf.md` 同源（117,675 B 已入库） | 待正文到手后按同规则并入，**不单独建页** |

> **锚点状态**：三条 note 载体在 `RAW/` 侧均无实体文件（插件自 2026-10-20 起零落盘），`source_path` 为预期路径；正文仅存 `RAW_FULL/` 镜像。按 AGENTS §1.1.5 保持 RAW 预期锚点，不改为 RAW_FULL、不批量迁移。

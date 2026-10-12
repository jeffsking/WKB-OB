---
type: source
title: "Online Core Competition & COCO V6 Strategy Workshop（在线新品竞争与策略）"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/在线新品竞争与策略.md
original_link: ""
date_published: 2026（推测，月份 [待验证]）
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "在线复合芯体已进入「竞速」阶段，各玩家优势在缩小；趋势关键词是 pattern + channel + zoning 的组合式设计，价值落点在干爽、快导流与芯体利用率"
  - "实测口径：平板注液 170 mL 时芯体利用率 65–70%；U 型注液 255 mL 时约 50%；而 L 号实际使用（2–3 h、50–70 mL 尿液）真实利用率仅 30–40%——一片 12 g SAP 中约 7 g 用不到"
  - "COCO V6 的 slogan「让每一颗 SAP 皆有其用」，成功标准聚焦三条：传导/扩散、U 型下的 intake 与 cradle 表现、贴近实际使用的性能；对标基准为 5.6 X（已在 top 水平）"
  - "Channel 设计八条：中间贯穿槽 + bonding；bonding 过宽会伤害 U 型扩散（由 6 mm 收窄到 3 mm 可缓解）；横向槽助 cradle；槽不贯通、不超出 pad 边缘；哑铃形（中间窄两头宽）提升中心 SAP density"
  - "FOCUS 工程实验：chamber 成型优于 OEM 的 shift 方式；约 20+ 的真空可支持 1,200 ppm；SAP 约 190 GSM 时分布最好且 CV 优秀，超过后 CV 明显漂移"
  - "施胶方式（spiral / summit vs signature）对 free SAP 与 pad integrity 影响极大，signature 改 summit 后明显改善；胶量可由 10+ 降到单层约 6 GSM"
  - "工程约束：车速不降低（目标约 450 m/min，挑战 500–520 m/min）；pattern 越复杂，ND/CD registration 与 air-knife on/off 频率风险越大；圆弧形可成型、尖角形不可"
pages_linked: ["[[COCO芯体平台]]", "[[Core Channel Pattern（芯体通道花型设计）]]", "[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]", "[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]"]
---

# Online Core Competition & COCO V6 Strategy Workshop（在线新品竞争与策略）

> 本页为 ASR 转写稿（soundrecording）的编译产物。转写讹字极多（如「星体/芯体」「三/SAP」「方面/bonding」「恒仓/恒昌」「iPad 泰/HCH」等）。凡无法确证者一律标 `[待验证]`；**竞品名称与工艺细节只记可辨识要点，不做推断性补全**。

## Attendees / Date 参会与日期

| 项目 | 内容 |
|---|---|
| Date 会议日期 | `[待验证]` —— 原文无日期字段；正文提及「今年是 2026 年」「天津四月份刚建离线复合芯体机」「基于二七年的 forecast」「今年三月份南京展会」，故为 **2026 年**（月份待验证） |
| Attendees 参会 | `[待验证]` —— 转写中出现：李想（主持与主题分享）、杰瑞（Jerry，研发/产品设计）、腾哥（OI 侧，工艺平台）、Gavin（盖文，SAP loading 与实验数据）、凯文（MPC 工程部，FOCUS 实验）、婷婷、浩哥、炮哥、廖总、戴老板、菲比、波哥、Michelle。原文未署名，**不作实体页依据** |
| Format 形式 | 全天 workshop：上午竞品与策略 + 工艺平台 + 工程实验（FOCUS），下午 knowledge gap 讨论（按「决策影响性 × 确定性」排 P1/P2 优先级）；含破冰游戏环节（与本库主题无关，不页面化） |

## 一句话定位

一次把**竞品在线芯体创新扫描、COCO V6 的成功标准与 channel 设计规则、以及「真空成型 + 多成型鼓」工艺平台的工程可行性**串起来的全天 workshop；产出是 V6 的设计方向与一列待验证的 knowledge gap，而非最终方案。

## Key decisions 决策要点

> 只记会上明确「定了 / 就这么做」的事项。

1. **COCO V6 的目标与 slogan 定案**：**「让每一颗 SAP 皆有其用」** —— 通过提升芯体利用率，要么放大性能优势，要么拿掉无用材料获得成本节约。
2. **成功标准聚焦三条**：① 平板与 U 型下的**传导与扩散**；② **intake time**（尤其是 U 型下 cradle time 与国标吸收时间）；③ 更贴近实际使用的性能表现。**对标基准为 5.6 X**（已在市场 top 水平），要求在基准上再大幅抬升。
3. **Channel 设计规则（本轮实验结论，作为 V6 设计指导）**：
   - 设**中间贯穿性中心导流槽**，以覆盖不同尿点、加快高压下 intake 与扩散；
   - 导流槽**必须加 bonding**（否则湿态下被 SAP 膨胀抹平、丧失导流作用），且 bonding 能进一步提升高压吸收；
   - **bonding 宽度要做窄**：过宽（超声 bonding）会伤害 U 型下扩散（推测因超声破坏内层纺粘纤维、影响毛细传导），由约 6 mm 收到 3 mm 后影响降低，后续继续试更窄；
   - 加**横向导流槽**以促进 cradle 下水、加速 cradle intake；
   - 横向导流槽**不得超出 pad 边缘**，需预留数毫米；
   - 导流槽**不能贯通**（贯通会让液体过度扩散到前后端 → 前后漏）；
   - 采用**哑铃形（中间窄、两头宽）**：两头宽扩大 coverage（前趴/后躺防漏），中间窄提升中心区 SAP density；**代价是材料用量上升，需做成本与性能平衡**。
4. **REL cutting 暂不作为必做项**：本轮实验设备不具备能力，产品收益尚未评估出显著提升，**暂列 option**（长期若平台搭建完成可再做）。
5. **车速不降低是硬约束**：目标车速即每条产线的既有目标（会上一口径约 **450 m/min**），挑战 **1,200 ppm（约 500–520 m/min）**。
6. **FOCUS 工程实验的可用性结论**：在基材（substrate）上以受控均匀真空成型的工艺（forming on the substrate）**是可尝试的方向**，可作为 V6 的候选工艺路径之一。

## Open issues 待决问题

- **U 型下的扩散尚未解决**：channel 属于「物理槽」，液体**不能靠物理槽反重力爬升**，U 型扩散更多要靠**材料的毛细作用**（这也解释了为什么行业克重越来越高）→ 属第二轮材料组合的攻关方向。
- **高速下的工艺未知项**：① SAP **克重漂移**在 400/450/500 m/min 下各是多少未知；② 圆形大盘承接 SAP（不同于现有皮带平行兜住）时，**free SAP 比例在高速下的波动未知**；③ **单一成型鼓在高速下最大能 hold 住多少 SAP 添加量**待定。
- **SAP 用量目标与现实的差距**：L 号现用约 15 g，目标压到 **12 g 以下**；但极端码（4XL）若按 LSS/PS = 7:3，PS 上可能要到 **18–20 g 的 70%** → 工艺极限待定。
- **成型鼓数量与 SAP 分区**：两个/三个成型鼓怎么布置、产线权限如何，未定；HCH 的 proposal 为在主机两个成型鼓基础上控制在约 4 米空间内，需工程团队复核。
- **pattern 复杂度 vs 工艺可行性**：pattern 越复杂，① ND/CD 方向的 **registration** 挑战越大；② air-knife 的 on/off 频率（如 6 次 on/off × 800 片）与 **SAP 流尾、solar valve / 气吹频率**能否匹配 —— **待验证**。
- **形状可成型的边界**：鼓上 3D 打印样件试验表明——**圆弧形可做**；**尖角/非常尖锐的形状做不到**（尖角处 SAP 分布不均）。圆润角要做到约 2 mm 级才漂亮，而圆润角又影响毛细反重力爬坡 → 需权衡。
- **施胶与胶量**：胶量已可由 10+ 降到单层约 6 GSM（双层 12 GSM），但**「胶喷在布上还是 SAP 上」「spiral 小螺旋 vs summit vs signature」**对 free SAP 影响极大；最佳组合**未定**，需继续实验。
- **胶枪布置的清洗难题**：若把胶枪放进（成型鼓）腔道内，如何清洗、如何避免回护/污染 → 未解。
- **SAP 与 fluff 在 PS 上混配**：PS 上混少量 fluff（如 90 SAP / 10 fluff）以提升反重力爬坡，**混合均匀性从未验证** → 下午重点讨论项。
- **长期运行风险未评估**：若采用真空成型路线，长期运行的**污染与磨损**情况未看过。
- **可重复性与稳定性**：FOCUS 实验明确**未做 R（重复性）**，且非 performance/qualify 实验，结论只作工程方向参考。
- **竞品对标的两条外部线索待查**：① 马来西亚某产品（代工生产）采用 IE 切割 + 小鼓两次铺粉 + screen 上 X-bar 形成 X forming；② 美国 active park 的两个方向（把 channel 变小 + 气吹/电磁控制）最新进展未知。

## Action items 行动项

| Task 任务 | Owner 负责人 | Due 截止 | Status 状态 |
|---|---|---|---|
| 第二轮实验：不同材料组合（提升毛细/反重力爬坡） | 研发（腾哥侧已开发多种材料） | 未指定 | 待启动 |
| 继续做窄 bonding 宽度（3 mm 以下）验证 U 型扩散是否回升 | `[待验证]` | 未指定 | 待启动 |
| 验证哑铃形（中心收窄）在大汕尾防漏测试上是否真有 benefit，再决定是否细化设计 | `[待验证]` | 未指定 | 待启动 |
| 准备第二次 FOCUS 实验：用普通 REL 试更高 SAP loading（190 → 250/300 GSM） | MPC 工程部（凯文侧） | 未指定（受产能排期影响） | 待启动 |
| 按「决策影响性 × 确定性」把 knowledge gap 排入 P1/P2，下午逐条讨论 | 组委会 + Jerry + 厚哥/浩哥 | 当日 | 进行中 |
| 与各产线核对芯体部位的目标车速，作为「高速」的明确定义 | `[待验证]` | 未指定 | 待启动 |
| 复核 HCH 的成型鼓 + 真空平台 proposal（空间约 4 m）是否合理 | 工程团队 | 未指定 | 待启动 |
| marketing 在 IPS 关键时间段引入设计（5.5T6 / 6.5T 高端线落地，配合概念做 device 升级） | marketing | IPS 关键时间段 | 待启动 |
| 查证马来西亚代工产品工艺与美国 active park 最新进展 | `[待验证]` | 未指定 | 待启动 |

## Background 背景

在线复合芯体（online composite core）已成行业主流，各头部玩家围绕 pattern / channel / zoning 做组合式创新，先发优势正在收敛；同时实测显示产品在实际使用条件下 SAP 利用率仅 30–40%，大量材料被浪费。COCO V6 即在此背景下启动，目标是同时拿到性能优势与成本空间。

## 提炼的数字与结论

| 项目 | 数值 / 结论 | 备注 |
|---|---|---|
| 平板（F）利用率 | 注液 170 mL → 利用率 **65–70%** | 平板测试口径 |
| U 型利用率 | 注液 255 mL → 利用率约 **50%** | 模拟最极端情况 |
| 实际使用利用率 | L 号 2–3 h、尿液 50–70 mL → 真实利用率 **30–40%** | 一片 12 g SAP 中约 **7 g** 用不到 |
| 成本节约估算 | 仅 T6+ 产品、基于 2027 forecast 约 **3.6 M USD**，平摊约 **20+ 元/SU** | 初步估算 `[待验证]` |
| SAP 成型量 | 约 **190 GSM**（对应约 6 g）时分布、channel 强度与手感最好 | CV 优秀；超过 190 GSM 后 CV 明显漂移 |
| 真空条件 | 约 **20+**（单位 `[待验证]`）的真空可支持 **1,200 ppm** | 约 200 GSM 量可行 |
| 胶量 | 由 10+ GSM 降到单层约 **6 GSM**（双层 6+6=12 GSM） | 与印尼一层 6 GSM 量级相当 |
| 目标车速 | 约 **450 m/min**（各线目标车速不降低），挑战 **1,200 ppm ≈ 500–520 m/min** | 芯体部位线速因线而异（约 420–450） |
| 开槽宽度 | 8 mm / 10 mm 设置；bonding 由约 6 mm 收到 3 mm | 需匹配工艺难度 |
| SAP 用量目标 | L 号由约 15 g 压到 **12 g 以下** | 极端码可能 18–20 g |
| 平台空间 | HCH proposal：主机两成型鼓基础上控制在约 **4 m** 内 | 需工程复核 |

> 🔴 **manual_review（2026-09-29）**：本资料含**成本节约金额（3.6 M USD、约 20+ 元/SU）、2027 forecast 口径、竞品工艺情报、供应商/设备商（HCH、恒昌、OEM 代工方）的 proposal 与产能排期**，属商务敏感信息（AGENTS.md §5）。本页只记**量级与工程要点**，**不落完整成本模型与商务条款**；原文留存于 `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/在线新品竞争与策略.md`。

## 关键论断（key_claims）

- **真正的浪费不是性能差，而是 SAP 用不到（真实利用率仅 30–40%）** —— 支撑页：[[COCO芯体平台]]
- **channel 是「物理槽」，解决不了 U 型反重力扩散，那一半要靠材料毛细** —— 支撑页：[[Core Channel Pattern（芯体通道花型设计）]]
- **bonding 是把双刃剑：保住湿态 channel，却伤害 U 型毛细传导，故必须做窄** —— 支撑页：[[Core Channel Pattern（芯体通道花型设计）]]
- **真空成型（chamber + vacuum）工艺的可行性已被工程实验支持，但高速稳定性与磨损是未验证项** —— 支撑页：[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]
- **胶的「喷法」比「胶量」更决定 free SAP 与 pad integrity** —— 支撑页：[[Polyolefin Hot Melt Adhesive（聚烯烃热熔胶）]]

## 关联页面

- 概念：[[COCO芯体平台]]、[[Core Channel Pattern（芯体通道花型设计）]]、[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]、[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]、[[Blizzard Core（Blizzard 芯体结构）]]、[[分区密度设计]]、[[Gel Blocking（凝胶阻塞）]]、[[Cradle Intake Test（Cradle 摄入测试）]]
- 实体：（本批不新建实体页；竞品名称因 ASR 讹字仅作要点记录）

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/在线新品竞争与策略.md`
- 原文链接：（无；录音转写稿）

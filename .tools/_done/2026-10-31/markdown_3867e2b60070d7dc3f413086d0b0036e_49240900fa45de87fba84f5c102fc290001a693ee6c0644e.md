---
type: source
title: "PEG-Based Slot-Die Emulsion for Visual Cue Layer（可视化功能层复配乳液方案集 · 2026-10-30）"
source_type: 研报
source_path: RAW/ima_sync/个人知识库/WKB/纸尿裤可视化功能层_PEG基slot_die复配乳液技术方案_20261030.md.md
source_paths:
  - RAW/ima_sync/个人知识库/WKB/纸尿裤可视化功能层_PEG基slot_die复配乳液技术方案_20261030.md.md
  - RAW/ima_sync/个人知识库/WKB/Knight_IV_PEG基slot_die复配乳液技术方案_20261030.md.md
original_link: ""
date_published: 2026-10-30
date_processed: 2026-10-31
credibility: 中
credibility_note: "自著技术方案集（桌面研究 + 工程推理），明标「非实测结论」；文献类判据标 [L]、工程经验标 [E]、推断标 [I]、已验证标 [F]。页内数值均取自原文，未做二次外推。含供应商实名与成本区间 → 本页只记要点与量级，不落完整报价表。"
knowledge_update_status: done
key_claims:
  - "**「上浆量不足」与「成本过高」不是两个问题，而是同一个架构错误的两次表现**：把「视觉所需的光学量」与「功效所需的活性量」用同一种高价材料在同一区域同时实现；解法是**解耦**（功能分层、分区承担）"
  - "**三阈值模型是整个方案的判据骨架**：W* 润湿阈值 0.1–0.3 gsm（表活吸附覆盖度）、O* 光学阈值 0.8–2.0 gsm（ΔE*ab ≥ 6）、F* 功能阈值 0.05–0.4 gsm 提取物 —— 高速产线失败的真实原因是「只满足了 W*，没满足 O*」"
  - "**狭缝涂布（slot die）是预计量工艺，正对着这个问题**：湿膜厚 = 流量 ÷ 车速，不受网穴容积封顶；丝网/网纹辊是自计量工艺，其转移量被物理封顶，调粘度/换辊/加深网纹辊全部无效"
  - "**极性必须早定，推荐主线 B（疏水基布 + 亲水 PEG 图案）**：PEG 水溶 → 遇液溶解释放活性物，转移率显著优于不溶拒水膜；极性 A 的连续拒水膜本身就是活性物向皮肤水相转移的物理障碍"
  - "**温度上限的真实约束是「≤65 °C 物料温度 + 线速 ≥250 m/min」，S2 热熔路线从物理上绕开它**：PEG1000/1500 熔体 58–62 °C 施胶、冷却辊固化、无干燥段；代价是 ±2 °C 施胶窗（全方案最脆一环）"
  - "**材料成本在纸尿裤尺度上不是瓶颈**：干基 ¥130–300/kg → ¥0.15–0.50/m² → 婴儿面层 ¥0.005–0.013/件；主导成本是良率、换型与 OEE"
  - "**最大风险不是干燥，而是货架期干膜降解**：文献明确干粉中烷酰胺 25/40 °C 存放 7 个月即显著下降（Ea ≈ 101 kJ/mol），比干燥过程危险得多 → 8 周加速验证必须前置"
  - "**PEG 占固含 60% 是硬性上界**：超上限必然吸湿发黏与货架期问题；用 PVP K30 替代部分 PEG 提供成膜与黏度，是压住占比而不牺牲覆盖率的关键手法"
pages_linked: ["[[Hot-Melt Slot Coating（热熔狭缝涂布）]]", "[[湿感指示条 Wetness Indicator]]", "[[Light-Scattering Masking Wetness Indicator（光散射遮蔽型尿湿指示）]]", "[[亲水化 Hydrophilisation]]", "[[会议纪要 Knight IV]]", "[[为什么纯 PEG 不能常规熔纺]]"]
compile_mode: semantic
---

# PEG-Based Slot-Die Emulsion for Visual Cue Layer（可视化功能层复配乳液方案集 · 2026-10-30）

## Positioning 一句话定位

A 7-option engineering proposal set that reframes a twice-rejected visual-cue coating programme (insufficient add-on, then excessive cost) as **one architecture error rather than two technical failures**, and prescribes decoupling the optical load from the active-ingredient load across three independent thresholds.

一份 7 方案技术方案集：把已被否决两次的可视化涂层项目（先「上浆量不足」、后「成本过高」）重构成**同一个架构错误的两次表现**，并给出「光学量 / 活性量」解耦 + 三阈值判定 + 分区承担的工程路线。

> ⚠ **性质声明**：原文自标「桌面研究 + 工程推理，非实测结论」。本页所有数值为**原文设计目标值**，非产线实测值；`[E]` 工程经验、`[L]` 文献、`[I]` 推断、`[F]` 已验证均沿用原文标注。

## Source Facts 来源事实

| 项 | 内容 |
|---|---|
| 主件 | 《纸尿裤亲水/拒水可视化功能层 × PEG 基狭缝涂布复配乳液技术方案》v1.1 · 55,223 字符 · 11 章 + 供应商甄选 |
| 次件（并入） | 《Knight IV · Visual Cue 可视化 × PEG 基 slot die 复配乳液技术方案集》v1.0 · 30,090 字符 · 同一骨架的项目定制版（去掉 §10 供应商甄选，阈值表述压缩为「双阈值」，成本区间 ¥0.17–0.44/m²） |
| 同源性判定 | 两件目录骨架逐节一致（§0–§9 同名同序）、同日同著者 → **同一文档的两个版本**，按 §1.1.4 以内容最全的 v1.1 为主件、v1.0 并入 `source_paths`，**未建平行页** |
| 载体 | IMA 知识库 markdown 原件直下（`get_media_info`，不吃 REST 配额） |

## Summary 摘要

The proposal's central move is to stop treating "add-on too low" and "cost too high" as separate defects. Both descend from loading a single expensive ingredient with two physically unrelated jobs: making the wetness cue visible (an optics problem — surface energy and light scattering) and delivering an active dose to skin (a chemistry problem — molecular dose). Because a screen or gravure roll is a **self-metering** process whose transfer volume is physically capped, the optics threshold was never reachable in production; and because the expensive extract was dosed at the *optical* rate, cost exploded on the second attempt. Slot die is a **pre-metered** process (wet film = flow ÷ line speed) and therefore the correct tool — but only if the active ingredient is moved out of the optical layer.

方案的核心动作是停止把「上浆量不足」和「成本过高」当作两个独立缺陷。二者的共同来源是：让同一种高价材料同时承担两件物理上无关的事 —— 让 cue 可见（光学问题：表面能 + 光散射）与把活性物送到皮肤（化学问题：分子剂量）。丝网/网纹辊是**自计量**工艺，转移量被物理封顶，因此 O* 在产线上从未被满足；而第二次否决时提取物是按 **O\* 的量**加的，成本必然爆。狭缝涂布是**预计量**工艺（湿膜厚 = 流量 ÷ 车速），是正确工具 —— 但前提是把活性物移出光学层。

The quantitative consequence is stated plainly: if O* needs 1.6 gsm and the extract sits at 4% of the formula, every square metre carries 0.064 gsm of extract; put 12% only in the outermost 0.3 gsm instead and 0.036 gsm suffices — **44% less extract for identical optics**.

量化后果写得很直白：若 O\* 需 1.6 gsm、提取物占配方 4%，每平米需 0.064 gsm；改为只在最外层 0.3 gsm 里放 12%，仅需 0.036 gsm —— **提取物省 44%，光学效果一点没少**。

## The Three-Threshold Model 三阈值模型

| 阈值 | 物理判据 | 由什么决定 | 典型量级 | 未达成后果 |
|---|---|---|---|---|
| **W\* 润湿阈值** | 涂区接触角 → 0，液体自发铺展 | 表活在纤维表面的吸附覆盖度 | 0.1–0.3 gsm `[E]` | 湿润斑驳、图案边缘毛糙、「有时有有时没有」 |
| **O\* 光学阈值** | 干/湿态光散射差可辨，ΔE*ab ≥ 6 | 涂层连续性 + 水膜厚度 + 毛孔填充率 | 0.8–2.0 gsm `[E]` | 图案「淡、虚、看不见」 |
| **F\* 功能阈值** | 皮肤转移量达最低起效量 | 提取物载量 ÷ 转移率（同类约 2% `[I]`） | 0.05–0.4 gsm 提取物 `[E]` | 有 cue 无功效 |

**关键推论 Key corollary**：产线失败 = 只满足 W\*、没满足 O\*。自计量工艺的最大转移量被网穴容积封顶，深度做到极限仍不够 → 必须换预计量工艺。

## Polarity 极性问题（必须先定方向）

| 极性 | 结构 | 干态 | 湿态 | 优势 | 劣势 |
|---|---|---|---|---|---|
| **A（现行路线）** | 亲水/弱亲水基布 + 拒水图案 | 不可见 | 图案区拒水保持白浊 → **白图浮现于深底** | 视觉反差最大、机制简单；已在 SMS 基布验证 `[F]` | 拒水膜需连续 → 上浆量 1.5–3.5 gsm；**拒水膜同时阻断活性物向皮肤的水相转移** |
| **B（推荐主线）** | 疏水基布 + 亲水 PEG 图案 | 不可见 | 图案区导液透明 → **深图浮现于白底** | 亲水体系天然承载水溶性提取物；PEG 遇液溶解释放，转移率显著优于不溶膜 | 对基布表面能要求高；须把 σ 压到 ≤26 mN/m |
| **C（兜底）** | 图案区拒水（纯视觉）+ 空白区亲水载活性物 | 不可见 | 图案浮现 | 视觉与递送互不干扰，各自最优 | 两道工序或双腔模头 → OEE 成本上升 |

**被低估的降本杠杆**：PP 表面能约 29–31 mN/m，而 PEG 水溶液 σ ≈ 43–45 mN/m —— 即便加了 PEG 也压不到 PP 之下，这才是「配方必须配弱亲水基布」的真正原因（不是配方挑基布，是表面张力不够低）。把动态 σ 压到 **≤26 mN/m** 即可直接在标准疏水 PP 上涂布，基布选择自由度与成本结构同时改变。

## Option Set 方案集与优先级

| 方案 | 一句话 | 优先级 |
|---|---|---|
| **S1** | PEG 水基高固含微乳 + 分区垫片：一条配方一道工序，PEG 兼做增溶剂/保湿剂/成膜骨架，用分区垫片把亲水图案「印」在疏水基布上（固含 ≈34%，干基成本 ≈¥150/kg，上浆 1.2–2.0 gsm） | **P0-b**（主线，第 2–8 周） |
| **S2** | PEG 热熔「无水面」：PEG1500/1000/400 三元熔体 58–62 °C 施胶、冷却辊固化，**没有干燥段**，温度上限约束物理上不存在（固含 100%，干基 ≈¥100/kg） | **P1**（战略价值最高，第 6–14 周） |
| **S3** | 双层解耦：PEG 光学骨架 + 活性薄层（湿压湿）—— 若 S1 提取物成本不过关，这是**唯一能砍掉 44% 提取物用量**的路线 | **P0-c**（与 S1 并行，第 4–10 周） |
| **S4** | 极性 A 改良：PEG 酯改性拒水层 + 活性物分区，延续已验证视觉效果 | **P0-a**（快速验证件，2–4 周，非最终方案） |
| **S5** | 「干白湿透」光学开关（多孔散射体 + PEG），不依赖基布极性 | P2（仅当「干态绝对不可见」成硬要求） |
| **S6** | PEG 隔离层「三物质」水显 + 提取物共载（染料路线） | P3（与「天然/植物提取物」宣称冲突，暂缓） |
| **S7** | 增强模块：环糊精包合 + 抗氧化网络，可叠加于 S1–S5 | P2（模块而非方案，随主线做正交试验） |

**排序逻辑不是「性能最好」，而是「单位时间能消除多少不确定性」**：① 先证明 slot die 到底能不能带上量（两次否决的共同根因，且最便宜可验证）→ ② 再证明 65 °C 能否保住活性（决定水基 vs 热熔路线分野）→ ③ 最后才优化成本与图案精细度。

### 决策门 Decision gates

| 门 | 时点 | 判据 |
|---|---|---|
| **D1** | 第 1–4 周（S4 快速验证） | 干基 ≥2.0 gsm 时，湿态 ΔE ≥6 且图案连续 → 通过 |
| **D2** | 第 2–8 周（S1 DOE：PEG400 10/16/22 × 表活 0.8/1.5/2.2 × 上浆 1.0/1.6/2.4） | 干态 ΔE <2 且湿态 ΔE ≥6 且 8 h cue 保持 → 通过 |
| **D3** | 第 6–14 周（S2 台架→中试） | 熔体停留 2 h 后烷酰胺保留率 ≥90% → 通过 |

## Slot-Die Hard Constraints 狭缝涂布通用硬约束

| 约束 | 数值 / 规则 | 常被忽略的后果 |
|---|---|---|
| 垫片厚度 | **≥ 10 × d90** → 200 µm 垫片对应 d90 ≤ 20 µm | 配方阶段最易忽略的一条 |
| 压降 | ∝ 1/t³：垫片减半 → 模头压力 ×8 | 超 40 bar 上限即无法上机 |
| 分区比值 | 用**台面长度**做进金属（Q ∝ 1/L，机加工 ±0.05 mm，寿命内优于 1%）；绝对量只用**泵速**一个变量 | 用泵速调比值会在换型时漂移 |
| 高速（400 m/min 级） | 必须**接触（刮涂）式喷嘴** + 冷却背辊；自由间隙方案因幅材抖动 ±150 µm 不可行 | 非接触方案在高速下条纹不可控 |
| 流变规范 | 必须写 **Cross 指数 n 与松弛时间 λ**；只写 Brookfield 黏度会漏掉条纹与边缘溢流成因 | 黏度单值无法预测涂布窗口 |
| 接触压 | 0.5–1.5 N/cm | 再高压入蓬松层造成透背、手感变硬 |

## Risk Register 风险清单（要点）

| # | 风险 | 等级 | 关键事实 | 缓解 |
|---|---|---|---|---|
| R1 | 温度上限与线速冲突 | 高 | ≤65 °C + ≥250 m/min → 干燥长度需 4–7 m | 蒸发冷却 + 分段控温 + 末段降温；S2 从物理上绕开 |
| R2 | 多孔基材过度渗透 | 高 | 接触压过高 → 透背 | 接触压 0.5–1.5 N/cm；提高低剪切黏度；选平整薄型基布 |
| **R3** | **货架期干膜降解** | **高** | 干粉中烷酰胺 25/40 °C 存放 7 个月即显著下降 `[L]`，**比干燥过程危险得多** | PEG 降 aw + 抗氧网络 + 螯合 + 避光包装 + **8 周加速验证前置** |
| R4 | PEG 吸湿发黏/迁移 | 中高 | PEG 占固含 >60% 时明显 | **硬性上限 60%**；优先 PEG600/1000；PEG-8 酯化降吸湿 |
| R5 | 提取物批次波动 | 中高 | 天然原料批间差异大 | 以总黄酮/总生物碱/菊粉为验收指标，按「活性含量」配料 |
| R6 | 配方储存稳定性 | 中高 | 水性多组分 1 个月量级胀气/沉淀；pH 4 + 碳酸盐放气 | **禁碳酸钙**；现配现用 ≤24 h；小批量高频供应 |
| R7 | 蓬松基布无效 | 中高 | 证据一致：蓬松热风布效果差 | 产品定义阶段锁定平整薄型基布；必要时改走 S5 |
| R8 | σ 压不到 26 mN/m | 中 | 需低动态 σ 表活且不牺牲干态白度与皮肤安全 | 筛 3–4 支（炔二醇 / 硅氧烷改性 / 无氟磷酸酯），动态 σ 与迁移双筛 |
| R10 | 监管口径 | 中 | 功效依赖渗入角质层以下 → 是否仍按一次性卫生用品监管 | 法规前置；宣称避开 restore/protect/treat/heal 类动词 |

## Open Decisions 待对齐决策点

| # | 问题 | 为什么必须现在定 | 建议 |
|---|---|---|---|
| **Q1** | 极性走 A 还是 B | 决定配方、基布、工序、成本的全部下游 | 走 **B**，用 S4 做兜底对照 |
| **Q2** | 「干态不可见」是硬要求吗 | 若可接受干态弱可见，S2 立刻变最优（无干燥 + 成本最低）；若是硬要求，S2 需加填料并降上浆量 | 与市场端明确，建议把「干态 ΔE < 2」写进规格 |
| **Q3** | 活性保全的判据是什么 | 以菊粉为准 → 上限可放宽（耐热 >150 °C）；以整体功效为准 → 上限成立 | 先按 ≤65 °C 设计，用**物料温度曲线**而非空气温度做判据 |

## Cost Envelope 成本量级

| 层级 | 数值 | 备注 |
|---|---|---|
| 干基配方成本 | ¥130–300/kg | 主件口径；S1 ≈¥150/kg、S2 ≈¥100/kg |
| 单位面积 | ¥0.15–0.50/m²（v1.0 版 ¥0.17–0.44/m²） | ±40% |
| 折算婴儿面层 | ¥0.005–0.013/件 | **材料成本非瓶颈** |
| 主导成本 | 良率、换型、OEE | 参照 BM 指示器模型：OEE 让渡 US$0.240/千片 vs 染料 US$0.02/千片，差 12 倍 |

## 关联页面

- 概念：[[Hot-Melt Slot Coating（热熔狭缝涂布）]] · [[湿感指示条 Wetness Indicator]] · [[Light-Scattering Masking Wetness Indicator（光散射遮蔽型尿湿指示）]] · [[亲水化 Hydrophilisation]] · [[为什么纯 PEG 不能常规熔纺]]
- 项目页：[[会议纪要 Knight IV]]

## 原文 Anchors 锚点状态

- 主件路径：`RAW/ima_sync/个人知识库/WKB/纸尿裤可视化功能层_PEG基slot_die复配乳液技术方案_20261030.md.md`
- 次件路径：`RAW/ima_sync/个人知识库/WKB/Knight_IV_PEG基slot_die复配乳液技术方案_20261030.md.md`
- **锚点状态**：两条 `RAW/` 侧文件均为**预期路径**（IMA 插件自 2026-10-20 起零落盘），正文已落 `RAW_FULL/` 同相对路径镜像；待插件落盘后自愈，**不得据缺失建重复页**。

---

## 附录 A：版本并入记录

| 项 | 内容 |
|---|---|
| 并入日期 | 2026-10-31 |
| 主件 | v1.1《纸尿裤亲水/拒水可视化功能层 × PEG 基狭缝涂布复配乳液技术方案》(55,223 字符) |
| 并入件 | v1.0《Knight IV · Visual Cue 可视化 × PEG 基 slot die 复配乳液技术方案集》(30,090 字符) |
| 同源证据 | 逐节骨架一致（§0–§9 同名同序）+ 同日 + 同著者；difflib raw 0.597 / 去空白 0.674（差异来自 v1.0 删 §10 供应商甄选、压缩阈值表述、成本区间微调）→ 判为同文档两版本，非两篇资料 |
| 处理 | 一页 `source_paths` 双登记（AGENTS §1.1.1 形态 2），**未建平行页**；v1.0 差异要点已吸收进本页 Source Facts 与 Cost 行 |

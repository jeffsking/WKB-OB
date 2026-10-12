---
type: source
title: GRIFFIN Female DPU2 AT Hybrid Rewet Summary（女性 DPU2 AT Hybrid 回渗总结）
source_type: 项目汇报 PPT（GRIFFIN 回渗项目 · 实验室回渗数据统计与材料清单）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/GRIFFIN - Female DPU2 AT Hybrid Rewet Summary.pptx.md
original_link: ""
date_published: "未标注（补充 GADT 结果在研究放行后约 2.5–3 个月；Female HUT 结果预计 mid-Feb）"
date_processed: 2026-09-29
credibility: 中高——K-C 内部项目汇报，含完整统计数据（Connecting Letters Report、95% CI、Std Error）与材料牌号；但缺日期、样本量与测试条件说明
knowledge_update_status: done
key_claims:
  - "第一轮对比（550 g / 450 g 加载，Closed Cradle 回渗）：AT Fluffless VONN（带 surge，550 g）最差 0.39750 g；AT Fluffless dSB 0.32250 g；AT Hybrid dSB 550 g 0.30750 g；AT Fluffless TABCW 550 g 0.28750 g；AT Hybrid dSB 450 g 0.28000 g；SAM/Fluff Control 最好 0.23000 g（Std Error 均为 0.02407）。"
  - "AT Fluffless VONN（不带 surge）因摄入时间过高被排除，其回渗为 0.17 g。"
  - "AT 系（ActivTech）代码普遍差于 SAM/Fluff 对照；AT Hybrid dSB 550 g 平均比对照高 0.07 g，但 95% CI 下不显著。"
  - "第二轮（同一批样品，两条测试路径）：AT Hybrid dSB 550 g 研究放行 0.40875 g vs GADT 0.30750 g；SAM/Fluff Control GADT 0.23000 g vs 研究放行 0.20775 g（Std Error 0.02249）。"
  - "AT Hybrid 经 LabVantage 路径（研究放行）测得的回渗在 95% CI 下**显著差于** GADT 实验室路径；同一代码走不同测试路径可改变统计结论。"
  - "研究放行口径下 Study Release 代码间存在显著差异，而 GADT 口径下各代码互不显著——**测试路径会翻转显著性判定**。"
  - "竞品对标：AT Hybrid 在研究放行数据下差于 Assurance；若用 GADT 数据则不显著（图中 Code G=Griffin SAM/Fluff、Code W=Griffin AT Hybrid、Code R=Assurance）。"
  - "材料配置差异：Wrapsheet——对照用 full-wrap 17 gsm tissue，AT Hybrid 用 c-wrap（dSB 12 gsm CM7；TABCW 20 gsm Shalag；VONN 35 gsm MOJAVE 2.35v2）；Liner——对照用未印刷 Fitesa 12 gsm spunbond，AT Hybrid 用 Honeycomb 印刷 Fitesa 12 gsm SB。"
  - "工艺差异：Surge 均为 Shalag White SS7CT5H80；**面层-导流层压花（liner-surge embossing）——SAM/fluff 代码有，AT 代码没有**。"
pages_linked:
  - "[[Rewet Measurement Variability（回渗测试变异性）]]"
  - "[[GRIFFIN Rewet Program（GRIFFIN 超低回渗项目）]]"
  - "[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]"
  - "[[Liner-Surge Embossing（面层-导流层压花）]]"
  - "[[IPC BCC OI Portfolio（开放创新项目组合）]]"
---

# GRIFFIN Female DPU2 AT Hybrid Rewet Summary 女性 DPU2 AT Hybrid 回渗总结

> 本文是 **GRIFFIN 回渗项目**在女性 DPU2 平台上的一轮实验室回渗数据汇总。**结论一句话：**AT（ActivTech）系芯体的回渗**普遍高于 SAM/Fluff 对照**，但**是否"显著"取决于测试路径**——同一批样品走 GADT 实验室与走 LabVantage（研究放行）会得到**不同的显著性判定**，这是本页最重要的发现。

## 数据集 1 · 首轮多代码对比（550 g / 450 g 加载）

| 代码 Level | 显著性字母 Letter | 回渗均值 Mean (g) | 标准误 Std Error |
|---|---|---|---|
| AT Fluffless VONN（With Surge）- 550 g | A | 0.39750 | 0.02407 |
| AT Fluffless dSB - 550 g | B | 0.32250 | 0.02407 |
| AT Hybrid dSB - 550 g | B | 0.30750 | 0.02407 |
| AT Fluffless TABCW - 550 g | B | 0.28750 | 0.02407 |
| AT Hybrid dSB - 450 g | B | 0.28000 | 0.02407 |
| SAM/Fluff Control | B | 0.23000 | 0.02407 |

- **读法**：Levels not connected by same letter are significantly different（不同字母即 95% 置信水平下显著不同）。
- **AT Fluffless VONN（Without Surge）被排除**——摄入时间过高（extremely high intake times），其回渗为 **0.17 g**。**这说明"回渗低"不能单独作为结论：VONN 无 surge 版本回渗最低但摄入不可用。**
- 源文要求：**把该（无 surge VONN）代码与 Always Discreet 一起加入本组作为参照**。
- 后续动作：**"SAM/Fluff Control" 与 "AT Hybrid dSB – 550 g" 两个代码已进入女性 HUT（家庭使用测试），结果预计 mid-Feb。**
- 关键判断：**AT Hybrid dSB 550 g 平均比对照高 0.07 g，但在 95% CI 下不显著**（基于 GADT 实验室结果）。

## 材料与工艺配置 Material and Process Setup

| 部件 Component | SAM/Fluff Control 对照 | AT Hybrid 代码 |
|---|---|---|
| Wrapsheet 包裹层 | full-wrap 17 gsm tissue | c-wrap |
| dSB | — | 12 gsm CM7 |
| TABCW | — | 20 gsm Shalag |
| VONN | — | 35 gsm MOJAVE 2.35v2 |
| Liner 面层 | 未印刷 Fitesa 12 gsm spunbond | Honeycomb **印刷** Fitesa 12 gsm SB |
| Surge 导流层 | Shalag White SS7CT5H80 | Shalag White SS7CT5H80（同） |
| **Liner-surge embossing 面层-导流层压花** | **有** | **无** |

> ⚠️ **对比口径警告**：AT 系与对照**同时改变了包裹层形式、面层（印刷与否）与压花工艺**，因此回渗差异**不能归因于单一变量**（芯体类型）。**缺 LSE 是已知的结构性差异**，见 [[Liner-Surge Embossing（面层-导流层压花）]]。

## 数据集 2 · 同一样品的两条测试路径（GADT vs LabVantage）

| 代码 Level | 显著性字母 | 回渗均值 Mean (g) | 标准误 Std Error |
|---|---|---|---|
| AT Hybrid dSB - 550 g（Study Release） | A | 0.40875 | 0.02249 |
| AT Hybrid dSB - 550 g | B | 0.30750 | 0.02249 |
| SAM/Fluff Control | B / C | 0.23000 | — |
| SAM/Fluff Control（Study Release） | C | 0.20775 | 0.02249 |

- **同批样品、两条路径**：一套在 **GADT 实验室**测，另一套按研究要求通过 **LabVantage** 走研究放行流程；补充的 GADT 结果在**约 2.5–3 个月后**测得。
- **AT Hybrid 经 LabVantage 测得的回渗在 95% CI 下显著差于 GADT 路径**（0.40875 vs 0.30750 g）。
- **显著性被路径翻转**：Study Release 口径下各代码间**存在显著差异**；GADT 口径下各代码**彼此不显著**。
- **对照方向的差异较小且不显著**：SAM/Fluff Control 在两条路径下为 0.23000 g（GADT）与 0.20775 g（Study Release）。

## 竞品对标 Competitive Reference

- 图表代码：**Code G = Griffin SAM/Fluff**、**Code W = Griffin AT Hybrid**、**Code R = Assurance**（图中 Rewet 值可读到 0.24 与 0.4）。
- 图下方标注的阈值刻度：**Closed Cradle Rewet 0.4 / 0.3 / 0.2 / 0.15 / 0.05 / 0**——即项目内部把 0.15 g 与 0.05 g 作为刻度档位。
- **AT Hybrid 在研究放行数据下差于 Assurance**；**若改用 GADT 数据，则二者不显著不同**。

## Caveats 使用注意

- 本文**未给出样本量、加载液体、环境温湿度与 Closed Cradle 测试的具体参数**，跨文档比较前须补齐。
- 两轮数据的 **Std Error 不同**（0.02407 vs 0.02249），说明**不是同一次方差分析**，两表**不可互相换算**。
- 「550 g / 450 g」为加载量口径，AT Hybrid dSB 在 450 g 下回渗（0.28000 g）低于 550 g（0.30750 g），符合加载量越高回渗越大的直觉，但**同字母 B 表示二者与对照均未达显著**。
- 内部物料代码（tissue / CM7 / Fitesa / Shalag 牌号号）为 K-C 内部编号，引用时须确认对外部可披露范围。

## 关联页面 关联页面

- [[Rewet Measurement Variability（回渗测试变异性）]]
- [[GRIFFIN Rewet Program（GRIFFIN 超低回渗项目）]]
- [[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]
- [[Liner-Surge Embossing（面层-导流层压花）]]
- [[Shalag（Shalag 导流层与面层材料）]]
- [[Fitesa（Fitesa 非织造布）]]
- [[Rewet Method Comparison（回渗测试方法横向对比）]]
- [[IPC BCC OI Portfolio（开放创新项目组合）]]

---
type: source
title: "SAP Grade Selection for Baby Diaper Core（三份PPT对比·最终推荐）"
source_type: 提案
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP选型分析_三PPT对比_EN.docx.md
original_link: ""
date_published: 2026-09
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "最终推荐架构：三牌号分层——贴身侧单置 LG LK804ND（SAP1）+ poly 侧 Nuoer KC-511（快膨胀）× NR-950（延迟膨胀）混配，SAP2:SAP3 = 36:64，总装载 13.5 g/片"
  - "相对高端单 SAP 基准：SAP 成本 −40%、累积回渗 −59%、后期穿透 −49%、设计容量 +29%，且 SAP 用量少 10%"
  - "核心机理是「错峰膨胀动力学」（staggered swell kinetics）而非空间分层——快:慢比例才是真正的设计杠杆，不是位置"
  - "关键结构增量：在贴身侧 SAP 与混配层之间夹一层 REL（五纤维 TAB，24 gsm），提供毛细梯度与单向 z-flow；PPT 2 是靠混配层内的高 GBP 牌号实现通道"
  - "单一自由膨胀数值会骗人：须用 4 次加液序列测试（multi-insult）验证错峰是否真的成立——这是硬 gate 不是可选项"
  - "PPT 3 最大脆弱点：SAP3（NR-950）GBP 仅 8、Vortex 51 s，自身几乎不渗透 → 通道功能完全依赖 REL 激活（TAB Zone 2 须达 138–143 ℃、强制冷却 <40 ℃）"
  - "顾问判断：PPT 2 与 PPT 3 给出不同的牌号答案，不要假装它们一致；保留 PPT 2 的 N8 + Satellite 710 架构作为 REL 不稳定时的回退方案"
pages_linked: ["[[SAP错峰膨胀]]", "[[SAP性能指标（CRC AUL GBP Vortex）]]", "[[Gel Blocking（凝胶阻塞）]]", "[[REL增强层]]", "[[LG Chem（LG 化学）]]", "[[诺尔（Nuoer）]]", "[[Satellite Chemical（卫星化学）]]", "[[Nippon Shokubai（日本触媒）]]", "[[巴斯夫欧洲公司（BASF SE）]]", "[[单牌号全511 vs 分层多SAP混底（性能·成本·供应链）]]", "[[IPC BCC OI Portfolio（开放创新项目组合）]]"]
---

# SAP Grade Selection for Baby Diaper Core（三份 PPT 对比·最终推荐）

## 一句话定位

把三份 SAP 选型 / 仿真 PPT（**PPT 1 选型策略**、**PPT 2 芯体仿真 1**、**PPT 3 五区 + REL 仿真**）横向对比后的**最终推荐与顾问判断（英文）**。本页是 [[SAP错峰膨胀]] 的**架构落地版**：给出具体牌号、配比、装载量、REL 结构与成本口径，并明确**PPT 2 与 PPT 3 的结论并不一致**。

## 摘要

推荐架构为**三牌号分层**：贴身侧**单置一层 LG LK804ND**（SAP1，CRC 31.5 / AUL₀.₇ 18.0 / **GBP 53** / Vortex 36 s / 4.0 g），poly 侧为 **Nuoer KC-511（快膨胀，CRC 30.9 / AUL 18.4 / GBP 24 / Vortex 29 s / 3.4 g）× Nuoer NR-950（延迟，CRC 36.7 / AUL 19.4 / GBP 8 / Vortex 51 s / 6.1 g）**，**SAP2:SAP3 = 36:64**（偏向延迟储库以匹配 4 次加液曲线），SAP1 **不参与混配**、作独立层。总装载 **13.5 g/片**，设计容量 **387 mL**，安全系数 **1.6×**，容量利用率 62%。

相对高端单 SAP 基准的收益：**SAP 成本 −40%、累积回渗 −59%（另一处给 −59–68%）、后期穿透 −49%、设计容量 +29%**，且 **SAP 用量少 10%**。核心机理是**错峰膨胀动力学**——**不是空间分层而是时间错位**：SAP2 快膨胀承接第 1–2 次排泄，SAP3（51 s Vortex）在第 3–4 次才启动，两者永不同时封堵凝胶床，从而抬高总可用容量。PPT 1 明确表述：**"快:慢比例——而非位置——才是真正的设计杠杆"**。

关键结构增量：**REL 五纤维 TAB 层（24 gsm）**夹在贴身侧 SAP 与混配层之间，提供毛细梯度与单向 z-flow；PPT 2 则靠混配层内放高 GBP 牌号实现通道，无 REL。

五区匹配：Z2（目标湿润区）最重 **424 gsm**、Z4（后部储库）次之；Z1/Z5 仅承担贴身侧防漏屏障。男婴前倾湿润型已优化；**女婴中心型需另设 Z2/Z3 SKU 变体**。

## 提炼的数字与结论

| 角色 | 牌号 | 供应商 | CRC (g/g) | AUL₀.₇ | GBP | Vortex (s) | 装载 (g) | 功能 |
|---|---|---|---|---|---|---|---|---|
| **SAP1 贴身侧** | **LK804ND** | LG Chem | 31.5 | 18.0 | **53** | 36 | **4.0** | 独立薄层；快吸 + 低回渗 + 贴肤安全 |
| **SAP2 快膨胀** | **KC-511** | Nuoer | 30.9 | 18.4 | 24 | 29 | **3.4** | 承接第 1–2 次；CRC 刻意封顶 |
| **SAP3 延迟** | **NR-950** | Nuoer | **36.7** | 19.4 | **8** | **51** | **6.1** | 高 CRC + 高 AUL 储库；慢 Vortex = 天然延迟 |

| 项目 | 数值 / 结论 | 备注 |
|---|---|---|
| SAP2:SAP3 混配比 | **36 : 64** | 偏向延迟储库以匹配 4 次加液曲线 |
| 总装载 / 设计容量 | **13.5 g/片** / **387 mL** | 利用率 **62%**；安全系数 **1.6×** |
| 收益 | 成本 **−40%**、回渗 **−59%（另处 −59–68%）**、后期穿透 **−49%**、容量 **+29%** | SAP 用量 **−10%** |
| REL 层 | 五纤维 **TAB 24 gsm**；Zone 2 须 **138–143 ℃**、强制冷却 **<40 ℃** | PPT 3 独有 |
| 加液协议 | **60 mL × 4 = 240 mL**（0 / 0.5 / 3.5 / 6 h 真实间隔） | PPT 3 |
| 双源 / 备份 | SAP3 主供 NR-950，**备份 BASF 9635（CRC 38）**；SAP1 区域备选 **Satellite CR740** | 用于对冲 Nuoer OTIF |
| ⚠️ 成本敏感 | SAP3 换日本触媒 CAW **+10%**；SAP1 换巴斯夫 **+6%** | 国产平衡料是主要成本杠杆 |

### 三份 PPT 的差异（不可混引）

| 维度 | PPT 1 选型策略 | PPT 2 芯体仿真 1 | PPT 3 五区 + REL 仿真 |
|---|---|---|---|
| 性质 | 方法论 / 规格（无牌号、无成本） | 一阶仿真（"线性估算，需实验室确认"） | **可执行集成设计（"冻结进入 Stage 1"）** |
| 通道实现方式 | 未涉及 | 混配层内放**高 GBP 牌号**（Satellite 710，GBP 75） | **REL 层** |
| 牌号集 | 只定义 SAP1/2/3 角色 | 贴身 N511；poly N8 + Satellite 710（60/40） | 贴身 **LK804ND**；poly **KC-511 + NR-950** |
| 加液协议 | 概念性（重复排泄） | 40/50/60/70 mL = 220 mL（递增累积） | **60 × 4 = 240 mL**（真实间隔） |
| 装载 / 容量 / 安全系数 | — | ~14.9 g、286 mL、**1.3×** | **13.5 g、387 mL、1.6×**（利用率 62%） |
| 成本 / 风险 / 路线图 | 仅原则 | 仅下一步建议 | **完整成本拆解 + 风险登记册 + 四阶段验证路线图** |

> 结构关系：**PPT 3 显式引用 PPT 1** 的选型策略与 REL 仿真方法为其上位方法；**PPT 2 是更早 / 并行的仿真支线**（hourglass 形状、无 REL、N8+710 混配），实为 PPT 3 的前身。PPT 3 用 REL 层取代了 PPT 2 的高 GBP 牌号。

### 顾问判断与关键风险

1. **两次仿真给出不同牌号答案——不要假装它们一致**：PPT 2 的贴身侧 N511 的 GBP 仅 **26**，PPT 3 的 LK804ND 为 **53**；按 PPT 1「贴身层须在低载下保持孔隙」的规则，**LK804ND 明显更优**。
2. **PPT 3 最大脆弱点**：**SAP3（NR-950）GBP 仅 8、Vortex 51 s，自身几乎不渗透** → 通道功能**完全依赖 REL 激活**。若 REL 激活窗口漂移，**PPT 2 的做法（混配层内直接用 Satellite 710，GBP 75）更稳健** → 建议保留 PPT 2 的 **N8+710 架构作为回退方案**。
3. **"62% 利用率"是保守余量不是缺陷**：单 SAP 基准为 80% / 84%，但 PPT 3 用更少的 SAP 拿到 +29–36% 容量——这是为最坏载荷预留的余量。若实产数据显示湿润区更集中，**Z4 的 47% 利用率低到可以再削减装载、继续降本**。
4. **一切建立在单一假设上**：**KC-511 与 NR-950 之间存在真实、可复现的膨胀速率差**。风险登记册已标 High（颗粒偏析）与 Med（延迟与婴儿 30 min–3 h 排泄间隔失配）。**Stage 1 的 bench 动力学筛选（30 s → 3 h）是冻结规格前的硬 gate**，不通过不得进 pilot。

> 🔴 **manual_review（2026-09-29）**：本资料含 **SAP 牌号单价（$/MT 级）、单只成本（US¢/片级）与供应商切换的成本敏感度（+10% / +6%）**，属商务报价与成本条款类内容。依 AGENTS.md §5，**本页只保留相对量级与供应链结构判断，不落完整价格表与定点结论**，原文留存于 `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP选型分析_三PPT对比_EN.docx.md`。

## 关键论断（key_claims）

- **错峰是「时间」杠杆不是「位置」杠杆：快:慢比例才是设计变量** —— 支撑页：[[SAP错峰膨胀]]
- **单一自由膨胀数值会骗人，须用 4 次加液序列验证——这是硬 gate** —— 支撑页：[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]
- **REL 层是 PPT 3 通道功能的单点依赖，须保留无 REL 的回退架构** —— 支撑页：[[REL增强层]]
- **成本杠杆在「亚洲产高 CRC / 高 AUL 料」+ 贴身侧用全球料的组合** —— 支撑页：[[单牌号全511 vs 分层多SAP混底（性能·成本·供应链）]]
- **利用率 62% 是预留余量，不是设计缺陷** —— 支撑页：[[SAP性能指标（CRC AUL GBP Vortex）]]

## 关联页面

- 概念：[[SAP错峰膨胀]]、[[SAP性能指标（CRC AUL GBP Vortex）]]、[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]、[[Gel Blocking（凝胶阻塞）]]、[[REL增强层]]、[[分区密度设计]]、[[Intake System（摄入系统）]]
- 实体：[[LG Chem（LG 化学）]]、[[诺尔（Nuoer）]]、[[Satellite Chemical（卫星化学）]]、[[Nippon Shokubai（日本触媒）]]、[[巴斯夫欧洲公司（BASF SE）]]
- 对比：[[单牌号全511 vs 分层多SAP混底（性能·成本·供应链）]]、[[REL vs ADL（收集传递层 vs 导流层）]]
- 组合：[[IPC BCC OI Portfolio（开放创新项目组合）]]（OI-13 SAP 方向）

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP选型分析_三PPT对比_EN.docx.md`
- 原文链接：（无；内部顾问分析）
- 同族：[[SAP Selection Strategy and Trial Data Synthesis v3（SAP选型策略与实验数据综合分析）]]、[[SAP Selection Decision Base（17-SAP选型与实验数据决策库）]]、[[SAM Database-CW（全球 SAM 牌号性能数据库）]]

---
type: source
title: "温度变色指示器（Thermochromic Indicato"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/温度变色指示器（Thermochromic Indicato.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# 温度变色指示器（Thermochromic Indicato

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 会议纪要`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/温度变色指示器（Thermochromic Indicato.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# 温度变色指示器（Thermochromic Indicato

### 来自内部 brief 的硬边界


|项目|内部边界含义|
|---|---|

|应用对象|Baby diapers，包含 Open Diaper 与 Pants|

|价值主张|thermal regulation / cooling / comfort 的 consumer-visible RTB|

|验证状态|dry 与 wet 两种状态都需要测试|

|风险约束|不可明显伤害 absorbency、fit、cost、skin health、manufacturability|

|当前空白|dry-state thermal method 更难；claim path 仍需澄清|


### 2. 推荐 MVP 形态


|项目|草案|
|---|---|

|结构形式|hydrochromic printed patch、window label，或与现有 wetness indicator 相邻的二级提示区|

|安装位置|与 insult path 有可控耦合的外表面可见区域|

|颜色逻辑|干态浅色/隐藏，湿态显色；也可做图标显现|

|触发模式|优先 liquid exposure trigger；若探索 humidity accumulation，再做二期|

|与现有 WI 关系|不替代现有 wetness indicator，先做 differentiation 学习|


## 我建议的下一步


|顺序|动作|目的|
|---|---|---|

|1|先发 5 家公开技术问询|判断谁真能做 30–37°C 与 diaper-compatible 体系|

|2|并行定义 KC 内部 bench protocol|把 dry/wet、response time、false trigger 量化|

|3|先做 coupon card，不急着上整片 diaper|快速排掉不稳定体系|

|4|consumer team 先测 signal comprehension|防止做出材料但消费者看不懂|


## 推荐打样路径（最省试错）


|阶段|目标|交付|
|---|---|---|

|Phase 0|Desk research + supplier sample shortlist|5–8 家候选、材料类型矩阵|

|Phase 1|离体片材打样（film/nonwoven coupon）|thermochromic 与 hydrochromic coupon cards|

|Phase 2|diaper 外层 dummy build|不上人体、不做 full claim，只看可读性与 converting 兼容|

|Phase 3|bench insult + thermal map|dry/wet 双状态对比数据|

|Phase 4|quick consumer comprehension|“看不看得懂、信不信、会不会误解”|


## 潜在供应商联系人清单（公开商务入口，desk-research 版）


下面这张表只放“更像真的能做这件事”的对象，不放纯泛贸易商。联系人优先采用官网公开邮箱或 contact page；未看到公开邮箱的，保留官方 inquiry 页面。


|公司|国家/地区|能力判断|公开联系入口|适配判断|
|---|---|---|---|---|

|OliKrom|France|thermochromic|官网：olikrom.com；邮箱：contact@olikrom.com；电话：+33 (0)5 64 37 13 00|强 custom thermochromic formulation，适合 temperature band customization|

|DaeHyun Corp / MicroCapsule Pigment|Korea|both（thermochromic + hydrochromic）|官网：microcapsulepigment.com；联系页：Email Us；电话：031.923.8300|上游功能材料池很全，尤其适合 hydrochromic/wetness cue 打样|


### 5. 温度版的主要技术风险


真实 diaper 外表面温度和体感温度不完全等价，容易出现“看起来热，但妈妈摸起来没那么热”的信任落差。


thermochromic 材料常有 light/UV stability 与 long-term drift 风险。


converting 温度、热压、摩擦可能提前触发或损伤色变体系。


如果把阈值设太靠近 room temperature，会导致 shelf / transport false trigger。


## MVP 规格草案 B：湿度变色指示器（Hydrochromic Indicator）


### 1. 使用场景定义


用于可视化提示“潮湿暴露（wet exposure）/ 湿区扩展 / 局部受潮”，验证 caregiver 是否能区分“热不舒服”和“湿了需要处理”这两个不同信号。


以上边界均来自内部 brief 对 success criteria、risks 与 next-step 的描述（依据：R&D Intake Brief_BCC Thermal Regulation）。


### MVP 设计原则


第一版只做“可读信号（readable signal）”，不做“精密测量仪表（instrumentation）”。


指示器必须位于非 skin-contact 面，优先 outer cover exterior 或 backsheet window。


指示器材料体系必须和现有 converting 温度窗口、油墨/胶粘剂体系、迁移风险控制兼容。


第一版以 bench demo + consumer comprehension 为目标，不把 full regulatory claim 当作 MVP 退出条件。


thermal 与 humidity 两类信号必须可区分，避免被误认成普通 wetness indicator。


## MVP 规格草案 A：温度变色指示器（Thermochromic Indicator）


### 1. 使用场景定义


用于外层可视化提示 diaper 内部或近体表区域“偏冷 / 舒适 / 偏热”的状态趋势，帮助 caregiver 快速理解 thermal comfort 概念。


### 2. 推荐 MVP 形态


### 4. 建议验收项目


|类别|MVP 验收项|
|---|---|

|功能|指定 insult 后稳定显色|

|区分度|消费者能分清它和传统 wetness indicator 的含义差别|

|制造|不污染导辊、版辊、热封区域|

|包材稳定性|包装内存放 4 周后无异常变色|

|可叙事性|能支持“humidity / wetness exposure cue”而非过度承诺|


如果你想一步验证“妈妈到底更在意热，还是更在意湿”，组合版最有学习价值，但不建议作为首个工程样。


|模块|设计建议|
|---|---|

|左侧区|湿度/受潮提示|

|右侧区|温度/舒适度提示|

|颜色策略|湿度用蓝系，温度用红绿系，避免语义打架|

|MVP 目标|学习消费者是否能正确解码两种不同信号|

|退出条件|若理解错误率高，就拆回单功能方案|


|Matsui International Co., Inc.|Japan|both（thermochromic + hydro indicator）|官网：matsui-color.com；联系页：Contact；邮箱：info@matsui-color.com；电话：+1 310 767 7812|最值得优先接触，既有 thermochromic，也提到 Aqua Indicator，适合 diaper indicator MVP 讨论|

|Chromatic Technologies, Inc. (CTI)|United States|thermochromic|官网：ctiinks.com；邮箱：inquire@ctiinks.com；电话：+1 719 592 1557|成熟温变油墨供应商，强在温度指示，但 diaper 需定制开发|

|结构形式|外层印刷条带（printed stripe）或 laminated label patch|

|安装位置|core centerline 对应外表面，优先 front lower panel 或 crotch 外侧可见区|

|颜色逻辑|蓝 / 绿 / 红三态，或无色 / 显色双态|

|变色机理|reversible thermochromic ink / pigment；若做 breach demo，可另测 irreversible label|

|与产品关系|仅做指示，不承担结构功能|


### 5. 湿度版的主要技术风险


真正的 hydrochromic 体系很多更像“water exposure indicator”，不是精准 humidity sensor。


尿液成分、pH、lotion、topsheet 回渗都会干扰显色路径。


如果色变过快，会和现有 wetness indicator 重叠；如果过慢，消费者感知不到价值。


部分体系需要多孔窗口或液体接触路径设计，不是单换油墨就能解决。


## MVP 规格草案 C：组合版（Thermal + Hydrochromic）


### 供应商优先级建议


|优先级|公司|原因|
|---|---|---|

|Tier 1|Matsui, CTI, DaeHyun|一个兼顾 thermo+hydro，一个强 thermochromic 工业化，一个强 hydro/微胶囊材料池|

|Tier 2|OliKrom|适合 custom temp band，但 lead time / MOQ 需确认|

|Tier 3|New Prismatic|更像 process indicator / irreversible specialty source，适合作为补充方案|


我的建议不是一上来做“高精度传感器”，而是先做两个 low-regret MVP：


|模块|推荐 MVP 形态|目的|开发难度|建议优先级|
|---|---|---|---|---|

|温度变色指示器|外表面印刷或贴标式 reversible thermochromic indicator|给 thermal comfort/cooling claim 提供直观 RTB|中|P1|

|湿度变色指示器|与现有 wetness indicator 相邻或耦合的 hydrochromic window / printed patch|快速验证“可视湿度/受潮状态提示”消费者理解度|低到中|P1|

|二者组合版|温度 + 湿度双区段显示|验证消费者是否能区分“热”和“湿”两种信号|中到高|P2|


### 4. 建议验收项目


|功能|在设定温区内出现稳定、可重复的颜色变化|

|消费者理解|70%+ 受访者能正确理解“太热/太冷/舒适”基本含义|

|产品兼容|不引起明显 curl、blocking、set-off、smudge|

|老化|40°C / 75%RH 1 周后仍可读|

|视觉|与现有 graphics 不冲突，不显脏、不显廉价|


|NEW PRISMATIC ENTERPRISE CO., LTD.|Taiwan|thermochromic（含 irreversible）|官网：colorchange.com.tw；联系页：Contact；邮箱：nccinfo@colorchange.com.tw|更偏 process / breach / QC indicator；若做高温阈值示范可谈，不一定是 body-heat 最优|


## 建议首轮 RFQ / 技术问询模板


你发给供应商时，别问泛泛的“有没有产品”，直接问下面这几个点：


Can you provide reversible thermochromic ink/pigment systems with visible transition in the 30–37°C range, suitable for printing or lamination on diaper outer surfaces?


Can you provide hydrochromic or liquid-exposure indicating systems that are readable on a diaper exterior without significant color bleeding?


What is the recommended substrate set: PE film, breathable film, PP nonwoven, paper label, or laminated patch?


What are the process constraints: coating/printing method, drying temperature, lamination temperature, pressure, shelf life, and storage conditions?


Do you have any systems with low migration / non-skin-contact hygiene application experience?


What MOQ, sample lead time, and customization lead time apply for a diaper indicator feasibility sample?


# 


# 温度变色指示器（Thermochromic Indicat

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/温度变色指示器（Thermochromic Indicato.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/温度变色指示器（Thermochromic Indicato.md`
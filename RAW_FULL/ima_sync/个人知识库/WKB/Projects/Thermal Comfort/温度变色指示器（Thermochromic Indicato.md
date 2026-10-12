---
media_id: "note_3867e2b60070d7dc3f413086d0b0036e_7490349366788955"
source_file: "温度变色指示器（Thermochromic Indicato"
original_path: "RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/温度变色指示器（Thermochromic Indicato.md"
extracted: "2026-09-30"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
---

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


# 温度变色指示器（Thermochromic Indicator）与湿度变色指示器（Hydrochromic Indicator）MVP 规格草案 + 潜在供应商联系人清单


## 一页结论


基于内部 BCC thermal regulation intake brief，这个方向是成立的：KC 内部已明确识别到 diaper microclimate 是消费者痛点，且“simple visual indicator”被视为可能需要的 RTB 组件；同时，项目成功边界也被定义得很清楚——必须在 dry 与 wet 两种状态下看到可测的 thermal benefit，且不能带来 absorbency、fit、cost、skin health、manufacturability 的不可接受 trade-off（依据：R&D Intake Brief_BCC Thermal Regulation）。


### 3. 建议技术指标（第一版假设值）


下表不是 final spec，而是 bench-ready spec draft，目的是让 supplier 能按同一语言回样。


|参数|建议值|备注|
|---|---|---|

|激活温区（activation window）|30–37°C 可定制|覆盖 diaper microclimate 有意义区间；最终需用 KC bench 数据校准|

|关键显示点|建议先筛 32°C / 34°C / 36°C 三档|方便快速做 consumer-friendly 颜色脚本|

|响应时间|≤120 s 达到可辨识状态|模拟实际使用而非实验室瞬时响应|

|可视对比度|ΔE 或肉眼明显分级|以 caregiver 一眼看懂为准|

|循环稳定性|10 次冷热循环后可读|够支撑 MVP demo|

|印刷/贴合耐受|能承受 converting/lamination 常规窗口|需 supplier 回答 process cap|

|干态背景色|低干扰，不影响 artwork|避免 consumer 误以为尿显|

|迁移/析出|不可见渗色、不可污染衣物|最低门槛|

|Skin-contact|不允许直接 skin contact|降低 stewardship 风险|


不建议第一版就宣称“精确温度测量”或“持续恒温”。内部 insight 已经提示，妈妈们对“actively maintaining a just-right zone”这类强 claim 接受度不足，更适合先从“help you know when to act”的 visual cue 切入（依据：R&D Intake Brief_BCC Thermal Regulation）。


在 Figure 1 中，内部 brief 已直接把 diaper area 温度分布和 skin irritation pain point 绑定起来。


Figure 1: 内部 thermal regulation 概念图，把 diaper 微气候（microclimate）与 skin irritation 风险直接关联。


在 Figure 2 中，内部概念已把“高透气材料 + 温控结构 + 可视化提示”放在同一个叙事里，这对 MVP 架构很关键：indicator 不是单独卖点，而是 thermal platform 的可视化窗口。


Figure 2: 内部 concept 把 self-circulating layer、temperature lock 与 high-breathability material 组合呈现。


在 Figure 3 和 Figure 4 中，内部概念画面已经明确出现“color-changing temperature indicator”这条消费者可见路径，这说明 MVP 最值得先验证的是“看得懂、信得过、不会误解”的 visual language，而不只是材料本身。


Figure 3: 内部 Thermo Breeze Comfort 概念页，已出现可视温度 indicator。


Figure 4: 内部 Thermo Care 概念直接示意“too warm / too cool”的颜色反馈。


## 项目边界与设计原则


### 3. 建议技术指标（第一版假设值）


|触发方式|以液体接触或液体迁移触发为主|比真正 RH sensor 更现实|

|首次显色时间|≤60 s|满足直观感知|

|最低可检出液量|bench 筛选 5 / 10 / 20 mL 三档|便于建立 readable window|

|显色面积增长|与 insult level 有一定关联，但不追求线性计量|MVP 只求“看懂”|

|色牢度|不允许明显 bleeding / back-transfer|特别重要|

|机械稳定性|卷装、摩擦、折叠后不掉粉不掉色|converting 必需|

|干态误报|高温高湿储存下不可提前显色|shelf robustness|

|与胶粘剂/薄膜兼容|不受 lotion、surfactant、SAP dust 明显干扰|diaper 环境真实复杂|


## 供应商分层建议


|类型|你要找谁|用途|
|---|---|---|

|功能油墨/颜料供应商|thermochromic / hydrochromic 材料本体|最快拿到 lab sample|

|标签/印刷转换商|会把功能油墨变成 label/printed patch 的供应商|更接近真实 diaper 结构|

|薄膜/非织造协同方|能把 indicator 集成进 backsheet / patch 的合作方|二阶段工程化|


## Sources


Internal concept and project boundaries: R&D Intake Brief_BCC Thermal Regulation


Supplier capability references: Matsui International, Chromatic Technologies, Inc., OliKrom, MicroCapsule Pigment / DaeHyun, New Prismatic Enterprise


Relevant sources


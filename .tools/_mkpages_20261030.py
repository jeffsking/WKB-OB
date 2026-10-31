#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-30 生成两张源摘要页到 _kb_compile_pages/<media_id>.md。

front matter 的 source_path 直接从 _kb_compile_plan.json 取，避免手抄偏差
（AGENTS §2.3：source_path 必须逐字等于该条 raw_path）。
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

PAGES_DIR = ".tools/_kb_compile_pages"
os.makedirs(PAGES_DIR, exist_ok=True)

SIX_ID = "wechatarticle_3867e2b60070d7dc3f413086d0b0036e_649da9df864de859cd2d6ee45e5a6439"
SOL_ID = "wechatarticle_3867e2b60070d7dc3f413086d0b0036e_5a7a531e7cb98131298210372e8ceb8d"

SIX_URL = "https://mp.weixin.qq.com/s/capHPiZ5m2mVhQST7ijAwA"
SOL_URL = "https://mp.weixin.qq.com/s/EyZVyvudF1UgHlUCgdUzWg"

SIX_TITLE = "Chromic Six-Trigger Combinations（变色局 005 · 六触发源组合追问 · 2026-10-26）"
SOL_TITLE = "Thermochromic Light-Modulation Daily No.14（遮阳隔热 · 热致与温致变色日报 · 2026-10-12）"

SIX_CLAIMS = [
    "**六触发源不是六条赛道，而是同一块界面的六种管理方式** —— 电致变管主动调光、温致变管被动响应、光致变管紫外与自适应遮光、力致变管应力可视、气致变管泄漏可读；判断标准从「谁的性能更高」转为「谁在管界面的哪一维」",
    "**EC/TC 第一次在电解质层面「合署办公」**：普鲁士蓝（PB）阳极着色电极 + 羟丙基纤维素（HPC）水凝胶电解质，TC 功能由电解质本体承担（633 nm 调制 ~83%），而非额外叠一层活性层 —— 器件因此可在「主动深调 / 被动温控 / 联合调制 / 全通透」四模式间切换，可见光总调制 87.3%",
    "**力致变已分岔为「开关型」与「阈值指示型」两条线**：罗格斯 B-N Lewis 酸碱对交联 PDMS 是开关型（拉伸荧光开、松手灭）；螺吡喃交联 PDMS 光波导是阈值型（1.4–1.6 MPa 起显色，远低于 7.6–10.8 MPa 破坏强度）。两者都**尚未跨过「定量」这道坎**",
    "**力致变工程障碍不是灵敏度而是循环可逆性与基体相容性** —— 作者给出的下一个观察指标是「1000 次以上加载循环后的标定曲线保持率」，而非更高的荧光对比度",
    "**光致变在拓宽光谱（500–2500 nm）、气致变在压低检测限（0.11 v/v% H₂ / 100 s 内变色）**，两者共同回答「能否在真实环境条件下给出无需仪器的可读信号」；光致变的合理定位是免维护被动层，不是替代电致变",
    "**产业端提示是制造韧性而非性能**：Gauzy 以 700 万美元股权融资重启 SPD 产线（此前经以色列法院批准的清偿方案处理约 6,100 万美元负债），说明「停产一年」的重启成本远不止修设备 —— 良率、客户认证、供应链信任都要重走",
    "**下一阶段分水岭：谁能把两个以上触发源装进同一套器件架构而不互相拖累** —— EC/TC 已有落地工作，光/热、力/气是作者点名的待验证交叉点",
]

SIX_BODY = r"""
# Chromic Six-Trigger Combinations（变色局 005）

## Positioning 一句话定位

A single editorial issue that reframes the six chromic trigger families from **competing product categories** into **six orthogonal ways of managing one interface dimension each** — and argues the next competitive frontier is multi-trigger device architecture, not single-material performance.

把六个致变色触发源从「六条平行赛道」重构为「一块界面上六个互相正交的管理维度」，并指出下一轮竞争不在单品性能，而在「能否把多个触发源装进同一套器件架构」。

## Source Facts 来源事实

| 项 | 内容 |
|---|---|
| 载体 | 微信公众号「变色局」· BIANSEJU DAILY SIGNAL · 第 005 期 |
| 发布日 | 2026-10-26（星期一） |
| 体裁 | 行业自媒体的「信号判断」型日报（非新闻搬运），含 3 处 `[reference:n]` 引文标注 |
| 本期覆盖 | 温致变 · 热致变 · 电致变 · 光致变 · 力致变 · 气致变 |
| 核心提问 | 「六个触发源里，哪两个的组合会最先在同一个器件里跑通？」 |
| 可信度 | 中 —— 有引文标注与期刊/机构出处，但判断句为编辑观点，数字未经原始论文复核 `[待验证]` |

## Signal 01 · EC/TC Dual-Response Window 电-热双响应智能窗

Prussian-blue (PB) anodic-coloration electrode coupled with a hydroxypropyl-cellulose (HPC) hydrogel electrolyte; the **electrolyte itself carries the thermochromic function**, so TC is no longer an added active layer but the EC device's working medium. `Advanced Science`, 2026.

| 指标 | 数值 | 备注 |
|---|---|---|
| TC 调制（633 nm） | ~83% | 由 HPC 电解质本体提供 |
| 离子电导率 | 62.58 mS/cm | 同时承担离子传输 |
| 拉伸应变 | 514% | 水凝胶柔性 |
| PB 着色效率 | 108.21 cm²/C | |
| 着色 / 褪色时间 | 5 s / 6.8 s | |
| 可见光总调制 | 87.3% | 显著优于单一 EC 或单一 TC 窗 |
| 工作模式 | **4 种** | 主动深调 / 被动温控 / 联合调制 / 全通透 |

- **Why it matters（为何关键）**：以往 EC+TC 叠加是「两层各干各的」，界面多、阻抗大、调制互相抵消；本工作让两者**共享同一套离子传输路径**，因此是「分工」而非「叠加」。
- **Remaining blocker（卡点）**：耐久性与大面积均匀性未解；作者判断竞争焦点将从「单品性能」转向「多触发源同架构而不互相拖累」。

## Signal 02 · Industry Motion 产业端：Gauzy 重启 SPD 产线

| 项 | 内容 |
|---|---|
| 事件 | Gauzy Ltd. 于 2026-10-15 完成 **700 万美元**股权融资 |
| 前置 | 以色列法院批准的清偿方案处理约 **6,100 万美元**负债 |
| 用途 | 重启以色列 SPD 乳液生产 + 德国 SPD 调光膜制造，推进建筑改造用 SPD 后装方案 |
| 状态 | Research Frontiers 确认付款已开始，**产能恢复节奏未明确** |

> 作者的解读是本条最有价值的部分：一条产线停一年，重启成本远不止修设备 —— 良率要重爬、客户认证要重走、供应链信任要重建。对 EC/TC/光致变所有冲量产的路线，这是「制造韧性」的前置信号：性能关过了，下一关是**停得起、也起得来**。

## Signal 03 · Six-Trigger Matrix 六触发源矩阵

| 品类 | 触发源 | 当前在管什么 | 主要卡点 |
|---|---|---|---|
| 电致变 | 电压 / 电流 | 按需、精确调光 | 大面积均匀性、车规/建筑质保 |
| 温致变 / 热致变 | 温度 | 零功耗被动热管理 | 可见光透过率与调制的取舍 |
| 光致变 | 紫外 / 可见光 | UV 屏蔽、自适应遮光 | 循环疲劳、响应速度 |
| 力致变 | 应力 / 应变 | 应力可视化、损伤预警 | 定量读数、循环可逆性 |
| 气致变 | 特定气体 / 蒸气 | 泄漏可视化、VOC / 氢气传感 | 可逆性、选择性、定量标定 |

> 该矩阵为「变色局」编辑部基于本期覆盖品类整理，**非单一来源数据**（原文已声明）。矩阵的用途不是排序，而是区分「功能重叠但维度不同」：电致变 vs 温致变都在调光，但一个主动一个被动；力致变与气致变根本不抢调光主战场，它们管的是界面的**状态可读性**。

## Signal 04 · Mechanochromism 力致变的两条线

| 路线 | 体系 | 行为类型 | 关键数字 |
|---|---|---|---|
| 罗格斯大学（JACS, 2026-10） | B–N Lewis 酸碱对交联 PDMS 弹性体 | **开关型**（拉伸即亮 / 松手即灭） | B–N 键拉伸断裂→荧光开启；PDMS 低 Tg 使键快速重组→荧光熄灭 |
| 螺吡喃交联 PDMS 光波导 | 螺吡喃开环显色 | **阈值指示型** | 起始应力 **1.4–1.6 MPa**；材料破坏强度 7.6–10.8 MPa；可逆、非破坏 |

- **两条线的分岔**：开关型回答「这里有没有受力 / 键有没有断」；阈值型回答「受力有没有到危险线」。
- **共同未跨过的坎 = 定量**：从「指示器」变「传感器」，需要颜色/荧光强度 ↔ 应力-应变之间**可标定、可重复、可温度补偿**的映射。
- **工程障碍排序**：作者明确把循环可逆性与基体相容性排在灵敏度之前（B–N 键在真实结构上经温度波动与长期预应变后重组效率是否衰减；螺吡喃阈值换基体/交联密度即漂移）。
- **下一个值得盯的指标**：不是更高荧光对比度，而是**1000 次以上加载循环后的标定曲线保持率**。

## Signal 05 · Photochromic & Gasochromic 光致变与气致变

| 方向 | 代表工作 | 指标 | 定位 |
|---|---|---|---|
| 光致变（光谱拓宽） | MoO₃ / WO₃·H₂O 复合膜 | 响应范围 **500–2500 nm**（可见→近红外） | 全光谱自适应遮光 |
| 光致变（多模式） | W₁₈O₄₉ 基缺陷-界面协同工程 | 可见-近红外**三模式**按需调控 | 被动热管理 |
| 气致变（低检测限） | Pd/Mo 双金属催化 + 偶氮染料纸基传感器 | **0.11 v/v% H₂**，100 s 内红→无色；对 CO/CO₂/N₂/O₂/NH₃ 选择性；室温 | 氢气泄漏可视化 |
| 气致变（可逆性） | WO₃ 基路线 | 追求可逆性与更快响应 | — |

- **光致变的真实瓶颈**：紫外响应数秒可启动，但饱和着色常需数十分钟、褪色依赖环境 → 在建筑/车规的「实时调控」场景天然慢半拍；合理定位是**免维护被动层**，不是替代电致变。
- **气致变的根本区别**：它的「界面」不是窗而是气体环境，价值不在调光而在安全。

## Cross-Read 横向判断（编者）

六个触发源并置后最清晰的一条线：致变色正在从「一种材料改变颜色」变成「**一块界面被拆成多个维度、由不同触发源分工管理**」。因此值得追踪的不是单品类性能刷新，而是交叉点 —— EC/TC 共享电解质（已落地）、光/热双响应（待验证）、力/气多模态（待验证）。产业端 Gauzy 的提醒则把话题拉回制造：分工再精细，最后都要落到「停得起、也起得来」。

## Relevance to Hygiene Applications 对卫材的启示 `[推断]`

> 以下为知识库侧推断，非原文结论，供后续验证。

- **力致变的「阈值型」定位比「开关型」更贴近卫材**：腰围张力指示、穿戴压痕预警需要的是「到危险线才变色」的可标定门槛，而非有无响应；但当前 1.4–1.6 MPa 的起始应力远高于织物/无纺布实际受力区间（kPa 级），**跨基体移植是硬门槛**。
- **气致变纸基传感器**（室温、低成本、可大规模部署）在「氨/硫化物气味可视化」上有想象空间，可与库内 [[Odor Control Technology Landscape（除味技术全景）]] 的化学吸附支线交叉验证；但 0.11 v/v% 的检测限对体味场景仍偏粗。
- **「多触发源同架构」正好对上卫材的真实需求**：湿 + 温 + 力 三信号共存于同一片芯体，任何「三层各干各的」叠加工艺都会被成本与厚度否掉 —— 与原文对 EC/TC 叠层的批评同构。

## Linked Pages 关联页面

- 分类总纲：[[Chromism Taxonomy（变色现象分类）]]、[[变色材料 Chromic Materials]]
- 触发源概念：[[热致变色 Thermochromic]]、[[电致变色 Electrochromic]]、[[光致变色 Photochromic]]、[[机械变色 Mechanochromic]]
- 机理/阈值：[[Mechanophore Mechanochromism（机械力致变色分子）]]、[[Mechanochromic Activation Threshold Down-Shifting（力致变色激活阈值下调）]]
- 应用侧：[[Odor Control Technology Landscape（除味技术全景）]]、[[Chromic Materials Bibliography（变色材料书籍·温湿力精表）]]

## Original 原文

- 本地路径：`__RAW_PATH__`
- 原文链接：__URL__
- 镜像正文：`__FULL_PATH__`
- 正文形态说明：REST/网页通道抽取，原文的 emoji 分隔符与版式已丢弃，文字与数字完整。
"""

SOL_CLAIMS = [
    "**「解耦」成为本期最强设计范式**：普渡 DLTC 把黑态/白态在**层间**解耦（68 μm 黑→半透明面层 + >400 μm 超白基底），黑龙江大学把可见光/LWIR 用 NSGA-II 算法协同优化，双通道综述把太阳光/LWIR 解耦列为下一步方向 —— 「让不同功能由不同结构承担」正在取代「单一材料全能」",
    "**DLTC 的双维度调制幅度是本期最硬的数字**：Tc 25 °C；ΔTsol **36.7%**（51.4%→88.1%）、ΔRvis **81.2%**（6.0%→87.2%）；户外实测较黑色屋顶降温 **23 °C**、较白色屋顶升温 **12 °C**",
    "**热致变色正从「省能」走向「产能 + 多功能」**：ASU 的 VO₂ + 重掺杂硅涂层白天太阳吸收率 90%/红外发射率 23%、夜间 8–13 μm 发射率 85%，发射率摆幅 62%，与商用 TEG 集成后正午 1.64 W/m²、夜间 26 mW/m²（真空 35 mm²）",
    "**转变温度下探基本完成，竞争焦点转向耐久性/雾度/可见光透过率/规模化**：DLTC 25 °C、水凝胶 25–42 °C 可调；VO₂ 的主要失效路径是氧化为 V₂O₅，核壳（Mg 掺杂 VO₂@ZrO₂：Tlum 52.4% / ΔTsol 7.1%）与 SiO₂ 抗反射层（ΔTsol 最高 17.7%）是主流耐久性解法",
    "**水凝胶路线的核心痛点（循环体积收缩）出现明确技术解法**：专利 CN119119356B（2026-04-28 授权，发明人章炜/徐刚）以离子液体替代传统交联剂，靠 PNIPAm 链与离子液体的多重氢键/离子相互作用实现相转变，宣称高透光、响应快、温度可调、循环稳定",
    "**产业化进入拐点但格局高度分散**：2026 年全球热致调光膜市场 75.3 亿美元→2030 年 142.8 亿（CAGR 13.6%），2026 被判为大规模商业化拐点年（中国新建公共建筑渗透率 12%→18%），但智能窗材料前三企业合计仅占 12% 份额",
    "**政策是最大外生变量**：欧盟 EPBD 修订案强制新建公共建筑安装动态遮阳（拉动需求 +22%）、LEED 将智能调光材料纳入加分项、中国建筑节能强标 —— 三条同时生效，解释了「拐点年」判断的政策基底",
    "**头部渠道壁垒已开始形成**：天津南玻把热致变色玻璃并入标准产品序列（与三银/双银 Low-E、EC、真空复合中空并列，U 值 0.4–1.8 W/(m²·K)、SC 0.15–0.60），福耀以 PDLC 为载体覆盖热致变色与 EC 并集成隔热层（单片天幕 >3 m²、−40~105 °C）",
]

SOL_BODY = r"""
# Thermochromic Light-Modulation Daily No.14（遮阳隔热 · 热致/温致变色日报）

## Positioning 一句话定位

A machine-generated but unusually dense industry digest that maps the **thermochromic light-modulation field onto three axes at once — materials science, building-scale energy simulation, and market/policy** — and lands on one design paradigm: functional decoupling across layers, wavelengths and time-of-day.

一份由 AI 生成、但信息密度异常高的行业日报：把热致/温致变色调光同时铺在**材料科学、建筑尺度能耗模拟、市场与政策**三条轴上，最终收敛到同一个设计范式 —— 在层间、波段、昼夜三个维度上做功能解耦。

> ⚠ **可信度提示**：原文自标「内容由AI生成」，全部数字为二手转述、未经原始文献复核。本页所有具体数值均标 `[待验证]`，引用前须回溯原文/专利/论文。该页的价值在于**索引与判断框架**，不在于数值本身。

## Source Facts 来源事实

| 项 | 内容 |
|---|---|
| 载体 | 微信公众号日报（第 14 期），标题「遮阳隔热 · 热致变色/温致变色调光材料日报」 |
| 报告日 | 2026-10-12 |
| 侧重 | 热致变色 / 温致变色调光材料最新进展 |
| 结构 | 科研前沿 11 条 + 产业与市场 5 组 + 趋势小结 7 条 |
| 生成方式 | AI 生成（原文自标），检索词与 freshness 窗口随文附出 |
| 可信度 | 低 —— AI 生成二手汇总；数值、专利号、市场口径均需回溯 `[待验证]` |

## Research Front 科研前沿（11 条）

| # | 团队 / 出处 | 体系 | 关键数字 `[待验证]` |
|---|---|---|---|
| 1 | 普渡 Xiulin Ruan · ACS Nano Letters（10-05 在线） | **DLTC 双层热致变色涂层**：~68 μm「黑→半透明」面层 + >400 μm 超白基底 | Tc **25 °C**；ΔTsol **36.7%**（51.4→88.1）；ΔRvis **81.2%**（6.0→87.2）；较黑屋顶降温 **23 °C**、较白屋顶升温 **12 °C**；EnergyPlus 全气候带节能 |
| 2 | 黑龙江大学 张文文 · Sci China Tech Sci 69(3):1320101 | TiO₂/VO₂/TiO₂/Ag + PDMS 相变自适应辐射涂层，NSGA-II 多目标优化 | Tvis 各相态 >**0.6**；ΔεAW **0.422**；较普通玻璃降温 **14.8 °C**；四城全年冷+暖能耗 −**22%~32%** |
| 3 | 亚利桑那州立大学 · Cell Rep Phys Sci | VO₂ 薄膜 + 重掺杂硅衬底 + 硅间隔层，温度自主切换吸收体/辐射制冷体 | 日间 αsol **90%** / εIR **23%**；夜间 8–13 μm ε **85%**；摆幅 **62%**；TEG 正午 **1.64 W/m²**（真空 35 mm²）、夜间 **26 mW/m²**；2 英寸圆片对流环境 0.48 W/m² |
| 4 | Adv Funct Mater 2026 | 企鹅羽毛启发 VO₂ 基 **Janus** 膜（双面异功能） | 光热侧 αsol **94.5%**；制冷侧 R>90%、εMIR **97.1%**；VO₂ 相变 4 个数量级电阻变化 → 8.2–40 GHz 微波调制（X 波段 0.78–32.1 dB）；超疏水 |
| 5 | Adv Funct Mater 2026-02 | 无电热等离激元智能窗（~200 nm 银纳米环 + 薄液层） | 室内降温 **>4 °C**，可见光保持透明，完全光驱动 |
| 6 | 2025 | 光子晶体 + PNIPAm 水凝胶 + ATO 智能窗 | 较普通玻璃低约 **7.2 °C**；兼作「光学温度计」 |
| 7 | SSRN 预印本 | 氨基甲基吡啶（AMP）异构体低维铅碘钙钛矿 | (2-AMP…)₂Pb₂I₇ 显著热致变暗；(4-AMP…)₂Pb₂I₇ 加热黄→红；结构稳定至 ~**200 °C** |
| 8 | 专利 **CN119119356B**（2026-04-28 授权，章炜/徐刚） | 离子液体/水二元溶剂相转变热响应凝胶（NIPAm + 离子液体替代交联剂） | 宣称高透光、响应快、温度可调，**克服循环体积收缩** |
| 9 | 河南大学 · Adv Nanocomposites 2026 | 等离子体液化学（PiLC）一步法 VOx/Au/PVA 多功能膜 | 钒价态调控 + 金纳米颗粒原位生成同步完成；NIR 调制 + 光热 + 抗菌三合一 |
| 10 | arXiv:2610.06711（10-05） | 硅–VO₂ 热调超表面，磁电耦合（bianisotropy）重构 | 多态双各向异性、功率限幅、方向性透射/反射 |
| 11 | Science Bulletin 综述（东南大学 + 康考迪亚）· DOI 10.1016/j.scib.2026.09.031 | VO₂ / 卤化物钙钛矿 / 水凝胶 / 液晶 / 离子液体五体系比较 | 结论：瓶颈已从「找更好材料」转向「把材料性能转化为可靠的建筑尺度产品」，呼吁部署导向设计 |
| 11b | NREL 建筑能耗模拟 | 12 层 / 窗墙比 95% 办公楼，8 气候区，15 min 步长 | 钙钛矿热致变色双玻各气候区均优于普通双玻；炎热区甚至优于三玻；寒冷区「双玻 + 热致变夹层」三玻最优；变色循环 200 次稳定 |
| 11c | Revista DYNA 综述（2026-10-12） | EC / TC / PC 三类智能玻璃按气候区能效评估 | 主动式（EC）削峰 + 动态调控；被动式（TC）稳定性好、运维低 |

**VO₂ 耐久性专题（生物通 2026-10-02）**：主要失效路径为氧化成 V₂O₅；三条解法 —— 核壳颗粒（Mg 掺杂 VO₂@ZrO₂：Tlum **52.4%** / ΔTsol **7.1%**）、SiO₂ 抗反射层（ΔTsol 最高 **17.7%**）、VO₂-SiO₂ 复合气凝胶。

## Industry & Market 产业与市场

| 口径 | 数值 `[待验证]` | 备注 |
|---|---|---|
| 热致调光膜专利 | 2026 年申请量同比 **+18.3%** | 集中在响应速度与低温启动；迭代周期缩至 18 个月 |
| 全球市场 | 2025 **75.3 亿美元** → 2030 **142.8 亿**（CAGR **13.6%**）；需求 3.8 亿 m² → 7.1 亿 m² | 2026 判为大规模商业化拐点年；中大型项目 ROI 8–12 年 |
| 中国位置 | 出口占全球 **41.2%**（最大净出口国）；高端光学级原料进口依赖 **35.7%** | 出口结构「量大、料在外」 |
| 政策 | 欧盟 EPBD 强制动态遮阳（+22% 需求）；LEED 加分；中国双碳强标 | 中国新建公共建筑渗透率 **12%→18%** |
| 变色膜/EC/PDLC 窗 | 2025 124.3 亿 → 2026 138.4 亿 → 2034 327.6 亿美元（CAGR **11.37%**） | 头部：Saint-Gobain(SageGlass)、Gentex、AGC、Gauzy、Polytronix |
| 智能窗材料 | 2024 3.08 亿 → 2025 3.45 亿 → 2034 7.01 亿美元（CAGR 12.8%） | 北美 32%/欧洲 28%；**前三企业合计仅 12%** → 高度分散 |
| 水凝胶光学限幅 | 2025 1.85 亿 → 2026 2.05 亿 → 2034 5.20 亿美元（CAGR 12.3%） | Pleotint/Suntuitive 称 95% Tvis、80% ΔTsol、响应 <12 s、可后贴；Chromatic Technologies 纳米填充 PNIPAM 滞回 <2 °C |

**产能与格局动向**：天津南玻产品线已并列三银/双银 Low-E、热致变色、电致变色、真空复合中空（U 0.4–1.8 W/(m²·K)、SC 0.15–0.60，PHI/NFRC 认证）；福耀以 PDLC 为载体覆盖热致变色与 EC 并集成隔热层（天幕 >3 m²、−40~105 °C）；绍兴迪飞签约滕州无机全固态 EC 玻璃项目（总投资 3 亿元、30 亩）；Apollo 基金 2026-10-10 完成收购日本板硝子（NSG）。中国节能玻璃 2025 出口预计 18 亿美元（+6%），主流向东南亚与中东。

## Trend Synthesis 趋势小结（原文 7 条，编者压缩为 5 条判断）

1. **解耦范式**：黑/白（DLTC 层间）、可见光/LWIR（算法协同）、太阳光/LWIR（综述定方向）——「让不同功能由不同结构承担」正在取代「单一材料全能」。
2. **从省能到产能 + 多功能**：ASU 昼夜自主切换 + TEG 发电；Janus 膜把热管理、微波调制、超疏水叠在一张膜上 →「调光膜 = 能源器件 / 功能表面」。
3. **载体三分裂**：玻璃 / 膜 / 涂层并行，DLTC 这类可涂覆路线把热致变色扩展到屋面与既有建筑改造。
4. **温度已不是主要矛盾**：转变温度稳定落在 25 °C 舒适区（DLTC 25 °C、水凝胶 25–42 °C 可调），竞争转向耐久性、雾度、Tvis 与规模化工艺。
5. **拐点 + 分散并存，政策与标准是最大外生变量**：2026 拐点年、前三企业仅 12% 份额（新进入者窗口仍开）与头部渠道壁垒成型同时发生；ISO 21344 类测试标准落地将加速「实验室→产品」。

## Relevance to Hygiene Applications 对卫材的启示 `[推断]`

> 以下为知识库侧推断，非原文结论。

- **可迁移的是「解耦范式」，不是建筑场景本身**：卫材的功能层（吸收 / 回渗 / 透气 / 指示）历来要求「一层多能」，而本期的核心命题恰好相反 —— **把功能拆给不同结构承担**。库内 [[REL 六层结构]] 与 [[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]] 的分区/分密度设计，本质是同一条思路在吸收芯体上的表达。
- **水凝胶路线值得关注但不适配一次性用品**：CN119119356B 解决了循环体积收缩，但离子液体 + NIPAm 的成本与可洗性决定其只能落在耐用品（尿布兜、可重复使用护垫）而非抛弃式芯体。
- **政策外生变量提示一个真实风险**：热致调光膜的「拐点年」判断高度依赖 EPBD/LEED/双碳三条政策的同时生效；卫材侧的变色油墨（温变湿变指示）若被纳入标准（如失禁护理标识规范），同样会出现政策驱动的需求跃迁 —— 库内 [[卫生护理用品特种变色油墨供应商调研（光敏温敏湿敏 · AI 痕迹件）]] 已记录该假设，但尚无标准依据 `[待验证]`。

## Linked Pages 关联页面

- 概念：[[热致变色 Thermochromic]]、[[电致变色 Electrochromic]]、[[VO2]]、[[Thermochromic Microcapsule (Leuco Dye System)]]、[[变色材料 Chromic Materials]]
- 分类与书目：[[Chromism Taxonomy（变色现象分类）]]、[[Chromic Materials Bibliography（变色材料书籍·温湿力精表）]]
- 姊妹期：[[Chromic Six-Trigger Combinations（变色局 005 · 六触发源组合追问 · 2026-10-26）]]
- 卫材应用：[[REL 六层结构]]、[[卫生护理用品特种变色油墨供应商调研（光敏温敏湿敏 · AI 痕迹件）]]

## Original 原文

- 本地路径：`__RAW_PATH__`
- 原文链接：__URL__
- 镜像正文：`__FULL_PATH__`
- 正文形态说明：微信公众号反爬需 Chrome UA + Referer，正文自 `#js_content` 抽取；原文表格被压平为行文，本页已按语义重排为表格。
"""


def build(it, title, claims, body, url, page_name, credibility, cred_note):
    fm = [
        "---",
        "type: source",
        f'title: "{title}"',
        "source_type: 公众号",
        f"source_path: {it['raw_path']}",
        f'original_link: "{url}"',
        f"date_published: {it['date_published']}",
        "date_processed: 2026-10-30",
        f"credibility: {credibility}",
        f'credibility_note: "{cred_note}"',
        "knowledge_update_status: done",
        "key_claims:",
    ]
    for c in claims:
        fm.append(f'  - "{c}"')
    links = ["[[热致变色 Thermochromic]]", "[[变色材料 Chromic Materials]]"]
    fm.append("pages_linked: [" + ", ".join(f'"{x}"' for x in links) + "]")
    fm.append("compile_mode: semantic")
    fm.append("---")
    text = "\n".join(fm) + "\n" + body.replace("__RAW_PATH__", it["raw_path"]) \
        .replace("__FULL_PATH__", it["full_path"]).replace("__URL__", url)
    p = os.path.join(PAGES_DIR, it["media_id"] + ".md")
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"[page] {page_name} → {len(text)} chars → {p}")


def main():
    plan = json.load(open(".tools/_kb_compile_plan.json", encoding="utf-8"))
    by = {x["media_id"]: x for x in plan["items"]}

    six = by[SIX_ID]
    six["date_published"] = "2026-10-26"
    six["page_name"] = SIX_TITLE
    build(six, SIX_TITLE, SIX_CLAIMS, SIX_BODY, SIX_URL, SIX_TITLE, "中",
          "行业自媒体「变色局」第 005 期，含 3 处 [reference:n] 引文标注与期刊/机构出处；判断句为编辑观点，具体数值未经原始论文复核，页内标 [待验证]。与卫材的相关性判断为知识库侧推断，非原文结论。")

    sol = by[SOL_ID]
    sol["date_published"] = "2026-10-12"
    sol["page_name"] = SOL_TITLE
    build(sol, SOL_TITLE, SOL_CLAIMS, SOL_BODY, SOL_URL, SOL_TITLE, "低",
          "AI 生成日报（原文自标「内容由AI生成」），全部数字为二手汇总、未经原始文献/专利/市场报告复核；专利号 CN119119356B、DOI 10.1016/j.scib.2026.09.031、arXiv:2610.06711 为可回溯锚点，其余市场口径仅作趋势参考。页内数值统一标 [待验证]。")

    json.dump(plan, open(".tools/_kb_compile_plan.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("[plan] page_name / date_published 已回写")


if __name__ == "__main__":
    main()

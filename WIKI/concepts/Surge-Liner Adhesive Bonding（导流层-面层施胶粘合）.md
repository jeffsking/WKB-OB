---
type: concept
title: "Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）"
domain: [卫材研发, 芯体与吸收]
status: growing
updated: 2026-09-30
tags: [施胶, 面层-导流层界面, 添加量, 喷嘴, 覆盖率, 压合, 回渗]
aliases: ["导流层-面层施胶", "Surge-Liner Interface Adhesive", "HSBL"]
---

# Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）

> 一句话定义：在**导流层与面层之间施加一层热熔胶**（通常施在导流层侧），用"胶连接"替代/补充"压花连接"，使两层在受压时**不脱开、不相对滑移**，从而让液体持续沿界面向下转移、降低回渗。它的核心矛盾是：**胶既是连接器也是堵塞物**——覆盖率越高连接越强，但胶本身会占住排液通道，且压合会把导流层压扁。

## 机理 / 结构拆解

1. **为什么界面连接会影响回渗**：面层与导流层若只是"叠在一起"，受压时会分层、出现间隙，液体被挤回贴肤侧时没有连续的毛细通路把它拉回芯体。**连接（continuity）本身就是一条抗回渗通道**——这正是试验假设"覆盖率越高 → 回渗越低"的物理基础。
2. **第一个反作用：胶堵排液**。胶是疏水的、占据孔隙的。覆盖率提高到一定程度后，胶膜反而**切断液体从面层进入导流层的通路**（"block drainage"）。因此回渗对覆盖率不是单调下降，而是**存在最优区间**。
3. **第二个反作用：压合压扁导流层**。用 PICASSO 花型加压合能同时提供连接与压花效果，但**压合会压缩导流层厚度、减少空隙体积**。空隙变少 → 持液能力下降、回渗可能上升；但同时连接变强 → 回渗可能下降。**两种效应方向相反，所以源资料把这条假设写成"could help or hurt"**。
4. **胶种的影响被归到"表面能"**：不同胶种对液体的润湿行为不同，会改变界面上的液体转移；但该假设在源资料中被明确标注"**可能需要进一步定义**"——即**机理尚未建立，属探索性变量**。
5. **喷嘴不是"等效替换件"**：同一流量下，**CF Swirl（1 孔、ø0.02 in）出口速度约 10,952 cm/min，Minibead（14 孔、ø0.03 in）仅约 348 cm/min——相差约 30 倍**。孔数少、孔径小的喷嘴必须靠极高速度送出同等流量，这直接决定**雾化程度、纤网穿透深度、胶丝形态与开放时间**。换喷嘴等于换施胶形态。
6. **换胶种必须重算泵速**：胶密度不同（RT-8723 **0.83 g/cc** vs DM5402U **0.92 g/cc**），同 gsm 下所需泵速差约 9%（18.15 vs 16.59 RPM）。**沿用旧泵速 = 添加量直接偏掉**。
7. **计算链条是可复用的模板**：施胶面积（62 mm CD × 250 mm MD = 15,500 mm²）→ 按目标 gsm 得 g/片 → 乘车速（300 片/分）得 g/min → 除以（泵排量 × 密度）得泵速 → 再按每喷嘴孔数与孔径算出口速度。**任何一次"改车速/改 gsm/换胶/换喷嘴"都应重跑这条链**。
8. **评价手段要配齐三类**：**剥离测试（Peel）**测连接强度、**毛细测试（Capillarity）**测液体转移、**MicroCT**测压缩后的空隙结构——三者分别对应"连接够不够""通路通不通""空隙还剩多少"，缺一项就无法区分上述两个反作用。

## 关键参数表

| 参数 Parameter | 典型值 / 范围 Value | 出处 Source |
|---|---|---|
| 施胶位置 | **导流层侧（Surge）**；基材对 = 74 mm CT5 导流层 + 12 gsm SB 面层 | [[HSBL Rewet Trial Plan & Adhesive Calcs（面层-导流层施胶回渗试产计划）]] |
| 添加量 Add-on | **1.7 / 2.8 / 3.9 gsm**（= 0.02635 / 0.0434 / 0.06045 g/片） | 同上 |
| 胶温 | 325（°F；约 163 ℃，单位源表未标） | 同上 |
| 线速 / 节拍 / 车速 | 246 fpm / 305 mm / 300 片/分 | 同上 |
| 压合 | **Pressure + PICASSO 花型** 或 None；压合压力 **70 psi** | 同上 |
| 胶种与密度 | Rextac RT-8723 **0.83 g/cc**；Henkel 5402（DM5402U）**0.92 g/cc** | 同上 |
| 泵速（3.9 gsm） | RT-8723 **18.15 RPM**；DM5402U **16.59 RPM** | 同上 |
| 喷嘴出口速度（3.9 gsm） | CF Swirl **10,952** > Summit 3,380 > Rhythym 2,867 > Signature 1,195 > Slot Coat 1,071 > Minibead **348** cm/min | 同上 |
| 喷嘴孔径 | Slot Coat 1 mm > Minibead 0.030 > Summit 0.018 > CF Swirl 0.020 > Signature / Rhythym 0.012 in | 同上 |
| 图案气 / 喷嘴-纤网距离 | 15–45 psi（视喷嘴）/ 25–40 mm（Minibead 为 touching web） | 同上 |
| 验证手段 | **Peel（剥离）+ Capillarity（毛细）+ MicroCT** | 同上 |

> ⚠️ **禁止无来源参数**：上表数值来自同一份内部试产计划（[[HSBL Rewet Trial Plan & Adhesive Calcs（面层-导流层施胶回渗试产计划）]]），**尚无实测结果交叉验证**；**"覆盖率 ↔ 回渗"的最优区间、表面能如何影响回渗**在本库中缺失，标 `[待验证]`。
> 🔴 **内部工艺敏感 Internal-sensitive**：码号、喷嘴件号与产线设定属内部工艺资产，本页只记变量结构与方向性结论。

## 相邻概念

- 同界面另一机制：[[Liner-Surge Embossing（面层-导流层压花）]]（压花提供连接，无胶；本页为其施胶版）
- 胶与设备族：[[Ultra-Low Add-On Adhesive Application（超低添加量施胶）]]（芯体侧的极低添加量路线，与本页 1.7–3.9 gsm 属不同量级）、[[Olefin-Based vs EVA Construction Hot Melt（烯烃基 vs EVA 结构胶）]]、[[Polyolefin Hot Melt Adhesive（聚烯烃热熔胶）]]
- 基材：[[Resilient Surge（PET 回弹导流层）]]（CT5 = 100% PET；PET 不易粘结正是本页施胶的动因之一）
- 判读前提：[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]、[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]（毛细测试是本页三种验证手段之一）

## 追加：Open Innovation 批（2026-09-29 追加 · 剥离实测结果）

> 本节为 **Resources / Open Innovation 批（批次 S4_Resources_Open Innovation_05）** 编译时的追加记录，**不改动上方既有结论**。上方四条假设在本批得到了**实测数据**（剥离强度），但**只验证了其中"连接性"一条**——回渗、毛细与 MicroCT 结果不在本批资料内。详见 [[Peel Test STM-00438（剥离强度测试）]]。

### 1. 实测：剥离强度由工艺组合决定，跨度约 35 倍

| 码 Code | 胶种 | 添加量 (gsm) | 喷嘴 | 压合 | 平均载荷 (gf) | 峰值载荷 (gf) |
|---|---|---|---|---|---|---|
| **7** | Henkel 5402 | 3.9 | Minibead | PICASSO | **537.1** | 750.3 |
| 11 | Rextac RT-8723 | 3.9 | Minibead | PICASSO | 375.9 | 546.4 |
| 6 | Henkel 5402 | 3.9 | Minibead | None | 355.9 | 526.3 |
| 3 | Henkel 5402 | 3.9 | Signature | PICASSO | 293.4 | 428.6 |
| 8 | Henkel 5402 | 3.9 | CF Swirl | PICASSO | 159.3 | 261.6 |
| 14 | Rextac RT-8723 | 3.9 | Summit | PICASSO | 124.8 | 190.6 |
| **17** | Rextac RT-8723 | 2.8 | Signature | PICASSO | **85.6** | 140.4 |
| **17B** | Rextac RT-8723 | 2.8 | Signature（**China Liner**） | PICASSO | **24.9** | 51.7 |
| 18 | Rextac RT-8723 | 2.8 | Signature | None | 25.3 | 47.8 |
| **15** | Rextac RT-8723 | 1.7 | Summit | None | **15.4**（最低） | 33.7 |

### 2. 四条假设的验证情况

| 假设 Hypothesis | 验证情况 Status | 证据 Evidence |
|---|---|---|
| ① 覆盖率越高 → 连接越强 → 回渗越低 | **前半段成立**（连接性确实上升）；**后半段未验证**（回渗数据不在本批） | 压合开/关对照：26.6 → 124.8 gf（Summit）；25.3 → 85.6 gf（Signature） |
| ② 添加量越高 → 连接性越好 | ✅ **成立且单调** | RT-8723/Summit/压合：1.7 → 24.6、2.8 → 34.7、3.9 → **124.8 gf** |
| ③ 胶种表面能影响回渗 | ⚠️ **未验证**——但胶种对**剥离强度**影响显著且一致 | Minibead/3.9/压合：Henkel **537.1** vs RT-8723 **375.9 gf** |
| ④ 压合既连接又压扁导流层（可能有利或有害） | ⚠️ **两条效应都观察到，但未分离** | 连接效应：2–5 倍提升；压缩效应：原表注记"高亮码出现 **导流层明显撕破**"，提示已过强 |

### 3. 本批新增的两个"计划外"发现

- **换面层等于换界面**：同工艺下把 12 gsm SB 面层换成 **China Liner**，剥离强度从 **85.6 gf 掉到 24.9 gf（约 1/3.4）**——界面结合是**两个表面**的事，不能只评价胶。
- **过强区是真实存在的**：原表注记"高亮的码在导流层上出现明显撕破"，说明结合强度已超过导流层自身强度，**剥离从界面失效转为基材撕裂**。这与假设①的"胶多会堵排液"共同构成"**结合并非越强越好**"的两条独立证据。

> 📌 **重要边界 Important boundary**：本批只有**剥离强度**数据，**没有回渗、毛细或 MicroCT 结果**。因此「连接性 ↑ → 回渗 ↓」在本库仍**属假设而非结论**；剥离强度最高的码（7）**不等于**回渗最优的码。

### 4. 验证记录

> ✅ 验证（2026-09-29，来源 [[HSBL Peel Test Results（面层-导流层剥离强度实测）]]）：本页假设②「添加量越高连接性越好」得到**直接实测支持且呈单调关系**；假设①的"连接性"半段亦成立。但**假设③、④与"回渗是否下降"均未获数据验证**，上方结论**未被修正也未被确认**。

- **追加 `[待验证]`**：剥离强度 ↔ 回渗的定量关系与"最优窗口"；毛细测试与 MicroCT 结果；China Liner 与 SB 面层差异的成因（表面能 vs 结构）。

## 经验教训

> ✅ 验证（2026-09-29，来源 [[HSBL Rewet Trial Plan & Adhesive Calcs（面层-导流层施胶回渗试产计划）]]）：本页为新概念页。首条来源的价值在于**把"施胶降回渗"写成可证伪的四条假设并各自标注反作用**——这是本库少见的"假设先于数据"的试验设计文档，可作为同类界面试验的模板。

- **教训**：**别把"更多胶 = 更好"当默认**。源资料自己在假设里写了"more adhesive may also block drainage"——覆盖率与添加量都要找**最优区间**而非单调加大。
- **教训**：**压合的正负效应必须分开测**。压合同时带来"连接↑"与"空隙↓"，两者对回渗方向相反；只测回渗会把净效应误当成单向结论，必须配合 **MicroCT 看空隙、Peel 看连接**。
- **教训**：**换胶或换喷嘴必须重算工艺设定**。密度差 10% → 泵速差约 9%；喷嘴孔数/孔径差 → 出口速度差可达 30 倍。**设错这两项，试验结论就是错的**。
- **教训**：**运行顺序要先"大变量"后"小变量"**（胶种 → 花型 → 压合 → 最后添加量），因为换胶需要冲洗施胶机（源计划中单独排了 8 h），把小变量放前面会造成重复冲洗。
- **待补 `[待验证]`**：本试验的实测结果（Peel / Capillarity / MicroCT / 回渗）；覆盖率与添加量的最优区间；表面能影响回渗的机理。

## 来源

- [[HSBL Rewet Trial Plan & Adhesive Calcs（面层-导流层施胶回渗试产计划）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/Surge-Liner Interface/53267-HSBL-REWET-CLEMMER Trial Plan and Adhesive Calcs .xlsx.md`

## 追加：层间空隙（interstitial）作为回渗变量与 LSE 的两面性（2026-09-29 追加 · 来源：Rewet Update 2025-12-02 Depend 拆解）

- **层间空隙是独立变量**：AD 的 **attachment strength 粘合强度高于 Depend** → **层间空隙（interstitial space）更少**；假设这**同时改善面层的排液（draining of the liner）**。即：粘合不只是力学/手感变量，**也是回渗变量**。
- **目标函数由此变为双目标**：粘合强度↑ 有利于排液与结构完整，但**过度粘合/熔掉空隙**会恶化摄入与铺展（见本页上方关于空隙体积的约束）。**「粘得更紧」与「留得住空隙」需成对验收**。
- **LSE 的两面性（重要修正性认识）**：当前用 **LSE** 形成该结构，但 **LSE 会制造 small pockets 小液袋，对回渗不利**；整体判断仍是 **net positive 净效应为正**，但问题被明确抛出：**can we find a better way 能否找到更好的方式？** —— LSE 不应被视为终态方案。
- **验证路径**：DOE #1（**adhesive pattern 施胶图案 / bonding 粘合方式 / adhesive type 胶型** 三因子），样品已制作，**microCT 预计 2026-01 出结果** —— 用 **microCT** 直接观测层间空隙与液袋，而不是只靠回渗终值反推。
- 与 [[Liner-Surge Embossing（面层-导流层压花）]] 的关系：压花是**同一设计空间内的另一手段**，两者都通过改变层间接触/空隙来影响排液，需在同一 DOE 框架下比较。
- 来源页 [[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]；相关机理 [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]。

> 校验：本节为 2026-09-29 追加，**未修正上方任何结论**。

## 追加：Surge-Liner Interface 试验矩阵结果落地（2026-09-29 追加 · 来源：Full Results.xlsx）

> ✅ Verification（2026-09-29，source 来源 [[Full Results.xlsx]]）：Surge-Liner Interface 的 **22-code 试验矩阵实测结果已回填**——变量覆盖基材（74mm CT5 surge vs 12gsm SB liner）× 施胶（Henkel 5402 vs Rextac RT-8723）× 上胶量（1.7–3.9 gsm）× 喷嘴（Signature/Summit/Minibead/CF Swirl）× 压合（None/Pressure/PICASSO）。实测 **残留液 0.096–0.157 g**、**附着强度 15.4–537 gf**。control = code 17；**code 17B（"Loki"，换 China Liner）残留液最低 0.096 g**。该结果部分回应了上方「待补：本试验的实测结果」缺口；附着强度近 35 倍的跨度证实施胶/压合组合是界面结合的主导变量，与「粘合强度↑ → 层间空隙↓」的既有判断方向一致。上胶量/喷嘴/压合各因子的单因子效应拆分库内暂无，标 `[待验证]`。

## 追加：AD 竞品双花型尺寸实测（2026-09-29 追加 · 来源：Always Discreet Adhesive Pattern Dimensions.pptx）

> ✅ Verification（2026-09-29，source 来源 [[Always Discreet Adhesive Pattern Dimensions.pptx]]）：AC Brand Connect 所述"AD 两种 surge attachment adhesive 花型"的**量化落地**（2025-08-07 HSBL 拆解采集）——**CF Swirl**（Line 80，XL 码）：swirl 直径 1.5-2 cm、宽 1-1.5 cm、列间距 1 cm、swirl 间距 0.5 cm；**Slot Coat**（Line 82/83）：中带 0.2 cm、侧带 0.1 cm、带间距 0.6 cm、外带间距 1 cm，且 **S/M 与 L 码同一花型尺寸复用**。P&G 大区 slot 线 + 高端 swirl 线的双花型产品化事实，为本库"花型是独立设计变量"的判断提供竞品佐证；具体数值为竞品拆解数据，不外发。花型编码（Code 6/6B/8/9）对应 [[Liner-Surge Interface HSBL Trial.xlsx]] 变量表。

## Related Sources 关联来源

- [[CD Pants Process Overview - GIC Korea（CD裤式产品工艺概览·韩国上岗培训）]]
- [[Code 10.jpg]]
- [[Code 11.jpg]]
- [[Code 13.jpg]]
- [[Code 2 (2).jpg]]
- [[Code 2 - liner.jpg]]
- [[Code 2.jpg]]
- [[Code 5 - liner.jpg]]
- [[Code 5.jpg]]
- [[Code 6b.jpg]]
- [[Code 8.jpg]]
- [[Code 9 try 1.jpg]]
- [[Code 9 try 2.jpg]]
- [[Code 9.jpg]]
- [[GRIFFIN Learning Cycle Check In（GRIFFIN 学习周期复盘 · 2025-06-25）]]
- [[GRIFFIN Regroup - Depend Rewet Update（GRIFFIN 重整更新 · 2025-08-28）]]
- [[HSBL Attachment Strength Results（HSBL 附着强度结果 · 2025-11-18）]]
- [[HSBL Peel Test Results（面层-导流层剥离强度实测）]]
- [[HSBL Rewet Trial Plan & Adhesive Calcs（面层-导流层施胶回渗试产计划）]]
- [[Liner-Surge Rewet Density Testing（面层-导流层密度测试数据）]]
- [[Rewet Competitive Analysis - Depend vs Always Discreet Intake System（回渗竞品分析 · 2025-09-11）]]
- [[Rewet Learning Plan（回渗学习计划工作表）]]
- [[Rewet Materials Study - Draft for initial scoping discussions 0.7.17.25.pptx]]
- [[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]
- [[US5266394A Disposable Articles Containing SIS Block Copolymers (Dow)]]
- [[War on Rewet Update 2026-01-21（Depend · Poise · Huggies 三条战线基准与假设台账）]]
- [[War on Wetness - Adult Care Rewet Update（成人护理回渗进展 2026-03）]]


---
type: source
title: Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）
source_type: pptx（非正式进展分享 · Raegan Informal）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.12.02 - Raegan Informal.pptx.md
original_link: ""
date_published: 2025-12-02
date_processed: 2026-09-29
credibility: A（内部实测与台架数据；机理假设部分为 B）
knowledge_update_status: done
key_claims:
  - 回渗总方针：系统性地把每一个组件里的每一滴残液都清掉（systematically eliminate every drop of residual fluid from every component）
  - Depend 三组件拆解判定：Liner ✗、Surge ✗、Interstitial ✓
  - 面层根因判定为润湿性（wettability）：AD 面层比 Depend 更不亲水；除此之外两者面层看起来一样
  - 不做亲水整理的面层在 GRIFFIN HUT 上渗漏更高（与 ATACAMA+ HUT 结果一致）→ 该路线回炉重做
  - 导流层根因判定为孔径分布（PSD）而非平均孔径：Depend 分布更宽、大孔更多
  - 机理假设：小孔里的液体不会被非常大的孔拉出来，液体被滞留（stranded）在导流层里（与 SIROCCO 学习一致）
  - 层间（interstitial）：AD 粘合强度高于 Depend，层间空隙更小；假设这有助于面层排液
  - LSE 会制造小液袋（对回渗不利），但净效应仍为正 → 寻找更好的替代方式
  - 摄入互换实验：AD 的面层+导流层单独就足以把 Depend 回渗降到 0.15–0.17 g（原 0.51 g）；AD 卷曲纤维无额外回渗收益
pages_linked:
  - Rewet Test（回渗测试）
  - Residual Fluid & Pore Stranding（残液与孔隙滞留）
  - ADL（导流层）
  - Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）
  - 亲水整理耐久性
  - LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）
  - Shalag（Shalag 导流层与面层材料）
  - 并列复合自卷曲纤维
  - Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）
  - Cradle Intake Test（Cradle 摄入测试）
  - Intake System（摄入系统）
---

# Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）

> 非正式进展分享（Raegan Informal），作者 Kerry Clemmer，2025-12-02。主题：**用基础机理（fundamentals）的方法讲 Depend 的回渗战役**。本页为该 PPTX 的编译页；所有数值均为原稿给出的实测/台架值，机理假设单独标注等级。

## Definition 定义

**Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）回渗进展 2025-12-02（非正式分享 · Depend 拆解与毛细机理）** — 一份以 Depend 为镜头（told through the Depend lens）的回渗进展汇报。核心方法论是：不靠试错，而是用**毛细压力法（Capillary Pressure Method）**定量测出每个摄入层「有多想留住液体」，再逐组件找根因、逐组件消残液。

## Goal & Approach 目标与方法

- **Goal 目标**：Best in class rewet（回渗做到业界最佳）。
- **Approach 方法**：**Systematically eliminate every drop of residual fluid from every component** 系统性地清除每一个组件中的每一滴残液。
- 组件分解（teardown 拆解）：**Surge 导流层 / Liner 面层 / Core 芯体 / Interstitial 层间**。
- 因果链（原稿图注）：`Closed Cradle Rewet is driven by desorption` → `Desorption is driven mainly by capillarity` → `Measure capillarity of each intake layer` 密闭 Cradle 回渗由**解吸**驱动，解吸主要由**毛细作用**驱动，因此要逐层测毛细性。

## Depend Teardown 判定结果（三组件）

|组件 Component|判定 Verdict|根因 Root cause|下一步 Next step|
|---|---|---|---|
|Liner 面层|✗ 有差距|润湿性（AD 更不亲水）；孔径（两者相当）|减处理面层（Oct）、LOKI 面层调研|
|Surge 导流层|✗ 有差距|**孔径分布 PSD**（非平均孔径）|窄 PSD 样品验证回渗；开发材料|
|Interstitial 层间|✓ 已对标|AD 粘合强度更高 → 层间空隙更小|DOE #1（胶型/图案/粘合方式）|
|Core 芯体|— （本次未列入主线）|—|—|

## Liner 面层：润湿性判定与「不做处理」路线的失败

- 毛细测试显示 AD 与 Depend 面层存在差异：**Depend 面层把液体留得更久**（keeps a hold of more fluid longer than AD）。
- 毛细性与**解吸能量（desorption energy）**两项指标**都偏向 Always Discreet（AD）**。
- 根本判定（capillary physics 毛细物理）：差距只能来自 **wettability 润湿性**或 **pore size 孔径**；实测 **AD 的润湿性低于 Depend**，除此之外两面层看起来一样。
- **反直觉结果**：不做亲水整理的面层（untreated liner）在 **GRIFFIN HUT 上渗漏更高**——与早前 **ATACAMA+ HUT** 的结论一致；该路线此前在 BCC 曾成功过，但现在需要 **go back to the drawing board 回炉重做**。

**HUT 渗漏（Std Lkg 标准渗漏率 + Tukey 分组）**

|Code 代码|Std Lkg 标准渗漏率|Grp 分组|
|---|---|---|
|Control 对照|3.1%|A|
|GRIFFIN|3.2%|AB|
|Always Discreet|3.7%|AB|
|Untreated Liner 未处理面层|4.6%|B|

> 证据等级：**A（实测 HUT + 统计分组）**。
> 设计原则呼应：**Intake materials have lower capillarity and wettability compared to where fluid is locked up**（摄入层材料的毛细性与润湿性应低于液体被锁住的地方）。同时正文另有一条原则：**The number of pores is minimized to provide less places for fluid to be trapped**（孔的数量要尽量少，减少液体可被困住的地方）。

## Surge 导流层：是孔径「分布」而不是孔径「大小」

- 反直觉现象：**Depend 毛细性更好，但整体排液反而更差**，原因是 **basis weight 克重更高**。
- AD 是**低克重 + 高毛细性**——对 intake 摄入不利；AD 用 **curly fiber 卷曲纤维**来补偿摄入，**而卷曲纤维不影响回渗**（doesn't impact rewet）。
- 反向启发：我方拟试用**含卷曲纤维的 wrapsheet 包覆层**，看能否抵消这类导流层带来的摄入损失。
- **根因判定**：最可能是**孔径差异**；平均孔径（average pore size）AD 与 Depend **相近**，但**孔径分布 PSD 不同**——**Depend 分布更宽、大孔更多**。
- **机理假设（B）**：**小孔中的液体不会被非常大的孔拉出来**，从而把液体**滞留（stranded）在导流层内**。与 **SIROCCO 学习**一致。
- **结论性判断**：**Size distribution is just as important as overall size** 孔径分布与孔径大小同等重要。
- 供应侧动作：Shalag 已提供候选样品 → 先查 PSD，再上产品验证回渗。
- 对应设计原则：**Pore networks are well connected, and no fluid is trapped at interfaces**（孔网络要连通良好、界面处不滞留液体）。

## Interstitial 层间：粘合强度与 LSE 的两面性

- **AD 的 attachment strength 粘合强度高于 Depend**（即层间空隙 interstitial space 更少）。
- 假设：更小的层间空隙**同时改善面层的排液**（improves draining of the liner）。
- 当前手段：**LSE**（用于形成该结构）**会制造小液袋（small pockets），对回渗不利**；但 **LSE 净效应仍为正**。问题被明确提出：**can we find a better way? 能否找到更好的方式？**
- 行动：DOE #1（adhesive pattern 胶图案 / bonding 粘合方式 / adhesive type 胶类型）；样品已制作，**microCT 预计 1 月出结果**。

## Intake Swap Experiment 摄入互换实验（决定性证据）

手工改制产品（hand-modified products）对比：

|配置 Configuration|Closed Cradle Rewet 密闭 Cradle 回渗（g）|
|---|---|
|Depend Core + Depend Liner/Surge|0.51 / 0.51（两次重复）|
|Depend Core + AD Liner/Surge|0.17|
|Depend Core + AD Liner/Surge + Curly Fiber 卷曲纤维|0.15|

- **AD 的面层 + 导流层单独就足以把 Depend 回渗从 ~0.51 g 降到 0.15–0.17 g**（降幅约 3 倍）。
- **AD 的卷曲纤维没有额外的回渗收益**（no incremental rewet benefit）——它只对 **intake 摄入**有益。
> 证据等级：**A（台架实测）**。这是一条**归因级证据**：回渗差距定位在摄入系统（liner+surge），不在芯体。

## Capillary Pressure Method 毛细压力法（方法附录）

**How it works 原理：**
1. 试样置于载物台，载物台与储液池保持恒定液体连通；
2. 载物台可垂直移动以改变**静水压头（hydrostatic head = 压力）**；
3. 测量试样中的液体量 → **saturation 饱和度**（按试样重量归一化，g/g）。

**输出：**
- **Height vs Saturation 曲线**（吸收支 absorption = 下降台面；解吸支 desorption = 上升台面）。
- **代表性毛细压力（representative capillary pressure）**：真实材料孔径有分布 → 为便于代码间比较，**用模型取「半饱和（halfway saturated）」处的单一毛细压力**作为代表值。
- **解吸能量（desorption energy）**：**height–saturation 曲线下的面积（area under the curve）**，代表把液体拉进或排出所需的总能量；**解吸能量越低 → 纤维越容易变干（fibers dry out easier）**。

> 该方法在同批 [[ATH SAM Relocation（2025-07-29 · 解吸能量·残液·microCT 与 SAM 再分配台架）]] 中亦作为量化工具出现（量级 1.8E+04 ~ 6.7E+04 ergs），本页为其**方法学出处**。

## Ongoing Activity 进行中工作（按品牌）

**Depend**
- Liner 面层：减处理面层（Oct 已排期）；LOKI 面层调研。
- Surge 导流层：窄化孔径分布 PSD → 验证回渗影响 → 开发材料；试制**卷曲纤维复合 + 低克重或窄 PSD 导流层**。
- Interstitial 层间：DOE #1（胶图案 / 粘合 / 胶型）。

**Poise**
- CR&D 拆解进行中；下一步 TBD；**ARTEMIS 落地 LSE**。

**Huggies**
- **SAM 用量与位置 DOE**：深挖如何在 Colt 上实现所见的**高压回渗（high pressure rewet）**水平。

## 关联页面 Linked Pages

- [[Rewet Test（回渗测试）]] · [[Cradle Intake Test（Cradle 摄入测试）]]
- [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]] · [[ADL（导流层）]]
- [[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]] · [[亲水整理耐久性]]
- [[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]] · [[Shalag（Shalag 导流层与面层材料）]]
- [[并列复合自卷曲纤维]] · [[Intake System（摄入系统）]]
- [[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]

## 存疑与冲突 Open Issues

1. **HUT 渗漏表两处不一致**：正文 Markdown 表为 `GRIFFIN 3.2% AB / AD 3.7% AB`；图片 alt 文本读作 `GRIFFIN Always Discreet 3.7% AB`（疑似 GRIFFIN 数值缺失、与 AD 列粘连）。**本页采用 Markdown 表**，差异已登记，未做修正。
2. **摄入互换实验的重复数**：图中为 0.51 / 0.51 / 0.15 / 0.17 四个柱，未明确标注哪根为「含卷曲纤维」；本页按「AD 组两根、其中较低者（0.15）为含卷曲纤维」解读，**结论不受影响**（两者差异 0.02 g 远小于 0.34 g 的主效应）。
3. **大孔滞留机理为假设（B）**：「小孔液体不被大孔拉出」尚未被直接验证，属于与 SIROCCO 一致的推断；Shalag 窄 PSD 样品的产品验证是判据。
4. **LSE 的定位存在张力**：本页称 LSE 制造小液袋但对回渗净效应为正；与 [[ActiveTech Platform（ActiveTech 在线薄芯体平台）]] 相关页面若出现相反表述，应以「净效应为正、但需寻找更好方式」为准。

> 🔴 **manual_review（2026-09-29）**
> 1. 本页含**竞品拆解级数据**（Always Discreet 面层/导流层的毛细性、解吸能量、HUT 渗漏率、互换实验克级回渗），属内部竞争情报，**对外引用前须脱敏**。
> 2. 原稿图片中 Depend / AD 的毛细压力与解吸能量**具体数值未以文本形式给出**（仅坐标轴刻度 0–25 dynes/cm²、0–8000 ergs、0–14000 ergs），**不得据坐标轴刻度反推数值**。
> 3. 项目代号（GRIFFIN / LOKI / ARTEMIS / Colt / SIROCCO）与 HUT 渗漏率属内部项目信息，本页仅登记其在知识网络中的关系，不展开商务含义。

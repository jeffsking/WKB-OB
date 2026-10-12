---
type: source
title: "ADT Brain Trust - Fluff and Rewet（绒毛浆与回渗 DOE 复盘）"
source_type: 内部技术材料
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/03.25.26 - ADT Brain Trust - Fluff and Rewet.pptx.md
original_link: ""
date_published: 2026-04-01
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "文件性质 = **ADT Brain Trust 复盘**（标题页标注 4/1/26；文件名标 03.25.26），主题「**绒毛浆（Fluff）与回渗**」+「**保液容量（Ret Cap）与回渗**」；把 **MAMBA #1 / #2 / #5 / HUT、MONEYBALL、BB DOE** 六套 DOE 与 GRIFFIN / Depend 的历史数据放在同一套因子排序下比较"
  - "**两种回渗的机理不同，这是全篇的骨架**：**Closed Cradle Rewet（CCR）由解吸（desorption）驱动**——来源是**摄入系统里的残液**；**High Pressure Rewet（HPR）由回流（flowback）驱动**——来源是**芯体里松散持留的液体**。因此**保液容量（Ret Cap）在 GRIFFIN 里怎么调都不影响 CCR**，却显著影响 HPR"
  - "**绒毛浆是回渗的一等因子，但方向相反**：**多加浆降低 LPR、却可能升高 HPR**；**把 SAM 掺进绒毛浆（SAM in Fluff, SiF）一般降低 HPR**（MAMBA 汇总中 SiF 对 HPR 的 Logworth 达 9.179，p≈0）——但**在 Depend GRIFFIN 的 CCR 上却反向升高了回渗（0.34 → 0.38 → 0.40 g）**，该现象至今无解释"
  - "**因子排序（MAMBA 全量汇总）**：LPR 由 **SAM 类型（7.057）> 浆量（6.725）> SAM 总量（3.052）> 垫长（2.955）> 垫容量（2.884）** 主导；HPR 由 **SAM 类型（25.749）> 垫容量（20.815）> 浆内 SAM（9.179）> SAM 总量（9.051）> 浆量（8.220）** 主导——**HPR 是 SAM 的游戏，LPR 是浆的游戏**"
  - "**毛细测试提供了机理旁证**（2025-07，GRIFFIN 产品，为排除 SAM 干扰而做成无 SAM 样品）：**有浆时解吸能更高、更难"晾干"，且截留更多残液**——两条同时指向「浆把液体留在摄入系统里，之后以解吸形式回到面层」"
  - "**保液容量对照表**：容量 450 / 550 / 763 g 对应的回渗为 ATH 0.28 / 0.31 g，SAM/Fluff 0.33（变异大）/ 0.24 / 0.23 g——**同一容量档下两条芯体路线给出相反的排序**，说明「容量 ↔ 回渗」不是单调函数，取决于容量由浆还是由 SAM 提供"
  - "**浆形（Fluff Shape）影响弱且方向不一致**：MAMBA #1 中异形浆对 LPR 略好（Logworth 2.463）；MONEYBALL 中异形浆「对 LPR 略好、对 HPR 略差」；MAMBA #2 与 HUT 中基本无影响"
  - "**导流层（Surge）本身是一等因子**：BB DOE 中 LPR 的因子排序为 **浆量 17.042 > Surge 11.448 > SAM 总量 10.156**，即**在这套 DOE 里换导流层的影响大于调 SAM 总量**"
  - "**试验边界条件必须记录**：各 DOE 的 AT 胶（Focus T193 / Henkel 5402U）、胶添加量 4.0%、垫长 398–410 mm、AT 宽度 80/100/115 mm、LSE 有/无、包裹层 7 或 11 gsm SMS、导流层 MOJAVE / CT5 / LIFESAVERS 各不相同——**这是同一因子在不同 DOE 里排序摇摆的直接原因**"
pages_linked: ["[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]", "[[绒毛浆（Fluff Pulp）]]", "[[Rewet Test（回渗测试）]]", "[[Resilient Surge（PET 回弹导流层）]]", "[[巴斯夫欧洲公司（BASF SE）]]"]
---

# ADT Brain Trust - Fluff and Rewet（绒毛浆与回渗 DOE 复盘）

## 一句话定位 One-line positioning

本库**"回渗到底由谁决定"这个问题最系统的一份答案**：六套 DOE 一致地指向一条分工——**低压回渗（LPR / CCR）是绒毛浆与摄入系统的游戏，高压回渗（HPR）是 SAM 与容量的游戏**。它同时诚实地留下两个未解矛盾（SiF 在 CCR 上反向、容量排序在两条芯体路线上相反），是本批少见的"给出结论也给出无解"的资料。

## 摘要 Summary

**背景段**先立起两条已被长期观察但未解释的现象：① 在 BCC 中 **SAM 用量对高压回渗影响显著**，但成因未定（是"液体足迹不同"还是"被锁住的液体量不同"——Aaron 的 ATH DOE 确认该结论对 BB 亦成立）；② 在 GRIFFIN 中反复调整保液容量**看不到对 closed cradle 回渗的影响**。随后的解释是全篇的钥匙：**CCR 由解吸驱动（残液在摄入系统），HPR 由回流驱动（芯体中松散持留液）**，因此容量只影响后者。

**ATH 绒毛浆假说**：ATH 结构中回渗高于 SAM/Fluff，假说为「**在 ATH 里绒毛浆实际上是摄入系统的一部分**」，残液留在浆里再以解吸形式回来。2025 年 7 月的毛细测试给出旁证：为排除干扰而做成**不含 SAM** 的 GRIFFIN 样品，对比有浆/无浆——**有浆时解吸能更高、更难晾干，且截留残液更多**（两种包裹层 12 gsm dSB 与 20 gsm BCW 下趋势一致）。

**Depend GRIFFIN 的反例**：把 SAM 移进绒毛浆后，closed cradle 回渗**小幅升高**（Always Discreet 0.17 g → GRIFFIN ATH 0.34 g → 掺 30% 0.38 g → 掺 47% 0.40 g），与"掺 SAM 捕获残液"的假说**相反**；文中自问"也许是掺入量不足以让浆及时解吸？"但未定论。

**六套 DOE** 随后给出因子显著度排序（Logworth / p 值）与方向结论，并在末页汇总成一张 2×2 表。

## 提炼的数字与结论 Key figures & conclusions

### A. 机理分工：谁驱动哪一种回渗

| 回渗类型 Rewet type | 驱动机理 Mechanism | 液体来源 Where the fluid sits | 受容量影响？ |
|---|---|---|---|
| **Closed Cradle Rewet（CCR）** / 低压段 | **解吸 Desorption** | **摄入系统（intake system）内的残液** | **不受影响**（GRIFFIN 反复调容量无变化） |
| **High Pressure Rewet（HPR）** | **回流 Flowback** | **芯体内松散持留的液体** | 显著（容量越高 HPR 越低） |
| Low Pressure Rewet（LPR） | 与 CCR 同族（解吸） | 摄入系统 / 绒毛浆 | 方向与 HPR 相反 |
| Source | Background: Ret Cap & Rewet | 同上 | 同上 |

### B. 保液容量 ↔ 回渗（GRIFFIN）

| 容量 Capacity (g) | ATH 回渗 (g) | SAM/Fluff 回渗 (g) |
|---|---|---|
| 450 | 0.28 | 0.33（**变异大**） |
| 550 | 0.31 | 0.24 |
| 763 | — | 0.23 |

> ⚠️ 同一容量档下两条路线的排序相反（450 g 时 ATH 更低、550 g 时 SAM/Fluff 更低），**"容量 ↔ 回渗"不是单调函数**。

### C. 掺 SAM 进绒毛浆（SAM in Fluff / SiF）的矛盾

| 研究 Study | 指标 Metric | 结果 Result |
|---|---|---|
| Depend GRIFFIN（TTM-00672，closed cradle under pressure） | CCR | **升高**：对照 0.34 g → 掺 30% 0.38 g → 掺 47% 0.40 g（对照品 Always Discreet 0.17 g）— **与假说相反** |
| MAMBA 全量汇总 | HPR | **降低**：SiF 的 Logworth **9.179**，p ≈ 0 |
| MONEYBALL | HPR | **降低**：SiF Logworth 7.570（该 DOE 中 HPR 唯一显著因子） |
| BB DOE | LPR | **降低** |
| MAMBA #5 | LPR | **降低** |

> ⚠️ 同一动作（SiF）在 **CCR 上升高回渗、在 HPR/LPR 上降低回渗**——文件本身把这列为 **Why?** 未解项，**本库不做裁决**。

### D. 因子显著度排序 Factor ranking（Logworth，越大越显著）

| 因子 Source | MAMBA 汇总 – LPR | MAMBA 汇总 – HPR | MONEYBALL – LPR | MONEYBALL – HPR | BB DOE – LPR |
|---|---|---|---|---|---|
| SAM 类型 SAM Type | **7.057** | **25.749** | 0.284（不显著） | 0.851 | — |
| 绒毛浆量 Fluff (g) | **6.725** | 8.220 | **2.638** | 0.289 | **17.042** |
| SAM 总量 Total SAM (g) | 3.052 | 9.051 | 2.425 | 0.304 | 10.156 |
| 垫长 Pad Length (mm) | 2.955 | 0.717（不显著） | — | — | — |
| 垫容量 Pad Capacity (g) | 2.884 | **20.815** | 2.462 | 0.382 | — |
| 浆内 SAM SAM in Fluff (g) | 1.058 | **9.179** | 2.188 | **7.570** | — |
| AT 宽度 AT Width (mm) | 1.368 | 1.201（边缘） | 0.979（边缘） | 0.594 | — |
| 浆形 Fluff Shape | 1.136（边缘） | 2.381 | 2.280 | 1.588 | — |
| 导流层 Surge | — | — | — | — | **11.448** |

### E. 方向性结论（各 DOE 一致项）

| 变量 Variable | 方向 Direction | 出处 |
|---|---|---|
| **多加绒毛浆** | **降低 LPR**；**可能升高 HPR**（效应在低 MACH SAM 下更大） | MAMBA #2 / #5 / HUT / MONEYBALL / BB DOE / 末页汇总 |
| **把 SAM 掺进浆（SiF）** | **一般降低 HPR 或 LPR**（具体降哪一个在不同 DOE 间摇摆） | 末页汇总 |
| **提高垫容量** | **降低两者**（MAMBA 汇总）；但在 MAMBA #5 中"**提高容量降低 HPR 却升高 LPR**"；MONEYBALL 中仅小幅影响 | MAMBA #5 / MONEYBALL / 末页汇总 |
| **提高容量是降 HPR 的最大单一因子** | 归因于 **SAM**（增加用量或提高保液能力都降 HPR）；**增加浆反而可能升 HPR** | 末页汇总 |
| **浆形 Fluff Shape** | 影响弱、方向不一致（异形浆对 LPR 略好、对 HPR 略差） | MAMBA #1 / #2 / HUT / MONEYBALL |
| **LPR 由浆驱动、HPR 由 SAM 驱动** | 文件给出的最终归因 | 末页汇总（Ret Cap 行） |

### F. 各 DOE 的边界条件 Boundary conditions

| DOE | 关键固定条件 Fixed conditions |
|---|---|
| MAMBA #1 | AT 胶添加量 4.0%；垫长 410 mm；性别 Boy；**LSE: No**；导流层含 MOJAVE / LIFESAVERS / None |
| MAMBA #2 | Boy；垫长 398 mm；胶添加量 4.0%；LSE: No；胶种 Focus T193；**浆内无 SAM** |
| MAMBA #5 | 80 / 100 mm AT 宽度；垫长 365–398 mm；引入 SiF、降胶、提高 TZ 容量、THUNDER 垫长等变体 |
| MAMBA HUT | LSE: No；垫长 398 mm；浆内无 SAM；Focus T193；胶添加量 4.0%；导流层 **LIFESAVERS**；含 Boy/Girl 与高浆（6.12 g）对照 |
| MONEYBALL | Boy；LSE: No；垫长 405 mm；Focus T193；胶添加量 4.0%；导流层 **CT5**；含 MOJAVE vs CT5、80%/126gsm、80/100/115 mm 宽度、Henkel 5402U vs Focus T193 |
| BB DOE | **LSE: Yes**；包裹层 11 gsm SMS；**剔除 40 gsm 导流层的码**；导流层 MOJAVE；BASF 5620 与 Stkn 5660 交叉 |

> 🔴 **manual_review（2026-09-29）**：本资料为 **K-C 内部 DOE 原始数据与试产代号体系**（试验批号 53171 / 53183 / 53393 / 53173 / 53185 / S25-018xxx，方法编号 **TTM-00623**（Lo/Hi 压力回渗）、**TTM-00672**（closed cradle under pressure），以及**供应商材料牌号与内部代号对应**（BASF 5620、Stkn 5660、Stkn 2281、Focus T193、Henkel 5402U、MOJAVE / CT5 / LIFESAVERS））。属内部研发资产与供应商对应关系，**本页只登记因子方向、显著度与边界条件，不落逐码原始读数表**；原文留存 `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/03.25.26 - ADT Brain Trust - Fluff and Rewet.pptx.md`。**对外引用、宣称支持或向供应商披露前须经 R&E 与采购确认。**
> ⚠️ **抽取噪声 Parse note**：源文件为 PPT 抽取，多数图表以图片 alt 文本堆积呈现（如 Logworth 柱状图、回渗散点），仅末页汇总表与部分表格为规整文本；上表数值**以正文结论句与规整表格为准**，未从图片串推断数值。
> ⚠️ **日期说明 Date note**：文件名为 `03.25.26`，**标题页自标 4/1/26**；本页索引日期取标题页日期 **2026-04-01**。

## 与本库其它页面的关系 Relations

- 派生概念：[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]
- 已追加：[[绒毛浆（Fluff Pulp）]]（2026-09-29 追加：浆作为摄入系统一部分的解吸证据）
- 相关：[[Rewet Test（回渗测试）]]（TTM-00623 的载荷口径）、[[Resilient Surge（PET 回弹导流层）]]（MOJAVE / CT5 / LIFESAVERS 三种导流层在本页 DOE 中作为变量出现）、[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]（容量段的另一种判读）
- 供应商：[[巴斯夫欧洲公司（BASF SE）]]（BASF 5620 为本页多套 DOE 的 SAM 之一）

## 原文摘录 Original excerpts

- "Different rewet mechanism to HPR — Closed cradle rewet driven by desorption, so residual fluid in the intake system — High pressure rewet driven by flowback, so loosely held fluid in the core"（Background: Ret Cap & Rewet）
- "In ATH systems, we hypothesize fluff acts as part of the intake system so residual fluid can be left in the fluff and come back out as rewet."（Background: ATH Fluff & Rewet）
- "✓ When system has fluff, it's harder to desorb (dry out) which may lead to higher rewet / ✓ When the system has fluff, it traps more residual fluid which may lead to higher rewet"（Desorption Energy / Residual Fluid，July 2025）
- "Unexpected result – opposite the hypothesis"（Depend: GRIFFIN Testing）
- "More fluff reduces LPR, but increases HPR / Adding SAM to fluff reduces HPR / Fluff shape does not have a strong impact"（MAMBA Summary – Fluff）
- "More capacity overall reduces both LPR & HPR / LPR likely driven by fluff / HPR likely driven by SAM"（MAMBA Summary – Ret Cap）
- "Higher pad capacity is the biggest factor to reduce HPR — Due to the SAM – an increase in amount or ret cap reduces HPR — An increase in fluff may increase HPR"（Summary 末页）

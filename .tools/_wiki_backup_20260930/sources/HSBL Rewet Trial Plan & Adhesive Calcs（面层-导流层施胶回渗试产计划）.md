---
type: source
title: "HSBL Rewet Trial Plan & Adhesive Calcs（面层-导流层施胶回渗试产计划）"
source_type: 实验计划
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/Surge-Liner Interface/53267-HSBL-REWET-CLEMMER Trial Plan and Adhesive Calcs .xlsx.md
original_link: ""
date_published: 2025-10-17
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "文件性质 = **试产计划书 + 施胶工艺计算表**（试验编号 53267，责任人 Clemmer，主题 HSBL–回渗；文件夹位于 `Performance/Rewet/Rewet Fundamentals/Surge-Liner Interface/`）。含四个工作表：Code List（23 个码的逐项工艺参数）、Mini Code List、Sheet1（运行顺序与假设）、Trial Flow and Calcs（日程 + 喷嘴设定 + 胶流量/泵速/喷嘴出口速度计算）"
  - "**试验对象就是"面层—导流层界面"**：基材为 **74 mm CT5 导流层 + 12 gsm SB 面层**（个别码用 China Liner），胶施加在**导流层侧**（Substrate Applied To = Surge），**压合花型为 PICASSO**，粘合方式为 Pressure 或 None"
  - "**四条假设（逐变量）**：① 施胶花型——**覆盖率越高回渗越低**（面层-导流层连接更强），但**胶多也会堵住排液通道**；② 添加量——**添加量越高连接性越好、回渗越低**；③ 胶种——**表面能会影响回渗**（假设尚需定义）；④ 压合花型——提供面层-导流层连接，但**同时压扁导流层，因此可能有利也可能有害**"
  - "**变量矩阵**：胶种 **Henkel 5402（DM5402U）vs Rextac RT-8723**；添加量 **1.7 / 2.8 / 3.9 gsm**（对应 0.02635 / 0.0434 / 0.06045 g/片）；喷嘴 **Signature(低流量) / Summit(标准) / Rhythym(低流量) / Minibead / CF Swirl / Slot Coat**；压合 **PICASSO vs 无**"
  - "**固定工艺条件**：线速 **246 fpm**、节拍 **305 mm**、车速 **300 片/分**、胶温 **325（°F）**、压合压力 **70 psi**、开模距离 45 mm、图案气 15–45 psi、喷嘴-纤网距离 25–40 mm（Minibead 为 touching web）"
  - "**喷嘴出口速度差异极大**：同在 3.9 gsm 下，**CF Swirl（1 孔、ø0.02 in）出口速度约 10,952 cm/min**，而 **Minibead（14 孔、ø0.03 in）仅约 348 cm/min**——**相差约 30 倍**。这是同一流量下不同喷嘴类型的本质差别，也是"换喷嘴 = 换雾化状态"的原因"
  - "**胶的密度差决定泵速**：RT-8723 密度 **0.83 g/cc**、DM5402U 密度 **0.92 g/cc**；同样 3.9 gsm 下泵速分别为 **18.15 RPM** 与 **16.59 RPM**——**换胶种必须重算泵速，不能沿用设定值**"
  - "**计算链条完整**：62 mm(CD) × 250 mm(MD) = 15,500 mm² 施胶面积 → 按 gsm 得 g/片 → 乘 300 片/分得 g/min → 除以（泵排量 × 密度）得泵速；再由每喷嘴孔数与孔径算出口速度"
  - "**验证手段明确**：Peel testing（剥离）、Capillarity（毛细）、MicroCT（显微 CT）三项线下测试 + 主要依赖目视的在线检查"
pages_linked: ["[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]", "[[Liner-Surge Embossing（面层-导流层压花）]]", "[[汉高]]", "[[Rextac（APAO 热熔胶）]]", "[[Resilient Surge（PET 回弹导流层）]]"]
---

# HSBL Rewet Trial Plan & Adhesive Calcs（面层-导流层施胶回渗试产计划）

## 一句话定位 One-line positioning

本库**"面层—导流层界面"这一层的施胶工艺与回渗假设的完整试验设计**：它把「为什么要在这一层施胶」（提升连接性 → 降回渗）与「施胶可能带来的两个反作用」（堵排液通道、压扁导流层）明确写成四条可证伪的假设，并配一套可直接上机的**流量—泵速—喷嘴速度计算表**。与 [[Liner-Surge Embossing（面层-导流层压花）]] 是同一界面的两种结合机制（压花 vs 施胶）。

## 摘要 Summary

**Code List** 给出 23 个码（含 6B / 11B / 15B / 17B 变体）的逐项参数：日期时间（2025-10-13 13:15 至 10-15 10:50）、优先级（1 号 B、17 号 **A+ control**、其余多为 C）、线速、节拍、主/副基材、胶种、胶温、施胶侧、添加量（gpp 与 gsm）、泵速、三个工位的喷嘴（OP / Center / DR）、喷嘴孔径、喷嘴-纤网距离、图案气压力与温度、粘合方式、压合花型、压合压力、开放时间。

**Mini Code List** 把 23 个码压缩为八列，可直接看出变量组合结构：**CT5 导流层 + 12 gsm SB 面层**为固定基材对，**胶种 × 添加量 × 喷嘴 × 是否压合**为四个变量；其中 6B / 11B 是**把施胶侧互换**（面层为主基材、导流层为副基材）的对照，**17B** 把副基材换成 China Liner。

**Sheet1** 给出 18 条运行顺序（OG run order 对应原码号），并在右侧列出试验前的开放问题：施胶幅宽（74 mm 卷材、62 mm 施胶）、目标车速（300 ppm，导流层长 250 mm）、胶施加在哪一侧（通常导流层）、各变量的假设、**换码之间的调整时间**、喷嘴类型是否纳入 mini-bead / Rhythym、导流层放卷与卷绕处理（Brian 之前跑过）、工艺设定起点（Derek 给建议）、**测试计划（剥离 / 毛细 / MicroCT）**、在线检测（主要目视）、贴合机参数（参照 GML 上跑的）、具体孔径选择（Derek 给建议）。

**Trial Flow and Calcs** 给出 5 天日程（10/13 胶路准备与卷绕调试各 4 h；10/14 Henkel 码 8 h；10/15 冲洗切换 RT8723 8 h；10/16–10/17 REXtac 码 8 h + 4 h），喷嘴设定表（含 Nordson 件号），以及两套胶（RT8723 与 DM5402U）的流量、泵速与喷嘴出口速度计算。

## 提炼的数字与结论 Key figures & conclusions

### A. 固定工艺条件与变量矩阵

| Item 项目 | 内容 Content |
|---|---|
| 主基材 Primary substrate | **74 mm CT5 导流层**（CT5 = 100% PET 回弹导流层，见 [[Resilient Surge（PET 回弹导流层）]]） |
| 副基材 Secondary substrate | **12 gsm SB 面层**（17B 码用 China Liner） |
| 施胶侧 Applied to | **导流层侧（Surge）** |
| 线速 / 节拍 / 车速 | **246 fpm / 305 mm / 300 片/分** |
| 胶温 Adhesive temp | **325（°F，源表未标单位）** |
| 添加量 Add-on | **1.7 / 2.8 / 3.9 gsm**（= **0.02635 / 0.0434 / 0.06045 g/片**） |
| 压合 Bonding | **Pressure（花型 PICASSO）** 或 **None**（花型 None）；压合压力 **70 psi** |
| 喷嘴类型 Nozzle | Signature（低流量）/ Summit（标准）/ Rhythym（低流量）/ Minibead / CF Swirl / Slot Coat |
| 胶种 Adhesive | **Henkel 5402（DM5402U）** 与 **Rextac RT-8723** |
| 图案气 / 喷嘴距离 | 15–45 psi（视喷嘴而定）/ 25–40 mm（Minibead 为 touching web） |

### B. 四条假设 Hypotheses（逐变量）

| 变量 Variable | 假设 Hypothesis | 内含的反作用 Counter-effect |
|---|---|---|
| 施胶花型 Pattern | **覆盖率越高 → 回渗越低**（面层-导流层连接更强） | **胶多也会堵住排液通道** |
| 添加量 Add-on | **添加量越高 → 连接性越好 → 回渗越低** | — |
| 胶种 Adhesive type | **表面能会影响回渗**（原文注明"可能需要进一步定义"） | — |
| 压合花型 Bond pattern | 提供面层-导流层连接 | **同时压扁导流层，因此可能有利也可能有害** |

### C. 胶流量与泵速计算 Adhesive flow & pump speed

| 项 Item | 1.7 gsm | 2.8 gsm | 3.9 gsm |
|---|---|---|---|
| 施胶面积 Area (mm²) | 15,500（62 CD × 250 MD） | 15,500 | 15,500 |
| 克/片 g/product | **0.02635** | **0.0434** | **0.06045** |
| 流量 Flow (g/min) | **7.905** | **13.02** | **18.135** |
| RT-8723（ρ = **0.83 g/cc**，泵 1.204 cc/rev）泵速 RPM | 7.91 | 13.03 | **18.15** |
| DM5402U（ρ = **0.92 g/cc**，泵 1.188 cc/rev）泵速 RPM | 7.23 | 11.91 | **16.59** |

> ⚠️ **换胶种必须重算泵速**：两种胶密度差约 10%（0.83 vs 0.92 g/cc），同 gsm 下泵速差约 9%（18.15 vs 16.59 RPM）。沿用旧设定会直接造成添加量偏差。

### D. 喷嘴出口速度对比 Nozzle exit velocity（同一流量下，差异极大）

| 喷嘴 Nozzle | 孔径 Orifice (in) | 孔数/喷嘴 | 1.7 gsm 速度 (cm/min) | 2.8 gsm | 3.9 gsm |
|---|---|---|---|---|---|
| **CF Swirl** | 0.02 | 1 | 4,774 | 7,863 | **10,952** |
| Summit（标准） | 0.018 | 4 | 1,474 | 2,427 | 3,380 |
| Rhythym（低流量） | 0.012 | 5 | 1,250 | 2,059 | 2,867 |
| Signature（低流量） | 0.012 | 12 | 521 | 858 | 1,195 |
| Slot Coat | 1 mm（0.0394 in） | 10 | 467 | 769 | 1,071 |
| **Minibead** | 0.03 | 14 | 152 | 250 | **348** |

> ⚠️ **同一流量下 CF Swirl 与 Minibead 的出口速度相差约 30 倍**（10,952 vs 348 cm/min）。孔数少、孔径小的喷嘴必须靠极高速度送出同等流量——这直接决定雾化状态、纤网穿透与开放时间，**因此"换喷嘴"不是等效替换**。

### E. 喷嘴设定与日程

| 喷嘴 Nozzle | 孔径 (in) | 喷嘴高度 | 图案气 (psi) | Nordson 件号 Part # |
|---|---|---|---|---|
| Signature – 低流量 | 0.012 | 50 | 45 | (2) 全幅 #1095242 + (1) 半幅 #1095240 |
| Summit – 标准 | 0.018 | 20 | 15 | (2) 全幅 #1035886 + (1) 半幅 #1035879 |
| Rhythym – 低流量 | 0.012 | — | — | — |
| Minibead | 0.03 | — | — | (1) #1073201 + (2) #1066314 |
| CF Swirl | 0.02 | — | — | (2) 全幅 #1095242 + (1) 半幅 #1095240 |

| 日期 Date | 活动 Activity | 时长 Duration (h) | 备注 Comments |
|---|---|---|---|
| 2025-10-13 | 胶路准备 Adh Setup | 4 | 用 DM5402 冲洗；在各添加量档位校核添加量 |
| 2025-10-13 | 卷绕准备 Web Setup | 4 | 优化走带张力；安装 PICASSO 压合花型 |
| 2025-10-14 | Henkel 码 | 8 | 换喷嘴、改添加量、开/关压合 |
| 2025-10-15 | 冲洗切换 RT8723 | 8 | 冲洗施胶机、换滤芯、再冲洗 |
| 2025-10-16 | REXtac 码 | 8 | 换喷嘴、改添加量、开/关压合 |
| 2025-10-17 | REXtac 码 | 4 | 机动时间；清理 |

> 🔴 **manual_review（2026-09-29）**：本资料为 **K-C 内部试产计划与工艺参数**（试验编号 53267、码号体系、供应商胶种与 Nordson 件号、产线工艺窗口与泵速设定）。属内部工艺资产，**本页只登记变量结构、计算链条与方向性结论，不落可作为产线作业指导的完整设定卡**；原文留存 `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Rewet Fundamentals/Surge-Liner Interface/53267-HSBL-REWET-CLEMMER Trial Plan and Adhesive Calcs .xlsx.md`。**产线引用或向供应商披露前须经工艺与采购确认。**
> ⚠️ **抽取噪声 Parse note**：源文件为 Excel 抽取，Code List 表存在**空列与列错位**（表头 24 列但内容列数不齐），部分行的"Tip-Web Distance / Pattern Air / Nip Pressure"与码号并非严格对齐；本页的**变量矩阵与计算表取自结构规整的 Mini Code List 与 Trial Flow and Calcs 两表**，未从错位行推断数值。
> ⚠️ **术语说明 Terminology**：**HSBL** 为该试验的项目代号，**原文未展开其全称**，本页不作推断；胶温 325 未标单位，依工艺惯例为 **°F**（约 163 ℃），标 `[待验证]`。

## 与本库其它页面的关系 Relations

- 派生概念：[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]
- 同界面另一机制：[[Liner-Surge Embossing（面层-导流层压花）]]（压花 vs 施胶）
- 供应商：[[汉高]]（Henkel 5402 / DM5402U）、[[Rextac（APAO 热熔胶）]]（RT-8723）
- 基材：[[Resilient Surge（PET 回弹导流层）]]（CT5 = 100% PET）
- 判读前提：[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]（本试验的回渗读数须先声明是哪一个口径）

## 原文摘录 Original excerpts

- "Higher coverage will yield lower reset because of higher liner-surge connection; but more adhesive may also block drainage"（施胶花型假设）
- "Higher add-on yield higher connectivity, thus lower rewet"（添加量假设）
- "Surface Energy will impact rewet…may need more definition"（胶种假设）
- "Liner-surge connectivity, but also compresses surge so could help or hurt"（压合花型假设）
- "Testing Plan | Peel testing; Capillarity, MicroCT"（Sheet1 右栏）
- "Tweak Run Order (Adh Type, Pattern, Bonder, Then Add-on)"（运行顺序策略：先胶种 → 花型 → 压合 → 最后添加量）
- "Bonder setup parameters | reference what is run on GML"（贴合机参数参照 GML 产线）

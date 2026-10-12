---
type: source
title: "SAP Four Core Metrics Breakdown（SAP 四大核心指标拆解 CRC_AUL_GBP_Vortex）"
source_type: 提案
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP四大核心指标拆解与说明.docx.md
original_link: ""
date_published: 2026-09
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "CRC is the theoretical ceiling under no load; AUL is the real-world retention under body weight — AUL/CRC ratio is 0.6-0.7 for premium SAP versus 0.4-0.5 for standard（中文：CRC 是理论天花板，AUL 是实战保水力；高端 AUL/CRC 0.6–0.7，普通 0.4–0.5）"
  - "GBP/SFC is the hidden boss metric: CRC and AUL only measure a single insult, while diapers see 5-8 insults per day; blocked gel bed causes 'no leak early, leak later'（中文：GBP/SFC 是隐藏 boss 指标——前几次不漏、后面必漏的根因是凝胶床堵塞）"
  - "Vortex versus AUL is the core SAP design conflict, resolved by a crosslink gradient: low crosslink core for speed plus high crosslink shell for retention（中文：Vortex 与 AUL 是核心矛盾，解法是交联梯度——内层低交联快吸、外层高交联保水）"
  - "Selection thresholds: premium diaper AUL >= 28 g/g at 0.7 psi plus Vortex <= 35 s plus SFC >= 30; mainstream AUL >= 24 g/g, Vortex <= 45 s, SFC >= 15（中文：选型门槛——高端 AUL≥28（0.7 psi）+ Vortex≤35 s + SFC≥30；主流 AUL≥24 + Vortex≤45 s + SFC≥15）"
  - "Bio-based SAP currently trails petroleum-based by 20-30% on AUL and 20-50% on CRC（中文：生物基 SAP 当前 AUL 低 20–30%、CRC 低 20–50%）"
pages_linked: ["[[SAP性能指标（CRC AUL GBP Vortex）]]", "[[SAP（高吸水树脂）]]", "[[Gel Blocking（凝胶阻塞）]]", "[[SAP 表面包覆（SAP Particle Surface Coating）]]", "[[Biodegradable SAP（可降解高吸水树脂）]]", "[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]"]
---

# SAP Four Core Metrics Breakdown（SAP 四大核心指标拆解 CRC/AUL/GBP/Vortex）

## 一句话定位 One-line Positioning

本批**SAP 四指标的测试口径 + 典型值 + 相互取舍的系统拆解**（基于知识库 SAP 技术总结报告、生物基 SAP 研究报告及行业公开资料整理）：把 CRC / AUL / GBP(SFC) / Vortex 从"读数字"升级为"懂取舍"。是本库回答「SAP 选型门槛与指标冲突」的口径底稿。

## 摘要 Summary

**CRC（Centrifuge Retention Capacity，离心保留容量）**：SAP 在无压力自由吸液后经离心脱去未结合水，每克干树脂保留的液体克数。茶袋法 / EDANA ERT 441.2——称 W1 克 SAP 入茶袋，浸入 0.9% NaCl 30 分钟自由吸液，250 g 离心 4 分钟，称重 W3，CRC = (W3 − W2 − W1)/W1。典型值：纸尿裤普通级 30–40 g/g（釜式/带式）、高端级 40–50 g/g（釜式 + 表面交联优化）、生物基 20–40 g/g（比石油基低 20–50%）、纯水测试 300–1000 g/g（**不代表实际使用性能**）。关键提醒：CRC 是"理论天花板"，纸尿裤实际使用中 SAP 受压，**CRC 高不代表真能吸这么多；CRC 是基础，AUL 才是实战**。CRC 偏低常见原因：内交联密度过高（网络空间小）、表面交联过度（吸液慢、30 分钟未达平衡）、粒径偏大（比表面积小）。

**AUL（Absorbency Under Load，载荷下吸收量）**：特定压力下吸液后每克干树脂保留的液体克数，模拟宝宝坐/躺压在纸尿裤上的真实工况。EDANA ERT 442.1：W1 克 SAP 置带孔平底圆柱容器，施规定压力（0.3 / 0.7 / 0.9 psi），底部接触 0.9% NaCl 吸液 60 分钟，AUL = (W3 − W1)/W1。典型值：0.3 psi（约 2.1 kPa）普通 25–30 / 高端 30–35 g/g（轻压、坐姿瞬间）；**0.7 psi（约 4.8 kPa）普通 18–25 / 高端 25–30 g/g（纸尿裤核心指标，宝宝体重压迫）**；0.9 psi（约 6.2 kPa）普通 15–20 / 高端 20–25 g/g（重压、学步期集中受力）。行业标准：0.7 psi 下 **AUL ≥25 g/g 为合格、≥28 g/g 为优质**。AUL 是 CRC 的"打折版"，AUL/CRC 越接近 1 说明加压后保水越强——高端可达 0.6–0.7，普通仅 0.4–0.5。**AUL 偏低 = 反渗**（宝宝坐着时尿液被压回面层，红屁屁元凶）。提升手段：表面交联形成致密壳层（受压时凝胶不塌陷）、内交联剂引入刚性基团构建支撑骨架、无机纳米材料掺杂（蒙脱土 MMT 作物理交联点，凝胶强度可提升 50%+）。

**GBP / SFC（Gel Bed Permeability，凝胶床渗透性 / Saline Flow Conductivity）**：SAP 吸液溶胀后形成凝胶层，液体透过该凝胶层的速率，衡量"第一次吸完后后续尿液还能不能穿过去"。EDANA ERT 470.2：定量 SAP 置特制圆柱容器，施 0.3 psi 吸 0.9% NaCl 至饱和，维持压力从顶部持续注入盐水，测单位时间透过量，SFC = K × (Q/ΔP)，单位 ×10⁻⁷ cm³·s/g。典型值：普通 SAP 5–15（凝胶堵死）、高端 20–40（保持通透）、超高端（多孔/复合交联）40–70（几乎不阻塞）。GBP 是"隐藏 boss 指标"的原因：CRC 与 AUL 都只测单次吸收，而宝宝一天排尿 5–8 次，第 3、5 次尿液到达时 SAP 已膨胀成凝胶；凝胶互相粘连堵死通道则后续尿液无法穿透，只能从侧边漏出——**这就是"前几次不漏，后面必漏"的根本原因**。提升手段：二次/多重表面交联（保持颗粒独立性防粘连）、不规则颗粒形态（堆积形成毛细缝隙，釜式工艺天然优势）、添加纳米 SiO₂ 等"隔离珠"、控制粒径分布（粗细搭配、粗颗粒形成骨架通道）。

**Vortex（涡流时间）**：SAP 接触液体后吸收至液面漩涡消失所需时间，直接反映吸液速度。行业通用（非 EDANA 标准）：50 mL 0.9% NaCl 入烧杯，加 1 g SAP，磁力搅拌 500–600 rpm，记录漩涡完全消失的时间。评级：**≤30 s 极快（高端纸尿裤首次瞬吸关键）**、30–45 s 快（纸尿裤标准要求）、45–60 s 中等（卫生巾、成人失禁）、>60 s 慢（农业保水剂）。Vortex 慢的后果：尿液不能即时锁定、沿导流层扩散到边缘、面层湿感时间延长、与 ADL 不匹配。影响因素：粒径小→更快；表面交联过度→更慢；多孔结构→更快；内交联密度高→更慢。**Vortex 与 AUL 的 trade-off 是 SAP 设计最核心的矛盾**——要快就要粒径小、表面交联浅，但 AUL 低；要 AUL 高就要表面交联深，但 Vortex 慢；解法是**内层低交联（快吸）+ 外层高交联（保水）的表面交联梯度设计**，这也是釜式工艺的核心优势。

四指标联动链：CRC（理论天花板）→ AUL（实战保水力，**决定反渗**）→ GBP（多次吸收通透性，**决定漏尿**）→ Vortex（首次响应速度，**决定瞬吸干爽感**）。四组矛盾取舍：CRC vs AUL（交联度↑→CRC↓AUL↑，高端牺牲 5–10% CRC 换 AUL）、Vortex vs AUL（梯度交联解耦）、GBP vs CRC（同向）、Vortex vs GBP（粒径小→Vortex 快，但细粉多→GBP 可能下降）。选型一句话：**高端纸尿裤 AUL ≥28 g/g（0.7 psi）+ Vortex ≤35 s + SFC ≥30；主流 AUL ≥24 g/g + Vortex ≤45 s + SFC ≥15；生物基 SAP 当前 AUL 比石油基低 20–30%，需重点攻关**。附录另列凝胶强度（普通 ≥500 Pa、改性复合型数千 Pa）、保水性（5.5 kPa 下 ≥85%）、粒径分布（纸尿裤常用 150 μm–1.4 mm）、残留单体（国标 ≤800 mg/kg、一线品牌 ≤300 ppm）、pH 6–8、可萃取物（釜式工艺显著低于带式）。

## 提炼的数字与结论 Key Numbers and Conclusions

| 项目 Item | 数值 / 结论 Value / Conclusion | 备注 Note |
|---|---|---|
| CRC 测试法 | 茶袋法 / EDANA ERT 441.2；0.9% NaCl、30 min、250 g 离心 4 min | CRC=(W3−W2−W1)/W1 |
| CRC 典型值 | 普通级 30–40；高端级 40–50；生物基 20–40 g/g | 纯水 300–1000 g/g **不代表实用** |
| AUL 测试法 | EDANA ERT 442.1；0.3 / 0.7 / 0.9 psi；0.9% NaCl、60 min | 压力必须随值标注 |
| AUL 0.3 psi（~2.1 kPa） | 普通 25–30；高端 30–35 g/g | 轻压、坐姿瞬间 |
| **AUL 0.7 psi（~4.8 kPa）** | **普通 18–25；高端 25–30 g/g** | **纸尿裤核心指标**；≥25 合格、≥28 优质 |
| AUL 0.9 psi（~6.2 kPa） | 普通 15–20；高端 20–25 g/g | 重压、学步期 |
| AUL/CRC 比 | 高端 0.6–0.7；普通 0.4–0.5 | 越接近 1 越强 |
| GBP/SFC 测试法 | EDANA ERT 470.2；0.3 psi 饱和后持续注盐水 | 单位 ×10⁻⁷ cm³·s/g |
| SFC 典型值 | 普通 5–15；高端 20–40；超高端 40–70 | 隐藏 boss 指标 |
| Vortex 评级 | ≤30 s 极快 / 30–45 s 快 / 45–60 s 中等 / >60 s 慢 | 50 mL 液 + 1 g SAP、500–600 rpm |
| **高端选型门槛** | **AUL ≥28（0.7 psi）+ Vortex ≤35 s + SFC ≥30** | — |
| **主流入选门槛** | **AUL ≥24 + Vortex ≤45 s + SFC ≥15** | — |
| 生物基差距 | AUL 低 20–30%；CRC 低 20–50% | 需重点攻关 |
| 多次吸收场景 | 宝宝一天排尿 5–8 次 | GBP 失守 = "前几次不漏、后面必漏" |
| 凝胶强度 | 普通 ≥500 Pa；改性复合型数千 Pa | MMT 掺杂可 +50% |
| 保水性 | 5.5 kPa 下 ≥85% | — |
| 粒径分布 | 150 μm–1.4 mm（纸尿裤常用） | — |
| 残留单体 | ≤800 mg/kg（国标）；≤300 ppm（一线品牌） | 安全口径 |
| 可萃取物 | 釜式工艺显著低于带式工艺 | 工艺差异 |

> ⚠️ **单位警示（2026-09-29）**：本页 SFC/GBP 以 **×10⁻⁷ cm³·s/g** 给出，而本库多数来源以 **Darcy** 给出；**两套单位不可直接换算**，跨页比较 GBP 前须先统一单位与测试条件。

## 关键论断（key_claims）

- **CRC 是天花板、AUL 是实战：选型不能只看吸收倍率** —— 支撑页：[[SAP性能指标（CRC AUL GBP Vortex）]]
- **GBP/SFC 决定"后面必漏"，是多次吸收场景的唯一解释变量** —— 支撑页：[[Gel Blocking（凝胶阻塞）]]
- **Vortex–AUL 矛盾的唯一解法是交联梯度（内层低 + 外层高）** —— 支撑页：[[SAP 表面包覆（SAP Particle Surface Coating）]]
- **AUL 偏低直接转化为回渗：这是 SAP 指标与皮肤健康的因果链** —— 支撑页：[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]
- **生物基 SAP 的差距是定量的（AUL −20~30%、CRC −20~50%），不是"能不能做"的问题** —— 支撑页：[[Biodegradable SAP（可降解高吸水树脂）]]

## 关联页面

- 概念：[[SAP性能指标（CRC AUL GBP Vortex）]]、[[SAP（高吸水树脂）]]、[[Gel Blocking（凝胶阻塞）]]、[[SAP 表面包覆（SAP Particle Surface Coating）]]、[[Biodegradable SAP（可降解高吸水树脂）]]、[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]
- 实体：（本页未落具名供应商规格）
- 对比：[[SAP 四牌号性能对比（KC511 vs NR-610S vs NR-950 vs Code X）]]、[[Super Absorbent Fibre（超吸水纤维 SAF）]] 相关对比见 [[SAF vs SAP（超吸水纤维 vs 高吸水树脂）]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP四大核心指标拆解与说明.docx.md`
- 原文链接：（无；基于知识库 SAP 技术总结报告、生物基 SAP 研究报告及行业公开资料整理）

---
type: source
title: "ATH SAM Relocation（2025-07-29 · 解吸能量·残液·microCT 与 SAM 再分配台架）"
source_type: 内部研究报告 + 台架结果（GRIFFIN Rewet · ActivTech Hybrid 专项）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.07.29 - ATH SAM Relocation.pptx.md
original_link: ""
date_published: 2025-07-29
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "总假设：AT hybrid 芯体产品的回渗将**持平或高于** SAM/绒毛浆产品，因为**绒毛浆层属于摄入系统**，摄入系统（含绒毛浆）中滞留的任何液体都可能被表达为回渗"
  - "三条基础工具假设全部 Supported：① AT hybrid 的**解吸能量**高于 SAM/绒毛浆（归因于摄入系统多出的层）；② AT hybrid 摄入系统的**残液质量**更高；③ **microCT** 显示含绒毛浆的摄入系统比 LSE 有额外湿润"
  - "解吸能量实测（ergs）：Code 31 WAS 6.67E+04、Code 32 WAS 6.52E+04；Code 31 LSE+CW(12gsm dSB) 1.83E+04、Code 32 LSE+CW(20gsm TABCW) 1.78E+04 —— 完整摄入系统约为 LSE+CW 的 3.6 倍"
  - "**20 gsm TABCW 被测出是疏水的（hydrophobic）**——这是本次基础测试的一个独立发现"
  - "第四条假设'MicroCT 不会显示 AT hybrid 面层湿润度与 LSE 或商品 Depend 有明显差异'为 **Likely Supported，待跟进**"
  - "**SAM 再分配台架失败**：把 30% / 47% 的 SAM 重新分配到绒毛浆层后，Closed Cradle 回渗由 0.34 g 变为 **0.38 / 0.40 g**——不但没改善，反而更差；Always Discreet 为 0.17 g"
  - "台架同时显示：SAM 再分配**恶化了 Open Cradle 第 3 次摄入**（65.93 → 150.58 / 142.62 s），即把 SAM 移进绒毛浆层严重伤害了多次摄入"
  - "结论与处置：『Bench testing did not show improved rewet by relocating SAM into ActivTech hybrid fluff layer』；**GRIFFIN 已将 ActivTech Hybrid 移出范围（eliminated from scope）**，由 Kerry 与 Aaron Schilpp 跟进是否继续该工作"
pages_linked:
  - "ActiveTech Platform（ActiveTech 在线薄芯体平台）"
  - "Residual Fluid & Pore Stranding（残液与孔隙滞留）"
  - "MCCT Multi-Component Capillary Tension（多组分毛细张力测试）"
  - "REL增强层"
  - "Rewet Test（回渗测试）"
  - "Cradle Intake Test（Cradle 摄入测试）"
---

# ATH SAM Relocation（2025-07-29 · 解吸能量·残液·microCT 与 SAM 再分配台架）

> 一句话定位：**这是一份"机理全对、方案全错"的经典记录**——三条基础工具假设**全部被支持**（ATH 确实更容易回渗），但据此设计的对策（把 SAM 搬进绒毛浆层）**在台架上不但无效，反而更差**。（中文：它证明了**"机理正确"不等于"解法正确"**。）

---

## 摘要 Executive Summary

| 类别 | 内容 |
|---|---|
| **总假设** | **ATH 回渗持平或更高**，因为**绒毛浆层属于摄入系统**，摄入系统中滞留的液体都可能被表达为回渗 |
| **测试工具** | **毛细张力（desorption energy）、残液质量、microCT** |
| **基础结论** | 三条假设**全部 Supported**；第四条（面层湿润度无差异）**Likely Supported 待跟进** |
| **意外发现** | **20 gsm TABCW 是疏水的** |
| **对策** | 把 **30% / 47% 的 SAM 重新分配到绒毛浆层** |
| **台架结果** | **回渗由 0.34 g 变为 0.38 / 0.40 g —— 更差**；**Open Cradle 第 3 次摄入 65.93 → 150.58 / 142.62 s —— 严重恶化** |
| **处置** | **GRIFFIN 已将 ActivTech Hybrid 移出范围** |

---

## 提炼的数字与结论 Numbers & Conclusions

### 1. 术语定义（源文明写，是理解全篇的前提）

| 术语 | 定义 |
|---|---|
| **Whole Absorbent System（WAS，完整吸收系统）** | **Liner、surge、CW（芯体包覆）、pulp（绒毛浆）** |
| **LSE+CW** | **Liner/surge 压花 + 单层上部芯体包覆** |
| **Wrapped Core（包覆芯体）** | **带包覆的绒毛浆芯体** |

### 2. 假设 1：解吸能量（Supported）

**假设**：ATH 产品的**解吸能量高于** SAM/绒毛浆芯体产品，因为**摄入系统多出的层**滞留了可能被表达为回渗的液体。

| 产品 | 样品质量 (g) | **des1 解吸能量 (ergs)** |
|---|---|---|
| **Code 31 — Whole Absorbent System** | **0.42** | **6.67E+04** |
| **Code 32 — Whole Absorbent System** | **0.42** | **6.52E+04** |
| **Code 31 — LSE+CW，12 gsm dSB** | **0.21** | **1.83E+04** |
| **Code 32 — LSE+CW，20 gsm TABCW** | **0.21** | **1.78E+04** |

- **量级关系**：**完整吸收系统的解吸能量约为 LSE+CW 的 3.6 倍**（6.67E+04 / 1.83E+04 ≈ 3.64）。
- ⚠️ **样品质量不同**（**0.42 g vs 0.21 g，相差 2 倍**），**源文未说明是否已归一化** —— 见 manual_review。

### 3. 独立发现：**20 gsm TABCW 是疏水的**

- 源文单列一页标题：**「20gsm TABCW found to be hydrophobic」**，图注为 **53901-06, Wrapped Core, 20gsm TABCW**（对照 **53901-04, Wrapped Core, 12gsm dSB**）。
- **⇒ 同为包覆/增强层材料，12 gsm dSB 与 20 gsm TABCW 的润湿性并不等价**，选型时不能只按定量替换。

### 4. 假设 2：残液质量（Supported）

**假设**：ATH 摄入系统的**残液质量高于** SAM/绒毛浆芯体摄入系统（同样归因于多出的层）。**结论：Supported**。

### 5. 假设 3：microCT（Supported）

**假设**：**microCT 会显示含绒毛浆的摄入系统相对 LSE 有额外的湿润**（因为多出的层）。**结论：Supported**（对照：Code 31 / Code 32 的 **LSE + core wrap** 与 **Whole Absorbent System**）。

### 6. 假设 4：面层湿润度（Likely Supported，待跟进）

**假设**：**microCT 不会显示 ATH 的面层湿润度相对 LSE 或商品 Depend 有明显差异**。**结论：Likely Supported, pending follow up**（对照含 **Depend Image, May 2025** 与 **Code 32 WAS Liner**）。

### 7. SAM 再分配台架结果（K. Clemmer）

| 指标 | **Always Discreet** | **GRIFFIN ATH 12gsm dSB wrap 550g** | **+30% SAM 再分配至绒毛浆** | **+47% SAM 再分配至绒毛浆** |
|---|---|---|---|---|
| Open Cradle 1st Intake (s) | 15.33 | 20.87 | 17.78 | 17.25 |
| Open Cradle 2nd Intake (s) | 18.04 | 21.56 | **32.12** | **29.69** |
| **Open Cradle 3rd Intake (s)** | **34.80** | **65.93** | **150.58** | **142.62** |
| Closed Cradle 1st Intake (s) | 15.50 | 16.80 | 18.20 | 18.54 |
| Closed Cradle 2nd Intake (s) | 34.64 | 28.76 | 32.10 | 34.22 |
| Closed Cradle 3rd Intake (s) | 44.20 | 32.00 | 42.50 | 44.50 |
| **Closed Cradle Rewet (g)** | **0.17** | **0.34** | **0.38** | **0.40** |

**统计分组（All Pairs Tukey-Kramer）：**
- **Open Cradle（总体）**：ATH 550g = **A**；30% = **B**；47% = **B**；**AD = C**（AD 最快）。
- **Open Cradle 第 3 次**：30% **A 150.58**、47% **A 142.62**、ATH 550g **65.93**、**AD B 34.80**。
- **Closed Cradle 第 1 次**：47% A 18.54；30% A B 18.20；550g A B 16.80；AD B 15.50。
- **Closed Cradle 第 3 次**：47% A 44.50；AD A 44.20；30% A 42.50；**550g B 32.00**（唯一单独成组）。
- **Closed Cradle 回渗**：**AD B 0.17**；550g A B 0.34；**30% A 0.38**；**47% A 0.40**。

### 8. 结论与下一步（源文原话要点）

- **「Bench testing did not show improved rewet by relocating SAM into ActivTech hybrid fluff layer」**；
- **但解吸测试仍提示"给绒毛浆脱水（dewatering the fluff）"是一个好机理** —— 于是提出四个未解问题：**SAM 再分配为什么没做到这一点？时间尺度问题？其他原因？还能怎么切入？**
- **「GRIFFIN has eliminated ActivTech hybrid from scope」** —— 由 Kerry 与 Aaron Schilpp 跟进是否继续该项工作。
- **基础工具部分的结论**：ATH 可能因摄入系统的额外层数而**易感于更高回渗**；下一步是**与 ADT 跟进，确认基础测试结果是否与 ATH 产品测试相关**；**替代性的 ATH 设计可能改变本 deck 的结论**。

---

## 关键论断 Key Claims

1. **"绒毛浆属于摄入系统"是 ATH 回渗问题的根因假设** —— 一旦绒毛浆被划入摄入系统，**它滞留的液体就不再算"已吸收"，而算"可被表达为回渗"**。**⇒ 系统边界的划分直接改变回渗的归因与量级。**
2. **三条基础工具假设全部 Supported，这在方法上很重要** —— **毛细张力（解吸能量）、残液质量、microCT** 三条独立路径指向同一结论；**⇒ 多方法交叉验证成立时，结论可信度显著高于单一指标。**
3. **解吸能量把"回渗易感性"变成了一个可测的标量** —— **完整吸收系统 ≈ 3.6 倍于 LSE+CW**。**⇒ 回渗不再只能靠成品测试，可以在材料/组件层面用能量指标预筛。**
4. **但"机理正确"不等于"解法正确"** —— 解吸测试提示"**给绒毛浆脱水**"是好机理，于是把 SAM 搬进绒毛浆层；**结果回渗 0.34 → 0.38 / 0.40 g，更差**。**⇒ 机理指向的目标（脱水）与手段（加 SAM）之间缺少已验证的因果链。**
5. **失败发生在"多次摄入"而非"回渗"** —— **Open Cradle 第 3 次摄入 65.93 → 150.58 / 142.62 s（约 2.3 倍）**。**⇒ SAM 搬进绒毛浆层后，绒毛浆层的结构/渗透性被破坏，液体进不去了。**
6. **回渗与摄入在此处同向恶化** —— 这**打破**了"回渗↓ ⇒ 摄入↑"的常规权衡预期；**⇒ 当改动破坏了液体的进入通道时，两个指标会一起变差，而不是此消彼长。**
7. **"时间尺度"被列为未解问题之一** —— 源文明确提出 "**Time scale?**"；**⇒ 解吸是一个有时间常数的过程，"加 SAM 就脱水"隐含了"时间足够"的假设，而台架的等待时间可能不满足。**
8. **20 gsm TABCW 疏水是一个被单列的意外发现** —— **⇒ 同为芯体包覆/增强材料，定量相近不代表润湿性相同；"20 gsm TABCW 替换 12 gsm dSB"不是等价替换。**
9. **项目层面的处置比技术结论更值得记录** —— **GRIFFIN 已将 ATH 移出范围**，但**仍保留"是否继续"的跟进**。**⇒ 当一个方向在机理上成立、在工程上失败时，正确动作是降级而非立刻终止。**
10. **"替代性 ATH 设计可能改变结论"被显式声明** —— **⇒ 本结论的适用边界是"当前 ATH 设计"，不是"ATH 这一类芯体"。**

---

## 关联页面 Related Pages

- [[ActiveTech Platform（ActiveTech 在线薄芯体平台）]] —— **ATH 推高回渗的机理由"推断"升级为"三条工具 Supported"**；**SAM 再分配失败**；**GRIFFIN 已将 ATH 移出范围**。
- [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]] —— **残液质量**与**解吸能量**是该页"残液可被表达为回渗"的量化证据。
- [[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]] —— **毛细张力被用于测 desorption energy（ergs）**，是该测试方法的**一个具体应用实例**。
- [[REL增强层]] —— **20 gsm TABCW 被测出疏水**，对热风粘合增强层的选型是直接警示。
- [[Rewet Test（回渗测试）]] —— **Closed Cradle 回渗 0.17 / 0.34 / 0.38 / 0.40 g** 的量级与 Tukey-Kramer 分组口径。
- [[Cradle Intake Test（Cradle 摄入测试）]] —— **Open vs Closed Cradle 结论相反**：Open 第 3 次严重恶化（150.58 s），Closed 第 3 次 ATH 550g 反而最快（32.00 s，单独 B 组）。

---

## 原文 Raw Excerpt

> **总假设原文**：「AT hybrid core products will have **parity or higher rewet** than SAM/fluff products because **the pulp layer is part of the intake system**, any retained fluid in the intake system (including pulp) may be available to be expressed as rewet.」
>
> **测试方案原文**：「**Capillary tension, residual fluid mass and microCT** were used to explore desorption energy and fluid retention in the intake system.」
>
> **意外发现原文**：「**20gsm TABCW found to be hydrophobic**」
>
> **台架失败原文**：「**Bench testing did not show improved rewet by relocating SAM into ActivTech hybrid fluff layer**」「Desorption testing suggests **dewatering the fluff is still a good mechanism**. **Is SAM relocation not doing that for some reason? Time scale? Other causes?**」
>
> **处置原文**：「**GRIFFIN has eliminated ActivTech hybrid from scope.** Kerry to follow up with Aaron Schilpp to determine priority of continuing this work.」
>
> **边界声明原文**：「**Alternate AT Hybrid designs might alter the conclusions in this deck.**」

---

> 🔴 **manual_review（2026-09-29）**：
> 1. **⚠️ 解吸能量数据存在未控制的混淆** —— **WAS 样品质量 0.42 g，LSE+CW 样品质量 0.21 g，相差 2 倍**；**源文未说明解吸能量是否已按质量归一化**。**⇒ 3.6 倍的差异中有一部分可能仅来自样品质量，不得直接解读为"层数导致的能量差"。**
> 2. **⚠️ 回渗图的统计阈值在源文中不一致** —— 图注出现 "All Pairs Tulkey-Kramer **0.7**"（疑为 0.05 的识别错误）；**本页按 0.05 记录分组，但标注此疑点**。
> 3. **竞品数据** —— **Always Discreet 的摄入与回渗（0.17 g）**属**竞品内部实测，不外发**。
> 4. **内部项目与人事信息** —— 源文含 **GRIFFIN / ATH / ADT** 内部代号，以及**"Kerry 与 Aaron Schilpp 跟进"**的人事安排；本页**仅作追溯保留，不页面化为个人联系信息**。
> 5. **图表数值部分退化** —— 多张图注已退化为文本与重复数据串；**本页仅采用可明确辨读的表格与均值**，**未从图中臆测数值**。
> 6. **结论的适用边界** —— 源文自陈"替代性 ATH 设计可能改变结论"；**本结论仅适用于本次测试的 ATH 设计**。

> ✅ 验证（2026-09-29）：本页为新 source 页，无既有结论被覆盖；所有数字直引源文，未做换算或外推（**3.6 倍为本页据源文两值计算的比值，已标注为计算值**）。

---
type: source
title: "Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）"
source_type: 内部进展汇报（GRIFFIN Rewet 项目 · Informal Update）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.03.26 - Raegan Informal.pptx.md
original_link: ""
date_published: 2025-03-26
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "第一轮未达成超低回渗目标，但已识别出有改善的 code；方法论被明确定性为 'informed shotgun（有依据的散弹）'——把经验回连到设计原则，同时与 Virtual R&D 团队共同开发建模"
  - "面层（liner）：回渗随亲水处理量降低而单调下降（0.65% → 0.3% → 0% Lertisan）；bond area（18% Oval vs 10% CD Rod）无显著差异——H1 被否；代价是 closed cradle 摄入显著变差，泄漏风险上升"
  - "MicroCT 显示面层本身在持液 —— 回渗来源被定位到 intake system 的'解吸（desorption）'而非仅'回流（flowback）'"
  - "3D topical surge 回渗大幅更低；主假设是更低定量（basis weight），次假设是双层压花带来更连通的孔隙网络以排空顶层"
  - "60 gsm CT8 surge（Shalag 3）相对 CT5（ATACAMA）改善了回渗但牺牲了 closed cradle 摄入 —— 与 SIROCCO 的历史教训同构"
  - "ActivTech Hybrid（ATH）芯体回渗更高；'Core' 被定义为从包裹层（wrapsheet）往内的全部材料——材料更多、界面更多，持液点更多"
  - "建模能力缺口被量化：需要分辨占总液量 0.03% 的液体，'目前已验证的模型很可能不够精确'；ALBA 可能有用但需 GRIFFIN 实验验证，已排入 Virtual R&D 排期池"
pages_linked:
  - "Residual Fluid & Pore Stranding（残液与孔隙滞留）"
  - "LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）"
  - "Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）"
  - "ActiveTech Platform（ActiveTech 在线薄芯体平台）"
  - "Cradle Intake Test（Cradle 摄入测试）"
  - "亲水整理耐久性"
---

# Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）

> 一句话定位：**超低回渗项目第一轮的真实战绩汇报**——面层"少处理"确实降回渗，但**代价是 closed cradle 摄入变差**；同时把回渗机理从"芯体回流"重新定位到"面层解吸"。（中文：这一页的价值在于**明确了回渗的两个不同来源（Desorption / Flowback）及其各自的抓手**。）

---

## 摘要 Executive Summary

| 类别 | 内容 |
|---|---|
| **总体判断** | 第一轮**没有一击命中**，但**已找到有改善的 code** |
| **方法论** | **"informed shotgun"（有依据的散弹）** —— 把经验回连到设计原则；同时与 **Virtual R&D 团队**共同开发建模 |
| **面层结论** | 处理量越低回渗越低（**0.65% → 0.3% → 0% Lertisan**）；**bond area 无差异** |
| **面层代价（watchout）** | **closed cradle 摄入显著变差** → 泄漏风险上升 → **暴露在竞争宣称攻击下** |
| **新机会** | **MicroCT 显示面层自身持液**；**3D topical surge 回渗大幅更低** |
| **ATH 芯体** | **ActivTech Hybrid 回渗更高**；需进一步分析 |
| **时间线** | ADL 试产已完成；GML 试产 4 月底–5 月初；测试 5 月中下旬 |

---

## 提炼的数字与结论 Numbers & Conclusions

### 1. 面层实验矩阵（Fitesa 12 gsm SB）

| 材料 | Bond pattern | 处理量 | 假设 |
|---|---|---|---|
| Fitesa 12 gsm SB | **Oval bond (18%)** | 0.65% Lertisan | **Control** |
| Fitesa 12 gsm SB | CD Rod bond (10%) | 0.65% Lertisan | 更开放的 bond pattern = 更少小口袋滞留残液 |
| Fitesa 12 gsm SB | CD Rod bond (10%) | 0.3% Lertisan | 无处理 = 排斥残液（**摄入/泄漏风险需平衡**） |
| Fitesa 12 gsm SB | CD Rod bond (10%) | **0% Lertisan** | 无处理 = 排斥残液（**摄入/泄漏风险上升**） |

**结果（Closed Cradle Rewet，GRIFFIN SAM/Fluff 芯体）：**
- **回渗随处理量降低而降低**（单调）。
- **Bond area 不产生差异** —— "更开放 bond pattern 减少小口袋"的假设**未被支持**。

**摄入结果（Closed Cradle 1st Intake）：**
- **Open cradle 摄入与 control 相近**；
- **Closed cradle 摄入显著变差** —— 源文明示这是**竞争宣称风险敞口**。

### 2. 面层新发现（New Learning）

1. **3D topical surge 回渗大幅更低**，原因在查；**主假设 = 更低定量（basis weight）**。
2. **次要假设 = 层间更好的互连（interconnection）以解吸顶层**。
3. **量级事实**：**回渗重量远小于吸墨纸（blotter）**，且**在无压力下也有大量液体被带起** —— 说明**回渗的主要贡献者是"面层里本来就留着的液体"**，而非压力下从芯体挤出的液体。
4. **当前产品把液体留在最靠近 blotter 的最顶层**。
5. **假设**：**双层压花 topical surge** 可能具有**更连通的孔隙网络**，从而排空最顶层。

### 3. Surge 定量与摄入的历史类比

- **60 gsm CT8 surge（Shalag 3）** 相对 **CT5（ATACAMA）** 实现了**回渗改善**，但导致 **closed cradle 摄入更差**。
- 源文直指这与 **SIROCCO** 的历史教训**同构**："**found rewet solution at expense of closed cradle intake**"。
- 图中对照品牌/结构：Assurance、AD、ATACAMA、Shalag 3（Intake 1/2/3 多列，数值未从图文本中提取）。

### 4. ActivTech Hybrid（ATH）

- **ATH 芯体回渗更高**（Rewet – Core Type Comparison：Always Discreet (23.0309)、SAM/Fluff、ActivTech Hybrid 三组）。
- **核心定义被明确**：**"Core" = 从包裹层（wrapsheet）往内的全部材料** —— 因此 ATH 的摄入系统**包含 wrapsheet 与绒毛浆**。
- **机理归因**：不只是**更多材料**可持液，还有**更多界面（interfaces）**。
- **分析困难**：**SAM 存在时难以判断液体停在哪里**。
- **下一步样品矩阵（5 组，实验 + 成像诊断用）：**

| Wrapsheet | Fluff | SAM | 假设 |
|---|---|---|---|
| 12 gsm dSB | Standard | Standard | **Control ATH core** |
| 20 gsm BCW | Standard | Standard | 在湿芯体与 blotter 之间提供**缓冲** |
| 12 gsm dSB | Standard | **None** | 用于成像诊断液体位置 |
| 20 gsm BCW | Standard | **None** | 用于成像诊断液体位置 |
| 12 gsm dSB | **+30% SAM** | Standard | SAM 会解吸绒毛浆中的液体，否则这些液体将可用于 flowback |

### 5. 建模与竞争情报

- **P&G 专利版图（IP real estate）复盘**：发现很多思路；P&G 在**以整体系统视角思考"把液体驱动到想去的地方"**，与本团队当前思路相似；其中亦含**建模**方向。
- **建模精度缺口（关键量化）**：需要在**占总液量 0.03%** 的量级上检出差异；**"目前已验证的模型很可能不够精确"**。
- **ALBA 可能有用**，但**必须用 GRIFFIN 实验验证**；已加入 **Virtual R&D bullpen（资源空闲时排期）**。
- **AD（Always Discreet）面层分析**在进行中，结果 4 月出。

### 6. 附录：LUGH 面层（可迁移的测试卫生警告）

- LUGH 对面层的要求：**提升柔软度（HAPe）**，且**不加成本、不影响加工、不影响耐久性、**不增加摄入、**不增加回渗**（六个约束同时满足）。
- 候选：Fibertex 12 / 14 / 15 gsm soft SB。
- ⚠️ **对照组异常**：L14 RSR 的 **control 面层回渗异常高（0.25–0.30 g）**，高于预期；
- 追加测试后：**L14 整体回渗偏高**，原因是未知的"**某种所有 code 共有的固有因素**"；
- **多个 L14 批次**也测得**高于 L18**；
- **结论仍可相对比较**（相对 control 排序有效），**但绝对值不可跨批次比较**。
- 领先选项 **Fibertex 14 gsm soft SB 会轻微增加回渗**。

---

## 关键论断 Key Claims

1. **"回渗低"和"摄入好"在同一根处理量旋钮上方向相反** —— 面层亲水处理降低 → 回渗降低但 **closed cradle 摄入变差**；**这不是噪声，是机理**：面层越疏水，越不容易被"吸回去"，也越不容易把液体交出去。
2. **Basis weight 是本轮最强的单一杠杆** —— 3D topical surge 的回渗优势，第一假设不是材料改性而是**更低定量**；**"少即是多"在回渗上成立**。
3. **回渗来源要分成两笔账：Desorption vs Flowback** —— 面层自身持液（desorption，无压力也发生）与湿芯体受压回流（flowback）；**本轮发现主因偏向 desorption**，因此抓手从"改芯体"转向"排空面层/改层间互连"。
4. **"core"的定义决定了归因边界** —— ATH 把 **wrapsheet 与绒毛浆都算进 core**，于是"更多材料 + 更多界面 = 更多持液点"；**先定义系统边界，再谈谁更差**。
5. **建模不能只看"能不能跑"，要看"能不能分辨 0.03%"** —— 回渗是**极小量信号**（占总液量万分之三量级），**分辨率要求远高于一般吸收仿真**；这是一个**对模型可信度的硬指标**。
6. **SIROCCO 教训在复发** —— "找到回渗方案但牺牲 closed cradle 摄入"是**结构性重复失败模式**，不是个案；**项目立项时就应该把 closed cradle 摄入设为并列门槛**。
7. **批次/机台效应会污染回渗绝对值** —— L14 与 L18 的差异、多个 L14 批次整体偏高，说明**回渗测试存在批次级系统偏移**；**相对比较可用，绝对值跨批次不可比**。

---

## 关联页面 Related Pages

- [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]] —— "面层自身持液""更低定量""层间互连排空顶层"都落在该页的残液机理上。
- [[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]] —— "无压力下也带起大量液体"直接支持**低压（无压）通道**是主要贡献者。
- [[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]] —— 本页给出**可验证性硬门槛**：需分辨**总液量 0.03%**；现有模型"很可能不够精确"。
- [[ActiveTech Platform（ActiveTech 在线薄芯体平台）]] —— ATH 回渗更高 + core 定义（wrapsheet 以内）。
- [[Cradle Intake Test（Cradle 摄入测试）]] —— closed cradle 摄入变差是本轮的**代价项与竞争风险敞口**。
- [[亲水整理耐久性]] —— 处理量（0.65 / 0.3 / 0%）是回渗-摄入权衡的直接旋钮。
- [[Depend Ultra-Low Rewet M2M Learning Share（2025-04-22 面层与 ActivTech 芯体）]] —— 同项目的**后续（4 月）版本**，含进一步统计检验结论。
- [[Depend Rewet Update 2025-04-04（LUGH 与 GRIFFIN 回渗进展）]] —— 同期的 LUGH / GRIFFIN 进展页。

---

## 原文 Raw Excerpt

> **方法论原文**：「Approaching challenge with an **'informed shotgun'**」——「Connecting learnings back to principles to inform next steps with fundamentals where we can」「Exploring co-development with virtual R&D team on modeling」
>
> **面层结果原文**：「Rewet lowers as wettability treatment lowers」「**Bond area does not make a difference**」「Watchout of lower treatment is possibly increased leakage」「**Closed cradle worse than open**」
>
> **回渗来源原文**：「**Rewet weight is much smaller than the blotter. Much of the fluid picked up as rewet with no pressure on blotter.**」「Our current product leaves fluid in the topmost layer near the blotter.」
>
> **SIROCCO 类比原文**：「Similar to **SIROCCO** solutions that found rewet solution at expense of closed cradle intake」
>
> **建模门槛原文**：「Early indications is that currently vetted models are **likely not accurate enough (looking to detect 0.03% of total fluid)**」
>
> **ATH 定义原文**：「ActivTech hybrid core results in higher rewet」「**'Core' includes everything from the wrapsheet inwards**」

---

> 🔴 **manual_review（2026-09-29）**：
> 1. **K-C 内部项目资料**（GRIFFIN / SIROCCO / ATACAMA / MOJAVE / LUGH 等内部项目代号、内部试样结果）；本页**只记录机理与方向性结论**，**不记录任何未公开的商务条款或合作方条款**。
> 2. **图中数值未提取** —— 本页所有图表（Closed Cradle Rewet 柱图、摄入柱图、Hypotheses 矩阵）**在原文中退化为图注文本**，**数值一律不臆测**；凡需引用具体 g 值或 s 值，**必须回到 RAW_FULL 原文件或图件核对**。
> 3. **L14 / L18 批次差异未定性** —— 源文只说"something inherent to all codes"，**未给出原因**；**不得据此判定某一批次材料不合格**。
> 4. 作者署名（Kerry Clemmer / David Scherzer）**仅作来源归属保留**，不页面化为个人联系信息。

> ✅ 验证（2026-09-29）：本页为新 source 页，无既有结论被覆盖；所有结论直引源文，未做外推。

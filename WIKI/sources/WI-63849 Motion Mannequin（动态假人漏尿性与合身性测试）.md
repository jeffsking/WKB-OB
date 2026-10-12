---
type: source
title: "WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）"
source_type: 标准测试方法（WI）
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/WI-63849 Motion mannequin.docx.md
original_link: ""
date_published: 2024-02-20
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "WI-63849（第 0 版，2024-02-20）用于模拟尿裤使用状态下**湿态与干态**的**漏尿性（leakage）与合身性（fit）**两部分研究，是动态假人（Motion mannequin）的完整操作文件"
  - "模拟液口径：**0.1 g 牛黄酸胆酸钠（sodium taurocholate）粉末加入 1 L 生理盐水**，磁力搅拌 5–10 min，水浴加热至 **37 ± 1 ℃**"
  - "校准双轨：管路润洗（Station Delay 10 s、Flow Rate 15 mL/s、Volume **300 mL**）；液体校准（Volume **70 mL**，波动控制在 **± 3%** 以内）；蠕动泵管路尺寸须为 **17**，管路校准误差须达到 **± 1%** 以内"
  - "漏尿性时序（Insult 70 mL @ 15 mL/s）：Insult(等 1 s) → Crawl(速度 30.0) → Insult(等 2 s) → Crawl → Insult(等 2 s) → Loop → Insult(等 30 s) → Run Complete"
  - "漏尿位置按 **17 个分区**记录：裆部左右腿、前左右腿、后左右腿、下左右侧、上左右侧、前腰中心/左右、后腰中心/左右、外层"
  - "合身性按假人型号设定 Tab Spacing：**Koopa（Step 2）20 mm、Yoshi（Step 3–4 低端）19 mm、Mario（Step 4）22 mm、Luigi（Step 4 高端–Step 5）30 mm、Kirby（Step 4 高端）38 mm**"
  - "合身性六项指标：Ear Roping、Panel shift（10 mm 垂直标记线）、前部/后部/裆部下坠、LegGap、Tab-to-Tab（Hook 中心到 Hook 中心）"
  - "参考文稿为 **TTM-00313-8**，而 [[Finished Product Testing Method Summary（成品测试方法汇总表）]] 的 Motion Mannequin 列写 **TTM-00318-8**——编号差一位，需人工核对"
  - "适用范围注记：**合身性测试主要针对 Diaper 产品**，Pants 需与测试提出者讨论；**本测试不涉及 FIA**（Fit Image Analysis）"
pages_linked: ["[[Static Mannequin Test（静态假人测试）]]", "[[Mannequin BM Test（BM 假人测试）]]", "[[尿液模拟液（Urine Analog）]]", "[[芯体测试方法与验收基准（STM）]]", "[[Mannequin Lab（Rockwell 假人平台）]]", "[[KC Tianjin Mill（金佰利天津厂）]]"]
---

# WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）

## 一句话定位

**WI-63849（第 0 版，2024-02-20）**是动态假人系统的完整操作文件：在会行走/爬行的 mannequin 上，把「漏不漏」与「贴不贴」这两类最贴近真实使用的问题，拆成可记录的**漏尿位置分区**与**六项合身性尺寸**。

## 摘要

**实验目的**：本试验用于模拟尿裤产品使用状态下，基于人体**湿态和干态**整体产品**漏尿性和合身性**两部分的研究。

**模拟液配制**：**0.1 g 牛黄酸胆酸钠（sodium taurocholate）粉末加入 1 L 生理盐水**，用磁力搅拌器搅拌 **5–10 min** 后加入液体贮存容器，并将水浴锅打开加热至 **37 ± 1 ℃**。

**校准（每次测试开始前必做）**：
- **润洗管路**：Mannequin 下方放液体收集容器 → 打开软件进入测试界面 → 点「Fluid Delivery」进入参数调整页 → **Station Delay 10 s、Flow Rate 15 mL/s、Volume 300 mL**，勾选工作站后开始润洗。**润洗后的液体不能再次使用**。
- **液体校准**：同样路径设 **Station Delay 10 s、Flow Rate 15 mL/s、Volume 70 mL** → 收集流出液体称重 → **波动控制在 ± 3% 以内**；超差则按公式 (Target WT − Actual WT) / Target WT 计算后，从校准区域数值中增减。**若校准数值接近 0.8 或 1.2，需手动校准蠕动泵**。
- **手动校准蠕动泵**：经「BSG1 Configuration → Remote PLC Control」切手动 → Station 1 Valve → Operator Mode → Open Valve → 检查蠕动泵**管路尺寸是否为 17** → 管路校准启动 → 重复称重输入**直到误差 ≤ ± 1%** → 输入所需注液量 → 关阀、Program Mode、切回自动模式。校准流出的液体**可倒回贮存容器继续使用**。

**漏尿性测试**：在「BSG1 Study Manager」中用 **Select Phase** 依次选择动作组合（可选 Wait / Walk / Message / Crawl / Insult / Sit / Loop / Motion Start / Lay / Recirculate / Motion Stop / Stand / Complete）→ 返回主界面 → 记录产品干重（Dry Wt）→ 将产品穿戴到 Mannequin 上 → **用一根手指划过腿部皮筋与折页皮筋位置确保服帖** → 运行 → 观察漏尿，**发生时在 Location 栏记录漏尿位置** → 脱下产品称重记录湿重（Wet Wt）→ 保存并切换下一轮。报告经桌面「Study Builder&Report / Mannequin Report.xlsm」的 Main 工作表刷新数据连接后按 Request Number 生成。

**漏尿位置分区（17 区）**：裆部右腿 / 裆部左腿、前右腿 / 前左腿、后右腿 / 后左腿、下右侧 / 下左侧、上右侧 / 上左侧、前腰中心 / 前右腰 / 前左腰、后腰中心 / 后右腰 / 后左腰、外层（Outer Cover）。

**合身性测试**：按需求设定动作组合与注液量、运动时长、运动间隔。样品准备除称重外，还需：用马克笔标出**两侧耳贴外轮廓线**（在产品前部中心划线，中心线左右两侧划出耳贴粘贴位置；**Tab Spacing 按假人型号取值；Pants 产品跳过此步骤**）→ 在 Mannequin 上划线标识前后腰围位置（若超出 Mannequin 顶部则不划）→ 手指划过皮筋确保服帖 → **用黑色背景板**拍前、后、左侧照 → 标识 **Ear Roping**（在耳贴基部 CD 中心垂直划线，与耳贴边缘平行）→ 标识 **Panel shift**（辨识 Inner Cover side panel，在外侧上下各标一条 **10 mm 垂直线**；测试后追踪新位置并测两线间距，直尺保持水平）→ 测量**前部下坠**（前腰围顶端到 Mannequin 顶端距离）、**后部下坠**、**裆部下坠**（腿部底部水平线到尿裤最低点，需两把直尺）→ 评估 **LegGap**（撇开并锁定双腿，观察下部左右是否有间隙）→ 测量 **Tab-to-Tab**（Hook 中心到 Hook 中心）。**前/后/裆部下坠与 Tab-to-Tab 均须在测试前后各测一次**。

**适用范围注记**：合身性测试**主要针对 Diaper 产品**，Pants 需与测试提出者讨论；**本测试不涉及 FIA**（Fit Image Analysis，WI-45237），如需 FIA 须另行讨论。

## 提炼的数字与结论

### 校准参数（Calibration）

| 项目 Item | 口径 Condition |
|---|---|
| 润洗 Volume | **300 mL**（Station Delay 10 s、Flow Rate 15 mL/s） |
| 液体校准 Volume | **70 mL** |
| 液体校准允差 | **± 3%**（超出则按 (Target − Actual)/Target 修正 Calibration 值） |
| 手动校准触发条件 | 校准数值接近 **0.8 或 1.2** |
| 蠕动泵管路尺寸 | **17** |
| 管路校准允差 | **± 1%** |
| 校准公式 | (Target WT − Actual WT) / Target WT |
| 润洗液处置 | **不可再用**；校准流出液**可回倒贮存容器** |

### 漏尿性时序（Leakage Sequence）

| 序 | Phase | 参数 Parameters |
|---|---|---|
| 1 | Insult | 70 mL @ **15 mL/s**，Wait **1 s**，Leak Detector On |
| 2 | Crawl | Speed **30.0** |
| 3 | Insult | 70 mL @ 15 mL/s，Wait **2 s** |
| 4 | Crawl | Speed 30.0 |
| 5 | Insult | 70 mL @ 15 mL/s，Wait **2 s** |
| 6 | Loop（Step Number 2，Loop Count 2） | — |
| 7 | Insult | 70 mL @ 15 mL/s，Wait **30 s** |
| 8 | Run Complete | — |

### 模拟液与假人型号

| 项目 Item | 口径 / 取值 Value |
|---|---|
| 模拟液 | 0.1 g **牛黄酸胆酸钠** + 1 L 生理盐水，搅拌 5–10 min |
| 液温 | **37 ± 1 ℃** |
| Koopa（Step 2）Tab Spacing | **20 mm** |
| Yoshi（Step 3、Step 4 低端） | **19 mm** |
| Mario（Step 4） | **22 mm** |
| Luigi（Step 4 高端、Step 5） | **30 mm** |
| Kirby（Step 4 高端） | **38 mm** |
| 漏尿位置分区 | **17 区** |
| Panel shift 标记线 | **10 mm** 垂直线 |
| Crawl 速度 | **30.0** |

> ⚠️ **编号差异提示（2026-09-29）**：本文件「参考文稿」写 **TTM-00313-8 Mannequin Wet and Dry Motion Fit Test**，而 [[Finished Product Testing Method Summary（成品测试方法汇总表）]] 的 Motion Mannequin 行写 **TTM-00318-8**。两者相差一位数字，**疑为笔误，需人工核对方法主档** `[待验证]`。

> ⚠️ **待验证（2026-09-29）**：本文件未给出漏尿性的**判定门槛**（多少 mL 算漏、第几次注液漏算失败），也未给出合身性六项尺寸的**合格范围**；Crawl 速度 30.0 的**单位未写明** `[待验证]`。

## 关键论断（key_claims）

- **动态假人同时回答「漏不漏」与「贴不贴」，是唯一带运动的成品评价方法** —— 支撑页：[[Static Mannequin Test（静态假人测试）]]
- **模拟液用牛黄酸胆酸钠 + 盐水，37 ± 1 ℃，与纯盐水体系不同** —— 支撑页：[[尿液模拟液（Urine Analog）]]
- **校准是双轨的：液体 ± 3% + 管路 ± 1%，且每次测试前必做** —— 支撑页：[[Mannequin Lab（Rockwell 假人平台）]]
- **漏尿位置按 17 区记录，位置信息比总量信息更有诊断价值** —— 支撑页：[[Run-off & Leakage Test（滑渗与渗漏测试）]]
- **Tab Spacing 按假人型号取 19–38 mm，Pants 跳过此步** —— 支撑页：[[Static Mannequin Test（静态假人测试）]]
- **合身性六项指标须测试前后各测一次，差值才是运动的影响** —— 支撑页：[[Skin Contact Pressure（皮肤接触压力）]]
- **本测试不涉及 FIA，Pants 需另行讨论** —— 支撑页：[[芯体测试方法与验收基准（STM）]]

## 关联页面

- 概念：[[Static Mannequin Test（静态假人测试）]]、[[Mannequin BM Test（BM 假人测试）]]、[[尿液模拟液（Urine Analog）]]、[[芯体测试方法与验收基准（STM）]]、[[Run-off & Leakage Test（滑渗与渗漏测试）]]、[[Skin Contact Pressure（皮肤接触压力）]]、[[Elastic Tension & Creep（橡筋张力与回缩率）]]
- 实体：[[Mannequin Lab（Rockwell 假人平台）]]、[[KC Tianjin Mill（金佰利天津厂）]]、[[Kimberly-Clark（金佰利）]]
- 对比：（本批对比页见 [[GB-T 28004.1-2021 与 KC STM 成品吸收性能测试方法对比]]）

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/WI-63849 Motion mannequin.docx.md`
- 原文链接：（无；内部作业指导书）
- 参考文稿（文件自述）：TTM-00313-8 Mannequin Wet and Dry Motion Fit Test；Urine Analog # WI-33165；Operation of Mannequin Lab Rockwell System Platform # WI-38044；Fit Image Analysis (FIA) Mannequin Procedure # WI-45237；Motion Mannequin Full System Calibration # WI-45322；Mannequin Wet and Dry Motion Fit Test Data Sheet # FORM-51078；Mannequin Lab Study Builder Tool # WI-38046

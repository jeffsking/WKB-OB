---
type: source
title: "Capillarity Testing Throughput Upgrade Plan（毛细测试吞吐提升计划）"
source_type: 项目任务书
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Capillarity Testing Increased Throughput Plan.xlsx.md
original_link: ""
date_published: 2026-05-07
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "文件性质 = K-C **毛细测试（capillarity testing）能力升级与吞吐提升的内部项目跟踪表**，6 个工作表：Status（逐周状态，2/19 → 5/7）、Timeline（3–8 月甘特骨架）、Solver March 9 Notes、Throughput Plan March 19 Notes、Solver March 24 notes、Capital Meeting（资本化会议）"
  - "被测量的对象就是 **MCCT（multi-component capillary tension，多组分毛细张力）**：输出 **Bn = 特征毛细压（characteristic capillary pressure）** 与 **n = 分布宽度（breadth）**；求解器一次同时生成**吸收（absorption）与解吸（desorption）三条曲线**"
  - "吞吐瓶颈是「时间」而非「人力」：现状**每样约 4 小时/天占机**，目标靠软件把**单样控制在 8 小时**以内；2026 年潜在样量约 **300 个**，按此测算送样预算可达 20 万美元量级（见 manual_review）"
  - "硬件改造清单 Hardware BOM：3D 打印 **frit 板（多孔砂芯板）** 与支架、激光测厚仪、天平（**Sartorius Secura 613-1S**，mg 分辨率、600 g 量程、带防风罩）、阀/阀夹/盘管/接头、执行件（管路→砂芯）、第二套 frit holder；外协装配与金加工走 **Kimtech**"
  - "软件与自动化 Software：脚本支持**每个高度独立设置停留时间（dwell time）**；正在开发**终点判定（end point / equilibrium detection）算法**以替代固定停留时间；既有公式由 **Peter Elliker** 提供；激光接口手册上传 DORA 由 AI 写出接口代码"
  - "数据与系统 Data flow：求解器改为 **web-based**，输出自动写入 **Lab Vantage** 数据表（Kay 提供汇总模板）；代码入库 **ADO Azure DevOps**；维护归属（maintenance ownership）是被明确提出的风险——操作系统升级、bug、编程语言过时、用户需求变化都无人兜底"
  - "设备部署 Disposition：**3 台新机放 Lab Vantage 实验室（Taylors 吸液实验室）**、**1 台新机 + 1 台样机放吸液能力实验室（Richmond 实验室）**；Absorbent Capabilities Lab 与 ADT 分摊改造费（ACL 1 台 / ADT 3 台）"
  - "资本化政策 Capital policy：**单台 < 25 k USD 不列为资本项**（可含设备、运费与安装）；若**合计 > 625 k USD** 则整体转资产；因每台可独立移动、独立运行，**可主张每台为独立资产**——这是把整机拆件采购的财务动因"
pages_linked: ["[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]", "[[Kimtech（毛细测试设备外协加工与装配）]]"]
---

# Capillarity Testing Throughput Upgrade Plan（毛细测试吞吐提升计划）

## 一句话定位 One-line positioning

本库**毛细测试能力建设（设备 + 软件 + 求解器 + 方法文件）的唯一过程记录**：它把「测什么（MCCT 的 Bn / n）」「为什么慢（单样占机 4 h/天）」「怎么提速（可变停留时间 + 终点判定 + 求解器 + 多机并行）」与「钱从哪来（资本化阈值 25 k/台）」四件事串成一条线。回渗议题上它与 [[Rewet Method Comparison（回渗测试方法横向对比·K-C vs P&G）]] 互补：后者管「方法口径」，本页管「测量能力本身」。

## 摘要 Summary

**Status 表**按周记录 12 项活动的进展（2/19 → 5/7），每项挂 Person 1 / Person 2 与优先级（多数为 A）。主线是「先做出一台可用样机 → 验证 → 报价 → 复制多台 → 同步做软件与求解器 → 最后写 TTM 与培训」。到 5/7 时点：样机设计与首套升级**基本完成**，新机报价已下、订单已下，资金已到位（资金条目标记 COMPLETE），样机验证与软件文档仍在收尾。

**Timeline 表**给出 3 月（设计完成、报价完成、资金完成、ADT 送样申请完成）到 8 月的骨架，其中两项被明确标注风险：*Obtain new units* 的周期要按 Kimtech 报价与交期调整；*TTM completion* 可能需要比表上更长的时间，需上 dashboard 并让 Dan Sprotte 介入。

**Throughput Plan（3/19）**列出六个 HOT TOPICS：实验室摆位（吸液实验室最多放 3 台）、单机 vs 双机（理想是双机；若只有 25 k 则 ICT 两台 + AC 一台）、ICT 台数、资金（设备属资本项，Maria 与采购 Raegan 沟通例外）、求解器归属（须把维护责任并入 Virtual R&D 与 ICT 的讨论）、送样预算（2026 年约 300 个潜在样品）。

**Solver 相关两表**确定：由 Andrew Baker（Virtual R&D / 建模）基于 Steve Rocke 既有软件做求解器，改成 web 端，输出 Bn 与解吸能（desorption energies），并写入 Kay 提供的 Lab Vantage 汇总模板；预期工期约 1 个月；维护归属被单独追问（操作系统变更、bug、语言过时、需求变更四类）。

**Capital Meeting 表**给出资本化判据与「拆件采购」的财务路径。

## 提炼的数字与结论 Key figures & conclusions

| Item 项目 | 内容 Content | Source |
|---|---|---|
| 测量量 Measurands | **Bn = 特征毛细压**；**n = 分布宽度**；一次生成吸收/解吸三条曲线 | Solver March 9 Notes |
| 样机硬件组成 | frit 板（3D 打印，不影响数据变异）+ 支架、激光测厚仪、天平、阀/盘管/接头、执行件、基座板 | Status 表 5/7、4/23、3/19 |
| 天平规格 Balance spec | mg 分辨率、量程上限 600 g（可更低）、带防风罩；**Sartorius Secura 613-1S** | Status 表（Maria 邮件要求） |
| 软件能力 Software | 每个高度可设不同 dwell time；可选「规定停留时间」或「终点判定算法」；有平衡（equilibrium）判据以压缩测试时长 | Status 表 4/3（a–e）、4/23 |
| 求解器 Solver | 由 Excel 时代的分钟级 → **秒级**；拟合更好；web 端；对接 Lab Vantage；代码存 ADO Azure DevOps | Status 表 5/1、4/23、Solver 3/9 与 3/24 |
| 吞吐现状与目标 Throughput | 现状约 **4 h/天·样**；目标靠软件把单样控制在 **8 h** 内；2026 潜在样量约 **300 个** | Throughput Plan 3/19 |
| 设备部署 Disposition | 3 台新机 → Lab Vantage 实验室（Taylors）；1 台新机 + 1 台样机 → 吸液能力实验室（Richmond） | Status 表（Secure funding） |
| 费用分摊 | Absorbent Capabilities Lab 1 台 / ADT 3 台；已确认 < 25 k USD 走非资本费用 | Status 表 4/23 |
| 资本化阈值 Capital threshold | **< 25 k USD/台不列资产**（含设备+运费+安装）；**合计 > 625 k USD 则整体转资产**；每台可独立移动、独立运行 → 可主张每台为独立资产 | Capital Meeting 表 |
| 方法文件 TTM | 由 Melissa Hildebrand 与 Matt Valaskey 完成；**暂不做精密度（precision）验证**，因此预期不需 validation；但需确认多台仪器给出一致结果 | Status 表 TTM 行 |
| 维护风险 Maintenance | 四类：操作系统变更致软件失效、bug、编程语言过时、用户需求变化；当前「坏了就打电话给 Rocke」，无正式维护 | Solver 3/20 |
| 在测样品队列 | fem care 梯度（Dayuan）、Lifesavers 2.0、Poise、wintogreen 层压材料、LS 面层 | Status 表 Current Testing 行 |

### 人员分工 Owners（节选）

| 角色 Role | 事项 |
|---|---|
| Steve Rocke | 硬件设计、软件主体、与 Kimtech 对接图纸与零件 |
| Matt Valaskey | 样机组装（3D 打印件、阀件、执行件）、测试执行、软件测试、天平采购 |
| María López García | 资金申请、跨团队协调（Virtual R&D / ICT / Lab Vantage）、资本化沟通 |
| Chantell Hamer | 测试执行与培训（Matt 的备份） |
| Melissa Hildebrand | TTM 编写 |
| Andrew Baker | 求解器（Virtual R&D / 建模） |
| Kay Flood | Lab Vantage 汇总模板 |
| Mark Krippner | ADT 毛细送样申请 |

> 🔴 **manual_review（2026-09-29）**：本表含**内部采购报价、设备单价、资本化金额阈值与送样预算**（Kimtech 装配人工、单台估价、天平/激光单价、Mosaic 计算机单价、2026 年送样预算量级、25 k / 625 k 资本阈值）。属 K-C 内部财务与采购信息，**本页只登记结构性事实（阈值规则、分摊结构、部署台数）与量级，不落完整报价明细**；原文留存 `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Capillarity Testing Increased Throughput Plan.xlsx.md`。**对外引用或据以谈判前须经采购/财务确认。**
> ⚠️ **抽取噪声 Parse note**：源文件为 Excel 抽取，Status 表单元格内含大量换行拼接的周报要点，个别行（如 Documentation、Capital Meeting）列错位；上表以可辨认语义的单元格为准，未从错位列推断数值。

## 与本库其它页面的关系 Relations

- 概念：[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]（本页派生）
- 实体：[[Kimtech（毛细测试设备外协加工与装配）]]（本页派生）
- 相邻：[[Rewet Method Comparison（回渗测试方法横向对比·K-C vs P&G）]]（方法口径）、[[Bladder Box Intake Test（膀胱箱压载摄入测试）]]（摄入侧方法）

## 原文摘录 Original excerpts

- "MCCT - multi component capillary tension / bn characteristic capillary pression / n breadth / need to do a resource request / decision to go with Modeling team to make solver"（Solver March 9 Notes，2026/03/09）
- "A new format for the script has been developed. The script permits the usage of different dwell times at each height. … The plan is to give the option to use the prescribed dwell time, or a yet-to-be-developed algorithm."（Status 表 4/3 软件进展 a–e）
- "-truly ~4hrs a day of tester / -need software to help control the time to 8 hrs per sample"（Throughput Plan March 19 Notes，HOT TOPICS 6）
- "-under 25K per asset is the capital limit / -if it is more than $625K total, then it turns into asset / -each one can be defined as its own separate asset / -they can be moved independently / -they function independently"（Capital Meeting 表）
- "-today there is no maintenance - today if there are problems, Rocke is called"（Solver March 20 notes）

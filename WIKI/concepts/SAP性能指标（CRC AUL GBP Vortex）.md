---
type: concept
title: "SAP性能指标（CRC AUL GBP Vortex）"
domain: [卫材研发, SAP与流体]
status: growing
updated: 2026-09-29
tags: [SAP, CRC, AUL, GBP, Vortex, PSD, 高吸水树脂, 测试口径]
aliases: ["SAP 性能指标（CRC / AUL / GBP / Vortex）"]
---

# SAP 性能指标（CRC / AUL / GBP / Vortex）

> 一句话定义：评价高吸水树脂（SAP）的四组核心指标——**CRC（离心保水）、AUL（加压吸收）、GBP（凝胶床渗透率）、Vortex（吸收速率）**；选型的难点不在读单个数字，而在**分清口径**（不同压力、不同液、不同时间）。

## 机理 / 结构拆解

1. **CRC（Centrifuge Retention Capacity，离心保水率）**：0.9% 盐水、250 G 离心后的持液量（g/g）。代表**静态容量**——储库型 SAP 的主指标（NR-950 典型值最高）。
2. **AUL（Absorbency Under Load，加压吸收）**：在一定载荷下（**0.3 / 0.7 / 0.9 psi**）的吸收量。代表**抗压容量**——穿在身上被体重压住时仍能吸多少。**口径必须随值标注**，0.9psi 与 0.7psi 不可横比。
3. **GBP（Gel Bed Permeability，凝胶床渗透率）**：单位 Darcy。代表**液体穿过已膨胀凝胶床的能力**——高 GBP 让液体在吸湿后仍能向下渗透，是**顶层（第一响应层）**的关键指标，直接对抗凝胶阻塞与高回渗。
4. **Vortex（涡旋吸收时间）**：一定量盐水在磁力搅拌下被 SAP 吸尽、涡旋消失的时间（s）。代表**吸收速率**——面层第一响应的速度。
5. **PSD（粒径分布）**：以 850 / 600 / 300 / 150 / 45 μm 目数分档计。SAP 常用主粒径目标为 **300–600 μm 约占 80%**；主粒径过大则接触面积小、过细则凝胶阻塞风险高。
6. **辅助指标**：表观密度、交货水分、pH、Hunter 白度、残单（残留单体 ppm，安全口径）。
7. **选型逻辑：指标是分工的，不是排名** ——
   - **顶层（第一响应）**：要 **高 GBP + 高 AUL + 快 Vortex**，可以牺牲 CRC（"求快不求多"）；
   - **储库层**：要 **高 CRC + 高 AUL**，Vortex 慢无妨；
   - 两者组合即 [[SAP错峰膨胀]] 的物质基础。

## 关键参数表

| 指标（口径） | 含义 | 典型值 / 范围 | 出处 |
|---|---|---|---|
| CRC 离心保水（0.9% 盐水, 250G） | 静态容量 | KC 511 30.9；NR-610S 30.8；NR-950 36.7；Code X 28.8（g/g） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| CRC 实测（本批 250G 口径） | — | NR950 38.79；NR610S 33.71；High GBP 30.594（g/g） | [[CI-06 COCO V6 第三轮试产测试结果]] |
| AUL 0.7psi | 抗压容量 | KC 511 18.4；NR-610S 12.1；NR-950 19.4（g/g） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| AUL 0.9psi | 抗压容量（更高载荷） | Code X 22.2（g/g）——**与 0.7psi 口径不可横比** | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| GBP | 凝胶床渗透率 | KC 511 24（本表口径）；NR-610S 6；NR-950 8；Code X 55.3（Darcy） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| GBP 口径警示 | 跨源四值 | KC 511 的 GBP 跨源见 24 / 25 / 26 / 35；本批取 S1 实测 24 | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| Vortex 吸收速率 | 吸收速度 | NR-610S 19（最快）；KC 511 29；Code X 33；NR-950 51（最慢）（s） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| PSD 30–50 目 | 粒径占比 | KC 511 76.9%；NR-610S 65.1%；NR-950 88.6%；Code X 77.8%（%） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| PSD 目标 | Nuoer PSD 目标 | 300–600 μm 约占 80% | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| 残单 | 安全口径 | KC 511 154；NR-610S 156；NR-950 156（ppm） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| DI 自由溶胀 | 纯水自由溶胀 | KC 511 59.4；NR-610S 60.8；NR-950 62.5（g/g） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |

> ⚠️ **禁止无来源参数**：表中数字分别来自本批两份来源（原料清单为厂家/准备会口径，试产结果为实验室实测口径），**两套口径不同**，不可混用。库内暂无 SAP 的膨胀**动力学曲线**，标 `[待验证]`。

> ⚠️ **跨来源数值差异（2026-09-29，待人工确认）**：同一"Code X / High GBP"牌号，准备会口径 GBP **55.3**、试产实测 GBP **37.92**；CRC 28.8 vs 30.594、AUL@0.9psi 22.2 vs 27.564。差异原因（样品批次 / 测试设备 / 口径）不明，**本页不裁决**。

## 追加：Open Innovation 批（2026-09-29 追加）

> 本节为 **Resources / Open Innovation 批（批次 S4_Resources_Open Innovation_05）** 编译时的追加记录，**不改动上方既有结论**。上方"**GBP 是跨源最不稳的指标**""AUL 必须连压力一起读"两条口径警示在本批**再次被验证**；本节补充的是**四指标之间的取舍原理与一条前置关系**。

### 1. 本批新增：四指标取舍原理（速查）

| 取舍关系 | 机理 | 优化路径 | 出处 |
|---|---|---|---|
| **CRC ↑ ↔ GBP ↓** | 高 CRC 需低交联密度 → 颗粒过软、易变形堵通道 | **核-壳梯度交联**（内核低交联保 CRC，外壳高交联保 GBP） | [[Nuoer High-GBP SAP Visit Plan & Roadmap（诺尔高GBP SAP拜访预案）]] |
| **GBP ↑ ↔ Vortex ↑** | 高交联外壳阻碍水分进入颗粒内部 | 表面造孔（湿法研磨）+ 发泡 + 粒径向 **300–600 μm** 集中 | 同上 |
| **AUL ↑ ↔ CRC ↓** | 高 AUL 需高交联密度 | 非均匀交联（表面高、芯部低） | 同上 |
| **GBP ↑ 需 AUL ↑** | **凝胶强度是渗透性的前置条件** | **AUL ≥18 是 GBP ≥50 的基础** | 同上 |

> 📌 **本批最重要的一条（2026-09-29）**：**AUL 是 GBP 的必要不充分条件**——没有足够的凝胶强度，颗粒在压力下变形塌陷，**再高的 GBP 数值也无意义**。这解释了为什么高 GBP 标杆（BASF 5400 AUL 19、LG LK804ND AUL 18、SDP SG-N210 AUL 19.5）**AUL 都在 18–20 g/g**，而 GBP 天花板 35 的 Nuoer NR511 **AUL 仅 14.7–15**。

### 2. 本批新增：GBP 门槛随芯体 SAM 含量递进

| 芯体类型 | SAM% | GBP 最低要求 |
|---|---|---|
| SAM/Fluff 中低含量 | <40% | 无硬性要求 |
| SAM/Fluff 中等含量 | 40–55% | **>7 Darcy** |
| SAM/Fluff 高含量 | 55–70% | **>15 Darcy** |
| 薄芯（BONNIE / AT-hybrid） | 70–85% | **>20 Darcy** |
| 无绒芯（Fluffless / CIRRUS） | 85–100% | **>20 Darcy** |

> ⚠️ **单位警示（本批新增）**：本批来源的 GBP 以 **Darcy** 给出，而本页上方既有记录多为无量纲或 10⁻⁷ cm³·s/g 口径，**两套单位不可直接换算**。跨页比较 GBP 前**必须先统一单位与测试条件**——这是上方"教训二"的第三条佐证。

### 3. 验证记录

> ✅ 验证（2026-09-29，来源 [[Nuoer High-GBP SAP Visit Plan & Roadmap（诺尔高GBP SAP拜访预案）]]）：本页"GBP 是跨源最不稳的指标"的判断在本批得到**机制层面的解释**——GBP 之所以不稳，是因为它**同时受 AUL（凝胶强度）、表面交联壳层、粒径分布与测试方法单位**四者影响，且**与 CRC、Vortex 存在结构性取舍**。原页结论**未被修正**。

- **追加要点**：**读 GBP 前先读 AUL**。若 AUL <18 g/g，GBP 数值高低不代表实际渗透能力。
- **追加 `[待验证]`**：GBP 的 Darcy 与 10⁻⁷ cm³·s/g 两套单位在本库各来源中的分布与换算关系；AUL ≥18 → GBP ≥50 这一门槛的实测边界。

## 追加：Open Innovation 批（2026-09-29 追加 · SAM 全球牌号数据库）

> 追加来源：[[SAM Database-CW（全球 SAM 牌号性能数据库）]]。**不改动上文既有结论**；本批追加的是**跨供应商口径一致性**的新证据。

### 1. AUL 压力条件混列（与本页"教训一"同向，并给出新证据）

源数据库在**同一列**内混记两种压力条件，并在列名中明示：`AUL, 0.9 psi / 0.7 psi for Nuoer (g/g)`。

| 条件 | 适用对象 | 含义 |
|---|---|---|
| **0.9 psi** | 通用（BASF / Evonik / LG / SDP / Satellite / Sumitomo / Nippon Shokubai / Formosa / Danson / Wanhua） | 标准负荷 |
| **0.7 psi** | **仅诺尔牌号** | 低负荷 → **数值偏高**，与 0.9 psi 不可直接比 |

> ⚠️ **重要**：本页"教训一（AUL 必须连压力一起读）"在本批得到**结构性证据**——混列不是个别现象，而是**数据库层面的设计**。跨供应商比较 AUL 时**必须先做压力归一化**，本页不代为换算。

### 2. GBP 跨表不一致（与本页"教训二"同向，且更严重）

同一牌号 **`Nuoer NR511`** 在同一份数据库的三张表中给出**三套数值**：

| Sheet | CRC | AUL | **GBP（Darcy）** | Vortex |
|---|---|---|---|---|
| SAM database Global | 31 | 15 | **25** | 33 |
| Global v2 | 31 | 14.7 | **35** | 33 |
| KCC-YJ | 31.5 | 18.2 | **26** | 28 |

> ⚠️ **并列记录（2026-09-29，不裁决）**：**GBP 25 / 35 / 26 三值并存且源文未给解释**。这与本页既有记录（KC 511 的 24/25/26/35 四值）**是同一类问题的第二次出现**，进一步支持"GBP 是跨源最不稳的指标"这一既有判断——**该判断未被修正，而是被加强**。本页照录，**不取代表值、不取均值**。

### 3. 数据来源标签：跨行比较必须连 Source 列一起读

源数据库逐行标注出处，至少六类：**TDS / spec / SAM lab / CaiShan / 供应商 COA / targets（设计目标值）**。

> 中文：`targets` 是**目标值而非实测值**（如 LG GD6100NS、SDP N14/N213/SG-N17 标注为 target/TDS 而性能格有空缺）。**把目标值当实测值比较是此类数据库最常见的误用**。

### 4. 全表取值区间（照录，供跨源核对）

| Metric 指标 | 表中出现范围 | 备注 |
|---|---|---|
| CRC（g/g） | 24 – 47 | 主流 30–40 |
| AUL（g/g） | 8 – 31 | **压力条件不统一** |
| GBP（Darcy） | 0 – 96（96 为 KCC-YJ 表中 Sandia SG-N212） | **高容量牌号普遍 0–3** |
| Vortex（s） | 18 – 120 | 越低越快 |

### 5. 与"AUL ≥18 是 GBP ≥50 前置"的关系（不裁决）

本页上一批追加记录了该前置判断。本批数据库显示：**GBP ≥50 的牌号确实集中在 AUL ≥18–19 的区间**（如 BASF 5400 AUL 19/GBP 65、Evonik 9394 AUL 20/GBP 65、BASF 9700 AUL 18/GBP 70、LG LK207PN/LK501 AUL 19/GBP 55、Evonik 4400 AUL 18/GBP 50），**方向一致**；但源文**未做统计检验**，本页**仅记方向、不据此确认门槛**。

> ✅ 验证（2026-09-29，source [[SAM Database-CW（全球 SAM 牌号性能数据库）]]）：本次追加**未修正**本页任何既有结论；两条既有教训（AUL 须连压力读、GBP 跨源最不稳）均被**加强**。上文标 `[待验证]` 的"GBP 两套单位分布与换算关系"**仍未闭环**——本批全部数据使用 Darcy，未提供 10⁻⁷ cm³·s/g 口径，**不可换算**。

> 🔴 **manual_review（2026-09-29）**：本源为内部材料数据库，含逐牌号性能与各区域实际使用牌号；依 AGENTS.md §5，**不页面化供应商商务条款与价格**（`Cost/MT` 列在本源为空，本页无成本数据）。

## 相邻概念

- 架构机制：[[SAP错峰膨胀]]、[[分区密度设计]]
- 层间关系：[[REL增强层]]、[[ADL（导流层）]]
- 验收方法：[[芯体测试方法与验收基准（STM）]]
- 对比：[[SAP 四牌号性能对比（KC511 vs NR-610S vs NR-950 vs Code X）]]

## 经验教训

> ✅ 验证（2026-09-29，来源 [[CI-06 COCO V6 第三轮试产测试结果]]）：本页"选型逻辑是分工不是排名"的表述被实测支持——NR-950（高 CRC / 高 AUL、Vortex 最慢 51 s）与 NR-610S（Vortex 最快 19 s、GBP 最低 6）在同一试产中分别对应"储库"与"极快吸"两种角色，无单一牌号全指标领先。

- **教训一（口径）**：**AUL 必须连压力一起读**。0.9psi 与 0.7psi 的 AUL 数值之间没有可比性——本批已两次因此产生"看起来矛盾"的数字。
- **教训二（口径）**：**GBP 是跨源最不稳的指标**（KC 511 出现 24/25/26/35 四值）。引用 GBP 前须确认来源与测试条件。
- **待补 `[待验证]`**：各牌号的膨胀动力学曲线；SAP 性能与芯体级回渗/摄入的定量关系（本批产品级数据尚不完整）。

## 追加：Meeting Minutes 批（2026-09-29 追加 · 复合芯体上下层搭配）

> 本节为 **S5_Areas_Meeting Minutes_01 批次（[[SAP Grade Strategy for Composite Core & Overseas Market Review — Nuoer Visit（复合芯体产品市场推广·诺尔交流）]]）** 编译时的追加记录，**不改动上方既有结论**。

### 1. Layer分工原则 上下层分工（本批核心）

| 层 | 性能取向 | 机理 |
|---|---|---|
| **上层** | **吸收慢 + 保水（CRC）高** | 让液体尽快下渗到下层；上层若先饱和，反渗（rewet）会明显变差 |
| **下层** | **吸收速度快**（且保水越高越好） | 承接下渗液体，决定整体 intake 速度 |

- 会上的关键提醒：**无论什么牌号，饱和后反渗都会变慢**；差别只在「什么时候饱和」。若上层吸收太慢（如下层 30 s、上层 70 s），则整体体验不可接受 → **上下层的速度差要有设计**。

### 2. GBP 与结构设计的替代关系（本批新认知）

- **GBP（通液性）的作用**：提高下渗 → 提升整体 SAP **利用率** 与 **多次 intake**。
- **但结构（槽 / channel）的收益更大**：会上判断「**GP（GBP）做得再高，也不如槽结构的效果与作用**」→ 若已有结构设计方案，**上层不必追求过高 GBP**。
- **成本约束**：把通液性做高会显著增加成本 → 目标区间应随结构设计而定，而非越高越好。

### 3. 聚合工艺 → 性能取向（本批新增因果链）

| 工艺 | 性能取向 | 在芯体中的用法 |
|---|---|---|
| **后中和**（先聚合再中和） | 分子链更长 → **溶出物低、更稳定** | 作为稳定性保障的基底 |
| **前中和**（聚合时间短、温度高） | **保水可很高，但吸收速度慢**；长期溶出物高 | 芯体中**不单独使用**，可少量放上层或下层 |
| **注油型**（注油反应/防腐处理） | **首次吸收快，后段弱** | 常规牌号多用此类；在木浆结构中二次/三次表现更好 |

### 4. 指标设想区间（未定案，仅登记）

- GBP：由约 **25** 提到 **30–40**；AUL 接近 **20**；CRC 由 **31–32** 降到 **28–29**（若必须降，AUL 可能降到 **16–17**）；vortex 会随之上**升**，但过高会导致吸收过慢。
- 外部牌号标称 GBP **53** / 吸收速度 **36** / 保水 **31.5** / 加压 **18** —— 会上评价「太完美、可能不现实」，**且跨实验室数据不可直接横比** → 仅作方向参考。

> ✅ 验证（2026-09-29，来源 [[SAP Grade Strategy for Composite Core & Overseas Market Review — Nuoer Visit（复合芯体产品市场推广·诺尔交流）]]）：本页既有「四项指标相互制约」的定位被本批**支持**，并**新增两条约束**：① **上下层分工**使同一牌号在不同层的取向不同；② **结构设计可以替代一部分 GBP 需求**。**原结论未被修正**。

> 🔴 **manual_review（2026-09-29）**：本批含 SAP 牌号与独供安排，**本页不落牌号规格**；要点留存于源摘要页。

## 追加：Meeting Minutes 批（2026-09-29 追加 · 高 GBP 牌号与 GBP/CRC 权衡）

> 来源：[[COCO V6 Trial Code Design & Process Alignment（录音纪要 2026-08-17）]]（2026-08-17 ASR 转写）。本批只**追加**，不修改既有结论。

**GBP/CRC 权衡的实证案例（本批新增）：**

- 供应商新开发的高 GBP 牌号：GBP **接近 40**，而现有主流牌号 GBP 在 **24–28** 区间；代价是**牺牲少量 CRC**。
- 会议口径评价：「从参数上看还是非常 promising」。

| Item 项目 | Value 数值 | Note 备注 |
| --- | --- | --- |
| 现有牌号 GBP | 24–28 | 会议转述，[待验证] |
| 新高 GBP 牌号 | ≈40 | 会议转述，须以 TDS 复核 |
| CRC 变化 | 略降（牺牲一点点） | 未给具体数值 |
| 开发周期 | 不到 1 个月（上一款之后） | 供应商开发速度佐证 |

**「吸水粉量增加 → 可否用更便宜 LSN」的联动假设（讨论中，非已决）：**

- 若 SAP 量增加，是否可让 LSN 使用更便宜的材料；需结合性能与成本评估（现有 38 g 全天胶方案之外的选择）。⚠️ 此为**讨论中的想法**，尚未形成结论。

✅ **验证记录（2026-09-29）**：以上数值均为会议转述的参数表口径，**非本方实测**；引用前须以供应商 TDS / 实测报告复核。参见 [[COCO V6 Trial Code Design & Process Alignment（录音纪要 2026-08-17）]]、[[诺尔（Nuoer）]]。

## Evidence Update 证据追加（2026-09-29 · Areas/IP 第 3 批）

> ✅ 追加（2026-09-29，source 来源 [[WO2024111948A1 Superabsorbent Polymer and Preparation Method Therefor (LG Chem)]]）：本批新增两项值得进入本页指标体系的**量化定义**（均为该专利申请原文口径，非本方实测）：
>
> | Metric 指标 | Definition（source wording）定义 | Threshold in claim 门槛 | Source 出处 |
> |---|---|---|---|
> | **EFFC（유효 흡수능，有效吸收能力）** | **EFFC(0.3 psi) =（CRC + 0.3 psi AUP）/ 2** | > **29.5 g/g**（从属项优选 30–40 g/g） | 同上 Claim 1 ii) 与式 1 |
> | **1 分钟自来水吸收量（1분 수도수 흡수능）** | SAP **1 g** 浸入自来水 **2 L**、溶胀 **1 分钟**时被吸收的水重 | > **115 g** | 同上 Claim 1 iv) |
> | **加压盐水 2 小时再润湿（가압 염수 2시간 재습윤）** | SAP **4 g** 浸入 **0.9 wt% NaCl 水溶液 100 g** 溶胀 **120 分钟** → 其上置滤纸 → **0.75 psi 加压 5 分钟** → 测得从 SAP 回渗到滤纸的水重 | **< 3.7 g**（从属项收紧 ≤3.4 g） | 同上 Claim 1 v) |
>
> - **EFFC 的价值**：它把 CRC（低压保水）与 AUP（0.3 psi 加压吸收）压成一个数，便于供应商单点对齐；本页既有指标群中缺这个组合量，可视为对 [[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]] 的量化补充（**追加的是指标定义，不修改本页既有结论与数值**）。
> - **背景中的技术矛盾值得记取**：该来源明文记载**吸收速度与 CRC/AUP 相互制约**——为提高吸收速度而采用高发泡聚合，会导致聚合物芯强度下降、CRC 与 AUP 劣化；其工艺解法是调节**表面交联液中有机溶剂（沸点 <90 ℃）的比例 ≥24 wt%（优选 25–30 wt%）、水/溶剂重量比 1.0–<3.0**，以及**表面交联剂密度（交联剂重/水重×1000）1.0–<17.0**。
> - **表面交联后团聚物门槛**：同一来源把「>850 µm 团聚物 <4.0 wt%」写进权利要求，可作为表面交联工艺的过程质量指标候选。
>
> 🔴 **manual_review（2026-09-29）**：该来源为 **PCT A1 国际申请公开**（公开日 2024-05-30），是否进入国家阶段/已授权，来源未记载 → `[待验证]`；**上述指标可用于供应商对齐讨论，但不得据此判断我方产品是否落入其权利要求**（FTO 属新结论，须法务评估）。

## 追加：Meeting Minutes 批（2026-09-29 追加 · EDANA 区间口径与 CRC/AUL trade-off 的产品化含义）

> 来源：[[Diaper NPD Workshop Prep — Absorbency, Skin Health & Comfort Feature Map（2026-06-05）]]（Workshop 准备材料 v1.0，2026-06-05）。本批只**追加**，不修改既有结论。

**四大指标的区间口径（本批新增，含标准号）：**

| 指标 | 含义 | 区间 | 标准 |
| --- | --- | --- | --- |
| **CRC（离心保留容量）** | 无加压下 SAP 吸水倍率 | **35–40 g/g** | **EDANA WSP 241.0** |
| **AUL（载荷下吸收量）** | **0.9 psi** 加压下保留量 | **25–30 g/g** | **EDANA WSP 242.2** |
| **GBP（凝胶床渗透性）** | 加压下液体穿透能力 | **25–40 Darcy** | EDANA WSP 241.0–242.2 |
| **Vortex Time（涡流时间）** | 吸液速度 | **20–40 s** | Vortex Method |

**核心 trade-off（本批新增，与本页既有记录一致并给出产品化含义）：**

> **CRC↑ → AUL↓** —— 高端产品必须在两者之间**找平衡点**，不能单向追求高 CRC。

**由此得到的认知（本批新增）：**

1. **AUL 的加压条件必须写明（0.9 psi）** —— 不同 psi 下的 AUL 不可直接比较；引述 AUL 时须同时给出载荷条件。
2. **GBP 有独立区间（25–40 Darcy）**，与 CRC/AUL 并列而非派生 —— 这解释了为什么"高 CRC"产品仍可能渗透差：三者是**三个正交维度**。
3. **产品分层的指标落点**（Workshop 口径）：
   - **主流款**：单 SAP 层优化 → 只做 baseline；
   - **高端款**：用 **REL 4 + 空隙体积优化** 补足，而非堆 CRC；
   - **旗舰款**：**多 SAP 层系统**（快速层 + 主体层 + 保留层）→ 用**分层**绕开单一牌号的 CRC/AUL trade-off。
4. **多 SAP 层是破解 CRC/AUL trade-off 的结构性办法**：不同层用不同牌号各司其职（快速吸入层低 CRC 高 AUL、主体层高 CRC），而不是要求一颗 SAP 同时做到两者。

✅ **验证记录（2026-09-29）**：以上区间来自 **Workshop 准备材料 v1.0**，其引用 `references/xx` **原始文件未随本批次提供**；标准号为文档口径，须回溯 EDANA 原文确认 [待验证]。参见 [[Multilayer SAP Core（多层SAP芯体）]]、[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]、[[诺尔（Nuoer）]]。

## 追加：Open Innovation 批（2026-09-29 追加 · 四指标测试口径与选型门槛）

> 来源：[[SAP Four Core Metrics Breakdown（SAP 四大核心指标拆解 CRC_AUL_GBP_Vortex）]]。本批只**追加**，不修改既有结论。

### 1. 本批新增：带标准号的测试口径（EDANA ERT 系列）

| 指标 | 标准 / 方法 | 关键测试条件 | 计算公式 |
|---|---|---|---|
| CRC | 茶袋法 / **EDANA ERT 441.2** | 0.9% NaCl、自由吸液 30 min、250 g 离心 4 min | CRC = (W3 − W2 − W1) / W1 |
| AUL | **EDANA ERT 442.1** | 0.3 / 0.7 / 0.9 psi，底部接触 0.9% NaCl 吸液 60 min | AUL = (W3 − W1) / W1 |
| GBP / SFC | **EDANA ERT 470.2** | 0.3 psi 吸至饱和后维持压力、顶部持续注盐水 | SFC = K × (Q / ΔP)，单位 **×10⁻⁷ cm³·s/g** |
| Vortex | 行业通用（**非 EDANA 标准**） | 50 mL 0.9% NaCl + 1 g SAP、磁力搅拌 500–600 rpm | 漩涡完全消失的时间（s） |

> ⚠️ **单位警示（本批新增）**：本批 GBP/SFC 以 **×10⁻⁷ cm³·s/g** 给出，而本页既有记录多为 **Darcy**；**两套单位不可直接换算**，这使"GBP 是跨源最不稳的指标"这一既有判断进一步被加强（**未修正，仅加强**）。

### 2. 本批新增：分级典型值与选型门槛

| 项目 | 普通级 | 高端级 | 生物基 |
|---|---|---|---|
| CRC（g/g） | 30–40 | 40–50 | 20–40（比石油基低 20–50%） |
| AUL 0.7 psi（g/g） | 18–25 | 25–30 | 当前比石油基低 20–30% |
| SFC（×10⁻⁷ cm³·s/g） | 5–15 | 20–40（超高端 40–70） | — |

- **AUL/CRC 比值**：高端 0.6–0.7，普通 0.4–0.5（越接近 1 表示加压后保水越强）。
- **选型门槛（原文口径）**：高端纸尿裤 **AUL ≥28（0.7 psi）+ Vortex ≤35 s + SFC ≥30**；主流 **AUL ≥24 + Vortex ≤45 s + SFC ≥15**；0.7 psi 下 AUL ≥25 为合格、≥28 为优质。
- **Vortex 评级**：≤30 s 极快 / 30–45 s 快 / 45–60 s 中等 / >60 s 慢。

### 3. 本批新增：GBP 的"隐藏 boss"定位与因果链

- CRC 与 AUL 都只测**单次吸收**；宝宝一天排尿 **5–8 次**，第 3、5 次尿液到达时 SAP 已膨胀成凝胶，凝胶粘连堵死通道 → 后续尿液无法穿透 → 从侧边漏出。
- 原文判读：**"前几次不漏，后面必漏"的根本原因是 GBP/SFC 失守**，而非 CRC 或 AUL 不足。
- 提升手段（本批新增）：二次/多重表面交联（保持颗粒独立性防粘连）、不规则颗粒形态（釜式工艺天然优势）、纳米 SiO₂ 等"隔离珠"、粒径粗细搭配形成骨架通道。

### 4. 本批新增：Vortex–AUL 矛盾与梯度交联解法

- 要 Vortex 快 → 粒径小、表面交联浅 → 但 AUL 低；要 AUL 高 → 表面交联深 → 但 Vortex 慢。
- 解法：**内层低交联（快吸）+ 外层高交联（保水）= 表面交联梯度设计**，原文指其为**釜式工艺的核心优势**。
- 提升 AUL 的另两条路径：内交联剂引入刚性基团构建"支撑骨架"；无机纳米材料掺杂（蒙脱土 MMT 作物理交联点，凝胶强度 +50%）。

> ✅ 验证（2026-09-29，source [[SAP Four Core Metrics Breakdown（SAP 四大核心指标拆解 CRC_AUL_GBP_Vortex）]]）：本页既有结论**均未被修正**——"AUL 必须连压力一起读"（本批给出 0.3/0.7/0.9 psi 三档完整典型值）、"GBP 跨源最不稳"（本批新增第三种单位口径）、"四项指标相互制约"（本批给出 Vortex–AUL 的机理级解释）三条均被**加强**。
>
> 追加 `[待验证]`：×10⁻⁷ cm³·s/g 与 Darcy 的换算关系；"前几次不漏、后面必漏"与 GBP 门槛的定量边界（本批为定性判读）。

## 来源

- [[Coco V6 试产原料清单（Raw material list v3.0）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Raw material list for Coco V6 trial.xlsx.md`
- [[SAP Four Core Metrics Breakdown（SAP 四大核心指标拆解 CRC_AUL_GBP_Vortex）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP四大核心指标拆解与说明.docx.md`（2026-09-29 追加）
- [[SAM Database-CW（全球 SAM 牌号性能数据库）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAM Database-CW.xlsx.md`（2026-09-29 追加）
- [[COCO V6 试产原料准备会（英文版，2026-09-11）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_EN.pptx.md`
- [[CI-06 COCO V6 第三轮试产测试结果]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/CI-06 COCO V6 3rd round trial.xlsx.md`

## Related Sources 关联来源

- [[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]
- [[2D Absorption Model v8 Simulation Report（二维吸收模型 v8 仿真报告）]]
- [[84 Sleeve 工程规格与换装防错设计]]
- [[BASF-YPC HySorb N7059 SAP 产品介绍（扬子石化-巴斯夫）]]
- [[BCNF as SAP Replacement - Feasibility Analysis（BCNF 替代 SAP 可行性分析 · 2026-04-13）]]
- [[Baby Diaper Absorbent Core Design（五层无浆 SAP 芯体设计方案与仿真 KPI）]]
- [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]]
- [[Botanical Extract Efficacy, Wetness Visualisation & Tri-Zone Lotion Review（植物提取物功效测试与验证）]]
- [[CI-06 COCO V6 第三轮试产测试结果]]
- [[CN 120285261 A（一种超吸收纸尿裤及其制备方法和应用·广东宜柔）]]
- [[CN 1330679 C（两性离子高吸水树脂及其制备方法·中国林科院林化所）]]
- [[COCO V6 Trial Code Design & Process Alignment（录音纪要 2026-08-17）]]
- [[COCO V6 Trial Round-2 Review（录音纪要 2026-09-16）]]
- [[COCO V6 试产原料准备会（Summary 版）]]
- [[COCO V6 试产原料准备会（v2 Final）]]
- [[COCO V6 试产原料准备会（英文版，2026-09-11）]]
- [[Citric Acid Crosslinked Cellulose Superabsorbent Hydrogels (CEJ 2025)]]
- [[Coco V6 试产原料清单（Raw material list v3.0）]]
- [[Diaper NPD Workshop Prep — Absorbency, Skin Health & Comfort Feature Map（2026-06-05）]]
- [[GB-T28004-2011 PH.doc]]
- [[GBP（From Nuoer）.docx]]
- [[High-Speed Core Forming Machine & SAP Dosing Design Review（录音纪要 2026-09-03 14-39）]]
- [[IPC BCC OI Materials Development Team 2026 Annual Review Outline（v7）]]
- [[IPC BCC OI 项目清单 2026 v2（2026-09-17）]]
- [[KR 10-2205294 B1（氧化淀粉-CMC-球形纳米纤维素高吸水体·Asiananotech）]]
- [[Material Portfolio & Process Priorities Review — SAP, Trilobal Fibre & Masterbatch（材料及工艺相关探讨）]]
- [[Nuoer Group 2026 Company Deck（诺尔集团 2026 版公司介绍）]]
- [[Nuoer High-GBP SAP Visit Plan & Roadmap（诺尔高GBP SAP拜访预案）]]
- [[One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）]]
- [[Raw Material STM - Nanjing Plant（原材料STM-NJ）]]


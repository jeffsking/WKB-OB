---
type: concept
title: "SAM Testing Methods（超级吸水材料测试方法）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-29
tags: [SAM, 超级吸水材料, 测试方法, Nuoer, 国标, 吸收, 通液, 密度]
---

# SAM Testing Methods（超级吸水材料测试方法）

> 一句话定义：**SAM = Superabsorbent Material（超级吸水材料，即芯体中的 SAP 形态）**。本页汇总本库编译的 SAM 测试方法族——来源分两条谱系：**诺尔（Nuoer）内部方法（WI-6607x，2025）** 与 **中国国家标准方法（China National Testing Method）**。每条子方法各有独立源摘要页；引用口径时必须注明所属谱系，切勿混为一谈。

## Definition 定义 / Lineage 谱系

- **Nuoer 谱系**：2025 年新引入，方法号 WI-66075 / WI-66076 等，普遍用 **0.9% NaCl、25±0.5 °C**，并规定特定加压（通液速度 0.3 PSI、加压吸收 0.9 psi）。样品量小（0.32 g / 0.9 g），偏来料快检。
- **国标谱系**：引用中国国家标准方法，按国标程序执行（本批 _08 吸收量/保水量、_09 密度/水分测定等）。口径与 Nuoer 不同，跨谱系数值不可直接比较。

## 子方法口径表（Caliber by sub-method）

| 子方法 | 谱系 | 关键口径 | 源摘要 |
|---|---|---|---|
| SAM 分布（Distribution） | 内部 SOP STM-4597 | 溴甲酚绿指示液，喷洒 152–254 mm，喷洒后 15–30 s 内与标准照片比对 | [[STM-4597纸尿裤SAM分布测试.docx]] |
| 通液速度（Liquid Speed） | Nuoer WI-66075 | 0.9% NaCl，0.32±0.005 g，0.3 PSI，T0/T1，速度 = 20×60/(T1−T0) mL/min | [[SAM通液速度(From Nuoer).docx]] |
| 加压吸收（Pressurized Absorption） | Nuoer WI-66076 | 0.9 psi，0.900±0.001 g，60 min，g/g=(B−A−0.9)/0.9 | [[SAM加压吸收(From Nuoer).docx]] |
| **SAM 含量（Content, Na⁺ ISE）** | **内部 SOP STM-00048（第 2 版）** | 氯化铵萃取 + 钠离子电极；NH₄Cl 1750±5 g/50 L；纯 SAP 四点标定 2/5/10/15 g；溶液 1500±10 g，搅拌 2 min、静置 ≥15 min；取 100±0.5 g + ISA 2±0.02 g；**电极斜率须在 54–60** | [[STM-00048 SAM含量.docx]] |
| 吸收量（Absorption Capacity） | 国标 WI-66078 | 0.200±0.001 g 茶袋（70×70 mm），0.9% 盐水浸没 30 min，滴水 10 min；g/g 双平行 | [[SAM吸收量(From China National Testing Method).docx]] |
| 保水量（Water Retention） | 国标 WI-66077 | 同上吸水后离心 1650 r/min（≈250 g）× 3 min；g/g | [[SAM保水量（From China National Testing Method）.docx]] |
| 吸收速度（Absorption Speed） | Nuoer WI-66079 | 2.000±0.05 g 入 50 mL 0.9% NaCl（23±2 ℃），600±5 rpm 旋涡消失法，2 次误差 <3 s | [[SAM吸收速度（From Nuoer）.docx]] |
| 密度（Density） | 国标 WI-66080 | 100 g 自然落料（漏斗孔口 40 mm、落距 40±1 mm）入 100±0.5 cm³ 杯；（M2−M1）/V | [[SAM密度(From China National Testing Method).docx]] |
| 水分测定（Moisture） | 国标 WI-66083 | 4 g、105±2 ℃ 烘 3 h、干燥器 30 min；恒重判据差 ≤0.4%；X=(M1−M2)/M1×100% | [[SAM水分测定(From China National Testing Method).docx]] |

> ⚠️ **禁止无来源参数**：上表已列口径来自单份 SOP/方法；合格阈值均未随方法给出，引用前回原文或验收标准确认。
> ⚠️ **谱系差异（2026-09-29）**：Nuoer 与国标同名为"吸收/保水"的方法，液体温度、样品量、加压条件不同，数值不可互推。

> ✅ 验证（2026-09-29，来源批次 S2_Areas_Test Method_08/_09 五份源页）：原「待补」五项口径已全部补齐（吸收量 WI-66078、保水量 WI-66077、吸收速度 WI-66079、密度 WI-66080、水分测定 WI-66083）。**吸收速度 WI-66079 与总表 Vortex（STM-00428）三主参数一致（2.000 g / 50 mL / 600±5 rpm）**，属同族方法；**保水量 WI-66077 与 CRC 同为 250 g × 3 min 离心**，可与 WSP 241.2 对表。各方法均为单源，数值引用须附方法号。

## 相邻概念

- 材料对象：[[SAP（高吸水树脂）]]、[[SAP性能指标（CRC AUL GBP Vortex）]]（AUL 与加压吸收同源）
- 终态形态：[[Liquid Diffusion Test（液体扩散测试）]]
- 供应商：[[诺尔（Nuoer）]]

## 经验教训

- **谱系即口径**：引用 SAM 数值必带"Nuoer / 国标"标识，否则不可比。
- ~~**待补 `[待补]`**：吸收量、保水量、吸收速度、密度、水分测定五项口径~~ ✅ 已于 2026-09-29（批次 _08/_09）补齐，见上方子方法口径表与验证记录。


> ✅ 验证（2026-09-29，来源 [[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]]、[[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]]）：SAM 的**成型分布判读**与**材料性能判读**是两条独立链路——前者用 **China-STM-03（SAM Island / Heavy Lane，判据为纵向连续或累计长度 > 吸收体总长 1/2）**、**China-STM-04（REL 下层自由 SAM 抖落称重，精度 0.01 g）**、**TTM-03（REL 下层 SAM 剥离称重）**；后者仍是 PSD / GBP / CRC / AUL / Vortex 五指标。**前者输出 mm 与 g，与后者 g/g 类指标不可换算**，引用时须标明是「分布判读」还是「材料性能」。

## 追加：Open Innovation 批（2026-09-29 追加）

> 本节为 **Resources / Open Innovation 批（批次 S4_Resources_Open Innovation_05）** 编译时的追加记录，**不改动上方既有结论**。上方"AUL 编号在本库并存 STM-00020 / STM-00220 / 内控-9"的编号冲突在本批**得到一次独立复核**；本节补充**一份完整的标准对照表**与两项新增编号。

### 1. 本批新增：KC 内部方法 ↔ EDANA/INDA 标准对照

| 测试项 | 缩写 | KC 内部方法（本批来源） | EDANA/INDA 对应 | 与上方既有记录的对照 |
|---|---|---|---|---|
| 离心保留容量 | CRC | **STM 00219** | **WSP 241.2** | 与上方一致 |
| 载荷下吸收量 | AUL | **STM 00220** | **WSP 242.2** | 与上方"STM-00020（PAN 法，总表）/ STM-00220（天津现场）并存"**吻合——本批再次出现 STM 00220** |
| 凝胶床渗透性 | GBP | **STM 00229** | — | 上方记为 **STM-00229-1**，本批为 **STM 00229** → 疑为主编号与版本/子编号关系，**未确认** |
| 涡流时间 | Vortex | **STM 00428** | — | 与上方一致 |
| 粒径分布 | PSD | **STM 00230** | **WSP 220.2** | 与上方一致 |
| 含水率 | Moisture | **STM 00378 / 00278** | **WSP 230.2** | **本批新增** |
| 粉尘 | Dust | **STM 00471** | — | **本批新增** |

> ⚠️ **编号冲突仍在（2026-09-29，未裁决）**：**AUL** 已出现 **STM-00020**（总表 PAN 法）与 **STM-00220**（天津现场 + 本批来源）；**GBP** 出现 **STM-00229** 与 **STM-00229-1**。本页**不裁决、不合并**，引用时须**附厂别与完整编号**。

### 2. 验证记录

> ✅ 验证（2026-09-29，来源 [[Nuoer High-GBP SAP Visit Plan & Roadmap（诺尔高GBP SAP拜访预案）]]）：本页既有编号体系被**独立来源复现**（CRC 00219、AUL 00220、GBP 00229、Vortex 00428、PSD 00230 全部一致），并补齐**含水率与粉尘**两项的方法编号。原页结论**未被修正**；AUL 与 GBP 的编号分歧**仍未解决**，维持并列记录。

- **追加 `[待验证]`**：STM-00229 与 STM-00229-1 的关系；STM-00020（PAN 法）与 STM-00220 是否为同一方法的不同版本；WSP 242.2 与 PAN 法 AUL 的结果偏差量级。

## 来源

- [[Nuoer High-GBP SAP Visit Plan & Roadmap（诺尔高GBP SAP拜访预案）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/Nuoer高GBP_SAP拜访讨论计划与开发路线图_20260708.docx.md`（2026-09-29 追加：标准对照表）
- [[STM-4597纸尿裤SAM分布测试.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-4597纸尿裤SAM分布测试.docx.md`
- [[SAM通液速度(From Nuoer).docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/SAM新引入测试方法-20250410/SAM通液速度(From Nuoer).docx.md`
- [[SAM加压吸收(From Nuoer).docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/SAM新引入测试方法-20250410/SAM加压吸收(From Nuoer）.docx.md`
- [[Raw Material STM - Tianjin Mill WI-60632（原材料标准测试方法-TJ）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM原材料-TJ.pdf.md`
- [[Raw Material STM - Nanjing Plant（原材料STM-NJ）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/原材料STM-NJ.pdf.md`
- [[Raw Material Testing Method Summary（原材料测试方法汇总表）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/Raw Material Testing Method Summary.xlsx.md`

> ✅ 验证（2026-09-29，来源上述三份）：本页原「待补」的五项口径已部分补齐——**速率**（2.000 g / 50 mL / 600 ± 5 rpm 漩涡消失法）、**CRC**（0.200 g 浸 30 min、F = 250 g、3 min）、**AUL**（0.900 g、加载 60 min）、**PSD**（100 g、Ro-Tap 五层筛 850/600/300/90/45 μm、10 min）。总表另给出正式编号：**PSD = STM-00230、GBP = STM-00229-1、CRC = STM-00219、AUL = STM-00020（PAN 法）、Vortex = STM-00428**。**新增风险**：AUL 编号在本库并存 **STM-00020**（总表）与 **STM-00220**（天津现场），南京则用「内控-9」——已标 manual_review，确认前引用须附厂别与编号。
- [[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/CoCo Product-REL Width, SAM Width in REL, LSS and PSS width China STM-05 20200303.pdf.md`
- [[STM-00048 SAM含量.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-00048 SAM含量.docx.md`（2026-09-29 追加：SAM 含量钠离子电极法）

## 追加：成品 SAM 含量法（2026-09-29 追加，不改动上方既有结论）

> 本节为 **Areas / Test Method 批次 05** 编译时的追加记录。上方子方法表新增一行 **「SAM 含量（Content, Na⁺ ISE）」**，**原结论未修改**。

### 新增子方法的定位

| 项 | 内容 | 出处 |
|---|---|---|
| 方法编号 | **STM-00048**（第 2 版，2021-08-24，南京厂成品） | [[STM-00048 SAM含量.docx]] |
| 测的是什么 | **成品中 SAM 的占比**（化学反推量），而非 SAM 的吸收性能 | 同上 |
| 原理 | SAM（聚丙烯酸钠系）是产品内钠的主要来源 → 用 NH₄Cl 萃取钠 → **钠离子选择电极**定量 → 反推 SAM 含量 | 同上 |
| 与既有子方法的区别 | 既有子方法（通液速度/加压吸收/分布）测 **SAM 的行为**；本方法测 **SAM 的量** | 同上、[[SAM通液速度(From Nuoer).docx]] |
| 标定 Calibration | 纯 SAP 四点 **2 / 5 / 10 / 15 g（±0.01 g）**，低→高浓度依次标定 | [[STM-00048 SAM含量.docx]] |
| 可用性闸门 Gate | 四点标定后**电极斜率须落在 54–60**；斜率**每月至少检查一次** | 同上 |
| 主要误差源 | 器皿**钠残留**；撕样时 **SAP 蹦出测试袋**（取样无效） | 同上 |

> ⚠️ **口径提示（2026-09-29）**：本方法输出的是**含量（占比）**，与 [[STM-4597纸尿裤SAM分布测试.docx]] 输出的**分布形态（mm / 照片比对）**维度不同，**两者互补但不能互相替代**——含量达标不代表分布达标。
> ⚠️ **待验证 `[待验证]`**：STM-00048 原文未给出"钠浓度 → SAM 含量"的换算式与合格阈值，引用前须回原文或配套标准确认。

## Related Sources 关联来源

- [[1780441413117.jpg]]
- [[2025.03.26 - Learning Cycle Update]]
- [[CD Pants产品学习]]
- [[CI-06 COCO V6 3rd round trial-10.10]]
- [[CI-06 COCO V6 3rd round trial-9.30]]
- [[COCO_V6_第三轮trial_两组对照分析_20261010]]
- [[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]]
- [[Document]]
- [[Finished Product Testing Method Summary（成品测试方法汇总表）]]
- [[GBT28004.1-2021面层附着物.doc]]
- [[IMA知识库索引_20261009]]
- [[Inertia在美国推出生物基芯体卫生巾：韩国女性科技品牌引入专利植物源吸收技术]]
- [[JD - IPC BCC Material Development Engineer（材料开发工程师岗位说明书）]]
- [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]]
- [[Nuoer High-GBP SAP Visit Plan & Roadmap（诺尔高GBP SAP拜访预案）]]

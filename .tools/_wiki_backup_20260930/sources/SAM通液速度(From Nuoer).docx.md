---
type: source
title: "SAM通液速度(From Nuoer).docx"
source_type: 内部测试方法 / SOP（供应商方法）
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/SAM新引入测试方法-20250410/SAM通液速度(From Nuoer).docx.md
original_link: ""
date_published: 2025-02-12
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "WI-66075 (Nuoer, Rev.1, 2025-02-12) measures SAM liquid-transport speed: 0.32 ± 0.005 g of SAM swollen 30 min in 150 mL of 0.9% NaCl is placed in a flow tube, and the time for the meniscus to fall from the 60 mL mark to the 40 mL mark is recorded as T1, against a blank T0."
  - "Caliber 口径: applied load 0.3 PSI (pressure shaft + weight), 30 s settling before opening the stopcock; speed (mL/min) = 20 × 60 / (T1 − T0)."
  - "Instrument gate: blank T0 must fall in 7 ± 5 s; if > 12 s the filter must be cleaned (or burned off / replaced) — this is the method's only quality gate."
pages_linked: ["[[SAM Testing Methods（超级吸水材料测试方法）]]", "[[诺尔（Nuoer）]]", "[[SAP性能指标（CRC AUL GBP Vortex）]]"]
---

# SAM通液速度(From Nuoer).docx

## 一句话定位

**诺尔（Nuoer）2025 年新引入的 SAM 来料快检方法 WI-66075**：测 **SAM 在 0.3 PSI 加压下的通液速度（mL/min）**——即膨胀后的 SAP 颗粒床让液体通过的能力，是 **GBP（凝胶床渗透性）类指标**的供应商版本。

## 摘要

仪器准备：打开天平**静放 10 min**并用法码校准；配 **0.9% 氯化钠溶液**；计时器清零。样品：SAM 原材料样品**置于密封袋内**。步骤：① 量取 **150 mL** 0.9% NaCl 倒入 **200 mL 烧杯**；② 称取 **0.32 ± 0.005 g** 试样加入烧杯；③ **放置 30 min** 使其充分膨胀；④ 往已关闭活栓的通液管内注满 0.9% NaCl，打开活栓放流，液面接近管底时关闭活栓，**确认活栓与滤器之间无空气**；⑤ 再次注入溶液至**液面高于 60 mL（中间刻度线）5 cm** 处，放入加压轴与砝码，打开活栓放流，测定液面从 **60 mL 降至 40 mL（下刻度线）** 所需时间，记为 **T0**——**T0 的适当范围是 7 ± 5 s**；**若超过 12 s，须清洗滤器表面**（清洗后仍超时可用火烧掉堵住网眼的样品；仍达不到 7 ± 5 s 则**更换滤器**）；⑥ 关闭活栓，把膨胀好的 SAM 连同溶液一起倒入通液管，并用管内溶液冲洗烧杯确保 SAM 全部转入；⑦ 打开活栓使液面降至 60 mL 以上 5 cm 处，**放入加压轴与砝码（合计 0.3 PSI）**，**放置 30 s**（排出加压轴网眼上的空气）；⑧ 打开活栓放流，用秒表测液面从 **60 mL 降至 40 mL** 的时间，记为 **T1**；⑨ **测试进行 2 次**，两次相差很大时须再测；⑩ **通液速度（mL/min）= 20 × 60 / (T1 − T0)**；两次测试的**算术平均值为结果，保留小数点后一位**。

## 提炼的数字与结论

| 项目 Item | 数值 / 结论 Value | 备注 Note |
|---|---|---|
| 方法编号 Method ID | **WI-66075**（诺尔，第 1 版，2025-02-12） | 供应商方法，2025 新引入 |
| 样品量 Sample mass | **0.32 ± 0.005 g** | 小样品、来料快检 |
| 液体 Liquid | **0.9% NaCl**，150 mL（200 mL 烧杯） | — |
| 预膨胀 Pre-swelling | **30 min** | 膨胀后才可测 |
| 加压载荷 Load | **0.3 PSI**（加压轴 + 砝码合计） | 明显低于加压吸收的 0.9 psi |
| 加压稳定 Settle | 放入加压轴后**放置 30 s** | 排网眼空气 |
| 计量区间 Measure window | 液面 **60 mL → 40 mL**（20 mL） | 中间刻度线 → 下刻度线 |
| 空白判据 Blank gate | **T0 = 7 ± 5 s**；**> 12 s** 须清洗/火烧/更换滤器 | **本方法唯一质量闸门** |
| 计算式 Formula | **通液速度（mL/min）= 20 × 60 / (T1 − T0)** | 分子为 20 mL × 60 s |
| 重复与取值 Replication | **2 次算术平均**，保留 **1 位小数**；差异大须加测 | — |
| 合格阈值 Threshold | 原文未给 `[待验证]` | 需与采购规格配对 |

> ⚠️ **口径提示（2026-09-29）**：本方法属 **Nuoer 谱系**，与国标谱系的同名指标**不可互推**（见 [[SAM Testing Methods（超级吸水材料测试方法）]]）；与 [[SAM加压吸收(From Nuoer).docx]]（WI-66076，0.9 psi / 0.900 g / 60 min）**样品量与载荷都不同**，是**两个独立指标**。
> ⚠️ **待验证 `[待验证]`**：T0 的"7 ± 5 s"区间意味着 **T1 − T0 可能接近 0 甚至为负**（当 SAM 通液快于空白时），原文未给出该情形的处理规则。

## 关键论断（key_claims）

- **通液速度是"颗粒床渗透性"的供应商版读数，与 GBP 同源但口径不同** —— 支撑页：[[SAP性能指标（CRC AUL GBP Vortex）]]
- **空白 T0 的 7 ± 5 s 闸门比样品读数更关键** —— 支撑页：[[SAM Testing Methods（超级吸水材料测试方法）]]
- **0.3 PSI 与 0.9 psi 是 Nuoer 两条方法的分水岭** —— 支撑页：[[SAM加压吸收(From Nuoer).docx]]

## 关联页面

- 概念：[[SAM Testing Methods（超级吸水材料测试方法）]]、[[SAP性能指标（CRC AUL GBP Vortex）]]、[[Gel Blocking（凝胶阻塞）]]
- 实体：[[诺尔（Nuoer）]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/SAM新引入测试方法-20250410/SAM通液速度(From Nuoer).docx.md`
- 原文链接：（无；供应商方法）
- 同族文档：[[SAM加压吸收(From Nuoer).docx]]（WI-66076）

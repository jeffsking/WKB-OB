---
type: source
title: "REL增强层专项对比分析_6样品benchmark_20260924"
source_type: 研报
source_path: RAW/ima_sync/个人知识库/WKB/REL增强层专项对比分析_6样品benchmark_20260924.md.md
original_link: ""
date_published: 2026-09-24
date_processed: 2026-10-13
credibility: 中
knowledge_update_status: pending
key_claims:
  - "6-sample REL benchmark (4 baselines + Code A 28.8 gsm + Code B 33.48 gsm): both Codes win on CD-direction mechanics and in-plane balance — CD normalised strength 18.65 / 17.05 gf/gsm rank #1/#2 of 6 (baseline mean 10.67), CD/MD ratio 0.283 / 0.243 rank #1/#2 (baseline mean 0.165)"
  - "Shared penalty: liquid penetration — Code B 1.232 s (slowest), Code A 1.02 s (2nd slowest), vs baseline mean 0.51 s; but both far below the KC pass threshold (3.5 s), so this is a relative, not absolute, weakness"
  - "Code A exclusive: Hold-住-SAM% = 62%, the only sample with data and reaching the 60% level (+47.6% vs best baseline ZB 42%); Code B not tested → the single biggest evidence gap"
  - "Code B exclusive: Wet-back = 0.0474 g, best of all six (−32.3% vs baseline mean, −47.3% vs Code A) — counter-intuitive against its slowest penetration"
  - "A↔B has no single winner: B leads 4 metrics, A leads 4, 6 neutral, 1 no-data; choice depends on whole-diaper priority (rewet → B, liquid transport/structure openness → A, SAP retention → undecidable without Code B Hold-SAM)"
  - "Mechanism: baselines show monotic 'porosity↑ → Hold-SAM↑, penetration↓', but both Codes depart in opposite directions → performance is driven by fibre functionalisation and inter-layer structure, not loft; YJ (dense, Hold-SAM only 4%) confirms density alone yields no benefit"
  - "Risk hypothesis: both Codes share 30% hollow-fibre fraction (2.1× the 14% baseline); NEW REL 4 warns oven >155 °C collapses the hollow lumen; the two Codes are exactly the two slowest penetrations → lumen-collapse hypothesis to verify by cross-section SEM + oven-temperature sweep"
  - "Evidence boundary: 8 of 10 KC qualification metrics untested for all six samples (Void Volume @0.5 kPa, compression recovery, ATB wet bond strength all blank) → neither Code can be declared qualification-passed; Code A/baselines are single-point observations (n unstated)"
  - "Caveats: Code B strength unit unstated (if N/2inch all strength conclusions void); thickness pressure differs (0.2 kPa vs unstated); both Codes' design formulations are compositionally identical — kg difference source to be reconciled; Code B tested under a possibly different protocol"
pages_linked: ["[[REL增强层]]", "[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]", "[[福建闽瑞新合纤]]", "[[延江（Yanjan）]]", "[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]", "[[SAP（高吸水树脂）]]", "[[COCO芯体平台]]", "[[REL benchmark.png]]"]
---

# REL 增强层专项横向对比分析 —— 6 组样品 benchmark（4 常规基线 + Code A + Code B）

## 一句话定位 Positioning

The **third sub-report** of the COCO V6 round-3 trial series: a horizontal benchmark of **six REL (Reinforcement Enhancement Layer) samples** — 4 conventional baselines plus two independently-named Codes (Code A 28.8 gsm / Code B 33.48 gsm) — across 16 metrics, intended to position the two new Codes against the current candidate field and against each other. （中文对照：COCO V6 第三轮 trial 的第三组子报告，把两个新 Code 与 4 组常规 REL 基线做 16 项指标横向对标。）

> REL = Reinforcement Enhancement Layer — the nonwoven layer between the two SAP layers of a 100% SAP core; four functions: **structure separation, liquid-transfer bridge, rebound/loft retention, SAP-migration blocking**.

## 摘要 Summary

The report analyses **6 samples** — baselines YJ DL24C, DY ND055, ZB 箱式REL, 芥东 箱式REL, plus **Code A** (newly developed REL, 28.8 gsm, all-Minrui 5-component blend) and **Code B** (REL Minrui, 33.48 gsm measured, n=5, from the CI-06 COCO V6 3rd-round trial). 13 of 16 metrics are complete across all six; **Wet-back** is valid for 5 (ZB missing) and **Hold-SAM%** for 5 (Code B missing). Both Codes share the consensus advantages of **CD-direction strength and in-plane balance** and the consensus penalty of **slow liquid penetration**, but each holds a distinct exclusive win (Code A: Hold-SAM%; Code B: Wet-back), leaving **no single winner between A and B**. A major observational caveat is that the two Codes' **design formulations are compositionally identical** (Code B's bi-layer weights fold to 70% PE/PET + 24% PTT/PET + 6% PVA = Code A), so any performance difference must come from **basis weight / thickness / forming process**, not material system. （中文对照：两 Code 配方逐组分同构，性能差异只能来自克重/厚度/成型工艺。）

## 提炼的数字与结论 Numbers & findings

### Samples & formulations 样品与配方

| 样品 | 角色 | 组分/克重 | 数据源 |
|---|---|---|---|
| YJ DL24C | 基线 B1 | 60% 博爱 CoPET(2D)+40% 仪征 PET(3D)，39.8 gsm | REL benchmark.png |
| DY ND055 | 基线 B2 | 50% 汇维仕 CoPET(6D)+50% 江南 PET(12D)，38.8 gsm | REL benchmark.png |
| ZB 箱式REL | 基线 B3 | 4 组分（仪征 PET+蕊滨 PE/PP+安顺 PE/PET+Lyocell），40.0 gsm | REL benchmark.png |
| 芥东 箱式REL | 基线 B4 | 3 组分（江南/新维狮 PET+PP），40.0 gsm | REL benchmark.png |
| **Code A** | 本文方法 A | 32% 2D + 8% 3D + 30% 中空 + 24% PTT/PET + 6% PVA（全闽瑞），**28.8 gsm** | REL benchmark.png |
| **Code B** | 本文方法 B | 上 11.2 gsm＋下 16.8 gsm（KET 系列 PE/PET 皮芯 + PTT/PET + PVA），**33.48 gsm（设计 28）** | CI-06 xlsx，n=5 |

### Key results 关键结果

| 指标 | Code A | Code B | 基线均值 | 位次（6 组） |
|---|---|---|---|---|
| CD 归一化强度 (gf/gsm) | **18.65** | **17.05** | 10.67 | **#1 / #2** |
| CD/MD 强度比 | **0.283** | **0.243** | 0.165 | **#1 / #2** |
| 穿透时间 (s) ↓ | 1.02 | **1.232** | 0.51 | #5 / #6（最慢） |
| Hold 住 SAM% ↑ | **62%** | 未测 | 23.5%（最优基线 ZB 42%） | #1（唯一有数据） |
| Wet-back (g) ↓ | 0.0698 | **0.0474** | 0.0700 | 5 组有效，Code B 最优 |
| KC 门槛 | 穿透合格 3.5 s | — | — | 两 Code 均远低于门槛 |

- **Code B 独占**：绝对力学（MD +23.7%、CD +6.3% vs A）、回渗（−47.3% vs A）、MD 归一化强度（+6.4%）。
- **Code A 独占**：穿透（快 17.2%）、结构开度（VV 高 36.8%）、CD 归一化强度（+9.4%）、CD/MD 比（+16.4%）。
- **中性项**：克重、厚度、堆密度、孔隙率、MD/CD 延伸率。

## 关键论断 Key claims

- **两 Code 的共识优势 = CD 向力学与面内均衡**：以更低的克重获得优于常规方案的面内承载与均衡性 —— 支撑页：[[REL增强层]]
- **两 Code 的共识代价 = 液体穿透**：唯二超过 1 s 的样品，但**是相对劣势、非绝对不达标**（KC 合格 3.5 s）—— 支撑页：[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]
- **A↔B 无单一胜者**：选择取决于整裤优先级（回渗→B；输运/结构开度→A；SAP 保持→须补测 Code B 的 Hold-SAM%）—— 支撑页：[[REL增强层]]
- **机理**：性能由**纤维功能化组合与层间结构**决定，而非蓬松度（两 Code 从相反方向同时偏离基线规律）—— 支撑页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- **失效风险假设**：两 Code 中空纤维占比同为 30%、穿透同为最慢两位 → **lumen 坍塌**待截面 SEM + 烤箱温度扫描验证
- **资质边界**：10 项 KC 资质指标 8 项六组全员未测 → **两 Code 均不能宣布资质通过**

## 建议动作 Recommended actions（节选）

| 优先级 | 动作 |
|---|---|
| **P0** | 补测 Code B 的 Hold 住 SAM% → 唯一能区分两 Code 定位的关键空白 |
| **P0** | 复核 Code B 的 MD/CD 强度单位（是否 N/2inch）→ 若不符，全部强度结论作废 |
| **P0** | 补测 Void Volume @0.5 kPa、压缩回弹 4×@1 kPa、ATB 湿态结合强度 → 三项决定性资质指标全空白 |
| **P0** | 两 Code 截面 SEM / 中空 lumen 保留率 → 直接验证结论 7 的坍塌假设 |
| P1 | 核对 Code B 与 4 基线是否同法测 Wet-back（决定结论 4 强度）；ATB 烤箱温度扫描 145→155 °C；澄清 Code B 实测 33.48 gsm 超设计 19.6% 的原因 |

## Source 来源

- 本地路径（判重锚）：`RAW/ima_sync/个人知识库/WKB/REL增强层专项对比分析_6样品benchmark_20260924.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/REL增强层专项对比分析_6样品benchmark_20260924.md.md`
- 原始类型：IMA markdown 条目（media_type 7）；正文经**通道 B**（`get_media_info` 签名 URL）于 2026-10-13 下载原件（本会话 MCP 不可用、REST 笔记通道配额耗尽，故走原件通道）。
- 数据源：Code A + 4 基线 ← IMA《REL benchmark.png》；Code B ← IMA《CI-06 COCO V6 3rd round trial.xlsx》[Material Test] REL 段（n=5）。
- 判据源：IMA《NEW REL 4.pptx》（KC REL Qualification Test Matrix，10 项）。
- 备注：报告自述为「第三组子报告」，主报告为《COCO_V6_第三轮trial_两组对照分析报告_20260924.md》。含 8 条口径分歧（C1–C8），引用结论时须同步声明。

## 关联页面

- 概念：[[REL增强层]]、[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]、[[Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）]]、[[SAP（高吸水树脂）]]
- 实体：[[福建闽瑞新合纤]]、[[延江（Yanjan）]]
- 平台/源：[[COCO芯体平台]]、[[REL benchmark.png]]

---
type: source
title: "ONE-PAGE OI PROJECT PROFILE - REL&Trilobal Liner（项目一页纸 · 2026-10-26/27）"
source_type: 研报
source_path: RAW/ima_sync/个人知识库/WKB/Projects/Template/ONE-PAGE OI PROJECT PROFILE - REL&Trilobal Liner.pptx.md
original_link: ""
date_published: 2026-10-27
date_processed: 2026-10-27
credibility: 高
credibility_note: "内部项目定稿材料（CONFIDENTIAL），数据与 [[CI-06 COCO V6 3rd round trial - final]] 及 [[REL_Cost_Model_28gsm_vs_40gsm]] 完全对齐，构成双源互证；明确标注了 Open Data Gaps（未测项），未夸大结论（对 REL 的判定是 REVISE 而非 GO），属诚实披露。"
knowledge_update_status: done
key_claims:
  - "**REL 项目正式判定为 REVISE（返修）**：10 项资格判据中仅 2 项已测，且两者均为**材料级代理指标而非装配级**；唯一一次装配级对比（Code 14 vs Control-2）显示**净权衡** —— 材料收益未在产品级兑现"
  - "**五纤维配方焊死为 32/8/30/24/6**（2D ES CoPET/PET 32% + 3D ES 8% + 4D 中空 ES 30% + 7D PTT/PET S/S 24% + 6D PVA 6%），Code A（28.8 gsm）与 Code B（33.48 gsm）**共用同一配方，仅克重与层结构不同** —— 这把「配方」与「克重」两个变量解耦，是本项目实验设计的关键进步"
  - "**材料级 SAP 保持率 62% vs 基线均值 23.5%（2.6 倍）**，但代价明确：Code A 的回渗是五个测量样本中**最高**（0.09 g）、穿透时间**第二慢**；Code B 回渗最好（0.0474 g）但穿透最慢（1.232 s）—— **两个 code 占据全组最慢穿透的两个席位**"
  - "**成本已过线、克重才是命门**：基线 40 gsm 0.6920 元/m²、33 gsm 实测 0.6537（−5.5%）、28 gsm 设计 0.5547（−19.8%）；**临界 34.93 gsm**，实测 33.48 gsm 仅余 **1.45 gsm** 余量。吨价溢价 +14.5%（19,810 vs 17,300）靠 −27% 质量节省对冲"
  - "**三个 Open Data Gap 被明确列出（不是含糊带过）**：① **Void volume @0.5 kPa 未测**——此前引用的 34.3 cm³/g 是**另一基材上的无应力估算**，不可用于本项目；② 压缩回复（4× @1 kPa）两个 code 均未测；③ 横向均匀性**已实测为缺陷**：左→右 +3.34 gsm / +12.4%"
  - "**Baymax 三叶异形面层平台：机理成立、代价明确**。Cradle MD 扩散 205 → 241.6 mm（+17.9%，超 +15% 设计目标，t=15.9）；真正的意外收益是**产能而非速度**——2nd/3rd 次吸入 +36%/+35%（等垫重）；代价是 GB 回渗翻倍 0.492 → 0.990 g（+101%）与侧向吸入变慢 33%"
  - "**三叶面层的工艺红线**：≥142 ℃ 会**磨圆异形截面**（"加了等于没加"），试验须压在 139 ℃ 以下；压力粘合无效，须线性超声（≈US$70k，500 m/min 但占地面）；PET 面层在超声密封道中充当**未粘合填充物**导致强度无声下降（HIGH 风险）"
  - "**路径已排到 2027**：REL = 材料基准（2026-09 已完成，6 样本）→ 产品三臂（2026 Q4，解 supplier vs basis weight）→ 放大锁定（2027 Q1，成本平衡点）→ 量产移交（2027 Q2，TRL 6）；Baymax = 2026 Q4 修回渗 → 2027 离线 600 m + 在线 500 m → 商务（待成本与回渗门）"
pages_linked: ["[[REL增强层]]", "[[Multilayer SAP Core（多层SAP芯体）]]", "[[REL_Cost_Model_28gsm_vs_40gsm]]", "[[CI-06 COCO V6 3rd round trial - final]]", "[[三叶形截面纤维（Trilobal Fibre）]]", "[[延江（Yanjan）]]", "[[恒碳（Hengtan）]]", "[[SAP 吸水纸（SAPP）]]"]
compile_mode: semantic
---

# ONE-PAGE OI PROJECT PROFILE - REL & Trilobal Liner

## Positioning 一句话定位

The project's **external-facing single source of truth**: two OI profiles (REL reinforcement layer, Baymax trilobal liner) on two pages, each carrying gate status, TRL, the measured table, the cost case, and — critically — an explicit list of what has **not** been measured. For the REL project this is the document that replaces optimism with a REVISE verdict.

本页是项目的**对外单一事实源**：两页纸承载两个 OI 项目（REL 增强层、Baymax 三叶异形面层），每页都含 gate 状态、TRL、实测表、成本案，以及最关键的一项——**明确列出哪些没测**。对 REL 项目而言，这份文件用 REVISE 判定取代了乐观叙事。

## Profile 01 · REL Reinforcement / Enhancement Layer

### Status & Challenge 状态与挑战

| 项 | 值 |
|---|---|
| 结构 | 双层 SAP 之间的 **5 纤维增强薄毡（reinforcement veil）** |
| 克重 | Code A 28.97 ± 1.61 gsm（n=30）；Code B **33.48 gsm（+19.6%）**；标称基数 33.48 gsm |
| 厚度 | 2.758 mm |
| 材料级 SAP 保持 | **62 %**（基线均值 23.5%） |
| 产品级结论 | **净权衡，非已证收益** |
| Gate | **G2 · 天津验证**（TRL 4，lab → pilot，目标 2027 H2 上市） |
| Verdict | **REVISE** |

### Formulation 五纤维配方（32 / 8 / 30 / 24 / 6）

| 纤维 | D × L | % | 角色 |
|---|---|---|---|
| 2D ES CoPET/PET | 2.0D × 38 | 32 | 细毛细 + 主粘结 |
| 3D ES CoPET/PET | 3.0D × 38 | 8 | 次级毛细 + 粘结 |
| 4D 中空 ES | 4.0D × 38 | 30 | Z 向通道 + 管腔空隙 |
| 7D PTT/PET S/S | 7.0D × 51 | 24 | 回弹 / 抗凝胶阻塞 |
| 6D PVA（水不溶） | 6.0D × 51 | 6 | Z 向骨架 / 湿强 |

> **Code A 与 Code B 共用同一配方**，仅克重与层结构不同 —— 这是把「配方效应」与「克重效应」解耦的实验设计。

### Product Test 成品级对照（Code 14 vs Control-2）

> 全芯体组装 · GB 28004 + Cradle + L/H · n = 5/4/4 · 测试日 2026-09-30

| 指标 | Code 14 | Control-2 | Δ | 判读 |
|---|---|---|---|---|
| 一次吸收 GB (s) | 24.10 | 25.66 | −6.1 % | ↑ |
| 二次吸收 GB (s) | 25.03 | 28.67 | −12.7 % | ↑ |
| 回渗 GB (g) | 0.500 | 0.492 | +1.6 % | = |
| **渗漏 GB (g)** | **0.650** | **0.466** | **+39.5 %** | **↓** |
| **Cradle 三次吸入 (s)** | **57.58** | **39.68** | **+45.1 %** | **↓** |
| L 吸入 (s) | 9.70 | 7.77 | +24.9 % | ↓ |
| H 吸入 (s) | 17.93 | 14.68 | +22.1 % | ↓ |
| L 回渗 (g) | 0.147 | 0.195 | −24.4 % | ↑ |
| L 残留 (g) | 0.015 | 0.100 | −85.0 % | ↑ |
| H 残留 (g) | 0.010 | 0.055 | −81.8 % | ↑ |

**Net trade-off**：retention（残留 −80~85%）与 lower-body rewet（L 回渗 −24%）的收益，被 leakage（+39.5%）与 late-insult intake（+22~45%）抵消。**材料收益未在产品级兑现**；且本次同时动了两个变量（供方 + 克重），收样日期相差 7 天 —— 不可归因单一因素。

### Cost 成本案（vs 官方 40 gsm 基线）

| 方案 | 全成本 元/m² | vs 基线 |
|---|---|---|
| 基线 40 gsm（17.3k 元/t） | **0.6920** | 参照 |
| 新 REL · 33 gsm 实测 | **0.6537** | **−5.5 %** |
| 新 REL · 28 gsm 设计 | **0.5547** | **−19.8 %** |
| **临界克重** | **34.93 gsm** | 打平点 |

> 结论原文：**"Basis weight, not fibre price, decides the business case."** 吨价 +14.5%（19,810 vs 17,300）仅在实际克重低于 34.93 gsm 时才被 −27% 质量节省抵消；实测 33.48 gsm **只剩 1.45 gsm 余量**。年度口径（1 亿片）：设计 211 万 / 实测 248 万 vs 基线 263 万元，分别省 52 万 / 15 万元。

**价格基准**（含税到厂）：PTT/PET S/S 20,500（恒碳千吨级 20,000–21,000；26,000 小样价不适用）· PVA 6D 20,000（皖维）· ES 2D/3D 11,600 · 中空 ES 13,500（待核）· 加工 5,000。**未含**：3–5% 工艺损耗、分切废料、打样摊销、关税与认证。

### Material Benchmark 六样本材料级基准

| 样本 | gsm | mm | STT (s) | 回渗 (g) | SAM % |
|---|---|---|---|---|---|
| Code A · 新 REL | 28.8 | 1.01 | 1.02 | 0.09 | **62** |
| Code B · Minrui | 33.48 | 0.865 | 1.232 | **0.0474** | n/a |
| YJ DL24C | 39.8 | 0.71 | 0.77 | 0.06 | 4 |
| DY ND055 | 38.8 | 1.13 | 0.55 | 0.07 | 15 |
| ZB 箱式 REL | 40.0 | 1.77 | 0.23 | n/a | 42 |
| 桥东箱式 REL | 40.0 | 2.02 | 0.49 | 0.08 | 33 |
| **基线均值** | 39.65 | 1.41 | 0.51 | 0.07 | **23.5** |

> 口径警告（原文如实交代）：**各来源方法不同，克重与厚度也不同，因此不存在单一排序**。SAM = 迁移测试后 REL 中保有的 SAP（内部方法，无 KC 阈值）；STT 与回渗是材料级，KC 判据是装配级，**只能作方向性参考**。

## Profile 02 · Baymax Trilobal Profiled-Fibre Liner

### Concept 技术概念

三叶（trilobal）截面纤维 + 在线超声粘合，实现 **MD 方向铺展而不增加克重**。机理：三叶沟槽形成轴向通道，梳理后与 MD 对齐，液体沿机器方向被抽走而不是堆在冲击点。**沟槽吸力 ≈40–50 kPa vs 孔网 ≈1–2 kPa；同等旦数下表面积 ≈圆纤维的 300%**。

### Composition 面层构成（Code 1 · 50 gsm · 4 层 × 102 mm）

| 层 | 纤维 | gsm | % | 角色 |
|---|---|---|---|---|
| Top A1 | 2D Bico PE/PET | 22.5 | 90 | 贴肤柔软 + 平面铺展起点 |
| Top A2 | 三叶 3D PET | 2.5 | 10 | 表面沟槽起始（贴肤侧仅 10%） |
| Bottom B1 | 4D Bico PE/PET | 12.5 | 50 | 蓬松、花型深度、压缩回复 |
| Bottom B2 | 三叶 3D PET | 12.5 | 50 | 主沟槽网络（合计 30% = 15 gsm） |

来料 n=5：45.22 gsm（比标称 50 低 9.6%）、1.72 mm、pH 7.11、剥离力 115.28 N。

### Product Test 成品对照（Code 3 vs Control 2，同芯同胶，仅换面层）

| 指标 | Control 2 | Code 3 | Δ | 显著性 |
|---|---|---|---|---|
| **MD 铺展 — Cradle (mm)** | 205.0 | **241.6** | **+17.9 %** | ✓ 达标 +15% |
| MD 铺展 — L-H (mm) | 331.0 | 349.3 | +5.5 % | ✓ 较弱 |
| 3rd 吸入 (g) | 39.68 | 53.36 | **+34.5 %** | ✓ |
| 2nd 吸入 (g) | 10.97 | 14.96 | **+36.4 %** | ✓ |
| 1st 吸入 (g) | 14.60 | 16.18 | +10.8 % | ✓ |
| 1st 吸入时间 GB (s) | 25.66 | 26.51 | +3.3 % | n.s. |
| **回渗 GB (g)** | 0.492 | **0.990** | **+101 %** | ⚠ 权衡 |
| 侧向吸入时间 (s) | 7.77 | 10.36 | +33.4 % | ⚠ 权衡 |

> **三条读法**：① 机理成立（t=15.9）；② **真正的收益是产能不是速度**——2nd/3rd 吸入 +36%/+35% 在等垫重下达成；③ 两项代价：回渗翻倍、侧向变慢。**回渗是 gate**。

### Risks 三类风险（原文分级）

| 类别 | 风险 |
|---|---|
| 设计/性能 | 回渗成硬约束（+101%）；三叶比例提高后**层间结合强度未知**（首要技术缺口）；贴肤侧三叶提升手感粗糙度（用 homo-PET 更差） |
| 工艺/设备 | **≥142 ℃ 磨圆异形截面** → "加了等于没加"，试验压在 139 ℃ 以下；压力粘合无效、无 LSE；线性超声 ≈US$70k、500 m/min 但占地面；HK 仿制 Herrmann 模块电压/频率不符 → 焊头寿命风险 |
| 供应/转换 | 三叶样品量卡试产；福地单一来源，Home PET 替代未认证；**PET 面层在超声密封道中充当未粘合填充物 → 强度无声下降（HIGH）** |

## Shared 两个项目的共同方法论

1. **都把「材料级代理指标」与「装配级判据」严格区分**，并明说前者只能作方向性参考。
2. **都主动列出未测项**（Void volume、压缩回复、横向均匀性、层间结合强度），把「未知」结构化而非掩盖。
3. **都用临界值说话**（34.93 gsm 成本临界；+15% 扩散目标）而非用平均值说话。
4. **都承认"两个变量同时动"使归因失效**（REL 的 supplier + basis weight；Baymax 的供应商变更），并把它写进下一步实验设计（三臂试验）。

## Links 关联

- 项目主线：[[REL增强层]] · [[Multilayer SAP Core（多层SAP芯体）]]
- 成本与数据源：[[REL_Cost_Model_28gsm_vs_40gsm]] · [[CI-06 COCO V6 3rd round trial - final]]
- 材料与工艺：[[三叶形截面纤维（Trilobal Fibre）]] · [[SAP 吸水纸（SAPP）]] · [[双组分纤维 Bicomponent]] · [[热风非织造 Hot-Air Bonded Nonwoven]]
- 供方：[[延江（Yanjan）]] · [[恒碳（Hengtan）]]

## Source 来源

- 原件：`RAW_FULL/ima_sync/个人知识库/WKB/Projects/Template/attachments/ONE-PAGE OI PROJECT PROFILE - REL&Trilobal Liner.pptx`（2,334,821 B，2 页）
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Projects/Template/ONE-PAGE OI PROJECT PROFILE - REL&Trilobal Liner.pptx.md`（`extract_status: ok`，python-pptx）
- 取件通道：通道 B `get_media_info` → 原件直下（不吃日配额）
- media_id：`ppt_3867e2b60070d7dc3f413086d0b0036e_fdc501344d364fe9f4ac2da3a2e46580001a693ee6c0644e`
- 保密级别：CONFIDENTIAL · IPC BCC OI/FEI（Profile 01 标注 2026-10-26，Profile 02 标注 2026-10-27）
- 锚点说明：`source_path` 为**预期路径**（插件未落盘），次日须复核实落名。

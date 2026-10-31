---
type: source
title: "ND33 改造 · Gate 0–Gate 2 分期能力清单 v2.1（Capability Staging List）"
source_type: 研报
source_path: RAW/ima_sync/个人知识库/WKB/Gate0-Gate2_决策清单_ND33vs北京_20261028.md.md
source_paths:
  - RAW/ima_sync/个人知识库/WKB/Gate0-Gate2_决策清单_ND33vs北京_20261028.md.md
  - RAW/ima_sync/个人知识库/WKB/Gate0-Gate2_决策清单_ND33vs北京_20261028.xlsx.md
original_link: ""
date_published: 2026-10-28
date_processed: 2026-10-28
credibility: 高
credibility_note: "同一文档的 Markdown 版与 Excel 版（v2.1，2026-10-28）双载体：Excel 含 11 个 sheet（00 说明与版本 / 01 Gate0 基本功 / 02 Gate1 硬指标 11 项 / 03–06 Gate2 Phase2–5 / 07 汇总 / 08 决策逻辑 / 09 信息与资源需求 14 项 / 10 跟进事项 13 项），Markdown 版为完整叙述。内容为内部自定门槛，非第三方数据；两项来源可逐条对上（F-01~F-08 直接引自 Bryan《Key point》）。"
knowledge_update_status: done
key_claims:
  - "**v1.0 的结构性错误已更正：把 Phase 2 的三项差异化当门槛，等于用后期目标否掉入场资格** —— 正确结构是「Gate 0 = Phase 1 入场券（F-01~F-08 全满足）／Gate 1 = 物理验证 11 项／Gate 2 = Phase 2–5 各自能做到什么程度」。**ND33 成立与否只看 Phase 1**，Phase 2–5 只决定分几期、投多少、哪些必须放北京"
  - "**F-01 运行速度：设计 1200 PPM、最低运行 1000 PPM**（20% 余量已内化进设计值，不再二次加余量）；**1B-1 主机机械最高速 ≥1200 PPM 是「最硬否决点」**——纯测量、第一周必出"
  - "**11 项 Gate 1 指标里有 4 项属硬否决**（空间 / 层高 / 90° 走线与 pulp 上料 / 主机最高速），3 项可通过加固或增容补救（承重 / 真空 / 电容除尘），1 项可推翻整套工艺（SAP 粉尘防爆与环评）"
  - "**评估截止日为 2026-11-15**：Bryan 原文「mid-Nov.」年份误写为 2027，按 2026 执行；而文中 2027 Q1/Q2 属补证计划未来时点，**不改**——只有评估截止日这一处更正"
  - "**明确写入：ND33 不承担 Phase 5**（fluff + 双面 pattern 的全球可扩展形态）"
  - "**Phase 2 需要 6 个能力单元**：两套独立可调量 SAP 给料 / 分区开孔筛网（可换可设计）/ 分区真空（多区独立可调）/ 多区配方管理 / 上下层独立 pattern 与配准 / **在线克重-密度检测**（闭环前提，否则「调不出来也复现不了」）"
pages_linked: ["[[Pilot Retrofit vs Greenfield Decision Framework（改造 vs 新建 pilot 线决策框架）]]", "[[COCO芯体平台]]", "[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]", "[[High Speed Converting Meeting 南京 2026-10-27（COCO V6 成型工艺与设备方向）]]"]
compile_mode: semantic
---

# ND33 改造 · Gate 0–Gate 2 分期能力清单（v2.1）

## Positioning 一句话定位

The single document that separates **eligibility** (can COCO V6 Phase 1 physically run on ND33) from **extent** (how much of Phase 2–5 ND33 can ever cover) — the distinction that v1.0 got wrong and that decides whether a vendor narrative can veto the project.

这份文件把**入场资格**（COCO V6 Phase 1 能否在 ND33 物理实现）与**覆盖程度**（Phase 2–5 能覆盖到哪一期）彻底分开——v1.0 正是把两者混淆，才让「后期目标」有机会否掉「入场资格」。

## Three-Gate Architecture 三闸结构

| 层级 | 回答什么 | 内容 | 判据 |
|---|---|---|---|
| **Gate 0** | Phase 1 能不能满足 | **入场券**：F-01~F-08 八条 | 任一做不到 → ND33 否决，转北京 |
| **Gate 1** | 物理上装不装得下、跑不跑得动 | 11 项硬指标 | 任一「否」→ 否决；任一「数据未取得」→ 不得判过，走降级 |
| **Gate 2** | Phase 2–5 各自能做到什么程度 | 逐期列能力单元 / 判定 / 何时能做 / 需什么输入 | 只影响分几期与投多少 |

> **决策逻辑（更正版）**：*ND33 成立与否，只看 Phase 1 能否满足一件事。*Phase 2–5 决定改造分几期、每期投多少、哪些必须放北京——不是能否成立。

## Gate 0 · F-01 ~ F-08（Phase 1 入场券）

| 编号 | 要求 | 量化 / 定义 |
|---|---|---|
| F-01 | 运行速度 | 设计 **1200 PPM**，最低 **1000 PPM** |
| F-02 | 5 层产品结构 | LSN + SAP1 + REL + SAP2 + PSN |
| F-03 | 2 个成型鼓 | 双鼓工艺 |
| F-04 | 每层 SAM 都有 pattern | 视觉提示 + channel 处更高 void volume |
| F-05 | LSS / PSS pattern 对齐 + 压花 | 双面配准精度（待量化） |
| F-06 | 100% SAM + shaped | 一期不含 fluff |
| F-07 | 尺寸覆盖 | **11 个尺寸 / 3 种宽度（100/110/120 mm）** |
| F-08 | 下游完整可制造性 | 复合、压花、切割、收卷（高蓬松不塌） |

**冻结检查表（10/28 三方签字）**：F-01~F-08 冻结 ｜ 基线 = 移除全部 Blizzard（**仅评估用，不构成拆除授权**）｜ 排除项 2 条（共存不可能 / 旁路 core collector 不可能）｜ 三案定义 ｜ Gate 1 十一项门槛写法 ｜ Phase 2–5 输入认领人 ｜ 会谈记录人 Bryan + 五项抓取清单 ｜ **ND33 不承担 Phase 5**

## Gate 1 · 11 项硬指标（只验证 F-01~F-08 能否实现）

| 编号 | 指标 | 门槛怎么定 | 不过后果 |
|---|---|---|---|
| 1A-1 | 可用空间（双鼓+真空+除尘+上料+通道） | 双鼓净需求 × 1.2 | **否决** |
| 1A-2 | 层高净空（鼓吊装+管路） | 吊装净高 + 20% | **否决** |
| 1A-3 | 地坪承重与振动 | 载荷 × 1.2 | 加固可行则过 |
| 1A-4 | 90° 走线与 pulp 上料通道 | 净宽 + 转弯半径 | **否决** |
| 1B-1 | 主机机械最高速 | **≥1200 PPM** | **最硬否决** |
| 1B-2 | 鼓驱动与传动（150 RPM runout/热变形） | Schaefers 给判据 | 降速 → F-01 不成立 |
| 1B-3 | 下游兼容（11 尺寸 / 3 宽度 / 压花 / 切割） | 全尺寸可通 | 受限改造 |
| 1B-4 | 收卷张力与高蓬松输送 | 支持低张力 / 表面卷绕 | F-08 不成立 |
| 1C-1 | 真空余量（风量 + 静压） | 两套鼓需求 × 1.2 | 加泵可行则过 |
| 1C-2 | 电容量与除尘风量余量 | 新增需求 × 1.2 | 增容可行则过 |
| 1C-3 | SAP 粉尘防爆 / 环评 / 消防 | 无需重报批或周期可接受 | **整套工艺推翻** |

## Gate 2 · 分期能力（Phase 2–5）

| Phase | 内容 | ND33 定位 |
|---|---|---|
| 2 | 2-a add-on 差异化 ｜ 2-b SAM 密度差异化 ｜ 2-c 覆盖率差异化 | 需 **6 个能力单元**（见下） |
| 3 | PSS 加入少量 fluff 提升毛细吸收 | 有条件（需 fiberizer / pulp 上料位） |
| 4 | REL pattern cut（trimming handle） | 后续期 |
| 5 | fluff + 双面 pattern，可全球扩展 | **ND33 不承担** |

**Phase 2 六能力单元**：① 两套独立可调量 SAP 给料；② 分区开孔筛网（可换 / 可设计）；③ 分区真空（多区、独立可调）；④ 多区控制与配方管理；⑤ 上下层独立 pattern 与配准；⑥ **在线克重/密度检测**（闭环前提——「否则调不出来也复现不了」）。

## Dual Carrier 双载体说明

| 载体 | 内容 | 用途 |
|---|---|---|
| `.md`（本页主源） | 完整叙述、逐项驳回 v1.0 逻辑错误 | 阅读与评审 |
| `.xlsx` v2.1 | 11 个 sheet，含汇总表 / 决策逻辑 / 14 项信息需求 / 13 项跟进事项 | 填数与会签 |

## Linked Pages 关联页面

- 框架：[[Pilot Retrofit vs Greenfield Decision Framework（改造 vs 新建 pilot 线决策框架）]]
- 概念：[[COCO芯体平台]]、[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]
- 同批：[[High Speed Converting Meeting 南京 2026-10-27（COCO V6 成型工艺与设备方向）]]、[[ND33 改造可行性评估·推进计划（20261028）]]、[[Gate 0 基线口径确认书（ND33-COCOV6-G0-001）]]

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Gate0-Gate2_决策清单_ND33vs北京_20261028.md.md`（+ 同名 `.xlsx.md`）
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/attachments/`

---
type: source
title: "Key point for COCO V6 engineering plan（Bryan 五阶段路线与 ND33 评估基线）"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Key point for COCO V6 engineer.md.md
original_link: ""
date_published: 2026-10-27
date_processed: 2026-10-28
credibility: 高
credibility_note: "Bryan（战略判定线）会前发给团队的英文要点函，是 2026-10-27 南京会议与后续全部 ND33 文件的**上游依据**（F-01~F-08、Phase 1–5、三条基线均源自本文）。原文含一处年份笔误「mid-Nov. 2027」，按会议与后续文件口径应为 2026。"
knowledge_update_status: done
key_claims:
  - "**COCO V6 的定义在这封函里被定量锁定**：1200 PPM 设计 / 1000 PPM 最低运行；5 层结构 LSN + SAP1 + REL + SAP2 + PSN；2 个成型鼓；每层 SAM 都需 pattern（视觉提示 + channel 处更高 void volume）；LSS 与 PSS pattern 需对齐并压花"
  - "**Phase 1 只用 100% SAM + 成形（shaped）** —— 这是「入场券」的原始出处；Phase 2 才引入三项差异化（add-on / 密度 / 覆盖率），Phase 3 加 fluff，Phase 4 做 REL pattern cut，Phase 5 转 fluff+SAM 双面 pattern 的全球可扩展形态"
  - "**优先级被明确规定**：当前工作集中在 Phase 1 与 Phase 2，但设计须为后续 Phase 预留空间；「若 capex 影响不大，Phase 3 可提前并入」"
  - "**三条基线原文出自此处**：① 从主机角度看，保留现有 Blizzard（2 套 SAM hopper）与 COCO V6 双鼓共存**不可能**，故以「移除全部 Blizzard」作空间评估基线；② 旁路 core collector（ND33 制芯后离线供其他 KC 机台）受空间限制**不可能**；③ Rocky（戴奇）团队主责 + Schaefers 团队技术咨询，共同出 ND33 改造方案（空间 / 技术方案 / 时间 / capex）"
  - "**评估截止原文为「before mid-Nov.」，年份笔误写作 2027** —— 实际按 2026-11 执行（后续文件已统一更正并在 Gate 0 检查表注明）"
pages_linked: ["[[COCO芯体平台]]", "[[High Speed Converting Meeting 南京 2026-10-27（COCO V6 成型工艺与设备方向）]]", "[[Pilot Retrofit vs Greenfield Decision Framework（改造 vs 新建 pilot 线决策框架）]]", "[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]"]
compile_mode: semantic
---

# Key point for COCO V6 engineering plan

## Positioning 一句话定位

The upstream one-page brief that turned COCO V6 from a concept into a **staged, gate-able engineering plan**: five phases, two drums, five layers, and three baselines that later became the frozen assumptions of every ND33 document.

这封上游要点函把 COCO V6 从概念变成**可分阶段、可设闸门的工程计划**：五期路线、两个鼓、五层结构，以及后来被全部 ND33 文件冻结为「基线」的三条判断。

## COCO V6 Process Definition 工艺定义

| 项 | 规格 |
|---|---|
| 速度 | **设计 1200 PPM，最低运行 1000 PPM** |
| 产品结构 | **5 层**：LSN + SAP1 + REL + SAP2 + PSN |
| 成型 | **2 个成型鼓（2 forming drum process）** |
| Pattern | 每层 SAM 均需 pattern —— 视觉提示 + channel 处更高 void volume |
| 配准 | LSS pattern 与 PSS pattern 需**对齐并压花** |

## Five-Phase Roadmap 五期路线

| Phase | 内容 | 备注 |
|---|---|---|
| **1** | 100% SAM + shaped（成形） | 当前优先级 |
| **2** | LSS/PSS 的 **add-on 差异化** + SAM **密度差异化**（LSS 或 PSS 或双侧）+ LSS/PSS **覆盖差异化** | 当前优先级 |
| 3 | PSS 加入**少量 fluff** 提升毛细吸收 | **capex 影响不大可提前并入** |
| 4 | REL **pattern cut**（带 trimming handle） | |
| 5 | PSS = **fluff + SAM**，双面 pattern，可全球扩展 | |

> **优先级规定**：当前工作集中于 Phase 1 与 Phase 2，但设计须为后续 Phase 预留空间（Phase 3 可在 capex 允许时提前）。

## ND33 Assessment 三条基线（原文出处）

| # | 基线 | 原文要点 |
|---|---|---|
| B-1 | 双鼓 COCO V6 与现有 Blizzard（2 套 SAM hopper）共存 | 从主机角度**不可能** → 以「移除全部 Blizzard」作空间评估基线 |
| B-2 | 旁路 core collector 离线供其他 KC 机台 | 受空间限制**不可能** |
| B-3 | 责任分工 | **Rocky（戴奇）团队主责** + Schaefers 团队（High Speed Converting）技术咨询 → 出空间可用性、技术方案、时间与 capex 估算 |

> **原文年份笔误**：评估截止写作「before mid-Nov. **2027**」，按会议与后续文件口径应为 **2026-11**；后续文件已统一更正并注明，建议与 Bryan 同步修订原稿。

## Linked Pages 关联页面

- 概念：[[COCO芯体平台]]、[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]
- 下游文件：[[High Speed Converting Meeting 南京 2026-10-27（COCO V6 成型工艺与设备方向）]]、[[ND33 改造 · Gate 0–Gate 2 分期能力清单 v2.1（Capability Staging List）]]
- 框架：[[Pilot Retrofit vs Greenfield Decision Framework（改造 vs 新建 pilot 线决策框架）]]

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Key point for COCO V6 engineer.md.md`

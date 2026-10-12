---
type: comparison
title: "芯包材料对比（LSN MPM vs PSN MPM）"
subjects: ["[[Unikorn]]", "[[芯体测试方法与验收基准（STM）]]"]
dimension: 综合
updated: 2026-09-29
tags: [Core Wrap, 芯包, MPM, LSN, PSN, 水刺, 三叶形, 成本, 供应链风险, COCO V6]
---

# 芯包材料对比（LSN MPM vs PSN MPM）

> 对比对象：COCO V6 芯体的**上片（LSN）与下片（PSN）包裹材料**。回答"为什么上下片规格不同、MPM 是否够格、有没有替代项"。
> 数据口径 2026-09-11 准备会 + 2026-09 CI-06 试产实测。

## 对比维度表

> 必含「成本」与「供应链风险」两列。

| 维度 | LSN MPM（上片） | PSN MPM（下片） | 依据 |
|---|---|---|---|
| **结构：克重** | 20 gsm（PP+fluff） | 20 gsm（PP+fluff） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| **结构：宽 × 长** | 200 mm × 2 km（英文版写 4 km）⚠️ | 150 mm（主表）/ 155 mm（135 Pad） | [[Coco V6 试产原料清单（Raw material list v3.0）]]、[[COCO V6 试产原料准备会（英文版，2026-09-11）]] |
| **结构：卷芯 / 卷径** | 6.75″ core，卷径 ≤800 mm | 6.75″ core，卷径 ≤800 mm | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| **供应商** | Unikorn | Unikorn | [[COCO V6 试产原料准备会（英文版，2026-09-11）]] |
| **到货状态** | **已到天津**（本批唯二提前到货项之一） | **已到天津** | [[CI-06 COCO V6 第三轮试产测试结果]] |
| **实测：含水率** | 0.02414（Unikorn 200 mm，复测） | 0.02666（Unikorn 150 mm，复测） | [[CI-06 COCO V6 第三轮试产测试结果]] |
| **实测：爬坡高度** | **51.1 mm** | **37.65 mm** | [[CI-06 COCO V6 第三轮试产测试结果]] |
| **实测：基重 / STT / 返渗** | `[待验证]`（Unikorn MPM 本轮未测，因"之前已测试"） | `[待验证]`（同上） | [[CI-06 COCO V6 第三轮试产测试结果]] |
| **验收基准（设计口径）** | 规格 **15–18 gsm SMS 或 tissue**；SAP 隔离 ≥90~98%；芯体级回渗 ≤3.0 g、摄入 ≤35 s；MD 分布 ≥130 mm；端封按 STM-00078 | 同左 | [[COCO V6 试产原料准备会（v2 Final）]]、[[芯体测试方法与验收基准（STM）]] |
| **成本** | `[待验证]`——本批**无任何芯包报价数据** | `[待验证]` | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| **供应链风险（规格适配）** | **中-高：试产 20 gsm MPM vs 规格 15–18 gsm，原文明确要求"确认适用性"** | 中-高：同左 | [[COCO V6 试产原料准备会（v2 Final）]] |
| **供应链风险（交付）** | **低**：已到货 | **低**：已到货 | [[CI-06 COCO V6 第三轮试产测试结果]] |
| **供应链风险（技术验证）** | **中：本轮只复测含水率与爬坡，基重/STT/返渗缺测** | 中：同左 | [[CI-06 COCO V6 第三轮试产测试结果]] |
| **适用场景** | 上片（皮肤侧下方）——需兼顾亲水与抗迁移 | 下片（背面）——偏结构与包覆 | [[COCO V6 试产原料准备会（v2 Final）]] |

**本批新增的替代 / 辅助项（Summary 版）**

| 项 | 定位 | 规格 / 数量 | 供应商 | 状态 | 依据 |
|---|---|---|---|---|---|
| LSN 水刺（含三叶形莱赛尔） | LSN 的水刺替代方案 | 6 km｜卷径 ≤700 mm，3″ core | Wangjin | 9/20 到天津 | [[COCO V6 试产原料准备会（Summary 版）]] |
| 亲水整理 3059 | 亲水、改善凝胶阻塞 | 40 kg | Hankel（与中文清单所记 **Henkel / [[汉高]]** 疑为同一方）⚠️ | 已到天津 | [[COCO V6 试产原料准备会（Summary 版）]]、[[Coco V6 试产原料清单（Raw material list v3.0）]] |

> **LSN 水刺（Wangjin）实测（CI-06，LSN-1 组）**：基重 **38.756 gsm**、厚度 0.37 mm、液体穿透 **1.594 s**、返渗 **0.896 g**、爬坡高度 **170.6 mm**——**爬坡远高于 MPM 组（51.1 mm）**，但返渗也显著更高（0.896 g vs MPM 组未测）。详见 [[CI-06 COCO V6 第三轮试产测试结果]]。

> 尾注：本表数字来自 [[Coco V6 试产原料清单（Raw material list v3.0）]]、[[COCO V6 试产原料准备会（英文版，2026-09-11）]]、[[COCO V6 试产原料准备会（v2 Final）]]、[[COCO V6 试产原料准备会（Summary 版）]]、[[CI-06 COCO V6 第三轮试产测试结果]] 五份源摘要页。**成本维度无来源，全部标 `[待验证]`。**
> **爬坡高度口径**：为"芯体吸收高度（爬坡 / 反重力测试）"，爬坡时长 5 min；不同材料组的测试批次不同（MPM 组为复测），**跨组比较须谨慎**。

> ⚠️ **名称与口径待核（2026-09-29，待人工确认）**：① LSN/PSN MPM 的长度口径在英文版（4 km）与 Summary（2 km）间不一致；② `Hankel` 与中文清单的 `Henkel` 是否同一方未确证。
> 🔴 **manual_review（2026-09-29）**：本表含**试产供应关系与物料规格**（AGENTS.md §5 边界）。页面按内部追溯保留；对外引用前须人工确认。

## 各自适用场景

- **LSN MPM（200 mm，Unikorn）**：上片，宽度最大——本批**唯二提前到货**的物料，供应稳定性最好；但**本轮的基重/STT/返渗未测**，只有含水率与爬坡。
- **PSN MPM（150 mm，Unikorn）**：下片，宽度较小（135 Pad 组用 155 mm）——同样已到货，爬坡（37.65 mm）低于 LSN。
- **LSN 水刺（Wangjin，含三叶形莱赛尔）**：上片的**水刺替代**——爬坡能力显著更强（170.6 mm），但返渗也更高（0.896 g），属"导流强、回渗弱的取舍项"，且 9/20 到货（晚于 MPM）。

## 结论

上下两片 MPM 均为 **Unikorn、20 gsm**，差异只在宽度与位置；两者是本批**供应链最稳**的物料（唯二提前到货）。真正的隐忧有两个：**① 试产 20 gsm 高于验收规格 15–18 gsm，原文要求确认适用性；② 本轮只复测含水率与爬坡，基重/STT/返渗缺测**——所以"MPM 够不够格"这个问题，**目前既没有结论、也没有完整数据**。水刺 LSN 是一个方向明确（导流强）但代价明确（返渗高）的替代项。

## 来源

- [[Coco V6 试产原料清单（Raw material list v3.0）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Raw material list for Coco V6 trial.xlsx.md`
- [[COCO V6 试产原料准备会（英文版，2026-09-11）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_EN.pptx.md`
- [[COCO V6 试产原料准备会（v2 Final）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_v2_Final.pptx.md`
- [[COCO V6 试产原料准备会（Summary 版）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_Summary.pptx.md`
- [[CI-06 COCO V6 第三轮试产测试结果]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/CI-06 COCO V6 3rd round trial.xlsx.md`
- [[Unikorn]] —— 供应商实体页

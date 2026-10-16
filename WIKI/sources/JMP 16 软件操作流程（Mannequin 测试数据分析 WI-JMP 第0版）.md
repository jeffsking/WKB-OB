---
type: source
title: "JMP 16 软件操作流程（Mannequin 测试数据分析 WI-JMP 第0版）"
source_type: 内部作业指导书
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/JMP软件操作流程.docx.md
credibility: 中
knowledge_area: Areas/Test Method/成品/TJ
subjects:
  - [[JMP 统计分析软件]]
  - [[Mannequin 测试]]
  - [[测试数据分析]]
pages_linked:
  - [[Elastic Tension Visualization Technology Assessment（拉力松紧可视化技术评估）]]
date_published: 2024-02-26
knowledge_update_status: done
key_claims: []
date_processed: 2026-10-11
compile_batch: P0-B02/B03/B04
---

## 概要

实验室内部作业指导书 **WI-JMP《JMP 软件操做流程》**（原文标题"操做"为文档原有错别字，本页标题沿用规范写法并保留原义）。

- 文件编号：WI-JMP
- 版本：**第 0 版**
- 修订日期：**2024 年 2 月 26 日**
- 实验目的：**分析 Mannequin（人体模型）的测试数据**

## 操作步骤

1. 打开 **JMP 16**
2. 把 Mannequin 导出的 **Excel 数据**拖放到 JMP 主窗口左侧
3. 在 JMP 主窗口**双击**打开刚刚拖放的 Excel 文件

## 数据结构（源文件记录的分析字段）

Mannequin 导出的 Excel 表含约 17 个字段，构成 JMP 分析的数据列：

| 字段 | 含义 |
|---|---|
| Study Number | 研究编号 |
| Code | 样品编码 |
| Gender | 性别 |
| Position | 位置 |
| Run | 轮次 |
| Mannequin | 模型标识 |
| Leaked | 是否泄漏 |
| Order | 顺序 |
| Time | 时间 |
| Leak Area | 泄漏面积 |

## 关联

- 成品测试主线：[[Elastic Tension Visualization Technology Assessment（拉力松紧可视化技术评估）]]（同属成品/TJ 目录）
- JMP 是本库统计口径的主要工具，凡涉及成对比较、多因子与图形化诊断的测试数据应优先走 JMP 而非手工透视表。

## 页面状态

- 本文档为**第 0 版**，仅含3 个主步骤，**未覆盖**数据清理、假设检验、图表模板化、报告导出等后续环节。
- 源文件含截图（`[图片: JMP 16]`、`[图片: JMP主窗口-...xshujv.xlsx]`），**图像内容未做视觉识读**，实际界面细节以本地软件为准。
- 建议在下一版补齐：列类型指定（测量/标识）、缺失值处理、分组比较的报表模板。

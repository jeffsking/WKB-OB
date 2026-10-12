---
type: source
title: "FIUP collagen Testing Victoria Maria.pptx"
source_type: pptx
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Test Methods/FIUP - TTM-00643/FIUP collagen Testing Victoria Maria.pptx.md
original_link: ""
date_published: ""
date_processed: 2026-09-29
credibility: internal-test
knowledge_update_status: done
key_claims:
  - "collagen 介质 vs blotter 对比：blotter 因 AD 产品 doming 与纸的刚度无法全接触，人为压低其回渗读数；collagen 可全接触"
  - "collagen 饱和容量约 0.269 g（1\"×2\" 0.5PSI 权重），层数不足会先饱和导致读数失真；从 2 片迭代至 10 片"
  - "10 sheets collagen 1\"×2\" 0.5PSI：Poise 6DL 0.199 / AD 6D Old 0.185 / Always 6DL New 0.147 g（A A B 分组）——与 blotter 2.44\" 大权重口径（AD Old 0.898 显著最差）结论不同"
  - "AD NEW 与 AD OLD 相对 Poise 的显著性随介质/口径翻转（= / -），复证测试路径可翻转结论"
pages_linked:
  - "[[FIUP Test Method TTM-00643（女性摄入与回渗测试法）]]"
  - "[[Rewet Measurement Variability（回渗测试变异性）]]"
---

# FIUP collagen Testing Victoria Maria.pptx

## Basic Information 基本信息
- **Presenter**: Victoria Maria
- **位置**: Test Methods / FIUP - TTM-00643（方法开发数据）
- **性质**: Privileged and Confidential 方法验证材料
- **Domain**: Performance / Rewet / 测试方法——collagen 介质替代 blotter 的探索

## Method Question 方法问题（方法问题）
blotter 纸测回渗时，AD（Always Discreet）产品因 **doming（穹起）** 与吸墨纸刚度，重量与表面**不能全接触**，读数被人为压低；collagen（胶原蛋白膜）柔软可贴合，是否更真实？

## Iterations 迭代过程（迭代过程）

| 轮次 | 设置 | 发现 |
| --- | --- | --- |
| 1 | Blotter / 2.44" 权重 | AD 与 Poise 均接触不全 |
| 2 | 2 片 collagen + 常规权重 | AD 疑似仍达 collagen 饱和限 |
| 3 | 4 片 collagen + 1"×2" 权重（减面积促全接触） | 疑似仍未全饱和；blotter 口径下 AD 因 doming 读数波动大；collagen 口径下两垫可能 parity |
| 4 | 6 片 collagen | **collagen 容量 = 0.269 g**（差 0.069 g 裕量） |
| 5 | **10 片 collagen**（1"×2" 0.5PSI 与 0.7PSI）+ blotter 对照 | 见下表 |

## Key Results 关键数据（关键数据）

| 口径 | Poise 6DL | AD 6D Old | Always 6DL New | 分组 |
| --- | --- | --- | --- | --- |
| Blotter, 2.44" 权重 | 0.2700 | **0.8980** | 0.4476 | A / A / B（AD Old 显著最差） |
| **10 sheets collagen, 1"×2" 0.5PSI** | 0.1990 | 0.1850 | **0.1470** | A / A / B |
| 10 sheets collagen, 0.7PSI | 0.2010 | — | 0.18075 | — |

- **结论翻转示例**: blotter 大权重口径下 AD Old 显著差于 Poise（0.898 vs 0.270）；collagen 口径下 AD Old 与 Poise 同组（0.185 vs 0.199），且 AD New（0.147）显著最优。
- **AD New vs AD Old × Poise** 的显著性矩阵（=/-）随介质与权重口径在三个组合间翻转。

## LabVantage Cross-Check LabVantage 交叉验证
- AD NEW LabVantage 数据：两请求（25-0431 首次、25-1242 四批次）+ ADT 1614 实验室请求三方对比——同一产品跨请求数据散布明显（衔接回渗变异性问题）。

## Findings 结论
1. blotter 测 AD 回渗因 **doming + 接触不全** variability 极高且系统性偏低。
2. collagen 介质需**足量层片**防饱和（容量 0.269 g 量级 @ 1"×2" 0.5PSI）。
3. collagen 口径下产品排序与 blotter 不同——介质选择即结论选择。

## 关联
- 与 [[Consumer Relevancy of FIUP Method Feb 2025.docx]] 同属 FIUP TTM-00643 方法体系；介质与口径问题衔接 [[Rewet Measurement Variability（回渗测试变异性）]] 的"测试路径可翻转结论"。

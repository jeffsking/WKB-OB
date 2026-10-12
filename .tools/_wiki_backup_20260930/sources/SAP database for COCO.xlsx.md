---
type: source
title: "SAP database for COCO.xlsx"
source_type: xlsx
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP database for COCO.xlsx.md
original_link: ""
date_published: ""
date_processed: 2026-09-29
credibility: internal-test
knowledge_update_status: done
key_claims:
  - "COCO 项目 SAP 数据库（11 牌号 × 8 参数）：CRC 双口径、AUL(0.7psi)、吸速、GBP、30-50 目占比、角色定位（SAP1 顶层 / SAP3 参考·候选 / 平衡级 / 中GBP / 高AUL替代）"
  - "KC 511 为 SAP1 顶层（CRC 59.4/30.9 双口径、AUL 18.4、29s、GBP 24★、76.9% 粒径达标）；N8 (611) GBP 45 异常高但 AUL 12/吸速 3s 数据可疑未标角色；SDP-930（住友）GBP 20、AUL 19"
  - "SAP3 候选四位：NR-959（34s 最快候选）、NR-951（27s）、NR-610S（19s★ 最快）、住友 60S（GBP 2★ 最低）；NR-950 为参考位"
  - "巴斯夫 7059 定位高 AUL 替代（AUL 17.7 接近 511、CRC 35.5 更高但吸速 56s 最慢）"
pages_linked:
  - "[[SAP 四牌号性能对比（KC511 vs NR-610S vs NR-950 vs Code X）]]"
  - "[[诺尔（Nuoer）]]"
  - "[[SAP（高吸水树脂）]]"
  - "[[COCO芯体平台]]"
---

# SAP database for COCO.xlsx

## Basic Information 基本信息
- **位置**: Material / SAM 目录
- **性质**: COCO 项目 SAP 选型数据库（11 牌号参数总表）
- **Domain**: Material / SAM / COCO V6 SAP Selection（OI-13 相关）

## Database 数据库（SAP 数据库总表）

| 型号 | CRC | CRC(2) | AUL(0.7psi) | 速度(s)↓ | GBP | 30-50目(%) | 角色定位 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KC 511 | 59.4 | 30.9 | 18.4 | 29 | **24 ★** | 76.9 | **SAP1 顶层** |
| NR-950 | 62.5 | 36.7 | 19.4 | 51 | 8 | 88.6 | SAP3 参考 |
| NR-959 | 62.4 | 35.3 | 16.1 | 34 | 6 | 73 | SAP3 候选 |
| NR-951 | 61.5 | 35.6 | 12.3 | 27 | 4.3 | 48.9 | SAP3 候选 |
| NR-610S | 60.8 | 30.8 | 12.1 | **19 ★** | 6 | 65.1 | SAP3 候选 |
| 住友60S | 63.2 | 35.4 | 14.2 | 36 | **2 ★** | 75.3 | SAP3 候选 |
| NR-511N | 61.7 | 33.8 | 13.6 | 31 | 8.5 | 81.2 | 平衡级 |
| NR-760H | 58 | 30.6 | 16 | 27 | 12 | 80.4 | 中GBP |
| 巴斯夫7059 | 54.9 | 35.5 | 17.7 | 56 | 4 | 59.9 | 高AUL替代 |
| NR-N8 (611) | 54.9 | 40 | 12 | 3 | 45 | — | — |
| SDP-930 | 54.9 | 31.5 | 19 | 35 | 20 | — | — |

（★ = 该列极值；CRC 双口径含义源表未标注 `[待验证]`）

## Read-out 读表要点（读表要点）
- **SAP1 顶层独尊 KC 511**：GBP 24 为表内常规最高，AUL 18.4 仅次于 NR-950（19.4）与 SDP-930（19）。
- **SAP3（下层）四候选各有优势**：吸速最快 NR-610S（19 s）、CRC 最高住友 60S（63.2/35.4）、GBP 最低住友 60S（2）、均衡 NR-959。
- **N8 (611) 数据异常**：GBP 45 全表最高但吸速 3 s 全表最快——与 [[SAM_511_分析汇报.pptx]] 中"N8 全混淆/封顶失效"结论一致，此表未给其角色定位。
- **巴斯夫 7059** = 高 AUL 替代位（对标 P&G 双层方案，见 [[诺尔（Nuoer）]] 959 对标记录）。

## 关联
- 与 [[SAP 四牌号性能对比（KC511 vs NR-610S vs NR-950 vs Code X）]] 的四牌号口径互补（本表扩至 11 牌号并加角色定位与粒径列）；角色分工衔接 [[COCO芯体平台]]。

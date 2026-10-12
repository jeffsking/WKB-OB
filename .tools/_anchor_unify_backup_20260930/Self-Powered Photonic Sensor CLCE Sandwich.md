---
type: source
title: "Self-Powered Photonic Sensor CLCE Sandwich"
source_type: book
source_path: RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mechanochromic_Photonic_Sensors_拆解/LCE自供电光子传感器_拆解.md.md
original_link: ""
date_published: 2025
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
author: "Cheng Xue, Haonan Sun, Yuting Tang, Jie Wei, Jinbao Guo (Beijing University of Chemical Technology)"
edition: ""
publisher: "ACS Applied Materials & Interfaces"
year: 2025
isbn: ""
original_language: "EN"
parent_book: "[[Mechanochromic Photonic Sensors]]"
key_claims:
  - "PDMS-CLCE-PDMS sandwich couples mechanochromism and triboelectric response in a single self-powered, dye-free device."
  - "Stretching shrinks the cholesteric pitch from P0 = 438 nm to P1 = 285 nm, i.e. red -> blue structural colour shift."
  - "Colour is formulation-tunable: chiral agent LC756 at 5.8% / 6.4% / 7% yields red / green / blue films."
  - "Self-healing at 80 C plus stretchable AgNW-PDMS electrodes address durability and skin-contact wear."
pages_linked: ["[[Mechanochromic Photonic Sensors]]", "[[机械变色 Mechanochromic]]", "[[胆甾相液晶弹性体 CLCE]]", "[[摩擦电自供电 TENG]]", "[[结构色 Structural Color]]", "[[银纳米线 AgNW]]"]
---

# Self-Powered Photonic Sensor Using Cholesteric Liquid Crystal Elastomer Sandwiched Architecture

## One-line Position 一句话定位
The most complete architecture in this vault for a dye-free, battery-free, self-healing mechanical sensor: cholesteric liquid crystal elastomer structural colour (red -> blue on stretch) read out optically, with triboelectric output read out electrically.

> Source caveat: the compiled source is the paper's **Supporting Information (S1-S9, 131 lines)**, not the main text. Quantitative VOC/ISC/QSC values and cycle counts are absent and marked as such below.

## Key Numbers & Conclusions 提炼数字与结论

| 项目 Item | 数值/结论 Value | 备注 Note |
|---|---|---|
| 器件架构 | PDMS-CLCE-PDMS 三明治 | 软-光子-软 |
| 双机制 | 机械变色 + 摩擦电响应 | 单一器件，无需外部电源 |
| 初始螺距 P0 | 438 nm（红态） | SEM 截面测量 |
| 拉伸后螺距 P1 | 285 nm（蓝态） | 红→蓝，蓝移 |
| 手性剂 LC756 含量 | 5.8% / 6.4% / 7% → 红 / 绿 / 蓝 | 颜色配方化可设计 |
| 配方组分 | LC756 + RM82（单体）+ EDDET（扩链）+ PETMP（交联）+ Irgacure 651（UV 引发） | 光固化可打印/可浇铸 |
| 自修复温度 | CLCEs-S 膜 80 °C 愈合 | FT-IR 确认 CLCE 与 CLCEs-S 结构差异 |
| 电极 | AgNWs 部分包埋于柔软黏性 PDMS | SEM 观察 |
| 电学输出 | VOC / ISC / QSC 三通道 | 具体数值 **[未找到原句/行号缺失]**（正文数据） |
| 耐久循环数 | — | **[未找到原句/行号缺失]** |

## Evidence 证据

- **核心主张** — "A Self-Powered Photonic Sensor Using Cholesteric Liquid Crystal Elastomer-Based Sandwiched Architecture with Mechanochromism and Triboelectric Response" (lines 5-7)
- **螺距直接观测（机制核心）** — "The pitch changes of CLCE in the initial red state and the stretched blue state were tested by SEM. It was found that the pitch decreased from P0 = 438 nm to P1 = 285 nm." (lines 77-78)
- **颜色配方化可调** — "Reflectance spectra of red, green and blue CLCE films prepared with different chiral agent contents (5.8%, 6.4%, 7%)." (lines 38-40)
- **三明治制备路线** — "Schematic flow diagram of the preparation of a self-powered sensor based on PDMS-CLCE-PDMS structure." (lines 51-52)
- **自修复可靠性** — "Microscopic photographs of CLCES-S films healed at 80 °C." (line 68)
- **柔性电极工艺** — "The PDMS doped with AgNWs was observed under the SEM, and it was found that the AgNWs were partially encapsulated within the soft material PDMS, which had a certain degree of stickiness." (lines 106-108)
- **电学输出定义** — "The open-circuit voltage (VOC), short-circuit current (ISC) and charge density (QSC) of the PDMS-CLCE-PDMS sensor." (lines 124-125)

## Business Connection Points 业务连接点

- **免电池尿湿/压力可视化指示器（推演，最强应用路径）** — CLCE 的"红→蓝"结构色（438→285 nm）与三色可调配方，可作免染料、免电源的视觉指示。可推演路径：将 CLCE 层与 SAP 溶胀/芯体膨胀耦合，吸水膨胀产生的应变触发变色，实现"尿湿即变色"的肉眼指示以替代现有 pH 染料指示条；颜色由手性剂含量定制，便于按品牌色设计。**论文未做 SAP/湿敏实验。**
- **自供电降低智能穿戴供电成本（推演）** — 摩擦电输出 VOC/ISC/QSC，无需电池，可避开电池与皮肤接触的安全与回收问题。摩擦电信号适合作为"应变/接触"事件计数通道用于低频人体活动监测；具体灵敏度与循环寿命需查正文。
- **自修复 + 可拉伸 = 延长贴身产品寿命** — 自修复 PDMS 与 80 °C 愈合的 CLCEs-S 意味着柔性传感器在反复弯折/拉伸后可恢复功能；对腰围、腿围等高频形变区域可提升耐用性、降低"传感失效"客诉风险。
- **AgNW-PDMS 柔性电路参考（推演）** — "纳米线导电网络 + 弹性封装"是耐形变电极的可行工艺；采购端可关注银纳米线浆料与 PDMS 弹性体供应链，评估非织造基材涂覆/印刷的可行性与成本（对银价波动敏感）。
- **特种光聚合物料采购清单** — LC756（手性剂）、RM82（液晶单体）、EDDET（扩链剂）、PETMP（交联剂）、Irgacure 651（光引发剂）均为小批量特种化学品，供应商集中、交期长，立项开发需提前锁源。同时"结构色免染料/免颜料"契合卫生材料对皮肤接触安全与无重金属染料的合规诉求（推演）。

## Related Pages 关联页面
- 同域合集 Sibling collection：[[Mechanochromic Photonic Sensors]]
- 概念 Concepts：[[机械变色 Mechanochromic]]、[[胆甾相液晶弹性体 CLCE]]、[[摩擦电自供电 TENG]]、[[结构色 Structural Color]]、[[银纳米线 AgNW]]
- 关联主题：[[SAP（高吸水树脂）]]（溶胀耦合推演）、[[Self-Powered Photonic Sensor CLCE Sandwich]] 与 [[Mechanochromic Fluorescent Polymers with AIE Features]] 构成"结构色 vs. 荧光"两条变色读出路线

## Source 原文
- 本地路径 Local path：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mechanochromic_Photonic_Sensors_拆解/LCE自供电光子传感器_拆解.md.md`
- 原文链接 Original link：doi:10.1021/acsami.5c10756

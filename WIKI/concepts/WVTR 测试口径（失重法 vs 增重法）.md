---
type: concept
title: "WVTR 测试口径（失重法 vs 增重法）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-30
tags: [WVTR, 水蒸气透过率, 失重法, 增重法, 测试口径, 底膜, ISO]
aliases: ["Water Vapour Transmission Rate", "水蒸气透过率测试口径"]
---

# WVTR 测试口径（失重法 vs 增重法）

> **Definition 定义**：**WVTR（Water Vapour Transmission Rate，水蒸气透过率）** 是透湿膜/底膜的核心功能指标。**同一材料在不同实验室测得的 WVTR 可以差出一倍以上**——差别不在材料，而在**测试方法族**：**失重法（loss-in-weight，杯内水减少）** 与 **增重法（gain-in-weight，干燥剂增重）**。

## Mechanism of the discrepancy 口径差异的机理

1. **两种方法测量的是相反方向的通量**：失重法跟踪**杯内水的减少**，增重法跟踪**干燥剂的增重**；两者对边界层、温度梯度与密封条件的敏感性不同。
2. **数据可比性的前提是方法一致**：一旦供需双方各用一族，看到的就不是材料差异而是**方法差异**——原文给出的实测关系是**约 2 倍**。
3. **采购后果**：按不同口径比价，会得出与真实性能相反的结论（"我方测得更透湿"可能只是方法不同）。
4. **收敛路径**：推动向 **ISO 标准统一**，并把方法写进规格与验收条款。

## Key parameter table 关键参数表

| Parameter 参数 | Value 值 | Source 出处 |
|---|---|---|
| Method used by supplier (紫华) | **失重法（loss-in-weight）** | [[EM Supplier Meetings 2026-06-02（紫华、恒碳、格菲林、Huayi 四场技术交流）]] |
| Method used by KC China | **增重法（gain-in-weight）** | 同上 |
| Observed offset 观测偏移 | 数据**约 2 倍关系** | 同上 |
| Convergence path 收敛路径 | KC 正推动向 **ISO 标准**统一 | 同上 |
| Related leak test 相关渗漏测试 | KC China 用**达因液加压测试**（较人工经血严苛）；需协商 BCCC 低克重膜标准 | 同上 |
| Typical membrane WVTR (nanofibre reference) | >100,000 g/m²/24h（PU 纳米纤维膜，供应商自测口径） | [[与华峰集团会晤纪要（2026-07-29）]]、[[August R&D Meeting 2026（华峰研发会议）]] |

> ⚠️ **No unsourced parameters 禁止无来源参数**：库内**无**任一具体牌号膜材在两种方法下的对照实测值；「约 2 倍」为**单次会议口头口径**，**不可外推为普适换算系数** `[待验证]`。

## Why it matters to the library 在本库中的用途

- **比价前必问的三件事**：方法族（失重/增重）、温湿度条件、是否密封正压（达因液法）。
- **与既有测试页的关系**：本页是**膜材/底膜**侧的口径问题；芯体侧的验收基准见 [[芯体测试方法与验收基准（STM）]]。
- **与透气性的连带疑问**：同批来源同时给出纳米纤维膜的**空气透过率、静水压、WVTR 与克重**四组数据，但**未说明测试方法**，故其数值与 PE 膜对照时同样存在口径风险（见 [[August R&D Meeting 2026（华峰研发会议）]]）。

## Adjacent concepts 相邻概念

- [[芯体测试方法与验收基准（STM）]]（芯体侧验收基准）
- [[认证与法规的区别]]、[[卫生用品认证体系完全指南]]
- 载体材料：[[Film-Free Backsheet（无膜背层）]]
- 对比：[[SMMMS Film-Free vs Microporous Film Backsheet（无膜背层 vs 微孔膜背层）]]

## Lessons learned 经验教训

> ✅ 验证（2026-09-29，来源 [[EM Supplier Meetings 2026-06-02（紫华、恒碳、格菲林、Huayi 四场技术交流）]]）：本页所载差异是**单点实证**（一次会议上的双方口径对照），方向明确（方法不一致 → 数据不可比），但**幅度（约 2 倍）未经第三方复现** `[待验证]`。

- **教训**：测试口径不是技术细节，而是**采购决策的前置条件**——口径不统一时，任何"性能更优"的结论都不成立。

## Sources 来源

- [[EM Supplier Meetings 2026-06-02（紫华、恒碳、格菲林、Huayi 四场技术交流）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/6.2EM供应商会议纪要.pdf.md`
- [[Raw Material STM - Tianjin Mill WI-60632（原材料标准测试方法-TJ）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM原材料-TJ.pdf.md`
- [[Raw Material STM - Nanjing Plant（原材料STM-NJ）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/原材料STM-NJ.pdf.md`

> ✅ 验证（2026-09-29，来源上述两份）：本页「方法不一致 → 数据不可比」的结论在本批得到**第二条独立证据链**——同一家公司的两个工厂对透气膜 WVTR 采用**完全不同的温湿度与时长**：天津厂 **38 ℃ / 90% RH、面积 33.18 cm²、减重法、预热 0.5 h、间隔 60 min、循环 4 次**；南京厂 **23 ± 2 ℃ / 50 ± 5% RH、33 cm² 圆形试样、透湿杯加 10 mL 二次蒸馏水、腔内干燥剂、12–24 h**。这已不是供应商与 KC 之间的口径差，而是**内部两厂之间的口径差**，风险等级更高。

## 追加：仪器化增湿法第三口径（2026-09-29 追加，不改动上方既有结论）

> 本节为 **Areas / Test Method 批次 08** 编译时的追加记录。上方「失重 vs 增重」两族之外，本批新增**第三条仪器化口径**。

| 项 | 内容 | 出处 |
|---|---|---|
| 方法 | **MOCON PERMATRAN-W 101K 仪器法（增湿法）**：水在膜一侧 37.8 ℃ 蒸发透过，传感器测载气增湿 | [[mocon底膜透气率测试.docx]] |
| 温度口径 | **腔体 37.8 ℃**（区别于上方 23 ℃ / 38 ℃ 杯式两口径） | 同上 |
| 校准 | 双层：Cal C（Raw Counts 60±2）+ 标准膜（偏差 ≤19%） | 同上 |
| 读数 | Transmission Rate gm/m²·day + Permeation gm·mil/m²·day | 同上 |

> ✅ 验证（2026-09-29，来源 [[mocon底膜透气率测试.docx]]）：本页「同材料跨方法差一倍以上、口径是比价前提」的结论获得**第三条证据链**——KC 内部现并存**杯式失重（TJ）、杯式增湿（NJ）、MOCON 仪器（37.8 ℃）三种 WVTR 口径**，跨口径数值只能排序、不能换算，引用 WVTR 必须三要素齐全：**方法族 + 温湿度 + 仪器/杯式**。

## Related Sources 关联来源

- [[August R&D Meeting 2026（华峰研发会议）]]
- [[EM Supplier Meeting Follow-ups]]
- [[EM Supplier Meetings 2026-06-02（紫华、恒碳、格菲林、Huayi 四场技术交流）]]
- [[OI_Project_Profile_OnePager]]
- [[OI_Project_Review_KC_BCC_Red]]
- [[OI_Project_Summary]]
- [[PF · 00_全书摘要]]
- [[PF · analysis_ch09]]
- [[PF · analysis_ch12]]
- [[Raw Material STM - Nanjing Plant（原材料STM-NJ）]]
- [[Raw Material STM - Tianjin Mill WI-60632（原材料标准测试方法-TJ）]]
- [[Raw Material Testing Method Summary（原材料测试方法汇总表）]]
- [[US20240099910A1 Digitally Printed Backsheet Film (RKW SE)]]
- [[mocon底膜透气率测试.docx]]

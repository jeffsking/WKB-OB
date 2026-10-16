---
type: concept
title: "Sensor-Equipped Absorbent Article（含传感器吸收性物品）"
domain: [卫材研发, 变色与智能材料]
status: growing
updated: 2026-09-30
tags: [sensor, leakage detection, 漏液检测, 传感, 尿湿监测, 智能纸尿裤]
---

# Sensor-Equipped Absorbent Article（含传感器吸收性物品）

> One-line definition 一句话定义：在吸收性物品或其配套穿戴物上集成**传感/检测手段**（窗口式可移除传感器、分体式漏液检测衣物等），用于监测渗漏、尿湿或穿戴状态的技术方向。

## Definition / Mechanism 定义与机理拆解

1. **两类集成位置**：
   - **物品内置传感器**：在吸收性物品本体设窗口式可移除传感器（如 P&G US8273939B2 的 windowed removable sensor），直接读取物品内状态。
   - **分体检测衣物**：穿戴在吸收性物品之外的独立衣物（如 K-C US11013641B2 的 leakage-detection garment），间接判断物品是否渗漏。
2. **要解决的用户痛点**：看护者难以及时察觉渗漏/尿湿，导致漏液、红屁屁与频繁检查；传感化把"被动发现"变为"主动提示"。
3. **与既有指示技术的区分**：不同于印刷/化学变色指示（湿敏油墨、力致变色），本方向偏**电子/结构传感**或窗口观察式，常配 APP/视觉提示。
4. **商务边界**：具体电路、算法、量产成本与供应商属敏感信息；本页只沉淀专利面与机理，不页面化商务细节。

## Key parameters 关键参数表

| Parameter 参数 | Typical value / range 典型值 / 范围 | Source 出处 |
|---|---|---|
| 集成位置 Integration | 物品内置（windowed removable sensor）或分体衣物 | [[US8273939B2 Disposable Absorbent Articles Having a Windowed Removable Sensor (P&G)]]、[[US11013641B2 Garment for Detecting Absorbent Article Leakage (Kimberly-Clark)]] |
| 权利人 Assignees | Kimberly-Clark；Procter & Gamble | 同上 |
| 分类 IPC | A61F 13/42, 13/74, 13/84（K-C）；A61F 13/15（P&G） | 同上 |

> ⚠️ **禁止无来源参数**：以上来自两个源摘要页；本库暂无该方向的实测性能、成本或商业化状态，标 `[待验证]`。

## Adjacent concepts 相邻概念

- 上位/相关：[[Wetness Indicator Ladder（尿湿指示阶梯）]]、[[Active Diagnostic Zones（主动诊断分区）]]、[[智能尿裤功能层]]
- 传感测试：[[Pressure Sensory Test（压力触感测试）]]
- 漏液测试：[[Run-off & Leakage Test（滑渗与渗漏测试）]]、[[Blowout Leakage Test（爆漏测试）]]

## 经验教训

> ✅ 验证（2026-09-29，来源 [[US8273939B2 Disposable Absorbent Articles Having a Windowed Removable Sensor (P&G)]]、[[US11013641B2 Garment for Detecting Absorbent Article Leakage (Kimberly-Clark)]]）：本批 02 出现 2 件独立权利人的"传感/漏液检测"专利，确认该方向为卫生用品头部企业的共同布局点；两专利分别覆盖"内置窗口传感器"与"分体检测衣物"两种路径。

- **待补 `[待验证]`**：两类方案的实测检测准确率、功耗/量产成本、与化学指示方案的优劣对比。

## 追加：Meeting Minutes 批（2026-09-29 追加 · IoT 方案的参数包、市场口径与三重落地风险）

> 来源：[[Diaper NPD Workshop Prep — Absorbency, Skin Health & Comfort Feature Map（2026-06-05）]]（Workshop 准备材料 v1.0，2026-06-05）。本批只**追加**，不修改既有结论。

**参数包（本批新增）：**

| Item 项目 | Value 数值 |
| --- | --- |
| 监测维度 | **湿度 / 温度 / 尿量** 三重监测 |
| 技术构成 | **柔性传感器 + 蓝牙传输** |
| 湿度检测精度 | **±5% RH** |
| 温度检测范围 | **25–40 °C** |
| 尿量估算误差 | **<10%** |
| 电池续航 | **>7 天** |
| 目标用户 | 高端婴儿 + **成人失禁护理** |

**市场口径（本批新增）：**

- 全球智能纸尿裤市场 **CAGR >25%（2024–2030）**；
- 主要玩家：**Ontex + Henkel（Orizon 产品）**；
- 技术壁垒：**柔性电子 + 超薄电池 + 皮肤安全性**。

**三重落地风险（本批新增，是本页最有价值的部分）：**

| 风险 | 内容 |
| --- | --- |
| **成本** | 传感器 + 电子元件 → 单片成本 **+¥3–5** |
| **皮肤安全性** | **柔性电极的生物相容性验证** —— 与皮肤长期接触，属本库 [[Material Safety Control（材料安全双轨管控）]] 的覆盖范围 |
| **可回收性** | **电子废弃物处理** —— 与行业的可持续方向直接冲突 |

**由此得到的认知（本批新增）：**

1. **智能感知的最大阻力不是技术，是"可回收性"** —— 把电子元件引入一次性卫生用品，与可降解/可回收的大方向**结构性冲突**；这也是它被 Workshop 列为"概念验证"级（优先级 ⭐⭐）的原因。
2. **三项风险分属三个不同职能**：成本归采购/财务、皮肤安全归法规/安全、可回收归可持续 —— 任一职能都能否决，因此**必须三方并行评估**，不能串行。
3. **成人失禁是比婴儿更现实的首发场景** —— 文档把"成人失禁护理"与"高端婴儿"并列为目标用户；成人侧对**成本敏感度更低、护理需求更强**，通常是该类技术的更早落点。
4. **与"免电力"路线的对照**：[[Mechanophore Mechanochromism（机械力致变色分子）]] / [[Structural Colour Mechanochromism（结构色力致变色）]] 提供的是**不需要电源与布线的可视化**路线 —— 两者是"主动电子感知"与"被动材料感知"的**替代关系**，评估时应对照。

> 🔴 **manual_review（2026-09-29）**：本页涉及单片成本（+¥3–5）、市场 CAGR 与竞品玩家，属商务信息；按 AGENTS.md §5 只保留量级与机制。请回原文核对：
> `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/Workshop_Prep_Absorbency_SkinHealth_Comfort_2026.md.md`

✅ **验证记录（2026-09-29）**：以上为 **Workshop 准备材料 v1.0** 口径，引用 `references/58` **原始文件未随本批次提供**；CAGR >25% 与 Ontex/Henkel 玩家信息为文档口径，须回溯原始市场报告 [待验证]。参见 [[Material Safety Control（材料安全双轨管控）]]、[[Active Diagnostic Zones（主动诊断分区）]]、[[Structural Colour Mechanochromism（结构色力致变色）]]。

## Sources 来源

- [[US8273939B2 Disposable Absorbent Articles Having a Windowed Removable Sensor (P&G)]] —— `RAW/ima_sync/个人知识库/WKB/Areas/IP/US8273939.pdf.md`
- [[US11013641B2 Garment for Detecting Absorbent Article Leakage (Kimberly-Clark)]] —— `RAW/ima_sync/个人知识库/WKB/Areas/IP/US11013641.pdf.md`
- [[US20220125319A1 Moisture and Fever Sensing Apparatus (Farnaz Zand)]] —— `RAW/ima_sync/个人知识库/WKB/Areas/IP/US20220125319A1.pdf.md`（2026-09-29 追加）
- [[US 20250064649A1 Intelligent Monitoring Diaper with Enhanced Features (Wu Guohui)]] —— `RAW/ima_sync/个人知识库/WKB/Areas/IP/六-1_Intelligent_Monitoring_Diaper_with_Enhanced_Features.pdf.md`（2026-09-29 追加）

## Evidence Update 证据追加（2026-09-29 · Areas/IP 第 4 批）

> ✅ 追加（2026-09-29，source 来源 [[US20220125319A1 Moisture and Fever Sensing Apparatus (Farnaz Zand)]]）：本批新增一例**"耗材可抛 + 电子件可复用"的双传感架构**，可作为本页既有两类方案之外的第三条参考路径。**只追加事实，不修改原结论**：
>
> - **同一条耗材上并行两条传感通道**：一条高效**毛细虹吸条**（尺寸约 7.75 × 0.5 × 0.063 inch，来源标明可购自 Filtrona Richmond, Inc.，商标名 TRANSPAD）——第一面丝印**两条间隔的导电油墨带**（间距优选为单条带宽的一半，厚度优选 0.002–0.003 inch，碳粉或银粉 + 丙烯酸树脂/溶剂）负责**尿湿**；第二面印**一条热致变色油墨带**负责**温度**。
> - **读取方式从"人看"变成"机器读"**：热致变色油墨变色 → **颜色传感器**产生信号 → 收发单元（**Bluetooth 或 WiFi**）→ 通知终端（计算机 / 手机 / 扬声器）。这与本页既有两条路径（窗口式可移除传感器、泄漏检测服装）都不相同，是"印刷油墨 + 光电读取"的混合路线。
> - **数值判据**：权利要求记载热致变色油墨在 **>98.6 °F**（高于正常体温）时变色；化学体系可为温敏有机分子（受热时分子在两种细微不同结构间切换）或 **leuco dyes**。
> - **背景列出的电子式误报清单（可直接进坑表）**：载流导体须穿过尿裤塑料外层、皮肤可能暴露于较高电压、灵敏区有限、**坐在潮湿或金属的长椅/公园滑梯上会误触发**。本案以毛细迁移替代暴露电极来规避。
>
> 🔴 **manual_review（2026-09-29）**：该来源为 **A1 申请公开**（公开日 2022-04-28），是否授权、权利要求是否被限缩，来源未记载 → `[待验证]`；**是否可自由实施（FTO）不作 AI 结论**，须由专利代理或法务评估。
>
> 追加 `[待验证]`：颜色传感器在实际尿裤光照/遮挡条件下的读数稳定性；蓝牙/WiFi 待机功耗与更换周期的实测。

### Evidence Update 证据追加（2026-09-29 · Areas/IP 第 4 批 · 第 2 条）

> ✅ 追加（2026-09-29，source 来源 [[US 20250064649A1 Intelligent Monitoring Diaper with Enhanced Features (Wu Guohui)]]）：本批新增一例**"可复用监控器夹 + 一次性导电层"的第四类架构**。**只追加事实，不修改原结论**：
>
> - **架构**：昂贵的多传感器监控器做成**带弹性夹的可拆模块**，一次性尿裤本体上只保留**导电层内的栅格状导电线缆**（纵横交错）作为耗材；防水层在接触点**开孔**露出线缆，弹性夹压紧**导电弹簧针（pogo pin）**完成电气连接。原文称此举"**reduces costs while promoting environmental sustainability**"。
> - **检测原理为电阻法**：尿液渗入导电线缆 → **电阻变化** → 主控板判定是否有尿。这既不同于本页既有的窗口式/分体式路径，也不同于 [[Light-Scattering Masking Wetness Indicator（光散射遮蔽型尿湿指示）]] 的光学法。
> - **传感器栈**（均挂在同一主控板上）：体温、湿度、**气味**（列举 H2S、NH3、C8H7N、C9H9N、CH3COOH、C4H8O2、H2、CH4，用于**判粪便**）、运动（三轴/六轴加速度，用于**睡姿**）、报警（扬声器 + LED）、通信（Bluetooth 或 WIFI）、GPS、以及**酶检测模块**（吸水层上的酶试纸，测尿酸；原文称可换为总胆固醇或 HDL 胆固醇试纸）。
> - **对"上位/相关"的补充**：本件把**生化检测（酶试纸）并入同一个电气接口**，是本页既有两条路径未覆盖的扩展方向。
>
> 🔴 **manual_review（2026-09-29）**：该来源为 **A1 申请公开**（公开日 2025-02-27，申请号 18/455,603），**是否授权、审查过程、延续/分案情况 → `[待验证]`**；原文含权 4 引权 4、权 7 引权 7 的自我引用，以及 [0044] 提及"blood sugar readings"但全文无血糖传感器等**文本不一致**（客观记录，不作法律效力推断）；**是否可自由实施（FTO）不作 AI 结论**。
>
> 追加 `[待验证]`：电阻法在多次排尿后的**基线漂移与误报率**；pogo pin 与栅格线缆在反复拆装后的**接触可靠性**；气味传感器在真实尿裤微环境下的**选择性与阈值**。

> 🔴 **manual_review（2026-09-29）**：本页为**专利技术方案的客观摘录**，不构成侵权或 FTO 判断；各专利法律状态须逐件核实。具体电路/算法/供应商与成本属商务敏感，不页面化。

## Related Sources 关联来源

- [[Diaper Market Claims and Marketing Concept Landscape（市场宣称与营销概念全景）]]
- [[Diaper NPD Workshop Prep — Absorbency, Skin Health & Comfort Feature Map（2026-06-05）]]
- [[Elastic Tension Visualization Technology Assessment（拉力松紧可视化技术评估）]]
- [[New Core Concepts and Claims Draft（芯体新概念与市场宣称草案·8 概念）]]
- [[Smart Sensing Diaper Technology Research Report（智能感知纸尿裤技术研究报告 · 2026-04）]]
- [[The Chromatic Shift（力致变色：Naphthopyran 与 HPC 双路线）]]
- [[US 20250064649A1 Intelligent Monitoring Diaper with Enhanced Features (Wu Guohui)]]
- [[US11013641B2 Garment for Detecting Absorbent Article Leakage (Kimberly-Clark)]]
- [[US20220125319A1 Moisture and Fever Sensing Apparatus (Farnaz Zand)]]
- [[US8273939B2 Disposable Absorbent Articles Having a Windowed Removable Sensor (P&G)]]

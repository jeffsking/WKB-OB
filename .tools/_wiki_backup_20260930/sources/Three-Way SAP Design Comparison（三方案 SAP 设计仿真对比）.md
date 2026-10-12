---
type: source
title: "Three-Way SAP Design Comparison（三方案 SAP 设计仿真对比）"
source_type: 提案
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP_Three_Way_Design_Comparison.pptx.md
original_link: ""
date_published: 2026-09
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "Three designs compared at equal 15 g total SAP add-on on a 385x110 mm sandglass core, 6-month infant, 3 sequential urine insults: zoned NR-610S/NR-950 blend (A), zoned KC511/NR-950 blend (C), mono KC511 uniform (B)（中文：在总添加量 15 g 相同的条件下对比分区混掺 A、分区混掺 C、单牌号均布 B）"
  - "Design C (zoned KC511/NR-950) dominates A on every capacity and permeability metric: worst-zone saturation 67% vs 76%, blend AUL 19.0 vs 16.5 g/g, blend GBP 14.4 vs 7.2（中文：C 在容量与渗透上全面优于 A）"
  - "Design B (mono KC511 uniform) overflows the crotch zone at 129% — a leak-risk signal regardless of blend choice; carry forward only as cost fallback（中文：单牌号均布方案裆部饱和 129% 溢出，仅作成本备选）"
  - "The known caveat: the capacity-budget model does not score acquisition speed, where NR-610S vortex 19 s beats KC511 29 s（中文：已知局限——容量模型不评摄入速度，NR-610S 涡流 19 s 优于 KC511 29 s）"
  - "Decision rule: if bench cGAM-LTD acquisition time for C stays within spec, prefer C (better margin, better permeability, one fewer SKU); otherwise A remains the faster-acquisition option（中文：决策规则——若 C 的摄入时间达标则选 C，否则 A 仍是更快摄入方案）"
pages_linked: ["[[SAP Zoned Blend vs Mono Design（分区混掺 vs 单牌号均布 · SAP 设计对比）]]", "[[SAP性能指标（CRC AUL GBP Vortex）]]", "[[SAP 四牌号性能对比（KC511 vs NR-610S vs NR-950 vs Code X）]]", "[[分区密度设计]]", "[[Multilayer SAP Core（多层SAP芯体）]]"]
---

# Three-Way SAP Design Comparison（三方案 SAP 设计仿真对比）

## 一句话定位 One-line Positioning

本批**SAP 芯体设计的仿真对照实验（R&D Design + Simulation Study — Update）**：在总添加量严格相同（15 g）的前提下，同时隔离两个问题——**分区布点是否优于均匀铺展**、以及**把混掺中的快吸组分从 NR-610S 换成 KC511 是否改变结论**。是本库回答「芯体 SAP 怎么分布、混掺怎么配」的量化依据。

## 摘要 Summary

设计集统一条件：**385×110 mm 沙漏型芯体（sandglass core）**、**6 个月婴儿**、**3 次连续排尿（3 sequential urine insults）**、**三者总 SAP 添加量均为 15.0 g**，面层 SAP1 均为 KC 511，同一面层、同一总质量，**唯一变量是 poly 侧（聚合物侧）的混掺配比与是否分区**。

**Design A（分区 · NR-610S / NR-950 混掺）**：面层 SAP1 = KC 511；poly = 40% NR-610S + 60% NR-950。**Design C（分区 · KC 511 / NR-950 混掺，NEW）**：面层 SAP1 = KC 511；poly = 40% KC 511 + 60% NR-950。**Design B（单牌号 · KC 511 均布）**：liner = KC 511，poly = 100% KC 511，**按面积均布、不做摄入靶向**。A 与 C 共用完全相同的 SAP1/面层分配与分区图形（沿用前一份 deck 的 insult-targeted zoning），仅把 poly 侧快吸组分由 NR-610S 换成 KC 511；B 按区分面积铺展、不做靶向。因此该设计集一次性隔离两个问题：**分区是否胜过均布**，以及**更换快吸组分是否改变结论**。

分区添加量（沿 385 mm 长度，单位 g）：Front（A/C：SAP1 0.53、快吸组分 0.23、NR-950 0.35；B：liner 1.20 / poly 2.23）、Front-Mid（1.84 / 0.87 / 1.31；B：1.00 / 1.86）、Crotch（2.10 / 1.56 / 2.34；B：0.88 / 1.64）、Back-Mid（0.63 / 0.94 / 1.40；B：1.00 / 1.86）、Back（0.16 / 0.30 / 0.45；B：1.16 / 2.16）。

仿真结果（第 3 次 insult 后的分区饱和度，% 分区容量占用）：**Design C 领先**——C 的最差分区（Back）峰值 **67%**，低于 A 的 **76%**；**Design B（单牌号）仍在 Crotch 分区溢出，达 129%**。原因是 **KC511 在 AUL（18.4 vs 12.1 g/g）与 GBP（24 vs 6）两项上均优于 NR-610S**，把 KC511 换进混掺后各处容量裕度都被抬高。**明确 caveat**：该容量预算模型**不评摄入速度**——NR-610S 更快的 vortex（19 s vs KC511 的 29 s）是这张图看不见的真实优势。

取舍表（0.7 psi 口径）：峰值分区饱和度 A 76%（Back）/ C 67%（Back）/ B 129%（Crotch 溢出）；混掺 AUL A 16.5 / C 19.0 / B 18.4 g/g；混掺 GBP A 7.2 / C 14.4 / **B 24（本组最佳）**；快吸组分 vortex A 19 s（可得最快）/ C 29 s / B 29 s；需认证的 SKU 数 A 2（KC511、NR-610S、NR-950）/ C 2（KC511、NR-950）/ B 1（仅 KC511）。判读：在该模型下 **C 在每一项容量与渗透指标上都优于 A**——以 KC511 取代混掺中的 NR-610S，既把采购简化到 2 个牌号，又同时改善饱和裕度与 GBP；**唯一放弃的是初始摄入速度**（KC511 29 s vs NR-610S 19 s），而这恰是饱和模型无法捕捉的。若台架 cGAM-LTD 测试表明该速度差在实践中确实重要（面层湿感、strike-through），则 A 仍是更快的摄入方案；若不重要，C 是更强的默认选择。

下一步：① 对 A 与 C 原型做台架 cGAM-LTD 摄入时序测试（这是容量模型无法裁决的唯一变量）；② 若 C 的摄入时间仍在规格内则优先 C（容量裕度更好、渗透更好、少一个 SKU 要认证）；③ 以**混合实测**而非线性平均重新确认 KC511 + NR-950 的混掺 AUL/GBP（与原 NR-610S/NR-950 混掺同样的 caveat）；④ Design B（单牌号 KC511）**仅作为成本备选保留**——其裆部溢出 129% 在该 insult 节奏下是**漏尿风险信号**，与混掺选择无关；⑤ 在最终锁定 gsm 前，把三个设计都按 **4–5 次 insult/wear（过夜场景）**重跑。

## 提炼的数字与结论 Key Numbers and Conclusions

| 项目 Item | Design A（分区 NR-610S/NR-950） | Design C（分区 KC511/NR-950） | Design B（单牌号 KC511 均布） | 备注 Note |
|---|---|---|---|---|
| 面层 SAP1 / liner | KC 511 | KC 511 | KC 511 | 三者一致 |
| Poly 混掺 | 40% NR-610S + 60% NR-950 | 40% KC511 + 60% NR-950 | 100% KC511 | 唯一变量 |
| 总添加量 | 15.0 g | 15.0 g | 15.0 g | **等量对照** |
| 是否分区靶向 | 是（insult-targeted） | 是（与 A 同图形） | 否（按面积均布） | 隔离第二个问题 |
| **峰值分区饱和度** | **76%（Back）** | **67%（Back）** | **129%（Crotch，溢出）** | 第 3 次 insult 后 |
| 混掺 AUL（0.7 psi） | 16.5 g/g | **19.0 g/g** | 18.4 g/g | — |
| 混掺 GBP | 7.2 | 14.4 | **24（本组最佳）** | — |
| 快吸组分 vortex | **19 s（可得最快）** | 29 s | 29 s | 模型未计分 |
| 需认证 SKU 数 | 2（另含 NR-610S） | 2 | **1** | 采购复杂度 |
| 关键牌号对比 | NR-610S：AUL 12.1、GBP 6、vortex 19 s | KC511：AUL 18.4、GBP 24、vortex 29 s | — | KC511 容量与渗透全面胜出 |
| 仿真场景 | 385×110 mm 沙漏芯体、6 月龄婴儿、3 次连续排尿 | 同 | 同 | 需再跑 4–5 次/过夜 |
| Crotch 分区添加量 | SAP1 2.10 / 快吸 1.56 / NR-950 2.34 g | 同 A | liner 0.88 / poly 1.64 g | B 在裆部投入最少 |

## 关键论断（key_claims）

- **分区靶向是必要项：单牌号均布在裆部溢出 129%，是漏尿风险而非成本优势** —— 支撑页：[[SAP Zoned Blend vs Mono Design（分区混掺 vs 单牌号均布 · SAP 设计对比）]]
- **容量与渗透 vs 摄入速度是两个维度，容量模型会系统性低估快吸组分的价值** —— 支撑页：[[SAP性能指标（CRC AUL GBP Vortex）]]
- **混掺性能必须实测，不能线性平均** —— 支撑页：[[SAP 四牌号性能对比（KC511 vs NR-610S vs NR-950 vs Code X）]]
- **SKU 数量是可量化的采购复杂度：C 比 A 少一个牌号且性能更好** —— 支撑页：[[SAP Zoned Blend vs Mono Design（分区混掺 vs 单牌号均布 · SAP 设计对比）]]

## 关联页面

- 概念：[[SAP性能指标（CRC AUL GBP Vortex）]]、[[分区密度设计]]、[[Multilayer SAP Core（多层SAP芯体）]]、[[SAP错峰膨胀]]、[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]
- 实体：（本页牌号对比见下；供应商商务条款未涉及）
- 对比：[[SAP Zoned Blend vs Mono Design（分区混掺 vs 单牌号均布 · SAP 设计对比）]]、[[SAP 四牌号性能对比（KC511 vs NR-610S vs NR-950 vs Code X）]]、[[单牌号全511 vs 分层多SAP混底（性能·成本·供应链）]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAP_Three_Way_Design_Comparison.pptx.md`
- 原文链接：（无；内部资料）

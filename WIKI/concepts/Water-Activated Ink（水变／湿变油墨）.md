---
type: concept
title: "Water-Activated Ink（水变／湿变油墨）"
domain: [卫材研发, 智能功能化, 材料]
status: growing
updated: 2026-09-30
tags: [水变油墨, 湿变, 尿显, PEG, 酯类溶剂, 透显性, 图案化]
aliases: ["Hydrochromic Ink", "水变油墨", "湿变油墨"]
---

# Water-Activated Ink（水变／湿变油墨）

> **Definition 定义**：A printed ink system that **changes colour on contact with liquid water** and is designed as an **irreversible** cue for wetness indication in diapers. It is the printed-ink alternative to the traditional [[Wetness Indicator Glue]] line, and its defining advantage is that it **can be printed as a pattern** — which a glue line cannot.
> （遇水显色、面向尿显设计为**不可逆**的印刷油墨体系；是传统 [[Wetness Indicator Glue]] 胶线之外的印刷替代方案，其决定性优势是**可印成图案**，而胶线做不到。）

## Mechanism 机理

1. **Three-material system 三物质体系**：**物质一 + 物质二**遇水反应显色（最终颜色由两者混合决定）；**物质三**是隔离层，负责在干燥态把一、二隔开，遇水被冲走 → 一、二接触 → 显色。物质三**疑似中低分子量 PEG 成分** `[待验证]`。
2. **Irreversibility is designed in 不可逆是设计选择**：物质三被水冲走后不会自动复位，因此该体系对尿显场景是**单向**信号（"已经湿了"），与可逆温变体系形成对照。
3. **Colour palette 色域**：目前有蓝、绿、橙（粉红）三色 + 定制酒红色；**干燥态呈粉状**，须先制成油墨再印刷。
4. **Graded display is a proposed extension 分级显示是待开发扩展**：希望通过**调整物质三的分子量**设定溶解阈值，或在一、二体系中增加多级变色物质，实现"达到一定尿量（如 60–80 mL）或多次排尿后才触发"——**属待探讨方向，非现有能力**。

## What blocks it 真正的卡点

| Issue 问题 | Substance 实质 | Status 状态 |
|---|---|---|
| **Optical transmittance 透显性** | 吹膜白度高 + 背面对视 + 底层无纺布叠加 → 成品显色打折扣；在**流延膜上效果很好**，成品上不如膜上直观 | **先天障碍**，须靠结构设计弥补 |
| **Humid storage 高湿储存** | 25 ℃/90% RH 有数据支撑、允迪有数月数据，但**仍有提前变色风险** | 未闭合 |
| **Colour decay 显色衰减** | 显色后 10 小时内深浅有衰减 | 仍保持一定变色稳定性 |
| **Dosing window 加量窗口** | 油墨色粉加在溶剂中，**加量过多会提前析出**、有提前变色风险，需换配方体系才能突破（工程量大） | 需配方体系突破 |
| **Printing parameter mismatch 印刷参数不匹配** | 恒耀柔印一下午完成打样；允迪设备上始终找不到合适参数点（疑与设备档次有关） | 待确认设备品牌/型号 |

## Advantages claimed 原文主张的优势

1. **变色稳定，不受尿液 pH 值影响**（对比 pH 指示型尿显）。
2. **无甲醛、无卤素**，安全性好；**无传统尿显胶异味**（原文：尿显胶是胶中气味最大的一块）。
3. **油墨可印各种图案**，视觉呈现远优于尿显胶刮条（**尿显胶无法实现图案化**）。
4. **潜在降本**：印刷克重约 **3–4 g/m²**（视网纹辊目数）vs 尿显胶约 **25–30 g/m²**——即便油墨单价数百元/kg，**成本理论上有百分之几十的下降空间**。

## Key parameter table 关键参数表

| Parameter 参数 | Value 值 | Source 出处 |
|---|---|---|
| System 体系 | 三物质（一/二显色 + 三隔离层） | [[Water-Activated Ink Wetness Indicator & Matsui Shikiso Technical Exchange（水变油墨尿显暨松井技术交流纪要 2026-08-14）]] |
| Separating layer 隔离层 | 疑似中低分子量 PEG `[待验证]` | 同上 |
| Reversibility 可逆性 | **不可逆**（针对尿显设计） | 同上 |
| Ink print weight 印刷克重 | 3–4 g/m² | 同上 |
| Glue line weight 胶线克重 | 25–30 g/m² | 同上 |
| Theoretical cost reduction 理论降本 | 百分之几十 | 同上（**潜在值，非实测**） |
| Colours 颜色 | 蓝 / 绿 / 橙（粉红）+ 定制酒红 | 同上 |
| Dry form 干燥态 | 粉状，须制墨印刷 | 同上 |
| Threshold target 阈值目标 | 60–80 mL 或多次排尿 `[待验证]`（讨论中） | 同上 |
| Storage test 储存测试 | 25 ℃ / 90% RH | 同上 |
| Decay 显色衰减 | 10 小时内深浅衰减 | 同上 |
| Chemical classification 化学分类 | 低等级危化品（含**酯类溶剂**） | 同上 |
| MSDS 披露 | 部分保留；与宝洁签安全协议时才披露 | 同上 |

> 🔴 **manual_review（2026-09-29）**：本来源含**价格与认证费用类商务敏感信息**（起订量下的通关/物流费用、第三方单项安全认证费用、宠物领域落地价）。依 AGENTS.md §5，本页**只保留克重与理论降本幅度**用于路线判断，**不展开具体报价与费用数字**。

> ⚠️ **No unsourced parameters 禁止无来源参数**：本页**无**该油墨在真实尿裤上的粘度/网纹辊规格、耐光性数据与迁移检测数值 `[待验证]`。

## Adjacent concepts 相邻概念

- 对照路线：[[Wetness Indicator Glue]]（热熔胶线，不可逆、可量产）、[[Thermochromic Microcapsule (Leuco Dye System)]]（温变，可逆，相变 vs 微胶囊两种实现）
- 上位概念：[[变色油墨]]、[[Chromism Taxonomy（变色现象分类）]]
- 使能技术：[[Microencapsulation]]（胶囊壁承压可调）
- 应用层：[[智能尿裤功能层]]、[[Diaper Microclimate]]
- 对比：[[Thermochromic vs Hydrochromic Wetness-Comfort Indicators]]、[[Urine Indicator vs BM Indicator（尿湿指示 vs 便指示）]]

## Lessons learned 经验教训

> ⚠️ **Route risk is physical, not chemical（2026-09-29 归纳）**：本页把"透显性"与"高湿储存提前变色"列为**两大未闭合卡点**——前者是**结构/光学**问题（不是化学问题），后者是**保存性**问题。任何以"油墨可印图案 + 克重更轻"为由推进该路线的判断，都必须先给出这两项的证据。
> ✅ 验证（2026-09-29，来源 [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]）：该来源把水基湿致油墨定位为**第二阶段差异化/环保选项**，并给出"可设计为可逆"的口径；本来源实测为**不可逆**（针对尿显设计）。两者**不矛盾但口径不同**——可逆性取决于定制配方而非体系先天属性，按 AGENTS.md §5 并列记录、待人工确认。
> ⚠️ 由此产生的**成本口径差异**：既有路线材料记"水基油墨相对热熔胶约 2–3 倍成本"，本来源记"理论上百分之几十下降空间"——两者**口径不同（成品形态 vs 印刷克重理论值）**，不构成直接矛盾，但**不可混用**。

## Sources 来源

- [[Water-Activated Ink Wetness Indicator & Matsui Shikiso Technical Exchange（水变油墨尿显暨松井技术交流纪要 2026-08-14）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/录音纪要_260814232451_1.md`
- [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/ThermoHydro_TechReview_EN_v3_2026-08-05.pptx.md`

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · 湿变微胶囊的量化边界与单一来源风险）

> 来源：[[温变湿变微胶囊技术参数对比表（X-Chromic 版 · 2026-06-18）]]（公开文献 + 厂商 Datasheet + 行业报告汇编，2026-06-18）。

| 维度 | 湿变微胶囊（Hydrochromic） | 对照：温变 |
|---|---|---|
| **触发** | 水分/湿气接触，**遇水、遇尿即刻变色**；**对 >85% RH 敏感** | 温度（−10~150 °C 可选，可定制 ±0.5 °C） |
| **响应时间** | **0.1 ~ 1 s** | 0.5 ~ 5 s |
| **粒径** | 主流 **2 ~ 15 μm** | 丝印/移印 1~10 μm；凹印/柔版 <5 μm |
| **壁材** | MF / 聚脲 / 聚丙烯酸酯；**亲水性需精确调控** | MF（主流）/ 聚脲（高端） |
| **可逆性** | 可逆型数千次（Ledio 宣称 >5,000）；**不可逆型（一次性尿显）为主流** | 可逆为主流 |
| **包覆率** | **要求极高，水分提前渗入即失效** | 国内 75~85% / 国际 ≥92% |
| **耐候/储存** | **低**：极敏感，需严格防潮密封，生产过程避开水汽 | 中 |
| **成本（元/kg）** | 国内 300~800 / 进口 800~2,000+ | 国内 200~800 / 进口 800~1,500+ |

1. **湿变的物理难点有明确来源** —— **水分子仅 ~0.28 nm**，「对壁材致密性要求**远高于**温变微胶囊」。**⇒ 湿变的密封是分子级问题，不是工艺精度问题。**
2. **核心指标是"响应速度 × 选择性"的组合，不是速度** —— 需 **0.1~0.5 s** 对微量尿液显色，**但不能被 <85% RH 的环境湿度错误触发**；**壁材亲水性需精确到分子级调控**。**⇒ 只报"响应 0.1 s"的湿变方案不可采信，必须同时给出误触发边界。**
3. **湿变亦有"更小粒径挑战包覆率"的反向约束** —— 与温变"越小越好"不同，湿变**粒径越小越难包覆**。**⇒ 湿变的粒径窗口是双向受限的，不能照搬温变的细化路线。**
4. **⚠️ 供应链风险显著高于温变** —— **CTI（美国）持有 Yellow→Blue 专利体系，被源文描述为"几乎垄断"**；国内（广州乐迪、心茉新材料、SUNREE）**"起步阶段，尚无大规模量产能力"**。**⇒ 选湿变 ≈ 接受单一来源风险，须在立项时显式接受。**
5. **不可逆型才是尿显主流** —— 源文明确「不可逆（一次性尿显指示为主流）」。**⇒ 可重复使用的湿变是可选项，不是默认项；产品定义应先确定"一次性指示"还是"可逆指示"。**
6. **产线适配的硬约束** —— **纸尿裤产线多采用溶剂型凹印**，而湿变**凹印"粒径和粘度挑战大"**。**⇒ 选型前必须先确认产线印刷方式与溶剂体系，否则配方无法落地。**
7. **应用场景局限** —— 主要用于**一次性尿显指示与防伪**，**市场规模远小于温变**；**⇒ 湿变的供应商投入意愿与迭代速度会长期低于温变。**

> ✅ 验证（2026-09-29）：本节为**追加**，**未修正上方任何既有结论**。
> 🔴 **manual_review（2026-09-29）**：源文**成本区间（元/kg）为公开资料汇编的估算**，附"因品牌/型号/批次不同可能存在差异"的免责说明；**不得作为采购议价依据、不得对外引用**。**"CTI 垄断""国内尚无大规模量产"等为源文判断，本页未独立核验**。**Ledio / 广州乐迪"宣称 >5,000 次循环"为厂商宣称，非实测**。另：MF 壁材的**甲醛属性**在卫材接触场景须由材料安全流程单独评估。

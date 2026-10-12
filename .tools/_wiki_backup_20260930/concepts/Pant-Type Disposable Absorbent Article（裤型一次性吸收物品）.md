---
type: concept
title: "Pant-Type Disposable Absorbent Article（裤型一次性吸收物品）"
domain: [卫材研发, 结构设计]
status: seed
updated: 2026-09-29
tags: [裤型, pull-on, pants-type, 侧缝焊接, tearable seam, 一次性吸收物品]
aliases: ["Diaper Pants", "Pull-On Article", "裤型纸尿裤", "拉拉裤"]
---

# Pant-Type Disposable Absorbent Article（裤型一次性吸收物品）

> One-line definition 一句话定义：制造商在出厂时就已把前后部侧边缘**连成闭合腰围**的一次性吸收制品（diaper pants / pull-on article）——使用时**像内裤一样拉上脱下**，可站立更换；其核心工程命题是**闭合状态下的侧缝既要够牢，又要在弃用时能撕开/脱下**。

## Definition / Mechanism 定义与机理拆解

1. **形态起点不同**：常规开放式纸尿裤是"装上之后才像裤子"，裤型产品**从一开始就是裤子**——由制造商把前后部的侧边缘接合（见 [[EP1581159B1 Method for Producing Diaper Pants（弹性片材）]]）。
2. **用法牵引结构**：因为要求**穿戴者站立时被拉下再换上**，所以腰带要做到"能拉开到过臀围、回落又贴合"，这与"开放式 + 魔术扣"的力学要求不同。
3. **侧缝的双重角色**（本概念的关键张力）：一侧要承受穿脱与活动中的**剪切载荷**；另一侧又要在弃用时**可撕开（tearable）**。本案给的解法是把焊缝设计成**只承受剪切力**，并在最内侧重叠侧边末端做出位于焊缝之外的**抓手（grip part）**作为撕开的物理拉手。
4. **薄型化约束**：前后的侧边缘只做**单层搭接（singly overlap）**、不做翻折层叠，因此接合区**不臃肿（not bulky）**；说明书明确这是优于"需要把片材翻面（turning the blank inside out）"那类做法的地方。
5. **过程中的张力管理**：折边与焊接期间，待焊接的那部分展开侧边缘必须在夹具区域内保持**松弛、无应力（relaxed and unstressed）**——即由支撑件承担定位与应变，**不让弹性侧片参与定尺寸**。
6. **图形是这个载体上的第二层功能**：裤型产品的侧翼常被用作**用户沟通载体**（"抓这里拉"），这把结构设计与 [[Informational Image on Pull-On Article（可穿脱制品信息图形）]]、[[Graphic Sheet in Non-Stretch Zone（非弹性区图形片）]] 绑到了一起。

## Key parameters 关键参数表

| Parameter 参数 | Typical value / range 典型值 / 范围 | Source 出处 |
|---|---|---|
| 侧缝焊接方式 seam welding | 超声焊或热焊（ultrasonic or thermal welding）；须至少一片 cover sheet 可热焊 | [[EP1581159B1 Method for Producing Diaper Pants（弹性片材）]] Claim 1 |
| 焊缝宽度 weld seam width | **6–10 mm**，优选 7–9 mm，**最优选 8 mm** | 同上 Claim 8 |
| 最外侧重叠长度 outermost overlap | **< 10 mm**，优选 < 7 mm，**最优选 < 4 mm** | 同上 Claim 7 |
| 焊缝强度 seam strength | **10–45 N/25mm** | 同上 Claim 10 |
| 是否可撕开 tearability | 焊缝**可被撕开（can be torn open）** | 同上 Claim 9 |
| 撕开结构 tear structure | 最内侧重叠侧边缘末端做成位于焊缝之外的 **grip part（抓手）** | 同上 Claim 6 |
| 焊缝受力状态 load mode | 主要**仅受剪切力（exposed only to shear forces）** | 同上 说明书 [0006] |
| 加工过程张力 process tension | 支撑件区域内的展开侧边缘在折边与焊接中保持**松弛无应力** | 同上 Claim 4 |
| 代表人物 proprietary example | 专利权人 **SCA Hygiene Products AB**（EP 1 581 159 B1，2012-04-11 公告授权） | 同上 INID (73)(45) |

> ⚠️ **禁止无来源参数**：表中每项均可回溯至所列源摘要页；未见于来源的一律写 `[待验证]`。

> 🔴 **manual_review（2026-09-29）**：本页只归纳**各件专利公开的技术方案**。以下内容 AI 不作结论：
> - **FTO / 侵权**：我方裤型产品的侧缝搭接长度、焊缝宽度、强度窗口是否落入任何一件现有权利要求，须由专利代理或法务比对授权公告文本后独立评估。
> - **法律状态**：本页引述的 EP 1 581 159 B1 已于 **2012-04-11** 公告授权（来源记录日期 2026-09-29），但**是否仍在维持、指定国是否生效、有无异议或限缩，来源未记载 → `[待验证]`**。

## Adjacent concepts 相邻概念

- 上位 / 相关：[[CD Pants Converting Process（CD裤式产品加工工艺）]]（加工路线在同库该工艺页另有归纳）
- 相关结构：[[Waist Guard（腰围护挡）]]（同为裤型产品的防漏/贴合部件，见 P&G US 2022/0339044 A1）
- 相关工艺失效：[[Elastic Strand Snicking（弹性橡筋断丝失效化）]]（侧翼切断与橡筋风险相邻）
- 用户沟通：[[Informational Image on Pull-On Article（可穿脱制品信息图形）]]、[[Graphic Sheet in Non-Stretch Zone（非弹性区图形片）]]

## Sources 来源

- [[EP1581159B1 Method for Producing Diaper Pants（弹性片材）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/IP/20_模块四：氨纶橡筋_弹性纤维_EP1581159B1_Method_for_producing_diaper_pants_(含弹性片材.pdf.md`
- [[EP2413866B1 Disposable Wearing Article (Unicharm)]] —— `RAW/ima_sync/个人知识库/WKB/Areas/IP/19_模块四：氨纶橡筋_弹性纤维_EP2413866B1_Disposable_wearing_article_(弹性部件).pdf.md`
- [[US2022-0339044A1 Pant-Type Absorbent Article with Waist Guard (P&G)]] —— `RAW/ima_sync/个人知识库/WKB/Areas/IP/四-2_Pant-type_absorbent_article_with_waist_guard.pdf.md`

---
type: source
title: Co-Development Tooling Design Review — Kirigami Pattern, Pin-Hole Module & Carbide Guidance（合作开发新模具设计）
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/合作开发新模具设计.md
original_link: ""
date_published: "[待验证]（ASR 未标注会议日期；为一次供应商现场访问结束时的收尾会，议题与 [[Precision Rotary Die & Module Supplier Review — Stretch Cutting, SAP Dosing & Layer Config（公司介绍与业务交流）]]、[[Pin-Hole Module, Targeted Fluff Distribution & Elastic Recovery Process Review（新材料开发与弹性恢复工艺探讨）]] 高度连续，疑为同一家精密旋转模切/模块供应商）"
date_processed: 2026-09-29
credibility: 内部一手（现场访问收尾会 ASR 转写，中英夹杂、时间戳乱序、转写质量差）
knowledge_update_status: done
key_claims:
  - 会中收敛出**三项 follow-up**：① **花型（pattern）设计**；② **hole cutter [待验证]** 提案；③ **pinhole（针孔）模块的共同开发**
  - **花型路线**：现场已看到 **3 种现成花型**；本方请供应商**把花型图纸发过来**，本方在此基础上挑选或直接沿用
  - 本方**明确不复制** 延江（Yanjan）/ Kimberly-Clark 的 "smile" 花型，要另找花型 [待验证]
  - **材质路线**：**高速钢（high speed steel）容易做出任意花型** → 用于**打样/原型**；**硬质合金（Thompson carbide / tungsten carbide）不容易做花型**，需**规避刚性角度与刚性边（rigid angles / rigid edges）**
  - 本方据此要求供应商给出**指引**：基于其理论，**哪些花型在硬质合金上做不出来**；以便**一开始就用高速钢把这些花型排除掉**
  - **Kirigami（kiga）**：供应商提供**两次拉伸（stretch one / stretch two）与拉伸模块**，本方要求其**完成完整设计**
  - **共同开发原则（会中达成）**：本方**只承担一定比例的模具/工装费用，不是 100%**（因为是共同开发）；条件是**该模块不得售予他人** —— 供应商当场表示接受
  - 目标应用材料：**liner（面层）与 panel**，形态考虑 **inline（在线）**，也可能做到 panel
  - 本方索要的**三项尺寸指引**：**最大孔径 / 最小孔径 / 孔—孔间距（hole-to-hole spacing，多近会闭合）** —— 未获答复
  - 本方追问**异形孔（非圆孔）**能否制造 —— **未获答复**；供应商被要求**给出两套技术方案**
pages_linked:
  - Rotary Die Tooling Material Route（旋转模切刀具材质路线：高速钢 vs 硬质合金）
  - Kirigami Apertured Nonwoven（切割拉伸开孔工艺）
  - Core Channel Pattern（芯体通道花型设计）
  - 延江（Yanjan）
  - Kimberly-Clark（金佰利）
---

# Co-Development Tooling Design Review — Kirigami Pattern, Pin-Hole Module & Carbide Guidance（合作开发新模具设计）

> ASR 转写讹字说明：本稿为**供应商现场访问结束时的收尾会**自动转写，**中英夹杂、时间戳乱序（00:00 段落与 00:09 段落交错）、转写质量差**。已识别的还原与存疑：
> - **「constant carbide / tompson car / carbon carbide」** = **硬质合金（tungsten carbide）**；疑与刀具品牌 **Thompson** 相关 [待验证]
> - **「high speed steel」** = **高速钢**；「rigid angle / rigid edges」= **刚性角度 / 刚性边**
> - **「kiga / k process / the d for the kiga」** = **Kirigami（切割 + 拉伸开孔工艺）**；「stretch one / stretch two / stretch modules」= **一级拉伸 / 二级拉伸 / 拉伸模块**
> - **「pinhole type module」** = **针孔打孔模块**；「hole to hold space」= **孔—孔间距（hole-to-hole spacing）**
> - **「youhan kimbrs smile」** = **延江（Yanjan）/ Kimberly-Clark 的 smile 花型** [待验证]
> - **「the whole culture / the whole cutter」** = **hole cutter（打孔刀/切孔刀具）** [待验证]
> - **「cap buyer」** 所指不明，疑为 **capital / capex buyer（资本性采购）** [待验证]
> - **「shoulder」** 疑为供应商名或人名 [待验证]；「Jerry / Li z / Li XG / Li X」为**人名音转**，一律 **[待验证]**
>
> ⛔ 本页只记录**已决**事项与**待决**问题；讨论中的构想一律归入 `Open issues 待决问题` 或 `Background 背景`。

## Attendees / Date 参会与日期

- Date 日期：**[待验证]** —— 转写未标注；为**访问结束时的收尾会**（会末出现"叫一辆大出租车、四人返回"与"回去后再开 follow-up call"）
- 场景：本方访问模具/模块供应商，收尾时逐条确认 follow-up
- 供应商方：模具/模块供应商技术与业务代表（**未具名**）[待验证]
- 本方：主讲人（"myself"）、**Jerry**、**Li Z**、**Li XG / Li X**（均为音转）[待验证]
- ⚠️ 除会中明确点到的音转名外，**不做任何实名指派**

## Key decisions 决策要点

1. **花型（pattern）取用方式确定**：现场已看到 **3 种现成花型**，本方请供应商**把花型图纸发过来**，本方**直接挑选沿用**（若对这 3 种不满意，才另做新花型设计）。
2. **不复制竞品花型**：本方明确表示**不想照抄延江 / Kimberly-Clark 的 smile 花型**，要找**其他花型** [待验证]。
3. **打样材质定为高速钢**：**高速钢"做任何花型都容易"** → 先做**原型（prototype）**；**原型确认后再转到硬质合金（Thompson carbide）** 做量产刀具。
4. **硬质合金的花型约束已被明确提出（作为设计输入）**：硬质合金**不容易做花型**，需要**规避某些角度与刚性边**；本方要求供应商给出**"哪些做不了"的指引**，以便**在高速钢阶段就把这些花型排除**。
5. **三项 follow-up 在会中逐条确认**（会末以 "number one / number two / number three" 收口，其中 number two 被评价为 "good news"）：
   - ① **花型设计**（发图纸、给硬质合金可行性指引）；
   - ② **hole cutter [待验证] 提案**（走邮件给 Li XG，抄送 Jerry 与主讲人，并引入本方采购）；
   - ③ **pinhole 模块共同开发**。
6. **共同开发（co-development）的原则达成**：本方**愿意承担一定比例的模具/工装费用，但不是 100%**（理由：这是共同开发）；对应条件是**该模块不得售予他人**。供应商当场回应同意 [待验证]。
7. **Kirigami 拉伸模块由供应商完成完整设计**：供应商已提供**一级/二级拉伸与拉伸模块**，本方要求其**把完整设计补齐**。
8. **目标应用材料明确**：**liner（面层）与 panel** —— 本方会**提供这两种材料**供试；形态上考虑 **inline（在线）**，panel 也在考虑范围内。
9. **供应商需提供两套技术方案**：会中就"上面一种 / 下面一种"要求供应商**给出两套不同的技术方案** [待验证]。

## Open issues 待决问题

1. **硬质合金的花型禁区清单（未获答复）**：本方两次追问"基于你们的经验/理论，**哪些花型在硬质合金上做不出来**"（例如要避开哪些角度、哪些刚性边）——**会中未给出**。
2. **孔径与间距的三项指引（未获答复）**：**最大孔径 / 最小孔径 / 孔—孔间距**（多近会导致孔"闭合"）——本方明确说"我需要这三项指引才能开始设计"，**未获答复**。
3. **异形孔（非圆孔）可制造性（未获答复）**：本方追问"如果孔是这种形状 / 那种形状（**不是圆孔**），你们能不能做？请给出**限制条件的提案**"——**未获答复**。
4. **最终花型未选定**：本方表示**回去后**由 **Li XG、Jerry 与主讲人**共同决定要哪个花型，并把材料寄去试 —— 结论**尚未形成**。
5. **共同开发的费用分摊比例未定**：本方只表明"**某个百分比、不是 100%**"，**具体比例未谈**（属商务，见 manual_review）。
6. **新模块的建造成本未谈**：本方提到"如果是合作开发，可以看**做一个新模块要花多少钱**"，**未获报价**。
7. **inline 还是 panel 未定**：本方说"我们在考虑 inline，也可能做 panel"，**路线未定**。
8. **hole cutter 提案的商务路径待落**：② 项需把提案**发邮件给 Li XG** 并**抄送 Jerry 与主讲人**，同时**引入本方采购**；邮件是否已发出**未获确认**。
9. **Kirigami 完整设计的交付与 follow-up call 排期未定**：本方说"回去后我们会再开一次电话会"，**时间未定**。
10. **"shoulder"/"cap buyer"/"the whole culture" 三处术语含义不明** [待验证]。

## Action items 行动项

| Task 任务 | Owner 负责人 | Due 截止 | Status 状态 |
| --- | --- | --- | --- |
| 发送已看到的 3 种花型图纸 | 供应商（ASR 未指名） | 会后 | Open |
| 给出硬质合金（Thompson carbide）花型可行性指引：哪些角度/刚性边不能做 | 供应商（ASR 未指名） | 后续 | Open |
| 给出三项尺寸指引：最大孔径 / 最小孔径 / 孔—孔间距 | 供应商（ASR 未指名） | 后续 | Open |
| 回复异形孔（非圆孔）的可制造性与限制条件 | 供应商（ASR 未指名） | 后续 | Open |
| 提供**两套**技术方案 | 供应商（ASR 未指名） | [待验证] | Open |
| 完成 Kirigami 一级/二级拉伸与拉伸模块的完整设计 | 供应商（ASR 未指名） | 回国后电话会前 | Open |
| 本方确定最终花型并把 liner / panel 材料寄出试做 | 本方：Jerry、Li XG、主讲人（均为音转）[待验证] | 回国后 | Open |
| hole cutter [待验证] 提案发邮件给 Li XG，抄送 Jerry 与主讲人 | 供应商（ASR 未指名） | [待验证] | Open |
| 引入本方采购（cap buyer [待验证]）参与 hole cutter 提案 | 本方（ASR 未指名） | [待验证] | Open |
| Pinhole 模块共同开发：本方发花型设计 → 供应商给出设计提案与费用口径 | 双方（ASR 未指名） | 回国后 | Open |
| 会后召开 follow-up conference call | 双方（ASR 未指名） | 回国后（时间未定） | Open |

## Background 背景

本方访问一家具备**精密旋转模切 / 打孔模块**能力的供应商，收尾时把访问中看到的三条机会收敛为三项 follow-up：现成花型的取用与新花型开发、**hole cutter [待验证]** 提案、**pinhole 模块的共同开发**。核心诉求是**先把"能做/不能做"的边界拿到手**（硬质合金花型禁区、孔径上下限与孔间距、异形孔可行性），再启动设计。

## 提炼的数字与结论 Numbers & takeaways

| Item 项目 | Value 数值 | Note 备注 |
| --- | --- | --- |
| 现成花型数量 | **3 种** | 现场已看到，待发图纸 |
| 打样材质 | **高速钢（high speed steel）** | 任意花型都容易做 |
| 量产材质 | **硬质合金（Thompson carbide）** [待验证] | 不易做花型，须避刚性角/边 |
| Kirigami 拉伸级数 | **两级（stretch one / stretch two）** | 含拉伸模块 |
| 目标应用 | **liner（面层）+ panel** | 本方提供材料；inline 与 panel 均考虑 |
| 孔型现状 | **圆孔** | 异形孔可行性未获答复 |
| 待索指引 | **最大孔径 / 最小孔径 / 孔—孔间距** | 三项均未获答复 |
| 方案数量要求 | **两套技术方案** | [待验证] |
| 共同开发费用原则 | **承担一定比例，非 100%** | 具体比例未谈（商务） |
| 共同开发对价 | **模块不得售予他人** | 供应商当场接受 [待验证] |

> 🔴 **manual_review（2026-09-29）**：本页涉及**模具/工装（tooling）成本、共同开发的费用分摊比例、以及供应商对"独家不售他人"的承诺** —— 按 AGENTS.md §5，**报价与商务条款不得页面化**；此处只保留"按比例分担、非 100%"这一机制性表述与"不售他人"的对价条件，**不记录任何金额**。请回原文核对：
> `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/合作开发新模具设计.md`
> 另：全文为**低质量 ASR**，术语（shoulder / cap buyer / whole culture）与人名（Jerry / Li Z / Li XG）均需回溯录音确认；"Thompson carbide" 是否为刀具品牌 [待验证]。

## Sources 来源

- 原始记录：`RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/合作开发新模具设计.md`（ASR 转写，会议日期 [待验证]）

## 关联页面 Related pages

- [[Rotary Die Tooling Material Route（旋转模切刀具材质路线：高速钢 vs 硬质合金）]]
- [[Kirigami Apertured Nonwoven（切割拉伸开孔工艺）]]
- [[Core Channel Pattern（芯体通道花型设计）]]
- [[Precision Rotary Die & Module Supplier Review — Stretch Cutting, SAP Dosing & Layer Config（公司介绍与业务交流）]]
- [[Pin-Hole Module, Targeted Fluff Distribution & Elastic Recovery Process Review（新材料开发与弹性恢复工艺探讨）]]
- [[延江（Yanjan）]]
- [[Kimberly-Clark（金佰利）]]

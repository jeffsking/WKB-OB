---
type: concept
title: "Cradle Intake Test（Cradle 摄入测试）"
domain: [卫材研发, 测试与验收]
status: growing
updated: 2026-09-29
tags: [Cradle, intake, 吸收时间, 摄入时间, TTM-00148, 注液点, 泵校验, 测试口径]
aliases: ["Cradle 摄入/吸收时间测试", "Cradle Intake（TTM-00148）"]
---

# Cradle Intake Test（Cradle 摄入测试 / Intake Time）

> 一句话定义：把纸尿裤**拉伸固定在 Cradle 试架**上、按 Size 以定量泵注入 37 ℃ 盐水，记录"液体全部渗到表面以下"所需时间（intake / strike-through time）的方法；因其注液量、流速与注液点被后续多份方法继承，本库把它当作**成品吸液速度的母协议**（中文：Cradle 不只是"一个方法"，而是本库成品注液参数的基准表）。

## 机理 / 结构拆解 Mechanism

1. **Cradle 试架的作用是"消除重力与贴合差异"**：产品被拉伸固定、前端面朝测试者、中心对准托架凹槽最底部，折页被捋开立起且不挡吸收芯——目的是让每片产品以相同的几何姿态接受注液。
2. **三个参数在"母协议"中被表格化**：`Flow rate`、`DISP`（60 s）、`Volume`，另加派生的 `Insult Rate`（mL/s），按 NB→XXL 六档给值。
3. **注液点有三套坐标**：Diaper 通用、Pant 男、Pant 女——**同一尺码男女注液点相差 40 mm**（如 NB：男 75 / 女 35 mm），这是穿着解剖差异而非随意设定。
4. **多冲击 + 固定间隔**是 method 的时间骨架：TTM-00148 为 3 次 × 15 min 间隔；KC U Rewet 为 2 次 × 5 min 间隔。
5. **数据有效性被显式约束**：液体落到非吸收部分 / 流出折页落到模具 / 超过 5 min 才流转 → 三种情况下判无效并载明产品失败。这是本库少见的"失败判定"条款。
6. **继承关系**：[[TTM-00623高低压反渗测试.docx]]、[[TTM-00279产品30°滑渗测试.docx]]、[[KC U Rewet测试.docx]] 均写明"注液量/流速/注液点按 Cradle 设置"。

## 关键参数表 Key Parameters

| 参数 | 口径 | 出处 |
|---|---|---|
| 测试液 | 0.1 g 蓝色食品级粉末 → 100 mL 定容；取 4 mL → 1 L 0.9% 盐水 | [[TTM-00148 Cradle测试.doc]]、[[KC U Rewet测试.docx]] |
| 液温 | 37 ℃（水浴） | [[TTM-00148 Cradle测试.doc]] |
| 泵校验窗口 | 流出液重量 目标值 ±3 g | [[TTM-00148 Cradle测试.doc]] |
| 出液口位置 | 距产品水平 10 mm | [[TTM-00148 Cradle测试.doc]] |
| DISP | 60 s（全 Size） | [[TTM-00148 Cradle测试.doc]] |
| Insult Rate | 10 / 12 / 15 mL·s⁻¹（NB / S / M–XXL） | [[TTM-00148 Cradle测试.doc]] |
| Volume | 50 / 60 / 70 / 85 / 100 / 100 mL（NB→XXL） | [[TTM-00148 Cradle测试.doc]] |
| Flow rate | 600 / 720 / 900 / 900 / 900 / 900（原文单位记作 mL，量纲 `[待验证]`） | [[TTM-00148 Cradle测试.doc]] |
| 注液点 · Diaper 通用 | 距产品中心 55 / 65 / 75 / 85 / 90 / 92 mm | [[TTM-00148 Cradle测试.doc]] |
| 注液点 · Pant 男 | 距产品中心 75 / 85 / 95 / 105 / 110 / 112 mm | [[TTM-00148 Cradle测试.doc]] |
| 注液点 · Pant 女 | 距产品中心 35 / 45 / 55 / 65 / 70 / 72 mm | [[TTM-00148 Cradle测试.doc]] |
| 冲击次数 · 间隔 | 3 次 × 15 min | [[TTM-00148 Cradle测试.doc]] |
| 冲击次数 · 间隔（U Rewet 变体） | 2 次 × 5 min（Pause 显示 15' 与正文矛盾，`[待验证]`） | [[KC U Rewet测试.docx]] |
| 数据无效条件 | 落到非吸收部分 / 流出折页到模具 / >5 min 才流转 | [[TTM-00148 Cradle测试.doc]] |

> ⚠️ **禁止无来源参数**：表中每个数字均来自本 block 源摘要页；Flow rate 列的量纲在原文中有歧义（写作 mL 与 DISP(s) 并列），标 `[待验证]`。
> ⚠️ **同类方法差异（2026-09-29）**：同为 Cradle 系，TTM-00148 与 KC U Rewet 的**冲击次数与间隔不同**（3×15 min vs 2×5 min），且 U Rewet 原文内部 Pause 15' 与实测 5 min 冲突——**不可把两者当作同一口径**。

## 相邻概念 Adjacent Concepts

- 下游读数：[[Rewet Test（回渗测试）]]（U Rewet / 高低压反渗均继承本协议）、[[Liquid Diffusion Test（液体扩散测试）]]
- 变体方法：[[Run-off & Leakage Test（滑渗与渗漏测试）]]（30° 滑渗把 Cradle 注液搬到斜面）
- 物质基础：[[SAP性能指标（CRC AUL GBP Vortex）]]（Vortex / AUL 决定 intake 快慢）
- 结构载体：[[ADL（导流层）]]、[[ATB双梳理面层（Dual-Card Topsheet）]]、[[REL增强层]]
- 上位索引：[[芯体测试方法与验收基准（STM）]]
- 对比：[[Rewet Protocols Compared（回渗测试口径对比）]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[TTM-00148 Cradle测试.doc]]、[[KC U Rewet测试.docx]]、[[TTM-00623高低压反渗测试.docx]]、[[TTM-00279产品30°滑渗测试.docx]]）：四份来源相互印证"Cradle 参数表是共同基准"这一结构性事实；同时证实**只有 TTM-00148 自己定义了泵校验与无效数据条款**，各变体只引用参数不引用失效判据——跨方法比较时须补读 TTM-00148。

- **教训一（口径）**：**注液点必须带产品类型与性别**。Diaper / Pant 男 / Pant 女三套坐标差最大 40 mm，混用会直接改变 intake 读数。
- **教训二（口径）**：**间隔时长是方法身份的一部分**。3×15 min 与 2×5 min 测的不是同一件事（前者含"长期未吸收"信息）。
- **待补 `[待验证]`**：Flow rate 列的真实量纲；U Rewet 的 Pause 口径（15' vs 5 min）。


> ✅ 验证（2026-09-29，来源 [[Preemie Diaper Absorption Test Methods & Parameters（早产儿纸尿裤吸收性能测试方法与参数）]]）：Cradle 法在**早产儿规格**上另有一套参数——加液量按体重分档 **3 / 5.5 / 6 / 8 mL**，流速 **1 mL/s × 3 次**（而非常规成人规格），属**低液量低速**口径。同来源另给出 TTM-00623 的压力 **0.02 / 0.4 psi** 与回渗 **0.005 / 0.24 psi**，以及滞留 **104–125 g**。**上述数值均来自单份检索汇总稿，无第二来源交叉印证，标 `[待验证]`。**

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · Closed Cradle 是回渗方案的"代价显示器"）

> 来源：[[Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）]]（K-C 内部项目汇报）。

1. **Open 与 Closed Cradle 会给出相反结论** —— 同一组面层处理量变更（0.65% → 0.3% → 0% Lertisan）：**Open cradle 摄入与 control 相近**，而 **Closed cradle 摄入显著变差**。**只报 open cradle 会漏掉全部代价。**
2. **代价的性质是"竞争宣称敞口"** —— 源文直言：closed cradle 变差「**Likely leaves us open to competitive claims**」。**摄入指标的用途不只是安全裕度，也是宣称防御面。**
3. **这是一个复发失败模式，不是个案** —— **60 gsm CT8 surge（Shalag 3）**相对 **CT5（ATACAMA）**改善了回渗，但**牺牲了 closed cradle 摄入**；源文明确指出这与 **SIROCCO** 的历史教训同构：「found rewet solution at expense of closed cradle intake」。**"回渗解法牺牲 closed cradle 摄入"在本库已出现至少两次（SIROCCO、GRIFFIN/CT8）。**
4. **可迁移的试验设计规则** —— **回渗与摄入必须同批、同 cradle 状态、并列设门槛**；把 closed cradle 摄入留作"后续再看"会让**看似成功的回渗方案在后期翻车**。
5. **对方法页的直接含义** —— 本页所记录的 Cradle 方法，其**失效判据与重复结构（3 次 × 15 min）**是在**同一产品上区分 open/closed 状态**的唯一载体；**在报告 Cradle 摄入时必须显式标注 open / closed**，否则数值不可比。

> ✅ 验证（2026-09-29）：本节为**追加**，**未修正上方任何既有结论**（含仍维持 `[待验证]` 的 Flow rate 量纲问题）。
> 🔴 **manual_review（2026-09-29）**：来源为 **K-C 内部项目汇报**（含内部项目代号与内部试样结果）；**不落具体 g/s 数值**（原图已退化为图注文本）。

## 来源 Sources

- [[Depend Ultra-Low Rewet Update 2025-03-26（Raegan Informal · 面层处理与 ActivTech Hybrid 芯体）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.03.26 - Raegan Informal.pptx.md`（2026-09-29 追加）
- [[TTM-00148 Cradle测试.doc]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/TTM-00148 Cradle测试.doc.md`
- [[KC U Rewet测试.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/KC U Rewet测试.docx.md`
- [[TTM-00623高低压反渗测试.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/TTM-00623高低压反渗测试.docx.md`
- [[TTM-00279产品30°滑渗测试.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/TTM-00279产品30°滑渗测试.docx.md`
- [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/STM-00034 FIFE/BCC成品STM-南京南厂 1.pdf.md`
- [[Finished Product Testing Method Summary（成品测试方法汇总表）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/Finished Product Testing Method Summary.xlsx.md`

> ✅ 验证（2026-09-29，来源上述两份）：本页原「待补」的 Flow rate 量纲问题仍未在原文中明确（表头写 `Flow rate (mL)` 但 DISP = 60 s、Insult Rate 单位为 mL/s，二者相乘得 mL）——**维持 `[待验证]`**。可补：Cradle 的**失效判据**（液体滴到非吸收区 / 流出折页到模具 / 超过 5 min 才流走，均判无效并记作产品失败）、**泵校验**（流出重量须在目标值 ± 3 g 内）、**出液口距产品水平 10 mm**、**间隔 15 min × 3 次**。成品总表另列 **TTM-00617-4 Cut Cradle（Free Fluid）** 为独立变体。
- [[Preemie Diaper Absorption Test Methods & Parameters（早产儿纸尿裤吸收性能测试方法与参数）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/早产儿测试方法.docx.md`

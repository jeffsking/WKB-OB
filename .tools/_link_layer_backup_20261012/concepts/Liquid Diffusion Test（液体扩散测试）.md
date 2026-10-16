---
type: concept
title: "Liquid Diffusion Test（液体扩散测试）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-29
tags: [扩散, spreading, MD分布, STM-1002, U型扩散, 平面扩散, 测试口径]
aliases: ["液体扩散长度测试", "平面扩散 / U 型扩散"]
---

# Liquid Diffusion Test（液体扩散测试 / Spreading）

> 一句话定义：测量液体进入产品后**在平面方向上铺展多远**的方法族总称。本库有两类实现：**仪器化 U 型扩散**（[[STM-1002U型扩散实验.docx]]，中心针注液、软件记录）与**人工量尺**（[[KC U Rewet测试.docx]]、[[TTM-00148 Cradle测试.doc]] 在注液后量 MD 方向扩散区长度）。

## 机理 / 结构拆解 Mechanism

1. **扩散长度反映的是"液体在面层/ADL/芯体表层的横向输运能力"**，而非容量：液体如果只在注液点就地吸收，扩散长度就短、局部饱和早、回渗与滑渗风险高。
2. **MD / CD 是两个不同读数轴**：本库三份来源都取 **MD 方向**扩散长度；量取时**直尺不得接触产品表面**（[[KC U Rewet测试.docx]] 明示），否则压痕会改变铺展。
3. **两类实现的口径差异**：
   - U 型扩散：仪器化、按 Size 给定注入量、周期 60 s、次数 1 次、软件出报告——**单冲击、标准化程度高**；
   - 人工量尺：在 Cradle / U Rewet 的第二次注液后取数——**双冲击、与回渗同一次实验**。
4. **定位基准都是"产品中心 / 绒毛中心"**：[[STM-1002U型扩散实验.docx]] 要求绒毛中心点对准中心针；[[STM-00433 Pants尺寸.doc]] 同样以产品中心为全部尺寸的基准点。
5. **平面扩散测试需要先解除弹性约束**：两份方法都要求把腿部/折页松紧带剪开（[[STM-1002U型扩散实验.docx]] 每隔 1 英寸剪开但不剪掉、不剪至密合缝或绒毛区；[[TTM-00279产品30°滑渗测试.docx]] 直接剪断）——**剪断方式不同会改变读数**。
6. **与 SAM 分布是同一"芯体内部状态"观察族**：扩散长度是动力学读数，[[SAM Distribution Test（SAM 分布膨胀测试）]] 是终态形态读数。

## 关键参数表 Key Parameters

| 参数 | U 型扩散（STM-1002） | 人工量尺（KC U Rewet / Cradle） | 出处 |
|---|---|---|---|
| 液体 | 0.9% NaCl | 0.9% 盐水 + 蓝粉（37 ℃） | [[STM-1002U型扩散实验.docx]]、[[KC U Rewet测试.docx]] |
| 注入量（NB→XL） | 50 / 65 / 80 / 100 mL | 按 Cradle Volume：50 / 60 / 70 / 85 / 100 mL | [[STM-1002U型扩散实验.docx]]、[[TTM-00148 Cradle测试.doc]] |
| 冲击次数 | 1 次 | 2 次（U Rewet） | [[STM-1002U型扩散实验.docx]]、[[KC U Rewet测试.docx]] |
| 周期 | 60 s | 5 min 间隔 | [[STM-1002U型扩散实验.docx]]、[[KC U Rewet测试.docx]] |
| 剂量标定 | 取 3 次 30 s 出液量平均值输入软件 | 泵校验 ±3 g | [[STM-1002U型扩散实验.docx]]、[[TTM-00148 Cradle测试.doc]] |
| 样品预处理 | 腿部/折页松紧带每隔 1 英寸剪开（不剪掉、不伤芯体） | 同左（Cradle 装样要求捋平、折页立起） | [[STM-1002U型扩散实验.docx]]、[[TTM-00148 Cradle测试.doc]] |
| 定位 | 绒毛中心点对准中心针 | 产品中心位置 | [[STM-1002U型扩散实验.docx]]、[[TTM-00148 Cradle测试.doc]] |
| 读数轴 | 软件记录（扩散 + 渗透） | MD 方向扩散区长度（mm） | [[STM-1002U型扩散实验.docx]]、[[KC U Rewet测试.docx]] |
| 量取约束 | 由仪器固定 | 直尺不得接触产品表面 | [[KC U Rewet测试.docx]] |
| 样品称重精度 | 0.01 g | — | [[STM-1002U型扩散实验.docx]] |

> ⚠️ **禁止无来源参数**：表中数字均来自本 block 源摘要页。**U 型扩散的注入量与 Cradle 的 Volume 分档数值不同（65/80 vs 60/70）**，标为两套口径，不可互推。
> ⚠️ **同类方法差异（2026-09-29）**：U 型扩散为**单冲击 + 仪器记录**，人工量尺为**双冲击 + 人工量尺**；两者数值不可直接比较。

## 相邻概念 Adjacent Concepts

- 上游指标：[[Cradle Intake Test（Cradle 摄入测试）]]（摄入时间决定扩散起点）
- 终态形态：[[SAM Distribution Test（SAM 分布膨胀测试）]]、[[分区密度设计]]
- 结构载体：[[ADL（导流层）]]、[[三叶形截面纤维（Trilobal Fibre）]]、[[MD Liquid Distribution]]、[[毛细梯度设计]]
- 互补指标：[[Rewet Test（回渗测试）]]、[[Run-off & Leakage Test（滑渗与渗漏测试）]]
- 基准同源：[[STM-00433 Pants尺寸.doc]]（以产品中心为基准的几何量测）
- 上位索引：[[芯体测试方法与验收基准（STM）]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[STM-1002U型扩散实验.docx]]、[[KC U Rewet测试.docx]]、[[TTM-00148 Cradle测试.doc]]）：三份来源在"扩散越长越好、按 MD 取值、需先解除弹性约束"三点上一致；但**注入量与冲击次数三份三样**，证实扩散读数同样必须连口径引用。

- **教训一（口径）**：**扩散长度必须带轴向（MD/CD）与冲击次数**。同一产品 1 次冲击与 2 次冲击的 MD 扩散长度不同。
- **教训二（操作）**：**量尺不得接触产品表面**。这是本库唯一被显式写出的量取禁忌。
- **待补 `[待验证]`**：U 型扩散的扩散长度门槛（[[芯体测试方法与验收基准（STM）]] 中的 +15%/+30% 分属另一口径，非本 block 来源）；两类实现的换算关系。

## 来源 Sources

- [[STM-1002U型扩散实验.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-1002U型扩散实验.docx.md`
- [[STM-1001平面扩散实验.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-1001平面扩散实验.docx.md`（2026-09-29 追加）

> ✅ 验证（2026-09-29，来源 [[STM-1001平面扩散实验.docx]]）：**STM-1001（平面扩散，NJ，第 1 版 2021-08-24）与 STM-1002（U 型扩散）口径完全一致**——0.9% NaCl、注入量 NB 50 / S 65 / M 80 / L&XL 100 mL、周期 60 s、次数 1 次、30 s 出液量 ×3 取平均标定、松紧带每隔 1 英寸剪开不剪掉、绒毛中心对准中心针。原页结论未被修正；两份 SOP 为并列姊妹方法，**不合并**，引用时须注方法号。
- [[KC U Rewet测试.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/KC U Rewet测试.docx.md`
- [[TTM-00148 Cradle测试.doc]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/TTM-00148 Cradle测试.doc.md`
- [[TTM-00279产品30°滑渗测试.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/TTM-00279产品30°滑渗测试.docx.md`

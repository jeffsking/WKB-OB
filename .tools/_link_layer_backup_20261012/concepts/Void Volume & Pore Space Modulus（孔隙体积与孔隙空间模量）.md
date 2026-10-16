---
type: concept
title: "Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）"
domain: [卫材研发, SAP与流体]
status: growing
updated: 2026-09-29
tags: [孔隙结构, 厚度, 压缩, 建模, STM-00429, TTM-00038]
---

# Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）

> 一句话定义：**孔隙体积（Void Volume, VV）**是材料中含空气的那部分体积（总体积 − 固体体积 − 已占液体体积），**孔隙空间模量（Pore Space Modulus, PSM）**是压缩曲线反演出的孔隙本构参数；两者共同回答「芯体吸液后还剩多少空间能让后续液体通过」。

## Definition 定义

两条互补的表征路线：

1. **VV 路线（STM-00429）**：在 **0.05 psi** 极低压下测干/湿厚度，结合各组分密度反算孔隙体积，扫描一系列饱和度得到 VV–饱和度曲线。回答「**还剩多少空间**」。
2. **PSM 路线（TTM-00038）**：在 **10–20 kPa** 量级做压缩-回弹循环，用指数核柔量分布反卷积（Cda.exe）反演出调和平均孔隙空间模量 **hpmsm**，供 AFEA 吸收/力学建模使用。回答「**这个空间有多软/多硬**」。

两者的物理接口是**固相密度**：VV 计算需要各组分密度（含已吸收液体的平均密度），PSM 反演同样需要输入固相密度。

## 机理 / 结构拆解 Mechanism

1. **VV 不是松厚度**：VV = 总体积 − 液体体积 − 固体体积。芯体吸液后厚度增加，但增量里既有「液体进入孔隙」也有「SAP 溶胀挤占孔隙」，只有扣除后才是真实可通行空间。
2. **高饱和下 VV 崩塌**：随饱和度上升，SAP 持续溶胀，孔隙被挤占，VV 先持平后骤降——这是**薄芯体高载设计的机理约束**。
3. **PSM 是分布而非单值**：压缩曲线经反卷积得到柔量（compliance）分布，hpmsm 是其调和平均；`L(inf-stress) + delta-L` 给出**零载荷厚度**，是建模必需输入。
4. **两条路线的压力尺度相差约两个数量级**：VV 在 0.05 psi（≈ 0.34 kPa）测「自由态松厚」，PSM 在 10–20 kPa 测「受压态响应」，**读数不可互换**。

## 关键参数表 Key Parameters

| 参数 Parameter | 典型值 / 范围 Value | 口径 Condition | 出处 Source |
|---|---|---|---|
| VV 测试压力 | 0.05 psi | 干态与湿态均在此压力下读厚度 | [[STM-00429 Void Volume as a Function of Saturation（方法正文）]] |
| VV 试样直径 | 76 mm（3 in）默认；模板页为 60.3 mm（2.375 in）；示例用 76 mm | 每 code 18 片 = 1 套 | 同上 + [[STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）]] |
| VV 培养皿 | 80–84 mm（正文）；65 mm（模板说明页） | 皿厚须逐只测 | 同上 |
| VV 等待时间 | ≥ 20 min，≤ 21 min；加液/读数间隔 60 ± 5 s | 加液量精度 ± 0.2 g | [[STM-00429 Void Volume as a Function of Saturation（方法正文）]] |
| VV 加载梯度 | 常规 SAM/绒毛芯 2.5/5/7.5/10/15/20 g/g；无绒毛芯 5/10/15/20/25/30 g/g | 申请方可改 | 同上 |
| 组分密度 | SAM 1.5；Pulp 1.5；PE/PET 双组分 1.15；PE/PP 双组分 0.95；PP 0.93；吸入层 1.2 g/cc | 模板默认值 | [[STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）]] |
| 盐水口径 | 0.9 ± 0.005%（w/w）；自配后静置 ≥ 4 h | 压缩法可用 0.9–2.0%（曾至 20%） | [[STM-00429 Void Volume as a Function of Saturation（方法正文）]]、[[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] |
| 压缩横梁速度 | 1 cm/min（典型） | 申请方指定 | [[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] |
| 最大压缩应力 | 10 ~ 20 kPa（典型）；PSM 反演应力范围近零 ~ 10 kPa | 申请方指定 | 同上 |
| 压缩试样 / 压板 | 试样 φ1.88 in（1 7/8″）；上压板 φ3.5 in、下压板 φ6.0 in | 湿态另用测试杯（OD 6.00 in / ID 5.50 in / 杯深 1.00 in，平面度 < 0.005 in） | 同上 |
| 压缩标距 | 湿态 3 cm；干态 1.5 cm | 3 次压缩-回弹循环 | 同上 |
| PSM 输出 | `hpmsm.dat`：第 1 列压力 kPa、第 2 列 hpmsm | Setup：Elements 1000、Smoothing 0.001、First Order | 同上 |

> ⚠️ **禁止无来源参数**：表中每个数字均来自上列源摘要页。实测 VV 曲线（Little Movers Control，干态 5.3–6.9 cm³/g；20 g/g 时湿态降至 0.58–0.96 cm³/g）**仅来自模板内嵌单一示例**，无第二来源交叉印证 `[待验证]`。

## 相邻概念 Related Concepts

- 上位 / 相关：[[芯体测试方法与验收基准（STM）]]、[[Fluff-Free 4th-Gen Absorbent Core（无木浆第四代芯体）]]、[[Blizzard Core（Blizzard 芯体结构）]]
- 并列指标：[[SAP性能指标（CRC AUL GBP Vortex）]]、[[SAM Testing Methods（超级吸水材料测试方法）]]
- 机理相关：[[SAP（高吸水树脂）]]、[[尿液模拟液（Urine Analog）]]
- 对比：[[Void Volume 与压缩模量两条孔隙表征路线对比]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[STM-00429 Void Volume as a Function of Saturation（方法正文）]]、[[STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）]]、[[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]]）：三份来源互证「VV 与 PSM 是同一孔隙结构的两种观测，接口是固相密度」；同时暴露**试样规格三处不一致**（正文 76 mm / 模板说明 60.3 mm / 示例 76 mm，培养皿 80–84 mm vs 65 mm）。

- **教训一（口径）**：**VV 数字必须附试样直径与压力**。0.05 psi 与 0.2 PSI（成品厚度）差一个量级，φ60.3 与 φ76 mm 面积差约 60%，混用会让 VV 完全失真。
- **教训二（口径）**：**加载梯度必须按芯体类型选**。无绒毛芯（no-fluff）若照搬常规 2.5–20 g/g，曲线到不了近全饱和区，会误判为「孔隙充足」。
- **教训三（流程）**：**TTM 与 STM 不可混用**。TTM-00038 明言 TTM 属研发方法，不用于来料验收与成品放行；对外报告要走 STM 体系。
- **待补 `[待验证]`**：VV 与 PSM 之间的定量换算式（本批 [[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]] 尚未编译）；本库尚无中国产芯体的 VV 实测数据。

## 来源 Sources

- [[STM-00429 Void Volume as a Function of Saturation（方法正文）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM-00429 VOID VOLUME AS A FUNCTION OF SATURATION.pdf.md`
- [[STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM-00429 Void Volume Template.xlsx.md`
- [[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/TTM-00038 Compression Test for Absorbent .pdf.md`

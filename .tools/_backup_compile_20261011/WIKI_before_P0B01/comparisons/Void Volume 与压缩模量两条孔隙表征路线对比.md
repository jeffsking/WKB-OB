---
type: comparison
title: "Void Volume 与压缩模量两条孔隙表征路线对比"
subjects: ["[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]", "[[芯体测试方法与验收基准（STM）]]"]
dimension: 性能
updated: 2026-09-29
tags: [孔隙结构, STM-00429, TTM-00038, 厚度, 压缩, 建模]
aliases: ["Void Volume vs Pore Space Modulus（两条孔隙表征路线对比）"]
---

# Void Volume vs Pore Space Modulus（两条孔隙表征路线对比）

## 对比维度表 Comparison Matrix

> 必含「成本」与「供应链风险」两列。

| 维度 Dimension | VV 路线（STM-00429） | PSM 路线（TTM-00038） | 依据 Source |
|---|---|---|---|
| 回答的问题 Question | 「还剩多少空间让液体通过」（**容量 / 渗透**） | 「这个空间有多软、受压如何响应」（**本构 / 力学**） | [[STM-00429 Void Volume as a Function of Saturation（方法正文）]]、[[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] |
| 物理量 Quantity | 孔隙体积 VV（cm³/g 或 cm³/cm²） | 调和平均孔隙空间模量 **hpmsm**、零载荷厚度 | 同上 |
| 压力尺度 Pressure scale | **0.05 psi（≈ 0.34 kPa）**，极低压自由态 | **10 ~ 20 kPa**（典型），PSM 反演范围近零 ~ 10 kPa；横梁 1 cm/min | 同上 |
| 试样 Specimen | φ76 mm（3 in）默认、18 片/套；培养皿 80–84 mm；加液后等 20 min | φ1.88 in（1 7/8″）；上压板 φ3.5 in、下压板 φ6.0 in；湿态用测试杯（杯深 1.00 in） | 同上 |
| 加载 / 循环 | 饱和度梯度 2.5/5/7.5/10/15/20 g/g（无绒毛芯 5–30 g/g） | 3 次压缩-回弹循环；标距湿态 3 cm、干态 1.5 cm | 同上 |
| 数据输出 Output | VV–饱和度曲线 + 三阶多项式拟合（R²） | `hpmsm.dat`（压力 kPa / hpmsm 两列）+ 柔量分布图 | 同上 |
| 成熟度 Status | **STM**（Standard Test Method，QA 归口，可对外） | **TTM**（Technical Test Method，明言不用于验收/放行） | [[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] |
| 成本 Cost 成本 | **中**：厚度仪 + 培养皿 + 冲刀，18 片/套 × 20 min 等待，人工加液与读数密集（60 ± 5 s 间隔）；**主要成本是人工时序** | **中**：需 CRE 拉伸试验机 + 计算机采集 + 专用压板与测试杯；**附加成本是 Cda.exe 反演的人工调参**（Upper Edge 需反复试算） | [[STM-00429 Void Volume as a Function of Saturation（方法正文）]]、[[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] |
| 供应链风险 Supply chain risk 供应链风险 | **低**：方法成熟、参数公开于 STM 正文，供应商可复现；风险点是**试样规格在正文/模板/示例三处不一致**（φ76 / φ60.3 / φ76 mm；培养皿 80–84 vs 65 mm），易造成来料比对争议 | **中**：依赖 KC 内部程序 **Cda.exe** 与内部反演经验（Setup 参数、Upper Edge 试算），**供应商与第三方无法复现**；且方法本身声明不做准确度评价 | [[STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）]]、[[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] |
| 适用场景 Where used | 芯体配方筛选、薄芯体高载可行性判断、与供应商沟通容量/渗透指标 | AFEA 吸收与力学建模、为仿真提供本构输入 | 同上 |

> 尾注 Footnote：本表所有数字均来自 [[STM-00429 Void Volume as a Function of Saturation（方法正文）]]、[[STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）]]、[[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] 三份源摘要页。

## 各自适用场景 Where Each Applies

- **VV 路线（STM-00429）**：当问题是「这个芯体在多高载液量下还能继续吸」时用。可直接出曲线与拟合，结果可对外；加载梯度须按芯体类型选（常规 2.5–20 g/g，无绒毛芯 5–30 g/g）。
- **PSM 路线（TTM-00038）**：当问题是「给仿真提供什么本构参数」时用。输出 hpmsm 与零载荷厚度，属建模输入；**不可用于验收与放行**。

## 结论 Conclusion

**VV 看「空间有多少」，PSM 看「空间有多软」，两者压力尺度相差约两个数量级，读数不可互换；唯一的物理接口是固相密度（须取含已吸收液体的平均密度）。** 对外沟通优先用 VV（STM 体系、可复现），建模内部用 PSM（TTM 体系、不可对外）。

## 来源 Sources

- [[STM-00429 Void Volume as a Function of Saturation（方法正文）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM-00429 VOID VOLUME AS A FUNCTION OF SATURATION.pdf.md`
- [[STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM-00429 Void Volume Template.xlsx.md`
- [[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/TTM-00038 Compression Test for Absorbent .pdf.md`

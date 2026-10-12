---
type: source
title: "STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）"
source_type: 标准测试方法（STM 计算模板）
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM-00429 Void Volume Template.xlsx.md
original_link: ""
date_published: 2022-01-25
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "STM-00429 的目标（Objective）：量化材料在不同饱和度（saturation）与 SAP 溶胀程度下的孔隙体积（void volume，VV），厚度统一在 0.05 psi 下测量"
  - "试样口径：φ2-3/8 英寸（2.375 in，面积 28.58 cm²）圆形试样，每个 code 冲切 18 片；65 mm 培养皿（Petri dish）；加液后等待 20 分钟"
  - "组分密度默认值（g/cc）：SAM 1.5、绒毛浆 Pulp 1.5、PE/PET 双组分粘合纤维 1.15、PE/PP 双组分粘合纤维 0.95、聚丙烯 PP 0.93、吸入层材料（Surge/Liner）1.2"
  - "饱和度梯度默认 1.25 / 2.5 / 3.75 / 5 / 7.5 / 10 g/g，每组 3 个培养皿；建议按芯体类型上调：Huggies SAM/绒毛芯 2.5–20 g/g、Pampers（含 100% SAM 芯）2.5–20 g/g、Huggies ActiveTech BLIZZARD 芯 5–30 g/g"
  - "实测示例（Little Movers Control，S20-002071，2019-09-17）：干态 VV 约 5.3–6.9 cm³/g；湿态 VV 在 2.5–10 g/g 区间维持 7.5–9.3 cm³/g，到 15 g/g 骤降至 3.5–4.3、20 g/g 降至 0.58–0.96 cm³/g——高饱和下孔隙被 SAP 溶胀挤占而崩塌"
  - "模板含 Saline（盐水）与 Blood（血）两套数据页，说明同一方法可换液体类型；结果经 LabVantage 导入，需三阶多项式拟合并报 R²"
pages_linked: ["[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]", "[[芯体测试方法与验收基准（STM）]]", "[[Blizzard Core（Blizzard 芯体结构）]]", "[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]", "[[SAM Testing Methods（超级吸水材料测试方法）]]", "[[尿液模拟液（Urine Analog）]]"]
---

# STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）

## 一句话定位

STM-00429 是 KC 用于**量化「芯体在不同吸液饱和度下还剩多少孔隙」**的标准方法与其 LabVantage 数据导入模板；它是把「厚度」这一易测物理量换算成「孔隙结构」这一机理量的桥梁。

## 摘要

方法的 Objective 原文为：*Quantify the void volume (via thickness at 0.05 psi) of a material at various levels of saturation and SAP swelling*（通过在 0.05 psi 下测厚度，量化材料在不同饱和度与 SAP 溶胀程度下的孔隙体积）。核心思路是：芯体吸液后厚度增加，但增量并非全部来自「孔隙保留」——SAP 溶胀会占据原本的孔隙空间；通过测量干/湿厚度并结合各组分密度反算，即可分离出真实孔隙体积。

流程为 10 步：取 65 mm 培养皿 → 每个 code 冲切 **18 片 φ2 3/8 英寸**圆形试样 → 培养皿去皮 → 放试样并记录重量 → 在 **0.05 psi** 下测试样 + 培养皿的干厚度（mm）→ 试样与培养皿一起去皮 → 加入并记录实际液重 → 等待 **20 分钟** → 在 0.05 psi 下测湿厚度 → 输入各组分百分比与密度。模板自动绘出 VV-饱和度曲线，并反算基重与密度。

试样规格有两种口径：模板默认 **φ2.375 in（面积 28.5815 cm²）**，而随附示例（Little Movers Control，Sample ID S20-002071，分析人 W. R. Baumann，2019-09-17）用的是 **φ3 in（面积 45.6037 cm²）**——两者面积相差约 60%，**引用时必须说明试样直径**。

模板含 **Saline Data**（盐水）与 **Blood data1**（血）两页，说明同一方法可切换液体类型研究不同液体下的孔隙行为。

## 提炼的数字与结论

### 方法固定口径（Fixed Conditions）

| 项目 Item | 口径 Condition | 备注 Note |
|---|---|---|
| 厚度测试压力 | **0.05 psi** | 与成品厚度法 0.2 PSI 不同，属极低压，专测松厚度 |
| 试样直径（默认） | 2.375 in（2 3/8″）= 面积 28.5815 cm² | 示例页用 3 in = 45.6037 cm² |
| 试样数量 | 每个 code 18 片 | 6 个饱和度 × 3 重复 |
| 容器 | 65 mm Petri dish（培养皿） | 需先测皿厚并去皮 |
| 平衡时间 | 加液后等待 **20 min** | — |
| 饱和度梯度（默认） | 1.25 / 2.5 / 3.75 / 5 / 7.5 / 10 g/g | 每档 3 皿 |
| 输出量 | VV 干态（cm³/g、cm³/cm²）、VV 湿态、实际饱和度、Web density、基重 | 三阶多项式拟合 + R² |
| 数据系统 | LabVantage，Sample ID 格式 SYY-000000，Data 页单元格不得改动 | 表保护密码 STM-00429 |

### 组分密度默认值（Typical Component Densities）

| 组分 Component | 密度 Density (g/cc) |
|---|---|
| SAM / Superabsorbent | 1.5 |
| Pulp（绒毛浆） | 1.5 |
| PE/PET Bicomponent binder fiber | 1.15 |
| PE/PP Bicomponent binder fiber | 0.95 |
| Polypropylene（聚丙烯） | 0.93 |
| Intake Materials（Surge / Liner） | 1.2 |

> Composition Constant（组分常数）随配比变化：默认页（SAM 0% / Pulp 82% / Binder 18%）为 **0.7361 cc/g**；示例页（SAM 60% / Pulp 40% / Binder 0%）为 **0.6667 cc/g**。

### 按芯体类型的建议加载梯度（Suggested Loadings）

| 芯体类型 Core type | 建议饱和度 Suggested saturation (g/g) |
|---|---|
| Huggies 尿裤 · SAM/绒毛芯 | 2.5, 5, 7.5, 10, 15, 20 |
| Pampers 尿裤 · SAM/绒毛芯 或 100% SAM 芯 | 2.5, 5, 7.5, 10, 15, 20 |
| Huggies 尿裤 · ActiveTech BLIZZARD 芯 | 5, 10, 15, 20, 25, 30 |

> 备选思路：也可按目标克载 0、12.5、25、37.5、50、75、100 g 设计，以覆盖 0 至接近 100% 饱和度区间，此时 g/g 由实际加载反算。

### 实测示例：VV 随饱和度的崩塌（Little Movers Control，φ3 in，2019-09-17）

| 目标饱和度 Saturation (g/g) | 湿态 VV（cm³/g）Wet VV | 干态 VV（cm³/g）Dry VV | 实际饱和度 Actual |
|---|---|---|---|
| 2.5 | 7.86 ~ 9.07 | 5.53 ~ 6.94 | 2.52 ~ 2.54 |
| 5 | 8.40 ~ 9.35 | 5.47 ~ 5.95 | 5.00 ~ 5.03 |
| 7.5 | 8.23 ~ 9.03 | 5.62 ~ 6.81 | 7.51 ~ 7.52 |
| 10 | 7.46 ~ 8.73 | 5.91 ~ 6.58 | 10.01 ~ 10.02 |
| 15 | 3.54 ~ 4.33 | 5.61 ~ 6.39 | 15.00 ~ 15.01 |
| 20 | 0.58 ~ 0.96 | 5.30 ~ 6.60 | 20.02 ~ 20.04 |

> 读法：干态 VV 稳定在 5.3–6.9 cm³/g（材料本身属性）；湿态 VV 在 10 g/g 以内基本持平甚至略升（液体填入孔隙、SAP 尚未充分溶胀），**到 15 g/g 骤降约一半、20 g/g 接近归零**——说明该芯体的孔隙在此加载下被 SAP 溶胀完全挤占。示例三阶多项式拟合 R² = 0.951（VV by Weight vs Saturation Level）。

> ⚠️ **单源数值标注（2026-09-29）**：上述曲线取自模板内嵌的**单一示例**（2019 年、单一 code、单一分析人），未在本批其他资料中出现同类数据，**不可作为普遍规律引用** `[待验证]`。

## 关键论断（key_claims）

- **VV 是通过 0.05 psi 厚度反算的孔隙量，压力口径与成品厚度法（0.2 PSI）完全不同** —— 支撑页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- **组分密度（SAM/Pulp 1.5、PE/PET 1.15、PE/PP 0.95、PP 0.93）是反算 VV 的必要输入** —— 支撑页：[[皮芯复合纤维]]
- **饱和度梯度须按芯体类型选：常规 SAM/绒毛芯 2.5–20 g/g，BLIZZARD 薄芯 5–30 g/g** —— 支撑页：[[Blizzard Core（Blizzard 芯体结构）]]、[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]
- **高饱和下 VV 崩塌是薄芯体设计的机理约束（SAP 溶胀挤占孔隙）** —— 支撑页：[[Fluff-Free 4th-Gen Absorbent Core（无木浆第四代芯体）]]
- **同一方法可切换盐水/血液两种液体** —— 支撑页：[[尿液模拟液（Urine Analog）]]

## 关联页面

- 概念：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]、[[芯体测试方法与验收基准（STM）]]、[[Blizzard Core（Blizzard 芯体结构）]]、[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]、[[SAM Testing Methods（超级吸水材料测试方法）]]、[[尿液模拟液（Urine Analog）]]、[[Fluff-Free 4th-Gen Absorbent Core（无木浆第四代芯体）]]
- 实体：[[Kimberly-Clark（金佰利）]]
- 对比：（本批对比页见 [[Void Volume 与压缩模量两条孔隙表征路线对比]]）

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM-00429 Void Volume Template.xlsx.md`
- 原文链接：（无；KC 内部标准方法模板）
- 同族文档：[[STM-00429 Void Volume as a Function of Saturation（方法正文）]]、[[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]

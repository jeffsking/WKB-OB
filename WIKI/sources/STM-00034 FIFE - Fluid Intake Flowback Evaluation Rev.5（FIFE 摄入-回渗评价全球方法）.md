---
type: source
title: "STM-00034 FIFE - Fluid Intake Flowback Evaluation Rev.5（FIFE 摄入-回渗评价全球方法）"
source_type: 标准测试方法（STM）
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/STM-00034 FIFE/STM-00034.pdf.md
original_link: ""
date_published: 2020-09-28
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "STM-00034 Rev.5（生效日 2020-09-28，Document Owner Peralta, Maximiliano，状态 Aprovado）是 FIFE 法的全球母版，南京南厂 WI-56234 与天津厂册中的 STM-00034 均为其本地化译本"
  - "单位换算锚点：14 ± 1 英寸水柱（inch of water）= 3.4 kPa；南京南厂译本写作 3447 Pa——本库此后引用压力时可据此互换"
  - "回渗（flowback）判定载荷为 0.5 psi（pound-force per square inch，磅力/平方英寸）；SAT CAP 测试仪按 0.5 psi 设计，超过 2.0 psi 有内爆（implode）风险"
  - "加液量按体重区间分档 35 / 50 / 65 / 80 / 100 mL（± 0.5 mL），南京南厂本地化为 Step1–Step6 同样五档，与全球版一一对应"
  - "目标区（target zone）按体重 × 性别三档给值（Unisex 89–146 mm、Male 76–114 mm、Female 121–152 mm，± 6 mm），且明言「International target zone areas may be different」——中国区取 102/114/127/146/146 mm 属国际变体"
  - "吸收时间判据是「圆柱孔区域内面层液体颜色消失即停表」，且明确注明「此时芯体可能仍在吸收」——该方法测的是表观摄入时间而非完全吸收时间"
pages_linked: ["[[Rewet Test（回渗测试）]]", "[[Acquisition Test STM-00060（导流性能测试）]]", "[[Retention Capacity Test（滞留能力测试）]]", "[[尿液模拟液（Urine Analog）]]", "[[芯体测试方法与验收基准（STM）]]", "[[Kimberly-Clark（金佰利）]]"]
---

# STM-00034 FIFE - Fluid Intake Flowback Evaluation Rev.5（FIFE 摄入-回渗评价全球方法）

## 一句话定位

**FIFE（Fluid Intake Flowback Evaluation，液体摄入-回渗评价）** 的 KC 全球标准方法母版（STM-00034，Rev. 5，2020-09-28 生效），定义纸尿裤/拉拉裤/POISE/DEPEND 的吸收时间、溢出量（overflow）与回渗量（flowback）三大成品指标及其全部口径。

## 摘要

方法分两段：先在 **FIFE 板**上完成三次定量注液并计时，再转移到 **SAT CAP（Saturated Capacity，饱和容量）测试仪**上于 14 ± 1 英寸水柱（3.4 kPa）负压下压 2 分钟，用滤纸增重测回渗。

FIFE 板结构为底板 + 上盖板，底板中央有 **75 × 150 mm（3 × 6 inch）凸台**，试样面层（liner side）朝上、目标区对准凸台中央；上盖板有圆柱开口，漏斗垂直插入并居中。底板凸台两侧各放一张预称重溢出滤纸（88 × 300 ± 13 mm），收集从侧面流出的液体。

注液后**当液体接触漏斗壁即开始计时**；漏斗一空立即移开；**当圆柱开口区域内面层上的液体「不可见」时立即停表**，精度 0.01 秒。原文明确注记：停表时芯体可能仍在吸收（Note 24），即该指标是**表观摄入时间**。每次注液后等 60 秒（Note 25：不得超过 65 秒）再进行下一次。

回渗段：第二次注液后把试样水平转移到 SAT CAP，面层朝上居中，放 1 张 238 × 300 ± 13 mm 或 2 张 88 × 300 ± 13 mm 预称重回渗滤纸（距前端绒毛边缘约 6 mm），盖乳胶膜抽真空至 14 ± 1 inH₂O（3.4 kPa）维持 2 分钟；回渗量 = 湿滤纸重 − 干滤纸重。

安全条款是本方法的重要边界：SAT CAP 测试仪**专为 0.5 psi 载荷设计，超过 2.0 psi 可能内爆**（10.5 条）；乳胶膜每次使用前须检查孔洞与撕裂。

## 提炼的数字与结论

### 压力与单位换算（Pressure & Unit Conversion）

| 表述 Expression | 数值 Value | 出处 / 备注 Note |
|---|---|---|
| 目标真空 Target vacuum | 14 ± 1 inch of water | 全球版 §3.2 |
| 换算值 Converted | 3.4 kPa | 全球版 §3.2.2.1 |
| 南京南厂译本换算 | 3447 Pa | 南京南厂 WI-56234 §STM-00034 |
| 回渗判定载荷 Flowback loading | 0.5 psi | §1.4.2 定义 |
| 设备上限 Equipment limit | > 2.0 psi 有内爆风险 | §10.5 |
| 厚度法压力（供对照） | 0.2 PSI | 见 [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] |

### 加液量分档（Insult Amount by Weight Range）

| 体重 Weight | < 4.5 kg | < 6.4 kg | 5.4–8.2 kg | 7.3–12.7 kg | 10.0 ~ > 15.9 kg |
|---|---|---|---|---|---|
| Insult amount | 35 mL | 50 mL | 65 mL | 80 mL | 100 mL |

> 每项 ± 0.5 mL。南京南厂本地化写作 **Step1 35 / Step2 50 / Step3 65 / Step4 80 / Step5-6 100 mL（± 0.5 mL）**，与全球版一一对应。研究用途可改液量，但必须记录。

### 目标区位置（Target Zone，距产品前端绒毛边缘，± 6 mm）

| 体重区间 Weight | < 2.7 kg | < 4.5 kg | < 6.4 kg | 5.4–8.2 kg | 7.3–12.7 kg | > 12.2 kg | > 15.9 kg |
|---|---|---|---|---|---|---|---|
| Unisex（mm） | 89 | 102 | 114 | 127 | 146 | 146 | 146 |
| Male（mm） | N/A | 76 | 89 | 102 | 114 | 114 | 114 |
| Female（mm） | N/A | 121 | 133 | 146 | 152 | 152 | 152 |

> 全球版 Note 18 明言：**国际区目标区可能与表 2 不同**。南京南厂取 Unisex 102/114/127/146/146 mm（ST1–ST5），属国际变体——**引用时必须注明是全球版还是中国版**。

### 其他关键口径

| 项目 Item | 口径 Condition |
|---|---|
| 试样制备 | 所有弹性材料每隔约 13 mm（0.5 in）剪开使之平铺；不得剪到密封线或绒毛区 |
| 凸台尺寸 | 75 × 150 mm（3 × 6 in） |
| 溢出滤纸 | 底板两侧各 1 张，88 × 300 ± 13 mm |
| 回渗滤纸 | 1 张 238 × 300 ± 13 mm，或 2 张 88 × 300 ± 13 mm（须完全重叠，不可错位） |
| 滤纸放置 | 距前端绒毛边缘约 6 mm（0.25 in） |
| 称重精度 | 0.01 g；吸收时间 0.01 s |
| 注液间隔 Wait time | 60 s（不得超过 65 s） |
| SAT CAP 保压 | 14 ± 1 inH₂O 维持 2 min；legacy 控制器需含升压时间（≤ 30 s），触屏版 10 inH₂O 时开始计时 |
| Drip timer（尿裤） | 1 或 15 min；POISE / Adult Care 为 2 min |
| 染色液 | 粉体染料约 1 g 溶于 1 L 蒸馏水，取约 4 mL 加入 1 L 盐水；液体染料为约 7 mL 溶于 1 L 蒸馏水后取 4 mL |
| 密封液 | 只能用 0.9% 盐水湿润测试仪边缘密封，**不得用自来水或蒸馏水**（南京南厂译本补注） |
| 适用组织 Scope | Global QA；含 China、Beijing Mill、Tianjin Mill、Nanjing North Mill 等 20+ 工厂与 Supplier |

> ⚠️ **单源数值标注（2026-09-29）**：本页压力换算 3.4 kPa 与 3447 Pa 分别来自全球版与南京南厂译本，两处互相印证；但 **0.5 psi 回渗载荷仅见于全球版**，中文译本未出现该表述，如需对外引用建议核对 SAT CAP 设备铭牌 `[待验证]`。

## 关键论断（key_claims）

- **FIFE 是成品吸收三指标（摄入时间 / 溢出 / 回渗）的唯一全球母法** —— 支撑页：[[Rewet Test（回渗测试）]]、[[Acquisition Test STM-00060（导流性能测试）]]
- **14 inH₂O = 3.4 kPa 是本库压力换算的锚点** —— 支撑页：[[Retention Capacity Test（滞留能力测试）]]
- **吸收时间是「表观摄入时间」，停表时芯体可能仍在吸收** —— 支撑页：[[芯体测试方法与验收基准（STM）]]
- **目标区按体重与性别分档，且允许国际变体** —— 支撑页：[[芯体测试方法与验收基准（STM）]]
- **SAT CAP 的 0.5 psi 设计载荷与 2.0 psi 内爆上限是硬性安全边界** —— 支撑页：[[Kimberly-Clark（金佰利）]]

## 关联页面

- 概念：[[Rewet Test（回渗测试）]]、[[Acquisition Test STM-00060（导流性能测试）]]、[[Retention Capacity Test（滞留能力测试）]]、[[尿液模拟液（Urine Analog）]]、[[芯体测试方法与验收基准（STM）]]
- 实体：[[Kimberly-Clark（金佰利）]]
- 对比：[[GB-T 28004.1-2021 与 KC STM 成品吸收性能测试方法对比]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/STM-00034 FIFE/STM-00034.pdf.md`
- 原文链接：（无；KC 内部标准方法，含保密声明）
- 同族文档：[[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]]、[[Quality Finished Product STM - Tianjin Plant（质量成品标准测试方法-TJ）]]

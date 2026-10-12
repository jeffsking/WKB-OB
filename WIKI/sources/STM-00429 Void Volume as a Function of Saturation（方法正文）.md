---
type: source
title: "STM-00429 Void Volume as a Function of Saturation（方法正文）"
source_type: 标准测试方法（STM）
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM-00429 VOID VOLUME AS A FUNCTION OF SATURATION.pdf.md
original_link: ""
date_published: 2022-02-04
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "STM-00429 Rev.2（生效日 2022-02-04，Document Owner Powers, Stephen，Status Approved）给出孔隙体积（Void Volume, VV）的正式定义：VV = 材料总体积 − 固体体积（Total material volume − Volume of solids）"
  - "饱和度（saturation level）在本法中定义为「试样含液量 / 干试样质量」，单位 g/g"
  - "默认试样直径 76 mm（3 英寸）、每 code 冲切 18 片为一套；培养皿直径须为 80–84 mm，超出此范围结果可能失真"
  - "厚度一律在 0.05 psi 下读，精度 0.01 mm；加液后等待至少 20 min、不超过 21 min；相邻试样加液与读数均须保持 60 ± 5 s 间隔；加液量精度 ± 0.2 g"
  - "盐水口径为 0.9 ± 0.005%（w/w）；自配盐水混合后须静置至少 4 h（或过夜）方可使用（引 TL 5076）；商品化盐水保质期更长（引 TL 976）"
  - "加载梯度：常规 SAM/绒毛芯 2.5、5、7.5、10、15、20 g/g；无绒毛芯（no-fluff core）需 5、10、15、20、25、30 g/g"
  - "取样位置可指定为「TTM-00148 的 Unisex 注液点」；对 Pampers / Luvs 等无绒毛竞品做预测建模时，明言「不要去除吸入层材料，并按 Fluff Percent 报告」"
pages_linked: ["[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]", "[[芯体测试方法与验收基准（STM）]]", "[[SAM Testing Methods（超级吸水材料测试方法）]]", "[[尿液模拟液（Urine Analog）]]", "[[Fluff-Free 4th-Gen Absorbent Core（无木浆第四代芯体）]]", "[[Cradle Intake Test（Cradle 摄入测试）]]", "[[Kimberly-Clark（金佰利）]]"]
---

# STM-00429 Void Volume as a Function of Saturation（方法正文）

## 一句话定位

**STM-00429 Rev.2** 是孔隙体积法的方法正文（母版），给出 VV 的正式定义、全部计算公式、试样/仪器口径与液体口径；上一页的计算模板是它的执行载体。

## 摘要

方法目的（1.1–1.2）：测定试样在给定饱和度下的孔隙体积（void volume）。**可用孔隙体积（available void volume）**即材料中可被液体侵入占据的空间，其大小直接估计材料作为**吸入层（intake material）**的表现，以及该材料能接受多少液体冲击（fluid insult）。正文特别强调：该信息是**按容量（capacity）与渗透性（permeability）要求设计吸收产品所必需的**。

定义部分给出四条关键界定：
- **Intake Material（吸入层材料）**：负责接受液体的材料，可为纺熔面层（spunmelt body side liner）、梳理粘合surge 材料、芯体包裹层（wrapsheet）或组合。若试样含吸入层，申请方须提供其百分比与组分密度以提高 VV 计算精度。
- **Superabsorbent（高吸水材料）**：颗粒或纤维状，吸水能力通常在 **15 g/g 以上**。
- **Pulp（绒毛浆）**：通常与 SAM 混合成芯；常为木浆绒毛浆，亦可为粘胶、棉或其他吸收纤维。
- **Binder（粘合剂）**：气流成网芯体中通常不存在；干法造纸（airlaid）材料中是赋予干湿强度的**双组分纤维**；在近 100% SAM 芯中则是把 SAM 粘住的胶。

流程：先测每个培养皿厚度（0.01 mm）→ 称试样干重（0.01 g）→ 测皿 + 干试样厚度 → 皿 + 试样一起去皮后按表算定量加液（± 0.2 g），**加液须均匀铺满试样表面**，相邻试样间隔 60 ± 5 s → 计时至少 20 min（不超过 21 min）→ 按同一顺序复测皿 + 湿试样厚度，读数间隔同样 60 ± 5 s。全部读数在 **0.05 psi** 下进行。

结果段给出完整公式族（Table 1），核心是**组分常数 c**（Composition Constant）：

c = (1/100) × ( %SAM/ρ_SAM + %Pulp/ρ_Pulp + %Binder/ρ_Binder + %IntakeMatls/ρ_Intake )

干态 VV（按重量）= (A × t_dry) / 干重 − c；湿态 VV（按重量）= [ (A × t_wet) − 加液体积 ] / 干重 − c。即**先从总容积中扣除液体占据的体积，再扣除固体体积，余者即孔隙**。

正文还写入两条建模导向的注记（Note 6/7）：做**预测渗漏建模（predictive leakage modeling）**时建议保留吸入层材料；对 Pampers、Luvs 这类**无绒毛芯（no fluff core）**竞品做预测建模时，须指示「不得去除吸入层材料，并以 Fluff Percent 报告」。另 Note 13 指定：预测建模时取样位置为 **TTM-00148 的 Unisex 注液点**。

## 提炼的数字与结论

### 口径清单（Test Conditions）

| 项目 Item | 口径 Condition | 备注 Note |
|---|---|---|
| 试样直径 Specimen diameter | **76 mm（3 in）为默认值** | 若不同须在表中填明；直径过小且 x-y 方向溶胀大时计算精度下降 |
| 试样数量 | 每 code 18 片 = 1 套 | — |
| 培养皿 Petri dish | 直径 **80–84 mm**，须事先量测 | 超出范围结果可能失真 |
| 厚度压力 | **0.05 psi** | 精度 0.01 mm |
| 厚度仪脚踏管路压力 | ≥ 60 psi（4.2 kg/cm²），≤ 65 psi（4.55 kg/cm²） | 与成品厚度法一致 |
| 厚度仪预热 | 10 min | 每次读数前须 RESET 归零，显示 0.00 |
| 加液量精度 | 表算值 **± 0.2 g** | 记录精度 0.01 g |
| 加液间隔 | **60 ± 5 s** | 读数间隔同为 60 ± 5 s |
| 等待时间 | ≥ 20 min，≤ 21 min | — |
| 测试液 | 0.9 ± 0.005%（w/w）盐水 | 自配后静置 ≥ 4 h（或过夜）再用；引 TL 5076 / TL 976 |
| 测试环境 |  ambient（常温常湿）条件下量测 | Note 22 |
| 加载梯度 | 常规 SAM/绒毛芯 2.5/5/7.5/10/15/20 g/g；无绒毛芯 5/10/15/20/25/30 g/g | Note 15 |
| 组分百分比 | 申请方提供，且**必须合计 100%** | 某组分为 0% 时仍须填密度，否则除零错误 |

### 计算公式（Table 1，原文公式）

| 量 Quantity | 公式 Formula |
|---|---|
| 组分常数 c（cc/g） | c = (1/100) × ( %SAM/ρ_SAM + %Pulp/ρ_Pulp + %Binder/ρ_Binder + %Intake/ρ_Intake ) |
| 试样面积 A（cm²） | A = (1 cm/10 mm)² × π × (SpecimenDiameter, mm / 4)² |
| 基重 BW（gsm） | BW = DryWeight, g / A × (100 cm / 1 m)² |
| 干厚度 t_dry（mm） | t_dry = 皿+干试样厚度 − 皿厚 |
| 湿厚度 t_wet（mm） | t_wet = 皿+湿试样厚度 − 皿厚 |
| 干态 web 密度 ρ_dry | ρ_dry = SpecimenDryWeight / (t_dry × A × (1 cm/10 mm)) |
| 湿态 web 密度 ρ_wet | ρ_wet = SpecimenWetWeight / (t_wet × A × (1 cm/10 mm)) |
| 干态 VV（cm³/g） | VV_wt,dry = [ A × t_dry × (1 cm/10 mm) / SpecimenDryWt ] − c |
| 干态 VV（cm³/cm²） | VV_area,dry = VV_wt,dry × SpecimenDryWt / A |
| 湿态 VV（cm³/g） | VV_wt = [ (A × t_wet × (1 cm/10 mm)) − FluidAdded, cc ] / SpecimenDryWt − c |
| 湿态 VV（cm³/cm²） | VV_area = [ (A × t_wet × (1 cm/10 mm)) − FluidAdded, cc − (c × SpecimenDryWt) ] / A |

> ⚠️ **同法异参提示（2026-09-29）**：方法正文默认**试样 φ76 mm（3 in）、培养皿 80–84 mm**；而配套的 [[STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）]] 的 INSTRUCTIONS 页写的是**φ2 3/8 英寸（2.375 in，面积 28.58 cm²）、65 mm 培养皿**，且其内嵌示例用 φ3 in（面积 45.60 cm²）。三处试样规格不一致，**执行前须确认以哪一版为准**，并在报告中注明。

> ⚠️ **可比性警告（原文 Note 41）**：*Specimens that are tested under different conditions may not be directly comparable.*（不同条件下测试的试样不可直接比较）——本库跨来源引用 VV 数据时必须附口径。

## 关键论断（key_claims）

- **VV = 总体积 − 液体体积 − 固体体积，是「可被液体侵入的空间」而非简单松厚度** —— 支撑页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- **0.05 psi 是 VV 法的专属压力，与成品厚度法 0.2 PSI 分属两套尺度** —— 支撑页：[[芯体测试方法与验收基准（STM）]]
- **无绒毛芯（no-fluff core）需把加载梯度上探到 30 g/g 才能画出近全饱和曲线** —— 支撑页：[[Fluff-Free 4th-Gen Absorbent Core（无木浆第四代芯体）]]
- **预测渗漏建模要求保留吸入层，无绒毛竞品须按 Fluff Percent 报告** —— 支撑页：[[Cradle Intake Test（Cradle 摄入测试）]]
- **SAM 在本法中的界定是吸水能力 ≥ 15 g/g** —— 支撑页：[[SAM Testing Methods（超级吸水材料测试方法）]]
- **自配盐水须静置 ≥ 4 h，是易被忽略的系统误差源** —— 支撑页：[[尿液模拟液（Urine Analog）]]

## 关联页面

- 概念：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]、[[芯体测试方法与验收基准（STM）]]、[[SAM Testing Methods（超级吸水材料测试方法）]]、[[尿液模拟液（Urine Analog）]]、[[Fluff-Free 4th-Gen Absorbent Core（无木浆第四代芯体）]]、[[Cradle Intake Test（Cradle 摄入测试）]]
- 实体：[[Kimberly-Clark（金佰利）]]
- 对比：[[Void Volume 与压缩模量两条孔隙表征路线对比]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM-00429 VOID VOLUME AS A FUNCTION OF SATURATION.pdf.md`
- 原文链接：（无；KC 内部标准方法，含保密声明）
- 同族文档：[[STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）]]、[[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]]

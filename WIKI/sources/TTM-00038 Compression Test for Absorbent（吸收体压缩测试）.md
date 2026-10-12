---
type: source
title: "TTM-00038 Compression Test for Absorbent（吸收体压缩测试）"
source_type: 技术测试方法（TTM）
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/TTM-00038 Compression Test for Absorbent .pdf.md
original_link: ""
date_published: 2013-04-29
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "TTM-00038 Rev.1（Technical Test Method，生效日 2013-04-29，Owner Miller, Debbie，作者 J. Levine，审阅 M. Veith）测的是吸收复合材料在湿态或干态下的「压缩载荷—厚度曲线」，输出供 KC 的吸收建模与力学建模（AFEA）使用"
  - "TTM 与 STM 的分工明写：TTM 用于研发期知识积累与跨组方法记录，不用于原材料/供应商批次验收、成品放行或厂内 QA；后者属 STM（Standard Test Method）"
  - "方法为「参数高度灵活」的研究方法：横梁速度典型 1 cm/min、最大压缩应力典型 10–20 kPa、试样直径与厚度、数据采集率、润湿量与流程、循环次数、压板尺寸均由申请方指定；标准为 3 次压缩-回弹循环"
  - "硬件口径：上压板典型 φ3.5 in、下压板 φ6.0 in；试样用 φ1.88 in（1 7/8″）圆形冲刀；湿态用尼龙/Delrin 测试杯（OD 6.00 in、ID 5.50 in、底厚 0.500、总长 1.50 in、杯深 1.00 in，底面平面度优于 0.005 in，优选 0.002 in）"
  - "润湿液典型 0.9–2.0 wt% 盐水，方法注明曾用过高至 20% 的盐水浓度；标距（gage length）湿态 3 cm、干态 1.5 cm"
  - "孔隙空间模量（Pore Space Modulus, PSM）由 Cda.exe（Exponential Kernel Compliance Distribution Program）反演：输入质量 g、面积 cm²、固相密度 g/cc（含已吸收液体的平均密度），应力范围近零至 10 kPa；输出 hpmsm.dat（第 1 列压力 kPa、第 2 列调和平均孔隙空间模量 hpmsm）"
  - "L(inf-stress) 与 delta-L 相加得到零载荷厚度（zero-load thickness），是 AFEA 的重要材料输入"
pages_linked: ["[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]", "[[芯体测试方法与验收基准（STM）]]", "[[尿液模拟液（Urine Analog）]]", "[[Kimberly-Clark（金佰利）]]"]
---

# TTM-00038 Compression Test for Absorbent（吸收体压缩测试）

## 一句话定位

TTM-00038 是 KC 研发侧的**吸收复合材料压缩载荷—厚度曲线**测试方法，其真正价值不在曲线本身，而在附录 9.1 给出的**孔隙空间模量（Pore Space Modulus, PSM）反演流程**——把压缩曲线换算成可供吸收/力学建模使用的孔隙本构参数。

## 摘要

摘要段明写：本方法测量吸收材料在**湿态或干态**下的压缩载荷/厚度曲线，所得数据用于 KC 产品与子系统的**吸收建模与力学建模**。同时声明这是**研究方法（for research purposes）**，在测试参数上非常灵活，使用者需自行指定：拉伸机横梁速度（典型 1 cm/min）、最大压缩应力水平（典型 10–20 kPa）、试样直径与厚度、数据采集率、润湿量与具体流程、循环次数，以及可选的压板尺寸与表面。输出仅为构成压缩曲线的载荷/厚度点，**不提供汇总统计量**；数据分析方法独立于本方法，不在文中给出。

文件另有一段对 **TTM 与 STM 的边界**作出定义：Technical Test Method 用于确定产品/材料属性或产品-使用交互，设计目的是在 KC 内部研发过程中积累知识、并记录跨组使用的方法；**用于原材料/供应商批次验收、成品放行、厂内 QA 或对外发布的方法不属于 TTM**，而是 Standard Test Method（STM），由 QA 归口。原本以 TTM 记录的方法，后续可转升为 STM。

硬件：恒速伸长（CRE, Constant Rate of Extension）拉伸试验机 + 计算机数据采集；载荷传感器建议使曲线大部分载荷落在量程的 10–90% 之间；上压板典型 φ3.5 in、下压板 φ6.0 in，两者须调平行（通常先让下压板自由浮动，再以最大载荷力使上压板接触，然后锁定下压板位置）；试样用 φ1.88 in 圆形冲刀（冲切时须垫保护材料以免损伤冲刀与底座）。

润湿液由申请方指定，**典型为 0.9–2.0 wt% 盐水**，文中注明该方法曾用过高至 **20%** 的盐水浓度。标距设置：湿态试样典型 3 cm、干态 1.5 cm。测试时通常自动采集 **3 个压缩-回弹循环**。

附录 9.1「Establishing Pore Space Modulus」给出完整反演流程：把「应力—修正后间距」两列数据存为 `xinput.dat`，用 **Cda.exe（Exponential Kernel Compliance Distribution Program）** 做指数核柔量分布反卷积；Setup 中 Lower Edge 取极小值（<<0）、First Order、Elements = 1000、Smoothing = 0.001，Upper Edge 由同类材料经验值起步或先取 ~10；运行后 RMSQ 应较低表示拟合良好；**L(inf-stress) 与 delta-L 相加即零载荷厚度**（AFEA 重要输入）。随后经 OutputVars 输入**质量（g）、面积（cm²）、固相密度（g/cc，注意是颗粒与纤维的平均密度，含已吸收的液体）**；应力范围典型为近零至 **10 kPa**；不建议勾选 "Use Porosity Approximation"。最终在 `hpmsm.dat` 中取得关键 AFEA 数据：**第 1 列为压力（kPa），第 2 列为调和平均孔隙空间模量 hpmsm（harmonic mean pore space modulus）**。

## 提炼的数字与结论

### 典型参数（Typical Values，均为「典型」而非强制）

| 项目 Item | 典型值 Typical value | 性质 Nature |
|---|---|---|
| 横梁速度 Crosshead speed | 1 cm/min | 典型值，申请方指定 |
| 最大压缩应力 Max compression stress | 10 ~ 20 kPa | 典型值 |
| 应力范围（PSM 反演） | 近零 ~ 10 kPa | 9.1.9.1 |
| 循环次数 Cycles | 3 次压缩-回弹 | 典型 |
| 标距 Gage length | 湿态 3 cm；干态 1.5 cm | 典型 |
| 试样直径 Specimen diameter | φ1.88 in（1 7/8″ 冲刀） | 典型 |
| 上压板 Upper platen | φ3.5 in | 典型 |
| 下压板 Lower platen | φ6.0 in | 典型 |
| 测试杯 Testing cell | 尼龙/Delrin；OD 6.00 in、ID 5.50 in、底厚 0.500、总长 1.50 in、杯深 1.00 in | 典型 |
| 杯底平面度 Flatness | 优于 0.005 in，优选优于 0.002 in | 要求 |
| 载荷传感器 Load cell | 曲线多数载荷落在量程 10–90% | 建议 |
| 润湿液 Wetting fluid | 0.9 ~ 2.0 wt% 盐水（曾用到 20%） | 申请方指定 |

### PSM 反演流程要点（Appendix 9.1）

| 步骤 Step | 内容 Content |
|---|---|
| 输入文件 | `xinput.dat`：左列应力、右列修正后间距（corrected separation） |
| 程序 | Cda.exe — Exponential Kernel Compliance Distribution Program |
| Setup 参数 | Lower Edge << 0；First Order；Elements = 1000；Smoothing = 0.001；Upper Edge 由经验起步或取 ~10 |
| 拟合判据 | RMSQ 越低越好；若峰贴近上边界会产生假峰、若末峰距上边界 > 1/3–1/2 距离，则需调整 Upper Edge 重跑 |
| 关键输出 1 | L(inf-stress) + delta-L = **零载荷厚度**（AFEA 输入） |
| 关键输出 2 | 经 OutputVars 输入质量 / 面积 / 固相密度后，查看 **AVV** 与 **HMPSM** |
| 关键输出 3 | `hpmsm.dat`：第 1 列压力（kPa），第 2 列 **hpmsm**（调和平均孔隙空间模量） |
| 注意事项 | 固相密度须为含液平均密度；部分饱和时需用湿态面积与重量；除非必要不勾 "Use Porosity Approximation" |

> ⚠️ **口径提示（2026-09-29）**：本方法**不提供精度与准确度评价**（§6.1 原文：*this test is not subject to accuracy evaluation*），且明言数据分析方法独立于方法之外。**引用 PSM 数值时必须附载硬件与参数配置**，否则不可复现。

> ⚠️ **单源数值（2026-09-29）**：上表「典型值」均来自本方法正文，本批 [[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]] 提供换算关系，但两处均未给出实测 PSM 数值；具体材料的 PSM 数值在本批中无第二来源 `[待验证]`。

## 关键论断（key_claims）

- **压缩曲线本身不是目的，PSM 与零载荷厚度才是建模输入** —— 支撑页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- **TTM 与 STM 有明确分工：TTM 研发用、STM 验收与放行用** —— 支撑页：[[芯体测试方法与验收基准（STM）]]
- **PSM 反演是反卷积问题，Upper Edge 的选取直接影响真假峰** —— 支撑页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- **固相密度须取含液平均密度，是 VV 与 PSM 互相换算的关键接口** —— 支撑页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]
- **盐水浓度可上探至 20%，远超常规 0.9% 口径** —— 支撑页：[[尿液模拟液（Urine Analog）]]
- **0.05 psi（VV 法）与 10–20 kPa（压缩法）是两套相差约两个数量级的压力尺度** —— 支撑页：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]

## 关联页面

- 概念：[[Void Volume & Pore Space Modulus（孔隙体积与孔隙空间模量）]]、[[芯体测试方法与验收基准（STM）]]、[[尿液模拟液（Urine Analog）]]
- 实体：[[Kimberly-Clark（金佰利）]]
- 对比：[[Void Volume 与压缩模量两条孔隙表征路线对比]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/TTM-00038 Compression Test for Absorbent .pdf.md`
- 原文链接：（无；KC 内部技术测试方法，含保密声明）
- 同族文档：[[TTM-00038 Pore Space Modulus to Void Volume Conversion（换算逻辑）]]、[[STM-00429 Void Volume as a Function of Saturation（方法正文）]]

---
type: source
title: "81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）"
source_type: 派生工程笔记（补库动作 · Gap G1 · 一阶模型值）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/81-成型鼓ups选型计算.md.md
original_link: ""
date_published: 2026-09-22
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "鼓距主式 P = πD / n（D 鼓节圆直径、n ups）：固定 ppm 时 ups 是改变鼓距的唯一杠杆，转速与线速随之必变"
  - "端区 E = P − L_pattern，判据 E ≥ 30 mm（端封 land + 切刀净空取大者）；30 mm 是净空下限而非最优，故选型规则是「取满足端区的最小鼓距」"
  - "推荐方案 A：Ø882.0 mm（周长 2,771 mm）+ 6-up/7-up 双套筒，鼓距 461.8 / 395.8 mm，端区均值 52 mm；B（Ø889，均值 76 mm）与 C（Ø1014，均值 69 mm）被否"
  - "最紧一档 Pant XL/XXL/XXXL 端区仅 30.8 mm（余量 0.8 mm / 2.7%）；若芯长公差为 365 ±1 mm，上偏差侧 E = 29.8 mm 判据失效——须索取芯长公差带做闭合校核"
  - "端区包覆浪费量级：单片 37–116 mg，相对单片 SAP（4.5–11.6 g）占比 <1% ⇒ 方案 A 内部端区不是包覆主成本项"
  - "可外推结论：多规格共鼓的主要代价不在尺寸跨度，而在尺寸在鼓距网格上的落点——尺寸族在某 ups 鼓距处聚集会集体被推向相邻 ups 而产生系统性浪费"
pages_linked: ["[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]", "[[One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）]]", "[[80 高速pattern芯体成型工程总纲（导航·速查·口径·分歧·验收）]]", "[[84 Sleeve 工程规格与换装防错设计]]", "[[82 鼓距与产品节距解耦 repitch 选型]]"]
---

# 81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）

## 一句话定位

80 号总纲所指「正文方法」的**第 81 号：成型鼓 ups 的选型方法论**（中文：给定 11 个尺寸与节拍，怎么选鼓径和 ups 数）。补的是 **Gap G1（「一鼓多 ups」选型方法论缺失，严重程度高，P0 批次）**。本页是 [[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]] 的**计算依据页**——该 concept 页的鼓距/端区数字均由此推导。

## 摘要

文件以 `One_Drum_Two_Ups_11_Sizes_1000ppm.pptx`（P2/P3/P4/P5 + notes）为源，给出五件事：**① 核心关系式推导**、**② 端区定义与 ≥30 mm 判据的物理来源**、**③ 搜索空间与算法**、**④ A/B/C 三方案比选**、**⑤ 端区↔包覆浪费换算**。

前置条件：节拍固定 **1,000 ppm**；尺寸族 **11 个 SAP-pattern 尺寸（6 open + 5 pants）**；芯长跨度 **280 → 420 mm（1.5×）**；芯宽 100/110/120 mm **由 CD 解决、不由 ups 解决**；鼓径窗口 **800–900 mm**；ups 搜索范围 **4–11**；端区下限 **≥30 mm**。

核心关系式：鼓距 **P = πD/n**（式 1）；鼓转速 **rpm = ppm/n**（式 2）；鼓面线速 **v = P × ppm / 1000**（式 3）；时间/度 **t_deg = 166.667/rpm**（式 4）；离心场 **a/g = (2π·rpm/60)²·(D/2)/9.80665**（式 5）。三处**因果链**值得记住：式(2) 是「换 ups 就必须改转速」的根源；式(3) 是「ups 一变、线速必变」的根源，也是 86 号 SAP 落料速度必须跟着重设的原因；式(5) 决定 SAP 落料后是否被甩飞，是真空设定的力学依据。

口径衔接：WKB `Open Diaper Process Introduction--202104.pdf` 载「Core wrap sheet design length ≈ 成形段外圆周长 / 数量」，是式(1) 在「n 固定、单一规格」下的**特例**——形式相同但**未把 n 当可选变量、无端区判据与选型规则**；本文件是其推广，**二者不冲突，引用时不得互相替代**。

方案比选：搜索 801 个直径（700–1100 mm，step 0.5）× 8 个 ups（4–11），对每个候选为 11 尺寸各解一次 n_s。窗口内按端区均值最小选优 → **方案 A：Ø882.0 mm（周长 2,771 mm）、6-up + 7-up 双套筒、鼓距 461.8/395.8 mm、端区均值 52 mm**（8 of 11 ≤ 42 mm；长端区 3 个：Open NB 116、Open S 82、Open L 77）。**方案 B（Ø889，6-up+8-up，均值 76 mm）**被否因 pants（355–365 mm）恰好落在「Ø889/8-up 装不下、退到 6-up」的夹缝区，**每片白扔 100–110 mm 包覆**；**方案 C（Ø1014，7-up+9-up，均值 69 mm）**被否因鼓径越出 800–900 mm 硬窗口。

## 提炼的数字与结论

| 项目 | 数值 / 结论 | 备注 |
|---|---|---|
| 节拍 | 1,000 ppm | 固定 |
| 尺寸族 | 11（6 open + 5 pants），芯长 280–420 mm | 芯宽 100/110/120 由 CD 解决 |
| 鼓径窗口 | 800 – 900 mm | 来自用户 Word 文件，**非源件假设** |
| ups 搜索范围 | 4 – 11 | — |
| 端区判据 | **E ≥ 30 mm**（端封 land + 切刀净空取大者） | 净空下限，非最优 |
| 端区定义 | **E = P − L_pattern** | 式(6) |
| 方案 A 鼓径 / 周长 | **Ø882.0 mm / 2,771 mm** | @NW 中面 |
| 方案 A ups | **6-up（461.8 mm）+ 7-up（395.8 mm）** | 同一鼓体两套 sleeve |
| 方案 A 端区均值 | **52 mm**（8/11 ≤ 42 mm） | 长端区：NB 116 / S 82 / L 77 |
| 方案 B | Ø889 mm，6-up+8-up，均值 **76 mm** | 否决：pants 每片浪费 100–110 mm |
| 方案 C | Ø1,014 mm，7-up+9-up，均值 **69 mm** | 否决：越出鼓径窗口 |
| ⚠️ 源文案勘误 | 源写「9 of 11 ≤ 42 mm」，按 P5 表重算应为 **8** | 以数据表为准 |
| 最紧一档 | **Pant XL/XXL/XXXL 端区 30.8 mm**（余量 0.8 mm / 2.7%） | 本件新增发现，源件未提示 |
| 单片端区包覆浪费 | **37 – 116 mg**（包覆 SMS 10 gsm） | 相对单片 SAP 4.5–11.6 g 占比 **<1%** |
| SAP 用量 | 160–230 gsm @芯体投影面积；**4.5–11.6 g/片**；吞吐 269–696 kg/h | — |
| repitch ratio | 0.99 – 1.25 | ⚠️ chassis 节距为源件假设值（芯长 +110 open / +130 pants） |
| 包覆放卷线速 | **= 鼓面线速 = 鼓距 × ppm** → 396 / 462 m/min | 式(3)；传动侧设计依据 |

> ⚠️ **证据等级红线（源件自述）**：全部数值为**一阶模型值（B 级）**，非实测；引用须携「工况 + 等级」。算术复算已验证，**物理模型未验证**（鼓径窗口、30 mm 判据、芯长公差的耦合均为 B/C 级输入）。§6.1 的余量风险为**推断**。结论不得外推到其它鼓径、其它 ups 组合或底盘节距不同的尺寸族。

## 关键论断（key_claims）

- **ups 是固定鼓径 + 固定 ppm 下改变鼓距的唯一杠杆** —— 支撑页：[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]
- **端区是「要贴着下限走」的量，不是「要做大」的量** —— 支撑页：[[84 Sleeve 工程规格与换装防错设计]]（land 体系）
- **选型规则的物理含义：优先把端区做小（省包覆），但绝不越过 30 mm 下限** —— 支撑页：[[One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）]]
- **多规格共鼓的主要代价在「尺寸在鼓距网格上的落点」，不在尺寸跨度** —— 可外推的一般结论
- **端区不是方案 A 内部的包覆主成本项（<1%）** —— 与源件「端区越小越省包覆」方向一致，但给出量化尺度

## 关联页面

- 概念：[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]、[[Core Channel Pattern（芯体通道花型设计）]]、[[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]
- 源：[[80 高速pattern芯体成型工程总纲（导航·速查·口径·分歧·验收）]]、[[One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）]]、[[84 Sleeve 工程规格与换装防错设计]]
- 同族待补：[[82 鼓距与产品节距解耦 repitch 选型]]、[[Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]]、[[87 卫材产线约束常量表（待并入补充行）]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/81-成型鼓ups选型计算.md.md`
- 原文链接：（无；派生工程笔记，由「纸尿裤全栈设计专家（CoreCraft）」2026-09-22 生成）
- 依据：`One_Drum_Two_Ups_11_Sizes_1000ppm.pptx`（P2/P3/P4/P5 + notes）；`[Open Diaper Process Introduction--202104.pdf]`；`references/80-高速pattern芯体成型工程总纲.md`；`references/74-COCO-v6项目技术档案.md`

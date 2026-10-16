---
type: source
title: "82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）"
source_type: 派生工程笔记（补库动作 · Gap G16 + 副交付 G15 · 一阶模型值）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/82-鼓距与产品节距解耦repitch选型.md.md
original_link: ""
date_published: 2026-09-22
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "鼓距 P = πD/n 是离散量，产品节距（chassis pitch）C 由产品规格各自决定，两者没有理由相等 ⇒ repitch（节距重排）单元是「一鼓多规格」的必要条件，不是可选优化项"
  - "两条解耦路线：cut-and-slip（切断后加速带，只能加速、ratio ≥~1.03、上限 ~1.30）vs 伺服 repitch 转塔（puck 沿各自凸轮轨迹，双向、0.85–1.40）；源文件采用转塔，判据是「NB 需要被减速」"
  - "repitch ratio = chassis pitch / drum pitch；11 规格重算跨度 0.985–1.251，其中 Open NB = 0.985 是唯一越界者（<1.03），一个越界即足以否决 cut-and-slip"
  - "⚠️ chassis pitch 全部为源文件假设值（芯长 +110 mm open / +130 mm pants，B 级）；替换为实测值后全部 ratio 需重算"
  - "反向校核靶：要让 Open NB 进入 cut-and-slip 窗口需 C_NB ≥ 407.7 mm，即 open 股间间隙 k_open ≥ 127.7 mm"
  - "芯片废切 chip trim 规则：端区 E > 80 mm 则切回 60 mm（NB 切 55.8≈56 mm、S 切 21.8≈22 mm）；NB 的硬冲突是「芯长 > 产品节距」（395.8 > 390 mm），剪到 340 mm 后才放得进"
  - "与 G1 的耦合：ups 加多 → 鼓距减小 → 端区减小（省包覆）但 ratio 减小；ratio 下界构成 ups 选择的隐藏约束"
pages_linked: ["[[Repitch（鼓距与产品节距解耦）]]", "[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]", "[[81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）]]", "[[Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]]", "[[80 高速pattern芯体成型工程总纲（导航·速查·口径·分歧·验收）]]"]
---

# 82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）

## 一句话定位

80 号总纲「正文方法」的**第 82 号：鼓距与产品节距的解耦（repitch）选型**（中文：成型鼓上的节距与后道要的节距不一样，中间靠什么单元过渡）。补的是 **Gap G16（鼓距—产品节距解耦单元完全缺失，零覆盖，严重程度高，P0 批次）**，副交付 **G15（chip trim 与「芯长 > 产品节距」处置规则）**。

## 摘要

问题陈述：**鼓距 P = πD/n** 是成型线由鼓径与 ups 决定的离散量；**产品节距 C（chassis pitch）** 是后道（复合/折叠/切断/包装）要求的产品中心距，由 11 个产品规格各自决定。**两者没有理由相等**。若强制 P = C，则 πD/n = C 会对 11 个规格给出 11 个不同的 D，与「单一鼓体」前提直接矛盾 → **repitch 单元是"一鼓多规格"的必要条件**。

两条路线对比：**cut-and-slip**（切断后由加速带/夹辊加速单片芯体送到下道）只能**加速**、可行窗口约 **1.03 ≤ ratio ≤ 1.30**、通用凸轮；**伺服 repitch 转塔**（转塔上独立 puck 沿各自凸轮轨迹取片再放到目标节距）**双向**、范围 **0.85–1.40**、每规格一份凸轮。源文件判据（P6 标题）：「**A servo repitch turret, not cut-and-slip — because NB needs the core slowed down**」。

转塔规格：类型伺服 repitch 转塔；节距比 **0.85–1.40**；取片线速 **396 或 462 m/min**（= 鼓面线速，见 81 式 3）；放片节距 = chassis pitch（按规格）；换规格靠每规格一份凸轮（recipe + 换件）；位置在**双鼓压合点之下**（切断、修边、repitch 依次在压合后）；**转塔只认"取片线速 + 目标节距"，不感知 ups**（ups 影响的是取片线速）。

**repitch ratio = C_s / P_group(s)**，分母取该尺寸所属 ups 组（7-up 组 395.83 mm、6-up 组 461.80 mm）。11 规格重算：Open NB **0.985**、S 1.071、M 1.182、L 1.072、XL 1.148、XXL 1.148、Pant L 1.225、Pant XL/XXL/XXXL 1.251、Pant XXXXL 1.191，跨度 **0.985–1.251**，落在转塔窗口内（下沿余量 −0.14、上沿 +0.15）。**恰有 1 个（Open NB）越 1.03 下界，且是唯一越界者——一个越界即足以否决 cut-and-slip。**

## 提炼的数字与结论

| 项目 | 数值 / 结论 | 备注 |
|---|---|---|
| 鼓距 P | **πD/n**；7-up 组 395.83 mm、6-up 组 461.80 mm | 离散量 |
| 转塔节距比范围 | **0.85 – 1.40** | 源文件 P6；B |
| cut-and-slip 可行窗口 | **~1.03 – ~1.30** | ⚠️ 两个边界无出处，B 级 |
| 11 规格 ratio 跨度 | **0.985 – 1.251** | 与源文件 P5 逐项一致 ✓ |
| 越界者 | **Open NB = 0.985（唯一）** | 低于 1.03 |
| chassis pitch 假设式 | C = 芯长 + k；**k_open = 110 mm**、**k_pants = 130 mm** | ⚠️ 源文件假设值，B 级 |
| 反向校核靶 | NB 需 **C ≥ 407.7 mm** ⇒ **k_open ≥ 127.7 mm** 才可能回到 cut-and-slip | 向产品侧索取实测值时的验算靶 |
| 稳健性 | 实测值与假设值差异 **<5%** 结论不变；pants 侧上偏约 4% 或 open 侧继续下偏，结论均不反转 | 推断 |
| chip trim 判据 | 端区 **E > 80 mm** → 切回 **60 mm** | 切除长度 = E − 60 |
| chip trim 应用 | **Open NB 切 55.8 ≈ 56 mm**（芯长变 340 mm）；**Open S 切 21.8 ≈ 22 mm**（变 374 mm） | 其余 9 规格不触发 |
| NB 硬冲突 | 鼓距 395.8 mm > 假设 NB 产品节距 390 mm ⇒ **不修剪则芯体放不进自己的产品节距** | 源文件 top risk #3 |
| 切刀硬件 | **双刀切刀辊**（同辊实现定长切 + 芯片切）+ 真空排屑 | 刀片插片仅随 NB/S 两个 sleeve 更换 |

> ⚠️ **证据等级红线（源件自述）**：chassis pitch **全部为假设值（B 级）**，源文件明确声明其不在 Word 文件中，**引用 ratio 表必须携带该标注，禁止当作实测值引用**；**ratio 的算术复算已验证**，但 §6.3 稳健性与 §7 耦合结论为**推断**；**1.03 / 1.30 两边界无出处**；chip trim 的 **80/60 mm 阈值未说明推导**。

## 关键论断（key_claims）

- **repitch 是"一鼓多规格"的必要条件，不是可选优化项** —— 支撑页：[[Repitch（鼓距与产品节距解耦）]]
- **选用转塔而非 cut-and-slip 的直接判据是「NB 需要被减速」** —— 支撑页：[[Repitch（鼓距与产品节距解耦）]]
- **chip trim 不只是省材料，更是解决「芯长 > 产品节距」的物理冲突** —— 支撑页：[[81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）]]
- **ups 分配不能只看端区，必须同时校核 repitch ratio（本件新增耦合发现）** —— 支撑页：[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]
- **WKB 的「尺寸标准」条目不能用来推导 chassis pitch** —— 尺寸标准给成品外形（长×宽），chassis pitch 是工艺节距（含股间间隙），**当节距用会引入系统性误差**

## 关联页面

- 概念：[[Repitch（鼓距与产品节距解耦）]]、[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]、[[Core Channel Pattern（芯体通道花型设计）]]
- 源：[[81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）]]、[[Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]]、[[80 高速pattern芯体成型工程总纲（导航·速查·口径·分歧·验收）]]、[[03_卫材产线约束常量表（准入校验工具）]]
- 参考标准：[[GB-T 28004.1-2021（纸尿裤国标）]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/82-鼓距与产品节距解耦repitch选型.md.md`
- 原文链接：（无；派生工程笔记，由「纸尿裤全栈设计专家（CoreCraft）」2026-09-22 生成）
- 依据：`One_Drum_Two_Ups_11_Sizes_1000ppm.pptx`（P1/P5/P6/P7/P12/P18 + notes）；`[Open Diaper Process Introduction--202104.pdf]`；GB/T 33280-2016；`[STM-00064 Diaper尺寸.docx]`、`[STM-00433 Pants尺寸.doc]`；`03_卫材产线约束常量表.md`；`references/80-…总纲.md`、`81-成型鼓ups选型计算.md`

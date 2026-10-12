---
type: source
title: "83 Changeover Four-Layer Architecture and Change Control（换型要素四层分层与变更控制）"
source_type: 派生工程笔记（补库动作 · Gap G2 · 一阶模型值）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/83-换型要素四层分层与变更控制.md.md
original_link: ""
date_published: 2026-09-22
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "分层第一原则（源文件 P8）：'Everything that defines phase is on the drum body; everything that defines size is on the sleeve.'（定相位的都在鼓体，定尺寸的都在套筒）"
  - "强约束（P4）：skin 鼓与 poly 鼓必须始终携带相同的 ups —— 双鼓对压要求两侧鼓距与相位完全一致 ⇒ ups 是整线级参数，不是单鼓参数"
  - "四层：Layer 1 Body（永不动）／Layer 2 Sleeve（必换，每次 2 片）／Layer 3 Recipe（必改，无实体换件）／Layer 4 Change-part（仅特定规格，chute 宽度插片 + NB/S 刀片插片）"
  - "归属判据 Q1–Q4：换 ups 时不变 → Body；由 MD 尺寸决定 → Sleeve；只由宽度族或边缘形状决定 → Change-part；能否仅靠设定值表达 → Recipe；不能 → 设计缺陷"
  - "CD 变更必须走 chute 宽度插片：用 ups 解决 CD 不可能（P=πD/n 只作用于 MD）；做进鼓体则 3 套鼓体与单一鼓体前提矛盾；做进 sleeve 则 22 片爆炸到 33 片"
  - "换型 SOP 四步：Stop & swap ≤15 min ／ Recipe load ／ Auto-phase（±0.05 mm 引脚 + ~17 片相机收敛）／ Verify；总目标 <30 min 但 Step 2–4 工时缺失 ⇒ 「<30 min」无法从分项加总验证"
  - "⚠️ sleeve 换装工时存在 30 倍分歧：源文件 ≤15 min/鼓 vs WKB [日本Nichdai 丝网工艺技术交流] 的 30 s/网，必须并列呈现不得择一"
pages_linked: ["[[83 Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]]", "[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]", "[[Repitch（鼓距与产品节距解耦）]]", "[[81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）]]", "[[84 Sleeve 工程规格与换装防错设计]]", "[[Nichidai（日丝）]]"]
---

# 83 Changeover Four-Layer Architecture and Change Control（换型要素四层分层与变更控制）

## 一句话定位

80 号总纲「正文方法」的**第 83 号：换型要素的四层分层架构与变更控制**（中文：换规格时到底该动哪一层）。补的是 **Gap G2（换型要素"四层分层"架构缺失，严重程度高，P0 批次）**。源件自我定位：WKB 有「丝网」知识（**零件级**，回答"网怎么做"），但没有「换型架构」知识（**系统级**，回答"换规格时该动哪一层"）——本文件填的是后者。

## 摘要

**第一原则**（源文件 P8 副标题原文）：*"Everything that defines phase is on the drum body; everything that defines size is on the sleeve."* 即按「**定相位** vs **定尺寸**」正交切分：鼓体 Body 承载一切决定相位基准与机械几何的量（**永不动**）；Sleeve 承载一切决定尺寸的量（**必换**，每次 2 片）。

**强约束**（P4）：*"Both drums (skin and poly) always carry the same ups — the nip requires identical pitch and phase on each side."* → **skin 鼓与 poly 鼓的 ups 必须始终相同**，这不是可选项，因为双鼓对压要求两侧鼓距与相位完全一致。**故 ups 是整线级参数，不是单鼓参数。**

**四层清单**：
- **Layer 1 · Body（永不动）**：节圆直径 Ø882.0 mm @ NW 中面（周长 2,771 mm）、鼓壳（估算 270 kg，J ≈ 52 kg·m²）、轴承、真空扇区（**固定角度，与 ups 无关**，P8："No sector change at grade change"）、力矩电机（≥250 Nm 连续 / ≥600 Nm 峰值）+ ≥23 bit 绝对值编码器、压合间隙 **land-to-land 0.15–0.18 mm**、轴向对中（100/110/120 共用同一轴向设定）、镜像手（skin/poly 同本体镜像）、风机/管路/胶模块。
- **Layer 2 · Sleeve（必换）**：**22 片 = 11 尺寸 × 2 侧**；pocket-and-land 浮雕、land 高 0.45 mm；**端区也是 land**（保证芯间无 SAP）；屏 Ø0.6–0.8 mm、30–40% 开孔、各 sleeve 一致；pattern 公差 **±0.02 mm over 2,771 mm**（等节距 = 同一相位适配全部）；pin + 锥面锁紧、≤15 min/鼓；**sleeve ID tag 由 PLC 读取以阻止错误 ups 的 recipe**；skin/poly **必须成对设计**（同一 CAD、同时制造）。
- **Layer 3 · Recipe（必改，无实体换件）**：ups n（6 或 7）、cams（含 repitch 转塔每规格凸轮）、fan（VFD 速度设定）、glue（分段阀开关按 100/110/120 宽度族 + 泵速跟随鼓面线速）、**chute（SAP 落料速度 396 或 462 级，头号失效模式，见 86）**、成型真空（−8…−12 kPa 属 recipe 项）、气刀压力。P12 摘要原文：*"Recipe (sleeve ID-checked): ups n, cams, fan, glue, chute"*。
- **Layer 4 · Change-part（仅特定规格）**：**SAP chute 宽度插片**（100/110/120，每次换宽度族时需要）；**刀片插片 knife insert**（**仅 NB、S** 需 chip 切，仅换到/离开 NB/S 时需要）。

P8「At grade change」双栏：**Changes** = 2 sleeves (skin + poly) · SAP chute width insert · Recipe (ups, cams, fan, glue) · Knife insert (NB, S only)；**Stays** = Drum bodies, bearings, sectors · Torque motors and encoders · Nip gap and axial alignment · Fans, ducts, glue modules。

**为什么 CD 变更走 chute 插片**：用 ups 解决 CD **不可能**（P = πD/n 只作用于 MD）；做进鼓体 → **3 套鼓体** + 3 套扇区 + 3 套对中，与"单一鼓体"矛盾；做进 sleeve → **22 片爆炸到 33 片**且 CD/MD 混层；**chute 宽度插片**最廉价、换装最快、CAD 上只改出口轮廓 ✓。逻辑闭环：**CD 由「鼓体对中 + chute 出口宽度插片」共同决定 → 鼓体只负责居中（不变），插片负责宽度（可换）→ 宽度族扩展的边际成本降到只剩一片插片**。源件称这是**本架构最重要的成本设计**。

## 提炼的数字与结论

| 项目 | 数值 / 结论 | 备注 |
|---|---|---|
| 第一原则 | **定相位在鼓体，定尺寸在套筒** | 源文件 P8 原文 |
| 双鼓约束 | **skin/poly 必须同 ups** | P4；ups 是整线级参数 |
| Sleeve 数量 | **22 片 = 11 尺寸 × 2 侧**；每次换型换 **2 片** | P9 |
| Body 关键值 | Ø882.0 mm（周长 2,771 mm）；鼓壳 ~270 kg（J ≈ 52 kg·m²）；压合间隙 **0.15–0.18 mm** | NW 中面口径 |
| Recipe 项 | **ups / cams / fan / glue / chute**（+ 成型真空、气刀） | P12；由 sleeve ID 校验把关 |
| Change-part | chute 宽度插片 **100/110/120**；刀片插片**仅 NB/S** | P7/P18、P6/P18 |
| 换型 SOP 四步 | Stop & swap ≤15 min → Recipe load → Auto-phase → Verify | 总目标 **<30 min** |
| 引脚 / 相机 | 引脚 **±0.05 mm**；相机闭环 **~17 片** 收敛 MD | P18 |
| ⚠️ 时间账 | **Step 2–4 工时缺失 ⇒ 「<30 min」无法从分项加总验证** | 本次发现 |
| ⚠️ 换装工时分歧 | 源文件 **≤15 min/鼓** vs Nichidai **30 s/网** → **差 30 倍，必须并列** | 可能源于换装对象/内容/口径不同 |

### 四层 × 工艺参数耦合矩阵（读法）

| 工艺参数 | Body | Sleeve | Recipe | Change-part |
|---|---|---|---|---|
| 真空扇区角度 | ● 定义（固定） | — | — | — |
| 各段停留时间 | — | — | ● 定义（随 ups 变） | — |
| 成型真空值 | — | ○ 影响床阻 | ● 设定 | — |
| 风机风量 | — | ○ 影响泄漏面积 | ● 设定 | — |
| 胶分段开关 | — | ○ 通道位置决定上胶图形 | ● 设定 | ● 插片决定涂布宽度 |
| 胶泵速 | — | — | ● 跟随鼓面线速 | — |
| SAP 落料速度 | — | — | ● 设定（**头号失效点**） | ○ 出口形状影响落点 |
| 相机相位修正 | ● 基准 | ● pattern 位置 | ● 控制环参数 | — |
| 套准（双层互套） | ● 相位基准 + 压合间隙 | ● 两片成对设计 | — | — |
| CD 宽度 | ● 对中（不变） | — | — | ● 插片宽度 |
| 端区 / chip | — | ● 端区 land | — | ● 刀片插片（NB/S） |

> ● 该层直接定义；○ 该层间接影响。**读法**：换 ups 时真正需要改的只有 **Recipe 一列（+ 换 sleeve）**；凡发现某工艺参数在多列同时被改动，说明**分层没做干净**，应回到 Q1–Q4 重判。

### 变更控制红线

**绝不可做进 Body / 固定结构**（否则规格扩展成本失控）：CD 宽度（100/110/120，必须走 chute 插片）｜ pattern 长度 / 端区分布（尺寸载体必须可换）｜ ups 相关的相位关系（n 脉冲，必须由 Recipe 表达为 e-cam；做进机械凸轮则每 ups 一套凸轮组）｜ 端区长度（属 sleeve，不可由固定挡块定义）｜ 换宽度族的涂布宽度（必须走分段阀 + 插片，不可用固定喷嘴）。

**必须固化在 Body（不可下放）**：真空扇区角度（下放会导致换型需改扇区）｜ 压合间隙与轴向对中（下放会引入每规格间隙误差，破坏 land-to-land）｜ 编码器零点 / 引脚基准（换型不重新对相的前提）｜ 双鼓镜像手与同 ups 约束。

> ⚠️ **证据等级红线（源件自述）**：四层清单与归属来自**源文件设计意图（B 级），非 KC 现行实践**，尚未与现场实际换型流程比对；**禁止对外声称「已验证 <30 min」**；sleeve 换装工时的 30 倍分歧**必须并列**；§3 判据与 §7 红线为**推断**，未实测；**不外推到多鼓方案或卡簧快换方案**。

## 关键论断（key_claims）

- **「定相位 vs 定尺寸」的正交切分是全部换型设计的根** —— 支撑页：[[83 Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]]
- **CD 走 chute 插片是本架构最重要的成本设计：宽度族扩展的边际成本降到只剩一片插片** —— 支撑页：[[83 Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]]
- **Q4 的"不能"分支是架构缺陷检测器** —— 任何"随尺寸变、又必须换实体件、且换起来很贵"的量，都是设计没做干净
- **ups 是整线级参数（双鼓必须同 ups），不是单鼓参数** —— 支撑页：[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]
- **换 ups 时真正需要改的只有 Recipe 一列（+ 换 sleeve）** —— 支撑页：[[Repitch（鼓距与产品节距解耦）]]

## 关联页面

- 概念：[[83 Changeover Four-Layer Architecture（换型要素四层分层与变更控制）]]、[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]、[[Repitch（鼓距与产品节距解耦）]]、[[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]
- 源：[[81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）]]、[[82 Drum-to-Chassis Pitch Decoupling and Repitch Selection（鼓距与产品节距解耦）]]、[[84 Sleeve 工程规格与换装防错设计]]、[[80 高速pattern芯体成型工程总纲（导航·速查·口径·分歧·验收）]]、[[03_卫材产线约束常量表（准入校验工具）]]
- 实体：[[Nichidai（日丝）]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/83-换型要素四层分层与变更控制.md.md`
- 原文链接：（无；派生工程笔记，由「纸尿裤全栈设计专家（CoreCraft）」2026-09-22 生成）
- 依据：`One_Drum_Two_Ups_11_Sizes_1000ppm.pptx`（P2/P4/P7/P8/P9/P12/P18 + notes）；WKB `[日本Nichdai 丝网工艺技术交流]`、`[Patterned SAP core 6.pptx]`、`[合作开发新模具设计]`、`03_卫材产线约束常量表.md`、`[BCC成品STM-南京南厂 1.pdf]`；本地 `references/80/81/82/84/86`

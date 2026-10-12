---
type: entity
title: "Nichidai（日丝）"
category: 供应商（成型丝网 / 印花芯体套筒）
relationship: 候选询价对象（未确认供货 / 未确认可制造性）
real_name_hint: "工商全称须人工核对；库内源文亦见拼写 Nichdai（少一个 i），引用时须确认"
updated: 2026-09-29
tags: [丝网, sleeve, pattern 成型, 锥度方向, 卡簧快换, pattern-SAP 干法沉积]
---

# Nichidai（日丝）

## Basic Profile 基本盘

| Item 项目 | Content 内容 |
|---|---|
| 主营 Main business | **成型丝网（screen）与套筒（sleeve）**类精密部件；库内以 **日本 Nichidai 丝网工艺技术交流** 为来源 |
| 本库定位 Role | **pattern-SAP 芯体成型鼓的丝网 / 套筒候选供应商**；亦是**既有丝网工艺知识的来源方** |
| 成熟产品口径（既有记录） | **六边形孔**；孔径 **≥1.4 mm（下限）**；开孔率 **60 / 70 / 80%**；**0.1 mm 层积蚀刻，有锥度方向** |
| 快换方式 | **卡簧式快换**，供应商目标 **30 s 换网**（经验待确认，C 级厂商标称） |
| 确认状态 Confirmation | **未确认** —— 库内**无**报价、样品、TDS、加工图或量产记录；所有规格均为**技术交流与方案目标值** |

## Cooperation and Supply History 合作与供货历史

- **技术交流（无日期，库内记为 WKB〔日本 Nichidai 丝网工艺技术交流〕）**：提供了丝网**孔型 / 孔径 / 开孔率 / 层积与锥度方向**的口径，以及**卡簧快换**与 **30 s 换网目标**。`[待验证]`
- **2026-09（[[One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）]]）**：本方案拟向其采购 **22 片 sleeve 套件**（11 尺寸 × skin/poly，pocket-and-land 浮雕）。
- **2026-09-22（[[84 Sleeve 工程规格与换装防错设计]]）**：把该询价收敛为可发送条目，并**明确列出须向其澄清的四项**：① **pattern 沉积类屏的既有规格**（因既有口径与本方案目标差约 2×）；② **换装工时口径**（≤15 min/鼓 vs 30 s/网，差 30 倍）；③ **锥度防呆 / ID 编码方案**；④ **land 高逐片加工能力**。
- **⚠️ 无历史合作事实**：本页所有内容均为**技术交流记录与询价准备**，**不构成供货历史或能力确认**。

## ⚠️ 两套丝网口径必须并列（关键）

| 项 | **本方案目标（84 号 / One_Drum P9）** | **既有 Nichidai 口径** |
|---|---|---|
| 孔型 | 未注明 | **六边形孔** |
| 孔径 | **Ø0.6–0.8 mm** | **≥1.4 mm（下限）** |
| 开孔率 | **30–40%** | **60 / 70 / 80%** |
| 层积 | 未注明 | **0.1 mm 层积蚀刻，有锥度方向** |
| 等级 | B（方案目标值） | C（厂商标称，既有成熟产品） |

- **差异约 2×（孔径与开孔率两个维度同时）**。
- **可能原因（未验证）**：面向的**成型机制不同** —— Nichidai 既有丝网为**传统整幅成型**（大孔高开孔率以通过纤维/浆料），本方案为 **pattern-SAP 干法沉积**（小孔以在 land 边缘形成**锐利边界**、抑制 stray SAP）。
- **处理要求**：**两条口径并列记录，禁止静默取其一**；询价时须明确说明「**本方案用于 pattern-SAP 干法沉积，非浆料成型**」。

## Known Incident 已知事故（须在设计中继承）

| 项 | 内容 |
|---|---|
| **锥度装反 → SAP 堵塞** | 丝网**锥度方向装反**会导致 SAP 堵塞（**已发生的历史事故**，记载于 WKB〔日本 Nichidai 丝网工艺技术交流〕） |
| 设计后果 | **锥度方向是不可逆向的装配依赖** → 必须在 **ID tag + PLC 联锁防错**体系中**一并编码**（不仅防错 ups，还须防错装反方向） |
| 规格落地 | 验收项 **A8：锥度方向 / 装配方向须不可逆向装配**（装配试验验证防呆） |

## Price and Commercial Points 价格与商务要点

> 🔴 **manual_review（2026-09-29）**
>
> - 库内**无**本实体的任何价格、报价、MOQ、交付期或质保数据。
> - 相关询价条目（22 片套件、索引重复性 ±0.02 mm、屏规格、ID tag 方案、动平衡 G1.0、NDA 与 IP 条款等）**属于商务文件**，本页**只记条目结构与等级，不落条款**。
> - **IP 归口**：源文明确 **孔径分布 / pattern 细节为 KC 专有技术**，须**签 NDA、图纸受控发放、pattern 数据不出 KC**；**ID 编码映射关系亦不宜外泄**。
> - **事故信息**（锥度装反致堵塞）为**内部记载**，对外沟通须谨慎。

## Relations 关联

- **需求侧页面**：[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]、[[One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）]]、[[84 Sleeve 工程规格与换装防错设计]]、[[SAP Dosing Speed Matching & Tolerance Spec（SAP 落料速度匹配与容差规范）]]。
- **易混实体**：[[Nippon Shokubai（日本触媒）]]（SAP 供应商，非丝网/套筒供应商，勿混淆）。
- **组合页**：[[IPC BCC OI Portfolio（开放创新项目组合）]]。

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · `Patterned SAP core 6.pptx` 已建源页，部分口径可核验）

> 来源：[[Patterned SAP Core 6（印花·分区·成形 SAP 芯体开发目标与收益 · 2026-07）]]（IPC FEI & OI，2026-07）。

1. **本页原记为 `[待验证]` 的转述源已有一手来源页** —— 「Patterned SAP core 6.pptx」现已编译为独立 source 页，**其中关于 Nichidai 的口径可直接核验**（此前系经 84 号与 One Drum Two Ups 两份派生文件转述）。
2. **Nichidai 网技术被定位为"可控真空的来源"** —— 源文标题即写明：「**Forming Fan with invertor & magnetic coupling technology + Nichidai screen technology, source of controllable vacuum**」。**Nichidai 的技术在方案中的角色是"让真空可被设计"，而非单纯供网。**
3. **与带框网的结构差异** —— 本方案为 **all-in-one 设计，无 pocket frame、无分段，开孔面积更大（more open area）**；与 **Innovent 带框网**的差异被显式点出为**开孔面积**。
4. **工艺路线** —— **支撑蚀刻（Support Etching）**与**多层层压蚀刻网（Multi-layer laminated etching screen）**；**当前能力下最小孔心距 0.14 mm**。
5. **能力落差被明确记录** —— 本国供应商 **Chuanyue** 的演示线使用**类 Innovent 常规网 + 自设计成形鼓**，源文直书其 **"don't know Nichidai screen technology"**；其线速 **100 m/min**（KC 天津平台），而 HCH 的印花芯体方案目标为 **1200 PPM**。**"掌握 Nichidai 网技术"与"能做出图案"在源文中被视为不同代际的能力。**
6. **⚠️ 与上方"两套丝网口径"的关系** —— 本源**未给出丝网目数/开孔率的第二套数值**，因此**上方两套口径并列的问题不在本源中得到解决**，**维持原状**；本源只补入**孔心距 0.14 mm** 这一独立指标。

> ✅ 验证（2026-09-29）：本节为**追加**，**未修正上方任何既有结论**（含"两套丝网口径必须并列"与"已知事故"两节）。上方关于 `Patterned SAP core 6.pptx` **尚未建源页**的说明，已因本批建立该源页而**在事实层面过期**，但为保留追溯，**未删改原文**，仅在此登记。
> 🔴 **manual_review（2026-09-29）**：源文同时点名 **Innovent、Chuanyue、HCH**；本页**只记技术能力事实，不记报价、合同条款或未公开合作约定**。

## Sources 来源

- [[84 Sleeve 工程规格与换装防错设计]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/84-Sleeve工程规格与换装防错设计.md.md`
- [[One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/One_Drum_Two_Ups_11_Sizes_1000ppm.pptx.md`
- ⚠️ 源文中引用的 **WKB〔日本 Nichidai 丝网工艺技术交流〕** 与 **Patterned SAP core 6.pptx** 在本库中**尚未建立独立来源页**，其口径经上述两份派生文件转述，**未经一手文件核验**，记为 `[待验证]`。

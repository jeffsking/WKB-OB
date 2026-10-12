---
type: concept
title: "Total Luminous Transmittance for Excretion Visibility（排泄可视·全光线透过率）"
domain: [卫材研发, 结构设计]
status: seed
updated: 2026-09-29
tags: [全光线透过率, total luminous transmittance, 排泄可视, 薄型芯体, 无绒毛浆, 光学验收]
aliases: ["Excretion Visibility", "Total Luminous Transmittance", "排泄可视性"]
---

# Total Luminous Transmittance for Excretion Visibility（排泄可视·全光线透过率）

> One-line definition 一句话定义：把"**从尿裤外侧能否看见排便**"量化为一个可验收的光学指标——**从非皮肤侧外片、经吸收结构体、到皮肤侧内片的整体全光线透过率（total luminous transmittance）**，其可用窗口为 **15%–65%**；低于约 15% 则排泄物不可见，高于约 65% 则日常体貌透明度过高（"过于透光"）。

## Definition / Mechanism 定义与机理拆解

1. **它是叠层指标，不是片材指标**：测量路径是**外片 → 吸收结构体 → 内片**的整体透光，任一层变厚或不透光都会把它压下来。
2. **要实现"看得见"，必须先"变薄"**（本库的因果主线）：传统绒毛浆 + SAP 的**纵向连续芯**在厚度 **5.8 mm** 时只有 **10.2%**、**3.2 mm** 时 **13.1%**，均落在窗口之外；改为**无绒毛浆的分区 SAP 薄结构**（整体 0.9 mm）后升到 **26.9%（吸收区）/ 28.8%（封合区）**。
3. **结构很简单但很关键**：两张 SMS 片材夹 SAP 颗粒形成**交替排列的吸收区**，再由**封合区环绕每个吸收区**并把上下片热封；既固定 SAP，又把厚度压住。
4. **白度与无花纺也是设计的一部分**：来源要求内片、外片及腰外片使用**无花纹的白色纤维无纺布**——避免色块与图案进一步吃掉透光。
5. **与"为什么要看见"的关系**：目的是让照护者**不经拆解即可判断排便是否发生**；这与本库途经化学/印刷路线的指示方案（[[BM Urine Indicator Concept（尿+便双指示概念）]]）是**两条并行路线**：一条靠"透出来"，一条靠"显色"。
6. **方向相反的相邻机制**：[[Geometric Optical Mask（几何光学掩膜）]] 刻意用哑光/遮光层把底下颜色遮住，直到拉伸才露出；本概念则是**尽量少遮**。二者可在同一产品的不同区域并存（例如裆部求透、腰围求遮）。

## Key parameters 关键参数表

| Parameter 参数 | Typical value / range 典型值 / 范围 | Source 出处 |
|---|---|---|
| 权利要求窗口 claim window | **15% – 65%** | [[EP2529717A1 Disposable Absorbent Article with Excretion-Visible Core (Unicharm)]] Claim 1 |
| 实测：吸收区 absorbing regions | **26.9%** | 同上 TABLE 1（Example 1-A） |
| 实测：封合区 sealing regions | **28.8%** | 同上 TABLE 1（Example 1-B） |
| 比较：传统连续芯 5.8 mm | **10.2%**（低于下限） | 同上 TABLE 1（Comparative Example 1） |
| 比较：传统连续芯 3.2 mm | **13.1%**（低于下限） | 同上 TABLE 1（Comparative Example 2） |
| 厚度 constraint | 吸收结构体厚度方向 **0.5–9.0 mm** | 同上 Claim 3 |
| 手感约束 bending resistance | 纵向悬臂法弯曲阻力 **15–140 mm** | 同上 Claim 3 |
| 材料约束 | 内片 / 外片 / 腰外片采用**无花纹白色纤维无纺布** | 同上 Claim 6 |
| 测量口径 measurement | **50 mm × 50 mm** 试片；**Nippon Denshoku A300/ZE-2000**；**3 次取平均** | 同上 Example [0059] |
| 实现叠层（实施例） | 内片亲水纺粘 18 g/m²；外片 = 拒水 SMS 11 g/m² + 无花纹白色透湿膜 18 g/m²；第一片亲水 SMS 10 g/m²；第二片拒水 SMS 11 g/m² | 同上 Example [0058] |
| 施胶量（实施例） | 固定 SAP 的第二胶 **3 g/m²**（满涂第二片）；封合区第三胶 **10 g/m²** | 同上 Example |
| 申请人 / 文献 | **Unicharm Corporation**（Ehime 799-0111, JP）；**EP 2 529 717 A1**，公开日 2012-12-05（A1 申请公开） | 同上 INID (71)(11)(43) |

> ⚠️ **禁止无来源参数**：表中每项均来自所列出处；未见于来源的一律写 `[待验证]`。特别注意：**15–65% 是本案的主张窗口，不是行业通用标准**，其他产品/材料的实测值本库目前**只有一个来源**。

> 🔴 **manual_review（2026-09-29）**：本页只整理**技术方案与实测数据**。以下 AI 不作结论：
> - **FTO / 侵权**：我方任一结构测得的整体全光线透过率是否落入 15–65% 并因此触及 EP 2 529 717 A1，须由专利代理或法务比对授权公告文本后独立评估。
> - **法律状态**：EP 2 529 717 A1 为 **A1 欧洲申请公开**（公开日 2012-12-05）；**是否被授予 B1、是否被修改限缩、是否维持有效及在哪些指定国生效，来源未记载 → `[待验证]`**（记录日期 2026-09-29）。
> - **测量不可比风险**：跨越不同仪器与取样尺寸的透光数据不可直接比较；比对前须统一到上述 50 mm × 50 mm / Nippon Denshoku A300-ZE2000 口径。

## Adjacent concepts 相邻概念

- 上位 / 相关：[[Fluff-Free 4th-Gen Absorbent Core（无木浆第四代芯体）]]（去绒毛浆是实现透光的前置条件）
- 相关：[[SMS复合结构]]（第一/第二片材均为 SMS）
- 并行路线（靠显色而非透光）：[[BM Urine Indicator Concept（尿+便双指示概念）]]、[[Titratable Acidity Lane（可滴定酸度通道）]]
- 反向机制：[[Geometric Optical Mask（几何光学掩膜）]]（刻意遮住 vs 本概念刻意透光）

## Sources 来源

- [[EP2529717A1 Disposable Absorbent Article with Excretion-Visible Core (Unicharm)]] —— `RAW/ima_sync/个人知识库/WKB/Areas/IP/04_模块一：SMMS_纺粘-熔喷-熔喷-纺粘无纺布_EP2529717A1_Disposable_absorbent_article_(亲水化SMS面层).pdf.md`

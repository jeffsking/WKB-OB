---
type: concept
title: "GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）"
domain: [卫材研发, 高吸水树脂, 测试方法]
status: stable
updated: 2026-09-29
tags: [SAP, GBP, CRC, 测试协议, DOE, 回渗, 选型]
aliases: ["测试协议依赖（Protocol-Dependent Ranking）", "GBP 受限 vs CRC 受限"]
---

# GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）

> One-line definition 一句话定义：**同一个芯体在不同测试工况下由不同机理主导**——高载短间隔（high-load / short-interval）工况受 **GBP（Gel Bed Permeability，凝胶床渗透率）** 限制，低载多次（low-load / multi-dose）工况受 **CRC（Centrifuge Retention Capacity，离心保水量）** 限制；选型的"胜负"因此会随协议翻转。
> (The dominant mechanism — and hence the ranking of SAP candidates — flips with the test protocol: high-load favours permeability (GBP), repeated low-dose favours capacity (CRC).)

## Mechanism 机理拆解

1. **GBP-limited regime 渗透受限**：单次大剂量 + 高载荷 + 短间隔（如 3.5 kg，80 ml × 3）时，液体必须在凝胶床中快速向下输运。此时**谁的 GBP 高谁赢**——KC 511 因 GBP 24 最高，凝胶床不阻塞，吸收速度最快（0 min 20.83 s / 20 min 18.50 s）。
2. **CRC-limited regime 容量受限**：多次小剂量 + 低载荷 + 长间隔（如 1.2–2.0 kg，60 ml × 4，34 min 终读）时，考验的是**总储液容量与抗饱和能力**。此时底层高 CRC 混配料（NR-950 CRC 36.7）在第 3–4 次加液后才释放储库，全面反超纯 511。
3. **Why the flip happens 为什么翻转**：两种工况考核的是互斥的材料属性——高 GBP 需要适度交联、孔径开放（牺牲部分 CRC）；高 CRC 需要低交联密度（牺牲通透）。因此**不存在"绝对最优牌号"，只有"在给定协议下最优"**。
4. **Practical trap 实务陷阱**：由单一协议得出的「单材最优」结论，换到另一协议即失效。文档中"全 511 最优"即高压短间隔协议的**伪峰（artifact）**，在贴近真实穿着的企标协议下被证伪。
5. **Confounding amplifier 混淆放大器**：若同时改变组成与结构变量（如同时对比率与添加剂取多个水平），两个 regime 的效应互相叠加，导致归因失败——见下「DOE 卫生」一节。

## Key data table 关键参数表

| Parameter 参数 | GBP-limited 渗透受限 | CRC-limited 容量受限 | Source 出处 |
|---|---|---|---|
| 典型协议 Typical protocol | 3.5 kg，80 ml × 3，3 min 间隔 | 1.2–2.0 kg，60 ml × 4，间隔 5/10 min，34 min 读数 | [[SAP Selection Decision Base（17-SAP选型与实验数据决策库）]] |
| Governing property 主导属性 | GBP（10⁻⁷ cm³·s/g） | CRC（g/g） | 同上 |
| 优势方 Winner | 全 511（KC511 GBP 24，最高） | 多 SAP 混底（底层 CRC 30.8–36.7） | 同上 |
| 实证读数 Evidence | 吸速 20.83 / 18.50 s（0 / 20 min） | 企标回渗 @34 min：930/住友 4.325 g < 511/951+959 5.582 g < 全511 8.363 g < 全511(3/7) 11.270 g | 同上 |
| GBP 分档 GBP bands | 高渗透型 30–50；平衡型 10–30；高容量型 <10 | — | 同上 |
| CRC 分档 CRC bands | — | 高容量型 38–45；平衡型 30–36；高渗透型 25–30 | 同上 |

> ⚠️ **禁止无来源参数 No unsourced numbers**：表中每个数字均来自上列出处；未给出的写 `[待验证]`。

## DOE hygiene 实验设计卫生（同 Buchanan 一并咬合）

> 本节来自同一批文档的**混淆地图（confounding map）**：8 个配方单元中仅 5 组可作干净对比（clean comparison）。原理与本 regime 概念同源——**只有隔离变量，才能说清是哪个 regime 在起作用**。

| Cell 单元 | Design status 设计状态 | Usability 可用性 |
|---|---|---|
| 全511 5/5 vs 3/7 | CLEAN（比率隔离） | 可估比率效应 |
| 511/951 vs +959 | CLEAN（仅添加剂变） | 可估 959 效应 |
| 511/951 vs +610S | CLEAN（仅添加剂变） | 可估 610S 效应 |
| 511/951+N8（3/7） | FULLY CONFOUNDED | 不可归因，N8 效应无法孤立 |
| 930/住友 | STRUCTURAL OUTLIER | 作独立参照，排除出 511 系列排序 |

- **留一法异常 Leave-one-out outliers**：511/951+N8 的 8 min 速度封顶 90 s（z = +4.15）与企标 12 min 60 s（全场最高）被判 **CRITICAL** —— 定性为**配方级失效**而非普通离群值，应剔除或重做，不得计入均值。
- **批次混淆 Batch confound**：全 511(5/5) 对照组于 2026-06-19 单独早测 1 个月（其余在 7/16–7/18），构成 CN-4 WARN，横向前须同批重测或做批次校正。

## Adjacent concepts 相邻概念

- 上位 Upstream：[[SAP性能指标（CRC AUL GBP Vortex）]]、[[芯体测试方法与验收基准（STM）]]
- 机理下游 Downstream：[[SAP错峰膨胀]]（错峰即在**同一工况内**用溶胀快慢比制造时间维度的通道冗余；其真实验证仍需 bench 序列加液，而非单点 free-swell）
- 结构耦合 Structural coupling：[[分区密度设计]]、[[REL增强层]]、[[COCO芯体平台]]
- 组合落点 Portfolio：[[IPC BCC OI Portfolio（开放创新项目组合）]]

## Verification log 验证记录

> ✅ 建立（2026-09-29，来源 [[SAP Selection Decision Base（17-SAP选型与实验数据决策库）]]）：三套协议（企标 / 新国标 / 盐水三次加液）在同一组幸运配方上给出**互不一致的排序**，构成本页概念的原始证据；「全 511 最优」被明确标注为高压短间隔假象。
> ⚠️ **manual_review（2026-09-29）**：该资料同时给出 SAP 牌号单价与单片成本（US¢1.90/片），属商务敏感信息，**本页不引用具体报价**；如需成本口径请人工决定是否引入。

## Lessons learned 经验教训

- **Bench protocols are not interchangeable 协议不可互换**：换协议 = 换选型结论，落地前必须锁定代表真实穿着的主 KPI（文档中为企标 @34 min 回渗）。
- **Single free-swell numbers lie 单点自由溶胀会骗人**：两个截然不同配方的单点 free-swell 可能完全相同，只有**顺序 4 次冲击（gush）序列测试**才能暴露差异。
- **Fix the axis before adding parts 先锁轴线再加变量**：文档中「顶/底比率」是第一主导轴（3/7 vs 5/5：扩散 +0.354 / 留存 −0.351），在未锁定比率前叠加添加剂，得到的都是混淆效应。
- **No replicates ⇒ no statistics 无重复即无统计量**：8 单元无组内重复，只能做 Spearman 相关（0.81–0.90）与秩次判断，**不得宣称统计显著**。

## 追加：Meeting Minutes 批（2026-09-29 追加 · 供应商侧"牺牲 CRC 换 GBP"的工艺上限）

> 来源：[[SAP GBP Improvement & Surface Crosslinking Process Review（GDP提升工艺探讨）]]（SAP 供应商工厂交流 ASR 转写，会议日期 [待验证]）。本批只**追加**，不修改既有结论。

**供给侧的三条提升路径与其共同上限（本批新增）：**

| 路径 | 本质 | 上限 |
| --- | --- | --- |
| **表面离子交联** | 前段工艺包 | 主要手段，但单一手段有天花板 |
| **后段多价金属盐涂层** | 金属离子与羧基交联，**属表面交联的一种** | **做过、未商业化**；效果到一定程度后难以继续提升 |
| **无机粉末撒粉** | 大线设备段 | 与多价金属盐"表象基本一致"，同样有上限 |

> 供应商口径："**提升到一定的程度之后，如果单纯地去靠它去增加它的 GBP，是比较困难的**。"
> 会中量级：**GBP 约 40**（在相应保水水平下）。

**"牺牲 CRC 换 GBP"的可行性与条件（本批新增）：**

- 前提：本方**对保水（CRC）的要求不是那么高** → 于是"保水这一块可以**牺牲掉一部分**，用来提升我们的通液（GBP）"。
- 这是一条**明确的交换曲线**：GBP 不是免费提升的，其代价是 CRC；本页既有的"GBP-limited vs CRC-limited"两区在此得到供给侧的工艺印证。
- ⚠️ 反向确认：若对现有牌号做后处理，"**通用性会更好一点，但去除量（吸收量）会降低**" —— 与本页机理一致。

**由此得到的认知（本批新增）：**

1. **GBP 的上限不是设计出来的，是工艺段决定的** —— 三条路径殊途同归，说明瓶颈在**表面交联化学本身**，而不是手段选择。
2. **换 GBP 的货币是 CRC** —— 只有当产品对保水不敏感时，GBP 提升才有空间；这解释了为什么"上层通液好"的思路会与"上层高保水"的常规思路冲突。
3. **分层结构让取舍可以分区进行** —— 不必在一颗 SAP 上同时拿高 CRC 与高 GBP，可上层/下层分工（见 [[Multilayer SAP Core（多层SAP芯体）]]）。

✅ **验证记录（2026-09-29）**：GBP≈40 与"到一定程度难以继续提升"为**会中口径**，无第三方数据；多价金属盐涂层"未商业化"的原因**未披露** [待验证]。参见 [[诺尔（Nuoer）]]、[[SAP性能指标（CRC AUL GBP Vortex）]]。

## Sources 来源

- [[SAP Selection Decision Base（17-SAP选型与实验数据决策库）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/17-SAP选型与实验数据决策库.docx.md`

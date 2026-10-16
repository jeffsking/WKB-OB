---
type: concept
title: "Use-Test Loading & Leakage Percentile（使用测试载荷与渗漏分位）"
domain: [卫材研发, 测试与验收, 成人护理]
status: growing
updated: 2026-09-30
tags: [HUT, single insult, loading, LD50, 渗漏, 容量设计, 成人护理]
aliases: ["使用测试载荷分位", "Single Insult Distribution", "LD50（半数渗漏载荷）"]
---

# Use-Test Loading & Leakage Percentile（使用测试载荷与渗漏分位）

> One-line definition 一句话定义：把**家庭使用测试（HUT）采集到的消费者实态**整理成三条可执行的设计曲线——**单次排尿量分位（single insult）**、**累积载荷分位（loading）**、**半数渗漏载荷（LD50）与渗漏率**——并据此反推出 bench 加液量与产品容量目标。
> (Home-use-test data distilled into three actionable curves — per-void volume percentiles, cumulative load percentiles and leakage LD50 — from which bench insult sizes and product capacity targets are derived.)

## Mechanism 机理拆解

1. **三条曲线，三种用途 Three curves, three jobs**：
   - **Single insult（单次排尿量）** → 决定 **bench 测试的冲击量**，并为吸收体的瞬时空隙（void volume）设计提供输入。
   - **Product loading（累积载荷）** → 决定产品在正常使用周期中**需要多大容量（capacity）**。
   - **Leakage（LD50 / 渗漏率）** → 给出**渗漏风险的载荷阈值**，用于容量上限校核。
2. **采集方式 How single insult is measured**：单次排尿量研究是一类**特殊 HUT**——要求使用者在产品被加载后立刻取下产品并称重，由此得到一次排尿的真实体积分布。
3. **抽样陷阱 The sampling trap**：若把研究中的**渗漏样本排除**，所得分布会被系统性低估（渗漏的产品恰恰是载荷最高的一批）；反之，若只按 Load–Leak 分位设计，又会**高估**容量需求。正确做法是**三条并存对比**：Load–All / Load–Leak / Load–No Leak。
4. **分布重叠会吞掉产品分层 Overlap collapses tiering**：当相邻等级产品的载荷分布显著重叠时，用「容量」做等级区隔失效，必须改用**摄入速度 / 干爽 / 贴合**等其他维度做产品定位。
5. **与婴儿线的差异 vs baby lines**：成人失禁线的加液量直接源自 **ULS / HUT 第 95 百分位总载量 ÷ 单次冲击量**（单次冲击量取整到 5 mL），因此**加液参数随品类锁死、不可跨品类套用**。

## Key parameters 关键参数表

| Parameter 参数 | Typical practice / value 典型做法与取值 | Source 出处 |
|---|---|---|
| Single insult 用途 | 决定 bench 冲击量与 void volume 设计输入 | [[R150540-TL-14137 Poise Use-Test Load & Leakage Summary（2009）]] |
| Loading 用途 | 决定产品容量目标（capacity） | 同上 |
| Leakage 用途 | LD50 与渗漏率用于容量上限与风险校核 | 同上 |
| Loading 取位 Design percentile | 下游加液表以 **95% 分位**为基准取值 | [[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]] |
| 单次冲击量取整 | 取整到 **5 mL** | 同上 |
| 并列对比要求 | Load–All / Load–Leak / Load–No Leak **三组分位必须并存** | [[R150540-TL-14137 Poise Use-Test Load & Leakage Summary（2009）]] |
| 样本规模（Single insult） | N(insults) 数百至逾千；N(subjects) 数十至上百 | 同上 |
| 更新节奏 Update cadence | 该类汇总约每 4–5 年更新一次（上一版 TL-11541 为 2005 年） | 同上 |

> ⚠️ **禁止无来源参数**：本页所有做法描述均来自上列两个源摘要页。**因源为 K-C CONFIDENTIAL 内部报告，本页不复制具体产品的分位数值与 LD50 明细**；需要具体数值时应经法务确认后回到 [[R150540-TL-14137 Poise Use-Test Load & Leakage Summary（2009）]] 所指认的原文。

## Adjacent concepts 相邻概念

- 下游方法 Downstream methods：[[Bladder Box Intake Test（膀胱箱压载摄入测试）]]、[[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]]、[[Rewet Test（回渗测试）]]
- 同类失效口径 Failure metrics：[[Run-off & Leakage Test（滑渗与渗漏测试）]]、[[Blowout Leakage Test（爆漏测试）]]
- 通用方法论 General discipline：[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]（protocol 决定结论）
- 物理核验 Physical simulation：[[Mannequin BM Test（BM 假人测试）]]、[[Static Mannequin Test（静态假人测试）]]

## Verification log 验证记录

> ✅ 建立（2026-09-29，来源 [[R150540-TL-14137 Poise Use-Test Load & Leakage Summary（2009）]]、[[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]]）：两份来源构成完整的「使用数据 → bench 参数」链条——前者产出三条曲线，后者在 95% 分位处取值生成加液表。
> 🔴 **manual_review（2026-09-29）**：源资料为 **K-C CONFIDENTIAL**，本页仅登记方法学，**不含任何具体数值明细**；对外使用须经法务与 QA 确认。

## Lessons learned 经验教训

- **不要把统计口径当默认值**：同一份数据，取 Load–All / Load–Leak / Load–No Leak 会给出差异巨大的目标值；写需求时必须指明取哪一列。
- **排除渗漏样本＝自我安慰**：剔除最差样本会让分布更好看，但由此定出的容量会在真实使用中被击穿。
- **分布重叠是产品分层的红灯**：当相邻等级载荷分布显著重叠，继续堆容量做等级区隔是无效投资。
- **注意数据年份**：使用实态数据会随人群与产品形态变化，该类汇总约每 4–5 年更新一次，长期使用须核实版本年份。

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · "3 次加液"的统计学来源）

> 追加来源 `[[FIUP Insult Amounts（FIUP 加液量阶梯与 TL 溯源）]]`（K-C 内部方法定义与溯源索引）。本段**只补"分位口径如何落成测试加液量"，不改动上方任何结论**。

### 1. ✅ 本页主题的直接落地：75 百分位总载荷 → ÷3 → 单次加液

原表脚注原句：*"**75ᵗʰ percentile total loadings from ULS 34724 divided into 3**"*（取自 2012 年尿液载荷研究 **ULS 34724** 的 75 百分位总载荷，均分为 3 次）。Poise 侧同注：*"FIUP TL says it uses 75th percentile total pad loading divided in 3"*。

| 档位 | Micro | Liner | UT | Mod | Max | Ult |
|---|---|---|---|---|---|---|
| **Total Load 总载荷（mL）** | 3 | 6 | 12 | **30** | **78** | **114** |
| **Single Insult 单次加液（mL）** | 1 | 2 | 4 | **10** | **26** | **38** |
| 加液次数 | **3** | 3 | 3 | 3 | 3 | 3 |

> ✅ **与本页主题的关系**：本页此前的教训是"**不要把统计口径当默认值**"。本批给出了**正面的完整链条**——**分位（75th）→ 总载荷 → 除以加液次数 → 单次加液**，且每一步都有编号可回溯（ULS 34724 → TTM-00643 v0）。这是"统计口径必须显式声明"的**最佳实践样本**。

### 2. 口径沿革（四代方法，1999 → 2017）

| 方法 / 年份 | Micro | Liner | UT | Mod | Max | Ult | 参考 |
|---|---|---|---|---|---|---|---|
| FIFE Flowback（1999–2005） | n/a | n/a | n/a | **30** | **30** | **30** | STM-2414 v4 / STM-00034 v0 |
| New Ad Claim Method（2014） | — | — | — | 30 | 78 | 114 | TOMLIN Ad Claim Justification |
| Draft STM-00497（2015） | 3 | **9 → 6** | 12 | 30 | 78 | 114 | TL-15927 |
| **FIUP（2017）** | 3 | 6 | 12 | 30 | 78 | 114 | **TTM-00643 v0 – ad claim** |

- ⚠️ 早期（1999–2005）**Micro/Liner/UT 三档为 n/a、中高三档统一 30** —— 即**不区分中高档**；2014 起才分档。
- ⚠️ 2015 草案曾把 **Liner 档设为 9、后改为 6**，是沿革中唯一可见的档位调整痕迹。

### 3. ⚠️ Long 规格的基准切换（本页"数据年份"教训的新实例）

| 品类 / 规格 | 总载荷基准 |
|---|---|
| Depend（DPU1 / DPU2·DSU2 / DAU·DRU2 / Briefs / GFM） | **ULS 34724（2012）** |
| Poise Liners / UT | **ULS 34724（2012）** |
| Poise **Mod–Ult 的 Long 规格** | 改用 **HUT**：Mod Long = HUT 36445（2014）；Max = HUT A83750（2003）；Max Long = HUT 31142（2007）；Ult = HUT 35609（2014） |

> **原因**：**ULS 34724 未区分 regular 与 long**，故 Long 规格另用 HUT。→ 这正印证本页 Lesson「**注意数据年份**」：不仅年份会变，**同一研究对不同规格的覆盖度也不同**，混用会引入系统性偏差。

### 4. 当前（2026）Poise 尺码命名体系（1D–8D）

`1D Microliners` ｜ `2D Liners` ｜ `3D Light` ｜ `3DL Light Long` ｜ `4D Moderate` ｜ `4DL Mod Long` ｜ `5D Maximum` ｜ `5DL Max Long` ｜ `6D Ultimate` ｜ `6DL Ult Long` ｜ `6DL+ Ult Long+` ｜ `7DL Ult Long` ｜ `8D Ex Cov Ovn`。

> 命名关键变更节点：2008 C4（**Extra = Moderate，Ultra = Maximum**，新增 Ultimate）→ 2011 CHANEL（Hourglass）→ 2014 NORMA（microliners）→ 2015 TOMLIN（Thin Shape 取代 Hourglass，**并开发 FIUP 前体方法 TL-15927**）→ 2016 LOPEZ（3D Light，对标 AD Ultrathin）→ 2017 RAY（Overnight，2018 CALVIN 更名 Ultimate Long）→ 2018 HOBBES（Thin Shape → Ultra Thin）。

> ✅ 验证（2026-09-29）：本追加段**未修正**上方任何结论；上方四条经验教训（统计口径勿当默认值 / 排除渗漏样本＝自我安慰 / 分布重叠是红灯 / 注意数据年份）**全部未被触及**，且第 1、3 条在本批获得**新的实证支持**。
> 🔴 **manual_review（2026-09-29）**：本源含 **K-C 内部研究编号（A-xxxxx / HUT / ULS / TL / STM）与 Poise 项目代号年表（2006–2026）**。依 AGENTS.md §5，本页**只记加液口径、溯源结构与命名沿革**，**不落内部研究数据与未公开项目细节**。

## Sources 来源

- [[R150540-TL-14137 Poise Use-Test Load & Leakage Summary（2009）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Test Methods/FIUP - TTM-00643/FIUP Research Docs/R150540_TL-14137_Summary of POISE Use Test Load and Leakage Data (2009).pdf.md`
- [[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Test Methods/FIUP - TTM-00643/Intake via Bladder Box draft STM-00497 - Copy.docx.md`

---

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · 「载荷目标会过期」与招募口径风险）

> 追加来源：[[R160739 TL-15582（单次加液与总载荷目标的方法学更新 · 2015）]]（`RAW/.../R160739_TL-15582_Updated Approaches for Defining DEPEND and POISE Single Insult and Total Product Loading Targets.pdf.md`，**K-C CONFIDENTIAL**）。
> **本追加不修正上方任何结论**；上方四条经验教训中**第 1 条（统计口径勿当默认值）与第 4 条（注意数据年份）**在本批获得**最直接的制度性支持**——**数据年份不是提示，而是有明文更新周期的硬要求**。
> 🔴 **manual_review（2026-09-29）**：本源为 **K-C CONFIDENTIAL**，含内部研究编号（Study 35493 / DPU2 / 4SPS）与分发名单；本页**不落分发名单中的个人姓名**，**不引用具体载荷数值**（本件仅含封面与附录清单，POV 正文不在文件内）。

### 追加-1 · ★ 载荷目标有「保质期」：明文要求每 5 年更新

| 输入项 | 更新周期 | 依据 |
|---|---|---|
| **单次加液载荷（single insult loading）** | **至少每 5 年变化一次** ⇒ 须同步更新 | 历史观察 |
| **总产品载荷（total product loading）** | 每 5 年 | 建议 |
| **加液次数（number of insults）** | 每 5 年 | 建议 |
| **润湿形态（wetting pattern）** | 每 5 年 | 建议 |
| **理想复核时机** | **新的 Urine Loss Spectrum（ULS）研究之后** | 建议 |

> 📌 **对上方第 4 条（注意数据年份）的加强**：上方把「年份」作为**提醒**；本追加给出**制度依据**——**四类输入均有 5 年更新周期要求**。⇒ **引用任何载荷值时，应记录其测定年份；超过 5 年未复核的载荷目标应视为「待更新」，而不是「既定值」。**

### 追加-2 · ★ 招募人群偏差：载荷是「招募敏感」的（**对本页最关键的增量**）

**实证（原文）**：**DPU2 上的新单次加液研究（Study 35493）与随后的 HUT 得到的载荷低于既往研究** ⇒ 引发**对招募人群结构（recruit demographics）的质疑** ⇒ 直接导致 2013 年后期 **DEPEND Leakage 4SPS HUT 改变招募做法**。

> ⚠️ **对本页的直接约束（新增第 5 条风险）**：
> **跨研究比较载荷值之前，必须先核对招募人群口径。** 否则极易把「**招募差异**」误读为「**产品差异**」——这与上方第 3 条「分布重叠是红灯」属**同一类混淆**，只是来源从**统计口径**换成了**人群口径**。
>
> ⇒ **本页在引用或列出载荷数据时，应把「招募人群口径」与「测定年份」并列记录**。

### 追加-3 · 方法学降本：把目标维护内嵌进既有 HUT

**做法**：在 **DEPEND Leakage 4SPS HUT** 中新增一道自报题——**"请报告每片产品经历的加液次数（若可察觉）"** ⇒ 生成**大样本量的单次加液数据库** ⇒ **无需新增使用研究、无需可自由支配经费**即可持续刷新目标。

> 📌 **可迁移价值**：这是一条**通用的实验设计原则**——**把目标值的维护成本内嵌进既有必做流程**，而不是单独立项。对本库而言：**任何需要周期性更新的目标值（载荷、加液量、回渗目标）都应检查「能否搭车既有测试」**。

### 追加-4 · ⚠️ 本源的取值边界（避免误引）

- 本 PDF **仅含封面、分发名单、摘要、目录、引言、建议与附录清单**；**六份 POV 正文（AI–AVI）不在文件内** ⇒ **本追加不含任何具体载荷数值**。
- 其中 **AIV「Protocol Impacts on TTM-00148 Results」**直接处理**协议变化对开式 Cradle 摄入结果的影响** ⇒ 与 [[Cradle Intake Test（Cradle 摄入测试）]]、[[Rewet Test（回渗测试）]] 的方法学争议**同一议题链**，**待该 POV 原件入库后再补**。
- **AV / AVI**（截至 **2014-12-16** 的单次加液载荷目标与总产品载荷假设）同样**未随本文件提供**。

> ✅ 验证（2026-09-29）：本追加段**未修正**上方任何结论；上方四条经验教训**全部保留**，本批补的是**更新周期的制度依据、招募人群口径风险、以及目标维护的降本方法**。

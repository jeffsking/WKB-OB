---
type: concept
title: "Resilient Surge（PET 回弹导流层）"
domain: [卫材研发, 导流层]
status: seed
updated: 2026-09-29
tags: [resilient surge, MOJAVE, CT5, PET, 回弹, 加工性, 断头, 粉尘]
aliases: ["回弹导流层", "Resilient Surge", "MOJAVE 导流层"]
---

# Resilient Surge（PET 回弹导流层）

> 一句话定义：用 **PET（而非聚烯烃）承担回弹**的导流层路线——PET 越多的导流层在受压后越能"弹回"，把液体继续往下送并压住回渗；代价是 **PET 不易粘结 → 纤网变弱 → 断头、粉尘、幅宽波动全面恶化**，因此这条路线的真实命题不是"要不要 PET"，而是"如何在不加工性崩掉的前提下把 PET 加上去"。

## 机理 / 结构拆解

1. **回弹为什么能降回渗**：回渗的本质是受压后结构塌陷、把已吸收的液体挤回面层。PET 纤维的弯曲回弹率显著高于聚烯烃，受压卸载后能重建导流层下的**空隙（void）**，断掉"液体被挤回贴肤侧"的通路。这是 MOJAVE 相对 HPP / PICASSO 回渗从 2.96 g 降到 0.82 g 的直接原因。
2. **PET 含量是单参数的双刃**：PET 越多 → 使用中表现越好、单位面积成本越低（PET 原料便宜且可用更低克重维持性能）；同时 PET 越多 → 纤网越弱。BCC 产线的**工艺窗口下限于 3,000–6,000 gf**，纤网强度一旦跌破窗口，加工侧就表现为断头。
3. **代价三项是一组共因症状**：断头（breaks/day/asset）、粉尘（dust, g/MSU）、幅宽波动（width range, mm）**同时恶化**，因为它们同源——纤维间粘合点不足。因此评估一个回弹导流层牌号时，**三项必须一起看**，只看回渗会把加工风险隐藏掉。
4. **解法不在"少加 PET"，而在配方与工艺的再平衡**：MOJAVE 2.1 保留了 40% 的 G75 中空 coPET，把粘结纤维从单一 5.3d PE/PP bico 60% 改为 **5.3d 40% + 1.5d 20%**（引入更细的粘结纤维增加粘合点数量），并把目标厚度从 0.180 in 压到 **0.130 in**；结果是断头回到 0.60、粉尘降到 158、幅宽波动降到 5.73 mm，而**回渗几乎不变（0.86 g）**——**性能与加工性不是必须互换的，关键是粘合点密度而非 PET 比例**。
5. **哪些工艺变量真的有用**：提高 TAB 烘箱温度**无效**；提高 TAB + 压辊压力**有效**；**降低粘结纤维平均旦数有效**、**缩短纤维长度有效**、**加长纤维反而不利**；热刀分切**有效**（针对粉尘与边缘）。这套结果指向同一结论——**增加有效粘合点、缩短纤维自由端**。
6. **成本逻辑是"降克重"而非"换便宜料"**：PET 路线的一条降本路径是**在维持性能的前提下降低克重**；另一条是认证第二货源（coPET 纤维），把单点供应风险与议价空间同时解决。
7. **与芯体存在匹配关系**：同一导流层在不同芯体上的档位不同——CT5（100% PET）在 **SAM/Fluff 芯体上摄入与回渗均最佳**，但在 **AT hybrid 芯体上仅与 MOJAVE 持平**。即回弹导流层的收益依赖芯体能否接住它送下来的液体。

## 关键参数表

| 参数 Parameter | 典型值 / 范围 Value | 出处 Source |
|---|---|---|
| MOJAVE 配方 | 40% 中空 coPET（G75）+ 60% 5.3d PE/PP 双组分粘结纤维；PET 含量 40% | [[Intake Systems Tech Pipeline - Archive（摄入系统技术管线·汇编存档）]] |
| MOJAVE 2.1 配方 | G75 coPET 40% + 5.3d PE/PP bico 40% + **1.5d PE/PP bico 20%** | 同上 |
| 目标厚度 | MOJAVE 0.180 in → MOJAVE 2.1 **0.130 in** | 同上 |
| 强度 Strength | MOJAVE 基材 10,000 gf / 接头 8,000 gf；CT5（100% PET）5,700 / 5,300 gf | 同上 |
| 产线工艺窗口下限 | BCC 设备 **3,000–6,000 gf** | 同上 |
| 回渗 Rewet（Snug & Dry） | PICASSO 2.96 g → MOJAVE **0.82 g** → MOJAVE 2.1 0.86 g | 同上 |
| 断头 Breaks/Day/Asset | PICASSO 0.62 → MOJAVE **1.28** → MOJAVE 2.1 0.60 | 同上 |
| 粉尘 Dust (g/MSU) | PICASSO 53 → MOJAVE **212** → MOJAVE 2.1 158 | 同上 |
| 幅宽波动 Width range (mm) | PICASSO 6.90 → MOJAVE **9.67** → MOJAVE 2.1 5.73 | 同上 |
| 芯体匹配 | CT5 在 SAM/Fluff 上摄入/回渗 Best；在 AT hybrid 上与 MOJAVE 同为 Better | 同上 |
| 成本方向（相对） | PET 含量越高单位面积成本越低；同一牌号不同供应商报价可差约 25%（内部报价，见 manual_review） | 同上 |

> ⚠️ **禁止无来源参数**：上表数值**全部来自同一份内部汇编 PPT**（[[Intake Systems Tech Pipeline - Archive（摄入系统技术管线·汇编存档）]]），**尚无第二来源交叉验证**；"回弹率 ↔ 回渗"的定量函数、**1.5d/2.0d 粘结纤维比例的最优解**在本库中缺失，标 `[待验证]`。
> 🔴 **商务敏感 Business-sensitive**：单位面积报价、供应商价差与年化节省金额属内部商务信息，**本页只记相对方向与百分比量级**，不落绝对价格；原始数值留存于源摘要页。

## 相邻概念

- 同层不同路线：[[ADL（导流层）]]（导流层的通用定义与指标）、[[REL增强层]]（芯体侧收集传递层，与导流层易混名）
- 结构耦合：[[Liner-Surge Embossing（面层-导流层压花）]]（面层与导流层的压花耦合；本页 PICASSO 为其上游材料）
- 机理同族：[[毛细梯度设计]]（用结构梯度替代单一材料指标；回弹是"抗压保梯度"的实现手段之一）
- 判读前提：[[Rewet Method Comparison（回渗测试方法横向对比）]]（回渗值随方法变化，跨页比较须先对齐口径）

## 经验教训

> ✅ 验证（2026-09-29，来源 [[Intake Systems Tech Pipeline - Archive（摄入系统技术管线·汇编存档）]]）：本页为新概念页，首条来源即给出一条可迁移的判断——**"性能提升伴随加工性恶化"不是必须接受的宿命**：MOJAVE 2.1 在**不降低 PET 含量**的前提下把三项加工指标全部拉回对照水平，说明**粘合点密度（细旦粘结纤维 + 压力 + 短纤维）才是可操作变量**。

- **教训**：**新牌号评估必须把"加工性三项"写进同一张验收表**。MOJAVE 之所以要出 2.1，是因为首轮只把回渗当作成功标准，断头翻倍与粉尘 4 倍要到上机后才暴露。
- **教训**：**"提高烘箱温度"是最容易被误用的第一反应**——本例中它明确无效，真正有效的是压力与纤维形态（旦数、长度）。温度解决的是"熔不熔"，本例的问题是"粘合点够不够"。
- **教训**：**单一货源是这条路线的隐性单点故障**——coPET 纤维的第二货源认证被列为下一步事项，与成本并列。
- **待补 `[待验证]`**：PET 含量 ↔ 回渗的定量曲线；不同芯体（含浆 / AT hybrid / 全 SAP）下的最优 PET 比例；MOJAVE 2.1 用 **2.0d 替代 1.5d 以消除 neps（棉结）** 的验证结果。

## 追加：Open Innovation 批（2026-09-29 追加 · 2023 年摄入系统通路中的定位）

> 追加来源 `[[Intake Systems Development Pathway 2023（摄入系统开发通路）]]`（2023-02，内文自注 Updated August 2023）。本段**只补"该路线在 2023 年通路图中的位置"，不改动上文任何配方、性能与加工性结论**。

### 1. 在通路图中的 TRL 定位

| 项 | 源文表述 |
|---|---|
| TRL 档 | **TRL 5+（已落地档）**，列为 "Resilient Surges (GNW, Shalag, etc.)" |
| 出现议题 | **Dryness 干爽**、**Body Conforming Fit 贴体合身**（"Resilient surges, Airlaid intake layers"） |
| 关联供应方 | **GNW、Shalag 等**（源文以 "etc." 收尾，家数未枚举） |

> ✅ **与上文一致**：上文以 MOJAVE / CT5 为主线给出该路线的**技术机理与加工性代价**，本追加段给出的是**组织层面的成熟度判断**——两者互补，不冲突。

### 2. 该路线的"跨议题复用"属性

- 回弹导流层在 2023 通路图中**同时服务于两个不同收益**：**干爽**（抗压保空隙 → 断掉回挤通路）与**贴体合身**（作为 airlaid 的低成本替代候选）。
- ⚠️ **口径提示**：源文在 Body Conforming Fit 议题下把 **"Resilient surges" 与 "Airlaid intake layers" 并列**写入 TRL 5+，但**未说明二者是否为同一方案的替代关系**；本页**照录并列，不推断替代关系**。

### 3. ⚠️ 并列记录：ActivTech 2.0 与回弹导流层是两条不同的线

- 同一份通路图中，**ActivTech 2.0**（intake/dryness、surge & facings）被放在 **TRL 1–2**，而 **Resilient Surges** 在 **TRL 5+**。
- **不因此推断二者优劣**：前者是芯体/结构平台项目，后者是材料路线，**评价维度不同**。

> 🔴 **manual_review（2026-09-29）**：本源为 KC 内部战略规划汇报，TRL 为**内部自评**、项目状态为**时点快照**；引用须注明 2023-02（Updated August 2023）。

## 来源

- [[Intake Systems Tech Pipeline - Archive（摄入系统技术管线·汇编存档）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Intake/Intake Systems Tech Pipeline - Archive.pptx.md`
- [[Intake Systems Development Pathway 2023（摄入系统开发通路）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Intake/Liner-Surge Pathway - Feb 2023.pptx.md`（2026-09-29 追加）

---
type: source
title: "Viscoelastic Properties of Amorphous Polymers Book"
source_type: book-index
author: ""
edition: ""
publisher: ""
year: 0
isbn: ""
original_language: "EN"
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/VISCOELASTIC_PROPERTIES_OF_AMORPHOUS_POL.pdf.md"
date_published: 0
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
summary_cn: "无定形聚合物粘弹性教学讲义（作者/出版信息未标注）——按『时温等效 → 四区域黏弹行为 → 力学模型（弹簧+阻尼）→ Maxwell 模型求解』的次序讲清模量随温度/时间跨越十数量级的成因，并给出 DMA 的 tan δ 峰是 Tg 判据的实操口径。"
key_claims:
  - "无定形聚合物的黏弹性行为分为四个区域（原文标题 AMORPHOUS POLYMERS - THE FOUR REGIONS OF VISCOELASTIC BEHAVIOUR）：Glassy State（构象变化被严重抑制）→ Tg 区（链段协同运动开始但迟缓，DMA 中 tan δ 出现极大值）→ Rubbery plateau（时间尺度变短但仍长于解缠结时间）→ Terminal flow（解缠结时间尺度变短、熔体行为更像流体）。"
  - "时温等效原理（TIME TEMPERATURE EQUIVALENCE）：以『10 sec modulus』的 Log E vs Temperature 图示表述——升高温度等价于延长观察时间，可用短时间变温实验代替长时间等温实验；同一图给出 Glassy region、Rubbery plateau、Cross-linked elastomers、Melt、Low molecular weight 的相对位置。"
  - "本构定义（## DEFINITIONS）：松弛模量 G(t) = τ(t)/γ₀；蠕变柔量 J(t) = γ(t)/τ₀；源文件原文明确写作 **G(t) ≠ 1/J(t)**（两者不等），且声明『We will only consider LINEAR MODELS』——即把处理限制在小载荷、小应变下的线性范围。"
  - "Maxwell 模型推导（原文）：由 Hooke 弹簧 σ = Eε 与 Newtonian 阻尼 σ = η(dε/dt) 串联，得 dε/dt = σ/η + (1/E)(dσ/dt)；在应力松弛条件 dε/dt = 0 下解得 σ = σ₀ exp[−t/τ_t]，其中 τ_t = η/E（Relaxation time 松弛时间）。"
  - "模型适用边界（原文对比图）：单 Maxwell 元的指数松弛无法拟合真实聚合物 S 形的 Log E(t) vs Log time 曲线（低分子量与高分子量两条曲线在长时区显著分叉），真实响应需要连续松弛时间谱/广义 Maxwell 表述。"
  - "半结晶聚合物的黏弹性不能照搬无定形结论（SEMI-CRYSTALLINE POLYMERS 节）：非晶域运动受晶区约束、Tg 以上常出现结晶与非晶的耦合过程，原文明确『Less easy to generalize - polymers often have to be considered individually』；该节 DMA 数据（LPE 与 LDPE 的 G′ 与 tan δ 温度谱）标注 Reproduced with permission from H. A. Flocke, Kolloid-Z. Z. Polym., 180, 188 (1962)。"
tags: ["source/book", "source/book-index", "viscoelasticity", "amorphous-polymer", "glass-transition", "maxwell-model", "relaxation-modulus", "creep-compliance", "time-temperature-equivalence", "DMA", "tan-delta"]
tags_zh: ["粘弹性", "无定形聚合物", "玻璃化转变", "麦克斯韦模型", "松弛模量", "蠕变柔量", "时温等效", "动态力学分析"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Viscoelastic Properties of Amorphous Polymers]]", "[[Ebewole Polymer Science Ch14 Polymer Viscoelasticity]]", "[[Origin of Rubber Elasticity Book]]", "[[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]]", "[[Introduction to Physical Polymer Science]]", "[[Polymer Testing Handbook]]"]
---

# Viscoelastic Properties of Amorphous Polymers Book

*Author/Editor 未标注 — Publisher 未标注, 未标注*

> Book index 书籍索引页。源文件为教学讲义（幻灯片体，OCR 抽取质量一般，标题存在断字如 `VI SCOELASTI C`）。本页只做整篇定位与口径固化；同一源文的逐行深度拆解见 [[Viscoelastic Properties of Amorphous Polymers]]。

## Book Metadata 书籍元数据

| 字段 Field | 值 Value |
|---|---|
| Author 作者 | 未标注 |
| Edition 版次 | 未标注 |
| Publisher 出版社 | 未标注 |
| Year 年份 | 未标注（源文件无出版年） |
| ISBN | 未标注 |
| Document type 文献类型 | 教学讲义 / 课件（幻灯片体，含大量图片占位 `[图片: ...]` 与三线表） |
| Original Language 原文语种 | EN |
| Source 源文件 | `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/VISCOELASTIC_PROPERTIES_OF_AMORPHOUS_POL.pdf.md`（7,002 bytes） |
| 唯一可溯源引文 | H. A. Flocke, *Kolloid-Z. Z. Polym.*, **180**, 188 (1962)（半结晶聚合物 DMA 图，源文件标注 Reproduced with permission） |

## Scope and Structure 范围与结构

讲义用一条很朴素的逻辑线解释一个反直觉现象：**同一块无定形聚合物，其模量为什么能横跨十多个数量级**。答案是模量不是常数，而是时间的函数（松弛），而温度与时间可以互相换算（时温等效）。随后用弹簧 + 阻尼两个机械元件搭出 Maxwell 模型，把「松弛」变成一个可解的微分方程，最后诚实地展示该模型与真实数据的差距。

原文结构（源文件 `^#{1,3} ` 标题序列，保留原始断字）：

| 序 | Slide/Section 标题（原文） | 内容 Content |
|---|---|---|
| 1 | VI SCOELASTI C PROPERTI ES OF AM ORPHOUS POLYM ERS | 开篇：10 秒模量的取样约定与 E(t) = G(t)/… 的测量定义 |
| 2 | TIME TEAM PERATURE EQUI VALENCE | Log E(Pa) vs 温度的图谱，标注 Glassy region / Rubbery plateau / Cross-linked elastomers / Melt / Low molecular weight |
| 3 | RELAXATION IN POLYMERS | 孤立链被瞬时拉伸 → 键角分布（trans, gauche 等）重排 → 以特征时间 τ 表征松弛 |
| 4 | AM ORPHOUS POLYM ERS - THE FOUR REGIONS OF VI SCOELASTIC BEHAVIOUR | 四区域定义（Glassy / Tg / Rubbery plateau / Terminal flow）+ 图示 Log E 参考值（Glassy 9.3、Rubbery plateau 6.0、Low MW 4.0、Melt 3.5） |
| 5 | SEMI - CRYSTALLINE POLYMERS | LPE 与 LDPE 的 G′ 与 tan δ 温度谱表（−120 ℃ ~ 110 ℃）；来源 Flocke 1962 |
| 6 | MECHANICAL AND THEORETICAL MODELS OF VI SCOELASTIC BEHAVIOUR（## DEFINITIONS） | G(t) = τ(t)/γ₀；J(t) = γ(t)/τ₀；G(t) ≠ 1/J(t)；限定线性模型 |
| 7 | SIMPLE MODELS OF THE VI SCOELASTI C BEHAVI OUR OF AM ORPHOUS POLYM ERS | 蠕变-恢复与应力松弛的真实曲线形态 |
| 8 | STRAIN VS. TIME FOR SIMPLE MODELS | Spring / Dashpot / 组合模型的应变响应示意 |
| 9 | MAXWELL MODEL | 由 Hooke 定律与 Newtonian 流变叠加得 dε/dt = σ/η + (1/E)(dσ/dt) |
| 10 | MAXWELL MODEL - creep and recovery | Maxwell 方程的图像化表示（瞬时弹性 + 稳态黏流） |
| 11 | MAXWELL MODEL - stress relaxation | 令 dε/dt = 0 解得 σ = σ₀ exp(−t/τ_t)，τ_t = η/E；随即与真实 S 形数据对比 |

源文件中可恢复的关键量化信息：Slack 式的 Log E 区域参考值（Glassy 9.3 / Rubbery plateau 6.0 / Low MW 4.0 / Melt 3.5，单位 Log E(Pa)）；半结晶 PE 温度谱表（LPE 在 −120 ℃ 时 G′ = 1.4×10⁹ N·m⁻²、tan δ = 0.05；LDPE 同温 G′ = 1.2×10⁹ N·m⁻²、tan δ = 0.04，至 110 ℃ 时 LPE G′ 降至 1.5×10⁸、LDPE 降至 1.0×10⁷）。

## Relevance to Hygiene R&D 与卫材研发的关联

相关性评级：**中（方法论价值高，产品数据为零）**。讲义本身与卫生用品无关，但它提供的**测试口径**直接落在卫材两类关键材料上：弹性体（弹性腰围/隔边/氨纶）与胶黏剂（热熔胶）。

| 可迁移要点 Transferable point | 卫材落点 Where it lands |
|---|---|
| DMA 的 tan δ 峰值 = Tg 判据 | 热熔胶低温脆断风险评估、无纺布热熔胶 Tg 与低温仓储适用性判定；胶黏剂原理底座可参见 Adhesive Handbook Part 2 Fundamental Aspects 方向（该页已在库内） |
| τ_t = η/E：松弛快慢由粘度与模量共同决定 | 热熔胶开放时间/初粘-持粘窗口的配方调节逻辑（改性任一参数都会移动粘合窗口）——注意该式对视觉为「胶层流变」而非「基材」 |
| G(t)（应力松弛）与 J(t)（蠕变柔量）两个可直接套用的评价量 | 弹性腰围、皮筋、拉伸复合膜的拉力衰减（应力松弛）与持久变形（蠕变/永久形变）评价；线性前提提醒测试必须落在小应变区 |
| 时温等效可构造主曲线 | 用短时变温 DMA 外推长期蠕变/老化，缩短材料筛选周期 |
| 半结晶聚合物『不可一概而论』 | 双组分/热风无纺布中的 PP 与 PE 组分黏弹行为差异需分别实测 DMA，不能拿无定形结论直接套 |

诚实评价：**这是讲义级方法论，不是材料规格书**。它有明确的适用边界（线性、小应变、单一松弛机制），越界使用（大应变、多相体系、熔体纺丝高速拉伸）结论不成立；[待验证] 卫材实测必须回到具体材料的 DMA 谱。

## Note on Compilation 编译说明

- 源文件 7,002 bytes，≤40 KB，已**全文读取**（跳过 YAML front matter）。
- 源文件由 PDF/PPT 抽取而来，OCR 质量一般：标题普遍断字（`VI SCOELASTI C`、`EQUI VALENCE`），公式排版存在串行，图片仅留 `[图片: ...]` 占位。本页只引用可确认的公式与文字，未对模糊处做补写。
- **与 [[Viscoelastic Properties of Amorphous Polymers]] 的一处口径差异需注意**：本页源文件原文写作 **G(t) ≠ 1/J(t)**（不等式），而深度拆解页将其记为 `"G(t) = 1 / J(t)"`。以源文件为准时应取不等式；两者是否等价取决于是否处于单一 Maxwell 元的线性情形，[待验证] 使用前请复核原始讲义页面。
- 本页为**索引页**，未生成 chapter 页（讲义单篇，无分章结构）。

## Related Sources 关联来源

- [[Viscoelastic Properties of Amorphous Polymers]] — 同一源文的逐行深度拆解（四区域、Maxwell 推导、卫材关联表）
- [[Ebewole Polymer Science Ch14 Polymer Viscoelasticity]] — 教材级的粘弹性平行章节，可互校术语与模型层次
- [[Origin of Rubber Elasticity Book]] — 橡胶弹性的理论底座，解释四区域中 Rubbery plateau（橡胶平台区）的物理来源
- [[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]] — 流变与物理测试的教科书入口（DMA 与拉伸测试方法语境）
- [[Introduction to Physical Polymer Science]] — 玻璃化转变与时间-温度叠加原理的系统论述
- [[Polymer Testing Handbook]] — 试验方法标准口径，用于把讲义定义落到可执行测试规程

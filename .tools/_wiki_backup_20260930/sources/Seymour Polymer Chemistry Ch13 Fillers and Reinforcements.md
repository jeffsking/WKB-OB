---
type: source
title: "Seymour Polymer Chemistry Ch13 Fillers and Reinforcements"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Seymour Polymer Chemistry/chapters/Seymour Polymer Chemistry_ch13.md.md"
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Under ASTM D-883 a filler is a relatively inert material added to a plastic to modify its strength, permanence, working properties, or other qualities or to lower costs, while a reinforced plastic has strength properties greatly superior to the base resin owing to high-strength fillers embedded in the composition."
  - "Einstein equation: η = η₀(1 + 2.5c) with ηsp/c = 2.5; viscosity depends on the fractional volume c occupied by spheres and is independent of sphere size or liquid polarity. Mooney added a crowding factor β equal to 1.35 (closely packed) and 1.91 (loosely packed)."
  - "Modulus of filled systems follows the Einstein–Guth–Gold (EGG) equation M = M₀(1 + 2.5c + 14.1c²), and nonspherical particles are handled by η = η₀(1 + 0.67fc + 1.62f²c²) where f = l/D is the aspect ratio."
  - "Longitudinal modulus follows the Kelly–Tyson equation ML = k M_F c_F + M_M c_M, where k = 1 for parallel continuous filaments and decreases for more randomly arranged shorter filaments; for fibres longer than the critical length lc the first term is multiplied by (l − lc)/lc, and fibres should generally have aspect ratios exceeding 100."
  - "Addition of carbon black increases the tensile strength of SBR from 100 to 4000 psi; about 1.5 million tons are produced annually in the United States, much of it used for reinforcement of elastomers."
  - "Composite strength depends on strong van der Waals interfacial forces, enhanced by polar functional groups on the polymer and by treatment of filler surfaces with silanes, titanates or other surface-active agents; γ-mercaptopropyltrimethoxysilane couples via trimethoxy groups to glass silanols and via mercapto groups to the polymer."
summary_cn: "第13章是填料与增强体系：以 ASTM D-883 定义 filler 与 reinforced plastic 的边界，用 Einstein/Mooney/EGG 黏度-模量方程描述球形填料，用 Kelly–Tyson 方程 ML = k·M_F·c_F + M_M·c_M 定量预测纤维增强，并展开 aspect ratio>100、临界长度 lc、硅烷/钛酸酯偶联剂与纳米复合材料。"
tags: ["source/book", "filler", "reinforcement", "composite", "einstein-equation", "kelly-tyson", "aspect-ratio", "coupling-agent", "silane", "carbon-black"]
tags_zh: ["填料", "增强材料", "复合材料", "爱因斯坦方程", "凯利-泰森方程", "长径比", "偶联剂", "硅烷", "炭黑"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Seymour Polymer Chemistry Ch02 Polymer Structure and Morphology]]", "[[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]]", "[[Seymour Polymer Chemistry Ch12 Inorganic Polymers]]", "[[06_SSMMS无纺布技术研究报告.md]]"]
---

# Seymour Polymer Chemistry Ch13 Fillers and Reinforcements

> Source: Seymour/Carraher, *Polymer Chemistry*, Ch.13 — Fillers and Reinforcements for Polymers（聚合物的填料与增强材料）.
> Citation convention 引用约定: 源文件为 .txt 抽取件，**无正式印张页码**，本页以源文件行号（line no.）定位；原书页码缺失处标注 [待验证]。

## Executive Summary 内容概要

Chapter 13 builds the four-level progression **filler（填料）→ reinforcement（增强材料）→ interfacial coupling（界面偶联）→ composite（复合材料）**. Its quantitative spine runs from the **Einstein viscosity equation** for spherical fillers to the **Kelly–Tyson equation** for fibre reinforcement, with **aspect ratio（长径比）** and **critical fibre length（临界纤维长度 lc）** as the fibre-efficiency parameters. 对卫材的映射：**无纺布是由纤维（而非球形填料）构成的纤维网络**，其强度传递效率由 aspect ratio、取向系数 k 与纤维-基体/纤维-纤维界面决定；CaCO₃/滑石粉填料在 PE 透气膜与 PP 共混体系中的分散与偶联，也直接落在本章。

## Definitions: Filler vs Reinforced Plastic 定义边界

> *"According to the American Society for Testing and Materials standard ASTM D-883, a filler is a relatively inert material added to a plastic to modify its strength, permanence, working properties, or other qualities or to lower costs, while a reinforced plastic is one with some strength properties greatly superior to those of the base resin resulting from the presence of high-strength fillers embedded in the composition."* (line 18-23, 55, 185)

| 术语 Term | 中文 | 定义要点 Key point |
|---|---|---|
| Filler 填料 | 填料 | 相对惰性，改性或降本 relatively inert, modify or lower cost |
| Reinforced plastic 增强塑料 | 增强塑料 | 因高强度填料嵌入而强度**远优于**基体树脂 greatly superior to base resin |
| Extender 延伸剂 | 增量剂 | *"The word extender, sometimes used for fillers, is not always appropriate because some fillers are more expensive than the resin"* (line 153) |
| Composite 复合材料 | 复合材料 | *"a strong fibers embedded in a continuous matrix"* (line 165) |

## Spherical Fillers: Viscosity and Modulus 球形填料的黏度与模量

> *"According to the Einstein equation, the viscosity of the mixture (η) is related to the fractional volume (c) occupied by the spheres, and η is independent of the size of the spheres or the polarity of the liquid."* (line 58)

| 方程 Equation | 表达式 Expression | 说明 Note |
|---|---|---|
| **Einstein**（Eq. 13.1） | **η = η₀(1 + 2.5c)**；ηsp/c = 2.5 | 与粒径、液体极性无关；适用 c < 0.1（line 172） |
| **Mooney**（Eq. 13.2） | **η = η₀(2.5c / (1 − βc))** | 引入 **crowding factor β = 1.35（密堆）/ 1.91（松堆）** (line 63) |
| **EGG 模量**（Eq. 13.3） | **M = M₀(1 + 2.5c + 14.1c²)** | 二次项 14.1c² 反映填料间相互作用 |
| **非球形修正**（Eq. 13.4） | **η = η₀(1 + 0.67fc + 1.62f²c²)** | **f = l/D 长径比 aspect ratio** (line 71) |

**填料与 Tg**：*"Small particles with a diameter of less than 10 μm increase the crosslinked density, and active fillers increase the glass transition temperature (Tg) of the composite."* (line 76)

## Fibre Reinforcement: Kelly–Tyson 纤维增强

> *"The longitudinal modulus (ML) may be estimated from the Kelly Tyson equation shown below... The constant k is equal to 1 for parallel continuous filaments and decreases for more randomly arranged shorter filaments."* (line 98)

> **ML = k·M_F·c_F + M_M·c_M**（Eq. 13.5, line 100）

| 参数 Parameter | 含义 Meaning | 取值 Value |
|---|---|---|
| M_F | 纤维模量 fibre modulus | 由纤维材质决定 |
| M_M | 树脂基体模量 matrix modulus | 由基体决定 |
| c_F / c_M | 纤维/基体体积分数 volume fraction | c_F + c_M = 1 |
| **k** | 取向效率系数 orientation factor | **k = 1（连续平行纤维）；k → 0.5（双向布）；随机短纤维 k 更小**（line 176, 213） |

**短纤维修正 Short-fibre correction**：*"When they are longer than the critical length (lc), it is necessary to modify the first term in the Kelly Tyson equation by multiplying by a factor (l − lc)/lc in which l is equal to the actual fiber length."* (line 103)

**长径比要求 Aspect ratio**：*"Generally, the fibers should have aspect ratios (ratio of length to diameter) exceeding 100, often much larger."* (line 106)

| 纤维/增强体 Reinforcement | 特征 Feature | 中文 |
|---|---|---|
| E-glass | *"Typical glass fiber"* (line 109) | 通用玻璃纤维 |
| C-glass | 耐化学型（章节地图 line 254） | [口径待验证] |
| R- / S-glass | *"Stiffer and stronger than E-glass"* (line 111) | 高模高强 |
| Carbon / graphite fibre | 由 PAN/粘胶原丝热解（line 256） | 碳纤维/石墨纤维 |
| **Carbon nanotube 碳纳米管** | **aspect ratio > 1000**；*"can withstand much greater deformations before they break"* (line 124-126) | 纳米增强 |

**成型工艺 Processes**：filament winding（缠绕）、pultrusion（拉挤）、**SMC（Sheet Molding Compound，resin-impregnated mat 片状模塑料，*"the most widely used form of molded fibrous glass resin composite"* line 114）**、**BMC（Bulk Molding Compound，resin-impregnated bundles of fibers 团状模塑料）**。

## Fillers: Natural and Synthetic 填料谱系

> *"Among the naturally occurring filler materials are cellulosics—such as wood flour, β-cellulose, shell flour, starch—and proteinaceous fillers such as soybean residues. Approximately 40,000 tons of cellulosic fillers is used annually by the American polymer industry."* (line 84)

| 类别 Class | 代表 Examples | 中文 |
|---|---|---|
| 天然纤维素类 Cellulosics | wood flour、β-cellulose、shell flour、starch | 木粉、β-纤维素、淀粉 |
| 天然蛋白类 Proteinaceous | soybean residues | 大豆渣 |
| 合成 Synthetic | carbon black、glass beads/flakes、powdered metals | 炭黑、玻璃珠/片、金属粉 |
| 金属氧化物 Metal oxides | ZnO、Fe₂O₃ | 氧化锌、氧化铁 |
| 硅酸盐 Silicates | kaolin、mica、talc、nepheline syenite、wollastonite | 高岭土、云母、滑石、霞石正长岩、硅灰石 |

**炭黑的定量效果 Carbon black**：

> *"For example, addition of these fillers increases the tensile strength of SBR from 100 to 4000 psi."* (line 87)

> *"Much of the 1.5 million tons produced annually in the United States is used for the reinforcement of elastomers."* (line 90)

## Coupling Agents 偶联剂与界面

> *"The high strength of composites is dependent on strong van der Waals interfacial forces. These forces are enhanced by the presence of polar functional groups on the polymer and by the treatment of filler surfaces with silanes, titanates, or other surface-active agents."* (line 79)

| 偶联剂 Coupling agent | 机理 Mechanism | 中文 |
|---|---|---|
| **Silane 硅烷**（如 γ-MPTMS） | *"the trimethoxy groups... couple with the silanol groups on the surface of fibrous glass and that the mercapto groups couple with the polymer"* (line 131) | 三甲氧基 ↔ 玻璃硅醇；巯基 ↔ 聚合物 |
| **Titanate 钛酸酯**（如 TTS） | *"monoalkyl titanates form titanium oxide monomolecular layers on the filler surface and modify the surface energy so that the viscosity of the resin-filler mixture is reduced"* (line 134) | 形成氧化钛单分子层 → 降低表面能与混炼能耗 |
| Zirconate 锆酸酯 | 章节地图列为同系（line 262） | [原文未展开] |

**具体表面处理配方**（line 137）：

- CaCO₃ 填料 + **硬脂酸 stearic acid** → 改善与树脂的界面结合；
- Silica + **邻羟基苯甲醇 O-hydroxybenzyl alcohol** 或 **乙二醇 ethylene glycol** → 强化与树脂的结合。

## Nanocomposites 纳米复合材料

> *"A number of inorganic/organic nanocomposites have been made. These include nano inorganics including nanofibers from silicon nitride, titanium(IV) oxide, zirconia, alumina, titanium carbide, and tungsten carbide. This includes the use of special clays (layered silicates) mixed with nylons to form nanocomposites."* (line 142)

> *"Nanofibers allow more contact between the fiber (on a weight basis) and the matrix resulting is a stronger composite because of an increased fiber surface–matrix interface."* (line 145)

> *"Compared with carbon fibers, carbon nanotubes imbedded within a polymer matrix can withstand much greater deformations before they break. Further, nanomaterials are generally more efficient in transferring applied load from the nanomaterial to the matrix."* (line 206)

## Methodology Critique 方法论批判

- **Mooney 方程的写法存疑**：源文件给出 "η = η₀(2.5c / (1 − βc))"（line 65），该形式在 c → 0 时不趋于 η₀，与 Einstein 极限不自洽；经典 Mooney 形式为 ln ηrel 或含指数项。**引用前须回原书核对** [待验证]。
- **Einstein 方程的适用范围被低估**：其 2.5 系数严格成立于稀悬浮液（c < 0.1，见 line 172）；本页表格中"与粒径无关"也仅在稀溶液、无相互作用下成立，高填充体系必须用 EGG 二次项或 Mooney 修正。
- **k 的取值是经验区间**：源文件只在正文给了 k = 1（连续平行）与"decreases for more randomly arranged shorter filaments"，而"k → 0.5（双向布）"来自报告的 Step 4 表格（line 176）与 RIA 卡片（line 213），**非原文逐字表述**，标 [待验证]。
- **SBR 100 → 4000 psi 的对照条件未给出**：原文未说明是未填充 SBR 与炭黑填充 SBR 在同一配方与测试标准下的对比，"40 倍"不能直接外推到其他弹性体 [待验证]。
- **纤维增强公式对无纺布只有类比价值**：Kelly–Tyson 假设纤维嵌入连续基体（resin matrix），而无纺布是纤维-纤维点粘合网络、无连续基体相，**直接套用会高估取向贡献**。

## Hygiene Implication 卫材关联

- **无纺布强度可用本章的语言定性理解，但不可直接套 Kelly–Tyson**：Kelly–Tyson 要求"纤维嵌入连续基体"，而纺粘/熔喷/SSMMS 是纤维自粘合网络，基体体积分数 c_M 实为孔隙（空气）。因此其适用部分是**取向系数 k 与长径比 f 的概念**：热轧/热风粘合提高的是纤维间界面（本章 §13.4 的界面力），而非纤维体积分数。**连续长丝纺粘（k 接近 1）与短纤维梳理成网（k 显著下降）的干/湿强度差异，正是 k 与 aspect ratio 的直观体现。**
- **CaCO₃ 是卫材最重要的矿物填料，本章给出其界面处理方案**：PE 透气底膜大量填充 CaCO₃（微孔成核 + 降本 + 白度），原文明确"CaCO₃ 与树脂的界面结合经**硬脂酸表面处理**改善"（line 137）——这与工业上碳酸钙的硬脂酸包覆活化完全一致；钛酸酯偶联剂（TTS）通过形成氧化钛单分子层降低表面能、降低混炼黏度（line 134），是**高填充母料降粘、降低螺杆扭矩**的机理依据。
- **Einstein/EGG 方程是高填充体系黏度预测的工具**：母料与透气膜配料的熔体黏度随填料体积分数 c 上升，EGG 的二次项 14.1c²（line 68）意味着**超过中等填充量后黏度呈超线性增长**，这直接约束透气膜可填充上限与拉伸成孔的工艺窗口。与 Ch.05 的流变测试口径可直接对接。
- **滑石粉/高岭土属层状硅酸盐**：其晶体结构见 Ch.12 的 Si₄O₁₀⁴⁻ 层状分类（Table 12.3 第 7 行）；层状形貌带来高 aspect ratio，按本章 Eq. 13.4 的非球形修正，其增粘效应远强于球形填料。
- **纳米银抗菌纤维、纳米黏土高阻隔膜**属 §13.5 纳米复合材料范畴，其增强机理是"单位重量更高的纤维-基体界面面积"（line 145），但本章未给出抗菌或阻隔的定量数据，不做延伸。

## Related Sources 关联来源

- [[Seymour Polymer Chemistry Ch02 Polymer Structure and Morphology]]
- [[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]]
- [[Seymour Polymer Chemistry Ch12 Inorganic Polymers]]
- [[06_SSMMS无纺布技术研究报告.md]]

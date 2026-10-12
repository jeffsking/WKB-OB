---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_a59253c0ccb9cc9be54f24bfb7d0e47e001a693ee6c0644e"
source_file: "Polymer Reaction Engineering_ch04_FRP_Heterogeneous.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Polymer Reaction Engineering (Asua)/chapters/Polymer Reaction Engineering_ch04_FRP_Heterogeneous.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Polymer Reaction Engineering_ch04_FRP_Heterogeneous.md.md

# Chapter 4 深度拆书报告

## Free-Radical Polymerization: Heterogeneous Systems

Source: José M. Asua (Ed.), Polymer Reaction Engineering, Wiley-VCH, Ch. 4, pp. 201–231
Authors: Gregorio R. Meira & Costas Kiparissides
Report prepared for: 卫材创新研发（HIPS / PVC 形态控制 / 非均相聚合工程挑战）与战略采购
Scope: HIPS 微观结构–性能关系、VCM 本体聚合机理、PVC 形态控制

## 1. 执行摘要（Executive Summary）

HIPS 韧性由"相转化 + 接枝聚合物界面稳定"共同决定，而非简单的橡胶含量。 本体 HIPS 聚合中，PS/PBD/S 三元体系在约 2% 转化率发生相分离（Point B），在约 13% 转化率发生相转化（Point C），形成典型的 "salami"（意大利腊肠状）形态——分散橡胶粒子内部包含 PS 包涵体。接枝聚合物 (poly(BD-graft-S)) 在相界面起"tie"作用：双支及以上 PS 支链位于橡胶粒子外表面，单支 PS 支链位于包涵体界面，是控制粒度和形态的关键变量。

HIPS 最优橡胶粒子尺寸存在"倒 U 型"规律：1–5 µm 韧性最佳。 小于 1 µm 的表面光泽/透明度好但力学性能下降；远大于 5 µm 时裂纹在粒子表面引发，冲击性能反而降低。PBD 含量分级：~3% PBD = 半抗冲级；6% PBD = 抗冲级；8–10% PBD = 高抗冲级。

VCM 本体聚合呈现"三段动力学 + Trommsdorff 自加速 + 玻璃化效应"的复合特征。 三段：(1) 均相 (<0.01% 转化)；(2) 三相共存 (单体相 + 聚合物富集相 + 气相)；(3) 单一聚合物富集相。反应热高达 ~100 kJ/mol，自加速峰值出现在 ~68.5°C；温度升高到玻璃化点以上会显著改变终止动力学，分子量随温度升高而下降。

PVC 颗粒形态呈"微米–纳米"两级层次结构，由动力学而非平衡控制。 一次粒子 (~80–100 nm) 通过聚集形成 2–10 µm 的团聚体（grain）；Rance 五阶段模型描述了从微域核化到一次粒子融合的全过程。Rhone–Poulenc 两段法中，一段温度 >62°C 控制一次粒子聚集强度，二段温度/转化率控制孔隙率与分子量——这是卫材管材/线束护套产品性能的"形态根源"。

工程痛点高度集中：散热、粘度高、壁面结垢。 只有约 8% 的 PVC 总产量采用本体聚合（其余走悬浮法），根本原因是热量移除和温控难题。非均相聚合的核心工程挑战在于"相界面 + 传质 + 传热"的耦合，这直接影响卫材产品的一致性和可追溯性。

## 2. 章节概览

本章系统梳理本体自由自由基聚合中的非均相（heterogeneous）体系，聚焦两大工业支柱：HIPS（高抗冲聚苯乙烯）与 PVC（聚氯乙烯）。章节结构从热力学相行为 → 动力学机理 → 形态控制 → 工业装置层层展开，是"微观结构–加工–性能"链条的经典范式案例。

|||||
|---|---|---|---|
|4.1|Introduction|非均相本体聚合的共性优势与工程痛点|1|
|4.2|HIPS Polymerization|HIPS 本体工艺、相分离/相转化、"salami"形态|8|
|4.2.1|Interrelationship between Microstructure and Application Properties|微观结构–性能定量关系|3|
|4.2.2|Modeling of Heterogeneous HIPS Systems|双相动力学模型（Casís et al.）|4|
|4.3|VCM Homopolymerization|三段动力学、Trommsdorff 效应、玻璃化效应|6|
|4.3.1|Kinetic Mechanism|VCM 详细/简化动力学机理表|3|
|4.3.2|PVC Morphology|Rance 五阶段形态模型、群体平衡方程|5|

## 3. Step 1 宏观定位

### 3.1 学科坐标

- 一级学科：Polymer Reaction Engineering（高分子反应工程）
- 二级分支：Free-Radical Polymerization（自由自由基聚合）
- 本章定位：Heterogeneous Bulk Systems（非均相本体体系）——介于均相本体（如 GPPS）与有分散介质的悬浮/乳液体系之间的"中间地带"
- 关键区分维度：

- 分散介质有无 → 无（vs. 悬浮/乳液）
- 体系是否均相 → 否（vs. GPPS / PMMA 本体）
- 非均相来源 → 产物本身析出（PVC）或 共混聚合物不相容（HIPS 中 PS 与 PBD）

### 3.2 战略重要性（卫材视角）

|||
|---|---|
|市场地位|PS 全球年消费 15.2 Mt/2004：Crystal 45% / HIPS 42% / Expandable 13%|
|HIPS 龙头集中度|Dow、BASF、NOVA、Total、Innovene 合计占全球产能 40%|
|PVC 本体占比|仅 ~8% 的 PVC 总产量走本体路线（多为 Rhone–Poulenc 工艺）|
|卫材应用关联|PVC grain 形态直接决定管材/线束护套的加工性、增塑剂吸收、力学性能|
|采购杠杆|头部 5 家占 40% 产能，HIPS 采购谈判存在明显寡头议价风险|

### 3.3 与前序/后续章节的关系

- 前序呼应：Ch. 3（均相本体/溶液）给出"理想极限"，本章揭示"非均相的现实"
- 后续铺垫：Ch. 5（Suspension Polymerization）——本章末尾明确指出 PVC、PS、HIPS、ABS、SAN、PMMA 等既可用本体也可用悬浮，两种工艺在形态控制上的取舍对比是后续讨论基础

## 4. Step 2 中观章节拆解（6 模块）

### 模块 A：引言与工程定位（4.1）

核心命题：本体聚合的优点（反应性能、纯度、无溶剂转移反应）与缺点（高粘度导致的散热/混合/泵送/壁面结垢问题）是同一枚硬币的两面。

- 非均相来源两种典型：

- 产物自析出（PVC）——聚合物不溶于单体
- 不相容共混（HIPS）——初始 PBD 预聚物与生成的 PS 链不相容
- 热塑性塑料的"多相化"是性能增强通途：PVC 靠增塑剂液滴软化、HIPS/ABS 靠橡胶粒子增韧
关键引述："The disadvantages are related with the high process viscosity, which in turn generates problems of heat removal, mixing, pumping and reactor wall fouling by film formation."

### 模块 B：HIPS 本体工艺与相行为（4.2）

|||
|---|---|---|---|
|Dissolution（溶解）|~70°C|0|橡胶溶于单体，抑制热聚合|
|Prepolymerization（预聚合）|90–120°C|至 ~30%|引发剂消耗、相分离（B 点 ~2%）、相转化（C 点 ~13%）|
|Finishing（后聚合）|~150°C|30% → ~75%|粘度剧增、缓慢搅拌以保护形态|
|Devolatilization（脱挥）|~250°C|—|真空脱溶剂/残余单体，橡胶交联|

相图关键点（Figure 4.2, PS/PBD/S 三元相图）：
- A：起始（PBD 溶于 S）
- B：相分离（~2% 转化）→ PS 富集相分散在 PBD 富集相
- C：相转化（~13% 转化）→ PS 富集相成为连续相
- D：预聚合结束（~30% 转化）

"Salami" 形态（意大利腊肠状）：分散橡胶粒子内部含有 PS 包涵体，是橡胶粒子的"内部结构骨架"，由接枝聚合物在界面起 tie 分子作用稳定。

关键引述："The dispersed rubber particles present a complex morphology with PS occlusions. This morphology is often referred to as 'salami' morphology."

### 模块 C：微观结构–应用性能关系（4.2.1）

定量规律汇总（Table 4.1，卫材选材关键）：

|||
|---|---|---|---|
|[PBD] 增加|↑|↓|↑ (微↓)|
|粒子尺寸|先 ↑ 后 ↓（1–5 µm 最优）|无影响|微 ↑（↓）|
|游离 PS 的 M_w|先快 ↑ 后不变|微 ↑|微 ↑（↓）|
|交联密度|先 ↑ 后 ↓|无影响|↑ (↑)|
|矿物油|↑|↓|↓ (无影响)|
|接枝度|↑|无影响|↑ (↓)|

HIPS 分级：Semi-impact ~3% PBD / Impact 6% PBD / High-impact 8–10% PBD

粒径影响因素三要素：
1. PBD 富集相 / PS 富集相的溶液粘度比
2. 搅拌速率
3. 两相界面张力（依赖接枝效率）

关键引述："Toughness first increases with particle size reaching a maximum value for particles in the range of 1–5 µm."

### 模块 D：HIPS 异相动力学模型（4.2.2）

模型框架（Casís et al.）：基于相图的两相（Phase I = PBD 富集相；Phase II = PS 富集相）质量守恒模型。

核心假设：
1. 每相完全搅拌
2. 引发剂按分配系数 K_I2(x) 在两相间分配（依赖转化率）
3. 单体、PS、PBD 的分配系数由三元相图决定
4. 相转化发生在 V_I = V_II 时
5. 相转化后聚合物不再在两相间传质

关键公式：
- 引发剂消耗：dN_I2/dt = −k_I([I₂]_I VI + [I₂]{II} V_{II})
- 单体消耗：dNM/dt = −Σᵢ R{p_i} V_i
- 接枝效率：E_S = G_GS / (G_GS + G_PS)
- 游离 PS 的 WCLD（重均链长分布）：包含传播/转移/复合终止的耦合项

模型验证（120°C 批次聚合）：相分离 2%、相转化 13%、预聚合终了 30%、最终转化 ~75%，预测与实际形态高度吻合。

### 模块 E：VCM 聚合动力学（4.3 + 4.3.1）

三段动力学（卫材 PVC 产品形态的关键基础）：

|||
|---|---|---|---|
|第一阶段|< 0.01%|均相|初级自由基快速与单体反应|
|第二阶段|0.01% → x_f|三相共存|单体相 + 聚合物富集相 + 气相；压力随 x_f 出现特征性下降|
|第三阶段|x_f < x < 1|单一聚合物富集相|聚合物溶胀残余单体，向玻璃态过渡|

Trommsdorff 自加速效应：链增长常数 k_p 随粘度升高而升高，终止常数 k_t 随粘度升高而下降 → 速率与分子量同步飙升。模型预测 68.5°C 时自加速最强。

玻璃化效应（Glass Effect）：当聚合物相 T_g 接近 T_rxn 时，体系进入玻璃态，自由基被"冻结"，速率急剧下降，分子量分布加宽。

详细 vs 简化机理：
- 详细：包含头-尾 (k_p1)、头-头 (k_p2)、氯迁移 (k₁, k₂, k_−2)、氯甲基支化 (k_p3)、乙基支化 (k_p4)、1,5-回咬 (k_bb)、六中心回咬 (k'_bb)、1,6-回咬 (k''_bb) 等
- 简化：传播、向单体转移、向聚合物转移、分子内转移（backbiting）、复合/歧化终止——j 下标区分相（j=1 单体相，j=2 聚合物相）

Rhone–Poulenc 两段法工业流程：
- 一段（预聚）：VCM 中引入引发剂，温度 >62°C（确保团聚体凝聚），约 5% 总聚合物在此阶段形成，剧烈搅拌至 10% 转化
- 二段：补充剩余 VCM 和引发剂，在较低温度下继续聚合至 80–85% 转化；温度控制分子量，转化控制孔隙率

关键引述："The polymerization of VCM is highly exothermic (~100 kJ mol⁻¹). Thus, the efficient removal of the reaction heat is very critical for the operation of large-scale reactors."

### 模块 F：PVC 形态控制（4.3.2）

Rance 五阶段颗粒形成模型（PVC grain 的"微观进化史"）：

|||
|---|---|---|
|1. 核化与微域形成|<0.01%|生成不稳定聚合物微域，半径 10–20 nm|
|2. 聚集与域形成|0.01–1%|微域聚集成初级粒子核（domain），初始尺寸 80–100 nm，带负静电荷形成胶体|
|3. 生长与二次聚集|1–20%|一次粒子在 5–10% 转化前大量生成；10–30% 转化形成连续网络|
|4. 一次粒子生长与融合|<70%|一次粒子生长至单体相消失|
|5. 压力下降、速率降低|>70%|一次粒子融合形成 2–10 µm 团聚体|

群体平衡方程（Population Balance）：
$$\frac{\partial n(v,t)}{\partial t} + \frac{\partial (I(v,t) \cdot n(v,t))}{\partial v} = \delta(v - v_0) \cdot r(v0, t) + \frac{1}{2}\int{v_0}^{v-v0} \beta(v-u, u) \cdot n(v-u, t) \cdot n(u, t) \, du - \int{v0}^{v\infty} \beta(v, u) \cdot n(v, t) \cdot n(u, t) \, du$$

- 聚结速率常数 β(u,v) 依赖静电稳定（Debye 长度 κ⁻¹、粒子总电荷）和空间位阻稳定（吸附聚合物分子量、Flory–Huggins χ 参数）
- 微域生成速率：r(v₀, t) = R_pm · w_m / [ρ_p(1−φ_m)·v₀²]
- 一次粒子生长速率：I_V = R_pp / ([M₀]·x·v)
孔隙率与卫材性能的直接关系："An increase of monomer conversion lowers porosity and increases bulk density." —— 卫材管材需要特定孔隙率区间以平衡增塑剂吸收、加工流动性和力学强度。

## 5. Step 3 核心概念深挖

### 概念 1：Phase Inversion（相转化）

- 英文原文："Phase inversion occurs … leading to the formation of a PS-rich phase dispersed in a PBD-rich continuous phase … For a conversion between 5% and 25%, … phase inversion occurs."
- 中文释义：在本体 HIPS 聚合中，随转化率升高，分散相与连续相的身份发生互换——PS 富集相从"液滴"转变为"连续相"，是形态定型的关键时刻。
- 物理本质：两相体积分数交叉（V_I = V_II）；在共连续态（co-contiguous morphology）短暂停留后完成反转。
- 工程意义：相转化发生在 ~13% 转化（模型预测），发生在预聚合段早期——这决定了搅拌强度、温度、引发剂用量在低转化阶段对最终形态具有放大效应。
- 卫材启示：若预聚合段控温/搅拌波动，最终 HIPS 产品的形态离散性将不可逆地锁定。

### 概念 2：Tie Molecule（连接分子 / 接枝聚合物界面稳定剂）

- 英文原文："Graft copolymer molecules stabilize the dispersed PS-rich phase … graft copolymers with two or more PS branches place themselves at the external interface of the rubber particles, while graft copolymer molecules with a single PS branch place themselves at the occlusions interface."
- 中文释义：接枝共聚物分子在两相界面起"锚定"作用，类似"分子缝线"——不同支化度的接枝聚合物按支链数自动择位，是"salami"形态的微观"结构工程师"。
- 物理本质：多支链 = 表面张力最低 → 外表面；单支链 = 空间熵优势 → 包涵体界面。
- 卫材启示：接枝效率 E_S = G_GS/(G_GS+G_PS) 是核心过程控制变量；改变引发剂类型（单/双官能）、CTA 用量、搅拌速率即可调 E_S，进而调形态。

### 概念 3：Trommsdorff–Norrish Effect（自加速效应 / 凝胶效应）

- 英文原文：*"The polymerization of VCM is highly exothermic (~100 kJ mol⁻¹)"；"the gel effect (autoacceleration)"* appears at ~68.5°C.
- 中文释义：在转化升高后，体系粘度急剧增大导致 k_t 下降、k_p 基本不变或略有升高，链自由基寿命延长，聚合速率和分子量同时激增。
- 物理本质：扩散控制的终止反应 vs 反应控制的传播反应的耦合失衡。
- 卫材启示：本体 VCM 聚合的热移除是生死线；自加速段若控温失稳，可能导致爆聚或分子量分布异常——直接影响管材/线束护套的力学一致性和热稳定性。

### 概念 4：Primary Particle / Agglomerate Hierarchy（一次粒子 / 团聚体两级层次）

- 英文原文："PVC is insoluble in its own monomer … The final product of bulk or suspension polymerization is made up of primary particles and its agglomerates."
- 中文释义：PVC 形态呈"分形"层次——80–100 nm 的一次粒子（primary particles）聚集为 2–10 µm 的团聚体（agglomerate），团聚体的孔隙率、粒径分布、比表面积决定卫材产品的加工流动性、增塑剂吸收、热稳定性、外观。
- 物理本质：由动力学路径（核化–聚集–融合）而非热力学平衡决定；Rance 五阶段模型给出"生长轨迹"。
- 卫材启示：一段温度 >62°C → 一次粒子凝聚强 → 高刚性级 PVC（硬管、型材）；二段温度低 + 转化率低 → 高孔隙率 → 高增塑剂吸收（软质线束护套、电缆料）。这是 PVC 牌号设计的"形态旋钮"。

## 6. Step 4 学术对话与批判

### 6.1 与 Ch. 3（均相本体）的对话

- 共同点：都面临高粘度散热问题；都用引发剂半衰期设计预聚合
- 关键差异：Ch. 3 假设均相、无相界面传质；Ch. 4 的核心是相图 + 相界面 + 相转化
- 学术张力：Ch. 3 的动力学模型（如 Trommsdorff 修正的 Smith-Ewart）在 Ch. 4 中需加上分配系数 K_I2(x)、K_M、K_PS 的耦合项

### 6.2 与 Ch. 5（悬浮聚合）的对话

- 本章末尾明确 "suspension polymerization is another important heterogeneous system, covering polymers such as PVC, PS, EPS, HIPS, SAN, ABS, PMMA, PVAc"
- 张力点：本体法产品纯度高、无分散介质残留，但散热与形态一致性不如悬浮法——为什么仍有 40%+ 的 PS 产能走本体？回答是：规模经济 + 纯度敏感产品（包装用）+ 寡头工艺壁垒。
- 批判视角：从"绿色化学 / 无溶剂"叙事看，本体法理论上更优；但从"工程现实 + 形态可控性"看，悬浮法在 PVC 上仍有绝对优势（92% 的 PVC 走悬浮）。

### 6.3 学术薄弱点与批判

HIPS 接枝机理仍为经验推断：*"It has been suggested that graft copolymers with two or more PS branches…"*——"suggested" 表明这是基于微观观察的合理推测，而非严格理论推导。分子动力学模拟在此仍待深入。

PVC 群体平衡模型的闭合问题：β(u,v) 同时依赖静电和空间稳定，但实际工艺中两者耦合非线性，模型多为半经验参数化，缺乏第一性原理支撑。

工业数据与学术模型的 gap：Rhone–Poulenc 工艺的关键参数（一段搅拌功率密度、二段温度曲线、脱挥段停留时间分布）在公开文献中极少——这既是 IP 壁垒，也是学术复现的障碍。

缺乏"全寿命"视角：本章聚焦反应段，但对后续挤出加工中形态的稳定性（"rubber crosslinking is beneficial, since it helps preserve the particle morphology during the material processing"）仅一笔带过——反应形态 → 加工形态 → 最终制品形态的链条未完整闭合。

## 7. Step 5 知识体系关联

### 7.1 HIPS 冲击改性机制的知识链条

PBD 橡胶粒子（5–10 wt%）
    ↓
引发剂攻击 PBD 烯丙基氢 → 生成接枝聚合物
    ↓
相分离（~2%）→ 相转化（~13%）→ "salami" 形态定型
    ↓
橡胶粒子（1–5 µm 最优）+ PS 包涵体 + 外/内界面接枝聚合物
    ↓
外力冲击 → 橡胶粒子引发 crazing（银纹化）+ shear yielding（剪切屈服）
    ↓
能量耗散 → 韧性↑（1–5 µm 时最大）

核心机制：橡胶粒子作为应力集中点，引发大量银纹/剪切带，将宏观冲击能分散到微观多重耗散事件中。粒子过小 → 无法引发银纹；粒子过大 → 银纹在表面早期失稳。

### 7.2 PVC 在卫材中的应用映射

|||
|---|---|---|
|管材（给水、燃气）|中-低孔隙率、高分子量、刚性团聚体|一段 T > 65°C、二段低 T、高 M_w|
|型材（门窗异型材）|中分子量、均匀粒度分布|二段 T 精细控制|
|线束护套|高孔隙率（增塑剂吸收）、中-低 M_w|二段较低 T、中-低 x_final|
|电缆料|高柔韧性、高增塑剂负载|高孔隙率 grain 结构|

战略采购含义：
- PVC 牌号本质上由聚合温度曲线定义，不同厂商温度窗口不同 → 采购谈判中"牌号可替代性"需评估温度窗口兼容度
- Rhone–Poulenc（现 Arkema）两段法是本体 PVC 的标杆，其他厂商工艺差异可能导致形态不可逆差异

### 7.3 与非均相聚合工程挑战的耦合

工程挑战
├── 散热（100 kJ/mol 反应热）
├── 高粘度（搅拌功率密度 vs 形态保护）
├── 壁面结垢（film formation）
├── 相转化窗口窄（13% ± Δx 是关键控制点）
└── 传质耦合（引发剂/单体在相间的分配）

## 8. Step 6 RIA 实践转化

### 8.1 RIA 卡片（Recognize–Interpret–Apply）

#### RIA 卡片 #1：HIPS 韧性优化的"1–5 µm 窗口"

|||
|---|---|
|Recognize（识别）|HIPS 韧性存在粒子尺寸最优窗口（1–5 µm），呈"倒 U 型"关系；过小过小或过大均不利|
|Interpret（解读）|该规律是"橡胶粒子作为应力集中点引发银纹/剪切带"的几何要求；1 µm 以下粒子不能有效引发银纹，5 µm 以上银纹在表面早期失稳|
|Apply（应用）|① 卫材采购 HIPS 时索取粒子尺寸分布数据（D50、D90）；② 高抗冲应用锁定 8–10% PBD + 1–3 µm 粒径组合；③ 表面光泽应用可接受  µm 但需评估力学损失|

#### RIA 卡片 #2：VCM 本体聚合"三段法"与热移除

|||
|---|---|
|Recognize|VCM 聚合热高达 ~100 kJ/mol；自加速峰值在 ~68.5°C；仅 ~8% PVC 走本体（散热难度是主因）|
|Interpret|自加速 + 高放热 = 反应工程风险热点；本体法"纯度优势"被"散热劣势"部分抵消|
|Apply|① 采购本体 PVC 时确认厂家热移除能力（反应器设计、夹套/内冷管规格）；② 要求提供分子量分布（PDI）数据作为温控一致性的代理指标；③ 战略上评估悬浮法 PVC 作为备选的替代可行性|

#### RIA 卡片 #3：PVC Grain 形态 = 卫材产品性能的"形态根源"

|||
|---|---|
|Recognize|PVC 产品性能（孔隙率、增塑剂吸收、加工性、刚性/韧性）根本上由 2–10 µm 团聚体的形态（含 80–100 nm 一次粒子的堆叠方式）决定|
|Interpret|一段温度 >62°C 控制一次粒子凝聚强度；二段 T + 转化控制孔隙率与 M_w；形态是动力学路径的"化石"，不可逆锁定|
|Apply|① 卫材不同应用锁定不同 grain 形态规格；② 采购谈判中要求供应商披露聚合温度曲线（至少二段温度范围）作为质量承诺的一部分；③ 建立"聚合温度–grain 形态–卫材制品性能"的内部映射数据库|

#### RIA 卡片 #4：接枝效率 E_S 是 HIPS 形态的"总开关"

|||
|---|---|
|Recognize|E_S = G_GS/(G_GS+G_PS) 直接决定界面张力、粒子尺寸、包涵体结构|
|Interpret|通过改变引发剂类型（单/双官能）、CTA 用量、搅拌速率可调 E_S → 间接调形态|
|Apply|① 卫材采购 HIPS 时需评估供应商对 E_S 的过程控制能力；② 高端应用要求供应商提供接枝率数据（Grafting Index）；③ 战略采购可考虑与头部厂商（Dow/BASF 等）建立联合工艺研发以获取 E_S 定制能力|

### 8.2 业务行动卡（Business Action Card）

|||||||
|---|---|---|---|---|---|
|P0|建立 HIPS/PVC 供应商"牌号–形态–聚合温度"映射数据库|采购 + 研发|2 个月|覆盖 Top 5 供应商主力牌号|
|P0|在 HIPS 采购规格中增加"橡胶粒子尺寸分布 D50/D90"强制条款|采购|1 个月|所有新合同落地|
|P1|与 Rhone–Poulenc 系（Arkema）建立本体 PVC 技术对话，评估二段温度曲线可披露性|战略采购|3 个月|技术备忘录签署|
|P1|建立"聚合形态 → 挤出加工 → 最终制品"的内部形态稳定性评估流程|研发|3 个月|完成 3 个典型卫材产品的形态追踪|
|P2|评估悬浮法 PVC 替代本体法 PVC 在特定卫材应用的可行性（成本 vs 形态）|研发 + 采购|6 个月|替代可行性报告|
|P2|与头部 HIPS 厂商（Dow/BASF）探讨 E_S 定制供应（针对高端抗冲需求）|战略采购|6 个月|联合工艺开发 MoU|

## 9. Step 7 原文摘选索引

|||||||
|---|---|---|---|---|---|
|1|4.1|"Bulk free-radical polymerizations are carried out in the absence of a dispersion medium, and without (or with a very little) solvent."|bulk, solvent-free|201|本体聚合定义|
|2|4.1|"The disadvantages are related with the high process viscosity, which in turn generates problems of heat removal, mixing, pumping and reactor wall fouling by film formation."|viscosity, fouling|201|本体法四大工程痛点|
|3|4.1|"In contrast, PVC soon precipitates from its monomer. In the HIPS process, the heterogeneity results from the incompatibility between the initial polybutadiene (PBD) prepolymer and the generated polystyrene (PS) chains."|heterogeneity, PBD|201|非均相两种来源|
|4|4.2|"In the bulk (or quasi-bulk) HIPS process, S is polymerized in the presence of 5–10% in weight of dissolved PBD, a chemical initiator, an antioxidant … and a chain transfer agent (CTA)."|HIPS, formulation|202|HIPS 配方要素|
|5|4.2|"The prepolymerization stage is carried out between 90°C and 120°C under well-stirred conditions, and it ends at around 30% conversion."|prepolymerization|202|预聚合温度/转化率|
|6|4.2|"Point A represents the initial solution of PBD in S. Polymerization starts upon addition of initiator, and the reaction path is represented by a straight line parallel to the PS–S axis."|ternary diagram|202|三元相图反应路径|
|7|4.2|"Phase inversion occurs … For a conversion between 5% and 25%, and close to the point when the PS-rich phase volume reaches the volume of the PBD-rich phase, phase inversion occurs."|phase inversion|203|相转化转化区间|
|8|4.2|"This morphology is often referred to as 'salami' morphology."|salami|203|意大利腊肠状形态|
|9|4.2|"Graft copolymers with two or more PS branches place themselves at the external interface of the rubber particles, while graft copolymer molecules with a single PS branch place themselves at the occlusions interface."|graft, tie molecule|203|接枝聚合物择位规则|
|10|4.2|"The final S conversion is around 75%."|conversion|204|最终转化率|
|11|4.2|"Toughness first increases with particle size reaching a maximum value for particles in the range of 1–5 µm. For significantly larger particles, impact resistance decreases as crazing occurs at the particle surface."|particle size, toughness|206|粒径–韧性倒 U 规律|
|12|4.2|"HIPS grades with rubber particles smaller than 1 µm are also produced for their improved surface gloss and transparency, but at the cost of reducing mechanical strength."|sub-µm particles|206|亚微米粒子的代价|
|13|4.2.2|"Phase inversion when VI = V{II}"|phase inversion model|209|相转化体积判据|
|14|4.3|"The polymerization of VCM is highly exothermic (~100 kJ mol⁻¹). Thus, the efficient removal of the reaction heat is very critical for the operation of large-scale reactors."|VCM, exothermic|216|VCM 反应热|
|15|4.3|"The disappearance of the monomer phase is associated with a characteristic drop in the reactor pressure."|pressure drop, x_f|217|压力降标志 x_f|
|16|4.3|"The most well-known bulk VCM polymerization process is the Rhone–Poulenc two-stage process."|Rhone–Poulenc|218|两段法标杆|
|17|4.3|"Only 8% of total PVC production is obtained by bulk polymerization, because heat removal and temperature control problems make suspension polymerization more attractive."|bulk vs suspension|218|本体 PVC 占比低的原因|
|18|4.3|"Always polymerized above 62°C to ensure aggregate cohesion."|aggregate, 62°C|218|一段温度下限|
|19|4.3.1|"The presence of chloromethyl and ethyl short-chain branches in PVC validates the conclusion that the propagation reactions involve several types of radicals."|branches, mechanism|220|支化证据|
|20|4.3.2|"PVC is insoluble in its own monomer; thus, vinyl chloride polymerization is a heterogeneous process that involves several physical transitions during the polymerization."|insoluble, heterogeneous|224|PVC 非均相本质|
|21|4.3.2|"These polymer chains combine together to form unstable polymer microdomains with a radius of about 10–20 nm."|microdomain, 10-20 nm|224|微域尺寸|
|22|4.3.2|"The primary particles can be produced up to about 5–10% monomer conversion … Primary particles fuse together to form agglomerates 2–10 µm in size."|primary particles, agglomerates|225|一次粒子/团聚体尺寸|
|23|4.3.2|"Experiments have shown that the porosity is dependent on the temperature of polymerization and on the degree of monomer conversion in the second stage."|porosity, second stage|227|孔隙率工艺调控|
|24|4.3.2|"The final product of bulk or suspension polymerization is made up of primary particles and its agglomerates."|morphology|224|PVC 产品形态定义|

## 附录：关键数字速查表

|||
|---|---|---|
|PS 全球年消费（2004）|15.2 Mt|—|
|HIPS 占比|42%|PS 分类|
|Top 5 产能集中度|40%|HIPS 全球|
|PBD 添加量|5–10 wt%|HIPS 配方|
|相分离转化|~2%|HIPS|
|相转化转化|~13%|HIPS（模型）|
|预聚合终了转化|~30%|HIPS|
|最终转化|~75%|HIPS|
|最优橡胶粒子尺寸|1–5 µm|HIPS 韧性|
|VCM 反应热|~100 kJ/mol|PVC|
|本体 PVC 占比|~8%|PVC 全球|
|自加速峰值温度|~68.5°C|VCM|
|二段终转化|80–85%|PVC|
|一段温度下限|>62°C|PVC|
|一次粒子尺寸|80–100 nm|PVC|
|团聚体尺寸|2–10 µm|PVC|
|微域尺寸|10–20 nm|PVC|

Report generated following 7-step SOP (academic full version). Original English quotations preserved verbatim; Chinese annotations in parentheses or annotation columns only.

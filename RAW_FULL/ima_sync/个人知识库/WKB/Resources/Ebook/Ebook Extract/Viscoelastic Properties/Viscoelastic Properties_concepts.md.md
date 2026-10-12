---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_14042a9c6d485728fb5bbcdb82060963001a693ee6c0644e"
source_file: "Viscoelastic Properties_concepts.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Viscoelastic Properties/Viscoelastic Properties_concepts.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Viscoelastic Properties_concepts.md.md

# Viscoelastic Properties — 概念索引（Concepts Index）

术语首次出现时：英文原文 + 中文释义。
引用原句保持英文原文，不翻译。

## A. 粘弹性核心概念

### A1. Viscoelasticity（粘弹性）

- 定义：材料力学响应兼具 Elastic（弹性、瞬时、可恢复）与 Viscous（粘性、时间依赖、耗散）双重特征。
- 原文位置：贯穿全文（标题、L152–L154 章节标题 "MECHANICAL AND THEORETICAL MODELS OF VISCOELASTIC BEHAVIOUR"）。
- 关联概念：Storage Modulus, Loss Modulus, Relaxation Time, Creep, Stress Relaxation。
### A2. Storage Modulus / Loss Modulus（储能模量 / 损耗模量）

- 定义：动态力学分析（DMA）中，复数模量的实部（E' 储能）与虚部（E" 损耗）；tan δ = E"/E'。
- 原文位置：L128–L129 — "a maximum in tan δ curves are observed in DMA experiments"
- 作用：tan δ 峰值用于定位 Tg。
### A3. Relaxation Time τ（松弛时间）

- 原文：*"we say the chain RELAXES to the new state and the relaxation is described by a characteristic time τ"*（L96–L97）
- Maxwell 模型中的定义：*"τ = η/E, Relaxation time"*（L362–L369）
## B. 温度与相态

### B1. Glass Transition, Tg（玻璃化转变）

- 位置：L125–L129
- 原文："Tg REGION - cooperative motions of segments now occur, but the motions are sluggish (a maximum in tan δ curves are observed in DMA experiments)"
- 物理意义：链段协同运动被激活的温区，是模量急剧下降的过渡区。
### B2. Glassy State（玻璃态）

- 原文：*"GLASSY STATE - conformational changes severely inhibited."*（L123–L124）
- 特征：构象变化被严重抑制，模量高（~10^9–10^10 Pa）。
### B3. Rubbery Plateau（橡胶平台区）

- 原文：*"RUBBERY PLATEAU - τ becomes shorter, but still longer than the time scale for disentanglement"*（L130–L133）
- 特征：模量在宽时间/温度范围内保持近似恒定。
### B4. Terminal Flow（终端流动区）

- 原文：*"TERMINAL FLOW - the time scale for disentanglement becomes shorter and the melt becomes more fluid like in its behaviour"*（L134–L135）
- 特征：缠结解缠结，材料表现为粘性流体。
## C. 材料体系

### C1. Amorphous Polymers（无定形聚合物）

- 标题：L1 "VISCOELASTIC PROPERTIES OF AMORPHOUS POLYMERS"
- 定义：不具有长程结晶有序的聚合物，其粘弹性行为可系统划分为四区域。
### C2. Semi-Crystalline Polymers（半结晶聚合物）

- 原文（L138–L147）：

- "Motion in the amorphous domains constrained by crystallites"
- "Motions above Tg are often more complex, often involving coupled processes in the crystalline and amorphous domains"
- "Less easy to generalize - polymers often have to be considered individually"
### C3. Cross-linked Elastomers（交联弹性体）

- 出现在模量-温度图（L15–L16, L114–L115）中，代表橡胶平台区不塌陷的情况。
## D. 数学与机械模型

### D1. Relaxation Modulus G(t)（松弛模量）

- 原文公式：L156–L158 — "G(t) = σ(t) / γ0"
- 定义：阶跃应变下，应力随时间的衰减函数。
### D2. Creep Compliance J(t)（蠕变柔量）

- 原文公式：L159–L160 — "J(t) = γ(t) / σ0"
- 定义：阶跃应力下，应变随时间的增长函数。
- 关系：*"G(t) = 1/J(t)"*（L161–L163，简化的代数关系）
### D3. Hooke's Law（胡克定律）— Spring Model（弹簧模型）

- 原文公式：L231 — "σ = Eε"
- 代表：纯弹性响应。
### D4. Newtonian Fluid（牛顿流体）— Dashpot Model（阻尼模型）

- 原文公式：L242 — "τ_xy = η γ̇"
- 代表：纯粘性响应。
### D5. Maxwell Model（麦克斯韦模型）

- 组成：Spring（E）与 Dashpot（η）串联。
- 微分方程（L271–L275）：
> "dε/dt = dσ/(E dt) + σ/η"
- 应力松弛解（L356–L369）：
> "σt = σ0 exp[−t/τ], where τ = η/E, Relaxation time"
- 适用范围：Small loads and strains（线性区）。
- 局限性：无法描述蠕变恢复；与真实 S 形数据存在偏差（L396–L416）。
### D6. Time-Temperature Equivalence（时温等效）

- 位置：L81
- 意义：不同温度下的粘弹性曲线可通过水平移动（log a_T）叠加成主曲线。
## E. 实验与表征

### E1. DMA — Dynamic Mechanical Analysis（动态力学分析）

- 原文：L128–L129 — "a maximum in tan δ curves are observed in DMA experiments"
- 用途：测定 Tg、储能/损耗模量随温度变化。
### E2. Creep and Recovery（蠕变-恢复）

- 位置：L175–L190（图示）；L300–L321（Maxwell 预测）
- 组成：Elastic response + Retarded elastic response + Permanent deformation。
### E3. Stress Relaxation（应力松弛）

- 位置：L195–L220（实验数据图示）；L339–L369（Maxwell 推导）
- 测量定义：L77–L80 — "Stretch sample an arbitrary Amount, then measure the Stress required to maintain This strain. Then E(t) = σ(t)/ε"
## F. 参考文献与数据来源

- H. A. Flocke, Kolloid–Z. Z. Polym., 180, 188 (1962)（L148–L149）— 半结晶聚合物 DMA 数据图来源。
- Maxwell（历史人物）— Maxwell 模型命名来源（L277–L285）。
## G. 未找到原文对应的概念（标注）

- 广义 Maxwell 模型 / 松弛时间谱（Continuous Relaxation Time Spectrum）—— 文中通过"Maxwell model vs Real data"对比图暗示，但未给出广义 Maxwell 公式：[未找到原句]
- WLF 方程（Williams–Landel–Ferry）—— 时温等效的具体数学形式：[未找到原句]
- Arrhenius 方程 — 未在文中出现：[未找到原句]
- Rubber Elasticity Theory（橡胶弹性理论，νkT）—— 未在文中出现：[未找到原句]

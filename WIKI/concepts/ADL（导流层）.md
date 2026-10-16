---
type: concept
title: "ADL（导流层）"
domain: [卫材研发, 芯体与吸收]
status: growing
updated: 2026-09-29
tags: [ADL, 导流层, 热风粘合, ES纤维, 回渗, 重复冲击]
aliases: ["ADL（导流层 / Acquisition & Distribution Layer）"]
---

# ADL（导流层 / Acquisition & Distribution Layer）

> 一句话定义：纸尿裤面层与吸收芯体之间的**临时储液与横向铺展层**——它不是最终储存层，职责是把液体**快速摄入（acquire）→ 沿 MD 铺展（distribute）→ 高效下送芯体（transfer）**，并在重复冲击下保持低回渗。

## 机理 / 结构拆解

1. **三层职责分工**：ACQUIRE（面层→ADL 快速摄入）、DISTRIBUTE（ADL 内 MD 横向铺展）、TRANSFER（ADL→吸收芯体下送）。三者的共同约束是**空隙体积（void volume）**——空隙被压实或过粘合熔掉，三项指标同时恶化。
2. **性能差异只在重复冲击中显现**：首次冲击时纤维基本干燥，PE/PET 在新鲜亲水整理下表现良好；第 2/3 次冲击才分叉——**亲水整理被洗脱**、毛细连续性受损的一方会显著落后。
3. **驱动机理（摄入）**：表面润湿 + 垂直渗透率 + 临时孔隙体积共同决定摄入时间；整理耐久性决定后续冲击的衰减速度。
4. **驱动机理（MD 铺展）**：纤维网络的毛细连续性与未饱和孔隙长度决定铺展距离；铺展越宽，冲击点下方局部 SAP 饱和度越低、凝胶阻塞越轻。
5. **驱动机理（回渗）**：ADL 越能快速把液体下送、并在每次冲击后少留自由液，回渗越低；**过粘合会提高滞留液量**，与化学改良反向。
6. **结构实现**：主流为**穿透热风粘合（ATB）非织造**，粘结纤维用 ES（皮芯双组分）——皮层选择性熔融在纤维交叉点成粘合点。
7. **选材分层规则（本批结论）**：干爽优先处用 CoPET/PET（下层 ADL），触感柔软主张优先时保留 PE/PET（贴近面层）；不是非此即彼的整层替换。

## 关键参数表

| 参数 | 典型值 / 范围 | 出处 |
|---|---|---|
| ADL 构造（CoPET 模拟基准） | 穿透热风粘合，35 gsm，80 mm 宽，270 mm 有效长 | [[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]] |
| 冲击协议 | 3 × 60 mL 合成尿液，间隔 15 min，37 ℃ | [[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]] |
| 回渗协议 | 10 min 后滤纸湿回，轻压 | [[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]] |
| PE/PET 皮层熔点 | 约 130 ℃ | [[CoPET ADL 转型蓝图（皮层聚合物替代评估）]] |
| CoPET/PET 皮层熔点 | 110–180 ℃（可定制） | [[CoPET ADL 转型蓝图（皮层聚合物替代评估）]] |
| CoPET vs PE/PET 第 3 次冲击摄入 | -16% | [[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]] |
| CoPET vs PE/PET MD 铺展 | +17% | [[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]] |
| CoPET vs PE/PET 第 3 次回渗 | -24%（0.34 g → 0.26 g 级） | [[CoPET ADL 转型蓝图（皮层聚合物替代评估）]] |
| 最优共混比 | 30% CoPET / 70% PE/PET（可捕获 50–70% 收益） | [[CoPET ADL 转型蓝图（皮层聚合物替代评估）]] |
| 厚度控制目标 | ≤ ±3% vs 对照 | [[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]] |
| 放行门槛（第 3 次冲击） | 摄入 ≥10% 更快；铺展 ≥15% 更长；回渗 ≥15% 更低 | [[CoPET ADL 转型蓝图（皮层聚合物替代评估）]] |
| 手感放行 | 僵硬度惩罚 ≤10%（Handle-O-Meter/面板） | [[CoPET ADL 转型蓝图（皮层聚合物替代评估）]] |
| 老化验证 | 40 ℃ / 75% RH，2–4 周，渗透性无显著损失 | [[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]] |
| REL 型导流/增强层对照 | 24 gsm；首次穿透 0.65 s；第 3 次分布 54 cm²；第 3 次回渗 0.10 g | [[优化 REL 五纤维配方与穿透热风粘合工艺模拟]] |
| 竞品对照（ES 层添加比例） | 低熔点 PET 添加 15–50%；PE/PET 皮芯添加 20–40% | [[皮芯复合纤维]] |

> ⚠️ **口径警告**：CoPET/PET 的 -16% / +17% / -24% 均为**受控假定下的工程估算型模拟值**（原文声明「not vendor guarantees」），不是实测承诺。实测须走第 3 次冲击穿透/铺展/回渗与厚度回复的实验室门槛。

## 相邻概念

- 关键原料：[[CoPET（低熔点共聚酯）]]、[[皮芯复合纤维]]
- 工艺载体：[[热风粘合无纺布]]
- 相邻层：[[REL增强层]]、[[SAP错峰膨胀]]、[[分区密度设计]]
- 性能决定因素：[[亲水整理耐久性]]、[[毛细梯度设计]]、[[亲水-疏水梯度设计]]
- 对比：[[CoPET-PET 与 PE-PET 皮芯纤维对比]]、[[无纺布五大工艺对比]]

## 经验教训

> ✅ 验证（2026-09-29，来源 [[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]]、[[CoPET ADL 转型蓝图（皮层聚合物替代评估）]]）：两份同族文档对「ADL 是临时储液层、重复冲击才是分水岭」的定位一致，且都把**厚度/空隙体积**列为不可让步的验收红线。本页机理表述与来源一致。

- **教训一**：**只换纤维不重调工艺等于白换**。CoPET 粘合点更强，沿用 PE 烘箱温度会过粘合；厚度损失 ≥8% 即把干爽收益归零。
- **教训二**：**不要用单点穿透值选型**。首次冲击两者接近，决策应看第 3 次冲击 + 厚度回复 + 手感三项的组合。
- **待补 `[待验证]`**：ADL 空隙体积与穿透/回渗的定量关系；30% 共混在真实产线上的中试结果（本批仅到模拟与试验设计阶段）。

## 追加：Meeting Minutes 批（2026-09-29 追加 · Super embossing ADL：密实/蓬松复合与降克重）

> 来源：[[Nonwoven Supplier Capability & 3D Embossing Platform Review（标准录音 2）]]（供应商交流会 ASR 转写，会议日期 [待验证]）。本批只**追加**，不修改既有结论。

**Super（high）embossing ADL 的结构逻辑（本批新增）：**

- 在 I emboss / trench emboss 的**两侧做密实压合**、**中间保持蓬松**：两侧密实区提供**液体通过的通道（stream）**，中间蓬松区提供**缓冲（cushion）** → 把「密实型 ADL」与「缓冲型 ADL」两种功能合到一片材料上。
- 声称的效果：**增加多方向扩散（omni-directional diffusion）**。
- 已在某些公司的产品上商用化。

**降克重的实证口径（本批新增）：**

| Item 项目 | Value 数值 | Note 备注 |
| --- | --- | --- |
| 传统 ADL | **50 gsm** | 现有基准 |
| Super embossing ADL | **35 gsm** | 有公司切换后采用，理由是「不需要那么高 GSM」以拿到更好的市场价格 |
| 降幅 | 约 −30% | 供应商口径，非本方实测 [待验证] |

⚠️ 该降克重为**供应商转述的客户案例**，本方未验证；是否适用于本方产品仍属待决（参见 [[Nonwoven Supplier Capability & 3D Embossing Platform Review（标准录音 2）]]）。

✅ **验证记录（2026-09-29）**：35 gsm 替代 50 gsm 为供应商侧案例陈述，缺少扩散/回渗实测数据支撑；引用前须以本方台架或成品测试复核。参见 [[Core Channel Pattern（芯体通道花型设计）]]、[[COCO芯体平台]]。

## 追加：Meeting Minutes 批 2（2026-09-29 追加 · 异形纤维用于 ADL 的路线选择与添加量窗口）

> 来源：[[Bicomponent Fibre Production & Performance Review — Spinneret, Crimp & Functional Masterbatch（复合纤维生产及性能探讨）]]（ES 双组分纤维供应商工厂交流 ASR 转写，会议日期 [待验证]）。本批只**追加**，不修改既有结论。

**问题起点：想用异形（profiled）纤维提升 ADL 的扩散（本批新增）**

- 设想：把异形截面纤维用在导流层上，用沟槽**帮助液体扩散**。
- **失效机理（已识别）**：若用**双组分**异形纤维，在**熔融 / 热风粘合时外层 PE 融平**，中间沟槽形态**消失** → 扩散效果失效。

**路线选择（本批新增，会中达成一致）：**

| 路线 | 判断 | 理由 |
| --- | --- | --- |
| **单组分异形纤维** | **优先** | 不依赖熔融粘合 → 形态不被融平；成本更低；可塑性更好；**导液性也不错** |
| 双组分「全融掉」 | 不划算 | 融掉后等同于单组分，"不如直接用单组分" |
| 双组分「半融掉」 | 备选 | 可**部分保留形态**，从而**提高异形纤维的添加量上限** |

**添加量窗口（本批新增）：**

- ADL 上**不会 100% 使用**异形纤维，预计 **10–20%**；小批量先试 **5% / 10%**。
- **单组分添加不能太多**（比例受限）→ 这构成单组分路线的天花板。
- ⚠️ **关键未知**：本方明确"我们现在也不知道异形的添加多少是有效果的" → **有效添加量尚未确定**。

**可得性障碍（本批新增）：**

- 市面上**单组分异形纤维大部分在纺织业**，且以**高旦数**为主（2 旦 / 1 旦少见）。
- 纺织厂的**洁净度、文虫管控、终端质量要求**与卫材**不是一个级别**，很少有**单线专做卫材** → 需评估供给。
- 跨行业差异示例：纺织业多用**十字形**（透气透湿），但十字形**手感很差、非常粗糙** → 对卫材不适用。

✅ **验证记录（2026-09-29）**：以上为会中技术讨论 + 供应商口径，**无实测数据**；"融平失效"为机理推断。参见 [[皮芯复合纤维]]、[[福建闽瑞新合纤]]、[[三叶形截面纤维（Trilobal Fibre）]]。

## 来源

- [[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/REL/COPET.pptx.md`
- [[CoPET ADL 转型蓝图（皮层聚合物替代评估）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/REL/CoPET_ADL_Strategic_Blueprint.pptx.md`
- [[CoPET 采购蓝图：成本拆解与供应分层]] —— `RAW/ima_sync/个人知识库/WKB/Projects/REL/CoPET_Sourcing_Blueprint.pptx.md`
- [[CoPET 双组份热粘合纤维市场与供应商（供应链分层·明细表）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/REL/CoPET双组份热粘合纤维_市场与供应商_20260709_095959.xlsx.md`
- [[优化 REL 五纤维配方与穿透热风粘合工艺模拟]] —— `RAW/ima_sync/个人知识库/WKB/Projects/REL/REL simulation.pptx.md`
- [[纸尿裤核心技术与应用材料全景解析]] —— `RAW/ima_sync/个人知识库/WKB/Areas/纸尿裤核心技术与应用材料全景解析.pdf.md`

## Evidence Update 证据追加（2026-09-29）

> ✅ Verification（2026-09-29，source 来源 [[纸尿裤核心技术与应用材料全景解析]]）：本页既有「不要用单点穿透值选型」的教训未被修正；本批补上了**ADL 与 REL 的功能分界**与**五条可量化设计杠杆**。分界：REL 负责**垂直向的「收」**（瞬捕、暂存、下传；低密度大孔径、中空/卷曲纤维空气铺网、湿态锚固用 SBR 胶乳/VAE），ADL 负责**水平向的「导」**（纵向扩散、均匀分配至 SAP；中等密度定向孔径、高蓬松热风或开孔三维结构、低粘着以保表面多孔）。
>
> 五条杠杆（设计窗口）：① 旦尼尔分层——上层 >5 d 提供涌流空隙与骨架、下层 <5 d 提供毛细抽力；② 熔喷转向层 **15–50 gsm**，把上层液体「拔」向芯体以减少表层回渗；③ 多层密度梯度（顶层低密度高膨体蓄、底层高密度抽）形成单向驱动力；④ **漏斗形贯通孔 3–20 个/cm²**、突起朝芯体，形成单向阀（易进难出），兼减恶臭；⑤ 开孔窗口——70% 纤维直径 **12–22 μm**、开口面积 **35–65%**、0.5 kPa 下厚度 **0.8–1.2 mm**。
>
> 失效模式对照：REL 失效＝受压塌缩/吸水软化导致溢漏；ADL 失效＝导流不足或**凝胶堵塞**导致局部过载、回渗与侧漏——即两者的失效归因不可互换。
>
> ⚠️ 口径：以上设计窗口来自产业综述，未见本库内部实测对应；与本页既有 CoPET/REL 模拟结论**未做交叉验证**。
>
> 追加 `[待验证]`：15–50 gsm 熔喷转向层对本页既有 ADL 配方的叠加效果；漏斗孔在含黏稠负荷（稀便）下的单向阀有效性；开孔面积 35–65% 与 0.8–1.2 mm 厚度的联合公差。

### 追加（2026-09-29）· 更粗的导流层纤维为何是"常见的低回渗解法"

来源：[[Rewet Principles（回渗设计原则与测试方法关联）]]（Updated 10/22/25）。

> *"**Larger diameter surge fibers are a common low rewet solution because they target multiple causes of rewet.**"*

```
Increasing Fiber Size (at same basis wt) → Decreasing # of fibers → Decreasing surface area
for adhesion → Decreased capillarity → More chances of pores connecting → Less fluid trapped
on fibers / in pores → Fluid can drain out into core
```

（中文：**同克重**下增大纤维直径 → 根数减少 → 粘附表面积减少 → 毛细性下降 → 孔隙连通概率上升 → 滞留减少 → 液体排入芯体。）

- ⚠️ **取舍（源文明写）**：*"Since smaller fibers are perceived as softer, **softness and rewet are often opposites**"* —— **越细越软 → 柔软与回渗常相反**。
- ⚠️ **与上文"旦尼尔分层（上层 >5 d / 下层 <5 d）"的关系**：两者**都涉及纤维直径**，但上文出自**产业综述的导流设计窗口**，本条出自**K-C 内部回渗原则稿的解吸机制**，**来源与目的不同（导流 vs 低回渗），本页并列不换算**。
- **"少孔"的另一条路径**（源文举例）：*"Less pores (i.e.: **lower BW at same density**, **non-fibrous film surge**)"* —— 同密度下降低克重，或改用**非纤维 film surge**（表面积更低，可作**单向阀**）。

> 🔴 **manual_review（2026-09-29）**：源文为 **K-C 内部原则草稿（Draft 1/2/3 并存）**，含内部方法编号（TTM-00132 / TTM-00382 / STM-00109 等）与内部自评句；本页**只记机理与相对关系**，编号仅作追溯。

---

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · 导流层的换代主因与「已接近饱和」判断）

> 追加来源：[[Intake Systems Tech Pipeline（吸收系统技术管线 2025-11）]]（`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Intake/Intake Systems Tech Pipeline.pptx.md`，NA PC – Tech ICT – ADT）。
> **本追加不修正上方任何结论**；上方为**解吸机理与纤维直径/孔径**层面，此处补入**产业侧对导流层的换代判断**——**导流层已从「性能主战场」转为「成本与加工主战场」**。
> 🔴 **manual_review（2026-09-29）**：含竞品实测回渗值、内部项目代号与 `$/m²` 成本基线；**本页不复制成本基线数值**，仅记相对关系。

### 追加-1 · ★ 换代主因变了：**不是性能，而是降克重与加工性**

| 代次 | 代表 | 换代的理由 |
|---|---|---|
| 上一代 | **MOJAVE 系列**（多数品牌在用） | — |
| 当前回渗最优 | **Depend CT5（ATACAMA+）** | **回渗最优，但加工（converting）上有权衡** |
| 下一代 | **中空双组分（hollow bico）** | **在降低克重（降本）的同时改善加工性** |

> 📌 **对本页的改写性提示（重要）**：上方多数条目把导流层当作**性能件**讨论（孔径、耐压、大直径纤维降回渗）。本追加显示，**在管线图层面，导流层的换代理由已经是「降本 + 加工性」而非「性能」** ⇒ **评估导流层方案时，性能之外的两列（成本、可加工性）权重正在上升**。

### 追加-2 · ★「导流层已接近饱和」：下一步在导流层之外

原文：*"Adult care improvements focused on driving out all residual fluid via capillarity changes… **Mostly focused outside surge as surge is fairly good for residual fluid**"*

**DOE 支持（⚠️ 图像提取，仅取方向）**：TM:00623 低/高压二次回渗 DOE 中，**Total SAM 显著（P≈0.000）**、**Surge 不显著（P≈0.523）**。

**影像学支持**：**MicroCT 显示 Depend 湿润样品中，面层的水（顶部白色带）多于导流层（下方纤维网络）**。

> ⚠️ **两条支持的引用限制**：① DOE 表经图像提取，**列头与数值映射存疑**，本页**只取方向性结论，不引用 logworth 数值**；② MicroCT 判读受「**水与非织造布射线透射率相同**」限制（见 [[Rewet Principles History and Opportunity（2025-03-04 回渗总纲与历史沿革）]]），**须靠吸墨前后差值判读**。

### 追加-3 · 导流层自身的下一步假设：**收窄孔径分布**

原文假设：*"**Reducing pore size distribution will eliminate last drops of residual fluid**"*

> 📌 **与上方的关系（一个值得注意的张力）**：上方多条强调「**更大孔径 / 大直径纤维**降毛细持液」；本追加提出「**收窄孔径分布**」以消灭最后几滴残液。二者**不是同一维度**——前者是**孔径均值**，后者是**孔径分布宽度**。⇒ **导流层的孔径设计可能需要在「均值偏大」与「分布偏窄」之间同时优化**，本页**并列登记，不裁决**。

### 追加-4 · 与导流层耦合的三条邻层假设（**降克重的前提**）

| 邻层 | 假设 | 对本页的含义 |
|---|---|---|
| **Fluff 绒毛浆** | **卷曲纤维 / 绒毛浆混合**可能改善摄入 ⇒ **从而允许导流层降克重** | **导流层降克重不是孤立的**，需以绒毛浆侧补摄入能力为前提 |
| **Liner-Surge 贴合** | **胶**可形成孔网连通，**且没有 LSE 的副作用** | 为 [[Liner-Surge Embossing（面层-导流层压花）]] 提供**替代路线** |
| **Wrapsheet 包裹层** | **SMS 可能在抬高回渗——原因未知** | 导流层的收益**可能被包裹层抵消**，须系统联评 |

> 📌 **系统观提醒**：三条假设共同指向——**导流层的任何改动（尤其降克重）都必须在「面层 + 导流层 + 绒毛浆 + 包裹层」的系统里评估**，单独优化导流层可能无效。

## 追加：导流层的「毛细性–克重–孔径分布」三角权衡（2026-09-29 追加 · 来源：Rewet Update 2025-12-02 Depend 拆解）

- **毛细性不是单值指标**：Depend 导流层**毛细性优于 AD**，但**整体排液更差**，原因是**克重更高** → 高毛细性 + 高克重 = **持液更多、下送更慢**。评价导流层必须**同时看毛细性与克重**。
- **AD 侧的对偶问题**：AD 采用**低克重 + 高毛细性**，对 **intake 摄入不利**；其补偿手段是 **curly fiber 卷曲纤维**（改善摄入），且**卷曲纤维不影响回渗** —— 摄入与回渗的解耦手段。
- **我方反向路径**：试制**含卷曲纤维的 wrapsheet 包覆层**，看能否抵消「低克重/窄 PSD 导流层」带来的摄入损失（即：用包覆层补摄入，让导流层专心降回渗）。
- **孔径分布（PSD）是第一根因**：Depend 与 AD 平均孔径相近，但 **Depend PSD 更宽、大孔更多**；大孔抽不空小孔 → 液体滞留。因此导流层的开发目标应写成 **「窄 PSD」而非「更小/更大孔径」**（见 [[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]）。
- **供应侧**：Shalag 已提供候选样品，验证顺序为 **PSD 先筛、再上产品验回渗**（见 [[Shalag（Shalag 导流层与面层材料）]]）。
- **归因结论**：摄入互换实验中，**只换面层+导流层**（芯体不动）即把 Depend 回渗从 ~0.51 g 降到 0.15–0.17 g —— 导流层是回渗差距的主要承载件之一。
- 来源页 [[Rewet Update 2025-12-02（Raegan Informal · Depend 拆解与毛细机理）]]；量化方法 [[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]。

> 校验：本节为 2026-09-29 追加，**未修正上方任何结论**。

## Related Sources 关联来源

- [[2025.03.26 - Learning Cycle Update]]
- [[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]
- [[2D Absorption Model v8 Simulation Report（二维吸收模型 v8 仿真报告）]]
- [[Absorbent System Overview（K-C 吸收系统概览培训·2021-02）]]
- [[Absorbent Technology]]
- [[Absorbent Technology Introduction]]
- [[Absorbent Technology Textile Science and Technology]]
- [[Absorbent Technology_README]]
- [[Absorbent Technology_ch10_report_20260823_031404]]
- [[Absorbent Technology_master_index.csv]]
- [[Absorbent Technology_synthesis]]
- [[Adhesive Handbook Part 1 History and Information Resources]]
- [[Adhesive Handbook Part 2 Fundamental Aspects]]
- [[Air-Through Nonwoven Supplier Audit（热风无纺布供应商考察纪要·修订版 2026-08-21）]]
- [[Ancient Organic Dyes and Pigments Chemistry]]
- [[BCNF Nonwoven Application Status and Outlook（BCNF 无纺布应用现状与展望 · 2026-04-13）]]
- [[BNC 卫品技术可行性评估（Slide 大纲版，20260824）]]
- [[BNC 卫生用品技术可行性评估（访前尽调详细版）]]
- [[Bicomponent Fibre Production & Performance Review — Spinneret, Crimp & Functional Masterbatch（复合纤维生产及性能探讨）]]
- [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]]
- [[COCO V6 试产原料准备会（Summary 版）]]
- [[COCO V6 试产原料准备会（v2 Final）]]
- [[Characterisation, testing and modelling of nonwoven fabrics]]
- [[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]]
- [[CoPET ADL 转型蓝图（皮层聚合物替代评估）]]
- [[CoPET 供应基盘背调汇总（26 家企业·联系方式版）]]
- [[CoPET 双组份热粘合纤维市场与供应商（供应链分层·明细表）]]
- [[CoPET-PET vs PE-PET Cost Difference Analysis v3（成本差异分析报告 v3 · 卫材级对等口径）]]
- [[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]]
- [[Diaper Structure & ADL-REL Compendium（纸尿裤结构·ADL与REL辨析）]]


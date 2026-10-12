---
type: concept
title: "三叶形截面纤维（Trilobal Fibre）"
domain: [卫材研发, 纤维材料]
status: seed
updated: 2026-09-29
tags: [三叶形, 异形截面, MD沟槽, 导流, Lyocell, PE/PET, 皮芯复合纤维]
aliases: ["三叶形截面纤维（Trilobal Cross-section Fibre）"]
---

# 三叶形截面纤维（Trilobal Cross-section Fibre）

> 一句话定义：截面呈**三叶（三裂片）形**的化学纤维——区别于圆形截面，三叶的凹槽在纤网中形成沿纤维轴向的**连续低阻通道**，被用作面层/导流层的 **MD 沟槽导流**元件。

## 机理 / 结构拆解

1. **截面决定功能**：圆形截面纤维之间只有"点接触"，液体靠纤维间孔隙毛细力输运；三叶形截面的三个凹槽在纤维表面形成**轴向沟道**，纤网中相邻纤维的沟道叠加即成为**准连续的低阻导流路径**。
2. **方向性 = MD 沟槽**：梳理成网时纤维沿机向（MD）取向，沟道也随之沿 MD 排列 → 液体被**沿机向拉长铺展**，而非在冲击点堆积。这是"MD distribution / MD 铺展"指标的物理来源。
3. **两种载体**：
   - **PE/PET 皮芯型三叶形**（面层用）：三叶形截面 + 皮芯结构并存，兼顾导流与热粘合；COCO V6 面层上层仅放 10%、下层放 50%。
   - **三叶形莱赛尔（Lyocell）粘胶纤维**（芯包/水刺用）：用于 LSN 水刺非织造，主打湿态强度与亲水通道——对应 OI-08「Trilobal Lyocell for LSN」。
4. **配比的两难**：三叶形越多导流越好，但贴肤侧三叶形**手感偏硬**。COCO V6 的解法是 **Z 梯度分层**——整体 30%（15 gsm），但皮肤侧只放 5%。详见 [[ATB双梳理面层（Dual-Card Topsheet）]]。
5. **与分区密度的关系**：三叶形沟槽是"材料级的 MD 定向导流"，与 [[分区密度设计]] 的"孔径分区"同属"按位置定功能"的家族，但实现层级不同（纤维截面 vs 网面结构）。
6. **供给约束**：异形截面纺丝（尤其是皮芯 + 三叶形复合、细旦三叶形）产能有限，**异型纤维样本量直接决定能否上机**——COCO V6 的 Code 2-B 即为"去三叶形"的降级版。

## 关键参数表

| 参数 | 典型值 / 范围 | 出处 |
|---|---|---|
| 面层三叶形总占比 | 15 gsm（30%）；皮肤侧 5% | [[COCO V6 试产原料准备会（v2 Final）]] |
| 上下层三叶形配比 | 上层 10%；下层 50% | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| 三叶形供应商（PE/PET 3D Bico） | 福地（Fudy/Fudi） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| PE/PET 2D/4D 供应商 | 延江（Yanjan） | [[Coco V6 试产原料清单（Raw material list v3.0）]] |
| MD 分布增益（模型，面层） | +30%（v2 Final）/ +15%（Summary）⚠️ | [[COCO V6 试产原料准备会（v2 Final）]]、[[COCO V6 试产原料准备会（Summary 版）]] |
| CD 拉伸（面层） | 9.3 N/50mm（下限 8.0 N @600 m/min） | [[COCO V6 试产原料准备会（v2 Final）]] |
| LSN 用三叶形莱赛尔 | 水刺非织造，6 km，9/20 到天津 | [[COCO V6 试产原料准备会（Summary 版）]] |
| LSN 含三叶草粘胶实测基重 | 38.756 gsm（Wangjin） | [[CI-06 COCO V6 第三轮试产测试结果]] |
| 官方项目对应 | OI-25（30% trilobal MD grooves）；OI-08 Trilobal Lyocell for LSN；OI-07 Profiled Cross-section Fibre (LSN) | [[IPC BCC OI 项目清单 2026 v2（2026-09-17）]] |
| 漂定窗口（OI-08） | PE 130 ℃ flow-rounding window；配方已定 | [[IPC BCC OI 项目清单 2026 v2（2026-09-17）]] |

> ⚠️ **禁止无来源参数**：三叶形截面的**几何参数**（叶长比、沟槽深度、异形度 dtex 对应表）库内无来源，标 `[待验证]`。

## 相邻概念

- 结构载体：[[皮芯复合纤维]]、[[ATB双梳理面层（Dual-Card Topsheet）]]
- 工艺载体：[[热风粘合无纺布]]、[[SMS复合结构]]
- 导流家族：[[ADL（导流层）]]、[[毛细梯度设计]]、[[分区密度设计]]
- 纤维成纤性：[[成纤性判据]]、[[原纤化]]
- 对比：[[COCO V6 Liner 方案对比（Code 1 vs Code 2-A vs Code 2-B）]]

## 经验教训

> ✅ 验证（2026-09-29，来源 [[IPC BCC OI 项目清单 2026 v2（2026-09-17）]]）：官方 OI 清单同时把三叶形写进 **OI-25（面层，30% MD grooves）** 与 **OI-08（LSN 用三叶形莱赛尔）**，说明该纤维截面在本库是**跨部件复用的设计元件**，而非单一面层的局部选择。既有判断未被修正。

- **要点**：三叶形的收益是**方向性的**（MD 而非 CD），评估时必须看 MD 分布指标，用各向同性指标衡量会低估其价值。
- **风险**：**供给与手感是两大约束**——异型纤维样本量决定上机，贴肤侧占比决定手感，二者共同限定配比上限。
- **待补 `[待验证]`**：三叶形截面参数与 MD 铺展增益的定量关系；三叶形莱赛尔在 LSN 水刺中的实测爬坡数据（本批复测仅含水率与爬坡 51.1 mm）。

## 追加：Liner 项目批（2026-09-29 追加）

> 本节为 **Liner 项目批（批次 S1_Projects_Liner_01，5 份资料）** 编译时的追加记录，**不改动上方既有结论**。上方「截面决定功能 / 方向性 / 配比的两难 / 供给约束」四条判断在本批全部仍成立，本节补充的是**定量物理参数、剂量窗口与工艺窗口**。

### 1. 本批新增的三叶形定量参数

| 参数 | 数值 / 范围 | 出处 |
|---|---|---|
| 沟槽半径 r_groove（3.3 dtex 三叶形） | ≈2–3 µm（对照纤维间孔径 40–80 µm） | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 沟槽吸力 | ≈40–50 kPa（θ→20°、γ≈66 mN/m）；孔隙网络仅 ≈1–2 kPa | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 吸力倍数 / 表面积增益 | 10–30×；同旦数表面积约为圆形 300% | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 已发表芯吸排序 | 4DG > 三叶形 > 圆形 | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 三叶形 PET 推荐线密度 | 2.2 / 3.3 dtex（细旦给吸力、粗旦给透气与梳理运行性） | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 切断长度（按层） | 38 / 44 / 51 mm（越长＝越长的连续 MD 沟槽） | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 卷曲 | 6–10 cpi（卷曲会把沟槽折出 MD 方向，取梳理可容忍的最低值） | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 干热收缩 | ≤3% @150 ℃（须热定型；未定型 PET 在烘箱中收缩→幅宽损失、边卷、CD 皱） | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 强度 | 4.5–5.5 cN/dtex（对比 ES 双组分 2.5–3.0） | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 45 gsm 四层替代方案（Option B） | A1 12 gsm 0% / A2 13 gsm 25% / B1 10 gsm 40% / B2 10 gsm 45% → 合计 11.75 gsm = 26%，**贴肤 0%** | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 模拟 MD 铺展（第三次冲击） | 145 mm（全 ES）→ 163 mm（15%）→ 188 mm（26%） | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 模拟 CD 拉伸 | 9.3 N/50 mm（下限 8.0 N）；粘合模型 k≈0.55、交点约 41% PET | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 圆角三叶形设计窗口（25 gsm 面层） | **10–20 wt%（起 15%）@1.5–2.0 dpf**；筛选矩阵评分 4/4/4/4/4/4/5（综合第一） | [[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]] |
| 45 gsm 双梳理上机工艺窗口 | 第 1 梳理道夫牵伸 1.15–1.25（MD/CD≈2:1）；第 2 梳理 1.45–1.60（≈4:1）；烘箱 132–136→138–142 ℃；停留 +10–15%；风速 1.2–1.5→1.4–1.8 m/s | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 转化失效（HIGH 风险） | 含 PET 面层的超声封合：PET 在 PP/PE 超声参数下不软化，表现为未粘合填充物 | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]]、[[Ultrasonic Bonding of PET-Containing Topsheet]] |
| 面层 DOE 中的三叶形剂量（本批口径） | C1/C2/C3/C4 上层均 10%；下层 50%（3D 福地三叶形） | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |

### 2. 验证记录

> ✅ 验证（2026-09-29，来源 [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]]、[[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]]、[[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]]、[[ATB Topsheet with Bico Spunbond for 600 mpm Ultrasonic Lamination]]）：本页既有四条判断全部被本批**支持**——①「截面决定功能」由沟槽吸力定量（40–50 kPa vs 1–2 kPa）补齐；②「方向性＝MD 沟槽」由 MD 铺展 +30% 模拟与"约 2/3 收益来自沟槽网络"佐证；③「配比的两难」由四份来源的剂量上限（≤15%/≤20 wt%）与**贴肤层 0%** 的分层解法确认；④「供给约束」被进一步收紧为**"卫生级整理 + 低收缩的三叶形单组分 PET 供方基数窄于圆形 ES，须认证两家来源"**。未发现矛盾。

- **追加要点一（截面规格要写清）**：采购规格必须索取**叶瓣轮廓图**，不能只写"trilobal"——沟槽半径直接决定吸力。
- **追加要点二（两条最常被漏的规格）**：**低收缩（≤3% @150 ℃）**与**耐久多次冲击亲水整理**是最常漏项，且都只在试产后以"幅宽损失 / 第三次冲击渗漏"形式暴露。
- **追加要点三（反向风险）**：40–50 kPa 的沟槽网络本身是储液体，芯体接近饱和时可能"抢液" → 第三次冲击的回渗须与 MD 铺展同步评估（详见 [[Groove Capillary Suction]]）。
- **追加 `[待验证]`**：本批 MD 铺展与 CD 拉伸增益**全部为模拟值**；Option C（38%）的铺展数值在提取中未解析；产线实测（含 385 mm 芯体端部效应）缺失。

## 追加：OI 直属文件批（2026-09-29 追加）

> 本节为 **S1_Projects_(直属文件)_02 批次（5 份 OI 资料）** 编译时的追加记录，**不改动上方既有结论**（含 Liner 项目批的定量参数）。本批补充的是**官方清单口径、自研队列与项目关系定性**。

### 1. 官方清单口径（与既有页互证）

| 项 | 官方口径 | 出处 |
|---|---|---|
| OI-25 面层结构 | **ATB dual-layer PE/PET bico 50 gsm，4 铺层 / 2 梳理系统**；三叶形 PET **30%（15 gsm）**、**贴身侧仅 5%**；Z 梯度 MD 沟槽网络 | [[IPC BCC OI Project List 2026-09-18（重构版·19 项）]]、[[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]] |
| 铺层明细 | A1 90% ES 2D 22.5 gsm ／ A2 10% 三叶形 3D 2.5 gsm（上）；B1 50% ES 4D 12.5 gsm ／ B2 50% 三叶形 3D 12.5 gsm（下） | 同上 |
| 实测 / 模型 | CD 拉伸 **9.3 N/50 mm**（下限 8.0 N @600 m/min）；MD 分布**模型 +15%**（目标 30%） | 同上 |
| 验收判据 | 回渗 <5.9 g @34 min（产品门）；1st STT ≤0.8 s；MD 扩散 ≥+15%（目标 30%）；湿态 MD ≥75 N/m | 同上 |
| 项目关系定性 | **OI-08（三叶形莱赛尔 / 纤维级选型）与 OI-25（三叶形 PE/PET / 织物结构级）为同一技术链的上游与下游**，非重复立项；自 2026-09-16 口径起各自独立保留、汇报相邻呈现 | [[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]] |

### 2. 自研队列与价格参考

| 供应商 | 形态 | 状态 | 出处 |
|---|---|---|---|
| 福地 Fudi | 3D 三叶形 **bico PE/PET** | 300 kg 已备，待试 | [[IPC BCC OI Project List 17.9.2026（供应商明细版）]] |
| 益盟 Emon | 十字形 / 哑铃形 **mono PET**（1.5D×38 / 3.5D×38） | 等下一轮商业化生产；NDA 待推进 | [[IPC BCC OI Project List 2026-09-18（重构版·19 项）]]、[[Emon Jiangsu（江苏益盟）]] |
| 江南高纤 | 异形喷丝板能力（Y 形/哑铃形） | 已走访，能力已确认 | [[IPC BCC OI Project List 17.9.2026（供应商明细版）]] |
| 兰精 Lenzing | 三叶形莱赛尔（trilobal lyocell）能力 | 待探索；样品原计划 8 月底 | 同上、[[兰精集团]] |
| 中纺 Chinatex | 三叶草喷丝板（与兰精同源技术） | 价格参考 ≈ RMB 11/kg vs 兰精常规码 ≈ RMB 17–18/kg（**市场级参考价，非谈判价**） | 同上 |

### 3. 验证记录

> ✅ 验证（2026-09-29，来源 [[IPC BCC OI Project List 2026-09-18（重构版·19 项）]]、[[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]]）：本页既有「整体 30% / 贴肤 5%」「方向性＝MD 沟槽」「供给与手感两大约束」三条判断**全部被官方清单与大纲支持**，未发现矛盾；并**新增一条项目治理结论**——三叶形在两份文件中分别以"纤维级"（OI-08）与"织物结构级"（OI-25）立项，属上下游而非重复。

- **追加 `[待验证]`**：三叶形（trilobal）与其他异形截面（Y 形、哑铃形）的**同条件对比数据**在本批来源中缺失；三叶形莱赛尔的实测流平镜检结果未在本批给出。

## 追加：Meeting Minutes 批（2026-09-29 追加）

> 本节为 **S5_Areas_Meeting Minutes_01 批次（产品研发与实验计划研讨）** 编译时的追加记录，**不改动上方既有结论**（含 Liner 批与 OI 直属文件批的定量参数、剂量窗口与工艺窗口）。本批补充的是**分层加量口径与耐热性取舍**。

### 1. 本批新增参数与口径

| 项目 | 本批口径 | 备注 |
|---|---|---|
| 分层加量 | 上层 **10% 或 0%**，下层 **10%** | 以「后端验证」为约束，贴肤侧压到 0% 与既有页「贴肤层 0%」互证 |
| 手感影响 | 下层 10% 对手感影响不大，**对透光度有影响**；Home PET 三叶草会增加手感硬度/蓬松度 | 实品待确认 `[待验证]` |
| 耐热性取舍 | 白口 PET 表面耐温约 **130 ℃**，复合 PET 约 **220 ℃** | 三叶草异形截面经两道加温（CW 输入 + 超声波）会流平，耐热高者异形度损失小 |
| 供方 | 现用**福地（白口三叶草）**（拿来主义，有现成料）；长期偏好 **Home PET** | 与既有页「须认证两家来源」方向一致 |
| 非热熔纤维上限（梳理机） | 约 **15%** 以内可调，超过需上机试；蚕丝类建议 **8–10%**，加 1% 混不匀 | 通用梳理稳定性边界 |

### 2. 验证记录

> ✅ 验证（2026-09-29，来源 [[Product Development & Trial Plan Workshop（产品研发与实验计划研讨）]]）：本页既有「方向性＝MD 沟槽」与「配比的两难」两条被本批支持——三叶草纤维被明确放在 **CW 上层用于 MD 方向导流**，且为了避免手感/异形度损失而把贴肤层降到 0%；同时本批**新增一条工艺约束**：异形截面会**在两道加温下流平**，故「耐温更高的 PET」是保住异形度的选型条件。原结论未被修正。

## 追加：COCO V6 第二轮实验批（2026-09-29 追加）

> 本节为 **S5_Areas_Meeting Minutes_01 批次（[[COCO V6 Trial Round-2 Review（录音纪要 2026-09-16）]]）** 编译时的追加记录，**不改动上方既有结论**。本批给出的是**热窗口这一硬约束与分层加量方案**。

### 1. Thermal window 本批新增的工艺硬约束

- **142 ℃ 以上异形截面会流平**（丧失截面形状）→ 三叶草纤维存在明确的**热窗口上限**；当前打样压到 **139 ℃ 以下**。
- 该约束来自两道加温叠加（梳理输入加温 + 超声波加温），与既有页「复合 PET 耐温约 220 ℃ vs 白口 PET 约 130 ℃」一致且**更严格**。

### 2. 分层加量方案（本批）

| 层 | 方案 | 备注 |
|---|---|---|
| 上层 | 约 **10%** 粘胶三叶草（蓝晶 `[待验证]`） | 目标 MD 导流；当前用白口（拿来主义） |
| 下层 | 约 **20–30%** Home PET 三叶草 | 后续拟从白口切到 Home PET |
| 打样克重 | 上层 25（22 + 2.5 小? `[待验证]`），下层 25 | 温度 139 ℃ 以下 |

### 3. Platform / supply constraints 平台与供方约束

- **平台要求**：热风供应商必须**双梳理、且每个梳理双投料** —— 对供应商能力要求高，可选供方基数窄。
- **有效性待验证**：三叶草在**服装行业**确实能大幅提高导流，但**在卫材成品上是否同样有效，尚未验证**（工程师设想，需用平台验证）。

> ✅ 验证（2026-09-29，来源 [[COCO V6 Trial Round-2 Review（录音纪要 2026-09-16）]]）：本页既有「供给约束」判断被本批**进一步收紧**——从「须认证两家来源」升级为「**必须具备双梳理 + 双投料的平台能力**」；同时**新增一条硬约束**：**142 ℃ 流平的热窗口上限**。**原结论未被修正**。

## 追加：Meeting Minutes 批（2026-09-29 追加 · 10% 分层配置、打样米数与温度窗口）

> 来源：[[COCO V6 Trial Code Design & Process Alignment（录音纪要 2026-08-17）]]（2026-08-17 ASR 转写）。本批只**追加**，不修改既有结论。

**已决的实验配置（本批新增）：** 三叶草（三叶形）纤维的开发目的为「给客户做 V6」；本轮按**分层配置**分两个 code：

| Code | 上层配置 | 下层配置 | Note 备注 |
| --- | --- | --- | --- |
| A | 含 **10%** 三叶形截面纤维 | 不含（0%） | 目的：液体一进入即提供**平面扩散** |
| B | 不含 | 含 **10%** | 反向对照 |

- 旦数约束：常规面层为两弹（2 denier [待验证]），三叶形纤维**只有三弹**（3 denier [待验证]）可选，「这个没办法选，因为它就是三弹的」→ 分层时旦数无法对齐，属已知不可控变量。
- 复合顺序：上下层各 15 g 单独成层 → 在延江处复合为 30 g 面层（转写「岩浆」[待验证]）→ 再到传越做超声波 bonding 粘合 ADL。与巴西方案同构。

**打样与工艺（本批新增，均为待决 / [待验证]）：**

- 打样米数：300 m/卷 × **6 卷 ≈ 1,800 m**（另一口径为 1,000 m）[待验证]。
- 长度与跑偏的权衡：「做长了之后就跑偏」→ 只能**跑低速度**以换取长度，能长一点更好。
- 温度窗口：需**跑不同温度**以平衡强度与纤维形态；具体温度点 [待验证]。
- 未决：为何用 Be max 方案而非让延江直接做完（会议中提出但未解答）。

✅ **验证记录（2026-09-29）**：分层 10%/0% 与 0%/10% 的双 code 设计为已决方案；打样米数、温度点、旦数口径均来自 ASR 转写，标 `[待验证]`，引用前须与实验记录核对。参见 [[COCO V6 Trial Code Design & Process Alignment（录音纪要 2026-08-17）]]、[[COCO芯体平台]]、[[Ultrasonic Bonding of PET-Containing Topsheet]]。

## 追加：Meeting Minutes 批（2026-09-29 追加 · "流平"失效机理与加工温度窗口的验证方法）

> 来源：[[Material Portfolio & Process Priorities Review — SAP, Trilobal Fibre & Masterbatch（材料及工艺相关探讨）]]（内部材料团队讨论 ASR 转写，会议日期 [待验证]）。本批只**追加**，不修改既有结论。

**核心失效机理：流平（本批新增，最重要）**

- **加异形纤维的目的**是**增加比表面积**；一旦在热风烘箱中温度过高，异形截面会被**流平变圆** → **"白加"**。
- 因此三叶形纤维的关键不是"能不能纺出来"，而是"**加工后形态还保不保得住**"。

**温度窗口与材料熔点（本批新增）：**

| Material 材料 | Melting point 熔点 | Implication 含义 |
| --- | --- | --- |
| **PE** | ≈ **130 ℃** | 温度窗口最低，最容易被流平 |
| **PBT** | ≈ **185 ℃** | 中间 |
| **PET** | ≈ **220 ℃** | 温度稳定、"稳得很"，但 **bonding 全靠 ES**，强度可能偏低 |

→ **永远是"形态保持"与"bonding strength"的平衡**：温度越低越保形，但 bonding 强度有风险。

**验证方法（本批新增，可直接执行）：**

1. 先向热风厂（延江）索取**当前的烘箱设定温度** —— 注意：**熔点 130 ℃ 只是材料属性，不是工艺温度**；设定温度可能高于熔点（如 135 ℃）。
2. **设定温度 ≠ 实际温度**：只能监控设定温度，两者之间可能存在 **2–5 ℃** 偏差；这个 delta 正是流平与否的关键。
3. 在产线上**以设定温度为基准往下调**，利用连续运行时烘箱的降温过程**分段收样**（例如跑 130 ℃ 收一批、降到 128 ℃ 再收一批、126 ℃ 再收一批），共 **3 批**。
4. 三批样送实验室测**拉伸强度**；**只要 bonding strength 能接受，就取低温样** —— 低温样形态保持最好。
5. 若热风厂对烘箱能力有信心（设定即实际），仍应**额外做出更低温度的样品**做对照。

**实践含义（本批新增）：**

- 该温度参数**只对特定产线有效** —— "这个设定温度只在延江的那条线上有效；以后配方给别人做，温度还要重新找"。因此**不要让纤维厂在自己的设备上验证**，意义有限，应**直接上目标产线验证**。
- 层结构方案：上层 **10% 三叶草 + 90% ES**，ES 部分拆成 **50/50**（用福地的 ES）。

✅ **验证记录（2026-09-29）**：熔点数值（130 / 185 / 220 ℃）与 2–5 ℃ delta 为会中口径 [待验证]；三批样方案为**计划**，**尚未执行**，无实测结果。参见 [[热风粘合无纺布]]、[[福地（Fudi）]]、[[延江（Yanjan）]]、[[COCO芯体平台]]。

## 追加：Meeting Minutes 批（2026-09-29 追加 · 梳理层分工、粘胶 vs PET 的亲水差异与 +20–30% MD 扩散目标）

> 来源：[[V6 & Be Max Materials Alignment — Profiled Fibre, Colour Spunbond & SAP Layering（录音纪要 2026-08-06）]]（K-C 内部项目对齐会 ASR 转写，2026-08-06）。本批只**追加**，不修改既有结论。

**ATB 双梳理中的层间分工（本批新增）：**

| 梳理层 | 纤维 | 用量 |
| --- | --- | --- |
| **第一梳理** | **苏州纯 PET 三叶形** | **10%** |
| **第二梳理** | **福地白口三叶形** | **可多加一点** |

- 目标：提升面层扩散，量化指标为 **MD 方向尿液分布（MD urine distribution）+20–30%**。
- 配比建议：若未涨价则 **50 / 50**（三叶形 50 配 50）；若偏贵则降。
- 本方判断："**大部分是价格的问题，而不是功能的问题**" → 主要障碍是成本。

**三叶形粘胶 vs 三叶形 PET（本批新增，是材质选择的关键机理）：**

| 材质 | 亲水性 | 结论 |
| --- | --- | --- |
| **粘胶（viscose / rayon）** | **本身亲水** | 同样三叶形，**导流优于 PET** |
| **PET** | **本身疏水（聚水）** | 三叶形增比表面积的收益被疏水性抵消一部分 |

- 实例：**蓝鲸** = **三叶形粘胶纤维**（原用于「碳矿」[待验证]，现移到水刺布上）；原理同样是**三叶形增加比表面积以增加导流**。
- 可考虑**把 10% 的三叶形 PET 换成蓝鲸粘胶** —— 关键仍是价格。
- 水刺路线的便利：粘胶也好、PET 三叶形也好，**在水刺机上直接梳理进去就行**。

**验证要点（本批新增，三个并列指标）：**

1. 对 **pattern（花型）**改善有没有帮助；
2. **皮肤手感有没有变糙**（柔软性）；
3. **performance** —— **MD distribution 的扩散长度有没有增加**；
4. 目标是**找到平衡点**，不是单向最大化。

✅ **验证记录（2026-09-29）**：+20–30% 为**目标值而非实测值**；50/50 为报价前的建议配比；「粘胶亲水、PET 疏水」为机理判断，未见对比测试数据 [待验证]。参见 [[ADL（导流层）]]、[[ATB双梳理面层（Dual-Card Topsheet）]]、[[COCO芯体平台]]。

## 追加：Meeting Minutes 批（2026-09-29 追加 · homo PET 上限 30%、+15% MD 分布目标与中间层粘合强度缺口）

> 来源：[[Be Max Platform — Trilobal Fibre Ratio, Ultrasonic Bonding & MD Distribution Target（纤维加工温度与成本验证）]]（跨团队技术交流，英文 ASR 转写，会议日期 [待验证]）。本批只**追加**，不修改既有结论。

**配比与目标（本批新增）：**

| Item 项目 | Value 数值 | Note 备注 |
| --- | --- | --- |
| 第一梳理三叶形 | **10%** | — |
| **homo PET 三叶形上限** | **30%** | 上限，非推荐值 |
| 目标收益 | **MD urine distribution 长度 +15%** | **理论值**，待实测 |
| 逻辑链 | 分布更长 → **更好地利用 SAP** | 与 [[ADL（导流层）]] 的"扩散—利用率"链条一致 |

**关键工艺缺口（本批新增，与本页既有"流平"失效机理同源）：**

- **三叶形纤维（尤其 homo PET）加得越多，中间层的 bonding strength 越不确定** —— 这是本平台**尚未解决的关键未知**。
- **温度是根因**：不同聚合物熔点差异大（PP vs PET / homo PET）→ 现有加工温度下，异形截面容易被"流平"，且层间粘合不足。
- **提出的解法**：**工程改性 PP，把加工温度降到接近 130 ℃（即 PE 的熔点）**，从而与现有 bicomponent / TBCW 体系兼容 —— 本方判断"近期应可行"，但**仍在推进中**。

**由此得到的认知（本批新增）：**

1. **异形纤维的收益有配比上限**：不是越多越好 —— homo PET 上限 30% 的背后是**中间层粘合强度**的约束。
2. **温度窗口是异形纤维的通用门槛**（与本页既有结论一致）：PE ≈ 130 ℃ 是参照锚点；要让 homo PET 异形纤维存活，要么**改材料（低温 PP）**，要么**改工艺（降加工温度）**。
3. **"+15% MD 分布"目前是理论值** —— 与 [[Be Max Platform — Trilobal Fibre Ratio, Ultrasonic Bonding & MD Distribution Target（纤维加工温度与成本验证）]] 中"10 月拿初始样品"的排程对应，属**待验证目标**而非实测。

✅ **验证记录（2026-09-29）**：+15% 为**理论推算**，非实测；"PP 改性至 130 ℃"**仍未落地**；"中间层 bonding strength 未知"是本方自述的缺口 [待验证]。参见 [[Ultrasonic Bonding of PET-Containing Topsheet]]、[[皮芯复合纤维]]、[[ADL（导流层）]]。

## 来源

- [[Coco V6 试产原料清单（Raw material list v3.0）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Raw material list for Coco V6 trial.xlsx.md`
- [[IPC BCC OI Project List 2026-09-18（重构版·19 项）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/IPC BCC OI Project List - 20260918 (Restructured).xlsx.md`（2026-09-29 追加）
- [[IPC BCC OI Project List 17.9.2026（供应商明细版）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/IPC BCC OI Project List - 17.9.2026.xlsx.md`（2026-09-29 追加）
- [[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/IPC BCC OI 材料开发团队 2026 年度汇报大纲_v7_红白配色与标题栏加倍版.md.md`（2026-09-29 追加）
- [[COCO V6 试产原料准备会（英文版，2026-09-11）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_EN.pptx.md`
- [[COCO V6 试产原料准备会（v2 Final）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_v2_Final.pptx.md`
- [[COCO V6 试产原料准备会（Summary 版）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_Summary.pptx.md`
- [[IPC BCC OI 项目清单 2026 v2（2026-09-17）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/IPC_BCC_OI_Project_List_2026_v2_EN_20260917.pptx.md`
- [[CI-06 COCO V6 第三轮试产测试结果]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/CI-06 COCO V6 3rd round trial.xlsx.md`
- [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/Trilobal_PET_Liner_MD_Distribution.pptx.md`
- [[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/pentagram_free_shaped_PET_alternatives_8slides.pptx.md`
- [[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/pentagram_PET_diaper_liner_deep_dive 1.pptx.md`
- [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/KC_Diffusion_Enhanced_Topsheet_v3.xlsx.md`

---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_c1f1a85f6213b35a878b2ca3a525bb44001a693ee6c0644e"
source_file: "LCE自供电光子传感器_拆解.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mechanochromic_Photonic_Sensors_拆解/LCE自供电光子传感器_拆解.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# LCE自供电光子传感器_拆解.md.md

# Self-Powered Photonic Sensor Using Cholesteric Liquid Crystal Elastomer-Based Sandwiched Architecture with Mechanochromism and Triboelectric Response — 深度拆解报告

文献来源：Cheng Xue, Haonan Sun, Yuting Tang, Jie Wei, Jinbao Guo (Beijing University of Chemical Technology), ACS Applied Materials & Interfaces, 2025 (DOI: 10.1021/acsami.5c10756)。
本报告基于所提供 txt 文件（该文件为该论文的 Supporting Information，S1–S9，共 131 行）进行拆解。所有引文、数据、行号均严格取自 txt 内部行号；正文（Main Text）中未在 txt 中出现的数据一律标注 "[未找到原句/行号缺失]" 或注明 (推演)。
核心概念：CLCE = Cholesteric Liquid Crystal Elastomer（胆甾相液晶弹性体）；PDMS = 聚二甲基硅氧烷；AgNWs = 银纳米线；SI = Supporting Information。

## 1. 核心论点 (Core Thesis)

- 论文提出一种 自供电 (self-powered) 光子传感器，采用 "PDMS–CLCE–PDMS" 三明治 (sandwiched) 结构，将胆甾相液晶弹性体（CLCE）的力致变色 (mechanochromism) 与摩擦电响应 (triboelectric response) 耦合于同一器件（行 5–7、51–52）。
- CLCE 层的结构色可随拉伸发生可逆变化：初始红态（P0 = 438 nm）拉伸后螺距减小至蓝态（P1 = 285 nm），即"红→蓝"的机械变色，为应力/形变提供无需染料的肉眼/光谱双重读出（行 77–78、38–40）。
- 器件为自供电传感：通过 PDMS-CLCE-PDMS 摩擦电体系输出开路电压（VOC）、短路电流（ISC）与电荷密度（QSC），无需外部电源即可感知机械刺激（行 5、51–52、124–125）。
- 材料体系兼具自修复 (self-healing) 与可拉伸特性：CLCEs-S 膜在 80 °C 下愈合（行 68），自修复 PDMS 可拉伸（行 100），AgNWs 部分包埋于柔软 PDMS 中充当柔性导电层（行 106–108）。
- 器件颜色可通过手性剂含量精确调控（5.8% / 6.4% / 7% 分别对应红 / 绿 / 蓝 CLCE 膜，行 38–40），说明配方可设计、可调色，具备面向不同应用场景的工程可调性。
- 总体技术主张：以"弹性体 + 液晶光子结构 + 摩擦电"的集成架构，实现可拉伸、自修复、自供电、可视化的多模态机械传感——是柔性可穿戴/智能纺织方向的代表路线之一（行 5–7、51–52）。
## 2. 关键概念操作性定义

每项 = 原文术语 + 原文逐字句（含 txt 行号）+ 中文释义。凡 txt 中无逐字原句者，标注 "[未找到原句/行号缺失]"。

- 

Self-Powered Photonic Sensor

- 原文（行 5–7）："A Self-Powered Photonic Sensor Using Cholesteric Liquid Crystal Elastomer-Based Sandwiched Architecture with Mechanochromism and Triboelectric Response"
- 释义：自供电光子传感器——器件利用摩擦电效应自身发电，无需外接电源即可完成力学信号的探测与输出；"光子"指以 CLCE 结构色（光子带隙反射）作为传感读出通道。
- 

Sandwiched Architecture / PDMS-CLCE-PDMS

- 原文（行 51–52）："Figure S3. Schematic flow diagram of the preparation of a self-powered sensor based on PDMS-CLCE-PDMS structure."
- 释义：三明治架构——CLCE 活性层被两侧 PDMS（其一掺杂 AgNWs 作电极/封装层）夹持，构成"软-光子-软"复合结构，兼顾保护、导电与可拉伸性。
- 

Mechanochromism

- 原文（行 6）：*"...with Mechanochromism and Triboelectric Response"（标题；行 77–78 给出机制性证据："the pitch decreased from P0 = 438 nm to P1 = 285 nm"*）
- 释义：力致变色——机械应变改变 CLCE 螺旋螺距，使选择性反射波长（颜色）移动（红→蓝），实现"拉伸即变色"。
- 

Triboelectric Response

- 原文（行 7）：*"...with Mechanochromism and Triboelectric Response"*（标题）
- 释义：摩擦电响应——不同材料接触-分离时表面电荷转移产生电信号（VOC/ISC/QSC），是该传感器"自供电"的电学读出通道。
- 

Chiral agent LC756

- 原文（行 25–26）："Figure S1. Molecular structures of chiral agent LC756, liquid crystal monomer RM82, chain extender EDDET, crosslinking agent PETMP, and Irgacure 651."
- 释义：手性剂 LC756——赋予液晶体系螺旋超结构（胆甾相）的组分；其含量（5.8%/6.4%/7%）直接决定 CLCE 反射颜色（红/绿/蓝，行 38–40）。
- 

Liquid crystal monomer RM82 / Chain extender EDDET / Crosslinking agent PETMP / Irgacure 651

- 原文（行 25–26）："Figure S1. Molecular structures of chiral agent LC756, liquid crystal monomer RM82, chain extender EDDET, crosslinking agent PETMP, and Irgacure 651."
- 释义：CLCE 光聚合配方体系——液晶单体 RM82（网络骨架）、扩链剂 EDDET（调节交联密度与柔顺性）、交联剂 PETMP、光引发剂 Irgacure 651（紫外引发聚合）。这四者与 LC756 共同构成可打印/可浇铸的光固化液晶弹性体配方。
- 

Pitch（螺旋螺距）

- 原文（行 77–78）："The pitch changes of CLCE in the initial red state and the stretched blue state were tested by SEM. It was found that the pitch decreased from P0 = 438 nm to P1 = 285 nm."
- 释义：胆甾相螺旋的螺距，直接决定选择性反射波长；拉伸使螺距由 438 nm 缩至 285 nm，对应反射色由红变蓝，是 mechanochromism 的微观机制。
- 

Self-healing（自修复）

- 原文（行 68）：*"Figure S5. (a)-(c) Microscopic photographs of CLCES-S films healed at 80 °C."；另见行 100："Figure S8. Optical photographs of the stretching process of self-healing PDMS films."*
- 释义：材料在受损后（此处 CLCEs-S 于 80 °C 加热、PDMS 经拉伸）可自行愈合恢复功能，延长器件寿命，是柔性可穿戴应用的关键可靠性指标。
- 

Silver nanowires (AgNWs) / AgNWs-doped PDMS

- 原文（行 106–108）："The PDMS doped with AgNWs was observed under the SEM, and it was found that the AgNWs were partially encapsulated within the soft material PDMS, which had a certain degree of stickiness."
- 释义：银纳米线导电填料——AgNWs 部分包埋于柔软且具一定黏性的 PDMS 中，构成可形变、贴合皮肤的柔性导电层（电极）。
- 

Reflectance spectra / 结构色

- 原文（行 38–40）："Figure S2. (a) Reflectance spectra of red, green and blue CLCE films prepared with different chiral agent contents (5.8%, 6.4%, 7%). (b) Optical photographs of red, green and blue CLCE films prepared with different chiral agent contents (5.8%, 6.4%, 7%)."
- 释义：反射光谱是表征 CLCE 结构色（光子带隙）的标准手段；不同手性剂含量得到不同反射峰，从而呈现红/绿/蓝三色，证明颜色可配方化调控。
- 

Open-circuit voltage (VOC) / Short-circuit current (ISC) / Charge density (QSC)

- 原文（行 124–125）："Figure S10. The open-circuit voltage (VOC), short-circuit current (ISC) and charge density (QSC) of the PDMS-CLCE-PDMS sensor."
- 释义：摩擦电传感器的三大电学输出指标——开路电压、短路电流与转移电荷密度，定量刻画自供电能力；本 SI 未给出具体数值（数值在正文，[未找到原句/行号缺失]）。
- 

CLCEs-S film（自修复型 CLCE 膜）

- 原文（行 63）："Figure S4. FT-IR spectra of (i) the CLCE film (black line) and (ii) the CLCEs-s film (red line)."
- 释义：经改性（引入自修复基元，S 后缀）的 CLCE 膜，用 FT-IR 与普通 CLCE 对比确认化学结构变化；其在 80 °C 下可愈合（行 68）。
## 3. 证据链 (Evidence Chain)

以下数据全部出自本 txt（SI），行号见各表。正文中未包含的数值（如 VOC 具体伏值、循环次数）在 txt 中不存在，一律标注 "[未找到原句/行号缺失]"。

### 表 1：材料组成与配方 (Material Composition & Formulation)

|||||
|---|---|---|---|
|Chiral agent LC756|手性剂，含量调控反射色|行 25–26、38–40|结构式给出（Figure S1）；5.8%/6.4%/7% 含量 → 红/绿/蓝膜|
|Liquid crystal monomer RM82|液晶单体（网络骨架）|行 25–26|Figure S1 结构式|
|Chain extender EDDET|扩链剂|行 25–26|Figure S1 结构式|
|Crosslinking agent PETMP|交联剂|行 25–26|Figure S1 结构式|
|Irgacure 651|光引发剂（UV 聚合）|行 25–26|Figure S1 结构式|
|CLCE film vs CLCEs-S film|普通膜 vs 自修复膜（FT-IR 对比）|行 63|黑色谱线 (i) vs 红色谱线 (ii)，确认化学结构差异|
|PDMS（无色透明、自修复）|封装/弹性基体|行 95、100|无色透明膜（Figure S7）；自修复 PDMS 拉伸过程（Figure S8）|
|AgNWs-doped PDMS|柔性导电层/电极|行 106–108、113|AgNWs 部分包埋于柔软黏性 PDMS（SEM，Figure S9）|

### 表 2：器件架构与制备 (Device Architecture & Fabrication)

|||||
|---|---|---|---|
|器件总架构|PDMS-CLCE-PDMS 三明治结构|行 51–52、124–125|"self-powered sensor based on PDMS-CLCE-PDMS structure"（Figure S3 流程图）|
|传感模式|Mechanochromism + Triboelectric Response 双通道|行 5–7|标题即架构与双机制声明|
|供电方式|Self-powered（无外接电源）|行 5、51|标题与 Figure S3 图题|
|变色驱动|拉伸（stretching）|行 77–78、83|初始红态→拉伸蓝态，SEM 测螺距变化（Figure S6）|
|自修复条件|CLCEs-S 膜 80 °C 愈合|行 68|Figure S5 显微照片|
|电极/封装|AgNWs 部分包埋于 PDMS（具黏性）|行 106–108|SEM 观察（Figure S9）|

### 表 3：光学/机械变色性能 (Optical & Mechanochromic Performance)

|||||
|---|---|---|---|
|三色反射光谱|红/绿/蓝 CLCE 膜的 Reflectance spectra|行 38–40|Figure S2(a)，不同手性剂含量对应不同反射峰|
|三色光学照片|红/绿/蓝膜目视颜色|行 38–40|Figure S2(b)|
|初始螺距 P0|438 nm（红态）|行 77–78|"pitch decreased from P0 = 438 nm to P1 = 285 nm"|
|拉伸后螺距 P1|285 nm（蓝态）|行 77–78|同上|
|变色方向|红→蓝（蓝移，高能量）|行 77–78、83|SEM 截面图（Figure S6）佐证螺距收缩|
|响应速度/灵敏度|具体数值|—|[未找到原句/行号缺失]（正文数据，本 SI 未含）|

### 表 4：电气/摩擦电输出与自修复 (Electrical/Triboelectric Output & Durability)

|||||
|---|---|---|---|
|Open-circuit voltage (VOC)|PDMS-CLCE-PDMS 传感器|行 124–125|Figure S10 给出 VOC 曲线（具体数值见正文，[未找到原句/行号缺失]）|
|Short-circuit current (ISC)|同上|行 124–125|Figure S10 给出 ISC 曲线（具体数值 [未找到原句/行号缺失]）|
|Charge density (QSC)|同上|行 124–125|Figure S10 给出 QSC 曲线（具体数值 [未找到原句/行号缺失]）|
|自修复温度|CLCEs-S 膜 80 °C 愈合|行 68|Figure S5 (a)-(c)|
|可拉伸性|自修复 PDMS 拉伸过程|行 100|Figure S8 光学照片|
|耐久循环次数|具体循环数|—|[未找到原句/行号缺失]（正文数据，本 SI 未含）|

## 4. 文章结构 (Paper Architecture)

所提供 txt 为论文 Supporting Information（S1–S9），共 7 个技术小节，逐层为正文的核心主张提供证据支撑：

- S1. 原料分子结构（行 20–26）：给出 CLCE 光聚合体系全部原料结构式（LC756、RM82、EDDET、PETMP、Irgacure 651），确立"配方可复现"的化学基础。
- S2. 三色 CLCE 膜反射光谱与照片（行 32–40）：证明颜色可由手性剂含量精确调控（5.8%/6.4%/7% → 红/绿/蓝），支撑"结构色可设计"的主张。
- S3. PDMS-CLCE-PDMS 传感器制备流程（行 46–52）：给出三明治器件制备路线图，衔接材料与器件。
- S4. FT-IR 与自修复特性（行 58–68）：用 FT-IR 对比 CLCE 与 CLCEs-S 确认结构改性；80 °C 愈合显微照片佐证自修复，支撑可靠性主张。
- S5. 拉伸前后 CLCE 截面 SEM（行 74–83）：螺距 438 nm → 285 nm 的直接观测，是 mechanochromism 机制的微观证据链核心。
- S6. PDMS 膜表征（行 90–113）：无色透明、可拉伸自修复、AgNWs 部分包埋——支撑柔性封装与导电电极设计。
- S7. 电学性能表征（行 119–125）：VOC/ISC/QSC 三大摩擦电输出，支撑"self-powered"主张。
整体论证逻辑（结合 SI 结构推断正文，标注 (推演)）：原料（S1）→ 颜色可调（S2）→ 器件制备（S3）→ 自修复可靠性（S4、S6）→ 变色机制（S5）→ 自供电输出（S7），即"材料化学基础 → 光子性能 → 器件集成 → 双机制（机械变色+摩擦电）验证"的递进式证据链，最终落点在"自供电、可拉伸、自修复、可视化"的多模态传感应用主张。

## 5. 业务连接点 (Business Connections)

面向纸尿裤/湿巾等卫生材料 R&D 与采购。行号均出自本 txt；(推演) 标注为合理推测，非论文原文结论。

- 免电池的尿湿/压力可视化指示器（(推演)）：CLCE 的"红→蓝"机械变色（行 77–78：pitch 438 nm → 285 nm）与三色可调配方（行 38–40）表明，结构色可作免染料、免电源的视觉指示。可推演路径：将 CLCE 层与纸尿裤 SAP 溶胀/芯体膨胀耦合，SAP 吸水膨胀产生的应变触发 CLCE 变色，实现"尿湿即变色"的肉眼指示（替代现有 pH 染料指示条）；颜色由手性剂含量定制（行 38–40）便于按品牌色设计。此为推演，论文未做 SAP/湿敏实验。
- 自供电传感降低智能穿戴/智能包装供电成本（(推演)）：器件以摩擦电输出 VOC/ISC/QSC（行 124–125），无需电池；对卫生用品（智能尿裤、湿巾包装防拆/挤压检测）而言，可避免电池与皮肤接触的安全与回收问题。摩擦电信号作为"应变/接触"事件计数通道，适合低频人体活动监测；具体灵敏度、循环寿命需查正文（本 txt 未含）。
- 自修复+可拉伸 = 延长贴身产品寿命与舒适性：自修复 PDMS（行 100）与 80 °C 愈合的 CLCEs-S（行 68）意味着柔性传感器在反复弯折/拉伸后可恢复功能；对纸尿裤腰围、腿围等高频形变区域（(推演) 集成电子后）可显著提升耐用性，降低"传感失效"客诉风险。
- AgNWs-PDMS 柔性导电层 → 无纺布/水刺布上柔性电路参考（(推演)）：AgNWs 部分包埋于柔软黏性 PDMS（行 106–108），说明"纳米线导电网络+弹性封装"是耐形变电极的可行工艺；采购端可关注银纳米线浆料与 PDMS 弹性体供应链，评估其在非织造基材涂覆/印刷的可行性与成本（银价波动敏感）。
- 特种光聚合配方物料的供应链/采购清单：CLCE 体系依赖 LC756（手性剂）、RM82（液晶单体）、EDDET（扩链剂）、PETMP（交联剂）、Irgacure 651（光引发剂）（行 25–26）——均为小批量特种化学品，供应商集中、交期长，若立项开发需提前锁源；同时"结构色免染料/免颜料"（行 38–40）契合卫生材料对皮肤接触安全与无重金属染料的合规诉求（(推演) 安全与环保卖点）。
## 6. 金句索引 (Quotable Index)

本小节为唯一中译区。逐字摘自 txt；行号即 txt 内部行号。

行 5–7：
"A Self-Powered Photonic Sensor Using Cholesteric Liquid Crystal Elastomer-Based Sandwiched Architecture with Mechanochromism and Triboelectric Response"
译文：一种基于胆甾相液晶弹性体三明治架构、兼具力致变色与摩擦电响应的自供电光子传感器。

行 25–26：
"Figure S1. Molecular structures of chiral agent LC756, liquid crystal monomer RM82, chain extender EDDET, crosslinking agent PETMP, and Irgacure 651."
译文：图 S1. 手性剂 LC756、液晶单体 RM82、扩链剂 EDDET、交联剂 PETMP 与光引发剂 Irgacure 651 的分子结构。

行 38–40：
"Figure S2. (a) Reflectance spectra of red, green and blue CLCE films prepared with different chiral agent contents (5.8%, 6.4%, 7%). (b) Optical photographs of red, green and blue CLCE films prepared with different chiral agent contents (5.8%, 6.4%, 7%)."
译文：图 S2. (a) 以不同手性剂含量（5.8%、6.4%、7%）制备的红、绿、蓝 CLCE 膜的反射光谱；(b) 相应三色 CLCE 膜的光学照片。

行 51–52：
"Figure S3. Schematic flow diagram of the preparation of a self-powered sensor based on PDMS-CLCE-PDMS structure."
译文：图 S3. 基于 PDMS-CLCE-PDMS 结构的自供电传感器制备流程示意图。

行 63：
"Figure S4. FT-IR spectra of (i) the CLCE film (black line) and (ii) the CLCEs-s film (red line)."
译文：图 S4. (i) CLCE 膜（黑线）与 (ii) CLCEs-s 膜（红线）的 FT-IR 光谱。

行 68：
"Figure S5. (a)-(c) Microscopic photographs of CLCES-S films healed at 80 °C."
译文：图 S5. (a)–(c) 在 80 °C 下愈合的 CLCES-S 膜的显微照片。

行 77–78：
"The pitch changes of CLCE in the initial red state and the stretched blue state were tested by SEM. It was found that the pitch decreased from P0 = 438 nm to P1 = 285 nm."
译文：采用 SEM 测试了 CLCE 在初始红态与拉伸蓝态下的螺距变化，发现螺距由 P0 = 438 nm 减小至 P1 = 285 nm。

行 95：
"Figure S7. Optical photograph of a colorless and transparent PDMS film."
译文：图 S7. 无色透明 PDMS 膜的光学照片。

行 106–108：
"The PDMS doped with AgNWs was observed under the SEM, and it was found that the AgNWs were partially encapsulated within the soft material PDMS, which had a certain degree of stickiness."
译文：在 SEM 下观察掺杂 AgNWs 的 PDMS，发现 AgNWs 部分包埋于柔软且具有一定黏性的 PDMS 材料内部。

行 124–125：
"Figure S10. The open-circuit voltage (VOC), short-circuit current (ISC) and charge density (QSC) of the PDMS-CLCE-PDMS sensor."
译文：图 S10. PDMS-CLCE-PDMS 传感器的开路电压（VOC）、短路电流（ISC）与电荷密度（QSC）。

### 附：可靠性声明

- 本报告引用的全部英文原句均逐字摘自 txt（行号对应），未做任何改写或拼接；所有"[未找到原句/行号缺失]"处为该信息（如 VOC 具体数值、循环次数、灵敏度）在 SI 文本中不存在，需查正文原文（DOI: 10.1021/acsami.5c10756）。
- 业务连接点中标注 (推演) 的条目为面向卫生材料场景的合理推测，非论文所述实验结论。


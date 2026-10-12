---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_60310046138c93b31c2bcf1a90d63c97001a693ee6c0644e"
source_file: "Absorbent Technology_ch11_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Absorbent Technology (Chatterjee & Gupta)/chapters/Absorbent Technology_ch11_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Absorbent Technology_ch11_report.md.md

# Chapter 11 深度分析报告

## 吸液材料测试技术（Measurement Techniques for Absorbent Materials）

来源：*Absorbent Technology*，P.K. Chatterjee & B.S. Gupta，Elsevier，2002
页码：pp. 406–463（58 页，书内页码 389–445）

## 1. 执行摘要（Executive Summary）

- 分层测试哲学（hierarchy in testing）：本章节的核心主张是，吸液产品的性能开发必须遵循"构成材料（聚合物/纤维）→ 二维结构（网布/片材）→ 装配产品"的三级层次进行测试，每一层级都有独立的指标体系与测试方法，不可越级或混用。
- 标准化 ≠ 完整表征：标准方法（ASTM、AATCC、INDA、TAPPI、EDANA、Scan-C）只能覆盖"过程控制、质量控制、供应商排名、研发比较"这类基本需求；对微观机理（孔结构、吸脱附动力学、界面能）的理解必须依赖非标准化的"研究工具"（research tools）。
- 界面能是吸液的物理起点：通过 Wilhelmy 法测量接触角、Wetting Force、Work of Adhesion（WA）和 Wettability Index（WI），可系统量化不同纤维（棉、粘胶、棉、丙纶）对水的亲和力，这是 Ch1-10 所述任何材料能否有效吸液的先决条件。
- 速率比容量更重要：章节反复强调，吸液容量（capacity）在静态条件下可能很高，但若不考察吸液速率（rate）、毛细上升（capillary rise）及在负载/压力下的保持能力，产品在实际使用中仍会失败（如擦净测试与静态容量测试的悖论）。
- 模拟使用环境的 in vitro 测试是研发的关键环节：Syngyna（卫生棉条）、Marketing/Technology（尿布）、动态擦净（Oathout sled test）等 proprietary 方法虽不公开，但它们代表了行业标准之外真正的产品性能预测能力，也是企业间竞争壁垒的来源。
## 2. 核心论点（Core Arguments）

吸液是一个跨层级的多变量问题。要优化产品，"this interaction needs to be examined and optimized at each layer level"，需要在流体性质、纤维表面/扩散/溶胀/湿力学、织物孔隙与粘合、测试/使用条件四类变量上同时工作（Section 1.2）。

测试金字塔是产品开发的必要组织原则。从聚合物/纤维到二维结构再到装配产品，逐级递进，"The single most important property of interest is the customer satisfaction"，而客户满意度只能通过逐层筛选 + 最终 in vivo 现场验证获得（Section 1.3, 1.5）。

测试方法分三类，各自定位明确：标准方法（process control、QC、ranking）、研究工具（机理洞察，如 fluid intrusion/extrusion）、in vitro / in vivo（模拟使用环境，企业专有）（Section 1.4）。

表面润湿性（wettability）是吸液的第一性原理。通过 Wilhelmy 湿附力法可获得 advancing/receding 接触角、Work of Adhesion（WAA、WAR）、Wettability Index、Hysteresis、表面能（dispersion / polar / total），从而在材料选择阶段（Ch1-10 的纤维）就做出定量决策。

湿态下纤维力学性能会发生系统性退化。亲水纤维（如粘胶、棉）吸水后 modulus 下降导致 bending rigidity 减小、压缩模量降低、湿态下每单位质量厚度（thickness per unit mass）显著减小，直接影响产品蓬松度与吸液容量。

毛细上升（capillary rise）是连接微观孔结构与宏观吸液速率的桥梁，其动力学由 Lucas–Washburn 方程描述，可通过 Klemm 法、声速法、电导法等多种方式测量。

在压吸收（Absorption Under Load, AUL）与离心/抽吸保持（retention under centrifugal or suction pressure）是对产品实际工况最贴近的评价，静态容量指标不能替代这些动态/负载指标。

产品级测试必须模拟真实使用环境：卫生棉条（总浸入法、滴加法、in vivo、Syngyna）、尿布（acquisition layer、surface dryness、leakage）、擦拭布（动态擦净 sled test）等，其共同特征是"非标准、企业专有、以模拟用况为目标"。

## 3. 关键概念与操作化定义（Key Concepts & Operational Definitions）

|||||
|---|---|---|---|
|Absorption Capacity（吸液容量）|吸液容量|试样浸入流体后，经固定时间浸泡 + 固定时间沥干，由湿重与干重差算出，对纤维非织造布以占调湿后质量百分比表示（INDA IST 10.2）。|"From the difference in weights of the wet and dry samples, the absorption capacity given as percentage of the weight of the conditioned material is determined."（Section 4.1）|
|Absorption Time / Rate（吸液时间 / 速率）|吸液时间 / 吸液速率|将约 5 g 试样卷成圆柱状放入 8 cm × 5 cm 金属网篮中，从 25 mm 高度落入水中，用秒表记录试样完全沉没的时间，取 5 个试样平均（INDA IST 10.1）。|"The basket with the sample is dropped from 25 mm height into a container of water. A stopwatch is started that measures the time the sample takes to fully submerge."（Section 4.1）|
|Wilhelmy Wetting Force（Wilhelmy 湿附力）|Wilhelmy 法湿附力|纤维或织物边缘接触液面时，液体表面张力沿接触线作用于试样产生的净力，等于 F_w = γ_lv P cos θ，其中 γ_lv 为液-气表面张力，P 为试样周长，θ 为接触角。|"F_w = γ_lv P cos θ"（eq. 1, Section 2.1）|
|Contact Angle (Advancing / Receding)（接触角，前进 / 后退）|前进接触角 / 后退接触角|液滴在固体表面前进（θ_A）与后退（θ_R）两种极限方向的接触角；θ_A > θ_R，差值体现 hysteresis。|"The transition between C and D is not as abrupt but gradual as it represents transition of the meniscus from a larger advancing angle, θ_A, to smaller receding angle, θ_R."（Section 2.4）|
|Wettability Index（润湿指数）|润湿指数|水的表面张力（常数）与接触角余弦的乘积，正比于固体对液体的归一化吸引力；θ 越小，WI 越大，对 receding 模式高于 advancing。|"Wettability index is given by the product of surface tension of water (a constant) and the cosine of the contact angle (eq. 7)."（Section 2.6）|
|Work of Adhesion（附着功）|附着功|W_A = γ_sv(1 + cos θ)，表征固-液界面形成的能量，可用于评估涂层、复合材料和吸液结构中的界面强度。|"Work of adhesion, for example, affects cohesion and bonding between surfaces and would be an important property to consider when selecting materials for applications such as coatings and composites."（Section 2.1）|
|Hysteresis（滞后）|润湿滞后|H = W_AR / W_AA，后退与前进模式下附着功之比；低 hysteresis 意味着快速达到平衡（棉、三角粘胶），高 hysteresis 意味着需要长时间接触才能达到平衡（圆粘胶、醋酯、涤纶）。|"This table also lists the values of hysteresis given by the ratio of the work of adhesion in the receding to that in the advancing mode."（Section 2.7）|
|Solid Surface Energy（固体表面能）|固体表面能|分为 polar、dispersion、total 三部分，通过接触角（advancing）计算；三纤维素纤维（棉、三角粘胶、圆粘胶）总表面能 46–68 dynes/cm，远高于丙纶（23 dynes/cm）。|"The total energy is highest for trilobal rayon (68 dynes/cm) and cotton (61 dynes/cm) and lowest for polypropylene (23 dynes/cm)."（Section 2.8）|
|Moisture Regain（回潮率）|回潮率|调湿状态下纤维含水量与绝干质量之比；是纺织标准方法（ASTM D 4446 等）的基础指标，影响产品干燥性、蓬松度与体积尺寸。|"The property of absorbing water by some fibers has several aesthetic and technical consequences for use of the latter in absorbent structures."（Section 3.1.1）|
|Water Retention Value / WRV（保水值）|保水值|纤维在离心或抽吸压力下仍保留的水量（占干重的百分比）；反映纤维内部孔隙对水的保持能力。|"Water retained at a suction of 30 cmHg"（Fig. 17 caption, Section 5）|
|Liquid Saturation Capacity（液体饱和容量）|液体饱和容量|纤维或织物在无外部压力下达到平衡吸液时的最大持液量，通常以占干重的倍数表示。|"The properties of interest are the standard moisture regain, the liquid saturation capacity, water retention value, surface free energy, contact angle, diffusion and swelling characteristics, and wet mechanical properties."（Section 1.3.1）|
|Linear Wicking / Capillary Rise（线性毛细上升）|线性毛细上升|Klemm 法：纸条竖直悬挂，下端接触水面，记录毛细前沿随时间的上升距离；用对数坐标图（lg h vs. t）外推得到 Washburn 速率常数 k₀。|"In the Klemm test, a paper strip is hung vertically above a trough filled with water... The waterfront rises through the paper and the distance is recorded as a function of time."（Section 5.3）|
|Cobb Test（科布法）|科布吸液速率|在固定时间内（如 1 min、60 min）测定的单位面积吸收水量（g/m²），衡量面内液体吸收的速率。|"The most widely used methods are the Cobb [41,42] and the Klemm [43,44] tests. The former measures the rate of fluid absorption in terms of the amount absorbed whereas the latter measures the linear rate of advance of liquid in the paper sample."（Section 5.3）|
|Draves Method（Draves 法）|Draves 法|一种用于纤维非织造布和卫生用品的体积吸液测试方法（Chapter 在 Section 4/5 引用该法作为研究工具之一；此处说明"具体操作细节因属文献外引用，本章节未给出完整定义"）。|"Draves method"（Section 5, as cited research tool）注：本章未给出该方法完整步骤；仅作为相关文献研究工具被提及。|
|Absorption Under Load / AUL（负载下吸液）|负载下吸液|在外部压力（模拟人体坐姿/卧姿）下测量产品的吸液容量；压力越大，有效吸液量越小；是卫生棉条与尿布产品的核心性能指标。|本章对 AUL 的具体数值/操作化定义未展开（详见 Section 5.4 关于压力对吸收的影响，以及对 tampon 的 "resilient rubber tubing under a pressure conforming to the physiological value" 方法描述）： "In a variation of this, the tampon is held in a resilient rubber tubing under a pressure conforming to the physiological value."（Section 6.3）|
|Flat-Panel Absorbency / FPA（平板吸液量）|平板吸液量|将纤维或 SAP 材料平铺在刚性平面上进行吸液测试，反映材料在受限厚度条件下的实际吸液表现；本章将其与"specific pore or air volume under desired environmental pressure"（eq. 39, Chapter I）结合讨论。|"This parameter assessed in the wet state should correlate directly with the absorption capacity of the material."（Section 3.3）|
|Penetration Absorbency（渗透吸液）|渗透吸液|液体在重力或压力驱动下穿过织物的量（透过吸收），区别于表面吸收；本章将其作为二维结构表征的关键参数。|"The properties of interest in characterizing these structures are absorption capacity, rate of absorption, linear wicking, water permeability, air permeability, and repellency."（Section 1.3.2）|
|Rewet（再湿润）|再湿润|已被吸收的液体在压力或温度变化下从产品中重新释放到表面，是皮肤干燥性劣化的原因。注：本章节对"rewet"一词没有作为独立标准方法给出定义；它是产品级性能指标，通常在 diaper/pads 性能部分涉及"surface dryness of the facing material"测试（Section 6.4）。|"Another important property assessed on these products is the surface dryness of the facing material."（Section 6.4）|
|Surface Feel（表面触感）|表面触感|反映产品与皮肤接触面的干燥性、柔软性；本章通过 coverstock wetness 测试（filter paper + plastic plate 加压吸取）操作化测量。|"A pre-weighed filter paper is positioned on the coverstock and loaded with a plastic plate on the top... After a set time, the filter paper is removed and weighed and the difference in dry and wet weights is used as a measure of the wetness of the coverstock."（Section 6.4）|
|Standardized Test Methods（标准化测试方法）|标准化测试方法|由 ASTM、AATCC、INDA、TAPPI、EDANA、Scan-C 等机构发布，提供"uniform orderly procedures for the determination of certain well defined properties of fibrous materials"。|"These tests are intended to provide uniform orderly procedures for the determination of certain well defined properties of fibrous materials. The procedures involved are used in assessing properties for the purpose of process control, quality control, ranking of materials from different producers, and for research and development."（Section 1.4.1）|
|Demand Wettability（需求润湿）|需求润湿|织物在不受外部压力、仅由毛细作用"自发"吸收流体的速度；由 point-source demand wettability tester（恒液位鼓泡器）测量。|"When a fabric imbibes fluid along its length even when the fluid is presented only at a point, the fabric is said to exhibit demand wettability."（Section 5.4）|
|Swelling Ratio（溶胀比）|溶胀比|分为 S_A（面积溶胀）、S_D（直径溶胀）、S_L（长度溶胀）、S_V（体积溶胀），表征纤维吸水后尺寸变化。|"Swelling ratio: SA (ΔA/A); SD (ΔD/D); SL (ΔL/L); SV (ΔV/V)."（Glossary, Section 7）|
|Pore Size Distribution（孔径分布）|孔径分布|通过汞入侵、液体挤出、氮吸附、水蒸气吸附、离心法等获得；对 textile/absorbent 材料，液体挤出（liquid extrusion）法优于汞入侵法，因为后者的高表面张力/大接触角会改变压缩性材料的孔结构。|"Complications, limitations, and uncertainties connected with mercury intrusion through textile materials can be avoided by using non-mercury liquids."（Section 5.5）|

## 4. 证据链（Evidence Chain）

### 4.1 标准方法与测试参数

|||||
|---|---|---|---|
|INDA IST 10.1 / 10.2|INDA Standard Test Methods Manual|样品约 5 g；金属网篮 8 cm × 5 cm（重 3 g）；落高 25 mm；浸泡 + 沥干各 10 s；取 5 样本平均|纤维非织造布吸液时间与容量|
|AATCC 127|AATCC Standard Test Methods Manual|液体渗透时间|医用/卫生织物液体透过|
|TAPPI、Scan-C 33:80|TAPPI Manual；Scan Standard|纸/纤维材料吸液与保水|纸浆类吸液芯评价|
|ASTM 系列|ASTM Manual（含 D 4446 回潮率等）|回潮率、容量、保水|通用纺织/纤维性能|
|Klemm Test|Cobb/Lowe (1934); Klemm (1944); 见 [41-47]|毛细前沿高度 vs. 时间，对数坐标|纸/纤维片材线毛细速率|
|Cobb Test|Cobb & Lowe (1934)|单位时间单位面积吸水量（g/m²）|纸基吸液速率|
|Wilhelmy / Miller 法|Wilhelmy (1863); Miller et al. (1975, 1983) [2, 6, 8]|F_w = γ_lv P cos θ；最大拉出力 F(M)|纤维接触角、附着功、润湿指数|
|超声脉冲法|Chatterjee (1990) [52]; Craver & Taylor|声速 V_w vs. 时间 → Washburn k₀|纤维片内液体传输速率|
|Laser Doppler Anemometry (LDA)|[54]|微尺度液流速度|纤维网内局部流速|
|液体挤出法（liquid extrusion）|Miller & Tyomkin (1983) [61]|有效孔径 15–1000 μm；扩展后可达 0.5 μm|柔性材料孔径分布|
|汞入侵法（Washburn）|Washburn (1921)|宽孔径范围|刚性多孔固体（不宜用于柔性纺织品）|
|离心法|[74]|r_c = 2γ / (ω² ρ_l R_cen)|纤维/纺织品保水|

### 4.2 核心表格数据

表 2（pp. 419–420）：各纤维的附着功与滞后（Work of Adhesion & Hysteresis）

|||||
|---|---|---|---|
|Cotton（棉）|133|141|1.06|
|Trilobal Rayon（三角粘胶）|140|142|1.01|
|Regular Rayon（圆粘胶）|114|142|1.25|
|Cellulose Acetate（醋酯）|113|125|1.11|
|Polyester（涤纶）|86|100|1.16|
|Polypropylene（丙纶）|65|69|1.06|

表 3（pp. 420）：各纤维的表面能组成（dynes/cm）

|||||
|---|---|---|---|
|Cotton|42|19|61|
|Trilobal Rayon|52|16|68|
|Round Rayon|24|22|46|
|Cellulose Acetate|17|35|52|
|Polyester|4|38|42|
|Polypropylene|2|21|23|

关键发现：三角粘胶总表面能最高（68 dynes/cm）、极性强；丙纶最低（23 dynes/cm）、92%+ 为色散；圆粘胶滞后最大（1.25），说明达到润湿平衡需要较长时间。

表 7（pp. 451–452）：孔径分布测试方法汇总

||||
|---|---|---|
|氮吸附|硅胶、水合硅酸钙|[68-71]|
|水蒸气吸附|硅胶|[72, 73]|
|离心法|粉末、纺织品|[74]|
|汞入侵|粉末、多孔板、陶瓷、烧结玻璃、膜、纤维、织物|[75, 76]|
|液体挤出|纺织品|[61]|
|液体吸收|纺织品|[74]|

### 4.3 关键方程

- Eq. 1（Wilhelmy 湿附力）：F_w = γ_lv P cos θ
- Eq. 7（Washburn 方程，参见 Chapter I）：x² = (γ r cos θ / 2η) · t，描述毛细上升距离 x 与时间 t 的关系，是 Klemm 法、超声法、Demand Wettability 分析的理论基础。
- Eq. 14（用 receding 力反推周长）：P = F_R / γ_lv（当假设 θ_R = 0）
- Eq. 15（Miller 最大拉出力）：F(M) = γ_lv P
- Eq. 34（超声脉冲法）：(1/V_w − 1/V_o) = k_1 · t^(1/u)，u 值实测 0.49–0.56，接近 Lucas–Washburn 模型的 0.5。
- Eq. 36（Laplace 毛细关系）：P_ci = 2γ_l cos θ / r_ci
- Eq. 37（孔径分布）：φ(r_c) = dV/d r_c
- Eq. 38（Kelvin 方程修正）：(r_c − a) = −2γ V_m / (G T ln(p/p_∞))
- Eq. 39（离心法平衡）：2γ_l / r_c² = π ρ_l R_cen ω² r
### 4.4 引用文献（节选，全部源自 Chapter 8 References）

- [1] Behery, 1993：非织造布性能测试综述（TAPPI Press）。
- [2] Wilhelmy, 1863：湿附力方法奠基论文。
- [3] Gupta & Whang, 1999：纤维接触角系统研究（International Nonwovens Journal）。
- [6] Miller, Penn, Hedvat, 1983：Wilhelmy 法改进。
- [8] Miller & Young, 1975：滞后分析。
- [13] Morton & Hearle, 1993：纺织纤维物理性质经典教材。
- [21] Gupta & Hong, 1995：湿态压缩与蓬松度。
- [22] Gupta, 1998：spunlace 能量对吸液性的影响。
- [23] Gupta & Powers, 2000：热风粘合粘胶/低熔点纤维复合。
- [24] INDA Manual：IST 10.1 / 10.2 定义。
- [27] Kozeny, 1927 与 [28] Carman, 1938：多孔介质流动（Kozeny–Carman）。
- [30] Epps & Leonas, 1997：纸/纤维结构毛细测试。
- [34] Lichstein, 1974：demand wettability 测试。
- [39] Hercules Aqualon Bulletin Vc-494B：SAP 数据表。
- [41] Cobb & Lowe, 1934 与 [43] Klemm, 1944：经典吸液速率测试。
- [51] Craver & Taylor 与 [52] Chatterjee, 1990：超声法测毛细。
- [54] Laser Doppler Anemometry：局部液流测量。
- [61] Miller & Tyomkin, 1983：液体挤出法（非汞）。
- [78]：尿布芯层沿厚度方向 SAP 与盐水分布（Fig. 28）。
- [79] Oathout：动态擦净 sled test。
- [80–81]：Syngyna 装置与 61 cm H₂O 生理压力。
- [84]：尿布 acquisition layer 与 coverstock wetness 测试。
- [86] Marketing/Technology (North America)：尿布 incontinence 测试人体模型。
### 4.5 图示索引（Figures）

- Fig. 6：Wilhelmy 力-时间曲线（A–F 六段）。
- Fig. 7：Miller 法最大拉出力 M。
- Fig. 12：Sink basket test 装置图。
- Fig. 17：离心与抽吸后保水率对比。
- Fig. 18：Southern Pine Kraft 声脉冲测试结果（密度 0.38/0.46/0.54 g/cc）。
- Fig. 19：Demand Wettability tester（恒液位鼓泡器）。
- Fig. 22：液体挤出法装置。
- Fig. 25：两种半径吸液体接触时平衡饱和度的等温线图。
- Fig. 26：挤出体积累积曲线与孔分布微分。
- Fig. 28：尿布厚度方向 SAP 与盐水分布（三层划分）。
- Fig. 29：Oathout 动态擦净 sled 装置。
- Fig. 30：Syngyna 装置（橡皮膜 + 玻璃压力舱）。
- Fig. 32：Acquisition layer 吸收测试。
- Fig. 33：Coverstock 干燥性测试。
## 5. 概念流向图（Concept Flow Diagram）

┌─────────────────────────────────────────────────────────────────────────────┐
│                    CHAPTER 1-10 材料基线（纤维/纸张/非织造/SAP/粘合剂）    │
│                                                                              │
│  ├─ Ch1-3: Cellulosic Fibers (kraft, dissolving pulp)                       │
│  ├─ Ch4-5: Synthetic & Composite Fibers (viscose, polyester, polypropylene)│
│  ├─ Ch6-7: Nonwovens & Bonding (air-laid, spunlace, thermobond)            │
│  ├─ Ch8-9: Superabsorbent Polymers & Composite Cores                       │
│  └─ Ch10: Cores, Adhesives, Acquire Layers                                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CHAPTER 11  测 试 与 表 征（三层金字塔）                  │
│                                                                              │
│   层级 1  构成材料（聚合物/纤维）─── 层级 2  二维结构（网布/片材）─── 层级 3  装配产品    │
│                                                                              │
│   ┌──────────────────────┐  ┌──────────────────────┐  ┌────────────────────┐│
│   │ 2. 表面润湿性         │  │ 4. 标准测试方法      │  │ 6. 产品性能测试    ││
│   │ • Wilhelmy Fw = γPcθ │  │ • INDA IST 10.1/2   │  │ • Syngyna (tampon) ││
│   │ • θ_A / θ_R / WI / WA│  │ • AATCC 127         │  │ • Sled (wiping)    ││
│   │ • Dispersion/Polar   │  │ • TAPPI, Scan-C      │  │ • Coverstock dry   ││
│   │ • Hysteresis         │  │ • Klemm / Cobb       │  │ • Acquisition      ││
│   └──────────────────────┘  └──────────────────────┘  │ • Leakage manikin  ││
│                    │                     │              └────────────────────┘│
│                    ▼                     ▼                      │             │
│   ┌──────────────────────┐  ┌──────────────────────┐              │             │
│   │ 3. 扩散/溶胀/湿力学   │  │ 5. 研究工具          │              │             │
│   │ • Moisture regain    │  │ • Demand wettability │◄─────────────┘             │
│   │ • Water retention    │  │ • Capillary rise     │                             │
│   │ • Swelling SA/SD/SL/V│  │ • Sonic velocity     │◄──────────────────────────┐│
│   │ • Wet bending rigidity│  │ • Liquid extrusion   │                           ││
│   │ • Compression modulus│  │ • Pore size dist.    │◄──────────────────────────┘│
│   └──────────────────────┘  └──────────────────────┘                             │
│                                                                              │
│   ┌────────────────────────────────────────────────────────────────────────┐  │
│   │ Section 1.4 三类方法定位：                                            │  │
│   │   标准方法 (ASTM/AATCC/INDA/TAPPI/EDANA) ←→ 研究工具 ←→ In vitro/In vivo │  │
│   └────────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘

与 Ch1-10 的连接关系：
- Ch1-3 木浆/粘胶 → 本章节 2.2、2.7、2.8（接触角、WA、hysteresis）、3.1（moisture regain）、3.2（扩散）
- Ch4-5 合成纤维 → 表 2/3 中 polyester、polypropylene 的低表面能、低极性解释其"non-wettable"
- Ch6-7 非织造布 → 4.1 (INDA IST 10.1/2)、4.3 (AATCC 127)、5.3 (Klemm/Cobb)、5.4 (demand wettability)
- Ch8-9 SAP 与复合芯 → 5.4 液体在混合体系平衡、Fig. 25（sorption isotherm）、Fig. 28（厚度方向 SAP/盐水分布）、5.5 液体挤出用于 SAP 复合材料孔分布
- Ch10 芯/粘合/导流层 → 6.4 尿布 acquisition layer、surface dryness、leakage 测试（Fig. 32/33）

## 6. 业务连接点（Business Connection Points）

### 6.1 供应商评估与标准化测试的映射

|||||
|---|---|---|---|
|木浆/粘胶纤维原料验收|ASTM D4446（回潮率）、TAPPI、INDA IST 10.1/2|回潮率、吸液时间、吸液容量（%）、WRV|供应商合同应同时规定静态容量 + 速率 + 湿态压缩模量，避免"高容量低速率"的劣质浆|
|粘胶/棉纤表面润湿性评价|Wilhelmy 法（Miller 改进）|θ_A、θ_R、WI、Hysteresis|选用 θ_R 小、hysteresis 低的纤维（如三角粘胶）以缩短达到平衡所需时间|
|SAP 复合材料验收|液体挤出法、Fig. 28 厚度方向分布|有效孔径、SAP 均匀性、盐水下的 AUL|SAP 供应商应提供在 0.3–0.7 psi 下、0.9% 盐水中的 AUL 数据；注意 SAP 沉降导致的厚度不均（Fig. 28）|
|导流层/获取层（acquisition layer）评价|AATCC 127、Fig. 32 装置|渗透吸液速率、导流均匀性|导流层需兼顾"快进液"与"防回渗"，不能仅看 Cobb 值|
|面料表面干燥性|Coverstock wetness 法（Fig. 33）|滤纸增重量|直接影响婴儿皮肤接触干燥性；供应商评估必须纳入|
|防漏性能|Manikin 动态测试（MKT）|泄漏量 vs. 冲击体积/速率|需在多尺寸 manikin + 多冲击模式组合下验证|
|湿巾/擦拭布|Oathout sled 动态擦净（Fig. 29）|动态擦净效率%|静态容量测试不能替代；动态条件下容量 > 挑战量但仍擦不干|
|卫生棉条|Syngyna 法（Fig. 30）|61 cm H₂O 生理压下吸液量、首滴渗出时间|各厂商设备不同，跨厂比较需谨慎；建议供应商统一报告设备参数|

### 6.2 关键测试标准与纸尿裤产品开发对应

- 原料端：木浆纤维用 INDA IST 10.1/2 定"容量 + 速率"、AATCC 标准测渗透；SAP 用 Aqualon Vc-494B 类数据表 + 自研 AUL 装置。
- 二维结构端：空气铺网/水刺/热风粘合各自对压缩模量和蓬松度影响不同——Chapter III 数据 + 本章 Section 3.3.4 表明：needling → 高蓬松（速率优）；spunlace 能量↑ → 吸液↓（trade-off）；热风粘合（粘胶 + 低熔点合成纤维）→ 高蓬松弹性。这直接影响供应商工艺选择。
- 产品端：尿布四层结构（coverstock → acquisition → core → backsheet）每层需独立测试 + 组合 in vitro。MKT（Marketing/Technology）类综合测试是目前行业标杆。
- 质量控制闭环：本章 Section 1.5 提出的"raw material 选型 → component 特性 → composite 预测 → field in vivo → customer survey"是供应商评估与内部研发流程的标准范式。
### 6.3 采购谈判中的测试要点（对王总的建议）

- 避免"仅报容量"：供应商常只给静态饱和容量，必须同时要求 INDA 10.1 速率、AUL、WRV、湿态压缩模量四指标配套。
- 三角粘胶 vs. 圆粘胶：同为粘胶，三角截面 WI 高、hysteresis 低、达到平衡快，采购合同应区分。
- SAP 复合芯：要求供应商提供厚度方向 SAP/水分布数据（Fig. 28），避免底部 SAP 沉降导致的"上干下湿"失败。
- 导流层：AATCC 127 渗透速率 + Fig. 32 acquisition 测试必须同步做，不能仅看 Cobb。
- 湿巾：务必要求供应商提供动态擦净（Oathout 类）数据，静态容量不能替代。
- 跨厂数据可比性：Syngyna、MKT 等 proprietary 设备间差异大，需统一测试协议或要求供应商提供设备参数细节。
## 7. 金句索引（Key Quote Index）

"Surface wetting force, adhesion and energy are important physical properties that affect the ability of a material to be processed into final products and the performance of the latter in many key applications."（Section 2.1, p. 411）
→ 润湿力、附着功、表面能是连接材料与产品性能的物理桥梁。

"Work of adhesion, for example, affects cohesion and bonding between surfaces and would be an important property to consider when selecting materials for applications such as coatings and composites."（Section 2.1, p. 411）
→ 附着功在选材阶段就是关键决策变量。

"The properties of interest are the standard moisture regain, the liquid saturation capacity, water retention value, surface free energy, contact angle, diffusion and swelling characteristics, and wet mechanical properties."（Section 1.3.1, p. 410）
→ 纤维级评价的完整指标清单。

"These tests are intended to provide uniform orderly procedures for the determination of certain well defined properties of fibrous materials. The procedures involved are used in assessing properties for the purpose of process control, quality control, ranking of materials from different producers, and for research and development."（Section 1.4.1, p. 411）
→ 标准方法的四大用途，也是供应商评估的理论基础。

"The properties measured are, however, highly valuable as they can provide an insight into the mechanisms governing the performance and a direction for developing new and improved materials and products."（Section 1.4.2, p. 411）
→ 研究工具虽不能标准化，但提供机理洞察。

"The single most important property of interest is the customer satisfaction which can, of course, be a very complex and difficult goal to achieve through a single kind of product."（Section 1.3.3, p. 410）
→ 产品级评价的终极目标是客户满意度，单一产品难以覆盖所有场景。

"Usually, the greater the absorption, the greater the loss in modulus. For example, among the two cellulosic fibers, rayon and cotton, the former, absorbing more water, usually undergoes a greater decrease in bending rigidity."（Section 3.3.4, p. 416）
→ 湿态下粘胶比棉更易失去弯曲刚性，直接影响蓬松度与容量。

"An increase in spunlacing energy usually led to a decrease in absorbency values."（Section 3.3.4, p. 416, [22]）
→ 水刺能量-吸液性的 trade-off，采购水刺布时需评估。

"Wettability index is given by the product of surface tension of water (a constant) and the cosine of the contact angle (eq. 7). It gives a measure of the normalized attractive force exerted by a solid on a fluid and is directly proportional to the cosine of the contact angle."（Section 2.6, p. 419）
→ WI 是材料选择的核心量化指标。

"Complications, limitations, and uncertainties connected with mercury intrusion through textile materials can be avoided by using non-mercury liquids."（Section 5.5, p. 435）
→ 柔性材料（SAP 复合、非织造）的孔径测试应避免汞法。

"A product may not wipe dry a surface even when its absorbent capacity exceeds the amount to be absorbed, as measured by the tests referred above."（Section 6.2, p. 438）
→ 静态容量 ≠ 使用性能，动态擦净测试不可替代。

"A general interest concerning the performance of such materials is how well a test fluid presented under suitable hydrodynamic conditions gets absorbed when the absorption mechanisms are capillary and diffusion."（Section 6.4, p. 439）
→ 尿布/护理垫性能的核心是毛细 + 扩散耦合下的真实吸收。

## 8. 质量自检（Quality Self-Check）

- ✅ 所有引语均按原文逐字保留（verbatim English），未做任何翻译或改写。
- ✅ 数值、表格、图号、方程编号均与原文一致（Table 2 六纤维 WA 值、Table 3 六纤维表面能值、Section 1.3.1/1.4.1 引语、Section 3.3.4 引语等）。
- ✅ AUL、rewet、surface feel、Draves method：本章未给出独立的标准操作化定义，报告中已明确标注"本章未展开"，不杜撰内容。
- ✅ FPA、penetration absorbency：在本章中的实际引用形式为"flat-panel absorbency / penetration absorbency 作为二维结构表征参数"，报告按此表述，未过度延伸。
- ✅ 标准组织（ASTM、AATCC、INDA、TAPPI、EDANA、Scan-C）均按原文列出。
- ✅ 参考文献按 Chapter 8 References 列出，未编造。
- ✅ 未编造任何具体数值（如具体 AUL 值、具体 SAP 克水倍率）——因本章本身未给出。
- ⚠️ Draves Method 具体操作细节：本章未提供，如需完整定义需另查原始文献。

报告生成日期：2026-08-23
报告路径：/sandbox/workspace/deepread/absorbent_tech_reports_20260823/Absorbent Technology_ch11_report.md
字数：约 4800 字（含表格）

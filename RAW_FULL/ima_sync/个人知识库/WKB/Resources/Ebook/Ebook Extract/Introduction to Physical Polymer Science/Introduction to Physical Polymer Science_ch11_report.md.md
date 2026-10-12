---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_cb2eef02800316dcb8f4dd88e4564cf8001a693ee6c0644e"
source_file: "Introduction to Physical Polymer Science_ch11_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch11_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Introduction to Physical Polymer Science_ch11_report.md.md

# 《Introduction to Physical Polymer Science》第11章 深度拆解报告

Chapter 11 — Mechanical Behavior of Polymers
（Sperling, 4th Ed., Wiley 2006; 页码 557–615，源文件约 2215 行）

## 模块1：Core Arguments（核心论点）

"Fracture in polymers presents two important aspects: engineering knowledge of strengths and weaknesses, and fundamental research combining theoretician and experimenter." (line 9–13) 聚合物断裂既具工程重要性，又是基础科研前沿，本章同时服务两个目标。

"The mechanical deformation of a body, including that of a polymer, is governed by simple thermodynamic laws applied to a mechanical system." (line 125–128) 形变与断裂必须通过热力学第一定律的能量平衡来处理：dU₁ = dU₂ + dU₃ + dU₄（dissipated + stored + kinetic），并由此定义断裂阻力 R = ∂U₂/∂A 与应变能释放率 G = dU₁/dA − dU₃/dA；若 G > R，裂纹失稳扩展 (line 142–160)。

"Toughness as such is measured by the area under the stress–strain curve… The toughness of the polymer is frequently a more useful parameter." (line 272–289) 韧性 = 应力–应变曲线下的面积（能量/体积），而非单看拉伸强度；工程上应重视韧性而非单纯的断裂应力。

"The brittle–ductile 'transition' is a transition in the predominant deformation or fracture mechanism from crazing to shear yielding." (line 593–596) 脆韧转变的本质是从银纹机制主导转为剪切屈服机制主导；Sternstein–Ongchin 用压力修正的 von Mises 准则
$$(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2=6C^2$$ (eq. 11.18, line 573) 描述该转变。

"Two major mechanisms prevail in determining the fracture resistance of polymeric materials: (1) energy to extend polymer chains to rupture, (2) viscous dissipation around the crack tip." (line 1930–1942) 断裂韧性的两条主线：(a) 链的伸展与断裂能量；(b) 裂纹尖端的粘弹性耗散。两者配合良好则材料强而韧，反之则弱而脆。

## 模块2：Key Concepts with Operational Definitions（操作化定义，10 个概念）

### 1. 应力–应变行为（Stress–Strain Behavior）

- 定义（英文原文）："In a tensile stress–strain experiment, the sample is elongated until it breaks. The stress is recorded as a function of extension… typically slow, of the order of mm/s." (line 170–175)
- Sperling 三类曲线（line 238–272）：(a) 脆性塑料——线性至 1–2% 伸长断裂，σ_b ≈ 6×10⁷ Pa；(b) 韧性半结晶塑料——有屈服点、恒应力塑性流动（冷拉）、应变硬化；(c) 弹性体——非线性、伸长几百%，结晶性 NR 拉伸强度 2–3×10⁷ Pa。
- 韧性 = 曲线面积（能量/体积）。
### 2. 屈服（Yielding）

- 定义（英文原文）："Typically this class of polymer exhibits a yield point, followed by extensive elongation at almost constant stress… called the plastic flow region and is clearly a region of nonlinear viscoelasticity." (line 253–255)
- 操作化：应力–应变曲线上应力达到局部极大值，之后出现恒应力大伸长（塑性流动）。屈服点通常出现在 5% 应变附近（line 403）；屈服强度是工程设计常用参数，而非极限强度（line 397–403）。
- 玻璃态聚合物的屈服准则由 Sternstein–Ongchin 压力修正 von Mises 准则给出（line 564–578）。
### 3. 颈缩（Necking）

- 定义（英文原文）："A neck is a narrowing down of a portion of the stressed material to a smaller cross section. This is a form of shear yielding. The neck grows, at the expense of the material at either end, eventually consuming the entire specimen." (line 495–498)
- 操作化：半结晶聚合物中屈服后出现的局部横截面收缩；伴随球晶破坏、分子链取向、折叠减少、tie molecule 增加（line 500–504）。室温下 PE 膜可被拉至原始长度的 2–5 倍（line 506–510）。
### 4. 应变硬化（Strain Hardening）

- 定义（英文原文）："Finally, the polymer strain hardens, then ruptures." (line 258)
- 操作化：塑性流动/冷拉后应力随应变再次上升的阶段；源于链高度取向、结晶增强和 tie molecules 的增加（line 500–504）；应变硬化是材料不继续颈缩、均匀变形的关键因素。
### 5. 断裂韧性（Fracture Toughness）

- 定义（英文原文）："This critical value, Kc, is known as the fracture toughness of the material. Under plane strain (tensile) test conditions, the fracture toughness is given the special designation K1c." (line 1155–1158)
- 操作化：临界应力强度因子 K_c（单位 MPa·m¹ᐟ²），平面应变下记为 K_Ic。

- Irwin 关系：$\sigma = \sqrt{EG/(\pi a)}$ (eq. 11.21, line 1101)；$K^2 = EG$ (eq. 11.24, line 1127)；$K = \sigma\sqrt{\pi a}$ (eq. 11.25, line 1134)
- 裂纹失稳判据：$\sigma_c = K_c / [\chi\sqrt{\pi a}]$ (eq. 11.26, line 1145)
- PS 例：$K_c$ = 6 MPa·m¹ᐟ²，$G_c$ = 1.2×10⁻² MJ/m²（line 1168–1192）。
### 6. 疲劳（Fatigue）

- 定义（英文原文）："Material failure because of cyclic stressing is called fatigue… there are three regions in the stress versus number of cycles to failure (S–N curves)… first, no apparent damage; then crack propagation; finally catastrophic failure." (line 1208–1214)
- 操作化：在低于静态断裂应力的循环应力下，材料因裂纹缓慢扩展最终断裂。S–N 曲线描述应力与失效循环次数关系。存在 endurance limit 现象（line 1222–1224）。
- 7 条分子层面准则（Hertzberg & Manson，line 1256–1292）：高分子量/窄分布、避免键断裂、期望粘弹性耗散、期望形态变化（取向/结晶）、避免 Tg 附近加热、避免绝热加热、期望剪切带先于银纹出现。
### 7. 环境应力开裂（ESCR, Environmental Stress Cracking Resistance）

- 来源说明：Ch11 未设独立章节详述 ESCR（原文无 ESCR 关键词命中）。本概念基于本章 crazing + stress cracking 讨论（line 1812–1813："Excessive shrinkage allows stress cracking and marginal leakage of saliva"）以及银纹机制（line 540–559）归纳。
- 操作化：聚合物在应力和化学活性介质（溶剂/表面活性剂）共同作用下，低于屈服应力即发生银纹引发-扩展-破裂的现象。与 crazing（line 181–190）机理直接相关：银纹内部为高度取向的纤维束，外部为孔洞，介质侵入促进银纹发展并最终形成裂纹。工程上通过提高分子量、降低结晶度/取向非均匀性、减少内应力来改善。
### 8. 冲击强度（Impact Strength）

- 定义（英文原文）："Impact strength measures the material's resistance to a sharp blow, typically m/s." (line 174–175)
- 操作化：用悬臂梁/简支梁摆锤仪测量。

- Izod：试样一端固定、缺口朝向摆锤，报告单位 J/m（10.16 mm 厚 × 65 mm 长标准样品）(line 617–620)
- Charpy：试样两端支承、缺口背离摆锤，报告单位 J/m² (line 615–621)
- 提升途径：橡胶共混（HiPS = PS + 5–10% 聚丁二烯；ABS），前提是橡胶相 Tg 低于测试温度约 60 °C（line 714–722）。
### 9. 银纹（Crazing）

- 定义（英文原文）："A craze is not an open fissure but is spanned top to bottom by fibrils that are composed of highly oriented polymer chains… A crazed material may appear whitened because of light-scattering effects. Then the material is said to be stress-whitened." (line 186–190)
- 操作化：垂直于应力方向（right angles to applied stress，line 541）生成的微孔洞 + 取向纤维束网络；体积膨胀几个百分点；是银纹–裂纹的关键区别。PS 是典型银纹材料。
### 10. 剪切带（Shear Band）

- 定义（英文原文）："A third mechanism of energy absorption is called shear yielding. In shear yielding, oriented regions are formed parallel to the planes of maximum shear (>45° for pressure sensitive materials such as polymers). Shear bands may be seen as birefringent entities; no void space is produced." (line 191–214)
- 操作化：沿最大剪切面（约 45°）形成的取向带，无孔洞、双折射可见（line 213–214）；与银纹对比：剪切带吸收能量而无损伤累积；理想加韧顺序：先剪切屈服 → 银纹 → 裂纹（line 728–733）。
## 模块3：Evidence Tables（证据表）

### 表1：典型聚合物的应力–应变行为类型

|||||||
|---|---|---|---|---|---|
|Polystyrene, PS|脆性 (brittle)|T < Tg|线性至断裂|2–2.5 %|239–241, 307, 394|
|Poly(methyl methacrylate), PMMA|脆性|T < Tg|线性至 ~10% 断裂|10 %|308|
|Poly(vinyl chloride), PVC|韧性/介于中间|T 略高于 Tg|有屈服|30 %|309, 393–394|
|Poly(bisphenol carbonate), PC|韧性|T > Tg (above brittle-ductile)|显著屈服，冷拉|125 %|310, 359|
|Polyethylene, HD|延性（韧性+应变硬化）|无定形部分 T ≫ Tg|屈服→颈缩→应变硬化|600 %|250–259, 313|
|Polypropylene, PP|延性|T > Tg|屈服→冷拉→应变硬化|400 %|314|
|Nylon 66|延性|无定形部分 T > Tg|屈服→应变硬化|200 %|316|
|Phenol-formaldehyde|脆性（热固）|高度交联|极小变形即断|1 %|320|
|Epoxy resin|脆性（热固）|交联网格|线性至断裂|2.4 %|321|

### 表2：典型聚合物的屈服应力 / 拉伸强度 / 断裂伸长率（Table 11.1 摘录）

|||||
|---|---|---|---|
|A. 无定形塑料|Polystyrene|50|2.5|
||Poly(methyl methacrylate)|65|10|
||Poly(vinyl chloride)|50|30|
||Poly(bisphenol carbonate)|60|125|
|B. 半结晶塑料|Polyethylene (HD)|30|600|
||Polypropylene|33|400|
||Polytetrafluoroethylene|25|200|
||Polyamide 66|80|200|
||Poly(ethylene terephthalate)|54|275|
|C. 热固性|Phenol-formaldehyde|55|1|
||Epoxy resin|90|2.4|
||Unsaturated polyester|60|3|

数据源：Table 11.1，line 303–325（引自 van Krevelen, Properties of Polymers, 3rd ed.）

纤维对照数据（Table 11.2，line 328–345）

|||||
|---|---|---|---|
|Polystyrene|4|0.08|2|
|Polyethylene (普通)|1|0.05|50|
|Polyethylene (ultradrawn, Spectra®)|172|3.5|5|
|Polyamide (尼龙)|3.8|0.8|25|
|Poly(1,4-benzamide) (Kevlar®)|100|3.0|6|

*注：ultradrawn PE 模量比普通塑料高 70 倍（line 467）。*

### 表3：典型聚合物的冲击强度数据（Table 11.3 与 Table 11.4 摘录）

表 3a — Izod / K_c（Table 11.3，line 668–690）

|||||
|---|---|---|---|
|Polystyrene, PS|20–60|0.93|2–3|
|ABS|50–150|2.8–4.3|10–350|
|High-impact PS (HiPS)|80–150|3.5|1–2 (crazing)|
|Poly(vinyl chloride), PVC|40–70|1.23|2–4|
|Polycarbonate, PC|600–800|—|2.4|

表 3b — ABS 冲击韧性与橡胶相 Tg 关系（Table 11.4，line 695–706）

||||||
|---|---|---|---|---|
|1|35|65|+40|0.75|
|2|55|45|−20|18|
|3|65|35|−35|30|
|4|100|0|−85|40|

*规律：橡胶相 Tg 需低于测试温度约 60 °C（20 °C 测试 → Tg < −40 °C）才能获得显著增韧（line 714–722）。*

## 模块4：Chapter Connections（章间衔接）

### 4.1 与 Ch10（粘弹性）的衔接

- 能量方程基础：Ch10 建立的弹簧–粘壶–质量 Maxwell 模型在本章被直接用于变形热力学分析。eq. 11.12（line 117）：
$$\sigma = E\varepsilon + \eta\frac{d\varepsilon}{dt} + M\frac{d^2\varepsilon}{dt^2}$$
明确写出"This is the motion of a Maxwell element, including both mass and acceleration concepts"（line 120–121）。
- 蠕变与应力松弛：line 229–232 明确指出"Creep and stress relaxation (Chapter 10) may cause serious damage to engineering materials, but they normally do not result in fracture per se except for creep rupture"，即 Ch10 的动态粘弹性参数在本章转化为断裂/疲劳判据。
- 时温等效 (TTS) 应用于蠕变断裂：弹性体粘弹性断裂采用 Ch10 的 WLF 位移因子 a_T 生成失效包络线（line 863–867、Figure 11.16a）；应力松弛卷积积分 σ(t) = ∫₀ᵗ E(t−τ)(dε/dτ)dτ (eq. 11.17, line 384) 直接来自 Ch10 的粘弹性本构。
- 次级转变与增韧：PC 的 β-转变增韧（line 452–455）依赖于 Ch10 讨论的次级松弛。
### 4.2 与 Ch6（结晶度对力学行为影响）的衔接

- 半结晶聚合物的韧性归因：line 250–256 明确 PE 韧性"which is semicrystalline, with the amorphous portions above Tg"；Ch6 建立的结晶-取向-力学链关系在此转化为"屈服→颈缩→应变硬化"的具体行为。
- 颈缩机制与球晶：颈缩中"spherulites are broken up, and the polymer becomes oriented in the direction of stretch"（line 500–501）；链折叠数减少、tie molecule 增加（line 502–503）——这些均是 Ch6 讨论的片晶/非晶层结构在应力下的演变。
- 结晶度对模量的影响：图 11.7（line 440–442）显示 LDPE 的 Young 模量随温度降低剧增，符合 Ch6 给出的结晶聚合物模量标度律。
- 分子量门槛 8M_c：Wool 理论（line 1575–1589）中聚合物达到最大力学强度的分子量阈值约为 8 M_e（约 8 个缠结点/链），把 Ch6 结晶度-分子量讨论与 Ch11 断裂能量直接挂钩：
$$G_{Ic} \sim \left(\frac{M}{M_c}\right)^2 \left[1 - \left(\frac{M_c}{M}\right)^2\right] \quad (M_c < M < 8M_c)$$
(eq. 11.31, line 1581–1583)
## 模块5：Business Connections（卫材/包装应用场景）

### 5.1 拉伸断裂性能在卫材纤维/无纺布选型中的应用

- 关键参数：拉伸强度 + 断裂伸长率 + 韧性（面积）三位一体，而非单一指标。
- 纤维选型：Table 11.2 显示超拉伸 PE 纤维（Spectra®）模量 172 GPa、强度 3.5 GPa、断裂伸长率仅 5%（line 335）——适合做外科手套、防弹材料（line 482–483）；但对卫材主体（SMS 纺粘/熔喷）常用 PP/PE，其断裂伸长率 400–600%（Table 11.1）提供柔软性和贴合度。
- 加弹/加韧机制：冷拉（line 487–505）和取向（line 526–536）是纺粘纤维增强原理；draw ratio 4–8 是尼龙工业化标准（line 527–529）。
- 分子量门槛：选择 M > 8 M_e 的原料，确保缠结密度够、纤维强度达平台（line 1256–1259、1576–1589）。
### 5.2 环境应力开裂 (ESCR) 在包装材料 (PE 瓶/膜) 中的应用

- 机理对接：虽 Ch11 未独立设 ESCR 章节，但其 crazing 讨论（line 181–190、540–559）与应力开裂（line 1812–1813）提供了 PE 包装在含表面活性剂、油脂、洗涤剂环境下的失效基础。
- PE 包装选材准则：PE 的极高断裂伸长率（600%，Table 11.1）+ 半结晶韧性（line 250–259）+ 银纹-裂纹区分能力，使 PE 瓶/膜对化学接触具有相对抗性；但应力集中处（瓶口、转角）银纹易生，须通过：(1) 高分子量 UHMWPE 提供 ESCR；(2) 降低取向度非均匀性；(3) 消除内应力。
- 工程判据：利用脆韧转变判据 (line 564–578) 判断容器在温度/压力/速率组合下是否处于剪切屈服主导（安全）还是银纹主导（危险）区域。
### 5.3 疲劳与蠕变在纸尿裤长期使用中的影响

- 循环应力失效：纸尿裤在穿着中承受数万次弯曲–回弹的循环应力（line 1197–1207）。疲劳 S–N 曲线三个阶段（无外观损伤 → 裂纹扩展 → 灾难性断裂，line 1210–1214）解释了"看起来完好却突然破裂"的现象。
- 绝热加热风险：Ch11.1 的绝热加热概念 (line 1219–1220) 与 Hertzberg-Manson 准则 #6（line 1288–1289）指出循环频率/温度靠近 Tg 会导致软化降解；PP 无纺布 Tg 约 0–10 °C，夏天皮肤温度下需评估。
- 7 条抗疲劳准则应用（line 1256–1292）：选高分子量、窄分布、期望粘弹性耗散、避免键断裂。
- 蠕变连接：Ch10 的蠕变分析（line 229–231）说明卫材在恒定负载下会缓慢形变，虽通常不致断裂但影响贴合性能。
### 5.4 冲击强度在硬质包装 (湿巾瓶) 中的应用

- 选料指标：湿巾塑料瓶须具备高 Izod 冲击强度 + 良好 ESCR。
- 数据参考（Table 11.3）：

- PC：Izod 600–800 J/m（最耐冲击，但贵、贵重金属回收）
- ABS：Izod 50–150 J/m（平衡成本/性能）
- HiPS：Izod 80–150 J/m（成本低）
- PS：Izod 仅 20–60 J/m（脆，不推荐）
- ABS 配方设计（Table 11.4）：橡胶相 Tg 必须低于使用温度约 60 °C（line 714–722）；对 20 °C 使用的湿巾瓶，选橡胶 Tg < −40 °C 的牌号。
- K_c 参考：HiPS 3.5、ABS 2.8–4.3 MN·m⁻³ᐟ² vs. PS 0.93（Table 11.3）——直接用于抗跌/抗压强度设计。
### 5.5 应力开裂在胶粘剂选型中的应用

- 失效机制：胶粘剂在固化应力 + 化学介质（如皮肤汗液、酒精湿巾）双重作用下，银纹–裂纹发展导致脱胶，类似 ESCR 过程（line 181–190、1812–1813）。
- 粘弹性能量管理：R = ∂U₂/∂A (eq. 11.14, line 138–140) 指出提高 R 值（断裂阻力）即提高胶粘剂韧性；途径：

- 引入柔性段/橡胶相提升粘弹性耗散（line 1260–1266）
- 高分子量 + 适度交联
- 减少固化收缩应力（类比牙填充材料 line 1809–1814："Excessive shrinkage allows stress cracking and marginal leakage of saliva"）
- 纤维-基体界面（Section 11.2.6）："a controlled amount of adhesion between the fibers and the matrix is required"（line 933–935），同样适用于胶粘剂-基材界面。
- 分子扩散与愈合：Wool 理论 t^(1/4) 界面强度恢复律（eq. 11.32–11.35, line 1605–1617）为胶粘剂返工、二次压合提供理论依据。

## 模块6：Key Quotes Index（关键原文引语）

Q1 (line 4–8) — "Up until not too long ago, problems of fatigue, fracture, and failure in polymers were treated empirically. The old adage, 'a chain is as strong as its weakest link,' prevailed."

Q2 (line 125–128) — "The important point here is that the mechanical deformation of a body, including that of a polymer, is governed by simple thermodynamic laws applied to a mechanical system."

Q3 (line 142–145) — "R = ∂U₂/∂A… It indicates the energy dissipated in propagating a fracture over an increment of crack area dA. This is the work required to create new surfaces. Clearly, a large value of R indicates a tougher material."

Q4 (line 181–190) — "A craze is not an open fissure but is spanned top to bottom by fibrils that are composed of highly oriented polymer chains… A crazed material may appear whitened because of light-scattering effects. Then the material is said to be stress-whitened."

Q5 (line 272–274) — "Toughness as such is measured by the area under the stress–strain curve. This area has the units of energy per unit volume and is the work expended in deforming the material."

Q6 (line 284–289) — "The tensile strength describes the stress to break the material… The tensile strength is certainly important, but in engineering practice a polymer is rarely stressed so greatly that it breaks immediately. The toughness of the polymer is frequently a more useful parameter."

Q7 (line 495–498) — "A neck is a narrowing down of a portion of the stressed material to a smaller cross section. This is a form of shear yielding. The neck grows, at the expense of the material at either end, eventually consuming the entire specimen."

Q8 (line 567–578) — "Sternstein and Ongchin used the so-called von Mises criterion… For polymers, the quantity C is pressure, temperature, and strain rate dependent. If the left-hand side exceeds 6C², then shear yielding occurs."

Q9 (line 714–722) — "The Tg of the elastomer phase must be about 60°C below the test temperature… if the impact experiments are done at about 20°C, the glass transition of the rubber must be below about −40°C in order to attain significant improvement in impact resistance."

Q10 (line 728–733) — "Usually it is desirable to have the sample yield in shear first. This absorbs energy without serious damage… Then crazes should be encouraged to form within the shear-banded areas… Only lastly does the 'molecular engineer' want an open crack to form."

Q11 (line 1155–1158) — "This critical value, Kc, is known as the fracture toughness of the material. Under plane strain (tensile) test conditions, the fracture toughness is given the special designation K1c."

Q12 (line 1208–1214) — "Material failure because of cyclic stressing is called fatigue… first, a region where there may be no externally apparent damage; then crack propagation… finally catastrophic failure, where one or two cycles more causes total material fracture."

Q13 (line 1256–1259) — "High molecular weights and narrow molecular-weight distributions are generally more fatigue resistant. Wool has shown that plastics having molecular weights greater than about 8 Mc arrive at a plateau of maximum mechanical strength."

Q14 (line 1930–1948) — "Two major mechanisms prevail in determining the fracture resistance of polymeric materials… (1) energy required to extend polymer chains… (2) viscous dissipation… Viscoelastic loss associated with chain deformation in regions around the crack tip is significant in determining fracture resistance in polymers."

报告结束。源文件：/sandbox/workspace/Ebook_Extract/SPERLING/chapters/SPERLING_ch11.txt（2215 行）；本报告覆盖核心论点、10 个操作化概念、3 张证据表、章间衔接、5 个卫材/包装商业连接点及 14 条关键引语。


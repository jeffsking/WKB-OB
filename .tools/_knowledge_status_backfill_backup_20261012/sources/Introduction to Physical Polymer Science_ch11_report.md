---
type: source
title: "Introduction to Physical Polymer Science_ch11_report.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch11_report.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
key_claims: []
pages_linked: []
compile_mode: extractive
---

# Introduction to Physical Polymer Science_ch11_report.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch11_report.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

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
|Poly(vinyl ch

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch11_report.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Introduction to Physical Polymer Science/Introduction to Physical Polymer Science_ch11_report.md.md`
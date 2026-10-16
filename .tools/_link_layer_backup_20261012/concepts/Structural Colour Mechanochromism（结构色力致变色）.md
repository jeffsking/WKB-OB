---
type: concept
title: "Structural Colour Mechanochromism（结构色力致变色）"
domain: [卫材研发, 变色与智能材料]
status: growing
updated: 2026-09-29
tags: [Mechanochromic, 结构色, 光子晶体, 液晶弹性体, HPC, 角度依赖]
---

# Structural Colour Mechanochromism（结构色力致变色）

> One-line definition 一句话定义：Strain-triggered colour produced by a change in **periodic dielectric structure** (lattice spacing, helical pitch or multilayer optical path) rather than by a chromophore — the most vivid published strain response, and today un-makeable on a hot-melt line.
> （中文：由**周期性介电结构**（晶格间距、螺距或多层光程）变化而非发色团产生的应变触发颜色——是文献中色彩最鲜艳的应变响应，但当前无法在热熔产线上制备。）

## Mechanism / Structure 机理 / 结构拆解

1. **Photonic crystals / polymer opals（光子晶体 / 聚合物蛋白石）**：core-shell PS/PEA particles ~200–300 nm shear-assemble into elastomeric opals with intense tunable colour; silica-in-rubber photonic fibres on spandex shift red → blue across 127 nm and survive 100+ stretch cycles; roll-to-roll is real (>100 m opal film produced by bending-induced oscillatory shear). **But ordering needs oscillatory shear at ~300 % strain amplitude between heated rollers — a dedicated line, not a slot die.**
2. **Cholesteric liquid-crystal elastomers（胆甾相液晶弹性体）**：helical pitch compresses under strain, blue-shifting the reflection band; 2025 work adds photo-switchable chiral dopants for imprinted patterns. Uniaxial red → blue typically needs > 100 % strain and colour intensity drops as it shifts; films need planar alignment and UV cure under nitrogen — two unit operations a hot-melt station does not have; reactive mesogen toxicology for an infant product is unresolved.
3. **Stretchable DBR（可拉伸分布式布拉格反射镜）**：multilayer Bragg stack with an NIR → visible band shift, but only over 0–50 % strain and as a co-extruded film.
4. **HPC structural colour（HPC 结构色）**：hydroxypropyl cellulose changes viscoelastic lattice spacing, giving a compressive blue-shift (red → blue) with a **predictable power-law strain–colour relation** — the most attractive candidate on paper.
5. **Two failure modes they share（两条共同的失效模式）**：
   - **Moisture and UV（湿与紫外）**：mechanochromic hydrogels take up moisture that changes both mechanical and optical behaviour; UV photodegrades chromogenic units. A diaper panel sees urine vapour, sweat and daylight.
   - **Angle dependence（角度依赖）**：Bragg colour travels with viewing angle — a parent tilting the pant would see a colour change that is not a strain change, **the worst possible failure for a fit meter**.
6. **Worth stealing（值得借鉴）**：non-iridescent "amorphous photonic" variants remove angle dependence, and silica-in-rubber costs are falling — review at the 2028 platform gate.
7. **The HPC strain ceiling（HPC 的应变上限）**：Barty-King et al. 2025 — below 25 % strain HPC stays in a stable viscoelastic pitch-compression regime; beyond 25–27 % it transitions into a flowing/sheared state and sensor integrity collapses.
8. **The honest limit（诚实边界）**：above threshold, shear-thinning + inelastic lateral flow can *relax* the colour away even while stress persists — a **false-negative safety reading, worse than no indicator at all**. Hence signal-stability validation is the pilot's life-or-death gate.

（中文：①光子晶体/聚合物蛋白石——200–300 nm 核壳 PS/PEA 颗粒经剪切组装成弹性蛋白石，硅-橡胶光子纤维在氨纶上红→蓝位移 127 nm 且耐受 100+ 次拉伸；卷对卷已可实现（>100 m）；**但有序化需要加热辊间约 300% 应变幅的振荡剪切——是专用产线，不是狭缝模头**。②胆甾相液晶弹性体——螺距受压蓝移；2025 年工作引入光开关手性掺杂剂做压印图案；单轴红→蓝通常需 >100% 应变且强度随位移下降；成膜需平面取向与氮气下 UV 固化（热熔工位没有的两道单元操作）；活性介晶对婴儿产品的毒理未解决。③可拉伸 DBR——多层布拉格堆栈，NIR→可见，但仅在 0–50% 应变且为共挤膜。④HPC 结构色——羟丙基纤维素改变黏弹晶格间距，压缩蓝移（红→蓝），具**可预测的幂律应变—色关系**，纸面上最有吸引力。⑤两条共同失效模式——湿与紫外（水凝胶吸水同时改变力学与光学行为、UV 光降解显色单元；纸尿裤面层同时暴露于尿汽、汗液与日光）、角度依赖（布拉格色随视角变化，家长一倾斜就会看到并非应变引起的变色，是合身仪表最糟的失效）。⑥值得借鉴——非虹彩「非晶光子」变体可消除角度依赖，硅-橡胶成本在下降，建议在 2028 平台门径复审。⑦HPC 应变上限——25% 以下保持稳定黏弹螺距压缩态，超过 25–27% 进入流动/剪切态，传感完整性崩塌。⑧诚实边界——超阈值后剪切变薄与无弹性侧向流动会在应力仍存在时把颜色「松弛掉」，构成**假阴性安全读数，比没有指示器更糟**，故信号稳定性验证是试产生死门。）

## Key Parameters 关键参数表

| Parameter 参数 | Value / range 数值/范围 | Source 出处 |
|---|---|---|
| Polymer opal shift demonstrated | 127 nm（red → blue） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Opal core-shell particle size | ~200–300 nm（PS/PEA） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Opal ordering requirement | oscillatory shear at ~300 % strain amplitude between heated rollers | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Opal cycle life | > 100 stretch cycles | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Opal usable strain（screening matrix） | 0–60 % | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Opal cost index / TRL | 25× / TRL 3 | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Cholesteric LCE full sweep | > 100 % strain; colour intensity drops as it shifts | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Cholesteric LCE cost index / TRL | 40× / TRL 2–3 | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Stretchable DBR usable strain | 0–50 %；cost index 15×；TRL 3 | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| HPC stable regime | below 25 % strain（viscoelastic pitch compression） | [[Mechanochromic Materials Technical Review（EN v3, 2026-08）]] |
| HPC collapse regime | beyond 25–27 % strain → flowing/sheared state, integrity collapses（Barty-King et al. 2025） | [[Mechanochromic Materials Technical Review（EN v3, 2026-08）]] |
| Interference pigment usable strain | 30–200 %；cost index 3×；TRL 4（BACKUP） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Craze / cavitation whitening | 40–120 %；thermal reset；cost index 1.4×；TRL 5（PHASE 2） | [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] |
| Backsheet optics required（BM lane, for contrast） | film 30–80 % light transmittance；outer nonwoven ≥ 50 % | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |

> ⚠️ **No unsourced parameters**：以上均来自本批源摘要页。HPC 的**循环寿命数据**与**在尿汽/汗液环境下的耐久数据**库内缺失 → `[待验证]`。

## Adjacent Concepts 相邻概念

- 替代路线：[[Geometric Optical Mask（几何光学掩膜）]]、[[Mechanophore Mechanochromism（机械力致变色分子）]]
- 分类学：[[Chromism Taxonomy（变色现象分类）]]
- 既有页对照：[[Mechanochromic变色纤维]]（可机洗液晶弹性体变色纤维）、[[变色油墨]]、[[三叶形截面纤维（Trilobal Fibre）]]
- 选型：[[Mechanochromic Routes Comparison（力致变色技术路线对比）]]

## Lessons 经验教训

> ✅ Verification（2026-09-29，来源 [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]]、[[Mechanochromic Materials Technical Review（EN v3, 2026-08）]]、[[Chromic Materials Bibliography（变色材料书籍·温湿力精表）]]）：三份来源在「结构色可逆性最好、但当前工艺不可及」上结论一致；书目把可穿戴光子学类书籍（Tao《Wearable Electronics and Photonics》等）归入力致变色书架，与本页「器件问题」一支对应。本页结论与来源一致。

- **教训一（失效模式优先）**：对合身仪表而言，**角度依赖是致命失效**——家长一倾斜纸尿裤就会看到并非应变引起的颜色变化。选结构色路线前必须先解决非虹彩化。
- **教训二（假阴性比缺失更糟）**：超阈值后颜色会「松弛掉」，护理者会看到「安全」色而纸尿裤仍过紧。这是结构色路线的**生死门**，不是可优化项。
- **教训三（工艺原生性）**：蛋白石需要加热辊间振荡剪切，胆甾相需要平面取向 + 氮气 UV 固化——这两道单元操作在热熔工位**不存在**，属架构级不兼容，而非配方问题。
- **教训四（保留观察窗口）**：「非晶光子」非虹彩变体 + 硅-橡胶成本下降值得在 **2028 平台门径**复审。

## 追加：Open Innovation 批（2026-09-29 追加 · 25–27% 应变区间与阈值下移）

> 追加来源 `[[Strategic Roadmap - Commercializing Mechanochromic Materials（力致变色商业化战略路线图·X-Chromic 版）]]`。本段**只补"超阈值失效的定量边界与流变对策"，不改动上文任何机理、参数与经验教训结论**。

### 1. ✅ 与上文「教训二」同向——本批给出的是定量边界

| 项 | 上文（既有） | 本批追加 |
|---|---|---|
| 失效现象 | 超阈值后颜色**「松弛掉」**，护理者看到"安全"色而产品仍过紧 | 同一现象，源文表述为 **colour change may "relax" or dissipate even while the stress is still being applied** |
| 失效后果 | **假阴性比缺失更糟** | 源文明确写为 **false-negative safety readings（假阴性安全读数）** |
| **阈值** | 上文未给数值 | **25–27% 应变**（Barty-King et al., 2025） |
| **机理分界** | 上文归为结构色路线的"生死门" | **低于 25–27%**：HPC 处于稳定的粘弹 **pitch compression（螺距压缩）**区间；**超过**：进入 **flowing / sheared（流动/剪切）**状态 |
| **对策** | 上文未给 | 优先用**胶凝剂（gelling agents，如 gelatin 明胶）**调流变，抵抗**剪切变稀与非弹性侧向流动** |

> ⚠️ **验证状态**：25–27% 这一具体数值来自源文引用的 **Barty-King et al., 2025**，**本库未核实原始文献**，记为 `[待验证]`。**上文"教训二"的结论未被修正，本批只是给了数值与对策。**

### 2. HPC 路线的可逆性论据（本批新增表述）

- 源文称 **HPC 提供应变与颜色之间的 power-law relationship（幂律关系）**，因此照护者可在**调整腰围后看到颜色回到安全基线**——这是把上文"结构色可逆性最好"落到**连续合身监测**场景的论证。
- **可逆性在本场景是硬要求**：源文原话 **"reversibility is a non-negotiable requirement"**。
- ⚠️ 源文同时区分：**螺吡喃（Spiropyrans）的热致瞬态** vs **萘并吡喃（Naphthopyrans）的合成模块化**——后者被认为更适合定制激活阈值。**这是分子型力色团的取舍，与结构色路线并列，不互推。**

### 3. 阈值下移缺口（跨路线共性）

| 项 | 值 |
|---|---|
| 工业级力色团阈值 | **≥40,000 PSI**（为检测高性能聚合物结构失效而设计） |
| 卫生用品需求区间 | **20–150 kPa**（源文称来自 microactuator 研究） |

> ⚠️ **不换算**：两个数字**单位不同、量级相差约三个数量级**，源文未给换算路径或中间验证数据。**照录，不推断可行性。**

> 🔴 **manual_review（2026-09-29）**：本源无日期无署名、含 IP 收购目标与供应商优先级；本页**只记机理边界与流变对策**，不记录商务条款。

## 追加：Meeting Minutes 批（2026-09-29 追加 · HPC 胆甾相液晶、微流控像素架构与两项物理硬限制）

> 来源：[[Mechanochromic Screen from Molecule to Market — HPC Structural Colour & Deep-Tech Funding（压力变色环保屏）]]（外部技术资料的音频解读 ASR 转写，日期 [待验证]）。本批只**追加**，不修改既有结论；全部为**资料口径**，**未见原始文献**。

**载体：HPC（羟丙基纤维素）（本批新增）：**

- **HPC（hydroxypropyl cellulose）** = 纤维素衍生物；特性：成本低廉、**无毒**、**完全可生物降解**、**可食用**。
- **自组装条件**：HPC + **约 35 wt% 纯水** → **无需外力即自动自组装**成**胆甾相液晶（cholesteric liquid crystal）**。
- **呈色机理**：可想象为"**微观螺旋楼梯**"，**螺距**决定反射光 → **结构色**（源于物理间距而非色素，如孔雀羽毛、蝴蝶翅膀）。

**微流控像素架构（本批新增，三层三明治）：**

| 层 | 内容 |
| --- | --- |
| 底层 | 刻有**微流控通道**的硅胶网络 |
| 中层 | **200 μm 厚柔性硅胶膜**（"无数个微型气球"） |
| 其上 | **HPC 液膜** |
| 顶端 | **刚性玻璃板** |

- **动作链**：通气 → **气球膨胀上顶** → HPC 被压向玻璃板 → **螺旋楼梯被压扁、螺距变短** → **反射光蓝移** → 显色；
- **复位**：排气 → HPC **像海绵一样弹性回弹** → 颜色复原。

**两项物理硬限制（本批新增，决定该技术的生态位）：**

| 限制 | 数值 | 原因 |
| --- | --- | --- |
| **弛豫时间常数** | **约 52 ms** | 系统依赖**真实的立体流动 + 聚合物物理回弹**，必须"真的弹回去" → 稳定刷新率锁死在约 **5 Hz** |
| **像素极限** | **约 500 μm** | 像素更小则**底部气囊面积不足**，无法产生足够力量推动 HPC |

- → **这是物理规律硬限制，不是工艺可优化项**；结论是**不要和手机屏比**。
- **合适的生态位**：不需高频刷新、**不需发光 → 几乎不耗电** → **可持续电子阅读器、低频更新的交互式商业标牌、智能壁纸**。

**阈值与失效形态（本批新增，与本页既有"25–27% 应变区间"互相印证）：**

- **应变阈值 25**（ASR 作「25 帕 / 二十五八千」，疑为 **25% 应变**）[待验证] —— 与本页既有的 **25–27% 应变区间**一致，可作为交叉印证。
- 阈值内：材料像**完美弹簧**，信号稳定、变色与复原高度一致；
- **超阈值 → 剪切变稀（shear thinning）**：失去弹性，变成"**无法回弹的软泥**" → **信号大幅衰减、颜色不准**；
- → 工程上必须把气压控制在阈值内的"**黄金区间**"。

**最巧的一点：用几何学取代气压控制（本批新增）：**

- 气囊凸起幅度**同时受气压与像素自身宽度影响** → 因此**只需一个统一气压泵**，而在制作时**把不同像素的物理宽度做得不同**；
- 同一气压下：**宽像素凸起高（变色大）、窄像素凸起低（变色小）**；
- 在 **19×19 高密度阵列**中"**只吹一口气**"即呈现多色 → **用几何学多样性取代气压控制的复杂性**。

✅ **验证记录（2026-09-29）**：全部为**二手转述**，**未见原始文献与实验条件**；52 ms / 500 μm / 35 wt% / 200 μm / 19×19 等数字**在回溯原始文献前不得作为设计依据** [待验证]。25 阈值与本页既有 25–27% 区间互相印证，但单位口径仍待确认。参见 [[Mechanophore Mechanochromism（机械力致变色分子）]]、[[Chromism Taxonomy（变色现象分类）]]、[[Panel Hysteresis and Threshold Calibration（面板回滞与阈值标定）]]。

## 追加：Meeting Minutes 批 2（2026-09-29 追加 · 光子带隙、RCP 免偏振片、25–27% 阈值与 14 ms 性能）

> 来源：[[Force-to-Colour Direct Conversion — Mechanophore Chemistry & HPC Photonic Bandgap（把压力变成颜色）]]（对 `the chromatic shift.pptx` 的音频解读 ASR 转写，日期 [待验证]）。本批只**追加**，不修改既有结论；本批**明确了此前存疑的单位口径**。

**机理：光子带隙的可逆压缩（本批新增）：**

- 静止时：螺旋**间距宽** → **光子带隙**反射**较长波长** → 看到**红色**；
- 用力压缩：**间距变窄 → 光子带隙被压缩** → 反射波长变短 → **可预测、完全可逆的蓝移**。
- → 一句话：**颜色不是染料给的，是"弹簧的间距"给的**；压缩弹簧即改变音符。

**反射右旋圆偏振光（RCP）（本批新增，是一条此前未记录的实用优势）：**

- HPC 的螺旋结构像**天然的光学筛子**，**选择性反射右旋圆偏振光（RCP）**；
- 因此 **肉眼直接看或用普通数码相机拍摄都无需加装偏振片**，即可得到鲜艳纯粹的色彩（对比：传统液晶屏 / 3D 电影**必须戴偏振眼镜**，否则光线互相干扰、看起来糊）。
- 工程含义：**该结构色的可读性不依赖额外的光学元件** → 对低成本显示与机器视觉读取都友好。

**器件三层与驱动（本批新增，与上一批互相印证）：**

| 层 | 材料 |
| --- | --- |
| 底层 | **精密光刻微通道**（输入气动压力） |
| 中层 | **透明弹性薄膜（PDMS）**（像气球） |
| 顶层 | **坚硬的玻璃天花板** |

- **三步驱动：输入 → 驱动 → 压缩**；像素尺寸 **500 μm**（上一批记为 200 μm 膜 + 500 μm 像素，二者可对应：500 μm 为像素、200 μm 为膜厚）。

**应变阈值 —— 单位口径在本批得到明确（本批新增）：**

- **25–27%**（本页既有 append 亦记 25–27%，**至此确证为百分比应变**）。
- **失效形态**：超过阈值后，HPC 从"**能像弹簧一样上下回弹的稳定粘弹性状态**"直接转变为"**非弹性的横向流动状态**" —— 捏得太狠，它**不往上顶，而是像水一样向四周挤出去** → 整齐的螺旋结构被破坏 → **颜色衰退**（"弹簧被压散架了，颜色就糊了"）。
- → 工程要求：**必须把气压精准控制在阈值内**，且阈值窗口**本身很窄**（这是尽调中被质疑的点）。

**性能数据（本批新增）：**

| 指标 | 数值 | 对比 |
| --- | --- | --- |
| **响应时间** | **14 ms** | 对比过去 **631 ms** 的**机电基准**，快十几倍 |
| **开关频率** | **5 Hz** | 与上一批一致 |
| **应变灵敏度** | **1.40 nm/%**（波长偏移 / 应变）[待验证] | 气压—颜色映射**极其精确**，非线性映射也准 |

> ⚠️ **口径冲突（两处）**：① 同一份资料中另有一处作"**45 ms**"；② 上一批同源资料记为"**52 ms 弛豫时间常数**"。**14 / 45 / 52 ms 三者可能是不同定义（响应 vs 弛豫）**，**须回溯原始资料统一定义后再比较**。

✅ **验证记录（2026-09-29）**：全部为**二手转述**，**未见 `the chromatic shift.pptx` 原始文件**；14 ms / 631 ms / 5 Hz / 1.40 nm/% / 25–27% 等数字**在回溯前不得作为设计依据** [待验证]。25–27% 的单位口径**在本批得到确证**（此前记为"25，单位不明"）。参见 [[Mechanophore Mechanochromism（机械力致变色分子）]]、[[Panel Hysteresis and Threshold Calibration（面板回滞与阈值标定）]]、[[Chromism Taxonomy（变色现象分类）]]。

## Sources 来源

- [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Stretch-Triggered Colour Indicator for Diaper Pant Side Panels.pptx.md`
- [[Mechanochromic Materials Technical Review（EN v3, 2026-08）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Mechanochromic_TechReview_EN_v3_2026-08-02_fixed.pptx.md`
- [[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Mechanochromic_Waistband_Tension_Indicator_Proposal_2026-08-19.pptx.md`
- [[Chromic Materials Bibliography（变色材料书籍·温湿力精表）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/变色材料书籍_温湿力精表.xlsx.md`
- [[Strategic Roadmap - Commercializing Mechanochromic Materials（力致变色商业化战略路线图·X-Chromic 版）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/X-Chromic/Strategic Roadmap_ Commerciali....pdf.md`（2026-09-29 追加）

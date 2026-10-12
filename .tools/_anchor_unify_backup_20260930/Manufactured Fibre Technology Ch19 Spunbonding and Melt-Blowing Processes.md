---
type: source
title: "Manufactured Fibre Technology Ch19 Spunbonding and Melt-Blowing Processes"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Manufactured_Fibre_Technology/Manufactured Fibre Technology · analysis_ch19.md.md"
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Spunbonding is defined as continuous filament fibrous structures made in the form of fabrics, prepared from synthetic polymers in a process integrated with fibre manufacture; melt-blowing extrudes a polymer melt through a die into a high velocity stream of hot air to produce fine or super fine fibres [p.560]."
  - "The limiting factor in spunbond production by this route is not necessarily the threadline speed, but the filament handling or filament forwarding-jet device [p.563]."
  - "The level of charge, size of jet, the air velocity and the jet-to-laydown distance have an important influence on the uniformity of laydown [p.570]."
  - "In melt-blowing, air drag is the most important parameter that determines the final diameter of the fibre [p.583]; measured fibre diameters of 2–10 µm are far below the 22 µm predicted by the Matsui-based model, attributed to neglected viscous forces [p.585]."
  - "Melt-blown fibres are very delicate and relatively weaker than fibres produced by other processes, with much lower birefringence [p.588, p.590]."
  - "Higher MFI resins usually produce fibres with higher tenacity, higher modulus and lower elongation [p.590]; process evolution raised MFI from 33 to 450–1500 and lowered die temperature from ~315°C to ~230°C [p.582]."
  - "The air-drag friction factor correlates with Reynolds number as C_f = 0.91 N_Re^-0.61 (Chen et al. [32]) [p.573]."
summary_cn: "第19章系统阐述纺粘与熔喷两类熔体直接成网非织造工艺：概念界定、原料体系、喷枪/模头/气流等成网设备、空气曳力与雷诺数的动力学关联、熔喷纤维细度由空气曳力主导且实测远细于模型预测、高 MFI 树脂提升强度与取向。这是全书对 REL 聚烯烃非织造最直接相关的一章。"
tags: ["source/book", "spunbonding", "melt-blowing", "nonwoven", "spunlaid", "air-drag", "Reynolds-number", "birefringence", "MFI", "web-uniformity", "filament-forwarding-jet"]
tags_zh: ["纺粘法", "熔喷法", "非织造布", "空气曳力", "雷诺数", "双折射", "熔融指数", "纤网均匀性", "铺网喷枪"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Manufactured Fibre Technology]]", "[[Manufactured Fibre Technology Ch16 Polypropylene Fibres]]", "[[Meltblown Nonwoven（熔喷非织造布）]]", "[[Nonwoven Process Classification（非织造布工艺分类）]]", "[[Bicomponent Fibre Production & Performance Review — Spinneret, Crimp & Functional Masterbatch（复合纤维生产及性能探讨）]]", "[[三叶形截面纤维（Trilobal Fibre）]]"]
---

# Spunbonding and Melt-Blowing Processes 纺粘法与熔喷法

> Source: Manufactured Fibre Technology, Ch.19, pp.560–590.
> Author of chapter: B.C. Goswami. 工艺—设备综述性章节，参考文献 1–68；证据来源为 1970s–1990s 的 INDA-TEC 会议论文、J. Nonwoven Res.、Textile Res. J. 与大量专利（Du Pont、Freudenberg、Kinney [16]、Brock [26]、David & Mormon [27] 等）。

## Definition 定义

- **Spunbonding / spunlaid 纺粘**：[p.560] "continuous filament fibrous structures which are made in the form of fabrics... prepared from synthetic polymers in a process integrated with fibre manufacture"（由合成聚合物在**一体化流程**中制成的连续长丝纤维结构）。
- **Melt-blowing 熔喷**：[p.560] "fibrous structures produced by extruding a polymer melt through a die into a high velocity stream of hot air to produce fine or super fine fibres"（熔体经模头挤入高速热气流制成超细纤维）。
- **Non-woven 非织造布**：[p.560] "made by bonding of web-like arrays of fibres or filaments"。
- **Web 纤网**：[p.563] 经成网铺设、尚"does not have integrity and lacks mechanical characteristics"的纤维集合体，须经加固（bonding）才具实用性。
- **Air drag / friction factor 空气曳力/摩擦因子**：[p.573] 决定纺粘/熔喷长丝拉伸取向的核心力，以 C_f 与雷诺数 N_Re 关联。
- **POY 部分取向丝**：[p.564] 提高纺丝速度后得到的 partially oriented yarns，强度约为传统路线的 60%、伸长 140%。
- **Birefringence 双折射**：[p.588] 衡量纤维取向的量，熔喷纤维值远低于纺粘/熔纺。

## Spunbonding 纺粘

### Process chain 工艺链
原料（尼龙 / 聚酯 / 聚丙烯 / 聚乙烯及共聚物）→ 挤出成网（喷枪、静电铺网）→ 加固（化学 / 热 / 针刺 / 水刺）→ 性能三变量（Table 19.1）。

### Bottleneck is the jet, not the speed 瓶颈在喷枪而非纺丝速度
[p.563] "The limiting factor in the production of spunbonds by this route is not necessarily the threadline speed, but the filament handling or filament forwarding-jet device..." 作者明确指出控制元件是 haul-off gun，工艺差异主要体现在成网环节。

### Web uniformity 纤网均匀性
[p.570] "The level of charge, size of jet, the air velocity and the jet-to-laydown distance have an important influence on the uniformity of laydown." 增大喷丝到铺设距离、降低空气速度可延长电荷铺展时间，防止纤维成束（bunching）。

### Dynamics 动力学
Chen 等的摩擦因子—雷诺数统一关联式 [p.573]：

> "C_f = 0.91 N_Re⁻⁰·⁶¹ Chen et al. [32]"

Hajji et al. [39] 将单丝熔融纺丝模型（四阶微分方程组，含动量/能量/流变/结晶动力学）用于 Reicofil™ 工艺；双折射数据证明纺粘纤维与熔纺纤维取向一致。

## Melt-Blowing 熔喷

### Origin and process 起源与工艺
1951 年海军实验室起步，Exxon 商业化，专利主导。设备含模头（T 型 / 衣架型）、喷嘴、气流；参数见 Table 19.3–19.4。

### Air drag governs fineness 空气曳力决定细度
[p.583] "Air drag is the most important parameter that determines the final diameter of the fibre." 熔喷在离开模头时纤维仍熔融、被气流即时拉伸，区别于传统固态长丝的拉伸模型。

**模型失效（作者坦诚指出）**：Narasimhan & Shambaugh 套用 Matsui 模型，但实测直径 2–10 µm 远小于模型预测的 22 µm，归因于忽略黏性力 [p.585]。

### Structure and mechanical properties 结构与性能
- [p.590] "The fibres produced by the melt-blowing process are very delicate and are relatively weaker than the fibres produced by other processes." 熔喷纤维受力仅来自表面摩擦（skin friction），分子取向有限，故强度低、伸长高；双折射远低于纺粘/熔纺（Table 19.8，[p.588]）。
- [p.590] "Higher MFI resins usually produce fibres with higher tenacity, higher modulus and lower elongation." 空气流量增大带来更高拉伸与分子取向，颈部形变区域减少。

### Process evolution 工艺演进（Table 19.3，[p.582]）
| 参数 Parameter | 早期 Early | 当前 Current |
|---|---|---|
| MFI (g/10 min) | 33 | 450–1500 |
| Die temperature 模头温度 | ~315°C | ~230°C |

数据来源：Table 19.3 [p.582]；树脂牌号与加工温度、降解数据见 Table 19.6–19.7；双折射与力学指标见 Table 19.8–19.9。

## Evidence Chain 证据链

| 核心论点 Core claim | 支撑证据 Supporting evidence | 页码 |
|---|---|---|
| 纺粘瓶颈在喷枪而非速度 | Kinney 装置、静电铺网实验 | [p.563–565] |
| 熔喷细度由空气曳力决定 | Narasimhan & Shambaugh 模型 + 实测直径反证 | [p.583, p.585] |
| 熔喷纤维更弱、取向更低 | Table 19.8 双折射、Table 19.9 力学对比 | [p.588, p.590] |
| MFI / 气流提升强度 | 应力—应变曲线与结论陈述 | [p.590] |

证据类型统计：专利文献（[13]–[29]、[46] 等）大量，为工艺主流证据；实验动力学（Chen [32]、Mulligan [61]、Straeffer [64]）多篇；工业建模（Hajji [39]、Matsubara [47–50]）数篇；数据表 Table 19.1–19.10 共 11 个；图表曲线 Fig.19.9–19.25 多幅。

论证强弱：**强**——纺粘/熔喷概念、设备与参数描述证据充分，且有统一摩擦因子关联式可作量化锚点；**中**——动力学模型在纺粘侧与熔纺数据吻合良好，但熔喷侧模型显著高估纤维直径 [p.585]，作者归因为"忽略黏性力"，论证留有未解缺口；**弱**——纺粘成网纤维取向分布缺乏公开数据支撑 [p.572]，相关结论多为推断，且不同厂商结构差异使性能横向比较困难 [p.576]。

## Strengths and Gaps 亮点与不足

✅ 亮点：
- 将看似"黑箱"的产业化工艺还原为可量化的动力学模型，给出摩擦因子—雷诺数统一关联式 [p.573]。
- 通过 Table 19.3 清晰呈现工艺演进（MFI 由 33 升至 450–1500、模头温度由 ~315°C 降至 ~230°C）[p.582]。
- 坦诚指出模型失效：现有模型均低估熔喷实际细度 [p.585]。

⚠️ 不足：
- 公开文献匮乏被多次强调 [p.572]，大量技术细节仅存于专利，削弱了对机理的完整解释。
- 纺粘与熔喷篇幅不均，熔喷结构与性能数据更充分，纺粘成网机理（尤其纤维取向分布）论述相对薄弱 —— 原文标注 [未找到原句支撑，此为推断]。
- 图表（Fig.19.1–19.25）在正文中仅以文字转述，读者无原图难以建立设备空间概念。

## Hygiene Implication 卫生材料启示（REL 相关性）

**本章是全书对 REL 工作最直接相关的一章**——纺粘/熔喷正是卫生用品面层、拒水层、SMS/SMMS 与导流层的成形工艺：

- **PP/聚烯烃非织造的工艺圣经**：本章与 [[Manufactured Fibre Technology Ch16 Polypropylene Fibres]] 构成"树脂（MFI、分子量分布、稳定剂）→ 熔体纺丝 → 直接成网"的完整链条，是理解纺粘与熔喷工艺窗口的基础。MFI 由 33 升至 450–1500、模头温度由 ~315°C 降至 ~230°C [p.582] 这一演进，正是今天高 MFI 卫材专用料路线的由来。
- **纤维细度—孔径—液体管理的因果链**：熔喷纤维直径由空气曳力主导 [p.583]，实测 2–10 µm；细度直接决定孔径分布与毛细吸力，是面层透水（strike-through）、回渗（rewet）与阻隔（barrier）性能的物理根源。可对照 [[Meltblown Nonwoven（熔喷非织造布）]] 与 [[Nonwoven Process Classification（非织造布工艺分类）]]。
- **纤网均匀性**：静电充电水平、喷枪尺寸、空气速度与喷丝到铺设距离共同决定铺网均匀性 [p.570]。这一"均匀性四变量"直接对应卫材面层的克重 CV 与局部渗漏风险，是产线调试的可操作清单。
- **熔喷纤维弱、取向低的工程后果**：[p.590] 熔喷层强度低、伸长高，故 SMMS 结构必须以纺粘层承担力学，熔喷层只提供阻隔——这是卫材 SMS/SMMS 层序设计的材料学依据。
- **高 MFI 提升强度与取向** [p.590]：为"高 MFI 树脂 + 低温加工"的节能高速路线提供理论依据，也解释了树脂降解（Table 19.6–19.7）对纤维强度的影响。
- **双组分与截面**：本章未展开双组分纺粘与异形截面（原文无相关论述 [待验证]），REL 侧实践见 [[Bicomponent Fibre Production & Performance Review — Spinneret, Crimp & Functional Masterbatch（复合纤维生产及性能探讨）]] 与 [[三叶形截面纤维（Trilobal Fibre）]]。

## Related Sources 关联来源

- [[Manufactured Fibre Technology]] — book index
- [[Manufactured Fibre Technology Ch16 Polypropylene Fibres]] — 同一树脂体系的熔体纺丝上游章节
- [[Meltblown Nonwoven（熔喷非织造布）]] — 熔喷工艺在卫材中的落地应用
- [[Nonwoven Process Classification（非织造布工艺分类）]] — 纺粘/熔喷在非织造工艺谱系中的定位
- [[Bicomponent Fibre Production & Performance Review — Spinneret, Crimp & Functional Masterbatch（复合纤维生产及性能探讨）]] — 双组分纺粘与功能母粒的 REL 侧资料
- [[三叶形截面纤维（Trilobal Fibre）]] — 异形截面纤维对卫材手感与遮盖的影响

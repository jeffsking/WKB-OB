---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_2159605ca99d48cc85d98d388d409d29001a693ee6c0644e"
source_file: "Manufactured Fibre Technology · analysis_ch19.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Manufactured_Fibre_Technology/Manufactured Fibre Technology · analysis_ch19.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Manufactured Fibre Technology · analysis_ch19.md.md

# 第19章 《Spunbonding and melt-blowing processes》— 深度拆解

## 一、本章核心内容概览（120-200字）

本章由 B.C. Goswami 撰写，系统阐述纺粘（spunbonding / spunlaid）与熔喷（melt-blowing）两类直接由聚合物熔体成网的非织造（nonwoven）工艺。先界定两者概念：纺粘为连续长丝在一体化流程中成布，熔喷则借助高速热气流将熔体拉伸成超细纤维（super fine fibres）并沉积成纤网（web）。随后分别梳理原料体系、制造设备（纺丝组件、喷枪/喷嘴、模头、收集帘）、成网动力学模型（空气曳力 friction drag、雷诺数 Reynolds number），以及纤维结构与力学性能。全章以专利与实验研究为证据，贯通了从长丝纺丝到非织造直接成网的技术延伸。

## 二、本章重要观点（3-6条）

观点1：纺粘工艺的核心是"聚合—纺丝—成网—加固"一体化，瓶颈在于长丝输送喷枪而非纺丝速度。 / 页码：[p.563] / 原文摘选：> "The limiting factor in the production of spunbonds by this route is not necessarily the threadline speed, but the filament handling or filament forwarding-jet device..." / 解读：作者明确指出 controlling element 是 haul-off gun，工艺差异主要体现在成网环节。

观点2：纺粘纤网的均匀性取决于静电充电水平、喷枪尺寸、空气速度与喷丝到铺设距离的动态交互。 / 页码：[p.570] / 原文摘选：> "The level of charge, size of jet, the air velocity and the jet-to-laydown distance have an important influence on the uniformity of laydown." / 解读：增大喷丝距离、降低空气速度可延长电荷铺展时间，防止纤维成束（bunching）。

观点3：熔喷的本质是用极高空气曳力把熔体直接拉细成超细纤维，纤维直径由空气曳力主导。 / 页码：[p.583] / 原文摘选：> "Air drag is the most important parameter that determines the final diameter of the fibre." / 解读：熔喷在离开模头时纤维仍熔融、被气流即时拉伸，区别于传统固态长丝的拉伸模型。

观点4：熔喷纤维比熔融纺丝或纺粘纤维更弱、双折射更低。 / 页码：[p.590] / 原文摘选：> "The fibres produced by the melt-blowing process are very delicate and are relatively weaker than the fibres produced by other processes." / 解读：熔喷纤维受力仅来自表面摩擦（skin friction），分子取向有限，故强度低、伸长高。

观点5：高熔融指数（MFI）树脂与高空气流量可提升熔喷纤维强度与取向。 / 页码：[p.590] / 原文摘选：> "Higher MFI resins usually produce fibres with higher tenacity, higher modulus and lower elongation." / 解读：空气流量增大带来更高拉伸（draw）与分子取向，颈部形变区域减少。

## 三、本章研究方法与数据来源

本章属工艺—设备综述性章节，证据主要来自：(1) 专利文献——纺粘与熔喷技术公开成果多集中于专利，如 Du Pont、Freudenberg、Kinney [16]、Brock [26]、David & Mormon [27] 等；(2) 实验动力学研究——Chen et al. [32] 设计悬挂长丝经吸气器的力平衡实验测定张力；Mulligan & Haynes [61]、Straeffer & Goswami [64] 模拟熔喷条件；(3) 工业建模——Hajji et al. [39] 将单丝熔融纺丝模型（四阶微分方程组，含动量/能量/流变/结晶动力学）用于 Reicofil™ 工艺；(4) 系统性参数表——Table 19.3 对比早期与当前工艺条件，Table 19.6–19.7 给出树脂牌号与加工温度、降解数据，Table 19.8–19.9 汇总双折射与力学指标。数据来源以 1970s–1990s 的 INDA-TEC 会议论文、J. Nonwoven Res.、Textile Res. J. 为主。

## 四、本章论证过程

- 概念界定：从非织造布定义出发，区分 carding/wet-laying 与 melt-extruded 成网，引出纺粘、熔喷。
- 纺粘技术链：原料（聚酰胺/聚酯/聚丙烯）→挤出成网（喷枪、静电铺网）→加固（化学/热/针刺/水刺）→性能三变量（Table 19.1）。
- 动力学校验：以 Chen et al. 的摩擦因子—雷诺数关联（Cf=0.91NRe⁻⁰·⁶¹）对比多家研究，并用双折射数据证明纺粘纤维与熔纺纤维取向一致。
- 熔喷技术链：起源（1951 海军实验室）→Exxon 商业化→模头/喷嘴/气流设计→动力学校验（Narasimhan & Shambaugh 套用 Matsui 模型，但实测直径 2–10µm 远小于模型预测 22µm，归因于忽略黏性力）。
- 结构—性能闭环：用双折射、应力—应变、降解数据说明气流与 MFI 对纤维细度、强度、取向的决定作用。
## 五、本章在全书中的作用

本书《Manufactured Fibre Technology》主线为化纤（长丝/短纤）制造。此前各章聚焦传统纺丝与纤维结构；本章将视角从"单丝成形"推进到"长丝直接成网"，是从纤维（fibre）到非织造布（nonwoven fabric）的关键转折。它把已建立的熔融纺丝、取向、结晶动力学知识直接嫁接到纺粘与熔喷，证明非织造直接成网只是纺丝—拉伸—收集环节的重构，从而把"化纤技术"版图扩展到产业用纺织品领域。

## 六、本章亮点与不足

✅ 亮点：
- 将看似"黑箱"的产业化工艺还原为可量化的动力学模型，给出摩擦因子—雷诺数统一关联式 [p.573]：> "C_f = 0.91 N_Re⁻⁰·⁶¹ Chen et al. [32]"。
- 通过 Table 19.3 清晰呈现工艺演进（MFI 由 33 升至 450–1500、模头温度由 ~315°C 降至 ~230°C）[p.582]。
- 坦诚指出模型失效：现有模型均低估熔喷实际细度 [p.585]，体现严谨学术态度。

⚠️ 不足：
- 公开文献匮乏被多次强调 [p.572]、[p.634 类似处]，大量技术细节仅存于专利，削弱了对机理的完整解释。
- 纺粘与熔喷篇幅不均，熔喷结构与性能数据更充分，纺粘成网机理（尤其纤维取向分布）论述相对薄弱 [未找到原句支撑，此为推断]。
- 图表（Fig.19.1–19.25）在正文中仅以文字转述，读者无原图难以建立设备空间概念。

## 七、本章关键术语与概念

- Spunbonding / spunlaid（纺粘）：[p.560] "continuous filament fibrous structures which are made in the form of fabrics... prepared from synthetic polymers in a process integrated with fibre manufacture"（由合成聚合物在一体化流程中制成的连续长丝纤维结构）。
- Melt-blowing（熔喷）：[p.560] "fibrous structures produced by extruding a polymer melt through a die into a high velocity stream of hot air to produce fine or super fine fibres"（聚合物熔体经模头挤出至高速热气流中制成超细纤维的结构）。
- Non-woven（非织造布）：[p.560] "made by bonding of web-like arrays of fibres or filaments"（由纤维/长丝纤网经黏合制成的片状材料）。
- Web（纤网）：[p.563] 经成网铺设、尚"does not have integrity and lacks mechanical characteristics"的纤维集合体，需经加固才具实用性。
- Air drag / friction factor（空气曳力/摩擦因子）：[p.573] 决定纺粘/熔喷长丝拉伸取向的核心力，以 C_f 与雷诺数 N_Re 关联。
- POY（部分取向丝）：[p.564] 提高纺丝速度后得到的 partially oriented yarns，强度约为传统路线的 60%、伸长 140%。
- MFI / Melt Flow Index（熔融指数）：[p.582] 影响熔喷纤维细度与强度的树脂指标，工艺已用至 450–1500 g/10min。
- Birefringence（双折射）：[p.588] 衡量纤维取向的量，熔喷纤维值远低于纺粘/熔纺。
## 八、本章逻辑结构

- 19 引言：织物与非织造定义、纺粘/熔喷概念界定
- 19.2 纺粘织物

- 19.2.1 引言：1940s 起源、1960s 商业化（Du Pont、Freudenberg）
- 19.2.2 原料：尼龙/聚酯/聚丙烯/聚乙烯及共聚物
- 19.2.3 制造工艺：挤出→喷枪铺网→加固；喷枪/静电/喷嘴设计；Table 19.1 三变量
- 19.2.4 工艺动力学：Chen et al. 力平衡、Hajji 工业模型
- 19.3 熔喷织物

- 19.3.1 引言：1951 海军实验室、Exxon 商业化、专利主导
- 19.3.2 制造工艺：模头（T型/衣架型）、喷嘴、气流、Table 19.3–19.4 参数
- 19.3.3 工艺动力学：空气曳力模型、模型与实测偏差
- 19.3.4 结构与力学性能：双折射、应力—应变、降解、Table 19.8–19.10
- 参考文献 1–68
## 九、本章证据链分析

-

核心论点→支撑证据

- 论点"纺粘瓶颈在喷枪而非速度" → [p.563–p.565] Kinney 装置、静电铺网实验
- 论点"熔喷细度由空气曳力决定" → [p.583] Narasimhan & Shambaugh 模型 + [p.585] 实测直径反证
- 论点"熔喷纤维更弱、取向更低" → [p.588] Table 19.8 双折射、[p.590] Table 19.9 力学对比
- 论点"MFI/气流提升强度" → [p.590] 应力—应变曲线与结论陈述
证据类型统计表
| 证据类型 | 代表出处 | 数量感 |
|---|---|---|
| 专利文献 | [13]–[29]、[46] 等 | 大量，工艺主流 |
| 实验动力学 | Chen[32]、Mulligan[61]、Straeffer[64] | 多篇 |
| 工业建模 | Hajji[39]、Matsubara[47–50] | 数篇 |
| 数据表 | Table 19.1–19.10 | 11 个表 |
| 图表曲线 | Fig.19.9–19.25 | 多幅 |

-

论证强弱评估

- 强：纺粘/熔喷概念、设备与参数描述证据充分，且有统一摩擦因子关联式可作量化锚点。
- 中：动力学模型在纺粘侧与熔纺数据吻合良好，但熔喷侧模型显著高估纤维直径 [p.585]，作者归因为"忽略黏性力"，论证留有未解缺口。
- 弱：纺粘成网纤维取向分布缺乏公开数据支撑 [p.572]，相关结论多为推断；不同厂商结构差异使性能横向比较困难 [p.576]。


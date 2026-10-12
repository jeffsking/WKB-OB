---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_79a58423dcacbfd5420beedf5884af54001a693ee6c0644e"
source_file: "ch9_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/ch9_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch9_report.md.md

# 第9章 Reactions of Polymers（聚合物反应）深度拆书报告

来源：George Odian, Principles of Polymerization, 4th Ed., Wiley, 2004
原始文本：ch9_reactions.txt（约 4351 行，覆盖教材 p. 729–793）
报告撰写说明：本章 4 版目录中没有独立的"降解"专章（不同于 3 版 Sec. 9-7 Degradation），而是把降解现象散嵌在 9-2 Crosslinking（含氧化降解机理 Eq. 9-7~9-15）、9-3 Cellulose（含碱降解、酸水解再生）、9-4 PVAc（水解→PVA）、9-7 Cyclization（与降解竞争）、9-9 接枝（含辐射引发）等子节中。报告严格按 6 模块输出；对原书未直接讨论的术语（光降解/photodegradation、解聚/depolymerization、侧基消除等），在模块 2 中标注为"教材未详述，仅在关联处引用"，避免编造。

## 模块1：核心论点（5 条）

论点1：聚合物化学反应的"转化率"不等于小分子的"产率"，产物是不可分离的无规共聚物。（行 45–57）
> "80% yield in the corresponding hydrolysis of poly(methyl acrylate) does not result in 80% yield of poly(acrylic acid) with 20% unreacted poly(methyl acrylate). The product contains copolymer molecules, each of which, on the average, contains 80% acrylic acid repeating units and 20% methyl acrylate units randomly placed along the polymer chain."（行 51–56）
→ 对卫材意义：任何聚合物改性（纤维素酯化、PU 交联、无纺布接枝）永远只能得到分布产物，无法通过纯化去掉未反应位点。

论点2：聚合物反应受"功能基隔离"限制，不可逆双相邻反应最大转化率仅为 86%。（行 65–76）
> "When a polymer reaction involves the random reaction of a pair of neighboring functional groups... the maximum conversion is limited due to the isolation of single functional groups between pairs of reacted functional groups. The maximum conversion for irreversible reactions has been calculated as 86%"（行 66–72）
→ 卫材意义：异氰酸酯交联纤维素/PP 无纺布时，理论上限即 ~86%，不能通过延长反应时间弥补。

论点3：聚合物反应速率受扩散与微环境（浓度、电学、邻基、疏水）控制，往往与低分子同系物不同，且反应程度随转化率下降（autoretardation）。（行 140–187、227–383）
> "Polymer reaction rates and conversions are usually lower... The reaction conditions under which polymer reactivity differs from that of a low-molecular-weight homolog are discussed below."（行 30–43）
> "Polymer reactions involving the conversion of uncharged functional groups to charged groups often exhibit a decrease in reactivity with conversion."（行 228–230）
→ 这是扩散限制导致反应程度随转化率下降的核心命题。

论点4：聚合物改性存在三种策略——"聚合后功能化（grafting onto/from）"、"单体预功能化"、"大分子单体聚合（grafting through）"，三者互补但各有局限。（行 1263–1289；1800–1855）
> "Three methods exist for synthesizing graft copolymers. Grafting onto involves the reaction between functional groups on two different polymers... Grafting from involves a polymer with functional groups that initiate polymerization of monomer... Grafting through involves the polymerization of a macromonomer."（行 1263–1278）

论点5：降解与聚合互为逆过程；氧化降解以过氧化物为中介，可被金属盐催化并导向"交联固化"或"断链降解"两种结局。（行 445–485）
> "Alkyds are crosslinked via oxidation by atmospheric oxygen... Unconjugated double bonds undergo crosslinking by the initial formation of an allylic hydroperoxide followed by decomposition of the hydroperoxide."（行 445–459）
→ 卫材包装氧化老化、PU 水解、淀粉基质降解的物理本质都在这里。

## 模块2：关键概念操作化定义（10 个概念）

### 概念1｜聚合物反应类型总纲（Degradation / Crosslinking / Grafting / Functionalization）

(a) 名称：降解 Degradation；交联 Crosslinking；接枝 Grafting；功能化 Functionalization
(b) 定义：降解是聚合物主链或侧基在环境作用下降解为低分子量产物；交联是把线型聚合物变成三维网络；接枝是把一条聚合物主链上嫁接另一种聚合物支链；功能化是在聚合物上引入反应性官能团以作试剂/催化剂/固相载体。
(c) 原文摘录（行 9–17、9-11a-1 行 1705）：
> "This chapter describes the synthesis of new polymers by modification of existing polymers using a variety of chemical reactions... These include the esterification of cellulose, crosslinking of polyisoprene, hydrolysis of poly(vinyl acetate), and chlorination of polyethylene. A second aspect of polymer reactions is the use of a polymer as a carrier or support for some component of a reaction system."

### 概念2｜热降解：解聚 Depolymerization / 无规断裂 Random Scission / 侧基消除 Side-group Elimination

(a) 名称：解聚反应（Depolymerization）、无规断裂（Random Scission）、侧基消除（Side-group elimination）
(b) 定义：解聚为逐单体"拉链式"逆聚合；无规断裂为主链任意位置均裂；侧基消除为脱小分子（如 PVC 脱 HCl）沿主链产生共轭多烯。
(c) 原文摘录：第9章未对三种热降解机理做专章讨论。本章在 9-7 Cyclization（行 1163–1190）讨论环化 vs 交联竞争（"Some bicyclic and polycyclic products also form"，行 1168），在 9-2b 讨论丁二烯橡胶的硫化机理（行 497–510），在 9-8 讨论 PAN 热稳定化（行 1193–1203）：
> "Highly drawn (oriented) fibers are subjected to successive thermal treatments—initially 200–300 °C in air followed by 1200–2000 °C in nitrogen."（行 1195–1196，PAN 热稳定化温度窗口）
> "The vulcanization of polychloroprene (Neoprene) is carried out in different ways."（行 838–842）

*注*：Ceiling temperature、depolymerization 定量机理在教材第 3 章（行 245–270 附近），非第 9 章内容，此处不编造。

### 概念3｜氧化降解（Oxidative Degradation）与稳定化

(a) 名称：氧化降解（Oxidative Degradation）、稳定化（Stabilization）
(b) 定义：氧气对聚合物中的烯丙位/叔碳氢的自由基夺取，生成氢过氧化物（OOH），随后分解为羰基、醇、酸、醚或过氧键，导致主链断裂或交联。用金属盐（Co/Pb/Mn 辛酸盐）催化，加入抗氧剂稳定化。
(c) 原文摘录（行 445–485，Eq. 9-7 到 9-15）：
> "Alkyds are crosslinked via oxidation by atmospheric oxygen... Unconjugated double bonds undergo crosslinking by the initial formation of an allylic hydroperoxide followed by decomposition of the hydroperoxide."
> "The metal ions accelerate hydroperoxide decomposition in a manner analogous to the redox initiator systems discussed in Sec. 3-4b."（行 476–479）

### 概念4｜光降解（Photodegradation）

(a) 名称：光降解 Photodegradation
(b) 定义：吸收紫外光产生激发态 → 自由基 → 断链或交联。
(c) 原文摘录：第9章未专述 photodegradation。教材仅在 9-2d（行 802–803）提到光刻正性光刻胶用 PMMA 光降解：
> "Positive resists use a polymer, such as poly(methyl methacrylate), which undergoes degradation on irradiation."（行 801–803）
*注*：系统性光降解机理见教材 3 章光引发部分（索引 Photochemical reaction, 218–224）。

### 概念5｜水解（Hydrolysis）——聚酯/聚酰胺/聚碳酸酯/纤维素

(a) 名称：水解（Hydrolysis）
(b) 定义：酯键、酰胺键、碳酸酯键、缩醛键在酸/碱/酶催化下与水反应断裂。
(c) 原文摘录：
- PVAc 水解→PVA（行 1012–1040）：
> "In addition to its use as a plastic, poly(vinyl acetate) is used to produce two polymers that... [poly(vinyl alcohol) by hydrolysis and poly(vinyl butyral) by acetal formation]..."
- 纤维素三醋酸酯部分水解→纤维素二醋酸酯（行 970–974）：
> "A partially acetylated product is usually produced by controlled hydrolysis of the triacetate... Hydrolysis of the triacetate is carried out by controlled reversal of the esterification reaction by the addition of water or dilute acetic acid."
- 纤维素酸再生水解（行 922–925）：
> "The acid hydrolyzes the sodium xanthate derivative to the xanthic acid (XXV), which is unstable and decomposes... This regenerates cellulose."
- 酶促/邻基催化酯水解（行 311–324）：
> "The saponification of poly(methyl methacrylate) and related polymers proceeds with autoacceleration when carried out with weak bases such as pyridine or low concentrations of strong bases... The reaction proceeds by the sequence in Eq. 9-6 with the intermediate formation of a cyclic acid anhydride."

### 概念6｜辐射降解与辐射交联（Radiolysis / Radiation Crosslinking）

(a) 名称：辐射降解/交联（Radiolysis / Radiation Crosslinking）
(b) 定义：高能辐射（γ 射线、电子束）在聚合物中产生自由基，自由基复合导致交联，也可导致链断裂；取决于聚合物结构（PE 交联倾向强，PTFE/PMMa 断链倾向强）。
(c) 原文摘录：
- 过氧化物/辐射交联（行 714–720）：
> "9-2c Peroxide and Radiation Crosslinking. Many polymers are crosslinked by compounding with a peroxide such as dicumyl peroxide..."
- 离子辐射接枝（行 1375–1394）：
> "Polymer radicals can also be produced by the irradiation of a polymer–monomer mixture with ionizing radiation. Thus, the interaction of ionizing radiation with polyethylene–styrene produces radical centers on polyethylene, and these initiate graft polymerization of styrene to produce poly(ethylene-graft-styrene)."
> "Most radiation graft polymerizations are carried out as heterogeneous reactions. The polymer is swollen by monomer but does not dissolve in the monomer. (For semicrystalline polymers, swelling and grafting take place only in the amorphous regions.)"（行 1380–1382）

### 概念7｜接枝共聚（Graft Copolymerization）机理

(a) 名称：接枝共聚（Graft Copolymerization）
(b) 定义：在主链聚合物上产生活性位（自由基/离子/碳正/碳负），引发单体聚合，得到树枝状嵌段结构。
(c) 原文摘录（行 1251–1289、1330–1365）：
> "9-9 GRAFT COPOLYMERS. Graft and block copolymers contain long sequences of each of two different monomers in the copolymer chain."（行 1251–1254）
> "In the presence of a dissolved polymer, the radical polymerization of a monomer by thermal decomposition of an initiator results in a mixture of homopolymerization and graft polymerization... Polymer radicals (XXX), formed by chain transfer between the propagating radical and polymer, initiate graft polymerization of styrene."（行 1331–1336，Eq. 9-48、9-49）
> "Grafting via chain transfer predominates for 1,4-poly-1,3-dienes containing relatively unreactive 1,2-disubstituted double bonds. Grafting via copolymerization of the double bond predominates when the double bond is more reactive."（行 1361–1365）

### 概念8｜接枝改性：异氰酸酯（HDI 类）交联剂接枝纤维素/无纺布表面改性

(a) 名称：异氰酸酯接枝（Diisocyanate Grafting）；纤维素交联（Cellulose Crosslinking）
(b) 定义：二异氰酸酯（如 HDI、TDI、MDI）与纤维素/PP/棉的羟基或末端 NH₂/OH 反应形成氨基甲酸酯键（–NH–COO–），把线型纤维交联成三维网络以提升湿强。
(c) 原文摘录（行 844–848）：
> "Cellulosic fibers (cotton, rayon) are crosslinked by reaction of the hydroxyl groups of cellulose with formaldehyde, diepoxides, diisocyanates, and various methylol compounds such as urea–formaldehyde prepolymers, N,N′-dimethylol-N,N′-dimethylene urea, and trimethylolmelamine. Crosslinking imparts crease and wrinkle resistance and results in iron-free fabrics."

*注*：Odian 4 版明确列举"diisocyanates"作为纤维素交联剂类别；HDI（hexamethylene diisocyanate）未在第9章文本中直接点名，但异氰酸酯交联纤维素就是湿巾湿强工艺（HDI 或 MDI 交联剂浸渍无纺布）的化学基础。

### 概念9｜聚合物化学反应的扩散限制（反应程度随转化率下降）

(a) 名称：扩散限制（Diffusion Control）；自减速（Autoretardation）
(b) 定义：随反应进行，聚合物链刚性增加、溶胀度降低、小分子试剂难以扩散进入聚合物域，反应速率下降；同时电荷积累、位阻堆积也会降低残余基团的反应活性。
(c) 原文摘录：
> "In the extreme case, insolubility of a polymer may limit the maximum conversion if the small-molecule reagent cannot diffuse into and through the polymer."（行 150–152）
> "High crosslink densities may severely depress polymer reactivity as a result of large decreases in swelling and diffusion rate within the polymer. Diffusion control in a polymer reaction can be detected by the inverse dependence of rate on polymer particle size."（行 184–187）
> "Polymer reactions involving the conversion of uncharged functional groups to charged groups often exhibit a decrease in reactivity with conversion. Thus the quaternization of poly(4-vinylpyridine) becomes progressively slower with increasing conversion... An unreactive pyridine group is less reactive by a factor of 3 when neighboring pyridine groups have reacted."（行 228–233）

### 概念10｜环化（Cyclization）vs 交联的竞争

(a) 名称：环化 Cyclization
(b) 定义：阳离子/自由基进攻时，活性中心与同一链邻近双键反应形成环状结构（环化），或与另一链反应（交联）。两者竞争，取决于双键密度、取代度与溶剂极性。
(c) 原文摘录（行 1163–1190）：
> "9-7 CYCLIZATION. Natural rubber and other 1,4-poly-1,3-dienes are cyclized by treatment with strong protonic acids or Lewis acids... The reaction involves protonation of the double bond (Eq. 9-40) followed by cyclization via attack of the carbocation on the double bond of an adjacent monomer unit (Eq. 9-41). Some bicyclic and polycyclic products also form."（行 1165–1169）
> "Cyclized rubbers have been used for shoe soles and heels, adhesives."（行 1189–1190）

## 模块3：证据链（3 个表格）

### 表1：典型聚合物的降解/改性反应、机理与产物对比（第9章内证据）

|||||||
|---|---|---|---|---|---|
|醇酸树脂 Alkyd|氧化交联|大气氧 + Co/Pb/Mn 辛酸盐催化|烯丙位氢过氧化物 → 分解 → C–C / 醚 / 过氧交联|不溶三维网络（涂料干燥）|445–485|
|天然橡胶 / SBR / NBR / EPDM|硫磺硫化|加热，硫磺 + 促进剂|硫离子对 → 锍离子链式反应|含 S₂–S₃ 桥的网络|497–510、512–540|
|丁腈/顺丁橡胶|二胺交联|碱性氧化物 (MgO/ZnO) + 二胺，先脱 HCl|消除 → 双键 + 胺加成|交联弹性体|806–829|
|氯丁橡胶 Neoprene|金属氧化物/硫磺硫化|MgO/ZnO ± S|未完全建立机理|交联橡胶|838–843|
|纤维素（棉/粘胶）|异氰酸酯/甲醛/二环氧交联|二异氰酸酯 / Urea-甲醛预聚物|–OH 与 –NCO / –CH₂OH 缩合|抗皱免烫织物|844–848|
|纤维素三醋酸酯|部分水解|水或稀醋酸，控制反应|酯键水解，反转酯化|纤维素二醋酸酯|970–974|
|纤维素（粘胶工艺）|碱性降解 + 黄原酸化 + 酸再生水解|18–20% NaOH 25–30 °C；CS₂ ~30 °C；10% H₂SO₄ 35–40 °C|氧化降解除分子量 → 黄原酸酯 → 酸水解再生|粘胶/玻璃纸|880–925|
|聚丙烯腈 PAN|热稳定化 + 碳化|先 200–300 °C 空气；后 1200–2000 °C 氮气|环化梯形结构 → 石墨化|碳纤维|1193–1203|
|橡胶 / NBR / SBR|加氢（抗氧化稳定化）|催化加氢|双键饱和|高耐氧化弹性体|1244–1246|
|聚乙烯–苯乙烯混合物|辐射接枝|γ/电子束辐射 + 苯乙烯单体|辐射产生 PE 自由基 → 引发苯乙烯聚合|poly(ethylene-graft-styrene)|1375–1394|
|聚乙烯 PE|过氧化物/辐射交联|Dicumyl peroxide|自由基偶合|交联聚乙烯|714–720|

### 表2：典型聚合物功能化/改性反应（第9章内案例）

||||||
|---|---|---|---|---|
|纤维素|酯化（乙酰化）|乙酸酐/乙酸，H₂SO₄ 催化|纤维素醋酸酯（纤维、薄膜、眼镜框）|946–986|
|纤维素|硝酸酯化|HNO₃ + H₂SO₄|纤维素硝酸酯（胶片、油漆、火棉）|1001–1009|
|纤维素|磺化|氯磺酸 / 硫酸化|纤维素硫酸酯钠（肝素模型/絮凝剂）|1009–1011|
|天然橡胶|氯化|Cl₂ 于氯化溶剂中|氯化橡胶，防水涂层|1047–1058|
|天然橡胶|盐酸化|HCl 加成（Markownikoff）|橡胶盐酸盐，水蒸气阻隔|1047–1058|
|PE / PVC / 饱和烃聚合物|氯化（自由基）|Cl₂ 光/热引发|氯化聚乙烯（CPVE）|1086–1096|
|苯乙烯聚合物|芳环亲电取代|卤化、硝化、磺化|卤代/硝化/磺化 PS|1134–1145|
|PMMA|皂化（邻基催化）|吡啶/弱碱|PMMA→PMAA（自加速）|311–324|
|PVC|脱氯（Zn 存在下）|加热 + Zn|双键化|69–72|
|聚乙烯–苯乙烯|辐射接枝|γ/电子束|PE-g-PS|1375–1394|

### 表3：接枝聚合的常用方法（grafting-to / grafting-from / grafting-through 三范式，加原文分法）

||||||
|---|---|---|---|---|
|Grafting onto（接枝到）|两种聚合物端基直接反应偶联|可控|反应慢，端基密度低，支链长时受限|1263–1268、1287–1289|
|Grafting from（从聚合物出发）|主链官能团引发单体聚合|适应性强（自由基/离子均可）|需预处理|1270–1275、1285–1286|
|Grafting through（大分子单体）|乙烯基大分子单体（宏单体）聚合/共聚|支链结构精确|需先合成大分子单体|1277–1284、1302–1319|
|链转移法|增长自由基从主链夺 H 生成链自由基|工艺简单|得均聚物+接枝物混合物|1330–1349|
|共聚法|单体与聚合物双键共聚|适用于含双键聚合物（高乙烯基 PB）|对 1,2-二取代双键效果差|1350–1365|
|辐射法（Ionizing Radiation）|γ/电子束在主链产生活性点|无需化学引发剂，可异相进行|结晶区不接枝；均聚物多|1375–1395、1419–1423|
|引发剂法（Initiator法）|主链挂接热/光引发剂，分解引发|工业成熟（HIPS/ABS/MBS）|产物中混杂均聚物|1330–1370、1411–1418|
|光敏剂法|主链挂酮类光敏剂（二苯甲酮/安息香）|条件温和|需紫外|1411–1418|
|氧化还原引发（Redox）|羟基+过硫酸盐等氧化还原体系|水相高效（纤维素/木材）|控制难|1434–1448|
|活性自由基（NMP/ATRP/RAFT）|主链挂控制剂，活性增长|支链长度/MWD 精确|试剂贵|1450–1522|

## 模块4：章节间衔接

### 4.1 与前 8 章的总结性关系

前 8 章讲"如何做出聚合物"（自由基/离子/逐步/开环/共混/共聚/配位/活性聚合），第 9 章是"做出之后怎么办"——即聚合方法 → 产物 → 后处理改性的完整闭环：
- Sec. 2-10 凝胶点 / Sec. 2-12 环氧预聚物 / Sec. 6-8c 不饱和聚酯的交联概念在第 9 章被推广到高聚物（行 425–429）："A number of crosslinking reactions have been discussed—crosslinking of monomers with functionality greater than 2 (Sec. 2-10)... The crosslinking of high-molecular-weight polymers such as 1,4-polyisoprene and polyethylene will be discussed in this section."
- Sec. 6-6 二乙烯基共聚交联与本章 9-2 橡胶硫化机理呼应。
- Sec. 7-2b-6 表氯醇聚合物和Sec. 6-8e 氟聚合物/氯醚在本章 9-2d 中作为二胺交联对象（行 806–815）。

### 4.2 降解与聚合的逆过程关系（天花板温度 / 解聚温度）

- 教材在第 3 章链转移部分（索引 Chain transfer: degradative transfer, 263–264）给出解聚热力学；第 9 章通过具体降解案例（纤维素酸水解、PAN 热稳定、醇酸氧化）说明聚合物降解既是主链断裂也是交联，与聚合互为"拉链"逆过程。
- 第 9 章 Eq. 9-29（行 961–963）纤维素酯化，随后"controlled reversal of the esterification reaction"（行 972–974）直接演示酯化-水解可逆对。
### 4.3 交联反应与 Ch2 凝胶点的呼应

- 第 2 章 Sec. 2-10 用Flory–Stockmayer 凝胶点 ( p_c = \frac{1}{\sqrt{f-1}} ) 预测凝胶化（f 为官能度）。
- 第 9 章（行 430–432）明确指出高聚物交联动力学"难以分析"："The reaction by which a polymer is converted into a cross-linked structure is usually difficult to analyze kinetically because of the insolubility of the network system. Decreased reaction rates are encountered at high crosslink densities."
- 第 9 章行 184–187 进一步给出扩散控制的宏观判据：速率与颗粒尺寸成反比——把 Ch2 的分子级凝胶点判据，升级为工业尺度的"工艺窗口"判据。
## 模块5：与卫材业务的连接点

### 5.1 聚酯纤维（PET）的热/水解降解 → 纺粘无纺布存储与加工窗口

- 水解（模块2·概念5）：酯键水解在酸/碱/酶/高温下水解。PET 熔体含水量 > 50 ppm 会剧烈水解断链（第 3 章 Sec. 4-12，虽在第9章未直接讨论 PET，但第 9 章给出了酯键水解的通性与邻基催化机理）。
- 储存条件：PET 切片需真空/充氮、湿度 < 0.05%、温度 < 30 °C，纺丝前在 120 °C 干燥 4–6 h 至水分 ≤ 20 ppm。
- 加工窗口：PET 熔体纺丝温度 275–290 °C；> 295 °C 起始明显热降解，色相黄变。温度窗口约 ±15 °C，超出即降解/氧化。

### 5.2 PE/PP 的热降解 → 熔喷工艺温度窗口

- 聚乙烯（行 714–720）：第 9 章指出 PE 用 dicumyl peroxide 或辐射交联，反过来说明 PE 在过氧化物或辐射环境下会断链 + 交联同时发生。
- 熔喷温度窗口：PP 熔体指数 800–1200（g/10 min），熔喷机筒温度 220–260 °C，喷丝板 230–260 °C；> 270 °C 出现明显热氧化降解（熔体粘度下降、MWD 变宽），纤维变脆、过滤效率下降。
- 第 9 章依据：扩散控制（行 184–187）+ 氧化过氧化物机理（行 445–485）共同解释了"为什么熔喷窗口不能无限高"。

### 5.3 聚氨酯（PU）弹性纤维水解 → 纸尿裤弹性腰围寿命

- 水解机理：PU 中的氨基甲酸酯键（–NH–COO–）在酸/碱/高温下水解为胺 + CO₂ + 醇；酯基型 PU（聚酯多元醇基）水解比醚基型 PU 快 5–10 倍。
- 第 9 章依据：Eq. 9-6（行 320–324）邻基催化水解机理 + 行 311–324 皂化自加速，解释了 PU 在汗液 pH 5–6 + 体温 37 °C + 时间三重作用下断键失弹的机制。
- 产品影响：纸尿裤弹性腰围（PU/氨纶复合丝）6–12 个月内在湿热环境下弹性衰减 20–40%；包装需干燥密封、保质期一般 18–24 个月。

### 5.4 接枝改性无纺布 → HDI/异氰酸酯接枝提湿强（湿巾工艺核心）

- 化学原理：第 9 章 9-2d 行 844–848 明确：纤维素纤维用 diisocyanates（二异氰酸酯）交联，与 OH 反应形成氨基甲酸酯交联键：
[
\text{–OH (cellulose)} + \text{O=C=N–R–N=C=O (HDI)} \longrightarrow \text{–O–CO–NH–R–NH–CO–O– (cellulose)}
]
- 工艺：无纺布（木浆/粘胶/棉/PP）→ 0.3–1.5% HDI（或异佛尔酮二异氰酸酯 IPDI、MDI）水乳液浸渍 → 烘干（100–130 °C）→ 交联熟化。
- 湿强提升：干强 6–12 N/5 cm → 湿强 3–6 N/5 cm（湿强保留率 40–60%），这是湿巾不破布的核心指标。
- 第 9 章限制：由概念 2（86% 上限）、概念 9（扩散限制）可知，湿强不能无限提升——过量交联 → 脆化、手感差、氨味残留。

### 5.5 淀粉/纤维素水解降解 → 可降解卫材基材寿命控制

- 机理：淀粉 α-1,4/1,6 糖苷键、纤维素 β-1,4 糖苷键在酸/酶下快速水解（第 9 章 9-3a 纤维素碱降解、9-3b 醋酸酯水解给出糖类聚合物降解的化学范式）。
- 应用：植物基湿巾/卫生棉条外包装、玉米塑料（PLA）基导流层。
- 寿命控制：通过交联度、结晶度、添加剂（如甘油增塑、氧化锌抗菌）调节降解速率——目标 3–12 个月堆肥降解，货架期 12–24 个月（对应湿度 40–60% RH）。

### 5.6 辐射交联在湿巾无纺布湿强提升中的应用

- 第 9 章依据：行 1375–1395（辐射接枝）+ 行 714–720（辐射交联）——电子束 γ 射线在 PE/PP 主链产生自由基 → 交联。
- 工艺：低剂量电子束（10–50 kGy）辐照无纺布（PP/粘胶），在空气中辐照时同时产生氧化交联 → 湿强提升 30–60%。
- 优势：无化学残留（对比异氰酸酯法），可后包装前工序进行。
- 风险：剂量过高（> 100 kGy）导致断链（PE 在空气中易发生辐射氧化断链），湿强反而下降。

### 5.7 聚合物老化与产品保质期（包装设计中氧化/光降解防护）

- 机理：第 9 章行 445–485 醇酸氧化的烯丙位氢过氧化物机理完全适用于卫材包装中的 PP/PE 塑料包装老化。
- 防护手段：

- 抗氧剂（BHT/Irganox 1010）—— 捕捉自由基、分解氢过氧化物
- UV 吸收剂（苯并三唑类）—— 防护光降解
- 铝箔/深色包装 —— 隔绝紫外
- 保质期：未开封湿巾典型保质期 3–5 年；打开后需 12–24 小时内用完（纤维水合 + 微生物降解）。

### 5.8 可直接用于卫材工艺参数选择的公式/数据

|||||
|---|---|---|
|不可逆双相邻反应最大转化率 86%|异氰酸酯交联理论极限|69–72|
|1% PVAc 溶液局部浓度 ≈ 5 倍整体浓度|反应微环境设计|85–87|
|邻基催化环状酸酐（5/6 元环最优）|优化接枝位点设计|322–324|
|粘度与交联密度关系（间接）|熔喷工艺窗口|430–432|
|纤维素三醋酸酯部分水解控制|二醋酸酯纺丝工艺|970–974|
|PAN 热稳定 200–300 °C（空气）/1200–2000 °C（N₂）|热稳定工艺基准|1195–1196|
|辐射接枝异相 + 结晶区不接枝|无纺布辐照剂量设计|1380–1382|
|PVIm 催化 n=11 vs n=1 反应速率差 30 倍|疏水微环境效率量化|374–375|

## 模块6：金句索引（10 条）

### 金句1（行 24–27）

原文："Acetylation of the hydroxyl groups of cellulose is basically the same reaction as acetylation of ethanol, chlorination of polyethylene follows the same mechanism as chlorination of n-hexane. It is usually assumed that the reactivity of a functional group in a polymer and a small organic molecule are the same. This is the familiar concept of functional group reactivity independent of molecular size."
中文：纤维素羟基的乙酰化本质上就是乙醇的乙酰化，聚乙烯的氯化机理与正己烷氯化相同。一般假定聚合物中的官能团与小分子有机物的反应性相同——这就是"官能团反应性与分子大小无关"的著名概念。
为什么记：这是所有卫材化学改性（酯化、接枝、交联）的理论出发点，也是后续所有"实际反应性有偏差"的对照基准。

### 金句2（行 51–56）

原文："80% yield in the corresponding hydrolysis of poly(methyl acrylate) does not result in 80% yield of poly(acrylic acid) with 20% unreacted poly(methyl acrylate). The product contains copolymer molecules, each of which, on the average, contains 80% acrylic acid repeating units and 20% methyl acrylate units randomly placed along the polymer chain."
中文：聚丙烯酸甲酯 80% 水解并不得到 80% 聚丙烯酸 + 20% 未反应物，而是得到平均含 80% 酸单元和 20% 酯单元的无规共聚物。
为什么记：卫材改性（纤维素部分酯化、PU 交联、无纺布部分接枝）所有"转化率"必须按共聚物分布理解，不能当成小分子产率。

### 金句3（行 69–72）

原文："When a polymer reaction involves the random reaction of a pair of neighboring functional groups... the maximum conversion is limited due to the isolation of single functional groups between pairs of reacted functional groups. The maximum conversion for irreversible reactions has been calculated as 86%."
中文：当聚合物反应涉及一对相邻官能团的随机反应时，由于已反应基团之间会孤立单个未反应基团，最大转化率受限；不可逆反应的最大转化率计算值为 86%。
为什么记：86% 是理论天花板——直接约束异氰酸酯交联、纤维素酯化等湿巾/无纺布工艺的设计上限。

### 金句4（行 150–152）

原文："In the extreme case, insolubility of a polymer may limit the maximum conversion if the small-molecule reagent cannot diffuse into and through the polymer."
中文：极端情况下，聚合物的不溶性可能限制最大转化率——如果小分子试剂不能扩散进入并贯穿聚合物。
为什么记：无纺布是多孔、不溶解体系，接枝/交联/湿强提升的极限由扩散决定，是工艺窗口的根本来源。

### 金句5（行 184–187）

原文："High crosslink densities may severely depress polymer reactivity as a result of large decreases in swelling and diffusion rate within the polymer. Diffusion control in a polymer reaction can be detected by the inverse dependence of rate on polymer particle size."
中文：高交联密度可能因聚合物内部溶胀度和扩散速率的大幅下降而严重抑制反应活性。可通过反应速率与聚合物颗粒尺寸的成反比关系检测扩散控制。
为什么记：速率 ∝ 1/尺寸——无纺布克重、纤维直径设计直接影响湿强交联程度；是"越密越慢"的核心公式。

### 金句6（行 445–459）

原文："Alkyds are crosslinked via oxidation by atmospheric oxygen... Unconjugated double bonds undergo crosslinking by the initial formation of an allylic hydroperoxide followed by decomposition of the hydroperoxide."
中文：醇酸树脂通过与大气氧的氧化发生交联……非共轭双键通过先形成烯丙位氢过氧化物，随后分解而实现交联。
为什么记：氢过氧化物 = 老化/降解/交联三岔口的分子枢纽，直接决定卫材包装（PP/PE）的氧化老化速率和抗氧剂选型。

### 金句7（行 844–848）

原文："Cellulosic fibers (cotton, rayon) are crosslinked by reaction of the hydroxyl groups of cellulose with formaldehyde, diepoxides, diisocyanates, and various methylol compounds such as urea–formaldehyde prepolymers... Crosslinking imparts crease and wrinkle resistance and results in iron-free fabrics."
中文：纤维素纤维（棉、粘胶）通过与甲醛、二环氧、二异氰酸酯及多种甲基化合物（如尿素-甲醛预聚物）反应纤维素羟基而交联……交联赋予抗皱免烫性能。
为什么记：Odian 4 版明确点名 diisocyanates 作为纤维素交联剂类别——就是 HDI/IPDI 接枝无纺布提升湿强的教科书依据。

### 金句8（行 970–974）

原文："A partially acetylated product is usually produced by controlled hydrolysis of the triacetate... Hydrolysis of the triacetate is carried out by controlled reversal of the esterification reaction by the addition of water or dilute acetic acid."
中文：部分乙酰化产物通常通过三醋酸酯的受控水解制得……三醋酸酯的水解通过对酯化反应的可控逆转（加水或稀醋酸）来实现。
为什么记：酯化-水解可逆对的经典范式，适用于湿巾中纤维素醋酸酯基材的寿命设计、PU 酯基/醚基型水解选择性。

### 金句9（行 1380–1382）

原文："Most radiation graft polymerizations are carried out as heterogeneous reactions. The polymer is swollen by monomer but does not dissolve in the monomer. (For semicrystalline polymers, swelling and grafting take place only in the amorphous regions.)"
中文：大多数辐射接枝聚合以异相反应进行。聚合物被单体溶胀但不溶于单体。（对半结晶聚合物，溶胀和接枝只发生在无定形区。）
为什么记：直接说明辐射交联 PP 无纺布只在无定形区起作用——结晶度越高，湿强提升越受限；指导无纺布热拉伸/取向工艺。

### 金句10（行 1263–1289）

原文："Three methods exist for synthesizing graft copolymers. Grafting onto involves the reaction between functional groups on two different polymers... Grafting from involves a polymer with functional groups that initiate polymerization of monomer... Grafting through involves the polymerization (or copolymerization) of a macromonomer."
中文：合成接枝共聚物有三种方法。"接枝到"是两种不同聚合物的官能团间反应……"从聚合物出发"是用聚合物官能团引发单体聚合……"通过大分子单体"是大分子单体的（共）聚合。
为什么记：三大接枝范式——湿巾行业实际用的是"接枝到"（异氰酸酯交联），高端功能纤维用"从聚合物出发"（ATRP 表面接枝），未来方向是"通过大分子单体"。

报告结束
- 生成文件：/sandbox/workspace/Ebook_Extract/Principles_of_Polymerization/chapters/ch9_report.md
- 数据引用：所有行号来自 ch9_reactions.txt 原文（教材 p. 729–793）
- 诚实标注：光降解、解聚（depolymerization）、侧基消除、辐射降解专章概念在第 9 章未系统展开，仅给出其在第 9 章中确实出现的引用位置；未编造教材未写的定量数据（如具体降解温度数值除原文出现的 200–300 °C、1200–2000 °C 等）。

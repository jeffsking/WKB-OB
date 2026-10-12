---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_75d9ad9c95613d6912bec176f55d20ac001a693ee6c0644e"
source_file: "Manufactured Fibre Technology · analysis_ch11.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Manufactured_Fibre_Technology/Manufactured Fibre Technology · analysis_ch11.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Manufactured Fibre Technology · analysis_ch11.md.md

# 第11章 《Testing of manufactured fibres》— 深度拆解

## 一、本章核心内容概览（120-200字）

本章由 V.K. Kothari 撰写，系统阐述人造纤维、长丝及其纱线各项关键性能的测试原理与方法。开篇（11.1）指出测试用途涵盖质量控制、工艺控制、产品开发与工艺优化，随后按性能分节：细度 fineness（11.2）、卷曲 crimp（11.3）、拉伸性能 tensile（11.4）、均匀度 evenness（11.5）、摩擦 friction（11.6）、收缩 shrinkage（11.7）与缠结 entanglement（11.8）。各节均从定义、量化指标出发，给出具体标准方法（如 ASTM 系列）与商用仪器（Uster、Dynafil、Toray 等），为纤维性能评价提供统一、可操作的方法学框架。

## 二、本章重要观点（3-6条）

观点1：细度以线密度（linear density）表述，优先采用直接称重法 / 页码：[p.248] / 原文摘选：> "The preferred method for measuring linear density is the direct weighing method." / 解读：因纤维截面非圆、直径测量困难且耗时，细度改用单位长度质量（denier 或 tex）衡量，直接称重最可靠。

观点2：拉伸测试普遍采用恒速拉伸（CRE）原理 / 页码：[p.252] / 原文摘选：> "Most fibre and filament yarn testers employ constant rate of extension (CRE) as the straining principle" / 解读：CRL 受蠕变影响、CRT 精度低，CRE 由载荷-伸长曲线可求出多项拉伸参数，成为主流。

观点3：纱线均匀度测试以电容法最通用，Uster 测试仪为主流 / 页码：[p.257] / 原文摘选：> "Capacitive methods of determining yarn evenness are the most popular and widely used methods." / 解读：纱线连续通过平行板空气电容，介电质量变化正比于单位长度重量，可输出 CV(%)、波谱图与方差-长度曲线。

观点4：静态摩擦恒大于动摩擦，摩擦影响加工行为 / 页码：[p.263] / 原文摘选：> "Static friction is always greater than kinetic friction." / 解读：短纤摩擦影响成纱性能，长丝摩擦决定假捻变形与空气喷射变形中的扭矩传递与丝条迁移。

观点5：测量收缩力比单纯测收缩率更能反映工艺稳定性 / 页码：[p.265] / 原文摘选：> "there must be a means of assessing and controlling shrinkage behaviour of the yarn." / 解读：Toray FTA-500 等可在运转纱线上同步测沸水/干热收缩率与收缩力，利于质控。

## 三、本章研究方法与数据来源（测试标准/方法章，列出各类测试项目）

本章为方法学综述，引用 ASTM 等标准与厂商文献：
- 细度：直接称重法（ASTM D1577­-79 [1]）、振动计法（vibroscope），并附商业回潮率表 Table 11.1（聚酯 0.4%、锦纶 4.5%、粘胶 11.0% 等）。
- 卷曲：波峰计数法（ASTM D3937-­90 [2]）、百分比卷曲法、Lenzing 自动 Vibrotex 仪。
- 拉伸：按原理分 CRE/CRT/CRL（ASTM D76­-90 [3]）；参数含断裂负荷、断裂伸长、强度 tenacity、初始模量、杨氏模量、断裂功、韧性 toughness；设置要素含隔距、横梁速度、满量程负荷、走纸速度（ASTM D2101/D3822/D76 等 [4–6]）。
- 均匀度：切割称重法、电容法（Uster 系列），输出图、CV(%)、波谱图、方差-长度曲线。
- 摩擦：块-纤维垫法、纱-金属/纱-纱张力法（Amonton 定律），仪器含 Rothschild F-Meter、Zweigle 等 [9–11]。
- 收缩：不连续法、连续法；Toray FTA-500、Lawson-Hemphill CTT-DST、Textechno Dynafil、Rothschild DEFT/CCT（ASTM D2102-­90 [12]）。
- 缠结：手动/自动针法、静电法（Obestat）、自动测厚法（Itemat、Toray 轮廓仪）[13–14]。

## 四、本章论证过程

作者采用"定义→量化指标→标准方法→仪器实现"的递进论证。先明确各性能概念（如 crimp frequency、percentage crimp），再以公式给出计算；继而说明为何选某方法（如 CRE 优于 CRL/CRT），最后列举商用仪器佐证可行性。论证以工程实践为导向，依"为何测—测什么—怎么测"展开，逻辑自洽。

## 五、本章在全书中的作用（为纤维性能评价提供方法）

作为全书性能评价的方法支撑章，承上启下：前章述纤维结构与工艺，本章提供量化手段，使第 12 章及后续性能/应用讨论得以用统一指标（tex、tenacity、CV%、摩擦系数等）对比分析，是连接"制造"与"性能判定"的桥梁。

## 六、本章亮点与不足

✅ 亮点：测试项目覆盖面广且紧跟产业（如 Uster 波谱图定位纺丝筒偏心、拉伸辊偏心等周期瑕疵）[p.261]；"振动计法对含卷曲纤维会给出虚假偏高的线密度，须加重张力去除卷曲" [p.250] 提醒实用陷阱。
⚠️ 不足：成书于 1997 年，仪器型号（Uster 3C/IIC、Dynafil 等）已过时，未涉近年光学/在线 AI 检测；部分公式因 OCR 排版错乱（如 dtex 表达式 [p.250]），需对照原书；各法精度与适用范围对比不足。

## 七、本章关键术语与概念

- Linear density 线密度：[p.248] "Fibre and yarn fineness is normally measured in terms of mass per unit length"——单位长度质量，即细度，单位 denier/tex。
- Crimp frequency 卷曲频率：[p.250] "the number of crimps or waves per unit length of extended or straightened fibre"——伸直纤维单位长度内的波数。
- Tenacity 强度：[p.253] "the breaking load per unit linear density of the unstrained specimen"——未应变试样单位线密度的断裂负荷。
- Evenness / CV(%) 均匀度：[p.257] 电容法测单位长度质量变异，以均方根不匀率 CV(%) 表达。
- Static / kinetic friction 静/动摩擦：[p.263] 起始运动阻力为静摩擦，运动中的为动摩擦，静>动。
- Shrinkage 收缩：[p.264] "the decrease in length of a specimen"——无约束受热后长度减少的百分率，负收缩称 stretch。
- Entanglement / opening length 缠结/开口长度：[p.267] 两缠结点间距离，表征缠结纱的临时抱合。
- Amonton's law 阿蒙顿定律：[p.264] T2/T1 = e^(μθ)，由绕摩擦销前后的张力比求摩擦系数。
## 八、本章逻辑结构（缩进文本骨架，不用 Mermaid）

- 11.1 引言：测试目的与待测性能概览

- 11.2 细度 fineness
- 11.2.1 直接称重法
- 11.2.2 振动计法（含短纤束平均线密度）
- 11.3 纤维卷曲 crimp：频率与百分比卷曲
- 11.4 拉伸性能 tensile
- 11.4.1 术语与定义
- 11.4.2 CRE 测试仪（应变片）与设置、高速测试
- 11.5 均匀度测试 evenness
- 11.5.1 图（diagram）
- 11.5.2 波谱图（spectrogram）
- 11.6 摩擦性能 friction
- 11.7 收缩行为 shrinkage
- 11.8 缠结测试 entanglement
- 11.8.1 手动针法
- 11.8.2 自动针法
- 11.8.3 静电法
- 11.8.4 自动测厚法
- 参考文献 [1]–[14]
## 九、本章证据链分析

- 核心论点→支撑证据

- 论点"CRE 为拉伸主流"→证据：CRL 受蠕变、CRT 精度低 [p.252]。
- 论点"电容法测均匀度有效"→证据：介电质量变化正比于单位长度重量，Uster 输出 CV/波谱/方差曲线 [p.257–258]。
- 论点"POY 拉伸力测试最能反映工艺波动"→证据：Stein [13] 比较多种方法，Dynafil 检测聚合/温度/风速变化最有效 [p.267]。
- 证据类型统计表
| 证据类型 | 数量/示例 | 强弱 |
|---|---|---|
| 标准文献（ASTM） | 7 项 | 强（权威） |
| 厂商/仪器说明 | Uster、Dynafil、Toray 等 | 中（商业） |
| 期刊研究 [13][14] | 2 项 | 强 |
| 表格数据（Table 11.1/11.2） | 2 项 | 中 |
- 论证强弱评估：方法描述权威、可操作性强；但多为"陈述+仪器举例"，缺实验数据验证与误差分析，属方法指南而非实证论文，论证偏"规范式"而非"检验式"。


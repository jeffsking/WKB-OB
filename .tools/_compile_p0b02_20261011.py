# -*- coding: utf-8 -*-
"""P0-B02/B03/B04 编译：新建 8 页 + 为已编译页登记同专利副本 source_paths。
RAW 层只读，绝不写入。source_path 一律使用 RAW/ 侧相对路径。"""
import os, io, sys, re, datetime
sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
OUT = 'WIKI/sources'
TODAY = '2026-10-11'

pages = []

# ============ P0-B02 · Areas/IP ============

pages.append(dict(
    fn='US 2007-0203469 A1 熔喷非织造背片（P&G SMMS 背片）.md',
    title='US 2007/0203469 A1 熔喷非织造背片（P&G SMMS 背片）',
    stype='专利',
    cred='中',
    zone='Areas/IP',
    src=['RAW/ima_sync/个人知识库/WKB/Areas/IP/01_模块一：SMMS_US20070203469A1_Disposable_garment_comprising_meltblown_.pdf.md',
         'RAW/ima_sync/个人知识库/WKB/Areas/IP/01_模块一：SMMS_纺粘-熔喷-熔喷-纺粘无纺布_US20070203469A1_Disposable_garment_comprising_meltblown_.pdf.md'],
    pub='2007-08-30',
    subj=['[[SMMS 纺粘-熔喷-熔喷-纺粘无纺布]]', '[[透气背片]]', '[[可弃式服装（P&G 专利族）]]'],
    links=['[[US 7,195,621 B2（P&G 熔喷背片授权本）]]'],
    body='''## 概要

P&G（宝洁）关于**熔喷非织造背片（meltblown nonwoven backsheet）**的美国专利申请公开。核心是**用熔喷细纤维网替代传统聚乙烯薄膜做液不可透背片**，同时解决传统 PE 膜"穿着不适、几乎无透湿与透气性"的痛点。

- 公开号：US 2007/0203469 A1；公开日 2007-08-30
- 申请号：11/716,150；申请日 2007-03-09
- 发明人：Kazuyuki Ohnishi（大阪）、Hiroyuki Ohgata（神户）
- 申请人：The Procter & Gamble Company
- 优先权：US 62/214,617（1999-12-22）、PCT/US99/30624
- 同族：US 7,195,621 B2（授权本）；本申请为 US 10/168,883 的延续案
- 分类号：Int. Cl. A61F 13/15；U.S. Cl. 604/385.23

## 关键参数（权利要求口径）

| 参数 | 数值范围 | 优选 | 测试方法 |
|---|---|---|---|
| 纤维直径 | 3–10 µm | 3–8 µm | — |
| 基重 | 3–60 g/m² | 15–25 g/m² | — |
| 透气率 | ≥15 cm³/cm²/sec | ≥20 | JIS L 1096（Frazier 型） |
| 透湿率 | ≥7000 g/m²/24hr | ≥9000 | JIS L 1099 |
| 最大拉伸强度 | ≥1.0 kgf | ≥1.3 kgf | JIS L 1085（样条 30×5 cm，夹距 20 cm） |
| 韦伯模量 | 230–650 g/mm | 300–550 g/mm | 应力/应变曲线 1%–5% 直线斜率 |
| 平均弯曲力 BFV | 20–80 mg·cm²/cm | <20 | — |
| 静水压阻力 | ≥250 mm H₂O | 400–500 | JIS L 1092 |

## 材料与结构

- 纤维材质：聚烯烃（PP / PE / 乙烯-丙烯共聚物），**优选 PP，PP 占网 >50 wt%**
- 结构：优选单层网；亦可为两层接合结构（折叠单层网形成）
- 可压花：离散结合点/区形式，**压花面积 ≥0.5%，优选 1%–10%**，提升 Martindale 摩擦耐久
- 可油墨印刷：油墨基重 <20 g/m²，优选 0.3–5 g/m²；优选 flexo 印刷；可用 FPOT、P-BEST、XS-787 等油墨

## 与现有认知的关联

- 该专利把**背片透气率（≥20 cm³/cm²/sec）**和**透湿率（≥9000 g/m²/24hr）**同时提为硬性指标，这是 SMMS 取代 PE 薄膜背片在"液不可透 + 可透气"之间做平衡的核心量化门槛。
- 与 [[SUPER ABSORBENT RESIN]] / 吸收芯方案配套：吸收芯可为绒毛浆木浆纤维、coform、化学改性或交联纤维素纤维、tissue、吸收泡沫、SAP 等，可为**非对称改良 T 形**（前腰区矩形）。
- 附图 FIG.1 给出完整可弃式服装构造：容纳组件 22 / 液可透顶片 24 / 液不可透背片 26 / 吸收芯 28 / 侧片 30 / 弹性腰区 34 / 腿箍 32 / 紧固系统 36。

## 识读局限（重要）

- **原件为纯扫描件，无文字层**，共 15 页：扉页 1 页 + 附图 6 张 Sheet（FIG. 1–11）+ 说明书第 1–3 页（段落 [0001]–[0050]）；第 11–15 页为空白。
- **权利要求书不在扫描范围内**。上表参数取自说明书正文与摘要的段落表述，**非权利要求逐条抄录**。
- 本页参数用于技术检索参考，不作为 FTO（自由实施）结论依据。

## 同源副本说明

IMA 内同一套扫描存在 2 份不同命名的副本：

1. `01_模块一：SMMS_US20070203469A1_Disposable_garment_comprising_meltblown_.pdf`
2. `01_模块一：SMMS_纺粘-熔喷-熔喷-纺粘无纺布_US20070203469A1_...pdf`

两件正文自述为同一套扫描（3,532 vs 3,436 字符，差异仅为标题行与识读标注）。**按同一件专利合并为单页，副本不单独建页。**
''',
))

pages.append(dict(
    fn='US 5266394 A SIS 嵌段共聚物热熔胶（Dow 与 Exxon·多线贴合用）.md',
    title='US 5,266,394 A SIS 嵌段共聚物热熔胶（Dow/Exxon，多线贴合用）',
    stype='专利',
    cred='中',
    zone='Areas/IP',
    src=['RAW/ima_sync/个人知识库/WKB/Areas/IP/16_模块三：聚烯烃类热熔胶_US5266394A_Hot_melt_adhesive_compositions_(嵌段共聚物).pdf.md'],
    pub='1993-11-30',
    subj=['[[SIS 嵌段共聚物]]', '[[热熔胶]]', '[[多线贴合（multi-line construction）]]', '[[可弃式服装（P&G 专利族）]]'],
    links=['[[US5266394A Disposable Articles Containing SIS Block Copolymers (Dow)]]'],
    body='''## 概要

Dow Chemical 与 Exxon Chemical Patents 持有的 **SIS（聚苯乙烯-聚异戊二烯-聚苯乙烯）嵌段共聚物热熔胶**专利，专门针对可弃式尿布的 **multi-line construction**（多线贴合结构）工况设计。

- 专利号：US 5,266,394 A；授权日 1993-11-30
- 申请号：925,385；申请日 1992-08-04
- 发明人：Charles F. Diehl、Michael O. Myers、Jean M. Tancrede（Baton Rouge, LA）
- 受让人：The Dow Chemical Company；Exxon Chemical Patents, Inc.
- 同族：为申请号 393,545（1989-08-11，授权为 US 5,143,968）的分案
- 权利要求：**29 项，无附图**

## 为什么用 SIS 而不是 SBS

尿布 multi-line construction 需要热熔胶同时满足 6 个互相冲突的条件：

1. 足够内聚强度承受应力
2. 耐高温混配/涂布而不降解
3. 耐老化氧化
4. **低施胶粘度**（避免热损伤 PE/PP 基材）
5. 对 PE/PP 基材低温下仍有高粘接强度
6. 良好剥离粘附力与初粘

专利核心论点：**SIS 的低温粘接强度显著优于 SBS**，这是选型差异的根因——对比实施例（Demonstrations 10–13）专门拿 Shell SOL T 193 B / Kraton D1107-D1111、Enichem Europrene、Firestone Stereon 840 A 等市售 SBS/SIS 做对照。

## A-B-A 嵌段共聚物参数

| 组分 | 范围 | 优选 |
|---|---|---|
| A（聚苯乙烯嵌段）平均分子量 | 12,000–20,000 | 14,000–19,000 |
| B（聚异戊二烯嵌段）平均分子量 | 30,000–70,000 | 35,000–60,000 |
| 共聚物总平均分子量 | 60,000–110,000 | 70,000–95,000 |
| A 组分含量（份/100 份共聚物） | 27–50 | 35–45 |

结构式（化 1–3）：`B-(AB)ₙ`（n≥2）、`A-(BA)ₙ`（n≥1）、`(AB)ₙ`（n≥2）；优选 A-B-A 三嵌段。

## 热熔胶配方（按热熔胶总重）

| 组分 | 范围 | 优选 |
|---|---|---|
| A-B-A 嵌段共聚物 | 15%–35% | 20%–30% |
| 主增粘树脂（primary tackifying resin） | 45%–70% | 50%–60% |
| 增塑油或二次增粘树脂 | 0%–30% | 5%–20% |
| 稳定剂 | 0.1%–2% | 0.5%–1.5% |

**主增粘树脂九类**：① 天然/改性松香（gum/wood/tall oil rosin、蒸馏、氢化、二聚化、聚合松香）；② 甘油与季戊四醇松香酯；③ 天然萜烯共聚物/三元共聚物（苯乙烯/萜烯、α-甲基苯乙烯类）；含软化点 80–150 °C（ASTM E28-58T）的聚萜烯树脂等。

**增塑油**：油烃低聚物、低分子量聚合物（植物油/动物油及其衍生物，芳香烃含量 <30% 优选 <15%；平均分子量 350–10,000）；优选聚丙烯、氢化聚异戊二烯、氢化聚丁二烯、聚戊烯、哌喃与异戊二烯共聚物。

**稳定剂**：高分子量受阻酚与多官能酚，优选 1,3,5-三甲基-2,4,6-三(3,5-二叔丁基-4-羟基苄基)苯、四(3-(3,5-二叔丁基-4-羟基苯基)丙酸)季戊四醇酯、4,4'-亚甲基双(2,6-二叔丁基苯酚）等。

## 表征测试方法（可复用）

- **苯乙烯含量**：质子 NMR（氘代四氯乙烷/四氯乙烯），Bruker 90 MHz，按 V. D. Mochel, *Rubber Chem. and Tech.*, **40**, 1200 (1967) 计算
- **分子量**：GPC，按 J. R. Runyon et al., *J. Polym. Sci.* **13**, 2359 (1969)
- **熔体流动速率 MFR**：ASTM D-1238-82，条件 "G"（200 °C / 5 kg 重）
- **胶粘剂熔融粘度**：ASTM D-3236，130 °C，Brookfield Thermosel
- **SAFT 剪切粘附失效温度**：PSTC-7；0.5 in × 1 in 样条粘不锈钢板，4.5 lb 滚辊，竖直 32 °C，1 kg 悬挂，10 °F/15 min 升温，记录失效温度

## 示例配方

100 份嵌段共聚物 + 220 phr ECR-149B（Exxon 芳香族改性脂肪族烃增粘树脂）+ 80 phr Tuffico 6056（Lyondell 增塑油）+ 3 phr Irganox 1010（稳定剂），涂于 2 mil Mylar。

## 与 REL 项目的关联点

- 该专利的 6 项冲突需求与用户与 Henkel 讨论的**超低上胶量**方向直接对应：低粘度 + 低温高粘接是减少上胶量的前提。
- SAFT / MFR / 熔融粘度三项测试方法可直接复用于卫材热熔胶来料与配方评价。
- 参见 [[US5266394A Disposable Articles Containing SIS Block Copolymers (Dow)]]（同一专利的另一编译页，正文取自另一份 IMA 副本）。
''',
))

pages.append(dict(
    fn='CN 111134966 A 防漏尿裤型纸尿裤（ω 型腿围橡筋·原件损坏）.md',
    title='CN 111134966 A 防漏尿裤型纸尿裤（ω 型腿围橡筋）',
    stype='专利',
    cred='低',
    zone='Areas/IP',
    src=['RAW/ima_sync/个人知识库/WKB/Areas/IP/18_模块四：氨纶橡筋_弹性纤维_CN111134966A_一种具有防漏尿功能的裤型纸尿裤（ω型腿围橡筋）.pdf.md'],
    pub='2020-05-12',
    status='manual_review',
    subj=['[[氨纶橡筋]]', '[[弹性纤维]]', '[[裤型纸尿裤]]', '[[防漏结构]]'],
    links=[],
    body='''## ⚠️ 本页为 manual_review：原件损坏，仅存书目轮廓

**结论先行：这件专利的技术内容我无法编译，也不应编。** 以下只登记可核实的书目信息与损坏证据。

## 可核实的书目信息

- 公开号：**CN 111134966 A**；公开日：**2020.05.12**
- 名称（取自 IMA 文件名与 source_file）：**一种具有防漏尿功能的裤型纸尿裤（ω 型腿围橡筋）**
- 文献类型：中国发明专利申请公开说明书
- 页数结构（原件页脚自述）：权利要求书 2 页、说明书 6 页、附图 16 页

### 页面树（据可重建页面栈）

| 页 | 内容 |
|---|---|
| p1 | 扉页（二维码/条码、"CN 111134966 A"、"2020.05.12"、页数声明） |
| p2–p3 | 权利要求书（2 页） |
| p4–p9 | 说明书（6 页） |
| p10–p25 | 附图（16 页） |

合计 25 页。

## 原件损坏证据

- 文件共 **1,444,259 字节**，起始正常（`%PDF-1.4`），但**缺少 xref 表、trailer 与 `%%EOF`**，尾部终止于一个未结束的压缩流（对象 215 声明 Length 112,772，实际仅余约 80 KB）。
- **已重新从 IMA 原件通道下载核验**：重新下载的字节数与 MD5 与本地磁盘副本**完全一致**（`b73eb774790a5f09e47464dc95bde4f3`）。→ **损坏发生在源文件侧，不是本地下载中断。**
- 缺失对象：末尾对象号断档（缺 3、34、65 及 216–232），其中包含 **FontDescriptor 221、各 CID 字体的 FontFile2 字体程序、以及正文所用字体的 ToUnicode 映射（obj 225/227/229/230/231/232）**。

## 损坏后果（三重不可读）

1. 正文各段使用 Type0/Identity-H 编码（SimSun、SimHei、MS-Mincho 子集），因缺字体程序与 ToUnicode，**文本层提取仅得乱码 CID**，无法映射为可读文字。
2. 16 页附图的内容对象位于缺失区段，**渲染后仅存页眉页脚，图面内容为空**。
3. 仅页眉/页脚使用带 ToUnicode 的字体子集（CMap 仅定义 14 个码位），可复原出公开号、公开日与页数声明——**这就是本页全部内容的来源**。

申请号、申请人、发明人、摘要、权利要求文字、说明书正文、附图内容：**全部 [无法辨认]**。

## 唯一可用的技术线索

文件名标注的技术方案为 **"ω 型腿围橡筋"**，指向以特定构型（Ω 形）的弹性材料替代传统平铺腿箍的做法。但**这只是文件名信息，未经正文验证，不作为技术结论**。

## 待办（需人工介入）

1. 向 IMA 侧索取未损坏的原文件重新上传，或改从 CNIPA 官方渠道调取 CN 111134966 A 全文。
2. 文件替换后重建 `RAW_FULL` 正文，再将本页 `knowledge_update_status` 从 `manual_review` 改为 `done` 并补全技术正文。
3. 在此之前，本专利**不得**用于 FTO 判断、权利要求规避设计或专利地图标注。

## 关联

- 模块四同批可读专利：[[EP2413866B1 Disposable Wearing Article（弹性部件）]]、[[EP1581159B1 Method for Producing Diaper Pants（含弹性片材）]]、[[EP0820747A1 Absorbent Article with Elastic Feature]]
- 主题入口：[[氨纶橡筋]]、[[弹性纤维]]
''',
))

# ============ P0-B03 · Areas/Supply Base ============

pages.append(dict(
    fn='BLOCLO 盛色科技（广州盛色）光变与温变动态色彩材料产品册.md',
    title='BLOCLO 盛色科技（广州盛色）光变/温变动态色彩材料产品册',
    stype='供应商资料',
    cred='中',
    zone='Areas/Supply Base',
    src=['RAW/ima_sync/个人知识库/WKB/Areas/Supply Base/BLOCLO盛色科技公司及产品介绍.pdf.md'],
    pub='',
    subj=['[[盛色科技（BLOCLO）]]', '[[光变材料]]', '[[温变材料]]', '[[动态色彩]]'],
    links=['[[盛色科技官网关于我们（BLOCLO 温变与光变材料）]]', '[[变色油墨]]'],
    body='''## 概要

广州盛色科技有限公司（**BLOCLO®**）产品册。BLOCLO = **B**looming **C**olor（盛开的色彩），定位功能性"动态色彩"材料制造商——材料本身随光或温度发生可逆颜色变化。

- 专注变色产品研发生产 **15 年**
- 拥有 **40 余项技术专利**，建立 **10 余个产品企业标准**
- 通过 **ISO 三体系认证**：ISO 9001（质量）/ ISO 14001（环境）/ ISO 45001（职业健康安全）
- 已应用行业：智能家电、纺织服装、包装印刷、创意 IP 产品

## 产品体系

| 类别 | 产品形态 | 形态清单 |
|---|---|---|
| 光变 | 光变染料、光变粉、光变色膏、光变纤维 | 4 种 |
| 温变 | 温变粉、温变色膏、温变色母粒 | 3 种 |

## 动态色彩协同开发中心（四大开发方向）

| 方向 | 协同对象 | 盛色提供 |
|---|---|---|
| 工艺技术开发 | 涂层印花、注塑、涂料、印刷美妆 | 标准化变色颜料、应用技术支持、样品/技术/定制/专利/检测支持 |
| 柔性制造开发 | 图层印花、纤维制造、模具注塑、包装印刷 | C2M / C2C 柔性生产、小批量多品种订单支持、标准/专利/技术支持 |
| 外观设计开发 | 纺织服装、智能穿戴、智能家电、创意礼品 | 样品、标准色卡、工艺应用、定制支持 |
| 创新商业开发 | 线上线下创新商业组织与个人 | 爆款新品研发、标准色卡、样品支持 |

## 与卫材变色的关联（历史参考）

- 该公司的**光变纤维**与**温变色母粒**两条产品线，与卫生用品"湿显/温显指示"方向存在技术交集。变色油墨供应商综合技术联系表、变色油墨供应商综合技术联系表（xlsx）中可查其行业位置。
- **光变 ≠ 湿变**：光变由紫外光触发（UV/蓝光激发），湿变需靠水分触发。**不能把 BLOCLO 光变产品当作湿显指示材料**，湿变方向需另找供应商。
- 相关：[[变色油墨]]、[[松井色素（Chromicolor 温变油墨）]]、[[Insilico 功能性微胶囊]]、[[Daehyun Microcapsule Catalogue（DH-Catalogue EN-CN）]]

## 页面状态

- 本页源文件为公司 PDF 产品册，含大量整版形象图与色卡图（`tmp_zip_img/` 路径），**图像内容未做视觉识读**，仅提取文字层。
- 页面源文件另有 `关于我们_盛色科技.html`（官网版），已单独编译为 [[盛色科技官网关于我们（BLOCLO 温变与光变材料）]]，两页 source_path 不同，按库纪律分别登记、互链，不合并。
''',
))

pages.append(dict(
    fn='Insilico 功能性微胶囊产品手册（感温·感光·水致变色·香精·英文版）.md',
    title='Insilico 功能性微胶囊产品手册（英文）',
    stype='供应商资料',
    cred='中',
    zone='Areas/Supply Base',
    src=['RAW/ima_sync/个人知识库/WKB/Areas/Supply Base/Insilico_brochure_eng.pdf.md'],
    pub='',
    subj=['[[Insilico]]', '[[微胶囊]]', '[[感温变色微胶囊]]', '[[感光变色微胶囊]]', '[[水致变色油墨]]'],
    links=['[[Insilico 功能性微胶囊（中文产品册）]]', '[[Daehyun Microcapsule Catalogue（DH-Catalogue EN-CN）]]'],
    body='''## 概要

**Insilico**（Insilicotech Co., Ltd.，韩国）公司手册（英文版）。定位为**化学 + IT 融合**的新材料公司，用分子模拟/计算机手段做配方与材料开发。

- 公司标识：**C**（Carbon 碳）的艺术化写法，象征分子对接（docking）
- 2002 年成立（Insilicotech Co. Ltd.）
- 业务板块：Formulation / AI / Bioinformatics / Atomistic / Quantum 优化 / Scale-up / Product Discovery，贯通基础研究→应用研究→产品

## 公司资质与里程碑（部分）

- 2002：Insilicotech 成立
- ISO 9001:2008 认证；ISO 14001:2004 认证
- 韩国 Venture Company 认证；INNO-BIZ（创新企业）认证，2016-02-22 至 2019-02-22
- 收购 Polychrom Co. Ltd. 为子公司
- 韩国国家世界级产品奖（MOTIE）；青龙奖 100 万 / 300 万韩元
- 迁至 Ansan  Banwol Industrial Complex 智能办公室
- 与 **Dassault Systèmes Consulting** 有合作关系（合作板块 FUCTIONAL MICROCAPSULE → WATER REPELLENT AGENT → BIOLOGICS）

## 功能微胶囊产品线（板块结构）

| 板块 | 定位 |
|---|---|
| FUCTIONAL MICROCAPSULE | 功能微胶囊主业 |
| WATER REPELLENT AGENT | 拒水剂 |
| BIOLOGICS | 生物材料 |

## 与卫材变色的关联（历史参考）

- Insilico 的**感温变色微胶囊（Chameleon T Series）**和**感光变色微胶囊（Chameleon UVC Series）**是微胶囊路线变色材料的主要供应商之一，**与盛色科技（粉体/膏体/母粒路线）构成不同技术路线**：
  - Insilico：微胶囊包覆感温色素，稳定性和耐久性更好，但成本通常更高
  - BLOCLO 盛色：粉/膏/母粒，成本低、适合大面材与纤维，耐久性需实测
- **水致变色（Hydrochromic Ink）**与尿显/湿显方向直接相关，见中文册 [[Insilico 功能性微胶囊（中文产品册）]]。
- 相关：[[变色油墨]]、[[Daehyun Microcapsule Catalogue（DH-Catalogue EN-CN）]]、[[德福伦高感性聚酯纤维简介]]

## 页面状态

- 本页为**英文公司手册**，产品型号/技术参数集中在另两份独立文件中：
  - 中文册：`RAW/.../Supply Base/microcapsule_brochure_2019_chn.pdf` → 已编译为 [[Insilico 功能性微胶囊（中文产品册）]]
  - DH 目录：`DH-Catalogue-EN-CN.pdf` → 已编译为 [[Daehyun Microcapsule Catalogue（DH-Catalogue EN-CN）]]
- 源文件含大量整版形象图与嵌图（`tmp_zip_img/`），**图像内容未做视觉识读**，仅提取文字层；历史时间线部分因图片承载文字，提取不完整。
''',
))

pages.append(dict(
    fn='Insilico 功能性微胶囊（中文产品册·2019）.md',
    title='Insilico 功能性微胶囊（中文产品册·2019）',
    stype='供应商资料',
    cred='中',
    zone='Areas/Supply Base',
    src=['RAW/ima_sync/个人知识库/WKB/Areas/Supply Base/microcapsule_brochure_2019_chn.pdf.md'],
    pub='2019',
    subj=['[[Insilico]]', '[[微胶囊]]', '[[感温变色微胶囊]]', '[[感光变色微胶囊]]', '[[水致变色油墨]]', '[[芳香微胶囊]]'],
    links=['[[Insilico 功能性微胶囊（英文公司手册）]]', '[[变色油墨]]'],
    body='''## 概要

Insilico **功能性微胶囊中文产品册（2019）**，是技术参数与产品系列最完整的一份材料。定位语："以优异的技术和质量为基础，专门制造特殊功能性新型材料。"

## 产品系列总目录（按变色机理）

### 感温变色微胶囊

| 系列 | 页 | 名称 |
|---|---|---|
| Chameleon T Series | 6 | 感温变色微胶囊 |
| Bichrom T Series | 9 | — |
| SpyBall | 11 | — |
| Reverse Thermochromic Series | 14 | 反向温变 |

### 感光变色微胶囊

| 系列 | 页 | 名称 |
|---|---|---|
| Chameleon UVC Series | 16 | — |
| Bichrom P Series | 18 | — |
| Polyshine Series | 19 | — |

### 其他功能性微胶囊

| 系列 | 页 | 名称 |
|---|---|---|
| Hydrochromic Ink | 20 | 水致变色油墨 |
| AromaBall | 24 | 香味微胶囊 |
| BioBall | 26 | — |
| ThermoBall | 27 | — |

## Chameleon T Series（感温变色微胶囊）关键参数

### 机理

感温微胶囊**包覆感温色素**。感温色素本身随温度改变颜色，但因对外界环境非常敏感，故用**微胶囊包覆技术加强温变的稳定性和耐久性**。加热时内部物质结构改变而失色，冷却时结构恢复而回色——**可逆**。

- **变色温度范围：0 ~ 70 °C**（可通过配方调控）
- 颜色种类多，变色温度范围可调控 → 可制造各种温度/颜色组合

### 形态

- **粉状（油性）Chameleon T P-Series**
- **悬浊液（水性）Chameleon T S-Series**

### 颜色清单（按色系分组）

| 组 | 颜色 |
|---|---|
| 绿/蓝 | Green、DarkBlue、FastBlue、SkyBlue、TurquoiseBlue |
| 紫/品红 | RealViolet、BlueViolet、Magenta |
| 红/橙 | RoseRed、Vermilion |
| 棕/黑 | Brown、Black |

### 性能

- **耐洗牢度 4~5 级**（韩国纤维技术研究所 Yoon Seok-Yoo 研究所检验）

### 应用领域

**纤维加工、涂料、塑料射出、生活用品、油墨**

> 卫材相关性：纤维加工 + 油墨两个方向直接对应无纺布印花与湿显/温显油墨。

## 与卫材变色的关联（历史参考）

- **Hydrochromic Ink（水致变色油墨）** 是与尿显/湿显最接近的机理：靠水分而非温度触发。变色油墨供应商联系表、变色油墨供应商综合技术联系表、温变湿变微胶囊技术参数对比表（xlsx）中可查行业横向对比。
- 与 [[松井色素（Chromicolor 温变油墨）]] 路线对比：松井是**粉末/油墨级 Chromicolor** 体系，Insilico 是**微胶囊包覆**体系，稳定性/耐久性/成本三层需按项目实测比选。
- 参见 [[Insilico 功能性微胶囊（英文公司手册）]]、[[Daehyun Microcapsule Catalogue（DH-Catalogue EN-CN）]]。

## 页面状态

- 源文件色卡图以整版图承载（`tmp_zip_img/`），**图像内容未做视觉识读**；颜色名称取自文字层。
- 检验报告部分原文含韩文与表格混排，提取为文本层，可能有排版错位。
''',
))

pages.append(dict(
    fn='松井色素 Chromicolor 温变油墨产品册（11 色 × 9 温度类型）.md',
    title='松井色素 Chromicolor 温变油墨产品册（11 色 × 9 温度类型）',
    stype='供应商资料',
    cred='中',
    zone='Areas/Supply Base',
    src=['RAW/ima_sync/个人知识库/WKB/Areas/Supply Base/Matsui 松井☆クロミ総合POP英語20260703.pdf.md'],
    pub='',
    subj=['[[松井色素（Chromicolor 温变油墨）]]', '[[温变油墨]]', '[[温变材料]]'],
    links=['[[会议纪要：松井油墨（水变温变油墨技术分享）]]', '[[水变油墨尿显暨松井技术交流纪要 2026-08-14]]'],
    body='''## 概要

**株式会社松井色素化学工業所**（Matsui Pigment）**Chromicolor** 温变油墨产品册（英文版，2026-07-03）。Chromicolor 是**可逆温变颜料（thermochromic pigment）**，随温度变化可逆变色。

## 三种产品形态

| 产品 | 形态 | 要点 |
|---|---|---|
| **Chromicolor AQ Ink LF Grade** | 高浓度水性浆料 | **甲醛含量 <0.06%**，可称 Low-Formaldehyde |
| **Chromicolor MS Powder LF Grade** | 粉体 | 粒径数微米；按目标**分散到溶剂型透明油墨**中 |
| **Chromicolor PP/PE Conc. BW Grade** | 母粒 | Chromicolor 高浓度复配于 **PP 或 PE 树脂** |

> 卫材相关性：PP/PE Conc. BW Grade 是**直接面向 PP/PE 纤维与薄膜母粒级**的形态，是与盛色科技温变色母粒（BLOCLO 路线）同一竞争位的产品。母粒形态免去现场分散，对大批量涂布/纺丝更友好。

## 色板与温度类型

- **基础色：11 种** — Fast Yellow、Magenta、Green、Gold Orange、Fast Blue、Fast Black、Vermilion、Turquoise Blue、Brown、Pink、Brilliant Green
- **温度类型：9 种（#5 ~ #85）**
- **混色能力**：11 基础色可预混实现 "Color to Another Color"（一色变另一色）效果 → **11 × 11 = 121 种颜色组合**

### 温度类型表（节选，-5 °C / 20 °C / 45 °C 三档行为）

| 编号 | -5 °C | 20 °C | 45 °C |
|---|---|---|---|
| #5 | Coloring（着色） | Coloring | Decolorization（褪色） |
| #10 | Coloring | Coloring | Decolorization |
| #15 | Coloring | Coloring | Decolorization |
| #45 | Decolorization | Decolorization | Coloring |
| #55 | Decolorization | Coloring | Coloring |
| #65 | Decolorization | Coloring | Coloring |
| #75 | Decolorization | Coloring | Coloring |
| #85 | Decolorization | Coloring | Coloring |

> **关键区分**：#5/#10/#15 是**升温褪色型**（低温深色，升温变浅）；#45~#85 是**升温着色型**（低温浅色，升温显色）。选型时**必须先确定目标触发方向**，否则会做出"该显色时反而褪色"的产品。

## 与卫材变色的关联（历史参考）

- **Chromicolor 是温变（热触发），不是湿变（水触发）**。与水变油墨尿显方向需分开对待。参见 [[水变油墨尿显暨松井技术交流纪要 2026-08-14]]、[[会议纪要：松井油墨（水变温变油墨技术分享）]]。
- **9 种温度类型中 #45~#55 是尿湿区附近最可能的工作区间**（人体接触温度 30~40 °C），但湿显仍需水触发机理，两者不可混。
- 与 Insilico Chameleon T（变色温区 0~70 °C）同属温变路线但形态不同：松井为油墨/粉/母粒，Insilico 为微胶囊。
- 与 [[盛色科技（广州盛色）光变/温变动态色彩材料产品册]] 同属温变赛道。

## 页面状态

- 色板图与温度类型图以整版图承载（`tmp_zip_img/`），**图像未做视觉识读**；颜色名与温度表文字取自文字层。
- 温度类型表原文仅列 8 行（#5/#10/#15/#45/#55/#65/#75/#85），第 9 种类型在源图内，未取到文字。
''',
))

# ============ P0-B04 · Areas/Test Method ============

pages.append(dict(
    fn='JMP 16 软件操作流程（Mannequin 测试数据分析 WI-JMP 第0版）.md',
    title='JMP 16 软件操作流程（Mannequin 测试数据分析 WI-JMP 第0版）',
    stype='内部作业指导书',
    cred='中',
    zone='Areas/Test Method/成品/TJ',
    src=['RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/JMP软件操作流程.docx.md'],
    pub='2024-02-26',
    subj=['[[JMP 统计分析软件]]', '[[Mannequin 测试]]', '[[测试数据分析]]'],
    links=['[[拉力松紧可视化技术评估报告]]'],
    body='''## 概要

实验室内部作业指导书 **WI-JMP《JMP 软件操做流程》**（原文标题"操做"为文档原有错别字，本页标题沿用规范写法并保留原义）。

- 文件编号：WI-JMP
- 版本：**第 0 版**
- 修订日期：**2024 年 2 月 26 日**
- 实验目的：**分析 Mannequin（人体模型）的测试数据**

## 操作步骤

1. 打开 **JMP 16**
2. 把 Mannequin 导出的 **Excel 数据**拖放到 JMP 主窗口左侧
3. 在 JMP 主窗口**双击**打开刚刚拖放的 Excel 文件

## 数据结构（源文件记录的分析字段）

Mannequin 导出的 Excel 表含约 17 个字段，构成 JMP 分析的数据列：

| 字段 | 含义 |
|---|---|
| Study Number | 研究编号 |
| Code | 样品编码 |
| Gender | 性别 |
| Position | 位置 |
| Run | 轮次 |
| Mannequin | 模型标识 |
| Leaked | 是否泄漏 |
| Order | 顺序 |
| Time | 时间 |
| Leak Area | 泄漏面积 |

## 关联

- 成品测试主线：[[拉力松紧可视化技术评估报告]]（同属成品/TJ 目录）
- JMP 是本库统计口径的主要工具，凡涉及成对比较、多因子与图形化诊断的测试数据应优先走 JMP 而非手工透视表。

## 页面状态

- 本文档为**第 0 版**，仅含3 个主步骤，**未覆盖**数据清理、假设检验、图表模板化、报告导出等后续环节。
- 源文件含截图（`[图片: JMP 16]`、`[图片: JMP主窗口-...xshujv.xlsx]`），**图像内容未做视觉识读**，实际界面细节以本地软件为准。
- 建议在下一版补齐：列类型指定（测量/标识）、缺失值处理、分组比较的报表模板。
''',
))

# ============ 写出 ============
def fm(p):
    L = ['---', 'type: source']
    L.append(f'title: "{p["title"]}"')
    L.append(f'source_type: {p["stype"]}')
    L.append(f'source_path: {p["src"][0]}')
    if len(p['src']) > 1:
        L.append('source_paths:')
        for s in p['src']:
            L.append(f'  - {s}')
    L.append(f'source_credibility: {p["cred"]}')
    L.append(f'knowledge_area: {p["zone"]}')
    L.append('subjects:')
    for s in p['subj']:
        L.append(f'  - {s}')
    if p['links']:
        L.append('related:')
        for s in p['links']:
            L.append(f'  - {s}')
    if p['pub']:
        L.append(f'date_published: {p["pub"]}')
    else:
        L.append('date_published: ""')
        L.append('  # 口径：源文件未记载发布日期，留空。RAW_FULL 的 extracted 字段是正文回填日期，不是发布日期')
    L.append(f'knowledge_update_status: {p.get("status","done")}')
    L.append(f'compiled_at: {TODAY}')
    L.append('compile_batch: P0-B02/B03/B04')
    L.append('---')
    return L

ok = 0
for p in pages:
    path = os.path.join(OUT, p['fn'])
    if os.path.exists(path):
        print('SKIP (已存在):', p['fn']); continue
    body = '\n'.join(fm(p)) + '\n\n' + p['body']
    io.open(path, 'w', encoding='utf-8', newline='\n').write(body)
    print('NEW:', p['fn'])
    ok += 1
print('\n新建页数:', ok)
---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_86427706fe68eabb9183f71f0b8d8733001a693ee6c0644e"
source_file: "84-Sleeve工程规格与换装防错设计.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/84-Sleeve工程规格与换装防错设计.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# 84-Sleeve工程规格与换装防错设计.md.md

# 84 · Sleeve 工程规格与换装防错设计

补库来源：One_Drum_Two_Ups_11_Sizes_1000ppm.pptx P4/P8/P9/P15/P16/P18
对应 Gap：G14（Sleeve 作为「尺寸载体」的工程规格与防错设计缺失）｜严重程度 高｜属 P0 批次
主表改善建议：补充①承载体接口与换装工时 ②sleeve ID tag + PLC 联锁防错规格 ③skin/poly 成对设计规则 ④land 高度体系 ⑤屏规格与 ups 无关性 ⑥验收项与磨损点检 ⑦IP 与保密归口
创建日期：2026-09-22

## 1. Sleeve 的定位

源文件 P8 副标题（原文）：*"Everything that defines phase is on the drum body; everything that defines size is on the sleeve."*

Sleeve 是本架构中唯一的尺寸载体：鼓体（含扇区、电机、编码器、压合间隙、对中）在 11 个尺寸间完全不变，尺寸全部由 sleeve 表达。

||||
|---|---|---|
|Body|相位与机械几何|永不动（见 83 §2.1）|
|Sleeve|尺寸（MD pattern 布局 + 端区 + 通道位置）|每次换 2 片|

推论：sleeve 的工程规格质量 = 整线多规格能力的上限。sleeve 一旦有缺陷（节距不等、land 高错、通道不成对），鼓体再精密也无法补偿。

## 2. 22 片架构

||||
|---|---|---|
|总数|22 片 = 11 尺寸 × 2 侧（skin / poly）|源文件 P9；B|
|每 size 的成对关系|skin 侧 1 片 + poly 侧 1 片，必须成对设计与制造|源文件 P9（§7）|
|每次换型更换|2 片（skin 1 + poly 1），两鼓并行更换|源文件 P18；B|
|存储|需 carrier racks（承放架） 22 位|源文件 P18 top risk #5；B|

⚠️ 22 片的规模含义：22 片要存储、点检、维护。源文件 P18 明确把「22 sleeves to store and maintain」列为 top risk #5，对策是「carrier racks, wear check of land faces per campaign」。这是本架构主要的运维负担来源，需在 RFQ 中作为独立条目列出（§10）。

## 3. Land 高度体系

### 3.1 定义

Sleeve 为 pocket-and-land 浮雕结构：

||||
|---|---|---|
|Pocket（凹坑）|SAP 沉积区，对应 pattern；屏开孔只在此区|✓|
|Land（凸台）|所有需要「无 SAP + 可与对侧粘合」的区域|✗|
|端区（30–116 mm）|也是 land —— 保证相邻两芯之间无 SAP|✗|

源文件 P9（原文）：*"Raised lands = channels + end zones — 0.45 mm high; 30–116 mm end zones are lands too, so no SAP between cores"*

### 3.2 Land 高与床高的匹配规则

核心规则（源文件 P15 原文）：*"Skin and poly SAP gsm can differ (e.g., 230 skin / 160 poly); give each sleeve the land height of its own bed so the nip still meets land-to-land."*

床高 → land 高映射（源文件 P16）：

||||
|---|---|---|
|160 gsm|0.31 mm|≈ 0.31 mm + 余量|
|230 gsm|0.44 mm|0.45 mm（= 源文件 P9 标称值）|

设计判据：land 高 ≥ 该 sleeve 自身床高，使对压时先由 land 接触（land-to-land），SAP 床不被过压。

### 3.3 ⚠️ 两处须澄清的口径问题（本次发现）

(a) 「0.45 mm」是全局常量还是 230 gsm 工况值？
- 源文件 P9 给单一值 0.45 mm；
- 源文件 P15 要求逐 sleeve 按自身床高取 land 高（160 gsm 侧应 ≈0.31 mm）；
- 源文件 P16 给床高 0.44 mm @230 gsm —— 与 0.45 吻合。
- 判定：0.45 mm 是 230 gsm 工况下的标称值；低 gsm 的 sleeve 的 land 高必须按自身床高取。因此sleeve 图纸上的 land 高是逐片变量，不是全局常量。
- 须澄清：源文件未给出 160 gsm sleeve 的 land 高取值，也未说明两鼓 land 高不同时压合间隙 0.15–0.18 mm 如何定义（是两侧 land 高之和？还是限位块间隙？）。此项直接决定压合能否 land-to-land 成立，须向设备商索取限位结构图后澄清。

(b) 床高与松密度规格不自洽。
- 由床高反推体积密度：ρ = gsm / 床高 → 160 gsm / 0.31 mm = 0.516 g/cm³；230 gsm / 0.44 mm = 0.523 g/cm³（两者一致 → 源文件内部自洽 ✓）；
- 但源文件 P16 的 SAP 规格是 松密度 0.62–0.70 g/cm³。
- 用 0.62–0.70 计算床高应为：160 gsm → 0.229–0.258 mm；230 gsm → 0.329–0.371 mm。
- 差距约 20–35%，方向为「实际床高会比按松密度预测的更厚」。
- 可能原因（未验证）：床高口径含颗粒间自由空隙的「自由堆积」状态、或含 land 浮雕的基准差异、或松密度规格与床高由不同假设独立得出。
- 影响：land 高是按床高设定的 → 若 SAP 实际松密度真的落在 0.62–0.70，则床会比设计更薄，land 相对偏高（对压时仍能 land-to-land 接触，但压实余量变大，可能导致 SAP 压实不足/通道粘接受影响）。须用实测床高（含铺放后未压实状态）替代计算值。
- 等级：本次发现的对账缺口，须用 [STM-00305 SAM分布.docx] / [STM-4597纸尿裤SAM分布测试.docx] 方法实测。

### 3.4 Land 边缘与表面

||||
|---|---|---|
|Land 边缘圆角|R ≤ 0.2 mm|源文件 P9（向 Nichidai 的索取项）；B|
|Land 表面|耐磨面（wear-resistant land faces）|源文件 P9；B|
|理由|边缘过锐会划伤包覆无纺布并在高速下产生应力集中；land 面承受反复压合与清机磨损|推断|

## 4. 屏（Perforated Screen）规格

||||
|---|---|---|
|孔径|Ø0.6–0.8 mm|源文件 P9；B|
|开孔率|30–40% open|源文件 P9；B|
|一致性要求|「same on every sleeve」—— 全部 22 片的屏规格必须一致|源文件 P9；B|
|与 ups 的关系|与 ups 无关（屏是 sleeve 的一部分，不受 n 影响）|源文件 P4/P9；B|

为什么「各 sleeve 一致」是硬要求：屏规格决定穿透风速与压损。若各 sleeve 屏开孔率不同，则同一个 recipe 的成型真空/风量在不同 sleeve 上产生不同的沉积行为 → 换型后工艺窗口漂移，且无法用单一 recipe 覆盖 11 尺寸。这是「一鼓多规格 + 单 recipe 体系」能否成立的前提。

### 4.1 ⚠️ 与既有 WKB Nichidai 知识的口径差异（须并列呈现）

||||||
|---|---|---|---|---|
|源文件 P9（本方案）|未注明|Ø0.6–0.8 mm|30–40%|未注明|
|WKB [日本Nichdai 丝网工艺技术交流]|六边形孔|≥1.4 mm（下限）|60 / 70 / 80%|0.1 mm 层积蚀刻，有锥度方向|

差异显著：孔径差约 2×，开孔率差约 2×。可能原因（未验证）：
- 两者面向的成型机制不同：Nichidai 的丝网为传统整幅成型（大孔高开孔率以通过纤维/浆料），本方案的屏为 pattern-SAP 沉积（小孔以在 land 边缘形成锐利边界、抑制 stray SAP）。
- 源文件 P9 的屏规格是目标规格（B 级）；Nichidai 是其既有成熟产品口径（C 级，厂商标称）。

处理要求：两条口径必须并列记录，禁止静默取其一。 向 Nichidai 询价时须明确说明「本方案用于 pattern-SAP 干法沉积，非浆料成型」，并索取其 pattern 沉积类屏的既有规格。

### 4.2 Nichidai 的历史事故教训（必须继承）

||||
|---|---|---|
|锥度装反 → SAP 堵塞|丝网锥度方向装反会导致 SAP 堵塞（已发生的历史事故）|WKB [日本Nichdai 丝网工艺技术交流]|
|快换方式|卡簧式快换，供应商目标 30 s 换网（经验待确认）|同上|
|IP 归口|孔径分布为 KC 专有技术，须保密并申请 IP|同上|

推论：锥度方向是不可逆向的装配依赖 → 必须在 §7 的 ID 防错体系中一并编码（不仅防错 ups，还须防错装反方向）。

## 5. Pattern 公差体系

|||||
|---|---|---|---|
|Sleeve pattern 制造公差|±0.02 mm over 2,771 mm，全部 n 个节距|22 片中任一片的 n 个节距必须等距，任一节距偏差不超过 ±0.02 mm|源文件 P8；B|
|引脚相位（→编码器零点）|±0.02 mm|装好后 pattern 相对编码器零点的相位准确度|源文件 P8；B|
|换型后引脚给出的相位|±0.05 mm|整机换型后引脚能保证的实际相位|源文件 P18；B|
|Sleeve 间索引重复性|±0.02 mm|22 片互换后索引位置的一致性（向 Nichidai 索取）|源文件 P9；B|

### 5.1 ⚠️ 相位精度两处口径不一致（本次发现）

||||
|---|---|---|
|源文件 P8|±0.02 mm|「Pinned to encoder zero ±0.02 mm, taper-locked」——规格值|
|源文件 P18|±0.05 mm|「Pins give ±0.05 mm」——换型实操值|

判定：两者不是同一件事，但在源文件中未区分：±0.02 mm 是制造+装配规格；±0.05 mm 是换型后整机实际相位分散（含更换动作引入的重复性、锥面锁紧差异、温度等）。差 2.5 倍，是 85 公差链的关键输入，必须澄清后才能做套准公差链闭合。等级：B（须澄清）。

### 5.2 「等节距 = 同一相位适配全部」的机理

源文件 P8 注释（原文）："Equal pitches = one phase fits all"

- 若某 sleeve 的 n 个节距不等，则无法用单一相位偏置把全部 n 个 pattern 对齐到对侧鼓 → 必须逐 pattern 修正（本架构的视觉闭环只能整体 trim，不能逐 pattern 修）。
- 因此 ±0.02 mm 等距要求是多规格共鼓 + 单视觉闭环的结构前提，不是「精度越高越好」的泛化要求。
## 6. 承载体（Carrier）与换装接口

||||
|---|---|---|
|定位|pin（销）+ 锥面（taper）锁紧|源文件 P8/P9；B|
|相位基准|pinned to encoder zero（销定位到编码器零点）|源文件 P8；B|
|换装工时|≤15 min / 鼓；两鼓并行 → 目标 ≤15 min|源文件 P9/P18；B|
|换型免对相|「Grade change without re-registration」——换型不需要重新对相|源文件 P8；B|
|与既有知识的差异|WKB Nichidai 记录卡簧式快换、目标 30 s 换网|WKB；C|

⚠️ 须澄清的 30 倍分歧：≤15 min/鼓（源文件）vs 30 s/网（Nichidai 目标）。差异可能来自（a）换装对象不同（整片 sleeve 含承载体 vs 仅丝网）、（b）是否含对相与验证、（c）供应商口径为纯动作时间。引用时必须并列，不得择一。 详见 83 §6。

## 7. Sleeve ID tag + PLC 联锁防错（本架构的关键安全设计）

### 7.1 规格

||||
|---|---|---|
|载具|每片 sleeve 带 ID tag|源文件 P9；B|
|读取方|由 PLC 读取|源文件 P9；B|
|防错动作|阻止（block）错误 ups 的 recipe 被载入 —— interlock on start|源文件 P9/P18；B|
|与 recipe 的关系|Recipe 载入流程的第一步就是 sleeve ID 校验|源文件 P12/P18；B|

### 7.2 防错覆盖范围（须覆盖的失效模式）

|||||
|---|---|---|---|
|1|装错 ups（本应 6-up 装了 7-up 的 sleeve）|✅ 核心功能|源文件 P18 top risk #2|
|2|skin / poly 装反|✅ 需 ID 编码侧别|源文件未明确，须补（推断）|
|3|丝网锥度装反（Nichidai 历史事故）|✅ 需 ID 编码方向|WKB Nichidai 事故教训，须补（推断）|
|4|装错尺寸（同 ups 组内混淆，如 Open M ↔ Pant L）|⚠️ 取决于 ID 粒度|两者均为 7-up，须确认 ID 是否区分到尺寸，否则同 ups 组的尺寸混淆无法被防住（推断，须澄清）|
|5|22 片存储中拿错|✅（读取即报错）|需 §9 的存储管理配合|
|6|ID tag 失效/未读到|✅ 应 fail-safe（拒绝启动）|须在规格中显式要求（推断）|

⚠️ 本架构的隐含短板（本次发现）：源文件只说明「阻止错误 ups 的 recipe」，但同一 ups 组内有多个尺寸（7-up 组含 Open NB/S/M + Pant L/XL/XXL/XXXL 共 7 个尺寸）。若 ID 只区分 ups，则组内尺寸错装不会被拦截，而组内尺寸错装的后果与 ups 错装同级（pattern 长度错 → 端区错 → 套准与切断全部失配）。
要求：ID tag 必须逐片唯一（22 个唯一 ID），并编码 尺寸 + 侧别(skin/poly) + 版本，而非仅 ups。此项须写入 RFQ。

## 8. Skin / poly 成对设计规则

源文件 P9（原文）：*"Skin/poly pairing rule: patterns may differ, but every channel meant to bond must exist on both sleeves at the same position. Design the pair as one CAD file and fabricate both from it."*

### 8.1 规则

||||
|---|---|---|
|R1|凡需粘合的通道，必须在对侧 sleeve 的同位置存在|压合时由两侧 land 互为支撑才能形成通道粘接；单侧有 land 只能形成半通道|
|R2|同一 CAD 文件设计一对，并由该文件同时制造两片|消除两片之间由独立建模/独立加工引入的相对偏差|
|R3|pattern 本身可以不同（skin ≠ poly）|允许 (a) skin/poly gsm 不同（如 230/160）、(b) 两侧功能分工不同（如吸收分布错峰，见 references/74-COCO-v6项目技术档案.md SAP 分区策略）|
|R4|通道位置是成对的定义域；SAP 布局是各自的自由度|「通道」与「SAP pattern」在本架构中是两个概念，不要混为一谈|

### 8.2 与套准的关系

通道成对性 + |MD| ≤1.0 / |CD| ≤0.5 mm 套准规格（见 85）共同保证 ≥90% 通道粘接面积：

通道粘接成立 ⇔ (a) 两侧通道同位置存在（本规则） ∧ (b) 两侧相位偏差在公差内（85）

若 (a) 不成立，则无论套准多好都无法粘合 —— 这是 R2「同一 CAD」的不可替代性。

## 9. 验收项清单与磨损管理

### 9.1 到货 / 加工验收项（源文件 P9「Ask Nichidai for」+ P8）

|||||
|---|---|---|---|
|A1|Sleeve 间索引重复性|±0.02 mm|三坐标 / 专用检具；22 片逐一比对|
|A2|Pattern 节距等距性|±0.02 mm over 2,771 mm，全部 n 个节距|三坐标逐节距测量|
|A3|Land 边缘圆角|R ≤ 0.2 mm|轮廓仪 / 光学|
|A4|Land 面耐磨处理|耐磨面（工艺待定）|材质证明 + 表面硬度|
|A5|屏规格|Ø0.6–0.8 mm、30–40% 开孔，22 片一致|光学计数 / 压损法|
|A6|Sleeve ID tag|逐片唯一，编码 尺寸+侧别+版本；PLC 可读；未读到须拒绝启动|装配合格测试|
|A7|承载体配合|pin + 锥面锁紧；相位对编码器零点|装配合格测试|
|A8|锥度方向/装配方向防错|不可逆向装配|装配试验（防呆验证）|
|A9|land 高（逐片）|按该 sleeve 自身床高（见 §3.2）|三坐标 / 塞规（须先澄清 §3.3(a)）|
|A10|动平衡|G1.0，逐 sleeve 组复检|动平衡机（源文件 P8）|

### 9.2 磨损管理

||||
|---|---|---|
|点检周期|每个 campaign（生产周期）后点检 land 面磨损|源文件 P18 top risk #5；B|
|关注面|land 面（承受反复压合）、端区 land（切断区）、边缘|推断|
|存储|carrier racks（承放架），避免碰撞与变形|源文件 P18；B|
|更换判据|未定义（源文件未给出 land 磨损限值）→ 见 §11|—|

### 9.3 IP 与保密归口

||||
|---|---|---|
|孔径分布/pattern 细节|KC 专有技术，须保密并申请 IP|WKB [日本Nichdai 丝网工艺技术交流]|
|归口动作|供应商签 NDA；图纸受控发放；pattern 数据不出 KC|推断（依据上述 WKB 记录）|
|与 source 文件的呼应|源文件 P9 提到 ID tag「由 PLC 读取」——ID 编码本身也不宜外泄完整映射关系|推断|

## 10. RFQ 询价项（可直接发给 sleeve 供应商）

发给 Nichidai（或同类 sleeve 供应商）的询价条目：

- 22 片 sleeve 套件（11 尺寸 × skin/poly），pocket-and-land 浮雕，端区亦为 land。
- 索引重复性 ≤ ±0.02 mm（片间互换）。
- pattern 节距等距性 ≤ ±0.02 mm over 2,771 mm（全部 n 个节距）。
- land 边缘 R ≤ 0.2 mm；land 面耐磨处理（请提供工艺与硬度）。
- 屏：Ø0.6–0.8 mm、30–40% 开孔，22 片规格一致。——并请说明贵司用于「pattern-SAP 干法沉积」的屏既有规格（孔型/孔径/开孔率/层积方式），因我司现有资料记载贵司丝网为六边形孔、≥1.4 mm、60/70/80% 开孔，与本方案目标不同，需澄清适用范围。
- Sleeve ID tag：逐片唯一（22 个唯一 ID），编码「尺寸 + 侧别 + 版本」，可被 PLC 读取；未读到或读到不匹配时须允许 PLC 拒绝启动。 请提供 tag 技术方案（RFID/二维码/其它）与读取冗余方案。
- 承载体：pin + 锥面锁紧，pinned to encoder zero；换装 ≤15 min/鼓。 请说明换装工时口径（含/不含对相与验证），以厘清与我司既有资料「30 s 换网」的差异。
- 防错装反设计：丝网锥度方向须有物理防呆或 ID 编码防错（我司记录贵司曾有锥度装反导致 SAP 堵塞事故）。
- 动平衡 G1.0，逐 sleeve 组复检。
- Land 高为逐片变量（按该片自身 SAP 床高）；请确认可否按我司逐片规格分别加工，并给出高差加工能力。
- NDA 与 IP 条款：孔径分布与 pattern 细节为 KC 专有技术，须受 NDA 约束并配合 IP 申请。
- 交付物：每片的检测报告（A1–A10 各项）、材质证明、装配图与限位结构图（用于澄清压合间隙定义，见 §3.3(a)）。
## 11. 待验证与外部输入

|||||
|---|---|---|---|
|1|澄清压合间隙在两侧 land 高不同时的定义（两侧 land 高之和 or 限位块间隙？）+ 索取限位结构图|设备商 / sleeve 供应商|最高|
|2|澄清相位精度口径：±0.02 mm vs ±0.05 mm|设备商|最高（85 公差链依赖）|
|3|要求 ID tag 逐片唯一（覆盖同 ups 组内尺寸混淆）|设备商 / PLC 供应商|最高|
|4|澄清「≤15 min/鼓」vs「30 s 换网」口径|Nichidai|高|
|5|索取 pattern 沉积类屏的既有规格（孔型/孔径/开孔率）|Nichidai|高|
|6|实测 SAP 床高（自由铺放状态）以解决 §3.3(b) 的松密度对账缺口|KC 实验室（用 [STM-00305 SAM分布.docx] / [STM-4597纸尿裤SAM分布测试.docx] 方法）|高|
|7|定义 land 磨损限值与更换判据|KC 工艺 + 设备商|中|
|8|确认 160 gsm sleeve 的 land 高取值|设备商|中|
|9|索取 sleeve 加工图与 ID tag 方案|Nichidai|中|

## 12. 依据与红线

依据：One_Drum_Two_Ups_11_Sizes_1000ppm.pptx P4/P8/P9/P15/P16/P18 + notes；WKB [日本Nichdai 丝网工艺技术交流]（丝网规格/卡簧快换/锥度事故/IP 归口）、[Patterned SAP core 6.pptx]（Nichidai screen technology 页）、[STM-00305 SAM分布.docx]、[STM-4597纸尿裤SAM分布测试.docx]；本地 references/80-高速pattern芯体成型工程总纲.md、83、85

红线：
1. 全部 sleeve 规格为源文件目标值（B 级），非已制造件实测值；引用须携带等级。
2. §3.3(a) land 高口径、§3.3(b) 床高-松密度对账、§5.1 相位精度口径、§4.1 屏规格差异、§6 换装工时分歧——五处冲突/缺口必须并列呈现，禁止静默取其一。
3. §7.2 的失效模式覆盖分析与「ID 须逐片唯一」的要求，是本次推断（基于 ups 组内多尺寸这一事实），依据已给出，未与 PLC 供应商确认。
4. 磨损限值、锥度防呆方式、ID 技术方案在源文件中均未定义，本文件已明确标注为待定义项，不得当作已定方案引用。
5. 结论不外推到其它 sleeve 架构（多鼓方案、卡簧快换方案）；外推须显式标注「推断」。

本文件由「纸尿裤全栈设计专家（CoreCraft）」生成 · 2026年09月22日

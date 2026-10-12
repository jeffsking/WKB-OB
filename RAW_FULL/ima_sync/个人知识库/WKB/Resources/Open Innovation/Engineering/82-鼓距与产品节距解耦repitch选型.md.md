---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_56f521bd1af7b6b076ab2599af3c4d09001a693ee6c0644e"
source_file: "82-鼓距与产品节距解耦repitch选型.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/82-鼓距与产品节距解耦repitch选型.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# 82-鼓距与产品节距解耦repitch选型.md.md

# 82 · 鼓距与产品节距解耦（repitch）选型

补库来源：One_Drum_Two_Ups_11_Sizes_1000ppm.pptx P1/P5/P6/P7/P18 + notes
对应 Gap：G16（鼓距—产品节距解耦单元完全缺失，零覆盖）｜严重程度 高｜属 P0 批次
副交付：G15（芯片废切 chip trim 与「芯长 > 产品节距」处置规则）
主表改善建议：补充①「鼓距 ≠ 产品节距」问题陈述与后果 ②cut-and-slip 适用边界 ③伺服 repitch 转塔原理/范围/单规格凸轮 ④repitch ratio 定义与逐规格表 ⑤chassis pitch 数据来源与假设标注
创建日期：2026-09-22

## 1. 问题陈述：为什么必须解耦

### 1.1 两个节距是两个不同的量

||||
|---|---|---|
|鼓距 drum pitch P|鼓面圆周上相邻两 pattern 中心距 = πD/n|成型线：鼓径 D + ups n|
|产品节距 chassis pitch C|后道（复合 / 折叠 / 切断 / 包装）要求的产品中心距|产品规格：芯长 + 股间间隙|

关键事实：P 只能取 πD/n 这一组离散值（D 定了以后由 n 决定），而 C 由 11 个产品规格各自决定，两者没有理由相等。

### 1.2 不解耦的后果

若不做解耦，则必须让 P = C，意味着：

- 换规格时必须换鼓径或换 ups —— 而 ups 是整数，大多数规格根本无法精确匹配；
- πD/n = C 对 11 个规格给出 11 个不同 D，与「单一鼓体」的前提直接矛盾。
因此 repitch（节距重排）单元是「一鼓多规格」的必要条件，不是可选优化项。

## 2. 两条解耦路线

||||
|---|---|---|
|原理|切断后由加速带/夹辊把单片芯体加速送到下道|转塔上的独立 puck（托块）沿各自凸轮轨迹取片、再放到目标节距|
|节距比范围|≥ ~1.03（源文件 P6）|0.85 – 1.40（源文件 P6）|
|方向性|只能加速（不能减速）|双向（可加速、可减速）|
|凸轮/换件|通用|每规格一份凸轮（recipe 项）|
|能否处理 Open NB（0.99）|✗ 失效|✓|
|源文件结论|不采用|采用|

源文件的判据（P6 标题）：「A servo repitch turret, not cut-and-slip — because NB needs the core slowed down」。
P6 脚注（结论稳健性条件）：「Replace the assumed chassis pitches with your product specs; the recommendation holds as long as any size needs a ratio below ~1.03 or above ~1.3.」
→ 即 cut-and-slip 的可行窗口约为 1.03 ≤ ratio ≤ 1.30；任何规格落在窗口外 ⇒ 必须用伺服转塔。

## 3. 转塔技术规格（可从源文件直接写入 RFQ 的部分）

||||
|---|---|---|
|类型|伺服 repitch 转塔（pucks on individual cam profiles）|源文件 P6/P7；B|
|节距比范围|0.85 – 1.40|源文件 P6；B|
|取片线速|396 或 462 m/min（= 鼓面线速，见 81 式 3）|源文件 P6/P7；B|
|放片节距|= chassis pitch（按规格）|源文件 P6；B|
|换规格方式|每规格一份凸轮（recipe + 换件）|源文件 P6/P12；B|
|传动|伺服轴，凸轮电子化描述为「cam per size」|源文件 P12；B|
|位置|双鼓压合点之下（切断、修边、repitch 依次在压合后）|源文件 P7；B|
|与 ups 的关系|转塔只认「取片线速 + 目标节距」，不感知 ups；ups 影响的是取片线速|源文件 P6/P7；推断（B）|

转速窗口自检：本方案 11 规格的 repitch ratio 实测跨度 0.99–1.25（§5），落在转塔 0.85–1.40 之内，双向余量充足（下沿 −0.14、上沿 +0.15）。这是选用通用转塔而非定制凸轮组的量化依据。

## 4. repitch ratio 的定义

ratio_s = chassis pitch_s / drum pitch_group(s)            …(1)

- 分母取决于该尺寸归属的 ups 组（见 81 §6）：7-up 组 = 395.83 mm；6-up 组 = 461.80 mm。
- ratio < 1 ⇒ 芯体需要减速（后道节距比鼓距更密）；
- ratio > 1 ⇒ 芯体需要加速。
chassis pitch 的构成（源文件假设值）：

chassis pitch = 芯长（MD 投影长） + k
k = 110 mm  （open diaper，源文件假设）
k = 130 mm  （pants，源文件假设）

## 5. repitch ratio 逐规格表（本次独立重算）

|||||||||
|---|---|---|---|---|---|---|---|
|Open NB|280|7-up|395.83|390|0.985|0.99|✗ 低于 1.03|
|Open S|314|7-up|395.83|424|1.071|1.07|✓|
|Open M|358|7-up|395.83|468|1.182|1.18|✓|
|Open L|385|6-up|461.80|495|1.072|1.07|✓|
|Open XL|420|6-up|461.80|530|1.148|1.15|✓|
|Open XXL|420|6-up|461.80|530|1.148|1.15|✓|
|Pant L|355|7-up|395.83|485|1.225|1.23|✓|
|Pant XL|365|7-up|395.83|495|1.251|1.25|✓|
|Pant XXL|365|7-up|395.83|495|1.251|1.25|✓|
|Pant XXXL|365|7-up|395.83|495|1.251|1.25|✓|
|Pant XXXXL|420|6-up|461.80|550|1.191|1.19|✓|

※ C 为源文件假设值（芯长 + k）。这是本表唯一的 B 级输入，替换为实测值后 ratio 全部需重算（见 §6）。

复算结论：11 项 ratio 与源文件 P5 表逐项一致（四舍五入到两位小数）✓。跨度 0.985 – 1.251。

## 6. ⚠️ 最关键的待替换输入：chassis pitch

### 6.1 源文件自述

源文件 notes（P1）：「Product (chassis) pitch was not in the Word file and is assumed as core + 110 mm (open) and core + 130 mm (pants); it only affects line speed and the repitch ratio.」

即：产品节距在源文件里是假设值，不是实测值；其影响面被明确限定为 线速 与 repitch ratio 两项。（对应主表 G19；待并入 WKB 常量表的行见 87。）

### 6.2 可执行的判定公式（替换实测值后如何复核结论）

设某 ups 组鼓距为 P，组内各规格的实测 chassis pitch 为 C_i：

判据：若存在任一 C_i / P < 1.03 或 > 1.30，则 cut-and-slip 不成立，必须用伺服转塔。

等价地，每组鼓距要求组内 chassis pitch 全部落在：

||||
|---|---|---|---|
|7-up|395.83|[407.7, 514.6] mm|假设值 {390, 424, 468, 485, 495, 495, 495} → 390 越下界 ❌|
|6-up|461.80|[475.7, 600.3] mm|假设值 {495, 530, 550} → 全部在区间内 ✓|

独立结论：在源文件假设下，11 个规格中恰有 1 个（Open NB）越界，且是唯一的越界者。这一个越界已足以否决 cut-and-slip。

反向校核：要让 Open NB 进入 cut-and-slip 窗口，需 C_NB ≥ 407.7 mm，即 open 的股间间隙 k_open ≥ 407.7 − 280 = 127.7 mm。该数值可作为向产品侧索取实测值时的验算靶——若实测 k_open ≥ 127.7 mm 且无其它规格 >1.30P，则 cut-and-slip 路线应重新评估（可省下转塔）。

### 6.3 敏感性与稳健性

|||
|---|---|
|chassis pitch 全部比假设值更小|7-up 组 ratio 进一步下降 → 更多规格越下界 → 转塔的必要性增强|
|open 的 k 显著大于 127.7 mm|NB 可能出界 → 转塔必要性减弱（但 pants 侧仍受 1.30 上界约束）|
|pants chassis pitch > 514.6 mm|Pant L–XXXL 越上界 → 转塔必要性恢复|
|实测值与假设值差异 < 5%|结论不变|

结论稳健性判定：由于假设值跨度（0.985–1.251）已同时逼近下界（−0.045）且预留上界余量有限（1.251 vs 1.30），实测值只要在 pants 侧上偏约 4% 或 open 侧继续下偏，转塔方向都不会反转。故「必须上伺服 repitch 转塔」这一结论对 chassis pitch 假设不敏感。

## 7. 与 G1（ups 选型）的耦合关系

鼓径 D  ──(πD/n)──▶  鼓距 P  ──┬──▶ 端区 E = P − L      （省包覆）
                               ├──▶ 鼓面线速 v = P×ppm   （SAP 落速基准，见 86）
                               └──▶ repitch ratio = C/P   （本节）

- ups 加多 → P 减小 → 端区减小（省包覆）但 → ratio 增大（7-up 组 ratio 普遍高于 6-up 组，见 §5：同为 420 mm 芯长，7-up 组 ratio 更高）。
- 反过来，ratio 的下界构成 ups 选择的一个隐藏约束：把某尺寸推到更高 ups 会拉低它的 ratio，可能突破 cut-and-slip 窗口（本例正是 NB 被推到 7-up 后 ratio = 0.985）。
- 故 81 的 ups 分配不能只看端区，必须同时校核 ratio。 本条为本次分析新增的耦合发现，源文件未显式表述。等级：推断（基于式(1) 与 81 §3.3 取舍规则的组合分析）。
## 8. 芯片废切 chip trim（副交付 G15）

### 8.1 触发判据

规则（源文件 P5 脚注）：Trim = cut the core wrap back to a 60 mm end zone where it would exceed 80 mm.
即：若某规格端区 E > 80 mm → 把端区切回到 60 mm，切除长度 = E − 60。

判据的理由（含两层）：

- 材料与形态：端区不承载 SAP，超过 80 mm 的部分纯属浪费；过长的无支撑包覆舌片在高速下有卷边/翻折风险。
- 物理冲突（仅 NB）：Open NB 存在「芯长 > 产品节距」的硬冲突——鼓距 395.8 mm（= 未修剪的整芯长度）大于假设的 NB 产品节距 390 mm。若不修剪，NB 芯体在后道物理上放不进自己的产品节距。修剪到 60 mm 端区后，芯长 = 280 + 60 = 340 mm ≤ 390 mm ✓。
（对应的源文件 top risk #3「NB core longer than chassis」；等级 B）

### 8.2 逐规格应用

||||||
|---|---|---|---|---|
|Open NB|115.8|✅|55.8 ≈ 56|280 + 60 = 340|
|Open S|81.8|✅|21.8 ≈ 22|314 + 60 = 374|
|Open M|37.8|✗|—|—|
|Open L|76.8|✗|—|—|
|Open XL / XXL|41.8|✗|—|—|
|Pant L|40.8|✗|—|—|
|Pant XL / XXL / XXXL|30.8|✗|—|—|
|Pant XXXXL|41.8|✗|—|—|

复算验证：56 / 22 mm 与源文件 P5/P18 表值完全一致 ✓。

### 8.3 硬件与换件要求

||||
|---|---|---|
|切刀辊|双刀切刀辊（double-knife cut roll） —— 同一个辊上实现「定长切 + 芯片切」|源文件 P6/P7/P18；B|
|排屑|真空排屑（vacuum chip extraction）|源文件 P6；B|
|换件归属|刀片插片仅随 NB 与 S 两个 sleeve 更换（其余规格用单切）|源文件 P6/P18；B → 见 83 Change-part 层|
|与既有约束的合并表述|WKB [Open Diaper Process Introduction--202104.pdf] FPC Pad Cutter Off 模块已含：刀辊/砧辊直径、cutter point 500 m/min、「MAX pad design length 必须小于砧辊弧长」。本节的 chip trim 是在该约束之外的补充：当「芯长 > 产品节距」时的处置手段。两者并列使用，不可互相替代。|源文件 P6/P18 + WKB FPC 模块|

## 9. 与既有 WKB 知识的衔接与差异（避免误引）

||||
|---|---|---|
|[Open Diaper Process Introduction--202104.pdf] FPC Pad Cutter 模块|刀辊/砧辊几何、cutter point 速度、「pad 长 < 砧辊弧长」|前置约束；本文件补「芯长 > 产品节距」的处置逻辑|
|GB/T 33280-2016 纸尿裤规格与尺寸、STM-00064 Diaper尺寸.docx、STM-00433 Pants尺寸.doc|产品尺寸标准（MD/CD 外形尺寸）|提供的是尺寸，不是节距；节距（相邻产品中心距）在 WKB 中不存在|
|[合作开发新模具设计]|模具打样讨论|与节距解耦无关|
|03_卫材产线约束常量表.md §1|线速 / ppm 基准|缺 chassis pitch 行 → 补充行见 87|
|[日本Nichdai 丝网工艺技术交流]|丝网孔型/开孔率/卡簧快换|与 repitch 无关|

口径提醒：WKB 中「尺寸标准」条目不能用来推导 chassis pitch。尺寸标准给的是成品外形（长×宽），chassis pitch 是工艺节距（含股间间隙），二者不同。本次比对中若把尺寸标准当作节距来源，会引入系统性误差。

## 10. 待验证与外部输入

||||
|---|---|---|---|
|1|索取 11 尺寸成品节距（chassis pitch）实测值|KC 产品侧|把 §5 的 ratio 从 B 级升为 A 级；复核 §6.2 判据（最高优先）|
|2|索取 repitch 单元配置说明（范围、凸轮更换方式、精度）|JOA、恒昌、HCH|交叉验证 §3 规格与 0.85–1.40 范围|
|3|确认 cut-and-slip 的实际上限（源文件取 ~1.30，无出处）|设备商 / 内部产线|§2 判据的上界锚定|
|4|确认 NB/S 双刀切刀辊的 knife insert 换装工时|设备商|并入 83 的 Change-part 层与换型工时分解|
|5|确认 NB 在剪短到 340 mm 后，后道（折叠/包装）是否仍有位置约束|KC 后道工艺|§8.1 理由 2 的下游闭合|

## 11. 依据与红线

依据：One_Drum_Two_Ups_11_Sizes_1000ppm.pptx P1/P5/P6/P7/P12/P18 + notes（P1/P5/P6）；WKB [Open Diaper Process Introduction--202104.pdf]（FPC 切断约束）、GB/T 33280-2016、[STM-00064 Diaper尺寸.docx]、[STM-00433 Pants尺寸.doc]、03_卫材产线约束常量表.md；本地 references/80-高速pattern芯体成型工程总纲.md、81-成型鼓ups选型计算.md

红线：
1. chassis pitch 全部为源文件假设值（B 级），源文件明确声明其不在 Word 文件中。引用 ratio 表时必须携带该标注，禁止当作实测值引用。
2. repitch ratio 的算术复算已验证（与 P5 逐项一致）；§6.3 的稳健性结论与 §7 的耦合结论为推断，依据是判据组合分析，未实测。
3. ~1.03 / ~1.30 两个边界来自源文件，无出处，属 B 级，使用前应向设备商锚定。
4. chip trim 的 80/60 mm 阈值来自源文件，未说明推导；§8.1 给出的两层理由是本次推断，须由工艺侧确认。
5. 结论不外推到其它鼓径 / 其它 chassis pitch 体系；外推须显式标注「推断」。

本文件由「纸尿裤全栈设计专家（CoreCraft）」生成 · 2026年09月22日

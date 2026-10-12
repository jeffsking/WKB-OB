---
type: source
title: "84 Sleeve 工程规格与换装防错设计"
source_type: 派生工程笔记（补库动作 · Gap G14）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/84-Sleeve工程规格与换装防错设计.md.md
original_link: ""
date_published: 2026-09-22
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "Positioning: the sleeve is the ONLY size carrier in the architecture — the drum body (sectors, motors, encoders, nip gap, alignment) is identical across all 11 sizes, and size is expressed entirely by the sleeve; source rule: 'Everything that defines phase is on the drum body; everything that defines size is on the sleeve'（定位：套筒是唯一尺寸载体；鼓体在 11 个尺寸间完全不变）"
  - "Corollary: sleeve engineering-spec quality IS the ceiling of the whole line's multi-size capability — a defective sleeve (unequal pitches, wrong land height, unpaired channels) cannot be compensated by any drum precision（推论：套筒规格质量 = 整线多规格能力的上限）"
  - "22-sleeve architecture: 22 = 11 sizes × 2 sides (skin/poly); each size is a PAIR that must be designed and fabricated together; each grade change swaps 2 sleeves on two drums in parallel; storage needs 22-position carrier racks — listed by the source as top risk #5（22 片架构：11 尺寸 × 2 侧；换型换 2 片；需 22 位承放架，源文列为 top risk #5）"
  - "Land system: pocket = SAP deposition zone (screen open only there); land = every zone that must be SAP-free AND bondable to the opposite side, including the 30–116 mm end zones; land height 0.45 mm nominal; design rule — give each sleeve the land height of ITS OWN bed so the nip still meets land-to-land（land/pocket 体系：端区也是 land；land 高按各 sleeve 自身床高取，保证 land-to-land 压合）"
  - "⚠️ Land height is a PER-SLEEVE VARIABLE, not a global constant: 0.45 mm is the 230 gsm condition (bed height 0.44 mm); 160 gsm → 0.31 mm. Left open: how the 0.15–0.18 mm nip gap is defined when the two drums have different land heights（land 高是逐片变量而非全局常量；压合间隙定义待澄清）"
  - "⚠️ Bed height vs bulk density is NOT self-consistent: back-calculated from bed height, ρ = 0.516–0.523 g/cm³, versus the stated SAP bulk density spec 0.62–0.70 g/cm³ — a ~20–35% gap, meaning real beds would be THINNER than designed, leaving land relatively high（床高反推松密度与规格 0.62–0.70 不自洽，差 20–35%）"
  - "Screen spec: Ø0.6–0.8 mm holes, 30–40% open, IDENTICAL across all 22 sleeves, and independent of ups; reason — screen spec sets through-air velocity and pressure drop, so any variation would make one recipe fail to cover 11 sizes（屏规格：Ø0.6–0.8 mm、30–40% 开孔、22 片一致、与 ups 无关）"
  - "⚠️ Screen spec conflicts with existing WKB Nichidai knowledge by ~2× on both axes: this plan Ø0.6–0.8 mm / 30–40% open versus Nichidai hexagonal ≥1.4 mm / 60–70–80% / 0.1 mm layered etching with taper direction; both must be recorded in parallel and never silently merged（屏规格与既有 Nichidai 口径差约 2 倍，须并列不得择一）"
  - "Nichidai legacy accident to inherit: reversed screen taper caused SAP blockage; snap-ring quick change with a 30 s target; pore-size distribution is KC proprietary and must be protected（Nichidai 历史事故：锥度装反导致 SAP 堵塞；孔径分布为 KC 专有技术）"
  - "Tolerance system: sleeve pattern pitch ±0.02 mm over 2,771 mm across all n pitches; pin phase to encoder zero ±0.02 mm; post-grade-change pin phase ±0.05 mm; sleeve-to-sleeve index repeatability ±0.02 mm; 'equal pitches = one phase fits all' is the STRUCTURAL premise of multi-size-one-drum plus a single vision loop（公差体系：等节距 ±0.02 mm 是多规格共鼓 + 单视觉闭环的结构前提）"
  - "⚠️ Phase accuracy has two conflicting values: ±0.02 mm (manufacture + assembly spec, source P8) versus ±0.05 mm (actual post-change dispersion, source P18) — a 2.5× gap and a key input to the registration tolerance chain（相位精度两处口径差 2.5 倍）"
  - "Poka-yoke: per-sleeve ID tag read by PLC with start interlock; the source only blocks the WRONG UPS, but the same ups group contains multiple sizes — so the ID must be UNIQUE PER SLEEVE (22 IDs) encoding size + side + version, otherwise same-ups size confusion is not caught（防错：ID 须逐片唯一，否则同 ups 组内尺寸混淆拦不住——此为本次推断）"
  - "Skin/poly pairing rule: patterns may differ, but every channel meant to bond must exist on BOTH sleeves at the same position; design the pair as ONE CAD file and fabricate both from it; channel pairing ∧ registration tolerance together guarantee ≥90% channel bond area（skin/poly 成对规则：同一 CAD 制造两片）"
  - "Acceptance list A1–A10 (index repeatability, pitch equality, land edge R ≤0.2 mm, wear-resistant land faces, screen spec, unique ID tag, carrier fit, anti-reverse assembly, per-piece land height, balancing G1.0) plus wear management and IP/NDA ownership（验收清单 A1–A10、磨损管理与 IP 归口）"
  - "Five red lines: all sleeve specs are source TARGET values (B level), not measured; five conflicts/gaps must be presented in parallel; the ID-uniqueness analysis is an inference not confirmed with the PLC supplier; wear limits / taper poka-yoke / ID technology are UNDEFINED; conclusions must not be extrapolated to other sleeve architectures（五条红线）"
pages_linked: ["[[IPC BCC OI Portfolio（开放创新项目组合）]]", "[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]", "[[One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）]]", "[[03_卫材产线约束常量表（准入校验工具）]]", "[[Nichidai（日丝）]]", "[[Core Channel Pattern（芯体通道花型设计）]]", "[[SAP性能指标（CRC AUL GBP Vortex）]]"]
---

# 84 Sleeve 工程规格与换装防错设计

> 一句话定位：一份 **套筒（sleeve）作为「尺寸载体」的工程规格与防错设计补库笔记**——把 One_Drum 方案里分散在 P4/P8/P9/P15/P16/P18 的套筒信息，**收敛成一套可发给供应商的规格、验收项与防错要求**。（中文：在多规格共鼓架构里，**套筒就是"尺码"本身**；这份文件的价值在于把"换码风险"翻译成"套筒规格"。）

> ⚠️ **来源性质（2026-09-29）**：本件为**派生工程笔记**（自述由"纸尿裤全栈设计专家（CoreCraft）"生成，2026-09-22），**规格全部为源文件目标值（B 级）而非已制造件实测值**，且**多处结论自标为"推断"**。credibility 定为**中**：**结构、机理与冲突识别可用，绝对数值须经供应商与实测确认**。

## 原文要点 Original Key Points

### 1. 文件定位与来源 Provenance

| 项 | 内容 |
|---|---|
| 补库来源 | **One_Drum_Two_Ups_11_Sizes_1000ppm.pptx P4 / P8 / P9 / P15 / P16 / P18** |
| 对应 Gap | **G14**（Sleeve 作为"尺寸载体"的工程规格与防错设计缺失）｜严重程度 **高**｜属 **P0 批次** |
| 主表改善建议 | ① 承载体接口与换装工时 ② sleeve ID tag + PLC 联锁防错规格 ③ skin/poly 成对设计规则 ④ land 高度体系 ⑤ 屏规格与 ups 无关性 ⑥ 验收项与磨损点检 ⑦ IP 与保密归口 |
| 创建日期 | **2026-09-22** |

### 2. Sleeve 的定位：唯一的尺寸载体

> 源文件 P8 副标题（原文）：*"Everything that defines phase is on the drum body; everything that defines size is on the sleeve."*

| 部件 Part | 承载什么 Carries | 是否变动 Changes |
|---|---|---|
| **Body 鼓体** | **相位与机械几何**（扇区、电机、编码器、压合间隙、对中） | **永不动**（11 尺寸间完全不变） |
| **Sleeve 套筒** | **尺寸**（MD pattern 布局 + 端区 + 通道位置） | **每次换 2 片** |

> **推论（源文）**：**套筒的工程规格质量 = 整线多规格能力的上限**。套筒一旦有缺陷（**节距不等、land 高错、通道不成对**），鼓体再精密也无法补偿。

### 3. 22 片架构 22-Sleeve Architecture

| 项 | 值 |
|---|---|
| 总数 | **22 片 = 11 尺寸 × 2 侧（skin / poly）** |
| 成对关系 | 每 size **skin 侧 1 片 + poly 侧 1 片**，**必须成对设计与制造** |
| 每次换型更换 | **2 片**（skin 1 + poly 1），**两鼓并行更换** |
| 存储 | 需 **carrier racks（承放架）22 位** |

> ⚠️ **22 片的规模含义**：源文件 P18 明确把 **"22 sleeves to store and maintain"** 列为 **top risk #5**，对策为 **carrier racks + 每 campaign 检查 land 面磨损**。这是**本架构主要的运维负担来源**，须在 RFQ 中作为独立条目列出。

### 4. Land 高度体系 Land Height System

#### 4.1 定义（pocket-and-land 浮雕结构）

| 结构 | 定义 | 是否有屏孔 |
|---|---|---|
| **Pocket（凹坑）** | **SAP 沉积区**，对应 pattern；**屏开孔只在此区** | ✓ |
| **Land（凸台）** | 所有需要「**无 SAP + 可与对侧粘合**」的区域 | ✗ |
| **端区（30–116 mm）** | **也是 land** —— 保证相邻两芯之间无 SAP | ✗ |

> 源文件 P9（原文）：*"Raised lands = channels + end zones — 0.45 mm high; 30–116 mm end zones are lands too, so no SAP between cores"*

#### 4.2 床高 → land 高映射

| SAP 床高 Bed | Land 高 | 备注 |
|---|---|---|
| **160 gsm** | **0.31 mm** | ≈ 0.31 mm + 余量 |
| **230 gsm** | **0.44 mm** | **0.45 mm**（= 源文件 P9 标称值） |

> **核心规则（源文 P15 原文）**：*"Skin and poly SAP gsm can differ (e.g., 230 skin / 160 poly); give each sleeve the land height of its own bed so the nip still meets land-to-land."*（两侧 gsm 可以不同，各 sleeve 取自身床高作 land 高，使压合时仍 **land-to-land** 接触。）
> **设计判据**：land 高 **≥ 该 sleeve 自身床高**，使对压时**先由 land 接触**，SAP 床不被过压。

#### 4.3 ⚠️ 两处须澄清的口径问题（本次发现）

**(a)「0.45 mm」是全局常量还是 230 gsm 工况值？**

| 出处 | 值 | 含义 |
|---|---|---|
| 源文件 P9 | **0.45 mm** | 单一值 |
| 源文件 P15 | 逐 sleeve 按自身床高取（160 gsm 侧应 ≈0.31 mm） | 逐片变量 |
| 源文件 P16 | 床高 **0.44 mm @230 gsm** | 与 0.45 吻合 |

- **判定**：**0.45 mm 是 230 gsm 工况下的标称值**；低 gsm 的 sleeve 的 land 高**必须按自身床高取**。因此**套筒图纸上的 land 高是逐片变量，不是全局常量**。
- **须澄清**：源文件**未给出 160 gsm sleeve 的 land 高取值**，也**未说明两鼓 land 高不同时压合间隙 0.15–0.18 mm 如何定义**（是两侧 land 高之和？还是限位块间隙？）—— **此项直接决定压合能否 land-to-land 成立**，须向设备商索取限位结构图。

**(b) 床高与松密度规格不自洽**

| 项 | 值 |
|---|---|
| 由床高反推体积密度 | **160/0.31 = 0.516 g/cm³**；**230/0.44 = 0.523 g/cm³**（两者一致 → 源文件内部自洽 ✓） |
| 源文件 P16 的 SAP 规格 | **松密度 0.62–0.70 g/cm³** |
| 用 0.62–0.70 反算床高 | 160 gsm → **0.229–0.258 mm**；230 gsm → **0.329–0.371 mm** |
| **差距** | **约 20–35%**，方向为「**实际床高会比按松密度预测的更厚**」 |
| 可能原因（未验证） | 床高口径含颗粒间自由空隙的"自由堆积"状态 / 含 land 浮雕的基准差异 / 松密度规格与床高由不同假设独立得出 |
| 影响 | land 高按床高设定 → **若实际松密度落在 0.62–0.70，则床比设计更薄，land 相对偏高**（对压仍 land-to-land，但**压实余量变大**，可能导致 SAP 压实不足/通道粘接受影响）。须用**实测床高（含铺放后未压实状态）**替代计算值 |
| 等级 / 方法 | 本次发现的对账缺口，须用 **STM-00305 SAM 分布 / STM-4597 纸尿裤 SAM 分布测试**方法实测 |

#### 4.4 Land 边缘与表面

| 项 | 规格 |
|---|---|
| Land 边缘圆角 | **R ≤ 0.2 mm**（向 Nichidai 的索取项；B 级） |
| Land 表面 | **耐磨面（wear-resistant land faces）**（B 级） |
| 理由（推断） | 边缘过锐会划伤包覆无纺布并在高速下产生应力集中；land 面承受反复压合与清机磨损 |

### 5. 屏（Perforated Screen）规格

| 项 | 规格 |
|---|---|
| 孔径 | **Ø0.6–0.8 mm** |
| 开孔率 | **30–40% open** |
| 一致性要求 | **"same on every sleeve"** —— 全部 22 片的屏规格必须一致 |
| 与 ups 的关系 | **与 ups 无关**（屏是 sleeve 的一部分，不受 n 影响） |

> **为什么"各 sleeve 一致"是硬要求**：**屏规格决定穿透风速与压损**。若各 sleeve 屏开孔率不同，则**同一个 recipe 的成型真空/风量在不同 sleeve 上产生不同的沉积行为** → **换型后工艺窗口漂移**，且**无法用单一 recipe 覆盖 11 尺寸**。这是「一鼓多规格 + 单 recipe 体系」能否成立的**前提**。

#### 5.1 ⚠️ 与既有 WKB Nichidai 知识的口径差异（须并列呈现）

| 来源 | 孔型 | 孔径 | 开孔率 | 层积 |
|---|---|---|---|---|
| **源文件 P9（本方案）** | 未注明 | **Ø0.6–0.8 mm** | **30–40%** | 未注明 |
| **WKB〔日本 Nichidai 丝网工艺技术交流〕** | **六边形孔** | **≥1.4 mm（下限）** | **60 / 70 / 80%** | **0.1 mm 层积蚀刻，有锥度方向** |

- **差异显著**：**孔径差约 2×，开孔率差约 2×**。
- **可能原因（未验证）**：两者面向的**成型机制不同** —— Nichidai 的丝网为**传统整幅成型**（大孔高开孔率以通过纤维/浆料），本方案的屏为 **pattern-SAP 沉积**（小孔以在 land 边缘形成**锐利边界**、抑制 stray SAP）。
- **等级**：源文件 P9 的屏规格是**目标规格（B 级）**；Nichidai 是其**既有成熟产品口径（C 级，厂商标称）**。
- **处理要求**：**两条口径必须并列记录，禁止静默取其一**。向 Nichidai 询价时须明确说明「**本方案用于 pattern-SAP 干法沉积，非浆料成型**」。

#### 5.2 Nichidai 的历史事故教训（必须继承）

| 项 | 内容 |
|---|---|
| **锥度装反 → SAP 堵塞** | 丝网锥度方向装反会导致 SAP 堵塞（**已发生的历史事故**） |
| 快换方式 | **卡簧式快换**，供应商目标 **30 s 换网**（经验待确认） |
| IP 归口 | **孔径分布为 KC 专有技术**，须保密并申请 IP |

> **推论**：**锥度方向是不可逆向的装配依赖** → 必须在 ID 防错体系中**一并编码**（不仅防错 ups，还须**防错装反方向**）。

### 6. Pattern 公差体系 Tolerance System

| 项 | 公差 | 含义 |
|---|---|---|
| Sleeve pattern 制造公差 | **±0.02 mm over 2,771 mm**，全部 n 个节距 | 22 片中任一片的 n 个节距必须等距 |
| 引脚相位（→编码器零点） | **±0.02 mm** | 装好后 pattern 相对编码器零点的相位准确度 |
| 换型后引脚给出的相位 | **±0.05 mm** | 整机换型后引脚能保证的实际相位 |
| Sleeve 间索引重复性 | **±0.02 mm** | 22 片互换后索引位置的一致性（向 Nichidai 索取） |

#### 6.1 ⚠️ 相位精度两处口径不一致（本次发现）

| 出处 | 值 | 性质 |
|---|---|---|
| 源文件 P8 | **±0.02 mm** | 「Pinned to encoder zero ±0.02 mm, taper-locked」—— **规格值** |
| 源文件 P18 | **±0.05 mm** | 「Pins give ±0.05 mm」—— **换型实操值** |

- **判定**：两者**不是同一件事**，但源文件中未区分—— **±0.02 mm 是制造 + 装配规格**；**±0.05 mm 是换型后整机实际相位分散**（含更换动作引入的重复性、锥面锁紧差异、温度等）。
- **差 2.5 倍**，是**套准公差链的关键输入**，**必须澄清后才能做公差链闭合**。等级 B（须澄清）。

#### 6.2 「等节距 = 同一相位适配全部」的机理

> 源文件 P8 注释（原文）：*"Equal pitches = one phase fits all"*

- 若某 sleeve 的 **n 个节距不等**，则**无法用单一相位偏置把全部 n 个 pattern 对齐到对侧鼓** → 必须**逐 pattern 修正**（而本架构的视觉闭环**只能整体 trim，不能逐 pattern 修**）。
- 因此 **±0.02 mm 等距要求**是**多规格共鼓 + 单视觉闭环的结构前提**，**不是"精度越高越好"的泛化要求**。

### 7. 承载体（Carrier）与换装接口

| 项 | 规格 |
|---|---|
| 定位 | **pin（销）+ 锥面（taper）锁紧** |
| 相位基准 | **pinned to encoder zero**（销定位到编码器零点） |
| 换装工时 | **≤15 min / 鼓**；两鼓并行 → **目标 ≤15 min** |
| 换型免对相 | **"Grade change without re-registration"** —— 换型不需要重新对相 |
| 与既有知识的差异 | WKB Nichidai 记录**卡簧式快换、目标 30 s 换网**（C 级） |

> ⚠️ **须澄清的 30 倍分歧**：**≤15 min/鼓（源文件）vs 30 s/网（Nichidai 目标）**。差异可能来自 (a) **换装对象不同**（整片 sleeve 含承载体 vs 仅丝网）、(b) **是否含对相与验证**、(c) **供应商口径为纯动作时间**。**引用时必须并列，不得择一。**

### 8. Sleeve ID tag + PLC 联锁防错 Poka-yoke

#### 8.1 规格

| 项 | 内容 |
|---|---|
| 载具 | 每片 sleeve 带 **ID tag** |
| 读取方 | 由 **PLC** 读取 |
| 防错动作 | **阻止（block）错误 ups 的 recipe 被载入** —— **interlock on start** |
| 与 recipe 的关系 | **Recipe 载入流程的第一步就是 sleeve ID 校验** |

#### 8.2 防错覆盖范围（须覆盖的失效模式）

| # | 失效模式 | 是否被覆盖 | 依据 |
|---|---|---|---|
| 1 | **装错 ups**（本应 6-up 装了 7-up 的 sleeve） | ✅ 核心功能 | 源文件 P18 top risk #2 |
| 2 | **skin / poly 装反** | ✅ 需 ID 编码侧别 | 源文件未明确，须补（**推断**） |
| 3 | **丝网锥度装反**（Nichidai 历史事故） | ✅ 需 ID 编码方向 | WKB 事故教训，须补（**推断**） |
| 4 | **装错尺寸**（同 ups 组内混淆，如 Open M ↔ Pant L） | ⚠️ **取决于 ID 粒度** | 两者均为 7-up，**须确认 ID 是否区分到尺寸**（**推断，须澄清**） |
| 5 | 22 片存储中拿错 | ✅（读取即报错） | 需存储管理配合 |
| 6 | **ID tag 失效/未读到** | ✅ 应 **fail-safe（拒绝启动）** | 须在规格中显式要求（**推断**） |

> ⚠️ **本架构的隐含短板（本次发现）**：源文件**只说明"阻止错误 ups 的 recipe"**，但**同一 ups 组内有多个尺寸**（7-up 组含 Open NB/S/M + Pant L/XL/XXL/XXXL 共 7 个尺寸）。**若 ID 只区分 ups，则组内尺寸错装不会被拦截**，而**组内尺寸错装的后果与 ups 错装同级**（pattern 长度错 → 端区错 → 套准与切断全部失配）。
> **要求**：**ID tag 必须逐片唯一（22 个唯一 ID），并编码 尺寸 + 侧别（skin/poly）+ 版本，而非仅 ups。** 此项须写入 RFQ。

### 9. Skin / poly 成对设计规则

> 源文件 P9（原文）：*"Skin/poly pairing rule: patterns may differ, but every channel meant to bond must exist on both sleeves at the same position. Design the pair as one CAD file and fabricate both from it."*

| 规则 | 内容 | 理由 |
|---|---|---|
| **R1** | 凡需粘合的通道，**必须在对侧 sleeve 的同位置存在** | 压合时由两侧 land 互为支撑才能形成通道粘接；单侧有 land 只能形成半通道 |
| **R2** | **同一 CAD 文件设计一对**，并由该文件同时制造两片 | 消除两片之间由独立建模/独立加工引入的相对偏差 |
| **R3** | pattern 本身**可以不同**（skin ≠ poly） | 允许 (a) skin/poly gsm 不同（如 230/160）、(b) 两侧功能分工不同 |
| **R4** | **通道位置是成对的定义域；SAP 布局是各自的自由度** | 「通道」与「SAP pattern」是两个概念，不要混为一谈 |

**与套准的关系**：**通道成对性 + 套准规格（|MD| ≤1.0 / |CD| ≤0.5 mm）**共同保证 **≥90% 通道粘接面积**：

> 通道粘接成立 ⇔ (a) 两侧通道同位置存在（本规则） **∧** (b) 两侧相位偏差在公差内

> 若 (a) 不成立，则**无论套准多好都无法粘合** —— 这是 **R2「同一 CAD」的不可替代性**。

### 10. 验收项清单与磨损管理 Acceptance & Wear

#### 10.1 到货 / 加工验收项 A1–A10

| # | 项目 | 规格 | 方法 |
|---|---|---|---|
| A1 | Sleeve 间索引重复性 | **±0.02 mm** | 三坐标 / 专用检具；22 片逐一比对 |
| A2 | Pattern 节距等距性 | **±0.02 mm over 2,771 mm**，全部 n 个节距 | 三坐标逐节距测量 |
| A3 | Land 边缘圆角 | **R ≤ 0.2 mm** | 轮廓仪 / 光学 |
| A4 | Land 面耐磨处理 | 耐磨面（工艺待定） | 材质证明 + 表面硬度 |
| A5 | 屏规格 | **Ø0.6–0.8 mm、30–40% 开孔，22 片一致** | 光学计数 / 压损法 |
| A6 | Sleeve ID tag | **逐片唯一，编码 尺寸 + 侧别 + 版本；PLC 可读；未读到须拒绝启动** | 装配合格测试 |
| A7 | 承载体配合 | pin + 锥面锁紧；相位对编码器零点 | 装配合格测试 |
| A8 | 锥度方向 / 装配方向防错 | **不可逆向装配** | 装配试验（防呆验证） |
| A9 | land 高（逐片） | 按该 sleeve 自身床高（§4.2） | 三坐标 / 塞规（须先澄清 §4.3(a)） |
| A10 | 动平衡 | **G1.0**，逐 sleeve 组复检 | 动平衡机 |

#### 10.2 磨损管理

| 项 | 内容 |
|---|---|
| 点检周期 | **每个 campaign（生产周期）后点检 land 面磨损**（源文件 P18 top risk #5；B 级） |
| 关注面 | land 面（承受反复压合）、端区 land（切断区）、边缘（**推断**） |
| 存储 | **carrier racks（承放架）**，避免碰撞与变形 |
| 更换判据 | **未定义**（源文件未给出 land 磨损限值） |

#### 10.3 IP 与保密归口

| 项 | 内容 |
|---|---|
| 孔径分布 / pattern 细节 | **KC 专有技术，须保密并申请 IP** |
| 归口动作（**推断**） | 供应商签 NDA；图纸受控发放；pattern 数据不出 KC |
| 与源文件的呼应（**推断**） | 源文件 P9 提到 ID tag「由 PLC 读取」—— **ID 编码本身也不宜外泄完整映射关系** |

### 11. RFQ 询价项（可直接发给 sleeve 供应商）

> 🔴 **商务敏感**：源文给出可直接发送的询价条目清单。本页**只登记条目结构与等级，不落报价、条款与商务条件**。条目要点如下（详见 manual_review）：

- **22 片 sleeve 套件**（11 尺寸 × skin/poly），pocket-and-land 浮雕，端区亦为 land；
- 索引重复性 **≤ ±0.02 mm**；pattern 节距等距性 **≤ ±0.02 mm over 2,771 mm**；
- land 边缘 **R ≤ 0.2 mm**，land 面耐磨处理（请提供工艺与硬度）；
- 屏 **Ø0.6–0.8 mm / 30–40%**，**22 片一致**；**并请说明贵司用于「pattern-SAP 干法沉积」的屏既有规格**（因既有资料记载为六边形孔 ≥1.4 mm / 60–70–80%，需澄清适用范围）；
- **Sleeve ID tag 逐片唯一（22 个）**，编码尺寸 + 侧别 + 版本，PLC 可读，未读到或不匹配时须允许 PLC 拒绝启动；请提供 tag 技术方案与读取冗余方案；
- 承载体 pin + 锥面锁紧、pinned to encoder zero、换装 **≤15 min/鼓**；**请说明换装工时口径**（含/不含对相与验证），以厘清与既有资料「30 s 换网」的差异；
- **防错装反设计**（锥度方向须有物理防呆或 ID 编码防错，源文记有锥度装反致 SAP 堵塞事故）；
- **动平衡 G1.0**，逐 sleeve 组复检；
- **land 高为逐片变量**（按该片自身 SAP 床高），请确认可否按逐片规格分别加工并给出高差加工能力；
- **NDA 与 IP 条款**；
- 交付物：每片检测报告（A1–A10）、材质证明、装配图与**限位结构图**（用于澄清压合间隙定义）。

### 12. 待验证与外部输入 Open Items

| # | 事项 | 归口 | 优先级 |
|---|---|---|---|
| 1 | 澄清压合间隙在两侧 land 高不同时的定义 + 索取限位结构图 | 设备商 / sleeve 供应商 | **最高** |
| 2 | 澄清相位精度口径：**±0.02 vs ±0.05 mm** | 设备商 | **最高**（套准公差链依赖） |
| 3 | 要求 ID tag **逐片唯一**（覆盖同 ups 组内尺寸混淆） | 设备商 / PLC 供应商 | **最高** |
| 4 | 澄清「**≤15 min/鼓** vs「**30 s 换网**」口径 | Nichidai | 高 |
| 5 | 索取 pattern 沉积类屏的既有规格（孔型/孔径/开孔率） | Nichidai | 高 |
| 6 | **实测 SAP 床高**（自由铺放状态）以解决松密度对账缺口（用 STM-00305 / STM-4597 方法） | KC 实验室 | 高 |
| 7 | 定义 land 磨损限值与更换判据 | KC 工艺 + 设备商 | 中 |
| 8 | 确认 **160 gsm sleeve 的 land 高取值** | 设备商 | 中 |
| 9 | 索取 sleeve 加工图与 ID tag 方案 | Nichidai | 中 |

### 13. 依据与红线 Basis & Red Lines

**依据**：One_Drum_Two_Ups_11_Sizes_1000ppm.pptx P4/P8/P9/P15/P16/P18 + notes；WKB〔日本 Nichidai 丝网工艺技术交流〕（丝网规格/卡簧快换/锥度事故/IP 归口）、〔Patterned SAP core 6.pptx〕（Nichidai screen technology 页）、STM-00305 SAM 分布、STM-4597 纸尿裤 SAM 分布测试；本地 references/80、83、85。

**红线（源文五条，照录）**：
1. **全部 sleeve 规格为源文件目标值（B 级）**，非已制造件实测值；**引用须携带等级**。
2. **五处冲突/缺口必须并列呈现，禁止静默取其一**：§4.3(a) land 高口径、§4.3(b) 床高-松密度对账、§6.1 相位精度口径、§5.1 屏规格差异、§7 换装工时分歧。
3. **§8.2 的失效模式覆盖分析与「ID 须逐片唯一」的要求是本次推断**（依据已给出），**未与 PLC 供应商确认**。
4. **磨损限值、锥度防呆方式、ID 技术方案在源文件中均未定义**，本文件已明确标注为待定义项，**不得当作已定方案引用**。
5. **结论不外推到其它 sleeve 架构**（多鼓方案、卡簧快换方案）；外推须显式标注「推断」。

## 与本项目库的关系 Relations

- **母方案**：`[[One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）]]` —— 本件是其 P4/P8/P9/P15/P16/P18 的展开。
- **概念页**：`[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]` —— 本件的 land 体系、屏规格、公差与防错规则是该页"尺寸在套筒"原则的规格化。
- **工具表**：`[[03_卫材产线约束常量表（准入校验工具）]]` —— 本件的床高/松密度对账缺口与常量表 §7 的落料速度匹配条目同源。
- **相关页**：`[[Core Channel Pattern（芯体通道花型设计）]]`（通道成对性）、`[[SAP性能指标（CRC AUL GBP Vortex）]]`（松密度 0.62–0.70 的来源规格）、`[[Nichidai（日丝）]]`（屏规格与锥度事故；⚠️ 库内暂无该实体页，此处为待建引用）。

## 🔴 manual_review（2026-09-29）

- **RFQ 与商务**：源文给出**可直接发给供应商的询价条目**（§11）。本页**只登记条目结构与等级，不落报价、付款、交付、质保等商务条件**；对外发送须走采购流程。
- **专有技术**：**孔径分布与 pattern 细节为 KC 专有技术**，源文要求 NDA 与 IP 申请。本页**保留必要的工程参数**（Ø0.6–0.8 mm、30–40%），但**不页面化完整 pattern 布局与 ID 编码映射**。
- **供应商历史事故**：Nichidai 锥度装反导致 SAP 堵塞为**内部记载的供应商事故**，对外沟通须谨慎。
- **等级纪律**：本件全部规格为 **B 级目标值**；**不得作为验收合同值**。
- **推断项标注**：§8.2 的 ID 唯一性要求、§10.2 关注面、§10.3 归口动作均为**本件推断**，未经供应商确认。

## 存疑 Open Questions（不裁决）

1. **0.45 mm land 高**：全局常量 vs 230 gsm 工况值 —— 判定为后者，**但 160 gsm 取值未给**。
2. **床高反推松密度 0.516–0.523 vs 规格 0.62–0.70** —— **不自洽，差 20–35%**，两种口径并存，须实测床高。
3. **屏规格**：本方案 Ø0.6–0.8 / 30–40% vs Nichidai 六边形 ≥1.4 mm / 60–70–80% —— **差约 2×，并列不合并**。
4. **换装工时**：≤15 min/鼓 vs 30 s 换网 —— **差 30 倍，口径不同，并列**。
5. **相位精度**：±0.02 mm（规格）vs ±0.05 mm（实操） —— **差 2.5 倍，套准公差链关键输入**。
6. **ID 粒度**：源文件只防 ups；**组内尺寸混淆是否可防取决于 ID 粒度**，未确认。

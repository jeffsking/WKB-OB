---
type: source
title: "Patterned SAP Core 6（印花·分区·成形 SAP 芯体开发目标与收益 · 2026-07）"
source_type: 内部技术方案（IPC FEI & OI · 芯体印花/分区开发目标）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/Patterned SAP core 6.pptx.md
original_link: ""
date_published: 2026-07
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "核心原理：SAP 只沉积在有真空的区域（'SAP only allocated on area where has vacuum'），因此可获得任意设计花型的无 SAP 洁净通道；用简单工艺实现复杂花型"
  - "SAP 添加量由风量连续调节：风量越大 SAP 越多、风量越小 SAP 越少——同一套成形鼓即可实现 MD 分区 / CD 分区 / MD+CD 复合分区 / 图案，属 all-in-one 设计"
  - "节材测算：800 PPM、日产 1,152,000 片、设计利用率 75%、年产 311,040,000 片；若单片省 1 g SAP，则单线年省 311 吨 SAP"
  - "真空可控性的来源是'成形风机 + 变频与磁耦合技术 + Nichidai 网技术'；无孔盲区无气流因而无 SAP，气流则由孔径与孔密度差异调节；当前网的最小孔心距 0.14 mm"
  - "COV 的头号机理是 'Particle Sizer Effect'：颗粒密度与风阻差异导致密颗粒飞得更远，破坏目标定量——窄粒径分布（Narrow PSD）SAP 对 COV 远为友好；单鼓 SAP 添加量越小越易控"
  - "HCH 提出的 1200 PPM 方案：双 poly 侧 SAP 计量系统（两种不同溶胀速度的 SAP 以避免凝胶阻塞）+ 150 kg 锤磨机 40 gsm 绒毛浆（约 1.2 g/片，作 MD 分布加速器以增加毛细）+ 第三个鼓用于高装载定点分区；三鼓分摊总定量以改善高速下的 COV"
  - "REL 需与 SAP 图案同形模切以保留通道；但蓬松热风粘合梳理网（TABCW）带来 CD 收缩与张力不稳，模切存在切断质量、修边排废（真空不足）与张力三大问题"
  - "已知工艺 watchout：花型外观保持性、多鼓同步、套准限制、SAP 落料方式（HCH 的 chute/喷管 vs 重力瀑布式落料，后者真空更小、精度更高）"
pages_linked:
  - "IPC BCC OI Portfolio（开放创新项目组合）"
  - "Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）"
  - "SAP Dosing Speed Matching（SAP 落料速度匹配与容差）"
  - "分区密度设计"
  - "Core Channel Pattern（芯体通道花型设计）"
  - "Multilayer SAP Core（多层SAP芯体）"
  - "SAP错峰膨胀"
  - "REL增强层"
---

# Patterned SAP Core 6（印花·分区·成形 SAP 芯体开发目标与收益 · 2026-07）

> 一句话定位：**"SAP 只落在有真空的地方"**——用一条成形鼓 + 可控真空，把**花型、分区、点状装载和洁净通道**做成同一个工艺。（中文：这是把"芯体图案"从**压花/印刷**变成**气流沉积**的方案。）

---

## 摘要 Executive Summary

| 类别 | 内容 |
|---|---|
| **核心原理** | **SAP 只沉积在有真空的区域** → 任意设计花型下都能得到**无 SAP 的洁净通道** |
| **添加量调节** | **风量越大 SAP 越多，风量越小 SAP 越少**（连续可调，非开关） |
| **All-in-one 能力** | **MD 分区 / CD 分区 / MD+CD 复合分区 / 图案**，同一套系统全覆盖 |
| **节材测算** | **单片省 1 g SAP ⇒ 单线年省 311 吨**（800 PPM、年产 3.1104 亿片） |
| **真空可控来源** | 成形风机 **+ 变频与磁耦合技术 + Nichidai 网技术** |
| **COV 头号机理** | **Particle Sizer Effect**（颗粒密度/风阻差异 ⇒ 飞行距离不同 ⇒ 定量跑偏） |
| **出处** | **IPC FEI & OI**，2026 年 7 月 |

---

## 提炼的数字与结论 Numbers & Conclusions

### 1. 节材测算表（源文原表，逐格直引）

| 项目 | 数值 |
|---|---|
| 机速 (PPM) | **800** |
| 日产 (片) | **1,152,000** |
| 设计利用率 | **75%** |
| 年产量（片） | **311,040,000** |
| **单片 SAP 节省 (g)** | **1** |
| **单线年节省 SAP (吨)** | **311** |

> ⚠️ 这是**敏感度测算**（"每片省 1 g 会怎样"），**不是已实现的节省**；**1 g 是输入假设，不是实测**。

### 2. 图案成形工艺：成形鼓 + 真空

**五条工艺原理（源文明写）：**
1. **All-in-one 设计** —— 无 pocket frame、无分段，**开孔面积更大**；
2. **无孔的盲区无气流 ⇒ 成形时该处无 SAP**；
3. **气流可通过孔径与孔密度的差异来调节**；
4. **按设计定制花型**；
5. **（风量足够大时）可做 pocket 式定点分区**。

**真空的来源**：**成形风机 + 变频（inverter）与磁耦合（magnetic coupling）技术 + Nichidai 网技术** ⇒ **可控真空**。

**网（screen）的能力与限制：**
- **当前能力下的最小孔心距：0.14 mm**；
- 工艺路线：**支撑蚀刻（Support Etching）**、**多层层压蚀刻网（Multi-layer laminated etching screen）**；
- 与 **Innovent 带框网**的差别：**本方案开孔面积更大**（more open area）。

### 3. 中试线能力（Chuanyue 演示线 · KC 天津试验平台）

- **本地中国供应商 Chuanyue** 交付了一条演示线，基于**成形鼓技术**，**运行速度 100 m/min**，可制作印花 SAP 芯体（KC 天津测试平台）。
- Chuanyue **自建常规网（类似 Innovent）+ 自设计成形鼓**，**不掌握 Nichidai 网技术**。

| 中试线指标 | 数值 |
|---|---|
| 机速 | **100 m/min** |
| 单层 SAM 喂入定量范围 | **50–300 gsm** |
| SAM 喂入喷洒宽度 | **50–280 mm**（另一处图注写 **70–280 mm** ⚠️ 不一致，登记） |
| **SAM 喂入精度** | **±2.5%** |

### 4. HCH 的 1200 PPM 印花芯体工艺方案

| 单元 | 内容 |
|---|---|
| **Poly 侧成形鼓（N）** | 真空分区；**每个鼓内各真空段与各段真空压力可在环内（in-loop）实时调节**，由 **SAP 重量传感器 + 压力传感器**支持，靠**独立成形风机系统的磁耦合与变频技术**实现 |
| **A：双 poly 侧 SAP 计量系统** | 允许**两种 SAP** 同时添加，**溶胀速度不同以规避凝胶阻塞（hydro-gel blocking）** |
| **D/B：150 kg 锤磨机** | **40 gsm 绒毛浆添加，约 1.2 g/片**，位于 poly 侧，作为 **MD 分布加速器（增加毛细）** |
| **O：liner 侧成形鼓真空** | H 高真空 / S 持续真空 / **R 真空释放 = 零** |
| **A1：额外计量系统** | 预留**功能性颗粒**添加：**BM/尿液气味控制**，或 **PCM 调温** |
| **基材包裹** | **PSN 或 LSN 包在鼓外**承接 SAP 落料 |

### 5. 三鼓方案（HCH）与其逻辑

- **原始理念**：**固定整片 SAP 总定量**，同步工序确定后**每个鼓分到的 SAM 更少 ⇒ 气流系统精度更容易保证 ⇒ 高速下 COV 改善**。
- 若要做 **沙漏型（sandglass）芯体设计**，在**流线化总 SAP 定量**的前提下，**MD + CD 分区是必需的**。
- **第三个鼓**可专门用于**需要高装载的定点分区**。
- **KC 侧的取舍**：需要设计 web path，把结构保持在**最简 —— 仅 LSN + SAP1 + REL + SAP2/SAP3 + PSN**。

### 6. COV 焦点：Particle Sizer Effect

- **机理**：**颗粒在密度与风阻上存在差异 ⇒ 较密的颗粒飞得更远 ⇒ 破坏目标定量**。
- **两条对策（源文明写）**：
  1. **窄粒径分布（Narrow PSD）SAP 对工艺控制 COV 友好得多**；
  2. **高速印花成形下，每个鼓的 SAP 添加量越小，越容易控制 SAM 重量偏差**（相对重添加）。

### 7. 定点分区：3D 成形网

| 要素 | 规格 |
|---|---|
| 覆盖材料 | 非织造网，用于封闭结构 |
| 颗粒材料 | **SAP 簇，精确计量，粒径 10–1000 µm** |
| 载体材料 | **SMS / SMMS 非织造，高延伸性（MD/CD 延伸率 >20%，最高 200%）** 以允许**深 pocket 成形** |
| 工序 A | 喷嘴（495）将**白胶细雾**只喷在 **pocket 网中平坦、无颗粒、由针支撑的区域** |
| 工序 B | 平坦半透明白色覆盖网（330）**切向汇入** |
| 工序 C | 覆盖网压紧涂胶的针支撑载体网，**颗粒被锁在密封 pocket 内** |

### 8. REL 与图案模切

**REL 的作用**：提升 **100% SAP 芯体的 pad integrity**，并改善**手感柔软度**；主要材质为 **COPET/PET ES 与 PE/PET 中空 ES**，经**热风粘合（air-through bonded）＋耐久亲水处理**。

**同形模切的收益**：印花 SAP **理想上应在 REL 上有同图案的模切**，以**保留通道用于尿液分布 + 提升透气 + 提供视觉线索 + 便于 LSN/PSN 的通道压花**。

**但高速加工下图案模切有三个问题（源文明写）：**
1. **切断质量**（因纤维蓬松）；
2. **修边排废问题**（因纤维间孔隙导致真空不足）；
3. **CD 收缩与模切前后的走带张力控制**。
- **未决**：双调速真空辊/输送带**能否抵消张力偏差，效果未知**。
- **蓬松 TABCW 的固有代价**：**孔隙率更高、纤维间结合点更少 ⇒ CD 收缩、高速加工时张力不稳**。

### 9. 其他工艺 watchout

- **花型外观**：高速工艺能否保持良好外观；
- **多成形鼓之间的同步问题**；
- **套准（registration）限制**；
- **SAP 落料工艺需核查**：
  1. **HCH 提出的 SAP chute / 喷管（nozzle tube）**（类似绒毛浆/SAP 成形，但印花成形需要**更大的真空**）的表现；
  2. **poly 侧最多 40 gsm 绒毛浆 + SAP 的印花成形是否可靠**；
  3. **考虑用 SAP 重力瀑布式落料（gravity drop waterfall）取代 chute/喷管**，用于 100% SAP 印花成形 —— **真空更小、精度更高**。

### 10. 尿液 MD 分布（KC 侧设计输入）

- **前部峰值不在正中**：**婴儿尿液在芯体中点之前进入，随后经 ADL 与绒毛浆/SAP 网络向后铺展**。
- 图注可辨读的分段（**部分不可辨读，见 manual_review**）：**前部 0–30% ≈ 8%**、**裆前 30–55% ≈ 35%**、**裆后 70–80% ≈ 13%**、**后段 ≈ 6%**。

---

## 关键论断 Key Claims

1. **图案芯体的第一性原理是"真空即模板"** —— 有孔有风就有 SAP，无孔无风就无 SAP；**花型不再是压出来的，而是"没落上去"的**。这使**洁净通道与复杂花型同时可得**，且无需分段式 pocket 结构。
2. **"风量调定量"把分区变成连续量而非离散档** —— MD / CD / 复合 / 图案四种能力共用一套执行机构；**分区 know-how 落在风量分布与孔型设计上**，而非机械换型。
3. **节材量级值得单独立项** —— **每片 1 g** 在 800 PPM、75% 利用率下就是**单线每年 311 吨**；**这是把"少放一点 SAP"从成本控制项提升为结构创新收益项的关键换算**。
4. **COV 的真正敌人是颗粒本身的不均一** —— Particle Sizer Effect 说明**定量偏差不是设备精度问题，而是颗粒密度/风阻分布问题**；**窄 PSD 是材料侧的 COV 解法**，与设备侧的"少放一点/多鼓分摊"并列。
5. **"多鼓分摊"是高速化的结构性解法** —— 总定量固定下把 SAP 分到 2–3 个鼓，**每个鼓的添加量变小 ⇒ 气流精度更容易保证 ⇒ COV 改善**；**这是用并行化换取单点精度**。
6. **两种 SAP 错峰溶胀被写进设备方案** —— 双计量系统的目的明确是**不同溶胀速度以避免凝胶阻塞**；**设备能力直接服务于吸收机理**（与 [[SAP错峰膨胀]] 同源）。
7. **少量绒毛浆被重新定位为"MD 分布加速器"** —— 在 100% SAP 芯体里仍保留 **~1.2 g/片（40 gsm）** 绒毛浆，**作用不是吸收而是增加毛细通道**；**"去绒毛浆"不等于"零绒毛浆"**。
8. **REL 与 SAP 图案必须同形，但这正是工艺难点** —— 蓬松热风粘合材料**模切质量差、修边排废难、CD 收缩与张力不稳**；**结构收益（通道/透气/视觉）与加工可行性在此正面冲突**。
9. **供应商能力存在明显分层** —— 本地 Chuanyue 能做 **100 m/min** 演示线，但**用的是类 Innovent 常规网、不掌握 Nichidai 网技术**；**"能做出图案"与"能高速稳定地做出图案"是两代能力**。
10. **落料方式是尚未收敛的岔路** —— chute/喷管（需更大真空）vs **重力瀑布式（更小真空、更高精度）**；**这条选择直接决定 100% SAP 图案成形能否跑高速**。

---

## 关联页面 Related Pages

- [[IPC BCC OI Portfolio（开放创新项目组合）]] —— 本方案署名为 **IPC FEI & OI（2026-07）**，属**开放创新/前瞻工程**产物；**具体的 OI 编号未在本源中标注**，故本页不指定编号（OI 编号基准见该页重构版 19 项）。
- [[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]] —— 本源是该概念页的**工艺原理与产业能力来源**（真空即模板、孔心距 0.14 mm、多鼓同步）。
- [[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]] —— "Particle Sizer Effect"与 ±2.5% 喂入精度是**落料计量一致性的直接输入**。
- [[分区密度设计]] —— MD/CD 分区与沙漏型设计；本源给出**分区的执行机构解法（风量）**。
- [[Core Channel Pattern（芯体通道花型设计）]] —— 洁净通道的四重收益（尿液分布 / 透气 / 视觉线索 / 便于 LSN·PSN 压花）。
- [[Multilayer SAP Core（多层SAP芯体）]] —— 双 SAP 错峰溶胀 + 少量绒毛浆作分布加速器的分层逻辑。
- [[SAP错峰膨胀]] —— 两种不同溶胀速度 SAP 规避凝胶阻塞的机理。
- [[REL增强层]] —— REL 材质（COPET/PET ES、PE/PET 中空 ES、热风粘合 + 耐久亲水）与模切问题。

---

## 原文 Raw Excerpt

> **原理原文**：「Build up clean channels with any designed pattern free from SAP —— **SAP only allocated on area where has vacuum**」「Flexible in complicated pattern SAP design with simple process」
>
> **定量调节原文**：「SAP add on in certain area can be controlled and adjusted by the air flow volume: **More air flow leads to more SAP, less air flow results in less SAP**」
>
> **真空来源原文**：「Forming Fan with invertor & magnetic coupling technology + **Nichidai screen technology**, source of controllable vacuum」
>
> **Particle Sizer 原文**：「Granules vary in density and air-resistance. **Denser particles travel further than lighter ones, destroying targeted basis weights.**」「**Narrow PSD SAP is much friendly for process to control COV**」
>
> **双 SAP 原文**：「Enable two SAP types add on for absorbency with **different swollen speed to avoid Hydro-gel blocks**」
>
> **绒毛浆定位原文**：「150kg hammer mill for 40 gsm fluff add on, roughly **1.2 gram fluff per pad at poly side for MD distribution accelerator (increasing capillaries)**」
>
> **落料岔路原文**：「Considering the **SAP gravity drop waterfall** to replace SAP chute/Nozzle tube for 100% SAP pattern forming with **less vacuum and higher precision**」

---

> 🔴 **manual_review（2026-09-29）**：
> 1. **供应商与技术来源信息** —— 源文点名 **Nichidai（网技术）、Innovent（带框网）、Chuanyue（本国演示线）、HCH（1200 PPM 方案提供方）**。本页**只记录技术能力事实**（速度、精度、是否掌握某项网技术），**不涉及任何报价、合同条款或未公开合作方约定**；**Chuanyue 是否可作为供应源属商务判断，本页不作结论**。
> 2. **节材测算为敏感度假设** —— 311 吨/年对应**"单片省 1 g"的假设输入**，**非实测节省**；引用时必须连同假设一起给出。
> 3. ⚠️ **源文内部不一致（登记，不修正）** —— SAM 喂入喷洒宽度一处写 **50–280 mm**、另一处图注写 **70–280 mm**。
> 4. ⚠️ **尿液 MD 分布图不可完整辨读** —— 图注已退化为文本，本页只列出**可明确辨读的分段**（8% / 35% / 13% / 6%），**中间 55–70% 段数值缺失**，**未臆测**；需用时回原图核对。
> 5. **未决项不得当作结论** —— 双调速真空辊能否抵消张力偏差、重力瀑布式落料是否可靠、多鼓同步与套准，**源文均标注为待验证/watchout**。
> 6. **OI 编号未在源文中出现** —— 本页不自行指派 OI 编号。

> ✅ 验证（2026-09-29）：本页为新 source 页，无既有结论被覆盖；所有数字直引源文，未做换算或外推。

---
type: source
title: "SAP Dosing Speed Matching & Tolerance Spec（SAP 落料速度匹配与容差规范）"
source_type: 内部工程规范（派生编号 86）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/86-SAP落料速度匹配与容差规范.md.md
original_link: ""
date_published: 2026-09-22
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "The #1 failure mode is 'Chute speed left at the other ups' — a recipe item, not a hardware item: a wrong chute setting produces NO mechanical alarm and shows up only as degraded SAP-pattern edge quality, so the chute↔ups binding must be recipe-locked in the control system（头号失效模式是"chute 速度留在另一个 ups 上"：属 recipe 项而非硬件项，改错不产生机械报警，只表现为图案边缘变差，因此必须在控制系统层面强制联动）"
  - "Drum line speed v [m/s] = drum pitch P [mm] × ppm / 60 000; at 1 000 ppm, 6-up (P = 461.8 mm) → 7.70 m/s and 7-up (P = 395.8 mm) → 6.60 m/s, i.e. Δv = 1.10 m/s — matching the source statement that a chute tuned for 6-up overshoots by 1.1 m/s（鼓面线速换算与两 ups 的 1.10 m/s 速度差）"
  - "Target is SAP ARRIVAL speed at the drum of 6.60 or 7.70 m/s with ±0.3 m/s tolerance (±4.5% for 7-up, ±3.9% for 6-up); what is locked in the recipe is the eductor setpoint, but what must be controlled is arrival speed — and the mapping between them is NOT given by the source（目标为"到达速度"而非 eductor 供气压力；两者映射源文未给，是最重要的缺口）"
  - "Simulated consequence of mismatch: SAP placement in-spec collapses from 99.996% to 92.7% (−7.3 percentage points); this is SAP placement in-spec, NOT mechanical registration in-spec (which is governed by Cpk) — the two must never be conflated（失配后果：SAP 落点 in-spec 由 99.996% 塌到 92.7%；该指标与套准机械 in-spec 是不同指标，禁止混引）"
  - "Slip model: s = Δv² / (2a), a = μ·Δp·A/m, with μ = 0.5, d = 450 µm, ρ = 1.5 g/cm³ giving A/m = 2.222 m²/kg and a = 1.111·Δp; hence s = 0.5446/Δp [m] — but Δp's definition is undefined, so the table cannot converge（滑移模型与复算；Δp 口径未定义是唯一阻塞）"
  - "Derived design criterion: requiring slip ≤1 mm gives Δp_req ≥ 545 Pa; since forming-zone vacuum is −8…−12 kPa (far above), slip is fully constrained once SAP lands inside the forming sector — so the dominant harm of mismatch is phase misalignment at arrival, not slip after landing（推断判据：滑移被真空充分约束，失配的主要危害是到达时刻的相位错位）"
  - "Slip distance scales with particle size and density (s ∝ d·ρ): within the specified PSD of 150–710 µm, the 710 µm fraction slips 4.8× the 150 µm fraction — a physical explanation for why D50 must be held at 350–450 µm with a controlled span, and why 'finer is not automatically better'（滑移与粒径/密度成正比：粗颗粒滑移是细颗粒的 4.8 倍——这解释了 D50 与跨度受控的物理原因，且细粉问题在于穿透与粘附、粗颗粒问题在于滑移）"
  - "Placement efficiency: phase-locked rotary valve pulses ~90% vs continuous full-width curtain ~50% (both explicitly 'geometric estimates', not measured); and placement efficiency must NOT be converted directly into SAP cost because strays return via cyclone with fines removal and neither recycle rate nor fines generation rate is given（落点效率 90% vs 50% 为几何估计；且不可直接换算成成本差——回用率与细粉产生率缺失）"
  - "Rotary valve pulse frequency = ppm/60 and is independent of ups (16.7 Hz at 1 000 ppm both for 6-up and 7-up) — therefore what changes with ups is arrival speed, not the valve pulse setting; this explains why the recipe item to re-set is the chute, not the valve（转阀脉冲频率 = ppm/60，与 ups 无关）"
  - "A proposed SAP 'process manufacturability' parameter set (targets for supplier discussion, NOT measured data): PSD 150–710 µm / D50 350–450 µm; fines <150 µm ≤2%; irregular gel-crushed shape; bulk density 0.62–0.70 g/cm³ with batch CV ≤1%; flowability ≥10 g/s; moisture 3–6%; CRC/AAP 0.7 psi 26–30 / ≥22 g/g; SFC ≥80 ×10⁻⁷ cm³·s/g; throughput 270–700 kg/h/drum（SAP 工艺可制造性参数表——全部为待与供应商讨论的目标值，非实测）"
  - "Two internal inconsistencies found: (a) bed heights stated by the source (0.31 mm @160 gsm, 0.44 mm @230 gsm) back-calculate to ~0.52 g/cm³, below the 0.62–0.70 bulk-density spec (a reconciliation gap); (b) flowability ≥10 g/s vs single-drum throughput 74.7–193.3 g/s differ by 7.5–19×, so the test method behind '≥10 g/s' must be clarified（两处内部不自洽：床高反推松密度低于规格；流动性规格与吞吐相差 7.5–19 倍）"
pages_linked: ["[[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]", "[[Core Channel Pattern（芯体通道花型设计）]]", "[[SAP性能指标（CRC AUL GBP Vortex）]]", "[[SAM Testing Methods（超级吸水材料测试方法）]]", "[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]", "[[IPC BCC OI Portfolio（开放创新项目组合）]]"]
---

# SAP Dosing Speed Matching & Tolerance Spec（SAP 落料速度匹配与容差规范）

> 一句话定位：一份 **2026-09-22 的内部工程规范（派生编号 86）**，针对 **"SAP 落料速度（chute）与成型鼓面线速（ups）不匹配"** 这一头号失效模式，给出**线速换算、允差、滑移模型、标定方法提案、落点效率口径与 SAP 工艺可制造性参数表**。（中文：把"配方里那个不能单独改的速度项"讲清楚——为什么必须随 ups 重设、失配会怎样、以及还缺什么。）

> ⚠️ **来源性质（2026-09-29）**：本文件为**内部派生工程笔记**，自述由"纸尿裤全栈设计专家（CoreCraft）"生成；其**原始数据来自内部 pptx（One_Drum_Two_Ups_11_Sizes_1000ppm）与既有笔记**，文中**大量结论标注为"推断/本次发现/提案"并分级（B 级仿真结论、C 级目标值）**。credibility 定为**中**：**机理与口径可用，数值须实测或向设备商确认**。

## 原文要点 Original Key Points

### 1. 为什么这是头号失效模式

源文 P18「Top risks and mitigations」第 1 条：风险 **"Chute speed left at the other ups"**；对策 **"recipe-locked eductor setpoint; alarm on SAP-edge camera metric"**。

| # | 理由 |
|---|---|
| 1 | **它是 recipe 项，不是硬件项**——ups/cams/fan/glue/chute 五项 recipe 中，ups 改错会立刻影响节拍（易发现），**chute 改错不产生任何机械报警**，只表现为 pattern 边缘变差 |
| 2 | **失配不表现为"故障"，只表现为"质量下降"**——需靠图像分析的 **SAP 边缘锐度**这一间接指标发现，故必须设自动报警 |
| 3 | 两 ups 的线速差异只有 **17%**，看似不大，但**对应的位移量级恰好落在公差边界附近** |
| 4 | 仿真给出的后果是**断崖式**的——in-spec 从 99.996% 塌到 92.7% |

> **推论**：**chute 速度与 ups 的绑定必须在控制系统层面强制（recipe-locked），不能依赖操作纪律。**

### 2. 鼓面线速换算

- **公式**：`v [m/s] = 鼓距 P [mm] × ppm / 60 000`；`v [m/min] = P [mm] × ppm / 1 000`。
- **6-up**：P = 461.80 mm → **7.70 m/s**（461.8 × 1000 / 60000 = 7.697 ✓）
- **7-up**：P = 395.83 mm → **6.60 m/s**（395.8 × 1000 / 60000 = 6.597 ✓），相对 6-up 为 **−14.3%（线速）/ −16.7%（转速）**
- **速度差 Δv = 1.10 m/s** —— 与源文 P13「a chute tuned for 6-up then overshoots by 1.1 m/s」一致 ✓

### 3. 允差与失配后果

| 项 | 值 |
|---|---|
| 目标到达速度 | **6.60 或 7.70 m/s**（随 ups 切换） |
| 允差 | **±0.3 m/s**（±4.5% @7-up / ±3.9% @6-up） |
| 正常（chute 随 ups 重设） | **99.996%** |
| 失配（chute 沿用另一 ups） | **92.7%** |
| 退化量 | **−7.3 个百分点**（废品率约放大 1.8×10⁴ 倍） |

> ⚠️ **口径区分（源文红线）**：**99.996% → 92.7% 是 SAP 落点 in-spec 率，不是套准机械 in-spec 率**（后者由 Cpk 决定）。**二者是不同指标，禁止混引。**

> ⚠️ **不可独立复算**：源文给出了 Δv = 1.1 m/s、滑移模型与结果，**但未给出 Δp 的口径、飞行时间、以及位移分布如何映射为 in-spec 率**。因此 92.7% **只能作为仿真结论引用（B 级）**，须向设备商索取仿真模型输入参数表。

### 4. 滑移模型与颗粒敏感性

**模型（源文 P13 原文）**：`s = Δv² / (2a)`；`a = μ · Δp · A / m`；参数 μ = 0.5、d = 450 µm、ρ = 1.5 g/cm³。

**本次复算**：m = 7.158×10⁻⁸ kg；A = 1.5904×10⁻⁷ m²；**A/m = 2.222 m²/kg**；**a = 1.111·Δp [m/s²]**（Δp 以 Pa 计）；代入 Δv = 1.1 → **s = 0.5446 / Δp [m]**。

| Δp | 滑移 s | 判读 |
|---|---|---|
| 100 Pa | 5.4 mm | 大于通道特征尺寸（~5 mm）→ **边缘完全糊掉** |
| **545 Pa** | **1.0 mm** | 与公差同量级 |
| 1 000 Pa | 0.54 mm | 与 │CD│ 公差同量级 |
| 5 000 Pa | 0.11 mm | 可忽略 |
| 10 000 Pa（成型区真空 −8…−12 kPa 量级） | 0.054 mm | **完全约束** |

> **推断判据（源文标注为"推断"）**：若要求 **s ≤ 1 mm**，则 **Δp_req ≥ 545 Pa**。成型区真空（−8…−12 kPa）**远超此值** → **只要 SAP 落点在成型扇区内，滑移即被充分约束**；**失配的主要危害应来自到达时刻的相位错位**（影响 SAP 是否落在有真空的 pocket 上），**而非落点后的滑移**。

**颗粒敏感性（推断）**：由 a ∝ A/m ∝ 1/(d·ρ) 得 **s ∝ d·ρ**——**滑移距离与颗粒直径、密度成正比**。

| 粒径 | 相对滑移 s/s(450 µm) | 影响 |
|---|---|---|
| 150 µm（细粉下限） | **0.33×** | 滑移最小，**利于边缘锐度** |
| 350 µm（D50 下限） | 0.78× | — |
| 450 µm（基准） | 1.00× | — |
| 550 µm | 1.22× | — |
| **710 µm（上限）** | **1.58×** | 滑移最大，**大颗粒侧的边缘风险** |

> **本条价值**：把 **PSD 规格（150–710 µm，D50 350–450 µm）与边缘锐度建立了定量联系**——同一批 SAP 内**粗颗粒的滑移是细颗粒的 4.8 倍**（710/150）。
> **一致性检查（源文自查）**：源文同时要求"细粉 ≤2%"（细粉会穿透无纺布、堵屏、粘附端区 land）与"粒径上限 710 µm"。**二者不矛盾**：**细粉的问题是穿透与粘附，粗颗粒的问题是滑移** → 需要**受控的跨度**，而非"越细越好"。

### 5. 标定方法（本次提案，源文未给出）

**S1–S4 直接标定**：离线试验台固定 chute 几何与 eductor 气压，用**高速相机 / PIV** 测粒子通过鼓面切面处的速度 → 得到 `p_air → v_arrive` 映射曲线；在**两鼓速（396 / 462 m/min）下分别标定**；写入 recipe 的 chute 项并设上下限报警；随 SAP 批号变更定期复标。

> **为什么必须两条曲线**：鼓面高速运动拖动空气（**伴随流**），**SAP 到达速度不可能与鼓速无关**——**不能用一条曲线覆盖两个 ups**。这从机理上解释了"chute 必须随 ups 重设"。

**间接在线判据（兜底）**：**SAP 边缘锐度**（图像分析）与**端区/通道的 stray SAP 量**；源文 P18 的对策明确要求 **"alarm on SAP-edge camera metric"**，但**报警阈值未定义**（属 G20 的 K7 缺口）。

> ⚠️ **外推限制**：候选标定平台（Chuanyue demo 线）为 **100 m/min 级**，而目标鼓面线速 **396–462 m/min（4–4.6×）**。**demo 线的标定结果不能直接外推到产线速度**（伴随流与颗粒阻力与速度非线性相关），**必须在目标速度下复标**。

### 6. 落点效率与 SAP 回用（副交付 G9）

| 供料方式 | 落点效率 | 机理 |
|---|---|---|
| **伺服转阀相锁（phase-locked pulses, n pulses/rev）** | **~90%** | 脉冲与 pocket 相位锁死，只在有真空的位置出料 |
| **连续全幅帘幕（continuous full-width curtain）** | **~50%** | 全幅出料，仅落到有真空 pocket 的部分被留住 |

> **等级**：源文自述为 **"geometric estimates for M 7-up"（几何估计值，非实测），C 级**。

> ⚠️ **落点效率 ≠ SAP 单耗（源文澄清，防误用）**：stray 从端区与通道**经旋风分离器（cyclone）除细粉后回用**。
> `净单耗 = 理论单耗 / (落点效率 + (1 − 落点效率) × 回用率 × (1 − 细粉损失率))`
> 若回用率 100% 且细粉损失 0 → **落点效率对净单耗无影响**；实际差异来自 (a) 细粉产生量、(b) **回用 SAP 的性能衰减**、(c) 回用回路的能耗与资本。
> **结论：不能把"90% vs 50%"直接换算成 2 倍 SAP 成本差异**——正确的论证是"转阀相锁降低细粉产生与回用负荷"。源文**未给出回用率与细粉产生率**，故 **BOM 影响目前无法闭合**。

**细粉分离门槛**：**<150 µm**，与 SAP 规格「Fines <150 µm ≤2%」一致 ✓；分离设备为**旋风分离器**。
> **推断**：150 µm 由 **SAP 规格定义**（fines 上限口径），**而非由分离设备能力定义** → **SAP 供应商若变更 fines 定义口径，回用回路的分离门槛须同步调整**（易被忽略的耦合项）。

### 7. SAP 工艺可制造性参数（副交付 G10，待并入 SAP 数据库）

> **缺口性质**：现有 SAP 数据库列全部是**吸收性能维度**（CRC / AUL(0.7 psi) / 吸液速度 / GBP / 30–50 目 / 角色定位），**无任何工艺维度** → 会导致"吸收性能最好的 SAP 可能是成型最差的 SAP"。

| 参数 | 目标 | 源文理由 | 补充机理 |
|---|---|---|---|
| **粒径** | 150–710 µm，**D50 350–450 µm** | 在 396 与 462 m/min 下均获得锐利边缘 | `s ∝ d`；710 µm 的滑移是 150 µm 的 **4.8×** |
| **细粉（<150 µm）** | **≤2%** | 穿透无纺布、堵屏、粘附端区 land | 细粉滑移小（0.33×）**不损害边缘**；危害在穿透（孔径 <100 µm）、堵塞屏（Ø0.6–0.8 mm）、粘附端区 |
| **形状** | **不规则（gel-crushed）** | 抗落点后滚动 | 球形颗粒落地后**滚动**，等效滑移远超滑动模型；不规则形状靠棱角咬合抑制滚动 |
| **松密度** | 0.62–0.70 g/cm³，**批间 CV ≤1%** | 床高须匹配 land 高（0.31 mm @160 gsm；**0.44 mm @230 gsm**） | ⚠️ 见下"余量不足" |
| **流动性** | **≥10 g/s**，抗结块 | 转阀在 **16.7 pulses/s**（1 000 ppm）下干净充填 | ⚠️ 见下"口径疑问" |
| **含水** | **3–6%** | 减少静电 → land 与端区更干净 | 过低→静电粘附；过高→结块、流动性下降。**3–6% 是静电与流动性的折中** |
| **CRC / AAP 0.7 psi** | 26–30 / ≥22 g/g | 无绒架构下吸收性能全由 SAP 承担 | — |
| **渗透率 SFC** | **≥80 ×10⁻⁷ cm³·s/g** | 无凝胶阻塞，湿态保持通道开孔 | 与通道设计呼应 |
| **吞吐** | **270–700 kg/h/鼓** | 覆盖 160 gsm → pants XXXXL 230 gsm | 74.7–193.3 g/s |

> **等级**：源文自述 **"Targets for supplier discussion, not measured data"**（待与供应商讨论的目标值，C 级）；**合格判据是"在两种鼓速下的床边缘锐度（图像分析）"** → 即**验收方法又回到 §5.2 那个尚未定义的图像分析算法**。这是 G8 / G10 / G20 **三者的共同卡点**。

### 8. 三项推导 / 发现（源文均标注为"推断"）

**8.1 转阀脉冲频率的 ups 不变性**：`脉冲频率 = (转速 rpm/60) × (脉冲数/转) = (ppm/n/60) × n = ppm/60` → 6-up（166.7 rpm × 6）与 7-up（142.9 rpm × 7）**均为 16.7 Hz**。
> 推论：**脉冲频率与 ups 无关**（恒为 ppm/60）；**随 ups 变化的只有到达速度** → 这解释了 **recipe 需要重设的是 chute（速度）而非阀的脉冲设定**。

**8.2 松密度 CV 与"land ≥ 床高"余量不足**：源文床高 0.31 mm @160 gsm 与 0.44 mm @230 gsm **反推 ρ_bed ≈ 0.516 / 0.523 g/cm³**，**低于松密度规格下限 0.62（差 16–17%）**（该对账缺口另记于 84 §3.3(b)）。
> 以床高 0.44 mm、land 高 0.45 mm 计：**余量仅 0.01 mm（2.2%）**；松密度批间 CV 1% → 床高波动 ±1%（1σ），**约 2.3σ 即触及 land 高，双侧越界概率 ≈2.1%**。即 **约 1–2% 的 SAP 批次可能出现"床高 ≥ land 高"** → 对压时 SAP 床先于 land 接触 → 违反 land-to-land 设计意图 → 套准与通道质量同时恶化。
> **三条处置路径**：① 收紧 CV ≤0.73%；② land 高按床高 +5% 设定（≈0.462 mm）；③ 按批实测松密度调整 recipe。
> ⚠️ **前置条件**：本条完全依赖"床高 vs 松密度"的对账结论；**若实际 ρ_bed 落在 0.62–0.70，则床高更薄、余量充足（>20%），本条风险不存在** → **必须先实测自由铺放床高再决定是否处置**。

**8.3 流动性口径疑问**：规格 **≥10 g/s** vs 单鼓吞吐 **74.7–193.3 g/s**，**相差 7.5–19 倍**。若 ≥10 g/s 是整机供料能力则严重不匹配；若是标准流动性测试读数则须注明方法。**须澄清测试方法**（是否指定漏斗孔径、是否含振动、是否在指定含水下测）。

### 9. 待闭环行动项（源文 §9，共 10 项）

1. 澄清 Nichidai 行动项 #9：**下落速度/密度的定义口径**（最高，已挂账多时，G8 正式归口）
2. **定义 SAP 边缘锐度的图像分析算法与报警阈值**（最高，G8 + G20 K7）
3. 索取 **chute/eductor 的到达速度—气压标定曲线（两 ups 各一条）**（高）
4. 索取**仿真模型输入参数表**（Δp 口径、飞行时间、位移分布 → in-spec 映射）（高）
5. **实测自由铺放床高**（解决松密度对账缺口）（高）
6. 澄清**流动性 ≥10 g/s 的测试方法**（中）
7. 索取**回用率与细粉产生率**（闭合 BOM 影响）（中）
8. 向 SAP 供应商索取**工艺参数列**填入数据库（中）
9. 澄清 **demo 线（100 m/min）到产线速度（4–4.6×）的外推方法**（中）
10. 确认 **chute recipe 项的强制联动**在控制系统中如何实现（不可单独编辑）（中）

> 🔴 **manual_review（2026-09-29）**：本源为**内部工程规范**，含① **设备商与供应商名称**（Chuanyue、Nichidai、chute/eductor 供应商、视觉供应商）与其能力口径——属供应与商务信息，本页仅记**技术判据与待澄清问题**，不页面化具体商务条款与报价；② **SAP 牌号**（KC511 / 610S / 950 等）仅作为"需补工艺参数列"的对象记存在；③ **BOM 成本结构引用**（源文称 SAP 占 BOM 35–50%，为最大单项）属**内部成本结构**，本页**只记"SAP 是最大单项、回用率 1% 的变化都值得量化"这一相对判断，不落占比数值**；④ 本文件大量结论标注为**推断/提案**，引用时须带上等级标注。

## 与库内页面的关系 Relations

- 核心概念：[[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]
- 结构：[[Core Channel Pattern（芯体通道花型设计）]]
- 指标口径：[[SAP性能指标（CRC AUL GBP Vortex）]]、[[SAM Testing Methods（超级吸水材料测试方法）]]
- 平台：[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]
- 项目组合：[[IPC BCC OI Portfolio（开放创新项目组合）]]

## 存疑 / 待人工确认 Open Questions

1. **Δp 口径未定义**——滑移表无法收敛为单一结论的唯一原因；因此 **Δp_req ≥545 Pa 与"滑移被真空充分约束"均为推断**，须由设备商确认后重算。
2. **92.7% 不可独立复算**（无 Δp 口径、飞行时间与位移分布映射），只能作仿真结论引用。
3. **落点效率 90% / 50% 为几何估计**，且**不可换算为成本倍数**（回用率与细粉产生率缺失）。
4. **床高 vs 松密度不自洽**（反推 ~0.52 vs 规格 0.62–0.70）——**在该对账缺口解决前，不得据此要求供应商收紧 CV**。
5. **流动性 ≥10 g/s 与吞吐 74.7–193.3 g/s 相差 7.5–19 倍**——测试方法待澄清，**不断定源文有误**。
6. **SAP 工艺参数表全部为"待与供应商讨论的目标值"**，非实测；其合格判据（图像分析算法）**本身尚未定义**。
7. 本源为**派生工程笔记**（编号 86，引用 80/81/84/85/02/22/74 等内部 references），其引用的原始 pptx **不在本批内**，本页**不代为回溯原始来源**。

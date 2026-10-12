---
type: source
title: "One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）"
source_type: 设备方案 / 工程概念（DEEP DIVE）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/One_Drum_Two_Ups_11_Sizes_1000ppm.pptx.md
original_link: ""
date_published: "[待验证]（文件无日期；为本库 86 号工程规范的原始来源 pptx）"
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "Concept: ONE Ø882 mm drum body running BOTH 6-up and 7-up sleeve families, printing skin-side and poly-side pattern-SAP for 6 open-diaper and 5 pants sizes at a fixed 1,000 ppm, with registration held through every grade change; simulated in-spec registration ≥99.99%（概念：单一 Ø882 mm 鼓体配 6-up 与 7-up 两套套筒族，在固定 1000 ppm 下为 6 个开放式纸尿裤码 + 5 个裤型码双面印花 SAP，仿真套准合格率 ≥99.99%）"
  - "The size problem is a 140 mm spread in core length (280–420 mm, longest 1.5× shortest) with 7 distinct lengths and 3 widths (100/110/120 mm handled in CD, not by ups); because drum pitch P = πD/n, the ONLY lever at fixed ppm and one diameter is the number of cores per revolution（尺寸问题的本质：芯体长度跨度 140 mm、7 种长度、3 种宽度；因 P = πD/n，单一鼓径下唯一杠杆是每转芯体数）"
  - "End zone = drum pitch − SAP pattern length, with ≥30 mm needed for end seal and cut; option A (Ø882, 6/7-up) gives the lowest mean end zone at 52 mm with 9 of 11 sizes ≤42 mm; option B (Ø889, 6/8-up) means 76 mm and wastes 100–110 mm of core wrap on M and all pants; option C (Ø1,014, 7/9-up) means 69 mm and is outside the 800–900 mm window（端区 = 鼓距 − 印花长度，≥30 mm 用于端封与分切；A 方案均值 52 mm 最优）"
  - "At 1,000 ppm: 6-up = 461.8 mm pitch / 166.7 rpm / 462 m/min / 13.7 g centrifugal / 1.00 ms per degree / 4 sizes; 7-up = 395.8 mm / 142.9 rpm / 396 m/min / 10.1 g / 1.17 ms / 7 sizes（两 ups 在 1000 ppm 下的鼓距、转速、线速、离心场、每度时间与覆盖码数）"
  - "Chassis pitch is decoupled downstream by a SERVO REPITCH TURRET (0.85–1.40 ratio) rather than cut-and-slip, because cut-and-slip needs ratio ≥~1.03 and can only speed a core up — open NB at 0.99 would fail; chip trim is needed only for NB (56 mm) and S (22 mm)（用伺服再分距转塔解耦：比例 0.85–1.40；剪切滑移只能加速，NB 的 0.99 会失败）"
  - "Design rule: everything that defines PHASE is on the drum body; everything that defines SIZE is on the sleeve. At grade change only 2 sleeves, the SAP chute width insert, the recipe (ups, cams, fan, glue) and the knife insert (NB/S only) move — drum bodies, bearings, sectors, motors, encoders, nip gap, fans and glue modules stay（设计规则：相位在鼓体、尺寸在套筒；换码只换 2 个套筒 + 下料口宽度嵌件 + 配方 + 刀具嵌件）"
  - "Nichidai sleeve set = 22 sleeves (11 sizes × skin + poly), pocket-and-land relief with end zones as blanked lands; lands 0.45 mm high, perforated screen Ø0.6–0.8 mm with 30–40% open, sleeve swap ≤15 min per drum; skin/poly pairing must be designed as ONE CAD file because every channel meant to bond must exist on both sleeves at the same position（Nichidai 套筒组 22 件，凸台 0.45 mm，网孔 0.6–0.8 mm，换套筒 ≤15 min；皮肤面/聚乙烯面须按同一 CAD 成对制造）"
  - "Vacuum sectors are fixed in DEGREES, so the 7-up (17% slower) gets 17% more dwell in every zone: NW wrap 60° = 60/70 ms, SAP forming 65° = 65/76 ms at −8…−12 kPa, land clean 25° = 25/29 ms, glue+hold 54° = 54/63 ms at −4…−5 kPa, nip/transfer 18° = 18/21 ms, return 138° = 138/161 ms（真空扇区按角度固定，7-up 各区停留时间多 17%）"
  - "SAP dosing: drum surface speed drops from 7.70 to 6.60 m/s in 7-up, so a chute tuned for 6-up overshoots by 1.1 m/s; eductor air is set so SAP ARRIVES at 6.6 or 7.7 m/s (±0.3); if left at the 6-up setting the simulated in-spec rate drops from 99.996% to 92.7%; a phase-locked servo rotary valve (~90% on pattern) beats a continuous full-width curtain (~50%)（落料速度必须随 ups 重设；到达速度 6.6/7.7 ±0.3 m/s；不重设则合格率 99.996%→92.7%；相锁转阀 ~90% vs 连续帘幕 ~50%）"
  - "Registration: 200,000 products simulated per case, spec |MD| ≤1.0 mm and |CD| ≤0.5 mm (keeps ≥90% channel bond area); Cpk MD/CD = 2.43/1.39 (6-up) and 2.49/1.39 (7-up); in-spec ≥99.99% both ups; after a grade change MD self-corrects in ~17 products (1 s) while CD must be pinned（套准仿真：20 万片/例，MD ≤1.0、CD ≤0.5 mm，Cpk 2.43/2.49（MD）与 1.39（CD），换码后 MD 约 17 片自校正、CD 必须销定位）"
  - "SAP selection targets for pattern fidelity: PSD 150–710 µm with D50 350–450 µm, fines ≤2%, irregular gel-crushed shape, bulk density 0.62–0.70 g/cm³ with lot CV ≤1%, flowability ≥10 g/s, moisture 3–6%, CRC/AAP 0.7 psi 26–30 / ≥22 g/g, SFC ≥80 ×10⁻⁷ cm³·s/g, throughput 270–700 kg/h/drum（SAP 选型目标——源文自述为"待与供应商讨论的目标值，非实测"）"
  - "Hot-melt for the nip: glue-to-nip time grows from 54 ms (6-up) to 63 ms (7-up), so pick the adhesive for the LONGER one — SBS-based PSA staying tacky ≥100 ms cold, 2,500–6,000 mPa·s at 150 °C, application 140–150 °C max, 3–5 gsm per drum, softening point 85–95 °C, wet channel bond ≥1.5 N/25 mm after 2 saturations（热熔胶按更长的 63 ms 选型；SBS 基压敏、黏度、温度、添加量与湿态通道粘结判据）"
  - "Top risks and mitigations, in the source's own priority order: chute speed left at the other ups (recipe-locked eductor setpoint + alarm on SAP-edge camera metric); wrong sleeve for recipe (sleeve ID tags read by PLC + start interlock); NB core longer than chassis (chip trim to 60 mm end zone + repitch turret at 0.99); skin/poly land heights differ with gsm (design pairs together, nip set land-to-land per recipe); 22 sleeves to store and maintain (carrier racks + wear check per campaign)（五大风险与对策，源文自排序）"
pages_linked: ["[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]", "[[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]", "[[Core Channel Pattern（芯体通道花型设计）]]", "[[SAP性能指标（CRC AUL GBP Vortex）]]", "[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]", "[[Nichidai（日丝）]]", "[[IPC BCC OI Portfolio（开放创新项目组合）]]"]
---

# One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）

> 一句话定位：一份 **"一个鼓、两套 ups、11 个码、1000 ppm"的印花 SAP 芯体设备方案深挖**——从**尺寸跨度问题出发，论证为何选 Ø882 mm + 6/7-up**，并给出**逐码运行窗口、鼓体/套筒/真空/伺服/落料/套准的完整参数与五大风险**。（中文：把"多码共线"这个难题，收敛成"只换套筒 + 只改配方"。）

> ⚠️ **来源性质（2026-09-29）**：本件为**设备方案 / 工程概念稿**（自标 DEEP DIVE），**数值以仿真与设计目标为主**（in-spec 率、Cpk、功率、扭矩均标注为 simulated / est.），**SAP 参数表源文自述为 "Targets for supplier discussion, not measured data"**。credibility 定为**中**：**方案逻辑与参数结构可用，绝对数值须经设备商与实测确认**。

## 原文要点 Original Key Points

### 1. 概念总览

| 项 | 值 |
|---|---|
| 鼓径 | **Ø882 mm**（单鼓体，双面使用） |
| Ups | **6-up / 7-up**（两套套筒族） |
| 线速 | **1,000 ppm；鼓面 396–462 m/min** |
| 覆盖 | **6 个开放式纸尿裤码 + 5 个裤型码（共 11 码）** |
| 套准 | **仿真 in-spec ≥99.99%**（在每次换码中保持） |
| 印花方式 | **皮肤面（skin-side）与聚乙烯面（poly-side）双面 pattern-SAP 印花** |

> 中文：核心命题是——**在固定的 1000 ppm 与单一鼓径下，如何让 11 个码共线**。

### 2. 尺寸问题：芯体长度跨度 140 mm

| Family | Size | MD × CD（mm） |
|---|---|---|
| Open diaper | NB | 280 × 100 |
| Open diaper | S | 314 × 100 |
| Open diaper | M | 358 × 110 |
| Open diaper | L | 385 × 110 |
| Open diaper | XL | 420 × 110 |
| Open diaper | XXL | 420 × 110 |
| Pants | L | 355 × 110 |
| Pants | XL / XXL / XXXL | 365 × 120 |
| Pants | XXXXL | 420 × 120 |

- **7 种长度**（280 → 420 mm，**最长是最短的 1.5×**）；其中 355/358/365 与 420 成簇，**NB 与 S 孤立**。
- **3 种宽度**（100 / 110 / 120 mm）——**在 CD 方向处理，不由 ups 决定**。
- **为什么 ups 是杠杆**：鼓径固定时，改变鼓距的唯一方式是**每转芯体数**（`P = πD / n`）；在固定 1000 ppm 下鼓以 `1000/n rpm` 旋转，其**表面速度（m/min）等于鼓距**；**机架节距由下游的再分距单元解耦**。

### 3. 三方案对比 → 推荐 A

**端区定义**：`End zone = 鼓距 − SAP 印花长度`（**端封与分切需 ≥30 mm**；越小则芯体包裹浪费越少）。

| 方案 | 配置 | 平均端区 | 评价 |
|---|---|---|---|
| **A（推荐）** | **Ø882 mm，6-up + 7-up** | **52 mm** | **9/11 码 ≤42 mm**；仅 NB、S（以及 open L 的 77）偏长；在 800–900 mm 窗口内 |
| B | Ø889 mm，6-up + 8-up | 76 mm | 对 NB/S 最好，但 **M 与全部裤型每片浪费 100–110 mm 芯体包裹** |
| C | Ø1,014 mm，7-up + 9-up | 69 mm | 裤型仍 ≥90 mm，且**鼓径超出窗口** |

### 4. 两 ups 的运行参数（@1,000 ppm）

| 项 | 6-up | 7-up |
|---|---|---|
| 鼓距 | **461.8 mm** | **395.8 mm** |
| 鼓速 | 166.7 rpm | 142.9 rpm |
| 表面速度 | **462 m/min** | **396 m/min** |
| 离心场 | **13.7 g** | **10.1 g** |
| 每度时间 | 1.00 ms | 1.17 ms |
| 覆盖码数 | **4** | **7** |

- **6-up** 覆盖：Open L / XL / XXL、Pants XXXXL
- **7-up** 覆盖：Open NB / S / M、Pants L–XXXL
- **两个鼓（皮肤面与聚乙烯面）必须始终使用相同的 ups**——压合区（nip）要求两侧**节距与相位一致**。

### 5. 逐码运行窗口（@1,000 ppm，SAP 160–230 gsm）

| Size | Core mm | Ups | 鼓距 | End zone | Trim | 鼓 m/min | SAP g/片/侧 | SAP kg/h/鼓 | 再分距比* |
|---|---|---|---|---|---|---|---|---|---|
| Open NB | 280×100 | 7 | 395.8 | **116 mm** | **56 mm 切屑** | 396 | 4.5–6.4 | 269–386 | 0.99 |
| Open S | 314×100 | 7 | 395.8 | 82 mm | **22 mm 切屑** | 396 | 5.0–7.2 | 301–433 | 1.07 |
| Open M | 358×110 | 7 | 395.8 | 38 mm | — | 396 | 6.3–9.1 | 378–543 | 1.18 |
| Open L | 385×110 | 6 | 461.8 | 77 mm | — | 462 | 6.8–9.7 | 407–584 | 1.07 |
| Open XL / XXL | 420×110 | 6 | 461.8 | 42 mm | — | 462 | 7.4–10.6 | 444–638 | 1.15 |
| Pant L | 355×110 | 7 | 395.8 | 41 mm | — | 396 | 6.2–9.0 | 375–539 | 1.23 |
| Pant XL / XXL / XXXL | 365×120 | 7 | 395.8 | **31 mm** | — | 396 | 7.0–10.1 | 420–604 | 1.25 |
| Pant XXXXL | 420×120 | 6 | 461.8 | 42 mm | — | 462 | 8.1–11.6 | 484–696 | 1.19 |

> 中文：**NB 是唯一的"负比"码（0.99）**——它的芯体比机架节距还长，这也是后面选伺服再分距转塔的直接原因。

### 6. 为什么用伺服再分距转塔（repitch turret）

| 方案 | 能力 | 结论 |
|---|---|---|
| **Cut-and-slip（剪切滑移）** | 需要比值 **≥~1.03**，且**只能让芯体加速** | **Open NB（0.99）会失败**；Open L 与 S 处于 1.07 |
| **Servo repitch turret（伺服再分距转塔）** | **0.85–1.40** | 采用：吸盘按各自凸轮曲线在 **396 或 462 m/min** 取芯体，再按机架节距放置——**每码一套配方** |

- **切屑修边仅 NB（56 mm）与 S（22 mm）需要**：双刀分切辊 + 真空切屑抽除；**仅这两个码换刀嵌件**。

### 7. 工艺架构（8 步）

1. **伺服旋转 SAP 阀 + 成形下料槽（shute）**，与图案**相位锁定**；宽度嵌件 100/110/120
2. **成形罩**，高真空扇区 **65° = 65 ms（6-up）/ 76 ms（7-up）**
3. **气刀**清理凸台（lands）、通道与端区
4. **纤维化热熔胶（Fiberized HMA）**，分段喷嘴，涂宽随芯宽
5. **皮肤/聚乙烯鼓对鼓压合（nip）**，凸台在套准状态下粘合通道
6. **UV 套准相机**，**仅对聚乙烯面鼓**做相位微调
7. **双刀分切辊**——单切；NB 与 S 加切屑切
8. **伺服再分距转塔**——鼓距 → 机架节距，按配方

### 8. 鼓体设计准则（"相位在鼓体、尺寸在套筒"）

| 参数 | 规格 | 理由 |
|---|---|---|
| 节径 | **882.0 mm**（NW 中平面），周长 **2,771 mm** | 6-up 461.8 / 7-up 395.8 mm |
| 设计转速 | **200 rpm**（6-up 166.7、7-up 142.9） | 对较快 ups 留 **20% 余量** |
| 跳动 / 平衡 | **TIR ≤0.03 mm**；每套筒组 **G1.0** | 每次换套筒族做再平衡检查 |
| 套筒接口 | **销定位到编码器零位 ±0.02 mm，锥面锁紧** | 换码无需重新套准 |
| 套筒图案公差 | **±0.02 mm / 2,771 mm，全部 n 个节距** | 节距相等 → 一个相位适配全部 |
| 真空扇区 | **固定角度扇区，与 ups 无关** | 换码时不换扇区 |
| CD 对中 | 图案在所有宽度下**居中于鼓面** | 100/110/120 用同一轴向设定 |
| 皮肤 vs 聚乙烯鼓 | **相同本体，镜像手性** | 节距、惯量与跳动等级一致 |
| 压合间隙 | **land-to-land 0.15–0.18 mm**，限位 + 预载 | 跨码不变 |

**换码时**：**变**的是 2 个套筒、SAP 下料槽宽度嵌件、配方（ups / cams / fan / glue）、刀嵌件（仅 NB、S）；**不变**的是鼓体、轴承、扇区、力矩电机与编码器、压合间隙与轴向对中、风机与风管、胶模块。

### 9. Nichidai 套筒组（22 件，一种构造）

- **11 码 ×（皮肤面 + 聚乙烯面）= 22 件**；**pocket-and-land 浮雕**，**端区作为"封堵凸台"（blanked lands）**。
- **4 项构造要点**：① **凸台 = 通道 + 端区**，高 **0.45 mm**（30–116 mm 的端区也是凸台，故**芯体之间无 SAP**）；② **凹槽 = SAP 图案**，全部 n 个重复节距一致、±0.02 mm；③ **穿孔网板 Ø0.6–0.8 mm，开孔率 30–40%，每个套筒相同**；④ **套筒载体**销 + 锥面，**每鼓更换 ≤15 min**。
- **向 Nichidai 提出的四项要求**：套筒间分度重复性 **±0.02 mm**、凸台边缘圆角 **≤0.2 mm**、耐磨凸台面、**PLC 可读的套筒 ID 标签**（用于阻止错误 ups 的配方）。
- **皮肤/聚乙烯配对规则**：**图案可以不同，但每一条需要粘合的通道必须在两个套筒的同一位置存在**——**按一个 CAD 文件成对设计并成对制造**。

### 10. 真空扇区：角度固定 → 停留时间不同

| Zone | Arc | 6-up dwell | 7-up dwell | Vacuum |
|---|---|---|---|---|
| NW wrap & pocket 无纺布包裹与凹槽成形 | 60° | 60 ms | 70 ms | −2…−3 kPa |
| **SAP forming SAP 成形** | **65°** | 65 ms | 76 ms | **−8…−12 kPa**（配方项） |
| Land clean 凸台清理 | 25° | 25 ms | 29 ms | 仅凹槽 |
| Glue + hold 施胶与保持 | 54° | 54 ms | 63 ms | −4…−5 kPa |
| Nip / transfer 压合与转移 | 18° | 18 ms | 21 ms | 皮肤面 **+1…+3** / 聚乙烯面 −4 kPa |
| Return 回程 | 138° | 138 ms | 161 ms | 0 / 气刀 |

> **关键判据（源文）**：**保持力从来不是限制**——在 **13.7 g** 离心场下，**230 gsm 的床层仅需约 39 Pa**，而保持区给出约 **4,000 Pa**。因此**配方改变的是成形真空（床层阻力）与气刀压力，而不是扇区几何**。

### 11. 成形风机（变频）

- **每鼓一台鼓风机**，VFD 转速由配方设定、由**集流腔压力 PID 微调**。
- **流量**：每码 **9–14 m³/min**（图案面积 × 2.5 m/s + 保持 + 40% 泄漏）。
- **压力构成**：**10–12 kPa** = 网板/无纺布 3 + SAP 床层 5–7 + 管路 2。
- **设计点**：**22 m³/min @ 15 kPa，8.5 kW 轴功率** → 选用 **11 kW IE5 永磁电机 + VFD**。
- **相对风门的节能**：**−36% 至 −62%**，**在 NB/S（160 gsm）上最大**。

### 12. 伺服架构（ups 感知的配方）

- **一个虚拟主轴 @1,000 ppm**；**每个轴按产品数（而非 m/min）齿轮/凸轮同步**。
- **EtherCAT，250 µs，DC 同步**；配方（**经套筒 ID 校验**）含 ups n、cams、fan、glue、chute。
- **UV 相机 + 套准回路**，仅对聚乙烯鼓做相位微调。

| Drive（每鼓） | 6-up | 7-up |
|---|---|---|
| 鼓速 | 166.7 rpm | 142.9 rpm |
| 惯量 J（估 270 kg 壳体） | ≈52 kg·m² | ≈52 kg·m² |
| 运行扭矩 / 功率 | 180 Nm / 3.1 kW | 180 Nm / 2.7 kW |
| 3 s 停止 | ≈455 Nm | ≈410 Nm |
| 跟随误差 | ±38 µm | ±33 µm |

- **一个电机规格覆盖两个 ups**：直驱力矩电机 **≥250 Nm 连续 / ≥600 Nm 峰值**，鼓轴上 **≥23 位绝对值编码器**；**配方只改 1/n 齿轮比**。

### 13. SAP 落料：速度必须随 ups 重设

- 鼓面线速从 **7.70（6-up）降到 6.60（7-up）m/s** → **按 6-up 调校的下料槽在 7-up 上超速 1.1 m/s**。
- **配方中的下料槽速度**：**eductor 气压设定为使 SAP 到达速度为 6.6 或 7.7 m/s（±0.3）**。
- **若未随 ups 重设**：仿真 in-spec 率从 **99.996% 降到 92.7%**。
- **用伺服转阀而非帘幕**：**相锁脉冲（每转 n 个）只把 SAP 撒在凹槽上**——**约 90% 落在图案上**，而**连续全幅帘幕仅约 50%**。
- **宽度嵌件 100/110/120 mm**：按宽度族配置成形下料槽出口；**端区与通道的散落料经旋风分离器除细粉后回用**。

### 14. 套准仿真

| 项 | 值 |
|---|---|
| 样本 | **每例 200,000 片** |
| 规格 | **│MD│ ≤1.0 mm，│CD│ ≤0.5 mm**（可保持 **≥90% 通道粘合面积**） |
| **Cpk MD / CD** | 6-up **2.43 / 1.39**；7-up **2.49 / 1.39** |
| In spec | **两 ups 均 ≥99.99%**；**若 chute 未重设则 92.7%** |
| 换码后 | **MD 约 17 片（1 s）内自校正**；**CD 必须靠销定位** |
| 换码后 MD 偏移（源文图） | 销定位 **±0.05 mm**；仅配方补偿 **0.6 mm**；无补偿 **2.5 mm** |

### 15. 压合后的层结构

| 层（自上而下） |
|---|
| 皮肤面芯体包裹——**SMS 10 gsm，亲水** |
| **皮肤面 SAP**（皮肤鼓） |
| **纤维化 HMA**（两鼓均施） |
| **聚乙烯面 SAP**（聚乙烯鼓） |
| 聚乙烯面芯体包裹——**SMS 10–12 gsm** |

**芯体包裹无纺布目标**：幅宽**每个芯宽族一个**；**最大孔径 <100 µm**；**MD 应变 @5 N/50 mm ≤1.5%**；**140 °C 热收缩 ≤1%**；**放卷速度跟随鼓距（396/462）**。

> **皮肤面与聚乙烯面的 SAP 克重可以不同**（如 230 皮肤 / 160 聚乙烯）——**但每个套筒必须给出各自床层的凸台高度，使压合仍然是 land-to-land**。

### 16. SAP 选型（跨 11 码的图案保真度）

| 属性 | 目标 | 理由 |
|---|---|---|
| 粒径 | 150–710 µm，**D50 350–450 µm** | 在 396 与 462 m/min 下均获得锐利边缘 |
| 细粉 <150 µm | **≤2%** | 穿透无纺布、堵网、粘附端区凸台 |
| 形状 | **不规则（gel-crushed）** | 抗落点后滚动 |
| 松密度 | 0.62–0.70 g/cm³，**批间 CV ≤1%** | 床高匹配凸台高：0.31 mm @160、0.44 mm @230 gsm |
| 流动性 | **≥10 g/s**，抗结块 | 转阀在 **16.7 脉冲/秒**（1,000 ppm）下干净充填 |
| 含水 | **3–6%** | 减少静电 → 凸台与端区更干净 |
| CRC / AAP 0.7 psi | 26–30 / ≥22 g/g | 无绒架构下吸收全由 SAP 承担 |
| 渗透率 | **SFC ≥80 ×10⁻⁷ cm³·s/g** | 无凝胶阻塞；湿态保持通道开孔 |
| 吞吐 | **270–700 kg/h/鼓** | NB 160 gsm → 裤型 XXXXL 230 gsm |

> ⚠️ **等级声明（源文原文）**：*"**Targets for supplier discussion, not measured data.** Qualify on bed-edge sharpness (image analysis) at both drum speeds."* —— **全部为待与供应商讨论的目标值**，且**合格判据是两种鼓速下的床边缘锐度（图像分析）**。

### 17. 热熔胶：按更长的 63 ms 选型

- **施胶到压合的时间**从 **54 ms（6-up）增至 63 ms（7-up）** → **按更长的那个选胶**。

| 判据 | 建议 |
|---|---|
| 化学 | **SBS 基压敏胶**，**冷态保持 tacky ≥100 ms** |
| 黏度 | **2,500–6,000 mPa·s @150 °C** |
| 施加温度 | **140–150 °C 上限**（保护 PP 无纺布） |
| 添加量 | **3–5 gsm/鼓（含凸台）**；4 gsm 时约 **175–240 g/min** |
| 软化点 | **85–95 °C**，高内聚以保湿态通道 |
| 湿态通道粘结 | **≥1.5 N/25 mm（2 次饱和后）**（待验证） |

**设备要点**：**分段纤维化喷嘴**（100/110/120 mm 芯体 + 10 mm 凸台余量，靠分段阀实现，**不换喷嘴**）；**泵速跟随鼓面线速（396 或 462 m/min）**，故 ups 变化时 gsm 不变；**沿节距连续施胶**（端区凸台需要胶来封芯体两端）；**UV 示踪剂仅加在皮肤面胶中**。

### 18. 换码 <30 分钟与五大风险

**换码四步**：① 停机与更换（皮肤与聚乙烯套筒并行 **≤15 min**；下料槽嵌件；NB/S 刀嵌件）；② 配方加载（**套筒 ID 校验** → ups n、cams、fan、glue 分段、chute 速度）；③ 自动相位（销定位 **±0.05 mm**，相机回路在 **约 17 片内**校正 MD）；④ 验证（首件通道套印与湿态粘结，放行）。

**Top risks and mitigations（源文排序）**

| # | 风险 | 对策 |
|---|---|---|
| **1** | **Chute speed left at the other ups** | **配方锁定 eductor 设定值；对 SAP 边缘相机指标设报警** |
| 2 | Wrong sleeve for recipe | **套筒 ID 标签由 PLC 读取；启动联锁** |
| 3 | NB core longer than chassis | **切屑修边至 60 mm 端区；再分距转塔（比 0.99）** |
| 4 | Skin/poly land heights differ with gsm | **成对设计；按配方设定 land-to-land 压合** |
| 5 | 22 sleeves to store and maintain | **载体料架；每次生产周期检查凸台面磨损** |

> 🔴 **manual_review（2026-09-29）**：本件为**设备方案稿**，含① **供应商名称与能力要求**（Nichidai 套筒、Chuanyue、chute/eductor 供应商、鼓风机与电机规格）；② **投资相关的设备规格**（电机扭矩/功率等级、风机 kW、套筒数量与库存维护）；③ **SAP 与热熔胶的选型目标**（含具体牌号级性能门槛）。依 AGENTS.md §5：本页**只记技术判据、参数结构与风险对策**，**不页面化商务条款、报价与定点意向**；**设备型号与供应商能力口径须由设备商确认**。

## 与库内页面的关系 Relations

- [[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]（本件是该概念页的主来源）
- [[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]（本件 §13 是该概念页的**原始出处**——本库 86 号规范即由本件 P13/P16/P18 派生）
- [[Core Channel Pattern（芯体通道花型设计）]]（通道与凸台设计）
- [[SAP性能指标（CRC AUL GBP Vortex）]]、[[ActiveTech Platform（ActiveTech 在线薄芯体平台）]]
- [[Nichidai（日丝）]]（套筒供应方）
- [[IPC BCC OI Portfolio（开放创新项目组合）]]

## 存疑 / 待人工确认 Open Questions

1. **本件是本库 [[SAP Dosing Speed Matching & Tolerance Spec（SAP 落料速度匹配与容差规范）]]（86 号）的原始来源**——86 号已指出本件**未给出 Δp 口径、飞行时间与位移分布映射**，故 **99.996% → 92.7% 不可独立复算**。本页**沿用该限制，不代为补齐**。
2. **"in-spec" 的两种口径**：本件同时出现 **≥99.99%（套准，由 Cpk 决定）**与 **99.996% / 92.7%（SAP 落点）**——**二者是不同指标，禁止混引**（该区分由 86 号规范明确）。
3. **SAP 参数表全部为"待与供应商讨论的目标值"**，且**合格判据（图像分析算法）本身尚未定义**。
4. **流动性 ≥10 g/s 与单鼓吞吐 74.7–193.3 g/s 相差 7.5–19 倍**——该口径疑问由 86 号规范提出，本件**未澄清**。
5. **床高 vs 松密度不自洽**：本件给床高 0.31 mm @160 gsm、0.44 mm @230 gsm，反推 ρ_bed ≈0.52 g/cm³，**低于本件自身规格 0.62–0.70**——86 号已记为对账缺口，本页**照录不裁决**。
6. **同一 Ø882 mm 鼓覆盖 11 码**为**仿真结论**（End zone、Cpk、in-spec 均标注 simulated），**未经验证**；**NB 需 56 mm 切屑修边**是结构代价。
7. 本件**无编制日期**，`date_published` 标 `[待验证]`。

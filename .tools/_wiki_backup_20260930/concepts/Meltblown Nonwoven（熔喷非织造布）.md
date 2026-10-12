---
type: concept
title: "Meltblown Nonwoven（熔喷非织造布）"
domain: [卫材研发, 无纺布工艺]
status: seed
updated: 2026-09-29
tags: [熔喷, Meltblown, 纤维直径, 孔密度, 阻隔, SMS, SMMMS]
---

# Meltblown Nonwoven（熔喷非织造布）

> One-line definition 一句话定义：把熔融聚合物经**高速热气流**牵伸成超细纤维并直接成网的工艺；本库新增的量化结论是——在工业窗口内，**纤维直径由每孔产量与射流速度决定，而不由熔体粘度／模头温度决定**。（中文：直径 = 阻力限制（drag-limited），温度只能决定多快达到速度匹配。）

## Mechanism / Structure 机理 / 结构拆解

1. **Drag-limited attenuation 阻力限制的牵伸**：filament reaches velocity-matching with the air jet, and after that mass conservation fixes the diameter（d ∝ v(m / Λ v_a)）。Melt viscosity only changes how fast matching is reached — 2.4 mm from the tip at 285 °C, 2.7 mm at 250 °C。中文：一旦与射流速度匹配，质量守恒即锁定直径；粘度只影响「多快达到匹配」。
2. **Three real levers 三个真实杠杆**：cut g/hole/min（0.73 → 0.20 at fixed line output means 35 → 130 hpi）、raise jet velocity（150 → 250 m/s buys 2.85 → 2.21 µm, then saturates）、and **nothing else** — tip temperature, MFR and hole diameter do not move the diameter。（温度、MFR、孔径都不动直径。）
3. **The opposing constraint is die pressure 对立约束是模头压力**：a 450 MFR resin at conventional tip temperature crosses the die-tip pressure limit at about **160 hpi**。Both conventional escapes cost something — MFR up to 1200 (pressure drops, but Mv falls, melt strength falls, breaks and shot rise, formation CV worsens) and bulk melt up to 300 °C+ (pressure drops, but thermal dose rises steeply)。The third escape is [[Laser-Assisted Die Tip（激光辅助模头）]]：same pressure relief, 4–20 ms of exposure instead of 480 s。
4. **Capillary density is the live battleground 孔密度是当前主战场**：production dies have moved from **35 hpi to 70–100 hpi**（up to 130 hpi in the modelled build），with multi-row cassette designs offered as a swap-in on composite lines。Sub-micron claims almost always come from low throughput per hole, not from a new attenuation mechanism。
5. **Die-tip air uniformity, not air volume 模头气流要均匀而非要大**：recent die-tip patents target uniform high-velocity air around the tip and faster changeover rather than higher air rates；**fibre CV, not mean diameter, is what limits barrier performance**（见 [[Formation-Limited Barrier（阻隔的成形受限机理）]]）。
6. **Laser drawing exists but is off-line 激光拉伸是真的，但在线下进行**：CO₂ laser supersonic drawing reliably makes 250–600 nm PP/PET/PA66/PPS fibres at draw ratios above 10⁵ — on an already-spun filament in a vacuum chamber。It is a **nanofibre lab route, not a web-forming process**。
7. **Where meltblown sits in the library's process map 在本库工艺图谱中的位置**：熔喷提供阻隔与过滤精度（1–5 µm 级纤维），但强度低、需纺粘支撑——故以 [[SMS复合结构]] 与 SMMMS 等形式使用；相关对照见 [[无纺布五大工艺对比]]。

## Key Parameter Table 关键参数表

| Parameter 参数 | Typical value / range 典型值 / 范围 | Source 出处 |
|---|---|---|
| Fibre diameter, industrial window 工业窗口纤维直径 | 1.5 µm modelled（at 0.195 g/hole/min, 250 m/s）；1.94 µm at 60 kg/h·m；2.21 µm at 0.73 g/hole/min | [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]] |
| Tip temperature effect on diameter 温度对直径的影响 | < 1 %（250 → 300 °C） | 同上 |
| Production die capillary density 量产孔密度 | 35 hpi → 70–100 hpi | 同上 |
| Modelled capillary density 建模孔密度档 | 100 / 130 / 160 hpi（回退／量产／高强） | 同上 |
| Capillary diameter 孔径 | 0.130 mm | 同上 |
| Throughput per hole 每孔产量 | 0.195 g/min（**the variable that actually sets diameter**） | 同上 |
| Primary air 一次风 | 250 m/s at 290 °C（> 300 m/s 直径增益饱和） | 同上 |
| Die-to-collector 模头-收集距离 | 180–220 mm（长到足以无飞絮铺网） | 同上 |
| Jet velocity vs diameter 射流速度-直径 | 150 → 250 m/s 换取 2.85 → 2.21 µm | 同上 |
| Die-tip pressure wall 压力墙 | ~160 hpi（450 MFR，常规模头温度） | 同上 |
| Wall shear rate 壁面剪切速率 | 20,400 s⁻¹ | 同上 |
| CO₂ laser supersonic drawing CO₂ 激光超声拉伸 | 250–600 nm（PP/PET/PA66/PPS），拉伸比 > 10⁵，**离线** | 同上 |
| Fibre diameter (library baseline) 库内基线 | 1–5 µm（超细） | [[无纺布-五大工艺论剑]]、[[无纺布五大工艺对比]] |
| Mechanical strength 机械强度 | ★★☆☆☆（需 SMS 支撑） | [[无纺布-五大工艺论剑]] |
| Filtration 过滤 | 唯一能实现 0.3 µm 颗粒物高效过滤的工艺 | [[无纺布-五大工艺论剑]] |
| PFAS risk 含氟风险 | 驻极助剂含氟电荷俘获剂是最易被忽视的 PFAS 来源 | [[SMS复合结构]]、[[无纺布五大工艺对比]] |

> ⚠️ **No unsourced parameters 禁止无来源参数**：上表直径／压力／孔密度数值均为**模拟值**（见源页「Honest limits」——Λ = 6 为拟合值、CV = 15 % 为假设值，未实测），引用时必须标注「模拟」而非「实测」。本库暂无熔喷线的实测纤维直径分布，标 `[待验证]`。

## Adjacent Concepts 相邻概念

- Composite structures 复合结构：[[SMS复合结构]]、[[Film-Free Backsheet（无膜背层）]]
- Process peers 同层工艺：[[热风粘合无纺布]]、[[无纺布五大工艺对比]]
- Governing physics 支配物理：[[Formation-Limited Barrier（阻隔的成形受限机理）]]、[[熔融指数与化学降解]]
- Hardware 硬件：[[Laser-Assisted Die Tip（激光辅助模头）]]
- Resin 树脂：[[茂金属聚丙烯]]

## Lessons Learned 经验教训

> ✅ Verification（2026-09-29，source [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]]）：该评估以 1-D 长丝 ODE 与质量守恒复核了熔喷牵伸逻辑，结论与库内既有「熔喷纤维 1–5 µm、强度低需 SMS 支撑」的定位一致，并**新增一条反直觉量化结论**：在工业窗口内提温不细化纤维。（中文：与既有页面结论一致，属补充而非修正。）

- **Lesson 1（别把温度当细化手段）**：想做到 1.5 µm，唯一可控变量是**每孔产量与射流速度**（即孔密度与风量），提模头温度得到的 <1 % 直径收益不足以支撑任何项目论证。
- **Lesson 2（孔密度的对手是压力墙）**：孔密度与 MFR 是联动的——用 1200 MFR 换低压降会牺牲 Mv、熔体强度与成形 CV，**而阻隔恰恰受成形均一性限制**，两者互为反噬。
- **Lesson 3（离线激光拉伸不能替代成网工艺）**：CO₂ 激光超声拉伸可做 250–600 nm，但作用对象是已纺长丝、且在真空腔内，属**纳米纤维实验室路线**，不是成网工艺。
- **待补 `[待验证]`**：本库暂无熔喷产线的实测孔密度-直径-静水压三联数据；也无熔喷束实际成形 CV 实测值。

## 追加：COCO V6 第二轮实验批（2026-09-29 追加 · 熔喷用作 core wrap）

> 本节为 **S5_Areas_Meeting Minutes_01 批次（[[COCO V6 Trial Round-2 Review（录音纪要 2026-09-16）]]）** 编译时的追加记录，**不改动上方既有结论**。本批新增的是**熔喷作为芯体包裹布（core wrap）** 这一应用场景。

### 1. Advantages observed 本批观察到的优势

- **纤维更细**：熔喷纤维的纤度约为一般纺粘/短纤纤维的 **1/20** → **毛细爬坡（反重力吸收）优势明显**，实测优于 38 g 水刺下盘（20 g 熔喷即有明显优势）。
- **利于印刷**：在 core wrap 上做印刷（图案/尿显）时，**对 ink 的承载能力更高**。
- 材料本身含 fluff，也利于吸收。

### 2. Risk identified 本批识别的风险

- **高速下的强度是最大风险**：**20 g** 熔喷在高速运行中强度可能不足；CD 方向强度的最低要求口径约 **1,600**（约 1,000 会断）`[待验证]`。
- **建议动作**：① 尽快组织 project team 解决强度；② 试 **25 g**；③ 采用「**上层熔喷 + 下层 SMS**」的组合以规避强度风险。

> ✅ Verification（2026-09-29，source 来源 [[COCO V6 Trial Round-2 Review（录音纪要 2026-09-16）]]）：本页既有「熔喷非织造布」的定位被本批**支持并扩展到芯体包裹布场景**；新增的**细纤度 → 毛细爬坡**因果链与既有机理一致。**原结论未被修正**。

> 🔴 **manual_review（2026-09-29）**：本批含材料供方（未公开）与内部成本口径，**本页不复制**；要点留存于源摘要页。

## 追加：Meeting Minutes 批（2026-09-29 追加 · 熔喷-木浆复合低克重材料与喷头孔密度）

> 来源：[[Low-GSM Pulp-Meltblown Core Wrap Review — Strength, Dual Colour & Cost（尿裤包覆层材料探讨）]]（供应商现场交流 ASR 转写，会议日期 [待验证]）。本批只**追加**，不修改既有结论。

**低克重熔喷-木浆复合（coform 类）材料的强度边界（本批新增）：**

| Item 项目 | Value 数值 | Note 备注 |
| --- | --- | --- |
| 样品克重 | **20 gsm**（供应商称 20–200 gsm 可做） | 本方见过最薄的同类样品 |
| 干态强力 | **6–6.5 N** | 上高速机（900 片/分钟）"大概率有问题" |
| 目标强力 | **8–9 N**（需 +2 至 +2.5 N） | 高速不断带的门槛 |
| 湿态表现 | **明显发脆、湿强不足** | 干态可拉但变形率偏高 |
| 木浆 / PP 配比 | 现约 **40 / 60**，可上调 PP 至 **70 / 30** | 提高 PP 推高成本 |

**熔喷侧的三条强度 lever（本批新增）：**

1. **喷头孔密度**：本方建议 **≥60 孔/英寸（25.4 mm）**，并指出国内熔喷装备供应商不一定能支持该密度 —— 供应商**不清楚现设计值**，需回查 [待验证]。
2. **压花花纹**：由大花纹改**小花纹 / 更致密压点**，在**不改配方**的前提下可能提升强度，同时改善手感；供应商不保证。
3. **配方**：提高 PP 比例（最直接但推高成本）。

**双色熔喷的可行边界（本批新增）：**

- 不同熔喷头组分别加入 **3–4% 色母粒** → **可做正反面异色**；色母对强力**基本无影响**（供应商已测）。
- **做不了**需对位切（registration）的"中间白 + 两边带色"构型 → 设计必须绕开对位。

**压花辊投资的量级（本批新增，商务敏感）**：离线热压辊 **15–16 万 / 30 多万元**；在线热压辊 **30 多万欧元** —— 在线方案本方判断无必要，原因是高速（500+ m/min）下热压辊受热旋转产生离心/弧形变形，"中间压得上、两边压不住"，对材质与凹凸咬合精度要求极高。

✅ **验证记录（2026-09-29）**：以上均为**供应商自述 + 本方现场判断**，未见实测数据；强力数值为供应商现有产品的干态口径 [待验证]。参见 [[Coform Composite Nonwoven（熔喷-木浆复合非织造）]]、[[绒毛浆（Fluff Pulp）]]。

## Sources 来源

- [[Laser-Assisted Meltblown Film-Free Backsheet（激光辅助熔喷无膜背层）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Film/Laser_Meltblown_Film_Free_Backsheet.pptx - 已修复.pptx.md`
- [[无纺布-五大工艺论剑]] —— `raw/ima_sync/个人知识库/WKB/Areas/Nonwoven/无纺布 - 五大工艺论剑.md`
- [[无纺布五大工艺对比]] —— 汇总页（库内）
- [[SMS复合结构]] —— 库内页
- [[纳米纤维素供应商拜访计划 V3.1（2026Q2）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/纳米纤维素供应商拜访计划_V3_2026Q2_FullData.docx.md`

## Evidence Update 证据追加（2026-09-29）

> ✅ Verification（2026-09-29，source 来源 [[纳米纤维素供应商拜访计划 V3.1（2026Q2）]]）：与既有「熔喷纤维 1–5 µm、强度低需纺粘支撑」的定位一致，本批补充了 **SSMMS 五层复合的层结构与整机工艺窗口**：S（PP 15–30 μm）+ M（PP 1–5 μm）+ M + S；挤出 190–250 °C、熔体压力 10–30 MPa、纺丝 3,000–5,000 m/min、熔喷 230–280 °C、热轧 130–160 °C / 50–150 N/mm；静电驻极 30–100 kV、0.5–2 s 可再提升过滤效率 10–20%。性能上 SSMMS 静水压 >50 cmH₂O（SMS 30–40，+25–67%）、过滤效率 >95%（SMS 85–90%）、强度 +20–30%，成本较 SMS 约 +1,200 元/吨，亲水整理再加 10–20%。详见同层 [[SMS复合结构]]。
>
> 该组数据与 Lesson 1 不冲突：SSMMS 的阻隔提升来自**层数与驻极**，而非提高熔喷温度细化纤维。
>
> 🔴 **manual_review（2026-09-29）**：该来源含具名无纺布企业产能、价格基准与供应商关系信息，**未页面化**。
>
> 追加 `[待验证]`：SSMMS 在卫材（非医用）场景下静水压与手感/柔软度的取舍曲线；驻极电荷在亲水整理后的衰减速率。

## Evidence Update 证据追加（2026-09-29 · Areas/IP 第 3 批）

> ✅ Verification（2026-09-29，source 来源 [[US7195621B2 Disposable Garment Comprising Meltblown Nonwoven Backsheet (P&G)]]）：本案（US 7,195,621 B2，授权日 2007-03-27）给出一组**产品级的熔喷窗口**，与本页既有「熔喷 1–5 µm、强度低需纺粘支撑」的定位互补而非冲突：
>
> - **平均纤维直径约 3–10 µm**、克重约 **3–60 g/m²**、透气度 **≥ 约 15 cm³/cm²/sec**、透湿度 **≥ 7,000 g/m²/24 hours**；另一披露维度为**纤网模量 230–650 gf/mm**（Instron，100 N 传感器，标距 508 mm，254 mm/min，读取 1% 与 5% 应变）。
> - **对"越细越好"的反向证据**：来源明确批判先行技术 JP kokai H03-240151（Asahi Kasei，1990-02-16 申请）的 **0.5–2.5 µm** 纤维——液体虽被兜住，但**孔径太小**导致透气不足且拉伸强度下降。这与 Lesson 1/ Lesson 5（纤维 CV 与成形，而非平均直径，才是阻隔瓶颈）方向一致，**不构成矛盾**。
> - **实测支撑**：三个实施例（15 / 15 / 50 g/m²）在 **1 psi 与 10 psi 下均无渗漏**；耐水压 650 / 680 / 520 mmH₂O，最大拉力 1.65 / 2.06 / 2.73 kgf，纤网模量 371 / 493 / 596 gf/mm。
> - 测试口径全为日本标准：透湿 JIS L-1099 A-1、耐水压 L-1092 A、透气 L-1096-6-27-1 A、拉力 L-1096-6-12-1 A。
>
> 🔴 **manual_review（2026-09-29）**：法律状态（是否仍在 154(b) 延长后的有效期内、有无更正后再公告）与侵权比对**不作 AI 结论**，详见该源摘要页。
>
> 追加 `[待验证]`：3–10 µm 窗口在本库主力 SSMMS/SMMMS 结构中的对应纺丝参数（该来源只给结果指标，未给对应的 g/hole/min 与射流速度）。

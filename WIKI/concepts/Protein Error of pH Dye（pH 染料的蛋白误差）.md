---
type: concept
title: "Protein Error of pH Dye（pH 染料的蛋白误差）"
domain: [卫材研发, 变色与智能材料]
status: growing
updated: 2026-09-29
tags: [蛋白误差, 溴甲酚紫, 便指示, 比色, 缓冲, 假阳性]
---

# Protein Error of pH Dye（pH 染料的蛋白误差）

> One-line definition 一句话定义：A **binding effect, not a pH effect** — a sulfonephthalein dye buffered hard to pH 3.0 sits fully in its yellow protonated form; when protein reaches the lane, free amino groups bind the dye anion electrostatically and stabilise it, shifting the apparent pKa down so the dye ionises and turns violet **while the bulk pH is still 3**.
> （中文：一种**结合效应而非 pH 效应**——磺酞类染料被强缓冲到 pH 3.0 而处于完全质子化黄色态；当蛋白抵达通道时，多肽游离氨基以静电方式结合染料阴离子并将其稳定，使表观 pKa 下移，于是染料电离转紫，**而本体 pH 仍是 3**。）

## Mechanism / Structure 机理 / 结构拆解

1. **Buffer hard, then let protein do the work（先强缓冲，再让蛋白起作用）**：the lane is buffered to pH 3.0 with a citrate / stearyl-phosphate acid system. The lane therefore reports **protein concentration, not pH**.
2. **Urine cannot move it（尿搬不动它）**：urine can arrive at pH 5.5 or at pH 9 after ammoniacal ageing and the lane does not move — the trigger is not a proton. This is described as **the load-bearing defence** against false BM signals.
3. **Trip point is set by dye loading alone（触发点仅由染料负载决定）**：D × C* ≈ 2,500 (µg/cm² · mg/L). Load less dye, and it takes more protein to move it. Design point 0.50 µg/cm² (= 0.025 wt % of a 20 gsm coat) trips at **5,000 mg/L protein**.
4. **Four independent defences（四重独立防线）**：
   - **MECHANISM 1 — protein binding, not pH**（尿 pH 从 5.5 漂到 9.0 时零响应）
   - **THRESHOLD 2 — trip at 5,000 mg/L**（健康婴儿尿的 33 倍；仅为粪便液的 1/2）
   - **MICRO-ENVIRONMENT 3 — buffer capacity**（1.94 µeq H⁺/cm² 可及酸 vs 约 0.0055 µeq 碱进入 → **350× 余量**，即使 8 h 尿素分解尿）
   - **GEOMETRY 4 — lane placement + conduit**（便通道位于后三分之一的低克重芯体通道上方；尿通道在裆部 25 mm 之外）
   > A false positive needs all four to fail at once. A false negative needs only the geometry to fail — **which is why fluid transport to the lane, not chemistry, is the harder engineering problem.**
5. **Micro-environment is all that matters（只需保护微环境）**：the alkali that matters is not the alkali in the diaper — it is only what dissolves into the melt film itself. At 5 wt % water uptake a 20 gsm coat takes up 0.10 µL/cm²; even 8-hour ammoniacal urine at 55 mmol/L base delivers only 0.0055 µeq/cm². **This is why a hydrophobic rosin / FT-wax matrix matters more than piling in more citric acid.**
6. **The organoclay trick（有机黏土替代法）**：standard wetness-indicator formulations anchor the dye with a **soluble quaternary ammonium salt** — but in a protein-error lane that salt **mimics protein** and develops the violet in the pack. Use a cationic organoclay (quaternised bentonite) at ≤ 1.5 % instead.
7. **Do not over-load acid（不要过量加酸）**：loading past ~8 wt % micronised citric acid is counter-productive — it raises viscosity, abrades the die land and risks shim blockage.
8. **Colour orthogonality（色相正交）**：urine lane = bromocresol green (pH trigger, pale amber → blue-green, "change soon"); BM lane = bromocresol purple (protein error, pale straw → deep violet, "CHANGE NOW", irreversible); temperature lane = leuco dye, 37.5 °C switch (grey → red, fever check). **≥ 6 Ostwald numbers** separate every post-change hue; **violet is reserved for BM alone** — nothing else on the diaper may use it.

（中文：①先用柠檬酸/硬脂基磷酸把通道缓冲到 pH 3.0，故通道报告的是**蛋白浓度而非 pH**；②尿搬不动它——尿无论以 pH 5.5 进来还是氨化老化后以 pH 9 进来，通道都不动，触发量不是质子，这是**承重防线**；③触发点仅由染料负载决定——D×C*≈2,500，负载越少需越多蛋白才能推动，设计点 0.50 µg/cm²（20 gsm 涂层中的 0.025 wt%）对应 **5,000 mg/L 蛋白**触发；④四重独立防线——机理（蛋白结合而非 pH，尿 pH 5.5→9.0 零响应）、阈值（5,000 mg/L，为健康婴儿尿 33 倍、粪便液 1/2）、微环境（1.94 µeq H⁺/cm² 可及酸 vs 约 0.0055 µeq 碱进入，**350 倍余量**）、几何（通道位置与导流通道）；假阳性需四者同时失效，而假阴性只需几何失效——**故流体输运工程比化学更硬**；⑤只需保护微环境——起作用的碱不是纸尿裤里的碱，而是溶进熔膜本身的那一点，5 wt% 吸水率下 20 gsm 涂层仅吸 0.10 µL/cm²，即使 8 h 55 mmol/L 碱度的氨化尿也只带来 0.0055 µeq/cm²，**这就是为何「疏水性松香/FT 蜡基体」比「多加柠檬酸」更重要**；⑥有机黏土替代法——标准尿显配方用**可溶性季铵盐**锚定染料，但在蛋白误差通道中该盐会**模拟蛋白**并在包内显紫，须改用阳离子有机黏土（季铵化膨润土）≤1.5%；⑦不要过量加酸——微粉柠檬酸超过约 8 wt% 适得其反：抬高黏度、磨损模头台面、有垫片堵塞风险；⑧色相正交——尿通道溴甲酚绿（pH 触发，淡琥珀→蓝绿，「尽快更换」）、便通道溴甲酚紫（蛋白误差，淡稻草→深紫，「立即更换」、不可逆）、温度通道隐色染料 37.5 ℃ 切换（灰→红，发热提示）；**≥6 个 Ostwald 数**分隔所有变色后色相，**紫色为便通道独占**，纸尿裤上其他任何元素不得使用。）

## Key Parameters 关键参数表

| Parameter 参数 | Value / range 数值/范围 | Source 出处 |
|---|---|---|
| Lane buffer pH 通道缓冲 pH | 3.0（citrate / stearyl-phosphate acid system） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Selectivity law 选择性定律 | D × C* ≈ 2,500 (µg/cm² · mg/L) | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Design dye loading | **0.50 µg/cm²** = 0.025 wt % of a 20 gsm coat | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Trip point 触发点 | **5,000 mg/L** soluble protein | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Protein in faecal liquid 粪便液蛋白 | 10,000–40,000 mg/L | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Protein in healthy infant urine | < 150 mg/L | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Margin vs healthy urine | **33×** | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Margin vs faecal liquid | **2×** | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Skin-safety cap 皮肤安全上限 | 17 µg/cm² → 设计点为其 1/34 | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Accessible acid 可及酸 | ≥ 1.8 µeq H⁺/cm²（titrated pH 2.5 → 4.5）；design 1.94 | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Equilibrium water uptake | ≤ 5 wt %（37 °C / 95 % RH / 24 h） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Buffer safety margin | 350×（vs 8 h ammoniacal urine at 55 mmol/L base） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Dye 染料 | Bromocresol purple 0.025 wt %（+ Solvent Red 24 0.025 % 作色相偏置） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Anti-migration anchor 锚定剂 | Cationic organoclay（quaternised bentonite）1.2 wt %，**≤ 1.5 %** | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Acid loading ceiling 加酸上限 | ~8 wt % micronised citric acid — **past this is counter-productive** | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Kinetics 动力学 | deep violet; irreversible（once violet, always violet） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Acceptance: BM insult | ΔE*ab ≥ 15 within 90 s（lane 概念口径） | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| Acceptance: urine challenge | ΔE*ab ≤ 5 at 4 h（lane 概念口径） | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| False positive target | < 2 % | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| False negative target | < 10 % breastfed / < 20 % formula-fed | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| Colour separation rule | ≥ 6 Ostwald numbers; violet reserved for BM alone | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Backsheet optics 底膜光学 | film 30–80 % light transmittance；outer nonwoven ≥ 50 %；> 80 % 则妈妈直接看到便便 | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |

> ⚠️ **口径差异（重要）**：**同一主题两条来源给出两套机制口径** —— [[BM Urine Indicator Concept（尿+便双指示概念）]] 的 Lane A 走「可滴定酸度（缓冲容量的酸碱滴定）」，本页记载的 [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] 走「蛋白误差（结合效应）」。两者**触发分子与判据不同**，库内**并存不裁决**，见下方矛盾记录。
> 另：**肾功能异常（nephrotic urine）为边界案例**，须以 10,000 mg/L 白蛋白挑战验证 → `[待验证]`。

## Adjacent Concepts 相邻概念

- 同族通道：[[Titratable Acidity Lane（可滴定酸度通道）]]、[[Bile Pigment Mordant Lane（胆色素媒染通道）]]、[[Wetness Indicator Ladder（尿湿指示阶梯）]]
- 干扰源：[[Odour-Control Granular Interference（除臭颗粒干扰）]]
- 工艺载体：[[Hot-Melt Slot Coating（热熔狭缝涂布）]]
- 既有页对照：[[变色油墨]]
- 选型：[[Urine Indicator vs BM Indicator（尿湿指示 vs 便指示）]]

## Lessons 经验教训

> ⚠️ **矛盾记录（2026-09-29）**：[[BM Urine Indicator Concept（尿+便双指示概念）]] 与 [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] 对「便指示的触发机制」给出**不同主张**——前者为「可滴定酸度（缓冲容量）＋胆色素媒染」双通道，后者为「可溶性蛋白（蛋白误差）」单通道。两者**不擅自裁决**，待人工确认（可能是产品代际差异：后者自述为面向复合透气底膜的「独立」方案）。见 [[Urine Indicator vs BM Indicator（尿湿指示 vs 便指示）]]。

> ✅ Verification（2026-09-29，来源 [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]）：本页机理、四重防线与「350× 缓冲余量」全部逐条来自该源摘要页，未做外推；对健康尿 33× 余量与对粪便液 2× 余量的口径均按原文记录。

- **教训一（分清「读什么」）**：**蛋白误差读的是结合事件，不是酸碱度**——这就是它能对 pH 5.5→9.0 的尿完全无响应的原因；把两条通道都做成 pH 型是本项目最容易犯的设计错误。
- **教训二（选择性旋钮只有一个）**：想调触发阈值，**只能改染料负载**（D × C*），不能改缓冲强度——缓冲只负责把微环境钉在 pH 3.0。
- **教训三（迁移锚定必须换料）**：可溶性季铵盐会**模拟蛋白**并在包内预显紫；这是从既有尿显配方直接「借用基料」时最隐蔽的坑。
- **教训四（疏水性胜过酸量）**：保护微环境靠疏水基体（松香/FT 蜡）把碱挡在外面，不靠往配方里堆柠檬酸；超过 ~8 wt% 反而堵垫片。
- **教训五（几何比化学难）**：假阴性只需几何失效——粪液到不了通道，化学再准也没用。

## Sources 来源

- [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/BM/BM_Indicator_Design_Viscosity_Cost.pptx.md`
- [[BM Urine Indicator Concept（尿+便双指示概念）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/BM/BM_Urine_Indicator_Concept.pptx.md`

## Related Sources 关联来源

- [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]

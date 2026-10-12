---
type: concept
title: "Odour-Control Granular Interference（除臭颗粒干扰）"
domain: [卫材研发, 芯体设计, 化学兼容]
status: growing
updated: 2026-09-29
tags: [除臭颗粒, 沸石, 环糊精, 便指示, 化学兼容, 假阳性, 碱度]
---

# Odour-Control Granular Interference（除臭颗粒干扰）

> One-line definition 一句话定义：The **self-inflicted** competition between an odour sorbent and a colour indicator inside the same core — the sorbent was added to scavenge the odour molecules, and those are exactly the molecules a head-space-reading indicator would need; if the sorbent is also alkaline, it will pre-develop a buffered indicator lane inside the pack.
> （中文：同一芯体内**除臭吸附剂与颜色指示器之间的「自造」竞争**——吸附剂本是为清除异味分子而加入，而那些恰是任何「读气相」指示器所需的分子；若吸附剂同时呈碱性，还会在包内就把缓冲型指示通道预显色。）

## Mechanism / Structure 机理 / 结构拆解

1. **The problem the granular created（颗粒制造出的问题）**：the odour granular (zeolite / silica / cyclodextrin in the core) scavenges NH₃, amines, H₂S and volatile fatty acids. That removes **Mom's learned head-space signal for a BM** — she now only finds out at the scheduled change. Change intervals stretch, BM sits against skin longer, faecal protease + lipase and rising pH drive dermatitis, and the rash/leak blame lands on the diaper rather than on the missing cue.
2. **Why any head-space indicator is dead on arrival（任何气相指示器为何一出生就死）**：the odour sorbent and the indicator want the same molecules. Intermediate zeolites are **chosen precisely because** they have high capacity for amine-type odours over a **700–800 m²/g surface**, and cyclodextrin complexes the same small organics. Any indicator that reads BM from the head-space — an ammonia-sensitive dye, a VFA-sensitive dye reading vapour — is **being starved by the very additive that created the problem**.
3. **Design rule（设计铁律）**：the BM indicator must **read the liquid phase, by direct contact**, and must be **physically decoupled** from both the odour granular and the SAP — keep the granular **≥ 20 mm MD** clear of the sampling head, and never in the same z-layer as the wick.
4. **The alkaline-granular failure mode（碱性颗粒失效模式）**：an alkaline granular can **titrate the BM lane's buffer from the inside** through the dusting layer over shelf life. This is described as the **single most important interference** and the **No. 1 risk in the programme**.
5. **Granular chemistry screen（颗粒化学筛查）**：

   | Granular 颗粒 | pH | Risk | Why 原因 |
   |---|---|---|---|
   | Zeolite (4A / 13X) | 9–11 | **HIGH** | Strongly alkaline slurry — will titrate the buffer through the dusting layer over shelf life |
   | Sodium bicarbonate 碳酸氢钠 | 8.3 | **HIGH** | Mobile, water-soluble, migrates readily — worst case for a buffered lane |
   | Activated carbon 活性炭 | 6–10 | MEDIUM | Grade-dependent alkalinity, **and it adsorbs the dye** — expect greying as well as drift |
   | Cyclodextrin 环糊精 | 6–7 | LOW | Neutral, non-migrating — **the compatible choice if the odour performance holds** |
   | Ion-exchange resin, H⁺ form | 4–6 | LOW | Acidic form is actively helpful — it reinforces the lane's own buffer |

6. **Screen-it-first protocol（先筛查的规程）**：(i) slurry 5 g granular in 50 mL deionised water, 1 h, 25 °C — measure pH and titratable base to pH 4; (ii) **accept only if slurry pH ≤ 7.5 and titratable base ≤ 0.2 mmol/g**; (iii) build a full diaper and age it 8 weeks at 40 °C / 75 % RH, grading the lane weekly 0–5 and rejecting at grade 1; (iv) if the granular fails, **the fix is a barrier — move it above the core wrap, or micro-encapsulate it — not more acid in the lane**.
7. **The test everyone forgets（所有人都会忘的测试）**：run the whole matrix on a diaper that **actually contains the odour granular, at full dose, aged**. A lane validated on a granular-free construction proves nothing about this product: the sorbent is a competing reagent, and its capacity changes over shelf life because zeolite and activated carbon keep adsorbing airborne organics in storage unless hermetically packed. Test **three ages — fresh, 6 months, 12 months — and two granular doses**. If the lane response drifts with granular age, **the clearance geometry is the problem, not the chemistry**.

（中文：①颗粒制造的问题——除臭颗粒（沸石/硅胶/环糊精）吸附 NH₃、胺类、H₂S 与挥发性脂肪酸，从而抹掉了妈妈赖以判断便便的气味线索，她只能在既定换尿时间才发现；换尿间隔被拉长、便便更久贴肤、粪便蛋白酶与脂肪酶及 pH 上升推动皮炎，且红臀/漏液的责任落到纸尿裤而非消失的线索上；②任何气相指示器为何「出生即死」——吸附剂与指示器争夺同一批分子，沸石正因在 700–800 m²/g 表面上对胺类异味容量高而被选用，环糊精也络合同一批小分子有机物；任何从顶空读便便的指示器（氨敏染料、读蒸气的 VFA 敏染料）都会被**制造问题的那个添加剂活活饿死**；③设计铁律——便指示必须**直接接触读液相**，并与除臭颗粒和 SAP 物理隔离：颗粒离采样头 ≥20 mm（MD），且永不与芯吸条同一 z 层；④碱性颗粒失效模式——碱性颗粒会通过粉尘层在货架期内**从内部滴定便通道缓冲体系**，原文称之为最重要的干扰与项目第一大风险；⑤颗粒化学筛查表见上（沸石 4A/13X 与碳酸氢钠为高风险，活性炭中风险且会吸附染料，环糊精与 H⁺ 型离子交换树脂为低风险、后者反而有益）；⑥先筛查规程——5 g 颗粒 + 50 mL 去离子水、1 h、25 ℃ 测 pH 与滴至 pH 4 的可滴定碱，**仅当浆液 pH ≤7.5 且可滴定碱 ≤0.2 mmol/g 才接受**；随后做整片并在 40 ℃/75% RH 下老化 8 周，每周 0–5 级评分、1 级即拒；若颗粒不合格，**修法是加阻隔（移到芯包上方或微胶囊化），而不是往通道里加更多酸**；⑦所有人都会忘的测试——整套矩阵必须在**真正含除臭颗粒、足量、且老化过**的整片上跑；在无颗粒结构上验证过的通道对本产品毫无证明力，因为吸附剂是竞争性试剂，且其容量随货架期变化（沸石与活性炭在仓储中会持续吸附空气中有机物，除非密封包装）；须测**新鲜/6 个月/12 个月三个库龄 × 两种颗粒用量**；若通道响应随颗粒库龄漂移，**问题在隔离几何，不在化学**。）

## Key Parameters 关键参数表

| Parameter 参数 | Value / range 数值/范围 | Source 出处 |
|---|---|---|
| Granular surface area 颗粒比表面 | 700–800 m²/g（intermediate zeolites） | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| Molecules scavenged 被清除的分子 | NH₃, amines, H₂S, volatile fatty acids（VFA） | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| Clearance rule 间隙规则 | granular ≥ **20 mm MD** clear of the sampling head；never in the same z-layer as the wick | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| Barrier 阻隔层 | 18 gsm PE barrier under the wick；construction HMA as a solid 12 mm film（MD 240–405） | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| What the barrier does / does not do | 防 SAP 抢走样本水；**不**阻尿到达采样头（拒尿是化学的职责，不是几何的） | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| Slurry screen acceptance 浆液筛查合格线 | pH ≤ 7.5 **and** titratable base ≤ 0.2 mmol/g（5 g in 50 mL DI water, 1 h, 25 °C） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Ageing validation 老化验证 | 8 weeks at 40 °C / 75 % RH, graded weekly 0–5, reject at grade 1 | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Shelf-age matrix 库龄矩阵 | fresh / 6 months / 12 months × two granular doses | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| Zeolite 4A / 13X | pH 9–11 → **HIGH** | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Sodium bicarbonate | pH 8.3 → HIGH（mobile, water-soluble） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Activated carbon | pH 6–10 → MEDIUM（adsorbs the dye → greying） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Cyclodextrin | pH 6–7 → LOW（compatible choice） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Ion-exchange resin, H⁺ form | pH 4–6 → LOW（actively helpful） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Preferred remediation 首选补救 | barrier（move above the core wrap）or micro-encapsulation — **not more acid** | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Related manufacturing change 相关制造变更 | Core: low-basis-weight faecal conduit aligned to the BM lane；odour granular requires an alkalinity screen before it goes near the lane | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| Related cost item 相关成本项 | Construction HMA barrier film：50 mg/diaper，US$0.14 / 1,000 | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| Sibling phenomenon in existing library 库内同族现象 | 尿显线的既有干扰逻辑（热致变色阈值 >87 °F；异味控制四路线）见 [[智能尿裤功能层专利地图]] | [[智能尿裤功能层专利地图]] |

> ⚠️ **No unsourced parameters**：以上全部来自本批源摘要页。**除臭颗粒自身的除臭性能与通道化学的联合优化窗口**库内无数据 → `[待验证]`。

## Adjacent Concepts 相邻概念

- 受影响通道：[[Protein Error of pH Dye（pH 染料的蛋白误差）]]、[[Bile Pigment Mordant Lane（胆色素媒染通道）]]、[[Titratable Acidity Lane（可滴定酸度通道）]]
- 与尿湿指示的关系：[[Wetness Indicator Ladder（尿湿指示阶梯）]]
- 工艺载体：[[Hot-Melt Slot Coating（热熔狭缝涂布）]]
- 既有页对照：[[智能尿裤功能层]]（抗菌除臭功能层与除臭四路线）、[[SAP错峰膨胀]]、[[分区密度设计]]
- 选型：[[Urine Indicator vs BM Indicator（尿湿指示 vs 便指示）]]

## Lessons 经验教训

> ✅ Verification（2026-09-29，来源 [[BM Urine Indicator Concept（尿+便双指示概念）]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]）：两份文档在**同一风险上独立互证**——前者称之为「设计铁律 / 决定整个设计的陷阱（颗粒与指示器争分子）」；后者称之为「本项目第一大风险 / 会杀死整个项目的唯一一件事（碱性颗粒把缓冲通道滴定显色）」。二者均要求 ≥20 mm 纵向隔离与整片老化验证。本页结论与来源一致。

- **教训一（系统性副作用）**：**除臭颗粒解决了一个问题、制造了另一个问题**——它把可感知信号换成了不可感知信号。任何「升级吸附/除臭」的改动都必须回头检查它是否吃掉了某个指示信号。
- **教训二（干扰是物理的，不是配方的）**：首选补救是**阻隔（移到芯包上方/微胶囊化）**，不是往配方里加酸。用化学去对抗一个会持续渗入的碱源，只是一场必败的军备竞赛。
- **教训三（验证必须带干扰源）**：**在无颗粒结构上验证过的通道对本产品毫无证明力**——这是本主题最容易被跳过、也最容易导致上市后失效的一条。
- **教训四（库龄是变量）**：吸附剂容量随货架期变化（仓储中持续吸附空气有机物），所以隔离几何必须用**三个库龄 × 两种用量**来验证。
- **教训五（选料顺序）**：若除臭性能允许，**环糊精（pH 6–7、不迁移）** 是与指示通道最兼容的选择；H⁺ 型离子交换树脂甚至有益。

## Sources 来源

- [[BM Urine Indicator Concept（尿+便双指示概念）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/BM/BM_Urine_Indicator_Concept.pptx.md`
- [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/BM/BM_Indicator_Design_Viscosity_Cost.pptx.md`

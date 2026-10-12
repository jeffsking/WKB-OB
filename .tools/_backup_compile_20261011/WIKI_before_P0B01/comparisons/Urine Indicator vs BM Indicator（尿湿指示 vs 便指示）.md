---
type: comparison
title: "Urine Indicator vs BM Indicator（尿湿指示 vs 便指示）"
subjects: ["[[Wetness Indicator Ladder（尿湿指示阶梯）]]", "[[Protein Error of pH Dye（pH 染料的蛋白误差）]]"]
dimension: 综合
updated: 2026-09-29
tags: [尿显, 便指示, 成本对比, 供应链风险, 双读出, 除臭颗粒]
---

# Urine Indicator vs BM Indicator（尿湿指示 vs 便指示）

> 对比对象：同一片纸尿裤上的**两个读出**——尿湿/载量指示（经典 pH 热熔阶梯）与便指示（BM lane）。
> 回答「为什么这两个功能必须在物理位置、色语言、触发化学上完全分离，以及各自的成本与供应链风险在哪」。
> 数字全部溯源至源摘要页；无来源项标 `[待验证]`。

## 对比维度表 Comparison Table

> 必含「成本」与「供应链风险」两列。

| 维度 | [[Wetness Indicator Ladder（尿湿指示阶梯）]] 尿湿指示 | [[Protein Error of pH Dye（pH 染料的蛋白误差）]] 便指示（BM lane） | 依据 Source |
|---|---|---|---|
| **成本（材料）** | US$0.07 / 1,000 片（0.0081 g/片 @ 30 g/m²，料价 ≈ US$8/kg） | US$0.142 / 1,000 片（40 mg/片 @ 20 gsm，混配料价 US$3.56/kg）；染料本身仅 US$0.02/1,000 | [[BM Urine Indicator Concept（尿+便双指示概念）]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| **成本（合计口径差异，两代概念）** | 代际一（电+便双通道概念）：阶梯 0.07 / 1,000 | 代际一：双通道 0.10 / 1,000（**两通道合计**）＋ADL 尾 0.23＋阻隔膜 0.14 → 总 US$0.54/1,000（0.00054 US$/片）<br>代际二（独立单通道）：**US$0.567 / 1,000**（0.057 ¢/片） | [[BM Urine Indicator Concept（尿+便双指示概念）]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| **成本（新增 capex）** | **US$0**：既有 WI 工位重编程为 3 段虚线即可，无套准、无新设备 | 代际一：US$38–60 k（BM 双通道 30–45 k、采样芯吸条 8–15 k 工装、色彩 QA 20–35 k 可选）<br>代际二：US$76,900（core scope）／US$108,900（含在线色彩验证） | [[BM Urine Indicator Concept（尿+便双指示概念）]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| **成本（OEE / 运行）** | 无 OEE 损失（沿用既有工位） | 代际二：**OEE allowance 0.30 % = US$0.240/1,000——本项最大成本**；capex 摊销 US$0.109/1,000（707 M 片/3 年）；年化运行成本 ≈US$108 k（3 亿片/年，代际一口径） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]、[[BM Urine Indicator Concept（尿+便双指示概念）]] |
| **成本（相对出厂价占比）** | 极低（属既有尿显条） | 代际一：0.6–0.9 % of a typical US$0.06–0.09 ex-works diaper；相对已带常规尿显条的规格**增量 US$0.36/1,000** | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| **供应链风险（工艺成熟度）** | **低**：proven, commodity chemistry；既有热熔尿显工位，免套准连续走料 | **中-高**：须新增独立低温熔化罐（10 L，独立回路）+ 接触式狭缝喷嘴 + 冷却背辊 + 伺服随速泵 + 按需胶珠阀；**非自由间隙预计量涂布**（Ca = 272，最大自由间隙 44 µm ≪ 幅材抖动 ±150 µm） | [[BM Urine Indicator Concept（尿+便双指示概念）]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| **供应链风险（基材/热约束）** | 低：底膜印刷侧，无特殊热限 | **高**：温度上限由**透气膜**而非化学决定——微孔 CaCO₃ 填充 PE 膜在约 90 ℃ 以上退火即不可逆损失 WVTR（线上看不见，一周后在恒温恒湿箱才发作）；须加冷却背辊（+约 15 K 余量）并逐设定点测 WVTR | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| **供应链风险（化学兼容 / 干扰源）** | 中：可溶性季铵盐锚定剂在蛋白误差通道中**会模拟蛋白并预显紫**；底膜须低色相增粘树脂（泛黄会掩蔽干态） | **极高（项目第一大风险）**：碱性除臭颗粒会**从内部滴定缓冲体系** —— 沸石 4A/13X pH 9–11 HIGH、碳酸氢钠 pH 8.3 HIGH、活性炭 pH 6–10 MEDIUM（且吸附染料）、环糊精 pH 6–7 LOW（兼容）、H⁺ 型离子交换树脂 pH 4–6 LOW（有益） | [[Protein Error of pH Dye（pH 染料的蛋白误差）]]、[[Odour-Control Granular Interference（除臭颗粒干扰）]] |
| **供应链风险（原料可得性）** | 低：溴酚蓝等属常规染料；酸（异硬脂酸/壬二酸/12-羟基硬脂酸）为大宗 | 中：溴甲酚紫 0.025 wt % 属常规；但**有机黏土（季铵化膨润土）替代可溶性季铵盐**属定制选型；柠檬酸须微粉化 d90 < 15 µm、有机黏土须过 25 µm 筛（垫片 ≥ 10 × d90） | [[Wetness Indicator Ladder（尿湿指示阶梯）]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| **供应链风险（读出被吞掉）** | 中：标准 TiO₂/CaCO₃ 填充底膜（15–18 gsm）会吞掉信号 → 须留未印刷读出窗 | 中：底膜须重新规格化为**光透过率 30–80 %**、外层无纺布在通道足迹内 **≥ 50 %**；> 80 % 则妈妈直接看到便便 | [[BM Urine Indicator Concept（尿+便双指示概念）]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| **性能（判别量）** | pH（卤致变色）——**WEAK** 作为便判别量：约半数配方奶便与多数日终尿落在同一 pH 窗口 | **可溶性蛋白（蛋白误差）** —— 粪便液 10,000–40,000 mg/L vs 健康婴儿尿 < 150 mg/L；**33× 尿余量、2× 粪便余量、34× 皮肤安全上限余量** | [[BM Urine Indicator Concept（尿+便双指示概念）]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| **性能（触发点如何设定）** | 由 pH 调节酸决定（**不是染料**） | 仅由**染料负载**决定：D × C* ≈ 2,500；设计点 0.50 µg/cm² → 触发 5,000 mg/L | [[Wetness Indicator Ladder（尿湿指示阶梯）]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| **性能（状态数 / 读出形态）** | **3 段载量仪表**（设计载量的 ~25–35 % / 中间 / 接近满载），计数式读出 | 单通道（代际二）**一次性深度紫色**（不可逆）；代际一为**双通道**（可滴定酸度 + 胆色素媒染），「两通道同时变深＝立即更换，单通道＝可疑」 | [[Wetness Indicator Ladder（尿湿指示阶梯）]]、[[Protein Error of pH Dye（pH 染料的蛋白误差）]]、[[Titratable Acidity Lane（可滴定酸度通道）]] |
| **性能（响应时间 / 灵敏度）** | 目标可见变化 < 30 s | 代际二：验收 ΔE*ab ≥ 15 within 90 s；真实粪便面板 ≥ 95 % 检出（15 min）；代际一：10–30 min（蛋白酶裂解膜 C 为 10–30 min） | [[Wetness Indicator Ladder（尿湿指示阶梯）]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| **性能（可逆性）** | 不可逆（尿湿后保持变色；pH 阶梯随载量递增） | **不可逆**（「once violet, always violet」）——有机黏土锁定络合物，使其在更换前不能褪色或迁移 | [[Protein Error of pH Dye（pH 染料的蛋白误差）]] |
| **性能（误报指标）** | 不适用（作为仪表读出） | 假阳性 < 2 %；假阴性 < 10 % 母乳 / < 20 % 配方奶（原文要求「state it, don't hide it」） | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| **位置（物理分离）** | 前裆，MD 60–195（3 段 2 × 45 mm 虚线） | 后腰，底膜内表面，MD 405–440（2 × 3 × 35 mm）；采样头 MD 250–280；芯吸条 MD 245–440 | [[BM Urine Indicator Concept（尿+便双指示概念）]] |
| **色语言（不得混用）** | 黄 → 蓝（溴酚蓝 / 溴甲酚绿） | **紫色为便通道独占**；色相间须 ≥ 6 个 Ostwald 数；纸尿裤上任何图形/弹性体/印刷件不得使用紫色 | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |
| **适用场景** | 「在对的时间更换」——把更换时机从猜测变为读数；同时是**免费的现场诊断**（段 3 从不触发 = MD 分布不足、前区 SAP 过吸） | 「立即更换」——**覆盖**阶梯：便事件无论还剩多少尿液容量都必须更换；解决「除臭颗粒让妈妈失去气味线索」这一具体失效 | [[BM Urine Indicator Concept（尿+便双指示概念）]]、[[Odour-Control Granular Interference（除臭颗粒干扰）]] |

> 尾注：本表所有数字均来自 [[BM Urine Indicator Concept（尿+便双指示概念）]]、[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] 两份源摘要页；颜色/位置/验收口径同源。
> ⚠️ **两代概念口径差异（须并读，不得混用）**：**代际一**（[[BM Urine Indicator Concept（尿+便双指示概念）]]）主张**双通道便指示**（可滴定酸度 A + 胆色素媒染 B），总成本 US$0.54/1,000；**代际二**（[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]）主张**单通道蛋白误差**且面向复合透气底膜，总成本 US$0.567/1,000。**成本数字接近但机制不同**，两行数据不可相加 → 见下矛盾记录。

> 🔴 **manual_review（2026-09-29）**：本对比页引用了**两代概念的成本模型、capex 与 OEE 让渡数字**，并涉及**内部专利申报角度与 FTO 规避清单**（US6342037、WO2016120876、US12396899 族等），属 AGENTS.md §5 边界。页面只保留**机制、位置、色彩与成本口径**用于技术判断，**完整成本表与专利申请角度不对外引用**；原文留存于 `RAW/ima_sync/个人知识库/WKB/Projects/BM/`。

## 各自适用场景 Where Each Fits

- **[[Wetness Indicator Ladder（尿湿指示阶梯）]]**：**任何一片纸尿裤都该有**——它是既有量产技术，零新增 capex、零新增料类，把「何时更换」从猜测升级为读数，还免费附带一个 MD 分布诊断能力。它的职责是**剂量与节奏**。
- **[[Protein Error of pH Dye（pH 染料的蛋白误差）]]**：**只在「除臭颗粒已上车」的产品上才必需**。它解决的不是一般湿感问题，而是**除臭颗粒把气味线索抹掉后留下的空白**——因此它的存在理由是**宣称与投诉规避**，不是降本或功能升级。它的职责是**事件类型判别**。
- **两者不得合并**：物理位置分离（前裆 vs 后腰）、色语言分离（黄→蓝 vs 独享紫）、触发化学分离（质子 vs 蛋白结合）。原文列为 MEDIUM 风险「caregiver misreads two indicators as one」，缓解措施正是「separate them physically and give them different colour languages, **not different shades of the same one**」。

（中文：尿湿阶梯——任何一片纸尿裤都该有，零新增 capex 与料类，职责是剂量与节奏，并免费附带 MD 分布诊断；便指示——只在「除臭颗粒已上车」的产品上才必需，职责是事件类型判别，其存在理由是宣称与投诉规避而非降本；两者不得合并，须在物理位置、色语言、触发化学三处分离——原文把「护理者把两个指示读成一个」列为中等风险，缓解措施正是物理分离 + 不同色语言，而**不是同一色的深浅**。）

## 结论 Conclusion

**这两个读出回答的是两个不同问题，因此不能合并成一个指示器。** 尿湿阶梯回答「**还剩多少容量**」（剂量/节奏，载体是已量产的 pH 热熔条，成本近零）；便指示回答「**这是不是便便**」（事件类型，载体是须新增工位与独立熔化罐的蛋白误差通道，成本 0.057 ¢/片，且主要成本是 OEE 而非化学）。**第二个读出只有在「除臭颗粒」这个前提下才成立**——因为正是除臭颗粒抹掉了妈妈的气味线索；换言之，**便指示的成本应记在「除臭升级」这一决策头上，而不是记在「智能功能」头上**。这也是原文的自我定位：**"this is not a cost-out project — it is a claim and a complaint-avoidance project"**。

（中文：两个读出回答两个不同问题，不能合并——阶梯答「还剩多少容量」，便指示答「这是不是便便」；后者只在除臭颗粒这一前提下成立，其成本应记在「除臭升级」的决策头上，而非「智能功能」头上。原文自述即：「这不是降本项目，而是宣称与投诉规避项目」。）

## 来源 Sources

- [[BM Urine Indicator Concept（尿+便双指示概念）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/BM/BM_Urine_Indicator_Concept.pptx.md`
- [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/BM/BM_Indicator_Design_Viscosity_Cost.pptx.md`
- [[Wetness Indicator Ladder（尿湿指示阶梯）]]、[[Protein Error of pH Dye（pH 染料的蛋白误差）]]、[[Titratable Acidity Lane（可滴定酸度通道）]]、[[Bile Pigment Mordant Lane（胆色素媒染通道）]]、[[Odour-Control Granular Interference（除臭颗粒干扰）]]（概念页）

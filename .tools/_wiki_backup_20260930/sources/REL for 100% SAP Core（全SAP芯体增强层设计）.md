---
type: source
title: "REL for 100% SAP Core（全SAP芯体增强层设计）"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Structure/NEW REL 4.pptx.md
original_link: ""
date_published: 2025
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "文件定位 = REL（Reinforcement Enhancement Layer，增强层）设计专稿：回答「在 100% SAP、无绒毛浆芯体中，增强层凭什么起作用」，覆盖设计原理、纤维科学、ATB（Air-Through Bonding，穿透热风粘合）工艺参数与 1st–4th void 的 KPI"
  - "第一性指标 First metric = **空体积（void volume）**：定义为每克非织造布在体重载荷下（0.5–1 kPa）的开放空间 cm³/g，目标 **80–117 cm³/g @0.5 kPa**；原文强调「若第 1 次冲击后空体积坍塌，任何纤维工程都救不回第 2/3/4 次」"
  - "REL 五项职责 Five jobs：①第 1 次冲击前建立开放空隙通道 ②在 0.5–1 kPa 体载下维持结构高度 ③冲击之间恢复空体积（压缩回复 >85%）④沿 MD 把尿液输离摄入区 ⑤快速把液体交给 SAP 并抗回渗"
  - "四纤维配方 Four-fibre blend（35–45 gsm）：**ES 2.2D/38mm 50%（热粘合基体）＋ PTT/PET S/S 4.0D/51mm 28%（回弹引擎）＋ 偏心中空 PE/PET 6.0D/51mm 14%（蓬松与 MD 输运）＋ 非水溶 PVA 1.5D/38mm 8%（Z 向骨架）**"
  - "理论六柱 Six pillars：Lucas-Washburn 毛细压（ΔP=2γcosθ/r，θ 目标 <30°）、Darcy 定律（k 目标 8,000–15,000 darcy）、弹性梁理论（PTT 螺旋卷曲＝预成型弹簧）、双峰孔径梯度（大孔 >40 µm 走 MD、小孔 10–20 µm 保液）、Z 向骨架理论（PVA 拉伸模量约 25 GPa，类比钢筋）、双峰纤维长度（38 mm 建 XY 键合面、51 mm 建 Z 向拱与 MD 取向）"
  - "ATB 工艺窗口 Process window：**炉温 148–155 ℃、风速 2.5–3.2 m/s、线速 15–22 m/min、入炉过喂 8–12%、冷却区 <60 ℃、压辊间隙 = 厚度 +10%、克重 35–45 gsm（±2）、厚度 4.8–5.5 mm（冷态测）**"
  - "三条高危工艺风险 HIGH-severity risks：PTT/PET 的 6–10% MD 收缩（须过喂补偿）、过粘合（>158 ℃ 会熔死 PE 皮层并永久杀死 PTT 卷曲回复）、以及 PVA 静电与迁移（须 ES ≥50% 保证键合网络）"
  - "KPI 门槛（Pass / Excellent）**：空体积 >80 / >100 cm³/g；压缩回复 >80% / >88%；1st/2nd/3rd STT <3.5/<6.0/<9.0 s 与 <2.5/<4.0/<6.0 s；第 3 次回渗 <2.0 / <1.5 g；MD 渗透率 >6,000 / >9,000 D；厚度 >4.0 / >4.8 mm"
  - "PVA 硬性要求 PVA hard requirement：必须是**非水溶（insoluble，缩醛化）**牌号，并以 **80 ℃ 水浸 30 min 不溶**验证；可溶性亲水整理会在第 1 次冲击后被洗脱，导致第 2 次起 STT 失效"
pages_linked: ["[[REL增强层]]", "[[并列复合自卷曲纤维]]", "[[分区密度设计]]", "[[COCO芯体平台]]", "[[热风粘合无纺布]]", "[[IPC BCC OI Portfolio（开放创新项目组合）]]"]
aliases: ["REL for 100% SAP Core（全SAP芯体增强层设计·四纤维方案）"]
---

# REL for 100% SAP Core（全 SAP 芯体增强层设计）

## 一句话定位 One-line positioning

本库 **REL（Reinforcement Enhancement Layer）的原理级主源**：一份把「为什么全 SAP 芯体必须有 REL」「四纤维各自的物理角色」「ATB 工艺窗口」「1st–4th void KPI」串成完整链条的设计稿。回答 REL 相关问题时，**本页与 [[REL增强层]] 需成对读取**。

## 摘要 Summary

文件从结构对比切入：传统芯体为 3 层（芯包 + SAP/绒毛浆混合 + 芯包），而 **100% SAP 芯体为 5 层**（芯包 / 上层 SAP / **REL** / 下层 SAP / 芯包）——REL 夹在两层 SAP 之间，**在 SAP 吸液之前先提供液体可穿行的空隙，从而避免表面凝胶阻塞**。文章列出缺 REL 的五种失效模式（SAP 凝胶阻塞、无空体积导致积液、Z 向坍塌、MD 分布差、回渗），并给出 REL 的五项职责与「空体积」这一唯一第一性指标。理论部分以六柱框架展开（毛细、Darcy、弹性梁、双峰孔径、Z 向骨架、双峰长度），纤维部分给出四种纤维的旦数/长度/卷曲/整理/ATB 行为，工艺部分给出炉温、风速、线速、过喂、冷却、压辊间隙等参数与逐纤维的 ATB 行为说明，最后给出风险矩阵、KPI 矩阵、五阶段试产协议、五档配方变体与「八种常见设计错误」。

## 提炼的数字与结论 Key figures & conclusions

| Item 项目 | Value / Conclusion 数值·结论 | Note 备注 |
|---|---|---|
| 芯体构型 Architecture | 传统 3 层 → **100% SAP 5 层**（REL 居中） | REL 位于上下两层 SAP 之间 |
| 空体积目标 VV target | **80–117 cm³/g @0.5 kPa**；判读区间 95–110 cm³/g | 第一性指标 |
| 冲击间空体积衰减 VV decay | 1st ~100% → 2nd ~88% → 3rd ~82% → 4th ~75% | 四次冲击的生命周期 |
| 压缩回复目标 Recovery | **>85%（4 次重复压缩 @1 kPa）**；KPI 表 Pass >80%、Excellent >88% | PTT 螺旋卷曲提供弹簧效应 |
| 渗透率目标 Permeability | **8,000–15,000 darcy**（正文）/ KPI 表 Pass >6,000 D、Excellent >9,000 D | 两处口径不同，见下「口径提示」 |
| 毛细接触角 Contact angle | 目标 **<30°**（耐久亲水整理）；PVA 纤维本身 **<20°** | Lucas-Washburn 输入 |
| 配方 Blend | ES 2.2D/38mm **50%** ＋ PTT/PET S/S 4.0D/51mm **28%** ＋ 偏心中空 6.0D/51mm **14%** ＋ 非水溶 PVA 1.5D/38mm **8%** | 克重 35–45 gsm |
| PTT 卷曲激活 Crimp activation | 约 **145 ℃**；卷曲数由 pre 8–12 /25mm → post ATB 50–70 /25mm | 伴随 6–10% MD 收缩 |
| PVA 模量 Modulus | 拉伸模量约 **25 GPa**（对比 PE 0.2 GPa、PET 2.8 GPa） | 类比混凝土中的钢筋 |
| ATB 窗口 Process window | 炉温 **148–155 ℃**；风速 **2.5–3.2 m/s**；线速 **15–22 m/min**；过喂 **8–12%**；冷却 **<60 ℃**；压辊间隙 = 厚度 +10% | 三者（温度/风速/过喂）被明确为「实验室设计能否活到量产」的决定项 |
| 克重/厚度 Basis weight & loft | 35–45 gsm（±2 gsm 均匀性目标）；厚度 **4.8–5.5 mm**（冷态测） | — |
| KPI（Pass / Excellent） | 空体积 >80 / >100；回复 >80% / >88%；STT1/2/3 <3.5/<6.0/<9.0 与 <2.5/<4.0/<6.0 s；回渗@3rd <2.0 / <1.5 g；MD 渗透 >6,000 / >9,000 D | 方法：EDANA WSP 10.1 / 70.3 / 80.10 / 120.6 / 130.1 等 |
| SAP 粒径建议 | **≤300 µm**（降低与 REL 的毛细竞争） | MD 分布设计项 |
| 五档变体 Variants | A 基线（100% ES）／B +18%（70 ES + 30 PTT）／**C +39% 推荐（四纤维）**／D +27%（58/24/12/6）／E +31%（可持续性：PP/PP+ 取代 PTT/PET 做单材 PP 路线） | 相对成本升幅，见下 |
| 高危风险 HIGH risks | ①PTT MD 收缩 6–10%（过喂补偿或降至 22–24%）②过粘合（>158 ℃ 熔死皮层、永久杀死卷曲回复）③（MED）中空纤维 >14% 导致布面不匀 | 风险矩阵原表共 7 项 |
| 八忌 Mistakes | 100% ES（回复仅约 60%）／过粘合／中空 >14%／**在 ES 上用水溶性亲水整理（第 2 次冲击起 STT 失效）**／… | 「Top 8」段 |

> 🔴 **manual_review（2026-09-29）**：本资料含**逐纤维的 FOB 单价（约 $1.00–3.80/kg）与成本到岸测算（RMB/ton、每片增量）**，属报价与成本类信息。依 AGENTS.md §5，本页**只保留相对关系**（五档变体的成本升幅百分比与推荐档位），**不落具体单价与每片成本**；完整数据留存原文 `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Structure/NEW REL 4.pptx.md`，对外引用前须人工确认。
> ⚠️ **口径提示 Caliber note**：正文中空体积与渗透率同时存在两套表述（VV 80–117 cm³/g 与判读 95–110；k 目标 8,000–15,000 D 与 KPI 表 Pass >6,000 D），**疑为"设计目标 vs 放行门槛"两档**，本页并列登记、不裁决。

## 关键论断（key_claims）

- **在全 SAP 芯体中，REL 是唯一的工程杠杆**：没有绒毛浆做天然输运层，一切输运/回弹/抗塌都要靠纤维工程实现 —— 支撑页：[[REL增强层]]、[[COCO芯体平台]]
- **旦数编码功能 Denier encodes function**：1.5D 骨架分散 / 2.2D 致密键合 / 4.0D 弹性支撑 / 6.0D MD 输运——旦数选错即功能错 —— 支撑页：[[热风粘合无纺布]]、[[并列复合自卷曲纤维]]
- **双峰长度是刻意的 Bimodal length is deliberate**：38 mm 建 XY 键合面、51 mm 建 Z 向拱与 MD 取向 —— 支撑页：[[毛细梯度设计]]
- **ATB 炉是量产临界点**：148–155 ℃ / 2.5–3.2 m/s / 8–12% 过喂这三个数字决定实验室设计能否活到量产 —— 支撑页：[[热风粘合无纺布]]
- **PVA 必须是非水溶牌号，且须以 80 ℃、30 min 验证**：否则亲水整理被洗脱，第 2 次冲击起 STT 崩 —— 支撑页：[[REL增强层]]

## 关联页面 Linked pages

- 概念 Concept：[[REL增强层]]（本页主派生关联，见其追加节）、[[毛细梯度设计]]、[[并列复合自卷曲纤维]]、[[热风粘合无纺布]]、[[分区密度设计]]、[[COCO芯体平台]]、[[ADL（导流层）]]
- 对比 Comparison：[[REL vs ADL（收集传递层 vs 导流层）]]
- 供应商线索 Supplier leads（本页不另建实体页）：ES 纤维（FiberVisions/Indorama、Huvis、Toray、远东新世纪）／PTT-PET（Toray、Teijin Frontier、Indorama、Hyosung）／偏心中空（北京京兰、ES FiberVisions 中空牌号、浙江恒逸、南亚塑胶）／非水溶 PVA（Kuraray KURALON™ K-II、皖维、中石化四川维尼纶）——详见 [[Kuraray（可乐丽）]]
- 组合 Portfolio：[[IPC BCC OI Portfolio（开放创新项目组合）]]

> 📌 OI 互链说明 Open Innovation linkage：本页属 OI Structure 资料层，与 REL 相关 OI 项目直接相关。涉及项目编号时默认采用 [[IPC BCC OI Portfolio（开放创新项目组合）]] 页认定的重构版 19 项口径（`OI-1`~`OI-19`）；引用 `OI-01`~`OI-25` 形式须同句注明出自年度汇报大纲 v7（2026-09-17）。

## 原文 Source file

- 本地路径 Local path：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Structure/NEW REL 4.pptx.md`
- 原文链接 Original link：（无；K-C 内部 PPT）
- 同族资料 Related：[[优化 REL 五纤维配方与穿透热风粘合工艺模拟]]（另一版 REL 方案，克重与纤维构成不同，见 [[REL增强层]] 的矛盾登记）、[[全芯体材料清单与实验计划 v2.0]]

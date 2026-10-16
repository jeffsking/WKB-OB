---
type: concept
title: "Thermochromic Microcapsule (Leuco Dye System)"
domain: [卫材研发, 变色与智能材料]
status: growing
updated: 2026-09-29
tags: [热致变色, leuco染料, 微胶囊, 可逆, 显示点, 面层外表面]
aliases: ["Thermochromic Microcapsule (Leuco Dye System) 热致变色微胶囊（leuco 染料体系）"]
---

# Thermochromic Microcapsule (Leuco Dye System) 热致变色微胶囊（leuco 染料体系）

> **Definition 定义**：A **reversible** colour-change system built from microcapsules containing a three-component mixture — **leuco dye + developer + solvent** — whose colour appears or disappears when the mixture crosses a temperature threshold.（由含三组分混合物——**leuco 染料 + 显色剂 + 溶剂**——的微胶囊构成的**可逆**变色体系；混合物跨越温度阈值时颜色出现或消失。）

## Mechanism 机理

| State 状态 | Physical state 物理状态 | Colour 颜色 |
|---|---|---|
| Below threshold 阈值以下 | Leuco dye + developer + solvent stable; microcapsule intact | Latent / clear or base hue 潜色/透明或底色 |
| At / above threshold 达到或超过阈值 | Electron transfer / phase change 电子转移或相变 | Colour appears or disappears 显色或褪色 |
| On cooling 降温 | Reversible cycle 可逆循环 | Returns to the latent state 回到潜色态 |

Two design variants are used in hygiene: **reversible** type for comfort cues, **irreversible** type for high-temperature / breach alerts.（卫材中两种变体：**可逆型**用于舒适提示，**不可逆型**用于高温/超限告警。）

## Spec implication 规格含义

An activation window of **30–37 °C** covers the meaningful diaper microclimate range, but display points (**32 / 34 / 36 °C**) must be calibrated with in-house bench data — they are consumer-friendly validation targets, not lab constants.（**30–37 ℃** 的激活窗口覆盖有意义的尿裤微气候区间，但显示点（**32/34/36 ℃**）必须以内部台架数据标定——它们是面向消费者的验证目标，而非实验室常数。）

## Key parameter table 关键参数表

| Parameter 参数 | Value 典型值 | Source 出处 |
|---|---|---|
| Activation window 激活窗口 | 30–37 °C, customisable | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| Key display points 关键显示点 | 32 / 34 / 36 °C | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| Response time 响应时间 | ≤120 s to readable | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| Cycle stability 循环稳定性 | ≥10 thermal cycles | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| Contrast 对比度 | ΔE or naked-eye grade | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| Dry background 干态本底 | Low interference — must not be misread as wetness | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| Migration 迁移 | No bleed / stain (hard floor) | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| Skin contact 皮肤接触 | NOT allowed | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| Converting tolerance 转化耐受 | Must survive lamination | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| Form 形态 | Printed stripe or laminated label patch on the outer surface (core-centreline / crotch panel) | [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] |
| Colour script 色彩脚本 | Blue = cool, green = comfort, red = warm | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| Comprehension gate 解读门 | >70% consumer comprehension of too hot / cold / comfort | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| Shelf risk 货架风险 | Premature triggering during storage or transport; UV stability and long-term drift | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| Dry-state difficulty 干态难度 | Dry-state thermal signalling is technically demanding; claim path requires stringent internal bench data | [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] |
| Legacy comparator 历史对照 | leuco systems previously indexed in this KB with threshold >87 °F (~30.6 °C), sensitivity 1–2 °C, ratio leuco:developer:fatty acid ≈1:5:50 | [[变色油墨]]（源：[[智能尿裤功能层专利地图]]） |

> ⚠️ **No unsourced parameters 禁止无来源参数**：本批未给出**具体染料/显色剂化学体系、胶囊粒径、ΔE 实测值**，标 `[待验证]`；温度—色差定量曲线库内无来源。

## Adjacent concepts 相邻概念

- Enabler 使能技术：[[Microencapsulation]]
- Sibling route 同族路线：[[Wetness Indicator Glue]]
- Application 应用：[[Diaper Microclimate]]、[[智能尿裤功能层]]、[[变色油墨]]
- Validation 验证：[[Signal Comprehension Gate]]
- Comparison 对比：[[Thermochromic vs Hydrochromic Wetness-Comfort Indicators]]
- Taxonomy 分类（并发批次）：[[Chromism Taxonomy（变色现象分类）]]（按触发物理量分类；可逆性为第二条轴、阈值为第三条轴）

## Lessons learned 经验教训

> ✅ **Validation（2026-09-29）**：本批两份来源在机理与形态上完全一致——均为"leuco 染料 + 显色剂 + 溶剂微胶囊、可逆相变、印刷条或复合标签片、位于非皮肤面"，且都把**干态热信号**列为技术难点、把 **>70% 解读率**列为出口门（[[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]、[[Diaper Microclimate Visualization Feasibility (Dual-MVP)]]）。与既有 [[变色油墨]] 页记录的 leuco 三组分体系一致，**未出现矛盾**；本页仅补齐阈值带宽、显示点与验收门槛。

- **要点**：温敏路线的成熟度**低于**湿敏路线——无尿裤专用 SKU，"先定义阈值与合规标准者占据 IP 护城河"。
- **风险**：安全侧存在硬性排除项——部分传统温变产品含**微量甲醛**，官方指引排除婴儿直接接触；指示层必须在非皮肤面。
- **待补 `[待验证]`**：耐层压（温度/压力）后的色差保持率；40 °C/75% RH 一周可读性的实测结论。

## Evidence Update 证据追加（2026-09-29 · Areas/IP 第 3 批）

> ✅ 追加（2026-09-29，source 来源 [[US5197958A & US5389093A Wetness Indicating Diaper (Howell)]]）：本批新增一份**把 leuco dye 体系写得很完整的一手专利文献**（US 5,197,958 / US 5,389,093，Howell）。**追加内容为配方与温度的客观摘录，不修改本页既有结论**。其中三条可直接用于配色与失效分析：
>
> 1. **阈值由脂肪酸的熔点决定，且可混用法微调**：来源明文表述为 "the discoloring temperature corresponds to the fusing temperature of a fatty acid"，受热时脂肪酸熔融触发变色、冷却凝固即复原，**两种以上脂肪酸并用可对转变温度作微调**。实测转变温度表：
>
> | Fatty acid 脂肪酸 | Carbon No. 碳数 | Transition temp. 转变温度 |
> |---|---|---|
> | Capric acid 癸酸 | 10 | **31 ℃** |
> | Lauric acid 月桂酸 | 12 | **44 ℃** |
> | Myristic acid 肉豆蔻酸 | 14 | **53 ℃** |
> | Palmitic acid 棕榈酸 | 16 | **63 ℃** |
> | Stearic acid 硬脂酸 | 18 | **69 ℃** |
> | Behenic acid 山嵛酸 | 22 | **79 ℃** |
>
> 2. **通用组成比**：着色剂 **1**：酚类（显色剂）**5**：脂肪酸（失感剂）**50**（原文单位 "group"）。
> 3. **必须微胶囊化的理由被写成了因果链**：反复显/消色会破坏三组分平衡 → 失衡后"can no longer discolor to the set color at the set discoloring temperature" → 因液态脂肪酸易迁出体系 → 故三组分**必须被包入微胶囊**（"necessary for putting the thermochromic ink into practical use"）。
>
> 另附该来源给出的**隐色染料（electron-donating color former）与色相对照**：3,6-二甲氧基荧烷（黄）、3-环己氨基-6-氯荧烷（橙）、3-二乙氨基-6-甲基-7-氯荧烷（朱红）、3-二乙氨基苯并荧烷（粉）、罗丹明 B 内酰胺（红）、结晶紫内酯（蓝）、3-二乙氨基-7-二苄氨基荧烷（绿）、3-二乙氨基-6-甲基-7-苯胺基荧烷（黑）；显色剂为**酚类化合物 / 酸性白土**。
>
> 🔴 **manual_review（2026-09-29）**：该来源为**个人发明人的同族美国专利**（母案授权 1993-03-30；延续案授权 1995-02-14，附 1995-06-13 更正证书，Claim 1 "material" 更正为 "insulation layer"，且 2010-03-30 之后的期限已被声明放弃）。**期限是否届满属法律结论 → `[待验证]`**；**不得据此判断该配方是否可自由实施**（FTO 须由法务评估）。
>
> 追加 `[待验证]`：上述脂肪酸熔点表在本库所用的**已微胶囊化的商品化温变油墨**中是否仍线性成立（本来源描述的是自行配制的三组分体系，非商品芯材）。

## Sources 来源

- [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/ThermoHydro_TechReview_EN_v3_2026-08-05.pptx.md`
- [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/Diaper_Microclimate_Visualization_Feasibility.pptx.md`

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · 量化边界：粒径 CV、寿命分档与国内外保质期差）

> 来源：[[温变湿变微胶囊技术参数对比表（X-Chromic 版 · 2026-06-18）]]（公开文献 + 厂商 Datasheet + 行业报告汇编，2026-06-18）。

| 维度 | 温变微胶囊（Thermochromic） |
|---|---|
| **机理** | **隐色染料（CVL / 荧光烷类）+ 双酚 A 类显色剂 + 脂肪醇/酯类相变溶剂**；温度 → 溶剂熔融/凝固 → 电子转移或晶体结构变化 |
| **触发** | **−10 ~ 150 °C 可选**；常用 **15 / 31 / 37 / 45 / 65 °C**；可定制 **±0.5 °C** |
| **粒径** | 丝印/移印 **1~10 μm**；凹印/柔版 **<5 μm（需窄分布）**；**批间 CV：国际 ≤15%，国内 ~30%** |
| **壁材** | **MF（三聚氰胺-甲醛，主流）**、**聚脲（高端）**、聚氨酯、聚丙烯酸酯、蜜胺树脂；**壁厚 100~200 nm** |
| **循环寿命** | 标准 **1,000~5,000 次**；高端（Matsui/CTI）**>10,000 次**；**聚脲壁材最高 50,000 次** |
| **精度** | **±0.5~1 °C**（医用/高端）、**±2~3 °C**（常规）、**±5~8 °C**（80 °C+ 超高温） |
| **响应** | **0.5~5 s**；金属/玻璃 **<1 s**；纸张/塑料 **2~5 s** |
| **颜色模式** | 有色↔无色（主流）；有色 A↔有色 B；多色阶段（液晶型）；**ΔE > 30 为清晰可见** |
| **包覆率** | 国内 **75~85%**；国际高端 **≥92%**；**包覆率低 → 有效成分泄漏 → 批次报废** |
| **储存** | **国内 1~3 月 vs CTI / Matsui 12~24 月** |
| **印刷** | 丝印✅、移印✅、**凹印⚠️（需专用分散液，<5 μm）**、柔印⚠️；**最优涂布厚度 5~10 μm** |

1. **寿命是分档的，不是一个数** —— **标准 1,000~5,000 次 / 高端 >10,000 次 / 聚脲壁材 50,000 次**。**⇒ "循环寿命"必须连同壁材体系一起报；只报次数等于没报。**
2. **粒径的判据是分布宽度（CV）而不是中值** —— 凹印/柔版要求 **<5 μm 且 >90% 落在目标区间、批间 CV ≤15%**；**国内现状多为 3~15 μm、CV ~30%**。**⇒ 评价微胶囊供应商时应索取粒径分布与批间 CV，而不是 D50。**
3. **壁材存在"强度 vs 薄度"的直接矛盾** —— 需**抵抗印刷剪切力**同时**尽可能薄（100~200 nm）以保证灵敏传热**；高端路线**聚脲/聚氨酯 = 无甲醛 + 耐疲劳 + 薄壁高强**。**⇒ 壁材选择同时决定了寿命、灵敏度与合规三项。**
4. **耐候性的根因在芯材** —— **隐色染料对 UV 与氧化敏感**，需 UV 吸收剂 + 抗氧化剂；**⇒ 耐候性不能只靠壁材解决。**
5. **⚠️ 国内外差距最硬的指标是保质期，不是价格** —— **1~3 月 vs 12~24 月**。**⇒ 这是可用性与库存损耗的差距，直接决定能否量产，而非"性价比"问题。**
6. **国产化的缺口在"基础微胶囊"而非"应用"** —— 源文直言国内厂商**"多数以配方和应用为主，基础微胶囊技术仍落后"**（千色变"基础微胶囊外购"）；**高端染料依赖进口（日本 NCB、山田化学）**。**⇒ 国产替代的对象应是微胶囊本体与染料，不是油墨配方。**
7. **⚠️ 两项卫材合规风险需单独评估** —— ① **MF 壁材的甲醛**；② **双酚 A 类显色剂**。**⇒ 温变在卫材上的合规审查对象不止壁材。**
8. **温变在纸尿裤上并非核心应用** —— 源文场景表中，纸尿裤/成人失禁裤一栏湿变为「**✅ 尿显指示（核心应用）**」，温变仅为"温度指示（体温联动）"；**核心应用是奶瓶 45 °C、冷链 ±1 °C、医疗 37 °C ±0.5 °C、智能纺织品 31 °C**。**⇒ 温变进入卫材需另行论证场景价值。**

> ✅ 验证（2026-09-29）：本节为**追加**，**未修正上方任何既有结论**。
> 🔴 **manual_review（2026-09-29）**：源文**成本区间（元/kg，国内 200~800 / 进口 800~1,500+）为公开资料汇编的估算**，附批次差异免责；**不得作为采购议价依据、不得对外引用**。**Matsui/CTI ">10,000 次"、聚脲"50,000 次"为源文/厂商口径，非本库实测**。**国内外保质期对比为源文判断，本页未独立核验**。

## Related Sources 关联来源

- [[BNC PCM-Free Thermoregulation v1（无微胶囊温控·细菌纳米纤维素）]]
- [[CN 111317617 A（可判断大小便的纸尿裤·马西臣）]]
- [[CN 116327488 B（便于识别吸湿状态的吸收性物品及其方法·露乐健康科技）]]
- [[Diaper Microclimate Visualization Feasibility (Dual-MVP)]]
- [[Elastic Tension Visualization Technology Assessment（拉力松紧可视化技术评估）]]
- [[Hygiene Chromic Ink Supplier Landscape（卫生护理变色油墨供应商调研 · 2026-06-12）]]
- [[NL 長效型夜光材料產品資料（Glow-in-the-Dark Material）]]
- [[Probiotic-Prebiotic-Postbiotic Diaper Project Review（益生菌-益生元-后生元尿布项目方案评审 · 录音纪要 2026-08）]]
- [[Strategic Roadmap - Commercializing Mechanochromic Materials（力致变色商业化战略路线图·X-Chromic 版）]]
- [[The Chromatic Shift（力致变色：Naphthopyran 与 HPC 双路线）]]
- [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]
- [[Thermochromic and Hydrochromic Materials Feasibility Review（温变湿变材料可行性分析·中文版）]]
- [[Thermochromic_Products_Comparison_by_Company]]
- [[US 20070270773 A1（Thermochromic Wetness Indicator）]]
- [[US20220125319A1 Moisture and Fever Sensing Apparatus (Farnaz Zand)]]
- [[US5197958A & US5389093A Wetness Indicating Diaper (Howell)]]
- [[Water-Activated Ink Wetness Indicator & Matsui Shikiso Technical Exchange（水变油墨尿显暨松井技术交流纪要 2026-08-14）]]
- [[感光变色材料产品资料（UV_CHT1608V2 · 台系变色供方）]]
- [[感温变色材料产品资料（TM_CHT1608V2 · 台系变色供方）]]
- [[河南嘉屹达新材料官网：热压敏染料产品页（JYDR-5）]]
- [[温变湿变微胶囊技术参数对比表（X-Chromic 版 · 2026-06-18）]]
- [[盛色科技官网关于我们（BLOCLO 温变与光变材料）]]


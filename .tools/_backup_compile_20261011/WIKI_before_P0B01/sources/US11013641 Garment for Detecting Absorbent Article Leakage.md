---
type: source
title: "US11013641 Garment for Detecting Absorbent Article Leakage"
source_type: patent
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/US_Patents_智能织物传感_拆解/US11013641_失禁传感_拆解.md.md
date_published: 2021
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "US 11,013,641 B2, assignee Kimberly-Clark Worldwide, Inc. (Neenah, WI) — NOT P&G — titled 'GARMENT FOR DETECTING ABSORBENT ARTICLE LEAKAGE AND METHODS OF DETECTING ABSORBENT ARTICLE LEAKAGE UTILIZING THE SAME'. Granted May 25, 2021; 20 Claims, 5 Drawing Sheets; PCT/US2017/026034 filed Apr. 5, 2017, published as WO2018/186842 on Oct. 11, 2018; US national phase 16/500,116; earlier publication US 2020/0375809 A1 (Dec. 3, 2020)."
  - "Claim 1 is an OUTER GARMENT (not the absorbent article itself) with a substrate plus a wetness detection system having a FIRST and a SECOND wetness detection mechanism at two DIFFERENT detection zones, each zone corresponding to a monitored location on the absorbent article."
  - "Claim 10 adds a controller in electrical communication with both mechanisms, both configured to detect wetness ELECTRONICALLY, with the monitored locations selected from front end edge, rear end edge, first side edge, second side edge."
  - "Conductive element: silver-plated conductive thread at 60 ohms/meter, exemplified as Shieldex 110/34 dtex 2 ply HC Premium Line (polyamide 6.6 trilobal filament, 99% silver plating); controller exemplified as a LilyPad Arduino USB board with rechargeable battery."
  - "Exemplary Test 1: 60% polyester / 40% cotton onesie; 3.3 VDC applied; ADC full scale 1024 counts, ~0.003223 V per count; dry ~1000 counts (~3.2 V), dropping after insult at ~14 s and stabilising at ~200 counts (~0.64 V) when fully wetted."
  - "Exemplary Test 2: Carter's 100% polyester footed pyjamas; dry ~1000 counts, drop to ~200 counts after insult at ~26 s; further drop at ~56 s suspected lead short. Insult volume in each test: 2 mL saline released onto the wetness mechanism."
summary_cn: "金佰利（非宝洁）US 11,013,641 B2：在吸收制品外面穿一件带多点电子湿感（银涂层导电纱）的检测服装，按检测区映射到纸尿裤前后端与左右侧边，实现渗漏「何时发生、何处发生」的定位与计时。"
tags: ["source/patent", "Kimberly-Clark", "leakage detection", "wetness sensing", "conductive thread", "electronic sensing", "test method"]
tags_zh: ["专利", "金佰利", "渗漏检测", "湿感", "导电纱", "电子传感", "测试方法"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[US11013641B2 Garment for Detecting Absorbent Article Leakage (Kimberly-Clark)]]", "[[US8273939B2 Disposable Absorbent Articles Having a Windowed Removable Sensor (P&G)]]", "[[Smart Sensing Diaper Technology Research Report（智能感知纸尿裤技术研究报告 · 2026-04）]]", "[[US 20250064649A1 Intelligent Monitoring Diaper with Enhanced Features (Wu Guohui)]]", "[[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]", "[[US10905605 Pull-On Wearable Article with Informational Image]]"]
---

# US11013641 — Garment for Detecting Absorbent Article Leakage（用于检测吸收制品渗漏的服装及其检测方法）

> Source: US patent 11,013,641 B2, **Kimberly-Clark Worldwide, Inc.（金佰利）, Neenah, WI (US)** — **assignee is K-C, NOT P&G**（源文明确提示）. Inventors: Shawn Jeffery Sullivan; Davis Dang H. Nhan; Rebecca E. Strong; Andrew Long. PCT/US2017/026034 filed **Apr. 5, 2017**, published **WO2018/186842** on **Oct. 11, 2018**; US national phase entered Oct. 2, 2019 (Appl. No. 16/500,116); earlier publication US 2020/0375809 A1 (Dec. 3, 2020); **granted May 25, 2021**. PTA under 35 U.S.C. 154(b) = **0 days**. Int. Cl. A61F 13/42, A61F 13/74, A61F 13/84. **20 Claims, 5 Drawing Sheets.**
>
> 拆解说明：原始 txt 为专利公告文本 OCR，双栏交错；引用均按原文 verbatim。**主题为「检测吸收制品渗漏的外穿服装 + 电子湿感系统」**。

## Technical Field 技术领域

**Electronic wetness/leakage detection on an over-garment（外穿服装上的电子湿感/渗漏检测）** — a substrate (garment) carrying a distributed wetness detection system, used to localise and time leakage from an absorbent article worn underneath.

- Int. Cl. **A61F 13/42**（吸收制品的湿气/湿度指示装置）, **A61F 13/74**（吸收制品的固定/附着件）, **A61F 13/84**；CPC 另含 A61F 2013/424, A61F 2013/8482.
- Target absorbent articles named in the source: diapers, training pants, incontinence products, feminine care products, swim pants.
- **Key boundary: the claimed article is the GARMENT, not the absorbent article**（权利要求对象是外穿服装，不是吸收制品本身）.

## Problem Solved 解决的问题

| Problem 问题 | Source wording 原文表述 | Note 备注 |
|---|---|---|
| Leakage time/location is hard to determine 渗漏的时间与位置难以确定 | "It is typically difficult to determine where, when, and how an absorbent article has leaked urine or other bodily fluids, especially when the absorbent article is being worn by a newborn or other very young wearers." | 新生儿等低龄穿着者尤甚 |
| Existing wetness indicators do not indicate leakage 现有湿显不指示渗漏本身 | "However, none of these indicators are designed to indicate leakage from the absorbent article itself and that can provide information as to the location and timing of the leakage." | 与尿湿指示器的关键区别 |
| Bed-mat sensing is delayed 床垫传感存在延迟 | "Additionally, sensors in bed mats can provide significant delay in detecting leakage, or may altogether not detect leakage of the absorbent article, due to additional layers that the body exudates must pass through between the absorbent article and the bed mat." | 多层阻隔导致延迟甚至漏检 |
| Stated need 需求 | "a need currently exists for a garment that includes a wetness detection system that can be used to determine when and where an absorbent article leaks." | — |
| Stated capability 能力 | "The garment can be configured to detect leakage of the absorbent article, a location of the leakage corresponding to the absorbent article, and the timing of the leakage, **without having to visually inspect the absorbent article itself or modifying the construction of the absorbent article**." | 不改吸收制品结构、无需目视 |

## Core Mechanism 核心机理

The mechanism is **conductive resistive sensing（导电/电阻式传感）**, not chromic:

1. **Conductive element as the transducer** — conductive materials listed: **conductive threads, conductive tape, conductive rubber, conductive wires**. Preferred: **silver-plated conductive thread at 60 ohms/meter**, exemplified by **Shieldex® 110/34 dtex 2 ply HC Premium Line**（polyamide 6.6 trilobal filament, **99% silver plating**）.
2. **Read-out** — a controller applies **3.3 VDC** across the conductive thread and monitors the voltage at its ends. **Dry state ≈ full-scale 3.3 V; wet state voltage drops significantly**（干态约满幅，湿态显著下降）— the exudate bridges/loads the conductive path and the measured potential collapses.
3. **Spatial encoding via zone-to-article mapping（检测区↔制品位置映射）** — each detection zone on the garment *corresponds to* a specific location on the absorbent article of interest (front end edge, rear end edge, first side edge, second side edge). Multiple zones ⇒ leakage **localisation**, not merely detection.
4. **Mechanical interface stack（机械防护结构）** — a **porous material 15** overlays the wetness mechanism to prevent skin contact while still allowing exudate to reach it, plus a **waterproof/water-resistant backing 17** that traps the leaked liquid (FIG.1A).
5. **Alternative sensing technologies acknowledged** in the specification: **capacitance**（US 8,866,624）, **inductance**（US 8,207,394）, **infra-red reflectance（红外反射）**.
6. **Controller** exemplified as a **LilyPad Arduino USB board**（含充电电池电源）; controller may be in electrical communication with a **computer** that records activity over time.

## Key Embodiments 关键实施例

| Parameter 参数 | Value 数值 | Note 备注 |
|---|---|---|
| Conductive thread 导电纱 | **60 ohms/meter**; Shieldex® 110/34 dtex 2 ply HC Premium Line, polyamide 6.6 trilobal, **99% Ag plating** | 优选方案 |
| Drive voltage 驱动电压 | **3.3 VDC** applied by the controller | — |
| ADC resolution 模数分辨率 | full scale **1024 counts**; **≈0.003223 V per count** (3.3 V / 1024) | Test 1 |
| Test 1 substrate 基材 | **60% polyester / 40% cotton onesie（连体衣）**; dry **~1000 counts (~3.2 V)**; insult at **~14 s**; fully wetted stabilises at **~200 counts (~0.64 V)** | FIG.4 |
| Test 2 substrate 基材 | Carter's **100% polyester footed pyjamas（连脚睡衣）**; dry **~1000 counts**; insult at **~26 s** → **~200 counts**; further drop at **~56 s** suspected **lead short（导线短路）** | FIG.5 |
| Insult volume 冲注量 | **2 mL saline**（生理盐水）released onto the wetness mechanism per test | 模拟渗漏 |
| Fixing method 固定方式 | conductive thread fixed to the garment substrate with **tape（胶带）** | 原型搭建 |
| Zone mapping example 检测区映射示例 | 1st zone ↔ first side edge 114; 2nd zone ↔ second side edge 116; 3rd zone ↔ front end edge 110; 4th zone ↔ rear end edge 112 | 四区映射 |
| Sub-zone refinement 细分 | zones may be subdivided within the same leg opening — inner/outer side, upper/lower, front/back | 特异性随数量与尺寸提升 |
| Test subject 测试对象 | mannequin（假人，静态/动态，可模拟爬行/行走/坐立转换）or human | — |
| Use cases 用途 | leakage design verification（何时/何地/何种体位渗漏、渗漏前可容纳的冲注量与速率）; caregiver change reminder（照护者及时更换提醒） | 研发 + 照护双场景 |

Figures: FIG.1 front plan view of garment 10 (onesie form) showing substrate 14, wetness detection system 12, mechanisms 16/20/28/32 and detection zones 18/22/30/34; FIG.1A partial cross-section showing porous material 15, waterproof backing 17, substrate inner surface 42; FIG.2 perspective of an exemplary absorbent article (diaper 100) with outer cover 102, bodyside liner 104, fastening system 106, leg flaps 108, front end edge 110 / rear end edge 112 / first side edge 114 / second side edge 116; FIG.3 garment applied over test subject 120, in electrical communication with computer 60; FIG.4/5 ADC count vs. time curves for Test 1 / Test 2.

## Claims Coverage 权利要求覆盖范围

Three independent claims — two product, one method.

| Claim 权利要求 | Scope 范围 |
|---|---|
| **Claim 1**（product, broadest） | A **garment** configured for detecting leakage from an absorbent article **underlying** the garment, comprising: **a substrate**; and **a wetness detection system** comprising a **first wetness detection mechanism at a first detection zone** (zone ↔ first monitored location on the absorbent article) and a **second wetness detection mechanism at a second detection zone** (zone ↔ second monitored location), **the second detection zone being different than the first**. ⇒ All four limitations (garment / substrate / ≥2 mechanisms / zone-to-article mapping) required. |
| **Claim 10**（product, narrower） | Claim 1 basis + both monitored locations **selected from {front end edge, rear end edge, first side edge, second side edge}** + **a controller in electrical communication** with both mechanisms + **both mechanisms configured to detect wetness ELECTRONICALLY**. |
| **Claim 14**（method） | Providing an absorbent article on a test subject; providing a garment with the wetness detection system (first mechanism on the substrate + controller recording its activity); **applying the garment so that it overlays the absorbent article**; and **monitoring the system to detect leakage**. |
| Dependent 从属 | Claim 2 controller added; Claim 3 both electronic; Claim 4 both include **conductive thread**; Claim 5 **power source**; Claim 6 controller ↔ computer; Claim 7/8 locations from the four-edge set; Claim 9 **third** wetness mechanism; Claim 11 third mechanism electronic; Claim 12 power source; Claim 13 computer monitors activity over time; Claim 15/16 computer has output interface and records **location and timing**; Claim 17–20 second mechanism / conductive thread / zone mapping in method form. |

Boundary note from the source: the claims are directed to the **garment**; **integrating the sensing into the absorbent article itself is outside the claim scope as described**（传感集成进吸收制品本体不在其权利要求范围内 — 源文推演表述）.

## Hygiene Implication 卫材关联

Relevance to the owner's **chromic-ink（变色油墨）programme** and REL core work:

1. **Direct route contrast: electronic vs chromic.** This patent is the *electronic* branch — silver-plated conductive thread + controller + ADC read-out. The KB's chromic branch（thermochromic / hydrochromic）answers the same "is it wet / did it leak" question **without power, electronics or an app**. Compare directly with [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]]; see also [[Smart Sensing Diaper Technology Research Report（智能感知纸尿裤技术研究报告 · 2026-04）]] for the broader sensing landscape and [[US 20250064649A1 Intelligent Monitoring Diaper with Enhanced Features (Wu Guohui)]] for a competing integrated-monitoring approach.
2. **Highest-value transferable asset: the leakage TEST METHOD（渗漏测试方法学）, not the product.** The "over-garment + multi-zone electronic wetness" rig quantifies **when / where / in which posture** leakage occurs, and how much insult volume/rate is held before leakage — replacing visual inspection and bed-mat sensing. This is directly usable as an internal bench method for K-C diaper/incontinence leakage characterisation, **independent of any chromic-ink decision**.
3. **Zone-mapping template is reusable.** Mapping detection zones to {front end edge, rear end edge, first side edge, second side edge} and subdividing (leg-opening inner/outer, upper/lower, front/back) gives a ready-made **leakage test matrix and failure-mode map** — useful even if the sensing element is swapped from conductive thread to a chromic strip.
4. **Interface stack lesson for chromic layers.** The **porous cover (prevents skin contact, passes liquid) + waterproof backing (traps leaked liquid)** pairing is a transferable design pattern for any indicator layer that must be wetted by exudate while staying off the skin — relevant to placing chromic ink on a backsheet/outer-cover-adjacent position.
5. **Reversibility / signal quality contrast.** The electronic route gives continuous, time-resolved, recoverable data but showed a suspected **lead short at ~56 s** in Test 2 — a robustness caveat. A chromic route gives a one-way (or slowly reversible) visual endpoint with no wiring risk; the two are complementary rather than substitutable.
6. **Chromic-ink placement is NOT taught here.** This patent contains **no thermochromic or hydrochromic chemistry** — do not cite it for colour-former/developer/solvent systems or transition temperatures.
7. **Freedom-to-operate（自由实施）: NOT assessed.** This patent is **K-C's own**（受让人为金佰利）. The source records PCT filing 2017-04-05 and PTA = 0 days but **does not establish expiry date, maintenance status, or the scope of any CN/EP national-phase counterparts** — all flagged `[待验证]` / manual review. No FTO or design-around position is taken here; route such questions to IP counsel.

## Related Sources 关联来源

- [[US11013641B2 Garment for Detecting Absorbent Article Leakage (Kimberly-Clark)]] — 同一专利的既有另一摘要页
- [[US8273939B2 Disposable Absorbent Articles Having a Windowed Removable Sensor (P&G)]] — 宝洁传感路线（windowed removable sensor）对照
- [[Smart Sensing Diaper Technology Research Report（智能感知纸尿裤技术研究报告 · 2026-04）]] — 智能感知纸尿裤技术全景
- [[US 20250064649A1 Intelligent Monitoring Diaper with Enhanced Features (Wu Guohui)]] — 竞品集成式监测方案
- [[Thermochromic & Hydrochromic Materials for Diapers (Feasibility Review v3)]] — 变色路线（本库 chromic-ink 主线）可行性评审
- [[US10905605 Pull-On Wearable Article with Informational Image]] — 非传感的图形引导路线对照

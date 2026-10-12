---
type: source
title: "Seymour Polymer Chemistry Ch05 Rheology and Physical Tests"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Seymour Polymer Chemistry/chapters/Seymour Polymer Chemistry_ch05.md.md"
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Polymers are viscoelastic materials — they can act as liquids (the 'visco' portion) and as solids (the 'elastic' portion); which behaviour dominates depends on temperature, the polymer and its prior treatment, polymer structure, and the measurement conditions."
  - "Hooke's law σ = Eε is independent of strain rate, whereas Newton's law σ = η dε/dt is independent of strain; the Hookean spring represents bond flexing and the Newtonian dashpot chain and local segmental movement."
  - "Below Tg the spring portion dominates; above Tg, where segmental mobility occurs, the dashpot portion dominates."
  - "Poisson's ratio is 0.5 when there is no volume change (elastomer stretched) and decreases toward 0.3 for rigid PVC and ebonite; creep is the irreversible elongation caused by application of force over a specified time."
  - "Tensile strength is measured by pulling a dumbbell specimen per ASTM D-638; flexural strength per ASTM D-790, with the modulus at 5% strain used when the specimen does not break."
  - "Elastic polymers show elongations in excess of 1,000% while even 'moldable' metals do not exceed 100%; polymer moduli range from about 7 MPa to 4 GPa versus 50–400 MPa for metals."
summary_cn: "第5章是力学与流变学核心：以胡克弹簧与牛顿粘壶两个元件构建粘弹性数学框架（Maxwell 串联-应力松弛 / Kelvin-Voigt 并联-蠕变），并展开五类应力-应变行为、蠕变、应力松弛、疲劳极限与拉伸/弯曲等 ASTM 物理测试。"
tags: ["source/book", "rheology", "viscoelasticity", "stress-strain", "creep", "fatigue", "physical-testing"]
tags_zh: ["流变学", "粘弹性", "应力应变", "蠕变", "应力松弛", "疲劳极限", "泊松比", "物理测试"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Seymour Polymer Chemistry Ch02 Polymer Structure and Morphology]]", "[[Seymour Polymer Chemistry Ch04 Testing and Spectrometric Characterization]]", "[[Seymour Polymer Chemistry Ch06 Step-Reaction Polymerization]]", "[[Absorbent Product Testing]]", "[[Characterisation, testing and modelling of nonwoven fabrics]]"]
---

# Seymour Polymer Chemistry Ch05 Rheology and Physical Tests

> Source: Seymour/Carraher, *Polymer Chemistry*, Ch.5 — Rheology and Physical Tests.
> 定位说明 / Citation convention: 原文为 .txt 抽取件，**无正式印张页码**，本报告以文件行号（line no.）定位。原抽取件对 stress relaxation 标注"[未找到完整单独定义原句]"，本页对应处保留 [待验证]。

## Executive Summary 内容概要

Chapter 5 is the mechanics-and-rheology core. Starting from two elements — the **Hookean spring** and the **Newtonian dashpot** — Seymour builds the mathematical framework of **viscoelasticity**（Maxwell series → stress relaxation；Kelvin-Voigt parallel → creep），then expands into the five classes of stress–strain behaviour, creep, stress relaxation, fatigue, and the ASTM physical test matrix. 本章把聚合物的"固体-液体二元性"从定性描述提升为可由元件模型精确描述的数学对象。

## Viscoelasticity 粘弹性本质

> *"Polymers are viscoelastic materials, meaning that they can act as liquids, the 'visco' portion, and as solids, the 'elastic' portion."* (line 3-4)

> *"Whether a material behaves as a viscous or an elastic material depends on temperature, the particular polymer and its prior treatment, polymer structure, and the particular measurement or conditions applied to the material."* (line 5-12)

**词源 / Etymology**：*"The branch of science related to the study of deformation and flow of materials was given the name rheology by Bingham, whom some have called the father of modern rheology. The prefix rheo is derived from the Greek term rheos, meaning current or flow."* (line 15-18)

## Rheological Elements and Constitutive Laws 流变元件与本构定律

| 元件 / 定律 Element / Law | 公式 Equation | 物理含义 Physical meaning |
|---|---|---|
| Hooke's law 胡克定律 | **σ = Eε** (Eq. 5.1) | *"the applied stress (σ) is proportional to the resultant strain (ε) but is independent of the rate of this strain (dε/dt)"* (line 21-25) |
| Newton's law 牛顿定律 | **σ = η dε/dt** (Eq. 5.3) | *"the applied stress σ is proportional to the rate of strain dε/dt, but is independent of the strain ε"* (line 46-49) |
| Arrhenius 粘度 | **η = A e^(E/RT)** (Eq. 5.4) | *"E is the activation energy for viscous flow"* (line 60-62) |
| Hookean spring 弹簧 | — | *"the Hookean spring represents bond flexing while the Newtonian dash pot represents chain and local segmental movement."* (line 64-69) |
| Newtonian dashpot 粘壶 | — | 链段与整体链运动（时间依赖） |

**温度决定元件主导权 / Temperature switches the dominant element**：*"Below their Tg polymers can be modeled as having a behavior where the spring portion is more important. Above their Tg where segmental mobility occurs, the dashpot portion is more important."* (line 72-74)

**Maxwell 模型**：*"Maxwell joined the two models in series to explain the mechanical properties"* (line 80-82) — 串联模型刻画**应力松弛**（恒应变下应力衰减）；**Kelvin-Voigt** 并联模型刻画**蠕变**。

**Poisson's ratio 泊松比**：*"ν = ε_l/ε_w... When there is no volume change, as when an elastomer is stretched, Poisson's ratio is 0.5. This value decreases as the Tg of the substance increases and approaches 0.3 for rigid poly(vinyl chloride) (PVC) and ebonite."* (line 32-36)

## Stress-Strain Behavior 应力-应变行为五分类

> *"class (c) polymers, such as plasticized PVC, have a low modulus of elasticity, high elongation, a Poisson ratio of about 0.5–0.6, and a well-defined yield point."* (line 312-315)

> *"Rigid PVC is representative of hard and strong class (d) polymers. These polymers have a high modulus of elasticity and high yield strength."* (line 316-318)

> *"hard and tough class (e) polymers, such as ABS copolymers, shows moderate elongation prior to the yield point followed by nonrecoverable elongation."* (line 319-321)

- **弹性区 / Elastic range**：*"The reversible recoverable elongation prior to the yield point, called the elastic range, is primarily the result of bending and stretching covalent bonds in the polymer backbone."* (line 322-323)
- **屈服后 / After yield**：*"Irreversible slippage of polymer chains is the predominant mechanism after the yield point."* (line 324)

## Physical Tests 物理测试

- **拉伸强度 / Tensile strength**：*"Tensile strength (Pascals) = force required to break sample (N) / cross-sectional area (m²)"* (Eq. 5.21)；*"usually measured by pulling a dumbbell specimen... in accordance with ASTM D-638–72."* (line 600-618)
- **弹性模量 / Elastic modulus**：*"the ratio of the applied stress to the strain it produces within the region where the relationship between stress and strain is linear. The ultimate tensile strength is equal to the force required to cause failure divided by the minimum cross-sectional area of the test sample."* (line 616-619)
- **蠕变 / Creep**：*"The wholesale movement of polymer chains is called creep or plastic strain. Here the strain is nonreversible with an end result of permanent deformation."* (line 635-637)；*"creep is the irreversible elongation caused by the application of force (such as a weight) over a specified time. If the change in length occurs at room temperature, it is called cold creep."* (line 638-641)
- **弯曲强度 / Flexural strength**：*"a measure of the bending strength or stiffness of a bar test specimen used as a simple beam in accordance with ASTM D-790."*；*"since many materials do not break even after being greatly deflected, the actual flexural strength cannot be calculated. Instead, by agreement, the modulus at 5% strain is used..."* (line 658-666)
- **疲劳 / Fatigue**：*"There is some limiting stress level below which fatigue does not occur (over some reasonably extended time). This value is called the fatigue or endurance limit. The fatigue strength is defined as the stress at which failure will occur for some specified number of cycles. Fatigue life is the number of cycles that are needed to cause failure."* (line 352-355)
- **应力松弛 / Stress relaxation**：在 Maxwell/Kelvin-Voigt 框架下描述为"恒应变下应力随时间衰减"；**原抽取件未给出完整单独定义原句** [待验证]。

**Polymer vs metal 聚合物-金属量级对比（line 356-363）**：

| 指标 Property | 聚合物 Polymers | 金属 Metals |
|---|---|---|
| 模量 Modulus | 7 MPa（高弹）至 4 GPa（刚性） | 50–400 MPa（更高但不那么分散） |
| 拉伸强度 Tensile strength | 约 100 MPa | 某些合金达 4000 MPa |
| 断裂伸长 Elongation | 弹性体 > 1,000% | 即使"可成型"金属也不超过 100% |

**等规度决定 Tg（PMMA 案例，line 374-380）**：*"Below the Tg the material behaves as a stiff, brittle solid... The Tg varies greatly for PMMA depending upon the tacticity with isotactic PMMA having a Tg of about 45°C, and for syndiotactic the Tg is about 130°C."*

## Methodology Critique 方法论批判

- **五分类的边界是操作定义而非本体定义**：*"class (a) polymers may resemble class (d) polymers if the stress is applied rapidly, and vice versa"* (line 325-326) — 分类依赖于温度、应变速率与材料历史。
- **二元件模型的简化**：真实聚合物需要 n 个元件的 generalized Maxwell/Kelvin 谱；二元件模型只在特定时间尺度内有效。
- **疲劳极限的存在性存疑**：聚合物是否真有"endurance limit"仍有争议——多数聚合物在足够长时间内总会疲劳失效。

## Hygiene Implication 卫材关联

- **PP 熔体流变与纺丝**：PP 的加工（熔融纺丝、挤出、热轧）完全由熔体粘度控制，而粘度服从 Arrhenius 关系 η = A e^(E/RT)，并在缠结临界分子量以上服从 Ch.3 的 η ∝ M^3.4。温度升高与分子量微调是纺丝窗口的两个杠杆。
- **AUL 本质是蠕变测试**：SAP 凝胶在外部压力（尿液重力、人体压力）下发生蠕变——凝胶变形并释放已吸收液体，表现为 gel blocking / AUL 下降。原文对蠕变的定义是"恒力作用下的不可逆伸长"。因此**高 AUL = 低蠕变倾向 = 更优凝胶网络结构**，这是用第5章语言重新表述 SAP 核心指标。
- **无纺布柔软度与 Tg**：i-PP 的 Tg ≈ 100°C，室温下处于 Tg 以下，理论上应表现为刚性——原文对 PMMA 的说明是"Below the Tg the material behaves as a stiff, brittle solid"。卫材用 PP 无纺布之柔软来自低结晶度、细纤度与后整理，而非 Tg 下移；报告 RIA 卡片"降低等规度"属**推演方向** [待验证]。
- **弹性腰围的疲劳设计**：腰围弹性体（spandex 类）在穿着中经历数千次循环拉伸，工作应力必须低于 fatigue strength（对应指定循环次数），否则会在穿着数日后断裂。
- **无纺布强度测试口径**：拉伸强度按 ASTM D-638 哑铃试样、弯曲强度按 ASTM D-790、不断裂试样取 5% 应变模量——这些是无纺布与芯体力学数据可比性的共同基准。

## Related Sources 关联来源

- [[Seymour Polymer Chemistry Ch02 Polymer Structure and Morphology]]
- [[Seymour Polymer Chemistry Ch04 Testing and Spectrometric Characterization]]
- [[Seymour Polymer Chemistry Ch06 Step-Reaction Polymerization]]
- [[Absorbent Product Testing]]
- [[Characterisation, testing and modelling of nonwoven fabrics]]

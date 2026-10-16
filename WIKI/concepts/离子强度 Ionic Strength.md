---
type: concept
title: "离子强度 Ionic Strength"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-09-30
tags: [ionic-strength, SAP, hydrogel, swelling, saline, crosslink]
---

# 离子强度 Ionic Strength

> 📌 **Page completed 2026-09-30** from 6 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

定义待补（引用来源未给出明确定义）。

The vault never states a formula or units for ionic strength; it treats it operationally as **one of the three parameters** that precisely tune a hydrogel SAP's absorbency / water retention / salt tolerance / oil resistance — **cross-link density + ionic strength + temperature**（源：[[Hydrogel-based Superabsorbent Polymers]]）。Its direction of effect is stated directly: **electrolytes such as NaCl and CaCl₂ affect swelling, and high ionic strength *lowers* water absorbency**（源：[[Hydrogel-based Superabsorbent Polymers]]）。

中文：本库未给离子强度的公式或单位，只把它当作调控水凝胶 SAP 吸水/保水/耐盐/耐油性能的三大参量之一（交联密度 + 离子强度 + 温度），并明确「高离子强度降低吸水性」。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| Effect of high ionic strength on water absorbency | 降低吸水性（lowers absorbency；定性，未给数值） | [[Hydrogel-based Superabsorbent Polymers]] |
| Electrolytes named as ionic-strength sources | NaCl、CaCl₂ | [[Hydrogel-based Superabsorbent Polymers]] |
| SAP performance parameters coupled to ionic strength | 3（cross-link density 交联密度 / ionic strength 离子强度 / temperature 温度） | [[Hydrogel-based Superabsorbent Polymers]] |
| Divalent cations abundant in real urine / menstrual fluid | Ca²⁺、Mg²⁺ | [[Ancient Organic Dyes and Pigments Chemistry]] |
| Ionic strength / conductivity as a bowel-movement trigger | rejected（与尿液重叠 + 需电子件） | [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]] |

## Method / Mechanism 方法 / 机理

**Charge → hydrophilicity → swelling.** Charged groups raise hydrophilicity (hence higher water absorption), and their **electrostatic repulsion raises solubility and the swelling ratio**（源：[[Hydrogels in Regenerative Medicine]]）。

**Ionic cross-linking.** The polymer-chemistry source states verbatim: *"divalent ions are known to act as cross-links between carboxyl groups in natural resins"*, and notes ionomers as the polymer class that carries ionic bonds — ionic bonds are otherwise uncommon in polymers（源：[[Ebewole Polymer Science Ch03 Chemical Bonding and Polymer Structure]]）。In the microfluidics source the same route appears as a fabrication option, where **Ca²⁺ + alginate gives "temporary hydrogel networks"**（源：[[Smart Polymers Ch14 Hydrogels in Microfluidics]]）。

**Ionic surface cross-linking is a design lever *and* a failure mode.** Modern SAP practice uses a cation (Al³⁺) to ionically surface-crosslink polyacrylic-acid carboxyls, which raises gel strength, SFC/permeability and reduces gel blocking; the Al-crosslinked shell is only **partly reversible and is sensitive to pH and ionic strength**（源：[[Ancient Organic Dyes and Pigments Chemistry]]）。

**Competitive complexation re-reads the "salt effect".** In real urine/menstrual fluid (rich in Ca²⁺, Mg²⁺), divalent cations participate in the coordination shell of the Al-crosslinked SAP surface and thereby change the cross-link density *in use*. This reframes the classic observation that **SAP absorbency drops in saline/urine** as **competitive complexation**, not only Donnan / ionic-strength screening — and predicts that **Ca²⁺ concentration should be a control variable for CRC / AUL / SFC test fluids**（源：[[Ancient Organic Dyes and Pigments Chemistry]]）。

中文：机理链为「带电基团→亲水性与静电排斥→溶胀」；二价离子可作羧基间的离子交联点（ionomer / 海藻酸钙属此列）；Al³⁺ 离子表面交联 SAP 是可提升凝胶强度与 SFC 的**杠杆**，但外壳对 pH 与离子强度敏感 → 也是**失效模式**；在真实尿液/经血中 Ca²⁺/Mg²⁺ 的竞争络合把「盐水吸液量下降」重解释为竞争络合，而非单纯 Donnan/离子强度屏蔽。

## Hygiene Relevance 卫材关联

- **SAP absorbency in urine.** The in-use absorbency drop this vault watches (CRC / AUL / SFC) is tied to ionic strength and, more specifically, to divalent cations in the test fluid — so Ca²⁺ concentration is proposed as a controlled test variable（源：[[Ancient Organic Dyes and Pigments Chemistry]]）。See [[SAP（高吸水树脂）]]、[[CRC 离心保持能力]]、[[AUL 加压吸水率]]。
- **Surface cross-linking as the direct lever.** Ionic (Al) surface cross-linking is exactly the route used to raise gel strength and reduce gel blocking — and its ionic-strength sensitivity is the same lever, turned into a risk when the load fluid is saline（源：[[Ancient Organic Dyes and Pigments Chemistry]]）。
- **Negative result — a rejected trigger.** Ionic strength / conductivity was rejected as a bowel-movement indicator trigger because it **overlaps with urine** and would require electronics（源：[[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]）。

## Open Questions 待补

- No formula, units or numeric ionic-strength values appear in the citing sources — the "high ionic strength lowers absorbency" statement is qualitative `[待补]`。
- No quantitative CRC/AUL/SFC-vs-ionic-strength curve is evidenced; the Ca²⁺-as-control-variable point is an inference the source itself labels as 外推 `[待补]`。
- The bulk high ionic strength route: no vault evidence yet of test-fluid Ca²⁺ levels specified in KC internal test standards `[待补]`。

## Related Sources 关联来源

- [[Hydrogel-based Superabsorbent Polymers]]
- [[Ancient Organic Dyes and Pigments Chemistry]]
- [[Hydrogels in Regenerative Medicine]]
- [[Ebewole Polymer Science Ch03 Chemical Bonding and Polymer Structure]]
- [[Smart Polymers Ch14 Hydrogels in Microfluidics]]
- [[BM Indicator Design — Viscosity & Cost（便指示·流变与成本）]]

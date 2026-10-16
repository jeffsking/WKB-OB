---
type: concept
title: "等电点 Isoelectric Point"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-30
tags: [isoelectric-point, IEP, polyampholyte, hydrogel, antipolyelectrolyte, protein, SAP, 等电点]
---

# 等电点 Isoelectric Point

> 📌 **Page completed 2026-09-30** from 3 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.
> 中文：本页定义取自**两性聚电解质凝胶**口径（正负电荷含量相等处）；另登记蛋白质 pI 的一个定量值。库内「等电点」无独立形式化定义条目，故以来源页用法为准。

## Definition 定义

**等电点（IEP）**：在两性（polyampholyte）聚电解质凝胶中，**正负电荷含量相等**处出现**溶胀比极小值**，此状态称等电点 IEP（源：[[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]，L476–479）。带电网络的**等电态（isoelectric regime）**由**非补偿电荷间距 σ₁** 判定：当 σ₁ > σ₃ 时**静电吸引主导**、抗衡离子极少 → 即使在极性介质中也塌缩（源：[[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]，L388–405）。

（蛋白质口径）库内另给出一个定量值：自由抗体的等电点 **pI ≈ 5.95**（源：[[Smart Polymers Ch01 Phase Transitions and Light Scattering]]，L2352–2353）。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| 等电点 IEP（凝胶口径） | 正负电荷含量相等处出现溶胀比**极小值** | [[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]（L476–479） |
| 等电态判据 Isoelectric regime | σ₁ > σ₃；静电吸引主导；抗衡离子极少 → 极性介质中也塌缩 | [[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]（L388–405） |
| 反聚电解质行为 antipolyelectrolyte | IEP 处**加低分子盐反而提高溶胀**（m/m_d 随 [NaCl] 上升） | [[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]（L484–485） |
| 三个溶胀区间 | 由非补偿电荷间距 σ₁ 决定：polyelectrolyte / intermediate / isoelectric | [[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]（L388–405） |
| 自由抗体 pI | **pI ≈ 5.95**（L2352–2353） | [[Smart Polymers Ch01 Phase Transitions and Light Scattering]] |
| Ab–PMAA 偶联物沉淀 | pH < 4.8（PMAA coil→compact 转变，**not** the antibody pI） | [[Smart Polymers Ch01 Phase Transitions and Light Scattering]]（L2357–2359） |

## Method / Mechanism 方法 / 机理

- **自由能分解.** 带电网络的总自由能 F = F_el + F_int + F_tr-en + F_elect（Eq 3.3，L322）；由非补偿电荷间距 σ₁ 导出三个溶胀区间（polyelectrolyte / intermediate / **isoelectric**）（源：[[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]）。
- **反直觉的盐响应.** 等电点的常规直觉是「无净电荷 → 加盐无影响」；但源明确记录：**"antipolyelectrolyte behavior was observed at the isoelectric point (IEP). The addition of low-molecular-weight salt resulted in the gel swelling."**（L484–485）——即 IEP 处**加盐反促溶胀**（源：[[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]）。
- **与离子强度的关系.** 二价抗衡离子在远低于单价的浓度下即可引发塌缩，并在高盐（~0.3 M）下出现三价阳离子的再入回溶胀（源：[[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]，L441–443）。

## Hygiene Relevance 卫材关联

- **高盐体液下的反向配方思路.** 常规阴离子 SAP 在高电解质体液（尿、汗）下失容；而**两性 PA 型凝胶在 IEP 处加盐反而溶胀**（源：[[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]，L484–500）——为高离子强度场景提供一条反向配方思路。
- **尿液离子 → 体积相变阈值.** 尿中 Ca²⁺/Mg²⁺ 属二价，其塌缩浓度远低于单价；自由溶胀容量与凝胶床刚度须按二价离子负载标定（源：[[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]，L441–443）。参见 [[SAP（高吸水树脂）]]、[[离子强度 Ionic Strength]]。
- **表面活性剂章节的登记.** [[The Role of Surfactants]] 将「等电点 Isoelectric Point」列为关联概念，但**未给出定义**（源：[[The Role of Surfactants]]）。

## Open Questions 待补

- 「等电点」的**通用（非凝胶/非蛋白）定义与量纲**在引用来源中均未给出。
- 库内**无 SAP 表面/凝胶体系的实测 IEP 数值**（pH 值）：来源未给。
- 等电点与卫材配方（如离子型表面活性剂配伍、SAP 表面交联）的**定量关联**：来源未给。参见 [[表面交联 Surface Cross-linking]]。

## Related Sources 关联来源

- [[Smart Polymers Ch03 Conformational Transitions in Ionic Gels]]
- [[Smart Polymers Ch01 Phase Transitions and Light Scattering]]
- [[The Role of Surfactants]]
- 相关概念：[[离子强度 Ionic Strength]]、[[表面交联 Surface Cross-linking]]、[[SAP（高吸水树脂）]]、[[蒙脱土 Montmorillonite]]、[[表面活性剂 Surfactant]]

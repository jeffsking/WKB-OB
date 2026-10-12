---
type: source
title: "Industrial Drying Ch31 Drying of Ceramics"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch31.md.md"
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Ceramic drying is usually carried out slowly to avoid cracks and deformation because a molded configuration must be maintained (p.727)"
  - "Initial drying rate must be limited: faster early rates rapidly attain the critical moisture content and cause a remarkable rate reduction in the falling-rate period, with shrinkage-induced internal stress causing failure (p.728)"
  - "Shrinkage is one of the most important quality-control factors, driving crack, warp and sagging and also influencing the drying process itself (p.730)"
  - "Suction potential splits by particle size: capillary suction dominates for particles larger than 50-µm order, while submicron particles shrink by osmotic suction from electrochemical (double-layer) effects (p.730)"
  - "Fast surface dry-up over a wet interior causes failure and deformation — the case-hardening mechanism in plain words (p.739)"
  - "Higher Biot number raises tensile stress; larger 1/Le (internal moisture diffusion) relieves it — internal moisture migration must be actively or passively enhanced, not just external heat transfer (p.839 per source numbering)"
summary_cn: "以刚性多孔坯体的收缩/开裂为主线，给出毛细-渗透吸势分类、恒速-降速设计方程与 Biot/Lewis 应力失效判据，是全书最清晰的'快干表面结壳'机理表述。"
tags: ["source/book", "drying/ceramics", "mechanism/shrinkage", "mechanism/case-hardening", "biot-lewis"]
tags_zh: ["书籍来源", "陶瓷干燥", "收缩机理", "表面结壳", "无量纲应力分析"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch15 Impingement Drying]]", "[[Industrial Drying Ch30 Drying of Nanosize Products]]", "[[Industrial Drying Ch33 Drying of Fibrous Materials]]", "[[Industrial Drying Ch4 Transport Properties in the Drying of Solids]]"]
---

# Chapter 31 — Drying of Ceramics

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.31, pp.727–740.
> Authors: Yoshinori Itaya, Shigekatsu Mori, Masanobu Hasatani.
> 注：页码按 PDF 页 − 21 推算（锚定 Ch.1 = p.1），与印刷版核对前属推算值。

## Scope & Position 范围与定位

Drying of molded ceramics — a rigid porous body whose shape must be preserved; dominant failure modes: shrinkage, cracking, warping, sagging, internal stress.
"drying is usually carried out slowly in order to avoid undesirable cracks and deformations. The reason is often attributed to the fact that ceramic drying involves maintaining a molded configuration." (p.727)
定位：全书"刚性多孔体收缩/开裂"参照系 — Ch.30（凝胶毛细开裂）、Ch.33（纤维收缩/角化）共用其毛细-渗透应力框架；它还提供了食物/纤维章节缺少的力学层（Biot/Lewis、拉应力峰值）。

## Four Difficulties 四大难点 (p.728)

"(1) the rise in the drying rate must be naturally limited because the faster rate in the beginning of drying results in rapid attainment of the critical moisture content and then the remarkable reduction of the rate in the falling rate period; (2) failures and irregular deformation may be generated due to drying shrinkage and internal stress it induces; (3) molding must be designed with predicting the deformation; (4) uniform drying is difficult..."
→ (1) 是恒速窗口上限，(2) 是开裂源头 — 两者合起来就是 case hardening 的孪生机理。

## Shrinkage Mechanism 收缩机理 (§31.3, p.730–732)

"Shrinkage during drying is one of the most important factors for the quality control of molded products. It is not only related to the deformation and the generation of crack, warp, and sagging but also influences the drying process itself." (p.730)

**吸势分类（关键粒径阈值）**：
"the capillary suction potential is affected by the capillary force in the materials consisting of particles larger than 50-µm order, the osmotic suction potential is brought about owing to an electrochemical effect between the water and the surface of particles smaller than micrometers or submicron order." (p.730)

**收缩几何极限**：颗粒间水膜消失、"the volume of the shrinkage may be equal to the volume of the removed water until particles contact with the neighbor particles and the removed water begins to be replaced in the void by air" (p.731) — 颗粒接触/空气进入即不可逆结构的起点（纤维角化的类比点）。取向各向异性：垂直取向方向收缩大于平行方向（Williamson/Cox，p.732）。

## Moisture Movement & Design Equations 传质与设计方程 (§31.4–31.5, p.732–735)

- 液相扩散主导至 ~20–30% db（坯料-dependent），其后汽相。
- 有效扩散系数 D（Eq. 31.1–31.2, Carman k=5）、多维守恒（31.3–31.4）、Darcy（31.8）、压力扩散率 D_p（31.9–31.10）。
- 恒速区长度（31.16–31.22, Lewis 关系 k_H≈h/c_p）、降速区 R_d = R_c·(w−w_e)/(w_c−w_e)（31.26）、总长 Z = z_c + z_d（31.29）。
- 工艺参数：热风 370–470 K；对数平均 ΔT 30–70 K；ha 230–350 W/(K·m³)（batch）。
- ⚠️ OCR 在 Eq. 31.1–31.10、31.34 有符号损伤（"«"代 ε、"tand"代 tanδ），定量复用前须对照印刷版。

## Dryer Families 干燥机族 (§31.6, p.737–739)

| Type | Key data / notes |
|---|---|
| Tunnel / band / batch | 常规热风；band 平行流 ha 45–95 |
| IR 红外 | 表面温度高于湿球可提速，但 "rapid drying rate may result in failure due to shrinkage"；效率：敞开 25–35% / 隧道 45–50% / 封闭 50–65%（Table 31.2）；降速段 IR+对流组合最有效 |
| Microwave 微波 | 内部加热 P = 5×10¹⁰ ε_r f E² tanδ（31.34）；内部温度可超表面 → 爆沸蒸汽膨胀，须功率控制 |
| Electric-current 电流加热 | 100–400 V 选择性内部加热，抑制绝缘子罩体开裂 |

## Failure Mechanics 失效力学 (§31.7, p.739–740)

"If the drying of molded clay is conducted too quickly, it may result in rapid surface dry-up while keeping a wet state in the inside. A fall in the fast-drying rate often causes the failure or the generation of deformation." (p.739)
→ 全书最干净的 case hardening 逐字定义：干硬应力皮 + 湿芯。

"Although a higher Bi results in remarkably stronger stress, the stress falls down with a larger 1/Le. Hence, heat-transfer enhancement in the dryer and uniform drying are not possible during ceramic drying unless the moisture-migration rate in the clay is actively or passively enhanced." (源页标 839，疑为 p.739 偏移笔误 [待验证])
→ 设计规则：提高内部水分迁移率（穿透风/吸风/蒸汽），而不是只加大外部 h。

## Limitations 局限

- 纯陶瓷/黏土证据（china clay、Kibushi、蜂窝绝缘子），无纤维/纸张/非织造实例 — 卫材迁移靠机理类比。
- 失效控制是诊断性（Bi/Le）而非规定性；原文自认 "few systematic investigations on the quality control of ceramics during drying" (p.740)。
- 除 IR 效率表外无 kJ/kg 能耗锚点。

## Hygiene Implication 卫材关联

- **★★★★★ 亚微米纤维的收缩按"渗透吸势"而非"毛细"建模**：纤维素/纳米纤维素直径在亚微米级（p.730 阈值以下），其收缩由双电层/电化学效应驱动 — 管理手段是电解质/电荷与干燥速率，而非单纯的孔-毛细思路。这直接改写绒毛浆/纳米纤维素垫材收缩的建模框架。
- **★★★★★ 逐字反 case-hardening 规则**：绝不允许表面快速干结而内部仍湿（p.739）——卫生纸/非织造纸幅卷曲与开裂的同源机理。表面先干时立即降热通量、切温和降速段条件。
- **★★★★ 初始干燥速率设上限**：尊重难点 (1)（p.728）——不要在产线开头猛开冲风/穿透风流量；恒速窗口短，过快起点会在降速段以收缩应力形式"还债"，导致纸幅翘曲/裂纹。
- **★★★★ 用 Bi/Le 规则解耦应力**：提高内部 1/Le（穿透风、吸抽、蒸汽助迁）优先于加大外部换热 — 冲风+吸抽协同的热力学依据（与 [[Industrial Drying Ch15 Impingement Drying]] 的纸幅实例互证）。
- **★★★ IR 只在降速段用并控功率**：对标陶瓷实践（p.737），在降速段用 IR/对流组合提速而不结壳 — 适用于擦拭布涂层固化。
- **★★★ 预期取向各向异性收缩**：垂直取向 > 平行取向（p.732）；定向非织造网须预估 MD/CD 尺寸差异并据此设计牵引/定型。
- 适用性边界：全章为无机坯体数据，迁移是机理级类比，无纤维实测验证 [待验证 — 需在绒毛浆/纳米纤维素垫上验证渗透吸势模型适用性]。

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch15 Impingement Drying]]
- [[Industrial Drying Ch30 Drying of Nanosize Products]]
- [[Industrial Drying Ch33 Drying of Fibrous Materials]]
- [[Industrial Drying Ch4 Transport Properties in the Drying of Solids]]

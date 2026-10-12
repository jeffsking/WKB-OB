---
type: source
title: "Ebewole Polymer Science Ch11 Unit Operations in Polymer Processing"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Ebewole Polymer Science Technology/chapters/Ebewole Polymer Science Technology_ch11.md.md"
date_published: 1997
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "only extrusion and injection molding, the two predominant polymer processing methods, are treated in fairly great detail. (Ch.11, p.282)"
  - "The choice of a particular processing technique is determined by part design, choice of material, production requirements, and, ultimately, cost–performance considerations. (Ch.11, p.282)"
  - "The frictional force generated between the resin, the barrel wall, and the rotating screw (viscous energy dissipation) is an important energy source for melting the resin. (Ch.11, p.284)"
  - "Polymer melts, being viscoelastic, recover the stored elastic energy as they emerge from the die — a process known as die swell. (Ch.11, p.285)"
  - "Fibers of various gauges and lengths are obtained in fiber extrusion. These can range from monofilament such as fishing lines to hundreds of continuous filaments extruded from the same die and drawn to hair-sized thickness. … The continuous filaments may be crimped for added bulk or made into staples. (Ch.11, p.285)"
  - "While the heating cycle has virtually no effect on the properties of the finished part, the cooling rate determines part shrinkage, final density, brittleness, and other physical properties. … A longer cooling time permits a greater ordered molecular arrangement in the crystalline polymer. (Ch.11, p.300–301)"
summary_cn: "《Ebewole 高分子科学与技术》第 11 章聚合物加工单元操作：以挤出与注塑两大主流方法为重点，系统展开七大加工路线（挤出、注塑、吹塑、滚塑、热成型、压缩/传递模塑、铸造），涵盖螺杆塑化、黏性能量耗散、模口膨胀、共挤出、分子取向、冷却速率-结晶度关系等工程要点；但明确未覆盖纺粘/熔喷、溶液纺丝、压光等非织造专有工艺。"
tags: ["source/book", "polymer-science", "polymer-processing", "extrusion", "injection-molding", "blow-molding", "rotational-molding", "thermoforming", "die-swell", "coextrusion", "fiber-extrusion", "molecular-orientation"]
tags_zh: ["聚合物加工", "单元操作", "挤出", "注塑", "吹塑", "滚塑", "热成型", "模口膨胀", "共挤出", "纤维挤出", "分子取向", "冷却速率与结晶度"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]", "[[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]", "[[Ebewole Polymer Science Ch10 Polymer Reaction Engineering]]", "[[Manufactured Fibre Technology Ch19 Spunbonding and Melt-Blowing Processes]]", "[[Handbook of Nonwovens]]", "[[皮芯复合纤维]]"]
---

# Ebewole Polymer Science Ch11 Unit Operations in Polymer Processing

> Source: Ebewole, *Polymer Science and Technology*, Ch.11 (Unit Operations in Polymer Processing), pp. 282–307. 章节主题：七类主流加工单元操作，重点为挤出与注塑。

Chapter 11 covers the route from **pellets to finished article（从颗粒到制品）**. The chapter states its own scope limit up front.

本章的自我定位与缺口同样重要：**非织造专有工艺（纺粘/熔喷、溶液纺丝、压光）未被作为独立工艺处理**，需配合专用文献。

## Scope and Selection Logic 加工选型逻辑

> "only extrusion and injection molding, the two predominant polymer processing methods, are treated in fairly great detail." (Ch.11, p.282)

> "The choice of a particular processing technique is determined by part design, choice of material, production requirements, and, ultimately, cost–performance considerations." (Ch.11, p.282)

（中文：加工选型四要素 = 制品设计、材料选择、产量要求、成本-性能权衡。）

| Unit operation 单元操作 | Definition 定义 | Source wording 原文表述 |
|---|---|---|
| Extrusion 挤出 | 热塑性粉/粒料 → 连续均匀熔体 → 经口模成型为等截面制品 | "Extrusion is a processing technique for converting thermoplastic materials in powdered or granular form into a continuous uniform melt, which is shaped into items of uniform cross-sectional area by forcing it through a die." (p.282) |
| Injection molding 注塑 | 间歇式：熔融塑化后高压注入闭合并冷却的模具 | "Injection molding is a batch molding process in which a thermoplastic resin or a thermoset material is melted or plasticized, and then injected at high pressure into a closed, cooled mold." (p.287) |
| Blow molding 吹塑 | 先成型中空型坯（parison），再在模具内吹胀贴壁 | "The blow molding process consists of a sequence of steps leading to the production of a hollow tube or parison from a molten thermoplastic resin. This is then entrapped between the two halves of a mold of the desired shape." (p.298) |
| Rotational molding 滚塑 | 用于形状不复杂的中空制品 | "Rotational molding (rotomolding) is used primarily for the manufacture of hollow articles that are not of complex shapes." (p.300) |
| Thermoforming 热成型 | 热塑性片材加热至可塑温度后贴模成型 | "In thermoforming, a thermoplastic sheet is heated to a pliable temperature and then formed against or into a mold." (p.301) |
| Compression molding 压缩模塑 | 开放模腔中加热加压流动并固化 | "Compression molding involves placing a predetermined quantity of uncured thermosetting compound or a thermoplastic material in the cavity of an open mold, closing the mold under pressure, and heating to effect the flow and cure of the resin." (p.304) |
| Transfer molding 传递模塑 | 热固性料先在热腔塑化，再压入预热闭合模 | "In transfer molding, the uncured thermosetting material is first plasticized in a hot chamber and then forced under pressure into a preheated closed mold." (p.305) |
| Casting 铸造 | 液态料浇入模具，靠冷却或聚合固化 | "In the casting process, a liquid material is poured into a mold and allowed to solidify by physical (e.g., cooling) or chemical (e.g., polymerization) means resulting in a rigid object that generally reproduces the mold cavity detail with great fidelity." (p.305) |

## Extrusion 挤出

> "The screw, which is the moving part of the extruder, is designed to pick up, mix, compress, and move the polymer as it changes from solid granules to a viscous melt." (Ch.11, p.283)

**Screw geometry 螺杆几何**：螺棱 = **flight**，相邻螺棱对应边的轴向距离 = **pitch（螺距）**："The thread of an extruder screw is called a flight, and the axial distance from the edge of one flight to the corresponding edge on the next flight is called the pitch." (p.283)

> "The frictional force generated between the resin, the barrel wall, and the rotating screw (viscous energy dissipation) is an important energy source for melting the resin." (Ch.11, p.284)

（中文：熔融能量不只来自外加热，**黏性能量耗散（viscous energy dissipation）是重要热源** —— 螺杆转速提高会增加剪切生热，是熔体温度控制的关键变量。）

### Die swell 模口膨胀

> "Polymer melts, being viscoelastic, recover the stored elastic energy as they emerge from the die — a process known as die swell." (Ch.11, p.285)

> "In general, a high-speed, high-temperature process provides a more uniform melt than a low-speed, low-temperature process." (Ch.11, p.285)

### Fiber extrusion and coextrusion 纤维挤出与共挤出

> "Fibers of various gauges and lengths are obtained in fiber extrusion. These can range from monofilament such as fishing lines to hundreds of continuous filaments extruded from the same die and drawn to hair-sized thickness." (Ch.11, p.285)

> "The continuous filaments may be crimped for added bulk or made into staples." (Ch.11, p.285)

> "In coextrusion, two or more different materials or the same material with two different colors are extruded through the same die so that one material flows over and coats the other." (Ch.11, p.285)

## Injection Molding 注塑

> "The plasticizing capacity of an injection molding machine is defined as the maximum weight of polymer that can be melted, accumulated, and stored in the barrel of the machine." (Ch.11, p.291)

> "The screw retracts into a position that allows a predetermined amount of melt to accumulate." (Ch.11, p.291)

> "Melt temperature must be sufficiently high to ensure that complete fusion of the polymer particles has been achieved." (Ch.11, p.291)

> "Melt temperatures in excess of this limit will cause the polymer to degrade." (Ch.11, p.291)

**Throughput and residence time 产出与停留时间（例 11.5, p.293）**：

```
Q   = W / t_c     (machine output / plasticizing capacity 机器产出)
t_r = I_w / Q     (residence time = inventory / output 停留时间 = 库量 / 产出)
```

（中文：熔体温度必须在"完全塑化"与"热降解"之间的窄窗口内；停留时间 t_r 是热降解风险的量化指标。）

> "Polymer molecules generally assume a random orientation in the melt. As the melt is forced through the gate during mold filling, polymer molecules tend to lose this random orientation and align themselves along the direction of flow." (Ch.11, p.296)

## Orientation and Cooling 取向与冷却

**Biaxial orientation 双向取向（吹塑）**：

> "During blow molding, the polymer is stretched biaxially — in the axial and radial directions — causing the polymer molecules to align in a biaxial orientation." (Ch.11, p.299)

**Cooling rate → structure → properties 冷却速率决定结构（滚塑）**：

> "While the heating cycle has virtually no effect on the properties of the finished part, the cooling rate determines part shrinkage, final density, brittleness, and other physical properties." (Ch.11, p.300)

> "A longer cooling time permits a greater ordered molecular arrangement in the crystalline polymer. The resultant enhanced crystallinity leads to higher specific gravity and shrinkage and reduced brittleness." (Ch.11, p.300–301)

（中文：**加热段几乎不影响性能，冷却段决定一切** —— 收缩率、密度、脆性；冷却越慢，结晶越完善，比重与收缩上升、脆性下降。这条规律可直接迁移到纤维与热轧粘合的冷却定型。）

**Compression molding 的产能约束**："Compression molding is limited to the fabrication of small parts and low production volumes because the process is slow." (p.304)

**Nylon casting 尼龙铸造**："Cocatalyzed anionic polymerization is currently the most widely used nylon casting method." (p.306)

## Academic Context and Critique 学术对话与批判

- **本章缺口（原书自述与业务提示共同确认）**：以下非织造核心工艺**未作为独立工艺处理** —— melt spinning / spunbond / meltblown（仅在 "fiber extrusion" 中隐含提及）、solution / wet / dry-jet wet spinning、calendering（压光）、blown film bubble / layflat、fiber crimping / texturizing / false-twist（仅一句 "crimped for added bulk"）、sheeting / coating / film casting（仅列为挤出产品类别）、reactive extrusion、spin finish。
- **聚焦刚性制品**：全章以注塑件、中空容器、片材为主，缺少柔性多层复合（非织造层压、热风穿透粘合）的加工经验。
- **"high-speed, high-temperature → 更均匀熔体"（p.285）是有条件的表述**：高速高剪切在提高熔融均匀性的同时升高熔体温度、增加降解与模口膨胀风险；本章未给出黏性耗散与降解的定量边界。
- **冷却速率-结晶度关系只作定性陈述**：本章给出方向（慢冷 → 结晶完善 → 比重↑、收缩↑、脆性↓），但**未给出结晶动力学模型（如 Avrami）或具体冷却速率数值** —— [待验证] 定量部分需另引文献。

## Hygiene Implication 卫材关联

1. **Fiber extrusion 是纺粘/熔喷的硬件基础.** "hundreds of continuous filaments extruded from the same die and drawn to hair-sized thickness"（p.285）直接描述熔体纺丝；"crimped for added bulk or made into staples" 对应短纤→针刺/热风非织造路线。但**拉伸比、冷却气流、纺丝甬道等专有参数本章未覆盖**。参见 [[Manufactured Fibre Technology Ch19 Spunbonding and Melt-Blowing Processes]]、[[Handbook of Nonwovens]]。
2. **Die swell 与熔喷模头设计.** 熔体黏弹性导致的模口膨胀（p.285）直接决定熔喷纺丝孔出口的初始纤维直径与射流稳定性 —— 这是"口模孔径 ≠ 纤维直径"的根因。参见 [[Manufactured Fibre Technology Ch19 Spunbonding and Melt-Blowing Processes]]。
3. **Coextrusion ↔ 双组分纤维.** 本章的共挤出定义（一种材料包覆另一种，p.285）是**皮芯（sheath-core）与并列（side-by-side）双组分纤维**的工艺原型，皮芯结构正是热粘合（thermal bonding）纤维的低温粘合机制所在。参见 [[皮芯复合纤维]]。
4. **Plasticizing capacity / residence time → 纺丝熔体均匀性.** Q = W/t_c 与 t_r = I_w/Q（p.293）可直接用于评估纺丝螺杆的塑化能力与热降解暴露时间；结合 Ch.9 的抗氧剂体系判断树脂在高温停留下的降解风险。参见 [[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]、[[Ebewole Polymer Science Ch10 Polymer Reaction Engineering]]。
5. **冷却速率-结晶度 → 热轧/热风粘合窗口.** "cooling rate determines part shrinkage, final density, brittleness"（p.300）是热轧辊温、冷却速率与纤网收缩/手感之间关系的通用机制；其热力学边界（Tg/Tm、结晶速率）见 Ch.4。参见 [[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]。
6. **Not covered 本章未涉及**: 非织造专有工艺参数（纺粘牵伸、熔喷热风、水刺、热轧压区）、非织造布幅宽与在线复合控制。

## Related Sources 关联来源

- [[Ebewole Polymer Science Ch04 Thermal Transitions in Polymers]]
- [[Ebewole Polymer Science Ch09 Polymer Additives and Reinforcements]]
- [[Ebewole Polymer Science Ch10 Polymer Reaction Engineering]]
- [[Manufactured Fibre Technology Ch19 Spunbonding and Melt-Blowing Processes]]
- [[Handbook of Nonwovens]]
- [[皮芯复合纤维]]

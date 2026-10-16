---
type: concept
title: "导电无纺布 Conductive Nonwoven"
domain: [卫材研发, 无纺布工艺]
status: growing
updated: 2026-09-30
tags: [conductive-nonwoven, conductive-textile, e-textile, ALD, AZO, wetness-sensing, electrochromic]
---

# 导电无纺布 Conductive Nonwoven

> 📌 **Page completed 2026-09-30** from 2 citing sources. All figures traced to their source pages. Anything not evidenced is marked `[待补]`.

## Definition 定义

形式化定义：**定义待补（引用来源未给出明确定义）**。库内**没有**任何页面给出"导电无纺布（conductive nonwoven）"的定义或规格。引用来源（cited-by）讨论的是一次**导电涤纶织物（conductive polyester textile, CPT）**——纬编涤纶 + ALD 沉积 AZO 的机织 / 针织织物，**并非无纺布**；该来源把"可迁移至纺粘 / 熔喷无纺布"明确标注为**推演（speculative）**（源：[[Interactively Mechanochromic Electronic Textile Sensor]]）。

> ⚠️ **口径提示**：本页所有实测数字来自**导电织物**（CPT），不是导电无纺布。无纺布侧的导电化路径在库内仍属推演，尚无实测数据。

## Key Parameters and Data 关键参数与数据

| Parameter 参数 | Value 数值 | Source 来源 |
|---|---|---|
| CPT 电导率（导电涤纶织物） | 0.012 S/m | [[Interactively Mechanochromic Electronic Textile Sensor]] |
| CPT 导电化工艺 | 等离子活化（15 Pa, 25 °C, 10.2 W, 10 min）→ 150 °C ALD 沉积 AZO（DEZ/TMA/H₂O；ZnO:Al₂O₃ 循环 20:1） | [[Interactively Mechanochromic Electronic Textile Sensor]] |
| CPT 应变系数 GF（负值） | 0–32 %: −1.76；32–98 %: −0.36；98–200 %: −0.04 | [[Interactively Mechanochromic Electronic Textile Sensor]] |
| 响应 / 恢复时间 | 5 % 应变下 ≈ 0.30 s / < 0.22 s | [[Interactively Mechanochromic Electronic Textile Sensor]] |
| 耐久性 | 30,000 次拉伸-释放循环（30 % 应变，2 Hz）无迟滞、无退化 | [[Interactively Mechanochromic Electronic Textile Sensor]] |
| 导电纱线（导电元件） | 优选**银镀导电缝纫线 60 Ω/m**；另列导电线 / 导电胶带 / 导电橡胶 / 导线 | [[导电纱线 Conductive Yarn]] |
| 纺织电阻跨度 | 约 4 个数量级（0.5 Ω/m 至 kΩ/m）；**无卫材传感器选型判据** | [[导电纱线 Conductive Yarn]] |

## Method / Mechanism 方法 / 机理

- **纤维级导电化的两条库内路线**：
  1. **织物后处理路线（CPT）** —— 等离子活化后低温 ALD 沉积掺铝氧化锌（AZO），在涤纶织物上形成纤维级导电层；原文强调该路线"低温、纤维保形、均匀"（源：[[Interactively Mechanochromic Electronic Textile Sensor]]）。
  2. **合成纤维本体改性路线** —— 合成纤维本身导电性差且易积聚静电（p.374）；三条命名路线为 **化学改性（chemical modification）、物理共混（physical blending）、添加导电物质（carbon / metal / metal oxide 粉末）**；其中**化学键合耐洗性最好、物理共混最差**，而靠导电颗粒者需借助**共轭双组分纺丝（conjugated bicomponent）** 才能保住强度（p.377，源：[[Manufactured Fibre Technology Ch14 Speciality Polyamide and Polyester Yarns]]；经 [[导电纱线 Conductive Yarn]] 转述）。
- **电阻式（resistive）传感器机理**：控制器在导电纱线两端施加电压并监测端电压；**干态读数约为满量程，一旦排泄液润湿该通路，测得电位即崩塌** —— 这是"是否尿湿 / 是否侧漏"的电子式判据（源：[[导电纱线 Conductive Yarn]]；原件 [[US11013641 Garment for Detecting Absorbent Article Leakage]]）。
- **双向信号耦合（光学 + 电学）**：CPT 与超分子光子弹性体半嵌入，拉伸时**晶格间距收缩 → λmax 蓝移**（Bragg 衍射）与**负电阻变化**同步发生；光学通道可规避温湿度干扰（源：[[Interactively Mechanochromic Electronic Textile Sensor]]）。

## Hygiene Relevance 卫材关联

- **湿 / 压力可视化指示的候选载体**：CPT 方案把"电阻变化 + 结构色变化"做成无需外接电源、肉眼可判读的指示层，对尿裤"何时更换"提示有借鉴价值；**注意该应用在原文中属推演**（源：[[Interactively Mechanochromic Electronic Textile Sensor]]）。
- **无纺布化仍是推演**：原文把"迁移至纺粘 / 熔喷无纺布、为尿裤 / 湿巾产线提供低克重导电基材"列为**推演**，无实测（源：[[Interactively Mechanochromic Electronic Textile Sensor]]）。
- **既有卫材应用不落在芯体上**：库内唯一的卫生级导电用例是 K-C 侧漏检测**衣物（garment）**——导电纱线位于外穿衣物而非吸收芯体，权利要求保护的是 garment 本身（源：[[导电纱线 Conductive Yarn]]、[[US11013641 Garment for Detecting Absorbent Article Leakage]]）。
- 关联：[[导电纱线 Conductive Yarn]]、[[机械变色 Mechanochromic]]、[[结构色 Structural Color]]、[[光子晶体 Photonic Crystal]]、[[电子纺织品 E-textile]]。

## Open Questions 待补

- **本主题无定义、无实测**：库内没有"导电无纺布"的定义、版式、电阻规格或测试方法；本页数字全部来自导电**织物**（CPT）与导电纱线 `[待补]`。
- **无卫生级导电材料规格**：未见耐尿液洗、皮肤接触、银镀生物相容性等卫材级判据（源：[[导电纱线 Conductive Yarn]]）`[待补]`。
- **无选型判据**：纺织电阻跨 ~4 个数量级（0.5 Ω/m 至 kΩ/m），但库内无"卫材传感器该选多大电阻"的判据（源：[[导电纱线 Conductive Yarn]]）`[待补]`。
- **成本与供应未评估**：银镀导电缝纫线用于一次性品的成本与供应，库内未涉及（源：[[导电纱线 Conductive Yarn]]）`[待补]`。
- **⚠️ 边界提醒**：cited-by 来源的正文主题是**针织 / 机织导电涤纶织物**；将其等同于"导电无纺布"属于跨材料类别外推，引用时须注明口径（源：[[Interactively Mechanochromic Electronic Textile Sensor]]）。

## Related Sources 关联来源

- [[Interactively Mechanochromic Electronic Textile Sensor]]
- [[导电纱线 Conductive Yarn]]
- [[US11013641 Garment for Detecting Absorbent Article Leakage]]
- [[Manufactured Fibre Technology Ch14 Speciality Polyamide and Polyester Yarns]]
- 相关概念：[[电子纺织品 E-textile]] · [[机械变色 Mechanochromic]] · [[结构色 Structural Color]] · [[光子晶体 Photonic Crystal]] · [[Nonwoven 非织造布]]

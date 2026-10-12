---
type: source
title: "Interactively Mechanochromic Electronic Textile Sensor"
source_type: book
source_path: RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mechanochromic_Photonic_Sensors_拆解/交互式机械变色电子织物传感器_拆解.md.md
original_link: ""
date_published: 2021
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
author: "Kai Zhao et al. (Dalian Univ. of Technology / UC; corresp. W. Niu)"
edition: ""
publisher: "Chemical Engineering Journal 426, 130870"
year: 2021
isbn: ""
original_language: "EN"
parent_book: "[[Mechanochromic Photonic Sensors]]"
key_claims:
  - "First textile sensor coupling electrical + structural-colour optical read-out: supramolecular photonic elastomer (PE) semi-embedded in conductive polyester textile (CPT)."
  - "Toughness 35.6 kJ/m3; response approx. 0.30 s, recovery < 0.22 s; optical and electrical response constant after 30,000 stretch-release cycles."
  - "Distinctive NEGATIVE resistance variation with strain (GF = -1.76 / -0.36 / -0.04 over 0-32% / 32-98% / 98-200%)."
  - "Mechanism is Bragg diffraction: stretching reduces vertical lattice spacing d0->d, so lamax blue-shifts; optical channel also rejects temperature/humidity interference."
pages_linked: ["[[Mechanochromic Photonic Sensors]]", "[[机械变色 Mechanochromic]]", "[[结构色 Structural Color]]", "[[光子晶体 Photonic Crystal]]", "[[导电无纺布 Conductive Nonwoven]]", "[[Wearable Electronics (National Science Review 2023)]]"]
---

# Interactively Mechanochromic Electronic Textile Sensor with Rapid and Durable Electrical/Optical Response

## One-line Position 一句话定位
The most engineering-mature source in this vault for a textile-integrated strain indicator: a woven fabric carrying both a negative-resistance electrical signal and a reversible structural colour, wearable/sewable on skin, durable over 30,000 cycles.

> Source note: compiled from an OCR scan with character noise; quotes below are the space-restored form with no words added or removed.

## Key Numbers & Conclusions 提炼数字与结论

| 项目 Item | 数值/结论 Value | 备注 Note |
|---|---|---|
| 韧度（MET 传感器） | 35.6 kJ/m³ | 对比 PTIP 17.6 / PE 20.7 / CPT 24.9 kJ/m³ |
| PTIP 弹性体 | 2.0 MPa，伸长 1270 %，17.6 kJ/m³ | Tg ≈ -75 °C（室温高弹态） |
| PE（PTIP + PCs） | 3.3 MPa，1126 %，20.7 kJ/m³ | |
| CPT 电导率 | 0.012 S/m | 纬编涤纶 + ALD 沉积 AZO |
| 应变系数 GF | 0-32 %: -1.76；32-98 %: -0.36；98-200 %: -0.04 | 负值 |
| 响应/恢复 | 5 % 应变下 ≈0.30 s / <0.22 s | 电、光信号同步 |
| 耐久性 | 30,000 次拉伸-释放循环（30 % 应变，2 Hz）无迟滞、无退化 | |
| 频率无关性 | 0.125-1.0 Hz 内 ΔR/R₀ 与频率无关 | |
| 反射峰红移（PE 渗入后） | 527 nm → 604 nm | 折射率增大 + 晶格间距增大 |
| 拉伸蓝移 | 0 %→51.6 % 应变 λmax 单调下降 | 0 %→20 % 由橙渐变至绿 |
| 两段线性区 | εx < 15.9 % 快速变化；15.9 %-51.6 % 变化不显著 | 邻近颗粒间距闭合 |
| 屈指演示 | λmax 604 nm → 571 nm（橙红→绿） | |
| CPT 工艺 | 等离子活化（15 Pa, 25 °C, 10.2 W, 10 min）→ 150 °C ALD 沉积 AZO | DEZ/TMA/H₂O；ZnO:Al₂O₃ 循环 20:1 |
| PTIP 合成 | PTMG 5 g + IPDI 1048 µL + 1,5-PDO 0.26 g + DBTDL，80 °C / 2 h | [NCO]/[OH] = 1:1 |

## Core Mechanism 核心机理

- **双通道动机** — "the current textile-based electronics are limited by single electrical signal input/output, and unable to be visualized directly by human eyes" (L22-L24)
- **集成方案** — "The MET sensors are based on the ingenious coupling of new supramolecular photonic elastomers (PEs) with hierarchical-fiber-structured conductive polyester textiles (CPTs)." (L29-L30)
- **结构色定义** — "Structural colors, arising from light interaction with periodically ordered nanostructures that are widely known as photonic crystals (PEs), are widespread in nature" (L75-L77)
- **晶格间距调控（物理机制）** — "when the MET sensor is stretched in the horizontal direction, the lattice spacing d is reduced from d0 to d in the vertical direction, thus resulting in a decrease in λmax" (L636-L639) — 即 Bragg 定律
- **半嵌入结构（同步的关键）** — "the CPT was partially embedded in PTIP elastomer and therefore, the two binds tightly together, ensuring their simultaneous movements during stretching" (L449-L454)；工艺上"this is the key to forming the semi-embedding" (L196-L197)
- **负电阻机制** — ① 纱线结点接触面积增大（决定电阻的关键）；② 同一线圈内纤维更致密，降低纱线自身电阻 → 总电阻随应变下降 (L852-L864)
- **抗干扰优势** — "the introduction of additional optical response can effectively avoid the measurement errors under interference (i.e., temperature, humidity)" (L1026-L1031)
- **可穿戴形态** — "the MET sensor can be easily knitted, sewed on garments or attached on human skin directly for tracking human joint motions with dual-signal response" (L1038-L1044)

## Business Connection Points 业务连接点

- **可视化湿/压力指示（尿裤核心场景）** — "电阻变化 + 结构色变化"双信号同步（L867-L879），可做无需外接电源、肉眼即可判断状态的指示层，例如吸水/受压区域变色提示更换时机；且光学通道可规避温湿度干扰（L1026-L1031），对尿液环境尤其有价值（推演）。
- **导电无纺布功能化路径** — "纬编涤纶织物 + 等离子活化 + ALD 沉积 AZO（150 °C）"实现纤维级导电，CPT 电导率 0.012 S/m（L410，工艺 L199-L247）。该"低温、纤维保形、均匀"思路可迁移至纺粘/熔喷无纺布，为尿裤/湿巾产线提供低克重导电基材（推演）。
- **与 SAP 膨胀耦合** — 变色机制是"应变→晶格间距调控→λmax 蓝移"（L636-L639, L650-L659），响应区间 0-51.6 % 且线性度可经 Bragg 定律设计。若与 SAP 层复合，吸水膨胀本身即应变源，可发展为"湿度/尿量可视化指示贴"；**须验证膨胀方向与变色区间匹配（推演）。**
- **半嵌入层合抗分层耐久** — CPT 部分嵌入弹性体形成一体化结构，30,000 次循环不退化（L446-L454, L851-L860, L1084-L1089），对尿裤腰贴、弹性耳贴等反复拉伸部位的功能层附着工艺（防分层、防脱层）有借鉴价值（推演）。
- **智能包装 / 防篡改可视化** — "无需电子仪器即可人眼可视化"的通用平台（L38-L40, L989-L997, L1095-L1100），可用于卫生用品包装开启指示、运输挤压报警或货架互动元素（推演）。

## Related Pages 关联页面
- 同域合集 Sibling collection：[[Mechanochromic Photonic Sensors]]
- 概念 Concepts：[[机械变色 Mechanochromic]]、[[结构色 Structural Color]]、[[光子晶体 Photonic Crystal]]、[[Wearable Electronics (National Science Review 2023)]]
- 对照：[[Self-Powered Photonic Sensor CLCE Sandwich]]（同为应变→结构色，但走胆甾液晶通道且加摩擦电）
- 关联主题：[[SAP（高吸水树脂）]]、[[ADL（导流层）]]、弹性无纺布/腰贴附着工艺

## Source 原文
- 本地路径 Local path：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mechanochromic_Photonic_Sensors_拆解/交互式机械变色电子织物传感器_拆解.md.md`
- 原文链接 Original link：Chemical Engineering Journal 426 (2021) 130870

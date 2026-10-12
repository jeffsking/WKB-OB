---
type: source
title: "Seymour Polymer Chemistry Ch04 Testing and Spectrometric Characterization"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Seymour Polymer Chemistry/chapters/Seymour Polymer Chemistry_ch04.md.md"
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Public acceptance of polymers is associated with an assurance of quality based on successful long-term and reliable tests; much dissatisfaction relates to failures that proper testing, design and quality control might have prevented."
  - "ASTM, through committees D-1 on paint and D-20 on plastics, develops standard tests; new tests are verified through 'round-robin' testing and accepted by consensus."
  - "Nondestructive tests result in no chemical change in the material; destructive tests involve a change in chemical structure of at least part of the tested material — and the distinction may differ depending on the test, material and definition."
  - "ASTM D-543, the classic chemical resistance test, measures the percentage weight change (PWC) of samples after immersion in different liquid systems."
  - "Condensation polymers generally show good stability to nonpolar liquids but only moderate or poor stability toward polar agents, acids and bases, because of the polarity of the connective condensation linkages; vinyl polymers show moderate to good stability toward both because the carbon–carbon backbone is not particularly susceptible to polar attack."
  - "IR absorption requires a change in dipole moment during the vibration, whereas Raman scattering requires a change in polarizability — the two techniques are therefore complementary."
summary_cn: "第4章是表征方法百科：以 ASTM/ISO 标准体系与 round-robin 共识流程为骨架，区分破坏性/非破坏性测试，并系统展开介电、化学耐性（ASTM D-543 PWC）与 IR/ATR/Raman/NMR/X-ray/DSC/TGA/ESR/ESCA 光谱谱系，确立“质量保障靠标准化可复现测试”的工程哲学。"
tags: ["source/book", "testing", "characterization", "astm", "spectroscopy", "atr-ftir", "raman", "dsc", "tga", "chemical-resistance"]
tags_zh: ["聚合物测试", "表征", "ASTM标准", "红外光谱", "拉曼光谱", "衰减全反射", "热分析", "化学耐性", "质量控制"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Seymour Polymer Chemistry Ch03 Molecular Weight of Polymers]]", "[[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]]", "[[Seymour Polymer Chemistry Ch06 Step-Reaction Polymerization]]", "[[Absorbent Product Testing]]", "[[Absorbent System Overview（K-C 吸收系统概览培训·2021-02）]]"]
---

# Seymour Polymer Chemistry Ch04 Testing and Spectrometric Characterization

> Source: Seymour/Carraher, *Polymer Chemistry*, Ch.4 — Testing and Spectrometric Characterization of Polymers.
> 定位说明 / Citation convention: 原文为 .txt 抽取件，**无正式印张页码**，本报告以文件行号（line no.）定位。原抽取件对 NMR 与 DSC/TGA 标注了"[未找到完整原句]"，本页对应处保留 [待验证] 标记。

## Executive Summary 内容概要

Chapter 4 is the book's encyclopedia of characterisation: **standard tests (ASTM/ISO) → electrical / thermal / optical / magnetic properties → spectrometric characterisation (IR, UV-Vis, NMR, Raman, X-ray, DSC, TGA, ESR, ESCA)**. Seymour's organising principle is the **destructive vs nondestructive dichotomy**, with the ASTM standard system as the skeleton. 本章的工程哲学是：**质量保障（quality assurance）只能通过标准化、可复现、跨实验室可比的测试实现**。

## Quality Assurance and Standardization 质量保障与标准化

> *"Public acceptance of polymers is usually associated with an assurance of quality based on a knowledge of successful long-term and reliable tests. In contrast, much of the dissatisfaction with synthetic polymers is related to failures that might have been prevented by proper testing, design, and quality control."* (line 4-6)

> *"The American Society for Testing and Materials (ASTM), through its committees D-1 on paint and D-20 on plastics, has developed many standard tests, which may be referred to by all producers and consumers of polymeric materials."* (line 7-9)

> *"New tests are continuously being developed, submitted to the appropriate ASTM committee, and after adequate verification through 'round-robin' testing, finally accepted by concensus, as standard tests."* (line 19-21)

**标准化流程 / Standardisation path**：committee 提案 → round-robin 循环比对验证 → consensus 共识 → 标准发布。每个 ASTM 测试由唯一的字母+数字组合指定（line 22）。全球对应体系还包括 ANSI、ISO、BSI、DIN。

## Destructive vs Nondestructive Testing 破坏性与非破坏性测试

> *"Nondestructive tests are those that result in no chemical change in the material. Nondestructive tests include many electrical property determinations, infrared and ultraviolet spectroanalysis, simple melting point determinations, density and color determinations, and most mechanical property determinations."* (line 41-45)

> *"Destructive tests are those where there is a change in the chemical structure of at least a portion of the tested material."* (line 46)

> *"What constitutes destructive and nondestructive tests may differ depending on the test, material, and definition. Thus, mechanical properties of solid polymers and viscosity test results of polymer melts may vary depending on the past history of the polymer."* (line 49-51)

| 类别 Category | 判据 Criterion | 典型方法 Typical methods |
|---|---|---|
| Nondestructive 非破坏性 | 材料无化学变化 no chemical change | 电性能测定、IR/UV 光谱、熔点测定、密度与颜色测定、多数力学性能测定 |
| Destructive 破坏性 | 至少部分材料化学结构改变 | 燃烧、热分解、化学侵蚀类试验 |

## Electrical Properties 电性能

> *"Some important dielectric properties are dielectric loss, loss factor, dielectric constant (or specific inductive capacity), direct current (DC) conductivity, alternating current (AC) conductivity, and electric breakdown strength."* (line 60-68)

- **Eq. 4.1**：C = Q / V
- **Eq. 4.2**：ε = C / C₀ — 介电常数 = 插入介电材料后的电容与真空电容之比

## Chemical Resistance 化学耐性

> *"The classic test for chemical resistance (ASTM D-543) measures the percentage weight change (PWC) of test samples after immersion in many different liquid systems."* (line 532-542)

**骨架化学决定耐性规律 / Backbone chemistry governs resistance**：

- *"As expected, condensation polymers generally exhibit good stability to nonpolar liquids while they are generally only (relatively) moderately or unstable toward polar agents and acids and bases. This is because of the polarity of the connective 'condensation' linkages within the polymer backbone."* (line 680-688)
- *"By comparison, vinyl type of polymers exhibit moderate to good stability toward both polar and nonpolar liquids and acids and bases. This is because the carbon–carbon backbone is not particularly susceptible to attack by polar agents..."* (line 684-688)

| 聚合物类型 Polymer class | 非极性液体 Nonpolar | 极性试剂/酸碱 Polar agents, acids, bases | 原因 Reason |
|---|---|---|---|
| Condensation 缩聚类（PET、PA 等） | 稳定 good stability | 仅中等或不 moderately / unstable | 主链缩合键（酯/酰胺）具极性 |
| Vinyl 乙烯基类（PE、PP 等） | 中等至良好 moderate–good | 中等至良好 moderate–good | C–C 主链不易受极性试剂攻击 |

## Spectrometric Characterization 光谱表征

### IR and ATR 红外与衰减全反射

> *"ATR occurs when radiation enters from a more dense (i.e., a material with a higher refractive index) into a material that is less dense (i.e., with a lower refractive index). The fraction of the incident radiation reflected increases when the angle of incidence increases."* (line 906-909)

> *"The radiation penetrates a short depth into the interface before complete reflection occurs. This penetration is called the evanescent wave."* (line 910-912)

ATR 使固体/薄膜无需制样即可测 IR；倏逝波（evanescent wave）只在界面穿透极短深度，故 ATR 本质是**表面敏感**技术。本章还覆盖 FTIR、DRIFTS、PAS、IR microscopy 等变体。

### Raman 拉曼光谱

> *"Raman spectroscopy is similar to IR spectroscopy in that it investigates polymer structure focusing on the vibrational modes. Whereas IR is a result of energy being absorbed by a molecule from the ground state to an excited state, Raman spectroscopy is a scattering phenomenon where the energy of photons is much larger than the vibrational transition energies."* (line 954-958)

**选择定则 / Selection rules**：*"IR absorption occurs only if there is a change in the dipole moment during the vibration whereas a change in polarizability is required for Raman scattering to occur."* (line 967-969)

| 对比维度 | IR 红外 | Raman 拉曼 |
|---|---|---|
| 物理本质 | 吸收 absorption（基态→激发态） | 散射 scattering（光子能量远大于振动能级） |
| 选择定则 | 振动时**偶极矩**变化 | 振动时**极化率**变化 |
| 强响应基团 | C=O 等极性基团 | C=C 等非极性/对称基团 |

### Hyphenated Methods 联用技术

> *"Today there are many so-called hyphenated methods with IR acting to illustrate this. Hyphenated methods involving IR include GC-IR where the IR spectra are taken of materials as they are evolved through the column. Related to this are HPLC-IR, TG-IR, and MS-IR."* (line 950-953)

### NMR / X-ray / DSC / TGA / ESR / ESCA

- **NMR**：本章包含 proton (¹H) NMR 与 ¹³C NMR 的结构表征描述，但**原抽取件未给出完整原句** [待验证]。
- **DSC / TGA**：原文说明 DSC 测热流随温度变化以揭示 Tg、Tm 与结晶转变；TGA 测质量随温度变化以揭示分解与填料含量——**原抽取件标注"[未找到完整原句]"**，此处为转述 [待验证]。
- **X-ray diffraction**：用于结晶度测定。**ESR (EPR)** 测自由基/顺磁中心。**ESCA (XPS)** 测表面化学。

## Methodology Critique 方法论批判

- **破坏性/非破坏性的二分是模糊的**：Seymour 自己指出该划分取决于测试、材料与定义。黏度测试因改变链取向可被视为"破坏"，但化学结构未变又属"非破坏"——这一模糊性正是聚合物**机械历史敏感性**的体现。
- **标准测试的滞后性**：round-robin → consensus 流程严谨，但可能滞后于新兴材料（如高性能工程塑料、生物基聚合物）的测试需求。
- **IR 与 Raman 互补的实际边界**：理论上互补，但 Raman 的荧光干扰与 IR 的强吸收截断会限制实际应用。
- **ASTM 标准的代表性问题**：标准方法给出的是可比性，不等于对真实服役工况的预测力。

## Hygiene Implication 卫材关联

- **PP 无纺布与芯体材料的出厂检验依赖本章标准体系**：原文指出工业测试用于满足产品规格与公众保护，包括 stress–strain 关系、flex life、tensile strength 等（line 15-16）。报告 RIA 卡片列举的 ASTM D-638（拉伸）、D-790（弯曲）、D-543（化学耐性）属**卡片转述，非本页所引原句直接给出**，标注 [待验证]；可确定的是 ASTM D-543 与 PWC 判据来自原书 §4.5。
- **乙烯基骨架的耐化学性 = 卫材选材基石**：PE/PP 属 vinyl 型聚合物，对极性与非极性液体、酸碱均表现中等至良好稳定性，因为它们的主链是 C–C 键、不易受极性试剂攻击。这正是 PP/PE 无纺布能在尿液、经血、清洁剂的复杂化学环境中服役的化学依据。
- **SAP 的热与结构表征**：SAP 的交联度影响 Tg（DSC 可测），凝胶的热稳定性与无机残余/填料含量（TGA 可测）。ATR-FTIR 可直接测 SAP 颗粒表面羧基/羧酸盐转化与交联剂残留，无需制样。
- **表面化学与粘合**：ESCA/XPS 与 ATR 是分析 PP 无纺布表面处理（等离子、亲水整理剂）与热熔胶界面化学的必备手段——粘合失败几乎总是界面化学问题。
- **非破坏性测试优先**：在线质量控制（克重、厚度、透气、颜色、IR 鉴别）应尽量选用非破坏性方法，避免测试本身改变样品化学结构或历史。

## Related Sources 关联来源

- [[Seymour Polymer Chemistry Ch03 Molecular Weight of Polymers]]
- [[Seymour Polymer Chemistry Ch05 Rheology and Physical Tests]]
- [[Seymour Polymer Chemistry Ch06 Step-Reaction Polymerization]]
- [[Absorbent Product Testing]]
- [[Absorbent System Overview（K-C 吸收系统概览培训·2021-02）]]

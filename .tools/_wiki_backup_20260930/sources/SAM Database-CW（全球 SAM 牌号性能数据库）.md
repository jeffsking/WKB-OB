---
type: source
title: "SAM Database-CW（全球 SAM 牌号性能数据库）"
source_type: 内部材料数据库（Excel）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/SAM/SAM Database-CW.xlsx.md
original_link: ""
date_published: "[待验证] 2025（sheet 名标注 01082025，日期格式歧义）"
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Three sheets: a global grade-level performance table (CRC / AUL / GBP / Vortex / 30–50 mesh %), a 'Global v2' supplier×grade view with country usage and supplier strength/opportunity notes, and a 'KCC-YJ' view with K-C usage flags (三张表：全球牌号性能表、全球 v2 供应商×牌号视图、KCC-YJ 视图含 K-C 使用标记)"
  - "AUL is measured at 0.9 psi, except Nuoer grades at 0.7 psi — the two pressure conditions are NOT interchangeable and are recorded in one column（AUL 测试压力：通用 0.9 psi，诺尔牌号为 0.7 psi，两者不可互换，却同列记录）"
  - "GBP is recorded in Darcy and spans 0–96 Darcy across grades; several high-capacity grades have GBP at or near 0–3 Darcy, i.e. high CRC/low permeability（GBP 以 Darcy 记录，跨度 0–96；多个高容量牌号 GBP 仅 0–3 Darcy，即高容量低渗透）"
  - "Data provenance is mixed and labelled: TDS, spec, SAM lab, CaiShan, supplier COA, targets — values are NOT all measured under one method or by one party（数据出处混杂并已标注：TDS / spec / SAM lab / CaiShan / COA / targets，非同一方法同一方测得）"
  - "'Global v2' records supply-risk notes per supplier: LG faces Anti-Dumping Tax; Evonik is 'being acquired by ICIG'; Nippon Shokubai is 'challenging as they are primary supplier for P&G'; Formosa is flagged 'Unreliable (OTIF)'（逐供应商的供应风险注记：LG 反倾销税；Evonik 被 ICIG 收购中；日本触媒因是宝洁主供而难谈；台塑 OTIF 不可靠）"
  - "Several grades carry 'Risk of leakage/rewet for SAM/fluff core' or 'Increased add-on required' as the implication to US products — i.e. substituting these grades into an existing SAM/fluff core is not drop-in（多个牌号标注「对 SAM/浆芯体存在渗漏/回渗风险」或「需提高添加量」——即非直接替换）"
  - "Feedstock is almost entirely petro-based; the only bio feedstock entry is Evonik 3930 (CRC 24, AUL 12, GBP 0, Vortex 107, 2016, Evonik COA)（原料几乎全为石油基；唯一生物基条目为 Evonik 3930）"
  - "A 'Cost/MT' column exists in the Global v2 sheet but is EMPTY in the extracted data — no cost data is available from this source（Global v2 表存在 Cost/MT 列，但抽取数据中为空——本源无成本数据）"
  - "Safety clearance and RMS identifiers appear for a few grades only (e.g. Nuoer NR511N IPSCS-RM-2024-00958 / RMS 42124562; Satellite CR-730 IPSCS-RM-2024-00346; Wanhua WH700C IPSCS-RM-2025-01025)（安全 clearance 与 RMS 编号仅少数牌号有）"
pages_linked: ["[[SAP性能指标（CRC AUL GBP Vortex）]]", "[[SAM Testing Methods（超级吸水材料测试方法）]]", "[[巴斯夫欧洲公司（BASF SE）]]", "[[诺尔（Nuoer）]]", "[[Nippon Shokubai（日本触媒）]]", "[[Satellite Chemical（卫星化学）]]", "[[Sumitomo Seika（住友精化）]]", "[[LG Chem（LG 化学）]]", "[[宜兴丹森科技有限公司]]", "[[Evonik（赢创）]]", "[[Formosa Plastics（台塑）]]", "[[Wanhua Chemical（万华化学）]]", "[[IPC BCC OI Portfolio（开放创新项目组合）]]"]
---

# SAM Database-CW（全球 SAM 牌号性能数据库）

> 一句话定位：一份**按供应商 × 牌号组织的全球 SAM（Superabsorbent Material）性能数据库**，三张表分别给出**牌号级四指标（CRC / AUL / GBP / Vortex）**、**全球在用品种与供应商强弱项**、**K-C 使用标记**。（中文：选型用的"牌号字典 + 供应格局注记"，不是实验报告。）

## 原文要点 Original Key Points

### Sheet 1 — `SAM database 01082025-Global`（牌号级性能表）

**列结构 / Column structure**：`Vendor | Grade name | CRC (g/g) | AUL, 0.9 psi / 0.7 psi for Nuoer (g/g) | GBP (Darcy) | Vortex Time (s) | 30–50 目 (%) | Year | Source | Feedstock | Legacy / current | Safety Clearance | SAP specification Code | RMS Number`

> ⚠️ **单位与条件警示（2026-09-29）**：**AUL 列的压力条件不统一**——通用 0.9 psi，**诺尔牌号为 0.7 psi**，两者同列记录但**不可互换**。GBP 单位为 **Darcy**（与库内 [[SAP性能指标（CRC AUL GBP Vortex）]] 记录的 10⁻⁷ cm³·s/g 口径**不可换算**）。

**覆盖的供应商与牌号数（源文统计）**：BASF（约 24 个牌号，含 Saviva 系列）、Danson（12）、Evonik（9）、Formosa（10）、LG（16）、Nippon Shokubai（8）、Nuoer（7）、Satellite（12，含 CR-630 的重复行）、SDP（8，含 Sandia 系列）、Sumitomo（4）、WanHua（4）。

**关键取值区间（照录，不做推断）**：

| Metric 指标 | Observed range 表中出现的范围 | 备注 |
|---|---|---|
| CRC（g/g） | 24（Evonik 3930）– 47（SDP N14） | 主流区间约 30–40 |
| AUL（g/g） | 8（BASF 4230、LG 506ND、Satellite CR-630 等）– 31（Satellite CR-710） | **注意压力条件不同** |
| GBP（Darcy） | 0（多个牌号）– 96（Sandia SG-N212，KCC-YJ 表） | 高容量牌号普遍偏低（0–3） |
| Vortex（s） | 18（LG DS 701FP 类）– 120（BASF 7085） | 越低越快 |
| 30–50 目（%） | 49–89（仅诺尔部分牌号有值） | 其余为空 |

**出处标签 / Provenance labels**：`TDS`、`spec`、`SAM lab`、`CaiShan`、`Evonik COA`、`LG COA`、`targets`、`CaiShan`。
**Legacy / current**：源文逐行标注；例如 BASF 5400/8760/9410/9630/9700/9807/9810/9900、Evonik 5600/5630/9300/9394/9500、LG GS4700/LK208PN/LK3800/LK501、SDP 全系、Danson 228x2 标记为 **Legacy**。

> 中文注解：**同一数据库内混有供应商自述（TDS/COA）、第三方/内部实验室（SAM lab、CaiShan）与设计目标值（targets）**——因此跨行比较时**必须连同 Source 列一起读**，不能只比数字。

### Sheet 2 — `Global v2`（全球在用品种 × 供应商格局）

**列结构**：`Supplier | SAM Grade | Country/Region Used | CRC | AUL | GBP | Vortex | SAM type | Implications to US Products | Applicable Products | Supplier Strengths | Supplier Opportunities | Cost/MT`

**在用品种与覆盖范围（摘录）**：

| Supplier | Grade | Countries / Regions 使用地区 | SAM type | Applicable products 适用产品 |
|---|---|---|---|---|
| LG | LK804ND | USA, China, Korea, Vietnam, Russia, South Africa, Israel, Czech, Mexico | Balanced | Huggies / Pull-Ups / Goodnites / Depend / UbK |
| Evonik | 5660 | USA | Balanced | Huggies / Pull-Ups / Goodnites / Depend / UbK / Poise UT |
| Evonik | Max2000 | USA, Czech, Israel, Mexico | High Capacity | Guards for Men / Poise Originals |
| Evonik | 4400 | USA | Mach 4 | Depend |
| BASF | T5520 | USA | Balanced | Depend / Huggies / Pull-Ups / Goodnites |
| BASF | T5400 | Mexico, USA（进口产品） | Balanced | Huggies（through KCM） |
| Nuoer | 511 | China, Russia, South Africa, Israel, Peru；**to qualify in USA** | Balanced | Huggies / Pull-Ups / Goodnites / Depend / Poise* / UbK |
| Nuoer | N8 | **In discussion for Czech and Israel** | specs TBD | — |
| Danson | 83K / 6052 / 228x3 / 228x5 | China；China/Malaysia/Indonesia；India/Mexico；— | Balanced / High Capacity | — / — / -Poise / — |
| Satellite | CR740 / CR630 | China；Indonesia/LAO | Balanced / High Capacity | — |
| Formosa | BC583FAK / BC283GAN / BC283HA | Taiwan；Mexico；China/Indonesia/India | Balanced / High Capacity | — |
| Sumitomo | HP600 / SA60S | Korea；Taiwan/Vietnam | High Capacity | — |
| Nippon Shokubai | CAW | Indonesia | High Capacity | — |

**"Implications to US Products" 列的四种注记（照录）**：

| 注记 | 出现的牌号 |
|---|---|
| **Current Grade / Current** | LG LK804ND、Evonik 5660/Max2000/4400、BASF T5520/T5400 |
| **Risk of leakage/rewet for SAM/fluff core** | Nuoer 511、Danson 83K |
| **Risk of increased leakage/rewet** | Danson 6052/228x3/228x5、Satellite CR630、Nippon Shokubai CAW |
| **Increased add-on required / Requires Reformulation** | Danson 6052、Formosa BC283HA、Sumitomo HP600/SA60S、Formosa BC583FAK/BC283GAN |

> 中文：**这张表的核心价值不在性能数字，而在"每个牌号对现有 SAM/浆芯体意味着什么"**——多数的非在用品种都带**渗漏/回渗风险**或**需提高添加量/重新配方**的注记，说明**牌号替换不是 drop-in**。

**Supplier Strengths / Opportunities 摘录**：

| Supplier | Strengths 强项 | Opportunities / Risks 机会与风险 |
|---|---|---|
| LG | Innovation；Prompt Support；Global Supply；**Vertically Integrated for Acrylic Acid** | **Anti-Dumping Tax**；Quality |
| Evonik | Quality；Breakthrough Innovation；CIRRUS Consortium | **Cost**；**Being acquired by ICIG** |
| BASF | Innovation；Vertically Integrated for Acrylic Acid；Stable Supply | SAM build-up on assets |
| Nuoer | **Cost**；Rapidly Expanding Capacity and Capability | Innovation |
| Danson | Cost | Innovation |
| Satellite | Cost | Quality；**Supply Chain (OTIF)**；Innovation |
| Formosa | Cost；Has sustainable option | Quality；**Unreliable (OTIF)**；Innovation |
| Sumitomo | Quality | Cost |
| **Nippon Shokubai** | — | **Challenging as they are primary supplier for P&G** |

### Sheet 3 — `KCC-YJ`（K-C 使用标记视图）

**列结构**：`SAM grade(s) | Indicate if CRC/AUL/GBP/Vortex performance are K-C or supplier result | CRC | AUL | GBP | Vortex | Shelf life (Months) | 是否KCC使用`

**"是否 K-C 结果" 标记**：绝大多数为 **Supplier result**；标注为 **K-C result** 的仅 **Satellite 740**、**Sandia SG-N210**、**Sandia KC-990LN** 三条。

**K-C 使用标记摘录**：

| Supplier | Grade | K-C 使用标记（原文） |
|---|---|---|
| BASF | 7059 | OEM-T5 |
| Danson | 6052 / 6052OC / 83K | BCC / AC / BCC |
| Danson | 228X2 / 228X3 / 228X5 | **BCC 南京曾经供应** / **BCC 印度正在供应** / **BCC 南美曾经供应** |
| Formosa | BC283HA / BC283FAN | FC / AC |
| LG | LK810ND | 国内市面上的芯体牌号;9800 |
| LG | LK804ND / LK861ND | **BCC — 离线复合芯体** / BCC |
| LG | LK-901ND | **新开发的牌号 for KCNA RSR HUT 完成** |
| Nuoer | NR 511 / NR N8 | BCC / EMEA |
| Satellite | 740 | BCC |
| Wanhua | WHS 700 / WHS 1200 | 墨西哥 / **釜式** |

> 中文：这张表把"牌号"与"**在哪个法人/区域实际用过**"连起来——是本库判断**供应连续性**与**区域切换可行性**的关键证据。

> 🔴 **manual_review（2026-09-29）**：本源为**内部材料数据库**，含① 逐牌号性能（含供应商自述与内部实测混合）、② **供应商商务注记**（LG 反倾销税、Evonik 被 ICIG 收购、日本触媒为宝洁主供、台塑/卫星 OTIF 不可靠）、③ **K-C 各区域实际使用牌号与法人**（BCC/AC/FC、南京/印度/南美、OEM-T5、离线复合芯体）。依 AGENTS.md §5：本页**只记要点与相对关系**，**不落全量牌号价格与合同条款**；`Cost/MT` 列在抽取数据中**为空**，本页**无任何成本数据**；安全 clearance（IPSCS-RM）与 RMS 编号属内部标识，仅记存在与举例，**不展开**。

## 与库内页面的关系 Relations

- 指标口径：[[SAP性能指标（CRC AUL GBP Vortex）]]、[[SAM Testing Methods（超级吸水材料测试方法）]]
- 供应方：[[巴斯夫欧洲公司（BASF SE）]]、[[诺尔（Nuoer）]]、[[Nippon Shokubai（日本触媒）]]、[[Satellite Chemical（卫星化学）]]、[[Sumitomo Seika（住友精化）]]、[[LG Chem（LG 化学）]]、[[宜兴丹森科技有限公司]]、[[Evonik（赢创）]]、[[Formosa Plastics（台塑）]]、[[Wanhua Chemical（万华化学）]]
- 项目组合：[[IPC BCC OI Portfolio（开放创新项目组合）]]

## 存疑 / 待人工确认 Open Questions

1. **日期歧义**：sheet 名为 `SAM database 01082025-Global`，`01082025` 可能为 2025-01-08 或 2025-08-01，**不作换算**，`date_published` 标 `[待验证]`。
2. **AUL 压力条件混列**：通用 0.9 psi 与诺尔 0.7 psi 同列——**跨供应商比较 AUL 前必须先统一压力条件**，本页不代为换算。
3. **同一牌号重复行**：如 Satellite CR-630 出现两行（CRC 均 43、AUL 均 8、GBP 均 2，Vortex 45 vs 34），CR-640 两行（CRC 30 vs 35）、CR-730 两行、CR-740 两行（GBP 18 vs 28）。**重复原因未说明**（不同批次/不同来源），本页照录**不合并、不取均值**。
4. **同一牌号跨表数值不一致**：例如 Nuoer NR511 在 Sheet 1 为 CRC 31 / AUL 15 / GBP 25 / Vortex 33，在 `Global v2` 为 CRC 31 / AUL 14.7 / GBP 35 / Vortex 33，在 `KCC-YJ` 为 CRC 31.5 / AUL 18.2 / GBP 26 / Vortex 28。**三表口径不一致，源文未给解释**——本页照录，**不裁决、不取代表值**。（中文：GBP 25 / 35 / 26 三值并存尤其影响"高 GBP"判断。）
5. **`Cost/MT` 列为空**：本库最关心的成本维度在本源**无数据**，不得以其他来源的单价填补。
6. **Evonik "being acquired by ICIG"、LG "Anti-Dumping Tax"** 等注记**未标日期**，其时效性与当前状态**需人工核验**。

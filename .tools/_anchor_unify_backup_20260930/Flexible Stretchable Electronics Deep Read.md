---
type: source
title: "Flexible Stretchable Electronics Deep Read"
source_type: book-index
author: "Prof. dr. ir. Jan Vanfleteren"
edition: ""
publisher: "Centre for Microsystems Technology (CMST), imec & Ghent University, Ghent, Belgium (deep-read annotation dated 2026-08-23)"
year: 0
isbn: ""
original_language: "EN"
source_path: RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Flexible_Stretchable_Electronics_DeepRead.md
date_published: 0
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
summary_cn: "对该 imec 柔性/可拉伸电子文章的第二手精读笔记（2026-08-23 生成，11 节），展开 UTCP 超薄芯片封装与蛇形互连可拉伸电路的工艺参数、材料体系与应用，但其中应变公式、可靠性测试框架、产业对比等内容在原文件中并无依据。"
key_claims:
  - "The deep read restates the two imec technologies: UTCP (bare Si thinned to 20–30 μm, spin-on polyimide embedding, fan-out metallisation, total package < 100 μm) and stretchable circuits (component islands + meander-shaped thin-film or PCB copper wiring embedded in PDMS or PU)."
  - "UTCP is benchmarked qualitatively against traditional BGA packages at 1–3 mm thickness, positioning it as extreme miniaturisation rather than incremental thinning."
  - "Process constraints flagged: polyimide cure thermal budget ~350–400 °C must be compatible with already-processed chips; back-side thinning to 20–30 μm is aggressive (grinding + CMP); fan-out adds TSV/RDL patterning complexity."
  - "Meander (serpentine) geometry, not material elasticity, is identified as the strain-relief mechanism protecting brittle metal interconnects — this is the central design rule of the stretchable route. [derived by the deep-read author; not verbatim source]"
  - "A 15-LED stretchable circuit demonstrated without electrical open-circuit under 'extreme deformation' is treated as a systems-level (not single-interconnect) proof."
  - "The source's own Quality Notes concede that specific reliability numbers (cycles to failure, max strain %) are referenced but NOT extractable from the text; images likely carry the process flow and test results."
tags: ["source/book", "flexible electronics", "stretchable electronics", "UTCP", "meander interconnect", "PDMS", "polyurethane", "polyimide", "deep-read", "second-hand summary"]
tags_zh: ["柔性电子", "可拉伸电子", "超薄芯片封装", "蛇形互连", "PDMS", "聚氨酯", "聚酰亚胺", "二次精读笔记"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Flexible and Stretchable Electronics]]", "[[Flexible Stretchable Electronics (imec)]]", "[[Smart Textiles & Wearables]]", "[[Smart Sensing Diaper Technology Research Report（智能感知纸尿裤技术研究报告 · 2026-04）]]"]
---

# Flexible Stretchable Electronics Deep Read

*Prof. dr. ir. Jan Vanfleteren (imec / Ghent University) — second-hand deep-reading note dated 2026-08-23 over `Flexible_and_Stretchable_Electronics.pdf`*

> ⚠️ **Second-hand document 二次文档 — read this first 请先读此说明**: this root file is **not the original paper**. It is an 11-section "Full-Text Deep Reading" note generated on 2026-08-23 against a source consisting of roughly one page of abstract. Consequently:
> - Content that is **traceable to the original** (UTCP parameters, meander architecture, PDMS/PU embedding, 15-LED demo, the three market drivers) is reported below as fact.
> - Content that the deep-read author **elaborated beyond the source** is flagged inline as `[derived]` — notably the meander strain-relief formula and its variables (§4.4), the five-item reliability test framework (§6, which the note itself admits is "implied" not stated), the BGA 1–3 mm comparison, the polyimide cure window ~350–400 °C, the Cu/Au yield-strain figures (~0.2–0.5 % for Cu, ~0.1 % for Au), the −40 °C to +125 °C thermal-cycling and 85 °C/85 % RH humidity figures, the CMOS-compatibility judgement, and the industry-context section naming IBM/John Rogers, Samsung and Apple.
> - These derived items **must not be cited as source-supported data without verification against the imec original**. Per AGENTS.md §2.3 (`preview/DeepRead` 节选需核验标注), this page is therefore marked `manual_review`.
> （中文：本文件为 AI 生成的精读笔记而非原文，标注 [derived] 的内容在原文件中无法追溯，引用前须回原文核验。）

## Book Metadata 书籍元数据

| Field 项 | Value 值 |
|---|---|
| Author 作者 | Prof. dr. ir. Jan Vanfleteren |
| Affiliation 机构 | Centre for Microsystems Technology (CMST), imec & Ghent University, Technology Park 914, B-9052 Ghent, Belgium |
| Underlying source 底层原文 | `Flexible_and_Stretchable_Electronics.pdf` (Conference Paper / Technical Presentation, per the note's header) |
| Deep-read date 精读日期 | 2026-08-23 (as stated in the note header) |
| Edition 版次 | 未标注 (not stated) |
| Publisher 出版社 | imec / Ghent University (CMST) |
| Year 年份 | 未标注 (not stated) |
| ISBN | 未标注 (not stated) |
| Original Language 原文语种 | EN |
| Credibility 可信度 | 中 — content is one derivative step removed from the primary text; see the warning block above |
| Relevance 相关性 | LOW 低 for hygiene materials (see below) |

## Scope and Structure 范围与结构

The note is organised in 11 numbered sections (本笔记为 11 节结构，此处作为索引概括):

| § | Section 节 | Content in one line 一行概要 |
|---|---|---|
| 1 | Executive Summary 摘要 | Two complementary technologies enabling industrial production of randomly deformable circuits |
| 2 | Motivation & Market Context 动机与市场 | Quote of the rigid-PCB/2.5D–3D framing; three drivers table (comfort & ergonomics / design & aesthetics / ecological) |
| 3 | UTCP 超薄芯片封装 | Concept, 5-row process-parameter table, four advantages, four process cautions |
| 4 | Stretchable Circuits 可拉伸电路 | Concept, ASCII architecture diagram, materials-system table, meander strain-relief principle |
| 5 | Application Demo 应用演示 | 15-LED stretchable circuit; before/after deformation states |
| 6 | Reliability Data 可靠性数据 | Admits numbers are not extractable; lists an implied five-test framework |
| 7 | Technology Comparison 技术对比 | 7-row UTCP vs stretchable comparison across benefit, substrate, enabler, thickness, flexibility type, max deformation, industrial readiness |
| 8 | Applications & Impact 应用影响 | Four UTCP applications; five stretchable applications |
| 9 | Broader Industry Context 产业背景 | Names IBM/John Rogers, Samsung flex-AMOLED, Apple flexible PCBs; three claimed differentiators of the imec approach |
| 10 | Key Takeaways 要点 | Six bullets |
| 11 | Quality Notes 质量说明 | Five ⚠️ caveats — conference paper, missing numbers, diagrams probably image-only, no competitive comparison, descriptive rather than analytical |

No chapter pages exist; this is the only page linked from this source_path.
（中文：无章节页，本 source_path 仅对应本页。）

## Key Findings 关键发现

**Traceable to the original paper 可追溯至原文**

- Demand is shifting from flat rigid PCB assembly toward 2.5D (free-form surface) and full 3D electronics; three named drivers are **comfort/ergonomics** (wearable, implantable), **design/aesthetics** (2.5D/3D light sources) and **ecology** (material efficiency, CO₂ reduction in automotive).
- **UTCP**: bare Si (or other inorganic-semiconductor) chips thinned to **20–30 μm**, stacked spin-on polyimide embedding, fan-out metallisation → total package thickness **< 100 μm**.
- **Stretchable route**: individual components or component islands interconnected by **meander-shaped thin-film or PCB-based metal wiring**, embedded in **PDMS (silicone rubber) or PU (polyurethane)**.
- The structural decomposition is explicit — **component islands** (rigid active parts on discrete rigid patches) + **meander traces** + **elastic embedding**; two wiring variants are named (thin-film deposited metal, PCB copper).
- **Demonstrator**: a 15-LED stretchable circuit survives "extreme deformation" with no electrical open-circuit — framed as a systems-level rather than single-interconnect proof.
- The source itself promises process flow details, reliability data and applications.

**Flagged as derived, not source-supported 标注为推导，原文无依据**

- Meander strain-relief relation ε_metal = ε_macroscopic × 1/(1 + h·w/(t·L_meander)) with h = amplitude, w = trace width, t = trace thickness, L_meander = wavelength. `[derived]`
- Claimed metal yield strains (~0.2–0.5 % Cu, ~0.1 % Au) as the reason meanders are required. `[derived]`
- Reliability test framework: bend cycling at various radii, % strain vs resistance change, −40 °C to +125 °C thermal cycling, 85 °C/85 % RH accelerated ageing, drop/mechanical shock. `[derived]` — the note itself labels this as "implied".
- UTCP vs BGA at 1–3 mm; polyimide cure thermal budget ~350–400 °C; thinning typically by mechanical grinding + CMP; fan-out via TSV/RDL; UTCP "higher industrial readiness, CMOS-compatible" vs stretchable "development stage". `[derived]`
- Industry-context claims naming IBM/John Rogers, Samsung and Apple, and the three imec differentiators including "PDMS/PU embedding (medical-grade biocompatibility potential)". `[derived]`
- The note's own §11 concedes: **no reliability numbers extractable**, diagrams likely image-only, no comparison against competing technologies, descriptive rather than analytical.

**Consistent across §7 comparison table**：UTCP delivers **bending** flexibility limited by polyimide; the meander route delivers **stretching + bending** limited by meander geometry. The two are complementary, not competing.

## Relevance to Hygiene R&D 与卫材研发的关联

**Rating 评级: LOW 低.**

Stated plainly 直说:

- **Nothing here touches our materials主线**: no ultra-thin absorbent core, fluff pulp, SAP, ES/PE-PP bicomponent fibre, nonwoven bonding, adhesive, or chromic-ink content. The named materials — Si, spin-on polyimide, PDMS, PU — do not appear in disposable hygiene constructions.
- **One architectural idea transfers, weakly**: `rigid island + compliant geometry + soft elastic matrix` is the same strain-management principle behind elastic-thread and elastic-laminate design for waistbands and cuffs, where stiff elements must survive large repeated strain in a soft assembly. But this source carries **no quantitative strain data**, and the numbers that would make it useful are precisely the `[derived]` ones — so it cannot be used for design.
- **Surface relevance only to the smart-diaper sensing track**: the UTCP form factor (< 100 μm package) is the reason a rigid sensor die could in principle sit inside a thin absorbent article without comfort penalty. That connection is not developed anywhere in this file and belongs to [[Smart Sensing Diaper Technology Research Report（智能感知纸尿裤技术研究报告 · 2026-04）]] instead.
- **PU appears as an elastic embedding matrix** and polyurethane elastomers do sit in our adjacency (elastic filaments/films), but this file offers no formulation or property data.
- **Recommendation 建议**: treat as background/horizon-scanning only. No concept or entity pages should be derived. If the plastic strain-accommodation principle is ever needed quantitatively, go to a primary mechanics source, not to this note.

## Related Sources 关联来源

- [[Flexible and Stretchable Electronics]] — 同一底层文章的另一个 root 文件（仅摘要一页），本页的交叉对照对象；两者内容重叠，本页多出的部分多为 [derived]。
- [[Flexible Stretchable Electronics (imec)]] — 同源主题的第三个已编译 source 页（来自 `Ebook Extract/Smart_Textiles_Wearables_拆解/`），三者构成同一材料的重复收录，需避免重复引用。
- [[Smart Textiles & Wearables]] — 上层框架页：智能纺织品与可穿戴电子的产业背景，UTCP/蛇形互连属其电子集成路径之一。
- [[Smart Sensing Diaper Technology Research Report（智能感知纸尿裤技术研究报告 · 2026-04）]] — 本库唯一将柔性电子落到纸尿裤的相关资料，若要追 validity of sensing 方向应从此处入手。

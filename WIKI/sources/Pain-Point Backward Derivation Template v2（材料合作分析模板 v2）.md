---
type: source
title: "Pain-Point Backward Derivation Template v2（材料合作分析模板 v2）"
source_type: 内部模板
source_path: RAW/ima_sync/个人知识库/WKB/Projects/BNC/05_材料合作分析模板_v2_痛点倒推法.md.md
original_link: ""
date_published: 2026-09-05
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "Template v2 replaces the old \"material performance → possible application\" forward derivation with \"product pain point → material role → delivery form → process route\"（模板 v2 用「产品痛点 → 材料角色 → 交付形态 → 工艺路线」四格倒推，替代旧的「材料性能 → 可能应用」正推）"
  - "The old template's classifying axis — \"what does BNC replace\" (topsheet / ADL / SAP / fluff) — structurally excludes intermediate and carrier roles; that omission (not a technical failure) is what hid the PEG dry-granule route（旧模板按「BNC 替代谁」分类，天然漏掉中间体/载体角色，这才是 PEG 干颗粒方案被漏掉的真实原因）"
  - "Six-role library: end-use material / reinforcer / synergist / intermediate or placeholder / functional carrier / structural component（六角色库：终端材料 / 增强剂 / 增效剂 / 中间体·占位剂 / 功能载体 / 结构组分）"
  - "Delivery form is the decisive gate: dry powder / granule or masterbatch / re-wettable dry granule / wet film or suspension / aerogel or film / foamed preform（交付形态是决定能否上车的格子）"
  - "Three self-check rules: if a scheme can only be phrased as \"replacing X as an end material\", return to Step 2; if the delivery form cannot be stated, return to Step 3; if the process route has no position in the genealogy / constants table, mark it \"process gap\" and validate before assuming feasible"
pages_linked: ["[[Pain-Point Backward Derivation（痛点倒推法）]]", "[[BNC Application Red Line（BNC 应用红线）]]", "[[BNC-PEG 母粒（干态可复水中介体）]]", "[[BNC Application Red Line Revision 20260905（BNC 应用红线修订说明）]]", "[[海南拜瑞科]]", "[[水凝胶脱水干燥工艺族谱]]", "[[智能尿裤功能层]]"]
---

# Pain-Point Backward Derivation Template v2（材料合作分析模板 v2）

## One-Line Positioning 一句话定位

This is the **standard analysis template for vendor visits and project initiation**, built backwards from the BNC × Baikerui（拜科瑞）case of 2026-09. Its purpose in this library is methodological: it defines *how* a new material is allowed to enter the candidate set, which is the upstream gate on every concept and comparison page in the materials track.
（本页是**供应商拜访与项目立项的标准分析模板**，由 2026-09 的 BNC × 拜科瑞案例反推产出。在本库中的用途是方法论层面的：它定义了「新材料的候选集准入规则」，位于全部材料类概念页/对比页的上游。）

## Summary 摘要

1. The source states the design intent directly: the old template derived forward from **material performance → possible application**, which structurally misses non-substitution paths such as *intermediates* and *carriers*. Among the four Baikerui needs, three were reachable with the old template; only the **PEG dry-granule intermediate** could not surface — and only backward derivation exposes it.（旧模板「材料性能 → 可能应用」正推，天然漏掉中间体/载体这类非替代型路径；四个需求里三个旧模板也能想到，唯独 PEG 干颗粒中间体只有倒推才能浮出来。）
2. The revised chain is four cells: **product pain point → material role → delivery form → process route**（五步落地为 Step 1–5，其中 Step 1 痛点必须先于材料侧约束）。
3. Step 1 requires every pain point to carry a **quantified admission value**, cross-referenced to the plant constraint constants table (document 03 of the same BNC document set). Two worked examples are given: a 20 g wrap layer that cannot run on a high-speed machine (900 pads/min core wrapping; strength must be ≥8–9 N against a current 6–6.5 N, i.e. a −2 N gap, priority P0), and a wet-state material that cannot be dried in line (dry assembly is an iron rule on the 400 m/min line).（Step 1 要求每个痛点带量化准入值并对照《卫材产线约束常量表》03 号文档；示例：20 g 包覆层上不了高速机 —— 900 片/分芯体包覆、强力需 ≥8–9 N（现 6–6.5 N，缺 −2 N）、P0；湿态材料无法在线干燥 —— 干法线（先胶后 SAP）线速 400 m/min。）
4. Step 2 replaces "what does it replace" with a **six-role library**, and Step 3 forces a **delivery form** choice that is tightly bound to the process route — the source calls this "the key cell that decides whether it can get onto the line"（决定能否上车的关键格）。
5. Step 4 validates the route against four existing BNC document-set instruments: the drying-process genealogy（01）, the PEG/polyol × cellulose cross index（02）, the plant constraint constants table（03）, and the smart-diaper functional-layer patent map（04）plus FTO screening.
6. Step 5 is a one-sentence conclusion template — "in 〔delivery form〕, at 〔process step〕, as 〔role〕, solving 〔pain point〕 (quantified target: ____)" — plus three self-check rules.
7. Section III archives an old-vs-new mapping for the same four Baikerui directions, and Section IV records the follow-up actions (template fixation, cross-referencing the four companion documents, the red-line revision, and a "what did the old template miss" post-mortem after each visit).
8. Note on credibility: this is an internal methodology document with explicit worked cases and no external citations; it is traceable to the 2026-09 Baikerui case. It is treated as **medium**-credibility process knowledge, not as materials data.（可信度判断依据：内部方法论文档，有明确案例、无外部引用，可回溯至 2026-09 拜科瑞案例，故按「中」处理，不作为材料实测数据来源。）

## Extracted Data and Conclusions 提炼的数字与结论

| Item 项目 | Value / Conclusion 数值 / 结论 | Note 备注 |
|---|---|---|
| Old classification axis 旧分类轴 | "what does BNC replace": topsheet / ADL / SAP / fluff（面层/ADL/SAP/绒毛浆） | Replace-对象导向，一票误伤 |
| New classification axis 新分类轴 | material role × delivery form（BNC 在产品中的角色 × 交付形态） | 角色 = 终端材料 / 中间体 / 载体 / 增强剂 |
| Old criterion 旧判据 | "is it acceptable as a final material"（作为最终材料行不行） | 盲区：中间体/载体/平台类路径进不了候选集 |
| New criterion 新判据 | "in a given form, at a given process step, solving a given pain point"（以某形态、在某工序、解某痛点） | 中间体既不替代绒毛浆也不替代 SAP，天然入选 |
| Result of the old template 旧模板结果 | PEG intermediate scheme lost（漏掉 PEG 中间体方案） | 本次案例实证 |
| Result of the new template 新模板结果 | all four need-directions structurally expressible（四个需求方向全部可结构化表达） | — |
| Pain-point admission value, example 1 痛点准入值示例 1 | 900 pads/min core wrapping; strength ≥8–9 N vs current 6–6.5 N; gap −2 N; priority P0 | 20 g wrap layer, high-speed machine（对照《03 产线约束常量表》） |
| Pain-point admission value, example 2 痛点准入值示例 2 | dry assembly iron rule; line speed 400 m/min | wet-state material cannot be dried in line |
| Direction ①: hydrophobic dry powder（疏水干粉增强） | 8 gsm → 5 gsm; pain point = insufficient strength at low basis weight; role = reinforcer; form = hydrophobic dry powder; route = PP melt blending | 旧模板勉强可放（面层/无纺布增强） |
| Direction ②: foam grafting（发泡嫁接） | pain point = collapsed pores / strength; role = structural reinforcement; form = foamed preform; route = grafting modification | 旧模板勉强可放（ADL/缓冲） |
| Direction ③: SAP enhancement（SAP 增强） | pain point = gel blocking / cost; role = synergist / SAP spacer; form = granule or masterbatch; route = core layering | 旧模板被红线边缘化（SAP 替代） |
| Direction ④: PEG displacement intermediate（PEG 置换中间体） | pain point = wet-state hydrogel cannot run on a dry line; role = placeholder / re-wetting platform; form = re-wettable dry granule; route = displacement + extrusion + ambient drying | **only backward derivation surfaces this**；旧模板「无处安放」 |
| Role library size 角色库 | 6 roles（终端材料 / 增强剂 / 增效剂 / 中间体·占位剂 / 功能载体 / 结构组分） | Step 2 可多选 |
| Delivery-form table size 交付形态表 | 6 forms（干粉 / 颗粒·母粒 / 可复水干颗粒 / 湿膜·悬浮液 / 气凝胶·膜 / 发泡坯） | 每格附关键指标 |
| Self-check rules 三问自检 | 3 rules | 见 Step 5 |
| Post-mortem trigger 复盘升级触发 | 3 same-type omissions accumulated → upgrade the template | 每次拜访后填「旧模板漏了什么」一格 |

### Delivery-form gate table 交付形态准入格（Step 3 原文）

| Delivery form 交付形态 | Typical boarding route 工艺路线 | Gate parameters 准入参数（原文） |
|---|---|---|
| Dry powder, hydrophobic or hydrophilic（干粉（疏水/亲水）） | PP melt blending, powder scattering, sizing（PP 熔融混合、撒粉、上浆） | moisture report, heat resistance ≥ process window, particle size distribution, dust safety |
| Granule / masterbatch（颗粒/母粒） | blended with SAP, core layering（与 SAP 共混、芯体分层） | dry-state stability, particle size matched to SAP dosing |
| Re-wettable dry granule, PEG / polyol displacement（可复水干颗粒） | normal dry-line run, reactivated by urine（干法线正常走，遇尿复水激活） | PEG molecular-weight screening, displacement efficiency, measured re-wetting speed |
| Wet film / suspension（湿膜/悬浮液） | coating, transfer（涂布、转移） | solids content, compatibility with adhesive / SAP steps |
| Aerogel / film（气凝胶/膜） | lamination, wrapping（层压、包覆） | thickness window, compression recovery |
| Foamed preform（发泡坯） | forming and lamination（成型复合） | compression recovery, thickness target |

## Key Claims（key_claims）

- **The template's real product is a candidate-set admission rule, not a form.** —— 支撑页：[[Pain-Point Backward Derivation（痛点倒推法）]]
- **Role-based wording is what de-fuses the red line.** The role-library phrasing changes the red line to "not starting projects that replace fluff/SAP *as an end material*", so intermediate roles stop being collateral damage. —— 支撑页：[[BNC Application Red Line（BNC 应用红线）]]
- **Delivery form is the load-bearing cell.** Both the template and the PEG page converge on the same rule: a material route must be quoted and evaluated per delivery form. —— 支撑页：[[BNC-PEG 母粒（干态可复水中介体）]]
- **The four companion documents form a closed citation loop** with this template (Step 1 must cite 03; Step 4 must cite 01/02/04). —— 支撑页：[[水凝胶脱水干燥工艺族谱]]、[[BNC-PEG 母粒（干态可复水中介体）]]

## Related Pages 关联页面

- Concepts 概念：[[Pain-Point Backward Derivation（痛点倒推法）]]、[[BNC Application Red Line（BNC 应用红线）]]、[[BNC-PEG 母粒（干态可复水中介体）]]、[[水凝胶脱水干燥工艺族谱]]、[[智能尿裤功能层]]
- Entities 实体：[[海南拜瑞科]]（案例对象）
- Comparisons 对比：[[三类纳米纤维素对比（CNC、CNF、BNC）]]、[[BNC功能层嫁接可行性对比]]
- Sibling document 同族文档：[[BNC Application Red Line Revision 20260905（BNC 应用红线修订说明）]]

## Source 原文

- Local path 本地路径：`RAW/ima_sync/个人知识库/WKB/Projects/BNC/05_材料合作分析模板_v2_痛点倒推法.md.md`
- Original link 原文链接：（无；内部资料）
- Maintainer recorded in source 源文记录维护人：IMA；建议固化为供应商拜访／立项流程标准附件（源文 Section IV）

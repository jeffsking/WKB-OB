---
type: concept
title: "Pain-Point Backward Derivation（痛点倒推法）"
domain: [卫材研发, 实体与供应链]
status: growing
updated: 2026-09-29
tags: [痛点倒推法, 材料角色, 交付形态, 立项模板, 候选集准入, BNC]
---

# Pain-Point Backward Derivation（痛点倒推法）

> One-line definition 一句话定义：先锁定产线／产品的**量化痛点**，再倒推「材料在产品中的角色 → 交付形态 → 工艺路线」的项目分析方法；用"角色 × 形态"取代"材料替代谁"作为分类轴，使中间体、载体、增效剂这类**非替代型路径**不再被漏掉。（中文：本方法的产出不是一张材料清单，而是一条**候选集准入规则**。）

## Mechanism / Structure 机理 / 结构拆解

1. **Two classification axes, and only one of them admits intermediates.** The forward axis (old) asked "what performance does the material have → who can it replace", and classified by substitution object（面层／ADL／SAP／绒毛浆）. The backward axis (new) asks "what pain point does the line or product have → what role is needed → what form can board the line".（中文：正推以「替代谁」为分类轴；倒推以「角色 × 交付形态」为分类轴。）
2. **Why the forward axis fails structurally rather than accidentally**：a candidate that replaces nothing（e.g. a re-wettable dry granule that acts as a *placeholder*) has no substitution object to be classified under, so it cannot enter the candidate set at all — this is a representational failure, not a judgement error.（中文：替代对象为空 → 无类别可归 → 结构性地进不了候选集。）
3. **Role library (Step 2), six roles, multi-select allowed**：end-use material（终端材料：面层／ADL／芯体／包覆层）、reinforcer（增强剂：力学／抗脆断）、synergist（增效剂：SAP 增效、吸液动力学）、intermediate / placeholder（中间体·占位剂：干态可复水、载体）、functional carrier（功能载体：嫁接抗菌／传感／加热／变色）、structural component（结构组分：发泡坯、间隔层 spacer）。
4. **Delivery form is the decisive cell (Step 3)**，not a downstream detail: form is bound to the process route, and the route is what gets validated. Six forms are tabulated — dry powder（干粉）、granule / masterbatch（颗粒·母粒）、re-wettable dry granule（可复水干颗粒）、wet film / suspension（湿膜·悬浮液）、aerogel / film（气凝胶·膜）、foamed preform（发泡坯）。
5. **Pain points must be quantified before materials are discussed (Step 1)**，each with an admission value taken from the plant constraint constants table（《03 卫材产线约束常量表》）: line speed → web width → basis-weight-vs-strength → thickness → dry-state → price band → temperature window.
6. **Route validation is by instrument, not by intuition (Step 4)**：drying routes → drying-process genealogy（01）；chemical functional roles → PEG/polyol × cellulose cross index（02）；line admission → the constants table（03）；functionalisation space → the smart-diaper patent map（04）+ FTO screening.
7. **Self-limiting design**：if the route has no position in the genealogy or constants table, it must be filed as a **"process gap"** for validation rather than assumed feasible. There is also a stated escalation rule — three same-type omissions in the post-mortem log trigger a template upgrade.（中文：工艺空白必须明标立项验证，不得默认可行；同类遗漏累计三次即升级模板。）

## Key Parameter Table 关键参数表

| Parameter 参数 | Typical value / rule 典型值 / 规则 | Source 出处 |
|---|---|---|
| Analysis chain 分析链 | pain point → role → delivery form → process route | [[Pain-Point Backward Derivation Template v2（材料合作分析模板 v2）]] |
| Role library 角色库 | 6 roles（终端材料／增强剂／增效剂／中间体·占位剂／功能载体／结构组分） | 同上 |
| Delivery-form options 交付形态 | 6 forms（干粉／颗粒·母粒／可复水干颗粒／湿膜·悬浮液／气凝胶·膜／发泡坯） | 同上 |
| Pain-point admission value, ex.1 准入值示例 1 | 900 pads/min core wrapping；strength ≥8–9 N vs current 6–6.5 N；gap −2 N；P0 | 同上 |
| Pain-point admission value, ex.2 准入值示例 2 | dry assembly iron rule；line speed 400 m/min | 同上 |
| Low-basis-weight target (case ①) 案例①目标 | 8 gsm → 5 gsm | 同上 |
| Escalation trigger 升级触发 | 3 same-type omissions → upgrade template | 同上 |
| Companion instruments 配套工具 | 4 documents（01 族谱 / 02 交叉索引 / 03 常量表 / 04 专利地图） | 同上 |

> ⚠️ **No unsourced parameters 禁止无来源参数**：this page's numbers all come from [[Pain-Point Backward Derivation Template v2（材料合作分析模板 v2）]]. The constants table（03）itself is **not yet compiled into this library**, so its numeric admission values cannot be cited here — mark `[待验证]`.
> （本页数字均来自该模板页；《03 卫材产线约束常量表》本体**尚未编译入库**，其数值化准入值本库无法引用，标 `[待验证]`。）

## Adjacent Concepts 相邻概念

- Governing rule 治理规则：[[BNC Application Red Line（BNC 应用红线）]]
- The route this method was built to rescue 本方法为救回该路线而建：[[BNC-PEG 母粒（干态可复水中介体）]]、[[水凝胶脱水干燥工艺族谱]]
- Application targets 应用落点：[[智能尿裤功能层]]、[[分区密度设计]]、[[ADL（导流层）]]
- Material family 材料家族：[[纳米纤维素（CNC、CNF、BNC）]]、[[细菌纳米纤维素]]
- Comparisons 对比：[[BNC功能层嫁接可行性对比]]、[[三类纳米纤维素对比（CNC、CNF、BNC）]]

## Lessons Learned 经验教训

> ✅ Verification（2026-09-29，source [[Pain-Point Backward Derivation Template v2（材料合作分析模板 v2）]]、[[BNC Application Red Line Revision 20260905（BNC 应用红线修订说明）]]）：两份同族文档在同一因果上互证——**漏掉 PEG 中间体不是判断失误，而是分类轴无法表达该路线**；修分类轴（角色化表述）与修红线（终端材料身份）是同一问题的两次修正。（中文：两条独立文档互证同一根因，本页「结构性准入失败」表述与来源一致。）

- **Lesson 1（先问形态）**：把「材料性能」当起点会天然漏掉中间体；把「交付形态」当起点才会先问「能不能上车」。立项书若写不出交付形态，应回到 Step 3 而不是继续论证性能。
- **Lesson 2（角色化表述可以防误伤）**：同一份 BNC 材料，写成「替代绒毛浆」被拦，写成「中间体／载体」放行——**表述方式直接决定候选集资格**，故角色库与红线必须成对维护。
- **Lesson 3（三条自检须真的执行）**：三问自检里最容易被跳过的是第三条——工艺路线在族谱／常量表无位置时，必须标「工艺空白」立项验证，**不得默认可行**。
- **待补 `[待验证]`**：《03 卫材产线约束常量表》《01 脱水干燥工艺族谱》《02 PEG 多元醇 × 纤维素交叉索引》《04 智能尿裤功能层专利地图》四份配套文档在本库内的**入库状态与本页 Step 1／Step 4 的引用完整性**；模板 v2 的下游采纳记录（哪些立项／拜访实际使用了本模板）。

## Sources 来源

- [[Pain-Point Backward Derivation Template v2（材料合作分析模板 v2）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/BNC/05_材料合作分析模板_v2_痛点倒推法.md.md`
- [[BNC Application Red Line Revision 20260905（BNC 应用红线修订说明）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/BNC/06_BNC应用红线修订说明_20260905.md.md`

## Related Sources 关联来源

- [[BNC Application Red Line Revision 20260905（BNC 应用红线修订说明）]]
- [[Pain-Point Backward Derivation Template v2（材料合作分析模板 v2）]]

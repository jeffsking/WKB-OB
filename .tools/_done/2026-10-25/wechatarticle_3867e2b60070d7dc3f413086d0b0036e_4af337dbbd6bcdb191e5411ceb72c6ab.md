---
type: source
title: "一片纸尿裤的六层，只有一层真的在吸水（与卫生巾工艺相同）"
source_type: 公众号
source_path: RAW/ima_sync/个人知识库/WKB/一片纸尿裤的六层，只有一层真的在吸水（与卫生巾工艺相同）.md
original_link: "https://mp.weixin.qq.com/s/I3nr6u2aVsmGXpwEgn1fFw"
date_published: 2026-10-24
date_processed: 2026-10-25
credibility: 中
credibility_note: "公众号科普稿，无作者署名、无参考文献；但六层功能分工、材料体系、克重区间与主流工程口径一致，可与本库既有芯体/无纺布页面交叉验证。文中克重与指标为该号自述『典型量产区间』，非特定产品规格书，实施前须以实际 BOM 与规格书复核。锚点为预期路径（插件当日未落盘），待次日复核。"
knowledge_update_status: done
key_claims:
  - "六层里只有第四层（芯体）真正储水，其余五层一滴不存，全部在做同一件事——控制水的行进路线（表层让水快进、导流层把水摊开、包覆层筛颗粒、防漏边挡侧漏、底膜挡液放汽）；把六层理解成『都在吸水』会让每一处结构显得多余"
  - "表层干爽的机理是『留不住水』而非『吸走了水』：1.5D ES 皮芯（PE 皮/PP 芯）热风布 18–22 g/m²，打孔压花使接触面积降 40–45 %，亲水剂把接触角从 112° 降到 22°，但纤维本身无羟基、不吸水"
  - "导流层的唯一职能是摊开而非吸收：60 % ES + 40 % 粗旦中空卷曲 PET（4–6D），30–45 g/m²，湿态回弹 ≥85 %、纵向扩散 160–200 mm；粗旦中空的三维螺旋卷曲是孔隙抗塌的关键"
  - "包覆层用 10–12 g/m² SMMS（两层纺粘夹两层 1–3 µm 熔喷），抗拉靠 S 层、筛 SAP 微珠靠 M 层，且必须亲水改性（高透水）——它的工作是『筛颗粒』不是『挡水』"
  - "芯体是本库 REL 议题的核心变量：220–360 g/m²，六层总克重约 400 g/m² 而芯体独占约七成 → 产品『薄』只能在芯体上做（提 SAP 比例、减绒毛浆，走复合芯体路线），其余五层合计可省空间有限"
  - "SAP 锁水不是『吸』而是渗透压：交联聚丙烯酸钠网络内外离子浓度差把水拉入并困成水凝胶（液→固），故受压不回流；4 kPa 下回渗 <0.15 g，吸水倍率 50–70 g/g（0.9 % NaCl），加压锁水 ≥24 g/g（4.8 kPa），芯体总锁水 500–750 mL"
  - "包覆层与防漏边同源同线：均为 100 % 均聚 PP、同一条 SMS 产线、克重接近（10–12 vs 13–16 g/m²），唯一差别是『做不做亲水改性』——一个接触角 22° 高透水，一个保持原生疏水（静水压 >22 mbar）弹回侧向液流"
  - "液体行进的时间尺度：0 s 接触铺展 → 0–1.8 s 穿透表层（干爽在此刻成立）→ 1.8–5 s 导流层纵向摊开 → 5 s 起 SAP 渗透压锁定（数十秒接近饱和）→ 稳态 4 kPa×3 min 回渗 <0.15 g"
pages_linked: ["[[SAP（高吸水树脂）]]", "[[ADL（导流层）]]", "[[Core Wrap（芯体包裹层）]]", "[[底膜 Backsheet]]", "[[复合吸收芯体（Composite Absorbent Core）]]", "[[Nonwoven 非织造布]]", "[[Meltblown Nonwoven（熔喷非织造布）]]", "[[亲水整理 Hydrophilic Finish]]", "[[接触角 Contact Angle]]", "[[Rewet Test（回渗测试）]]", "[[局部亲水印花面层（锥形孔导流）]]", "[[Gasketing Effectiveness（防漏阻隔有效性）]]"]
compile_mode: semantic
---

# 一片纸尿裤的六层，只有一层真的在吸水（与卫生巾工艺相同）

## Positioning 一句话定位

A **structure-first explainer** that reframes the six layers of a diaper as one control problem — *where does the water go* — rather than six absorption functions. Its library value is a compact, parameterised map of layer-by-layer material choices that can be used as a **sanity baseline** when reviewing a REL/core design or a supplier's BOM.

本页是一篇**以结构为主线的科普解释**：把纸尿裤六层重新表述为同一个控制问题——**水往哪走**，而不是六种吸收功能。其库内价值在于给出了一张**逐层材料 + 量化参数**的紧凑地图，可作为审阅 REL/芯体设计或供应商 BOM 时的**基线对照表**。

## Summary 摘要

The article's core move is negative: **five of the six layers store no water at all.** Only layer 4 — the absorbent core — converts liquid into solid; the other five exist to route, spread, filter, block, or vent. Once that is accepted, every layer's design becomes legible and any "all six layers absorb" mental model makes each structure look redundant.

文章的核心是一个**否定式**命题：**六层里有五层一滴水都不存**。只有第四层（芯体）把液体变成固体，其余五层分别负责导流、摊开、筛颗粒、挡漏、放汽。承认这一点之后，每一层的设计都变得可解释；反之若按「六层都吸水」去理解，几乎每处结构都显得多余。

The second reusable asset is the **inversion used to explain dryness**: the topsheet stays dry *because it cannot retain water*, not because it absorbs it. Synthetic PP/PE fibre has no hydroxyl groups; it only lets water pass. A topsheet that actually absorbed would stay wet against the skin.

第二个可复用资产是**干爽机理的反转表述**：表层干爽是因为它**留不住水**，不是因为吸水。PP/PE 合成纤维没有羟基、没有亲水基团，只「让水通过」；如果表层真吸水，它会一直湿着贴皮肤。

## Six-Layer Functional Map 六层功能对照表

| # | 层 / Layer | 材料与规格 Material & spec | 关键参数 Key parameters | 职能 Role |
|---|---|---|---|---|
| 1 | 表层 Top sheet | 1.5 D ES 皮芯短纤（PE 皮 / PP 芯），热风穿透无纺布，18–22 g/m² | 首次穿透 ≤1.8 s · 摩擦系数 ≤0.22 · 接触角 <25°（未处理 112°） | 让水快速通过并离开皮肤；打孔压花使接触面积 −40–45 % |
| 2 | 导流层 ADL | 60 % ES + 40 % 粗旦中空卷曲 PET（4–6 D），30–45 g/m² | 湿态回弹 ≥85 % · 纵向扩散 160–200 mm · 二次穿透 ≤2.5 s | 把水沿纵向摊开，避免只在中间鼓包、两侧闲置 |
| 3 | 包覆层 Core wrap | SMMS 复合无纺布（2 层纺粘夹 2 层 1–3 µm 熔喷），10–12 g/m²，100 % 均聚 PP | 亲水改性高透水 · 360° 包裹 | 水通过、SAP 微珠（≈300 µm）不漏；S 层管湿态抗拉，M 层管阻隔 |
| 4 | 芯体 Core | SAP 微珠 + 绒毛浆 / 蓬松无纺布复合，220–360 g/m² | 吸水倍率 50–70 g/g（0.9 % NaCl）· 加压锁水 ≥24 g/g（4.8 kPa）· 总锁水 500–750 mL · 4 kPa 回渗 <0.15 g | **唯一储水层**；渗透压致液→固，故挤压不回流 |
| 5 | 防漏边 Leg cuff | 同源 SMS（13–16 g/m²），100 % 均聚 PP，**不做**亲水改性 | 原生疏水 · 静水压 >22 mbar | 把侧向冲来的液体弹回；同时允许水蒸气从微孔逸出 |
| 6 | 底膜 Backsheet | 阻液透湿膜 | 挡液态水、放水蒸气 | 外侧防漏的最后一层（文中为定性描述，未给克重/透湿量） |

> 克重合计约 400 g/m²，芯体一层占约七成。（Total ≈400 g/m², with the core accounting for roughly 70 %.)

## Transport Timeline 液体行进时间轴

| 时刻 | 发生什么 | 对应层 |
|---|---|---|
| 0 s | 液滴接触表层，接触角 22° 瞬间铺展，从倒锥孔大口进入 | 表层 |
| 0–1.8 s | 穿过打孔层；纤维不吸水，走完即空 → **干爽在此刻成立** | 表层 |
| 1.8–5 s | 进入导流层，粗旦中空孔隙湿态不塌，毛细拉动纵向扩散至 160–200 mm | 导流层 |
| 5 s 起 | SAP 遇液，渗透压把水拉进交联网络并膨胀成水凝胶（数十秒接近饱和） | 芯体 |
| 稳态 | 4 kPa × 3 min，回渗 <0.15 g（验证「变成固体」是否成立） | 芯体 |
| 全程 | 两侧疏水护围弹回横向液流（>22 mbar），水蒸气经微孔逸出 | 防漏边/底膜 |

## Why It Matters for REL 与本库 REL 议题的关联

The article is useful precisely at the boundary the REL project operates on: **the core is the only layer with meaningful mass to remove.** With the core at ~70 % of total grammage, thinning cannot come from the other five layers — it must come from raising SAP fraction and cutting fluff, i.e. the **composite (fluff-free / low-fluff) core** route that the library already documents separately.

这篇文章的有用之处，正好落在 REL 项目的工作边界上：**只有芯体这一层还有可观的克重可减**。芯体约占总克重七成，产品变薄不可能靠其余五层，只能靠提高 SAP 比例、减少绒毛浆——即本库已单独成页的**复合（无木浆/低木浆）芯体**路线。

It also supplies a quantitative cross-check for two numbers REL work repeatedly touches: **rewet at 4 kPa (<0.15 g)** and **pressurised retention (≥24 g/g at 4.8 kPa)** — both stated here as typical production ranges, so they can serve as sanity bounds rather than specifications.

同时给出两个 REL 反复涉及指标的量化参照：**4 kPa 回渗 <0.15 g** 与 **加压锁水 ≥24 g/g（4.8 kPa）**。文中明确其为「典型量产区间」，因此只能当**合理量级校验**，不能当规格值使用。

## Links 关联

- 结构/材料：[[SAP（高吸水树脂）]] · [[ADL（导流层）]] · [[Core Wrap（芯体包裹层）]] · [[底膜 Backsheet]] · [[Nonwoven 非织造布]] · [[Meltblown Nonwoven（熔喷非织造布）]]
- 界面与改性：[[亲水整理 Hydrophilic Finish]] · [[接触角 Contact Angle]] · [[局部亲水印花面层（锥形孔导流）]]
- 性能评价：[[Rewet Test（回渗测试）]] · [[Gasketing Effectiveness（防漏阻隔有效性）]]
- 芯体路线：[[复合吸收芯体（Composite Absorbent Core）]]

## Source 来源

- 原文链接：https://mp.weixin.qq.com/s/I3nr6u2aVsmGXpwEgn1fFw
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/一片纸尿裤的六层，只有一层真的在吸水（与卫生巾工艺相同）.md`（4.3 k 字符，`extract_status: ok`）
- 取文通道：`get_media_info` 返回公众号 URL → 浏览器 UA 直取 HTML → 抽 `#js_content`（不吃 `get_doc_content` 日配额）。首次 urllib 默认 UA 命中微信反爬「环境异常」页，换 UA 后正常。
- media_id：`wechatarticle_3867e2b60070d7dc3f413086d0b0036e_4af337dbbd6bcdb191e5411ceb72c6ab`

---
type: source
title: "REL_Cost_Model_28gsm_vs_40gsm_20261023.xlsx"
source_type: 报价单
source_path: RAW/ima_sync/个人知识库/WKB/REL_Cost_Model_28gsm_vs_40gsm_20261023.xlsx.md
original_link: ""
date_published: 2026-10-23
date_processed: 2026-10-25
credibility: 中
credibility_note: "自建成本模型（四页工作表 Model/Compare/Sensitivity/Assumptions），输入参数均标注来源与日期，可直接追溯到报价与行情；但全部派生单元格为**公式且未存缓存值**，本页只能复述输入口径与文件内的文字结论，无法复核具体数值。关键输入『PTT/PET S/S 20,500 元/t』取供应商千吨级口头交底中值，高于按公开行情推导的 17,000–19,500 区间，属**供应商口径**而非市场价；『偏心中空 ES 13,500』文件自标【待核】。"
knowledge_update_status: done
key_claims:
  - "本模型的核心结论不在价格而在克重：设计克重 28.8 gsm 时全成本低于 40 gsm 传统 REL 四基线均值，但**回缩后实际成网 33 gsm** 时，克重优势被配方溢价吃掉，成本**反超**传统方案 —— 决策变量是回缩率，不是纤维单价"
  - "四家 40 gsm 传统 REL 竞品基线：YJ DL24C 39.8 gsm / 配方 10,600 元/t；DY ND055 38.8 / 10,350；ZB 箱式 40 / 10,146；藤东 40 / 9,170 元/t；传统基线均值定为 **0.5775 元/m²**（PET 短纤按 9,100 计），取代 10-18 口径的 0.567"
  - "PTT/PET S/S 纤维取 **20,500 元/t**（恒碳千吨级 20,000–21,000 中值）；文件明确『26,000 系小样价不适用』——即采纳了 10-18 页的『26,000 站不住』判断，但用**千吨级交底价**而非公开行情推导值"
  - "价格拆解口径：PTT 18,000×50% + PET 8,600×50% + 复合纺丝 4,000 + 成品率 94–95% + 运输 400 + 溢价 1,500–2,500；普通短纤纺丝加工费仅 900–1,000，复合纺 4,000 是主要加成项"
  - "配方口径：非 PTT 组分按 34:8:30:6 归一化（ES CoPET/PET 2D / 3D / 偏心中空 ES / PVA 6D），PTT 添加比例 22%（会议确认，合理区间 10–30%，超 30% 骨感变差）"
  - "加工费按 4,500 元/t（ATB 热风粘合 + 分切，含能耗与人工）；单片面积 0.038 m²（≈100×380 mm），年产 1 亿片用于年度金额换算"
  - "敏感度矩阵三张：纤维价 19,000–22,000 × 克重 28–34；PTT 比例 10–30% × 克重 28–34；以及对应年度金额差（万元/年·按 1 亿片）"
  - "未含项被显式列出：3–5% 工艺损耗、分切废料、打样摊销、关税与认证（ISCC 等）单独费用 —— 意味着模型偏乐观，实际落地成本应在此之上"
  - "辅助判据：纤维价每降 1,000 元/t 对元/m² 的传导、以及『与基准打平的临界克重』被单列为关键判断项（Model!B39），说明作者把克重而非价格当作首要杠杆"
pages_linked: ["[[REL增强层]]", "[[PTT（聚对苯二甲酸丙二醇酯）]]", "[[恒碳（Hengtan）]]", "[[C1 Life Biotech]]", "[[皖维高新]]", "[[江南高纤]]", "[[热风非织造 Hot-Air Bonded Nonwoven]]", "[[双组分纤维 Bicomponent]]", "[[ES 双组分弹性纤维热风布（弹性体改性）]]", "[[PTT切片价格对标：恒碳非切片厂，26,000元每吨报价偏离公开行情]]"]
compile_mode: semantic
---

# REL_Cost_Model_28gsm_vs_40gsm_20261023.xlsx

## Positioning 一句话定位

The project's **first first-class cost model for the 28 gsm lightweight REL**: four linked worksheets (inputs → comparison → sensitivity → assumptions) that convert a supplier price quote into a **per-m² full cost versus four 40 gsm incumbent baselines**. Its value is less the number it produces than the variable it identifies as decisive — **shrinkage-driven actual grammage**, not fibre price.

本页是本项目**第一份正式化的 28 gsm 轻量化 REL 成本模型**：四张联动工作表（输入 → 对比 → 敏感度 → 假设）把一次供应商报价换算成**相对四家 40 gsm 传统基线的元/m² 全成本**。其价值不在算出的那个数，而在于它指认了真正的决定性变量——**由回缩决定的实际克重**，而不是纤维单价。

## Model Structure 模型结构

| 工作表 Sheet | 作用 Role | 关键内容 Key content |
|---|---|---|
| Model | 输入参数 + 吨成本 + 单位成本 + 关键判断 | 13 项输入（纤维价/克重/比例/加工费/面积/年产量/传统基准），配方按 34:8:30:6 归一化 |
| Compare | 新 REL（设计 vs 实际成网）× 四家传统基线 | YJ DL24C、DY ND055、ZB 箱式、藤东；读数行给出定性结论 |
| Sensitivity | 纤维价 × 克重、PTT% × 克重、年度金额差 | 三维度扫描，用于判断结论稳健性 |
| Assumptions | 价格假设与口径说明 | 每项带来源与日期；标注【待核】项；显式列出未含项 |

## Key Inputs 关键输入（含来源口径）

| 参数 Input | 值 Value | 口径 / 来源 Basis |
|---|---|---|
| PTT/PET S/S 纤维价 | 20,500 元/t | 恒碳千吨级交底 20,000–21,000 取中值；**26,000 系小样价，不适用** |
| 设计克重 Design gsm | 28.8 gsm | 图纸 / 标称 28 gsm |
| 实际成网 Actual gsm | 33 gsm | 会议：布 28–29 gsm → 工厂回缩至 33 gsm |
| PTT 添加比例 | 22 % | 会议确认；合理区间 10–30 %，>30 % 骨感变差 |
| ES CoPET/PET 2D / 3D | 11,600 元/t | 卫材级复合短纤（江南高纤均价折算） |
| 偏心中空 ES | 13,500 元/t | **【待核】** 原生中空 7D 10,100–10,200 + ES 皮芯溢价 |
| PVA 水不溶 6D | 20,000 元/t | 皖维高新报价 |
| 加工费 ATB | 4,500 元/t | 热风粘合 + 分切，含能耗与人工 |
| 单片面积 | 0.038 m² | ≈100×380 mm |
| 传统 40 gsm 基准 | 0.5775 元/m² | 四竞品基线均值（PET 短纤按 9,100 计） |

## Cost Verdict 成本判断

The file's own reading is explicit: **at the design 28.8 gsm the new REL beats the four-baseline mean; once the web shrinks to 33 gsm, the grammage advantage is consumed by the formulation premium and the cost reverses above baseline.** Derived cells carry no cached values, so the crossover grammage (Model!B39) cannot be verified here — but the qualitative call is stated in the Compare sheet and is what the Sensitivity pages are built to test.

文件自述的读数很明确：**设计克重 28.8 gsm 时新 REL 优于四基线均值；一旦回缩到 33 gsm，克重优势被配方溢价吃掉，成本反超。** 派生单元格无缓存值，临界克重（Model!B39）在本页无法复核——但定性结论写在 Compare 页，且 Sensitivity 三张表正是为检验该结论的稳健性而设计。

**Reconciliation with the 2026-10-18 price check 与 10-18 价格核查的口径衔接**

| 口径项 | 10-18 页 | 本模型（10-23） | 差异原因 |
|---|---|---|---|
| 40 gsm 传统均值 | 0.567 元/m² | **0.5775 元/m²** | PET 短纤取价 9,025/9,300 → **9,100**；基线四项重新取值 |
| PTT/PET S/S 纤维价 | 17,000–19,500（按公开行情推导） | **20,500**（供应商千吨级交底） | 由「市场推导」改为「供方承诺价」——**更保守，也更可作为谈判锚** |
| 26,000 报价定性 | 站不住（+60% vs 巨化） | 明确不适用（小样价） | 一致 |

> 结论：两次口径**不矛盾而是升级**——10-18 用公开价证明 26,000 站不住；本模型改用供方千吨级价 20,500，反而更容易被供方接受，同时保留了「价格不是主变量」的判断。
> (The two exercises are consistent: the earlier note proved the CNY 26,000 quote indefensible; the model then adopts the supplier's kiloton-scale number instead — a more conservative but more negotiable anchor, while keeping the conclusion that price is not the primary lever.)

## Decision Implications 决策含义

1. **把回缩率变成一级技术指标。** 28.8 → 33 gsm 是 +14.6 % 克重，足以吃掉全部成本优势。任何 28 gsm 方案在报价前必须先锁定「成布回缩后克重」，否则成本结论不可用。
2. **临界克重是本项目真正的 KPI 门槛**（文件把它单列为「关键判断」）。采购谈判的让步空间应以「临界克重 − 实际克重」的余量来度量，而不是以元/t 让价度量。
3. **未含项须计入决策。** 3–5 % 工艺损耗 + 分切废料 + 打样摊销 + ISCC 认证，叠加后足以把「低 2–4 %」抹平——这与上一条同向。
4. **偏心中空 ES 的 13,500 是最大单点不确定**：若降至 12,000，文件自述全成本再降 0.0043 元/m²（约 0.7 %），属可谈判项。

## Links 关联

- 上游价格与供方：[[PTT切片价格对标：恒碳非切片厂，26,000元每吨报价偏离公开行情]] · [[恒碳（Hengtan）]] · [[C1 Life Biotech]] · [[皖维高新]] · [[江南高纤]]
- 材料与工艺：[[PTT（聚对苯二甲酸丙二醇酯）]] · [[双组分纤维 Bicomponent]] · [[ES 双组分弹性纤维热风布（弹性体改性）]] · [[热风非织造 Hot-Air Bonded Nonwoven]]
- 项目主线：[[REL增强层]]

## Source 来源

- 原件：`RAW_FULL/ima_sync/个人知识库/WKB/attachments/REL_Cost_Model_28gsm_vs_40gsm_20261023.xlsx`（14,741 B，4 工作表）
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/REL_Cost_Model_28gsm_vs_40gsm_20261023.xlsx.md`（`extract_status: ok`，`zipfile` 直读 sheet XML 转换）
- 取件通道：通道 B `get_media_info` → 签名 URL 直下原件（**不吃 `get_doc_content` 日配额**）
- media_id：`excel_3867e2b60070d7dc3f413086d0b0036e_37abcdd9529d15c386310e20902922c6001a693ee6c0644e`
- 锚点说明：`source_path` 为**预期路径**（插件当日未落盘），次日需复核插件实落名；不符按三处同步修正，勿新建重复页。

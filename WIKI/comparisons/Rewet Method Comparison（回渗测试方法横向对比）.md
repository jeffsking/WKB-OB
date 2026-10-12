---
type: comparison
title: "Rewet Method Comparison（回渗测试方法横向对比）"
subjects: ["[[Rewet Test（回渗测试）]]", "[[Bladder Box Intake Test（膀胱箱压载摄入测试）]]", "[[Cradle Intake Test（Cradle 摄入测试）]]"]
dimension: 综合
updated: 2026-09-29
tags: [回渗, 测试方法, FIUP, TTM-00623, TTM-00643, Collagen, 对标]
---

# Rewet Method Comparison（回渗测试方法横向对比）

## 对比维度表 Comparison matrix

> 必含「成本 Cost」与「供应链风险 Supply chain risk」两列（Required columns per AGENTS.md §2.4）。本页的「成本」指**测试执行成本（设备、耗材、工时）**，「供应链风险」指**耗材/设备可得性与方法连续性风险**。

| Dimension 维度 | KC Lo/Hi（TTM-00623） | P&G Duck | P&G Collagen（BCC / AFC） | KC FIUP（TTM-00643） | KC Closed Cradle | NWSP 070.9（零售商要求） | Source 依据 |
|---|---|---|---|---|---|---|---|
| 加液压力 Insult pressure (psi) | 0.02（低）/ 0.4（高） | 0 | 0.53 / 0.30 | 0.25 | 约 0.25 | 无（不加压） | [[Rewet Method Comparison（回渗测试方法横向对比·K-C vs P&G）]] |
| 回渗压力 Rewet pressure (psi) | 0.005 / 0.24 | 0.55 | 3.35 / 1.0 | **0.5** | 0.5 | 1.0 | 同上 |
| 回渗砝码尺寸 | 114 × 432 mm | 直径 76.2 mm | — / 直径 61 mm | 直径 61 mm 或 25×50 mm | 直径 61 mm | — | 同上 |
| 加液温度 Fluid temp | 室温 | 室温 | 37 ℃ / 室温 | **37 ℃** | 37 ℃ | — | 同上 |
| 液体 Fluid | 盐水 | 盐水 | 合成尿 / 盐水 | 盐水 0.9±0.005% | 盐水 | — | 同上 |
| 吸水纸 Blotter | 100 lb Verigood（300 gsm），1–2 张 | 同左，2 张 | **31 gsm Collagen（Naturin Coffi 0.08 mm）** | 300 gsm Verigood，2 张 | 2 张 88×300 mm | 10 g 滤纸，直径 90 mm | 同上 |
| 加液靶点 Target | 按尺码/性别（消费者研究） | — | **mid-pad** | 按尺码与应用 | F 95 / M 200 mm | Center pad, flat | 同上 |
| 末次加液 → 读数等待 | — | — | 5 min（AFC） | **2 min** | 2 min | 10 min | 同上 |
| 加液方案 Loading | 多次、Lo/Hi 双档 | — | 多次 | 3 次（T=0/15/30 min） | 3 × 50 mL，间隔 15 min | 1 × 105 mL | 同上 |
| **成本 Cost（执行侧）** | **低**：常压/低压、通用吸水纸、室温盐水，无特殊耗材 | 低—中 | **高**：需专用 **31 gsm Collagen 纸**（Naturin Coffi 牌号）与更高回渗压力夹具 | 中：需压力箱（bladder box）+ 37 ℃ 盐水 + 温控；单次流程约 34 min | 中：需 cradle 与压力控制 | 低—中：单次加液、10 min 等待，但需另备 90 mm 滤纸 | 同上（耗材与设备项） |
| **供应链风险 Supply chain risk** | **低**：100 lb Verigood 吸水纸为通用耗材，方法沿用多年 | 低 | **高**：Collagen 纸为**特定牌号专用耗材**，且其方法参数绑定竞品宣称体系，切换成本高 | **中**：依赖压力箱、独立压力传感器与 37 ℃ 恒温盐水；方法版本仍在演进（2015 → 2020 rev 4 改压力） | 中：依赖 cradle 夹具与解剖位定义 | 中：零售商指定方法（外部不可控），且与 KC 方法差异显著，需另行送测建立换算 | 同上 |

> 尾注 Endnote：本表所有参数均来自 [[Rewet Method Comparison（回渗测试方法横向对比·K-C vs P&G）]]（K-C 内部方法学对标，2024-09-30，含 2024-10-22 FIUP 专审）。**该来源未给出任何价格数字**，「成本」列为基于设备/耗材/工时的相对判断，非报价；「供应链风险」列为基于耗材专用性与方法演进的判断。

## 已知实测差异 Known empirical gaps

| Finding 发现 | Detail 具体 | Source 出处 |
|---|---|---|
| **FIUP 回渗 > Closed Cradle 回渗** | 成人失禁品 2022–2024 数据：**FIUP 回渗高于 Closed Cradle**，有时高出很多；成因不明 | [[Rewet Method Comparison（回渗测试方法横向对比·K-C vs P&G）]] |
| 缺同批次对照 | 其他方法之间**缺少同一测试申请下的对照数据**，无法建立换算关系 | 同上 |
| 版本断点 Version break | 回渗砝码由 **0.7 psi / 1 in 直径 → 2020-09（rev 4）0.5 psi / 6 cm 或 1×2 in**，跨 2020 年同期数据不可直接比较 | 同上 |
| 草案流入正式方法 | STM-00497 草案**从未正式发布**，但其参数进入了 FIUP TTM-00643 rev 0 | 同上；[[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]] |
| 加载数据陈旧 | 2015 年前 Poise 加载数据来自 2009 年汇总（TL-14137）；2013–2014 研究定义了 2015 年启用的新数据；**至 2024-10 仍有新品尺码为假设外推** | 同上；[[R150540-TL-14137 Poise Use-Test Load & Leakage Summary（2009）]] |

## 各自适用场景 Where each fits

- **KC FIUP（TTM-00643）**：成人/女性护理**加压摄入 + 回渗**的内部主方法；需压力箱，读数在 34 min 处，适合做产品宣称支撑前的完整评估。
- **KC Closed Cradle**：无/低压解剖位条件下的对照方法；读数更接近"平躺未受压"场景，数值系统性低于 FIUP。
- **KC Lo/Hi（TTM-00623）**：低/高两档压力的成对设计，用于观察产品对压力敏感度的斜率，而非单点绝对值。
- **P&G Collagen 系列**：竞品自有方法（含专用 collagen 纸与更高回渗压力），**仅可用于对标理解，不可当作 K-C 数据的替代**。
- **NWSP 070.9**：零售商（Walmart）指定方法，用于投标/送测场景；与 K-C 方法差异大，须单独建立换算或另做送测。

## 结论 Conclusion

一句话结论 One-sentence conclusion：**回渗不是一个绝对值而是一个"方法 + 版本"的函数——六个参数（加液压力、回渗压力、液体温度与种类、吸水纸、靶点、等待时间）任一不同即不可比；跨方法、跨 2020 年版本、跨加载数据年份的比较都必须先声明口径。**

## 追加：Resources/Open Innovation 批（2026-09-29 追加 · 11 方法参数矩阵底稿）

> 追加来源 `[[Rewet Method Parameter Matrix (xlsx)（回渗测试方法参数矩阵·11 方法）]]`（`Rewet Method Comparison.xlsx` 的 `[Parameter Comparison]` + `[Insult Parameters]` 子表）。本段**只补"逐方法 × 逐参数的原始取值"，不改动上方任何对比维度、适用场景与结论**。

### 1. 11 方法 × 12 参数的取值对照（本批新增的量化底稿）

| 维度 | KC Lo/Hi（低） | KC Lo/Hi（高） | KC FIUP | KC Closed Cradle | P&G Duck | P&G Collagen (BCC) | P&G Collagen (AFC) | China U Rewet | Diaper Testing Intl | NWSP 070.9.R1 | Costco FQ Demo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **加液压力 (psi)** | 0.02 | 0.4 | 0.25 | ~0.25 | 0 | **0.53** | 0.25 / 0.30 | 0.29 | 0 | 0 | 0 |
| **回渗压力 (psi)** | **0.005** | 0.24 | 0.5 | 0.5 | 0.55 | **3.35** | 0.77 / 1.0 | 0.58 | 0.34 | 1 | 0.5? |
| 液体 | Saline | Saline | Saline | **STCH Saline** | Saline | **Synthetic Urine** | Saline | Saline | Saline | Saline | Saline |
| 温度 (°C) | 室温 | 室温 | **37** | **37** | 37 | 37 | 37 | **36** | 23（室温） | 室温 | 室温? |
| 吸水纸 | 100 lb Verigood | 同左 | 同左 | 同左 | Blotter | **Collagen** | Collagen 31 gsm | Filter Paper 145 gsm | Filter Paper Type 102 | Filter Paper Grade 950 | Grade 950? |
| 张数 | **1** | 2 | 2 | 2 | 1 | — | 4 或 2 | **10** | **10** | ~10 g | ~10 g? |
| 加液位置 | 随尺码/性别 | 同左 | 随尺码/用途 | **女 95 / 男 200 mm** | — | 护垫中点 | 护垫中点 | 中心前 ~35 mm | 前 1/3 | 裆部中心 | 裆部中心? |

> ⚠️ 表中带 `?` 者为原表**未确认值**（Costco 整列多带 `?`），**不得当作确定口径引用**。

### 2. ⚠️ 三处最刺眼的跨度（对上方结论的量化支撑）

| 维度 | 跨度 | 倍差 |
|---|---|---|
| **回渗压力** | **0.005 psi（KC Lo/Hi 低）↔ 3.35 psi（P&G Collagen BCC）** | **≈670×** |
| **吸水纸张数** | 1 张 ↔ 10 张 | **10×** |
| **液体温度** | 23 °C ↔ 37 °C | 约 14 °C |

> 这三条是"**回渗不是一个绝对值，而是方法 + 版本 + 口径的函数**"这一结论最直接的量化证据 —— 与上方结论**同向且互补**（上方给的是六个参数清单，本批给的是**实际取值跨度**）。

### 3. 逐产品 × 性别 × 尺码的加液量（Insult Parameters 子表）

| 品类 | 尺码 / 档位 | 单次加液 (mL) | 次数 | 速率 (mL/s) | 加液位置（center 前 cm） |
|---|---|---|---|---|---|
| 婴儿纸尿裤（Low/Hi TTM-00623） | NB → S1 → S2 → S3 → S4 → S5/S6 | **40 → 50 → 60 → 70 → 85 → 100** | 3 | 9 → 15 | 4 → 5.5 → 6.5 → 7.5 → 8.5 → 9 / 9.2 |
| Training Pants | Size 2（女/男/中性） | 80 | 3 | 15 | **6.5 / 10.5 / 8.5** |
| Training Pants | Size 3 / 3.5 | 100 / 110 | 3 | 15 | 7 / 11 / 9；7 / 12 / 9.5 |
| Youth Pants | Size 4 | 120 | 3 | 15 | **9 / 15 / 12** |
| Youth Pants | **Size 5.5** | **220** | **2** | 15 | 8 / 17 / 15 |
| 成人 DPU（FIUP） | DPU1 女 / DPU2·DSU 女 / 男 / DPU3 女 / 男 | 50 / 105 / 115 / 150 / 165 | 3 | 8 | 9.5（女）/ 20（男） |
| Poise（Ad Claim） | 1 → 2 → 3 → 4 → 5 → 6-8 drop | 1 → 2 → **≤23** → 10 → 26 → 38 | 3 | 1 或 8 | 3.5 → 11.55 cm |
| **NWSP 070.9** | 全部 | **100（单加液）** | — | — | — |

> **重要**：Poise 分 **Research** 与 **Ad Claim** 两套加液口径，**Ad Claim 明显更保守**（例：3 drop 档 Research 8 mL vs Ad Claim ≤23 mL 级别差异；4–8 drop 档改用"Mean study loadings"研究实测平均载荷）。**引用 Poise 数据必须声明是哪一套**。

### 4. 方法编号索引（可回溯）

| 方法 | 编号 |
|---|---|
| KC Lo/Hi | **TL-15701 / TTM-00623** |
| KC FIUP | **TL-15927 / TTM-00643** |
| KC Closed Cradle | **TL-15599 / TTM-00672** |
| P&G Collagen (AFC) | TL-15599, TL-16227 |
| China U Rewet | 2015 & 2018 disclosures + `China Urewet Sizing and blotter selection guide.xlsx` |

> ✅ 验证（2026-09-29）：本追加段**未修正**上方任何结论；上方"六个参数任一不同即不可比"的结论在本批获得**逐参数取值验证 ✓**，且新量化出**回渗压力 670×、吸水纸张数 10×、温度 14 °C** 三处跨度。

## 追加：方法谱系与宣称史（2026-09-29 追加 · 来源：Rewet Development.pptx）

> ✅ Verification（2026-09-29，source 来源 [[Rewet Development.pptx]]）：本库各 rewet 方法的**谱系归属**获得培训材料级确认——**BCC 与 AFC 各自开发**了消费者相关参数的 rewet 方法（**TTM-00623 Lo/Hi、TTM-00643 FIUP、TTM-00772 Closed Cradle**），**Depend 基于 Poise 方法加 curvature** 反映其产品使用条件。宣称史背景：KC 曾以 TEWL 为产品湿度度量，2014 P&G 发起激进 rewet 宣称、NAD 裁定 rewet 宣称可成立，开启 rewet 宣称时代。**边界重申**：rewet 与 leakage 不相关（leakage 看 intake/runoff），intake/retention 也不必然给出 rewet 洞察；皮肤干爽主张仍以 **EWL** 为推荐 substantiation 方法（inner cover breathability 为皮肤水分主驱动）。方法开发报告编号：R161025（00623）、R164444（00643）、R167540（00772）、R182317（claims substantiation）。

## 追加：AFC 五方法 brief 参数矩阵与 FIUP-CC 系统差（2026-09-29 追加 · 来源：Rewet Method Comparison_brief.pptx）

> ✅ Verification（2026-09-29，source 来源 [[Rewet Method Comparison_brief.pptx]]）：Clemmer & Gaweda（2024-09-30）五方法 brief 为上方矩阵提供**AFC 在用方法的核心参数行**：KC Lo/Hi（Lo 0.02 psi / Hi 0.4 psi insult，回渗权重 0.005/0.24 psi）、KC FIUP（F 95 / M 200 mm 加液位、**37 °C**、0.25 psi）、KC Closed Cradle（**31 gsm Collagen** 介质、37 °C）、P&G Collagen（回渗权重 **1.0 psi**、仅等 **15 秒**）。**新增实测事实：2022-2024 成人失禁裤中 FIUP 回渗系统性高于 Closed Cradle（有时差很多，驱动因素不明），且同一测试请求内无跨方法对比数据**——该系统差是"方法间不可比"结论的首个成体系实证，驱动因素归因 `[待验证]`。完整参数表见 source 页。

## Sources 来源

- [[Rewet Method Comparison（回渗测试方法横向对比·K-C vs P&G）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Test Methods/Rewet Method Comparison.pptx.md`
- [[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]] —— `RAW/.../Intake via Bladder Box draft STM-00497 - Copy.docx.md`
- [[R150540-TL-14137 Poise Use-Test Load & Leakage Summary（2009）]] —— `RAW/.../R150540_TL-14137_Summary of POISE Use Test Load and Leakage Data (2009).pdf.md`
- [[Rewet Test（回渗测试）]]、[[Bladder Box Intake Test（膀胱箱压载摄入测试）]] —— 本库既有概念页

---
type: concept
title: "Product Waist Break Test（产品腰围拉断测试）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-30
tags: [拉断强度, 腰围, Pants, 快速上提, 内控, gf]
---

# Product Waist Break Test（产品腰围拉断测试）

> 一句话定义：**产品腰围拉断测试**模拟消费者**快速上提后腰围**的动作，以**拉力仪最快速度（1000 ± 10 mm/min）**拉伸试样并读取最大载荷（gf），用来量化 Pants（拉拉裤）在使用中被「拉断」的抵抗能力。

## Definition 定义

本方法是**为应对消费者投诉而新创建**的方法，不是 KC 全球 STM 体系内的既有编号方法。它来自 [[BCC Pants Waist Break Study（Pants 产品拉断研究与两项新方法创建）]]（Tulip Cai，2026-03）；[[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] 中亦出现「**STM-产品拉断新**」这一未编号方法，说明该指标已在厂内落地。

配套的第二项新方法为**底膜与内腰围粘合强度**（夹具距离 40 mm、底膜向后撕开 10 mm），用于定位拉断的界面成因。

## 机理 / 结构拆解 Mechanism

1. **工况是「快速」而非「慢速」**：拉伸速度取拉力仪最快（1000 ± 10 mm/min），因为消费者上提裤子的动作是瞬时的；慢速拉伸会测到材料的蠕变行为而非断裂行为。
2. **读最大值而非平台值**：断裂是瞬时事件，取峰值载荷（gf）。
3. **拉断不是单一材料问题**：鱼骨图把成因分到环境（夏季、刚洗完澡后穿着）、材料（内/外腰围 CD 强度、有无丢弃贴、是否 online try）、人（操作）、方法（Chopper 位置、芯体长度与 MD 位置、Folder 强度、芯体与腰围粘合）、机器（Chopper 切割、Folder 施胶、芯体复合 nip roll）六个方面。
4. **主导因子是几何 + 胶宽**：回归显示 **Foldover 盖芯体胶宽度**与拉断强度线性相关，方程 **拉断强度 = 477.3 + 126.5 × 胶宽度**（R-sq 84.54%，P = 0.009）——**胶盖住芯体越多，抗拉断越强**。
5. **方向性**：**前端拉断低于后端拉断**；**chopper 位于底膜固定上方时产品更易拉断**。

## 关键参数表 Key Parameters

| 参数 Parameter | 口径 / 数值 Value | 出处 Source |
|---|---|---|
| 模拟动作 Simulated action | 消费者快速上提后腰围 | [[BCC Pants Waist Break Study（Pants 产品拉断研究与两项新方法创建）]] |
| 制样 Specimen | 宽 **3 in**，至少 **100 mm** 长 | 同上 |
| 拉伸速度 Speed | **1000 ± 10 mm/min**（拉力仪最快速度） | 同上 |
| 夹具距离 Gauge | **3 in** | 同上 |
| 读值 Readout | 最大值，单位 **gf** | 同上 |
| 配套方法：底膜与内腰围粘合强度 | 夹具 **40 mm**；底膜向后撕开 **10 mm** 后夹紧；速度同产品拉断 | 同上 |
| 内腰围 CD 内控 | **1400 gf** | 同上 |
| 产品拉断推荐标准 | **3500 ± 1000 gf** | 同上 |
| 产品拉断内控阈值 | **2800 gf** | 同上 |
| 长期过程能力 | 后端拉断（无丢弃贴相）均值 **3200 gf**，**Cpk = 1.06** | 同上 |
| 回归关系 Regression | 拉断强度 = 477.3 + 126.5 × foldover 盖芯体胶宽度；R-sq 84.54%（adj 80.68%），P = 0.009 | 同上 |
| Foldover 理论标准 | L **30 mm**；XL/XXL **20 mm**（FPS 暂无规定） | 同上 |
| 丢弃贴效应 | 有丢弃贴组均 **P < 0.05** 显著且为正向；无丢弃贴组 P > 0.05 | 同上 |
| 改善效果 | Foldover 调整后均值 **2700 gf**；底膜-内腰围剥离 390 → 720 gf 后升至 **3050 gf**；**连续 6 个月无投诉** | 同上 |

> 🔴 **manual_review（2026-09-29）**：上表内控阈值（1400 / 2800 / 3500 ± 1000 gf）为**厂内质量判据**，是否对外披露需人工确认。原文留存于 `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/Pants 产品拉断测试方法/关于pants类产品拉断的研究分享- Tulip.pdf.md`。

> ⚠️ **禁止无来源参数**：本页全部数字来自单一来源 [[BCC Pants Waist Break Study（Pants 产品拉断研究与两项新方法创建）]]，且该报告多数图表为 OCR 提取，**部分配对数值存在重复行与疑似错位** `[待验证]`。

## 相邻概念 Related Concepts

- 上位 / 相关：[[芯体测试方法与验收基准（STM）]]、[[Hook-and-Loop Strength Test（粘扣系统强度测试）]]、[[Elastic Tension & Creep（橡筋张力与回缩率）]]
- 结构相关：[[Waist Guard（腰围护挡）]]、[[COCO芯体平台]]、[[Hot-Melt Slot Coating（热熔狭缝涂布）]]
- 失效相关：[[Elastic Strand Snicking（弹性橡筋断丝失效化）]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[BCC Pants Waist Break Study（Pants 产品拉断研究与两项新方法创建）]]、[[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]]）：两份来源互证「拉断是三厂共性使用现象、且已催生专门方法」，非单点偶发。

- **教训一（方法）**：**有些失效必须先造方法才能谈改善**。拉断投诉在北厂/南厂/天津厂均有，但直到自建「快速上提」方法后才可量化攻关。
- **教训二（结构）**：**抗拉断的主杠杆在 Foldover 盖芯体胶宽度，不在腰围材料本身**。R-sq 84.5% 说明几何+胶量的权重高于原材料强度。
- **教训三（方向）**：**前/后端与 chopper 位置是方向性变量**，只报一个「产品拉断值」会掩盖前后端差异。
- **教训四（质量）**：**改善要以 Cpk 与投诉数双重验收**——本例 Cpk 1.06 且连续 6 个月零投诉才算闭环。
- **待补 `[待验证]`**：该方法的正式 STM 编号（南京册仅写「STM-产品拉断新」）；不同尺码的阈值是否分档；Pants 与 OD 是否共用同一方法。

## 来源 Sources

- [[BCC Pants Waist Break Study（Pants 产品拉断研究与两项新方法创建）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/Pants 产品拉断测试方法/关于pants类产品拉断的研究分享- Tulip.pdf.md`
- [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/STM-00034 FIFE/BCC成品STM-南京南厂 1.pdf.md`
- [[STM-01086 BCC Pants 产品拉断测试（Pants 产品拉断测试方法）.doc]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/Pants 产品拉断测试方法/STM-01086 BCC Pants 产品拉断测试.doc.md`（2026-09-29 追加）
- [[STM-01086 BCC Pants 产品拉断测试（成品）.doc]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/STM-01086 BCC Pants 产品拉断测试.doc.md`（2026-09-29 追加，内容相同的副本）

## 追加：正式 SOP 落地（2026-09-29 追加，不改动上方既有结论）

> 本节为 **Areas / Test Method 批次 05** 编译时的追加记录。上方"待补 `[待验证]`：该方法的正式 STM 编号"**在本批得到解答**。

> ✅ 验证（2026-09-29，来源 [[STM-01086 BCC Pants 产品拉断测试（Pants 产品拉断测试方法）.doc]]）：本方法已有**正式编号 STM-01086**（厂内 SOP），且**明确写由端封方法 STM-00078 改参数而来**。SOP 与研究报告给出的口径**完全一致**——拉伸速度 **1000 ± 10 mm/min**、夹具距离 **3 in**、单位 **gf**、试样 **3 in 宽 × ≥100 mm**——**原结论未被修正，仅补齐编号与派生关系**。

### 本批新增的口径细节

| 项目 Item | 数值 / 口径 Value | 出处 Source |
|---|---|---|
| 正式编号 Method ID | **STM-01086** | [[STM-01086 BCC Pants 产品拉断测试（Pants 产品拉断测试方法）.doc]] |
| 派生来源 Lineage | **参考端封方法 STM-00078 修改参数** | 同上 |
| 夹具气压 Clamp pressure | **≤ 0.6 MPa** | 同上 |
| 夹具定位 Clamp mark | 沿芯体 **Insert 边缘向下 2 in** 划线 → 下夹具位置 | 同上 |
| 取样规则 Sampling | 按穿着方向标记前后端，**交替取样** | 同上 |
| 特殊品相 Special case | 带**丢弃贴**的品相沿用同一取样方式，不需单独处理 | 同上 |
| 装样 Orientation | 产品捋直、**底膜侧面朝操作者**、避免松弛 | 同上 |

> ⚠️ **口径提示（2026-09-29）**：STM-01086 与母方法 STM-00078 **夹具距离不同（3 in vs 2 in）**，同属 gf 峰值法族但**数值不可互比**，详见 [[峰值 gf 粘合强度方法族对比（端封 vs Pants 拉断 vs 面层压纹）]]、[[Seal Strength Test（端封·侧封强度测试）]]。
> 📌 **重复副本（2026-09-29）**：同一 SOP 在 `成品/` 与 `成品/Pants 产品拉断测试方法/` 两个目录下各存一份、正文一致，**不得计为两次独立证据**。

## Related Sources 关联来源

- [[CN 118369075 A（具有前后弹性腰带的胶粘吸收制品·宝洁）]]
- [[STM-00078 端封强度.doc]]
- [[STM-00090 腰围密封强度.doc]]
- [[STM-01086 BCC Pants 产品拉断测试（Pants 产品拉断测试方法）.doc]]
- [[STM-01086 BCC Pants 产品拉断测试（成品）.doc]]

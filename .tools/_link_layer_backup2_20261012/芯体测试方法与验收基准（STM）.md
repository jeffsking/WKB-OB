---
type: concept
title: "芯体测试方法与验收基准（STM）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-29
tags: [STM, 回渗, STT, Cradle, L-H, 验收基准, 试产, KPI]
---

# 芯体测试方法与验收基准（STM）

> 一句话定义：COCO V6 试产验收用的**测试方法编号体系（STM / TTM）与通过-优秀基准**——把"好不好"翻译成可复现的数字门槛，覆盖 Liner / REL / Core Wrap 三个部件与产品级回渗、STT、Cradle 摄入与扩散、L-H 等项目。

## 机理 / 结构拆解

1. **方法与基准是两件事**：**STM 编号**（如 STM-00059-2）锁定的是"怎么测"（设备、载荷、液量、时序）；**基准**锁定的是"多少算过"（Pass / Excellent）。两者必须成对引用，否则数字不可比。
2. **产品级主 KPI 是回渗（Rewet）**：STM-00059-2 Flowback，14±1 in WC（≈3.4 kPa）· 3 min + 2 min，门槛 **< 5.9 g / 34 min**。原文明确：**Liner 回渗须按低负载协议判定**——高负载短间隔法会掩盖真实穿着表现。
3. **STT（Strike-through，穿透时间）**：STM-2470（Lister，4×4 in，5 mL 盐水），产品级门槛 **≤0.8 s**。
4. **MD 分布 / 铺展**：STM 1001，30 s。基准分两档写法（见下），是本批**唯一出现跨版本冲突**的基准项。
5. **湿态 MD 抗张**：STM-00146（50.8×152.4 mm，76 mm 夹距，305 mm/min，60 psi），门槛 **≥75 N/m**。
6. **REL 专项**：空体积（TTM 000429 @0.05 psi，VV-Sat 曲线）、压缩回复（TTM 00038 / TTM 00437，3 循环厚度-应力）、STT 与第 3 次回渗（STM 00034）、克重（STM-00109，As-is 与绝干）。
7. **Core Wrap 专项**：规格与亲水等级（15–18 gsm SMS 或 tissue，L1 处理 / L5 标准）、SAP 隔离/抗迁移（Stage 2）、芯体级回渗与摄入（ISO 11950 或 EDANA）、MD 分布、端封/复合强度（STM-00078 Rev.7, 2024-12）。
8. **试产用的产品级测试项**：国标重量、国标 1st/2nd 吸收时间、国标回渗与渗漏、**Cradle 重量与 1st/2nd/3rd intake 及扩散长度**、**L-H（低-高负载）intake / Rewet / Residue / 扩散长度**、Surface moisture、Run off、FIFE intake、SAM density、Pad integrity、Mannequins（侧卧/俯卧/仰卧）扩散拍照。

## 关键参数表

| 部件 | 核心参数 | 方法 / 标准 | 通过-优秀基准 | 出处 |
|---|---|---|---|---|
| Liner | Rewet（产品主 KPI） | STM-00059-2 Flowback（14±1 in WC ≈3.4 kPa · 3 min + 2 min） | < 5.9 g / 34 min（产品级门） | [[COCO V6 试产原料准备会（v2 Final）]] |
| Liner | Strike-through (STT) | STM-2470（Lister，4×4 in，5 mL 盐水） | ≤ 0.8 s（产品级） | [[COCO V6 试产原料准备会（v2 Final）]] |
| Liner | MD 分布 / 铺展 | STM 1001，30 s | v2 Final：≥ +30%（目标 34.9%）／Summary：≥ +15%（目标 30%）⚠️ | [[COCO V6 试产原料准备会（v2 Final）]]、[[COCO V6 试产原料准备会（Summary 版）]] |
| Liner | 湿态 MD 抗张 | STM-00146（50.8×152.4 mm，76 mm 夹距，305 mm/min，60 psi） | ≥ 75 N/m | [[COCO V6 试产原料准备会（v2 Final）]] |
| REL | Void Volume | TTM 000429 @0.05 psi VV-Sat 曲线 | cm³/g @0.05 psi | [[COCO V6 试产原料准备会（v2 Final）]] |
| REL | 压缩回复 | TTM 00038 / TTM 00437，3 循环厚度-应力曲线 | TBC | [[COCO V6 试产原料准备会（v2 Final）]] |
| REL | 1st/2nd/3rd void STT、3rd void rewet | STM 00034 | ≤ 对照批 | [[COCO V6 试产原料准备会（v2 Final）]] |
| REL | 克重 | STM-00109（As-is 与绝干） | 名义 28 gsm（上 11.2 + 下 16.8） | [[COCO V6 试产原料准备会（v2 Final）]] |
| Core Wrap | 规格与亲水等级 | 克重 / 厚度法 | 15–18 gsm SMS 或 tissue（L1 处理 / L5 标准） | [[COCO V6 试产原料准备会（v2 Final）]] |
| Core Wrap | SAP 隔离 / 抗迁移 | SAP migration / isolation check（Stage 2） | v2 Final：≥90% 捕获 / 97% 迁移 <3%／Summary：≥98% 捕获 ⚠️ | [[COCO V6 试产原料准备会（v2 Final）]]、[[COCO V6 试产原料准备会（Summary 版）]] |
| Core Wrap | 芯体级回渗 / 摄入 | ISO 11950 或 EDANA | 回渗 ≤3.0 g（3rd void）；摄入 ≤35 s · 3 次冲击 | [[COCO V6 试产原料准备会（v2 Final）]] |
| Core Wrap | MD 分布 | STM 1001，30 s | ≥ 130 mm | [[COCO V6 试产原料准备会（v2 Final）]] |
| Core Wrap | 端封 / 复合强度 | STM-00078（Rev.7, 2024-12, 2-in gauge） | 峰值载荷 gf（记录最大 + 平均） | [[COCO V6 试产原料准备会（v2 Final）]] |

**试产实测输出项（CI-06 格式）**

| 组别 | 输出指标 |
|---|---|
| 国标 | 重量、1st/2nd 吸收时间、回渗、渗漏 |
| Cradle | 重量、1st/2nd/3rd intake、扩散长度 |
| L-H | 重量、L/H intake、L/H Rewet、L/H Residue、L-H 扩散长度 |
| 其他 | Surface moisture、Run off、FIFE intake、SAM Density、Pad integrity、Mannequins（侧/俯/仰）扩散拍照 |

> ⚠️ **禁止无来源参数**：STM 编号与基准值均来自本批准备会材料；**库内没有这些方法的完整操作规程原文**（只有编号与参数），标 `[待验证]`。

> ⚠️ **跨来源基准差异（2026-09-29，待人工确认）**：同一 2026-09-11 的两份材料对 **Liner MD 分布基准**（≥+30%/目标 34.9% vs ≥+15%/目标 30%）与 **Core Wrap SAP 隔离基准**（≥90% vs ≥98%）给出不同门槛，疑为草案→汇总的口径演进。**本页不裁决**，两值并列。

## 相邻概念

- 被验收对象：[[COCO芯体平台]]、[[ATB双梳理面层（Dual-Card Topsheet）]]、[[REL增强层]]、[[SAP错峰膨胀]]、[[ADL（导流层）]]
- 指标物理：[[SAP性能指标（CRC AUL GBP Vortex）]]、[[三叶形截面纤维（Trilobal Fibre）]]、[[毛细梯度设计]]
- 对比：[[芯包材料对比（LSN MPM vs PSN MPM）]]、[[COCO V6 Liner 方案对比（Code 1 vs Code 2-A vs Code 2-B）]]

## 经验教训

> ✅ 验证（2026-09-29，来源 [[CI-06 COCO V6 第三轮试产测试结果]]）：试产实际输出项与本页试产输出项清单**完全对应**（国标/Cradle/L-H/Surface moisture/Run off/FIFE/SAM Density/Pad integrity/Mannequins），方法体系描述与来源一致。

- **教训一**：**回渗要挑对协议**。原文明确高负载短间隔法会掩盖真实穿着表现，产品级判定须走低负载协议（STM-00059-2）。
- **教训二**：**跨批次比较前先对齐基准版本**。本批已出现同一日期两份材料基准不同的情况；引用门槛值时应写明来自哪一份。
- **待补 `[待验证]`**：STM/TTM 各方法的完整操作规程；Cradle 与 L-H 指标与产品级回渗的相关性；试产 MPM 20 gsm 相比规格 15–18 gsm 的适用性结论。


> ✅ 验证（2026-09-29，来源 [[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]]、[[STM-00034 FIFE Nanjing Edition（FIFE 吸收时间与溢出量·南京厂第5版）]]、[[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]]）：本批暴露**三类编号/版本治理问题**，引用时必须带版本号与厂别。① **版本**：China-STM-05 第 4 版（2020-02-26）新增 COCO V2 的 LSS/PSS × Diaper/Pants 四套步骤，而 WI-56234 收录的是第 2 版（2019-06-20），**两版不可混用**。② **同一编号不同档位**：STM-00034 FIFE 第 5 版在南京厂文件为 **50/65/80/100/100 mL**，与 WI-56234 同版次记录的 **35/50/65/80/100 mL** 错开一档（🔴 已标 manual_review）。③ **编号差一位**：动态假人参考方法 TTM-00313-8 vs 总表 TTM-00318-8 `[待验证]`。

## 追加：Open Innovation 批次（2026-09-29 追加）

> 本节为 **S4_Resources_Open Innovation_04 批次** 编译时的追加记录，**不改动上方既有结论**。新增来源是成人/女性护理（AFC）条线的 **STM-00497 草案**，补上了本页此前缺失的「**加压摄入**」方法族。

| Method 方法 | Scope 范围 | Key conditions 关键条件 | Source 出处 |
|---|---|---|---|
| STM-00497 Intake via Bladder Box（草案） | Adult & Feminine Care（Adult Care / Feminine Care） | 充气泡加压 **0.25 psi**；3 次冲击、间隔 15 min；流速 1 或 8 mL/s；回渗段 **0.7 psi / 25 mm / 2 min**；0.9% 盐水约 37 ℃ | [[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]] |

- **为什么是"缺失的一环"**：本页原有清单以 **COCO V6 婴儿线**（Cradle / L-H / STM-00059-2 等）为主，且多处强调「低负载协议」；STM-00497 证明**另一条产品线把压力显式写进了方法本身**——即常压/低压法会高估摄入能力。二者不是冲突，而是**不同产品线的不同失效工况**。
- **加液参数锁定的逻辑**：STM-00497 的单次冲击量取自 **ULS / HUT 的第 95 百分位总载量**，因此**不可跨品类套用**（女性护垫与成人失禁裤相差一个数量级）；这与本页既有教训「回渗要挑对协议」同向，只是把 protocol 的范围从压力扩展到了**加液量来源**。
- **状态提示 Status note**：该草案的 Table 1（精密度）为**空白模板**，故无可用的重复性与再现性数据；只能用于内部趋势判断，不能作为放行判据。

> ✅ 验证（2026-09-29，来源 [[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]]）：本页既有「**方法编号 + 基准必须成对引用**」的规则在本批再次被印证——STM-00497 同时给出方法二段压力（摄入 0.25 psi / 回渗 0.7 psi），若只写"膀胱箱回渗 2 min"而不带压力，数据不可比。既有结论未被修正。
> 📌 已派生新页 New derived page：[[Bladder Box Intake Test（膀胱箱压载摄入测试）]]（2026-09-29 建立）。

## 来源

- [[COCO V6 试产原料准备会（v2 Final）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_v2_Final.pptx.md`
- [[COCO V6 试产原料准备会（Summary 版）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_Summary.pptx.md`
- [[CI-06 COCO V6 第三轮试产测试结果]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/CI-06 COCO V6 3rd round trial.xlsx.md`
- [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/STM-00034 FIFE/BCC成品STM-南京南厂 1.pdf.md`
- [[Finished Product Testing Method Summary（成品测试方法汇总表）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/Finished Product Testing Method Summary.xlsx.md`
- [[Raw Material Testing Method Summary（原材料测试方法汇总表）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/Raw Material Testing Method Summary.xlsx.md`

> ✅ 验证（2026-09-29，来源 [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]]、[[Finished Product Testing Method Summary（成品测试方法汇总表）]]）：本批确认 STM/TTM 编号体系的**三条结构性事实**——① 编号族分 STM（QA 归口，可用于验收/放行）/ TTM（研发用，明言不用于验收）/ China-STM + 内控（中国区与厂内自定）；② 同一编号在两厂可能为不同版本（南京 WI-56234 Rev.8 vs 天津各方法独立版本）；③ 成品总表方法编号带版本后缀（如 STM-00034-4、TTM-00148-11），与 PDF 页眉的 Revision 体系不同。**引用门槛值必须写明厂别 + 版本来源**，与本页既有「跨批次比较前先对齐基准版本」教训一致。
- [[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/CoCo Product-REL Width, SAM Width in REL, LSS and PSS width China STM-05 20200303.pdf.md`
- [[STM-00034 FIFE Nanjing Edition（FIFE 吸收时间与溢出量·南京厂第5版）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-00034 FIFE.docx.md`

## Related Sources 关联来源

- [[BCC Pants Waist Break Study（Pants 产品拉断研究与两项新方法创建）]]
- [[Blizzard and ActiveTech Technologies（在线薄型无绒毛浆芯体技术）]]
- [[CI-06 COCO V6 第三轮试产测试结果]]
- [[COCO V6 试产原料准备会（Summary 版）]]
- [[COCO V6 试产原料准备会（v2 Final）]]
- [[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]]
- [[Diaper Market Claims and Marketing Concept Landscape（市场宣称与营销概念全景）]]
- [[FIUP Insult Amounts（FIUP 加液量阶梯与 TL 溯源）]]
- [[Finished Product Testing Method Summary（成品测试方法汇总表）]]
- [[GB-T 28004.1-2021 Absorption Tester SOP（国标吸收性能测试仪操作步骤）]]
- [[GBP（From Nuoer）.docx]]
- [[History of FIUP TTM-00643（FIUP 测试方法沿革史）]]
- [[IMA 知识库索引（2026-08-21）]]
- [[IMA 知识库索引（2026-09-18）]]
- [[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]]

---
type: concept
title: "尿液模拟液（Urine Analog）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-30
tags: [Urine Analog, 尿液模拟液, 胆盐, 渗漏测试, 吸收测试]
---

# 尿液模拟液（Urine Analog）

> 一句话定义：**模拟人尿成分与体温的测试液体**，用于假人/吸收/回渗等涉及"真实排泄"的卫品测试方法，使实验室结果逼近穿着场景。

## Definition 定义 / Principle 原理

卫品吸收/渗漏测试若用纯盐水，会丢失尿液中**表面活性剂（胆盐）**对 SAP 溶胀与液体铺展的影响。为此在生理盐水基础上加入**牛黄酸胆酸钠（sodium taurocholate）**等胆盐，并把液体加热至体温，以更真实地驱动芯体摄入与渗漏。

## 常见配方口径（Caliber）

| 参数 | 典型值 / 范围 | 出处 |
|---|---|---|
| 基础液 | 生理盐水（0.9% NaCl） | [[WI-63848 Static mannequin.docx]] |
| 胆盐添加 | 0.1 g 牛黄酸胆酸钠 / 1 L 生理盐水 | [[WI-63848 Static mannequin.docx]] |
| 搅拌 | 磁力搅拌 5–10 min | [[WI-63848 Static mannequin.docx]] |
| 温度 | 37 ± 1 °C（水浴） | [[WI-63848 Static mannequin.docx]] |

> ⚠️ **禁止无来源参数**：以上为单来源（WI-63848）口径；不同方法的模拟液配方（盐浓度、是否含尿素/缓冲）可能不同，跨方法比较须对齐配方，标 `[待验证]`。

## 相邻概念

- 应用方法：[[Static Mannequin Test（静态假人测试）]]、[[Mannequin BM Test（BM 假人测试）]]、[[Rewet Test（回渗测试）]]
- 平台：[[Mannequin Lab（Rockwell 假人平台）]]

## 经验教训

- **配方即口径**：胆盐浓度、温度直接改变 SAP 摄入行为，引用吸收/渗漏数据时必须注明所用模拟液配方。
- **待补 `[待验证]`**：本库尚未系统收录各方法的模拟液配方差异对照。


> ✅ 验证（2026-09-29，来源 [[GB-T 28004.1-2021 Absorption Tester SOP（国标吸收性能测试仪操作步骤）]]、[[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]]、[[TTM-00467 BM Mannequin Absorption NB-S2（BM 假人吸收测试）]]）：本批再确认**三支并存的液体口径，温度各不同**——① 国标吸收测试仪：**0.9% 生理盐水、36 ± 1 ℃**；② 假人（静态 WI-63848 / 动态 WI-63849）：**牛黄酸胆酸钠 0.1 g + 1 L 生理盐水、37 ± 1 ℃**（两法同配方同温，可互认）；③ BM 假人 TTM-00467：**BM simulant A 400 mL（Normal）或 3:1 兑盐水 Runny、22 ± 1 ℃**。**BM 支的 22 ℃ 与尿液支的 36–37 ℃ 相差约 15 ℃，黏度与吸收速率均受影响，跨方法引用须标明液体与温度。**

## 来源

- [[WI-63848 Static mannequin.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/WI-63848 Static mannequin.docx.md`
- [[Raw Material STM - Tianjin Mill WI-60632（原材料标准测试方法-TJ）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM原材料-TJ.pdf.md`
- [[STM-00429 Void Volume as a Function of Saturation（方法正文）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/STM-00429 VOID VOLUME AS A FUNCTION OF SATURATION.pdf.md`
- [[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/Material/TTM-00038 Compression Test for Absorbent .pdf.md`

> ✅ 验证（2026-09-29，来源上述三份）：本页原「各方法模拟液配方差异对照」的缺口已部分补齐——**0.9% 盐水的明文配比为 18 ± 0.1 g NaCl + 蒸馏水至总重 2000 ± 1 g**（天津厂）；STM-00429 要求 **0.9 ± 0.005%（w/w）且自配后静置 ≥ 4 h**；TTM-00038 允许 **0.9–2.0 wt%（曾用到 20%）**。**新增事实**：成品 FIFE 类方法统一在盐水之外加**亮蓝食品级染料**（0.1 g 定容 100 mL，取 4 mL 加入 1 L 盐水），而国标法与 VV 法不强制染色。
- [[GB-T 28004.1-2021 Absorption Tester SOP（国标吸收性能测试仪操作步骤）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/GBT28004.1-2021纸尿裤国标吸收性能测试仪操作步骤.doc.md`
- [[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/WI-63849 Motion mannequin.docx.md`
- [[TTM-00467 BM Mannequin Absorption NB-S2（BM 假人吸收测试）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/BM测试方法/TTM-00467 BM Mannequin Absorption NB-S2.docx.md`

## Related Sources 关联来源

- [[BM simulant A配方 & BM gun操作.docx]]
- [[Elastic Tension Visualization Technology Assessment（拉力松紧可视化技术评估）]]
- [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]]
- [[REL 结构优化与选材技术方案]]
- [[Raw Material STM - Tianjin Mill WI-60632（原材料标准测试方法-TJ）]]
- [[Rewet Method Parameter Matrix (xlsx)（回渗测试方法参数矩阵·11 方法）]]
- [[STM-00034 FIFE - Fluid Intake Flowback Evaluation Rev.5（FIFE 摄入-回渗评价全球方法）]]
- [[STM-00429 Void Volume as a Function of Saturation（方法正文）]]
- [[STM-00429 Void Volume vs Saturation Template（孔隙体积-饱和度曲线计算模板）]]
- [[TTM-00038 Compression Test for Absorbent（吸收体压缩测试）]]
- [[TTM-00467 BM Mannequin Absorption NB-S2（BM 假人吸收测试）]]
- [[WI-63848 Static mannequin.docx]]
- [[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]]

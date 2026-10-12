---
type: comparison
title: "锑测试方法：ICP-MS vs ICP-OES（检出限·成本·适用性）"
subjects: ["[[锑（Antimony, Sb）测试方法三口径：可迁移·消解·燃烧]]", "[[Antimony-Free PET Fibre（无锑 PET 纤维）]]"]
dimension: 综合
updated: 2026-09-29
tags: [ICP-MS, ICP-OES, 检出限, 锑, 无锑, 检测成本]
---

# 锑测试方法：ICP-MS vs ICP-OES（检出限·成本·适用性）

## 对比维度表

| 维度 Dimension | ICP-OES（电感耦合等离子体发射光谱） | ICP-MS（电感耦合等离子体质谱） | 依据 Basis |
|---|---|---|---|
| 精度 / 检出限 Precision | **PPM 级**（发射光谱法） | 可达 **1 ppm 及以下**（质谱，数据稳定性最好） | [[Antimony-Free PET Fibre Compliance Strategy Meeting（无锑合规策略会·录音纪要 2026-07-10）]] |
| 能否覆盖 10 ppm 判定 | **可以**：10 ppm level 的结果可信 | 可以（能力过剩） | 同上 |
| 能否覆盖 ≤1 ppm 判定 | **不可以**（精度不足） | **必须用它** | 同上 |
| **成本 Cost** | **低**（会上判断「费用应该也不会特别高」）；适合 ongoing 常规监控 | **高**（会上明确「MS 的检测方法比较贵」）；适合目标收紧到 1 ppm 后的判定与仲裁 | 同上 |
| 数据稳定性 Data Stability | 够用于 10 ppm 级判定 | **最稳定**（会上口径：测重金属时 ICP-MS 数据最稳定） | 同上 |
| 可委托性 Availability | SGS 可测 | SGS 可测（两种都能测） | 同上 |
| 样品前处理耦合 | 与**微波消解**（硝酸 + 硫酸 / 王水，密闭微波，溶出接近 100%）配套，得到 ≈总含量 | 同左；**检出限越高要求，前处理的污染控制越关键**（取样避免 ziplock/铝膜等引入污染） | 同上 |
| **供应链风险 Supply Chain Risk** | **低**：方法普及、周期短，供应商易自行送检，适合**高频摸底与切换期监控** | **中**：费用与周期更高，若直接定为唯一方法，会抬高供应商合规成本、拉长切换验证周期；但**不指定它则无法支撑 ≤1 ppm 的远期目标** | 同上（含会上关于「时长和费用」待询的安排） |
| 适用场景 Application | 现行目标 **≤10 ppm（消解法）** 的日常判定与摸底 | 下一阶段目标 **≤1 ppm（完全无锑）**、争议仲裁、客户/法规要求低检出限时 | 同上 |

> 尾注 Footnote：本表所有结论均来自 [[Antimony-Free PET Fibre Compliance Strategy Meeting（无锑合规策略会·录音纪要 2026-07-10）]]（`RAW/ima_sync/个人知识库/WKB/Areas/Regulation&PSC/录音纪要_260710100449.md`，中文 ASR 转写，**credibility 低**）。会上未给出具体金额与检测周期数字（明确为待询价事项），故本表**不填金额**；「费用低/高」为**相对定性**表述。

## 各自适用场景

- **ICP-OES**：目标为现行 **≤10 ppm（消解法，FZ/T 50057-2022 口径 `[待验证]`）**时的主力方法 —— 覆盖足够、成本低、周期短，适合先「摸底」再决定是否收紧。
- **ICP-MS**：目标收紧到 **≤1 ppm（完全无锑）**、或客户/法规要求低检出限、或出现跨实验室争议需要仲裁时使用。

## 结论

**检出限决定仪器，仪器决定成本**：10 ppm 用 ICP-OES、1 ppm 用 ICP-MS。项目推进上应先以 ICP-OES 完成供应商摸底（会上做法），同时把「将来收紧到 1 ppm 必须换 ICP-MS」写进路线图 —— 否则会用廉价方法得出「全部合格」的假象，在目标升级时集中暴露。

> 🔴 **manual_review（2026-09-29）**：来源含供应商能力承诺与无锑 up-charge 量级（约 +500 元/吨），属商务敏感，**不在本页展开**。

## 来源

- [[Antimony-Free PET Fibre Compliance Strategy Meeting（无锑合规策略会·录音纪要 2026-07-10）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Regulation&PSC/录音纪要_260710100449.md`
- [[锑（Antimony, Sb）测试方法三口径：可迁移·消解·燃烧]]（方法口径上位页）
- [[Antimony-Free PET Fibre（无锑 PET 纤维）]]（既有概念页，检出限相关经验教训）

---
type: concept
title: "Mechanochromic变色纤维"
domain: [卫材研发, 智能功能化, 材料]
status: growing
updated: 2026-09-30
tags: [Mechanochromic, 力致变色, 液晶弹性体, 可机洗, 应变可视化]
aliases: ["Mechanochromic 变色纤维（力致变色纺织材料）"]
---

# Mechanochromic 变色纤维（力致变色纺织材料）

> 一句话定义：在外加机械应变下改变颜色的纤维/织物材料，可实现**应变的可视化**（如拉伸变色）；本库作为 Projects/Mechanochromic 项目方向的技术基础。

## 机理 / 结构拆解

1. **技术路线**：光子晶体结构变色、液晶弹性体（LCE）取向变色、染料-聚合物体系受力构象变化变色。已报道的突破方向为**可机洗的液晶弹性体变色纤维**（Nature Materials 系报道），使布料自带应变可视化能力。
2. **卫生用品相关性**：可对应「穿戴张力/贴合指示」——尿液或体位变化引起弹性侧片拉伸，通过力致变色提供视觉反馈（K-C US7704589B2 拉伸变色专利已失效，说明该方向有早期探索与 FTO 空间）。
3. **与热致变色的分工**：热致变色（温敏）用于湿态指示（尿温触发）；力致变色（力敏）用于贴合/张力指示——二者可组合成多信号织物。
4. **工程约束**：耐水洗性、循环疲劳寿命、色牢度、与一次性制品成本的匹配。

## 关键参数表

| 参数 | 内容 | 出处 |
|---|---|---|
| 代表突破 | 可机洗液晶弹性体变色纤维（Nature Materials） | [[智能尿裤功能层专利地图]]（引用） |
| 相关早期专利 | K-C US7704589B2（拉伸变色，**已失效**） | [[智能尿裤功能层专利地图]] |
| 相关技术 | MET 电子织物、PDMS-CLCE 光子弹性体 | [[智能尿裤功能层专利地图]] |
| 应用映射 | 穿戴张力/贴合指示（油墨遮罩于弹性侧片） | [[智能尿裤功能层专利地图]] |

## 相邻概念

- 材料家族：[[变色油墨]]
- 应用载体：[[智能尿裤功能层]]
- 项目目录：`raw/ima_sync/个人知识库/WKB/Projects/Mechanochromic/`（待编译）
- 2026-09-29 追加：[[Active Diagnostic Zones（主动诊断分区）]]、[[Printable Pressure-Activated Inks vs Covalent Mechanophores（力致变色两条落地路线）]]、[[Mechanophore Mechanochromism（机械力致变色分子）]]、[[Chromism Taxonomy（变色现象分类）]]

## 经验教训

> ⚠️ 本页为 seed 状态：主来源为 [[智能尿裤功能层专利地图]] 中的引用，**Projects/Mechanochromic 目录（5 份）尚未编译**，编译后应补全本页并回填源路径。

> ✅ 验证（2026-09-29，来源 [[Active Hygiene Roadmap（力致变色材料商业化路线图）]]，批次 S1_Projects_Active Hygiene_01）：本页「力致变色 → 穿戴张力/贴合指示」的定位被一份**商业化路线图**推进到可执行层面，新增三条量化/结构化结论——① **分区落点**：Zone 1 腰围耳贴（拉力超安全生理阈值即显色，防勒伤）与 Zone 3 体表压力分布热点；② **力值缺口**：工业力色团需 **40,000 PSI**，而卫材目标区间仅 **20–150 kPa**，须靠「stabilization bridge」（集成胶凝剂，如 gelatin）把阈值下移，激活曲线标注约 **25–27 % 应变**；③ **两条产业化路径**：可印刷压力激活油墨（offset/flexo，最快上市，借食品接触级油墨作监管护盾）vs 共价力色团（键合到聚合物主链，自评估材料 + 永久 IP 护城河）。本页既有结论未被修正，属**补充**（详见 [[Active Diagnostic Zones（主动诊断分区）]]、[[Printable Pressure-Activated Inks vs Covalent Mechanophores（力致变色两条落地路线）]]）。
> ⚠️ 该路线图可信度为**低**（无数据溯源、原文自标 NotebookLM 辅助、图为 OCR 残片），且其**面向婴儿的安全合规四项为源文声明、无检测报告**，一律标 `[待验证]`。

- **要点**：力致变色与热致变色是**互补而非替代**的信号机制，产品设计时应先确定「要指示什么物理量」再选机制。

> ✅ 验证（2026-09-29，来源 [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]]、[[Mechanochromic Materials Technical Review（EN v3, 2026-08）]]、[[Chromic Materials Bibliography（变色材料书籍·温湿力精表）]]）：本批已把 Projects/Mechanochromic 目录的 4 份资料编译入库。**本页既有结论未被改写**，仅追加编译追记：本页第 2 条「穿戴张力/贴合指示（油墨遮罩于弹性侧片）」已获完整实现细节支撑——该方向被工程化为**几何光学掩膜**（刚性遮光热熔胶覆盖弹性层压件自身波纹，TRL 8、无限循环、成本指数 1.0×），详见 [[Geometric Optical Mask（几何光学掩膜）]]；本页第 1 条列举的「光子晶体结构变色、液晶弹性体（LCE）取向变色」在卫品语境下被评估为**工艺不可及**（蛋白石需加热辊间振荡剪切、胆甾相需平面取向 + UV 固化），详见 [[Structural Colour Mechanochromism（结构色力致变色）]]。**新增相邻概念**：[[Mechanophore Mechanochromism（机械力致变色分子）]]、[[Chromism Taxonomy（变色现象分类）]]。

- **编译追记（2026-09-29）**：本页原「待编译」状态**已解除**；原 4 条要点（技术路线 / 卫生用品相关性 / 与热致变色的分工 / 工程约束）与新增来源**一致**——尤其第 3 条「力致变色与热致变色互补而非替代」在 [[Chromism Taxonomy（变色现象分类）]] 中被提升为分类学判据（先定要指示的物理量，再选机制）。
- **编译追记 `[待验证]`（2026-09-29）**：本页原引用的「可机洗液晶弹性体变色纤维（Nature Materials）」那份资料**不在本批 6 份内**（`跨界科技早读…md`），仍待编译，其独立源摘要页尚未建立。
- **2026-09-29 追加要点（材料细目）**：路线图给出四种候选机理与各自战略优势——**HPC**（黏弹性格点间距变化 → 压缩蓝移，红→蓝；可食/无毒/可降解，被称战略黄金标准，理由是**充当即时监管护盾**）、**Naphthopyrans**（共价键断裂 → 模块化变色；合成可达性与稳定性最优）、**Spiropyrans**（6π 电环化开环 → 强显色；**热致瞬态**）、**Cu-based HCP**（杂化配位聚合物发射位移 → 发光位移；受环境污染物影响小）。此外原文强调**可逆性是贴合监测的硬要求**（HPC 结构色提供可预测的幂律关系），而瞬态信号适合事件记录。出处同上。

## 来源

- [[智能尿裤功能层专利地图]] —— `raw/ima_sync/个人知识库/WKB/智能尿裤功能层专利地图.md`
- 待编译：`raw/ima_sync/个人知识库/WKB/Projects/Mechanochromic/跨界科技早读 _ 一拉变色、可机洗！Nature Materials突破：可机洗的液晶弹性体变色纤维，让布料自带应变可视化.md`

**编译追记来源（追加，2026-09-29）**

- [[Stretch-Triggered Colour Indicator for Diaper Pant Side Panels]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Stretch-Triggered Colour Indicator for Diaper Pant Side Panels.pptx.md`
- [[Mechanochromic Waistband Tension Indicator Proposal（2026-08-19）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Mechanochromic_Waistband_Tension_Indicator_Proposal_2026-08-19.pptx.md`
- [[Mechanochromic Materials Technical Review（EN v3, 2026-08）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Mechanochromic_TechReview_EN_v3_2026-08-02_fixed.pptx.md`
- [[Chromic Materials Bibliography（变色材料书籍·温湿力精表）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/变色材料书籍_温湿力精表.xlsx.md`
- 派生新页（追加，2026-09-29）：[[Geometric Optical Mask（几何光学掩膜）]]、[[TB-A Opaque Mask Hot Melt（TB-A 遮光热熔胶）]]、[[Mechanophore Mechanochromism（机械力致变色分子）]]、[[Structural Colour Mechanochromism（结构色力致变色）]]、[[Panel Hysteresis and Threshold Calibration（面板回滞与阈值标定）]]、[[Skin Contact Pressure（皮肤接触压力）]]、[[Chromism Taxonomy（变色现象分类）]]、[[Mechanochromic Routes Comparison（力致变色技术路线对比）]]、[[Kimberly-Clark（金佰利）]]
- [[Active Hygiene Roadmap（力致变色材料商业化路线图）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Active Hygiene/Active_Hygiene_Roadmap.pptx.md`（2026-09-29 追加）

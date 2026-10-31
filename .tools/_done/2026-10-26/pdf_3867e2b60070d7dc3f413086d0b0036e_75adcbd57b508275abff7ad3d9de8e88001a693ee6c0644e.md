---
type: source
title: "Baymax Brazil Dam 花型面层样品矩阵（2026-10-14 抽样总结）"
source_type: 研报
source_path: RAW/ima_sync/个人知识库/WKB/Projects/Baymax/Summary of Brazil Dam liner sampling in Chuanyue.pdf.md
original_link: ""
date_published: 2026-10-14
date_processed: 2026-10-26
credibility: 高
credibility_note: "KC 内部 Project Baymax 试验总结（署名 Tingting Du，2026-10-14，标注 Kimberly-Clark Confidential），为一手试验数据与目视判读结论。文字层由 pypdf 抽取（6 页 / 6,861 字符）；PDF 以图示为主，部分版面信息未进入文字层，实际样品照片需回看原件。"
knowledge_update_status: done
key_claims:
  - "**8 个 Code 的对照试验推翻了两条直觉**：① 偏心（eccentric）纤维对 3D 立体效果的贡献在本轮试验中**不显著**（Code 2 vs 5 无显著差异）；② 下层纤维旦数从 3D 提到 6D 也**无显著差异**（Code 4 vs 5）—— 意味着『换更粗/更特殊的纤维来买立体感』这条路在 30 gsm 档位不成立"
  - "**唯一显著有效的是克重**：40 gsm（Code 3）的 3D 效果最好；20 gsm 配偏心纤维反而出现纤维分布不匀，可能**反噬** 3D 效果；30 gsm 配偏心纤维的纤维分布与常规 20 gsm TABCW 相当"
  - "**复合强度排序：Bico > 低熔点 PP > 普通 PP**；但 TABCW 与普通 PP 的复合强度也可接受，且三者 3D 效果无显著差异 → 底层的选择可由成本/工艺决定，不必为强度付溢价"
  - "**工艺约束（可直接落到设计规格）**：因面层 necking，无法保证每边 3 个 Dam，实际只有 2 个 Dam → **面层宽度应按 90 mm 设计**（而非 82 mm）"
  - "样品矩阵本身是可复用的 DOE 骨架：上层 2D 半亲水 / 下层 6D 偏心全亲水为主轴，变量分离为『克重 20/30/40』『下层纤维 3D/6D/6D 偏心』『底层 Bico/低熔点 PP/普通 PP/TABCW 4D 18gsm』『三叶草截面 vs 4D Bico』四组"
pages_linked: ["[[热风无纺布]]", "[[纺粘 Spunbond]]", "[[ES 纤维 ES Fiber]]", "[[ES 双组分弹性纤维热风布（弹性体改性）]]", "[[Nonwoven Lamination]]", "[[ES 纤维驻极研究]]", "[[Baymax T4 Vista 卷样取样总结（2026-10-14）]]"]
compile_mode: semantic
---

# Baymax Brazil Dam 花型面层样品矩阵（2026-10-14 抽样总结）

## 一句话定位 Positioning

Project Baymax 在传越（Chuanyue）的一轮**面层花型（Brazil Dam Liner pattern）材料组合筛选**总结。价值不在于"又做了一轮打样"，而在于它用 8 个 Code 把"3D 立体感到底由什么决定"这个问题做了一次**变量分离**，并给出两个否定性结论（偏心纤维无效、旦数升级无效）和一个肯定性结论（克重才是主变量）。可直接复用于下一轮 DOE 的设计骨架，也可直接落到面层宽度规格（90 mm）。

A screening DOE on Brazil Dam liner pattern materials at Chuanyue: 8 codes isolating basis weight, fibre denier, eccentric fibres, and bottom-layer bonding type. Two counter-intuitive variables (eccentric fibre, denier upgrade) proved insignificant; basis weight was the only significant driver of 3D effect; laminate strength ranked Bico > low-melt PP > normal PP, all acceptable.

## 摘要 Summary

样品结构统一为双层：上层（82 mm × 259 mm）+ 底层（80 mm × 259 mm），底层为主 10 gsm 全亲水（个别 Code 用 TABCW 4D 18 gsm）。主轴组合是"上层 50% 2D 半亲水 + 下层 50% 6D 偏心全亲水"。

8 个 Code 的变量分配：Code 1/2/3 = 同结构下克重 20/30/40 gsm；Code 4 = 下层改 3D（非偏心）；Code 5 = 下层改 6D（非偏心）；Code 6 = 40 gsm + 底层换 TABCW 4D 18 gsm；Code 7 = 上层降为 10 gsm 2D、下层升为 20 gsm 6D（验证"下层占比提高能否增强 3D"）；Code 8 = 40 gsm + 底层改 Bico。另设 Code 2-A：30 gsm，上层 15 gsm（10% 三叶草截面 + 90% 2D Bico PE/PET），下层 15 gsm（50% 三叶草截面 + 50% 4D Bico PE/PET），验证三叶形截面的贡献。

结果：40 gsm（Code 3）3D 效果最好；20 gsm 配偏心纤维出现纤维分布不匀，可能负面影响 3D；30 gsm 配偏心纤维的分布与常规 20 gsm TABCW 相当。偏心纤维对 3D 的贡献不显著（Code 2 vs 5）；下层旦数 3D→6D 也无显著差异（Code 4 vs 5）。复合强度排序 Bico > 低熔点 PP > 普通 PP，但 TABCW 与普通 PP 亦可接受，三者 3D 效果无显著差异。工艺侧发现面层 necking 导致每边只能保证 2 个 Dam，故面层宽度应改为 90 mm。

## 提炼的数字与结论 Key Numbers

| 项目 | 数值 / 结论 | 备注 |
|---|---|---|
| 样品尺寸 | 上层 82 × 259 mm；底层 80 × 259 mm | 建议面层改 **90 mm**（necking 后仅 2 Dam/边） |
| 克重档位 | 20 / 30 / 40 gsm（上层） | 40 gsm 3D 效果最佳 |
| 底层 | 10 gsm 全亲水（主）；TABCW 4D 18 gsm（Code 6） | |
| 主纤维组合 | 上层 50% 2D 半亲水 + 下层 50% 6D 偏心全亲水 | |
| 偏心纤维贡献 | **不显著**（Code 2 vs 5） | 本轮回合否定 |
| 旦数 3D→6D | **不显著**（Code 4 vs 5） | 本轮回合否定 |
| 20 gsm + 偏心 | 纤维分布不匀，可能负面影响 3D | 低克重不宜配偏心 |
| 30 gsm + 偏心 | 分布与常规 20 gsm TABCW 相当 | |
| 复合强度排序 | Bico > 低熔点 PP > 普通 PP | TABCW 与普通 PP 亦可接受 |
| 3D 效果 vs 底层类型 | 三种底层无显著差异 | 底层可按成本选 |
| Code 数 | 8 + Code 2-A（三叶草截面验证） | 可复用 DOE 骨架 |

## 关键论断（key_claims）

- **3D 立体感的主变量是克重，不是纤维特殊性**：40 gsm 才出现明显 3D；换偏心纤维或升旦数都不显著 —— 支撑页：[[热风无纺布]]
- **低克重配偏心纤维会反噬**：20 gsm 时纤维分布不匀，对目视 3D 有负面影响 —— 这是"材料升级不等于效果升级"的具体反例 —— 支撑页：[[ES 纤维 ES Fiber]]
- **底层复合方式可按成本优化**：三种底层 3D 无差异、强度虽以 Bico 最优但普通 PP 可接受 —— 支撑页：[[Nonwoven Lamination]]
- **面层宽度须按 90 mm 设计**：necking 使实际 Dam 数从 3 降到 2，这是可直接写进图纸的工艺结论 —— 支撑页：[[Baymax T4 Vista 卷样取样总结（2026-10-14）]]

## 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Projects/Baymax/Summary of Brazil Dam liner sampling in Chuanyue.pdf.md`
- 原件：`RAW_FULL/ima_sync/个人知识库/WKB/Projects/Baymax/attachments/Summary of Brazil Dam liner sampling in Chuanyue.pdf`（1,204,776 B / 6 页）
- 原文链接：（内部文件，无外链）

> 🔒 密级：Kimberly-Clark Confidential（Project Baymax）。本页含未公开的材料组合与试验结论，仅内部使用。

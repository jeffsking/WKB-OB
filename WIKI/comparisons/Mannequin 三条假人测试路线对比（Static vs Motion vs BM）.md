---
type: comparison
title: "Mannequin 三条假人测试路线对比（Static vs Motion vs BM）"
subjects: ["[[Static Mannequin Test（静态假人测试）]]", "[[Motion Mannequin Test（动态假人测试）]]", "[[Mannequin BM Test（BM 假人测试）]]"]
dimension: 综合
updated: 2026-09-29
tags: [假人测试, WI-63848, WI-63849, TTM-00467, 漏尿, 合身性, 模拟液, 口径]
---

# Mannequin 三条假人测试路线对比（Static vs Motion vs BM）

## 对比维度表 Comparison Matrix

> 必含「成本」与「供应链风险」两列。三条路线**共用 Rockwell 假人平台**，差异在运动脚本、模拟液与输出指标。

| 维度 Dimension | 静态 Static（WI-63848） | 动态 Motion（WI-63849，第 0 版 2024-02-20） | BM 假人（TTM-00467，第 0 版 2021-02-28） | 依据 Source |
|---|---|---|---|---|
| 回答的问题 Question | 穿着姿态下的**吸收与漏尿** | 运动后的**漏尿位置 + 合身性变化** | **便液（BM）**的滞留与可视化 | [[Static Mannequin Test（静态假人测试）]]、[[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]]、[[TTM-00467 BM Mannequin Absorption NB-S2（BM 假人吸收测试）]] |
| 模拟液 Simulant | **0.1 g 牛黄酸胆酸钠 + 1 L 生理盐水** | 同上（**与静态版同配方**） | **BM simulant A 400 mL（Normal）**；Runny 为 **3:1 兑盐水，350 rpm × 30 s** | 同上 |
| 液温 Temperature | **37 ± 1 ℃** | **37 ± 1 ℃** | **22 ± 1 ℃** | 同上 |
| 注液 Insult | 15 mL/s；体积按型号 | **70 mL @ 15 mL/s**，时序含 Crawl 30.0 | 盐水 **40 / 40 / 45 mL @ 4.1 mL/s** + BM **11 mL @ 20 mL/s** | 同上 |
| 加载 / 压力 Loading | 姿势 Sitting / Prone / Side；工作站延迟 **10 s** | 运动脚本（Insult → Crawl → Loop → Insult 30 s） | **10 ± 1 英尺水柱**（同文件步骤 8 又写作 10 **英寸**，内部冲突 `[待验证]`）；穿着位置 **13.9 / 20 / 24.3 mm** | 同上 |
| 校准 Calibration | 液体 **± 3%**；管路 MASTERFLEX L/S **Tube 17 ± 1%** | 液体 **70 mL ± 3%**；管路 **17 ± 1%**（校准值接近 0.8/1.2 须手动校泵） | 未给出同口径校准条款 `[待验证]` | 同上 |
| 输出 Output | 漏点 **17 区** | 漏点 **17 区** + **六项合身性**（前后各测一次取差值）；Tab Spacing **19–38 mm** | BM 滞留量四项输出（公式见源文件） | 同上 |
| **成本 Cost** | **中**：平台固定投入高、单次运行成本低；润洗 300 mL 液体不可复用，耗材为经常性支出 | **中—高**：同平台，但需 Study Manager 脚本与更长周期时间（Crawl + Loop 多轮），**单片工时显著高于静态** | **中**：需自行配制 BM 模拟液（350 rpm × 30 s）与专用加载工装，**配方与工装均为额外成本** | 同上 |
| **供应链风险 Supply chain risk** | ① **平台与耗材单点依赖**：MASTERFLEX L/S Tube 17、牛黄酸胆酸钠属特定规格；② 仅厂内具备，**委外不可得** | ① 与静态版同源风险；② 脚本参数绑定具体假人型号（Koopa / Yoshi / Mario / Luigi / Kirby 的 Tab Spacing 各异），**换型即需重新设定** | ① **BM simulant A 完整配方仅见于内部文件** `[待验证]`，外部复现困难；② **温度口径 22 ℃ 与另两条 37 ℃ 相差约 15 ℃**，跨方法数据不可互比，委外或供应商比对时易产生争议 | 同上 |
| 适用场景 When to use | 常规产品吸收/漏尿评价、多型号横向对比 | 结构变更验证（腿围、耳贴、腰围）、**只在运动中暴露的失效**（LegGap、Ear Roping、下坠） | 便液相关宣称验证、可视化取证 | 同上 |

> 尾注 Footnote：本表所有数字均来自 [[Static Mannequin Test（静态假人测试）]]、[[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]]、[[TTM-00467 BM Mannequin Absorption NB-S2（BM 假人吸收测试）]] 三份源摘要页；含 `[待验证]` 者为单一来源、库内无第二来源交叉印证。

## 各自适用场景 Application Scope

- **静态 Static（WI-63848）**：**主力普查方法**——用可控的「人工排泄」替代主观穿戴评价，把渗漏定位到 17 个解剖位置，适合常规型号对比与放行。
- **动态 Motion（WI-63849）**：**结构验证方法**——只有运动才会暴露的腿围间隙、耳贴束绳、前后下坠；合身性读数是**运动前后的差值**，不是绝对值。适合结构/材料变更后的验证。
- **BM 假人（TTM-00467）**：**专项方法**——面向便液（BM）的滞留与可视化，温度与液体口径自成一支，**不与尿液路线共用判据**。

## 结论 Conclusion

三条路线**共用平台与 17 区漏点体系，但液体、温度、注液口径三要素各自独立**：静态与动态可互认液体与管路校准（同为 0.1 g 牛黄酸胆酸钠 + 1 L 盐水、37 ± 1 ℃、±3% / ±1%），而 BM 支为 **22 ± 1 ℃ + BM simulant A**，属完全独立口径。**跨路线引用数值前，必须先核对液体与温度。**

## 来源 Sources

- [[Static Mannequin Test（静态假人测试）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/WI-63848 Static mannequin.docx.md`
- [[WI-63849 Motion Mannequin（动态假人漏尿性与合身性测试）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/WI-63849 Motion mannequin.docx.md`
- [[TTM-00467 BM Mannequin Absorption NB-S2（BM 假人吸收测试）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/BM测试方法/TTM-00467 BM Mannequin Absorption NB-S2.docx.md`

## 关联页面 Related

- 平台：[[Mannequin Lab（Rockwell 假人平台）]]
- 试剂：[[尿液模拟液（Urine Analog）]]
- 相邻方法：[[Run-off & Leakage Test（滑渗与渗漏测试）]]、[[Rewet Test（回渗测试）]]、[[Cradle Intake Test（Cradle 摄入测试）]]
- 上位索引：[[芯体测试方法与验收基准（STM）]]

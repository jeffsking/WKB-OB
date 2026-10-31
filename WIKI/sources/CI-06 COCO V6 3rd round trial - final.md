---
type: source
title: "CI-06 COCO V6 3rd round trial - final.xlsx"
source_type: 报价单
source_path: RAW/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/CI-06 COCO V6 3rd round trial - final.xlsx.md
source_paths:
  - RAW/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/CI-06 COCO V6 3rd round trial - final.xlsx.md
  - RAW/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/CI-06 COCO V6 3rd round trial-10.10.xlsx.md
  - RAW/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/CI-06 COCO V6 3rd round trial-9.30.xlsx.md
original_link: ""
date_published: 2026-09-30
date_processed: 2026-10-27
credibility: 高
credibility_note: "内部试产原始数据（Lab data form，每 Code n=5，含 adv/Std），非二手转述；但『厚度』列全表 #DIV/0!、Code 4/16/17 数据空缺，且 Test Result 为多版本迭代定稿（9.30 → 10.10 → final），三份快照已合并于本页。"
knowledge_update_status: done
key_claims:
  - "最终定稿版把 COCO V6 第三次试产（2026-09-21~09-30，Pad 长 382 mm，中间加 bonding）17 个 Code 与 4 个对照臂的数据全部并表，共 10 张工作表；相较 9.30/10.10 两份中途快照，本版首次含完整 Lab data form 与芯吸高度实测"
  - "唯一『换变量单因子』对照是 Code 14：对 Control-2 仅调胶型/胶量（3.5×4 mm 亲水胶），成品级结论是**净权衡而非净收益** —— 国标一次吸收 24.10 s vs 25.66 s（−6.1%）、二次 25.03 vs 28.67（−12.7%）、L 回渗 0.147 vs 0.195 g（−24.4%）、L/H 残留 −85%/−82%，但**渗漏 0.650 vs 0.466 g（+39.5%）**、Cradle 三次吸入 57.58 vs 39.68 s（+45.1%）、L/H 吸入时间 +24.9%/+22.1%"
  - "Code 3（Yanjan Code 1 三叶异形 50 gsm 面层）是全表唯一在**扩散长度**上大幅胜出的臂：Cradle 扩散 241.6 mm vs Control-2 205.0 mm（+17.9%），代价是回渗翻倍 0.99 vs 0.492 g、侧向吸入 10.36 vs 7.77 s"
  - "原材料级芯吸高度给出四条候选的排序（10 s / 30 min）：王金三叶草 68.7/168.6 mm ＞ Control LSN 61.6/125.4 ＞ Unikorn 9.7/64.7 ＞ Control PSN 12.2/17.7 —— LSN 为纵向主通道、PSN 基本不爬升，说明**亲水/毛细能力高度集中在面层而非支撑层**"
  - "目标克重口径被写死：135 Pad 总重 21.44–22.82 g（LSN 200/PSN 155/REL 140/胶 137.5/SA P 15.5），110 Pad 总重 22.12 g（PSN 130/REL 115/胶 125）；USL/LSL 按 ±0.5 g 控制"
  - "Code 1（亲水胶 3.5×4）与 Code 2（亲水胶 2×4）的差异几乎只在胶量：回渗 0.322 vs 0.440 g、Cradle 三次 29.43 vs 33.21 s —— 胶量加倍（3.5 vs 2 mm 宽）换来回渗降 27%，是本文对『胶量—回渗』唯一直接的剂量证据"
pages_linked: ["[[REL增强层]]", "[[亲水整理 Hydrophilic Finish]]", "[[毛细芯吸 Capillary Wicking]]", "[[Hydrophilic SAP Wrapping Adhesive（亲水SAP包裹胶）]]", "[[延江（Yanjan）]]", "[[诺尔（Nuoer）]]"]
compile_mode: semantic
---

# CI-06 COCO V6 3rd round trial - final.xlsx

## Positioning 一句话定位

The consolidated, self-contained data book of COCO V6's third pilot round: **17 codes × 10 worksheets**, turning a trial plan into a comparable dataset (code matrix → target weights → lab results → wick heights). Its value is that it is the **only place where all four control arms and all material-level measurements sit in one file** — and it shows, on the one single-variable comparison available (Code 14 vs Control-2), that the change is a **net trade-off, not a gain**.

本页是 COCO V6 第三次试产的**总账本**：17 个 Code × 10 张表，把试产计划变成可横向比较的数据集（编码矩阵 → 目标克重 → 实验室实测 → 芯吸高度）。其价值在于它是**唯一把四个对照臂与全部原材料级测量放在同一文件里**的地方——并且在唯一可用的单因子对比（Code 14 vs Control-2）上给出「**净权衡而非净收益**」的结论。

## Trial Design 试产设计

| 项 Item | 设定 Setting |
|---|---|
| Pad 长度 Pad length | 382 mm（两种规格：110 Pad / 135 Pad） |
| 编码数量 Codes | Code 1–17 + Control-1 / Control-2（Code 4/16/17 数据缺失） |
| 固定项 Fixed | LSN Control-38g、PSN Control-26g、REL Control-40g、LSS/PSS add-on 7.75 g |
| 可变项 Variables | 胶型与胶量、面层（Liner）、PSN 材料（610/950/混配）、LSN 材料（Unikorn/王金） |
| 测试日 Test days | 2026-09-21 ~ 09-30（逐日收样，详见 Daily Plan） |

**Code 矩阵读法**：Code 1 = 亲水胶 3.5×4；Code 2 = 亲水胶 2×4；Code 3/4 = 以 Control-2 为基座换面层（Yanjan Code 1 / 传越 Code 2）；Code 7–10 = PSN 换 610/950/混配；Code 13 = LSN 换 Unikorn；Code 14 = 以 Control-2 为基座、胶 3.5×4；Code 17 = 换 PSN 宽度与胶宽。

## Head-to-Head Compare 单因子对照（Code 14 vs Control-2）

> 这是全表**唯一**「只改一件事」的对照：胶型/胶量 3.5×4 mm 亲水胶 vs Control 结构胶，其余全同。n=5/5。

| 指标 Metric | Code 14 | Control-2 | Δ | 判读 Read |
|---|---|---|---|---|
| 国标一次吸收 GB 1st intake (s) | 24.10 | 25.66 | −6.1 % | ↑ better |
| 国标二次吸收 GB 2nd intake (s) | 25.03 | 28.67 | −12.7 % | ↑ better |
| 国标回渗 GB rewet (g) | 0.500 | 0.492 | +1.6 % | = flat |
| **国标渗漏 GB leakage (g)** | **0.650** | **0.466** | **+39.5 %** | **↓ worse** |
| **Cradle 三次吸入 (s)** | **57.58** | **39.68** | **+45.1 %** | **↓ worse** |
| L 吸入时间 (s) | 9.70 | 7.77 | +24.9 % | ↓ worse |
| H 吸入时间 (s) | 17.93 | 14.68 | +22.1 % | ↓ worse |
| L 回渗 (g) | 0.147 | 0.195 | −24.4 % | ↑ better |
| L 残留 (g) | 0.015 | 0.100 | −85.0 % | ↑ better |
| H 残留 (g) | 0.010 | 0.055 | −81.8 % | ↑ better |
| Pad 重量 (g) | 36.34 | 36.51 | −0.5 % | 可比 |

**Verdict 判读**：retention 与 lower-body rewet 显著改善（残留 −82~−85%、L 回渗 −24%），但 leakage（+39.5%）与 late-insult intake（+22~45%）同步恶化 —— **material-level 的收益没有在产品级兑现**。且本次同时动了两个变量（供方 + 克重）、收样日期相差 7 天，不可归因为单一因素。

## Code 3 vs Control-2 面层单换（Source: Lab data form）

| 指标 | Code 3（Yanjan Code 1 三叶 50 gsm） | Control-2 | Δ |
|---|---|---|---|
| Cradle 扩散长度 (mm) | **241.6** | 205.0 | **+17.9 %** |
| Cradle 三次吸入 (s) | 53.36 | 39.68 | +34.5 % |
| 国标回渗 (g) | 0.990 | 0.492 | **+101 %** |
| 侧向吸入时间 (s) | 10.36 | 7.77 | +33.4 % |
| Pad 重量 (g) | 37.00 | 36.51 | +1.3 %（可比） |

> 扩散换回渗：三叶异形沟槽把液体沿 MD 摊开（+17.9%），代价是回渗翻倍。**回渗是这条路线真正的门槛**。

## Wick Height 原材料级芯吸高度（新增数据）

| 材料 Material | 10 s (mm) | 5 min (mm) | 30 min (mm) |
|---|---|---|---|
| Control LSN（38 g） | 61.6 | 109.5 | 125.4 |
| Control PSN（26 g） | 12.2 | 15.9 | 17.7 |
| Unikorn LSN（200 mm） | 9.7 | 51.1 | 64.7 |
| 王金三叶草 LSN | **68.7** | **137.2** | **168.6** |

**判读**：LSN 承担纵向毛细主通道（30 min 爬升 125–169 mm），PSN 几乎不爬升（17.7 mm）。Unikorn 的 10 s 值仅 9.7 mm 但 30 min 达 64.7 mm，**起效慢、后劲足**——与「瞬时就差」的直觉判断相反，属延迟润湿型。

## Target Weight 目标克重口径

| 规格 Spec | 组成 Composition | 总重 Total | LSL / USL |
|---|---|---|---|
| 135 Pad（Code 11 胶 2×4） | LSN 200 / PSN 155 / REL 140 / 胶 137.5 / SAP 15.5 | 22.50 g | 21.38 / 23.63 |
| 135 Pad（Code 13/14/17） | LSN 200 / PSN 155 / REL 140 / 胶 137.5 | 22.18–22.46 g | — |
| 110 Pad | LSN 200 / PSN 130 / REL 115 / 胶 125 | 22.12 g | 21.01 / 23.23 |

## Data Gaps 数据缺口

- `厚度` 列全表 `#DIV/0!`（未测或未填）→ 本页不含厚度结论。
- Code 4 / 16 / 17 的 Lab data form 为空（未测或未收样）。
- `Surface Moisture` 与 `Run off` 仅 Control-1/2 与 Code 1/2 有值，覆盖面不足以横向比较。

## Version History 版本迭代

| 快照 Snapshot | 内容 Content | 处理 Handling |
|---|---|---|
| `...-9.30.xlsx` | 试产计划 + 早期编码矩阵 | 已并入本页（`source_paths`），原页转 `status: merged` 指针 |
| `...-10.10.xlsx` | 中期数据（部分 Code） | 同上 |
| `...- final.xlsx`（本页主件） | 全 17 Code + 4 对照 + 10 表定稿 | 主件 |

## Links 关联

- 项目主线：[[REL增强层]]
- 机理与材料：[[亲水整理 Hydrophilic Finish]] · [[毛细芯吸 Capillary Wicking]] · [[Hydrophilic SAP Wrapping Adhesive（亲水SAP包裹胶）]] · [[SAP 吸水纸（SAPP）]]
- 供方：[[延江（Yanjan）]] · [[诺尔（Nuoer）]]

## Source 来源

- 原件：`RAW_FULL/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/attachments/CI-06 COCO V6 3rd round trial - final.xlsx`（4,199,914 B，10 工作表）
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/CI-06 COCO V6 3rd round trial - final.xlsx.md`（`extract_status: ok`，openpyxl `data_only=True`）
- 取件通道：通道 B `get_media_info` → 签名 URL 直下原件（**不吃 `get_doc_content` 日配额**）
- media_id：`excel_3867e2b60070d7dc3f413086d0b0036e_134d2034e11e4eaad653496442cc172d001a693ee6c0644e`
- 锚点说明：`source_path` 为**预期路径**（插件连续两日未落盘），次日须复核插件实落名；不符按三处同步修正，勿新建重复页。

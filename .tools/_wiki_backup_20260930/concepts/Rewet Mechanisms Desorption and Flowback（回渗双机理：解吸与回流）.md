---
type: concept
title: "Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）"
domain: [卫材研发, 回渗, 摄入系统]
status: seed
updated: 2026-09-29
tags: [回渗, rewet, desorption, flowback, 摄入系统, 机理]
---

# Rewet Mechanisms Desorption and Flowback（回渗双机理：解吸与回流）

> 一句话定义 One-line definition：回渗（rewet，受压后返回皮肤/吸墨纸的液量）由两条**物理通路**构成——**Desorption 解吸**（摄入系统内部滞留的液体被压出）与 **Flowback 回流**（已润湿芯体中未锁住的液体返逃）。两者**治理抓手不同**：前者改材料与界面，后者改容量与隔离。

## 机理 / 结构拆解 Mechanism and Structure

1. **Desorption 解吸通路**：液体被困在摄入系统（面层 liner / 导流层 surge 及其界面）的孔隙与"小口袋"中，受压时释放。治理抓手是**让摄入材料不拉住、不滞留液体并促使排空**——降低亲水性、打开粘合花型（减少滞留小口袋）、改用非纤维/开孔结构、提高毛细连通性与单向流。
2. **Flowback 回流通路**：芯体已吸收但未充分锁住的液体，在压力下从湿芯体返逃。治理抓手是**容量与隔离**——在需要的时间与位置提供足够容量（capacity / zoning / speed）、用缓冲层与单向流把自由液锁住，并使芯体中未锁住的液体与皮肤/吸墨纸**分离**（separation from core）。
3. **回渗设计原则三支柱**（源自 GRIFFIN 问题陈述）：① 摄入材料 discourage pulling/trapping fluid、encourage draining（毛细/粘附、孔隙网络连通性）；② 有足够且及时可得的容量 fully lock up fluid（容量、分区分布、速度、单向流、缓冲）；③ 未锁住的液体与皮肤/吸墨纸隔离（分区/分离）。
4. **机制会随方案迁移**：ATACAMA+ 阶段回渗主因在 surge 与摄入层界面；修复后，Post-SIROCCO 阶段液体积聚点转移到 liner。因此每轮迭代都要**重新定位积聚点**，不能沿用上一轮的主攻层。
5. **与高低压机理的关系**：本页的 desorption/flowback 是**通路分类**，[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]] 是**压力条件分类**，二者正交；同一产品在不同压力下可能由不同通路主导。

## 关键参数表 Key Parameters

| 参数 Parameter | 典型值 / 范围 Typical Value | 出处 Source |
|---|---|---|
| 回渗目标（GRIFFIN 立项） | ≤0.15 g（closed cradle） | [[GRIFFIN Rewet Technical Problem Statement（GRIFFIN 回渗技术问题描述 · 2025-01-31）]] |
| 当前 DPU 回渗 | 0.25 g | 同上 |
| 竞品对标 Always Discreet | 0.18 g（SIROCCO 期 0.16–0.18 g） | 同上 |
| ATACAMA+ 前基线 | 约 1.6 g | 同上 |
| 摄入系统滞留治理抓手 | 更开放粘合花型（oval 18% → CD Rod 10%）、降低亲水剂（Lertisan 0.65% → 0.3% / 0%）、非纤维开孔膜（22 gsm TS3） | 同上 |
| 界面治理抓手 | 面层-导流层压花（liner-surge embossing, LSE） | 同上 |

> ⚠️ **禁止无来源参数 No unsourced numbers**：表中数字均来自上列源摘要页；解吸能量（desorption energy）的定量口径见 [[Capillary Pressure Method（毛细压力法·解吸毛细压力与解吸能量）]]。各通路在不同压力下的贡献占比库内暂无来源，标 `[待验证]`。

## 相邻概念 Adjacent Concepts

- 上位 / 相关：[[Rewet Test（回渗测试）]]、[[Intake System（摄入系统）]]、[[Residual Fluid & Pore Stranding（残液与孔隙滞留）]]、[[Dryness Measure System（干爽度量三分）]]
- 压力口径：[[LPR vs HPR Rewet（低压回渗 vs 高压回渗机制）]]、[[MCCT Multi-Component Capillary Tension（多组分毛细张力测试）]]
- 工艺落点：[[Liner-Surge Embossing（面层-导流层压花）]]、[[Surge-Liner Adhesive Bonding（导流层-面层施胶粘合）]]、[[ADL（导流层）]]、[[亲水-疏水梯度设计]]
- 容量侧：[[Gel Blocking（凝胶阻塞）]]、[[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]]
- 项目：[[GRIFFIN Rewet Program（GRIFFIN 超低回渗项目）]]、[[IPC BCC OI Portfolio（开放创新项目组合）]]

## 经验教训 Lessons

> ✅ 验证（2026-09-29，来源 [[GRIFFIN Rewet Technical Problem Statement（GRIFFIN 回渗技术问题描述 · 2025-01-31）]]）：ATACAMA+ 与 SIROCCO 两段项目史互证了「解吸通路主导 → 修复后积聚点迁移」的判断；SIROCCO 的失败（surge 方案与摄入互斥）进一步说明**单攻一条通路会与摄入性能冲突**。

- **教训一（同轮验证）**：改 surge 必须同轮测摄入（intake），否则会出现「回渗改善、摄入变差」的结构性互斥——SIROCCO 即因此未在时间窗内成功。
- **教训二（对比口径）**：AT Hybrid 早期回渗偏高但代码缺 LSE，与 ATACAMA 的成功方案不构成同条件对比；跨芯体类型比较前必须补齐工艺变量。
- **教训三（playbook 需改写）**：从 SAM/fluff 芯体转到 ActivTech 混合芯体时，部分机理可迁移，但需为新型芯体改写打法（"adapt the playbook for this new core type"）。
- **待补 `[待验证]`**：两条通路在同一压力下的定量贡献拆分；liner 侧 4 条假设（粘合花型 × 亲水剂）的试验结果。

## Evidence Update 证据追加（2026-09-29 · 竞品物性）

> ✅ Verification（2026-09-29，source 来源 [[Rewet Competitive Analysis - Depend vs Always Discreet Intake System（回渗竞品分析 · 2025-09-11）]]）：**解吸通路的驱动量得到修正**——AD 面层/导流层与 Depend 的最可几孔径相当，孔径本身不解释解吸能差异；AD 解吸能更低（8.26E+03 vs 1.23E+04）源于**导流层克重显著更低**（49.95 vs 76.97 gsm）。**界面间隙被确认为独立变量**：AD 层压剥离载荷更高且平滑，Depend 呈粘滑剥离，提示 Depend 界面间隙更大。
>
> 新增可操作杠杆（原文四条建议）：① 降低 Depend 面层润湿性；② 提高孔径分布单分散性（连通性假设 `[待验证]`）；③ 降 surge 克重同时保持摄入速度；④ 用其他手段减小面层/导流层界面间隙。
>
> 新增明确权衡：**压力粘合面层与导流层可改善回渗，代价是孔隙体积与渗透率下降**。

## Evidence Update 证据追加（2026-09-29 · STEC 设计原则脚本）

> ✅ Verification（2026-09-29，source 来源 [[2025.10.03 - STEC 2025 - Rewet Design Principles Script.docx]]）：Kerry Clemmer 演讲稿以**双通路归因表述**复证本页框架——"Desorption comes from the intake system where small pockets of fluid are trapped"（解吸来自摄入系统截留的小液袋）；"Flowback comes from the core where fluid isn't fully locked up"（回流来自芯体未锁住的液体）。六条设计原则的结构化拆分：**原则 1–4 属芯体侧**（capacity + SAM），**原则 5–6 将摄入系统定位为 buffer**；解吸侧六因素 = 前三项毛细作用 + 两项组分间液体交接（handoff）+ 一项生产波动。与上方 GRIFFIN 三支柱结论一致，不构成修改。

## Evidence Update 证据追加（2026-09-29 · 摄入材料变量 scoping 草案）

> ✅ Verification（2026-09-29，source 来源 [[Rewet Materials Study - Draft for initial scoping discussions 0.7.17.25.pptx]]）：Clemmer 草案确立了「**主动围绕摄入材料设计建回渗数据**」的试验纲领，范围聚焦研究不足的 **bodyside liner 与 topical surge**（传统 under-liner surge 已充分研究）。变量矩阵三块：BSL-Spunmelt（SB/dSB/SMS、12 vs 20 gsm、bond pattern Oval 18%/CD Rod 10%/Open dot、润湿处理、柔软化学）、BSL-TABCW（denier、PE/PP vs PE/PET vs PE/PET eccentric loft、亲疏水组合、finish）、Topical surge（40/50/60 gsm、底层 denier 4/6/12d、亲疏水 × apertured）。**重要方法论事实：GRIFFIN 未看到 bond area 18% vs 10% 的差异，但 MOJAVE 提示可能与低/高回渗相关**——支持本页「机制随方案迁移」的既有判断；测试采用 closed cradle + low/high rewet 双口径。

## 来源 Sources

- [[GRIFFIN Rewet Technical Problem Statement（GRIFFIN 回渗技术问题描述 · 2025-01-31）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/GRIFFIN Rewet/Updates/2025.01.31 - GRIFFIN Rewet.pptx.md`

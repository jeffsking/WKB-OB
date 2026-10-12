---
type: concept
title: "ATB双梳理面层（Dual-Card Topsheet）"
domain: [卫材研发, 无纺布结构]
status: seed
updated: 2026-09-29
tags: [ATB, 穿透热风粘合, 双梳理, Topsheet, Z梯度, MD沟槽, 三叶形纤维]
aliases: ["ATB 双梳理面层（Dual-Card Topsheet）"]
---

# ATB 双梳理面层（Dual-Card Topsheet）

> 一句话定义：用**两套梳理系统、四层铺网**叠成的穿透热风粘合（ATB）面层结构——把「贴肤柔软」与「芯体侧 MD 沟槽导流」两件互相拉扯的事，通过**分层配比**而不是整层换料来解决。

## 机理 / 结构拆解

1. **"双梳理"= 两套独立梳理系统**：上下各一套梳理分别成网，再叠合后进入穿透热风烘箱（ATB）粘合。好处是**上下层可以配不同的纤维组合与克重**，而不必在同一梳理里迁就。
2. **分层配比（COCO V6 口径）**：总 50 gsm = 上层 25 gsm + 下层 25 gsm
   - 上层（贴肤面）：22.5 gsm 90% ES 2D 圆形 + 2.5 gsm 10% 三叶形 PE/PET 3D；
   - 下层（芯体面）：12.5 gsm 50% ES 4D + 12.5 gsm 50% 三叶形 PE/PET 3D。
3. **Z 梯度设计意图**：贴肤侧以圆形 ES 为主 → **手感软**；越往芯体侧三叶形占比越高 → **形成 MD 方向的沟槽网络**（三叶形的凹槽沿机向引液）。整体三叶形 15 gsm（30%），但**皮肤侧仅 5%**，以"保手感"。
4. **导流机理**：三叶形截面的凹槽为液体提供**沿 MD 的低阻通道**，把冲击点液体沿机向铺开，降低局部 SAP 饱和度 → 回渗与凝胶阻塞同步改善。详见 [[三叶形截面纤维（Trilobal Fibre）]]。
5. **与 ADL 的分工**：ATB 面层承担的是面层侧"摄入 + 初铺展"，与 [[ADL（导流层）]] 的"临时储液 + 横向铺展"功能相邻但不同层；COCO V6 的 OI-20 路线曾"移除 ADL"，把铺展职责更多压到面层沟槽与 REL 上。
6. **量产约束**：三叶形纤维的**供给量**直接决定能否上机——COCO V6 的 Code 2-B（上层去三叶形）就是"视异型纤维样本量"的降级方案。

## 关键参数表

| 参数 | 典型值 / 范围 | 出处 |
|---|---|---|
| 结构 | 4 铺层 / 2 梳理系统（ATB 穿透热风粘合） | [[COCO V6 试产原料准备会（v2 Final）]] |
| 总克重 | 50 gsm（上 25 + 下 25） | [[COCO V6 试产原料准备会（v2 Final）]] |
| 上层配比 | 22.5 gsm 90% ES 2D + 2.5 gsm 10% 三叶形 PE/PET 3D | [[COCO V6 试产原料准备会（v2 Final）]] |
| 下层配比 | 12.5 gsm 50% ES 4D + 12.5 gsm 50% 三叶形 PE/PET 3D | [[COCO V6 试产原料准备会（v2 Final）]] |
| 三叶形总占比 | 15 gsm（30%），**皮肤侧仅 5%** | [[COCO V6 试产原料准备会（v2 Final）]] |
| MD 分布增益（模型） | v2 Final 记 +30%；Summary 记 +15% ⚠️ | [[COCO V6 试产原料准备会（v2 Final）]]、[[COCO V6 试产原料准备会（Summary 版）]] |
| CD 拉伸 | 9.3 N/50mm（下限 8.0 N @600 m/min） | [[COCO V6 试产原料准备会（v2 Final）]] |
| 实测基重（Yanjan Code 1） | 45.222 gsm（标称 50） | [[CI-06 COCO V6 第三轮试产测试结果]] |
| 实测 STT / 层间剥离 / pH | 0.874 s / 115.276 N / 7.112 | [[CI-06 COCO V6 第三轮试产测试结果]] |
| OI 项目对应 | OI-25 Liner Nonwoven Development（ATB dual-card 50 gsm；30% trilobal MD grooves） | [[IPC BCC OI 项目清单 2026 v2（2026-09-17）]] |

> ⚠️ **禁止无来源参数**：MD 分布增益在两份同日期来源中不一致（+30% vs +15%），**本页不取舍**，两值并列；库内暂无 ATB 双梳理的**产线速度-粘合强度**曲线，标 `[待验证]`。

## 相邻概念

- 关键原料：[[三叶形截面纤维（Trilobal Fibre）]]、[[皮芯复合纤维]]
- 工艺载体：[[热风粘合无纺布]]
- 相邻层：[[ADL（导流层）]]、[[REL增强层]]
- 平台：[[COCO芯体平台]]、[[分区密度设计]]
- 验收：[[芯体测试方法与验收基准（STM）]]

## 经验教训

> ✅ 验证（2026-09-29，来源 [[IPC BCC OI 项目清单 2026 v2（2026-09-17）]]）：官方 OI 清单把该结构正式立项为 **OI-25（In progress, high）**，其一句话简述"ATB dual-card 50 gsm；30% trilobal MD grooves"与本页设计口径完全一致，**未出现矛盾**。

- **要点**：双梳理的价值是**让"手感"与"导流"解耦**——分层配比替代整层选料，比"换一种纤维"更可控。
- **风险**：**三叶形纤维的供给量是上机前提**，异型纤维短缺会直接触发 Code 2-B 降级方案（上层去三叶形）。
- **待补 `[待验证]`**：MD 分布增益的实测值（本批产品级数据未覆盖 Code 3/4 面层替换组）；ATB 烘箱温度/风速窗口对 50 gsm 双梳理层压强度的影响。

## 追加：Liner 项目批（2026-09-29 追加）

> 本节为 **Liner 项目批（批次 S1_Projects_Liner_01，5 份资料）** 编译时的追加记录，**不改动上方既有结论**。上方的 COCO V6 口径（50 gsm = 25 + 25、整体三叶形 30%、皮肤侧 5%、分层解耦手感与导流）在本批仍成立；本节补充的是**另外三种构造口径**（25 gsm 双梳理、45 gsm 四给料、25 gsm + 纺粘层压）以及**工艺与转化窗口**。

### 1. 本批新增的构造口径（三种，并列登记）

| 构造 | 总克重 | 分层与配比 | 出处 |
|---|---|---|---|
| **A · 25 gsm 双梳理（五角星形路线）** | 25 gsm | 上层固定 12.5 gsm 2D ES；下层 10.0 gsm 4D ES + 2.5 gsm 3D 星形 PET（**星形仅在芯体侧**） | [[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]] |
| **B · 45 gsm 双梳理 / 四给料（三叶形路线）** | 45 gsm | A1 12 gsm 100% ES 2.2 dtex（贴肤，0% PET）/ A2 13 gsm 75% ES + 25% 三叶形 3.3 dtex / B1 10 gsm 60% ES 4.4 + 40% 三叶形 3.3 / B2 10 gsm 55% ES 4.4 + 45% 三叶形 2.2；合计三叶形 11.75 gsm = **26%** | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| **C · 25 gsm ATB + 12 gsm 双组分纺粘层压（超声 3D 花型）** | 25 + 12 gsm | ATB 网 60% 2D ES + 25% 4D 偏心 ES + 15% 2D 圆角三叶形单组分 PET；Card A 贴肤侧 ≈16 gsm、Card B 层压侧 ≈9 gsm | [[ATB Topsheet with Bico Spunbond for 600 mpm Ultrasonic Lamination]] |

### 2. 本批新增的工艺 / 转化参数

| 参数 | 数值 / 范围 | 出处 |
|---|---|---|
| 双梳理职责解耦 | 第 1 梳理低牵伸（MD/CD≈2:1）保 CD 拉伸与横向完整性；第 2 梳理高牵伸（≈4:1）换 MD 芯吸 | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 烘箱风温 | 现状 132–136 → 含 PET 构造 138–142 ℃；停留 +10–15%；风速 1.2–1.5 → 1.4–1.8 m/s | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 张力 / 冷却 / 分切 | 压网张力降 10–15%；卷绕前强制冷却；刀片改碳化物/陶瓷、换刀频次 +30–40% | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 梳理环境 | 55–65% RH、22–25 ℃；PET 与 ES 分别预开松、在喂料槽混合（**不在打包机混合**） | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| 幅宽监控 | 过烘箱收缩 >1–2% ⇒ PET 热定型不足，须停线改规格 | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| ES 占比硬约束 | 直纺单组分异形 PET 场景下保持 ES ≥80 wt%（目标 ≈85 wt%）；单组分 PET 起始不超 20 wt% | [[ATB Topsheet with Bico Spunbond for 600 mpm Ultrasonic Lamination]]、[[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]] |
| 纺粘层克重窗口 | <10 gsm 操作性与花型支撑差 · 12 gsm 推荐 · >14 gsm 偏硬且穿透变慢 | [[ATB Topsheet with Bico Spunbond for 600 mpm Ultrasonic Lamination]] |
| 面层 DOE 的固定因子 | 50 gsm（25+25）、异形纤维 3.0D、ES 2D/4D、耐久亲水、ATB 粘合（**不升温**） | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| 面层 DOE 的温度窗口 | 126 / 128 / 130 ℃ × 低/高载荷；PE 皮层约 130 ℃ 流动是扁平化风险的锚点 | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |

### 3. 验证记录

> ✅ 验证（2026-09-29，来源 [[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]]、[[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]]、[[ATB Topsheet with Bico Spunbond for 600 mpm Ultrasonic Lamination]]、[[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]]）：本页既有判断——「双梳理的价值是让手感与导流解耦」「三叶形供给量是上机前提」——在本批**被进一步支持并一般化**：四份来源在 25 / 45 gsm 两种克重、星形/三叶形/圆角三叶形三种截面上**独立采用同一解法**（贴肤层 0% 异形纤维 + 芯体侧集中导流纤维 + 两张梳理不同牵伸）。原页的"分层配比替代整层选料"判断**未被修正**。

- **追加要点一（口径扩表）**：本库现有**四种** ATB 双梳理/分层构造口径（COCO V6 50 gsm、Liner 25 gsm、Liner 45 gsm 四给料、Liner 25+12 gsm 层压），互相不可直接换算，引用时必须带克重与层压条件。
- **追加要点二（工艺随配方走）**：引入不可粘的单组分 PET 后，**烘箱温度、停留、风速、张力、冷却、刀片**须整体重调；只调温度会牺牲蓬松度。
- **追加 `[待验证]`**：本批构造的**实测** MD 铺展、CD 拉伸与回渗数据（现有全部为模拟或设计值）；25+12 gsm 层压构造的超声封合强度实测。

## 追加：OI 直属文件批（2026-09-29 追加）

> 本节为 **S1_Projects_(直属文件)_02 批次（5 份 OI 资料）** 编译时的追加记录，**不改动上方既有结论**。本批补充的是 **OI-25 面层方案的官方定稿口径与验收矩阵**。

### 1. 官方定稿口径（2026-09-16 / 09-18）

| 项 | 内容 | 出处 |
|---|---|---|
| 方案收敛 | 面层由 **Code 1 / Code 2-A / Code 2-B 三选一 → 收敛为 Code 1（50 gsm）单一方案**；试验选择维度由 3 项（面层×SAP×包覆）降为 2 项；REL 改为单选项直采、不进矩阵 | [[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]] |
| 结构 | ATB 双层 PE/PET bico 面层 · **总 50 gsm · 4 铺层 / 2 梳理系统** | [[IPC BCC OI Project List 2026-09-18（重构版·19 项）]] |
| 铺层 | A1 90% ES 2D 22.5 gsm ／ A2 10% 三叶形 PE/PET 3D 2.5 gsm（上）；B1 50% ES 4D 12.5 gsm ／ B2 50% 三叶形 PE/PET 3D 12.5 gsm（下） | 同上、[[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]] |
| 三叶形占比 | **30%（15 gsm）；贴身侧仅 5%**；Z 梯度 MD 沟槽网络 | 同上 |
| 实测 / 模型 | CD 拉伸 **9.3 N/50 mm**（底线 8.0 N @600 m/min）；MD 扩散**模型 +15%**（目标 30%） | 同上 |
| 卷材规格 | 102 mm × >100 m，3" 纸芯，卷径 ≤700 mm；2026-09-18 天津上机 | 同上 |
| 验收判据（STM） | 回渗 <5.9 g @34 min（STM-00059-2 Flowback）｜1st STT ≤0.8 s（STM-2470）｜MD 扩散 ≥+15%，目标 30%（STM 1001）｜湿态 MD 拉伸 ≥75 N/m（STM-00146） | [[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]] |
| 供应链 | 成网 + 2D/4D ES = Yanjan；三叶形 = Fudy；LSN 水刺莱赛尔三叶形 = WangJin（6 km，卷径 ≤700 mm） | [[IPC BCC OI Project List 2026-09-18（重构版·19 项）]] |
| 法务 / IP | 项目不在 OI 原表，无编号/无 POC/无法务编号；建议**挂靠 OI-07 异形纤维专利**，作为其实施例数据源 | [[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]] |

### 2. 验证记录

> ✅ 验证（2026-09-29，来源 [[IPC BCC OI Project List 2026-09-18（重构版·19 项）]]、[[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]]）：本页既有构造口径（双梳理 / Z 梯度 / 贴肤层低三叶形）**被官方定稿方案支持**；本批新增的是**方案收敛结论**（三候选 → Code 1 单一方案）与**完整验收矩阵**。与 OI-08（三叶形莱赛尔，纤维级）经 09-16 口径定性为**上下游**关系，非重复立项。
> ⚠️ **知识缺口（源内明示）**：面层 ATB 双层梳理**无织物结构级专项资料**（现有知识仅覆盖纤维级与整机工艺）；**无成本数据**（50 gsm 方案 vs 常规面层的克重与成本差异未核算，三叶形纤维单价、双梳理系统效率均缺）。

- **追加 `[待验证]`**：MD 扩散增益存在 09-11（+30%）与 09-16（+15%）两版，依大纲 §6.4 裁定以 **9/16 版（+15%，目标 30%）** 为准；50 个图片位素材在本批同样**为 0 张**。

## 来源

- [[COCO V6 试产原料准备会（v2 Final）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_v2_Final.pptx.md`
- [[COCO V6 试产原料准备会（Summary 版）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Coco_V6_Trial_Raw_Materials_Summary.pptx.md`
- [[Coco V6 试产原料清单（Raw material list v3.0）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Raw material list for Coco V6 trial.xlsx.md`
- [[IPC BCC OI Project List 2026-09-18（重构版·19 项）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/IPC BCC OI Project List - 20260918 (Restructured).xlsx.md`（2026-09-29 追加）
- [[IPC BCC OI 材料开发团队 2026 年度汇报大纲 v7（2026-09-17）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/IPC BCC OI 材料开发团队 2026 年度汇报大纲_v7_红白配色与标题栏加倍版.md.md`（2026-09-29 追加）
- [[IPC BCC OI 项目清单 2026 v2（2026-09-17）]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/IPC_BCC_OI_Project_List_2026_v2_EN_20260917.pptx.md`
- [[CI-06 COCO V6 第三轮试产测试结果]] —— `RAW/ima_sync/个人知识库/WKB/Projects/COCO/Test Result/CI-06 COCO V6 3rd round trial.xlsx.md`
- [[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/pentagram_PET_diaper_liner_deep_dive 1.pptx.md`
- [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/Trilobal_PET_Liner_MD_Distribution.pptx.md`
- [[ATB Topsheet with Bico Spunbond for 600 mpm Ultrasonic Lamination]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/ATB_topsheet_600mpm_ultrasonic_8slides.pptx.md`
- [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/KC_Diffusion_Enhanced_Topsheet_v3.xlsx.md`

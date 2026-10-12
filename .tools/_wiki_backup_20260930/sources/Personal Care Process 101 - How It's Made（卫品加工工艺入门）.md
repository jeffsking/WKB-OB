---
type: source
title: "Personal Care Process 101 - How It's Made（卫品加工工艺入门）"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Products/Personal Care Process 101 - How its Made.pptx.md
original_link: ""
date_published: 2025-09
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "文件性质 = K-C 内部培训教材（2025-09，Joe Sina & Hwa Kim），目标是让工程师理解卫品加工（converting）的基本工序、术语与「同一目标有多种工艺解」的事实"
  - "十段式知识框架 Ten topics：Process Flow → Web Handling → Air Systems → Bonding/Laminating → Cutting → Applying Components → Folding → Electrical System → Putting it all together → Appendix"
  - "MD vs CD 是产线构型的第一分野：MD（Machine-Direction，纵向）为「头对头/端对端」制造，约 1970s 起；CD（Cross-Direction，横向）为「并排/侧挨侧」制造，约 1990s 起，弹性侧围以连续卷材在线送入"
  - "芯体成型靠气流 Air-laid core forming：SAM 输送计量 → 绒毛浆输送与纤维化 → 气流成型（可折叠）→ 脱蓬与裁切；**绒毛浆与 SAM「跟着气流走」，因此可用成型网做出形状、分区（pocketed screen 3D / zoning segment 2D）与通道**"
  - "胶黏剂是主力 Hot melt first：热熔胶用得最多，可粘接异质材料、固化快、成本低；三种施加方式为 Slot（接触式狭缝）、Spray（非接触喷涂）、Strand（橡筋股线涂布）"
  - "四种粘合/复合工艺 Four bonding routes：Pressure（压力，仅冷流非晶区）、Thermal（热粘合，熔点相近材料最佳）、Embossing（压花，带刻意间隙）、Ultrasonic（超声波，20–40 kHz，靠迟滞生热，可熔化结晶区）"
  - "超声波的代价 Ultrasound price：能量足以快速熔化聚合物的非晶与结晶两相，但**投资与维护成本高于热粘合与压力粘合**，且 horn 与驱动电子对热、压力与自身状态敏感"
  - "裁切方式 Cutting：直刀与打孔（Straight-Knife & Perf）、模切（Die Cutting，成形）、水切（Water Cutting，成形）、分切（Slitting）、切断（Chopping）"
pages_linked: ["[[Pressure vs Thermal vs Ultrasonic Bonding（压力·热·超声波粘合对比）]]", "[[Ultrasonic Bonding of PET-Containing Topsheet]]", "[[Hot-Melt Slot Coating（热熔狭缝涂布）]]", "[[Polyolefin Hot Melt Adhesive（聚烯烃热熔胶）]]", "[[分区密度设计]]", "[[COCO芯体平台]]"]
---

# Personal Care Process 101 - How It's Made（卫品加工工艺入门）

## 一句话定位 One-line positioning

K-C 内部**加工工艺（converting）入门教材**：把「一片纸尿裤/卫生巾是怎么被做出来的」拆成十段，是本库把**材料选型 ↔ 产线可行性**连起来的通用地图。回答「这个材料/结构能不能上线、要用哪种粘合方式」时应先落本页。

## 摘要 Summary

教材开宗明义：**无论 pads、diapers 还是 pants，基础制造步骤是相同的**，复杂度来自步骤数量与组合方式。**Process Flow** 段给出工序链（Web Handling → Bonding/Laminating → Vacuum Transport → Component Application → Cutting → Folding），并用 **MD vs CD** 说明产线构型的第一个分野：MD 为端对端制造（约 1970s 起，弹性侧围需裁切并旋转为单片），CD 为并排制造（约 1990s 起，弹性侧围以连续卷材在线送入）。**Web Handling** 段介绍三类料卷（pancake/cookie rolls 如浆卷、traverse wound rolls/spools 如腰围与橡筋）、放卷、Process Draws（**控制点**＝以固定速度连续驱动幅材的点）与纠偏（web guide，用于处理"非理想"幅材）。**Air Systems** 段区分机器真空系统（为各机台提供真空以输送材料）与集中空气系统（除尘过滤、物料收集分离、废料处理与回收、HVAC、中央真空）。**Absorbent Core Forming** 段是材料侧最关键的一段：**绒毛浆与 SAM 跟着气流走**，因此可用成型网做形状、分区（pocketed screen 3D / zoning segment 2D）与通道，典型为 70% SAM 芯体。**Bonding/Laminating** 段给出胶黏剂（热熔胶为主，三种施加方式）与四种复合工艺。**Cutting / Applying Components / Folding** 段给出裁切五法、组件施加与折叠。

## 提炼的数字与结论 Key figures & conclusions

| Item 项目 | Value / Conclusion 数值·结论 | Note 备注 |
|---|---|---|
| 知识框架 Topics | **10** 段（Process Flow → … → Appendix） | 主讲人 Joe Sina（工艺/电气/气路）与 Hwa Kim（裁切/组件/折叠） |
| MD vs CD | MD 端对端、约 1970s；CD 并排、约 1990s，弹性侧围连续卷材在线送入 | 构型分野 |
| 芯体 SAM 占比示例 | **70% SAM core for diapers** | 示例值 |
| 芯体成型工序 | SAM 输送计量 → 绒毛浆输送与纤维化 → 气流成型 →（可选）折叠 → 脱蓬与裁切 | 全程用气 |
| 成型可选项 Forming options | 形状芯体 / 分区芯体（3D pocketed screen 或 2D zoning segment）/ 带通道芯体 | 气流成型带来的自由度 |
| 胶黏剂地位 | **热熔胶用得最多**：可粘异质材料、固化快、成本有效 | 三种施加方式见下 |
| 施加方式 Application | **Slot（接触，狭缝模头挤出）**／**Spray（非接触，喷嘴喷涂）**／**Strand（橡筋股线涂布）** | 含胶路系统：卸料→软管→分配→计量→温控/压控 |
| 压力粘合 Pressure bonding | 花辊 + 光滑砧辊高压机械变形；常与胶粘并用，可减胶量 | 花辊磨损与辊隙载荷决定一致性 |
| 热粘合 Thermal bonding | 两辊加热至特定温度；**材料熔点相近时效果最好**；需精确控温以预测辊膨胀 | 间隙失控 → 过粘/欠粘与花辊磨损 |
| 压花 Embossing | 与压力粘合类似，但**按材料类型与厚度留刻意间隙**；用于外观、性能提升、层压 | 间隙控制决定图案一致性 |
| **超声波粘合 Ultrasonic** | 焊头振动 **20–40 kHz**，靠**迟滞（hysteresis）**把能量传入材料使聚合物熔融；花型砧座几何决定粘合形态；**能量足以熔化非晶与结晶两相** | 压力粘合只冷流非晶区（时间/能量不足） |
| 超声波代价 Cost of ultrasonics | **投资与维护成本高于热粘合与压力粘合**；horn 与驱动电子对热、压力、horn 自身状态敏感（"裂了的铃不响"类比） | 依赖场景：热/压力粘合不行时才用 |
| 裁切方式 Cutting | 直刀 + 打孔（Straight-Knife & Perf）／模切（Shaped, Die）／水切（Shaped, Water）／分切（Slitting）／切断（Chopping） | 依材料性质与目标效果选择 |

## 关键论断（key_claims）

- **同一目标有多条工艺解，选型的胜负常取决于工艺窗口而非材料本身** —— 支撑页：[[Pressure vs Thermal vs Ultrasonic Bonding（压力·热·超声波粘合对比）]]
- **气流成型是"分区化/形状化"路线的物理前提：绒毛浆与 SAM 跟着气流走** —— 支撑页：[[分区密度设计]]、[[COCO芯体平台]]
- **热熔胶之所以是主力，是因为它同时满足异质粘接 + 快速固化 + 成本三项** —— 支撑页：[[Hot-Melt Slot Coating（热熔狭缝涂布）]]、[[Polyolefin Hot Melt Adhesive（聚烯烃热熔胶）]]
- **超声波能粘热/压力粘不了的材料，但代价是投资与维护：它是兜底而非首选** —— 支撑页：[[Ultrasonic Bonding of PET-Containing Topsheet]]、[[Pressure vs Thermal vs Ultrasonic Bonding（压力·热·超声波粘合对比）]]

## 关联页面 Linked pages

- 对比 Comparison：[[Pressure vs Thermal vs Ultrasonic Bonding（压力·热·超声波粘合对比）]]（本页派生）
- 概念 Concept：[[Ultrasonic Bonding of PET-Containing Topsheet]]、[[Hot-Melt Slot Coating（热熔狭缝涂布）]]、[[Polyolefin Hot Melt Adhesive（聚烯烃热熔胶）]]、[[分区密度设计]]、[[芯体通道花型设计]]、[[COCO芯体平台]]、[[Ultra-Low Add-On Adhesive Application（超低添加量施胶）]]
- 组合 Portfolio：[[IPC BCC OI Portfolio（开放创新项目组合）]]

> 📌 OI 互链说明 Open Innovation linkage：本页属 OI Products/工艺资料层，是判断 OI 项目「工艺就绪度（Process Readiness）」的通用底座。涉及组合编号时默认采用 [[IPC BCC OI Portfolio（开放创新项目组合）]] 页认定的重构版 19 项口径（`OI-1`~`OI-19`）。

## 原文 Source file

- 本地路径 Local path：`RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Products/Personal Care Process 101 - How its Made.pptx.md`
- 原文链接 Original link：（无；K-C 内部培训 PPT，2025-09，作者 Joe Sina & Hwa Kim）
- 同族资料 Related：Products 目录下另有 `CD Pants Process Overview -GIC Korea.pptx`（后续批次编译）

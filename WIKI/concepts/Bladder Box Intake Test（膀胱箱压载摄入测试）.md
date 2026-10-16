---
type: concept
title: "Bladder Box Intake Test（膀胱箱压载摄入测试）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-29
tags: [STM-00497, intake, 摄入时间, 压力, 回渗, 失禁用品, 成人护理]
aliases: ["Intake via Bladder Box", "膀胱箱法", "STM-00497"]
---

# Bladder Box Intake Test（膀胱箱压载摄入测试）

> One-line definition 一句话定义：用**充气泡（bladder box）对产品施加消费者相关压力**，并**在该压力下**测量灌入一定量液体所需的摄入时间（intake time）的 K-C 标准测试方法（STM-00497）——摄入后按回渗方法学测表面干爽度。
> (A K-C standard test method in which an inflatable bladder applies consumer-relevant pressure to the product, and intake time is measured *under that pressure*.)

## Mechanism 机理拆解

1. **压力是被隐藏的自变量 Hidden variable = pressure**：液体是否被「吸收」取决于产品受压后的孔隙状态；常压法下孔隙张开，会系统性**高估**摄入能力。膀胱箱的作用就是把这条路堵死。
2. **两级压力、两种用途 Two pressures, two purposes**：①**摄入段 0.25 psi**（另有装置能力表述为 bladder bag 可维持 0.08 psi）；②**回渗段 0.7 psi / 25 mm 砝码 / 2 分钟**。两者不可混淆，写门槛时必须分别标明。
3. **加液量源于使用实态 Loadings traceable to use data**：单次冲击量 = ULS（Urinary Loss Study）或 HUT 的**第 95 百分位总载量 ÷ 单次冲击量**（取整），单次冲击量再取整到 5 mL；因此不同品类（护垫 vs 失禁裤）的加液量天然不可横向比较。
4. **靶点由几何决定 Target location is geometric**：Poise 产品取吸收体长度 L 的中前/中后两点，`Middle-Front = ((L/6)×2) + ((L/6)×1/2)`，**每步计算均先四舍五入到 0.1 cm**；Depend 产品则按附录表给出距中心的距离。
5. **Run-off failure 是终止条件 not a data point**：液体越过非吸收腿部橡筋流到 bladder 上即判失败，该次冲击记 FAIL 并**立即终止整段测试**（不得继续后续冲击）。

## Key parameters 关键参数表

| Parameter 参数 | Value 数值 | Source 出处 |
|---|---|---|
| Bladder bag 维持压力 | 0.08 psi | [[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]] |
| 摄入段设定压力 | **0.25 psi** | 同上 |
| 进液口内径 | 1.0 英寸 | 同上 |
| 压力传感器 | 0–2 psi，分辨率 0.01 psi（如 Omega HHP701-2） | 同上 |
| 加液次数 / 间隔 | 3 次冲击 / 每次 15 分钟 | 同上 |
| 流速 | 1 或 8 mL/s（按品类取） | 同上 |
| 测试液 | 0.9 ± 0.005% 盐水，约 37 ℃ | 同上 |
| 回渗段条件 | 0.7 psi、25 mm 砝码、2 分钟，两张预称吸水纸 | 同上 |
| 记录精度 | 重量 0.01 g／厚度 0.1 mm／吸入时间 0.01 s／吸水纸 0.001 g | 同上 |
| 实验室环境 | 23 ± 2 ℃、50 ± 5% RH（ASTM）；在线测站可不控但须记录 | 同上 |
| 适用单元 | Adult & Feminine Care（个人护理与国际业务）；QA / 运营 / 研发 | 同上 |
| 文件状态 | **Draft / New STM**（起草人 Madeline Rutherford，AFC R&E） | 同上 |

> ⚠️ **禁止无来源参数**：表中数值均转载自上列源摘要页；该文件为草案，**精密度表（Table 1）为空白模板**，故本页不给出重复性与再现性数据 `[待验证]`。

## Relationship to other intake methods 与其他摄入方法的关系

| Method 方法 | Pressure 是否加压 | Typical scope 适用范围 | Link 页面 |
|---|---|---|---|
| **Bladder Box Intake（本法）** | **是，0.25 psi** | 成人/女性护理（Depend / Poise） | 本页 |
| Cradle Intake | 否（常压/压载 multi-insult settings） | 婴儿线产品的 1st/2nd/3rd 摄入 | [[Cradle Intake Test（Cradle 摄入测试）]] |
| STT Strike-through | 否 | 面层穿透的放行级快速指标 | [[芯体测试方法与验收基准（STM）]] |
| L-H Rewet | 低/高负载双档 | 产品级干爽度（摄入后） | [[Rewet Test（回渗测试）]] |

> ✅ **呼应既有教训 Echoes an existing lesson**：本库 [[GBP-Limited vs CRC-Limited Regime（渗透受限 vs 容量受限机制）]] 已记录「测试协议决定胜负」——本法把压力显式化是同一逻辑在**成人/女性护理产品线**上的制度性表达。

## Adjacent concepts 相邻概念

- 平行 Parallel methods：[[Cradle Intake Test（Cradle 摄入测试）]]、[[Acquisition Test STM-00060（导流性能测试）]]、[[Retention Capacity Test（滞留能力测试）]]
- 指标邻接 Adjacent metrics：[[Rewet Test（回渗测试）]]、[[Run-off & Leakage Test（滑渗与渗漏测试）]]
- 体系 System：[[SAM Testing Methods（超级吸水材料测试方法）]]、[[芯体测试方法与验收基准（STM）]]

## Verification log 验证记录

> ✅ 建立（2026-09-29，来源 [[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]]）：本页参数与方法学逐条对应该文件 PURPOSE / Scope / Procedure / Results / Apparatus 各段。
> 🔴 **manual_review（2026-09-29）**：源文件为 **K-C 内部 STM 草案**，含按产品列出的加液参数表与内部研究编号；**本页不复制加液表**，对外引用或作合同附件前须 QA/法务确认。

## Lessons learned 经验教训

- **KPI 必须写明"在什么压力下测得"**：同一产品换压力等级，摄入时间可能翻倍——这就是 protocol-dependence。
- **加液表按品类锁定，不可跨品类套用**：成人失禁裤与女性护垫的总载量相差一个数量级。
- **草案方法慎用**：精密度数据缺失意味着无法声明重复性与检出能力，只能用于内部趋势判断。

## Sources 来源

- [[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Test Methods/FIUP - TTM-00643/Intake via Bladder Box draft STM-00497 - Copy.docx.md`

## Related Sources 关联来源

- [[Capillarity Testing Throughput Upgrade Plan（毛细测试吞吐提升计划）]]
- [[History of FIUP TTM-00643（FIUP 测试方法沿革史）]]
- [[R150540-TL-14137 Poise Use-Test Load & Leakage Summary（2009）]]
- [[Rewet Method Comparison（回渗测试方法横向对比·K-C vs P&G）]]
- [[Rewet Method Parameters（回渗测试方法参数沿革）]]
- [[STM-00497 Intake via Bladder Box（成人·女性护理压载摄入法草案）]]

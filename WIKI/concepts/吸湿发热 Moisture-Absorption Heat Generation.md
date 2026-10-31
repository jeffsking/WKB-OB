---
type: concept
title: "吸湿发热 Moisture-Absorption Heat Generation"
domain: [卫材研发, 基础理论与模型]
status: growing
updated: 2026-10-23
tags: [thermoregulation, moisture-absorption, heatset, 吸湿发热, 回潮率, 焓变]
---

# 吸湿发热 Moisture-Absorption Heat Generation 吸湿发热

## Definition 定义

**Moisture-absorption heat generation (吸湿发热)** is the transient release of heat when water vapour is sorbed by a fibre and transitions from the vapour state into a bound state within the polymer. The fibre is **not** an energy source: the heat comes from the enthalpy difference between a high-chemical-potential state (vapour) and a low one (fibre-bound water).

**吸湿发热**指水蒸气被纤维吸附、由气态转为纤维结合态时释放热量的**瞬态**现象。纤维**不是热源**：热量来自「高化学势态（气态水）→ 低化学势态（结合水）」的焓差。

> Precise phrasing 严格表述：「热量搬家」是便于传播的说法，物理上应为**「水分状态变化伴随的焓释放」**。

## Mechanism 机理

The governing lumped energy balance 集总能量平衡方程：

```
mcp·(dT/dt) = qabs(R, T)·(dmw/dt) − Q̇loss
```

| Symbol 符号 | Meaning 含义 | Nature 性质 |
|---|---|---|
| `mcp` | 织物热容（质量 × 比热） | 常数（一阶近似） |
| `qabs(R,T)` | 单位吸湿焓变（J/g 水） | **非常数**：随回潮率 R、温度 T、材料变化；低回潮率区间显著偏高 |
| `dmw/dt` | 吸湿速率 | 受吸湿容量与传质动力学约束；∝ (Req − R(t)) |
| `Q̇loss` | 散热功率 | 含对流、辐射、传导、蒸发四项；工程上常合并为 heff·A·(T − Tamb) |
| `ΔT` | 升温值 | **响应变量**，由方程求解得出，**不是**与上列各项同层级的待定参数 |

## Key Parameters 关键参数

| Parameter 参数 | Value 数值 | Note 口径 |
|---|---|---|
| 25 ℃ 水汽化潜热 Lv | ≈ **2442 J/g** | 44.0 kJ/mol ÷ 18.0 g/mol；凝聚贡献的量级参考 |
| 吸湿微分热（液态水被吸附） | **830–1256 J/g 水**；羊毛约 **1340 J/g** | 教材典型值，须连测量定义理解 |
| 示例性单位焓变 | 约 **3.4 kJ/g 水** | 选定热力学路径后的量级估算，**非普适参数** |
| 吸湿积分热 | 羊毛 112.6 / 黏胶 104.7 / 蚕丝 69.1 / 棉 46.1 / 涤纶 3.4（J/g 干纤维） | 教材值 |
| 归一化后 | 355–850 J/g 水（极差 2.4 倍，原 33 倍） | 按标准回潮率折算；涤纶因分母过小失真 |
| 标准阈值 | FZ/T 73036—2010：最高升温 **≥4.0 ℃**、30 min 平均 **≥3.0 ℃** | 20 ℃ / 90% RH / 30 min，特定装置条件 |

## Three constraints that must not be violated 三条不可逾越的约束

1. **Transient, not steady-state 瞬态而非稳态** — 通量趋零（吸饱）则产热停止；价值只在湿度跃变后的数分钟。注意「环境湿度不变」≠「吸湿速率为零」（织物未平衡、人体持续产湿、服装内外存在水汽梯度时仍在吸湿）。
2. **Standard value ≠ wearing experience 标准值≠穿着体验** — 4 ℃ 是特定试样状态与试验条件下的材料响应；纤维→纱线→织物→服装→人体-服装-环境共**五级尺度跳跃**，不可直接等同。
3. **No net gain over a cycle 循环无净增益** — 回到同一热力学状态时 **∮dH = 0**（焓为状态函数），故材料不是持续供能材料；但净热交换不必为零（热与功非状态函数），非平衡条件下仍可有实用瞬态收益。

## Design Implications 工程与设计含义

| 场景 | 推论 |
|---|---|
| 宣称设计 | 只能定位「更换/进入湿冷环境后前数分钟的体感补偿」，不可承诺长效升温（否则与「整夜干爽」类宣称直接冲突，与 PCM 的吸热饱和问题同构 → [[相变材料 Phase Change Material]]） |
| 材料改性 | 提高吸湿容量（接枝 −OH/−NH₂/−COOH、碱法水解刻蚀、与铜氨丝复合）是重要路线，但非唯一；效果还取决于吸湿动力学、单位焓与织物结构 |
| 混纺策略 | 产业实践几乎总是**亲水组分发热 + 疏水组分导湿**混纺，在发热与干爽间取平衡 |
| 评价方法 | 须同时考察吸湿、放湿与水分传输能力；**只看吸湿阶段升温会误判** |

## Common Misconceptions 常见误说与纠正

| 常见说法 | 纠正 |
|---|---|
| 「水分子动能转化为热能 / 氢键放热」 | 真实过程是由初态（水蒸气）到终态（纤维结合水）的焓差，不宜拆成两个独立步骤 |
| 「液化潜热占 71%、吸附热占 29%」 | 只能作量级参考，不是物理结论；qabs 随 R、T 变化 |
| 「把汗液汽化潜热全部回收」 | 不成立。须区分「材料释放多少热」与「人体实际获得多少热」——取决于吸湿位置、服装结构与热湿传递条件 |
| 「升温 4 度就是穿上暖 4 度」 | 标准测试条件下的材料响应，非穿着体验 |
| 「吸湿发热材料能持续供热」 | 理想循环 ∮dH = 0，无持续净增益 |

## Related 关联

- 源论述 → [[吸湿发热纤维的热物理学分析]]
- 相邻概念 → [[含水率 Moisture Regain]] · [[湿热耦合 Heat-Moisture Coupling]] · [[热传递 Heat Transfer]]
- 对照技术 → [[相变材料 Phase Change Material]] · [[PCM-Free Thermoregulation]]

## Sources 来源

| 来源 | 用途 |
|---|---|
| [[吸湿发热纤维的热物理学分析]] | 全部方程、数值、标准阈值与纠偏论述的唯一来源（含 FZ/T 73036—2010、GB/T 29866—2013、JIS L 1915:2020 引用） |
| [[含水率 Moisture Regain]] | 回潮率定义与纤维吸着两种模式的背景 |

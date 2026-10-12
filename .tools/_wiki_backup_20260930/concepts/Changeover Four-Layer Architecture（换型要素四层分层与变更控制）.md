---
type: concept
title: "Changeover Four-Layer Architecture（换型要素四层分层与变更控制）"
domain: [卫材研发, 设备工程, 芯体工艺]
status: seed
updated: 2026-09-29
tags: [换型, 分层架构, 变更控制, Body, Sleeve, Recipe, Change-part, 降本]
---

# Changeover Four-Layer Architecture（换型要素四层分层与变更控制）

> One-line definition 一句话定义：**把"换规格时要动的所有量"按「定相位 / 定尺寸 / 可设定 / 仅特定规格」切成 Body、Sleeve、Recipe、Change-part 四层**，使规格扩展的边际成本降到最低——其第一原则是 **"定相位的都在鼓体，定尺寸的都在套筒"**。（中文：换型不是"重新调机器"，而是"只换必要那一层"。）

## Definition 定义：第一原则与四层划分

> 源文件原句：*"Everything that defines phase is on the drum body; everything that defines size is on the sleeve."*

| 层 | 中文 | 承载什么 | 换型行为 |
|---|---|---|---|
| **Layer 1 · Body（鼓体层）** | 鼓体 | 一切决定**相位基准与机械几何**的量：节圆直径、扇区角度、编码器零点、压合间隙、轴向对中、镜像手 | **永不动** |
| **Layer 2 · Sleeve（套筒层）** | 尺寸载体 | 一切决定**尺寸（MD 方向 pattern 布局）**的量 | **必换**（每次 2 片） |
| **Layer 3 · Recipe（配方层）** | 配方 | 可用设定值表达的量：ups、cams、fan、glue、**chute**、成型真空、气刀 | **必改，无实体换件** |
| **Layer 4 · Change-part（换件层）** | 换件 | 只由**宽度族（CD 100/110/120）**或**边缘形状**决定的量 | **仅特定规格需要** |

> **强约束（源文件 P4）**：*"Both drums (skin and poly) always carry the same ups — the nip requires identical pitch and phase on each side."* → **ups 是整线级参数，不是单鼓参数**。

## Mechanism 机理

### 1. 归属判据 Q1–Q4（决策规则）

对任何一个"换型时会变化的量"，按序判定：

```
Q1. 换 ups 时它会变吗？
    ├─ 不变 → Layer 1 Body（永不动）
    └─ 变   → Q2
Q2. 它由「尺寸（MD 长度）」决定吗？
    ├─ 是 → Layer 2 Sleeve（实体换件）
    └─ 否 → Q3
Q3. 它只由「宽度族（CD）」或「边缘形状」决定吗？
    ├─ 是 → Layer 4 Change-part（宽度插片 / 刀片插片）
    └─ 否 → Q4
Q4. 它能否仅靠设定值（伺服/变频/阀）表达，无需换实体件？
    ├─ 能 → Layer 3 Recipe
    └─ 不能 → ⚠️ 设计缺陷：应重新设计为 Recipe 或 Change-part
```

- **Q1 的工程含义**：把"几何与相位"完全隔离在 Body，是**换型不需要重新对相（re-registration）**的前提（依赖 sleeve 由 pin 定位到编码器零点 ±0.02 mm）。
- **Q4 的"不能"分支是架构缺陷检测器**：任何"随尺寸变、又必须换实体件、且换起来很贵"的量，都是**设计没做干净**。

### 2. 为什么 CD 变更必须走 chute 插片（本架构最重要的成本设计）

| 方案 | 后果 | 判定 |
|---|---|---|
| 用 **ups** 解决 CD | **不可能**：P = πD/n 只作用于 MD 方向，与 CD 无关 | ✗ |
| 把 CD 做进**鼓体** | 每宽度族一套鼓体 → **3 套鼓体 + 3 套扇区 + 3 套对中**，与"单一鼓体"前提矛盾 | ✗ |
| 把 CD 做进 **sleeve** | **22 片 → 33 片**（11 尺寸 × 3 宽度），sleeve 数量爆炸；CD 与 MD 正交却混在一层 | ✗ |
| **chute 宽度插片** | 100/110/120 三档成型出口插片；最廉价、换装最快、CAD 上只改出口轮廓 | **✓（采纳）** |

> **逻辑闭环**：CD 由「**鼓体对中（不变）+ chute 出口宽度插片（可换）**」共同决定 → **宽度族扩展的边际成本降到只剩一片插片**。

### 3. 变更控制红线（双向）

**绝不可做进 Body / 固定结构**（否则规格扩展成本失控）：
- CD 宽度（100/110/120）→ 必须走 chute 插片
- pattern 长度 / 端区分布 → 尺寸载体必须可换（sleeve）
- ups 相关的相位关系（n 脉冲）→ 必须由 Recipe 表达为 e-cam；做进机械凸轮则每 ups 一套凸轮组
- 端区长度（随尺寸变）→ 属 sleeve，不可由固定挡块定义
- 换宽度族的涂布宽度 → 必须走分段阀 + 插片，不可用固定喷嘴

**必须固化在 Body（不可下放）**：
- 真空扇区角度（下放 → 换型需改扇区）
- 压合间隙与轴向对中（下放 → 每规格间隙误差，破坏 land-to-land）
- 编码器零点 / 引脚基准（换型不重新对相的前提）
- 双鼓镜像手与同 ups 约束

## Key Parameter Table 关键参数表

| Parameter 参数 | Value 数值 | 出处 |
|---|---|---|
| Sleeve 数量 | **22 片 = 11 尺寸 × 2 侧**；每次换型换 **2 片** | [[83 Changeover Four-Layer Architecture and Change Control（换型要素四层分层与变更控制）]] |
| Body 节圆 | **Ø882.0 mm @ NW 中面**（周长 2,771 mm） | 同上 |
| 鼓壳惯量 | 估算 **270 kg**（J ≈ **52 kg·m²**） | 同上 |
| 压合间隙 | **land-to-land 0.15–0.18 mm**（限位 + 预压） | 同上 |
| 电机 / 编码器 | **≥250 Nm 连续 / ≥600 Nm 峰值**；**≥23 bit** 绝对值编码器；一套电机覆盖两个 ups | 同上 |
| Recipe 五项 | **ups n / cams / fan / glue / chute**（+ 成型真空 −8…−12 kPa、气刀压力） | 同上 |
| Change-part | chute 宽度插片 **100/110/120**；刀片插片**仅 NB、S** | 同上 |
| 换型 SOP | 4 步：Stop & swap → Recipe load → Auto-phase → Verify；总目标 **<30 min** | 同上 |
| Stop & swap 工时 | **≤15 min**（两鼓并行） | 同上 |
| 引脚 / 相机收敛 | 引脚 **±0.05 mm**；相机 **~17 片** 收敛 MD | 同上 |
| ⚠️ 换装工时分歧 | 源文件 **≤15 min/鼓** vs [[Nichidai（日丝）]] **30 s/网** → **差 30 倍，必须并列** | 同上 |

> ⚠️ **No unsourced parameters 禁止无来源参数**：上表全部来自上列源摘要页。**Step 2–4 工时缺失 ⇒「<30 min」无法从分项加总验证**；四层清单与归属为 **B 级（源文件设计意图，非 KC 现行实践）**。

## Adjacent Concepts 相邻概念

- 本位架构：[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]（"相位在鼓体、尺寸在套筒"）
- 同层：[[Repitch（鼓距与产品节距解耦）]]（cams 中的 repitch 转塔凸轮）、[[81 Forming Drum Ups Selection（鼓距·端区·11 尺寸分配）]]（ups 归属 Recipe）
- 失效点：[[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]（chute 为头号静默失效模式）
- 零件级对照：[[84 Sleeve 工程规格与换装防错设计]]（套筒层的规格化细节）
- 设计哲学外延：[[Pain-Point Backward Derivation（痛点倒推法）]]、[[Technology Roadmap 2026-2029（技术路线图）]]

## 经验教训

- **Lesson 1（把复杂度收敛到可换件）**：与 [[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]] 的 Lesson 1 同源——**规格扩展的成本不由"尺寸多少"决定，而由"新增一个规格要动几层"决定**。本架构把它压到 **2 片 sleeve + 1 片插片 + 一组设定值**。
- **Lesson 2（Q4 是缺陷检测器）**："随尺寸变、又必须换实体件、且换起来很贵"的量 = 设计没做干净。**这条判据可外推到任何换型/换规格架构的评审**。
- **Lesson 3（正交维度不要混层）**：CD 与 MD 正交，把 CD 塞进 sleeve（MD 载体）会让换件规则复杂化且数量爆炸——**正交维度应分属不同层**。
- **Lesson 4（红线是双向的）**：既防"把变量固化到 Body"（扩展失控），也防"把常量下放到 Sleeve/Recipe"（引入每规格误差）。**两个方向的越界都要拦**。
- **Lesson 5（时间账要能加总）**：「<30 min」是**目标不是事实**——Step 1 已占 ≤15 min 而 Step 2–4 缺失，**不得对外声称已验证**。
- **待补 `[待验证]`**：Step 2–4 工时分解（最高优先）；sleeve 换装口径的 30 倍分歧澄清；chute 插片换装工时与精度；knife insert 换装能否与 sleeve 换装并行；HCH 多鼓方案换型记录作对照。

> 🔴 **manual_review（2026-09-29）**：本源含**待索取清单**（KC 现场 WI 结构、Nichidai 口径澄清、设备商换件工时）与**选型对照**（HCH 多鼓方案）。依 AGENTS.md §5，**只记技术判据与缺口，不落商务条款与定点结论**；四层归属为 **B 级设计意图**，**不得作验收合同值**。

## 来源

- [[83 Changeover Four-Layer Architecture and Change Control（换型要素四层分层与变更控制）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/83-换型要素四层分层与变更控制.md.md`

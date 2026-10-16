---
type: concept
title: Gasketing Effectiveness（防漏阻隔有效性）
category: 结构 / 防漏
updated: 2026-09-30
tags: [Gasketing, 腰围垫片, 腿围垫片, 护围, 最小阻力路径, Gap Test, STCH, Tunnel Leakage]
domain: [卫材研发, 芯体与吸收]
status: growing
---

# Gasketing Effectiveness（防漏阻隔有效性）

**一句话定义**：Gasketing = **材料属性 + 位置 + 与其他部件的连接方式**三者共同决定的能力 —— 使未受控的尿液**无法沿最小阻力路径**（tunnel 通道 / channel 沟槽 / hole 孔 / gutter 槽 / seam 缝）逃逸；在纸尿裤上具体指**腰围 / 腿围 / 护围垫片**。

> 名称说明：ASR 与内部文件中 "gasket" 有歧义（垫片 vs. 芯体成形的 shim）。本页采用 **KC 尿液泄漏管理五支柱**中的定义（**防漏阻隔垫片**），证据等级 High；若语境指 shim / pad forming，另见附录型内容。

## 机理 / 结构拆解

### 1. 在尿液管理体系中的位置

KC 尿液泄漏管理**五支柱**（按序）：

**Target Zone Capacity（目标区容量）→ Intake at Rate of Insult（按冲击速率摄入）→ Free Fluid Control（自由液体控制）→ Bucket Volume（桶容积）→ Gasketing（有效阻隔系统）**

→ Gasketing 是**最后一道**，也是唯一一道"**不发生吸收、只管拦住**"的机制。

### 2. 两类典型失效模式（KC 内部命名）

| 失效模式 | 表现 | 根因 |
| --- | --- | --- |
| **Flow Underneath** | 液体沿**贴肤层底面**流动 | 贴肤层下方未被封住 |
| **Tunnel Leakage** | **通道（tunnel）泄漏** | **缺胶** —— "No adhesive to stop fluid flow" |

> 关键：**Tunnel Leakage 的根因是缺胶**，不是材料本身 —— 因此其改善手段落在**施胶路径、胶量监控、在线检测**，而非垫片材料升级。

### 3. 测试体系

| 方法 | 测什么 | 输出 / 用途 |
| --- | --- | --- |
| **Gap Test** | 垫片元件失效前能维持的**液柱高度** | 输出柱高；用于评估**设计变更**与**表面张力效应** |
| **Clear mannequin（透明假人）** | 识别失效模式 | 定性定位 |
| **Flap hydrohead（护围耐静水压）** | 护围的耐静水压 | — |
| **Outercover pinhole（底膜针孔）** | 底膜针孔泄漏 | — |
| **MOCON** | 透气性 | — |
| **SAM poke-through** | SAM 穿刺抵抗（属垫片有效性测试包） | 垫片区的压缩集中 → SAM 与下层穿刺表现 |

### 4. 测试液 —— 最容易被忽略的关键点

**0.9% NaCl 生理盐水 + 0.1% 牛磺胆酸钠（STCH）**，把**静态与动态表面张力拉到尿液水平**。

> **含 gasket 的测试必须使用 STCH（TL-16147）。** 用纯盐水测垫片会得到系统性偏乐观的结果 —— 因为垫片失效本质上是"液体沿低阻力路径爬出去"，对**表面张力极度敏感**。

## 关键参数表

| Item 项目 | Value 数值 / 内容 | Note 备注 |
| --- | --- | --- |
| 五支柱序位 | Target Zone Capacity → Intake at Rate → Free Fluid Control → Bucket Volume → **Gasketing** | 末道机制 |
| 三类垫片 | **腰围 / 腿围 / 护围** | — |
| 失效模式 | **Flow Underneath** / **Tunnel Leakage** | 后者根因 = **缺胶** |
| 测试液 | **0.9% NaCl + 0.1% STCH** | 含 gasket 测试**强制**（TL-16147） |
| 弹性区专利参考 | **JP07308341**：**弯曲弹性区**（PU 泡沫 / 氨纶弹性片粘合到垫片护围） | 腿围垫片护围的弹性区设计 |
| 与 T5 的接口 | **SOAR4（腰围弹性化）** 与垫片的界面属 **T5 升级项** | 会随 tier 提升而变化 |
| 与开孔面层的交叉风险 | 开孔区若延伸到腿围/腰围垫片区 → 可能创造**新的最小阻力路径** | 需在面层与垫片两个议题间交叉验证 |

## 相邻概念

- [[Blowout Leakage Test（爆漏测试）]]
- [[Run-off & Leakage Test（滑渗与渗漏测试）]]
- [[Mannequin BM Test（BM 假人测试）]]
- [[Motion Mannequin Test（动态假人测试）]]
- [[Kirigami Apertured Nonwoven（切割拉伸开孔工艺）]]
- [[Front Belt Force Window（前腰带弹性力窗口）]]
- [[Pant-Type Disposable Absorbent Article（裤型一次性吸收物品）]]

## 经验教训

1. **垫片是"拦"而不是"吸"** —— 五支柱中前四者都在处理"吸收与容纳"，只有 Gasketing 处理"逃逸路径"。因此**芯体再强也救不了垫片失效**。
2. **缺胶比材料更要命**：Tunnel Leakage 的根因被明确归为"没有胶阻止液体流动" —— 改善手段应在**施胶路径、胶量监控、在线检测**，而不是换垫片材料。
3. **测试液决定结论方向**：垫片失效对表面张力极敏感；**不加 STCH 的垫片测试是无效测试**（TL-16147 强制）。这条容易被当成"化验细节"而忽略，实际会系统性高估垫片性能。
4. **开孔与垫片是一对矛盾**：面层开孔（Kirigami / 激光）改善液体管理与透气，但如果开孔区延伸到垫片区，会**主动创造新的最小阻力路径** —— 两个议题必须交叉评审，不能各自优化。
5. **tier 升级会改变接口**：T5 引入 SOAR4 腰围弹性化后，垫片与弹性化的界面变成新的设计项 —— 垫片不是静态部件。

> 🔴 **manual_review（2026-09-29）**：本页涉及 KC 内部失效模式命名、测试标准编号（TL-16147）与专利号（JP07308341），以及内部项目代号。按 AGENTS.md §5，**内部标准与专利细节不得对外页面化**；此处只保留机制、方法与量级。请回原文核对：
> `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/TJ_Mill_Visit_Pre-Brief_20260907_v3.1_EN.docx.md`

## 来源

- [[TJ Mill Visit Pre-Brief — GRID × Kirigami, Coform & Gasket Deep-Dive（2026-09-07 v3.1）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/TJ_Mill_Visit_Pre-Brief_20260907_v3.1_EN.docx.md`

## Related Sources 关联来源

- [[CD Pants Overview 1-Piece vs 3-Piece Design（裤型 1P 与 3P 设计总览 · 2017-11-30）]]
- [[STM-00061 折页渗漏.docx]]
- [[TJ Mill Visit Pre-Brief v3.1（中文版 · TJ工厂访问会前简报 2026-09-07）]]
- [[TJ Mill Visit Pre-Brief v3（中文版 · TJ工厂访问会前简报 2026-09-07）]]
- [[TJ Mill Visit Pre-Brief — GRID × Kirigami, Coform & Gasket Deep-Dive（2026-09-07 v3.1）]]

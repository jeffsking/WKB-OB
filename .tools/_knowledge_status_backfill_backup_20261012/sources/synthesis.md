---
type: source
title: "synthesis.md"
source_type: 行业新闻
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/synthesis.md.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
key_claims: []
pages_linked: []
compile_mode: extractive
---

# synthesis.md

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 行业新闻`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/synthesis.md.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# synthesis.md.md

# Synthesis — 《Mathematics of Diffusion》(Crank, 1975) 全书合成报告

## 一、全书理论地图（Theoretical Map）

                    ┌─────────────────────────────────────────────────────┐
                    │                  Chapter 1                          │
                    │  The Diffusion Equations (PDE + Fick's Law)         │
                    │  核心：F = −D∇C, ∂C/∂t = ∇·(D∇C)                    │
                    └───────────────────────┬─────────────────────────────┘
                                            │
                    ┌───────────────────────▼─────────────────────────────┐
                    │                Chapter 2                             │
                    │  Methods of Solution (恒 D)                          │
                    │  反射法 · 分离变量 · Laplace 变换                    │
                    └───────┬──────────┬──────────────┬───────────────────┘
                            │          │              │
         ┌──────────────────▼──┐  ┌────▼───────┐  ┌──▼──────────────┐
         │    Chapter 3        │  │  Chapter 4 │  │  Chapter 5/6    │
         │ Infinite/Semi-inf.  │  │ Plane Sheet│  │ Cylinder / Sphere│
         │ (源函数)            │  │(时间滞后法)│  │(Bessel/u=Cr)    │
         └─────────────────────┘  └────┬───────┘  └─────────────────┘
                                       │
                    ┌──────────────────▼────────────────────────────────┐
                    │                Chapter 7                           │
                    │  Concentration-Dependent D                        │
                    │  Boltzmann 变换 + Crank-Henry 迭代                 │
                    └──────────┬───────────────────────┬────────────────┘
                               │                       │
                    ┌──────────▼──────────┐    ┌──────▼─────────────┐
                    │    Chapter 8        │    │   Chapter 9        │
                    │  Numerical Methods  │    │  Calculated Results│
                    │  FDM/Crank-Nicolson│    │  (D(C) 图形)       │
                    └─────────────────────┘    └────────────────────┘

                    ┌──────────────────────────────────────────────────┐
                    │                Chapter 10                         │
                    │  Definition & Measurement of D                    │
                    │  参考系 · 时间滞后 · Frisch · 动态法              │
                    └───────────────────────┬──────────────────────────┘
                                            │
                    ┌───────────────────────▼──────────────────────────┐
                    │                Chapter 11                         │
                    │  Non-Fickian Diffusion                            │
                    │  Case I/II/Non-Fickian · Mt∝tⁿ                   │
                    └───────────────────────┬──────────────────────────┘
                                            │
              ┌─────────────────────────────┼──────────────────────────┐
              │                             │                          │
    ┌─────────▼────────┐        ┌──────────▼─────────┐   ┌────────────▼────────┐
    │   Chapter 12     │        │   Chapter 13       │   │   Chapter 14       │
    │ Heterogeneous    │        │ Moving Boundaries  │   │ Diffusion + Chem.   │
    │ (层状+颗粒)      │        │ (Stefan 问题)      │   │ Reaction            │
    └──────────────────┘        └────────────────────┘   └─────────────────────┘
              │                             │                          │
              └──────────────┬──────────────┴──────────────────────────┘
                             │
              ┌──────────────▼────────────────────────────────────────┐
              │                Chapter 15                              │
              │  Simultaneous Diffusion of Heat and Moisture           │
              │  耦合 PDE · 正常坐标 · Henry 定标                      │
              └───────────────────────────────────────────────────────┘

地图解读：
- 底层（Ch1）：公理化基础——Fick 定律 + 扩散 PDE。
- 工具箱（Ch2）：解析解的三套方法。
- 几何扩展（Ch3–6）：从无限域到片/柱/球有限域。
- 变系数（Ch7–9）：D 从常数到 D(C)，解析 + 数值。
- 测量方法学（Ch10）：实验到 D 的桥梁。
- 偏离 Fick（Ch11）：高分子非菲克行为——本书对 SAP 应用最关键的章。
- 复杂介质（Ch12–15）：多层、动边界、化学反应、湿热耦合——本书对纸尿裤/湿巾应用最直接的章。

## 二、概念索引（按理论层级组织）

### 层级 0：公理层

- 扩散过程（Ch1 §1.1）
- Fick 第一定律（Ch1 §1.2）
- 扩散 PDE / Fick 第二定律（Ch1 §1.3）
- 各向同性/各向异性（Ch1 §1.2–1.4）
### 层级 1：解法层

- 反射法（Ch2 §2.2）
- 分离变量法（Ch2 §2.3）
- Laplace 变换法（Ch2 §2.4）
- Boltzmann 变换（Ch7 §7.2.1）
- Crank-Henry 迭代法（Ch7 §7.2.2）
- 有限差分法（Ch8）
- Crank-Nicolson 法（Ch8 §8.5）
### 层级 2：几何层

- 瞬时点/面/球/柱源（Ch3）
- 片层（Ch4）：稳态 + 非稳态 + 时间滞后
- 圆柱（Ch5）：Bessel 函数
- 球（Ch6）：u=Cr 变换
### 层级 3：参数层

- 扩散系数 D（Ch1, Ch10）
- 渗透常数 P（Ch4 §4.2.1）
- Barrer 积分 D̄（Ch4 §4.2.2, Ch9）
- 有效扩散系数 D_eff（Ch14 §14.2）
- 热力学 D_T / 动力学 D_0（Ch10 §10.6.2）
### 层级 4：测量层

- 稳态透过法（Ch4 §4.2）
- 时间滞后法 L = l²/6D（Ch4 §4.3.3, Ch10）
- Frisch 分解 L_F+L_T（Ch10 §10.6.2）
- 动态振动膜法（Ch10 §10.6）
- Ash-Barrer 稳态反演（Ch10 §10.6.1）
### 层级 5：偏离层

- 非菲克扩散（Ch11）
- Case I / Case II / Non-Fickian（Ch11 §11.1）
- Mt ∝ tⁿ 判据（Ch11）
- 动边界（Ch13）
- Stefan 问题（Ch13 §13.1）
### 层级 6：耦合层

- 层状介质串联（Ch12 §12.2）
- Maxwell 等效（Ch12 §12.3）
- 扩散-化学反应（Ch14）
- 湿热耦合（Ch15）
- 正常坐标解耦（Ch15 §15.6）
## 三、原文摘选索引（CSV 格式）

完整版 CSV 见 index.csv，共 48 条记录，涵盖 Ch1–Ch15 每章 3–4 条关键原文。

索引字段说明：
- 章节：Ch1–Ch15
- 页码：原文页码
- 原句：英文原文摘选
- 引用目的：该摘选在拆解中的论证功能

按业务主题分组的关键摘选：

||||
|---|---|---|
|SAP 吸水|u=Cr 变换（球→线）|Ch6 p.90|
|SAP 吸水|Mt ∝ tⁿ, 0.5<1|Ch11 p.256|
|SAP 吸水|Case II 匀速前沿|Ch11 p.256|
|SAP 溶胀前沿|−D₁dC/dx = C₁dX/dt|Ch13 p.297|
|SAP 等效 D|D/(R+1)|Ch14 p.327|
|芯体多层|串联阻力 Σ(lᵢ/Dᵢ)|Ch4 p.47|
|芯体多层|层状串联 (12.4)|Ch12 p.268|
|湿迁移|时间滞后 L = l²/6D|Ch4 p.52|
|湿迁移|稳态判据 Dt/l²=0.45|Ch4 p.52|
|湿巾 MVTR|P = DS|Ch4 p.46|
|防回渗|耦合 D' = D(1+γα)|Ch15 p.364|
|湿冷感|吸湿曲线实为冷却曲线|Ch15 p.354|
|D(C) 反演|Frisch 时间滞后法|Ch10 p.225|
|非菲克诊断|L_F + L_T 分解|Ch10 p.227|
|纤维吸液|对数分布非線性|Ch5 p.70|
|抗菌剂缓释|exp(−x√(k/D))|Ch14 p.335|

## 四、阅读路线图（Reading Roadmap）

### 4.1 面向 SAP 研发工程师的路线

必读路径（核心 8 章）：
Ch1 → Ch4 → Ch7 → Ch9 → Ch10 → Ch11 → Ch13 → Ch14

可选路径（按

*（正文超过 6000 字，此处截断；完整内容见镜像层）*

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/synthesis.md.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/synthesis.md.md`
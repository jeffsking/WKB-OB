---
type: concept
title: "MCCT Multi-Component Capillary Tension（多组分毛细张力测试）"
domain: [卫材研发, 测试与标准]
status: growing
updated: 2026-09-30
tags: [MCCT, 毛细张力, Bn, 解吸, 吸收曲线, 停留时间, 终点判定, 测试吞吐]
aliases: ["MCCT（多组分毛细张力）", "Capillarity Testing（毛细测试）"]
---

# MCCT Multi-Component Capillary Tension（多组分毛细张力测试）

> 一句话定义：一种**台阶式升降液面**的毛细测试——把样品夹在多孔砂芯板（frit）上，逐档改变液面高度并记录吸液/脱液量，拟合出 **Bn（特征毛细压，characteristic capillary pressure）** 与 **n（分布宽度，breadth）** 两个参数，用来回答「这个结构在什么压力下还能把液体拉住 / 什么时候开始吐回来」。

## 机理 / 结构拆解

1. **测的是「毛细压—饱和度」关系，不是吸水量**：样品在每个高度台阶上达到平衡（equilibrium）后称重，减重即含水量；压差由液面相对样品的高度给出。由此得到**吸收（absorption）与解吸（desorption）两条分支**，二者不重合即**滞后（hysteresis）**——滞后本身就是结构的指纹。
2. **Bn 与 n 的物理含义**：**Bn 是特征毛细压**（把液体拉住的能力所在的位置），**n 是分布宽度**（孔径/毛细尺寸的均一程度；n 小 = 孔径集中、吸力台阶陡；n 大 = 孔径分散、吸力过渡平缓）。
3. **为什么它能解释回渗**：回渗的本质是「已吸收的液体在外部压力下被挤回到面层」。Bn 决定**多大的压力开始吐液**，n 决定**吐的过程是突然还是渐进**。因此 MCCT 是把「结构 → 回渗」从经验相关推进到可计算参数的桥。
4. **停留时间（dwell time）是精度的敌人**：每档必须等到真正平衡，否则曲线系统性偏低。软件化后允许**每个高度独立设置停留时间**，并正在用**终点判定算法**（自动识别已达平衡）替代固定等待——这既是提速手段，也是把「操作员经验」从方法里拿掉的动作。
5. **硬件三件套决定数据可比性**：**frit 板**（3D 打印件被明确确认不影响数据变异）、**天平**（mg 分辨率 / 600 g 量程 / 防风罩）、**激光测厚仪**（厚度用于把重量换算成饱和度）。砂芯板水平（zero level / frit level）与蒸发（beaker 加盖）是可复现性的两个隐形变量。
6. **吞吐是这项方法的现实约束**：单样占机以**小时**计（现状约 4 h/天·样），2026 年潜在样量约 300 个 —— 这直接推动「多机并行 + 求解器 +终点判定」的整条改造线；换言之，**MCCT 不是测不了，而是测得太慢**。
7. **数据链的最后一环是 LIMS**：曲线必须落到 **Lab Vantage** 数据表才能进入项目决策；求解器从 Excel（分钟级）变为 **web 端（秒级）** 后，一次性输出吸收/解吸曲线、Bn 与解吸能（desorption energies）。

## 关键参数表

| 参数 Parameter | 典型值 / 范围 Value | 出处 Source |
|---|---|---|
| 输出参数 Outputs | **Bn（特征毛细压）**、**n（分布宽度）**、解吸能（desorption energies） | [[Capillarity Testing Throughput Upgrade Plan（毛细测试吞吐提升计划）]] |
| 曲线 Curves | 吸收（absorption）+ 解吸（desorption），求解器一次生成三条曲线 | 同上 |
| 停留时间策略 Dwell | 每个高度可独立设置；可选「规定停留时间」或「终点判定算法」 | 同上 |
| 天平 Balance | mg 分辨率、上限 600 g、带防风罩；型号 Sartorius Secura 613-1S | 同上 |
| 关键硬件 Hardware | frit 板（可 3D 打印，不影响数据变异）、激光测厚仪、阀/盘管/执行件、基座板 | 同上 |
| 控制变量 Controls | 砂芯板水平（zero level / frit level）、烧杯加盖抑制蒸发 | 同上 |
| 单样耗时 Cycle time | 现状约 4 h/天·样；目标 ≤ 8 h/样（含软件提速） | 同上 |
| 样量 Sample load | 2026 年潜在约 300 个样品（量级，内部预算口径） | 同上 |
| 可测对象 Specimens | 面层（liner）、导流层（surge）、含浆结构（pulp containing structure） | 同上（Status 表 5/7 软件条目） |

> ⚠️ **禁止无来源参数**：上表全部数值来自同一份内部项目跟踪表（[[Capillarity Testing Throughput Upgrade Plan（毛细测试吞吐提升计划）]]），**尚无第二来源交叉验证**；Bn / n 的**绝对数值区间、单位与典型材料对照表在本库中缺失**，标 `[待验证]`。

## 相邻概念

- 同属回渗方法族：[[Rewet Method Comparison（回渗测试方法横向对比）]]（口径差异）、[[Rewet Test（回渗测试）]]（终点指标）
- 结构侧解释：[[毛细梯度设计]]（Bn 的结构来源：上细下粗的吸力梯度）、[[Groove Capillary Suction]]（沟槽吸力）
- 摄入侧方法：[[Bladder Box Intake Test（膀胱箱压载摄入测试）]]（加压摄入，回答「进得去吗」，与 MCCT 的「留得住吗」互补）
- 测试资产管理：[[芯体测试方法与验收基准（STM）]]（方法文件化路径，对应本方法的 TTM 编写）

## 经验教训

> ✅ 验证（2026-09-29，来源 [[Capillarity Testing Throughput Upgrade Plan（毛细测试吞吐提升计划）]]）：本页为新概念页，首条来源即揭示两条此前本库未记录的事实——① 回渗可以落到 **Bn / n 两个可拟合参数**上，而不止于「回渗多少克」；② 该方法的**瓶颈是占机时长与求解速度**，故改造是「硬件复制 + 软件自动化 + 求解器」三位一体而非单点提速。

- **教训**：**方法的可推广性取决于维护归属，而不是算法本身**。来源把维护风险单列为四类（操作系统变更、bug、编程语言过时、需求变更），且现状是「坏了就打电话给原作者」——任何自研求解器在无人接手维护时都会在第二年变成债务。
- **教训**：**「3D 打印件不影响数据变异」这类判断要显式写进方法文件**，否则每次更换加工方式都要重做精密度验证。本方法的 TTM 明确了暂不做精密度（precision）验证、只验证多台仪器结果一致，属「先复制能力、后补精密度」的务实顺序。
- **待补 `[待验证]`**：Bn / n 与回渗实测值的定量对应关系；不同结构（面层/导流层/含浆芯体）的 Bn 典型区间；滞后环面积的物理意义与判读规则。

## 来源

- [[Capillarity Testing Throughput Upgrade Plan（毛细测试吞吐提升计划）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Performance/Rewet/Capillarity Testing Increased Throughput Plan.xlsx.md`

## Related Sources 关联来源

- [[ATH SAM Relocation（2025-07-29 · 解吸能量·残液·microCT 与 SAM 再分配台架）]]
- [[Capillarity Testing Throughput Upgrade Plan（毛细测试吞吐提升计划）]]
- [[P&G Rewet Patent Deep Dive（宝洁回渗专利深挖）]]
- [[Rewet Competitive Analysis Poise vs Always Discreet（解吸机制与毛细压力）]]
- [[War on Wetness - Adult Care Rewet Update（成人护理回渗进展 2026-03）]]

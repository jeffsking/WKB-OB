---
type: concept
title: "Differentiable CFD and AI Surrogate Solvers（可微分 CFD 与 AI 代理求解器）"
domain: [仿真建模, 吸收仿真, AI4Science, 开放创新]
status: growing
updated: 2026-09-30
tags: [CFD, 可微分编程, differentiable, 神经算子, neural operator, 代理模型, surrogate, OpenFOAM, SPH, AI-Agent]
---

# Differentiable CFD and AI Surrogate Solvers（可微分 CFD 与 AI 代理求解器）

> 一句话定义 One-line definition：**可微分 CFD**指把整个数值求解流程（含 PDE 残差与数值格式）嵌入自动微分图，使梯度可从物理量反向传播到神经网络参数；**AI 代理求解器**指用神经网络直接近似流场映射（几何/边界条件 → 速度场、压力场），以换取数量级级别的推理加速。两者是 AI 与流体仿真融合的两条主干。

## 机理 / 结构拆解 Mechanism and Structure

1. **可微分路径（differentiable path）**：求解器本身由 PyTorch/JAX/Julia AD 承载，PDE 离散与数值格式进入计算图 → 损失函数可对求解结果求导 → 神经网络（闭合模型、源项、边界模型）可用物理梯度训练。工程价值在于**训练目标与物理一致**，而不是只拟合数据。
   - 后验训练（a posteriori training）：把 NN 闭合模型嵌入 LES 后按实际模拟结果训练，而非先离线拟合再插入——避免训练/部署分布不一致。
2. **嵌入路径（embedding path）**：保留 OpenFOAM 等成熟求解器作计算核心，把 DNN 插到特定环节——替代 RANS 的线性动量耗散项、预测 LES 动态 Smagorinsky 系数，或在求解器运行中在线训练（IN_SITU）。
3. **神经算子路径（neural operator path）**：FNO / KNO 等学习的是**函数到函数的映射**（与离散分辨率无关），PINNs 以 PDE 残差作损失，PDE-Net 走机理融合；优势是推理快，代价是外推与守恒性需额外约束。
4. **粒子法路径（SPH path）**：针对自由表面、大变形、多相与颗粒场景，用 SPH 系压力求解器（WCSPH / PCISPH / PBF / IISPH / DFSPH）与最小二乘 SPH（LS-SPH）提高精度，并以代理模型（如 NeuralDEM）换实时性。
5. **智能体路径（AI-Agent path）**：LLM/VLM 作为协调器调用求解器、改代码、扫参数、生成假设；**VLM 物理验证关卡**（审图判断流场特征是否正确）是可信度的关键闸门——把「物理合理性」从人工评审前移到自动关卡。

## 关键参数表 Key Parameters

| 参数 Parameter | 典型值 / 范围 Typical Value | 出处 Source |
|---|---|---|
| 单 GPU DNS 分辨率（IncompressibleNavierStokes.jl） | 840³ 不可压缩 NS 直接数值模拟 | [[Open-Source AI-CFD Frameworks Landscape（开源 AI+流体仿真框架调研）]] |
| 稳态层流代理加速（DeepCFD） | 约 3 个数量级（相对传统 CFD，转述值） | 同上 |
| 可微分压力求解器 | PISO（PICT，PyTorch，多块网格） | 同上 |
| 湍流基准 | lid-driven cavity、湍流通道流（PICT） | 同上 |
| 神经算子类型 | FNO、KNO、PDE-Net、PINNs（MindSpore Flow） | 同上 |
| 数值重构 | WENO5（MindSpore Flow 端到端可微分求解器） | 同上 |
| SPH 压力求解器族 | WCSPH、PCISPH、PBF、IISPH、DFSPH（SPlisHSPlasH） | 同上 |

> ⚠️ **禁止无来源参数 No unsourced numbers**：上表数字**全部来自二手综述转述**，未标注基线求解器、网格、收敛判据与硬件型号，**不可直接横向对比**；引用前须回原始仓库核验。卫材吸收仿真（多孔介质两相渗流、SAP 溶胀、可变孔隙率）在该综述中**未被覆盖**，适用性标 `[待验证]`。

## 相邻概念 Adjacent Concepts

- 数值基础：[[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]——任何代理模型仍需网格无关性验证作 ground truth 基线
- 卫材仿真落点：[[2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）]]、[[2D Absorption Model v8 Simulation Report（二维吸收模型 v8 仿真报告）]]、[[REL Simulation Baby Diaper Core（五纤维 TAB 增强层模拟与改进路线图）]]
- 物理机理：[[Darcy Flow in Fibrous Porous Media（纤维多孔介质达西流动）]]、`[待验证]` 库内是否已建
- 项目：[[IPC BCC OI Portfolio（开放创新项目组合）]]

## 经验教训 Lessons

- **教训一（选型按需求分叉）**：要梯度反传与模型优化 → 可微分求解器（JAX-Fluids / PhiFlow）；要复用 OpenFOAM 生态 → 嵌入路线（DeepFlame / TensorFlowFoam）；要全栈 AI 与极速推理 → 神经算子（MindSpore Flow / DeepCFD）；要自主仿真与物理发现 → AI Agent + VLM 验证。
- **教训二（加速倍数是口径陷阱）**：「3 个数量级」类数字的比较基线不同（稳态层流 vs 通用求解器、网格数、硬件），**跨项目倍率不可比**。
- **教训三（守恒性优先）**：代理模型进入工程流前必须检查**质量守恒与稳定性**；NeuralDEM 明确宣称单 GPU 实时且守恒，说明守恒是被当作卖点而非默认属性。
- **待补 `[待验证]`**：各框架的开源许可证与维护活跃度；对多孔介质/可变孔隙率/毛细驱动的支持程度；与现有吸收模型的耦合路径。

## 来源 Sources

- [[Open-Source AI-CFD Frameworks Landscape（开源 AI+流体仿真框架调研）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/基于搜索结果，目前确实存在多种开源的流体.pdf.md`

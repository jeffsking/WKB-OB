---
type: comparison
title: "Open-Source AI-CFD Framework Routes（开源 AI+CFD 五类路线对比）"
subjects: [端到端可微分求解器, AI 嵌入传统 CFD, 神经算子 / AI 领域套件, 特定机理代理模型, AI Agent 自主仿真]
dimension: 技术路线（融合方式、代表项目、适用问题、成熟度、成本、供应链风险）
updated: 2026-09-29
tags: [CFD, AI4Science, 可微分求解器, 神经算子, SPH, AI-Agent, 仿真选型]
---

# Open-Source AI-CFD Framework Routes（开源 AI+CFD 五类路线对比）

> 一句话结论 One-line conclusion：五条路线的取舍点是**「梯度是否要反传」「是否复用 OpenFOAM 生态」「是否要极致推理速度」「是否针对特定机理」**；对卫材吸收仿真而言，**本综述未覆盖多孔介质两相渗流与 SAP 溶胀**，任何路线落地前都要先做适用性验证 `[待验证]`。

## 主线对比 Main Comparison

| 维度 Dimension | 端到端可微分求解器 | AI 嵌入传统 CFD | 神经算子 / AI 领域套件 | 特定机理代理模型 | AI Agent 自主仿真 |
|---|---|---|---|---|---|
| 代表项目 代表 | JAX-Fluids、PhiFlow、PICT、IncompressibleNavierStokes.jl | DeepFlame、TensorFlowFoam | MindSpore Flow、DeepCFD | SPlisHSPlasH、LS-SPH、NeuralDEM / Noether | RPI「AI 流体力学科学家」、CfdOF、Nek5000、classy_blocks |
| 融合方式 融合 | 求解器写进 AD 框架，PDE 与数值格式可导 | OpenFOAM 为计算核心，DNN 嵌入特定环节 | 神经网络直接近似流场映射 | 针对粒子流/多相/微粒流的专用实现 | LLM/VLM 调用并验证既有求解器 |
| 技术底座 Backend | JAX / PyTorch / Julia | OpenFOAM + Cantera/PyTorch、OpenFOAM + TensorFlow | MindSpore、CNN | SPH（C+++AVX，Python 绑定）、Fortran+Python、单 GPU DL | LLM/VLM + OpenFOAM 工具链 |
| 适用问题 Use case | 需要物理梯度训练 ML 模型（闭合模型、湍流模型学习） | 反应流、RANS/LES 模型替代与系数预测 | 稳态层流快速推理、参数扫描、工业大模型 | 自由表面、大变形、颗粒/微粒流实时仿真 | 自然语言驱动的自动建模、参数扫描、假设探索 |
| 验证基准 Benchmark | lid-driven cavity、湍流通道流（PICT）；单 GPU 840³ DNS（INS.jl） | 反应流算例（原文未列具体基准） | 稳态层流（DeepCFD，约 3 个数量级加速） | 标准 SPH 基准测试（LS-SPH） | VLM 审图物理验证关卡 |
| 成熟度 Maturity | 研究向为主，PICT 为近期发布 | 与工业求解器耦合，工程可接入性较好 | MindSpore Flow 体系完整；DeepCFD 偏研究 | SPlisHSPlasH 较成熟；NeuralDEM 为厂商开源 | 前沿探索阶段，可信度依赖验证关卡 |
| **成本 Cost** | 训练侧 GPU 成本高（DNS/可微求解显存开销大）；软件许可成本为零，但需 JAX/PyTorch 工程能力 | 复用现有 OpenFOAM 资产，**迁移成本最低**；异构硬件（GPU/FPGA）另计 | 训练成本高、单次推理成本极低（DeepCFD 约 3 个数量级加速） | 依赖高性能 C++/Fortran 与 GPU；NeuralDEM 单 GPU 实时，硬件门槛相对低 | 需 LLM/VLM 调用成本与人工复核成本；基础设施多为现成开源件 |
| **供应链风险 Supply-chain risk** | 依赖 JAX/PyTorch 等上游框架版本演进；Julia 生态小众，人才供给有限 | 依赖 OpenFOAM 版本与 Cantera 维护；FPGA 供应商锁定风险 | **MindSpore 与昇思生态绑定**，硬件/框架自主可控性与迁移性需评估 | 依赖 AVX/CUDA 硬件特性；Emmi AI 为单一商业主体开源，路线连续性受厂商决策影响 | 依赖闭源 LLM/VLM API，**模型与接口变更风险最高**；Nek5000 等生态件维护状态不一 |

> ⚠️ **成本与供应链风险列说明**：本表**未使用任何报价数据**，成本为「GPU/工程投入/迁移成本」的定性判断，供应链风险为「上游依赖与锁定」的定性判断。原文未给出许可证类型与维护活跃度，二者**须在选型前补齐** `[待验证]`。

## 卫材吸收仿真适用性 Applicability to Hygiene Absorption

| 路线 Route | 与吸收仿真的关系 关系 | 判断 Judgment |
|---|---|---|
| 端到端可微分求解器 | 可用于**参数反演**（把实验 KPI 作损失，反推材料参数） | 有潜力，但需多孔介质本构 `[待验证]` |
| AI 嵌入传统 CFD | 若吸收模型已基于 OpenFOAM，可沿用 | 迁移成本最低 |
| 神经算子 | 适合**大量几何/工况的快速筛选** | 需先有可信 ground truth 训练集 |
| 特定机理代理模型 | 颗粒流/微粒流与 SAP 颗粒床、绒毛浆纤维网络有一定类比性 | 类比关系**未经证实** `[待验证]` |
| AI Agent | 可自动化参数扫描与后分析 | 需人工把好物理验证关 |

## 关联页面 关联页面

- [[Differentiable CFD and AI Surrogate Solvers（可微分 CFD 与 AI 代理求解器）]]
- [[Open-Source AI-CFD Frameworks Landscape（开源 AI+流体仿真框架调研）]]
- [[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]
- [[IPC BCC OI Portfolio（开放创新项目组合）]]

## 来源 Sources

- [[Open-Source AI-CFD Frameworks Landscape（开源 AI+流体仿真框架调研）]] —— `RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/基于搜索结果，目前确实存在多种开源的流体.pdf.md`

---
type: source
title: Open-Source AI-CFD Frameworks Landscape（开源 AI+流体仿真框架调研）
source_type: 调研综述（网络搜索汇总，PDF 摘录 · 8 页）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/基于搜索结果，目前确实存在多种开源的流体.pdf.md
original_link: ""
date_published: "2026-09-27（PDF 处理日；原文未标注发表日）"
date_processed: 2026-09-29
credibility: 中——二手综述，未给出仓库链接、论文出处与版本号；性能数字（840³ DNS、3 个数量级加速、实时推理）均为转述，需回到原始仓库核验
knowledge_update_status: done
key_claims:
  - "开源 AI+流体仿真方案分五类：端到端可微分 CFD 求解器、AI 与传统 CFD 深度融合、AI 领域套件/神经算子、特定物理机制代理模型、AI Agent 自主仿真生态。"
  - "端到端可微分求解器（JAX-Fluids、PhiFlow、PICT、IncompressibleNavierStokes.jl）的价值在于把 PDE 与数值格式一起纳入反向传播，使梯度可从物理模拟直传神经网络。"
  - "IncompressibleNavierStokes.jl 在单 GPU 上可达 840³ 分辨率不可压缩 NS 方程 DNS，并支持把 NN 闭合模型嵌入 LES 做后验训练（a posteriori training）。"
  - "PICT 为 PyTorch 实现，含可微分 PISO 压力求解器、多块网格，在 lid-driven cavity 与湍流通道流基准上验证，主攻 2D/3D 湍流模型学习。"
  - "DeepFlame 组合 OpenFOAM + Cantera + PyTorch，面向反应流，支持 GPU/FPGA 异构；TensorFlowFoam 把 DNN 直接嵌入 OpenFOAM，可替代 RANS 的线性动量耗散项、预测 LES 动态 Smagorinsky 系数，并支持 IN_SITU 在线训练。"
  - "MindSpore Flow 覆盖物理驱动（PINNs）、数据驱动（FNO/KNO、东方·御风 / 东方·翼风工业大模型）、数据机理融合（PDE-Net）三层，并含 WENO5 等数值重构。"
  - "DeepCFD 用 CNN 近似稳态层流，相对传统 CFD 约 3 个数量级加速，输入几何+流动区域，输出速度场与压力场。"
  - "粒子法侧：SPlisHSPlasH（SPH，含 WCSPH/PCISPH/PBF/IISPH/DFSPH 压力求解器与 Python 绑定）、LS-SPH（最小二乘 SPH，Fortran+Python）、Emmi AI 的 NeuralDEM（工业微粒流代理模型，单 GPU 实时、守恒）与 Noether 框架。"
  - "AI Agent 侧：伦斯勒理工（RPI）的「AI 流体力学科学家」用协调器 + 三支队伍（常规实验 / 代码修改 / 开放式探索），并以 VLM 物理验证关卡审图把关；生态工具含 CfdOF、Nek5000、classy_blocks。"
pages_linked:
  - "[[Differentiable CFD and AI Surrogate Solvers（可微分 CFD 与 AI 代理求解器）]]"
  - "[[Open-Source AI-CFD Framework Routes（开源 AI+CFD 五类路线对比）]]"
  - "[[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]"
  - "[[IPC BCC OI Portfolio（开放创新项目组合）]]"
---

# Open-Source AI-CFD Frameworks Landscape 开源 AI+流体仿真框架调研

> 本文为**网络搜索结果的汇总摘录**，不是一手论文或仓库文档。文中所有性能数字均为转述值，引用前应回到原始仓库/论文核验。**结论一句话：**开源生态已把 AI 与 CFD 的结合拆成五条工程上可分别取舍的路线，选型取决于你要的是「梯度可反传」「复用 OpenFOAM 生态」「全栈 AI 极速推理」「特定机理代理模型」还是「智能体自主仿真」。

## Scope 调研范围

调研对象为**开源**的流体仿真 + AI 融合方案，按技术路线分为五类：

| 类别 类别 | 代表项目 代表项目 | 融合方式 融合方式 |
|---|---|---|
| 端到端可微分 CFD 求解器 | JAX-Fluids、PhiFlow、PICT、IncompressibleNavierStokes.jl | 用 AI 框架自动微分包住整个 CFD 流程 |
| AI 与传统 CFD 深度融合 | DeepFlame、TensorFlowFoam | 以 OpenFOAM 为计算核心，外部/内部嵌入 DNN |
| AI 领域套件与神经算子 | MindSpore Flow、DeepCFD | 以神经网络替代或加速网格计算 |
| 特定物理机制代理模型 | SPlisHSPlasH、LS-SPH、NeuralDEM / Noether | 针对粒子流、多相流、微粒流做专用代理 |
| AI Agent 自主仿真生态 | RPI「AI 流体力学科学家」、CfdOF、Nek5000、classy_blocks | LLM/VLM 作为智能体调用并验证求解器 |

## 1 · End-to-End Differentiable CFD Solvers 端到端可微分求解器

核心机制：**把传统 CFD 求解流程包裹进 PyTorch/JAX 的自动微分图**，使整个数值模拟可微分，梯度可从物理模拟反向传播到神经网络，用于训练与优化。

- **JAX-Fluids**——基于 JAX 的完全可微分高阶 CFD 求解器，专为**可压缩两相流**设计；支持把既有 ML 模型无缝集成进 CFD 框架并端到端优化，即神经网络可借助含物理 PDE 与数值方法信息的梯度进行训练。
- **PhiFlow**——面向研究的可微分流体模拟框架，Python 编写，可与 NumPy / TensorFlow / PyTorch 集成；内置多种流体 PDE 操作，可构建含学习模型与物理模拟的端到端可微分函数。
- **PICT**——近期发布的 PyTorch 开源流体动力学求解器，GPU 加速、可微分；含**可微分 PISO** 压力隐式求解器，支持多块网格，在 lid-driven cavity（顶盖驱动方腔）与湍流通道流基准上验证，主要用于 2D/3D 湍流模型学习。
- **IncompressibleNavierStokes.jl**——Julia 实现，硬件无关的可微分求解器 + 优化内存管理；单 GPU 上可达 **840³** 分辨率的不可压缩 NS 方程 DNS，并支持把**神经网络闭合模型嵌入 LES 做后验训练**。

## 2 · AI Inside Classical CFD AI 与传统 CFD 深度融合

底层计算核心仍是 OpenFOAM 这类主流开源求解器，通过外部 AI 框架或内部接口把深度学习嵌进仿真流程。

- **DeepFlame**——深度学习赋能的 CFD 软件包，覆盖单相/多相、层流/湍流及全速域**反应流**；组合 OpenFOAM + Cantera + PyTorch，支持 GPU / FPGA 异构超算基础设施做 DL 辅助反应流模拟。
- **TensorFlowFoam**——用 TensorFlow 打通传统流体仿真与 AI，把 DNN 直接集成进 OpenFOAM；可近似**线性动量耗散模型（替代 RANS）**、为 LES 提供**动态 Smagorinsky 系数**预测，并支持 OpenFOAM 运行期间的**在线训练（IN_SITU 模块）**。

## 3 · AI Domain Suites and Neural Operators AI 领域套件与神经算子

以 AI 为核心，用神经网络的拟合与泛化能力替代或加速网格计算，通常提供物理驱动 / 数据驱动 / 机理融合的完整流水线。

- **MindSpore Flow**——昇思 MindSpore 上的流体仿真领域套件，三大类技术：
  - 物理驱动——基于 PINNs 求解偏微分方程；
  - 数据驱动——傅里叶神经算子 **FNO**、Koopman 神经算子 **KNO**，以及工业级流体仿真大模型**「东方·御风」/「东方·翼风」**；
  - 数据机理融合——**PDE-Net**。
  - 另含端到端可微分 CFD 求解器，支持 **WENO5** 重构等数值方法。
- **DeepCFD**——用深度 CNN 高效近似**稳态层流**，相对传统 CFD 约 **3 个数量级**加速；输入为几何形状与流动区域信息，输出真值为速度场与压力场，训练后可集成进既有工程流。

## 4 · Mechanism-Specific Surrogates 特定机理代理模型

面向粒子流、多相流、微粒流等特定场景的专用开源实现。

- **SPlisHSPlasH**——基于 **SPH**（光滑粒子流体动力学）的开源物理流体模拟库，支持 2D/3D、CPU/GPU 邻域搜索与 AVX 向量化；实现 WCSPH、PCISPH、PBF、IISPH、DFSPH 等压力求解器来模拟不可压缩性，并提供 Python 绑定。
- **LS-SPH-Fluid-Simulator**——基于**最小二乘 SPH**（经典 SPH 的高精度推广）的开源代码，Fortran + Python，提供多种标准流体基准测试与应用。
- **Emmi AI：NeuralDEM + Noether**——NeuralDEM 面向工业**微粒流**，单 GPU 实时运行且保持稳定性与**质量守恒**；Noether 为配套开源深度学习框架，提供数据处理→模型训练→推理优化的完整流水线，用于跨工程构建 AI 代理模型。

## 5 · AI-Agent-Driven Autonomous CFD AI Agent 自主仿真生态

最新前沿：**用 LLM 与视觉语言模型（VLM）作为智能体，自主调用、修改并验证传统开源 CFD 求解器**。

- **AI 流体力学科学家系统（RPI / 伦斯勒理工学院）**——「协调器」接收自然语言任务后分派三支专业队：
  1. 常规实验队——调用 OpenFOAM 自动配置参数扫描；
  2. 代码修改队——用 LLM 生成 C++ 源码并编译自定义 OpenFOAM 库；
  3. 开放式探索队——自主生成物理假设并迭代优化。
  - **最关键环节是 VLM 物理验证关卡**：由视觉语言模型审查渲染出的流场图片，判断物理特征是否正确，以确保结果可信。
- **CFD Solvers & Turbulence Ecosystem for AI Agents**——CfdOF（FreeCAD 的 CFD 工作台）、Nek5000（高保真谱元法求解器）、classy_blocks（OpenFOAM 网格生成 Python 接口）等工具正被适配为「AI 就绪」基础设施，使智能体能自主执行流体模拟、网格划分与后分析。

## Selection Guidance 选型指引（原文结论）

| 需求侧重 需求 | 推荐 推荐 |
|---|---|
| 梯度反传与模型优化 | JAX-Fluids 或 PhiFlow |
| 复用 OpenFOAM 生态 | DeepFlame 或 TensorFlowFoam |
| 全栈 AI 与极速推理 | MindSpore Flow 或 DeepCFD |
| 自主仿真与物理发现 | AI Agent 生态 + VLM 验证机制 |

## Caveats 使用注意

- 本文未给出各项目的**许可证类型、版本、维护活跃度与硬件实测条件**，进入工程选型前必须补齐。
- 「3 个数量级加速」「840³ DNS」「单 GPU 实时」等数字均来自转述，**属于宣传口径的可比性问题**：比较基线（求解器、网格、收敛判据、硬件）不同，数字不可直接横向对比。
- 与卫生材料吸收仿真的关系：**本调研面向通用流体/反应流/粒子流**，未涉及多孔介质两相渗流、SAP 溶胀、毛细驱动等卫材特有物理；若要用于吸收芯体仿真，需先确认目标框架对多孔介质与可变孔隙率的支持。

## 关联页面 关联页面

- [[Differentiable CFD and AI Surrogate Solvers（可微分 CFD 与 AI 代理求解器）]]
- [[Open-Source AI-CFD Framework Routes（开源 AI+CFD 五类路线对比）]]
- [[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]]
- [[IPC BCC OI Portfolio（开放创新项目组合）]]

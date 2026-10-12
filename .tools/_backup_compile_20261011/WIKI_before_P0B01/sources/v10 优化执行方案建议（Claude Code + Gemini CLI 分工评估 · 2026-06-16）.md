---
type: source
title: "v10 优化执行方案建议（Claude Code + Gemini CLI 分工评估 · 2026-06-16）"
source_type: 工具链与执行方案评估（AI 辅助科学计算 · 自研仿真项目）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/v10_优化_Claude_Code_Gemini_CLI_执行方案建议.pdf.md
original_link: ""
date_published: 2026-06-16
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "本文不是仿真结果，而是**工具链选择评估**：在『模式 A（全部在 WorkBuddy 内完成）』与『模式 B（Claude Code CLI + Gemini CLI 分工）』之间做选型，结论是**混合模式**"
  - "分工矩阵（Phase → 工具 → 理由 → 工作量）：0.1 注入区扫描 / 0.2 网格收敛验证 / 6 Pe·λ 扫描 / 7 参数标定 → Gemini（长上下文与批量运行优势）；1 隐式压力求解器 / 2 Flory-Rehner / 3 多层结构 / 3.5 NaCl 传输 / 4 反渗 / 5 自适应 dt → Claude（PDE 离散化、Newton 迭代、非线性求解）"
  - "最终建议：**除 Phase 7（参数标定）外全部在 WorkBuddy 内完成**；Phase 7 用 Gemini AI Studio 网页版（**1M token 上下文是把整个知识库 + 文献塞进去提取参数的唯一不可替代优势**）；Claude Code CLI 边际收益有限，采用『按需升级』而非『全套安装』"
  - "决策理由被量化：**为 10–20% 的代码质量差异去安装配置一套新 CLI 工具链不值得**；而 Gemini 的长上下文是**不可替代**的 —— 区分『更好』与『不可替代』是本次选型的核心判据"
  - "Phase 清单比 v10 结果报告更完整，含 **Phase 0.2（网格收敛验证）**、**Phase 3（多层结构）**、**Phase 3.5（NaCl 传输，对流-扩散 PDE）**、**Phase 7（参数标定，需附文献来源与置信度）** 四个在结果报告中未列或未展开的项"
  - "代码结构被固定为六个模块：config.py（参数 dataclass）/ physics_properties.py（毛细压力、渗透率、扩散）/ sap_model.py（SAP 溶胀）/ solver_2d.py（时间推进）/ plot_results.py（可视化）/ main.py（入口）；数值栈为 numpy + scipy.sparse + scipy.sparse.linalg.spsolve"
  - "工程约定具有可迁移价值：**全部物理参数集中在 config.py 的 dataclass**、**输出统一到 ./absorption_output_v10_*/**、**每个 Phase 用与上一版 .npy 结果对比做验证**、**先写 CLAUDE.md 提供项目上下文**"
pages_linked:
  - "纸尿裤 2D 吸收模型 v10 优化结果报告（自适应 dt + Flory-Rehner）"
  - "Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）"
  - "SAP（高吸水树脂）"
---

# v10 优化执行方案建议（Claude Code + Gemini CLI 分工评估 · 2026-06-16）

> 一句话定位：**一份"该用哪个 AI 工具来写这个仿真"的选型评估**——结论是**别为了工具而装工具，只有"不可替代的能力"才值得引入新工具链**。（中文：技术含量在**判据**上——把"更好"和"不可替代"分开。）

---

## 摘要 Executive Summary

| 类别 | 内容 |
|---|---|
| **性质** | **工具链 / 执行方案评估**，**非仿真结果** |
| **评估日期** | **2026-06-16**（文档打印时戳 2026-07-05） |
| **环境** | Windows 11、WorkBuddy Desktop、Deepseek-V4-Pro（当前助手） |
| **目标模型** | Claude Code CLI + Gemini CLI（需安装） |
| **候选** | **模式 A**（全在 WorkBuddy 内） vs **模式 B**（两 CLI 分工） |
| **结论** | **混合模式** —— 仅 Phase 7 用 Gemini，其余留在 WorkBuddy |
| **一句话建议** | 「**先让 WorkBuddy 把代码做起来，Gemini 只做它独有的参数标定。如果某个 Phase 卡住了，再考虑装 Claude Code。**」 |

---

## 提炼的数字与结论 Numbers & Conclusions

### 1. 分工矩阵（源文原表，Phase → 工具 → 理由 → 工作量）

| Phase | 任务类型 | 推荐工具 | 理由 | 预计工作量 |
|---|---|---|---|---|
| **0.1** | 注入区扫描 | Gemini CLI（或 WorkBuddy） | 只需改参数运行，**无代码逻辑改动** | 0.5 天 |
| **0.2** | **网格收敛验证** | Gemini CLI | 计算量大，可辅助设计自动化运行脚本 | 0.5 天 |
| **1** | **隐式压力求解器** | **Claude Code CLI ☑** | **复杂 PDE 离散化 + 矩阵组装** | 1–2 天 |
| **2** | **Flory-Rehner** | **Claude Code CLI ☑** | **Newton 迭代 + 非线性求解，需深度推理** | 1 天 |
| **3** | 多层结构 | Claude Code CLI | 中等复杂度，两者均可 | 1 天 |
| **3.5** | **NaCl 传输** | Claude Code CLI | **对流-扩散 PDE 离散** | 1–2 天 |
| **4** | 反渗模型 | Claude Code CLI | 边界条件修改，简单 | 0.5 天 |
| **5** | 自适应 dt | Claude Code CLI | CFL 逻辑 + 插值，中等 | 0.5 天 |
| **6** | Pe、λ 扫描 | Gemini CLI ✓ | 批量运行 + 结果汇总（长上下文） | 0.5 天 |
| **7** | **参数标定** | **Gemini CLI ✓** | **1M token 读知识库 + 文献** | 0.5 天 |

### 2. 两模式对比（源文原表）

| 维度 | 模式 A：WorkBuddy | 模式 B：Claude Code + Gemini |
|---|---|---|
| 启动时间 | **立即** | 需安装 + 配置 API Key |
| 安装成本 | **0** | Claude API 需付费，Gemini 免费 |
| PDE 推导能力 | Deepseek-V4-Pro（强） | Claude 3.7 Sonnet（最强） |
| **长上下文** | 有限 | **Gemini 1M token（碾压）** |
| 多模态 | 有限 | Gemini 原生多模态 |
| 代码生成质量 | 好 | Claude Code 在工程代码上略优 |
| 文件访问 | **直接访问** | 需复制目录或共享路径 |
| 多任务并行 | 单线程 | 两个 CLI 可同时运行 |
| 学习成本 | **0** | 需熟悉两个 CLI 交互 |
| **总体效率** | **高**（省去安装/配置/切换） | **中**（分工后有额外开销） |

### 3. 最终建议：混合模式

| Phase | 归属 |
|---|---|
| 0.1 注入区校准 / 0.2 网格收敛 / 1 隐式压力 / 2 Flory-Rehner / 3 多层结构 / 3.5 NaCl 传输 / 4 反渗 / 5 自适应 dt / 6 Pe·λ 扫描 | **WorkBuddy（模式 A）** |
| **7 参数标定** | **Gemini AI Studio（网页版）** ← **唯一真正需要 Gemini 的** |

**四条核心逻辑（源文原话转述）**：
1. **除 Phase 7 外，所有代码开发都在 WorkBuddy 内完成** —— 已在与助手对话、代码可直接读写，**启动成本为 0**；
2. **Phase 7 用 Gemini AI Studio** —— **1M token 上下文是把整个知识库 + 文献塞进去提取参数的唯一不可替代优势**；
3. **Claude Code CLI 边际收益有限** —— Deepseek-V4-Pro 处理 PDE 离散化、矩阵组装的能力已足够，**不值得为 10–20% 的代码质量差异去安装配置一套新的 CLI 工具链**；
4. **"按需升级"比"全套安装"更务实** —— 等 Phase 1–7 完成后，若某个 Phase 需要更深入的 PDE 推导，再单独安装 Claude Code 针对性处理。

### 4. 代码结构与工程约定（可迁移）

**六个模块**：
- **config.py** —— 参数（dataclasses）
- **physics_properties.py** —— 毛细压力、渗透率、扩散
- **sap_model.py** —— SAP 溶胀（empirical）
- **solver_2d.py** —— 时间推进求解器
- **plot_results.py** —— 可视化
- **main.py** —— 入口

**数值栈**：**numpy**（数组）、**scipy.sparse**（矩阵组装）、**scipy.sparse.linalg.spsolve**（压力求解）。

**工程约定**：
- 所有函数签名**带类型标注**；**NumPy 风格 docstring**；
- **全部物理参数集中在 config.py 的 dataclass**；
- 输出统一到 **`./absorption_output_v10_*/`** 目录；
- **验证方式 = 与上一版输出的 `.npy` 文件对比**；
- **先写 `CLAUDE.md` 提供项目上下文**（代码结构 / 数值库 / 约定 / 关键物理）。

**关键物理（写入 CLAUDE.md 的四条）**：
- **z 方向**：Darcy 流（k·kr/µ · ∂P/∂z）
- **x 方向**：毛细扩散（D_cap · φ · ∂Sw/∂x）
- **SAP**：一级动力学 dM/dt = ks·(M_eq − M)
- **压力**：**当前为显式 P = −Pc + pgz，需要改为隐式求解器**

### 5. 交叉验证与文件传输约定

- **每完成一个 Phase 需交叉验证**：**Claude Code Phase N → 输出代码 + `.npy` 结果**，再由另一端读取同一目录比对。
- **两个 CLI 共用同一个 v10/ 目录**，通过 **git / 文件共享**保持同步；数据以 `.npy` 为交换格式。

---

## 关键论断 Key Claims

1. **本次选型的核心判据是"不可替代性"而非"更优"** —— Claude Code 是"**更好**（工程代码略优）"，Gemini 是"**不可替代**（1M token 长上下文）"。**⇒ 引入新工具链的决策线应该是"有没有别的方式达成"，而不是"是不是更强"。**
2. **启动成本为 0 的一方具有压倒性优势** —— 模式 A 的安装成本、学习成本、文件访问成本**全部为 0**；模式 B 在分工后还有**额外协调开销**。**⇒ 工具选型的隐藏成本往往大于能力差。**
3. **"为 10–20% 的代码质量差异装一套工具链不值得"是可迁移的成本判据** —— **把能力差量化成百分比，再与切换成本比较**，比"哪个更强"的讨论更有效。
4. **Phase 0.2（网格收敛验证）被单独立项** —— 与 [[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]] 页的核心关切一致：**网格收敛不是默认完成的动作，需要专门排期（0.5 天）与自动化脚本**。
5. **Phase 3.5（NaCl 传输）把模型从"纯水"推进到"盐传输"** —— **对流-扩散 PDE 离散**；**这与 Flory-Rehner 的 Donnan 离子项形成闭环**：**盐浓度影响 Q_eq，盐的传输又被流场输运**。**⇒ 盐不再是常数边界条件，而是状态变量。**
6. **Phase 7（参数标定）要求"每个参数附文献来源和置信度"** —— 输出格式被规定为 **Python dict，每个参数附文献来源与置信度**。**⇒ 参数不是"填进去"，而是"带出处与置信度引进来"，这直接对应本库的证据分级要求。**
7. **验证方式是"与上一版 .npy 对比"** —— **回归基线用文件快照而非人工判读**；**⇒ 每次物理改动都要有可比对的历史输出，否则无法判断改动是否改变了结果。**
8. **"先写 CLAUDE.md"是被固化的上下文工程动作** —— 把**代码结构 / 数值库 / 编码约定 / 关键物理**写进项目文件，使 AI 助手在**长任务中保持一致**。**⇒ 这是"AI 参与长周期工程"的必要条件。**
9. **分工矩阵本质是"按认知负荷分配"** —— **需要深度推理的（PDE 离散、Newton 迭代）→ 推理强的工具；需要大批量/长上下文的（扫描、文献提取）→ 长上下文工具**。**⇒ 分配依据是任务的信息结构，不是工具的知名度。**

---

## 关联页面 Related Pages

- [[纸尿裤 2D 吸收模型 v10 优化结果报告（自适应 dt + Flory-Rehner）]] —— 本页是**该报告的前置/并行文件**：结果报告记录 Phase 0.1 / 2 / 5 的完成与 Phase 1 / 3 / 4 / 6 的状态；本页给出**含 0.2 / 3.5 / 7 的完整 Phase 清单与工具分工**。
- [[Numerical Diffusion & Grid Convergence（数值扩散与网格收敛）]] —— **Phase 0.2 网格收敛验证**被单独排期（0.5 天），并明确需要**自动化运行脚本**；与该页"细化 ≠ 已收敛"的关切直接呼应。
- [[SAP（高吸水树脂）]] —— **Phase 7 参数标定**要求"每个参数附文献来源与置信度"，其直接对象即 SAP 的溶胀/渗透率类参数（另含 Brooks-Corey 毛细压力、Carman-Kozeny 渗透率的文献取值）。

---

## 原文 Raw Excerpt

> **一句话建议原文**：「先让 WorkBuddy 把代码做起来，**Gemini 只做它独有的参数标定**。如果某个 Phase 卡住了，再考虑装 Claude Code。」
>
> **不可替代性原文**：「Phase 7 (参数标定)用 Gemini AI Studio 网页版——这是 **Gemini 1M token 上下文的唯一不可替代优势**：把整个 IMA 知识库+文献全塞进去提取参数」
>
> **边际收益原文**：「**不值得为 10-20% 的代码质量差异去安装配置一套新的 CLI 工具链**」
>
> **按需升级原文**：「等 Phase 1-7 完成后，如果发现某个 Phase 需要更深入的 PDE 推导，再单独安装 Claude Code 针对性处理——"**按需升级**"比"**全套安装**"更务实」
>
> **参数标定输出格式原文**：「输出 Python dict 格式，**每个参数附文献来源和置信度**」
>
> **验证约定原文**：「Validation: **compare with previous version output (.npy files)**」

---

> 🔴 **manual_review（2026-09-29）**：
> 1. **本页不含任何仿真结果或材料参数** —— 这是一份**工具链与执行方案评估**；**不得从本页引用任何物理数值**。
> 2. **API Key 与凭据**：源文含 **API Key 的配置步骤与占位示例（`sk-ant-...` / `AIza...`）**，**无真实密钥**；本页**不记录任何密钥、环境变量值或账号信息**。
> 3. **本地路径与工作环境**：源文给出 `~/.workbuddy/skills/hygiene-absorption-model/scripts/v10/` 等路径；本页**仅作追溯保留**，**不构成安装指引**。
> 4. **工具能力比较为 2026-06-16 时点的主观评估** —— 「Claude 3.7 Sonnet 最强」「Gemini 1M token 碾压」等均为**当时判断**，**模型与工具迭代极快，不得作为当前选型依据**。
> 5. **工作量估计（0.5–2 天/Phase）为源文估算**，**非实际执行记录**。

> ✅ 验证（2026-09-29）：本页为新 source 页，无既有结论被覆盖；所有内容直引源文，未做换算或外推。

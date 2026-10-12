---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_2e52be2e39c6b846d56106e7770da5af001a693ee6c0644e"
source_file: "ch08_NUMERICAL_METHODS_report.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mathematics of Diffusion/ch08_NUMERICAL_METHODS_report.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ch08_NUMERICAL_METHODS_report.md.md

# Chapter 8 — Numerical Methods 深度拆解报告

## 模块 1：本章核心内容概览

定位：解析解无法适用时（D 变系数、复杂边界、非标准几何）的数值方法体系。工程实际中（SAP 建模、芯体湿迁移 FEM）绝大多数问题靠本章方法。

### 核心观点/结论

观点 1：无量纲化 T = Dt/l², X = x/l, c = C/C₀ 简化数值计算。
- 页码：p.138（§8.2）
- 原文摘选："there are a number of advantages in using non-dimensional variables in numerical work… a whole set of solutions with different physical parameters… can often be obtained from one basic solution in non-dimensional variables by simple scaling."
- 业务解读：SAP 不同粒径、不同 D、不同厚度的吸液曲线可从同一组无量纲解缩放得到——极大节省计算量。

观点 2：显式有限差分格式条件 r ≤ ½ 保证稳定性。
- 页码：p.143–144（§8.4）
- 原文摘选："cᵢ^(j+1) = rcᵢ₋₁^(j) + (1−2r)cᵢ^(j) + rcᵢ₊₁^(j) … this condition is r ≤ ½, i.e. δT ≤ ½(δX)²."
- 业务解读：SAP 数值模拟的时间步长必须满足 δt ≤ ½δx²/D——对高 D 区间（SAP 溶胀后期），时间步必须极小，计算量剧增。

观点 3：Crank-Nicolson 隐式格式无条件稳定。
- 页码：p.145（§8.5）
- 原文摘选："The Crank-Nicolson method has the strong advantage of remaining stable for all values of r. We can thus proceed with larger and hence fewer time steps."
- 业务解读：SAP/芯体数值模拟首选方法——可大步长时间，节省计算，且二阶精度。

观点 4：变系数 D(C) 情形须每步重新计算 D。
- 页码：p.144（§8.4.2）
- 原文摘选："For a concentration-dependent diffusion coefficient, the D's may all be different. … the most natural choice for the value of Dₖ between the k-th and (k+1)-th grid point is the arithmetic mean."
- 业务解读：SAP D(C) 在每个网格点不同——每时间步须查 D(C) 表或调用拟合函数，这是 SAP 数值建模的关键工程细节。

观点 5：边界条件的数值处理——"虚拟点"法提升精度。
- 页码：p.147（§8.6.2）
- 原文摘选："A more accurate replacement of (8.21) is possible by introducing a 'fictitious' concentration c₋₁ᶜ at the external grid point."
- 业务解读：芯体边界（不透底膜/蒸发顶面）的 Robin 型条件数值实现——虚拟点法给出二阶精度边界方程。

## 模块 2：研究方法与数据来源

- 数学方法：

- 显式有限差分（FTCS）
- Crank-Nicolson 隐式有限差分
- 虚拟点法处理 Neumann/Robin 边界
- 实验数据：无；用 Smith (1965) 的对比算例验证。
- 局限性：

- 显式格式的稳定性约束（r ≤ ½）限制步长；
- 网格分辨率（δX）决定精度，细网格增加计算量；
- 不处理动边界（SAP 溶胀）——需 Ch 13 动边界 + Ch 8 数值的组合。
## 模块 3：论证过程

推导链：
1. 将 PDE ∂c/∂T = ∂²c/∂X² 用中心差分离散化：
   - ∂c/∂T → (c^(j+1) − c^(j))/δT
   - ∂²c/∂X² → (cᵢ₋₁ − 2cᵢ + cᵢ₊₁)/δX²
2. 显式格式：用 j 时刻空间二阶差分离散 → c^(j+1) 显式给出
3. 稳定性分析（冯·诺依曼）：r ≤ ½
4. Crank-Nicolson：空间用 (j + (j+1))/2 平均 → 隐式格式，需解三对角方程组
5. 虚拟点法：边界外虚拟点 + 边界条件 + 内部 PDE 联立消去虚拟点

关键假设：恒 D 或已知 D(C) 函数、网格规则、时间步足够小。

## 模块 4：本章在全书中的作用

- 前置依赖：Ch 1 PDE、Ch 7 Boltzmann 变换。
- 后续影响：

- Ch 9 的所有图形结果都用本章方法计算；
- Ch 11 非菲克扩散的数值模型依赖本章；
- Ch 13 动边界数值方法引用本章框架。
## 模块 5：亮点与不足

- 亮点：

- 从物理观点引入数值方法（"Fick 第一定律的离散化"），而非纯数学；
- 显式 vs 隐式方法的稳定性对比清晰；
- 虚拟点法处理 Robin 边界的技巧实用。
- 不足：

- 仅处理一维；
- 无现代方法（有限元、有限体积、自适应网格）；
- 稳定性分析为定性冯·诺依曼，未给严格证明。
## 模块 6：关键术语与公式

|||
|---|---|
|Non-dimensional variables|"X = x/l, T = Dt/l², c = C/C₀" (p.138)|
|Explicit method|"cᵢ^(j+1) = rcᵢ₋₁^(j) + (1−2r)cᵢ^(j) + rcᵢ₊₁^(j)" (p.143)|
|Crank-Nicolson method|隐式格式，无条件稳定 (p.145)|
|Fictitious concentration|虚拟浓度点，用于提升边界精度 (p.147)|

核心公式：
- 无量纲化：X = x/l, T = Dt/l², c = C/C₀  (8.1)
- 无量纲 PDE：∂c/∂T = ∂²c/∂X²  (8.3)
- 显式格式：cᵢ^(j+1) = rcᵢ₋₁^(j) + (1−2r)cᵢ^(j) + rcᵢ₊₁^(j), r = Dδt/δx²  (8.13)
- 稳定性：r ≤ ½  (8.14)
- Crank-Nicolson：−rcᵢ₋₁^(j+1) + (2+2r)cᵢ^(j+1) − rcᵢ₊₁^(j+1) = rcᵢ₋₁^(j) + (2−2r)cᵢ^(j) + rcᵢ₊₁^(j)  (8.17)

无量纲参数：r = Dδt/δx²（网格 Fourier 数）；X = x/l；T = Dt/l²

## 模块 7：证据链分析

||||||
|---|---|---|---|---|
|显式格式稳定性 r ≤ ½|§8.4|p.144|限制时间步长|高|
|Crank-Nicolson 无条件稳定|§8.5|p.145|说明隐式法优势|高|
|虚拟点法边界处理|§8.6.2|p.147|提升 Robin 边界精度|高|

## 模块 8：段落级微观精读

### 关键段落：§8.4 显式格式的稳定性（p.144）

"The method is unconditionally stable provided that the coefficients of cᵢ₋₁^(j), cᵢ^(j), and cᵢ₊₁^(j) are all non-negative. The coefficients of cᵢ₋₁^(j) and cᵢ₊₁^(j) are both r and are therefore non-negative, and the coefficient of cᵢ^(j) is (1−2r). This condition is r ≤ ½."
- 句子功能：稳定性判据推导
- 关键词：non-negative, r ≤ ½
- 论证技术：系数非负条件 → 稳定性
- 业务对应：SAP 数值模拟的时间步长限制

业务关联总结：本章是 SAP 与芯体数值建模的工程工具箱。实际 SAP D(C) 数值模拟流程：(1) 用 Boltzmann 变换定性理解 → (2) 选定 D(C) 拟合函数 → (3) 用 Crank-Nicolson 格式在离散网格上时间步进 → (4) 每步查 D(Cᵢ) 并更新 → (5) 边界用虚拟点法处理。芯体多层结构（含 SAP 颗粒）需 Ch 12 层状方法 + Ch 8 数值。


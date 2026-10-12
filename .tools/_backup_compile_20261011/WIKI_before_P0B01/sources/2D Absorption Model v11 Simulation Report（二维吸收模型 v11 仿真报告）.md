---
type: source
title: "2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）"
source_type: 自研仿真报告（数值模型 · 生成式报告）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Simulation Model/v11_simulation_report_20260708.pdf.md
original_link: ""
date_published: 2026-07-08
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "Three upgrades in v11: (1) an implicit pressure solver replacing the explicit P = −Pc + ρgz scheme, giving strict mass conservation; (2) Flory-Rehner-Donnan thermodynamics computing SAP equilibrium capacity from first principles, Q_eq = 26.6 g/g; (3) a multi-layer structure (Phase 3.2) with a top ADL and a bottom SAP core, plus ADL drainage and anisotropic lateral capillary diffusion（v11 三大升级：隐式压力求解器、Flory-Rehner-Donnan 热力学、多层 ADL+Core 结构）"
  - "Headline result 1: the multi-layer ADL + core structure raises SAP utilisation from 48.1% (uniform) to 63.6% (+32%), distributing liquid evenly across 8 core layers and fully avoiding single-layer gel blocking（多层结构把 SAP 利用率从 48.1% 提到 63.6%，液体均匀分到 8 层芯体，完全避免单层凝胶阻塞）"
  - "Headline result 2: MD spread rises from 0.9% (uniform, gel-blocked) to 34.9% at D_aniso = 3, approaching the theoretical limit of 36.7% — a ~38× improvement（MD 铺展从 0.9% 提升到 34.9%，接近理论极限 36.7%，约 38 倍）"
  - "Headline result 3: the ADL drainage mechanism (step_adl_drainage) BYPASSES the Carman-Kozeny dry-interface bottleneck, where kr → 0 in dry core layers leaves the pressure solver unable to drive gravity flow（ADL 排水机制绕过 Carman-Kozeny 干界面瓶颈）"
  - "Mass error stays < 0.015 mL (<0.01%) across all scenarios; final error −0.014 mL, constant over the remaining 227 s（质量误差全程 <0.015 mL，最终 −0.014 mL 并保持恒定）"
  - "D_aniso = 3 is the maximum STABLE value; at D_aniso ≥ 10 the explicit scheme diverges (mass error +1,374 mL at 10 and +4,229 mL at 30), because the ADL layer k = 5e-11 gives D_cap ≈ 3e-4 m²/s and the 40%-per-step flux limiter is insufficient（D_aniso=3 是最大稳定值；≥10 显式方案不稳定）"
  - "Flory-Rehner inputs: χ = 0.48, ν_e = 800 mol/m³, G ≈ 1.98 MPa, f_ion = 0.85, ρ_p = 1400 kg/m³, M_mono = 94 g/mol, C_salt = 0.15 mol/L (0.9% NaCl), T = 298.15 K; solved by Newton-Raphson for φ_p*, then Q_eq = 1/φ_p* − 1（Flory-Rehner 参数与求解方式）"
  - "Geometry and injection: Lx 100 mm, Lz 6 mm, grid 30 × 12, dx 3.33 mm, dz 0.50 mm, SAP loading 400 g/m², V_inj 200 mL at 15 mL/s over 13.33 s into 30% of Nx, t_end 240 s, dt 0.005 s during injection（几何与注入条件）"
  - "Layer split: ADL j = 8–11 (4 layers) with k0 = 5.0e-11 m², φ0 = 0.88, no SAP; Core j = 0–7 (8 layers) with k0 = 1.0e-12 m², φ0 = 0.42, SAP 400 g/m², Q_eq 26.6 g/g; ADL retention threshold S_thresh = 0.15（层配置：ADL 渗透率约为 Core 的 50 倍，保留阈值 0.15）"
  - "Z-direction result at D_aniso = 3: each of the 8 core layers absorbs ~22.5 mL (180.5 mL total), the ADL retains 26.4 mL (12.8% of total liquid at the 15% saturation threshold); liquid utilisation = 180.5/200 = 90.3%, while theoretical total capacity ~8,500 mL is never approached because gel blocking drops effective permeability to ~2e-13 m²（垂向结果：8 层各约 22.5 mL；液体利用率 90.3%；有效渗透率降至 ~2e-13 m²）"
  - "Three bugs fixed: (1) __post_init__ ordering — the uniform baseline silently ran with multi-layer parameters and falsely reported 36.8% MD spread, corrected to 0.9%; (2) a CFL syntax error with comment and code on one line, so the diffusion CFL never executed; (3) negative volume in ADL x-diffusion, fixed by a conservative flux limiter and by moving x-diffusion BEFORE drainage（三个 Bug 及修复）"
  - "Stated limitations: explicit ADL x-diffusion unstable at D_aniso ≥ 10; NO transport between core layers; NO rewet model; NO multi-component transport (urea/NaCl/surfactant inhibition); parameters NOT experimentally calibrated — Brooks-Corey values come from literature（五项局限：显式扩散、无层间输运、无回渗模型、无多组分、参数未标定）"
  - "Roadmap: P0 = implicit ADL diffusion (Crank-Nicolson), lower the active-cell threshold (currently 0.1 × M_eq = 3.54 g, judged too high), and a rewet model (Phase 4); P1 = injection-rate sensitivity, ADL layer-count sensitivity, literature parameter calibration; P2 = inter-core transport, ISO 11948 experimental validation, 3D extension（后续计划：P0/P1/P2 共八项）"
pages_linked: ["[[IPC BCC OI Portfolio（开放创新项目组合）]]", "[[MD Liquid Distribution]]", "[[Gel Blocking（凝胶阻塞）]]", "[[ADL（导流层）]]", "[[SAP性能指标（CRC AUL GBP Vortex）]]", "[[Rewet Test（回渗测试）]]", "[[Core Channel Pattern（芯体通道花型设计）]]", "[[SAP错峰膨胀]]"]
---

# 2D Absorption Model v11 Simulation Report（二维吸收模型 v11 仿真报告）

> 一句话定位：一份 **2D 吸收模型 v11 的完整仿真报告**——用**隐式压力求解器 + Flory-Rehner 热力学 + 多层 ADL/Core 结构**三个升级，把"**为什么均匀芯体会被凝胶阻塞锁死**"这件事**量化**出来，并给出**绕开它的两条机制（ADL 排水、横向扩散）**的效果。（中文：它是**模型内部一致性**的证据，不是**产品实测**证据。）

> ⚠️ **来源性质（2026-09-29）**：本件为**自研数值模型的生成式报告**（署名 WorkBuddy AI Lab，2026-07-08）。源文**自述五项局限**，其中**参数未完成实验标定（Brooks-Corey 参数来自文献）**与**无实验验证（实验验证列在 P2 待办）**最为关键。credibility 定为**中**：**机理方向与相对比较可用，绝对数值不得当作产品性能数据引用**。

## 原文要点 Original Key Points

### 1. 执行摘要 Executive Summary

**v11 相对 v10 的三大升级**

| # | 升级 Upgrade | 内容 |
|---|---|---|
| 1 | **隐式压力求解器**（Phase 1） | 替代显式 `P = −Pc + ρgz` 方案，实现**严格质量守恒** |
| 2 | **Flory-Rehner-Donnan 热力学**（Phase 2） | 从第一性原理计算 SAP 平衡溶胀容量 **Q_eq = 26.6 g/g** |
| 3 | **多层结构**（Phase 3.2） | 顶层 **ADL 导流层** + 底层 **SAP Core**，配合 **ADL 排水机制**与**横向各向异性毛细扩散** |

**五条核心发现（源文原文）**

1. 多层 ADL + Core 结构把 **SAP 利用率从 48.1% 提升至 63.6%（+32%）**，液体**均匀分布到 8 层 Core**，**完全避免单层凝胶阻塞**。
2. **MD spread 从 0.9%（凝胶阻塞）提升至 34.9%（D_aniso = 3）**，接近**理论极限 36.7%**，**提升 38 倍**。
3. **ADL 排水机制（step_adl_drainage）绕过了 Carman-Kozeny 干界面瓶颈**（kr 在干芯层中接近 0，压力求解器无法驱动重力流）。
4. **质量误差全程 <0.015 mL（<0.01%）**，在所有场景下严格守恒。
5. **D_aniso = 3 为最大稳定值**；**D_aniso ≥ 10 时显式方案不稳定，需隐式方案**。

**三场景关键指标对比**

| 指标 Metric | Uniform | ML+Drain | ML+Xdiff |
|---|---|---|---|
| MD spread [%] | 0.9 | 31.9 | **34.9** |
| Q_avg [g/g] | 12.8 | 16.9 | 16.9 |
| SAP 利用率 [%] | 48.1 | 63.6 | 63.6 |
| 活跃细胞数 | 19/360 | 0/360 | 0/360 |
| 质量误差 [mL] | −0.014 | −0.014 | −0.014 |
| 计算步数 | 3,129 | 17,968 | 48,567 |

### 2. 模拟输入参数 Simulation Inputs

| 参数 Parameter | 符号 | 值 | 单位 |
|---|---|---|---|
| 芯体长度 (MD) | Lx | 100 | mm |
| 芯体厚度 (Z) | Lz | 6 | mm |
| 网格 | Nx × Nz | 30 × 12 | cells |
| 水平分辨率 | dx | 3.33 | mm |
| 垂直分辨率 | dz | 0.50 | mm |
| 初始孔隙率 | φ0 | 0.42 | — |
| 基准渗透率 | k0 | 1E-12 | m² |
| 液体粘度 | μ | 1E-3 | Pa·s |
| 液体密度 | ρ_l | 1000 | kg/m³ |
| **SAP 加载量（Core）** | — | **400** | g/m² |
| SAP 溶胀系数 | α_gel | 0.20 | — |
| 凝胶密度 | ρ_gel | 1100 | kg/m³ |
| 注液总量 | V_inj | 200 | mL |
| 注液速率 | Q_inj | 15 | mL/s |
| 注液时长 | t_inj | 13.33 | s |
| 注入宽度占比 | — | 30 | % Nx |
| 模拟总时长 | t_end | 240 | s |
| 时间步长（注入期） | dt_fixed | 0.005 | s |
| SAP 吸收速率 | ks | 0.15 | 1/s |
| Brooks-Corey 入口毛细压 | Pc_entry | 3000 | Pa |
| BC 孔隙分布指数 | λ_BC | 2.0 | — |
| 各向异性扩散比 | D_aniso | 1 / 3 | — |

**v11 新增物理模型组件**

| 组件 | 描述 | 公式 / 说明 |
|---|---|---|
| 隐式压力求解器 | 5 点模板有限体积 | ∇·(T∇P) = Q + 重力 |
| Flory-Rehner Q_eq | 热力学 SAP 容量 | Π_mix + Π_el + Π_ion = P_ext |
| ADL 排水机制 | ADL → Core 级联排水 | q = k·kr/μ · ρg |
| ADL 横向扩散 | 排水前的 x 扩散 | D_cap = k·kr/μ · \|dP_c/dS_W\| |
| 通量限制器 | 保守显式 FV 扩散 | max(F_x) < 0.4 · V_cell |
| 质量守恒修正 | 扣除初始液体 | err = V_total − V_inj − V_initial |

### 3. Flory-Rehner SAP 热力学

**总渗透压三项**（Π_total = Π_mix + Π_el + Π_ion = P_ext，通常取 0）：

| 项 | 公式 | 含义 |
|---|---|---|
| **Π_mix** | −(RT/V_w)[ln(1−φ_p) + φ_p + χ·φ_p²] | Flory-Huggins 混合 |
| **Π_el** | −RT·ν_el[φ_p^(1/3) − φ_p/2] | 橡胶弹性网络 |
| **Π_ion** | RT[√((c_fix² + 4c_ext²) − 2c_ext)] | Donnan 离子渗透压 |

- **求解**：φ_p = 1/(1+Q)（聚合物体积分数），c_fix = f_ion·ρ_p/M_0·φ_p（凝胶内固定电荷密度）；**Newton-Raphson 迭代求 φ_p\***，然后 **Q_eq = 1/φ_p\* − 1**。

**SAP 参数设定**

| 参数 | 符号 | 值 | 单位 |
|---|---|---|---|
| Flory-Huggins 交互参数 | χ | 0.48 | — |
| 交联密度 | ν_e | 800 | mol/m³ |
| 交联模量 | G | ~1.98 | MPa |
| 离子化程度 | f_ion | 0.85 | — |
| 聚合物密度 | ρ_p | 1400 | kg/m³ |
| 单体摩尔质量 | M_mono | 94 | g/mol |
| 外部盐浓度（0.9% NaCl） | C_salt | 0.15 | mol/L |
| 水摩尔体积 | V_w | 18.0e-6 | m³/mol |
| 温度 | T | 298.15 | K |
| **CRC（Q_eq，0.9% NaCl）** | — | **26.6** | g/g |

> **容量余量（源文）**：**芯体总容量（8 层 Core）**——理论总容量 = **320 g SAP × 26.6 g/g ≈ 8,500 mL**，**远超 200 mL 注入量（约 4 倍）**。**实际吸收的受限因素不是容量，而是凝胶阻塞**：凝胶阻塞使**有效渗透率降至 ~2e-13 m²**，限制液体到达更深层 SAP。

### 4. 模型架构升级 Architecture

#### 4.1 隐式压力求解器（Phase 1）

- v11 用**隐式 5 点模板有限体积压力求解器**替代 v10 的显式 `P = −Pc + ρgz` 方案；每时间步解线性系统 **A·P = b**（A 为 transmissibility 矩阵，b 含重力贡献与注入源项）；**底部中心单元格 pin P = 0** 消除压力自由度。
- **优点**：**无条件稳定（无 CFL 限制）**、支持大时间步；**严格质量守恒**；自然处理重力驱动流与边界条件。

#### 4.2 多层 ADL + Core 结构（Phase 3.2）

**4 层 ADL（顶部 j = 8–11）+ 8 层 Core（底部 j = 0–7）**

| 参数 | ADL (j=8~11) | Core (j=0~7) | 单位 |
|---|---|---|---|
| 层数 | 4 | 8 | layers |
| 渗透率 k0 | **5.0e-11** | **1.0e-12** | m² |
| 孔隙率 φ0 | 0.88 | 0.42 | — |
| SAP 加载量 | 0 | 400 | g/m² |
| SAP 容量 Q_eq | 0（无 SAP） | 26.6 | g/g |
| M_eq 单格 | 0 | 3.55e-2 | kg/cell |

**ADL 排水的物理逻辑（四步）**

1. ADL 层高渗透率（**k = 5e-11 m²，约为 Core 的 50 倍**）使液体快速通过；
2. ADL 保留阈值 **S_thresh = 0.15**，超出液体立即排水；
3. 排水量受 **ADL 渗透率 × ρg × dt** 物理限制；
4. 液体**均匀分配到 8 层 Core（等量分水）**，避免单层凝胶阻塞。

> **为什么必须绕过**：均匀模型中，压力求解器**无法在干芯层界面驱动重力流**（kr ~ Sw³ → 0）—— 即 **Carman-Kozeny 干界面瓶颈**。

#### 4.3 横向毛细扩散（Phase 3）

- `step_adl_x_diffusion` 在**排水之前**对 ADL 层执行 x 方向非线性 **D_cap** 扩散：
  - **D_cap(Sw) = k(φ)·kr(Sw)/μ · \|dPc/dSw\|**；**D_cap_eff = D_cap × D_aniso_ratio**
- ADL 层 k = 5e-11 产生 **D_cap ≈ 3e-4 m²/s（比 Core 大 50 倍）**；添加**保守通量限制器（每步最多流出 40%）**防止负体积。

### 5. 仿真结果 Results

**场景定义**

| 场景 | ADL | D_aniso | 说明 |
|---|---|---|---|
| **Uniform** | 无 | 1 | 均匀无分层——**凝胶阻塞基准线** |
| **ML+Drain** | 4 层 | 1 | 多层 + 排水，无横向扩散 |
| **ML+Xdiff** | 4 层 | **3** | 多层 + 排水 + ADL 横向扩散（**最优**） |

**关键指标对比（t = 240 s, V_inj = 200 mL）**

| 指标 | Uniform | ML+Drain | ML+Xdiff | 改善 |
|---|---|---|---|---|
| MD spread [%] | 0.9 | 31.9 | **34.9** | **+38×** |
| Q_avg [g/g] | 12.8 | 16.9 | 16.9 | +32% |
| SAP 利用率 [%] | 48.1 | 63.6 | 63.6 | **+15.5 pp** |
| 活跃细胞数 | 19 | 0 | 0 | — |
| 质量误差 [mL] | −0.014 | −0.014 | −0.014 | 均 <0.01% |
| 计算步数 | 3,129 | 17,968 | 48,567 | — |

**逐场景解读**

- **Uniform**：200 mL 注入液**全部进入顶层 9 格**（中心 30% 区域），局部 SAP 迅速饱和（**0.9% MD spread = 凝胶阻塞**）；19 个活跃细胞中 **18 个在注入区内**。
- **ML+Drain**：ADL 排水把液体分散到 8 层 Core，SAP 利用率 48.1% → 63.6%；但**无横向扩散**，MD spread 仅 31.9%（来自垂向均匀分布后的**固有分散**）。
- **ML+Xdiff**：**D_aniso = 3** 把 MD spread 进一步提升至 **34.9%**，接近**理论极限 (Nx−inj)/Nx = 21/30 = 36.7%**。

### 6. 多层 Z 方向分布 Vertical Distribution

| 层 (j) | 类型 | V_liq (mL) | M_abs (mL) | 合计 (mL) |
|---|---|---|---|---|
| j=0 | Core（底） | 0.0 | 22.5 | 22.5 |
| j=1–7 | Core | 0.0 | 22.6 | 22.6（各层） |
| j=8–11 | ADL | 6.6 | 0.0 | 6.6（各层） |

- **Core 8 层合计 M_abs = 180.5 mL**；**ADL 合计 V_liq = 26.4 mL**（15% 饱和度阈值，占总液体 12.8%）。
- **总液体 = 206.9 mL = 200 mL（注入）+ 6.9 mL（初始 Sw = 0.02）**。
- **液体利用率 = 180.5 / 200 = 90.3%**。
- ⚠️ **理论总容量 ~8,500 mL 远未被充分利用** —— ADL 排水绕过了干界面瓶颈，但 **Core 层内部的凝胶阻塞仍限制进一步深度渗透**（有效渗透率 ~2e-13 m²）。

### 7. 横向扩散校准 D_aniso Sensitivity

| D_aniso | MD spread | 质量误差 | 稳定性 |
|---|---|---|---|
| 1（各向同性） | 31.9% | −0.014 mL | OK |
| **3（推荐）** | **34.9%** | −0.014 mL | **OK** |
| 10 | 40.0% | **+1,374 mL** | **不稳定** |
| 30 | 36.9% | **+4,229 mL** | **不稳定** |

- **D_aniso = 3 为最大稳定值**；**D_aniso ≥ 10 时显式扩散方案不稳定**（质量误差高达数千 mL），原因：ADL 层 k = 5e-11 产生 D_cap ≈ 3e-4 m²/s，配合大 D_aniso 后通量过大，**通量限制器（每步 40%）不足以维持稳定性**。
- **通量限制器实现**：逐列计算 D_cap_face、dSw/dx、F_x = −Dc·φ·dSw/dx·A·dt；**每步流出不超过当前 cell 液体量的 40%**；⚠️ **限制器引入的数值耗散意味着实际有效 D_aniso 略低于设定值**。
- **改进方向**：① **隐式/半隐式 ADL 扩散（Crank-Nicolson）** —— 无条件稳定，支持 D_aniso ≥ 10；② **ADL 层间差异化**（当前 4 层同用 k0 = 5e-11，可区分 topsheet / ADL / airlaid）；③ **Core 层层间输运**（当前 Core 间无输运）。

### 8. 修复的三个 Bug Fixed Bugs

| # | 问题 | 后果 | 修复 |
|---|---|---|---|
| **Bug 1** | `__post_init__` 时序：创建 uniform 配置后执行 `cfg.multi_layer.enabled = False`，但 `__post_init__()` 已按默认 enabled=True 生成 ADL 分层参数 | **uniform 基准线实际使用多层参数（ADL 层 M_eq = 0 → SAP 不吸收），MD spread 伪报 36.8%**（实为初始 Sw = 0.02 均匀液体被吸收的比例） | 构造时传入 `MultiLayerConfig(enabled=False)`；修正后 uniform 的 MD spread 回到正确的 **0.9%** |
| **Bug 2** | CFL 语法错误：注释与代码同一行、无换行分隔 | **扩散 CFL 从未执行** → D_aniso ≥ 3 时注入阶段 dt = 0.005 远超扩散 CFL 限值，产生不稳定 | 注释与代码分两行；修复后所有 D_aniso ≤ 3 场景稳定运行 |
| **Bug 3** | ADL x-diff 负体积：D_cap ≈ 3e-4 m²/s（比 Core 大 50×）的无限制显式扩散可使 V_liq 变负 | 负体积 | 添加**保守通量限制器（≤40%/步）**；并把 **ADL x-diff 移至排水步骤之前**（先扩散再排水），使液体有更多时间横向铺展 |

### 9. 质量守恒验证 Mass Conservation

- 三个场景的**质量误差轨迹一致且稳定**：注入阶段（t = 0~13.3 s）误差从 0 缓慢增长至 **+0.06 mL**（数值截断），注入结束后回落到 **−0.014 mL（<0.01%）**，并在剩余 **227 秒保持恒定**。

```
V_error = V_total − V_injected − V_initial
V_total = Σ(V_liq) + Σ(M_abs)/ρ_l
V_initial = Sw0 · φ0 · cell_vol · Nx · Nz = 6.88 mL（多层）/ 5.04 mL（均匀）
```

- 该公式从 **v9 Fix 1 继承**（修正 v8 未扣除初始液体的常数偏移问题）。

| 版本 | 质量误差 |
|---|---|
| **v8** | **~5.0 mL（常数偏移）** |
| **v9 / v10 / v11** | **−0.014 mL** |

**各场景最终质量平衡**

| 场景 | V_liq (mL) | M_abs (mL) | V_total (mL) | 误差 (mL) |
|---|---|---|---|---|
| Uniform | 0.0 | 205.1 | 205.1 | −0.014 |
| ML+Drain | 26.4 | 180.5 | 206.9 | −0.014 |
| ML+Xdiff | 26.4 | 180.5 | 206.9 | −0.014 |

- **Uniform 场景 V_liq = 0.0**：液体被完全吸收（凝胶阻塞在顶层）。
- **ML 场景 V_liq = 26.4 mL**：ADL 层保留的 15% 阈值液体**未被 Core 吸收**（ADL 无 SAP，且 Core 处于凝胶阻塞状态无法继续吸收）。

### 10. 结论、后续计划与局限性

**四条核心结论**：① ADL 排水把 SAP 利用率 **48.1% → 63.6%（+32%）**，液体均匀分布到 8 层 Core（各 ~22.5 mL），**完全避免凝胶阻塞**；② ADL 横向扩散（D_aniso = 3）把 MD spread **0.9% → 34.9%（+38×）**，接近理论极限 36.7%；③ 质量误差全程 <0.015 mL；④ 均匀模型验证了 v10 的基准行为（0.9% MD spread = 凝胶阻塞），**多层模型解决了这一根本性限制**。

**后续计划（源文优先级）**

| 优先级 | 项目 | Phase | 说明 |
|---|---|---|---|
| **P0** | 隐式 ADL 扩散方案 | Phase 3 | Crank-Nicolson，支持 D_aniso ≥ 10 |
| **P0** | 降低活跃细胞阈值 | Phase 3.2 | 当前 0.1 × M_eq = 3.54 g **过高** |
| **P0** | **反渗（rewet）模型** | Phase 4 | 定义 rewet 判据与回流速率 |
| P1 | 注入速率敏感性 | Phase 3.2 | Q_inj 15 → 5 mL/s 敏感性 |
| P1 | ADL 层数敏感性 | Phase 3.2 | 扫 n_adl = [2, 4, 6, 8] |
| P1 | 参数标定（文献） | Phase 5 | ADL / SAP 标准参数提取 |
| P2 | Core 层间输运 | Phase 3.2 | 重力驱动层间排水 + 扩散 |
| P2 | **实验验证** | Phase 6 | **ISO 11948 吸收/反渗测试** |
| P2 | 3D 扩展 | Phase 7 | 增加 y 方向维度 |

**五项局限性（源文自述，照录）**

1. **ADL x-diff 使用显式方案** —— D_aniso ≥ 10 不稳定，需隐式方案；
2. **Core 层间无输运** —— 仅靠 ADL 排水分配，未模拟层间再分配；
3. **无反渗模型** —— 无法模拟二次加载后的液体回流；
4. **无多组分传输** —— 尿素 / NaCl / 表面活性剂对 SAP 的抑制效应未建模；
5. **参数未完成实验标定** —— **Brooks-Corey 参数来自文献而非实验数据**。

### 11. 附录 A：改动文件清单

| 文件 | 改动内容 |
|---|---|
| config.py | MultiLayerConfig 分层参数系统 + `__post_init__` z-profile 数组生成 |
| solver_v11.py | `_step_adl_drainage()` + `_step_adl_x_diffusion()` + 层相关初始化 |
| physics_properties.py | dynamic_phi / carman_kozeny 参数支持 2D 数组广播 |
| pressure_solver.py | inj_layers 多注入层支持（ADL 层等量注入） |
| flory_rehner.py | Flory-Rehner-Donnan 热力学模型（Newton-Raphson 求解） |
| run_multi_layer.py | Uniform vs Multi-Layer 对比运行器 + 结果输出 |
| scan_daniso_ml.py | D_aniso = [1, 3, 10, 30] 灵敏度扫描 + 质量误差检测 |

## 与本项目库的关系 Relations

- **机理页**：`[[Gel Blocking（凝胶阻塞）]]`（本件的量化证据：0.9% MD spread、有效渗透率 ~2e-13 m²、48.1% vs 63.6%）、`[[MD Liquid Distribution]]`（MD spread 与 D_aniso 校准）、`[[ADL（导流层）]]`（ADL 排水的物理角色）、`[[Core Channel Pattern（芯体通道花型设计）]]`、`[[SAP错峰膨胀]]`。
- **参数页**：`[[SAP性能指标（CRC AUL GBP Vortex）]]` —— 本件 **Q_eq = 26.6 g/g（0.9% NaCl）由热力学模型算出**，与该页的实测 CRC 口径**来源不同，不可直接等同**。
- **方法页**：`[[Rewet Test（回渗测试）]]` —— 本件**尚无 rewet 模型**（P0 待办），因此**不能用于回渗预测**。
- **组合页**：`[[IPC BCC OI Portfolio（开放创新项目组合）]]`。

## 🔴 manual_review（2026-09-29）

- **无商务敏感信息**：本件不含价格、报价、供应商条款。
- **数值引用纪律**：全部结果为**模型内部数值**，**参数未实验标定、无实验验证**（实验验证仍在 P2 待办）；**不得作为产品性能数据、不得写入规格或对外材料**。
- **模型演进信息**：v8 → v11 的质量误差沿革与三个 Bug 属**内部开发历史**，引用时须标注版本与时间。
- **作者与工具署名**：文档署名为 WorkBuddy AI Lab（2026-07-08），属来源元信息，本页保留以便追溯。

## 存疑 Open Questions（不裁决）

1. **Q_eq = 26.6 g/g（热力学模型）vs 实测 CRC** —— **来源不同，不换算、不等同**。
2. **MD spread 理论极限 36.7%** 由 `(Nx−inj)/Nx = 21/30` 定义，是**网格离散下的极限**，**不等于物理极限**。
3. **D_aniso ≥ 10 的两个值（40.0% / 36.9%）来自不稳定运行**（质量误差数千 mL），**不可作为有效结果引用**。
4. **"完全避免凝胶阻塞"** 是模型结论；同页 §6 又承认 **Core 层内部凝胶阻塞仍限制深度渗透** —— 两者**作用域不同（多层分配 vs 层内输运）**，照录不裁决。
5. **活跃细胞阈值 0.1 × M_eq = 3.54 g 被判为过高**，但**未给出新值**。
6. **ADL 保留 26.4 mL（12.8%）** 是**阈值设定（S_thresh = 0.15）的直接结果**，非材料属性。

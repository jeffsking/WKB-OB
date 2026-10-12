---
type: source
title: "85 双层pattern芯体套准工程规格"
source_type: 派生工程笔记（补库动作 · Gap G4 + 副交付 G17）
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/85-双层pattern芯体套准工程规格.md.md
original_link: ""
date_published: 2026-09-22
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "Registration is the ONLY quality gate in this architecture whose failure is an ARCHITECTURE failure: channels are not cut, they are BONDED by two drums pressing land-to-land ('raised lands bond channels in register'); misregistration drops channel bond area → channels open when wet → the architecture's core advantages (wet-state openings, gel-blocking resistance) disappear（套准是唯一「失效即架构失效」的质量门：通道是两侧 land 对压粘出来的，不是切出来的）"
  - "Spec: |MD| ≤ 1.0 mm and |CD| ≤ 0.5 mm, both stated to guarantee ≥90% channel bond area; the source gives the endpoint conclusion but NOT the conversion formula（规格：MD ≤1.0 / CD ≤0.5 mm，保证 ≥90% 通道粘接面积；源文件未给换算式）"
  - "⚠️ Reconstructed conversion (this document's own inference): with a linear overlap model, overlap ≈ (feature size − |δ|) / feature size, and allowing 10% area loss gives CD feature (channel width) w ≈ 5.0 mm and MD feature (cross-link length) l ≈ 10.0 mm; this MUST be back-checked against actual sleeve drawings (fishbone rib width / cross-rib length)（重构换算：通道宽 ≈5 mm、MD 向 land 特征长 ≈10 mm；须用 sleeve 图纸反验）"
  - "⚠️ Three easily confused metrics: registration in-spec rate ≥99.99% (drops to 92.7% only when the chute is not re-set for ups); Cpk MD 2.43–2.49 / CD 1.39; and the 92.7% LANDING rate which is caused by chute speed mismatch (see 86), NOT by registration precision — the three must never be interchanged（三项易混指标：套准 in-spec 率、Cpk、落点合格率 92.7%，后者与套准机械精度无关）"
  - "Error budget: σ_pin ±0.02 mm (spec) or ±0.05 mm (post-change practice) — CONFLICTING; σ_pattern ±0.02 mm over 2,771 mm; σ_cam ±0.1 mm deadband; σ_mat, σ_thermal, σ_cd all UNQUANTIFIED（公差链：三项已知、三项未量化）"
  - "⚠️ Sigma back-solved from Cpk (σ = USL / (3·Cpk)): MD 0.137 mm (6-up) / 0.134 mm (7-up); CD 0.120 mm. CD's Cpk is worse PURELY because its USL is half of MD's — CD is the binding constraint of the whole line（由 Cpk 反解隐含 sigma；CD 是整线约束项）"
  - "The back-solved sigma independently reproduces the source's 'in-spec ≥99.99%': CD failure rate = 2[1−Φ(4.167)] ≈ 31 ppm → in-spec ≈ 99.9969%; MD's Cpk 2.43 gives a negligible ~10⁻¹³, so in-spec is 100% determined by CD（反解值与源文件结论自洽，构成独立交叉验证）"
  - "MD residual is NOT camera-limited: σ_cam = 0.1/√3 = 0.058 mm, so σ_other = √(0.137² − 0.058²) = 0.124 mm — about 82% of the MD residual comes from unquantified material/tension/mechanical terms. Upgrading the camera therefore barely helps; σ_mat and σ_thermal must be quantified（MD 残差 82% 来自未量化项，相机升级几乎无益）"
  - "Cpk CD improvement targets: 1.39 → 1.67 requires σ 0.120 → 0.100 mm (−17%); → 2.00 requires 0.083 mm (−31%) — the hardest mechanical precision requirement in this architecture（Cpk 改善目标：CD 机械链合成误差须降 17–31%）"
  - "MD self-corrects in ~17 products (~1 s) because MD error is a single PHASE SCALAR correctable by servo on the poly drum; CD MUST be pinned because CD error is an axial GEOMETRIC quantity with no servo degree of freedom, no axial correction axis, and no vision coverage（MD 可自纠 ≈17 片；CD 必须机械钉死）"
  - "Why trim must act on the POLY side only: if both sides were corrected, one observable (relative MD error) would map to two degrees of freedom and the solution would not be unique; fixing skin as the datum reduces 2 DOF to 1（只在 poly 侧 trim：可辨识性要求）"
  - "Vision loop spec (G17): UV camera MA-10, deadband ±0.1 mm, trims the poly drum phase only, converges in ~17 products, correction summed into the poly drum torque motor (1/n rev per product + trim); UV tracer is added to the SKIN-side glue only（视觉闭环规格：UV 相机 MA-10、死区 ±0.1 mm、仅修 poly 侧、≈17 片收敛）"
  - "Grade-change waste conversion: 17 products/change; SAP loss ≈0.21–0.39 kg/change (12.6–18.2 g dual-side SAP @Open M, 16.2–23.2 g @Pant XXXXL); wrap loss ≈0.25 g/change (negligible); time ≈1 s. Lever = reduce the 17-product convergence, not save wrap. ⚠️ TOTAL changeover waste cannot be closed because Step 4 verification scrap is not given（换型废片换算：损失几乎全是 SAP；⚠️ 总废片不可闭合）"
  - "⚠️ 15–20 pieces ≠ 17 pieces: the 15–20 figure is splice/single-layer registration waste from the existing Open Diaper Process document; the 17 figure is post-changeover phase-loop convergence. They are coincidentally similar in magnitude but differ in cause, system and remedy — never cross-quote（15–20 片 vs 17 片：成因完全不同，禁止混引）"
  - "Acceptance: online 100% registration in-spec + SAP edge sharpness; first-piece channel overlay + wet bond check; Cpk MD/CD with n ≥ 125 (this document's recommendation); wet channel bond ≥1.5 N/25 mm after 2 saturations — marked '(validate)' by the source, test method NOT defined; offline SAM distribution per STM-00305 / STM-4597（验收五条；⚠️ 湿态粘接判据尚未建立）"
pages_linked: ["[[IPC BCC OI Portfolio（开放创新项目组合）]]", "[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]", "[[One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）]]", "[[84 Sleeve 工程规格与换装防错设计]]", "[[SAP Dosing Speed Matching & Tolerance Spec（SAP 落料速度匹配与容差规范）]]", "[[Core Channel Pattern（芯体通道花型设计）]]", "[[Nichidai（日丝）]]", "[[汉高]]"]
---

# 85 双层pattern芯体套准工程规格

> 一句话定位：一份 **双层 pattern 芯体套准的公差链与 Cpk 体系补库笔记**——回答三个问题：**为什么套准是本架构唯一"失效即架构失效"的质量门**、**1.0 / 0.5 mm 这两个公差是怎么来的**、以及**为什么 MD 能自纠而 CD 必须一次做对**。（中文：它把"套准"从一句口号，翻译成**可分配的误差预算与可写进设备协议的 Cpk 目标**。）

> ⚠️ **来源性质（2026-09-29）**：本件为**派生工程笔记**（自述由"纸尿裤全栈设计专家（CoreCraft）"生成，2026-09-22）。**套准规格与 Cpk 均为源文件的一阶模型/仿真值（B 级）**，源文件 notes 明确 *error sigmas 是待中试台校准的估计值*；且**本件多处结论自标为"本次推断"**。credibility 定为**中**。

## 原文要点 Original Key Points

### 1. 文件定位与来源 Provenance

| 项 | 内容 |
|---|---|
| 补库来源 | **One_Drum_Two_Ups_11_Sizes_1000ppm.pptx P3 / P4 / P7 / P9 / P12 / P14 / P15 / P17 / P18** |
| 对应 Gap | **G4**（双层 pattern 套准公差链与 Cpk 体系缺失，主表标为**最高优先级**）｜严重程度 高｜属 **P1 批次** |
| 副交付 | **G17**（视觉闭环「相位微调」的控制规格） |
| 主表改善建议 | ① MD/CD 套准公差与通道粘接面积的换算（≥90% 的依据）② 公差链拆解 ③ Cpk 目标与样本量 ④ MD 可自纠 / CD 需机械钉死的机理解释 ⑤ 视觉闭环相位控制规格 |
| 创建日期 | **2026-09-22** |

### 2. 为什么套准是质量门 Why Registration Is the Gate

```
skin 侧鼓 → 沉积 skin SAP pattern ─┐
                                    ├─ 双鼓对压（land-to-land）→ 通道粘接
poly 侧鼓 → 沉积 poly SAP pattern ─┘
```

- 芯体的「**通道**」**不是切出来的，而是两侧 land 对压粘出来的**（源文件 P7：*"raised lands bond channels in register"*）。
- **失效链**：两层 pattern 错位 → **land 与 land 不再正对** → **通道粘接面积下降** → **通道在润湿后开胶** → **通道丧失导流功能** → **本架构相对传统芯体的核心优势（湿态开孔、防凝胶阻塞）消失**。
- **推论（源文）**：套准是本架构中**唯一一个「失效即架构失效」的质量门**。

### 3. 规格定义 Specification

#### 3.1 公差规格

| 方向 | 规格 | 目的 | 出处 / 等级 |
|---|---|---|---|
| **MD**（机器方向，沿鼓面周向） | **\|MD\| ≤ 1.0 mm** | 保证 **≥90% 通道粘接面积** | 源文件 P14；**B** |
| **CD**（横向，沿鼓轴） | **\|CD\| ≤ 0.5 mm** | 同上 | 源文件 P14；**B** |

#### 3.2 ⚠️「≥90% 通道粘接面积」的换算（源文件未给，本次重构）

**模型（线性重叠）**：设 land 特征尺寸（CD 方向 = 通道宽 **w**；MD 方向 = 横向连接段长 **l**），偏移为 δ：

> 重叠率 ≈ (特征尺寸 − \|δ\|) / 特征尺寸 …(1)

令重叠率 = 0.90（容许 **10% 面积损失**），反解特征尺寸：

| 方向 | 公差 | 反解特征尺寸 | 量级 |
|---|---|---|---|
| CD | 0.5 mm | **w = 0.5 / 0.10 = 5.0 mm** | **通道宽量级 ≈ 5 mm** |
| MD | 1.0 mm | **l = 1.0 / 0.10 = 10.0 mm** | **MD 向 land 特征长量级 ≈ 10 mm** |

> ⚠️ **等级与用法**：本重构为**推断**，依据是式(1) 与「10% 面积损失」这一**隐含判据**。必须用 **sleeve 图纸的实际几何**（通道宽、横向连接段长、fishbone 骨架尺寸）**反验**：
> - 若实际 land 特征尺寸与 **5 mm / 10 mm 同量级** → 公差与 90% 判据**自洽**，可继续使用；
> - 若**显著不同** → **0.5 / 1.0 mm 公差必须重新推导，不得直接引用**。
>
> 源文件 P1 提到 sleeve 为 **fishbone（鱼骨形）图案**，其「**骨宽 / 横肋长**」正是式(1) 所需的特征尺寸 —— 这是向 sleeve 供应商索取图纸时的**新增必填项**。

#### 3.3 ⚠️ 三项易混指标（防误引）

| 指标 | 值 | 含义 | 误差来源 |
|---|---|---|---|
| **套准 in-spec 率** | **≥99.99%**（两 ups；chute 未随 ups 重设时 **92.7%**） | 套准偏差落入 \|MD\|≤1.0 / \|CD\|≤0.5 的**片数占比** | 套准偏差（机械 + 控制） |
| **Cpk** | **MD 2.43–2.49 / CD 1.39** | 套准分布的**过程能力指数** | 同上 |
| **落点合格率 92.7%** | 92.7%（**仅当 chute 未随 ups 重设**） | **SAP 落点**落入 pattern 的合格占比 | **chute 线速失配（见 86）**，**不是机械套准问题** |

> **关键区分**：**92.7% 的成因是 SAP 落料速度失配，与套准机械精度无关**。**不得把 92.7% 归因于套准精度不足。**

### 4. 公差链拆解 Tolerance Chain

#### 4.1 误差源清单

| 符号 | 误差源 | 值 | 状态 |
|---|---|---|---|
| **σ_pin** | Sleeve 承载体定位（pin + 锥面） | **±0.02 mm**（P8 规格值）**或 ±0.05 mm**（P18 换型实操值） | ⚠️ **口径冲突**，见 84 §5.1 |
| **σ_pattern** | Sleeve pattern 加工（n 个节距等距性） | **±0.02 mm over 2,771 mm** | 已知（B） |
| **σ_cam** | 视觉测量 / 闭环死区 | **±0.1 mm** | 已知（B） |
| **σ_mat** | 包覆材料 pitch 波动 / 张力波动 | 未量化 | ❌ 缺（主表 G12） |
| **σ_thermal** | 热漂移（鼓温升、胶温、材料热收缩） | 未量化（但包覆 140 ℃ 热收缩 ≤1%，见 86） | ❌ 缺 |
| **σ_cd** | CD 侧：鼓体对中 + sleeve 横向加工 + 装配 | 未量化 | ❌ 缺 |

#### 4.2 ⚠️ 由 Cpk 反解隐含 sigma（本次独立推导）

> 源文件未给误差 sigma（其 notes 明确说 *"error sigmas are estimates to calibrate on a pilot rig"*）。由 **Cpk = USL / (3σ)**（分布近似居中）反解 **σ = USL / (3 × Cpk)** …(2)

| 方向 | ups | USL | Cpk | **σ_implied** |
|---|---|---|---|---|
| MD | 6-up | 1.0 mm | 2.43 | **0.137 mm** |
| MD | 7-up | 1.0 mm | 2.49 | **0.134 mm** |
| CD | 6-up / 7-up | 0.5 mm | 1.39 | **0.120 mm** |

**三条推导结论**

1. **MD 与 CD 的 sigma 同量级**（0.134 vs 0.120 mm），但 **CD 的 Cpk 差得多**（1.39 vs 2.43）——**纯粹因为 CD 的 USL 只有 MD 的一半**（0.5 vs 1.0 mm）。**CD 是整线的约束项。**
2. **Cpk CD 1.39 独立解释了源文件的「in-spec ≥99.99%」**：
   - 失效率 = 2[1 − Φ(USL/σ)] = 2[1 − Φ(0.5/0.120)] = 2[1 − Φ(4.167)] ≈ **3.1 × 10⁻⁵ = 31 ppm**
   - → **in-spec ≈ 99.9969% ≥ 99.99% ✓**
   - **MD 侧 Cpk 2.43 → 失效率 ~10⁻¹³，可忽略**。故 **in-spec 率 100% 由 CD 决定**。✅ **该反解与源文件结论自洽，构成对源文件数值的独立交叉验证**。
3. **MD 侧的误差主要不来自相机死区**：
   - σ_cam（±0.1 mm 均匀分布）= 0.1/√3 = **0.058 mm**
   - σ_other = √(0.137² − 0.058²) = **0.124 mm** ← **远大于相机项**
   - → **MD 残差的 82% 来自未量化的材料/张力/机械项**，**相机死区不是瓶颈**。→ **把相机升级为更高分辨率对套准几乎没有帮助**；要改善 MD 必须去量化 **σ_mat / σ_thermal**。

> ⚠️ **等级**：§4.2 全部为**本次推导**（基于式(2) 与源文件 Cpk 值），**未实测**。其价值在于给出「**哪些误差源值得量化**」的**排序**，**不是替代实测**。

#### 4.3 提高 Cpk CD 的量化目标（可写进设备协议）

| Cpk 目标 | 所需 σ | 降幅 |
|---|---|---|
| **1.39（当前）** | 0.120 mm | — |
| **1.67** | 0.100 mm | **−17%** |
| **2.00** | 0.083 mm | **−31%** |

> 通用验收口径常取 **Cpk ≥ 1.67**；若项目要求 **Cpk ≥ 2.0**，则 **CD 机械链的合成误差须从 0.120 降到 0.083 mm（−31%）**。这是**本架构最硬的一条机械精度要求**，应作为**鼓体 / 承载体 / sleeve 的公差分配起点**。

### 5. Cpk 体系与样本量 Sampling

| 项 | 值 | 状态 |
|---|---|---|
| 仿真样本量 | **200,000 片/工况** | 源文件 P14；**B** |
| 工况数 | **2（6-up、7-up）** | 源文件 P14 |
| 报告指标 | **Cpk MD、Cpk CD、in-spec 率** | 源文件 P14 |
| **实测建议样本量** | 源文件未给出 → **建议 n ≥ 125** | ❌ 缺 → **本次建议（推断）** |

- ⚠️ **实测样本量的空白**：源文件的 **20 万片是仿真样本量**，**实线验收所需的实测样本量未定义**。Cpk 的置信区间依赖样本量：
  - 常规做法：**n ≥ 100** 用于短期 Cpk（Cp/Cpk 的 90% 置信下限在 n=100 时约为点估计的 **0.75 倍**）；
  - 若要在 **Cpk 1.39 附近做判定**，建议 **n ≥ 125**（使点估计与置信下限差 **<0.25**）；
  - **换型后首件验证只能用极小样本**（首件 + 收敛后数片），**不能据此计算 Cpk** —— 只能做「通道叠合目视 + 湿态粘接」的**属性判定**。
- **要求**：在验收 KPI 集（80 §6）中把样本量补为「**n ≥ 125，连续取样，覆盖两 ups 与至少 3 个尺寸**」。

### 6. MD 可自纠 / CD 必须钉死——机理

#### 6.1 现象（源文件 P14）

| 方向 | 表述 |
|---|---|
| **MD** | **"MD self-corrects in ~17 products (1 s)"** —— 可在约 **17 片**内自动收敛 |
| **CD** | **"CD must be pinned"** —— 必须在机械上钉死，**无自纠** |

#### 6.2 机理解释（源文件未展开，本次推导）

**为什么 MD 可自纠**

- MD 偏差是「**一个相位标量**」：鼓面圆周方向上，pattern 相对对侧 pattern 的 MD 偏差**对所有 n 个 pattern 是同一个相位偏置**（前提：**节距等距**，见 84 §5.2）→ **只需修正一个标量即可对齐全部 n 个 pattern**。
- **该标量可由伺服直接修正**：相位偏置可叠加在鼓轴传动上（源文件 P12：*"Poly drum torque motor — 1/n rev per product + trim"*）→ **纯软件修正，无需动硬件**。
- **存在可观测的基准**：**UV 相机可读 skin 侧**（其胶含 **UV 示踪剂**，源文件 P17）→ 以 skin 侧为基准测 MD 偏差 → **闭环修正 poly 侧**。

**为什么 CD 不能自纠**

- CD 偏差是「**一个轴向几何量**」：修正它需要改变 **sleeve 相对鼓面的轴向坐标**或 **pattern 的横向坐标** —— 两者都是**硬件属性，不是设定值**。
- **不存在可伺服修正的自由度**：鼓沿轴线的位置由**承载体锥面/端面机械定位**，**没有轴向伺服轴**（源文件 P12 的轴清单中无轴向修正轴）。
- **视觉也不覆盖**：相机**只测 MD 相位**（P12：*"phase trim → poly drum only"*）→ **CD 是开环量**。
- 因此 CD **只能靠三段机械链一次做对**：**鼓体对中**（P8：100/110/120 共用同一轴向设定）→ **承载体定位** → **sleeve 横向加工精度**。

> **工程结论**：**CD 公差链是「一次做对、事后不可补救」的链路**，因此必须 **(a)** 作为 sleeve 与鼓体的**到货验收项**（84 §9.1 A1/A2）；**(b)** 在设计阶段**预留收紧**（§4.3 的 −17%~−31% 目标）；**(c)** **视觉系统只做 MD 闭环**，不要把 CD 的期望寄托在视觉升级上。

#### 6.3 附带推论：为何必须「只在 poly 侧 trim」

- 若**两侧都做相位修正**，则**一个观测量**（相机测得的相对 MD 偏差）对应**两个自由度**（两侧相位）→ **解不唯一**（可整体平移，无法收敛）。
- **固定 skin 侧为基准、只动 poly 侧**，是**把 2 个自由度降为 1 个的必要手段**——这也是源文件 P12 只保留一条 *phase trim → poly drum only* 通路的原因。
- **等级**：**推断**（基于控制可辨识性），但**结论与源文件设计一致**。

### 7. 视觉闭环相位控制规格（副交付 G17）

#### 7.1 规格

| 项 | 值 | 出处 / 等级 |
|---|---|---|
| 相机 | **UV 相机，型号 MA-10** | 源文件 P12/P14；**B** |
| 死区（deadband） | **±0.1 mm** | 源文件 P12/P18；**B** |
| 修正对象 | **仅 poly 侧鼓相位**（skin 侧为基准） | 源文件 P12/P14；**B** |
| 收敛速度 | **约 17 片**内（1,000 ppm 下 ≈ **1 s** 生产时间） | 源文件 P12/P14/P18；**B** |
| 修正量叠加位置 | **Poly 鼓力矩电机传动**（1/n rev per product + trim） | 源文件 P12；**B** |
| UV 示踪剂 | **仅加在 skin 侧胶中** | 源文件 P17；**B** |
| 控制环带宽 / 响应时间 | **未给出** | ❌ 缺 |
| 首件后是否需人工确认 | Step 4「Verify」要求**首件通道叠合 + 湿态粘接** | 源文件 P18；**B** |

#### 7.2 控制环结构（据源文件信息重构）

```
┌──────────────── 虚拟主轴 1,000 产品/min ────────────────┐
│  EtherCAT 250 µs · DC 同步                              │
└───────┬──────────────────────────────┬──────────────────┘
        │ 1/n rev/product              │ 1/n rev/product + TRIM
        ▼                              ▼
┌──────────────┐               ┌──────────────┐
│  Skin 鼓轴    │═══ 对压 ═══▶  │  Poly 鼓轴    │
│ （基准，不动）│   land-land   │（被修正轴）   │
└──────────────┘               └────▲───────┘
        │                             │
        │ skin 侧胶含 UV 示踪剂        │ 相位偏置修正
        ▼                             │
┌──────────────┐   MD 偏差 e         │
│ UV 相机 MA-10├──────────────▶ ┌────┴─────┐
│  死区 ±0.1 mm │                │ 套准控制器│
└──────────────┘                └──────────┘
                      │e| > 0.1 mm 才动作（死区）
```

**控制律（据规格反推）**：`if |e| > deadband(0.1 mm): 修正 poly 鼓相位偏置，使 e → 0；else: 保持（死区内不动作，避免追噪声）`

**⚠️ 未给出的控制参数（须向供应商索取或自行整定）**

- **死区内的稳态残差**：死区 ±0.1 mm 意味着理论残差可达 ±0.1 mm，但 §4.2 反解的 **σ_MD = 0.137 mm > 0.058 mm（死区等效 σ）** → 说明**实际稳态由过程噪声支配，而非死区**。→ **死区可适度放大（如 ±0.15 mm）而不显著恶化 Cpk**，反而可减少执行机构动作频次（降低磨损）。（**推断**）
- **修正增益 / 积分时间 / 是否逐片修正还是每 k 片修正**：未给出。
- **相机视野覆盖几个 pattern**：未给出（影响 n 个 pattern 的平均 vs 单片测量）。
- **是否只在特定相位窗口采样**（高速下曝光时间约束）：未给出。
- **UV 示踪剂在 140–150 ℃ 施胶温度下的稳定性**：未给出（源文件 P17 规定施胶 ≤150 ℃）。

#### 7.3 换型废片换算

| 项 | 值 | 依据 |
|---|---|---|
| MD 收敛废片 | **17 片/次换型** | 源文件 P12/P14/P18；B |
| 折算材料损失（SAP） | **≈ 0.21 – 0.39 kg SAP/次** | 17 片 × 单片双侧 SAP（**12.6–18.2 g @Open M** / **16.2–23.2 g @Pant XXXXL**） |
| 折算材料损失（包覆） | **≈ 0.25 g/次**（可忽略） | 17 × [2 侧 × 0.396 m × 0.11 m × 10 g/m²] ≈ 0.25 g |
| 折算时间损失 | **≈ 1 s 生产时间**（但含启停与验证则不止） | 17 片 / 1,000 ppm |

> **换算结论**：**换型损失几乎全部是 SAP，包覆与时间可忽略**。因此**降低换型损失的杠杆是减少收敛片数（17 → 更少），而不是省包覆**。
> ⚠️ **提示**：还有 **Step 4（首件通道叠合 + 湿态粘接验证）所需的额外废片**，源文件未给出片数 → **「换型总废片」目前无法闭合**（与 83 §6「<30 min 时间账不闭合」是同一缺口 G3）。**禁止把 17 片当作换型总废片引用。**

### 8. 与既有 WKB 知识的差异（防误引）

| 既有资料 | 内容 | 与本件关系 |
|---|---|---|
| **Open Diaper Process Introduction--202104.pdf** · 底膜图形注册 | 单层图形注册：Checker vs Vision；拼接后 **15–20 片排废**；基准是「印刷标记 ↔ 刀口」；单层 | **✗ 不可替代** |
| 同上 · Vision system | 检测/剔除：I1/I2/FOD/K1–K5 检测项；目的**判废**而非闭环控制相位 | **✗ 不可替代** |
| **Patterned SAP core 6.pptx** | 把 "Registration limitation" 列为 watchout（**无量化**） | **○ 补充其量化** |
| **V6 产品设计与工艺优化**（录音） | 提出「上下层 SAP 需要对齐」的需求 | **○ 需求来源** |
| **STM-00305 / STM-4597** | SAM 分布/对位的实测方法 | **○ 用于实测验证** |
| **本件** | **上下双层 SAP pattern 互相套准 + 闭环相位控制**（双基准、双鼓、闭环） | — |

#### 8.1 ⚠️ 15–20 片 vs 17 片：数值接近，成因完全不同

| 数值 | 场景 | 出处 |
|---|---|---|
| **15–20 片排废** | **印刷/图案拼接**（单层注册，材料接驳处） | Open Diaper Process Introduction--202104.pdf |
| **17 片** | **换型后相位闭环收敛** | 源文件 P12/P14/P18 |

> **这两个数必须严格区分。二者量级接近纯属巧合**，**成因、归属系统、改善手段完全不同**（前者靠减少拼接次数，后者靠提高闭环收敛速度）。**禁止混引或互相"印证"。**

### 9. 验收方法 Acceptance

| 层级 | 方法 | 状态 |
|---|---|---|
| **在线（100% 检测）** | 视觉套准 in-spec 率 + **SAP 边缘锐度（图像分析）** | 源文件 P5/P16 提到边缘锐度 KPI，但**分析方法未定义**（G20 的 K7） |
| **换型首件（属性判定）** | 首件**通道叠合（overlay）** + **湿态粘接验证** | 源文件 P18；**方法细节缺** |
| **过程能力（统计判定）** | **Cpk MD/CD，n ≥ 125**（建议，见 §5） | 源文件只给仿真 20 万片 |
| **湿态通道粘接（功能验证）** | **≥1.5 N/25 mm，2 次饱和后** | 源文件 P17；**测试方法未定义**（G11） |
| **SAP 分布/对位（离线）** | **STM-00305 / STM-4597** | WKB 已有方法 ✓ |

> **两点必须注意**（源文原文）：
> 1. 「**湿态通道粘接 ≥1.5 N/25 mm @2 次饱和后**」是**通道功能是否真正成立的最终判据**，**其重要性高于套准尺寸**。源文件自己标注为 **"(validate)"** —— 即**尚未验证**。该测试方法（**试样制备、饱和液、加载速率、剥离角度**）**必须先定义**。
> 2. **套准尺寸合格（in-spec ≥99.99%）不等于通道粘接合格**。前者是**几何条件**，后者是**功能结果**，中间还隔着**胶的开放时间与压合压力**（见 G11，**未闭环**）。

### 10. 待验证与外部输入 Open Items

| # | 事项 | 归口 | 优先级 |
|---|---|---|---|
| 1 | 索取 **sleeve 图纸的 land 特征尺寸**（fishbone 骨宽 / 横肋长）→ 反验 §3.2 的 5 mm / 10 mm 推断 | sleeve 供应商 / Nichidai | **最高** |
| 2 | 澄清**相位精度口径 ±0.02 vs ±0.05 mm** | 设备商 | **最高**（§4.1 公差链基础） |
| 3 | **定义湿态通道粘接测试方法**（≥1.5 N/25 mm @2 次饱和后） | KC 测试 / Adhesive 体系 | **最高**（功能判据） |
| 4 | 量化 **σ_mat**（包覆 pitch 波动/张力）与 **σ_thermal**（热漂移） | KC 实验室 / 供应商 TDS | 高（§4.2 指出这是 MD 残差主项） |
| 5 | 量化 **σ_cd**（鼓体对中 + 承载体 + sleeve 横向）→ 支撑 §4.3 的 Cpk 2.0 目标 | 设备商 | 高 |
| 6 | 索取**视觉闭环控制参数**（增益/积分/采样窗口/视野覆盖 pattern 数） | 相机供应商（MA-10） | 中 |
| 7 | 确认 **UV 示踪剂在 140–150 ℃ 的稳定性**与其对胶性能的影响 | 胶供应商 | 中 |
| 8 | 索取视觉系统的**既有实绩**（同速同场景 Cpk 实绩） | 相机供应商 | 中 |
| 9 | 确认**换型总废片数**（含 Step 4 验证废片） | KC 现场 | 中（G3 缺口） |

### 11. 依据与红线 Basis & Red Lines

**依据**：One_Drum_Two_Ups_11_Sizes_1000ppm.pptx P3/P4/P7/P9/P12/P14/P15/P17/P18 + notes；WKB〔Open Diaper Process Introduction--202104.pdf〕（底膜注册/视觉检测项）、〔Patterned SAP core 6.pptx〕（Registration limitation watchout）、〔V6 产品设计与工艺优化〕（上下层对齐需求）、STM-00305、STM-4597、〔Adhesive Product & Process - 201.pptx〕；本地 references/80、83、84、86。

**红线（源文六条，照录）**：
1. **套准规格（\|MD\| ≤ 1.0 / \|CD\| ≤ 0.5 mm）与 Cpk 值均为源文件的一阶模型/仿真值（B 级），非实测**。源文件 notes 明确：*error sigmas 是待中试台校准的估计值*。**引用须携带该标注。**
2. §3.2 的 **5 mm / 10 mm 特征尺寸**、§4.2 的**反解 sigma**、§4.3 的**改善目标**、§5 的**样本量建议**、§6.2/§6.3 的**机理解释**、§7.2 的**死区放宽建议** —— **全部为本次推断**，依据已给出，**未实测、未与供应商确认**。
3. §3.3 的**指标区分**（in-spec 率 / Cpk / 落点合格率 92.7%）与 §8.1 的「**15–20 片 ≠ 17 片**」**必须严格遵守，禁止混引**。
4. **禁止声称「湿态通道粘接 ≥1.5 N/25 mm 已建立验收」** —— 源文件自己标注为 **(validate)**，**测试方法尚未定义**。
5. 「**换型总废片**」**不可闭合**（Step 4 片数缺失），**禁止把 17 片当作换型总废片**。
6. **结论不外推到其它 sleeve 图案 / 其它胶体系**；外推须显式标注「推断」。

## 与本项目库的关系 Relations

- **母方案**：`[[One Drum Two Ups 11 Sizes 1000 ppm（单鼓双ups 11码 1000ppm 芯体印花方案）]]`（P3/P4/P7/P9/P12/P14/P15/P17/P18）。
- **概念页**：`[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]` —— 本件的公差链、Cpk 体系与 MD/CD 机理是该页"套准"要点的规格化。
- **姊妹规范**：`[[84 Sleeve 工程规格与换装防错设计]]`（σ_pin / σ_pattern 的口径来源）、`[[SAP Dosing Speed Matching & Tolerance Spec（SAP 落料速度匹配与容差规范）]]`（92.7% 的真正成因）。
- **相关页**：`[[Core Channel Pattern（芯体通道花型设计）]]`（通道的功能含义）、`[[Nichidai（日丝）]]`、`[[汉高]]`（胶/UV 示踪剂）。

## 🔴 manual_review（2026-09-29）

- **供应商与型号**：源文点名 **UV 相机 MA-10** 与**胶供应商**（UV 示踪剂稳定性）。本页**只记规格与待确认事项，不落价格、报价与商务条款**。
- **设备协议数值**：§4.3 的 **Cpk 目标（1.67 / 2.00）与 σ 降幅（−17% / −31%）**为**本次推断**，**写入设备协议前须经设备商确认**。
- **等级纪律**：套准规格与 Cpk 均为 **B 级仿真值**，**不得作为验收合同值**。
- **未闭环项**：换型总废片、湿态粘接测试方法、边缘锐度分析方法**均不可闭合**，禁止按已定方案引用。

## 存疑 Open Questions（不裁决）

1. **\|MD\| 1.0 / \|CD\| 0.5 mm ↔ ≥90% 粘接面积** —— 源文件只给端点结论，**换算式为本件重构**（w≈5 mm / l≈10 mm），**须用图纸反验**。
2. **σ_pin ±0.02 vs ±0.05 mm** —— 口径冲突，**公差链基础未定**。
3. **92.7%（落点）vs ≥99.99%（套准）** —— **成因不同，禁止互引**。
4. **15–20 片（拼接）vs 17 片（收敛）** —— **成因不同，禁止互引**。
5. **湿态粘接 ≥1.5 N/25 mm** —— 源文件自标 **(validate)**，方法未定义。
6. **MD 残差 82% 来自未量化项** —— 为反解推论，**须实测 σ_mat / σ_thermal 才能确认**。

---
type: source
title: "Origin of Rubber Elasticity"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Origin of Rubber Elasticity/chapters/Origin of Rubber Elasticity_report.md.md
date_published: 2021
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Rubber elasticity is entropic: 'This decrease in entropy gives rise to the elastic force in the network chains' — f = (∂H/∂l)_{T,P} − T(∂S/∂l)_{T,P} (Eq. 6), with the entropic term dominating."
  - "'The shift from negative slope at low degree of elongation to the positive slope at a higher extension ratio is called the thermoelastic inversion. The thermoelastic inversion value may lies around 10% for rubbery materials.' — general to all rubbery materials, not just NR."
  - "Modulus is proportional to crosslink density: N_o = d/M_c (Eq. 12) and G_0 = (dRT/M_c)·(⟨r²⟩₀/⟨r²⟩_f)·(1 − 2M_c/M) (Eq. 17), with an entanglement factor (1+a) added in Eq. 18."
  - "Filler reinforcement follows Guth-Smallwood: E_f/E_0 = 1 + 2.5φ_f + 14.1φ_f² (Eq. 19); 'Filler is an indispensable ingredient in the rubber industry.'"
  - "Mullins effect: 'the stress-strain curve depends on the maximum loading previously encountered'; Bueche's mechanism is that prestrained chains detach or break and stop sharing the load — the key fatigue mode for repeatedly stretched waistbands."
  - "Stress-induced crystallization: crystallites act as crosslinks with modulus ~10¹¹ Pa versus ~10⁶ Pa for the rubbery matrix — five orders of magnitude higher; NR shows a steep stress rise beyond λ > 0.3."
  - "Time-temperature superposition: E(t₁,T₁) = E(t₁/a_T,T₂) (Eq. 21), log a_T = log(t₁/t₂) (Eq. 22); BPA-PC (Mw = 40,000 g/mol) master curve at reference temperature 141°C."
summary_cn: "IntechOpen《Elasticity of Materials》章节拆解（Pal, Das, Naskar, IIT Kharagpur, 2021）：橡胶弹性本质是熵弹性，热弹倒转约 10% 伸长比；模量由交联密度（G₀ = dRT/M_c）与填料（Guth-Smallwood）决定，Mullins 效应是腰围/防侧漏条反复拉伸的疲劳失效主因，TTS 主曲线可用于穿着寿命加速评估。"
tags: ["source/book", "rubber-elasticity", "entropic-elasticity", "crosslink-density", "Guth-Smallwood", "Mullins-effect", "strain-induced-crystallization", "TTS", "viscoelasticity"]
tags_zh: ["橡胶弹性", "熵弹性", "交联密度", "填料增强", "Mullins效应", "应力诱导结晶", "时间-温度叠加", "粘弹性"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Spandex Elastomer Brand Comparison & DMAC Safety Assessment（氨纶弹性体品牌对比及 DMAC 安全评估 2026-07-28）]]", "[[STM-00070 Elastic Tension - BCC Products（皮筋张力测试 第4版）]]", "[[BCC Pants Waist Break Study（Pants 产品拉断研究与两项新方法创建）]]", "[[Pin-Hole Module, Targeted Fluff Distribution & Elastic Recovery Process Review（新材料开发与弹性恢复工艺探讨）]]", "[[Viscoelastic Properties of Amorphous Polymers]]"]
---

# Origin of Rubber Elasticity 橡胶弹性的起源

> Source: chapter "Origin of Rubber Elasticity" from *Elasticity of Materials* (IntechOpen series); authors Sanjay Pal, Mithun Das, Kinsuk Naskar (Rubber Technology Centre, IIT Kharagpur, India); DOI http://dx.doi.org/10.5772/intechopen.100205; © 2021 IntechOpen, CC BY License; ~13 pages, 26K characters; structure = Introduction / Main Body / Conclusions. Compiled from `Origin of Rubber Elasticity_report.md.md`.
> Method skeleton 方法论骨架：thermodynamics（宏观，与分子结构弱相关）+ statistical mechanics（Flory–Rehner 网络理论，微观定量）+ phenomenological equations（Guth–Smallwood、TTS）。

## Chapter structure 章节结构映射

| # | Section 小节 | Content 内容 | Page 页码 |
| --- | --- | --- | --- |
| 1 | Introduction | 问题提出；与晶体/金属/玻璃对比 | P1 |
| 2.1 | Effect of temperature 温度效应 | 热力学推导 Eq. 1–11；thermoelastic inversion | P1–P5 |
| 2.2 | Effect of crosslinking 交联效应 | 交联密度、M_c、纠缠、缺陷 Eq. 12–18 | P5–P7 |
| 2.3 | Effect of filler 填料效应 | Guth–Smallwood、Mullins 效应、Bueche 分子机制 Eq. 19 | P7–P8 |
| 2.4 | Stress-induced crystallization 应力诱导结晶 | 取向→结晶→物理交联→模量突变 | P8–P9 |
| 2.5 | Time-temperature superposition 时间-温度叠加 | 粘弹性三特征、TTS 主曲线 Eq. 20–22 | P9–P10 |
| 3 | Conclusions | 5 大因素（温度/交联/填料/结晶/时间）总结 | P10–P11 |

## Entropic elasticity 熵弹性（2.1, Eq. 1–11）

Definition 定义性表述 (P3–P4)：
> "dW = PdV − fdl (Eq. 1)"
> "dH = TdS + fdl (Eq. 5)"
> "f = (∂H/∂l)_{T,P} − T(∂S/∂l)_{T,P} (Eq. 6)"
> "This decrease in entropy gives rise to the elastic force in the network chains"

Physical picture 物理图像：未拉伸时高分子链为高熵无规线团；拉伸时链被强制线性取向，构象数下降、熵降低，由此产生回复力。与金属/晶体的**能量弹性**（ΔU 主导）相对。

Limit of the equation 方程的极限 (P5)：
> "At sufficiently high elongation, most rubber crystalizes and thus (∂H/∂l)_{T,P} factor may overweight −T(∂S/∂l)_{T,P}."

Thermoelastic inversion 热弹倒转 (P2)：
> "The shift from negative slope at low degree of elongation to the positive slope at a higher extension ratio is called the thermoelastic inversion."
> "The thermoelastic inversion value may lies around 10% for rubbery materials." — "not confined to natural rubber, but it is general for all rubbery materials."

Natural-rubber experimental sample 天然橡胶实验样本：NBS pale creep rubber, 1.5 phr dicumyl peroxide, cured 145°C / 40 min.

## Crosslink density 交联密度（2.2, Eq. 12–18）

> "rubber elastic modulus under a uniaxial elongation is directly proportional to the number of crosslinks per unit volume (N_o)"
> "N_o = d/M_c (Eq. 12)"
> "G_o = (dRT/M_c)(⟨r²⟩₀/⟨r²⟩_f)(1 − 2M_c/M) (Eq. 17)"

| Variable 变量 | Meaning 含义 |
| --- | --- |
| M_c | 网络链平均分子量 average molecular weight of network chains |
| M | 聚合物原始分子量 original polymer molecular weight |
| d | 橡胶密度 rubber density |
| (1 − 2M_c/M) | 末端链缺陷修正 dangling-chain correction（末端链不参与弹性） |
| (1 + a) | 纠缠因子 entanglement factor（Eq. 18） |

> "the contribution of such entanglements to elastic stress cannot be overlooked"

Engineering reading 工程含义：交联密度越高 → M_c 越小 → G_0 越大 → 硬度越高、回弹越快。M_c 是配方工程师的"旋钮"。

## Filler reinforcement 填料增强（2.3, Eq. 19）

> "Filler is an indispensable ingredient in the rubber industry."
> "E_f/E_o = 1 + 2.5·φ_f + 14.1·φ_f² (Eq. 19)"

- φ_f = filler volume fraction 填料体积分数；下标 f / 0 分别指填充/未填充橡胶。
- Definition 定义："Reinforcing fillers increase the rubber's stiffness without impairing the strength and losing the rubbery characteristic."
- Common fillers 常用填料：carbon black 炭黑、zinc oxide 氧化锌、silica 白炭黑、clay 滑石粉/黏土。
- Origin 物理来源：源自 Einstein 悬浮粒子粘度方程。

## Mullins effect 应力软化（2.3）

> "the stress-strain curve depends on the maximum loading previously encountered"
> "the 'prestrained' chains first reach maximum extension, and then they either become detached or break ... detached/broken chains no longer share the overall applied load, thus giving rise to the observed softening of stress behavior."

- Bueche molecular mechanism Bueche 分子机制：填料间 prestrained 链先达最大延伸 → 脱附/断裂 → 后续循环不再分担载荷。
- Key judgement 关键判断：Mullins effect 不仅存在于填充橡胶，也存在于未填充橡胶。
- Countermeasures 对策：硅烷偶联剂增强填料-聚合物界面、控制填料粒径分布、优化分散。

## Stress-induced crystallization 应力诱导结晶（2.4）

> "These crosslinks then, in turn, cause a rise in elastic stress ... ~10¹¹ Pa ... five orders of magnitude higher than the elastic moduli of rubbery materials (~10⁶ Pa)."

- Critical point 临界点：天然橡胶 λ > 0.3 后应力陡升。
- Temperature sensitivity 温度敏感性：30°C 与 60°C 曲线差异明显；60°C 时仅见末端轻微上翘（受 finite extensibility 限制）。

## Viscoelasticity and TTS 粘弹性与时间-温度叠加（2.5, Eq. 20–22）

> "There are three main characteristics of viscoelastic materials: creep, stress relaxation, and hysteresis."
> "E(t) = σ(t)/ε₀ (Eq. 20)"
> "E(t₁,T₁) = E(t₁/a_T,T₂) (Eq. 21)"; "log a_T = log(t₁/t₂) (Eq. 22)"

- Constitutive models 本构模型：Maxwell、Kelvin-Voigt、Generalized Maxwell。
- Case 案例：BPA-PC（Mw = 40,000 g/mol），参考温度 141°C（Fig. 10）。

## Academic critique 学术对话与批判（报告 §3.6）

| Issue 议题 | Source note 出处 | Comment 评述 |
| --- | --- | --- |
| PdV 项处理 | "PdV is so small relative to the fdl that PdV can be dropped out"，但作者又 "for the sake of completeness" 保留 | 学界长期争论；对高度可压缩的泡沫腰围，PdV 可能不可忽略 |
| Eq. 11 的局限 | "in practice, does not comply well with the real behavior of rubber-like materials" | 热力学完美方程在实测中失真——采购评估不宜"唯公式论" |
| Mullins 归因 | 引用 Bueche 填料-链脱附机制 | 后续研究补充：填料聚集体自身破坏、聚合物主链断裂同样重要 |
| TTS 适用范围 | 主曲线在参考温度 141°C（BPA-PC）附近有效 | 卫材宽温区（冷藏 −25°C 到穿着 40°C）下 WLF 在 Tg+50 之外可能失效，[待验证] |
| 未涉及主题 | 发泡橡胶、生物基弹性体（TPS 等）、回收橡胶粉 | 正是卫材绿色创新的切入点 |

## Hygiene implication 卫材关联

Highly relevant — the chapter's own business hooks cover waistband, leg cuff and backsheet adhesive elastomers. 落地要点：
1. **腰围弹性体选型**：要求 Tg < −20°C（确保常温处于橡胶态、链段充分活动以保证 complete recovery）、伸长率 ≥ 300%、回复率 ≥ 90%。采购时应索取 Tg、M_c、拉伸-回复曲线。
2. **背胶交联度平衡**：M_c 同时决定模量与剥离力——交联不足则永久变形/残胶，过度交联则脆、剥离力高。建议用 Shore A 硬度 + 180° 剥离力 + 循环拉伸回复率三项数据验收。
3. **Mullins 效应 = 腰围越穿越松**：需要 500 次循环拉伸测试（如 ASTM D882）评估软化量；建议验收线为软化后模量保持率 ≥ 80%。
4. **TTS 加速寿命**：在 40/50/60°C 三档测应力松弛绘制主曲线，用短期数据预测 30 天穿着后的腰围保持力，避免"上机好、下机差"。
5. **填料选型**：φ_f 每升 0.05 按 Guth–Smallwood 模量约增 6%；但填料必然带来 Mullins 效应——增强与疲劳是一体两面，需配合硅烷偶联剂界面改性。

## Related Sources 关联来源

- [[Spandex Elastomer Brand Comparison & DMAC Safety Assessment（氨纶弹性体品牌对比及 DMAC 安全评估 2026-07-28）]] — 氨纶弹性体牌号对比，交联/回弹的产业侧数据。
- [[STM-00070 Elastic Tension - BCC Products（皮筋张力测试 第4版）]] — 皮筋张力标准测试方法，对应循环拉伸与张力保持。
- [[BCC Pants Waist Break Study（Pants 产品拉断研究与两项新方法创建）]] — Pants 腰围拉断失效分析，与应力诱导结晶和极限拉伸相关。
- [[Pin-Hole Module, Targeted Fluff Distribution & Elastic Recovery Process Review（新材料开发与弹性恢复工艺探讨）]] — 弹性恢复工艺，对应蠕变-恢复与永久形变。
- [[Viscoelastic Properties of Amorphous Polymers]] — 同批编译的粘弹性讲义，提供 Maxwell 模型与 G(t)/J(t) 的定义基础。

---
type: concept
title: "PE-PET Bond Efficiency Model"
domain: [卫材研发, 无纺布工艺]
status: growing
updated: 2026-09-29
tags: [粘合模型, 穿透热风, ES纤维, CD拉伸, 单组分PET]
aliases: ["PE-PET Bond Efficiency Model PE-PET 粘合效率模型"]
---

# PE-PET Bond Efficiency Model PE-PET 粘合效率模型

> **Definition 定义**：A two-parameter bond-count model that predicts the loss of web tensile when part of an ES (PE/PET bicomponent) fibre population is replaced by **non-bonding one-component PET** — and the point at which CD tensile crosses a converting floor.（一个双参数粘合点模型，用于预测当部分 ES（PE/PET 双组分）纤维被**不可粘合的单组分 PET** 替代时网面拉伸的损失，以及 CD 拉伸跌破转化下限的临界点。）

## Model 模型

```
B(w) = w² + 2w(1 − w) · k
```

- `w` = ES weight fraction（ES 重量占比）；`(1 − w)` = inert PET fraction（惰性 PET 占比）。
- `k ≈ 0.55` = **PE-to-PET adhesion efficiency** relative to PE-to-PE.（PE 与 PET 之间的粘合效率相对于 PE-to-PE 的比值。）
- The `w²` term counts ES–ES crossings (fully bondable); the `2w(1−w)·k` term discounts ES–PET crossings by `k`. 1-crossings among inert PET contribute nothing.
- **Net CD tensile** weights `B(w)` at **85%** and a fibre-tenacity term at the remaining **15%**.

（`w²` 项计 ES–ES 交叉（完全可粘）；`2w(1−w)·k` 项把 ES–PET 交叉按 k 折算；惰性 PET 之间的交叉无贡献。最终 CD 拉伸中 `B(w)` 权重 85%、纤维强度项权重 15%。）

## Results 结论

1. **Bond count falls faster than the ES fraction does** — this is the central non-linearity, and it is why a "26% PET" substitution costs more tensile than 26% suggests.（粘合点下降速度快于 ES 占比的下降——这是核心非线性，也是"26% 替代"损失大于直觉的原因。）
2. **Crossover with the 8.0 N/50 mm converting floor sits near 41% PET.** Option B at 26% keeps about **16% headroom**; modelled CD tensile is **9.3 N/50 mm** against the 8.0 N floor.（与 8.0 N/50mm 转化下限的交点在约 41% PET；26% 的 Option B 保有约 16% 余量，模拟 CD 拉伸 9.3 N/50mm。）
3. **Reclaim 3–5% of the loss by oven compensation** — a higher oven temperature and a 10–15% longer dwell let fewer ES crossings each carry more load. The cap on this lever is caliper: over-bonding collapses loft and destroys the softness case.（可通过烘箱补偿回收 3–5% 损失——提高风温、延长停留 10–15%，让更少的 ES 交叉各承担更大载荷；该杠杆的上限是厚度：过粘合会压塌蓬松并毁掉柔软度主张。）
4. **Fibre tenacity partially offsets the loss** — a higher-tenacity PET (4.5–5.5 cN/dtex vs the 2.5–3.0 cN/dtex ES bico range) offsets part of the bond-density loss, since fibres break less even though bonds break more.（更高强度的 PET（4.5–5.5 cN/dtex，对比 ES 双组分 2.5–3.0）可部分抵消粘合密度损失：纤维更少断，但粘合点更多断。）

## Key parameter table 关键参数表

| Parameter 参数 | Value 典型值 | Source 出处 |
|---|---|---|
| PE-to-PET adhesion efficiency `k` | ≈0.55 (relative to PE-to-PE) | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Bond-model weighting 权重分配 | B(w) at 85%, fibre-tenacity term at 15% | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| CD tensile crossing floor CD 拉伸交点 | ≈41% PET vs 8.0 N/50 mm | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Modelled CD tensile 模拟 CD 拉伸 | 9.3 N/50 mm (Option B, 26% PET) | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |
| Tensile acceptance gate (25 gsm programme) | ≥75 N/m wet tensile (finished diaper) / ≥70 N/m sheet | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Bonding-strength gate 粘合强度门 | ≥10 N/cm peel (strength vs flattening balance) | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| Caliper constraint 厚度约束 | Hole ≥92% caliper retention; loss ≥8% kills the gain | [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] |
| ES fraction rules ES 占比规则 | Keep ES ≥80 wt% (target ≈85 wt%) in shaped-fibre builds | [[ATB Topsheet with Bico Spunbond for 600 mpm Ultrasonic Lamination]]、[[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]] |
| Mechanism statement 机理论断 | One-component PET does not bond at PE-sheath air-through temperatures | [[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]] |
| Tenacity headroom 强度余量 | PET 4.5–5.5 cN/dtex vs ES bico 2.5–3.0 cN/dtex | [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] |

> ⚠️ **No unsourced parameters 禁止无来源参数**：模型与 k≈0.55 均为**单一来源的内部模型参数**，库内无第二来源交叉验证；跨聚合物体系（CoPET 皮层）的 k 值标 `[待验证]`。

## Adjacent concepts 相邻概念

- Ingredients 组分：[[皮芯复合纤维]]、[[三叶形截面纤维（Trilobal Fibre）]]、[[Pentagram PET (Star Cross-Section Fibre)]]
- Process 工艺：[[热风粘合无纺布]]、[[Ultrasonic Bonding of PET-Containing Topsheet]]
- Dosage frame 剂量框架：[[Shaped PET Add-On Window]]
- Structure 结构：[[ATB双梳理面层（Dual-Card Topsheet）]]
- Related cost/process page 成本工艺相邻页：[[CoPET（低熔点共聚酯）]]

## Lessons learned 经验教训

> ✅ **Validation（2026-09-29）**：本批四份来源在"**不可粘的异形 PET 会削弱粘合**"这一机理上互证（[[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] 给出定量模型，[[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]]、[[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]]、[[ATB Topsheet with Bico Spunbond for 600 mpm Ultrasonic Lamination]] 给出定性约束与 ES 占比下限）。与既有 [[皮芯复合纤维]] 页"皮层选择性熔融是本质"一致。

- **要点**：配方评估应**先算粘合点，再算液体指标**——粘合点不足时所有液体指标都不可信（网面已在起毛/断边）。
- **风险**：补偿手段（升温、延长停留）与**厚度/蓬松**互为敌对；必须"先对齐厚度，再测液体指标"。
- **待补 `[待验证]`**：k 值在 CoPET/PET 皮层体系下的取值；模型在 45 gsm 以上克重与多梳理构型下的适用性。

## Sources 来源

- [[Trilobal PET for MD Distribution in 45 gsm Dual-Card ATB Liner]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/Trilobal_PET_Liner_MD_Distribution.pptx.md`
- [[Pentagram PET Fiber Add-On for 25 gsm ATB Diaper Liner (Deep Dive)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/pentagram_PET_diaper_liner_deep_dive 1.pptx.md`
- [[Pentagram-Free Shaped PET Alternatives for 25 gsm Diaper Topsheet]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/pentagram_free_shaped_PET_alternatives_8slides.pptx.md`
- [[ATB Topsheet with Bico Spunbond for 600 mpm Ultrasonic Lamination]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/ATB_topsheet_600mpm_ultrasonic_8slides.pptx.md`
- [[KC Diffusion-Enhanced Topsheet v3 DOE Plan (C1-C4 Liner DOE)]] —— `RAW/ima_sync/个人知识库/WKB/Projects/Liner/KC_Diffusion_Enhanced_Topsheet_v3.xlsx.md`

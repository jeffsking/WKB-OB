---
type: source
title: "Porous Structure and Liquid Flow Models"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Absorbent Technology (Chatterjee & Gupta)/chapters/Absorbent Technology_ch01_report.md.md
original_link: ""
date_published: 2002
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
author: "Pronoy K. Chatterjee (Nutech International, East Brunswick NJ), Bhupender S. Gupta (College of Textiles, NC State, Raleigh)"
edition: "2nd"
publisher: "Elsevier (Academic Press) Science B.V."
year: 2002
isbn: ""
original_language: "EN"
parent_book: "[[Absorbent Technology]]"
key_claims:
  - "Capillary pressure — not gravity or imposed pressure — is the intrinsic driving force for absorption into a porous medium."
  - "Unsteady absorbency flow is mathematically a diffusion-type process (Darcy + diffusivity factor F(s)); the visually observed front obeys x_v ∝ t^1/2 (Washburn/Rudd)."
  - "Pore size sets the absorption RATE; pore volume sets the CAPACITY — two independent, competing design levers."
  - "Fibre density is the hidden capacity lever: Vs = (1/φ)(1/ρ_f − 1), so low-density cellulose (~1.5 g/cc) beats polyolefin (~0.92 g/cc) per unit areal density — provided wettability is comparable."
  - "The strategic open problem: 'materials that have the densities of polyolefins but the hydrophilicities of celluloses'."
  - "Fibre packing fraction in a web is only 2.5–10% (Gupta), so the web is overwhelmingly void; binder volume subtracts directly from pore volume."
pages_linked: ["[[Absorbent Technology]]", "[[达西定律 Darcy's Law]]", "[[Washburn Equation]]", "[[SAP（高吸水树脂）]]", "[[吸收芯体]]", "[[ADL（导流层）]]", "[[绒毛浆（Fluff Pulp）]]", "[[Characterisation, testing and modelling of nonwoven fabrics]]", "[[Chemical bonding]]"]
---

# Porous Structure and Liquid Flow Models

## One-line Position 一句话定位

Chapter 1 (pp. 18–73) is the physics bedrock of the whole handbook: it converts "fast-absorbing core" into three measurable quantities — capillary pressure, permeability/flow rate, and pore volume — and closes with the specific-air-volume relation that lets REL teams predict capacity from fibre density and packing fraction before any prototype is spun.（中文：第 1 章把"吸得快"翻译成三个可测量——毛细压力、渗透率/流速、孔隙体积，并以比空气体积关系给出"料定产能"的前置预测工具。）

## Summary 摘要

- **Driving force.** "The driving force for absorption of the bulk of the liquid into an absorbing material, which is in most cases a porous medium, is the capillary pressure" (p. 19); gravity/pressure are secondary.
- **Unsteady flow = diffusion.** "Unsteady flow in a porous medium is similar to a diffusion process ... or a heat conduction process" (p. 36). The governing PDE is ∂s/∂t = ∇·[F(s)∇s], where F(s) = (k/μΦ)(dp/ds) is the diffusivity factor (soil-physics "moisture diffusivity").
- **The √t law.** With constant diffusivity, s = 1 − erf(x/√(4F₁t)), so "x_v/t^(1/2) is a constant" (Rudd, p. 37) — the theoretical basis for why product testing must use a fixed time window (e.g. 60 s uptake, 40 g distribution) rather than running to equilibrium.
- **Steady flow + permeability.** Darcy's law q = −K∇P with K = k/μ; permeability estimated by Kozeny–Carman k = Φ³/[k″S₀²(1−Φ)²] (k″≈5), plus network models (Dullien) and drag theories (Iberall, Brinkman). Validity ceiling: "the critical Reynolds number above which this deviation occurs is around 1 ... in the range of 0.1 to 75" (p. 35, Scheidegger).
- **Capacity from structure.** C = ρ_L·Φ/[ρ(1−Φ)]; and Vs = (1/φ)(1/ρ_f − 1) (Eq. 46) — the single most useful relation in the chapter for areal-density-based design.
- **Pore-size geometry.** Three fibres forming an equilateral triangle constitute the capillary of a fibrous web; pore size Y is an explicit analytic function of fibre diameters and linear densities — a computable blending tool for pulp/nonwoven/SAP mixes.
- **SAP swelling kinetics.** Equilibrium swelling is governed by cross-linking (↓), ionisation (↑) and ionic strength (↓); swelling mode spans Fickian (V ∝ t^1/2) to Case II (V ∝ t), with real gels following the mixed V = K₁t^1/2 + K₂t. Case II imposes tensile stress on the unswollen solid — the mechanical root of gel blocking.

## Key Numbers & Conclusions 提炼数字与结论

| 项目 Item | 数值 / 结论 Value / Conclusion | 备注 Note |
|---|---|---|
| Max absorption capacity | C = ρ_L·Φ / [ρ(1−Φ)] | Eq. 10, p. 30 |
| Porosity from density | Φ = 1 − ρ_bulk/ρ | Eq. 9, p. 30 |
| Permeability | k = Φ³/[k″·S₀²(1−Φ)²], k″ ≈ 5 | Kozeny–Carman, Eq. 17, p. 33 |
| Hydraulic diameter | D_H = 4Φ/[S₀(1−Φ)] | Eq. 16, p. 33 |
| Diffusivity factor | F(s) = (k/μΦ)·(dp/ds) | p. 36 |
| Constant-diffusivity example | F₁ = 0.20 cm²/s, L₀ = 20 cm | Fig. 6, paper-like material |
| Packing fraction φ (measured) | 0.025–0.10 (2.5%–10%) | Gupta; material/weight/bonding dependent |
| Specific air volume | V_s = (1/φ)(1/ρ_f − 1) | Eq. 46, p. 54 |
| Fibre density: cellulose | ~1.5 g/cc | Fig. 15/16 |
| Fibre density: polyolefin | ~0.92 g/cc | lower ρ → higher Vs, but poor wetting |
| Darcy validity | Re_crit ≈ 1; range 0.1–75 | Scheidegger, p. 35 |
| Network model accuracy | Dullien model on 14 sandstone samples, mean error ±23% | p. 35 |
| Swelling (mixed) | V = K₁·t^1/2 + K₂·t | Eq. 38, p. 49 |
| Front advance | x_v ∝ √t | Washburn Eq. 7 / Rudd p. 37 |

## Key Claims 关键论断

- **Rate and capacity are antagonists, and both are geometric.** Bigger pores raise rate (Hagen–Poiseuille: flow ∝ r², so Y ×2 → flow ×16) but lower capillary pressure (p_c ∝ 1/r), so capacity falls. The optimum sits mid-range, not at either extreme.
- **Kozeny–Carman is a leverage equation.** k ∝ Φ³/(1−Φ)² — a small porosity gain yields a large permeability gain, but raising Φ means lower packing fraction, i.e. thinner web, more thickness, or fewer g/m². The trade is real and unavoidable.
- **Fibre density beats g/m² intuition.** Lower-density fibres give more void per gram at equal areal density — but only if wettability is comparable; polyolefin's 0.92 g/cc is a trap without a hydrophilic surface.
- **Binder is a capacity tax.** Binder volume is subtracted directly from pore volume; glue loading and web strength must be co-designed against absorption capacity.
- **Test windows are not convenience, they are physics.** Because uptake decays as √t, the first 30 s absorbs roughly what the next 300 s do — hence time-boxed protocols (60 s uptake, 40 g distribution) are the correct instrument.
- **Next-generation material target.** "The challenge, thus, lies in developing next generation polymeric materials that have the densities of polyolefins but the hydrophilicities of celluloses" (p. 53) — the stated frontier.

## Related Pages 关联页面

- 父书：[[Absorbent Technology]]
- 概念：[[达西定律 Darcy's Law]]、[[Washburn Equation]]、[[毛细压力 Capillary Pressure]]、[[孔隙率 Porosity]]、[[渗透率 Permeability]]、[[SAP（高吸水树脂）]]、[[Gel Blocking（凝胶阻塞）]]、[[吸收芯体]]、[[ADL（导流层）]]、[[绒毛浆（Fluff Pulp）]]、[[双组分纤维 Bicomponent]]
- 相关章节/页面：[[Absorbent Technology Introduction]]、[[Characterisation, testing and modelling of nonwoven fabrics]]（测试与建模）、[[Chemical bonding]]（粘合剂容量税）、[[Dry-laid web formation]]（气流成网孔径）

## Source 原文

- 本地路径 Local path：`RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Absorbent Technology (Chatterjee & Gupta)/chapters/Absorbent Technology_ch01_report.md.md`
- 原文链接 Original link：

> 🔗 治理合并（2026-09-30）：[[Liquid Flow in Porous Structures]] 已并入本页（指针页保留，原文存档于指针页）。Absorbent Technology 同章 IMA 重同步双编译

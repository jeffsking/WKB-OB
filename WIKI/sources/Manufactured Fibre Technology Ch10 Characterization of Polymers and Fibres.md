---
type: source
title: "Manufactured Fibre Technology Ch10 Characterization of Polymers and Fibres"
source_type: book
source_path: RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Manufactured_Fibre_Technology/Manufactured Fibre Technology · analysis_ch10.md.md
date_published: 0
date_processed: 2026-09-29
credibility: 高
knowledge_update_status: done
key_claims:
  - "Fibre characterization has received relatively less attention than polymer characterization, so general polymer methods must be adapted for fibres (p.203)"
  - "The molecular weight distribution influences the properties of the final product and must be characterized and controlled through appropriate variation of process parameters (p.204)"
  - "Methods split into absolute methods (end group analysis, osmometry, light scattering) determined from first principles and secondary methods (viscometry, gel permeation chromatography) requiring calibration with standards (p.206)"
  - "Polymers and fibres have a two phase structure comprising an ordered (crystalline) and a disordered (amorphous) phase; five widely used techniques are density measurement, optical birefringence, X-ray diffraction, small angle X-ray scattering and infrared spectroscopy (p.219)"
  - "The orientation function from birefringence is the overall orientation function, distinct from the crystalline orientation function determined by X-ray diffraction (p.225)"
  - "Combining IR data with X-ray data allows amorphous orientation to be estimated, because the trans conformer exists in both phases while gauche is confined to the amorphous phase (p.238)"
summary_cn: "第10章是全书的表征方法工具箱：按分子级（分子量及分布、绝对法 vs 相对法）、物理结构（密度、双折射、X射线、SAXS、红外）与热/显微三大层面梳理纤维表征技术，并给出结晶度、取向函数、晶粒尺寸与长周期等关键量的计算公式。"
tags: ["source/book", "characterization", "molecular-weight", "crystallinity", "orientation", "XRD", "SAXS", "IR", "DSC", "microscopy"]
tags_zh: ["源/书籍", "表征方法", "分子量", "结晶度", "取向", "X射线衍射", "小角散射", "红外光谱", "热分析", "显微"]
domain: "hygiene-materials"
priority: "P1"
pages_linked: ["[[Manufactured Fibre Technology]]", "[[Manufactured Fibre Technology Ch09 Heat-setting of Thermoplastic Fibres]]", "[[应力诱导取向与结晶]]", "[[Raw Material Testing Method Summary（原材料测试方法汇总表）]]", "[[低熔点PP技术路线对比]]"]
---

# Chapter 10 Characterization of Polymers and Fibres 聚合物与纤维的表征

> Source: Manufactured Fibre Technology, Ch.10, pp.203–245.
> Author of chapter: A.K. Gupta. 本章作者：A.K. Gupta。

## Summary 摘要

This is the book's **methods toolbox 方法工具箱**. Characterization is organized into three levels: **molecular level 分子级** (molecular weight and its distribution), **thermal properties 热性能** (glass transition, melting, crystallization, decomposition) and **physical structure and morphology 物理结构与形态** (crystallinity, crystallite size, orientation). Each level is presented with principles, working equations and instruments, so later fibre-specific chapters can quote crystallinity, orientation function, long period or degree of crystallinity against a common methodology.

Opening claim (p.203): "However, fibre characterization has received relatively less attention than polymer characterization [1-3]." 纤维表征相对聚合物表征受关注不足。

## Molecular Level 分子级表征

Why distributions matter (p.204): "The molecular weight distribution, which influences the properties of the final product, must be characterized and controlled through appropriate variation of process parameters." Hence several averages are needed together — number-average **Mn**, weight-average **Mw**, z-average — plus **polydispersity 多分散性** = Mw/Mn (1 for monodisperse, normally well above 1). Table 10.1 gives typical values by route: **addition polymerization 1.5–2.0**, **branched polymer 20–50** (p.204).

Two classes of method (p.206): "primary or absolute methods, which determine molecular weight from first principles. These include end group analysis, osmometry, light scattering... secondary methods, which require calibration with known molecular weight standards, such as the methods based on viscometry and gel permeation chromatography."

| Technique 技术 | Type 类别 | What it yields 读出量 | Page |
|---|---|---|---|
| End group analysis 端基分析 | Absolute 绝对法 | Mn (titration of PET / nylon end groups) | p.207 |
| Osmometry 渗透压（膜法/蒸气压） | Absolute | Mn | p.208 |
| Light scattering 光散射 | Absolute | Mw | p.210 |
| Viscometry 黏度法 | Secondary, calibrated | Viscosity-average M via **[η] = K M^a** (Mark-Houwink) | p.214 |
| GPC 凝胶渗透色谱 | Secondary, calibrated | Mw/Mn and full distribution | p.216 |

## Physical Structure and Morphology 物理结构与形态

The starting axiom (p.219): "polymers and fibres have a two phase structure comprising an ordered (also called crystalline) and a disordered (also called amorphous) phase." The five widely used techniques: "(1) density measurement, (2) optical birefringence, (3) X-ray diffraction, (4) small angle X-ray scattering and (5) infrared spectroscopy."

| Technique 技术 | Key quantity 关键量 | Working equation 公式 | Page |
|---|---|---|---|
| Density measurement 密度法（梯度柱） | Crystallinity from additivity V = X·Vc + (1−X)·Va (Table 10.3 lists ρa/ρc per polymer) | V = X·Vc+(1−X)·Va | p.220 |
| Optical birefringence 光学双折射 | Overall orientation; Δn = difference of refractive index in two orthogonal directions (Babinet compensator) | Δn; f = (1/2)(3cos²φ−1) | pp.223–224 |
| X-ray diffraction X射线衍射 | Crystallinity, crystallite size, crystalline orientation | **2d sinθ = nλ** (Bragg, p.226); **t = Kλ/(B cosθ)** (Scherrer, p.228) | pp.226–228 |
| Small angle X-ray scattering SAXS | **Long period 长周期** = average vertical distance between two crystallites in the fibril; Bragg gives d ≈ 100 Å corresponding to 2θ ≈ 1°, beyond WAXS range | Bragg at very low angle | p.229 |
| Infrared spectroscopy 红外（FTIR / ATR / IR dichroism） | Group frequencies, Beer-Lambert quantification, **dichroic ratio R = A∥/A⊥** | R = A∥/A⊥ | pp.230–236 |

**Overall versus crystalline orientation** (p.225): "Such an orientation function is thus called the 'overall orientation function', as distinct from the 'crystalline orientation function' determined by X-ray diffraction." Because birefringence carries both crystalline and amorphous contributions while X-ray sees only the crystalline phase, the two are not interchangeable. 总体取向 ≠ 结晶取向。

**Amorphous orientation by IR + X-ray** (p.238): "One of the most important and useful applications of IR spectroscopy to the study of fibres is the possibility of using the IR data in combination with X-ray data to estimate amorphous orientation." The logic: **trans** conformers occur in both phases, **gauche** only in the amorphous phase (p.238). Worked examples use PET trans/gauche quantification and nylon/PET end-group titration.

## Thermal and Microscopic Characterization 热表征与显微表征

- **DTA / DSC 差热/差示扫描量热** — Tg, Tm, Tc, decomposition (p.239).
- **TG / DTG 热重** — thermal stability (p.240).
- **TMA 热机械分析** — transitions via probe penetration (p.241).
- **DMA / DMTA 动态力学分析** — loss peaks, WLF equation (p.242).
- **Optical microscopy 光学显微镜** — ordinary, polarized, phase contrast (p.244).
- **Electron microscopy SEM / TEM** — replicas, OsO4 staining, etching (p.245).

## Evidence Base 证据链

| Evidence type 证据类型 | Examples 实例 | Scale 数量 |
|---|---|---|
| Mathematical derivation 数学公式/推导 | Mn, Mw, Scherrer, Bragg, Mark-Houwink | approx. 28 equations |
| Experimental procedure 实验流程 | End-group titration, density gradient column preparation | medium |
| Data tables 数据表 | Table 10.1, 10.3, 10.4 | 3 tables |
| Figures / instrument schematics 图谱 | Fig. 10.1–10.28 | 28 figures |
| Literature citations 文献引用 | [1]–[25] | 25 |

Assessment from the source: molecular-level and physical-structure sections are strongly argued with complete equations and figure cross-checks; thermal and microscopy sections are enumerative descriptions with fewer worked examples; no systematic comparison of method error and applicability boundaries is given, so independent method selection is hard — flagged as a limitation of methods-survey chapters.

## Limitations 局限（源自原书内容）

- "作为 1997 年教材，方法偏经典" — NMR for chain-structure characterization only mentioned in passing (stereochemical studies, p.237); **AFM** and later surface/nano-morphology tools absent; hyphenated techniques such as GPC-FTIR not discussed.
- 公式与图表符号多处 OCR 错误（如 p.231 波数边界、Fig. 10.24 标注为 OTA/OSC），阅读需对照原文。

## Hygiene implication 卫生材料启示

High utility as a **reference vocabulary and method-selection frame**, even though no hygiene product is mentioned in the chapter.

1. **Sheath-core PP/PE bicomponent fibre specification** depends on exactly the quantities defined here: crystallinity by density or XRD, melting onset by DSC, crystallite size by Scherrer. When qualifying a low-melting-point PP sheath grade, DSC onset vs. through-air oven temperature is the same pair of numbers discussed at pp.220 and 239 — see [[低熔点PP技术路线对比]].
2. **Orientation splitting matters for nonwoven filaments**: birefringence gives overall orientation (crystalline + amorphous), XRD gives crystalline orientation only. Using them interchangeably is the common error warned against at p.225; the IR+X-ray route to amorphous orientation (p.238) is what explains why a high-spinning-speed PP/PET filament can have high XRD orientation yet mediocre tenacity. See [[应力诱导取向与结晶]].
3. **Molecular-weight control of PP for meltblown/spunbond**: the MFI-grade PP used in polyolefin nonwovens is selected by Mw and polydispersity; this chapter supplies why multiple averages plus distribution are needed rather than a single value (p.204).
4. **Cross-check discipline**: the chapter's recurring theme that one physical quantity should be measured by two independent routes and compared applies directly to raw-material incoming inspection — see [[Raw Material Testing Method Summary（原材料测试方法汇总表）]].
5. Link to Chapter 9: **CDT (critical dissolution time)** used there as a crystallinity proxy rests on the density-crystallinity additivity defined here — see [[Manufactured Fibre Technology Ch09 Heat-setting of Thermoplastic Fibres]].

Chapter 10 says nothing about fluff pulp, SAP or absorbency measurement; those stay outside this source.

## Related Sources 关联来源

- [[Manufactured Fibre Technology]] — book index
- [[Manufactured Fibre Technology Ch09 Heat-setting of Thermoplastic Fibres]] — CDT and crystallinity proxies defined here, applied there
- [[应力诱导取向与结晶]] — orientation/crystallization coupling in fibre processing
- [[Raw Material Testing Method Summary（原材料测试方法汇总表）]] — incoming raw-material test methods, cross-check discipline
- [[低熔点PP技术路线对比]] — low-melting PP sheath grades qualified via DSC/on-set temperature

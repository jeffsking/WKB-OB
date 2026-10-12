---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_716de7a636ebbef968ea468e3b853238001a693ee6c0644e"
source_file: "Gravure_Roll_101_ch4_Trials_and_Design_拆解报告.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Training/Pants/Gravure Roll 101 (KC 2025)/Gravure_Roll_101_ch4_Trials_and_Design_拆解报告.md.md"
extracted: "2026-10-01"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: ""
processed: ""
---

# Gravure_Roll_101_ch4_Trials_and_Design_拆解报告.md



章节：Ch4 Trials & Design ｜ 覆盖幻灯片：29–38 ｜ 文档：Gravure Roll 101 (KC, Capability Days 2025) ｜ 拆解日期：2026-08-30

## 0. Sourcing & Method Notes（来源与方法说明）

Primary sources used for this report

||||
|---|---|---|
|Gravure_Roll_101_ch4_Trials_and_Design.md (text layer + speaker notes)|SLIDE 29–38|Verbatim from PPTX|
|「图像内容补充」block in the same file (pre-extracted by page rendering)|SLIDE 29–38 images|Stated reliable by task owner; used as-is|
|Re-render of uploads/Gravure Roll 101.pptx (LibreOffice → PDF → PNG, 130/260/300 dpi) and model-read of SLIDE 29–38|SLIDE 29–38 images|Added by this report to recover text that exists only inside images (notably SLIDE 38 Summary, SLIDE 36 band table, SLIDE 32 drawing dimensions)|


Why re-rendering was necessary: the SLIDE 38 "Summary" slide carries no text-layer bullets at all — the PPTX text layer contains only the word Summary, with the seven bullets baked into Picture 7. The pre-extracted 「图像内容补充」block states "p38 Summary 七条见正文文本层", which is not correct — the bullets are image-only. This report recovered them by rendering (see Module 3, T5).

Two source discrepancies found and recorded (not silently resolved):

||||||
|---|---|---|---|---|
|D1|SLIDE 34 annotation word|ceramic 'shell'|ceramic "shelf"|Rendered reading used as primary (shelf); shell recorded as the alternate reading. Both refer to the same defect: residual ceramic occluding the engraved cell after laser engraving|
|D2|SLIDE 32 dot-array dimensions|0.02926" / 0.02926" / 0.01463"|0.025926" / 0.051852" / 0.25926" / 0.14493"|Re-read values used; note that 1 / 0.025926² ≈ 1488, which is internally consistent with the drawing's own 1488 DOTS/SQ-IN callout, whereas 1 / 0.02926² ≈ 1168 is not|
|D3|SLIDE 29 control date|—|Control IR Engraving Jenks GR2 – 12/3/25 vs trial Pamarco Trial – 12/3/24|Control dated 1 year after the trial → [本报告标注：疑似笔误，应为 12/3/24]; not used as a factual date|


Verification checks that passed

- SLIDE 36 band widths sum to 13.75 + 11×7 + 13.75 = 104.5" — exactly equal to the 104.5" engraved-area callout on SLIDE 32. This independently validates the 9-band reading.
- SLIDE 32: 3,800,000 µm³/cell × 1488 cells/in² = 5.6544 BCM/in² — a physically plausible OLU gravure volume, cross-checked against Ch3 SLIDE 28's 27.6 BCM VIVA spec (a different, much deeper engraving).
Terms searched across the entire 38-slide deck and NOT found (declared up front; these drive the [未找到原句] marks in Modules 2–3): maintenance (0 hits), refurbish (0), inventory in text layer (0 — appears only inside the SLIDE 38 image), robustness (0), objectives (0), variables (0), defect (0), plugged (0), adhesive (0), cleaning (1 hit, and it is Embossing Cleaning System on Ch1 SLIDE 7 — an embosser-cleaning unit, not roll cleaning).

## 模块1：核心论点（Core Arguments）

### A1 — Every gravure roll trial in this chapter missed the product target; none achieved the 1800 OLU GMT target on first attempt.



"1100 GMT vs 1800 OLU GMT Target" (SLIDE 29, speaker notes)
"1550 GMT vs 1800 OLU GMT Target" (SLIDE 30, speaker notes)

Verifiable support: Two first-round trials (Pamarco VIVA Trial #1, 12/3/24; Apex VIVA Trial #1, 2/12/25) both report a measured GMT below the identical 1800 target. Attainment = 61.1% and 86.1% respectively [本报告推导, T2]. No slide in Ch4 reports a trial that met the GMT target.

### A2 — Gravure roll design is mathematically and practically an iterative loop, not a one-shot specification exercise.



"Gravure roll design is an iterative process" (SLIDE 36)
"Banded gravure rolls can help speed up the iterative process – typically don't produce sellable product – RSR not MSR" (SLIDE 36)

Verifiable support: The iteration is visible at three nested time scales inside Ch4: (i) within one trial — SLIDE 31 shows Apex VIVA Trial #2 "Ran for 24 Hours" with three sequential re-polishes (Re-Polish #1 / #2 / #3); (ii) across trials — VIVA Trial #1 (Pamarco, Apex) → VIVA Trial #2 (Apex); (iii) across vendors and years — SLIDE 34 "VENUS Engraving Journey": Harper → IR Engraving → Pamarco, with Harper needing "9 months to engrave first roll".

### A3 — You can specify only two of the three key engraving parameters (volume, depth, diameter); the third is emergent and must be measured.



"Engraver must have at least 1 degree of freedom. Can only specify 2 from the key engraving parameters of volume, depth, and diameter" (SLIDE 36)
"Same volume from different combinations of diameter vs depth" (SLIDE 36)

Verifiable support: SLIDE 36's band diagram encodes exactly this: 9 bands, only 3 distinct diameters (530 / 560 / 590 µm), only 4 distinct volume targets (5 / 6 / 7 / 8 BCM), and depth as the resulting measured value (31.42 – 43.14 µm). The band roll is a physical design-of-experiments over two locked parameters with one emergent output.

### A4 — Engraving variation translates directly and dramatically into finished-product property variation; therefore vendor capability is product capability.



"Product properties can change dramatically with engraving changes/inconsistencies" (SLIDE 38, bullet 6)
"X and Y direction sheet surface coverage - Key to GMT (Cell diameter)" / "Z direction sheet penetration - Key to VIVA/WypAll Z peel strength (Cell depth)" / "High Z direction penetration can also negatively impact bulk/caliper" (SLIDE 35)

Verifiable support: The causal chain is explicitly stated: cell diameter → GMT, cell depth → Z peel strength, excess depth/penetration → bulk/caliper loss. The 1100 vs 1550 GMT spread between two vendors engraving the same VIVA pattern is the empirical proof of A4.

### A5 — The gravure roll supply base is in a re-qualification phase, and the constraint on KC is inventory health and innovation speed, not just unit cost.



"New vendors are learning with KC as we attempt to get back to healthy gravure roll inventories and look to ignite innovation" (SLIDE 38, bullet 7)
"Engraved with 3 vendors and struggled with engraving consistency and quality until Pamarco came on line in Q3 2024" (SLIDE 32, speaker notes)
"Tissue machine can't run without 2 functional gravure rolls" (Ch3 SLIDE 23, speaker notes)

Verifiable support: Four vendors named (Ch3 SLIDE 22: Harper / Precision Roll Solutions–IR Engraving / Pamarco / Apex). Two named vendor failures documented on SLIDE 34 (Harper: 9 months + volume skew; IR Engraving: tool mismatch + low volumes + failed repeat of a banded roll). "get back to healthy inventories" is retrospective phrasing — it implies the inventory is currently unhealthy.

## 模块2：关键概念操作化定义（Key Concepts — Operationalized Definitions）

Notation: (b) and (c) are marked [SOURCE] when derived from deck content and [本报告定义] where the deck is silent. (d) is verbatim English with SLIDE N; [未找到原句] where the deck contains no such sentence.

### C1. Gravure Roll Trials ｜ 凹版辊试车

(b) Definition [SOURCE]: A structured on-machine or off-line run in which an engraved roll is produced to a candidate specification and the resulting printed/coated sheet is measured against a pre-set product target, alongside a control roll of the incumbent engraving.

(c) Operationalization [SOURCE]:
- Measurement dimensions: GMT (product property, vs. an explicit numeric target), DuPont Stain coverage (fluid deposition image at defined magnification), run duration (time-on-machine as an endurance/robustness screen), 3D topography (µm-scale cell dimensions).
- Decision rule (as practised): pass/fail against a single numeric target — measured GMT vs 1800 OLU GMT Target.
- Control design: each trial slide pairs the trial roll with a control roll engraved by the incumbent vendor (SLIDE 29, 30).
- Endurance gate: one trial is explicitly labelled "Ran for 24 Hours" (SLIDE 31) → duration is a trial parameter, not an afterthought.
- Iteration counter: rework loops within a trial are counted (Re-Polish #1/#2/#3).

(d) Verbatim:
> "Pamarco VIVA Trial #1 DuPont Stain Results" — SLIDE 29
> "Apex VIVA Trial #1 DuPont Stain Results" — SLIDE 30
> "Apex VIVA Trial #2 – Ran for 24 Hours" — SLIDE 31
> "1100 GMT vs 1800 OLU GMT Target" — SLIDE 29 (speaker notes)

### C2. GMT ｜ GMT（克重/抗张类片材指标，见下方缩写考辨）

(b) Definition [SOURCE — usage only]: A numeric sheet property used as the pass/fail target for OLU gravure trials; per SLIDE 35 it is driven by X–Y (in-plane) sheet surface coverage, which in turn is driven by cell diameter.

Acronym expansion — honesty note: The deck never expands "GMT" anywhere in all 38 slides [未找到原句]. Full occurrence list (exhaustive, 5 hits): SLIDE 29 notes, SLIDE 30 notes, SLIDE 35 body (plus duplicates in the raw dump). Candidate readings:
1. Geometric Mean Tensile — [本报告推断，最可能]。SLIDE 35 ties GMT to bidirectional X and Y coverage; the standard tissue metric that responds to both MD and CD is the geometric mean tensile, √(MD × CD). A "target of 1800" is consistent with a grammage-normalised tensile value, not a machine rate.
2. Grams per Minute / per Thousand (a dosing or count rate) — [未找到原句]。This reading is weakened by SLIDE 35, which frames GMT as a sheet property responding to surface coverage, and by the units-free "1800 OLU GMT Target" being a per-product constant rather than a line-speed-dependent rate.
3. Other — [未找到原句]。

Handling rule for downstream use: treat GMT as an opaque, vendor-neutral product KPI with a defined numeric target, and require the vendor/KC to supply the test method (instrument, specimen width, MD/CD combination rule, units) in writing before contractualising it. Do not assume a unit.

(c) Operationalization [SOURCE]:
- Target: 1800 (stated twice, SLIDE 29 + 30).
- Attainment: measured GMT / 1800, expressed as % [本报告推导, T2].
- Direction of control: increase via larger cell diameter (more X–Y coverage).
- Read-out pairing: GMT is always reported together with a DuPont Stain image (SLIDE 29, 30) — i.e. a number and a picture, never a number alone.

(d) Verbatim:
> "1100 GMT vs 1800 OLU GMT Target" — SLIDE 29 (speaker notes)
> "1550 GMT vs 1800 OLU GMT Target" — SLIDE 30 (speaker notes)
> "X and Y direction sheet surface coverage  - Key to GMT (Cell diameter)" — SLIDE 35

### C3. Trial objectives / variables / measures ｜ 试车目标 / 变量 / 测量

(b) Definition [本报告定义 — the deck does not use these three words]: The standard trial frame: objectives = the product properties to be achieved; variables = the roll/process parameters deliberately changed; measures = the instruments and metrics used to read the outcome.

(c) Operationalization — reconstructed from what the deck actually does:

||||
|---|---|---|
|Objectives|Achieve the 1800 OLU GMT target; achieve the Z peel strength needed for VIVA/WypAll; hold bulk/caliper|SLIDE 29, 30, 35|
|Variables|Cell diameter, cell depth, cell volume (pick 2 of 3); screen/pattern (34.5 DPI, 1488 dots/sq-in); vendor; re-polish iteration; run duration|SLIDE 36, 32, 34, 31|
|Measures|DuPont Stain (coverage image), GMT (numeric), Capatch strips (BCM/in² or cc/m²), Impression strips (contact/footprint), 3DQC system (3-D metrology), 3D Scan topography (µm)|SLIDE 29, 30, 33, 37, 31|
|Control|Side-by-side control roll engraved by the incumbent vendor|SLIDE 29, 30|
|Endurance|24 hours continuous run|SLIDE 31|


(d) Verbatim:
> "Measurement tools — Capatch strips / Impression strips / 3DQC measurement system" — SLIDE 37
> "DuPont Stain VENUS Commercial Trial #6" — SLIDE 33
> For the words objectives / variables: [未找到原句] (0 occurrences in the deck). The nearest source phrase is "the key engraving parameters of volume, depth, and diameter" — SLIDE 36.

### C4. Robustness ｜ 稳健性（抗变异能力）

(b) Definition [本报告定义]: The ability of an engraving to deliver the target product property consistently across cells, across the roll face, across re-polish cycles, and across production time.

(c) Operationalization — four proxies measurable from this deck:

||||
|---|---|---|
|Engraving consistency|Vendor-to-vendor repeatability of the same pattern; the deck's own verdict: "struggled with engraving consistency and quality until Pamarco"|SLIDE 32|
|Volume uniformity across face|Flat Burn Target < ±10% (Ch3 SLIDE 28 drawing note)|Ch3 SLIDE 28|
|Volume conformance to spec|Target - 3,800,000 µm³ ± 5%|SLIDE 32|
|Time robustness|Trial run extended to 24 hours, then re-polished 3× and re-measured|SLIDE 31|
|Property robustness|"Product properties can change dramatically with engraving changes/inconsistencies" → the sensitivity of the product to engraving noise is the inverse of robustness|SLIDE 38|


(d) Verbatim: for the word robustness — [未找到原句] (0 occurrences). Nearest source sentences:
> "Engraved with 3 vendors and struggled with engraving consistency and quality until Pamarco came on line in Q3 2024" — SLIDE 32 (speaker notes)
> "Product properties can change dramatically with engraving changes/inconsistencies" — SLIDE 38

### C5. Defect — plugged cells / ceramic shell / round cells ｜ 缺陷：网穴堵塞、陶瓷壳残留、圆整网穴

(b) Definition [SOURCE]: Engraving defects in which (i) the cell is partly or wholly occluded by residual ceramic left behind after laser engraving (the deck calls it a ceramic "shelf" in the rendered annotation; the pre-extracted supplement renders it "shell" — see D1), and (ii) the cell outline fails to form a complete, clean circle.

(c) Operationalization:

|||||
|---|---|---|---|
|Ceramic residual in cell|Optical microscopy of engraved/printed surface, 40X Zoom, annotated with a defect circle|"1/3 of dot" occluded on IR VENUS CT5|SLIDE 34|
|Incomplete / non-round cell|Same; positive criterion is a full circle|Pamarco CT9: "Dots are full circles and clean"|SLIDE 34|
|Plugged cells (post-run)|[未找到原句] — the words plugged / plugging do not appear in the deck|—|—|
|Downstream symptom|Volume shortfall; the deck links the IR period to "Struggled with low volumes"|qualitative|SLIDE 34|
|Root-cause anchor (Ch2)|Laser engraving raises corner peaks; "Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear" → removal/polishing is the controlling operation|qualitative|Ch2 SLIDE 14|


(d) Verbatim:
> "IR Engraving VENUS CT5 — Engraving – 1/3 of dot is still filled with ceramic "shelf"" — SLIDE 34 (image annotation, 300-dpi render read)
> "Pamarco VENUS engraving CT9 – Dots are full circles and clean. No ceramic "shelf"." — SLIDE 34 (image annotation, 300-dpi render read)
> For plugged cells: [未找到原句] (0 occurrences in the deck)

Note on the defect mechanism [本报告推导]: the deck places this defect at the engraving + final-polishing step, not at the run. Ch2 SLIDE 12 lists the ceramic roll production sequence ending in Laser engraving → Final polishing; Ch2 SLIDE 14 states polishing is mandatory to remove laser-induced corner peaks. A cell still holding 1/3 ceramic is therefore a post-engraving cleaning/polishing failure, i.e. a vendor process defect present at first article, not wear accrued in service.

### C6. "Volume / depth / diameter — pick 2" design law ｜ 「容积 / 深度 / 直径 — 只能锁两个」设计铁律

(b) Definition [SOURCE]: Of the three key engraving parameters — cell volume, cell depth, cell diameter — only two may be specified; the engraver must retain at least one degree of freedom, so the third parameter is determined by the other two plus the cell's geometry.

(c) Operationalization:
- Decision form: a roll specification is well-posed iff it fixes exactly 2 of {V, D, h}. Fixing 3 over-constrains the engraver (removes the required 1 DOF); fixing 1 under-specifies.
- Closure equation (idealised axisymmetric cell) [本报告推导]:
  V_cell = k · D² · h
  Dimensional check: [L²] × [L] = [L³] ✔.
  Fitted to the 9 SLIDE 36 bands: k ≈ 5.16 × 10⁻⁷ with V in BCM, D and h in µm; 1σ residual ≈ 10.0%; per-band error range −13.6% to +18.4%.
- Empirical consequence [本报告推导]: the residual scatter (~10% 1σ) is larger than the ±5% volume window on the VENUS spec (SLIDE 32). Therefore the third parameter can be predicted only to ~±10–18% and must be measured, never assumed — which is exactly why the deck calls design iterative.
- Screening instrument: a banded roll — one physical roll carrying multiple (D, V) combinations simultaneously (9 bands on SLIDE 36) — resolves the two-of-three trade-off empirically in a single run.

(d) Verbatim:
> "Engraver must have at least 1 degree of freedom.  Can only specify 2 from the key engraving parameters of volume, depth, and diameter" — SLIDE 36
> "Same volume from different combinations of diameter vs depth" — SLIDE 36
> "Banded gravure rolls can help speed up the iterative process – typically don't produce sellable product – RSR not MSR" — SLIDE 36

### C7. Gravure / adhesive maintenance ｜ 凹版辊与胶液维护

(b) Definition [本报告定义]: The set of routine actions that keep an in-service gravure station delivering fluid at its specified volumetric rate — doctor blade/chamber condition, fluid make-up and filtration, roll surface condition, and plugging prevention.

(c) Operationalization:
- From the deck: the only maintenance adjacency in the entire 38 slides is the Doctor Blade Chamber (Metering Blade / Containment Blade, Ch1 SLIDE 9) and the Print Fluid Make-up System / Print Fluid Delivery on the OLU line (Ch3 SLIDE 26).
- From Ch2, the one mechanism-level maintenance driver: Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear (Ch2 SLIDE 14) → blade wear is a function of engraving quality, so blade life is a maintenance KPI and an engraving KPI.
- Proposed KPI set [本报告建议], NOT sourced from the deck: doctor blade change interval; chamber seal condition; fluid solids/temperature control; volumetric re-verification interval (Capatch / 3DQC, SLIDE 37); plugged-cell count per unit area.

(d) Verbatim: for maintenance / adhesive — [未找到原句] (0 occurrences in the deck). Nearest source items:
> "Doctor Blade Chamber" / "Metering Blade" / "Containment Blade" — Ch1 SLIDE 9 (image)
> "Print Fluid Delivery" / "Print Fluid Make-up System" — Ch3 SLIDE 26 (image)
> "Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear" — Ch2 SLIDE 14

### C8. Roll cleaning ｜ 辊体清洗

(b) Definition [本报告定义]: Removal of residual fluid, dried coating, and ceramic debris from the engraved cell structure to restore the specified cell volume.

(c) Operationalization:
- Cleanliness state criterion (source-grounded, positive form): at 40X, dots must be "full circles and clean" with no ceramic residual — SLIDE 34. This is the deck's only explicit cleanliness acceptance language.
- Failure criterion (source-grounded, negative form): any dot with ≥1/3 of its area still filled — SLIDE 34 (action limit implied, not stated; no numerical AQL is given in the deck [未找到原句]).
- Process anchor (Ch2): cleaning/removal is inseparable from polishing; Ch2 SLIDE 12 places Final polishing as the last step of ceramic roll production, and Ch3 SLIDE 28 carries a hard numeric polish gate: POLISHING NOTE: Target <= 10,700,000 Shallow Dot Volume Average.
- Measurement tools for verification (SLIDE 37): Capatch strips (volume, BCM/in² or cc/m²), Impression strips (contact footprint), 3DQC system (3-D geometry).

(d) Verbatim:
> "Dots are full circles and clean. No ceramic "shelf"." — SLIDE 34
> "Measurement tools — Capatch strips / Impression strips / 3DQC measurement system" — SLIDE 37
> "Final polishing" — Ch2 SLIDE 12
> For the terms roll cleaning / cleaning the roll: [未找到原句] (the single clean hit in the deck is "Embossing Cleaning System", Ch1 SLIDE 7 — an embosser unit, not roll cleaning)

### C9. Ceramic roll refurbishment ｜ 陶瓷辊翻新

(b) Definition [本报告定义]: Restoration of an in-service or failed ceramic gravure roll to specification by re-polishing / re-engraving / re-plasma-coating, as an alternative to buying new.

(c) Operationalization — grounded in the deck's re-polish evidence:
- Unit of refurbishment iteration: the deck counts discrete Re-Polish #1 / #2 / #3 events on a single roll within a single trial (SLIDE 31) → refurbishment is iterative, and one pass is not assumed sufficient.
- Effect measurable per pass: each re-polish step is accompanied by a 3D Scan with µm-level readings (SLIDE 31: 3D Scan #2 30 lpi, 20 degrees; feature dimensions 649 / 627 / 729 / 697 / 896 / 187 µm on the main scan, and 867 / 670 / 665 / 777 / 756 / 122 / 204 µm on Re-Polish #1) → refurbishment is verified by topography, not by eye.
- Governing limit [本报告推导]: each polish removes material and therefore reduces cell volume; Ch3 SLIDE 28's POLISHING NOTE: Target <= 10,700,000 Shallow Dot Volume Average shows the deck already polices an upper bound on post-polish shallow-dot volume. Repeated re-polishing therefore walks the roll down a one-way volume ladder toward scrap — the number of viable refurbishment cycles is bounded by the volume window, and must be tracked per roll.
- No data on coating re-spray / re-plasma / strip-and-recoat [未找到原句].

(d) Verbatim:
> "Apex VIVA Trial #2 – Ran for 24 Hours" / "Re-Polish #1" / "Re-Polish #2" / "Re-Polish #3" — SLIDE 31
> "3D Scan #2 30 lpi, 20 degrees" — SLIDE 31 (image)
> For the word refurbish(ment): [未找到原句] (0 occurrences in the deck)

### C10. Roll inventory health ｜ 辊库存健康度

(b) Definition [SOURCE]: The state of holding enough rolls that are at specification and functional to run the assets and to fund innovation, as opposed to merely owning rolls.

(c) Operationalization:
- Qualitative target (the deck's own phrasing): "healthy gravure roll inventories" — SLIDE 38, bullet 7. No numeric definition is given [未找到原句].
- Hard floor from Ch3: Tissue machine can't run without 2 functional gravure rolls (Ch3 SLIDE 23) → minimum 2 functional rolls per machine, i.e. 1 running + ≥1 spare [本报告推导].
- Lead-time exposure: up to 9 months — Harper took 9 months to engrave first roll (SLIDE 34).
- Health metrics proposed [本报告建议, not from deck]: (i) # rolls at spec ÷ # rolls required per machine; (ii) vendor first-article attainment rate (see C2 / T2); (iii) count of qualified vendors per pattern (deck shows 4 vendors, Ch3 SLIDE 22, and 3 that failed on VENUS, SLIDE 32); (iv) refurbishment turnaround days; (v) longest observed engrave lead time.
- "Healthy" ≠ "full" [本报告推导]: the deck's own failure mode is owning rolls that are engraved but not to spec — the VENUS journey accumulated at least 5–6 engraving/trial events (VENUS CT5, VENUS CT9, VENUS Commercial Trial #6, VIVA Trial #1 ×2 vendors, VIVA Trial #2) without producing a passing GMT result. Inventory health must be measured in conforming rolls, not in roll count.

(d) Verbatim:
> "New vendors are learning with KC as we attempt to get back to healthy gravure roll inventories and look to ignite innovation" — SLIDE 38, bullet 7
> "Tissue machine can't run without 2 functional gravure rolls" — Ch3 SLIDE 23 (speaker notes)
> "Harper took 9 months to engrave first roll and then had a large volume skew" — SLIDE 34 (speaker notes)

### C11. Banded gravure roll ｜ 带状（多参数分区）凹版辊

(b) Definition [SOURCE]: A single roll whose face is divided into transverse bands, each band engraved to a different parameter combination, used to screen the design space in one run.

(c) Operationalization (from SLIDE 36 — full 9-band dataset):

||||||
|---|---|---|---|---|
|#9|13.75"|530 µm|6 BCM|35.78 µm|
|#8|11"|530 µm|7 BCM|43.14 µm|
|#7|11"|590 µm|5 BCM|31.42 µm|
|#6|11"|590 µm|6 BCM|32.95 µm|
|#5|11"|590 µm|7 BCM|38.71 µm|
|#4|11"|590 µm|8 BCM|41.99 µm|
|#3|11"|560 µm|7 BCM|42.03 µm|
|#2|11"|560 µm|6 BCM|40.31 µm|
|#1|13.75"|560 µm|5 BCM|36.63 µm|


Validation: Σwidths = 13.75 + 11×7 + 13.75 = 104.5" — exactly the engraved face width on the VENUS drawing (SLIDE 32). [本报告推导]
Design structure: only 3 distinct diameters × 4 distinct volumes → a 2-factor screen with depth emergent. [本报告推导]
Grade penalty: banded output is non-saleable — RSR not MSR (SLIDE 36).

(d) Verbatim:
> "Banded gravure rolls can help speed up the iterative process – typically don't produce sellable product – RSR not MSR" — SLIDE 36
> For the expansion of RSR / MSR: [未找到原句] (0 occurrences elsewhere in the deck). The slide glosses its own contrast as "don't produce sellable product", so MSR = saleable grade and RSR = non-saleable trial grade; treat both as opaque internal codes.

### C12. Measurement-tool parity ｜ 测量工具一致性

(b) Definition [SOURCE-grounded]: The requirement that vendor and customer measure the same parameter with the same instrument and method, or the datasets are not comparable.

(c) Operationalization:
- Named toolset (SLIDE 37): Capatch strips (volume, reads BCM/in² and cc/m²), Impression strips (contact footprint; package reads 2.0 mil / 20–50 µm), 3DQC measurement system (MicroDynamics Model 3DQC, 3-D metrology).
- Unit conversion gate (Ch2 SLIDE 18): 1 BCM/in² = 1.55 cm³/m².
- Screen-count unit hazard (Ch2 SLIDE 17): 180 Lines/cm and 180 Lines/inch are both "6 BCM VOLUME" yet are entirely different rolls; 180 LCM = 460 LPI and 180 LPI = 70 LCM. Any spec that says "180" without the unit is ambiguous by a factor of ~2.56 in screen count.
- Failure consequence (documented, SLIDE 34): Did not measure volume with same tools so none of the data translated.

(d) Verbatim:
> "Did not measure volume with same tools so none of the data translated" — SLIDE 34 (speaker notes)
> "Measurement tools — Capatch strips / Impression strips / 3DQC measurement system" — SLIDE 37
> "1 BCM/in2 = 1.55 cm3/m2" — Ch2 SLIDE 18
> "180 LCM = 460 LPI and 180 LPI = 70 LCM" — Ch2 SLIDE 17 (speaker notes)

## 模块3：证据链（Evidence Chain）

### T1 — Pamarco / Apex VIVA Trial Results（试车结果总表）

||||||||||
|---|---|---|---|---|---|---|---|---|
|1|Pamarco|VIVA Trial #1|12/3/24|DuPont Stain, Printed Side, 40X Zoom (scale 1000 µm)|1100|1800 OLU GMT|MISS|29|
|2|Control|IR Engraving Jenks GR2 (control)|12/3/25 (see D3: probable typo for 12/3/24)|DuPont Stain, Printed Side, 40X Zoom|not reported|—|control|29|
|3|Apex|VIVA Trial #1|2/12/25|DuPont Stain, Printed Side, 40X Zoom (scale 1 mm)|1550|1800 OLU GMT|MISS|30|
|4|Control|IR Engraving Jenks GR3 (control)|2/11/25|DuPont Stain, Printed Side, 40X Zoom|not reported|—|control|30|
|5|Apex|VIVA Trial #2|—|3D Scan #2 (30 lpi, 20 degrees) + 3× re-polish; endurance 24 hours|not reported|—|iteration, no GMT figure published|31|
|6|VENUS (vendor not named on slide)|Commercial Trial #6|—|DuPont Stain, Magnification ×12.8, scale bar 0.5 mm|not reported|—|no numeric result on slide|33|


Key structural observations [本报告推导]
- Both quantified VIVA trials used an identical target (1800) and an identical read-out (DuPont Stain, printed side, 40X), and both ran a control roll — the trial protocol is standardised; only the vendor engraving differs. This makes the 1100 vs 1550 gap attributable to vendor capability, not to method.
- Neither trial hit the target. Aggregate first-round attainment: 0 of 2.
- Apex out-delivered Pamarco by 450 GMT points, i.e. 1550 / 1100 = 1.409 → +40.9%.
- The two trials are 71 days apart (12/3/24 → 2/12/25) [本报告推导] — roughly 2.3 months of iteration for a +450 point gain; extrapolating the gap to target at the same cadence is a business risk, not a plan.

### T2 — GMT Attainment Derivation（达标率推导表）[本报告推导]

Formula: Attainment (%) = Measured GMT ÷ 1800 × 100
Shortfall: 1800 − Measured
Shortfall rate: (1800 − Measured) ÷ 1800 × 100

||||||||
|---|---|---|---|---|---|---|
|Pamarco (SLIDE 29)|1100|1800|61.1%1100 ÷ 1800 = 0.61111|700|38.9%700 ÷ 1800|−28.9 pts (fails)|
|Apex (SLIDE 30)|1550|1800|86.1%1550 ÷ 1800 = 0.86111|250|13.9%250 ÷ 1800|−3.9 pts (fails, marginally)|
|Delta (Apex − Pamarco)|+450|—|+25.0 pts0.86111 − 0.61111|−450|—|—|
|Ratio (Apex ÷ Pamarco)|1.409|—|—|—|—|—|


Derived readings
1. Best-in-chapter attainment is 86.1% — still below a 90% first-article gate.
2. The within-vendor spread (450 points) is 64% of the Apex shortfall (250 points) — i.e. choosing the wrong vendor costs more than the remaining gap of the better vendor. Vendor selection dominates residual design effort.
3. Required improvement to close: Pamarco 1800 ÷ 1100 = 1.636 → +63.6% GMT; Apex 1800 ÷ 1550 = 1.161 → +16.1% GMT.
4. Since cell diameter → GMT (SLIDE 35), the +16.1% / +63.6% gaps must be closed primarily by increasing coverage, i.e. moving toward larger-diameter / higher-coverage cells — which, per the pick-2 law (SLIDE 36), forces a compensating change in depth or volume.

### T3 — IR VENUS CT5 vs. Pamarco VENUS CT9: Engraving Defect Table（雕刻缺陷对比）

||||
|---|---|---|
|Verbatim annotation (SLIDE 34)|"Engraving – 1/3 of dot is still filled with ceramic "shelf""|"Dots are full circles and clean. No ceramic "shelf"."|
|Defect type|Residual ceramic occluding the cell (post-engraving removal failure)|None reported|
|Occlusion magnitude|≈ 33% of the dot area|0%|
|Cell shape|Not round / incomplete (implied by the contrast)|Complete round cells|
|Visual flagging on slide|Red circle drawn around the defect|No flag|
|Consequence in the deck's own words|"Struggled with low volumes" (SLIDE 34)|"Pamarco has shown promise with strong engraving plan and enforcement" (SLIDE 34)|
|Business outcome|Vendor dropped — "switched to Pamarco" (SLIDE 34)|Vendor retained and scaled|
|SLIDE|34 (left image)|34 (right image)|


Defect-mechanism reading [本报告推导]
- 1/3 ceramic occlusion does not mean 1/3 volume loss in a linear sense — for a cell of depth h, a residual shelf occupying the lower portion removes disproportionately more volume than its plan-view area suggests if the shelf sits at the mouth, and less if it sits at the floor. The deck gives no profile data, so the volume penalty is bounded but not quantified: 0 < ΔV/V < 1/3 is the only defensible interval without a cross-section [本报告推导]. What is defensible: a 1/3 occluded cell cannot deliver its design volume, and the deck's contemporaneous note is "low volumes".
- This is a first-article defect, not a wear defect. Ch2 SLIDE 12 sets the production sequence … Laser engraving → Final polishing, and Ch2 SLIDE 14 states Polishing is required to remove the corner peaks. A cell still holding ceramic at CT5 means the removal/polish operation under-performed — hence it is catchable before shipment, by inspection at the engraver's works.
- The control mechanism KC actually used was a visual microscope check with a red circle (SLIDE 34). That is a qualitative method. Module 5(3) proposes converting it into a quantified acceptance test.

### T4 — Trial Design & Evaluation Framework（试车设计与评估框架）

Sourcing rule: the deck does not contain a formal trial-design template. Cells labelled [未找到原句] are genuine gaps; cells labelled [本报告重构] are inferred from what the trials actually did.

|||||
|---|---|---|---|
|Objective — product property target|✔ Partial|1800 OLU GMT target; Z peel strength; bulk/caliper must not be degraded|29, 30, 35|
|Objective — volumetric target|✔|VENUS Target - 3,800,000 µm³ ± 5%; polish gate ≤ 10,700,000 Shallow Dot Volume Average (Ch3 SLIDE 28)|32; Ch3 28|
|Variables — roll (locked 2 of 3)|✔|volume / depth / diameter — "Can only specify 2"|36|
|Variables — pattern|✔|34.5 DPI, 1488 DOTS/SQ-IN, Shallow Dot 0.02" = 0.508mm, spacing 0.025926" / 0.051852" / 0.25926" / 0.14493"|32|
|Variables — vendor|✔|Harper → IR Engraving → Pamarco (+ Apex on VIVA)|34; Ch3 22|
|Variables — rework|✔|Re-Polish #1 / #2 / #3|31|
|Variables — run duration|✔|24 hours|31|
|Control group|✔|Incumbent-vendor control roll run side-by-side (GR2, GR3)|29, 30|
|Measures — numeric product|✔|GMT|29, 30|
|Measures — image|✔|DuPont Stain at 40X (VIVA) and ×12.8 (VENUS)|29, 30, 33|
|Measures — volumetric / geometric|✔|Capatch strips (BCM/in², cc/m²), Impression strips, 3DQC system, 3D Scan (µm)|37, 31|
|Explicit "objectives" statement|✘|[未找到原句] (0 occurrences)|—|
|Explicit "variables" statement|✘|[未找到原句] (0 occurrences); nearest = "key engraving parameters"|36|
|Explicit "robustness" criterion|✘|[未找到原句] (0 occurrences)|—|
|Statistical design (DOE, replicates, sample size)|✘|[未找到原句] — SLIDE 36's 9-band roll is a physical multi-level screen, but no replication or statistics are documented|—|
|Pre-registered pass/fail threshold|△|A target (1800) exists; no stated acceptance band (e.g. ±x%)|29, 30|
|Measurement-tool parity requirement|✔ (learned the hard way)|"Did not measure volume with same tools so none of the data translated"|34|


Framework reconstruction [本报告重构] — the 8-step loop the chapter actually describes:

- Fix the product CTQ and its numeric target (GMT 1800, Z-peel, bulk).
- Map CTQ → cell parameter (diameter → GMT; depth → Z-peel) — SLIDE 35.
- Lock 2 of 3 of {V, D, h} — SLIDE 36.
- Issue the drawing with full pattern detail (DPI, dots/sq-in, dot size, spacing, target volume ± tolerance) — SLIDE 32 / Ch2 SLIDE 21.
- Engrave; verify at the engraver's works by microscopy for ceramic residual — SLIDE 34.
- Run the trial against a control roll with the same measurement tools — SLIDE 29, 30, 34.
- Read out GMT + DuPont Stain + volumetric/topographic measurement; extend to 24 hours for endurance — SLIDE 29, 30, 31, 37.
- If short, re-polish and re-measure (up to 3× documented) or re-band the roll and repeat — SLIDE 31, 36.
### T5 — SLIDE 38 Summary: All Seven Points（Summary 七条全表）

Recovery note: these seven bullets exist only inside the slide image; the PPTX text layer for SLIDE 38 contains just Summary. Recovered by 260-dpi render read (see §0).

||||
|---|---|---|
|1|"Gravure rolls are engraved rolls that deliver a precise amount of fluid to a substrate"|Definition, carried verbatim from Ch1 SLIDE 2. The operative word is precise — the entire chapter is about the difficulty of achieving precision. Closes the deck by returning to first principles.|
|2|"GRs are critical to many of FCP's premium products"|Business framing: FCP (Family Care / Professional, KC's business segment) premium tier. Gravure rolls are not a commodity input; they are a premium-product enabler (cf. Ch1 SLIDE 4: "Enhanced properties create Premium products … Higher margins").|
|3|"Ceramic laser engraved rolls dominate the market"|Technology settling: Ch2 SLIDE 11 listed laser-ceramic pros (corrosion/abrasion resistance, longer life, flexibility, precision, vendor competition) vs. the single con (higher cost). Market has chosen the higher-cost option.|
|4|"Gravure roll design is an iterative process"|Direct echo of SLIDE 36. Placed in the summary → the author considers iteration the single most important process lesson of the deck.|
|5|"KC's engineered patterns create a tight engraving window"|The structural cause of all the difficulty. Cf. Ch2 SLIDE 20: "Engineered patterns … Outside the engravers comfort zones", "Deep engravings", "Large cells", "Large amount of unengraved area = more complex polishing". A tight window + a 2-of-3 DOF constraint = a very small feasible set.|
|6|"Product properties can change dramatically with engraving changes/inconsistencies"|The risk statement. Note the pairing: changes (deliberate design moves) and inconsistencies (unintended process noise) both move product properties — i.e. both the design lever and the capability problem are in scope.|
|7|"New vendors are learning with KC as we attempt to get back to healthy gravure roll inventories and look to ignite innovation"|The strategic close. Three claims in one sentence: (a) the vendor base is new / being trained — a capability-building programme, not a purchasing transaction; (b) inventories are currently unhealthy ("get back to" = restoring a prior good state); (c) the purpose of restoring inventory health is to unlock innovation capacity — a healthy spare position is what makes experimentation possible.|


Cross-check on bullet 7 [本报告推导]: "healthy inventories" is what allows trials at all, because Ch3 SLIDE 23 establishes the hard floor — Tissue machine can't run without 2 functional gravure rolls. With a 9-month worst-case engraving lead time (SLIDE 34) and 0 of 2 first-round GMT passes (T2), the spare float is consumed by failed engravings. Inventory health is therefore a direct function of first-article yield — see Module 5(4).

### T6 — Roll Maintenance / Cleaning / Refurbishment: Principle Checklist（辊维护 / 清洗 / 翻新原则清单）

Honesty banner: the deck contains no maintenance, cleaning, or refurbishment section — maintenance (0 hits), refurbish (0), roll cleaning (0). The table below therefore separates source-anchored principles from reported gaps.

|||||
|---|---|---|---|
|P1|Polishing is a mandatory, not optional, finishing step — it removes laser-induced corner peaks and prevents excessive doctor blade wear|Ch2 SLIDE 14: "Polishing is required to remove the corner peaks and eliminate excessive doctor blade wear"|✔ Verbatim|
|P2|Polishing is the last operation before the roll ships — so polish quality is as-delivered quality|Ch2 SLIDE 12: "… Laser engraving → Final polishing"|✔ Verbatim|
|P3|Post-polish volume is numerically gated, not left to judgement|Ch3 SLIDE 28: "POLISHING NOTE: Target <= 10,700,000 Shallow Dot Volume Average"|✔ Verbatim|
|P4|Cleanliness is defined positively, at the cell level, under magnification — clean = "full circles and clean", no ceramic residual|SLIDE 34: "Dots are full circles and clean. No ceramic "shelf"."|✔ Verbatim|
|P5|Re-polish is an adjustable, repeatable corrective action — up to 3 documented passes in one trial|SLIDE 31: "Re-Polish #1 / #2 / #3"|✔ Verbatim|
|P6|Rework must be verified by topography, not by appearance — each re-polish carries a 3D Scan with µm readings|SLIDE 31: "3D Scan #2 30 lpi, 20 degrees"; readings 649 / 627 / 729 / 697 / 896 / 187 µm|✔ Verbatim|
|P7|Three volumetric/topographic tool families are available for verification — Capatch (BCM/in² & cc/m²), Impression strips (footprint), 3DQC (3-D)|SLIDE 37|✔ Verbatim|
|P8|Units must be declared — BCM/in² vs cm³/m² (1 BCM/in² = 1.55 cm³/m²); LPI vs LCM (a "180" ambiguity worth a factor of ~2.56 in screen count)|Ch2 SLIDE 18, Ch2 SLIDE 17|✔ Verbatim|
|P9|Vendor and customer must use the same tools, or the data is worthless|SLIDE 34: "Did not measure volume with same tools so none of the data translated"|✔ Verbatim|
|P10|Re-polish consumes volume irreversibly — each pass removes material, so refurbishment cycles are finite and bounded by the volume window|[本报告推导] from P3 + P5 + SLIDE 32's ±5% window|○ Derived|
|G1|No documented in-service cleaning method, frequency, or chemistry|[未找到原句]|✘ Gap|
|G2|No documented plugged-cell inspection or threshold|[未找到原句] (plugged = 0 hits)|✘ Gap|
|G3|No documented doctor-blade change interval or wear limit|[未找到原句] (blade wear is mentioned only as a consequence of poor polishing, Ch2 SLIDE 14)|✘ Gap|
|G4|No documented ceramic re-coat / strip-and-re-spray refurbishment path|[未找到原句]|✘ Gap|
|G5|No numeric definition of "healthy inventory"|[未找到原句] (only the qualitative phrase on SLIDE 38)|✘ Gap|


### T7 (supplementary) — SLIDE 36 Banded Roll DOE Table（带状辊设计空间，支撑「pick 2」）

Derived quantities [本报告推导]; k = 5.1554 × 10⁻⁷ (least-squares fit of V = k·D²·h over the 9 bands, V in BCM, D & h in µm).

||||||||
|---|---|---|---|---|---|---|
|#9|530|6|35.78|5.18|−13.6%|Under-predicted|
|#8|530|7|43.14|6.25|−10.8%|Under-predicted|
|#7|590|5|31.42|5.64|+12.8%|Over-predicted|
|#6|590|6|32.95|5.91|−1.4%|Good fit|
|#5|590|7|38.71|6.95|−0.8%|Good fit|
|#4|590|8|41.99|7.54|−5.8%|Fair|
|#3|560|7|42.03|6.80|−2.9%|Good fit|
|#2|560|6|40.31|6.52|+8.6%|Over-predicted|
|#1|560|5|36.63|5.92|+18.4%|Worst fit|


Statistics [本报告推导]: residual 1σ ≈ 10.0%; error range −13.6% … +18.4%; free log-log fit V ∝ D^1.20 · h^1.25 gives R² = 0.672.

What this proves (and does not prove):
- ✔ The 2-of-3 constraint is a geometric identity — you cannot independently choose all three. This is tautologically true and needs no data.
- ✔ D and h both enter positively and with roughly comparable weight (fitted exponents 1.20 and 1.25), consistent with a volume-like quantity.
- ✘ The closure constant k is not known a priori to better than ~±10–18% on real rolls. With only 3 distinct diameters spanning 530–590 µm (an 11% range) and 9 points, R² = 0.672 → the two-parameter model explains only about two-thirds of the log-variance in volume.
- Therefore [本报告推导]: the ~10% prediction scatter exceeds the ±5% volume tolerance on the VENUS spec (SLIDE 32). This is the quantitative reason the deck calls design iterative and mandates banded screening and trial-and-measure rather than calculation. Specify 2; measure the 3rd; never calculate it and ship.

### T8 (supplementary) — SLIDE 32 VENUS Drawing: Spec Decode & Derived Volumes

|||||
|---|---|---|---|
|Drawing number|HC 110615901, XDI #2|—|32|
|Date / customer|10-16-2022 / Kimberly Clark|—|32|
|Roll face width|112"|—|32|
|Roll diameter|19.701"|—|32|
|Engraved area|104.5" wide, centred|= Σ of the 9 band widths on SLIDE 36 ✔|32, 36|
|Pattern|34.5 DPI, 1488 DOTS/SQ-IN|1 / 0.025926² = 1487.8 ≈ 1488 ✔ (supports the 0.025926" reading, see D2)|32|
|Dot spacing|0.025926" (H), 0.051852" (V row), 0.25926" (pattern height), 0.14493" (diagonal)|note 0.051852 = 2 × 0.025926|32|
|Shallow dot|0.02" = 0.508 mm|—|32|
|Target volume|3,800,000 µm³ ± 5%|—|32|
|→ Areal volume|—|3.8×10⁶ µm³ × 1488 /in² ÷ 10⁹ = 5.6544 BCM/in²|[本报告推导]|
|→ Metric equivalent|—|5.6544 × 1.55 = 8.764 cm³/m² (conversion per Ch2 SLIDE 18)|[本报告推导]|
|→ ±5% window|—|5.372 – 5.937 BCM/in² (8.33 – 9.20 cm³/m²)|[本报告推导]|
|→ Roll lateral area|—|π × 19.701" × 104.5" = 6,467.8 in²|[本报告推导]|
|→ Cells per roll|—|1488 × 6467.8 = ≈ 9.62 million cells|[本报告推导]|
|→ Fluid per revolution (full cells)|—|3.8×10⁶ µm³ × 9.624×10⁶ = 3.657×10¹³ µm³ = ≈ 36.6 cm³|[本报告推导]|


Utility: the 36.6 cm³/revolution figure is the practical bridge from cell geometry to fluid supply logistics (pump sizing, make-up system capacity, consumption forecasting) for anyone scoping a comparable functional-coating line. Marked [本报告推导] — the deck states no such figure.

## 模块4：章节间衔接（Chapter Connections）

### 4.1 — vs. Ch2 (Engraving & Specs, SLIDE 10–21): how the "pick 2" law explains why every trial missed

||||
|---|---|---|
|Three engraving specification primitives — "Cell dimensions (Cell diameter / Cell depth / Cell volume)" (Ch2 SLIDE 21)|Ch4 turns these three into a 2-of-3 constraint (SLIDE 36)|A spec that only pins volume — e.g. VENUS 3,800,000 µm³ ± 5% (SLIDE 32) — leaves diameter and depth both free. But GMT is driven by diameter (SLIDE 35) and Z-peel by depth (SLIDE 35). Volume conformance therefore does not constrain the product property at all. A roll can pass its volumetric spec and still miss GMT.|
|"BOTH '6 BCM VOLUME'" — 180 L/cm and 180 L/in are both "6 BCM" yet utterly different rolls (Ch2 SLIDE 17); 180 LCM = 460 LPI, 180 LPI = 70 LCM|Volume alone is geometrically ambiguous|Reinforces the same point from the screen-count side: "6 BCM" is not a specification. Ch4's answer is to add diameter + depth as the second locked parameter.|
|Laser physics — "Circular laser beam that creates ~10 µm round hole"; "each corner is exposed to the laser a minimum of 3 times"; "Raised peaks are created in the corners"; "Polishing is required to remove the corner peaks" (Ch2 SLIDE 14)|Explains the origin of the SLIDE 34 ceramic residual|The CT5 defect ("1/3 of dot is still filled with ceramic") is the failure mode of the mandatory polishing step that Ch2 SLIDE 14 prescribes. Ch2 predicts it; Ch4 photographs it.|
|Production sequence ends in polishing — … Laser engraving → Final polishing (Ch2 SLIDE 12)|Also explains Re-Polish #1/#2/#3 (SLIDE 31)|Re-polish is the same operation, applied correctively after delivery rather than preventively at the works.|
|"Outside the engravers comfort zones", "Deep engravings", "Large cells", "Large amount of unengraved area = more complex polishing" (Ch2 SLIDE 20)|KC's patterns sit at the edge of process capability|Predicts long lead times and vendor failures → Harper 9 months, IR low volumes, Pamarco "non-ideal engravings" (SLIDE 34).|
|"Engravers have no insight beyond the cell dimensions" (Ch2 SLIDE 20, notes)|KC must translate product CTQ → cell geometry itself|Explains why SLIDE 35 exists: it is the translation table (GMT←diameter; Z-peel←depth; bulk←penetration).|
|1 BCM/in² = 1.55 cm³/m² (Ch2 SLIDE 18)|Unit bridge|Enables the T8 derivation: VENUS = 5.6544 BCM/in² = 8.764 cm³/m².|


Synthesis [本报告推导]: Ch2 establishes what to specify (diameter, depth, volume; plus pattern details). Ch4 establishes that you may only specify two of them. The missed trials are the direct consequence: the VENUS drawing (SLIDE 32) locks volume (+ pattern), so diameter and depth float — and since GMT is a diameter-driven property, a volume-conforming roll has no guaranteed GMT. The missing link in the deck is a drawing that locks volume + diameter (or diameter + depth) for GMT-critical products.

### 4.2 — vs. Ch3 (Vendors & Patterns, SLIDE 22–28): vendor capability ↔ trial outcome

|||||
|---|---|---|---|
|Harper|Charlotte, NC|"took 9 months to engrave first roll and then had a large volume skew" (SLIDE 34)|Failed — lead time + uniformity|
|Precision Roll Solutions / IR Engraving|Richmond, VA|"Did not measure volume with same tools so none of the data translated"; "Struggled with low volumes"; ran a banded roll then "did not do a good job repeating the preferred engraving"; VENUS CT5 = "1/3 of dot is still filled with ceramic" (SLIDE 34). However: serves as the control roll engraver on both VIVA trials (GR2, GR3 — SLIDE 29, 30)|Failed as a development partner; retained as the control/benchmark incumbent|
|Pamarco|Atlanta, GA|Came on line Q3 2024 (SLIDE 32); VIVA Trial #1 = 1100 GMT (61.1%) (SLIDE 29); VENUS CT9 = "Dots are full circles and clean. No ceramic 'shelf'" (SLIDE 34); "shown promise with strong engraving plan and enforcement. Moving fast to meet pre-determined trial dates has created some non-ideal engravings" (SLIDE 34)|Best engraving quality, worst GMT result — quality ≠ hitting the product target|
|Apex|Pittsburgh, PA|VIVA Trial #1 = 1550 GMT (86.1%) (SLIDE 30); VIVA Trial #2 ran 24 hours with 3 re-polishes (SLIDE 31); also flagged in Ch2 SLIDE 13 notes: "Anilox vs Gravure and Apex Owner Discussion this week"|Best GMT result (still short of 1800); active development partner|


The counter-intuitive finding [本报告推导]: the vendor with the cleanest engraving (Pamarco, CT9, "full circles and clean") produced the worse GMT (1100), while Apex produced the better GMT (1550). Therefore:



Cell cleanliness is necessary but not sufficient. A perfectly formed cell that is the wrong diameter will not deliver GMT. Engraving-quality inspection (SLIDE 34) and product-property trials (SLIDE 29/30) are two different gates, and Ch4 shows they do not rank vendors the same way. Any vendor scorecard must score them separately.

Pattern/process context from Ch3 that constrains the trials:
- Ch3 SLIDE 26 (Jenks & BIL OLU process): Tissue Machine → Unwind → Printer Backing Roll → Gravure Roll → Pressure Roll → Air Layer → Print Fluid Delivery → Print Fluid Make-up System → Heated Hood → Crepe Dryer → Crepe Blade → Reel → Converting Line. Every trial variable must survive this whole chain — hence the 24-hour endurance run (SLIDE 31).
- Ch3 SLIDE 28 (OLU–VIVA pattern, HARPER, 8/30/23): 27 dpi dot; 2:1 dot spacing; rotated 19.6° from vertical; deep dot 0.032" × 0.022" ±10%; volume 27,600,000 µm³ (27.6 BCM); Flat Burn Target < ±10%; POLISHING NOTE: Target ≤ 10,700,000 Shallow Dot Volume Average.
- Scale contrast [本报告推导]: VIVA's 27.6 BCM vs VENUS's 5.6544 BCM/in² (T8) — roughly a 4.9× difference in areal volume, with VIVA using a much coarser 27 dpi vs VENUS's 34.5 DPI. The same supplier base is being asked to span both extremes, which is precisely Ch2 SLIDE 20's "outside the engravers comfort zones".

### 4.3 — vs. Ch1 (Fundamentals, SLIDE 1–9): coating form constrains the trial variable set

||||
|---|---|---|
|"Direct = gravure roll to substrate …… DRC and OLU" (SLIDE 5)|Direct|The roll touches the sheet. Therefore cell diameter → contact footprint → X–Y coverage → GMT, and cell depth → how much fluid is pushed into the sheet → Z penetration → peel strength. This is exactly SLIDE 35's mapping. All of Ch4's trials (VIVA, VENUS) are OLU = direct.|
|"Indirect = gravure roll to applicator roll to substrate …. Facial and Embossing winders" (SLIDE 5)|Indirect|The applicator roll is an intervening transfer step, so the mapping from cell geometry to sheet property is mediated by a second transfer efficiency. Trial variables must add applicator-roll hardness/nip/speed; the SLIDE 35 direct mapping cannot be assumed to transfer.|
|"OLU/DRC – Direct Gravure Coating" (SLIDE 6); Backing Roll + Gravure Roll + Doctor Blade Chamber|Direct|Fixed geometry: the nip between backing roll and gravure roll sets the contact patch — a process variable that does not exist in indirect coating.|
|"2 Ply Winder ELC = Indirect Gravure Coating" (SLIDE 7) — roll stack Embossing Roll / Marrying Roll / Applicator Roll / Gravure Roll / Steel & Rubber Calendar Rolls, plus Embossing Cleaning System|Indirect|Adds embossing + marrying steps between the roll and the finished 2-ply product.|
|"Facial OLP = Indirect Gravure Coating" (SLIDE 8) — DOCTOR CHAMBER → GRAVURE ROLL → RUBBER ROLL → WEB|Indirect|Fluid is metered onto a rubber roll first → release/transfer efficiency becomes a first-order variable.|
|"Gravure roll and anilox roll – pretty much the same thing. Gravure roll … direct to substrate and patterned. Anilox roll … more indirect and common/simple engraving" (SLIDE 2, notes)|Both|Naming convention only — the physics is shared, which is why the pick-2 law (derived from cell geometry) is platform-independent.|
|"Engraved roll that delivers a precise amount of fluid to a substrate" / "Heart of printing/coating process" (SLIDE 2)|Both|The word precise is the contract; Ch4 documents the cost of precision when the design window is tight.|
|"Enhanced properties create Premium products … Higher margins" (SLIDE 4)|Both|Justifies tolerating a multi-vendor, multi-year development programme (SLIDE 34) that has produced 0 of 2 GMT passes so far.|


Consolidated cross-chapter contrast table

||||||
|---|---|---|---|---|
|Question answered|Which coating architecture?|What defines an engraving?|Who can make it?|Does it hit the product target?|
|Unit of analysis|Line / roll stack|Cell|Vendor + pattern|Trial + sheet property|
|Key metric|Direct vs. Indirect|BCM, LPI, diameter/depth/volume|Lead time, pattern conformance|GMT vs. 1800; DuPont Stain; µm topography|
|Failure mode|Wrong architecture|Ambiguous spec ("6 BCM", "180")|Vendor can't hold the window|Roll passes volumetric spec but misses GMT|
|Constraint|Transfer path|3 parameters|Capability + lead time|Pick 2 of 3|
|Evidence type|Diagram|Definition + unit conversion|Drawings + process flow|Measured numbers + micrographs|


## 模块5：业务连接点（Business Connections）

Context: 卫材（纸尿裤 / 湿巾）创新研发 + 木浆与纸品战略采购.

### 5.1 — "Pick 2" is a universal coating/embossing design constraint (not a gravure curiosity)

Slides involved: SLIDE 36 (primary), SLIDE 35 (CTQ mapping), SLIDE 32 (spec), Ch2 SLIDE 21, Ch3 SLIDE 28.
Core concepts: volume / depth / diameter — pick 2; cell geometry DOF; banded screening (RSR not MSR).
Key data: 9 bands, 3 diameters (530 / 560 / 590 µm), 4 volumes (5 / 6 / 7 / 8 BCM), depths 31.42 – 43.14 µm; fitted V = 5.16×10⁻⁷ · D² · h with 1σ ≈ 10%; VENUS tolerance ±5%.

Mathematical essence [本报告推导]

For any repeating surface relief feature (gravure cell, embossing protuberance, anilox cell, lotion dot):

Free geometric variables:   D (in-plane size),  h (out-of-plane size)
Derived quantity:           V (void / displacement volume per feature)
Closure relation:           V = k · D² · h        [shape factor k, 0 < k < 1]
Dimensional check:          [L²] × [L] = [L³]  ✔
Degrees of freedom:         3 quantities (V, D, h) − 1 equation = 2

Therefore: at most 2 of {V, D, h} may be independently specified. Specify 3 → the system is over-determined → generally no physical solution → the engraver silently picks a compromise → the deck's own phrase for the result is "non-ideal engravings" (SLIDE 34). Specify 1 → infinitely many solutions → the vendor's default wins.

Why it is universal, not gravure-specific [本报告推导]: the relation V = k·D²·h is a geometric statement, not a process statement. It holds for:
- gravure / anilox cells (this deck),
- embossing patterns (D = protuberance footprint, h = embossing depth, V = displaced volume → governs softness/bulk),
- lotion / functional-coating dot deposition (D = dot footprint → skin contact area; h = dot height; V = dose delivered),
- adhesive pattern coating (D = bond spot size, h = bead height, V = adhesive add-on → bond strength vs. hand-feel),
- apertured / perforated films (D = hole diameter, h = film thickness, V = void volume → fluid acquisition rate).

Decision rule — "if you must pick, pick these two" [本报告建议]

||||||
|---|---|---|---|---|
|R1 (default)|Product CTQ is a mechanical / structural property (tensile, GMT, peel, softness, bulk)|Diameter + Depth|Volume|D and h are the primitives the laser controls and the ones with direct CTQ mapping (SLIDE 35: diameter→GMT, depth→Z-peel). Volume is the integral result → use it as the acceptance gate, not as a design input.|
|R2|Product CTQ is a dosing / add-on property (lotion laydown, adhesive add-on, active-agent dose, coating weight)|Volume + Diameter|Depth|Dose is set by V; footprint sets coverage/release. Depth then emerges — verify it against plugging/cleanability, because a deep narrow cell plugs and holds residue (see 5.3).|
|R3|Product CTQ is penetration / strike-through (acquisition, wipe wet-strength, barrier)|Volume + Depth|Diameter|Penetration needs depth and total dose; diameter becomes the screen-count consequence. Watch the bulk/caliper penalty flagged on SLIDE 35.|
|R4 (anti-pattern)|"We need all three"|—|—|Never specify all 3. Over-constraint removes the engraver's required DOF (SLIDE 36) and is the documented root cause of "non-ideal engravings" (SLIDE 34). Instead: specify 2, then run a banded roll to explore the third.|
|R5 (tie-break)|Two of the three map to CTQs and you can't decide|Use a banded roll (SLIDE 36): 9 candidate (D, V) combos on one roll, depths measured after|—|Resolves the trade-off empirically in one run instead of via argument. Accept the RSR (non-saleable) output penalty — it is far cheaper than sequential full rolls at up to 9 months each (SLIDE 34).|


Actionable recommendations
1. Rewrite every internal coating/embossing spec template to have exactly two locked lines — "LOCKED: ☐ volume ☐ depth ☐ diameter (choose 2)" — and a third line marked "DERIVED — measure, do not assume".
2. Add a CTQ→geometry translation row to each spec, in the SLIDE 35 style: target property → controlling cell parameter → locked value. Ch2 SLIDE 20 warns that "Engravers have no insight beyond the cell dimensions" — the supplier cannot do this translation for you.
3. Budget one banded roll per new platform. Nine bands at 11" each is a small material cost against a 9-month single-point lead time.
4. Set the derived-parameter tolerance from measured capability, not from wish. The VENUS ±5% window (SLIDE 32) is tighter than the ~10% 1σ scatter measured on SLIDE 36's own banded roll — a spec that the demonstrated process cannot hold. Renegotiate the tolerance or fund the capability improvement explicitly.

### 5.2 — GMT attainment as a supplier KPI, and writing first-article acceptance into the contract

Slides involved: SLIDE 29, 30 (measurements), SLIDE 35 (mapping), SLIDE 34 (vendor history), SLIDE 37 (tools), Ch2 SLIDE 17/18 (units).
Core concepts: GMT attainment rate; first-article acceptance; measurement-tool parity.
Key data: target 1800; Pamarco 1100 → 61.1%; Apex 1550 → 86.1%; gap to a 90% gate: −28.9 and −3.9 points; Apex/Pamarco ratio 1.409.

Why this belongs in a contract [本报告推导]: the deck shows that volumetric conformance and product conformance are different failure modes. VENUS's drawing locks 3,800,000 µm³ ± 5% (SLIDE 32), yet the VIVA trials failed on GMT, not on volume. If the contract only enforces the volumetric spec, the supplier can ship a conforming roll that misses the product target — and the buyer has no remedy.

Proposed KPI structure [本报告建议]

|||||
|---|---|---|---|
|First-Article GMT Attainment (FAGA)|measured GMT ÷ target GMT × 100%, measured on the first production-intent trial roll|61.1% (Pamarco), 86.1% (Apex)|≥ 90% = accept|
|Conditional acceptance band|—|—|85–89.9% = accept with a mandatory corrective-action plan and a funded 2nd article at vendor cost (Apex at 86.1% would sit here)|
|Rejection|—|—|< 85% = reject / re-engrave at vendor cost (Pamarco at 61.1% would sit here)|
|Volumetric conformance|measured BCM within the drawing window|window 5.372 – 5.937 BCM/in² for VENUS [本报告推导, T8]|100% of measurement fields inside window|
|Cell cleanliness (first article)|% of cells with any residual ceramic|IR CT5: 1/3 of dot occluded; Pamarco CT9: 0%|0% of fields showing occluded cells (see 5.3)|
|Measurement-tool parity|vendor and buyer read the same roll with the same instrument class, within an agreed inter-lab tolerance|Breached once: "Did not measure volume with same tools so none of the data translated" (SLIDE 34)|Mandatory: pre-contract round-robin on 3 reference rolls using Capatch / Impression / 3DQC (SLIDE 37)|
|Engrave lead time|PO → first article delivered|Harper 9 months|Contractual maximum with liquidated damages|
|Repeat-order reproducibility|Δvolume between successive rolls of the same spec|Harper: "large volume skew"; IR: "did not do a good job repeating the preferred engraving"|±x% roll-to-roll (set from capability study)|


Actionable recommendations
1. Insert a First-Article Acceptance clause with the three-band gate above (≥90 / 85–90 / <85). Use the deck's own 1800 target as the worked example in the clause so the mechanism is unambiguous.
2. Require the GMT test method to be fully specified in the contract — instrument, specimen preparation, MD/CD combination rule, units, and number of replicates. The deck never defines GMT [未找到原句]; leaving it undefined is the single largest contractual loophole in this chapter.
3. Mandate measurement-tool parity and a pre-award round-robin. Make the toolset explicit (Capatch strips for volume in BCM/in² and cc/m²; Impression strips for footprint; 3DQC for 3-D geometry — SLIDE 37) and state the conversion (1 BCM/in² = 1.55 cm³/m², Ch2 SLIDE 18).
4. Ban unit-ambiguous specs. Every screen-count figure must carry its unit; require both LPI and LCM on the drawing. Ch2 SLIDE 17's 180 LCM = 460 LPI vs 180 LPI = 70 LCM is a documented, expensive ambiguity (~2.56× in screen count).
5. Score vendors on two independent axes — engraving quality (cell cleanliness/roundness, SLIDE 34) and product attainment (GMT, SLIDE 29/30). Ch4 proves these rank differently: Pamarco wins on cleanliness (CT9) and loses on GMT (1100); Apex wins on GMT (1550).

### 5.3 — Ceramic residual in cells is a post-engraving cleaning defect: add an incoming-acceptance inspection

Slides involved: SLIDE 34 (primary defect evidence), SLIDE 31 (re-polish as the corrective), Ch2 SLIDE 12 + 14 (process origin), SLIDE 37 (verification tools), SLIDE 29/30/33 (microscopy magnifications in use).
Core concepts: ceramic residual ("shelf"/"shell"); round-cell criterion; re-polish; plugged cells.
Key data: IR VENUS CT5 = 1/3 of dot still filled with ceramic; Pamarco CT9 = "Dots are full circles and clean"; microscopy protocols already in use at 40X (VIVA) and ×12.8 (VENUS).

Defect classification [本报告推导]

|||
|---|---|
|Where it is created|At the engraver's works, in the laser engraving → final polishing sequence (Ch2 SLIDE 12)|
|Why|Incomplete removal of laser-recast / redeposited ceramic; Ch2 SLIDE 14 establishes that polishing is the removal operation and is mandatory|
|When it is detectable|Before shipment — it is present at first article|
|Symptom downstream|Reduced effective cell volume; the deck's contemporaneous note is "Struggled with low volumes" (SLIDE 34)|
|Corrective action|Re-polish (SLIDE 31 documents up to 3 passes) — i.e. rework, at the cost of irreversibly consumed volume|
|Is it wear?|No. Nothing in the deck attributes it to service. [未找到原句] for any in-service plugging data|


Proposed incoming-acceptance inspection [本报告建议 — all thresholds are proposed, NOT sourced from the deck]

||||
|---|---|---|
|Method|Optical/digital microscopy of the as-engraved roll surface (or a roll-face replica), minimum 40X — matching the magnification already used for trial read-outs|SLIDE 29, 30 (40X Zoom); SLIDE 34 (defect found visually and circled)|
|Sampling across the face|Minimum 1 field per engraved band, plus 1 field in each end burn area. For a VENUS-class roll (104.5" engraved face, SLIDE 32) → propose ≥ 10 fields evenly spaced across the face + 2 end fields|SLIDE 32; Ch3 SLIDE 28 (Top Burn Area 3.5" Max Both Ends)|
|Sampling depth (circumferential)|≥ 3 angular positions (e.g. 0° / 120° / 240°) per band, to catch periodic laser-bed errors|[本报告建议]|
|Primary criterion|0% of cells in any field showing any residual ceramic. Positive reference wording: "full circles and clean"|SLIDE 34 (Pamarco CT9 wording adopted verbatim as the accept criterion)|
|Action limit|Any single field with > 1% of dots occluded → 100% re-inspection of that band|[本报告建议]; scaled from the observed 1/3 occlusion failure|
|Reject limit|Any field with a cell occluded by ≥ 1/3 of its dot area → reject the roll, return for re-polish|SLIDE 34 (the documented reject-level defect)|
|Corroborating volumetric check|Measured areal volume must fall inside the drawing window — for VENUS, 5.372 – 5.937 BCM/in² [本报告推导, T8]|SLIDE 32 (±5%); Ch2 SLIDE 18 (conversion)|
|Corroborating functional check|DuPont Stain coverage image at the trial stage; 3DQC or 3D Scan topography for µm-level cell geometry|SLIDE 29/30/33; SLIDE 37; SLIDE 31|
|Cleanliness at re-polish|After any re-polish, repeat the full inspection. Track the cumulative re-polish count per roll serial number|SLIDE 31 (Re-Polish #1/#2/#3); Ch3 SLIDE 28 (polish volume gate)|
|Record|Photograph + field ID + occlusion % per field, retained against the roll serial|[本报告建议]|


Actionable recommendations
1. Make cell-level microscopy a contractual incoming-inspection item, not a development-stage courtesy. The deck already does this check informally (a red circle on SLIDE 34); formalise it with a sampling plan and a written criterion.
2. Adopt "full circles and clean" (SLIDE 34) as the literal accept criterion — it is the deck's own positive definition of a clean cell, so it is defensible in a supplier dispute.
3. Correlate occlusion to volume. Require the supplier to report occlusion % and measured BCM together, so the buyer builds its own occlusion→volume-loss curve. (The deck gives only the bound 0 < ΔV/V < 1/3 [本报告推导] — do not accept a vendor-supplied conversion factor without data.)
4. Log re-polish cycles per roll serial and cap them. Each pass removes material (P10, T6); the polish volume gate on Ch3 SLIDE 28 (≤ 10,700,000 Shallow Dot Volume Average) shows the deck already polices a post-polish bound. A roll that reaches its cap is scrap — plan replacement before that point, not after.

### 5.4 — Roll inventory health = capacity continuity

Slides involved: SLIDE 38 bullet 7 (primary), SLIDE 34 (lead time), SLIDE 32 (3 vendors, Q3 2024), SLIDE 29/30/31/33 (trial consumption), Ch3 SLIDE 23 (hard floor), Ch3 SLIDE 22 (4 vendors), Ch3 SLIDE 26 (OLU line).
Core concepts: healthy roll inventory; functional-roll floor; lead time; refurbishment cycle; first-article yield.
Key data: "get back to healthy gravure roll inventories" (SLIDE 38); "Tissue machine can't run without 2 functional gravure rolls" (Ch3 SLIDE 23); Harper 9 months to first roll (SLIDE 34); Pamarco online Q3 2024 (SLIDE 32); 3 vendors struggled on VENUS (SLIDE 32); 4 vendors named (Ch3 SLIDE 22); 0 of 2 first-round GMT passes (T2); ≥ 6 engraving/trial events documented in Ch4.

Reverse-engineering KC's spare policy [本报告推导]

Hard floor (Ch3 SLIDE 23):            ≥ 2 functional rolls per tissue machine
                                      → 1 running + ≥ 1 spare, minimum

Worst-case replenishment lead time:   9 months  (Harper, SLIDE 34)
Observed first-article yield:          0 of 2 trials met the GMT target (T2)
                                      → a replacement roll is NOT guaranteed on the
                                        first attempt; each failed article costs a
                                        full engrave cycle

Required float  ≈  (running rolls) + (spares to cover lead time × failure rate)
                ≥  1 running + 1 statutory spare + (buffer for failed first articles)

What "unhealthy" looks like, structurally [本报告推导]: inventory health is not a count of rolls owned — it is a count of rolls at specification. Ch4 documents a chain in which the float is consumed by failed but engraved rolls: Harper (9 months, volume skew) → IR (low volumes, failed banded repeat, CT5 ceramic defect) → Pamarco (clean cells, 1100 GMT) → Apex (1550 GMT, then a 24-hour trial with 3 re-polishes). Every one of these consumed calendar time and machine time. With a 9-month worst-case engrave cycle and a 0-of-2 first-pass rate, the programme is structurally incapable of rebuilding inventory quickly — which is exactly why SLIDE 38 says "get back to" rather than "maintain".

Spare-policy parameters to extract from the deck and set for our own operation

||||
|---|---|---|
|Functional rolls per line (floor)|2 (Ch3 SLIDE 23)|≥ 2 for any line that cannot be stopped; 3 where the roll is a premium-product enabler (SLIDE 38 bullet 2 / Ch1 SLIDE 4)|
|Qualified vendors per pattern|4 named (Ch3 SLIDE 22); 3 failed on VENUS before 1 succeeded (SLIDE 32)|Dual-source minimum for every critical pattern; qualify the second source before the first is needed|
|Engrave lead time to plan against|up to 9 months (SLIDE 34)|Plan at 9 months for a new pattern; ≤ 3 months for a repeat of a proven spec (contractual)|
|Refurbishment / re-polish turnaround|not stated; 3 re-polish iterations occurred inside a single trial (SLIDE 31) [未找到原句 for turnaround days]|Contract a turnaround SLA per re-polish; track cycles-to-scrap per roll serial|
|Endurance validation before a roll counts as "healthy"|24 hours continuous run (SLIDE 31)|Require ≥ 24 h run + full volumetric re-verification before a roll graduates from "spare" to "qualified spare"|
|Inventory-health metric|no numeric definition given [未找到原句]|ConformingRolls ÷ RequiredRolls, reported monthly, with a red flag below 1.0|
|Innovation buffer|healthy inventory is what lets KC "ignite innovation" (SLIDE 38)|Hold +1 roll beyond the operational floor specifically as the trial/development float — otherwise trials cannibalise production spares|


Actionable recommendations
1. Reclassify gravure/anilox rolls from "consumable" to "long-lead capital spare" in the procurement master — a 9-month lead time and a 0-of-2 first-pass yield are capital-spare characteristics, not consumable ones.
2. Never single-source a critical pattern. Ch3 SLIDE 22 shows four qualified-capable vendors, yet VENUS burned through three before succeeding. Dual-qualify, and keep the second source warm (periodic small orders) so it is not cold when needed.
3. Define inventory health in conforming units, and report it. "We own 6 rolls" is meaningless if 4 are off-spec. Metric: conforming rolls ÷ required rolls.
4. Contract the lead time and the re-polish turnaround, with liquidated damages. The 9-month Harper figure is the negotiation anchor.
5. Fund an explicit innovation float (+1 roll above the operational floor). SLIDE 38 ties inventory health directly to the ability to "ignite innovation" — starving spares is what freezes the development pipeline.
6. Link first-article yield to inventory planning. Every failed first article costs a full engrave cycle; at a 9-month cycle, a 61.1% attainment vendor cannot sustain a 2-roll floor. Yield is inventory.

### 5.5 — If we introduce functional coating: recommended trial variable checklist

Slides involved: SLIDE 36 (pick 2), SLIDE 35 (CTQ mapping), SLIDE 32 (spec template), SLIDE 29/30 (control design), SLIDE 31 (endurance + rework), SLIDE 37 (measurement), Ch2 SLIDE 16/17/18/21, Ch3 SLIDE 26/28.
Core concepts: locked vs. derived parameters; CTQ→geometry translation; control roll; measurement parity; endurance.

A. Variables to LOCK (exactly 2 of the three, per SLIDE 36)

|||||
|---|---|---|---|
|L1|Cell volume (BCM/in², cc/m²)|Ch2 SLIDE 18; SLIDE 32|Sets the dose — the primary lever for lotion/actives/binder add-on|
|L2|Cell diameter (µm)|SLIDE 35, 36|Sets coverage / contact footprint → GMT, bond area, skincontact area|
|L3|Cell depth (µm)|SLIDE 35, 36|Sets Z penetration → peel strength, strike-through; penalises bulk/caliper (SLIDE 35)|
|—|⚠ Lock exactly two|SLIDE 36|Locking all three removes the engraver's required 1 DOF → "non-ideal engravings" (SLIDE 34)|


B. Pattern variables (all lockable — they are not part of the 2-of-3 constraint)

||||
|---|---|---|
|P1|Screen count with unit — DPI / LPI / LCM, never a bare number|SLIDE 32 (34.5 DPI); Ch2 SLIDE 17 (180 LCM = 460 LPI; 180 LPI = 70 LCM)|
|P2|Dots per unit area|SLIDE 32 (1488 DOTS/SQ-IN)|
|P3|Dot / cell spacing & row spacing|SLIDE 32 (0.025926" H, 0.051852" V)|
|P4|Pattern rotation angle|Ch3 SLIDE 28 (rotated 19.6° from vertical)|
|P5|Cell geometry / shape class|Ch2 SLIDE 13 (60° Hex, GTT, 45°, Longcell, Channellox, Trihelical); Ch2 SLIDE 16 (60 degree hex, 180 LPI, 6.0 BCM)|
|P6|Dot aspect ratio|Ch3 SLIDE 28 (deep dot 0.032" × 0.022" ±10%)|
|P7|Engraved face width & end burn areas|SLIDE 32 (104.5"); Ch3 SLIDE 28 (Top Burn Area 3.5" Max Both Ends)|
|P8|Shallow-dot size & polish volume gate|SLIDE 32 (0.02" = 0.508mm); Ch3 SLIDE 28 (≤ 10,700,000)|


C. Coating-architectecture variables (from Ch1)

||||
|---|---|---|
|A1|Direct vs. Indirect — this single choice changes whether SLIDE 35's CTQ mapping applies|Ch1 SLIDE 5, 6, 7, 8|
|A2|Roll stack / nip configuration|Ch1 SLIDE 6 (Backing + Gravure + Doctor Blade Chamber); Ch1 SLIDE 7 (ELC stack); Ch1 SLIDE 8 (Facial OLP)|
|A3|Doctor blade chamber condition (metering + containment blades)|Ch1 SLIDE 9|
|A4|Fluid delivery & make-up system|Ch3 SLIDE 26|


D. Process variables (must be held constant or deliberately varied — no deck data, [未找到原句], listed as required-by-discipline [本报告建议])

Line speed · nip pressure · web tension · fluid solids / viscosity / temperature · drying & cure energy (Heated Hood, Crepe Dryer, Ch3 SLIDE 26) · run duration (≥ 24 h, SLIDE 31) · substrate (basesheet lot, basis weight, moisture) · ambient conditions.

E. Measures (the read-out set the deck actually uses + the additions we recommend)

|||||
|---|---|---|---|
|M1|GMT (numeric, vs. target)|Mechanical tensile testing; method to be contractually defined|SLIDE 29, 30, 35|
|M2|DuPont Stain coverage (image)|Stain + microscopy at 40X (VIVA) / ×12.8 (VENUS)|SLIDE 29, 30, 33|
|M3|Z peel strength|Peel test|SLIDE 35|
|M4|Bulk / caliper|Caliper / bulk test|SLIDE 35|
|M5|Areal cell volume|Capatch strips (reads BCM/in² and cc/m²)|SLIDE 37|
|M6|Contact footprint / impression|Impression strips (2.0 mil / 20–50 µm)|SLIDE 37|
|M7|3-D cell geometry|3DQC system (MicroDynamics Model 3DQC)|SLIDE 37|
|M8|Cell topography / depths|3D Scan (30 lpi, 20 degrees, µm readouts)|SLIDE 31|
|M9|Cell cleanliness / roundness|Microscopy ≥ 40X; criterion "full circles and clean"|SLIDE 34|
|M10|Across-face uniformity|Flat Burn Target < ±10%|Ch3 SLIDE 28|
|M11|Add-on / coat weight|Gravimetric|[本报告建议]|


F. Trial-design controls (non-negotiable, all sourced)

||||
|---|---|---|
|F1|Run a control roll of the incumbent engraving side-by-side|SLIDE 29, 30 (Control IR Engraving Jenks GR2 / GR3)|
|F2|Use identical measurement tools on both sides, or the data will not translate|SLIDE 34|
|F3|State units on every parameter (BCM/in² vs cm³/m²; LPI vs LCM)|Ch2 SLIDE 17, 18|
|F4|Run ≥ 24 hours before declaring a result|SLIDE 31|
|F5|Screen with a banded roll when the 2-of-3 trade-off is unresolved; accept RSR (non-saleable) output|SLIDE 36|
|F6|Iterate via re-polish with topographic re-verification, not by eye|SLIDE 31|
|F7|Record the vendor's engraving plan and enforce it — and accept that compressing to pre-set trial dates produces non-ideal engravings|SLIDE 34|


### 5.6 — Data list ready for R&D / procurement decisions（可直接用于研发/采购决策的数据清单）

|||||||
|---|---|---|---|---|---|
|1|OLU GMT target|1800|SLIDE 29, 30|—|The acceptance target in any GMT clause|
|2|Pamarco VIVA Trial #1 GMT|1100 (61.1% of target)|SLIDE 29|derivation|Vendor scorecard / FAGA KPI baseline|
|3|Apex VIVA Trial #1 GMT|1550 (86.1% of target)|SLIDE 30|derivation|Vendor scorecard / FAGA KPI baseline|
|4|First-round pass rate|0 of 2|SLIDE 29, 30|derivation|Inventory float sizing; lead-time risk|
|5|Apex vs Pamarco uplift|+450 points, ratio 1.409, +40.9%|SLIDE 29, 30|✔ derivation|Vendor selection dominates residual design effort|
|6|Required uplift to hit target|Pamarco +63.6%; Apex +16.1%|SLIDE 29, 30|✔ derivation|Development effort sizing|
|7|Trial-to-trial elapsed time|71 days (12/3/24 → 2/12/25)|SLIDE 29, 30|✔ derivation|Iteration cadence / project timeline|
|8|Endurance run length|24 hours|SLIDE 31|—|Validation gate before a roll counts as qualified|
|9|Re-polish iterations in one trial|3 (#1/#2/#3)|SLIDE 31|—|Rework allowance in cost & schedule|
|10|Ceramic residual defect level|1/3 of dot occluded (IR CT5) vs 0% (Pamarco CT9)|SLIDE 34|—|Incoming-acceptance reject limit|
|11|Microscopy magnification in use|40X (VIVA trials), ×12.8 (VENUS CT6)|SLIDE 29, 30, 33|—|Inspection method specification|
|12|Worst-case engrave lead time|9 months (Harper, first roll)|SLIDE 34|—|Lead-time planning & spares sizing|
|13|Vendors failed on VENUS before success|3|SLIDE 32|—|Dual-sourcing justification|
|14|Vendors named / available|4 (Harper–Charlotte NC; Precision Roll Solutions/IR–Richmond VA; Pamarco–Atlanta GA; Apex–Pittsburgh PA)|Ch3 SLIDE 22|—|Supplier long-list|
|15|Pamarco online date|Q3 2024|SLIDE 32|—|Vendor maturity assessment|
|16|Functional roll floor per machine|2|Ch3 SLIDE 23|—|Spare-policy floor|
|17|VENUS target volume|3,800,000 µm³ ± 5%|SLIDE 32|—|Volumetric spec template|
|18|VENUS pattern density|34.5 DPI, 1488 DOTS/SQ-IN|SLIDE 32|—|Pattern spec template|
|19|VENUS areal volume|5.6544 BCM/in² = 8.764 cm³/m²; window 5.372 – 5.937 BCM/in²|SLIDE 32 + Ch2 SLIDE 18|✔ derivation|Cross-unit spec checking|
|20|VENUS roll geometry|face 112", diameter 19.701", engraved 104.5"; lateral area 6,467.8 in²; ≈ 9.62 M cells; ≈ 36.6 cm³ fluid/revolution|SLIDE 32|✔ derivation|Pump sizing, consumption forecasting|
|21|VIVA areal volume (contrast)|27.6 BCM (27 dpi, rotated 19.6°, deep dot 0.032"×0.022")|Ch3 SLIDE 28|—|Capability-range envelope|
|22|VENUS vs VIVA volume ratio|≈ 4.9×|SLIDE 32 + Ch3 SLIDE 28|✔ derivation|Shows the capability span demanded of one supply base|
|23|Pick-2 design closure|V = k·D²·h, k ≈ 5.16×10⁻⁷, 1σ ≈ 10%, errors −13.6%…+18.4%|SLIDE 36 bands|✔ derivation|Proves the 3rd parameter must be measured, not calculated|
|24|Banded-roll DOE structure|9 bands, 3 diameters (530/560/590 µm), 4 volumes (5/6/7/8 BCM), depths 31.42–43.14 µm; Σwidths = 104.5"|SLIDE 36|✔ validation|Screening-roll template|
|25|Tolerance vs demonstrated scatter|spec ±5% vs measured ~10% 1σ|SLIDE 32 + 36|✔ derivation|Renegotiate the tolerance or fund capability|
|26|Polish volume gate|≤ 10,700,000 shallow-dot volume average|Ch3 SLIDE 28|—|Post-polish acceptance item|
|27|Across-face uniformity target|Flat Burn < ±10%|Ch3 SLIDE 28|—|Uniformity acceptance item|
|28|Unit conversion|1 BCM/in² = 1.55 cm³/m²|Ch2 SLIDE 18|—|Contract boilerplate|
|29|Screen-count hazard|180 LCM = 460 LPI; 180 LPI = 70 LCM; both are "6 BCM"|Ch2 SLIDE 17|—|Ban bare screen-count numbers|
|30|Measurement toolset|Capatch strips / Impression strips / 3DQC system|SLIDE 37|—|Tool-parity clause|
|31|Tool-parity failure|"Did not measure volume with same tools so none of the data translated"|SLIDE 34|—|Mandatory pre-award round-robin|
|32|GMT acronym expansion|never expanded anywhere in the deck|—|[未找到原句]|Loophole to close in the contract|
|33|Terms absent from the deck|maintenance, refurbishment, roll cleaning, plugged cells, robustness, objectives, variables, numeric healthy inventory|—|[未找到原句]|Must be invented and written into our own standards|


## 模块6：金句索引（Key Quotes Index）

||||||
|---|---|---|---|---|
|1|"Engraver must have at least 1 degree of freedom.  Can only specify 2 from the key engraving parameters of volume, depth, and diameter"|36|「雕刻商必须至少保留 1 个自由度。在容积、深度、直径这三项关键雕刻参数中，你只能指定其中 2 项。」|全章、乃至全套材料最重要的一句。它不是经验谈，而是几何恒等式：3 个量 − 1 个约束 = 2 个自由度。所有涂布/压花/点胶设计都适用。任何写下三个参数的技术规格都是过度约束。|
|2|"Same volume from different combinations of diameter vs depth"|36|「相同的容积，可以由不同的直径与深度组合得到。」|解释了为什么"容积合格"不等于"产品合格"——同一 BCM 值对应无穷多种细胞形貌，而直径与深度分别驱动不同的产品性能。这是把容积写进技术规格却仍然失标的根本原因。|
|3|"1100 GMT vs 1800 OLU GMT Target"|29|「1100 GMT，对照 1800 的 OLU GMT 目标。」|全章最刺眼的数字：61.1% 达标率。用最干净、最圆整的网穴（Pamarco CT9）换来最差的产品结果——证明"雕刻质量"与"产品达成"是两道独立的门。|
|4|"1550 GMT vs 1800 OLU GMT Target"|30|「1550 GMT，对照 1800 的 OLU GMT 目标。」|86.1% 达标率——本章最好成绩，仍然不达标。它是"首件达标率 ≥90%"这条 KPI 的现实校准点：连最好的供应商都差 3.9 个百分点。|
|5|"Engraving – 1/3 of dot is still filled with ceramic "shelf"" (pre-extracted supplement renders this word as "shell")|34|「雕刻——网穴（网点）仍有 1/3 被陶瓷"壳/残留物"填满。」|陶瓷残留缺陷的唯一量化证据：1/3。它锚定了来料验收的拒收限。更重要的是它的性质——来自 Ch2 SLIDE 12/14 的"激光雕刻 → 最终抛光"工序，说明这是出厂前就该拦下的来料缺陷，不是使用磨损。|
|6|"Dots are full circles and clean. No ceramic "shelf"."|34|「网点是完整、干净的圆形。无陶瓷残留。」|全章唯一的正向洁净判据。可直接改写为验收标准原文——在供应商争议中，这是最站得住脚的一句定义。|
|7|"Gravure roll design is an iterative process"|36|「凹版辊设计是一个迭代过程。」|这句话被作者原样搬进了 SLIDE 38 的 Summary（第 4 条），说明作者本人认为它是全套材料最重要的流程教训。它也是把"试车"写进项目计划与预算的依据。|
|8|"New vendors are learning with KC as we attempt to get back to healthy gravure roll inventories and look to ignite innovation"|38|「新供应商正在与 KC 共同学习，我们正努力恢复健康的凹版辊库存，并以此点燃创新。」|全章的战略落点。一句话里三个信息：供应商在受训（能力建设项目，不是采购交易）；库存当前不健康（"get back to"是恢复此前的好状态）；恢复库存的目的是释放创新产能。把备件管理从成本项提升为创新前提。|
|9|"Product properties can change dramatically with engraving changes/inconsistencies"|38|「产品性能会随雕刻的变化或不一致性而发生剧烈改变。」|注意并列的两类原因：changes（有意的设计改动）与 inconsistencies（无意的工序波动）。两者都会撼动产品性能——意味着设计杠杆与制程能力同为风险源，供应商审核必须同时覆盖。|
|10|"KC's engineered patterns create a tight engraving window"|38|「KC 的工程化图案造就了很窄的雕刻窗口。」|所有困难的结构性成因。配合 Ch2 SLIDE 20（"Engineered patterns … Outside the engravers comfort zones"、"Deep engravings"、"Large cells"）：窗口窄 + 只能锁两个参数 = 可行解集合极小。这是供应商能力与交付周期的定价依据。|
|11|"Tissue machine can't run without 2 functional gravure rolls"|Ch3 23|「没有 2 支可用的凹版辊，纸机就开不起来。」|唯一的硬下限数字。叠加 SLIDE 34 的 9 个月交期与 T2 的 0/2 首件通过率，就推导出备辊策略：1 运行 + ≥1 法定备件 + 首件失败缓冲。|
|12|"Harper took 9 months to engrave first roll and then had a large volume skew"|34|「Harper 花了 9 个月才雕出第一支辊，而且容积偏差很大。」|9 个月是交期谈判的锚点，也是"长周期资本备件"分类的依据。同时说明：长交期并不换来一致性。|
|13|"Did not measure volume with same tools so none of the data translated"|34|「由于没有用同一套工具测量容积，所有数据都无法互相换算。」|最贵的一句教训。一次工具不一致，让整段供应商开发的数据全部作废。这是必须在合同里写成量具一致性条款 + 授标前循环比对的依据。|
|14|"Pamarco has shown promise with strong engraving plan and enforcement. Moving fast to meet pre-determined trial dates has created some non-ideal engravings"|34|「Pamarco 展现出潜力，雕刻计划与执行都很有力。但为了赶在预设试车日期前完成而推进过快，产生了一些不理想的雕刻。」|罕见的自我批评式经验：把试车日期排在雕刻能力之前，会直接制造缺陷。可用于反对"倒排工期"式的新品开发节奏。|
|15|"X and Y direction sheet surface coverage - Key to GMT (Cell diameter) / Z direction sheet penetration - Key to VIVA/WypAll Z peel strength (Cell depth) / High Z direction penetration can also negatively impact bulk/caliper"|35|「X、Y 方向的片材表面覆盖——是 GMT 的关键（细胞直径）；Z 方向的片材渗透——是 VIVA/WypAll Z 向剥离强度的关键（细胞深度）；过高的 Z 向渗透还会对蓬松度/厚度产生负面影响。」|全套材料唯一的产品性能 ↔ 细胞几何 翻译表。没有它，供应商根本无从选择锁哪两个参数——Ch2 SLIDE 20 明说"雕刻商对细胞尺寸之外一无所知"。做任何功能涂布，第一件事就是建立自己的这张表。|
|16|"Banded gravure rolls can help speed up the iterative process – typically don't produce sellable product – RSR not MSR"|36|「带状凹版辊可以加快迭代过程——但通常不产出可销售产品——是 RSR 而非 MSR。」|给出了"如何解决只能锁两个"的实操答案：用一支辊同时试 9 组组合（SLIDE 36），代价是产出不可销售（RSR）。用一支辊的料损，换掉 9 个月的串行试错。|
|17|"Gravure rolls are engraved rolls that deliver a precise amount of fluid to a substrate"|38|「凹版辊是向基材输送精确液量的雕刻辊。」|Summary 第 1 条，与 Ch1 SLIDE 2 逐字相同——全套材料首尾呼应。关键词是 precise（精确）：整章讲的都是"精确"这四个字有多贵。|
|18|"Ceramic laser engraved rolls dominate the market"|38|「陶瓷激光雕刻辊主导市场。」|技术路线的定论。Ch2 SLIDE 11 曾列出它唯一的缺点是"成本更高"——市场仍然选了它。采购谈判中不要试图用铬辊降本来替换。|


## 附：本报告的方法论声明（Academic Integrity Statement）

- Every claim in Modules 1–5 is tagged SLIDE N (source-backed) or [本报告推导] (derived, with the arithmetic shown) or [本报告建议] (recommendation with no source) or [未找到原句] (term/concept absent from the deck).
- No data was invented. All 33 items in the Module 5.6 data list trace to a slide number or are explicitly flagged as derived with the formula shown.
- Two source discrepancies were found and recorded rather than silently resolved (D1: shelf/shell; D2: SLIDE 32 dot-array dimensions), plus one probable typo (D3: SLIDE 29 control date).
- SLIDE 38's seven Summary bullets were recovered by re-rendering the PPTX, because they exist only inside the slide image and the pre-extracted supplement incorrectly directed readers to the text layer.
- The GMT acronym is not expanded anywhere in the deck. This report offers Geometric Mean Tensile as [本报告推断，最可能] with the reasoning shown, and explicitly warns against contractualising GMT without obtaining the test method in writing.
- Eight required concept areas are absent from the source and are declared as gaps rather than filled with plausible content: maintenance, refurbishment, roll cleaning, plugged cells, robustness, explicit objectives/variables, and any numeric definition of "healthy inventory". These are the areas where our own standards must be written from scratch.
- Verification arithmetic is reproducible: band-width summation (= 104.5", matching SLIDE 32), VENUS areal volume (3.8×10⁶ × 1488 ÷ 10⁹ = 5.6544 BCM/in²), unit conversion (× 1.55 = 8.764 cm³/m²), GMT attainment (1100/1800, 1550/1800), and the V = k·D²·h least-squares fit over the 9 SLIDE 36 bands.


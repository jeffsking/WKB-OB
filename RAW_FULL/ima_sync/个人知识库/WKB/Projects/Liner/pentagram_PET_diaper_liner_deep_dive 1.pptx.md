---
media_id: "ppt_3867e2b60070d7dc3f413086d0b0036e_66762e83f836c52c0d8b048161a34cff001a693ee6c0644e"
source_file: "pentagram_PET_diaper_liner_deep_dive 1.pptx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Projects/Liner/pentagram_PET_diaper_liner_deep_dive 1.pptx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# pentagram_PET_diaper_liner_deep_dive 1.pptx.md

8
# Pentagram PET Fiber Add-on for 25 gsm Air-through Bonded Diaper Liner

Simulation, formulation recommendation, process window, and validation plan for a 2-card PE/PET ES topsheet

Recommended starting point: 10% total add-on, 3D pentagram PET, lower card only

[图片: 5 open grooves = capillary rails]
5 open grooves = capillary rails

[图片: Skin-side card: 2D PE/PET ES Core-side card: 4D TS + pentagram PET ADL / atent core ild a vertical capillary gradient while adding MD liquid lanes below the skin contact surfa]
# Executive answer

Best first trial for a baby diaper topsheet where skin softness and dryness cannot be sacrificed.

## Recommended formulation

Start at 10% total pentagram PET add-on, 3D, 38–51 mm cut length, durable hydrophilic finish. Put it in the core-side card only: 12.5 gsm top card 2D ES; 10.0 gsm 4D ES + 2.5 gsm star PET lower card.

## Why not higher?

One-component PET does not bond at normal PE-sheath air-through temperatures. Above ~15% total add-on, the risk shifts from useful capillary lanes to lint, tensile loss, rougher hand feel, rewet, and process instability.

[图片: 112 104 96 88 80 0% 5% 10% 15% 20% Simulated balance of MD distribution, acquisition, softness, rewet, and bond integrity]
Simulated balance of MD distribution, acquisition, softness, rewet, and bond integrity

# Baseline architecture and development target

Keep the topsheet "skin-safe and fast-through"; use shaped PET mainly as a sub-surface transport modifier.

[图片: Skin-side card: 2D PE/PET ES Core-side card: 4D S + pentagram PET ADL / at bent core ild a vertical capillary gradient while adding MD liquid lanes below the skin contact surfa]
## Current 25 gsm concept

Air-through bonded PE/PET ES bicomponent staple fiber web.

Two carding feeds: fine 2D ES for softness/coverage; coarser 4D ES for loft/permeability.

Hot-air bonding relies on PE sheath softening; the PET core stays structural.

## Target improvement

Increase capillary absorbency and MD urine distribution before liquid hits the SAP-rich core.

Preserve low strike-through, low rewet, soft touch, low lint, and good CD tensile.

Avoid converting the topsheet into an ADL: it should guide liquid, not store it.

# Why pentagram PET can help

The five-lobed cross-section creates external grooves: more wettable surface and more capillary edges per gram.

### Round ES fiber

[图片]
capillary mostly between fibers

### Pentagram PET

[图片: Pentagram PET]
surface grooves add continuous lanes

### Mechanism 1 — capillary rails

Open grooves along the fiber act as low-volume liquid pathways after hydrophilic finish lowers contact angle. This favors spreading rather than local pooling.

### Mechanism 2 — MD bias

Carded webs usually have partial machine-direction fiber orientation. Adding profiled PET to the second card can bias lateral urine distribution along MD.

### Mechanism 3 — loft support

PET is stiffer than PE/PET ES at bonding temperatures. Moderate addition can help preserve void volume under light pressure.

# The main constraint: one-component PET is not an ES binder

Add enough shaped PET to change capillarity, but not enough to destroy air-through bonding.

[图片: 135 115 105 95 85 75 65 55 45 0% MD distribution benefit Bond / softness risk Benefit saturates; risk accelerates Practical guardrails Keep total one-component PET ≤15% in early trials; 20% is an upper stress-test, not a launch candidate. Use hydrophilic finish on star PET and confirm finish durability after ATB thermal exposure. Mix star PET into the lower card only; avoid skin-side star fibers until hand-feel and lint are proven. Watch CD tensile, lint, fuzz, thermal bond points, and roll winding stability. Launch candidate zone: 5-12% total add-on]
## Practical guardrails

Keep total one-component PET ≤15% in early trials; 20% is an upper stress-test, not a launch candidate.

Use hydrophilic finish on star PET and confirm finish durability after ATB thermal exposure.

Mix star PET into the lower card only; avoid skin-side star fibers until hand-feel and lint are proven.

Watch CD tensile, lint, fuzz, thermal bond points, and roll winding stability.

Launch candidate zone: 5-12% total add-on

# Simulation model used for screening

A practical, assumption-based model to rank trial recipes before running pilot samples.

## Model inputs

Basis weight fixed at 25 gsm.

Top card fixed at 12.5 gsm 2D ES.

Lower card receives 4D ES + star PET.

Pentagram PET shape factor: +25–35% effective surface / groove contribution vs round-equivalent PET.

PET equivalent diameters: 2D ≈ 14.3 µm, 3D ≈ 17.5 µm, 4D ≈ 20.2 µm.

## Score logic

|Output|Direction used|
|---|---|
|MD distribution|↑ with star % and 1/$\sqrt{D}$, saturates after ~15%|
|Strike-through|↑ from permeability + capillary gradient; penalized by over-dense 2D|
|Rewet / dryness|↓ when star % too high or finish stores liquid near topsheet|
|Softness|↓ with stiff profiled PET and skin-side exposure|
|Bond integrity|↓ with unbonded PET fraction|

## Interpretation

Use this simulation to choose trial points, not to certify performance. The real ranking must come from repeated diaper insult tests under pressure.

# Add-on percentage simulation: 3D pentagram PET

Best overall point appears at ~10% total add-on; 15% is useful for stress testing.

[图片: Best overall point appears at ~10% total add-on; 15% is useful for stress testing. 135 125 115 105 95 85 75 0% 5% 10% 5% 15% 20% MD spread Acquisition speed Dryness / rewet score Bond integrity Normalized index, control = 100 Simulation only, validate with repeated strike-through, run-off, rewet, MD/CD spread, tensile, lint and softness tests. Engineering simulation only — validate by line trials and diaper bench tests]
## Readout by addition level

|Total star PET|Expected effect|Decision|
|---|---|---|
|5%|Low-risk modest MD gain|Include|
|10%|Best balance; strong MD gain with manageable risk|Primary|
|15%|High MD gain; monitor rewet/lint/bond loss|Stress point|
|20%|Performance plateau; quality risk rises|Do not launch|

Recommended DOE: 0 / 5 / 10 / 15 / 20%

# Denier simulation at 10% total add-on

3D is the best first denier: enough capillary count without over-densifying the 25 gsm web.

[图片: 130 120 115 100 95 85 2D 3D 4D MD spread Acquisition speed Dryness / rewet Softness Bond integrity Normalized index, control = 100]
## 2D star PET

Higher fiber count and surface area, but can reduce pore size, slow drainage under repeated insults, and raise wetback risk if the finish is too absorbent.

## 3D star PET

Preferred balance for a 25 gsm liner: good groove density, acceptable permeability, and manageable tactile/bond risk.

## 4D star PET

Safer for permeability and dryness, but lower capillary count per gram and may feel coarser; consider only if 3D creates rewet or pressure collapse.

Normalized index, control = 100

Denier-to-diameter estimates assume PET density =1.38 g/cm$^{2}$ and round-e quivalent diameter; profiled shape changes local perimeter and grow geometry.

# Recommended formulations for a 25 gsm, two-card liner

Keep top card unchanged; tune the lower card.

|Trial|Top card / skin side|Lower card / core side|Total star PET|Purpose|
|---|---|---|---|---|
|C0|12.5 gsm 2D PE/PET ES|12.5 gsm 4D PE/PET ES|0%|Control|
|P5|12.5 gsm 2D PE/PET ES|11.25 gsm 4D ES + 1.25 gsm 3D star PET|5%|Low-risk screen|
|P10|12.5 gsm 2D PE/PET ES|10.0 gsm 4D ES + 2.5 gsm 3D star PET|10%|Primary candidate|
|P15|12.5 gsm 2D PE/PET ES|8.75 gsm 4D ES + 3.75 gsm 3D star PET|15%|High-performance stress|
|P20|12.5 gsm 2D PE/PET ES|7.5 gsm 4D ES + 5.0 gsm 3D star PET|20%|Upper-limit stress only|

## Supplier spec for star PET

3.0D ±0.3D; 38–51 mm cut length; 3D crimp; durable hydrophilic finish; low spin-finish extractables; cross-section fidelity ≥85%; low dust/fines.

## Manufacturing note

Pre-blend star PET into the lower-card 4D ES fiber stream. Do not split randomly across both cards until the skin-side softness and wetback effect are known.

# Process window: carding, blending, and web formation

Most defects will come from blending uniformity and fiber control, not from the gross recipe.

## Recommended process route

|1|Open & condition|Condition star PET and ES fibers 24 h; confirm moisture, finish level, static, and bale-to-bale denier.|
|---|---|---|
|2|Pre-blend lower card|Pre-mix 3D star PET with 4D ES in the lower-card feed. Target CV of blend <5% by weight.|
|3|Card gently|Reduce neps and star fiber breakage; monitor web streaks and MD/CD anisotropy.|
|4|Layer orientation|Place 2D ES card on skin side; lower card contains star PET. Keep fiber orientation consistent with desired MD distribution.|
|5|Thermal bond|Use current ATB profile first; adjust only if tensile or fuzz fails.|

## Line parameters to record

Basis weight profile: MD/CD CV, roll edges, and across-width uniformity. Card doffer speed, worker/stripper settings, web draft, suction, and static control.

Through-air oven temperature zones, air velocity, residence time, belt tension.
Caliper, air permeability, tensile MD/CD, fuzz/lint, and hydrophilicity after
bonding.

Orientation ratio: MD/CD tensile and MD/CD wicking length.

Do not raise oven temperature to bond PET; protect PE sheath + web loft instead

# Thermal bonding and surface chemistry

The hydrophilic finish is as important as the cross-section.

[图片: 105 100 95 90 85 80 75 70 Insult 1 Insult 2 Insult 3 Too little finish Durable moderate finish Too high finish / retention Conceptual repeated-insult acquisition index]
## Practical chemistry targets

Durable hydrophilic finish: contact angle low enough for fast wetting, but not so high-retention that it stores liquid in the liner.

Check finish compatibility with lotion, adhesives, SAP dust, hot-air oven temperature, and storage aging.

Require supplier COA: finish chemistry class, add-on %, extractables, and odor/VOC statement.

Validate after heat aging and repeated insults, not only initial strike-through.

## Recommended first target

Moderate durable hydrophilic finish on 3D star PET; no extra hydrophilic treatment on skin-side 2D ES until rewet is benchmarked.

# Pilot DOE: formulation × denier × finish

Run a compact DOE that separates fiber geometry from surface chemistry.

|Factor|Levels|Why it matters|
|---|---|---|
|Star PET total %|0, 5, 10, 15, 20|Quantifies benefit saturation and bond/softness risk.|
|Star PET denier|2D, 3D, 4D at 10%|Separates capillary count from permeability/rewet.|
|Finish level|Supplier standard, +/- one level|Determines wetting vs liquid retention.|
|Placement|Lower card only; optional mixed cards|Proves whether skin-side exposure is acceptable.|
|Emboss/aperture|Current vs light emboss|Tests if geometry can amplify MD distribution without rewet.|

## Minimum sample plan

Make at least 10 kg per liner trial if line permits; lower quantities risk non-representative blending.

Convert each liner trial into identical diapers: same ADL, core SAP/fluff, backsheet, acquisition zone, and emboss.

Randomize testing order and condition all samples 24 h at controlled temperature/humidity.

Use triplicate or n≥5 for liquid tests; report average and standard deviation.

Fast screen: C0, P5, P10, P15 first; run P20 only if line is stable

# Performance test plan: liner-only and diaper-level

Measure topsheet behavior separately from full diaper behavior.

|Test block|Key outputs|Pass / watch criteria|
|---|---|---|
|Liner physical|GSM, caliper, air permeability, MD/CD tensile, elongation, lint/fuzz|No major CD tensile loss; no visible fiber shedding.|
|Surface wetting|Contact angle, strike-through, repeated strike-through, runoff|Equal or faster than control over 3 insults.|
|Capillary distribution|MD/CD wicking length, horizontal spread area, liquid front speed|MD spread +15-25% at P10 vs control.|
|Diaper bench|Repeated insult acquisition time, rewet under load, leakage/runoff, core stain map|No rewet penalty; broader core utilization.|
|Consumer risk|Hand feel, skin-side roughness, noise, odor, lint after rubbing|No noticeable tactile downgrade at P10.|

## Critical measurement

Map the wet core stain after each repeated insult. A better topsheet should spread liquid further in MD without leaving high liquid in the topsheet.

## Failure signature

Fast first strike-through but high rewet after second/third insult means the star PET/finish is retaining liquid too close to skin.

# Decision gates and expected outcomes

A concise framework to move from pilot to product development.

|Gate|Accept|Investigate / adjust|Stop|
|---|---|---|---|
|Fluid performance|P10: MD spread +15-25%, equal/faster acquisition|If strike-through slower, try 4D star or lower finish|Rewet > control by meaningful margin|
|Web quality|GSM CV stable; no streaking; tensile acceptable|Improve blending, anti-static, card settings|Lint/fuzz persists or CD tensile collapses|
|Skin feel|No clear roughness increase vs control|Move star deeper / reduce to 5-8%|Star fibers detectable on skin surface|
|Cost & supply|Supplier can deliver stable cross-section, finish, denier|Dual-source or lower %|High variability or poor finish durability|

[图片: Conservative launch zone Stress-test only 0% 5% 10% 15% 20%]
Decision framework based on topsheet function: fast liquid movement into core, surface dryness, softness, and manufa durability.

# Supplier RFQ / specification checklist

Ask for data that predicts both fluid performance and manufacturing behavior.

Cross-section: pentagram / five-lobed geometry, photomicrographs, cross-section fidelity ≥85%.

Denier: target 3.0D ±0.3D; optional 2D and 4D comparison lots.

Cut length: 38-51 mm; crimp level and crimp stability after opening/carding.

Finish: durable hydrophilic, finish add-on %, extractables, odor/VOC, thermal stability.

Fiber quality: low dust/fines, low static, bale consistency, opening behavior.

Regulatory: hygiene/contact material compliance, heavy metals, allergen/skin-irritation statement as needed.

Pilot support: 25-100 kg lots, same polymer/finish as production scale.

QC: supplier COA for denier, length, finish, moisture, cross-section images, and defect rate.

### Minimum procurement request

Order 3D pentagram PET in two finish levels if possible. If budget allows, add 2D and 4D at the same finish to confirm denier sensitivity.

### Red flag

Reject lots where the pentagram collapses toward round/fused lobes. The grooves are the function; denier alone is not enough.

# Final recommendation

A practical route for sample making and scale-up.

## Recommended first sample

* P10 / 3D / lower-card only

25 gsm total: 12.5 gsm 2D PE/PET ES on skin side; 10.0 gsm 4D PE/PET ES + 2.5 gsm 3D pentagram PET on core side. Use durable hydrophilic finish on star PET.

## Expected result vs control

MD distribution: +15-25% expected if cross-section and finish are stable.

* Acquisition: equal to moderately faster in repeated insult tests.

Dryness: should be near control if star PET remains below skin side.

Process: manageable if total star PET stays around 10%.

## Next steps

Run C0, P5, P10, P15 first. Add P20 only as a process risk boundary.

Test liner-only and converted diapers; prioritize repeated-insult rewet and core stain map.

If P10 rewet rises, reduce finish or move to 4D star PET; if MD spread is weak, try 2D star or light embossing.

Only consider skin-side star PET after roughness/lint and wetback are clearly controlled.

# References and evidence base

Key sources used to shape the engineering assumptions.

|Topic|Reference used|
|---|---|
|Topsheet role and capillary gradient|WO1999039672A1: absorbent article topsheet can use a capillary gradient to drive liquid from wearer-facing surface toward absorbent core.|
|Topsheet material and comfort functions|WO2002013750A2 and EP3810056: topsheet should rapidly accept/move fluid while maintaining body-contact comfort.|
|ADL role|US20050267429A1, EP3238679A1, Sandler Group, Magnera: ADL receives liquid from topsheet, distributes laterally, reduces local saturation and surface wetness.|
|Pentagram / non-circular PET|CN201873791U: five-pointed-star polyester staple fiber increases pore quantity/permeability in nonwovens.|
|Profiled fiber wicking|Stanelle et al. 2005; Cui et al. 2025: grooved/profileed PET fibers create capillary channels and can facilitate liquid transport.|
|Hygiene market context|Supplier ATB topsheet examples: hot-air-through nonwovens are widely sold for baby diaper topsheets; ADL products emphasize fast diffusion and backflow control.|

Note: many hygiene details are proprietary or patent-based. Treat the numerical simulation as a conservative development screen, not as published performance data.


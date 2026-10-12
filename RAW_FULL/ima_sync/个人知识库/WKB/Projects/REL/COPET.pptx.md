---
media_id: "ppt_3867e2b60070d7dc3f413086d0b0036e_c5ed08cd73e2046cd92c5effd6ab4300001a693ee6c0644e"
source_file: "COPET.pptx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Projects/REL/COPET.pptx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# COPET.pptx.md

8
# COPET/PET ES fiber vs PE/PET ES fiber

Impact simulation for baby diaper acquisition & distribution layer (ADL): intake, MD distribution and rewet under repeated insults

Same ADL geometry

Same core/SAP

Only sheath polymer changes

[图片: # COPET/PET ES fiber vs PE/PET ES fiber ##Impact simulation for baby diaper acquisition & distribution layer (ADL): intake, MD distribution and rewet under repeated insults Same ADL geometry Same core/SAP Only sheath polymer changes PE PET]
# Executive answer

Material change alone can improve repeated liquid handling, but process settings and finish durability decide the gain.

COPIET/PET is the stronger candidate for high-speed ADL when the target is better 2nd/3rd insult stability and more MD spreading. PE/PET remains the lower-risk default for softness, cost and low-temperature bonding.

3RD INSULT INTAKE

-16%

CoPET/PET vs PE/PET simulated time

MD SPREAD LENGTH

+17%

third insult lateral reach

REWET MASS

-24%

third insult wetback under load

RAW MATERIAL COST

+8-18%

typical penalty before optimization

## Recommended use

CoPET/PET as ADL bonding fiber where dry-back and repeated insult are premium targets; maintain PE/PET for topsheet-facing softness unless surface feel is validated.

### Key risk

CoPET bonds can become harder or denser if oven temperature/dwell is not re-tuned; this can erase the wetting benefit by losing void volume.

### Next lab gate

Run WSP/EDANA strike-through and rewet with 3×60 mL synthetic urine, same finish add-on, same caliper target, and 40 °C aging.

# 1. Fiber architecture: both are sheath-core ES fibers

Core delivers stiffness and web recovery; low-melt sheath creates thermal-bonded fiber crossover points.

[图片: PE PET COPE]
### PE/PET ES

PE sheath / PET core. Low melting sheath around 130 °C; very soft hand; low surface energy; requires hydrophilic finish for ADL.

### CoPET/PET ES

Copolyester sheath / PET core. Low-melt CoPET can be formulated across roughly 110–220 °C; all-polyester family improves recycling simplicity.

WHAT CHANGES WHEN ONLY SHEATH POLYMER CHANGES?

|Property|PE/PET|CoPET/PET|ADL implication|
|---|---|---|---|
|Sheath surface|low surface energy|more polar|better repeat permeability|
|Bond node|soft/flexible|stronger|can improve integrity|
|Thermal window|easy low-temp|grade-specific|oven re-tune needed|
|Cost/supply|mature/low cost|higher cost|use where dry-back matters|

## 2. ADL function: rapid intake + MD distribution + low wetback

The ADL is a temporary reservoir and lateral spreading layer, not the final storage layer.

[图片: ####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################]
# 3. Simulation setup: same diaper, same core, only ES sheath material changed

Values are relative engineering estimates for screening; they are not vendor guarantees.

FIXED DESIGN

|Parameter|Assumption held constant|
|---|---|
|ADL construction|Air-through bonded nonwoven, 35 gsm, 80 mm width, 270 mm active length|
|Fiber geometry|Same dpf, cut length, crimp and basis-weight CV|
|Hydrophilic finish|Same add-on and chemistry applied to both fibers|
|Diaper core|Same SAP / fluff / core wrap / channel design and same topsheet|
|Insult protocol|3 × 60 mL synthetic urine, 15 min interval, 37 °C|
|Rewet protocol|Filter-paper wetback after 10 min, light pressure|

MODEL LOGIC

Intake time

Driven by surface wetting + vertical permeability + temporary pore volume. CoPET receives a durability benefit in later insults.

MD distribution

Driven by capillary continuity along fiber network and remaining unsaturated pore length; CoPET improves continuity if loft is preserved.

Rewet

Lower when ADL drains into core quickly and retains less free liquid after each insult; over-bonding increases retained liquid.

Sensitivity note: if CoPET oven setting reduces ADL caliper by ≥8%, the predicted benefit can shrink to near zero. The model assumes equal caliper after process tuning.

# 4. Repeated-insult intake simulation

CoPET/PET gives a modest first-insult benefit and larger 2nd/3rd-insult advantage through wetting durability.

SECONDS TO ACQUIRE 60 ML

[图片: 1st 1s 2nd 3rd 3rd 32s 37s 38s 39s 30s 31s 32s 37s]
PE/PET ES

CoPET/PETES

### INTERPRETATION

### First insult

Both fibers are mostly dry. PE/PET can perform well if fresh hydrophilic finish is strong.

### Second insult

CoPET/PET begins to separate because finish anchoring and capillary continuity are more robust.

### Third insult

PE/PET becomes more dependent on remaining surfactant; CoPET/PET holds a clearer advantage.

Key risk: if CoPET is over-bonded and loses loft, vertical permeability may fall and the intake curve can cross back toward PE/PET.

# 5. Machine-direction distribution simulation

Better MD spreading can use more core length and reduce localized SAP saturation under the insult point.

MD SPREAD LENGTH, MM

[图片: 1st 2nd 3rd PE/PET ES CoPET/PET ES Simulated core wetting map after 3 insults PE/PET ES 110 30% front 45% center 25% rear CoPET/PET 25% What this means CoPET/PET shifts urine away from the original insult point faster. The largest benefit is lower local SAP gel blocking and less pooled liquid in the ADL.]
## Simulated core wetting map after 3 insults

PE/PET ES

[图片: PE/PET ES 30% front 45% center 25% rear CoPET/PET 25% front 48% center 27% rear What this means CoPET/PET shifts urine away from the original insult point faster. The largest benefit is lower local SAP gel blocking and less pooled liquid in the ADL.]
## What this means

CoPET/PET shifts urine away from the original insult point faster. The largest benefit is lower local SAP gel blocking and less pooled liquid in the ADL.

# 6. Rewet simulation under repeated insult

Lower rewet comes from faster downward transfer and lower ADL liquid hold-up after each insult.

REWET MASS, G

[图片: 1st 2nd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd 3rd]
MECHANISM SPLIT

### PE/PET ES

Softer surface and high bulk help comfort, but low surface energy makes repeat permeability more finish-dependent.

### CoPET/PET ES

Better finish durability and PET-family surface can lower residual liquid in the ADL if process keeps pores open.

### Diaper impact

A 0.08 g lower third-insult rewet is meaningful in premium baby
diapers because dryness perception is driven by the last insult.

Worst case: CoPET/PET with excessive bonding density may increase rewet despite better chemistry. Validate caliper and pore-size distribution after aging.

# 7. Overall baby diaper performance impact

Relative score assumes same topsheet, core, SAP, elastic, chassis and conversion settings.

RELATIVE SCORE OUT OF 100

[图片: Intake speed MD distribution Dry-back Softness Process robust. Cost PE/PET ES CoPET/PET ES SCORE MEANING Metric Intake 82 91 90 more uniform core use Dry-back 78 88 Low wetness Softness 92 82 PE wins skin feel Process 90 78 PE easier drop-in Cost 92 76 CoPET premium]
PE/PET ES

CoPET/PET ES

SCORE MEANING

|Metric|PE|CoPET|Takeaway|
|---|---|---|---|
|Intake|82|91|better repeat insult|
|MD spread|76|90|more uniform core use|
|Dry-back|78|88|lower wetness|
|Softness|92|82|PE wins skin feel|
|Process|90|78|PE easier drop-in|
|Cost|92|76|CoPET premium|

Best practical route: use CoPET/PET in ADL or lower ADL sub-layer, keep PE/PET-rich topsheet for skin softness, and re-optimize oven temperature to match baseline caliper.

# 8. Process implications on air-through bonded ADL

Do not swap PE/PET to CoPET/PET without re-tuning oven profile, suction, and winding tension.

### PE/PET ES PROCESS WINDOW

#### Lower bonding temperature

PE sheath bonds easily; good for high-speed, low-energy ATB.

### Soft web touch

Lower modulus bond nodes preserve soft bulk and skin-side comfort.

### Finish dependence

Hydrophilic finish must survive storage and repeated wetting; monitor strike-through aging.

### COPET/PET ES PROCESS WINDOW

### Grade-specific melt point

CoPET can be formulated low-melt, but supplier grade determines safe oven setting.

### Stronger bond network

Better tensile stability and web integrity under converting tension.

### Hardness / caliper risk

Over-bonding decreases loft and can hurt intake; target same caliper first.

## CONTROL CHART TARGETS

|QC item|Target|
|---|---|
|ADL caliper|≤ ±3% vs control|
|Air permeability|≥ baseline|
|Bond microscope|no pore blockage|
|Tensile MD/CD|no brittleness|
|3rd strike-through|aging Δ ≤10%|
|Rewet aging|no increase|

# 9. Selection matrix: where each fiber wins

Choose by consumer promise and production risk, not by single strike-through number.

|Decision criterion|PE/PET ES advantage|CoPET/PET ES advantage|Recommendation|
|---|---|---|---|
|Premium dry-back|good with strong finish|better repeat dryness|Trial CoPET/PET ADL|
|Ultra-soft skin contact|softer sheath|needs validation|Keep PE/PET near topsheet|
|Thin core / high SAP|local saturation risk|better spread, less gel-blocking|CoPET/PET favored|
|Cost-down diaper|lower fiber cost|harder to justify|PE/PET favored|
|High-speed line drop-in|lower process risk|needs oven re-tune|Start with 10-30% CoPET blend|
|Mono-material story|mixed polymer|all-PET-family|CoPET/PET favored|

Practical trial ladder: 100% PE/PET control $\rightarrow$ 30% CoPET/PET blend $\rightarrow$ 60% CoPET/PET blend $\rightarrow$ 100% CoPET/PET only if softness and cost are acceptable.

# 10. Recommended ADL development designs

Three formulations to test with exactly the same diaper core and topsheet.

### A — PE/PET control

$\bullet$ 100% PE/PET ES ADL

$\bullet$ Current hydrophilic finish

$\bullet$ Oven setting: current baseline

$\bullet$ Purpose: commercial reference for softness and cost

Expected: lowest risk, good 1st insult, weaker 3rd insult stability.

### B — balanced blend

$\cdot$ 60–70% PE/PET ES

$\bullet$ 30-40% CoPET/PET ES

$\bullet$ Same finish; slight oven increase only if needed

$\bullet$ Purpose: keep softness while improving repeat permeability

Expected: best risk-adjusted route for production trial.

## C — CoPET/PET premium

$\cdot$ 100% CoPET/PET ES ADL

$\bullet$ Adjust oven to equal caliper, not maximum strength

$\bullet$ Purpose: premium dry-back / thin-core concept

Expected: strongest wetting + MD spread, but needs softness and cost validation.

Preferred next step: run B first, because it likely captures 50-70% of the dry-back improvement with much lower softness/cost/process risk than full CoPET/PET.

# 11. Lab validation plan and pass/fail criteria

Use the same pilot line, basis weight and caliper target; otherwise material effect will be confounded.

|Test|Method / condition|Pass target vs PE/PET|Why it matters|
|---|---|---|---|
|Strike-through|3×60 mL, 15 min interval|3rd insult ≥10% faster|Repeated use is the differentiator|
|MD spread|Blue liquid image analysis|3rd spread ≥15% higher|Core utilization / leak protection|
|Wetback / rewet|Filter paper under load|3rd wetback ≥15% lower|Skin dryness perception|
|Caliper recovery|Dry + wet compression|≥ baseline recovery|Maintains void volume|
|Aging durability|40 °C / 75% RH, 2-4 weeks|No major loss of permeability|Finish retention and shelf life|
|Skin feel|Handle-O-Meter or panel|No >10% stiffness penalty|Consumer acceptance|

GATE DECISION

Advance CoPET/PET if it beats PE/PET in 3rd-intake and rewet without losing caliper, softness or converting stability. Otherwise use partial blend only.

# Sources and research basis

Key public sources used to build the comparison and simulation assumptions.

|Source|Deck use|
|---|---|
|WPT Nonwovens — Bicomponent guide|Common sheath-core combinations: PET/CoPET and PET/PE; thermal bonding role of low-melt sheath.|
|Nanya — PET/CoPET Low Melt Fiber|Example PET/CoPET low-melt grade with 125–130 °C melting point and nonwoven bonding use.|
|Liu, Feng & Qian, J. Engineered Fibers and Fabrics, 2019|Through-air bonded PE/PET ADL study; diaper ADL relevance; permeability and wetback metrics.|
|Sandler Group — ADL application page|ADL function: rapid acquisition, transfer to core, minimal wetback and dryness comfort.|
|WPT Nonwovens — Acquisition Layer page|Hydrophilic acquisition layer and open-structure liquid distribution concept.|
|Sanyo Chemical — hydrophilic treatment|Hydrophilic treatment importance for PPIPE/PET hygiene nonwovens and repeated permeability.|
|High-void ADL patent literature|Void volume as lever for strikethrough, rewet and thinner/cost-optimized diaper cores.|

Simulation disclaimer: numerical values are engineering estimates to compare material direction under controlled assumptions. Final design must be validated by pilot-line samples and standard liquid-handling tests.


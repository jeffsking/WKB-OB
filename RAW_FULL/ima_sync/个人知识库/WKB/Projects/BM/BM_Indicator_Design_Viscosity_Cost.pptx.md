---
media_id: "ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e"
source_file: "BM_Indicator_Design_Viscosity_Cost.pptx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Projects/BM/BM_Indicator_Design_Viscosity_Cost.pptx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# BM_Indicator_Design_Viscosity_Cost.pptx.md

8
PROCESS DEVELOPMENT · ABSORBENT HYGIENE · JULY 2026

# An independent BM indicator for the composite breathable backsheet

Protein-error chemistry, slot-die rheology design and cost impact — for a hot-melt lane that fires only on stool, never on urine, never on body heat.

125 °C

application

3 200 mPa·s

0.50 µg/cm$^{2}$

0.056 $\cdot$

per diaper

EXECUTIVE SUMMARY

# The answer, in six numbers

### $\bullet$ TRIGGER

### Soluble protein

> 5 000 mg/L

Protein-error of a sulfonephthalein dye — a binding effect, not a pH effect

## DYE LOADING

## 0.50 µg/cm$^{2}$

= 0.025 wt%

Sets the trip point. Below the 17 µg/cm$^{2}$ skin-safety cap by 34x

## MELT VISCOSITY

## 3 200 mPa·s

@ 120 °C

Brookfield; 2 100 @130 °C, 1 400 @140 °C. Cross index n = 0.88

### APPLICATION

125 °C

115-132 °C

Ceiling is the breathable film, not the chemistry

### COAT WEIGHT

## 20 gsm

10 × 200 mm

40 mg per diaper on the skin side of the backsheet

### COST IMPACT

## 0.056

per diaper

$0.57 per 1 000 all-in, incl. capex amortisation and OEE

THE PROBLEM

# Why BM detection is not just a second wetness lane

## What changed

The odour-control granular removed the smell cue. Mom's primary BM detector is gone — and a conventional pH wetness indicator cannot replace it, because it fires on urine first and stays fired.

## THE DESIGN RULE

The BM lane must key off a molecule that is abundant in stool and effectively absent from urine — and it must do so through a mechanism that is not pH, not humidity, and not temperature.

Everything downstream — dye choice, buffer, matrix, coat weight, lane placement — follows from that one sentence.

### 1

### Urine arrives first, and often

6-8 voids per 12 h. Any moisture- or pH-driven lane is saturated long before the first stool.

### 2

### Stool carries very little free water

Fecal liquid must be transported to the lane; the lane cannot go to the stool.

### 3

### Ammonia rewrites the pH landscape

Urea $\rightarrow$ NH₃ pushes a used diaper to pH 8-9 within hours. pH is no longer a usable discriminator.

### 4

### Body heat is always present

A temperature lane switched at 31-34 °C is permanently ON in wear. It cannot carry the BM message.

MECHANISM SELECTION

# Five candidate BM triggers — scored

|MECHANISM|WHY IT DISCRIMINATES|PRACTICAL LIMIT|SCORE|CALL|
|---|---|---|---|---|
|Soluble protein (protein-error of pH dye)|10 000-40 000 mg/L in faecal liquid vs < 150 mg/L in healthy urine|Melt-stable, cheap, dye already qualified for hygiene|◆◆◆◆◆|SELECTED|
|Bilirubin / bile pigment (diazonium coupling)|Very high in infant stool; essentially zero in urine|Diazonium salts are light- and heat-labile in a 125 °C melt|◆◆◆◆◆|Confirmatory tier 2|
|Faecal protease (cleavable chromogen)|Trypsin / chymotrypsin / elastase are faecal markers|Highest specificity but peptide substrate cost and melt survival|◆◆◆◆◆|R&D only|
|Faecal lipase (chromogenic ester)|Lipase abundant in stool|Slow kinetics; needs an aqueous phase the melt does not offer|◆◆◆◆◆|Rejected|
|Conductivity / ionic strength or viscosity|Stool differs in ionic strength and rheology|Overlaps urine almost completely; needs electronics|◆◆◆◆◆|Rejected|

MECHANISM

# The protein error — a colour change that ignores pH

[图片: What actually happens The lane is buffered hard to pH 3.0 with a citrate / stearyl-phosphate acid system, so the dye sits fully in its yellow, protonated form. Protein reaches the lane. Free amino groups on the polypeptide bind the dye anion electrostatically and stabilise it. Binding shifts the dye's apparent pKa downward. It ionises and turns violet — while the bulk pH is still 3. The lane therefore reports protein concentration, not pH. Urine can arrive at pH 5.5 or at pH 9 after ammoniacal ageing and the lane does not move. Trip point is set by dye loading alone: D × C* ≈ 2 500 (µg/cm$^{2}$ · mg/L). Load less dye, and it takes more protein to move it. DRY — in pack DRY protonated · buffered pH 3.0 · pale amber URINE ONLY Water enters, pH outside rises to 8–9 Buffer holds the micro-environment at pH 3 Protein < 150 mg/L $\rightarrow$ no binding $\rightarrow$ NO CHANGE BRM STOOL ARRIVES Faecal liquid delivers > 5 000 mg/L protein Dye-protein complex forms · pKa collapses LANE TURNS DEEP VIOLET — irreversible]
CROSS-TALK

# Orthogonality: what each lane is allowed to see

[图片: Urine lane (BCG, pH) (BCG, pH) none none none none new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new]
## Urine lane and BM lane share no trigger

One reads protons, the other reads polypeptide binding. There is no pathway by which a urine event can produce a BM signal.

### Temperature lane is fully isolated

A leuco-dye / PCM system responds to heat only. Keep it in a separate melt circuit — its bisphenol developers are weak acids that would poison a pH lane by migration.

## One real coupling remains

An alkaline odour-control granular can titrate the BM lane's buffer from the inside. This is the only amber cell in the matrix and it is the No. 1 risk in the programme.

ROBUSTNESS

# Four independent defences against a false BM signal

[图片: MECHANISM 1 Protein binding, not pH A urine pH excursion of 5.5 $\rightarrow$ 9.0 produces zero response because the trigger is not a proton. This is the load-bearing defence. THRESHOLD 2 Trip at 5 000 mg/L 33× above healthy infant urine; still 2× below faecal liquid. Set purely by dye loading — 0.50 µg/cm$^{2}$. MICRO-ENVIRONMENT GEOMETRY 4 Lane placement + conduit 3. 1.94 µeq H⁺/cm$^{2}$ of accessible acid against ~0.0055 µeq of alkali ingress $\rightarrow$ 350× margin even on aged urine. BM lane sits over a low-basis-weight core channel in the rear third; urine lane is 25 mm away in the crotch.]
A false positive needs all four to fail at once. A false negative needs only the geometry to fail — which is why fluid transport to the lane, not chemistry, is the harder engineering problem.

SELECTIVITY DESIGN

# Setting the trip point: dye loading is the only knob

[图片: D × C* ≈ 2 500 — the protein-error selectivity hyperbola healthy infant urine < 150 mg / Lm² — skin-safety cap up to 10 000 mg/L INFANT FAECAL LIQUID > 10 000 mg/L DESIGN POINT LIQUID > 10 000 mg/L PH-indicator loading (μg/cm²) DESIGN POINT 0.50 μg/cm² $\rightarrow$ trips at 5 000 mg/L (= 0.025 wt% of a 20 gsm coat) ### protein concentration at which the lane turns (mg/L) DESIGN POINT 0.50 μg/cm² $\rightarrow$ trips at 5 000 mg/L (= 0.025 wt% of a 20 gsm coat) ### protein concentration at which the lane turns (mg/L)]
## DESIGN POINT

0.50 µg/cm$^{2}$

= 0.025 wt% of a 20 gsm coat

MARGIN VS HEALTHY URINE

33 ×

trip 5 000 vs < 150 mg/L

MARGIN VS FAECAL LIQUID

2 ×

trip 5 000 vs > 10 000 mg/L

MARGIN VS SAFETY CAP

34 ×

0.50 vs 17 µg/cm$^{2}$ limit

Nephrotic urine is the edge case — verify with a 10 000 mg/L albumin challenge.

MICRO-ENVIRONMENT SPEC

# The buffer only has to protect a micro-environment

[图片: RSA SPEC: matrix water uptake ≤ 5 wt% (37 °C / 24 h) $\rightarrow$ ≥ 350 × margin Fresh urine (20 mmol/L base) 8 h ammoniacal urine (55 mmol/L base) Buffer safety margin (x) $10^{3}$ $10^{2}$ $10^{3}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}]
$\bullet$ The alkali that matters is not the alkali in the diaper — it is only what dissolves into the melt film itself.

$\bullet$ At 5 wt% water uptake, a 20 gsm coat takes up 0.10 µL/cm$^{2}$. Even 8-hour ammoniacal urine at 55 mmol/L base delivers 0.0055 µeq/cm$^{2}$.

$\bullet$ Against 1.94 $\mueq/cm^2$ of accessible acid that is a 350× margin — which is why a hydrophobic rosin / FT-wax matrix matters more than piling in more citric acid.

$\bullet$ Loading past ~8 wt% micronised citric acid is counter-productive — it raises viscosity, abrades the die land and risks shim blockage.

### SPECIFICATION

Equilibrium water uptake ≤ 5 wt%
37 °C / 95% RH / 24 h
Accessible acid ≥ 1.8 μeq H⁺/cm$^{2}$
titrated pH 2.5 $\rightarrow$ 4.5

titrated pH 2.5 $\rightarrow$ 4.5

FORMULATION

# Material composition — BM indicator hot melt

|COMPONENT|wt %|FUNCTION|
|---|---|---|
|Pentaerythritol rosin ester, SP ≈ 98 °C|34.0|1st binder — holds the dye in its yellow state; acidic|
|Polymerised rosin|14.0|Colour depth, cohesion, acid reserve|
|Fischer-Tropsch wax, C40-C60|26.0|Sets viscosity and open time; keeps n near 1|
|Hydrogenated C5 hydrocarbon resin|9.0|Flexibility, adhesion to PE film, anti-flake|
|Citric acid, micronised d90 < 15 µm|6.0|Buffer acid leg — pins the lane at pH 3.0|
|Monostearyl citrate|3.5|Melt-soluble buffer leg; no particulate load|
|Stearyl phosphate free acid|2.0|Strong-acid stabiliser against humid storage|
|C12-14 alcohol ethoxylate (7 EO)|3.0|Wet-out; accelerates colour kinetics|
|Organoclay (quaternised bentonite)|1.2|Anchors the violet anion — see warning below|
|Hindered phenol AO + phosphite|1.25|Melt stability over 8 h residence at 130 °C|
|Bromocresol purple|0.025|The protein-error dye. 0.50 µg/cm² at 20 gsm|
|Solvent Red 24 (oil-soluble tint)|0.025|Offsets the pre-change hue away from the urine lane|

## BLENDED COST

$3.56 / kg

40 mg per diaper $\rightarrow$ $0.142 per 1 000

### $\blacktriangle$ DO NOT USE A SOLUBLE QUAT

Standard wetness-indicator formulations anchor the dye with a soluble quaternary ammonium salt. In a protein-error lane that salt mimics protein and develops the violet in the pack. Use a cationic organoclay instead, ≤ 1.5 %.

### PARTICLE-SIZE RULE

Every solid must satisfy shim ≥ 10 × d90. At a 200 µm shim that caps d90 at 20 µm — micronise the citric acid and screen the organoclay at 25 µm before the melter.

SIGNAL DESIGN

# Colour system: three lanes that can never be confused

[图片: URINE LANE Bromocresol green, pH trigger pale amber blue-green Change soon Change soon BM LANE Bromocresol purple, protein error pale straw DEEP VIOLET CHANGE NOW TEMP LANE Leuco dye, 37.5 °C switch grey red Fever check TRE� RULES ≥ 6 Ostwald numbers separates every post-change hue from every other lane's post-change hue. Violet is reserved for BM alone. Nothing else on the diaper — graphic, elastic, print — may use it. elastic, print — may use it. Irreversible Once violet, always violet. The organoclay locks the complex so it cannot fade or migrate before the change. Backsheet optics Film 30-80 % light transmittance; outer nonwoven ≥ 50 %. Above 80 % and mom sees the stool itself.]
RHEOLOGY · 1 OF 3

# Viscosity specification for the slot-die lane

[图片: APPLICATION WINDOW 115 - 132 °C 6000 mPa·s - pump / distribution ceiling Brookfield viscosity (mPa·s) 3,200 2,092 1,396 800 mPa·s - bead break-up / stringing floor Spec band ±18 % Design curve Ea = 56 kJ/mol 90 100 110 120 130 140 150 160 170 Melt temperature (°C) Brookfield @ 140 °C Ring & ball softening pt. Flow activation energy 56 kJ/mol Application temperature 125 °C (115-132) Melt density @ 125 °C Surface tension @ 125 °C 30 mN/m]
This sits squarely inside what a standard diaper HMA melter and hose set already deliver — the target is deliberately close to a construction adhesive so no new pump technology is needed.

RHEOLOGY · 2 OF 3

# Design it near-Newtonian — on purpose

[图片: Target: n = 0.88 — deliberately near-Newtonian Viscosity (mPa·s) 115 °C 125 °C 132 °C Newtonian reference (125 °C) Shear rate (s⁻$^{1}$) slot shear rate 180-300 µm shim 200-500 m/min 10$^{5}$ Shear rate (s⁻$^{1}$) SPEC ADDITION Cross index n ≥ 0.85 measured 10-50 000 s⁻$^{1}$ on a capillary rheometer at 125 °C.]
$\bullet$ In the slot the melt sees 9 000–40 000 s$^{-1}$. A strongly shear-thinning hot melt loses more than half its viscosity there, then recovers on the web — and that mismatch is what produces ribbing and edge bleed.

$\bullet$ Published slot-die work shows shear-thinning fluids roughly double the minimum stable wet thickness versus a Newtonian fluid at the same capillary number; shear-thickening fluids reduce it by ~10 %.

$\bullet$ So specify the Cross index, not just the Brookfield number: $n \ge 0.85$, $\lambda \le 2 \times 10^{-4}$ s.

$\bullet$ Practically that means a wax-and-rosin matrix with no high-molecular-weight styrenic block copolymer. SBC would give you tack you do not need and a coating window you cannot hold at 400 m/min.

### SPEC ADDITION

Cross index $n \ge 0.85$ measured $10-50 000 s^{-1}$ on a capillary rheometer at 125 °C.

RHEOLOGY · 3 OF 3

# Slot geometry sets the pressure — and 100 µm will not work

[图片: Pressure drop across die land (bar) at 125 °C 300 m/min RECOMMENDED 500 m/m/200 µm 120 100 80 60 40 bar — existing HMA system ceiling 20 0 100 150 200 250 300 0 Slot shim thickness (µm) 120 - dashed, 400 m/m 99.7 bar X Melt throughput 80 g/min WHY IT MATTERS Pressure scales with 1/t$^{3}$. Halving the shim to gain a crisper edge multiplies die pressure by eight and takes you past what the existing hose and gear pump can hold. Buy the edge definition with the land geometry, not the shim. Poiseuille slot: $\dot{y} = 6Q/(w \cdot t^2)$, $\Delta P = 12 \cdot \eta \cdot Q \cdot L/(w \cdot t^3)$, $L = 5$ mm land, 10 mm lane width, 20 gsm.]
|Shim thickness|200 µm|
|---|---|
|Wall shear rate @ 400 m/min|22 200 $s^{-1}$|
|Viscosity at that shear|1 225 mPa·s|
|Pressure drop over land|13.6 bar|
|At 100 µm shim instead|99.7 bar X|
|Melt throughput|80 g/min|

## WHY IT MATTERS

Pressure scales with 1/t$^{3}$. Halving the shim to gain a crisper edge multiplies die pressure by eight and takes you past what the existing hose and gear pump can hold. Buy the edge definition with the land geometry, not the shim.

APPLICATION ARCHITECTURE

# The single most important process finding

You cannot run this as a free-gap pre-metered slot die.

Capillary number at 400 m/min, 125 °C

$$Ca=\eta V/\sigma=272$$

Deep in the high-Ca regime — viscocapillary theory says the minimum wet thickness plateaus at t/H ≈ 0.45–0.55

Required wet film

$$h=22.2\mu m$$

$$20\text{ gsm}\div 900\,\text{kg/m}^3$$

Therefore maximum free gap

$$H\leq 44\mu m$$

$h \div 0.50$. A 44 µm free span on a diaper line is not achievable — web flutter alone is ±150 µm

## WHAT TO SPECIFY INSTEAD

### Contact (wiped) slot nozzle

Die lip rides on the film over a hardened, chilled backing roll. Effective gap ≈ 0 — the bead is wiped, not spanned.

### Chilled backing roll, 15-20 °C

Removes the heat before it reaches the microporous structure and freezes the bead within one lip length.

### Servo-metered gear pump

Speed-following so coat weight stays at 20 gsm through
accel/decel. Bead-on-demand for the dashed lane pattern.

### Nozzle contact pressure 2-4 N/cm

Enough to seal the bead, low enough not to emboss the film.

PROCESS WINDOW

# The operating window is boxed in the three sides

[图片: 200 µm shim · 20 gsm · 10 mm lane Melt application temperature (°C) 150 140 130 120 110 120 130 130 130 [重复数据串: 140 140 140 140 ×22] 140 140]
LOWER TEMPERATURE LIMIT

≈ 112 °C

Die pressure exceeds the 40 bar system ceiling at line speed

UPPER TEMPERATURE LIMIT

≈ 134 °C

Film bulk temperature reaches 90 °C and the microporous structure starts to close

VISCOSITY FLOOR

≈ 136 °C

Below 800 mPa·s the bead breaks up and the lane edge bleeds

NOMINAL SET POINT

125 °C

≈ 13 K of headroom below the film limit and 13 K above the pressure limit

THERMAL LOAD

# The breathable film, not the chemistry, sets the temperature ceiling

[图片: Film temperature (°C) Film bulk equilibrium (no chill roll) Contact interface (effusivity) 90 °C — microporous PE pore-collapse / WVTR loss 89 °C at the 132 °C edge $\rightarrow$ 1.5 K headroom Film temperature (°C) Film bulk equilibrium (no chill roll) Contact interface (effusivity) 90 °C — microporous PE pore-collapse / WVTR loss 89 °C at the 132 °C edge $\rightarrow$ 1.5 K headroom Film temperature (°C) A microporous CaCO$_{3}$-filled PE film loses WVTR irreversibly once the drawn structure anneals — typically above 90 °C. You will not see it on the line; you will see it in the humidity chamber a week later. Fitting a chilled backing roll moves the ceiling up by roughly 15 K and is far cheaper than reformulating for a lower application temperature. MANDATORY TEST WVTR (ASTM E96) on coated vs uncoated film, and hydrohead, at every temperature set point in the window.]
$\bullet$ Two temperatures matter. The contact interface — set by thermal effusivity — reaches 69 °C at a 125 °C melt. That is comfortable.

$\bullet$ The bulk equilibrium temperature of coating plus film, with no chill roll, reaches 85 °C at 125 °C and 90 °C at 135 °C. That is the number that closes the pores.

$\bullet$ A microporous CaCO$_3$-filled PE film loses WVTR irreversibly once the drawn structure anneals — typically above 90 °C. You will not see it on the line; you will see it in the humidity chamber a week later.

$\bullet$ Fitting a chilled backing roll moves the ceiling up by roughly 15 K and is far cheaper than reformulating for a lower application temperature.

## MANDATORY TEST

WVTR (ASTM E96) on coated vs uncoated film, and hydrohead, at every temperature set point in the window.

LINE INTEGRATION

# What you keep, what you add, what you must change

### KEEP AS-IS

$\bullet$ Melter platform, controller and hose architecture — the target viscosity is deliberately construction-adhesive-like

* Gear-pump technology and pressure class (13.6 bar working, 40 bar ceiling)

$\bullet$ Backsheet unwind, splicer and web guiding

$\bullet$ Existing urine-indicator applicator and its recipe

## ADD

$\bullet$ Dedicated low-temperature melter, 10 L, on its own circuit — never share a hose with the temperature lane

$\bullet$ Contact slot nozzle, 10 mm lane, 200 µm shim, 5 mm land

$\bullet$ Chilled backing roll, 15-20 °C, hardened surface

$\bullet$ Servo speed-following on the pump plus bead-on-demand valve

## CHANGE

$\bullet$ Backsheet film light transmittance re-spec to 30-80 %

$\bullet$ Outer nonwoven transmittance ≥ 50 % in the lane footprint

$\bullet$ Core: low-basis-weight faecal conduit aligned to the BM lane

$\bullet$ Odour-control granular: alkalinity screen before it goes near the lane

Net new hardware ≈ $77 k core / $109 k with in-line colour verification. Nothing on the list requires a line rebuild or a new pitch.

PRODUCT ARCHITECTURE

# Where the lane goes — and how the stool reaches it

[图片: CROSS-SECTION Outer nonwoven ≥ 50% transmittance Composite breathable film 30-80% BMLANE 20 gsm · 10 mm · violet Core wrap / dusting layer Absorbent core — low-basis-weight conduit Acquisition / distribution layer Topsheet THE FALSE-NEGATIVE PROBLEM Stool carries far less free water than urine, so it will not reach a lane sitting behind a full-basis-weight core. Cut a 12 mm wide, SAP-free conduit through the core directly above the BM lane and put a diffusion layer between core and lane. Without that conduit the chemistry is irrelevant — the lane simply never sees protein. PLAN VIEW (non-skin side) BACK FRONT BM lane 10 × 200 mm · straddles the fold line, so an unreacted section remains for a two-tone read Urine lanes 2 × 6 mm in the crotch, 25 mm clear of the BM lane Temperature lane Waistband only — separate circuit, separate melter Rear placement is deliberate — stool pools posteriorly whether the baby is lying or standing.]
## THE FALSE-NEGATIVE PROBLEM

Stool carries far less free water than urine, so it will not reach a lane sitting behind a full-basis-weight core. Cut a 12 mm wide, SAP-free conduit through the core directly above the BM lane and put a diffusion layer between core and lane. Without that conduit the chemistry is irrelevant — the lane simply never sees protein.

### PLAN VIEW (non-skin side)

[图片: BACK FRONT]
### BM lane

10 × 200 mm · straddles the fold line, so an unreacted section remains for a two-tone read

### Urine lanes

2 × 6 mm in the crotch, 25 mm clear of the BM lane

## Temperature lane

Waitband only — separate circuit, separate melter

Rear placement is deliberate — stool pools posteriorly whether the baby is lying or standing.

CRITICAL INTERFERENCE

# The one thing that will kill this programme

Your odour-control granular is probably alkaline. If it is, it will turn the BM lane violet inside the pack.

[图片: Zeolite (4A / 13X) pH 9-11 HIGH Strongly alkaline slurry. Will titrate the buffer through the dusting layer over shelf life. Sodium bicarbonate pH 8.3 HIGH Mobile, water-soluble, migrates readily. Worst case for a buffered lane. Activated carbon pH 6-10 MEDIUM Grade-dependent alkalinity, and it adsorbs the dye — expect greying as well as drift. Cyclodextrin pH 6-7 LOW Neutral, non-migrating. The compatible choice if the odour performance holds. Ion-exchange resin, H⁺ form pH 4-6 LOW Acidic form is actively helpful — it reinforces the lane's own buffer. SCREEN IT FIRST Before any coating trial, run this: 1 Slurry 5 g granular in 50 mL deionised water, 1 h, 25 °C. Measure pH and titratable base to pH 4. 2 Accept only if slurry pH ≤ 7.5 and titratable base ≤ 0.2 mmol/g. 3 Build a full diaper and age it 8 weeks at 40 °C / 75 % RH. Grade the lane weekly on a 0-5 scale; reject at grade 1. 4 If the granular fails, the fix is a barrier — move it above the core wrap, or micro-encapsulate it — not more acid in the lane.]
ECONOMICS

# Cost impact: 0.056 US cents per diaper

[图片: Total ≈ $0.57 per 1 000 = 0.057 US cents per diaper USD per 1 000 diapers 0.30 0.25 0.20 0.15 0.10 0.05 0.00 Indicator material Applicator capex (3 y) OEE loss 0.30% Melter energy + purge Film / graphic re-spec Capex, core scope Capex with colour verification Amortised over 707 M diapers (3 y) $0.109 $0.045 OEE allowance, 0.30% $0.240$ Film / graphic re-spec Total]
The dominant cost is not the chemistry — the dye is $0.02 per 1 000 diapers. It is the OEE you give up to a fourth applicator. Budget the engineering effort accordingly: reliability of the lane, not cost of the melt.

|Blended melt cost|$3.56 / kg|
|---|---|
|Coat weight per diaper|40 mg|
|Material|$0.142 / 1 000|
|Capex, core scope|$76 900|
|Capex with colour verification|$108 900|
|Amortised over 707 M diapers (3 y)|$0.109 / 1 000|
|OEE allowance, 0.30 %|$0.240 / 1 000|
|TOTAL|$0.567 / 1 000|

TEST PLAN

# Validation protocol

## CHEMISTRY

$\bullet$ Protein challenge ladder: 0 / 150 / 1 000 / 5 000 / 10 000 / 40 000 mg/L bovine albumin — record $\Delta$E* at 2, 5, 15 min

$\bullet$ Synthetic urine, pH 5.5 and pH 9.0, 3 × 40 mL insults — require no change at 15 min and at 4 h

$\bullet$ Aged-urine challenge: 8 h ureolysed urine at 55 mmol/L base

$\bullet$ Buffer titration: accessible μeq H$^{+}$/cm$^{2}$ between pH 2.5 and 4.5

## STABILITY

$\bullet$ 40 °C / 75% RH for 8 weeks, graded weekly 0–5 — reject at grade 1

$\bullet$ Melt-pot residence: 8 h at 130 °C, then re-run the protein ladder

$\bullet$ Light stability: 24 h under 6 500 K, 1 000 lux

$\bullet$ Dye leach: 16 h weighted contact, inspect adjacent core for bleed

## PROCESS & PRODUCT

* Coat-weight capability across 200-500 m/min: Cpk ≥ 1.33 on 20 ± 3 gsm

$\bullet$ WVTR (ASTM E96) and hydrohead, coated vs uncoated, at every set point

$\bullet$ Real-stool panel: breast-fed and formula-fed, 20 samples each, ≥ 95 % detection at 15 min

$\bullet$ Caregiver comprehension: 40 mothers, unprompted — target ≥ 90 % correct action

PLAN AND RISK

# 90 days to a line trial

[图片: WEEKS 1-2 Screen the odour granular Slurry pH and titratable base on every candidate. Go / no-go before any spend. WEEKS 3-6 Bench formulation Three dye loadings × two buffer levels. Protein ladder plus urine challenge on hand-drawn films. WEEKS 7-9 Pilot coater Confirm the viscosity spec on a capillary rheometer; coat at 100-200 m/min; WVTR and hydrohead. WEEKS 10-13 Line trial Contact nozzle plus chilled roll on one lane. Coat-weight Cpk, 8-week ageing pull, stool panel. TOP RISKS Alkaline odour granular pre-develops the lane HIGH Low-basis-weight conduit plus diffusion layer; validate on real stool, not synthetic HIGH Specify organodlay; audit the supplier's base formulation MEDIUM Chilled backing roll; cap at 132 °C; WVTR at every set point Film WVTR loss from thermal load Freedom to operate around granted feces-indicator claims MEDIUM Formal FTO on US 12,396,899 and family before pilot spend]
### TOP RISKS

[图片: Alkaline odour granular pre-develops the lane HIGH Screen in week 1; barrier or encapsulate; do not compensate with acid Faecal liquid never reaches the lane HIGH Low-basis-weight conduit plus diffusion layer; validate on real stool, not synthetic Soluble quat in a carried-over WI base develops the dye MEDIUM Specify organodlay; audit the supplier's base formulation Film WVTR loss from thermal load MEDIUM Chilled backing roll; cap at 132 °C; WVTR at every set point Freedom to operate around granted feces-indicator claims MEDIUM Formal FTO on US 12,396,899 and family before pilot spend]

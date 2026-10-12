---
media_id: "ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e"
source_file: "BM_Indicator_Design_Viscosity_Cost.pptx.md"
original_path: "RAW/ima_sync/WKB/Projects/BM/BM_Indicator_Design_Viscosity_Cost.pptx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
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

![What actually happens\n\nThe lane is buffered hard to pH 3.0 with a citrate / stearyl-phosphate acid system, so the dye sits fully in its yellow, protonated form.\nProtein reaches the lane. Free amino groups on the polypeptide bind the dye anion electrostatically and stabilise it.\nBinding shifts the dye's apparent pKa downward. It ionises and turns violet — while the bulk pH is still 3.\nThe lane therefore reports protein concentration, not pH. Urine can arrive at pH 5.5 or at pH 9 after ammoniacal ageing and the lane does not move.\n\nTrip point is set by dye loading alone: D × C* ≈ 2 500 (µg/cm$^{2}$ · mg/L). Load less dye, and it takes more protein to move it.\n\nDRY — in pack DRY protonated · buffered pH 3.0 · pale amber\n\nURINE ONLY\n\nWater enters, pH outside rises to 8–9 Buffer holds the micro-environment at pH 3 Protein < 150 mg/L $\rightarrow$ no binding $\rightarrow$ NO CHANGE\n\nBRM\n\nSTOOL ARRIVES\n\nFaecal liquid delivers > 5 000 mg/L protein Dye-protein complex forms · pKa collapses LANE TURNS DEEP VIOLET — irreversible\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/c437aa48-733a-4cff-8324-3eed9676a9d6.png)
CROSS-TALK

# Orthogonality: what each lane is allowed to see

![Urine lane (BCG, pH)\n\n(BCG, pH)\n\nnone\n\nnone\n\nnone\n\nnone\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\n\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\nnew\n\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/89532c85-38da-4908-82a9-e3486dd911ba.png)
## Urine lane and BM lane share no trigger

One reads protons, the other reads polypeptide binding. There is no pathway by which a urine event can produce a BM signal.

### Temperature lane is fully isolated

A leuco-dye / PCM system responds to heat only. Keep it in a separate melt circuit — its bisphenol developers are weak acids that would poison a pH lane by migration.

## One real coupling remains

An alkaline odour-control granular can titrate the BM lane's buffer from the inside. This is the only amber cell in the matrix and it is the No. 1 risk in the programme.

ROBUSTNESS

# Four independent defences against a false BM signal

![MECHANISM\n\n1\n\nProtein binding, not pH\n\nA urine pH excursion of 5.5 $\rightarrow$ 9.0 produces zero response because the trigger is not a proton. This is the load-bearing defence.\n\nTHRESHOLD\n\n2\n\nTrip at 5 000 mg/L\n\n33× above healthy infant urine; still 2× below faecal liquid. Set purely by dye loading — 0.50 µg/cm$^{2}$.\n\nMICRO-ENVIRONMENT\n\nGEOMETRY\n\n4\n\nLane placement + conduit\n\n3. 1.94 µeq H⁺/cm$^{2}$ of accessible acid against ~0.0055 µeq of alkali ingress $\rightarrow$ 350× margin even on aged urine.\n\nBM lane sits over a low-basis-weight core channel in the rear third; urine lane is 25 mm away in the crotch.\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/c5b8f5f5-b14d-4710-9e8c-a511a9e6984a.png)
A false positive needs all four to fail at once. A false negative needs only the geometry to fail — which is why fluid transport to the lane, not chemistry, is the harder engineering problem.

SELECTIVITY DESIGN

# Setting the trip point: dye loading is the only knob

![D × C* ≈ 2 500 — the protein-error selectivity hyperbola\n\nhealthy infant urine < 150 mg / Lm² — skin-safety cap up to 10 000 mg/L\n\nINFANT FAECAL LIQUID > 10 000 mg/L\n\nDESIGN POINT\nLIQUID\n> 10 000 mg/L\n\nPH-indicator loading (μg/cm²)\n\nDESIGN POINT\n0.50 μg/cm² $\rightarrow$ trips at 5 000 mg/L\n(= 0.025 wt% of a 20 gsm coat)\n\n### protein concentration at which the lane turns (mg/L)\n\nDESIGN POINT\n0.50 μg/cm² $\rightarrow$ trips at 5 000 mg/L\n(= 0.025 wt% of a 20 gsm coat)\n\n### protein concentration at which the lane turns (mg/L)\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/3bfc4d0f-8669-4a19-84ea-2edf6c0e361c.png)
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

![RSA\nSPEC: matrix water uptake ≤ 5 wt% (37 °C / 24 h) $\rightarrow$ ≥ 350 × margin\nFresh urine (20 mmol/L base)\n8 h ammoniacal urine (55 mmol/L base)\nBuffer safety margin (x)\n$10^{3}$ $10^{2}$ $10^{3}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}$ $10^{2}\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/6234ed5a-7fff-4dc3-8660-086158c52cf0.png)
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

![URINE LANE\nBromocresol green, pH trigger\n\npale amber\n\nblue-green\n\nChange soon\n\nChange soon\n\nBM LANE\n\nBromocresol purple, protein error\n\npale straw\n\nDEEP VIOLET\n\nCHANGE NOW\n\nTEMP LANE\n\nLeuco dye, 37.5 °C switch\n\ngrey\n\nred\n\nFever check\n\nTRE� RULES\n\n≥ 6 Ostwald numbers\nseparates every post-change hue from every other lane's post-change hue.\n\nViolet is reserved\nfor BM alone. Nothing else on the diaper — graphic, elastic, print — may use it.\n\nelastic, print — may use it.\n\nIrreversible\nOnce violet, always violet. The organoclay locks the complex so it cannot fade or migrate before the change.\n\nBacksheet optics\nFilm 30-80 % light transmittance; outer nonwoven ≥ 50 %. Above 80 % and mom sees the stool itself.\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/0161dab8-d5a3-47cd-8a5c-f3a5faea90dc.png)
RHEOLOGY · 1 OF 3

# Viscosity specification for the slot-die lane

![APPLICATION WINDOW\n115 - 132 °C\n6000 mPa·s - pump / distribution ceiling\nBrookfield viscosity (mPa·s)\n3,200\n2,092\n1,396\n800 mPa·s - bead break-up / stringing floor\nSpec band ±18 %\nDesign curve Ea = 56 kJ/mol\n90 100 110 120 130 140 150 160 170\nMelt temperature (°C)\nBrookfield @ 140 °C\nRing & ball softening pt.\nFlow activation energy\n56 kJ/mol\nApplication temperature\n125 °C (115-132)\nMelt density @ 125 °C\nSurface tension @ 125 °C\n30 mN/m\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/f592d071-3a1e-4824-9a58-a8804932cb4d.png)
This sits squarely inside what a standard diaper HMA melter and hose set already deliver — the target is deliberately close to a construction adhesive so no new pump technology is needed.

RHEOLOGY · 2 OF 3

# Design it near-Newtonian — on purpose

![Target: n = 0.88 — deliberately near-Newtonian\n\nViscosity (mPa·s)\n\n115 °C\n\n125 °C\n\n132 °C\n\nNewtonian reference (125 °C)\n\nShear rate (s⁻$^{1}$)\n\nslot shear rate\n\n180-300 µm shim\n\n200-500 m/min\n\n10$^{5}$\n\nShear rate (s⁻$^{1}$)\n\nSPEC ADDITION\n\nCross index n ≥ 0.85 measured 10-50 000 s⁻$^{1}$ on a capillary rheometer at 125 °C.\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/21eee8f9-3005-4d04-82f0-89672d7b8166.png)
$\bullet$ In the slot the melt sees 9 000–40 000 s$^{-1}$. A strongly shear-thinning hot melt loses more than half its viscosity there, then recovers on the web — and that mismatch is what produces ribbing and edge bleed.

$\bullet$ Published slot-die work shows shear-thinning fluids roughly double the minimum stable wet thickness versus a Newtonian fluid at the same capillary number; shear-thickening fluids reduce it by ~10 %.

$\bullet$ So specify the Cross index, not just the Brookfield number: $n \ge 0.85$, $\lambda \le 2 \times 10^{-4}$ s.

$\bullet$ Practically that means a wax-and-rosin matrix with no high-molecular-weight styrenic block copolymer. SBC would give you tack you do not need and a coating window you cannot hold at 400 m/min.

### SPEC ADDITION

Cross index $n \ge 0.85$ measured $10-50 000 s^{-1}$ on a capillary rheometer at 125 °C.

RHEOLOGY · 3 OF 3

# Slot geometry sets the pressure — and 100 µm will not work

![Pressure drop across die land (bar) at 125 °C\n300 m/min\nRECOMMENDED 500 m/m/200 µm\n120\n100\n80\n60\n40 bar — existing HMA system ceiling\n20\n0\n100\n150\n200\n250\n300\n0\nSlot shim thickness (µm)\n120\n- dashed, 400 m/m\n99.7 bar X\nMelt throughput\n80 g/min\nWHY IT MATTERS\nPressure scales with 1/t$^{3}$. Halving the shim to gain a crisper edge multiplies die pressure by eight and takes you past what the existing hose and gear pump can hold. Buy the edge definition with the land geometry, not the shim.\nPoiseuille slot: $\dot{y} = 6Q/(w \cdot t^2)$, $\Delta P = 12 \cdot \eta \cdot Q \cdot L/(w \cdot t^3)$, $L = 5$ mm land, 10 mm lane width, 20 gsm.\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/24d8527c-343b-4690-a8aa-368cb0be5663.png)
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

![200 µm shim · 20 gsm · 10 mm lane\n\nMelt application temperature (°C)\n\n150\n\n140\n\n130\n\n120\n\n110\n\n120\n\n130\n\n130\n\n130\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n\n140\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/82370e74-79ad-412f-b6d0-02ef9ddc8233.png)
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

![Film temperature (°C)\n\nFilm bulk equilibrium (no chill roll)\nContact interface (effusivity)\n\n90 °C — microporous PE pore-collapse / WVTR loss\n\n89 °C at the 132 °C edge\n$\rightarrow$ 1.5 K headroom\n\nFilm temperature (°C)\n\nFilm bulk equilibrium (no chill roll)\nContact interface (effusivity)\n\n90 °C — microporous PE pore-collapse / WVTR loss\n\n89 °C at the 132 °C edge\n$\rightarrow$ 1.5 K headroom\n\nFilm temperature (°C)\n\nA microporous CaCO$_{3}$-filled PE film loses WVTR irreversibly once the drawn structure anneals — typically above 90 °C. You will not see it on the line; you will see it in the humidity chamber a week later.\n\nFitting a chilled backing roll moves the ceiling up by roughly 15 K and is far cheaper than reformulating for a lower application temperature.\n\nMANDATORY TEST\n\nWVTR (ASTM E96) on coated vs uncoated film, and hydrohead, at every temperature set point in the window.\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/8c8c6b15-2293-4913-9ec4-583f5dbff8b9.png)
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

![CROSS-SECTION\n\nOuter nonwoven ≥ 50% transmittance\n\nComposite breathable film 30-80%\n\nBMLANE 20 gsm · 10 mm · violet\n\nCore wrap / dusting layer\n\nAbsorbent core — low-basis-weight conduit\n\nAcquisition / distribution layer\n\nTopsheet\n\nTHE FALSE-NEGATIVE PROBLEM\n\nStool carries far less free water than urine, so it will not reach a lane sitting behind a full-basis-weight core. Cut a 12 mm wide, SAP-free conduit through the core directly above the BM lane and put a diffusion layer between core and lane. Without that conduit the chemistry is irrelevant — the lane simply never sees protein.\n\nPLAN VIEW (non-skin side)\n\nBACK\n\nFRONT\n\nBM lane\n\n10 × 200 mm · straddles the fold line, so an unreacted section remains for a two-tone read\n\nUrine lanes\n\n2 × 6 mm in the crotch, 25 mm clear of the BM lane\n\nTemperature lane\n\nWaistband only — separate circuit, separate melter\n\nRear placement is deliberate — stool pools posteriorly whether the baby is lying or standing.\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/6b4b5885-f4f7-467e-8608-ecf34d3321c3.png)
## THE FALSE-NEGATIVE PROBLEM

Stool carries far less free water than urine, so it will not reach a lane sitting behind a full-basis-weight core. Cut a 12 mm wide, SAP-free conduit through the core directly above the BM lane and put a diffusion layer between core and lane. Without that conduit the chemistry is irrelevant — the lane simply never sees protein.

### PLAN VIEW (non-skin side)

![BACK\n\nFRONT\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/17c5b3b3-e618-4d93-bfac-3215f85a1b15.png)
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

![Zeolite (4A / 13X)\n\npH 9-11\n\nHIGH\n\nStrongly alkaline slurry. Will titrate the buffer through the dusting layer over shelf life.\n\nSodium bicarbonate\n\npH 8.3\n\nHIGH\n\nMobile, water-soluble, migrates readily. Worst case for a buffered lane.\n\nActivated carbon\n\npH 6-10\n\nMEDIUM\n\nGrade-dependent alkalinity, and it adsorbs the dye — expect greying as well as drift.\n\nCyclodextrin\n\npH 6-7\n\nLOW\n\nNeutral, non-migrating. The compatible choice if the odour performance holds.\n\nIon-exchange resin, H⁺ form\n\npH 4-6\n\nLOW\n\nAcidic form is actively helpful — it reinforces the lane's own buffer.\n\nSCREEN IT FIRST\n\nBefore any coating trial, run this:\n\n1 Slurry 5 g granular in 50 mL deionised water, 1 h, 25 °C. Measure pH and titratable base to pH 4.\n\n2 Accept only if slurry pH ≤ 7.5 and titratable base ≤ 0.2 mmol/g.\n\n3 Build a full diaper and age it 8 weeks at 40 °C / 75 % RH. Grade the lane weekly on a 0-5 scale; reject at grade 1.\n\n4 If the granular fails, the fix is a barrier — move it above the core wrap, or micro-encapsulate it — not more acid in the lane.\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/4350990d-02c4-4bc1-97e9-34957f168322.png)
ECONOMICS

# Cost impact: 0.056 US cents per diaper

![Total ≈ $0.57 per 1 000 = 0.057 US cents per diaper\n\nUSD per 1 000 diapers\n\n0.30\n\n0.25\n\n0.20\n\n0.15\n\n0.10\n\n0.05\n\n0.00\n\nIndicator material\n\nApplicator capex (3 y)\n\nOEE loss 0.30%\n\nMelter energy + purge\n\nFilm / graphic re-spec\n\nCapex, core scope\n\nCapex with colour verification\n\nAmortised over 707 M diapers (3 y)\n\n$0.109\n\n$0.045\n\nOEE allowance, 0.30%\n\n$0.240$\n\nFilm / graphic re-spec\n\nTotal\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/4bdb2991-fbad-4b87-9041-e362a23b9a03.png)
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

![WEEKS 1-2\n\nScreen the odour granular\n\nSlurry pH and titratable base on every candidate. Go / no-go before any spend.\n\nWEEKS 3-6\n\nBench formulation\n\nThree dye loadings × two buffer levels. Protein ladder plus urine challenge on hand-drawn films.\n\nWEEKS 7-9\n\nPilot coater\n\nConfirm the viscosity spec on a capillary rheometer; coat at 100-200 m/min; WVTR and hydrohead.\n\nWEEKS 10-13\n\nLine trial\n\nContact nozzle plus chilled roll on one lane. Coat-weight Cpk, 8-week ageing pull, stool panel.\n\nTOP RISKS\n\nAlkaline odour granular pre-develops the lane\n\nHIGH\n\nLow-basis-weight conduit plus diffusion layer; validate on real stool, not synthetic\n\nHIGH\n\nSpecify organodlay; audit the supplier's base formulation\n\nMEDIUM\n\nChilled backing roll; cap at 132 °C; WVTR at every set point\n\nFilm WVTR loss from thermal load\n\nFreedom to operate around granted feces-indicator claims\n\nMEDIUM\n\nFormal FTO on US 12,396,899 and family before pilot spend\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/763c9563-90e5-4abc-a3b7-cb008a8c61fe.png)
### TOP RISKS

![Alkaline odour granular pre-develops the lane\n\nHIGH\n\nScreen in week 1; barrier or encapsulate; do not compensate with acid\n\nFaecal liquid never reaches the lane\n\nHIGH\n\nLow-basis-weight conduit plus diffusion layer; validate on real stool, not synthetic\n\nSoluble quat in a carried-over WI base develops the dye\n\nMEDIUM\n\nSpecify organodlay; audit the supplier's base formulation\n\nFilm WVTR loss from thermal load\n\nMEDIUM\n\nChilled backing roll; cap at 132 °C; WVTR at every set point\n\nFreedom to operate around granted feces-indicator claims\n\nMEDIUM\n\nFormal FTO on US 12,396,899 and family before pilot spend\n](2/Oy0YFe4o874ND9Udefofxe/ppt_3867e2b60070d7dc3f413086d0b0036e_b3dda467472a596f8591596a63ca11cf001a693ee6c0644e/tmp_zip_img/178c7b61-1815-4ade-99a6-ea0c97e23b8f.png)
